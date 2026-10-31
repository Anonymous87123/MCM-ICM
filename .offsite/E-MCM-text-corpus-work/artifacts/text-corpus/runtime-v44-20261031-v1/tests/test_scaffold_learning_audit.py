from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scaffold_learning_audit.py"
SPEC = importlib.util.spec_from_file_location("scaffold_learning_audit", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ScaffoldLearningAuditTests(unittest.TestCase):
    def test_scaffold_copies_ids_counts_and_remains_explicitly_incomplete(self):
        paper_id = "P-A-2010-1234-aaaaaaaa"
        language = {
            "schema_version": 3, "paper_id": paper_id, "problem_type": "A",
            "year": "2010", "source_sha256": "a" * 64,
            "available_chapters": ["abstract"],
            "units": [{"language_unit_id": "LU-A-1", "candidate_pattern_ids": ["LP-A-1"]}],
            "chapter_layouts": [{"chapter": "abstract", "paragraph_count": 1}],
        }
        models = {
            "schema_version": 2, "paper_id": paper_id,
            "models": [{"model_id": "MU-A-1", "governing_equations": [{"equation_id": "EQ-A-1"}]}],
        }
        card = {
            "paper_id": paper_id,
            "visualization_observations": [{"summary": "Compare the response."}],
        }
        observations = [
            {"dimension": "language"}, {"dimension": "weakness"}, {"dimension": "logic"}
        ]
        manifest = {"paper_id": paper_id}

        draft = MODULE.scaffold(language, models, card, observations, manifest)

        self.assertEqual(draft["review_status"], "draft")
        self.assertEqual(draft["chapter_saturation"][0]["coverage_status"], "gap-open")
        self.assertEqual(draft["model_retention"]["retained_equation_ids"], ["EQ-A-1"])
        self.assertEqual(draft["dimension_counts"]["weakness"], 1)
        self.assertEqual(draft["visualization_dispositions"][0]["paper_card_visual_index"], 1)

    def test_requires_current_language_and_model_versions(self):
        with self.assertRaisesRegex(ValueError, "language record"):
            MODULE.scaffold(
                {"schema_version": 2}, {"schema_version": 2}, {}, [], {}
            )


if __name__ == "__main__":
    unittest.main()
