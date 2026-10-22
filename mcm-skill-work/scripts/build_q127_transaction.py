#!/usr/bin/env python3
"""Build a create-only Queue 127 closure draft from frozen canonical bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2019-1908904-8b5a9e33"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    ("review-proxies/01-pages-0001-0005.jpg", 426468, "3bd9851bca767ee16cbe2fff6460f3889fc5187e8af78c02b38d526316ca8d69"),
    ("review-proxies/02-pages-0006-0010.jpg", 418834, "9530fc51ab46ef0487c428af4fbd7d75c9eff6d60266864aad1bdea94952d916"),
    ("review-proxies/03-pages-0011-0015.jpg", 449239, "37f4ed5050f596b387874546d77b34ffb483e7c087ddcbc92ccc8c950e1d8cb4"),
    ("review-proxies/04-pages-0016-0020.jpg", 421482, "48e1b6063add0c720f87af40d215e32adb6b1926c412ac84d93d731ac1e3ee16"),
    ("review-proxies/05-pages-0021-0025.jpg", 392984, "1b6e1bf4a3ac43c64aeaf28d585f8ba7af9d6a0bd698492b79fde1df2230cd1c"),
    ("review-proxies/06-pages-0026-0030.jpg", 341634, "bd79d17c7c7450d82ef2fae29e33d1a4460fbcd7ddf1493a4c5e8384cb95484f"),
    ("review-proxies/07-pages-0031-0033.jpg", 193366, "9c308337b7a01fa4cec3ab701ab561d39609de6238014acee8442253394feb4a"),
    ("review-proxies/08-crop-page-0013-distance-and-rough-location.jpg", 202103, "6ce7b238f3e96511414233e574814c61adc76d8f4c6dba71cf48ceab05c286bb"),
]

EXPECTED_CORE_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": "4a7c53f5765d94c1395b4b13e70f8b562744e9e9692c63545998e9c891ced8d9",
    f"artifacts/language-units/{PAPER_ID}.json": "459f7380c94de1e3db78ac0fd6f120ea9b851c093c627a4d490d6a6096fe10d5",
    f"artifacts/model-units/{PAPER_ID}.json": "fccbd360a7effed1e6b0d122ec5598f2bbc592d40e9f8fa31d0622a885578b06",
    f"artifacts/learning-audits/{PAPER_ID}.json": "8de7b5fee3818d7d88feda75b83c08875422087101a0d26ba0d36519a6a64de4",
    f"artifacts/observations/{PAPER_ID}.jsonl": "ba1fcac36dfd42f341ebb2438ab5e415e3d3de24d6aa5910809887c9d6b9b9f2",
    f"artifacts/papers/{PAPER_ID}/extraction.json": "94e1f2025b4f8bce02021eb7ad125bc16fc54ff97b2a7fd29eadf80a148cf0a5",
    "artifacts/type-branches/B/rules.jsonl": "145836c4285dc870bcefc4b310a0671ae3467566a32018b649da4d47beb581a0",
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": "7e5e3fe173cf6cb175874be43373bb2b7a19261f0891db8dbfbfd40321c6cf51",
}

EXPECTED_PATTERNS = {
    "LP-B-ABS-STAGE-RESULT": 19,
    "LP-B-ALG-STATE-ACTION-STOP": 28,
    "LP-B-ASM-CLAIM-JUSTIFICATION": 13,
    "LP-B-DEC-PREFERENCE-PARAMETER": 6,
    "LP-B-INT-TASK-ROADMAP": 13,
    "LP-B-MEMO-NEED-SYSTEM-ACTION": 7,
    "LP-B-MOD-DEFINITION-EQUATION": 29,
    "LP-B-RES-VISUAL-CLAIM": 21,
}

EXPECTED_RULE_LIFECYCLES = {
    "R-B-LANG-001": "corroborated",
    "R-B-DATA-002": "seed",
    "R-B-MOD-003": "corroborated",
    "R-B-MOD-004": "corroborated",
    "R-B-COMP-001": "seed",
    "R-B-VER-002": "corroborated",
    "R-B-VER-004": "seed",
    "R-B-VIZ-001": "seed",
    "R-B-LOG-001": "corroborated",
}

EXPECTED_ADDED_EVIDENCE_COUNTS = {
    "R-B-LANG-001": 3,
    "R-B-DATA-002": 3,
    "R-B-MOD-003": 3,
    "R-B-MOD-004": 2,
    "R-B-COMP-001": 3,
    "R-B-VER-002": 3,
    "R-B-VER-004": 3,
    "R-B-VIZ-001": 3,
    "R-B-LOG-001": 3,
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


def paragraph_count(audit: dict[str, Any], chapter: str) -> int:
    matches = [
        item for item in audit["paragraph_chains"] if item.get("chapter") == chapter
    ]
    if len(matches) != 1:
        raise SystemExit(f"expected one {chapter} paragraph chain; found {len(matches)}")
    return len(matches[0]["paragraphs"])


def verify_review_proxies(
    extraction: dict[str, Any], audit: dict[str, Any]
) -> dict[str, Any]:
    manifest = audit.get("visual_review_manifest")
    if not isinstance(manifest, dict):
        raise SystemExit("learning audit has no visual_review_manifest")
    expected_paths = [item[0] for item in EXPECTED_PROXIES]
    expected_sizes = {path: size for path, size, _ in EXPECTED_PROXIES}
    expected_hashes = {path: sha256 for path, _, sha256 in EXPECTED_PROXIES}

    records = manifest.get("files")
    record_paths = [
        f"review-proxies/{item.get('file')}" for item in records
    ] if isinstance(records, list) else []
    if record_paths != expected_paths:
        raise SystemExit("review proxy identity or order changed")

    root = PAPER_ROOT.resolve()
    actual_names = sorted(
        path.name for path in (PAPER_ROOT / "review-proxies").iterdir()
        if path.is_file()
    )
    if actual_names != sorted(Path(path).name for path in expected_paths):
        raise SystemExit("review proxy directory contains an unexpected file set")

    verified: list[dict[str, Any]] = []
    for record in records:
        relative = f"review-proxies/{record['file']}"
        canonical = f"artifacts/papers/{PAPER_ID}/{relative}"
        if record.get("path") != canonical:
            raise SystemExit(f"review proxy canonical path changed: {relative}")
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise SystemExit(f"unsafe review proxy path: {relative}")
        path = (root / candidate).resolve()
        try:
            path.relative_to(root)
        except ValueError as error:
            raise SystemExit(f"review proxy escapes paper root: {relative}") from error
        if not path.is_file() or path.suffix.lower() != ".jpg":
            raise SystemExit(f"missing byte-bounded JPEG review proxy: {relative}")
        size = path.stat().st_size
        sha256 = digest(path)
        if size != expected_sizes[relative] or record.get("bytes") != size:
            raise SystemExit(f"review proxy byte count changed: {relative}")
        if sha256 != expected_hashes[relative] or record.get("sha256") != sha256:
            raise SystemExit(f"review proxy hash changed: {relative}")
        if size > 450_000:
            raise SystemExit(f"review proxy exceeds 450,000 bytes: {relative}")
        verified.append({"path": relative, "bytes": size, "sha256": sha256})

    total = sum(item["bytes"] for item in verified)
    largest = max(item["bytes"] for item in verified)
    expected_pages = list(range(1, 34))
    extraction_review = extraction.get("visual_review")
    if (
        manifest.get("coverage_status") != "complete"
        or manifest.get("physical_pages_reviewed") != expected_pages
        or manifest.get("proxy_byte_limit") != 450_000
        or manifest.get("all_proxies_within_limit") is not True
        or manifest.get("original_pngs_retained_on_disk") is not True
    ):
        raise SystemExit("learning-audit visual manifest differs from frozen review state")
    if (
        not isinstance(extraction_review, dict)
        or extraction_review.get("status") != "complete"
        or extraction_review.get("reviewed_pages") != expected_pages
        or extraction.get("visual_review_status") != "complete"
    ):
        raise SystemExit("extraction review does not cover physical pages 1-33")
    if len(verified) > 8 or total >= 4 * 1024 * 1024:
        raise SystemExit("review context segment exceeds the request-body guard")

    guard = audit.get("gate_attestation", {}).get("request_body_guard")
    if not isinstance(guard, dict):
        raise SystemExit("learning audit has no request_body_guard")
    audit_files = guard.get("proxy_files")
    expected_audit_files = [
        {"file": Path(path).name, "bytes": size, "sha256": sha256}
        for path, size, sha256 in EXPECTED_PROXIES
    ]
    audit_file_projection = [
        {key: item.get(key) for key in ("file", "bytes", "sha256")}
        for item in audit_files
    ] if isinstance(audit_files, list) else []
    manifest_without_paths = [
        {key: value for key, value in item.items() if key != "path"}
        for item in records
    ]
    if (
        audit_file_projection != expected_audit_files
        or audit_files != manifest_without_paths
    ):
        raise SystemExit("learning-audit proxy ledger differs from frozen JPEGs")
    if (
        guard.get("proxy_byte_limit") != 450_000
        or guard.get("review_proxy_count") != len(verified)
        or guard.get("review_proxy_total_bytes") != total
        or guard.get("largest_proxy_bytes") != largest
        or guard.get("full_page_png_sent_to_model") is not False
        or guard.get("full_session_jsonl_sent_to_model") is not False
        or guard.get("base64_content_printed") is not False
        or guard.get("additional_images_in_current_context_allowed") is not False
    ):
        raise SystemExit("learning-audit request-body guard differs from frozen review state")
    return {
        "proxy_count": len(verified),
        "contact_sheet_proxy_count": 7,
        "focused_crop_proxy_count": 1,
        "segment_count": 1,
        "total_proxy_bytes": total,
        "largest_proxy_bytes": largest,
        "proxies": verified,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validated-test-count", required=True, type=int)
    parser.add_argument("--timestamp-utc")
    args = parser.parse_args()
    if args.validated_test_count <= 0:
        raise SystemExit("validated test count must be positive")

    draft_path = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    timestamp_path = ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt"
    if draft_path.exists() or timestamp_path.exists():
        raise SystemExit("refusing to overwrite Queue 127 draft or timestamp")

    canonical = {
        f"artifacts/paper-cards/{PAPER_ID}.json": ROOT / f"artifacts/paper-cards/{PAPER_ID}.json",
        f"artifacts/language-units/{PAPER_ID}.json": ROOT / f"artifacts/language-units/{PAPER_ID}.json",
        f"artifacts/model-units/{PAPER_ID}.json": ROOT / f"artifacts/model-units/{PAPER_ID}.json",
        f"artifacts/learning-audits/{PAPER_ID}.json": ROOT / f"artifacts/learning-audits/{PAPER_ID}.json",
        f"artifacts/observations/{PAPER_ID}.jsonl": ROOT / f"artifacts/observations/{PAPER_ID}.jsonl",
        f"artifacts/papers/{PAPER_ID}/extraction.json": PAPER_ROOT / "extraction.json",
        "artifacts/type-branches/B/rules.jsonl": ROOT / "artifacts/type-branches/B/rules.jsonl",
        f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": ROOT / f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json",
        **{
            f"artifacts/papers/{PAPER_ID}/{relative}": PAPER_ROOT / relative
            for relative, _, _ in EXPECTED_PROXIES
        },
    }
    missing = [str(path) for path in canonical.values() if not path.is_file()]
    if missing:
        raise SystemExit(f"missing frozen source(s): {missing}")
    for relative, expected_hash in EXPECTED_CORE_HASHES.items():
        actual_hash = digest(canonical[relative])
        if actual_hash != expected_hash:
            raise SystemExit(
                f"Queue 127 frozen core hash changed: {relative} "
                f"{actual_hash} != {expected_hash}"
            )

    card = load_json(canonical[f"artifacts/paper-cards/{PAPER_ID}.json"])
    language = load_json(canonical[f"artifacts/language-units/{PAPER_ID}.json"])
    models = load_json(canonical[f"artifacts/model-units/{PAPER_ID}.json"])
    audit = load_json(canonical[f"artifacts/learning-audits/{PAPER_ID}.json"])
    extraction = load_json(canonical[f"artifacts/papers/{PAPER_ID}/extraction.json"])
    impact = load_json(canonical[f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json"])
    observations_path = canonical[f"artifacts/observations/{PAPER_ID}.jsonl"]
    rules_path = canonical["artifacts/type-branches/B/rules.jsonl"]

    for name, record in (
        ("card", card),
        ("language", language),
        ("models", models),
        ("audit", audit),
        ("extraction", extraction),
        ("impact", impact),
    ):
        if record.get("paper_id") != PAPER_ID:
            raise SystemExit(f"{name} paper_id mismatch")

    progress_matches = [
        record
        for record in load_jsonl(ROOT / "artifacts/progress.jsonl")
        if record.get("paper_id") == PAPER_ID
    ]
    if len(progress_matches) != 1:
        raise SystemExit(f"expected one Queue 127 progress record; found {len(progress_matches)}")
    progress = progress_matches[0]
    expected_before = {
        "branch_update_status": "pending",
        "extraction_status": "pending",
        "paper_card_status": "pending",
        "protocol_status": "absent",
        "status": "discovered",
        "validation_status": "pending",
    }
    for field, expected in expected_before.items():
        if field != "protocol_status" and progress.get(field) != expected:
            raise SystemExit(
                f"Queue 127 progress {field} changed "
                f"({progress.get(field)!r} != {expected!r})"
            )
    if (
        progress.get("queue_position") != 127
        or progress.get("problem_type") != "B"
        or progress.get("year") != "2019"
    ):
        raise SystemExit("Queue 127 progress identity changed")

    review = verify_review_proxies(extraction, audit)
    dispositions = audit.get("language_unit_dispositions", [])
    computed_positive = sum(
        item.get("disposition") != "paper-specific-nonreusable"
        for item in dispositions
        if isinstance(item, dict)
    )
    patterns = {
        item.get("pattern_id"): item.get("occurrences")
        for item in language.get("repeated_patterns", [])
        if isinstance(item, dict)
    }
    counts = {
        "page_count": extraction["page_count"],
        "chapter_count": len(language["available_chapters"]),
        "language_count": len(language["units"]),
        "positive_reusable_language_count": audit["positive_reusable_language_count"],
        "weakness_count": audit["dimension_counts"]["weakness"],
        "model_count": len(models["models"]),
        "equation_count": sum(len(model["governing_equations"]) for model in models["models"]),
        "dependency_edge_count": len(models["dependency_edges"]),
        "visual_count": len(card["visualization_observations"]),
        "observation_count": len(load_jsonl(observations_path)),
        "warning_count": len(card["unresolved_questions"]),
        "formula_warning_count": len(audit["formula_error_watch"]["warnings"]),
        "section_count": len(audit["organization_logic"]["section_progressions"]),
        "argument_count": len(audit["organization_logic"]["main_argument_chains"]),
        "abstract_paragraph_count": paragraph_count(audit, "abstract"),
        "introduction_paragraph_count": paragraph_count(audit, "introduction"),
        "rule_change_count": impact["rule_change_count"],
        "rule_count": len(load_jsonl(rules_path)),
        "test_count": args.validated_test_count,
        **review,
    }
    expected_counts = {
        "page_count": 33,
        "chapter_count": 18,
        "language_count": 130,
        "positive_reusable_language_count": 130,
        "weakness_count": 18,
        "model_count": 14,
        "equation_count": 32,
        "dependency_edge_count": 21,
        "visual_count": 18,
        "observation_count": 246,
        "warning_count": 20,
        "formula_warning_count": 12,
        "section_count": 18,
        "argument_count": 6,
        "abstract_paragraph_count": 5,
        "introduction_paragraph_count": 5,
        "rule_change_count": 9,
        "rule_count": 23,
        "test_count": 119,
        "proxy_count": 8,
        "contact_sheet_proxy_count": 7,
        "focused_crop_proxy_count": 1,
        "segment_count": 1,
        "total_proxy_bytes": 2846110,
        "largest_proxy_bytes": 449239,
    }
    errors = [
        f"{field} differs from validated Queue 127 value ({counts[field]} != {expected})"
        for field, expected in expected_counts.items()
        if counts[field] != expected
    ]
    dimensions = audit["dimension_counts"]
    changes = impact.get("changes", [])
    changed_lifecycles = {
        item.get("rule_id"): item.get("lifecycle_unchanged")
        for item in changes
        if isinstance(item, dict)
    }
    added_counts = {
        item.get("rule_id"): len(item.get("added_evidence_ids", []))
        for item in changes
        if isinstance(item, dict)
    }
    valid_roles = {"input", "state", "parameter", "intermediate", "output"}
    invalid_roles = [
        (model["model_id"], variable["symbol"], variable["role"])
        for model in models["models"]
        for variable in model["variables"]
        if variable.get("role") not in valid_roles
    ]
    if extraction.get("visual_review_status") != "complete":
        errors.append("visual review is not complete")
    if dimensions.get("language") != counts["language_count"]:
        errors.append("audit language dimension differs from language-unit count")
    if counts["positive_reusable_language_count"] != computed_positive:
        errors.append("positive reusable language count differs from dispositions")
    if patterns != EXPECTED_PATTERNS:
        errors.append("repeated-language pattern occurrences changed")
    if len(changes) != counts["rule_change_count"] or changed_lifecycles != EXPECTED_RULE_LIFECYCLES:
        errors.append("rule-impact changes or preserved lifecycles changed")
    if added_counts != EXPECTED_ADDED_EVIDENCE_COUNTS:
        errors.append("per-rule Q127 added-evidence counts changed")
    if impact.get("output_sha256") != digest(rules_path):
        errors.append("rule-impact output hash does not bind frozen B rules")
    if invalid_roles:
        errors.append(f"model variables retain invalid schema roles: {invalid_roles}")
    if counts["warning_count"] >= counts["language_count"]:
        errors.append("unresolved question count is not a strict minority of language units")
    if counts["weakness_count"] >= counts["positive_reusable_language_count"]:
        errors.append("weakness count is not below positive reusable language evidence")
    if dimensions["language"] <= max(
        count for dimension, count in dimensions.items() if dimension != "language"
    ):
        errors.append("language is not the strictly largest evidence dimension")
    protocol = card.get("protocol_v2_records", {})
    if protocol.get("language", {}).get("path") != f"artifacts/language-units/{PAPER_ID}.json":
        errors.append("card language canonical path is incorrect")
    if protocol.get("models", {}).get("path") != f"artifacts/model-units/{PAPER_ID}.json":
        errors.append("card model canonical path is incorrect")
    if errors:
        raise SystemExit("Queue 127 frozen-state mismatch: " + "; ".join(errors))

    timestamp = args.timestamp_utc or datetime.now(timezone.utc).replace(
        microsecond=0
    ).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp):
        raise SystemExit("timestamp must be an exact UTC second: YYYY-MM-DDTHH:MM:SSZ")

    draft = {
        "after": {
            "artifact_hash_binding": "machine-readable-core-five-plus-extraction-review-proxies-and-B-branch",
            "branch_update_status": "validated",
            "dimension_counts": dimensions,
            "equation_count": counts["equation_count"],
            "extraction_status": "validated",
            "extraction_visual_review_status": extraction["visual_review_status"],
            "important_visual_count": counts["visual_count"],
            "language_pattern_occurrences": patterns,
            "language_unit_count": counts["language_count"],
            "model_count": counts["model_count"],
            "observation_count": counts["observation_count"],
            "paper_card_status": "validated",
            "positive_reusable_language_count": counts["positive_reusable_language_count"],
            "protocol_status": "current-validated",
            "section_contract_count": counts["section_count"],
            "source_action_count": counts["language_count"],
            "status": "closed",
            "validation_status": "pass",
            "warning_count": counts["warning_count"],
        },
        "artifact_diffs": [
            f"artifact:{relative}|sha256:{digest(path)}"
            for relative, path in canonical.items()
        ],
        "before": expected_before,
        "changed_fields": [
            "progress.status",
            "progress.extraction_status",
            "progress.paper_card_status",
            "progress.branch_update_status",
            "progress.validation_status",
            "paper-card",
            "language-units",
            "model-units",
            "learning-audit",
            "observations",
            "extraction.visual-review-manifest",
            "review-proxies",
            "type-branch.B.rules",
            "type-branch.B.rule-impact-report",
        ],
        "event_type": "paper-closed",
        "history_completeness": "native",
        "paper_id": PAPER_ID,
        "type_branch_diff": {
            "new_equation_count": counts["equation_count"],
            "new_language_unit_count": counts["language_count"],
            "new_model_count": counts["model_count"],
            "new_observation_count": counts["observation_count"],
            "new_rule_impact_count": counts["rule_change_count"],
            "problem_type": "B",
            "section_contracts_after": counts["section_count"],
            "section_contracts_before": 0,
            "shared_catalog_changes": [],
            "updated_rule_ids": list(EXPECTED_RULE_LIFECYCLES),
        },
        "unresolved_added": card["unresolved_questions"],
        "unresolved_resolved": [],
        "validation_results": [
            {
                "validator": "validate_extraction.py",
                "status": "pass",
                "details": (
                    f"All {counts['page_count']} physical pages retain page-aware text and rendered pixels; "
                    "seven contact-sheet JPEGs cover pages 1-33 in order, and one focused JPEG crop preserves "
                    "the page-13 distance equations and rough-location diagram, with all eight proxy hashes frozen."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all {counts['chapter_count']} "
                    "substantive chapters after Abstract and Introduction first-pass reading and a final "
                    "zero-new-move saturation pass; the eight retained rhetorical patterns occur "
                    + ", ".join(f"{key}={value}" for key, value in patterns.items())
                    + "."
                ),
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']}/{counts['language_count']} language units passed complete-source "
                    "anti-copy checks with two original instantiations each and no full-clause, unique-shingle, "
                    "source-fact, or eight-word-run leakage."
                ),
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} model units retain {counts['equation_count']} visually checked equations "
                    f"and {counts['dependency_edge_count']} handoff edges across AHP weighting, criterion normalization, "
                    "greedy fleet construction, range geometry, medicine allocation, three-dimensional packing, "
                    "raster siting, timetable construction, and sensitivity analysis; all variables use "
                    "the schema roles input/state/parameter/intermediate/output."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} five-part chapter contracts, {counts['abstract_paragraph_count']} Abstract "
                    f"moves, {counts['introduction_paragraph_count']} Introduction moves, {counts['argument_count']} main "
                    f"chains, {counts['visual_count']} visual dispositions, and {counts['formula_warning_count']} final "
                    f"formula/claim warnings passed; positive reusable language {counts['positive_reusable_language_count']} "
                    f"strictly exceeds weakness evidence {counts['weakness_count']}."
                ),
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": (
                    f"The card, {counts['observation_count']} observations, {counts['rule_count']} cumulative B rules, "
                    "extraction, language record, model record, and complete 33-page visual review cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    f"Three independent runs are byte-identical at {digest(rules_path)}; "
                    f"{counts['rule_change_count']} nominated B rules received 26 paper-matched observations about "
                    "claim scope, provenance, typed physical-to-decision interfaces, output semantics, computation, "
                    "validation, mathematical preflight, auditable visuals, and memo traceability, while all "
                    "seed/corroborated lifecycle labels remained unchanged."
                ),
            },
            {
                "validator": "validate_plan_protocol.py",
                "status": "pass",
                "details": "The live plan retains language-first G0-G8 ordering and prospective-before-live transaction ordering.",
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": f"All {counts['test_count']} regression tests pass against the Queue 127 frozen bytes and current formal baseline.",
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    f"One bounded context segment contains exactly {counts['proxy_count']} JPEGs/"
                    f"{counts['total_proxy_bytes']} bytes; the largest is {counts['largest_proxy_bytes']} bytes, below "
                    "the 450,000-byte limit. No original full-page PNG, complete session JSONL, or printed base64 entered "
                    "model context; the prior HTTP 413 is an nginx ingress rejection caused by the accumulated serialized "
                    "request, while the exact server-side threshold remains unobservable."
                ),
            },
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
                "paper_id": PAPER_ID,
                "draft": str(draft_path),
                "timestamp_utc": timestamp,
                **counts,
                "pattern_occurrences": patterns,
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
