from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "summarize_language_layouts.py"
SPEC = importlib.util.spec_from_file_location("summarize_language_layouts", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def record(paper_id: str, year: str, words: int, sentences: int) -> dict[str, object]:
    return {
        "schema_version": 3,
        "paper_id": paper_id,
        "problem_type": "A",
        "year": year,
        "chapter_layouts": [
            {
                "chapter": "abstract",
                "word_count": words,
                "sentence_count": sentences,
                "paragraph_count": 5,
                "page_fraction": 0.04,
            }
        ],
    }


class LanguageLayoutSummaryTests(unittest.TestCase):
    def test_summary_reports_distribution_and_era_boundary(self):
        summaries = MODULE.summarize_records(
            [
                record("P-A-2010-one", "2010", 100, 10),
                record("P-A-2012-two", "2012", 200, 20),
            ],
            problem_type="A",
        )

        words = next(
            item for item in summaries if item["chapter"] == "abstract" and item["unit"] == "word"
        )
        self.assertEqual(words["sample_size"], 2)
        self.assertEqual(words["observed_range"], {"minimum": 100, "maximum": 200})
        self.assertEqual(words["median"], 150)
        self.assertEqual(words["quartiles"], {"q1": 125, "q3": 175, "iqr": 50})
        self.assertEqual(words["era"], {"start_year": "2010", "end_year": "2012"})

    def test_legacy_v2_records_are_not_aggregated(self):
        legacy = record("P-A-2010-old", "2010", 100, 10)
        legacy["schema_version"] = 2

        self.assertEqual(MODULE.summarize_records([legacy], problem_type="A"), [])

    def test_duplicate_paper_ids_are_rejected(self):
        duplicate = record("P-A-2010-one", "2010", 100, 10)

        with self.assertRaisesRegex(ValueError, "duplicate paper_id"):
            MODULE.summarize_records([duplicate, duplicate], problem_type="A")


if __name__ == "__main__":
    unittest.main()
