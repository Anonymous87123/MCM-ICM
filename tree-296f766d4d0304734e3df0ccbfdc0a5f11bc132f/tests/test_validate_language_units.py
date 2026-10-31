from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_language_units.py"
SPEC = importlib.util.spec_from_file_location("validate_language_units", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def language_unit(
    unit_id: str,
    chapter: str,
    page: int,
    candidate_pattern_ids: list[str] | None = None,
) -> dict[str, object]:
    return {
        "language_unit_id": unit_id,
        "page": page,
        "section": chapter.title(),
        "chapter": chapter,
        "granularity": "sentence",
        "source_excerpt": "We develop a model to estimate the requested quantity.",
        "function": "Preview the solution architecture.",
        "rhetorical_move": "task-to-method",
        "information_order": ["task", "method", "output"],
        "features": {
            "voice": "active",
            "tense": "present",
            "modality": "none",
            "clause_structure": "purpose-main",
            "quantitative_role": "none",
            "transition": "none",
        },
        "reusable_pattern": "We develop {method} to estimate {quantity}.",
        "reusable_elements": ["explicit method", "explicit output"],
        "prohibited_generalizations": ["Do not imply validation from construction."],
        "candidate_pattern_ids": candidate_pattern_ids or [],
    }


def valid_record() -> dict[str, object]:
    return {
        "schema_version": 3,
        "paper_id": "P-A-2010-6749-395f556a",
        "problem_type": "A",
        "year": "2010",
        "source_sha256": "a" * 64,
        "available_chapters": ["abstract", "introduction"],
        "units": [
            language_unit("LU-A-2010-6749-ABS-001", "abstract", 1),
            language_unit("LU-A-2010-6749-INT-001", "introduction", 2),
        ],
        "chapter_layouts": [
            chapter_layout("abstract", 1),
            chapter_layout("introduction", 2),
        ],
        "review_status": "validated",
    }


def chapter_layout(chapter: str, page: int) -> dict[str, object]:
    return {
        "chapter": chapter,
        "page_start": page,
        "page_end": page,
        "page_fraction": 0.1,
        "word_count": 100,
        "sentence_count": 5,
        "paragraph_count": 2,
        "sentence_words": {"minimum": 10, "maximum": 30, "median": 20},
        "paragraph_functions": ["task", "method-result"],
        "rhetorical_proportions": {"task": 0.4, "method-result": 0.6},
        "content_counts": {
            "equations": 0,
            "figures": 0,
            "tables": 0,
            "citations": 1,
            "quantitative_results": 1,
        },
        "move_types": {
            "opening": ["task-framing"],
            "transition": ["task-to-method"],
            "closing": ["result-boundary"],
        },
        "counting_method": "Page-aware extracted prose; captions excluded.",
        "ambiguities": [],
    }


class LanguageUnitValidationTests(unittest.TestCase):
    def test_valid_record_passes(self):
        self.assertEqual(MODULE.validate_record(valid_record()), [])

    def test_legacy_v2_remains_readable_during_migration(self):
        record = valid_record()
        record["schema_version"] = 2
        del record["chapter_layouts"]

        self.assertEqual(MODULE.validate_record(record), [])

    def test_every_available_chapter_requires_a_unit(self):
        record = valid_record()
        record["units"] = record["units"][:1]

        errors = MODULE.validate_record(record)

        self.assertTrue(any("introduction" in error for error in errors))

    def test_every_available_chapter_requires_a_quantitative_layout(self):
        record = valid_record()
        record["chapter_layouts"] = record["chapter_layouts"][:1]

        errors = MODULE.validate_record(record)

        self.assertTrue(any("introduction" in error and "layout" in error for error in errors))

    def test_layout_requires_reconciled_counts_and_proportions(self):
        record = valid_record()
        layout = record["chapter_layouts"][0]
        layout["sentence_count"] = 0
        layout["rhetorical_proportions"] = {"task": 0.7, "method-result": 0.7}

        errors = MODULE.validate_record(record)

        self.assertTrue(any("sentence_count" in error for error in errors))
        self.assertTrue(any("rhetorical_proportions" in error for error in errors))

    def test_unit_requires_information_order_and_reusable_pattern(self):
        record = valid_record()
        unit = record["units"][0]
        unit["information_order"] = []
        unit["reusable_pattern"] = ""

        errors = MODULE.validate_record(record)

        self.assertTrue(any("information_order" in error for error in errors))
        self.assertTrue(any("reusable_pattern" in error for error in errors))

    def test_source_excerpt_is_short_and_source_faithful(self):
        record = valid_record()
        record["units"][0]["source_excerpt"] = "x" * 501

        errors = MODULE.validate_record(record)

        self.assertTrue(any("excerpt exceeds" in error for error in errors))

    def test_candidate_pattern_ids_must_exist_when_catalog_is_supplied(self):
        record = valid_record()
        record["units"][0]["candidate_pattern_ids"] = ["LP-A-ABS-404"]

        errors = MODULE.validate_record(record, {"LP-A-ABS-001"})

        self.assertTrue(any("unknown pattern" in error for error in errors))

    def test_duplicate_language_unit_ids_fail(self):
        record = valid_record()
        record["units"][1]["language_unit_id"] = record["units"][0]["language_unit_id"]

        errors = MODULE.validate_record(record)

        self.assertTrue(any("duplicate language_unit_id" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
