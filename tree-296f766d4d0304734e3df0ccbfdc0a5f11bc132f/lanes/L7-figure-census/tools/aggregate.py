"""Aggregate the distillation records. Nothing in here is typed by hand.

Every count is taken from records/*.json blocks written per exhibit, so the distributions
in reports/ can never drift from the field values. Papers that still carry only a
census_version 1 record (no place/mention/caption/geometry blocks) are counted as
un-backfilled and excluded from every distribution, never silently mixed in.

Usage: python -I lanes/L7-figure-census/tools/aggregate.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
RECORDS = LANE / "records"
REPORTS = LANE / "reports"


def bump(counter: Counter, *keys) -> None:
    for k in keys:
        counter[k] += 1


def main() -> int:
    rows, backfilled, stale = [], 0, []
    for path in sorted(RECORDS.glob("*.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        if rec.get("census_version", 1) < 2:
            stale.append(rec["paper"])
        for bucket, kind in ((rec["items"], "figure"), (rec.get("tables", []), "table")):
            for e in bucket:
                if "place" not in e or "caption" not in e or "mention" not in e:
                    continue
                if kind == "figure" and "geometry" not in e:
                    continue
                rows.append((kind, e))
        # A paper can be all tables and no figures, so an empty `items` list is not
        # the test for "not distilled": either bucket carrying a distilled row counts.
        if any("geometry" in e for e in rec["items"]) or rec.get("tables"):
            backfilled += 1

    fam = Counter()
    section_family: dict[str, Counter] = defaultdict(Counter)
    zone = Counter()
    solo = 0
    numbering = Counter()
    cap_len = Counter()
    pattern = Counter()
    lead_pages = Counter()
    unread = 0
    mismatch = []
    three_d = Counter()
    legend = Counter()
    colorbar = 0
    rstyle = Counter()
    width = Counter()
    orient = Counter()
    header_rows = Counter()
    zebra = merged = diag = units_hdr = 0
    gap = Counter()

    for kind, e in rows:
        g = e.get("geometry", {})
        family = g.get("family", "table-grid")
        p, m, c = e["place"], e["mention"], e["caption"]
        fam[family] += 1
        section_family[p["section_kind"]][family] += 1
        zone[p["page_zone"]] += 1
        solo += 1 if p["solo_page"] else 0
        numbering[c["numbering"]] += 1
        cap_len["0-8" if c["words"] <= 8 else "9-16" if c["words"] <= 16
                else "17-30" if c["words"] <= 30 else "31+"] += 1
        pattern[m["lead_pattern"]] += 1
        if m["lead_pages"] is not None:
            lead_pages["same page" if m["lead_pages"] == 0 else
                       "exhibit before text" if m["lead_pages"] < 0 else
                       "1-2 pages early" if m["lead_pages"] <= 2 else "3+ pages early"] += 1
        unread += 1 if m["read_sentences"] == 0 else 0
        if m["gap_sentences"] is not None:
            gap["0" if m["gap_sentences"] == 0 else "1-3" if m["gap_sentences"] <= 3
                else "4+"] += 1
        if kind == "figure":
            three_d[g.get("three_d", "no")] += 1
            legend[g.get("legend", "none")] += 1
            colorbar += 1 if g.get("colorbar") else 0
            if c["variable_count"] >= 3 and g.get("panel_count", 1) == 1:
                mismatch.append(f"{e['page']}:{c['variable_count']}v/{g.get('panel_count', 1)}p")
        else:
            t = e["table"]
            rstyle[t["rule_style"]] += 1
            width[t["width"]] += 1
            orient[t["orientation"]] += 1
            header_rows[t["header_rows"]] += 1
            zebra += 1 if t["zebra"] else 0
            merged += 1 if t["merged_cells"] else 0
            diag += 1 if t["diagonal_header"] else 0
            units_hdr += 1 if t["units_in_header"] else 0

    figures = sum(v for k, v in fam.items() if k != "table-grid")
    tables = fam.get("table-grid", 0)

    def ranked(counter: Counter) -> str:
        total = sum(counter.values()) or 1
        return ", ".join(f"{k} {v} ({100 * v / total:.1f}%)"
                         for k, v in counter.most_common())

    lines = [
        f"papers in records: {len(list(RECORDS.glob('*.json')))}",
        f"backfilled (schema v2): {backfilled}",
        f"stale (v1, no distillation blocks): {len(stale)}",
        "",
        f"exhibits: figures {figures}, tables {tables}, total {figures + tables}",
        f"family: {ranked(fam)}",
        f"page zone: {ranked(zone)}  | solo page: {solo}",
        f"unread exhibits (read_sentences 0): {unread}/{figures + tables} "
        f"({100 * unread / max(figures + tables, 1):.1f}%)",
        f"caption numbering: {ranked(numbering)}",
        f"caption length: {ranked(cap_len)}",
        f"lead pattern: {ranked(pattern)}",
        f"lead distance: {ranked(lead_pages)}",
        f"gap sentences to previous exhibit: {ranked(gap)}",
        "",
        f"3D: {ranked(three_d)}",
        f"legend: {ranked(legend)}  colorbar present: {colorbar}",
        f"table rule style: {ranked(rstyle)}",
        f"table width: {ranked(width)}  orientation: {ranked(orient)}",
        f"table header rows: {ranked(header_rows)}",
        f"zebra {zebra}, merged cells {merged}, diagonal header {diag}, "
        f"units in header {units_hdr}",
        f"caption naming 3+ variables on one panel: {len(mismatch)} "
        f"({', '.join(mismatch[:8])}{' ...' if len(mismatch) > 8 else ''})",
        "",
        "section kind x family:",
    ]
    for key in sorted(section_family):
        lines.append(f"  {key}: {sum(section_family[key].values())}")
    text = "\n".join(lines) + "\n"
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "distillation.txt").write_text(text, encoding="utf-8")
    (REPORTS / "distillation.json").write_text(json.dumps({
        "papers": len(list(RECORDS.glob("*.json"))),
        "backfilled": backfilled,
        "stale": stale,
        "figures": figures,
        "tables": tables,
        "family": dict(fam),
        "page_zone": dict(zone),
        "solo_page": solo,
        "unread": unread,
        "caption_numbering": dict(numbering),
        "caption_length": dict(cap_len),
        "lead_pattern": dict(pattern),
        "lead_distance": dict(lead_pages),
        "gap_sentences": dict(gap),
        "three_d": dict(three_d),
        "legend": dict(legend),
        "colorbar": colorbar,
        "table_rule_style": dict(rstyle),
        "table_width": dict(width),
        "table_orientation": dict(orient),
        "table_header_rows": dict(header_rows),
        "zebra": zebra, "merged_cells": merged, "diagonal_header": diag,
        "units_in_header": units_hdr,
        "caption_variable_mismatch": mismatch,
        "section_family": {k: dict(v) for k, v in section_family.items()},
    }, indent=1), encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
