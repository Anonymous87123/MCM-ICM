"""Hand pass for P-E-2017-67171-0a99e096 (smart growth, Edinburgh and Wellington).

Shape of the paper: a three-dimensional cube for measuring smart growth, then a linear-programming
update of it, then two case studies. Nine printed figures and ten printed tables (the numbering
skips Table 9), against 36 measured regions and 17 exclusions - the exclusions being ten equation
fragments on pages 11-12, one on page 19, two table continuations across page breaks, two extra
panels of a three-panel figure, one stray box around reference text and one undetermined small
vector on page 7.

What the record has to say out loud:

1. No exhibit is ever cited by number. Every "Fig N" and "Table N" string in the text layer is a
   caption; the prose refers only to "the following table", "the following figure", "the
   following list". So mention.style is empty and mention.first_page is null on all nineteen rows,
   and the deixis is what gets quoted as the lead sentence.
2. The numbering skips Table 9 outright, runs "Table1:" with no space, and mixes four printed
   prefixes: "Figure 1", "Table1:", "Table 2:", "Fig 3.", "Table 3." - recorded normatively with
   the printed form in every row note.
3. Three exhibits carry the same caption grammar defect: Figures 4, 5 and 6 print as three
   panels in one row whose captions interleave line by line in the text layer, so all three are
   typed from the crop.
4. Two tables break across a page turn and neither repeats its header: Table 6 (p13 -> p14) and
   Table10 (p17 -> p18). Table 1 breaks the other way - its caption and header row sit on p6,
   which returns no region at all, so the grid is measured only from its second line down.
5. Ten of the 36 measured regions are pieces of typeset equations on pages 11 and 12, and one
   more is equation (11) on p19 whose number sits outside the box. The detector boxes the math,
   not the paper.

Usage: python -I tools/_dist_paper136.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-E-2017-67171-0a99e096"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((LANE / f".proxy/{PID}-ctx.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

HEAD: dict[str, str] = {}
for _h in CTX["headings"]:
    _n, _l = _h.get("number"), _h.get("label")
    if not _n or not _l or not _l.startswith(_n + " "):
        continue
    if _n not in HEAD:
        HEAD[_n] = _l


def H(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


S_INTRO = ["未编号标题：I. Introduction"]
S_411 = H("4.1.1")
S_412 = H("4.1.2")

EXCLUDED = [
    {"page": 7, "bbox": REG[(7, 2)], "reason": "in-body-diagram",
     "note": "small typeset fragment inside section 4.1.2: the display form of the SGI "
             "definition, sitting between the paragraph that defines cos(CG,SG) and the table "
             "that summarises it. No caption, no frame, no equation number."},
    {"page": 8, "bbox": REG[(8, 1)], "reason": "fragment-of-other",
     "note": "middle panel of the three-panel Figure 2 ('Developing city'). The Figure 2 row "
             "carries the left panel ('Balanced city'); this and the right panel are the same "
             "exhibit under one caption. The three boxes sort middle-right-left by y, because their "
             "top edges differ by under 2 pt and the middle one starts highest."},
    {"page": 8, "bbox": REG[(8, 2)], "reason": "fragment-of-other",
     "note": "right panel of the three-panel Figure 2 ('Developed city'), same exhibit and one "
             "caption as the row's left panel."},
    {"page": 11, "bbox": REG[(11, 1)], "reason": "in-body-diagram",
     "note": "the constraint block of equation (6): the 's.t.' qualifier and the left brace over "
             "B >= 0, Delta S >= 0 and the budget sum. Typeset math with no caption and no frame. "
             "The box holds the brace only - the objective line 'max SGI' prints above its top edge "
             "and the number (6) at the right margin, both outside it."},
    {"page": 11, "bbox": REG[(11, 2)], "reason": "in-body-diagram",
     "note": "right-hand side of equation (7): the 3x7 coefficient matrix times the column vector "
             "of budget shares. The number (7) prints at the right margin outside the box."},
    {"page": 11, "bbox": REG[(11, 3)], "reason": "in-body-diagram",
     "note": "left-hand side of equation (7): the state-change vector written as a bracketed "
             "column of derivatives. The box stops short of the equality sign, which falls between "
             "this box and the right-hand-side box, inside neither."},
    {"page": 11, "bbox": REG[(11, 4)], "reason": "in-body-diagram",
     "note": "first display line of equation (8) on p11: the stacked state-difference matrix."},
    {"page": 11, "bbox": REG[(11, 5)], "reason": "in-body-diagram",
     "note": "second display line of equation (8), the matching budget matrix directly under the "
             "first; the single number (8) prints between the two lines, outside both boxes."},
    {"page": 12, "bbox": REG[(12, 1)], "reason": "in-body-diagram",
     "note": "an unnumbered display equation on p12: the squared norm of the residual. Typeset "
             "math with no caption, no frame and no number."},
    {"page": 12, "bbox": REG[(12, 2)], "reason": "in-body-diagram",
     "note": "equation (9) on p12 in full: the adjacent-year state difference written as a column "
             "of derivatives. The number (9) prints at the right margin, outside the box."},
    {"page": 12, "bbox": REG[(12, 3)], "reason": "in-body-diagram",
     "note": "equation (10) on p12, the one-step state update - matrix, optimal budget vector and "
             "state vector on one line. This is the worst-fitting box on either page: its right "
             "edge cuts the final column vector, so the closing bracket and the t subscript print "
             "outside it, and the number (10) is outside at the margin."},
    {"page": 12, "bbox": REG[(12, 4)], "reason": "in-body-diagram",
     "note": "upper of the two unnumbered displays at the foot of p12: the optimal budget vector "
             "written out as its seven components."},
    {"page": 12, "bbox": REG[(12, 5)], "reason": "in-body-diagram",
     "note": "lower of the two unnumbered displays at the foot of p12: the same vector primed, the "
             "starting point of the ranking. A third display line under it - the chain of "
             "inequalities that actually states the ranking - prints with no box at all."},
    {"page": 14, "bbox": REG[(14, 1)], "reason": "split-across-pages",
     "note": "foot of Table 6: the last two data rows (the negative EPI and SJI of the CG row and "
             "the SGI row) printed on p14 after the page turn. The Table 6 row carries the head on "
             "p13; no header repeats and no 'continued' marker is printed."},
    {"page": 18, "bbox": REG[(18, 1)], "reason": "split-across-pages",
     "note": "body of Table10 continuing from p17: ranks 1-7 plus the Average row, no header "
             "repeated, no 'continued' marker. The Table10 row carries the two-row header on p17."},
    {"page": 19, "bbox": REG[(19, 1)], "reason": "in-body-diagram",
     "note": "the closed-form line of the F-test equation group in section VI. The detector box "
             "holds only the F = MSR/MSE line; the equation number (11) prints one line above it "
             "at the right margin, outside the box, so the box under-covers the equation."},
    {"page": 22, "bbox": REG[(22, 1)], "reason": "not-an-exhibit",
     "note": "three lines of the reference list crossed by the measurement window (the tail of "
             "entry [16] and the first line of [17]). Text, not a grid: the only rules on the page "
             "are the running-head rules at the top and none of them intersects this box."},
]


def place(page: int, idx: int, path: list[str], kind: str, numbered: bool = True) -> dict:
    b = REG[(page, idx)]
    mid = (b[1] + b[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    frac = (b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H)
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 0,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": frac > 0.5,
    }


def caption(v: str, *, numbering: str, cond: bool = False, concl: bool = False,
            units: bool = False, vars_: int = 0, pos: str = "below",
            voice: str = "none") -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": units,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": cond,
        "concludes": concl,
        "voice": voice,
        "position": pos,
    }


def tcap(v: str, *, numbering: str) -> dict:
    """Every table caption here prints above its grid, and two of them state a unit."""
    return caption(v, numbering=numbering, pos="above", units="(%" in v)


def mention(page: int, *, first: int | None = None, style: list[str] | None = None,
            count: int = 0, lead: str = "", pattern: str = "none", read: int = 0,
            trail: str = "") -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style or [],
        "count": count,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def figure(page: int, idx: int, family: str, cap: dict, men: dict, *, path: list[str],
           kind: str, legend: str = "none", printed: bool = False, labels: bool = False,
           panels: int = 1, layout: str = "1", shared: bool = False, colorbar: bool = False,
           three_d: str = "no", numbered: bool = True, source: str = "text-layer",
           other_note: str | None = None, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "other_note": other_note,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "place": place(page, idx, path, kind, numbered),
        "mention": men,
        "caption": cap,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(page: int, idx: int, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, note: str = "", numbered: bool = True,
          source: str = "text-layer") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "place": place(page, idx, path, kind, numbered),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed", zebra: bool = False,
         merged: bool = False, diag: bool = False, units_hdr: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "column",
         orient: str = "portrait", continued: bool = False, note_sentence: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rules,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diag,
        "units_in_header": units_hdr,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": orient,
        "continued": continued,
        "note_sentence": note_sentence,
    }


_LIG = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"}


def _fold(s: str) -> tuple[str, list[int]]:
    out: list[str] = []
    idx: list[int] = []
    for i, ch in enumerate(s):
        rep = _LIG.get(ch, ch)
        for c in rep:
            out.append(c)
            idx.append(i)
    return "".join(out), idx


def _find(page: int, needle: str, after: int = 0) -> tuple[str, int, int]:
    t = text(page)
    f, idx = _fold(t)
    n, _ = _fold(needle)
    j = f.find(n, after)
    assert j >= 0, f"{needle!r} not on page {page}"
    return t, idx[j], idx[j + len(n) - 1] + 1


def _to_word_end(page: int, pos: int) -> int:
    t = text(page)
    k = t.find(" ", pos)
    return len(t) if k < 0 else k


def span(page: int, start: str, end: str) -> str:
    t, i, _ = _find(page, start)
    _, j, jend = _find(page, end, i)
    q = t[i:_to_word_end(page, jend)].strip()
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


ALL = [
    figure(4, 1, "other", caption("Figure 1 Three E's sustainability and related components",
                                  numbering="Figure N"),
           mention(4),
           path=S_INTRO, kind="introduction", numbered=False, other_note="sunburst",
           note="a colour sunburst: an inner disc labelled 'Smart Growth', a middle ring of three "
                "arcs ('Environmentally Friendly', 'Socially Equitable', 'Economically "
                "Prosperous') and an outer ring of nine wedges, three per E - Renewable Energy "
                "Consumption, Employment (Population), Number of Study participants, Gini "
                "Coefficient, Life Expectancy, GDP per Capita, Expense (% of GDP), Total "
                "Greenhouse Gas Emission, Forest Area. Every label sits inside its arc, so the "
                "drawing needs no legend, no axes and no numbers. The caption prints ~6 pt below "
                "the box and is wider than it, overhanging the right text margin by about 26 pt, "
                "and the whole block is centred to the right of the text column with body prose "
                "wrapping to its left"),
    figure(8, 3, "composite-panel",
           caption("Fig 2. The value of λ for different types of city", numbering="Fig. N"),
           mention(8), path=S_412, kind="model", panels=3, layout="1x3",
           source="typed-from-crop",
           note="the leftmost of three two-slice pies in one row (this box holds 'Balanced city'), "
                "each with its slice labels printed inside the "
                "slices - 'cos(CG,SG)' in the larger slice and '|CG|' in the smaller - so no legend "
                "and no axes anywhere. Under each pie the panel name ('Balanced city', 'Developing "
                "city', 'Developed city') and the relation that the pie illustrates (lambda = 1/sqrt3, "
                "lambda > 1/sqrt3, lambda < 1/sqrt3) are printed outside the measured boxes, and the "
                "single caption sits below all three. The lambda glyph comes out of the text layer as "
                "a private-use character, hence typed-from-crop"),
    figure(9, 1, "surface-or-3D",
           caption("Fig 3. Three dimensional baseline cube model", numbering="Fig. N"),
           mention(9, lead=span(9, "The baseline cube model is shown",
                                "in the following figure:"), pattern="direct"),
           path=H("4.1.5"), kind="model", three_d="isometric",
           note="the measurement cube itself: a wireframe axes box with floor and two wall grids, "
                "axes 'EPI' (vertical), 'EDI' (bottom-left receding) and 'SJI' (bottom-right), each "
                "ticked 0 to 1 in 0.2 steps. Two vectors from the origin - a blue arrow to the far "
                "top vertex labelled 'SMART GROWTH' and a red-brown arrow to an interior face "
                "labelled 'CURRENT GROWTH' - so the ideal is drawn as the cube's diagonal, exactly "
                "as the prose claims. No legend, no colourbar, no values on the arrow tips. The "
                "enum has no value for a 3-D axes box with no surface, so it is stored as isometric "
                "with the projection named here: it is a true perspective box, not a flat "
                "imitation"),
    figure(14, 3, "scatter",
           caption("Fig 4. SJI and EDI in current growth plan of Edinburgh and Wellington",
                   numbering="Fig. N"),
           mention(14), path=H("5.1.2"), kind="evaluation", source="typed-from-crop",
           note="one of three panels printed side by side, each under its own caption; the text "
                "layer interleaves the three caption lines, so the wording is read off the crop. "
                "Not a point scatter but a pair of vectors on a bare axis cross through the "
                "origin - both axes -1.0 to 1.0 with 0.5 ticks, x 'SJI' and y 'EDI', one arrow "
                "labelled 'Edinburgh' and one 'Wellington' with the names written at the arrow "
                "tips and no framed legend. No values printed, no reference line, no plot frame"),
    figure(14, 4, "scatter",
           caption("Fig 5. SJI and EPI in current growth plan of Edinburgh and Wellington",
                   numbering="Fig. N"),
           mention(14), path=H("5.1.2"), kind="evaluation", source="typed-from-crop",
           note="the middle vector panel: x 'SJI', y 'EPI', same -1.0 to 1.0 cross, same two "
                "arrows labelled at their tips, no legend, no values printed"),
    figure(14, 2, "scatter",
           caption("Fig 6. EDI and EPI in current growth plan of Edinburgh and Wellington",
                   numbering="Fig. N"),
           mention(14), path=H("5.1.2"), kind="evaluation", source="typed-from-crop",
           note="the right-hand vector panel: x 'EDI', y 'EPI', built like Fig 4 and Fig 5. The "
                "three together are the three pairwise projections of the cube, drawn as arrows "
                "from the origin rather than as points, and none of them draws the ideal-growth "
                "diagonal the prose argues from"),
    figure(14, 5, "surface-or-3D",
           caption("Fig 7. The current growth plan of Wellington and Edinburgh in the cube model",
                   numbering="Fig. N"),
           mention(14), path=H("5.1.2"), kind="evaluation", three_d="isometric",
           note="the only three-dimensional exhibit in the paper: a matplotlib-style 3-D axis box "
                "with three visible grid panes, axes 'EPI' (vertical), 'EDI' (bottom left) and "
                "'SJI' (bottom right), each -1 to 1 in 0.5 steps. Three arrows from the origin "
                "labelled at their tips: 'Ideal Smart Growth' aimed at the (1,1,1) corner, "
                "'Edinburgh' and 'Willton' - the drawing misspells Wellington and the caption does "
                "not. No legend, no colourbar, no values printed"),
    figure(16, 1, "line",
           caption("Fig 8. Growth plan for Edinburgh in the next three decades",
                   numbering="Fig. N"),
           mention(16, lead=span(16, "The figure is shown below:", "below:"), pattern="direct"),
           path=H("5.2.1"), kind="result", legend="inside",
           note="three stepped annual series (SJI red, EDI blue, EPI green) over 2017-2047, y "
                "'Index' 0-2, x 'Time', boxed legend inside the plot at the lower right, no values "
                "printed on the curves. Carries an in-frame title of its own - 'The Development of "
                "Edinburgh Over the Next Three Decades' - and, unlike Fig 9, its caption line "
                "prints inside the measured box at the bottom edge rather than below it"),
    figure(17, 1, "line", caption("Fig 9. Growth plan for Wellington in the next three decades",
                                  numbering="Fig. N"),
           mention(17), path=H("5.2.2"), kind="result", legend="inside",
           note="three annual series (SJI red, EDI blue, EPI green) over 2017-2047 with no point "
                "markers and no values printed on the curves; y-axis 'Index' 0-2, x-axis 'Time'. "
                "The chart carries its own title inside the frame - 'The Development of Wellington "
                "Over the Next Three Decades' - which duplicates the caption, and the caption "
                "prints below the frame. Boxed legend sits inside the plot at mid-height on the "
                "right; frame on all four sides, ticks inward, no gridlines"),
]

TABLES = [
    table(7, 1, tcap("Table1: Main parameters utilized in baseline cube model",
                        numbering="Table N:"),
          mention(7, lead=span(6, "we selected the following parameters",
                               "determine the smart growth"), pattern="direct"),
          grid(10, 3, header=1, rules="vertical-rules", merged=True, numeric=0, txt=3,
               width="full", continued=True),
          path=S_411, kind="model",
          note="three physical columns: a first-stage cell 'Smart Growth Index(SGI)' merged down "
               "all nine indicator rows, three second-stage cells (EDI, SJI, EPI) each merged over "
               "a block of three, and the nine third-stage indicators one per row. Full grid - outer "
               "frame, a rule between the columns, a rule under every indicator row and full-width "
               "rules only at the three block boundaries - no zebra, no numbers anywhere, and it "
               "runs 1 pt past the right text margin. Only the body is measured: the caption and the "
               "header row ('First stage | Second stage | Third stage') print at the foot of p6, and "
               "p6 returns no region at all, so the header row is a declared gap rather than an "
               "invented box"),
    table(7, 3, tcap("Table 2: A summary of SGI Expression", numbering="Table N:"),
          mention(7, lead=span(7, "A summary of the SGI equation is given",
                               "as the following table:"), pattern="direct"),
          grid(5, 4, header=1, rules="vertical-rules", merged=True, numeric=0, txt=4,
               width="full"),
          path=S_412, kind="model",
          note="four columns (Expression | Term | Description | Meaning) over four data rows, one "
               "for each piece of the SGI formula. Full grid, no zebra. The Expression column is a "
               "single merged cell spanning all four rows and holding the SGI fraction as typeset "
               "math - the only body cell in the paper that carries a formula instead of a word. "
               "No units, no numbers, no note row"),
    table(10, 1, tcap("Table 3. Classification of EDI/SJI/EPI according to their values",
                         numbering="Table N."),
          mention(10, style=[], count=0,
                  lead=span(9, "Each of the three variables is classified",
                            "levels in our cube model."), pattern="direct"),
          grid(7, 4, header=1, rules="vertical-rules", numeric=0, txt=4, width="half"),
          path=H("4.1.5"), kind="model",
          note="four columns (Value | EDI | SJI | EPI) over six value bands from 0.8~1 down to "
               "-1~-0.8, with the same word repeated across the three index columns in every row "
               "(High / Medium / Low / Negative / Bad / Worst). Full grid, no zebra, no merges, "
               "nothing numeric to align, and the only table in the paper that does not fill the "
               "measure - it runs about 0.57 of the text width, so its right edge stops well short "
               "of every other grid. The caption is stranded at the foot of page 9 while the grid "
               "opens page 10"),
    table(10, 2, tcap("Table 4. Evaluation of growth results", numbering="Table N."),
          mention(10, lead=span(10, "The results are listed in the following table:", "table:"),
                  pattern="direct"),
          grid(5, 4, header=1, rules="vertical-rules", merged=True, numeric=0, txt=4,
               width="full"),
          path=H("4.1.5"), kind="model",
          note="four columns (Min(EDI,SJI,EPI) | Growth type | SGI | Level of growth) over two "
               "logical blocks: '>0' and 'Smart growth' each merge three rows whose right-hand "
               "cells carry the 0.8~1 / 0.5~0.8 / 0~0.5 bands against High / Medium / Low, then a "
               "single '<0 | Non-smart growth | - | -' row. Full grid, no zebra, no numbers to "
               "align. It is the lookup table that turns the cube into a verdict, and its columns "
               "stop spelling out what the merged cells already say"),
    table(13, 1, tcap("Table 5. Evaluation results of Edinburgh", numbering="Table N."),
          mention(13, lead=span(13, "The results are shown in the following table:", "table:"),
                  pattern="direct", read=1,
                  trail=span(13, "According to the results",
                             "the three factors of CG are all positive.")),
          grid(5, 4, header=1, rules="vertical-rules", merged=True, decimal=True,
               numeric=3, txt=1, width="full"),
          path=H("5.1.1"), kind="evaluation",
          note="four data rows (Previous, Current, CG, SGI) under a header of bare factor names: "
               "State | EPI | SJI | EDI. Full grid - outer frame plus a rule between every column "
               "and every row - no zebra, four-decimal values aligned on the point. The SGI row "
               "merges its last three cells into one, which is how a single scalar sits under "
               "three columns at once"),
    table(13, 2, tcap("Table 6. Evaluation results of Wellington", numbering="Table N."),
          mention(13, lead=span(13, "The results are shown in the following table:", "table:"),
                  pattern="direct", read=1,
                  trail=span(14, "It’s clear from the table",
                             "that are negative")),
          grid(5, 4, header=1, rules="vertical-rules", merged=True, decimal=True,
               numeric=3, txt=1, width="full", continued=True),
          path=H("5.1.2"), kind="evaluation",
          note="the Table 5 template printed across a page turn: the header plus the Previous and "
               "Current rows close p13 with a bottom rule that makes the fragment look "
               "self-terminating, and the CG and SGI rows open p14 with no header repeated and no "
               "marker. The SGI row again merges EPI/SJI/EDI into one em-dash cell, so the two "
               "negative CG values are the only numbers on the whole table that say the city "
               "regressed"),
    table(15, 1, tcap("Table 7. the current budget plan and optimal budget plan"
                         "(% of total budget) of Edinburgh", numbering="Table N."),
          mention(15, lead=span(15, "The results of current plan and optimal plan are shown",
                                "as percentage of total budget:"), pattern="direct", read=1,
                  trail=span(15, "According to the table, we give the following suggestions",
                             "in the next three decades.")),
          grid(9, 5, header=1, rules="vertical-rules", units_hdr=True, decimal=True,
               numeric=3, txt=2, width="full"),
          path=H("5.2.1"), kind="result",
          note="five columns (Term | Factor | Current plan(%) | Optimal plan(%) | Change "
               "Delta(%)) over eight rows - B1 to B7 plus a Total/All row carrying 100 100 0. "
               "Full grid, no zebra, no merges, four decimals aligned on the point, and the unit "
               "carried in each numeric header rather than in the body, which repeats the "
               "'(% of total budget)' already printed in the caption"),
    table(16, 2, tcap("Table 8. the current budget plan and optimal budget plan"
                         "(% of total budget) of Wellington", numbering="Table N."),
          mention(16, lead=span(16, "The results of current plan and optimal plan are shown",
                                "as percentage of total budget:"), pattern="direct", read=1,
                  trail=span(16, "we give the following suggestions for the growth plan",
                             "for Wellington.")),
          grid(9, 5, header=1, rules="vertical-rules", units_hdr=True, decimal=True,
               numeric=3, txt=2, width="full"),
          path=H("5.2.2"), kind="result",
          note="the Table 7 grid reprinted for the second city: same five columns, same eight rows "
               "plus Total/All, same full grid, same units in the header, same four-decimal "
               "alignment. The two city tables print with no comparison between them, so a reader "
               "has to hold Table 7 in mind to see that Wellington's transport budget moves the "
               "opposite way from Edinburgh's"),
    table(17, 2, tcap("Table10. ranking and comparison of components for Edinburgh "
                         "and Wellington", numbering="Table N."),
          mention(17, lead=span(17, "The results are shown in the following table:", "table:"),
                  pattern="direct", read=1,
                  trail=span(18, "It is clear from table",
                             "between Edinburgh and Wellington.")),
          grid(10, 5, header=2, rules="vertical-rules", merged=True, units_hdr=True,
               decimal=True, numeric=2, txt=3, width="full", continued=True),
          path=H("5.3"), kind="result",
          note="five physical columns under a two-row header: 'Ranking' spans both header rows, "
               "'Edinburgh' and 'Wellington' each span the two columns beneath them (Components, "
               "Change |Delta|(%)), and the percent sign lives in the header. Outer frame plus a "
               "vertical rule between every column and a rule under every row; no zebra. Seven "
               "rank rows plus an 'Average' row whose two Components cells hold a bare em dash "
               "each - placeholders, not a spanning cell. Four-decimal values align on the point. "
               "Breaks across the p17/p18 turn with no header repeated and no marker"),
    table(20, 1, tcap("Table 11. Original results and changed results of Edinburgh",
                         numbering="Table N."),
          mention(20, lead=span(20, "The changed result and original results are shown",
                                "in the following list:"), pattern="direct", read=1,
                  trail=span(20, "As is shown in the table",
                             "SGI changed by 1.6702%.")),
          grid(7, 5, header=1, rules="vertical-rules", merged=True, decimal=True,
               numeric=3, txt=2, width="full"),
          path=["未编号标题：VII. Sensitivity Analysis"], kind="sensitivity", numbered=False,
          note="five physical columns (two unlabelled label columns plus EPI, SJI, EDI) whose "
               "header row names only the three value columns; the blocks 'original', 'changed' "
               "and 'Delta (%)' each merge two rows, and every SGI value is one cell merged "
               "across the EPI/SJI/EDI columns - so the SGI column is a spanning block, not a "
               "fourth value column. Outer frame, a rule between every column and every row, and "
               "an extra rule separating 'result' from 'SGI' inside each block; no zebra, "
               "four decimals aligned on the point"),
]

RULES = [
    "版式跟着论证阶段走：model 章吃掉 6 件（Table 1、2、3、4 与 Fig 2、3），evaluation 6 件"
    "（Fig 4、5、6、7 与 Table 5、6），result 5 件（Fig 8、9 与 Table 7、8、10），introduction "
    "只有 Fig 1 一件，sensitivity 只有 Table 11 一件且挂在无编号的 VII 章下 [place.section_kind]。",
    "全篇没有一次按编号引用展品：19 件里 0 件在正文被 'Fig N'/'Table N' 点过名，正文只会说 "
    "'the following table'、'the following figure'、'the following list'，因此 mention.style 全空、"
    "first_page 全为 null、count 全为 0，能记的只有那句指示语 [mention.first_page][mention.style]"
    "[mention.count]。",
    "引出靠指示语不靠编号：12 件有引出句且全是直陈式（'The results are shown in the following "
    "table:' 出现三次、'A summary of ... is given as the following table:'、'The figure is shown "
    "below:'、'we selected the following parameters'），7 件没有引出句（Figure 1、Fig 2、Fig 4、5、6、"
    "7、Fig 9）[mention.lead_sentence][mention.lead_pattern]。",
    "题注方位一刀切按展品类型分工：9 张图的题注全在图下方，10 张表的题注全在表上方，一件例外都没有 "
    "[caption.position]。",
    "编号四种写法且跳号：'Figure 1' 无冒号无句点，'Table1:' 连空格都没有，'Table 2:' 有冒号，"
    "'Fig 2.'、'Table 3.' 起改用句点，'Table10.' 又没空格；表号从 8 直接跳到 10，全篇没有 Table 9。"
    "封闭词表装不下 'Table1:'，统一记成 'Table N:' 并把印法写进行注 [caption.numbering]。",
    "题注全是名词短语：词数 6-15，voice 19 条全为 none，variables 全假，concludes 全假；units 只有 "
    "Table 7/8 的 '(% of total budget)' 算数；因为编号自带句点，13 条被切成两句、6 条一句，是排版"
    "假象不是双句题注 [caption.words][caption.sentences][caption.voice][caption.units]。",
    "图后解读句稀缺：19 件里只有 6 件有解读句（Table 5、6、7、8、10、11），其余 13 件读完就换节；"
    "9 张图没有一张被解读 [mention.read_sentences]。",
    "图只有五种形态，且没有一张印数：折线 2（Fig 8、9，三条年度序列、图例在绘图区内）、三维坐标箱 2"
    "（Fig 3、7）、平面向量图 3（Fig 4、5、6，原点指向两城的箭头）、三饼复合 1（Fig 2）、旭日环 1"
    "（Fig 1）；全篇 printed_numbers 与 data_labels 全假——没有一个数据点标过值 [geometry.family]"
    "[geometry.printed_numbers][geometry.data_labels]。",
    "三维只出现在两个坐标箱里：Fig 3 是测量用的立方体（'SMART GROWTH' 箭头指向远顶点、'CURRENT "
    "GROWTH' 箭头指向面内一点），Fig 7 是同一立方体内的两城向量；两张都是透视坐标框而非平面模仿，"
    "封闭词表没有“三维坐标箱”这一档，因此记 isometric 并在行注写明投影 [geometry.three_d]。",
    "图例只有 2 张图有且都在绘图区内：Fig 8 的方框图例在右下、Fig 9 的在右侧中部；其余 7 张把标签"
    "直接写在弧、切片或箭头尖上；9 张图零 colorbar [geometry.legend][geometry.colorbar]。",
    "三张图共用一句题注的名字空间：Fig 4、5、6 是同一行三个小面板、各有自己的题注，文字层把三条题注"
    "逐行交错（'Fig 4. SJI and EDI in' / 'Fig 5. SJI and EPI in current' / 'Fig 6. EDI and EPI in "
    "current' 之后才接三条尾巴），三行都取不到连续子串，因此全部 typed-from-crop [caption.verbatim]。",
    "十张表一个规制：全部是外框加竖线加逐行横线的满格（vertical-rules），没有一张 booktabs、没有一张"
    "隔行底纹；宽度 9 张满版心、只有 Table 3 停在 0.57 处，全部纵向 [table.rule_style][table.zebra]"
    "[table.width][table.orientation]。",
    "合并单元格是这张卷子的默认手法，10 张里 7 张用了：Table 1 第一列跨九行、第二列每格跨三行，"
    "Table 2 的 Expression 跨四行，Table 4 的 '>0' 与 'Smart growth' 各跨三行，Table 5/6 的 SGI 行"
    "把三个数值列并成一格，Table 11 的行标签跨两行、SGI 值横跨三列，Table10 表头 'Ranking' 跨两行、"
    "城市名各跨两列 [table.merged_cells][table.header_rows]。",
    "跨页三张表三种命运：Table 1 的上半截（题注与表头行 'First stage/Second stage/Third stage'）印在 "
    "p6 页脚而 p6 一个区域都没有返回，网格只从 p7 顶上第二行起被测量；Table 6 在 p13 断在 CG 行、"
    "p14 续两行；Table10 在 p17 只印两行表头、p18 续八行——三张都没有 continued 标记 "
    "[table.continued][table.rows]。",
    "单位三种写法：Table 7/8 把 '(%% of total budget)' 写进题注又在表头写 'Current plan(%%)'，"
    "Table10 把百分号塞进表头 'Change |Δ|(%)'，其余七张没有单位；小数对齐只发生在六张带四位小数的表"
    "（Table 5、6、7、8、10、11），其余四张全是文本或区间 [table.units_in_header]"
    "[table.decimal_aligned]。",
    "36 个区域里 13 个是公式碎片：p11 五块（式 6 的约束块、式 7 的左右两半、式 8 的两行）、p12 五块"
    "（式 9、式 10 与三处无编号显示式）、p19 一块（式 11 的 F 行），全部 in-body-diagram；式 6、7、8、9、"
    "10、11 的编号都印在各框之外，p12 式 10 的框还把末尾那列向量的右括号切在框外 [place.area_frac]。",
    "三块既不是展品也不是公式：p8 两块是 Fig 2 的另两个面板（fragment-of-other），p22 一块框住参考"
    "文献三行（not-an-exhibit），p14 与 p18 两块是跨页表的续表（split-across-pages）"
    "[place.section_kind]。",
]

NOTE = (
    "Nine printed figures and ten printed tables - the numbering skips Table 9 and runs 'Table1:' "
    "with no space - against 36 measured regions and 17 exclusions. Thirteen of the exclusions are "
    "pieces of typeset display math: five on page 11 (the constraint block of (6), the two halves "
    "of (7), the two lines of (8)), five on page 12 ((9), (10) and three unnumbered displays) and "
    "the F line of (11) on page 19. Every equation number in the paper prints outside the box that "
    "measured its equation, and page 12 box 3 cuts the closing bracket of (10). Two exclusions are "
    "table continuations across page turns, two are the outer panels of the three-panel Figure 2, "
    "and one is a window that fell on three lines of the reference list. No exhibit is cited by "
    "number anywhere: every 'Fig N' and 'Table N' string in the text layer is a caption, and the "
    "prose points with 'the following table' / 'the following figure' / 'the following list' only, "
    "so every mention block carries an empty style list, a zero count and a null first_page. Figure "
    "1 is a colour sunburst and is the only exhibit whose family is 'other'; Figures 4, 5 and 6 are "
    "three vector panels whose captions interleave line by line, so all three are typed from the "
    "crop; Figures 3 and 7 are the only three-dimensional exhibits. All ten tables use the same "
    "full grid, seven of them merge cells, and Table 1 loses its top - the caption and the header "
    "row print on page 6, which returns no region, so the grid is measured from its second line "
    "down."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ALL,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

for _e in ALL + TABLES:
    _e["page_order"] = sorted(
        [x for x in ALL + TABLES if x["page"] == _e["page"]],
        key=lambda x: (x["bbox"][1], x["bbox"][0])).index(_e) + 1
    _e["place"]["page_order"] = _e["page_order"]
for _n, _e in enumerate(sorted(ALL + TABLES, key=lambda x: (x["page"], x["page_order"])), 1):
    _e["place"]["doc_order"] = _n


def main() -> int:
    from collections import Counter

    rows = ALL + TABLES
    print("figures", len(ALL), "tables", len(TABLES), "excluded", len(EXCLUDED))
    for k in ("family", "legend", "panel_count", "shared_axes", "three_d", "colorbar",
              "printed_numbers", "data_labels"):
        print(k, dict(Counter(e["geometry"][k] for e in ALL)))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in rows)))
    for k in ("position", "numbering", "voice", "words", "sentences", "units", "variables",
              "conditions", "concludes"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in rows)))
    for k in ("first_page", "lead_pages", "count", "lead_pattern", "read_sentences"):
        print("mention." + k, dict(Counter(e["mention"][k] for e in rows)))
    for k in ("rule_style", "zebra", "merged_cells", "header_rows", "units_in_header",
              "decimal_aligned", "width", "orientation", "continued"):
        print("table." + k, dict(Counter(t["table"][k] for t in TABLES)))
    print("area", [e["place"]["area_frac"] for e in rows])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
