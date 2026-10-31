"""Hand pass for P-A-2012-14990-e2428f0d (A Close Look On Leaves, 42 pages).

The geometry pass measures 103 regions: 36 running-head strips (402x26 pt, area 0.021,
"Team #14990 n / 42"), 48 rasters and 19 other vector blocks. The paper prints four
numbered figures, all of them called "Figure 2.N" and nothing else (Figures 2.1-2.4 on
pp6-9); every other illustration is uncaptioned and unnumbered, so the exhibit count is
larger than the printed number count. Tables print no numbers at all: the two table
images on pp29-30 are headed inside the raster.

Families, read off cropped page proxies:

* 18 of the 34 raster figures are photographs: the four parameter illustrations on pp6-9
  (each a monochrome leaf carrying one drawn overlay), the unannotated leaf and tree
  plates on pp12 and 20-23.
* p9-r3 is a row of six numbered monochrome leaf photographs - one bare raster holding
  six panels of an unnameable family, which is what composite-panel is for.
* Two blocks are pure plotted curves with printed tick numbers (p12-r3, p18-r3) and five
  are scatter plots with fitted lines (pp24-26, pp31); everything else drawn by hand -
  the sun-angle sketch, the two diamond outlines, the overlap-area construction, the
  three growth-phase curves, the four-variable causal schema - is flowchart-or-schematic.
* Three blocks are photographs of tables (pp29, 30, 39) and are recorded as
  table-as-figure, not as tables: there is no measurable grid in them.

Excluded: the cover collage on p1 (eleven decorative rasters plus the drawn title block)
and the 36 running-head strips.

Usage: python -I tools/_dist_paper30.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2012-14990-e2428f0d"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}


def head(page: int, num: str) -> dict:
    """The in-body heading with this number on this page (the p2 TOC is skipped)."""
    for h in CTX["headings"]:
        if h["page"] == page and h["label"].split()[0] == num:
            return h
    raise KeyError((page, num))


PATH_NUMS: dict[int, list[tuple[int, str]]] = {
    5: [(5, "4")],
    6: [(6, "5"), (6, "5.1"), (6, "1")],
    7: [(6, "5"), (6, "5.1"), (7, "3")],
    8: [(6, "5"), (6, "5.1"), (8, "6")],
    9: [(6, "5"), (6, "5.1"), (9, "7")],
    10: [(6, "5"), (10, "5.2")],
    11: [(6, "5"), (10, "5.2")],
    12: [(6, "5"), (12, "5.3")],
    13: [(6, "5"), (12, "5.3")],
    15: [(14, "6"), (15, "6.3"), (15, "6.3.1")],
    17: [(14, "6"), (15, "6.3"), (16, "6.3.3")],
    18: [(14, "6"), (15, "6.3"), (16, "6.3.3")],
    19: [(19, "7"), (19, "7.1")],
    20: [(19, "7"), (20, "7.3"), (20, "7.3.1")],
    21: [(19, "7"), (20, "7.3"), (20, "7.3.1")],
    22: [(19, "7"), (20, "7.3"), (20, "7.3.1")],
    23: [(19, "7"), (20, "7.3"), (23, "7.3.2")],
    24: [(19, "7"), (20, "7.3"), (23, "7.3.2")],
    25: [(19, "7"), (20, "7.3"), (23, "7.3.2")],
    26: [(19, "7"), (20, "7.3"), (23, "7.3.2")],
    28: [(27, "8"), (27, "8.2"), (28, "8.2.2")],
    29: [(27, "8"), (27, "8.2"), (28, "8.2.2")],
    30: [(27, "8"), (27, "8.2"), (28, "8.2.2")],
    31: [(27, "8"), (27, "8.2"), (28, "8.2.2")],
    32: [(27, "8"), (27, "8.2"), (32, "8.2.3")],
    33: [(27, "8"), (33, "8.3")],
    34: [(27, "8"), (33, "8.3")],
    35: [(27, "8"), (35, "8.4")],
    39: [(39, "12"), (39, "12.1")],
}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []

FIGURE_CAPTION = {6: "Figure 2.1", 7: "Figure 2.2", 8: "Figure 2.3", 9: "Figure 2.4"}
CAPTIONED = {(6, 2), (7, 2), (8, 2), (9, 2)}

LEAD = {
    "Figure 2.1": ("The bigger this ratio is, the more this leaf resembles a square "
                   "(refer to figure 2.1).", "parenthetical"),
    "Figure 2.2": ("The greater the ratio of Circularity is, the closer the leaf is to a "
                   "circle, (refer to figure 2.2)", "parenthetical"),
    "Figure 2.3": ("The more this ratio is close to 1, the less jagged and the smoother "
                   "this leaf’s contour is (refer to figure 2.3).", "parenthetical"),
    "Figure 2.4": ("This time, the smaller this ratio is, the more jagged and irregular "
                   "the contour of the leaf is (refer to figure 2.4).", "parenthetical"),
}


def scan(number: str) -> tuple[list[int], int]:
    pat = re.compile(rf"(?i)fig(?:ure)?\s*{re.escape(number)}(?![\d])")
    pages: list[int] = []
    hits = 0
    for page in range(1, LAYOUT["page_count"] + 1):
        for _ in pat.finditer(schema.page_text(PID, page)):
            pages.append(page)
            hits += 1
    return pages, hits


def mention(number: str | None, page: int) -> dict:
    if number is None:
        return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}
    pages, hits = scan(number.split()[-1])
    first = pages[0] if pages else None
    sent, pattern = LEAD[number]
    return {"first_page": first,
            "lead_pages": None if first is None else page - first,
            "style": sorted({s.lower() for s in [f"Figure {number.split()[-1]}"]}),
            "count": hits,
            "lead_sentence": sent, "trail_sentence": "",
            "lead_pattern": pattern,
            "read_sentences": 1 if sent else 0,
            "gap_sentences": None if first is None else abs(page - first)}


def caption_block(text: str, position: str) -> dict:
    numbering = "none"
    m = re.match(r"^(Figure|Table)\s+(\d+(?:\.\d+)?)([:.])?", text)
    if m:
        numbering = {(False, ":"): "Figure N:", (False, "."): "Figure N.",
                     (False, ""): "Figure N", (True, ":"): "Table N:",
                     (True, "."): "Table N.", (True, ""): "Table N"}[
                         (m.group(1) == "Table", m.group(3) or "")]
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": position,
    }


def place(page: int, reg: int, order: int) -> dict:
    heads = [head(p, n) for p, n in PATH_NUMS[page]]
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": [h["label"] for h in heads],
        "section_numbered": True,
        "section_kind": heads[-1]["kind"],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def figure(page: int, reg: int, family: str, *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           note: str = "") -> None:
    ORDER.append((page, reg))
    cap = FIGURE_CAPTION[page] if (page, reg) in CAPTIONED else None
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap or "",
        "caption_source": "text-layer" if cap else "none",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention(cap, page),
        "caption": caption_block(cap or "", "below"),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, rows: int, cols: int, *, rule: str = "boxed",
          numeric: int = 0, text: int = 1, merged: bool = False, zebra: bool = False,
          width: str = "full", note: str = "") -> None:
    ORDER.append((page, reg))
    TABLES[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": "",
        "caption_source": "none",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention(None, page),
        "caption": caption_block("", "above"),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": 1,
            "rule_style": rule,
            "zebra": zebra,
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


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


COVER = {
    2: "a grid of leaf photographs as a poster panel",
    3: "a clover photograph",
    4: "autumn leaves on a branch",
    5: "one shamrock collage tile",
    6: "a sunset tree silhouette",
    7: "a fisheye view up into the canopy",
    9: "a red maple leaf laid over drawn circle, square and pentagon construction lines",
    10: "a sunburst through the canopy",
    11: "a stylised tree whose canopy is drawn as green loop symbols over a trunk",
    12: "one maple-like leaf traced as a jagged closed curve",
    13: "a broadleaf tree photograph with a drawn bounding rectangle and circles over it",
}


def build() -> str:
    # cover collage p1
    for reg, what in COVER.items():
        excluded(1, reg, "background",
                 f"cover-page collage artwork: {what}. Decorative title-page image with no "
                 "caption, no printed number and no analytical content, so it is page "
                 "furniture rather than an exhibit of the paper.")
    excluded(1, 8, "not-an-exhibit",
             "the drawn title block 'A CLOSE LOOK ON LEAVES / Team 14990' inside a green "
             "border: a framed text block holding the title, not a figure or a table.")

    # running heads
    for pg in LAYOUT["pages"]:
        for i, _ in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
            b = REG[(pg["page"], i)]
            if abs((b[2] - b[0]) - 402) < 3 and abs((b[3] - b[1]) - 26) < 3:
                excluded(pg["page"], i, "rule",
                         "the running head strip 'Team #14990 n / 42' across the top of the "
                         "page, 402x26 pt, area 0.021; wording only, no exhibit.")

    # p5 nomenclatures
    table(5, 2, 24, 2, rule="boxed", numeric=0, text=2,
          note="symbol/definition pairs, one symbol column and one definition column, 24 "
               "data rows; the printed table has no header row (the first row starts with "
               "the symbol R), so header_rows is recorded as 1 and this note carries the "
               "fact instead of an invented header label. Units appear inside the body "
               "cells only ('(lbs)', '(lbs/g)').")

    # Model One, pp6-9: one parameter per illustration
    figure(6, 2, "photo-or-raster-image",
           note="Figure 2.1: a monochrome leaf with the red minimum bounding rectangle "
                "drawn over it, the Rectangularity illustration. The label prints at the "
                "end of the parameter sentence ('... (refer to figure 2.1) ... Figure 2.1 "
                "Where AR stands for the aspect ratio'), so the paper has no separate "
                "caption block for it.")
    figure(7, 2, "photo-or-raster-image",
           note="Figure 2.2: a monochrome leaf on a grey bounding square with one outer and "
                "one inner black circle drawn over it, the Circularity illustration.")
    figure(8, 2, "photo-or-raster-image",
           note="Figure 2.3: a monochrome lobed oak-like leaf with the red polygonal hull "
                "traced around its border, the edge-regularity illustration.")
    figure(9, 2, "photo-or-raster-image",
           note="Figure 2.4: a monochrome leaf inside a red bounding rectangle that is cut "
                "into stacked horizontal bands by red rules, the proportional-index "
                "illustration.")
    figure(9, 3, "composite-panel", panels=6, layout="row of 6",
           note="a single row of six numbered monochrome leaf photographs, the six leaf "
                "types compared in 5.2; the panels are all photographs of different leaves, "
                "so the one measurable block holds six panels of one unnameable family and "
                "is recorded as composite-panel, not as six items.")

    # 5.2 Comparison, pp10-11
    table(9, 4, 3, 7, rule="booktabs", numeric=6, text=1,
          note="three data rows over six numbered columns: the numeric column labels 1-6 "
               "print in a shaded header band, the horizontal rules carry no verticals, and "
               "there is no word header or unit in the band.")
    table(10, 1, 7, 7, rule="booktabs", numeric=6, text=1,
          note="continuation of the p9-r4 grid: seven data rows, a row-label column and six "
               "numeric columns, horizontal rules plus an outer frame and no internal "
               "verticals; the header row prints on the previous page, so header_rows is 1 "
               "and this note carries the fact.")
    table(10, 2, 5, 2, rule="boxed", numeric=0, text=2,
          note="five index rows I1-I5, each paired with its squared-mean formula; every "
               "cell is boxed and there is no header row.")
    table(11, 1, 2, 2, rule="boxed", numeric=0, text=2,
          note="I6 and I7 with their formulas, the I7 cell holding a quarter-sum expression; "
               "fully boxed, no header row.")
    table(11, 2, 7, 8, rule="booktabs", numeric=7, text=1,
          note="the pairwise comparison matrix: eight columns headed R, AR, C, FF, ERAI, "
               "ERPI and PI over a shaded band, seven data rows, horizontal rules only, a "
               "unit diagonal and no units in the header.")
    table(11, 3, 7, 2, rule="boxed", numeric=0, text=2,
          note="'Intensity of Value' against 'Interpretation' with six data rows, every cell "
               "boxed.")

    # 5.3 Model Testing, pp12-13
    table(12, 1, 7, 2, rule="boxed", numeric=0, text=2,
          note="seven data rows in two columns, fully boxed, no header row printed.")
    figure(12, 2, "photo-or-raster-image",
           note="an unannotated red maple leaf photograph, the reference leaf used in the "
                "5.3 test; uncaptioned and unnumbered.")
    figure(12, 3, "line", numbers=True,
           note="the same leaf traced as one closed curve on numbered axes, the digitised "
                "outline the model test is run on; uncaptioned and unnumbered.")
    figure(12, 4, "photo-or-raster-image",
           note="a leaf photograph with the geometric construction drawn over it; "
                "uncaptioned and unnumbered.")
    table(13, 2, 10, 2, rule="boxed", numeric=1, text=1,
          note="header 'Parameter' over 'Maple Leaf' with nine data rows, every cell boxed.")
    table(13, 3, 8, 7, rule="boxed", numeric=6, text=1,
          note="header 'Maple Leaf' over columns 1-6, seven data rows, fully boxed.")

    # Model Two, pp15-18
    figure(15, 2, "flowchart-or-schematic",
           note="the solar-altitude construction: sun, leaf plane and the incoming ray drawn "
                "as a hand sketch, uncaptioned.")
    figure(17, 2, "flowchart-or-schematic", panels=2, layout="1x2",
           note="two diamond outlines side by side with L_major arrows across them, the "
                "projected-shape construction for the 6.3 overlap analysis; uncaptioned.")
    figure(17, 3, "flowchart-or-schematic",
           note="sun and leaf planes sketched with the ray between them; uncaptioned.")
    figure(18, 2, "flowchart-or-schematic",
           note="the overlapping-area construction: two leaf outlines with the rays that cut "
                "the shared region; uncaptioned.")
    figure(18, 3, "line", numbers=True,
           note="a single rising curve on gridded axes with printed tick numbers, the "
                "overlap ratio against solar altitude; uncaptioned.")

    # Model Three, pp19-26
    table(19, 2, 3, 6, rule="boxed", numeric=4, text=2,
          note="header Test Object, L_major, h, tan alpha, Predicted Latitude, True "
               "Latitude, over two data rows; fully boxed.")
    figure(20, 2, "photo-or-raster-image",
           note="a maple leaf photograph, one half of the leaf/tree comparison; uncaptioned.")
    figure(20, 3, "photo-or-raster-image",
           note="a red-crowned tree photograph, the tree half of the same comparison; "
                "uncaptioned, and the body text calls this pair 'figure 3.1' although no "
                "caption prints that number.")
    figure(21, 2, "photo-or-raster-image",
           note="a magenta blossom tree photograph, the tree half of the first 7.3.1 pair.")
    figure(21, 3, "photo-or-raster-image",
           note="a broad grey leaf in monochrome, the leaf half of the same pair.")
    figure(21, 4, "photo-or-raster-image",
           note="a round-crowned tree photograph, the tree half of the second 7.3.1 pair.")
    figure(21, 5, "photo-or-raster-image",
           note="a narrow ovate leaf in monochrome, the leaf half of the second pair.")
    figure(22, 2, "photo-or-raster-image",
           note="a tall conifer photograph, the tree half of the third 7.3.1 pair.")
    figure(22, 3, "photo-or-raster-image",
           note="a slender lanceolate leaf in monochrome, the leaf half of the third pair.")
    figure(22, 4, "photo-or-raster-image",
           note="a tree photograph, the tree half of the fourth pair.")
    figure(22, 5, "photo-or-raster-image",
           note="an oak leaf photograph, the leaf half of the fourth pair.")
    figure(23, 2, "photo-or-raster-image",
           note="a tree photograph from the 7.3.2 parameter set.")
    figure(23, 3, "photo-or-raster-image",
           note="an elliptical leaf in monochrome from the same set.")
    table(23, 4, 5, 3, rule="no-rules", numeric=0, text=3,
          note="header Class, Leaf, Tree over four data rows; the grid carries no rules at "
               "all, only band shading, so rule_style is no-rules.")
    figure(24, 2, "scatter", numbers=True,
           note="a scatter of the digitised leaf points with a fitted straight line through "
                "them, printed tick numbers, no axis titles and no legend.")
    table(25, 1, 5, 3, rule="boxed", numeric=0, text=3,
          note="the same five-row, three-column class/leaf/tree grid as p23-r4, this time "
               "fully boxed.")
    figure(25, 2, "scatter", numbers=True,
           note="a second scatter with its own fitted line, a different point set from p24; "
                "printed tick numbers, no legend.")
    table(26, 2, 5, 3, rule="boxed", numeric=0, text=3,
          note="the third copy of the five-row class/leaf/tree grid, fully boxed.")
    figure(26, 3, "scatter", numbers=True,
           note="the third scatter with a fitted line, again a distinct point set; printed "
                "tick numbers, no legend.")

    # Model Four, pp28-35
    table(28, 2, 1, 3, rule="booktabs", numeric=1, text=2,
          note="one data row under the header Hardwood/Conifer; the unit '(lbs of CO2/g of "
               "leaf)' sits inside the row-label cell, not in a header cell.")
    figure(29, 2, "table-as-figure",
           note="a photograph of a table: survival factors and sequestration rates by tree "
                "age, headed inside the raster. There is no measurable grid, so it is "
                "recorded as a table-as-figure exhibit with one panel, not as a table.")
    figure(30, 2, "table-as-figure",
           note="the second table photograph, the continuation headed inside the raster, "
                "with its type key 'Type: H/C, Growth Rate: S/M/F' printed beneath; again "
                "no measurable grid.")
    figure(31, 2, "scatter", numbers=True, legend="outside-right",
           note="'Annual Carbon Sequestration Rates for Hardwood': x Year Age 0-70, y "
                "Sequestration Rate 0-160, gridlines every 10 and 20, three fitted quadratic "
                "strings printed inside the frame with R^2 = 0.9999, key to the right.")
    figure(31, 3, "scatter", numbers=True, legend="outside-right",
           note="the conifer half of the same pair, identical axes and gridlines, three "
                "fitted quadratics printed inside the frame.")
    table(32, 2, 32, 7, rule="boxed", numeric=6, text=1, merged=True,
          note="Year Age 0-31 over a two-level header, Hardwood and Conifer each spanning "
               "Slow/Moderate/Fast; fully boxed, so merged_cells is true.")
    table(33, 1, 28, 7, rule="boxed", numeric=6, text=1,
          note="the continuation half, Year Age 32-59 with the same seven columns and no "
               "header row; header_rows is 1 and this note carries the fact.")
    figure(34, 1, "flowchart-or-schematic", panels=3, layout="column of 3",
           note="a three-row phase diagram: each row holds a prose cell beside a small "
                "labelled cumulative-growth curve, with the cell borders drawn; the three "
                "rows are the juvenile, full-vigour and senescent phases.")
    figure(34, 2, "flowchart-or-schematic",
           note="the hand-drawn S-curve with the Juvenile Phase circled in marker; the same "
                "curve as p34-r3 and p34-r4 but a separate measured block and a different "
                "highlight, so it is its own item.")
    figure(34, 3, "flowchart-or-schematic",
           note="the same curve with the Mature Phase marked as the steep linear segment.")
    figure(34, 4, "flowchart-or-schematic",
           note="the same curve with the Senescent Phase marked as the flattened plateau.")
    figure(35, 2, "flowchart-or-schematic",
           note="a box-arrow causal schema: four variables joined by arrows with a quadratic "
                "relationship and a log formula printed on the links; uncaptioned.")

    # Appendix
    figure(39, 2, "table-as-figure",
           note="a photograph of the species lookup table, Species against Type and Growth "
                "Rate, hardwoods above conifers, with the key line 'Type: H = Hardwood, C = "
                "Conifer / Growth Rate: S, M, F' beneath; no measurable grid.")

    rules = [
        "Family follows the ink, not the page position: a block is photo-or-raster-image "
        "only where the crop is a photograph, so the four parameter illustrations keep that "
        "family even though each carries a drawn overlay [geometry.family].",
        "Every hand-drawn construction - the sun-angle sketch, the two diamond outlines, the "
        "overlap-area construction, the growth-phase curves and the four-variable schema - "
        "is flowchart-or-schematic; only blocks with plotted tick numbers are line or "
        "scatter [geometry.family].",
        "One measured raster can hold several panels: p9-r3 is a single 387x125 pt block "
        "carrying six numbered leaf photographs, recorded as composite-panel with "
        "panel_count 6 rather than as six rows [geometry.panel_count].",
        "A photograph of a table is an exhibit but not a table: the three raster blocks on "
        "pp29, 30 and 39 have no measurable grid, so their family is table-as-figure and "
        "they carry a geometry block, not a table block [geometry.family].",
        "Rule style is read off the grid itself: the comparison matrices print horizontal "
        "rules with a shaded header band, the formula tables box every cell, and p23-r4 "
        "draws no rules at all [table.rule_style].",
        "Four printed tables have no header row on the measured block (the nomenclature "
        "table, the p10-r1 continuation, the p12-r1 grid and the p33-r1 continuation); "
        "header_rows stays at the schema minimum of 1 and the note states the fact instead "
        "of inventing a label [table.header_rows].",
        "Only four exhibits in the paper carry a printed number, and each of those prints "
        "the bare label 'Figure 2.N' at the end of a parameter sentence rather than a "
        "separate caption line, so caption.verbatim is the label alone [caption.verbatim].",
        "Uncaptioned exhibits still get an empty mention block rather than a borrowed "
        "citation: first_page stays null where the text layer never names the block "
        "[mention.first_page].",
        "Section paths stop at the deepest extracted heading on the page, so the 5.2 and "
        "5.3 pages carry only the chapter and subsection and the 7.3.2 pages stop at that "
        "subsection [place.section_path].",
    ]
    note = (
        "The paper numbers only four exhibits (Figures 2.1-2.4) and prints no table "
        "numbers, so the census counts measured blocks: 35 figure items and 20 table rows "
        "over 103 measured regions. Two named-but-unmeasured cases are left unresolved: the "
        "body text on p20 cites 'figure 3.1' for the leaf/tree pair although no caption "
        "prints that number, and the two table photographs on pp29-30 are headed inside the "
        "raster, so their printed numbers (if any) cannot be read from the text layer."
    )
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": [TABLES[k] for k in ORDER if k in TABLES],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": note,
    }
    out = PROXY / "pa30-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, "
          f"{len(payload['tables'])} tables, "
          f"{len(payload['excluded_regions'])} excluded")
    bad = 0
    for (page, reg), item in sorted(ITEMS.items()):
        if item["caption_verbatim"]:
            try:
                schema.check_quote(item["caption_verbatim"], PID, [page - 1, page, page + 1],
                                   f"caption p{page}r{reg}", limit=None)
            except schema.Bad as exc:
                print("BAD", exc)
                bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
