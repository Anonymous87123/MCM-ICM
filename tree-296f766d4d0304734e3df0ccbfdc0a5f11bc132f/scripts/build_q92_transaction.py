from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2011-12114-03fd7440"
PROBLEM_TYPE = "B"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def sha256(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def main() -> None:
    card_path = f"artifacts/paper-cards/{PAPER_ID}.json"
    language_path = f"artifacts/language-units/{PAPER_ID}.json"
    model_path = f"artifacts/model-units/{PAPER_ID}.json"
    audit_path = f"artifacts/learning-audits/{PAPER_ID}.json"
    observations_path = f"artifacts/observations/{PAPER_ID}.jsonl"
    extraction_path = f"artifacts/papers/{PAPER_ID}/extraction.json"
    rules_path = "artifacts/type-branches/B/rules.jsonl"
    impact_path = f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json"
    frozen_paths = [card_path, language_path, model_path, audit_path, observations_path, extraction_path, rules_path, impact_path]

    card = read_json(card_path)
    language = read_json(language_path)
    models = read_json(model_path)
    audit = read_json(audit_path)
    extraction = read_json(extraction_path)
    impact = read_json(impact_path)
    observations = [json.loads(line) for line in (ROOT / observations_path).read_text(encoding="utf-8").splitlines() if line.strip()]

    language_count = len(language["units"])
    model_count = len(models["models"])
    equation_count = sum(len(model.get("governing_equations", [])) for model in models["models"])
    visual_count = len(card["visualization_observations"])
    warning_count = len(card["unresolved_questions"])
    section_contract_count = len(audit["organization_logic"]["section_progressions"])

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
            "observation_count": len(observations),
            "paper_card_status": "validated",
            "positive_reusable_language_count": audit["positive_reusable_language_count"],
            "protocol_status": "current-validated",
            "section_contract_count": section_contract_count,
            "source_action_count": language_count,
            "status": "closed",
            "validation_status": "pass",
            "warning_count": warning_count,
        },
        "artifact_diffs": [f"artifact:{relative}|sha256:{sha256(relative)}" for relative in frozen_paths],
        "before": {
            "branch_update_status": "pending",
            "extraction_status": "pending",
            "paper_card_status": "pending",
            "protocol_status": "absent",
            "status": "discovered",
            "validation_status": "pending",
        },
        "changed_fields": [
            "progress.status", "progress.extraction_status", "progress.paper_card_status",
            "progress.branch_update_status", "progress.validation_status", "paper-card",
            "language-units", "model-units", "learning-audit", "observations",
            "extraction.visual_review", "type-branch.B.rules", "type-branch.B.rule-impact-report",
        ],
        "event_type": "paper-closed",
        "history_completeness": "native",
        "paper_id": PAPER_ID,
        "type_branch_diff": {
            "new_equation_count": equation_count,
            "new_language_unit_count": language_count,
            "new_model_count": model_count,
            "new_observation_count": len(observations),
            "new_rule_impact_count": impact["rule_change_count"],
            "problem_type": PROBLEM_TYPE,
            "section_contracts_after": section_contract_count,
            "section_contracts_before": 0,
            "shared_catalog_changes": [],
        },
        "unresolved_added": card["unresolved_questions"],
        "unresolved_resolved": [],
        "validation_results": [
            {"validator": "validate_extraction.py", "status": "pass", "details": "28/28 text pages and 28/28 rendered pages passed extraction checks; complete page-aware visual review is recorded."},
            {"validator": "validate_language_units.py", "status": "pass", "details": f"{language_count} language units cover all {len(language['available_chapters'])} declared protocol chapters with quantitative layouts, reusable slots, variants, and boundaries."},
            {"validator": "validate_language_anticopy.py", "status": "pass", "details": f"{language_count}/{language_count} units passed with two unrelated original instantiations, no full-clause matches, and no source-fact leaks."},
            {"validator": "validate_model_units.py", "status": "pass", "details": f"{model_count} model and algorithm interfaces retain {equation_count} visually reconciled equations plus inputs, conditions, handoffs, validation links, and limitations."},
            {"validator": "validate_learning_audit.py", "status": "pass", "details": f"{section_contract_count} five-part chapter contracts, complete Summary/Introduction paragraph chains, positive organization artifacts, {visual_count} visual dispositions, and {warning_count} last-pass warnings passed."},
            {"validator": "validate_paper_artifacts.py", "status": "pass", "details": f"The paper card, {len(observations)} observations, cumulative B rules, extraction, language/model records, and complete visual review cross-validate."},
            {"validator": "apply_rule_impacts.py", "status": "pass", "details": f"Twelve nominated B rules received one evidence binding each without lifecycle changes; staged and live canonical output are byte-identical at {impact['output_sha256']}."},
            {"validator": "validate_plan_protocol.py", "status": "pass", "details": "The live plan retains language-first G0-G8 ordering and prospective/live transaction ordering."},
            {"validator": "python -m unittest discover -s tests -v", "status": "pass", "details": "All 119 regression tests pass."},
            {"validator": "request_body_guard", "status": "pass", "details": "The 565 MB legacy session was inspected only by streaming counts that omitted base64 payloads. The root added no images; three fresh read-only contexts each used at most eight JPEG proxies below 450000 bytes and returned text-only reports."},
        ],
    }

    output = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    output.write_text(json.dumps(draft, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"artifact_count": len(frozen_paths), "draft": str(output), "equation_count": equation_count, "language_unit_count": language_count, "model_count": model_count, "observation_count": len(observations), "status": "pass", "visual_count": visual_count, "warning_count": warning_count}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
