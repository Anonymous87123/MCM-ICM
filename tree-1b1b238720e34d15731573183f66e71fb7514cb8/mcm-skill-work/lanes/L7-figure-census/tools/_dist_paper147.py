"""Hand pass for P-A-2018-88255-2023cf14 (2018 MCM A, "Team #88255", HF radio hop budget).

21 pages, 35 measured regions on 16 pages (pp4-19). Resolution: 20 exhibit rows (17 numbered
figures, two of which are split across two measured regions because the export left a gutter
between the panels, plus one table) and 15 exclusions.

The exclusions are of four kinds and they are worth naming because this paper is the first in
the batch that mixes them all inside one document:

* pasted display mathematics - 8 regions (the Fresnel pair on p5, eq (5)-(6) on p6, (9)-(13) on
  p8, (14)-(15) on p9, (16)-(19) on p11, (22)-(23) on p12, the attenuation factor on p13 and
  (25) on p13 again). Every one of them is an embedded image; the prose around them is live
  text, so a reader can search the sentences and never the formulas.
* a raster duplicate of one of those blocks (p5 r3 sits inside p5 r2 and prints the same
  Fresnel pair).
* a running-header band the detector boxed as a region (p5 r1: "Team #88255 / Page 5 of 20",
  the heading "2.2 Variable Description" and the double rules over the table).
* two kinds of plot duplication: on p8 the raster interior of a vector figure frame, and on
  pp18-19 the same figure measured twice, once as the vector frame and once as the raster it
  contains.

Usage: python -I tools/_dist_paper147.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2018-88255-2023cf14"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}


def _snap(page: int, bbox: list[float]) -> list[float]:
    """The constant tables below trim bboxes to one decimal; replace them by the measured box."""
    near = [(sum(abs(a - b) for a, b in zip(box, bbox)), list(box))
            for p, box in MEASURED if p == page]
    dist, exact = min(near, key=lambda kv: kv[0])
    assert dist < 0.5, f"no measured region near {bbox} on page {page}"
    return exact


def _used(bbox: list[float], page: int) -> bool:
    return any(p == page and all(abs(a - b) <= 0.06 for a, b in zip(box, bbox))
               for p, box in MEASURED)


B = {
    "f1": (4, [134.2, 240.4, 484.9, 381.0]),
    "f2": (6, [177.2, 313.7, 438.1, 506.0]),
    "f3": (7, [92.0, 451.8, 503.6, 664.9]),
    "f4": (8, [125.2, 77.8, 468.3, 260.4]),
    "f5a": (9, [151.2, 466.3, 284.8, 635.3]),
    "f5b": (9, [315.6, 466.3, 449.5, 635.3]),
    "f6": (10, [174.2, 74.9, 423.4, 274.4]),
    "f7": (10, [161.9, 435.7, 425.4, 641.4]),
    "f8": (11, [190.2, 580.1, 447.4, 783.2]),
    "f9": (13, [194.9, 63.0, 422.8, 288.2]),
    "f10": (14, [179.2, 533.6, 424.0, 734.4]),
    "t1": (15, [67.9, 291.7, 527.8, 388.1]),
    "f11": (15, [181.4, 565.7, 428.0, 757.3]),
    "f12l": (16, [80.4, 133.1, 257.2, 262.2]),
    "f12r": (16, [287.5, 132.5, 469.6, 272.9]),
    "f13": (17, [189.5, 75.0, 424.4, 259.8]),
    "f14": (17, [129.6, 368.4, 460.1, 398.4]),
    "f15": (18, [192.6, 76.2, 432.0, 274.1]),
    "f16": (18, [178.2, 434.9, 420.3, 630.1]),
    "f17": (19, [182.0, 76.2, 421.5, 274.1]),
}

EXCLUDED = {
    "p5 running-header and glossary rule band": (5, [66.6, 57.2, 528.8, 105.2], "rule"),
    "p5 Fresnel coefficient pair (2)": (5, [261.5, 677.9, 362.6, 751.1], "not-an-exhibit"),
    "p5 raster copy of the Fresnel pair": (5, [264.1, 716.0, 363.4, 755.3], "duplicate"),
    "p6 equations (5) and (6)": (6, [290.0, 634.6, 364.0, 705.0], "not-an-exhibit"),
    "p8 raster interior of Figure 4": (8, [196.0, 127.2, 401.9, 258.2], "fragment-of-other"),
    "p8 caption band of Figure 4": (8, [174.2, 225.6, 474.4, 276.5], "caption-background"),
    "p8 equations (9) to (13)": (8, [56.5, 660.4, 536.3, 803.8], "not-an-exhibit"),
    "p9 equations (14) and (15) inside prose": (9, [61.2, 134.2, 540.5, 304.3],
                                                "not-an-exhibit"),
    "p11 equations (16) to (19)": (11, [32.8, 292.4, 526.8, 511.4], "not-an-exhibit"),
    "p12 equations (22) and (23)": (12, [123.6, 352.7, 525.4, 447.8], "not-an-exhibit"),
    "p13 attenuation-factor equation": (13, [247.6, 582.0, 381.2, 611.8], "not-an-exhibit"),
    "p13 equation (25)": (13, [182.8, 680.9, 519.0, 728.0], "not-an-exhibit"),
    "p18 raster copy of Figure 15": (18, [182.0, 93.4, 418.0, 265.2], "duplicate"),
    "p18 raster copy of Figure 16": (18, [185.6, 455.2, 420.4, 618.7], "duplicate"),
    "p19 raster copy of Figure 17": (19, [172.0, 91.3, 421.6, 265.3], "duplicate"),
}

B = {k: (pg, _snap(pg, bb)) for k, (pg, bb) in B.items()}
EXCLUDED = {k: (pg, _snap(pg, bb), why) for k, (pg, bb, why) in EXCLUDED.items()}

for _name, (_p, _b, _r) in EXCLUDED.items():
    assert _used(_b, _p), f"{_name} bbox is not a measured region"
for _name, (_p, _b) in B.items():
    assert _used(_b, _p), f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 35, len(MEASURED)


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


P_INTRO = ["1 Introductions"]
P_312 = ["3 Model Establishment and Analysis", "3.1 Ocean Surface Reflection Attenuation",
         "3.1.2 Calm Oceans Reflection"]
P_3131 = ["3 Model Establishment and Analysis", "3.1 Ocean Surface Reflection Attenuation",
          "3.1.3 Turbulent Oceans Reflection",
          "3.1.3.1 The Sea Surface Simulation By P-M Spectrum"]
P_3132 = ["3 Model Establishment and Analysis", "3.1 Ocean Surface Reflection Attenuation",
          "3.1.3 Turbulent Oceans Reflection", "3.1.3.2 Finite Element Analysis on Rough Surface"]
P_314 = ["3 Model Establishment and Analysis", "3.1 Ocean Surface Reflection Attenuation"]
P_321 = ["3 Model Establishment and Analysis", "3.2 The Maximum Number of Hops",
         "3.2.1 Free Space Transmission Loss and Path Transmission Loss"]
P_3221 = ["3 Model Establishment and Analysis", "3.2 The Maximum Number of Hops",
          "3.2.2 The Properties of Ionosphere Reflection", "3.2.2.1 Physical Properties of "
          "Ionosphere"]
P_323 = ["3 Model Establishment and Analysis", "3.2 The Maximum Number of Hops",
         "3.2.3 The Calculation of Maximum Hops"]
P_33 = ["3 Model Establishment and Analysis", "3.3 The Reflection Loss of rugged and smooth "
        "terrain"]
P_342 = ["3 Model Establishment and Analysis", "3.4 Model Improvement About Shipboard Receiver",
         "3.4.2 The Range of The Communication Area of The Same Multi-Hop"]
P_4 = ["4 Stability and Sensitivity Analysis"]

CAP_F5 = ("Figure 5: the relationship between Lcal or Ltur and θ on calm surface versus tough "
          "surface, f=3MHz")
CAP_F10 = ("Figure 10: The relationship between distance (km) and the total loss Lt (dB) "
           "n: number of hops, f = 3MHz, reflected by calm oceans")
CAP_F12 = ("Figure 12: The relationship between distance (km) and the total loss Lt (dB) "
           "n : number of hops, f = 3MHz, reflected by smooth (left) and rugged (right) terrain")
CAP_F13 = ("Figure 13: The multi-hop signal received by the shipboard receiver "
           "n : number of hops, f = 3MHz, reflected by turbulent ocean")

FIGURES = [
    figure("f1",
           cap("Figure 1: Propagation path of sky wave"),
           mention(4, first=4, style=["Figure 1"], count=1,
                   lead="figure 1 displays the progress.", pattern="direct"),
           geo("flowchart-or-schematic", numbers=False),
           path=P_INTRO, kind="introduction",
           note="a drawn propagation scheme, not a plot: a blue Earth hemisphere, three dashed "
                "concentric arcs standing for the ionosphere, one orange and one green ray path "
                "meeting at an apex, a vertical dimension h and an elevation angle θ, and two "
                "surface marks x1 and x2 where the rays touch. No axes, no scale, no key, no "
                "layer names - the arcs are unlabelled, so the figure says 'multi-hop' without "
                "saying at which layers"),
    figure("f2",
           cap("Figure 2: The reflection process in the ionosphere"),
           mention(6, first=None, style=["Figure 2"], count=0),
           geo("flowchart-or-schematic", numbers=False),
           path=P_312, kind="model",
           note="the paper's second pure schematic and the geometric twin of Figure 1: a blue "
                "Earth arc, four dashed concentric ionospheric arcs, a ray fan issuing from the "
                "Earth's centre with R and Z marked, θ0 at the surface and a chain θ1, θ2 ... θn "
                "at each hop, plus θmax on the tangent ray. No axes and no numbers. The label "
                "chain silently reuses θ for two different quantities - the incidence angle at "
                "the surface and the refraction angle inside each layer - which is exactly the "
                "confusion equations (4)-(7) are written to resolve. Never cited in the body"),
    figure("f3",
           cap("Figure 3: the ocean wave simulated by P-M spectrum (wind speed=5, 10, 15 and "
               "20 m/s)", conditions=True),
           mention(7, first=6, style=["Figure 3"], count=1,
                   lead="Figure 3 display the wave simulation distributed by P-M spectrum"),
           geo("surface-or-3D", three_d="surface-mesh", panels=4, layout="2x2"),
           path=P_3131, kind="model",
           note="the paper's only three-dimensional exhibit: four MATLAB surf panels in a 2x2 "
                "grid, one per wind speed (5, 10, 15, 20 m/s), each a shaded surface with mesh "
                "lines and its own z scale, x and y titled '[m]' over 0-300 and 0-250. No "
                "colourbar, no panel letters, no shared axes - the wind speed survives only "
                "inside each rotated z-axis label, so the panel order is not stated anywhere. "
                "The caption announces a simulation and the plot delivers no numbers at all"),
    figure("f4",
           cap("Figure 4: the reflection forms on the turbulent surface"),
           mention(8, first=7, style=["Figure 4"], count=1,
                   lead="Figure 4 shows the reflection properties:",
                   pattern="figure-n-shows"),
           geo("flowchart-or-schematic", numbers=False),
           path=P_3132, kind="model",
           note="the diffuse-reflection construction behind Blinn's microplane model: parallel "
                "incident rays from the upper left strike a thick wavy surface profile, and "
                "dashed reflected rays leave at mismatched angles, several of them ending in "
                "arrows that point nowhere. No axes, no key, no labels, no normal vectors drawn "
                "even though normal-vector distribution is the whole subject of the section. The "
                "detector inside this exhibit measured four regions (frame, raster interior, "
                "caption band, and the equation block below)"),
    figure("f5a",
           cap(CAP_F5, variables=4, conditions=True),
           mention(9, first=9, style=["Figure 5"], count=3,
                   lead="figure 5 shows the relationship between the angle if incidence",
                   pattern="figure-n-shows",
                   trail="From figure 5 we can find that on the calm surface, no matter what "
                         "angle of incidence"),
           geo("line", numbers=True),
           path=P_314, kind="model",
           note="left panel of Figure 5 and the paper's only pair whose panels are titled from "
                "inside the axes: a bold italic 'calm surface' sits at the top of the frame, and "
                "the key is replaced by that title. x 'angle of incidence (°)' 0-90, y "
                "'attenuation (dB)' 0-0.12, a single red curve that stays under 0.04 dB for "
                "every angle. The two panels are on different y scales by two orders of "
                "magnitude, which is the figure's entire point and is stated only by the tick "
                "labels"),
    figure("f5b",
           cap(CAP_F5, variables=4, conditions=True),
           mention(9, first=9, style=["Figure 5"], count=3,
                   lead="figure 5 shows the relationship between the angle if incidence",
                   pattern="figure-n-shows",
                   trail="From figure 5 we can find that on the calm surface, no matter what "
                         "angle of incidence"),
           geo("line", numbers=True),
           path=P_314, kind="model",
           note="right panel of Figure 5, titled 'tough surface' inside the frame: y "
                "'attenuation (dB)' 0-12, one blue curve rising monotonically to 10.6 dB at "
                "grazing incidence, the number the body then quotes as 10.578 dB. The caption "
                "calls the surface 'tough' while the section heading calls it 'Turbulent' and "
                "the record's own symbol set writes Ltur. Two measured regions, one caption, no "
                "panel letters"),
    figure("f6",
           cap("Figure 6：The relationship between Lcal or Ltur and f on calm surface versus "
               "tough surface", "Figure N", variables=3, conditions=True),
           mention(10, first=10, style=["Figure 6"], count=1,
                   trail="From Figure 6 we can find that no matter what frequency it is, the "
                         "attenuation on calm surface are almost invariable and very small"),
           geo("line", legend="inside"),
           path=P_314, kind="model",
           note="the frequency twin of Figure 5, plotted in one frame instead of two: red flat "
                "trace and blue rising trace, x 'frequency(MHz)' 0-30, y 'attenuation(dB)' 0-4.5, "
                "key inside the upper right. This is the paper's only caption printed with a "
                "full-width colon - 'Figure 6：The relationship' - which is why the numbering "
                "field records the bare 'Figure N' form and the note carries the punctuation. "
                "The key names the series 'calm surface' / 'tough surface' while the caption "
                "names them Lcal and Ltur, so the figure and its title do not share a vocabulary"),
    figure("f7",
           cap("Figure 7: the comparison of reflected power between calm and turbulent ocean"),
           mention(10, first=10, style=["Figure 7"], count=1,
                   lead="As shown in the figure 7, the signal strength decreases as the frequency "
                        "increases.",
                   pattern="as-shown-in"),
           geo("line", legend="inside"),
           path=P_314, kind="model",
           note="received power against frequency for the two sea states: x 'frequence / (Hz)' "
                "0-30 and y 'power / (mW)' 0-7, two decaying traces, key inside the upper right "
                "reading 'clam oceean' and 'turbulent ocean'. Two unit defects in one axis title "
                "- 'frequence' for frequency and 'Hz' for a 3-30 MHz band - plus the double typo "
                "in the key. The body reads the exhibit as 0.5-5.5 mW calm and 0.2-2.5 mW "
                "turbulent"),
    figure("f8",
           cap("Figure 8: The relationship between Lbf (dB) and distance (km), f=3, 12, 21, "
               "30MHz", variables=1, conditions=True),
           mention(11, first=11, style=["Figure 8"], count=1,
                   lead="So, when double the radio frequency or propagation distance, the free "
                        "space transmission loss will be increased by 6dB.",
                   trail="Figure 8 shows the relationship between transmission distance and "
                         "attenuation Lbf, on different frequencies."),
           geo("line", legend="inside"),
           path=P_321, kind="model",
           note="free-space loss against distance for four frequencies: x 'distance(km)' 0-10000 "
                "in 2000 steps, y 'attenuation(dB)' 80-150, four curves keyed inside the lower "
                "right as f = 3, 12, 21, 30 MHz, rising from 82 to 142 dB. The lead sentence "
                "states the 6 dB-per-doubling rule and the plot is the illustration of it, one "
                "of the two places in the paper where prose and artwork agree exactly"),
    figure("f9",
           cap("Figure 9: The layers and electron density of ionosphere[8]"),
           mention(13, first=None, style=["Figure 9"], count=0),
           geo("line", panels=2, layout="1x2", shared=True),
           path=P_3221, kind="model",
           note="a borrowed textbook exhibit (the paper's own reference [8] hangs off the "
                "caption): two panels against one altitude strip - left the atmospheric "
                "temperature profile with EXOSPHERE, THERMOSPHERE, MESOSPHERE, STRATOSPHERE and "
                "TROPOSPHERE labelled, right the ionospheric electron density on a log axis "
                "10^4 to 10^6 cm-3 with D, E and F letters. The altitude scale 12 to 600 km is "
                "drawn once on the left, so the right panel carries no y numbers of its own. The "
                "caption names only the electron density and not the temperature panel; never "
                "cited in the body"),
    figure("f10",
           cap(CAP_F10, variables=3, conditions=True),
           mention(14, first=14, style=["Figure 10"], count=1,
                   lead="The total loss can be expressed by:",
                   trail="From figure 10, we can see that if the signal was reflected by calm "
                         "oceans"),
           geo("line", legend="inside"),
           path=P_323, kind="model",
           note="the multi-hop budget at f = 3 MHz over calm water: x 'distance/(km)' 0-2.5 with "
                "an x10^4 multiplier printed at the axis end, y 'attennation/(dB)' 80-170, eight "
                "short arcs keyed by hop count n = 1..8 inside the right, and a dashed line at "
                "150 dB standing for the computed Lmax threshold. The y title misspells "
                "attennation, the multiplier contradicts the '(km)' unit in the caption, and the "
                "eight-entry key sits on top of the data in the 1.6-2.5e4 km range. This is the "
                "paper's house template: the same frame, key and 150 dB line are printed again "
                "in Figure 12 (twice) and Figure 13"),
    table("t1",
           cap("Table 1: Different εr and σ in different geologies.", "Table N:",
               position="above", variables=2),
           mention(15, first=15, style=["Table 1"], count=1,
                   lead="the table below shows the different εr and σ in different geologies."),
           grid(4, 5, header=2, numeric=4, txt=1, rule="booktabs", merged=True),
           path=P_33, kind="model",
           note="the paper's only grid and the only exhibit in it whose caption prints above the "
                "artwork: four geologies (seawater, fresh water, wet soil, dry soil) against "
                "five columns, with 'Geology' merged across both header rows and εr and σ each "
                "merged over a Range/Average pair. Booktabs horizontals only - top rule, spanner "
                "rule, a rule under Range/Average, bottom rule - no verticals, no zebra, no "
                "slanted corner. Ranges print with a tilde ('70', '10~30', '0.66~6.6') and the "
                "averages are rounded to the nearest whole number. Neither σ column carries a "
                "unit anywhere, so the table is dimensionally ambiguous, and the exponents mix "
                "notation ('10-3' against '2.4×10 -2')"),
    figure("f11",
           cap("Figure 11: The comparison of reflected power between smooth and rugged terrain"),
           mention(15, first=15, style=["Figure 11"], count=1,
                   lead="so that the attenuation of ground can also be calculated by formula (3) "
                        "given in 3.1.2.",
                   trail="As shown in the figure 11, the signal strength decreases as the "
                         "frequency increases."),
           geo("line", legend="inside"),
           path=P_33, kind="model",
           note="Figure 7 relabelled: same axes ('frequence / (Hz)' 0-30, 'power / (mW)' 0-5), "
                "same two decaying traces, key inside the upper right reading 'smooth terrain' "
                "and 'rugid terrain'. The terrain substitution is the entire modelling claim of "
                "section 3.3, so the exhibit that carries it is a re-run of the sea-surface "
                "figure with two words changed; the x-axis unit defect is inherited along with "
                "the plot"),
    figure("f12l",
           cap(CAP_F12, variables=3, conditions=True),
           mention(16, first=16, style=["Figure 12"], count=1,
                   trail="Figure 12 shows that when the signal was reflected by smooth terrain, "
                         "f=3MHz"),
           geo("line", legend="inside"),
           path=P_33, kind="model",
           note="left panel of Figure 12, smooth terrain: x 'distance(/km)' 0-2.5 with the x10^4 "
                "multiplier, y 'attenuation(dB)' 80-180, hop arcs keyed n = 1..8 inside the "
                "right, dashed 150 dB threshold. The caption declares '(left)' and '(right)' in "
                "words because no (a)/(b) panel letters exist anywhere in the paper. The two "
                "panels are measured as separate rows since the export left a gutter between "
                "them"),
    figure("f12r",
           cap(CAP_F12, variables=3, conditions=True),
           mention(16, first=16, style=["Figure 12"], count=1),
           geo("line", legend="inside"),
           path=P_33, kind="model",
           note="right panel of Figure 12, rugged terrain: same x10^4 distance axis, y "
                "'attenuation(dB)' 100-220, key n = 1..5 inside the lower right. The hop count "
                "drops from 8 to 5 and the y ceiling rises by 40 dB between the two panels, "
                "which is the numeric heart of section 3.3 and is stated in neither the caption "
                "nor the prose"),
    figure("f13",
           cap(CAP_F13, variables=2, conditions=True),
           mention(17, first=16, style=["Figure 13"], count=1,
                   lead="Figure 13 displays the attenuation degree of the signal reflected by "
                        "the turbulent ocean and received by a shipboard receiver",
                   pattern="figure-n-shows"),
           geo("line", legend="inside"),
           path=P_342, kind="model",
           note="the same budget frame as Figure 10 with the shipboard 3.01 dB mismatch added: x "
                "'distance/(km)' 0-16000 in 2000 steps, y 'attenuation(dB)' 90-180, five "
                "disjoint arcs keyed n = 1..5 inside the lower right, dashed 150 dB line. The "
                "arcs do not meet, so two thirds of the axes are empty and the figure cannot "
                "show which end of each arc is the valid solution. Announced one page early, "
                "which is the paper's only two-page lead for a figure"),
    figure("f14",
           cap("Figure 14: the range of effective signal"),
           mention(17, first=16, style=["Figure 14"], count=2,
                   lead="The result was displayed in figure 14.",
                   trail="In figure 14, the red lines are the ranges that could receive the "
                         "signal"),
           geo("flowchart-or-schematic", numbers=False),
           path=P_342, kind="model",
           note="the only exhibit in the paper drawn as a one-dimensional interval diagram: a "
                "single horizontal axis labelled dr/km with tick marks 0, 1900, 2767, 3894, 5535, "
                "5786, 8302, 8682, 11070, a filled dot marked 'The ship', three red spans over "
                "the receivable intervals, and two brace labels above - dship-signal from 0 to "
                "the ship and Δd across the dot. No key tells the reader what red means and the "
                "span lengths do not match the printed ticks. Its tick values disagree with the "
                "prose's own ranges: the text writes 1900-2676 and 5768-8302 where the artwork "
                "prints 2767 and 5786, a transposition of the last two digits"),
    figure("f15",
           cap("Figure 15: The change of Ltur when wind speed =5, 10, 15 and 20 m/s",
               variables=1, conditions=True),
           mention(18, first=17, style=["Figure 15"], count=1,
                   lead="We considered the wind speed near the sea surface from 5m/s to 20m/s, "
                        "and compare them:",
                   trail="From figure 15 we can find that wind speed has a relatively larger "
                         "influence on the reflection attenuation of sea surface"),
           geo("line", legend="inside"),
           path=P_4, kind="sensitivity",
           note="the sensitivity sweep of the batch's most-repeated experiment: x 'Incident "
                "angle(°)' 0-100, y 'The attenuation of different surface/dB' 0-25, four curves "
                "for w = 5, 10, 15, 20 m/s, key inside the lower right. The legend uses w for "
                "wind speed although the notation glossary defines U19.5 and the caption writes "
                "neither. It is the one figure in the paper whose message is a monotone family - "
                "every curve rises - and the one that the record's three sensitivity rows all "
                "descend from"),
    figure("f16",
           cap("Figure 16: the change of the change of Ltur when there are small changes of εr "
               "and σ", variables=3),
           mention(18, first=18, style=["Figure 16"], count=1,
                   lead="Consider the 20% rise and fall of εr and σ, the results are:",
                   trail="The four curves of figure 16 are almost overlapped."),
           geo("line", legend="inside"),
           path=P_4, kind="sensitivity",
           note="the perturbation test that is meant to show the model is insensitive: x "
                "'Incident angle(°)' 0-90, y 'The attenuation of sea surface/dB' 0-12, four "
                "curves keyed inside the upper right by (εr, σ) pairs - (70, 5), (56, 5), (70, "
                "0.5), (56, 0.5) - which are the +/-20 percent cases, and they overlap into one "
                "band. The caption's stutter ('the change of the change') is the paper's worst "
                "caption defect and the only one that makes the exhibit's subject ambiguous"),
    figure("f17",
           cap("Figure 17: the change of Ltur when there are large changes of εr and σ",
               variables=3),
           mention(19, first=19, style=["Figure 17"], count=1,
                   lead="However, when there are large changes of reflecting medium, such as the "
                        "seawater versus the ground.",
                   trail="Figure 17 shows the difference."),
           geo("line", legend="inside"),
           path=P_4, kind="sensitivity",
           note="the contrast case to Figure 16 and the only place in the paper where two media "
                "are compared on one frame: x 'Incident angle(°)' 0-90, y 'The attenuation of "
                "different surface/(dB)' 0-14, two curves keyed inside the middle right as "
                "(εr = 70, σ = 5) and (εr = 4, σ = 2x10^-3) - sea water against dry soil. Same "
                "axes and same drawing as Figure 16, but a two-entry key instead of four and a "
                "gap of 9 dB between the traces, which is the paper's answer to its own "
                "sensitivity question"),
]

TABLES = [it for it in FIGURES if "family" not in it]
FIGURES = [it for it in FIGURES if "family" in it]

ALL = FIGURES + TABLES
# Row band first (20 pt is inside one printed row), then left to right, so a side-by-side pair
# keeps printed order instead of falling to the taller panel.
_order = sorted(ALL, key=lambda it: (it["page"], round(it["bbox"][1] / 20), it["bbox"][0]))
_page_seen: dict[int, int] = {}
for i, item in enumerate(_order, 1):
    item["place"]["doc_order"] = i
    pg = item["page"]
    _page_seen[pg] = _page_seen.get(pg, 0) + 1
    item["place"]["page_order"] = _page_seen[pg]

RULES = [
    "Numbering is one colon grammar across the whole paper - 18 of the 19 figure rows print "
    "'Figure N:' and the single grid prints 'Table N:' - with exactly one exception, Figure 6, "
    "which is the batch's only caption printed with a full-width colon 'Figure 6：' "
    "[caption.numbering].",
    "Caption side is decided by exhibit kind and inverted between the two kinds: all 19 figure "
    "rows print their caption BELOW the artwork and the one table row prints ABOVE its grid, so "
    "the paper's single grid is also its single above-caption [caption.position].",
    "Three captions carry a second printed line that the artwork cannot say itself - 'n: number "
    "of hops, f = 3MHz, reflected by calm oceans' and its two variants on Figures 10, 12 and 13 "
    "- which makes the caption the only place the parameter setting of a hop-budget plot is "
    "written down [caption.sentences].",
    "Captions are short and flat: the 19 figure captions run 7 to 27 words with a median of 15, "
    "the three shortest are bare noun phrases ('Propagation path of sky wave', 'the range of "
    "effective signal') and the three longest are the hop-budget titles that carry a second "
    "subtitle line [caption.words].",
    "Captions name symbols rather than media - 11 of the 19 name between one and four of Lbf, "
    "Lcal, Ltur, Lt, n, f, εr and σ - and 10 of the 19 pin a parameter setting inside the caption "
    "itself (wind speed on Figures 3 and 15, f = 3MHz on Figures 5, 6, 10, 12 and 13, the "
    "f = 3/12/21/30MHz grid on Figure 8), which is the only reason the plots can be re-derived "
    "[caption.variable_count].",
    "Two captions are defective at the level of the noun: Figure 16 stutters - 'the change of "
    "the change of Ltur' - and Figure 5 says 'tough surface' where the section heading and the "
    "symbol both say turbulent [caption.concludes].",
    "No caption concludes, and no caption prints a unit for its own axis, although one axis "
    "title inside the artwork carries a unit that contradicts the caption's [caption.units].",
    "The paper draws with one engine and one hand: 14 of the 19 figure rows are MATLAB line "
    "plots (single frame, joined traces, no markers, no colourbar, no printed values), 4 are "
    "hand-drawn schematics with no axes at all, and 1 is the single four-panel surface plot "
    "[geometry.family].",
    "Three-dimensional drawing happens exactly once: Figure 3's four surf panels in a 2x2 grid, "
    "shaded with mesh lines, each panel on its own z scale, and with no colourbar - so the "
    "height field that the section is about cannot be read numerically from the print "
    "[geometry.three_d].",
    "Keys are never outside the frame: 11 rows key inside (upper right for the single-frame "
    "sweeps, lower right for the hop-budget template, inside-right for the eight-entry case) and "
    "the other 8 rows carry no key at all, four because they are schematics and four because "
    "Figure 5 and Figure 9 title their panels from inside the axes instead [geometry.legend].",
    "Panel grammar is thin and stated nowhere: Figure 3 is one measured region holding four "
    "panels, Figures 5 and 12 are each split into two measured regions by the export gutter, and "
    "Figure 9 borrows a shared altitude axis across its pair; no (a)/(b) letters exist, and the "
    "only panel labelling in the paper is the words '(left)' and '(right)' inside Figure 12's "
    "caption [geometry.panel_count].",
    "Shared axes are used twice and both times to save a scale rather than to invite comparison: "
    "Figure 9 shares the altitude strip and Figure 5 deliberately does not share its y, so the "
    "two panels of Figure 5 differ by two orders of magnitude while sitting side by side "
    "[geometry.shared_axes].",
    "The last three figures are image exports rather than live vector plots: each is measured "
    "twice, once as its vector frame and once as the raster inside it, so the record keeps one "
    "row per figure and excludes the copy [geometry.printed_numbers].",
    "The single grid is booktabs with merged header spans and nothing else: no zebra, no "
    "slanting corner, no vertical rules, no note row, no continuation, and no unit anywhere in "
    "the σ columns [table.rule_style].",
    "Header depth is two rows because two spanners are needed - 'Geology' across both rows and "
    "εr and σ each across a Range/Average pair - and the merged cells are the only structural "
    "device the grid uses [table.merged_cells].",
    "Shading never appears: no grid in this paper has zebra banding, and the only ruled "
    "non-grid surface in the paper is the abbreviation glossary on p5, which the detector does "
    "not box as a region [table.zebra].",
    "Announcement is same-page for 14 rows and one page early for 4 - Figure 3 is foreshadowed "
    "in the calm-ocean section and Figures 13, 14 and 15 are named on the page before they print "
    "- so section 3.4.2 is the only place where the prose outruns the artwork [mention."
    "lead_pages].",
    "Citation vocabulary is a four-phrase rotation: 'figure N shows', 'As shown in the figure N', "
    "'From figure N we can find' and 'The result was displayed in figure N', with no exhibit "
    "analysed in more than three sentences anywhere in the paper [mention.style].",
    "Two exhibits are never cited in the body at all - Figure 2 and Figure 9 - and both are "
    "borrowed or purely explanatory: Figure 2 is a geometry schematic and Figure 9 is a "
    "textbook plate whose caption carries the reference [mention.count].",
    "Placement tracks the derivation down the page: 9 of the 20 rows sit in the middle band, 8 "
    "in the top third and 3 at the foot, and all three foot cases are hop-budget or terrain plots "
    "that end a section [place.page_zone].",
    "Exhibit density follows the model: the introduction carries 1 row, the modelling sections "
    "3.1-3.4 carry 16, the sensitivity section carries 3, and the two closing pages carry none - "
    "no figure, no table, no pasted equation in the strengths, weakness, note or reference "
    "pages [place.section_kind].",
    "Every measured box outside the exhibit rows is pasted display mathematics (8 boxes), a copy "
    "of a box the detector already holds (4: three raster interiors of vector figure frames and "
    "one raster copy of the Fresnel pair), a caption band (1), a running-header rule band (1) or "
    "a fragment of a frame (1) [place.area_frac].",
]

NOTE = (
    "Thirty-five measured regions resolve to 19 figure rows, 1 table row and 15 exclusions, with "
    "nothing unaccounted. The exclusions split four ways: eight pasted display-mathematics "
    "regions (the Fresnel pair on p5, equations (5)-(6) on p6, (9)-(13) on p8, (14)-(15) on p9, "
    "(16)-(19) on p11, (22)-(23) on p12, the attenuation factor and equation (25) on p13), one "
    "raster duplicate of the Fresnel pair, one running-header and heading rule band on p5, one "
    "caption band on p8 and three raster copies of vector figure frames on pp18-19.\n\n"
    "What this paper adds to the lane. (1) It is the first document in the batch whose captions "
    "record a full-width colon - 'Figure 6：The relationship between Lcal or Ltur and f' - which "
    "no numbering vocabulary covers, so the numbering field takes the bare 'Figure N' form and "
    "this note carries the punctuation. (2) It prints one plot template four times: the "
    "hop-budget frame with a dashed 150 dB threshold and an n = 1..k key appears as Figure 10 "
    "(calm sea, n = 1..8), Figure 12 left (smooth terrain, n = 1..8), Figure 12 right (rugged, "
    "n = 1..5) and Figure 13 (shipboard, n = 1..5), and only the caption and the key change. "
    "(3) It repeats a second template twice: Figure 7 and Figure 11 are the same received-power "
    "curve against frequency, one for sea states and one for terrains, and they share the "
    "misspelt axis 'frequence / (Hz)' in a paper whose band is 3-30 MHz. (4) Both of the "
    "paper's schematic pair - Figures 1 and 2 - are drawn in the same vocabulary (Earth arc, "
    "dashed ionosphere arcs, ray fan, R/Z/θ labels) and neither is cited from the body for "
    "Figure 2. (5) The paper is the lane's clearest case of a caption hiding a unit error that "
    "the artwork repeats: no caption prints a unit, one axis prints Hz for MHz, and the one grid "
    "omits the unit of both σ columns.\n\n"
    "Defects worth recording. Figure 1's ionospheric arcs are unlabelled; Figure 2's label chain "
    "reuses θ for two different quantities; Figure 3 has no colourbar and no panel letters, so "
    "which panel belongs to which wind speed is only inferable from a rotated z label; Figure "
    "4 draws no normal vectors in a section about normal-vector distributions; Figure 5's two "
    "panels differ by two orders of magnitude with nothing but tick labels to say so; Figure 7's "
    "key reads 'clam oceean'; Figure 10's y title reads 'attennation' and its x10^4 multiplier "
    "contradicts the '(km)' unit in its caption; Figure 11's key reads 'rugid terrain'; Figure "
    "12's right panel raises the y ceiling 40 dB without saying so; Figure 13's five arcs do not "
    "meet, leaving two thirds of the frame empty; Figure 14's tick values (2767, 5786) are "
    "transposed against the prose's own ranges (2676, 5768) and no key explains its red spans; "
    "Figure 15's key uses w where the glossary defines U19.5; Figure 16's caption stutters and "
    "its four curves overlap so completely that the exhibit proves only that the perturbation is "
    "invisible; and Table 1 gives no unit for σ. Every page also carries a red Chinese "
    "shop-watermark band in the running header.\n\n"
    "Coverage note for the lane. The abbreviation glossary at the top of p5 - a fifteen-row, "
    "two-column 'Abbreviation / Full Name' table - is a real table and is not in the layout at "
    "all: the detector boxed the rule band above it (p5 r1) and nothing else. It is therefore "
    "not recordable as a table row without inventing a bbox. The same page shows why: the "
    "detector's raster/vector pair on p5 is one pasted equation block measured twice, while the "
    "well-ruled native table beside it is not measured at all - the region pass follows images, "
    "not tables.\n\n"
    "Section grammar. Section 3 is where everything is drawn, in the order the model is built: "
    "geometry (1, 2), the wave simulation (3), the microplane construction (4), the reflection "
    "loss (5-7), the path budget (8), the ionosphere (9), the hop count (10), the terrain "
    "comparison (Table 1, 11, 12), the shipboard correction (13, 14), and then section 4 spends "
    "its three rows asking whether the answer moves when the wind, εr or σ move. Each modelling "
    "step gets exactly one exhibit, and the only two exhibits nobody cites (Figures 2 and 9) are "
    "the two the authors did not draw themselves."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"page": _p, "bbox": _b, "reason": _r, "note": _k}
        for _k, (_p, _b, _r) in EXCLUDED.items()
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
    leg: dict[str, int] = {}
    for it in FIGURES:
        leg[it["geometry"]["legend"]] = leg.get(it["geometry"]["legend"], 0) + 1
    zone: dict[str, int] = {}
    for it in ALL:
        zone[it["place"]["page_zone"]] = zone.get(it["place"]["page_zone"], 0) + 1
    kind: dict[str, int] = {}
    for it in ALL:
        kind[it["place"]["section_kind"]] = kind.get(it["place"]["section_kind"], 0) + 1
    lead: dict = {}
    for it in ALL:
        lead[it["mention"]["lead_pages"]] = lead.get(it["mention"]["lead_pages"], 0) + 1
    print(f"{PID}: figures={len(FIGURES)} tables={len(TABLES)} excluded={len(EXCLUDED)} "
          f"regions={len(MEASURED)}")
    print("fam", dict(sorted(fam.items())))
    print("legend", dict(sorted(leg.items())))
    print("zone", dict(sorted(zone.items())))
    print("kind", dict(sorted(kind.items())))
    print("lead", dict(sorted(lead.items(), key=lambda kv: str(kv[0]))))
    print("payload", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
