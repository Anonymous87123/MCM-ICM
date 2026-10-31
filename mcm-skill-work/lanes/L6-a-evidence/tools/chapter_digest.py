"""Print a reading digest for one A chapter: candidate blocks with opening sentences.

Heuristic only: a paragraph starts on a line indented by at least ten spaces.
Nothing here classifies or writes; the operator reads the digest and quotes from
the original page files.

Usage: python -I chapter_digest.py <paper_id> <chapter> [max_chars_per_block]
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
PAPERS = ROOT / "artifacts" / "papers"
UNITS = ROOT / "artifacts" / "language-units"
LEDGER = ROOT / "lanes" / "L1-f-structure" / "merge" / "snapshot" / "paragraph-ledger.jsonl"

NOISE = re.compile(r"Team\s*#?\s*\d+|Page\s+\d+\s+of\s+\d+|精品数模资料|^.{0,3}\s*$")
START = re.compile(r"^ {10,}\S")
EQUATION = re.compile(r"\(\d+\)\s*$")


def page_paths(pid: str) -> dict[int, pathlib.Path]:
    pages = PAPERS / pid / "text" / "pages"
    out: dict[int, pathlib.Path] = {}
    for path in sorted(pages.glob("page-*.txt")):
        out[int(path.stem.split("-")[1])] = path
    return out


def is_prose(block: str) -> bool:
    """Keep running text; drop table rows, equation fragments, caption-only lines."""
    words = block.split()
    if len(words) < 8:
        return False
    alpha = sum(ch.isalpha() or ch.isspace() for ch in block) / len(block)
    if alpha < 0.72:
        return False
    if re.search(r"\S {4,}\S", block) and len(block) < 200:
        return False
    if re.match(r"^(Figure|Table|Abbreviation|Contents)\b", block):
        return False
    return True


def paragraphise(text: str) -> list[str]:
    lines = [l for l in text.splitlines() if l.strip() and not NOISE.search(l)]
    blocks: list[str] = []
    buf: list[str] = []
    for line in lines:
        if START.match(line) and buf and not EQUATION.match(buf[-1]):
            blocks.append(" ".join(buf))
            buf = [line.strip()]
        else:
            buf.append(line.strip())
    if buf:
        blocks.append(" ".join(buf))
    return blocks


def first_sentence(block: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+", block)
    out = parts[0] if parts else block
    return out if len(out) >= 40 else " ".join(parts[:2])


MATHFONT = re.compile("[-𝐀-𝟿]")


def clean_sentence(block: str) -> str:
    """First sentence of the block that is running prose, not an OCR maths sequence."""
    for part in re.split(r"(?<=[.!?:])\s+", block):
        words = part.split()
        glyphs = len(MATHFONT.findall(part))
        if len(words) >= 6 and glyphs <= 1:
            return part
    return first_sentence(block)


def main(pid: str, chapter: str, cap: int = 320) -> int:
    ledger_jobs = None
    with LEDGER.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row["type"] == "A" and row["paper"] == pid and row["chapter"] == chapter:
                ledger_jobs = row["jobs"]
    if ledger_jobs is None:
        print(f"no ledger row {pid}/{chapter}", file=sys.stderr)
        return 1

    units = json.loads((UNITS / f"{pid}.json").read_text(encoding="utf-8")).get("units", [])
    pages = sorted({u["page"] for u in units if u.get("chapter") == chapter})
    print(f"{pid} / {chapter}: jobs {len(ledger_jobs)}, unit pages {pages}")

    paths = page_paths(pid)
    index = 0
    for page in range(min(pages), max(pages) + 1):
        path = paths.get(page)
        if path is None:
            continue
        for block in paragraphise(path.read_text(encoding="utf-8", errors="replace")):
            prose = is_prose(block)
            if cap < 0 and not prose:
                index += 1
                continue
            if cap < 0:
                print(f"[{index:02d}] p{page} :: {clean_sentence(block)}")
                index += 1
                continue
            if cap:
                mark = "P" if prose else "N"
                print(f"[{index:02d}] {mark} p{page} len{len(block):>4} :: {block[:cap]}")
            else:
                print(f"[{index:02d}] p{page} :: {clean_sentence(block)}")
            index += 1
    print(f"candidate blocks {index} / jobs {len(ledger_jobs)}")
    return 0


if __name__ == "__main__":
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 320
    raise SystemExit(main(sys.argv[1], sys.argv[2], cap))
