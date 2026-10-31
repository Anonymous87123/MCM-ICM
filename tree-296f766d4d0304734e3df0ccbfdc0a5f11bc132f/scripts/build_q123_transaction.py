#!/usr/bin/env python3
"""Build a create-only Queue 123 closure draft from frozen canonical bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-77238-4380ec81"
PROXY_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID / "review-proxies"


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


def checked_proxy_paths(expected: dict[str, Any], name: str) -> list[Path]:
    relative_paths = expected.get("proxy_files")
    if not isinstance(relative_paths, list) or not relative_paths or not all(
        isinstance(item, str) and item for item in relative_paths
    ):
        raise SystemExit(f"{name} has invalid proxy_files")
    root = PROXY_ROOT.resolve()
    paths: list[Path] = []
    for relative in relative_paths:
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise SystemExit(f"{name} has unsafe proxy path: {relative}")
        path = (root / candidate).resolve()
        try:
            path.relative_to(root)
        except ValueError as error:
            raise SystemExit(f"{name} proxy escapes review root: {relative}") from error
        paths.append(path)
    if len(paths) != len(set(paths)):
        raise SystemExit(f"{name} contains duplicate proxy paths")
    return paths


def verify_segment(name: str, expected: dict[str, Any]) -> dict[str, Any]:
    paths = checked_proxy_paths(expected, name)
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit(f"missing {name} review proxies: {missing}")
    sizes = [path.stat().st_size for path in paths]
    if len(sizes) > 8:
        raise SystemExit(f"{name} exceeds the eight-image context-segment limit")
    if max(sizes) > 450_000 or sum(sizes) >= 4 * 1024 * 1024:
        raise SystemExit(f"{name} exceeds the request-body review guard")
    if len(paths) != int(expected.get("proxy_count", -1)):
        raise SystemExit(f"{name} proxy count differs from extraction manifest")
    if sum(sizes) != int(expected.get("total_proxy_bytes", -1)):
        raise SystemExit(f"{name} byte total differs from extraction manifest")
    if max(sizes) != int(expected.get("largest_proxy_bytes", -1)):
        raise SystemExit(f"{name} largest proxy differs from extraction manifest")
    return {
        "name": name,
        "proxy_count": len(paths),
        "total_proxy_bytes": sum(sizes),
        "largest_proxy_bytes": max(sizes),
    }


def proxy_summary(extraction: dict[str, Any]) -> dict[str, Any]:
    manifest = extraction.get("visual_review_manifest")
    if not isinstance(manifest, dict):
        raise SystemExit("extraction has no visual_review_manifest")
    full_expected = manifest.get("full_page_proxy_segments")
    focused_expected = manifest.get("focused_crop_segments")
    if not isinstance(full_expected, list) or len(full_expected) != 4:
        raise SystemExit("four full-page review segments are required")
    if not isinstance(focused_expected, list) or len(focused_expected) != 1:
        raise SystemExit("one focused-crop review segment is required")

    expected_page_groups = (
        list(range(1, 8)),
        list(range(8, 15)),
        list(range(15, 22)),
        list(range(22, 24)),
    )
    segments: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    for index, (expected, pages) in enumerate(
        zip(full_expected, expected_page_groups, strict=True), start=1
    ):
        if not isinstance(expected, dict) or expected.get("page_range") != pages:
            raise SystemExit(f"full-page-{index} page range changed")
        paths = expected.get("proxy_files", [])
        expected_names = [f"full/page-{page:04d}.jpg" for page in pages]
        if paths != expected_names:
            raise SystemExit(f"full-page-{index} proxy identity changed")
        if seen_paths.intersection(paths):
            raise SystemExit(f"full-page-{index} reuses a proxy from another segment")
        seen_paths.update(paths)
        segments.append(verify_segment(f"full-page-{index}", expected))

    focused = focused_expected[0]
    if not isinstance(focused, dict) or focused.get("page_range") != [7, 11, 11, 23]:
        raise SystemExit("focused-crop page coverage changed")
    focused_names = [
        "focused/page-0007-ci-cr.jpg",
        "focused/page-0011-cosine.jpg",
        "focused/page-0011-office-objective.jpg",
        "focused/page-0023-map-table.jpg",
    ]
    if focused.get("proxy_files") != focused_names:
        raise SystemExit("focused-crop proxy identity changed")
    if seen_paths.intersection(focused_names):
        raise SystemExit("focused-crop segment reuses a full-page proxy")
    segments.append(verify_segment("focused-crop-1", focused))

    full_count = sum(item["proxy_count"] for item in segments[:4])
    focused_count = segments[4]["proxy_count"]
    if full_count != int(manifest.get("full_page_proxy_count", -1)):
        raise SystemExit("full-page proxy total differs from extraction manifest")
    if focused_count != int(manifest.get("focused_crop_proxy_count", -1)):
        raise SystemExit("focused-crop proxy total differs from extraction manifest")
    if manifest.get("pages_reviewed") != list(
        range(1, int(extraction["page_count"]) + 1)
    ):
        raise SystemExit("visual review page coverage differs from physical pages")
    if manifest.get("original_full_page_png_in_context") is not False:
        raise SystemExit("review manifest permits an original full-page PNG in context")
    return {
        "proxy_count": full_count + focused_count,
        "full_page_proxy_count": full_count,
        "focused_crop_proxy_count": focused_count,
        "segment_count": len(segments),
        "segments": segments,
        "largest_proxy_bytes": max(
            item["largest_proxy_bytes"] for item in segments
        ),
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
        raise SystemExit("refusing to overwrite Queue 123 draft or timestamp")

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
        f"artifacts/papers/{PAPER_ID}/extraction.json": ROOT
        / f"artifacts/papers/{PAPER_ID}/extraction.json",
        "artifacts/type-branches/B/rules.jsonl": ROOT
        / "artifacts/type-branches/B/rules.jsonl",
        f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": ROOT
        / f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json",
    }
    missing = [str(path) for path in canonical.values() if not path.is_file()]
    if missing:
        raise SystemExit(f"missing frozen source(s): {missing}")

    card = load_json(canonical[f"artifacts/paper-cards/{PAPER_ID}.json"])
    language = load_json(canonical[f"artifacts/language-units/{PAPER_ID}.json"])
    models = load_json(canonical[f"artifacts/model-units/{PAPER_ID}.json"])
    audit = load_json(canonical[f"artifacts/learning-audits/{PAPER_ID}.json"])
    extraction = load_json(
        canonical[f"artifacts/papers/{PAPER_ID}/extraction.json"]
    )
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
            f"expected one Queue 123 progress record; found {len(progress_matches)}"
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
        if field == "protocol_status":
            continue
        if progress.get(field) != expected:
            raise SystemExit(
                f"Queue 123 progress {field} changed "
                f"({progress.get(field)!r} != {expected!r})"
            )
    if (
        progress.get("queue_position") != 123
        or progress.get("problem_type") != "B"
        or progress.get("year") != "2018"
    ):
        raise SystemExit("Queue 123 progress identity changed")

    review = proxy_summary(extraction)
    dispositions = audit.get("language_unit_dispositions", [])
    computed_positive = sum(
        item.get("disposition") != "paper-specific-nonreusable"
        for item in dispositions
        if isinstance(item, dict)
    )
    counts = {
        "page_count": extraction["page_count"],
        "chapter_count": len(language["available_chapters"]),
        "language_count": len(language["units"]),
        "positive_reusable_language_count": audit[
            "positive_reusable_language_count"
        ],
        "weakness_count": audit["dimension_counts"]["weakness"],
        "model_count": len(models["models"]),
        "equation_count": sum(
            len(model["governing_equations"]) for model in models["models"]
        ),
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
        "page_count": 23,
        "chapter_count": 16,
        "language_count": 106,
        "positive_reusable_language_count": 106,
        "weakness_count": 18,
        "model_count": 13,
        "equation_count": 27,
        "dependency_edge_count": 18,
        "visual_count": 45,
        "observation_count": 302,
        "warning_count": 12,
        "formula_warning_count": 18,
        "section_count": 16,
        "argument_count": 7,
        "abstract_paragraph_count": 4,
        "introduction_paragraph_count": 3,
        "rule_change_count": 11,
        "rule_count": 23,
        "test_count": 119,
        "full_page_proxy_count": 23,
        "focused_crop_proxy_count": 4,
        "proxy_count": 27,
        "segment_count": 5,
    }
    errors = [
        f"{field} differs from validated Queue 123 value "
        f"({counts[field]} != {expected})"
        for field, expected in expected_counts.items()
        if counts[field] != expected
    ]
    dimensions = audit["dimension_counts"]
    if extraction.get("visual_review_status") != "complete":
        errors.append("visual review is not complete")
    if dimensions.get("language") != counts["language_count"]:
        errors.append("audit language dimension differs from language-unit count")
    if counts["positive_reusable_language_count"] != computed_positive:
        errors.append("positive reusable language count differs from dispositions")
    if len(impact.get("changes", [])) != counts["rule_change_count"]:
        errors.append("rule-impact change list differs from rule_change_count")
    if impact.get("output_sha256") != digest(rules_path):
        errors.append("rule-impact output hash does not bind frozen B rules")
    if counts["warning_count"] >= counts["language_count"]:
        errors.append("unresolved question count is not a strict minority of language units")
    if counts["weakness_count"] >= counts["positive_reusable_language_count"]:
        errors.append("weakness count is not below positive reusable language evidence")
    if dimensions["language"] <= max(
        count for dimension, count in dimensions.items() if dimension != "language"
    ):
        errors.append("language is not the strictly largest evidence dimension")
    protocol = card.get("protocol_v2_records", {})
    if protocol.get("language", {}).get("path") != (
        f"artifacts/language-units/{PAPER_ID}.json"
    ):
        errors.append("card language canonical path is incorrect")
    if protocol.get("models", {}).get("path") != (
        f"artifacts/model-units/{PAPER_ID}.json"
    ):
        errors.append("card model canonical path is incorrect")
    if errors:
        raise SystemExit("Queue 123 frozen-state mismatch: " + "; ".join(errors))

    timestamp = args.timestamp_utc or datetime.now(timezone.utc).replace(
        microsecond=0
    ).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp):
        raise SystemExit("timestamp must be an exact UTC second: YYYY-MM-DDTHH:MM:SSZ")

    draft = {
        "after": {
            "artifact_hash_binding": "machine-readable-core-five-plus-extraction-and-B-branch",
            "branch_update_status": "validated",
            "dimension_counts": dimensions,
            "equation_count": counts["equation_count"],
            "extraction_status": "validated",
            "extraction_visual_review_status": extraction["visual_review_status"],
            "important_visual_count": counts["visual_count"],
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
            "extraction.visual_review",
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
        },
        "unresolved_added": card["unresolved_questions"],
        "unresolved_resolved": [],
        "validation_results": [
            {
                "validator": "validate_extraction.py",
                "status": "pass",
                "details": (
                    f"All {counts['page_count']} physical pages have page-aware text "
                    f"and complete visual review; {counts['proxy_count']} byte-bounded "
                    f"proxies were verified in {counts['segment_count']} independent "
                    "context segments."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} author-language units cover all "
                    f"{counts['chapter_count']} normalized chapters with source anchors, "
                    "functions, information order, reusable slots, variants, boundaries, "
                    "original instantiations, and zero-action saturation."
                ),
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']}/{counts['language_count']} units passed "
                    "complete-source anti-copy checks without full-clause, unique-shingle, "
                    "or source-fact leakage."
                ),
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} model units retain "
                    f"{counts['equation_count']} governing equations and "
                    f"{counts['dependency_edge_count']} dependency edges plus variables, "
                    "conditions, algorithms, handoffs, validation links, and limitations."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} chapter contracts, "
                    f"{counts['abstract_paragraph_count']} Abstract moves, "
                    f"{counts['introduction_paragraph_count']} Introduction moves, "
                    f"{counts['argument_count']} main arguments, "
                    f"{counts['visual_count']} visual dispositions, "
                    f"{counts['formula_warning_count']} equation-bound final warnings, "
                    f"and {counts['positive_reusable_language_count']} positive reusable "
                    "language units passed."
                ),
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": (
                    f"The card, {counts['observation_count']} observations, "
                    f"{counts['rule_count']} cumulative B rules, extraction, language and "
                    "model records, and complete visual review cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    f"{counts['rule_change_count']} nominated B rules received "
                    "source-matched Queue 123 evidence without lifecycle changes; two "
                    f"independent replays are byte-identical at {digest(rules_path)}."
                ),
            },
            {
                "validator": "validate_plan_protocol.py",
                "status": "pass",
                "details": (
                    "The live plan retains language-first G0-G8 ordering and "
                    "prospective/live transaction ordering."
                ),
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": (
                    f"All {counts['test_count']} regression tests pass against the "
                    "Queue 123 frozen bytes and current formal baseline."
                ),
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    "The review manifest records five bounded segments: "
                    + "; ".join(
                        f"{item['name']} {item['proxy_count']} proxies/"
                        f"{item['total_proxy_bytes']} bytes"
                        for item in counts["segments"]
                    )
                    + f"; each segment is below 4 MiB, the largest proxy is "
                    f"{counts['largest_proxy_bytes']} bytes, and no full-page PNG, "
                    "session JSONL, or base64 entered model context."
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
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
