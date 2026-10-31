"""Check one paper's E-lane records against stored counts and evidence rules.

Rules: every chapter record must carry a job, a verbatim opening sentence and a
verbatim closing sentence per group; group_count must equal the stored
paragraph_count unless the record's note states the delta reason; the layout must
reproduce byte for byte.

`--coverage` instead recomputes block coverage for every paper that has a layout,
and writes reports/coverage.json: dup (block in two groups), extra (coded block the
layout does not hold), and miss (uncoded block inside the coded page range) split
by the lane's scope exclusions. `unexplained` must be empty.

Usage:
  python -I lanes/L5-e-ledger/tools/check.py <paper_id> [<paper_id> ...]
  python -I lanes/L5-e-ledger/tools/check.py --coverage
"""
import collections
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L5-e-ledger"

TOC = re.compile(r"(?:\.\s*){4,}|…{3,}|·{4,}")
CONTENTS_LABEL = re.compile(r"^(?:table\s+of\s+)?contents$", re.I)
REF_HEAD = re.compile(r"(References?|REFERENCES?|Bibliography|Work [Cc]ited)\b")
REF_ITEM = re.compile(r"\[[0-9]{1,3}\]|\bpp?\.\s*\d|\bdoi:|\bhttps?://|\b(?:19|20)\d\d\b\s*[,.]")
APPENDIX = re.compile(r"^\s*(Appendix|APPENDIX|Report on Use of AI|Use of AI)\b")
APPENDIX_TAIL = re.compile(r"(?:Appendix|APPENDIX)\s+[A-Z]\b[\w\s:]{0,40}$")
AI_LOG = re.compile(r"^\s*(Query\s*\d|Output\s*\d?)\s*:", re.I)
WM_ONLY = re.compile(r"^[\sm·.\-_|]*$")
FRONT_CHAPTERS = {"abstract", "memo"}
WM = ("微信公众号：数学模型", "微信号：MATHmodels", "关注数学模型", "MATHmodels",
      "获取更多资讯", "数学模型")


def stored_counts(paper: str) -> dict:
    rec = json.loads((ROOT / "artifacts" / "language-units" / (paper + ".json")).read_text(encoding="utf-8"))
    out = {}
    for ch in rec.get("chapter_layouts", []):
        out[ch["chapter"]] = ch.get("paragraph_count")
    return out


def check(paper: str) -> None:
    rows = [json.loads(l) for l in (LANE / "jobs-e.jsonl").read_text(encoding="utf-8").splitlines()
            if l.strip() and json.loads(l)["paper"] == paper]
    stored = stored_counts(paper)
    skip_path = LANE / "records" / (paper + ".skipped.json")
    skipped = json.loads(skip_path.read_text(encoding="utf-8")) if skip_path.exists() else {}
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
            if ch in skipped:
                print("  stored chapter %s declared not coded: %s" % (ch, skipped[ch]))
                continue
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


def clean(text: str) -> str:
    for w in WM:
        text = text.replace(w, " ")
    return re.sub(r"\s+", " ", text).strip()


def classify_miss(blocks: dict, used: set, first_coded: int, front_used: set = frozenset()) -> dict:
    """Assign one exclusion class per uncoded block, stateful in print order.

    Front matter is everything printed before the first coded body paragraph, which
    is what catches a title that continues onto page 2; the dotted contents lines win
    over both front matter and reference, because a TOC line matches the reference
    item patterns too. `front_used` holds the blocks of the abstract and memo records,
    which sit on title pages; they are excluded when locating that first body page,
    otherwise a one-page summary on page 1 would put the title sheet out of reach.
    """
    body_pages = [blocks[n]["pages"][0] for n in used
                  if blocks[n]["kind"] == "body" and n not in front_used]
    first_body_page = min(body_pages) if body_pages else None
    titles = collections.Counter(clean(p["text"]) for p in blocks.values() if clean(p["text"]))
    repeated = {t for t, c in titles.items() if c >= 3 and len(t.split()) <= 14}
    toc_blocks = {n for n, b in blocks.items()
                  if TOC.search(b["text"]) or CONTENTS_LABEL.match(clean(b["text"]))}
    contents_pages = {page for page, c in collections.Counter(blocks[n]["pages"][0] for n in toc_blocks).items()
                      if c >= 2}

    def refish(n: int) -> bool:
        text = clean(blocks[n]["text"])
        return bool(REF_HEAD.search(text) or REF_ITEM.search(text))

    order = sorted(blocks)
    ref_start = appendix_start = None
    for i, n in enumerate(order):
        if n < first_coded:
            continue
        if ref_start is None and refish(n):
            window = [m for m in order[i:i + 4] if m >= first_coded]
            if sum(1 for m in window if refish(m)) >= 2:
                ref_start = n
        if appendix_start is None:
            text = clean(blocks[n]["text"])
            if n not in toc_blocks and (APPENDIX.match(text) or AI_LOG.match(text)):
                appendix_start = n
            elif n in used and APPENDIX_TAIL.search(text):
                appendix_start = n + 1
    out = {}
    for n, block in blocks.items():
        if n in used:
            continue
        text = clean(block["text"])
        tokens = re.findall(r"[A-Za-z']+", text)
        m_share = sum(1 for t in tokens if t.lower() == "m") / max(1, len(tokens))
        if appendix_start is not None and n >= appendix_start:
            out[n] = "appendix"
        elif TOC.search(block["text"]) or block["pages"][0] in contents_pages:
            out[n] = "contents"
        elif n < first_coded or (first_body_page is not None
                                 and block["pages"][0] < first_body_page):
            out[n] = "front-matter"
        elif ref_start is not None and n >= ref_start:
            out[n] = "reference"
        elif (not text or WM_ONLY.match(text) or text in repeated
              or (len(tokens) >= 20 and m_share >= 0.8)):
            out[n] = "banner"
        else:
            out[n] = "unexplained"
    return out


def coverage() -> int:
    ledger = LANE / "jobs-e.jsonl"
    rows = [json.loads(l) for l in ledger.read_text(encoding="utf-8").splitlines() if l.strip()] \
        if ledger.exists() else []
    by_paper = collections.defaultdict(list)
    for r in rows:
        by_paper[r["paper"]].append(r)
    out = []
    for paper in sorted(by_paper):
        layout = json.loads((LANE / "layout" / (paper + ".json")).read_text(encoding="utf-8"))
        blocks = {p["n"]: p for p in layout["paragraphs"]}
        used = collections.Counter()
        front_used = set()
        for rec in by_paper[paper]:
            for g in rec["blocks"]:
                for n in g:
                    used[n] += 1
                    if rec["chapter"] in FRONT_CHAPTERS:
                        front_used.add(n)
        dup = sorted(n for n, c in used.items() if c > 1)
        extra = sorted(n for n in used if n not in blocks)
        first_page = min(r["pages"][0] for r in by_paper[paper])
        last_page = max(r["pages"][1] for r in by_paper[paper])
        first_coded = min(used) if used else 0
        classes = classify_miss(blocks, set(used), first_coded, front_used)
        miss = []
        for n in sorted(classes):
            b = blocks[n]
            if not (first_page <= b["pages"][0] <= last_page):
                continue
            if b["kind"] not in ("body", "heading", "display"):
                continue
            miss.append({"block": n, "pages": b["pages"], "kind": b["kind"],
                         "class": classes[n], "text": re.sub(r"\s+", " ", b["text"])[:90]})
        out.append({"paper": paper, "records": len(by_paper[paper]),
                    "blocks_coded": sum(used.values()), "distinct_blocks": len(used),
                    "dup": dup, "extra": extra,
                    "miss_by_class": dict(collections.Counter(m["class"] for m in miss)),
                    "miss": miss,
                    "units": sum(len(r["units"]) for r in by_paper[paper]),
                    "groups": sum(r["group_count"] for r in by_paper[paper])})
    tally = collections.Counter(k for c in out for k, v in c["miss_by_class"].items() for _ in range(v))
    report = {"papers": len(out),
              "queued": len([l for l in (LANE / "queue.txt").read_text(encoding="utf-8").splitlines() if l.strip()]),
              "duplicate_blocks": sum(len(c["dup"]) for c in out),
              "extra_blocks": sum(len(c["extra"]) for c in out),
              "miss_by_class": dict(tally), "rows": out}
    (LANE / "reports").mkdir(exist_ok=True)
    (LANE / "reports" / "coverage.json").write_text(
        json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("papers %d queued %d dup %d extra %d miss %s" % (
        report["papers"], report["queued"], report["duplicate_blocks"],
        report["extra_blocks"], report["miss_by_class"]))
    bad = [c["paper"] for c in out if c["dup"] or c["extra"] or c["miss_by_class"].get("unexplained")
           or c["units"] != c["groups"]]
    for p in bad:
        print("FAIL", p)
    return 1 if bad else 0


def main() -> None:
    if sys.argv[1:2] == ["--coverage"]:
        raise SystemExit(coverage())
    for paper in sys.argv[1:]:
        check(paper)
        reproducibility(paper)


if __name__ == "__main__":
    main()
