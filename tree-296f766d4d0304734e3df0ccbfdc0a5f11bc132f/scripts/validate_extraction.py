#!/usr/bin/env python3
"""Validate one page-aware paper extraction, including rendered PNG pixels."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageStat


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON is not an object: {path}")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-dir", type=Path, required=True)
    parser.add_argument("--require-visual-review", action="store_true")
    args = parser.parse_args(argv or sys.argv[1:])
    paper_dir = args.paper_dir.resolve()
    errors: list[str] = []

    try:
        metadata = load_json(paper_dir / "extraction.json")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1

    page_count = metadata.get("page_count")
    if not isinstance(page_count, int) or page_count < 1:
        errors.append("invalid page_count")
        page_count = 0

    pages_path = paper_dir / "pages.jsonl"
    page_records: list[dict[str, Any]] = []
    if not pages_path.is_file():
        errors.append("pages.jsonl missing")
    else:
        with pages_path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as error:
                    errors.append(f"pages.jsonl line {line_number}: {error}")
                    continue
                page_records.append(record)
    if len(page_records) != page_count:
        errors.append(f"page record count {len(page_records)} != {page_count}")

    calculated_chars = 0
    calculated_words = 0
    for expected_index, record in enumerate(page_records, start=1):
        if record.get("page_index") != expected_index:
            errors.append(f"page {expected_index}: index mismatch")
        text_relative = record.get("text_file")
        if not isinstance(text_relative, str):
            errors.append(f"page {expected_index}: text_file missing")
            continue
        text_path = paper_dir.joinpath(*text_relative.split("/"))
        if not text_path.is_file():
            errors.append(f"page {expected_index}: text file missing")
            continue
        text = text_path.read_text(encoding="utf-8", errors="replace")
        char_count = len(re.sub(r"\s+", "", text))
        word_count = len(re.findall(r"[A-Za-z0-9]+", text))
        calculated_chars += char_count
        calculated_words += word_count
        if record.get("char_count") != char_count:
            errors.append(f"page {expected_index}: char_count mismatch")
        if record.get("word_count") != word_count:
            errors.append(f"page {expected_index}: word_count mismatch")

    if metadata.get("text_char_count") != calculated_chars:
        errors.append("metadata text_char_count mismatch")
    if metadata.get("text_word_count") != calculated_words:
        errors.append("metadata text_word_count mismatch")

    image_checks: list[dict[str, Any]] = []
    for relative in metadata.get("rendered_files", []):
        image_path = paper_dir.joinpath(*relative.split("/"))
        if not image_path.is_file():
            errors.append(f"rendered file missing: {relative}")
            continue
        try:
            with Image.open(image_path) as image:
                image.verify()
            with Image.open(image_path).convert("L") as grayscale:
                width, height = grayscale.size
                extrema = grayscale.getextrema()
                standard_deviation = ImageStat.Stat(grayscale).stddev[0]
        except (OSError, ValueError) as error:
            errors.append(f"invalid image {relative}: {error}")
            continue
        if width < 100 or height < 100:
            errors.append(f"render too small: {relative}: {width}x{height}")
        if extrema[0] == extrema[1] or standard_deviation < 0.5:
            errors.append(f"render appears blank: {relative}")
        image_checks.append(
            {
                "file": relative,
                "height": height,
                "pixel_stddev": round(standard_deviation, 3),
                "width": width,
            }
        )

    if args.require_visual_review and metadata.get("visual_review_status") not in {
        "sampled",
        "complete",
    }:
        errors.append("visual review is required but not recorded")

    report = {
        "errors": errors,
        "extraction_status": metadata.get("extraction_status"),
        "image_checks": image_checks,
        "page_count": page_count,
        "paper_id": metadata.get("paper_id"),
        "status": "pass" if not errors else "fail",
        "text_char_count": calculated_chars,
        "visual_review_status": metadata.get("visual_review_status"),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
