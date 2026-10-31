"""Print every prose candidate block of a chapter with its clause splits.

Read-only helper for the operator: use it to choose which clause of which
candidate block supplies the quote for each coded job.

Usage: python -X utf8 inventory.py <paper_id> <chapter> [min_words] [width]
"""
import sys

import chapter_digest as cd
import emit
import show_blocks


def main(pid: str, chapter: str, min_words: int = 6, width: int = 110) -> int:
    blocks = show_blocks.candidates(pid, chapter)
    total = 0
    for i, (page, block) in enumerate(blocks):
        parts = emit.clauses(block)
        if not cd.is_prose(block) and len(parts) < 2:
            continue
        usable = [p for p in parts if len(p.split()) >= min_words]
        if not usable:
            continue
        total += len(usable)
        print(f"[{i:02d}] p{page} clauses {len(usable)}")
        for j, part in enumerate(parts):
            flag = " " if len(part.split()) >= min_words else "-"
            print(f"   {flag}${j} {part[:width]}")
    print(f"usable clauses {total}")
    return 0


if __name__ == "__main__":
    width = int(sys.argv[4]) if len(sys.argv) > 4 else 110
    raise SystemExit(main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 6, width))
