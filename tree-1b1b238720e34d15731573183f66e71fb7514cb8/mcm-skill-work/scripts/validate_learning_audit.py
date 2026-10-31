#!/usr/bin/env python3
"""Validate the language-first learning audit for one paper."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


PRIORITY_ORDER = [
    "language-imitation",
    "organization-logic",
    "formula-error-watch",
]
SECTION_CONTRACT_PREFIXES = (
    "input:",
    "rhetorical job:",
    "analytical job:",
    "output:",
    "handoff:",
)
DIMENSIONS = {
    "language",
    "modeling",
    "logic",
    "visualization",
    "verification",
    "data",
    "assumption",
    "result",
    "weakness",
    "other",
}
DISPOSITIONS = {
    "supports-existing",
    "opens-candidate",
    "paper-specific-nonreusable",
}
IDENTITY_FIELDS = ("paper_id", "problem_type", "year")


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


def find_manifest_record(path: Path, paper_id: str) -> dict[str, Any]:
    matches = [record for record in load_jsonl(path) if record.get("paper_id") == paper_id]
    if len(matches) != 1:
        raise ValueError(
            f"expected one manifest record for {paper_id}; found {len(matches)}"
        )
    return matches[0]


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(nonempty_string(item) for item in value)
    )


def object_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def string_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if isinstance(item, str)}


def duplicate_strings(values: list[Any]) -> set[str]:
    strings = [value for value in values if isinstance(value, str)]
    counts = Counter(strings)
    return {value for value, count in counts.items() if count > 1}


def validate_identity(
    audit: dict[str, Any],
    language: dict[str, Any],
    models: dict[str, Any],
    card: dict[str, Any],
    observations: list[dict[str, Any]],
    manifest: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    for field in IDENTITY_FIELDS:
        expected = manifest.get(field)
        if audit.get(field) != expected:
            errors.append(f"audit {field} differs from manifest")
        if language.get(field) != expected:
            errors.append(f"language record {field} differs from manifest")
        if models.get(field) != expected:
            errors.append(f"model record {field} differs from manifest")
        if card.get(field) != expected:
            errors.append(f"paper card {field} differs from manifest")
    source_hash = manifest.get("sha256")
    if audit.get("source_sha256") != source_hash:
        errors.append("audit source_sha256 differs from manifest")
    if language.get("source_sha256") != source_hash:
        errors.append("language source_sha256 differs from manifest")
    if models.get("source_sha256") != source_hash:
        errors.append("model source_sha256 differs from manifest")
    source = card.get("source")
    if not isinstance(source, dict):
        errors.append("paper card source must be an object")
        source = {}
    if source.get("sha256") != source_hash:
        errors.append("paper card source sha256 differs from manifest")
    if source.get("page_count") != manifest.get("page_count"):
        errors.append("paper card source page_count differs from manifest")
    page_count = manifest.get("page_count")
    for index, observation in enumerate(observations, start=1):
        for field in IDENTITY_FIELDS:
            if observation.get(field) != manifest.get(field):
                errors.append(f"observation[{index}] {field} differs from manifest")
        page = observation.get("page")
        if not isinstance(page, int) or page < 1:
            errors.append(f"observation[{index}] has invalid page")
        elif isinstance(page_count, int) and page > page_count:
            errors.append(f"observation[{index}] page exceeds manifest page_count")
    return errors


def validate_artifact_versions(
    audit: dict[str, Any],
    language: dict[str, Any],
    models: dict[str, Any],
    card: dict[str, Any],
    manifest: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    if audit.get("schema_version") != 1:
        errors.append("audit schema_version must be 1")
    if audit.get("review_status") != "validated":
        errors.append("audit review_status must be validated")
    if audit.get("priority_order") != PRIORITY_ORDER:
        errors.append("audit priority_order must be language-imitation, organization-logic, formula-error-watch")
    if language.get("schema_version") != 3:
        errors.append("language schema_version must be 3")
    if language.get("review_status") != "validated":
        errors.append("language review_status must be validated")
    if models.get("schema_version") != 2:
        errors.append("model schema_version must be 2")
    if models.get("review_status") != "validated":
        errors.append("model review_status must be validated")
    if card.get("review_status") != "validated":
        errors.append("paper card review_status must be validated")
    if manifest.get("eligible_paper") is not True:
        errors.append("manifest record must be an eligible paper")
    if not isinstance(manifest.get("page_count"), int) or manifest["page_count"] < 1:
        errors.append("manifest page_count must be a positive integer")
    return errors


def validate_card_declarations(
    card: dict[str, Any],
    language: dict[str, Any],
    models: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    declarations = card.get("protocol_v2_records")
    if not isinstance(declarations, dict):
        return ["paper card requires protocol_v2_records"]
    language_declaration = declarations.get("language")
    if not isinstance(language_declaration, dict):
        errors.append("paper card requires language declaration")
    else:
        comparisons = {
            "schema_version": language.get("schema_version"),
            "unit_count": len(language.get("units", []))
            if isinstance(language.get("units"), list)
            else None,
            "chapters": language.get("available_chapters"),
            "review_status": language.get("review_status"),
        }
        for field, expected in comparisons.items():
            if language_declaration.get(field) != expected:
                errors.append(f"paper card language {field} differs from language record")
    model_declaration = declarations.get("models")
    model_units = object_list(models.get("models"))
    equations = [
        equation
        for model in model_units
        for equation in object_list(model.get("governing_equations"))
    ]
    if not isinstance(model_declaration, dict):
        errors.append("paper card requires model declaration")
    else:
        comparisons = {
            "model_count": len(model_units),
            "equation_count": len(equations),
            "review_status": models.get("review_status"),
        }
        for field, expected in comparisons.items():
            if model_declaration.get(field) != expected:
                errors.append(f"paper card model {field} differs from model record")
    return errors


def language_indexes(
    language: dict[str, Any],
) -> tuple[list[str], dict[str, dict[str, Any]], dict[str, dict[str, Any]], list[str]]:
    errors: list[str] = []
    chapters_value = language.get("available_chapters")
    chapters = (
        [chapter for chapter in chapters_value if isinstance(chapter, str)]
        if isinstance(chapters_value, list)
        else []
    )
    if not chapters or len(chapters) != len(set(chapters)):
        errors.append("language available_chapters must be a nonempty unique string array")
    units: dict[str, dict[str, Any]] = {}
    for index, unit in enumerate(object_list(language.get("units")), start=1):
        unit_id = unit.get("language_unit_id")
        if not nonempty_string(unit_id):
            errors.append(f"language unit[{index}] has invalid language_unit_id")
            continue
        if unit_id in units:
            errors.append(f"language record has duplicate language_unit_id {unit_id}")
        units[unit_id] = unit
        if unit.get("chapter") not in chapters:
            errors.append(f"language unit {unit_id} has undeclared chapter")
    if len(object_list(language.get("units"))) != len(language.get("units", [])):
        errors.append("language units must be objects")
    layouts: dict[str, dict[str, Any]] = {}
    for index, layout in enumerate(object_list(language.get("chapter_layouts")), start=1):
        chapter = layout.get("chapter")
        if not nonempty_string(chapter):
            errors.append(f"chapter layout[{index}] has invalid chapter")
            continue
        if chapter in layouts:
            errors.append(f"language record has duplicate chapter layout {chapter}")
        layouts[chapter] = layout
        if not isinstance(layout.get("paragraph_count"), int) or layout["paragraph_count"] < 1:
            errors.append(f"chapter layout {chapter} has invalid paragraph_count")
    if set(layouts) != set(chapters):
        errors.append("language chapter layout chapters differ from available_chapters")
    return chapters, units, layouts, errors


def validate_chapter_saturation(
    audit: dict[str, Any], chapters: list[str]
) -> list[str]:
    errors: list[str] = []
    records = object_list(audit.get("chapter_saturation"))
    raw = audit.get("chapter_saturation")
    if not isinstance(raw, list) or len(records) != len(raw):
        errors.append("chapter_saturation must be an object array")
    names = [record.get("chapter") for record in records]
    duplicates = duplicate_strings(names)
    for chapter in sorted(duplicates):
        errors.append(f"chapter_saturation has duplicate chapter {chapter}")
    if string_set(names) != set(chapters) or len(names) != len(chapters):
        errors.append("chapter_saturation chapters differ from available_chapters")
    for index, record in enumerate(records, start=1):
        label = f"chapter_saturation[{index}]"
        if not isinstance(record.get("pass_count"), int) or record["pass_count"] < 2:
            errors.append(f"{label} pass_count must be at least 2")
        if record.get("last_pass_new_moves") != 0:
            errors.append(f"{label} last_pass_new_moves must be 0")
        if record.get("coverage_status") != "complete":
            errors.append(f"{label} coverage_status must be complete")
        gaps = record.get("gaps")
        if not isinstance(gaps, list) or gaps:
            errors.append(f"{label} gaps must be empty")
    return errors


def validate_language_dispositions(
    audit: dict[str, Any], units: dict[str, dict[str, Any]]
) -> tuple[list[str], int]:
    errors: list[str] = []
    records = object_list(audit.get("language_unit_dispositions"))
    raw = audit.get("language_unit_dispositions")
    if not isinstance(raw, list) or len(records) != len(raw):
        errors.append("language_unit_dispositions must be an object array")
    ids = [record.get("language_unit_id") for record in records]
    for unit_id in sorted(duplicate_strings(ids)):
        errors.append(f"duplicate language_unit_id in dispositions: {unit_id}")
    if string_set(ids) != set(units) or len(ids) != len(units):
        errors.append("language unit dispositions do not exactly cover language units")
    positive_count = 0
    for index, record in enumerate(records, start=1):
        label = f"language_unit_dispositions[{index}]"
        unit_id = record.get("language_unit_id")
        disposition = record.get("disposition")
        targets = record.get("target_pattern_ids")
        reason = record.get("reason")
        if disposition not in DISPOSITIONS:
            errors.append(f"{label} has invalid disposition")
            continue
        if not isinstance(targets, list) or not all(nonempty_string(item) for item in targets):
            errors.append(f"{label} target_pattern_ids must be a string array")
            targets = []
        unit = units.get(unit_id) if isinstance(unit_id, str) else None
        nominated = string_set(unit.get("candidate_pattern_ids")) if unit else set()
        if disposition in {"supports-existing", "opens-candidate"}:
            positive_count += 1
            if not targets:
                errors.append(f"{label} target_pattern_ids must not be empty")
            elif not set(targets).issubset(nominated):
                errors.append(f"{label} target_pattern_ids are not nominated by the language unit")
        else:
            if targets:
                errors.append(f"{label} nonreusable disposition cannot target patterns")
            if not nonempty_string(reason):
                errors.append(f"{label} requires a nonreusable reason")
            elif re.search(
                r"(?:no|missing|without|not yet).{0,40}(?:catalog|pattern(?: id)?|corroborat)",
                reason,
                flags=re.IGNORECASE,
            ):
                errors.append(
                    f"{label} cannot call a unit nonreusable merely because a catalog or pattern ID is absent"
                )
    return errors, positive_count


def validate_paragraph_chains(
    audit: dict[str, Any],
    chapters: list[str],
    layouts: dict[str, dict[str, Any]],
    units: dict[str, dict[str, Any]],
) -> list[str]:
    errors: list[str] = []
    records = object_list(audit.get("paragraph_chains"))
    raw = audit.get("paragraph_chains")
    if not isinstance(raw, list) or len(records) != len(raw):
        errors.append("paragraph_chains must be an object array")
    expected = {chapter for chapter in ("abstract", "introduction") if chapter in chapters}
    names = [record.get("chapter") for record in records]
    for chapter in sorted(duplicate_strings(names)):
        errors.append(f"paragraph_chains has duplicate chapter {chapter}")
    if string_set(names) != expected or len(names) != len(expected):
        errors.append("paragraph_chains must exactly cover available Abstract and Introduction")
    for record in records:
        chapter = record.get("chapter")
        if not isinstance(chapter, str):
            continue
        label = f"paragraph_chains[{chapter}]"
        layout = layouts.get(chapter, {})
        layout_count = layout.get("paragraph_count")
        visual_count = record.get("visual_paragraph_count")
        paragraphs = object_list(record.get("paragraphs"))
        raw_paragraphs = record.get("paragraphs")
        if visual_count != layout_count:
            errors.append(f"{label} visual paragraph count differs from layout paragraph_count")
        if not isinstance(raw_paragraphs, list) or len(paragraphs) != len(raw_paragraphs):
            errors.append(f"{label} paragraphs must be an object array")
        if len(paragraphs) != layout_count:
            errors.append(f"{label} paragraph chain count differs from layout paragraph_count")
        indices = [paragraph.get("paragraph_index") for paragraph in paragraphs]
        if indices != list(range(1, len(paragraphs) + 1)):
            errors.append(f"{label} paragraph indices must be consecutive from 1")
        if record.get("coverage_status") != "complete":
            errors.append(f"{label} coverage_status must be complete")
        gaps = record.get("gaps")
        if not isinstance(gaps, list) or gaps:
            errors.append(f"{label} gaps must be empty")
        for paragraph in paragraphs:
            if not nonempty_string(paragraph.get("dominant_move")):
                errors.append(f"{label} paragraph requires dominant_move")
            unit_ids = paragraph.get("language_unit_ids")
            if not nonempty_string_list(unit_ids):
                errors.append(f"{label} paragraph requires language_unit_ids")
                continue
            for unit_id in unit_ids:
                unit = units.get(unit_id)
                if unit is None:
                    errors.append(f"{label} paragraph references unknown language unit {unit_id}")
                elif unit.get("chapter") != chapter:
                    errors.append(f"{label} paragraph language unit chapter differs: {unit_id}")
    return errors


def validate_organization_logic(
    audit: dict[str, Any], card: dict[str, Any], chapters: list[str], page_count: int | None
) -> list[str]:
    errors: list[str] = []
    logic = audit.get("organization_logic")
    if not isinstance(logic, dict):
        return ["organization_logic must be an object"]
    if logic.get("positive_artifacts_status") != "complete":
        errors.append("organization_logic positive_artifacts_status must be complete")
    if logic.get("weakness_substitution_allowed") is not False:
        errors.append("organization_logic weakness substitution must be false")
    if not nonempty_string_list(logic.get("global_organization_chain")):
        errors.append("organization_logic requires a global organization chain")
    progressions = object_list(logic.get("section_progressions"))
    if not progressions:
        errors.append("organization_logic requires section progression artifacts")
    progression_chapters = [progression.get("chapter") for progression in progressions]
    for chapter in sorted(duplicate_strings(progression_chapters)):
        errors.append(f"organization_logic has duplicate section progression {chapter}")
    if (
        string_set(progression_chapters) != set(chapters)
        or len(progression_chapters) != len(chapters)
    ):
        errors.append("organization_logic section progressions must exactly cover available chapters")
    for index, progression in enumerate(progressions, start=1):
        if progression.get("chapter") not in chapters:
            errors.append(f"section_progressions[{index}] has undeclared chapter")
        moves = progression.get("moves")
        if not nonempty_string_list(moves):
            errors.append(f"section_progressions[{index}] requires moves")
        else:
            normalized_moves = [move.strip().lower() for move in moves]
            if len(normalized_moves) != len(SECTION_CONTRACT_PREFIXES):
                errors.append(
                    f"section_progressions[{index}] must encode exactly five section-contract moves"
                )
            for prefix in SECTION_CONTRACT_PREFIXES:
                matches = [move for move in normalized_moves if move.startswith(prefix)]
                if len(matches) != 1 or not matches[0][len(prefix):].strip():
                    errors.append(
                        f"section_progressions[{index}] requires one nonempty {prefix[:-1]} move"
                    )
        if not nonempty_string(progression.get("positive_pattern")):
            errors.append(f"section_progressions[{index}] requires positive_pattern")
    chains = object_list(logic.get("main_argument_chains"))
    if not chains:
        errors.append("organization_logic requires main argument chains")
    for index, chain in enumerate(chains, start=1):
        if not nonempty_string(chain.get("claim")):
            errors.append(f"main_argument_chains[{index}] requires claim")
        if not nonempty_string_list(chain.get("support_steps")):
            errors.append(f"main_argument_chains[{index}] requires support_steps")
        if not nonempty_string(chain.get("decision_consequence")):
            errors.append(f"main_argument_chains[{index}] requires decision_consequence")
        pages = chain.get("source_pages")
        if not isinstance(pages, list) or not pages:
            errors.append(f"main_argument_chains[{index}] requires source_pages")
        elif not all(
            isinstance(page, int)
            and page >= 1
            and (page_count is None or page <= page_count)
            for page in pages
        ):
            errors.append(f"main_argument_chains[{index}] has invalid source_pages")
    if not object_list(card.get("writing_logic")):
        errors.append("paper card writing_logic requires a positive organization artifact")
    return errors


def model_indexes(
    models: dict[str, Any]
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, set[str]],
    list[str],
]:
    errors: list[str] = []
    model_index: dict[str, dict[str, Any]] = {}
    equation_index: dict[str, dict[str, Any]] = {}
    equations_by_model: dict[str, set[str]] = {}
    for index, model in enumerate(object_list(models.get("models")), start=1):
        model_id = model.get("model_id")
        if not nonempty_string(model_id):
            errors.append(f"model[{index}] has invalid model_id")
            continue
        if model_id in model_index:
            errors.append(f"duplicate model_id {model_id}")
        model_index[model_id] = model
        model_equations: set[str] = set()
        for equation in object_list(model.get("governing_equations")):
            equation_id = equation.get("equation_id")
            if not nonempty_string(equation_id):
                errors.append(f"model {model_id} has invalid equation_id")
                continue
            if equation_id in equation_index:
                errors.append(f"duplicate equation_id {equation_id}")
            equation_index[equation_id] = equation
            model_equations.add(equation_id)
        equations_by_model[model_id] = model_equations
    return model_index, equation_index, equations_by_model, errors


def validate_model_retention_and_formula_watch(
    audit: dict[str, Any],
    models: dict[str, Any],
    page_count: int | None,
) -> list[str]:
    model_index, equation_index, equations_by_model, errors = model_indexes(models)
    retention = audit.get("model_retention")
    if not isinstance(retention, dict):
        return [*errors, "model_retention must be an object"]
    if retention.get("model_count") != len(model_index):
        errors.append("model_retention model_count differs from model record")
    retained_models = string_set(retention.get("retained_model_ids"))
    if retained_models != set(model_index) or len(retention.get("retained_model_ids", [])) != len(model_index):
        errors.append("model_retention retained_model_ids do not exactly match model record")
    retained_equations = string_set(retention.get("retained_equation_ids"))
    if retained_equations != set(equation_index) or len(retention.get("retained_equation_ids", [])) != len(equation_index):
        errors.append("model_retention retained_equation_ids do not exactly match model record")
    central_records = object_list(retention.get("central_equations"))
    central_models = [record.get("model_id") for record in central_records]
    expected_central_models = {
        model_id for model_id, equation_ids in equations_by_model.items() if equation_ids
    }
    if string_set(central_models) != expected_central_models or len(central_models) != len(expected_central_models):
        errors.append("model_retention central equation coverage differs from equation-bearing models")
    for model_id in sorted(duplicate_strings(central_models)):
        errors.append(f"model_retention duplicate central equation model {model_id}")
    for index, record in enumerate(central_records, start=1):
        label = f"central_equations[{index}]"
        model_id = record.get("model_id")
        equation_ids = string_set(record.get("equation_ids"))
        if not equation_ids:
            errors.append(f"{label} requires central equation_ids")
        elif isinstance(model_id, str) and not equation_ids.issubset(
            equations_by_model.get(model_id, set())
        ):
            errors.append(f"{label} references equations outside its model")
        if not equation_ids.issubset(retained_equations):
            errors.append(f"{label} central equations are not all retained")
        if record.get("all_central_equations_retained") is not True:
            errors.append(f"{label} all_central_equations_retained must be true")

    formula_watch = audit.get("formula_error_watch")
    if not isinstance(formula_watch, dict):
        return [*errors, "formula_error_watch must be an object"]
    if formula_watch.get("mode") != "last-pass-warning-only":
        errors.append("formula_error_watch mode must be last-pass-warning-only")
    if formula_watch.get("completed_after_positive_passes") is not True:
        errors.append("formula_error_watch completed_after_positive_passes must be true")
    warnings = formula_watch.get("warnings")
    if not isinstance(warnings, list):
        errors.append("formula_error_watch warnings must be an array")
        warnings = []
    for index, warning in enumerate(warnings, start=1):
        label = f"formula_error_watch warnings[{index}]"
        if not isinstance(warning, dict):
            errors.append(f"{label} must be an object")
            continue
        model_id = warning.get("model_id")
        equation_id = warning.get("equation_id")
        if model_id not in model_index:
            errors.append(f"{label} formula warning model_id is unknown")
        if equation_id not in equation_index:
            errors.append(f"{label} formula warning equation_id is unknown")
        elif isinstance(model_id, str) and equation_id not in equations_by_model.get(model_id, set()):
            errors.append(f"{label} formula warning equation_id does not belong to model_id")
        page = warning.get("page")
        if not isinstance(page, int) or page < 1 or (
            page_count is not None and page > page_count
        ):
            errors.append(f"{label} has invalid page")
        if not nonempty_string(warning.get("warning")):
            errors.append(f"{label} requires warning text")
    return errors


def validate_visualizations(audit: dict[str, Any], card: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    visuals = card.get("visualization_observations")
    if not isinstance(visuals, list) or not all(isinstance(item, dict) for item in visuals):
        return ["paper card visualization_observations must be an object array"]
    records = object_list(audit.get("visualization_dispositions"))
    raw = audit.get("visualization_dispositions")
    if not isinstance(raw, list) or len(records) != len(raw):
        errors.append("visualization_dispositions must be an object array")
    indices = [record.get("paper_card_visual_index") for record in records]
    if set(indices) != set(range(1, len(visuals) + 1)) or len(indices) != len(visuals):
        errors.append("visualization dispositions do not exactly cover paper card visualizations")
    valid_ids: list[Any] = []
    for index, record in enumerate(records, start=1):
        if record.get("disposition") != "important-visual-record":
            errors.append(f"visualization_dispositions[{index}] must be an important visual record")
        if not nonempty_string(record.get("visual_record_id")):
            errors.append(f"visualization_dispositions[{index}] requires visual_record_id")
        else:
            valid_ids.append(record["visual_record_id"])
        if not nonempty_string(record.get("analytical_purpose")):
            errors.append(f"visualization_dispositions[{index}] requires analytical_purpose")
    for visual_id in sorted(duplicate_strings(valid_ids)):
        errors.append(f"duplicate visual_record_id {visual_id}")
    return errors


def validate_dimension_counts(
    audit: dict[str, Any], observations: list[dict[str, Any]], positive_count: int
) -> list[str]:
    errors: list[str] = []
    actual = Counter()
    for index, observation in enumerate(observations, start=1):
        dimension = observation.get("dimension")
        if dimension not in DIMENSIONS:
            errors.append(f"observation[{index}] has invalid dimension")
        else:
            actual[dimension] += 1
    expected = {dimension: actual[dimension] for dimension in DIMENSIONS}
    declared = audit.get("dimension_counts")
    if not isinstance(declared, dict) or set(declared) != DIMENSIONS:
        errors.append("audit dimension_counts must contain the exact dimension fields")
    elif declared != expected:
        errors.append(f"audit dimension_counts differ from observations ({declared} != {expected})")
    weakness_count = actual["weakness"]
    if audit.get("positive_reusable_language_count") != positive_count:
        errors.append("positive_reusable_language_count differs from reusable dispositions")
    if audit.get("weakness_record_count") != weakness_count:
        errors.append("weakness_record_count differs from weakness observations")
    if positive_count <= weakness_count:
        errors.append("positive reusable language must exceed weakness records")
    return errors


def validate_audit(
    audit: Any,
    language: Any,
    models: Any,
    card: Any,
    observations: Any,
    manifest: Any,
) -> list[str]:
    if not isinstance(audit, dict):
        return ["audit must be an object"]
    if not isinstance(language, dict):
        return ["language record must be an object"]
    if not isinstance(models, dict):
        return ["model record must be an object"]
    if not isinstance(card, dict):
        return ["paper card must be an object"]
    if not isinstance(observations, list) or not all(
        isinstance(item, dict) for item in observations
    ):
        return ["observations must be an object array"]
    if not isinstance(manifest, dict):
        return ["manifest record must be an object"]

    errors: list[str] = []
    errors.extend(validate_artifact_versions(audit, language, models, card, manifest))
    errors.extend(validate_identity(audit, language, models, card, observations, manifest))
    errors.extend(validate_card_declarations(card, language, models))
    chapters, units, layouts, index_errors = language_indexes(language)
    errors.extend(index_errors)
    errors.extend(validate_chapter_saturation(audit, chapters))
    disposition_errors, positive_count = validate_language_dispositions(audit, units)
    errors.extend(disposition_errors)
    errors.extend(validate_paragraph_chains(audit, chapters, layouts, units))
    page_count = manifest.get("page_count") if isinstance(manifest.get("page_count"), int) else None
    errors.extend(validate_organization_logic(audit, card, chapters, page_count))
    errors.extend(validate_model_retention_and_formula_watch(audit, models, page_count))
    errors.extend(validate_visualizations(audit, card))
    errors.extend(validate_dimension_counts(audit, observations, positive_count))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--language-record", type=Path, required=True)
    parser.add_argument("--model-record", type=Path, required=True)
    parser.add_argument("--paper-card", type=Path, required=True)
    parser.add_argument("--observations", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        audit = load_json(args.audit)
        language = load_json(args.language_record)
        models = load_json(args.model_record)
        card = load_json(args.paper_card)
        observations = load_jsonl(args.observations)
        manifest = find_manifest_record(args.manifest, audit.get("paper_id", ""))
        errors = validate_audit(
            audit, language, models, card, observations, manifest
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors = [str(error)]
        audit = {}
        observations = []
    report = {
        "audit": str(args.audit),
        "error_count": len(errors),
        "errors": errors,
        "observation_count": len(observations),
        "paper_id": audit.get("paper_id"),
        "status": "pass" if not errors else "fail",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
