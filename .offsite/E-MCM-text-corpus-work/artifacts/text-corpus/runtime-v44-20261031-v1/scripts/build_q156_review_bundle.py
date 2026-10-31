#!/usr/bin/env python3
"""Build create-only, byte-bounded visual-review proxies for Queue 156."""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2025-2503268-228e0ec5"
SOURCE = ROOT / "artifacts" / "papers" / PAPER_ID / PAPER_ID
OUTPUT_ROOT = SOURCE / "review-proxies-v1"
MAX_PROXY_BYTES = 450_000
MAX_CONTEXT_IMAGE_BYTES = 4 * 1024 * 1024


GROUPS: list[dict[str, Any]] = [
    {
        "file": "review-01-pages-01-05.jpg",
        "coverage": ["physical pages 1-5 overview"],
        "columns": 5,
        "cell_width": 320,
        "panels": [{"page": page, "label": f"p{page:02d}"} for page in range(1, 6)],
    },
    {
        "file": "review-02-pages-06-10.jpg",
        "coverage": ["physical pages 6-10 overview"],
        "columns": 5,
        "cell_width": 320,
        "panels": [{"page": page, "label": f"p{page:02d}"} for page in range(6, 11)],
    },
    {
        "file": "review-03-pages-11-15.jpg",
        "coverage": ["physical pages 11-15 overview"],
        "columns": 5,
        "cell_width": 320,
        "panels": [{"page": page, "label": f"p{page:02d}"} for page in range(11, 16)],
    },
    {
        "file": "review-04-pages-16-20.jpg",
        "coverage": ["physical pages 16-20 overview"],
        "columns": 5,
        "cell_width": 320,
        "panels": [{"page": page, "label": f"p{page:02d}"} for page in range(16, 21)],
    },
    {
        "file": "review-05-pages-21-26.jpg",
        "coverage": ["physical pages 21-26 overview"],
        "columns": 6,
        "cell_width": 270,
        "panels": [{"page": page, "label": f"p{page:02d}"} for page in range(21, 27)],
    },
    {
        "file": "review-06-memo-and-data.jpg",
        "coverage": [
            "physical page 2 stakeholder memo and paragraph layout",
            "physical page 7 data collection, data selection, and ELA figure",
        ],
        "columns": 2,
        "cell_width": 1020,
        "panels": [
            {"page": 2, "crop": [100, 100, 1140, 900], "label": "p02 memo - upper"},
            {"page": 2, "crop": [100, 820, 1140, 1660], "label": "p02 memo - lower"},
            {"page": 7, "crop": [100, 120, 1180, 850], "label": "p07 data - upper"},
            {"page": 7, "crop": [100, 820, 1180, 1530], "label": "p07 data and ELA - lower"},
        ],
    },
    {
        "file": "review-07-equations-and-weights.jpg",
        "coverage": [
            "numbered equations (1)-(23)",
            "integrated STDM system",
            "parameter table and four AHP judgment matrices",
        ],
        "columns": 2,
        "cell_width": 1000,
        "panels": [
            {"page": 8, "crop": [130, 1220, 1190, 1460], "label": "p08 equation (1)"},
            {"page": 9, "crop": [130, 480, 1190, 650], "label": "p09 equation (2)"},
            {"page": 9, "crop": [130, 1060, 1190, 1240], "label": "p09 equation (3)"},
            {"page": 10, "crop": [130, 230, 1190, 510], "label": "p10 equations (4)-(6)"},
            {"page": 14, "crop": [150, 760, 1190, 1340], "label": "p14 equations (7)-(9)"},
            {"page": 15, "crop": [150, 120, 1190, 750], "label": "p15 equations (10)-(14)"},
            {"page": 15, "crop": [150, 730, 1190, 1520], "label": "p15 equations (15)-(19)"},
            {"page": 16, "crop": [150, 140, 1190, 910], "label": "p16 equations (20)-(23)"},
            {"page": 17, "crop": [130, 120, 1190, 520], "label": "p17 Table 5 parameters"},
            {"page": 17, "crop": [130, 510, 1190, 1225], "label": "p17 AHP matrices and Table 6"},
        ],
    },
    {
        "file": "review-08-transfer-and-close.jpg",
        "coverage": [
            "physical page 22 local sensitivity table and Big Sur validation opening",
            "physical page 23 Big Sur source visual, equation (24), and transferred score",
            "physical page 24 strengths and weaknesses",
        ],
        "columns": 2,
        "cell_width": 1000,
        "panels": [
            {"page": 22, "crop": [130, 120, 1190, 1080], "label": "p22 sensitivity table"},
            {"page": 22, "crop": [130, 1040, 1190, 1520], "label": "p22 Big Sur validation opening"},
            {"page": 23, "crop": [130, 120, 1190, 590], "label": "p23 Big Sur source visual"},
            {"page": 23, "crop": [130, 560, 1190, 1410], "label": "p23 equation (24) and result"},
            {"page": 24, "crop": [130, 130, 1190, 1100], "label": "p24 strengths"},
            {"page": 24, "crop": [130, 1070, 1190, 1520], "label": "p24 weaknesses"},
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
        for quality in range(92, 35, -4):
            encoded = encode_jpeg(candidate, quality)
            if len(encoded) <= MAX_PROXY_BYTES:
                return encoded, candidate, quality
        next_width = round(candidate.width * 0.9)
        next_height = round(candidate.height * 0.9)
        if next_width < 900:
            raise RuntimeError("cannot meet proxy byte limit above the legibility floor")
        candidate = candidate.resize((next_width, next_height), Image.Resampling.LANCZOS)


def page_path(page: int) -> Path:
    return SOURCE / "rendered" / f"page-{page:04d}.png"


def validate_crop(
    crop: list[int] | None,
    size: tuple[int, int],
) -> tuple[int, int, int, int]:
    if crop is None:
        return 0, 0, size[0], size[1]
    if len(crop) != 4 or any(not isinstance(value, int) for value in crop):
        raise RuntimeError(f"invalid crop: {crop}")
    left, top, right, bottom = crop
    if left < 0 or top < 0 or right <= left or bottom <= top:
        raise RuntimeError(f"invalid crop bounds: {crop}")
    if right > size[0] or bottom > size[1]:
        raise RuntimeError(f"crop {crop} exceeds page bounds {size}")
    return left, top, right, bottom


def build_group(group: dict[str, Any]) -> tuple[Image.Image, list[dict[str, Any]]]:
    label_height = 30
    padding = 14
    columns = group["columns"]
    cell_width = group["cell_width"]
    rendered: list[tuple[Image.Image, dict[str, Any]]] = []
    panel_records: list[dict[str, Any]] = []
    try:
        for panel in group["panels"]:
            source_path = page_path(panel["page"])
            if not source_path.is_file():
                raise RuntimeError(f"missing source page: {source_path}")
            with Image.open(source_path) as opened:
                source = ImageOps.exif_transpose(opened).convert("RGB")
            source_size = source.size
            crop = validate_crop(panel.get("crop"), source.size)
            snippet = source.crop(crop)
            source.close()
            target_height = max(1, round(snippet.height * cell_width / snippet.width))
            resized = snippet.resize((cell_width, target_height), Image.Resampling.LANCZOS)
            snippet.close()
            rendered.append((resized, panel))
            panel_records.append(
                {
                    "crop": list(crop),
                    "label": panel["label"],
                    "page": panel["page"],
                    "source_bytes": source_path.stat().st_size,
                    "source_file": source_path.relative_to(ROOT).as_posix(),
                    "source_height": source_size[1],
                    "source_sha256": sha256_file(source_path),
                    "source_width": source_size[0],
                }
            )

        rows = (len(rendered) + columns - 1) // columns
        row_heights: list[int] = []
        for row in range(rows):
            row_images = rendered[row * columns : (row + 1) * columns]
            row_heights.append(max(image.height for image, _ in row_images))
        canvas_width = padding + columns * (cell_width + padding)
        canvas_height = padding + sum(label_height + height + padding for height in row_heights)
        canvas = Image.new("RGB", (canvas_width, canvas_height), "white")
        draw = ImageDraw.Draw(canvas)
        y = padding
        for row, row_height in enumerate(row_heights):
            for column in range(columns):
                index = row * columns + column
                if index >= len(rendered):
                    break
                image, panel = rendered[index]
                x = padding + column * (cell_width + padding)
                draw.rectangle((x, y, x + cell_width, y + label_height), fill=(238, 242, 247))
                draw.text((x + 8, y + 7), panel["label"], fill="black")
                canvas.paste(image, (x, y + label_height))
            y += label_height + row_height + padding
        return canvas, panel_records
    finally:
        for image, _ in rendered:
            image.close()


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
        raise SystemExit(f"source stage missing: {SOURCE}")
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite review bundle: {OUTPUT_ROOT}")
    metadata = json.loads((SOURCE / "extraction.json").read_text(encoding="utf-8"))
    if (
        metadata.get("paper_id") != PAPER_ID
        or metadata.get("page_count") != 26
        or metadata.get("dpi") != 150
        or metadata.get("source_sha256")
        != "228e0ec59bed8bf2d8ade0e628dba456075523c293b87be7d88d8182eeb5ded3"
        or metadata.get("visual_review_status") != "pending"
    ):
        raise SystemExit("Queue 156 source identity or review prerequisite changed")

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=False)
    proxy_records: list[dict[str, Any]] = []
    for index, group in enumerate(GROUPS, start=1):
        canvas, panel_records = build_group(group)
        try:
            encoded, bounded, quality = byte_bound(canvas)
            output_path = OUTPUT_ROOT / group["file"]
            output_path.write_bytes(encoded)
            proxy_records.append(
                {
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
            )
            if bounded is not canvas:
                bounded.close()
        finally:
            canvas.close()

    total_proxy_bytes = sum(item["output_bytes"] for item in proxy_records)
    if len(proxy_records) != 8:
        raise RuntimeError(f"expected 8 proxies, got {len(proxy_records)}")
    if total_proxy_bytes >= MAX_CONTEXT_IMAGE_BYTES:
        raise RuntimeError("proxy bundle exceeds the between-compactions image budget")
    ledger = {
        "files_deleted": 0,
        "max_proxy_bytes": MAX_PROXY_BYTES,
        "paper_id": PAPER_ID,
        "proxy_bundle_sha256": proxy_bundle_sha(proxy_records),
        "proxy_count": len(proxy_records),
        "proxies": proxy_records,
        "purpose": (
            "Complete physical-page overview plus focused memo, data, equations, AHP, "
            "Big Sur transfer, and final-section review. Proxies do not replace original PNGs."
        ),
        "request_body_guard": {
            "detail": "high",
            "endpoint": "https://1for.cc/v1/responses",
            "max_model_visible_image_bytes_between_compactions": MAX_CONTEXT_IMAGE_BYTES,
            "max_proxies_in_context_segment": 8,
            "max_proxy_bytes": MAX_PROXY_BYTES,
            "maximum_images_per_tool_call": 1,
            "original_full_pages_model_visible": False,
        },
        "source_extraction_signature_sha256": metadata["extraction_signature_sha256"],
        "status": "built-pending-model-review",
        "total_proxy_bytes": total_proxy_bytes,
    }
    ledger_path = OUTPUT_ROOT / "ledger.json"
    ledger_path.write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "files_created": len(proxy_records) + 1,
                "files_deleted": 0,
                "ledger": str(ledger_path.resolve()),
                "output_tree_sha256": tree_sha(OUTPUT_ROOT),
                "paper_id": PAPER_ID,
                "proxy_bundle_sha256": ledger["proxy_bundle_sha256"],
                "proxy_count": len(proxy_records),
                "status": "pass",
                "total_proxy_bytes": total_proxy_bytes,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
