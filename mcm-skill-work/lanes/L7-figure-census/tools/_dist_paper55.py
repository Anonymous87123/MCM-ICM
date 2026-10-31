"""Hand pass for P-A-2014-30532-8f80536d (a 2014 A paper on multi-lane cellular-automaton
traffic rules: a Keep-Right-Except-Pass simulation panel, three alternative rules compared, and
a factor-analysis score used to rank them), 29 PDF pages.

Twenty-one measured regions over nineteen pages: 16 figure rows, 3 printed tables and 2
exclusions. Five of the figure regions carry two separately numbered exhibits each, so nineteen
printed figure numbers resolve into fifteen numbered rows plus one uncaptioned flowchart.

    p1-r1   excluded  not-an-exhibit   the summary-sheet control-number form and title band
    p5-r1   flowchart-or-schematic     uncaptioned "analyzing procedure" flowchart
    p9-r1   heatmap-or-contour         Figure 1: Track Time vs. Space
    p10-r1  line                       Figures 2.a-2.c: density against flow / lane change / velocity
    p11-r1  line                       Figures 3.a-3.c: lane count against the same three
    p12-r1  line                       Figures 4.a-4.c: max velocity limit against the same three
    p13-r1  scatter                    Figures 5.a-5.c: big car fraction
    p14-r1  scatter                    Figures 6.a-6.c: lane change probability
    p15-r1  scatter                    Figures 7.a-7.c: random braking probability
    p17-r1  line                       Figures 8 and 9: flow vs density, lane change frequency vs density
    p18-r1  line                       Figures 10 and 11: average velocity vs density, lane usage vs density
    p20-r1  table-grid                 Table 1: eigenvalues of the correlation matrix
    p20-r2  table-grid                 Table 2: rotated factor pattern (continues on p21)
    p21-r1  excluded  split-across-pages   the x6-x8 tail of Table 2
    p21-r2  table-grid                 Table 3: standardized scoring coefficients
    p22-r1  line                       Figure 12: density vs factor score
    p23-r1  line                       Figures 13 and 14: max speed limit, big car fraction
    p24-r1  line                       Figure 15: probability of changing lanes
    p25-r1  line                       Figure 16: probability of random brake
    p26-r1  line                       Figures 17 and 18: density vs flow, density vs lane change
    p27-r1  line                       Figure 19: density vs average velocity, plus an unnumbered chart

Usage: python -I tools/_dist_paper55.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2014-30532-8f80536d"
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

MODEL = "4 Model Development"
KREP = "4.2 Rule analysis\uff1aKeep-Right-Except-Pass Rule"
SIM = "4.2.3 Simulation Results and Discussion"
CMP = "4.3 Comparison of Different Rules"
CMPRES = "4.3.2 Simulation Results and Discussion"
FACRES = "4.3.4 Simulation Results and Discussion"
INTEL = "4.4 Results and Discussion under Intelligent System"
ANALYSIS = "2 Problem Analysis"
METHOD = "2.2 Research Method"

PATH: dict[tuple[int, int], tuple[list[str], str]] = {
    (5, 1): ([ANALYSIS, METHOD], "model"),
    (9, 1): ([MODEL, KREP, SIM], "evaluation"),
}
for _key in [(10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1)]:
    PATH[_key] = ([MODEL, KREP, SIM], "evaluation")
for _key in [(17, 1), (18, 1)]:
    PATH[_key] = ([MODEL, CMP, CMPRES], "evaluation")
for _key in [(20, 1), (20, 2), (21, 2), (22, 1), (23, 1), (24, 1), (25, 1)]:
    PATH[_key] = ([MODEL, CMP, FACRES], "evaluation")
for _key in [(26, 1), (27, 1)]:
    PATH[_key] = ([MODEL, INTEL], "evaluation")

VENTIONS = {5: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 17: 1, 18: 1,
            20: 2, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def deictic(first_page: int, lead_pages: int, *, lead: str = "", trail: str = "") -> dict:
    """A pointer that prints no exhibit number, so it counts as zero named citations."""
    return {"first_page": first_page, "lead_pages": lead_pages, "style": [], "count": 0,
            "lead_sentence": lead, "trail_sentence": trail, "lead_pattern": "direct",
            "read_sentences": 1, "gap_sentences": None}


CAP = {
    2: "Figure 1: Track Time vs. Space",
    3: "Figure 2.b: Density vs. Lane Changing Figure 2.a: Density vs. Flow Frequency "
       "Figure 2.c: Density vs. Velocity",
    4: "Figure 3.b: Lanes vs. Lane Changing Figure 3.a: Lanes vs. Flow Frequency "
       "Figure 3.c: Lanes vs. Velocity",
    5: "Figure 4.b: Max Velocity Limit vs. Lane Figure 4.a: Max Velocity Limit vs. Flow "
       "Changing Frequency Figure 4.c: Max Velocity Limit vs. Velocity",
    6: "Figure 5.b: Big Car Fraction vs. Lane Figure 5.a: Big Car Fraction vs. Flow "
       "Changing Frequency Figure 5.c: Big Car Fraction vs. Velocity",
    7: "Figure 6.b: Lane Change Probability vs. Lane Figure 6.a: Lane Change Probability "
       "vs. Flow Changing Frequency Figure 6.c: Lane Change Probability vs. Velocity",
    8: "Figure 7.a: Random Braking Probability vs. Figure 7.b: Random Braking Probability "
       "vs. Flow Lane Changing Frequency Figure 7.c: Random Braking Probability vs. Velocity",
    9: "Figure 8: Flow vs. Density",
    10: "Figure 10: Average Velocity vs. Density",
    11: "Figure 12: Density vs. Factor Score",
    12: "Figure 13: Max speed limits vs. Factor sore",
    13: "Figure 15: Probability of changing lanes vs. Factor score",
    14: "Figure 16: Probability of random brake vs. Factor score",
    15: "Figure 17: Density vs. Traffic Flow",
    16: "Figure 19: Density vs. Average Velocity",
}

T_CAP = {1: "Table 1", 2: "Table 2", 3: "Table 3"}

MENTION = {
    1: deictic(5, 0, lead="The analyzing procedure can be illustrated by the flowchart below:"),
    2: deictic(9, 0, trail="We can find that traffic jam is generated after a period of time."),
    3: deictic(10, 0, trail="The figures show that with the density increasing, flow and lane "
                         "changing frequency both first increase then decrease"),
    4: deictic(11, 0, trail="Obviously, flow\u3001lane changing frequency and average velocity "
                          "all increase with the lane number."),
    5: deictic(12, 0, trail="We can find that at first, flow and average velocity both increase "
                          "with the max velocity"),
    6: deictic(13, 0, trail="We find that big car fraction mainly influence the lane changing "
                          "frequence"),
    7: deictic(14, 0, trail="We find that with the increase of lane changing probability, flow"),
    8: deictic(15, 0, trail="We can see that with the random braking probability increase, flow "
                          "and average velocity decrease"),
    9: deictic(17, 0, trail="This figure shows that, when density is around 0.15, "
                          "Keep-left-or-right rule has a bigger flow."),
    10: deictic(18, 0, lead="Compare this two figures, because our lane is a loop which means "
                          "the total lane usage is not changed"),
    11: deictic(22, 0, lead="We apply theses scoring functions to our simulation data, and get "
                          "following curves."),
    12: deictic(22, 1, lead="We apply theses scoring functions to our simulation data, and get "
                          "following curves."),
    13: deictic(24, 0, trail="Above figure shows that, with the increase of lane changing "
                           "probability, the flow of three rules is sable with no big change"),
    14: deictic(25, 0, trail="From above figure we can find that with the increase of random "
                           "braking probability, the flow decrease but the safety increase."),
    15: deictic(25, 1, lead="The following are figures of flow, lane change frequency and "
                          "average speed."),
    16: deictic(25, 2, lead="The following are figures of flow, lane change frequency and "
                          "average speed."),
    101: deictic(20, 0, lead="We use principal component method to estimate the factor loading "
                           "matrix, and get the eigenvalues of the correlation matrix"),
    102: deictic(20, 0, lead="Then we apply the orthogonal rotation that has the biggest "
                           "variance to the factor loading matrix, and get the rotated factor "
                           "pattern:"),
    103: deictic(21, 0, lead="After that, we use Thompson factor to calculate the scores of F1, "
                           "F2, F3 and F4, and get the following form of standardized scoring "
                           "coefficients:"),
}


def printed(page: int, text: str) -> str:
    """Verify a caption really prints on the page, once Unicode-normalised."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text))
    return text


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH[(page, reg)]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": PAGE_SEEN[page] + sum(VENTIONS[p] for p in VENTIONS if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, position: str, numbering: str) -> dict:
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


def figure(page: int, reg: int, family: str, key: int, *, text: str | None = None,
           numbering: str = "Figure N:", panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = True, labels: bool = False,
           note: str = "", other_note: str = "") -> None:
    ORDER.append((page, reg))
    cap = "" if text is not None and text == "" else printed(page, CAP[key])
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap,
        "caption_source": "text-layer" if cap else "none",
        "note": note,
        "place": place(page, reg),
        "mention": dict(MENTION[key]),
        "caption": caption_block(cap, "below", numbering if cap else "none"),
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
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, key: int, *, cap_page: int | None = None, rows: int,
          cols: int, header_rows: int = 2,
          rules: str = "vertical-rules", numeric_cols: int = 4, text_cols: int = 1,
          merged: bool = True, continued: bool = False, note: str = "") -> None:
    ORDER.append((page, reg))
    text = printed(page if cap_page is None else cap_page, T_CAP[key])
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": dict(MENTION[100 + key]),
        "caption": caption_block(text, "below", "Table N"),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rules, "zebra": False, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": True, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "column", "orientation": "portrait",
            "continued": continued, "note_sentence": "",
        },
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note})


def build() -> str:
    excluded(1, 1, "not-an-exhibit",
             "The summary-sheet frame: the control-number form grid, the contest title band and "
             "the signature lines. A form to be filled in, with no artwork, no axis and no "
             "caption, so it is not an exhibit.")

    # --- section 2.2: the analysis framework ----------------------------------------------
    figure(5, 1, "flowchart-or-schematic", 1, text="", numbers=False,
           note="The uncaptioned 'analyzing procedure' flowchart of section 2.2: a box reading "
                "'The performance of rule' over three levels of plain rectangles - Heavy and "
                "Light traffic, then Density fed by Number of lanes, Max speed limit, Vehicle "
                "types and Random brake probability, then Traffic flow, Safety and an ellipsis "
                "box, then Velocity, Lane change and a second ellipsis box - joined by plain "
                "orthogonal arrows. No figure number, no axis, no scale and no printed values; "
                "the caption field is empty because the page prints none [caption.numbering].")

    # --- section 4.2.3: the Keep-Right-Except-Pass panel ----------------------------------
    figure(9, 1, "heatmap-or-contour", 2, panels=2, layout="1x2", numbers=False,
           note="The space-time diagram of the simulation: two side-by-side blocks of a cell "
                "lattice, one per lane, each cell holding a printed digit 0 to 5 for the number "
                "of vehicles in that road section, so the picture is a state grid rather than a "
                "curve. Bare arrow axes only - 'Space' along the top and 'Time' down the left - "
                "with no ticks, no scale, no colour ramp, no colour bar and no legend. The "
                "lattice blocks are dense type, and the jam that the prose describes reads as a "
                "wedge of high digits spreading backwards through the left block "
                "[geometry.printed_numbers].")
    figure(10, 1, "line", 3, panels=3, layout="2x2",
           note="Three quarters of a 2x2 plate, cell bottom-right empty: panel a plots flow "
                "against density with open square markers on a thin line, panel b lane changing "
                "frequency against density, panel c velocity against density, each carrying its "
                "own small in-image title ('Density vs. Flow', 'Density vs. LaneChange', "
                "'Density vs. Velocity') and its own axis titles in density(vehicle/section) "
                "units. No legend, no data labels, printed ticks on every axis. The typeset "
                "sub-captions sit below each panel and the text layer reads them right to left, "
                "b then a then c, which is why the quoted caption keeps that order "
                "[caption.verbatim].")
    figure(11, 1, "line", 4, panels=3, layout="2x2",
           note="The lane-count sweep: three single-series line charts with open square markers, "
                "x 'lanes' 1 to 8, y flow / laneChange frequency / velocity respectively. Panel "
                "b rises as an almost exact straight line, which is the least credible curve in "
                "the set. No legend and no data labels; in-image titles read 'Lanes vs. Flow', "
                "'Lanes vs. LaneChange', 'Lanes vs. Velocity'.")
    figure(12, 1, "line", 5, panels=3, layout="2x2",
           note="The maximum-velocity sweep: three single-series line charts in blue, red-brown "
                "and green, x 'max speed(section/s)' 1 to 10. Panel b is non-monotonic - a sharp "
                "dip to about 0.06 at x = 3 then a slow rise - where the prose says lane "
                "changing frequency simply decreases. In-image titles say 'Max_Speed vs. ...', "
                "with an underscore and without the caption's words 'Velocity Limit'.")
    figure(13, 1, "scatter", 6, panels=3, layout="2x2",
           note="The big-car-fraction sweep, and the first of three scatter plates: three "
                "unconnected square-marker clouds of about a hundred points each. Panel a's "
                "x-axis is titled 'bic car fraction' (the paper's typo, twice) and runs 0 to 1 "
                "in decimals while panels b and c run 0 to 100 as percentages for the same "
                "variable. Panel a is pure noise on a y-range of one thousandth of a unit, so "
                "the trend the prose claims is not visible; panels b and c show a decrease and a "
                "flat band respectively.")
    figure(14, 1, "scatter", 7, panels=3, layout="2x2",
           note="The lane-change-probability sweep: three unconnected point clouds, again with "
                "the same 0 to 1 against 0 to 100 x-scale split between panel a and panels b and "
                "c. Panel c's axis is titled 'lane change probability' while carrying 0 to 100 "
                "ticks. No legend, no data labels, printed ticks throughout.")
    figure(15, 1, "scatter", 8, panels=3, layout="2x2",
           note="The random-braking sweep: three dense point clouds, panel a blue open squares, "
                "panel b small green circles, panel c red open squares, each a single series "
                "with no legend and no data labels. The compositor swapped the sub-captions: the "
                "typeset letter b sits under the panel titled 'vs. Velocity' and the letter c "
                "under the one titled 'vs. Lane Change', so the quoted caption and the artwork "
                "disagree about which panel is which [caption.verbatim].")

    # --- section 4.3.2: the alternative rules ----------------------------------------------
    figure(17, 1, "line", 9, panels=2, layout="2x1", legend="inside",
           note="Two stacked charts in one raster: above, flow against density for the three "
                "rules with a key inside at the middle right; below, lane changing frequency "
                "against density with a key inside at the upper left. Both key "
                "'Keep-Left-Or-Right', 'Hight-in-Left-Low-in-Right' and 'Keep-Right-Except-Pass' "
                "(the paper's spelling) and both print ticks. The upper chart's y-axis starts at "
                "0.1 rather than 0, and its three curves lie within a line thickness of each "
                "other although the prose claims one rule has 'a bigger flow'. The lower chart's "
                "curves are cleanly separated, the red one reaching 0.23 against 0.045 and 0.03. "
                "Both exhibits are numbered in the text layer - Figures 8 and 9 - and both "
                "captions print below their chart, so the row quotes both "
                "[geometry.panel_count].")
    figure(18, 1, "line", 10, panels=3, layout="2x1+1x2", legend="inside",
           note="The same construction one page on: Figure 10's average-velocity chart across "
                "the top, then a two-panel lane-usage exhibit split left and right below, making "
                "three plot panels in the region. Legends sit inside each frame (lower left, "
                "then lower right twice) with the same three rule names. The lane-usage y-axes "
                "are not matched - 0 to 0.4 on the left against 0 to 0.35 on the right - for two "
                "quantities the prose describes as a closed loop, and the series everywhere are "
                "so nearly coincident that stroke colour is the only discriminator "
                "[geometry.panel_count].")

    # --- section 4.3.4: the factor analysis ------------------------------------------------
    table(20, 1, 1, rows=9, cols=5,
          note="The eigenvalue table, a boxed SPSS-style grid: a merged title cell reading "
               "'Eigenvalues of the Correlation Matrix: Total = 8 Average = 1' across all five "
               "columns, a header row of Eigenvalue, Difference, Proportion, Cumulative over a "
               "blank stub, then eight numbered rows. Full-height vertical rules between every "
               "column, an outer frame on all four sides, a rule under the header and a rule "
               "between every body row, decimal-aligned statistics and no zebra. Row 8 prints an "
               "empty Difference cell, which is blank rather than merged. The caption is the "
               "bare word 'Table 1' below the grid, with no title "
               "[table.merged_cells].")
    table(20, 2, 2, cap_page=21, rows=10, cols=5, continued=True,
          note="The rotated factor pattern, split over the page break: a merged title cell "
               "'Rotated Factor Pattern' with an empty spacer row beneath it, a header row of "
               "Factor1 to Factor4 over a blank stub, then eight rows x1 to x8 loaded -0.89 to "
               "0.90. Five rows print on page 20 and the last three on page 21 with the title "
               "and header repeated, so the row carries `continued` true and the p21 band is "
               "excluded `split-across-pages`. The caption 'Table 2' prints on page 21 under the "
               "tail, not under the p20 band [table.continued].")
    excluded(21, 1, "split-across-pages",
             "The x6, x7 and x8 tail of Table 2 with its merged 'Rotated Factor Pattern' title "
             "and header row repeated, closing with the table's bottom rule and the caption "
             "'Table 2'. Counted once, on the p20 region.")
    table(21, 2, 3, rows=10, cols=5,
          note="The standardized scoring coefficients in the same boxed construction: merged "
               "title cell 'Standardized Scoring Coefficients', a header row of Factor1 to "
               "Factor4 over a blank stub, eight rows x1 to x8, vertical rules full height, "
               "outer frame, no zebra. The coefficients here are the ones the p22 equations "
               "print, so the table and the three factor-score formulas can be cross-checked "
               "digit by digit; the caption is the bare 'Table 3' below the grid "
               "[table.rule_style].")
    figure(22, 1, "line", 11, legend="below",
           note="The first factor-score plate: six series over density - solid lines for "
                "KROL, KREP and HLLR traffic flow, dashed lines for the same three rules' safety "
                "- keyed in two blocks in an outside legend below the x-axis, with the x-axis "
                "itself drawn through y = 0 rather than at the foot of the frame. y 'Factor "
                "score' runs -4 to 1.5, x 'Density' 0 to 1.2. The dashed traffic-flow curve "
                "swings up to about 1.05 and back below zero, the widest excursion in the paper.")
    figure(23, 1, "line", 12, legend="below",
           note="Two stacked factor-score plates in one raster: Figure 13 above with x 'Max "
                "speed limits' 0 to 12, Figure 14 below with x 'The proportion of big car' 0 to "
                "1.2, y 'Factor score' on both, six series each keyed in the same outside split "
                "legend (solid traffic flow, dashed safety). Neither plate carries an x-axis "
                "title - the variable name lives only in the legend header. The typeset caption "
                "for Figure 13 misspells 'Factor score' as 'Factor sore', and Figure 14's "
                "caption prints on the same page although the paragraph that discusses it opens "
                "page 24 with 'Above figure shows that with the increasing of the big car "
                "fraction' [caption.verbatim].")
    figure(24, 1, "line", 13, legend="below",
           note="The lane-changing-probability plate: six series on the same encoding, y 'Factor "
                "score' -1.5 to 1.0, x 0 to 1.2 with the tick labels printed above the zero rule "
                "so they read as if inside the plot. Legend outside below, split solid and "
                "dashed, header 'Probability of changing lanes' standing in for an axis title.")
    figure(25, 1, "line", 14, legend="below",
           note="The random-braking plate: six series, y 'Factor score' -2 to 3.5, the widest "
                "range of the factor set with an empty band below -1.4; both curve families "
                "pinch and stop at x about 1, leaving the right margin blank to 1.2. Legend "
                "outside below with the header 'Probability of random brake'.")

    # --- section 4.4: the intelligent-system results ---------------------------------------
    figure(26, 1, "line", 15, panels=2, layout="2x1", legend="inside",
           note="The intelligent-system comparison above, Figure 17's density-against-flow chart "
                "and Figure 18's density-against-lane-change chart below, each keyed inside a "
                "box at the right middle with the same three rule names, each with printed "
                "ticks. Figure 18's lane-change axis is scaled by 10^-4 and its three rules occupy "
                "disjoint density windows - KREP a spike at 0.05 to 0.07, HLLR two teeth at 0.09 "
                "to 0.15, KROL a step from 0.25 - which is the disjointness the prose calls "
                "consistent with the factor analysis [geometry.panel_count].")
    figure(27, 1, "line", 16, panels=2, layout="2x1", legend="inside",
           note="Figure 19's average-velocity chart above and, below it, a larger six-series "
                "factor-score chart that the page introduces with 'we get the data into the "
                "formula of factor score, get the following figure:' and then labels 'Figure 12: "
                "Density vs. Factor Score' - the number and title of the page-22 plate, reused "
                "for a different drawing with different curves and a different axis range (0 to "
                "0.35 against 0 to 1.2). Both numbers are quoted as printed; the reuse is the "
                "paper's, not a transcription slip. The lower chart's x-axis also sits at y = 0 "
                "rather than at the foot, and its six series collapse into two bands so the "
                "three safety curves are unreadable [caption.verbatim].")

    rules = [
        "The numbering is the colon form throughout - 'Figure 1:' to 'Figure 19:' - except for "
        "the three tables, which print a bare 'Table 1', 'Table 2' and 'Table 3' with no title "
        "and no stop, so `caption.numbering` is 'Figure N:' for the figures and 'Table N' for "
        "the tables [caption.numbering].",
        "Five measured regions each carry two separately numbered exhibits, and the layout pass "
        "cannot split them: the p17 plate holds Figures 8 and 9, p18 holds 10 and 11, p23 holds "
        "13 and 14, and p26 holds 17 and 18, all as one raster each. One row per region is "
        "mandatory (`record.py` refuses a region counted twice), so each of those rows quotes "
        "both printed captions in print order and carries `panel_count` for the plot panels it "
        "holds [geometry.panel_count].",
        "Figures 2 to 7 are three-quarters of a 2x2 plate each, with panel a top left, b top "
        "right, c bottom left and the bottom-right cell empty; the typeset sub-captions print "
        "below the panels and the text layer reads them in a different order from the letters "
        "('b', then 'a', then 'c'), so the quoted caption keeps the printed order rather than "
        "the reading order [caption.verbatim].",
        "No exhibit in this paper is cited by number in prose. Every pointer is deictic - 'the "
        "flowchart below', 'the figures show that', 'compare this two figures', 'get following "
        "curves', 'the following are figures of flow, lane change frequency and average speed' - "
        "so all sixteen figure rows and all three tables record an empty style list and "
        "`count` 0, with the pointer sentence quoted from the page it prints on "
        "[mention.lead_pattern].",
        "Three of those deictic pointers run backwards: the p25 sentence 'The following are "
        "figures of flow, lane change frequency and average speed' introduces the p26 and p27 "
        "plates, and the p22 sentence that introduces the factor-score curves is reused for the "
        "p23 plate, so those rows carry a negative `lead_pages` [mention.lead_pages].",
        "Table 2 breaks over the page boundary: five of its eight rows print on page 20 and the "
        "x6 to x8 rows on page 21 with the merged title and header repeated. It is counted once "
        "on the p20 band with `continued` true, and the p21 band is excluded "
        "`split-across-pages` [table.continued].",
        "All three tables are one construction - a merged title cell, an empty spacer row, a "
        "header row of four factor columns over a blank stub, rules under the title and the "
        "header and between every body row, full-height vertical rules and a complete outer "
        "frame, with no zebra anywhere - so all three are `vertical-rules` with "
        "`merged_cells` true and decimal-aligned statistics [table.rule_style].",
        "Every caption in this paper is in the text layer, tables included, and every caption "
        "prints below its grid or chart, so no caption is typed from the crop and no table is "
        "captioned above [caption.position].",
        "The one uncaptioned exhibit is the p5 flowchart, which the prose introduces with 'The "
        "analyzing procedure can be illustrated by the flowchart below:' and never numbers. It "
        "is recorded with an empty caption, `caption_source` none and numbering none "
        "[caption.numbering].",
        "Figure 1 is a state lattice, not a plot: each cell of a two-block space-time grid "
        "prints the number of vehicles in that section, with only bare 'Space' and 'Time' arrow "
        "axes, so it is recorded `heatmap-or-contour` rather than `line` "
        "[geometry.family].",
        "Families follow what is drawn, not what a caption promises: Figures 2, 3 and 4 are "
        "connected line charts with square markers and Figures 5, 6 and 7 are unconnected point "
        "clouds, so the first three are `line` and the last three `scatter`, although all six "
        "are captioned the same way [geometry.family].",
        "The factor-score plates key six series each and put the key outside, below the plot, in "
        "two blocks - solid for traffic flow, dashed for safety - with the x-variable name used "
        "as the legend header instead of an axis title, so `legend` is 'below' on Figures 12 to "
        "16 and 'inside' on the p17, p18, p26 and p27 plates [geometry.legend].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2014\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "A-30532-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twenty-one measured regions over nineteen of twenty-nine pages, resolving into 16 "
            "figure rows, 3 printed tables and 2 exclusions (the p1 summary-sheet form and the "
            "p21 tail of Table 2), with nothing unresolved and no declared gaps. Families: 11 "
            "`line`, 3 `scatter`, 3 `table-grid`, 1 `heatmap-or-contour` and 1 "
            "`flowchart-or-schematic`. Nineteen printed figure numbers resolve into fifteen "
            "numbered rows and one uncaptioned flowchart, because five raster regions carry two "
            "numbered exhibits each and Figures 2 to 7 carry three sub-panels apiece in a 2x2 "
            "plate with one cell empty. The numbering is the colon form 'Figure 1:' to 'Figure "
            "19:' against a bare 'Table 1' to 'Table 3'; every caption is in the text layer and "
            "every caption prints below its art; and no exhibit is cited by number anywhere - "
            "all seventeen pointers are deictic, three of them running backwards onto the page "
            "before their plate. Faults worth carrying downstream: Figures 5 and 6 switch the "
            "same x variable between a 0 to 1 and a 0 to 100 scale, Figure 5's axis is titled "
            "'bic car fraction', Figure 7's typeset sub-captions are swapped against its "
            "in-image titles, Figure 13's caption misspells 'Factor score' as 'Factor sore', the "
            "p27 plate reuses 'Figure 12' as the number and title of a different chart, and "
            "Figure 1 is a printed-digit state lattice rather than a plot."
        ),
    }
    out = PROXY / "pc55-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
