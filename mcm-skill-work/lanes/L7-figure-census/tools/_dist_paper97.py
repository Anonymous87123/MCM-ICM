"""Hand census of P-B-2016-48573-960f7126 (Team 48573, 30 pages, 13 measured regions).

A space-debris orbital-debris-removal (ODR) paper. Thirteen measured regions resolve into TWELVE
FIGURE ROWS, ONE TABLE ROW and NO EXCLUSION.

  p4  r1  Figure 1   photo-or-raster-image  a dark render of the Earth in LEO, square 198 pt
  p5  r1  Figure 2   line                   the object catalogue 1956-2012 with red annotations drawn on
  p10 r1  Figure 3   line                   dual y axis, Sh/Sl/D, "with ODR"
  p12 r1  Figure 4   node-link-network      four nodes into D, edges labelled minus theta D S
  p13 r1  Figure 5   line                   dual y axis, Sh/Sl/D, "without ODR"
  p15 r1  Figure 6   node-link-network      the same diagram with five nodes
  p16 r1  Figure 7   line                   dual y axis, Sh/Sl/D, "with specialization"
  p18 r1  Figure 8   line                   dual y axis, Sh/Sl/D, "with recycling"
  p19 r1  Figure 9   line                   four Sh/Sl curves, single left axis, beta halved
  p19 r2  Figure 10  line                   four Sh/Sl curves, single left axis, beta doubled
  p22 r1  Table 1    table-grid             the AHP two-layer hierarchy, 3 by 6, booktabs
  p23 r1  --         bar                    grouped bars, four cleaners by five criteria, NO CAPTION
  p25 r1  Figure 11  surface-or-3D          the surveillance box and the inner box, X/Y/Z arrows

THREE PRINTED TABLES CARRY NO ROW because fig_extract measured no region over them: the RI
coincidence scale on p22, the AHP score table on p23 and the ranking table inside the executive
summary on p29. They are declared gaps in the note, not silently dropped regions.

THE PAIR THE PAPER COMPARES IS DRAWN ON INCOMPATIBLE AXES. Figure 3 ("with ODR") prints "Debris
Number x 10^3" as its right-axis label with integer ticks 0, 2, 4 and a SECOND, floating "x 10^4"
above the frame; Figure 5 ("without ODR") prints the same label with ticks 0, 1000, 2000. The two
exhibits that carry the paper's central result therefore key their debris series to spans of 4e4
and 2e6, and neither prints which curve belongs to which axis.

ONE SENTENCE IS CUT IN HALF BY A FIGURE. The paragraph that begins at the foot of p18 ("...and a
lower peak appears at an advanced time with") is interrupted by Figure 9, prints the figure's
caption, and resumes on the line below it as "bigger beta. These observations are in accordance
with our hypothesis."

Only Figures 1 and 2 are named by a sentence, both on p4, one page before Figure 2 prints.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2016-48573-960f7126"
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


def place(page: int, reg: int, kind: str, path: list[str], order: int = 1) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": order,
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
            variables: int = 0, sentences: int = 1) -> dict:
    """Caption block. `verbatim` is what the page prints under the exhibit."""
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": sentences, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def no_caption() -> dict:
    """The block for an exhibit that prints no caption at all: the p23 bar chart."""
    return {"verbatim": "", "numbering": "none", "words": 0, "sentences": 0, "units": False,
            "variables": False, "variable_count": 0, "conditions": False, "concludes": False,
            "voice": "none", "position": "below"}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


def head(page: int, prefix: str) -> str:
    """The indexed heading on `page` whose label starts with `prefix`, exactly as printed."""
    for h in CTX["headings"]:
        if h["page"] == page and h["label"].startswith(prefix):
            return h["label"]
    raise SystemExit(f"no heading on p{page} starting {prefix!r}")


S_11 = [head(4, "1 Introduction"), head(4, "1.1 Background")]
S_23 = [head(6, "2 Models"), head(7, "2.3 Establishment")]
S_24 = [head(6, "2 Models"), head(10, "2.4 Model II")]
S_31 = [head(13, "3 Model Extension"), head(13, "3.1 What if")]
S_33 = [head(13, "3 Model Extension"), head(17, "3.3 What if")]
S_4 = [head(18, "4 Sensitivity Analysis")]
S_53 = [head(20, "5 Evaluation Model"), head(21, "5.3 Analytic")]
S_54 = [head(20, "5 Evaluation Model"), head(24, "5.4 A proper")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_PRINTED = schema.printed_lines(PID)
for _group in (S_11, S_23, S_24, S_31, S_33, S_4, S_53, S_54):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN and schema.norm(_label) not in _PRINTED:
            raise SystemExit(f"section label is neither an indexed heading nor a printed line: "
                             f"{_label!r}")

# The printed captions. Every one of them is a colon and a noun phrase; no caption has a verb.
CAP1 = caption("Figure 1: LEO view")
CAP2 = caption("Figure 2: Satellites around earth")
CAP3 = caption("Figure 3: The satellite and debris population with ODR")
CAP4 = caption("Figure 4: The structure of the system")
CAP5 = caption("Figure 5: The satellite and debris population without ODR")
CAP6 = caption("Figure 6: The structure of the system with different cleaners")
CAP7 = caption("Figure 7: The satellite and debris population with specialization")
CAP8 = caption("Figure 8: The satellite and debris population with recycling")
CAP9 = caption("Figure 9: β is half of its original value")
CAP10 = caption("Figure 10: β doubles its original value")
CAPT1 = caption("Table 1: Two-Layer Hierarchy Structure", numbering="Table N:")
CAP11 = caption("Figure 11: approach to avoid collision")

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_block: dict, cap_src: str, mention: dict,
           section: list[str], note: str, geo: dict | None = None, number: str = "",
           section_kind: str = "other", confidence: str = "high", order: int = 1) -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap_block["verbatim"],
        "caption": cap_block, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section, order),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    })


def table(page: int, reg: int, section: list[str], note: str, spec: dict,
          cap_block: dict | None = None, cap_src: str = "none",
          section_kind: str = "other", order: int = 1) -> None:
    block = cap_block or no_caption()
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
        "family": "table-grid", "caption_source": cap_src,
        "caption_verbatim": block["verbatim"], "caption": block, "table": spec,
        "place": place(page, reg, section_kind, section, order),
        "mention": uncited(), "note": note, "confidence": "high",
    })


# ============================================================ 1.1: the two opening exhibits
figure(4, 1, "photo-or-raster-image", CAP1, "text-layer",
       cited(4, 4, ["Figure 1"], 1,
             "Figure 1 shows the debris distribution in view of LEO (low earth orbit)"),
       S_11,
       "A dark render of the Earth: deep-blue oceans, green landmasses, a dark band from the upper "
       "left across the globe, and a field of fine white speckles over and around it. No axes, no "
       "scale, no legend, no title, no arrow and no key - NOTHING ON THE EXHIBIT SAYS WHAT THE "
       "SPECKLES ARE. The sentence that names it reads 'the debris distribution' off the picture, "
       "but the same speckles would serve equally as stars, as the catalogue of satellites or as the "
       "debris the paper means, and the exhibit prints no annotation to decide between them. The "
       "globe is also oriented against the page: South America sits at the centre with the north "
       "pole toward the lower left, so the picture is either rotated or a view from below. It is a "
       "198 by 198 pt square, the smallest region in the paper by width, and at print size the "
       "speckle field reads as noise.",
       geometry("photo-or-raster-image"), "1", section_kind="introduction")

figure(5, 1, "line", CAP2, "text-layer",
       cited(4, 5, ["Figure 2"], 1,
             "Figure 2 illustrates the number of different types of debris from year 1956 to 2012"),
       S_11,
       "Five polyline series over a light grey grid, 'Year' 1956 to 2012 in two-year steps against "
       "'Number of Objects' 0 to 16000 in steps of 1000, under the in-plot title 'Monthly Number of "
       "Objects in Earth Orbit by Object Type' and a five-entry legend inside the frame at the upper "
       "left: Total Objects, Fragmentation Debris, Spacecraft, Mission-related Debris, Rocket Bodies. "
       "The Total Objects series is drawn far heavier than the four under it. ON TOP OF THE PLOT A "
       "SECOND HAND HAS DRAWN RED CIRCLES, RED ARROWS AND RED-OUTLINED TEXT BOXES - 'Iridium 33 & "
       "Cosmos 2251 collision' and 'Chinese ASAT test' - over the 2008 and 2009 steps; the ellipses "
       "cover the very steps they annotate, so the size of the jump they point at is hidden by the "
       "mark that points at it. Both label and title disagree with the content: the caption names one "
       "of the five series ('Satellites around earth') and the title's 'Monthly' meets an abscissa "
       "graduated in years.",
       geometry("line", legend="inside"), "2", section_kind="introduction")

# ============================================================ 2.3 and 2.4: the two population runs
figure(10, 1, "line", CAP3, "text-layer", uncited(), S_23,
       "The ODR run: three curves - Sh blue, Sl orange, D magenta - over 'Time (year)' 0 to 150, with "
       "a left axis 'Spacecraft Number x 10^3' 0 to 4 and a right axis labelled 'Debris Number x "
       "10^3'. THE RIGHT AXIS CARRIES TWO MULTIPLIERS AT ONCE: its own label says x 10^3, its ticks "
       "are the bare integers 0, 2 and 4, and a separate 'x 10^4' is printed OUTSIDE the frame above "
       "the top right corner, so the debris scale is either 0 to 4e3, 0 to 4e4 or 0 to 4e7 and the "
       "exhibit does not say which. Nothing on the figure assigns a curve to an axis; the magenta D "
       "curve leaves the frame through the top before year 150 while the two satellite curves decay "
       "to zero on the left scale. No in-frame title, legend inside the frame at the upper right, "
       "caption below. The only sentence that points at it is 'From the graph we can see the "
       "satellite population reaches its peak around the 50 years in the future', which names no "
       "figure.",
       geometry("line", legend="inside"), "3", section_kind="model")

figure(12, 1, "node-link-network", CAP4, "text-layer", uncited(), S_24,
       "Four blue circles - W above, Sl left, Sh right, D in the centre - joined by three thin blue "
       "arrows that ALL POINT INTO D, each label written beside its arrow in italic mathematics: "
       "minus delta W D on the vertical edge, minus theta(l) D Sl on the left edge, minus theta(h) D "
       "Sh on the right edge. No axes, no legend, no scale. THE DIAGRAM USES A SYMBOL THE EQUATIONS "
       "ABOVE IT DO NOT: the ODE system printed on the same page writes dSl/dt = -beta(l) D Sl + "
       "alpha(l) - gamma(l) and dD/dt = (beta(h)Sh + beta(l)Sl)DN1 + ... - theta W D, while the "
       "figure's loss edges are labelled theta, so the collision coefficient beta of the equations "
       "appears as the cleaning efficiency theta of the figure, and the reader has to notice that "
       "only the cleaner edge (-delta W D) agrees with the system. The diagram also carries no "
       "launch (+alpha), no expiry (-gamma), no fragments (+N) and no natural growth (+lambda), so "
       "four of the five terms of the system it illustrates have no arrow. Sl and Sh are clipped by "
       "the left and right edges of the picture.",
       geometry("node-link-network"), "4", section_kind="model")

figure(13, 1, "line", CAP5, "text-layer", uncited(), S_24,
       "The twin of Figure 3, run without ODR: the same three curves and the same legend inside the "
       "frame at the upper right, over 'Time (year)' 0 to 150 and 'Spacecraft Number x 10^3' 0 to 4, "
       "with a right axis printed 'Debris Number x 10^3' and ticks 0, 1000 and 2000. THE PAIR THAT "
       "CARRIES THE PAPER'S RESULT IS KEYED TO INCOMPATIBLE SCALES: this exhibit's debris axis reads "
       "0 to 2e6, while Figure 3's reads 0 to 4e4 once its floating x 10^4 is taken and 0 to 4e3 "
       "without it - a span fifty times larger here than there - so the difference the prose draws "
       "between 'with ODR' and 'without ODR' is drawn on two rulers, and neither exhibit says which "
       "curve is on which axis. The pointer names no figure either: 'Running the model by MATLAB, the "
       "development of this system is shown in the following figure.'",
       geometry("line", legend="inside"), "5", section_kind="model")

# ============================================================ 3.1: the cleaner variants
figure(15, 1, "node-link-network", CAP6, "text-layer", uncited(), S_31,
       "The same four-circle diagram widened to five: W1 above, W2 below, Sl left, Sh right, and the "
       "centre node written (D1 D2). The arrows still all point inward and every label carries the "
       "summed debris of the two size classes - minus theta(l)(D1+D2)Sl on the left, minus "
       "theta(h)(D1+D2)Sh on the right, minus delta W1(D1+D2) above and minus delta W2(D1+D2) below. "
       "No axes, no legend. The two outer circles are clipped by the frame edges and the centre "
       "label is the only node whose text is not a single symbol. IMMEDIATELY UNDER THE CAPTION the "
       "page prints the nine parameters the figure's symbols stand for as a bulleted list (W2 0.015, "
       "D1 5000, D2 15000, p1 0.7, p2 1.2, theta1 10, theta2 3, rho1 0.25, rho2 0.75), which is the "
       "only place in the paper where a node's value can be read - and the caption's own printed "
       "line runs straight into the first of those bullets.",
       geometry("node-link-network"), "6", section_kind="model")

figure(16, 1, "line", CAP7, "text-layer", uncited(), S_31,
       "The dual-axis population template again, now with two cleaner classes: Sh, Sl and D over "
       "'Time (year)' 0 to 150, left 'Spacecraft Number x 10^3' 0 to 4 in steps of 0.5, right 'Debris "
       "Number x 10^3' 0 to 600. Legend inside the frame at the upper right, no in-frame title, "
       "caption below and then the 3.2 heading. The right axis tops out at 600x10^3 against Figure "
       "3's 4x10^4 and Figure 5's 2x10^6, so the four population exhibits of this paper print four "
       "different debris scales and no table reconciles them. Nothing identifies which curve belongs "
       "to which axis.",
       geometry("line", legend="inside"), "7", section_kind="model")

# ============================================================ 3.3: recycling
figure(18, 1, "line", CAP8, "text-layer", uncited(), S_33,
       "The template again for the recycling variant: Sh blue, Sl orange and D magenta over 'Time "
       "(year)' 0 to 150, left 'Spacecraft Number x 10^3' 0 to 4, right 'Debris Number x 10^3' 0 to "
       "16000 in steps of 2000. THE AXIS AND THE PROSE CANNOT BOTH BE RIGHT: the paragraph below the "
       "caption reads the debris population at year 60 as '28.95 thousand without recycle and 168 "
       "thousand with recycle system', but the magenta curve sits near two units of the right-hand "
       "tick scale there, which is about two million with the printed x 10^3 multiplier and about two "
       "thousand without it - neither figure is 168 thousand. Half of the left axis (2 to 4) is empty "
       "because no satellite curve passes 1.6, the legend box sits over the top of the rising debris "
       "curve and overlaps it, and the magenta curve leaves the frame before year 150. No in-frame "
       "title; caption below.",
       geometry("line", legend="inside"), "8", section_kind="model")

# ============================================================ 4: the beta sweep
figure(19, 1, "line", CAP9, "text-layer", uncited(), S_4,
       "The first of the collision-rate pair: FOUR satellite curves on a single left axis, "
       "'Spacecraft Number x 10^3' 0 to 1.6, over 'Time (year)' 0 to 150 - Sh and Sl at the original "
       "beta as solid blue and solid orange, then the half-beta pair as a dashed yellow and a dashed "
       "purple. The legend inside the frame at the upper right spells the same word two ways in one "
       "box: 'SH(Original Beta)' and 'SL(Origin Beta)'. NO DEBRIS CURVE AND NO DEBRIS AXIS: the "
       "parameter being varied is the collision rate between debris and satellites, yet D is absent "
       "from the exhibit and the reader cannot see the quantity the variation acts on. The left "
       "scale is also 0 to 1.6 where Figures 3 to 8 print 0 to 4, so this pair cannot be laid against "
       "them. THE SENTENCE THAT BEGINS AT THE FOOT OF p18 IS CUT IN HALF BY THIS FIGURE: it stops at "
       "'...a lower peak appears at an advanced time with' and resumes below the caption as 'bigger "
       "beta. These observations are in accordance with our hypothesis.'",
       geometry("line", legend="inside"), "9", section_kind="sensitivity", order=1)

figure(19, 2, "line", CAP10, "text-layer", uncited(), S_4,
       "The second of the pair, drawn from the identical template: the same four-curve single-axis "
       "frame, 0 to 1.6 on 'Spacecraft Number x 10^3' and 0 to 150 on 'Time (year)', with the legend "
       "inside the upper right now reading 'SH(Original Beta)', 'SL(Origin Beta)', 'SH(Double Beta)' "
       "and 'SL(Double Beta)' - three of the four entries keep the misspelling the first figure "
       "makes. The two exhibits are a page's height apart on the same sheet with nothing between "
       "them but a caption, and the only pointer in the paper is the p18 sentence 'The first figure "
       "shows the result when beta is decreased to 0.5 times. The second shows the result when beta "
       "doubles.' - which names neither number and prints on the page before both pictures. Below "
       "the caption, the page turns to '(2) Numbers of Fragments Produced : N'.",
       geometry("line", legend="inside"), "10", section_kind="sensitivity", order=2)

# ============================================================ 5.3: the AHP hierarchy
table(22, 1, S_53,
      "The AHP hierarchy as a three-column grid with a header row and five body lines: the Goal "
      "column holds the single phrase 'Rank of the Cleaners', the Criteria column stacks the five "
      "criteria (Cost, Efficiency, Production Cycle, Disturbance, Life Expectancy) and the "
      "Alternatives column stacks the four cleaners (Laser, SpaDE, Water Jet, Tethered Tug). Ruling: "
      "one rule above the header, one under it and one at the foot, with NO vertical rule, no box "
      "and no interior row rule - the booktabs shape - so the five criteria and the four alternatives "
      "are related to the goal by vertical position alone, and nothing lines the criteria against the "
      "alternatives. The table is centred, 306 pt wide against a 419 pt text measure, and it prints "
      "its caption BELOW itself: 'Table 1: Two-Layer Hierarchy Structure'. NO SENTENCE IN THE PAPER "
      "NAMES IT - the AHP section points at its exhibits with 'the following table' and with nothing "
      "at all for this one; the criteria the chart on p23 abbreviates are printed in full here and "
      "nowhere else.",
      {"rows": 6, "cols": 3, "header_rows": 1, "rule_style": "booktabs", "zebra": False,
       "merged_cells": False, "diagonal_header": False, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 0, "text_cols": 3, "width": "full",
       "orientation": "portrait", "continued": False, "note_sentence": ""},
      CAPT1, "text-layer", section_kind="evaluation")

# ============================================================ 5.3: the grade vectors, uncaptioned
figure(23, 1, "bar", no_caption(), "none", uncited(), S_53,
       "A grouped column chart of the AHP grade vectors: four series - cyan Laser, blue SpaDE, green "
       "Water Jet, yellow Tethered Tug - over five categories labelled Cost, Efficiency, PC, "
       "Disturbance and Life Span, on a bare ordinate running 0 to 0.8 in steps of 0.1 with NO AXIS "
       "TITLE, no in-frame title, no gridline and no value printed on any column. The legend sits "
       "inside the frame at the upper right. NO CAPTION AND NO NUMBER: the prose above it says 'The "
       "grade vectors of four alternatives in the respect of five criteria is shown in the following "
       "figure' and the line below the chart says 'The final score of four alternatives are', so the "
       "exhibit is bracketed by two sentences that name no figure and describe neither the axis nor "
       "the scale. TWO OF THE FIVE CATEGORY LABELS ARE ABBREVIATED AWAY FROM THE PAPER'S OWN "
       "VOCABULARY: 'PC' is the Production Cycle and 'Life Span' the Life Expectancy that Table 1 on "
       "the previous page prints in full, and 'Efficiency' drops the 'cleaning' the section text "
       "keeps. SpaDE is highest on Cost, Efficiency and Disturbance and Water Jet on PC, while Laser "
       "and Tethered Tug stay below 0.25 everywhere - which is the ranking the paper adopts but which "
       "no number on the chart confirms.",
       geometry("bar", legend="inside"))

# ============================================================ 5.4: the surveillance geometry
figure(25, 1, "surface-or-3D", CAP11, "text-layer", uncited(), S_54,
       "A three-dimensional illustration rather than a data plot: a translucent orange box drawn in "
       "axonometric projection with a small blue solid at its centre, black X, Y and Z arrows through "
       "the origin, dotted guide lines on the ground plane, and two leader labels, 'Surveilling Box' "
       "pointing at the orange box and 'Inner Box' at the blue solid. No axes are graduated, no "
       "value, no unit, no legend and no dimension appears anywhere on it. It is the only exhibit in "
       "the paper that depicts a geometry rather than a run, and its caption - 'Figure 11: approach "
       "to avoid collision' - describes neither of the two things the picture labels: the exhibit "
       "shows the surveillance volume and the inner volume, not the minimum-distance test the prose "
       "derives immediately above it (md = |Rs - Rd|). The picture sits at the bottom of the page, "
       "caption below, and no sentence names it.",
       geometry("surface-or-3D", three_d="isometric"), "11", section_kind="evaluation")

RULES = [
    "Measure first, then read the pixels: thirteen measured regions resolve into twelve figure rows "
    "and one table row with no exclusion, and every region is accounted for once "
    "[place.doc_order].",
    "Three printed tables have no measured region and therefore no row: the RI coincidence scale on "
    "p22, the AHP score table on p23 and the ranking table in the executive summary on p29 are "
    "recorded as declared gaps in the note, because a census that silently omits them would report a "
    "paper with one table [table.rule_style].",
    "A caption that names one series of a five-series chart is not a description of the exhibit: "
    "'Figure 2: Satellites around earth' sits under a plot of five object classes whose in-plot "
    "title says something else again [caption.verbatim].",
    "The two exhibits the paper compares for its central result key their debris series to different "
    "multipliers, x 10^4 against x 10^3 with a tick span fifty times larger, and neither assigns a "
    "curve to an axis [geometry.shared_axes].",
    "A diagram is read against the equations on its own page: Figure 4 labels its satellite-loss "
    "edges theta where the ODE system above it writes beta, and four of the system's five terms have "
    "no arrow at all [geometry.family].",
    "A figure can be inserted into the middle of a sentence and the census records the exhibit, not "
    "the split: the paragraph that stops at the foot of p18 resumes under Figure 9's caption on p19 "
    "[caption.position].",
    "A bare pointer is not a citation: 'the development of this system is shown in the following "
    "figure', 'Then the satellite and debris population are shown in the figure', 'The first figure "
    "shows the result ... The second shows the result' and 'is shown in the following figure' name "
    "no exhibit, so ten figure rows and the one table row record no citation at all "
    "[mention.count].",
    "Two exhibits in this paper print no caption and no plot title and one of those still carries the "
    "paper's adopted ranking: the p23 grouped bars are keyed by an in-frame legend alone, and their "
    "category labels abbreviate the vocabulary Table 1 prints in full [caption.numbering].",
]

NOTE = """\
Paper 97, Team 48573, an orbital-debris-removal model with an AHP cleaner evaluation. Thirty pages,
thirteen measured regions on thirteen of them, resolving into TWELVE FIGURE ROWS and ONE TABLE ROW,
with no exclusion and nothing unaccounted. The paper prints seven tables' worth of grid in total but
fig_extract boxed only one, so three printed tables are declared gaps rather than silently dropped:
the RI coincidence scale on p22, the AHP score table on p23 and the ranking table inside the
executive summary on p29. None of the three carries a caption or a number.

Citation is nearly absent. Only Figures 1 and 2 are named by a sentence, both on p4 - "Figure 1
shows the debris distribution in view of LEO (low earth orbit)" and "Figure 2 illustrates the number
of different types of debris from year 1956 to 2012", the second naming a figure that prints on the
next page. The other ten figures and Table 1 are pointed at only by phrases that name nothing: "A
diagram can be drawn to illustrate the structure of the system", "Running the model by MATLAB, the
development of this system is shown in the following figure", "Also, we can use a diagram to
illustrate the structure", "The result is shown in the following figure", "Then the satellite and
debris population are shown in the figure", "The first figure shows the result when beta is
decreased to 0.5 times. The second shows the result when beta doubles", "The grade vectors of four
alternatives in the respect of five criteria is shown in the following figure".

The exhibits disagree with each other on their own scales. Figures 3, 5, 7 and 8 are the same
MATLAB template - Sh, Sl and D over Time (year) 0 to 150 with a left axis "Spacecraft Number x 10^3"
- and they print four different debris axes: 0 to 4e4 (and a second, floating x 10^4 above the
frame) on Figure 3, 0 to 2e6 on Figure 5, 0 to 600x10^3 on Figure 7 and 0 to 16000x10^3 on Figure
8. Figure 3, the one the paper calls "with ODR", is the exhibit whose right axis carries two
multipliers at once: an "x 10^3" in the label, bare integer ticks 0, 2 and 4, and a separate
"x 10^4" printed outside the frame. The comparison the paper is built on - with ODR against
without - is therefore drawn on rulers whose spans differ by a factor of fifty, and not one of the
four figures says which curve is read on which axis. Figure 8 goes further: its paragraph reads the
year-60 debris as 168 thousand, while the curve sits near two units of a tick scale that multiplies
by a thousand, so the printed axis and the printed prose cannot both be right.

The two node-link diagrams are the only exhibits that state their symbols, and they state the wrong
one. Figure 4 labels the satellite-loss edges minus theta(l) D Sl and minus theta(h) D Sh while the
ODE system printed immediately above on the same page writes dSl/dt = -beta(l) D Sl + alpha(l) -
gamma(l); the collision coefficient of the equations appears in the diagram as the cleaning
efficiency, and only the cleaner edge, minus delta W D, matches. Both diagrams also drop four of the
system's five terms - no launch, no expiry, no fragments, no natural growth - and both clip their
outer nodes against the frame edges. Figure 6 repeats the figure with five nodes and two size
classes, and the page then prints the nine parameter values as a bulleted list that runs on from the
caption's own line.

The beta pair is the thinnest exhibit in the paper. Figures 9 and 10 plot four satellite curves and
NO debris curve, although the collision rate between debris and satellites is the parameter under
test; their legend spells the same word two ways inside one box, "SH(Original Beta)" against
"SL(Origin Beta)"; their left axis runs 0 to 1.6 where every other population figure runs 0 to 4, so
they cannot be laid against their own neighbours; and the two of them are printed a page's height
apart on the same sheet, keyed only by the p18 sentence that names no number. Figure 9 is also
inserted into the middle of a sentence: the paragraph that stops at the foot of p18 at "a lower peak
appears at an advanced time with" resumes under the caption as "bigger beta. These observations are
in accordance with our hypothesis."

Table 1 is the one exhibit of the paper that is laid out cleanly and the one nobody names. Three
columns - Goal, Criteria, Alternatives - with a header rule, a rule under the header and a foot rule
and nothing else, its five criteria stacked against four alternatives with no line relating the two
columns, and its caption below rather than above, which is the only caption in the paper that sits
under a table. On the next page the same five criteria appear as the five categories of a grouped
bar chart that prints no caption at all, abbreviates two of them away from the vocabulary Table 1
establishes ("PC" for Production Cycle, "Life Span" for Life Expectancy) and carries no axis title,
no value label and no title in the frame - and that uncaptioned chart is the exhibit the paper's
adopted ranking rests on.

Families: line 7, node-link-network 2, bar 1, photo-or-raster-image 1, surface-or-3D 1, table-grid 1.
"""

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc97-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
