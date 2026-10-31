#!/usr/bin/env python3
"""Build a create-only Queue 132 closure draft from frozen canonical bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2020-2010821-2af4f390"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    (
        "review-proxies/contact-01-05.jpg",
        [1, 2, 3, 4, 5],
        273_727,
        "4f821701cf5c908f6ab3558c64ad8303bd44b8644c13a8ec8567706325077664",
    ),
    (
        "review-proxies/contact-06-10.jpg",
        [6, 7, 8, 9, 10],
        247_283,
        "1f765e4f8ea40639f1a477cd0fc0142a6ab49512e0cd338e16291c08c53916e6",
    ),
    (
        "review-proxies/contact-11-15.jpg",
        [11, 12, 13, 14, 15],
        237_966,
        "981d7ac29105c110da64c06d8a94ac57e03ced2aa6173f0b3cc3d3ba6651081b",
    ),
    (
        "review-proxies/contact-16-20.jpg",
        [16, 17, 18, 19, 20],
        256_707,
        "02fc888a897cee2bf60044471a09c3227b4230d0c5124a93b337c64f657da6a2",
    ),
    (
        "review-proxies/contact-21-25.jpg",
        [21, 22, 23, 24, 25],
        223_186,
        "73d9249e46700deb2db4d964f6a9a28faf7f745f893c3c34bbe9e44234bd2acb",
    ),
    (
        "review-proxies/formula-sheets/formula-01-07.jpg",
        [5, 6],
        410_857,
        "26d944dce3a808762fd956b2bc94fad208a19cecf1aa619cfce1d94c2bc03c53",
    ),
    (
        "review-proxies/formula-sheets/formula-09-17.jpg",
        [10, 11, 12, 13],
        444_787,
        "80461202d00996dc13a4fed8789c4165fb40a9b04409e8a2daba2db4a4b0a090",
    ),
    (
        "review-proxies/formula-sheets/formula-08-and-18-25.jpg",
        [7, 14, 15, 16, 17],
        426_062,
        "2de79277447d80c118048f1c63551f35c22091a57c429ff44eaf9edfeaf570a2",
    ),
]

EXPECTED_CORE_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": (
        "8dc850dd5bc448c686e0600a66339b633049a50e7afcd7eacb9cb4c1dd580594"
    ),
    f"artifacts/language-units/{PAPER_ID}.json": (
        "a2e023954c44df594fade78b9aa985c1a0686b1c24c119f815f02de050869c13"
    ),
    f"artifacts/model-units/{PAPER_ID}.json": (
        "f2172fb9d73572750012dafcf1252fad7398a3e3370e7152755f09e82b2bf729"
    ),
    f"artifacts/learning-audits/{PAPER_ID}.json": (
        "67710c11ca1aaaacdba69959367b58697749fcf16cfe89aa5399df423d0d570d"
    ),
    f"artifacts/observations/{PAPER_ID}.jsonl": (
        "11c9f765dfdf889e32b0be2b29deda5a2e61eea5c40268e6043fc2cbab7aba6c"
    ),
    f"artifacts/papers/{PAPER_ID}/extraction.json": (
        "3360229b17ee2fb223fca8d2f8d46183bd30be574124e44616c37e56aa91e6b7"
    ),
    "artifacts/type-branches/B/rules.jsonl": (
        "2b53c150b63246d779c3f53a27938ca4f2f363496e7f13eb72eb5d9053cc4357"
    ),
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": (
        "c7b876f4f180524d65a5964be65ac5e0f27b8463a5dc5c7ba15e64ebef78474c"
    ),
}

EXPECTED_PATTERNS = {
    "LP-B-ABS-TASK-METHOD-RESULT-LADDER": 32,
    "LP-B-ANL-DECOMPOSE-HANDOFF": 26,
    "LP-B-ASM-PREMISE-CONSEQUENCE": 12,
    "LP-B-MOD-DEFINE-CONSTRAIN-HANDOFF": 112,
    "LP-B-ALG-STATE-STEP-STOP": 28,
    "LP-B-RES-VISUAL-DECISION": 40,
    "LP-B-VER-CHECK-CLAIM-BOUNDARY": 58,
    "LP-B-LIM-BOUNDARY-REPAIR": 44,
    "LP-B-MEMO-FINDING-RECOMMENDATION": 12,
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
    "R-B-DATA-002": 8,
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
    "data": 8,
    "language": 364,
    "logic": 18,
    "modeling": 18,
    "other": 0,
    "result": 8,
    "verification": 8,
    "visualization": 28,
    "weakness": 28,
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
    records = manifest.get("files")
    if not isinstance(records, list):
        raise SystemExit("visual_review_manifest files must be an array")

    expected_paths = [item[0] for item in EXPECTED_PROXIES]
    expected_pages = {path: pages for path, pages, _, _ in EXPECTED_PROXIES}
    expected_sizes = {path: size for path, _, size, _ in EXPECTED_PROXIES}
    expected_hashes = {path: sha256 for path, _, _, sha256 in EXPECTED_PROXIES}
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
        sha256 = digest(path)
        if size != expected_sizes[relative] or record.get("bytes") != size:
            raise SystemExit(f"review proxy byte count changed: {relative}")
        if sha256 != expected_hashes[relative] or record.get("sha256") != sha256:
            raise SystemExit(f"review proxy hash changed: {relative}")
        if size > 450_000:
            raise SystemExit(f"review proxy exceeds 450,000 bytes: {relative}")
        verified.append(
            {
                "path": relative,
                "physical_pages": expected_pages[relative],
                "bytes": size,
                "sha256": sha256,
            }
        )

    physical_pages = list(range(1, 26))
    coverage_pages = sorted(
        page
        for relative, pages, _, _ in EXPECTED_PROXIES
        if "/contact-" in relative
        for page in pages
    )
    extraction_review = extraction.get("visual_review")
    if (
        manifest.get("status") != "complete"
        or manifest.get("reviewed_pages") != physical_pages
        or manifest.get("proxy_count") != 8
        or manifest.get("total_proxy_bytes") != 2_520_575
        or manifest.get("maximum_proxy_bytes") != 444_787
        or coverage_pages != physical_pages
    ):
        raise SystemExit("learning-audit visual manifest differs from frozen review state")
    if (
        not isinstance(extraction_review, dict)
        or extraction_review.get("status") != "complete"
        or extraction_review.get("reviewed_pages") != physical_pages
        or extraction.get("visual_review_status") != "complete"
    ):
        raise SystemExit("extraction review does not cover physical pages 1-25")

    total = sum(item["bytes"] for item in verified)
    largest = max(item["bytes"] for item in verified)
    if total >= 4 * 1024 * 1024:
        raise SystemExit("review proxy set exceeds the four-MiB transport ceiling")
    return {
        "proxy_count": len(verified),
        "contact_sheet_proxy_count": 5,
        "focused_crop_proxy_count": 3,
        "segment_count": 1,
        "maximum_proxies_per_segment": 8,
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
        raise SystemExit("refusing to overwrite Queue 132 draft or timestamp")

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
            for relative, _, _, _ in EXPECTED_PROXIES
        },
    }
    missing = [str(path) for path in canonical.values() if not path.is_file()]
    if missing:
        raise SystemExit(f"missing frozen source(s): {missing}")
    for relative, expected_hash in EXPECTED_CORE_HASHES.items():
        actual_hash = digest(canonical[relative])
        if actual_hash != expected_hash:
            raise SystemExit(
                f"Queue 132 frozen core hash changed: {relative} "
                f"{actual_hash} != {expected_hash}"
            )

    card = load_json(canonical[f"artifacts/paper-cards/{PAPER_ID}.json"])
    language = load_json(canonical[f"artifacts/language-units/{PAPER_ID}.json"])
    models = load_json(canonical[f"artifacts/model-units/{PAPER_ID}.json"])
    audit = load_json(canonical[f"artifacts/learning-audits/{PAPER_ID}.json"])
    extraction = load_json(canonical[f"artifacts/papers/{PAPER_ID}/extraction.json"])
    impact = load_json(
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
        question = item if isinstance(item, str) else item.get("question") if isinstance(item, dict) else None
        if not isinstance(question, str) or not question.strip():
            raise SystemExit(f"card unresolved_questions[{index}] has no nonempty question")
        unresolved_added.append(question)
    if len(set(unresolved_added)) != len(unresolved_added):
        raise SystemExit("card unresolved_questions contains duplicate questions")

    progress_matches = [
        record
        for record in load_jsonl(ROOT / "artifacts/progress.jsonl")
        if record.get("paper_id") == PAPER_ID
    ]
    if len(progress_matches) != 1:
        raise SystemExit(
            f"expected one Queue 132 progress record; found {len(progress_matches)}"
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
                f"Queue 132 progress {field} changed "
                f"({progress.get(field)!r} != {expected!r})"
            )
    if (
        "protocol_status" in progress
        or progress.get("queue_position") != 132
        or progress.get("problem_type") != "B"
        or progress.get("year") != "2020"
    ):
        raise SystemExit("Queue 132 progress identity or absent protocol state changed")

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
    observations = load_jsonl(observations_path)
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
        "abstract_paragraph_count": paragraph_count(audit, "abstract"),
        "introduction_paragraph_count": paragraph_count(audit, "introduction"),
        "rule_change_count": impact["rule_change_count"],
        "rule_count": len(load_jsonl(rules_path)),
        "rule_evidence_count": sum(
            len(item.get("added_evidence_ids", []))
            for item in impact.get("changes", [])
            if isinstance(item, dict)
        ),
        "test_count": args.validated_test_count,
        **review,
    }
    expected_counts = {
        "page_count": 25,
        "chapter_count": 18,
        "substantive_source_section_count": 18,
        "language_count": 364,
        "positive_reusable_language_count": 364,
        "weakness_count": 28,
        "model_count": 18,
        "equation_count": 25,
        "dependency_edge_count": 23,
        "visual_count": 28,
        "observation_count": 488,
        "warning_count": 8,
        "g7_warning_count": 28,
        "formula_warning_count": 18,
        "section_count": 18,
        "argument_count": 7,
        "abstract_paragraph_count": 5,
        "introduction_paragraph_count": 1,
        "rule_change_count": 9,
        "rule_count": 23,
        "rule_evidence_count": 89,
        "test_count": 119,
        "proxy_count": 8,
        "contact_sheet_proxy_count": 5,
        "focused_crop_proxy_count": 3,
        "segment_count": 1,
        "maximum_proxies_per_segment": 8,
        "total_proxy_bytes": 2_520_575,
        "largest_proxy_bytes": 444_787,
    }
    errors = [
        f"{field} differs from validated Queue 132 value ({counts[field]} != {expected})"
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
        errors.append("per-rule Q132 added-evidence counts changed")
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
    if protocol.get("language", {}).get("unit_count") != counts["language_count"]:
        errors.append("card language protocol count is incorrect")
    if protocol.get("models", {}).get("model_count") != counts["model_count"]:
        errors.append("card model protocol count is incorrect")
    if errors:
        raise SystemExit("Queue 132 frozen-state mismatch: " + "; ".join(errors))

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
        "unresolved_added": unresolved_added,
        "unresolved_resolved": [],
        "validation_results": [
            {
                "validator": "validate_extraction.py",
                "status": "pass",
                "details": (
                    f"All {counts['page_count']} physical pages retain page-aware text and nonblank rendered pixels; "
                    "five byte-bounded contact JPEGs preserve pages 1-25 in order and three focused formula sheets "
                    "preserve numbered equations (1)-(25), while the page contacts retain figures, tables, and labels."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all "
                    f"{counts['chapter_count']} normalized chapters and {counts['substantive_source_section_count']} "
                    "substantive source sections after Summary and Introduction first-pass reading and a final "
                    "zero-new-move saturation pass; the nine retained patterns occur "
                    + ", ".join(f"{key}={value}" for key, value in patterns.items())
                    + "."
                ),
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']}/{counts['language_count']} language units passed complete-source "
                    "anti-copy checks with two original instantiations each, no source-fact leaks, and maximum shared content run 2."
                ),
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} model units retain {counts['equation_count']} visually checked equations "
                    f"or reconstructed/code relations and {counts['dependency_edge_count']} handoff edges across "
                    "carrying capacity, transient foundation dynamics, damage, successive descent, polymerization, "
                    "rain-wave fuzzy evaluation, RBF humidity prediction, sensitivity, and decision handoffs."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} five-part normalized chapter contracts, "
                    f"{counts['substantive_source_section_count']} substantive source sections, "
                    f"{counts['abstract_paragraph_count']} Summary moves, "
                    f"{counts['introduction_paragraph_count']} Introduction moves, {counts['argument_count']} main "
                    f"chains, {counts['visual_count']} visual dispositions, {counts['g7_warning_count']} final-pass "
                    f"warnings, and {counts['formula_warning_count']} formula warnings passed; positive language "
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
                    "The independent replay and staged bytes are byte-identical at "
                    f"{digest(rules_path)}; {counts['rule_change_count']} nominated B rules received "
                    f"{counts['rule_evidence_count']} paper-matched observations, the idempotence replay added zero, "
                    "and all seed/corroborated lifecycle labels remained unchanged."
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
                    f"All {counts['test_count']} regression tests pass against the Queue 132 frozen bytes and current "
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
                    "JSONL, or printed base64 entered model context. The prior HTTP 413 came from a 21,873,774-byte "
                    "request containing 16 image data URLs and about 19.873 MiB of base64; the exact nginx threshold "
                    "remains unobservable."
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
