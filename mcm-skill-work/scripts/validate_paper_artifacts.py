#!/usr/bin/env python3
"""Cross-validate one paper card, observations, rules, manifest, and extraction."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


EVIDENCE_CLASSES = {"O", "P", "I", "E", "J", "C"}
DIMENSIONS = {
    "language", "modeling", "logic", "visualization", "verification", "data",
    "assumption", "result", "weakness", "other",
}
CONFIDENCE = {"high", "medium", "low"}
LIFECYCLES = {
    "seed", "candidate", "corroborated", "bounded", "operationalized",
    "promoted", "challenged", "revised", "retired",
}
PAGE_ANCHORED_CARD_FIELDS = (
    "section_map", "contributions", "assumptions", "data_and_preprocessing",
    "models", "verification", "results_trace", "writing_logic",
    "language_observations", "visualization_observations",
    "judge_relevance_hypotheses", "weaknesses",
)
REQUIRED_CARD_FIELDS = (
    "schema_version", "paper_id", "problem_type", "year", "source",
    "source_quality", "task_reconstruction", "section_map", "contributions",
    "dependency_graph", "assumptions", "data_and_preprocessing", "models",
    "verification", "results_trace", "writing_logic", "language_observations",
    "visualization_observations", "judge_relevance_hypotheses", "weaknesses",
    "independent_extensions", "candidate_rule_impacts", "unresolved_questions",
    "review_status",
)
REQUIRED_OBSERVATION_FIELDS = (
    "schema_version", "observation_id", "paper_id", "problem_type", "year",
    "page", "section", "evidence_class", "dimension", "source_basis",
    "interpretation", "applicability", "counterevidence", "confidence",
    "candidate_rule_ids",
)
REQUIRED_RULE_FIELDS = (
    "schema_version", "rule_id", "problem_type", "dimension", "lifecycle",
    "statement", "applicability", "inapplicable", "procedure", "positive_pattern",
    "forbidden", "evidence_ids", "source_papers", "source_count", "confidence",
    "required_tests",
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                value = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path} line {line_number}: {error}") from error
            if not isinstance(value, dict):
                raise ValueError(f"{path} line {line_number}: expected object")
            values.append(value)
    return values


def observation_corpus_paths(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(candidate for candidate in path.glob("*.jsonl") if candidate.is_file())
    raise ValueError(f"observation corpus does not exist: {path}")


def build_observation_index(
    current_path: Path,
    current_observations: list[dict[str, Any]],
    corpus_path: Path | None,
) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    source_by_id: dict[str, Path] = {}

    def add(records: list[dict[str, Any]], source: Path) -> None:
        for record in records:
            observation_id = record.get("observation_id")
            if not isinstance(observation_id, str) or not observation_id:
                continue
            if observation_id in index:
                previous = source_by_id[observation_id]
                raise ValueError(
                    f"duplicate observation_id {observation_id} in {previous} and {source}"
                )
            index[observation_id] = record
            source_by_id[observation_id] = source

    resolved_current = current_path.resolve()
    add(current_observations, resolved_current)
    if corpus_path is not None:
        for path in observation_corpus_paths(corpus_path):
            resolved_path = path.resolve()
            if resolved_path == resolved_current:
                continue
            add(load_jsonl(path), resolved_path)
    return index


def find_manifest_record(path: Path, paper_id: str) -> dict[str, Any]:
    matches = [record for record in load_jsonl(path) if record.get("paper_id") == paper_id]
    if len(matches) != 1:
        raise ValueError(f"expected one manifest record for {paper_id}; found {len(matches)}")
    return matches[0]


def missing_fields(value: dict[str, Any], required: tuple[str, ...]) -> list[str]:
    return [field for field in required if field not in value]


def validate_protocol_v2_records(
    card: dict[str, Any],
    language_record: dict[str, Any] | None,
    model_record: dict[str, Any] | None,
) -> list[str]:
    declarations = card.get("protocol_v2_records")
    if declarations is None:
        return []
    if not isinstance(declarations, dict):
        return ["paper card protocol_v2_records must be an object"]
    errors: list[str] = []
    paper_id = card.get("paper_id")

    language_declaration = declarations.get("language")
    if language_declaration is not None:
        if language_record is None:
            errors.append("paper card declares a language record but none was supplied")
        elif not isinstance(language_declaration, dict):
            errors.append("paper card language declaration must be an object")
        else:
            if language_record.get("paper_id") != paper_id:
                errors.append("language record paper_id differs from paper card")
            if language_declaration.get("schema_version") != language_record.get("schema_version"):
                errors.append("paper card language schema_version differs from language record")
            if language_declaration.get("unit_count") != len(language_record.get("units", [])):
                errors.append("paper card language unit_count differs from language record")
            if language_declaration.get("chapters") != language_record.get("available_chapters"):
                errors.append("paper card language chapters differ from language record")
            if language_declaration.get("review_status") != language_record.get("review_status"):
                errors.append("paper card language review_status differs from language record")

    model_declaration = declarations.get("models")
    if model_declaration is not None:
        if model_record is None:
            errors.append("paper card declares a model record but none was supplied")
        elif not isinstance(model_declaration, dict):
            errors.append("paper card model declaration must be an object")
        else:
            models = model_record.get("models", [])
            equation_count = sum(
                len(model.get("governing_equations", []))
                for model in models
                if isinstance(model, dict)
            )
            if model_record.get("paper_id") != paper_id:
                errors.append("model record paper_id differs from paper card")
            if model_declaration.get("model_count") != len(models):
                errors.append("paper card model_count differs from model record")
            if model_declaration.get("equation_count") != equation_count:
                errors.append("paper card equation_count differs from model record")
            if model_declaration.get("review_status") != model_record.get("review_status"):
                errors.append("paper card model review_status differs from model record")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-card", type=Path, required=True)
    parser.add_argument("--observations", type=Path, required=True)
    parser.add_argument("--rules", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--extraction", type=Path, required=True)
    parser.add_argument(
        "--observation-corpus",
        type=Path,
        help="JSONL file or directory containing cross-paper observations used by cumulative rules.",
    )
    parser.add_argument("--require-complete-visual-review", action="store_true")
    parser.add_argument("--language-record", type=Path)
    parser.add_argument("--model-record", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    errors: list[str] = []

    try:
        card = load_json(args.paper_card)
        observations = load_jsonl(args.observations)
        rules = load_jsonl(args.rules)
        extraction = load_json(args.extraction)
        manifest = find_manifest_record(args.manifest, card.get("paper_id", ""))
        evidence_observations = build_observation_index(
            args.observations, observations, args.observation_corpus
        )
        language_record = load_json(args.language_record) if args.language_record else None
        model_record = load_json(args.model_record) if args.model_record else None
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1

    missing = missing_fields(card, REQUIRED_CARD_FIELDS)
    if missing:
        errors.append(f"paper card missing fields: {', '.join(missing)}")
    paper_id = card.get("paper_id")
    problem_type = card.get("problem_type")
    year = card.get("year")
    page_count = card.get("source", {}).get("page_count")
    if card.get("schema_version") != 1:
        errors.append("paper card schema_version must be 1")
    if problem_type not in set("ABCDEF"):
        errors.append("invalid paper card problem_type")
    if not isinstance(page_count, int) or page_count < 1:
        errors.append("invalid paper card page_count")
        page_count = 0
    if card.get("review_status") not in {"draft", "source-checked", "validated"}:
        errors.append("invalid paper card review_status")

    source = card.get("source", {})
    for field in ("relative_path", "sha256", "page_count"):
        if source.get(field) != manifest.get(field):
            errors.append(f"paper card source {field} differs from manifest")
    for field in ("paper_id", "problem_type", "year"):
        if card.get(field) != manifest.get(field):
            errors.append(f"paper card {field} differs from manifest")
    for field in ("paper_id", "problem_type", "year", "page_count", "source_sha256"):
        if field == "source_sha256":
            expected = source.get("sha256")
        elif field == "page_count":
            expected = source.get("page_count")
        else:
            expected = card.get(field)
        if extraction.get(field) != expected:
            errors.append(f"extraction {field} mismatch")
    if args.require_complete_visual_review and extraction.get("visual_review_status") != "complete":
        errors.append("complete visual review required")
    errors.extend(validate_protocol_v2_records(card, language_record, model_record))

    for field in PAGE_ANCHORED_CARD_FIELDS:
        value = card.get(field)
        if not isinstance(value, list):
            errors.append(f"paper card {field} is not an array")
            continue
        for index, item in enumerate(value, start=1):
            if not isinstance(item, dict):
                errors.append(f"paper card {field}[{index}] is not an object")
                continue
            page = item.get("page")
            if not isinstance(page, int) or page < 1 or page > page_count:
                errors.append(f"paper card {field}[{index}] has invalid page")
            if not isinstance(item.get("summary"), str) or not item["summary"].strip():
                errors.append(f"paper card {field}[{index}] has empty summary")

    observation_ids: set[str] = set()
    for index, observation in enumerate(observations, start=1):
        missing = missing_fields(observation, REQUIRED_OBSERVATION_FIELDS)
        if missing:
            errors.append(f"observation {index} missing: {', '.join(missing)}")
            continue
        observation_id = observation["observation_id"]
        if observation_id in observation_ids:
            errors.append(f"duplicate observation_id: {observation_id}")
        observation_ids.add(observation_id)
        for field, expected in (("paper_id", paper_id), ("problem_type", problem_type), ("year", year)):
            if observation.get(field) != expected:
                errors.append(f"{observation_id}: {field} mismatch")
        if observation.get("evidence_class") not in EVIDENCE_CLASSES:
            errors.append(f"{observation_id}: invalid evidence_class")
        if observation.get("dimension") not in DIMENSIONS:
            errors.append(f"{observation_id}: invalid dimension")
        if observation.get("confidence") not in CONFIDENCE:
            errors.append(f"{observation_id}: invalid confidence")
        page = observation.get("page")
        if not isinstance(page, int) or page < 1 or page > page_count:
            errors.append(f"{observation_id}: invalid page")

    rule_ids: set[str] = set()
    for index, rule in enumerate(rules, start=1):
        missing = missing_fields(rule, REQUIRED_RULE_FIELDS)
        if missing:
            errors.append(f"rule {index} missing: {', '.join(missing)}")
            continue
        rule_id = rule["rule_id"]
        if rule_id in rule_ids:
            errors.append(f"duplicate rule_id: {rule_id}")
        rule_ids.add(rule_id)
        if rule.get("problem_type") != problem_type:
            errors.append(f"{rule_id}: type mismatch")
        if rule.get("lifecycle") not in LIFECYCLES:
            errors.append(f"{rule_id}: invalid lifecycle")
        if rule.get("confidence") not in CONFIDENCE:
            errors.append(f"{rule_id}: invalid confidence")
        if rule.get("source_count") != len(set(rule.get("source_papers", []))):
            errors.append(f"{rule_id}: source_count mismatch")
        evidence_papers: set[str] = set()
        for evidence_id in rule.get("evidence_ids", []):
            evidence = evidence_observations.get(evidence_id)
            if evidence is None:
                errors.append(f"{rule_id}: unknown evidence_id {evidence_id}")
                continue
            evidence_paper = evidence.get("paper_id")
            evidence_type = evidence.get("problem_type")
            if isinstance(evidence_paper, str):
                evidence_papers.add(evidence_paper)
            if evidence_type != problem_type:
                errors.append(f"{rule_id}: evidence {evidence_id} has type mismatch")
        source_papers = set(rule.get("source_papers", []))
        if evidence_papers != source_papers:
            errors.append(
                f"{rule_id}: source_papers do not match evidence papers "
                f"({sorted(source_papers)} != {sorted(evidence_papers)})"
            )

    for observation in observations:
        for rule_id in observation.get("candidate_rule_ids", []):
            if rule_id not in rule_ids:
                errors.append(f"{observation['observation_id']}: unknown rule_id {rule_id}")
    for impact in card.get("candidate_rule_impacts", []):
        if impact.get("rule_id") not in rule_ids:
            errors.append(f"paper card impact references unknown rule {impact.get('rule_id')}")
    for extension in card.get("independent_extensions", []):
        if not str(extension.get("extension_id", "")).startswith(f"E-{problem_type}-"):
            errors.append("independent extension has invalid id or type")
    for hypothesis in card.get("judge_relevance_hypotheses", []):
        if hypothesis.get("evidence_class") not in {"C", "J"}:
            errors.append("judge relevance hypothesis must be class C or J")

    report = {
        "error_count": len(errors),
        "errors": errors,
        "observation_count": len(observations),
        "page_count": page_count,
        "paper_id": paper_id,
        "rule_count": len(rules),
        "status": "pass" if not errors else "fail",
        "visual_review_status": extraction.get("visual_review_status"),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
