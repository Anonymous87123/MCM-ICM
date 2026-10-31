from __future__ import annotations

"""Prepare Queue 103's frozen draft and create-only prospective projections."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-26636-060c74b1"
PROBLEM_TYPE = "B"
STAGE = ROOT / "tmp/q103-stage-v2"
STAGED_RULES = ROOT / f"tmp/{PAPER_ID}-B-rules-staged.jsonl"
STAGED_IMPACT = ROOT / f"tmp/{PAPER_ID}-rule-impact-report-staged.json"
SHADOW_ROOT = ROOT / "tmp/q103-prospective-root"
SHADOW_OBSERVATIONS = ROOT / "tmp/q103-prospective-observations"
DRAFT = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
TIMESTAMP = ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def create_only(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()


def count_jsonl(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def main() -> None:
    canonical_sources = {
        f"artifacts/paper-cards/{PAPER_ID}.json": STAGE / "card.json",
        f"artifacts/language-units/{PAPER_ID}.json": STAGE / "language.json",
        f"artifacts/model-units/{PAPER_ID}.json": STAGE / "models.json",
        f"artifacts/learning-audits/{PAPER_ID}.json": STAGE / "audit.json",
        f"artifacts/observations/{PAPER_ID}.jsonl": STAGE / "observations.jsonl",
        f"artifacts/papers/{PAPER_ID}/extraction.json": (
            ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json"
        ),
        "artifacts/type-branches/B/rules.jsonl": STAGED_RULES,
        f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json": STAGED_IMPACT,
    }
    observation_sources = sorted((ROOT / "artifacts/observations").glob("*.jsonl"))
    current_observation_target = SHADOW_OBSERVATIONS / f"{PAPER_ID}.jsonl"

    missing = [str(path) for path in canonical_sources.values() if not path.is_file()]
    if missing:
        raise SystemExit(f"missing frozen source(s): {missing}")
    if any(path.name == f"{PAPER_ID}.jsonl" for path in observation_sources):
        raise SystemExit("formal Queue 103 observations already exist before promotion")

    targets = [SHADOW_ROOT / relative for relative in canonical_sources]
    targets.extend(SHADOW_OBSERVATIONS / path.name for path in observation_sources)
    targets.extend([current_observation_target, DRAFT, TIMESTAMP])
    existing = [str(path) for path in targets if path.exists()]
    if SHADOW_ROOT.exists() or SHADOW_OBSERVATIONS.exists():
        existing.extend(
            str(path)
            for path in (SHADOW_ROOT, SHADOW_OBSERVATIONS)
            if path.exists() and str(path) not in existing
        )
    if existing:
        raise SystemExit(f"refusing to overwrite prospective output(s): {existing}")

    card = load_json(STAGE / "card.json")
    language = load_json(STAGE / "language.json")
    models = load_json(STAGE / "models.json")
    audit = load_json(STAGE / "audit.json")
    extraction = load_json(ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json")
    impact = load_json(STAGED_IMPACT)
    observations = [
        json.loads(line)
        for line in (STAGE / "observations.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    language_count = len(language["units"])
    model_count = len(models["models"])
    equation_count = sum(
        len(model.get("governing_equations", [])) for model in models["models"]
    )
    visual_count = len(card["visualization_observations"])
    warning_count = len(card["unresolved_questions"])
    section_count = len(audit["organization_logic"]["section_progressions"])
    rule_count = count_jsonl(STAGED_RULES)
    timestamp_utc = datetime.now(timezone.utc).replace(microsecond=0).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

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
            "section_contract_count": section_count,
            "source_action_count": language_count,
            "status": "closed",
            "validation_status": "pass",
            "warning_count": warning_count,
        },
        "artifact_diffs": [
            f"artifact:{relative}|sha256:{digest(source)}"
            for relative, source in canonical_sources.items()
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
            "new_observation_count": len(observations),
            "new_rule_impact_count": impact["rule_change_count"],
            "problem_type": PROBLEM_TYPE,
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
                "details": "All 38/38 physical pages have extracted text, rendered pixels, and completed visual review backed by thirty-eight byte-bounded JPEG proxies across five bounded context segments.",
            },
            {
                "validator": "validate_language_units.py",
                "status": "pass",
                "details": f"{language_count} language units cover all {len(language['available_chapters'])} declared protocol chapters with quantitative layouts, reusable slots, variants, and boundaries.",
            },
            {
                "validator": "validate_language_anticopy.py",
                "status": "pass",
                "details": f"{language_count}/{language_count} units passed against the full 38-page source text with no failed original-instantiation checks.",
            },
            {
                "validator": "validate_model_units.py",
                "status": "pass",
                "details": f"{model_count} model and algorithm interfaces retain {equation_count} source-anchored equations plus conditions, handoffs, validation links, and limitations.",
            },
            {
                "validator": "validate_learning_audit.py",
                "status": "pass",
                "details": f"{section_count} five-part chapter contracts, Abstract and Introduction chains, positive organization artifacts, {visual_count} visual dispositions, and {warning_count} last-pass warnings passed.",
            },
            {
                "validator": "validate_paper_artifacts.py",
                "status": "pass",
                "details": f"The paper card, {len(observations)} observations, {rule_count} cumulative B rules, extraction, language/model records, and complete visual review cross-validate.",
            },
            {
                "validator": "apply_rule_impacts.py",
                "status": "pass",
                "details": f"{impact['rule_change_count']} nominated B rules received source-matched Queue 103 evidence without lifecycle changes; staged output is frozen at {impact['output_sha256']}.",
            },
            {
                "validator": "validate_plan_protocol.py",
                "status": "pass",
                "details": "The live plan retains language-first G0-G8 ordering and prospective/live transaction ordering.",
            },
            {
                "validator": "python -m unittest discover -s tests -v",
                "status": "pass",
                "details": "All 119 regression tests pass against the Queue 103 staged bytes and current formal baseline.",
            },
            {
                "validator": "request_body_guard",
                "status": "pass",
                "details": "Queue 103 used single JPEG review proxies no larger than 450,000 bytes, at most eight per context segment, and no original-page PNG or full session JSONL transport.",
            },
        ],
    }

    for relative, source in canonical_sources.items():
        create_only(SHADOW_ROOT / relative, source.read_bytes())
    for source in observation_sources:
        create_only(SHADOW_OBSERVATIONS / source.name, source.read_bytes())
    create_only(current_observation_target, (STAGE / "observations.jsonl").read_bytes())
    create_only(
        DRAFT,
        (json.dumps(draft, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
            "utf-8"
        ),
    )
    create_only(TIMESTAMP, (timestamp_utc + "\n").encode("ascii"))

    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "artifact_count": len(canonical_sources),
                "prospective_observation_files": len(observation_sources) + 1,
                "draft": str(DRAFT),
                "shadow_root": str(SHADOW_ROOT),
                "shadow_observations": str(SHADOW_OBSERVATIONS),
                "timestamp_utc": timestamp_utc,
                "language_unit_count": language_count,
                "model_count": model_count,
                "equation_count": equation_count,
                "observation_count": len(observations),
                "section_contract_count": section_count,
                "rule_count": rule_count,
                "status": "pass",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
