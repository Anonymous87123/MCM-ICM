"""Hand pass for P-A-2011-9582-99696cfc (half-pipe snowboard course, 34 pages).

The paper prints 30 numbered figures, three unnumbered body tables, one unnumbered method
flowchart, and one inline defaults table that recurs three times (p21, p27, p29). Every
family below was read off a cropped page proxy; the geometry pass only supplied the
rectangles.

Three structural facts drive the layout of this record:

* Figure 11 is a three-sketch sequence whose first sketch is the last region of p12 and
  whose caption prints under the second sketch on p13. The exhibit is recorded once, at
  the captioned region, with panel_count 3; the two uncaptioned stages are excluded as
  fragments of it rather than counted again.
* Figure 25 is a five-panel sensitivity block printed across p27 and p28, and Figure 30 is
  a six-panel block printed across p32 and p33 with its single caption under the p33 half.
  Panels are measured as separate regions and recorded as separate items, each carrying the
  shared caption, which is the convention this lane already uses for multi-panel figures.
* The parameter list runs across the p3/p4 break: p3 carries the header row, p4 continues
  the same four-column key/value grid with no header of its own. The p3 half is recorded as
  the table with continued=true and the p4 half is excluded as split-across-pages, so the
  rows are not counted twice and the continuation is not silently dropped.

Usage: python -I tools/_dist_paper17.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2011-9582-99696cfc"
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

PAGE_W, PAGE_H = 595.32, 841.92


def raw_lines(page: int) -> list[str]:
    path = PAGES / f"page-{page:04d}.txt"
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def page_caption(page: int, number: int) -> str:
    """The printed caption block for Figure <number>, joined the way the page sets it."""
    lines = raw_lines(page)
    pat = re.compile(rf"^\s*Figure\s+{number}(?!\d)")
    start = next((i for i, ln in enumerate(lines) if pat.match(ln)), None)
    if start is None:
        raise SystemExit(f"no caption for Figure {number} on page {page}")
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


def mentions_of(number: int) -> list[dict]:
    return [m for m in MENTIONS if m["kind"] == "figure" and m["number"] == number]


def trim(text: str, limit: int = 25) -> str:
    toks = text.split()
    return " ".join(toks[:limit]) if len(toks) > limit else text


def mention(number: int | None, page: int, *, lead: bool = True) -> dict:
    if number is None:
        return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}
    ms = mentions_of(number)
    if not ms:
        return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}
    first = min(m["page"] for m in ms)
    styles = sorted({m["spelling"] for m in ms})
    sent = ""
    if lead:
        pool = [m for m in ms if m["page"] <= page] or ms
        sent = trim(pool[0]["sentence"])
    pattern = "none"
    if sent:
        low = sent.lower()
        if re.match(r"^figure\s+\d+\s+shows", low):
            pattern = "figure-n-shows"
        elif "as shown in" in low or "as shown" in low:
            pattern = "as-shown-in"
        elif re.search(r"\(figure\s+\d+", low):
            pattern = "parenthetical"
        else:
            pattern = "direct"
    return {"first_page": first, "lead_pages": page - first, "style": styles,
            "count": len(ms), "lead_sentence": sent, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": 1 if sent else 0,
            "gap_sentences": abs(page - first)}


def place(page: int, reg: int, doc_order: int) -> dict:
    c = CTXREG[(page, reg)]
    same = [e for e in ITEMS_ORDER if e[0] == page]
    return {
        "section_path": c["section_path"],
        "section_numbered": c["section_numbered"],
        "section_kind": c["section_kind"],
        "doc_order": doc_order,
        "page_order": same.index((page, reg)) + 1 if (page, reg) in same else 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, position: str = "below") -> dict:
    numbering = "none"
    m = re.match(r"^(Figure\s+\d+)([:.])?", text)
    if m:
        numbering = {"": "Figure N", ":": "Figure N:", ".": "Figure N."}[m.group(2) or ""]
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
           position: str = "below") -> dict:
    cap_text = cap or ""
    men = mention(number, page)
    return {
        "page": page,
        "bbox": REG[(page, reg)],
        "family": family,
        "confidence": conf,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": source if cap_text else "none",
        "note": note,
        "place": place(page, reg, 0),
        "mention": men,
        "caption": caption_block(cap_text, position),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, rows: int, cols: int, *, rule: str = "boxed",
          numeric: int = 0, text: int = 4, width: str = "full",
          continued: bool = False, units_hdr: bool = False,
          number: int | None = None, cap: str | None = None, note: str = "") -> dict:
    cap_text = cap or ""
    return {
        "page": page,
        "bbox": REG[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": "text-layer" if cap_text else "none",
        "note": note,
        "place": place(page, reg, 0),
        "mention": mention(number, page),
        "caption": caption_block(cap_text),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": 1,
            "rule_style": rule,
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": units_hdr,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text,
            "width": width,
            "orientation": "portrait",
            "continued": continued,
            "note_sentence": "",
        },
    }


def excluded(page: int, reg: int, reason: str, note: str) -> dict:
    return {"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note}


ITEMS_ORDER: list[tuple[int, int]] = [
    (2, 1), (2, 2),
    (4, 2),
    (5, 1), (5, 2),
    (6, 1),
    (9, 1),
    (11, 1),
    (12, 1), (12, 2),
    (13, 2),
    (14, 1), (14, 2),
    (15, 1),
    (18, 1),
    (19, 1),
    (20, 1),
    (21, 1), (21, 2), (21, 3), (21, 4), (21, 5),
    (22, 1), (22, 2), (22, 3), (22, 4),
    (23, 1), (23, 2),
    (24, 1),
    (25, 1), (25, 2), (25, 3), (25, 4), (25, 5), (25, 6),
    (26, 1), (26, 2), (26, 3),
    (27, 2), (27, 3), (27, 4),
    (28, 1), (28, 2), (28, 3),
    (29, 1), (29, 2), (29, 3),
    (30, 1), (30, 2), (30, 3),
    (31, 1), (31, 2), (31, 3),
    (32, 1), (32, 2),
    (33, 1), (33, 2), (33, 3), (33, 4),
]

ITEMS = [
    figure(2, 1, "flowchart-or-schematic", 1, "high",
           page_caption(2, 1), number=1, printed=False, labels=True,
           note="front and back wall of a half-pipe drawn in blue outline in profile view, "
                "each wall labelled deck, coping, vert, transition and the floor labelled "
                "flat bottom, with HALT-PIPE / VERT RAMP PROFILE VIEW set in the middle: a "
                "labelled cross-section, not a plot, so no numeric ticks and the dimension "
                "letters are the only printed data"),

    figure(2, 2, "flowchart-or-schematic", 1, "high",
           page_caption(2, 2), number=2, printed=False, labels=True,
           note="faint grey dimensioned drawing of the same cross-section with the FIS "
                "measures marked W (width), H (height), T (transition), B (flat bottom) and a "
                "V arrow at the coping; the drawing is a low-contrast scan pasted whole, which "
                "is why the region is an image block rather than vector paths"),

    figure(4, 2, "surface-or-3D", 1, "high",
           page_caption(4, 3), number=3, three_d="surface-mesh",
           note="MATLAB 3D axes box with the pipe wall drawn as a colour-mapped wire mesh graded "
                "red at the rim to blue at the floor, two red path curves lying on it, and an "
                "x/y/z triad floating inside the box: the coordinate conventions the paper uses "
                "for every later plot"),

    figure(5, 1, "flowchart-or-schematic", 1, "high",
           page_caption(5, 4), number=4, printed=False,
           note="six-node flow diagram of the model in blue outline: rounded boxes for course "
                "shape and v, ellipses for f, path and Vertical Air, a diamond for snowboarder, "
                "joined by plain arrows; the only printed text is the node names, so there are "
                "no numbers or axes"),

    figure(5, 2, "surface-or-3D", 1, "high",
           page_caption(5, 5), number=5, three_d="surface-mesh",
           note="same 3D pipe mesh as Figure 3 but with the whole cycle drawn on it: red curve "
                "along the wall and floor for the ride, then a green parabola leaving the coping "
                "and a blue parabola for the airborne leg without air drag"),

    figure(6, 1, "composite-panel", 3, "high",
           page_caption(6, 6), number=6, layout="1+2", three_d="surface-mesh",
           note="three panels joined by the two cyan arrows: the upper panel is the 3D pipe mesh "
                "with the force vectors N, mg and f and the velocity v drawn on the rider, and the "
                "two lower panels are zooms of the same corner in the x-y and y-z projections; the "
                "lower two are measured as their own regions and are excluded here as fragments "
                "of this exhibit"),

    figure(9, 1, "flowchart-or-schematic", 1, "high",
           page_caption(9, 7), number=7, printed=False, labels=True,
           note="side view of the airborne leg: a pale parabola from launch to landing on the "
                "slope, with the velocity resolved into Vy and Vz, gravity mg drawn downward, the "
                "air-drag arrow, the vertical air H marked by a bracket and the slope angle theta "
                "set at the landing point"),

    figure(11, 1, "flowchart-or-schematic", 1, "high",
           page_caption(11, 8), number=8, printed=False, labels=True,
           note="rider carried as a stick figure at the coping with the angular momentum Lz0 "
                "shown as the usual circled cross, the friction arrows f1 and f2 resolved at the "
                "board, mg through the mass point, and the trajectory of the mass point drawn out "
                "as a curve; the x/y/z triad sits at the right"),

    figure(12, 1, "flowchart-or-schematic", 1, "high",
           page_caption(12, 9), number=9, printed=False,
           note="trick sketch for the beginner twist: rider as a small body on the board inside "
                "the pipe cross-section, x/y/z triad at the upper left, a long straight axis of "
                "rotation line and short arrows at the board; line art with no numeric axes"),

    figure(12, 2, "flowchart-or-schematic", 1, "high",
           page_caption(12, 10), number=10, printed=False,
           note="second trick sketch: the triad is centred, Lz is drawn as one arrow and the "
                "boarder as a white ball, with the axis of rotation running down to the left and "
                "the pipe profile set at the right"),

    figure(13, 2, "flowchart-or-schematic", 3, "high",
           page_caption(13, 11), number=11, layout="column of 3",
           note="three stacked trick sketches sharing one caption: the Flip 1 stage closes p12, "
                "and the Twist and Flip 2 stages are the two sketches on p13, with an open "
                "down-arrow chaining them; both uncaptioned stages are excluded as fragments of "
                "this exhibit, so panel_count 3 counts the sequence rather than this region"),

    figure(14, 1, "flowchart-or-schematic", 1, "high",
           page_caption(14, 12), number=12, printed=False, labels=True,
           note="cross-section of the pipe drawn with a dashed measuring grid over a colour-"
                "graded ramp outline, annotated width across the top, depth down the inside and "
                "flat along the floor, over the title Shape of ramp surface"),

    figure(14, 2, "heatmap-or-contour", 2, "medium",
           page_caption(14, 13), number=13, layout="1x2",
           note="two colour-field panels joined by a hollow double arrow: the left one paints the "
                "ramp cross-section in rainbow bands under dotted axes and names ramp and path, "
                "the right one is a dense rainbow field with the red curve tau(x) drawn over it and "
                "the relation z = z(tau(x)) set inside the panel; no colour bar on either panel, "
                "which is why the family is read from the banded fields rather than from a key",),

    figure(15, 1, "surface-or-3D", 1, "high",
           page_caption(15, 14), number=14, three_d="surface-mesh",
           note="numerical-simulation output: the pipe mesh in perspective with the computed "
                "trajectory drawn as a red curve on the wall that turns green once airborne; "
                "numeric ticks print on all three axes, no legend and no colour bar"),

    figure(18, 1, "flowchart-or-schematic", 2, "high",
           page_caption(18, 15), number=15, layout="1x2", printed=False,
           note="two stick-figure riders drawn against a thin vertical axis, arms out on the left "
                "and tucked on the right, with circular arrows over each head and a thick blue "
                "arrow labelled w between them: the posture change that adds to the initial "
                "angular momentum, drawn as a pair of sketches with no axes"),

    figure(19, 1, "flowchart-or-schematic", 1, "medium",
           page_caption(19, 16), number=16, printed=False,
           note="the whole model as one dependency diagram: about twenty ellipses for quantities "
                "(vert, shape of transition, flat, fly time, Ereach, angular momentum and so on) "
                "and four boxes for decisions (shape, practical, vertical air, total degree of "
                "rotation) joined by blue arrows, two of them edge-labelled best choice and "
                "conservation of energy; recorded as a schematic because the caption calls it a "
                "schema and the arrows carry no process order, though a node-link reading is "
                "defensible, hence medium confidence",),

    figure(20, 1, "surface-or-3D", 1, "high",
           page_caption(20, 17), number=17, three_d="surface-mesh",
           note="3D mesh of the pipe with a bright green closed loop rising well above the sheet "
                "and two red marked curves on it, one along the valley and one bending up at the "
                "right end: the search space of Analysis 1 drawn in the same MATLAB view as the "
                "earlier surfaces"),

    figure(21, 1, "table-as-figure", 1, "high", None, printed=True, labels=True,
           note="four-column key/value grid drawn with ruled borders and no header row: W(width) "
                "15m and H(height) 3.5m on the first row, B(length of flat bottom) 5m and theta "
                "18 degrees on the second, zt(location of start point of Fly) 10m and Transition "
                "Shape Standard ellipse on the third; recorded as table-as-figure because the "
                "lane's table-grid block needs a header row and this grid has none, and because "
                "the same grid recurs on p27 with the title Default Values",),

    figure(21, 2, "line", 1, "high", page_caption(21, 18), number=18,
           note="left panel of Figure 18: blue line through nine black square markers, panel "
                "title relationship between width & VA_f, x axis width 10-25, y axis VA_f 5.5-"
                "8.5, rising and flattening; the panel titles, not letters, are what identify "
                "the two panels"),

    figure(21, 3, "line", 1, "high", page_caption(21, 18), number=18,
           note="right panel of Figure 18: blue line through black square markers, panel title "
                "relationship between width & Eleave, x axis width 10-25, y axis Eleave 6700-"
                "7600, falling almost linearly"),

    figure(21, 4, "line", 1, "high", page_caption(21, 19), number=19,
           note="right panel of Figure 19: blue line through black square markers, panel title "
                "relationship between height & Velocity_y, x axis height 2-20, y axis 10.5-13.5, "
                "peaking near height 15"),

    figure(21, 5, "line", 1, "high", page_caption(21, 19), number=19,
           note="left panel of Figure 19: blue line through black square markers, panel title "
                "relationship between height & VerticalAir, x axis height 2-20, y axis 5.5-9.5, "
                "rising then flat and slightly declining after height 16"),

    figure(22, 1, "line", 1, "high", page_caption(22, 20), number=20,
           note="right panel of Figure 20: panel title relationship between flat & Eleave, x "
                "axis flat 0-6, y axis Eleave 7150-7400, straight decreasing line"),

    figure(22, 2, "line", 1, "high", page_caption(22, 20), number=20,
           note="left panel of Figure 20: panel title relationship between flat & VA_f, x axis "
                "flat 0-6, y axis VA_f 6.0-6.8, straight increasing line"),

    figure(22, 3, "line", 1, "high", page_caption(22, 21), number=21,
           note="left panel of Figure 21: panel title relationship between theta & VA_f, x axis "
                "theta 0-45, y axis VA_f 4-12, bending upward"),

    figure(22, 4, "line", 1, "high", page_caption(22, 21), number=21,
           note="right panel of Figure 21: panel title relationship between theta & Eleave, x "
                "axis theta 0-45, y axis Eleave 5000-10000, nearly straight rising line"),

    figure(23, 1, "line", 1, "high", page_caption(23, 22), number=22,
           note="left panel of Figure 22: panel title relationship between zlength & VA, thick "
                "blue curve through black square markers, x axis zlength 0-15, y axis VA 4-10, "
                "peaking near zlength 2-3 then falling to 4.2"),

    figure(23, 2, "line", 1, "high", page_caption(23, 22), number=22,
           note="right panel of Figure 22: panel title relationship between zlength & Eleave, x "
                "axis zlength 0-15, y axis Eleave 5000-8500, rising almost linearly"),

    figure(24, 1, "flowchart-or-schematic", 1, "high", None, printed=False,
           note="unnumbered six-box method chart: Define Controling Points, Generate sampling "
                "points convex curves, Define Gene, Define Fitness-Function, Gene-Algorithm, "
                "Optimize curve, each a grey box with a white title tab and bullet lines, stacked "
                "in reading order with no connectors; the gene-algorithm design that Figure 23 "
                "then reports, printed as a body exhibit without a caption",),

    figure(25, 1, "line", 1, "high", page_caption(25, 23), number=23,
           note="first of the four axis boxes making up panel (a) of Figure 23: the blue initial "
                "generation of curves in a V shape, x -10 to 10, y 0 to -3.5; the region is one "
                "sub-axis of the panel, whose letter (a) prints under the pair"),

    figure(25, 2, "line", 1, "high", page_caption(25, 23), number=23,
           note="second axis box of panel (a): the fitness curve of the initial generation, x 0-"
                "100, y 0-0.1, rising then dropping at the right edge"),

    figure(25, 3, "line", 1, "high", page_caption(25, 23), number=23,
           note="first axis box of panel (b): the same V family of curves in blue with the selected "
                "red curve among them"),

    figure(25, 4, "line", 1, "high", page_caption(25, 23), number=23,
           note="second axis box of panel (b): the fitness readings of the finished generation, a "
                "dense bank of light-blue vertical strokes, x 0-100, y 0-0.025"),

    figure(25, 5, "line", 1, "high", page_caption(25, 23), number=23,
           note="panel (d) of Figure 23: a raster screenshot inside an otherwise vector figure, "
                "grey background, dashed ellipse with a thick red arc and two red plus markers, "
                "x -6 to 6, y -3 to 3: the fitted curve against the ellipse"),

    figure(25, 6, "line", 1, "high", page_caption(25, 23), number=23,
           note="panel (c) of Figure 23: the optimised pipe profile as one thin curve running "
                "along the bottom and curling up at both ends, x -6 to 6, y 0 to -0.3; the panel "
                "letter prints above the caption rather than under the plot"),

    figure(26, 1, "surface-or-3D", 1, "high", page_caption(26, 24), number=24,
           three_d="surface-mesh",
           note="panel (a) of Figure 24: 3D wire mesh of the optimised course with the red ride "
                "curve on the surface and the green airborne arch rising out of it"),

    figure(26, 2, "line", 1, "high", page_caption(26, 24), number=24,
           note="panel (b) of Figure 24: the cross-section of the optimised course as a thin "
                "dashed U curve, x -8 to 8, y -0.5 to -3.0"),

    figure(26, 3, "line", 1, "high", page_caption(26, 24), number=24,
           note="panel (c) of Figure 24: the optimal curve fitted with an ellipse, the dashed "
                "ellipse with the thick red arc and small red plus markers over it, panel title "
                "Ellipse Fitting of Optimal Shape of Course"),

    figure(27, 2, "table-as-figure", 1, "high", None, labels=True,
           note="the Default Values grid printed again, this time with its title line: W(width) "
                "18m is absent here, the rows are W 15m / H 3.5m, B 5m / theta 18 degrees, zt "
                "10m / Transition Shape Standard ellipse; the measured box starts at the title "
                "and carries all three rows",),

    figure(27, 3, "line", 1, "high", None, number=25,
           note="panel (a) of Figure 25, whose caption prints on p28: panel title relationship "
                "between width & FlyTime/s, blue curve through black square markers, y axis "
                "FlyTime/s about 2.5-3.0; the x tick labels fall below the measured box"),

    figure(27, 4, "line", 1, "high", None, number=25,
           note="panel (b) of Figure 25: panel title relationship between flat & FlyTime/s, blue "
                "curve through black square markers, same y range, x ticks below the box"),

    figure(28, 1, "line", 1, "high", page_caption(28, 25), number=25,
           note="panel (c) of Figure 25: panel title relationship between zlength & FlyTime/s, "
                "blue curve through markers, x axis zlength 0-15, peaking near zlength 4 then "
                "falling to 2.58"),

    figure(28, 2, "line", 1, "high", page_caption(28, 25), number=25,
           note="panel (d) of Figure 25: panel title relationship between height & FlyTime/s, x "
                "axis height 2-6, rising monotonically"),

    figure(28, 3, "line", 1, "high", page_caption(28, 25), number=25,
           note="panel (e) of Figure 25: panel title relationship between theta & FlyTime/s, x "
                "axis theta 0-45, y axis 2.0-4.5, convex rising curve"),

    figure(29, 1, "table-as-figure", 1, "high", None, labels=True,
           note="the same key/value grid for the recommended course, rows W(width) 18m / H(height) "
                "3.5m, B 5m / theta 18 degrees, zt 10m / Transition Shape To Be Optimized; the "
                "measured box starts below the title and the first row, so the table is taller "
                "than the region the geometry pass found",),

    figure(29, 2, "line", 1, "high", page_caption(29, 26), number=26,
           note="left panel of Figure 26: the optimised cross-section for angular momentum as a "
                "thin dashed U curve, x -8 to 8, y 0 to -3.5"),

    figure(29, 3, "line", 1, "high", page_caption(29, 26), number=26,
           note="right panel of Figure 26: panel title Ellipse Fitting of Optimal Shape of Course "
                "for Angular Momentum, dashed ellipse with a thick red arc and one red plus "
                "marker; the panel title says ellipse while the caption says second order curve"),

    figure(30, 1, "surface-or-3D", 1, "high", page_caption(30, 27), number=27,
           three_d="surface-mesh",
           note="right panel of Figure 27: the 3D course mesh with the green airborne arch and the "
                "red ride curve, the same MATLAB rendering as Figure 24 panel (a)"),

    figure(30, 2, "line", 1, "high", page_caption(30, 27), number=27,
           note="left panel of Figure 27: the optimised cross-section for total degree of rotation "
                "as a thin dashed U curve with no panel title, x -8 to 8, y 0 to -3.5"),

    figure(30, 3, "line", 1, "high", page_caption(30, 28), number=28, legend="none",
           note="single plot titled Ellipse Fitting of Optimal Shape of Course for Total Degree of "
                "Rotation: faint dashed ellipse, thick red arc and one red plus marker over it, "
                "plus a short blue segment along the floor, x -8 to 4, y -4 to 3"),

    figure(31, 1, "surface-or-3D", 1, "high", page_caption(31, 29), number=29,
           three_d="surface-mesh",
           note="panel (a) of Figure 29: 3D wire mesh of the hybrid optimum with the green arch and "
                "the red ride curve, ticks -10 to -50 on one floor axis and -5 to 5 on the other"),

    figure(31, 2, "line", 1, "high", page_caption(31, 29), number=29,
           note="panel (b) of Figure 29: the optimal cross-section judged by the eclectic score, a "
                "single thin dashed U curve on ruled gridlines, x -8 to 8, y 0 to -3.5"),

    figure(31, 3, "line", 1, "high", page_caption(31, 29), number=29, legend="inside",
           note="panel (c) of Figure 29: the four optimal curves overplotted in one frame with the "
                "legend box inside at the upper right keying Vertical Air, Total Degree, Hybrid "
                "Scoring, Fit 1 and Fit 2, axes x -8 to 6, y -4 to 3; this is the only figure in "
                "the paper with a legend"),

    figure(32, 1, "line", 1, "high", None, number=30,
           note="width pair, left half: panel title width Vs Ereach, x axis width 13-18, y axis "
                "Ereach 1.32-1.39 with a x10^4 exponent tag, straight decreasing line; the caption "
                "Figure 30 prints under the p33 half of this six-panel exhibit, not here"),

    figure(32, 2, "line", 1, "high", None, number=30,
           note="width pair, right half: panel title width Vs VerticalAir, x axis width 13-18, y "
                "axis 9.0-9.9, straight increasing line; no panel letters anywhere in Figure 30"),

    figure(33, 1, "line", 1, "high", page_caption(33, 30), number=30,
           note="height pair, left half of the 2x2 block: panel title height Vs Ereach, x axis "
                "height 1-6, y axis 1.30-1.44 with the x10^4 tag, decreasing straight line"),

    figure(33, 2, "line", 1, "high", page_caption(33, 30), number=30,
           note="height pair, right half: panel title height Vs VerticalAir, x axis height 1-6, y "
                "axis 8.2-10.2, increasing curve through markers"),

    figure(33, 3, "line", 1, "high", page_caption(33, 30), number=30,
           note="flat pair, left half: panel title flat Vs Ereach, x axis flat 0-6, y axis 1.355-"
                "1.405 with the x10^4 tag, decreasing straight line"),

    figure(33, 4, "line", 1, "high", page_caption(33, 30), number=30,
           note="flat pair, right half: panel title flat Vs VerticalAir, x axis flat 0-6, y axis "
                "9.0-9.45, increasing straight line"),

    table(3, 1, 5, 4, rule="boxed", numeric=0, text=4, continued=True,
          note="header row Parameter / Parameter, then four body rows pairing a symbol with its "
               "meaning on each side: x,y,z; xdot,ydot,zdot; y',y''; z' on the left and s, E0, "
               "Eleave, Ereach on the right; the same grid continues on p4 with the force and "
               "energy symbols and no repeated header"),

    table(15, 2, 7, 6, rule="boxed", numeric=5, text=1,
          note="analytical-versus-numerical comparison: header Condition, Method, Vy, Vertical "
               "Air, Fly Distance, Duration of Fly, then two groups of three rows, Without "
               "friction and With friction, each running Analytical, Numerical, Error Ratio with "
               "values such as 11.2316 m/s and a 0.083 percent error cell"),

    table(16, 1, 5, 5, rule="boxed", numeric=4, text=1, continued=False,
          note="plus-or-minus-ten-percent sensitivity grid: header cells +10%, Vertical Air "
               "Change Percentage, -10%, Vertical Air Change Percentage beside an empty corner, "
               "then one row per changed parameter W, H, B and Zt, each listing the perturbed "
               "value and the percentage change; the Extended Model heading begins just below"),
]

TABLES = ITEMS[len(ITEMS) - 3:]
ITEMS = ITEMS[: len(ITEMS) - 3]

EXCLUDED = [
    excluded(4, 1, "split-across-pages",
             "continuation of the Parameters table begun on p3: the force and energy symbols N, "
             "f, m, theta, delta-h, Elost, Hf, Whuman, WG, alpha, beta, rho and the xt family, in "
             "the same four-column grid with no repeated header row; counted once, at p3"),
    excluded(6, 2, "fragment-of-other",
             "right-hand zoom of the Figure 6 corner in the y-z projection, counted as the third "
             "panel of that exhibit"),
    excluded(6, 3, "fragment-of-other",
             "left-hand zoom of the Figure 6 corner in the x-y projection, counted as the second "
             "panel of that exhibit"),
    excluded(12, 3, "fragment-of-other",
             "Flip 1 stage of the three-sketch Figure 11 sequence, whose caption prints under the "
             "second sketch on p13; counted as panel 1 of that exhibit"),
    excluded(13, 1, "fragment-of-other",
             "Twist stage of the Figure 11 sequence that the caption below it covers; counted as "
             "panel 2 of that exhibit"),
    excluded(27, 1, "not-an-exhibit",
             "single line of bold body text, 1) Optimize total duration of fly, measured only "
             "because it is set in a wide boxed run; a numbered sub-heading of the results "
             "section, not a figure or a formula block"),
]

RULES = [
    "a caption is quoted as the page sets it, so a bare printed label carries numbering "
    "Figure N and a label with a full stop carries Figure N. [caption.numbering]",
    "a panel measured as its own region still carries the shared caption of its exhibit, so "
    "the panel count lives in [geometry.panel_count] and the shared caption in "
    "caption.verbatim rather than in eleven different caption strings. [geometry.panel_count]",
    "an exhibit printed without any caption keeps caption_source none and zero "
    "caption.words instead of borrowing the nearest paragraph or heading. [caption.words]",
    "a colour-field panel with no key is recorded as heatmap-or-contour and its missing key "
    "is stated by a false [geometry.colorbar], not by widening the family. [geometry.colorbar]",
    "whether numeric ticks print decides if a crop is legible on its own, so it is recorded "
    "per exhibit in [geometry.printed_numbers]. [geometry.printed_numbers]",
    "a legend is recorded only where a key box keys series, so the single in-frame key of "
    "Figure 29 panel (c) is inside and every other plot in this paper is none. "
    "[geometry.legend]",
    "panels of one exhibit that sit on different pages keep their page in place and are "
    "ordered by [place.page_order] within the page, which is how the Figure 25 and Figure 30 "
    "blocks stay one exhibit across a page break. [place.page_order]",
]

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": "34 pages, 68 measured regions. Thirty numbered figures, three of them multi-panel "
            "blocks whose panels are measured separately (Figure 6 with 3, Figure 23 with 6, "
            "Figure 25 with 5, Figure 30 with 6 across the p32/p33 break), one unnumbered method "
            "flowchart on p24, three unnumbered body tables, and one key/value defaults grid that "
            "recurs on p21, p27 and p29 with no header row, recorded as table-as-figure because "
            "the table-grid block requires a header row these grids do not print. Figure 11 is a "
            "three-sketch sequence whose first sketch closes p12; it is counted once at the "
            "captioned region. The parameter list crosses the p3/p4 break and is counted once at "
            "p3. Display equations, the p27 sub-heading and both zoom fragments are excluded with "
            "reasons rather than dropped.",
}

def main() -> int:
    order = {(it["page"], round(it["bbox"][1], 2)): i for i, it in enumerate(ITEMS, 1)}
    page_seen: dict[int, int] = {}
    for it in ITEMS:
        key = (it["page"], round(it["bbox"][1], 2))
        it["place"]["doc_order"] = order[key]
        page_seen[it["page"]] = page_seen.get(it["page"], 0) + 1
        it["place"]["page_order"] = page_seen[it["page"]]
    tseen: dict[int, int] = {}
    for t in TABLES:
        tseen[t["page"]] = tseen.get(t["page"], 0) + 1
        t["place"]["doc_order"] = len(ITEMS) + tseen[t["page"]]
        t["place"]["page_order"] = page_seen.get(t["page"], 0) + tseen[t["page"]]
    out = PROXY / "pa17-payload.json"
    out.write_text(json.dumps(PAYLOAD, indent=1, sort_keys=True, ensure_ascii=False),
                   encoding="utf-8")
    print(f"wrote {out} items={len(ITEMS)} tables={len(TABLES)} "
          f"excluded={len(EXCLUDED)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
