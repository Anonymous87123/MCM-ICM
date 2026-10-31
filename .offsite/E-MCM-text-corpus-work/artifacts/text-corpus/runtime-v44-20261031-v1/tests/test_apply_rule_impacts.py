from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "apply_rule_impacts.py"
SPEC = importlib.util.spec_from_file_location("apply_rule_impacts", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def rule() -> dict[str, object]:
    return {
        "rule_id": "R-A-LANG-001",
        "problem_type": "A",
        "lifecycle": "corroborated",
        "evidence_ids": ["O-A-prior-001"],
        "source_papers": ["P-A-prior"],
        "source_count": 1,
    }


def observation(observation_id: str = "O-A-current-001") -> dict[str, object]:
    return {
        "observation_id": observation_id,
        "paper_id": "P-A-current",
        "problem_type": "A",
        "candidate_rule_ids": ["R-A-LANG-001"],
    }


def paper_card(evidence_id: str = "O-A-current-001") -> dict[str, object]:
    return {
        "paper_id": "P-A-current",
        "problem_type": "A",
        "candidate_rule_impacts": [
            {
                "rule_id": "R-A-LANG-001",
                "action": "corroborate",
                "evidence_ids": [evidence_id],
                "rationale": "Adds a source-checked language example.",
            }
        ],
    }


class ApplyRuleImpactsTests(unittest.TestCase):
    def test_appends_evidence_and_recomputes_sources_without_promoting_lifecycle(self):
        rules = [rule()]
        index = {
            "O-A-prior-001": {
                "observation_id": "O-A-prior-001",
                "paper_id": "P-A-prior",
                "problem_type": "A",
                "candidate_rule_ids": ["R-A-LANG-001"],
            },
            "O-A-current-001": observation(),
        }

        updated, changes = MODULE.apply_impacts(rules, paper_card(), index)

        self.assertEqual(updated[0]["evidence_ids"], ["O-A-prior-001", "O-A-current-001"])
        self.assertEqual(updated[0]["source_papers"], ["P-A-prior", "P-A-current"])
        self.assertEqual(updated[0]["source_count"], 2)
        self.assertEqual(updated[0]["lifecycle"], "corroborated")
        self.assertEqual(changes[0]["added_evidence_ids"], ["O-A-current-001"])

    def test_reapplying_the_same_impact_is_idempotent(self):
        index = {
            "O-A-prior-001": {
                "observation_id": "O-A-prior-001",
                "paper_id": "P-A-prior",
                "problem_type": "A",
                "candidate_rule_ids": ["R-A-LANG-001"],
            },
            "O-A-current-001": observation(),
        }
        first, _ = MODULE.apply_impacts([rule()], paper_card(), index)

        second, changes = MODULE.apply_impacts(first, paper_card(), index)

        self.assertEqual(second, first)
        self.assertEqual(changes[0]["added_evidence_ids"], [])

    def test_unknown_rule_fails(self):
        card = paper_card()
        card["candidate_rule_impacts"][0]["rule_id"] = "R-A-MISSING-001"

        with self.assertRaisesRegex(ValueError, "unknown rule"):
            MODULE.apply_impacts([rule()], card, {"O-A-current-001": observation()})

    def test_evidence_must_name_the_rule_as_a_candidate(self):
        current = observation()
        current["candidate_rule_ids"] = []

        with self.assertRaisesRegex(ValueError, "does not nominate rule"):
            MODULE.apply_impacts([rule()], paper_card(), {"O-A-current-001": current})

    def test_evidence_type_and_paper_must_match_card(self):
        current = observation()
        current["problem_type"] = "B"

        with self.assertRaisesRegex(ValueError, "type mismatch"):
            MODULE.apply_impacts([rule()], paper_card(), {"O-A-current-001": current})


if __name__ == "__main__":
    unittest.main()
