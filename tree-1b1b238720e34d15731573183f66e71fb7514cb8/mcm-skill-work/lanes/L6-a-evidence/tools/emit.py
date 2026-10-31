"""Write records-a/<paper>.json from hand-picked candidate block indices.

The choice of where a block starts is the operator's: this script only copies
the block's opening sentence verbatim from text/pages and attaches the ledger
job name for that position. It never decides boundaries itself.

Usage: python emit.py <paper_id> <chapter>:<idx,idx,...> [<chapter>:<idx,...>]
"""
import json
import sys

import chapter_digest as cd
import show_blocks


def ledger_jobs(pid: str, chapter: str) -> list[str]:
    with cd.LEDGER.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row["type"] == "A" and row["paper"] == pid and row["chapter"] == chapter:
                return row["jobs"]
    raise SystemExit(f"no ledger row {pid}/{chapter}")


def clean_sentences(block: str) -> list[str]:
    out = []
    for part in cd.re.split(r"(?<=[.!?:])\s+", block):
        words = part.split()
        if len(words) >= 6 and len(cd.MATHFONT.findall(part)) <= 1:
            out.append(part)
    return out or [block]


def clauses(block: str) -> list[str]:
    """Finer split for blocks that hold fewer sentences than coded jobs."""
    out = []
    for part in cd.re.split(r"(?<=[.!?:;])\s+|(?<=,)\s+", block):
        words = part.split()
        if len(words) >= 6 and len(cd.MATHFONT.findall(part)) <= 1:
            out.append(part)
    return out or clean_sentences(block)


def quote_for(block: str, k: int = 0, fine: bool = False) -> str:
    parts = clauses(block) if fine else clean_sentences(block)
    text = (parts[k] if k < len(parts) else parts[-1]).strip()
    if len(text.split()) < 6:
        text = " ".join(block.split()[:14])
    text = cd.re.sub(r"^\s*(Team\s*#?\s*\d+\s*\d*)?\s*(Figure\s*\d+\s*:)?\s*", "", text)
    words = text.split()
    while words and (len(words[0]) <= 2 or not words[0][0].isalpha()):
        words = words[1:]
    return " ".join(words) if len(words) >= 6 else text


def picks(pid: str, chapter: str, spec: str) -> list[dict]:
    """Resolve one chapter spec into blocks with verbatim quotes (no writing)."""
    indices = []
    for token in spec.split(","):
        if not token:
            continue
        base, sep, nth = token.partition("#")
        if not sep:
            base, sep, nth = token.partition("$")
        fine = sep == "$"
        if "-" in base:
            lo, hi = (int(x) for x in base.split("-"))
            indices.append(((lo, hi), int(nth) if nth else 0, fine))
        else:
            indices.append((int(base), int(nth) if nth else 0, fine))
    jobs = ledger_jobs(pid, chapter)
    if len(indices) != len(jobs):
        raise SystemExit(f"{pid}/{chapter}: {len(indices)} picked vs {len(jobs)} jobs")
    blocks = show_blocks.candidates(pid, chapter)
    out = []
    for i, ((idx, nth, fine), job) in enumerate(zip(indices, jobs)):
        if isinstance(idx, tuple):
            lo, hi = idx
            page = blocks[lo][0]
            block = " ".join(b for _, b in blocks[lo : hi + 1])
        else:
            page, block = blocks[idx]
        out.append(
            {"block_index": i, "job": job, "quote": quote_for(block, nth, fine), "page": page}
        )
    return out


def main(pid: str, specs: list[str]) -> int:
    records = []
    for spec in specs:
        chapter, raw = spec.split(":")
        out = picks(pid, chapter, raw)
        records.append({"paper": pid, "chapter": chapter, "blocks": out})

    path = cd.ROOT / "lanes" / "L6-a-evidence" / "records-a" / f"{pid}.json"
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path} ({sum(len(r['blocks']) for r in records)} blocks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1], sys.argv[2:]))
