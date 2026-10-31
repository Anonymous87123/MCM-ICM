"""Hand pass for P-C-2013-21165-17e64d15 (a linked neural-network model of global air quality:
global/local nodes, AQI, fit verification, critical nodes, sensitivity, three case studies),
19 pp, 17 measured regions over 11 pages.

    p3-r1   line     Figure 1, World3 scenario 2 - five labelled curves, 1900-2100
    p4-r1   line     Figure 2(a) - population, people (billion), 1750-2000
    p4-r2   line     Figure 2(b) - transport, number (million), 1750-2000
    p4-r3   line     Figure 2(c) - atmosphere, N2O concentration, 1750-2000
    p4-r4   table    Table 1 - AQI levels, numerical value, meaning, colour bands
    p5-r1   table    Table 2 - notations, symbol | meaning
    p6-r1   network  Figure 3 - the basic framework, global and local nodes
    p8-r1   table    Table 3 - input and output of the local network
    p10-r1  line     Figure 4 - stepwise forecast, Belgium
    p11-r1  bar      Figure 5 - eighteen countries ranked by nodal influence
    p12-r1  line     Figure 6(a) - sensitivity, India
    p12-r2  line     Figure 6(b) - sensitivity, China
    p13-r1  map      Figure 7(a) - world pollution distribution, 1970
    p13-r2  map      Figure 7(b) - world pollution distribution, 2008
    p14-r1  line     Figure 8 - autonomous forecast, Japan
    p15-r1  line     Figure 9 - autonomous forecast, India (reprints Figure 6a)
    p15-r2  line     Figure 10 - autonomous forecast, Hungary, y axis to 200

Usage: python -I tools/_dist_paper50.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2013-21165-17e64d15"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

S12 = "1.2 An Overview of Air Quality"
S122 = "1.2.2 Primary Influence Factors"
S13 = "1.3 Air Quality Index (AQI)"
S15 = "1.5 Notations"
S21 = "2.1 Generic Methodology"
S221 = "2.2.1 Input and Output of Local Network"
S32 = "3.2 Fit verification"
S33 = "3.3 Identifying critical nodes"
S34 = "3.4 Sensitivity to a relationship change"
S35 = "3.5 Case Study"

PATH: dict[int, tuple[list[str], str]] = {
    3: ([S12], "other"),
    5: ([S15], "symbols"),
    6: ([S21], "model"),
    8: ([S221], "result"),
    10: ([S32], "test"),
    11: ([S33], "other"),
    12: ([S34], "sensitivity"),
    13: ([S35], "other"),
    14: ([S35], "other"),
    15: ([S35], "other"),
}
# p4 carries Figure 2 under one heading and Table 1 under the next
PATH_ONE = {
    (4, 1): ([S122], "other"),
    (4, 2): ([S122], "other"),
    (4, 3): ([S122], "other"),
    (4, 4): ([S13], "other"),
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

VENTION = {3: 1, 4: 4, 5: 1, 6: 1, 8: 1, 10: 1, 11: 1, 12: 2, 13: 2, 14: 1, 15: 2}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}

CAP_31 = "Figure 1: World3 Computer Model Scenario 2: More Abundant Nonrenewable Resources [3]"
CAP_42 = ("Figure 2 (a) (b) The Increasing rates of change in human activity (c) Global scale "
          "changes in the Earth system as a result of the dramatic increase in human activity: "
          "atmospheric N2O concentration [2]")
CAP_43 = "Figure 3 The basic framework"
CAP_104 = "Figure 4 The result of stepwise forecast: Belgium"
CAP_115 = "Figure 5 Identifying the critical nodes"
CAP_126 = "Figure 6 (a) (b) Sensitivity to a relationship change: removing or not removing China"
CAP_137 = "Figure 7 (a) (b) The change of world pollution distribution"
CAP_148 = "Figure 8 Case Study using an autonomous forecast: Japan"
CAP_159 = "Figure 9 Case Study using an autonomous forecast: India"
CAP_1510 = "Figure 10 Case Study using an autonomous forecast: Hungary"


def printed(page: int, text: str) -> str:
    """Verify a caption string really prints on the page, once Unicode-normalised."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text))
    return text


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH_ONE.get((page, reg)) or PATH[page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, source: str, position: str, numbering: str) -> dict:
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": position,
    }


def figure(page: int, reg: int, family: str, caption_text: str = "", *, source: str = "none",
           numbering: str = "none", position: str = "below", panels: int = 1,
           layout: str = "1", legend: str = "none", colorbar: bool = False,
           numbers: bool = True, labels: bool = False, other_note: str = "", note: str = "",
           mention: dict | None = None) -> None:
    ORDER.append((page, reg))
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg),
        "mention": mention or dict(NULL_MENTION),
        "caption": caption_block(caption_text, source, position, numbering),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, caption_text: str = "", *, source: str = "none",
          numbering: str = "none", rows: int, cols: int, header_rows: int = 1,
          rules: str = "booktabs", zebra: bool = False, numeric_cols: int = 0,
          text_cols: int = 0, merged: bool = False, continued: bool = False, note: str = "",
          mention: dict | None = None) -> None:
    ORDER.append((page, reg))
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": caption_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg),
        "mention": mention or dict(NULL_MENTION),
        "caption": caption_block(caption_text, source, "above", numbering),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rules, "zebra": zebra, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "full", "orientation": "portrait",
            "continued": continued, "note_sentence": "",
        },
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note})


def build() -> str:
    # --- section 1: the World3 backdrop and the AQI factors -----------------------------
    figure(3, 1, "line", printed(3, CAP_31), source="text-layer", numbering="Figure N:",
           position="below",
           note="A photograph of the World3 screen plot pasted in as one raster, greyscale. "
                "Five curves are labelled in place rather than by a legend - Resources "
                "(dotted, falling from 2100 back), Population (solid, peaking near 2000), Food "
                "(dotted), Pollution (dashed, exploding after 1950) and Industrial output "
                "(dash-dot) - over an x axis of 1900, 2000 and 2100. In-figure title 'State of "
                "the World', a light grey plot field, three horizontal gridlines and no y axis "
                "labels at all, so no numeric scale is printed [geometry.legend].")

    figure(4, 1, "line", printed(4, CAP_42), source="text-layer", numbering="Figure N",
           position="below", layout="1 of 3",
           note="Panel (a) of a three-panel row, printed as its own small raster with the "
                "panel letter '(a)' in the upper left. A filled area under a line: in-figure "
                "title 'population', y 'people (billion)' 0 to 7 by 1, x 'year' 1750 to 2000 in "
                "fifty-year ticks drawn diagonally. No legend and no gridlines.",
           mention={
               "first_page": 4, "lead_pages": 0, "style": ["Figure 2"],
               "count": 1,
               "lead_sentence": "such a growth has also left a significant imprint on the "
                                "environment, which is shown in the figures below",
               "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
               "gap_sentences": None})
    figure(4, 2, "line", printed(4, CAP_42), source="text-layer", numbering="Figure N",
           position="below", layout="2 of 3",
           note="Panel (b), same construction as (a): in-figure title 'transport: motor "
                "vehicles', y 'number (million)' 0 to 800 by 200, x 'year' 1750 to 2000, the "
                "area filled grey and flat at zero until about 1950 before rising steeply.")
    figure(4, 3, "line", printed(4, CAP_42), source="text-layer", numbering="Figure N",
           position="below", layout="3 of 3",
           note="Panel (c): in-figure title 'atmosphere: N2O concentration', y 270 to 310 ppbv "
                "by 10, x 'year' 1750 to 2000, a grey fill under a rising curve, and the "
                "sub-label '(ii)' printed inside the frame's upper left corner. The caption "
                "splits its three panels into two sub-titles - '(a) (b)' under 'The Increasing "
                "rates of change in human activity' and '(c)' under 'Global scale changes'.")

    table(4, 4, printed(4, "Table 1"), source="text-layer", numbering="Table N",
          rows=7, cols=3, numeric_cols=0, text_cols=3, rules="no-rules", merged=False,
          note="The AQI band table, pasted in as a colour raster: header 'Air Quality Index "
               "Levels of Health Concern | Numerical Value | Meaning' over six bands, Good 0 to "
               "50, Moderate 51 to 100, Unhealthy for Sensitive Groups 101 to 150, Unhealthy 151 "
               "to 200, Very Unhealthy 201 to 300, Hazardous 301 to 500. No rules at all: each "
               "band is a solid colour fill (green, yellow, orange, red, purple, maroon) and the "
               "white gaps between bands stand in for row rules, so `rule_style` is `no-rules` "
               "and `zebra` is false. The caption is the bare word 'Table 1' with no title.")

    table(5, 1, printed(5, "Table 2"), source="text-layer", numbering="Table N",
          rows=10, cols=2, numeric_cols=0, text_cols=2, rules="booktabs",
          note="The notation list: header 'Symbol | Meaning' over nine entries - f, g, d, r, p, "
               "F, q, S and l - with the symbols set in italic. Horizontal rules only, at the "
               "top, under the header and at the foot, plus two extra heavy rules that group the "
               "entries in threes; no vertical rules. One entry wraps to a second line inside "
               "its cell. The caption is the bare word 'Table 2' with no title. This table is "
               "live vector text, unlike the colour-grid Table 1 above it.")

    figure(6, 1, "node-link-network", printed(6, CAP_43), source="text-layer",
           numbering="Figure N", position="below", legend="inside", labels=True,
           note="The model's architecture drawing, 127 vector paths: a box of numbered local "
                "nodes ('1', '2', ... 'n') with 'Inputs' arrows entering from below and "
                "'Global Type Output' leaving upward, joined to three rectangular global nodes "
                "('i+1', 'i+2', '...') by arrows labelled 'Global Link (i, i+1)', '(i, i+2)', "
                "'(i, ...)'; a dashed circle marks the 'Local Network' and a dashed ellipse on "
                "the right opens the 'Local View', a dense cluster of small filled nodes with "
                "its own 'Local Type Output'. The bottom left corner carries the figure's own "
                "two-entry symbol key, open rectangle = 'Global Nodes', open circle = 'Local "
                "Nodes', so the legend is inside the region [geometry.legend].")

    table(8, 1, printed(8, "Table 3"), source="text-layer", numbering="Table N",
          rows=6, cols=4, header_rows=2, numeric_cols=0, text_cols=4, rules="vertical-rules",
          merged=True,
          note="Input and output of the local network in one grid: a spanner header 'Input' "
               "over 'Name and Notation | Initial Value' and a spanner header 'Output' over "
               "'Name and Notation | Type', then four body rows (population density, forest "
               "coverage rate, share of the secondary sector, sum of feedbacks to a global "
               "node). Two header rows, so `header_rows` is 2 and `merged_cells` is true; a "
               "vertical rule separates the Input half from the Output half, and horizontal "
               "rules run between every row. Two name cells wrap to three lines. The caption is "
               "the bare word 'Table 3' with no title.")

    # --- section 3: fit verification, critical nodes, sensitivity, case studies ---------
    figure(10, 1, "line", printed(10, CAP_104), source="text-layer", numbering="Figure N",
           position="below", legend="outside-right",
           note="Stepwise forecast for Belgium: a solid dark-blue 'actual value' line against "
                "red '+' markers for the 'forecast value', legend boxed outside the frame at "
                "the right. x 1970 to 2010 in five-year ticks, y 30 to 130 by 10, and both "
                "vertical (five-yearly) and horizontal (ten-unit) gridlines drawn. No axis "
                "titles and no in-plot title.")

    figure(11, 1, "bar", printed(11, CAP_115), source="text-layer", numbering="Figure N",
           position="below",
           note="Eighteen glossy steel-blue columns, one per country, on a rotated x axis (US, "
                "China, Japan, Korea, Germany, UK, France, Italy, Canada, Australia, South "
                "Africa, India, Indonesia, Brazil, Saudi Arabia, Mexico, Turkey, Argentina). y 0 "
                "to 600 by 100 with horizontal gridlines only; China at about 550 is the "
                "outlier, Brazil about 270 and Canada about 210. No legend, no colour key, no "
                "axis titles: the nodal influence is encoded in bar height alone, which is why "
                "the drawing is a bar chart and not the node graph the caption's wording "
                "suggests [geometry.family].",
           mention={
               "first_page": 11, "lead_pages": 0, "style": ["Figure 5"], "count": 1,
               "lead_sentence": "From Figure 5, it can be found out that this measure of nodal "
                                "influence correctly shows the worldwide difference",
               "trail_sentence": "", "lead_pattern": "direct", "read_sentences": 1,
               "gap_sentences": None})

    figure(12, 1, "line", printed(12, CAP_126), source="text-layer", numbering="Figure N",
           position="below", layout="1 of 2", legend="outside-right",
           note="Panel (a): the forecast on India. Blue 'actual value' line rising from about 5 "
                "in 1970 to about 150 by 2008 with a spike near 1999, and red '+' forecast "
                "markers scattered below the line from 1985 onward. x 1970 to 2010 in fives, y 0 "
                "to 160 by 20, vertical and horizontal gridlines, legend outside right.",
           mention={
               "first_page": 12, "lead_pages": 0, "style": ["Figure 6"], "count": 1,
               "lead_sentence": "Contained in Figure 6 are two results we get respectively in a "
                                "forecast on India, a geographically adjacent country of China.",
               "trail_sentence": "", "lead_pattern": "direct", "read_sentences": 1,
               "gap_sentences": None})
    figure(12, 2, "line", printed(12, CAP_126), source="text-layer", numbering="Figure N",
           position="below", layout="2 of 2", legend="outside-right",
           note="Panel (b): the forecast on China, on a frame identical to (a) - same 1970-2010 "
                "and 0-160 scales, same gridlines, same outside-right legend, the same blue "
                "actual curve. Only the forecast markers differ: they now form a smooth arc "
                "tracking the line from 1985 (peak about 145 near 1988-1991) instead of the "
                "scattered band in (a), which is what the caption means by removing or not "
                "removing China [geometry.shared_axes].")

    figure(13, 1, "map-or-plan-view", printed(13, CAP_137), source="text-layer",
           numbering="Figure N", position="below", layout="1 of 2",
           note="Panel (a), 1970: a greyscale world choropleth on a geographic basemap - "
                "recognisable continents, individual country polygons, white ocean and a thin "
                "lat/lon graticule of about eight meridians and five parallels. Europe and "
                "North America are the darkest classes and Asia the lightest. No axis titles, "
                "no ticks, no legend box and no colour key of its own: the class palette is "
                "explained only by the sentence 'the darker the color, the more serious the "
                "pollution'. The panel letter '(a)' and the year '1970' print below the frame, "
                "outside it [geometry.legend].",
           mention={
               "first_page": 13, "lead_pages": 0, "style": ["Figure 7"], "count": 1,
               "lead_sentence": "This trend can be easily seen in Figure 7 (a) (b) below.",
               "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
               "gap_sentences": None})
    figure(13, 2, "map-or-plan-view", printed(13, CAP_137), source="text-layer",
           numbering="Figure N", position="below", layout="2 of 2",
           note="Panel (b), 2008: the same basemap and graticule as (a), rescaled by the same "
                "greyscale classes, with the darkest values now over China and East Asia, parts "
                "of South Asia, the Middle East and North Africa while Europe and North America "
                "have lightened - the eastward shift of manufacturing the prose describes. "
                "Panel letter '(b)' and year '2008' below the frame, outside it.")

    figure(14, 1, "line", printed(14, CAP_148), source="text-layer", numbering="Figure N",
           position="below", legend="outside-right",
           note="Autonomous forecast for Japan: blue 'actual value' from about 115 in 1970 down "
                "to about 55 by 1985, back up to about 140 around 1991-92 and then down to about "
                "15 by 2008; red '+' forecast markers cluster on the line for 1985-1992 and then "
                "sit far above it (150-180) for 1993-2008. Same 1970-2010 and 0-160 frame and "
                "outside-right legend as the other case plots.",
           mention={
               "first_page": 14, "lead_pages": 0, "style": ["Figure 8"], "count": 3,
               "lead_sentence": "Figure 8 is the plot we get from an autonomous forecast by our "
                                "model.",
               "trail_sentence": "the warnings shown in Figure 8 indicates that the result "
                                 "might be very serious.",
               "lead_pattern": "figure-n-shows", "read_sentences": 3,
               "gap_sentences": None})

    figure(15, 1, "line", printed(15, CAP_159), source="text-layer", numbering="Figure N",
           position="below", legend="outside-right",
           note="Autonomous forecast for India. The artwork is the p12 panel (a) reused almost "
                "pixel for pixel - same blue curve, same scattered red markers, same 1970-2010 "
                "and 0-160 frame - printed again under its own caption, so it is a second "
                "printed exhibit and not a duplicate region: the paper prints Figure 6(a) as the "
                "sensitivity result and Figure 9 as the India case study from the same forecast "
                "file.",
           mention={
               "first_page": 14, "lead_pages": 1, "style": ["Figure 9"], "count": 1,
               "lead_sentence": "Figure 9 is the plot we get from an autonomous forecast by our "
                                "model in which no condition has changed except the nation.",
               "trail_sentence": "", "lead_pattern": "figure-n-shows", "read_sentences": 1,
               "gap_sentences": None})
    figure(15, 2, "line", printed(15, CAP_1510), source="text-layer", numbering="Figure N",
           position="below", legend="outside-right",
           note="Autonomous forecast for Hungary, the one case plot on a different scale: y runs "
                "0 to 200 by 20 where the others stop at 160. Blue 'actual value' about 120 in "
                "1970, peaking near 160 in 1979, easing to about 90 by 1999 and collapsing to "
                "near zero after 2005; red '+' markers track it to 1995 and then sit at 180-210 "
                "through 2008. x 1970-2010 in fives, gridlines both ways, legend outside right.",
           mention={
               "first_page": 15, "lead_pages": 0, "style": ["Figure 10"], "count": 1,
               "lead_sentence": "Figure 10 is the plot from the autonomous of our model (start "
                                "from 1985).",
               "trail_sentence": "", "lead_pattern": "figure-n-shows", "read_sentences": 1,
               "gap_sentences": None})

    rules = [
        "Every exhibit in this paper carries a flat number - 'Figure 1' to 'Figure 10' and "
        "'Table 1' to 'Table 3' - so unlike the previous papers in this range the enum fits, "
        "and only Figure 1 needs the colon form 'Figure N:' because it prints 'Figure 1:' "
        "[caption.numbering].",
        "Three of the four tables caption themselves with the bare word ('Table 1', 'Table 2', "
        "'Table 3') and print no title line at all, so the title the reader sees is the one in "
        "the note and not in the caption [caption.verbatim].",
        "Table 1 is a pasted colour raster whose bands are separated by fill and white gaps "
        "rather than by rules, so `rule_style` is `no-rules` and `zebra` is false even though "
        "the bands alternate in colour [table.rule_style].",
        "Table 3 is the only table with a vertical rule (between its Input and Output halves) "
        "and the only one with a two-row spanner header, so it alone records `merged_cells` "
        "[table.merged_cells].",
        "The two p12 panels and the two p13 panels are separate measured regions with separate "
        "frames, so each gets its own row with a panel layout rather than being folded into one "
        "`composite-panel` [geometry.panel_layout].",
        "p13's panels are world choropleths on a graticule basemap with no key of their own, "
        "recorded `map-or-plan-view`; p11's caption says 'Identifying the critical nodes' but the "
        "drawing is an eighteen-column bar chart, so the family follows the ink "
        "[geometry.family].",
        "Figure 9 on p15 reprints the Figure 6(a) artwork nearly pixel for pixel under its own "
        "caption; it is counted once as a printed exhibit per caption, and the reuse is declared "
        "in the note rather than silently dropped [caption.verbatim].",
        "All six case-study plots share one template - 1970-2010 x axis, blue actual line, red "
        "'+' forecast markers, outside-right legend - except that Figure 10's y axis runs to 200 "
        "where the others stop at 160, so the scale is read per region and not assumed "
        "[geometry.legend].",
        "Figure 2's three panels print as three separate small rasters in one row under one "
        "caption that splits them into '(a) (b)' and '(c)', so the caption is repeated verbatim "
        "on all three rows and the split is explained in each note [caption.verbatim].",
        "Every heading is numbered (1.2.2, 2.2.1, 3.4, 3.5), so `section_path` quotes the "
        "printed heading and `section_numbered` is true throughout; p4 needs two routes because "
        "Figure 2 sits under 1.2.2 and Table 1 under 1.3 [place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2013\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "\u5176\u4ed6\u5956\u9879/C-21165-Finalist.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Seventeen measured regions over eleven pages, all accounted: 14 figure rows and 3 "
            "printed tables, no exclusions. The paper numbers its exhibits flatly - Figure 1 to "
            "Figure 10, Table 1 to Table 3 - which is the first paper in this run whose numbering "
            "fits the enum without a note. Figure 2 prints its three panels as three separate "
            "measured rasters under one caption that splits them into '(a) (b)' under 'The "
            "Increasing rates of change in human activity' and '(c)' under 'Global scale "
            "changes'; Figures 6 and 7 each print two panels as two separate regions with two "
            "identical frames. The tables are of three different constructions: Table 1 is a "
            "pasted colour raster with no rules, Table 2 a booktabs notation list, Table 3 a "
            "spanner-header grid with one vertical rule. One artwork is printed twice: the p15 "
            "Figure 9 plot is the p12 Figure 6(a) forecast reused almost pixel for pixel, so the "
            "family and the row are separate per caption but the note says the drawing repeats. "
            "No exhibit lacks a citing sentence except Figure 4, which is introduced by prose "
            "and never named. No declared gaps: the layout pass measures nothing on the pages "
            "that carry only prose."
        ),
    }
    out = PROXY / "pc50-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
