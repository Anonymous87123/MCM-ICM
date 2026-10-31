"""Draw the hand sample for one lane and write reports/spot-check-<lane>.md.

Usage:
    python -I -X utf8 lanes/L7-quote-backfill/tools/spot_check.py <B|C|D> [--size 30]

Rows are taken at an even stride through the quote file, so the sample covers the whole
lane instead of its first paper. Every sampled row is re-read against its block and its
verification text; a row is flagged when its ladder level is a partial match or when the
quote does not end like a sentence.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import quote_blocks as qb

SUSPECT_LEVELS = {"span", "gapped", "unverified", "layout-only", "ocr-only", "text-gap"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("lane", choices=sorted(qb.LANE_DIRS))
    parser.add_argument("--size", type=int, default=30)
    args = parser.parse_args()

    path = os.path.join(qb.OUT_DIR, f"quotes-{args.lane.lower()}.jsonl")
    with open(path, encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]

    stride = max(1, len(rows) // args.size)
    sample = rows[::stride][: args.size]

    by_paper: dict[str, list[dict]] = {}
    for row in sample:
        by_paper.setdefault(row["paper"], []).append(row)

    detail: dict[str, dict] = {}
    for paper, paper_rows in by_paper.items():
        found, _ = qb.rows_for_paper(args.lane, paper)
        detail[paper] = {
            (row["chapter_index"], row["block_index"]): row for row in found
        }

    lines = [
        f"# L7 spot check — lane {args.lane}",
        "",
        f"Sample: {len(sample)} rows drawn at stride {stride} from "
        f"{len(rows)} rows in `quotes-{args.lane.lower()}.jsonl`.",
        "",
        "A row is flagged `suspect` when its ladder level is a partial match "
        "(`span`, `gapped`, `unverified`, `layout-only`, `ocr-only`, `text-gap`) or when the quote does not end "
        "on sentence punctuation. Flagged rows are the ones worth a second read.",
        "",
        "| # | paper | chapter | block | job | level | quote |",
        "|---|---|---|---|---|---|---|",
    ]
    flagged = 0
    for number, row in enumerate(sample, start=1):
        entry = detail.get(row["paper"], {}).get((row["chapter_index"], row["block_index"]), {})
        level = entry.get("_match", "?")
        quote = row["quote"]
        ending = quote.rstrip().endswith((".", "!", "?", ":", ";"))
        suspect = level in SUSPECT_LEVELS or not ending
        flagged += suspect
        shown = quote.replace("|", "/")
        if len(shown) > 150:
            shown = shown[:147] + "…"
        mark = "**suspect**" if suspect else "clean"
        lines.append(
            f"| {number} | {row['paper']} | {row['chapter']} | {row['block_index']} | "
            f"{row['job']} | {level} {mark} | {shown} |"
        )

    lines += [
        "",
        f"Flagged rows: {flagged} of {len(sample)}.",
        "",
    ]
    reports = os.path.join(qb.OUT_DIR, "reports")
    os.makedirs(reports, exist_ok=True)
    out_path = os.path.join(reports, f"spot-check-{args.lane.lower()}.md")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))
    print(f"wrote {out_path} ({len(sample)} rows, {flagged} flagged)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
