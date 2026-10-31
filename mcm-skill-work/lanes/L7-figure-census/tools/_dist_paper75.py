"""Hand census of P-B-2015-32879-2c587e51 (Team 32879, 35 pages, 32 measured regions).

Thirty-two measured regions over twenty-four of the thirty-five pages. Thirty become figure
rows and two are refused, so nothing is unaccounted for and nothing is left unresolved. The
paper prints no numbered tables at all; the only grid-shaped artwork in it is the cover form
on p1, which is a registration block, not an exhibit.

   p1  r1  refused - the cover's "For office use only" registration block
   p5  r1  Fig.1b  bearing-change sketch, top view
   p5  r2  Fig.1a  glide-angle sketch, side view
   p6  r1  Fig.2   glide-slope right triangle
   p8  r1  Fig.3   prior probability surface
   p9  r1  Fig.4   corridor of width W
   p10 r1  Fig.5   sweep offset h on the same corridor
   p12 r1  Fig.6   prior and posterior over a discrete index
   p13 r1  Fig.7   contour map of the mass distribution
   p15 r1  Fig.8   zoom box over a contour, beside the parallel sweep path
   p16 r1  Fig.9   density surface after five days
   p16 r2  Fig.10  cumulative and daily probability curves
   p17 r1  Fig.11  density surface, rectangular search
   p18 r1  Fig.12  cumulative curve, rectangular search
   p18 r2  Fig.13  spiral sweep diagram
   p19 r1  Fig.14  contour plus the two mirrored spiral ladders
   p20 r1  Fig.15  density surface, spiral search
   p20 r2  Fig.16  cumulative curve, spiral search
   p21 r1  Fig.17  octagonal sector search diagram
   p21 r2  Fig.18  contour plus the octagon's diagonal bands
   p22 r1  Fig.19  density surface, octagonal search
   p23 r1  Fig.20  cumulative curve, octagonal search
   p24 r1  Fig.21  four-model comparison
   p25 r1  Fig.22  five-plane comparison
   p26 r1  Fig.23  density surface for the stall case
   p26 r2  Fig.24  four-model comparison for the stall case
   p27 r1  Fig.25(a) small-plane comparison over 20 days
   p27 r2  Fig.25(b) the same over 5 days
   p28 r1  Fig.26  same against different paths
   p30 r1  Fig.27  two effectiveness values
   p31 r1  Fig.28  747 against Cessna
   p35 r1  refused - the closing letter's letterhead

Thirty figure rows and two refusals, no tables and nothing unresolved.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2015-32879-2c587e51"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]
        KIND[(_pg["page"], _i)] = _r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

for _key, _bbox in REG.items():
    _ctx = CTXREG.get(_key)
    if _ctx is None or max(abs(a - b) for a, b in zip(_ctx["bbox"], _bbox)) > 0.5:
        raise SystemExit(f"region numbering disagrees with the context dump at {_key}")

# 595.32 x 841.92 pt page; the text block runs x 56.7 to 538.6, so the measure is 481.9 pt
MEASURE = 481.9
DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def cap(page: int, prefix: str, tail: str) -> str:
    """Take the caption verbatim out of the layer: from its number to its last printed word."""
    text = schema.page_text(PID, page)
    start = text.find(prefix)
    if start < 0:
        raise KeyError((page, prefix))
    end = text.find(tail, start)
    if end < 0:
        raise KeyError((page, tail))
    return schema.norm(text[start:end + len(tail)])


def pct(span: float) -> str:
    return f"{span / MEASURE * 100:.1f}"


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


def none_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          pattern: str = "direct") -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": 1, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


# ---------------------------------------------------------------- section paths
HEAD = {h["number"]: h["label"] for h in CTX["headings"] if h.get("number")}


def sec(number: str) -> list[str]:
    """Printed heading chain for a numbered heading, built from the ctx index."""
    parts = number.split(".")
    chain = [".".join(parts[:i]) for i in range(1, len(parts) + 1)]
    return [HEAD[k] for k in chain if k in HEAD]


SEC_THEORY = sec("2.1")
SEC_BAYES = sec("2.2")
SEC_POST = sec("2.3")
SEC_OPT = sec("2.4")
SEC_GRID = sec("3.1")
SEC_SQUARE = sec("3.3")
SEC_RECT = sec("3.4")
SEC_SPIRAL = sec("3.5")
SEC_SECTOR = sec("3.6")
SEC_VARY = sec("3.7")
SEC_ONE = sec("3.7.1")
SEC_FIVE = sec("3.7.2")
SEC_STALL = sec("3.7.3")
SEC_SHORT = sec("3.7.4")
SEC_PATHS = sec("3.7.5")
SEC_EFF = sec("3.7.6")


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", note: str = "",
           other_note: str = "", shared_axes: bool = False,
           confidence: str = "high") -> None:
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": confidence,
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, numbering),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "reason": reason,
        "note": note,
    })


# ---------------------------------------------------------------- refused artwork
excluded(1, 1, "not-an-exhibit",
         ("The cover's registration block: the lines For office use only, Team Control Number "
          "32879 and Problem Chosen B sit inside a ruled box with blank T1-T4 and F1-F4 cells "
          "beside them. No chart, no plotted data and no caption; the summary sheet's own title "
          "and abstract print below it as live text."))
excluded(35, 1, "not-an-exhibit",
         ("The letterhead of the closing letter to commercial airlines - the firm's name block "
          "and address rule - measured as a raster because the letter is set as a two-column "
          "page with that banner across the top. It carries no number and no caption and holds "
          "no data; the letter's text runs below it to the page foot."))

# ---------------------------------------------------------------- chapter 2: the theory sketches
figure(5, 1, "flowchart-or-schematic",
       cap(5, "(b) Visual definition of", "."), "none",
       cited(5, 5, ["Figures 1a & 1b"], 1,
             "These quantities are illustrated in Figures 1a & 1b below:"),
       "model", SEC_THEORY, labels=True, note=(
           "Top view of an aircraft silhouette with the North reference drawn as a dashed "
           "vertical line, a fan of dashed arcs sweeping to a point marked C, and the bearing "
           "change labelled beside the arc. Caption (b) prints under the right-hand panel."))
figure(5, 2, "flowchart-or-schematic",
       cap(5, "(a) Visual definition of", "."), "none",
       cited(5, 5, ["Figures 1a & 1b"], 1,
             "These quantities are illustrated in Figures 1a & 1b below:"),
       "model", SEC_THEORY, labels=True, note=(
           "Side view of a jet in a glide: the aircraft nose-down along a dashed descent line, "
           "the Horizontal reference dashed above it, and the glide angle marked between the "
           "two. Caption (a) prints under the left-hand panel. The two panels are separate "
           "measured boxes because the paper captions them separately, and the text layer "
           "carries both letters as ordinary Greek - theta for (a), phi for (b) - not as "
           "private-use glyphs."))
figure(6, 1, "flowchart-or-schematic",
       cap(6, "Figure 2: Derivation", "Maximum Glide Range."), "Figure N:",
       cited(5, 6, ["Figure 2"], 1,
             "as shown in Figure 2 below, an expression defining the maximum range"),
       "model", SEC_THEORY, labels=True, note=(
           "A right triangle standing on its base: the vertical leg is the altitude h, the base "
           "is the maximum range, the hypotenuse is labelled Glide Slope, the point of lost "
           "contact sits at the apex and the ocean at the far end, with the same minimum glide "
           "angle marked at both vertices. The caption's number is the only numeral in the "
           "drawing."))
figure(8, 1, "surface-or-3D",
       cap(8, "Figure 3: Initial", "Plane Location."), "Figure N:",
       cited(7, 8, ["Figure 3"], 1,
             "Figure 3 below displays the initial probability distribution for our example "
             "aircraft"),
       "model", SEC_BAYES, legend="none", numbers=True, three_d="surface-mesh", note=(
           "MATLAB mesh surface titled Prior Probability Density: one smooth mound of "
           "probability over the x and y coordinates in miles, axes running -150 to 150 on "
           "both, the vertical axis a Probability scale to 2 x 10^-4. The grid is dense enough "
           "that the wireframe reads as shading; no colour bar and no legend. The prose "
           "announces it on the page before it prints."))
figure(9, 1, "flowchart-or-schematic",
       # The layer prints an extra space before the full stop in this one caption.
       cap(9, "Figure 4: Visual", "of W ."), "Figure N:", none_mention(),
       "model", SEC_POST, labels=True, note=(
           "Two parallel blue curves with a dashed centreline between them, drawn inside a "
           "plain frame - the corridor a single pass sweeps out - with the width marked at the "
           "left end. The axis letters A and W are the only text; there are no axes and no "
           "numbers."))
figure(10, 1, "flowchart-or-schematic",
       cap(10, "Figure 5: Visual", "of h."), "Figure N:", none_mention(),
       "model", SEC_POST, labels=True, note=(
           "The same framed corridor as Figure 4, this time with one incremental swept "
           "rectangle drawn across the path and the offset marked h at its lower edge. Same "
           "frame, same two parallel curves, same absence of axes; only the marked segment "
           "differs from Figure 4."))
figure(12, 1, "line",
       cap(12, "Figure 6: Two Dimensional", "Bayesian Inference."), "Figure N:",
       cited(11, 12, ["Figure 6"], 1,
             "shown below in Figure 6, where the middle section is"),
       "model", SEC_OPT, legend="inside", numbers=True, note=(
           "Two curves over a discrete index axis 0 to 120: the prior rising and falling "
           "smoothly, the posterior the same shape with a bite taken out of its middle where "
           "the section has been searched. Legend inside the top right - Prior Probability and "
           "Posterior Probability - over a plot title that reads Discrete Application of Bayes "
           "Theorem. The plot is vector, so its axis and legend text are in the layer, y-axis "
           "label included and printed mirrored."))
figure(13, 1, "heatmap-or-contour",
       cap(13, "Figure 7: Contour map", "mass distribution."), "Figure N:", none_mention(),
       "model", SEC_GRID, legend="none", numbers=True, note=(
           "A filled contour plot of the prior probability mass: nested bands of colour fanned "
           "across a wedge that widens from a single bright spot at the origin up to the top of "
           "the frame, over x and y coordinates in miles on axes of -100 to 100 and -110 to "
           "110. No contour labels, no colour bar, no legend - the bands themselves carry the "
           "quantity."))
figure(15, 1, "composite-panel",
       cap(15, "Figure 8: “Parallel Sweep”", "search square."), "Figure N:",
       cited(15, 15, ["figure 8"], 1, "from figure 8", "parenthetical"),
       "model", SEC_SQUARE, panels=2, layout="row of 2", numbers=True, labels=True, note=(
           "Two panels joined by a single arrow: on the left the contour plot of the prior with "
           "a box zoomed out of its middle, and on the right the square that box becomes, "
           "crossed by four parallel sweeps drawn as orange double-headed arrows with the "
           "green search corridor under them, the pass width and the square side marked at the "
           "foot. The panels are of different families - a filled contour and a geometric "
           "search-path drawing - so the row is a composite. The paper cites it twice on this "
           "page, once by description and once in lower case as 'from figure 8'."))

# ---------------------------------------------------------------- 3.3 to 3.6: one model per section
figure(16, 1, "surface-or-3D",
       cap(16, "Figure 9: Probability", "5-day search."), "Figure N:", none_mention(),
       "model", SEC_SQUARE, numbers=True, three_d="surface-mesh", note=(
           "The prior after five days of square searching, as a mesh surface: the mound has "
           "been eaten into from one side where the sweeps have already looked. Axes in miles, "
           "no colour bar, no legend."))
figure(16, 2, "line",
       cap(16, "Figure 10: Cumulative", "20-day search."), "Figure N:", none_mention(),
       "model", SEC_SQUARE, legend="inside", numbers=True, note=(
           "Two series over the 0-to-20-day search axis behind the title Single Plane Simple "
           "Square Search Model: the cumulative probability climbing to just under one and the "
           "daily probability falling away, both named in the legend inside the top left of the "
           "plot. Vector plot, axis and legend text in the layer, y-axis label mirrored."))
figure(17, 1, "surface-or-3D",
       cap(17, "Figure 11: Probability", "5-day search."), "Figure N:", none_mention(),
       "model", SEC_RECT, numbers=True, three_d="surface-mesh", note=(
           "The same surface after five days of rectangular searching, and the difference is "
           "legible: the searched rectangle has been cut clean out of the raised mass, leaving "
           "a squared crater edge rather than the soft bite of Figure 9."))
figure(18, 1, "line",
       cap(18, "Figure 12: Cumulative", "20-day search."), "Figure N:", none_mention(),
       "model", SEC_SPIRAL, legend="inside", numbers=True, note=(
           "The cumulative and daily probability pair again, this time behind the title Single "
           "Plane Rectangular Search Model. The caption and the plot title name the same "
           "search, and the caption is the only text that gives the figure a number."))
figure(18, 2, "flowchart-or-schematic",
       cap(18, "Figure 13: “Spiral Sweep”", "search square [12]."), "Figure N:",
       none_mention(), "model", SEC_SPIRAL, labels=True, note=(
           "The spiral sweep drawn as a search square: concentric dashed runs turning inward, "
           "arrowheads marking the direction of travel, and the growing radius of each arm "
           "marked at the corners. No axes and no numbers beyond those labels."))
figure(19, 1, "composite-panel",
       cap(19, "Figure 14: Symmetry", "“Spiral Sweep”."), "Figure N:",
       cited(19, 19, ["Figure 14"], 1, "as the arrows show in Figure 14"),
       "model", SEC_SPIRAL, panels=2, layout="row of 2", numbers=True, note=(
           "Two panels, and the point of the figure is that they are mirror images: on the left "
           "the contour plot of the prior, on the right two spiral ladders of dashed search "
           "runs wrapped around each other, one turning clockwise and one anticlockwise, with "
           "the arrows the prose points to. A filled contour beside a geometric search-path "
           "drawing, so the row is a composite."))
figure(20, 1, "surface-or-3D",
       cap(20, "Figure 15: Probability", "5-day search."), "Figure N:", none_mention(),
       "model", SEC_SPIRAL, numbers=True, three_d="surface-mesh", note=(
           "The prior after five days of spiral searching: a low basin across most of the frame "
           "with the probability pushed up into a single peak at one corner. Axes in miles, no "
           "colour bar."))
figure(20, 2, "line",
       cap(20, "Figure 16: Cumulative", "20-day search."), "Figure N:", none_mention(),
       "model", SEC_SPIRAL, legend="inside", numbers=True, note=(
           "The cumulative and daily pair for the spiral search, behind the title Single Plane "
           "Square Spriral Search Model - the paper's own misspelling of its own search name, "
           "printed inside the plot."))
figure(21, 1, "flowchart-or-schematic",
       cap(21, "Figure 17: “Sector Search”", "in a region [12]."), "Figure N:",
       none_mention(), "model", SEC_SECTOR, labels=True, note=(
           "The octagonal sector search drawn as a search region: an octagon holding sector "
           "arms that fan out from its centre, with several aircraft shapes in the sectors and "
           "the search distances marked at the corners. No axes throughout."))
figure(21, 2, "composite-panel",
       cap(21, "Figure 18: Parameters", "“Sector Search”."), "Figure N:",
       none_mention(), "model", SEC_SECTOR, panels=2, layout="row of 2", numbers=True, note=(
           "Two panels again: the contour plot of the prior on the left and, on the right, the "
           "regular octagon that the sector search is drawn inside, crossed by diagonal bands "
           "that stand for the sweeps and marked with the octagon's side length. Filled contour "
           "beside geometric drawing, so a composite."))
figure(22, 1, "surface-or-3D",
       cap(22, "Figure 19: Probability", "5-day search."), "Figure N:", none_mention(),
       "model", SEC_SECTOR, numbers=True, three_d="surface-mesh", note=(
           "The prior after five days of octagonal searching, and the surface carries the "
           "pattern of the search: the mesh is drawn as a spoked fan of petals rather than a "
           "smooth mound, under the plot title After 5 Days of Octagonal Sector Search."))
figure(23, 1, "line",
       cap(23, "Figure 20: Cumulative", "20-day search."), "Figure N:", none_mention(),
       "model", SEC_SECTOR, legend="inside", numbers=True, note=(
           "The sector search's cumulative and daily pair, behind the title Single Plane "
           "Octagonal Sector Search Model. Cumulative rises to roughly two thirds by day 20, "
           "the lowest ceiling of the four patterns the paper tests."))

# ---------------------------------------------------------------- 3.7: the comparisons
figure(24, 1, "line",
       cap(24, "Figure 21: Direct", "Model Comparison."), "Figure N:", none_mention(),
       "model", SEC_ONE, legend="inside", numbers=True, note=(
           "Four cumulative curves on one pair of axes, titled Single Plane Model Comparison - "
           "Cumulative Success Probability: the simple square, spiral square and rectangular "
           "searches run tightly together and the octagonal sector search sits clearly below "
           "them. Legend inside, one entry per model."))
figure(25, 1, "line",
       cap(25, "Figure 22: Comparison", "over 20 Days."), "Figure N:",
       cited(25, 25, ["Figure 22"], 1, "This is shown below in Figure 22:"),
       "model", SEC_FIVE, legend="inside", numbers=True, note=(
           "The same four models with five search planes instead of one: the three square-ish "
           "patterns saturate near one within about three days and the octagonal sector again "
           "lags. Because the curves pile up at the top of the axis, the legend prints over them "
           "inside the plot rather than beside it."))
figure(26, 1, "surface-or-3D",
       cap(26, "Figure 23: Initial", "More Likely."), "Figure N:", none_mention(),
       "model", SEC_STALL, numbers=True, three_d="surface-mesh", note=(
           "The prior probability surface rebuilt for the stall case, titled Stall Likely Prior "
           "Probability Density: the same axis frame as Figure 3 but the mass is no longer a "
           "single centred mound. This is the only raster in the paper whose title names the "
           "scenario rather than the search."))
figure(26, 2, "line",
       cap(26, "Figure 24: Model Comparison", "Stall Scenario."), "Figure N:", none_mention(),
       "model", SEC_STALL, legend="inside", numbers=True, note=(
           "The four models run against the stall-case prior, behind the title Stall Likely "
           "Model Comparison - Cumulative Success Probability. Same four curves and same "
           "legend-in-plot arrangement as Figure 21."))
figure(27, 1, "line",
       "(a) Comparison of Search Patterns for Single Small Plane over 20 Days.", "none",
       none_mention(), "model", SEC_SHORT, legend="inside", numbers=True,
       source="typed-from-crop", note=(
           "The left panel of the paper's unnumbered comparison figure: the four search models "
           "for a short-range aircraft, cumulative success over the full 20 days, y axis 0 to "
           "0.2. The caption is typed from the crop because the text layer interleaves the two "
           "panels' captions line by line, so no contiguous printed string spans this one."))
figure(27, 2, "line",
       "(b) Comparison of Search Patterns for Single Small Plane over 5 Days.", "none",
       none_mention(), "model", SEC_SHORT, legend="inside", numbers=True,
       source="typed-from-crop", note=(
           "The right panel of the same figure, the first five days zoomed: the same four "
           "curves with the y axis rescaled to 0 to 0.05, which is what the prose promises - "
           "20 days and then the same zoomed to the first five. Typed from the crop for the "
           "same reason as (a)."))
figure(28, 1, "line",
       cap(28, "Figure 26: Comparison", "Different Paths."), "Figure N:", none_mention(),
       "model", SEC_PATHS, legend="inside", numbers=True, note=(
           "Two cumulative curves comparing two square paths against one square and one "
           "octagonal path, titled Two Plane Model Comparison - Same vs. Different Patterns. "
           "The pair separates late, after about eight days, and the two labels are the whole "
           "legend."))
figure(30, 1, "line",
       cap(30, "Figure 27: Comparison", "Effectiveness Parameters."), "Figure N:",
       none_mention(), "model", SEC_EFF, legend="inside", numbers=True, note=(
           "Unit effectiveness against double effectiveness on a square search, two curves "
           "over 20 days under the title Effectiveness Model Comparison - Cumulative Success "
           "Probability. Doubling the parameter lifts the cumulative curve away from one much "
           "earlier in the run."))
figure(31, 1, "line",
       cap(31, "Figure 28: Comparison", "Missing Aircraft."), "Figure N:", none_mention(),
       "model", SEC_VARY, legend="inside", numbers=True, note=(
           "A 747 crash against a Cessna 172 crash, two cumulative curves under the title "
           "Missing Aircraft Type Comparison. The section this figure belongs to prints no "
           "heading of its own - the run of 3.7.x stops at 3.7.6 on p29 and 4 Final Remarks "
           "opens on p32 - so the row's section path stops at 3.7 Model Variation and "
           "Comparison."))

# ---------------------------------------------------------------- rules and note
RULES: list[str] = [
    "Families are read off the page, not off the captions, and the captions repeat: thirteen "
    "rows are line plots, seven are schematic drawings, six are 3-D surfaces, one is a contour "
    "plot and three are composites. Fourteen captions print the same two sentences - "
    "'Probability Density Distribution after a 5-day search' four times and 'Cumulative "
    "Probability of Success after a 20-day search' five times - so a caption alone never fixes "
    "a family here [geometry.family].",
    "The 3-D surfaces are all one kind: six mesh surfaces exported from MATLAB, each drawn over "
    "an x/y frame in miles with a plain Probability axis and none carrying a colour bar, so "
    "'surface-mesh' is the whole class rather than a per-figure judgement [geometry.three_d].",
    "Three rows hold two panels of different families - a filled contour beside a geometric "
    "search-path drawing - and all three are laid out as a row of two: Figures 8, 14 and 18. "
    "The rest of the multi-panel work is single-family and keeps its family with a panel count "
    "of one, because each panel is its own caption or its own figure [geometry.panel_layout].",
    "Every figure caption prints BELOW its artwork, in all thirty captioned rows, and no "
    "exhibit in this paper is a table - the only ruled grid is the cover's registration block, "
    "which is refused. So the caption side is uniform where the families are not "
    "[caption.position].",
    "Numbering is not uniform. Twenty-six rows carry the printed form 'Figure N:' with the "
    "colon, but four rows carry subcaptions only: the pair on p5 prints '(a) Visual definition "
    "of theta.' and '(b) Visual definition of phi.', and the pair on p27 prints '(a)' and '(b) "
    "Comparison of Search Patterns for Single Small Plane...'. Neither pair prints its own "
    "figure number anywhere on the page, so both are recorded with numbering 'none' "
    "[caption.numbering].",
    "The printed numbers skip one. Captions run Figure 2 to Figure 24 and then Figure 26 to "
    "Figure 28, with no 'Figure 25' printed anywhere in the paper, and the p27 pair under 3.7.4 "
    "is the only exhibit the missing number can belong to - two panels of the same comparison "
    "at full and zoomed scale, which is what that section's prose introduces. The census counts "
    "them as two rows and says so here rather than inventing a caption [caption.numbering].",
    "Only six printed figures are ever named by number in prose: Figure 2 on p5, Figure 3 on "
    "p7, Figure 6 on p11, Figure 14 on p19 and Figure 22 on p25, plus one lower-case 'from "
    "figure 8' on p15 which is recorded as it prints. Everything else is pointed at deictically "
    "- 'shown below', 'the following figure', 'Consider now the following figure' - so "
    "twenty-four rows carry an empty mention block [mention.count].",
    "Two exhibits lead their section by a page: Figure 2's caption prints on p6 while its "
    "citation prints on p5, and Figure 3's caption prints on p8 while its citation prints on p7 "
    "- the prose introducing the contour plot on p7 is the only place Figure 3 is named "
    "[mention.lead_pages].",
    "Section paths come from the printed headings and not from the ctx index, which was fooled "
    "four times on this paper: '0.8 Rectangular Model' and '0.9 Rectangular Model' are legend "
    "lines from the comparison plots, '0.18 Octagonal Sector Model Octagonal Sector Model' is "
    "the axis tick and legend of Figure 25, and '747 Crash' is a legend entry on p31. All four "
    "are replaced by the real chain here [place.section_path].",
    "Figure 28's section has no heading at all. The 3.7.x run ends with 3.7.6 The Effectiveness "
    "Parameter on p29 and 4 Final Remarks opens on p32, and p31 carries only the plot and its "
    "caption, so the row stops at '3.7 Model Variation and Comparison' instead of borrowing the "
    "preceding subsection's name [place.section_path].",
    "Captions were copied out of the layer with their curly quotation marks intact - Figures 13, "
    "14, 17 and 18 all quote a search pattern in quotes - and the two p5 subcaptions carry real "
    "Greek letters, theta and phi, not the private-use glyphs that spoil the Greek in the body "
    "prose of this paper [caption.verbatim].",
    "Area does nothing to separate exhibits here. The six surfaces are the biggest boxes on "
    "their pages - the p8 one at 0.245 of the page and the p16 and p20 ones at 0.243 and 0.249 "
    "- while the two refusals are 0.069 and 0.136, so the cover block and the letterhead sit "
    "inside the same size band as real exhibits and only the crop could tell them apart "
    "[place.area_frac].",
]

NOTE = (
    "Paper 75, Team 32879, a 2015 search-theory paper about finding a missing aircraft over "
    "open ocean. Thirty-two measured regions over twenty-four of the thirty-five pages: thirty "
    "figure rows and two refusals, nothing left unaccounted for and nothing unresolved. The "
    "paper prints no tables at all, so this is the lane's first census entry in a while with an "
    "empty table list beside a full figure list.\n\n"
    "What the exhibits are. Thirteen line plots carry the model comparisons: the prior and "
    "posterior overlay of Figure 6, the cumulative-and-daily pair printed five times over "
    "(Figures 10, 12, 16, 20 and 25), and the seven multi-model comparisons from Figure 21 to "
    "Figure 28. Six 3-D mesh surfaces carry the probability densities before and after "
    "searching. Seven drawings carry the geometry the paper argues with: the glide-angle and "
    "bearing sketches of Figure 1, the glide-slope triangle, the corridor figures, the spiral "
    "and the octagonal sector. One contour map, Figure 7, carries the mass distribution itself, "
    "and three composites - Figures 8, 14 and 18 - pair a contour panel with a drawing of the "
    "search that produced it.\n\n"
    "The two refusals are both page furniture that the measurer could not tell from artwork: "
    "the cover's 'For office use only' registration block, and the letterhead of the closing "
    "letter to commercial airlines. Neither carries a number or a caption.\n\n"
    "What the paper gets wrong, and what the census therefore has to declare rather than "
    "repair. The printed figure numbers run 2 to 24 and then 26 to 28: there is no Figure 25 "
    "anywhere, and the only exhibit that can be it is the unnumbered (a)/(b) pair on p27. "
    "Figure 1 is in the same state - two separately captioned panels, cited in prose as "
    "'Figures 1a & 1b' and never printed with a number of its own. Figure 28's subsection has "
    "no heading, so its section path stops one level short. And the paper's own plot titles "
    "disagree with its captions in small ways that a reader would trip over: Figure 16's title "
    "prints 'Square Spriral Search Model', Figure 21's caption says Direct Model Comparison "
    "while the plot is titled Single Plane Model Comparison, and the p27 pair is titled Small "
    "Plane Model Comparison although the aircraft under discussion is a V-22 Osprey.\n\n"
    "Two reading difficulties are worth recording because they cost time. Fourteen raster "
    "figures are MATLAB exports whose axis text is part of the bitmap, so it reads only from a "
    "crop; the thirteen vector plots by contrast have their axis and legend text in the layer, "
    "with the y-axis label always printed mirrored - 'ytilibaborP' rather than 'Probability' - "
    "which is why the geometry dump for those pages looks like noise. And the text layer "
    "interleaves the two p27 captions line by line, so neither can be quoted as a contiguous "
    "string; both are typed from the crop instead.\n\n"
    "Citation practice is thin: six figures are named by number in the whole paper, and the "
    "rest are introduced by a deictic sentence immediately above the art. That is not a defect "
    "in the paper so much as a property of its genre, but it does mean the mention column here "
    "is mostly empty and should not be read as a measurement of how often the figures are used."
)

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT.get("layout_sha256") or LAYOUT.get("sha256", ""),
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc75-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
