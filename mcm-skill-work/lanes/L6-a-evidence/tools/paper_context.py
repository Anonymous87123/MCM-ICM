"""Print the reading context for one A paper: ledger jobs plus chapter span.

Read-only. Prints the ledger rows for the paper, the language-unit anchors for
the same chapter, and the full.txt span once the chapter heading is located.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LEDGER = ROOT / "lanes" / "L1-f-structure" / "merge" / "snapshot" / "paragraph-ledger.jsonl"
PAPERS = ROOT / "artifacts" / "papers"
UNITS = ROOT / "artifacts" / "language-units"

HEADINGS = {
    "model-establishment": ("model", "modelling", "modeling", "assumption", "notation"),
    "results": ("result", "finding"),
}


def main(pid: str) -> int:
    rows = []
    with LEDGER.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row["type"] == "A" and row["paper"] == pid:
                rows.append(row)
    if not rows:
        print(f"no A ledger rows for {pid}", file=sys.stderr)
        return 1

    units_path = UNITS / f"{pid}.json"
    units = json.loads(units_path.read_text(encoding="utf-8")) if units_path.exists() else {}
    unit_rows = units.get("units", [])

    for row in rows:
        chapter = row["chapter"]
        print(f"### {pid} / {chapter}: stored {row['stored_count']}, jobs {len(row['jobs'])}")
        for i, job in enumerate(row["jobs"]):
            print(f"  [{i:02d}] {job}")
        anchors = [u for u in unit_rows if u.get("chapter") == chapter]
        print(f"  units for chapter: {len(anchors)}")
        for i, u in enumerate(anchors):
            print(f"   u[{i:02d}] p{u.get('page')} :: {u.get('source_excerpt', '')[:160]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
