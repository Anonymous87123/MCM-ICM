"""Print the full text of selected candidate blocks.

Usage: python -I show_blocks.py <paper_id> <chapter> <idx,idx,...>
Indices are the ones printed by chapter_digest.py with cap 90.
"""
import json
import sys

import chapter_digest as cd


def candidates(pid: str, chapter: str) -> list[tuple[int, str]]:
    units = json.loads((cd.UNITS / f"{pid}.json").read_text(encoding="utf-8")).get("units", [])
    pages = sorted({u["page"] for u in units if u.get("chapter") == chapter})
    paths = cd.page_paths(pid)
    out: list[tuple[int, str]] = []
    index = 0
    for page in range(min(pages), max(pages) + 1):
        path = paths.get(page)
        if path is None:
            continue
        for block in cd.paragraphise(path.read_text(encoding="utf-8", errors="replace")):
            out.append((page, block))
            index += 1
    return out


def main(pid: str, chapter: str, wanted: str) -> int:
    blocks = candidates(pid, chapter)
    for raw in wanted.split(","):
        i = int(raw)
        page, block = blocks[i]
        print(f"[{i:02d}] p{page}\n{block}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
