#!/usr/bin/env python3
"""Validate per-paper protocol v2 language units."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PROBLEM_TYPES = set("ABCDEF")
CHAPTERS = {
    "title",
    "abstract",
    "introduction",
    "problem-restatement",
    "problem-analysis",
    "assumptions",
    "notation",
    "data-preprocessing",
    "model-establishment",
    "model-improvement",
    "algorithm",
    "results",
    "sensitivity-analysis",
    "robustness-verification",
    "error-analysis",
    "sensitivity-robustness",
    "strengths",
    "limitations",
    "future-improvements",
    "strengths-limitations",
    "memo",
    "conclusion",
    "references",
    "appendix",
}
GRANULARITY = {"word", "phrase", "sentence", "paragraph", "section"}
REVIEW_STATUS = {"draft", "source-checked", "validated"}
FEATURE_FIELDS = {
    "voice",
    "tense",
    "modality",
    "clause_structure",
    "quantitative_role",
    "transition",
}
CONTENT_COUNT_FIELDS = {
    "equations",
    "figures",
    "tables",
    "citations",
    "quantitative_results",
}
MOVE_TYPE_FIELDS = {"opening", "transition", "closing"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(nonempty_string(item) for item in value)
    )


def validate_unit(
    unit: Any,
    problem_type: str,
    page_count: int | None,
    known_pattern_ids: set[str] | None,
    index: int,
) -> list[str]:
    label = f"units[{index}]"
    if not isinstance(unit, dict):
        return [f"{label} must be an object"]
    errors: list[str] = []
    unit_id = unit.get("language_unit_id")
    if not nonempty_string(unit_id) or not re.fullmatch(
        rf"LU-{re.escape(problem_type)}-[A-Za-z0-9-]+", unit_id
    ):
        errors.append(f"{label} has invalid language_unit_id")
    page = unit.get("page")
    if not isinstance(page, int) or page < 1:
        errors.append(f"{label} has invalid page")
    elif page_count is not None and page > page_count:
        errors.append(f"{label} page exceeds source page_count")
    if not nonempty_string(unit.get("section")):
        errors.append(f"{label} has empty section")
    if unit.get("chapter") not in CHAPTERS:
        errors.append(f"{label} has invalid chapter")
    if unit.get("granularity") not in GRANULARITY:
        errors.append(f"{label} has invalid granularity")
    excerpt = unit.get("source_excerpt")
    if not nonempty_string(excerpt):
        errors.append(f"{label} has empty source_excerpt")
    elif len(excerpt) > 500:
        errors.append(f"{label} excerpt exceeds 500 characters")
    for field in ("function", "rhetorical_move", "reusable_pattern"):
        if not nonempty_string(unit.get(field)):
            errors.append(f"{label} has empty {field}")
    for field in (
        "information_order",
        "reusable_elements",
        "prohibited_generalizations",
    ):
        if not nonempty_string_list(unit.get(field)):
            errors.append(f"{label} requires {field}")

    features = unit.get("features")
    if not isinstance(features, dict):
        errors.append(f"{label} requires features")
    else:
        missing = sorted(FEATURE_FIELDS - set(features))
        if missing:
            errors.append(f"{label} missing feature fields: {', '.join(missing)}")
        for field in FEATURE_FIELDS & set(features):
            if not nonempty_string(features[field]):
                errors.append(f"{label} has empty feature {field}")

    candidate_ids = unit.get("candidate_pattern_ids")
    if not isinstance(candidate_ids, list) or not all(
        nonempty_string(pattern_id) for pattern_id in candidate_ids
    ):
        errors.append(f"{label} candidate_pattern_ids must be a string array")
    elif known_pattern_ids is not None:
        unknown = sorted(set(candidate_ids) - known_pattern_ids)
        if unknown:
            errors.append(f"{label} references unknown pattern: {', '.join(unknown)}")
    return errors


def validate_chapter_layout(
    layout: Any,
    page_count: int | None,
    index: int,
) -> list[str]:
    label = f"chapter_layouts[{index}]"
    if not isinstance(layout, dict):
        return [f"{label} must be an object"]
    errors: list[str] = []
    chapter = layout.get("chapter")
    if chapter not in CHAPTERS:
        errors.append(f"{label} has invalid chapter")
    page_start = layout.get("page_start")
    page_end = layout.get("page_end")
    if not isinstance(page_start, int) or page_start < 1:
        errors.append(f"{label} has invalid page_start")
    if not isinstance(page_end, int) or page_end < 1:
        errors.append(f"{label} has invalid page_end")
    if isinstance(page_start, int) and isinstance(page_end, int):
        if page_start > page_end:
            errors.append(f"{label} page_start exceeds page_end")
        if page_count is not None and page_end > page_count:
            errors.append(f"{label} page_end exceeds source page_count")
    page_fraction = layout.get("page_fraction")
    if not isinstance(page_fraction, (int, float)) or not 0 < page_fraction <= 1:
        errors.append(f"{label} has invalid page_fraction")
    for field in ("word_count", "sentence_count", "paragraph_count"):
        value = layout.get(field)
        if not isinstance(value, int) or value < 1:
            errors.append(f"{label} has invalid {field}")

    sentence_words = layout.get("sentence_words")
    if not isinstance(sentence_words, dict):
        errors.append(f"{label} requires sentence_words")
    else:
        values = [sentence_words.get(field) for field in ("minimum", "median", "maximum")]
        if not all(isinstance(value, (int, float)) and value > 0 for value in values):
            errors.append(f"{label} has invalid sentence_words")
        elif not values[0] <= values[1] <= values[2]:
            errors.append(f"{label} sentence_words are not ordered")

    paragraph_functions = layout.get("paragraph_functions")
    if not nonempty_string_list(paragraph_functions):
        errors.append(f"{label} requires paragraph_functions")
    elif isinstance(layout.get("paragraph_count"), int) and len(paragraph_functions) != layout["paragraph_count"]:
        errors.append(f"{label} paragraph_functions count differs from paragraph_count")

    proportions = layout.get("rhetorical_proportions")
    if not isinstance(proportions, dict) or not proportions:
        errors.append(f"{label} requires rhetorical_proportions")
    elif not all(
        nonempty_string(key)
        and isinstance(value, (int, float))
        and 0 <= value <= 1
        for key, value in proportions.items()
    ):
        errors.append(f"{label} has invalid rhetorical_proportions")
    elif abs(sum(proportions.values()) - 1.0) > 1e-6:
        errors.append(f"{label} rhetorical_proportions must sum to 1")

    content_counts = layout.get("content_counts")
    if not isinstance(content_counts, dict) or set(content_counts) != CONTENT_COUNT_FIELDS:
        errors.append(f"{label} requires exact content_counts fields")
    elif not all(isinstance(value, int) and value >= 0 for value in content_counts.values()):
        errors.append(f"{label} has invalid content_counts")

    move_types = layout.get("move_types")
    if not isinstance(move_types, dict) or set(move_types) != MOVE_TYPE_FIELDS:
        errors.append(f"{label} requires exact move_types fields")
    else:
        for field in MOVE_TYPE_FIELDS:
            if not nonempty_string_list(move_types.get(field)):
                errors.append(f"{label} requires move_types.{field}")
    if not nonempty_string(layout.get("counting_method")):
        errors.append(f"{label} requires counting_method")
    ambiguities = layout.get("ambiguities")
    if not isinstance(ambiguities, list) or not all(nonempty_string(item) for item in ambiguities):
        errors.append(f"{label} ambiguities must be a string array")
    return errors


def validate_record(
    record: Any,
    known_pattern_ids: set[str] | None = None,
    manifest_record: dict[str, Any] | None = None,
) -> list[str]:
    if not isinstance(record, dict):
        return ["record must be an object"]
    errors: list[str] = []
    schema_version = record.get("schema_version")
    if schema_version not in {2, 3}:
        errors.append("schema_version must be 2 or 3")
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

    chapters = record.get("available_chapters")
    if not nonempty_string_list(chapters) or any(chapter not in CHAPTERS for chapter in chapters):
        errors.append("available_chapters must contain valid chapter labels")
        chapters = []
    units = record.get("units")
    unit_ids: set[str] = set()
    covered_chapters: set[str] = set()
    if not isinstance(units, list) or not units:
        errors.append("units must contain at least one language unit")
        units = []
    for index, unit in enumerate(units, start=1):
        errors.extend(
            validate_unit(unit, problem_type, page_count, known_pattern_ids, index)
        )
        if isinstance(unit, dict):
            unit_id = unit.get("language_unit_id")
            if isinstance(unit_id, str):
                if unit_id in unit_ids:
                    errors.append(f"duplicate language_unit_id {unit_id}")
                unit_ids.add(unit_id)
            chapter = unit.get("chapter")
            if isinstance(chapter, str):
                covered_chapters.add(chapter)
    for chapter in chapters:
        if chapter not in covered_chapters:
            errors.append(f"available chapter {chapter} has no language unit")

    layouts = record.get("chapter_layouts")
    layout_chapters: set[str] = set()
    if schema_version == 3 and (not isinstance(layouts, list) or not layouts):
        errors.append("chapter_layouts must contain at least one quantitative layout")
        layouts = []
    elif layouts is None:
        layouts = []
    elif not isinstance(layouts, list):
        errors.append("chapter_layouts must be an array")
        layouts = []
    for index, layout in enumerate(layouts, start=1):
        errors.extend(validate_chapter_layout(layout, page_count, index))
        if isinstance(layout, dict) and isinstance(layout.get("chapter"), str):
            chapter = layout["chapter"]
            if chapter in layout_chapters:
                errors.append(f"duplicate chapter layout {chapter}")
            layout_chapters.add(chapter)
    if schema_version == 3:
        for chapter in chapters:
            if chapter not in layout_chapters:
                errors.append(f"available chapter {chapter} has no quantitative layout")
    for chapter in layout_chapters - set(chapters):
        errors.append(f"chapter layout {chapter} is not declared available")
    return errors


def load_pattern_ids(path: Path | None) -> set[str] | None:
    if path is None:
        return None
    catalog = load_json(path)
    templates = catalog.get("templates", [])
    return {
        template["pattern_id"]
        for template in templates
        if isinstance(template, dict) and nonempty_string(template.get("pattern_id"))
    }


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
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        record = load_json(args.record)
        pattern_ids = load_pattern_ids(args.catalog)
        manifest_record = (
            find_manifest_record(args.manifest, record.get("paper_id", ""))
            if args.manifest
            else None
        )
        errors = validate_record(record, pattern_ids, manifest_record)
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
