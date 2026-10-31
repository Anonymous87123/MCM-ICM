"""Complete chapter query families, preserving printed tasks and source order."""
from __future__ import annotations

import re

from text_corpus import PROSE_KINDS, canonical_role, section_blocks, title_role

EXCLUDED_AUTHOR_ROLES={"contents","references","ai_disclosure"}
NON_AUTHOR_KINDS = PROSE_KINDS | EXCLUDED_AUTHOR_ROLES | {"source_object", "caption"}
QUERY_FAMILIES={
    "all_author_text":None,
    "problem_restatement":{"problem_restatement"},
    "problem_analysis":{"problem_analysis"},
    "model_building_and_solution":{"model","results"},
    "sensitivity_validation":{"sensitivity","validation"},
    "improvements_evaluation":{"improvements","discussion","strengths_weaknesses"},
}
TASK_QUERIES={f"task_{number}":number for number in range(1,5)}


def task_numbers(title):
    """Only explicit Task/Problem/Question wording; never chapter numbers alone."""
    convert={"I":1,"II":2,"III":3,"IV":4,"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"一":1,"二":2,"三":3,"四":4}
    found=set()
    for pattern in (r"\b(?:task|problem|question)\s*(?:no\.?\s*)?([1-4]|IV|III|II|I|one|two|three|four)(?![A-Za-z0-9])",
                    r"问题\s*([1-4一二三四])",r"第\s*([1-4一二三四])\s*问"):
        for match in re.finditer(pattern,title,re.I):
            value=match.group(1).upper();found.add(int(value) if value.isdigit() else convert[value])
    return found


def select_sections(document,section,*,exact_title=False):
    role=canonical_role(section)
    if exact_title:
        matches = [s for s in document['sections'] if s['title'].strip().casefold()==section.strip().casefold()]
        # Non-author data remain separately addressable by explicit title/role.
        # Ordinary author-section queries must not inherit nested bibliography,
        # contents or AI reports from the source's imperfect heading hierarchy.
        excluded = set() if matches and all(s['role'] in EXCLUDED_AUTHOR_ROLES for s in matches) else EXCLUDED_AUTHOR_ROLES
        return [s['section_id'] for s in matches],excluded
    if role=="all_author_text":
        return [s["section_id"] for s in document["sections"] if s["role"] not in EXCLUDED_AUTHOR_ROLES],EXCLUDED_AUTHOR_ROLES
    if role in TASK_QUERIES:
        return [s["section_id"] for s in document["sections"] if TASK_QUERIES[role] in task_numbers(s["title"])],EXCLUDED_AUTHOR_ROLES
    roles=QUERY_FAMILIES.get(role,{role})
    return [s["section_id"] for s in document["sections"] if s["role"] in roles or (
        role in {"problem_restatement","problem_analysis","improvements_evaluation"} and
        title_role(s["title"],1) in roles)],set() if role in EXCLUDED_AUTHOR_ROLES else EXCLUDED_AUTHOR_ROLES


def selected_blocks(document,selection):
    ids = selection["section_ids"]
    excluded = set(selection.get("excluded_roles", []))
    by_id = {s["section_id"]: s for s in document["sections"]}
    explicit_non_author = bool(ids) and not excluded and all(
        by_id[sid]["role"] in EXCLUDED_AUTHOR_ROLES for sid in ids)
    return section_blocks(document, ids, excluded_roles=excluded,
                          kinds=NON_AUTHOR_KINDS if explicit_non_author else None)


def section_view_text(document, section_id):
    """One exact chapter ID, sharing reader policy without matching duplicate titles."""
    section = next(s for s in document["sections"] if s["section_id"] == section_id)
    excluded = set() if section["role"] in EXCLUDED_AUTHOR_ROLES else EXCLUDED_AUTHOR_ROLES
    return "\n\n".join(b["text"] for b in selected_blocks(document,
        {"section_ids": [section_id], "excluded_roles": sorted(excluded)}))


def all_author_blocks(document):
    ids,excluded=select_sections(document,"all_author_text")
    return section_blocks(document,ids,excluded_roles=excluded)
