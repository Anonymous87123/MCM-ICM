#!/usr/bin/env python3
"""Create the complete page-ordered source text used by the Q129 anti-copy gate."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2019-1923964-678ee565"
PAPER_DIR = ROOT / "tmp" / "q129-extraction-v1" / PAPER_ID


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    if output.exists():
        raise SystemExit(f"refusing to overwrite Q129 source text: {output}")

    pages = [
        json.loads(line)
        for line in (PAPER_DIR / "pages.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    chunks: list[str] = []
    for expected_page, page in enumerate(pages, start=1):
        if page.get("page_index") != expected_page:
            raise SystemExit(f"non-contiguous Q129 page index at {expected_page}")
        relative = page.get("text_file")
        if not isinstance(relative, str) or not relative:
            raise SystemExit(f"missing Q129 text_file at page {expected_page}")
        chunks.append((PAPER_DIR / Path(relative)).read_text(encoding="utf-8"))

    value = "\n\f\n".join(chunks) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(value)

    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "page_count": len(pages),
                "character_count": len(value),
                "sha256": hashlib.sha256(value.encode("utf-8")).hexdigest(),
                "output": str(output),
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
