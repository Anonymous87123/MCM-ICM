#!/usr/bin/env python3
"""Build a create-only, full-page RapidOCR stage for Queue 134."""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import re
import shutil
import tempfile
import time
from pathlib import Path
from typing import Any

from rapidocr_onnxruntime import RapidOCR


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2020-2013836-4c773f05"
SOURCE = ROOT / "tmp" / "q134-ocr-stage-v1" / PAPER_ID
OUTPUT_ROOT = ROOT / "tmp" / "q134-ocr-stage-v2"
PAGE_COUNT = 25
LOW_CONFIDENCE_THRESHOLD = 0.65


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def normalize_box(box: Any) -> list[list[float]]:
    return [[round(float(x), 3), round(float(y), 3)] for x, y in box]


def normalize_elapsed(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return [normalize_elapsed(item) for item in value]
    try:
        return round(float(value), 6)
    except (TypeError, ValueError):
        return str(value)


def write_text(path: Path, value: str) -> None:
    path.write_text(value, encoding="utf-8", newline="\n")


def tree_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def main() -> int:
    if not SOURCE.is_dir():
        raise SystemExit(f"source stage is missing: {SOURCE}")
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing OCR stage: {OUTPUT_ROOT}")

    source_metadata = json.loads((SOURCE / "extraction.json").read_text(encoding="utf-8"))
    expected_pages = list(range(1, PAGE_COUNT + 1))
    if (
        source_metadata.get("paper_id") != PAPER_ID
        or source_metadata.get("page_count") != PAGE_COUNT
        or source_metadata.get("dpi") != 200
        or source_metadata.get("render_pages") != expected_pages
    ):
        raise SystemExit("Queue 134 source stage identity or complete render coverage changed")

    temporary_root = Path(
        tempfile.mkdtemp(prefix=".q134-ocr-stage-v2-", dir=OUTPUT_ROOT.parent)
    )
    target = temporary_root / PAPER_ID
    started = time.perf_counter()
    try:
        shutil.copytree(SOURCE, target)
        engine = RapidOCR()
        ocr_records: list[dict[str, Any]] = []
        page_records: list[dict[str, Any]] = []
        page_texts: list[str] = []
        low_confidence_pages: list[int] = []
        empty_pages: list[int] = []
        total_chars = 0
        total_words = 0

        for page in expected_pages:
            image = target / "rendered" / f"page-{page:04d}.png"
            if not image.is_file() or image.stat().st_size == 0:
                raise RuntimeError(f"rendered page is missing or empty: {image}")
            result, elapsed = engine(str(image))
            lines: list[dict[str, Any]] = []
            for box, text, confidence in result or []:
                normalized = normalize_box(box)
                item = {
                    "box": normalized,
                    "confidence": round(float(confidence), 6),
                    "text": str(text),
                }
                lines.append(item)

            page_text = "\n".join(
                item["text"].strip() for item in lines if item["text"].strip()
            ).rstrip() + "\n"
            page_path = target / "text" / "pages" / f"page-{page:04d}.txt"
            write_text(page_path, page_text)
            page_texts.append(page_text.rstrip())

            char_count = len(re.sub(r"\s+", "", page_text))
            word_count = len(re.findall(r"[A-Za-z0-9]+", page_text))
            low_count = sum(
                item["confidence"] < LOW_CONFIDENCE_THRESHOLD for item in lines
            )
            if char_count < 20:
                empty_pages.append(page)
            if low_count:
                low_confidence_pages.append(page)
            total_chars += char_count
            total_words += word_count
            page_records.append(
                {
                    "char_count": char_count,
                    "ocr_line_count": len(lines),
                    "ocr_low_confidence_count": low_count,
                    "page_index": page,
                    "rendered": True,
                    "rendered_file": f"rendered/page-{page:04d}.png",
                    "text_file": f"text/pages/page-{page:04d}.txt",
                    "word_count": word_count,
                }
            )
            ocr_records.append(
                {
                    "engine_elapsed": normalize_elapsed(elapsed),
                    "lines": lines,
                    "page_index": page,
                }
            )

        full_text = "\n\f\n".join(page_texts).rstrip() + "\n"
        write_text(target / "text" / "full.txt", full_text)
        write_text(
            target / "pages.jsonl",
            "".join(
                json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n"
                for record in page_records
            ),
        )
        ocr_jsonl = "".join(
            json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
            for record in ocr_records
        )
        write_text(target / "ocr-lines.jsonl", ocr_jsonl)

        engine_version = importlib.metadata.version("rapidocr-onnxruntime")
        full_text_sha = digest_bytes(full_text.encode("utf-8"))
        ocr_lines_sha = digest_bytes(ocr_jsonl.encode("utf-8"))
        wall_seconds = round(time.perf_counter() - started, 3)
        metadata = source_metadata.copy()
        metadata.update(
            {
                "empty_or_near_empty_pages": empty_pages,
                "extraction_signature_sha256": digest_bytes(
                    (
                        f"{source_metadata['extraction_signature_sha256']}|"
                        f"rapidocr-onnxruntime-{engine_version}|{full_text_sha}|{ocr_lines_sha}"
                    ).encode("utf-8")
                ),
                "extraction_status": "text-extracted",
                "ocr_low_confidence_pages": low_confidence_pages,
                "ocr_provenance": {
                    "canonical_text_source": (
                        "RapidOCR over every 200 dpi rendered physical page; retained as a "
                        "reading aid pending page-wise visual reconciliation"
                    ),
                    "engine": "rapidocr_onnxruntime",
                    "engine_version": engine_version,
                    "low_confidence_threshold": LOW_CONFIDENCE_THRESHOLD,
                    "ocr_lines_file": "ocr-lines.jsonl",
                    "ocr_lines_sha256": ocr_lines_sha,
                    "page_order": "physical PDF pages 1 through 25, processed sequentially",
                    "reading_order": (
                        "RapidOCR detector order retained; headings, columns, tables, equations, "
                        "and continuation order require rendered-page reconciliation"
                    ),
                    "render_dpi": 200,
                    "total_wall_seconds": wall_seconds,
                },
                "text_char_count": total_chars,
                "text_chars_per_page": round(total_chars / PAGE_COUNT, 3),
                "text_coverage_ratio": round(
                    (PAGE_COUNT - len(empty_pages)) / PAGE_COUNT, 6
                ),
                "text_page_count": PAGE_COUNT,
                "text_word_count": total_words,
                "visual_review_status": "pending",
                "warnings": [
                    "RapidOCR text is a reading aid; equations, chart labels, tables, code, and small symbols require rendered-page verification.",
                    "RapidOCR confidence scores are not calibrated transcription probabilities; low-confidence text is preserved without silent correction.",
                    "MATHmodels/QR promotional overlays are third-party watermarks and must be excluded from positive author-language evidence.",
                ],
            }
        )
        metadata.pop("visual_review", None)
        write_text(
            target / "extraction.json",
            json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )

        output_tree_sha = tree_digest(target)
        os.replace(temporary_root, OUTPUT_ROOT)
        print(
            json.dumps(
                {
                    "empty_page_count": len(empty_pages),
                    "files_deleted": 0,
                    "low_confidence_page_count": len(low_confidence_pages),
                    "output": str((OUTPUT_ROOT / PAPER_ID).resolve()),
                    "output_tree_sha256": output_tree_sha,
                    "page_count": PAGE_COUNT,
                    "paper_id": PAPER_ID,
                    "status": "pass",
                    "text_char_count": total_chars,
                    "text_word_count": total_words,
                    "wall_seconds": wall_seconds,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    except Exception:
        if temporary_root.exists():
            shutil.rmtree(temporary_root, ignore_errors=True)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
