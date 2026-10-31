#!/usr/bin/env python3
"""Create a byte-bounded JPEG proxy for safe model visual review."""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
from pathlib import Path

from PIL import Image, ImageOps


MAX_SAFE_PROXY_BYTES = 450_000


def parse_crop(value: str) -> tuple[int, int, int, int]:
    try:
        crop = tuple(int(part.strip()) for part in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError("crop must contain four integers") from error
    if len(crop) != 4:
        raise argparse.ArgumentTypeError("crop must be LEFT,TOP,RIGHT,BOTTOM")
    left, top, right, bottom = crop
    if left < 0 or top < 0 or right <= left or bottom <= top:
        raise argparse.ArgumentTypeError("crop bounds must define a positive rectangle")
    return left, top, right, bottom


def fit_dimensions(
    width: int,
    height: int,
    max_width: int,
    max_height: int,
) -> tuple[int, int]:
    scale = min(1.0, max_width / width, max_height / height)
    return max(1, round(width * scale)), max(1, round(height * scale))


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


def build_proxy(
    source: Image.Image,
    *,
    max_width: int,
    max_height: int,
    max_bytes: int,
    start_quality: int,
) -> tuple[bytes, Image.Image, int]:
    target_width, target_height = fit_dimensions(
        source.width,
        source.height,
        max_width,
        max_height,
    )
    candidate = source.resize(
        (target_width, target_height),
        Image.Resampling.LANCZOS,
    )

    while True:
        for quality in range(start_quality, 34, -6):
            encoded = encode_jpeg(candidate, quality)
            if len(encoded) <= max_bytes:
                return encoded, candidate, quality

        next_width = round(candidate.width * 0.84)
        next_height = round(candidate.height * 0.84)
        if next_width < 480 or next_height < 480:
            break
        candidate = candidate.resize(
            (next_width, next_height),
            Image.Resampling.LANCZOS,
        )

    encoded = encode_jpeg(candidate, 28)
    if len(encoded) > max_bytes:
        raise RuntimeError(
            f"cannot meet --max-bytes without shrinking below the legibility floor: "
            f"{len(encoded)} > {max_bytes}"
        )
    return encoded, candidate, 28


def atomic_write(path: Path, content: bytes) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(content)
    os.replace(temporary, path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--crop", type=parse_crop)
    parser.add_argument("--max-width", type=int, default=1400)
    parser.add_argument("--max-height", type=int, default=1800)
    parser.add_argument("--max-bytes", type=int, default=MAX_SAFE_PROXY_BYTES)
    parser.add_argument("--quality", type=int, default=82)
    args = parser.parse_args(argv or sys.argv[1:])

    if args.output.suffix.lower() not in {".jpg", ".jpeg"}:
        raise SystemExit("--output must use a .jpg or .jpeg suffix")
    if args.max_width < 480 or args.max_height < 480:
        raise SystemExit("maximum dimensions must both be at least 480 pixels")
    if not 50_000 <= args.max_bytes <= MAX_SAFE_PROXY_BYTES:
        raise SystemExit(
            f"--max-bytes must be between 50000 and {MAX_SAFE_PROXY_BYTES}"
        )
    if not 40 <= args.quality <= 95:
        raise SystemExit("--quality must be between 40 and 95")

    input_path = args.input.resolve()
    output_path = args.output.resolve()
    if not input_path.is_file():
        raise SystemExit(f"input image missing: {input_path}")

    with Image.open(input_path) as opened:
        oriented = ImageOps.exif_transpose(opened)
        original_size = oriented.size
        if args.crop:
            left, top, right, bottom = args.crop
            if right > oriented.width or bottom > oriented.height:
                raise SystemExit(
                    f"crop exceeds source bounds {oriented.width}x{oriented.height}"
                )
            oriented = oriented.crop(args.crop)
        source = oriented.convert("RGB")

    encoded, proxy, quality = build_proxy(
        source,
        max_width=args.max_width,
        max_height=args.max_height,
        max_bytes=args.max_bytes,
        start_quality=args.quality,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(output_path, encoded)

    print(
        json.dumps(
            {
                "bytes": len(encoded),
                "crop": list(args.crop) if args.crop else None,
                "input": str(input_path),
                "original_height": original_size[1],
                "original_width": original_size[0],
                "output": str(output_path),
                "proxy_height": proxy.height,
                "proxy_width": proxy.width,
                "quality": quality,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
