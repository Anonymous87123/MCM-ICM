"""Assemble quotes-a.jsonl from records-a/<paper>.json.

Each record file holds the hand-chosen quotes for one paper. This script only
validates and concatenates: job names must equal the ledger row, block_index
must run 0..n-1, quotes must be non-empty. Order follows queue.txt.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L6-a-evidence"
RECORDS = LANE / "records-a"
LEDGER = ROOT / "lanes" / "L1-f-structure" / "merge" / "snapshot" / "paragraph-ledger.jsonl"
OUT = LANE / "quotes-a.jsonl"
FIELDS = ("paper", "chapter", "block_index", "job", "quote", "page")


def ledger_map() -> dict[tuple[str, str], list[str]]:
    out: dict[tuple[str, str], list[str]] = {}
    with LEDGER.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row["type"] == "A":
                out[(row["paper"], row["chapter"])] = row["jobs"]
    return out


def main() -> int:
    expected = ledger_map()
    order = [line.split("\t")[0] for line in (LANE / "queue.txt").read_text(encoding="utf-8").splitlines() if line]
    done = {p.stem for p in RECORDS.glob("*.json")} if RECORDS.exists() else set()

    rows: list[dict] = []
    problems: list[str] = []
    for pid in order:
        if pid not in done:
            continue
        for record in json.loads((RECORDS / f"{pid}.json").read_text(encoding="utf-8")):
            key = (record["paper"], record["chapter"])
            jobs = expected.get(key)
            if jobs is None:
                problems.append(f"{pid}: no ledger row for {record['chapter']}")
                continue
            blocks = record["blocks"]
            if [b["job"] for b in blocks] != jobs:
                problems.append(f"{pid}/{record['chapter']}: job sequence differs from ledger")
                continue
            if [b["block_index"] for b in blocks] != list(range(len(jobs))):
                problems.append(f"{pid}/{record['chapter']}: block_index not 0..n-1")
                continue
            for block in blocks:
                row = {"paper": record["paper"], "chapter": record["chapter"]}
                row.update({k: block[k] for k in FIELDS[2:]})
                rows.append({k: row[k] for k in FIELDS})

    for problem in problems:
        print("PROBLEM", problem, file=sys.stderr)
    if problems:
        return 1

    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    print(f"records {len(done)} papers, rows {len(rows)} -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
