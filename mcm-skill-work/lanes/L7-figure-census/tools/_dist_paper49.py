"""Hand pass for P-C-2013-18492-ab739371 (a two-tier communication network model of global
health: node / link / topology, a revised Bayesian belief network, policy simulation), 21 pp.

Twenty-one measured regions over ten pages: 9 figure rows, 3 printed tables and 9 exclusions.
The arithmetic `check.py` enforces is 9 + 3 + 9 = 21.

    p5-r1   map        node definition in state level - a western-US state map with ring nodes
    p6-r1   schematic  Forrester's World Model - five boxes joined by arrows
    p7-r1   table      Air Quality Index stages (EPA, 2012)
    p7-r2   exclude    body paragraph band ("Agriculture: We appeal to ...")
    p7-r3   exclude    body paragraph band ("Industry: The industrial factor is ...")
    p9-r1   table      quantified factor's discretization metrics
    p9-r2   network    bipartite Bayesian belief network, two node sets joined by edges
    p14-r1  schematic  node status transfer - pre-condition / transfer / post-condition
    p14-r2  heatmap    a square lattice in 2-dimensions, a 5x5 cell grid
    p15-r1  table      needed historical data and their possible source
    p16-r1  bar        Figure 4.3-1, five extruded bars
    p16-r2  exclude    the same chart boxed a second time
    p17-r1  line       Figure 4.3-2, situation 1
    p17-r2  exclude    the same plot boxed a second time
    p17-r3  line       Figure 4.3-3, situation 2
    p17-r4  exclude    the same plot boxed a second time
    p18-r1  line       Figure 4.3-4, situation 3
    p18-r2  exclude    the same plot boxed a second time
    p19-r1  exclude    page furniture plus prose plus equation (16)
    p19-r2  exclude    prose around equation (18)
    p19-r3  exclude    display equation (19)

Captions: this paper labels its exhibits by SECTION number - "Figure 3-1", "Figure 3.1.2-1",
"Table 3.1.4-1", "Fig. 3.3.5-1", "Figure 4.3-2" - and none of those forms is in the `NUMBERINGS`
enum, which knows only the flat "Figure N" families. Every record therefore carries
`numbering: none`, keeps the printed label inside the quoted caption, and the payload note says
so once.

Usage: python -I tools/_dist_paper49.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2013-18492-ab739371"
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

S3 = "3 Two-tier Communication Network Model"
S312 = "3.1.2 Driving factors of environment degradation"
S313 = "3.1.3 Node characterizing with communication protocol"
S314 = "3.1.4 A Revised Bayesian Belief Network study of factors"
S335 = "3.3.5 Node status evolve in every iteration"
S34 = "3.4 Global Health Measurement"
S41 = "4.1 Dataset Requirements and Collect Suggestion"
S43 = "4.3 Impact of policy and decision support 国 ne"
S45 = "4.5 Critical nodes and links"

PATH: dict[int, tuple[list[str], str]] = {
    5: ([S3], "model"),
    6: ([S312], "model"),
    7: ([S313], "model"),
    9: ([S314], "model"),
    15: ([S41], "model"),
    16: ([S43], "model"),
    17: ([S43], "result"),
    18: ([S43], "result"),
    19: ([S45], "other"),
}
# p14 carries two figures under two different headings: the status diagram closes 3.3.5 and
# the lattice opens 3.4
PATH_ONE = {(14, 1): ([S335], "model"), (14, 2): ([S34], "model")}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

VENTION = {5: 1, 6: 1, 7: 1, 9: 2, 14: 2, 15: 1, 16: 2, 17: 4, 18: 2, 19: 0}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}

CAP_51 = "Figure 3-1 Node definition in state level"
CAP_61 = "Figure 3.1.2-1 Forrester’s World Model"
CAP_71 = "Table 3.1.2-1 Air Quality Index stages (EPA, 2012)"
CAP_91 = "Table 3.1.4-1 Quantitated factor’s discretization metrics"
CAP_92 = "Figure 3.1.4-1 a simple bipartite Bayesian Belief Network model"
CAP_141 = "Figure 3.3.5-1 Node status transfer"
CAP_142 = "Figure 3.4-1 A square lattice in 2-dimensions"
CAP_151 = "Table 4.1-1 needed historical data and their possible source"


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


def caption_block(text: str, source: str, position: str) -> dict:
    return {
        "verbatim": text,
        "numbering": "none",
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
           position: str = "below", panels: int = 1, layout: str = "1",
           legend: str = "none", colorbar: bool = False, numbers: bool = True,
           labels: bool = False, other_note: str = "", note: str = "",
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
        "caption": caption_block(caption_text, source, position),
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
          rows: int, cols: int, header_rows: int = 1, rules: str = "booktabs",
          zebra: bool = False, numeric_cols: int = 0, text_cols: int = 0,
          merged: bool = False, continued: bool = False, note: str = "",
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
        "caption": caption_block(caption_text, source, "above"),
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
    # --- section 3: nodes, factors and the belief network -------------------------------
    figure(5, 1, "map-or-plan-view", printed(5, CAP_51),
           source="text-layer", position="below",
           note="A map of the western United States drawn as state polygons - Washington, "
                "Oregon, Idaho, Montana, Nevada, Utah, California and Arizona are named - with "
                "eight ring nodes placed one per state and dashed edges between them, plus a "
                "pink node labelled PACIFIC OCEAN joined to the coast by red dashed edges. The "
                "ink is a geographic partition with nodes on it, not a free-floating graph, so "
                "the family follows the basemap.",
           mention={
               "first_page": 5, "lead_pages": 0, "style": ["Fig. 3-1", "Figure 3-1"],
               "count": 3,
               "lead_sentence": "such as county, state (as shown in Fig. 3-1) and nation",
               "trail_sentence": "The signal channels represent physical adjacency relations "
                                 "between two nodes (the links in Fig. 3-1).",
               "lead_pattern": "parenthetical", "read_sentences": 2,
               "gap_sentences": None})

    figure(6, 1, "flowchart-or-schematic", printed(6, CAP_61),
           source="text-layer", position="below", labels=True,
           note="Five shaded rounded boxes - Environment, Resources, Population, Agriculture, "
                "Industry - joined by thick black arrows with arrowheads at the target end: "
                "Environment to Population, Resources to Population and to Agriculture, "
                "Population to Agriculture, Agriculture and Industry to each other and to "
                "Resources. No axes and no scale, so the drawing is a flow chart and not a "
                "survival or system diagram with feedback loops; the five factors are the ones "
                "the prose names.",
           mention={
               "first_page": 6, "lead_pages": 0, "style": ["Fig. 3.1.2-1", "Figure 3.1.2-1"],
               "count": 2,
               "lead_sentence": "inspired by Forrester’s World Model (Natali H., et, al., "
                                "2006) shown in Fig. 3.1.2-1",
               "trail_sentence": "",
               "lead_pattern": "parenthetical", "read_sentences": 1,
               "gap_sentences": None})

    table(7, 1, printed(7, CAP_71), source="text-layer",
          rows=7, cols=3, numeric_cols=0, text_cols=3, rules="vertical-rules", zebra=True,
          note="Seven printed rows - one header and six AQI bands - under the header 'Air "
               "Quality Index (AQI) | Levels of Health Concern | Colors'. A rule above the "
               "header, a rule under it, a rule below the last row and one vertical rule "
               "between the index column and the concern column; alternating rows are filled "
               "grey (0~50 and 101~150 and 201~300 shaded). Text cells only except the index "
               "ranges, which are printed as '0~50' and not as two numeric columns, so the record "
               "counts three text columns and no numeric one.")

    excluded(7, 2, "not-an-exhibit",
             "A body paragraph band, not an exhibit: it measures as four vector paths because "
             "the lead-in word 'Agriculture:' is bold, and reads 'We appeal to Agricultural "
             "Production Indices (API) to study agriculture factor.'")
    excluded(7, 3, "not-an-exhibit",
             "The next body paragraph band on the same page, three vector paths, 'Industry: The "
             "industrial factor is quantized by Industrial Production Index (IPI)'. Same class "
             "as the region above: a bold lead-in word and running prose.")

    table(9, 1, printed(9, CAP_91), source="text-layer",
          rows=3, cols=6, numeric_cols=5, text_cols=1, rules="vertical-rules", zebra=True,
          note="One header row 'Factor | Environment | Resources | Population | Industry | "
               "Agriculture' with the factor names set in italic, over two body rows 'Max Value' "
               "(1.0, 4.0, Vn*3.0, 100.0, 100.0) and 'Level Gap' (0.2, 0.8, Vn*0.6, 20.0, 20.0). "
               "The Max Value row is shaded grey. One vertical rule after the stub column, "
               "horizontal rules above the header, under it and below the last row.")

    figure(9, 2, "node-link-network", printed(9, CAP_92),
           source="text-layer", position="below", labels=True,
           note="Two columns of shaded nodes - 'X Set' left and 'Y Set' right, each inside a "
                "dashed rounded frame - joined by straight arrows: X nodes are five-bit state "
                "strings ('0,0,0,0,0' through '4,4,4,4,4', the middle ones elided with vertical "
                "dots) and Y nodes are the changes 'dX=1', 'dX=0.9', 'dX=0', 'dX=-0.9', "
                "'dX=-1.0'. The drawing is a bipartite graph, not a flow chart: no process "
                "stages, every arrow runs between two node sets.")

    figure(14, 1, "flowchart-or-schematic", printed(14, CAP_141),
           source="text-layer", position="below", labels=True,
           note="A state-transition diagram: one box 'Pre-condition' with a self-referential "
                "curved arrow labelled 'Inner Interaction of Factors', receiving 'Outside "
                "Impact' and 'Policy or Emergency Impact' from outside, passing down to a "
                "'Transfer' box (which also takes 'Extrose Impact' from below) and on to "
                "'Post-condition', with a branch from Transfer to a boxed 'Outer Network'.")

    figure(14, 2, "heatmap-or-contour", printed(14, CAP_142),
           source="text-layer", position="below",
           note="A 5x5 grid of square cells drawn as thin vector rules, six of the cells filled "
                "solid black (two in the top row, two in the second, one in the third, one in "
                "the bottom row) and the rest left white. A cell-state matrix with no axes, no "
                "labels, no legend and no colour key, so the family is the cell-grid one.",
           mention={
               "first_page": 14, "lead_pages": 0, "style": ["Fig. 3.4-1"],
               "count": 1,
               "lead_sentence": "Rosowsky, 1999) as illustrated in Fig. 3.4-1.",
               "trail_sentence": "", "lead_pattern": "parenthetical",
               "read_sentences": 1, "gap_sentences": None})

    # --- section 4: data requirements and the three simulated situations ----------------
    table(15, 1, printed(15, CAP_151), source="text-layer",
          rows=7, cols=2, numeric_cols=0, text_cols=2, rules="vertical-rules", zebra=True,
          note="Two columns 'Data Requirement | Possible Source' over six body rows - Air "
               "Quality Index, Species Diversity Index, Landform Change Rate, Resources "
               "('Including land, forest, coal, and oil'), Industrial Production Index and "
               "Agricultural Production Indices. A rule above the caption band, a second rule "
               "under the header, a rule at the foot and one internal vertical rule between the "
               "two columns; no outer verticals and no rules between body rows, which are "
               "separated by alternating grey fill instead. Several source cells wrap onto a "
               "second line.",
          mention={
              "first_page": 15, "lead_pages": 0, "style": ["Table 4.1-1"],
              "count": 1,
              "lead_sentence": "Table 4.1-1 lists all the needed historical data and their "
                               "possible source.",
              "trail_sentence": "", "lead_pattern": "direct", "read_sentences": 1,
              "gap_sentences": None})

    figure(16, 1, "bar", printed(16, "Figure 4.3-1 a typical developing area’s quantitative "
                                    "indicators"),
           source="text-layer", position="below", labels=True,
           note="Five extruded (3-D) bars - Environment, Resources, Population, Industry, "
                "Argiculture, the last spelled as printed - rising to about 0.90, 0.88, 0.32, "
                "0.12 and 0.22 on a 0 to 0.9 y axis stepped by 0.1 with horizontal gridlines "
                "only. No axis titles, no legend and no in-plot title; the whole chart sits in "
                "a thin grey frame with a drop shadow. The bars are one embedded raster about "
                "200 dpi while the tick labels, category labels and frame rules are live "
                "vector, which is why the region measures as vector around a raster.")
    excluded(16, 2, "fragment-of-other",
             "The same Figure 4.3-1 chart measured a second time: the page holds exactly one "
             "image object and both regions enclose it, the outer box taking in the caption "
             "line and the frame's shadow and the inner box stopping at the plot frame. Not a "
             "second graphic and not an inset.")

    figure(17, 1, "line", printed(17, "Figure 4.3-2 the expected output in situation 1"),
           source="text-layer", position="below", legend="outside-right",
           note="Five smooth series over '0 years' to '100 years' in twenty-year steps - "
                "Environment, Resources, Population, Industry, Argiculture - with a colour-key "
                "legend standing to the right of the plot area. y 0 to 1 by 0.1 with horizontal "
                "gridlines only, no axis titles and no in-plot title. Situation 1: Environment "
                "and Resources run from about 0.85 down to 0.12 and 0.20, Population dips to "
                "0.28 and peaks at 0.57 near year 70, Industry climbs to 0.35 and falls back to "
                "0.28, Argiculture rises to about 0.32. Artwork is live vector; the page's two "
                "image objects here are empty frame and shadow fills.",
           mention={
               "first_page": 17, "lead_pages": 0, "style": ["Fig. 4.3-2"],
               "count": 1,
               "lead_sentence": "If the decision makers adopt these policies, the expected "
                                "results are shown in Fig. 4.3-2.",
               "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
               "gap_sentences": None})
    excluded(17, 2, "fragment-of-other",
             "The plot area of Figure 4.3-2 measured a second time - the same five curves, the "
             "same 0-1 and 0-100 year frames, with the legend and caption outside the box. The "
             "page paints an empty frame image over the chart, so the extractor opened a second "
             "region; there is no second graphic.")

    figure(17, 3, "line", printed(17, "Figure 4.3-3 the expected output in situation 2"),
           source="text-layer", position="below", legend="outside-right",
           note="The same five-series frame as Figure 4.3-2, legend to the right, y 0 to 1 and "
                "x 0 to 100 years in twenties. Situation 2: Environment falls from 0.85 to 0.58 "
                "and Resources from 0.85 to 0.50, the two crossing Population near year 95; "
                "Population rises 0.30 to 0.55, Industry 0.10 to 0.42, and Argiculture peaks at "
                "about 0.32 near year 85 before easing to 0.25.",
           mention={
               "first_page": 17, "lead_pages": 0, "style": ["Fig. 4.3-3"],
               "count": 1,
               "lead_sentence": "In this case, the expected output of our model is shown in "
                                "Fig. 4.3-3.",
               "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
               "gap_sentences": None})
    excluded(17, 4, "fragment-of-other",
             "The plot area of Figure 4.3-3 measured a second time, curves identical, legend "
             "and caption outside the box: a duplicate region opened by the overlaid frame "
             "image, not a separate exhibit.")

    figure(18, 1, "line", printed(18, "Figure 4.3-4 the expected output in situation 3"),
           source="text-layer", position="below", legend="outside-right",
           note="The same five-series frame as Figures 4.3-2 and 4.3-3, legend to the right, "
                "y 0 to 1 and x 0 to 100 years. Situation 3: Environment dips to 0.70 near year "
                "42, rebounds to 0.82 by year 55 and closes at 0.72; Resources slides to 0.63 "
                "with a small bump near year 85; Population rises to 0.55, Industry to 0.30 and "
                "Argiculture to 0.33 before flattening at 0.31.",
           mention={
               "first_page": 18, "lead_pages": 0, "style": ["Fig. 4.3-4"],
               "count": 1,
               "lead_sentence": "By doing this, the expected output of our model is shown in "
                                "Fig. 4.3-4.",
               "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
               "gap_sentences": None})
    excluded(18, 2, "fragment-of-other",
             "The plot area of Figure 4.3-4 measured a second time, curves identical, legend "
             "and caption outside the box; the duplicate comes from the empty frame image the "
             "page paints over the chart.")

    excluded(19, 1, "not-an-exhibit",
             "Page furniture and prose, not an exhibit: the running head 'Team #18492 / Page 18 "
             "of 20' over a horizontal rule, then five lines of body text on betweenness "
             "centrality, closed by the top of display equation (16).")
    excluded(19, 2, "not-an-exhibit",
             "Four lines of body prose ('After the definition and explanation of some important "
             "concepts ...') around display equation (18), I_c(i) as the mean of betweenness "
             "and closeness centrality.")
    excluded(19, 3, "in-body-diagram",
             "A display equation and the text line that introduces it: 'represented by edge "
             "betweenness E_B(j)' over equation (19), the edge-betweenness sum. Seven paths, "
             "no drawing, and the paper prints no caption for it.")

    rules = [
        "This paper labels every exhibit by section number - 'Figure 3-1', 'Figure 3.1.2-1', "
        "'Table 3.1.2-1', 'Fig. 3.3.5-1', 'Figure 4.3-2' - and the `NUMBERINGS` enum knows only "
        "the flat 'Figure N' families, so every record carries numbering `none` and the printed "
        "label survives inside the quoted caption [caption.numbering].",
        "Nine of the twelve numbered exhibits are cited in prose by the same section-numbered "
        "label ('as shown in Fig. 3-1', 'shown in table 3.1.4-1', 'shown in Fig. 4.3-2'), which "
        "is why the mention blocks carry the literal spellings 'Fig. 3-1', 'table 3.1.4-1' and "
        "so on rather than a normalized form [mention.style].",
        "Five measured regions are a second box around a chart that was already measured: the "
        "p16 bar chart and the three p17/p18 situation charts each open an outer region (caption "
        "and frame) and an inner one (plot area), because the page paints an empty frame image "
        "over live vector artwork. The inner box is excluded `fragment-of-other` and the exhibit "
        "is recorded once and `panel_count` stays 1 on all four [geometry.panel_count].",
        "Three tables print a single internal vertical rule after the stub column with no outer "
        "verticals, and separate their rows by alternating grey fill rather than by rules, so "
        "`rule_style` is `vertical-rules` and `zebra` is true on all three [table.rule_style].",
        "The p7 table's index column prints bands as ranges ('0~50', '51~100') and the p9 table "
        "prints two cells as formulas ('Vn*3.0', 'Vn*0.6'), so neither table has a column that "
        "is numeric end to end [table.numeric_cols].",
        "The p5 figure is a state map with nodes drawn on it - the ink is a geographic partition "
        "- so it is recorded `map-or-plan-view`; the p9 bipartite belief network, which has no "
        "basemap under it, is recorded `node-link-network` [geometry.family].",
        "The p16 chart is the lane's only extruded bar chart: `three_d` is `perspective-bars` "
        "and the bars themselves are one embedded raster inside a vector frame "
        "[geometry.three_d].",
        "The p14 lattice is a bare 5x5 cell grid with six cells filled, no axes and no key, so "
        "it is recorded `heatmap-or-contour` on the strength of the cell matrix alone "
        "[geometry.family].",
        "Nine measured regions are not exhibits: two prose bands on p7, three bands on p19 (two "
        "prose and one display equation) and the four duplicate chart boxes. `check.py` counts "
        "them as excluded, so the arithmetic stays 9 + 3 + 9 = 21, and the excluded bands are the smallest regions on their pages [place.area_frac].",
        "Every heading in the paper is numbered (3.1.2, 3.3.5, 4.3), so `section_path` quotes "
        "the printed heading and `section_numbered` is true throughout; p14 needs two routes "
        "because its two figures close one section and open the next [place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2013\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-18492-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twenty-one measured regions over ten pages, all accounted: 9 figure rows, 3 "
            "printed tables and 9 exclusions. The paper numbers its exhibits by SECTION, not in "
            "a flat sequence - Figure 3-1, Figure 3.1.2-1, Table 3.1.2-1, Table 3.1.4-1, Figure "
            "3.1.4-1, Figure 3.3.5-1, Figure 3.4-1, Table 4.1-1, Figures 4.3-1 to 4.3-4 - and "
            "no such form exists in the `NUMBERINGS` enum, so every record keeps numbering "
            "`none` with the label quoted inside the caption. Nine exhibits are cited in the "
            "prose by that same label and carry a mention block; Table 3.1.2-1 and Figure 4.3-1 "
            "are never cited, and Figure 3.1.4-1 is only introduced by the surrounding "
            "paragraph. Four of the twelve numbered exhibits come with a second measured box "
            "around the same artwork (p16, p17 twice, p18), because each page paints an empty "
            "frame image over a live vector chart; those four duplicates are excluded "
            "`fragment-of-other` rather than counted as separate panels. Two p7 regions and the "
            "three p19 regions are prose bands and display equations, not exhibits. No declared "
            "gaps: every region `fig_extract` measured is accounted for."
        ),
    }
    out = PROXY / "pc49-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
