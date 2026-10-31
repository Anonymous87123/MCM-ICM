#!/usr/bin/env python3
"""Build a create-only Queue 121 closure draft from frozen canonical bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-73410-069a3764"
PROXY_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID / "review-proxies"
FORMULA_GROUPS = (
    (
        "p05-fig1-eq1.jpg",
        "p06-eq2-eq4.jpg",
        "p06-eq5-eq6.jpg",
        "p07-fig2-eq7.jpg",
        "p08-eq8-eq10.jpg",
        "p08-eq11-eq12.jpg",
        "p09-table1-eq13.jpg",
    ),
    (
        "p11-symbols.jpg",
        "p12-fig3.jpg",
        "p12-matrix-eq14-eq15.jpg",
        "p13-english-matrix.jpg",
        "p13-eq16-data.jpg",
        "p14-eq17-parameters.jpg",
    ),
    (
        "p17-sensitivity-eq.jpg",
        "p18-eq18.jpg",
        "p18-fig8.jpg",
        "p19-sa-parameters.jpg",
        "p19-symbols.jpg",
        "p20-weights-gdp.jpg",
    ),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"expected JSON object: {path}")
    return value


def jsonl_count(path: Path) -> int:
    with path.open("r", encoding="utf-8") as handle:
        return sum(1 for line in handle if line.strip())


def paragraph_count(audit: dict[str, Any], chapter: str) -> int:
    matches = [
        item for item in audit["paragraph_chains"] if item.get("chapter") == chapter
    ]
    if len(matches) != 1:
        raise SystemExit(f"expected one {chapter} paragraph chain; found {len(matches)}")
    return len(matches[0]["paragraphs"])


def verify_segment(
    name: str, paths: list[Path], expected: dict[str, Any]
) -> dict[str, Any]:
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit(f"missing {name} review proxies: {missing}")
    sizes = [path.stat().st_size for path in paths]
    if not sizes or len(sizes) > 8:
        raise SystemExit(f"{name} has an invalid proxy count")
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
    formula_expected = manifest.get("formula_proxy_segments")
    if not isinstance(full_expected, list) or len(full_expected) != 4:
        raise SystemExit("full-page review segments are missing or incomplete")
    if not isinstance(formula_expected, list) or len(formula_expected) != 3:
        raise SystemExit("formula review segments are missing or incomplete")

    segments: list[dict[str, Any]] = []
    for index, (first_page, last_page) in enumerate(
        ((1, 7), (8, 14), (15, 21), (22, 28)), start=1
    ):
        paths = [
            PROXY_ROOT / "full" / f"page-{page:04d}.jpg"
            for page in range(first_page, last_page + 1)
        ]
        segments.append(
            verify_segment(f"full-page-{index}", paths, full_expected[index - 1])
        )
    for index, names in enumerate(FORMULA_GROUPS, start=1):
        paths = [PROXY_ROOT / "formulas" / name for name in names]
        segments.append(
            verify_segment(f"formula-{index}", paths, formula_expected[index - 1])
        )

    full_count = sum(item["proxy_count"] for item in segments[:4])
    formula_count = sum(item["proxy_count"] for item in segments[4:])
    if full_count != int(manifest.get("full_page_proxy_count", -1)):
        raise SystemExit("full-page proxy total differs from extraction manifest")
    if formula_count != int(manifest.get("formula_proxy_count", -1)):
        raise SystemExit("formula proxy total differs from extraction manifest")
    if sorted(manifest.get("pages_reviewed", [])) != list(
        range(1, int(extraction["page_count"]) + 1)
    ):
        raise SystemExit("visual review page coverage differs from physical pages")
    if manifest.get("original_full_page_png_in_context") is not False:
        raise SystemExit("review manifest permits an original full-page PNG in context")
    return {
        "proxy_count": full_count + formula_count,
        "full_page_proxy_count": full_count,
        "formula_proxy_count": formula_count,
        "segment_count": len(segments),
        "segments": segments,
        "largest_proxy_bytes": max(item["largest_proxy_bytes"] for item in segments),
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
        raise SystemExit("refusing to overwrite Queue 121 draft or timestamp")

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

    visual_by_figure = {
        item.get("figure"): item
        for item in card.get("visualization_observations", [])
        if isinstance(item, dict)
    }
    table_1_rows = visual_by_figure.get("Table 1 and Equation (13)", {}).get(
        "structured_ledger", {}
    ).get("rows", [])
    table_8_rows = visual_by_figure.get("Tables 6-8", {}).get(
        "structured_ledger", {}
    ).get("rows", [])
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
        "non_prose_review_count": len(card.get("non_prose_source_reviews", [])),
        "language_count": len(language["units"]),
        "positive_reusable_language_count": audit["positive_reusable_language_count"],
        "weakness_count": audit["dimension_counts"]["weakness"],
        "model_count": len(models["models"]),
        "equation_count": sum(
            len(model["governing_equations"]) for model in models["models"]
        ),
        "dependency_edge_count": len(models["dependency_edges"]),
        "visual_count": len(card["visualization_observations"]),
        "table_1_row_count": len(table_1_rows),
        "table_8_row_count": len(table_8_rows),
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

    errors: list[str] = []
    dimensions = audit["dimension_counts"]
    if extraction.get("visual_review_status") != "complete":
        errors.append("visual review is not complete")
    if dimensions.get("language") != counts["language_count"]:
        errors.append("audit language dimension differs from language-unit count")
    if counts["positive_reusable_language_count"] != computed_positive:
        errors.append("positive reusable language count differs from dispositions")
    if counts["positive_reusable_language_count"] != 82:
        errors.append("positive reusable language count differs from the validated 82")
    if counts["weakness_count"] != 18:
        errors.append("weakness count differs from the validated 18")
    if counts["non_prose_review_count"] != 5:
        errors.append("appendix non-prose source review count differs from five")
    if counts["table_1_row_count"] != 10 or counts["table_8_row_count"] != 19:
        errors.append("Table 1 or Table 8 ledger is incomplete")
    table_8_labels = [row.get("source_label") for row in table_8_rows]
    if table_8_labels.count("Spain") != 2 or "Rassia" not in table_8_labels or "Bengaladesh" not in table_8_labels:
        errors.append("Table 8 source-label fidelity changed")
    if not any(
        row.get("source_label") == "Spain"
        and row.get("probable_intended_label") == "Brazil"
        for row in table_8_rows
    ):
        errors.append("Table 8 probable Brazil label review is missing")
    if len(impact["changes"]) != counts["rule_change_count"]:
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
    if protocol.get("language", {}).get("path") != f"artifacts/language-units/{PAPER_ID}.json":
        errors.append("card language canonical path is incorrect")
    if protocol.get("models", {}).get("path") != f"artifacts/model-units/{PAPER_ID}.json":
        errors.append("card model canonical path is incorrect")
    if errors:
        raise SystemExit("Queue 121 frozen-state mismatch: " + "; ".join(errors))

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
        "before": {
            "branch_update_status": "pending",
            "extraction_status": "pending",
            "paper_card_status": "pending",
            "protocol_status": "absent",
            "status": "discovered",
            "validation_status": "pending",
        },
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
                    f"All {counts['page_count']} physical pages have page-aware text and complete visual review; "
                    f"{counts['proxy_count']} byte-bounded proxies were verified in {counts['segment_count']} independent context segments."
                ),
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": (
                    f"{counts['language_count']} author-language units cover {counts['chapter_count']} prose chapters with source anchors, functions, information order, reusable slots, variants, boundaries, original instantiations, and zero-action saturation; {counts['non_prose_review_count']} Appendix spans remain separate structural source reviews."
                ),
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": f"{counts['language_count']}/{counts['language_count']} units passed complete-source anti-copy checks with maximum shared content run four.",
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": (
                    f"{counts['model_count']} model units retain {counts['equation_count']} governing equations and {counts['dependency_edge_count']} dependency edges plus variables, conditions, algorithms, handoffs, validation links, and limitations."
                ),
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": (
                    f"{counts['section_count']} prose chapter contracts, {counts['abstract_paragraph_count']} Abstract moves, {counts['introduction_paragraph_count']} Introduction moves, {counts['argument_count']} main arguments, {counts['visual_count']} visual dispositions, {counts['formula_warning_count']} equation-bound final warnings, and {counts['positive_reusable_language_count']} positive reusable language units passed."
                ),
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": (
                    f"The card, {counts['observation_count']} observations, {counts['rule_count']} cumulative B rules, extraction, language and model records, complete visual review, and exact {counts['table_1_row_count']}/{counts['table_8_row_count']} Table 1/Table 8 ledgers cross-validate."
                ),
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": (
                    f"{counts['rule_change_count']} nominated B rules received source-matched Queue 121 evidence without lifecycle changes; two independent replays are byte-identical at {digest(rules_path)}."
                ),
            },
            {
                "validator": "validate_plan_protocol.py",
                "status": "pass",
                "details": "The live plan retains language-first G0-G8 ordering and prospective/live transaction ordering.",
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": f"All {counts['test_count']} regression tests pass against the Queue 121 frozen bytes and current formal baseline.",
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": (
                    "The review manifest records seven bounded segments: "
                    + "; ".join(
                        f"{item['name']} {item['proxy_count']} proxies/{item['total_proxy_bytes']} bytes"
                        for item in counts["segments"]
                    )
                    + f"; each segment is below 4 MiB, the largest proxy is {counts['largest_proxy_bytes']} bytes, and no full-page PNG, session JSONL, or base64 entered model context."
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
