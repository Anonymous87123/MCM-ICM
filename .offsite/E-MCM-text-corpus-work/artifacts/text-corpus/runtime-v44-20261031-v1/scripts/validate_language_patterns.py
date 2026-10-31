#!/usr/bin/env python3
"""Validate an evidence-backed, type-specific language pattern catalog."""

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
    "sensitivity-robustness",
    "strengths-limitations",
    "memo",
    "conclusion",
    "appendix",
}
PATTERN_KINDS = {"sentence-template", "paragraph-chain", "transition", "claim-frame"}
CONFIDENCE = {"high", "medium", "low"}
JUDGE_RELEVANCE = {"direct-evidence", "correlational", "unknown"}
LIFECYCLES = {
    "seed",
    "candidate",
    "corroborated",
    "bounded",
    "operationalized",
    "promoted",
    "challenged",
    "revised",
    "retired",
}


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


def validate_template(
    template: Any,
    catalog_type: str,
    pattern_ids: set[str],
    index: int,
    unit_index: dict[str, dict[str, Any]] | None = None,
    content_ids: dict[str, str] | None = None,
) -> list[str]:
    errors: list[str] = []
    label = f"templates[{index}]"
    if not isinstance(template, dict):
        return [f"{label} must be an object"]

    pattern_id = template.get("pattern_id")
    if not nonempty_string(pattern_id) or not re.fullmatch(r"LP-[A-F]-[A-Z0-9-]+", pattern_id):
        errors.append(f"{label} has invalid pattern_id")
    elif pattern_id in pattern_ids:
        errors.append(f"duplicate pattern_id {pattern_id}")
    else:
        pattern_ids.add(pattern_id)

    if template.get("pattern_kind") not in PATTERN_KINDS:
        errors.append(f"{label} has invalid pattern_kind")
    lifecycle = template.get("lifecycle")
    if lifecycle not in LIFECYCLES:
        errors.append(f"{label} has invalid lifecycle")
    problem_types = template.get("problem_types")
    if not nonempty_string_list(problem_types) or catalog_type not in problem_types:
        errors.append(f"{label} problem_types must include catalog problem_type {catalog_type}")
    elif any(problem_type not in PROBLEM_TYPES for problem_type in problem_types):
        errors.append(f"{label} has invalid problem type")

    chapters = template.get("chapters")
    if not nonempty_string_list(chapters) or any(chapter not in CHAPTERS for chapter in chapters):
        errors.append(f"{label} has invalid or empty chapters")
    for field in ("function", "trigger", "filled_example"):
        if not nonempty_string(template.get(field)):
            errors.append(f"{label} has empty {field}")
    if not nonempty_string_list(template.get("paragraph_moves")):
        errors.append(f"{label} requires paragraph_moves")
    if not nonempty_string_list(template.get("forbidden_uses")):
        errors.append(f"{label} requires forbidden_uses")

    slots = template.get("slots")
    if not isinstance(slots, list) or not slots:
        errors.append(f"{label} requires at least one slot")
    else:
        slot_names: set[str] = set()
        for slot_index, slot in enumerate(slots, start=1):
            if not isinstance(slot, dict):
                errors.append(f"{label}.slots[{slot_index}] must be an object")
                continue
            name = slot.get("name")
            if not nonempty_string(name) or not re.fullmatch(r"[a-z][a-z0-9_]*", name):
                errors.append(f"{label}.slots[{slot_index}] has invalid name")
            elif name in slot_names:
                errors.append(f"{label} has duplicate slot {name}")
            else:
                slot_names.add(name)
            if not isinstance(slot.get("required"), bool):
                errors.append(f"{label}.slots[{slot_index}] requires boolean required")
            if not nonempty_string(slot.get("description")):
                errors.append(f"{label}.slots[{slot_index}] has empty description")

    variants = template.get("variants")
    if not nonempty_string_list(variants) or len(set(variants)) < 2:
        errors.append(f"{label} requires at least two variants")

    evidence = template.get("evidence")
    source_papers: set[str] = set()
    if not isinstance(evidence, list) or len(evidence) < 2:
        errors.append(f"{label} requires evidence from at least two independent papers")
    else:
        for evidence_index, record in enumerate(evidence, start=1):
            evidence_label = f"{label}.evidence[{evidence_index}]"
            if not isinstance(record, dict):
                errors.append(f"{evidence_label} must be an object")
                continue
            language_unit_id = record.get("language_unit_id")
            if not nonempty_string(language_unit_id) or not re.fullmatch(
                r"LU-[A-F]-[A-Za-z0-9-]+", language_unit_id
            ):
                errors.append(f"{evidence_label} has invalid language_unit_id")
            paper_id = record.get("paper_id")
            if not nonempty_string(paper_id) or not paper_id.startswith("P-"):
                errors.append(f"{evidence_label} has invalid paper_id")
            else:
                source_papers.add(paper_id)
            if record.get("problem_type") not in PROBLEM_TYPES:
                errors.append(f"{evidence_label} has invalid problem_type")
            if not isinstance(record.get("page"), int) or record["page"] < 1:
                errors.append(f"{evidence_label} has invalid page")
            if not nonempty_string(record.get("section")):
                errors.append(f"{evidence_label} has empty section")
            excerpt = record.get("excerpt")
            if not nonempty_string(excerpt):
                errors.append(f"{evidence_label} has empty excerpt")
            elif len(excerpt) > 500:
                errors.append(f"{evidence_label} excerpt exceeds 500 characters")
            if unit_index is not None and isinstance(language_unit_id, str):
                unit = unit_index.get(language_unit_id)
                if unit is None:
                    errors.append(f"{evidence_label} references unknown language_unit_id")
                else:
                    expected = {
                        "paper_id": paper_id,
                        "problem_type": record.get("problem_type"),
                        "page": record.get("page"),
                    }
                    for field, value in expected.items():
                        if unit.get(field) != value:
                            errors.append(
                                f"{evidence_label} {field} differs from language unit"
                            )
                    unit_excerpt = unit.get("source_excerpt")
                    if (
                        nonempty_string(excerpt)
                        and nonempty_string(unit_excerpt)
                        and excerpt not in unit_excerpt
                        and unit_excerpt not in excerpt
                    ):
                        errors.append(
                            f"{evidence_label} excerpt differs from language unit"
                        )
                    if (
                        lifecycle not in {"seed", "candidate"}
                        and unit.get("review_status") != "validated"
                    ):
                        errors.append(
                            f"{label} lifecycle {lifecycle} requires validated language units"
                        )
    if len(source_papers) < 2:
        errors.append(f"{label} requires evidence from at least two independent papers")
    if content_ids is not None:
        missing_content = sorted(source_papers - set(content_ids))
        if missing_content:
            errors.append(
                f"{label} papers missing manifest content_id: {', '.join(missing_content)}"
            )
        independent_content = {
            content_ids[paper_id]
            for paper_id in source_papers
            if paper_id in content_ids
        }
        if len(independent_content) < 2:
            errors.append(f"{label} requires evidence from independent content entities")
    if template.get("source_count") != len(source_papers):
        errors.append(f"{label} source_count does not match independent papers")
    if template.get("confidence") not in CONFIDENCE:
        errors.append(f"{label} has invalid confidence")

    judge_relevance = template.get("judge_relevance")
    if not isinstance(judge_relevance, dict):
        errors.append(f"{label} requires judge_relevance")
    else:
        if judge_relevance.get("status") not in JUDGE_RELEVANCE:
            errors.append(f"{label} has invalid judge_relevance status")
        if not nonempty_string(judge_relevance.get("basis")):
            errors.append(f"{label} has empty judge_relevance basis")
    return errors


def validate_lexicon(
    lexicon: Any,
    pattern_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    if not isinstance(lexicon, dict):
        return ["lexicon must be an object"]
    requirements = {
        "positive": ("term", "function", "chapters", "use_when", "avoid_when", "example"),
        "negative": ("term", "failure_mode", "replacement_rule", "chapters"),
    }
    for polarity, fields in requirements.items():
        entries = lexicon.get(polarity)
        if not isinstance(entries, list) or not entries:
            errors.append(f"lexicon.{polarity} must contain at least one entry")
            continue
        for index, entry in enumerate(entries, start=1):
            label = f"lexicon.{polarity}[{index}]"
            if not isinstance(entry, dict):
                errors.append(f"{label} must be an object")
                continue
            for field in fields:
                value = entry.get(field)
                if field == "chapters":
                    if not nonempty_string_list(value) or any(
                        chapter not in CHAPTERS for chapter in value
                    ):
                        errors.append(f"{label} has invalid chapters")
                elif not nonempty_string(value):
                    errors.append(f"{label} has empty {field}")
            references = entry.get("evidence_pattern_ids")
            if not nonempty_string_list(references):
                errors.append(f"{label} requires evidence_pattern_ids")
            else:
                unknown = sorted(set(references) - pattern_ids)
                if unknown:
                    errors.append(f"{label} references unknown patterns: {', '.join(unknown)}")
    return errors


def validate_layout_profiles(profiles: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(profiles, list) or not profiles:
        return ["layout_profiles must contain at least one profile"]
    for index, profile in enumerate(profiles, start=1):
        label = f"layout_profiles[{index}]"
        if not isinstance(profile, dict):
            errors.append(f"{label} must be an object")
            continue
        if profile.get("chapter") not in CHAPTERS:
            errors.append(f"{label} has invalid chapter")
        if profile.get("unit") not in {"sentence", "paragraph", "word", "page-fraction"}:
            errors.append(f"{label} has invalid unit")
        if profile.get("measurement_status") not in {"provisional", "validated"}:
            errors.append(f"{label} has invalid measurement_status")
        papers = profile.get("sample_papers")
        unique_papers = set(papers) if nonempty_string_list(papers) else set()
        if len(unique_papers) < 2:
            errors.append(f"{label} requires at least two sample papers")
        if profile.get("sample_size") != len(unique_papers):
            errors.append(f"{label} sample_size does not match unique sample_papers")
        observed_range = profile.get("observed_range")
        if not isinstance(observed_range, dict):
            errors.append(f"{label} requires observed_range")
        else:
            minimum = observed_range.get("minimum")
            maximum = observed_range.get("maximum")
            if not isinstance(minimum, (int, float)) or not isinstance(maximum, (int, float)):
                errors.append(f"{label} observed_range must be numeric")
            elif minimum < 0 or maximum < minimum:
                errors.append(f"{label} observed_range is invalid")
        if not nonempty_string(profile.get("recommended_use")):
            errors.append(f"{label} has empty recommended_use")
    return errors


def validate_catalog(
    catalog: Any,
    unit_index: dict[str, dict[str, Any]] | None = None,
    content_ids: dict[str, str] | None = None,
) -> list[str]:
    if not isinstance(catalog, dict):
        return ["catalog must be an object"]
    errors: list[str] = []
    if catalog.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    if not nonempty_string(catalog.get("catalog_id")):
        errors.append("catalog_id is required")
    catalog_type = catalog.get("problem_type")
    if catalog_type not in PROBLEM_TYPES:
        errors.append("problem_type must be A-F")
        catalog_type = "?"

    templates = catalog.get("templates")
    pattern_ids: set[str] = set()
    if not isinstance(templates, list) or not templates:
        errors.append("templates must contain at least one pattern")
    else:
        for index, template in enumerate(templates, start=1):
            errors.extend(
                validate_template(
                    template,
                    catalog_type,
                    pattern_ids,
                    index,
                    unit_index,
                    content_ids,
                )
            )
    errors.extend(validate_lexicon(catalog.get("lexicon"), pattern_ids))
    errors.extend(validate_layout_profiles(catalog.get("layout_profiles")))
    return errors


def load_language_unit_index(path: Path | None) -> dict[str, dict[str, Any]] | None:
    if path is None:
        return None
    paths = [path] if path.is_file() else sorted(path.glob("*.json"))
    if not paths:
        raise ValueError(f"no language unit records found: {path}")
    index: dict[str, dict[str, Any]] = {}
    for record_path in paths:
        record = load_json(record_path)
        paper_fields = {
            "paper_id": record.get("paper_id"),
            "problem_type": record.get("problem_type"),
            "review_status": record.get("review_status"),
        }
        for unit in record.get("units", []):
            if not isinstance(unit, dict):
                continue
            unit_id = unit.get("language_unit_id")
            if not nonempty_string(unit_id):
                continue
            if unit_id in index:
                raise ValueError(f"duplicate language_unit_id in corpus: {unit_id}")
            index[unit_id] = {**paper_fields, **unit}
    return index


def load_manifest_content_ids(path: Path | None) -> dict[str, str] | None:
    if path is None:
        return None
    result: dict[str, str] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"manifest line {line_number} is not an object")
            paper_id = value.get("paper_id")
            content_id = value.get("content_id")
            if isinstance(paper_id, str) and isinstance(content_id, str):
                result[paper_id] = content_id
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--language-units", type=Path)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        catalog = load_json(args.catalog)
        unit_index = load_language_unit_index(args.language_units)
        content_ids = load_manifest_content_ids(args.manifest)
        errors = validate_catalog(catalog, unit_index, content_ids)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors = [str(error)]
    report = {
        "catalog": str(args.catalog),
        "error_count": len(errors),
        "errors": errors,
        "status": "pass" if not errors else "fail",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
