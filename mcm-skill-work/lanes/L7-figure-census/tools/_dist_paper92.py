"""Hand census of P-A-2016-44845-998bce33 (Team 44845, 44 pages, 53 measured regions).

Beneath the Surface: A Thermal-Fluid Analysis of a Hot Bath. Fifty-three measured regions
resolve into FIFTY FIGURE ROWS, ONE TABLE and TWO EXCLUSIONS, unaccounted zero.

  p1  r1  banner       not-an-exhibit   "For office use only / Team Control Number"
  p6  r1  Fig.1        flowchart-or-schematic  bathtub geometry
  p6  r2  Fig.2        flowchart-or-schematic  cross-sectional fluid element
  p7  r1  Fig.3        line                    enthalpy against temperature
  p9  r1  Fig.4        line                    h_t against water temperature
  p9  r2  Fig.5        line                    h_b against water temperature
  p10 r1  Fig.6        line                    h_w against water temperature
  p11 r1  table        table-grid              parameter list, NO caption, no table number
  p11 r2  Fig.7        flowchart-or-schematic  thermodynamic system, control volume
  p13 r1  Fig.8        line                    steady temp against mass flow
  p13 r2  Fig.9        line                    steady temp against inlet temp
  p14 r1  Fig.10       line                    steady temp against ambient temp
  p19 r1  Fig.11       heatmap-or-contour
  p20 r1  Fig.12       heatmap-or-contour
  p21 r1  Fig.13       heatmap-or-contour
  p24 r1  Fig.14       heatmap-or-contour
  p25 r1  Fig.15       heatmap-or-contour
  p25 r2  Fig.16       heatmap-or-contour
  p26 r2  Fig.17 (a)   heatmap-or-contour      99% even distribution
  p26 r1  Fig.17 (b)   heatmap-or-contour      half heat at the exit side
  p27 r1  Fig.18 (a)   heatmap-or-contour
  p27 r2  Fig.18 (b)   line
  p28 r1  Fig.19 (a)   line                    analytical
  p28 r2  Fig.19 (b)   line                    numerical
  p29 r1  Fig.20 (a)   line                    width, analytical
  p29 r2  Fig.20 (b)   line                    width, numerical
  p29 r4  Fig.21 (a)   line                    height, analytical
  p29 r3  Fig.21 (b)   line                    height, numerical
  p30 r1  Fig.22 (a)   line                    volume, analytical
  p30 r2  Fig.22 (b)   line                    volume, numerical
  p31 r1  Fig.23 (a)   line                    five diffusivities, full length
  p31 r2  Fig.23 (b)   line                    five diffusivities, magnified
  p32 r1  Fig.24 (a)   line                    input temperature varied
  p32 r2  Fig.24 (b)   line                    mass flow varied
  p32 r3  Fig.25 (a)   heatmap-or-contour      low input temperature
  p32 r4  Fig.25 (b)   heatmap-or-contour      high input temperature
  p33 r1  Fig.26 (a)   heatmap-or-contour      zero mass flow
  p33 r2  Fig.26 (b)   heatmap-or-contour      high mass flow
  p33 r3  Fig.27 (a)   line                    body length
  p33 r4  Fig.27 (b)   line                    body area
  p34 r1  Fig.28 (a)   line                    body temperature
  p34 r2  Fig.28 (b)   line                    body heat transfer coefficient
  p35 r1  Fig.29       line                    borrowed step response, "Figure 20a."
  p36 r1  Fig.30       line                    proportional control
  p37 r1  Fig.31       line                    full PID control
  p38 r2  Fig.32 (a)   line                    optimal input temperature
  p38 r1  Fig.32 (b)   heatmap-or-contour      optimised uniformity
  p38 r3  Fig.33 (a)   line                    optimal mass flow
  p38 r4  Fig.33 (b)   heatmap-or-contour      optimised uniformity
  p39 r1  Fig.34 (a)   line                    manual heat distribution
  p39 r2  Fig.34 (b)   line                    uniformity over time
  p40 r1  Fig.35       heatmap-or-contour      optimised PID heat map
  p44 r1  letterhead   not-an-exhibit          consulting-firm logo art

The paper prints thirty-five figure captions and NO table caption or table number anywhere in its
forty-four pages - the single table on p11 is named only by the pointer sentence on p10. Two
captions cannot be quoted from the linear text layer because the two-column wrap interleaves them
with the body column ("the Ther- be zero, as no mass or energy can be accu- modynamic System"), so
Figures 7 and 29 are typed from the printed block geometry. Fourteen of the thirty-five caption
numbers are carried into a pointer sentence; twenty-one figures are named by no sentence at all,
and Figure 33 is the worst of them - p38 says "The same results are shown in 33 below", dropping
the word "Figure" entirely.

Section placement follows the printed heading positions, not the context dump: the dump attributes
p7 r1 to "3.2 Heat Transfer Coefficients", p10 r1 to section 4, p14 r1 to 6.1, p19-p21 to a formula
line, p31 to 8.4 and p35 and p37 one subsection too far, because its heading carry-over is keyed to
the last heading it saw rather than to the region's y position.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2016-44845-998bce33"
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
          pattern: str = "direct", read: int = 1, lead_page: int | None = None) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, lead_page or first_page),
            "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below",
            variables: int = 0, sentences: int = 1) -> dict:
    """Caption block. `verbatim` is what the page prints, not what the line order emits."""
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": sentences, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


SEC_2 = ["2 Geometric Considerations"]
SEC_3 = ["3 Thermodynamic Considerations"]
SEC_31 = ["3 Thermodynamic Considerations", "3.1 Properties of Water"]
SEC_32 = ["3 Thermodynamic Considerations", "3.2 Heat Transfer Coefficients"]
SEC_4 = ["4 Nominal Values Used in Model Simulations"]
SEC_5 = ["5 A Steady State, Uniform Temperature Model"]
SEC_51 = ["5 A Steady State, Uniform Temperature Model", "5.1 Theory"]
SEC_52 = ["5 A Steady State, Uniform Temperature Model", "5.2 Implementation and Results"]
SEC_63 = ["6 An Analytical Model of the Heat Equation", "6.3 Basic Results and Verification"]
SEC_72 = ["7 A Numerical Model of Convection-Diffusion", "7.2 Basic Results and Verification"]
SEC_73 = ["7 A Numerical Model of Convection-Diffusion", "7.3 Modeling Bather Actions"]
SEC_81 = ["8 Model Comparison", "8.1 Solution Metrics"]
SEC_82 = ["8 Model Comparison", "8.2 Effect of Bathtub Geometry"]
SEC_83 = ["8 Model Comparison", "8.3 Effect of Adding Soap"]
SEC_84 = ["8 Model Comparison", "8.4 Effect of Varied Input Temperature and Flow Rate"]
SEC_85 = ["8 Model Comparison", "8.5 Effect of Varied Size and Position of Bather"]
SEC_91 = ["9 Control Theory and Implementation", "9.1 PID Control Theory"]
SEC_92 = ["9 Control Theory and Implementation",
          "9.2 Implementation of PID Control in Numerical Model"]
SEC_93 = ["9 Control Theory and Implementation",
          "9.3 Control of Uniformity of Water Temperature Distribution"]
SEC_94 = ["9 Control Theory and Implementation",
          "9.4 Final PID Control with With Manual Heat Distribution"]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
for _group in (SEC_2, SEC_3, SEC_31, SEC_32, SEC_4, SEC_5, SEC_51, SEC_52, SEC_63, SEC_72,
               SEC_73, SEC_81, SEC_82, SEC_83, SEC_84, SEC_85, SEC_91, SEC_92, SEC_93, SEC_94):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN:
            raise SystemExit(f"section label is not an indexed heading: {_label!r}")

ITEMS: list[dict] = []
TABLES: list[dict] = []


def figure(page: int, reg: int, number: str, family: str, cap: dict, cap_src: str,
           mention: dict, section: list[str], note: str, geo: dict | None = None,
           section_kind: str = "other", other_note: str = "",
           confidence: str = "high") -> None:
    item = {
        "page": page, "bbox": REG[(page, reg)], "kind": "raster", "family": family,
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


PANEL = dict(panels=2, layout="1x2")

# ============================================================ geometric figures
figure(6, 1, "1", "flowchart-or-schematic",
       caption("Figure 1: Bathtub Geometry"), "text-layer",
       cited(6, 6, ["Figure 1"], 1,
             "The bathtub will be considered as a rectangular prism, with dimensions equal to "
             "L, W , and H as shown below in Figure 1.", "as-shown-in"),
       SEC_2,
       "The tub drawn as a shaded three-dimensional box in perspective with the water surface "
       "shaded, a drain hole at the lower right, a faucet pipe entering at the upper left and the "
       "three edge lengths lettered H, W and L on dimension arrows. No axis graduations, no "
       "legend, no scale, no printed number: the L, W and H it letters are the symbols the prose "
       "then carries into the model, not measured values. It is the geometric premise of the whole "
       "paper and the only exhibit that shows the tub itself.",
       geometry("flowchart-or-schematic", three_d="isometric"))

figure(6, 2, "2", "flowchart-or-schematic",
       caption("Figure 2: Cross-sectional Fluid Element"), "text-layer", uncited(), SEC_2,
       "A cross-section of the water drawn as a shaded rectangle with a double-line boundary, "
       "dimension arrows for H, W and delta-x and a small x-y-z axis triad. The caption calls it "
       "the cross-sectional fluid element, but the drawing carries NO velocity arrow and NO force "
       "arrow: it fixes the dimensions of the element, and the prose that follows it does the rest. "
       "No legend, no graduation, no number. Note that the caption is the only thing in the paper "
       "that names this drawing - the surrounding sentence ('Heat capacity, fluid flow velocity, "
       "heat loss to the surroundings, and other extensive properties') runs straight through it in "
       "the text layer, which is why the line reads 'Heat capacity, Figure 2: Cross-sectional Fluid "
       "Element'.",
       geometry("flowchart-or-schematic"))

figure(7, 1, "3", "line",
       caption("Figure 3: Linear Enthalpy Variation"), "text-layer",
       cited(7, 7, ["Figure 3"], 1,
             "as- sumption was validated using property val- ues from the XSteam[1] MATLAB "
             "function, shown at right in Figure 3.", "as-shown-in"),
       SEC_31,
       "One straight blue line across a light grid, with a short black arrow pointing at the fitted "
       "equation printed on the plot ('h = 4.1854u + 0.21431'). Axes: temperature on the abscissa "
       "0 to 100 deg C, specific enthalpy on the ordinate 0 to 450 kJ/kg. No legend, no marker, no "
       "printed data value; the only number in the picture besides the tick labels is the slope the "
       "caption's 'linear' refers to. It is the paper's evidence for assuming constant specific heat "
       "and it fits in one straight line, so the exhibit and the claim agree.",
       geometry("line", three_d="no"))

# ============================================================ coefficient plots
figure(9, 1, "4", "line",
       caption("Figure 4: Variation of ht with Water Temperature"), "text-layer",
       cited(9, 9, ["Figure 4"], 1,
             "the variation of ht with water temperature is shown below in Figure 4.",
             "as-shown-in", read=2),
       SEC_32,
       "A solid blue rising curve over a 20 deg C window of water temperature against a long-dashed "
       "orange horizontal reference line at the predicted mean, with a key box INSIDE the plot at "
       "the lower right carrying 'Actual Value' and 'Mean = 4.6922 W/m2K'. Axes: water temperature "
       "30 to 50 deg C, heat transfer coefficient 0 to 5.5 W/m2K. No printed data values beyond the "
       "mean in the key. The whole coefficient moves about half a unit, which the authors then "
       "declare negligible and replace by that mean - the exhibit is honest about it and the "
       "pointer says so ('As shown by the above figure, the heat transfer coefficient does vary "
       "with temperature of water, as was expected').",
       geometry("line", legend="inside"))

figure(9, 2, "5", "line",
       caption("Figure 5: Variation of hb with Water Temperature"), "text-layer", uncited(),
       SEC_32,
       "The bottom-surface coefficient plotted exactly as Figure 4 is: one solid blue rising curve "
       "and one long-dashed orange mean line, key box inside the lower right reading 'Mean = 1.9341 "
       "W/m2K'. Axes: water temperature 30 to 50 deg C, heat transfer coefficient 0 to 2 W/m2K. No "
       "printed values but the mean. The pointer for this family of plots is not repeated here - "
       "the sentence immediately above the caption reads only 'Similarly, the variation of hb with "
       "system temperature is shown below', so the figure is named by no label anywhere.",
       geometry("line", legend="inside"))

figure(10, 1, "6", "line",
       caption("Figure 6: Variation of hw with Water Temperature"), "text-layer", uncited(),
       SEC_32,
       "The wall coefficient, again a solid blue rising curve with a long-dashed orange mean line "
       "and an inside key box ('Mean = 3.8044 W/m2K'). Axes: water temperature 30 to 50 deg C, heat "
       "transfer coefficient 0 to 4 W/m2K. Its pointer is bare too ('Finally, the same analysis is "
       "shown for hw'), so the figure carries no label in the running text. The three coefficient "
       "plots are otherwise indistinguishable in style, and their means order top 4.69, wall 3.80, "
       "bottom 1.93 - the ordering the prose claims for face-up, vertical and face-down surfaces.",
       geometry("line", legend="inside"))

# ============================================================ the unlabelled table
table(11, 1,
      caption("", numbering="none", position="above", sentences=0),
      "none",
      {"first_page": 10, "lead_pages": 1, "style": ["The following table"], "count": 1,
       "lead_sentence": q("The following table contains the model parameters that can be altered "
                          "as well as their nominal values.", 10),
       "trail_sentence": "", "lead_pattern": "direct", "read_sentences": 1,
       "gap_sentences": None},
      SEC_4,
      "The paper's only table and it is UNLABELLED: three columns (Parameter, Description, Nominal "
      "Value) with vertical strokes between the columns and a single horizontal rule under the "
      "header row, twenty rows in all - the header plus nineteen parameters (L, W, H, bath volume, "
      "water density, specific heat, thermal conductivity, three heat transfer coefficients, "
      "ambient temperature, inlet temperature, mass flow, body dimensions and body properties). "
      "Units sit inside the cells of the third column rather than in the header, bracketed citation "
      "superscripts ([2], [3]) sit inside cells too, and no cell is shaded. The paper never prints "
      "'Table 1': the grid is named only by the p10 pointer sentence, and because the pointer calls "
      "it 'the following table' the caption block is empty rather than absent.",
      rows=20, cols=3, numeric=1, text=2, rule="vertical-rules", header_rows=1,
      units_in_header=False, width="full", section_kind="model",
      note_sentence="")

# ============================================================ the system schematic
figure(11, 2, "7", "flowchart-or-schematic",
       caption("Figure 7: Graphical Illustration of the Ther- modynamic System"),
       "typed-from-crop",
       cited(11, 11, ["Figure 7"], 1,
             "This is shown in Figure 7 at right, where the dotted line represents the control "
             "volume (the system).", "as-shown-in"),
       SEC_51,
       "A hand-drawn-looking rectangle for the water with a dashed inner boundary marking the "
       "control volume, two hollow block arrows at left and right labelled with the inlet and "
       "outlet mass flows, four red wavy arrows rising off the top surface for the net heat out, and "
       "the two inscriptions 'System (water)' and 'Surroundings'. No axis, no graduation, no "
       "legend, no number. It is the only exhibit in the paper that shows the control volume the "
       "energy equation is written on. Typed from the printed block geometry, not the line order: "
       "the linear text layer interleaves the caption with the body column ('the Ther- be zero, as "
       "no mass or energy can be accu- modynamic System'), so the caption cannot be quoted from the "
       "page string and this one is transcribed from the two-column block as printed, hyphen break "
       "and all.",
       geometry("flowchart-or-schematic"))

# ============================================================ steady-state sensitivity
figure(13, 1, "8", "line",
       caption("Figure 8: Sensitivity of Final Temperature to Inlet Mass Flow"), "text-layer",
       cited(13, 13, ["Figure 8"], 1,
             "Using the nominal parameter values, the steady, uniform temperature as a function of "
             "mass flow is shown below in Figure 8.", "as-shown-in"),
       SEC_52,
       "One continuous blue curve rising steeply and then flattening, on a light grey grid inside a "
       "white axes box. Axes: mass flow 0 to 0.5 kg/s, steady water temperature 28 to 46 deg C. No "
       "legend, no markers, no printed values. The saturation is the paper's argument that the "
       "steady-state model reaches a ceiling of about 45 deg C whatever the flow; the curve prints "
       "no point estimate for that ceiling, so the number lives only in the caption of the table "
       "below.",
       geometry("line"))

figure(13, 2, "9", "line",
       caption("Figure 9: Sensitivity of Final Temperature to Inlet Temperature"), "text-layer",
       uncited(), SEC_52,
       "One straight blue rising line on the same grey grid. Axes: inlet temperature 20 to 50 deg "
       "C, steady water temperature 20 to 50 deg C, so the diagonal is the identity and the axes "
       "share a scale - the exhibit states no more than that the steady temperature tracks the "
       "inlet one for one. No legend, no printed values. Its pointer is bare ('A similar plot is "
       "shown below to illustrate the dependence on inlet temperature'), so no label appears in the "
       "running text.",
       geometry("line"))

figure(14, 1, "10", "line",
       caption("Figure 10: Sensitivity of Final Temperature to Ambient Air Temperature"),
       "text-layer", uncited(), SEC_52,
       "One straight blue rising line on the same grey grid, and the telling detail is the ordinate: "
       "it spans 42.2 to 44 deg C while the abscissa spans 20 to 40 deg C, so a twenty-degree sweep "
       "of ambient temperature moves the bath by less than two degrees, and the slope that fills "
       "the frame is the axis window's doing rather than the model's. No legend, no printed values. "
       "Named by no sentence - the introduction above it says nothing at all about ambient air.",
       geometry("line"))

# ============================================================ analytical heat maps
figure(19, 1, "11", "heatmap-or-contour",
       caption("Figure 11: Heat Map of Heat Loss over Time"), "text-layer",
       cited(19, 19, ["Figure 11"], 1,
             "For the data used in Equation 33, Figure 11 displays the temperature distribution in "
             "x and t.", "figure-n-shows"),
       SEC_63,
       "Temperature as a colour field over position and time: the abscissa runs 0 to 1.5 m and the "
       "ordinate is time, 0 to 60 minutes, INVERTED so that t = 0 sits at the top. Yellow at the top "
       "grading smoothly to dark blue at the bottom; the colour bar sits at the right with a deg C "
       "scale. No grid, no contour lines, no printed data value. It is the first exhibit to use the "
       "position-by-time frame that Figures 12 to 16 and 21 to 35 then repeat.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

figure(20, 1, "12", "heatmap-or-contour",
       caption("Figure 12: Demonstration of Heat Distribution and Heat Loss With Input Water"),
       "text-layer",
       cited(20, 20, ["Figure 12"], 2,
             "the full solution in x and t for the conditions set in Equation 36 are shown in "
             "Figure 12.", "as-shown-in", read=2),
       SEC_63,
       "A near-uniform dark blue block covering most of the frame with one thin, bright, multicolour "
       "vertical strip down the left edge - the inlet water entering at x = 0 - and a faint "
       "horizontal seam where the plume stalls. Same inverted time ordinate 0 to 60 min, position 0 "
       "to 1.5 m, colour bar at the right. It is the only exhibit in this family where the whole "
       "point is the contrast between one bright edge and an otherwise flat field, and the pointer "
       "is read twice: the lead sentence, and the following sentence that interprets it ('Figure 12 "
       "demonstrates that the heat propagates through the water').",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

figure(21, 1, "13", "heatmap-or-contour",
       caption("Figure 13: Demonstration of a Moving Heat Source in the Bath"), "text-layer",
       cited(21, 21, ["Figure 13"], 2,
             "The new solution is displayed below in Figure 13.", "as-shown-in", read=2),
       SEC_63,
       "The same frame with a bright yellow wedge spreading downward and to the right from a point "
       "near the top centre - the moving source the caption names. Time 0 to 60 min inverted, "
       "position 0 to 1.5 m, colour bar at the right. Two sentences read it: the lead, and 'Figure "
       "13 shows that the analytical model is capable of capturing a moving heat source in both "
       "space and time.' No contour line and no printed value, so the wedge's angle and speed have "
       "to be read off the colour scale by eye.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

# ============================================================ numerical heat maps
figure(24, 1, "14", "heatmap-or-contour",
       caption("Figure 14: Demonstration of Heat Loss over Time in Numerical Model"), "text-layer",
       cited(24, 24, ["Figure 14"], 1,
             "The results from this simulation are shown below in Figure 14.", "as-shown-in"),
       SEC_72,
       "Yellow at the top grading through green to dark blue at the bottom in smooth horizontal "
       "bands: the numerical model's cooling of an undisturbed tub. Time 0 to 60 min inverted, "
       "position 0 to 1.5 m with graduations every 0.25, colour bar at the right in deg C. No "
       "printed value. Its twin is Figure 11, the same experiment run in the analytical model, and "
       "the pair is presented without a difference map.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

figure(25, 1, "15", "heatmap-or-contour",
       caption("Figure 15: Heat Map of Uniform Mass Flow from Faucet with Heat Loss"), "text-layer",
       uncited(), SEC_72,
       "A blocky colour field with a hot yellow wedge at the left edge fading into dark blue - the "
       "faucet plume entering at x = 0. The panel prints its own title inside the plot, 'Heat Loss "
       "with Faucet On', and the same inverted time axis 0 to 60 min against position 0 to 1.5 m, "
       "colour bar at the right. No printed value. Bare pointer above it ('Next, the presence of "
       "the bather, Joe, was added and the simulation was run' introduces the following figure, not "
       "this one), so no label appears anywhere in the text.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

figure(25, 2, "16", "heatmap-or-contour",
       caption("Figure 16: Heat Map of Numerical Model with Bather Present"), "text-layer",
       uncited(), SEC_72,
       "Yellow at the top to blue at the bottom, the field perturbed by the bather, with the "
       "in-plot title 'Heat Propogation with Bather' - the exhibit MISSPELLS 'propagation' and the "
       "caption does not repeat the error, so the defect is visible only to a reader who looks at "
       "the pixels. Same axes (time 0 to 60 min inverted, position 0 to 1.5 m) and the same colour "
       "bar. No printed value, no pointer, no contour. The bather is a body in the model with "
       "properties set from the table on p11, and nothing in the picture marks where he sits.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

# ============================================================ two-panel bather exhibits
figure(26, 2, "17 (a)", "heatmap-or-contour",
       caption("Figure 17: Effects of Redistribution of Water"), "text-layer", uncited(), SEC_73,
       "The good case of the redistribution experiment: a near-uniform field whose in-plot title "
       "claims '99% Even Heat Distribution', with the panel letter '(a) Nearly Uniform Heat "
       "Distribution' printed beneath it. Yellow lowers toward blue across the frame but no band is "
       "sharp. Time 0 to 60 min inverted, position 0 to 1.5 m, colour bar at the right, no printed "
       "value. It is the left panel of a two-panel exhibit - panel (b) sits to its right - and the "
       "captioned pair is named by no sentence in the paper.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(26, 1, "17 (b)", "heatmap-or-contour",
       caption("Figure 17: Effects of Redistribution of Water"), "text-layer", uncited(), SEC_73,
       "The bad case, in-plot titled 'Half Heat Distributed Over Exit Boundary Side': a blocky "
       "field with a hot yellow wedge at the left and coarse vertical banding, carrying the panel "
       "letter '(b) Split Heat Distribution'. Same inverted time axis and position axis and its own "
       "colour bar; no printed value. The contrast between the two panels is the exhibit's whole "
       "content and neither prints the fraction of uniformity its title asserts.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(27, 1, "18 (a)", "heatmap-or-contour",
       caption("Figure 18: Demonstration of the Objective Functions, u(t) and σ(t) With "
               "Nominal Param- eters"),
       "text-layer", uncited(), SEC_81,
       "A heat map with a narrow yellow left strip and a diagonal transition, in-plot titled 'Heat "
       "Loss with Faucet On', lettered '(a) Heat Map of Simulation'. Inverted time 0 to 60 min, "
       "position 0 to 1.5 m, colour bar at the right, no printed value.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(27, 2, "18 (b)", "line",
       caption("Figure 18: Demonstration of the Objective Functions, u(t) and σ(t) With "
               "Nominal Param- eters"),
       "text-layer", uncited(), SEC_81,
       "The exhibit's second panel is NOT a heat map: it plots the two objective functions against "
       "time as two drawn curves, one nearly linear and rising and one saturating, with an inside "
       "key box and the letter '(b) Objective Functions From Simulation'. Axes: time 0 to 60 min, "
       "temp 0 to 3.5 in whatever units the two functions happen to carry. No printed value. A heat "
       "map and a line plot sharing one caption and one number is the paper's clearest mixed-media "
       "pair.",
       geometry("line", **PANEL, legend="inside"))

# ============================================================ geometry sensitivity pairs
figure(28, 1, "19 (a)", "line",
       caption("Figure 19: Effects of Variation of Length in Both Models"), "text-layer", uncited(),
       SEC_82,
       "Objective functions against tub length for the analytical model: two curves, one descending "
       "and one rising, with a dashed vertical rule at the nominal 1.5 m and an in-plot key box "
       "above the plot. Axes: length 0.5 to 2 m, objective function -0.8 to 0.6 deg C. No printed "
       "value. The panel letter is '(a) Analytical Model'.",
       geometry("line", **PANEL, legend="above"))

figure(28, 2, "19 (b)", "line",
       caption("Figure 19: Effects of Variation of Length in Both Models"), "text-layer", uncited(),
       SEC_82,
       "The numerical twin: one steep U-shaped curve and one shallow arc, again with the nominal "
       "rule, lettered '(b) Numerical Model'. Axes: length 0.5 to 2.5 m, objective function 0.5 to "
       "5.5 deg C - roughly TEN TIMES the analytical ordinate span, so the two halves of this "
       "exhibit are not on a common scale and the comparison 'in Both Models' cannot be read off "
       "the page without rescaling one of them.",
       geometry("line", **PANEL, legend="inside"))

figure(29, 1, "20 (a)", "line",
       caption("Figure 20: Effects of Variation of Width in Both Models"), "text-layer", uncited(),
       SEC_82,
       "Width swept with the analytical model: two kinked curves with a dashed rule at width = 1 m, "
       "lettered '(a) Analytical Model', key inside the plot. Axes: width 0.5 to 2 m, objective "
       "function -3 to 2 deg C. No printed value. Same caption as the panel beside it.",
       geometry("line", **PANEL, legend="inside"))

figure(29, 2, "20 (b)", "line",
       caption("Figure 20: Effects of Variation of Width in Both Models"), "text-layer", uncited(),
       SEC_82,
       "Width swept with the numerical model: two smooth curves, nominal rule at 1 m, lettered "
       "'(b) Numerical Model'. Axes: width 0.5 to 2 m, objective function 0.5 to 4 deg C - again a "
       "different ordinate window from its analytical partner, and the curves even have a different "
       "shape (kinked against smooth), so the disagreement between the models is drawn as much as "
       "measured.",
       geometry("line", **PANEL, legend="inside"))

figure(29, 4, "21 (a)", "line",
       caption("Figure 21: Effects of Variation of Height in Both Models"), "text-layer", uncited(),
       SEC_82,
       "Height swept with the analytical model, piecewise-linear curves with a nominal rule near "
       "0.48 m, lettered '(a) Analytical Model', key boxed inside the plot. Axes: height 0.2 to 1.5 "
       "m, objective function -5 to 1 deg C. No printed value.",
       geometry("line", **PANEL, legend="inside"))

figure(29, 3, "21 (b)", "line",
       caption("Figure 21: Effects of Variation of Height in Both Models"), "text-layer", uncited(),
       SEC_82,
       "The numerical twin of the panel to its left, two smooth curves, rule near 0.48 m, lettered "
       "'(b) Numerical Model'. Axes: height 0.2 to 1.6 m, objective function 0 to 4.5 deg C, a "
       "six-degree span against the analytical panel's six-degree span but shifted, so the same "
       "qualitative bowl is drawn a full axis out of register with its partner.",
       geometry("line", **PANEL, legend="inside"))

figure(30, 1, "22 (a)", "line",
       caption("Figure 22: Effects of Variation of Volume in Both Models"), "text-layer",
       cited(30, 30, ["Figure 22"], 1,
             "The results from this analysis are shown in Figure 22 below.", "as-shown-in"),
       SEC_82,
       "Volume factor on the abscissa (0 to 2), two curves crossing near 0.38, and here the exhibit "
       "does something none of the other geometry pairs do: it carries TWO ordinates, -1.4 to -0.2 "
       "on the left and 0 to 8 on the right, both labelled 'Objective Function [deg C]'. Two curves "
       "of the same quantity on two scales of the same quantity is unreadable, and the negative "
       "left-hand axis is a second defect - an objective function bounded below zero by "
       "construction. Lettered '(a) Analytical Model', key inside.",
       geometry("line", **PANEL, legend="inside"))

figure(30, 2, "22 (b)", "line",
       caption("Figure 22: Effects of Variation of Volume in Both Models"), "text-layer",
       cited(30, 30, ["Figure 22"], 1,
             "The results from this analysis are shown in Figure 22 below.", "as-shown-in"),
       SEC_82,
       "The numerical twin, two smooth curves with a sharp rise and crossing near 0.3, again on dual "
       "ordinates - 0 to 8 left and 0 to 4 right, both 'Objective Function [deg C]' - lettered "
       "'(b) Numerical Model'. Both panels of the pair are counted here because the region pass "
       "boxes each of them, and the caption that governs both is the only pointer either has.",
       geometry("line", **PANEL, legend="inside"))

figure(31, 1, "23 (a)", "line",
       caption("Figure 23: Effects of Variation of Thermal Diffusivity in Numerical Model"),
       "text-layer", uncited(), SEC_83,
       "Five closely bunched sigmoid curves falling from 45 to 36.7 deg C across a transition near "
       "0.4 m, one per diffusivity, with the key inside the plot naming alpha = 7.36e-08 m2/s and "
       "four others. Axes: distance 0 to 1.5 m, temperature 36 to 45 deg C, so the panel prints the "
       "values it varies in the key rather than on the marks. Lettered '(a) Varied of Diffusivity "
       "over Full Length' - the panel title is ungrammatical in the source and is reproduced as "
       "printed.",
       geometry("line", **PANEL, legend="inside", numbers=True))

figure(31, 2, "23 (b)", "line",
       caption("Figure 23: Effects of Variation of Thermal Diffusivity in Numerical Model"),
       "text-layer", uncited(), SEC_83,
       "The magnified view: the same five curves over distance 0.2 to 0.6 m on temperature 36 to 45 "
       "deg C, where they separate by about a degree and a half. Lettered '(b) Magnified Variations "
       "of Diffusivity'; the key repeats with alpha = 1.288e-07 m2/s leading. The magnification "
       "factor is about seven and the paper never says so - the only cue is the changed abscissa.",
       geometry("line", **PANEL, legend="inside", numbers=True))

# ============================================================ input sensitivity
figure(32, 1, "24 (a)", "line",
       caption("Figure 24: Effects of Varied Input Temperature and Mass Flow at Input"),
       "text-layer",
       cited(31, 32, ["Figure 24"], 1,
             "The results from this analysis are shown below in Figure 24.", "as-shown-in",
             lead_page=31),
       SEC_84,
       "The two objective functions against input temperature: a blue rising stroke and an orange "
       "falling one with vertex markers, an inside key naming both objectives, a dashed vertical "
       "rule at the nominal value and the in-plot title 'Objective Functions vs. Input Temperature "
       "after 1 Hour'. Axes: input temperature 35 to 50 deg C, objective function -1 to 6 deg C. "
       "Lettered '(a) Variation of Input Temperature'. The pointer sits on the previous page, hence "
       "lead_pages 1.",
       geometry("line", **PANEL, legend="inside"))

figure(32, 2, "24 (b)", "line",
       caption("Figure 24: Effects of Varied Input Temperature and Mass Flow at Input"),
       "text-layer",
       cited(31, 32, ["Figure 24"], 1,
             "The results from this analysis are shown below in Figure 24.", "as-shown-in",
             lead_page=31),
       SEC_84,
       "The same experiment against mass flow: two marked strokes, inside key, nominal rule and the "
       "title 'Objective Functions vs. Mass Flow after 1 Hour'. Axes: mass flow 0 to 0.1 kg/s, "
       "objective function -0.5 to 4 deg C. Lettered '(b) Variation of Mass Flow Rate'. Note that "
       "this pair varies two inputs the paper has already declared independent in the steady-state "
       "model.",
       geometry("line", **PANEL, legend="inside"))

figure(32, 3, "25 (a)", "heatmap-or-contour",
       caption("Figure 25: Heat Map Comparison of Input Temperature Effect in Numerical Model"),
       "text-layer", uncited(), SEC_84,
       "The low-input-temperature run: a smooth field over position and time with a thin wave band, "
       "colour bar at the right spanning 35 to 37 deg C, and the in-plot title 'Low Input "
       "Temperature Distribution'. Time 0 to 60 min inverted, position 0 to 1.5 m. Lettered '(a) "
       "Low Input Temperature'.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(32, 4, "25 (b)", "heatmap-or-contour",
       caption("Figure 25: Heat Map Comparison of Input Temperature Effect in Numerical Model"),
       "text-layer", uncited(), SEC_84,
       "The high-input-temperature run: a blocky two-tone field split by a diagonal band, colour bar "
       "37 to 44 deg C, in-plot title 'High Input Temperature Distribution'. Lettered '(b) High "
       "Input Temperature'. The two panels are captioned as a comparison but their colour scales "
       "differ by nine degrees and neither prints a shared reference, so the 'comparison' is between "
       "two differently normalised pictures.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(33, 1, "26 (a)", "heatmap-or-contour",
       caption("Figure 26: Heat Map Comparison of Mass Flow Rates in Numerical Model"), "text-layer",
       uncited(), SEC_85,
       "Zero flow: an almost featureless gradient filling the frame, colour bar 36.8 to 37 deg C - a "
       "tenth-of-a-degree window, which is why the field looks smooth rather than flat. In-plot "
       "title 'Zero Mass Flow Temperature Distribution', lettered '(a) Zero Mass Flow Rate'. Time 0 "
       "to 60 min inverted, position 0 to 1.5 m.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(33, 2, "26 (b)", "heatmap-or-contour",
       caption("Figure 26: Heat Map Comparison of Mass Flow Rates in Numerical Model"), "text-layer",
       uncited(), SEC_85,
       "High flow: a blocky field with a diagonal yellow front advancing from the inlet, colour bar "
       "37 to 44 deg C, in-plot title 'High Mass Flow Temperature Distribution', lettered '(b) High "
       "Mass Flow Rate'. The panel pair spans 36.8-37 deg C against 37-44 deg C, so the two halves "
       "of the comparison are on colour scales an order of magnitude apart.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(33, 3, "27 (a)", "line",
       caption("Figure 27: Impact of Body Shape and Size on Objective Functions"), "text-layer",
       uncited(), SEC_85,
       "Body length on the abscissa (0 to 1.5 m): two nearly flat strokes, blue low and orange "
       "upper, with vertex markers, an inside key, a nominal rule and the title 'Objective "
       "Functions vs. Body Length after 1 Hour'. Objective function 1.6 to 3.6 deg C. Lettered '(a) "
       "Effect of Body Length'. The strokes are nearly horizontal, so the exhibit shows body length "
       "barely matters and prints no value to say how barely.",
       geometry("line", **PANEL, legend="inside"))

figure(33, 4, "27 (b)", "line",
       caption("Figure 27: Impact of Body Shape and Size on Objective Functions"), "text-layer",
       uncited(), SEC_85,
       "Body surface area instead of length (0 to 2 m): the same two flat strokes on the same 1.6 to "
       "3.6 deg C window, inside key and nominal rule, titled 'Objective Functions vs. Body Area "
       "after 1 Hour', lettered '(b) Effect of Body Surface Area'. Because both panels use one "
       "ordinate window, this pair is at least directly comparable - unlike every other two-panel "
       "pair in the paper.",
       geometry("line", **PANEL, legend="inside"))

figure(34, 1, "28 (a)", "line",
       caption("Figure 28: Impact of Thermal Properties of Body on Objective Functions"),
       "text-layer", uncited(), SEC_85,
       "Body temperature on the abscissa (30 to 50 deg C): two curves, blue rising and orange "
       "descending, crossing near 37 deg C, with a dashed nominal rule tagged 'Nominal Value' and an "
       "inside key. Objective function 1.5 to 3.5 deg C. Lettered '(a) Effect of ...' - the panel "
       "title is clipped mid-phrase in the print. No printed value.",
       geometry("line", **PANEL, legend="inside"))

figure(34, 2, "28 (b)", "line",
       caption("Figure 28: Impact of Thermal Properties of Body on Objective Functions"),
       "text-layer", uncited(), SEC_85,
       "Body heat transfer coefficient on the abscissa (0 to 50 W/m2K): two nearly horizontal "
       "strokes, blue at the bottom and orange at the top, with the nominal rule and its tag. "
       "Objective function 1.6 to 3.6 deg C, lettered '(b)'. The coefficient the paper argues is "
       "negligible for the water (Figures 4 to 6, replaced by means) is varied by a factor of fifty "
       "here and moves the objective function not at all - the two exhibits together make the "
       "paper's case for using means.",
       geometry("line", **PANEL, legend="inside"))

# ============================================================ control exhibits
figure(35, 1, "29", "line",
       caption("Figure 29: Illustration of Properly Tuned PID Controller[11]"), "typed-from-crop",
       uncited(), SEC_91,
       "A single step response: one smooth curve rising to a plateau, a red dashed line at y = 1, a "
       "plain black frame, the gains printed inside the plot as Kp = 5, Ki = 3, Kd = 3 - and the "
       "ABSCISSA LABELLED ONLY 't' with no title on the ordinate at all. The raster also carries a "
       "label from wherever it was copied: 'Figure 20a. Illustration of Properly Tuned', so a "
       "foreign figure number is baked into the pixels of the paper's Figure 29. The caption credits "
       "reference [11] and names no axes. Typed from the printed block geometry because the linear "
       "text layer interleaves the caption with the body column.",
       geometry("line", numbers=True))

figure(36, 1, "30", "line",
       caption("Figure 30: Effect of Proportional Control"), "text-layer", uncited(), SEC_92,
       "Proportional control alone: two oscillating strokes on a shared time axis with dual "
       "coloured ordinates, error in average temperature (-10 to 10 deg C) on the left in blue and "
       "the required change in faucet temperature (-50 to 50 deg C) on the right in orange, and NO "
       "legend - the colour of the axis labels is the only key. Time 0 to 60 min. In-plot title "
       "'Proportional Control'. The oscillation amplitude is the exhibit's whole point and it prints "
       "no damping ratio or settling time.",
       geometry("line"))

figure(37, 1, "31", "line",
       caption("Figure 31: Optimal Control of Average Bath Temperature"), "text-layer",
       cited(36, 37, ["Figure 31"], 1,
             "Using full PID, the results from the same analysis are shown below in Figure 31.",
             "as-shown-in", lead_page=36),
       SEC_92,
       "Full PID: two strokes on dual coloured ordinates, the blue error sitting near zero and the "
       "orange faucet demand dipping and then rising, time 0 to 60 min, in-plot title 'Full PID "
       "Control', no legend. The blue left axis spans -10 to 5 deg C and the orange right axis -2 to "
       "4 deg C, both narrower than Figure 30's, which is how the paper shows the tuned controller "
       "is quieter - a comparison the reader has to make across two figures with four different "
       "scales.",
       geometry("line"))

figure(38, 2, "32 (a)", "line",
       caption("Figure 32: Determination of Optimal Input Temperature with Prescribed Flow Rate"),
       "text-layer",
       cited(37, 38, ["Figure 32"], 1,
             "In Figure 32 below, we show the objective functions vs. inlet temperature, where the "
             "heat is being distributed evenly and the mass flow is fixed.", "as-shown-in",
             lead_page=37),
       SEC_93,
       "The optimiser run: a blue rising stroke, an orange stroke flat at zero, a filled black "
       "marker, a dashed nominal rule and an annotation printed inside the plot, 'Optimal Input "
       "Temperature = 38.0425 deg C'. Axes: input temperature 35 to 50 deg C, objective function -1 "
       "to 3 deg C. Lettered '(a) Optimal Input Temperature'. Five significant figures on a "
       "temperature whose own model uses a mean coefficient to one decimal place.",
       geometry("line", **PANEL, legend="inside", numbers=True))

figure(38, 1, "32 (b)", "heatmap-or-contour",
       caption("Figure 32: Determination of Optimal Input Temperature with Prescribed Flow Rate"),
       "text-layer",
       cited(37, 38, ["Figure 32"], 1,
             "In Figure 32 below, we show the objective functions vs. inlet temperature, where the "
             "heat is being distributed evenly and the mass flow is fixed.", "as-shown-in",
             lead_page=37),
       SEC_93,
       "The second panel is the heat map that the optimum buys: a uniform teal field filling the "
       "plot rectangle with a colour bar at the right and the in-plot title 'Optimal Input "
       "Temperature Distribution'. Time 0 to 60 min inverted, position 0 to 1.5 m. Lettered '(b) "
       "Heat Map of Optimized Uniformity'. A field this uniform means the colour bar spans almost "
       "nothing, and the panel does not print its extremes, so 'uniform' is asserted by the title "
       "rather than shown by a scale.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(38, 3, "33 (a)", "line",
       caption("Figure 33: Determination of Optimal Mass Flow Rate with Prescribed Nominal Input "
               "Temperature"),
       "text-layer", uncited(), SEC_93,
       "The mass-flow optimiser: a rising blue stroke, a flat orange stroke with a filled marker, a "
       "dashed nominal rule and the annotation 'Optimal Mass Flow = 0.006518 kg/s' printed inside "
       "the plot. Axes: mass flow 0 to 0.07 kg/s, objective function -0.5 to 3 deg C, lettered '(a) "
       "Optimal Mass Flow Rate'. This figure has the worst pointer in the paper: p38 introduces it "
       "with 'The same results are shown in 33 below', dropping the word 'Figure' entirely, so the "
       "caption number is never written as a label anywhere.",
       geometry("line", **PANEL, legend="inside", numbers=True))

figure(38, 4, "33 (b)", "heatmap-or-contour",
       caption("Figure 33: Determination of Optimal Mass Flow Rate with Prescribed Nominal Input "
               "Temperature"),
       "text-layer", uncited(), SEC_93,
       "The heat map for the optimum flow: a single smooth column of blue grading to yellow, colour "
       "bar at the right spanning 37.0001 to 37.0004 deg C - THREE TEN-THOUSANDTHS OF A DEGREE. The "
       "colour bar is the exhibit's real content: at that window any field is uniform, so the panel "
       "and its partner both certify uniformity by choosing a scale narrow enough to make the "
       "residual noise invisible. Lettered '(b) Heat Map of Optimized Uniformity'.",
       geometry("heatmap-or-contour", **PANEL, legend="outside-right", colorbar=True))

figure(39, 1, "34 (a)", "line",
       caption("Figure 34: PID System Response Using Intelligent Heat Distribution"), "text-layer",
       uncited(), SEC_94,
       "Intelligent distribution with manual control: two curves on a shared time axis, a blue "
       "rising error and an orange decaying demand, dual ordinates (-7 to 0 left, 0 to 14 right), "
       "no legend, in-plot title 'PID Control'. Time 0 to 60 min. The error curve rises toward zero "
       "from below, which is the first panel in the control sequence where the bath converges "
       "without overshoot.",
       geometry("line", **PANEL))

figure(39, 2, "34 (b)", "line",
       caption("Figure 34: PID System Response Using Intelligent Heat Distribution"), "text-layer",
       uncited(), SEC_94,
       "The uniformity half of the exhibit: a single curve rising to a peak near 10 min and decaying "
       "over the hour, ordinate 'Standard Deviation of Temperature Distribution' 0 to 2.5 deg C, "
       "no legend, in-plot title 'PID Control Temperature Uniformity', lettered '(b) Uniformity over "
       "Time'. Two panels, one caption, and the caption names neither the error nor the standard "
       "deviation.",
       geometry("line", **PANEL))

figure(40, 1, "35", "heatmap-or-contour",
       caption("Figure 35: Heat Map of PID System Response Using Intelligent Heat Distribution"),
       "text-layer",
       cited(39, 40, ["Figure 35"], 1,
             "The heat map corresponding to this control is shown below in Figure 35.", "as-shown-in",
             lead_page=39),
       SEC_94,
       "The final state of the whole paper: a blocky field, dark blue at the margins and a yellow "
       "band across the interior, colour bar at the right spanning 30 to 37 deg C, in-plot title "
       "'Optimized PID Heat Map'. Time 0 to 60 min inverted, position 0 to 1.5 m. Yellow at 37 deg C "
       "is the objective and the band is the region the controller holds there, but the bar's lower "
       "bound of 30 deg C covers a range the run never reaches, which compresses the band that "
       "matters into the top fifth of the scale.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

# ============================================================ exclusions
EXCLUSIONS = [
    {"page": 1, "bbox": REG[(1, 1)], "reason": "not-an-exhibit",
     "note": "the summary sheet's 'For office use only / Team Control Number 44845 / Problem "
             "Chosen A' control box and its fill-in rules, boxed as a region because it is a raster "
             "stamp - form lettering with no data, no axis and no caption"},
    {"page": 44, "bbox": REG[(44, 1)], "reason": "not-an-exhibit",
     "note": "the letterhead of the paper's fictional consulting firm ('Superior Products*: Applied "
             "Mathematical Consulting Firm') - a blue bracket glyph beside two lines of serif type, "
             "logo art with no data, no axis and no caption"},
]

RULES = [
    "Measure first, then read the pixels: fifty-three measured regions resolve into fifty figure "
    "rows, one table and two exclusions, and no region is counted twice [place.page_order].",
    "A panel measured as its own box is its own row: the fifteen two-panel exhibits of this paper "
    "(Figures 17 to 28, 32, 33 and 34) are split into two measured boxes each, so the figure count "
    "follows the boxes and panel_count names the exhibit the row belongs to [geometry.panel_count].",
    "A panel's family is its own, not its exhibit's: Figure 18 pairs a heat map with a line plot "
    "and Figures 32 and 33 pair a line plot with a heat map, so the two rows of one captioned "
    "exhibit can carry different families [geometry.family].",
    "Two ordinates carrying the SAME quantity are a geometry defect, not a family: Figures 22, 30, "
    "31 and 34 print left and right y axes both labelled or both serving the same objective "
    "function, and the rows stay line rather than composite [geometry.family].",
    "A table with no caption and no printed label is still a table: the p11 grid is named only by "
    "the p10 pointer sentence 'The following table contains the model parameters', so its "
    "caption_source is none and its numbering is none [place.section_kind].",
    "A caption the linear text layer cannot carry is typed from the printed block geometry: the "
    "two-column wrap interleaves Figures 7 and 29 with the body text, so both are transcribed from "
    "the block as printed rather than quoted from the page string [place.doc_order].",
    "Form lettering and logo art boxed as regions are not exhibits: the summary-sheet control box "
    "on p1 and the consulting-firm letterhead on p44 are excluded as not-an-exhibit rather than "
    "counted as figures [place.area_frac].",
    "Section placement follows the printed heading positions: a region on p7 above the 3.2 heading "
    "belongs to 3.1 and a region on p35 above the 9.2 heading belongs to 9.1, whatever carry-over "
    "the context dump reports [place.section_path].",
]

NOTE = """\
Paper 92, Team 44845, the hot-bath thermal-fluid paper. Forty-four pages, fifty-three measured
regions over twenty-nine of them, and the fifty-three resolve into FIFTY FIGURE ROWS, ONE TABLE and
TWO EXCLUSIONS. Unaccounted zero. The paper prints thirty-five figure captions and NO table caption
or table number in any of its forty-four pages: the single table is the unlabelled parameter grid on
p11, named only by the p10 sentence "The following table contains the model parameters that can be
altered as well as their nominal values". Fifteen exhibits are two-panel and supply thirty of the
fifty rows; the panels are boxed separately and each row keeps its own family, so Figure 18, Figure
32 and Figure 33 each contribute one heat map row and one line-plot row under a single caption.

Citation is uneven. Fourteen of the thirty-five captions are carried into a pointer sentence - "as
shown below in Figure 1", "shown at right in Figure 3", "this is shown in Figure 7 at right",
"Figure 11 displays", "shown in Figure 22 below" - and twenty-one figures are named by no sentence
at all, most of them in the sensitivity sections where the pointer degenerates into "shown below" or
"a similar plot is shown below" with no label. Four pointers sit a page before their figure: Figures 24, 31,
32 and 35 are each introduced on the page before the one that prints them. The worst case
is Figure 33: p38 writes "The same results are shown in 33 below", dropping the word "Figure"
entirely, so no page of the paper ever prints "Figure 33".

Two captions could not be quoted from the linear text layer at all, because the two-column wrap runs
the caption's second line through the body column: p11 gives "Figure 7: Graphical Illustration of the
Ther- be zero, as no mass or energy can be accu- modynamic System" and p35 gives "Figure 29:
Illustration of Properly Tuned of the three components of a PID controller PID Controller[11]". Both
are typed from the printed block geometry, hyphen break included. Figure 29 also carries a label from
its source: the raster itself prints "Figure 20a. Illustration of Properly Tuned", so a foreign
figure number is baked into the paper's own Figure 29, and its abscissa is labelled with a bare "t"
and its ordinate not at all. Figure 16's in-plot title misspells "propagation" as "Propogation";
Figure 23's panel title reads "Varied of Diffusivity over Full Length"; Figure 28's first panel title
is clipped mid-phrase.

The exhibits themselves are honest about one thing and careless about another. Honest: the three
heat-transfer-coefficient plots (Figures 4, 5, 6) each print the mean they are replaced by, and the
two near-flat body-property panels (Figure 28) visibly justify that substitution. Careless: almost
every comparison pair is drawn on non-common scales. Figures 19(a) and 19(b), 20(a) and 20(b), 21(a)
and 21(b), 25(a) and 25(b) and 26(a) and 26(b) use colour or ordinate windows that differ by an order
of magnitude, so the "comparison" cannot be read off the page without rescaling one half; Figure 10
fills its frame with a slope whose ordinate spans 1.8 deg C; Figure 22 puts the same objective
function on two ordinates at once; Figures 32(b) and 33(b) certify uniformity with colour bars 0.0003
deg C wide. No exhibit in the paper prints a raw data value on its marks except the three annotated
optima (38.0425 deg C, 0.006518 kg/s) and the borrowed gains Kp = 5, Ki = 3, Kd = 3 of Figure 29.

Families: line 31, heatmap-or-contour 16, flowchart-or-schematic 3, table-grid 1. The two excluded
regions are form lettering (p1's control box) and logo art (p44's consulting-firm letterhead).
"""

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUSIONS,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc92-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUSIONS))
print("figures+table+excluded", len(ITEMS) + len(TABLES) + len(EXCLUSIONS))
