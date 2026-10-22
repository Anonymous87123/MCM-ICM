"""Recount the A evidence lane: coverage, verbatim hits, determinism.

Reads lanes/L6-a-evidence/quotes-a.jsonl and re-checks it against the ledger
snapshot and each paper's text/full.txt. Writes reports/coverage.json.
"""
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L6-a-evidence"
LEDGER = ROOT / "lanes" / "L1-f-structure" / "merge" / "snapshot" / "paragraph-ledger.jsonl"
PAPERS = ROOT / "artifacts" / "papers"
QUOTES = LANE / "quotes-a.jsonl"
REPORT = LANE / "reports" / "coverage.json"

SPACE = re.compile(r"\s+")


def fold(text: str) -> str:
    """Collapse all whitespace runs to one space, for verbatim matching."""
    return SPACE.sub(" ", text).strip()


def ledger_blocks() -> dict[tuple[str, str], list[str]]:
    out: dict[tuple[str, str], list[str]] = {}
    with LEDGER.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row["type"] == "A":
                out[(row["paper"], row["chapter"])] = row["jobs"]
    return out


def main() -> int:
    expected = ledger_blocks()
    rows: list[dict] = []
    bad_json = 0
    if QUOTES.exists():
        with QUOTES.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    bad_json += 1

    seen: dict[tuple[str, str], list[str]] = {}
    dup_index: list[str] = []
    for row in rows:
        key = (row["paper"], row["chapter"])
        seen.setdefault(key, []).append(str(row["block_index"]))
    for key, idx in seen.items():
        if len(idx) != len(set(idx)):
            dup_index.append(f"{key[0]}/{key[1]}")

    full_cache: dict[str, str] = {}
    miss_text: list[str] = []
    miss_page: list[str] = []
    for row in rows:
        pid = row["paper"]
        if pid not in full_cache:
            path = PAPERS / pid / "text" / "full.txt"
            full_cache[pid] = fold(path.read_text(encoding="utf-8", errors="replace")) if path.exists() else ""
        if fold(row["quote"]) not in full_cache[pid]:
            miss_text.append(f"{pid}#{row['chapter']}#{row['block_index']}")
        page = PAPERS / pid / "text" / "pages" / f"page-{int(row['page']):04d}.txt"
        if not page.exists():
            miss_page.append(f"{pid}#{row['page']}")

    per_paper: dict[str, dict[str, int]] = {}
    for (pid, chapter), jobs in expected.items():
        got = len(seen.get((pid, chapter), []))
        per_paper.setdefault(pid, {})[chapter] = got
        if got != len(jobs):
            print(f"MISMATCH {pid} {chapter}: {got}/{len(jobs)}", file=sys.stderr)

    total_expected = sum(len(j) for j in expected.values())
    report = {
        "papers_expected": len({p for p, _ in expected}),
        "chapters_expected": len(expected),
        "blocks_expected": total_expected,
        "rows": len(rows),
        "bad_json": bad_json,
        "duplicate_block_index": sorted(dup_index),
        "quote_not_in_fulltxt": miss_text,
        "page_file_missing": miss_page,
        "quote_hit_rate": (len(rows) - len(miss_text)) / len(rows) if rows else 0.0,
        "coverage": per_paper,
        "quotes_sha256": hashlib.sha256(QUOTES.read_bytes()).hexdigest() if QUOTES.exists() else None,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"rows {report['rows']}/{total_expected} | miss_text {len(miss_text)} | "
        f"dup_idx {len(dup_index)} | pages_missing {len(miss_page)} | hit {report['quote_hit_rate']:.4%}"
    )
    return 0 if report["rows"] == total_expected and not miss_text and not dup_index else 1


if __name__ == "__main__":
    raise SystemExit(main())
