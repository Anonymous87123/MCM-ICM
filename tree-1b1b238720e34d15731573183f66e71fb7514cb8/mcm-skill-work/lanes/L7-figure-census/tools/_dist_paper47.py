"""Hand pass for P-A-2013-23004-8dba2d4c (the "Ultimate Brownie Pan" paper: a heat model for
rectangular and polygonal pans, a centre-dot arrangement algorithm, and three optimisation tests,
21 pp + the two advertising sheets).

Seventy-seven measured regions resolve to 26 counted rows and 51 exclusions:

    23 figure rows + 3 tables = 26, plus 51 excluded = 77, unaccounted 0.

    p4-r1   Fig. 1   photograph cluster beside an isometric pan model
    p4-r2   Fig. 2   heat flow into the pan faces
    p5-r2   Fig. 3   3-D surface of the square pan
    p6-r1   Fig. 4   edge temperature curve of the square pan
    p6-r2   Fig. 5   3-D surface of the circular pan
    p7-r1   Fig. 6   temperature curves of eight polygon pans
    p7-r2   Table 3  deviation of temperature per polygon
    p8-r1   Fig. 7   curve fitting result, markers plus fitted line
    p9-r1   Fig. 8   five 2-D arrangement methods
    p10-r1  Fig. 9   labelled rectangle sketch
    p10-r2  Fig. 10  arrangement of rectangles
    p11-r1  Fig. 11  circle arrangement, pattern 1
    p11-r2  Fig. 12  circle arrangement, pattern 2
    p12-r1  Fig. 13  three different arrangements
    p12-r2  Fig. 14  regular dodecagon and circle
    p12-r3  Fig. 15  arrangement of heptagons
    p13-r1  Fig. 16  edges and centre matrix of the octagon
    p14-r1  Fig. 17  special condition of the hexagon
    p14-r2  Fig. 18  algorithm flowchart
    p15-r1  Fig. 19  oven, racks and bakes (three photographs)
    p15-r2  Table 4  arrangements for rectangle, hexagon, octagon
    p16-r1  Table 5  arrangements for the circle
    p16-r4  Fig. 20  best arrangement, test one
    p17-r1  Fig. 21  best arrangement, test two
    p17-r2  Fig. 22  best arrangement, test three
    p19-r1  Fig. 23  changes on round corners

Declared gaps: Table 1 (Notation, p3) and Table 2 (Parameters of Standard State, p5) print with
captions but return no measured region - the only region on p5 is a nine-path band over a line of
body text. Neither is a caption-only exhibit that could be forced into a bbox.

Excluded: the p5 text band (`not-an-exhibit`); the eight flowchart boxes of Figure 18 on p14 and
the six and two arrangement thumbnails inside Tables 4 and 5 (`fragment-of-other`); and the 34
regions of the two advertising sheets on p20-p21 (`background` for the two page-filling vector
panels, `not-an-exhibit` for everything else). The paper announces those sheets itself: "The
authors provided advertising sheets attached at the end of the article... See advertising Sheets
on Next Two Pages."

Figure labels are judged from crops, never from the caption word: eleven of the figures are
un-axed polygon line art, so they are `other` with an `other_note`.

Usage: python -I tools/_dist_paper47.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2013-23004-8dba2d4c"
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

INTRO = "未编号标题 Introduction"
MODEL1 = "未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon"
MODEL2 = "未编号标题 Model 2: Baking Pan Optimization Design Model"
MODELTEST = "未编号标题 Model test"
STRENGTHS = "未编号标题 Strengths and Weaknesses"

PATH = {
    4: ([INTRO, MODEL1], "model"),
    5: ([INTRO, MODEL1], "model"),
    6: ([MODEL1], "model"),
    7: ([MODEL1], "model"),
    8: ([MODEL2], "model"),
    9: ([MODEL2], "model"),
    10: ([MODEL2], "model"),
    11: ([MODEL2], "model"),
    12: ([MODEL2], "model"),
    13: ([MODEL2], "model"),
    14: ([MODEL2], "model"),
    15: ([MODELTEST], "test"),
    16: ([MODELTEST], "test"),
    17: ([MODELTEST], "test"),
    19: ([STRENGTHS], "evaluation"),
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# counted rows per page, so doc_order stays monotonic
VENTION = {4: 2, 5: 1, 6: 2, 7: 2, 8: 1, 9: 1, 10: 2, 11: 2, 12: 3, 13: 1,
           14: 2, 15: 2, 16: 2, 17: 2, 19: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def ctext(page: int, prefix: str) -> str:
    """The printed caption whose text starts with `prefix`, checked against the text layer."""
    for c in CTX["captions"]:
        if c["page"] == page and c["text"].startswith(prefix):
            text = c["text"]
            if schema.norm(text) not in schema.page_text(PID, page):
                raise KeyError((page, prefix))
            return text
    raise KeyError((page, prefix))


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH[page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": False,
        "section_kind": kind,
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, numbering: str, position: str = "below") -> dict:
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


def figure(page: int, reg: int, family: str, caption_text: str, *, numbering: str = "Fig. N",
           panels: int = 1, layout: str = "1", legend: str = "none", colorbar: bool = False,
           numbers: bool = False, labels: bool = False, other_note: str = "",
           note: str = "") -> None:
    ORDER.append((page, reg))
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption_text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": dict(NULL_MENTION),
        "caption": caption_block(caption_text, numbering),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": "surface-mesh" if family == "surface-or-3D" else "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, caption_text: str, *, rows: int, cols: int,
          numeric_cols: int, text_cols: int, note: str = "") -> None:
    ORDER.append((page, reg))
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": caption_text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": dict(NULL_MENTION),
        "caption": caption_block(caption_text, "Table N", "above"),
        "table": {
            "rows": rows, "cols": cols, "header_rows": 1,
            "rule_style": "booktabs", "zebra": False, "merged_cells": False,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "full", "orientation": "portrait",
            "continued": False, "note_sentence": "",
        },
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note})


def build() -> str:
    # --- model 1: the heat pictures ----------------------------------------------------
    figure(4, 1, "composite-panel", ctext(4, "Fig. 1"), panels=2, layout="1x2",
           note="Two different kinds of picture in one measured region: on the left a cluster of "
                "overlapping greyscale photographs of real metal and glass baking trays, "
                "tilted and unaligned; a heavy solid black arrow across the middle; and on the "
                "right an isometric wireframe drawing of a rectangular pan with a raised lip on "
                "four thin legs. The photograph cluster is photo-or-raster-image and the wireframe "
                "is un-axed line art, so the exhibit takes composite-panel rather than one label "
                "for the pair.")
    figure(4, 2, "flowchart-or-schematic", ctext(4, "Fig. 2"),
           labels=True,
           note="Isometric line drawing of the slab pan with straight arrows entering each of the "
                "four side faces and the top face and dashed arrows rising from the bottom, plus "
                "a key at the lower right - a short horizontal line with an arrowhead labelled "
                "'Heat flow'. No axes, no ticks, no numbers: the arrows carry the flux direction "
                "per face, which is what makes this a schematic rather than a sketch.")
    figure(5, 2, "surface-or-3D", ctext(5, "Fig. 3"), colorbar=True, legend="none",
           note="A MATLAB perspective surface of the square pan: two raised corners and a "
                "saddle-like dip, floor axes running -0.5 to 0.5 with only -0.5 and 0 labelled, "
                "height axis 366 to 378 by 2, a dark-red-to-yellow colour map and a vertical "
                "colour bar at the right reading 367 to 376 in steps of 1. The header line above "
                "the plot reads 'Time=10 Color: T Height: T'. One surface, no legend, no printed "
                "values.")

    # --- model 1: the curves -----------------------------------------------------------
    figure(6, 1, "line", ctext(6, "Fig. 4"), legend="inside", numbers=True,
           note="One boxed plot, y 'Tempurature /K' from 371.5 to 376.5 by 0.5, x unlabelled from "
                "-0.5 to 0.5 with ticks only at the ends and the centre. A single thin curve, "
                "symmetric, flat at 371.5 near the centre and rising to about 376.4 at both "
                "edges - the overcooking profile the paper is built on. One legend entry "
                "('Square') in a boxed frame inside the axes.")
    figure(6, 2, "surface-or-3D", ctext(6, "Fig. 5"), colorbar=True, legend="none",
           note="The same perspective rendering for the circular pan: a shallow bowl, hot yellow "
                "rim and dark-red centre, floor axes -0.8 to 0.6 by 0.2 with only the negative "
                "labels printed, height axis 362 to 370 by 2, colour bar at the right 363 to 368 "
                "in steps of 0.5. Header 'Time=10 Color: T Height: T'; one surface, no legend, no "
                "printed values.")
    figure(7, 1, "line", ctext(7, "Fig. 6"), legend="inside", numbers=True,
           note="Eight curves of one family on one pair of axes: y 'Tempurature /K' 368 to 377 by "
                "1, x unlabelled -0.5 to 0.5. The curves nest, each symmetric with a flat minimum "
                "at the centre, the top peaking near 376.6 and the lowest at about 368.5; the "
                "legend inside the axes stacks eight entries - Square, Pentagon, Hexagon, "
                "Heptagon, Octagon, Decagon, 14-gon, 16-gon - each with a sample line in a "
                "different red tone. Eight series, one family, so the family is line and the "
                "panel count stays one.")

    table(7, 2, ctext(7, "Table 3"), rows=10, cols=5, numeric_cols=4, text_cols=1,
          note="'Number of edges (m) | Overall standard deviation (sigma_w) | Deviation at the "
               "edges (sigma_m^2) | Standard deviation at the edges (sigma_m) | Per-unit value' "
               "over nine body rows: m = 4, 5, 6, 7, 8, 10, 14, 16 and infinity, the last cell "
               "carrying '(Circle)' on a second line. Header cells wrap onto two lines and are "
               "not otherwise merged. Horizontal rules only - above the header, under it and "
               "under the last row - with no verticals and no rules between body rows.")

    # --- model 2: arrangement drawings -------------------------------------------------
    figure(8, 1, "scatter", ctext(8, "Fig. 7"), legend="inside", numbers=True,
           note="Ten green filled circular markers plotted at the measured points over one "
                "straight blue line, the markers keyed 'Original' and the line 'Fitting Curve' in "
                "a boxed legend inside the upper right. x '1/m^2' from 0 to 0.07 by 0.01, y 'K' "
                "from 0 to 1.6 by 0.2, ticks on all four sides. The markers are the observations "
                "and the line is the fitted model, so the family follows the markers: scatter.")
    figure(9, 1, "other", ctext(9, "Fig. 8"), panels=5, layout="5",
           other_note="five un-axed tiling drawings in one region - a square split into a 2 by 2 "
                      "lattice, two hexagons, a cluster of four octagons and two variants of "
                      "three dot-centred polygons; packing thumbnails, not plots",
           note="The arrangement methods drawn as line art with no axes, no scale and no values: a "
                "square field split into a 2 by 2 lattice with a dot per cell, two overlapping "
                "hexagons each dot-centred, four octagons in a tight cluster with small diamond "
                "gaps, and two lower variants of three dot-centred polygons. Five drawings of one "
                "kind, so the family stays `other` with a panel count rather than composite.")

    figure(10, 1, "other", ctext(10, "Fig. 9"), labels=True,
           other_note="labelled rectangle sketch: a large L by W outline with S written inside, a "
                      "small inset l by w at the corner and the ratio L/W above; a definition "
                      "drawing, not a plot",
           note="A heavy-ruled rectangle labelled L along the top edge, W down the left edge and S "
                "inside, with a smaller rectangle inset at the lower-right corner labelled l, w "
                "and A, and the ratio 'A width to length ratio: L/W' set in italics above. Line "
                "art with no axes, no ticks and no data - the sketch that defines the packing "
                "variables used from here on.")
    figure(10, 2, "other", ctext(10, "Fig. 10"),
           other_note="arrangement drawing: a four row by eight column wall of ruled rectangles "
                      "lettered A, with a narrower right column; a packing pattern, not a plot",
           note="A wall of ruled rectangles - four rows by eight columns - each face lettered A, "
                "the rightmost column visibly narrower and separated by two or three extra thin "
                "rules per cell. No axes, no labels, no values: the rectangle packing pattern "
                "read off the centre-dot matrix.")
    figure(11, 1, "other", ctext(11, "Fig. 11"),
           other_note="circle lattice: four staggered rows of open circles each carrying a centre "
                      "dot, rows offset by half a circle; a packing pattern, not a plot",
           note="Four staggered rows of open circles, each with a filled centre dot, alternate "
                "rows shifted by half a circle so the discs overlap slightly - the hexagonal "
                "close-packing case for round pans. Line art only, no axes, no values.")
    figure(11, 2, "other", ctext(11, "Fig. 12"),
           other_note="circle lattice: a square-aligned four by four array of tangent circles "
                      "with centre dots; a packing pattern, not a plot",
           note="The square-aligned alternative: a four by four array of tangent circles, rows and "
                "columns in line rather than offset, a filled dot at every centre. No axes, no "
                "values; the pair with Figure 11 is the whole circle-arrangement argument.")
    figure(12, 1, "other", ctext(12, "Fig. 13"), panels=3, layout="1x3",
           other_note="three arrangement drawings side by side: a dotted 4 by 4 grid, a hexagon "
                      "packing and a staggered hexagon packing; patterns, not plots",
           note="Three panels of equal height side by side: a four by four dotted grid inside a "
                "heavy frame, dotted hexagons with centre dots and small diamond voids at the "
                "triple junctions, and staggered hexagon rows shifted by half a cell with a "
                "partial hexagon hanging off the right edge. Three drawings of one kind, so "
                "`other` with a panel count.")
    figure(12, 2, "other", ctext(12, "Fig. 14"),
           other_note="overlay drawing: one regular dodecagon and one circle of nearly equal "
                      "diameter printed on top of each other; a geometry sketch, not a plot",
           note="A regular dodecagon and a circle of almost the same diameter drawn as two thin "
                "overlapping outlines, the mismatch showing at the vertices at the sides and the "
                "top - the argument that a many-sided polygon may be treated as a circle. Empty "
                "interiors, no axes, no labels.")
    figure(12, 3, "other", ctext(12, "Fig. 15"),
           other_note="heptagon lattice: about sixteen heptagons in four offset rows with diamond "
                      "gaps; a packing pattern, not a plot",
           note="Roughly sixteen heptagons in four offset rows, tessellating with diamond-shaped "
                "gaps between adjacent rows and contact along alternate edges only - the odd-sided "
                "case the paper later admits its model handles badly. Line art, no axes, no "
                "values.")
    figure(13, 1, "other", ctext(13, "Fig. 16"),
           other_note="centre-dot matrix drawing: a plane-filling lattice of dotted octagon and "
                      "hexagon outlines with centre dots, a heavy rectangle laid over it, and two "
                      "bare arrow axes with no scale",
           note="Two thin arrow axes with no ticks, no scale and no labels, over a plane-filling "
                "lattice of dotted octagon and hexagon outlines each with a solid centre dot, and "
                "a heavy black rectangle overlaid slightly skewed so its lower-left corner sits on "
                "the lattice. Recorded as `other`, not scatter: the marks are polygon cells, not "
                "measured points, and the axes carry no scale.")
    figure(14, 1, "other", ctext(14, "Fig. 17"),
           other_note="centre-dot matrix drawing: the same dotted hexagon lattice with two heavy "
                      "rectangles crossing at right angles; an arrangement sketch, not a plot",
           note="The same dotted hexagon lattice and bare arrow axes as Figure 16, with two heavy "
                "rectangles crossing at right angles - the rack before and after a ninety-degree "
                "rotation. The special case the flowchart's hexagonal branch is written for. No "
                "axes scale, no values.")
    figure(14, 2, "flowchart-or-schematic", ctext(14, "Fig. 18"),
           note="The full algorithm as a flowchart: rounded Start and End terminals, two "
                "parallelograms (input boundary equations; output N), four decision diamonds "
                "('Select a dot', 'The dot within boundaries?', 'Dot meets the arranging "
                "conditions?') and four process rectangles (initialise N = 0, build the centre-dot "
                "matrix, calculate distances, N = N + 1), joined by arrows labelled Yes and No, "
                "with a bracketed two-item note at the right about the least distance and the "
                "inscribed radius. A bold in-figure title block duplicates the printed caption. "
                "Its eight text boxes return as separate measured rasters on the same page and "
                "are excluded as parts of it.")

    # --- model test --------------------------------------------------------------------
    figure(15, 1, "photo-or-raster-image", ctext(15, "Fig. 19"), panels=3, layout="1x3",
           note="Three catalogue photographs side by side on white: a black countertop toaster "
                "oven seen at three-quarter view with three knobs and bakes visible through the "
                "glass; an overlapping scatter of wire cooling racks and two black pans; and a "
                "tray of finished bakes. The caption names the source URL in the line above. No "
                "axes, no numbers - a photograph set, not a plot.")
    table(15, 2, ctext(15, "Table 4"), rows=4, cols=3, numeric_cols=0, text_cols=3,
          note="'Shape | Arranging pattern 1 | Arranging pattern 2' over three body rows - "
               "Rectangle, Regular hexagon, Regular octagon. The two pattern columns hold "
               "thumbnails rather than numbers, one per cell, with 'See Condition 1' and 'Square' "
               "printed under two of them. Horizontal rules above the header, under the header and "
               "under the last row, no verticals. The six thumbnails return as separate measured "
               "rasters and are parts of this table.")
    table(16, 1, ctext(16, "Table 5"), rows=2, cols=3, numeric_cols=0, text_cols=3,
          note="The same three headings with one body row, Circle: pattern 1 is a staggered "
               "hexagonal-close packing of about seventeen dot-centred circles, pattern 2 a "
               "four by five rectilinear grid of them. 'Basic parameters:' follows below the "
               "table. Horizontal rules only. Its two thumbnails return as separate rasters and "
               "are parts of the table.")
    figure(16, 4, "heatmap-or-contour", ctext(16, "Fig. 20"),
           note="A black rectangular plate holding four staggered rows of five hexagons, each "
                "hexagon filled with a smooth radial greyscale gradient - pale at the rim, darker "
                "toward the centre - and dark high-temperature wedges at the shared corners. The "
                "temperature field is rendered straight onto the pan cells: no axes, no ticks, no "
                "colour bar, no legend, no printed values. The parameter line above gives m = 6, "
                "a = 3.3981 cm.")
    figure(17, 1, "heatmap-or-contour", ctext(17, "Fig. 21"),
           note="The same plate rendering for the octagon: three rows of five octagons in a "
                "gap-bridging honeycomb arrangement, each filled with the radial greyscale field "
                "and dark contact wedges at the corners. No axes, no colour bar, no legend, no "
                "printed values.")
    figure(17, 2, "heatmap-or-contour", ctext(17, "Fig. 22"),
           note="The third plate: four rows of five octagons, rows two and four offset in a "
                "staggered brick packing, same radial greyscale fill and dark corner wedges. "
                "Parameter line above reads m = 8, a = 2.4926 cm. No axes, no colour bar, no "
                "printed values.")
    figure(19, 1, "composite-panel", ctext(19, "Fig. 23"), panels=3, layout="1x3",
           colorbar=True,
           note="A measured region holding two kinds of artwork: a top strip of line art - a plain "
                "hollow square, a heavy right arrow and a hollow square with rounded corners, no "
                "axes and no labels - and below it two side-by-side 3-D surface plots titled "
                "'Time=10 Color: T Height: T', z 366 to 378 and 366 to 376, floor axes -1 to 1, "
                "red-to-yellow surfaces with two corner peaks, each with its own colour bar at the "
                "right. Schematic plus two surfaces, so composite-panel with three panels.")

    # --- excluded regions ---------------------------------------------------------------
    excluded(5, 1, "not-an-exhibit",
             "A nine-path vector band laid over one line of running body text ('temperature of the "
             "air. The boundary condition is Neumann boundary condition...') - a text-run wrapper, "
             "not an exhibit. Table 2, whose caption prints on this page, returns no region of its "
             "own and is a declared gap.")

    FLOW = ("One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined "
            "to the rest by its arrows, not an exhibit of its own. ")
    for reg, box in ((3, "decision diamond 'Select a dot / dot within ranges ?'"),
                     (4, "parallelogram 'Input Boundary equations and the shapes of polygon'"),
                     (5, "parallelogram 'Output N as the result'"),
                     (6, "decision diamond 'The dot within boundaries ?'"),
                     (7, "rectangle 'Build the center dot matrix of an arrangement'"),
                     (8, "rectangle 'Calculate the distance between the dot and all the boundaries'"),
                     (9, "rectangle 'Initialize the Number of polygon in this arrangement N = 0'"),
                     (10, "decision diamond 'Dot meets the arranging conditions ?'")):
        excluded(14, reg, "fragment-of-other", FLOW + f"Carries the {box}.")

    for reg, row in ((3, "Rectangle, pattern 1"), (4, "Rectangle, pattern 2"),
                     (5, "Regular hexagon, pattern 1"), (6, "Regular hexagon, pattern 2"),
                     (7, "Regular octagon, pattern 1"), (8, "Regular octagon, pattern 2")):
        excluded(15, reg, "fragment-of-other",
                 f"The arrangement thumbnail printed in the {row} cell of Table 4 - a raster "
                 "inside the table, counted with the table, not a figure.")
    for reg, row in ((2, "Circle, pattern 1"), (3, "Circle, pattern 2")):
        excluded(16, reg, "fragment-of-other",
                 f"The arrangement thumbnail printed in the {row} cell of Table 5 - a raster "
                 "inside the table, counted with the table, not a figure.")

    SHEET = ("A region of the advertising sheets the paper announces on p19 ('See advertising "
             "Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, "
             "with no figure number, no table number and no caption line anywhere on the page.")
    excluded(20, 3, "background",
             "The page-filling vector panel of the first advertising sheet - the printed border "
             "and gold banner that carry the folio and the display title. " + SHEET)
    excluded(21, 1, "background",
             "The page-filling vector frame of the second advertising sheet, carrying the running "
             "head 'THE ULTIMATE BROWNIE PAN | TEAM # 23004 | PAGE 20 OF 20'. " + SHEET)
    for reg in range(1, 19):
        if reg == 3:
            continue
        excluded(20, reg, "not-an-exhibit",
                 "A text band or a picture of the first advertising sheet ('The Ultimate Brownie "
                 "Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with "
                 "its two recoloured heat fields). " + SHEET)
    for reg in range(2, 17):
        excluded(21, reg, "not-an-exhibit",
                 "A text band or a product rendering of the second advertising sheet "
                 "('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon "
                 "and circle pan renderings with sales copy). " + SHEET)

    rules = [
        "No figure and no table is cited by number anywhere in this paper: all 28 captions print "
        "as 'Fig. N' or 'Table N' and every pointer in the prose is deictic ('The flow chart of "
        "Algorithm is listed as follow.'), so every mention block is empty [mention.count].",
        "Eleven of the twenty-three figures are polygon lattices, arrangement thumbnails or "
        "labelled sketches with no axes, no scale and no data, so they carry family `other` with "
        "an `other_note` naming what they draw [geometry.family].",
        "Figures 3 and 5 are MATLAB perspective surfaces with a colour bar; Figures 20 to 22 "
        "render the same temperature field straight onto the pan cells with no axes and no bar. "
        "The first pair is surface-or-3D, the plates are heatmap-or-contour [geometry.colorbar].",
        "Figures 1 and 23 each put two or three sub-plots of different kinds into one measured "
        "region (photograph beside a wireframe; line art above two surfaces), so both are "
        "composite-panel. Figures 8 and 13 repeat one kind and stay `other` with a panel count "
        "[geometry.panel_count].",
        "Figure 7 plots ten measured observations as markers with the fitted straight line over "
        "them: the markers are the data and the line is the model, so the family follows the "
        "markers [geometry.data_labels].",
        "All three recorded tables print horizontal rules only - above the header, under it and "
        "under the last row - with no verticals anywhere, so their rule style is `booktabs` "
        "[table.rule_style].",
        "Tables 4 and 5 hold arrangement thumbnails instead of numbers in their pattern columns, "
        "which is why both record a numeric column count of zero [table.numeric_cols].",
        "Table captions print above their grids and figure captions below their artwork; no "
        "exhibit in the paper mixes the two sides [caption.position].",
        "Only the 26 counted rows carry a printed caption line: the 34 regions of the two "
        "advertising sheets the paper announces on p19 have neither a figure number nor a caption "
        "sentence anywhere on the page, so they are excluded rather than counted [caption.verbatim].",
        "The paper prints unnumbered headings throughout, so `section_path` uses the printed "
        "titles in the unnumbered form, and 'Model 1: The Distribution of Heat at the Edges of "
        "Polygon' has to be recovered from the line where it shares the page with Figure 1's "
        "caption [place.section_numbered].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2013\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "A-23004-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Seventy-seven measured regions, all accounted: 23 figure rows, 3 recorded tables and "
            "51 exclusions. The 51 are the eight text boxes of the Figure 18 flowchart and the six "
            "plus two arrangement thumbnails inside Tables 4 and 5, all `fragment-of-other`; one "
            "text-run band on p5; and the 34 regions of the two advertising sheets on p20-p21, "
            "which the paper itself announces on p19. Tables 1 (Notation, p3) and 2 (Parameters of "
            "Standard State, p5) print with captions but return no measured region and are "
            "declared gaps. No exhibit in the paper is cited by number: all 28 captions print as "
            "'Fig. N' / 'Table N' and the prose points at exhibits only by position."
        ),
    }
    out = PROXY / "pb47-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
