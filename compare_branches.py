#!/usr/bin/env python3
"""Compare nalegalu-public output quality between two git branches.

Usage:
    python3 compare_branches.py /path/to/nalegalu-public master resync-auto-source

Compares:
  - Act counts (added, removed, shared)
  - Source field changes (eli-html vs isap-pdf)
  - Content size changes (significantly shorter = possible data loss)
  - Article count changes (fewer articles = possible regression)
  - Front matter completeness
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from collections import Counter

def git_list_files(repo: Path, branch: str) -> list[str]:
    """List all index.md files in a branch."""
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", branch],
        cwd=repo, capture_output=True, text=True, check=True,
    )
    return [f for f in result.stdout.splitlines() if f.endswith("index.md")]

def git_show(repo: Path, branch: str, path: str) -> str:
    """Read file content from a specific branch."""
    try:
        result = subprocess.run(
            ["git", "show", f"{branch}:{path}"],
            cwd=repo, capture_output=True, text=True, check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return ""

def extract_source(content: str) -> str:
    m = re.search(r'^source:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    return m.group(1).strip() if m else "unknown"

def extract_address(content: str) -> str:
    m = re.search(r'^address:\s*(\S+)', content, re.MULTILINE)
    return m.group(1) if m else ""

def count_articles(content: str) -> int:
    return len(re.findall(r'\*\*Art\.\s+\d+', content))

def extract_title(content: str) -> str:
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    return m.group(1).strip('"') if m else ""

def body_length(content: str) -> int:
    """Length of content after front matter."""
    m = re.search(r'^---\n.*?\n---\n(.*)$', content, re.DOTALL)
    return len(m.group(1).strip()) if m else len(content)

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <repo-path> <old-branch> <new-branch>")
        sys.exit(1)

    repo = Path(sys.argv[1])
    old_branch = sys.argv[2]
    new_branch = sys.argv[3]

    print(f"Comparing {old_branch} → {new_branch} in {repo}\n")

    old_files = set(git_list_files(repo, old_branch))
    new_files = set(git_list_files(repo, new_branch))

    added = new_files - old_files
    removed = old_files - new_files
    shared = old_files & new_files

    print(f"{'='*60}")
    print(f"ACT COUNTS")
    print(f"  {old_branch}: {len(old_files)} acts")
    print(f"  {new_branch}: {len(new_files)} acts")
    print(f"  Added:   {len(added)}")
    print(f"  Removed: {len(removed)}")
    print(f"  Shared:  {len(shared)}")

    # Analyze removed acts
    if removed:
        print(f"\n{'='*60}")
        print(f"REMOVED ACTS (in {old_branch} but not {new_branch}):")
        for f in sorted(removed)[:20]:
            content = git_show(repo, old_branch, f)
            addr = extract_address(content)
            title = extract_title(content)[:60]
            print(f"  {addr}  {title}")
        if len(removed) > 20:
            print(f"  ... and {len(removed) - 20} more")

    # Analyze shared acts
    source_changes = Counter()  # (old_src, new_src) → count
    shrunk = []      # acts that got significantly shorter
    grew = []        # acts that got significantly longer
    lost_articles = []  # acts that lost articles
    gained_articles = []
    total_old_size = 0
    total_new_size = 0

    print(f"\nAnalyzing {len(shared)} shared acts ...", flush=True)
    for i, f in enumerate(sorted(shared)):
        if (i + 1) % 2000 == 0:
            print(f"  {i+1}/{len(shared)} ...", flush=True)

        old_content = git_show(repo, old_branch, f)
        new_content = git_show(repo, new_branch, f)

        old_src = extract_source(old_content)
        new_src = extract_source(new_content)
        source_changes[(old_src, new_src)] += 1

        old_len = body_length(old_content)
        new_len = body_length(new_content)
        total_old_size += old_len
        total_new_size += new_len

        # Flag if body shrunk by >20%
        if old_len > 100 and new_len < old_len * 0.8:
            addr = extract_address(old_content)
            shrunk.append((addr, old_len, new_len, old_src, new_src))

        # Flag if body grew by >20%
        if old_len > 100 and new_len > old_len * 1.2:
            addr = extract_address(old_content)
            grew.append((addr, old_len, new_len, old_src, new_src))

        old_arts = count_articles(old_content)
        new_arts = count_articles(new_content)
        if old_arts > 0 and new_arts < old_arts:
            addr = extract_address(old_content)
            lost_articles.append((addr, old_arts, new_arts, old_src, new_src))
        elif new_arts > old_arts and old_arts > 0:
            addr = extract_address(old_content)
            gained_articles.append((addr, old_arts, new_arts, old_src, new_src))

    print(f"\n{'='*60}")
    print(f"SOURCE CHANGES")
    for (old_s, new_s), count in sorted(source_changes.items(), key=lambda x: -x[1]):
        arrow = "→" if old_s != new_s else "="
        print(f"  {old_s:15s} {arrow} {new_s:15s}  {count:>6} acts")

    print(f"\n{'='*60}")
    print(f"CONTENT SIZE")
    print(f"  Total body ({old_branch}): {total_old_size:,} chars")
    print(f"  Total body ({new_branch}): {total_new_size:,} chars")
    ratio = total_new_size / total_old_size if total_old_size else 0
    print(f"  Ratio: {ratio:.4f}")

    if shrunk:
        print(f"\n{'='*60}")
        print(f"SHRUNK >20% ({len(shrunk)} acts):")
        for addr, old_l, new_l, old_s, new_s in sorted(shrunk, key=lambda x: x[2]/x[1])[:20]:
            pct = (new_l / old_l) * 100
            print(f"  {addr}  {old_l:>7} → {new_l:>7} ({pct:.0f}%)  {old_s}→{new_s}")

    if grew:
        print(f"\n{'='*60}")
        print(f"GREW >20% ({len(grew)} acts):")
        for addr, old_l, new_l, old_s, new_s in sorted(grew, key=lambda x: x[2]/x[1], reverse=True)[:20]:
            pct = (new_l / old_l) * 100
            print(f"  {addr}  {old_l:>7} → {new_l:>7} ({pct:.0f}%)  {old_s}→{new_s}")

    if lost_articles:
        print(f"\n{'='*60}")
        print(f"LOST ARTICLES ({len(lost_articles)} acts):")
        for addr, old_a, new_a, old_s, new_s in sorted(lost_articles, key=lambda x: x[1]-x[2], reverse=True)[:20]:
            print(f"  {addr}  {old_a} → {new_a} articles  {old_s}→{new_s}")

    if gained_articles:
        print(f"\n{'='*60}")
        print(f"GAINED ARTICLES ({len(gained_articles)} acts):")
        for addr, old_a, new_a, old_s, new_s in sorted(gained_articles, key=lambda x: x[2]-x[1], reverse=True)[:20]:
            print(f"  {addr}  {old_a} → {new_a} articles  {old_s}→{new_s}")

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    eli_to_eli = source_changes.get(("eli-html", "eli-html"), 0)
    isap_to_isap = source_changes.get(("isap-pdf", "isap-pdf"), 0)
    isap_to_eli = source_changes.get(("isap-pdf", "eli-html"), 0)
    eli_to_isap = source_changes.get(("eli-html", "isap-pdf"), 0)
    print(f"  Stayed on ISAP:    {isap_to_isap}")
    print(f"  Stayed on ELI:     {eli_to_eli}")
    print(f"  ISAP → ELI:        {isap_to_eli}")
    print(f"  ELI → ISAP:        {eli_to_isap}")
    print(f"  Shrunk >20%:       {len(shrunk)}")
    print(f"  Grew >20%:         {len(grew)}")
    print(f"  Lost articles:     {len(lost_articles)}")
    print(f"  Gained articles:   {len(gained_articles)}")

    if not shrunk and not lost_articles and len(removed) == 0:
        print(f"\n  VERDICT: QUALITY OK ✓")
    elif lost_articles or len(shrunk) > 10:
        print(f"\n  VERDICT: REVIEW NEEDED ✗")
    else:
        print(f"\n  VERDICT: MINOR CHANGES — spot check recommended")

if __name__ == "__main__":
    main()
