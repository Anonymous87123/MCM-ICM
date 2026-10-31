"""Dump one paper's measured paragraphs as a compact reading list.

Usage: python -I lanes/L2-d-ledger/tools/dump_paper.py <paper_id> [head] [tail]
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LAYOUT = ROOT / "lanes" / "L2-d-ledger" / "layout"
OUTDIR = ROOT / "lanes" / "L2-d-ledger" / ".proxy"


def main() -> None:
    paper = sys.argv[1]
    head = int(sys.argv[2]) if len(sys.argv) > 2 else 380
    tail = int(sys.argv[3]) if len(sys.argv) > 3 else 80
    lo = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    hi = int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 6
    rec = json.loads((LAYOUT / (paper + ".json")).read_text(encoding="utf-8"))
    lines = []
    for p in rec["paragraphs"]:
        if not (lo <= p["pages"][0] <= hi):
            continue
        text = p["text"]
        if len(text) > head + tail:
            shown = text[:head] + " …… " + text[-tail:]
        else:
            shown = text
        lines.append("[%d] %s p%s-%s w=%d :: %s" % (
            p["n"], p["kind"][:4], p["pages"][0], p["pages"][1], p["words"], shown))
    OUTDIR.mkdir(parents=True, exist_ok=True)
    path = OUTDIR / (paper + "-read.txt")
    path.write_text("\n".join(lines), encoding="utf-8")
    print(path, "blocks", len(lines))


if __name__ == "__main__":
    main()
