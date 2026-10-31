#!/usr/bin/env python3
"""Build a create-only Queue 124 closure draft from frozen canonical bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-79002-238b850f"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    ("review-proxies/contact-01-05.jpg", 256385, "c5971e08399ee31cd026b36182d223447ad8a75573536c7ceb4a7d83597776aa"),
    ("review-proxies/contact-06-10.jpg", 226642, "913e39f8b1f724bf4f80d6d4d9437b5f47feb80ca2e05b14f95319c34a14bb49"),
    ("review-proxies/contact-11-15.jpg", 228864, "1f6a12912ff0cd6e9cb72de1252e9cff04a403b6e705732d324b3fa49a8146af"),
    ("review-proxies/contact-16-20.jpg", 242135, "f69bd3286d9b980b059d148bd39e4055964142da4aac5f748230fd63f5edebad"),
    ("review-proxies/contact-21-25.jpg", 197850, "b7074841290b30cd2839b6e0028e4e70717c9ab049061b3ce986c8a82a789db0"),
    ("review-proxies/contact-26-29.jpg", 107038, "7c4a06b487507793983e4d7225fb9ad1ee87b3ed459a9935744497b9be516a16"),
    ("review-proxies/formula-evidence.jpg", 195469, "115131dc40a1241ddc0f9c85aa234882bb77cdcc944a1ff6014320eb51599c8e"),
    ("review-proxies/code-evidence.jpg", 145077, "39be1a155096c0d203a45ee33296675adabc2f156ec646cbb4b587453c344e1a"),
]

EXPECTED_PATTERNS = {
    "LP-A-ABS-PARAGRAPH-CHAIN": 11,
    "LP-A-ABS-TASK-METHOD-RESULT": 36,
    "LP-A-INT-METHOD-ROADMAP": 11,
    "LP-A-ABS-BOUNDARY": 16,
    "LP-A-INT-OPERATIONAL-DEFINITION": 13,
    "LP-A-ABS-MODEL-STAIRCASE": 41,
    "LP-A-INT-RESEARCH-GAP": 4,
    "LP-A-INT-DEFINITION-TAXONOMY-TO-CHOICE": 8,
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
    manifest = extraction.get("visual_review_manifest")
    if not isinstance(manifest, dict):
        raise SystemExit("extraction has no visual_review_manifest")
    expected_paths = [item[0] for item in EXPECTED_PROXIES]
    expected_sizes = {path: size for path, size, _ in EXPECTED_PROXIES}
    expected_hashes = {path: sha256 for path, _, sha256 in EXPECTED_PROXIES}

    records = manifest.get("proxy_files")
    if not isinstance(records, list) or [item.get("path") for item in records] != expected_paths:
        raise SystemExit("review proxy identity or order changed")
    root = PAPER_ROOT.resolve()
    verified: list[dict[str, Any]] = []
    for record in records:
        relative = record["path"]
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
    if manifest.get("pages_reviewed") != list(range(1, 30)):
        raise SystemExit("review manifest does not cover physical pages 1-29")
    if manifest.get("proxy_count") != len(verified):
        raise SystemExit("review manifest proxy_count changed")
    if manifest.get("largest_proxy_bytes") != largest:
        raise SystemExit("review manifest largest proxy count changed")
    if manifest.get("original_full_page_png_in_context") is not False:
        raise SystemExit("review manifest permits an original full-page PNG")
    if manifest.get("original_contact_sheet_png_in_context") is not False:
        raise SystemExit("review manifest permits an original contact-sheet PNG")

    segments = manifest.get("context_segments")
    if not isinstance(segments, list) or len(segments) != 1:
        raise SystemExit("review manifest must retain exactly one bounded context segment")
    segment = segments[0]
    if (
        segment.get("segment") != 1
        or segment.get("proxy_paths") != expected_paths
        or segment.get("proxy_count") != len(verified)
        or segment.get("total_proxy_bytes") != total
        or segment.get("largest_proxy_bytes") != largest
    ):
        raise SystemExit("review context segment differs from frozen proxy bytes")
    if len(verified) > 8 or total >= 4 * 1024 * 1024:
        raise SystemExit("review context segment exceeds the request-body guard")

    guard = audit.get("gate_attestation", {}).get("request_body_guard")
    if not isinstance(guard, dict):
        raise SystemExit("learning audit has no request_body_guard")
    audit_files = guard.get("proxy_files")
    expected_audit_files = [
        {"file": Path(path).name, "bytes": size}
        for path, size, _ in EXPECTED_PROXIES
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
        "contact_sheet_proxy_count": 6,
        "focused_crop_proxy_count": 2,
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
        raise SystemExit("refusing to overwrite Queue 124 draft or timestamp")

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
        raise SystemExit(f"expected one Queue 124 progress record; found {len(progress_matches)}")
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
            raise SystemExit(f"Queue 124 progress {field} changed ({progress.get(field)!r} != {expected!r})")
    if progress.get("queue_position") != 124 or progress.get("problem_type") != "B" or progress.get("year") != "2018":
        raise SystemExit("Queue 124 progress identity changed")

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
        "page_count": 29,
        "chapter_count": 15,
        "language_count": 140,
        "positive_reusable_language_count": 140,
        "weakness_count": 10,
        "model_count": 14,
        "equation_count": 31,
        "dependency_edge_count": 19,
        "visual_count": 46,
        "observation_count": 306,
        "warning_count": 13,
        "formula_warning_count": 6,
        "section_count": 15,
        "argument_count": 5,
        "abstract_paragraph_count": 5,
        "introduction_paragraph_count": 6,
        "rule_change_count": 8,
        "rule_count": 23,
        "test_count": 119,
        "proxy_count": 8,
        "contact_sheet_proxy_count": 6,
        "focused_crop_proxy_count": 2,
        "segment_count": 1,
        "total_proxy_bytes": 1599460,
        "largest_proxy_bytes": 256385,
    }
    errors = [
        f"{field} differs from validated Queue 124 value ({counts[field]} != {expected})"
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
        errors.append("each Q124 rule impact must add exactly two source-matched observations")
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
        raise SystemExit("Queue 124 frozen-state mismatch: " + "; ".join(errors))

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
                    f"six contact-sheet JPEGs cover pages 1-29 and two focused JPEGs preserve small formula "
                    f"and code labels, with all {counts['proxy_count']} proxy hashes frozen."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all {counts['chapter_count']} "
                    "chapters after Abstract and Introduction first-pass reading and zero-new-move saturation; "
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
                    f"and {counts['dependency_edge_count']} handoff edges across L1/L2 growth, five L2 mechanisms, "
                    "continental migration, city portfolios, office thresholds, sensitivity checks, and executable appendices."
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
                    "extraction, language record, model record, and complete 29-page visual review cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    f"Two independent replays are byte-identical at {digest(rules_path)}; eight nominated B rules each "
                    "received two paper-matched observations while all seed/corroborated lifecycle labels remained unchanged."
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
                "details": f"All {counts['test_count']} regression tests pass against the Queue 124 frozen bytes and current formal baseline.",
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    f"One bounded context segment contains exactly {counts['proxy_count']} JPEGs/{counts['total_proxy_bytes']} bytes; "
                    f"the largest is {counts['largest_proxy_bytes']} bytes, below the 450,000-byte limit. No original page/contact PNG, "
                    "full session JSONL, or printed base64 entered model context; the prior 413 is attributed to accumulated request "
                    "history and image/base64 payload rather than a single Q124 proxy."
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
