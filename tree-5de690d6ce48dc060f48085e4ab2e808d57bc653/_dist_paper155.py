"""Hand pass for P-C-2018-78577-919f0d0f (2018 MCM C, team 78577, "Sustainable Energy
Assessment": five energy indices per state, a PCA-plus-AHP combination weighting that
turns them into one overall score, an ARIMA forecast to 2025 and 2050, and a cooperative
compact whose funding shares come from a Shapley value).

23 pages, 36 measured regions on 16 of them. The paper prints 14 figures and 9 tables.
Page 1 is a cover page in letter format, so the document carries two page geometries.

Usage: python -I tools/_dist_paper155.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2018-78577-919f0d0f"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
REG = {(pg["page"], i): list(r["bbox"])
       for pg in LAYOUT["pages"] for i, r in enumerate(pg["regions"], 1)}
MEASURED = {(p, tuple(b)) for (p, _), b in REG.items()}

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


def cap(v: str, numbering: str = "Figure N:", *, position: str = "below",
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
    if caption["numbering"] == "Figure N:":
        caption = dict(caption, numbering="Table N:")
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

S_132 = ["1.3 Detailed Assumptions and Notations", "1.3.2 Mathematical Notations"]
S_32 = ["3 Energy Profile", "3.2 Energy Indices"]
S_331 = ["3 Energy Profile", "3.3 Analysis of Energy Profiles of Four States",
         "3.3.1 Energy Structure"]
S_332 = ["3 Energy Profile", "3.3 Analysis of Energy Profiles of Four States",
         "3.3.2 Use of Renewable and Clean Energy"]
S_333 = ["3 Energy Profile", "3.3 Analysis of Energy Profiles of Four States",
         "3.3.3 Greenhouse Gas Emissions"]
S_334 = ["3 Energy Profile", "3.3 Analysis of Energy Profiles of Four States",
         "3.3.4 Influential Factors"]
S_41 = ["4 Model for Overall Score", "4.1 Overview of the Model"]
S_42 = ["4 Model for Overall Score", "4.2 Utility Function"]
S_431 = ["4 Model for Overall Score", "4.3 Determination of Weights",
         "4.3.1 Solving for Weights of Secondary Indices Using PCA"]
S_432 = ["4 Model for Overall Score", "4.3 Determination of Weights",
         "4.3.2 Combination Weighting Approach"]
S_44 = ["4 Model for Overall Score", "4.4 Determination of the Best Profile"]
S_52 = ["5 Prediction of Energy Profiles", "5.2 Solution and Results of ARIMA"]
S_61 = ["6 Cooperation Strategies of Energy Compact", "6.1 Future Energy Targets"]
S_621 = ["6 Cooperation Strategies of Energy Compact", "6.2 Actions to Take",
         "6.2.1 Establish a Fund"]
# ---------------------------------------------------------------- pp 1, 5, 8-10
B["p1r1"] = bb(1, 1)
EXCLUDED.append((
    "p1-r1", B["p1r1"], "not-an-exhibit",
))

B["t1"] = bb(5, 1)
TABLES.append(table(
    "t1",
    cap("Table 1: Mathematical Notations", position="above"),
    mention(5, first=None, style=[], count=0, read=0),
    grid(9, 2, header=1, numeric=0, txt=2, rule="booktabs", width="full"),
    path=S_132, kind="symbols",
    note="The symbol glossary, and the widest grid in the paper at 1.00 of the "
         "measure. Three horizontal rules - top, under the header, foot - and not "
         "one vertical stroke anywhere in the body, so the two 2-line meanings "
         "wrap instead of colliding. Units are absent because every row is a "
         "symbol definition. The prose never numbers it: 'Here are the notations "
         "and their meanings in our paper:' hands it over.",
))

B["t2"] = bb(8, 1)
TABLES.append(table(
    "t2",
    cap("Table 2: CO2 Emission Ratio of Different Fuels", position="above"),
    mention(8, first=8, style=["Table 2"], count=1, read=0,
            lead="To analyze emissions across different fuels, we compare the amount of "
                 "CO2 emitted per unit of energy output using the data in Table 2.[1]",
            pattern="parenthetical",
            trail="Therefore, we calculate the index of total greenhouse gas emissions GE "
                  "as the weighted sum of consumption of fossil fuels"),
    grid(4, 2, header=1, numeric=1, txt=1, rule="booktabs", width="half",
         units_in_header=True),
    path=S_32, kind="model",
    note="Three fuels against one ratio, 0.74 of the measure. The unit lives in the "
         "header - 'CO2 Emission Ratio (Pound/Million Btu)' - which is why the three "
         "body cells are bare numbers; the foot rule prints heavier than the other "
         "two, the only weight difference anywhere in the paper's grid furniture. "
         "Cited while the sentence is still building ('using the data in Table 2'), "
         "not after it.",
))

CAP_F1 = cap("Figure 1: Energy Consumption Structure")
MEN_F1 = mention(9, first=9, style=["Figure 1"], count=2, read=1,
                 lead="In Figure 1, we present the consumption of five types of energy "
                      "per capita in the four states.",
                 pattern="direct",
                 trail="This shows that energy consumption in both 1960 and 2009 comes "
                       "mainly from non-renewable energy sources")
GEO_F1 = geo("bar", legend="inside", panels=4, layout="1x4", numbers=True)

B["p9r2"] = bb(9, 2)
FIGURES.append(figure(
    "p9r2", CAP_F1, MEN_F1, GEO_F1, path=S_331, kind="result",
    note="Arizona, the leftmost of four panels. Text-labelled bars, five fuel "
         "categories, y 0-300; the 'Consumption (Billion Btu Per Capita)' axis "
         "title prints on this panel only, which is how the strip shares its units "
         "without sharing its axes. Legend upper-right inside (1960 blue, 2009 dark "
         "red). x-label misspelt 'PATROLEUM'.",
))
B["p9r1"] = bb(9, 1)
FIGURES.append(figure(
    "p9r1", CAP_F1, MEN_F1, GEO_F1, path=S_331, kind="result", panel_of="Figure 1",
    note="California panel of the same strip: identical frame, no y-axis title, "
         "same 0-300 scale. Its region box overlaps the Arizona box by 138 pt of "
         "crop padding only - the artwork itself does not.",
))
B["p9r3"] = bb(9, 3)
FIGURES.append(figure(
    "p9r3", CAP_F1, MEN_F1, GEO_F1, path=S_331, kind="result", panel_of="Figure 1",
    note="New Mexico panel. Smallest inks in the strip after Texas, which is the "
         "point the trail sentence draws.",
))
B["p9r4"] = bb(9, 4)
FIGURES.append(figure(
    "p9r4", CAP_F1, MEN_F1, GEO_F1, path=S_331, kind="result", panel_of="Figure 1",
    note="Texas panel, rightmost. Retains the legend even though the group already "
         "carries one - the strip repeats its legend in every panel rather than "
         "declaring it once.",
))

CAP_F2 = cap("Figure 2: Energy Production Structure")
MEN_F2 = mention(9, first=9, style=["Figure 2"], count=1, read=1,
                 lead="Figure 2 shows the production of five types of energy per capita.",
                 pattern="figure-n-shows",
                 trail="Arizona and California lack natural resources while New Mexico "
                       "and Texas are rich in resources such as patroleum and natural gas.")
GEO_F2 = geo("bar", legend="inside", panels=4, layout="1x4", numbers=True)

B["p9r6"] = bb(9, 6)
FIGURES.append(figure(
    "p9r6", CAP_F2, MEN_F2, GEO_F2, path=S_331, kind="result",
    note="Arizona, leftmost panel of the production strip. Same template as Figure "
         "1 but the y ceiling moves to 1000, so the production/consumption ratio is "
         "readable across the two strips only by eye. Caption sits outside all four "
         "boxes, 20 pt below the row.",
))
B["p9r5"] = bb(9, 5)
FIGURES.append(figure(
    "p9r5", CAP_F2, MEN_F2, GEO_F2, path=S_331, kind="result", panel_of="Figure 2",
    note="California panel. Its box is the widest of the eight (0.751 aspect against "
         "0.685 for its siblings) because the crop caught a stray tick label.",
))
B["p9r7"] = bb(9, 7)
FIGURES.append(figure(
    "p9r7", CAP_F2, MEN_F2, GEO_F2, path=S_331, kind="result", panel_of="Figure 2",
    note="New Mexico panel - the clearest visual statement of the paper's own claim "
         "that NM and TX are resource-rich while AZ and CA are not.",
))
B["p9r8"] = bb(9, 8)
FIGURES.append(figure(
    "p9r8", CAP_F2, MEN_F2, GEO_F2, path=S_331, kind="result", panel_of="Figure 2",
    note="Texas panel, rightmost. Dominates the strip on natural gas, which is what "
         "the trail sentence generalises from.",
))

B["p10r1"] = bb(10, 1)
FIGURES.append(figure(
    "p10r1", cap("Figure 3: Use of Renewable and Clean Energy"),
    mention(10, first=9, style=["Figure 3"], count=2, read=1,
            lead="Figure 3 illustrates the proportion of consumption of renewable and "
                 "clean energy",
            pattern="figure-n-shows",
            trail="The general trend of proportion of consumed clean energy had been "
                  "decreasing before 1985 and have been slowly increasing sincethen."),
    geo("line", legend="inside", panels=1, numbers=True),
    path=S_332, kind="result",
    note="Eight series - four states times renewable/clean - on one 'Proportion' "
         "axis, 0-0.8. The measured region is the vector axes box; the plot layer "
         "itself is two rasters nested inside it, so the census boxes this exhibit "
         "three times and only the largest box is claimed here. Legend upper-right "
         "inside, eight entries. The x tick labels print as an unreadable glyph "
         "cluster - the axis is unscannable at print size.",
    other_note="",
))

B["p10r2"] = bb(10, 2)
FIGURES.append(figure(
    "p10r2", cap("Figure 4: Greenhouse Gas Emissions Per Capita"),
    mention(10, first=10, style=["Figure 4"], count=2, read=1,
            lead="Figure 4 illustrates the emissions per capita and the changing trend "
                 "over time.",
            pattern="figure-n-shows",
            trail="Arizona and California have obvious advantages over New Mexico and "
                  "Texas in this aspect."),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_333, kind="result",
    note="Structurally complete and substantively empty: frame, gridlines, y-axis "
         "title and tick labels all print, and the plot area holds 0.000 per cent "
         "coloured ink - no series was ever drawn. Zero legends is normal here, but "
         "with no ink at all there is nothing a legend could name. Caption shares one "
         "physical text line with Figure 3's caption; each has its own box.",
))

B["p10r3"] = bb(10, 3)
B["p10r4"] = bb(10, 4)
EXCLUDED.append(("p10-r3", B["p10r3"], "not-an-exhibit"))
EXCLUDED.append(("p10-r4", B["p10r4"], "not-an-exhibit"))
# --------------------------------------------------------------- pp 11-15
B["p11r1"] = bb(11, 1)
FIGURES.append(figure(
    "p11r1", cap("Figure 5: Population of Four States"),
    mention(11, first=11, style=["Figure 5"], count=1, read=1,
            lead="Population of the four states is shown in Figure 5.",
            pattern="as-shown-in",
            trail="It can be seen that the population of California and Texas are much "
                  "larger than that of Arizona and New Mexico."),
    geo("bar", legend="inside", panels=1, numbers=True),
    path=S_334, kind="result",
    note="The paper's only stacked bar: one column per year 1960-2009, four states "
         "piled in each column, y 'Population (Thousand)' to 70000. 299 vector paths, "
         "the densest vector figure here. Legend upper-left inside, which is the only "
         "place in this paper a legend takes the left corner. x ticks print legibly "
         "here, unlike Figures 3, 4 and 9.",
))

B["p12r1"] = bb(12, 1)
FIGURES.append(figure(
    "p12r1", cap("Figure 6: Overview of the Model"),
    mention(12, first=12, style=["Figure 6"], count=1, read=1,
            lead="Figure 6 gives an intuitive representation of our model.",
            pattern="figure-n-shows",
            trail="After that, we adopt the Combination Weighting Approach to get the "
                  "overall score S."),
    geo("flowchart-or-schematic", legend="none", panels=1, numbers=False),
    path=S_41, kind="model",
    note="Three-tier hierarchy on one bitmap: 'Overall Score' at the top, the three "
         "energy indices in the middle row, the eight secondary indices in the bottom "
         "row, arrows fanning up. No legend box - the two method names that explain "
         "the tiers, 'Combination Weighting Approach' and 'PCA', print outside-left "
         "of the middle and bottom rows as plain marginalia, so the diagram's "
         "semantics sit in the caption rail rather than in a key.",
))

B["p13r1"] = bb(13, 1)
EXCLUDED.append(("p13-r1", B["p13r1"], "not-an-exhibit"))

B["p13r2"] = bb(13, 2)
FIGURES.append(figure(
    "p13r2", cap("Figure 7: Sketch Map of Utility Function"),
    mention(13, first=13, style=["Figure 7"], count=1, read=1,
            lead="As is shown in Figure 7, we effectively increase the distinction of "
                 "the data by using utility function.",
            pattern="as-shown-in",
            trail="Substituting formula (3) (4) into formula (2), ai = 0, bi = 1 and ki "
                  "can be"),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_42, kind="model",
    note="One concave increasing curve from (0,0) to (1,1) on unit axes, with two "
         "dashed guides at the median crossing. The guide is annotated in-artwork - "
         "'median(x_i)' printed inside the plot near the baseline - instead of in a "
         "legend, which is why a single-series teaching sketch still carries a label.",
))

B["t3"] = bb(14, 1)
TABLES.append(table(
    "t3",
    cap("Table 3: Results of PCA", position="above"),
    mention(14, first=14, style=["Table 3"], count=2, read=1,
            lead="We obtain the weights of secondary indices contributing to the first "
                 "two principle components as shown in Table 3.",
            pattern="as-shown-in",
            trail=""),
    grid(6, 6, header=2, numeric=5, txt=1, rule="vertical-rules", width="full",
         decimal=True),
    path=S_431, kind="model",
    note="Two tabulars stacked without a gap: a 'Renewable' block and a 'Clean' block, "
         "each with its own header row and its own Comp.1/Comp.2 rows, which is why it "
         "carries two header rows against four data rows. The verticals are short - "
         "block-height only, 0.47 ink coverage - so they mark column edges inside each "
         "block and do not line up across the seam. Decimals five places, right "
         "aligned per column. Captioned above; the second citation on p15 uses the "
         "same spelling.",
))

B["p14r2"] = bb(14, 2)
EXCLUDED.append(("p14-r2", B["p14r2"], "not-an-exhibit"))

CAP_F8 = cap("Figure 8: Energy Indices in 2009")
MEN_F8 = mention(15, first=15, style=["Figure 8"], count=1, read=1,
                 lead="The energy indices of four states in 2009 are shown in Figure 8 "
                      "and the overall scores of four states during 50 years",
                 pattern="as-shown-in",
                 trail="From Figure 9, we know that CA (California) has the best energy "
                       "profile in 2009, followed by TX (Texas), NM (New Mexico) and AZ "
                       "(Arizona).")

B["p15r2"] = bb(15, 2)
FIGURES.append(figure(
    "p15r2", CAP_F8, MEN_F8,
    geo("bar", legend="inside", panels=1, numbers=True),
    path=S_44, kind="result",
    note="Three grouped series (U_r, U_c, GE) over four state categories, y 'Value' "
         "0-1, x 'State' with the only legible state labels in the paper. Legend "
         "upper-right inside. Cited jointly with Figure 9 in one sentence that names "
         "both exhibits and then reads them in a second sentence - the paper's "
         "two-figure weld.",
))

B["p15r1"] = bb(15, 1)
FIGURES.append(figure(
    "p15r1", cap("Figure 9: Overall Scores"),
    mention(15, first=15, style=["Figure 9"], count=2, read=1,
            lead="The energy indices of four states in 2009 are shown in Figure 8 and "
                 "the overall scores of four states during 50 years",
            pattern="as-shown-in",
            trail="This result is quite reasonable because California had the lowest "
                  "emission of greenhouse gases (per capita)"),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_44, kind="result",
    note="Second empty plot area in the paper: frame, gridlines and y title "
         "'Overall Score' 0.00-0.25 print, plot ink 0.000 per cent, x ticks an "
         "unreadable glyph cluster. The census boxes this exhibit twice (r1 vector "
         "axes, r3 raster layer, IoU 0.93) and the vector box is claimed. The prose "
         "nevertheless ranks all four states from it, which is a reading the artwork "
         "cannot support.",
))

B["p15r3"] = bb(15, 3)
EXCLUDED.append(("p15-r3", B["p15r3"], "not-an-exhibit"))
# --------------------------------------------------------------- pp 16-21
B["p16r1"] = bb(16, 1)
EXCLUDED.append(("p16-r1", B["p16r1"], "not-an-exhibit"))

B["p17r1"] = bb(17, 1)
FIGURES.append(figure(
    "p17r1", cap("Figure 10: Autocorrelation Function"),
    mention(17, first=17, style=["Figure 10"], count=1, read=1,
            lead="As is shown in Figure 10, the autocorrelation value basically does "
                 "not exceed the confidence intervals after the 4-th order hysteresis.",
            pattern="as-shown-in",
            trail="so we have p = 4."),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_52, kind="result",
    note="Left panel of a side-by-side stem pair, 156 vector paths. y 'ACF' from 1.0 "
         "down past -0.4, x 'Lag' 0-30, plus dashed dark-red confidence bounds and a "
         "zero baseline. No legend: a single correlogram does not need one, and the "
         "series identity is carried by the axis title. Its caption and Figure 11's "
         "share one printed line; each caption owns the panel beneath it.",
))

B["p17r2"] = bb(17, 2)
FIGURES.append(figure(
    "p17r2", cap("Figure 11: Partial Autocorrelation Function"),
    mention(17, first=17, style=["Figure 11"], count=1, read=0,
            lead="Using the same method, according to Figure 11, we can obtain that "
                 "q = 4.",
            pattern="parenthetical",
            trail=""),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_52, kind="result",
    note="Right panel of the stem pair, 154 paths, same frame and same bounds as "
         "Figure 10. Identical geometry to its twin: equal width, 22 pt gutter, one "
         "caption each. The lag-0 stem prints at 0.37 rather than 1.0, which is the "
         "one thing in the pair that does not read as a textbook PACF.",
))

B["p17r3"] = bb(17, 3)
FIGURES.append(figure(
    "p17r3", cap("Figure 12: Prediction of CAr of California"),
    mention(17, first=17, style=["Figure 12"], count=1, read=1,
            lead="And then by calculation, we can draw the prediction results as shown "
                 "in Figure 12.",
            pattern="as-shown-in",
            trail="These results show the feasibility of the model."),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_52, kind="result",
    note="The only pasted chart on this page: a single 2.076-aspect bitmap with y 'CAr' "
         "0.001-0.004 and x 'Year' 1975-2050, observed salmon against predicted teal "
         "with a pale-blue band. The band is a coarse stepped polygon, visibly built by "
         "hand rather than computed, and with no legend the three inks are "
         "unidentified. Its two siblings above are vector and native; this one is a "
         "screenshot, which is why it is the only figure in the paper whose tick "
         "labels are missing from the text layer.",
))

B["t6"] = bb(18, 1)
TABLES.append(table(
    "t6",
    cap("Table 6: Results of Parameters in ARIMA", position="above"),
    mention(18, first=17, style=["Table 6"], count=1, read=0,
            lead="The parameters are shown in Table 6.",
            pattern="as-shown-in",
            trail="These results show the feasibility of the model."),
    grid(4, 5, header=1, numeric=4, txt=1, rule="vertical-rules", width="half"),
    path=S_52, kind="result",
    note="Transposed on purpose: parameter names are the column heads, 'Parameter' and "
         "'Value' are the stub labels, and the four phi and four theta coefficients "
         "sit as two 2-row blocks. One full-height vertical separates the stub from "
         "the values; the horizontals stop after the phi block, so the theta header "
         "and its values run together with no rule between them - an asymmetry nothing "
         "else in the paper's grids shows. Values centred, not decimal-aligned, so "
         "-0.0048 and -0.1790 do not line up on the point.",
))

CAP_F13 = cap("Figure 13: Prediction of Overall Scores")

B["p18r2"] = bb(18, 2)
FIGURES.append(figure(
    "p18r2", CAP_F13,
    mention(18, first=18, style=["Figure 13"], count=1, read=1,
            lead="Our prediction of overall score of each state is shown in Figure 13.",
            pattern="as-shown-in",
            trail="The overall scores of the four states in 2025 and 2050 are shown in "
                  "Table 7."),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_52, kind="result",
    note="Four unlabelled series - red, purple, green, blue - over 1960-2050 with a "
         "dashed vertical at 2010 marking the forecast seam, y 'Overall Score'. No "
         "legend, so which colour is which state is unrecoverable from the artwork "
         "while Table 7 supplies exactly that mapping. Every year is a rotated x tick. "
         "The census boxes this exhibit twice (r2 vector frame, r3 the bitmap nested "
         "96 per cent inside it); the outer box is claimed.",
))

B["p18r3"] = bb(18, 3)
EXCLUDED.append(("p18-r3", B["p18r3"], "not-an-exhibit"))

B["t7"] = bb(18, 4)
TABLES.append(table(
    "t7",
    cap("Table 7: Prediction of Overall Scores in 2025 and 2050", position="above"),
    mention(18, first=18, style=["Table 7"], count=1, read=0,
            lead="The overall scores of the four states in 2025 and 2050 are shown in "
                 "Table 7.",
            pattern="as-shown-in",
            trail=""),
    grid(3, 5, header=1, numeric=4, txt=1, rule="vertical-rules", width="half",
         decimal=True),
    path=S_52, kind="result",
    note="The smallest grid with a state header: five columns (empty stub, AZ, CA, NM, "
         "TX), two year rows, one internal vertical after the stub, three horizontals. "
         "The stub corner is left blank rather than labelled, the paper's default for "
         "every state-column grid. Four decimals, decimal-aligned - the numbers line up "
         "on the point here, unlike Tables 6, 8 and 9.",
))

B["p19r1"] = bb(19, 1)
FIGURES.append(figure(
    "p19r1", cap("Figure 14: Prediction of Overall Scores"),
    mention(19, first=19, style=["Figure 14"], count=1, read=1,
            lead="As is shown in Figure 14, we can know that the prediction value of Ur "
                 "in 2025 and 2050 is respectively 0.34 and 0.59.",
            pattern="as-shown-in",
            trail="In order to show the strength of cooperation, we set the target as "
                  "110% of the predicted value."),
    geo("line", legend="none", panels=1, numbers=True),
    path=S_61, kind="result",
    note="A third distinct artwork carrying a duplicate caption: single blue series of "
         "Ur on a purple frame with a dashed horizontal at 0.34, a dashed vertical at "
         "2025 and a solid horizontal at 0.59 - the two numbers the prose reads out. "
         "It is NOT a reprint of Figure 13 (four series, no reference levels). The "
         "caption was copied from page 18 verbatim, so the paper's two forecast "
         "figures cannot be told apart from their captions alone.",
))

B["p20r1"] = bb(20, 1)
EXCLUDED.append(("p20-r1", B["p20r1"], "not-an-exhibit"))

B["t8"] = bb(20, 2)
TABLES.append(table(
    "t8",
    cap("Table 8: Electricity Information", position="above"),
    mention(20, first=20, style=["Table 8"], count=1, read=1,
            lead="The detailed information of electricity and its price is shown in "
                 "Table 8.",
            pattern="as-shown-in",
            trail=""),
    grid(5, 5, header=1, numeric=4, txt=1, rule="booktabs", width="half"),
    path=S_621, kind="model",
    note="The widest grid of the second half, 0.81 of the measure, and the only one "
         "whose row labels occupy more lines than its data rows: four stubs print as "
         "six text lines because 'Electricity Price' wraps over its unit. Three "
         "horizontal rules, no vertical anywhere, no bands. The units live inside the "
         "stub cells - '(Btu)', '($/MWh)' - not in the header, and the two price rows "
         "glue wind and solar into one label, so the table never says which of 50/40/35/30 "
         "belongs to which technology.",
))

B["t9"] = bb(21, 1)
TABLES.append(table(
    "t9",
    cap("Table 9: Results of Investment", position="above"),
    mention(21, first=21, style=["Table 9"], count=1, read=1,
            lead="we solve formula (7) (8) and get the share and the amount of investment "
                 "of each state illustrated in Table 9.",
            pattern="as-shown-in",
            trail=""),
    grid(3, 6, header=1, numeric=5, txt=1, rule="booktabs", width="half"),
    path=S_621, kind="result",
    note="Two measured rows over a six-column header, three horizontal rules and no "
         "vertical at all - so the columns are tracked by spacing alone, which works "
         "here because the stub cells carry their units. Unit-in-stub is the paper's "
         "convention for the second half of the document. The printed totals do not "
         "foot: the share row sums to 0.998 against a printed 1, and the money row "
         "sums to 348.6 against a printed 343.85.",
))
RULES = [
    "Twenty figure boxes caption BELOW the artwork and seven table boxes caption "
    "ABOVE it: the side is decided by exhibit kind, with no exception in either "
    "direction [caption.position].",
    "Two four-panel strips print ONE caption for four panels and place it once, "
    "centred under the whole row, so the caption belongs to the strip and every "
    "panel item inherits it [geometry.panel_count].",
    "Panel order inside a strip runs x-ascending (AZ, CA, NM, TX) while the box "
    "indices run AZ, CA, NM, TX as r2, r1, r3, r4 - the census orders panels by "
    "geometry, never by region index [geometry.panel_layout].",
    "The legend takes the upper-right corner inside the frame in ten boxes and the "
    "upper-left in exactly one, the only stacked bar in the paper [geometry.legend].",
    "Nine figures carry no legend at all, and in five of them the absence is the "
    "defect: four-series Figure 13, the three-ink Figure 12, the unlabelled guides "
    "of Figure 14, and the two empty plot areas [geometry.legend].",
    "No figure carries a colourbar and no figure is three-dimensional; both devices "
    "stay unused across all fourteen [geometry.colorbar] [geometry.three_d].",
    "The only artwork with no printed numbers is the one schematic; every chart "
    "that plots a series also prints ticks and tick labels [geometry.printed_numbers].",
    "No artwork prints values on its marks, so every number a reader needs is in a "
    "grid rather than on a bar [geometry.data_labels].",
    "The two strips repeat frame, scale, legend and axis title in each panel instead "
    "of declaring shared axes [geometry.shared_axes].",
    "Rule style alternates: the two early definition grids and the two late data "
    "grids are horizontals only, while the three middle result grids each carry an "
    "internal full-height vertical [table.rule_style].",
    "Two grids span the full measure (1.00 and 0.97) and five sit between 0.49 and "
    "0.81 of it; nothing is column-narrow [table.width].",
    "Only Table 2 puts its unit in the header; Tables 8 and 9 put the unit inside "
    "the stub cell and the other four print no unit at all [table.units_in_header].",
    "Two grids are decimal-aligned - Table 3 and the two-row state grid of Table 7 - "
    "and five are centred, which is why negative coefficients in Table 6 do not "
    "line up on the point [table.decimal_aligned].",
    "The paper never uses zebra shading, merged cells, a diagonal header, a "
    "landscape grid or a continued table, though its spanner-widths invite all "
    "five [table.zebra] [table.merged_cells] [table.diagonal_header] "
    "[table.orientation] [table.continued].",
    "Header rows are one on every grid except Table 3, where two stacked tabulars "
    "each contribute their own header row [table.header_rows].",
    "Every grid puts one text stub against three to five numeric columns; the only "
    "all-text grid is the symbol glossary [table.numeric_cols] [table.text_cols].",
    "Grid size runs 3 rows by 5 columns up to 9 rows by 2 columns; the glossary's "
    "nine rows make it the tallest table in the paper [table.rows] [table.cols].",
    "Only three section kinds host an exhibit - symbols for the notation glossary, "
    "model for the method apparatus, result for everything measured; the abstract, "
    "the assumptions and the evaluation section carry none [place.section_kind].",
    "All fourteen figures and six of the nine tables are cited by number; the "
    "notation glossary is the only table the prose never names, reached instead by "
    "'Here are the notations and their meanings in our paper:' [mention.first_page].",
    "Lead sentences take three shapes and the shape decides the word order: "
    "'In Figure 1, we present' (figure first), 'Figure 2 shows' (figure as "
    "subject), 'as shown in Figure 7' (figure last) [mention.lead_pattern].",
    "Two exhibits are pointed at from inside a subordinate clause while the sentence "
    "is still building - 'according to Figure 11' and 'using the data in Table 2' - "
    "rather than from a sentence of their own [mention.lead_pattern].",
    "Every cited figure is followed within one sentence by a reading sentence, and "
    "the reading regularly outruns the artwork: four states are ranked from a figure "
    "with no data ink [mention.read_sentences].",
    "Two exhibits are cited twice (Figures 1/3 and 9) and one only inside a joined "
    "spelling, 'Figure9'; the count field keeps the printed occurrences, not the "
    "intended ones [mention.count].",
    "A lead of one page occurs twice (Figure 3, Table 6) and no lead exceeds it; the "
    "rest are cited on their own page [mention.lead_pages].",
    "Caption spellings are recorded as printed, including the joined 'Figure9' that "
    "the p15 sentence uses for the second of its two figures [mention.style].",
    "Captions are noun phrases: none concludes, none states a condition, none prints "
    "a unit, and none is written in the active voice [caption.concludes] "
    "[caption.conditions] [caption.units] [caption.voice].",
    "Only one caption names a variable symbol - Figure 12's CAr - and the rest name "
    "a quantity in words, which is why the two forecast figures end up with "
    "identical captions [caption.variables].",
    "Captions run four to eight words each, one sentence every time, always with the "
    "colon inside the number line [caption.words] [caption.sentences] "
    "[caption.numbering].",
    "Exhibits cluster in the top and middle thirds of their pages and none is given a "
    "page of its own: no exhibit is solo [place.page_zone] [place.solo_page].",
    "A region's area runs from 0.02 of the page for a strip panel to 0.18 for the "
    "notation glossary; the paper never prints a page-sized exhibit [place.area_frac].",
    "Panel boxes are claimed as items with the parent strip named in panel_of, so the "
    "family aggregate counts eight bar rows for the two four-panel strips rather than "
    "two [geometry.family] [geometry.panel_count].",
]

NOTE = (
    "Coverage. The paper prints 23 exhibits: 14 numbered figures and 9 numbered "
    "tables. Twenty-one of them own a measured region; Tables 4 and 5 print side by "
    "side above every detected box on p15, so they are declared here as unboxed and "
    "carry no item. The census claims 27 items over 36 measured regions with 9 "
    "exclusions, and no exhibit is solo on a page. Page 1 is a cover in letter "
    "format (612x792 pt) while pages 2-23 are 595.5x842, so the document carries two "
    "page geometries and any area fraction on page 1 is computed against the cover's "
    "own frame. "
    "\n\n"
    "Region count is not exhibit count. The eight boxes on p9 are two exhibits: each "
    "four-panel strip is a column of separate bitmaps, so the detector sees four "
    "regions per figure, and the census claims them as panel items rather than "
    "collapsing them. Four more regions are duplicate detections of an exhibit "
    "already claimed - p10's r3 and r4 are the raster plot layer inside Figure 3's "
    "vector axis box, p15's r3 sits over Figure 9 at IoU 0.93, and p18's r3 is "
    "nested 96 per cent inside Figure 13's frame. The last five exclusions are "
    "raster strips that are not exhibits at all: two Summary paragraphs on p1, the "
    "utility-function equations (2)(3)(4) on p13, equation (5) on p14, the prose "
    "plus equation (6) on p16, and the Shapley equations (7)(8) on p20. "
    "\n\n"
    "Apparatus. Every one of those raster strips is invisible to the text layer: p1 "
    "jumps from 'average values of other cities.' to 'After that, we use the ARIMA "
    "model', losing both Summary paragraphs, and p16 and p20 lose whole equations. "
    "Two figures print with completely empty plot areas - Figure 4 on p10 and Figure "
    "9 on p15 both show frame, gridlines and axis titles over 0.000 per cent data "
    "ink - while the prose ranks four states from Figure 9. Figure 14 repeats Figure "
    "13's caption verbatim though the two artworks share nothing but plot chrome. "
    "The x tick labels of Figures 3, 4 and 9 print as unreadable glyph clusters and "
    "the fuel category is misspelt 'PATROLEUM' in all eight strip panels. Table 8 "
    "glues wind and solar into single row labels, so its four prices are never "
    "attached to a technology, and Table 9's two rows both fail to foot: shares sum "
    "to 0.998 against a printed 1, money to 348.6 against a printed 343.85. "
    "\n\n"
    "What the custody buys. Read as a set, the exhibits keep three habits: captions "
    "below for figures and above for tables without exception; one caption per "
    "composite, printed outside the panels; and a reading sentence after the citation "
    "that converts the picture into a ranking. Everything the paper knows about how "
    "to place an exhibit comes from that trio, and nothing in it depends on the "
    "figure family."
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
assert len(ALL) + len(EXCLUDED) == len(MEASURED) == 36, (
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
