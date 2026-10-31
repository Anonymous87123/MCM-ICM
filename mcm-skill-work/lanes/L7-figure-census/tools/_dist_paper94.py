"""Hand census of P-A-2016-48649-e4d30266 (Team 48649, 44 pages, 35 measured regions).

A bathtub heat-loss paper: ANSYS for the temperature distribution, MATLAB for the curves, FCE for
the choice between two inflow strategies. Thirty-five measured regions resolve into TWENTY-EIGHT
FIGURE ROWS, SIX TABLE ROWS and ONE EXCLUSION, unaccounted zero.

  p8  r1  Graph 1   surface-or-3D           tub as a translucent solid with the inflow pipe
  p9  r1  Graph 2   flowchart-or-schematic  BWOP model tree
  p15 r1  Table 3   table-grid              tub dimensions
  p16 r1  Graph 3   surface-or-3D           hex-dominant element
  p16 r2  Graph 4   surface-or-3D           the tub as a 3-D solid
  p16 r3  Graph 5   surface-or-3D           tetrahedral mesh, WITH scale bar
  p16 r4  Graph 6   heatmap-or-contour      isothermal intersecting section
  p17 r1  Graph 7   heatmap-or-contour      isothermal tub body from outside
  p17 r2  Table 4   table-grid              volume-integral report
  p18 r1  Graph 8   flowchart-or-schematic  BWP model tree
  p19 r1  Graph 9   surface-or-3D           tub with a bather
  p19 r2  Graph 10  heatmap-or-contour      isothermal, bather not shown
  p20 r1  Graph 11  heatmap-or-contour      isothermal on the body surface
  p22 r1  Graph 12  line                    water-air cooling curve
  p23 r1  Graph 13  line                    water-bathtub cooling curve, 0-3000 min
  p23 r2  Graph 14  line                    total cooling curve
  p24 r1  --        not-an-exhibit         display equation
  p26 r1  Graph 15  line                    continuous-inflow run
  p28 r1  Graph 16  line                    discontinuous-inflow run, sawtooth
  p29 r1  Table 7   table-grid              FCE input factors
  p30 r1  Table 9   table-grid              velocity sweep
  p31 r1  Graph 17  line                    volume temperatures against velocity
  p31 r2  Graph 18  line                    heat flux against velocity
  p32 r1  Table 10  table-grid              inflow-temperature sweep
  p32 r2  Graph 19  line                    volume temperatures against inflow temperature
  p33 r1  Graph 20  line                    heat flux against inflow temperature
  p33 r2  Table 11  table-grid              air-temperature sweep
  p34 r1  Graph 21  line                    volume temperatures against air temperature
  p34 r2  Graph 22  line                    heat flux against air temperature
  p36 r1  Graph 23  line                    five surface areas
  p37 r1  Graph 24  line                    five tub volumes
  p38 r1  Graph 25  line                    five wall materials
  p39 r1  Graph 26  line                    five bather volumes
  p40 r1  Graph 27  photo-or-raster-image    the bubble layer as a bumpy slab
  p41 r1  Graph 28  line                    three bubble-layer coefficients

THE PAPER PRINTS ELEVEN NUMBERED TABLES AND ONLY SIX WERE BOXED. Tables 1 and 2 (pp6-7), Table 5
(p26), Table 6 (p28) and Table 8 (p29) print in full - caption, header row and data - and no measured
region covers any of them, so the five are declared gaps rather than rows. The extraction blind spot
is the open grid: these tables are drawn with rules that do not close a rectangle, and the region
finder needs a box.

The exhibit label is "Graph N:", a form outside the lane's numbering vocabulary, so every figure row
carries numbering "none" while printed_number records the number the caption actually prints.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2016-48649-e4d30266"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]
        KIND[(_pg["page"], _i)] = _r["kind"]

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


def place(page: int, reg: int, kind: str, path: list[str]) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
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


def caption(verbatim: str, numbering: str = "none", position: str = "below",
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


S4 = ["4 Model for bathtub without a person in it (BWOP model)"]
S44 = ["4.4 Simulation of BWOP model based on ANSYS"]
S5 = ["5 Model for bathtub with a person in it (BWP model)"]
S51 = ["5 Model for bathtub with a person in it (BWP model)",
       "5.1 Simulation of the temperature distribution if the person is still"]
S53 = ["5 Model for bathtub with a person in it (BWP model)",
       "5.3 Simulation of BWP model with MATLAB"]
S541 = ["5 Model for bathtub with a person in it (BWP model)", "5.4 Heat addition model",
        "5.4.1 Continuous Inflow model (CI model)"]
S542 = ["5 Model for bathtub with a person in it (BWP model)", "5.4 Heat addition model",
        "5.4.2 Discontinuous Inflow model (DCI model)"]
S543 = ["5 Model for bathtub with a person in it (BWP model)", "5.4 Heat addition model",
        "5.4.3 FCE of the two models"]
S61 = ["6 Sensitivity analysis", "6.1 Sensitivity analysis for BWOP"]
S611 = S61 + ["6.1.1 Inflow Velocity"]
S612 = S61 + ["6.1.2 Inflow Temperature"]
S613 = S61 + ["6.1.3 Air Temperature"]
S62 = ["6 Sensitivity analysis", "6.2 Sensitivity analysis for BWP"]
S621 = S62 + ["6.2.1 Different surface area of the bathtub"]
S622 = S62 + ["6.2.2 Different volume of the bathtub"]
S623 = S62 + ["6.2.3 Different material of the bathtub"]
S624 = S62 + ["6.2.4 Different volume of person in the bathtub"]
S7 = ["7 Model for Cleansing with a Bubble Bath Additive (CBBA model)"]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_PRINTED = schema.printed_lines(PID)
for _group in (S4, S44, S5, S51, S53, S541, S542, S543, S61, S611, S612, S613, S62,
               S621, S622, S623, S624, S7):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN and schema.norm(_label) not in _PRINTED:
            raise SystemExit(f"section label is neither an indexed heading nor a printed line: "
                             f"{_label!r}")

ITEMS: list[dict] = []
TABLES: list[dict] = []


def figure(page: int, reg: int, number: str, family: str, cap: dict, cap_src: str,
           mention: dict, section: list[str], note: str, geo: dict | None = None,
           section_kind: str = "other", confidence: str = "high") -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap["verbatim"],
        "caption": cap, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    })


def table(page: int, reg: int, cap: dict, cap_src: str, mention: dict, section: list[str],
          note: str, rows: int, cols: int, numeric: int, text: int, rule: str,
          header_rows: int = 1, merged: bool = False, zebra: bool = False,
          diagonal: bool = False, units_in_header: bool = False, decimal: bool = False,
          continued: bool = False, width: str = "full", section_kind: str = "model",
          note_sentence: str = "", confidence: str = "high") -> None:
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
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


# ============================================================ the tub as a body
figure(8, 1, "1", "surface-or-3D",
       caption("Graph 1: The hot water tube model"), "text-layer",
       cited(8, 8, ["Graph 1"], 1,
             "As Graph 1 shows, the addition of the hot water is equivalent to a hot water tube from "
             "faucet to the water outlet"),
       S4,
       "The tub drawn as a translucent grey solid in a CAD perspective view inside a dark navy "
       "frame, with a thin pipe passing through it end to end - the 'hot water tube' the heating "
       "process is reduced to. No axes, no graduation, no legend, no printed value, no lettering of "
       "any kind: the caption is the only text the exhibit carries. It is a rendering, not a data "
       "surface, so nothing on the page can be read as a measurement.",
       geometry("surface-or-3D", three_d="isometric"))

figure(9, 1, "2", "flowchart-or-schematic",
       caption("Graph 2: The framework of BWOP model"), "text-layer", uncited(), S4,
       "The model tree of chapter 4: a top box 'BWOP' branches to 'Heat Loss' and 'Heat Addition', "
       "the middle row holds 'Water-Air', 'Real Simulation' and 'Hot-water Tube', and arrows gather "
       "into 'Real Simulation Model' and 'Hot-water Tube Model' at the foot. No axes, no legend, no "
       "printed value. The chart is the outline of the chapter - every branch becomes a section - "
       "and no sentence anywhere names it.",
       geometry("flowchart-or-schematic"))

table(15, 1,
      caption("Table 3: Size of the tub", numbering="Table N:", position="above"),
      "text-layer",
      cited(15, 15, ["Table 3"], 1,
            "To adjust to the real size in Table 3 of the tub, we define the tub model as Graph 4."),
      S44,
      "The tub's dimensions, printed above its own grid: four columns (cubage(m3), height(m), "
      "top-surface-size(m,m), bottom-surface-size(m,m)) and two rows - the header and one data row "
      "(0.3, 0.4, 1.4(length),0.7(width), 1.0(length),0.5(width)). Heavy rule under the header, thin "
      "rule at the foot, no vertical strokes. TWO UNIT PAIRS ARE BAKED INTO THE CELLS as words - "
      "'(length)' and '(width)' - because the header can only promise 'm,m' for a pair of numbers, "
      "so half of this table's unit information sits inside its data cells.",
      rows=2, cols=4, numeric=2, text=2, rule="booktabs", header_rows=1,
      units_in_header=True, section_kind="model", note_sentence="")

# ============================================================ the ANSYS run
figure(16, 1, "3", "surface-or-3D",
       caption("Graph 3: 3-D Hex Dominant model"), "text-layer",
       cited(15, 16, ["Graph 3"], 1,
             "In the 3-D model analysis, we use Hex Dominant unit whose shape is like Graph 3.",
             lead_page=15),
       S44,
       "One mesh element drawn on its own as a grey-white 3-D block standing on end, a single face "
       "shaded lavender, on the dark navy ground the ANSYS screenshots share. No axes, no scale bar, "
       "no legend, no lettering. The exhibit shows the element's SHAPE only, exactly as the sentence "
       "above it says; the pointer comes on p15, a page before the picture.",
       geometry("surface-or-3D", three_d="isometric"))

figure(16, 2, "4", "surface-or-3D",
       caption("Graph 4: 3-D Bathtub model"), "text-layer",
       cited(15, 16, ["Graph 4"], 1,
             "To adjust to the real size in Table 3 of the tub, we define the tub model as Graph 4.",
             lead_page=15),
       S44,
       "The whole tub as a 3-D solid: an open trapezoidal basin, one end wall shaded blue, with thin "
       "pipes entering at the top left and leaving at the bottom right, printed beside Graph 3 on a "
       "single shared caption line. No axes, no scale, no legend, no lettering. It fixes the geometry "
       "that Table 3 then sizes, and it is the only exhibit in the pair the body text returns to.",
       geometry("surface-or-3D", three_d="isometric"))

figure(16, 3, "5", "surface-or-3D",
       caption("Graph 5: Mesh Carve up"), "text-layer",
       cited(16, 16, ["Graph 5"], 1,
             "Using the ANSYS mesh we get the mesh carve up graph for the bathtub as Graph 5."),
       S44,
       "The tetrahedral volume mesh of the tub: grey-blue facets with black wireframe edges over a "
       "light-blue gradient, inlet pipe at the upper left and outlet at the lower right. THIS IS THE "
       "ONLY EXHIBIT IN THE PAPER THAT PRINTS A SCALE - a segmented bar reading 0.000, 0.018, 0.035, "
       "0.053 and 0.070 m - so it is the one picture a reader can measure instead of trusting Table "
       "3. No axes, no colour bar, no legend.",
       geometry("surface-or-3D", three_d="surface-mesh", numbers=True))

figure(16, 4, "6", "heatmap-or-contour",
       caption("Graph 6: The isothermal diagram of the intersecting surface"), "text-layer",
       cited(16, 16, ["Graph 6"], 2,
             "Using FEM by ANSYS, we get the isothermal diagram both inside and outside the bathtub "
             "as Graph 6 and Graph 7."),
       S44,
       "A 2-D isothermal cross-section through the tub: a cyan field filling the basin with a small "
       "green-yellow hot patch low on the right beside a red bar, and a colour bar at the left "
       "reading 3.13e+02 to 3.18e+02 with NO UNIT PRINTED. No axis titles, no ticks, no legend, no "
       "printed value: the kelvin has to be inferred from the constants table two chapters earlier, "
       "and the field's floor sits above every temperature the paper later reports.",
       geometry("heatmap-or-contour", legend="outside-left", colorbar=True))

figure(17, 1, "7", "heatmap-or-contour",
       caption("Graph 7: The isothermal diagram of the tub body from outside"), "text-layer",
       cited(16, 17, ["Graph 7"], 2,
             "Using FEM by ANSYS, we get the isothermal diagram both inside and outside the bathtub "
             "as Graph 6 and Graph 7.", lead_page=16),
       S44,
       "The same solution seen from OUTSIDE and in three dimensions: a deep blue interior under "
       "lighter cyan rims with the hot patch again at the outlet, colour bar at the left 3.13e+02 to "
       "3.18e+02, still with no unit. No axis titles, no legend, no printed value. The pair is the "
       "paper's one honest comparison - same colour window, same solution - although the first "
       "member is a flat cut and this one is a perspective render, so the two cannot be laid over "
       "one another.",
       geometry("heatmap-or-contour", legend="outside-left", colorbar=True, three_d="isometric"))

table(17, 2,
      caption("Table 4: Report on Volume Integral"), "text-layer",
      cited(17, 17, ["table 4"], 2,
            "Calculate the result we get statistic in table 4."),
      S44,
      "The volume-integral report of the ANSYS run: six columns and two rows, with headings stacked "
      "three lines deep - 'Average tub-wall heat flux(W)', 'Average top surface heat flux(W)' and "
      "four volume statistics, -0.06104, -1.3394727, 313.1946, 318.0238, 312.9532, 40.4178. Heavy "
      "rule under the header, thin at the foot, no vertical strokes. THE UNITS DISAGREE ACROSS ONE "
      "ROW: the third heading prints 'Temp(k)' with a lower-case k, the fourth and fifth 'Temp(K)', "
      "and the sixth 'Temp(ºC)' - and that Celsius cell cannot be the conversion of any Kelvin value "
      "beside it (313.1946 K is 40.04 deg C, 318.0238 K is 44.87, 312.9532 K is 39.80, none of them "
      "40.4178). The pointer calls the exhibit 'table 4' in lower case.",
      rows=2, cols=6, numeric=6, text=0, rule="booktabs", header_rows=1,
      units_in_header=True, section_kind="model", note_sentence="")

# ============================================================ the bather
figure(18, 1, "8", "flowchart-or-schematic",
       caption("Graph 8: The framework of BWP model"), "text-layer",
       cited(18, 18, ["Graph 8"], 1, "Graph 8 shows the framework of BWP model",
             "figure-n-shows"),
       S5,
       "A symmetric tree of chapter 5: a top box 'BWP' branches to 'Heat Loss' and 'Heat Addition', "
       "each of those to two boxes (Water-Air, Water-Bathtub, Continuous inflow, Discontinuous "
       "inflow), and crossing arrows gather everything into 'Continuous model' and 'Discontinuous "
       "model'. No axes, no legend, no printed value. Like Graph 2 it doubles as an outline, and it "
       "is the only figure in the two chapters that a sentence introduces by name at the point it "
       "prints.",
       geometry("flowchart-or-schematic"))

figure(19, 1, "9", "surface-or-3D",
       caption("Graph 9: Bathtub model with person"), "text-layer",
       cited(19, 19, ["Graph 9"], 1,
             "Graph 9 shows the model of the bathtub when a person is cleaning.", "figure-n-shows"),
       S51,
       "The populated tub: the tapered basin as a 3-D solid with a bather standing in it, the figure "
       "modelled as a plain cylinder with a sphere for the head, on the same dark navy ground as the "
       "ANSYS screenshots. No axes, no scale, no legend, no colour bar, no lettering at all. The "
       "bather's volume is the only property the model gives it, and this exhibit is the only place "
       "the whole body is drawn.",
       geometry("surface-or-3D", three_d="isometric"), confidence="medium")

figure(19, 2, "10", "heatmap-or-contour",
       caption("Graph 10: The isothermal diagram of the tub body with a person "
               "(We don’t show the person in the graph)"),
       "text-layer",
       cited(19, 19, ["Graph 10"], 1,
             "Graph 10 show the isothermal in the bathtub and Graph 11 show the temperature "
             "distribution on the body surface of the person.", "figure-n-shows"),
       S51,
       "The isothermal solution of the populated tub seen from above: a flat field over the basin in "
       "blue-to-green bands with a red inflow stub and a thin outlet line, colour bar at the left "
       "3.12e+02 to 3.18e+02 in 1e-02 steps and still no unit. No axis titles, no legend, no printed "
       "value. The caption states its own omission in brackets - '(We don’t show the person in the "
       "graph)' - so the field is the water only, and the bather's absence is the point rather than "
       "an accident of the drawing.",
       geometry("heatmap-or-contour", legend="outside-left", colorbar=True))

figure(20, 1, "11", "heatmap-or-contour",
       caption("Graph 11: The isothermal diagram on the body surface of a person"), "text-layer",
       cited(19, 20, ["Graph 11"], 1,
             "Graph 10 show the isothermal in the bathtub and Graph 11 show the temperature "
             "distribution on the body surface of the person.", lead_page=19),
       S51,
       "The temperature field ON THE BATHER rather than on the water: a 3-D render of the body "
       "surface lying in the tub, coloured cyan-green over a blue-violet field, colour bar at the "
       "left 3.13e+02 to 3.18e+02, no unit. No axis titles, no legend, no printed value. It exists to "
       "support one sentence - that the surface temperature distributes unevenly while the bather "
       "keeps still - and it is the only exhibit in the paper that shows a human being as a "
       "temperature surface.",
       geometry("heatmap-or-contour", legend="outside-left", colorbar=True, three_d="isometric"))

# ============================================================ cooling curves
figure(22, 1, "12", "line",
       caption("Graph 12: Temperature curve of Water-Air heat transfer process"), "text-layer",
       cited(22, 22, ["Graph 12"], 1,
             "Graph 12 shows the heat loss caused by the heat convection between the water surface "
             "and the air.", "figure-n-shows"),
       S53,
       "One smooth decay curve of water temperature over 0 to 1000 min, ordinate 300 to 318 K, "
       "in-plot title 'Temperature curve of Water-Air heat transfer process'. Single series, no "
       "legend, no markers, no printed value; abscissa 'Time/min', ordinate 'Temperature/K'. It is "
       "the air-convection half of the dissipation model and the first of three curves that are meant "
       "to be read together.",
       geometry("line"))

figure(23, 1, "13", "line",
       caption("Graph 13: Temperature curve of Water-Bathtub heat transfer process"), "text-layer",
       cited(23, 23, ["Graph 13"], 1,
             "Graph 13 shows the heat loss only caused by the heat conduction between the water and "
             "the bathtub.", "figure-n-shows"),
       S53,
       "The bathtub-conduction path over a WIDER window than its siblings - 0 to 3000 min, ordinate "
       "308 to 318 K - so the curve is visibly flatter, which the body text reads as the tub losing "
       "heat 'much slower' than the water surface. One series, no legend, no markers. THE IN-PLOT "
       "TITLE MISSPELLS THE PATH as 'Water-Buthtub' while the caption under it prints "
       "'Water-Bathtub' correctly, and the three curves of this set are drawn on two different time "
       "axes, so the comparison the text draws cannot be made from the pages.",
       geometry("line"))

figure(23, 2, "14", "line",
       caption("Graph 14: Temperature curve of total heat transfer process"), "text-layer",
       cited(23, 23, ["Graph 14"], 1,
             "Graph 14 shows the total heat dissipation in BWP model which contains the Water-Air "
             "transfer and the Water-Bathtub transfer.", "figure-n-shows"),
       S53,
       "The total dissipation, 0 to 1000 min, ordinate 300 to 318 K, in-plot title 'Temperature curve "
       "of the total heat transfer process'. One curve, no legend, no markers, no printed value. It "
       "is the sum of the two paths above and the pointer says so, but it is drawn on Graph 12's time "
       "axis and not on Graph 13's, so only two of the three curves can be overlaid.",
       geometry("line"))

figure(26, 1, "15", "line",
       caption("Graph 15: Temperature curve of the continuous inflow process"), "text-layer",
       cited(26, 26, ["Graph 15"], 1,
             "We simulate the Continuous Inflow model with MATLAB and we get the temperature curve "
             "as Graph 15 shows."),
       S541,
       "The continuous-inflow run: the temperature falls steeply through the first hundred minutes "
       "and then sits on a noisy plateau near 313 K for the rest of the bath, ordinate 310 to 319 K, "
       "in-plot title 'Temperature curve of the continuous inflow process'. One curve, no legend, no "
       "markers, no printed value. The plateau is the whole argument for this model - the faucet "
       "holds the bath at the comfort temperature - and the ripple on it is the only place in the "
       "paper where the simulation's noise is visible.",
       geometry("line"))

figure(28, 1, "16", "line",
       caption("Graph 16: Temperature curve of the discontinuous inflow process"), "text-layer",
       uncited(), S542,
       "The discontinuous-inflow run: the water cools to about 312 K and then OSCILLATES in a regular "
       "sawtooth between roughly 312 and 314 K to the end of the bath - the two thresholds the text "
       "sets (tl = 312 K, th = 314 K) drawn as a cycle on the temperature axis. Ordinate 310 to "
       "319 K, in-plot title 'Temperature curve of the discontinuous inflow process'. One curve, no "
       "legend, no markers. No sentence names it: the body text points at 'this graph' without a "
       "number.",
       geometry("line"))

# ============================================================ FCE and the sweeps
table(29, 1,
      caption("Table 7: values of factors and allocations", numbering="Table N:", position="above"),
      "text-layer",
      cited(29, 29, ["Table 7"], 1,
            "Based on the actual statistics of the 2 strategies, we get the values of each factor "
            "from section 5.4 and show them in Table 7."),
      S543,
      "The FCE input table: five columns (Model, Water need (m3), The comfortable degree, operation "
      "complexity, operative difficulty index) and three rows - the header, CI and DCI. Booktabs "
      "rules, no vertical strokes, one unit in the header. TWO OF THE FOUR CRITERIA ARE ROUND "
      "ASSUMPTIONS - operation complexity 1 against 0.01064, difficulty index 10 against 1 - so the "
      "FCE weights that follow are built on two invented numbers. The transposition defect: p27 "
      "derives the CI comfortable degree as 'CdCI =10.6021' and this table prints it as 10.0621.",
      rows=3, cols=5, numeric=4, text=1, rule="booktabs", header_rows=1,
      units_in_header=True, section_kind="evaluation", note_sentence="")

table(30, 1,
      caption("Table 9: Results by Changing Inflow Velocity", numbering="Table N:", position="above"),
      "text-layer",
      cited(30, 30, ["Table 9"], 2,
            "By doing simulation we get the result shown in Table 9, Table 10 and Table 11."),
      S611,
      "Seven columns - Inflow Velocity (m/s), Inflow Temp(K), Air Temp(K), Average top surface heat "
      "flux(W) and the volume-average, volume-maximum and volume-minimum temperatures - and six "
      "rows, the header plus five velocities from 0.01 to 0.05 m/s. Booktabs rules, no vertical "
      "strokes, units in the header, four decimals throughout. TWO COLUMNS ARE CONSTANT down the "
      "whole grid (318 K inflow and 298 K air) because only the velocity is swept, so fourteen of the "
      "thirty-five data cells carry no information; the heat flux rises from 1.1590 to 1.6765 W while "
      "the volume-maximum temperature moves by 0.1 K.",
      rows=6, cols=7, numeric=7, text=0, rule="booktabs", header_rows=1,
      units_in_header=True, section_kind="sensitivity", note_sentence="")

figure(31, 1, "17", "line",
       caption("Graph 17: Temperature-Inflow Velocity graph"), "text-layer", uncited(), S611,
       "Three series against inflow velocity 0.01 to 0.05 m/s: the volume-average and volume-minimum "
       "temperatures rise with velocity while the volume-maximum temperature stays flat at 318 K, "
       "ordinate 309 to 319 K, abscissa 'Inflow Velocity/(m/s)', in-plot legend entries "
       "'Volume-average Temp', 'Volume-maximum Temp' and 'Volume-minimum Temp'. No markers, no "
       "printed value. The ordinate floor is set by the lowest average temperature, so the flat "
       "maximum hugs the top edge and the two rising curves are compressed into the lower half.",
       geometry("line", legend="inside"))

figure(31, 2, "18", "line",
       caption("Graph 18: Average top surface heat-Inflow Velocity graph"), "text-layer",
       uncited(), S611,
       "A single curve of average top-surface heat flux against inflow velocity 0.01 to 0.05 m/s, "
       "ordinate 1.1 to 1.8 'heat flux/W', rising from about 1.16 to 1.68 W. One series, no markers, "
       "no legend - because there is nothing to label - and no printed value. It is the heat-flux half "
       "of the pair whose temperature half is Graph 17, and the two halves share no scale: the table "
       "they come from puts both quantities on one row.",
       geometry("line"))

table(32, 1,
      caption("Table 10: Results by Changing Inflow Temperature", numbering="Table N:",
              position="above"),
      "text-layer",
      cited(30, 32, ["Table 10"], 2,
            "By doing simulation we get the result shown in Table 9, Table 10 and Table 11.",
            lead_page=30),
      S612,
      "The inflow-temperature sweep in the same seven columns as Table 9: 314, 316, 318, 320 and "
      "322 K at a fixed 0.02 m/s with air at 298 K, heat flux rising from 1.1525 to 1.7287 W. "
      "Booktabs, units in the header, no vertical strokes. CROSS-TABLE DEFECT: its 318 K row and "
      "Table 9's 0.02 m/s row describe the same run and print the same three volume temperatures "
      "(313.4178, 318.024, 312.9532), but the heat flux is 1.5652 W here and 1.4406 W there - the "
      "same simulation reported two ways.",
      rows=6, cols=7, numeric=7, text=0, rule="booktabs", header_rows=1,
      units_in_header=True, section_kind="sensitivity", note_sentence="")

figure(32, 2, "19", "line",
       caption("Graph 19: Volume Temperature- Inflow Temperature graph"), "text-layer", uncited(),
       S612,
       "Three series against inflow temperature 314 to 322 K: volume-maximum, volume-average and "
       "volume-minimum all rise almost linearly and almost together, ordinate 308 to 324 K, "
       "abscissa 'Inflow Temperature/K', in-plot legend 'Volume-average Temp', 'Volume-maximum Temp' "
       "and 'Volume-minimum Temp'. No markers, no printed value. The maximum sits a little above 320 "
       "and the other two a little below 316, so the three curves cross the middle of the frame and "
       "the ordering of the three statistics inverts between the two ends of the sweep.",
       geometry("line", legend="inside"))

figure(33, 1, "20", "line",
       caption("Graph 20: Average top surface heat - Inflow Temperature graph"), "text-layer",
       uncited(), S613,
       "One curve of average top-surface heat flux against inflow temperature 314 to 322 K, ordinate "
       "1.1 to 1.9 'heat flux/W', rising in steps and plateaus rather than on a straight line. Single "
       "series, no markers, no legend, no printed value. The steps come from the sweep's five "
       "discrete inflow temperatures, which the curve joins with straight segments.",
       geometry("line"))

table(33, 2,
      caption("Table 11: Results by Changing Air Temperature", numbering="Table N:", position="above"),
      "text-layer",
      cited(30, 33, ["Table 11"], 2,
            "By doing simulation we get the result shown in Table 9, Table 10 and Table 11.",
            lead_page=30),
      S613,
      "The air-temperature sweep: 294, 296, 298, 300 and 302 K at 0.02 m/s and 318 K inflow, heat "
      "flux falling from 1.7287 to 1.1525 W as the room warms. Same seven columns, booktabs rules, "
      "units in the header. This table does agree with its siblings where the inputs coincide: its "
      "298 K row is Table 10's 318 K row to the digit (1.5652 W, 313.4178, 318.024, 312.9532). A "
      "stray word 'Table' prints at the left margin immediately under the grid.",
      rows=6, cols=7, numeric=7, text=0, rule="booktabs", header_rows=1,
      units_in_header=True, section_kind="sensitivity", note_sentence="")

figure(34, 1, "21", "line",
       caption("Graph 21: Volume Temperature - Air Temperature graph"), "text-layer", uncited(),
       S613,
       "Three series against air temperature 294 to 302 K, ordinate 311 to 319 K, abscissa "
       "'Air Temperature/K', in-plot legend 'Volume-average Temp', 'Volume-maximum Temp' and "
       "'Volume-minimum Temp'. The maximum stays flat near 318 K while the average and the minimum "
       "rise with the room temperature. No markers, no printed value.",
       geometry("line", legend="inside"))

figure(34, 2, "22", "line",
       caption("Graph 22: Average top surface heat - Air Temperature graph"), "text-layer",
       uncited(), S613,
       "One curve of average top-surface heat flux against air temperature 294 to 302 K, ordinate 1.1 "
       "to 1.9 'heat flux/W', falling as the room warms - the mirror image of Graph 20, as it must be "
       "when the driving difference between water and air shrinks. Single series, no markers, no "
       "legend, no printed value.",
       geometry("line"))

# ============================================================ the 6.2 sweeps
figure(36, 1, "23", "line",
       caption("Graph 23: Temperature curve with different surface area of the bathtub"),
       "text-layer",
       cited(36, 36, ["Graph 23"], 1, "From Graph 23 we can easily find that"),
       S621,
       "Five temperature-decay curves over 0 to 1000 min for surface areas s = 1.4, 1.5, 1.53, 1.6 "
       "and 1.7 m2, ordinate 300 to 318 K, in-plot legend at the upper right. The curves lie almost "
       "on top of one another - which IS the finding the pointer states ('the surface area of the "
       "bathtub have very small effect') - and it is also why the exhibit cannot show the effect it "
       "argues for: five lines inside a 2 pt band read as one line.",
       geometry("line", legend="inside"))

figure(37, 1, "24", "line",
       caption("Graph 24: Temperature curve with different volume area of the bathtub"), "text-layer",
       cited(37, 37, ["Graph 24"], 1, "From Graph 24 we can easily find that"),
       S622,
       "Five decay curves over 0 to 1000 min for tub volumes V = 230, 270, 300, 320 and 350 L, "
       "ordinate 300 to 318 K, in-plot legend upper right. Here the curves separate cleanly and the "
       "larger the volume the slower the fall, so this is the one exhibit of the four whose effect is "
       "visible on the page. The caption says 'volume area', which is not a quantity: the body text "
       "says volume.",
       geometry("line", legend="inside"))

figure(38, 1, "25", "line",
       caption("Graph 25: Temperature curve with different material of the bathtub"), "text-layer",
       cited(38, 38, ["Graph 25"], 1, "From Graph 25 we can easily find that"),
       S623,
       "Five near-coincident decay curves over 0 to 1000 min for wall materials, ordinate 300 to "
       "318 K, with the conductivity printed inside the legend entries themselves ('cast iron l=42', "
       "'acrylic l=1.4', 'steel l=36', 'porcelain l=0.87', 'wood l=0.38') rather than in a table. No "
       "markers, no printed value elsewhere. The order of the curves does not follow the "
       "conductivity - steel conducts almost as strongly as cast iron and its curve sits nearer the "
       "insulating pair - but the five are so close that the reader cannot check it.",
       geometry("line", legend="inside"))

figure(39, 1, "26", "line",
       caption("Graph 26: Temperature curve with different volume of person"), "text-layer",
       cited(39, 39, ["Graph 26"], 1, "From Graph 26 we can easily find that"),
       S624,
       "Five decay curves over 0 to 1000 min for bather volumes V = 30, 40, 50, 60 and 75 L, ordinate "
       "300 to 318 K, legend upper right, the 30 L curve lowest. COPY-PASTE DEFECT IN THE TEXT THE "
       "FIGURE TYPESETS: the pointer that cites it reads 'the material of the bathtub have larger "
       "effect on the total heat loss than the surface or the material of the bathtub', carried over "
       "from the material section and naming the wrong variable twice in one sentence.",
       geometry("line", legend="inside"))

# ============================================================ the bubble layer
figure(40, 1, "27", "photo-or-raster-image",
       caption("Graph 27: The diagram of the bubble layer"), "text-layer",
       cited(40, 40, ["Graph 27"], 1,
             "As Graph 27 shows, we modeled the bubble layer as a kind of porous medium",
             "as-shown-in"),
       S7,
       "Not a chart: a rendered 3-D view of a flat slab covered with a regular array of small oval "
       "bumps, shaded blue-grey on a dark navy ground - the paper's picture of the bubble layer as a "
       "porous medium lying on the water. No axes, no scale, no lettering, no dimension, no printed "
       "value. The layer's thickness and coefficient exist only in the symbols list printed beside "
       "it, so the picture cannot be measured and is not meant to be.",
       geometry("photo-or-raster-image", three_d="isometric"))

figure(41, 1, "28", "line",
       caption("Graph 28: Temperature curve of bubble model with different heat transfer coefficient "
               "bub"),
       "text-layer",
       cited(40, 41, ["Graph 28"], 1,
             "and get the total heat dissipation in natural cooling process as Graph 28 shows",
             lead_page=40),
       S7,
       "Three decay curves over 0 to 1000 min for the bubble layer's heat transfer coefficient, "
       "ordinate 300 to 318 K, in-plot legend entries 'l=0.5', 'l=0.7' and 'l=1'; the smaller the "
       "coefficient the slower the fall, which is the paper's closing claim that a bubble layer slows "
       "the heat loss. No markers, no printed value. The caption carries the symbol into the text as "
       "a Symbol-font letter, so 'bub' arrives as a subscript with no lamba-shaped glyph beside it in "
       "a plain extraction of the page.",
       geometry("line", legend="inside"))

# ============================================================ exclusion
EXCLUSIONS = [
    {"page": 24, "bbox": REG[(24, 1)], "reason": "not-an-exhibit",
     "note": "a display equation boxed as a region because its fraction bar and radical counted as "
             "drawn paths: the standard deviation 1/sqrt(sum((t_i - t_mean)^2)/n) with the sum and "
             "the radical set large. It is body mathematics, not an exhibit - no frame, no caption, "
             "no number, and the surrounding sentence defines it in words"},
]

RULES = [
    "Measure first, then read the pixels: thirty-five measured regions resolve into twenty-eight "
    "figure rows, six table rows and one exclusion, and no region is counted twice "
    "[place.page_order].",
    "The exhibit label is 'Graph N:', a form the numbering vocabulary does not name, so every figure "
    "row records numbering 'none' while printed_number keeps the number the caption prints "
    "[caption.numbering].",
    "A printed exhibit with no measured region is a declared gap, not a row: FIVE of the paper's "
    "ELEVEN numbered tables - Tables 1 and 2 on pp6-7, Table 5 on p26, Table 6 on p28 and Table 8 on "
    "p29 - print their caption, header and data and are covered by no region, because their grids are "
    "open rule sets that close no rectangle [place.doc_order].",
    "A display equation boxed as a region is not an exhibit: p24's standard-deviation formula is "
    "excluded as not-an-exhibit rather than counted as a one-line figure [place.area_frac].",
    "A caption carries the exhibit's number even when the in-plot title says the same thing: every "
    "figure row quotes the printed 'Graph N:' line and not the title the plotting program drew inside "
    "the frame, because the two disagree in spelling (Graph 13 is titled 'Water-Buthtub' above a "
    "caption reading 'Water-Bathtub') [caption.verbatim].",
    "A pointer that prints before its exhibit gives a negative lead: p15 introduces Graphs 3 and 4 "
    "one page before they print, and Graph 11 is named on p19 for p20, so those three rows carry "
    "lead_pages -1 and +1 respectively [mention.lead_pages].",
    "A bare pointer with no number cites nothing: 'this graph', 'the corresponding graph' and 'as "
    "shown in the following tables' never name a row, so Graphs 16 to 22 and Tables 1, 2, 5, 6 and 8 "
    "are counted as uncited rather than attributed by position [mention.count].",
    "Section placement follows the printed heading positions, and the heading index has dropped two "
    "of them: '4 Model for bathtub without a person in it (BWOP model)' and '5 Model for bathtub with "
    "a person in it (BWP model)' head their chapters but are not indexed, so the paths quote the "
    "printed lines [place.section_path].",
    "A figure printed above a heading belongs to the section that heading closes: Graph 2 sits at "
    "the top of p9 above '4.1 The calculation of the heat-transfer coefficient' and is therefore a "
    "chapter-4 preface, and Graph 11 sits above '5.2 Heat dissipation in BWP model' and is therefore "
    "part of 5.1 [place.section_path].",
]

NOTE = """\
Paper 94, Team 48649, the bathtub heat-loss paper. Forty-four pages, thirty-five measured regions
over twenty-five of them, and the thirty-five resolve into TWENTY-EIGHT FIGURE ROWS, SIX TABLE ROWS
and ONE EXCLUSION. Unaccounted zero, but the paper is not fully covered: it prints ELEVEN numbered
tables and only six of them were boxed as regions. Tables 1 and 2 (pp6-7), Table 5 (p26), Table 6
(p28) and Table 8 (p29) print caption, header and data with no measured region over any of them,
because their grids are open rule sets that close no rectangle, so they are recorded here as gaps.
The one excluded region is a display equation on p24 - the standard deviation 1/sqrt(sum((t_i -
t_mean)^2)/n) - boxed because its fraction bar and radical counted as drawn paths.

The numbering is the paper's own: every exhibit is a "Graph N:", twenty-eight of them, a form the
lane's vocabulary does not name, so the rows carry numbering "none" and keep the printed number
separately. All six tables print "Table N:". The captions sit below their art in twenty-seven of the
twenty-eight cases and above it for none; the exception is Graph 7, whose caption prints at the top of
p17 under art that ends level with it.

Citation is uneven. Twenty of the twenty-eight graphs are named by a sentence and eight are not:
Graphs 2, 16, 17, 18, 19, 20, 21 and 22. The six tables named are all named, but three of them first
appear in a single sentence on p30 - "By doing simulation we get the result shown in Table 9, Table 10
and Table 11" - so Tables 10 and 11 are introduced two and three pages before they print. Three
pointers run the other way: Graphs 3 and 4 are introduced on p15 for the p16 pair, and Graph 11 is
named on p19 for p20. The eight uncited graphs are exactly the sweep charts of section 6.1, where the
pointer degenerates into "the corresponding graph" with no label.

Two chapters are drawn twice as trees, Graphs 2 and 8, and both are genuine flowcharts of the model
hierarchy rather than data. The eight ANSYS exhibits (Graphs 1 and 3 to 11) are a single visual
idiom - grey solids and colour fields on a dark navy ground, with no axes anywhere - and only ONE of
them, the tetrahedral mesh of Graph 5, prints a scale bar (0.000 to 0.070 m); the other seven could be
any size. Their colour bars are printed in scientific notation, 3.12e+02 to 3.18e+02 and 3.13e+02 to
3.18e+02, with no unit on any of them, so the kelvin has to be inferred from the constants table two
chapters earlier.

The MATLAB curves are honest and unlabelled in the same breath: not one of the sixteen line rows
prints a data value on a mark, none carries a marker, and the series are identified by in-plot legends
whose entries are the model's own variable names ("Volume-average Temp", "Volume-maximum Temp",
"Volume-minimum Temp") rather than anything a reader would choose. Graphs 12, 13 and 14 are the
water-air, water-bathtub and total cooling curves, but Graph 13 is drawn over 0 to 3000 min while its
two siblings stop at 1000, so the "much slower" comparison the text draws from them cannot be read off
the pages. Graphs 23 to 26 repeat the same five-curve repeat-plot for surface area, tub volume, wall
material and bather volume, and the first of the four shows five lines inside a 2 pt band - the
finding is real and invisible at the same time.

Design defects that print: Graph 13's in-plot title misspells the path as "Water-Buthtub" above a
caption that spells it correctly; Graph 24's caption says "volume area", which is not a quantity;
Graph 26's pointer reads "the material of the bathtub have larger effect on the total heat loss than
the surface or the material of the bathtub", carried over from the material section and naming the
wrong variable twice in one sentence. Table 4's units disagree across one row - "Temp(k)",
"Temp(K)", "Temp(ºC)" - and its Celsius cell prints 40.4178 where the Kelvin value beside it is
313.1946, which converts to 40.04. Table 10 reports the same run as Table 9 with a different heat flux
(1.5652 W against 1.4406 W) while printing the identical three volume temperatures, and Table 11 does
agree with its siblings where the inputs coincide. Table 7 prints the CI comfortable degree as 10.0621
while the derivation on p27 gives 10.6021, and two of its four criteria are round assumptions - 1 and
10 - on which the whole FCE weighting rests.

Families: line 16, surface-or-3D 5, heatmap-or-contour 4, flowchart-or-schematic 2,
photo-or-raster-image 1, table-grid 6.
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

out = PROXY / "pc94-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUSIONS))
print("figures+table+excluded", len(ITEMS) + len(TABLES) + len(EXCLUSIONS))
