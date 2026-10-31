"""Rebuild queue.txt from the corpus manifest.

Queue = rows with problem_type == "E" and eligible_paper, ordered by
(year, relative_path, file_name), one paper per line as
"<n> <paper_id> <file_name>".

Usage: python -I lanes/L5-e-ledger/tools/build_queue.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L5-e-ledger"


def main() -> None:
    rows = [json.loads(l) for l in (ROOT / "artifacts" / "corpus" / "manifest.jsonl")
            .read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [r for r in rows if r.get("problem_type") == "E" and r.get("eligible_paper")]
    b.sort(key=lambda r: (r["year"], r["relative_path"], r["file_name"]))
    lines = ["%d %s %s" % (i, r["paper_id"], r["file_name"]) for i, r in enumerate(b, 1)]
    (LANE / "queue.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("queued", len(lines), "of", sum(1 for r in rows if r.get("problem_type") == "E"), "E rows")


if __name__ == "__main__":
    main()
