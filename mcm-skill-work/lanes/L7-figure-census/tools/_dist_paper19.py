"""Hand pass for P-B-2011-11759-ee4be862 (radio-repeater coverage for search and rescue, 51 pages).

The paper prints twenty-four numbered figures, three uncaptioned parameter tables and two
uncaptioned result tables. Every family below was read off a cropped page proxy; the
geometry pass only supplied the rectangles.

Four things drive the record:

* Family split. Sixteen of the numbered figures are repeater-placement plots on a Miles x
  Miles frame: a grey field with the potential-user cloud, red and green repeater dots, and
  coverage circles. They look like scatter plots but the frame is geographic, so they are
  map-or-plan-view. Four are parity diagrams (circles bearing + or - joined by thin links),
  which are node-link-network. Two are model flow charts.
* Two figures are declared and never measured. Figures 3 and 9 ("Surface Plot of Users",
  p15 and p19) were pasted into the PDF as a stack of twelve 17 pt horizontal image strips
  plus a 4 pt tail; `fig_extract` drops any box thinner than 25 pt, so the montage leaves no
  measured region and cannot be recorded against one. They stay unresolved, stated here and
  in the README, rather than being given a bbox the tool never measured.
* Appendix A (p29-p35) reprints seven body figures at full page as Figures 18-24. They are
  separate numbered exhibits with their own captions, so they are recorded as separate items
  even though their artwork repeats Figures 4, 6, 7, 10, 12, 13 and 15.
* Caption strings. `context_extract` glues the following body sentence onto a caption when
  the caption line has no full stop (Figure 7 on p18, Figure 17 on p25). The record quotes
  the printed caption line only.

Usage: python -I tools/_dist_paper19.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2011-11759-ee4be862"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}
MENTIONS = CTX["mentions"]

CORPUS = LANE.parents[2] / "MCM-ICM-master"
QUEUE = LANE / "queue.txt"
PDF = next(
    CORPUS.joinpath(*line.split()[2].split("/"))
    for line in QUEUE.read_text(encoding="utf-8").splitlines()
    if line.strip() and line.split()[1] == PID)

HEADINGS: list[tuple[int, float, str, str, str]] = []


def load_headings() -> None:
    """Attach the printed y of each heading, so a region is placed by position, not by the
    extracted heading index (which carries the contents page on p2-p3)."""
    import pymupdf

    doc = pymupdf.open(PDF)
    for h in CTX["headings"]:
        if h["page"] < 4:
            continue
        num, title = h["number"].strip(), h["title"].strip()
        if num and not re.match(r"^\d+(\.\d+)*$", num):
            continue
        y = None
        for block in doc[h["page"] - 1].get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                text = schema.norm(" ".join(s["text"] for s in line["spans"]))
                if num and text == num:
                    y = line["bbox"][1]
                elif not num and schema.norm(title).lower() in text.lower():
                    y = line["bbox"][1]
        if y is not None:
            HEADINGS.append((h["page"], y, num, title, h["kind"]))
    doc.close()


def place_for(page: int, reg: int) -> dict:
    y0 = REG[(page, reg)][1]
    before = [h for h in HEADINGS if h[0] < page or (h[0] == page and h[1] <= y0)]
    if not before:
        raise SystemExit(f"no heading before p{page} r{reg}")
    _, _, num, title, kind = before[-1]
    path = [f"{h[2]} {h[3]}".strip() for h in before
            if h[2] and (h[2] == num or num.startswith(h[2] + "."))]
    if not num:
        path = [title]
    same = [k for k in EXHIBITS if k[0] == page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def raw_lines(page: int) -> list[str]:
    return (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()


def page_caption(page: int, number: int, kind: str = "Figure") -> str:
    """The printed caption line itself.

    In this paper every caption sits on one line of its own, and the line carries no final
    full stop, so the blob that `context_extract` reports for it has the next body sentence
    glued on. Taking the line alone keeps the quote to what is printed as the caption.
    """
    pat = re.compile(rf"^\s*{kind}\s+{number}(?!\d)")
    for line in raw_lines(page):
        if pat.match(line):
            return schema.norm(line)
    raise SystemExit(f"no {kind} {number} caption on page {page}")


PROSE = re.compile(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}")
AXIS_TICK = re.compile("−")
TABLE_CELL = re.compile(r"\d+\.\d+")
INLINE_CAPTION = re.compile(r"(Figure|Table)\s+\d+\s*[:.]")
RUNHEAD = re.compile(r"Control\s+Number:\s*\d+\s+Page\s+\d+\s+of\s+\d+\s*", re.I)


def lead_sentence(number: int, kind: str) -> tuple[str, str]:
    pat = re.compile(r"[Ff]igure\s+" + str(number) if kind == "figure"
                     else r"[Tt]able\s+" + str(number))
    for page in range(1, LAYOUT["page_count"] + 1):
        for unit in schema.page_units(PID, page):
            unit = RUNHEAD.sub("", unit)
            if not pat.search(unit) or INLINE_CAPTION.match(unit):
                continue
            hit = next((s for s in schema.sentences(unit)
                        if pat.search(s) and PROSE.search(s)
                        and AXIS_TICK.search(s) is None
                        and len(TABLE_CELL.findall(s)) < 3
                        and INLINE_CAPTION.search(s) is None
                        and s.count("(") < 2), "")
            if not hit:
                continue
            parts = hit.split()
            text = " ".join(parts[:schema.MAX_QUOTE_WORDS])
            while len(schema.words(text)) > schema.MAX_QUOTE_WORDS:
                parts = parts[:-1]
                text = " ".join(parts[:schema.MAX_QUOTE_WORDS])
            low = text.lower()
            if re.search(r"\(figure\s+\d+", low) or "(see figure" in low:
                pattern = "parenthetical"
            elif "as shown" in low:
                pattern = "as-shown-in"
            elif re.match(r"^figure\s+\d+\s+shows", low):
                pattern = "figure-n-shows"
            else:
                pattern = "direct"
            return text, pattern
    return "", "none"


def mention(number: int | None, page: int, kind: str = "figure") -> dict:
    blank = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
             "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
             "read_sentences": 0, "gap_sentences": None}
    if number is None:
        return blank
    ms = [m for m in MENTIONS if m["number"] == number and m["kind"] == kind]
    if not ms:
        return blank
    first = min(m["page"] for m in ms)
    sent, pattern = lead_sentence(number, kind)
    label = "Figure" if kind == "figure" else "Table"
    styles = sorted({m["spelling"] for m in ms if m["page"] == page})
    return {"first_page": first, "lead_pages": page - first,
            "style": styles or [f"{label} {number}"], "count": len(ms),
            "lead_sentence": sent, "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": 1 if sent else 0, "gap_sentences": abs(page - first)}


def caption_block(text: str, position: str = "below") -> dict:
    numbering = "none"
    m = re.match(r"^(Figure|Table)\s+(\d+)([:.])?", text)
    if m:
        numbering = {(False, ":"): "Figure N:", (False, "."): "Figure N.",
                     (False, ""): "Figure N", (True, ":"): "Table N:",
                     (True, "."): "Table N.", (True, ""): "Table N"}[
                         (m.group(1) == "Table", m.group(3) or "")]
    vars_ = 1 if re.search(r"[A-Za-z]\s*[=~]", text) or "_" in text else 0
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": bool(re.search(r"\b(m|m/s|degree|degrees|%)\b", text)),
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": bool(re.search(r"\b(under|with|without|fixed|default|varying)\b", text)),
        "concludes": bool(re.search(r"\b(which|so that|therefore)\b", text)),
        "voice": "none",
        "position": position,
    }


def figure(page: int, reg: int, family: str, panels: int, conf: str, cap: str | None, *,
           layout: str = "1", legend: str = "none", number: int | None = None,
           labels: bool = False, note: str = "", shared_axes: bool = False) -> dict:
    cap_text = cap or ""
    return {
        "page": page,
        "bbox": REG[(page, reg)],
        "family": family,
        "confidence": conf,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": "text-layer" if cap_text else "none",
        "note": note,
        "place": place_for(page, reg),
        "mention": mention(number, page),
        "caption": caption_block(cap_text),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared_axes,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": True,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, rows: int, cols: int, *, header_rows: int = 1,
          numeric: int = 0, text: int = 2, width: str = "column", note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, reg)],
        "caption_verbatim": "",
        "caption_source": "none",
        "note": note,
        "place": place_for(page, reg),
        "mention": mention(None, page, "table"),
        "caption": caption_block(""),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": "boxed",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text,
            "width": width,
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    }


ITEMS: list[dict] = []
TABLES: list[dict] = []
RULES: list[str] = []

# Every measured region of this paper is an exhibit: 22 figure items (one per numbered
# figure that the geometry pass saw) and 5 uncaptioned tables.
EXHIBITS: list[tuple[int, int]] = [
    (6, 1), (7, 1), (11, 1), (12, 1), (16, 1), (16, 2), (17, 1), (17, 2),
    (18, 1), (18, 2), (20, 1), (20, 2), (21, 1), (21, 2), (22, 1), (23, 1),
    (24, 1), (24, 2), (25, 1), (25, 2),
    (29, 1), (30, 1), (31, 1), (32, 1), (33, 1), (34, 1), (35, 1),
]

PLACEMENT = "map-or-plan-view"
KIND = "flowchart-or-schematic"


def build() -> str:
    load_headings()

    ITEMS.extend([
        figure(6, 1, KIND, 1, "high", page_caption(6, 1), number=1,
               note="rounded boxes joined by arrows: Create and Score Clusters, then Place 1st "
                    "Repeater (Open), then the decision Enough Users & Channels? whose yes branch "
                    "reaches End of Method and whose no branch reaches Enough Channels?; a yes "
                    "there goes to Find Optimal Direction and Place New Repeater (Open) back into "
                    "the first decision, a no goes to Add Repeater (PL) and back up the left side. "
                    "Decision nodes are drawn as diamonds, so the shape is a flow chart and not a "
                    "network"),

        figure(11, 1, KIND, 1, "high", page_caption(11, 2), number=2,
               note="the branching model's flow chart in the same box-and-diamond style: Create "
                    "and Score Clusters, Create Backbone Network (Open), Recreate and Rescore "
                    "Clusters, Connect Highest Score Cluster, then Enough Users? with a no branch "
                    "looping back to Recreate and Rescore Clusters through Recreate; Enough "
                    "Channels? ends the method on yes and adds a repeater on no"),

        figure(16, 2, PLACEMENT, 1, "high", page_caption(16, 4), number=4, legend="inside",
               note="snaking-model repeater placement over a grey -40..40 mile field: hundreds of "
                    "small white squares for potential users, red dots for open repeaters, green "
                    "dots for CTCSS repeaters, black open triangles for k-means cluster points and "
                    "green solid plus red dashed circles for coverage footprints; the four-entry "
                    "legend sits inside the bottom of the frame. The frame is geographic (both axes "
                    "titled Miles), which is why the family is map-or-plan-view and not scatter"),

        figure(17, 1, "node-link-network", 1, "high", page_caption(17, 5), number=5,
               note="repeater parity for the snaking model: eight white circles on a bare white "
                    "ground, each bearing a plus or a minus, joined by thin straight links into a "
                    "ring with one interior link; no axes, no frame, no legend, no labels beyond "
                    "the signs"),

        figure(17, 2, PLACEMENT, 1, "high", page_caption(17, 6), number=6, legend="inside",
               note="branching-model placement in the same geographic format as Figure 4, but "
                    "here the repeaters are joined by thin solid black edges that draw the "
                    "branching tree itself across the grey field; user squares are faint, red "
                    "dashed coverage circles sit round each open repeater"),

        figure(18, 1, PLACEMENT, 1, "high", page_caption(18, 7), number=7, legend="inside",
               labels=True,
               note="CTCSS line placement for the branching model: the green repeaters carry "
                    "small printed index numbers (1 to 8) and two families of coverage circles are "
                    "drawn, red solid and blue solid, to show the shared subaudible channels; the "
                    "legend sits inside the bottom of the frame"),

        figure(18, 2, "node-link-network", 1, "high", page_caption(18, 8), number=8,
               note="branching-model parity, same bare diagram as Figure 5: eight signed circles "
                    "joined by thin links, here arranged as a long vertical chain with two "
                    "horizontal runs, no axes and no legend"),

        figure(20, 1, PLACEMENT, 1, "high", page_caption(20, 10), number=10, legend="inside",
               note="rural-case snaking placement: the user cloud is grouped into visible clumps, "
                    "cluster points are marked with black open triangles, and the coverage circles "
                    "mostly overlap inside the disc; the legend box sits at the bottom left of the "
                    "frame and overlaps the axis line"),

        figure(20, 2, "node-link-network", 1, "high", page_caption(20, 11), number=11,
               note="rural-case parity for the snaking model: nine signed circles in a ring with "
                    "one chord, again with no axes, frame or legend"),

        figure(21, 1, PLACEMENT, 1, "high", page_caption(21, 12), number=12, legend="inside",
               note="rural-case branching placement: branching tree edges drawn over the clumped "
                    "user field, red dashed and green solid coverage circles, cluster-point "
                    "triangles; the legend spans nearly the whole frame width along the bottom"),

        figure(21, 2, PLACEMENT, 1, "high", page_caption(21, 13), number=13, legend="inside",
               labels=True,
               note="the CTCSS arrangement for that same branching plan, printed under it: green "
                    "repeaters numbered 1, 5, 6, 7, 8 with three overlapping families of thin "
                    "circles (red, blue, orange) marking which repeaters share a channel; one label "
                    "is overprinted by a circle stroke"),

        figure(22, 1, "node-link-network", 1, "high", page_caption(22, 14), number=14,
               note="rural-case branching parity: eight signed circles joined by links, no axes "
                    "and no legend; the smallest of the four parity diagrams"),

        figure(23, 1, PLACEMENT, 1, "high", page_caption(23, 15), number=15,
               note="the 10,000-user run: the same snaking placement format with a far denser user "
                    "field, so the white squares fill most of the grey field and the green and red "
                    "coverage circles are heavily overplotted; no legend is drawn on this figure"),

        figure(24, 1, PLACEMENT, 2, "high", page_caption(24, 16), number=16, layout="1x2",
               note="cluster-point sensitivity, two plots side by side, each with its own title: "
                    "\"Bender\" Snaking Method Repeater Placement (k=10) on the left and (k=20) on "
                    "the right. Both panels are the same geographic format, and neither carries a "
                    "legend inside the region"),

        figure(25, 1, PLACEMENT, 2, "high", page_caption(25, 17), number=17, layout="1x2",
               note="separation-distance sensitivity, two plots side by side titled Branching "
                    "Method Repeater Placement (d=10) and (d=20): the same grey mile field, red and "
                    "green repeaters, red dashed circles, but no tree edges and no legend"),

        figure(29, 1, PLACEMENT, 1, "high", page_caption(29, 18), number=18, legend="inside",
               note="Appendix A full-page reprint of Figure 4's snaking placement, drawn to the "
                    "whole page with the same -40..40 mile frame and the four-entry legend along "
                    "the bottom inside the frame; the artwork repeats Figure 4 but the page carries "
                    "its own Figure 18 caption, so it is recorded as its own exhibit"),

        figure(30, 1, PLACEMENT, 1, "high", page_caption(30, 19), number=19, legend="inside",
               note="Appendix A reprint of Figure 6's branching placement, full page, tree edges "
                    "over the grey user field, legend inside the bottom of the frame"),

        figure(31, 1, PLACEMENT, 1, "high", page_caption(31, 20), number=20, legend="inside",
               labels=True,
               note="Appendix A reprint of Figure 7's CTCSS arrangement, full page: numbered green "
                    "repeaters and red, blue and orange channel circles; the printed title spells "
                    "CTCSS as CTCOSS, and two repeaters both carry the label 1"),

        figure(32, 1, PLACEMENT, 1, "high", page_caption(32, 21), number=21, legend="inside",
               note="Appendix A reprint of the rural snaking placement (Figure 10), full page: "
                    "clumped user field, cluster triangles, orange and green circles plus red "
                    "dashed ones, legend along the bottom"),

        figure(33, 1, PLACEMENT, 1, "high", page_caption(33, 22), number=22, legend="inside",
               note="Appendix A reprint of the rural branching placement (Figure 12), full page: a "
                    "long near-vertical tree edge through the middle, green dotted and red dashed "
                    "circles, legend along the bottom"),

        figure(34, 1, PLACEMENT, 1, "high", page_caption(34, 23), number=23, legend="inside",
               labels=True,
               note="Appendix A reprint of the CTCSS arrangement (Figure 13), full page: numbered "
                    "green repeaters with thin red, blue and orange circles; the printed title "
                    "again reads CTCOSS, and the label 1 is printed on four different repeaters"),

        figure(35, 1, PLACEMENT, 1, "high", page_caption(35, 24), number=24,
               note="Appendix A reprint of the 10,000-user run (Figure 15), full page: the densest "
                    "user field in the paper with red and green dots almost coincident and circles "
                    "cut by all four frame edges; unlike the other reprints this one carries no "
                    "legend, which is why the legend is recorded as none"),
    ])

    TABLES.extend([
        table(7, 1, 7, 2, header_rows=1, numeric=0, text=2, width="column",
              note="uncaptioned parameter glossary closing 4.2 Mathematical Interpretation: "
                   "Parameter against Description, six body rows (n, k, d_s, h_r, d_h, Δf) under a "
                   "one-row header, every row separated by a rule and both columns boxed, with no "
                   "caption on the page"),

        table(12, 1, 9, 2, header_rows=1, numeric=0, text=2, width="column",
              note="the branching model's own parameter glossary at the end of 5.2, the same "
                   "two-column boxed layout as the p7 table but with two more rows, still "
                   "uncaptioned"),

        table(16, 1, 9, 2, header_rows=1, numeric=0, text=2, width="column",
              note="the case-study instantiation of that glossary: the same two-column boxed grid "
                   "with the parameters given their rural-case values (n = 1400 and so on) at the "
                   "top of 7.1 City Distribution, uncaptioned"),

        table(24, 2, 4, 3, header_rows=1, numeric=2, text=1, width="half",
              note="small uncaptioned grid inside the sensitivity section: repeater output "
                   "distance d_h against the tower height it implies in feet and the number of "
                   "open repeaters left, three data rows, every cell boxed"),

        table(25, 2, 4, 3, header_rows=1, numeric=3, text=1, width="half",
              note="the branching model's version of the same lookup, one page later: d_h against "
                   "open, CTCSS and total repeater counts for 1400, 3000 and 10000 users, "
                   "uncaptioned and fully boxed"),
    ])

    RULES.extend([
        "repeater-placement plots are map-or-plan-view, not scatter: both axes are titled Miles "
        "over a -40..40 field, the markers are placed geography rather than a statistical cloud, "
        "and the coverage circles are drawn in the same coordinate frame [geometry.family]",

        "a parity diagram of signed circles joined by thin links is node-link-network, even "
        "though it has no axes, frame or legend and sits directly above a placement map "
        "[geometry.family] [geometry.legend]",

        "two plots printed side by side with their own titles inside one measured region (the "
        "k-sensitivity and d-sensitivity figures) take panel_count 2 and panel_layout 1x2 "
        "[geometry.panel_count] [geometry.panel_layout]",

        "index numbers printed beside repeater markers are data labels, not axis ticks: the "
        "CTCSS figures label each repeater with a small integer, so data_labels is true there and "
        "false on the unlabelled placement figures [geometry.data_labels]",

        "these tables use a full box, not three-line rules: every row is separated by a rule and "
        "both columns are separated by a vertical rule, and the three parameter grids are the "
        "text-width variety while the two sensitivity grids are half width "
        "[table.rule_style] [table.header_rows]",

        "Appendix A reprints seven body figures at full page as Figures 18-24 with their own "
        "captions, so each reprint is a separate item even though the artwork repeats an earlier "
        "figure [caption.verbatim]",

        "only Figures 1 and 2 are referred to by number in the prose; the twenty placement and "
        "parity figures are introduced by their captions alone, so those items honestly carry "
        "lead_pattern none and an empty lead sentence rather than a quote borrowed from a "
        "neighbouring paragraph [mention.lead_pattern] [mention.count]",

        "when a caption line carries no full stop the extracted caption string has the next body "
        "sentence glued to it (Figure 7 on p18, Figure 17 on p25); the record quotes the printed "
        "caption line only [caption.verbatim] [caption.words]",
    ])

    return (
        "Twenty-four numbered figures and five uncaptioned tables across 51 pages. 27 measured "
        "regions resolve to 22 figure items and 5 tables with no leftovers; the two remaining "
        "numbered figures, 3 and 9 (Surface Plot of Users, p15 and p19), are unresolved because "
        "each was pasted in as a stack of twelve 17 pt image strips, below the extractor's 25 pt "
        "minimum side, so they leave no measured region to record against. Sixteen of the "
        "recorded figures are geographic placement maps, four are parity node-link diagrams, two "
        "are flow charts, and seven of the maps are Appendix A full-page reprints of earlier "
        "figures."
    )


def main() -> int:
    note = build()
    order = 0
    merged = sorted([(it["page"], it["bbox"][1], it) for it in ITEMS]
                    + [(it["page"], it["bbox"][1], it) for it in TABLES],
                    key=lambda t: (t[0], t[1]))
    for _, _, it in merged:
        order += 1
        it["place"]["doc_order"] = order

    payload = {
        "paper": PID,
        "page_count": LAYOUT["page_count"],
        "layout_sha256": LAYOUT["layout_sha256"],
        "measured_regions": sum(len(pg["regions"]) for pg in LAYOUT["pages"]),
        "items": ITEMS,
        "tables": TABLES,
        "excluded_regions": [],
        "rules": RULES,
        "note": note,
    }
    out = PROXY / "pb19-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"items={len(ITEMS)} tables={len(TABLES)} -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
