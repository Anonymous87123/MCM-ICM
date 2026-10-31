#!/usr/bin/env python3
"""Create one byte-bounded, wide crop for Queue 134 Equation (27)."""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2020-2013836-4c773f05"
SOURCE = (
    ROOT
    / "tmp"
    / "q134-ocr-stage-v2"
    / PAPER_ID
    / "rendered"
    / "page-0016.png"
)
OUTPUT_ROOT = ROOT / "tmp" / "q134-formula-review-eq27-v1"
OUTPUT_NAME = "review-09-equation-27-wide.jpg"
MAX_PROXY_BYTES = 450_000
CROP = (250, 1250, 1480, 1580)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def encode_bounded(image: Image.Image) -> tuple[bytes, int]:
    for quality in range(94, 39, -3):
        buffer = io.BytesIO()
        image.save(
            buffer,
            format="JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
            subsampling=0,
        )
        encoded = buffer.getvalue()
        if len(encoded) <= MAX_PROXY_BYTES:
            return encoded, quality
    raise RuntimeError("Equation (27) crop cannot meet the 450 KB proxy limit")


def main() -> int:
    if not SOURCE.is_file():
        raise SystemExit(f"missing source page: {SOURCE}")
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing supplement: {OUTPUT_ROOT}")

    with Image.open(SOURCE) as opened:
        page = ImageOps.exif_transpose(opened).convert("RGB")
    try:
        if page.size != (1700, 2200):
            raise SystemExit(f"unexpected source dimensions: {page.size}")
        crop = page.crop(CROP)
        try:
            encoded, quality = encode_bounded(crop)
            width, height = crop.size
        finally:
            crop.close()
    finally:
        page.close()

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=False)
    proxy_path = OUTPUT_ROOT / OUTPUT_NAME
    proxy_path.write_bytes(encoded)
    ledger = {
        "crop": list(CROP),
        "files_created": 2,
        "files_deleted": 0,
        "max_proxy_bytes": MAX_PROXY_BYTES,
        "output_bytes": len(encoded),
        "output_file": OUTPUT_NAME,
        "output_height": height,
        "output_sha256": sha256_bytes(encoded),
        "output_width": width,
        "page": 16,
        "paper_id": PAPER_ID,
        "purpose": "Wide left-inclusive fidelity check of the complete Equation (27).",
        "quality": quality,
        "source_file": SOURCE.relative_to(ROOT).as_posix(),
        "source_sha256": sha256_file(SOURCE),
        "transport_policy": {
            "detail": "high",
            "maximum_images_per_tool_call": 1,
            "original_full_page_model_visible": False,
        },
    }
    ledger_path = OUTPUT_ROOT / "ledger.json"
    ledger_path.write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
