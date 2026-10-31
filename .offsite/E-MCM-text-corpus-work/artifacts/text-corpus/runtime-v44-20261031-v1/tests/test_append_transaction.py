from __future__ import annotations

import importlib.util
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "append_transaction.py"
SPEC = importlib.util.spec_from_file_location("append_transaction", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def draft(paper_id: str = "P-A-2011-9665-6560aced") -> dict[str, object]:
    return {
        "event_type": "paper-closed",
        "paper_id": paper_id,
        "before": {"status": "discovered"},
        "after": {"status": "closed"},
        "changed_fields": ["status", "paper_card_status"],
        "artifact_diffs": ["created paper card"],
        "type_branch_diff": {"rules_touched": ["R-A-LANG-001"]},
        "validation_results": [{"validator": "paper-artifacts", "status": "pass"}],
        "unresolved_added": [],
        "unresolved_resolved": [],
    }


def correction_draft(paper_id: str = "P-A-2011-9665-6560aced") -> dict[str, object]:
    value = draft(paper_id)
    value["event_type"] = "paper-corrected"
    value["before"] = {"status": "closed", "artifact_sha256": "a" * 64}
    value["after"] = {"status": "current-validated", "artifact_sha256": "b" * 64}
    value["changed_fields"] = ["artifact_sha256"]
    value["artifact_diffs"] = ["corrected and revalidated the frozen artifact"]
    return value


class AppendTransactionTests(unittest.TestCase):
    def test_first_event_starts_hash_chain(self):
        event = MODULE.build_event(draft(), [], "2026-07-11T12:00:00Z")

        self.assertEqual(event["sequence"], 1)
        self.assertIsNone(event["previous_event_hash"])
        self.assertTrue(event["event_id"].startswith("TX-000001-"))
        self.assertEqual(len(event["event_hash"]), 64)

    def test_second_event_links_to_first_and_chain_validates(self):
        first = MODULE.build_event(draft(), [], "2026-07-11T12:00:00Z")
        second = MODULE.build_event(
            draft("P-A-2012-next-bbbbbbbb"),
            [first],
            "2026-07-11T12:01:00Z",
        )

        self.assertEqual(second["sequence"], 2)
        self.assertEqual(second["previous_event_hash"], first["event_hash"])
        self.assertEqual(MODULE.validate_history([first, second]), [])

    def test_migration_baseline_is_explicitly_marked_baseline_only(self):
        migration = draft()
        migration["event_type"] = "migration-baseline"
        migration["history_completeness"] = "baseline-only"

        event = MODULE.build_event(migration, [], "2026-07-11T11:59:00Z")

        self.assertEqual(event["history_completeness"], "baseline-only")

    def test_second_migration_baseline_is_rejected(self):
        migration = draft()
        migration["event_type"] = "migration-baseline"
        migration["history_completeness"] = "baseline-only"
        first = MODULE.build_event(migration, [], "2026-07-11T11:59:00Z")

        with self.assertRaisesRegex(ValueError, "genesis"):
            MODULE.build_event(migration, [first], "2026-07-11T12:00:00Z")

    def test_tampered_history_is_rejected(self):
        first = MODULE.build_event(draft(), [], "2026-07-11T12:00:00Z")
        first["after"]["status"] = "tampered"

        errors = MODULE.validate_history([first])

        self.assertTrue(any("event_hash mismatch" in error for error in errors))

    def test_duplicate_paper_closed_event_is_rejected(self):
        first = MODULE.build_event(draft(), [], "2026-07-11T12:00:00Z")

        with self.assertRaisesRegex(ValueError, "duplicate paper-closed"):
            MODULE.build_event(draft(), [first], "2026-07-11T12:01:00Z")

    def test_append_event_persists_one_valid_json_line(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "history.jsonl"

            event = MODULE.append_event(path, draft(), "2026-07-11T12:00:00Z")
            records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

            self.assertEqual(records, [event])
            self.assertEqual(MODULE.validate_history(records), [])

    def test_correction_rejects_unknown_paper_and_empty_evidence(self):
        first = MODULE.build_event(draft(), [], "2026-07-11T12:00:00Z")

        with self.assertRaisesRegex(ValueError, "unknown paper"):
            MODULE.build_event(
                correction_draft("P-A-2025-unknown-aaaaaaaa"),
                [first],
                "2026-07-11T12:01:00Z",
            )

        invalid = correction_draft()
        invalid["artifact_diffs"] = []
        invalid["validation_results"] = []
        with self.assertRaisesRegex(ValueError, "artifact_diffs"):
            MODULE.build_event(invalid, [first], "2026-07-11T12:01:00Z")

    def test_history_lock_prevents_a_second_writer(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "history.jsonl"

            with MODULE.exclusive_history_lock(path):
                with self.assertRaisesRegex(ValueError, "locked by another writer"):
                    MODULE.append_event(path, draft(), "2026-07-11T12:00:00Z")

            event = MODULE.append_event(path, draft(), "2026-07-11T12:00:00Z")
            self.assertEqual(event["sequence"], 1)

    def test_validate_only_checks_the_draft_without_appending(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            history = root / "history.jsonl"
            draft_path = root / "draft.json"
            candidate = draft()
            candidate["event_type"] = "migration-baseline"
            candidate["history_completeness"] = "baseline-only"
            draft_path.write_text(json.dumps(candidate), encoding="utf-8")

            result = MODULE.main(
                [
                    "--history",
                    str(history),
                    "--draft",
                    str(draft_path),
                    "--timestamp-utc",
                    "2026-07-11T12:00:00Z",
                    "--validate-only",
                ]
            )

            self.assertEqual(result, 0)
            self.assertFalse(history.exists())

    def test_declared_artifact_hashes_and_counts_are_verified(self):
        paper_id = "P-A-2011-9665-6560aced"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            records = {
                f"artifacts/paper-cards/{paper_id}.json": {
                    "visualization_observations": [{"page": 1}],
                },
                f"artifacts/language-units/{paper_id}.json": {"units": [{"id": "LU-1"}]},
                f"artifacts/model-units/{paper_id}.json": {
                    "models": [{"governing_equations": [{"id": "EQ-1"}]}],
                },
                f"artifacts/learning-audits/{paper_id}.json": {"review_status": "validated"},
            }
            declarations: list[str] = []
            for relative, value in records.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(value), encoding="utf-8")
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                declarations.append(f"artifact:{relative}|sha256:{digest}")
            observations_relative = f"artifacts/observations/{paper_id}.jsonl"
            observations_path = root / observations_relative
            observations_path.parent.mkdir(parents=True, exist_ok=True)
            observations_path.write_text('{"dimension":"language"}\n', encoding="utf-8")
            declarations.append(
                f"artifact:{observations_relative}|sha256:"
                f"{hashlib.sha256(observations_path.read_bytes()).hexdigest()}"
            )

            candidate = correction_draft(paper_id)
            candidate["artifact_diffs"] = declarations
            candidate["after"].update(
                {
                    "protocol_status": "current-validated",
                    "language_unit_count": 6400,
                    "model_count": 1,
                    "equation_count": 1,
                    "important_visual_count": 1,
                }
            )

            errors = MODULE.validate_declared_artifacts(candidate, root)

            self.assertTrue(any("language_unit_count" in error for error in errors))
            candidate["after"]["language_unit_count"] = 1
            self.assertEqual(MODULE.validate_declared_artifacts(candidate, root), [])

            observations_path.write_text('{"dimension":"weakness"}\n', encoding="utf-8")
            errors = MODULE.validate_declared_artifacts(candidate, root)
            self.assertTrue(any("artifact hash mismatch" in error for error in errors))

    def test_paper_closed_requires_core_artifacts_and_frozen_counts(self):
        candidate = draft()

        errors = MODULE.validate_declared_artifacts(candidate, Path.cwd())

        self.assertTrue(any("lacks artifact declarations" in error for error in errors))
        self.assertTrue(any("language_unit_count" in error for error in errors))
        self.assertTrue(any("model_count" in error for error in errors))
        self.assertTrue(any("equation_count" in error for error in errors))
        self.assertTrue(any("important_visual_count" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
