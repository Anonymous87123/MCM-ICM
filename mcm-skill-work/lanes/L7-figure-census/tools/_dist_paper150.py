"""Hand pass for P-B-2018-77238-4380ec81 (2018 MCM B, "Team 77238", language
development over 50 years plus an office-siting model).

23 pages, 50 measured regions on 18 of them. The paper prints seventeen numbered
exhibits plus an unnumbered notation grid and a memo grid; several of its tables are
native text that the region pass never boxes, so the tables recorded here are the ones
the detector actually measured.

Usage: python -I tools/_dist_paper150.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2018-77238-4380ec81"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
REG = {(pg["page"], i): list(r["bbox"])
       for pg in LAYOUT["pages"] for i, r in enumerate(pg["regions"], 1)}
MEASURED = {(p, tuple(b)) for (p, _), b in REG.items()}


def bb(page: int, index: int) -> tuple[int, list[float]]:
    return page, REG[(page, index)]


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    w, h = DIMS[page]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < h / 3 else ("middle" if mid < 2 * h / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    return {
        "section_path": list(path),
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


def mention(page: int, *, first: int | None, style: list[str], count: int = 0,
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
           kind: str, note: str = "", caption_source: str = "text-layer",
           panel_of: str = "", other_note: str = "") -> dict:
    page, bbox = B[key]
    item = {
        "page": page,
        "bbox": bbox,
        "family": geom["family"],
        "confidence": "high",
        "panel_count": geom["panel_count"],
        "is_panel_of": panel_of,
        "caption_verbatim": caption["verbatim"],
        "caption_source": caption_source,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }
    if other_note:
        item["other_note"] = other_note
    return item


def grid(rows: int, cols: int, *, header: int = 1, numeric: int = 0, txt: int = 1,
         rule: str = "booktabs", zebra: bool = False, merged: bool = False,
         diagonal: bool = False, units_in_header: bool = False, decimal: bool = False,
         width: str = "full", continued: bool = False, note: str = "") -> dict:
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
        "continued": continued,
        "note_sentence": note,
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          note: str = "", caption_source: str = "text-layer") -> dict:
    if caption["numbering"] == "Figure N":
        caption = dict(caption, numbering="Table N")
    if caption["position"] == "below":
        caption = dict(caption, position="above")
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


def uncap(position: str = "above") -> dict:
    """An exhibit the paper prints with no caption line of its own."""
    return cap("", "none", position=position)


FIGURES: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[tuple[str, tuple[int, list[float]], str]] = []
B: dict[str, tuple[int, list[float]]] = {}

S_NOTATION = ["3 Notation"]
S_41 = ["4 Model", "4.1 Language Development Model"]
S_411 = S_41 + ["4.1.1 Judgment Process"]
S_412 = S_41 + ["4.1.2 Stochastic Simulation Process"]
S_42 = ["4 Model", "4.2 Location Determination Model"]
S_421 = S_42 + ["4.2.1 Solution Oriented by Language Structure"]
S_422 = S_42 + ["4.2.2 Solution Oriented by Geographic Condition"]
S_511 = ["5 Sensitivity Analysis",
         "5.1 Sensitivity Analysis on Language Development Model",
         "5.1.1 Net Birth Rate Impact"]
S_512 = ["5 Sensitivity Analysis",
         "5.1 Sensitivity Analysis on Language Development Model",
         "5.1.2 GDP Growth Rate Impact"]
S_513 = ["5 Sensitivity Analysis",
         "5.1 Sensitivity Analysis on Language Development Model",
         "5.1.3 Migration Rate Impact"]
S_515 = ["5 Sensitivity Analysis",
         "5.2 Sensitivity Analysis on Location Determination Model"]
S_6 = ["6 Further Discussion"]
S_MEMO = ["Memo to the Service Company"]
B.update({
    "tnot": bb(4, 1),
    "f1": bb(4, 2),
    "f2": bb(5, 1),
    "f3": bb(5, 3),
    "f4": bb(6, 2),
    "f5": bb(7, 1),
    "f6a": bb(8, 2),
    "f6b": bb(8, 3),
    "f7": bb(9, 1),
    "f8a": bb(10, 1),
    "f8b": bb(10, 2),
    "f9a": bb(10, 3),
    "f9b": bb(10, 4),
    "f10": bb(13, 3),
    "f11": bb(14, 1),
    "t5b": bb(13, 1),
    "t6": bb(13, 2),
    "t7": bb(14, 6),
    "t8": bb(14, 7),
})

EXCLUDED += [
    ("p4 left node box of Figure 1", bb(4, 3), "fragment-of-other"),
    ("p4 bottom node box of Figure 1", bb(4, 4), "fragment-of-other"),
    ("p4 decision diamond of Figure 1", bb(4, 5), "fragment-of-other"),
    ("p4 lower node box of Figure 1", bb(4, 6), "fragment-of-other"),
    ("p5 lower row of Figure 2 (three score ovals)", bb(5, 2), "fragment-of-other"),
    ("p9 caption and lead-in band under Figure 7", bb(9, 2), "caption-background"),
    ("p11 the angle-cosine similarity formula", bb(11, 1), "not-an-exhibit"),
    ("p11 the office criterion expression", bb(11, 2), "not-an-exhibit"),
    ("p11 the max-form objective function", bb(11, 3), "not-an-exhibit"),
    ("p14 node box of Figure 11 (initial office number)", bb(14, 2), "fragment-of-other"),
    ("p14 decision diamond of Figure 11", bb(14, 3), "fragment-of-other"),
    ("p14 node box of Figure 11 (objective function)", bb(14, 4), "fragment-of-other"),
    ("p14 node box of Figure 11 (P Center grouping)", bb(14, 5), "fragment-of-other"),
]

FIGURES += [
    figure("f1",
           cap("Figure 1 Judgment process of Language Development Model"),
           mention(4, first=4, style=["Figure 1"], count=1, pattern="as-shown-in",
                   lead="The judgment process of our Language Development Model is shown in "
                        "Figure 1."),
           geo("flowchart-or-schematic"),
           path=S_411, kind="model",
           note="the paper's first drawing and the only one that explains the model's own "
                "logic: a rectangle for the newly-born cohort, a diamond asking whether they "
                "speak a second language, a second diamond asking which one, four language "
                "branches on the right and a dead-end box below for the monolinguals, with "
                "the two branch labels (A_i) and (1-A_i) printed on the edges. Only the "
                "central body of the flowchart comes back as one measured region; its four "
                "node boxes are boxed separately and recorded as fragments"),
    figure("f2",
           cap("Figure 2 Principle to determine whether one speaks a second language"),
           mention(5, first=None, style=[]),
           geo("flowchart-or-schematic", labels=True),
           path=S_411, kind="model",
           note="a two-level tree that does the arithmetic of the second-language decision: "
                "Second Language Percentage splits 50/50 into the communicative factor and "
                "GDP per capita, and the left branch lands on Diversity (Score=number/16) "
                "while the right lands on three score ovals (Developed 0.4, Developing 0.6, "
                "Backward 0.2). Two measured regions, the top half and the oval row, of one "
                "chart; the oval row is excluded as a fragment"),
    figure("f3",
           cap("Figure 3 Classification of countries according to GDP per capita"),
           mention(5, first=None, style=[]),
           geo("scatter", labels=True),
           path=S_411, kind="model",
           note="a rank-ordered scatter of GDP per capita against rank for about 52 "
                "countries, with the three class boundaries annotated in place ('Developed "
                "Country 4', 'Developing Country 23', 'Backward Country 64') and two dashed "
                "reference lines labelled Mean = 14100 and Median = 5900. The one exhibit in "
                "the paper that prints its own thresholds inside the plot area"),
    figure("f4",
           cap("Figure 4 Sections and their weight when determining which second language "
               "to speak"),
           mention(6, first=6, style=["Figure 4"], count=1, pattern="as-shown-in",
                   lead="The sections we consider together with their weight is shown in "
                        "Figure 4 below."),
           geo("flowchart-or-schematic", labels=True),
           path=S_411, kind="model",
           note="an AHP weight tree: five factor boxes across the top (Communication 34.16%, "
                "Geography 19.67%, Economy 34.16%, Knowledge 7.32%, Diplomacy 4.69%) each "
                "splitting into two or three parameter boxes, every box carrying its "
                "percentage. The percentages are printed as data labels, so this is the one "
                "exhibit whose numbers sit inside the artwork rather than on an axis"),
    figure("f5",
           cap("Figure 5 Determination of which second language to speak"),
           mention(7, first=None, style=[]),
           geo("other", numbers=True, labels=True),
           path=S_412, kind="solution",
           other_note="a one-dimensional interval strip, not a chart: a horizontal line "
                      "ruled 0.000 to 1.000 with vertical ticks at the cumulative language "
                      "boundaries (English up to 0.608, French to 0.741, Spanish to 0.790) "
                      "and a red arrow at 0.725 showing where one random draw falls. No "
                      "family in the vocabulary covers an axis-only number line, so it is "
                      "filed 'other'",
           note="the mechanism of the simulation in one line: a random value between 0 and 1 "
                "picks a language by falling inside its interval. The red 0.725 and its arrow "
                "are the only colour in the drawing"),
    figure("f6a",
           cap("Figure 6 Change of total number and rank of the 16 languages over 50 years"),
           mention(8, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_412, kind="solution",
           note="left half of a two-frame plate: total speakers 0-3.5e9 on a 2017-2067 time "
                "axis, sixteen curves keyed in a box inside the upper right, English and "
                "Chinese separating from the other fourteen by an order of magnitude. The "
                "ordinate prints scientific notation without a unit"),
    figure("f6b",
           cap("Figure 6 Change of total number and rank of the 16 languages over 50 years"),
           mention(8, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_412, kind="solution",
           note="right half of the same plate: rank 0-16 from top to bottom against the same "
                "years, drawn as flat steps that jump when two languages cross. The two "
                "frames share neither axis nor caption, which is why the detector measured "
                "them as two regions"),
    figure("f7",
           cap("Figure 7 Change of language distribution around the world"),
           mention(9, first=None, style=[]),
           geo("map-or-plan-view", panels=4, layout="4x1", legend="outside-right",
                numbers=False, labels=True),
           path=S_412, kind="solution",
           note="four stacked Robinson-projection world maps for 2017, 2030, 2050 and 2067, "
                "each a bubble map of sixteen languages sized by speaker count, with the "
                "sixteen-entry key printed once OUTSIDE the maps at the right and the year "
                "stamped in red under each frame. The only exhibit in the paper whose legend "
                "sits outside the artwork, and the only one that leaves a page's middle band "
                "entirely to a single image"),
    figure("f8a",
           cap("Figure 8 Change of number of native speakers and rank of 16 languages over "
               "50 years"),
           mention(10, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_412, kind="solution",
           note="left half of the native-speaker plate: 0-1.4e9, sixteen curves keyed inside "
                "the upper right. Compared with Figure 6's total-speaker frame the same "
                "sixteen languages produce a smoother, lower bundle"),
    figure("f8b",
           cap("Figure 8 Change of number of native speakers and rank of 16 languages over "
               "50 years"),
           mention(10, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_412, kind="solution",
           note="right half of the same plate: native-speaker rank 0-16, the step lines far "
                "more broken than Figure 6's because the 'dominant language' shortcut makes a "
                "country jump class when its prevailing language changes"),
    figure("f9a",
           cap("Figure 9 Simulation result when take migration into account"),
           mention(10, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_412, kind="solution",
           note="left half of the migration plate: total speakers 0-2.0e9, sixteen curves "
                "keyed inside the upper right. The title inside the frame still reads 'Total "
                "Speaker Number Over Time', so the migration run is distinguishable from the "
                "baseline only by its ordinate ceiling"),
    figure("f9b",
           cap("Figure 9 Simulation result when take migration into account"),
           mention(10, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_412, kind="solution",
           note="right half of the migration plate: native speakers 0-1.2e9. The three "
                "panels of Figures 6, 8 and 9 are the same template - sixteen keyed curves, "
                "years on x - printed six times across pp8-10"),
    figure("f10",
           cap("Figure 10 The grouping process"),
           mention(13, first=None, style=[]),
           geo("node-link-network", labels=True),
           path=S_422, kind="solution",
           note="a hand-drawn six-node example of the P-center split: two filled reference "
                "countries A and B, the candidate C above them, the other countries in grey, "
                "and the two distances d_AC and d_BC lettered on the edges, with a sentence "
                "printed under the drawing ('Because d_AC<d_BC, C is grouped in the second "
                "group.'). The only exhibit in the paper that carries its own reading inside "
                "the artwork"),
    figure("f11",
           cap("Figure 11 Process of solution oriented"),
           mention(14, first=None, style=[]),
           geo("flowchart-or-schematic"),
           path=S_422, kind="solution",
           note="the decision flowchart of the geographic solution: initial office number -> "
                "'More than 1 office on a continent?' -> No into the objective function or "
                "Yes into the P Center split -> determine the languages. The caption stops at "
                "'solution oriented' because the printed line is truncated - 'by geographic "
                "condition' never reaches the text layer or the page. Four node boxes are "
                "measured separately and excluded as fragments"),
]

TABLES += [
    table("tnot",
          uncap("above"),
          mention(4, first=None, style=[]),
          grid(5, 2, header=1, numeric=0, txt=2, rule="boxed"),
          path=S_NOTATION, kind="symbols", caption_source="none",
          note="the Notation grid: five symbol rows against their definitions, fully boxed "
               "with a rule between every row and a rule between the two columns, the symbol "
               "column italic and right-aligned. It has no caption and no number - the "
               "heading '3. Notation' is the only thing that names it - and header_rows is "
               "recorded as 1 because the field has no zero state"),
    table("t5b",
          cap("Table 5 Future grouping result", "Table N"),
          mention(13, first=12, style=["Table 5"], count=1, pattern="as-shown-in",
                  lead="the locations as well as spoken languages will change as Table 5 "
                       "and Table 6 show below:"),
          grid(3, 4, header=1, numeric=1, txt=3, rule="boxed", continued=True),
          path=S_421, kind="solution",
          note="the tail of Table 5 carried over the page break: the third line of group 4 "
               "(Republic, Colombia, Portugal), group 5 Japanese (Japan, 1 country) and group 6 "
               "French (France, Belgium, 2). The block prints "
               "with no header row on this page and no rule under it, so the reader has to "
               "match the columns to the page before"),
    table("t6",
          cap("Table 6 Future locations and languages for each office", "Table N"),
          mention(13, first=12, style=["Table 6"], count=1, pattern="as-shown-in",
                  lead="Table 5 and Table 6 show below:"),
          grid(3, 7, header=1, numeric=0, txt=7, rule="boxed"),
          path=S_421, kind="solution",
          note="the 2067 office answer: seven printed rows - one country row, one capital "
               "row under it and one Language row - with the capitals lettered in "
               "parentheses under each name (Riyadh, Warsaw, Dhaka, Tokyo, Paris, Buenos "
               "Aires) and one merged language cell below. Every cell is ruled, and the "
               "only non-ASCII text in the paper's grids is the three-language stack in the "
               "Poland column"),
    table("t7",
          cap("Table 7 Initial distribution of office number", "Table N"),
          mention(14, first=None, style=[]),
          grid(2, 7, header=1, numeric=6, txt=1, rule="boxed"),
          path=S_422, kind="solution",
          note="six continents against the number of offices to be built there (Asia 2, "
               "Europe 2, the rest 1) - the input the whole geographic solution runs on. "
               "Two rows only, boxed cell by cell, continent names bold"),
    table("t8",
          cap("Table 8 Current grouping result (Solution 2)", "Table N"),
          mention(14, first=None, style=[]),
          grid(13, 7, header=1, numeric=1, txt=6, rule="boxed", merged=True),
          path=S_422, kind="solution",
          note="the 2017 grouping: eight continent groups, the group number and continent "
               "merged down each group's member rows, members spilled into a five-column "
               "block with the trailing cells left blank. Fourteen printed rows, and the "
               "blank cells are structural - the grid is a ragged set, not a missing-data "
               "table"),
]
B.update({
    "t3": bb(12, 1),
    "t4": bb(12, 2),
    "t5a": bb(12, 3),
    "f12": bb(15, 1),
    "t9": bb(15, 2),
    "t10": bb(16, 1),
    "f13": bb(16, 2),
    "t11": bb(16, 3),
    "t12": bb(17, 1),
    "t13": bb(18, 1),
    "t14a": bb(18, 2),
    "t14b": bb(19, 1),
    "t15": bb(19, 2),
    "f14": bb(20, 1),
})

TABLES += [
    table("t3",
          cap("Table 3 Current grouping result (solution 1)", "Table N"),
          mention(12, first=12, style=["the following table"], count=1,
                  pattern="figure-n-shows", read=3,
                  lead="we obtain the members of each group as the following table shows:"),
          grid(7, 4, header=1, numeric=1, txt=3, rule="boxed"),
          path=S_421, kind="solution",
          note="the 2017 language-structure grouping in four columns: group number, the "
               "dominant language, the member countries as a comma list, and the count. One "
               "row carries three languages stacked in the cell (group 2 prints Spanish, "
               "French and Russian one above another with plus signs between them), so that "
               "row is nearly eight times the height of the others and the count 38 sits "
               "opposite the middle of the stack"),
    table("t4",
          cap("Table 4 Current locations and languages for each office", "Table N"),
          mention(12, first=12, style=["Table 4"], count=1, pattern="as-shown-in", read=2,
                  lead="Final result of locations and the languages used in each office is "
                       "shown in Table 4."),
          grid(2, 7, header=1, numeric=0, txt=7, rule="boxed"),
          path=S_421, kind="solution",
          note="the same six offices read off the map: one header row whose cells carry the "
               "country with its capital struck underneath in parentheses, and one Language "
               "row under it. Germany's cell stacks two languages in two lines and is the "
               "only cell that wraps"),
    table("t5a",
          cap("Table 5 Future grouping result", "Table N"),
          mention(12, first=12, style=["Table 5"], count=1, pattern="as-shown-in", read=2,
                  lead="the grouping result and the locations as well as spoken languages will "
                       "change as Table 5 and Table 6 show below:"),
          grid(5, 4, header=1, numeric=1, txt=3, rule="boxed"),
          path=S_421, kind="solution",
          note="Table 3 repeated on the 2067 data: same four columns, six groups, and the "
               "membership churns - group 2 absorbs twenty-nine countries under Hindustani, "
               "Malay and German stacked in one cell. Group 4 is cut by the page break; its "
               "tail is recorded as the continuation t5b"),
    table("t9",
          cap("Table 9 Languages spoken in each office in 2017", "Table N"),
          mention(15, first=15, style=["the table below"], count=1, pattern="direct",
                  read=2,
                  lead="The languages spoken in each country are shown in the table below:"),
          grid(2, 9, header=1, numeric=0, txt=9, rule="boxed"),
          path=S_422, kind="solution",
          note="eight offices across in one header row whose cells pair the country with its "
               "capital in parentheses underneath, and one Language row beneath it. India and "
               "America carry two-line capital names ((New Delhi), (New York)), so the header "
               "band is deeper than the data band"),
    table("t10",
          cap("Table 10 Future grouping result (solution 2)", "Table N"),
          mention(16, first=None, style=[]),
          grid(14, 7, header=1, numeric=0, txt=7, rule="boxed", merged=True),
          path=S_422, kind="solution",
          note="the 2067 geographic grouping: eight groups, the group number merged down each "
               "group and the continent merged beside it, members spilled five to a line. "
               "Fourteen printed rows; group 5 is the only one whose fifth member "
               "(Dominican Republic) needs a second line"),
    table("t11",
          cap("Table 11 Languages spoken in each office in 2067", "Table N"),
          mention(16, first=None, style=[]),
          grid(2, 9, header=1, numeric=0, txt=9, rule="vertical-rules"),
          path=S_422, kind="solution",
          note="Table 9 one simulation run later: Italy and India drop out and Poland and "
               "Russia take their columns; Germany's cell stacks German, French and Spanish "
               "in three lines. The one grid in the paper ruled vertically only - eight "
               "internal vertical rules against two horizontals, no right border and no "
               "bottom rule, so the last cell runs off the open edge of the table"),
    table("t12",
          cap("Table 12 Analytical result of Net Birth Rate impact", "Table N"),
          mention(17, first=17, style=["the following table"], count=1, pattern="direct",
                  read=2,
                  trail="As can be seen from the above table, for most languages, the number "
                        "of language speakers is positively correlated with the Net Birth "
                        "Rate.",
                  lead="The relative changes are shown in the following table."),
          grid(17, 5, header=1, numeric=4, txt=1, rule="boxed", width="half"),
          path=S_511, kind="sensitivity",
          note="the first sensitivity sweep: sixteen languages down, the four birth-rate "
               "variations (-20, -10, +10, +20 per cent) across, every body cell a signed "
               "percentage. The header band is twice the depth of the body rows because "
               "'Change of Net Birth Rate' wraps over two lines above the four level labels, "
               "but it is still one header row; every value is centred, none decimal-aligned"),
    table("t13",
          cap("Table 13 Analytical result of GDP Growth Rate impact", "Table N"),
          mention(18, first=18, style=["following table"], count=1, pattern="direct",
                  read=2,
                  trail="As can be seen from the above table, the increase in GDP growth rate "
                        "will cause an increase in the number of most languages."),
          grid(17, 5, header=1, numeric=4, txt=1, rule="boxed", width="half"),
          path=S_512, kind="sensitivity",
          note="the same sixteen languages against the four GDP-growth variations (-50, -10, "
               "+10, +100 per cent). One header row only, because the variation labels fit "
               "on the header line here; the smallest changes in the paper live in this grid "
               "(-0.13 per cent for Hausa in every column)"),
    table("t14a",
          cap("Table 14 Analytical result of Migration Rate impact", "Table N"),
          mention(18, first=None, style=[]),
          grid(17, 5, header=1, numeric=4, txt=1, rule="boxed", width="half"),
          path=S_513, kind="sensitivity",
          note="the migration sweep, first half: Chinese through French on page 18, the "
               "remaining five languages carried to page 19 as t14b. The measured region sits "
               "a little high, so it also catches the closing line of the paragraph and the "
               "caption before the first five rows; the drawn grid is seventeen rows and the "
               "split falls without a rule under the last row and without a repeated header "
               "on page 19"),
    table("t14b",
          cap("Table 14 Analytical result of Migration Rate impact", "Table N"),
          mention(19, first=None, style=[]),
          grid(5, 5, header=1, numeric=4, txt=1, rule="boxed", continued=True),
          path=S_513, kind="sensitivity",
          note="the last five language rows of Table 14 (Hausa, Punjabi, Japanese, German, "
               "Persian) printed as a bare block at the top of page 19 with no caption and "
               "no header row of its own; header_rows is 1 because the field has no zero "
               "state"),
    table("t15",
          cap("Table 15 Sensitivity Analysis of Location Determination Model", "Table N"),
          mention(19, first=19, style=["the table above"], count=1, pattern="direct",
                  read=4,
                  lead="and record the recommending countries for new offices under each "
                       "circumstance, respectively.",
                  trail="From the table above we can conclude that:"),
          grid(10, 9, header=2, numeric=8, txt=1, rule="boxed", merged=True),
          path=S_515, kind="sensitivity",
          note="the widest grid in the paper: four side-by-side blocks, each a Group members "
               "and a Recommanded Country column under one of the four GDP variations, with "
               "the top-left header cell left empty and 'GDP growth rate variation' printed "
               "across it, each of the four level cells spanning two columns, and the Asia "
               "and Europe stub cells spanning two rows. Eight data rows - one per continent, "
               "with Asia and Europe taking two each - and every member cell a signed count. "
               "The rules are drawn in light grey, so the grid reads as unruled at a glance"),
]
B.update({
    "t1": bb(6, 1),
    "t2": bb(8, 1),
    "memo": bb(23, 2),
    "f15": bb(23, 1),
})

TABLES += [
    table("t1",
          cap("Table 1 Increasing rate of GDP per capita for countries in different "
              "development level", "Table N"),
          mention(6, first=5, style=["Table 1"], count=1, pattern="direct", read=2,
                  lead="GDP per capita increases at different rate for countries in "
                       "different development level, which is listed in Table 1 below."),
          grid(2, 4, header=1, numeric=3, txt=1, rule="boxed", width="half"),
          path=S_411, kind="model",
          note="the smallest grid in the paper and the only one that is not full measure: "
               "a header row naming the three development classes and one data row of "
               "growth rates (+2%, +7%, +3%). The unit stays inside the data cells - the "
               "header carries no per cent sign - and the whole block occupies about 340 pt "
               "of the 468 pt measure, indented from the left margin"),
    table("t2",
          cap("Table 2 First simulation result", "Table N"),
          mention(8, first=None, style=[]),
          grid(17, 7, header=1, numeric=6, txt=1, rule="boxed", units_in_header=True),
          path=S_412, kind="model",
          note="the baseline simulation in one panel: sixteen languages down, and seven "
               "columns across that are really three stacked pairs - rank in 2017, rank in "
               "2067, population in 2017, population in 2067, then the increased rate (in "
               "per cent) and the increased number. The header is one row of double depth: "
               "the pair labels sit on the upper line and the years on the lower, with "
               "Language vertically centred against both. This is the only grid whose header "
               "carries a unit"),
]

FIGURES += [
    figure("f12",
           cap("Figure 12 Location of offices worldwide in 2017"),
           mention(15, first=15, style=["Figure 12"], count=2, pattern="figure-n-shows",
                   read=3,
                   lead="Figure 12 distinctly shows the location of offices and corresponding "
                        "relative members in the same group on the map of the world."),
           geo("map-or-plan-view", legend="none", labels=True),
           path=S_422, kind="solution",
           note="a world map in an oval frame with the landmass left raster and the offices "
                "drawn on top: one filled bubble at each of the eight office countries, a "
                "small dot for every other grouped country, and the eight country names "
                "lettered on the map. There is no legend box and no colourbar - the bubbles "
                "vary only 9.6 to 13.9 pt across, so size encodes little, and the grouping "
                "is read from the printed names, not from a key"),
    figure("f13",
           cap("Figure 13 Location of offices worldwide in 2067"),
           mention(16, first=None, style=[]),
           geo("map-or-plan-view", legend="none", labels=True),
           path=S_422, kind="solution",
           note="Figure 12 one run later: same oval map, same eight-bubble encoding, but "
                "Italy and India are gone and Poland and Russia take their place - and "
                "'Poland' is printed on a grey highlight band, which is the drawing tool's "
                "label backing rather than a legend. Bubble diameters 10.1 to 13.0 pt, the "
                "same weak size encoding as the 2017 map"),
    figure("f14",
           cap("Figure 14 Changes in the location of Europe continent"),
           mention(20, first=20, style=["the following figure"], count=1, pattern="direct",
                   read=2,
                   lead="Calculating this situation on Matlab program, we get the result"),
           geo("flowchart-or-schematic", panels=4, layout="2x2", labels=True),
           path=S_6, kind="other",
           note="a box-and-arrow schematic laid inside a ruled 2x2 matrix rather than on a "
                "map: columns headed Short-term (2017) and Long-term (2067), rows labelled "
                "Europe and Other Continents in orange, rounded boxes joined by block "
                "arrows, each box naming the office countries it holds. The top-left cell is "
                "left blank, so only three of the four cells carry artwork, and the whole "
                "frame is one bitmap with the matrix rules drawn inside it"),
    figure("f15",
           uncap("below"),
           mention(23, first=None, style=[]),
           geo("map-or-plan-view", legend="none", labels=True),
           path=S_MEMO, kind="other", caption_source="none",
           note="the memo page's world map, and the only exhibit in the paper with no caption "
                "and no number anywhere on its page: eight large origin bubbles coloured one "
                "colour per office country and lettered in that colour, small dots for the "
                "destination countries, and arrows from each origin to its destinations. "
                "Colour is a categorical key mapped one-to-one onto the printed names, so "
                "there is no legend box and no colourbar; the faint black basemap labels are "
                "not legible at this resolution and are not recorded"),
]

TABLES += [
    table("memo",
          uncap("above"),
          mention(23, first=None, style=[]),
          grid(9, 2, header=1, numeric=0, txt=2, rule="booktabs"),
          path=S_MEMO, kind="other", caption_source="none",
          note="the memo's answer grid: eight recommended offices against the language to be "
               "spoken in each, delivered as a single booktabs block - three rules only (a "
               "1.4 pt rule above and below, a hairline under the header) and not one "
               "vertical rule, in contrast to every other grid in the paper. No table "
               "number and no caption; the two column heads are the only labels it has"),
]
"""Rule layer for #150: the distilled regularities of this paper's exhibits.

Every rule ends on the payload field it was aggregated from, and the counts in the
rules are counts of this payload, not impressions.
"""

RULES: list[str] = [
    "Caption side is decided by exhibit kind, not by available space: all 18 recorded "
    "figures carry their caption under the artwork and all 17 captioned grids carry it "
    "over the box, on every page of the paper, with no exception. The two uncaptioned "
    "exhibits - the notation grid and the memo's answer grid - sit under a heading that "
    "names them instead [caption.position].",

    "Numbering is positional only: Figure N and Table N with a plain space, never a colon "
    "and never a full stop, across all 35 captions; figure and table numbers run "
    "independently and neither restarts, so the caption alone places an exhibit in the "
    "argument [caption.numbering].",

    "Captions are noun phrases: not one of the 35 carries a finite verb, so voice is none "
    "throughout, and none states a unit, a condition, a parameter value or a conclusion. "
    "Figure captions run 5 to 16 words, grid captions 5 to 14, and the longest are the "
    "ones that have to say what is being compared - total number and rank, number of "
    "native speakers and rank [caption.voice].",

    "Family follows the argument stage. The six model-kind exhibits are three box-and-"
    "arrow drawings, one rank-ordered point cloud, one axis-only interval strip and two "
    "grids; the twenty-two solution-kind exhibits are six 16-curve line plates, three "
    "maps, two more flowcharts, one node-link distance example, a second interval strip "
    "and eight grids; the five sensitivity exhibits are grids and nothing else; the memo "
    "closes on one map and one grid. No bar, histogram, heatmap, 3D view or colourbar "
    "appears anywhere in the paper [place.section_kind].",

    "The recurring figure template is the sixteen-curve line plate: years on the x axis, "
    "0 to N on the y axis in scientific notation without a unit, sixteen series keyed in "
    "a box inside the upper right corner, and a twin frame beside it turning the same run "
    "into rank 0-16 read top-down. Figures 6, 8 and 9 print that pair six times across "
    "three spreads, and the frames are measured as six regions because the ordinate "
    "scales differ [geometry.legend].",

    "A panel plate carries one caption, printed once under the pair, and the second frame "
    "inherits it verbatim. The only plate whose key moves outside the artwork is the "
    "four-frame map row, where the sixteen-entry key sits in the right margin and each "
    "frame stamps its year in red underneath [geometry.panel_count].",

    "Maps encode by bubble size plus the country name printed on the map, never by a "
    "legend box or a colourbar: the three office maps put one bubble on each office "
    "country, a dot on every grouped country and letter the office countries in place, so "
    "size carries almost nothing (bubble diameters vary only about 1.4 to 1) and the "
    "reader is meant to read names, not areas [geometry.colorbar].",

    "Grid ruling is heavy by default: 17 of the 19 grids box every cell, and the tall ones "
    "draw eighteen horizontals at a 16.8 pt pitch plus every internal vertical. The memo's "
    "answer grid is the only booktabs block - three rules, no verticals - and Table 11 is "
    "the only half-drawn one: verticals only, open on the right and at the bottom. No grid "
    "uses zebra striping and no grid uses a diagonal header [table.rule_style].",

    "Merged cells appear only where a label owns several body rows: the group number and "
    "the continent merge down the member rows of the two geographic grouping grids, the "
    "four GDP-level header cells each span two columns in the sensitivity summary, and the "
    "Asia and Europe stubs span two rows there. The two language-structure grouping grids "
    "merge nothing - their tall rows are single cells holding a stack of three languages "
    "[table.merged_cells].",

    "Grid width tracks the column count, not the importance: the two-column memo grid and "
    "the four-column location grid run at 89 to 99 per cent of the text measure, the "
    "seven-column simulation grid at 94 per cent, the nine-column office strips at or past "
    "the measure, while the three grids holding one number per cell shrink to 62 to 73 per "
    "cent. Nothing in the paper is set landscape or rotated [table.width].",

    "Units are almost never in the header: Table 2 prints Increased rate (%) over its "
    "column and is the only grid that does. Everywhere else - the GDP growth rates of "
    "Table 1, the three sensitivity sweeps - the per cent sign is repeated inside every "
    "cell, so the header row stays pure label [table.units_in_header].",

    "Numbers are centred, never decimal-aligned and never right-aligned: the signed "
    "percentages of the three sensitivity grids and the counts of the grouping grids all "
    "sit on the cell centre, so digits do not line up in a column even where every entry "
    "is a decimal [table.decimal_aligned].",

    "Header depth is one row in every grid, but the band is stretched wherever labels "
    "stack: the simulation grid doubles it to fit a pair label over its year, the "
    "birth-rate grid doubles it to fit Change of Net Birth Rate over the four levels, and "
    "the sensitivity summary needs two rows for its stacked corner. Below that band the "
    "pitch is uniform, which is what makes the eight-row body of Table 15 readable despite "
    "its rules being drawn in light grey [table.header_rows].",

    "Two grids break across a page and neither repeats its header: the tail of the "
    "language-structure grouping arrives at the top of page 13 as three bare rows, and five "
    "language rows of the migration sweep arrive at the top of page 19 with the caption "
    "still on the page before. A continuation is therefore recognisable only by its column "
    "count and by the missing rule under its last row [table.continued].",

    "Announcement is optional and mostly numberless: 14 of the 35 captioned exhibits get a "
    "lead-in sentence, 11 of those on the exhibit's own page, and only 8 of the 14 print "
    "the exhibit's number in the sentence. The other six say the following table, the table "
    "below, the following figure, or nothing at all, so the caption has to do the pointing "
    "[mention.lead_sentence].",

    "Interpretation after the exhibit belongs to the sensitivity section: all three sweeps "
    "are followed by a paragraph that opens on the grid itself, whereas the solution grids "
    "are followed by the next step of the argument rather than by a reading of the grid "
    "[mention.trail_sentence].",

    "Exhibits cluster away from the page top: only 14 of the 37 sit in the top third of "
    "their page, 10 in the middle and 13 in the bottom third, and no exhibit occupies a "
    "page alone - every one shares its page with text or with a second exhibit, which is "
    "why the papers' figures are read as inline evidence rather than as plates "
    "[place.page_zone].",
]

NOTE = (
    "P-B-2018-77238-4380ec81 (2018 MCM B, Team 77238): 23 pages, 50 measured regions, "
    "18 figures and 19 grids recorded, 13 fragments excluded, no unaccounted region. The "
    "paper is a two-model chain - a language-development simulation and an office-siting "
    "model - and its exhibit language splits along that seam: the model half argues with "
    "schematics and two small grids, the solution half carries every dense exhibit (six "
    "16-curve plates, three maps, four grouping grids), the sensitivity half is grids "
    "only, and the memo page ends on an uncaptioned map and a booktabs answer grid. Three "
    "structural traps worth carrying to the queue: the heading detector mistakes table "
    "rows for headings, so the section paths here come from the numbered headings only; "
    "the paper prints fifteen numbered tables but seven of them are native text that the "
    "region pass never boxes, so this record covers the twelve grids the detector measured "
    "plus the notation and memo blocks; and both page-break continuations arrive without "
    "their header, which is why they are recorded as separate exhibits with continued set."
)
ALL: list[dict] = FIGURES + TABLES

# Reading order: page, then top-to-bottom within the page, left-to-right on a shared row.
_order = sorted(ALL, key=lambda it: (it["page"],
                                     round((it["bbox"][1] + it["bbox"][3]) / 2),
                                     it["bbox"][0]))
_page_seen: dict[int, int] = {}
for _i, _it in enumerate(_order, 1):
    _it["place"]["doc_order"] = _i
    _pg = _it["page"]
    _page_seen[_pg] = _page_seen.get(_pg, 0) + 1
    _it["place"]["page_order"] = _page_seen[_pg]

_claimed = {(it["page"], tuple(it["bbox"])) for it in ALL}
_claimed |= {(p, tuple(b)) for _k, (p, b), _r in EXCLUDED}
assert _claimed == MEASURED, (
    f"claimed {len(_claimed)} of {len(MEASURED)} measured regions; "
    f"unclaimed {sorted(MEASURED - _claimed)[:5]} "
    f"phantom {sorted(_claimed - MEASURED)[:5]}")
assert len(ALL) + len(EXCLUDED) == len(MEASURED) == 50


def t_ok(t: dict) -> bool:
    return bool(t["caption"]["words"])


PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"page": _p, "bbox": _b, "reason": _r, "note": _k}
        for _k, (_p, _b), _r in EXCLUDED
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
    rule: dict[str, int] = {}
    for it in TABLES:
        rule[it["table"]["rule_style"]] = rule.get(it["table"]["rule_style"], 0) + 1
    pos: dict[str, int] = {}
    for it in ALL:
        pos[(("fig" if "family" in it else "grid"), it["caption"]["position"])] = \
            pos.get((("fig" if "family" in it else "grid"), it["caption"]["position"]), 0) + 1
    lead: dict = {}
    for it in ALL:
        lead[it["mention"]["lead_pages"]] = lead.get(it["mention"]["lead_pages"], 0) + 1
    words = [it["caption"]["words"] for it in FIGURES if it["caption"]["words"]]
    twords = [it["caption"]["words"] for it in TABLES if t_ok(it)]
    print(f"{PID}: figures={len(FIGURES)} tables={len(TABLES)} excluded={len(EXCLUDED)} "
          f"regions={len(MEASURED)}")
    print("fam", dict(sorted(fam.items())))
    print("legend", dict(sorted(leg.items())))
    print("pos", dict(sorted(pos.items(), key=lambda kv: str(kv[0]))))
    print("rule", dict(sorted(rule.items())))
    print("zone", dict(sorted(zone.items())))
    print("kind", dict(sorted(kind.items())))
    print("lead", dict(sorted(lead.items(), key=lambda kv: str(kv[0]))))
    print("figwords", min(words), max(words))
    print("tabwords", min(twords), max(twords))
    print("payload", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
