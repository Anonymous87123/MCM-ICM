"""Reconcile the coded chapter jobs with the stored corpus chapter layouts.

`artifacts/language-units/<pid>.json` holds G2 chapter buckets with a
`paragraph_count` (rhetorical blocks counted inside that bucket) and a
`paragraph_functions` list. The ledger holds printed sections coded paragraph by
paragraph. The two counts are not the same measure, so this tool reports the
comparison instead of asserting equality:

  * which stored buckets have a ledger record under the normalised label,
  * stored `paragraph_count` against the ledger's group count,
  * the delta, so a systematic difference is visible rather than claimed.

Out-of-scope stored labels (abstract, references, appendix) are listed, not
counted, because the lane never codes them (README "Scope exclusions").

Usage: python -I lanes/L1-f-structure/tools/reconcile.py
"""
import collections
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L1-f-structure"

LABEL = {
    "problem-restatement": "introduction",
    "problem-analysis": "introduction",
    "literature-review": "introduction",
    "policy-letter": "recommendation",
    "sensitivity-robustness": "sensitivity-analysis",
    "model-improvement": "model-establishment",
    "algorithm": "model-establishment",
    "metrics": "model-establishment",
    "robustness-verification": "model-testing",
}
OUT_OF_SCOPE = {"abstract", "references", "appendix"}


def main() -> None:
    rows = [json.loads(line) for line in (LANE / "jobs-f.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    by_paper = collections.defaultdict(list)
    for row in rows:
        by_paper[row["paper"]].append(row)

    out = []
    totals = collections.Counter()
    for paper in sorted(by_paper):
        units = json.loads((ROOT / "artifacts" / "language-units" / (paper + ".json")).read_text(encoding="utf-8"))
        coded = collections.defaultdict(lambda: [0, 0, 0])  # groups, blocks, records
        for row in by_paper[paper]:
            bucket = coded[row["chapter"]]
            bucket[0] += row["group_count"]
            bucket[1] += row["literal_blocks"]
            bucket[2] += 1
        for ch in units.get("chapter_layouts", []):
            label = ch["chapter"]
            if label in OUT_OF_SCOPE:
                out.append([paper, label, ch.get("paragraph_count"), "", "", "", "out-of-scope"])
                totals["out_of_scope"] += 1
                continue
            mapped = LABEL.get(label, label)
            groups, blocks, records = coded.get(mapped, (0, 0, 0))
            status = "coded" if records else "MISSING"
            totals[status] += 1
            exact = "yes" if groups == ch.get("paragraph_count") else "no"
            totals["exact_" + exact] += 1
            out.append([paper, label, ch.get("paragraph_count"), mapped, groups, blocks, status + ("/exact" if exact == "yes" else "")])
        for label, (groups, blocks, records) in sorted(coded.items()):
            if label not in {LABEL.get(c["chapter"], c["chapter"]) for c in units.get("chapter_layouts", [])}:
                out.append([paper, "", "", label, groups, blocks, "no-stored-bucket"])
                totals["no_stored_bucket"] += 1

    dest = LANE / "recon" / "stored-vs-coded.tsv"
    dest.parent.mkdir(exist_ok=True)
    with dest.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["paper", "stored_label", "stored_count", "coded_label", "coded_groups", "coded_blocks", "status"])
        w.writerows(out)

    summary = {
        "papers": len(by_paper),
        "ledger_records": len(rows),
        "stored_buckets_in_scope": totals["coded"] + totals["MISSING"],
        "buckets_coded": totals["coded"],
        "buckets_missing": totals["MISSING"],
        "exact_group_equals_stored_count": totals["exact_yes"],
        "exact_share": round(totals["exact_yes"] / max(1, totals["coded"] + totals["MISSING"]), 4),
        "buckets_out_of_scope": totals["out_of_scope"],
        "coded_chapters_without_stored_bucket": totals["no_stored_bucket"],
        "row_count": len(out),
    }
    (LANE / "recon" / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
