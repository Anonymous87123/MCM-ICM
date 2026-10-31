"""Hand census of P-A-2016-54164-57a2b533 (Team 54164, 44 pages, 35 measured regions).

A bathtub heat-loss paper whose exhibits are almost all uncaptioned. Thirty-five measured regions
resolve into THIRTY-FIVE FIGURE ROWS, NO TABLE ROW and NO EXCLUSION: the paper prints no table at
all, and every boxed region is an exhibit.

  p6  r1  Figure 1   flowchart-or-schematic  hands swirling the bath water
  p9  r1  --         line                    three beaker cooling series
  p10 r1  --         line                    the same data with three exponential fits
  p11 r1  --         line                    own bathtub experiment, raw series
  p11 r2  --         line                    own bathtub experiment, shifted series with fit
  p12 r1  --         scatter                 k against V^2/SA^3
  p13 r1  --         scatter                 k against (V^2/SA^3)^2
  p13 r2  --         scatter                 k against sqrt(V^2/SA^3)
  p14 r1  --         scatter                 k against cbrt(V^2/SA^3)
  p16 r1  --         line                    deviance against flow rate, standard tub
  p17 r1  --         scatter                 simulated temperature at 1.81 GPM
  p18 r1  --         line                    simulation against experiment
  p19 r1  --         surface-or-3D           Inventor render, standard tub
  p20 r1  --         line                    deviance against flow rate, standard tub AGAIN
  p21 r1  --         surface-or-3D           Inventor render, circular tub
  p22 r1  --         line                    deviance, circular tub
  p23 r1  --         surface-or-3D           Inventor render, triangular tub
  p24 r1  --         line                    deviance, triangular tub
  p25 r1  --         surface-or-3D           Inventor render, square tub
  p26 r1  --         line                    deviance, square tub
  p27 r1  --         surface-or-3D           Inventor render, hemispherical tub
  p28 r1  --         line                    deviance, hemispherical tub
  p29 r1  --         surface-or-3D           Inventor render, oval tub
  p30 r1  --         line                    deviance, oval tub
  p31 r1  --         surface-or-3D           Inventor render, quarter-circle tub
  p32 r1  --         line                    deviance, quarter-circle tub
  p33 r1  --         surface-or-3D           Inventor render, trapezoidal tub
  p34 r1  --         line                    deviance, trapezoidal tub
  p35 r1  --         scatter                 optimal flow rate against surface area
  p36 r1  --         scatter                 optimal flow rate against volume
  p37 r1  --         line                    deviance, fiberglass tub
  p38 r1  --         line                    deviance, tub with bubble bath
  p39 r1  Figure 2   photo-or-raster-image    dimensioned part drawing
  p40 r1  Figure 3   photo-or-raster-image    the product on its own
  p40 r2  Figure 4   photo-or-raster-image    the product lying in a bathtub

THE PAPER IS A ONE-CAPTION-FOR-EVERY-EIGHT-FIGURES PAPER. Thirty-five exhibits print and only four
carry a caption and a number (Figures 1 to 4), and three of those four are the closing product
pictures. Twenty-one of the thirty-one uncaptioned exhibits are screenshots of plots pasted straight
out of Excel and MATLAB, each keeping the plotting program's own in-plot title; that title is the only
thing on the page that says what the exhibit is, and for the eight Inventor renders there is no title
at all.

THE SENSITIVITY CHAPTER IS A TEMPLATE RUN EIGHT TIMES. Section 5.1 and 5.2 replace the standard tub
with seven other shapes, and each design gets exactly two exhibits: an unlabelled Inventor render on
one page and a deviance-against-flow-rate chart on the next, whose title is the only thing that
identifies the design. Every one of those eight charts is the same plot template - same abscissa
(Flow Rate (GPM), 1.0 to 16.0), same unitless ordinate (Deviance), same unframed outside-left legend
with entries "Bathtub" and "Minimum" - and in every one of them the "Minimum" entry is never drawn:
the point the text says the reader should read off the chart ("the point indicated at the bottom of
the graph") has no marker anywhere in the axes.

The standard tub's chart is printed TWICE in the same paper, once on p16 as the flow-rate selection
of section 4.3.1 and again on p20 as the first case of section 5.1, with the same title
"Optimal Flow Rate (SA: 1800, V: 25200)".
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2016-54164-57a2b533"
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


def no_caption() -> dict:
    """The block for an exhibit that prints no caption at all: twenty-one of this paper's rows."""
    return {"verbatim": "", "numbering": "none", "words": 0, "sentences": 0, "units": False,
            "variables": False, "variable_count": 0, "conditions": False, "concludes": False,
            "voice": "none", "position": "below"}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


S3 = ["3 The Strategy", "3.1 Distribution: A Simple Solution"]
S422 = ["4 Simulating Heat Transfer", "4.2 Creation of the Model", "4.2.2 Experimental Data"]
S431 = ["4 Simulating Heat Transfer", "4.3 Simulation Design",
        "4.3.1 Selecting Optimal Flow Rate"]
S432 = ["4 Simulating Heat Transfer", "4.3 Simulation Design", "4.3.2 Validation of Model"]
S51 = ["5 Sensitivity Analysis: Varying Bathtub Characteristics",
       "5.1 Varying Surface Area Under Constant Volume"]
S52 = ["5 Sensitivity Analysis: Varying Bathtub Characteristics",
       "5.2 Varying Volume Under Constant Surface Area"]
S53 = ["5 Sensitivity Analysis: Varying Bathtub Characteristics", "5.3 Observations"]
S54 = ["5 Sensitivity Analysis: Varying Bathtub Characteristics", "5.4 Material of Bathtub"]
S55 = ["5 Sensitivity Analysis: Varying Bathtub Characteristics",
       "5.5 Additives (bubble bath)"]
S64 = ["6 Conclusion", "6.4 Future Work/Discussion"]
S65 = ["6 Conclusion", "6.5 Home Jacuzzi"]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_PRINTED = schema.printed_lines(PID)
for _group in (S3, S422, S431, S432, S51, S52, S53, S54, S55, S64, S65):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN and schema.norm(_label) not in _PRINTED:
            raise SystemExit(f"section label is neither an indexed heading nor a printed line: "
                             f"{_label!r}")

# The four printed captions, quoted from the text layer.
CAP1 = caption("Figure 1: Proposed strategy for equalizing the temperature of the water in any "
               "single-faucet bathtub.")
CAP2 = caption("Figure 2: A blueprint of the dimensions for our product.")
CAP3 = caption("Figure 3: The product.")
CAP4 = caption("Figure 4: Our product in use with a standard bathtub.")

ITEMS: list[dict] = []


def figure(page: int, reg: int, family: str, cap: dict, cap_src: str, mention: dict,
           section: list[str], note: str, geo: dict | None = None, number: str = "",
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


# ======================================================== the strategy cartoon
figure(6, 1, "flowchart-or-schematic", CAP1, "text-layer",
       cited(1, 6, ["Figure 1"], 1,
             "we suggest that the user swirl his hands counter-clockwise with respect to the faucet "
             "as shown in Figure 1", "as-shown-in"),
       S3,
       "A cross-section cartoon rather than a plot: a black outline bathtub seen from the side with "
       "the faucet at the upper right, a stick figure standing in it whose arm is drawn as two "
       "straight lines reaching into the water, and two thick red circular arrows showing the "
       "counter-clockwise swirl the text asks for. The water is filled with a red-to-blue gradient "
       "that runs from the faucet side to the far side - the temperature gradient the swirl is meant "
       "to remove - although nothing on the drawing states this and no scale, axis or legend exists. "
       "It is the only exhibit in the paper that is a drawing of an action rather than a plot of a "
       "measurement, and the only one whose caption prints below it as a numbered figure in the body "
       "chapters.",
       geometry("flowchart-or-schematic"), "1", "solution")

# ======================================================== the beaker regressions
figure(9, 1, "line", no_caption(), "none", uncited(), S422,
       "Three cooling series measured in 100 mL, 300 mL and 800 mL beakers, drawn as marker-plus-line "
       "curves over 0 to 62 min, ordinate 20 to 100 degrees Celsius, title 'Water Beaker Cooling', "
       "legend at the top right INSIDE the axes with entries '100mL', '300mL Beaker' and "
       "'800mL Beaker'. The three markers differ (open circle, triangle, cross) but the legend's "
       "first entry drops the word 'Beaker' that the other two keep, and no caption, number or "
       "pointer in the body text identifies the exhibit - the surrounding sentence only says 'We "
       "created a graph to represent the data'.",
       geometry("line", legend="inside"))

figure(10, 1, "line", no_caption(), "none", uncited(), S422,
       "The same three beaker series re-plotted from a spreadsheet as thick marker lines with three "
       "thin dotted fit curves overlaid, title 'Water Beaker Temperature vs. Time Regression', "
       "ordinate 0 to 90 degrees Celsius, legend OUTSIDE the frame on the right with six entries: the "
       "three data series and 'Expon. (800mL)', 'Expon. (300mL)', 'Expon. (100mL)'. Three fit labels "
       "print inside the plot at the right, each reading 'Y = 77e^-0.029x', 'Y = 77e^-0.052x' and "
       "'Y = 77e^-0.036x' with R squared 0.9694, 0.9092 and 0.8528. THE PRINTED FIT EQUATIONS ARE NOT "
       "THE PAPER'S EQUATIONS: (8), (9) and (10) on the next page all read y = 77e^-knx + 23, and the "
       "asymptote constant 23 is missing from all three labels here, so the plot's own labels imply "
       "the water cools towards 0 degrees and not towards the 23 degree room.",
       geometry("line", legend="outside-right", numbers=True))

figure(11, 1, "line", no_caption(), "none", uncited(), S422,
       "The team's own bathtub experiment: a single marker line falling from 37.0 to 33.2 degrees "
       "Celsius over 0 to 62 min, title 'Temperature vs. Time for Real-World Bathtub Experiment', "
       "ordinate 33 to 37.5 degrees Celsius, one-entry legend 'temp' outside the frame at the right. "
       "This is the only absolute-temperature curve of the paper's own data and the only one where "
       "the y-axis span is small enough to show the measurement wobble - the series steps down in "
       "flat runs of three or four points between readings.",
       geometry("line", legend="outside-right"))

figure(11, 2, "line", no_caption(), "none", uncited(), S422,
       "The same experiment re-plotted after the 21 degree offset: the series now runs from 16.05 to "
       "12.4 over the same 0 to 62 min, with a dotted exponential fit labelled "
       "'Y = 16.00000e^-0.00448x / R squared 0.97326' and a two-entry legend ('temp', "
       "'Expon. (temp)') outside the frame. THE AXIS STILL SAYS TEMPERATURE IN DEGREES CELSIUS AND "
       "THE TITLE IS WORD FOR WORD THE ONE ABOVE: the shifted quantity T minus 21 is plotted against "
       "a temperature axis, so the exhibit shows 37 degree bath water sitting at 16 degrees and "
       "nothing on the page says the 21 degrees were subtracted. The offset itself disagrees with "
       "the beakers' 23 degrees, and equation (24) on p18 restores it as +21 while the beaker "
       "constants are +23 with no explanation of the difference.",
       geometry("line", legend="outside-right", numbers=True))

# ======================================================== four k regressions
figure(12, 1, "scatter", no_caption(), "none", uncited(), S422,
       "Four open circles and a fitted power curve, title 'K-value Regression', ordinate K from 0.00 "
       "to 0.04, abscissa 'V^2/SA^3' from 0 to 140000, and the label 'R squared: 0.99764' printed "
       "inside the frame at the top right. No legend, no gridline, no unit on K. The four points are "
       "the team's bathtub experiment plus the three beakers, and the whole of section 4.2.2's model "
       "selection rests on them - which is why the next three pages print the same four points three "
       "more times against three other transforms of the same predictor.",
       geometry("scatter", numbers=True))

figure(13, 1, "scatter", no_caption(), "none", uncited(), S422,
       "The same four points and the same fit against the SQUARED predictor: abscissa "
       "'(V^2/SA^3)^2' with ticks in scientific notation 0.0e+00 to 1.5e+10, ordinate K 0.00 to 0.04, "
       "title 'K-value Regression' again, label 'R squared: 0.996529' inside the frame. Nothing in "
       "the drawing distinguishes it from the exhibit one page earlier except the abscissa ticks: the "
       "points sit in the same order, the curve has the same shape, and the two pages are otherwise "
       "identical screenshots.",
       geometry("scatter", numbers=True))

figure(13, 2, "scatter", no_caption(), "none", uncited(), S422,
       "The third copy: the same four points against 'square root of (V^2/SA^3)', ticks 50 to 350, "
       "ordinate K 0.00 to 0.04, title 'K-value Regression', 'R squared: 0.999294' inside the frame. "
       "The text between the two exhibits says 'Seeing as this is worse, we test ...' and then "
       "'Noticing improvement, we test ...', so the reader is asked to compare three regressions "
       "whose only difference is a tick-label string.",
       geometry("scatter", numbers=True))

figure(14, 1, "scatter", no_caption(), "none", uncited(), S422,
       "The fourth and last: the same four points against 'cubic root of V^2/SA^3', ticks 20 to 50, "
       "ordinate K 0.00 to 0.04, title 'K-value Regression', 'R squared: 0.999299' inside the frame. "
       "This one is the model the paper adopts, and its regression is reported in the body as "
       "'R2 = 0.99929854436231100000' - twenty significant digits for four data points, and one more "
       "digit than the 0.999299 the same page's exhibit prints.",
       geometry("scatter", numbers=True))

# ======================================================== flow-rate selection
figure(16, 1, "line", no_caption(), "none", uncited(), S431,
       "Deviance against flow rate for the standard tub: one red curve on a unitless ordinate "
       "(Deviance, 200 to 1800) against 'Flow Rate (GPM)' 1.0 to 16.0, title 'Optimal Flow Rate "
       "(SA: 1800, V: 25200)', and an unframed legend OUTSIDE-LEFT with two entries, 'Bathtub' and "
       "'Minimum'. THE MINIMUM THE LEGEND PROMISES IS NOT VISIBLE: the text tells the reader the "
       "answer is 'represented by the point indicated at the bottom of the graph, at (1.81, "
       "10.179381314125882)', but no marker, crosshair or label appears at that point or anywhere "
       "else in the axes, and the appendix's own code shows why - it adds the 'Minimum' entry as a "
       "single point carrying its value, and that point sits at the curve's floor, at or below the "
       "frame's lowest tick, so the one number the method minimizes is the one the chart cannot "
       "place. The ordinate has no zero tick either.",
       geometry("line", legend="outside-left"))

figure(17, 1, "scatter", no_caption(), "none", uncited(), S431,
       "The simulated bath at the chosen flow rate: open circles falling from 37.5 to 35.6 degrees "
       "Celsius, ordinate 'Temperature (degrees Celsius)' 36.0 to 37.5 with the frame extending below "
       "the lowest tick, abscissa 'Time (minutes)' 0 to 40, title "
       "'Temperature vs. Time @ Optimal Flow Rate 1.81GPM'. No legend, no marker on the point where "
       "the faucet turns on. The claim it illustrates - that the curve stops falling and turns back "
       "up once 1.4 degrees have been lost - is not visible: the series is a nearly straight decay "
       "with no turn, and the title's '@' and the run-together '1.81GPM' are the only text on it.",
       geometry("scatter"))

figure(18, 1, "line", no_caption(), "none", uncited(), S432,
       "Simulation against experiment: open circles with a straight fit line over 0 to 40 min, "
       "ordinate 34.5 to 37.0 degrees Celsius, title 'Validation of Experiment', and "
       "'R squared: 0.999836.' printed inside the frame - the trailing full stop is part of the "
       "label. No legend and no key to say which mark is the simulation and which the experiment, "
       "which matters because the section's claim is that the two cannot be told apart.",
       geometry("line", numbers=True))

# ======================================================== 5.1: eight designs
def render(page: int, reg: int, what: str, section: list[str], kind: str = "sensitivity") -> None:
    figure(page, reg, "surface-or-3D", no_caption(), "none", uncited(), section,
           f"An Autodesk Inventor render of {what}, printed alone on its page: grey shaded surfaces "
           f"with soft shadows and no annotation of any kind - no dimension line, no axis, no scale "
           f"bar, no label, not even the design's name, which appears only in the prose of the "
           f"following page. The drawing is the only place the shape of this design exists, and "
           f"nothing on it can be measured or matched to the surface area and volume the text quotes "
           f"beside it.",
           geometry("surface-or-3D", three_d="isometric"), section_kind=kind)


def deviance(page: int, reg: int, title: str, ticks: str, section: list[str], note_extra: str,
             kind: str = "sensitivity") -> None:
    figure(page, reg, "line", no_caption(), "none", uncited(), section,
           f"Deviance against flow rate, title '{title}', abscissa 'Flow Rate (GPM)' 1.0 to 16.0, "
           f"unitless ordinate 'Deviance' with ticks {ticks}, unframed outside-left legend 'Bathtub' "
           f"and 'Minimum'. Same template as the standard tub's chart: no 'Minimum' point is visible "
           f"in the axes, the ordinate carries no unit and no zero, and the design is identified "
           f"only by the numbers in the title. {note_extra}",
           geometry("line", legend="outside-left"), section_kind=kind)


render(19, 1, "the standard 60 by 30 by 14 inch tub", S51)
deviance(20, 1, "Optimal Flow Rate (SA: 1800, V: 25200)", "200.0 to 1800.0", S51,
         "THIS PLOT IS THE P16 PLOT PRINTED A SECOND TIME - identical title, identical axis ranges, "
         "identical curve - so the paper's first sensitivity case is the same exhibit as its "
         "flow-rate selection, and the reader who has already read p16 learns nothing new from it.")
render(21, 1, "the circular tub, radius 23.14 in by 15 in high", S51)
deviance(22, 1, "Optimal Flow Rate (SA: 1680, V: 25200)", "100.0 to 1100.0", S51,
         "The circular tub is the one design whose deviance floor is visible - the curve bottoms out "
         "well above the frame's lower edge, unlike the standard tub's.")
render(23, 1, "the triangular tub, 57.02 by 57.02 by 80.64 in by 15.5 in high", S51)
deviance(24, 1, "Optimal Flow Rate (SA: 1625, V: 25200)", "100.0 to 500.0", S51,
         "The curve starts below the lowest printed tick, so the minimum it is supposed to show sits "
         "off the labelled scale.")
render(25, 1, "the square tub, 39.69 in square by 16 in high", S51)
deviance(26, 1, "Optimal Flow Rate (SA: 1575, V: 25200)", "2.0 to 32.0", S51,
         "This is the design that produces the paper's best flow rate, 4.7 gallons per minute, and "
         "its ordinate shows why: the scale is 2.0 to 32.0, an order of magnitude below every other "
         "chart of the set, so the same curve that bottoms out near 100 on the standard tub's frame "
         "reaches 1.20 degrees squared here. The frame is then subdivided by sixteen tick labels to "
         "resolve it.")

# ======================================================== 5.2: four more designs
render(27, 1, "the hemispherical tub, radius 22.57 in - seen from above as a plain circular basin",
       S52)
deviance(28, 1, "Optimal Flow Rate (SA: 1600, V: 24079)", "100.0 to 900.0", S52,
         "The curve again begins below the lowest printed tick.")
render(29, 1, "the oval tub, a 50 by 23.4 in rectangle with an 11.7 in arc radius by 15 in high", S52)
deviance(30, 1, "Optimal Flow Rate (SA: 1600, V: 24000)", "100.0 to 900.0", S52,
         "The curve runs above the top printed tick.")
render(31, 1, "the quarter-circle tub, radius 45.14 in by 14 in high", S52)
deviance(32, 1, "Optimal Flow Rate (SA: 1600, V: 22400)", "200.0 to 1600.0", S52,
         "Near-duplicate of the oval tub's chart with only the title numbers and the ordinate range "
         "changed.")
render(33, 1, "the trapezoidal tub, 50 by 32 in at the top and 36 by 24 in at the bottom by 15 in",
       S52)
deviance(34, 1, "Optimal Flow Rate (SA: 1600, V: 18200)", "200.0 to 2400.0", S52,
         "The largest ordinate of the eight, and the curve still overshoots it.")

# ======================================================== 5.3 observations
figure(35, 1, "scatter", no_caption(), "none", uncited(), S53,
       "The seven designs collapsed into one picture: three open circles of optimal flow rate "
       "against surface area, title 'Constant Volume', abscissa 'Surface Area (sq.in)' 1600 to 1800, "
       "ordinate 'Optimal Flow Rate (GPM)' 1.5 to 4.5. No legend, no labels on the points, no line. "
       "Three points cannot support the section's claim that the flow rate 'decreases, but then "
       "increases again, following no set pattern', and two of the seven designs are missing from "
       "the plot entirely - the standard tub at 1800 sq.in and the fiberglass and bubble-bath runs "
       "are the only ones near this abscissa range.",
       geometry("scatter"))

figure(36, 1, "scatter", no_caption(), "none", uncited(), S53,
       "The volume sweep: four open circles of optimal flow rate against volume, title 'Constant "
       "Surface Area', abscissa 'Volume (cubic in)' 18000 to 24000, ordinate 1.4 to 2.0, with one "
       "marker sitting above the highest labelled tick. No legend, no point labels. Like its twin "
       "above it, the exhibit is titled with the quantity that is held fixed rather than the one "
       "that varies, so the two plots are named for their constants and the reader has to read the "
       "abscissa to learn which is which.",
       geometry("scatter"))

# ======================================================== 5.4 and 5.5
figure(37, 1, "line", no_caption(), "none", uncited(), S54,
       "The fiberglass run: deviance against flow rate, title 'Optimal Flow Rate (SA: 2340, "
       "V: 25200)', ordinate 1000.0 to 4000.0, outside-left legend 'Bathtub' and 'Minimum'. The "
       "ordinate is an order of magnitude above every other chart's, which is the point - the tub "
       "loses heat fast enough that its best flow rate is 7.52 gallons per minute - but the "
       "'Minimum' entry is again undrawn, and the title's surface area, 2340 sq.in, is not the 6120 "
       "sq.in the text derives one page earlier for the same run.",
       geometry("line", legend="outside-left"), "sensitivity")

figure(38, 1, "line", no_caption(), "none", uncited(), S55,
       "The bubble-bath run: deviance against flow rate, title 'Optimal Flow Rate (SA: 1710, "
       "V: 25200)', ordinate 100.0 to 1400.0, outside-left legend 'Bathtub' and 'Minimum'. The "
       "title's 1710 sq.in is the arithmetic of the section - 1800 square inches of water surface "
       "multiplied by the assumed 0.95 insulation factor - so this is the one deviance chart whose "
       "title can be checked against the text and agrees with it. Two of the frame's gridlines are "
       "drawn heavier than the rest.",
       geometry("line", legend="outside-left"), "sensitivity")

# ======================================================== the product
figure(39, 1, "photo-or-raster-image", CAP2, "text-layer", uncited(), S65,
       "A dimensioned engineering drawing pasted in as a low-resolution screenshot inside a grey "
       "gradient background: two views of the same U-shaped part side by side, the left a plan of the "
       "bend with the dimension callouts R4.00, R12.00, R7.50, R8.00, 45.00 and 3.00, the right the "
       "same part turned 90 degrees with 20.00, 25.00, 23.10, 2.90, R1.50, 1.50, 4.00, 3.00 and "
       "R1.00. Border zone marks '1', '2', 'A', 'B' and a faxed 'AUTODESK' title-block mark frame it. "
       "This is the paper's only dimensioned exhibit and almost the only place a unit appears on any "
       "exhibit - though the drawing prints bare numbers with no inch marks, and the smallest "
       "callouts are illegible at the printed size.",
       geometry("photo-or-raster-image"))

figure(40, 1, "photo-or-raster-image", CAP3, "text-layer", uncited(), S65,
       "The product on its own: a blue translucent U-shaped tube whose two straight arms carry a row "
       "of round holes, with a short open nozzle rising from the bend, rendered on a plain white "
       "background. No dimension, no label, no scale - the drawing above it is the only source for "
       "its size, and the two are not drawn to a common scale.",
       geometry("photo-or-raster-image"))

figure(40, 2, "photo-or-raster-image", CAP4, "text-layer", uncited(), S65,
       "The product in use: the same blue slotted U-tube lying inside a black open-top rectangular "
       "tub with the nozzle standing up at one end. This is the only exhibit in the paper that shows "
       "an exhibit in the situation it is meant for, and it is a rendering rather than a photograph: "
       "no water, no person, no faucet connection, and no indication of how the tube's own holes "
       "relate to the water level.",
       geometry("photo-or-raster-image"))

RULES = [
    "Measure first, then read the pixels: thirty-five measured regions resolve into thirty-five "
    "figure rows, no table row and no exclusion, and no region is counted twice "
    "[place.page_order].",
    "Thirty-one of the thirty-five exhibits print NO caption and NO number: only Figures 1 to 4 are "
    "captioned, so every other row records caption_source 'none' and numbering 'none' while the four "
    "captioned rows take the printed 'Figure N:' form [caption.numbering].",
    "The plotting program's own title is not a caption: an uncaptioned chart keeps whatever title "
    "Excel or MATLAB drew inside the frame ('Optimal Flow Rate (SA: 1800, V: 25200)'), that title is "
    "recorded in the note and in the geometry, and no caption block is invented from it "
    "[caption.verbatim].",
    "A bare pointer is not a citation: the paper says 'We created a graph', 'Comparing the deviance "
    "of every flow rate produces the following' and 'The following constructions were rendered using "
    "Autodesk Inventor', and none of those names a figure, so thirty-four rows are uncited and only "
    "Figure 1 is named (on the abstract page, five pages before it prints) [mention.count].",
    "An exhibit printed alone on a page with no text is placed by the section that precedes it: the "
    "eight Inventor renders sit on textless pages and belong to the design whose dimensions the "
    "following page states, which is the page order 5.1 and 5.2 run through "
    "[mention.lead_pages].",
    "Two regions hold the same plot: p16 and p20 print the standard tub's deviance chart twice, with "
    "the same title and the same axes, and both are recorded as rows because both are printed "
    "exhibits [place.doc_order].",
    "A figure block with no caption, no axis and no label is still an exhibit when the paper prints "
    "it as one: the eight Inventor renders are rows, not exclusions, because each occupies its whole "
    "page and is referred to by the surrounding prose as a design [place.area_frac].",
    "Section placement follows the heading index, which indexed every heading this paper prints; the "
    "paths quote the labels the index gives [place.section_path].",
]

NOTE = """\
Paper 95, Team 54164, the bathtub heat-loss paper with a home-made diffuser at the end. Forty-four
pages, thirty-five measured regions on thirty-two of them, resolving into THIRTY-FIVE FIGURE ROWS,
NO TABLE ROW and NO EXCLUSION. Unaccounted zero. The paper prints no table at all: not a constants
table, not a symbol table, not a results table, and every one of the thirty-five exhibits is a plot,
a render or a product picture.

The overwhelming fact about this paper's exhibits is that thirty-one of the thirty-five carry no
caption and no number. The four that do are Figures 1 to 4, and three of those are the closing
product pictures; the only captioned exhibit in the body chapters is Figure 1, a cartoon. Everything
else - twenty-one spreadsheet and MATLAB screenshots and eight Inventor renders - is dropped into the
page with whatever title the plotting tool drew inside its own frame, or with nothing at all. The
renders have no label of any kind, so the only thing that identifies a design is the dimension
paragraph that follows its page.

Citation is even thinner than captioning. Only Figure 1 is ever named by a sentence, and that
sentence is on the abstract page, five pages before the exhibit prints: "we suggest that the user
swirl his hands counter-clockwise with respect to the faucet as shown in Figure 1". Figures 2, 3 and
4 are never named at all, and the other thirty-one exhibits are pointed at, when they are pointed at,
by bare phrases that name no figure: "We created a graph to represent the data", "The results of our
experiment are as follows", "Comparing the deviance of every flow rate produces the following",
"The following is a temperature vs. time graph". A reader who wants to know which chart is which has
to read the in-plot titles, which is the only reason the paper is legible.

Section 5 is a template run eight times. Seven alternative tub designs are each given exactly two
exhibits - an unlabelled Inventor render alone on its page, then a deviance-against-flow-rate chart
on the next page whose title is the only identification - plus the standard tub, whose deviance chart
is printed TWICE, once on p16 as section 4.3.1's flow-rate selection and again on p20 as 5.1's first
case, with the identical title "Optimal Flow Rate (SA: 1800, V: 25200)". All eight charts share one
recipe: abscissa "Flow Rate (GPM)" 1.0 to 16.0, a unitless "Deviance" ordinate whose limits change
from chart to chart (2-32 for the square tub up to 1000-4000 for the fiberglass run), and an unframed
outside-left legend with two entries, "Bathtub" and "Minimum". No minimum point is visible in any of
the eight. The appendix explains the absence: the plotting code appends the second series as a single
point carrying its value, so the minimum is drawn at the curve's own floor - and in three of the eight
charts that floor lies below the frame's lowest tick, which is why the text can tell the reader the
answer is "the point indicated at the bottom of the graph, at (1.81, 10.179381314125882)" while the
graph shows no such point.

The four k-value regressions (pp12-14) are the same four data points plotted four times against four
transforms of one predictor - V^2/SA^3, its square, its square root and its cube root - with
R squared 0.99764, 0.996529, 0.999294 and 0.999299 printed inside the frames. Nothing in the four
screenshots distinguishes them except tick labels, and the paper adopts the last one and reports its
fit as "R2 = 0.99929854436231100000" - twenty significant digits from four points.

Two plotting defects change what the exhibits say. The three exponential fits printed on p10 read
"Y = 77e^-0.029x" with no asymptote constant, while equations (8) to (10) on p11 all read
"y = 77e^-knx + 23": the plot's own labels imply the water cools to 0 degrees instead of the 23
degree room. And p11's second plot is the SAME experiment after the offset has been subtracted -
37 degrees of bath water appearing at 16 degrees - still against an axis labelled "Temperature
[degrees Celsius]" and still under the identical title "Temperature vs. Time for Real-World Bathtub
Experiment"; the constant is restored as +21 in equation (24), not the +23 the beakers use, and the
paper never mentions the difference.

Design and rendering: the eight Inventor renders carry no dimension, no scale bar, no axis and no
name, and are printed one per page at full page height; the blueprint of Figure 2 is pasted as a
low-resolution screenshot of a drawing sheet, with the smallest dimension callouts illegible at
printed size; Figures 3 and 4 are renderings rather than photographs and are not drawn to the same
scale as the blueprint. The scatter on p35 has three points and is titled with the quantity that is
held constant, as is the four-point scatter on p36, so the pair is named for its constants and the
abscissae have to be read to tell them apart.

Families: line 16, surface-or-3D 8, scatter 7, photo-or-raster-image 3, flowchart-or-schematic 1.
"""

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": [],
    "excluded_regions": [],
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc95-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables 0", "excluded 0")
print("regions accounted", len(ITEMS))
