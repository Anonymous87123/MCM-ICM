#!/usr/bin/env python3
"""Build a create-only Queue 129 closure draft from frozen canonical bytes."""

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
PAPER_ID = "P-B-2019-1923964-678ee565"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID

EXPECTED_PROXIES = [
    ("review-proxies/01-pages-0001-0005.jpg", 445715, "1e3829c7969cbd1a04af4ffe1887f66b510e660d980ea701ce582c5cfe50d337"),
    ("review-proxies/02-pages-0006-0010.jpg", 448497, "87aa58868314c1ba0a192de0c116f82562e6af40c8c5b92decb5361019b1e82e"),
    ("review-proxies/03-pages-0011-0015.jpg", 430479, "4dfa8e7cfe156c35bcfcdb4077d5eb36bc2952e65bd1b8c56e14b2f1c68cb8f4"),
    ("review-proxies/04-pages-0016-0020.jpg", 440711, "db04e8a0a305dbc7ea88f4ef8e1ce9d2b2de1baa0c2443ea0d69aa9ed2744468"),
    ("review-proxies/05-pages-0021-0025.jpg", 415784, "63d60b8f98bc62a0fb6f1f4bd18f1361aa205d131de1a62e6d686d523ae13ab5"),
    ("review-proxies/06-focus-payload-camera.jpg", 228925, "89b523d5b58a63db73bd6e5ff0e7d58f0842614db4b8a3ae100ac20b4dbd9a0e"),
    ("review-proxies/07-focus-combination-importance.jpg", 373802, "99478f1562fb63e7d58d4f98ddb3f79a41ac0f439615dd42625ad06817d02c28"),
    ("review-proxies/08-focus-maps-sensitivity.jpg", 439503, "13fe6ff0b8849a3419c9665ddfb550962f9b1a1796cdf295c28aedabf900e96b"),
]

EXPECTED_CORE_HASHES = {
    f"artifacts/paper-cards/{PAPER_ID}.json": "aa852338785e35683ce4abe1907df90d5afd67abd22d8212ee8ac3955886598b",
    f"artifacts/language-units/{PAPER_ID}.json": "b767c916e4de421e00e36be03aa344ef9b201a5f0057eb5e01f6d9af50032cf6",
    f"artifacts/model-units/{PAPER_ID}.json": "1547592f259a1d64cf1f4fa58e4ca4361caac9f5d21f27cc2f1e3cc87b94de07",
    f"artifacts/learning-audits/{PAPER_ID}.json": "34a7e0282f3e1db54e26ff3ed354f6e55c8655c8e7cd0d0502b5c1c028794b22",
    f"artifacts/observations/{PAPER_ID}.jsonl": "d8a2086e6cdb616dddf80f69f4ade901317436222c08e72ba85f82d47d0d7522",
    f"artifacts/papers/{PAPER_ID}/extraction.json": "fff36e6f208a96b7ad1a797f65ee05eb675a4fee3645734b4d210666e6640b4e",
    "artifacts/type-branches/B/rules.jsonl": "cc5cc9cddec228b3b79b57c30d8533e1d2e9a92cafea4bc26ed69cea92ac8b14",
    f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": "4e3663f25a1af1144f2e28a385ffd94b2343894ea710b2a3cb93d2d8298e20b2",
}

EXPECTED_PATTERNS = {
    "LP-B-ABS-METHOD-RESULT-LADDER": 18,
    "LP-B-MEMO-SCENARIO-OPTION": 18,
    "LP-B-ANL-DECOMPOSE-HANDOFF": 19,
    "LP-B-ASM-PREMISE-JUSTIFY": 10,
    "LP-B-MOD-DERIVE-TRANSFER": 33,
    "LP-B-ALG-STATE-STEP-STOP": 14,
    "LP-B-RES-VISUAL-DECISION": 28,
    "LP-B-SEN-PERTURB-COMPARE": 10,
    "LP-B-LIM-BOUNDARY-NEXT": 12,
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

    records = manifest.get("files")
    if not isinstance(records, list):
        raise SystemExit("visual_review_manifest files must be an array")
    expected_paths = [item[0] for item in EXPECTED_PROXIES]
    expected_sizes = {path: size for path, size, _ in EXPECTED_PROXIES}
    expected_hashes = {path: sha256 for path, _, sha256 in EXPECTED_PROXIES}
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
        if size > 450_000:
            raise SystemExit(f"review proxy exceeds 450,000 bytes: {relative}")
        verified.append({"path": relative, "bytes": size, "sha256": sha256})

    expected_pages = list(range(1, 26))
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
        raise SystemExit("extraction review does not cover physical pages 1-25")

    total = sum(item["bytes"] for item in verified)
    largest = max(item["bytes"] for item in verified)
    if len(verified) != 8 or total >= 4 * 1024 * 1024:
        raise SystemExit("review context segment exceeds the request-body guard")
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
        raise SystemExit("refusing to overwrite Queue 129 draft or timestamp")

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
                f"Queue 129 frozen core hash changed: {relative} "
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
        raise SystemExit(f"expected one Queue 129 progress record; found {len(progress_matches)}")
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
                f"Queue 129 progress {field} changed "
                f"({progress.get(field)!r} != {expected!r})"
            )
    if (
        progress.get("queue_position") != 129
        or progress.get("problem_type") != "B"
        or progress.get("year") != "2019"
    ):
        raise SystemExit("Queue 129 progress identity changed")

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
        "observation_count": len(observations),
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
        "page_count": 25,
        "chapter_count": 19,
        "language_count": 162,
        "positive_reusable_language_count": 162,
        "weakness_count": 26,
        "model_count": 17,
        "equation_count": 23,
        "dependency_edge_count": 24,
        "visual_count": 23,
        "observation_count": 298,
        "warning_count": 6,
        "formula_warning_count": 10,
        "section_count": 19,
        "argument_count": 6,
        "abstract_paragraph_count": 7,
        "introduction_paragraph_count": 2,
        "rule_change_count": 9,
        "rule_count": 23,
        "test_count": 119,
        "proxy_count": 8,
        "contact_sheet_proxy_count": 5,
        "focused_crop_proxy_count": 3,
        "segment_count": 1,
        "total_proxy_bytes": 3223416,
        "largest_proxy_bytes": 448497,
    }
    errors = [
        f"{field} differs from validated Queue 129 value ({counts[field]} != {expected})"
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
    if len(changes) != counts["rule_change_count"] or changed_lifecycles != EXPECTED_RULE_LIFECYCLES:
        errors.append("rule-impact changes or preserved lifecycles changed")
    if added_counts != EXPECTED_ADDED_EVIDENCE_COUNTS:
        errors.append("per-rule Q129 added-evidence counts changed")
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
        raise SystemExit("Queue 129 frozen-state mismatch: " + "; ".join(errors))

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
                    "five contact-sheet JPEGs cover pages 1-25 in order and three focused JPEG crops preserve "
                    "payload/camera formulas, combination/importance relations, maps, and sensitivity fidelity, "
                    "with all eight hashes frozen."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} source-anchored language units cover all {counts['chapter_count']} "
                    "chapters after Summary and Introduction first-pass reading and a final zero-new-move saturation pass; "
                    "the nine retained rhetorical patterns occur "
                    + ", ".join(f"{key}={value}" for key, value in patterns.items())
                    + "."
                ),
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']}/{counts['language_count']} language units passed complete-source "
                    "anti-copy checks with two original instantiations each and maximum shared content run 2."
                ),
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} model units retain {counts['equation_count']} visually checked equations "
                    f"or relations and {counts['dependency_edge_count']} handoff edges across terrain interpolation, "
                    "payload-duration reach, camera geometry, destination/fleet combinations, allocation, road importance, "
                    "PSO and grid siting, joint operations, Dijkstra routing, Haiti transfer, and sensitivity comparison."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} five-part chapter contracts, {counts['abstract_paragraph_count']} Summary "
                    f"moves, {counts['introduction_paragraph_count']} Introduction moves, {counts['argument_count']} main "
                    f"chains, {counts['visual_count']} visual dispositions, and {counts['formula_warning_count']} final "
                    f"formula warnings passed; positive language {counts['positive_reusable_language_count']} strictly "
                    f"exceeds weakness evidence {counts['weakness_count']}."
                ),
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": (
                    f"The card, {counts['observation_count']} observations, {counts['rule_count']} cumulative B rules, "
                    "extraction, language record, model record, and complete 25-page visual review cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    f"Two independent canonical replays are byte-identical at {digest(rules_path)}, and the staged rule "
                    f"objects are semantically identical; {counts['rule_change_count']} nominated B rules received "
                    "26 paper-matched observations while all seed/corroborated lifecycle labels remained unchanged."
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
                "details": f"All {counts['test_count']} regression tests pass against the Queue 129 frozen bytes and current formal baseline.",
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
