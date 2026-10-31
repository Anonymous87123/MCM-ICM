#!/usr/bin/env python3
"""Build a create-only metadata correction draft for Queue 131 protocol links."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2020-2007698-75afc422"
OLD_CARD_HASH = "a6133a6b93876b41153a22c1f3719ab9466b3ba4f8b069fdb3c848ec93ef6571"
PRIOR_EVENT_ID = "TX-000190-187f075b75c0"
PRIOR_EVENT_HASH = "b810c84af4b60c756dd79ffbad5b92ba67c7d3a0d0108556dfbb534a98c0c546"

ARTIFACT_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": (
        "1511eb43b0c8c228742aa1fdd7dcbf313c91fd31e0784d3dd64af93abe28d035"
    ),
    f"artifacts/language-units/{PAPER_ID}.json": (
        "494a9df007d369d7b08c7ae1a91f6077579a87f481e504704ef66a2ebb5be06b"
    ),
    f"artifacts/model-units/{PAPER_ID}.json": (
        "2cae41736cf34273323db8dbf57dd0e87813e9f583a1c70e6d7b3016dbf1b81f"
    ),
    f"artifacts/learning-audits/{PAPER_ID}.json": (
        "154e3e113865de60bc2a09eb9750435c79de326edc8d7c3c284f77f74e02d8af"
    ),
    f"artifacts/observations/{PAPER_ID}.jsonl": (
        "88588d5ba14f0b25dd861e5236faa2545b48ed97b52978afede04bcdce31d945"
    ),
    f"artifacts/papers/{PAPER_ID}/extraction.json": (
        "ce192b7af2e0a246c65966f6e20c430c3b4d327b24fe9bd15bf25f5eb16d43aa"
    ),
    "artifacts/type-branches/B/rules.jsonl": (
        "b51560c7fb438992e7e7eef4cb58193fdc884e19bced50caf98e93eae12cdb14"
    ),
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": (
        "6918818e02e7c446fa09485ad2b6b53a318e157ebd0db35a59ede8468505fbb0"
    ),
}

EXPECTED_CARD_CHANGES = {
    "protocol_v2_records.language.path",
    "protocol_v2_records.models.path",
    "protocol_v2_records.models.schema_version",
}
CORRECTION_REASONS = [
    "card:language-path-mismatch",
    "card:model-path-mismatch",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"expected JSON object: {path}")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise SystemExit(f"expected JSON object at {path}:{line_number}")
            records.append(value)
    return records


def changed_paths(before: Any, after: Any, prefix: str = "") -> set[str]:
    if type(before) is not type(after):
        return {prefix}
    if isinstance(before, dict):
        changes: set[str] = set()
        for key in set(before) | set(after):
            path = f"{prefix}.{key}" if prefix else key
            if key not in before or key not in after:
                changes.add(path)
            else:
                changes.update(changed_paths(before[key], after[key], path))
        return changes
    if isinstance(before, list):
        return set() if before == after else {prefix}
    return set() if before == after else {prefix}


def paper_record(report: dict[str, Any]) -> dict[str, Any]:
    records = [
        item
        for item in report.get("records", [])
        if isinstance(item, dict) and item.get("paper_id") == PAPER_ID
    ]
    if len(records) != 1:
        raise SystemExit(f"expected one compliance record for {PAPER_ID}")
    return records[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timestamp-utc")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    draft_path = (
        ROOT
        / f"artifacts/transactions/{PAPER_ID}-protocol-path-correction-draft.json"
    )
    timestamp_path = (
        ROOT / f"tmp/{PAPER_ID}-protocol-path-correction-timestamp.txt"
    )
    if not args.check_only and (draft_path.exists() or timestamp_path.exists()):
        raise SystemExit("refusing to overwrite Queue 131 correction draft or timestamp")

    for relative, expected_hash in ARTIFACT_HASHES.items():
        path = ROOT / relative
        if not path.is_file():
            raise SystemExit(f"missing correction artifact: {relative}")
        actual_hash = digest(path)
        if actual_hash != expected_hash:
            raise SystemExit(
                f"correction artifact changed: {relative} "
                f"{actual_hash} != {expected_hash}"
            )

    old_card_path = ROOT / "tmp/q131-protocol-path-correction-preimage-card.json"
    if digest(old_card_path) != OLD_CARD_HASH:
        raise SystemExit("Queue 131 pre-correction card is not the closed-event card")
    old_card = load_json(old_card_path)
    card = load_json(ROOT / f"artifacts/paper-cards/{PAPER_ID}.json")
    actual_changes = changed_paths(old_card, card)
    if actual_changes != EXPECTED_CARD_CHANGES:
        raise SystemExit(f"unexpected paper-card correction scope: {sorted(actual_changes)}")

    language_path = f"artifacts/language-units/{PAPER_ID}.json"
    model_path = f"artifacts/model-units/{PAPER_ID}.json"
    links = card.get("protocol_v2_records", {})
    if (
        links.get("language", {}).get("path") != language_path
        or links.get("models", {}).get("path") != model_path
        or links.get("models", {}).get("schema_version") != 2
    ):
        raise SystemExit("Queue 131 corrected protocol links are incomplete")

    history = load_jsonl(ROOT / "artifacts/transactions/history.jsonl")
    if len(history) != 190:
        raise SystemExit(f"expected 190 pre-correction events; found {len(history)}")
    last = history[-1]
    if (
        last.get("event_id") != PRIOR_EVENT_ID
        or last.get("event_hash") != PRIOR_EVENT_HASH
    ):
        raise SystemExit("live history advanced after Queue 131 paper-close append")
    old_declaration = (
        f"artifact:artifacts/paper-cards/{PAPER_ID}.json|sha256:{OLD_CARD_HASH}"
    )
    if old_declaration not in last.get("artifact_diffs", []):
        raise SystemExit("Queue 131 close event does not declare the pre-correction card")

    progress = [
        item
        for item in load_jsonl(ROOT / "artifacts/progress.jsonl")
        if item.get("paper_id") == PAPER_ID
    ]
    expected_progress = {
        "status": "closed",
        "extraction_status": "validated",
        "paper_card_status": "validated",
        "branch_update_status": "validated",
        "validation_status": "pass",
    }
    if len(progress) != 1 or any(
        progress[0].get(field) != expected
        for field, expected in expected_progress.items()
    ):
        raise SystemExit("Queue 131 progress is not in interrupted-append recovery state")

    before_report = load_json(ROOT / "tmp/q131-precorrection-compliance.json")
    before_record = paper_record(before_report)
    if (
        before_report.get("report_status") != "correction-required"
        or before_report.get("current_protocol_complete") != 139
        or before_report.get("lifecycle_closed") != 140
        or before_report.get("migration_paper_ids") != [PAPER_ID]
        or before_record.get("protocol_status") != "correction-required"
        or before_record.get("reasons") != CORRECTION_REASONS
    ):
        raise SystemExit("frozen Queue 131 pre-correction compliance is unexpected")

    after_report = load_json(ROOT / "tmp/q131-postfix-precorrection-compliance.json")
    after_record = paper_record(after_report)
    if (
        after_report.get("report_status") != "current-validated"
        or after_report.get("current_protocol_complete") != 140
        or after_report.get("lifecycle_closed") != 140
        or after_report.get("migration_paper_ids") != []
        or after_record.get("protocol_status") != "current-validated"
        or after_record.get("reasons") != []
    ):
        raise SystemExit("post-fix temporary compliance report is not 140/140 clean")

    timestamp = args.timestamp_utc or datetime.now(timezone.utc).replace(
        microsecond=0
    ).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp):
        raise SystemExit("timestamp must be an exact UTC second: YYYY-MM-DDTHH:MM:SSZ")

    draft = {
        "event_type": "paper-corrected",
        "paper_id": PAPER_ID,
        "before": {
            "paper_card_sha256": OLD_CARD_HASH,
            "protocol_status": "correction-required",
            "reasons": CORRECTION_REASONS,
        },
        "after": {
            "artifact_hash_binding": (
                "corrected-machine-readable-core-five-plus-extraction-and-B-branch"
            ),
            "paper_card_sha256": ARTIFACT_HASHES[
                f"artifacts/paper-cards/{PAPER_ID}.json"
            ],
            "paper_card_status": "validated",
            "protocol_status": "current-validated",
            "protocol_v2_language_path": language_path,
            "protocol_v2_model_path": model_path,
            "protocol_v2_model_schema_version": 2,
            "validation_status": "pass",
        },
        "changed_fields": [
            "paper-card.protocol_v2_records.language.path",
            "paper-card.protocol_v2_records.models.path",
            "paper-card.protocol_v2_records.models.schema_version",
            "paper-card.sha256-binding",
        ],
        "artifact_diffs": [
            f"artifact:{relative}|sha256:{sha256}"
            for relative, sha256 in ARTIFACT_HASHES.items()
        ]
        + [
            "Metadata-only correction adds canonical language/model paths and the model schema link; all substantive language, model, audit, observation, visual, result, warning, extraction, and B-branch bytes remain unchanged."
        ],
        "type_branch_diff": {
            "metadata_only": True,
            "new_language_unit_count": 0,
            "new_model_count": 0,
            "new_observation_count": 0,
            "new_rule_impact_count": 0,
            "problem_type": "B",
            "shared_catalog_changes": [],
        },
        "validation_results": [
            {
                "validator": "validate_extraction.py",
                "status": "pass",
                "details": "All 30 pages retain page-aware text, nonblank rendered pixels, and complete visual review.",
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": "The unchanged 296-unit, 15-chapter language record validates with zero errors.",
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": "All 296 unchanged language units pass complete-source anti-copy validation.",
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": "The unchanged 18-model, 15-equation, 33-edge record validates with zero errors.",
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": "The audit cross-validates the corrected card links and all 414 observations with zero errors.",
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": "The corrected card, canonical links, extraction, core artifacts, and 23 B rules cross-validate.",
            },
            {
                "validator": "derive_protocol_compliance.py",
                "status": "pass",
                "details": "A temporary rebuild reports 140/140 current-validated with zero migration debt or correction-required records.",
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": "All 119 regression tests pass after the protocol-link correction.",
            },
            {
                "validator": "validate_plan_protocol.py",
                "status": "pass",
                "details": "The live plan retains the required G0-G8 and prospective-before-live ordering.",
            },
        ],
        "unresolved_added": [],
        "unresolved_resolved": CORRECTION_REASONS,
    }

    if args.check_only:
        print(
            json.dumps(
                {
                    "artifact_declaration_count": len(ARTIFACT_HASHES),
                    "card_changes": sorted(actual_changes),
                    "files_deleted": 0,
                    "paper_id": PAPER_ID,
                    "status": "ready",
                },
                sort_keys=True,
            )
        )
        return

    draft_path.parent.mkdir(parents=True, exist_ok=True)
    with draft_path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(draft, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    with timestamp_path.open("x", encoding="ascii", newline="\n") as handle:
        handle.write(timestamp + "\n")

    print(
        json.dumps(
            {
                "artifact_declaration_count": len(ARTIFACT_HASHES),
                "card_changes": sorted(actual_changes),
                "draft": str(draft_path),
                "files_deleted": 0,
                "paper_id": PAPER_ID,
                "status": "pass",
                "timestamp_utc": timestamp,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
