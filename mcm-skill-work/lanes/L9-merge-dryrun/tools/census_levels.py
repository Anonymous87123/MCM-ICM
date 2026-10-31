"""The census's own level for one row, computed by the generator's ladder.

`quote_blocks.rows_for_paper` decides each row's `_match` with a closure that has no
per-row export, but its rungs are ordinary functions: exact / nfkc / squeezed on the
candidate strings, then `span_quote`, then `ocr-only` for prose under an OCR layout, then
`gapped_quote`, then `unverified`, `ocr-only`, `text-gap`. The first three rungs agree
row for row between the census and the recomputation, so this tool re-runs the ladder from
the `span` rung down on the rows where a level is in dispute and reports every row whose
census level differs from `quote-levels.jsonl`.

Read-only over the lanes; the judging stays in reports/residue.md.
"""

from __future__ import annotations

import importlib.util
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

L9 = os.path.join("lanes", "L9-merge-dryrun")
SPEC = importlib.util.spec_from_file_location("levels_l9", os.path.join("tmp", "levels_l9.py"))
l9 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(l9)
qb = l9.qb

DISPUTED = ("span", "gapped", "unverified", "ocr-only", "no-text-layer", "text-gap", "layout-only")

GAPS: dict[str, int] = {}


def census_level(raw: str, kind: str | None, state: "l9.Paper", paper: str) -> str | None:
    """The rungs below `squeezed`, in the generator's own order."""
    if state.provenance == "missing":
        return "layout-only"
    span = qb.span_quote(raw, state.squeezed)
    if span and qb.has_real_words(span):
        return "span"
    if state.ocr and qb.is_prose(raw, kind):
        return "ocr-only"
    if qb.has_real_words(raw):
        gapped = qb.gapped_quote(raw, state.tokens)
        if gapped and qb.has_real_words(gapped):
            return "gapped"
    if not qb.is_prose(raw, kind):
        return "unverified"
    if state.ocr:
        return "ocr-only"
    if paper not in GAPS:
        GAPS[paper] = qb.text_gap_blocks(state.paragraphs, state.squeezed)
    if GAPS[paper] >= qb.TEXT_GAP_MIN_BLOCKS:
        return "text-gap"
    return None


def main() -> int:
    levels = [json.loads(line) for line in io.open(os.path.join(L9, "reports", "quote-levels.jsonl"), encoding="utf-8") if line.strip()]
    states: dict[str, "l9.Paper"] = {}
    moved: list[dict] = []
    for row in levels:
        if row["type"] == "A" or row["level"] not in DISPUTED:
            continue
        paper = row["paper"]
        if paper not in states:
            states[paper] = l9.Paper(row["type"], paper)
            print(f"  {len(states)} papers", file=sys.stderr, flush=True)
        state = states[paper]
        members = state.groups.get((int(row["chapter_index"]), int(row["group_index"]))) or []
        block = None
        for member in members or [int(row["block_index"])]:
            candidate = state.blocks.get(member)
            if candidate is not None and not qb.is_stamp_only(candidate.get("text", "")):
                block = candidate
                break
        if block is None:
            block = state.blocks.get(int(row["block_index"]))
        raw = qb.strip_leading_stamp((block or {}).get("text", ""))
        kind = (block or {}).get("kind")
        theirs = census_level(raw, kind, state, paper)
        here = row["level"]
        if theirs == "ocr-only" and isinstance(row.get("page"), int) and state.page_words.get(row.get("page")) == 0:
            theirs = "no-text-layer"
        if theirs != here:
            moved.append(
                {
                    "lane": row["type"],
                    "paper": paper,
                    "chapter": row["chapter"],
                    "chapter_index": int(row["chapter_index"]),
                    "group_index": int(row["group_index"]),
                    "block_index": int(row["block_index"]),
                    "page": row.get("page"),
                    "page_words": state.page_words.get(row.get("page")),
                    "level_here": here,
                    "level_census": theirs,
                    "source_quote_file": row["source_quote_file"],
                    "source_quote_row": int(row["source_quote_row"]),
                    "token_span": state.span(raw)[:120],
                    "probe_span": qb.span_quote(raw, state.squeezed)[:120],
                    "is_prose": qb.is_prose(raw, kind),
                    "ocr": state.ocr,
                    "raw_head": raw[:200],
                }
            )
    path = os.path.join(L9, "reports", "census-diff.json")
    with io.open(path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(moved, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    print("moved", len(moved), "->", path)
    for lane in "BCDEF":
        pairs: dict[str, int] = {}
        for item in moved:
            if item["lane"] != lane:
                continue
            key = f"{item['level_census']}->{item['level_here']}"
            pairs[key] = pairs.get(key, 0) + 1
        print(lane, len([m for m in moved if m["lane"] == lane]), json.dumps(pairs, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
