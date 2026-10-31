"""Hand census of P-D-2015-35780-97fea85b (Team 35780, 24 pages, 21 measured regions).

Fourteen figure rows, six table rows, one excluded region, no unaccounted region. The paper prints
fourteen numbered figures and seven numbered tables; Table 2 prints on p9 as a text-only grid with
no rules, so it owns no measured region and is declared as a gap rather than invented.

  p1  r1  (unnumbered) not-an-exhibit          summary-sheet fill-in rules, excluded
  p4  r1  Fig.1   flowchart-or-schematic       Social / Environment / Economic cycle
  p6  r1  Table 1 table-grid                   the Level1/Level2/Level3 indicator system
  p9  r1  Fig.2   heatmap-or-contour           the 3x3 GE-Matrix, shaded cells I-IX
  p11 r1  Table 3 table-grid                   2013 sustainability rankings, ten countries
  p12 r2  Fig.3   line                         nine forecast curves, three countries
  p12 r1  Fig.4   line                         three state-space trajectories, 2009-2029
  p13 r2  Fig.5   flowchart-or-schematic       closed loop before the plan
  p13 r1  Fig.6   flowchart-or-schematic       the same loop with U_ba and G_cA
  p14 r1  Table 4 table-grid                   plan effects according to c_i and alpha_ij
  p16 r1  Table 5 table-grid                   eighteen development activities and scores
  p17 r1  Fig.7   line                         DI against c_1 at five offsets
  p17 r2  Fig.8   line                         DI against every b_i at +-2/4 per cent
  p17 r4  Fig.9   line                         DI against every c_i at +-5 per cent
  p17 r3  Fig.10  line                         DI against every b_i at +-2 per cent
  p18 r2  Fig.11  line                         forecasts of Congo with and without a plan
  p18 r1  Fig.12  line                         the same forecasts in the CI/DI plane
  p18 r3  Table 6 table-grid                   the six activities of the plan
  p19 r1  Table 7 table-grid                   the four-period control scheme
  p20 r1  Fig.13  line                         forecast under external perturbation
  p21 r1  Fig.14  line                         D_12 against eta, three series

Three printed faults shape this record. The four two-column exhibits on pp12, 13, 17 and 18 have
their captions interleaved by the text layer ("Figure 3: Forecast on comprehensive Figure 4: The
GE-Matrix for sustainability of performances of three countries three countries"), so those eight
captions are typed from the crops. Table 2 is printed and cited twice but rules nothing, so it is
invisible to the region pass. And Figure 14's caption promises a two-dimensional concentration
distribution while the art draws a one-dimensional profile.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2015-35780-97fea85b"
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


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below",
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
# Typed from the printed lines: the heading index of this paper returns 39 entries with null text
# and top 0, so nothing here could be looked up. `check_place` accepts a printed line as a heading.
SEC_INTRO = ["Introduction 1"]
SEC_31 = ["3.1 Sustainable Development Indicators (SDI)"]
SEC_324 = ["3.2.4 A GE-Matrix to Score Sustainability"]
SEC_341 = ["3.4 Results", "3.4.1 Country Rankings"]
SEC_342 = ["3.4 Results", "3.4.2 A 20-Year Forecast"]
SEC_411 = ["4.1 Adding Control into the State Equation",
           "4.1.1 Direct and Indirect Control Matrices"]
SEC_43 = ["4.3 Development Activities in Practice"]
SEC_441 = ["4.4 A Case Study on Congo", "4.4.1 Adjusting Control Elements"]
SEC_442 = ["4.4 A Case Study on Congo", "4.4.2 20-year Forecasts with(out) Plan-controlling"]
SEC_443 = ["4.4 A Case Study on Congo", "4.4.3 The Plan in Practice"]
SEC_52 = ["External Effects 5", "5.2 A Revised Forecast on Congo"]
SEC_6 = ["Stability Analysis 6"]

for _label in [p for group in (SEC_INTRO, SEC_31, SEC_324, SEC_341, SEC_342, SEC_411, SEC_43,
                               SEC_441, SEC_442, SEC_443, SEC_52, SEC_6) for p in group]:
    if schema.norm(_label) not in schema.printed_lines(PID):
        raise SystemExit(f"section label is not a printed line: {_label!r}")

ITEMS: list[dict] = []


def figure(page: int, reg: int, number: str, family: str, cap: dict, cap_src: str,
           mention: dict, kind: str, section: list[str], note: str,
           geo: dict | None = None, confidence: str = "high",
           section_kind: str = "model") -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": kind, "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap["verbatim"],
        "caption": cap, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    })


# ------------------------------------------------------------------- p4 Figure 1
figure(4, 1, "1", "flowchart-or-schematic",
       caption(q("Figure 1: Three aspects in SDI system", 4)),
       "text-layer",
       cited(3, 4, ["Figure 1"], 1, "as shown in Figure 1."),
       "raster", SEC_INTRO,
       "Three thick curved arrows closing a ring around a solid centre disk lettered 'Sustainable "
       "development', with the three sector labels set outside the ring: Social at the left, "
       "Environment at the upper right, Economic at the foot. The disk carries a faint checkered "
       "fill and the arrows a dotted fill, so the three aspects are distinguished by position only. "
       "No axis, no scale, no number, no legend box - the labels are drawn straight onto the "
       "picture. Drawn as one pasted bitmap, and its cycle direction is only half stated: two arcs "
       "carry arrowheads and the left arc carries none, so a reader cannot tell whether the ring "
       "runs clockwise or not at all.",
       geometry("flowchart-or-schematic", legend="inside", numbers=False),
       section_kind="introduction")

# ------------------------------------------------------------------- p9 Figure 2
figure(9, 1, "2", "heatmap-or-contour",
       caption(q("Figure 2: A GE-Matrix to evaluate Develop- ment Index and Coordination Index", 9),
               variables=2),
       "text-layer",
       cited(9, 9, ["Figure 2"], 1, "Figure 2[12] shows the matrix we adopt."),
       "raster", SEC_324,
       "The GE-Matrix as a three-by-three block of shaded cells, each block subdivided by a faint "
       "ten-by-ten lattice and numbered I to IX in reading order from the bottom left, with thin "
       "divider lines overlaid at the middle in both directions so the nine regions are drawn twice "
       "- once by fill, once by the numerals. Cells are filled green, pale blue, grey and olive, four "
       "classes, and nothing on the page keys the four fills to a level. Axes are real and number: "
       "Coordination Index (CI) across 0.00 to 1.00 in tenths with full-width parentheses as printed, "
       "Development Index (DI) up 0.10 to 1.00 in tenths, tick numerals set in blue. The numerals sit "
       "half a cell off the shaded blocks they are supposed to name, so the picture's own two "
       "encodings of the same nine regions disagree.",
       geometry("heatmap-or-contour", numbers=True))

# ------------------------------------------------------------------- p12 Figure 3
figure(12, 2, "3", "line",
       caption("Figure 3: Forecast on comprehensive performances of three countries"),
       "typed-from-crop",
       cited(12, 12, ["Figure 3", "Figures 3-4"], 2,
             "In Figure 3, comprehensive performances on environmental, social and economic aspects "
             "of the"),
       "raster", SEC_342,
       "Nine smooth curves over Year, the three aspects of three countries labelled at their right "
       "ends only - US(Fso), US(Fec), US(Fen), China(Fec), China(Fso), China(Fen), Congo(Fen), "
       "Congo(Fso), Congo(Fec) - with no colour swatches and no key for the en/so/ec shorthand. The "
       "y axis is titled Index and runs 0.00 to 0.50, the x axis Year from 2015 to 2035 in fives. "
       "China(Fec) and US(Fen) labels collide near 0.40, and the three Congo curves are drawn "
       "almost on top of each other near 0.05, so two of the nine series cannot be followed at all. "
       "The caption is typed from the crop because the text layer interleaves it with Figure 4's.",
       geometry("line", legend="inside", labels=True))

# ------------------------------------------------------------------- p12 Figure 4
figure(12, 1, "4", "line",
       caption("Figure 4: The GE-Matrix for sustainability of three countries"),
       "typed-from-crop",
       cited(12, 12, ["Figure 4", "Figures 3-4"], 2,
             "A comprehensive view of our 20-year prediction is shown in Figure 4 under the frame of "
             "a GE-Matrix."),
       "raster", SEC_342,
       "A state-space diagram rather than a forecast: three straight two-point trajectories in the "
       "Coordination Index (x) against Development Index (y) plane, red circle for the US, green "
       "triangle for China, blue triangle for Congo, each a single segment joined 2009 to 2029 with "
       "a boxed key inside the upper left of the plot. Both axes run 0.0 to 1.0 in tenths. The only "
       "dates printed are the two endpoints - there is no time axis, no arrow showing which way the "
       "trajectory runs, and dashed gridlines partly cover the Congo path.",
       geometry("line", legend="inside", labels=True))

# ------------------------------------------------------------------- p13 Figure 5 and 6
FIG5_NOTE = (
    "The control loop drawn as a block diagram before the plan: the input U-hat into block B, the "
    "summing junction marked only with '+', the planned matrix F', the integrator box, the output F, "
    "and the feedback path F through A back into the summing junction. Nine boxes and arrows, no "
    "axis, no scale, no number. Two printed faults: the summing junction shows a plus sign but no "
    "sign on any input, so the paper's subtraction of the feedback is invisible; and the region's "
    "right edge cuts the final F label and the start of the next symbol, because the two panels were "
    "pasted as separate bitmaps at column width."
)
figure(13, 2, "5", "flowchart-or-schematic",
       caption("Figure 5: Flowchart of F’s change before executing the plan"),
       "typed-from-crop",
       cited(13, 13, ["Figures 5-6"], 1,
             "Figures 5-6 are ﬂowcharts of change of F before and after executing the plan."),
       "raster", SEC_411,
       FIG5_NOTE + " This is the left half, before the plan.",
       geometry("flowchart-or-schematic", numbers=False))
figure(13, 1, "6", "flowchart-or-schematic",
       caption("Figure 6: Flowcharts of F’s change after executing the plan"),
       "typed-from-crop",
       cited(13, 13, ["Figures 5-6"], 1,
             "Figures 5-6 are ﬂowcharts of change of F before and after executing the plan."),
       "raster", SEC_411,
       FIG5_NOTE + " This is the right half, after the plan, and it differs in exactly two ways: a "
       "second input U_ba enters the summing junction from above, and the control matrix G_cA is "
       "inserted into the feedback path between A and the junction. The plus sign still carries no "
       "polarity beyond itself, and the two subscripts are set differently in the same picture "
       "(U_ba inline, G_cA as a true subscript).",
       geometry("flowchart-or-schematic", numbers=False))

# ------------------------------------------------------------------- p17 Figures 7-10
FIG_SERIES = (
    "Five smooth curves drawn in a common crossing near 2012-2013 and labelled inline at their "
    "right ends; no legend box anywhere, so curve identity depends on those end labels alone. The y "
    "axis is titled Development Index(DI) and the x axis Year."
)
figure(17, 1, "7", "line",
       caption("Figure 7: Effects on Congo’s DI when c1 changes"),
       "typed-from-crop",
       cited(17, 17, ["Figures 7-8", "Figures 7-10"], 2,
             "Figures 7-8 indicates effects c1 and b1 have on the Development Index when c1 changes "
             "±5% and ±10% and when b1 changes ±2% and ±4%."),
       "raster", SEC_441,
       FIG_SERIES + " here the five end labels read C_1+10%, C_1+5%, C_1, C_1-5% and C_1-10%, and "
       "all five curves lie on top of one another until about 2015, so four of the five offsets are "
       "invisible over the first third of the window. Y runs 0.0260 to 0.0270 in steps of 0.0002. "
       "One printed defect: the y title of this panel reads 'Development Index(DJ)', a J where the "
       "other three panels print I.",
       geometry("line", legend="inside", labels=True))
figure(17, 2, "8", "line",
       caption("Figure 8: Effects on Congo’s DI when b1 changes"),
       "typed-from-crop",
       cited(17, 17, ["Figures 7-8", "Figures 7-10"], 2,
             "Figures 7-8 indicates effects c1 and b1 have on the Development Index when c1 changes "
             "±5% and ±10% and when b1 changes ±2% and ±4%."),
       "raster", SEC_441,
       FIG_SERIES + " here the labels read b_i+4%, b_i+2%, b_i, b_i-2% and b_i-4%, and the fan is "
       "the flattest of the four: the curves barely separate and the top one is labelled outside the "
       "axis area. Y runs 0.022 to 0.032, a different window from Figure 7's, so the four panels of "
       "this pair are not on a common scale. The caption names b1 while the picture varies every b_i.",
       geometry("line", legend="inside", labels=True))
figure(17, 4, "9", "line",
       caption("Figure 9: Effects on Congo’s DI when ci changes ±5%"),
       "typed-from-crop",
       cited(17, 17, ["Figures 9-10", "Figures 7-10"], 2,
             "From Figures 9-10, clear comparisons among indirect control elements"),
       "raster", SEC_441,
       FIG_SERIES + " here seven labels are printed for five or six curves - C_1+5%, C_1-5%, "
       "C_3+5%, C_3-5%, C_2+5%, C_2-5% and 'no change' - and the two C_2 labels are set in the middle "
       "of the plot on top of the curve bundle rather than at the ends, so no curve can be matched to "
       "them. This is the only panel of the four where the curves visibly cross, around 2014-2016, "
       "and where the top curve turns back up after 2019. Y runs 0.0260 to 0.0270 like Figure 7.",
       geometry("line", legend="inside", labels=True))
figure(17, 3, "10", "line",
       caption("Figure 10: Effects on Congo’s DI when bi changes ±2%"),
       "typed-from-crop",
       cited(17, 17, ["Figures 9-10", "Figures 7-10"], 2,
             "From Figures 9-10, clear comparisons among indirect control elements"),
       "raster", SEC_441,
       FIG_SERIES + " here seven curves run with labels b_1+2%, b_3+2%, b_2+2%, 'no change', "
       "b_2-2%, b_3-2% and b_1-2%, and the ordering is not monotonic: the green b_2+2% curve sits "
       "between the rising and falling groups. Y runs 0.024 to 0.029, another window. A stray "
       "fragment of a legend or tick string bleeds into the left edge of the region outside the "
       "plot box.",
       geometry("line", legend="inside", labels=True))

# ------------------------------------------------------------------- p18 Figures 11-12
figure(18, 2, "11", "line",
       caption("Figure 11: Forecasts of Congo on performance with(out) a plan"),
       "typed-from-crop",
       cited(18, 18, ["Figure 11", "Figures 11-12"], 2,
             "In Figure 11, full lines are predictions of performances with a plan; dotted lines are "
             "those without a plan."),
       "raster", SEC_442,
       "Six forecast series over Year 2014 to 2033: two solid curves rising from about 0.02 to 0.40 "
       "and 0.37, and four near-flat curves hugging 0.01 to 0.07 whose end labels - F_en, F_so, "
       "F_ec - stack on top of one another, so the without-plan half of the comparison is drawn but "
       "not readable. The with-plan half is labelled F_sc(plan), F_en(plan), F_ec(plan). Y is titled "
       "Development Index(DI) 0.00 to 0.45, x Year ticked every four years, and a second rotated DI "
       "title from the neighbouring panel bleeds in at the right edge.",
       geometry("line", legend="inside", labels=True))
figure(18, 1, "12", "line",
       caption("Figure 12: Forecasts of Congo with(out) a plan shown in the GE-Matrix"),
       "typed-from-crop",
       cited(18, 18, ["Figure 12", "Figures 11-12"], 2,
             "Ac- cording to Figure 12, the development direction is a complete changeover after "
             "adding a plan."),
       "raster", SEC_442,
       "The same comparison as Figure 11, re-drawn as trajectories in the Coordination Index (x) "
       "against Development Index (y) plane, both axes 0.0 to 1.0 in tenths, with a key inside the "
       "upper left: green dashed squares 'no plan', blue solid circles 'with plan'. The with-plan "
       "path starts near (0.37, 0.02) and bends up and left to about (0.50, 0.57); the no-plan path "
       "lies flat along the bottom and collapses onto the baseline at this scale. No year axis, no "
       "direction arrows, and the year labels the paper relies on sit in the prose, not in the art.",
       geometry("line", legend="inside", labels=True))

# ------------------------------------------------------------------- p20 Figure 13
figure(20, 1, "13", "line",
       caption(q("Figure 13: Forecasts of Congo on performances with external perturbation", 20)),
       "text-layer",
       cited(19, 20, ["Figure 13"], 2,
             "And a new forecast result of Congo after adding external perturbation inﬂuences are "
             "shown in Figure 13."),
       "raster", SEC_52,
       "Three jagged series rising over Year 2015 to 2030 with step-like high-frequency jitter, "
       "labelled F_so, F_en and F_ec at their right ends and drawn red, black and blue. The y axis "
       "carries no quantity name at all - it is titled only 'Item' - and runs 0.0 to 0.4. The caption "
       "promises external perturbation and the picture draws no perturbation event, no marker and no "
       "reference line, so the fluctuation the caption attributes to noise is indistinguishable from "
       "the integer rounding already visible in Table 7.",
       geometry("line", legend="inside", labels=True),
       section_kind="result")

# ------------------------------------------------------------------- p21 Figure 14
figure(21, 1, "14", "line",
       caption(q("Figure 14: Two dimensional concentration distribution under Gaussian model", 21)),
       "text-layer",
       cited(20, 21, ["Figure 14"], 1,
             "sensitivity analysis result shown in Figure 14."),
       "raster", SEC_6,
       "D_12 plotted against eta on one axis: three series that each run down into a V and touch "
       "exactly zero at eta = 0 - black F_en, red F_so, blue F_ec - with a small legend inside the "
       "upper left. eta runs -0.3 to 0.3 in tenths, D_12 runs 0.00 to 0.12 in 0.02 steps, and each "
       "series is joined from about ten sample points with straight segments. The caption sells this "
       "as a two-dimensional concentration distribution under a Gaussian model; the art is a "
       "one-dimensional profile with a cusp, and the interpolation is too coarse to resolve a "
       "Gaussian at all. The legend spells the series Fen/Fso/Fec where the other forecast figures "
       "print F_en/F_so/F_ec.",
       geometry("line", legend="inside", labels=True),
       section_kind="sensitivity")


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


table(6, 1,
      caption(q("Table 1: Indicator system for sustainable development", 6), numbering="Table N:",
              position="above"),
      "text-layer", uncited(), SEC_31,
      "The indicator system, three columns headed Level1, Level2 and Level3, seventeen indicator "
      "rows. Environment covers the Population and Resources groups, Social covers Pullotion, Health, "
      "Education and Livelihood, Economic covers three indicators; the first two columns merge "
      "vertically over their groups, which is what makes seventeen rows read as a three-level tree. "
      "Three-line ruling with an extra rule between level-one groups and no vertical strokes. Printed "
      "faults: the group label for pollution arrives as 'Pullotion', 'Depth of the food deficit' is "
      "filed under Education, and the upper-left cell of the header carries no label for the Row "
      "column. The prose never names this table.",
      rows=17, cols=3, numeric=0, text=3, rule="booktabs", merged=True)

table(11, 1,
      caption(q("Table 3: 2013 Sustainability rankings of 10 countries", 11), numbering="Table N:",
              position="above"),
      "text-layer",
      cited(11, 11, ["Table 3"], 1, "The rankings are shown in Table 3."),
      SEC_341,
      "Ten ranked countries in eight printed columns - Rank, Country, Fen, Fso, Fec, DI, CI, Score - "
      "of which seven hold numbers and only Country holds text. Three-line ruling, nothing merged. "
      "Printed faults: the country names for ranks 4 and 10 are pushed out of their cells to the end "
      "of the text layer ('Nepal' and 'Congo' arrive after the last numeric row), the three "
      "performance headers lose their subscripts and print as Fen/Fso/Fec in roman, decimals are not "
      "aligned on the point, and the Score column rises with worse sustainability while neither the "
      "header nor the caption says which direction is good.",
      rows=10, cols=8, numeric=7, text=1, rule="booktabs")

table(14, 1,
      caption(q("Table 4: Effects of the plan according to ci and αij", 14), numbering="Table N:",
              position="above"),
      "text-layer",
      cited(14, 14, ["Table 4"], 1, "Properties of ci are shown in Table 4."),
      SEC_411,
      "A two-by-two statement of the plan's effect: a stub column headed alpha_ij<1 and alpha_ij>1 "
      "against two data columns headed c_i<1 and c_i>1, every cell a full sentence of text, no "
      "numbers anywhere. Three-line ruling; the caption's rule doubles as the table's top rule, and "
      "the upper-left header cell over the stub column is left empty. The two data headers are "
      "centred over very unequal column widths, so the columns do not read as a grid.",
      rows=2, cols=3, numeric=0, text=3, rule="booktabs")

table(16, 1,
      caption(q("Table 5: Development activities and their scores of effectiveness", 16),
              numbering="Table N:", position="above"),
      "text-layer",
      cited(15, 16, ["Table 5"], 2,
            "With the help of this research we can obtain Table 5 which reveals development "
            "activities and their score of effectiveness in"),
      SEC_43,
      "Eighteen development activities, each scored to two decimals, sorted under three group labels "
      "- environmental, social, economic - that are set once per block and never repeated, so the "
      "group is carried by position and a rule rather than by a column of its own. Three printed "
      "columns: group, activity, score. Booktabs top and header rules, a rule at each group break, "
      "and no vertical strokes. Printed faults: 'Transferring the obtrusive industries to the "
      "industrial towns' appears twice, once at 0.13 and once at 0.19; 'The reduction of air "
      "pollution' is filed under social while its near-double sits under economic; the longest "
      "entry runs to the edge of the score column; and 'No damaging to the protected areas' closes "
      "the environmental block after the group rule has already been drawn.",
      rows=21, cols=3, numeric=1, text=2, rule="booktabs", merged=True)

table(18, 3,
      caption(q("Table 6: Activities for plan on Congo’s sustainable development", 18),
              numbering="Table N:", position="above"),
      "text-layer",
      cited(18, 18, ["Table 6"], 1,
            "following development activities (selected from Table 5)are recommended in our plan "
            "(Shown in Table 6):"),
      SEC_443,
      "The six activities the plan actually adopts, in two printed columns: a recommended level "
      "numbered 1, 2, 3 that merges vertically over its group, and the activity text with the aspect "
      "it serves in parentheses - (ec), (so), (en). Three-line ruling plus a rule at each level "
      "break, no vertical strokes. Every activity is copied out of Table 5's environment, social and "
      "economic blocks, but the caption gives no scores and the table repeats no score column, so the "
      "reader cannot check the selection against Table 5's numbers from this page.",
      rows=6, cols=2, numeric=1, text=1, rule="booktabs", merged=True)

table(19, 1,
      caption(q("Table 7: 20 years’ optimal control scheme for Congo", 19), numbering="Table N:",
              position="above"),
      "text-layer",
      cited(19, 19, ["Table 7"], 1, "The revised control elements are shown in Table 7."),
      SEC_52,
      "The control scheme as a six-row plan: c1, c2, c3, b1, b2, b3 against four four-year periods "
      "headed 2014~2018, 2019~2023, 2024~2028 and 2029~2033, four numeric columns and one symbol "
      "column. Three-line ruling, nothing merged. Printed faults: c1's row is 0.05 in all four "
      "periods, which reads as a fill value rather than an optimised result; b3's row is printed with "
      "no numbers at all, its values pushed past the end of the text layer; the period headers use a "
      "tilde where the caption's own page prints an en dash elsewhere; the apostrophe in 'years'' is "
      "typographic while the rest of the paper's is not; and the decimal width swings from 0 to "
      "0.05 to -0.1 within one row. No unit or scale is given for either control family.",
      rows=6, cols=5, numeric=4, text=1, rule="booktabs")

RULES = [
    "Measure first, then read the pixels: twenty-one measured regions resolve into fourteen figure "
    "rows, six table rows and one exclusion, with nothing unaccounted [place.area_frac].",
    "A summary-sheet form is not an exhibit: the p1 region is the sheet's T1-T4 and F1-F4 fill-in "
    "rules plus its separator line, measured as one 0.77-area vector cluster because the rules span "
    "the page, so it is excluded rather than counted [place.area_frac].",
    "Two measured regions under two printed captions are two rows with two verbatims, never one row "
    "with a union box: Figures 5 and 6 are pasted side by side on p13, and so are the two pairs on "
    "pp12, 17 and 18 [caption.verbatim].",
    "When the text layer interleaves the captions of a two-column page into one run, the verbatim is "
    "typed from the crop and the source is marked accordingly; the eight captions on pp12, 13, 17 "
    "and 18 are the only such rows here [caption.numbering].",
    "A caption hyphenated by the page is recorded as the layer prints it: Figure 2's verbatim keeps "
    "the 'Develop- ment' break instead of being repaired [caption.verbatim].",
    "A numbered caption that the layer prints contiguously is quoted from the layer even when it "
    "carries a ligature, so Figure 13's and Figure 14's captions keep 'influences' as the f-ligature "
    "the page sets [caption.verbatim].",
    "A shaded block matrix with two real index axes is heatmap-or-contour, not table-as-figure: "
    "Figure 2 draws nine filled blocks with a lattice inside each and ticks CI and DI along its "
    "edges [geometry.family].",
    "A block diagram of boxes and arrows carrying a state vector is flowchart-or-schematic, and the "
    "three-aspect ring of Figure 1 takes the same family because its arcs are drawn as a cycle "
    "[geometry.family].",
    "A state-space trajectory drawn as a joined path with markers is line, not scatter, even when "
    "each series has only two points: Figures 4 and 12 both draw the connector and both key their "
    "series with marker shapes [geometry.family].",
    "A chart with no series key box is still legend 'inside' when the series are labelled at their "
    "own ends; all fourteen figure rows here label inline and not one carries an outside legend "
    "[geometry.legend].",
    "A panel whose y axis is titled only 'Item' prints no quantity name, so printed_numbers records "
    "the ticks it does print and the note carries the missing title instead [geometry.printed_numbers].",
    "Four panels of one figure family drawn on four different y windows are not a common scale: "
    "Figures 7 to 10 print 0.0260-0.0270, 0.022-0.032, 0.0260-0.0270 and 0.024-0.029 respectively, so "
    "shared_axes stays false [geometry.shared_axes].",
    "Rows are counted as printed: Table 5 counts its three group-label rows as rows and Table 1 "
    "counts its seventeen indicator rows without the header [table.rows].",
    "A group label set once and merged over its block makes merged_cells true, and the multi-line "
    "cell contents alone do not [table.merged_cells].",
    "Count the physical columns, not the logical ones: Table 1 prints three level columns for a "
    "three-level tree, Table 3 prints eight columns of which seven are numeric, and Table 4 prints a "
    "two-by-two statement with a stub column [table.cols].",
    "A table whose only rules are horizontal is booktabs even when it adds a rule at every group "
    "break, so all six grids here are booktabs and none is boxed [table.rule_style].",
    "An exhibit first named a page before it prints takes a positive lead_pages: Figure 1 is named on "
    "p3 and printed on p4, Figures 13 and 14 are named a page early too [mention.lead_pages].",
    "An exhibit the prose never names records count 0 with a null first_page and no style spelling - "
    "Table 1 here [mention.count].",
    "A pointer hyphenated across a line break is quoted with the hyphen the layer keeps, so Figure "
    "12's lead sentence begins 'Ac- cording to Figure 12' rather than being repaired [mention.lead_sentence].",
]

NOTE = """Paper 86, Team 35780. Twenty-one measured regions over fourteen of the twenty-four pages, all
twenty-one accounted for: fourteen figure rows, six table rows, one exclusion, so unaccounted is
zero and nothing is left unresolved. The paper numbers fourteen figures and seven tables, and this
record carries all of them except Table 2, which is printed on p9 as a plain text grid with no rules
at all and therefore owns no measured region - it is a declared gap, not a guess.

The region pass had one easy case and one awkward one. The easy case is the summary sheet: the p1
region is a single 0.77-area vector cluster because the T1-T4 and F1-F4 fill-in rules and the
sheet's separator line span the page, which is page furniture and not an exhibit, so it is excluded.
The awkward case is that this paper draws eight of its fourteen figures as two-column pairs -
Figures 3 and 4 on p12, 5 and 6 on p13, 7 to 10 on p17, 11 and 12 on p18 - and each pair is pasted
as separate bitmaps, so every half is its own region and its own row, with its own printed caption.
That is also why the text layer reads like a puzzle: it interleaves the two captions of a pair into
one run, "Figure 3: Forecast on comprehensive Figure 4: The GE-Matrix for sustainability of
performances of three countries three countries", so all eight of those captions are typed from the
crops and marked as such.

What the pictures actually show, read off the crops one at a time. Figure 1 is a three-arrow ring
labelled Social, Environment and Economic around a centre disk, with no arrowhead on the left arc, so
its cycle direction is only half stated. Figure 2 is the GE-Matrix as nine shaded blocks over a
ten-by-ten lattice, numbered I to IX from the bottom left, with four fill classes and no key - and
the numerals sit half a cell off the blocks they name, so the picture encodes the same nine regions
twice and the two encodings disagree. Figures 3 and 4 are the two-column pair on p12: nine forecast
curves whose Congo half collapses into an unreadable knot near 0.05, and three two-point trajectories
in the CI/DI plane with no time axis. Figures 5 and 6 are the same control loop drawn twice, before
and after the plan, differing only by the extra input U_ba and the inserted G_cA block, and in both
the summing junction prints a plus sign with no polarity on any input, so the feedback subtraction
the equations perform is invisible in the drawing.

Figures 7 to 10 are the paper's largest block and its least honest: four panels of five, five, six
and seven curves, each panel on a different y window, each identified only by inline end labels, and
Figure 9 prints seven labels for at most six curves with two of them floating in the middle of the
plot. Figure 7's own y title reads "Development Index(DJ)". Figures 11 and 12 re-read the Congo
forecast with and without the plan, once as six time series where the without-plan half is unreadable
and once as two trajectories in the index plane. Figure 13 is titled on its y axis only "Item" and
promises a perturbation the drawing never marks. Figure 14 is the sharpest caption defect on the
paper: it announces a two-dimensional concentration distribution under a Gaussian model and delivers
a one-dimensional cusp of about ten straight-interpolated points.

The tables carry the arithmetic and several of the faults. Table 1 builds a three-level indicator
tree in three columns, with "Pullotion" printed for pollution and the food-deficit indicator filed
under Education. Table 3 ranks ten countries and loses the country names of ranks 4 and 10 out of
their cells to the end of the text layer. Table 4 states the plan's effect in four sentences with no
numbers at all. Table 5 scores eighteen development activities, prints "Transferring the obtrusive
industries to the industrial towns" twice with two different scores, and files "The reduction of air
pollution" under social while its near-double sits under economic. Table 6 is the six-activity plan
with no scores, so it cannot be checked against Table 5 from its own page. Table 7 is the four-period
control scheme, where c1 reads 0.05 in all four periods and b3's entire row is printed with no
numbers.

Citation is uneven but not empty. Table 1 is the only exhibit the prose never names. Figures 1, 13
and 14 are each named a page before they print; Figures 5 and 6 are named only together, as
"Figures 5-6"; the p17 quartet is named twice as a rounded range ("Figures 7-10", then as the pairs
7-8 and 9-10); and Table 2, the one grid with no measured region, is cited twice while Table 1,
which is drawn and measured, is cited never."""

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT.get("layout_sha256") or LAYOUT.get("sha256", ""),
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": 1, "bbox": REG[(1, 1)], "reason": "not-an-exhibit",
         "note": "Summary-sheet fill-in rules: the T1-T4 and F1-F4 answer lines plus the sheet's "
                 "separator, measured as one cluster because the rules run the page width."},
    ],
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc86-payload.json"
out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "rules", len(RULES))
print("wrote", out)
