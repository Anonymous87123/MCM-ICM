"""Validate and append one paper's chapter-job records.

Input: lanes/L1-f-structure/records/<paper_id>.json, a list of chapter records:
  {"chapter": "introduction", "heading": "1 Introduction", "pages": [3, 3],
   "groups": [[11], [12], [13]], "jobs": ["route", "route", "route"],
   "note": "..."}

`groups` lists measured paragraph numbers from layout/<paper_id>.json. A group
with several numbers is one block (table rows, a heading split from its body).
Vocabularies are checked here so a typo cannot reach the ledger.

Usage: python -I lanes/L1-f-structure/tools/record.py <paper_id>
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L1-f-structure"
JOBS = {
    "route", "define", "source", "select", "derive", "compute", "read-figure",
    "compare", "check", "limit", "mechanism", "interpret", "handoff",
}
EXT = {"context", "claim"}


def first_sentence(text: str, limit: int = 260) -> str:
    """First whole sentence that actually says something (skips heading fragments)."""
    text = re.sub(r"\s+", " ", text).strip()
    for m in re.finditer(r"[.!?](?:\s|$)", text):
        sentence = text[:m.end()].strip()
        if len(re.findall(r"[A-Za-z']+", sentence)) >= 6:
            return sentence if len(sentence) <= limit else sentence[:limit].rstrip() + " …"
    return text[:limit].rstrip() + " …"


WM = (
    "微信公众号：数学模型", "微信号：MATHmodels", "关注数学模型", "MATHmodels",
    "获取更多资讯", "数学模型",
)


def clean_text(text: str) -> str:
    """Strip the corpus watermark so word counts measure paper prose."""
    text = re.sub(r"\s+", " ", text)
    for w in WM:
        text = text.replace(w, " ")
    text = re.sub(r"_{2,}", " ", text)
    text = re.sub(r"(?:\bm\b[\s.·|_-]*){3,}", " ", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def closed_sentence(text: str, limit: int = 260) -> str:
    """Last whole sentence of a block: the hand-off line to the next paragraph."""
    text = re.sub(r"\s+", " ", text).strip()
    marks = [m.end() for m in re.finditer(r"[.!?](?:\s|$)", text)]
    for end in reversed(marks):
        sentence = text[:end].strip()
        tail = sentence[sentence.rfind(". ", 0, end - 1) + 2:] if end > 1 else sentence
        tail = tail.strip()
        if len(re.findall(r"[A-Za-z']+", tail)) >= 5:
            return tail if len(tail) <= limit else "… " + tail[-limit:].lstrip()
    return text[-limit:].lstrip() if len(text) > limit else text


def base_job(job: str) -> str:
    return job.split("+close:")[0].replace("ext:", "")


def is_ext(job: str) -> bool:
    return job.startswith("ext:") or "+close:ext:" in job


def main() -> None:
    paper = sys.argv[1]
    src = LANE / "records" / (paper + ".json")
    recs = json.loads(src.read_text(encoding="utf-8"))
    layout = json.loads((LANE / "layout" / (paper + ".json")).read_text(encoding="utf-8"))
    by_n = {p["n"]: p for p in layout["paragraphs"]}

    units = json.loads((ROOT / "artifacts" / "language-units" / (paper + ".json")).read_text(encoding="utf-8"))
    stored = {ch["chapter"]: ch.get("paragraph_count") for ch in units.get("chapter_layouts", [])}
    stored_pf = {ch["chapter"]: len(ch.get("paragraph_functions", []) or []) for ch in units.get("chapter_layouts", [])}

    out = []
    for rec in recs:
        groups = rec["groups"]
        jobs = rec["jobs"]
        if len(groups) != len(jobs):
            raise SystemExit("%s %s: %d groups vs %d jobs" % (paper, rec["chapter"], len(groups), len(jobs)))
        for job in jobs:
            b = base_job(job)
            if b not in JOBS and b not in EXT:
                raise SystemExit("%s %s: bad job %r" % (paper, rec["chapter"], job))
        evidence = []
        units = []
        for g, job in zip(groups, jobs):
            missing = [n for n in g if n not in by_n]
            if missing:
                raise SystemExit("%s %s: unknown blocks %s" % (paper, rec["chapter"], missing))
            raw = " ".join(by_n[n]["text"] for n in g)
            text = clean_text(raw)
            evidence.append(first_sentence(text))
            units.append({
                "blocks": g,
                "job": job,
                "block_count": len(g),
                "words_raw": len(re.findall(r"[A-Za-z']+", raw)),
                "words_clean": len(re.findall(r"[A-Za-z']+", text)),
                "open": first_sentence(text),
                "close": closed_sentence(text),
            })

        vacant = {}
        if not groups:
            if not rec.get("vacant_units"):
                raise SystemExit("%s %s: empty groups without vacated units" % (paper, rec["chapter"]))
            page_blocks = [n for n, p in by_n.items()
                           if p.get("page") in range(rec["pages"][0], rec["pages"][1] + 1)]
            folded = rec.get("folded_into")
            if folded is not None:
                if folded not in by_n:
                    raise SystemExit("%s %s: folded_into %r missing" % (paper, rec["chapter"], folded))
                page_blocks = [n for n in page_blocks if n != folded]
            if page_blocks:
                raise SystemExit("%s %s: vacated but text layer has blocks %s"
                                 % (paper, rec["chapter"], sorted(page_blocks)))
            vacant = {
                "vacant": True,
                "vacated_units": rec["vacant_units"],
                "vacant_reason": rec["vacant_reason"],
                "text_layer_blocks_on_pages": [],
            }
            if folded is not None:
                vacant["folded_into"] = folded
        out.append({
            "paper": paper,
            "type": "F",
            "chapter": rec["chapter"],
            "heading": rec["heading"],
            "pages": rec["pages"],
            "stored_count": stored_pf.get(rec["chapter"], stored.get(rec["chapter"])),
            "literal_blocks": sum(len(g) for g in groups),
            "group_count": len(groups),
            "blocks": groups,
            "jobs": jobs,
            "ext": sorted({base_job(j) for j in jobs if is_ext(j) or base_job(j) in EXT}),
            "evidence": evidence,
            "units": units,
            "note": rec["note"],
            **vacant,
        })

    ledger = LANE / "jobs-f.jsonl"
    kept = []
    if ledger.exists():
        for line in ledger.read_text(encoding="utf-8").splitlines():
            if line.strip() and json.loads(line)["paper"] != paper:
                kept.append(line)
    new_bytes = "\n".join(json.dumps(r, ensure_ascii=False) for r in out)
    ledger.write_text("\n".join(kept + [new_bytes]) + "\n", encoding="utf-8")

    notes = ["# %s — chapter jobs (hand-coded)" % paper, ""]
    for r in out:
        notes.append("## %s — %s (pp. %d-%d, %d blocks)" % (
            r["chapter"], r["heading"], r["pages"][0], r["pages"][1], r["group_count"]))
        notes.append("")
        notes.append("`" + " → ".join(r["jobs"]) + "`")
        notes.append("")
        notes.append(r["note"])
        notes.append("")
    (LANE / "notes" / (paper + ".md")).write_text("\n".join(notes), encoding="utf-8")
    blocks = sum(len(g) for r in out for g in r["blocks"])
    words = sum(u["words_clean"] for r in out for u in r["units"])
    print("wrote %s %d chapters, %d groups, %d blocks, %d clean words"
          % (paper, len(out), sum(r["group_count"] for r in out), blocks, words))


if __name__ == "__main__":
    main()
