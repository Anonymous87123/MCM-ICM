#!/usr/bin/env python3
"""Build a create-only Queue 134 closure draft from frozen canonical bytes."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import build_q132_transaction as base


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2020-2013836-4c773f05"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    (
        "review-proxies/q134-formula-review-v1/review-01-tables-1-2.jpg",
        196_180,
        "5a934ca459e778f598007c2b9d0f75e3910a66809380577b78e10a9085d2655b",
        1,
        "focused Table 1-2 and notation fidelity",
    ),
    (
        "review-proxies/q134-formula-review-v1/review-02-equations-01-02.jpg",
        31_831,
        "f189001252cdf35ba0ab634f51557f7c3e239e52f800bb317da1aa046a72fb3d",
        1,
        "focused numbered-formula fidelity",
    ),
    (
        "review-proxies/q134-formula-review-v1/review-03-equations-03-10.jpg",
        113_917,
        "06d5a7f4d34ef6072305c1749a1b7a0f1dd5cf32d4b3c0a46c1d231b7107e85a",
        1,
        "focused numbered-formula fidelity",
    ),
    (
        "review-proxies/q134-formula-review-v1/review-04-equations-11-14.jpg",
        240_129,
        "222aa82e3c4a651e54777be5fc2f75e7025495329aeaaebb6a4c671b2ccc5d50",
        1,
        "focused numbered-formula fidelity",
    ),
    (
        "review-proxies/q134-formula-review-v1/review-05-equations-15-16-table-3.jpg",
        177_548,
        "91e28ad612cace07fcd84998ea36c3c653bb03302172abea2d4fb8b864c9287a",
        1,
        "focused Equations (15)-(16) and Table 3 fidelity",
    ),
    (
        "review-proxies/q134-formula-review-v1/review-06-equations-17-24-table-4.jpg",
        175_775,
        "6c1d5b42ed078172cf834bcb6e0b00d5298ebdf9f4aa25b0dfcde6a9a2f7bd7b",
        1,
        "focused Equations (17)-(24) and Table 4 fidelity",
    ),
    (
        "review-proxies/q134-formula-review-v1/review-07-equations-25-27-ratio.jpg",
        253_921,
        "7158ec949346ebf7f67a3c1e5f20ad171ead7df6807e5df70225d02f42bef095",
        1,
        "focused numbered-formula fidelity",
    ),
    (
        "review-proxies/q134-formula-review-v1/review-08-page-22-missing-line.jpg",
        116_295,
        "6ec485fd1b88749878698752b7f1fbfc1ea1db40a51edf32122714dd4778d469",
        1,
        "focused recovery of the OCR-omitted rainfall-sensitivity transition",
    ),
    (
        "review-proxies/q134-formula-review-eq27-v1/review-09-equation-27-wide.jpg",
        103_862,
        "cd4bf40a79fb6ddde21768c4577f32cfdcc0b757bfa76aca5c06602db299ae5e",
        2,
        "later-context, left-inclusive Equation (27) numerator/denominator fidelity",
    ),
]

EXPECTED_CORE_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": (
        "cc6bc260e4a7fdf03ff2275f4dfe0e55dd4ff0479ccb717914050baddd9eee34"
    ),
    f"artifacts/language-units/{PAPER_ID}.json": (
        "0d8f263ee4fcee9c8cbf0d7480e4e012518c986c8060aecb66b3b088926d4f31"
    ),
    f"artifacts/model-units/{PAPER_ID}.json": (
        "6e21f3880db0fb2ae9d6dfb777f0f4ba5f57abc3ccadce44010932dd0e1519d5"
    ),
    f"artifacts/learning-audits/{PAPER_ID}.json": (
        "d81499b0b94d7b2eb01284bd0a843f1437188f30c2279fc915d0580bd180800f"
    ),
    f"artifacts/observations/{PAPER_ID}.jsonl": (
        "1605722b6416b0baa49b3746969c77d979e7adebd1857f3b6bfa53b18203f08b"
    ),
    f"artifacts/papers/{PAPER_ID}/extraction.json": (
        "444e0bc8cdd51944fdf8a83ea27d0c1646407da0ea07acc2ff211a47ca605167"
    ),
    "artifacts/type-branches/B/rules.jsonl": (
        "d5b9e18c7aef24650ea811c22bc097ef06958c7800ff646a7dcc492a5b228d2d"
    ),
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": (
        "e6adf466c66da484c3930b8b98bb4a2b59edcd3d458d7418fa55e60e41c421b6"
    ),
}

EXPECTED_PATTERNS = {
    "LP-B-ABS-TASK-METHOD-RESULT-LADDER": 24,
    "LP-B-ANL-DECOMPOSE-HANDOFF": 41,
    "LP-B-ASM-PREMISE-CONSEQUENCE": 11,
    "LP-B-MOD-DEFINE-CONSTRAIN-HANDOFF": 131,
    "LP-B-ALG-STATE-STEP-STOP": 64,
    "LP-B-RES-VISUAL-DECISION": 26,
    "LP-B-VER-CHECK-CLAIM-BOUNDARY": 34,
    "LP-B-LIM-BOUNDARY-REPAIR": 7,
    "LP-B-MEMO-FINDING-RECOMMENDATION": 37,
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
    "R-B-LANG-001": 12,
    "R-B-DATA-002": 10,
    "R-B-MOD-003": 12,
    "R-B-MOD-004": 12,
    "R-B-COMP-001": 6,
    "R-B-VER-002": 10,
    "R-B-VER-004": 7,
    "R-B-VIZ-001": 12,
    "R-B-LOG-001": 12,
}

EXPECTED_DIMENSIONS = {
    "assumption": 12,
    "data": 10,
    "language": 375,
    "logic": 25,
    "modeling": 18,
    "other": 0,
    "result": 10,
    "verification": 10,
    "visualization": 21,
    "weakness": 7,
}

EXPECTED_REVIEW_HASHES = {
    "primary_review_tree_sha256": "c0fafed4f0b5193d9a46adf9103740f2d298be3318d3e5dcb28e5bbc92248552",
    "eq27_supplement_tree_sha256": "be9241c54c53bcf3807f782091b4ec3504f7e806cd576d684a141b91ae4d9c77",
    "combined_review_tree_sha256": "75f3fef3c5ada2268573938fd7cedbb29fa57b4680320051024bb0017f622935",
    "findings_sha256": "c1042f67079bdaba274bc35da3b088232af37a41d1f3c58cfe97173140a42794",
}


def verify_review_proxies(
    extraction: dict[str, Any], audit: dict[str, Any]
) -> dict[str, Any]:
    manifest = audit.get("visual_review_manifest")
    extraction_review = extraction.get("visual_review")
    if not isinstance(manifest, dict) or not isinstance(extraction_review, dict):
        raise SystemExit("missing frozen visual review manifest")
    bundle = extraction_review.get("review_bundle")
    records = manifest.get("files")
    if not isinstance(bundle, dict) or not isinstance(records, list):
        raise SystemExit("visual review bundle or files are invalid")
    if bundle.get("files") != records:
        raise SystemExit("audit and extraction review proxy records differ")

    expected_paths = [item[0] for item in EXPECTED_PROXIES]
    expected_sizes = {path: size for path, size, _, _, _ in EXPECTED_PROXIES}
    expected_hashes = {path: sha256 for path, _, sha256, _, _ in EXPECTED_PROXIES}
    expected_segments = {path: segment for path, _, _, segment, _ in EXPECTED_PROXIES}
    expected_purposes = {path: purpose for path, _, _, _, purpose in EXPECTED_PROXIES}
    record_paths = [f"review-proxies/{item.get('relative_path')}" for item in records]
    if record_paths != expected_paths:
        raise SystemExit("review proxy identity or order changed")

    review_root = PAPER_ROOT / "review-proxies"
    actual_paths = sorted(
        f"review-proxies/{path.relative_to(review_root).as_posix()}"
        for path in review_root.rglob("*")
        if path.is_file()
    )
    if actual_paths != sorted(expected_paths):
        raise SystemExit("review proxy directory contains an unexpected file set")

    verified: list[dict[str, Any]] = []
    root = PAPER_ROOT.resolve()
    for record in records:
        relative = f"review-proxies/{record['relative_path']}"
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
        sha256 = base.digest(path)
        if size != expected_sizes[relative] or record.get("bytes") != size:
            raise SystemExit(f"review proxy byte count changed: {relative}")
        if sha256 != expected_hashes[relative] or record.get("sha256") != sha256:
            raise SystemExit(f"review proxy hash changed: {relative}")
        if record.get("context_segment") != expected_segments[relative]:
            raise SystemExit(f"review proxy context segment changed: {relative}")
        if record.get("purpose") != expected_purposes[relative]:
            raise SystemExit(f"review proxy purpose changed: {relative}")
        if size > 450_000:
            raise SystemExit(f"review proxy exceeds 450,000 bytes: {relative}")
        verified.append(
            {
                "path": relative,
                "bytes": size,
                "sha256": sha256,
                "context_segment": record["context_segment"],
                "purpose": record["purpose"],
            }
        )

    physical_pages = list(range(1, 26))
    segment_counts = Counter(item["context_segment"] for item in verified)
    for key, expected in EXPECTED_REVIEW_HASHES.items():
        if manifest.get(key) != expected or bundle.get(key) != expected:
            raise SystemExit(f"review manifest {key} changed")
    if (
        manifest.get("status") != "complete"
        or manifest.get("reviewed_pages") != physical_pages
        or manifest.get("proxy_count") != 9
        or manifest.get("total_proxy_bytes") != 1_409_458
        or manifest.get("maximum_proxy_bytes") != 253_921
        or bundle.get("status") != "complete"
        or extraction_review.get("status") != "complete"
        or extraction_review.get("reviewed_pages") != physical_pages
        or extraction.get("visual_review_status") != "complete"
        or segment_counts != {1: 8, 2: 1}
    ):
        raise SystemExit("visual review manifest differs from frozen Queue 134 state")
    total = sum(item["bytes"] for item in verified)
    if total >= 4 * 1024 * 1024:
        raise SystemExit("review proxy set exceeds the four-MiB transport ceiling")
    return {
        "proxy_count": len(verified),
        "contact_sheet_proxy_count": 0,
        "focused_crop_proxy_count": len(verified),
        "segment_count": len(segment_counts),
        "maximum_proxies_per_segment": max(segment_counts.values()),
        "total_proxy_bytes": total,
        "largest_proxy_bytes": max(item["bytes"] for item in verified),
        "proxies": verified,
    }


def verify_promotion() -> dict[str, int]:
    report_path = ROOT / "tmp" / "q134-promotion-report-v1.json"
    backup_root = ROOT / "tmp" / "q134-promotion-backup-v1"
    report = base.load_json(report_path)
    manifest_path = backup_root / "manifest.json"
    manifest = base.load_json(manifest_path)
    if (
        report.get("status") != "pass"
        or report.get("files_deleted") != 0
        or report.get("preimage_file_count") != 31
        or report.get("promoted_file_count") != 70
        or report.get("created_files") != 38
        or report.get("overwritten_after_backup") != 32
        or report.get("backup_manifest_sha256") != base.digest(manifest_path)
    ):
        raise SystemExit("promotion report differs from the frozen zero-delete state")

    promoted = report.get("promoted")
    if not isinstance(promoted, list) or len(promoted) != 70:
        raise SystemExit("promotion report does not contain 70 file declarations")
    destinations: set[str] = set()
    for item in promoted:
        source = ROOT / item["source"]
        destination = ROOT / item["destination"]
        expected = item["sha256"]
        if item["destination"] in destinations:
            raise SystemExit("promotion report contains a duplicate destination")
        destinations.add(item["destination"])
        if (
            not source.is_file()
            or not destination.is_file()
            or base.digest(source) != expected
            or base.digest(destination) != expected
        ):
            raise SystemExit(f"promoted source/destination drift: {item['destination']}")

    preimage = manifest.get("paper_preimage")
    if (
        manifest.get("status") != "complete-preimage-backup"
        or manifest.get("paper_preimage_file_count") != 31
        or not isinstance(preimage, list)
        or len(preimage) != 31
        or manifest.get("rules_preimage", {}).get("sha256")
        != "f70a1e227a33e9010d6b5106eb628de92191c920905202fa7c76da5c6eab775b"
    ):
        raise SystemExit("promotion preimage manifest changed")
    for item in preimage:
        path = backup_root / "paper-canonical-preimage" / item["relative_path"]
        if (
            not path.is_file()
            or path.stat().st_size != item["bytes"]
            or base.digest(path) != item["sha256"]
        ):
            raise SystemExit(f"paper preimage backup drift: {item['relative_path']}")
    rules_preimage = backup_root / "B-rules-preimage.jsonl"
    if base.digest(rules_preimage) != manifest["rules_preimage"]["sha256"]:
        raise SystemExit("B-rules preimage backup drift")
    return {
        "preimage_file_count": 31,
        "promoted_file_count": 70,
        "promotion_created_file_count": 38,
        "promotion_overwritten_file_count": 32,
        "promotion_deleted_file_count": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validated-test-count", required=True, type=int)
    parser.add_argument("--timestamp-utc")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    if args.validated_test_count <= 0:
        raise SystemExit("validated test count must be positive")

    draft_path = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    timestamp_path = ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt"
    if not args.check_only and (draft_path.exists() or timestamp_path.exists()):
        raise SystemExit("refusing to overwrite Queue 134 draft or timestamp")

    canonical = {
        f"artifacts/paper-cards/{PAPER_ID}.json": ROOT
        / f"artifacts/paper-cards/{PAPER_ID}.json",
        f"artifacts/language-units/{PAPER_ID}.json": ROOT
        / f"artifacts/language-units/{PAPER_ID}.json",
        f"artifacts/model-units/{PAPER_ID}.json": ROOT
        / f"artifacts/model-units/{PAPER_ID}.json",
        f"artifacts/learning-audits/{PAPER_ID}.json": ROOT
        / f"artifacts/learning-audits/{PAPER_ID}.json",
        f"artifacts/observations/{PAPER_ID}.jsonl": ROOT
        / f"artifacts/observations/{PAPER_ID}.jsonl",
        f"artifacts/papers/{PAPER_ID}/extraction.json": PAPER_ROOT / "extraction.json",
        "artifacts/type-branches/B/rules.jsonl": ROOT
        / "artifacts/type-branches/B/rules.jsonl",
        f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": ROOT
        / f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json",
        **{
            f"artifacts/papers/{PAPER_ID}/{relative}": PAPER_ROOT / relative
            for relative, _, _, _, _ in EXPECTED_PROXIES
        },
    }
    missing = [str(path) for path in canonical.values() if not path.is_file()]
    if missing:
        raise SystemExit(f"missing frozen source(s): {missing}")
    for relative, expected_hash in EXPECTED_CORE_HASHES.items():
        actual_hash = base.digest(canonical[relative])
        if actual_hash != expected_hash:
            raise SystemExit(
                f"Queue 134 frozen core hash changed: {relative} "
                f"{actual_hash} != {expected_hash}"
            )

    card = base.load_json(canonical[f"artifacts/paper-cards/{PAPER_ID}.json"])
    language = base.load_json(canonical[f"artifacts/language-units/{PAPER_ID}.json"])
    models = base.load_json(canonical[f"artifacts/model-units/{PAPER_ID}.json"])
    audit = base.load_json(canonical[f"artifacts/learning-audits/{PAPER_ID}.json"])
    extraction = base.load_json(canonical[f"artifacts/papers/{PAPER_ID}/extraction.json"])
    impact = base.load_json(
        canonical[f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json"]
    )
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

    raw_unresolved = card.get("unresolved_questions")
    if not isinstance(raw_unresolved, list):
        raise SystemExit("card unresolved_questions must be an array")
    unresolved_added: list[str] = []
    for index, item in enumerate(raw_unresolved, start=1):
        question = (
            item
            if isinstance(item, str)
            else item.get("question")
            if isinstance(item, dict)
            else None
        )
        if not isinstance(question, str) or not question.strip():
            raise SystemExit(f"card unresolved_questions[{index}] has no question")
        unresolved_added.append(question)
    if len(set(unresolved_added)) != len(unresolved_added):
        raise SystemExit("card unresolved_questions contains duplicates")

    progress_matches = [
        record
        for record in base.load_jsonl(ROOT / "artifacts/progress.jsonl")
        if record.get("paper_id") == PAPER_ID
    ]
    if len(progress_matches) != 1:
        raise SystemExit(f"expected one Queue 134 progress record; found {len(progress_matches)}")
    progress = progress_matches[0]
    expected_before = {
        "branch_update_status": "pending",
        "extraction_status": "needs-ocr",
        "paper_card_status": "pending",
        "protocol_status": "absent",
        "status": "needs-ocr",
        "validation_status": "pending",
    }
    for field, expected in expected_before.items():
        if field != "protocol_status" and progress.get(field) != expected:
            raise SystemExit(f"Queue 134 progress {field} changed")
    if (
        "protocol_status" in progress
        or progress.get("queue_position") != 134
        or progress.get("problem_type") != "B"
        or progress.get("year") != "2020"
    ):
        raise SystemExit("Queue 134 progress identity or absent protocol state changed")

    review = verify_review_proxies(extraction, audit)
    promotion = verify_promotion()
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
    observations = base.load_jsonl(observations_path)
    observation_dimensions = Counter(item.get("dimension") for item in observations)
    source_sections = [
        item
        for item in card.get("section_map", [])
        if isinstance(item, dict) and item.get("normalized_chapter") != "non-substantive"
    ]
    counts = {
        "page_count": extraction["page_count"],
        "chapter_count": len(language["available_chapters"]),
        "substantive_source_section_count": len(source_sections),
        "language_count": len(language["units"]),
        "positive_reusable_language_count": audit["positive_reusable_language_count"],
        "weakness_count": audit["dimension_counts"]["weakness"],
        "model_count": len(models["models"]),
        "equation_count": sum(
            len(model["governing_equations"]) for model in models["models"]
        ),
        "dependency_edge_count": len(models["dependency_edges"]),
        "visual_count": len(card["visualization_observations"]),
        "observation_count": len(observations),
        "warning_count": len(unresolved_added),
        "g7_warning_count": audit["g7_warning_count"],
        "formula_warning_count": len(audit["formula_error_watch"]["warnings"]),
        "section_count": len(audit["organization_logic"]["section_progressions"]),
        "argument_count": len(audit["organization_logic"]["main_argument_chains"]),
        "abstract_paragraph_count": base.paragraph_count(audit, "abstract"),
        "introduction_paragraph_count": base.paragraph_count(audit, "introduction"),
        "rule_change_count": impact["rule_change_count"],
        "rule_count": len(base.load_jsonl(rules_path)),
        "rule_evidence_count": sum(
            len(item.get("added_evidence_ids", []))
            for item in impact.get("changes", [])
            if isinstance(item, dict)
        ),
        "test_count": args.validated_test_count,
        **review,
        **promotion,
    }
    expected_counts = {
        "page_count": 25,
        "chapter_count": 14,
        "substantive_source_section_count": 25,
        "language_count": 375,
        "positive_reusable_language_count": 375,
        "weakness_count": 7,
        "model_count": 18,
        "equation_count": 27,
        "dependency_edge_count": 28,
        "visual_count": 21,
        "observation_count": 488,
        "warning_count": 8,
        "g7_warning_count": 7,
        "formula_warning_count": 5,
        "section_count": 14,
        "argument_count": 9,
        "abstract_paragraph_count": 5,
        "introduction_paragraph_count": 2,
        "rule_change_count": 9,
        "rule_count": 23,
        "rule_evidence_count": 93,
        "test_count": 119,
        "proxy_count": 9,
        "contact_sheet_proxy_count": 0,
        "focused_crop_proxy_count": 9,
        "segment_count": 2,
        "maximum_proxies_per_segment": 8,
        "total_proxy_bytes": 1_409_458,
        "largest_proxy_bytes": 253_921,
        "preimage_file_count": 31,
        "promoted_file_count": 70,
        "promotion_created_file_count": 38,
        "promotion_overwritten_file_count": 32,
        "promotion_deleted_file_count": 0,
    }
    errors = [
        f"{field} differs from validated Queue 134 value ({counts[field]} != {expected})"
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
    equation_ids = [
        equation["equation_id"]
        for model in models["models"]
        for equation in model["governing_equations"]
    ]
    expected_equation_ids = [f"EQ-B-2020-2013836-{index:03d}" for index in range(1, 28)]
    if dimensions != EXPECTED_DIMENSIONS:
        errors.append("audit dimension counts changed")
    if dimensions != {key: observation_dimensions[key] for key in dimensions}:
        errors.append("audit dimensions differ from frozen observations")
    if dimensions.get("language") != counts["language_count"]:
        errors.append("language dimension differs from language-unit count")
    if counts["positive_reusable_language_count"] != computed_positive:
        errors.append("positive reusable language differs from dispositions")
    if patterns != EXPECTED_PATTERNS:
        errors.append("repeated-language pattern occurrences changed")
    if len(changes) != 9 or changed_lifecycles != EXPECTED_RULE_LIFECYCLES:
        errors.append("rule-impact changes or preserved lifecycles changed")
    if added_counts != EXPECTED_ADDED_EVIDENCE_COUNTS:
        errors.append("per-rule Queue 134 added-evidence counts changed")
    if impact.get("output_sha256") != base.digest(rules_path):
        errors.append("rule-impact report does not bind frozen B rules")
    if equation_ids != expected_equation_ids:
        errors.append("numbered equation identities are not continuous 1-27")
    replay_rules = ROOT / "tmp" / "q134-B-rules-replay-v2.jsonl"
    replay_report = ROOT / "tmp" / "q134-rule-impact-replay-v2.json"
    if (
        base.digest(replay_rules) != base.digest(rules_path)
        or base.digest(replay_report)
        != base.digest(
            canonical[f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json"]
        )
    ):
        errors.append("independent rule replay differs from frozen canonical bytes")
    if counts["warning_count"] >= counts["language_count"]:
        errors.append("unresolved questions are not a strict minority")
    if counts["weakness_count"] >= counts["positive_reusable_language_count"]:
        errors.append("positive reusable language does not exceed weakness evidence")
    if dimensions["language"] <= max(
        count for dimension, count in dimensions.items() if dimension != "language"
    ):
        errors.append("language is not the strictly largest evidence dimension")
    protocol = card.get("protocol_v2_records", {})
    if protocol.get("language", {}).get("unit_count") != counts["language_count"]:
        errors.append("card language protocol count is incorrect")
    if protocol.get("models", {}).get("model_count") != counts["model_count"]:
        errors.append("card model protocol count is incorrect")
    if errors:
        raise SystemExit("Queue 134 frozen-state mismatch: " + "; ".join(errors))

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
            "g7_warning_count": counts["g7_warning_count"],
            "important_visual_count": counts["visual_count"],
            "language_pattern_occurrences": patterns,
            "language_unit_count": counts["language_count"],
            "model_count": counts["model_count"],
            "observation_count": counts["observation_count"],
            "paper_card_status": "validated",
            "positive_reusable_language_count": counts[
                "positive_reusable_language_count"
            ],
            "protocol_status": "current-validated",
            "section_contract_count": counts["section_count"],
            "source_action_count": counts["language_count"],
            "status": "closed",
            "validation_status": "pass",
            "warning_count": counts["warning_count"],
        },
        "artifact_diffs": [
            f"artifact:{relative}|sha256:{base.digest(path)}"
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
        "unresolved_added": unresolved_added,
        "unresolved_resolved": [],
        "validation_results": [
            {
                "validator": "validate_extraction.py",
                "status": "pass",
                "details": (
                    "All 25 physical pages retain page-aware OCR text and nonblank 1700x2200 rendered pixels. "
                    "Sequential page review found no missing, duplicate, clipped, blank, or image-only page; nine "
                    "focused byte-bounded JPEG crops preserve Equations (1)-(27), Tables 1-4, notation, and the "
                    "OCR-omitted page-22 rainfall-sensitivity transition."
                ),
            },
            {
                "validator": "source_coverage_audit",
                "status": "pass",
                "details": (
                    "The complete 25-page OCR text was read in order, including the Summary, Contents, every body "
                    "chapter, conclusion, references, and stakeholder magazine article. Formula/table review retains "
                    "27/27 numbered equations and 4/4 tables without silently repairing the seven G7 issues."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all "
                    f"{counts['chapter_count']} normalized chapters and {counts['substantive_source_section_count']} "
                    "source sections after the five-paragraph Summary and two-paragraph Introduction were read first. "
                    "Nine repeated B-language patterns retain occurrence, function, information order, slots, "
                    "variants, boundaries, and two unrelated original examples; occurrences are "
                    + ", ".join(f"{key}={value}" for key, value in patterns.items())
                    + "."
                ),
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']}/{counts['language_count']} units passed against the complete source "
                    "with two unrelated instantiations each, zero full-clause matches, zero source-fact leaks, zero "
                    "unique content-shingle matches, and maximum shared content run 2."
                ),
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} typed model units retain {counts['equation_count']} visually checked "
                    f"numbered equations and {counts['dependency_edge_count']} handoff edges across cubic-cell state "
                    "construction, tide and shallow-water forcing, implicit wave-speed averaging, mixture-dependent "
                    "viscosity, slide/scour/floatage transitions, rain and seawater mixture updates, residual ratio, "
                    "shape iteration, mixture sweeps, rainfall sensitivity, and bounded recommendations."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} normalized chapter contracts retain 25 source-section progressions, "
                    f"{counts['argument_count']} main argument chains, {counts['visual_count']} visual dispositions, "
                    f"{counts['g7_warning_count']} final-pass G7 warnings, and {counts['formula_warning_count']} formula "
                    f"warnings. Positive reusable language {counts['positive_reusable_language_count']} strictly "
                    f"exceeds weakness evidence {counts['weakness_count']}."
                ),
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": (
                    f"The card, {counts['observation_count']} observations, {counts['rule_count']} cumulative B rules, "
                    "extraction, language record, model record, complete visual review, and full prior-observation "
                    "corpus cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    "The independent replay and canonical staged bytes are byte-identical at SHA-256 "
                    f"{base.digest(rules_path)}; nine nominated B rules received {counts['rule_evidence_count']} "
                    "paper-matched observations while every seed/corroborated lifecycle label remained unchanged."
                ),
            },
            {
                "validator": "promotion_preimage_and_hash_verification",
                "status": "pass",
                "details": (
                    "The complete 31-file needs-ocr placeholder and live B-rules preimage were copied to a create-only "
                    "backup and hash-verified before promotion. All 70 promoted source/destination pairs match their "
                    "declared SHA-256 values; 38 files were created, 32 were overwritten only after backup, and zero "
                    "files were deleted or moved."
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
                "details": (
                    f"All {counts['test_count']} regression tests pass against the Queue 134 frozen canonical bytes "
                    "and current formal baseline."
                ),
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    f"The {counts['proxy_count']} JPEG review proxies total {counts['total_proxy_bytes']} bytes and "
                    f"were inspected across {counts['segment_count']} bounded context segments with at most "
                    f"{counts['maximum_proxies_per_segment']} images per segment; the largest is "
                    f"{counts['largest_proxy_bytes']} bytes. No tool call returned more than one image and no full-page "
                    "PNG, contact sheet at original detail, complete .codex session JSONL, or base64 dump entered this "
                    "continuation. The prior HTTP 413 followed five original-size images totaling about 20.84 MB, so "
                    "future review remains capped at 450,000 bytes per JPEG and below 4 MiB per context segment."
                ),
            },
        ],
    }

    if args.check_only:
        print(
            json.dumps(
                {
                    "artifact_declaration_count": len(draft["artifact_diffs"]),
                    "files_deleted": 0,
                    "paper_id": PAPER_ID,
                    "status": "ready",
                    **{key: value for key, value in counts.items() if key != "proxies"},
                },
                ensure_ascii=False,
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
                "paper_id": PAPER_ID,
                "draft": str(draft_path),
                "timestamp_utc": timestamp,
                "artifact_declaration_count": len(draft["artifact_diffs"]),
                "files_deleted": 0,
                **{key: value for key, value in counts.items() if key != "proxies"},
                "pattern_occurrences": patterns,
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
