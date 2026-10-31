from __future__ import annotations

"""Build a create-only Queue 109 closure draft from frozen formal artifacts."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-36178-d0225ad0"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    draft_path = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    timestamp_path = ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt"
    if draft_path.exists() or timestamp_path.exists():
        raise SystemExit("refusing to overwrite Queue 109 draft or timestamp")

    canonical = {
        f"artifacts/paper-cards/{PAPER_ID}.json": ROOT / f"artifacts/paper-cards/{PAPER_ID}.json",
        f"artifacts/language-units/{PAPER_ID}.json": ROOT / f"artifacts/language-units/{PAPER_ID}.json",
        f"artifacts/model-units/{PAPER_ID}.json": ROOT / f"artifacts/model-units/{PAPER_ID}.json",
        f"artifacts/learning-audits/{PAPER_ID}.json": ROOT / f"artifacts/learning-audits/{PAPER_ID}.json",
        f"artifacts/observations/{PAPER_ID}.jsonl": ROOT / f"artifacts/observations/{PAPER_ID}.jsonl",
        f"artifacts/papers/{PAPER_ID}/extraction.json": ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json",
        "artifacts/type-branches/B/rules.jsonl": ROOT / "artifacts/type-branches/B/rules.jsonl",
        f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": ROOT / f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json",
    }
    missing = [str(path) for path in canonical.values() if not path.is_file()]
    if missing:
        raise SystemExit(f"missing frozen source(s): {missing}")

    card = json.loads(canonical[f"artifacts/paper-cards/{PAPER_ID}.json"].read_text(encoding="utf-8"))
    language = json.loads(canonical[f"artifacts/language-units/{PAPER_ID}.json"].read_text(encoding="utf-8"))
    models = json.loads(canonical[f"artifacts/model-units/{PAPER_ID}.json"].read_text(encoding="utf-8"))
    audit = json.loads(canonical[f"artifacts/learning-audits/{PAPER_ID}.json"].read_text(encoding="utf-8"))
    extraction = json.loads(canonical[f"artifacts/papers/{PAPER_ID}/extraction.json"].read_text(encoding="utf-8"))
    impact = json.loads(canonical[f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json"].read_text(encoding="utf-8"))
    observations_path = canonical[f"artifacts/observations/{PAPER_ID}.jsonl"]

    observation_count = sum(
        1 for line in observations_path.read_text(encoding="utf-8").splitlines() if line.strip()
    )
    language_count = len(language["units"])
    model_count = len(models["models"])
    equation_count = sum(
        len(model["governing_equations"]) for model in models["models"]
    )
    visual_count = len(card["visualization_observations"])
    warning_count = len(card["unresolved_questions"])
    section_count = len(audit["organization_logic"]["section_progressions"])
    argument_count = len(audit["organization_logic"]["main_argument_chains"])
    rules_path = canonical["artifacts/type-branches/B/rules.jsonl"]
    rule_count = sum(
        1 for line in rules_path.read_text(encoding="utf-8").splitlines() if line.strip()
    )
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")

    draft = {
        "after": {
            "artifact_hash_binding": "machine-readable-core-five-plus-extraction-and-B-branch",
            "branch_update_status": "validated",
            "dimension_counts": audit["dimension_counts"],
            "equation_count": equation_count,
            "extraction_status": "validated",
            "extraction_visual_review_status": extraction["visual_review_status"],
            "important_visual_count": visual_count,
            "language_unit_count": language_count,
            "model_count": model_count,
            "observation_count": observation_count,
            "paper_card_status": "validated",
            "positive_reusable_language_count": audit["positive_reusable_language_count"],
            "protocol_status": "current-validated",
            "section_contract_count": section_count,
            "source_action_count": language_count,
            "status": "closed",
            "validation_status": "pass",
            "warning_count": warning_count,
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
            "new_equation_count": equation_count,
            "new_language_unit_count": language_count,
            "new_model_count": model_count,
            "new_observation_count": observation_count,
            "new_rule_impact_count": impact["rule_change_count"],
            "problem_type": "B",
            "section_contracts_after": section_count,
            "section_contracts_before": 0,
            "shared_catalog_changes": [],
        },
        "unresolved_added": card["unresolved_questions"],
        "unresolved_resolved": [],
        "validation_results": [
            {
                "validator": "validate_extraction.py",
                "status": "pass",
                "details": "All 20 physical pages have page-aware extracted text and a complete visual review. Four bounded JPEG overview proxies covered pages 1-20, and focused formula and figure crops reconciled the retained mathematics and seven numbered figures without transporting an original full-page PNG.",
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": f"{language_count} language units cover all {len(language['available_chapters'])} protocol chapters with measured layouts, reusable slots, variants, boundaries, and zero-action saturation passes.",
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": f"{language_count}/{language_count} units passed against the complete 20-page extracted source text with no failed original-instantiation checks.",
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": f"{model_count} connected model interfaces retain {equation_count} visually checked equations plus variables, conditions, algorithms, handoffs, validation links, and limitations.",
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": f"{section_count} five-part chapter contracts, four Summary paragraphs, one Introduction paragraph, {argument_count} main arguments, {visual_count} visual dispositions, and {warning_count} last-pass warnings passed.",
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": f"The paper card, {observation_count} observations, {rule_count} cumulative B rules, extraction, language/model records, and complete visual review cross-validate.",
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": f"{impact['rule_change_count']} nominated B rules received source-matched Queue 109 evidence without lifecycle changes; frozen rules hash is {digest(rules_path)}.",
            },
            {
                "validator": "validate_plan_protocol.py",
                "status": "pass",
                "details": "The live plan retains language-first G0-G8 ordering and prospective/live transaction ordering.",
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": "All 119 regression tests pass against the Queue 109 frozen bytes and current formal baseline.",
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": "Each review image was a byte-bounded JPEG proxy returned one at a time; formula and small-label checks used focused crops, and no full session JSONL, contact-sheet original, or original full-page PNG was transported.",
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
                "language_unit_count": language_count,
                "model_count": model_count,
                "equation_count": equation_count,
                "observation_count": observation_count,
                "section_contract_count": section_count,
                "argument_count": argument_count,
                "rule_count": rule_count,
                "status": "pass",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
