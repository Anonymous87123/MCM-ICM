#!/usr/bin/env python3
"""Validate per-paper protocol v2 formula-level model units."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PROBLEM_TYPES = set("ABCDEF")
REVIEW_STATUS = {"draft", "source-checked", "validated"}
VARIABLE_ROLES = {"input", "state", "parameter", "intermediate", "output"}
SOURCE_STATUS = {"explicit-defined", "inferred-from-equation", "unspecified"}
MODEL_ORIGINS = {"base", "modification", "hybrid", "paper-specific"}
EQUATION_SOURCE_TYPES = {"paper", "reconstructed", "extension"}
CONFIDENCE = {"high", "medium", "low"}
PRESENCE_STATUS = {"present", "omitted-by-paper", "not-applicable", "uncertain"}
PROCESS_STATUS = {
    "implemented",
    "partial",
    "omitted-by-paper",
    "not-applicable",
    "uncertain",
}
FEASIBILITY_STATUS = {"demonstrated", "partial", "not-demonstrated", "uncertain"}
MODEL_FIELDS = {
    "model_id",
    "page",
    "section",
    "family",
    "purpose",
    "base_or_modification",
    "summary",
    "variables",
    "inputs",
    "outputs",
    "governing_equations",
    "equation_status",
    "objectives",
    "constraints",
    "conditions",
    "parameter_estimation",
    "algorithm",
    "assumptions",
    "identifiability_feasibility",
    "handoff_outputs",
    "validation_refs",
    "computational_cost",
    "strengths",
    "limitations",
    "missing_details",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def string_list(value: Any, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (bool(value) or not nonempty)
        and all(nonempty_string(item) for item in value)
    )


def validate_status_details(value: Any, label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label} must be an object"]
    errors: list[str] = []
    if value.get("status") not in PRESENCE_STATUS:
        errors.append(f"{label} has invalid status")
    if not string_list(value.get("details")):
        errors.append(f"{label} details must be a string array")
    return errors


def validate_variable(value: Any, label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label} must be an object"]
    errors: list[str] = []
    for field in ("symbol", "normalized_name", "unit", "definition"):
        if not nonempty_string(value.get(field)):
            errors.append(f"{label} has empty {field}")
    if value.get("role") not in VARIABLE_ROLES:
        errors.append(f"{label} has invalid role")
    if value.get("source_status") not in SOURCE_STATUS:
        errors.append(f"{label} has invalid source_status")
    return errors


def validate_equation(
    value: Any,
    label: str,
    variable_symbols: set[str],
    page_count: int | None,
) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label} must be an object"]
    errors: list[str] = []
    equation_id = value.get("equation_id")
    if not nonempty_string(equation_id) or not equation_id.startswith("EQ-"):
        errors.append(f"{label} has invalid equation_id")
    page = value.get("page")
    if not isinstance(page, int) or page < 1:
        errors.append(f"{label} has invalid page")
    elif page_count is not None and page > page_count:
        errors.append(f"{label} page exceeds source page_count")
    for field in ("source_expression", "normalized_latex", "purpose"):
        if not nonempty_string(value.get(field)):
            errors.append(f"{label} has empty {field}")
    if value.get("label") is not None and not nonempty_string(value.get("label")):
        errors.append(f"{label} equation label must be null or nonempty")
    equation_variables = value.get("variable_symbols")
    if not string_list(equation_variables, nonempty=True):
        errors.append(f"{label} requires variable_symbols")
        equation_variables = []
    for symbol in equation_variables:
        if symbol not in variable_symbols:
            errors.append(f"{label} references undefined variable {symbol}")
    if value.get("source_type") not in EQUATION_SOURCE_TYPES:
        errors.append(f"{label} has invalid source_type")
    if value.get("visual_checked") is not True:
        errors.append(f"{label} visual_checked must be true")
    if value.get("transcription_confidence") not in CONFIDENCE:
        errors.append(f"{label} has invalid transcription_confidence")
    return errors


def validate_model(value: Any, problem_type: str, page_count: int | None, index: int) -> list[str]:
    label = f"models[{index}]"
    if not isinstance(value, dict):
        return [f"{label} must be an object"]
    errors: list[str] = []
    missing = sorted(MODEL_FIELDS - set(value))
    if missing:
        errors.append(f"{label} missing fields: {', '.join(missing)}")

    model_id = value.get("model_id")
    if not nonempty_string(model_id) or not re.fullmatch(
        rf"MU-{re.escape(problem_type)}-[A-Za-z0-9-]+", model_id
    ):
        errors.append(f"{label} has invalid model_id")
    page = value.get("page")
    if not isinstance(page, int) or page < 1:
        errors.append(f"{label} has invalid page")
    elif page_count is not None and page > page_count:
        errors.append(f"{label} page exceeds source page_count")
    for field in ("section", "family", "purpose", "summary", "computational_cost"):
        if not nonempty_string(value.get(field)):
            errors.append(f"{label} has empty {field}")
    if value.get("base_or_modification") not in MODEL_ORIGINS:
        errors.append(f"{label} has invalid base_or_modification")

    variables = value.get("variables")
    if not isinstance(variables, list) or not variables:
        errors.append(f"{label} requires variables")
        variables = []
    variable_symbols: set[str] = set()
    for variable_index, variable in enumerate(variables, start=1):
        errors.extend(validate_variable(variable, f"{label}.variables[{variable_index}]"))
        if isinstance(variable, dict) and nonempty_string(variable.get("symbol")):
            symbol = variable["symbol"]
            if symbol in variable_symbols:
                errors.append(f"{label} has duplicate variable {symbol}")
            variable_symbols.add(symbol)

    for field in ("inputs", "outputs", "handoff_outputs"):
        references = value.get(field)
        if not string_list(references):
            errors.append(f"{label} {field} must be a string array")
            continue
        for symbol in references:
            if symbol not in variable_symbols:
                errors.append(f"{label} {field} references undefined variable {symbol}")

    equations = value.get("governing_equations")
    if not isinstance(equations, list):
        errors.append(f"{label} governing_equations must be an array")
        equations = []
    equation_ids: set[str] = set()
    for equation_index, equation in enumerate(equations, start=1):
        errors.extend(
            validate_equation(
                equation,
                f"{label}.governing_equations[{equation_index}]",
                variable_symbols,
                page_count,
            )
        )
        if isinstance(equation, dict) and nonempty_string(equation.get("equation_id")):
            equation_id = equation["equation_id"]
            if equation_id in equation_ids:
                errors.append(f"{label} has duplicate equation_id {equation_id}")
            equation_ids.add(equation_id)

    equation_status = value.get("equation_status")
    if not isinstance(equation_status, dict):
        errors.append(f"{label} equation_status must be an object")
    else:
        status = equation_status.get("status")
        reason = equation_status.get("reason")
        if status not in PRESENCE_STATUS or not nonempty_string(reason):
            errors.append(f"{label} has invalid equation_status or empty reason")
        if equations and status != "present":
            errors.append(f"{label} equation_status must be present when equations exist")
        if not equations and status not in PRESENCE_STATUS - {"present"}:
            errors.append(f"{label} equation_status must explain why equations are absent")

    for field in ("objectives", "constraints", "assumptions", "validation_refs", "strengths", "limitations", "missing_details"):
        if not string_list(value.get(field), nonempty=True):
            errors.append(f"{label} requires nonempty {field}")

    conditions = value.get("conditions")
    if not isinstance(conditions, dict):
        errors.append(f"{label} conditions must be an object")
    else:
        for condition_name in ("initial", "boundary", "equilibrium"):
            errors.extend(
                validate_status_details(
                    conditions.get(condition_name), f"{label}.conditions.{condition_name}"
                )
            )

    estimation = value.get("parameter_estimation")
    if not isinstance(estimation, dict):
        errors.append(f"{label} parameter_estimation must be an object")
    else:
        if estimation.get("status") not in PROCESS_STATUS:
            errors.append(f"{label} parameter_estimation has invalid status")
        if not nonempty_string(estimation.get("method")):
            errors.append(f"{label} parameter_estimation has empty method")
        if not string_list(estimation.get("parameters")):
            errors.append(f"{label} parameter_estimation parameters must be a string array")

    algorithm = value.get("algorithm")
    if not isinstance(algorithm, dict):
        errors.append(f"{label} algorithm must be an object")
    else:
        status = algorithm.get("status")
        steps = algorithm.get("steps")
        if status not in PROCESS_STATUS:
            errors.append(f"{label} algorithm has invalid status")
        if not string_list(steps):
            errors.append(f"{label} algorithm steps must be a string array")
        elif status in {"implemented", "partial"} and not steps:
            errors.append(f"{label} algorithm steps are required for {status} status")
        if not string_list(algorithm.get("software")):
            errors.append(f"{label} algorithm software must be a string array")
        if not nonempty_string(algorithm.get("convergence_criteria")):
            errors.append(f"{label} algorithm has empty convergence_criteria")

    feasibility = value.get("identifiability_feasibility")
    if not isinstance(feasibility, dict):
        errors.append(f"{label} identifiability_feasibility must be an object")
    else:
        if feasibility.get("status") not in FEASIBILITY_STATUS:
            errors.append(f"{label} identifiability_feasibility has invalid status")
        if not nonempty_string(feasibility.get("analysis")):
            errors.append(f"{label} identifiability_feasibility has empty analysis")
    return errors


def validate_record(
    record: Any,
    manifest_record: dict[str, Any] | None = None,
) -> list[str]:
    if not isinstance(record, dict):
        return ["record must be an object"]
    errors: list[str] = []
    if record.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    problem_type = record.get("problem_type")
    if problem_type not in PROBLEM_TYPES:
        errors.append("problem_type must be A-F")
        problem_type = "?"
    paper_id = record.get("paper_id")
    if not nonempty_string(paper_id) or not paper_id.startswith(f"P-{problem_type}-"):
        errors.append("paper_id does not match problem_type")
    year = record.get("year")
    if not nonempty_string(year) or not re.fullmatch(r"(?:19|20)\d{2}", year):
        errors.append("year must be four digits")
    source_sha256 = record.get("source_sha256")
    if not nonempty_string(source_sha256) or not re.fullmatch(r"[a-f0-9]{64}", source_sha256):
        errors.append("source_sha256 must be lowercase SHA-256")
    if record.get("review_status") not in REVIEW_STATUS:
        errors.append("invalid review_status")

    page_count: int | None = None
    if manifest_record is not None:
        page_count = manifest_record.get("page_count")
        for field in ("paper_id", "problem_type", "year"):
            if record.get(field) != manifest_record.get(field):
                errors.append(f"{field} differs from manifest")
        if source_sha256 != manifest_record.get("sha256"):
            errors.append("source_sha256 differs from manifest")

    models = record.get("models")
    if not isinstance(models, list) or not models:
        errors.append("models must contain at least one model unit")
        models = []
    model_ids: set[str] = set()
    for index, model in enumerate(models, start=1):
        errors.extend(validate_model(model, problem_type, page_count, index))
        if isinstance(model, dict) and nonempty_string(model.get("model_id")):
            model_id = model["model_id"]
            if model_id in model_ids:
                errors.append(f"duplicate model_id {model_id}")
            model_ids.add(model_id)

    edges = record.get("dependency_edges")
    if not isinstance(edges, list):
        errors.append("dependency_edges must be an array")
        edges = []
    for index, edge in enumerate(edges, start=1):
        label = f"dependency_edges[{index}]"
        if not isinstance(edge, dict):
            errors.append(f"{label} must be an object")
            continue
        source_id = edge.get("from_model_id")
        target_id = edge.get("to_model_id")
        if source_id not in model_ids:
            errors.append(f"{label} references unknown model {source_id}")
        if target_id not in model_ids:
            errors.append(f"{label} references unknown model {target_id}")
        if source_id == target_id:
            errors.append(f"{label} creates a self dependency")
        if not nonempty_string(edge.get("handoff")):
            errors.append(f"{label} has empty handoff")
    return errors


def find_manifest_record(path: Path, paper_id: str) -> dict[str, Any]:
    matches: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            value = json.loads(line)
            if isinstance(value, dict) and value.get("paper_id") == paper_id:
                matches.append(value)
    if len(matches) != 1:
        raise ValueError(f"expected one manifest record for {paper_id}; found {len(matches)}")
    return matches[0]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        record = load_json(args.record)
        manifest_record = (
            find_manifest_record(args.manifest, record.get("paper_id", ""))
            if args.manifest
            else None
        )
        errors = validate_record(record, manifest_record)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors = [str(error)]
    report = {
        "error_count": len(errors),
        "errors": errors,
        "record": str(args.record),
        "status": "pass" if not errors else "fail",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
