#!/usr/bin/env python3
"""Record a deterministic visual review for an extracted paper."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path


def load_page_parser():
    script_path = Path(__file__).with_name("extract_paper.py")
    spec = importlib.util.spec_from_file_location("paper_extractor", script_path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import extractor: {script_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.parse_page_spec


def atomic_write(path: Path, content: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-dir", type=Path, required=True)
    parser.add_argument("--reviewed-pages", required=True)
    parser.add_argument("--status", choices=("sampled", "complete", "failed"), required=True)
    parser.add_argument("--note", action="append", default=[])
    args = parser.parse_args(argv or sys.argv[1:])

    metadata_path = args.paper_dir.resolve() / "extraction.json"
    if not metadata_path.is_file():
        raise SystemExit(f"extraction metadata missing: {metadata_path}")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    page_count = metadata.get("page_count")
    if not isinstance(page_count, int) or page_count < 1:
        raise SystemExit("invalid page_count in extraction metadata")

    parse_page_spec = load_page_parser()
    try:
        reviewed_pages = parse_page_spec(args.reviewed_pages, page_count)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    rendered_pages = set(metadata.get("render_pages", []))
    missing_renders = sorted(set(reviewed_pages) - rendered_pages)
    if missing_renders:
        raise SystemExit(f"reviewed pages were not rendered: {missing_renders}")

    metadata["visual_review"] = {
        "notes": args.note,
        "reviewed_pages": reviewed_pages,
        "status": args.status,
    }
    metadata["visual_review_status"] = args.status
    atomic_write(metadata_path, json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(metadata["visual_review"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
