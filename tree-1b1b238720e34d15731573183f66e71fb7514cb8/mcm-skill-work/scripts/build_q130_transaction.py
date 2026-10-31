#!/usr/bin/env python3
"""Build a create-only Queue 130 closure draft from frozen canonical bytes."""

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
PAPER_ID = "P-B-2019-1924588-bd69a632"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    (
        "review-proxies/01-pages-0001-0005.jpg",
        [1, 2, 3, 4, 5],
        425858,
        "5af042c392b425f56b654a55aa2ca17084576bd5b885bf9e12e92a98fcdc60b8",
    ),
    (
        "review-proxies/02-pages-0006-0010.jpg",
        [6, 7, 8, 9, 10],
        448739,
        "f3c6e3ed6b2cbb62a70755d099f24205c76cc62a83a6f194d7d8168c26ed6136",
    ),
    (
        "review-proxies/03-pages-0011-0015.jpg",
        [11, 12, 13, 14, 15],
        415013,
        "67a6788380c73a4c470ec04ad922d4ffd406d2c355076f12a90ab32529454e88",
    ),
    (
        "review-proxies/04-pages-0016-0020.jpg",
        [16, 17, 18, 19, 20],
        421043,
        "df5f2baeac075f7b072e03306b305fd4d0675d57c9a580b9b90b98d6f5dad67a",
    ),
    (
        "review-proxies/05-pages-0021-0025.jpg",
        [21, 22, 23, 24, 25],
        449543,
        "86475f4a9d31ce3f30dc6d7bb371a9f443b00cc805dc91381501fcb29c50dcfc",
    ),
    (
        "review-proxies/06-pages-0026-0030.jpg",
        [26, 27, 28, 29, 30],
        256394,
        "e0ac7d0a16d54f8c438bf21e59838476a9352087781ecec11cbfb7bf30700c48",
    ),
    (
        "review-proxies/07-pages-0031-0033.jpg",
        [31, 32, 33],
        168739,
        "f90ce4f41aaaf72d7ea76278fed2099f86baef06b4ec729cd0514bbe87ec1fa0",
    ),
    (
        "review-proxies/08-pages-0014-0015-tables.jpg",
        [14, 15],
        247220,
        "62b71a016a022adaf3c37b61082ae006555dae04fe2faeeaa6aeebea16bf0edf",
    ),
]

EXPECTED_CORE_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": (
        "22fc90a585fbab7937ec34405b672c9673193e51cf777d187e2a3d010e838ddd"
    ),
    f"artifacts/language-units/{PAPER_ID}.json": (
        "b99644731a42063f3928045a6b9e4e0cd32eb11ea5f022daf8f5c394d38256ef"
    ),
    f"artifacts/model-units/{PAPER_ID}.json": (
        "94d504cbbf73c81654d152055ed56b7aa6a7641481f8bddede6cbf2f188bffc5"
    ),
    f"artifacts/learning-audits/{PAPER_ID}.json": (
        "3248d34cbbc7b191c2ff886f4a3373cb79c7ef7537541ff79076a90fc3b96e71"
    ),
    f"artifacts/observations/{PAPER_ID}.jsonl": (
        "bd4142b60fcdffe3c38fad9cf35b90db6d07e9776fa494524a78538ee5bfb38a"
    ),
    f"artifacts/papers/{PAPER_ID}/extraction.json": (
        "561eba2cf96fc7bf628a88c37e0724cadf7d09087e72ad4f2c285e71253ccc9d"
    ),
    "artifacts/type-branches/B/rules.jsonl": (
        "3574868b59d3488f6796296a8e68e318c25aa194dbacc27f70fb3f54f0b82b94"
    ),
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": (
        "8f238a2f04c844fb1a90d608852b025f1005f9aab6accfc538948239200fd1f1"
    ),
}

EXPECTED_PATTERNS = {
    "LP-B-ABS-TASK-METHOD-RESULT-LADDER": 15,
    "LP-B-MEMO-FINDING-RECOMMENDATION": 14,
    "LP-B-ANL-DECOMPOSE-HANDOFF": 20,
    "LP-B-ASM-PREMISE-CONSEQUENCE": 13,
    "LP-B-MOD-DEFINE-CONSTRAIN-HANDOFF": 71,
    "LP-B-ALG-STATE-STEP-STOP": 82,
    "LP-B-RES-VISUAL-DECISION": 17,
    "LP-B-VER-CHECK-CLAIM-BOUNDARY": 8,
    "LP-B-LIM-BOUNDARY-REPAIR": 12,
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
    rule_id: 3 for rule_id in EXPECTED_RULE_LIFECYCLES
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
    record_paths = [f"review-proxies/{item.get('file')}" for item in records]
    if record_paths != expected_paths:
        raise SystemExit("review proxy identity or order changed")

    actual_names = sorted(
        path.name
        for path in (PAPER_ROOT / "review-proxies").iterdir()
        if path.is_file()
    )
    if actual_names != sorted(Path(path).name for path in expected_paths):
        raise SystemExit("review proxy directory contains an unexpected file set")

    verified: list[dict[str, Any]] = []
    root = PAPER_ROOT.resolve()
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
        if record.get("physical_pages") != expected_pages[relative]:
            raise SystemExit(f"review proxy page coverage changed: {relative}")
        if size > 450_000:
            raise SystemExit(f"review proxy exceeds 450,000 bytes: {relative}")
        verified.append({"path": relative, "bytes": size, "sha256": sha256})

    physical_pages = list(range(1, 34))
    extraction_review = extraction.get("visual_review")
    if (
        manifest.get("coverage_status") != "complete"
        or manifest.get("physical_pages_reviewed") != physical_pages
        or manifest.get("proxy_byte_limit") != 450_000
        or manifest.get("all_proxies_within_limit") is not True
        or manifest.get("original_pngs_retained_on_disk") is not True
    ):
        raise SystemExit("learning-audit visual manifest differs from frozen review state")
    if (
        not isinstance(extraction_review, dict)
        or extraction_review.get("status") != "complete"
        or extraction_review.get("reviewed_pages") != physical_pages
        or extraction.get("visual_review_status") != "complete"
    ):
        raise SystemExit("extraction review does not cover physical pages 1-33")

    total = sum(item["bytes"] for item in verified)
    largest = max(item["bytes"] for item in verified)
    if len(verified) != 8 or total >= 4 * 1024 * 1024:
        raise SystemExit("review context segment exceeds the request-body guard")
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
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    if args.validated_test_count <= 0:
        raise SystemExit("validated test count must be positive")

    draft_path = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    timestamp_path = ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt"
    if draft_path.exists() or timestamp_path.exists():
        raise SystemExit("refusing to overwrite Queue 130 draft or timestamp")

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
                f"Queue 130 frozen core hash changed: {relative} "
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

    progress_matches = [
        record
        for record in load_jsonl(ROOT / "artifacts/progress.jsonl")
        if record.get("paper_id") == PAPER_ID
    ]
    if len(progress_matches) != 1:
        raise SystemExit(
            f"expected one Queue 130 progress record; found {len(progress_matches)}"
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
                f"Queue 130 progress {field} changed "
                f"({progress.get(field)!r} != {expected!r})"
            )
    if (
        progress.get("queue_position") != 130
        or progress.get("problem_type") != "B"
        or progress.get("year") != "2019"
    ):
        raise SystemExit("Queue 130 progress identity changed")

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
        "warning_count": len(card["unresolved_questions"]),
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
        "page_count": 33,
        "chapter_count": 13,
        "substantive_source_section_count": 18,
        "language_count": 252,
        "positive_reusable_language_count": 252,
        "weakness_count": 32,
        "model_count": 21,
        "equation_count": 24,
        "dependency_edge_count": 28,
        "visual_count": 28,
        "observation_count": 413,
        "warning_count": 8,
        "g7_warning_count": 30,
        "formula_warning_count": 10,
        "section_count": 13,
        "argument_count": 7,
        "abstract_paragraph_count": 7,
        "introduction_paragraph_count": 5,
        "rule_change_count": 9,
        "rule_count": 23,
        "rule_evidence_count": 27,
        "test_count": 119,
        "proxy_count": 8,
        "contact_sheet_proxy_count": 7,
        "focused_crop_proxy_count": 1,
        "segment_count": 1,
        "total_proxy_bytes": 2832549,
        "largest_proxy_bytes": 449543,
    }
    errors = [
        f"{field} differs from validated Queue 130 value ({counts[field]} != {expected})"
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
        errors.append("per-rule Q130 added-evidence counts changed")
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
        raise SystemExit("Queue 130 frozen-state mismatch: " + "; ".join(errors))

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
        "unresolved_added": card["unresolved_questions"],
        "unresolved_resolved": [],
        "validation_results": [
            {
                "validator": "validate_extraction.py",
                "status": "pass",
                "details": (
                    f"All {counts['page_count']} physical pages retain page-aware text and rendered pixels; "
                    "seven byte-bounded coverage JPEGs preserve pages 1-33 in order and one focused crop preserves "
                    "the cross-page ISO packing tables, with all eight hashes frozen."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all "
                    f"{counts['chapter_count']} normalized chapters and {counts['substantive_source_section_count']} "
                    "substantive source sections after Abstract and Introduction first-pass reading and a final "
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
                    "anti-copy checks with two original instantiations each and maximum shared content run 3."
                ),
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} model units retain {counts['equation_count']} visually checked equations "
                    f"or relations and {counts['dependency_edge_count']} handoff edges across fleet selection, "
                    "container packing, location, obstacle-aware delivery, scheduling, reconnaissance, ACO, and testing."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} five-part normalized chapter contracts, "
                    f"{counts['substantive_source_section_count']} substantive source sections, "
                    f"{counts['abstract_paragraph_count']} Abstract moves, "
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
                    "Two independent canonical replays and the staged bytes are byte-identical at "
                    f"{digest(rules_path)}; {counts['rule_change_count']} nominated B rules received "
                    f"{counts['rule_evidence_count']} paper-matched observations, the second replay added zero, "
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
                    f"All {counts['test_count']} regression tests pass against the Queue 130 frozen bytes and current "
                    "formal baseline."
                ),
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    f"One bounded context segment contains exactly {counts['proxy_count']} JPEGs/"
                    f"{counts['total_proxy_bytes']} bytes; the largest is {counts['largest_proxy_bytes']} bytes, below "
                    "450,000 bytes. No original full-page PNG, complete session JSONL, or printed base64 entered model "
                    "context. The prior HTTP 413 came from a 21,873,774-byte request containing 16 image data URLs and "
                    "about 19.873 MiB of base64; the exact nginx threshold remains unobservable."
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
