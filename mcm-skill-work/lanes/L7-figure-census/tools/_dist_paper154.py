"""Hand pass for P-C-2018-73767-a72d3a8a (2018 MCM C, team 73767, "A Setting
System of Interstate Energy Cooperation Goals Based on Data Insight": a decoupling
and simultaneous-equations read of four state energy profiles, a PCA evaluation
index, a BP-network forecast under two scenarios, and a cooperate-or-not target
argument, closed by per-state appendix plates).

29 pages, 35 measured regions on 20 of them. Sixteen printed exhibits are shown on
the four appendix plates, where each state gets a profile figure, a means figure,
a pie figure and two grids - so the appendix alone carries 16 of the 36 exhibits.

Usage: python -I tools/_dist_paper154.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2018-73767-a72d3a8a"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
REG = {(pg["page"], i): list(r["bbox"])
       for pg in LAYOUT["pages"] for i, r in enumerate(pg["regions"], 1)}
MEASURED = {(p, tuple(b)) for (p, _), b in REG.items()}

# The appendix is the one part of this paper whose headings the extractor never
# sees; every appendix path therefore carries this prefix.
UNCAP = "未编号标题："


def bb(page: int, index: int) -> tuple[int, list[float]]:
    return page, REG[(page, index)]


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    w, h = DIMS[page]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < h / 3 else ("middle" if mid < 2 * h / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    return {
        "section_path": list(path),
        "section_numbered": not path[0].startswith(UNCAP),
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 1,
        "page_zone": z,
        "area_frac": round(frac, 4),
        "solo_page": False,
    }


def cap(v: str, numbering: str = "Figure N", *, position: str = "below",
        units: bool = False, variables: int = 0, conditions: bool = False,
        concludes: bool = False, voice: str = "none") -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)) if v else 0,
        "sentences": len(schema.sentences(v)) if v else 0,
        "units": units,
        "variables": variables > 0,
        "variable_count": variables,
        "conditions": conditions,
        "concludes": concludes,
        "voice": voice,
        "position": position,
    }


def mention(page: int, *, first: int | None, style: list[str], count: int = 0,
            lead: str = "", pattern: str = "none", trail: str = "",
            read: int = 0) -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": 0 if first is None else count,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def geo(family: str, *, legend: str = "none", numbers: bool = True,
        colorbar: bool = False, three_d: str = "no", panels: int = 1,
        layout: str = "1", shared: bool = False, labels: bool = False) -> dict:
    return {
        "family": family,
        "panel_count": panels,
        "panel_layout": layout,
        "shared_axes": shared,
        "legend": legend,
        "colorbar": colorbar,
        "three_d": three_d,
        "printed_numbers": numbers,
        "data_labels": labels,
    }


def figure(key: str, caption: dict, men: dict, geom: dict, *, path: list[str],
           kind: str, note: str = "", caption_source: str = "text-layer",
           panel_of: str = "", other_note: str = "") -> dict:
    page, bbox = B[key]
    item = {
        "page": page,
        "bbox": bbox,
        "family": geom["family"],
        "confidence": "high",
        "panel_count": geom["panel_count"],
        "is_panel_of": panel_of,
        "caption_verbatim": caption["verbatim"],
        "caption_source": caption_source,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }
    if other_note:
        item["other_note"] = other_note
    return item


def grid(rows: int, cols: int, *, header: int = 1, numeric: int = 0, txt: int = 1,
         rule: str = "booktabs", zebra: bool = False, merged: bool = False,
         diagonal: bool = False, units_in_header: bool = False, decimal: bool = False,
         width: str = "full", continued: bool = False, note: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rule,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diagonal,
        "units_in_header": units_in_header,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": continued,
        "note_sentence": note,
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          note: str = "", caption_source: str = "text-layer") -> dict:
    if caption["numbering"] == "Figure N":
        caption = dict(caption, numbering="Table N")
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": caption["verbatim"],
        "caption_source": caption_source,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "table": g,
    }


FIGURES: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[tuple[str, tuple[int, list[float]], str]] = []
B: dict[str, tuple[int, list[float]]] = {}

S_22 = ["2 Assumptions and Notations", "2.2 Notations"]
S_4 = ["4 Energy Profile"]
S_5 = ["5 Model Construction"]
S_51 = S_5 + ["5.1 Decoupling Analysis"]
S_52 = S_5 + ["5.2 The Simultaneous Equations Model"]
S_53 = S_5 + ["5.3 The Multi-dimensional Evaluation System"]
S_531 = S_53 + ["5.3.1 Construction of Indexes"]
S_532 = S_53 + ["5.3.2 Principle Component Analysis"]
S_54 = S_5 + ["5.4 Energy Profile Predicting System"]
S_542 = S_54 + ["5.4.2 Constructing BP Neural Network"]
S_543 = S_54 + ["5.4.3 Predicting the Target Values"]
S_61 = ["6 Testing Our Model", "6.1 Predicting Reliability Test"]
S_62 = ["6 Testing Our Model", "6.2 Sensitivity Analysis"]
S_72 = ["7 Determining Goals for the Energy Compact", "7.2 Idea two: Cooperate"]


def app(title: str) -> list[str]:
    return [UNCAP + "Appendices", UNCAP + title]
# Pages 7-16: the notation and variable grids, the four California charts that open
# section 4, the elasticity pair, the resource map, the index tree and the BP flow,
# plus the five equation rasters the detector boxes on this paper's text pages.

B["t1"] = bb(7, 1)
TABLES.append(table(
    "t1", cap("Table 1: notation", "Table N:"),
    mention(7, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    grid(14, 2, header=1, numeric=0, txt=2, rule="vertical-rules", width="full"),
    path=S_22, kind="symbols",
    note="The paper's only symbol glossary: a grey header band over Notation / Meaning, "
         "then thirteen italic symbol rows (Epd, Tpd, Rce, ttdp, Cpd, Pri, Ind, Pop, Wcs, "
         "Tcs, Enc, Cep, K). Closed box - a rule between the two columns and a rule on "
         "every row - so it is vertical-rules with a shaded header, not zebra. The prose "
         "never cites it by number; the caption is the only label it gets."))

B["t2"] = bb(8, 2)
TABLES.append(table(
    "t2", cap("Table 2: basic variable", "Table N:"),
    mention(8, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    grid(12, 2, header=1, numeric=0, txt=2, rule="boxed", width="full"),
    path=S_4, kind="other",
    note="Eleven basic variables mapped to the Federal Reserve dataset's mnemonics, under a "
         "grey header band. The only grid in the paper with a plain frame and no internal "
         "vertical rule - a header rule, two side rules and a foot rule, and NOTHING between "
         "rows, so long mnemonics (GDPRX, TETCB) never collide. Printed 0.85 of the measure "
         "wide. Uncited: it is reached from the sentence 'we call them the basic variables' "
         "immediately above it, with no number."))

B["f1"] = bb(9, 1)
FIGURES.append(figure(
    "f1", cap("Figure 1: change trend of price and energy consumption in California",
              "Figure N:"),
    mention(9, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("line", legend="inside", numbers=True, panels=4, layout="2x2"),
    path=S_4, kind="other",
    note="Four dual-axis time series in a 2x2 grid, sub-labelled in the artwork Pic1-Pic4, "
         "1960-2008 on a shared year axis. Each panel repeats its own key INSIDE the frame "
         "just under the Pic label: Consumption/Price in the first three, T&N/C&R in the "
         "fourth. One pasted chart-group screenshot, so the whole row is a single region; it "
         "runs about 1.12 of the text measure and bleeds past both margins. No number is "
         "printed in the prose - the group is introduced only as 'the energy profile of "
         "California'. Its Pic numbering is decoded on page 10 by Table 3."))

B["f2"] = bb(9, 2)
FIGURES.append(figure(
    "f2", cap("Figure 2: energy consumption of different items in California", "Figure N:"),
    mention(9, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("bar", legend="none", numbers=True, panels=1),
    path=S_4, kind="other",
    note="One nine-bar dual-axis panel: five bars over the group caption 'Clean and renewable "
         "energy' and four over 'Traditional and unrenewable energy', divided by colour only. "
         "NO legend - the letters F, HY, GE, WE, PH&SO, C, PE, NG, OT are decoded on page 10 "
         "by Table 3, so this figure cannot be read without a table two pages behind it. "
         "Also 1.13 of the measure. Uncited by number."))

B["f3"] = bb(10, 1)
FIGURES.append(figure(
    "f3", cap("Figure 3: constitution of total energy consumption in California in 2009",
              "Figure N:"),
    mention(10, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("other", legend="outside-right", numbers=True, panels=1, labels=True),
    path=S_4, kind="other",
    note="A flat five-slice pie of 2009 consumption with the state name printed INSIDE the "
         "box as an in-figure title and percentages printed in the slices (39.09, 22.11, "
         "19.72, 19.08, and a 0.00 on a leader line). The five-entry legend sits to the RIGHT "
         "of the pie, outside the region box, and spells the sectors out as full sentences. "
         "The in-figure title is the only above-art text on any exhibit in this paper.",
    other_note="pie chart - the closed family list has no pie entry, so it is recorded as "
               "other; the branch keys are a legend, not a colourbar"),
    )

B["f4"] = bb(11, 2)
FIGURES.append(figure(
    "f4", cap("Figure 4: elasticity coefficient of FTE(left) and CRE(right)", "Figure N:"),
    mention(11, first=11, style=["figure 4"], count=1,
            lead="The calculation results are shown in figure 4.",
            pattern="direct",
            trail="we can intuitively know that generally the dependency between economic "
                  "development and CRE",
            read=2),
    geo("line", legend="inside", numbers=True, panels=2, layout="1x2"),
    path=S_51, kind="result",
    note="Two side-by-side elasticity panels that share one legend repeated at the top "
         "INSIDE each frame - AZ, CA, NM, TX plus the black 'Tendency' fit line - with the "
         "y title 'Elastic Coefficient' on both and different y ranges (0-4 and 0-9). The "
         "right panel is clipped at the right edge, so its last year tick prints as '200'. "
         "The paper's one figure cited by number with a lowercase 'figure 4'. The caption "
         "mislabels TFE as FTE."))

EXCLUDED.append(("p8-r1", bb(8, 1), "not-an-exhibit"))
EXCLUDED.append(("p11-r1", bb(11, 1), "not-an-exhibit"))
EXCLUDED.append(("p12-r1", bb(12, 1), "not-an-exhibit"))

B["t5"] = bb(12, 2)
TABLES.append(table(
    "t5", cap("Table 5: the regression results of Equation 1", "Table N:"),
    mention(12, first=12, style=["Table 5"], count=1,
            lead="From the Table 5, we can see that population has no significant influence",
            pattern="direct",
            trail="While the the economic development and the share of secondary industy "
                  "have significant influence on the energy consumption.",
            read=1),
    grid(9, 9, header=2, numeric=8, txt=1, rule="vertical-rules", merged=True, width="full",
         note="*，**，*** respectively represent the confidence of 10%,5%,1%"),
    path=S_52, kind="model",
    note="The paper's widest numeric grid: seven coefficient rows (ln(ttdp) to Constant) "
         "across four TFE states and four CRE states, under TWO header rows - 'Equation 1' "
         "spans both rows vertically in the stub, TFE and CRE each span four columns. Boxed "
         "with full-height verticals at the stub and group boundaries and no row rules; "
         "significance stars carry the reading. The printed note line under the caption is "
         "the only such note in the paper and it uses fullwidth commas."))

B["f5"] = bb(13, 1)
FIGURES.append(figure(
    "f5", cap("Figure 5: resource distribution of CRE", "Figure N:"),
    mention(13, first=12, style=["Figure 5"], count=2,
            lead="we collect information about the natural environment of the four states, "
                 "which is shown in Figure 5",
            pattern="as-shown-in",
            trail="From Figure 5, we know that the four states differ in the potential of "
                  "CRE production.",
            read=2),
    geo("map-or-plan-view", legend="inside", numbers=False, panels=1, labels=True),
    path=S_52, kind="model",
    note="The paper's one map: a raster basemap of the south-west United States with relief "
         "and city labels, three point symbols (wind turbine, solar starburst, hydro droplet) "
         "and a white legend box INSIDE the artwork at lower left. No scale bar, no "
         "coordinates, no colourbar. It prints at the top of page 13 above the 5.3 heading, "
         "so the record places it in 5.2, where the sentence that introduces it lives on the "
         "previous page - the only exhibit cited a page before it prints."))

B["f6"] = bb(13, 2)
FIGURES.append(figure(
    "f6", cap("Figure 6: evaluation index systerm", "Figure N:"),
    mention(13, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("flowchart-or-schematic", legend="none", numbers=False, panels=1, labels=True),
    path=S_531, kind="model",
    note="A three-level index tree drawn as black line art: one rounded CUP box at the top, "
         "three ellipses (Ep, Epf, Enp) under it, and nine leaf boxes at the foot, every "
         "arrow pointing upward from child to parent. Monochrome, no legend, no numbers. The "
         "caption keeps the paper's typo 'systerm'. It is uncited by number: the sentence "
         "above it names Table 6 instead, so the tree is read as an illustration of the table."))

B["t6"] = bb(14, 1)
TABLES.append(table(
    "t6", cap("Table 6: indexes and their formulas", "Table N:"),
    mention(14, first=13, style=["Table 6"], count=2,
            lead="These indexes and their formulas are detailed in the Table 6.",
            pattern="direct", trail="", read=0),
    grid(10, 4, header=1, numeric=0, txt=4, rule="vertical-rules", merged=True),
    path=S_531, kind="model",
    note="Nine indexes in three vertically merged blocks - Energy performance, Economic "
         "proformance (sic), Environment performance - each block name spanning its three "
         "rows in the stub. Closed box with every internal vertical and horizontal rule "
         "drawn. The Formula column carries real typeset fractions, so that column prints no "
         "units and no decimals. The block header cell of the fourth column is left EMPTY."))

EXCLUDED.append(("p14-r2", bb(14, 2), "not-an-exhibit"))
EXCLUDED.append(("p15-r1", bb(15, 1), "not-an-exhibit"))

B["f7"] = bb(16, 1)
FIGURES.append(figure(
    "f7", cap("Figure 7: the principle of BP neural network", "Figure N:"),
    mention(16, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("flowchart-or-schematic", legend="none", numbers=False, panels=1, labels=True),
    path=S_542, kind="other",
    note="The pseudocode-as-drawing exhibit of the paper: one vertical flow from "
         "Initialization through parameter setting, input and target vectors, hidden and "
         "output values, to the deviation E, then a decision diamond 'Whether the E meets the "
         "requirements?' whose No branch runs through error and gradient boxes and loops back "
         "into the network box, and whose Yes branch ends. Monochrome, no legend, no numbers, "
         "0.66 of the measure. Uncited: section 5.4.2 talks about the network without ever "
         "pointing at its diagram."))
# Pages 17-29: the prose strip, the average-error grid, the fitted and two-scenario
# scatter rows, the prediction grids, then the three appendix plates that repeat the
# same four exhibits per state.

EXCLUDED.append(("p17-r1", bb(17, 1), "not-an-exhibit"))

B["t8"] = bb(18, 1)
TABLES.append(table(
    "t8", cap("Table 8: average fitting error", "Table N:", position="below"),
    mention(18, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    grid(2, 5, header=1, numeric=4, txt=1, rule="booktabs", width="full"),
    path=S_543, kind="other", caption_source="typed-from-crop",
    note="One header row (State / California / Arizona / New Mexico / Texas) over ONE data "
         "row of percentages, three horizontal rules and no vertical anywhere - booktabs, "
         "with the header band shaded. It has no region of its own: the only box on page 18 "
         "is a page-sized prose strip that happens to swallow the grid AND its caption, so "
         "the measured bbox is the strip and the caption is typed from the crop because page "
         "18's text layer loses its whole upper half. The prose introduces it as 'Here are "
         "the results.' and never prints its number."))

B["f8"] = bb(19, 1)
FIGURES.append(figure(
    "f8", cap("Figure 8: the fitting results", "Figure N:"),
    mention(19, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("line", legend="inside", numbers=True, panels=4, layout="2x2"),
    path=S_543, kind="other",
    note="Four 2x2 panels, one per state, each titled 'The fitting figure' inside the "
         "artwork and each carrying its own two-entry key below the plot - Actual value of "
         "AZ / Fitted value of AZ, and so on. Actual and fitted series are joined by markers "
         "over printed years, so it is a line exhibit rather than a scatter of residuals. No "
         "citation by number, no reading sentence: it is the reliability evidence for the "
         "prediction and the prose goes straight on to the two scenarios."))

B["f9"] = bb(19, 3)
FIGURES.append(figure(
    "f9", cap("Figure 9: Scenario one", "Figure N:"),
    mention(19, first=19, style=["figure 9"], count=1,
            lead="As is shown in figure 9, if the change of the three independent variables "
                 "follows",
            pattern="as-shown-in", trail="", read=0),
    geo("scatter", legend="none", numbers=True, panels=1),
    path=S_543, kind="other",
    note="The left half of one printed baseline: a single scatter with a straight fitted "
         "trend line, y axis 0-0.8, year labels along x squeezed until they overlap and are "
         "unreadable. No legend, no title, no panel letter - identity comes only from the "
         "shared caption line. Its box and Figure 10's overlap by 95 per cent in y; the two "
         "crops separate them left (this one) and right, so panel order must be taken from x, "
         "never from the region index."))

B["f10"] = bb(19, 2)
FIGURES.append(figure(
    "f10", cap("Figure 10: Scenario two", "Figure N:"),
    mention(19, first=19, style=["figure 10"], count=1,
            lead="As is shown in figure 10, if the change of the three independent variables "
                 "follow",
            pattern="as-shown-in", trail="", read=0),
    geo("scatter", legend="none", numbers=True, panels=1),
    path=S_543, kind="other",
    note="The right half of the same baseline: a scatter with a smooth fitted curve instead "
         "of a straight line, y axis 0-350. Same squeezed year labels, same absent legend. "
         "The pair is the paper's only two-up comparison printed under ONE caption line, and "
         "each half is its own region."))

B["t9"] = bb(20, 1)
TABLES.append(table(
    "t9", cap("Table 9: the predicting results", "Table N:"),
    mention(20, first=20, style=["table 9"], count=1,
            lead="The results are shown in table 9.",
            pattern="direct", trail="", read=0),
    grid(10, 10, header=2, numeric=8, txt=2, rule="vertical-rules", zebra=True, merged=True,
         decimal=True),
    path=S_61, kind="test",
    note="The paper's densest prediction grid and the only zebra-shaded one: four states by "
         "two years under two spanner headers (Scenario 1 / Scenario 2) over four index "
         "columns each. The state stubs merge across their two year rows and each spanner "
         "merges across four columns; verticals at the stub and scenario boundaries only, no "
         "row rules, and the light grey banding does the row tracking. Values right-aligned "
         "and decimal-consistent per column."))

B["t10"] = bb(20, 2)
TABLES.append(table(
    "t10", cap("Table 10: the predicting error", "Table N:"),
    mention(20, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    grid(3, 5, header=2, numeric=4, txt=1, rule="vertical-rules", merged=True, width="full"),
    path=S_61, kind="test",
    note="The smallest grid in the paper: one spanner row ('The predicting error') merged "
         "across all five columns, a State/California/Arizona/New Mexico/Texas header row, and "
         "one row of percentages. Fully boxed with verticals at every column boundary. Uncited "
         "by number - 'Here are the results.' hands it over, the same formula the paper uses "
         "for Table 8."))

B["f11"] = bb(24, 1)
FIGURES.append(figure(
    "f11", cap("Figure 11: Energy profile of Arizona", "Figure N:"),
    mention(24, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("line", legend="inside", numbers=True, panels=4, layout="2x2"),
    path=app("Appendix A Profiles of Arizona"), kind="appendix",
    note="The Arizona copy of page 9's four-panel row: the same Pic1-Pic4 dual-axis time "
         "series with Consumption/Price keys inside the top of each frame. The appendix does "
         "not redraw anything; it reprints the state chapter that section 4 sent to the back "
         "('those of other states are attached to the appendix')."))

B["f12"] = bb(24, 2)
FIGURES.append(figure(
    "f12", cap("Figure 12: Means of energy consumption in Arizona", "Figure N:"),
    mention(24, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("bar", legend="none", numbers=True, panels=1),
    path=app("Appendix A Profiles of Arizona"), kind="appendix",
    note="The Arizona nine-bar panel under the same two group captions as page 9's Figure 2, "
         "again with NO legend. Colour alone separates clean from traditional, and the letter "
         "keys are decoded only by the Table 13 plate two pages on - except that plate still "
         "points at 'Figure 2 and Figure 3', the California numbers."))

B["f13"] = bb(25, 1)
FIGURES.append(figure(
    "f13", cap("Figure 13: The constitute of total energy consumption in Arizona in 2009",
               "Figure N:"),
    mention(25, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("other", legend="outside-right", numbers=True, panels=1, labels=True),
    path=app("Appendix A Profiles of Arizona"), kind="appendix",
    note="Arizona's pie, identical in construction to page 10's Figure 3: in-figure title, "
         "percentages in the slices with a stray 0.00 on a leader line, five-entry sentence "
         "legend outside the box at the right. The caption's verb 'constitute' is the "
         "appendix's own wording - the body chapter said 'constitution'.",
    other_note="pie chart - no pie entry exists in the closed family list, so it is recorded "
               "as other; the sector keys are a legend, not a colourbar"))

B["t14"] = bb(25, 2)
TABLES.append(table(
    "t14", cap("Table 14: The quantitative change and the rate of change of typical variables",
               "Table N:"),
    mention(25, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    grid(10, 3, header=2, numeric=2, txt=1, rule="vertical-rules", merged=True),
    path=app("Appendix A Profiles of Arizona"), kind="appendix",
    note="Eight variables against quantitative change and rate of change, under a spanner row "
         "'Data from 1960 to 2009' merged across all three columns and a second header row. "
         "Fully boxed with verticals at both column boundaries. Units are printed INSIDE the "
         "cells (Billion Btu, Million dollars) rather than in the header, and the values are "
         "centred rather than decimal-aligned - which is why the GDP rate of change prints as "
         "a bare 6.736912662 where every other row is a percentage."))
# Pages 26-29: the New Mexico and Texas plates. Appendix C's heading prints at the foot
# of page 26, four pages before the figures it governs.

B["f14"] = bb(26, 1)
FIGURES.append(figure(
    "f14", cap("Figure 14: energy profile of New Mexico", "Figure N:"),
    mention(26, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("line", legend="inside", numbers=True, panels=4, layout="2x2"),
    path=app("Appendix B Profile of New Mexico"), kind="appendix",
    note="New Mexico's four-panel dual-axis row, the third printing of the same Pic1-Pic4 "
         "template; only the data change. Its appendix heading prints at the top of the same "
         "page, but the heading is not detected as a heading by the extractor, so the path "
         "carries an unnumbered label."))

B["f15"] = bb(26, 2)
FIGURES.append(figure(
    "f15", cap("Figure 15: means of energy consumption in New Mexico", "Figure N:"),
    mention(26, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("bar", legend="none", numbers=True, panels=1),
    path=app("Appendix B Profile of New Mexico"), kind="appendix",
    note="New Mexico's nine-bar panel, still with no legend: colour alone separates the two "
         "groups, exactly as in Arizona. Texas alone gets a key (Figure 18), so the same "
         "encoding is explained on one plate and left implicit on two."))

B["f16"] = bb(27, 1)
FIGURES.append(figure(
    "f16", cap("Figure 16: the constitute of total energy consumption in New Mexico in 2009",
               "Figure N:"),
    mention(27, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("other", legend="outside-right", numbers=True, panels=1, labels=True),
    path=app("Appendix B Profile of New Mexico"), kind="appendix",
    note="New Mexico's pie, fourth printing of the pie template: in-figure state title, "
         "percentages in the slices, stray 0.00 on a leader line, sentence legend outside the "
         "box at the right.",
    other_note="pie chart - no pie entry exists in the closed family list, so it is recorded "
               "as other; the sector keys are a legend, not a colourbar"))

B["t16"] = bb(27, 2)
TABLES.append(table(
    "t16", cap("Table 16: The quantitative change and the rate of change of typical variables",
               "Table N:", position="above"),
    mention(27, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    grid(10, 3, header=2, numeric=2, txt=1, rule="vertical-rules", merged=True),
    path=app("Appendix B Profile of New Mexico"), kind="appendix",
    note="New Mexico's variable-change grid, structurally the twin of Table 14: two header "
         "rows with a 'Data from 1960 to 2009' spanner, full box, units in the cells. It is "
         "the paper's ONLY exhibit captioned ABOVE its artwork; every other caption, on all "
         "nineteen figures and the other nine grids, prints below. Its numbers are the "
         "California figures re-printed - the same 156.56% and 873.31% that appear in Table 4."))

B["f17"] = bb(28, 1)
FIGURES.append(figure(
    "f17", cap("Figure 17: Energy profile of Texas", "Figure N:"),
    mention(28, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("line", legend="inside", numbers=True, panels=4, layout="2x2"),
    path=app("Appendix C Profiles of Texas"), kind="appendix",
    note="Texas's four-panel row, fourth printing of the Pic template. It prints on page 28 "
         "but 'Appendix C Profiles of Texas' is printed at the FOOT of page 26, above the New "
         "Mexico plate, so the heading and its exhibits are separated by a whole page - the "
         "path is assigned from the printed heading, not from page order."))

B["f18"] = bb(28, 2)
FIGURES.append(figure(
    "f18", cap("Figure 18: Means of energy consumption in Texas", "Figure N:"),
    mention(28, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("bar", legend="inside", numbers=True, panels=1, labels=False),
    path=app("Appendix C Profiles of Texas"), kind="appendix",
    note="Texas's nine-bar panel and the ONLY one of the three that carries a legend: a "
         "two-entry key inside the frame at upper left, 'The consumption of CRE' and 'The "
         "consumption of TFE'. Arizona's and New Mexico's print the same chart with no key at "
         "all, so the appendix is internally inconsistent about whether colour needs "
         "explaining."))

B["f19"] = bb(29, 1)
FIGURES.append(figure(
    "f19", cap("Figure 19: The constitute of total energy consumption in Texas in 2009",
               "Figure N:"),
    mention(29, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("other", legend="outside-right", numbers=True, panels=1, labels=True),
    path=app("Appendix C Profiles of Texas"), kind="appendix",
    note="Texas's pie, fifth and last printing of the pie template on this paper. Same "
         "percentages-in-slices construction, same stray 0.00, same sentence legend to the "
         "right of the box.",
    other_note="pie chart - no pie entry exists in the closed family list, so it is recorded "
               "as other; the sector keys are a legend, not a colourbar"))

B["t18"] = bb(29, 2)
TABLES.append(table(
    "t18", cap("Table 18: The quantitative change and the rate of change of typical variables",
               "Table N:"),
    mention(29, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    grid(9, 3, header=1, numeric=2, txt=1, rule="vertical-rules"),
    path=app("Appendix C Profiles of Texas"), kind="appendix",
    note="Texas's variable-change grid and the odd one out among the three: ONE header row "
         "with no 'Data from 1960 to 2009' spanner, so it is nine rows against its siblings' "
         "ten, and its body is a genuine Texas table rather than a reprint. Same full box, "
         "same units-in-cells, same centred rather than decimal-aligned values."))
# What 29 exhibits and 6 excluded strips generalise to.

RULES: list[str] = [
    "[caption.position] All 19 figures and 9 of the 10 recorded grids are captioned BELOW "
    "their artwork; the single exception is Table 16, captioned above. The side is a house "
    "habit here, not a choice made per exhibit kind - this paper captions tables the way it "
    "captions figures.",

    "[caption.numbering] Every recorded caption is the colon form 'Figure N:' or 'Table N:' "
    "with the colon attached to the number and no period after it; the caption body is then "
    "a lower-case noun phrase that does not repeat the word Figure or Table.",

    "[caption.words] Captions stay at 2 to 8 words except the three appendix "
    "variable-change grids (12 words each), which grow only because they must name both the "
    "quantity and its two measures.",

    "[caption.voice] Twenty-nine of twenty-nine captions are verbless noun phrases: not one "
    "states a conclusion, and not one carries a unit or a condition - the conditions live in "
    "the table note (Table 5) or in the cells (Tables 14, 16, 18), never in the caption.",

    "[table.rule_style] Eight of the ten grids are closed boxes with full-height verticals at "
    "every column boundary; Table 2 is the one plain frame with side rules and no internal "
    "vertical; Table 8 is the only booktabs grid - horizontals only.",

    "[table.zebra] Exactly one grid shades alternate rows (Table 9, the two-scenario "
    "prediction block), and it is also the widest. Every other grid tracks rows with the stub "
    "column or with rules.",

    "[table.merged_cells] Six grids merge cells and every merge is a header merge: a spanner "
    "(TFE / CRE, Scenario 1 / Scenario 2, Data from 1960 to 2009, The predicting error) or a "
    "stub that spans the three rows of an index block (Table 6).",

    "[table.header_rows] Five grids carry two header rows and all five are two-block "
    "constructions - a group spanner over column names (Tables 5, 9, 10, 14, 16); the other "
    "five carry one.",

    "[table.decimal_aligned] Only Table 9 aligns decimals. Every other grid centres its "
    "numbers, which is why Table 14's GDP rate of change prints as a bare 6.736912662 among "
    "percentages.",

    "[table.units_in_header] No grid puts a unit in its header. The three appendix grids put "
    "the unit inside each cell ('1116104.735(Billion Btu)'), and no other grid carries a unit "
    "at all.",

    "[table.width] Eight of the ten grids run 0.83 to 1.01 of the 424 pt measure and two "
    "overhang it slightly; there is no half-width insert and no column-width grid in the "
    "paper, however few columns a claim needs.",

    "[table.diagonal_header] No grid has a diagonal header cell, and no grid continues across "
    "a page break - the one split candidate is Table 3's plate, which is a key rather than a "
    "table.",

    "[table.note_sentence] Exactly one grid carries a printed note under its caption, and it "
    "is the significance key for Table 5's stars; the appendix grids instead bury their unit "
    "and their date range inside the cells and the spanner.",

    "[geometry.family] Section 4 and the appendix plates are a fixed quartet per state - a "
    "2x2 line row, a grouped bar, a pie and a variable-change grid - so family is chosen by "
    "the state chapter template, not per finding: 6 line exhibits, 4 bar, 4 pies, 2 scatter, "
    "1 map, 2 schematics.",

    "[geometry.panel_count] The 2x2 panel row is the paper's standard exhibit (5 of 19 "
    "figures) and always holds one time series per state or per quantity; every other figure "
    "is single-panel, and the only two-up row is the Figure 9 / Figure 10 pair.",

    "[geometry.legend] Legends are placed where the reader needs them and omitted where a "
    "table two pages back decodes the letters: 8 inside the frame, 7 absent, 4 outside-right "
    "on the pies - and the two bar charts that print no key are the same chart as the one bar "
    "chart that prints one.",

    "[geometry.three_d] Nothing in the paper is three-dimensional; every one of the 35 "
    "regions was cropped and read, and no axis, projection or depth cue appears in any of "
    "them.",

    "[geometry.colorbar] No exhibit carries a colourbar. Colour is used only to separate "
    "groups and sectors, never to encode a value, so no ramp is decoded anywhere in this "
    "paper.",

    "[mention.first_page] Only 7 of the 29 exhibits are ever cited by number, and they are "
    "the mid-paper results (the elasticity pair, the resource map, the two scenarios, the "
    "regression grid, the index grid, the prediction grid). Every appendix exhibit and every "
    "chart in section 4 stands uncited.",

    "[mention.lead_pattern] The pointer is either a flat results sentence ('The results are "
    "shown in table 9.', 'The calculation results are shown in figure 4.') or 'as is shown in "
    "figure N'; the number is spelled 'Figure' capitalised except three times, where the "
    "paper writes 'figure 4', 'figure 9' and 'table 7' in lower case.",

    "[mention.lead_pages] Citation lands on the exhibit's own page in six of the seven cited "
    "cases; the exception is Figure 5, pointed at from the foot of page 12 and printed at the "
    "top of page 13.",

    "[mention.read_sentences] A cited exhibit gets a reading sentence and an uncited one gets "
    "none - the appendix plates and the four California charts are presented as evidence with "
    "no sentence telling the reader what to see.",

    "[place.section_kind] Twelve of the 29 exhibits sit in the appendix, 9 in 'other' "
    "sections, 4 in model sections, 2 in the reliability test, 1 in results and 1 in the "
    "symbols list - the body carries fewer exhibits than the plates do.",

    "[place.solo_page] No exhibit owns a page: even the two figure-only pages (9 and 28) hold "
    "two exhibits each, and every grid shares its page with prose.",

    "[place.page_zone] Exhibits sit where the section needs them - 11 in the top third of a "
    "page, 10 in the middle, 8 at the bottom - so page zone does not separate figures from "
    "tables here.",

    "[place.area_frac] Area is an artefact of how the artwork was cut: the pies and bars tile "
    "into 0.10-0.16 boxes, the 2x2 rows into 0.23, and the largest single number (0.555) is "
    "the prose strip on page 17 that is not an exhibit at all.",
]

NOTE = (
    "Coverage. Eighteen tables are printed with captions; ten are recorded. The eight gaps "
    "are declared, not invented: Table 3 (p10), Table 13 (p25), Table 15 (p27) and Table 17 "
    "(p29) are the same 'cutline' key plate four times over - a boxless four-column glossary "
    "under two grey banner rows reading 'Figure 2 :' / 'Figure 3 :' (and, on the appendix "
    "plates, Figures 12/13, 15/16, 18/19), all four still carrying the stale cross-reference "
    "'in Figure 2 and Figure 3' and the misspelling 'Fuel enthanol'; Table 4 (p10), Table 12 "
    "(p21) and the unboxed sweep of Table 11 (p20, the k-sensitivity grid) are native "
    "text-layer tables the region pass never boxes; and Table 7 (p15, PCA scores) prints "
    "directly under the page-15 raster, above the box's lower edge. Table 8 does have a "
    "measured region but only incidentally: page 18's single box is a page-sized prose strip "
    "that swallows the grid AND its caption, so the reported caption had to be typed from the "
    "crop - page 18's text layer loses its entire upper half, including equations (17)-(19) "
    "and the 5.4.3 heading.\n\n"
    "Region count is not exhibit count, and on this paper the surplus runs the other way from "
    "the census's usual failure. Six of the 35 regions hold no exhibit: five are display "
    "mathematics or pasted prose (equation (1) p8, equation (2) p11, the three-equation block "
    "(3) p12, the standardisation block (4) p14, and the fifteen-line prose-plus-equations "
    "raster on p15), and the sixth is page 17, which is one 0.555-area strip of prose and "
    "equations (11)-(16) that the detector reports as a single region. So 35 regions hold 29 "
    "exhibits, and no region holds two printed exhibits except the ambiguous page-19 pair: "
    "those two boxes share 95 per cent of their y extent and only x separates Figure 9 (left) "
    "from Figure 10 (right), so panel order must be read from the crop, never from the region "
    "index.\n\n"
    "The paper's apparatus is broken in three specific ways that a later pass must not "
    "'fix'. First, the caption collision: Tables 3, 13, 15 and 17 print banner rows that "
    "reuse figure numbers already spent by real captions on pages 9, 10, 24, 25, 27, 28 and "
    "29, so a naive caption scan finds 'Figure 2', 'Figure 3', 'Figure 12', 'Figure 13', "
    "'Figure 15', 'Figure 16', 'Figure 18' and 'Figure 19' twice each. Second, the misplaced "
    "heading: 'Appendix C Profiles of Texas' prints at the FOOT of page 26, above the New "
    "Mexico plate, while its four exhibits print on pages 28 and 29 - the path is assigned "
    "from the printed heading, not from page order. Third, the reprint: Table 16's body is "
    "California's Table 4 numbers re-printed under a New Mexico caption (156.56% and 873.31% "
    "appear in both), and Table 18 is the only one of the three appendix grids that drops the "
    "'Data from 1960 to 2009' spanner row, which is why it has nine rows where its siblings "
    "have ten."
)
ALL: list[dict] = FIGURES + TABLES
_order = sorted(ALL, key=lambda it: (it["page"],
                                     round((it["bbox"][1] + it["bbox"][3]) / 2),
                                     it["bbox"][0]))
_page_seen: dict[int, int] = {}
for _i, _it in enumerate(_order, 1):
    _it["place"]["doc_order"] = _i
    _pg = _it["page"]
    _page_seen[_pg] = _page_seen.get(_pg, 0) + 1
    _it["place"]["page_order"] = _page_seen[_pg]

_claimed = {(it["page"], tuple(it["bbox"])) for it in ALL}
_claimed |= {(p, tuple(b)) for _k, (p, b), _r in EXCLUDED}
assert _claimed == MEASURED, (
    f"unclaimed {sorted(MEASURED - _claimed)} extra {sorted(_claimed - MEASURED)}")
assert len(ALL) + len(EXCLUDED) == len(MEASURED) == 35, (
    len(ALL), len(EXCLUDED), len(MEASURED))

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"key": k, "page": p, "bbox": b, "reason": r} for k, (p, b), r in EXCLUDED
    ],
    "rules": RULES,
    "note": NOTE,
}


def main() -> None:
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"figures {len(FIGURES)} tables {len(TABLES)} excluded {len(EXCLUDED)} "
          f"-> {out.name}")
    fam: dict[str, int] = {}
    for it in FIGURES:
        fam[it["geometry"]["family"]] = fam.get(it["geometry"]["family"], 0) + 1
    print("families", dict(sorted(fam.items())))
    legs: dict[str, int] = {}
    for it in FIGURES:
        legs[it["geometry"]["legend"]] = legs.get(it["geometry"]["legend"], 0) + 1
    print("legends", dict(sorted(legs.items())))
    pos = {"figure": {}, "table": {}}
    for it in FIGURES:
        pos["figure"][it["caption"]["position"]] = pos["figure"].get(
            it["caption"]["position"], 0) + 1
    for t in TABLES:
        pos["table"][t["caption"]["position"]] = pos["table"].get(
            t["caption"]["position"], 0) + 1
    print("caption side", pos)
    rules: dict[str, int] = {}
    for t in TABLES:
        rules[t["table"]["rule_style"]] = rules.get(t["table"]["rule_style"], 0) + 1
    print("rule styles", rules)
    widths = sorted({round(t["bbox"][2] - t["bbox"][0], 1) for t in TABLES})
    print("table widths pt", widths)
    print("cited exhibits", sum(1 for it in FIGURES if it["mention"]["first_page"]))
    print("numbered captions",
          sum(1 for it in FIGURES if it["caption"]["numbering"] != "none"))
    kinds: dict[str, int] = {}
    for it in ALL:
        kinds[it["place"]["section_kind"]] = kinds.get(it["place"]["section_kind"], 0) + 1
    print("section kinds", dict(sorted(kinds.items())))


if __name__ == "__main__":
    main()
