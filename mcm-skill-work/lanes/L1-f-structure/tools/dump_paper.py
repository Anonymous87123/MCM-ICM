"""Dump one paper's measured paragraphs as a compact reading list.

Usage: python -I lanes/L1-f-structure/tools/dump_paper.py <paper_id> [head] [tail]
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LAYOUT = ROOT / "lanes" / "L1-f-structure" / "layout"
OUTDIR = ROOT / "lanes" / "L1-f-structure" / ".proxy"


def main() -> None:
    paper = sys.argv[1]
    head = int(sys.argv[2]) if len(sys.argv) > 2 else 380
    tail = int(sys.argv[3]) if len(sys.argv) > 3 else 80
    rec = json.loads((LAYOUT / (paper + ".json")).read_text(encoding="utf-8"))
    lines = []
    for p in rec["paragraphs"]:
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
