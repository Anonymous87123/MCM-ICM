#!/usr/bin/env python3
"""Build a create-only Queue 125 closure draft from frozen canonical bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-91566-2607f7ec"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    ("review-proxies/contact-01-05.jpg", 150405, "b596ac0cdd30b7d020680e7a575de06eec45e350954bd90cc05fa80c86970017"),
    ("review-proxies/contact-06-10.jpg", 168211, "23487b8b71aedafb1b58d91ac459edd132b2e7484e427cfffcc69769ac357720"),
    ("review-proxies/contact-11-15.jpg", 152296, "fc552138ca2d6b125d286d979618d38c3e0ee01d4012e8e3c2a2de40e823121b"),
    ("review-proxies/contact-16-20.jpg", 176739, "c4f1bf038f90b0e124223352ff17263d9f5532333fd8a3bf1d162344cb9381e8"),
    ("review-proxies/contact-21-26.jpg", 164119, "6722c3223b26a1d19442d01a2b3f63210b5ae05a08548db0337078f47c741f6b"),
    ("review-proxies/formula-sheet-a.jpg", 402407, "587c1ce8585991d5bc3eb0d2fa49bd9ce4f2a15b265857b3f84fbd11739a8572"),
    ("review-proxies/formula-sheet-b.jpg", 184705, "18d9e378d8dd8447837c156cbc27063a4ba8312507ce52a6556c009afd1a97dd"),
    ("review-proxies/formula-sheet-c.jpg", 348792, "db5c6391b1e8ecbaf4c43cd034ad18710d634126d46a14aa7c188b9747bb6820"),
]

EXPECTED_PATTERNS = {
    "LP-A-ABS-PARAGRAPH-CHAIN": 19,
    "LP-A-ABS-TASK-METHOD-RESULT": 40,
    "LP-A-INT-METHOD-ROADMAP": 14,
    "LP-A-ABS-BOUNDARY": 17,
    "LP-A-INT-OPERATIONAL-DEFINITION": 21,
    "LP-A-ABS-MODEL-STAIRCASE": 9,
    "LP-A-INT-RESEARCH-GAP": 11,
    "LP-A-INT-DEFINITION-TAXONOMY-TO-CHOICE": 9,
}

EXPECTED_RULE_LIFECYCLES = {
    "R-B-LANG-001": "corroborated",
    "R-B-DATA-002": "seed",
    "R-B-MOD-003": "corroborated",
    "R-B-MOD-004": "corroborated",
    "R-B-VER-002": "corroborated",
    "R-B-VER-004": "seed",
    "R-B-VIZ-001": "seed",
    "R-B-LOG-001": "corroborated",
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


def jsonl_count(path: Path) -> int:
    return len(load_jsonl(path))


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
    expected_pages = list(range(1, 27))
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
        raise SystemExit("extraction review does not cover physical pages 1-26")
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
    if audit_files != expected_audit_files:
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
        "contact_sheet_proxy_count": 5,
        "focused_crop_proxy_count": 3,
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
        raise SystemExit("refusing to overwrite Queue 125 draft or timestamp")

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
        raise SystemExit(f"expected one Queue 125 progress record; found {len(progress_matches)}")
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
            raise SystemExit(f"Queue 125 progress {field} changed ({progress.get(field)!r} != {expected!r})")
    if progress.get("queue_position") != 125 or progress.get("problem_type") != "B" or progress.get("year") != "2018":
        raise SystemExit("Queue 125 progress identity changed")

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
        "observation_count": jsonl_count(observations_path),
        "warning_count": len(card["unresolved_questions"]),
        "formula_warning_count": len(audit["formula_error_watch"]["warnings"]),
        "section_count": len(audit["organization_logic"]["section_progressions"]),
        "argument_count": len(audit["organization_logic"]["main_argument_chains"]),
        "abstract_paragraph_count": paragraph_count(audit, "abstract"),
        "introduction_paragraph_count": paragraph_count(audit, "introduction"),
        "rule_change_count": impact["rule_change_count"],
        "rule_count": jsonl_count(rules_path),
        "test_count": args.validated_test_count,
        **review,
    }
    expected_counts = {
        "page_count": 26,
        "chapter_count": 19,
        "language_count": 140,
        "positive_reusable_language_count": 140,
        "weakness_count": 10,
        "model_count": 17,
        "equation_count": 30,
        "dependency_edge_count": 20,
        "visual_count": 23,
        "observation_count": 301,
        "warning_count": 18,
        "formula_warning_count": 8,
        "section_count": 19,
        "argument_count": 5,
        "abstract_paragraph_count": 5,
        "introduction_paragraph_count": 9,
        "rule_change_count": 8,
        "rule_count": 23,
        "test_count": 119,
        "proxy_count": 8,
        "contact_sheet_proxy_count": 5,
        "focused_crop_proxy_count": 3,
        "segment_count": 1,
        "total_proxy_bytes": 1747674,
        "largest_proxy_bytes": 402407,
    }
    errors = [
        f"{field} differs from validated Queue 125 value ({counts[field]} != {expected})"
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
    if any(len(item.get("added_evidence_ids", [])) != 2 for item in changes):
        errors.append("each Q125 rule impact must add exactly two source-matched observations")
    if impact.get("output_sha256") != digest(rules_path):
        errors.append("rule-impact output hash does not bind frozen B rules")
    if counts["warning_count"] >= counts["language_count"]:
        errors.append("unresolved question count is not a strict minority of language units")
    if counts["weakness_count"] >= counts["positive_reusable_language_count"]:
        errors.append("weakness count is not below positive reusable language evidence")
    if dimensions["language"] <= max(count for dimension, count in dimensions.items() if dimension != "language"):
        errors.append("language is not the strictly largest evidence dimension")
    protocol = card.get("protocol_v2_records", {})
    if protocol.get("language", {}).get("path") != f"artifacts/language-units/{PAPER_ID}.json":
        errors.append("card language canonical path is incorrect")
    if protocol.get("models", {}).get("path") != f"artifacts/model-units/{PAPER_ID}.json":
        errors.append("card model canonical path is incorrect")
    if errors:
        raise SystemExit("Queue 125 frozen-state mismatch: " + "; ".join(errors))

    timestamp = args.timestamp_utc or datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
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
                    f"five contact-sheet JPEGs cover pages 1-26 and three focused JPEGs preserve equations 1-30, "
                    f"including the low-legibility dependency regions, with all {counts['proxy_count']} proxy hashes frozen."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all {counts['chapter_count']} "
                    "substantive chapters after Abstract and Introduction first-pass reading, explicit exclusion of the "
                    "contents page from positive author evidence, and a final zero-new-move saturation pass; "
                    "the eight retained rhetorical patterns occur "
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
                    f"and {counts['dependency_edge_count']} handoff edges across bilingual transition flows, the 26-language "
                    "world state, country-language competition, natural growth, migration coupling, short-window calibration, "
                    "fifty-year forecasts, geographic comparison, marginal office economics, and sensitivity analysis."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} five-part chapter contracts, {counts['abstract_paragraph_count']} Abstract moves, "
                    f"{counts['introduction_paragraph_count']} Introduction moves, {counts['argument_count']} main chains, "
                    f"{counts['visual_count']} visual dispositions, and {counts['formula_warning_count']} equation-bound final "
                    f"warnings passed; positive reusable language {counts['positive_reusable_language_count']} strictly exceeds "
                    f"weakness evidence {counts['weakness_count']}."
                ),
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": (
                    f"The card, {counts['observation_count']} observations, {counts['rule_count']} cumulative B rules, "
                    "extraction, language record, model record, and complete 26-page visual review cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    f"Two independent replays are byte-identical at {digest(rules_path)}; eight nominated B rules each "
                    "received two paper-matched observations about language claims, parameter provenance, typed model fusion, "
                    "output semantics, validation scope, mathematical preflight, decision visuals, and task-to-memo traceability, "
                    "while all seed/corroborated lifecycle labels remained unchanged."
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
                "details": f"All {counts['test_count']} regression tests pass against the Queue 125 frozen bytes and current formal baseline.",
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    f"One bounded context segment contains exactly {counts['proxy_count']} JPEGs/{counts['total_proxy_bytes']} bytes; "
                    f"the largest is {counts['largest_proxy_bytes']} bytes, below the 450,000-byte limit. No original page/contact PNG, "
                    "full session JSONL, or printed base64 entered model context; the prior 413 is attributed to accumulated request "
                    "history plus image/base64 payload at nginx ingress, while the exact server-side byte threshold remains unobservable."
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
