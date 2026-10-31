from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_language_priority_drift.py"
SPEC = importlib.util.spec_from_file_location("validate_language_priority_drift", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def history(count: int = 5) -> list[dict[str, object]]:
    return [
        {
            "event_type": "paper-closed",
            "history_completeness": "native",
            "paper_id": f"P-A-2012-{index}-aaaaaaaa",
        }
        for index in range(count)
    ]


class LanguagePriorityDriftTests(unittest.TestCase):
    def write_observations(self, root: Path, paper_id: str, dimensions: list[str]) -> None:
        (root / f"{paper_id}.jsonl").write_text(
            "".join(json.dumps({"dimension": item}) + "\n" for item in dimensions),
            encoding="utf-8",
        )

    def test_recent_five_language_largest_with_models_and_visuals_passes(self):
        events = history()
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            root = Path(directory)
            for event in events:
                self.write_observations(
                    root, str(event["paper_id"]),
                    ["language", "language", "modeling", "visualization", "weakness"],
                )
            report = MODULE.validate_window(events, root)
        self.assertEqual(report["status"], "pass")

    def test_model_dominance_and_missing_visuals_fail(self):
        events = history()
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            root = Path(directory)
            for event in events:
                self.write_observations(
                    root, str(event["paper_id"]),
                    ["language", "modeling", "modeling", "weakness"],
                )
            report = MODULE.validate_window(events, root)
        self.assertTrue(any("not the strictly largest" in item for item in report["errors"]))
        self.assertTrue(any("visualization" in item for item in report["errors"]))

    def test_tie_with_another_dimension_fails_strict_language_priority(self):
        events = history()
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            root = Path(directory)
            for event in events:
                self.write_observations(
                    root, str(event["paper_id"]),
                    ["language", "modeling", "visualization", "weakness"],
                )
            report = MODULE.validate_window(events, root)
        self.assertEqual(report["status"], "fail")
        self.assertFalse(report["assertions"]["language_is_strictly_largest"])
        self.assertTrue(any("strictly largest" in item for item in report["errors"]))

    def test_requires_full_window_and_all_observation_files(self):
        events = history(4)
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            report = MODULE.validate_window(events, Path(directory))
        self.assertTrue(any("requires 5" in item for item in report["errors"]))
        self.assertTrue(any("missing observations" in item for item in report["errors"]))

    def test_substantive_corrections_are_recent_and_metadata_corrections_are_skipped(self):
        events = history(4)
        learned_id = "P-F-2025-learned-aaaaaaaa"
        events.extend([
            {
                "event_id": "TX-LEARN",
                "event_type": "paper-corrected",
                "history_completeness": "native",
                "paper_id": learned_id,
                "after": {
                    "language_unit_count": 60,
                    "model_count": 8,
                    "equation_count": 20,
                    "important_visual_count": 7,
                },
                "type_branch_diff": {"new_weakness_observations": 0},
            },
            {
                "event_id": "TX-META",
                "event_type": "paper-corrected",
                "history_completeness": "native",
                "paper_id": learned_id,
                "after": {"protocol_status": "current-validated"},
            },
        ])
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            root = Path(directory)
            for event in history(4):
                self.write_observations(
                    root, str(event["paper_id"]),
                    ["language", "language", "modeling", "visualization", "weakness"],
                )
            self.write_observations(
                root, learned_id,
                ["modeling", "modeling", "weakness", "weakness"],
            )
            report = MODULE.validate_window(events, root)
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["paper_ids"][-1], learned_id)
        self.assertEqual(report["event_ids"][-1], "TX-LEARN")
        self.assertEqual(
            report["count_basis"][learned_id],
            "mixed:frozen-language-model-visual+live-observations",
        )
        self.assertEqual(report["per_paper_counts"][learned_id]["language"], 60)
        self.assertEqual(report["per_paper_counts"][learned_id]["modeling"], 20)
        self.assertEqual(report["per_paper_counts"][learned_id]["visualization"], 7)
        self.assertEqual(report["per_paper_counts"][learned_id]["weakness"], 2)

    def test_latest_substantive_event_for_same_paper_replaces_older_occurrence(self):
        repeated = history(5)
        repeated.append({
            "event_id": "TX-NEW",
            "event_type": "paper-corrected",
            "history_completeness": "native",
            "paper_id": repeated[0]["paper_id"],
            "after": {
                "language_unit_count": 10,
                "model_count": 2,
                "equation_count": 3,
                "important_visual_count": 1,
            },
            "type_branch_diff": {"new_weakness_observations": 0},
        })
        selected = MODULE.rolling_paper_events(repeated, 5)
        self.assertEqual(len(selected), 5)
        self.assertEqual(selected[-1]["event_id"], "TX-NEW")
        self.assertEqual(
            len({event["paper_id"] for event in selected}),
            5,
        )


if __name__ == "__main__":
    unittest.main()
