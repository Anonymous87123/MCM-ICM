"""Hand census of P-A-2015-34317-1232cf72 (Team 34317, 47 pages, 54 measured regions).

This paper paints a white filled rectangle behind every text line. The measurer groups
those rectangles into paragraph bands, so seven of the fifty-four regions are ordinary
prose rather than exhibits, and two flow charts shatter into a chart region plus six
node fragments each. Geometry settles the prose bands on its own: every band carries
1.05 to 2.00 white fills per text line, while every real exhibit carries 0.00, because
nothing in a pasted bitmap or a drawn grid is filled with white.

   p4  r1  five prose lines under 1.2                    excluded not-an-exhibit
   p6  r1  six prose lines closing 1.3                   excluded not-an-exhibit
   p7  r1  eight prose lines under 4.1                   excluded not-an-exhibit
   p7  r2  eight more, new paragraph                     excluded not-an-exhibit
   p8  r1  eight prose lines introducing the symbols     excluded not-an-exhibit
   p8  r2  Table 4.1   nine symbols, SYMBOL/DEFINITION/UNITS
   p9  r1  Figure 4.1  the SEIIFR compartment cartoon
   p10 r1  five prose lines                               excluded not-an-exhibit
   p10 r2  two integral display equations                 excluded not-an-exhibit
   p12 r1  START node of the p12 chart                    excluded fragment-of-other
   p12 r2  Figure 4.2  genetic-algorithm flow chart
   p12 r3  PARAMETER INITIALIZATION node                  excluded fragment-of-other
   p12 r4  GENETIC node                                    excluded fragment-of-other
   p12 r5  N>N_f diamond                                   excluded fragment-of-other
   p12 r6  OUTPUT OPTIMAL node                             excluded fragment-of-other
   p12 r7  END node                                        excluded fragment-of-other
   p13 r1  Figure 4.3  the fit to Guinea, cases and deaths
   p14 r1  Figure 4.4  3-D pie of infection routes
   p14 r2  Table 4.2   eight hospital parameters
   p15 r1  Figure 4.5  the advanced compartment graph
   p16 r1  Table 4.3   the Guinea parameter set
   p17 r1  Figure 4.6  the hospital-aware fit
   p18 r1  Figure 4.7  the Guinea forecast
   p19 r1  Table 4.4   the Liberia parameter set
   p19 r2  Figure 4.8  the fit to Liberia
   p20 r1  Table 4.5   the Sierra Leone parameter set
   p20 r2  Figure 4.9  the fit to Sierra Leone
   p21 r1  Table 5.1   normal against emergency supplies
   p24 r1  Figure 5.1  the clustering dendrogram
   p27 r1  a five-symbol grid, untitled and unnumbered
   p29 r1  Figure 7.1  the routing algorithm
   p29 r2  GET LOCATIONS node                             excluded fragment-of-other
   p29 r3  second decision node                           excluded fragment-of-other
   p29 r4  right-hand branch box                          excluded fragment-of-other
   p29 r5  decision diamond                               excluded fragment-of-other
   p29 r6  GET LOCATIONS AND TRANSPORT box                 excluded fragment-of-other
   p29 r7  END terminal                                   excluded fragment-of-other
   p30 r1  Figure 7.2  one delivery location in Guinea
   p31 r1  Figure 7.3  three delivery locations in Guinea
   p31 r2  the Guinea route lengths, unnumbered
   p32 r1  Table 7.1   the six routes
   p33 r1  Figure 7.4  one location in Liberia
   p33 r2  the Liberia route lengths, unnumbered
   p34 r1  Figure 7.5  Sierra Leone
   p34 r2  the Sierra Leone route lengths, unnumbered
   p35 r1  an eight-symbol grid under 8.3, untitled
   p36 r1  Figure 8.1  medicine produced per day
   p37 r1  Figure 8.2  the three countries on one axis
   p38 r1  Figure 8.3  medicine needed against time
   p39 r1  Figure 9.1  controlling spread in hospitals
   p39 r2  Figure 9.2  controlling spread in funerals
   p41 r1  Figure 11.1  sensitivity of beta
   p42 r1  Figure 11.2  sensitivity of gamma, clustered bars
   p42 r2  Figure 11.3  sensitivity of b1

Thirty printed exhibits - twenty-three figures and seven tables - plus five grids the
paper prints without a caption or a number, against twelve flow-chart fragments and seven
prose bands that are not exhibits. Thirty-five exhibit regions, nineteen exclusions,
nothing unresolved.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2015-34317-1232cf72"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]
        KIND[(_pg["page"], _i)] = _r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

for _key, _bbox in REG.items():
    _ctx = CTXREG.get(_key)
    if _ctx is None or max(abs(a - b) for a, b in zip(_ctx["bbox"], _bbox)) > 0.5:
        raise SystemExit(f"region numbering disagrees with the context dump at {_key}")

# 595.32 x 841.92 pt page, text block x 90.0 to 505.4
MEASURE = 415.4
DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def qp(text: str, pages: list[int]) -> str:
    """Same guard, for a sentence that may print on a neighbouring page."""
    for page in pages:
        if schema.norm(text) in schema.page_text(PID, page):
            return schema.norm(text)
    raise KeyError((pages, text[:70]))


def qtail(page: int, marker: str, nwords: int) -> str:
    """Quote the nwords words that end at a printed marker - the sentence may be too long."""
    text = schema.page_text(PID, page)
    end = text.find(marker)
    if end < 0:
        raise KeyError((page, marker))
    end += len(marker)
    start = end
    seen = 0
    while start > 0 and seen < nwords:
        start -= 1
        if text[start].isspace() and text[start + 1:start + 2] not in ("", " "):
            seen += 1
    return schema.norm(text[start:end].strip())


def cap(page: int, prefix: str, tail: str) -> str:
    """Take the caption verbatim out of the layer: from its number to its last printed word.

    This paper prints every caption in lower case with no space after the word - `figure4.6:`
    on most pages, `figure 4.6:` on a few - so the prefix has to be given in the case the
    layer actually holds.
    """
    text = schema.page_text(PID, page)
    start = text.find(prefix)
    if start < 0:
        raise KeyError((page, prefix))
    end = text.find(tail, start)
    if end < 0:
        raise KeyError((page, tail))
    return schema.norm(text[start:end + len(tail)])


def pct(span: float) -> str:
    return f"{span / MEASURE * 100:.1f}"


def place(page: int, reg: int, kind: str, path: list[str], numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": c["region"],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def none_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          pattern: str = "direct", read: int = 1, gap: int | None = None,
          trail: str = "") -> dict:
    pages = sorted({page - 1, page, page + 1, first_page - 1, first_page, first_page + 1})
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": qp(lead, pages) if lead else "",
            "trail_sentence": qp(trail, pages) if trail else "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": gap}


def caption(verbatim: str, numbering: str = "none", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", numbered: bool = True,
           position: str = "below", note: str = "", other_note: str = "",
           shared_axes: bool = False, confidence: str = "high") -> None:
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": confidence,
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path, numbered),
        "mention": mention,
        "caption": caption(cap_text, numbering, position),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, rows: int, cols: int, kind: str, path: list[str],
          note_sentence: str, note: str, *, rule: str = "booktabs", numeric: int = 1,
          header_rows: int = 1, numbered: bool = True, width: str = "full",
          zebra: bool = False, merged: bool = False, decimal: bool = False,
          diagonal: bool = False, continued: bool = False, cap_text: str = "",
          position: str = "below", mention: dict | None = None,
          source: str = "text-layer") -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": source if cap_text else "none",
        "note": note,
        "place": place(page, reg, kind, path, numbered),
        "mention": mention or none_mention(),
        "caption": caption(cap_text, "Table N:" if cap_text else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued,
                  "note_sentence": qp(note_sentence, [page, page + 1]) if note_sentence else ""},
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "reason": reason,
        "note": note,
    })


# ---------------------------------------------------------------- section paths
SEC_SYMB4 = ["4.2 Symbols and Definitions"]
SEC_MODEL4 = ["4.3 Construction of the Model"]
SEC_REFRESH = ["4.5 Refresh the Values of Parameters"]
SEC_ADV = ["4.6 Advanced Model"]
SEC_RESULTS = ["4.7 Results are Reasonable"]
SEC_PREDICT = ["4.8 Prediction of the Future"]
SEC_SUPPLY = ["5.1 What is Emergency Supplies"]
SEC_CLUSTER = ["5.4 Results of Clustering Method"]
SEC_SYMB6 = ["6.2 Symbols and Definitions"]
SEC_ALGO = ["7.1 General algorithm"]
SEC_GUINEA = ["7.2 Application of Algorithm", "7.2.1 Application in Guinea"]
SEC_LIBERIA = ["7.2 Application of Algorithm", "7.2.2 Application in Liberia"]
SEC_SIERRA = ["7.2 Application of Algorithm", "7.2.3 Sierra Leone"]
SEC_SYMB8 = ["8.3 symbols and definitions"]
SEC_SPEED = ["8.4 How Fast Need We Produce Medicine and Vaccine"]
SEC_QUANT = ["8.5 The Quantity of the Medicine Needed"]
SEC_OTHER9 = ["Ⅸ Other Factors We Think Are Important"]
SEC_SENS1 = ["11.1 Sensitivity Analysis of SEIIRF Model"]
SEC_SENS2 = ["11.2 Sensitivity Analysis of Model of the Speed to Produce Medicine"]

# ---------------------------------------------------------------- prose bands
# The seven regions the white-fill rectangles turn into paragraphs. Justified body lines,
# no drawn graphic anywhere in the box.
excluded(4, 1, "not-an-exhibit",
         "Five justified body lines at full measure, x 90.0 to 505.4, hanging below the 1.2 "
         "'Our understanding of the words' heading. Measured as a region only because the page "
         "paints a white filled rectangle behind every text line - 1.49 white fills per line "
         "here, against 0.00 in every real exhibit on the paper.")
excluded(6, 1, "not-an-exhibit",
         "Six justified body lines closing section 1.3 at the foot of the page, 1.28 white fills "
         "per line. Nothing is drawn in the band: no rule, no grid, no axes.")
excluded(7, 1, "not-an-exhibit",
         "Eight justified body lines directly under the 4.1 Introduction heading, 1.66 white "
         "fills per line - the highest ratio on the paper, because the band holds shorter lines.")
excluded(7, 2, "not-an-exhibit",
         "The eight-line continuation of the same section, opening a fresh paragraph with a "
         "first-line indent, split off from the band above by the one line of white that the "
         "measurer read as a gap: 1.21 white fills per line.")
excluded(8, 1, "not-an-exhibit",
         "Eight justified body lines introducing Table 4.1, 1.05 white fills per line. The prose "
         "ends on 'We show them below:' and the grid begins in the next region.")
excluded(10, 1, "not-an-exhibit",
         "Five justified body lines, 1.63 white fills per line, ending in the rhetorical question "
         "'...for rapid interment with little more than a cursory prayer? Moreover, the'. The "
         "measurer placed this band 280 pt below the display equations it sits under, so the "
         "region holds prose and not the SEIIFR system printed above it.")
excluded(10, 2, "not-an-exhibit",
         "Two unnumbered display equations, no frame and no rule: y_C = the integral from 0 to t "
         "of alpha E(t) dt, and beneath it y_D = the integral of delta_2 gamma_2 I_2(t) dt. "
         "Introduced by the sentence 'to measure the total cases and death cases of Ebola, We "
         "invoke'; 2.00 white fills per line. Display math, not an exhibit.")

# ---------------------------------------------------------------- p12 flow chart fragments
excluded(12, 1, "fragment-of-other",
         "The START stadium and its outgoing arrow stub, measured out of the p12 flow chart: "
         "102.0 by 27.0 pt, wholly inside the chart box at [149.2, 92.5, 481.8, 501.0].")
for _reg, _what in ((3, "the rectangle reading 'PARAMETER INITIALIZATION X = X_0'"),
                    (4, "the rectangle reading 'GENETIC' alone, the operator noun dropped"),
                    (5, "the diamond 'N>N_f' with its two branch stubs"),
                    (6, "the rectangle reading 'OUTPUT OPTIMAL'"),
                    (7, "the END stadium and the arrowhead feeding it")):
    excluded(12, _reg, "fragment-of-other",
             f"One node of the p12 flow chart - {_what} - measured as a region of its own. The "
             "chart's spine, arrows and loop-back are drawn in vector while the node interiors are "
             "raster gradient blocks, so the measurer caught each box separately; all six sit "
             "wholly inside the chart region at [149.2, 92.5, 481.8, 501.0].")

# ---------------------------------------------------------------- p29 flow chart fragments
for _reg, _what in ((2, "the 'USING CLATER METHOD' box with the return arrowhead touching its "
                        "right edge"),
                    (3, "the 'TSP MODEL TO GET THE' box"),
                    (4, "the 'INCREASE THE NUMBER OF' box, with the N-return connector drawn "
                        "straight through its grey fill instead of round it"),
                    (5, "the 'CARS FINISH EVERY ROUTE IN ONE DAY?' diamond with its Y and N "
                        "branches"),
                    (6, "the 'GET LOCATIONS AND TRANSPORT' box"),
                    (7, "the END terminal")):
    excluded(29, _reg, "fragment-of-other",
             f"One node of the p29 routing chart - {_what} - measured as a region of its own. The "
             "nodes are raster gradient blocks dropped into the vector chart, so the measurer "
             "caught each box separately; all six sit wholly inside the chart region at [189.7, "
             "215.4, 519.4, 669.9].")

# ---------------------------------------------------------------- p8, Table 4.1
table(8, 2, 9, 3, "symbols", SEC_SYMB4,
      "There are some symbols appear in the model. We show them below:",
      "The model's symbol list, 410.6 by 462.0 pt at 98.8 per cent of the measure and the tallest "
      "grid on the paper: nine body rows under a SYMBOL, DEFINITION, UNITS head on a solid black "
      "band with knockout white capitals. Boxed - full outer frame, a rule between every row, no "
      "vertical between the columns. The symbol column is set in math italic and holds the paper's "
      "whole Greek inventory with subscripts and stacked fractions (beta_1, beta_2/beta_1, "
      "beta_F/beta_1, alpha^-1, gamma_1^-1, gamma_2^-1, gamma_F^-1, delta_1 delta_2, delta_2). "
      "Column widths are the defect: the DEFINITION column takes about 60 per cent of the grid, "
      "the SYMBOL column about 13 per cent - more than the short glyphs need - and UNITS about 27 "
      "per cent, so the middle column carries text wrapped to two lines in most rows while the "
      "other two stay half empty. Only two cells are tight enough to note: delta_1 delta_2 runs "
      "its two deltas together, and gamma_F^-1 crowds its raised -1 against the subscript.",
      rule="boxed", numeric=0, width="full",
      cap_text=cap(8, "table4.1:", "symbols in the model"), position="above")

# ---------------------------------------------------------------- p9, Figure 4.1
figure(9, 1, "flowchart-or-schematic",
       cap(9, "figure 4.1:", "Ebola propagation"), "Figure N:",
       cited(9, 9, ["figure 4.1", "Figure 4.1"], 2,
             qtail(9, "from the figure 4.1.", 8), trail=qtail(10, "Figure 4.1 are", 5)),
       "model", SEC_MODEL4, labels=True, numbers=True,
       note="A 289.5 by 79.9 pt strip at 69.7 per cent of the measure, centred at 149.5 to 439.0 "
            "pt: the paper's first SEIIFR compartment cartoon, six outlined circles on one "
            "baseline joined by solid arrows S to E to I1 to I2 to F, with a solid diagonal "
            "I1 to R and a dashed diagonal I2 to R closing the two removed-from-infectious paths "
            "down to a sixth circle below the row. Letters only in the circles - S, E, R in black, "
            "I1, I2 and F in red - and no rate label on any edge, so the drawing carries the "
            "topology of the model and nothing quantitative. The text layer holds just the letters "
            "(SEIIF, 12, R), which is why the chart cannot be read out of the layer at all. One "
            "defect: the arrow leaving F runs right and ends in empty white space with no target "
            "node, a dangling stub that no layer records.")

# ---------------------------------------------------------------- p12, Figure 4.2
figure(12, 2, "flowchart-or-schematic",
       cap(12, "figure4.2:", "combined with least square method"), "Figure N:", none_mention(),
       "model", SEC_REFRESH, labels=True,
       note="A 332.5 by 408.6 pt flow chart at 80.0 per cent of the measure, drawn in vector with "
            "uniform rule weights and clean arrowheads, seven nodes on one vertical spine: a "
            "stadium START, the rectangle 'PARAMETER INITIALIZATION X = X_0', the rectangle "
            "'CALCULATE FITNESS f = F(X)', the rectangle 'GENETIC', the diamond 'N>N_f', the "
            "rectangle 'OUTPUT OPTIMAL' and a stadium END. Every node carries a soft grey gradient "
            "band as fill only. Arrows run straight down; the loop-back leaves the diamond's right "
            "vertex labelled N, runs up the right margin and re-enters the trunk between "
            "PARAMETER INITIALIZATION and CALCULATE FITNESS with an arrowhead but no junction dot, "
            "and the Y branch falls to OUTPUT OPTIMAL. Two defects: the box reads 'GENETIC' alone, "
            "the operator noun dropped, leaving the step semantically incomplete; and the "
            "subscript f in 'N>N_f' overhangs the diamond's lower-right edge, which is already "
            "tight for its label. The six fragments the measurer split off this chart are all "
            "listed as excluded rather than counted twice.")

# ---------------------------------------------------------------- p13, Figure 4.3
figure(13, 1, "line",
       cap(13, "figure4.3:", "test of the calculated curves"), "Figure N:",
       cited(13, 13, ["figures 4.3"], 1, qtail(13, "from the figures 4.3", 6)),
       "result", SEC_REFRESH, panels=2, layout="2", legend="inside",
       note="Two line-and-marker panels side by side, 474.7 by 226.1 pt, 114.3 per cent of the "
            "measure - the block overruns the text block by 59 pt on the right. Left panel plots "
            "total cases against time, y 1000 to 3500 in steps of 500, x 0 to 120 in steps of 20 "
            "with the title 'Time from October 1st'; right panel plots deaths on the same x axis "
            "and a 500 to 3500 y axis. Three series in each: a solid black prediction line, blue "
            "markers for the points used to fit, red x markers for the points held back, under a "
            "three-key legend inside the upper left of each panel reading 'Predict Value', 'Data "
            "used for fitting' and 'Data not used for fitting'. A blue dashed vertical rule at "
            "about day 92 marks the split between the two. Both panels are pasted bitmaps - the "
            "tick and legend type is stair-stepped and the panel backgrounds are pale grey blocks "
            "- and the right panel was cropped too tight before pasting: its right spine is "
            "missing and three y ticks survive as detached dashes floating inside the plot. The "
            "left panel's prediction curve is clipped by its own 3500 ceiling at about day 120. "
            "The caption is the only one on the paper that says 'figures' in the plural.")

# ---------------------------------------------------------------- p14, Figure 4.4
figure(14, 1, "other",
       cap(14, "figure4.4:", "getting infected in different ways"), "Figure N:", none_mention(),
       "model", SEC_ADV, legend="below", numbers=True, three_d="isometric",
       other_note="3-D exploded pie chart - no pie family in the vocabulary",
       note="A 213.0 by 142.6 pt pasted raster, 51.3 per cent of the measure: a three-dimensional "
            "exploded pie, the disc drawn in perspective as an ellipse with extruded side walls "
            "and the three slices pulled apart, keyed by a three-chip legend below the art. Three "
            "slices only, values printed inside them: 72.0 per cent grey Community, 17.6 per cent "
            "orange Hospitals, 10.4 per cent blue Funerals, summing to 100.0. The perspective is "
            "the exhibit's one real defect: the 72 per cent grey slice sits at the front of the "
            "tilt and reads as visibly larger than its share, and the shadow edge the 3-D style "
            "adds is heavier than any line in the paper. Filed as 'other' because the vocabulary "
            "has no pie family and the chart is not a bar chart whatever the generator called it. "
            "Nothing in the prose points at it, and the sentence that follows it - 'There are 17.6% "
            "of healthy people in Sierra Leone get Ebola because of hospital' - is the only place "
            "the number is restated.")

# ---------------------------------------------------------------- p14, Table 4.2
table(14, 2, 8, 3, "model", SEC_ADV, "",
      "The advanced model's hospital parameters: eight body rows under a SYMBOL, DEFINITION, "
      "UNITS header, 461.7 by 392.6 pt at 111.2 per cent of the measure, so the grid runs 46 pt "
      "past the text block. Fully boxed with a solid black header band carrying white capitals, a "
      "thin rule under every one of the eight body rows and the two outer verticals, but no "
      "interior column dividers and no zebra. Six of the eight definitions wrap to two centred "
      "lines, which is what makes the grid so tall. The symbol column is set in math italic and "
      "is the worst-set type on the paper: the raised -1 on h1, h2, gamma3 and gamma4 floats "
      "detached and above its subscript so the cell reads 'h1 ~1'; both gammas are drawn in an "
      "italic that reads as a lowercase y; and the two deltas in 'delta_1H delta_2H' run together "
      "with their H subscripts and no space.",
      rule="boxed", numeric=0, width="full",
      cap_text=cap(14, "table4.2:", "in this advanced model"), position="above")

# ---------------------------------------------------------------- p15, Figure 4.5
figure(15, 1, "flowchart-or-schematic",
       cap(15, "figure4.5:", "ebola propagation"), "Figure N:", none_mention(),
       "model", SEC_ADV, labels=True,
       note="A 279.0 by 128.3 pt vector drawing, 67.2 per cent of the measure: the advanced "
            "compartment graph, eight thick-outlined circles S, E, I1, I2, R, H1, H2 and F with "
            "S, E and R in black and the five infectious and dead states in red, joined by "
            "thirteen edges - twelve solid and two dashed, the dashed pair being I2 to R and H2 to "
            "R. I1 also feeds H1 vertically and I2 feeds H2, so the hospital arm hangs below the "
            "row rather than beside it, and R is a pure sink with four inflows and no outflow. "
            "Three defects. No edge carries a rate label and there is no key for solid against "
            "dashed, so the drawing names the topology and nothing else. The exit arrow from F ends "
            "in empty space at the right with no target node - the same dangling stub as Figure "
            "4.1, drawn again. R is set at about 60 per cent of the diameter of every other circle "
            "although it collects four edges, and the dashed I2 to R stroke grazes the solid "
            "I1 to R and I2 to F strokes, so its arrowhead at R is easy to miss.")

# ---------------------------------------------------------------- p16, Table 4.3
table(16, 1, 8, 4, "result", SEC_RESULTS,
      "We calculate all parameters in Guinea are:",
      "The Guinea parameter set, 368.1 by 296.4 pt at 88.6 per cent of the measure, laid out as "
      "two SYMBOL/VALUE pairs side by side under a four-head band. Boxed, not booktabs: one "
      "outer hairline, a solid black header band with knockout white heads reading PARAMETER, "
      "VALUE, PARAMETER, VALUE, and no interior rule at all, horizontal or vertical - the eight "
      "rows are separated by white space alone, which is what the paper does on every one of its "
      "parameter grids. Cells are clean, nothing clipped.",
      rule="boxed", numeric=2, width="full",
      cap_text=cap(16, "table4.3:", "all parameters in Guinea"), position="above")

# ---------------------------------------------------------------- p17, Figure 4.6
figure(17, 1, "line",
       cap(17, "figure 4.6:", "Curves (Guinea)"), "Figure N:",
       cited(17, 17, ["figure 4.6"], 1, qtail(17, "from the figure 4.6,", 8)),
       "result", SEC_RESULTS, panels=2, layout="2", legend="inside",
       note="The hospital-aware fit, 473.6 by 226.1 pt, 114.0 per cent of the measure: two "
            "line-and-scatter panels abreast, each with its own three-key legend inside the upper "
            "left. Black Predict Value curve, blue dots for the points used to fit, red crosses "
            "for the points held back, and a dashed blue vertical rule at about t = 90 splitting "
            "the fitted span from the extrapolated one - the same grammar as Figure 4.3 with the "
            "hospital term added, which is exactly the comparison the prose draws ('our curves fit "
            "much better if we take hospital into consideration'). One small defect: the third row "
            "of the left panel's legend sits flush against the legend's own bottom border.")

# ---------------------------------------------------------------- p18, Figure 4.7
figure(18, 1, "line",
       cap(18, "figure 4.7:", "future cases in Guinea"), "Figure N:",
       cited(18, 18, ["figure 4.7"], 2,
             qtail(18, "From the figure 4.7,", 6), trail=qtail(18, "see figure 4.7)", 4)),
       "result", SEC_PREDICT, legend="inside",
       note="The forecast, 415.3 by 310.9 pt at exactly 100.0 per cent of the measure - the one "
            "exhibit on the paper drawn to the text block's own width. A single closed-frame plot: "
            "solid black total cases and red dashed deaths, blue dots over the fitting span and red "
            "crosses over the forecast span, under a legend inside the frame. The vertical axis "
            "carries no title at all, so the reader has to take 'cases' and 'deaths' from the "
            "legend alone; the horizontal axis is titled beneath the frame and the caption sits "
            "below that. The prose cites it twice on the same page, once forward and once "
            "parenthetically.")

# ---------------------------------------------------------------- p19, Table 4.4
table(19, 1, 8, 4, "result", SEC_PREDICT,
      "The parameters of Liberia:",
      "The Liberia parameter set, 377.0 by 295.1 pt at 90.8 per cent of the measure, the same "
      "two-pair layout as Table 4.3 and the same solid black header band with knockout white "
      "heads. Eight body rows, four columns, no interior rules, no cell merged, both value "
      "columns printed to two decimals throughout.",
      rule="boxed", numeric=2, width="full",
      cap_text=cap(19, "table4.4:", "parameters of Liberia"), position="above")

# ---------------------------------------------------------------- p19, Figure 4.8
figure(19, 2, "line",
       cap(19, "figure4.8:", "Curves (Liberia)"), "Figure N:",
       cited(19, 19, ["figure 4.8"], 1, qtail(19, "from the figure 4.8 that", 8)),
       "result", SEC_PREDICT, panels=2, layout="2", legend="inside",
       note="The Liberian fit, 476.8 by 227.1 pt at 114.8 per cent of the measure: twin panels of "
            "fitted curve against blue dots and red crosses with the dashed rule at the fitting "
            "boundary, 60 days in on this country. Both panels are pasted rasters whose right "
            "spine is missing, so the rightmost y ticks hang free inside the plot and the dashed "
            "rule runs several points past the frame; nothing is clipped and no point is lost.")

# ---------------------------------------------------------------- p20, Table 4.5
table(20, 1, 8, 4, "result", SEC_PREDICT,
      "The parameters Sierra Leone:",
      "The Sierra Leone parameter set, 377.0 by 295.1 pt at 90.8 per cent of the measure, "
      "identical in construction to Tables 4.3 and 4.4: boxed outer hairline, black header band, "
      "eight body rows in two symbol/value pairs, no interior rule. The caption carries the "
      "paper's own stray colon - 'table4.5: parameters Sierra Leone:' - and is kept verbatim.",
      rule="boxed", numeric=2, width="full",
      cap_text=cap(20, "table4.5:", "parameters Sierra Leone:"), position="above")

# ---------------------------------------------------------------- p20, Figure 4.9
figure(20, 2, "line",
       cap(20, "figure4.9:", "curves (Sierra Leone)"), "Figure N:", none_mention(),
       "result", SEC_PREDICT, panels=2, layout="2", legend="inside",
       note="The Sierra Leone fit, 484.9 by 231.5 pt at 116.7 per cent of the measure - the "
            "widest exhibit on the paper, 69.5 pt past the right margin. Twin panels as in "
            "Figures 4.3, 4.6 and 4.8, with a visibly concave fitted curve rather than the "
            "straight-line fit of the Guinea panels, one point sitting above its curve, and the "
            "same missing right spine and overrunning dashed rule. The caption is a single line "
            "set left of centre under the left panel rather than centred under the pair. Prose "
            "calls it 'the figure' with no number, so the mention stays empty although the "
            "sentence that follows it is about this chart.")

# ---------------------------------------------------------------- p21, Table 5.1
table(21, 1, 6, 3, "other", SEC_SUPPLY,
      "differences between them are shown as the table below:",
      "A three-column comparison of normal against emergency supplies, 416.4 by 227.1 pt at "
      "100.2 per cent of the measure, with ASPECTS, NORMAL SUPPLIES and EMERGENCY SUPPLIES across "
      "the top and six body rows - Aims, Formation, Property, Scheme, Balance Between Efficiency "
      "And Optimization, Delivery Mode. Rules run horizontally only, one under the header and one "
      "under each body row, with no vertical anywhere and no outer frame, so the grid reads as a "
      "stack of rules rather than a boxed table. The cells hold prose rather than data - 'Maximize "
      "Profile And Consider Both Fair And Efficiency' against 'Minimize Cost', 'Permanent' "
      "against 'Temporary', 'Return And Tour Return' - and each wraps to three or four lines, "
      "which is what makes six rows fill a third of a page. Cited only as 'the table below', "
      "never by number.",
      rule="booktabs", numeric=0, width="full",
      cap_text=cap(21, "table5.1:", "two supplies[3]"), position="above")

# ---------------------------------------------------------------- p24, Figure 5.1
figure(24, 1, "node-link-network",
       cap(24, "figure5.1:", "Clustering Picture of Liberia"), "Figure N:", none_mention(),
       "result", SEC_CLUSTER, labels=True,
       note="427.2 by 256.8 pt at 102.8 per cent of the measure, and not the map the section "
            "heading ('Clustering Method, A Way to Determine Regions for Medicine') and the "
            "caption ('Clustering Picture') lead a reader to expect: it is a dendrogram, a tree of "
            "joined branches drawn horizontally with the Liberian district names printed as leaves "
            "along the base. No basemap, no borders, no shading by value - the districts are "
            "grouped by where their leaves join, and nothing in the drawing states where any "
            "district is on the ground, although the delivery locations the chapter goes on to "
            "choose are read straight off this tree. One defect: the caption is set so tight under "
            "the leaves that it collides with the tick labels of the base axis.")

# ---------------------------------------------------------------- p27, the p27 symbol grid
table(27, 1, 5, 2, "symbols", SEC_SYMB6, "",
      "A small untitled SYMBOL/DEFINITION grid, 399.8 by 159.7 pt at 96.2 per cent of the "
      "measure, sitting directly under the 6.2 Symbols and Definitions heading with no caption "
      "and no number: the routing chapter's five symbols - c_ij, j, i, x_ij and H_1 - under a "
      "black header band and white small caps, a rule between the rows, no vertical between the "
      "two columns. Unlike Table 4.1 and Table 4.2 this list is Latin italic rather than Greek: "
      "the chapter it belongs to counts things rather than rates them. Not excluded, because it "
      "is a real ruled grid inside the text flow; recorded as a table with an empty caption and a "
      "numbering of none because the paper gives it neither.",
      rule="boxed", numeric=0, width="full", source="none")

# ---------------------------------------------------------------- p29, Figure 7.1
figure(29, 1, "flowchart-or-schematic",
       cap(29, "figure7.1:", "delivery locations and route"), "Figure N:", none_mention(),
       "solution", SEC_ALGO, labels=True,
       note="The routing algorithm, 329.8 by 454.5 pt at 79.4 per cent of the measure and the "
            "tallest exhibit on the paper: a single vertical flow chart drawn in vector, in "
            "capitals throughout, running from the start box through the clustering and CLATER "
            "steps and the TSP model to 'FINISH EVERY ROUTE IN ONE DAY?', with a Y branch to the "
            "output box and an N branch that increases a counter and returns. Four of its box "
            "labels are truncated - the text runs to the edge of the shape and stops - and the "
            "N-return connector is routed straight through the 'INCREASE THE NUMBER OF' box "
            "instead of around it, so the loop reads as passing through that step. The six "
            "regions the measurer split off this chart are listed as excluded rather than counted "
            "as separate exhibits.")

# ---------------------------------------------------------------- p39, Figures 9.1 and 9.2
FIG9 = cap(39, "figure9.1:", "spreading in hospitals")
figure(39, 1, "line", FIG9, "Figure N:", none_mention(), "other", SEC_OTHER9,
       legend="inside", labels=True,
       note="302.5 by 226.5 pt at 72.8 per cent of the measure: total cases against time from "
            "February 1st, y 3000 to 4200, x 0 to 60, three series keyed inside a boxed legend in "
            "the upper left. The three keys are policy levels rather than model variables - the "
            "100, 50 and 10 per cent hospital-control cases - so the chart is a what-if family "
            "rather than a fit. It sits above the section Ⅸ heading printed at the foot of p38, "
            "which is the heading it belongs to although the heading pass never indexed it.")
figure(39, 2, "line",
       cap(39, "figure9.2:", "spreading in funerals"), "Figure N:", none_mention(),
       "other", SEC_OTHER9, legend="inside", labels=True,
       note="The funeral-control twin of Figure 9.1, 290.8 by 218.2 pt at 70.0 per cent of the "
            "measure, same axes and same boxed legend, but the level set is 0, 50 and 90 per cent "
            "rather than 100, 50 and 10 - so the two charts answer different questions and the "
            "pair cannot be read side by side as a like-for-like comparison. The 50 and 90 per "
            "cent curves cross and overprint each other between about day 15 and day 25.")

# ---------------------------------------------------------------- p41, Figure 11.1
figure(41, 1, "line",
       cap(41, "figure11.1:", "to the total cases"), "Figure N:", none_mention(),
       "sensitivity", SEC_SENS1, legend="inside", labels=True,
       note="360.9 by 217.0 pt at 86.9 per cent of the measure: a marker-and-line sensitivity "
            "chart whose horizontal axis is a date category axis running 2/1 to 4/2 rather than a "
            "model parameter, with light gridlines behind the series. The chart is drawn by a "
            "spreadsheet rather than by the plotting code behind the section 4 fits - the type, "
            "the gridlines and the marker style all change at the section 11 boundary - and the "
            "category axis means the perturbation it claims to sweep is plotted as a sequence of "
            "dates instead of as a value.")

# ---------------------------------------------------------------- p42, Figures 11.2 and 11.3
figure(42, 1, "bar",
       cap(42, "figure11.2:", "to the total cases"), "Figure N:", none_mention(),
       "sensitivity", SEC_SENS1, legend="inside", labels=True,
       note="A clustered bar chart, 360.9 by 217.0 pt at 86.9 per cent of the measure, three bars "
            "per date group against a value axis that starts at zero. The zero base is the whole "
            "problem: the three bars in every group differ by a few per cent of a total that runs "
            "into the thousands, so they are within a line width of each other and the chart shows "
            "no visible effect at all - which is the conclusion the prose draws ('the total cases "
            "stay relatively stable'), reached here by construction rather than by measurement. "
            "Filed under 11.1 Sensitivity Analysis of SEIIRF Model, where the printed heading "
            "above it puts it, although its own caption and the 11.2 heading below it both speak of "
            "the medicine-production speed model.")
figure(42, 2, "line",
       cap(42, "figure11.3:", "to the total cases"), "Figure N:", none_mention(),
       "sensitivity", SEC_SENS2, legend="inside", labels=True,
       note="The third sensitivity chart, 348.0 by 260.2 pt at 83.8 per cent of the measure: "
            "five series, b1 equal to 3 through 7, keyed in a boxed legend in the upper right. The "
            "b1 = 5 dotted and b1 = 7 marker-only series are low contrast against the frame and "
            "against each other, so two of the five cases the chart exists to show are barely "
            "legible. Unlike Figure 11.2's caption this one names the parameter by its spreadsheet "
            "row label ('b1') rather than by the Greek letter used everywhere else on the paper.")

# ---------------------------------------------------------------- p30, Figure 7.2
figure(30, 1, "map-or-plan-view",
       cap(30, "figure7.2:", "one delivery location in guinea"), "Figure N:", none_mention(),
       "solution", SEC_GUINEA, legend="inside", labels=True,
       note="429.0 by 263.6 pt at 103.3 per cent of the measure: a prefecture-level choropleth of "
            "Guinea, some thirty prefecture boundaries over an irregular national outline, "
            "prefecture names in small grey type, filled in five steps of blue-grey from 1-5 cases "
            "to 501-4000 under a five-chip legend titled 'Confirmed Cases' at the lower left. Two "
            "closed route loops are drawn over the raster in navy, with solid red circular markers "
            "at the prefecture capitals, and the two candidate locations are marked A and B. The "
            "map is a pasted bitmap with its labels added afterwards as vector text, and that is "
            "where it breaks: the word 'location' is centred straight on the northern route, so the "
            "navy line and its red markers run through the glyphs, and the magenta A and B float in "
            "open map with no leader and no anchor - B sits about 40 pt from the nearest route. The "
            "legend bins are also non-monotonic and overlap: '6-30' is followed by '21-100'.")

# ---------------------------------------------------------------- p31, Figure 7.3
figure(31, 1, "map-or-plan-view",
       cap(31, "figure7.3:", "three delivery locations in guinea"), "Figure N:", none_mention(),
       "solution", SEC_GUINEA, legend="inside", labels=True,
       note="The same Guinean choropleth and the same five-chip case legend, 463.5 by 263.3 pt at "
            "111.6 per cent of the measure and the widest map on the paper: six route polylines in "
            "three colours - two navy A and B in the west, two yellow C and D in the north-centre, "
            "two orange E and F in the south-east - each threaded through red markers at the "
            "capitals. Three separate 'location' words are printed here, one per chosen site, and "
            "all three are struck through by their own routes. The magenta letters A to F sit off "
            "the loops they label with no leader line, the yellow C loop is not a closed polygon - "
            "its segments cross and one diagonal runs from a southern marker to the far-east one - "
            "and a stray numeral 1 sits at the right edge, detached from every route and label.")

# ---------------------------------------------------------------- p31, the Guinea distance grid
table(31, 2, 1, 6, "solution", SEC_GUINEA, "",
      "The Guinea route lengths, a six-column one-row grid, 349.0 by 52.0 pt, no caption and no "
      "number: A through F across a black header band and 752.2, 686.6, 578.0, 546.5, 640.4 and "
      "701.2 beneath them, in kilometres by inference only, since the grid carries no unit. This is "
      "the table the prose introduces as 'the distances of them show in the table:' immediately "
      "after the map, and the introducing sentence itself drops a route - 'A, B, C, D, E and "
      "represent the two route' - so the six values are matched to the six letters by eye. Clipped "
      "closed and clean otherwise.",
      rule="boxed", numeric=6, width="full", source="none")

# ---------------------------------------------------------------- p32, Table 7.1
table(32, 1, 6, 2, "solution", SEC_GUINEA,
      "The route is listed:",
      "The six tours, 426.7 by 297.0 pt at 102.7 per cent of the measure: a narrow letter column "
      "A to F behind one internal vertical rule, and a wide column holding each tour as a chain of "
      "prefecture names in capitals joined by solid right-pointing arrowheads, from DUBREKA round "
      "six prefectures and back. Boxed - closed outer frame, a full-width rule at every one of the "
      "six row boundaries, and that one vertical for the letter column; no interior horizontals "
      "inside a row because a row is a chain, not cells. Rows A and E are the only two that wrap, "
      "and each continuation line begins with a bare arrowhead ('->COYAH->DUBREKA', "
      "'->KEROUANE->MACENTA') with no place name in front of it, so the wrap reads as a dangling "
      "lead arrow rather than a continued chain. The caption sits under the standfirst 'The route "
      "is listed:' and above the grid.",
      rule="boxed", numeric=0, width="full",
      cap_text=cap(32, "table7.1:", "the six routes"), position="above")

# ---------------------------------------------------------------- p33, Figure 7.4
figure(33, 1, "map-or-plan-view",
       cap(33, "figure7.4:", "one location in Liberia"), "Figure N:", none_mention(),
       "solution", SEC_LIBERIA, legend="inside", labels=True,
       note="The Liberian choropleth, 404.9 by 278.5 pt at 97.5 per cent of the measure: fourteen "
            "county boundaries over the national outline, county names in small grey type, the same "
            "five-step blue-grey ramp, and the legend moved to the upper right with its title "
            "'Confirmed Cases' broken over two lines. Two navy polylines with red markers at the "
            "county capitals, one 'location' word and the magenta A and B. Three defects: the word "
            "'location' is overprinted by the routes with a red marker sitting inside it; both "
            "routes are drawn in the same navy with no colour or dash distinction, so which is A "
            "and which is B rests entirely on two magenta letters floating 30 to 40 pt from any "
            "marker; and the county names RIVER CESS and GRAND GEDEH are partly hidden under the "
            "route lines.")

# ---------------------------------------------------------------- p33, the Liberia distance grid
table(33, 2, 1, 2, "solution", SEC_LIBERIA, "",
      "The Liberian route lengths, 109.0 by 52.0 pt, two columns and one body row: A and B on a "
      "black header band with 869.0 and 715.6 under them, the numbers the prose then turns into "
      "'Therefore, the deliver location is Grand Bassa.' No caption, no number, no unit. At a "
      "quarter of the measure it reads as a floating fragment between two paragraphs, and the same "
      "construction appears again on the next page for Sierra Leone.",
      rule="boxed", numeric=2, width="column", source="none")

# ---------------------------------------------------------------- p34, Figure 7.5
figure(34, 1, "map-or-plan-view",
       cap(34, "figure7.5:", "Sierra Leone"), "Figure N:", none_mention(),
       "solution", SEC_SIERRA, labels=True,
       note="433.9 by 284.7 pt at 104.4 per cent of the measure: the third country map, a filled "
            "choropleth of Sierra Leone's districts with the confirmed-case ramp behind it and the "
            "two candidate nodes drawn on top as a small node-link overlay, A and B, joined to the "
            "chosen location. The caption is the bare place name - 'figure7.5: Sierra Leone' - so it "
            "does not say what is being shown, and the section heading above it, 7.2.3 Sierra "
            "Leone, says the same two words. One defect: the italic 'location' label and the "
            "magenta A and B markers are overprinted on the map fills and on the link lines, so "
            "the two candidates are hard to tell apart from the shading they sit on. The exhibit "
            "itself is not clipped.")

# ---------------------------------------------------------------- p34, the Liberia/Sierra Leone distance grid
table(34, 2, 1, 2, "solution", SEC_SIERRA, "",
      "A one-row two-column distance grid, 109.0 by 52.0 pt, no caption and no number: A and B "
      "across the head and 411.4 and 616.9 beneath them, the two route lengths the prose "
      "introduces as 'the distances of them show in the table:'. Printed as a bare ruled box in "
      "the middle of a sentence, which is why the measurer caught it as a region at all. The last "
      "of the three such grids on the paper and, with the p33 r2 grid built to exactly the same "
      "109 by 52 pt, one of the two smallest exhibits in the census.",
      rule="boxed", numeric=2, width="column", source="none")

# ---------------------------------------------------------------- p35, the 8.3 symbol grid
table(35, 1, 8, 2, "symbols", SEC_SYMB8, "",
      "The medicine-production chapter's symbol list, 356.1 by 303.5 pt at 85.7 per cent of the "
      "measure, boxed, eight rows under a SYMBOL/DEFINITION head on a black band. It has no "
      "caption of any kind - not above it in the fourteen points before the grid and not below "
      "it - and is introduced only by the section heading '8.3 symbols and definitions', which is "
      "the one heading on the paper printed in lower case after its number. The symbols run from "
      "V_1 through lambda_i^-1, so this is the fastest-production-rate chapter's notation: the "
      "exhibit that says what the medicine-speed model's terms mean, printed without a name.",
      rule="boxed", numeric=0, width="full", source="none")

# ---------------------------------------------------------------- p36, Figure 8.1
figure(36, 1, "line",
       cap(36, "figure8.1:", "speed of producing medicine"), "Figure N:",
       cited(36, 36, ["figure 8.1"], 1, qtail(36, "From the figure 8.1,", 6)),
       "model", SEC_SPEED, labels=True,
       note="266.3 by 199.7 pt at 64.1 per cent of the measure: a single solid black curve of "
            "medicine produced per day against time, rising to a peak of 123 units at about day "
            "23 and stopping there. The prose reads the peak as a milestone - production grows "
            "linearly until every first-stage patient can be treated and then holds - so the "
            "chart's one line is the paper's statement of how fast it can make medicine. No "
            "legend, because one series needs none; the axes carry no titles.")

# ---------------------------------------------------------------- p37, Figure 8.2
figure(37, 1, "line",
       cap(37, "figure 8.2:", "When Using Medicine"), "Figure N:", none_mention(),
       "result", SEC_SPEED, legend="inside", labels=True,
       note="301.7 by 225.9 pt at 72.6 per cent of the measure: total cases against time for the "
            "three countries at once - Guinea, Liberia and Sierra Leone as three series under a "
            "legend inside the frame - with two vertical dashed reference lines marking the points "
            "the prose reads off. It is the only exhibit on the paper that puts the three "
            "countries on one axis, which is what makes it the closest thing to a comparison the "
            "paper prints; the three series are not scaled to population and the caption does not "
            "say so.")

# ---------------------------------------------------------------- p38, Figure 8.3
figure(38, 1, "line",
       cap(38, "figure8.3:", "Quantity of The Medicine"), "Figure N:", none_mention(),
       "result", SEC_QUANT, labels=True,
       note="238.6 by 178.9 pt at 57.4 per cent of the measure, the smallest chart on the paper: "
            "a single logistic curve flattening at about 3,400 units, drawn over a dotted "
            "gridlines background. The saturation value is the number the prose then quotes - "
            "'we need about 3400 units of medicine to cure the patient who are in first stage in "
            "the three west African countries' - so the chart and the sentence carry the same "
            "figure, and the gridlines are the only decoration in an otherwise bare plot.")

# ---------------------------------------------------------------- payload
# doc_order follows the page, not the order in which the blocks above were written: sort the
# figures and the grids together by (page, region) and number them straight through.
for _n, _row in enumerate(sorted(ITEMS + TABLES, key=lambda r: (r["page"], r["place"]["page_order"])), 1):
    _row["place"]["doc_order"] = _n

RULES: list[str] = [
    "Panels are measured boxes, not figure numbers, so a two-panel exhibit drawn inside one "
    "measured region carries a panel_count of two rather than two rows [geometry.panel_count].",
    "Full width means 75 per cent or more of this paper's own 415.4 pt text measure, never of the "
    "595.32 pt page: Table 4.2 at 111.2 per cent is full and overruns the block, while every "
    "centred chart at 51 to 80 per cent is measured against the same number [table.width].",
    "The paper splits its captions by exhibit type: all seven numbered tables print theirs above "
    "the grid and all twenty-three figures print theirs below the art, without one exception in "
    "either direction, which is why position is recorded per row rather than assumed - and the "
    "five grids that print no caption at all keep the default while caption_source stays none "
    "[caption.position].",
    "This paper prints every caption in lower case with no space after the word - 'figure4.6:' on "
    "most pages, 'figure 4.6:' on a few - and the numbering vocabulary has no lower-case form, so "
    "num is recorded as 'Figure N:' and the printing is described in the note "
    "[caption.numbering].",
    "A table with no number is still a table when it is a ruled grid inside the prose: the three "
    "'distances of them show in the table:' grids carry an empty caption and a numbering of none "
    "by default, not a made-up number [caption.verbatim].",
    "Seven of the fifty-four measured regions are ordinary prose, because this PDF paints a white "
    "filled rectangle behind every text line and the measurer grouped the rectangles into bands. "
    "The white fills give them away - 1.05 to 2.00 per line in the bands against 0.00 in every "
    "exhibit - which is why a region's area buys it nothing here [place.area_frac].",
    "Two flow charts are each measured as one whole region plus six node fragments, because the "
    "nodes are raster blocks dropped into a vector drawing; the fragments are excluded as "
    "fragments of the chart rather than counted as six more exhibits, so the second region on "
    "p12 and the second region on p29 carry the whole drawing between them [place.page_order].",
    "Where the prose cites an exhibit more than once, count records the printed instances outside "
    "that exhibit's own caption, and first_page the earliest of them [mention.count].",
    "Section paths follow the printed heading above the block, so figure 11.2 is filed under 11.1 "
    "and figure 11.3 under 11.2, which is where the paper put them, not where their captions "
    "belong [place.section_path].",
    "Two section labels are headings the heading pass missed - the Roman-numbered 'IX Other "
    "Factors We Think Are Important' on p38 and '8.3 symbols and definitions' on p35 - and both "
    "are accepted because each is a printed line of the text layer [place.section_path].",
    "Twenty-four of the thirty numbered exhibits are never named in the prose at all; the six that "
    "are carry a count, and every one of those six is cited on its own page, so no exhibit on this "
    "paper is ever back-referenced across a page break [mention.lead_pages].",
    "Note sentences are quoted from the layer that introduces the grid, which is why three of the "
    "six carry the paper's own errors - 'There are some symbols appear', 'We calculate all "
    "parameters in Guinea are' and 'parameters Sierra Leone:' [table.note_sentence].",
]

NOTE = (
    "Paper 72, Team 34317. Fifty-four measured regions over thirty-one of the forty-seven pages, "
    "and all fifty-four are accounted for: thirty-five exhibit regions - twenty-three figures, "
    "seven numbered tables and five captionless grids - and nineteen exclusions, so unaccounted "
    "is zero and nothing is left unresolved. The paper numbers twenty-three figures and seven "
    "tables and every one of the thirty is here.\n\n"
    "The paper's own habit is what makes this census unusual. It paints a white filled rectangle "
    "behind every line of type, and the measurer read those rectangles as illustrated blocks, so "
    "seven of the fifty-four regions are ordinary paragraphs and two integral display equations. "
    "The white fills separate them from real exhibits without a judgement call: every prose band "
    "carries 1.05 to 2.00 filled rectangles per text line and every pasted bitmap and drawn grid "
    "carries none. The same page-painting habit splits each flow chart into a chart region plus "
    "six fragments, because the node boxes are raster blocks dropped into a vector drawing, so "
    "the twelve fragment regions are excluded rather than counted as twelve more exhibits.\n\n"
    "What the exhibits are. Twelve line plots carry the fitting and the sensitivity work, four "
    "are schematics - the two compartment graphs and the two flow charts - four are prefecture or "
    "county choropleths of the three countries, one is a dendrogram, one a clustered bar chart and "
    "one a three-dimensional exploded pie, and twelve are grids. The line plots come in two "
    "manufactures: the section 4 fit panels are pasted Matlab bitmaps, while the section 11 "
    "sensitivity charts are spreadsheet output with gridlines and category axes, and the change "
    "is visible in the type.\n\n"
    "Eleven exhibit regions run wider than the paper's own 415.4 pt measure, led by Figure 4.9 at "
    "116.7 per cent and Figure 4.8 at 114.8; Table 4.2 at 111.2 per cent puts a grid 46 pt into "
    "the right margin. Three of the four country maps overrun as well, by 3 to 12 per cent, "
    "because the bitmap inside them was pasted wider than the block; the Liberian map is the only "
    "one that fits.\n\n"
    "Defects worth recording, in rough order of how much they cost a reader. Both compartment "
    "graphs end in a dangling arrow: Figure 4.1's F and Figure 4.5's F both point into empty white "
    "space with no target node, and Figure 4.5 redraws the same circle-and-arrow grammar without "
    "repairing it. On the delivery maps the word 'location' is drawn on top of the route polylines "
    "and the magenta A to F letters float 30 to 40 pt from whatever they label with no leader "
    "line, so the candidate sites have to be inferred; the legend bins are also non-monotonic on "
    "the three maps where the legend was read, from Guinea and Liberia, running 1-5, 6-30, 21-100, "
    "101-500, 501-4000 - which makes two of the five classes of confirmed cases overlap. "
    "Figure 4.3, Figure 4.8 and Figure 4.9 all lost their right plot spine before pasting, so "
    "their right-hand y ticks hang detached inside the frames. Figure 4.3's left prediction curve "
    "is clipped by its own 3500 ceiling. Figure 4.7 prints no vertical-axis title at all. Figure "
    "11.1 plots a parameter sweep on a date category axis, and Figure 11.2 draws a sweep of a few "
    "per cent on a zero-based bar scale where every bar is within a line width of its neighbours, "
    "so the chart cannot show the effect it was made to show. Figure 5.1 is a dendrogram, not the "
    "map the section and the caption both imply, and its caption collides with the leaf labels. "
    "Figure 4.2's fourth box reads 'GENETIC' alone, the operator noun dropped, and the "
    "subscripted f in its decision node overhangs the diamond.\n\n"
    "Type and numbering. Every caption on the paper is printed in lower case with no space after "
    "the word - 'figure4.6:', 'table4.4:' - except on four pages where a space does appear "
    "(figures 4.1, 4.6, 4.7 and 8.2), so the caption layer is inconsistent with itself across "
    "the twenty-five pages that carry a caption. Sections 11.1 and 11.2 are "
    "used twice, once for the sensitivity work on pp41-42 and again for Strengths and Weaknesses "
    "and Overall Results on pp43-44, and the heading pass dropped the Roman-numbered 'IX Other "
    "Factors We Think Are Important' on p38 and '8.3 symbols and definitions' on p35, so Figure "
    "9.1, Figure 9.2 and the p35 symbol grid hang off sections the index does not hold. Figure "
    "11.2 is printed under the 11.1 heading although its caption and the 11.2 heading below it "
    "both describe the production-speed model, and that mismatch is recorded where the paper put "
    "it rather than corrected.\n\n"
    "The five grids the paper prints without a name are the paper's quietest failure. Three of "
    "them are the route-length tables, each introduced only by 'the distances of them show in the "
    "table:', one of them holding six values under letters A to F for a sentence that itself "
    "drops route F; the p31 table is 349 pt wide and the other two are 109 pt, so the same "
    "content arrives at three different sizes with no unit and no number on any of them. The "
    "other two are symbol lists, one under 6.2 and one under 8.3, printed as ruled grids with no "
    "caption at all.\n\n"
    "Citation practice is thin even by this lane's standards. Twenty-four of the thirty numbered "
    "exhibits are never named in the prose. The six that are - Figure 4.1 twice, Figure 4.3, "
    "Figure 4.6, Figure 4.7 twice, Figure 4.8 and Figure 8.1 - are every one of them cited on "
    "their own page, several of them in the sentence that follows the caption, so this paper never "
    "points backwards across a page break and never forecasts an exhibit to come."
)

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc72-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
