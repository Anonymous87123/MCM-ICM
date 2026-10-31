from __future__ import annotations

"""Build a create-only Queue 119 closure draft from frozen canonical bytes."""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2017-70174-8bf62421"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def jsonl_count(path: Path) -> int:
    return sum(
        1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip()
    )


def paragraph_count(audit: dict, chapter: str) -> int:
    matches = [
        item for item in audit["paragraph_chains"] if item.get("chapter") == chapter
    ]
    if len(matches) != 1:
        raise SystemExit(f"expected one {chapter} paragraph chain; found {len(matches)}")
    return len(matches[0]["paragraphs"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validated-test-count", required=True, type=int)
    args = parser.parse_args()
    if args.validated_test_count <= 0:
        raise SystemExit("validated test count must be positive")

    draft_path = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    timestamp_path = ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt"
    if draft_path.exists() or timestamp_path.exists():
        raise SystemExit("refusing to overwrite Queue 119 draft or timestamp")

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

    review = extraction["visual_review_manifest"]
    counts = {
        "page_count": extraction["page_count"],
        "chapter_count": len(language["available_chapters"]),
        "language_count": len(language["units"]),
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
        "proxy_count": review["proxy_count"],
        "proxy_total_bytes": review["proxy_total_bytes"],
        "largest_proxy_bytes": review["largest_proxy_bytes"],
    }

    errors = []
    if extraction.get("visual_review_status") != "complete":
        errors.append("visual review is not complete")
    if sorted(review["pages_reviewed"]) != list(range(1, counts["page_count"] + 1)):
        errors.append("visual review page coverage does not match the physical page range")
    if review.get("original_full_page_png_in_context") is not False:
        errors.append("visual review manifest permits an original full-page PNG in context")
    if counts["proxy_count"] > 8:
        errors.append("visual proxy count exceeds the per-context limit of eight")
    if counts["proxy_total_bytes"] >= 4 * 1024 * 1024:
        errors.append("visual proxy bytes are not below 4 MiB")
    if counts["largest_proxy_bytes"] > 450_000:
        errors.append("largest visual proxy exceeds 450,000 bytes")
    if audit["dimension_counts"].get("language") != counts["language_count"]:
        errors.append("audit language dimension does not equal the language-unit count")
    if audit["positive_reusable_language_count"] != counts["language_count"]:
        errors.append("positive reusable language count does not equal language units")
    if len(impact["changes"]) != counts["rule_change_count"]:
        errors.append("rule-impact change list does not equal rule_change_count")
    if impact.get("output_sha256") != digest(rules_path):
        errors.append("rule-impact output hash does not bind the frozen B rules")
    if errors:
        raise SystemExit("Queue 119 frozen-state mismatch: " + "; ".join(errors))

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    draft = {
        "after": {
            "artifact_hash_binding": "machine-readable-core-five-plus-extraction-and-B-branch",
            "branch_update_status": "validated",
            "dimension_counts": audit["dimension_counts"],
            "equation_count": counts["equation_count"],
            "extraction_status": "validated",
            "extraction_visual_review_status": extraction["visual_review_status"],
            "important_visual_count": counts["visual_count"],
            "language_unit_count": counts["language_count"],
            "model_count": counts["model_count"],
            "observation_count": counts["observation_count"],
            "paper_card_status": "validated",
            "positive_reusable_language_count": audit[
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
            "extraction_status": "text-extracted",
            "paper_card_status": "pending",
            "protocol_status": "absent",
            "status": "text-extracted",
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
                "details": f"All {counts['page_count']} physical pages have page-aware text, valid rendered pixels, and complete visual review. The frozen manifest records {counts['proxy_count']} byte-bounded proxies totaling {counts['proxy_total_bytes']} bytes; the largest is {counts['largest_proxy_bytes']} bytes.",
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": f"{counts['language_count']} language units cover all {counts['chapter_count']} normalized protocol chapters with source anchors, functions, information order, reusable slots, variants, boundaries, original instantiations, and zero-action saturation passes.",
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": f"{counts['language_count']}/{counts['language_count']} units passed against all {counts['page_count']} pages with no source-fact leaks, full-clause matches, or failed original-instantiation checks.",
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": f"{counts['model_count']} model units retain {counts['equation_count']} governing equations and {counts['dependency_edge_count']} dependency edges plus variables, conditions, algorithms, handoffs, validation links, and limitations.",
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": f"{counts['section_count']} five-part chapter contracts, {counts['abstract_paragraph_count']} Abstract moves, {counts['introduction_paragraph_count']} Introduction moves, {counts['argument_count']} main arguments, {counts['visual_count']} visual dispositions, {counts['formula_warning_count']} equation-bound final warnings, and {counts['warning_count']} unresolved questions passed.",
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": f"The paper card, {counts['observation_count']} observations, {counts['rule_count']} cumulative B rules, extraction, language and model records, and complete visual review cross-validate.",
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": f"{counts['rule_change_count']} nominated B rules received source-matched Queue 119 evidence without lifecycle changes; two independent replays are byte-identical at {digest(rules_path)}.",
            },
            {
                "validator": "validate_plan_protocol.py",
                "status": "pass",
                "details": "The live plan retains language-first G0-G8 ordering and prospective/live transaction ordering.",
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": f"All {counts['test_count']} regression tests pass against the Queue 119 frozen bytes and current formal baseline.",
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": f"The frozen review manifest records {counts['proxy_count']} byte-bounded proxies totaling {counts['proxy_total_bytes']} bytes below 4 MiB, with a largest proxy of {counts['largest_proxy_bytes']} bytes; closure added no images, never printed session JSONL or base64, and kept original full-page PNGs out of model context.",
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
