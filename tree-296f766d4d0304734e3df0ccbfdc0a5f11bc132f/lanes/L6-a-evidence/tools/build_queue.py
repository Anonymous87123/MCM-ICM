"""Build queue.txt for the A evidence lane.

Deterministic: manifest (eligible A papers) x ledger snapshot (A chapter rows).
Writes one line per paper: paper_id, year, chapters, coded blocks.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "artifacts" / "corpus" / "manifest.jsonl"
LEDGER = ROOT / "lanes" / "L1-f-structure" / "merge" / "snapshot" / "paragraph-ledger.jsonl"
OUT = ROOT / "lanes" / "L6-a-evidence" / "queue.txt"


def main() -> int:
    eligible = {}
    with MANIFEST.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row.get("problem_type") == "A" and row.get("eligible_paper"):
                eligible[row["paper_id"]] = row

    rows = []
    with LEDGER.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row["type"] == "A":
                rows.append(row)

    missing = sorted({r["paper"] for r in rows} - set(eligible))
    if missing:
        print("A ledger papers not eligible in manifest:", missing, file=sys.stderr)
        return 1

    per_paper = {}
    for row in rows:
        per_paper.setdefault(row["paper"], []).append(row)

    lines = []
    for pid in sorted(per_paper, key=lambda p: (eligible[p]["year"], p)):
        chapters = per_paper[pid]
        blocks = sum(len(c["jobs"]) for c in chapters)
        chap_names = "+".join(c["chapter"] for c in chapters)
        lines.append("\t".join([pid, str(eligible[pid]["year"]), chap_names, str(blocks)]))

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    total = sum(int(l.split("\t")[3]) for l in lines)
    print(f"queue {len(lines)} papers, {total} blocks -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
