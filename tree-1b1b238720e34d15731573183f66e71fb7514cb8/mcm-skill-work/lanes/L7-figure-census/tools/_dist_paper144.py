"""Hand pass for P-A-2018-76271-27d535ab ("Wave Goodbye to Poor Reception", HF skywave).

31 pages, 31 measured regions: 18 captioned figures, 8 captioned tables and five pasted
LaTeX display-equation images that the region detector reads as artwork.

What the record has to say out loud:

1. Caption side is decided by exhibit kind and never varies: all 18 figure captions print
   BELOW their artwork, all 8 table captions print ABOVE their grid.
2. The paper has exactly one table template - a full grid with verticals at every cell
   boundary - applied eight times, unshaded, unmerged, no diagonal header, no note line.
3. Five box plots make box-and-whisker the most-used family, and three of them are the same
   unfilled blue box with a red median bar and black dashed whiskers.
4. Three-dimensional drawing is confined to the terrain model: Figures 2, 6 and 7 are all
   point-mesh surfaces with quiver arrows and an inside legend.
5. Colour bars appear only where the exhibit encodes a continuous field - the two
   electron-density disks of Figure 8 and the three cell-grids 12-14.
6. The appendix is a plate section: all 14 appendix figures are announced from the body,
   10 to 15 pages before they print, and no appendix page cites another.
7. Figures 3 and 4 are captured basemaps with a map pin and one arrow - never cited, and
   the only two figures whose subject is a place rather than a simulation.
8. Table citations are broken: twice the prose prints "the numerical values are shown in 1",
   so two tables are announced without a number and two more are never announced at all.
9. Figure 11's left panel plots calm against turbulent water while its caption names only
   terrain, so half of the exhibit answers a question the caption does not ask.

Usage: python -I tools/_dist_paper144.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2018-76271-27d535ab"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    "f1": (9, [102.7, 312.2, 513.1, 578.5]),
    "f2": (12, [128.2, 171.5, 500.4, 356.2]),
    "t1": (15, [186.7, 645.6, 425.8, 693.6]),
    "t2": (16, [92.1, 164.3, 542.9, 212.3]),
    "t3": (16, [192.9, 416.3, 419.7, 464.2]),
    "t4": (16, [92.1, 564.6, 530.3, 612.6]),
    "f3": (17, [91.8, 369.0, 297.6, 501.0]),
    "f4": (17, [314.5, 359.9, 518.0, 508.4]),
    "t5": (17, [95.1, 611.0, 517.6, 659.0]),
    "t6": (19, [139.6, 176.7, 473.0, 251.7]),
    "t7": (19, [139.6, 516.9, 473.0, 578.4]),
    "t8": (20, [139.6, 259.6, 473.0, 334.7]),
    "f5": (25, [178.4, 171.8, 430.0, 307.8]),
    "f6": (25, [159.6, 479.4, 462.4, 640.3]),
    "f7": (26, [142.1, 111.8, 476.3, 295.1]),
    "f8": (26, [147.6, 394.4, 487.3, 576.0]),
    "f9": (27, [125.9, 91.0, 487.4, 288.1]),
    "f10": (27, [127.9, 374.6, 482.5, 569.6]),
    "f11": (28, [128.2, 91.0, 482.5, 286.0]),
    "f12": (28, [125.4, 374.5, 497.8, 571.2]),
    "f13": (29, [125.4, 91.0, 503.4, 287.5]),
    "f14": (29, [184.4, 349.7, 428.0, 583.4]),
    "f15": (30, [119.6, 126.0, 482.5, 318.6]),
    "f16": (30, [119.6, 414.0, 482.5, 610.7]),
    "f17": (31, [119.6, 123.5, 482.5, 320.2]),
    "f18": (31, [127.9, 407.0, 482.5, 602.4]),
}

EXCLUDED = {
    "p10 equations (3) and (4)": (10, [108.7, 109.0, 571.6, 199.9]),
    "p10 equations (5) to (8)": (10, [85.0, 312.2, 551.4, 458.3]),
    "p10 equations (9) and (10)": (10, [108.7, 512.4, 549.7, 620.8]),
    "p11 equations (11) to (15)": (11, [85.0, 51.0, 547.9, 395.2]),
    "p13 equation (18)": (13, [85.0, 267.1, 532.9, 313.1]),
}

for _name, (_p, _b) in {**B, **EXCLUDED}.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 31, len(MEASURED)


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    w, h = DIMS[page]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < h / 3 else ("middle" if mid < 2 * h / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 1,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": False,
    }


def cap(v: str, numbering: str = "Figure N.", *, position: str = "below",
        units: bool = False, concludes: bool = False) -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)) if v else 0,
        "units": units,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": concludes,
        "voice": "none",
        "position": position,
    }


def mention(page: int, *, first: int | None, style: list[str], lead: str = "",
            pattern: str = "none", trail: str = "", read: int = 0) -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": 0 if first is None else 1,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def geo(family: str, *, legend: str = "none", numbers: bool = True,
        colorbar: bool = False, three_d: str = "no", panels: int = 1,
        layout: str = "1", shared: bool = False) -> dict:
    return {
        "family": family,
        "panel_count": panels,
        "panel_layout": layout,
        "shared_axes": shared,
        "legend": legend,
        "colorbar": colorbar,
        "three_d": three_d,
        "printed_numbers": numbers,
        "data_labels": False,
    }


def figure(key: str, family: str, caption: dict, men: dict, geom: dict, *,
           path: list[str], kind: str, note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "family": family,
        "confidence": "high",
        "panel_count": geom["panel_count"],
        "is_panel_of": "",
        "caption_verbatim": caption["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }


def grid(rows: int, cols: int, *, header: int = 1, numeric: int = 0, txt: int = 1,
         width: str = "full", units_in_header: bool = True) -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": "boxed",
        "zebra": False,
        "merged_cells": False,
        "diagonal_header": False,
        "units_in_header": units_in_header,
        "decimal_aligned": False,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": False,
        "note_sentence": "",
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": caption["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "table": g,
    }


IV = "IV. Model Development"
A_MC = "A. Model Construction"
P_ION = [IV, A_MC, "1. Propagation and Ionosphere Interaction"]
G_ION = [IV, A_MC, "2. Ground Interaction"]
VI = "VI. Results"
P_I = [VI, "B. Part I"]
P_II = [VI, "C. Part II"]
P_III = [VI, "E. Part III"]
VII = "VII. Sensitivity Analysis"
AEPS = "A. Explore Parameter Space"
TURB = [VII, AEPS, "2. Wave Turbulence"]
POWER = [VII, AEPS, "3. Transmit Power"]
DENS = [VII, AEPS, "4. Ionosphere Density"]
APX = "X. Appendix"
A_TRAJ = [APX, "Diagram of Calculated Ionosphere Trajectory"]
A_TERR = [APX, "Example Terrain with Vectors"]
A_VALID = [APX, "Model Validation: Comparing Absorbed and Escaped Signals to Modeled "
                 "Electron Density"]
A_REM = [APX, "Signal Remaining After First Bounce for Water (Part I) and Land (Part I)"]
A_SWEEP = [APX, "Results of Frequency and Elevation Angle Sweep Sensitivity Analysis"]
A_TURB = [APX, "Results of Ocean Turbulence Sensitivity Analysis"]
A_PWR = [APX, "Results of Transmit Power Sensitivity Analysis"]
A_SOL = [APX, "Results of Ionosphere Electron Density Sensitivity Analysis"]
A_GEO = [APX, "Results from Geographic Locations in Part III"]

FIGURES = [
    figure("f1", "flowchart-or-schematic",
           cap("Figure 1. Diagram of Skywave Interaction with Ionosphere"),
           mention(9, first=9, style=["Figure 1"], pattern="as-shown-in",
                   lead="The equations in this section are based on a curved radio wave "
                        "trajectory, as shown in our diagram, Figure 1.",
                   trail="This trajectory matches Figure 1 well."),
           geo("flowchart-or-schematic", numbers=False),
           path=P_ION, kind="model",
           note="the paper's opening exhibit and its only free-hand line drawing: a side "
                "elevation of one hop with the transmitter at the left and the receiver at the "
                "right, a dotted band standing in for the ionosphere, the curved ray labelled S "
                "inside a bisector construction, and the symbolic labels D1, D2, h0, hr, theta, "
                "theta-prime and P_proj. No axes, no ticks, no scale; the two node markers "
                "(TRANSMITTER, RECEIVER) are plain words rather than symbols, and the only "
                "arrowheads anywhere are the two on the reflected ray"),
    figure("f2", "surface-or-3D",
           cap("Figure 2. Incident and Reflected Rays Off Random Turbulent Waves"),
           mention(12, first=12, style=["Figure 2"], pattern="direct",
                   lead="Figure 2 (and Figure 7 in the Appendix) are examples of turbulent and "
                        "calm random waves, respectively."),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=G_ION, kind="model",
           note="the first of three terrain surfaces: a MATLAB patch of turbulent sea drawn as a "
                "coloured mesh with a five-entry inside legend at upper right (Water surface, "
                "Local reflected, Local incident, Mean reflected, Mean incident). Axes X distance "
                "(m), Y distance (m) and Height (m), each labelled separately and all three "
                "printed; no colour scale, so the cyan-to-yellow fill that encodes height has no "
                "key. The local-vector glyphs are dense enough at print size to read as texture "
                "rather than arrows"),
    figure("f3", "map-or-plan-view",
           cap("Figure 3. Honduras Trajectory"),
           mention(17, first=None, style=[]),
           geo("map-or-plan-view", numbers=False),
           path=P_III, kind="result",
           note="left half of the p17 pair and the paper's only exhibit drawn on a captured web "
                "basemap: a colour tile of Central America carrying place labels (United States, "
                "Mexico, Gulf of Mexico, Nicaragua, and the state abbreviations CA through TX) "
                "plus one red map pin on the Nicaraguan coast and a single thick black arrow "
                "running west across Honduras. No axes, no ticks, no scale bar and no legend, so "
                "the distance the arrow covers cannot be read off the exhibit at all. Never "
                "cited: the sentence that introduces the pair names neither figure"),
    figure("f4", "map-or-plan-view",
           cap("Figure 4. L.A. Trajectory"),
           mention(17, first=None, style=[]),
           geo("map-or-plan-view", numbers=False),
           path=P_III, kind="result",
           note="the California half of the same pair: a captured basemap of the southern "
                "California coast labelled San Francisco, CALIFORNIA, NEVADA and Las Vegas, one "
                "red pin near Los Angeles and one black arrow pointing south-west into the "
                "Pacific. Geography differs from Figure 3 in every way that matters - a "
                "north-up coastal frame against a gulf frame, a different zoom, a different "
                "label set - so the two panels of one comparison do not share a basemap, a "
                "scale or an orientation"),
    figure("f5", "line",
           cap("Figure 5. Example Ionosphere Signal Trajectory"),
           mention(25, first=10, style=["Figure 5"], pattern="as-shown-in",
                   lead="See Figure 5 in the Appendix for an example of a trajectory calculated "
                        "by our model."),
           geo("line", legend="inside"),
           path=A_TRAJ, kind="appendix",
           note="the appendix's first plate and the only exhibit that draws the virtual-path "
                "construction: a solid red triangular ray paired with a green dashed one of the "
                "same shape peaking higher, a black dashed undulating line for the layer "
                "boundary and a thin flat blue band along the baseline, keyed by a three-entry "
                "inside legend reading True Path, Virtual Path and Ionosphere Lower Boundary. "
                "Axes x (km) and y (km), so this is the one appendix plot whose units are "
                "physical distance rather than a count"),
    figure("f6", "surface-or-3D",
           cap("Figure 6. Incident, Normal, and Reflected Rays Off Random Mountainous Terrain"),
           mention(25, first=13, style=["Figure 6"], pattern="as-shown-in",
                   lead="The example terrain plots, including Figure 2 and Figure 7 and 6 in the "
                        "Appendix"),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=A_TERR, kind="appendix",
           note="the land half of the terrain pair: a brown dotted height field of about 14 m by "
                "14 m with a ridge across the middle, a blue-violet normal arrow at every mesh "
                "point, and two long mean rays drawn as a yellow up-left arrow and a red "
                "down-right arrow. Six-entry inside legend (Land surface, Local reflected, Local "
                "incident, Local normal, Mean reflected, Mean incident) - one entry more than "
                "its calm-water twin on p26, because only the land plot keeps the local normals"),
    figure("f7", "surface-or-3D",
           cap("Figure 7. Incident and Reflected Rays Off Random Calm Waves"),
           mention(26, first=12, style=["Figure 7"], pattern="parenthetical",
                   lead="Figure 2 (and Figure 7 in the Appendix)"),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=A_TERR, kind="appendix",
           note="the calm-water twin of Figure 6 and the only exhibit whose y axis runs "
                "backwards (15 at the left of the axis to -15 at the right), a quirk the surface "
                "inherits from the MATLAB view command. Five-entry inside legend with the local "
                "normals dropped, matching the p25 prose that says the water plot omits them. "
                "Announced from p12, fourteen pages before it prints"),
    figure("f8", "map-or-plan-view",
           cap("Figure 8. Oceanic Bounce Locations Plotted Over Ionosphere Electron Density"),
           mention(26, first=15, style=["Figures 8 and 9"], pattern="as-shown-in",
                   lead="as shown in Figures 8 and 9 in the Appendix",
                   trail="The former plots the latitude and longitude of modeled oceanic "
                         "bounces"),
           geo("map-or-plan-view", legend="below", colorbar=True, panels=2,
               layout="2 in a row"),
           path=A_VALID, kind="appendix",
           note="the paper's only two-panel map exhibit: two filled circular disks of ionosphere "
                "electron density in a black-red-yellow-hot ramp, each with its own colour bar "
                "labelled 'Electron Density m^-3' scaled by 10^12, with a cloud of black bounce "
                "dots laid over each. A one-entry legend ('Oceanic Bounce Locations') sits under "
                "the left disk only, so the right disk is keyed by proximity. Neither disk "
                "carries a latitude or longitude axis - the geography is only implied by the "
                "dot pattern"),
    figure("f9", "line",
           cap("Figure 9. Probability of Escaping to Space Versus Ionosphere Electron Density"),
           mention(27, first=15, style=["Figures 8 and 9"], pattern="as-shown-in",
                   lead="as shown in Figures 8 and 9 in the Appendix",
                   trail="The latter plot shows the probability of radio waves bursting through "
                         "the ionosphere"),
           geo("line"),
           path=A_VALID, kind="appendix",
           note="a single blue line against peak electron density, flat at 1.0, then a cliff down "
                "to about 0.4 and a noisy band between 0.2 and 0.35, then a straight climb back "
                "to 1.0 at the right edge. No legend, no markers, no frame beyond the two axes. "
                "The x multiplier prints as 10^12 at the lower right, so the tick values 0 to 2.5 "
                "have to be rescaled by the reader, and the two flat ends mean the curve says "
                "nothing at the extremes of its own axis"),
    figure("f10", "box-or-violin",
           cap("Figure 10. Average Power Directly After First Bounce for Calm and Turbulent "
               "Water"),
           mention(27, first=16, style=["Figure 10"], pattern="as-shown-in",
                   lead="The distribution of signal strength after the first bounce is shown in "
                        "Figure 10 in the Appendix"),
           geo("box-or-violin", panels=2, layout="2 boxes in a row", shared=True),
           path=A_REM, kind="appendix",
           note="two side-by-side box-and-whisker glyphs - unfilled blue boxes, red median bar, "
                "black dashed whiskers with caps - over the categorical axis 'Calm Water', "
                "'Turbulent Water' under the title 'Reflection Conditions of First Bounce', "
                "y axis 'Signal Power (dB)' from 15 to 35. The calm box sits about 24.5 to 28 dB "
                "with whiskers to 31.5 while the turbulent box sits about 22.5 to 27.5 with "
                "whiskers down to 15.5, so the two boxes overlap over most of their length and "
                "the caption's 'average' is the only thing separating them"),
    figure("f11", "box-or-violin",
           cap("Figure 11. Average Power Directly After First Bounce for Smooth and Rugged "
               "Terrain"),
           mention(28, first=16, style=["Figure 11"], pattern="as-shown-in",
                   lead="The distribution of signal strength after the first bounce is shown in "
                        "Figure 11 in the Appendix"),
           geo("box-or-violin", panels=2, layout="2 boxes in a row", shared=True),
           path=A_REM, kind="appendix",
           note="the same box template twice on one plate: the left panel plots Calm Water "
                "against Turbulent Water and the right panel plots Flat Land against Rugged "
                "Terrain, both over 'Signal Power (dB)'. The caption names only terrain, so the "
                "left half repeats Figure 10's comparison inside an exhibit whose title says "
                "nothing about water, and the reader who wants the terrain numbers has to know "
                "that only the right panel answers the question"),
    figure("f12", "heatmap-or-contour",
           cap("Figure 12. Average Number of Bounces"),
           mention(28, first=18, style=["Figures 12 and 13"], pattern="as-shown-in",
                   lead="as is seen in Figures 12 and 13 in the Appendix"),
           geo("heatmap-or-contour", colorbar=True),
           path=A_SWEEP, kind="appendix",
           note="the first of three cell grids over the same axes - frequency 4 to 20 MHz by "
                "elevation angle 0 to 50 degrees in 5-degree steps - with cells that carry no "
                "values and a right-hand colour bar titled 'Average Number of Bounces' running 0 "
                "to 1.6 in 0.2 steps. Most of the field prints black, meaning values below the "
                "lowest tick, and the live region is a staircase band widening to the left, so "
                "the exhibit is legible only as a shape and not as a table of numbers"),
    figure("f13", "heatmap-or-contour",
           cap("Figure 13. Net Arc Length on the Earth from the Starting Point a.k.a. Total "
               "Distance in km", units=True),
           mention(29, first=18, style=["Figures 12 and 13"], pattern="as-shown-in",
                   lead="Pairs with low frequencies and high angles tend to bounce more, but "
                        "travel a shorter overall distance, as is seen in Figures 12 and 13"),
           geo("heatmap-or-contour", colorbar=True),
           path=A_SWEEP, kind="appendix",
           note="the same cell grid as Figure 12 with the same axes and the same masked black "
                "background, recoloured by distance: the colour bar reads 'Average Distance From "
                "Start (km)' from 0 to 2500. The caption is the only one in the paper that "
                "carries two names for one quantity ('Net Arc Length on the Earth from the "
                "Starting Point a.k.a. Total Distance in km') and it also prints a unit, which no "
                "other figure caption does"),
    figure("f14", "heatmap-or-contour",
           cap("Figure 14. Percentage of Signals that are Absorbed by Loss as Opposed to "
               "Escaping to Space"),
           mention(29, first=18, style=["Figure 14"], pattern="as-shown-in",
                   lead="This can be observed in Figure 14 in the Appendix."),
           geo("heatmap-or-contour", colorbar=True),
           path=A_SWEEP, kind="appendix",
           note="the third cell grid, and the one that breaks the family's axis convention: it "
                "steps elevation by 10 degrees rather than 5 and frequency by 5 MHz rather than "
                "2, so its cells do not line up with Figures 12 and 13 even though the three "
                "plates sit in one column. No black mask here - the whole field carries a value - "
                "with the colour bar reading 'Percentage of Signals Destroyed by Loss' from 0 to "
                "90. The bar's label uses the word 'Destroyed' where the caption uses 'Absorbed'"),
    figure("f15", "box-or-violin",
           cap("Figure 15. Total Distance Travelled Related to Ocean Turbulence. Calm "
               "distances are sta- tistically different than both turbulent oceans.",
               concludes=True),
           mention(30, first=19, style=["Figure 15"], pattern="as-shown-in",
                   lead="A box-plot of these data are found in Figure 15 in the Appendix."),
           geo("box-or-violin"),
           path=A_TURB, kind="appendix",
           note="three boxes over Calm, Turbulent and Super Turbulent water, y axis 'Total "
                "Distance Traveled (km)' from 600 to 2600, x title 'Ocean Conditions'. The calm "
                "box runs about 1000 to 1900 km while both turbulent boxes are short and low at "
                "about 900 to 950 km median, so the exhibit shows the collapse the prose reports "
                "and the two turbulent cases are visually indistinguishable. This is the one "
                "caption in the paper that carries a second, concluding sentence"),
    figure("f16", "box-or-violin",
           cap("Figure 16. Total Distance Travelled Related to Initial Power of Signal"),
           mention(30, first=19, style=["Figure 16"], pattern="as-shown-in",
                   lead="A box plot of this data can be found in Figure 16 in the Appendix."),
           geo("box-or-violin"),
           path=A_PWR, kind="appendix",
           note="three boxes over 180, 190 and 210 dB, y axis 'Total Distance Traveled (km)' from "
                "500 to 6000 - a range five times wider than Figure 15 on the same 600 to 2600 "
                "data - so the three medians that sit near 1600 to 1800 km look flat while the "
                "210 dB box spreads to 3200 and its whiskers reach 5400. Same template as Figure "
                "15, different axis crowding, and the reader who compares the two plates sees a "
                "different story from the same numbers"),
    figure("f17", "box-or-violin",
           cap("Figure 17. Total Distance Travelled Depending on Solar Activity"),
           mention(31, first=20, style=["Figure 17"], pattern="as-shown-in",
                   lead="See Figure 17 in the Appendix for a box-plot of these data."),
           geo("box-or-violin"),
           path=A_SOL, kind="appendix",
           note="three boxes over the three NASA datasets, x title 'Dataset Used (Solar "
                "Activity)' and categories 2009 (low), 2003 (medium), 2000 (high); y axis again "
                "'Total Distance Traveled (km)'. The medians sit within a few tens of kilometres "
                "of one another and every box spans roughly 1000 to 2000 km, so the exhibit on "
                "which the paper's solar-activity conclusion rests is the least separated of the "
                "three box plots"),
    figure("f18", "scatter",
           cap("Figure 18. Dispersion of Radio Signal Originating from Honduras"),
           mention(31, first=18, style=["Figure 18"], pattern="as-shown-in",
                   lead="As show in Figure 18 in the Appendix"),
           geo("scatter", legend="inside"),
           path=A_GEO, kind="appendix",
           note="the paper's only scatter: three marker classes keyed by a boxed inside legend at "
                "upper right (Starting Point, First Bounce, Second Bounce) plotting latitude "
                "against longitude with only the left and bottom spines drawn. One black dot "
                "marks the origin, a tight red horizontal cluster the first bounces and a wide "
                "green oval the second bounces, which is the dispersion the caption claims. Marks "
                "print at two to three pixels and there is no density encoding, so the second-"
                "bounce cloud is a field of specks rather than a distribution"),
]

TABLES = [
    table("t1", cap("Table 1. Power After First Bounce by Varying Turbulence of Ocean",
                     "Table N.", position="above"),
          mention(15, first=16, style=["1"], pattern="as-shown-in",
                  lead="the numerical values are shown in 1."),
          grid(2, 3, numeric=2, txt=1, width="half"),
          path=P_I, kind="result",
          note="the paper's narrowest grid and the first of two 3-column power summaries: Mean "
               "(dB) and Std Power (dB) against Calm and Turbulent, six numbers in all, printed "
               "about 60 per cent of the text width and centred. Its only citation prints a page "
               "later as 'the numerical values are shown in 1' - the table number is missing, so "
               "the reference points at nothing"),
    table("t2", cap("Table 2. Distance of Signal by Varying Turbulence of Water", "Table N.",
                     position="above"),
          mention(16, first=None, style=[]),
          grid(2, 5, numeric=4, txt=1),
          path=P_I, kind="result",
          note="the five-column distance twin of Table 1: Av Distance (km), Std Distance (km), Av "
               "Bounces and Std Bounces against the same two water states, full text width and "
               "about 5 per cent wider than the column. The only table in the paper that no "
               "sentence names at all, and it is the table that carries the numbers the prose "
               "quotes for the calm/turbulent distance claim"),
    table("t3", cap("Table 3. Power After First Bounce by Varying Ruggedness of Terrain",
                     "Table N.", position="above"),
          mention(16, first=16, style=["1"], pattern="as-shown-in",
                  lead="the numerical values are shown in 1."),
          grid(2, 3, numeric=2, txt=1, width="half"),
          path=P_II, kind="result",
          note="Table 1's template rerun on land: same two headers, Smooth and Rugged in the stub, "
               "half width, centred. Announced by the second 'shown in 1' of the same page, so two "
               "different tables are cited by the same missing number within twenty lines"),
    table("t4", cap("Table 4. Distance of Signal by Varying Ruggedness of Terrain", "Table N.",
                     position="above"),
          mention(16, first=None, style=[]),
          grid(2, 5, numeric=4, txt=1),
          path=P_II, kind="result",
          note="Table 2's five-column template rerun on land: distances and bounce counts for "
               "Smooth against Rugged, full width. Uncited, and the last table printed on a page "
               "that carries four grids and no table citation"),
    table("t5", cap("Table 5. Distance for Signals Aimed at a Ship in Turbulent Seas (Measured "
                     "in km)", "Table N.", position="above", units=True),
          mention(17, first=None, style=[]),
          grid(2, 5, numeric=4, txt=1),
          path=P_III, kind="result",
          note="the only grid that puts its unit in the caption instead of the header or the "
               "stub, and the only one with empty cells: the L.A. row prints dashes under both "
               "second-bounce columns because that signal never bounces twice. Two locations "
               "against four bounce-distance columns, full width. Uncited - the p18 prose quotes "
               "its first-bounce range but names Figure 18 instead of the table"),
    table("t6", cap("Table 6. Effects of Ocean Turbulence on Distance Traveled", "Table N.",
                     position="above"),
          mention(19, first=18, style=["Table 6"], pattern="direct",
                  lead="Table 6 contains the resulting values from the simulation as the "
                       "turbulence is varied."),
          grid(2, 4, numeric=3, txt=1, width="full"),
          path=TURB, kind="sensitivity",
          note="the first of three 4-column grids that are one template: a stub column of two "
               "metric rows (Mean (km), Standard Deviation (km)) against three conditions, "
               "integers only, about 80 per cent of the text width. The header cell 'Super "
               "Turbulent' wraps onto two printed lines inside a single header row, which is the "
               "paper's only wrapped header. Announced a page before it prints, the one table in "
               "the paper whose citation arrives early"),
    table("t7", cap("Table 7. Effects of Transmitter Power on Distance Traveled", "Table N.",
                     position="above"),
          mention(19, first=19, style=["Table 7"], pattern="as-shown-in",
                  lead="Plugging these values into the simulation, we find statistics presented "
                       "in Table 7."),
          grid(2, 4, numeric=3, txt=1, width="full"),
          path=POWER, kind="sensitivity",
          note="Table 6's template with dBm columns (180, 190, 210) and the unit left in the "
               "column headers instead of the stub, which is the reverse of its sibling. Same "
               "two metric rows, same integers, same width. Cited on the sentence that "
               "introduces it"),
    table("t8", cap("Table 8. Effects of Solar Activity on Distance Traveled", "Table N.",
                     position="above"),
          mention(20, first=20, style=["Table 8"], pattern="as-shown-in",
                  lead="with overall statistics displayed in Table 8."),
          grid(2, 4, numeric=3, txt=1, width="full"),
          path=DENS, kind="sensitivity",
          note="the third run of the same 4-column template, with the solar datasets as columns "
               "(2009 Data (Low), 2003 Data (Medium), 2000 Data (High)) and the header cells "
               "wrapping onto two lines each. Its 2009 mean of 1587 km is the same row as Table "
               "6's Calm mean of 1445 km only by coincidence, and nothing in either caption says "
               "which baseline the other grid reuses"),
]

EXCLUDED_REGIONS = [
    {"page": p, "bbox": b, "reason": "not-an-exhibit", "note": n}
    for n, (p, b) in EXCLUDED.items()
]

RULES = [
    "Caption side is decided by exhibit kind and never varies within the kind: all eighteen "
    "figure captions print BELOW their artwork and all eight table captions print ABOVE their "
    "grid, although both kinds share one numbering grammar [caption.position].",
    "Numbering is 'Figure N.' and 'Table N.' with a period and a space on every one of the "
    "twenty-six exhibits, so the paper has exactly one label form and a reader can grep either "
    "kind with the same pattern [caption.numbering].",
    "The paper has one table template applied eight times: an outer box, a vertical rule at "
    "every cell boundary, a horizontal under the header and between the body rows. Not one "
    "grid is booktabs, and the absence is uniform across both problem parts and the "
    "sensitivity section [table.rule_style].",
    "No grid shades alternating rows, merges a cell, or prints a diagonal header - zero "
    "instances across all eight tables - so this paper is the cleanest counter-example in the "
    "lane to the idea that merged headers come with multi-condition grids [table.zebra].",
    "Numeric cells are centred, never decimal-aligned: the 2-decimal power grids and the "
    "5-decimal distance grids both centre, and Table 5's 1085.87 and 810.67 do not share a "
    "decimal column even though they sit one above the other [table.decimal_aligned].",
    "Units ride in the header or the stub on seven of the eight grids and appear in the "
    "caption exactly once, on Table 5 ('Measured in km'), which is also the only grid with "
    "empty cells - so the unit convention breaks where the data are incomplete [table."
    "units_in_header].",
    "Width is the only table variable: half width for the two 3-column power grids, full width "
    "for everything else - 80 per cent of the column for the three 4-column sensitivity grids "
    "and about 100 for the four 5-column distance grids - and no grid continues onto a second "
    "page [table.width].",
    "Colour bars appear only where the exhibit encodes a continuous field: the two electron-"
    "density disks of Figure 8 (each with its own bar) and the three cell grids 12 to 14. The "
    "five box plots and the three surfaces carry none, so colour encodes a quantity only on "
    "the four exhibits that plot a field over a parameter plane [geometry.colorbar].",
    "Three-dimensional drawing is confined to the terrain model: Figures 2, 6 and 7 are all "
    "point-mesh surfaces with a normal arrow at each mesh point, all carry an inside legend at "
    "upper right, and all print Height (m), X distance (m) and Y distance (m) - the only "
    "exhibits in the paper whose z axis is labelled [geometry.three_d].",
    "Box-and-whisker is the most-used family at five exhibits and all five use the same glyph "
    "- unfilled blue box, red median bar, black dashed whiskers with caps - so the paper runs "
    "one box template seven panels deep and spends its variety on the categorical axis instead "
    "[geometry.family].",
    "Every appendix figure is announced from the body, 10 to 15 pages before it prints, and not "
    "one appendix page cites another exhibit: the plate section is written as if the body "
    "sentences were its only reading instructions [mention.lead_pages].",
    "Five exhibits are never cited at all - the two captured basemaps (Figures 3 and 4) and "
    "three tables (2, 4 and 5) - so the uncited share is one ninth of the figures against "
    "three eighths of the tables, and the tables are the exhibits a reader is most likely to "
    "be sent to by a numberless sentence [mention.count].",
    "Table citations are broken rather than absent: twice on p16 the prose prints 'the "
    "numerical values are shown in 1', so Tables 1 and 3 are announced without a number and "
    "Table 2 and Table 4 are never announced at all [mention.style].",
    "One caption carries a second, concluding sentence (Figure 15's 'Calm distances are "
    "statistically different than both turbulent oceans'), and it is the only caption in the "
    "paper that states a result rather than naming a subject [caption.concludes].",
    "The captions are subject labels and nothing else: no figure caption names a unit, a "
    "variable value, a condition or a parameter except Figure 13's 'a.k.a. Total Distance in "
    "km', which is also the only caption with two names for one quantity [caption.verbatim].",
    "Figure 11 is the paper's one caption/panel mismatch: its caption names only terrain, while "
    "its left panel plots Calm Water against Turbulent Water - the comparison already made by "
    "Figure 10 - so half the exhibit answers a question its own title does not ask [caption."
    "verbatim].",
    "The two map exhibits are not model output at all but captured web basemaps with a pin and "
    "one arrow each, printed with no axes, no scale and no legend, so the distance a trajectory "
    "covers cannot be read off either exhibit [geometry.printed_numbers].",
]

NOTE = (
    "Thirty-one regions across 17 of 31 pages, and every region is an exhibit or a pasted "
    "equation: 18 captioned figures, 8 captioned tables, and five LaTeX display-equation "
    "blocks that the region detector measures as artwork (equations 3 to 10 on p10, 11 to 15 "
    "on p11, 18 on p13). The paper is a LaTeX report with MATLAB screenshots dropped in, so "
    "caption side is decided by exhibit kind and holds without exception - every figure "
    "caption below its artwork, every table caption above its grid - and both kinds share one "
    "numbering grammar, 'Figure N.' and 'Table N.', with no roman, no colon and no glued "
    "number. The tables are the tidiest part of the paper: eight grids, one template, an outer "
    "box with a vertical at every cell boundary, no zebra shading anywhere, no merged cell, no "
    "diagonal header, no note line, no continuation across a page, and centred rather than "
    "decimal-aligned figures. Only width varies, half for the three-column power grids and the "
    "four-column sensitivity grids, full for the five-column distance grids, and units move "
    "between header, stub and caption in a pattern that is consistent except on the one grid "
    "with empty cells. The figures split into three drawing tools. Five box plots share one "
    "glyph. Three terrain surfaces are the only three-dimensional exhibits and the only ones "
    "with a labelled z axis. Four exhibits carry colour bars - the two electron-density disks "
    "of Figure 8 and the three cell grids of Figures 12 to 14 - and nothing else does, so "
    "colour encodes a field only where the axes are a parameter plane. The three cell grids "
    "are worth flagging: 12 and 13 share axes to the tick, but 14 steps elevation by 10 "
    "degrees and frequency by 5 MHz, so the three plates in one column cannot be read across. "
    "Two figures are captured web basemaps with a map pin and a single arrow, printed without "
    "axes or scale, and those are the two the text never cites. The appendix is a plate "
    "section announced entirely from the body, 10 to 15 pages ahead, with no cross-reference "
    "inside it; the paper's own citations are the weakest part of the record, since the prose "
    "prints 'the numerical values are shown in 1' twice, leaving two tables announced without "
    "a number and two more never announced. One caption states a result (Figure 15) and one "
    "caption covers only half of its own exhibit (Figure 11, whose left panel plots water "
    "conditions the caption does not mention)."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": EXCLUDED_REGIONS,
    "rules": RULES,
    "note": NOTE,
}

DOC_ORDER = {
    "f1": 1, "f2": 2, "t1": 3, "t2": 4, "t3": 5, "t4": 6,
    "f3": 7, "f4": 8, "t5": 9, "t6": 10, "t7": 11, "t8": 12,
    "f5": 13, "f6": 14, "f7": 15, "f8": 16, "f9": 17, "f10": 18,
    "f11": 19, "f12": 20, "f13": 21, "f14": 22, "f15": 23, "f16": 24,
    "f17": 25, "f18": 26,
}

_order = sorted(DOC_ORDER, key=lambda k: (B[k][0], B[k][1][1], B[k][1][0]))
_seen_page: dict[int, int] = {}
for _key in _order:
    _page = B[_key][0]
    _seen_page[_page] = _seen_page.get(_page, 0) + 1
    for _e in FIGURES + TABLES:
        if _e["page"] == _page and _e["bbox"] == B[_key][1]:
            _e["place"]["doc_order"] = DOC_ORDER[_key]
            _e["place"]["page_order"] = _seen_page[_page]


def main() -> int:
    from collections import Counter

    exhibits = FIGURES + TABLES
    assert all(e["place"]["doc_order"] for e in exhibits), "unnumbered exhibit"
    print("figures", len(FIGURES), "tables", len(TABLES), "excluded", len(EXCLUDED_REGIONS))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in exhibits)))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in exhibits)))
    print("fam", dict(Counter(e["family"] for e in FIGURES)))
    print("cap.pos", dict(Counter(e["caption"]["position"] for e in exhibits)))
    print("cap.words", [e["caption"]["words"] for e in exhibits])
    print("men.lead", dict(Counter(e["mention"]["lead_pages"] for e in exhibits)))
    print("legend", dict(Counter(e["geometry"]["legend"] for e in FIGURES)))
    print("area", [e["place"]["area_frac"] for e in exhibits])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
