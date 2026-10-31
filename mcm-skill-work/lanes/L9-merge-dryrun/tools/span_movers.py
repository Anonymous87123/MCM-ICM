"""Rows whose level rests on the bottom rungs, with the two span routines compared directly.

`Paper.span` reads an eight-token index; `quote_blocks.span_quote` probes the squeezed text as
a substring. A block whose text layer glues two words into one token (`themodel`) fails the
first and passes the second, so the recomputation labels it `gapped` or `unverified` where the
generator, which probed substrings, labelled it `span`. This tool names those rows and the
glued token that causes each one. Read-only over the lanes; judging is done by hand in
reports/residue.md.
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

BOTTOM = ("gapped", "unverified", "ocr-only", "no-text-layer", "text-gap", "layout-only")


def glues(raw: str, tokens: set[str]) -> list[str]:
    """Adjacent block words that the text layer carries as one token."""
    words = [qb.squeeze(word) for word in qb.normalise(raw).split(" ")]
    found: list[str] = []
    for index in range(len(words) - 1):
        joined = words[index] + words[index + 1]
        if joined and joined in tokens and joined not in found:
            found.append(joined)
    return found


def main() -> int:
    levels = [json.loads(line) for line in io.open(os.path.join(L9, "reports", "quote-levels.jsonl"), encoding="utf-8") if line.strip()]
    states: dict[str, "l9.Paper"] = {}
    movers: list[dict] = []
    ocr: list[dict] = []
    gaps: list[dict] = []
    for row in levels:
        if row["type"] == "A" or row["level"] not in BOTTOM:
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
        base = {
            "lane": row["type"],
            "paper": paper,
            "chapter": row["chapter"],
            "chapter_index": int(row["chapter_index"]),
            "group_index": int(row["group_index"]),
            "block_index": int(row["block_index"]),
            "level": row["level"],
            "page": row.get("page"),
            "page_words": state.page_words.get(row.get("page")),
            "source_quote_file": row["source_quote_file"],
            "source_quote_row": int(row["source_quote_row"]),
            "raw_head": raw[:200],
        }
        if row["level"] == "text-gap":
            gaps.append(base)
        token_span = state.span(raw)
        substring_span = qb.span_quote(raw, state.squeezed)
        if substring_span and qb.has_real_words(substring_span) and not token_span:
            tokens = set(state._squeezed_tokens) if state._squeezed_tokens else {qb.squeeze(token) for token in state.tokens}
            movers.append(
                dict(
                    base,
                    token_span="",
                    substring_span=substring_span[:200],
                    substring_words=len(substring_span.split(" ")),
                    glues=glues(raw, tokens),
                    is_prose=qb.is_prose(raw, (block or {}).get("kind")),
                    ocr=state.ocr,
                )
            )
        if row["level"] in ("ocr-only", "no-text-layer"):
            ocr.append(
                dict(
                    base,
                    is_prose=qb.is_prose(raw, (block or {}).get("kind")),
                    ocr=state.ocr,
                )
            )
    path = os.path.join(L9, "reports", "span-movers.json")
    with io.open(path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump({"movers": movers, "ocr_edge": ocr, "text_gap": gaps}, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    print("movers", len(movers), "ocr_edge", len(ocr), "text_gap", len(gaps), "->", path)
    for lane in "BCDEF":
        print(lane, "movers", sum(1 for m in movers if m["lane"] == lane))
    return 0


if __name__ == "__main__":
    sys.exit(main())
