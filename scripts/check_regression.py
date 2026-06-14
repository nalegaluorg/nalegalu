#!/usr/bin/env python3
"""
Public-repo regression checker: compare changed .md act files in a PR
against the base branch (main).

Runs as a GitHub Actions step on the public nalegalu repo. No pipeline
dependencies — just git + Python stdlib.

Flags regressions:
  - File size decreased >10% (content was lost)
  - Article count decreased (parser dropped articles)
  - Quality gate failures (corruption introduced)

Usage:
  # In a PR branch, compare against main:
  python3 scripts/check_regression.py

  # Compare against a specific base:
  python3 scripts/check_regression.py --base origin/main

  # Write JSON results for CI:
  python3 scripts/check_regression.py --output results.json

Exit codes:
  0 — all changed acts equal or improved
  1 — regressions detected
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Quality gate checks (standalone, no pipeline imports needed)
# ---------------------------------------------------------------------------

_POLISH_DIACRITICS = set("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ")
_MIN_BODY_LENGTH = 50
_DIACRITICS_CHECK_MIN_LENGTH = 500
_DIACRITICS_MIN_RATIO = 0.005  # 0.5%
_MAX_LINE_REPEATS = 20
_MIN_LINE_LENGTH_FOR_REPEAT_CHECK = 20

# PostScript CE garbled diacritics
_POSTSCRIPT_CE_RE = re.compile(
    r"(?:uÊtaw|okreÊl|Êwiadcz|przest[ąa]p|uÊ[łl]ug|miesiÊc"
    r"|∏[aeoóu]|∏[ąa]cz|wy∏[ąa]cz|ƒ[aeiou]|à[cklmnprst])"
)

# Mojibake: UTF-8 Polish diacritics decoded as Latin-1/CP1252
_MOJIBAKE_SEQUENCES = [
    "".join(chr(b) for b in ch.encode("utf-8"))
    for ch in "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
]
_MOJIBAKE_RE = re.compile("|".join(re.escape(s) for s in _MOJIBAKE_SEQUENCES))

# PDF artifacts
_PDF_HEADER_RE = re.compile(r"©\s*Kancelaria Sejmu")
_PDF_DATE_RE = re.compile(r"^\d{2}/\d{2}/\d{2,4}\s*$", re.MULTILINE)

# Single letters that are legitimate Polish words
_LEGIT_SINGLE = {"i", "w", "z", "o", "u", "a"}

# Article marker pattern
_ARTICLE_RE = re.compile(r"\*\*Art\.\s+\d+")


def get_body(md_content: str) -> str:
    """Extract body excluding YAML front matter."""
    if md_content.startswith("---"):
        parts = md_content.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return md_content.strip()


def count_articles(md_content: str) -> int:
    """Count article markers in markdown content."""
    return len(_ARTICLE_RE.findall(md_content))


def quality_check(content: str) -> list[str]:
    """Run quality gate checks on markdown content. Returns list of issues."""
    issues: list[str] = []
    content_bytes = content.encode("utf-8")

    # CID font
    cid_matches = re.findall(rb"\(cid:\d+\)", content_bytes)
    if cid_matches:
        issues.append(f"CID font ({len(cid_matches)} occurrences)")

    # Null bytes
    null_matches = re.findall(rb"\x00", content_bytes)
    if null_matches:
        issues.append(f"null bytes ({len(null_matches)} occurrences)")

    body = get_body(content)

    # Empty body
    if len(body) < _MIN_BODY_LENGTH:
        issues.append(f"body too short ({len(body)} chars)")
        return issues

    # PostScript CE
    ps_matches = _POSTSCRIPT_CE_RE.findall(body)
    if ps_matches:
        issues.append(f"PostScript CE garbled ({len(ps_matches)} occurrences)")

    # Mojibake
    moji_matches = _MOJIBAKE_RE.findall(body)
    if len(moji_matches) >= 3:
        issues.append(f"mojibake ({len(moji_matches)} occurrences)")

    # PDF artifacts
    if _PDF_HEADER_RE.findall(body):
        issues.append("PDF header artifact")
    date_matches = _PDF_DATE_RE.findall(body)
    if date_matches:
        issues.append(f"PDF date stamp ({len(date_matches)} occurrences)")

    # Table garbage
    table_garbage = 0
    for line in body.splitlines():
        stripped = line.strip()
        if len(stripped) < 20:
            continue
        pipe_slash = sum(1 for c in stripped if c in "|/")
        if pipe_slash / len(stripped) > 0.25:
            table_garbage += 1
    if table_garbage >= 3:
        issues.append(f"table garbage ({table_garbage} lines)")

    # Diacritics density
    if len(body) >= _DIACRITICS_CHECK_MIN_LENGTH:
        letters = [c for c in body if c.isalpha()]
        if letters:
            diac = sum(1 for c in letters if c in _POLISH_DIACRITICS)
            ratio = diac / len(letters)
            if ratio < _DIACRITICS_MIN_RATIO:
                issues.append(f"missing diacritics ({ratio:.2%})")

    # Character-spaced text
    spaced_lines = 0
    for line in body.splitlines():
        words = line.split()
        if len(words) < 10:
            continue
        singles = sum(
            1 for w in words
            if len(w) == 1 and w.isalpha() and w.lower() not in _LEGIT_SINGLE
        )
        if singles / len(words) > 0.30:
            spaced_lines += 1
    if spaced_lines > 0:
        issues.append(f"character-spaced ({spaced_lines} lines)")

    # Repetition
    line_counts: dict[str, int] = {}
    for line in body.splitlines():
        stripped = line.strip()
        if len(stripped) < _MIN_LINE_LENGTH_FOR_REPEAT_CHECK:
            continue
        if stripped.startswith(("#", "**Art.", "§", "- **", "- ")):
            continue
        line_counts[stripped] = line_counts.get(stripped, 0) + 1
    repeated = {l: c for l, c in line_counts.items() if c > _MAX_LINE_REPEATS}
    if repeated:
        worst = max(repeated, key=repeated.get)
        short = (worst[:50] + "...") if len(worst) > 50 else worst
        issues.append(f"repetition: '{short}' x{repeated[worst]}")

    return issues


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def git(*args: str) -> str:
    """Run a git command and return stdout."""
    result = subprocess.run(
        ["git"] + list(args),
        capture_output=True, text=True, check=True
    )
    return result.stdout


def get_changed_md_files(base: str) -> list[str]:
    """Get list of .md files changed in the current branch vs base."""
    try:
        diff_output = git("diff", "--name-only", "--diff-filter=AM", base,
                          "--", "*.md", "**/*.md")
    except subprocess.CalledProcessError:
        # Try merge-base
        try:
            merge_base = git("merge-base", "HEAD", base).strip()
            diff_output = git("diff", "--name-only", "--diff-filter=AM",
                              merge_base, "--", "*.md", "**/*.md")
        except subprocess.CalledProcessError:
            print("ERROR: could not determine changed files")
            return []

    files = [f for f in diff_output.strip().splitlines() if f]
    # Filter to act files — skip repo meta files
    skip = {"README", "CHANGELOG", "BLOCKED_ACTS", "PUBLISH_SUMMARY",
            "TEST_RESULTS"}
    # SAOS case-law cross-reference tables (orzecznictwo.md) are not act
    # bodies, so the size/article/diacritics gates below — which are tuned
    # for PDF-extracted legal prose — misfire on them:
    #   - "missing diacritics" on ASCII judgment metadata (case signatures,
    #     court codes, saos.org.pl URLs, scores); ratio is ~0.15% by nature.
    #   - large but legitimate size swings: e.g. the compact format moved
    #     inline judgments out into per-article orzecznictwo/*.csv siblings,
    #     shrinking the .md ~70% while preserving every judgment.
    # The judgment data lives in orzecznictwo/*.csv (not *.md, so already
    # outside this checker). Exclude the index file by name.
    saos_crossref_names = {"orzecznictwo.md"}
    return [f for f in files
            if Path(f).name not in saos_crossref_names
            and not any(s in Path(f).stem.upper() for s in skip)]


def get_base_content(base: str, filepath: str) -> str | None:
    """Get file content from the base branch. Returns None if file is new."""
    try:
        return git("show", f"{base}:{filepath}")
    except subprocess.CalledProcessError:
        return None


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

def compare_file(filepath: str, base: str) -> dict:
    """Compare current file against base branch version."""
    new_content = Path(filepath).read_text(encoding="utf-8")
    old_content = get_base_content(base, filepath)

    new_body_size = len(get_body(new_content))
    new_articles = count_articles(new_content)
    new_quality = quality_check(new_content)

    result = {
        "file": filepath,
        "new_size": new_body_size,
        "new_articles": new_articles,
        "new_quality_issues": new_quality,
        "is_new": old_content is None,
        "regression": False,
        "reasons": [],
    }

    if old_content is None:
        # New file — just check quality
        if new_quality:
            result["regression"] = True
            result["reasons"].append(f"quality: {'; '.join(new_quality[:3])}")
        return result

    old_body_size = len(get_body(old_content))
    old_articles = count_articles(old_content)
    old_quality = quality_check(old_content)

    result["old_size"] = old_body_size
    result["old_articles"] = old_articles
    result["old_quality_issues"] = old_quality

    size_delta = new_body_size - old_body_size
    size_pct = (size_delta / old_body_size * 100) if old_body_size > 0 else 0
    art_delta = new_articles - old_articles

    result["size_delta"] = size_delta
    result["size_pct"] = size_pct
    result["articles_delta"] = art_delta

    # Regression: significant size shrinkage
    if old_body_size > 0 and new_body_size < old_body_size * 0.9:
        result["regression"] = True
        result["reasons"].append(
            f"size shrank {old_body_size:,} -> {new_body_size:,} ({size_pct:+.1f}%)"
        )

    # Regression: lost articles
    if new_articles < old_articles:
        result["regression"] = True
        result["reasons"].append(
            f"articles dropped {old_articles} -> {new_articles} ({art_delta:+d})"
        )

    # Regression: new quality issues that didn't exist before
    new_issue_types = set(new_quality) - set(old_quality)
    if new_issue_types:
        result["regression"] = True
        result["reasons"].append(
            f"new quality issues: {'; '.join(list(new_issue_types)[:3])}"
        )

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Check for regressions in changed act files")
    parser.add_argument(
        "--base", default="origin/main",
        help="Base ref to compare against (default: origin/main)")
    parser.add_argument(
        "--output", default=None,
        help="Write JSON results to this file")
    parser.add_argument(
        "--max-files", type=int, default=500,
        help="Max files to check (default: 500)")
    args = parser.parse_args()

    # Make sure we have the base ref
    try:
        git("rev-parse", "--verify", args.base)
    except subprocess.CalledProcessError:
        try:
            git("fetch", "origin", "main", "--depth=1")
        except subprocess.CalledProcessError:
            print("WARNING: could not fetch origin/main")

    changed = get_changed_md_files(args.base)
    if not changed:
        print("No act files changed — nothing to check.")
        sys.exit(0)

    if len(changed) > args.max_files:
        print(f"WARNING: {len(changed)} files changed, "
              f"checking first {args.max_files}")
        changed = changed[:args.max_files]

    print(f"Regression check: {len(changed)} changed act files vs {args.base}")
    print()

    results = []
    regressions = 0
    improved = 0
    new_files = 0

    for i, filepath in enumerate(changed, 1):
        short = filepath if len(filepath) < 60 else "..." + filepath[-57:]
        print(f"[{i}/{len(changed)}] {short}", end="  ")

        if not Path(filepath).exists():
            print("SKIP (not on disk)")
            continue

        result = compare_file(filepath, args.base)
        results.append(result)

        if result["is_new"]:
            new_files += 1
            if result["regression"]:
                regressions += 1
                print(f"NEW + ISSUES: {', '.join(result['reasons'])}")
            else:
                print("NEW (ok)")
        elif result["regression"]:
            regressions += 1
            print(f"REGRESSION: {', '.join(result['reasons'])}")
        else:
            delta = result.get("size_delta", 0)
            art_delta = result.get("articles_delta", 0)
            pct = result.get("size_pct", 0)
            if delta > 0 or art_delta > 0:
                improved += 1
                print(f"IMPROVED: size {pct:+.1f}%, articles {art_delta:+d}")
            else:
                print(f"OK: size {pct:+.1f}%, articles {art_delta:+d}")

    # Summary
    print()
    print("=" * 60)
    checked = len(results)
    passed = checked - regressions
    print(f"Results: {checked} checked, {passed} passed, "
          f"{regressions} regressions, {improved} improved, "
          f"{new_files} new")

    if regressions:
        print()
        print("REGRESSIONS:")
        for r in results:
            if r["regression"]:
                print(f"  {r['file']}")
                for reason in r["reasons"]:
                    print(f"    - {reason}")

    # Write JSON
    if args.output:
        summary = {
            "total": len(changed),
            "checked": checked,
            "passed": passed,
            "regressions": regressions,
            "improved": improved,
            "new_files": new_files,
            "details": results,
        }
        Path(args.output).write_text(
            json.dumps(summary, indent=2, ensure_ascii=False))
        print(f"\nResults written to {args.output}")

    sys.exit(1 if regressions > 0 else 0)


if __name__ == "__main__":
    main()
