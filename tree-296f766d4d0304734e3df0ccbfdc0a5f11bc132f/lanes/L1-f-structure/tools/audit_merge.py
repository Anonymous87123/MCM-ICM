"""Merge-and-promotion audit for the paragraph-job ledger (writes only under merge/).

Inputs, read-only:
  lanes/L1-f-structure/jobs-f.jsonl        F: 48 papers, 672 chapter records (hand-coded)
  artifacts/paragraph-ledger.jsonl         A-E manual rows plus a stale F row set
  artifacts/language-units/P-*.json        stored chapter layouts and paragraph_functions
  tmp/para-taxonomy.md                     the 13-job vocabulary and the promotion rule

Outputs, all under lanes/L1-f-structure/merge/:
  jobs-by-type.csv      per type per job: blocks, share of that type's blocks, papers
  metrics.json          every number quoted in report.md
  taxonomy-sha256.txt   hashes of the four inputs this run consumed

The promotion rule (tmp/para-taxonomy.md, unchanged) is:
  a job sequence enters the skill only when it holds in >= 60% of that type's
  read papers, in >= 4 of 6 types at the same position, and every claim carries
  one verbatim sentence from a paper read in full.

`unresolved` is a ledger token, not a job: it marks a block the earlier pass could
not name. Such tokens are dropped from a sequence and the row is flagged, so a
dropped token cannot silently shift later positions.

Usage: python -I lanes/L1-f-structure/tools/audit_merge.py
"""
import collections
import csv
import hashlib
import json
import pathlib
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L1-f-structure"
OUT = LANE / "merge"

JOBS = ["route", "define", "source", "select", "derive", "compute", "read-figure",
        "compare", "check", "limit", "mechanism", "interpret", "handoff"]
TYPES = list("ABCDEF")
EXTRAS = ["context", "claim"]
LABEL = {  # stored corpus label -> ledger label (same map as tools/reconcile.py)
    "problem-restatement": "introduction", "problem-analysis": "introduction",
    "literature-review": "introduction", "policy-letter": "recommendation",
    "sensitivity-robustness": "sensitivity-analysis",
    "model-improvement": "model-establishment", "algorithm": "model-establishment",
    "metrics": "model-establishment", "robustness-verification": "model-testing",
}
OUT_OF_SCOPE = {"abstract", "references", "appendix"}  # ext:context / ext:claim, allowed only as a job suffix
ALLOWED = set(JOBS) | set(EXTRAS)


def base(job: str) -> str:
    return job.split("+close:")[0].replace("ext:", "")


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


SNAP = OUT / "snapshot" / "paragraph-ledger.jsonl"


def load_sequences():
    """One job sequence per (type, chapter, paper), print order."""
    rows = collections.defaultdict(list)  # (type, chapter, paper) -> [(row_index, [jobs])]
    source = SNAP if SNAP.exists() else ROOT / "artifacts" / "paragraph-ledger.jsonl"
    ledger = [json.loads(l) for l in source.read_text(encoding="utf-8").splitlines() if l.strip()]
    ledger_flags = []
    for i, r in enumerate(ledger):
        if r["type"] == "F":
            continue  # stale F rows: jobs-f.jsonl is authoritative
        dropped = [j for j in r["jobs"] if j == "unresolved"]
        seq = [base(j) for j in r["jobs"] if j != "unresolved"]
        rows[(r["type"], r["chapter"], r["paper"])].append((i, seq))
        if dropped:
            ledger_flags.append({"paper": r["paper"], "chapter": r["chapter"], "dropped": len(dropped)})
    f_rows = [json.loads(l) for l in (LANE / "jobs-f.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, r in enumerate(f_rows):
        rows[("F", r["chapter"], r["paper"])].append((i, [base(j) for j in r["jobs"]]))

    seqs = collections.defaultdict(list)  # (type, chapter) -> [(paper, seq)]
    for (t, ch, paper), parts in rows.items():
        parts.sort()
        seqs[(t, ch)].append((paper, [j for _, s in parts for j in s]))
    snapshot = {
        "ledger_rows": len(ledger),
        "ledger_rows_by_type": dict(collections.Counter(r["type"] for r in ledger)),
        "jobs_f_records": len(f_rows),
        "source": str(source.relative_to(ROOT)),
        "note": ("artifacts/paragraph-ledger.jsonl is appended by another session while this audit runs, so "
                 "the ledger was frozen to merge/snapshot/paragraph-ledger.jsonl; every number here describes "
                 "that frozen copy, whose sha256 is in taxonomy-sha256.txt."),
    }
    return seqs, ledger_flags, snapshot


def main() -> None:
    OUT.mkdir(exist_ok=True)
    seqs, flags, snapshot = load_sequences()

    # ---- 1. vocabulary alignment per type -------------------------------------
    per_type = collections.defaultdict(lambda: {"blocks": 0, "papers": set(), "chapters": 0, "jobs": collections.Counter(),
                                                "papers_by_job": collections.defaultdict(set)})
    for (t, ch), papers in seqs.items():
        agg = per_type[t]
        agg["chapters"] += len(papers)
        for paper, seq in papers:
            agg["papers"].add(paper)
            agg["blocks"] += len(seq)
            for j in seq:
                agg["jobs"][j] += 1
                agg["papers_by_job"][j].add(paper)

    csv_rows = []
    for t in TYPES:
        agg = per_type[t]
        for j in JOBS + EXTRAS:
            n = agg["jobs"][j]
            csv_rows.append([t, j, n, round(n / max(1, agg["blocks"]), 4), len(agg["papers_by_job"][j])])
        unknown = {j: n for j, n in agg["jobs"].items() if j not in ALLOWED}
        if unknown:
            raise SystemExit("type %s: jobs outside the taxonomy %s" % (t, unknown))
    with (OUT / "jobs-by-type.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["type", "job", "blocks", "share_of_type_blocks", "papers_using_it"])
        w.writerows(csv_rows)

    vocab = {
        t: {
            "papers": len(per_type[t]["papers"]),
            "chapter_records": per_type[t]["chapters"],
            "blocks": per_type[t]["blocks"],
            "jobs_used": sorted(per_type[t]["jobs"]),
            "jobs_never_used": [j for j in JOBS if j not in per_type[t]["jobs"]],
            "top": [[j, n] for j, n in per_type[t]["jobs"].most_common(5)],
        }
        for t in TYPES
    }

    # ---- 2. stored paragraph_functions: template strings or real labels? ------
    pf = {}
    for t in TYPES:
        total = distinct = 0
        counts = collections.Counter()
        per_chapter = []
        for path in sorted((ROOT / "artifacts" / "language-units").glob("P-%s-*.json" % t)):
            ul = json.loads(path.read_text(encoding="utf-8"))
            for ch in ul.get("chapter_layouts", []):
                strings = ch.get("paragraph_functions") or []
                total += len(strings)
                distinct += len(set(strings))
                counts.update(strings)
                if strings:
                    per_chapter.append({"paper": path.stem, "chapter": ch["chapter"], "n": len(strings),
                                        "distinct": len(set(strings))})
        pf[t] = {
            "values": total,
            "distinct": distinct,
            "distinct_share": round(distinct / max(1, total), 4),
            "top_repeated": [[s, n] for s, n in counts.most_common(3)],
            "chapters": len(per_chapter),
            "chapters_with_repeats": sum(1 for c in per_chapter if c["distinct"] < c["n"]),
            "min_distinct": min((c["distinct"] for c in per_chapter), default=0),
        }

    # ---- 3. promotion test ----------------------------------------------------
    def modal(seq_list):
        pos = []
        for i in range(max(len(s) for s in seq_list)):
            v = [s[i] for s in seq_list if len(s) > i]
            if not v:
                break
            pos.append(collections.Counter(v).most_common(1)[0][0])
        return pos

    def evaluate(ch, cand):
        support = {}
        for t in TYPES:
            papers = [(p, sq) for p, sq in seqs.get((t, ch), []) if sq]
            if not papers:
                support[t] = None
                continue
            hit = [p for p, sq in papers if len(sq) >= len(cand) and sq[:len(cand)] == cand]
            support[t] = {"hit": len(hit), "of": len(papers), "share": round(len(hit) / len(papers), 4),
                          "miss_example": next((p for p, _ in papers if p not in hit), None)}
        held = [t for t, v in support.items() if v and v["share"] >= 0.6]
        return support, held

    tests = []
    for ch in sorted({c for _, c in seqs}):
        pool_all = [(t, p, sq) for t in TYPES for p, sq in seqs.get((t, ch), []) if sq]
        pool = [sq for _, _, sq in pool_all]
        candidates = collections.OrderedDict()
        if len(pool) >= 6:
            full = modal(pool)
            kept = []
            for i, j in enumerate(full):
                v = [sq[i] for sq in pool if len(sq) > i]
                if sum(1 for x in v if x == j) / len(v) < 0.6:
                    break
                kept.append(j)
            candidates["pool-modal prefix (>=60% within itself)"] = kept
            candidates["pool-modal first position"] = full[:1]
        for t in TYPES:
            own = [sq for tt, _, sq in pool_all if tt == t]
            if len(own) >= 2:
                candidates["%s-modal first position" % t] = modal(own)[:1]
        options = []
        for name, cand in candidates.items():
            if not cand:
                options.append({"name": name, "candidate": [], "types_held": [], "support": {}, "pass": False})
                continue
            support, held = evaluate(ch, cand)
            options.append({"name": name, "candidate": cand, "types_held": held,
                            "support": support, "pass": len(held) >= 4})
        best = max(options, key=lambda o: (len(o["types_held"]), len(o["candidate"]))) if options else             {"name": "none", "candidate": [], "types_held": [], "support": {}, "pass": False}
        tests.append({"chapter": ch, "pool_papers": len(pool),
                      "types_present": [t for t in TYPES if seqs.get((t, ch))],
                      "best": best, "all_candidates": options,
                      "pass": best["pass"]})

    # first-position agreement, the weakest possible form of "same position"
    first = {}
    for ch in sorted({c for _, c in seqs}):
        pool = [sq for t in TYPES for _, sq in seqs.get((t, ch), []) if sq]
        if not pool:
            continue
        cand = collections.Counter(sq[0] for sq in pool).most_common(1)[0][0]
        first[ch] = {"candidate": cand, "types": {
            t: {"hit": sum(1 for _, sq in seqs[(t, ch)] if sq and sq[0] == cand),
                "of": sum(1 for _, sq in seqs[(t, ch)] if sq)}
            for t in TYPES if seqs.get((t, ch))}}

    # within-type agreement: does a type agree with itself?
    agreement = {}
    for (t, ch), papers in sorted(seqs.items()):
        v = [(p, sq) for p, sq in papers if sq]
        if len(v) < 3:
            continue
        counts = collections.Counter(tuple(sq) for _, sq in v)
        top, n = counts.most_common(1)[0]
        agreement["%s/%s" % (t, ch)] = {
            "papers": len(v), "modal_sequence_papers": n, "share": round(n / len(v), 4),
            "modal_sequence_length": len(top), "median_length": int(statistics.median(len(sq) for _, sq in v)),
            "length_range": [min(len(sq) for _, sq in v), max(len(sq) for _, sq in v)],
        }

    # ---- 4. coverage and blockage --------------------------------------------
    manifest = [json.loads(l) for l in (ROOT / "artifacts" / "corpus" / "manifest.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    eligible = collections.Counter(r["problem_type"] for r in manifest if r.get("eligible_paper"))
    coverage = {}
    for t in TYPES:
        coded = {p for (tt, _ch), papers in seqs.items() if tt == t for p, _ in papers}
        missing_chapters = []
        for path in sorted((ROOT / "artifacts" / "language-units").glob("P-%s-*.json" % t)):
            if path.stem not in coded:
                continue
            ul = json.loads(path.read_text(encoding="utf-8"))
            have = {ch_label for (tt, ch_label), papers in seqs.items()
                    if tt == t and any(p == path.stem for p, _ in papers)}
            for ch in ul.get("chapter_layouts", []):
                label = ch["chapter"]
                if label in OUT_OF_SCOPE:
                    continue
                if LABEL.get(label, label) not in have:
                    missing_chapters.append([path.stem, label])
        coverage[t] = {
            "eligible": eligible.get(t, 0),
            "papers_with_manual_jobs": len(coded),
            "papers_without_manual_jobs": eligible.get(t, 0) - len(coded),
            "chapters_missing_on_coded_papers": len(missing_chapters),
            "chapter_gaps_examples": missing_chapters[:12],
        }

    # ---- 5. per-paper blockage list ------------------------------------------
    # F bucket gaps carry the reconciliation verdict, where one exists
    # (reconcile/bucket-decisions.jsonl: a covered elsewhere, c no such section).
    decided = {}
    dec_path = LANE / "reconcile" / "bucket-decisions.jsonl"
    if dec_path.exists():
        for line in dec_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                decided[(d["paper"], d["stored_label"])] = d["class"]
    blocked_rows = []
    gap_by_type = {}
    for t in TYPES:
        coded = {p for (tt, _ch), papers in seqs.items() if tt == t for p, _ in papers}
        per_paper = {}
        for path in sorted((ROOT / "artifacts" / "language-units").glob("P-%s-*.json" % t)):
            ul = json.loads(path.read_text(encoding="utf-8"))
            have = {ch_label for (tt, ch_label), papers in seqs.items()
                    if tt == t and any(p == path.stem for p, _ in papers)}
            missing = [ch["chapter"] for ch in ul.get("chapter_layouts", [])
                       if ch["chapter"] not in OUT_OF_SCOPE and LABEL.get(ch["chapter"], ch["chapter"]) not in have]
            if missing:
                per_paper[path.stem] = missing
        counter = collections.Counter(label for labels in per_paper.values() for label in labels)
        gap_by_type[t] = {"papers_with_gaps": len(per_paper), "chapter_gap_counts": dict(counter.most_common())}
        for paper, labels in sorted(per_paper.items()):
            verdicts = " | ".join(decided.get((paper, label), "") for label in labels)
            blocked_rows.append([t, paper, len(labels), " | ".join(labels),
                                 "no manual row" if paper not in coded else "partial",
                                 verdicts])
    with (OUT / "blocked-papers.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["type", "paper", "chapters_missing", "chapters", "state", "bucket_class"])
        w.writerows(blocked_rows)

    metrics = {
        "inputs_sha256": {
            "jobs-f.jsonl": sha(LANE / "jobs-f.jsonl"),
            "paragraph-ledger.jsonl": sha(SNAP),
            "para-taxonomy.md": sha(ROOT / "tmp" / "para-taxonomy.md"),
        },
        "vocabulary": vocab,
        "paragraph_functions": pf,
        "promotion": {"tests": tests, "first_position": first, "within_type_agreement": agreement},
        "coverage": coverage,
        "blockage": gap_by_type,
        "snapshot": snapshot,
        "ledger_rows_with_unresolved": flags,
    }
    (OUT / "metrics.json").write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = ["sha256  path"]
    for rel in ("tmp/para-taxonomy.md", "lanes/L1-f-structure/jobs-f.jsonl",
                "lanes/L1-f-structure/merge/snapshot/paragraph-ledger.jsonl", "artifacts/corpus/manifest.jsonl",
                "lanes/L1-f-structure/tools/audit_merge.py"):
        lines.append("%s  %s" % (sha(ROOT / rel), rel))
    (OUT / "taxonomy-sha256.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({"tests": [(t["chapter"], t["best"]["candidate"], t["best"]["types_held"], t["pass"]) for t in tests],
                      "coverage": {t: (v["papers_with_manual_jobs"], v["eligible"]) for t, v in coverage.items()}},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
