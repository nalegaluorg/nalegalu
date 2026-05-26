# Test Results

**Status:** PASSED
**Run:** 2026-05-26 03:51 UTC
**Scope:** unit
**Total:** 96 tests — 96 passed, 0 failed, 0 errors, 33 skipped

## Summary by module

| Module | Tests | Status |
|--------|------:|--------|
| e2e parity | 4 | 4 skipped (e2e) |
| e2e parity | 4 | 4 skipped (e2e) |
| e2e parity | 12 | 12 skipped (e2e) |
| e2e parity | 6 | 6 skipped (e2e) |
| e2e parity | 5 | 5 skipped (e2e) |
| e2e sources | 2 | 2 skipped (e2e) |
| eli parity | 2 | all passed |
| eli parity | 6 | all passed |
| eli parity | 5 | all passed |
| eli parity | 7 | all passed |
| pdf download | 9 | all passed |
| pdf download | 3 | all passed |
| quality gate | 9 | all passed |
| quality gate | 3 | all passed |
| quality gate | 2 | all passed |
| quality gate | 3 | all passed |
| quality gate | 2 | all passed |
| quality gate | 3 | all passed |
| saos | 5 | all passed |
| saos | 6 | all passed |
| saos | 9 | all passed |
| saos | 10 | all passed |
| saos | 4 | all passed |
| saos | 8 | all passed |

## Full output

```
============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0 -- /opt/homebrew/opt/python@3.14/bin/python3.14
cachedir: .pytest_cache
rootdir: /Users/michal/repos/nalegaluorg
collecting ... collected 129 items

tests/test_e2e_parity.py::TestFrontMatterParity::test_same_keys SKIPPED  [  0%]
tests/test_e2e_parity.py::TestFrontMatterParity::test_address_matches SKIPPED [  1%]
tests/test_e2e_parity.py::TestFrontMatterParity::test_eli_field_matches SKIPPED [  2%]
tests/test_e2e_parity.py::TestFrontMatterParity::test_source_field_differs SKIPPED [  3%]
tests/test_e2e_parity.py::TestStructureParity::test_same_article_count SKIPPED [  3%]
tests/test_e2e_parity.py::TestStructureParity::test_same_article_markers SKIPPED [  4%]
tests/test_e2e_parity.py::TestStructureParity::test_same_division_count SKIPPED [  5%]
tests/test_e2e_parity.py::TestStructureParity::test_same_division_numbers SKIPPED [  6%]
tests/test_e2e_parity.py::TestStructureParity::test_same_paragraph_count SKIPPED [  6%]
tests/test_e2e_parity.py::TestContentParity::test_article_text_identical SKIPPED [  7%]
tests/test_e2e_parity.py::TestContentParity::test_przepisy_zmieniajace_present_in_both SKIPPED [  8%]
tests/test_e2e_parity.py::TestContentParity::test_first_article_text SKIPPED [  9%]
tests/test_e2e_parity.py::TestContentParity::test_last_article_text SKIPPED [ 10%]
tests/test_e2e_parity.py::TestRenderedParity::test_both_have_bold_article_markers SKIPPED [ 10%]
tests/test_e2e_parity.py::TestRenderedParity::test_both_have_metadata_table SKIPPED [ 11%]
tests/test_e2e_parity.py::TestRenderedParity::test_both_have_division_headings SKIPPED [ 12%]
tests/test_e2e_parity.py::TestRenderedParity::test_no_url_links_in_body SKIPPED [ 13%]
tests/test_e2e_parity.py::TestRenderedParity::test_body_text_similarity SKIPPED [ 13%]
tests/test_e2e_parity.py::TestRenderedParity::test_body_length_identical SKIPPED [ 14%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_count_matches[DU-2024-1976] SKIPPED [ 15%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_count_matches[DU-2024-1975] SKIPPED [ 16%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_count_matches[DU-2024-1781] SKIPPED [ 17%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_count_matches[DU-2024-1559] SKIPPED [ 17%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_markers_match[DU-2024-1976] SKIPPED [ 18%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_markers_match[DU-2024-1975] SKIPPED [ 19%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_markers_match[DU-2024-1781] SKIPPED [ 20%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_markers_match[DU-2024-1559] SKIPPED [ 20%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_text_matches[DU-2024-1976] SKIPPED [ 21%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_text_matches[DU-2024-1975] SKIPPED [ 22%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_text_matches[DU-2024-1781] SKIPPED [ 23%]
tests/test_e2e_parity.py::TestQuickCheckParity::test_article_text_matches[DU-2024-1559] SKIPPED [ 24%]
tests/test_e2e_sources.py::test_pdf_and_eli_html_sources_publish_comparable_output SKIPPED [ 24%]
tests/test_e2e_sources.py::test_sources_publish_kodeks_cywilny SKIPPED   [ 25%]
tests/test_eli_parity.py::TestHtmlToSegments::test_strips_heading_markers PASSED [ 26%]
tests/test_eli_parity.py::TestHtmlToSegments::test_strips_url_links PASSED [ 27%]
tests/test_eli_parity.py::TestHtmlToSegments::test_strips_list_markers PASSED [ 27%]
tests/test_eli_parity.py::TestHtmlToSegments::test_empty_html_returns_empty PASSED [ 28%]
tests/test_eli_parity.py::TestHtmlToSegments::test_sample_produces_valid_segments PASSED [ 29%]
tests/test_eli_parity.py::TestASTFromELI::test_articles_parsed PASSED    [ 30%]
tests/test_eli_parity.py::TestASTFromELI::test_division_parsed PASSED    [ 31%]
tests/test_eli_parity.py::TestOutputParity::test_front_matter_keys_match PASSED [ 31%]
tests/test_eli_parity.py::TestOutputParity::test_eli_md_has_bold_article_markers PASSED [ 32%]
tests/test_eli_parity.py::TestOutputParity::test_eli_md_has_division_headings PASSED [ 33%]
tests/test_eli_parity.py::TestOutputParity::test_eli_md_has_metadata_table PASSED [ 34%]
tests/test_eli_parity.py::TestOutputParity::test_eli_md_has_source_field PASSED [ 34%]
tests/test_eli_parity.py::TestOutputParity::test_no_url_links_in_body PASSED [ 35%]
tests/test_eli_parity.py::TestOutputParity::test_eli_txt_matches_isap_format PASSED [ 36%]
tests/test_eli_parity.py::TestChooseSource::test_pdf_available_uses_isap PASSED [ 37%]
tests/test_eli_parity.py::TestChooseSource::test_pdf_available_with_consolidated_uses_isap PASSED [ 37%]
tests/test_eli_parity.py::TestChooseSource::test_no_pdf_with_eli_uses_eli PASSED [ 38%]
tests/test_eli_parity.py::TestChooseSource::test_no_pdf_no_eli_uses_isap PASSED [ 39%]
tests/test_eli_parity.py::TestChooseSource::test_pdf_only_no_eli_uses_isap PASSED [ 40%]
tests/test_eli_parity.py::TestChooseSource::test_empty_texts_no_pdf_with_eli_uses_eli PASSED [ 41%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_prefers_U_over_O PASSED [ 41%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_prefers_T_when_no_U PASSED [ 42%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_prefers_U_over_T_and_O PASSED [ 43%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_falls_back_to_O_when_only_O PASSED [ 44%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_falls_back_to_api_when_empty_texts PASSED [ 44%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_url_uses_isap_download_base PASSED [ 45%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_url_contains_address PASSED [ 46%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_ignores_entries_without_type PASSED [ 47%]
tests/test_pdf_download.py::TestBestPdfTypeAndUrl::test_ignores_entries_without_filename PASSED [ 48%]
tests/test_pdf_download.py::TestEpubTtsPlanParts::test_czesc_at_top_level_creates_separate_parts PASSED [ 48%]
tests/test_pdf_download.py::TestEpubTtsPlanParts::test_ksiega_still_works PASSED [ 49%]
tests/test_pdf_download.py::TestEpubTtsPlanParts::test_dzial_still_works PASSED [ 50%]
tests/test_quality_gate.py::TestBasicChecks::test_clean_content_passes PASSED [ 51%]
tests/test_quality_gate.py::TestBasicChecks::test_cid_font_corruption_blocked PASSED [ 51%]
tests/test_quality_gate.py::TestBasicChecks::test_single_cid_still_blocked PASSED [ 52%]
tests/test_quality_gate.py::TestBasicChecks::test_null_bytes_blocked PASSED [ 53%]
tests/test_quality_gate.py::TestBasicChecks::test_empty_body_blocked PASSED [ 54%]
tests/test_quality_gate.py::TestBasicChecks::test_body_with_only_whitespace_blocked PASSED [ 55%]
tests/test_quality_gate.py::TestBasicChecks::test_no_front_matter_still_checks_body PASSED [ 55%]
tests/test_quality_gate.py::TestBasicChecks::test_no_front_matter_empty_blocked PASSED [ 56%]
tests/test_quality_gate.py::TestBasicChecks::test_multiple_issues_all_reported PASSED [ 57%]
tests/test_quality_gate.py::TestMojibakeDetection::test_mojibake_blocked PASSED [ 58%]
tests/test_quality_gate.py::TestMojibakeDetection::test_single_mojibake_not_false_positive PASSED [ 58%]
tests/test_quality_gate.py::TestPostScriptCEResidual::test_postscript_ce_markers_blocked PASSED [ 59%]
tests/test_quality_gate.py::TestPostScriptCEResidual::test_clean_polish_not_flagged PASSED [ 60%]
tests/test_quality_gate.py::TestPDFArtifacts::test_kancelaria_sejmu_header PASSED [ 61%]
tests/test_quality_gate.py::TestPDFArtifacts::test_date_stamp_footer PASSED [ 62%]
tests/test_quality_gate.py::TestPDFArtifacts::test_date_inline_not_flagged PASSED [ 62%]
tests/test_quality_gate.py::TestDiacriticsDensity::test_ascii_only_text_blocked PASSED [ 63%]
tests/test_quality_gate.py::TestDiacriticsDensity::test_proper_polish_passes PASSED [ 64%]
tests/test_quality_gate.py::TestDiacriticsDensity::test_short_text_skips_diacritics_check PASSED [ 65%]
tests/test_quality_gate.py::TestRepetitionDetection::test_repeated_header_blocked PASSED [ 65%]
tests/test_quality_gate.py::TestRepetitionDetection::test_short_repeated_lines_ignored PASSED [ 66%]
tests/test_quality_gate.py::TestRepetitionDetection::test_normal_text_no_false_positive PASSED [ 67%]
tests/test_saos.py::TestModels::test_judgment_properties PASSED          [ 68%]
tests/test_saos.py::TestModels::test_referenced_regulation_isap_address PASSED [ 68%]
tests/test_saos.py::TestModels::test_referenced_regulation_empty_address PASSED [ 69%]
tests/test_saos.py::TestModels::test_judge_roles PASSED                  [ 70%]
tests/test_saos.py::TestApiConversion::test_basic_conversion PASSED      [ 71%]
tests/test_saos.py::TestApiConversion::test_referenced_regulations PASSED [ 72%]
tests/test_saos.py::TestApiConversion::test_missing_fields PASSED        [ 72%]
tests/test_saos.py::TestApiConversion::test_save_load_json PASSED        [ 73%]
tests/test_saos.py::TestApiConversion::test_load_missing_json PASSED     [ 74%]
tests/test_saos.py::TestHtmlConversion::test_basic_paragraphs PASSED     [ 75%]
tests/test_saos.py::TestHtmlConversion::test_bold_italic PASSED          [ 75%]
tests/test_saos.py::TestHtmlConversion::test_unordered_list PASSED       [ 76%]
tests/test_saos.py::TestHtmlConversion::test_ordered_list PASSED         [ 77%]
tests/test_saos.py::TestHtmlConversion::test_headings PASSED             [ 78%]
tests/test_saos.py::TestHtmlConversion::test_strips_style_script PASSED  [ 79%]
tests/test_saos.py::TestHtmlConversion::test_br_tag PASSED               [ 79%]
tests/test_saos.py::TestHtmlConversion::test_empty_html PASSED           [ 80%]
tests/test_saos.py::TestHtmlConversion::test_sample_judgment_html PASSED [ 81%]
tests/test_saos.py::TestHtmlConversion::test_nonbreaking_space_cleanup PASSED [ 82%]
tests/test_saos.py::TestRendering::test_front_matter PASSED              [ 82%]
tests/test_saos.py::TestRendering::test_title_and_metadata PASSED        [ 83%]
tests/test_saos.py::TestRendering::test_judges_table PASSED              [ 84%]
tests/test_saos.py::TestRendering::test_keywords PASSED                  [ 85%]
tests/test_saos.py::TestRendering::test_content_included PASSED          [ 86%]
tests/test_saos.py::TestRendering::test_referenced_acts_with_links PASSED [ 86%]
tests/test_saos.py::TestRendering::test_referenced_acts_without_links PASSED [ 87%]
tests/test_saos.py::TestRendering::test_no_references PASSED             [ 88%]
tests/test_saos.py::TestDatabase::test_upsert_and_get PASSED             [ 89%]
tests/test_saos.py::TestDatabase::test_get_nonexistent PASSED            [ 89%]
tests/test_saos.py::TestDatabase::test_set_stage PASSED                  [ 90%]
tests/test_saos.py::TestDatabase::test_set_stage_with_error PASSED       [ 91%]
tests/test_saos.py::TestDatabase::test_list_by_stage PASSED              [ 92%]
tests/test_saos.py::TestDatabase::test_summary PASSED                    [ 93%]
tests/test_saos.py::TestDatabase::test_count_by_court PASSED             [ 93%]
tests/test_saos.py::TestDatabase::test_sync_meta PASSED                  [ 94%]
tests/test_saos.py::TestDatabase::test_upsert_preserves_stage PASSED     [ 95%]
tests/test_saos.py::TestCrossRef::test_parse_single_article PASSED       [ 96%]
tests/test_saos.py::TestCrossRef::test_parse_multiple_articles PASSED    [ 96%]
tests/test_saos.py::TestCrossRef::test_parse_paragraphs PASSED           [ 97%]
tests/test_saos.py::TestCrossRef::test_parse_article_with_superscript PASSED [ 98%]
tests/test_saos.py::TestCrossRef::test_parse_no_articles PASSED          [ 99%]
tests/test_saos.py::TestCrossRef::test_render_crossref_md PASSED         [100%]

======================== 96 passed, 33 skipped in 0.17s ========================
```
