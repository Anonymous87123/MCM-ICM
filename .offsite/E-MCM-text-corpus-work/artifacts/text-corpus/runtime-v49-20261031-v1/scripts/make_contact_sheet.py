#!/usr/bin/env python3
"""Create a labeled contact sheet from an extracted paper's rendered pages."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_page_parser():
    script_path = Path(__file__).with_name("extract_paper.py")
    spec = importlib.util.spec_from_file_location("paper_extractor", script_path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import extractor: {script_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.parse_page_spec


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-dir", type=Path, required=True)
    parser.add_argument("--pages", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--thumbnail-width", type=int, default=320)
    args = parser.parse_args(argv or sys.argv[1:])
    if args.columns < 1 or args.columns > 8:
        raise SystemExit("--columns must be between 1 and 8")
    if args.thumbnail_width < 120 or args.thumbnail_width > 800:
        raise SystemExit("--thumbnail-width must be between 120 and 800")

    paper_dir = args.paper_dir.resolve()
    metadata = json.loads((paper_dir / "extraction.json").read_text(encoding="utf-8"))
    parse_page_spec = load_page_parser()
    try:
        pages = parse_page_spec(args.pages, metadata["page_count"])
    except ValueError as error:
        raise SystemExit(str(error)) from error

    label_height = 30
    gap = 12
    cells: list[tuple[int, Image.Image]] = []
    max_cell_height = 0
    for page in pages:
        path = paper_dir / "rendered" / f"page-{page:04d}.png"
        if not path.is_file():
            raise SystemExit(f"rendered page missing: {path}")
        with Image.open(path) as source:
            image = source.convert("RGB")
        height = round(image.height * args.thumbnail_width / image.width)
        thumbnail = image.resize((args.thumbnail_width, height), Image.Resampling.LANCZOS)
        cells.append((page, thumbnail))
        max_cell_height = max(max_cell_height, height + label_height)

    rows = (len(cells) + args.columns - 1) // args.columns
    canvas_width = gap + args.columns * (args.thumbnail_width + gap)
    canvas_height = gap + rows * (max_cell_height + gap)
    canvas = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=18)
    for index, (page, thumbnail) in enumerate(cells):
        row, column = divmod(index, args.columns)
        x = gap + column * (args.thumbnail_width + gap)
        y = gap + row * (max_cell_height + gap)
        draw.text((x, y + 4), f"PDF page {page}", fill="black", font=font)
        canvas.paste(thumbnail, (x, y + label_height))
        draw.rectangle(
            (x, y + label_height, x + thumbnail.width - 1, y + label_height + thumbnail.height - 1),
            outline="#555555",
            width=1,
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)
    print(
        json.dumps(
            {
                "columns": args.columns,
                "height": canvas_height,
                "output": str(args.output.resolve()),
                "page_count": len(pages),
                "pages": pages,
                "width": canvas_width,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
