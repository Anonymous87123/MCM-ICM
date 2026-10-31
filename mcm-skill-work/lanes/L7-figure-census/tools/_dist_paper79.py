"""Hand census of P-B-2015-40612-8bcdc1a7 (Team 40612, 34 pages, 19 measured regions).

Fourteen figure rows and five table rows, no refusal and nothing unresolved. The paper prints
fourteen numbered figures and nine numbered tables; all fourteen figures and five of the nine
tables own a measured region. The other four grids - Tables 2, 3, 4 and 6 - have no region at
all and are declared as a gap rather than invented.

   p8  r1  Table 1   table-grid            comparison of three search planes, 3 rules
   p12 r1  Fig.1     flowchart-or-schematic one aircraft over the sea, theta and the weights
   p14 r1  Fig.2     composite-panel       the computation flowchart with a heatmap inset
   p15 r1  Fig.3     scatter               cumulative distance distribution and its fit
   p15 r2  Fig.4     heatmap-or-contour    flight dynamics prior over lon/lat
   p17 r1  Fig.5     map-or-plan-view      imagined drifter trajectories over bathymetry
   p17 r2  Fig.6     heatmap-or-contour    surface search prior
   p18 r1  Fig.7     heatmap-or-contour    surface search posterior
   p20 r1  Fig.8     heatmap-or-contour    underwater search prior
   p20 r2  Fig.9     heatmap-or-contour    underwater search posterior
   p22 r1  Fig.10    composite-panel       allocation plan: heatmap plus a two-box inset
   p24 r1  Fig.11    heatmap-or-contour    underwater search prior for AF447
   p25 r1  Fig.12    map-or-plan-view      the printed MH370 search-area poster
   p26 r1  Fig.13    map-or-plan-view      Google Earth globe with the constrained-autopilot cones
   p27 r1  Fig.14    heatmap-or-contour    the four PDFs for MH370 in a 2x2 block
   p29 r1  Table 5   table-grid            nine search planes and their detection limits
   p29 r2  Table 7   table-grid            weights in computing the flight dynamics PDF
   p30 r1  Table 8   table-grid            weights in computing the surface search prior
   p30 r2  Table 9   table-grid            weights in computing the underwater search prior

Declared gap: Table 2 (p10, an unruled fifteen-row variable list), Table 3 (p28, unruled three
rows), Table 4 (p28, three rules at 383.7/404.3/453.8 across 226.0 pt) and Table 6 (p29, three
rules at 338.0/358.7/494.8 across 237.5 pt) return no measured region.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2015-40612-8bcdc1a7"
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


def none_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": "direct",
            "read_sentences": 1, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


# ---------------------------------------------------------------- section paths
# Each region at the top of a page is governed by the last heading printed ABOVE it, which on
# four rows is a heading on the previous page. Every label below is either an indexed heading or
# a printed line, and each was checked against the page it prints on.
SEC_32 = [q("3 Base Analysis", 7), q("3.2 Type of Search Plane", 7)]
SEC_612 = ["6 Establishing and Solving of Model", "6.1 Collision Model",
           "6.1.2 Water Disintegration"]
SEC_632 = ["6 Establishing and Solving of Model", "6.3 Overview on Search Model",
           "6.3.2 Steps of Search Plan"]
SEC_64 = ["6 Establishing and Solving of Model", "6.4 Water Surface Search Model"]
SEC_641 = SEC_64 + ["6.4.1 Surface Search Prior PDF for Impact Location",
                    "6.4.1.1 Flight Dynamics Prior PDF"]
SEC_6413 = SEC_64 + ["6.4.1 Surface Search Prior PDF for Impact Location",
                     "6.4.1.3 Surface Search Prior PDF"]
SEC_642 = SEC_64 + ["6.4.2 Surface Search Posterior PDF for Impact Location"]
SEC_654 = ["6 Establishing and Solving of Model", "6.5 Underwater Search Model",
           "6.5.4 Recursion"]
SEC_72 = ["7 Allocation Model", "7.2 Allocation of Search Planes"]
SEC_813 = ["8 Applying of Model", "8.1 Application on AF447", "8.1.3 Computation Result"]
SEC_821 = ["8 Applying of Model", "8.2 Prediction on MH370",
           "8.2.1 Review on Established Models"]
SEC_822 = ["8 Applying of Model", "8.2 Prediction on MH370", "8.2.2 Probability Distribution"]
SEC_823 = ["8 Applying of Model", "8.2 Prediction on MH370", "8.2.3 Computation Process"]
SEC_93 = ["9 Sensitivity Analysis", "9.3 The Types of Search Planes"]
SEC_94 = ["9 Sensitivity Analysis", "9.4 Weights in Computing Flight Dynamics PDF"]
SEC_95 = ["9 Sensitivity Analysis", "9.5 Weights in Computing Surface Search Prior PDF"]
SEC_96 = ["9 Sensitivity Analysis", "9.6 Weights in Computing Underwater Search Prior PDF"]


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "single",
           legend: str = "none", numbers: bool = True, labels: bool = False,
           three_d: str = "no", colorbar: bool = False, source: str = "text-layer",
           shared_axes: bool = False, note: str = "", other_note: str = "",
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
                     "shared_axes": shared_axes, "legend": legend, "colorbar": colorbar,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, cap_text: str, mention: dict, kind: str, path: list[str], *,
          rows: int, cols: int, numeric_cols: int, text_cols: int, rule_style: str,
          width: str, header_rows: int = 1, units_in_header: bool = False,
          note: str = "", note_sentence: str = "", source: str = "text-layer") -> None:
    c = CTXREG[(page, reg)]
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, "Table N:", "above"),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule_style, "zebra": False, "merged_cells": False,
                  "diagonal_header": False, "units_in_header": units_in_header,
                  "decimal_aligned": False, "numeric_cols": numeric_cols,
                  "text_cols": text_cols, "width": width, "orientation": "portrait",
                  "continued": False, "note_sentence": note_sentence},
    })


# ---------------------------------------------------------------- 3.2 the plane comparison
table(8, 1, q("Table 1: Comparison between Different Types of Search Planes", 8),
      cited(7, 8, ["Table 1"], 1,
            "their corresponding performances [4] are listed in Table 1 for comparison."),
      "model", SEC_32, rows=3, cols=5, numeric_cols=2, text_cols=3, rule_style="booktabs",
      width="full", units_in_header=True, note=(
          "Three rules - one above the header, one under it, one closing rule at 273.2 pt - and "
          "not one vertical across 464.5 pt, so a booktabs grid that spans the whole measure and "
          "overhangs the body text on both sides. Header 'Example | Type | Search Speed (km/h) | "
          "Voyage (km) | Search Sensors'; the P-3C sensor cell wraps over three lines while the "
          "other two rows print on one, which is why the grid is 107 pt tall for three rows. No "
          "prose sentence about it prints beside it - the only one, 'their corresponding "
          "performances [4] are listed in Table 1 for comparison.', is the last line of 3.2 on "
          "p7 - so the note sentence is left empty"),
      note_sentence="")

# ---------------------------------------------------------------- 6.x the drawn figures
figure(12, 1, "flowchart-or-schematic",
       q("Figure 1: The Diagram for Water Disintegration", 12), "Figure N:",
       cited(11, 12, ["Figure 1"], 4, "The diagram of this situation is shown in Figure 1."),
       "model", SEC_612, labels=True, note=(
           "A white aircraft silhouette over a photographic sea-and-sky raster, the sight line "
           "dotted down to the water, the surface marked with a short dotted line and the contact "
           "angle lettered theta at the nose. The background is a pasted photograph but the "
           "exhibit is the drawn construction on it, so it is recorded as a schematic and not as "
           "a photo. It is the figure the paper leans on most: four separate sentences name it, "
           "on pp11, 23, 24 and 26 [mention.count]."))
figure(14, 1, "composite-panel",
       q("Figure 2: Summary of the Probability Distribution Computation", 14), "Figure N:",
       cited(13, 14, ["Figure 2"], 1,
             "As is illustrated in Figure 2, we can divide the search model into"),
       "model", SEC_632, panels=2, layout="flowchart with heatmap inset", labels=True,
       colorbar=True, note=(
           "One flowchart and one inset heatmap in the same picture: the boxes run upward from "
           "the flight-path computations through Flight Dynamics Prior and Reverse Drift Prior "
           "into Surface Search Prior, Surface Search Posterior and two Underwater Search boxes "
           "at weights of 50/50, 70/30 and 30/70; the inset in the upper right is a lon/lat "
           "probability field with its own colour bar. TWO FAMILIES, so a composite and not a "
           "same-family panel. THE INSET CARRIES ITS OWN CAPTION INSIDE THE PICTURE - the line "
           "'Figure 9: Underwater Search Posterior PDF for Impact Location' is painted under the "
           "inset, which is Figure 9 printed again twelve pages before Figure 9 appears on p20. "
           "The flowchart also misspells its own box twice as 'Underwater Search Porior'."))
figure(15, 1, "scatter",
       q("Figure 3: Cumulative Distribution of Distance from Beginning of Emergency to Impact "
         "Location", 15), "Figure N:",
       cited(15, 15, ["Figure 3"], 2,
             "the cumulative distribution of distance traveled from the beginning of emergency "
             "to the impact location is plotted in Figure 3."),
       "model", SEC_641, labels=True, note=(
           "Blue crosses and a few exes rising from 0.1 at 2 NM to near 1.0 at 20 NM, with one "
           "red fitted curve through them, on a four-sided frame ticked 0 to 20 across and 0 to 1 "
           "up. The x axis is titled 'Distance (NM)' and the y axis carries no title at all, "
           "although the caption says what it is. A second sentence on p19 names the same figure "
           "for its 70 per cent mixture weight [mention.count]."))
figure(15, 2, "heatmap-or-contour",
       q("Figure 4: Flight Dynamics Prior PDF", 15), "Figure N:", none_mention(),
       "model", SEC_641, labels=True, colorbar=True, note=(
           "A filled field over 171.5-173.0 E and 14.0-15.5 N with one bright cell near 14.8 N, "
           "172.35 E, white graticule lines and a colour bar on the right. The first of nine "
           "lon/lat probability fields in the paper, all of them the same kind of pasted raster: "
           "none has an axis title, a legend or anything printed inside the picture "
           "[geometry.family]."))
figure(17, 1, "map-or-plan-view",
       q("Figure 5: Imagined Trajectories in System Simulation in Two Days", 17), "Figure N:",
       cited(16, 17, ["Figure 5"], 1,
             "Figure 5 is depicted according to our system simulation."),
       "model", SEC_6413, labels=True, note=(
           "A top-down plan over a blue bathymetric relief with ten or more thin coloured "
           "search tracks running in from the edges and ending in coloured dots, the impact point "
           "annotated in white at the top and a 10 NM scale bar at lower left. The tracks are "
           "coloured per drifter but no key prints, so the reader cannot say which colour is "
           "which drifter. It illustrates reverse drift, which belongs to 6.4.1.2, but 6.4.1.3 "
           "has already begun when it prints, and the sentence that names it - 'Figure 5 is "
           "depicted according to our system simulation' - sits under 6.4.1.3 on p16, so the "
           "path follows the page and the prose, not the topic."))
figure(17, 2, "heatmap-or-contour",
       q("Figure 6: Surface Search Prior PDF for Impact Location", 17), "Figure N:",
       cited(16, 17, ["Figure 6"], 1, "The result of the calculation is shown in Figure 6."),
       "model", SEC_6413, labels=True, colorbar=True, note=(
           "The same lon/lat window and the same ramped field as Figure 4, with a larger red core "
           "and a full colour bar ticking to 0.008. Two rows with the same window, the same "
           "ramp and the same axes: only the caption and the peak value separate them."))
figure(18, 1, "heatmap-or-contour",
       q("Figure 7: Surface Search Posterior PDF for Impact Location", 18), "Figure N:",
       cited(18, 18, ["Figure 7"], 2,
             "A posterior PDF for the impact point is calculated in this fashion and the result "
             "is depicted in Figure 7."),
       "model", SEC_642, labels=True, colorbar=True, note=(
           "The posterior over the same window: dark blue field, one compact green-yellow-red "
           "core near 172.2 E, 14.8 N, colour bar 0 to 0.04. The p19 sentence that reuses it "
           "gives the mixture weight, so the same picture is cited as a prior input downstream "
           "[mention.count]."))
figure(20, 1, "heatmap-or-contour",
       q("Figure 8: Underwater Search Prior PDF for Impact Location", 20), "Figure N:",
       cited(19, 20, ["Figure 8"], 1, "The PDF is plotted in Figure 8."),
       "model", SEC_654, labels=True, colorbar=True, note=(
           "The same window again, with a diffuse cyan field and a small red peak near the centre "
           "and a colour bar to 0.040. Printed at the top of p20 although the sentence that "
           "introduces it sits under 6.5.1 on p19 [place.section_path]."))
figure(20, 2, "heatmap-or-contour",
       q("Figure 9: Underwater Search Posterior PDF for Impact Location", 20), "Figure N:",
       cited(19, 20, ["Figure 9"], 1, "The posterior PDF is plotted in Figure 9."),
       "model", SEC_654, labels=True, colorbar=True, note=(
           "The broadest and faintest field in the paper - mid-blue to cyan nearly everywhere, "
           "one small red peak, colour bar to 0.0021. This is the figure already printed inside "
           "Figure 2's inset on p14, caption and all; the record keeps both rows and reports the "
           "duplication rather than dropping either."))
figure(22, 1, "composite-panel",
       q("Figure 10: Allocation Plan of the Search Aircrafts", 22), "Figure N:",
       cited(22, 22, ["Figure 10"], 1, "Figure 10 is depicted to show the allocation plan."),
       "solution", SEC_72, panels=2, layout="heatmap with map inset", labels=True,
       colorbar=True, note=(
           "The lon/lat probability field with a large yellow-red blob, plus an inset at upper "
           "left holding the two allocation rectangles - red for the better aircraft, green for "
           "the weaker ones - over its own mini axes. Two families in one picture, so a composite. "
           "The prose points at the inset in the same breath: 'In the upper left corner, the "
           "larger rectangle accords with the better planes.'"))
figure(24, 1, "heatmap-or-contour",
       q("Figure 11: Underwater Search Prior PDF for AF447", 24), "Figure N:",
       cited(23, 24, ["Figure 11"], 1,
             "The underwater search prior PDF for the case of AF447 is shown in Figure 11."),
       "result", SEC_813, labels=True, colorbar=True, note=(
           "The only field in the paper drawn over a different window: 33.0-28.0 W and 0.5-5.0 N, "
           "dashed graticule, one compact peak near 31.2 W, 3.0 N and a faint streak east of it, "
           "colour bar to 0.0326. It is the AF447 application, so the window is the Atlantic and "
           "not the Indian Ocean [geometry.family]."))
figure(25, 1, "map-or-plan-view",
       q("Figure 12: The Search for MH370", 25), "Figure N:",
       cited(24, 25, ["Figure 12"], 1,
             "As is shown in Figure 12 [17], different models proposed on different dates gives "
             "different search areas"),
       "other", SEC_821, labels=True, legend="inside", note=(
           "A printed poster map pasted in: 'The Search for Malaysia Airlines Flight 370 in the "
           "Southern Indian Ocean (through November 2014)', bathymetric tint, the Western "
           "Australian coast, a rotated 'Current Search Area (as of November 2014)' inset at top "
           "left, coloured survey swaths, drifting search-area polygons dated March to April and "
           "a sonar-contact legend block at bottom right. The poster's own banner is painted "
           "inside the image; the printed caption below it is the two-word 'The Search for "
           "MH370'. The only exhibit in the paper whose art was not made by the authors."))
figure(26, 1, "map-or-plan-view",
       q("Figure 13: Representation of Probability Distribution", 26), "Figure N:",
       cited(26, 26, ["Figure 13"], 2, "The representation is shown in Figure 13."),
       "result", SEC_822, labels=True, note=(
           "A tilted Google Earth globe of the southern Indian Ocean carrying the authors' own "
           "overlay: a red cone labelled 'Constrained autopilot dynamics', a green blob labelled "
           "'Data error optimisation', a grey great-circle band with dense tracks fanning along "
           "it, a white arc and a purple bar marked MRC. The basemap credits are legible inside "
           "the picture. Two sentences on p26 name it [mention.count]."))
figure(27, 1, "heatmap-or-contour",
       q("Figure 14: PDFs for MH370", 27), "Figure N:",
       cited(26, 27, ["Figure 14"], 1, "The PDF for each search is shown in Figure 14."),
       "result", SEC_823, panels=4, layout="2x2", labels=True, colorbar=True, note=(
           "Four pasted fields in a 2x2 block, each with its own colour bar and its own letter "
           "printed inside the panel: (a) water surface prior, (b) water surface posterior, "
           "(c) underwater prior, (d) underwater posterior. The panel titles are typeset outside "
           "the block - (a) and (b) above the top row, (c) and (d) below the bottom row, with the "
           "figure caption between the block and the lower pair, so reading order in the layer "
           "runs parent above, caption, then two more parent labels. Same family four times, so "
           "one row with a panel count of four [geometry.panel_count]."))

# ---------------------------------------------------------------- the remaining printed grids
table(29, 1, q("Table 5: Types of Search Planes according to Search Capabilities", 29),
      cited(28, 29, ["Table 5"], 1, "The detailed setting is pre- sented in Table 5."),
      "sensitivity", SEC_93, rows=9, cols=4, numeric_cols=3, text_cols=1,
      rule_style="booktabs", width="half", note=(
          "Two rules at 145.3 and 165.9 pt across 379.3 pt, no vertical and NO closing rule: the "
          "nine rows run from 171.1 to 292.6 pt and then the grid simply stops, so the last row "
          "sits open above Table 6's caption at 314.7 pt. Nine serial numbers, a limit of search "
          "area in cells and two detection probabilities; the header wraps to three lines "
          "because both probability symbols are subscripted twice [table.rule_style]. No prose "
          "sentence about it prints beside it either - the pointing sentence, 'The detailed "
          "setting is pre- sented in Table 5.', closes 9.3 on p28 - so the note sentence is "
          "left empty."),
      note_sentence="")
table(29, 2, q("Table 7: Sensitivity Tests on the Weights in Computing Flight Dynamics PDF", 29),
      cited(29, 29, ["Table 7"], 2,
            "The value of PAk W (Si,j ) is listed in Table 7."),
      "sensitivity", SEC_94, rows=3, cols=3, numeric_cols=3, text_cols=0,
      rule_style="booktabs", width="full", note=(
          "Three rules at 663.1, 683.7 and 733.2 pt across 437.9 pt at the foot of the page, "
          "three rows, no vertical. Columns are the LKP-based share, the cumulative distance "
          "share and the summed detection probability; the three results - 0.520, 0.516, 0.508 - "
          "differ by 0.012 across the whole sweep."),
      note_sentence="The value of PAk W (Si,j ) is listed in Table 7.")
table(30, 1, q("Table 8: Sensitivity Tests on the Weights in Computing Surface Search Prior PDF",
               30),
      cited(30, 30, ["Table 8"], 1, "The calculation results are shown in Table 8."),
      "sensitivity", SEC_95, rows=3, cols=3, numeric_cols=3, text_cols=0,
      rule_style="booktabs", width="half", note=(
          "Three rules at 252.1, 272.7 and 322.2 pt across 321.2 pt, three rows. Columns are the "
          "flight dynamics prior share, the reverse drift prior share and the summed probability; "
          "the results 0.518, 0.518, 0.520 are flatter than Table 7's."),
      note_sentence="The calculation results are shown in Table 8.")
table(30, 2, q("Table 9: Sensitivity Tests on the Weights in Computing Underwater Search Prior "
               "PDF", 30),
      cited(30, 30, ["Table 9"], 1, "The results are shown in Table 9."),
      "sensitivity", SEC_96, rows=3, cols=3, numeric_cols=3, text_cols=0,
      rule_style="booktabs", width="half", note=(
          "Three rules at 509.2, 529.8 and 579.3 pt across 349.4 pt. Columns are the surface "
          "search posterior share, the flight dynamics prior share and the summed probability, "
          "results 0.516, 0.518, 0.519. Its caption is the only one in the paper that runs to "
          "two lines - 'Table 9: Sensitivity Tests on the Weights in Computing Underwater Search "
          "Prior' at 474.7 pt and the orphan 'PDF' at 489.1 pt - so the caption reads 'Prior' on "
          "one line and 'PDF' on the next [caption.words]."),
      note_sentence="The results are shown in Table 9.")

# ---------------------------------------------------------------- rules and note
RULES: list[str] = [
    "Families split two ways by kind and four ways overall: fourteen figure rows as seven "
    "heatmap-or-contour fields, three map-or-plan-view frames, two composite-panel pictures and "
    "one each of flowchart-or-schematic and scatter, plus five table-grid rows "
    "[geometry.family].",
    "The heatmap rows are one template stamped nine times: the same lon/lat window of "
    "171.50-173.00 E by 14.00-15.50 N, the same rainbow ramp, white graticule and right-hand "
    "colour bar, differing only in peak value and spread. None carries an axis title, a legend "
    "or any title printed inside the picture [geometry.colorbar].",
    "Two rows hold two different kinds of picture and are therefore composites, not panels: "
    "Figure 2 is a flowchart with a heatmap inset, Figure 10 is a heatmap with a two-rectangle "
    "map inset [geometry.panel_count].",
    "Figure 14 breaks the panel rule the other way: four fields of the SAME family in a 2x2 "
    "block, so it is one row with a panel count of four, and its panel titles are typeset "
    "outside the block with the figure caption between the rows [geometry.panel_count].",
    "Figure 9 is printed twice. Its caption and picture are painted inside Figure 2's inset on "
    "p14 - 'Figure 9: Underwater Search Posterior PDF for Impact Location' is legible inside the "
    "p14 artwork - and again on p20 as its own numbered exhibit. Both rows stay in the census "
    "and the duplication is stated here rather than silently merged [caption.verbatim].",
    "Caption side is inverted between the two kinds and never mixed: all fourteen figure "
    "captions print BELOW their picture, all five measured table captions print ABOVE their grid "
    "[caption.position].",
    "Numbering is 'Figure N:' and 'Table N:' throughout, with one ragged edge: the paper's "
    "running prose uses the same form plus a full stop when it points forward ('...is plotted "
    "in Figure 3.'), so the layer prints both 'Figure 3.' as a sentence end and 'Figure 3:' as a "
    "caption [caption.numbering].",
    "FOUR PRINTED GRIDS ARE MISSING AND THAT IS DECLARED, NOT PATCHED: Table 2 on p10 (a "
    "fifteen-row variable list with no rules at all), Table 3 on p28 (three rows, no rules), "
    "Table 4 on p28 (three rules at 383.7/404.3/453.8 pt across 226.0 pt) and Table 6 on p29 "
    "(three rules at 338.0/358.7/494.8 pt across 237.5 pt each returned no measured region, "
    "although both carry a printed caption above them and Table 6 is even cited on p28. A "
    "rule-only grid of three rules and 70-157 pt of height is outside what the measurer returns, "
    "so no bbox exists to anchor a row [place.area_frac].",
    "Citation is unusually complete for this lane: eighteen of the nineteen measured exhibits "
    "are named in prose and only Table 2 never is. Figure 1 carries four separate pointers "
    "across pp11, 23, 24 and 26, Figures 3, 7 and 13 carry two each, Table 7 carries two "
    "[mention.count].",
    "Leads are mostly forward by exactly one page: Table 1, Figures 1, 2, 5, 6, 8, 9, 11, 12, "
    "14 and Table 5 are each cited a page before they print, and only Table 3 is cited far "
    "ahead, on p23 for a grid that prints on p28 [mention.lead_pages].",
    "Section paths follow the last heading printed above each region, and on seven rows that "
    "heading is on the previous page: Table 1 is governed by 3.2 on p7, Figure 1 by 6.1.2 on "
    "p11, Figure 2 by 6.3.2 on p13, Figures 5 and 6 by 6.4.1.3 on p16, Figure 11 by 8.1.3 on "
    "p23, Figures 8 and 9 by 6.5.4 on p19. Figures 8 and 9 are announced under 6.5.1 and 6.5.3 "
    "and print under 6.5.4 [place.section_path].",
    "The heading index is wrong on three rows and the printed order says so. It attributes "
    "Figure 1 to 6.2 System Module and Figure 2 to the 6.4.1.1 chain, but on p12 the 6.2 "
    "heading prints at 634.9 pt while Figure 1 occupies 121.8-307.4 pt, and on p14 the 6.4, "
    "6.4.1 and 6.4.1.1 headings print at 463.7, 495.6 and 569.0 pt while Figure 2 occupies "
    "121.8-414.6 pt and its caption prints at 430.4 pt - both headings come BELOW the picture "
    "they are credited with. The same pass gives Figure 5 the path of 6.4.1.1. Every path here "
    "was rebuilt from the printed line tops [place.section_path].",
    "Width almost separates the two kinds, but not quite: the five grids run 321.2 to 464.5 pt "
    "wide and the figures 251.7 to 331.2 pt, so Figure 12's 331.2 pt is wider than Table 8's "
    "321.2 pt. What does separate them cleanly is the raster/vector kind - every figure row is "
    "a raster and every table row has a vector grid with rules - and no figure in the paper "
    "carries a single rule or fill [place.area_frac].",
]


NOTE = (
    "Paper 79, Team 40612, a 2015 paper that builds a collision, drift and Bayesian search "
    "model for an aircraft lost over water and then applies it to AF447 and MH370. Thirty-four "
    "pages, nineteen measured regions over fourteen pages, all of them exhibits: fourteen "
    "figure rows and five table rows, no refusal and nothing unresolved. The paper prints "
    "fourteen numbered figures and nine numbered tables; every figure and five of the tables "
    "own a region.\n\n"
    "What the exhibits are. Seven heatmap-or-contour rows carry the probability fields - the "
    "flight dynamics prior, the reverse drift prior, the surface and underwater priors and "
    "posteriors, and the four MH370 PDFs of Figure 14 - and they are one template stamped nine "
    "times over the same Indian Ocean window, differing only in peak value and spread. Three "
    "map rows carry place rather than probability: the imagined drifter trajectories of Figure "
    "5 over bathymetry, the pasted MH370 search-area poster of Figure 12, and the Google Earth "
    "globe of Figure 13 with the authors' own autopilot cones drawn over it. Two composites "
    "carry the computation itself - the flowchart with an inset field on p14, the allocation "
    "plan with its two-rectangle inset on p22 - and Figure 3 is the paper's single scatter, the "
    "cumulative distance distribution with its fitted curve.\n\n"
    "The finding worth carrying out of this paper is the duplication inside Figure 2. Its "
    "pasted artwork includes a heatmap inset with the caption 'Figure 9: Underwater Search "
    "Posterior PDF for Impact Location' painted under it, so Figure 9 exists twice: once inside "
    "Figure 2 on p14 and once as its own exhibit on p20. The two rows are kept separate and the "
    "duplication is declared. The flowchart in the same picture also misspells its own box "
    "twice as 'Underwater Search Porior'.\n\n"
    "Four printed grids are missing and that is a declared gap, not an oversight. Table 2 on "
    "p10 is a fifteen-row variable list with no rules at all, Table 3 on p28 is three unruled "
    "rows, and Tables 4 and 6 print three rules each - at 383.7/404.3/453.8 pt across 226.0 pt "
    "and at 338.0/358.7/494.8 pt across 237.5 pt - with no measured region returned for either, "
    "although both carry a caption above them and Table 6 is even cited on p28. No bbox exists "
    "to anchor a row, so none was invented.\n\n"
    "Citation is far better here than in the rest of the run: eighteen of nineteen measured "
    "exhibits are named in prose, Figure 1 four times, and leads are mostly a single page "
    "forward. The one outlier is Table 3, announced on p23 for a grid that prints on p28. "
    "Section paths needed hand work because six regions sit at the top of a page under a "
    "heading printed on the previous one, and Figures 8 and 9 are announced under 6.5.1 and "
    "6.5.3 but print under 6.5.4."
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

out = PROXY / "pc79-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
