from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "derive_protocol_compliance.py"
)
SPEC = importlib.util.spec_from_file_location("derive_protocol_compliance", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def language_record(paper_id: str, schema_version: int = 3) -> dict[str, object]:
    record: dict[str, object] = {
        "schema_version": schema_version,
        "paper_id": paper_id,
        "available_chapters": ["abstract", "introduction"],
        "units": [
            {"language_unit_id": f"LU-{paper_id}-ABS", "chapter": "abstract"},
            {"language_unit_id": f"LU-{paper_id}-INT", "chapter": "introduction"},
        ],
        "review_status": "validated",
    }
    if schema_version == 3:
        record["chapter_layouts"] = [
            {"chapter": "abstract"},
            {"chapter": "introduction"},
        ]
    return record


def model_record(paper_id: str) -> dict[str, object]:
    return {
        "schema_version": 2,
        "paper_id": paper_id,
        "models": [
            {
                "model_id": f"MU-{paper_id}-001",
                "governing_equations": [{"equation_id": f"EQ-{paper_id}-001"}],
            }
        ],
        "review_status": "validated",
    }


def audit_record(paper_id: str) -> dict[str, object]:
    return {
        "schema_version": 1,
        "paper_id": paper_id,
        "review_status": "validated",
    }


def card_record(paper_id: str, language_schema: int = 3) -> dict[str, object]:
    return {
        "schema_version": 1,
        "paper_id": paper_id,
        "protocol_v2_records": {
            "language": {
                "path": f"artifacts/language-units/{paper_id}.json",
                "schema_version": language_schema,
                "unit_count": 2,
                "chapters": ["abstract", "introduction"],
                "review_status": "validated",
            },
            "models": {
                "path": f"artifacts/model-units/{paper_id}.json",
                "model_count": 1,
                "equation_count": 1,
                "review_status": "validated",
            },
        },
        "review_status": "validated",
    }


class ComplianceWorkspace:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.progress = root / "progress.jsonl"
        self.cards = root / "paper-cards"
        self.languages = root / "language-units"
        self.models = root / "model-units"
        self.audits = root / "learning-audits"
        for directory in (self.cards, self.languages, self.models, self.audits):
            directory.mkdir(parents=True)

    def write_progress(self, rows: list[dict[str, object]]) -> None:
        content = "".join(json.dumps(row) + "\n" for row in rows)
        self.progress.write_text(content, encoding="utf-8")

    def write_artifacts(
        self,
        paper_id: str,
        *,
        language_schema: int = 3,
        include_audit: bool = True,
        card: dict[str, object] | None = None,
    ) -> None:
        payloads = {
            self.cards / f"{paper_id}.json": card
            or card_record(paper_id, language_schema),
            self.languages / f"{paper_id}.json": language_record(
                paper_id, language_schema
            ),
            self.models / f"{paper_id}.json": model_record(paper_id),
        }
        if include_audit:
            payloads[self.audits / f"{paper_id}.json"] = audit_record(paper_id)
        for path, payload in payloads.items():
            path.write_text(json.dumps(payload), encoding="utf-8")

    def derive(self) -> dict[str, object]:
        return MODULE.derive_report(
            progress_path=self.progress,
            paper_cards_dir=self.cards,
            language_units_dir=self.languages,
            model_units_dir=self.models,
            learning_audits_dir=self.audits,
        )

    def derive_with_semantic_errors(
        self, errors: dict[str, list[str]]
    ) -> dict[str, object]:
        return MODULE.derive_report(
            progress_path=self.progress,
            paper_cards_dir=self.cards,
            language_units_dir=self.languages,
            model_units_dir=self.models,
            learning_audits_dir=self.audits,
            semantic_errors_by_paper=errors,
        )


class ProtocolComplianceTests(unittest.TestCase):
    def test_new_closed_v2_paper_automatically_enters_migration_set(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = ComplianceWorkspace(Path(directory))
            current_id = "P-A-2010-current"
            legacy_id = "P-A-2011-newly-closed-v2"
            workspace.write_progress(
                [
                    {"paper_id": current_id, "status": "closed"},
                    {"paper_id": legacy_id, "status": "closed"},
                ]
            )
            workspace.write_artifacts(current_id)
            workspace.write_artifacts(legacy_id, language_schema=2)

            report = workspace.derive()

            self.assertEqual(report["lifecycle_closed"], 2)
            self.assertEqual(report["current_protocol_complete"], 1)
            self.assertEqual(report["migration_paper_ids"], [legacy_id])
            records = {item["paper_id"]: item for item in report["records"]}
            self.assertEqual(records[current_id]["protocol_status"], "current-validated")
            self.assertEqual(records[legacy_id]["protocol_status"], "partial")
            self.assertIn("language:schema-version-2", records[legacy_id]["reasons"])

    def test_missing_learning_audit_is_partial(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = ComplianceWorkspace(Path(directory))
            paper_id = "P-A-2012-missing-audit"
            workspace.write_progress([{"paper_id": paper_id, "status": "closed"}])
            workspace.write_artifacts(paper_id, include_audit=False)

            report = workspace.derive()

            self.assertEqual(report["current_protocol_complete"], 0)
            self.assertEqual(report["migration_paper_ids"], [paper_id])
            self.assertEqual(report["records"][0]["protocol_status"], "partial")
            self.assertIn("learning-audit:missing", report["records"][0]["reasons"])

    def test_card_count_mismatch_requires_correction(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = ComplianceWorkspace(Path(directory))
            paper_id = "P-A-2012-count-mismatch"
            workspace.write_progress([{"paper_id": paper_id, "status": "closed"}])
            card = card_record(paper_id)
            card["protocol_v2_records"]["language"]["unit_count"] = 3
            workspace.write_artifacts(paper_id, card=card)

            report = workspace.derive()

            self.assertEqual(report["records"][0]["protocol_status"], "correction-required")
            self.assertIn(
                "card:language-unit-count-mismatch",
                report["records"][0]["reasons"],
            )

    def test_semantic_learning_audit_failure_requires_correction(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = ComplianceWorkspace(Path(directory))
            paper_id = "P-A-2012-semantic-failure"
            workspace.write_progress([{"paper_id": paper_id, "status": "closed"}])
            workspace.write_artifacts(paper_id)

            report = workspace.derive_with_semantic_errors(
                {paper_id: ["language unit disposition is invalid"]}
            )

            record = report["records"][0]
            self.assertEqual(record["protocol_status"], "correction-required")
            self.assertIn("learning-audit:semantic-validation-failed", record["reasons"])
            self.assertEqual(
                record["semantic_validation_errors"],
                ["language unit disposition is invalid"],
            )

    def test_duplicates_and_artifact_set_differences_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = ComplianceWorkspace(Path(directory))
            duplicate_id = "P-A-2013-duplicate"
            orphan_id = "P-B-2013-artifact-only"
            workspace.write_progress(
                [
                    {"paper_id": duplicate_id, "status": "closed"},
                    {"paper_id": duplicate_id, "status": "closed"},
                ]
            )
            workspace.write_artifacts(duplicate_id)
            (workspace.audits / f"{orphan_id}.json").write_text(
                json.dumps(audit_record(orphan_id)), encoding="utf-8"
            )

            report = workspace.derive()

            self.assertEqual(report["lifecycle_closed"], 1)
            self.assertEqual(report["progress_closed_rows"], 2)
            self.assertEqual(
                report["integrity"]["duplicate_progress_paper_ids"],
                [duplicate_id],
            )
            self.assertEqual(
                report["integrity"]["artifact_only_paper_ids"]["learning_audits"],
                [orphan_id],
            )
            self.assertEqual(report["report_status"], "correction-required")
            self.assertEqual(
                report["records"][0]["protocol_status"], "correction-required"
            )


if __name__ == "__main__":
    unittest.main()
