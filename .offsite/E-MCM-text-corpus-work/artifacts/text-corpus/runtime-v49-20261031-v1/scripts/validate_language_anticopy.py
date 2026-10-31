#!/usr/bin/env python3
"""Fail-closed anti-copy checks for original language instantiations."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CONTENT_WORD = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
SOURCE_SPECIFIC_TERMS: set[str] = set()  # loaded per paper via --source-terms


@dataclass(frozen=True)
class SourceProfile:
    words: list[str]
    normalized: str
    unique_shingles: set[tuple[str, ...]]
    terms: set[str]
    positions: dict[str, tuple[int, ...]]


def words(text: str) -> list[str]:
    return [value.lower() for value in CONTENT_WORD.findall(text)]


def unique_shingles(text: str, size: int) -> set[tuple[str, ...]]:
    values = words(text)
    counts = Counter(tuple(values[index:index + size]) for index in range(max(0, len(values) - size + 1)))
    return {shingle for shingle, count in counts.items() if count == 1}


def build_source_profile(source: str, minimum: int) -> SourceProfile:
    source_words = words(source)
    counts = Counter(
        tuple(source_words[index:index + minimum])
        for index in range(max(0, len(source_words) - minimum + 1))
    )
    mutable_positions: dict[str, list[int]] = {}
    for index, word in enumerate(source_words):
        mutable_positions.setdefault(word, []).append(index)
    return SourceProfile(
        words=source_words,
        normalized=" ".join(source_words),
        unique_shingles={shingle for shingle, count in counts.items() if count == 1},
        terms=set(source_words),
        positions={word: tuple(indices) for word, indices in mutable_positions.items()},
    )


def longest_run_from_profile(profile: SourceProfile, right: str) -> int:
    previous: dict[int, int] = {}
    best = 0
    for word in words(right):
        current: dict[int, int] = {}
        for source_index in profile.positions.get(word, ()):
            run = previous.get(source_index - 1, 0) + 1
            current[source_index] = run
            best = max(best, run)
        previous = current
    return best


def longest_run(left: str, right: str) -> int:
    return longest_run_from_profile(build_source_profile(left, 2), right)


def example_texts(unit: dict[str, Any]) -> list[str]:
    features = unit.get("features")
    if not isinstance(features, dict):
        return []
    values = features.get("original_instantiations")
    if not isinstance(values, list):
        return []
    result: list[str] = []
    for value in values:
        if isinstance(value, dict) and isinstance(value.get("text"), str):
            result.append(value["text"])
        elif isinstance(value, str):
            result.append(value)
    return result


def scan_unit_with_profile(
    unit: dict[str, Any],
    profile: SourceProfile,
    minimum: int,
    terms: set[str] | None = None,
) -> dict[str, Any]:
    terms = SOURCE_SPECIFIC_TERMS if terms is None else terms
    examples = example_texts(unit)
    full_clause_matches = sum(
        1 for example in examples if " ".join(words(example)) in profile.normalized
    )
    unique_matches = 0
    longest = 0
    source_fact_leaks = 0
    for example in examples:
        example_words = words(example)
        longest = max(longest, longest_run_from_profile(profile, example))
        unique_matches += sum(
            1
            for index in range(max(0, len(example_words) - minimum + 1))
            if tuple(example_words[index:index + minimum]) in profile.unique_shingles
        )
        if terms & set(example_words) & profile.terms:
            source_fact_leaks += 1
    result = "pass" if examples and len(examples) == 2 and full_clause_matches == 0 and unique_matches == 0 and source_fact_leaks == 0 and longest < minimum else "fail"
    return {
        "language_unit_id": unit.get("language_unit_id"),
        "example_count": len(examples),
        "full_clause_matches": full_clause_matches,
        "unique_content_shingle_matches": unique_matches,
        "source_fact_leaks": source_fact_leaks,
        "maximum_shared_content_run": longest,
        "result": result,
    }


def scan_unit(unit: dict[str, Any], source: str, minimum: int) -> dict[str, Any]:
    return scan_unit_with_profile(
        unit, build_source_profile(source, minimum), minimum, SOURCE_SPECIFIC_TERMS
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--min-content-words", type=int, default=8)
    parser.add_argument("--source-terms", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    errors: list[str] = []
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
        source = args.source.read_text(encoding="utf-8", errors="replace")
        units = record.get("units") if isinstance(record, dict) else None
        if not isinstance(units, list) or not units:
            errors.append("record.units must be a nonempty array")
            units = []
        if args.min_content_words < 2:
            errors.append("--min-content-words must be at least 2")
        profile = build_source_profile(source, args.min_content_words)
        terms = SOURCE_SPECIFIC_TERMS
        if not args.source_terms and isinstance(record, dict):
            own = record.get("source_specific_terms")
            if isinstance(own, list) and all(isinstance(item, str) for item in own):
                terms = {item.lower() for item in own}
        if args.source_terms:
            loaded = json.loads(args.source_terms.read_text(encoding="utf-8"))
            if not isinstance(loaded, list) or not all(
                isinstance(item, str) for item in loaded
            ):
                errors.append("--source-terms must hold a JSON array of strings")
            terms = {item.lower() for item in loaded}
        reports = [
            scan_unit_with_profile(unit, profile, args.min_content_words, terms)
            for unit in units
            if isinstance(unit, dict)
        ]
        failed = [item for item in reports if item["result"] != "pass"]
        if failed:
            errors.append(f"{len(failed)} language units failed anti-copy checks")
        output = {
            "record": str(args.record),
            "source": str(args.source),
            "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "minimum_content_words": args.min_content_words,
            "unit_count": len(reports),
            "failed_unit_ids": [item["language_unit_id"] for item in failed],
            "results": reports,
            "errors": errors,
            "status": "pass" if not errors else "fail",
        }
    except (OSError, ValueError, json.JSONDecodeError) as error:
        output = {"errors": [str(error)], "status": "fail"}
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if output.get("status") == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
