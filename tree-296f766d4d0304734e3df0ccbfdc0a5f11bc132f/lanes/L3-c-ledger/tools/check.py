"""Check one paper's C-lane records against stored counts and evidence rules.

Rules: every chapter record must carry a job, a verbatim opening sentence and a
verbatim closing sentence per group; group_count must equal the stored
paragraph_count unless the record's note states the delta reason; the layout must
reproduce byte for byte.

Usage: python -I lanes/L3-c-ledger/tools/check.py <paper_id> [<paper_id> ...]
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L3-c-ledger"


def stored_counts(paper: str) -> dict:
    rec = json.loads((ROOT / "artifacts" / "language-units" / (paper + ".json")).read_text(encoding="utf-8"))
    out = {}
    for ch in rec.get("chapter_layouts", []):
        out[ch["chapter"]] = ch.get("paragraph_count")
    return out


def check(paper: str) -> None:
    rows = [json.loads(l) for l in (LANE / "jobs-c.jsonl").read_text(encoding="utf-8").splitlines()
            if l.strip() and json.loads(l)["paper"] == paper]
    stored = stored_counts(paper)
    print(paper, "chapters", len(rows), "stored chapters", len(stored))
    problems = []
    for r in rows:
        ch = r["chapter"]
        want = stored.get(ch)
        got = r["group_count"]
        flag = "ok" if want == got else "delta %+d" % (got - want)
        missing_ev = [u["job"] for u in r["units"] if not u.get("open") or not u.get("close")]
        if missing_ev:
            problems.append("%s: groups without open/close %s" % (ch, missing_ev))
        if want is None:
            problems.append("%s: chapter absent from stored layout" % ch)
        elif got != want and "Delta" not in r["note"] and "Stored count" not in r["note"]:
            problems.append("%s: %d groups vs stored %d and the note gives no delta reason" % (ch, got, want))
        print("  %-24s groups %2d stored %2d %-9s blocks %2d jobs %s"
              % (ch, got, want if want is not None else -1, flag, r["literal_blocks"], ",".join(r["jobs"])))
    for ch in stored:
        if ch not in {r["chapter"] for r in rows}:
            problems.append("%s: stored chapter never coded" % ch)
    print("  problems", problems if problems else "none")


def reproducibility(paper: str) -> None:
    path = LANE / "layout" / (paper + ".json")
    first = hashlib.sha256(path.read_bytes()).hexdigest()
    import subprocess
    subprocess.run([sys.executable, "-I", str(LANE / "tools" / "para_extract.py"), "layout", paper],
                   check=True, stdout=subprocess.DEVNULL)
    second = hashlib.sha256(path.read_bytes()).hexdigest()
    print("  layout sha256", "identical" if first == second else "CHANGED", first[:16])


def main() -> None:
    for paper in sys.argv[1:]:
        check(paper)
        reproducibility(paper)


if __name__ == "__main__":
    main()
