"""Hand pass for P-B-2011-10496-de9286d6 (mesh-network repeater placement, 34 pages).

The paper prints eight numbered figures, four numbered tables, one uncaptioned two-column
channel table, and two algorithm listings. Every family below was read off a cropped page
proxy; the geometry pass only supplied the rectangles.

Three things drive the record:

* Heading positions. `context_extract` builds `section_path` from the extracted heading
  index, and that index here carries the table of contents (pages 2-3) plus four rows of
  the channel table on p21 misread as headings ("2 B/A'", "3 C/B'", ...). The record is
  placed against headings re-located on the page by their printed number, so Table 1 sits
  under 5.1 Procedure and not under 5.3 Coverage, and Figure 2 sits under 4.3 Naive
  Approach and not under 4.4.
* Figure 1 is a six-panel block (a)-(f) at the top of p12. Panels (a)-(e) are vector plots
  with the population point cloud pasted in as an image block inside the frame, so the
  vector frame is the exhibit and the inner raster is a fragment of it. Panel (f) is a
  raster image with no vector frame and is its own exhibit.
* Both algorithm listings (p9, p20) measure only their title rule and header line, because
  the listing body is ordinary text. They are excluded as not-an-exhibit, the same class
  the lane already carries for program listings.

Usage: python -I tools/_dist_paper18.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2011-10496-de9286d6"
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

# Heading index with the printed y of each heading, so a region can be placed by position
# instead of by the (TOC-contaminated) extracted path.
HEADINGS: list[tuple[int, float, str, str, str]] = []


def load_headings() -> None:
    import pymupdf

    doc = pymupdf.open(PDF)
    for h in CTX["headings"]:
        if h["page"] < 4:
            continue
        num, title = h["number"].strip(), h["title"].strip()
        if num and not re.match(r"^\d+(\.\d+)*$", num):
            continue
        if re.match(r"^[A-E]\s*/", title):
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


def place_for(page: int, reg: int, doc_order: int) -> dict:
    y0 = REG[(page, reg)][1]
    before = [h for h in HEADINGS
              if h[0] < page or (h[0] == page and h[1] <= y0)]
    if not before:
        raise SystemExit(f"no heading before p{page} r{reg}")
    page_h, _, num, title, kind = before[-1]
    path = [f"{h[2]} {h[3]}".strip() for h in before
            if num and h[2] and (h[2] == num or num.startswith(h[2] + "."))]
    if not num:
        path = [title]
    same = [e for e in ITEMS_ORDER if e[0] == page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": doc_order,
        "page_order": same.index((page, reg)) + 1 if (page, reg) in same else 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def raw_lines(page: int) -> list[str]:
    path = PAGES / f"page-{page:04d}.txt"
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def page_caption(page: int, number: int) -> str:
    lines = raw_lines(page)
    pat = re.compile(rf"^\s*(Figure|Table)\s+{number}(?!\d)")
    start = next((i for i, ln in enumerate(lines) if pat.match(ln)), None)
    if start is None:
        raise SystemExit(f"no caption for {number} on page {page}")
    parts = [schema.norm(lines[start])]
    i = start + 1
    while i < len(lines):
        nxt = schema.norm(lines[i])
        i += 1
        if not nxt:
            break
        if nxt.startswith("(") or re.match(r"^(Figure|Table)\s+\d", nxt):
            break
        if parts[-1].endswith((".", "!", "?")):
            break
        parts.append(nxt)
    return schema.norm(" ".join(parts))


PROSE = re.compile(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}")
AXIS_TICK = re.compile("−")
TABLE_CELL = re.compile(r"\d+\.\d+")


def lead_sentence(number: int, kind: str, upto: int) -> tuple[str, str]:
    """First prose unit that refers to the exhibit, trimmed to the quote limit.

    `context_extract` reports one paragraph-sized blob per page here, because the text
    layer interleaves axis numbers with the prose. So the lead sentence is taken from
    `schema.page_units`, skipping the caption itself and the running head.
    """
    pat = re.compile(r"[Ff]igure\s+" + str(number) if kind == "figure"
                     else r"[Tt]able\s+" + str(number))
    head = re.compile(r"Team\s*#?\s*\d+\s*Page\s+\d+\s+of\s+\d+\s*", re.I)
    for page in range(1, max(pg["page"] for pg in LAYOUT["pages"]) + 1):
        for unit in schema.page_units(PID, page):
            unit = head.sub("", unit)
            if not pat.search(unit) or re.match(r"^(Figure|Table)\s+\d", unit):
                continue
            hit = next((s for s in schema.sentences(unit)
                        if pat.search(s) and PROSE.search(s)
                        and AXIS_TICK.search(s) is None
                        and len(TABLE_CELL.findall(s)) < 3), "")
            if not hit:
                continue
            text = " ".join(hit.split()[:schema.MAX_QUOTE_WORDS])
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
    sent, pattern = lead_sentence(number, kind, page)
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


def figure(page: int, reg: int, family: str, panels: int, conf: str,
           cap: str | None, *, layout: str = "1", legend: str = "none",
           three_d: str = "no", printed: bool = True, labels: bool = False,
           number: int | None = None, note: str = "", source: str = "text-layer",
           position: str = "below", shared_axes: bool = False) -> dict:
    cap_text = cap or ""
    return {
        "page": page,
        "bbox": REG[(page, reg)],
        "family": family,
        "confidence": conf,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": source if cap_text else "none",
        "note": note,
        "place": place_for(page, reg, 0),
        "mention": mention(number, page),
        "caption": caption_block(cap_text, position),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared_axes,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, rows: int, cols: int, *, header_rows: int = 1,
          rule: str = "booktabs", numeric: int = 0, text: int = 1, width: str = "full",
          merged: bool = False, number: int | None = None, cap: str | None = None,
          note: str = "") -> dict:
    cap_text = cap or ""
    return {
        "page": page,
        "bbox": REG[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": "text-layer" if cap_text else "none",
        "note": note,
        "place": place_for(page, reg, 0),
        "mention": mention(number, page, "table"),
        "caption": caption_block(cap_text),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": rule,
            "zebra": False,
            "merged_cells": merged,
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


def excluded(page: int, reg: int, reason: str, note: str) -> dict:
    return {"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note}


ITEMS_ORDER: list[tuple[int, int]] = [
    (12, 1), (12, 4), (12, 7), (12, 8),
    (15, 1),
    (16, 1),
    (18, 1),
    (26, 1), (26, 2),
    (31, 1), (31, 2),
    (32, 1), (32, 2),
    (33, 1), (33, 2),
]

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
RULES: list[str] = []


def build() -> str:
    load_headings()

    ITEMS.extend([
        figure(12, 1, "heatmap-or-contour", 2, "high", page_caption(12, 1), number=1,
               layout="1x2",
               note="panels (a) Random Population Distribution and (b) Clumped Population "
                    "Distribution with 5 Clumps: one vector frame of two square plots, x and y "
                    "ticked every 10 from -30 to 30 with y running negative at the top, and each "
                    "plot filled by a raster density image on a black ground using a hot ramp "
                    "from dark red through orange to white; panel (a) is a diffuse field of small "
                    "bright blobs and panel (b) the same data aggregated into about five clumps"),

        figure(12, 4, "heatmap-or-contour", 2, "high", page_caption(12, 1), number=1,
               layout="1x2",
               note="panels (c) Clumped Population Distribution with 10 Clumps and (d) with 20 "
                    "Clumps: the second two-plot frame, same axes, same hot-ramp density image, "
                    "with six or seven clumps in panel (c) and bright ridges round the rim in "
                    "panel (d); the two inner raster regions are the image bodies of these "
                    "panels, not exhibits"),

        figure(12, 7, "heatmap-or-contour", 1, "high", page_caption(12, 1), number=1,
               note="panel (e) Clumped Population Distribution with 40 Clumps: single square "
                    "plot with the same -30..30 inverted-y frame and the same hot-ramp density "
                    "image, here showing a dark void at centre-left between bright cores; a "
                    "second raster region measured inside this bbox is the same panel detected "
                    "twice, not a second plot"),

        figure(12, 8, "heatmap-or-contour", 1, "medium", page_caption(12, 1), number=1,
               note="panel (f) Actual Population Distribution: the real Southeastern United "
                    "States population, printed as a coarse raster density grid on a warm "
                    "cream-to-brown ramp, with square cells clearly coarser than the plots "
                    "beside it and no axes, ticks or frame of its own; it is a data field, not a "
                    "photograph, which is why the family is heatmap-or-contour rather than "
                    "photo-or-raster-image"),

        figure(15, 1, "node-link-network", 1, "high", page_caption(15, 2), number=2,
               note="circle-bounded x/y plot ticked every 10 from -50 to 50: the repeater "
                    "network the naive approach builds, drawn as blue nodes joined by straight "
                    "blue edges over a grey point cloud of users, with dashed green circles "
                    "marking coverage radii and one large blue ring marking the arena; no legend "
                    "and no axis titles"),

        figure(16, 1, "node-link-network", 1, "high", page_caption(16, 3), number=3,
               note="the same kind of network but rasterised: about twelve numbered nodes "
                    "joined by blue edges, with no arena circle and no user cloud. The printed "
                    "caption names the colour code, dark blue = A, light blue = B/A', yellow = "
                    "C/B' and maroon = D/C', so node colour encodes repeater type"),

        figure(18, 1, "scatter", 1, "high", page_caption(18, 4), number=4,
               note="square x/y plot ticked every 10 from -40 to 40 inside a blue circular "
                    "arena: several thousand black points coloured by cluster (red, orange, "
                    "yellow, green, cyan, blue) around a few dense centres, which is the k-means "
                    "partition of the population; no legend, no axis titles"),

        figure(26, 1, "node-link-network", 1, "high", page_caption(26, 5), number=5,
               note="panel (a) No subnetwork: the circle-bounded -50..40 plot with the repeater "
                    "network as blue nodes and edges over the user cloud and dashed green "
                    "coverage circles, identical in format to Figure 2"),

        figure(26, 2, "node-link-network", 1, "high", page_caption(26, 5), number=5,
               note="panel (b) With subnetwork: same plot with an extra cluster of nodes filling "
                    "the gap below the main chain; the caption prints once under this panel and "
                    "covers both"),

        figure(31, 1, "node-link-network", 2, "high", page_caption(31, 6), number=6,
               layout="1x2",
               note="panels (a) and (b), both Random Population Distribution, side by side: each "
                    "panel is a -40..40 square plot with the blue arena circle, a black user "
                    "cloud, light-green clump outlines and a blue node-and-edge tree; no legend, "
                    "no axis titles, no node labels"),

        figure(31, 2, "node-link-network", 2, "high", page_caption(31, 6), number=6,
               layout="1x2",
               note="panels (c) and (d), both Clumped Distribution - 5 Clumps: same two-panel "
                    "format as the region above, with dashed green clump outlines and nodes "
                    "coloured by cluster"),

        figure(32, 1, "node-link-network", 2, "high", page_caption(32, 7), number=7,
               layout="1x2",
               note="panels (a) and (b), both Clumped Distribution - 10 Clumps: more, smaller "
                    "clumps than Figure 6, each panel still a -40..40 square plot with the arena "
                    "circle, user cloud, green clump outlines and a blue tree"),

        figure(32, 2, "node-link-network", 2, "high", page_caption(32, 7), number=7,
               layout="1x2",
               note="panels (c) and (d), both Clumped Distribution - 20 Clumps: same format, "
                    "with dense clump outlines across most of the disc and a long blue edge "
                    "crossing the middle of the right panel"),

        figure(33, 1, "node-link-network", 1, "high", page_caption(33, 8), number=8,
               note="panel (a) Clumped Distribution - 40 Clumps: a single large -40..40 square "
                    "plot (the regions on this page are stacked vertically, not side by side) "
                    "with about twenty tightly packed clump outlines and a blue tree whose nodes "
                    "are coloured by cluster"),

        figure(33, 2, "node-link-network", 1, "high", page_caption(33, 8), number=8,
               note="panel (b) Clumped Distribution - 40 Clumps: the second stacked plot, same "
                    "format as panel (a), with a few very long rim-to-centre edges; the shared "
                    "Figure 8 caption prints under this panel"),
    ])

    TABLES.extend([
        table(21, 1, 6, 2, header_rows=1, rule="vertical-rules", numeric=1, text=1,
              width="half",
              note="uncaptioned two-column lookup printed at the end of 4.5.2 Assigning "
                   "Channels: Channel Number 1-5 against the frequency set each channel carries "
                   "or shares (A, B/A', C/B', D/C', E/D'). It has a header row, a top rule and "
                   "a bottom rule with one vertical rule between the columns, and no caption "
                   "anywhere on the page, so the caption is recorded as none"),

        table(22, 1, 8, 7, header_rows=2, rule="booktabs", numeric=6, text=1, merged=True,
              number=1, cap=page_caption(22, 1),
              note="two header rows: a spanning Population Distribution over five distribution "
                   "columns, then # of clusters over six rows (5, 10, 15, 20, 25, Naive); every "
                   "cell is mean plus-minus standard deviation of the repeater count, so the "
                   "table is numeric except the cluster-count column"),

        table(23, 1, 8, 7, header_rows=2, rule="booktabs", numeric=6, text=1, merged=True,
              number=2, cap=page_caption(23, 2),
              note="same grid as Table 1, but the cells are mean plus-minus standard deviation "
                   "of the number of people left uncovered; the Naive row is 0.00 everywhere "
                   "because the naive network covers the whole disc"),

        table(23, 2, 3, 6, header_rows=1, rule="booktabs", numeric=5, text=1, merged=True,
              number=3, cap=page_caption(23, 3),
              note="a different shape from Tables 1, 2 and 4: one header row of five "
                   "distribution columns and only two body rows, K-means and Naive, holding "
                   "single standard-deviation figures with no plus-minus term"),

        table(24, 1, 8, 7, header_rows=2, rule="booktabs", numeric=6, text=1, merged=True,
              number=4, cap=page_caption(24, 4),
              note="same grid as Tables 1 and 2, holding the fraction of transmission requests "
                   "processed as a mean with a plus-minus half-width; the Naive row falls from "
                   "0.31 to 0.22, the paper's headline comparison"),
    ])

    EXCLUDED.extend([
        excluded(9, 1, "not-an-exhibit",
                 "top rule and header line of the Algorithm 1 listing, measured only because "
                 "the rule is page-wide; the listing body is ordinary text, so nothing here is "
                 "a figure or a table"),
        excluded(20, 1, "not-an-exhibit",
                 "top rule and header line of the Algorithm 3 listing, the same shape as the "
                 "p9 listing"),
        excluded(18, 2, "not-an-exhibit",
                 "the whole Algorithm 2 'Main Network Generation Algorithm' box. It has a "
                 "ruled frame and a title bar, so the table detector now measures it as one "
                 "block, but the body is pseudocode: Require lines and numbered procedural "
                 "statements, no cells, columns or data values. Not a figure or a table."),
        excluded(21, 2, "not-an-exhibit",
                 "the whole Algorithm 4 'Assign Channels' box, the same pseudocode shape as "
                 "the p18 listing: Require lines and numbered statements inside a ruled frame."),
        excluded(12, 2, "fragment-of-other",
                 "the density image that fills panel (a): the measured vector region is the "
                 "frame with its ticks and labels, the raster inside it is the picture body"),
        excluded(12, 3, "fragment-of-other",
                 "the density image that fills panel (b), inside the same vector frame"),
        excluded(12, 5, "fragment-of-other",
                 "the density image that fills panel (c), inside the second vector frame"),
        excluded(12, 6, "fragment-of-other",
                 "the density image that fills panel (d), inside the second vector frame"),
        excluded(12, 9, "fragment-of-other",
                 "second detection of panel (e): this raster bbox lies wholly inside the vector "
                 "bbox of the panel, so it is the same plot measured twice, not a sixth picture"),
    ])

    RULES.extend([
        "fragment-of-other covers a raster block drawn inside a vector chart frame: the five "
        "pasted-in density images on p12 are the picture bodies of panels (a)-(e), not "
        "exhibits of their own, so one panel is one item even where two measured regions "
        "cover it [geometry.panel_count] [geometry.family]",

        "a multi-panel block whose panels are measured as separate regions (Figures 6 and 7, "
        "two regions of two panels each) is recorded per region with panel_count 2 and the "
        "shared caption quoted on both, while a panel split vertically on one page (Figure 8) "
        "is recorded per region with panel_count 1 [geometry.panel_layout]",

        "a printed caption line is quoted only up to the point where the text layer runs into "
        "body prose: Table 1's caption ends at 'net- work' and Table 4's at 'distribu- tions', "
        "and the sentences that follow on the same line are body text, not caption "
        "[caption.verbatim] [caption.words]",

        "an uncaptioned two-column lookup inside a subsection (p21, Channel Number against "
        "Frequencies) is a table with caption_source none, not a figure, because it has a "
        "header row and rules [table.rule_style] [table.header_rows]",

        "algorithm listings measure only their title rule and header line; the body is text, "
        "so the region is excluded as not-an-exhibit rather than counted as a flowchart "
        "[geometry.data_labels]",

        "a raster panel that stands alone beside a vector frame (Figure 1 panel (f), the real "
        "population grid) is its own exhibit, and it is read as a coarse density field rather "
        "than as a photograph, unlike the raster blocks drawn inside the other frames "
        "[geometry.family]",

        "node colour in the network figures encodes repeater type, which the Figure 3 caption "
        "states outright; the record never reads a legend off colour alone where the caption "
        "does not say so [geometry.legend] [caption.verbatim]",
    ])

    return (
        "Eight numbered figures, four numbered tables, one uncaptioned lookup table and two "
        "algorithm listings across 34 pages. 27 measured regions resolve to 15 figure items, "
        "5 tables and 7 excluded regions with no leftovers. The lane's heading index is "
        "unreliable here (table of contents on pages 2-3, plus table rows on p21 read as "
        "headings), so every place block was rebuilt from heading positions found on the page. "
        "Geometry bought no rule change: the raster-inside-frame case was resolved with the "
        "existing fragment-of-other reason."
    )


def main() -> int:
    note = build()
    order = 0
    for item in ITEMS:
        order += 1
        item["place"]["doc_order"] = order
    for tbl in TABLES:
        order += 1
        tbl["place"]["doc_order"] = order

    payload = {
        "paper": PID,
        "page_count": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "measured_regions": sum(len(pg["regions"]) for pg in LAYOUT["pages"]),
        "items": ITEMS,
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": RULES,
        "note": note,
    }
    out = PROXY / "pb18-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"items={len(ITEMS)} tables={len(TABLES)} excluded={len(EXCLUDED)} -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
