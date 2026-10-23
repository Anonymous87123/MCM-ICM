"""Hand pass for P-A-2018-86103-6d21eb9d ("Simulation Analysis of Multi-hop HF Radio").

28 pages, 34 measured regions on 18 pages: 18 figure rows, 6 table rows and 10 exclusions.
The exclusions are the display mathematics (1)-(4) on p9, (7) and (8) on p11, (10)-(13) on
p12 - all pasted equation images - plus the two MATLAB code bands of the appendix on p25 and
p27.

What this paper contributes to the census:

1. It is the only paper in the batch that runs its figure numbers TWICE. The abstract page
   prints "Figure 1 The wave situation when the wind scale is 6" and "Figure 2 The
   relationship between the wind scale and the first reflection intensity"; the body opens
   section 4.1.2 with "Figure 1 HF propagation diagram" and "Figure 2 Inner layers of
   ionosphere". Four exhibits, two numbers, and no sentence anywhere reconciles them.
2. Caption side is decided by exhibit kind and never varies: all 18 figure rows caption BELOW
   their artwork, all 6 table rows caption ABOVE their grid. The numbering has no colon and
   no period - "Figure N" / "Table N", then the title as a noun phrase.
3. The abstract's two exhibits print in reverse order: Figure 2 sits above Figure 1 on p2, and
   the abstract prose that introduces them is interleaved across two columns so that no lead
   sentence survives intact.
4. Three of the four 3-D exhibits in the paper are the same MATLAB surface: the abstract's
   Figure 1, the four frames of Figure 3 and the SNR surface of Figure 13. Figure 13 is the
   only exhibit with a colourbar, and the only 3-D exhibit whose third axis carries data.
5. Two figures are pasted Excel charts carrying their own numeric data table under the plot
   area, with dashed leader lines from the bars to the table rows - the same chart twice, as
   the abstract's Figure 2 and the body's Figure 10.
6. The grids split by tool, not by taste: the three native Word tables (Table 1, Table 4,
   Table 5) are booktabs-like with no outer box, the two imported multi-tier grids (Table 2,
   Table 3) are fully boxed with merged header cells, and Table 2 adds a slanted corner cell
   under it. Table 5 has no header row at all.
7. The paper is the batch's first with a WRONG kind noun: p17 announces Table 2 as "The
   following figure shows the atmospheric noise table".

Usage: python -I tools/_dist_paper146.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2018-86103-6d21eb9d"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    "abs_f2": (2, [313.9, 445.2, 500.2, 563.6]),
    "abs_f1": (2, [103.0, 585.0, 273.7, 710.3]),
    "f1": (8, [154.7, 71.4, 439.7, 202.6]),
    "f2": (8, [156.0, 409.3, 422.6, 553.2]),
    "f3a": (10, [164.3, 132.0, 292.3, 226.0]),
    "f3b": (10, [308.8, 132.2, 436.8, 226.0]),
    "f3c": (10, [162.8, 261.0, 290.9, 354.7]),
    "f3d": (10, [307.3, 261.0, 435.4, 354.7]),
    "f4": (10, [151.1, 579.0, 441.6, 716.3]),
    "f5": (12, [149.4, 440.8, 444.5, 676.3]),
    "f6": (13, [112.1, 172.8, 481.8, 295.1]),
    "f7": (14, [156.0, 71.4, 467.0, 218.8]),
    "f8": (14, [137.3, 484.4, 439.9, 720.0]),
    "f9": (15, [143.4, 173.5, 439.8, 409.1]),
    "f10": (16, [126.4, 112.1, 467.5, 314.8]),
    "f11": (18, [137.6, 297.4, 438.7, 552.4]),
    "f12": (19, [97.9, 71.4, 493.2, 306.2]),
    "f13": (20, [119.4, 87.6, 462.2, 309.0]),
    "t0": (7, [94.4, 215.1, 501.6, 469.4]),
    "t1": (16, [204.2, 381.9, 391.1, 465.3]),
    "t2": (17, [129.7, 363.2, 470.6, 454.3]),
    "t3": (18, [132.0, 649.4, 463.8, 732.9]),
    "t4": (20, [121.0, 442.9, 474.9, 538.7]),
    "t5": (21, [88.2, 289.4, 515.5, 399.1]),
}

EXCLUDED = {
    "p9 equation (1)": (9, [212.3, 240.4, 514.4, 283.9]),
    "p9 equation (2)": (9, [191.3, 348.1, 507.0, 387.1]),
    "p9 equation (3)": (9, [182.5, 467.4, 514.0, 499.0]),
    "p9 equation (4)": (9, [139.3, 665.3, 514.3, 705.8]),
    "p11 equation (7)": (11, [104.0, 229.1, 527.0, 271.8]),
    "p11 equation (8)": (11, [125.0, 499.4, 522.5, 550.4]),
    "p12 equation (10)": (12, [242.6, 171.8, 351.4, 202.7]),
    "p12 equations (11) to (13)": (12, [176.3, 247.0, 506.5, 370.0]),
    "p25 MATLAB code band": (25, [87.8, 47.0, 510.3, 135.6]),
    "p27 MATLAB code band": (27, [87.8, 47.0, 510.3, 79.8]),
}

for _name, (_p, _b) in {**B, **EXCLUDED}.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 34, len(MEASURED)


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
        "area_frac": round(frac, 4),
        "solo_page": False,
    }


def cap(v: str, numbering: str = "Figure N", *, position: str = "below",
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


def figure(key: str, caption: dict, men: dict, geom: dict, *, path: list[str],
           kind: str, note: str = "", caption_source: str = "text-layer") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "family": geom["family"],
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
         rule: str = "booktabs", zebra: bool = False, merged: bool = False,
         diagonal: bool = False, units_in_header: bool = False, decimal: bool = False,
         width: str = "full", note: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rule,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diagonal,
        "units_in_header": units_in_header,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": False,
        "note_sentence": note,
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


P_ABS = ["Summary"]
P_NOT = ["3 Notation"]
P_41 = ["4 Radio propagation on sea surface model", "4.1 Introduction to HF propagation",
        "4.1.2 Structure of ionosphere"]
P_42 = ["4 Radio propagation on sea surface model", "4.2 Wave model",
        "4.2.3 Model simulation"]
P_43 = ["4 Radio propagation on sea surface model",
        "4.3 Transmission loss of HF radio waves Lb"]
P_433 = P_43 + ["4.3.3 Sea surface reflection loss Lg"]
P_44 = ["4 Radio propagation on sea surface model", "4.4 First reflection intensity"]
P_452 = ["4 Radio propagation on sea surface model", "4.5 Calculation of SNR",
         "4.5.2 Field intensity of atmospheric noise"]
P_5 = ["5 Comparison between sea surface model and ground surface"]
P_61 = ["6.1 Maximum time(tmax) using the same multi-hop path"]
P_62 = ["6.2 Suggestions on frequency selection of transmitter"]

CAP_ABS_F2 = "Figure 2 The relationship between the wind scale and the first reflection intensity"
CAP_ABS_F1 = "Figure 1 The wave situation when the wind scale is 6"
CAP_F3 = "Figure 3 Wave situation of 5∼8 winds"
CAP_T5 = ("Table 5 Recommended emission frequency 2∼ 4 MHz Tropical frequency, small number "
          "of sunspots and transmission is good.")

FIGURES = [
    figure("abs_f2",
           cap(CAP_ABS_F2),
           mention(2, first=2, style=["Figure 2"], count=1),
           geo("bar", legend="inside", labels=True),
           path=P_ABS, kind="abstract",
           note="an Excel clustered-column chart with its numeric data table burned into the "
                "same image: nine wind-scale categories on x, three series (10MHz, 20MHz, "
                "30MHz), y 'The Strength of the First Reflection P (dBw)' from -161 to -158, a "
                "legend chip block inside the plot area at lower left, and dashed leader lines "
                "running from each bar down to a three-row value table that prints -161.2 to "
                "-167.4 under the x axis. Pasted as a screenshot with a light grey frame, so "
                "the table half is artwork, not a constructible grid. This is the same chart as "
                "the body's Figure 10, printed twice under two different numbers"),
    figure("abs_f1",
           cap(CAP_ABS_F1),
           mention(2, first=2, style=["Figure 1"], count=1,
                   lead="we analyze the possible superposition of waves, and get the "
                        "three-dimensional simulation diagram of the waves, and simulate it."),
           geo("surface-or-3D", three_d="surface-mesh"),
           path=P_ABS, kind="abstract",
           note="the abstract's three-dimensional sea surface: a faceted MATLAB surf of the "
                "Longuet-Higgins model with height colour-mapped across the mesh, x and y both "
                "0 to 500 and a vertical axis 100 to 300, no axis titles and no colourbar. This "
                "is the exhibit the abstract text calls 'the three-dimensional simulation "
                "diagram of the waves'. It prints BELOW the abstract's Figure 2 and carries the "
                "smaller number, so the abstract page numbers its two exhibits against reading "
                "order"),
    figure("f1",
           cap("Figure 1 HF propagation diagram"),
           mention(8, first=8, style=["Figure 1"], count=1),
           geo("flowchart-or-schematic", numbers=False),
           path=P_41, kind="model",
           note="a pasted illustration, not a plot: a photographic Earth globe at the lower "
                "right, a gradient sky, a satellite inset, red and blue single-hop and multi-hop "
                "ray paths between ground and an 'ionosphere' band, and concentric ground-wave "
                "arcs. No axes, no ticks, no key, no scale of any kind - the only quantitative "
                "content is the words 'ionosphere' burned into the image. It reuses the number 1 "
                "of the abstract's surface plot two pages earlier"),
    figure("f2",
           cap("Figure 2 Inner layers of ionosphere"),
           mention(8, first=8, style=["Figure 2"], count=1),
           geo("flowchart-or-schematic", panels=2, layout="1x2", shared=True),
           path=P_41, kind="model",
           note="two banded frames side by side, 'Night' and 'Day', each stacking the ionospheric "
                "layers as coloured stripes labelled F, F1, F2, E, D inside the bands. Only the "
                "left frame carries a y axis, 'Height(km)' with ticks 0/100/200/300, and the "
                "shared scale is the reason the right frame prints none; the x axis is unlabelled "
                "and a centre divider reads as a frame edge. No (a)/(b) panel letters. Second "
                "reuse of a body number already spent on the abstract"),
    figure("f3a",
           cap(CAP_F3),
           mention(10, first=10, style=["Figure 3"], count=1,
                   lead="We simulated the model in MATLAB, and the results are as follows:"),
           geo("surface-or-3D", three_d="surface-mesh", layout="2x2"),
           path=P_42, kind="model",
           note="panel 1 of the four-frame Figure 3 grid (wind scales 5 to 8, read in reading "
                "order): the same faceted surf as the abstract's Figure 1, at a coarser grid, "
                "with x and y 0 to 500 and z 100 to 300 but no axis titles. The four frames are "
                "four separate measured regions because the export left a wide gutter between "
                "them, and no (a)-(d) labels exist anywhere - the order is implied by the "
                "caption's range '5∼8' alone"),
    figure("f3b",
           cap(CAP_F3),
           mention(10, first=10, style=["Figure 3"], count=1,
                   lead="We simulated the model in MATLAB, and the results are as follows:"),
           geo("surface-or-3D", three_d="surface-mesh", layout="2x2"),
           path=P_42, kind="model",
           note="panel 2 of Figure 3: same axes, same palette, one wind scale further on. The "
                "frames differ only in facet density, so a reader cannot tell which wind scale "
                "he is looking at without counting the caption's range"),
    figure("f3c",
           cap(CAP_F3),
           mention(10, first=10, style=["Figure 3"], count=1,
                   lead="We simulated the model in MATLAB, and the results are as follows:"),
           geo("surface-or-3D", three_d="surface-mesh", layout="2x2"),
           path=P_42, kind="model",
           note="panel 3 of Figure 3: the lower-left frame, the roughest sea of the four, with "
                "the same unlabelled 0-500 base and 100-300 height"),
    figure("f3d",
           cap(CAP_F3),
           mention(10, first=10, style=["Figure 3"], count=1,
                   lead="We simulated the model in MATLAB, and the results are as follows:"),
           geo("surface-or-3D", three_d="surface-mesh", layout="2x2"),
           path=P_42, kind="model",
           note="panel 4 of Figure 3: lower-right frame, closing the wind-scale range. With the "
                "caption printed once for four frames, this exhibit is the paper's only multi-"
                "panel figure that shares one caption across regions the detector measured "
                "separately"),
    figure("f4",
           cap("Figure 4 Parts of transmission loss"),
           mention(10, first=10, style=["Figure 4"], count=1,
                   lead="the basic transmission loss of sky-wave propagation is as follows:"),
           geo("flowchart-or-schematic", numbers=False),
           path=P_43, kind="model",
           note="a left-to-right decomposition tree: a pale-blue 'Transmission loss Lb' root box "
                "with four grey boxes stacked vertically to its right (free space Lbf, "
                "ionospheric absorption La, sea surface reflection Lg, additional YP) joined by "
                "dashed curved connectors, all labels burned in. No axes, no numbers. The node "
                "labelled 'La' contradicts equation (5) printed directly above it, which "
                "decomposes Lb into Lbf + Li + Lg + YP - the diagram and the formula disagree on "
                "the ionospheric term's letter"),
    figure("f5",
           cap("Figure 5 The relationship between RH , RV and incidence angle"),
           mention(12, first=12, style=["Figure 5"], count=1,
                   lead="Accordingto thisformula"),
           geo("line", panels=2, layout="1x2", shared=True),
           path=P_433, kind="model",
           note="two MATLAB frames side by side, 'incident angle( ° )' on x from 0 to 90 and "
                "'reflection coefficient' on y from 0.2 to 1 in both, blue and red traces for "
                "the two working frequencies the code sets. No key anywhere: the legend call is "
                "commented out in the appendix listing, so the colours are identified only by "
                "the caption's prose. The left frame falls monotonically and the right frame "
                "dips to a minimum near 8 degrees, the paper's only non-monotone curve"),
    figure("f6",
           cap("Figure 6 Diagram of electromagnetic wave reflection on turbulent ocean"),
           mention(13, first=13, style=["Figure 6"], count=1),
           geo("flowchart-or-schematic", numbers=False),
           path=P_433, kind="model",
           note="a hand-drawn ray construction: seven or eight arrow-headed rays from upper left "
                "striking a thick cyan wavy sea profile, with reflected rays leaving at matching "
                "angles and one near-vertical ray. No axes, no ticks, no key, no letters - the "
                "only annotation is the wave line itself. This is the paper's one attempt to "
                "draw the geometry that the rest of section 4.3.3 computes"),
    figure("f7",
           cap("Figure 7 Diagram of wave shadow"),
           mention(14, first=14, style=["Figure 7"], count=1,
                   trail="As shown in the figure, the actual waves will have ups and downs."),
           geo("flowchart-or-schematic", numbers=False),
           path=P_433, kind="model",
           note="the mechanism behind the correction coefficient: two rays grazing a cyan wave "
                "profile with the occluded pocket between wave crest and ray filled with hatching. "
                "No axes, no key, no numbers - the hatched area is the 'shaded area' that "
                "equation (17) divides by the total surface area, and the figure is the only "
                "thing that explains what s means"),
    figure("f8",
           cap("Figure 8 Diagrams of correction coefficients"),
           mention(14, first=14, style=["Figure 8"], count=1,
                   lead="The correction method is as follows:"),
           geo("line", legend="inside", panels=2, layout="1x2"),
           path=P_433, kind="model",
           note="two frames of the correction coefficient against 'wind speed(m/s)' 0 to 20: the "
                "left one keyed 10MHz/20MHz/30MHz with y 0.97 to 1, the right one keyed "
                "1°/5°/15° with y 0.84 to 1, both keys boxed inside the lower left. The two "
                "frames hold the same three curves at different grazing angles, so the pair is a "
                "wind-speed sweep drawn twice rather than two variables - and the y ranges differ "
                "by a factor of five, which the shared 0-20 x axis hides"),
    figure("f9",
           cap("Figure 9 Relation curve of reflection coefficient under different wind speed"),
           mention(15, first=15, style=["Figure 9"], count=1,
                   lead="We can get the following curve"),
           geo("line", legend="inside"),
           path=P_433, kind="model",
           note="one frame, four decaying traces keyed inside at upper right as calm / level 2 / "
                "level 4 / level 6, x 'frequency(MHz)' from 0 to 30 and y 'reflection "
                "coefficient' from 0.1 to 1. The wind states are named in words, not by the sea "
                "state numbers the prose uses elsewhere, so the figure and the text do not share "
                "a vocabulary; the top trace is flat enough that the caption's 'under different "
                "wind speed' is visible only in the lower three"),
    figure("f10",
           cap("Figure 10 The strength of the first reflection P1"),
           mention(16, first=16, style=["Figure 10"], count=1,
                   lead="we get the following chart by calculation:"),
           geo("bar", legend="inside", labels=True),
           path=P_44, kind="result",
           note="the same Excel screenshot as the abstract's Figure 2, printed at body size with "
                "its numeric table burned in and its legend chips floating inside the plot area. "
                "Caption carries the only symbol in the paper's caption set ('P1'), and the "
                "values run -154.2 to -167.4 dBw. Because the table is pixels, none of the "
                "numbers this exhibit exists to communicate can be extracted as text"),
    figure("f11",
           cap("Figure 11 Reflection coefficient relationship curves under different ground "
               "conditions"),
           mention(18, first=18, style=["Figure 11"], count=1,
                   lead="tute the electromagnetic parameters of ground into the formula"),
           geo("line", legend="inside", panels=2, layout="1x2"),
           path=P_5, kind="evaluation",
           note="the ground twin of Figure 5: two frames against 'frequency(MHz)', the left one "
                "titled 'reflection coefficient' and the right one 'sea surface reflection loss' "
                "(the y title was not updated when the ground case was cloned from the sea "
                "case), four traces keyed calm / hills / low mountains / middle mountains inside "
                "the right frame only. The left panel's traces are therefore identified by colour "
                "alone, and the right panel converts the same four curves to a negative dB "
                "scale"),
    figure("f12",
           cap("Figure 12 Strength of the first reflection"),
           mention(19, first=19, style=["Figure 12"], count=1,
                   trail="We take Lg as 6.53dB when the ground is flat and we get that n = 4."),
           geo("bar", legend="inside", labels=True),
           path=P_5, kind="evaluation",
           note="the same chart a third time, with the axis recast for terrain: pasted Excel "
                "clustered columns, y 'The Strength of the First Reflection P (dBw)', x 'The "
                "relief degree', three series, a data table burned in under the plot and leader "
                "lines down to it. The x title is detached below the embedded table and the "
                "y title is set at roughly twice the size of the tick numerals, so the exhibit "
                "reads as a screenshot pasted at the wrong scale"),
    figure("f13",
           cap("Figure 13 Relationships among distance, frequency and SNR"),
           mention(20, first=20, style=["Figure 13"], count=1,
                   trail="As shown in the figure, SNR of 100w signal is obtained at the receiving "
                         "points"),
           geo("surface-or-3D", three_d="surface-mesh", colorbar=True),
           path=P_61, kind="result",
           note="the paper's only exhibit with three data axes: a MATLAB surf of SNR against "
                "'Distances /km' (the x ticks print 00 for the leading zero) and 'Frequency "
                "/MHz', z 'SNR /dB', coloured by a jet colourbar running -50 to 100. It is also "
                "the only colourbar in the paper and the only 3-D exhibit whose vertical axis is "
                "a measured quantity rather than a surface height. No key: the colour is the "
                "fourth dimension"),
]

TABLES = [
    table("t0",
          cap("", "none"),
          mention(7, first=None, style=[]),
          grid(16, 2, header=1, numeric=0, txt=2, zebra=True,
               note="P.s. Other symbols instruction will be given in the text."),
          path=P_NOT, kind="symbols", caption_source="none",
          note="the notation glossary of section 3, and the only grid in the paper with no "
               "caption and no number: the section heading '3 Notation' is its title, and a "
               "note row under the last rule prints 'P.s. Other symbols instruction will be "
               "given in the text.' Sixteen body rows in two columns, top rule and header rule "
               "and bottom rule with one internal vertical between the columns, and alternating "
               "grey row shading - the paper's only zebra banding anywhere. Sixteen symbols "
               "including the three the model leans on most (r propagation distance, D maximum "
               "propagation distance, n number of hops)"),
    table("t1",
          cap("Table 1 Related Parameters", "Table N", position="above"),
          mention(16, first=16, style=["Table 1"], count=0),
          grid(5, 3, header=1, numeric=2, txt=1, units_in_header=True),
          path=P_44, kind="result",
          note="the paper's parameter sheet, printed on the same page as Figure 10 and never "
               "announced by a sentence - the caption is the only thing that names it. Three "
               "columns (Parameter, Reference value, Unit), five rows: La 4 dB, YP 15 dB, f 100 "
               "MHz, P0 100 w, θ 3 degrees. Top rule, header rule and bottom rule with internal "
               "verticals and no outer box, so it reads as booktabs that kept one vertical line "
               "per column boundary. Units are all in the third column rather than in the "
               "header, which is the only grid in the paper that does it that way; 'w' prints "
               "lowercase for watts"),
    table("t2",
          cap("Table 2 Atmospheric noise at different times in a certain area in summer",
              "Table N", position="above"),
          mention(17, first=17, style=["Table 2"], count=1,
                  lead="atmospheric noise table at different times in a certain area in summer"),
          grid(4, 10, header=3, numeric=9, txt=1, rule="boxed", merged=True, diagonal=True),
          path=P_452, kind="model",
          note="the paper's widest and most structured grid: ten columns - a stub plus nine "
               "coefficients - under three header tiers (a longitude band 75~90 / 90~105 / "
               "105~120 merged across three columns each, a local-time band 0~4 / 4~8 / 8~12, "
               "and a slanted corner cell carrying 'Longitude / Local Time / Coefficient'). "
               "Fully boxed with a vertical rule at every cell boundary, four body rows, no "
               "units and no decimal alignment because every entry is an integer coefficient. "
               "It is also the exhibit the prose mislabels: p17 introduces it as 'The following "
               "figure shows the atmospheric noise table', so the paper's only three-tier header "
               "is announced with the wrong exhibit noun"),
    table("t3",
          cap("Table 3 ε,σ in different environments", "Table N", position="above"),
          mention(18, first=18, style=["Table 3"], count=1,
                  lead="The related parameters are shown in the table."),
          grid(4, 5, header=2, numeric=4, txt=1, rule="boxed", merged=True,
               units_in_header=True),
          path=P_5, kind="evaluation",
          note="the ground-parameter grid behind Figure 11: four materials (seawater, "
               "freshwater, wet soil, dry soil) against five effective columns, with two merged "
               "two-column header spans - 'Variation' over the ε/σ pair and 'Average' over the "
               "second ε/σ pair - which is why the header needs two rows. Units sit in the "
               "header as ε(F/m) and σ(S/m), fully boxed with vertical cell rules. The caption "
               "is a formula fragment ('ε,σ in different environments') with no verb, the "
               "shortest caption in the paper at five words, and it is cited only as 'the "
               "table' - the number is never spoken"),
    table("t4",
          cap("Table 4 Maximum propagation distance r when f =15Hz, P =100w", "Table N",
              position="above"),
          mention(20, first=20, style=["Table 4"], count=0),
          grid(6, 3, header=1, numeric=3, txt=0, units_in_header=True),
          path=P_61, kind="result",
          note="the multi-hop budget: three columns (Number of hops n, Maximum propagation "
               "distance r(km), SNR(dB)) and six body rows for n = 1 to 6, printed with a top "
               "rule, a header rule and a bottom rule plus internal verticals and no side rules. "
               "Units are in the header, the SNR column runs four decimals but the numbers do "
               "not stack because the integer column sets the tab stop. The caption carries a "
               "unit defect that no other caption shares: 'f =15Hz' for a 15 MHz working "
               "frequency, with the M dropped"),
    table("t5",
          cap(CAP_T5, "Table N", position="above"),
          mention(21, first=21, style=["Table 5"], count=1,
                  lead="The following table shows the range of radio broadcasts commonly used to "
                       "take into account ionospheric effects:"),
          grid(5, 2, header=1, numeric=0, txt=2),
          path=P_62, kind="result",
          note="the paper's only grid without a typed header: five rows pairing a frequency "
               "band with a description, separated by horizontal rules with short vertical ticks "
               "at the left of the description column and no outer box. The frequency bands "
               "(2-4, 6-7, 9-11, 13, 15-17 MHz) carry their unit inside the first column, so no "
               "header row is printed and the first band row stands in as the header tier. It is "
               "also the one caption that welds itself to the first body row: the caption "
               "sentence runs straight into '2∼ 4 MHz Tropical frequency, small number of "
               "sunspots and transmission is good.' and the text layer treats the row as part of "
               "the caption"),
]

EXCL = [
    (k, p, b) for k, (p, b) in EXCLUDED.items()
]

ALL = [(k, it) for k, it in [(k, i) for k, i in zip(
    ["abs_f2", "abs_f1", "f1", "f2", "f3a", "f3b", "f3c", "f3d", "f4", "f5", "f6", "f7",
     "f8", "f9", "f10", "f11", "f12", "f13"], FIGURES)]]
ALL += [(k, it) for k, it in zip(["t0", "t1", "t2", "t3", "t4", "t5"], TABLES)]

_order = sorted(ALL, key=lambda kv: (B[kv[0]][0], B[kv[0]][1][1]))
_page_seen = {}
for i, (key, item) in enumerate(_order, 1):
    item["place"]["doc_order"] = i
    pg = item["page"]
    _page_seen[pg] = _page_seen.get(pg, 0) + 1
    item["place"]["page_order"] = _page_seen[pg]

RULES = [
    "The paper spends its figure numbers twice: the abstract prints 'Figure 1 The wave "
    "situation when the wind scale is 6' and 'Figure 2 The relationship between the wind scale "
    "and the first reflection intensity', and the body then opens section 4.1.2 with 'Figure 1 "
    "HF propagation diagram' and 'Figure 2 Inner layers of ionosphere' - four exhibits, two "
    "numbers, and no sentence anywhere reconciles the two runs [caption.numbering].",
    "Numbering carries no punctuation at all: 18 figure captions print 'Figure N' and 5 table "
    "captions print 'Table N', a bare number followed by the title as a noun phrase, with no "
    "colon and no period in either set [caption.numbering].",
    "Caption side is decided by exhibit kind and never varies - all 18 figure rows print their "
    "caption BELOW the artwork and all 5 numbered table rows print theirs ABOVE the grid - so "
    "the single page 16 that carries both kinds shows the rule twice in one column "
    "[caption.position].",
    "Captions are titles, not descriptions: the eighteen numbered figure captions run 5 to 13 "
    "words with a median of 8, the table captions are shorter still (Table 1 four words, Table 3 "
    "five), and the longest title in the paper is the abstract's 13-word 'relationship between "
    "the wind scale and the first reflection intensity' [caption.words].",
    "Only one caption names a plotted symbol, Figure 10's 'P1', and none names an axis "
    "quantity, a unit or a parameter value - so the caption names the exhibit's subject and "
    "the axis titles inside the image carry everything else [caption.variable_count].",
    "No caption concludes anything and none states a direction of change: the reading sentence "
    "lives in the body text instead, and for the two Excel charts the reading sentence is the "
    "only place the trend is stated in words [caption.concludes].",
    "Three-dimensional drawing appears in three exhibits across six measured rows - the "
    "abstract's surface, the four frames of Figure 3 and Figure 13 - and it is always the same "
    "MATLAB surf export, so the paper's 3-D is a surface-height aesthetic, not a scatter of "
    "points in space [geometry.three_d].",
    "Exactly one exhibit carries a colour scale: Figure 13's jet colourbar, which encodes SNR "
    "from -50 to 100. Every other coloured surface in the paper is coloured by height with no "
    "scale printed, so the reader of Figure 3 cannot recover a value from a colour "
    "[geometry.colorbar].",
    "Key placement never leaves the frame: 6 of the 18 figure rows carry a key and every one of "
    "them is inside, always at the upper right for a single frame and at the lower left for a "
    "two-frame pair, while the three pasted Excel charts key as a chip row floating inside the "
    "plot area and the twelve remaining rows - surfaces and schematics - carry no key at all "
    "[geometry.legend].",
    "Panel count follows the comparison being made: 14 rows stand on a single frame and the 4 "
    "two-frame rows are all side-by-side pairs - night vs day, two polarisations, two grazing "
    "angles, sea vs ground - while Figure 3's four frames are measured as four separate rows "
    "because the export left a wide gutter between them, which makes the paper's only 2x2 the "
    "one place where panel_count and doc_order disagree [geometry.panel_count].",
    "Shared axes are used in exactly half the pairs and only where the two frames plot the same "
    "variable on the same range: Figure 2's ionospheric bands share one Height(km) scale and "
    "Figure 5's frames share the 0-90 incident angle, while Figures 8 and 11 keep two "
    "independent y ranges inside one shared x axis - which is the reason Figure 8's y goes 0.97 "
    "to 1 in one frame and 0.84 to 1 in the other without any warning beyond the tick labels "
    "[geometry.shared_axes].",
    "Family follows the drawing tool: the six surface exhibits are all MATLAB surf exports, the "
    "four line rows are MATLAB plot exports, the three bar rows are pasted Excel screenshots "
    "with their data tables burned in, and the five schematics are the paper's only "
    "line-artwork [geometry.family].",
    "Rule style splits by the software that made the grid, not by the data: the four native "
    "Word tables keep booktabs horizontals with internal verticals and no outer box, the two "
    "imported multi-tier grids are fully boxed with a rule at every cell boundary, and no grid "
    "in the paper uses verticals alone [table.rule_style].",
    "Shading happens once, in the uncaptioned notation glossary, and never in a captioned "
    "table - every grid that the paper numbers is flat white [table.zebra].",
    "Merged header cells and a slanted corner appear only in Table 2, the one grid with three "
    "header tiers, so header complexity and the diagonal coincide in a single exhibit "
    "[table.diagonal_header].",
    "Units sit in three different places under one roof: in the header parenthetically where the "
    "grid has a typed header row (Table 3's ε(F/m), Table 4's r(km)), in a dedicated Unit column "
    "where it has a header but no room for the unit (Table 1), and inside the stub cell where "
    "there is no header at all (Table 5's '2-4 MHz'), so 'where the unit goes' tracks the grid's "
    "shape rather than the table's subject [table.units_in_header].",
    "No grid in the paper merges a body cell, continues across a page break, or prints a note "
    "row except the uncaptioned glossary, whose note line is the only sentence any grid prints "
    "under its rule [table.note_sentence].",
    "Announcement is always same-page: all 21 rows that carry a mention have lead_pages 0, so "
    "the paper never names an exhibit on an earlier page than the one it prints on, and the "
    "uncaptioned notation glossary is the only row with no mention at all [mention.lead_pages].",
    "Citations are deixis, not analysis: 21 of the 24 rows are reached by their own printed "
    "number, but the leaning sentence almost never repeats it - the habitual form is 'as "
    "follows:', 'we get the following chart by calculation:', 'The related parameters are shown "
    "in the table.' - and only Figures 7, 12 and 13 get a trail sentence that reads the exhibit "
    "back to the reader [mention.style].",
    "Two exhibits are announced with the wrong kind word or with no number at all: p17 opens "
    "Table 2 with 'The following figure shows the atmospheric noise table' - the paper's only "
    "reader-lead that says 'figure' for a grid - and p18 introduces Table 3 as 'the table' with "
    "no number, so Table 3 is identified only by its caption [mention.lead_sentence].",
    "Placement follows the argument rather than the page: 12 of the 24 rows sit in the middle "
    "band of their page, 8 in the top third and 4 at the foot, and the foot cases are all "
    "figures whose caption closes the page just before the next section heading opens the next "
    "[place.page_zone].",
    "Exhibit density tracks the derivation: the abstract carries 2 rows, the model sections "
    "(4.1-4.4) carry 13, the result sections carry 5, the ground comparison 3, the notation "
    "glossary 1, and the appendix carries only code - which is excluded, not counted as artwork "
    "[place.section_kind].",
]

NOTE = (
    "Thirty-four measured regions resolve to 18 figure rows, 6 table rows and 10 exclusions, "
    "with nothing unaccounted. The exclusions are the display mathematics and the code: "
    "equations (1)-(4) on p9 are four pasted equation images, (7) and (8) on p11 are two more, "
    "(10) on p12 is a pasted body whose number alone stayed in the text layer, (11)-(13) on p12 "
    "are three pasted images inside one measured band, and the last two are the MATLAB code "
    "bands of pp25 and p27. The appendix lists its own source code page after page, and the "
    "same detector reads those monospaced bands as artwork.\n\n"
    "What this paper adds to the lane. (1) It runs the figure numbers twice: the abstract's "
    "Figure 1 and Figure 2 are re-spent by the body's Figure 1 and Figure 2, and both pairs are "
    "real exhibits. (2) The abstract's two exhibits print in reverse order on the page - "
    "Figure 2 above Figure 1 - and the abstract's prose is set in two interleaved columns, so "
    "no lead sentence for either thumbnail survives as a contiguous string; the only readable "
    "lead for the surface is 'we analyze the possible superposition of waves, and get the "
    "three-dimensional simulation diagram of the waves, and simulate it'. (3) The same Excel "
    "chart is printed three times: as the abstract's Figure 2, as Figure 10, and as Figure 12 "
    "with a recast x axis - a duplicate-exhibit pattern no other paper in the batch has shown. "
    "(4) The caption side rule is the cleanest yet: side follows exhibit kind, figures below, "
    "tables above, 23 rows out of 23. (5) The caption numbering is the barest in the batch - "
    "'Figure N' with no colon, no period, and a four-word title in the shortest case ('Table 1 "
    "Related Parameters').\n\n"
    "Defects worth recording. p17 announces Table 2 as 'The following figure shows the "
    "atmospheric noise table' - the wrong exhibit noun. Table 4's caption prints 'f =15Hz' for "
    "a 15 MHz frequency. Table 1 prints 'w' for watts. Figure 4's decomposition tree labels the "
    "ionospheric term 'La' while equation (5) directly above it writes 'Li'. Figure 11's right "
    "frame is titled 'sea surface reflection loss' on a ground-reflection chart, because the "
    "plot was cloned from the sea case and one axis title was never edited. Figure 13's x ticks "
    "print '00' for the leading zero. Figure 12's x axis title sits below its own embedded "
    "data table, detached from the axis. Table 3's caption is a formula fragment with no verb. "
    "And every page carries a red Chinese shop-watermark band that on p19 and p25 crosses the "
    "running header.\n\n"
    "What the record calls a pattern. The drawing pipeline is three tools and the census can "
    "name them: a MATLAB surf/plot export for every numeric exhibit, a pasted Excel screenshot "
    "for every chart that needed a printed table, and hand-drawn line art for every mechanism "
    "schematic. Grid style follows the tool too - native Word tables come out booktabs-like, "
    "imported multi-tier grids come out boxed with merged headers. That is the strongest "
    "tool-to-form coupling in the batch so far: in the earlier papers caption side followed "
    "either the exhibit kind or the part of the paper, here it follows the exhibit kind and the "
    "grid's rule style follows the software.\n\n"
    "Section grammar. Section 4 is where everything is drawn: 13 of the 24 rows live between "
    "4.1 and 4.3, one per modelling step, in the order loss mechanics (Figure 4), geometry "
    "(Figures 5-9), parameters (Table 1), and the first-reflection result (Figure 10). Section "
    "5 re-runs the sea exhibits on ground (Figure 11, Table 3) and section 6 tabulates the "
    "multi-hop budget (Table 4, Figure 13) before recommending frequencies (Table 5). Every "
    "model step gets exactly one exhibit, and the two exhibits that are never announced by a "
    "sentence (Table 1, Table 4) are both parameter sheets rather than findings."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"page": p, "bbox": b, "reason": "not-an-exhibit", "note": k} for k, p, b in EXCL
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
