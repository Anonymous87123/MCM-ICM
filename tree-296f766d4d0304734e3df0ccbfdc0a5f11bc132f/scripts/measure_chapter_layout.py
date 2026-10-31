#!/usr/bin/env python3
"""Measure reproducible chapter-layout drafts from page-aware extracted text."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
from pathlib import Path
from typing import Any


WORD_PATTERN = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")
SENTENCE_PATTERN = re.compile(r"[^.!?]+(?:[.!?]+|$)")


def split_pages(text: str) -> list[str]:
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def extract_segment(pages: list[str], segment: dict[str, Any]) -> str:
    page_start = segment.get("page_start")
    page_end = segment.get("page_end")
    if not isinstance(page_start, int) or not isinstance(page_end, int):
        raise ValueError("segment page_start and page_end must be integers")
    if page_start < 1 or page_end < page_start or page_end > len(pages):
        raise ValueError(
            f"invalid page range {page_start}-{page_end} for {len(pages)} pages"
        )
    text = "\n\n".join(pages[page_start - 1 : page_end])
    start_marker = segment.get("start_marker")
    if start_marker is not None:
        if not isinstance(start_marker, str) or not start_marker:
            raise ValueError("start_marker must be a nonempty string")
        offset = text.find(start_marker)
        if offset < 0:
            raise ValueError(
                f"start_marker {start_marker!r} not found on pages {page_start}-{page_end}"
            )
        if segment.get("include_start_marker", True):
            text = text[offset:]
        else:
            text = text[offset + len(start_marker) :].lstrip(" \t\n")
    end_marker = segment.get("end_marker")
    if end_marker is not None:
        if not isinstance(end_marker, str) or not end_marker:
            raise ValueError("end_marker must be a nonempty string")
        offset = text.find(end_marker)
        if offset < 0:
            raise ValueError(
                f"end_marker {end_marker!r} not found on pages {page_start}-{page_end}"
            )
        text = text[:offset]
    return text.strip()


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"(?<=[A-Za-z])-\n(?=[a-z])", "", text)
    text = re.sub(r"\n(?=[ \t]{3,}\S)", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *\n+ *", "\n\n", text)
    return text.strip()


def prose_paragraphs(text: str) -> list[str]:
    normalized = normalize_text(text)
    paragraphs = []
    for block in re.split(r"\n\s*\n", normalized):
        paragraph = re.sub(r"\s*\n\s*", " ", block).strip()
        word_count = len(WORD_PATTERN.findall(paragraph))
        if word_count >= 3 and re.search(r"[.!?][^A-Za-z0-9]*$", paragraph):
            paragraphs.append(paragraph)
    return paragraphs


def sentence_texts(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", normalize_text(text))
    protected = re.sub(r"(?<=\d)\.(?=\d)", "<DECIMAL_POINT>", normalized)
    return [
        match.group(0).replace("<DECIMAL_POINT>", ".").strip()
        for match in SENTENCE_PATTERN.finditer(protected)
        if match.group(0).strip()
    ]


def exclude_lines(text: str, patterns: list[str] | None) -> str:
    if not patterns:
        return text
    compiled = [re.compile(pattern) for pattern in patterns]
    return "\n".join(
        "" if any(pattern.fullmatch(line.strip()) for pattern in compiled) else line
        for line in text.splitlines()
    )


def measure_text(
    text: str,
    exclude_line_patterns: list[str] | None = None,
) -> dict[str, Any]:
    text = exclude_lines(text, exclude_line_patterns)
    paragraphs = prose_paragraphs(text)
    prose_text = "\n\n".join(paragraphs)
    sentences = sentence_texts(prose_text)
    sentence_lengths = [len(WORD_PATTERN.findall(sentence)) for sentence in sentences]
    sentence_lengths = [length for length in sentence_lengths if length]
    previews = []
    for index, paragraph in enumerate(paragraphs, start=1):
        encoded = paragraph.encode("utf-8")
        previews.append(
            {
                "paragraph_index": index,
                "sha256": hashlib.sha256(encoded).hexdigest(),
                "preview": paragraph[:180],
            }
        )
    return {
        "word_count": len(WORD_PATTERN.findall(prose_text)),
        "sentence_count": len(sentences),
        "paragraph_count": len(paragraphs),
        "sentence_words": (
            {
                "minimum": min(sentence_lengths),
                "median": statistics.median(sentence_lengths),
                "maximum": max(sentence_lengths),
            }
            if sentence_lengths
            else None
        ),
        "paragraph_digests": previews,
    }


def measure_spec(text: str, spec: dict[str, Any]) -> dict[str, Any]:
    pages = split_pages(text)
    denominator = spec.get("technical_page_denominator")
    if not isinstance(denominator, int) or denominator < 1:
        raise ValueError("technical_page_denominator must be a positive integer")
    chapters = spec.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        raise ValueError("spec chapters must be a nonempty array")
    measured = []
    for chapter in chapters:
        if not isinstance(chapter, dict) or not isinstance(chapter.get("chapter"), str):
            raise ValueError("each chapter spec must name a chapter")
        segments = chapter.get("segments")
        if not isinstance(segments, list) or not segments:
            raise ValueError(f"chapter {chapter['chapter']} requires segments")
        resolved_segments = []
        for segment in segments:
            resolved = dict(segment)
            resolved.setdefault(
                "include_start_marker", spec.get("include_start_markers", True)
            )
            resolved_segments.append(resolved)
        extracted = [extract_segment(pages, segment) for segment in resolved_segments]
        pages_touched = {
            page
            for segment in segments
            for page in range(segment["page_start"], segment["page_end"] + 1)
        }
        result = {
            "chapter": chapter["chapter"],
            "measurement_status": "mechanical-draft",
            "source_segments": resolved_segments,
            "page_start": min(pages_touched),
            "page_end": max(pages_touched),
            "page_fraction": round(len(pages_touched) / denominator, 6),
            **measure_text(
                "\n\n".join(extracted),
                [
                    *spec.get("exclude_line_patterns", []),
                    *chapter.get("exclude_line_patterns", []),
                ],
            ),
            "counting_method": spec.get("counting_method", ""),
            "ambiguities": [
                *spec.get("ambiguities", []),
                *chapter.get("ambiguities", []),
            ],
        }
        measured.append(result)
    return {
        "paper_id": spec.get("paper_id"),
        "source_page_count": len(pages),
        "technical_page_denominator": denominator,
        "measurement_status": "mechanical-draft",
        "chapter_layout_drafts": measured,
    }


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        result = measure_spec(args.text.read_text(encoding="utf-8"), load_json(args.spec))
        encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(encoded, encoding="utf-8")
        else:
            print(encoded, end="")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
