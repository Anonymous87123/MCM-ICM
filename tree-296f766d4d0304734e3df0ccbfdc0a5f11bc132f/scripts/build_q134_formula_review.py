#!/usr/bin/env python3
"""Build create-only, byte-bounded focused review proxies for Queue 134."""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2020-2013836-4c773f05"
SOURCE = ROOT / "tmp" / "q134-ocr-stage-v2" / PAPER_ID
OUTPUT_ROOT = ROOT / "tmp" / "q134-formula-review-v1"
MAX_PROXY_BYTES = 450_000
PAGE_SIZE = (1700, 2200)
LABEL_HEIGHT = 34
PADDING = 16


GROUPS: list[dict[str, Any]] = [
    {
        "file": "review-01-tables-1-2.jpg",
        "coverage": ["Table 1 nomenclature", "Table 2 cellular-automaton state rules"],
        "panels": [
            {"page": 5, "crop": [420, 1340, 1280, 2140], "label": "p05 - Table 1"},
            {"page": 6, "crop": [350, 1680, 1250, 2150], "label": "p06 - Table 2"},
        ],
    },
    {
        "file": "review-02-equations-01-02.jpg",
        "coverage": ["Equation (1)", "Equation (2)"],
        "panels": [
            {"page": 7, "crop": [600, 640, 1480, 810], "label": "p07 - Equation (1)"},
            {"page": 8, "crop": [600, 1810, 1480, 1960], "label": "p08 - Equation (2)"},
        ],
    },
    {
        "file": "review-03-equations-03-10.jpg",
        "coverage": ["Equations (3)-(10)", "Equation (7) numbering check"],
        "panels": [
            {"page": 9, "crop": [550, 250, 1480, 1340], "label": "p09 - Equations (3)-(10)"},
        ],
    },
    {
        "file": "review-04-equations-11-14.jpg",
        "coverage": ["Equation (11)", "Equations (12)-(14)"],
        "panels": [
            {"page": 10, "crop": [650, 720, 1480, 900], "label": "p10 - Equation (11)"},
            {"page": 11, "crop": [430, 430, 1480, 1720], "label": "p11 - Equations (12)-(14)"},
        ],
    },
    {
        "file": "review-05-equations-15-16-table-3.jpg",
        "coverage": ["Equations (15)-(16)", "Table 3 wave grades"],
        "panels": [
            {
                "page": 13,
                "crop": [480, 1030, 1480, 2100],
                "label": "p13 - Equations (15)-(16) and Table 3",
            },
        ],
    },
    {
        "file": "review-06-equations-17-24-table-4.jpg",
        "coverage": ["Equations (17)-(24)", "Table 4 rainfall grades"],
        "panels": [
            {"page": 14, "crop": [550, 480, 1480, 1450], "label": "p14 - Equations (17)-(24)"},
            {"page": 15, "crop": [500, 620, 1150, 1100], "label": "p15 - Table 4"},
        ],
    },
    {
        "file": "review-07-equations-25-27-ratio.jpg",
        "coverage": ["Equations (25)-(27)", "printed initial water-to-sand ratio 0.045"],
        "panels": [
            {"page": 16, "crop": [600, 450, 1480, 1550], "label": "p16 - Equations (25)-(27)"},
            {"page": 19, "crop": [180, 1230, 1480, 1460], "label": "p19 - printed initial ratio"},
        ],
    },
    {
        "file": "review-08-page-22-missing-line.jpg",
        "coverage": ["text after Figure 18", "sentence ending before 'much smaller'"],
        "panels": [
            {"page": 22, "crop": [180, 1180, 1480, 1510], "label": "p22 - Figure 18 transition text"},
        ],
    },
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def encode_jpeg(image: Image.Image, quality: int) -> bytes:
    buffer = io.BytesIO()
    image.save(
        buffer,
        format="JPEG",
        quality=quality,
        optimize=True,
        progressive=True,
        subsampling=0,
    )
    return buffer.getvalue()


def byte_bound(image: Image.Image) -> tuple[bytes, Image.Image, int]:
    candidate = image
    while True:
        for quality in range(92, 39, -4):
            encoded = encode_jpeg(candidate, quality)
            if len(encoded) <= MAX_PROXY_BYTES:
                return encoded, candidate, quality
        next_width = round(candidate.width * 0.9)
        next_height = round(candidate.height * 0.9)
        if next_width < 760:
            raise RuntimeError("cannot meet the proxy byte limit above the legibility floor")
        candidate = candidate.resize((next_width, next_height), Image.Resampling.LANCZOS)


def validate_crop(crop: list[int]) -> tuple[int, int, int, int]:
    if len(crop) != 4 or any(not isinstance(value, int) for value in crop):
        raise RuntimeError(f"invalid crop: {crop}")
    left, top, right, bottom = crop
    if left < 0 or top < 0 or right <= left or bottom <= top:
        raise RuntimeError(f"invalid crop bounds: {crop}")
    if right > PAGE_SIZE[0] or bottom > PAGE_SIZE[1]:
        raise RuntimeError(f"crop exceeds the fixed page bounds: {crop}")
    return left, top, right, bottom


def build_group(group: dict[str, Any]) -> tuple[Image.Image, list[dict[str, Any]]]:
    opened_pages: dict[int, Image.Image] = {}
    cropped_panels: list[tuple[Image.Image, dict[str, Any]]] = []
    panel_records: list[dict[str, Any]] = []
    try:
        for panel in group["panels"]:
            page = panel["page"]
            source_path = SOURCE / "rendered" / f"page-{page:04d}.png"
            if not source_path.is_file():
                raise RuntimeError(f"missing source page: {source_path}")
            if page not in opened_pages:
                opened = Image.open(source_path)
                oriented = ImageOps.exif_transpose(opened).convert("RGB")
                opened.close()
                if oriented.size != PAGE_SIZE:
                    raise RuntimeError(
                        f"unexpected page size for {source_path}: {oriented.size} != {PAGE_SIZE}"
                    )
                opened_pages[page] = oriented
            crop = validate_crop(panel["crop"])
            snippet = opened_pages[page].crop(crop)
            cropped_panels.append((snippet, panel))
            panel_records.append(
                {
                    "crop": list(crop),
                    "label": panel["label"],
                    "page": page,
                    "source_bytes": source_path.stat().st_size,
                    "source_file": source_path.relative_to(ROOT).as_posix(),
                    "source_height": PAGE_SIZE[1],
                    "source_sha256": sha256_file(source_path),
                    "source_width": PAGE_SIZE[0],
                }
            )

        canvas_width = max(image.width for image, _ in cropped_panels) + 2 * PADDING
        canvas_height = PADDING + sum(
            LABEL_HEIGHT + image.height + PADDING for image, _ in cropped_panels
        )
        canvas = Image.new("RGB", (canvas_width, canvas_height), "white")
        draw = ImageDraw.Draw(canvas)
        y = PADDING
        for snippet, panel in cropped_panels:
            draw.rectangle((0, y - 4, canvas_width, y + LABEL_HEIGHT - 4), fill=(238, 242, 247))
            draw.text((PADDING, y + 5), panel["label"], fill="black")
            y += LABEL_HEIGHT
            canvas.paste(snippet, (PADDING, y))
            y += snippet.height + PADDING
            snippet.close()
        return canvas, panel_records
    finally:
        for opened in opened_pages.values():
            opened.close()


def proxy_bundle_sha(records: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for record in records:
        digest.update(record["output_file"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(bytes.fromhex(record["output_sha256"]))
    return digest.hexdigest()


def tree_sha(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(bytes.fromhex(sha256_file(path)))
    return digest.hexdigest()


def main() -> int:
    if not SOURCE.is_dir():
        raise SystemExit(f"source OCR stage is missing: {SOURCE}")
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing review bundle: {OUTPUT_ROOT}")

    metadata = json.loads((SOURCE / "extraction.json").read_text(encoding="utf-8"))
    if (
        metadata.get("paper_id") != PAPER_ID
        or metadata.get("page_count") != 25
        or metadata.get("dpi") != 200
        or metadata.get("visual_review_status") != "complete"
        or metadata.get("source_sha256")
        != "4c773f053b00da659fae50121f4d8d6a0d6bb29d3af57d0eb1951d45e2d13c14"
    ):
        raise SystemExit("Queue 134 source identity or visual-review prerequisite changed")

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=False)
    proxy_records: list[dict[str, Any]] = []
    for index, group in enumerate(GROUPS, start=1):
        canvas, panel_records = build_group(group)
        try:
            encoded, bounded, quality = byte_bound(canvas)
            output_path = OUTPUT_ROOT / group["file"]
            output_path.write_bytes(encoded)
            record = {
                "coverage": group["coverage"],
                "group_index": index,
                "output_bytes": len(encoded),
                "output_file": output_path.relative_to(OUTPUT_ROOT).as_posix(),
                "output_height": bounded.height,
                "output_sha256": hashlib.sha256(encoded).hexdigest(),
                "output_width": bounded.width,
                "panels": panel_records,
                "quality": quality,
            }
            if record["output_bytes"] > MAX_PROXY_BYTES:
                raise RuntimeError(f"proxy exceeded byte limit: {record}")
            proxy_records.append(record)
            if bounded is not canvas:
                bounded.close()
        finally:
            canvas.close()

    ledger = {
        "files_deleted": 0,
        "max_proxy_bytes": MAX_PROXY_BYTES,
        "paper_id": PAPER_ID,
        "proxy_bundle_sha256": proxy_bundle_sha(proxy_records),
        "proxy_count": len(proxy_records),
        "proxies": proxy_records,
        "purpose": (
            "Focused pixel review of all numbered formulas, Tables 1-4, the printed "
            "initial ratio, and the page-22 OCR gap; transport proxies do not replace "
            "the original rendered PNGs."
        ),
        "source_extraction_signature_sha256": metadata["extraction_signature_sha256"],
        "status": "built-pending-model-review",
        "transport_policy": {
            "detail": "high",
            "maximum_images_per_tool_call": 1,
            "original_full_pages_model_visible": False,
        },
    }
    ledger_path = OUTPUT_ROOT / "ledger.json"
    ledger_path.write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    result = {
        "files_created": len(proxy_records) + 1,
        "files_deleted": 0,
        "ledger": str(ledger_path.resolve()),
        "output_tree_sha256": tree_sha(OUTPUT_ROOT),
        "paper_id": PAPER_ID,
        "proxy_bundle_sha256": ledger["proxy_bundle_sha256"],
        "proxy_count": len(proxy_records),
        "status": "pass",
        "total_proxy_bytes": sum(item["output_bytes"] for item in proxy_records),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
