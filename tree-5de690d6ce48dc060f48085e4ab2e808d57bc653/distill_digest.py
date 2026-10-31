"""Print one exhibit's surrounding prose so the coder can pick sentences by hand.

For each exhibit in .proxy/<pid>-skel.json: its caption, every reference sentence that
names it (with page), and the body sentences of the exhibit page and the two pages
before it. Sentences are printed verbatim from the text layer, so anything copied out of
this file is guaranteed to be a substring and will pass record.py's quote check.

No judgement happens here: it does not choose a lead sentence, count interpretation, or
decide a pattern.

Usage: python -I lanes/L7-figure-census/tools/distill_digest.py <pid> [first] [last]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402


def main(argv: list[str]) -> int:
    if not argv:
        raise SystemExit("usage: distill_digest.py <pid> [first] [last]")
    pid = argv[0]
    first = int(argv[1]) if len(argv) > 1 else 1
    last = int(argv[2]) if len(argv) > 2 else 10 ** 6
    skel = json.loads((LANE / ".proxy" / f"{pid}-skel.json").read_text(encoding="utf-8"))
    out: list[str] = [f"paper {pid} digest"]
    cache: dict[int, list[str]] = {}
    for e in skel:
        n = e["doc_order"]
        if not first <= n <= last:
            continue
        page = e["page"]
        out.append("")
        out.append(f"--- exhibit {n}  p{page}  {e['kind']}  family={e['family']}  "
                   f"sec={' > '.join(e['section_path'])}")
        out.append(f"    caption[{e['caption_numbering']} {e['caption_words']}w"
                   f"/{e['caption_sentences']}s]: {e['caption_verbatim']}")
        out.append(f"    refs: first={e['first_page']} lead={e['lead_pages']} "
                   f"count={e['count']} style={e['style']}")
        for r in e["refs"]:
            out.append(f"      p{r['page']} [{r['spelling']}] {r['sentence']}")
        for p in range(max(1, page - 2), page + 2):
            if p not in cache:
                cache[p] = schema.page_units(pid, p)
            body = [s for s in cache[p] if len(schema.words(s)) >= 5]
            if not body:
                continue
            out.append(f"    page {p} body ({len(body)} sentences):")
            for s in body:
                out.append(f"      | {s}")
    text = "\n".join(out) + "\n"
    path = LANE / ".proxy" / f"{pid}-digest.txt"
    path.write_text(text, encoding="utf-8")
    print(f"{pid}: digest -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
