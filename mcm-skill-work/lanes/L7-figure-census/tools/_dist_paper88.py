"""Hand census of P-D-2015-38996-1efe10af (Team 38996, 21 pages, 19 measured regions).

Eleven figure rows, five table rows, three excluded regions, no unaccounted region. The paper
numbers ten figures and six tables; Table 1 prints on p9 as a text-only calculation a reader has to
read line by line, rules nothing, and owns no measured region, so it is declared as a gap.

  p8  r1  Fig.1   flowchart-or-schematic       the four-level index system tree
  p10 r1  Fig.2   line                         SE/ER plane, ideal direction and angle theta
  p10 r2  Fig.3   other                        the vector-and-angle construction of theta
  p12 r1  Fig.4   line                         five country trajectories, 2003-2012
  p12 r2  Table 2 table-grid                   sustainable distance of the five countries
  p14 r1  Fig.5   line                         Nepal's trajectory
  p14 r2  Fig.6   line                         ARIMA forecast with two confidence bands
  p15 r1  Table 3 table-grid                   effective indices list
  p16 r1  Fig.7   bar                          sensitivity, upper panel, 22 bars
  p16 r2  Fig.7   bar                          sensitivity, lower panel, 22 bars
  p16 r3  Table 4 table-grid                   possible proposal trade-off
  p18 r1  (piece)  duplicate                   Society cluster pasted inside Figure 8, excluded
  p18 r2  Fig.8   flowchart-or-schematic       the three-cluster system dynamics diagram
  p18 r3  (piece)  duplicate                   Economic cluster pasted inside Figure 8, excluded
  p18 r4  (piece)  duplicate                   Environment cluster pasted inside Figure 8, excluded
  p18 r5  Table 5 table-grid                   estimated equations of the three subsystems
  p19 r1  Fig.9   line                         simulation against the ARIMA time series
  p19 r2  Fig.10  line                         four programme loci
  p20 r1  Table 6 table-grid                   sustainable distance every five years

The one structural finding is on p18: Figure 8 is ONE drawing, but the region pass measures four
regions there because the Society, Economic and Environment sub-graphs are pasted as their own
bitmaps inside the outer vector cluster. The 0.29-area vector region holds the whole three-cluster
diagram and is the exhibit; the three raster pieces repeat it and are excluded as duplicates.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2015-38996-1efe10af"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

for _key, _bbox in REG.items():
    _ctx = CTXREG.get(_key)
    if _ctx is None or max(abs(a - b) for a, b in zip(_ctx["bbox"], _bbox)) > 0.5:
        raise SystemExit(f"region numbering disagrees with the context dump at {_key}")

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


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


def uncited() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          pattern: str = "direct", read: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N", position: str = "below",
            units: bool = False, variables: int = 0, conditions: bool = False,
            concludes: bool = False, voice: str = "none") -> dict:
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim.strip() else 0),
            "units": units, "variables": variables > 0, "variable_count": variables,
            "conditions": conditions, "concludes": concludes, "voice": voice,
            "position": position}


def geometry(family: str, panels: int = 1, layout: str = "1x1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = True,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


# ---------------------------------------------------------------- section paths
# The heading index of this paper carries real labels, so these are its own entries; the four
# junk entries it also returns ("1 Ideal development direction S", "0.0015 Sensitivity", ...) are
# figure text and are not used as sections.
SEC_331 = ["3.3 The Model", "3.3.1 Index System"]
SEC_332 = ["3.3 The Model", "3.3.2 Sustainability Measurement"]
SEC_333 = ["3.3 The Model", "3.3.3 An Implementation of Our model"]
SEC_41 = ["4 Sustainability Development Plan",
          "4.1 Current Situation and Forecast without intervention"]
SEC_421 = ["4.2 Details of the Plan", "4.2.1 Effectiveness Judgment by Sensitivity Analysis"]
SEC_422 = ["4.2 Details of the Plan", "4.2.2 Reasonability Judgment by Actual Conditions"]
SEC_51 = ["5 Dynamic Improvement", "5.1 System Dynamics and Structure Equations"]
SEC_52 = ["5 Dynamic Improvement", "5.2 Simulation Run and Results"]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
for _label in [p for group in (SEC_331, SEC_332, SEC_333, SEC_41, SEC_421, SEC_422, SEC_51,
                               SEC_52) for p in group]:
    if schema.norm(_label) not in _KNOWN:
        raise SystemExit(f"section label is not an indexed heading: {_label!r}")

ITEMS: list[dict] = []


def figure(page: int, reg: int, number: str, family: str, cap: dict, cap_src: str,
           mention: dict, kind: str, section: list[str], note: str,
           geo: dict | None = None, confidence: str = "high",
           section_kind: str = "model", other_note: str = "") -> None:
    item = {
        "page": page, "bbox": REG[(page, reg)], "kind": kind, "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap["verbatim"],
        "caption": cap, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS.append(item)


# ------------------------------------------------------------------- p8 Figure 1
figure(8, 1, "1", "flowchart-or-schematic",
       caption(q("Figure 1 Index System", 8)),
       "text-layer",
       cited(8, 8, ["Figure 1"], 1, "The indices system is showed in Figure 1."),
       "vector", SEC_331,
       "The index system drawn as a four-level tree. 'Level 4 Sustainable Development' is a single "
       "box at the crown; three dashed cluster boxes carry Level 3 - Society, Economics, "
       "Environment; Level 2 hangs under them as seven boxes (Labor, Health, Education, Technology "
       "under Society; Agri-culture, Industry, Service under Economics; Natural Resource and "
       "Pollution under Environment); Level 1 hangs as circles under the Level 2 boxes, each "
       "naming a World Bank indicator with ', etc.' after it. Two brace labels inside the picture "
       "read 'SE Index' and 'ER Index', so the tree also declares which half feeds which axis of "
       "the later scatter. No axis, no scale, no number, no legend box. Printed defects: every "
       "Level 1 label is broken mid-word by the narrow circle ('Labor force participat ion rate, "
       "etc.', 'Communi ty health workers, re, etc.'), 'Education' appears twice as a Level 2 "
       "box (under Health and as its own box) with an 'education expenditu re, etc.' circle under "
       "each, and 'Agri-culture' is hyphenated across two lines.",
       geometry("flowchart-or-schematic", numbers=False))

# ------------------------------------------------------------------- p10 Figure 2
figure(10, 1, "2", "line",
       caption(q("Figure 2 Sustainability Measurement", 10)),
       "text-layer",
       cited(11, 10, ["Figure 2"], 1,
             "the valid development is the projection vector"),
       "vector", SEC_332,
       "A construction in the SE Index (x) against ER Index (y) plane, both axes ticked 0 and 1 "
       "only, with the intermediate scale left unstated. Four rays meet the upper-right corner S: "
       "the red 'Ideal development direction' along the diagonal, a black 'Valid Development' "
       "vector from the origin to point A, a blue 'Standard Development Line' beside it, and a fine "
       "dashed 'Development direction (Calculated by regression)' below. The intersection angle "
       "theta is drawn as an arc between the ideal ray and the actual one, and A' marks the "
       "projection of A. Four small year markers 2009 to 2012 cluster just above A - they are the "
       "only data on the picture, and they are drawn at a size that makes the cluster unreadable. "
       "The ray labels are rotated and sit inside the plotting area, colliding with the theta arc "
       "and the year labels.",
       geometry("line", legend="inside", labels=True))

# ------------------------------------------------------------------- p10 Figure 3
figure(10, 2, "3", "other",
       caption(q("Figure 3 Ideal development direction", 10)),
       "text-layer",
       cited(10, 10, ["Figure 3"], 1,
             "Figure 3 shows the relation between these two direction and the interseSction angle."),
       "vector", SEC_332,
       "A bare vector construction with no axes, no ticks and no numbers: a ringed origin at the "
       "left, one long red 'Ideal development direction' arrow, and five short grey arrows leaving "
       "the origin at increasing angles, each with its own theta_i label. There is no data series, "
       "no scale and nothing measured; the picture exists only to define the angle the paper calls "
       "harmonious development. It is recorded as other rather than as line or schematic because "
       "it is neither a plot nor a diagram of a system, only a set of rays and one angle glyph.",
       geometry("other", numbers=False),
       other_note="vector-and-angle construction: origin ring, five grey rays, one red ideal ray, "
                  "angle labels theta_1 to theta_4, no axes and no data")

# ------------------------------------------------------------------- p12 Figure 4
figure(12, 1, "4", "line",
       caption(q("Figure 4 Implementation of five countries", 12)),
       "text-layer",
       cited(12, 12, ["Figure 4"], 1, "Figure 4 shows our implementation result"),
       "vector", SEC_333,
       "Five country trajectories in the SE Index (x) against ER Index (y) plane, both axes 0 to 1 "
       "in tenths, drawn as polylines with markers and labelled at their two ends only: 2003 and "
       "2012. The legend is OUTSIDE at the right and names the five countries with marker samples - "
       "China, America, Nepal, France, South Africa - with no year key. Two dashed ideal-direction "
       "rays and one solid diagonal run from the origin corner to S. America's path is drawn at the "
       "far right near ER 0.15 with the theta annotation inside it, and its two end labels both "
       "print '2012' while its 2003 label sits over the trajectory; Nepal's path runs from the "
       "upper left down to 0.52; China's and France's overlap in the middle band around SE 0.45. "
       "The picture is the only one on the paper with an outside legend.",
       geometry("line", legend="outside-right", labels=True))

# ------------------------------------------------------------------- p14 Figure 5 and 6
figure(14, 1, "5", "line",
       caption(q("Figure 5 Profile of Nepalese development", 14)),
       "text-layer",
       cited(14, 14, ["Figure 5"], 1, "Figure 5 shows the Nepalese development from 2003 to 2012."),
       "vector", SEC_41,
       "Nepal's ten-year trajectory alone in the same SE/ER plane as Figure 4: ten diamond markers "
       "joined by a plain line, an outside-right legend with the single entry 'Nepal', y titled ER "
       "Index from 0.60 to 0.80 in 0.02 steps, x titled SE Index with only three ticks printed "
       "(0.1, 0.15, 0.2). The path jumps at the third point - a sharp spike up to 0.76 and back "
       "down to 0.71 - and then falls steadily to 0.62, which is the paper's evidence for "
       "environmental deterioration. The x axis is squeezed into three ticks over a decimal-second "
       "range while the y axis is printed to two decimals, so the two axes carry different "
       "precision.",
       geometry("line", legend="outside-right", labels=True),
       section_kind="result")
figure(14, 2, "6", "line",
       caption(q("Figure 6 Forecast GDP (per capita) from ARIMA(0,1,0)", 14)),
       "text-layer",
       cited(14, 14, ["Figure 6"], 1,
             "we show the forecast result of GDP (per capita) in Figure 6."),
       "vector", SEC_41,
       "The ARIMA forecast of GDP per capita: a thin black line for the observed years up to about "
       "year 11, then a blue forecast line rising roughly linearly to year 30, wrapped in two "
       "nested confidence bands - a light blue inner band and a grey outer one. The prose, not the "
       "picture, is the key: the grey band is the 0.8 confidence level and the light blue the 0.95, "
       "and neither is labelled in the plot. The x axis is ticked every five years from 0 to 30 "
       "with no title and no unit, and the y axis carries the index values with no title either, so "
       "the quantity the band is drawn around is only named in the caption.",
       geometry("line", numbers=True),
       section_kind="result")

# ------------------------------------------------------------------- p16 Figure 7, two panels
FIG7_NOTE = (
    "One of the two panels of Figure 7, pasted as its own bitmap. Both panels are column charts "
    "over the same twenty-two index numbers on x (1 to 22, no axis title) with a single-entry "
    "outside-right legend reading 'Sensitivity'. Neither axis is titled and neither panel names "
    "the quantity it plots, so the two panels are distinguishable only by their y range - the "
    "upper one 0 to 0.0015 with 0.0005 steps, the lower one 0 to 0.005 with only its two end "
    "ticks printed. The bars are plain blue columns with no error bars, several of them at exactly "
    "zero, so a quarter of the index list reads as 'no effect' rather than 'not tested'."
)
figure(16, 1, "7", "bar",
       caption(q("Figure 7 Sensitivity of each index", 16)),
       "text-layer",
       cited(15, 16, ["Figure 7"], 1,
             "and Figure 7 shows the result of each index."),
       "vector", SEC_421,
       FIG7_NOTE + " This is the upper panel, whose tallest bar reaches about 0.001 at index 6.",
       geometry("bar", legend="outside-right", numbers=True),
       section_kind="sensitivity")
figure(16, 2, "7", "bar",
       caption(q("Figure 7 Sensitivity of each index", 16)),
       "text-layer",
       cited(15, 16, ["Figure 7"], 1,
             "and Figure 7 shows the result of each index."),
       "vector", SEC_421,
       FIG7_NOTE + " This is the lower panel, whose tallest bar reaches about 0.0035 at index 4; it "
       "is the panel the plan's four chosen indices (4, 2, 19/7, 10/11/12) actually come from.",
       geometry("bar", legend="outside-right", numbers=True),
       section_kind="sensitivity")

# ------------------------------------------------------------------- p18 Figure 8
figure(18, 2, "8", "flowchart-or-schematic",
       caption(q("Figure 8 System dynamics of development", 18)),
       "text-layer",
       cited(17, 18, ["Figure 8"], 1,
             "We design the dynamic system for our indices and show the relationship between these "
             "indices in Figure 8."),
       "vector", SEC_51,
       "The system dynamics diagram in full: three dotted cluster boxes - Society (orange, top, ten "
       "boxes), Economic (blue, lower left, five boxes), Environment & Resources (green, lower "
       "right, eight boxes) - joined by right-angled arrows, each arrow annotated with a PLUS or "
       "MINUS at its endpoint or mid-segment. The Society cluster holds school enrollment, adjusted "
       "savings for education, electricity access, telephone lines, labour force participation, "
       "population, community health workers, crude death rate, food production index and crude "
       "birth rate; Economic holds GDP per capita, services, industry, manufacturing and "
       "agriculture value added; Environment holds the three freshwater withdrawal series, "
       "agricultural land, road-sector energy, combustible renewables, CO2 and nitrous oxide. No "
       "axis, no scale, no number, no legend - the polarity signs are the only key and nothing on "
       "the page explains them. A dense bus of parallel connectors crosses the middle band, several "
       "arrows leave a cluster and re-enter the same cluster without a visible arrowhead, and the "
       "three sub-graphs are pasted bitmaps inside the outer drawing, which is why the region pass "
       "measures them separately.",
       geometry("flowchart-or-schematic", numbers=False))

# ------------------------------------------------------------------- p19 Figures 9 and 10
figure(19, 1, "9", "line",
       caption(q("Figure 9 Comparison to ARIMA model without intervention", 19)),
       "text-layer",
       cited(19, 19, ["Figure 9"], 1, "in one coordinate system in Figure 9."),
       "vector", SEC_52,
       "Two series in one coordinate frame: the blue diamond-marked 'Simulation' and the dark red "
       "square-marked 'Time Series', both falling steeply from about (0.10, 0.79) to the middle of "
       "the window and then flattening near 0.56. Legend is OUTSIDE at the right. Neither axis is "
       "titled and neither carries a unit: x is ticked 0.08 to 0.33 in 0.05 steps and y 0.55 to "
       "0.80 in 0.05 steps, and only horizontal gridlines are drawn. The Simulation series stops at "
       "about 0.31 while the Time Series runs on to 0.33.",
       geometry("line", legend="outside-right", labels=False),
       section_kind="solution")
figure(19, 2, "10", "line",
       caption(q("Figure 10 Simulation results of three programs compared with no intervention", 19)),
       "text-layer",
       cited(19, 19, ["Figure 10"], 1,
             "in the same coordinate system in Figure 10"),
       "vector", SEC_52,
       "The same frame as Figure 9 with four series instead of two - purple x-marked 'No change', "
       "blue diamond 'Economic Aid', dark red square 'Education Program', green triangle "
       "'Modernization Program' - legend OUTSIDE at the right. All four track nearly on top of one "
       "another down to 0.59-0.62 and only separate after about x = 0.20, so the three programmes "
       "are visually indistinguishable over most of the window; the separation the paper's "
       "conclusion rests on lives in the last third. Four near-vertical dashed drop lines carry the "
       "terminal markers down to a row of points at about 0.66 whose meaning is not stated anywhere "
       "in the picture. Same missing axis titles and units as Figure 9.",
       geometry("line", legend="outside-right", labels=False),
       section_kind="solution")


# ------------------------------------------------------------------- tables
TABLES: list[dict] = []


def table(page: int, reg: int, cap: dict, cap_src: str, mention: dict, section: list[str],
          note: str, rows: int, cols: int, numeric: int, text: int, rule: str,
          header_rows: int = 1, merged: bool = False, zebra: bool = False,
          diagonal: bool = False, units_in_header: bool = False, decimal: bool = False,
          continued: bool = False, width: str = "full", section_kind: str = "model",
          note_sentence: str = "", confidence: str = "high") -> None:
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": "vector",
        "caption_source": cap_src, "caption_verbatim": cap["verbatim"], "caption": cap,
        "place": place(page, reg, section_kind, section),
        "mention": mention, "note": note, "confidence": confidence,
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": units_in_header,
                  "decimal_aligned": decimal, "numeric_cols": numeric, "text_cols": text,
                  "width": width, "orientation": "portrait", "continued": continued,
                  "note_sentence": note_sentence},
        "family": "table-grid",
    })


table(12, 2,
      caption(q("Table 2 Sustainable Distance of five countries from 2003 to 2012", 12),
              numbering="Table N", position="below"),
      "text-layer",
      cited(12, 12, ["Table 2"], 1,
            "by calculating the sustainable distance of each country (Table 2)"),
      SEC_333,
      "The table is transposed: the five countries run across the top as the header row and the "
      "single measure, 'Sustainable Distance', runs down as one data row, so a reader looking for a "
      "ranking has to read sideways. Six printed columns, one text and five numeric to six "
      "decimals. Ruled only horizontally - a double rule above the header and another under the "
      "data row - with no vertical strokes. Two values are printed in RED (China 1.401829 and Nepal "
      "1.114179) and nothing on the page says what red means; the prose's threshold is only that "
      "the distance must be under D_0, which the table never prints.",
      rows=1, cols=6, numeric=5, text=1, rule="booktabs",
      section_kind="model")

table(15, 1,
      caption(q("Table 3 Effective indices list", 15), numbering="Table N", position="below"),
      "text-layer",
      cited(15, 15, ["Table 3"], 1,
            "we obtain the effective indices list for Nepal (2003~2012) in Table 3"),
      SEC_421,
      "Three rows of number-name pairs read across nine cells: 16 CO2 emissions, 4 education "
      "expenditure, 19 access to electricity; 7 Technology index, 2 GINI coefficient, 12 Services "
      "(added); 10 Industry (added), 11 Manufacturing (added) and an empty cell. The grey cells hold "
      "the index numbers and each of them is closed by vertical strokes, so the grid reads as nine "
      "little boxes rather than three ranked rows. The list is printed in index order, not in "
      "sensitivity order, although the prose introduces it as a ranking by difference quotient; the "
      "last cell is blank because nine indices do not fill three rows of three. The grid prints NO "
      "header row at all - header_rows is recorded as 1 only because the schema has no zero.",
      rows=3, cols=6, numeric=3, text=3, rule="boxed",
      section_kind="sensitivity")

table(16, 3,
      caption(q("Table 4 Possible proposal trade-off", 16), numbering="Table N", position="below"),
      "text-layer",
      cited(16, 16, ["Table 4"], 1,
            "the draw a decision on possible solution in Table 4."),
      SEC_422,
      "Five candidate directions against five judgement columns: Possible Direction, a merged "
      "'Actual Requirement' band over Cost / Political stability / Resource, then Demands and "
      "Decision. Five body rows, every cell a word rather than a number, two-line header with one "
      "merged band. Ruled horizontally only. The Decision column is colour-coded green for Accepted "
      "and red for the one Rejected row, with no legend and no key; the missing Resource judgement "
      "for two rows prints as a bare hyphen with no footnote.",
      rows=5, cols=5, numeric=0, text=5, rule="booktabs", header_rows=2, merged=True,
      section_kind="evaluation")

table(18, 5,
      caption(q("Table 5 Estimated equations of each subsystem", 18), numbering="Table N",
              position="below"),
      "text-layer",
      cited(17, 18, ["Table 5"], 1, "The parameter estimation result is showed in Table 5"),
      SEC_51,
      "Three columns headed Economic Subsystem, Society Subsystem and Environment & Resources "
      "Subsystem, holding five, ten and eight estimated equations respectively - the columns do not "
      "share rows, so the printed grid is a sheet of three independent lists rather than a table "
      "with records. Rules above the header and below the last row only, nothing between rows. "
      "Every equation is linear in its regressors with coefficients to four decimals: I = -4.1019 + "
      "0.0804 CRW, M = -31.7202 + 0.3703 LFPR + 0.0949 RSEC, POP = POP/1000 (BR - DR), NOE = 1858.4 "
      "- 14.3 CRW, and so on. Long equations wrap onto continuation lines with no hanging indent, "
      "so an equation can read as two rows; the wrapped lines in the environment column carry a "
      "small negative indent that reads as misalignment.",
      rows=10, cols=3, numeric=0, text=3, rule="booktabs",
      section_kind="model")

table(20, 1,
      caption(q("Table 6 Sustainable distance of each proposal (every five year)", 20),
              numbering="Table N", position="below"),
      "text-layer",
      cited(19, 20, ["Table 6"], 1, "of every five year in Table 6."),
      SEC_52,
      "Four proposals down against the years 2015, 2020, 2025 and 2030 across: No Intervention "
      "0.852894 / 0.984006 / 0.964756 / 0.29873; Economic Aid 0.853072 / 0.984272 / 0.965149 / "
      "0.299622; Education Program 0.852192 / 0.982975 / 0.96332 / 0.294641; Modernization Program "
      "0.848138 / 0.977041 / 0.955021 / 0.272045. Five printed columns, four numeric, ruled "
      "horizontally only. The four proposals differ in the fourth decimal place in every year "
      "except 2030, where the last column switches between five and six decimals and the "
      "differences are still under 0.03, so the table cannot support a ranking on the evidence it "
      "prints; the caption's 'every five year' is the paper's own grammar.",
      rows=4, cols=5, numeric=4, text=1, rule="booktabs",
      section_kind="solution")

RULES = [
    "Measure first, then read the pixels: nineteen measured regions resolve into eleven figure "
    "rows, five table rows and three exclusions, with nothing unaccounted [place.area_frac].",
    "A drawing whose sub-graphs are pasted as separate bitmaps counts once: the 0.29-area vector "
    "region on p18 holds the whole of Figure 8, and the three raster pieces inside it repeat "
    "clusters that are already in that drawing, so they are excluded as duplicates rather than "
    "recorded as further rows [place.area_frac].",
    "Two measured panels under one printed caption are two rows with one shared verbatim: Figure 7 "
    "prints its sensitivity bars in an upper and a lower panel, pasted apart, and both rows carry "
    "'Figure 7 Sensitivity of each index' [caption.verbatim].",
    "A caption that prints no colon is numbered 'Figure N' or 'Table N' and not 'Figure N:'; every "
    "caption on this paper is set that way [caption.numbering].",
    "A caption printed under the data rows is position 'below' even when the words precede the "
    "grid in the text layer's own reading order, as Table 2's does [caption.position].",
    "A construction with real index axes is line even when it plots almost nothing: Figure 2 draws "
    "rays and an angle in the SE/ER plane with both axes ticked, so it takes the plot families "
    "[geometry.family].",
    "A construction with no axes and no data is other, and it is the only other row on the paper: "
    "Figure 3 is five grey rays, one red ideal ray and four angle labels, set in the model section "
    "rather than beside the results [place.section_kind].",
    "A tree of labelled boxes and circles is flowchart-or-schematic, and the four-level index "
    "system of Figure 1 is that family with no numbers anywhere [geometry.family].",
    "An outside legend is recorded as outside-right and not as inside: Figures 4, 5, 9 and 10 and "
    "both Figure 7 panels carry their key to the right of the plot, which is the only legend "
    "placement this paper uses [geometry.legend].",
    "A chart whose axes print no titles is recorded with printed_numbers true and the missing "
    "titles named in the note: Figures 9 and 10 print tick values on both axes and no axis titles "
    "at all [geometry.printed_numbers].",
    "A confidence band keyed only by prose is legend 'none': Figure 6's grey and light blue bands "
    "are named in the sentence above the figure and nowhere in the art [geometry.legend].",
    "Rows are counted as printed and columns physically: Table 2 prints one data row across five "
    "country columns, Table 3 prints three rows of number-name pairs in nine cells, Table 5 prints "
    "three unrelated lists side by side [table.rows].",
    "A merged band over a group of judgement columns makes merged_cells true even when no cell "
    "spans two rows, as Table 4's 'Actual Requirement' header does [table.merged_cells].",
    "A grid whose only rules are horizontal is booktabs, and a grid whose small cells are each "
    "closed by vertical strokes is boxed: Table 3's grey index cells are the only boxed grid here "
    "[table.rule_style].",
    "A colour code printed with no key is recorded as a defect, not as a legend: Table 2's two red "
    "distances and Table 4's red and green decisions both carry their meaning only in prose "
    "[table.zebra].",
    "An exhibit first named on an earlier page takes a positive lead_pages: Figure 7 and Table 5 "
    "are both named a page before they print, and Table 6 a page before its grid [mention.lead_pages].",
    "An exhibit whose pointer sits a page after the art takes a negative lead_pages: Figure 2 is "
    "printed on p10 and first named on p11 as '(Figure 2)' [mention.lead_pages].",
    "A pointer written parenthetically is recorded with lead_pattern parenthetical and the "
    "parenthesised spelling quoted as printed [mention.lead_pattern].",
]

NOTE = """Paper 88, Team 38996. Nineteen measured regions over nine of the twenty-one pages, all
nineteen accounted for: eleven figure rows, five table rows, three exclusions, so unaccounted is
zero and nothing is left unresolved. The paper numbers ten figures and six tables; Table 1, the
"process of calculation of weighting process", prints on p9 as a run of text with no rules, owns no
measured region at all, and is declared as a gap rather than invented.

The one structural finding is on p18. Figure 8 is a single system-dynamics diagram - three dotted
cluster boxes labelled Society, Economic and Environment & Resources, twenty-three boxes in all,
joined by arrows carrying plus and minus polarity signs - but the region pass measures FOUR regions
there, because the three sub-graphs are pasted as their own bitmaps inside the outer vector drawing.
The 0.29-area vector region holds the whole diagram and is the exhibit; the three raster pieces
repeat clusters already inside it, so they are excluded as duplicates. That is the first time in
this lane that a single figure arrives as one drawing wrapped around three copies of itself.

What the pictures show, read off the crops. Figure 1 is the index system as a four-level tree,
ending in circles that break every indicator name mid-word and printing "Education" twice as a
Level 2 box. Figure 2 and Figure 3 are the same idea twice: the first is a construction in the
SE/ER plane with both axes ticked only at 0 and 1, one red ideal ray, one black actual vector, a
theta arc, four year markers 2009-2012 squeezed into an unreadable cluster, and rotated ray labels
that collide with the arc; the second throws the axes away and keeps only the rays and the angle.
Figures 4 and 5 are country trajectories in that plane with the legend outside at the right, and
the paper labels each path with 2003 and 2012 only, printing "2012" twice inside America's. Figure 6
is an ARIMA forecast whose two confidence bands are keyed only in the sentence above it.

Figures 7, 9 and 10 are the paper's quantitative evidence and they are thin: Figure 7 is two pasted
column charts over the same twenty-two index numbers with different y windows, neither axis titled,
and about a quarter of the bars at exactly zero; Figures 9 and 10 share an axis frame with no axis
titles and no units at all, Figure 9 puts two series in it and Figure 10 four, and in Figure 10 the
four programmes sit on top of each other until the last third of the window, which is where the
paper's conclusion is supposed to come from.

The tables are where the paper's arithmetic is legible, and where its labels fail. Table 2 is
transposed - countries across, one measure down - and prints two distances in red with no key.
Table 3 is nine little grey boxes in three rows in index order though the prose calls it a ranking,
with the last cell empty and no header row. Table 4 carries the plan's judgement in five words per
row and colours the one rejection red with no legend. Table 5 is three unrelated lists of estimated
equations side by side, five and ten and eight of them, wrapping onto unindented continuation
lines. Table 6 compares four proposals whose distances agree to the fourth decimal place in three
of the four years, so the ranking it is meant to support is not visible in its own numbers.

Citation is regular on this paper, which is worth recording because it is unusual here: every
numbered figure and every measured table is named in the prose. Figure 7 and Table 5 are named a
page before they print, Table 6 a page before its grid, and Figure 2 is named a page after it -
once, parenthetically - while Tables 2, 3 and 4 and Figures 1, 3, 4, 5, 6, 8, 9 and 10 are named on
their own pages. The one grid never mentioned is Table 1, the one grid with no measured region."""

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT.get("layout_sha256") or LAYOUT.get("sha256", ""),
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": 18, "bbox": REG[(18, 1)], "reason": "duplicate",
         "note": "Society cluster pasted as its own bitmap inside Figure 8: box for box the same "
                 "sub-graph already drawn in the p18 r2 vector region."},
        {"page": 18, "bbox": REG[(18, 3)], "reason": "duplicate",
         "note": "Economic cluster pasted as its own bitmap inside Figure 8: the same five value-"
                 "added boxes already drawn in the p18 r2 vector region."},
        {"page": 18, "bbox": REG[(18, 4)], "reason": "duplicate",
         "note": "Environment & Resources cluster pasted as its own bitmap inside Figure 8: the "
                 "same eight boxes already drawn in the p18 r2 vector region."},
    ],
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc88-payload.json"
out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "rules", len(RULES))
print("wrote", out)
