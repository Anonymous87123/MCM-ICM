"""Assemble the measurable half of each exhibit block so the hand pass only decides.

For every exhibit already recorded in records/<pid>.json this emits one entry carrying
what the geometry and the text layer already know: section path, document and page
order, page zone, area, solo page, the verbatim caption, its word and sentence count,
and the reference sentences that name it. Judgement fields (units/variables/conditions/
voice, interpretation counts, three-d, rule style, ...) are left null for the hand pass.

Nothing is written to records/ here; the output is a working file for the coder.

Usage: python -I lanes/L7-figure-census/tools/distill_skeleton.py <pid>
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

NUMBERING = [
    (re.compile(r"^Figure\s+\d+\s*:"), "Figure N:"),
    (re.compile(r"^Figure\s+\d+\s*\."), "Figure N."),
    (re.compile(r"^Figure\s+\d+(\s|$)"), "Figure N"),
    (re.compile(r"^FIGURE\s+\d+"), "FIGURE N"),
    (re.compile(r"^Fig\.?\s+\d+"), "Fig. N"),
    (re.compile(r"^Table\s+\d+\s*:"), "Table N:"),
    (re.compile(r"^Table\s+\d+\s*\."), "Table N."),
    (re.compile(r"^Table\s+\d+(\s|$)"), "Table N"),
    (re.compile(r"^TABLE\s+\d+"), "TABLE N"),
]


CAPNUM = re.compile(r"^(figure|fig\.?|table)\s*(\d+)", re.I)


def numbering_of(text: str) -> str:
    for pattern, label in NUMBERING:
        if pattern.match(text.strip()):
            return label
    return "none"


def main(argv: list[str]) -> int:
    if not argv:
        raise SystemExit("usage: distill_skeleton.py <pid>")
    pid = argv[0]
    ctx = json.loads((LANE / ".proxy" / f"{pid}-ctx.json").read_text(encoding="utf-8"))
    rec = json.loads((LANE / "records" / f"{pid}.json").read_text(encoding="utf-8"))
    by_key = {(r["page"], r["region"]): r for r in ctx["regions"]}

    out = []
    doc_order = 0
    page_seen: dict[int, int] = {}
    prev_page: int | None = None
    units = {p: schema.page_units(pid, p) for p in range(1, int(ctx["pages"][-1]) + 1)}
    merged = sorted(
        [("figure", e) for e in rec["items"]] + [("table", e) for e in rec.get("tables", [])],
        key=lambda kv: (kv[1]["page"], kv[1]["bbox"][1]))
    for kind, e in merged:
        page = e["page"]
        page_seen[page] = page_seen.get(page, 0) + 1
        doc_order += 1
        cand = [r["region"] for r in ctx["regions"] if r["page"] == page
                and abs(r["bbox"][1] - e["bbox"][1]) < 0.6]
        region = by_key[(page, cand[0])] if cand else None
        cap = e.get("caption_verbatim", "") or ""
        refs = []
        head = CAPNUM.match(cap.strip())
        # The v1 record kept only the numbering token for a bare "Figure 7" line; the
        # fresh context pass joins the caption body under it, so prefer that text.
        if head:
            kind_word = "table" if head.group(1).lower().startswith("tab") else "figure"
            want = int(head.group(2))
            fresh = [c for c in ctx["captions"]
                     if c["kind"].startswith(kind_word[:3]) and c["number"] == want
                     and c["page"] == page]
            if not fresh:
                fresh = [c for c in ctx["captions"]
                         if c["kind"].startswith(kind_word[:3]) and c["number"] == want]
            if fresh and len(fresh[0]["text"]) > len(cap):
                cap = fresh[0]["text"]
        if head:
            kind_word = "table" if head.group(1).lower().startswith("tab") else "figure"
            refs = [m for m in ctx["mentions"]
                    if m["kind"] == kind_word and m["number"] == int(head.group(2))]
        first = refs[0]["page"] if refs else None
        out.append({
            "kind": kind,
            "page": page,
            "bbox": e["bbox"],
            "family": e.get("family", "table-grid"),
            "panel_count": e.get("panel_count", 1),
            "doc_order": doc_order,
            "page_order": page_seen[page],
            "section_path": region["section_path"] if region else [],
            "section_numbered": region["section_numbered"] if region else False,
            "section_kind": region["section_kind"] if region else "other",
            "page_zone": region["page_zone"] if region else "middle",
            "area_frac": region["area_frac"] if region else round(
                (e["bbox"][3] - e["bbox"][1]) * (e["bbox"][2] - e["bbox"][0]) / 500000, 3),
            "solo_page": region["solo_page"] if region else False,
            "caption_verbatim": cap,
            "caption_numbering": numbering_of(cap),
            "caption_words": len(schema.words(cap)),
            "caption_sentences": len(schema.sentences(cap)),
            "gap_auto": (None if prev_page is None else
                         sum(len(units[p]) for p in range(prev_page + 1, page))),
            "first_page": first,
            "lead_pages": (page - first) if first is not None else None,
            "count": len(refs),
            "style": sorted({m["spelling"] for m in refs}),
            "refs": refs[:8],
            "note": e.get("note", ""),
        })
        prev_page = page
        del cand
    path = LANE / ".proxy" / f"{pid}-skel.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{pid}: {len(out)} exhibits -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
