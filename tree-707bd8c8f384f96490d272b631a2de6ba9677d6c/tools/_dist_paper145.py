"""Hand pass for P-A-2018-77845-746864a6 ("MHPM and MSRSM", HF multi-hop propagation).

32 pages, 43 measured regions: 18 figure rows, 7 table rows and 18 exclusions.  The
exclusions are the paper's whole display mathematics - eleven equation images plus one
terrain list - and the seven bands of the MATLAB appendix.

What the record has to say out loud:

1. Caption side never varies and it is the inverse of the usual table convention: all 18
   figure captions and all 7 table captions print BELOW their artwork, including Table 1
   whose caption is pixels inside the pasted table image itself.
2. One numbering run: "Figure N:" and "Table N:" with a colon, 17 and 6 numbers, and the
   appendix's two reprints carry no number and no caption at all.
3. The drawing language is one line-chart engine.  Fifteen of the eighteen figure rows are
   line plots drawn by the same MATLAB export - three to ten joined traces, a key inside
   the top-right corner, no markers, no colour scale; the other three are hand-drawn ray
   schematics.  Nothing in the paper is three-dimensional and nothing carries a colour bar.
4. Panel count tracks the exhibit's job: one frame for a curve family, two side-by-side
   frames for a parameter sweep, 2x2 for the multi-hop propagation process, two stacked
   frames for the F-layer height.
5. Every grid is booktabs - top rule, header rule, bottom rule, no verticals anywhere -
   with no shading, no merge, no diagonal header, no note row and no continuation.  Units
   sit in the header or the stub on all seven.
6. The tables are captioned below and announced by deixis: five of the seven are named
   only as "as shown in Table N", and Table 4's header is transposed - the left block's
   first column is headed "20M Hz" over grazing angles and the right block's is headed
   "15" over frequencies.
7. Eleven cell entries in this paper's display mathematics are pasted equation images that
   the region detector reads as artwork; equation (10) and (13) alone survive as vector
   text.  This is the fourth paper in the batch with that detector asymmetry.
8. The appendix is not a plate section: it reprints Figure 14 and Table 6 inline, with no
   number and no caption, introduced only as "the following figure" and "the following
   table" - the only two exhibits in the paper that no number ever reaches.

Usage: python -I tools/_dist_paper145.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2018-77845-746864a6"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    "f1": (3, [155.9, 536.4, 439.3, 692.3]),
    "t1": (6, [88.0, 297.4, 520.3, 599.0]),
    "f2": (8, [127.6, 411.8, 467.8, 598.6]),
    "t2": (9, [124.2, 57.8, 469.9, 132.8]),
    "f3": (9, [127.6, 271.1, 467.8, 401.0]),
    "f4": (11, [155.9, 64.8, 439.3, 223.8]),
    "f5": (12, [127.6, 443.3, 467.8, 614.3]),
    "f6": (13, [123.1, 330.2, 472.3, 509.9]),
    "f7": (14, [127.6, 194.2, 467.8, 365.2]),
    "f8": (15, [127.6, 64.8, 467.8, 235.8]),
    "f9": (15, [123.1, 278.2, 472.2, 405.7]),
    "f10": (16, [155.9, 181.6, 439.3, 440.5]),
    "t3": (17, [64.8, 51.0, 529.0, 137.3]),
    "f11": (17, [94.8, 228.0, 500.6, 327.8]),
    "f12": (17, [94.8, 500.6, 500.6, 609.6]),
    "t4": (18, [121.0, 65.5, 474.0, 126.3]),
    "t5": (18, [82.7, 347.3, 513.0, 420.3]),
    "f13": (18, [127.6, 529.4, 467.8, 700.4]),
    "f14": (19, [85.1, 409.0, 510.2, 488.9]),
    "t6": (19, [111.0, 620.7, 484.1, 708.2]),
    "f15": (20, [94.8, 438.6, 500.6, 538.4]),
    "f16": (21, [127.6, 64.8, 467.8, 235.8]),
    "f17": (21, [127.6, 336.0, 467.8, 507.0]),
    "fax": (26, [127.6, 94.0, 467.8, 157.9]),
    "tax": (26, [111.0, 215.4, 484.1, 302.9]),
}

EXCLUDED = {
    "p7 equation (1)": (7, [151.7, 364.0, 526.7, 397.8]),
    "p7 equation (2)": (7, [198.1, 569.9, 522.8, 617.9]),
    "p8 equations (3) and (4)": (8, [64.8, 49.7, 529.8, 282.2]),
    "p11 equation (5)": (11, [141.6, 260.8, 524.8, 374.0]),
    "p11 equation (6)": (11, [215.0, 433.4, 529.2, 460.4]),
    "p11 equation (7)": (11, [171.6, 505.0, 529.3, 544.7]),
    "p12 equation (8)": (12, [175.6, 49.7, 521.3, 131.4]),
    "p12 equation (9)": (12, [179.0, 275.2, 529.2, 352.4]),
    "p13 equation (11)": (13, [162.5, 137.0, 529.2, 224.8]),
    "p14 equation (12)": (14, [209.0, 495.1, 530.0, 544.7]),
    "p14 terrain-category list": (14, [65.0, 610.9, 346.2, 703.9]),
    "p27 code band": (27, [64.8, 41.5, 530.5, 119.2]),
    "p30 code band 1": (30, [64.8, 202.8, 530.5, 234.9]),
    "p30 code band 2": (30, [64.8, 695.0, 530.5, 727.2]),
    "p31 code band 1": (31, [64.8, 41.3, 530.5, 127.3]),
    "p31 code band 2": (31, [64.8, 336.4, 530.5, 368.6]),
    "p32 code band 1": (32, [64.8, 41.3, 530.5, 73.8]),
    "p32 code band 2": (32, [64.8, 282.6, 530.5, 314.9]),
}

for _name, (_p, _b) in {**B, **EXCLUDED}.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 43, len(MEASURED)


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


def mention(page: int, *, first: int | None, style: list[str], count: int = 1,
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


def figure(key: str, family: str, caption: dict, men: dict, geom: dict, *,
           path: list[str], kind: str, note: str = "",
           caption_source: str = "text-layer") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "family": family,
        "confidence": "high",
        "panel_count": geom["panel_count"],
        "is_panel_of": "",
        "caption_verbatim": caption["verbatim"],
        "caption_source": caption_source,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }


def grid(rows: int, cols: int, *, header: int = 1, numeric: int = 0, txt: int = 1,
         width: str = "full", units_in_header: bool = True,
         decimal: bool = False) -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": "booktabs",
        "zebra": False,
        "merged_cells": False,
        "diagonal_header": False,
        "units_in_header": units_in_header,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": False,
        "note_sentence": "",
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          note: str = "", caption_source: str = "text-layer") -> dict:
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


P_INTRO = ["1 Introduction", "1.1 Background"]
P_SYM = ["2 Assumption and Symbols", "2.2 Symbols"]
P_MODEL = "3 Multi-Hop Propagation Model"
P_ION = [P_MODEL, "3.2 The Ionosphere"]
P_REFIDX = P_ION + ["3.2.2 The Refractive Index vs. Altitude and Frequency"]
P_ELAY = P_ION + ["3.2.3 E-Layer Refraction"]
P_FLAY = P_ION + ["3.2.4 F-Layer Refraction and Reflection"]
P_SEA = [P_MODEL, "3.3 Propagation on The Sea"]
P_GND = [P_MODEL, "3.4 Propagation on The Ground"]
P_NOISE = [P_MODEL, "3.6 Background Noise"]
P_RES = "4 Result of Part I and Part II"
P_CALM = [P_RES, "4.1 The Comparison of Strength of Single-Hop Radio Wave"]
P_MULTI = [P_RES, "4.2 The Multi-Hop Radio Propagation Process on Ocean Surface"]
P_RUGGED = [P_RES, "4.3 The Comparison of Strength of Single-Hop Radio Wave"]
P_P3 = ["6 Result of Part III"]
P_SENS = "7 Sensitivity Analysis"
P_DENS = [P_SENS, "7.1 Electron Density of The E Layer and F Layer"]
P_HEIGHT = [P_SENS, "7.2 The Height of The F Layer"]
P_WIND = [P_SENS, "7.3 The Wind Speed Near The Sea"]
P_APX = ["Appendix A A Short Synopsis"]

KEYS = ["f1", "t1", "f2", "t2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "t3",
        "f11", "f12", "t4", "t5", "f13", "f14", "t6", "f15", "f16", "f17", "fax", "tax"]

ALL_ITEMS = [
    figure("f1", "flowchart-or-schematic",
           cap("Figure 1: Schematic diagram of Skywave reflection[3]"),
           mention(3, first=3, style=["Figure 1"], count=2, pattern="figure-n-shows",
                   lead="Figure 1 displays the propagation mode."),
           geo("flowchart-or-schematic", numbers=False),
           path=P_INTRO, kind="introduction",
           note="the paper's only side elevation of one hop: a curved earth surface at the "
                "bottom, three coloured ionospheric shells (D-Layer, E-Layer, F-Layer) drawn as "
                "concentric arcs, one critical-angle ray and both single-hop and multi-hop ray "
                "families. No axes, no ticks and no printed numbers - the annotation is eight "
                "rotated word labels inside the drawing. The caption glues the citation to the "
                "last word ('reflection[3]', no space) and the drawing itself is a low-contrast "
                "raster whose two faintest hop paths are close to invisible at print size"),
    table("t1",
          cap("Table 1: Symbols and their meanings", "Table N:", position="below"),
          mention(6, first=6, style=["Table 1"], pattern="direct",
                  lead="Some symbols used in this paper are listed in Table 1"),
          grid(19, 2, header=1, numeric=0, txt=2, units_in_header=False),
          path=P_SYM, kind="symbols", caption_source="typed-from-crop",
          note="the paper's notation glossary and the only exhibit whose caption is pixels: "
               "the whole thing - double top rule, header rule, bottom rule and the line "
               "'Table 1: Symbols and their meanings' - is one pasted image, so the caption "
               "had to be typed from the crop. Two columns, eighteen body rows, no vertical "
               "rule anywhere. The Meaning column mixes prose with nine inline symbols and "
               "carries the paper's only constants (Boltzmann 1.38x10^-23, T0 in Kelvin, the "
               "effective noise bandwidth b), and three rows end with a bracketed citation "
               "([7], [8], [9]) - a reference style no figure caption in the paper uses"),
    figure("f2", "line",
           cap("Figure 2: The distribution of refractive index and electron density with altitude"),
           mention(8, first=8, style=["Figure 2"], count=3, pattern="as-shown-in",
                   lead="the graphs of the distribution of the refractive index and the electron "
                        "density along the height, which is shown in Figure 2",
                   trail="According to the Figure 2 and Equation 2, the refractive index is "
                         "gradually reduced with the increase of the elevation in F layer",
                   read=1),
           geo("line", legend="inside", panels=2, layout="1x2"),
           path=P_REFIDX, kind="model",
           note="the model's first output exhibit: two equal-sized MATLAB frames side by side, "
                "left electron density (10^12 m^-3) against Altitude(km) with one curve and no "
                "key, right refractive index against Altitude(km) with three curves keyed 15 MHz, "
                "17.65 MHz and 20 MHz in a box at upper right. The two panels carry different x "
                "quantities, so nothing is shared; both y axes are the same Altitude(km) scale. "
                "This is the figure the prose re-reads twice on the following page, once for the "
                "decrease of the index and once for its increase above the F layer"),
    table("t2",
          cap("Table 2: Ionospheric parameters used to determine the distribution of "
              "refractive index and electron density", "Table N:", position="below",
              units=True),
          mention(9, first=8, style=["Table 2"], count=1, pattern="figure-n-shows",
                  lead="All these parameters of ionosphere are shown in Table 2."),
          grid(4, 5, header=2, numeric=4, txt=1, units_in_header=True),
          path=P_REFIDX, kind="model",
          note="the only two-tier grid in the paper: five columns printed as two stacked "
               "header-and-value blocks, 'Parameters' and 'Values' repeating as the stub of "
               "each block rather than merging into one. Every cell is a unit-bearing header "
               "over one value - f0E/MHz 3.21, hmE/km 101, ymE/km 10.7, f0F2/MHz 14.20, then "
               "hmF2/km 339.3, ymF2/km 78.0, NmE/m^-3 10^10.5, NmF2/m^-3 2.5x10^12 - so no "
               "column has two numbers and nothing can align on the decimal. The caption prints "
               "below the grid and states no unit of its own"),
    figure("f3", "flowchart-or-schematic",
           cap("Figure 3: A schematic of the refraction of radio waves in the E layer"),
           mention(9, first=9, style=["Figure 3"], pattern="as-shown-in",
                   lead="The refraction process in E layer is a simple single refraction, as "
                        "shown in the Figure 3."),
           geo("flowchart-or-schematic", numbers=False),
           path=P_ELAY, kind="model",
           note="the second hand drawing and the paper's smallest exhibit: two colour-filled "
                "bands (light blue above the middle height of the E layer, yellow-green below) "
                "split by a straight horizontal interface, with a dashed vertical normal, one "
                "incoming ray and one refracted ray. The fills are annotated inside the block "
                "and the layer name 'E layer' sits outside at the right. No axes, no numbers, "
                "no key. Both coloured rectangles keep a hard print outline, so the block reads "
                "as a pasted screenshot of a drawing rather than a vector figure"),
    figure("f4", "flowchart-or-schematic",
           cap("Figure 4: A schematic of the refraction and reflection of radio waves in the F layer"),
           mention(11, first=9, style=["Figure 4"], pattern="figure-n-shows",
                   lead="a schematic diagram Figure 4 based on the"),
           geo("flowchart-or-schematic", numbers=False, panels=2, layout="2x1"),
           path=P_FLAY, kind="model",
           note="two hand-drawn ray constructions stacked in one measured box: the upper half "
                "carries three layer lines labelled n1, n2, n3 with the angle set beta1 to beta3 "
                "and a dashed vertical between the refraction and the reflection legs, the lower "
                "half the same construction one layer deeper with alpha1 to alpha3. These are the "
                "only exhibits in the paper whose annotation is Greek letters instead of words. "
                "No axes, no numbers, no key; the panel spacing is uneven and the lower "
                "construction is drawn about half the width of the upper one"),
    figure("f5", "line",
           cap("Figure 5: The reflection coefficient varies with the grazing angle, the left one "
               "is the hori- zontal polarization wave, and the right one is the vertical "
               "polarization wave", voice="active"),
           mention(12, first=12, style=["Figure 5"], pattern="as-shown-in",
                   lead="are shown in the Figure 5 with the change of grazing angle"),
           geo("line", legend="inside", panels=2, layout="1x2"),
           path=P_SEA, kind="model",
           note="two MATLAB frames side by side, both with grazing angle on x and the reflection "
                "coefficient on y, three curves each (15 MHz, 17.65 MHz, 20 MHz) keyed in a box "
                "at upper right. The left panel decays smoothly, the right panel falls steeply "
                "and flattens, and the two y ranges differ, so the pair shares a variable but not "
                "a scale. The caption identifies the panels by prose ('the left one ... the right "
                "one') and prints no (a)/(b) labels - the paper's usual habit elsewhere"),
    figure("f6", "line",
           cap("Figure 6: Rough correction factor varies with the grazing angle and the wind speed "
               "near the sea surface", voice="active"),
           mention(13, first=13, style=["Figure 6"], count=2, pattern="figure-n-shows",
                   lead="The changes of rough correction factor over the grazing angle and the wind "
                        "speed near the sea surface are shown in Figure 6.",
                   trail="with the increase of grazing angle and the increase of wind speed near "
                         "the sea surface, the rough correction factor of sea surface decreases "
                         "gradually",
                   read=1),
           geo("line", legend="inside", panels=2, layout="1x2"),
           path=P_SEA, kind="model",
           note="the correction-factor sweep, two frames side by side: (a) the factor against "
                "grazing angle at a fixed wind speed, (b) the factor against wind speed at 15 "
                "degrees, three curves each, keys in the top-right corner. Unlike Figure 5 this "
                "pair does carry (a)/(b) labels, printed under the frames - and both labels have "
                "lost their symbols, '(a) varying with the grazing angle, v =' ending in nothing "
                "and '(b) varying with the wind speed, = 15 8m=s' printing a bare equals sign"),
    figure("f7", "line",
           cap("Figure 7: The reflection coefficient of the plane ground surface varies with the "
               "grazing angle, the left one is the horizontal polarization wave, and the right "
               "one is the vertical polarization wave", voice="active"),
           mention(14, first=14, style=["Figure 7"], pattern="figure-n-shows",
                   lead="varying over grazing angle can be drawn as Figure 7"),
           geo("line", legend="inside", panels=2, layout="1x2", shared=True),
           path=P_GND, kind="model",
           note="the ground twin of Figure 5: two frames, three curves each, same key position, "
                "both x axes grazing angle 0-90 so the pair does share a scale. The panels are "
                "told apart only by the caption's prose - no (a)/(b) labels are printed, unlike "
                "Figure 6 directly above it - and both y-axis titles are rotated, tiny and "
                "clipped by the frame, with tick numerals close to illegible at print size"),
    figure("f8", "line",
           cap("Figure 8: The change of s over grazing angle", variables=1),
           mention(15, first=14, style=["Figure 8"], count=2, pattern="as-shown-in",
                   lead="which are shown in Figure 8 and Figure 9",
                   trail="And Figure 8 shows that s can also decrease with the increase of "
                         "grazing angle",
                   read=1),
           geo("line", legend="inside"),
           path=P_GND, kind="model",
           note="one frame of the topographic reduction factor against grazing angle, three "
                "curves, key at upper right, y 0 to 1 in 0.1 steps and x ticks to 80. The caption "
                "is a single line stranded in the gutter between this plot and the two-panel "
                "Figure 9 underneath it, so at first glance it is captioned either; only the "
                "panel labels further down belong to Figure 9. The caption also drops its "
                "subscript, printing 'The change of  s over grazing angle' with the symbol left "
                "bare"),
    figure("f9", "line",
           cap("Figure 9: The change of s over frequency and Sh", variables=2),
           mention(15, first=14, style=["Figure 9"], count=3, pattern="as-shown-in",
                   lead="which are shown in Figure 8 and Figure 9",
                   trail="As can be seen from Figure 9(b), the rough correction factor decreases "
                         "rapidly with the increase of elevation standard deviation",
                   read=1),
           geo("line", legend="inside", panels=2, layout="1x2"),
           path=P_GND, kind="model",
           note="the two-variable version of Figure 8, two frames side by side with their own "
                "(a)/(b) labels printed under them: (a) frequency 0 to 30 MHz, (b) Sh 0 to 100 m, "
                "both y axes 0 to 1. Each panel shows one trace plus a two-entry key. The prose "
                "reads only panel (b) and only at the level of 'decreases rapidly', and one "
                "sentence two pages later cites Figure 9 as the reason to abandon multi-hop "
                "ground cases altogether"),
    figure("f10", "line",
           cap("Figure 10: The background noise corresponding to each frequency[19]"),
           mention(16, first=16, style=["Figure 10"], pattern="as-shown-in",
                   lead="where P is the power (Watt) of radio waves, as shown in Figure 10"),
           geo("line", legend="below"),
           path=P_NOISE, kind="model",
           note="the paper's only borrowed exhibit and its only two-axis plot: a reproduced ITU "
                "noise figure with a log frequency axis 10^4 to 10^8 Hz, a left F_a (dB) scale "
                "and a right F_a (K) decade scale, and six bold curves lettered A to F. The key "
                "is a printed block BELOW the x axis, the only key in the paper that is not "
                "inside the frame, and the block doubles as a legend of six prose descriptions "
                "(atmospheric noise at 0.1% and 99.5% of time, man-made at quiet and median "
                "sites, galactic, minimum expected). The artwork also carries its own bold "
                "title inside the frame, so the figure is titled twice"),
    table("t3",
          cap("Table 3: A show of some cases of the comparison of the wave strength between calm "
              "and turbulent surfaces, where P owerc means the power( in dBw) of the calm-surface "
              "case, and P owert means the power( in dBw) of the turbulent-surface case, Diff. "
              "means the difference between P owerc and P owert", "Table N:", position="below",
              units=True),
          mention(17, first=16, style=["Table 3"], pattern="figure-n-shows",
                  lead="Several cases of radio waves with different frequencies, wind speeds and "
                       "grazing angles are shown in Table 3."),
          grid(5, 5, header=1, numeric=4, txt=1, units_in_header=True, decimal=True),
          path=P_CALM, kind="evaluation",
          note="a five-column booktabs grid of four simulated cases (Cases, Power_c(dBW), "
               "Power_t(dBw), Diff.(dBw), Power ratio), every numeric column printed to three "
               "decimals so the points stack. The stub is a compound string - '20MHz, 15, 8m/s' - "
               "carrying frequency, grazing angle and wind speed in one cell, which is why the "
               "paper needs no second header tier. Units live in the header (dBw) but the "
               "caption has to spell out what the subscripts mean, and it does so in a 53-word "
               "sentence that is four times the length of any figure caption in the paper"),
    figure("f11", "line",
           cap("Figure 11: The changes of the power ratio between the waves on turbulent and calm "
               "ocean surfaces with grazing angle and the wind speed near the sea surface"),
           mention(17, first=16, style=["Figure 11"], pattern="as-shown-in",
                   lead="the changes of the power ratio between the waves on turbulent and calm "
                        "ocean surfaces with grazing angle"),
           geo("line", legend="inside", panels=2, layout="1x2"),
           path=P_CALM, kind="evaluation",
           note="the turbulent/calm power ratio as two frames with (a)/(b) labels, grazing angle "
                "on the left and wind speed on the right. Both frames are drawn at roughly half "
                "the available column width, which leaves wide blank margins and shrinks every "
                "axis label below legibility; the y axis is a ratio in dB and no tick value can "
                "be read at print size"),
    figure("f12", "line",
           cap("Figure 12: A show of the propagation process with varying grazing angle and "
               "varying frequency, in 12(a) the frequency is 20M Hz, and in 12(b) , the grazing "
               "angle is 15", units=True, conditions=True),
           mention(17, first=17, style=["Figure 12"], count=2, pattern="as-shown-in",
                   lead="As shown in the Figure 12, we get the number of hops and the maximum "
                        "propagation distance of each case"),
           geo("line", legend="inside", panels=4, layout="2x2", shared=True),
           path=P_MULTI, kind="result",
           note="the first 2x2 exhibit and the paper's standard way of drawing a multi-hop run: "
                "the left column varies the grazing angle at 20 MHz, the right column varies the "
                "frequency at 15 degrees, each column with the ray family on top and its decaying "
                "envelope underneath, each panel keyed top right and each x axis labelled "
                "propagation distance. Within a column the two rows share one x axis but not a y "
                "scale. This is the exhibit Table 4 tabulates, and the only caption in the paper "
                "that prints parameter values (20M Hz, 15) as prose"),
    table("t4",
          cap("Table 4: A shown of the number of hops and the maximum propagation distance of each "
              "case shown in Figure 12, D means the maximum propagation distance", "Table N:",
              position="below", units=True),
          mention(18, first=17, style=["Table 4"], pattern="figure-n-shows",
                  lead="we get the number of hops and the maximum propagation distance of each "
                       "case, as shown in Table 4"),
          grid(4, 6, header=1, numeric=5, txt=1, units_in_header=True),
          path=P_MULTI, kind="result",
          note="the paper's only six-column grid and its most damaged one: two three-column "
               "blocks abut with no vertical rule between them, so the two half-tables are "
               "separated by whitespace alone. The headers are transposed - the left block's "
               "first column is headed '20M Hz' over grazing angles 5/15/25 and the right "
               "block's is headed '15' over frequencies 15M Hz/17:65M Hz/20M Hz - so a reader who "
               "trusts the header reads the table backwards. One body cell prints a colon for a "
               "decimal point ('17:65M Hz'), and there is no (a)/(b) or block label anywhere"),
    table("t5",
          cap("Table 5: A show of some cases of the comparison of the wave strength between rugged "
              "and smooth ground terrains, where P owers means the power( in dBw) of the "
              "smooth-surface case, and P owerr means the power( in dBw) of the rugged-surface "
              "case, Diff. means the difference between P owers and P owerr, Power ratio is ratio "
              "of rugged-surface power to smooth-surface power", "Table N:", position="below",
              units=True),
          mention(18, first=18, style=["Table 5"], pattern="direct",
                  lead="Table 5 shows the radio-wave power ratio of rugged surface to smooth "
                       "surface in several cases."),
          grid(5, 5, header=1, numeric=4, txt=1, units_in_header=True),
          path=P_RUGGED, kind="evaluation",
          note="the ground twin of Table 3, same five columns and same booktabs skeleton, but the "
               "stub is now three separate parameters ('20M Hz; 15 ; Sh = 5'), consistent to three "
               "decimals in the middle columns. The Power ratio column breaks the alignment: two "
               "values print as 0.309 and 0.009 and the next two jump to scientific notation "
               "(2.547E-5, 6.804E-9), so the decimal points stop stacking. Power_r runs negative "
               "on the last row (-34.486) and the caption still calls the entry a power in dBw"),
    figure("f13", "line",
           cap("Figure 13: A show of the change of the ratio of rugged-surface power to smooth- "
               "surface power with Sh", variables=1),
           mention(18, first=18, style=["Figure 13"], pattern="figure-n-shows",
                   lead="And Figure 13 indicates the change of the power ratio of rugged surface "
                        "to smooth"),
           geo("line", legend="inside"),
           path=P_RUGGED, kind="evaluation",
           note="one frame, three curves in pale blue, pale yellow and pale orange, y the power "
                "ratio 0 to 1 in 0.1 steps, x Sh in metres to about 55. The traces are drawn in "
                "pastels light enough to nearly vanish in print, the rotated y title overlaps its "
                "own tick numerals, and the x title is cut by the frame. This is the one figure "
                "in the paper whose y axis is a dimensionless ratio plotted on the same 0-1 scale "
                "as Figure 8's correction factor"),
    figure("f14", "line",
           cap("Figure 14: A show of the multi-hop propagation of the continue-frequency radio "
               "waves, with speed of wind near the sea is 20m=s, and the ship speed is "
               "41:67km=h, and the frequency range is 21M Hz 21:45M Hz", units=True,
               conditions=True),
           mention(19, first=19, style=["Figure 14"], pattern="direct",
                   lead="A show of the multi-hop propagation process of the continue-frequency "
                        "radio waves is given in Figure 14."),
           geo("line", legend="inside", labels=True),
           path=P_P3, kind="result",
           note="the MSRSM result: one frame carrying a dense family of blue traces that fuse "
                "into five lobes, y A(mV/m) 0 to 300 and x propagation distance to 16000, key at "
                "upper right. This is the paper's only exhibit with printed data labels - MATLAB "
                "data-cursor tooltips are burned into the image at each lobe apex ('X "
                "7.934e+03 Y: 260'), a screenshot artefact no other figure carries. The caption "
                "reproduces the paper's unit and decimal faults unchanged (20m=s, 41:67km=h)"),
    table("t6",
          cap("Table 6: A show of the length of time a ship can remain getting signal in each "
              "intersection area", "Table N:", position="below", units=True),
          mention(19, first=19, style=["Table 6"], pattern="as-shown-in",
                  lead="get the length of time ( hour ) the ship can remain receiving signal in "
                       "each intersection area, as shown in Table 6"),
          grid(6, 5, header=1, numeric=4, txt=1, units_in_header=True, decimal=True),
          path=P_P3, kind="result",
          note="five columns (Intersection zone, Left(km), Right(km), Length(km), Time(hour)) and "
               "four numbered zones plus a total row, the total leaving Left and Right blank "
               "rather than printing a sum. Time is printed to two decimals throughout so it "
               "aligns; the Length column sums correctly (203+393+571+758 = 1925) but the Time "
               "column does not sum to its own total by a rounding step (46.20 against 46.19). "
               "This is the grid the appendix reprints without its number"),
    figure("f15", "line",
           cap("Figure 15: A show of the radio-wave propagation process with the change of electron "
               "density distribution of the E and F layers"),
           mention(20, first=20, style=["Figure 15"], pattern="figure-n-shows",
                   lead="Figure 15 indicates the effect of the change of the maximum electron "
                        "density of E Layer and that of F layer.",
                   trail="As can be seen from it, the increase in E-layer electron density makes "
                         "the radio waves spread farther",
                   read=1),
           geo("line", legend="inside", panels=4, layout="2x2", shared=True),
           path=P_DENS, kind="sensitivity",
           note="the first sensitivity exhibit, drawn with the Figure 12 template exactly: 2x2 "
                "grid, left column (a) varying the E-layer maximum electron density, right "
                "column (b) varying the F layer's, ray family on top and envelope below, keys top "
                "right, columns sharing an x axis but not a y scale. The two columns answer "
                "different questions - the left plot visibly widens with density and the right "
                "does not move at all, which is exactly what the prose says"),
    figure("f16", "line",
           cap("Figure 16: A show of the radio-wave propagation process with the change of the "
               "altitude of F layer"),
           mention(21, first=20, style=["Figure 16"], pattern="as-shown-in",
                   lead="As shown in Figure 16, as the altitude of the F-layer ionosphere "
                        "increases, radio waves can travel higher and the maximum propagation "
                        "distance is increased.",
                   trail="the maximum number of hops does not change",
                   read=1),
           geo("line", legend="inside", panels=2, layout="2x1", shared=True),
           path=P_HEIGHT, kind="sensitivity",
           note="the same drawing turned on its side: two frames stacked instead of two columns, "
                "rays above and envelope below, one key each, x axis shared and y ranges different. "
                "Two traces only, so only two of the three F-layer altitudes named in the prose "
                "(289.8 m, 339.3 m, 418.6 m) are actually plotted, and no legend entry can be read "
                "to say which two. This is the paper's only 2-stacked exhibit"),
    figure("f17", "line",
           cap("Figure 17: A show of the changes of radio wave energy during propagation with "
               "different wind speed"),
           mention(21, first=21, style=["Figure 17"], pattern="figure-n-shows",
                   lead="Figure 17 shows the changes in radio wave energy during propagation with "
                        "different wind speed near the ocean surface.",
                   trail="will cause the electromagnetic wave to lose more energy in reflection",
                   read=1),
           geo("line", legend="inside"),
           path=P_WIND, kind="sensitivity",
           note="the last numbered exhibit, and the only one drawn as a staircase: six traces that "
                "hold a plateau and then drop at discrete propagation distances, one per wind "
                "speed, keyed in a six-entry block at upper right. The plot occupies less than a "
                "third of its column, which pushes the y title and all y numerals below reading "
                "size; the x axis carries a x10^4 multiplier above the tick row"),
    figure("fax", "line",
           cap("", "none"),
           mention(26, first=26, style=[], pattern="direct",
                   lead="The simulation is shown in the following figure."),
           geo("line", legend="inside", labels=True),
           path=P_APX, kind="appendix", caption_source="none",
           note="Figure 14 reprinted inline in Appendix A with no number and no caption - the only "
                "figure in the paper that no number ever reaches. Same five-lobe blue trace "
                "family, same A(mV/m) 0-300 and propagation-distance-to-16000 axes, same burned-in "
                "data-cursor tooltips at the same lobe apices, typeset narrower than the original. "
                "Announced only as 'The simulation is shown in the following figure.'"),
    table("tax",
          cap("", "none"),
          mention(26, first=26, style=[], pattern="direct",
                  lead="the sea is shown in the following table"),
          grid(6, 5, header=1, numeric=4, txt=1, units_in_header=True, decimal=True),
          path=P_APX, kind="appendix", caption_source="none",
          note="Table 6 reprinted inline in Appendix A, identical cells and identical "
               "horizontal-only rules, with no number and no caption - announced only as 'is shown "
               "in the following table'. Together with the plate above it makes the appendix the "
               "one part of the paper where an exhibit carries neither a number nor a caption, "
               "and it is the only duplicate pair in the census (Figure 14 / Table 6)."),
]

FIGURES = [it for it in ALL_ITEMS if "family" in it]
TABLES = [it for it in ALL_ITEMS if "family" not in it]

_order = sorted(((k, it) for k, it in zip(KEYS, ALL_ITEMS)),
                key=lambda kv: (B[kv[0]][0], B[kv[0]][1][1]))
_page_seen = {}
for i, (key, item) in enumerate(_order, 1):
    item["place"]["doc_order"] = i
    pg = item["page"]
    _page_seen[pg] = _page_seen.get(pg, 0) + 1
    item["place"]["page_order"] = _page_seen[pg]

RULES = [
    "Caption side never varies and it inverts the usual table convention: all 18 figure "
    "captions and all 7 table captions print BELOW their artwork, so 25 of 25 exhibits are "
    "below-cased and the paper has no above-case to compare against [caption.position].",
    "One numbering vocabulary runs the whole body - 'Figure N:' for 17 numbers and 'Table N:' "
    "for 6 - a colon with no period anywhere, and the only exhibits outside it are the two "
    "appendix reprints, which print no number at all [caption.numbering].",
    "Captions are labels, not sentences: the 17 numbered figure captions run 8 to 41 words "
    "with a median of 18, and the four longest (Figures 5, 7, 11 and 14) are long only because "
    "they enumerate panels or parameter values rather than because they argue [caption.words].",
    "Only three captions name a plotted symbol, and one of them names two: the 'change of s "
    "over grazing angle' of Figure 8, the 'change of s over frequency and Sh' of Figure 9 and "
    "the '... power with Sh' of Figure 13 - so everywhere else the caption names the exhibit's "
    "subject and leaves the plotted quantity to the axis title [caption.variable_count].",
    "Units are stated in 7 of the 25 captions - Figures 12 and 14 and the four value grids - "
    "and only ever as a parenthesised or trailing unit inside a prose list ('20m=s', "
    "'41:67km=h', 'Power_c(dBW)'), never as a bracketed unit after the plotted quantity, so a "
    "reader who wants the unit of Figure 5's reflectance has to go to the axis [caption.units].",
    "No caption in the paper concludes anything: none of the 25 states a result, a comparison "
    "or a direction of change, and the four that look like conclusions (the 'A show of the "
    "change of ...' family) stop at naming the two quantities being plotted [caption.concludes].",
    "Every one of the seven grids is booktabs - a top rule, one rule under the header band and "
    "a bottom rule, with no vertical rule at any cell boundary and no box - which makes this "
    "the cleanest table set in the batch after three papers of fully ruled grids "
    "[table.rule_style].",
    "No grid in the paper shades a row, merges a cell, prints a diagonal header, continues "
    "across a page break or carries a note row: the only structural variation among the seven "
    "is Table 2's second header band and Table 4's two abutting blocks [table.zebra].",
    "Units go into the header or the stub on every grid that has them - dBw, km, MHz, m^-3, "
    "hour - so no cell ever repeats a unit, and the two grids whose cells are pure numbers "
    "(Tables 4 and 6) are exactly the two whose headers carry the unit instead [table."
    "units_in_header].",
    "Decimal alignment happens only where a column is printed to a fixed number of places: "
    "Tables 3 and 6 align because all their values carry three and two decimals, and Tables "
    "4 and 5 do not because integers or the E-notation ratio column break the stack [table."
    "decimal_aligned].",
    "Grid width is not a design choice here but a column count: the two-column glossary and "
    "the five-column grids all run the full measure, and the only narrowing is whatever the "
    "tabulation engine produced [table.width].",
    "Drawing language is one engine: 15 of the 18 figure rows are line plots from the same "
    "MATLAB export - joined traces with no markers, a key inside the top-right corner and no "
    "annotated data - while the other three are hand-drawn ray schematics with no axes at all "
    "[geometry.family].",
    "Nothing in the paper is three-dimensional and nothing carries a colour scale: every plot "
    "is a flat 2-D frame and the only colour anywhere encodes a curve identity, not a "
    "continuous field [geometry.colorbar].",
    "Fourteen of the fifteen plots key their curves inside the frame at upper right, the "
    "borrowed noise figure keys its six entries below the x axis instead, and the three "
    "schematics carry no key at all - so key position is the field that separates the paper's "
    "own art from its one quotation [geometry.legend].",
    "Panel count tracks the exhibit's job rather than its subject: 8 exhibits stand on one "
    "frame (a single curve family), 8 on two frames - side by side for a parameter sweep "
    "(Figures 2, 5, 6, 7, 9, 11) or stacked for the F-layer height (Figures 4 and 16) - and the "
    "2 propagation-process exercises (Figures 12 and 15) alone get a 2x2 [geometry.panel_count].",
    "Panels share an axis only when they plot the same variable: the 2x2 propagation grids "
    "share the x axis within each column and Figure 7's polarization pair shares its grazing "
    "angle, while every sweep pair (Figures 5, 6, 9, 11) keeps two independent x axes "
    "[geometry.shared_axes].",
    "Exhibits are announced on their own page or one page early and never later: 17 of the 25 "
    "carry lead 0 and 7 carry lead 1, with one outlier - Figure 4, announced two pages before "
    "it prints - so the announcement follows the argument's grain rather than a fixed rule "
    "[mention.lead_pages].",
    "Citations are formulaic to the point of vacancy: most of the 25 are reached only by 'as "
    "shown in Figure N' or 'as shown in Table N', and only Figures 1, 2, 6, 8, 13, 15, 16 and "
    "17, plus Tables 3 and 5, get a verb that reads them [mention.style].",
    "The appendix breaks the numbering system: its two exhibits carry no number and no "
    "caption and are announced only as 'the following figure' and 'the following table', so "
    "the paper ends with two exhibits that no number reaches [mention.first_page].",
    "Placement follows the text that introduces it rather than the top of the page: 12 of the "
    "25 exhibits land in the middle band and 10 in the top third, and the three foot-band "
    "cases - Figure 1, Figure 13 and Table 6 - each carry their caption as the last line on "
    "the page, so a bottom-of-page exhibit always closes its page rather than opening the next "
    "[place.page_zone].",
    "Exhibit density follows the section kind: the model sections (3.2-3.6) hold 9 of the 18 "
    "figures, section 4 holds 3, section 6 one, sensitivity 3 and the appendix 1, so the paper "
    "front-loads its drawings into the derivation and repeats the same 2x2 grammar three "
    "sections later [place.section_kind].",
]

NOTE = (
    "This is a model paper built around one plotting engine and one table engine, and the "
    "census reads cleanly because almost every field has a single value. Forty-three measured "
    "regions resolve to 18 figure rows, 7 table rows and 18 exclusions, with nothing "
    "unaccounted.\n\n"
    "The exclusions are the interesting half. Eleven of the paper's display equations are "
    "pasted images - (1) and (2) on p7, (3) and (4) on p8, (5), (6) and (7) on p11, (8) and "
    "(9) on p12, (11) on p13 and (12) on p14 - while equations (10) and (13) alone survive as "
    "vector text. That asymmetry is the same detector artefact recorded on three earlier "
    "papers in this batch (MathType on P-A-2018-76082, NetLogo on P-F-2017-68940, pasted "
    "LaTeX on P-A-2018-76271), and it is worth folding into the lane findings: display "
    "mathematics pasted from an equation editor registers as artwork, one more region per "
    "equation, and the only defence is reading the crop. The twelfth exclusion is a pasted "
    "screenshot of the terrain-category bullet list on p14, and the last seven are the MATLAB "
    "code bands of Appendix B on pp27-32.\n\n"
    "What the record calls a pattern. (1) Caption side is invariant: every exhibit in the "
    "paper, figure or table, prints its caption below the artwork. That is worth stating "
    "because the lane has now seen four conventions - side follows the exhibit kind, side "
    "follows the section of the paper, side follows the drawing tool, and here no convention "
    "at all beyond 'always below'. (2) The plot template is one export: joined traces, no "
    "markers, a key inside the top-right corner, no colour scale, no data labels, axes titled "
    "in words. The second sensitivity, legend position, is what identifies the single "
    "borrowed figure - its six-entry key sits below the x axis. (3) Panel count is a grammar: "
    "1 for a curve family, 1x2 for a sweep over two parameters, 2x2 for the propagation "
    "process, 2x1 for the height sweep. (4) The table template is booktabs, seven times, with "
    "no shading, no merge, no diagonal, no note row and no continuation; the only two "
    "structural exceptions are Table 2's second header band and Table 4's two blocks, and "
    "Table 4's blocks are the paper's worst table defect because the headers are transposed "
    "against the columns beneath them.\n\n"
    "What the record calls a defect. Figure 8's caption is stranded in the gutter between two "
    "plots and reads as captioned to the wrong one. Figure 16 names three F-layer altitudes "
    "in the prose and plots two. Figure 14's artwork carries MATLAB data-cursor tooltips "
    "burned in as if they were data labels. Table 5 calls a negative dBw entry a power. The "
    "p8 and p13 equations lose every superscript in the text layer ('m 3' for m^-3, 'dB=km' "
    "for dB/km). Figure 4 is announced two pages before it prints while every other exhibit "
    "is announced on its page or one page early.\n\n"
    "How the section-level grammar runs. Sections 1 and 2 carry one exhibit each (the hop "
    "schematic and the notation glossary). Section 3 carries nine - one per mechanism as the "
    "model is derived: distribution of electron density, E-layer refraction, F-layer "
    "reflection, sea reflection, sea roughness, ground reflection, ground roughness times "
    "two, and background noise. Section 4 carries five, and the pattern there is tabulate-"
    "then-plot: Table 3 then Figure 11, Table 4 then (via Figure 12) Table 4, Table 5 then "
    "Figure 13. Sections 5 and 6 carry three, one of which is the appendix reprint. Section 7 "
    "carries three, all drawn with the same 2x2/2x1 grammar. Appendix A carries the two "
    "unnumbered reprints and Appendix B the code, which is excluded as not-an-exhibit.\n\n"
    "Reading-order note. The caption of Figure 9 prints below Figure 9's panels, and Figure "
    "8's caption prints immediately under Figure 8's single frame; the (a)/(b) labels under "
    "the Figure 9 panels belong to Figure 9, not to Figure 8, even though the text layer "
    "emits them in the order caption-8, label-a, label-b, caption-9."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"page": p, "bbox": b, "reason": "not-an-exhibit", "note": name}
        for name, (p, b) in EXCLUDED.items()
    ],
    "rules": RULES,
    "note": NOTE,
}


def main() -> int:
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, indent=1, ensure_ascii=False), encoding="utf-8")
    fam: dict[str, int] = {}
    for it in FIGURES:
        fam[it["family"]] = fam.get(it["family"], 0) + 1
    zone: dict[str, int] = {}
    for it in FIGURES + TABLES:
        zone[it["place"]["page_zone"]] = zone.get(it["place"]["page_zone"], 0) + 1
    lead: dict = {}
    for it in FIGURES + TABLES:
        lead[it["mention"]["lead_pages"]] = lead.get(it["mention"]["lead_pages"], 0) + 1
    print(f"{PID}: figures={len(FIGURES)} tables={len(TABLES)} "
          f"excluded={len(EXCLUDED)} regions={len(MEASURED)}")
    print("fam", dict(sorted(fam.items())))
    print("zone", dict(sorted(zone.items())))
    print("lead", dict(sorted(lead.items(), key=lambda kv: str(kv[0]))))
    print("payload", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
