from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "measure_chapter_layout.py"
SPEC = importlib.util.spec_from_file_location("measure_chapter_layout", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ChapterLayoutMeasurementTests(unittest.TestCase):
    def test_split_pages_discards_only_trailing_empty_page(self):
        pages = MODULE.split_pages("page one\fpage two\f")

        self.assertEqual(pages, ["page one", "page two"])

    def test_extract_segment_uses_inclusive_start_and_exclusive_end_markers(self):
        pages = ["header\nSTART\nkeep one", "keep two\nEND\nfooter"]

        text = MODULE.extract_segment(
            pages,
            {"page_start": 1, "page_end": 2, "start_marker": "START", "end_marker": "END"},
        )

        self.assertEqual(text, "START\nkeep one\n\nkeep two")

    def test_extract_segment_can_exclude_heading_marker(self):
        text = MODULE.extract_segment(
            ["1 Introduction\nBody sentence."],
            {
                "page_start": 1,
                "page_end": 1,
                "start_marker": "1 Introduction",
                "include_start_marker": False,
            },
        )

        self.assertEqual(text, "Body sentence.")

    def test_measure_text_joins_line_break_hyphenation_and_reports_sentence_words(self):
        text = "A repro-\nducible model works. It reports one result.\n\nA boundary remains."

        result = MODULE.measure_text(text)

        self.assertEqual(result["word_count"], 11)
        self.assertEqual(result["sentence_count"], 3)
        self.assertEqual(result["paragraph_count"], 2)
        self.assertEqual(result["sentence_words"], {"minimum": 3, "median": 4, "maximum": 4})

    def test_indented_prose_line_starts_a_new_visual_paragraph(self):
        result = MODULE.measure_text(
            "First paragraph continues.\n    Second paragraph begins and\ncontinues."
        )

        self.assertEqual(result["paragraph_count"], 2)

    def test_decimal_points_do_not_split_sentences(self):
        result = MODULE.measure_text("The value is 18.21 cm. It changes by 0.72 percent.")

        self.assertEqual(result["sentence_count"], 2)

    def test_explicit_line_exclusions_remove_headings_from_counts(self):
        result = MODULE.measure_text(
            "1.1. Definition of a sweet spot\nBody sentence remains.",
            exclude_line_patterns=[r"^\d+(?:\.\d+)+\.?\s+.*$"],
        )

        self.assertEqual(result["sentence_count"], 1)
        self.assertEqual(result["word_count"], 3)

    def test_plot_label_without_sentence_boundary_is_not_a_prose_paragraph(self):
        result = MODULE.measure_text(
            "Body sentence remains.\n    tip of the bat\n    Another result follows."
        )

        self.assertEqual(result["paragraph_count"], 2)
        self.assertEqual(result["word_count"], 6)

    def test_nonprose_segment_returns_explicit_zero_draft_counts(self):
        result = MODULE.measure_text("45 50 55\n    tip of the bat")

        self.assertEqual(result["word_count"], 0)
        self.assertEqual(result["sentence_count"], 0)
        self.assertEqual(result["paragraph_count"], 0)
        self.assertIsNone(result["sentence_words"])

    def test_excluded_table_heading_preserves_preceding_prose_boundary(self):
        result = MODULE.measure_text(
            "The source data are listed below.\nTable 2 Data used for simulation\nMass Value 0.885",
            exclude_line_patterns=[r"^Table\s+\d+.*$"],
        )

        self.assertEqual(result["paragraph_count"], 1)
        self.assertEqual(result["word_count"], 6)

    def test_missing_marker_is_an_explicit_error(self):
        with self.assertRaisesRegex(ValueError, "start_marker"):
            MODULE.extract_segment(
                ["page text"],
                {"page_start": 1, "page_end": 1, "start_marker": "absent"},
            )

    def test_spec_can_exclude_all_chapter_headings_by_default(self):
        result = MODULE.measure_spec(
            "1 Introduction\nBody sentence has four words.",
            {
                "paper_id": "P-A-test",
                "technical_page_denominator": 1,
                "include_start_markers": False,
                "chapters": [
                    {
                        "chapter": "introduction",
                        "segments": [
                            {"page_start": 1, "page_end": 1, "start_marker": "1 Introduction"}
                        ],
                    }
                ],
            },
        )

        self.assertEqual(result["chapter_layout_drafts"][0]["word_count"], 5)


if __name__ == "__main__":
    unittest.main()
