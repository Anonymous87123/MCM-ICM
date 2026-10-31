from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "validate_language_patterns.py"
)
SPEC = importlib.util.spec_from_file_location("validate_language_patterns", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def evidence(paper_id: str, page: int, excerpt: str) -> dict[str, object]:
    token = paper_id.split("-")[3]
    return {
        "language_unit_id": f"LU-A-{token}-ABS-001",
        "paper_id": paper_id,
        "problem_type": "A",
        "page": page,
        "section": "Abstract",
        "excerpt": excerpt,
    }


def valid_template() -> dict[str, object]:
    return {
        "pattern_id": "LP-A-ABS-001",
        "pattern_kind": "sentence-template",
        "lifecycle": "corroborated",
        "problem_types": ["A"],
        "chapters": ["abstract"],
        "function": "State the task and preview the solution architecture.",
        "trigger": "Use after the one-sentence problem context.",
        "paragraph_moves": ["task", "method-preview"],
        "slots": [
            {
                "name": "task",
                "required": True,
                "description": "The decision or quantity requested.",
            },
            {
                "name": "method",
                "required": True,
                "description": "The model family used to answer it.",
            },
        ],
        "variants": [
            "To address {task}, we develop {method}.",
            "We formulate {task} through {method}.",
        ],
        "filled_example": (
            "To identify a safe operating region, we develop a constrained "
            "mechanics model."
        ),
        "forbidden_uses": ["Do not claim novelty without a named comparator."],
        "evidence": [
            evidence("P-A-2010-6749-395f556a", 1, "We develop models for ..."),
            evidence("P-A-2010-7571-1ac2a627", 1, "We formulate the problem ..."),
        ],
        "source_count": 2,
        "confidence": "medium",
        "judge_relevance": {
            "status": "unknown",
            "basis": "No direct judge commentary is available.",
        },
    }


def valid_catalog() -> dict[str, object]:
    return {
        "schema_version": 2,
        "catalog_id": "LANG-A-v2",
        "problem_type": "A",
        "templates": [valid_template()],
        "lexicon": {
            "positive": [
                {
                    "term": "quantify",
                    "function": "Introduce a measured relationship.",
                    "chapters": ["abstract", "results"],
                    "use_when": "A numerical metric follows.",
                    "avoid_when": "Only a qualitative comparison is available.",
                    "example": "We quantify the response under three regimes.",
                    "evidence_pattern_ids": ["LP-A-ABS-001"],
                }
            ],
            "negative": [
                {
                    "term": "perfect",
                    "failure_mode": "Unsupported certainty.",
                    "replacement_rule": "Name the metric, residual, and scope.",
                    "chapters": ["abstract", "conclusion"],
                    "evidence_pattern_ids": ["LP-A-ABS-001"],
                }
            ],
        },
        "layout_profiles": [
            {
                "chapter": "abstract",
                "unit": "sentence",
                "measurement_status": "provisional",
                "sample_papers": [
                    "P-A-2010-6749-395f556a",
                    "P-A-2010-7571-1ac2a627",
                ],
                "sample_size": 2,
                "observed_range": {"minimum": 5, "maximum": 9},
                "recommended_use": "Treat as a corpus range, not a fixed quota.",
            }
        ],
    }


class LanguagePatternValidationTests(unittest.TestCase):
    def test_valid_catalog_passes(self):
        errors = MODULE.validate_catalog(valid_catalog())
        self.assertEqual(errors, [])

    def test_recurring_template_requires_two_independent_papers(self):
        catalog = valid_catalog()
        template = catalog["templates"][0]
        template["evidence"] = [
            evidence("P-A-2010-6749-395f556a", 1, "First source."),
            evidence("P-A-2010-6749-395f556a", 2, "Same paper again."),
        ]

        errors = MODULE.validate_catalog(catalog)

        self.assertTrue(any("independent papers" in error for error in errors))

    def test_duplicate_content_does_not_count_as_independent_evidence(self):
        catalog = valid_catalog()
        content_ids = {
            "P-A-2010-6749-395f556a": "C-shared",
            "P-A-2010-7571-1ac2a627": "C-shared",
        }

        errors = MODULE.validate_catalog(catalog, content_ids=content_ids)

        self.assertTrue(any("independent content" in error for error in errors))

    def test_evidence_must_resolve_to_matching_language_unit(self):
        catalog = valid_catalog()
        unit_index = {
            "LU-A-6749-ABS-001": {
                "paper_id": "P-A-2010-6749-395f556a",
                "problem_type": "A",
                "page": 1,
                "chapter": "abstract",
                "source_excerpt": "We develop models for ...",
            }
        }

        errors = MODULE.validate_catalog(catalog, unit_index=unit_index)

        self.assertTrue(any("unknown language_unit_id" in error for error in errors))

    def test_corroborated_template_rejects_unvalidated_language_units(self):
        catalog = valid_catalog()
        first = catalog["templates"][0]["evidence"][0]
        second = catalog["templates"][0]["evidence"][1]
        unit_index = {
            first["language_unit_id"]: {
                **first,
                "chapter": "abstract",
                "source_excerpt": first["excerpt"],
                "review_status": "validated",
            },
            second["language_unit_id"]: {
                **second,
                "chapter": "abstract",
                "source_excerpt": second["excerpt"],
                "review_status": "source-checked",
            },
        }

        errors = MODULE.validate_catalog(catalog, unit_index=unit_index)

        self.assertTrue(any("requires validated language units" in error for error in errors))

    def test_template_requires_two_original_variants_and_slots(self):
        catalog = valid_catalog()
        template = catalog["templates"][0]
        template["variants"] = ["We use {method}."]
        template["slots"] = []

        errors = MODULE.validate_catalog(catalog)

        self.assertTrue(any("at least two variants" in error for error in errors))
        self.assertTrue(any("at least one slot" in error for error in errors))

    def test_evidence_excerpt_cannot_be_a_full_source_paragraph(self):
        catalog = valid_catalog()
        catalog["templates"][0]["evidence"][0]["excerpt"] = "x" * 501

        errors = MODULE.validate_catalog(catalog)

        self.assertTrue(any("excerpt exceeds" in error for error in errors))

    def test_layout_sample_size_must_match_unique_papers(self):
        catalog = valid_catalog()
        catalog["layout_profiles"][0]["sample_size"] = 3

        errors = MODULE.validate_catalog(catalog)

        self.assertTrue(any("sample_size" in error for error in errors))

    def test_cli_returns_failure_for_invalid_catalog(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "catalog.json"
            catalog = valid_catalog()
            catalog["templates"][0]["problem_types"] = ["B"]
            path.write_text(json.dumps(catalog), encoding="utf-8")

            result = MODULE.main(["--catalog", str(path)])

            self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
