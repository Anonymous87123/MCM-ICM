#!/usr/bin/env python3
"""Extract page-aware text and selected rendered pages for one manifest paper."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def load_record(manifest_path: Path, record_id: str) -> dict[str, Any]:
    match: dict[str, Any] | None = None
    with manifest_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise RuntimeError(f"Invalid manifest JSON on line {line_number}: {error}") from error
            if record.get("paper_id") == record_id or record.get("document_id") == record_id:
                if match is not None:
                    raise RuntimeError(f"Duplicate record identifier in manifest: {record_id}")
                match = record
    if match is None:
        raise RuntimeError(f"record identifier not found: {record_id}")
    if match.get("file_extension") != ".pdf":
        raise RuntimeError(f"record is not a PDF: {record_id}")
    return match


def parse_page_spec(value: str, page_count: int) -> list[int]:
    if value.casefold() == "all":
        return list(range(1, page_count + 1))
    pages: set[int] = set()
    for item in value.split(","):
        item = item.strip()
        if not item:
            continue
        if re.fullmatch(r"\d+", item):
            pages.add(int(item))
            continue
        match = re.fullmatch(r"(\d+)-(\d+)", item)
        if not match:
            raise ValueError(f"Invalid page selector: {item}")
        start, end = (int(group) for group in match.groups())
        if start > end:
            raise ValueError(f"Descending page range: {item}")
        pages.update(range(start, end + 1))
    if not pages:
        raise ValueError("No render pages selected")
    invalid = sorted(page for page in pages if page < 1 or page > page_count)
    if invalid:
        raise ValueError(f"Render pages outside 1-{page_count}: {invalid}")
    return sorted(pages)


def split_pages(raw_text: str, expected_pages: int) -> tuple[list[str], list[str]]:
    normalized = raw_text.replace("\r\n", "\n").replace("\r", "\n")
    pages = normalized.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    warnings: list[str] = []
    if len(pages) < expected_pages:
        warnings.append(
            f"pdftotext returned {len(pages)} pages; expected {expected_pages}; padded empty pages"
        )
        pages.extend("" for _ in range(expected_pages - len(pages)))
    elif len(pages) > expected_pages:
        extras = pages[expected_pages:]
        if any(page.strip() for page in extras):
            warnings.append(
                f"pdftotext returned {len(pages)} nontrivial page segments; expected {expected_pages}"
            )
        pages = pages[:expected_pages]
    return pages, warnings


def run_text_extraction(executable: str, source_path: Path, output_path: Path) -> None:
    result = subprocess.run(
        [executable, "-layout", "-enc", "UTF-8", str(source_path), str(output_path)],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
    )
    if result.returncode != 0:
        message = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"pdftotext failed: {message[:1000]}")


def render_page(
    executable: str,
    source_path: Path,
    page: int,
    dpi: int,
    output_prefix: Path,
) -> Path:
    result = subprocess.run(
        [
            executable,
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-png",
            "-r",
            str(dpi),
            str(source_path),
            str(output_prefix),
        ],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
    )
    if result.returncode != 0:
        message = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"pdftoppm failed on page {page}: {message[:1000]}")
    output_path = output_prefix.with_suffix(".png")
    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError(f"pdftoppm did not create page {page}: {output_path}")
    return output_path


def atomic_write_text(path: Path, content: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def extraction_signature(
    record: dict[str, Any], artifact_id: str, render_pages: list[int], dpi: int
) -> str:
    value = {
        "dpi": dpi,
        "artifact_id": artifact_id,
        "render_pages": render_pages,
        "source_sha256": record["sha256"],
        "version": 3,
    }
    serialized = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def existing_is_current(target: Path, signature: str) -> bool:
    metadata_path = target / "extraction.json"
    if not metadata_path.is_file():
        return False
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return metadata.get("extraction_signature_sha256") == signature


def extract(
    manifest_path: Path,
    source_root: Path,
    output_root: Path,
    record_id: str,
    render_spec: str,
    dpi: int,
    replace: bool,
) -> dict[str, Any]:
    record = load_record(manifest_path, record_id)
    artifact_id = record.get("paper_id") or record["document_id"]
    page_count = record.get("page_count")
    if not isinstance(page_count, int) or page_count < 1:
        raise RuntimeError(f"record has no valid page_count: {record_id}")
    render_pages = parse_page_spec(render_spec, page_count)
    source_path = source_root.joinpath(*record["relative_path"].split("/"))
    if not source_path.is_file():
        raise RuntimeError(f"source PDF missing: {source_path}")
    current_hash = sha256_file(source_path)
    if current_hash != record["sha256"]:
        raise RuntimeError(f"source hash differs from manifest: {record_id}")

    pdftotext = shutil.which("pdftotext")
    pdftoppm = shutil.which("pdftoppm")
    if not pdftotext or not pdftoppm:
        raise RuntimeError("pdftotext and pdftoppm are required")

    signature = extraction_signature(record, artifact_id, render_pages, dpi)
    output_root.mkdir(parents=True, exist_ok=True)
    target = output_root / artifact_id
    if target.exists():
        if existing_is_current(target, signature):
            return json.loads((target / "extraction.json").read_text(encoding="utf-8"))
        if not replace:
            raise RuntimeError(
                f"extraction target exists with different or incomplete settings: {target}"
            )
        if target.resolve().parent != output_root.resolve() or target.name != artifact_id:
            raise RuntimeError(f"refusing to replace unsafe extraction target: {target}")
        shutil.rmtree(target)

    temporary_root = Path(tempfile.mkdtemp(prefix=f".{artifact_id}-", dir=output_root))
    try:
        text_dir = temporary_root / "text" / "pages"
        render_dir = temporary_root / "rendered"
        text_dir.mkdir(parents=True)
        render_dir.mkdir(parents=True)

        raw_text_path = temporary_root / "text" / "full.txt"
        run_text_extraction(pdftotext, source_path, raw_text_path)
        raw_text = raw_text_path.read_text(encoding="utf-8", errors="replace")
        pages, warnings = split_pages(raw_text, page_count)

        page_records: list[dict[str, Any]] = []
        total_chars = 0
        total_words = 0
        empty_pages: list[int] = []
        for index, page_text in enumerate(pages, start=1):
            page_path = text_dir / f"page-{index:04d}.txt"
            atomic_write_text(page_path, page_text.rstrip() + "\n" if page_text else "")
            char_count = len(re.sub(r"\s+", "", page_text))
            word_count = len(re.findall(r"[A-Za-z0-9]+", page_text))
            total_chars += char_count
            total_words += word_count
            if char_count < 20:
                empty_pages.append(index)
            page_records.append(
                {
                    "char_count": char_count,
                    "page_index": index,
                    "rendered": index in render_pages,
                    "rendered_file": f"rendered/page-{index:04d}.png" if index in render_pages else None,
                    "text_file": f"text/pages/page-{index:04d}.txt",
                    "word_count": word_count,
                }
            )

        rendered_files: list[str] = []
        for page in render_pages:
            output_prefix = render_dir / f"page-{page:04d}"
            rendered = render_page(pdftoppm, source_path, page, dpi, output_prefix)
            rendered_files.append(rendered.relative_to(temporary_root).as_posix())

        text_pages = page_count - len(empty_pages)
        average_chars_per_page = total_chars / page_count
        if total_chars == 0 or average_chars_per_page < 100:
            extraction_status = "needs-ocr"
        elif empty_pages:
            extraction_status = "partial-text-review"
        else:
            extraction_status = "text-extracted"

        metadata = {
            "dpi": dpi,
            "artifact_id": artifact_id,
            "document_id": record["document_id"],
            "document_role": record["document_role"],
            "empty_or_near_empty_pages": empty_pages,
            "extraction_signature_sha256": signature,
            "extraction_status": extraction_status,
            "extraction_version": 3,
            "page_count": page_count,
            "paper_id": record.get("paper_id"),
            "problem_type": record["problem_type"],
            "render_pages": render_pages,
            "rendered_files": rendered_files,
            "source_relative_path": record["relative_path"],
            "source_sha256": record["sha256"],
            "text_char_count": total_chars,
            "text_chars_per_page": round(average_chars_per_page, 3),
            "text_coverage_ratio": round(text_pages / page_count, 6),
            "text_page_count": len(pages),
            "text_word_count": total_words,
            "visual_review_status": "pending",
            "warnings": warnings,
            "year": record["year"],
        }
        pages_jsonl = "\n".join(
            json.dumps(record, sort_keys=True) for record in page_records
        ) + "\n"
        atomic_write_text(temporary_root / "pages.jsonl", pages_jsonl)
        atomic_write_text(
            temporary_root / "extraction.json",
            json.dumps(metadata, indent=2, sort_keys=True) + "\n",
        )
        os.replace(temporary_root, target)
        return metadata
    except Exception:
        shutil.rmtree(temporary_root, ignore_errors=True)
        raise


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    identifiers = parser.add_mutually_exclusive_group(required=True)
    identifiers.add_argument("--paper-id")
    identifiers.add_argument("--document-id")
    parser.add_argument("--render-pages", default="1-3")
    parser.add_argument("--dpi", type=int, default=144)
    parser.add_argument("--replace", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.dpi < 72 or args.dpi > 300:
        raise SystemExit("--dpi must be between 72 and 300")
    try:
        metadata = extract(
            args.manifest.resolve(),
            args.source.resolve(),
            args.output.resolve(),
            args.paper_id or args.document_id,
            args.render_pages,
            args.dpi,
            args.replace,
        )
    except (RuntimeError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(json.dumps(metadata, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
