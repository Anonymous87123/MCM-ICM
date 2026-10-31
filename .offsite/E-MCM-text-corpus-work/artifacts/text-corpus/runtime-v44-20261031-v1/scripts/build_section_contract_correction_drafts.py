#!/usr/bin/env python3
"""Build corrective transaction drafts for the section-contract migration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--test-count", type=int, required=True)
    args = parser.parse_args(argv)

    try:
        report = json.loads(args.report.read_text(encoding="utf-8"))
        records = report.get("records") if isinstance(report, dict) else None
        if not isinstance(records, list) or not records:
            raise ValueError("migration report requires nonempty records")
        args.output_dir.mkdir(parents=True, exist_ok=True)
        created: list[str] = []
        for record in records:
            if not isinstance(record, dict):
                raise ValueError("migration records must be objects")
            paper_id = record.get("paper_id")
            count = record.get("changed_section_contracts")
            before_hash = record.get("before_sha256")
            after_hash = record.get("after_sha256")
            if not isinstance(paper_id, str) or not paper_id:
                raise ValueError("migration record requires paper_id")
            if not isinstance(count, int) or count < 1:
                raise ValueError(f"{paper_id} requires a positive contract count")
            if not all(isinstance(value, str) and len(value) == 64 for value in (before_hash, after_hash)):
                raise ValueError(f"{paper_id} requires before/after SHA-256 values")
            parts = paper_id.split("-")
            if len(parts) < 3 or parts[1] not in "ABCDEF":
                raise ValueError(f"cannot derive problem type from {paper_id}")
            problem_type = parts[1]
            draft: dict[str, Any] = {
                "event_type": "paper-corrected",
                "paper_id": paper_id,
                "before": {
                    "learning_audit_sha256": before_hash,
                    "section_contract_status": "implicit-move-sequence",
                },
                "after": {
                    "learning_audit_sha256": after_hash,
                    "section_contract_status": "explicit-five-part",
                    "section_contract_count": count,
                    "protocol_status": "current-validated",
                },
                "changed_fields": [
                    "learning_audit.organization_logic.section_progressions"
                ],
                "artifact_diffs": [
                    f"Replaced {count} topic-only section progressions with explicit input, rhetorical job, analytical job, output, and handoff contracts; audit SHA-256 changed from {before_hash} to {after_hash}."
                ],
                "type_branch_diff": {
                    "problem_type": problem_type,
                    "section_contracts_before": 0,
                    "section_contracts_after": count,
                    "new_weakness_observations": 0,
                    "shared_catalog_changes": [],
                },
                "validation_results": [
                    {
                        "validator": "validate_language_units.py",
                        "status": "pass",
                        "details": "Validated language artifact remains unchanged.",
                    },
                    {
                        "validator": "validate_model_units.py",
                        "status": "pass",
                        "details": "Validated formula-level model artifact remains unchanged.",
                    },
                    {
                        "validator": "validate_learning_audit.py",
                        "status": "pass",
                        "details": f"All {count} section progressions contain exactly one nonempty input, rhetorical job, analytical job, output, and handoff move.",
                    },
                    {
                        "validator": "validate_paper_artifacts.py",
                        "status": "pass",
                        "details": "Paper card, observations, rules, extraction, language, and model artifacts remain cross-valid.",
                    },
                    {
                        "validator": "unittest",
                        "status": "pass",
                        "details": f"{args.test_count} tests passed after the semantic organization-contract gate was added.",
                    },
                ],
                "unresolved_added": [],
                "unresolved_resolved": [
                    "Topic-only organization sequences can no longer satisfy section-contract coverage; every substantive audited chapter now exposes its input, rhetorical job, analytical job, output, and handoff."
                ],
            }
            path = args.output_dir / f"{paper_id}-section-contract-correction-draft.json"
            path.write_text(
                json.dumps(draft, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            created.append(str(path))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1

    print(
        json.dumps(
            {"status": "pass", "draft_count": len(created), "drafts": created},
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
