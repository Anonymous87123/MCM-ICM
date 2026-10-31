"""Hand pass for P-A-2018-76082-bbcfb427 (HF radio propagation over terrains).

25 pages, 18 measured regions: 12 captioned figures, the p4 notation glossary and five MathType
display equations that the region detector reads as graphics.

What the record has to say out loud:

1. Caption side does not vary: all twelve figure captions print below their artwork.
2. The numbering glues the number to the title at both ends of the paper ("Figure1" on p5,
   "Figure6" on p15) and spaces it everywhere else, so a grep for one form misses two exhibits.
3. One caption area carries a prose sentence as well as the printed title, and one figure is
   cited in roman numerals ("Figure VI") three pages later.
4. Figure 9 is never cited by its own number: the sentence printed under its caption says
   "Figure 8", so the last two schematic figures are indistinguishable by reference.
5. Exactly one exhibit is three-dimensional - Figure 3, a flat-shaded MATLAB sea surface with a
   colour-coded height and no colour scale - and it is also the only exhibit in the bottom third
   of a page.
6. The two sensitivity plots print a twelve-entry legend that overflows its frame, and Figure 11's
   legend advertises twelve series for two visible traces while Figure 12's y ticks repeat
   values, so neither axis can be read.

Usage: python -I tools/_dist_paper143.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2018-76082-bbcfb427"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    "f1": (5, [80.2, 209.8, 526.1, 429.6]),
    "f2": (9, [105.0, 85.8, 477.2, 294.4]),
    "f3": (9, [166.2, 531.7, 430.8, 720.7]),
    "f4": (10, [174.2, 253.6, 425.5, 428.8]),
    "f5": (11, [109.0, 158.0, 485.0, 356.0]),
    "f6": (15, [75.0, 64.8, 521.2, 250.8]),
    "f7": (16, [114.7, 113.8, 480.5, 328.3]),
    "f8": (17, [157.6, 143.3, 425.3, 347.3]),
    "f9": (18, [111.8, 74.8, 477.8, 300.0]),
    "f10": (19, [173.0, 351.8, 411.8, 532.4]),
    "f11": (20, [84.2, 352.2, 513.4, 584.4]),
    "f12": (21, [75.8, 82.4, 513.2, 319.4]),
    "t1": (4, [66.2, 121.0, 479.2, 472.9]),
}

EXCLUDED = {
    "p8 equation (11)": (8, [299.6, 585.0, 387.4, 629.9]),
    "p8 equation (12)": (8, [296.8, 646.9, 392.5, 691.8]),
    "p12 equation (18)": (12, [130.0, 286.4, 563.4, 327.0]),
    "p12 equation (19)": (12, [172.0, 409.2, 544.0, 455.8]),
    "p12 equation (20)": (12, [72.7, 564.5, 518.9, 695.0]),
}

for _name, (_p, _b) in {**B, **EXCLUDED}.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 18, len(MEASURED)

S = {
    "intro": "1 Introduction",
    "notations": "1.2 Notations",
    "sky": "3 Skywave basic transmission loss",
    "loss": "3.1 Loss model",
    "refl": "4 The Mathematical Model of Ocean signal’s Reflection",
    "basic": "4.1 Basic model",
    "fresnel": "4.1.2 Fresnel reflection coefficient of Sea",
    "ground": "5 The comparison of Ground Signal Transmission and Sea",
    "gmodel": "5.1 The mathematical model of ground signal reflection",
    "mountain": "5.1.2 Shortwave sky wave in mountainous terrain transmission loss",
    "compare": "5.2 Comparing results",
    "ship": "6 The communication model of marine ship receiver",
    "rocks": "6.1 The model of ship rocks",
    "sway": "6.2 Sea signal transmission model of combining ship swaying",
    "hop": "6.3 The same multi-hop path to maintain communication time",
    "sens": "7 Sensitivity Analysis-Time factor",
}


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


def cap(v: str, numbering: str = "Figure N", *, position: str = "below") -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)) if v else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": position,
    }


NOCAP = cap("", "none")


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
        labels: bool = False, three_d: str = "no", colorbar: bool = False) -> dict:
    return {
        "family": family,
        "panel_count": 1,
        "panel_layout": "1",
        "shared_axes": False,
        "legend": legend,
        "colorbar": colorbar,
        "three_d": three_d,
        "printed_numbers": numbers,
        "data_labels": labels,
    }


def figure(key: str, family: str, caption: dict, men: dict, geom: dict, *,
           path: list[str], kind: str, note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "is_panel_of": "",
        "caption_verbatim": caption["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }


FIGURES = [
    figure("f1", "flowchart-or-schematic",
           cap("Figure1 Signal transmission diagram", "Figure N"),
           mention(5, first=5, style=["figure 1"], pattern="direct",
                   lead="we give the figure 1 about a simple representation of its jumping process"),
           geo("flowchart-or-schematic", numbers=False),
           path=[S["sky"], S["loss"]], kind="model",
           note="the paper's opening exhibit and its only free-standing line drawing with angled "
                "labels: a side elevation of one skywave hop, transmitter at the left and receiver "
                "at the right, a hatched vertical column standing in for the reflecting layer, "
                "with the symbolic labels d1, d2, h>0, θ>0, θ1 and θ2. No axes, no scale, no "
                "arrowheads on the rays; the hatched column is cut off flat at the figure's lower "
                "edge, so the layer has no base line. The theta glyphs print as a partial symbol "
                "at page size and the caption's number is glued to the word"),
    figure("f2", "line",
           cap("Figure 2 power reflection coefficient and the grazing incidence angle."),
           mention(9, first=8, style=["Figure 2"], pattern="as-shown-in",
                   lead="The curve in Figure 2 reflects the relationship between the power "
                        "reflection coefficient"),
           geo("line", legend="inside", numbers=True),
           path=[S["refl"], S["basic"], S["fresnel"]], kind="model",
           note="a MATLAB line plot pasted small: three frequency curves in grey dash-dot, black "
                "solid and red dash-dot, boxed frame, axis titles 'Grazing incidence angle/rad' "
                "and 'Power reflection coefficient', with a three-entry legend inside at upper "
                "right reading 2MHz, 5MHz and 3MHz - not in numerical order, and sub-readable at "
                "print size. The plot also carries its own title inside the frame that repeats "
                "what the caption says below, so the exhibit is titled twice"),
    figure("f3", "surface-or-3D",
           cap("Figure 3 ocean wave diagram"),
           mention(9, first=9, style=["Figure 3"], pattern="figure-n-shows",
                   lead="Figure 3 is our simulation of the waves."),
           geo("surface-or-3D", numbers=True, three_d="surface-mesh"),
           path=[S["refl"], S["basic"], S["fresnel"]], kind="model",
           note="the paper's only three-dimensional exhibit: a MATLAB sea surface, flat-shaded and "
                "colour-coded by height in cyan through yellow to orange, with no wireframe edges "
                "and no colour scale printed anywhere. Three axes, each 0-200 by 50 for x and y and "
                "0-8 by 2 for z, inside a dotted 3-D box, and not one axis title. The spikes "
                "overshoot the top of the z box, the two front corners are empty white, and the "
                "image was pasted small enough that the pixels are visibly aliased"),
    figure("f4", "line",
           cap("Figure 4 Wave spectrum"),
           mention(10, first=10, style=["Figure 4", "figure 4"], pattern="figure-n-shows",
                   lead="Figure 4 describes the spectrum with the wind speed changes:",
                   trail="From figure 4 we conclude that wind speed is a major factor affecting "
                         "the frequency of"),
           geo("line", legend="inside", numbers=True),
           path=[S["refl"], S["basic"], S["fresnel"]], kind="model",
           note="three wind-speed spectra in blue, red and yellow with a three-entry inside legend "
                "reading 10m/s, 12m/s and 15m/s, axis titles 'ω(rad/s)' and 'S(ω²s)'. Boxed frame, "
                "x 0 to 2 by 0.2, y 0 to 4 by 0.5. The upper half of the plot area is empty, both "
                "small-amplitude curves hug the baseline, the y unit string is unreadable at print "
                "size, and the x-axis title sits hard against the caption below it with no gap"),
    figure("f5", "line",
           cap("Figure 5 Relationship between wind speed and power reflection coefficient"),
           mention(11, first=11, style=["Figure 5"], pattern="figure-n-shows",
                   lead="Figure 5 shows the effect of wind speed on the roughness correction "
                        "factor.",
                   trail="Figure 5 shows that when the wind speed exceeds a certain level, the "
                         "roughness"),
           geo("line", legend="inside", numbers=True),
           path=[S["refl"], S["basic"], S["fresnel"]], kind="model",
           note="three frequency curves in black solid, blue dashed and red dash-dot against wind "
                "speed, with an inside legend reading 5MHz, 10MHz and 20MHz. The caption calls the "
                "ordinate a power reflection coefficient while the sentence above the figure calls "
                "it a roughness correction factor, and the in-frame title uses a third wording, so "
                "one exhibit carries three names. Tick decimals drop out at print size (02 for "
                "0.2) and all three curves overlap near 0.8 for the first 6 m/s"),
    figure("f6", "flowchart-or-schematic",
           cap("Figure6 Double-edged peak diffration", "Figure N"),
           mention(15, first=14, style=["Figure 6", "Figure VI"], pattern="figure-n-shows",
                   lead="Figure 6 is a schematic of the Epstein-Peterson method."),
           geo("flowchart-or-schematic", numbers=False),
           path=[S["ground"], S["gmodel"], S["mountain"]], kind="model",
           note="two-peak terrain profile drawn inside a dashed rectangle with the four diffraction "
                "ray lengths as solid and dashed lines and the peak heights marked h1, h1'. The only "
                "axis words anywhere in the paper's schematics - 'height' rotated at the left and "
                "'distance' centred below - and still no ticks, no scale and no arrowheads. "
                "Announced one page earlier as 'a schematic of the Epstein-Peterson method' and "
                "captioned as a double-edged peak, then cited again on p15 as 'Figure VI'"),
    figure("f7", "bar",
           cap("Figure 7 Loss comparison chart"),
           mention(16, first=16, style=["Figure 7"], pattern="as-shown-in",
                   lead="as shown in Figure 7"),
           geo("bar", numbers=True, labels=True),
           path=[S["ground"], S["compare"]], kind="result",
           note="the paper's only bar chart and its only exhibit with data labels: four bars for "
                "mountainous terrain, smooth terrain, turbulent ocean and calm ocean, printed "
                "12.1084, 9.1133, 2.855 and 0.9637 dB. Light grey on white with a thin grey frame, "
                "y titled only 'dB', no x-axis title, no legend, and every bar value printed to four "
                "decimals although the axis ticks are whole numbers. Two data labels float clear of "
                "their bars"),
    figure("f8", "flowchart-or-schematic",
           cap("Figure 8 Boat and antenna schematic"),
           mention(17, first=17, style=["Figure 8"], pattern="as-shown-in",
                   lead="As shown in Figure 8, we create a spherical reference frame that is the "
                        "center of the Earth."),
           geo("flowchart-or-schematic", numbers=False),
           path=[S["ship"], S["rocks"]], kind="model",
           note="boat silhouette with an antenna mast and a three-arrow x/y/z triad, no frame, no "
                "numbers, no labels other than the three axis letters. The sentence that introduces "
                "it promises a spherical reference frame centred on the Earth, but no sphere and no "
                "curvature is drawn - the exhibit the prose describes is not the exhibit on the page"),
    figure("f9", "flowchart-or-schematic",
           cap("Figure 9 Radio waves environment propagation model"),
           mention(18, first=18, style=["Figure 8"], pattern="as-shown-in",
                   lead="Radio waves at sea environment propagation model shown in Figure 8[15]."),
           geo("flowchart-or-schematic", numbers=False),
           path=[S["ship"], S["sway"]], kind="model",
           note="the curved-earth propagation diagram: transmitter T at the left, receivers RA, RB "
                "and RC along an earth arc of radius Re, with four ray paths labelled A/d1, B/d2, "
                "C/d3 and the refracted heights Hr and Hr' crowded along the top arc. No frame, no "
                "axes, no numbers. The only sentence printed under its caption cites it as "
                "'Figure 8', so the paper's fifteenth-region schematic is never named by its own "
                "number"),
    figure("f10", "flowchart-or-schematic",
           cap("Figure 10 Ionospheric reflection wave schematic"),
           mention(19, first=19, style=["Figure 10"], pattern="as-shown-in",
                   lead="Its schematic diagram is shown in Figure 10."),
           geo("flowchart-or-schematic", numbers=False),
           path=[S["ship"], S["hop"]], kind="other",
           note="four ionospheric return curves f1 to f4 in blue, each reaching the sea at a "
                "different range, enclosed by a dashed envelope which is the only labelled thing on "
                "the exhibit: an in-figure note reading 'Glide spread' on a leader line. No frame, "
                "no axes, no numbers, no drawn sea line, and an unlabelled upward arrow at the top "
                "left. Curves cross each other with no annotation"),
    figure("f11", "line",
           cap("Figure 11 Sensitivity of time (for signal-noise)"),
           mention(20, first=20, style=[], pattern="direct",
                   lead="The sensitivity of time by calculation is obtained, as shown in the "
                        "following figures."),
           geo("line", legend="outside-right", numbers=True),
           path=[S["sens"]], kind="sensitivity",
           note="a MATLAB boxed plot with inward ticks on all four sides, y titled "
                "'SIGNAL-NOISE RATIO(dB)' from -10 to 50 and x titled 'Grazing incidence(angle)' "
                "from 0 to 80. Its outside-right legend lists twelve entries from t=0 to t=22 and "
                "overflows the frame, yet only two traces are distinguishable, so the legend "
                "promises twelve series that print as two asymptotes. The in-frame title runs three "
                "quantities together in one string"),
    figure("f12", "line",
           cap("Figure 12 Sensitivity of time (for ionospheric loss)"),
           mention(21, first=20, style=[], pattern="direct",
                   lead="The sensitivity of time by calculation is obtained, as shown in the "
                        "following figures."),
           geo("line", legend="outside-right", numbers=True),
           path=[S["sens"]], kind="sensitivity",
           note="the ionospheric partner of Figure 11: twelve time curves from t=0 to t=22, the "
                "same overflowing outside-right legend and the same run-on in-frame title, y titled "
                "'Ionospheric loss(dB)'. Its y axis is its own defect - the ticks run 1.6582 to "
                "1.6586 on a step of about 0.00006 printed to four decimals, so adjacent labels "
                "repeat (1.6582 twice, 1.6583 twice) and the axis shows no usable scale. Thin light "
                "curves crowd the baseline and cross near x = 10 to 20"),
]

TABLES = [
    {
        "page": B["t1"][0],
        "bbox": B["t1"][1],
        "caption_verbatim": "",
        "caption_source": "none",
        "note": "the paper's only grid and its only uncaptioned exhibit: a two-column symbol "
                "glossary under '1.2 Notations', fifteen body rows from the sea-water dielectric "
                "constant to the extra system loss, symbol column in italic math and definition "
                "column in roman. Announced by the sentence 'Let's first define the list of "
                "notations used in this article:' and given no label, no number and no note line "
                "of any kind - the paper counts its figures to twelve and its tables not at all",
        "place": place(B["t1"][0], B["t1"][1], [S["intro"], S["notations"]], "symbols"),
        "mention": mention(4, first=4, style=[], pattern="direct",
                           lead="Let's first define the list of notations used in this article:"),
        "caption": NOCAP,
        "table": {
            "rows": 15,
            "cols": 2,
            "header_rows": 1,
            "rule_style": "vertical-rules",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": 0,
            "text_cols": 2,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    },
]

EXCLUDED_REGIONS = [
    {"page": p, "bbox": b, "reason": "not-an-exhibit",
     "note": n + " - a MathType display equation, not a figure"}
    for n, (p, b) in EXCLUDED.items()
]

RULES = [
    "All twelve figure captions print BELOW their artwork and not one prints above, so this paper "
    "sits with the below-caption majority of the lane at every page of the body [caption.position].",
    "The numbering glues the number to the title at both ends of the paper - 'Figure1' on p5 and "
    "'Figure6' on p15 - and spaces it in the ten between, so the paper uses two numbering forms "
    "for one run of twelve [caption.numbering].",
    "Captions are 4 to 10 words, almost all bare noun phrases ('Wave spectrum', 'Loss comparison "
    "chart', 'Boat and antenna schematic'), and not one names a unit, a variable or a condition or "
    "states a result [caption.words].",
    "One caption slot carries a prose sentence as well as the title: 'Figure 3 is our simulation of "
    "the waves.' prints above the printed caption, so the same figure is announced, titled and "
    "captioned in three consecutive lines [caption.verbatim].",
    "One caption misspells its own subject and prints that way: 'Double-edged peak diffration' for "
    "diffraction, on the same line as the glued number 'Figure6' [caption.words].",
    "One figure is cited in roman numerals three pages after its arabic citation: 'Figure 6 is a "
    "schematic of the Epstein-Peterson method' on p14 against 'The meaning of the parameters in "
    "the formula refer to Figure VI' on p15 [mention.style].",
    "Figure 9 is never cited by its own number: the only sentence printed under its caption says "
    "'shown in Figure 8[15]', which is the same sentence already used for Figure 8 a page earlier, "
    "so two consecutive schematics share one reference [mention.style].",
    "A figure is announced as one thing and captioned as another: p14 calls Figure 6 a schematic "
    "of the Epstein-Peterson method while its caption reads 'Double-edged peak diffration' "
    "[mention.lead_sentence].",
    "References split into a subject-first grammar ('Figure 4 describes', 'Figure 5 shows', 'Figure "
    "6 is') and a passive one ('as shown in Figure 7', 'shown in Figure 10'), with two exhibits - "
    "Figures 11 and 12 - announced only by the plural deictic 'as shown in the following figures' "
    "[mention.lead_pattern].",
    "Three references displace by exactly one page - Figure 2 cited on p8 for p9, Figure 6 cited on "
    "p14 for p15, and Figure 12 announced on p20 inside the plural 'following figures' for p21 - "
    "and the other nine are local, so the paper never displaces a reference by more than one page "
    "[mention.lead_pages].",
    "The exhibit inventory is 5 schematics, 5 line plots, 1 bar chart and 1 surface, so drawings "
    "and plots are balanced and neither form dominates [geometry.family].",
    "Exactly one exhibit is three-dimensional: Figure 3's sea surface, flat-shaded and colour-coded "
    "by height with no wireframe and no colour scale, printed as a perspective box [geometry.three_d].",
    "The only colour scale in the paper is that unlabelled height shading - no exhibit carries a "
    "colourbar, so the surface's colours are decorative rather than readable [geometry.colorbar].",
    "Legends appear on five of the twelve figures and never outside the plot except on the "
    "sensitivity pair: inside at upper right on Figures 2, 4 and 5, and outside-right on Figures 11 "
    "and 12 where the twelve-entry box overflows the frame [geometry.legend].",
    "The sensitivity pair fails at exactly the point where the legend matters: Figure 11's legend "
    "lists twelve series from t=0 to t=22 while only two traces can be told apart, so the key "
    "cannot be matched to the ink [geometry.legend].",
    "Figure 12's y axis has no usable scale - ticks from 1.6582 to 1.6586 printed to four decimals "
    "on a step near 0.00006 make adjacent labels identical - while its partner Figure 11 prints a "
    "coarse -10 to 50 axis, so a caller comparing them compares a readable and an unreadable "
    "ordinand [geometry.printed_numbers].",
    "The four drawn schematics and the two terrain drawings carry no numbers at all, and only "
    "Figure 6 prints axis words ('height', 'distance'), so in this paper a schematic is identified "
    "by its absence of scale rather than by its content [geometry.printed_numbers].",
    "Five of the twelve carry a printed in-frame title above the plot as well as a caption below it, "
    "and the two disagree often enough to matter: Figure 5's frame names a frequency curve, its "
    "caption names a reflection coefficient and the sentence above it names a roughness factor "
    "[geometry.data_labels].",
    "The single grid is the notation glossary on p4: two columns, fifteen rows, announced by a "
    "sentence that ends in a colon and followed by no label at all, so the paper's only table is "
    "also its only unnumbered exhibit [mention.lead_pattern].",
    "The glossary's rule style is the paper's only one - rules above and below the header and a "
    "closing rule at the foot, with a single vertical rule between the symbol and definition "
    "columns and no side rules - so the grid is booktabs plus one internal vertical [table.rule_style].",
    "No shading, no merged cell, no two-tier header, no unit in the header, no note line and no "
    "continuation: the glossary is as plain as a grid can be, and the italic symbol column is the "
    "only typographic signal in the paper's tables [table.zebra].",
    "Five of the eighteen measured regions are not exhibits at all but MathType display equations "
    "pasted as graphics (11 and 12 on p8, 18 to 20 on p12), so the region detector counts inline "
    "mathematics as artwork on this paper [place.doc_order].",
    "Exhibit size runs the other way from importance: the notation glossary at 0.29 of a page is "
    "the largest object in the paper, the twelve figures run 0.086 to 0.21, and the only "
    "three-dimensional exhibit, the surface, is the third smallest at 0.10 [place.area_frac].",
    "Seven of the twelve figures print in the top third of their page and only one prints in the "
    "bottom third - Figure 3, the surface - so the page rhythm is a figure at the head followed by "
    "its discussion below it [place.page_zone].",
]

NOTE = (
    "A 25-page HF-propagation modelling paper whose exhibit set is balanced between drawings and "
    "plots: five schematics (the hop, the two-peak terrain, the boat, the curved-earth model and "
    "the ionospheric fan), five line plots, one bar chart and exactly one three-dimensional "
    "surface. Every caption prints below its artwork, numbering is 'Figure N' except at both ends "
    "of the paper where the number is glued to the word ('Figure1', 'Figure6'), and one figure is "
    "cited in roman numerals as 'Figure VI'. Reference hygiene is the weak point: Figure 9 is only "
    "ever cited as 'Figure 8', Figure 6 is announced as one schematic and captioned as another, "
    "and Figures 11 and 12 are announced together by the plural deictic 'as shown in the following "
    "figures'. The only table is an uncaptioned, unnumbered two-column notation glossary whose "
    "verticals are the paper's only vertical rules. Five measured regions are display equations "
    "pasted as MathType images rather than exhibits, and the paper's most ambitious figure - the "
    "MATLAB sea surface - prints with no axis titles and no colour scale."
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
    "t1": 1, "f1": 2, "f2": 3, "f3": 4, "f4": 5, "f5": 6, "f6": 7,
    "f7": 8, "f8": 9, "f9": 10, "f10": 11, "f11": 12, "f12": 13,
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
    print("legend", dict(Counter(e["geometry"]["legend"] for e in FIGURES)))
    print("three_d", dict(Counter(e["geometry"]["three_d"] for e in FIGURES)))
    print("cap.words", [e["caption"]["words"] for e in exhibits])
    print("men.first", dict(Counter(e["mention"]["first_page"] for e in exhibits)))
    print("men.lead", dict(Counter(e["mention"]["lead_pages"] for e in exhibits)))
    print("area", [e["place"]["area_frac"] for e in exhibits])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
