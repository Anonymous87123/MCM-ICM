"""List the rows whose stored L7 quote differs from the ladder's own quote.

Read-only over the lanes. Reuses tmp/levels_l9.py's Paper and pick() so the ladder is
exactly the one the recomputation ran; this tool only *locates* rows and prints the two
strings side by side. Judging each row is done by hand in reports/residue.md.
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
    rows = [json.loads(line) for line in io.open(os.path.join(L9, "reports", "rows.jsonl"), encoding="utf-8") if line.strip()]
    states: dict[str, "l9.Paper"] = {}
    out = []
    for row in rows:
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
        level, expected = l9.pick(block, state)
        stored = l9.quote_text(row)
        if stored is None or not expected or stored == expected:
            continue
        block_text = (block or {}).get("text", "")
        group_text = " ".join((state.blocks.get(member) or {}).get("text", "") for member in (members or [int(row["block_index"])]))
        out.append(
            {
                "lane": row["type"],
                "paper": paper,
                "chapter": row["chapter"],
                "chapter_index": int(row["chapter_index"]),
                "group_index": int(row["group_index"]),
                "block_index": int(row["block_index"]),
                "block_members": members,
                "source_quote_file": row["source_quote_file"],
                "source_quote_row": int(row["source_quote_row"]),
                "stored_quote": stored,
                "ladder_quote": expected,
                "stored_len": len(stored),
                "ladder_len": len(expected),
                "rows_quote_level": row["quote_level"],
                "ladder_level": level,
                "record_block_text": block_text[:400],
                "block_len": len(block_text),
                "stored_in_block": stored in block_text,
                "stored_in_group": stored in group_text,
                "ladder_in_block": expected in block_text,
                "squeezed_equal": qb.squeeze(stored) == qb.squeeze(expected),
                "stored_squeezed_in_group": qb.squeeze(stored) in qb.squeeze(group_text),
            }
        )
    out.sort(key=lambda item: (item["lane"], item["paper"], item["chapter_index"], item["group_index"]))
    path = os.path.join(L9, "reports", "residue-mismatches.jsonl")
    with io.open(path, "w", encoding="utf-8", newline="\n") as handle:
        for item in out:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    print("mismatches", len(out), "->", path)
    by_lane: dict[str, int] = {}
    for item in out:
        by_lane[item["lane"]] = by_lane.get(item["lane"], 0) + 1
    print("by lane", json.dumps(by_lane, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
