"""Hand census of P-A-2016-46830-92f43919 (Team 46830, 51 pages, 24 measured regions).

A hot-bath optimal-control paper. Twenty-four measured regions resolve into TWELVE FIGURE ROWS,
NINE TABLE ROWS and THREE EXCLUSIONS, unaccounted zero.

  p7  r1  Table 1        table-grid              symbol table, constants
  p8  r1  Table 2        table-grid              symbol table, variables with a Units column
  p8  r2  --             fragment-of-other       slice of the Figure 1 node-link chart
  p8  r3  --             fragment-of-other       second slice of the same chart
  p10 r1  Fig.2          flowchart-or-schematic  tub in a three-axis Cartesian frame
  p12 r1  Fig.3          flowchart-or-schematic  clip-art tub with the six heat arrows
  p15 r1  Fig.4          heatmap-or-contour      surface temperature field at 2.5 s
  p15 r2  Fig.5          heatmap-or-contour      surface temperature field at 100 s
  p17 r1  Fig.6          surface-or-3D           temperature distribution surface
  p17 r2  Fig.7          surface-or-3D           the fitted plane
  p20 r1  Fig.8          flowchart-or-schematic  forced-convection volume schematic
  p22 r1  Fig.9          line                    mixing ratio against forced convection
  p31 r1  Fig.10(b)      flowchart-or-schematic  Strategy 2 flow chart (right panel)
  p31 r2  Fig.10(a)      flowchart-or-schematic  Strategy 1 flow chart (left panel)
  p32 r1  Fig.11         line                    average water temperature over time
  p32 r2  Table 3        table-grid              average temperature data grid
  p36 r1  Fig.12         line                    three temperature curves
  p40 r1  Table 4        table-grid              tub shape/volume, water consumption
  p40 r2  Table 5        table-grid              tub shape/volume, water temperature
  p41 r1  Table 6        table-grid              human parameters, water consumption
  p41 r2  Table 7        table-grid              human parameters, water temperature
  p41 r3  Table 8        table-grid              heat transfer rate, water consumption
  p41 r4  Table 9        table-grid              heat transfer rate, water temperature
  p44 r1  --             duplicate               second printing of the Figure 3 clip-art

Figure 1 is a declared gap rather than a row: its caption prints on p9 ("Figure 1: The relationship
among the models and equations") but no art sits on p9, and the chart itself begins at the bottom of
p8, where the extractor boxed only two lettering slices (p8 r2, r3) instead of the whole diagram.

Section placement follows the printed heading positions. The extracted heading index drops the
numbering from several subsections ("1 The shape and volume of the tub" is printed 5.2.1) and misses
4.1.3 entirely, so the paths below quote the printed line where the index disagrees.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2016-46830-92f43919"
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


SEC_NOT = ["3 Notations"]
SEC_41 = ["4 The Model", "4.1 Normal Thermodynamic Model of Water Temperature"]
SEC_413 = ["4 The Model", "4.1 Normal Thermodynamic Model of Water Temperature",
           "4.1.3 Temperature field distribution of the water in the tub"]
SEC_421 = ["4.2 Forced convection model", "4.2.1 The introduction of forced convection source"]
SEC_422 = ["4.2 Forced convection model", "4.2.2 Effect of forced convection on the temperature"]
SEC_442 = ["4.4 Optimized control model of bathing strategy", "4.4.2 Strategy II"]
SEC_452 = ["4.5 Bubble bath", "4.5.2 Effect of bubble water on optimal control strategy"]
SEC_521 = ["5.2 Sensitivity Analysis", "5.2.1 Sensitivity to the shape and volume of the tub"]
SEC_522 = ["5.2 Sensitivity Analysis", "5.2.2 Sensitivity to the human parameters"]
SEC_523 = ["5.2 Sensitivity Analysis", "5.2.3 Sensitivity to the heat transfer rate"]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_PRINTED = schema.printed_lines(PID)
for _group in (SEC_NOT, SEC_41, SEC_413, SEC_421, SEC_422, SEC_442, SEC_452,
               SEC_521, SEC_522, SEC_523):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN and schema.norm(_label) not in _PRINTED:
            raise SystemExit(f"section label is neither an indexed heading nor a printed line: "
                             f"{_label!r}")

ITEMS: list[dict] = []
TABLES: list[dict] = []


def figure(page: int, reg: int, number: str, family: str, cap: dict, cap_src: str,
           mention: dict, section: list[str], note: str, geo: dict | None = None,
           section_kind: str = "other", other_note: str = "",
           confidence: str = "high") -> None:
    item = {
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
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


PANEL = dict(panels=2, layout="1x2")

# ============================================================ the two symbol tables
table(7, 1,
      caption("Table 1 Symbol Table–Constants", numbering="Table N", position="above"),
      "text-layer",
      cited(7, 7, ["Table1"], 1,
            "All the variables and constants used in this paper are listed in Table1 and Table 2."),
      SEC_NOT,
      "The constants table, printed above its own grid on p7: three columns (Symbol, Definition, "
      "Value) with one rule under the header and one at the foot, nine rows in all - the header "
      "plus eight constants (air temperature at 298K, saturated vapour pressure, water density, "
      "specific heat, thermal conductivity, both heat transfer coefficients and the latent heat). "
      "No vertical strokes, no shading, units carried inside the Value cells ('298K', '2.26 106 "
      "J/kg') rather than in a column of their own. The pointer on the same page spells the label "
      "'Table1' with no space, so the paper never prints 'Table 1' as two words.",
      rows=9, cols=3, numeric=1, text=2, rule="booktabs", header_rows=1,
      section_kind="symbols", note_sentence="")

table(8, 1,
      caption("Table 2 Symbol Table–Variables", numbering="Table N", position="above"),
      "text-layer",
      cited(7, 8, ["Table 2"], 1,
            "All the variables and constants used in this paper are listed in Table1 and Table 2."),
      SEC_NOT,
      "The variables table, the taller sibling of Table 1 and the only exhibit in the paper with a "
      "Units column: three columns and sixteen rows (header plus fifteen variables - Q, the average "
      "temperature, exchange, evaporation, body and radiation heat, T(x,y,z,t), the evaporation "
      "rate, flow, outlet temperature, the movement distance and volume of the k-th body position, "
      "the forced-convection source, the best flow and the best outlet temperature). Vertical "
      "strokes run between the columns so the grid is ruled rather than open, the units sit in the "
      "third column as superscripted powers ('m s-1', 'm3 s-1', 'm4'), and the two best-strategy "
      "symbols print with a prime (T0', Tb'). The pointer that names both tables is one sentence on "
      "p7, a page before this grid.",
      rows=16, cols=3, numeric=0, text=3, rule="vertical-rules", header_rows=1,
      units_in_header=True, section_kind="symbols", note_sentence="")

# ============================================================ coordinate frame and heat arrows
figure(10, 1, "2", "flowchart-or-schematic",
       caption("Figure 2: the three-dimensional Cartesian coordinate system of the tub"),
       "text-layer", uncited(), SEC_41,
       "The tub drawn as a wireframe box with the water surface shaded and a three-axis triad "
       "lettered X, Y and Z at the origin corner; the three edge lengths are lettered a, b and H, "
       "the symbols the model then carries through the whole paper. No graduation, no scale, no "
       "legend, no printed value: the picture fixes the frame and the letters, and the geometry "
       "itself lives in the equations. Its caption is printed under the art but no sentence anywhere "
       "names it - the paragraph below moves straight to the volume balance.",
       geometry("flowchart-or-schematic", three_d="isometric"))

figure(12, 1, "3", "flowchart-or-schematic",
       caption("Figure 3: The origin and destination of heat"), "text-layer", uncited(), SEC_41,
       "A clip-art bathtub, drawn as a coloured raster with a human figure in it, surrounded by six "
       "labelled arrows for the heat paths the model balances - the equivalent heat source, "
       "evaporation, the body, radiation and the in/out water terms behind 'Combining the six "
       "equations of heat exchange [15]'. The lettering is baked into the raster, so the labels are "
       "pixel art rather than text. THIS CAPTION IS PRINTED ON THE NEXT PAGE: the art sits at the "
       "foot of p12 and 'Figure 3: The origin and destination of heat' prints at the top of p13, "
       "which is why the caption is quoted from p13 and the row is placed on p12. The same clip-art "
       "is printed a second time on p44 with no caption at all (excluded there as a duplicate).",
       geometry("flowchart-or-schematic"))

# ============================================================ the solved temperature field
figure(15, 1, "4", "heatmap-or-contour",
       caption("Figure 4: Surface temperature field at 2.5s"), "text-layer", uncited(), SEC_413,
       "The surface temperature field the MATLAB PDE tool returns 2.5 s after the hot source is "
       "switched on: a false-colour field over the tub surface with a quiver of short arrows "
       "overlaid, the arrow direction being the heat-flow direction the sentence below the captions "
       "points at ('The arrow in the figure is the direction of heat transmission'). A colour bar "
       "at the right runs 40 to 45 deg C. No axis titles, no graduation, no legend, no printed "
       "value, and no panel letter - the caption alone says 2.5 s, and the time is the only thing "
       "distinguishing this from Figure 5.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

figure(15, 2, "5", "heatmap-or-contour",
       caption("Figure 5: Surface temperature field at 100s"), "text-layer", uncited(), SEC_413,
       "The same field at 100 s, drawn in exactly the same frame, colour map and quiver, with the "
       "colour bar again 40 to 45 deg C - so the pair is one of the few comparison pairs in the "
       "paper drawn on a COMMON scale, and the spread visible between them is a real spread. At "
       "2.5 s the heat hugs the tap corner; by 100 s it has diffused over most of the surface. No "
       "axis titles, no legend, no printed value.",
       geometry("heatmap-or-contour", legend="outside-right", colorbar=True))

figure(17, 1, "6", "surface-or-3D",
       caption("Figure 6: The distribution surface of temperature in space"), "text-layer", uncited(),
       SEC_413,
       "The same temperature field lifted into three dimensions as a surface mesh over the tub "
       "footprint, with a colour bar at the right spanning 40 to 45 deg C and the vertical axis "
       "running 38 to 46 deg C. This is the raw surface the paper then fits: the prose says 'we "
       "firstly fit the above surfaces by plane fitting' and the next exhibit is the fit. No axis "
       "titles, no legend, no printed value; the vertical axis reaches below the colour bar's floor, "
       "which is why the surface reads as flat over most of its span.",
       geometry("surface-or-3D", legend="outside-right", colorbar=True, three_d="surface-mesh"))

figure(17, 2, "7", "surface-or-3D",
       caption("Figure 7: The fitting plane"), "text-layer",
       cited(17, 17, ["Figure 7"], 1,
             "Thus we determine to use the fitting method and the fitting plane is shown in "
             "Figure 7.", "as-shown-in"),
       SEC_413,
       "The plane fitted to Figure 6, drawn as a wire mesh with the sample points marked as blue "
       "dots, and the only exhibit in the paper whose caption sentence also explains why it exists. "
       "All three axes are titled x, y and z, and there is NO colour bar: the fit is shown as a "
       "surface with markers rather than as a field, so the two exhibits of this pair are drawn in "
       "two different visual idioms and their vertical scales cannot be read against one another.",
       geometry("surface-or-3D", labels=True, three_d="surface-mesh"))

# ============================================================ forced convection
figure(20, 1, "8", "flowchart-or-schematic",
       caption("Figure 8: Forced convection cause by body"), "text-layer",
       cited(20, 20, ["Fig 8"], 1,
             "this process has caused the movement of water and water, to complete this action in "
             "the form of flow (Fig 8).", "parenthetical"),
       SEC_421,
       "A vector schematic of one swimmer's stroke: a body outline moving through the water with the "
       "displaced volume drawn as a shaded band and two lettered quantities in the figure, Vk (the "
       "volume) and Sk (the distance). The only pointer is parenthetical - '(Fig 8)', the paper's "
       "only use of the abbreviated form. The caption's 'cause by body' is printed as written. No "
       "axis, no scale, no legend, no printed value: the exhibit defines the two symbols "
       "F_k = V_k / S_k is built from, and the prose does the arithmetic.",
       geometry("flowchart-or-schematic"))

figure(22, 1, "9", "line",
       caption("Figure 9: The variation of convective mixing rate over the forced convection"),
       "text-layer", uncited(), SEC_422,
       "One smooth S-shaped curve, rising slowly from zero and saturating near one, plotted as the "
       "convective mixing ratio against the forced-convection strength - the shape that motivates "
       "the 'partial large state distribution function' the next equation gives, f(F) = 1 - "
       "exp(-(F - Fa)/Fb). Axis windows are cut tight to the sampled range, no legend, no markers, "
       "no printed value, no grid. The pointer above it is 'should be shown in the following "
       "figure', which names nothing, so no sentence in the paper prints 'Figure 9'.",
       geometry("line"))

# ============================================================ the two strategy flow charts
figure(31, 1, "10", "flowchart-or-schematic",
       caption("Figure 10: Algorithm flow charts"), "text-layer", uncited(), SEC_442,
       "The RIGHT panel of the pair, and the taller of the two: the Strategy 2 chart, lettered "
       "'Strategy2' at the top of its own column. It opens with 'Initialize variables', runs three "
       "decision loops - 'While Tb< the highest water temperature', 'While Tmin1<Ts' and "
       "'While Tmin2<Ts' - with Y/N branch markers at every diamond, and ends at 'Output The "
       "optimal result' and 'Finding the optimal temperature of adding water/draining'. The two "
       "panels are drawn side by side in one frame under one caption and neither carries a panel "
       "letter: only the printed 'Strategy1' and 'Strategy2' labels above each column tell them "
       "apart, and the left column is Strategy 1, so the reading order and the panel order are "
       "reversed here.",
       geometry("flowchart-or-schematic", **PANEL))

figure(31, 2, "10", "flowchart-or-schematic",
       caption("Figure 10: Algorithm flow charts"), "text-layer", uncited(), SEC_442,
       "The LEFT panel, lettered 'Strategy1', and the smaller of the two: one decision loop, "
       "'While sum<1800 (30 minutes)', with 'sum=sum+beta_t' on the return leg, one "
       "'Solve temperature increment (negative)beta_k' box, 'Tnext=Tk+beta_k' and the two outputs "
       "'Dispersed the water in interval within the range of 0 to 1800' and 'Output the average "
       "temperature(the water in the bathtub)-time relationship curve'. Fewer decisions than its "
       "right-hand sibling and one column narrower, both drawn in the same box-and-arrow idiom with "
       "Y/N markers. Same caption, same exhibit, no panel letter - the row keeps its own family and "
       "shares the exhibit's panel count of two.",
       geometry("flowchart-or-schematic", **PANEL))

# ============================================================ strategy II results
figure(32, 1, "11", "line",
       caption("Figure 11: The change curve of water average temperature"), "text-layer",
       cited(33, 32, ["Fig11"], 1, "Where, T (t ) is determined Fig11.", "direct", lead_page=33),
       SEC_442,
       "Two decaying curves over the bathing window: the red one is normal hot water under optimal "
       "strategy I and the blue one is plain cooling water, with a legend box INSIDE the plot "
       "lettered 'improved' and 'normal'. The abscissa is time in seconds and the ordinate the "
       "average water temperature in kelvin, but neither axis carries a title beyond the tick "
       "numbers. The pointer comes AFTER the exhibit: p33 closes a derivation with 'Where, T (t ) "
       "is determined Fig11.', so the first mention page is one past the exhibit page and the "
       "lead offset is negative. The paper prints 'Fig11' as one word, with no space and no period.",
       geometry("line", legend="inside"))

table(32, 2,
      caption("Table 3: Average temperature data", numbering="Table N:", position="above"),
      "text-layer", uncited(), SEC_442,
      "The numbers behind Figure 11, printed directly under it: seven columns (a corner cell "
      "reading 'T / t' split by a diagonal stroke, then six time points 300, 600, 900, 1200, 1500 "
      "and 1800 s) and three rows in all - the time header, the average temperature row and the "
      "second row the caption does not explain. One vertical stroke separates the corner label from "
      "the data, the rest of the grid is open. DATA DEFECT: the 900 s entry prints '3143814' with "
      "no decimal point where its neighbours give 316.0650, 315.1926, 313.6271, so the cell reads "
      "as three million instead of about 314.4 - the one arithmetic error a reader can catch by eye "
      "in the whole paper.",
      rows=3, cols=7, numeric=7, text=0, rule="vertical-rules", header_rows=2, diagonal=True,
      section_kind="result", note_sentence="")

# ============================================================ bubble bath
figure(36, 1, "12", "line",
       caption("Figure 12: Curves of temperature"), "text-layer",
       cited(36, 36, ["Figure 12"], 1,
             "As is shown in Figure 12, the green curve is the curve of the temperature change over "
             "time", "as-shown-in"),
       SEC_452,
       "Three curves in one frame comparing tap water against bubble water: green for the optimal "
       "strategy with bubble water, red for normal hot water under the same strategy, blue for "
       "natural cooling, with a legend INSIDE the plot lettered 'improved', 'normal' and 'bubble'. "
       "Time on the abscissa, temperature on the ordinate, no axis titles, no printed value, no "
       "markers. It is the paper's closing evidence that the bubble layer slows the heat loss, and "
       "the pointer sentence names all three curves in order, which is unusual for this paper.",
       geometry("line", legend="inside"))

# ============================================================ sensitivity tables
table(40, 1,
      caption("Table 4: Sensitivity of the shape and volume of the tub (for water consumption)",
              numbering="Table N:", position="above"),
      "text-layer", uncited(), SEC_521,
      "A five-row, eight-column response grid: a header row of perturbations (-5%, -3%, -1%, 0, "
      "1%, 3%, 5%) and four tub parameters down the left edge (a, b, H, h), each cell a signed "
      "percentage change in water consumption. Open grid, one rule under the header and one at the "
      "foot, right-aligned numbers, no shading. The pointer above it is 'as shown in the following "
      "tables' with no number, so no sentence names Table 4 or Table 5. The zero column is all 0% as "
      "it must be, and the -5% column is the largest response (-85.71% for the length a).",
      rows=5, cols=8, numeric=7, text=1, rule="booktabs", header_rows=1,
      section_kind="sensitivity", note_sentence="")

table(40, 2,
      caption("Table 5: Sensitivity of the shape and volume of the tub (for water temperature)",
              numbering="Table N:", position="above"),
      "text-layer", uncited(), SEC_521,
      "The sibling of Table 4 for outlet water temperature instead of water consumption: same five "
      "rows, same eight columns, same four tub parameters. Every cell is 0% or -0.03%, so the grid "
      "states in numbers what the sentence under it says in words - the temperature is almost "
      "insensitive to tub shape and volume while the consumption is very sensitive. The paper gives "
      "no precision beyond those two values, and the caption calls the quantity 'water temperature' "
      "while the body text calls it the outlet temperature.",
      rows=5, cols=8, numeric=7, text=1, rule="booktabs", header_rows=1,
      section_kind="sensitivity", note_sentence="")

table(41, 1,
      caption("Table 6: Sensitivity of the human parameters (for water consumption)",
              numbering="Table N:", position="above"),
      "text-layer", uncited(), SEC_522,
      "A two-row, eight-column grid: the same seven perturbations in the header and one body row "
      "labelled S for the body surface area, giving 28.57%, 14.29%, 0%, 0%, -42.86%, -57.14% and "
      "-71.43% in water consumption. Open rules, right-aligned values, no shading. The body "
      "sentence above calls them 'the following two tables', so the pair is named only by "
      "position. Note the asymmetry of the response around zero, which the text does not remark "
      "on: -5% costs 28.57% of the water and +5% saves 71.43% of it.",
      rows=2, cols=8, numeric=7, text=1, rule="booktabs", header_rows=1,
      section_kind="sensitivity", note_sentence="")

table(41, 2,
      caption("Table 7: Sensitivity of the human parameters (for water temperature)",
              numbering="Table N:", position="above"),
      "text-layer", uncited(), SEC_522,
      "The temperature half of the human-parameter pair: two rows, eight columns, the single body "
      "row S carrying 0% for the three negative perturbations and -0.03% for +1%, +3% and +5%. "
      "Open rules, right-aligned, no shading. Read with Table 6 it says the surface area moves the "
      "water bill by two thirds and the outlet temperature by three hundredths of a percent.",
      rows=2, cols=8, numeric=7, text=1, rule="booktabs", header_rows=1,
      section_kind="sensitivity", note_sentence="")

table(41, 3,
      caption("Table 8: Sensitivity of the heat transfer rate (for water consumption)",
              numbering="Table N:", position="above"),
      "text-layer", uncited(), SEC_523,
      "Two rows, eight columns, the body row labelled hwater (the heat transfer rate of the water, "
      "printed with a subscript): 28.57%, 14.29%, 14.29%, 0%, -42.86%, -57.14%, -71.43% in water "
      "consumption. Open rules, right-aligned, no shading. The -1% column reads 14.29% where the "
      "-3% column also reads 14.29%, so the response is flat between those two perturbations - a "
      "plateau the body text does not mention.",
      rows=2, cols=8, numeric=7, text=1, rule="booktabs", header_rows=1,
      section_kind="sensitivity", note_sentence="")

table(41, 4,
      caption("Table 9: Sensitivity of the heat transfer rate (for water temperature)",
              numbering="Table N:", position="above"),
      "text-layer", uncited(), SEC_523,
      "The last exhibit of the sensitivity block: two rows, eight columns, row label hwater, "
      "reading -0.03%, -0.03%, 0.03%, 0%, 0%, -0.03% and 0% for the seven perturbations. Open "
      "rules, right-aligned, no shading. DATA DEFECT: the -1% cell prints POSITIVE 0.03% while its "
      "neighbour on Table 5, for the same kind of response, prints -0.03% - the sign is dropped in a "
      "column where every other entry is negative or zero, and no sentence comments on it.",
      rows=2, cols=8, numeric=7, text=1, rule="booktabs", header_rows=1,
      section_kind="sensitivity", note_sentence="")

# ============================================================ exclusions
EXCLUSIONS = [
    {"page": 8, "bbox": REG[(8, 2)], "reason": "fragment-of-other",
     "note": "a lettering slice of the Figure 1 node-link chart - the extractor boxes the drawn text "
             "'Forced convection' on its own because the chart's arrows and nodes merge into one "
             "large path rather than separate regions; the chart continues onto p9, where its "
             "caption prints with no art beneath it, so the whole exhibit is a declared gap and this "
             "slice is not counted as a figure of its own"},
    {"page": 8, "bbox": REG[(8, 3)], "reason": "fragment-of-other",
     "note": "the second lettering slice of the same Figure 1 chart ('comfort model'), boxed for the "
             "same reason as the region above it; not a figure and not a table"},
    {"page": 44, "bbox": REG[(44, 1)], "reason": "duplicate",
     "note": "the Figure 3 clip-art printed a second time, on the explanation page, with no caption "
             "and no reference to it - the same bathtub raster with the same six heat arrows. The "
             "captioned printing on p12 is the row; this one adds nothing a reader cannot find "
             "there"},
]

RULES = [
    "Measure first, then read the pixels: twenty-four measured regions resolve into twelve figure "
    "rows, nine table rows and three exclusions, and no region is counted twice [place.page_order].",
    "A region boxed as drawn text inside a diagram is a fragment of that diagram, not a figure: two "
    "lettering slices of the Figure 1 node-link chart on p8 are excluded as fragment-of-other "
    "because the chart's own art is one merged path that the extractor never boxed as a region "
    "[place.area_frac].",
    "A printed exhibit with no measured region is a declared gap, not a row: Figure 1's caption "
    "prints on p9 with no art on that page and its chart begins at the foot of p8, so the paper's "
    "first figure is recorded in this note and in no item [place.doc_order].",
    "The same art printed twice is one exhibit: the p44 raster repeats the p12 clip-art with no "
    "caption and no pointer, so p12 is the row and p44 is excluded as a duplicate "
    "[place.section_path].",
    "A caption printed on the next page belongs to the art it describes: Figure 3's art sits at the "
    "foot of p12 and its caption at the top of p13, so the row is placed on p12 and the caption is "
    "quoted from p13 [caption.position].",
    "A side-by-side pair under one caption is one exhibit with two measured boxes: Figure 10's two "
    "flow charts are boxed separately, each becomes its own row, each keeps its own note, and both "
    "carry the exhibit's panel_count of two [geometry.panel_count].",
    "The reading order of a pair is the printed label, not the box order: Figure 10's left column is "
    "lettered 'Strategy1' and its right column 'Strategy2', so the row order and the panel order "
    "disagree and the notes say which panel is which [geometry.panel_layout].",
    "Section placement follows the printed heading positions, and where the heading index has "
    "dropped the subsection numbering or missed a heading altogether the path quotes the printed "
    "line: 5.2.1 to 5.2.3 are indexed as bare list lines and 4.1.3 is not indexed at all, yet all "
    "four print on the page [place.section_path].",
    "A pointer that follows its exhibit gives a negative lead: p33 says 'Where, T (t ) is determined "
    "Fig11.' about the figure printed on p32, so the first mention page is one past the exhibit page "
    "[mention.lead_pages].",
]

NOTE = """\
Paper 93, Team 46830, the hot-bath optimal-control paper. Fifty-one pages, twenty-four measured
regions over fourteen of them, and the twenty-four resolve into TWELVE FIGURE ROWS, NINE TABLE ROWS
and THREE EXCLUSIONS. Unaccounted zero. Nine of the twelve figures and every one of the nine tables
are printed with a caption; four of the twelve figures and one table are named by a sentence.

Figure 1 is a declared gap rather than a row. Its caption prints at the top of p9 ("Figure 1: The
relationship among the models and equations") with no art anywhere on that page, and the chart itself
starts at the foot of p8, where the extractor boxed only two lettering slices ("Forced convection",
"comfort model") because the diagram's arrows and nodes merge into a single large path. The two
slices are excluded as fragment-of-other; the chart as a whole is recorded here and nowhere else.

Citation is thin. Four of the twelve figure captions are carried into a sentence and eight are named
by nothing: the pointers that do exist are "the fitting plane is shown in Figure 7", "to complete this
action in the form of flow (Fig 8)" - the paper's only abbreviated form - and "As is shown in
Figure 12". Figure 11 is the one exhibit named AFTER it is printed: p33 closes a derivation with
"Where, T (t ) is determined Fig11.", which prints the label as a single word with no space and no
period. Figures 2, 3, 4, 5, 6, 9 and 10 are named by no sentence, their introductions reading "here
are the results", "the following figure" and nothing at all.

Two placement facts drive the rows. Figure 3's caption prints on the page AFTER its art, so the row
is p12 and the caption is quoted from p13. Figure 10 is a side-by-side pair in one frame with no panel
letters: the left column is lettered "Strategy1" and carries one decision loop, "While sum<1800 (30
minutes)", while the right column is lettered "Strategy2" and carries three, "While Tb< the highest
water temperature", "While Tmin1<Ts" and "While Tmin2<Ts", ending at "Finding the optimal temperature
of adding water/draining". The row order therefore runs right-to-left against the reading order, and
each row keeps its own note.

The tables carry the paper's arithmetic and two of its slips. Table 3 gives the data behind Figure 11
in a grid whose corner cell is split by a diagonal stroke reading "T / t", and its 900 s entry prints
"3143814" with the decimal point missing, so the cell reads as three million instead of about 314.4.
Table 9 prints POSITIVE 0.03% in a column where its sibling Table 5 prints -0.03%, the sign dropped
in a column that is otherwise negative or zero. Otherwise the sensitivity pairs are internally
consistent and the zero column of every grid is 0%: the tub's shape and volume moves water
consumption by up to -85.71% while moving outlet temperature by 0.03%, and the body surface area
moves consumption by -71.43% at +5% while moving temperature by -0.03%, which is the paper's whole
argument in two numbers.

Families: line 3, heatmap-or-contour 2, surface-or-3D 2, flowchart-or-schematic 5, table-grid 9. The
three excluded regions are the two lettering slices of the Figure 1 chart and the second printing of
the Figure 3 clip-art on p44.
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

out = PROXY / "pc93-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUSIONS))
print("figures+table+excluded", len(ITEMS) + len(TABLES) + len(EXCLUSIONS))
