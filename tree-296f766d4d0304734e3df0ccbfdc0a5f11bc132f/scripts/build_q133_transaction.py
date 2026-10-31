#!/usr/bin/env python3
"""Build a create-only Queue 133 closure draft from frozen canonical bytes."""

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
PAPER_ID = "P-B-2020-2011873-0d3ec7b7"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    (
        "review-proxies/q133-review-v1/contact-01-05.jpg",
        191_580,
        "c1e78656cba07d0658d1ee8e7d42d52fc9a865c154e37db211279ce9d9cdf624",
        1,
        "complete-page coverage",
    ),
    (
        "review-proxies/q133-review-v1/contact-06-10.jpg",
        157_047,
        "17116de9e3de11d36239768bbf2c59b62dc3792904df59fbfdb2bb1fd6943afe",
        1,
        "complete-page coverage",
    ),
    (
        "review-proxies/q133-review-v1/contact-11-15.jpg",
        173_724,
        "0733adb388e900c58113125a737d34c2f95b1aa8def092af1df6e6c6f5644046",
        1,
        "complete-page coverage",
    ),
    (
        "review-proxies/q133-review-v1/contact-16-20.jpg",
        186_187,
        "85325851017dee64c475ff80bc315cb00d05321da4127f988ce42f6960aa9321",
        1,
        "complete-page coverage",
    ),
    (
        "review-proxies/q133-review-v1/contact-21-23.jpg",
        78_612,
        "38591e136d0385d23f53a5e21cb759b36638cda06005587353841c1aaccb2620",
        1,
        "complete-page coverage",
    ),
    (
        "review-proxies/q133-formula-review-v1/formula-01-08.jpg",
        220_420,
        "95bc2aeb80549ce5786a381f7cdeb98f8302881d87baff6a35e413a246017913",
        1,
        "focused numbered-formula fidelity",
    ),
    (
        "review-proxies/q133-formula-review-v1/formula-09-13.jpg",
        186_726,
        "3c03f23e78687576fb69dd43270b98483bf30507f79965fc0cd02164a1a93716",
        1,
        "focused numbered-formula fidelity",
    ),
    (
        "review-proxies/q133-formula-review-v1/formula-14-18.jpg",
        263_162,
        "fb5e9cbc1093db06c904082e73c188529d22a53d91550c22410e92a562427d94",
        1,
        "focused numbered-formula fidelity",
    ),
    (
        "review-proxies/q133-formula-review-v1/eq1-hi.jpg",
        56_952,
        "fb158f306d17e4dd1891c92be7b25cc98abe409a1c7a064e1b47c43d2a976bcd",
        2,
        "high-resolution Equation (1) coefficient fidelity",
    ),
]

EXPECTED_CORE_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": (
        "820e750e4d25f35d88e61e2daf0429211adec0774a88b8ba67df6d89e7f69210"
    ),
    f"artifacts/language-units/{PAPER_ID}.json": (
        "7e538a905638aa216b00238291a04f835f27fb4ba8b981e9d4918a35958d55ef"
    ),
    f"artifacts/model-units/{PAPER_ID}.json": (
        "e85ac479e749e8bb16e31f7b2a21cf3882653bf14f20edcccd42128ed95950ad"
    ),
    f"artifacts/learning-audits/{PAPER_ID}.json": (
        "37b2fbc2d9ea694be441303811de10ec57ad434d0b33315787d90ba579ff46e9"
    ),
    f"artifacts/observations/{PAPER_ID}.jsonl": (
        "af7c0d11c7a9f194d503ac8474f39c9081063e49a897194eda35af2ed0f48bb2"
    ),
    f"artifacts/papers/{PAPER_ID}/extraction.json": (
        "8cd8599ae043840edbb368376f2255ce9d60b75a82a5cb664d806aea02da4fcf"
    ),
    "artifacts/type-branches/B/rules.jsonl": (
        "f70a1e227a33e9010d6b5106eb628de92191c920905202fa7c76da5c6eab775b"
    ),
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": (
        "84411a5b18fb69643a79b54dabda02c733bd33a49c62fa4796e8aa0d4dcf17b6"
    ),
}

EXPECTED_PATTERNS = {
    "LP-B-ABS-TASK-METHOD-RESULT-LADDER": 18,
    "LP-B-ANL-DECOMPOSE-HANDOFF": 28,
    "LP-B-ASM-PREMISE-CONSEQUENCE": 12,
    "LP-B-MOD-DEFINE-CONSTRAIN-HANDOFF": 138,
    "LP-B-ALG-STATE-STEP-STOP": 19,
    "LP-B-RES-VISUAL-DECISION": 28,
    "LP-B-VER-CHECK-CLAIM-BOUNDARY": 22,
    "LP-B-LIM-BOUNDARY-REPAIR": 25,
    "LP-B-MEMO-FINDING-RECOMMENDATION": 29,
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
    "R-B-DATA-002": 9,
    "R-B-MOD-003": 12,
    "R-B-MOD-004": 12,
    "R-B-COMP-001": 1,
    "R-B-VER-002": 8,
    "R-B-VER-004": 12,
    "R-B-VIZ-001": 12,
    "R-B-LOG-001": 12,
}

EXPECTED_DIMENSIONS = {
    "assumption": 8,
    "data": 9,
    "language": 319,
    "logic": 21,
    "modeling": 18,
    "other": 0,
    "result": 8,
    "verification": 8,
    "visualization": 16,
    "weakness": 26,
}


def verify_review_proxies(
    extraction: dict[str, Any], audit: dict[str, Any]
) -> dict[str, Any]:
    manifest = audit.get("visual_review_manifest")
    if not isinstance(manifest, dict):
        raise SystemExit("learning audit has no visual_review_manifest")
    records = manifest.get("files")
    if not isinstance(records, list):
        raise SystemExit("visual_review_manifest files must be an array")

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

    physical_pages = list(range(1, 24))
    contact_pages = [
        *range(1, 6),
        *range(6, 11),
        *range(11, 16),
        *range(16, 21),
        *range(21, 24),
    ]
    extraction_review = extraction.get("visual_review")
    segment_counts = Counter(item["context_segment"] for item in verified)
    if (
        manifest.get("status") != "complete"
        or manifest.get("reviewed_pages") != physical_pages
        or manifest.get("proxy_count") != 9
        or manifest.get("total_proxy_bytes") != 1_514_410
        or manifest.get("maximum_proxy_bytes") != 263_162
        or contact_pages != physical_pages
        or segment_counts != {1: 8, 2: 1}
    ):
        raise SystemExit("learning-audit visual manifest differs from frozen review state")
    if (
        not isinstance(extraction_review, dict)
        or extraction_review.get("status") != "complete"
        or extraction_review.get("reviewed_pages") != physical_pages
        or extraction.get("visual_review_status") != "complete"
    ):
        raise SystemExit("extraction review does not cover physical pages 1-23")

    total = sum(item["bytes"] for item in verified)
    largest = max(item["bytes"] for item in verified)
    if total >= 4 * 1024 * 1024:
        raise SystemExit("review proxy set exceeds the four-MiB transport ceiling")
    return {
        "proxy_count": len(verified),
        "contact_sheet_proxy_count": 5,
        "focused_crop_proxy_count": 4,
        "segment_count": 2,
        "maximum_proxies_per_segment": max(segment_counts.values()),
        "total_proxy_bytes": total,
        "largest_proxy_bytes": largest,
        "proxies": verified,
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
        raise SystemExit("refusing to overwrite Queue 133 draft or timestamp")

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
                f"Queue 133 frozen core hash changed: {relative} "
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
            raise SystemExit(f"card unresolved_questions[{index}] has no nonempty question")
        unresolved_added.append(question)
    if len(set(unresolved_added)) != len(unresolved_added):
        raise SystemExit("card unresolved_questions contains duplicate questions")

    progress_matches = [
        record
        for record in base.load_jsonl(ROOT / "artifacts/progress.jsonl")
        if record.get("paper_id") == PAPER_ID
    ]
    if len(progress_matches) != 1:
        raise SystemExit(
            f"expected one Queue 133 progress record; found {len(progress_matches)}"
        )
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
                f"Queue 133 progress {field} changed "
                f"({progress.get(field)!r} != {expected!r})"
            )
    if (
        "protocol_status" in progress
        or progress.get("queue_position") != 133
        or progress.get("problem_type") != "B"
        or progress.get("year") != "2020"
    ):
        raise SystemExit("Queue 133 progress identity or absent protocol state changed")

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
    }
    expected_counts = {
        "page_count": 23,
        "chapter_count": 15,
        "substantive_source_section_count": 21,
        "language_count": 319,
        "positive_reusable_language_count": 319,
        "weakness_count": 26,
        "model_count": 18,
        "equation_count": 18,
        "dependency_edge_count": 23,
        "visual_count": 16,
        "observation_count": 433,
        "warning_count": 8,
        "g7_warning_count": 26,
        "formula_warning_count": 15,
        "section_count": 15,
        "argument_count": 7,
        "abstract_paragraph_count": 5,
        "introduction_paragraph_count": 3,
        "rule_change_count": 9,
        "rule_count": 23,
        "rule_evidence_count": 90,
        "test_count": 119,
        "proxy_count": 9,
        "contact_sheet_proxy_count": 5,
        "focused_crop_proxy_count": 4,
        "segment_count": 2,
        "maximum_proxies_per_segment": 8,
        "total_proxy_bytes": 1_514_410,
        "largest_proxy_bytes": 263_162,
    }
    errors = [
        f"{field} differs from validated Queue 133 value ({counts[field]} != {expected})"
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
    valid_origins = {"base", "modification", "hybrid", "paper-specific"}
    invalid_roles = [
        (model["model_id"], variable["symbol"], variable["role"])
        for model in models["models"]
        for variable in model["variables"]
        if variable.get("role") not in valid_roles
    ]
    invalid_origins = [
        (model["model_id"], model.get("base_or_modification"))
        for model in models["models"]
        if model.get("base_or_modification") not in valid_origins
    ]
    if extraction.get("visual_review_status") != "complete":
        errors.append("visual review is not complete")
    if dimensions != EXPECTED_DIMENSIONS:
        errors.append("audit dimension counts changed")
    if dimensions != {key: observation_dimensions[key] for key in dimensions}:
        errors.append("audit dimension counts differ from frozen observations")
    if dimensions.get("language") != counts["language_count"]:
        errors.append("audit language dimension differs from language-unit count")
    if counts["positive_reusable_language_count"] != computed_positive:
        errors.append("positive reusable language count differs from dispositions")
    if patterns != EXPECTED_PATTERNS:
        errors.append("repeated-language pattern occurrences changed")
    if (
        len(changes) != counts["rule_change_count"]
        or changed_lifecycles != EXPECTED_RULE_LIFECYCLES
    ):
        errors.append("rule-impact changes or preserved lifecycles changed")
    if added_counts != EXPECTED_ADDED_EVIDENCE_COUNTS:
        errors.append("per-rule Q133 added-evidence counts changed")
    if impact.get("output_sha256") != base.digest(rules_path):
        errors.append("rule-impact output hash does not bind frozen B rules")
    if invalid_roles:
        errors.append(f"model variables retain invalid schema roles: {invalid_roles}")
    if invalid_origins:
        errors.append(f"model units retain invalid origin values: {invalid_origins}")
    if counts["warning_count"] >= counts["language_count"]:
        errors.append("unresolved question count is not a strict minority of language units")
    if counts["weakness_count"] >= counts["positive_reusable_language_count"]:
        errors.append("weakness count is not below positive reusable language evidence")
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
        raise SystemExit("Queue 133 frozen-state mismatch: " + "; ".join(errors))

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
                    f"All {counts['page_count']} physical pages retain page-aware text and nonblank rendered pixels; "
                    "five byte-bounded contact JPEGs preserve pages 1-23 in order, three formula sheets preserve "
                    "numbered equations (1)-(18), and a later high-resolution Equation (1) crop confirms the printed "
                    "coefficient 1256 without a silent decimal repair."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all "
                    f"{counts['chapter_count']} normalized chapters and {counts['substantive_source_section_count']} "
                    "substantive source sections after the five-paragraph Summary and three-paragraph Introduction "
                    "were read first and every chapter ended with a zero-new-move saturation pass; the nine retained "
                    "patterns occur "
                    + ", ".join(f"{key}={value}" for key, value in patterns.items())
                    + "."
                ),
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']}/{counts['language_count']} language units passed complete-source "
                    "anti-copy checks with two original instantiations each, no source-fact leaks or full-clause "
                    "matches, and maximum shared content run 2."
                ),
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} model units retain {counts['equation_count']} visually checked numbered "
                    f"equations and {counts['dependency_edge_count']} handoff edges across tide fitting, Airy waves, "
                    "Morison force, Mohr-Coulomb stability, Horton infiltration, Van Genuchten retention, geometry "
                    "comparison, mixture traversal, rainfall kinematics, scour/seepage, and ANSYS verification."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} five-part normalized chapter contracts retain all "
                    f"{counts['substantive_source_section_count']} source-section contracts, "
                    f"{counts['abstract_paragraph_count']} Summary moves, "
                    f"{counts['introduction_paragraph_count']} Introduction moves, {counts['argument_count']} main "
                    f"chains, {counts['visual_count']} visual dispositions, {counts['g7_warning_count']} final-pass "
                    f"warnings, and {counts['formula_warning_count']} formula warnings; positive language "
                    f"{counts['positive_reusable_language_count']} strictly exceeds weakness evidence "
                    f"{counts['weakness_count']}."
                ),
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": (
                    f"The card, {counts['observation_count']} observations, {counts['rule_count']} cumulative B rules, "
                    f"extraction, language record, model record, and complete {counts['page_count']}-page visual "
                    "review cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    "The independent replay and staged bytes share SHA-256 "
                    f"{base.digest(rules_path)}; {counts['rule_change_count']} nominated B rules received "
                    f"{counts['rule_evidence_count']} paper-matched observations and all seed/corroborated lifecycle "
                    "labels remained unchanged."
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
                    f"All {counts['test_count']} regression tests pass against the Queue 133 frozen bytes and current "
                    "formal baseline."
                ),
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    f"The {counts['proxy_count']} JPEG review proxies total {counts['total_proxy_bytes']} bytes on disk "
                    f"and were inspected across {counts['segment_count']} bounded context segments with at most "
                    f"{counts['maximum_proxies_per_segment']} images per segment; the largest proxy is "
                    f"{counts['largest_proxy_bytes']} bytes, below 450,000. No original full-page PNG, complete session "
                    "JSONL, or printed base64 entered model context. The prior HTTP 413 correlated with a "
                    "21,873,774-byte request containing 16 image data URLs and about 19.873 MiB of base64; the exact "
                    "nginx threshold remains unobservable."
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
                    **counts,
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
