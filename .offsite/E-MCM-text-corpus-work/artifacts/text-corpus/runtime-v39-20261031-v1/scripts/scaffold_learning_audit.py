#!/usr/bin/env python3
"""Create an explicitly incomplete learning-audit draft from validated artifacts."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


DIMENSIONS = (
    "language", "modeling", "logic", "visualization", "verification",
    "data", "assumption", "result", "weakness", "other",
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"expected object at {path}:{line_number}")
        records.append(value)
    return records


def find_manifest(path: Path, paper_id: str) -> dict[str, Any]:
    matches = [row for row in load_jsonl(path) if row.get("paper_id") == paper_id]
    if len(matches) != 1:
        raise ValueError(f"expected one manifest row for {paper_id}; found {len(matches)}")
    return matches[0]


def equation_ids(model: dict[str, Any]) -> list[str]:
    return [
        equation["equation_id"]
        for equation in model.get("governing_equations", [])
        if isinstance(equation, dict) and isinstance(equation.get("equation_id"), str)
    ]


def scaffold(
    language: dict[str, Any],
    models: dict[str, Any],
    card: dict[str, Any],
    observations: list[dict[str, Any]],
    manifest: dict[str, Any],
) -> dict[str, Any]:
    paper_id = language.get("paper_id")
    if language.get("schema_version") != 3:
        raise ValueError("language record must be schema v3 before audit scaffolding")
    if models.get("schema_version") != 2:
        raise ValueError("model record must be schema v2 before audit scaffolding")
    for artifact_name, artifact in (("model", models), ("card", card), ("manifest", manifest)):
        if artifact.get("paper_id") != paper_id:
            raise ValueError(f"{artifact_name} paper_id mismatch")

    chapters = list(language.get("available_chapters", []))
    layouts = {
        item.get("chapter"): item
        for item in language.get("chapter_layouts", [])
        if isinstance(item, dict)
    }
    units = [item for item in language.get("units", []) if isinstance(item, dict)]
    dispositions = []
    provisional_positive = 0
    for unit in units:
        targets = [item for item in unit.get("candidate_pattern_ids", []) if isinstance(item, str)]
        if targets:
            disposition = "opens-candidate"
            reason = "DRAFT: decide whether each nominated pattern is existing or newly opened."
            provisional_positive += 1
        else:
            disposition = "paper-specific-nonreusable"
            reason = "DRAFT: classify this unit; absence of a candidate ID is not evidence of nonreusability."
        dispositions.append({
            "language_unit_id": unit.get("language_unit_id"),
            "disposition": disposition,
            "target_pattern_ids": targets,
            "reason": reason,
        })

    paragraph_chains = []
    for chapter in ("abstract", "introduction"):
        if chapter not in chapters:
            continue
        paragraph_chains.append({
            "chapter": chapter,
            "visual_paragraph_count": layouts.get(chapter, {}).get("paragraph_count", 0),
            "coverage_status": "gap-open",
            "gaps": ["DRAFT: map every visual paragraph to its dominant move and language units."],
            "paragraphs": [],
        })

    model_rows = [item for item in models.get("models", []) if isinstance(item, dict)]
    retained_equations = [equation_id for model in model_rows for equation_id in equation_ids(model)]
    central = [
        {
            "model_id": model.get("model_id"),
            "equation_ids": equation_ids(model),
            "all_central_equations_retained": True,
        }
        for model in model_rows
        if equation_ids(model)
    ]
    counts = Counter(item.get("dimension") for item in observations)
    dimension_counts = {dimension: counts[dimension] for dimension in DIMENSIONS}
    visualizations = [item for item in card.get("visualization_observations", []) if isinstance(item, dict)]

    token = str(paper_id).replace("P-", "", 1).replace("-", "-")
    return {
        "schema_version": 1,
        "audit_id": f"LA-{token}-001",
        "paper_id": paper_id,
        "problem_type": language.get("problem_type"),
        "year": language.get("year"),
        "source_sha256": language.get("source_sha256"),
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [
            {
                "chapter": chapter,
                "pass_count": 1,
                "last_pass_new_moves": 1,
                "coverage_status": "gap-open",
                "gaps": ["DRAFT: run another positive-language pass and record all newly found moves."],
            }
            for chapter in chapters
        ],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "gap-open",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [],
            "section_progressions": [],
            "main_argument_chains": [],
        },
        "formula_error_watch": {
            "mode": "last-pass-warning-only",
            "completed_after_positive_passes": False,
            "warnings": [],
        },
        "model_retention": {
            "model_count": len(model_rows),
            "retained_model_ids": [model.get("model_id") for model in model_rows],
            "retained_equation_ids": retained_equations,
            "central_equations": central,
        },
        "visualization_dispositions": [
            {
                "paper_card_visual_index": index,
                "visual_record_id": f"V-{paper_id[2]}-{paper_id.split('-')[-2]}-{index:03d}",
                "disposition": "important-visual-record",
                "analytical_purpose": item.get("summary", "DRAFT: state analytical purpose."),
            }
            for index, item in enumerate(visualizations, 1)
        ],
        "dimension_counts": dimension_counts,
        "positive_reusable_language_count": provisional_positive,
        "weakness_record_count": dimension_counts["weakness"],
        "review_status": "draft",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language-record", type=Path, required=True)
    parser.add_argument("--model-record", type=Path, required=True)
    parser.add_argument("--paper-card", type=Path, required=True)
    parser.add_argument("--observations", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv or None)
    try:
        language = load_json(args.language_record)
        draft = scaffold(
            language,
            load_json(args.model_record),
            load_json(args.paper_card),
            load_jsonl(args.observations),
            find_manifest(args.manifest, str(language.get("paper_id", ""))),
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(draft, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1
    print(json.dumps({"status": "draft-created", "output": str(args.output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
