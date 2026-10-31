#!/usr/bin/env python3
"""Build a create-only metadata correction draft for Queue 128 protocol links."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2019-1915782-41065334"
OLD_CARD_HASH = "aa91a30e7c736ae338ab0873d30ce5046ad05b1ef8426833b68246f321e47bf7"
PRIOR_EVENT_ID = "TX-000186-86e86a1961a8"
PRIOR_EVENT_HASH = "8a7698cfb1f41f7d6fdcc1d216364ae1ede687f181e3bd2768a55f3c85f1664f"

ARTIFACT_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": "9f9b83c53b7cb642e23ee84f107694aa87a460042da5d959dff1760230d22d01",
    f"artifacts/language-units/{PAPER_ID}.json": "984a1d2408e98627f5635dd06f7a55ba28aa3699902aa062c50854c50ef53f37",
    f"artifacts/model-units/{PAPER_ID}.json": "a19fe5c43d3d7548f92c6d0af8be8f3fc926e8630d5c00c9888950ae5ef9f08d",
    f"artifacts/learning-audits/{PAPER_ID}.json": "4b2b6c804022010aa2a8c3a6cbb12fef02f35b86a2c9b8a9cd9c97b94e9e5119",
    f"artifacts/observations/{PAPER_ID}.jsonl": "5f152562fccb04c30db54e29f0301834411178b1851e66ada72f7a2544105442",
    f"artifacts/papers/{PAPER_ID}/extraction.json": "b1207cf5d634ec038baf3090c8cbda95acdc44ccf15b197f16b56b2bdf4e6d47",
    "artifacts/type-branches/B/rules.jsonl": "58636c86db381f49e64b54e1595385193bc60c21d62aa46f476d4282ca26586b",
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": "f0d6550852b5fcdb9ff79e8136abbac68a4227c36cc1b5dc0c98164850393a08",
}

EXPECTED_CARD_CHANGES = {
    "protocol_v2_records.language.path",
    "protocol_v2_records.models.path",
    "protocol_v2_records.models.schema_version",
}


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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timestamp-utc")
    args = parser.parse_args()

    draft_path = ROOT / f"artifacts/transactions/{PAPER_ID}-protocol-path-correction-draft.json"
    timestamp_path = ROOT / f"tmp/{PAPER_ID}-protocol-path-correction-timestamp.txt"
    if draft_path.exists() or timestamp_path.exists():
        raise SystemExit("refusing to overwrite Queue 128 correction draft or timestamp")

    for relative, expected_hash in ARTIFACT_HASHES.items():
        path = ROOT / relative
        if not path.is_file():
            raise SystemExit(f"missing correction artifact: {relative}")
        actual_hash = digest(path)
        if actual_hash != expected_hash:
            raise SystemExit(
                f"correction artifact changed: {relative} {actual_hash} != {expected_hash}"
            )

    old_card_path = ROOT / f"tmp/q128-stage-v1/paper-card-{PAPER_ID}.json"
    if digest(old_card_path) != OLD_CARD_HASH:
        raise SystemExit("Queue 128 pre-correction card is not the frozen closed-event card")
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
        raise SystemExit("Queue 128 corrected protocol links are incomplete")

    history = load_jsonl(ROOT / "artifacts/transactions/history.jsonl")
    if len(history) != 186:
        raise SystemExit(f"expected 186 pre-correction events; found {len(history)}")
    last = history[-1]
    if last.get("event_id") != PRIOR_EVENT_ID or last.get("event_hash") != PRIOR_EVENT_HASH:
        raise SystemExit("live history advanced after Queue 128 paper-close append")
    old_declaration = (
        f"artifact:artifacts/paper-cards/{PAPER_ID}.json|sha256:{OLD_CARD_HASH}"
    )
    if old_declaration not in last.get("artifact_diffs", []):
        raise SystemExit("Queue 128 close event does not declare the pre-correction card")

    progress = [
        item
        for item in load_jsonl(ROOT / "artifacts/progress.jsonl")
        if item.get("paper_id") == PAPER_ID
    ]
    if len(progress) != 1 or any(
        progress[0].get(field) != expected
        for field, expected in {
            "status": "closed",
            "extraction_status": "validated",
            "paper_card_status": "validated",
            "branch_update_status": "validated",
            "validation_status": "pass",
        }.items()
    ):
        raise SystemExit("Queue 128 progress is not in the interrupted-append recovery state")

    compliance = load_json(ROOT / "tmp/q128-postfix-precorrection-compliance.json")
    paper_records = [
        item for item in compliance.get("records", []) if item.get("paper_id") == PAPER_ID
    ]
    if (
        compliance.get("report_status") != "current-validated"
        or compliance.get("current_protocol_complete") != 137
        or compliance.get("migration_paper_ids") != []
        or len(paper_records) != 1
        or paper_records[0].get("protocol_status") != "current-validated"
        or paper_records[0].get("reasons") != []
    ):
        raise SystemExit("post-fix temporary compliance report is not 137/137 clean")

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
            "reasons": [
                "card:language-path-mismatch",
                "card:model-path-mismatch",
            ],
        },
        "after": {
            "artifact_hash_binding": "corrected-machine-readable-core-five-plus-extraction-and-B-branch",
            "paper_card_sha256": ARTIFACT_HASHES[f"artifacts/paper-cards/{PAPER_ID}.json"],
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
            "Metadata-only correction adds the canonical language/model paths and model schema link; all substantive language, model, audit, observation, visual, result, warning, extraction, and type-branch bytes remain unchanged."
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
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": "The unchanged 152-unit, 17-chapter language record validates with zero errors.",
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": "The unchanged 13-model, 30-equation, 19-edge record validates with zero errors.",
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": "The audit cross-validates the corrected paper-card declarations and all 253 observations with zero errors.",
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": "The corrected card, canonical protocol links, core artifacts, extraction, observations, and 23 B rules cross-validate with zero errors.",
            },
            {
                "validator": "derive_protocol_compliance.py",
                "status": "pass",
                "details": "A temporary rebuild reports 137/137 current-validated, this paper current-validated with no reasons, and zero migration debt.",
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": "All 119 regression tests pass after the protocol-link correction.",
            },
        ],
        "unresolved_added": [],
        "unresolved_resolved": [
            "card:language-path-mismatch",
            "card:model-path-mismatch",
        ],
    }

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
                "paper_id": PAPER_ID,
                "status": "pass",
                "timestamp_utc": timestamp,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
