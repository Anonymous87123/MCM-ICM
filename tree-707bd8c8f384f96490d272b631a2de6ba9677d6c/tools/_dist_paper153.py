"""Hand pass for P-C-2018-72969-f2349d15 (2018 MCM C, team 72969, "CAFE:
Characterization, Analysis, Forecasting, and Evaluation of Energy Profile": a
Gaussian-process characterisation of a 20-item state energy profile, a similarity
study, a TOPSIS evaluation, an ARMA-GPR hybrid forecast, a target-setting LP and
a memo).

30 pages, 57 measured regions on 21 of them. The last five pages are three
MATLAB appendix listings, which the detector boxes as tables because every glyph
run measures like a cell; they are excluded. Pages 26-30 carry no exhibit.

Usage: python -I tools/_dist_paper153.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2018-72969-f2349d15"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
REG = {(pg["page"], i): list(r["bbox"])
       for pg in LAYOUT["pages"] for i, r in enumerate(pg["regions"], 1)}
MEASURED = {(p, tuple(b)) for (p, _), b in REG.items()}

# Headings the extractor cannot see (pasted inside raster screenshots) and the
# appendix, which the paper never numbers, are recorded under this prefix.
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
    if caption["position"] == "below":
        caption = dict(caption, position="above")
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


def uncap(position: str = "above") -> dict:
    """An exhibit the paper prints with no caption line of its own."""
    return cap("", "none", position=position)


FIGURES: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[tuple[str, tuple[int, list[float]], str]] = []
B: dict[str, tuple[int, list[float]]] = {}

S_1 = ["1 Introduction"]
S_2 = ["2 Assumptions"]
S_3 = ["3 Abbreviation and Definitions"]
S_4 = ["4 CAFE: Characterization, Analysis, Forecasting, and Evalu-"]
S_41 = S_4 + ["4.1 Energy Profile Formulation"]
S_42 = S_4 + ["4.2 Energy Profile Characterization and Analysis"]
S_421 = S_42 + ["4.2.1 GPR model: Evolution of Energy Profile"]
S_422 = S_42 + ["4.2.2 Similarity Analysis of Energy Profile"]
S_43 = S_4 + ["4.3 Influential Factors of Similarities"]
S_44 = S_4 + ["4.4 Energy Profile Evaluation"]
S_45 = S_4 + ["4.5 Energy Profile Prediction"]
S_5 = ["5 Targets and Actions for Interstate Energy Compact"]
S_51 = S_5 + ["5.1 Targets: Total Renewable Consumption Based Optimization"]
S_52 = S_5 + ["5.2 Actions: Motivating Renewable Energy Use in NM, TX, and AZ"]
S_6 = ["6 Sensitivity Analysis"]
S_7 = ["7 Strengths and Weaknesses"]


def app(title: str) -> list[str]:
    return [UNCAP + "Appendices", UNCAP + title]
# Pages 4-13: the framework schematic, the abbreviation and taxonomy exhibits, the
# GPR panel rows, the similarity heat maps, the four scatter fits, and the five pasted
# text/equation strips that the detector boxes but which carry no exhibit.

B["f1"] = bb(4, 1)
FIGURES.append(figure(
    "f1", cap("Figure 1: Framework of CAFE (Characterization, Analysis, Forecasting, and "
              "Evaluation of Energy Profile)", "Figure N:"),
    mention(4, first=4, style=["Figure 1", "Fig. 1"], count=2,
            lead="The framework of CAFE is shown in Figure 1.",
            pattern="as-shown-in",
            trail="CAFE framework in Fig. 1 can be summarized as the following steps:",
            read=2),
    geo("flowchart-or-schematic", legend="none", numbers=False, panels=1, layout="1",
        labels=True),
    path=S_1, kind="introduction",
    note="The paper's only framework diagram and the only exhibit in an unnumbered-block "
         "position: a left-to-right pipeline of five stages, the middle four of each stage "
         "hanging beneath a solid grey caption bar, closed by a green 'Target and Action' "
         "box. Drawn with vector boxes and connectors, every label printed in place, no "
         "legend, no number, no scale. It is the one exhibit that pre-announces the rest of "
         "the paper, and every later section maps onto a stage of it."))

B["t1"] = bb(6, 1)
TABLES.append(table(
    "t1", cap("Table 1: Abbreviation of Relevant Terms", "Table N:"),
    mention(6, first=6, style=["Table 1"], count=1,
            lead="we define a series of abbreviations for some notions concerning energy "
                 "profile in Table 1",
            pattern="direct", trail="", read=0),
    grid(21, 2, header=1, numeric=0, txt=2, rule="booktabs"),
    path=S_3, kind="symbols",
    note="The paper's only nomenclature table: bold Abbreviation / Full Name heads, one "
         "heavy rule under the header, a hairline between every row, one heavy rule at the "
         "foot - booktabs with row rules, which no later table repeats. Twenty rows, no "
         "numbers at all, and the two long entries run their words together where the "
         "column is tight ('Entropy bySource', 'byEnd-useSector'). The detector also boxes "
         "the row hairlines so tightly that the lower half of the glyphs is struck through "
         "in the render."))

B["f2"] = bb(7, 1)
FIGURES.append(figure(
    "f2", cap("Figure 2: The Energy Profile of a State", "Figure N:"),
    mention(7, first=8, style=["Figure 2"], count=2,
            lead="In Figure 2, we group these items into four sub-classes based on whether "
                 "the energy is renewable and supply or usage of the energy.",
            pattern="parenthetical",
            trail="Moreover, these items can be classified into four categories with "
                  "different physical dimensions: entropy, volume, ratio, and volume per "
                  "capita.",
            read=2),
    geo("flowchart-or-schematic", legend="outside-right", numbers=False, panels=1, layout="1",
        labels=True),
    path=S_41, kind="model",
    note="A taxonomy matrix rather than a plot: two rows (Supply, Usage) crossed with two "
         "columns (Unrenewable, Renewable), each cell a stack of grey rounded item boxes, "
         "with a solid green frame around the whole grid marking the energy profile. The "
         "four dimensions - entropy, volume, ratio, volume per capita - are keyed by a grey "
         "swatch legend printed to the RIGHT of the grid, outside the region box and outside "
         "every other box on the page, so the region under-claims its own artwork. Two green "
         "italic callout frames carry the ratio definitions and are separate regions, "
         "recorded as fragments. Cited one page after it prints."))

EXCLUDED.append(("p7-r2", bb(7, 2), "fragment-of-other"))
EXCLUDED.append(("p7-r3", bb(7, 3), "fragment-of-other"))

B["f3"] = bb(8, 2)
FIGURES.append(figure(
    "f3", cap("Figure 3: Three typical time series of longitudinal energy profile data.",
              "Figure N:"),
    mention(8, first=8, style=["Fig. 3", "Fig. 3(a)", "Fig. 3(b)", "Fig. 3(c)"], count=4,
            lead="which present different shapes and trends, as shown in Fig. 3",
            pattern="as-shown-in",
            trail="GPR model makes a probabilistic prediction of outputs with confidence "
                  "intervals",
            read=2),
    geo("scatter", legend="none", numbers=True, panels=3, layout="1x3"),
    path=S_421, kind="model",
    note="The paper's raw-data exhibit: three side-by-side scatter strips of hollow red "
         "rings with no fitted line, RED / RE / RCES of Arizona, Time on a shared 1960-2010 "
         "x axis but independent y scales. Sub-captions (a)(b)(c) sit BELOW each panel and "
         "the main caption below the sub-captions, so the exhibit carries two caption "
         "levels. Panels (a) and (b) are pasted bitmaps while (c) is native vector with tiny "
         "pasted markers - one figure, two rendering technologies. Anchored on the left "
         "panel; the other two are separate regions recorded as fragments."))

EXCLUDED.append(("p8-r1", bb(8, 1), "fragment-of-other"))
EXCLUDED.append(("p8-r3", bb(8, 3), "fragment-of-other"))
EXCLUDED.append(("p9-r1", bb(9, 1), "not-an-exhibit"))

B["f4"] = bb(10, 1)
FIGURES.append(figure(
    "f4", cap("Figure 4: GPR curve of three typical time series", "Figure N:"),
    mention(10, first=9, style=["Figure 4"], count=2,
            lead="By adopting GPR, we fit the time series in Figure 3 as Figure 4.",
            pattern="direct",
            trail="The gap surrounded by the upper and lower confident lines is called "
                  "confidence interval.",
            read=3),
    geo("line", legend="inside", numbers=True, panels=3, layout="1x3"),
    path=S_421, kind="model",
    note="The fitted counterpart of Figure 3: same three Arizona items, now with a black "
         "regression curve and a pink 95% confidence band over the red history. Each panel "
         "repeats a three-entry unboxed legend at upper left INSIDE the axes, which is why "
         "this figure, unlike Figure 3, needs no caption text to name its elements. Panel "
         "(c) again comes from a different tool and carries a blue plot frame. The other two "
         "panels are separate regions, recorded as fragments."))

EXCLUDED.append(("p10-r2", bb(10, 2), "fragment-of-other"))
EXCLUDED.append(("p10-r3", bb(10, 3), "fragment-of-other"))

B["t3"] = bb(10, 4)
TABLES.append(table(
    "t3", cap("Table 3: GPR regression results for energy profiles of Arizona (1960-2009) "
              "(The arrow direc- tions represent the basic evolving trends while L and S is "
              "the abbreviation of large and small respectively)", "Table N:"),
    mention(10, first=10, style=["Table 3"], count=1,
            lead="the regression parameters of AZ in Table 3",
            pattern="direct", trail="", read=0),
    grid(16, 11, header=2, numeric=10, txt=1, rule="booktabs"),
    path=S_421, kind="model",
    note="The densest grid in the paper: two stacked blocks of ten items each, the stub "
         "column carrying beta / Trend / alpha / Fluctuation / sigma-squared / Noise / MAPE, "
         "the second block's ten item names serving as its own header row - hence two header "
         "rows over one grid. The Trend and Fluctuation rows hold arrows and L/S letters "
         "rather than numbers, so the numeric columns are the remaining four. The caption is "
         "three lines, the longest in the paper, and it carries the two conditions that make "
         "the letters readable; it breaks the word 'directions' across a hyphen at the line "
         "end, so the verbatim quote preserves 'direc- tions'."))

B["f5"] = bb(11, 1)
FIGURES.append(figure(
    "f5", cap("Figure 5: Evolution of Energy Profile for AZ (the placing order is the same "
              "as Table 3)", "Figure N:"),
    mention(11, first=10, style=["Fig. 5"], count=1,
            lead="and the corresponding regression curve in Fig. 5",
            pattern="direct", trail="", read=0),
    geo("line", legend="none", numbers=False, panels=20, layout="2x10"),
    path=S_421, kind="model",
    note="Small multiples at their most extreme: a 2x10 grid of twenty equal line panels, "
         "one per item, with NO axis ticks, NO axis titles, NO panel letters and NO grid - "
         "the only orientation is the caption's promise that the order matches Table 3. "
         "Every panel is pasted as one strip, so the whole grid is a single region. The only "
         "exhibit in the paper whose reader must hold a table open beside it."))

EXCLUDED.append(("p11-r2", bb(11, 2), "not-an-exhibit"))
EXCLUDED.append(("p12-r1", bb(12, 1), "not-an-exhibit"))

B["f6"] = bb(12, 2)
FIGURES.append(figure(
    "f6", cap("Figure 6: Heat map for GRC and KRCC", "Figure N:"),
    mention(12, first=None, style=[], count=0, lead="", pattern="none", trail="", read=0),
    geo("heatmap-or-contour", legend="none", numbers=True, colorbar=True, panels=2,
        layout="1x2"),
    path=S_422, kind="model",
    note="Two 4x4 state-pair matrices, GRC then KRCC, AZ/CA/NM/TX on both axes, each with "
         "a vertical colourbar at its right edge - the only colourbars in the paper, and the "
         "only exhibits where colour rather than position carries the value. The two ramps "
         "differ on purpose: sequential blue for the 0.64-0.96 GRC, diverging red-blue "
         "through zero for the -0.5 to 0.75 KRCC. Identity comes from the italic sub-captions "
         "'(a)GRC' and '(b)KRCC' sharing one line above the main caption. The paper never "
         "cites this figure by number - its only predecessor sentence names IKRCC, not the "
         "figure. Anchored on the left map; the right one is a fragment. Table 2 on page 7 "
         "and Table 7 on page 20 are printed with captions but covered by no region: this "
         "paper's two declared coverage gaps."))

EXCLUDED.append(("p12-r3", bb(12, 3), "fragment-of-other"))
EXCLUDED.append(("p13-r1", bb(13, 1), "not-an-exhibit"))

B["f7"] = bb(13, 3)
FIGURES.append(figure(
    "f7", cap("Figure 7: Factor Similarity v.s. IGRC", "Figure N:"),
    mention(13, first=13, style=["Figure 7"], count=1,
            lead="In Figure 7, we plot the factor similarity v.s. IGRC",
            pattern="direct",
            trail="As we can see, the scattered points appear to have a consistent trend, "
                  "which indicates that the factor similarity is related to IGRC.",
            read=2),
    geo("scatter", legend="none", numbers=True, panels=4, layout="2x2"),
    path=S_43, kind="model",
    note="Four scatter panels in a 2x2 grid, one per influential factor - Area, Temperature, "
         "Population, GDP - each 12 state-pair points under a linear fit with a pale blue "
         "band that the figure never explains: no legend anywhere, so the band's meaning is "
         "left to the prose. All four repeat the same 'IGRC' y title. The region list is in "
         "row-major order by x only, so (a) is r3 and (b) is r2; sorting by region index "
         "would scramble the panels. Anchored on panel (a); the other three are fragments."))

EXCLUDED.append(("p13-r2", bb(13, 2), "fragment-of-other"))
EXCLUDED.append(("p13-r4", bb(13, 4), "fragment-of-other"))
EXCLUDED.append(("p13-r5", bb(13, 5), "fragment-of-other"))
# Pages 14-20: four native grids, the prediction figures and their panel rows, the
# hybrid-model schematic, the radar row, and the nine pasted equation screenshots.

B["t4"] = bb(14, 1)
TABLES.append(table(
    "t4", cap("Table 4: Pearson Correlation Coefficient and Partial Relational "
              "Coefficient.", "Table N:"),
    mention(14, first=14, style=["Table 4"], count=1,
            lead="Table 4 shows the PCC and PRC between influential factors and IKRCC",
            pattern="direct", trail="", read=0),
    grid(6, 5, header=2, numeric=4, txt=1, rule="booktabs"),
    path=S_44, kind="result",
    note="Two stacked blocks in one grid: four factors over Area / Water Percentage / "
         "Altitude / Rainfall, then a second header row over Temperature / Population / GDP "
         "/ GDP Per Capita, with PCC and PRC rows under each. The second header row is why "
         "this is the paper's only two-header grid. Horizontal rules only, values at two "
         "decimals but centred rather than decimal-aligned, so minus signs hang out to the "
         "left of the column edge."))

B["t5"] = bb(14, 2)
TABLES.append(table(
    "t5", cap("Table 5: Criteria for Evaluating Energy Profile", "Table N:"),
    mention(14, first=14, style=["Table 5"], count=1,
            lead="measure how good a profile is in regards to renewable energy use, list in "
                 "detail in Table 5",
            pattern="direct", trail="", read=0),
    grid(8, 3, header=1, numeric=2, txt=1, rule="booktabs", width="half"),
    path=S_44, kind="result",
    note="Seven criteria, one per row, each with a significance phrase and its entropy "
         "weight - a reading table rather than a data dump. Booktabs, no vertical rule, no "
         "shading, weights at three decimals."))

B["t6"] = bb(15, 2)
TABLES.append(table(
    "t6", cap("Table 6: Evaluation Results of Renewable Energy Usage for Four States",
              "Table N:"),
    mention(15, first=15, style=["Table 6"], count=1,
            lead="The evaluation results are presented in Table 6",
            pattern="direct", trail="", read=0),
    grid(5, 9, header=1, numeric=8, txt=1, rule="booktabs"),
    path=S_44, kind="result",
    note="Eight criteria columns plus an unlabelled state stub, one row per state, the last "
         "column the TOPSIS score. Mixed precision - some cells 1 decimal place, some 3 - so "
         "alignment holds within a column, not across the table. No vertical rule, no zebra, "
         "no merged cells, no unit anywhere."))

B["f8"] = bb(16, 1)
FIGURES.append(figure(
    "f8", cap("Figure 8: GPR-Based Energy Profile Prediction of Arizona."),
    mention(16, first=15, style=["Figure 8", "Figure 8(b)"], count=2,
            lead="Following the GPR model in profile characterization (Section 4.1), we "
                 "first make prediction by GPR, results of which are presented in Figure 8.",
            pattern="direct",
            trail="GPR synthesizes all the historical data, and thus drags down the sudden "
                  "increase after 2009.",
            read=2),
    geo("line", legend="inside", numbers=True, panels=3, layout="1x3"),
    path=S_45, kind="result",
    note="Three panels in one row, each the same item as the p8/p10 rows but now carried to "
         "2050: filled 95% confidence band, red regression curve, blue markers for history "
         "and a blue segment for the prediction. Every panel repeats the same boxed "
         "four-entry legend at upper left and every panel has its own y scale, so the three "
         "are not comparable by eye. The left panel's y title reads 'Renewable Expendirture' "
         "- the misspelling is in the artwork. Panels two and three are separate regions, "
         "recorded as fragments of this figure."))

EXCLUDED.append(("p15-r1", bb(15, 1), "not-an-exhibit"))
EXCLUDED.append(("p16-r2", bb(16, 2), "fragment-of-other"))
EXCLUDED.append(("p16-r3", bb(16, 3), "fragment-of-other"))
EXCLUDED.append(("p16-r4", bb(16, 4), "not-an-exhibit"))

B["f9"] = bb(16, 5)
FIGURES.append(figure(
    "f9", cap("Figure 9: ARMA-GPR Hybrid Model in short-term and long-term prediction"),
    mention(16, first=17, style=["Figure 9"], count=1,
            lead="An intuitive example is illustrated in Figure 9.",
            pattern="as-shown-in", trail="", read=0),
    geo("flowchart-or-schematic", legend="none", numbers=False, panels=1, layout="1"),
    path=S_45, kind="model",
    note="A mechanism diagram rather than a plot: four rows of small square cells on a time "
         "axis, a dashed green 'GPR Window' enclosure over the first two rows, a dashed "
         "yellow 'GPR Prediction(constant)' box over the last two, rose dotted boxes marking "
         "the ARMA sliding windows, and coloured span arrows labelling the four regimes "
         "LTP/STP history and future. Every label is printed in place, so there is no legend "
         "box, no axis scale and no number anywhere on the artwork."))

EXCLUDED.append(("p17-r1", bb(17, 1), "not-an-exhibit"))

B["f10"] = bb(18, 3)
FIGURES.append(figure(
    "f10", cap("Figure 10: ARMA-GPR-Based Energy Profile Prediction of Arizona."),
    mention(18, first=17, style=["Fig. 10"], count=1,
            lead="We plot the prediction results of ARMA-GPR model in Fig. 10.",
            pattern="direct",
            trail="With the time going by, the ARMA-GPR predicted value inclines to "
                  "converge to the GPR predicted value, which results from the "
                  "time-decaying weight.",
            read=3),
    geo("line", legend="inside", numbers=True, panels=3, layout="1x3"),
    path=S_45, kind="result",
    note="The same three Arizona items as Figure 8, now overlaying GPR and ARMA-GPR: two "
         "confidence bands, four curves and two sets of markers, which is why the boxed "
         "legend at upper left grew from four entries to seven. The three panels are stored "
         "right to left in the region list - the left panel is the LAST region on the page - "
         "so any left-to-right reading must sort by x, not by region index. The other two "
         "panels are recorded as fragments."))

EXCLUDED.append(("p18-r1", bb(18, 1), "fragment-of-other"))
EXCLUDED.append(("p18-r2", bb(18, 2), "fragment-of-other"))
EXCLUDED.append(("p18-r4", bb(18, 4), "not-an-exhibit"))
EXCLUDED.append(("p19-r1", bb(19, 1), "not-an-exhibit"))
EXCLUDED.append(("p19-r2", bb(19, 2), "not-an-exhibit"))

B["f11"] = bb(20, 1)
FIGURES.append(figure(
    "f11", cap("Figure 11: The Effects of Proposed Policies in Energy Profile Enhancement."),
    mention(20, first=20, style=["Figure 11"], count=1,
            lead="The results are shown in Figure 11.",
            pattern="as-shown-in",
            trail="the predicted values with targets all outstrip those without targets in "
                  "both 2025 and 2050",
            read=2),
    geo("bar", legend="above", numbers=True, panels=3, layout="1x3"),
    path=S_51, kind="result",
    note="Three grouped vertical bar panels - RCPR, SRC, RCPC - four states on each x axis, "
         "two years times with-and-without-policy, with the pale target bars drawn wider "
         "behind the saturated prediction bars. The single legend is unboxed and floats "
         "ABOVE all three panels, outside every region box, so a crop of the panels alone "
         "loses the key; it is the only legend in the paper not attached to one panel. "
         "Panels two and three are recorded as fragments."))

EXCLUDED.append(("p20-r2", bb(20, 2), "fragment-of-other"))
EXCLUDED.append(("p20-r3", bb(20, 3), "fragment-of-other"))

B["f12"] = bb(20, 4)
FIGURES.append(figure(
    "f12", cap("Figure 12: Radar Map: Energy Profile Evaluation and Target"),
    mention(20, first=20, style=["Fig. 12"], count=1,
            lead="Moreover, we also calculate the evaluation criteria based on the RC "
                 "targets and present the results in Fig. 12.",
            pattern="direct",
            trail="As we can see, SRC, RCPR, and, REGR for four states achieve signifi- "
                  "cant improvement under the RC targets.",
            read=2),
    geo("other", legend="outside-right", numbers=False, panels=4, layout="1x4"),
    path=S_52, kind="result",
    other_note="radar (spider) chart - a chart type the closed vocabulary does not name; "
               "four heptagons, one per state, with no radial scale printed",
    note="Four radar charts in one row on seven spokes, one polygon per scenario (2009, "
         "2050 prediction, 2050 target). No numeric tick labels on any spoke, so the reader "
         "compares polygon shapes, not values. The three unboxed legend entries sit outside "
         "to the RIGHT of the fourth chart, and the region boxes only tile part of the "
         "artwork - the fourth radar and most of its legend fall outside every box, so the "
         "coordinates here under-claim the figure. The other two boxes are recorded as "
         "fragments."))

EXCLUDED.append(("p20-r5", bb(20, 5), "fragment-of-other"))
EXCLUDED.append(("p20-r6", bb(20, 6), "fragment-of-other"))
# Pages 21-30: the two decrease tables, the sensitivity figure and its own table,
# and the seven regions that are nothing but the three appendix MATLAB listings.

B["t8"] = bb(21, 1)
TABLES.append(table(
    "t8", cap("Table 8: The decrease of RC and RP of NM and TX in 2025", "Table N:"),
    mention(21, first=21, style=["Table 8"], count=1,
            lead="According to our prediction of 2025, we discover the following decrease "
                 "in RC and RP of NM and TX, listed in Table 8.",
            pattern="direct", trail="", read=0),
    grid(3, 5, header=1, numeric=4, txt=1, rule="booktabs", merged=True),
    path=S_52, kind="result",
    note="One empty stub column, then NM and TX each spanning two columns, so the only "
         "merged cells in the paper are these two header spans. Every cell is a printed "
         "inline expression rather than a number - (35635-30119)/35635 = 15.5% - so the "
         "percentages land at different x positions and nothing is decimal-aligned. Three "
         "horizontal rules, no vertical rule, no shading."))

B["t9"] = bb(22, 1)
TABLES.append(table(
    "t9", cap("Table 9: The decrease of RCES of NM and TX in 2025 and 2050", "Table N:"),
    mention(22, first=21, style=["Table 9"], count=1,
            lead="The predicted decrease is shown in Table 9, which may be a consistent "
                 "downhill in future.",
            pattern="direct", trail="", read=0),
    grid(3, 3, header=1, numeric=2, txt=1, rule="booktabs", width="half"),
    path=S_52, kind="result",
    note="It prints at the top of p22 but belongs to the p21 action, and its pointer is the "
         "sentence that closes the previous page. Year stub plus NM and TX, two years, same "
         "inline-expression cells as Table 8 but with single-column headers and no merged "
         "cells."))

B["f13"] = bb(22, 2)
FIGURES.append(figure(
    "f13", cap("Figure 13: Sensitivity Analysis of Parameters in ARMA-GPR model"),
    mention(22, first=22, style=["Fig. 13(a)", "Fig. 13(b)"], count=2,
            lead="As shown in Fig. 13(a), when we change b from 0.1 to 0.9, the predicted "
                 "curve moves upward.",
            pattern="as-shown-in", trail="", read=2),
    geo("line", legend="inside", numbers=True, panels=2, layout="1x2"),
    path=S_6, kind="sensitivity",
    note="Two panels, one per parameter, each a single black GPR curve under a fan of blue "
         "ARMA-GPR curves swept over the parameter's range, with historical data as open "
         "circles and a dashed divider at 2010. The legend is the only boxed key in the "
         "paper and sits inside the axes at upper left. The right panel is a separate "
         "region, recorded as a fragment of this figure. Subcaptions are italic and "
         "unnumbered - '(a) sensitivity of b' and '(b) sensitivity of c' - so the only "
         "number on the exhibit is in the caption line below them."))

EXCLUDED.append(("p22-r3", bb(22, 3), "fragment-of-other"))

B["t10"] = bb(22, 4)
TABLES.append(table(
    "t10", cap("Table 10: Sensitivity Analysis of Parameter in Optimization Model",
               "Table N:"),
    mention(22, first=22, style=["Table 10"], count=1,
            lead="we obtain the optimized value of the objective function, shown in "
                 "Table 10",
            pattern="direct", trail="", read=0),
    grid(2, 10, header=1, numeric=9, txt=1, rule="booktabs"),
    path=S_6, kind="sensitivity",
    note="The widest grid in the paper and the only one that is wider than it is tall by a "
         "factor of five: a lambda stub row over nine lambda values, then one TRCP row of "
         "nine optimised values. The lambda row serves as the header, so the table reads as "
         "a function table rather than a data table; centred values, no decimal alignment, "
         "no unit."))

EXCLUDED.append(("p26-r1", bb(26, 1), "not-an-exhibit"))
EXCLUDED.append(("p27-r1", bb(27, 1), "not-an-exhibit"))
EXCLUDED.append(("p27-r2", bb(27, 2), "not-an-exhibit"))
EXCLUDED.append(("p28-r1", bb(28, 1), "not-an-exhibit"))
EXCLUDED.append(("p28-r2", bb(28, 2), "not-an-exhibit"))
EXCLUDED.append(("p29-r1", bb(29, 1), "not-an-exhibit"))
EXCLUDED.append(("p30-r1", bb(30, 1), "not-an-exhibit"))
# What 21 exhibits and 36 excluded regions generalise to.

RULES: list[str] = [
    "[caption.position] Figures are captioned below and tables above, with no exception "
    "across all 13 figures and all 8 grid exhibits - the side is fixed by exhibit type, not "
    "by page pressure.",

    "[caption.numbering] Every exhibit number is followed by a colon, 'Figure N:' or "
    "'Table N:', never by a period and never by a bare space; the caption then closes with a "
    "period only when it is a full clause.",

    "[caption.words] Captions stay short and noun-phrase shaped - 17 of the 21 run under "
    "twelve words - and the one long caption (32 words, Table 3) is long only because it has "
    "to define the arrows and the letters it prints in its cells.",

    "[table.rule_style] All eight grid exhibits are booktabs: one heavy rule under the header "
    "block, one heavy rule at the foot, and no vertical rule anywhere in the paper.",

    "[table.zebra] No table shades alternate rows; row tracking is done by the stub column, "
    "which is why the widest grid (10 item columns) stays readable without banding.",

    "[table.merged_cells] Merged cells occur exactly once in the paper, as Table 8's two "
    "header spans where NM and TX each sit over two columns of inline expressions.",

    "[table.header_rows] Two grids carry two header rows and both are pairs of stacked "
    "blocks over one shared stub set - Table 3's ten item names twice, Table 4's eight factor "
    "names twice; the other six grids carry a single header row.",

    "[table.rows] Grid size is read off the claim: the three grids of two or three rows hold "
    "a single comparison each, while the 5- to 21-row grids enumerate something the prose has "
    "just promised to enumerate.",

    "[table.width] Six grids run the full measure and two are narrow inserts at 299.6 and "
    "336.5 pt against a 520 pt text block; width follows the column count a claim needs, not "
    "the claim's importance.",

    "[geometry.family] Section kind picks the family before the data does: model sections "
    "take the schematics, the two raw scatter panels and the heat maps, result and "
    "sensitivity sections take the multi-panel line rows, the grouped bars and the radar.",

    "[geometry.legend] Legends are omitted wherever the caption or the italic sub-captions "
    "already name the elements - 6 of 13 figures carry no legend box - and the ones that do "
    "carry one place it inside at upper left except when three panels must share a key.",

    "[geometry.panel_count] Panel rows are the paper's default: 10 of 13 figures are "
    "multi-panel and the 1x3 row is the standard, used five times whenever three items are "
    "compared - here always the same three Arizona items.",

    "[geometry.three_d] Nothing in the paper is three-dimensional; all 57 regions were "
    "cropped and inspected, and no axis, projection or depth cue appears in any of them.",

    "[geometry.colorbar] Colour carries the value in exactly one figure: Figure 6's two "
    "colourbarred matrices are the only place where a reader decodes a ramp rather than a "
    "position.",

    "[mention.first_page] Every exhibit but one is cited by number in the body; the single "
    "uncited figure is also the only one whose neighbouring prose names a metric instead of "
    "the figure, so citation is the paper's default and its omission is local, not systemic.",

    "[mention.lead_pages] Pointer position is not stable: six citations print on the "
    "exhibit's own page, four one page early and two one page late, so 'cited before it "
    "appears' is not a rule this paper obeys.",

    "[mention.lead_pattern] Two pointer idioms alternate and neither dominates - the flat "
    "'we plot / we present ... in Fig. N' form (7 exhibits) and 'as shown in Fig. N' (5) - "
    "with the number always spelled 'Figure N' only on first use.",

    "[mention.read_sentences] A third of the figures (3 of 13) hand the reader no "
    "interpretation sentence at all, and they are the small-multiple strip, the heat maps and "
    "the mechanism diagram - the three exhibits whose reading is supposed to be self-evident.",

    "[place.solo_page] No exhibit is given a page of its own: all 21 share their page with "
    "prose, and the two full-page-scale grids still leave room for the paragraph that reads "
    "them.",

    "[place.page_zone] Exhibits are spread through the column rather than pushed to one end "
    "- 7 in the top third of a page, 8 in the middle, 6 at the bottom - so page zone says "
    "nothing about exhibit type.",

    "[place.area_frac] Region area is not emphasis: the two largest numbers (0.277, 0.271) "
    "belong to the two big grids, while every composed figure is tiled into small boxes of "
    "0.024 to 0.13, so area measures how the detector cut the artwork, not how loud the "
    "exhibit is.",

    "[place.section_kind] Nine exhibits land in result sections, eight in model sections, two "
    "in sensitivity, one in introduction and one in symbols - the exhibits are used as the "
    "evidence for a claim already made in prose, never as the argument itself.",
]

NOTE = (
    "Coverage. Ten tables are printed with captions; eight are boxed by the detector. The two "
    "gaps are declared rather than invented: Table 2 on page 7 ('Aggregated Items in Energy "
    "Profile', two columns, one header row, five data rows, cells holding the aggregation "
    "formulas, plus a numbered footnote defining p_j) and Table 7 on page 20 ('Renewable "
    "Consumption Targets for 2025 and 2050 (10^14 Btu)', five columns, one header row, two "
    "data rows, units carried in the caption). Both were confirmed on the rendered page and "
    "in the text layer; neither has a region, so neither can carry a record item without a "
    "fabricated bbox. The census for this paper therefore accounts 8 of the 10 printed "
    "tables, and the ratio of printed to boxed exhibits is 23 to 21. The same under-claim "
    "affects Figure 2's swatch legend (page 7, right of the grid, outside every box), Figure "
    "11's shared legend (page 20, floating above all three panels) and Figure 12's legend and "
    "fourth radar (page 20, right of and below the boxes).\n\n"
    "Region count is not exhibit count. 19 of the 36 exclusions are panel fragments, because "
    "the detector boxes each panel of a composed figure separately: 57 regions hold 21 "
    "exhibits. Sorting regions by index also scrambles two figures - page 18's row is stored "
    "right to left and page 13's 2x2 is stored row-major by x only, so panel (a) is region 3 "
    "in both - and any left-to-right reading must sort by bbox, not by index.\n\n"
    "Text pages are image-backed. Physical pages 9, 11, 12, 13, 15, 16, 17, 18 and 19 each "
    "contain low-resolution pasted strips of typeset prose and equations at 87-92 dpi; the "
    "detector boxes them and they are not exhibits. Page 12's strip is a duplicate placement "
    "of page 11's (one image xref, two placements), which is why the document jumps from "
    "equation (10) to equation (13) - equations (11) and (12) are printed nowhere. Pages "
    "26-30 are three MATLAB appendix listings that the detector boxes as seven table-like "
    "regions because every glyph run measures like a cell; they are excluded, not recorded."
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
assert len(ALL) + len(EXCLUDED) == len(MEASURED) == 57, (
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
