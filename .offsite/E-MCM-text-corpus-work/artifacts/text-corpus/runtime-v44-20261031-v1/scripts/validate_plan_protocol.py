#!/usr/bin/env python3
"""Fail when plan.md drifts from the language-first execution contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = (
    "### Mandatory Intellectual Priority and Execution Order",
    "### Non-Negotiable Interpretation and Dual-Axis Gate",
    "### 8.3 Gate G1 - Summary/Abstract and Introduction First",
    "### 8.4 Gate G2 - Chapter-by-Chapter Positive Language Saturation",
    "### 8.5 Gate G3 - High-Frequency and Patterned Expression Mining",
    "### 8.7 Gate G4 - Reconstruct the Authors' Observable Article Organization",
    "#### Organization skeleton test",
    "### 8.9 Gate G5 - Formula-Level Model, Data, Assumption, and Algorithm Retention",
    "### 8.11 Gate G6 - Important Visualization Retention",
    "### 8.12 Gate G7 - Last-Pass Formula, Fact, Notation, and Claim Warnings",
    "language must be **strictly greater** than every other single evidence dimension",
    "Occurrence, function, information order, slots, variants, and boundary",
    "input`, `rhetorical job`, `analytical job`, `output`, and `handoff`",
    "## GSTACK REVIEW REPORT",
)

BANNED = (
    "Step 7 - Reconstruct Every Core Model",
    "Step 13 - Mine Language",
    "Deep modeling reconstruction.",
    "Language/logic/visual mining.",
)

ORDERED = (
    "Gate G1",
    "Gate G2",
    "Gate G3",
    "Gate G4",
    "Gate G5",
    "Gate G6",
    "Gate G7",
)


def validate_text(text: str) -> list[str]:
    errors: list[str] = []
    for required in REQUIRED:
        if required not in text:
            errors.append(f"missing required plan contract: {required}")
    for banned in BANNED:
        if banned in text:
            errors.append(f"banned legacy workflow remains: {banned}")
    positions = [text.find(label) for label in ORDERED]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append("G1-G7 gate order is missing or reversed")
    if text.count("## GSTACK REVIEW REPORT") != 1:
        errors.append("GSTACK REVIEW REPORT must appear exactly once")
    h2_headings = [line for line in text.splitlines() if line.startswith("## ")]
    if not h2_headings or h2_headings[-1] != "## GSTACK REVIEW REPORT":
        errors.append("GSTACK REVIEW REPORT must be the last H2 section")
    if sum(line.startswith("```") for line in text.splitlines()) % 2:
        errors.append("markdown code fences are unbalanced")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        errors = validate_text(args.plan.read_text(encoding="utf-8"))
    except OSError as error:
        errors = [str(error)]
    report = {
        "status": "pass" if not errors else "fail",
        "error_count": len(errors),
        "errors": errors,
        "plan": str(args.plan),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
