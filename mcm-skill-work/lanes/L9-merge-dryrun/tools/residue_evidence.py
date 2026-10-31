"""Evidence for the residue ledger: rows whose level moves between the token index and the
substring probe, the text-gap rows, and the empty-page rows. Read-only; names candidates,
judging is done by hand in reports/residue.md.
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


def main() -> int:
    levels = [json.loads(line) for line in io.open(os.path.join(L9, "reports", "quote-levels.jsonl"), encoding="utf-8") if line.strip()]
    states: dict[str, "l9.Paper"] = {}
    movement, gaps, empty_page = [], [], []
    for row in levels:
        if row["type"] == "A":
            continue
        paper = row["paper"]
        if paper not in states:
            states[paper] = l9.Paper(row["type"], paper)
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
        token_span = state.span(raw)
        substring_span = qb.span_quote(raw, state.squeezed)
        base = {
            "lane": row["type"],
            "paper": paper,
            "chapter": row["chapter"],
            "chapter_index": int(row["chapter_index"]),
            "group_index": int(row["group_index"]),
            "block_index": int(row["block_index"]),
            "level": row["level"],
            "source_quote_file": row["source_quote_file"],
            "source_quote_row": int(row["source_quote_row"]),
            "page": row.get("page"),
            "page_words": state.page_words.get(row.get("page")),
            "ocr": state.ocr,
            "token_span": token_span,
            "substring_span": substring_span,
            "raw_head": raw[:300],
        }
        if not token_span and substring_span:
            movement.append(base)
        if row["level"] == "text-gap":
            gaps.append(base)
        if isinstance(row.get("page"), int) and state.page_words.get(row.get("page")) == 0 and row["level"] not in ("ocr-only", "no-text-layer"):
            empty_page.append(base)
    out = os.path.join(L9, "reports", "residue-evidence.json")
    with io.open(out, "w", encoding="utf-8", newline="\n") as handle:
        json.dump({"movement": movement, "text_gap": gaps, "empty_page": empty_page}, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    print("movement", len(movement), "text-gap", len(gaps), "empty-page", len(empty_page), "->", out)
    for lane in "BCDEF":
        print(lane, "movement", sum(1 for m in movement if m["lane"] == lane))
    return 0


if __name__ == "__main__":
    sys.exit(main())
