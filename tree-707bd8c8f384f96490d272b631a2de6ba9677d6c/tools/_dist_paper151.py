"""Hand pass for P-B-2018-79002-238b850f (2018 MCM B, "Team 79002", how many
languages: a difference-equation speaker model plus a six-office siting model).

29 pages, 43 measured regions on 21 of them. The paper prints nineteen numbered
exhibits (Figures 1-16 with 3 and 14 missing, Tables 2-17 with 1, 7 and 9 missing),
twelve appendix images and seven display-equation images that the region pass boxes
like artwork.

Usage: python -I tools/_dist_paper151.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2018-79002-238b850f"
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

S_22 = ["2 Assumptions and Symbols", "2.2 Symbols and definitions"]
S_3 = ["3 Part I Models and Results"]
S_31 = S_3 + ["3.1 Model I: Various Languages Speakers Difference Equation Model"]
S_311 = S_31 + ["3.1.1 The increase of the native speakers"]
S_3121 = S_31 + ["3.1.2 The increase of the second language speakers",
                 "3.1.2.1 Effect of the language own features"]
S_3122 = S_31 + ["3.1.2 The increase of the second language speakers",
                 "3.1.2.2 Effect of the global situation"]
S_313 = S_31 + ["3.1.3 The total difference equation of model I"]
S_32 = S_3 + ["3.2 Model I Results & Analysis"]
S_321 = S_32 + ["3.2.1 Initial rank and parameter setting"]
S_322 = S_32 + ["3.2.2 Results & Analysis"]
S_33 = S_3 + ["3.3 Model II: Geographical Distribution Difference Model"]
S_34 = S_3 + ["3.4 Population growth fitting and current migration pattern"]
S_36 = S_3 + ["3.6 Result and Analysis"]
S_4 = ["4 Part II Models & Results"]
S_42 = S_4 + ["4.2 Explanation about our choices"]
S_5 = ["5 Sensitivity Analysis"]
S_6 = ["6 Strength and Weakness"]
S_MEMO = ["7 Memo"]
S_APP = ["8 Appendix"]
# Pages 4-11: the two symbol tables, Figure 1/2, the pie pair, Figure 5's two boxes
# and the four tables of Model I including both headerless continuations.

B["t1"] = bb(4, 1)
TABLES.append(table(
    "t1", cap("Table 1 Symbols and definitions"),
    mention(4, first=None, style=[],
            lead="", pattern="none",
            trail="", read=0),
    grid(11, 2, header=1, numeric=0, txt=2, rule="vertical-rules"),
    path=S_22, kind="symbols", caption_source="typed-from-crop",
    note="Eleven printed rows: one header over ten symbol rows. Three horizontals "
         "(thick-thin-thick) plus one vertical rule between the symbol and definition "
         "columns; symbol cells centred, definitions left. No zebra, no merges, no unit."))

B["t2"] = bb(4, 2)
TABLES.append(table(
    "t2", cap("Table 2 codes for top 16 languages"),
    mention(4, first=None, style=[],
            lead="", pattern="none",
            trail="", read=0),
    grid(4, 9, header=1, numeric=1, txt=8, rule="vertical-rules", width="full"),
    path=S_22, kind="symbols",
    note="Nine columns (index stub plus eight), four printed rows only: the code row i = "
         "1-8, its language row, then i = 9-16 and its language row, so the sixteen codes "
         "are laid out as two stacked bands under one header rather than sixteen rows."))

B["t3"] = bb(5, 1)
TABLES.append(table(
    "t3", cap("Table 3     types of languages"),
    mention(5, first=None, style=[],
            lead="", pattern="none",
            trail="we divide all 16 languages into 2 types", read=1),
    grid(3, 2, header=1, numeric=0, txt=2, rule="vertical-rules"),
    path=S_311, kind="model",
    note="Two text columns, two body rows whose cells wrap onto several lines each; the "
         "language lists inside a cell are the only multi-line content in the table."))

EXCLUDED.append(("p6-r1", bb(6, 1), "not-an-exhibit"))
EXCLUDED.append(("p6-r2", bb(6, 2), "not-an-exhibit"))

B["f1"] = bb(7, 1)
FIGURES.append(figure(
    "f1", cap("Figure 1 The foreign language studied in school, taking U.S. for example[6]"),
    mention(7, first=None, style=[],
            lead="We assume that the language promoted by the government is the foreign "
                 "language taught in school.",
            pattern="none",
            trail="k1 is the coefficient to measure how much this factor (the language "
                  "taught in school) will influence the increase of 2nd language speakers",
            read=2),
    geo("other", legend="outside-right", numbers=False),
    path=S_3121, kind="model",
    other_note="pasted screenshot of a pie chart (Excel-style grey hatched frame, "
               "sans-serif labels, title printed inside the image)",
    note="Pie with a nine-entry key parked outside the plot on the right, inside the "
         "screenshot's own grey frame. Slice sizes are not printed; only the internal "
         "title names the subject."))

B["f2"] = bb(7, 2)
FIGURES.append(figure(
    "f2", cap("Figure 2 The neighborhood effect among the top 16 languages"),
    mention(7, first=None, style=[],
            lead="If the speakers of two language live near to each other, it is more likely "
                 "for them to have cultural communication.",
            pattern="none",
            trail="the two language having a line linked means there will be Neighborhood "
                  "effect between them", read=1),
    geo("node-link-network", legend="none", numbers=False),
    path=S_3121, kind="model",
    note="Sixteen labelled boxes, one per language, joined by directed arrows; monochrome, "
         "no grid, no legend, no weights. The caption's second line is the reading key, so "
         "the exhibit explains its own encoding in the caption rather than a legend."))

B["f4"] = bb(8, 1)
FIGURES.append(figure(
    "f4", cap("Figure 4 GDP contributed by language [7]"),
    mention(8, first=None, style=[],
            lead="Through the GDP contributed by different languages [See Figure 3], we "
                 "give different weight to the top 16 language.",
            pattern="parenthetical",
            trail="k3 describes how much the economic factor motivates people to learn "
                  "language i as their 2nd language.", read=1),
    geo("other", legend="outside-right", labels=True),
    path=S_3122, kind="model",
    other_note="pasted screenshot of a donut chart",
    note="Donut rather than a full pie, percentages printed on the sectors with leader "
         "lines, key outside on the right. The lead-in sentence points at 'Figure 3', a "
         "number this paper never prints, so the citation and the caption disagree."))

B["f5l"] = bb(9, 2)
FIGURES.append(figure(
    "f5l", cap("Figure 5 languages in the internet (left) [9] & the pressure of mainstream "
               "website(right)[8]"),
    mention(9, first=None, style=[],
            lead="Though there are thousands of languages all over the world, only 5% of "
                 "them are used widely in the internet.",
            pattern="none",
            trail="54.5% of all web content is still in English despite huge growth in "
                  "users that do not understand English", read=2),
    geo("other", legend="outside-right", labels=True),
    path=S_3122, kind="model",
    other_note="pasted screenshot of a pie chart, one wedge per language share of web "
               "content",
    note="Left panel of a figure the paper prints as two separate boxes with one caption "
         "line running under both: ten wedges with leader-line percentages and an "
         "outside-right key."))

B["f5r"] = bb(9, 1)
FIGURES.append(figure(
    "f5r", cap("Figure 5 languages in the internet (left) [9] & the pressure of mainstream "
               "website(right)[8]"),
    mention(9, first=None, style=[],
            lead="Data also show us that the number of languages used by mainstream social "
                 "medias, such as Facebook, Twitter and LinkedIn is limited to few languages.",
            pattern="none",
            trail="We can express the power of language in the network as follows:",
            read=1),
    geo("bar", legend="none", labels=True),
    path=S_3122, kind="model",
    note="Right panel of the same two-box figure: a paired bar chart comparing a 2012 and "
         "a 2015 count for eight platforms, every value printed as a number beside its bar "
         "(17/24, 21/48, 63/91 and so on) instead of an axis. Same screenshot styling as "
         "its left-hand partner."))

EXCLUDED.append(("p9-r3", bb(9, 3), "not-an-exhibit"))

B["t4"] = bb(9, 4)
TABLES.append(table(
    "t4", cap("Table 4 The initial rank by language size [1]"),
    mention(9, first=None, style=[],
            lead="We get the initial rank by total language speaker", pattern="none",
            trail="And here is the initial data:", read=1),
    grid(3, 7, header=1, numeric=6, txt=1, rule="vertical-rules"),
    path=S_321, kind="result",
    note="Only rows 1-2 of sixteen print on this page; the remaining fourteen arrive on the "
         "next page as a headerless continuation, so the reader has to carry the column "
         "meaning across the page break."))

B["t4c"] = bb(10, 1)
TABLES.append(table(
    "t4c", uncap("above"),
    mention(10, first=None, style=[], lead="", pattern="none", trail="", read=0),
    grid(14, 7, header=1, numeric=6, txt=1, rule="booktabs", continued=True),
    path=S_321, kind="result", caption_source="none",
    note="Rows 3-16 of Table 4, printed with neither header nor caption and with the "
         "vertical rule dropped: the continuation is not a copy of the first half. The "
         "Punjabi row is the one place the paper prints '?' instead of a number."))

B["t5"] = bb(10, 2)
TABLES.append(table(
    "t5", cap("Table 5 Indices setting"),
    mention(10, first=None, style=[],
            lead="According to the data we collected in [1, 4-7, 9], we can set indices in "
                 "the formula (4) and formula (5).",
            pattern="none",
            trail="These parameters in our various languages speakers difference equation "
                  "model are given by our estimate.", read=2),
    grid(3, 6, header=1, numeric=4, txt=2, rule="vertical-rules"),
    path=S_321, kind="result",
    note="Three printed rows: an index row, a value row whose first two cells are stacked "
         "fractions (1/300, 1/90000) and a worded explanation row. The fractions are the "
         "only cells in the paper whose height is set by typography instead of text."))

B["t6"] = bb(10, 3)
TABLES.append(table(
    "t6", cap("Table 6 The predicted rank by language size after 50 years, Unit: million"),
    mention(10, first=None, style=[],
            lead="After inputting the initial value and indices in MATLAB, we got the new "
                 "rank:", pattern="none",
            trail="", read=0),
    grid(11, 7, header=1, numeric=6, txt=1, rule="vertical-rules"),
    path=S_322, kind="result",
    note="Rows 1-10 here, rows 11-16 headerless on the next page. The unit lives in the "
         "caption ('Unit: million'), not in any column head, and the numbers are printed to "
         "four to five decimals while the caption's unit is a round million."))

B["t6c"] = bb(11, 1)
TABLES.append(table(
    "t6c", uncap("above"),
    mention(11, first=None, style=[], lead="", pattern="none",
            trail="The top ten of total speakers vary from Mandarin", read=0),
    grid(6, 7, header=1, numeric=6, txt=1, rule="vertical-rules", continued=True),
    path=S_322, kind="result", caption_source="none",
    note="Rows 11-16 of Table 6 with the header and caption left behind on the previous "
         "page. The prose that follows immediately cites 'Table 7' for these rows, another "
         "number the paper never prints."))
# Pages 12-17: Model II exhibits, the migration-route table and Part II siting maps.

B["f6"] = bb(12, 1)
FIGURES.append(figure(
    "f6", cap("Figure 6 Language distribution in 2017"),
    mention(12, first=None, style=[], lead="Below is the language distribution in 2017:",
            pattern="as-shown-in",
            trail="Therefore, we divide Earth language data into six continents, and each "
                  "different continent has a different language distribution.", read=1),
    geo("map-or-plan-view", legend="inside", numbers=False),
    path=S_33, kind="model",
    note="World choropleth: continental polygons coloured by dominant language, grey for "
         "unfilled regions. Ten-swatch white key sits inside the bottom-left corner; no "
         "colourbar, no 3-D, no country names, no printed numbers. Pasted raster."))

B["f7"] = bb(12, 2)
FIGURES.append(figure(
    "f7", cap("Figure 7 The regression on the world demographic data"),
    mention(12, first=None, style=[],
            lead="Below is our fitting effect and function expression.",
            pattern="as-shown-in",
            trail="N(t) denotes the world population in t years.", read=1),
    geo("scatter", legend="none"),
    path=S_34, kind="model",
    note="Open-circle scatter of World Bank 1960-2016 population with the fitted Gaussian "
         "curve over it; MATLAB grey axes box, x ticked 1950-2080 every 20, y 2-11 with "
         "'x10^10' printed at the axis head. No legend, no data labels, 2-D."))

B["f8"] = bb(13, 1)
FIGURES.append(figure(
    "f8", cap("Figure 8 Some main routes of global migration[11]"),
    mention(13, first=None, style=[],
            lead="Then we look for the main migration patterns, and the image below shows "
                 "some of the routes we found.",
            pattern="as-shown-in",
            trail="Based on the current global migration patterns, we propose to assume the "
                  "following seven major migration routes.", read=1),
    geo("map-or-plan-view", legend="inside", numbers=False),
    path=S_34, kind="model",
    note="World map with migration flow arrows, pasted raster that carries its own source "
         "credit printed inside the artwork. Legend box inside the top-right names the "
         "subject; a separate red caption sits top-left. No colourbar, no 3-D, no numeric "
         "labels. Only place in the paper where a figure credits a source inside the image."))

B["t8"] = bb(13, 2)
TABLES.append(table(
    "t8", cap("Table 8      7 main migration routes"),
    mention(13, first=None, style=[],
            lead="These seven migration routes are the most promising migration path we "
                 "believe will be in the next 50 years.",
            pattern="none",
            trail="we make the following assumptions as to the proportion of these seven "
                  "routes in all the routes", read=1),
    grid(8, 3, header=1, numeric=1, txt=2, rule="vertical-rules", width="full"),
    path=S_34, kind="model",
    note="Header row plus seven route rows. Three horizontal rules (thick-thin-thick) and "
         "one vertical rule between the detail and proportion columns only: the vertical "
         "line stops at the outer horizontals, so this is a booktabs body with a single "
         "column divider rather than a boxed grid. Header italic; column 1 left, column 2 "
         "centred, column 3 right; no merges, no zebra."))

EXCLUDED.append(("p13-r3", B.get("x13r3") or bb(13, 3), "not-an-exhibit"))
EXCLUDED.append(("p14-r1", B.get("x14r1") or bb(14, 1), "not-an-exhibit"))

B["f9"] = bb(14, 2)
FIGURES.append(figure(
    "f9", cap("Figure 9 The distribution of languages in 6 main continents in 2017."),
    mention(14, first=None, style=[],
            lead="Thus, we have the following difference equation:",
            pattern="none",
            trail="The distribution of languages in Africa, Australia, Asia and Latin "
                  "America did not change much.", read=2),
    geo("composite-panel", legend="none", panels=6, layout="6 pies on a world map",
        labels=True),
    path=S_36, kind="result",
    note="Six pie charts pasted onto a decolourised world map, one pie per continent placed "
         "at that continent's position, so the arrangement is geographic and not a grid. "
         "No legend frame: language names and percentages are printed on the artwork with "
         "leader lines. 2-D, no colourbar."))

B["f10"] = bb(15, 1)
FIGURES.append(figure(
    "f10", cap("Figure 10 The distribution of languages in 6 main continents in 2037"),
    mention(15, first=None, style=[],
            lead="In order to easily differentiate data changes on all continents, we "
                 "specialized in converting data of different continents to pie charts.",
            pattern="none", trail="", read=0),
    geo("composite-panel", legend="none", panels=6, layout="6 pies on a world map",
        labels=True),
    path=S_36, kind="result",
    note="Same six-pie composite as Figure 9, re-rendered for 2037; identical legend, "
         "labels and layout, so the pair reads as a time series of one graphic."))

B["f11"] = bb(15, 2)
FIGURES.append(figure(
    "f11", cap("Figure 11 The distribution of languages in 6 main continents in2067"),
    mention(15, first=None, style=[],
            lead="According to the above changes show, we could find:",
            pattern="none",
            trail="The proportion of Mandarin and Spanish in the United States and Canada is "
                  "on the rise.", read=2),
    geo("composite-panel", legend="none", panels=6, layout="6 pies on a world map",
        labels=True),
    path=S_36, kind="result",
    note="Third of the pie-composite triple; the caption itself is misprinted with the "
         "'in 2067' run together, which is how it is quoted here."))

B["f12"] = bb(16, 1)
FIGURES.append(figure(
    "f12", cap("Figure 12 population density map and locations of 6 offices based on data "
               "in 2017"),
    mention(16, first=None, style=[],
            lead="The population density map and the locations of offices are shownbelow:",
            pattern="as-shown-in",
            trail="The top-six used languages are Mandarin, English, Hindustani, Spanish, "
                  "Arabic and Malay.", read=2),
    geo("map-or-plan-view", legend="inside", numbers=False),
    path=S_42, kind="solution",
    note="Population-density choropleth with six office pins. Discrete class legend inside "
         "the left edge, eight classes with the unit spelled on it (0-12 up to 801+ "
         "people/km2) rather than a continuous colourbar. No per-country labels."))

B["f13"] = bb(17, 1)
FIGURES.append(figure(
    "f13", cap("Figure 13 population density map and locations of 6 offices based on data "
               "in 2067"),
    mention(17, first=None, style=[],
            lead="However, when we consider the site selection in the long term, we refer "
                 "to the results of our model I.",
            pattern="none",
            trail="Singapore is replaced by Rio de Janeiro since the rapid growth of "
                  "Portuguese speakers.", read=2),
    geo("map-or-plan-view", legend="inside", numbers=False),
    path=S_42, kind="solution",
    note="Identical base map and legend to Figure 12; the only change is the pin set, "
         "Singapore swapped for Rio de Janeiro. The body text that introduces it cites "
         "'Figure 14', a number the paper never prints, so the exhibit carries a dangling "
         "cross-reference instead of its own number."))

B["t10"] = bb(17, 2)
TABLES.append(table(
    "t10", cap("Table 10 The most suitable cities"),
    mention(17, first=None, style=[],
            lead="We have calculated the most suitable cities in 4.1.",
            pattern="none", trail="", read=1),
    grid(2, 7, header=1, numeric=1, txt=6, rule="vertical-rules", width="full",
         note="1. Shanghai and New York is the two office we already have."),
    path=S_42, kind="solution",
    note="Two printed rows: a numbered rank row and a city row, with italic stub cells. "
         "Same three horizontals plus one vertical rule as Table 8. The introducing "
         "sentence calls it 'Table 9', another number that is never printed, and the two "
         "note lines sit below the last rule outside the grid."))
# Pages 18-25: sensitivity tables, the two sensitivity figures, and the six pasted
# spreadsheet screenshots in the appendix.

EXCLUDED.append(("p18-r1", bb(18, 1), "not-an-exhibit"))

B["t11"] = bb(18, 2)
TABLES.append(table(
    "t11", cap("Table 11 How many offices should the company set up?"),
    mention(18, first=None, style=[],
            lead="Given different value of C/α, we can give the following suggestions:",
            pattern="none",
            trail="Therefore, given the additional information of α and C, we can help the "
                  "company to decide how many offices they should build.", read=2),
    grid(6, 3, header=1, numeric=2, txt=1, rule="vertical-rules", units_in_header=True),
    path=S_42, kind="solution",
    note="Header plus five bracket-interval rows, the last of which wraps its city list onto "
         "a second line. The unit is printed inside the header cell ('C-p ratio (unit: "
         "million)') and never repeated; the column-1 intervals are right-aligned so the "
         "brackets line up. Measured 487 pt against a 468 pt measure, so the grid overhangs "
         "the text block."))

B["t12"] = bb(18, 3)
TABLES.append(table(
    "t12", cap("Table 12 Sensitivity analysis on natural increase rate"),
    mention(18, first=None, style=[],
            lead="We enter different natural growth rates of Mandarin into the program, and "
                 "we get different Mandarin L2 speakers number.",
            pattern="none", trail="Here is the result:", read=1),
    grid(3, 4, header=1, numeric=3, txt=1, rule="vertical-rules"),
    path=S_5, kind="sensitivity",
    note="Three label rows and no separate header band: the parameter-value row doubles as "
         "the header, which is why the table reads top-down as setting, response, index. "
         "Right-aligned numbers share a right edge but are not decimal-aligned. 360 pt of "
         "468."))

B["t13"] = bb(19, 1)
TABLES.append(table(
    "t13", cap("Table 13 Sensitivity analysis on k1"),
    mention(19, first=None, style=[],
            lead="k1 is the proportional coefficient of the second language growth rate and "
                 "school learning rate.",
            pattern="none", trail="Here is the result:", read=1),
    grid(3, 4, header=1, numeric=3, txt=1, rule="vertical-rules"),
    path=S_5, kind="sensitivity",
    note="First of four tables built from one template: italic parameter label in column 1, "
         "three perturbed values, the response row, then a single pooled sensitivity index "
         "printed only under the baseline column."))

B["t14"] = bb(19, 2)
TABLES.append(table(
    "t14", cap("Table 14 Sensitivity analysis on k2"),
    mention(19, first=None, style=[],
            lead="k2 is the proportional coefficient of the second language growth rate and "
                 "cultural communication.",
            pattern="none", trail="Here is the result:", read=1),
    grid(3, 4, header=1, numeric=3, txt=1, rule="vertical-rules"),
    path=S_5, kind="sensitivity",
    note="Same template as Table 13, values in the 1e-5 range; the index again sits in the "
         "middle column alone so nothing marks which interval it was computed over."))

B["t15"] = bb(19, 3)
TABLES.append(table(
    "t15", cap("Table 15 Sensitivity analysis on k3"),
    mention(19, first=None, style=[],
            lead="k3 is the proportional coefficient of the second language growth rate and "
                 "economics.",
            pattern="none", trail="Here is the result:", read=1),
    grid(3, 4, header=1, numeric=3, txt=1, rule="vertical-rules"),
    path=S_5, kind="sensitivity",
    note="Third copy of the template; the mid rule between the value row and the response "
         "row is the only thing separating the setting from the result."))

B["t16"] = bb(19, 4)
TABLES.append(table(
    "t16", cap("Table 16 Sensitivity analysis on k4"),
    mention(19, first=None, style=[],
            lead="k4 is the proportional coefficient of the second language growth rate and "
                 "technology.",
            pattern="none", trail="Here is the result:", read=1),
    grid(3, 4, header=1, numeric=3, txt=1, rule="vertical-rules"),
    path=S_5, kind="sensitivity",
    note="Fourth copy; four of these tables are stacked on one page, each followed by one "
         "paragraph that reads its index back into words."))

B["t17"] = bb(20, 1)
TABLES.append(table(
    "t17", cap("Table 17 Sensitivity analysis on k5"),
    mention(20, first=None, style=[],
            lead="k5 is the proportional coefficient of the second language growth rate and "
                 "media.",
            pattern="none", trail="Here is the result:", read=1),
    grid(3, 4, header=1, numeric=3, txt=1, rule="vertical-rules"),
    path=S_5, kind="sensitivity",
    note="Fifth and last copy of the template, alone at the head of its page; 376 pt wide "
         "because the parameter values are shorter than in Tables 13-16."))

B["f15"] = bb(20, 2)
FIGURES.append(figure(
    "f15", cap("Figure 15 Sensitivity analysis on the natural growth rate"),
    mention(20, first=None, style=[],
            lead="we only change the natural growth rate of Hindi in Asia to see what changes "
                 "it will bring.",
            pattern="none",
            trail="As the pie chart shows, subtle changes in the rate of natural increase do "
                  "not change the distribution in Asia.", read=2),
    geo("composite-panel", legend="none", panels=2, layout="1x2", labels=True),
    path=S_5, kind="sensitivity",
    note="Two pies side by side showing the same continent under two Hindi growth rates; no "
         "legend box at all, each slice labelled inline. The caption's second line names "
         "which panel is which ('0.8%(right) and 1.2%(left)'), so the reading key is in the "
         "caption rather than in a legend."))

B["f16"] = bb(21, 1)
FIGURES.append(figure(
    "f16", cap("Figure 16 The sensitivity analysis on migration coefficient"),
    mention(21, first=None, style=[],
            lead="k6 is the proportional coefficient of migration to the growth of native "
                 "language speakers.",
            pattern="none",
            trail="English and French speakers in the U.S. and Canada dropped slightly. "
                  "Besides, Australian English users dropped slightly.", read=2),
    geo("composite-panel", legend="none", panels=6, layout="6 pies on a world map",
        labels=True),
    path=S_5, kind="sensitivity",
    note="Six-pie composite on a grey world map, same family as Figures 9-11 but desaturated, "
         "with a handful of floating single-language labels outside the pies. The caption is "
         "followed by a detached '6' glyph, the subscript of k6 that lost its anchor."))

B["apx1"] = bb(23, 1)
FIGURES.append(figure(
    "apx1", cap("(1) language distribution of various continents:", "none"),
    mention(23, first=None, style=[], lead="", pattern="none", trail="", read=0),
    geo("table-as-figure", legend="none", numbers=True),
    path=S_APP, kind="appendix",
    note="Pasted spreadsheet screenshot: header row of six continent names over eighteen "
         "rows (sixteen languages, total, others). Grey vertical cell rules at every column "
         "boundary, thin rule under the header, numbers right-aligned, no zebra. The three "
         "source URLs print below the image, not inside it."))

B["apx2"] = bb(24, 1)
FIGURES.append(figure(
    "apx2", cap("(2) languages On the Internet[9]", "none"),
    mention(24, first=None, style=[], lead="", pattern="none", trail="", read=0),
    geo("table-as-figure", legend="none", numbers=True),
    path=S_APP, kind="appendix",
    note="Pasted screenshot of eighteen rows by four filled columns, with three empty grid "
         "columns still drawn; a second pasted copy of the same block sits inside the same "
         "image on the right, so the raster holds two tables."))

B["apx3"] = bb(24, 2)
FIGURES.append(figure(
    "apx3", cap("(3) GDP", "none"),
    mention(24, first=None, style=[], lead="", pattern="none", trail="", read=0),
    geo("table-as-figure", legend="none", numbers=True),
    path=S_APP, kind="appendix",
    note="Sixteen rows by three filled columns, again duplicated inside the raster, again "
         "without a header row: the label '(3) GDP' above is the only column meaning."))

B["apx4"] = bb(25, 1)
FIGURES.append(figure(
    "apx4", cap("", "none", position="above"),
    mention(25, first=None, style=[], lead="", pattern="none", trail="", read=0),
    geo("table-as-figure", legend="none", numbers=True),
    path=S_APP, kind="appendix", caption_source="none",
    note="A sixteen by sixteen language-against-language value matrix with a two-row header "
         "block (column index, then language names) and a matching stub column. It is the "
         "only table in the appendix printed without a label of its own; the heading "
         "'(4) foreign language taught in school' is stranded at the foot of the previous "
         "page with no table under it, and the matrix content does not match that heading."))

B["apx5"] = bb(25, 2)
FIGURES.append(figure(
    "apx5", cap("(5)natural growth rate:", "none"),
    mention(25, first=None, style=[], lead="", pattern="none", trail="", read=0),
    geo("table-as-figure", legend="none", numbers=True),
    path=S_APP, kind="appendix",
    note="Sixteen rows by four columns with a printed header (NO., language, natural growth "
         "rate (%), Main countries); unlike its neighbours this one carries no vertical "
         "rules at all, only faint per-row separators and one rule under the header."))
RULES = [
    "Caption side is decided by exhibit kind, not by section: every one of the twenty "
    "figures prints its caption under the artwork and every one of the seventeen tables "
    "prints its caption over the grid. The paper never mixes the two conventions "
    "[caption.position].",
    "Numbering is the bare two-word form 'Figure N' / 'Table N' with no period, no colon and "
    "no bold run, and it reaches fifteen of the twenty figures and fifteen of the seventeen "
    "tables; the seven that carry no number are the two headerless continuations and the five "
    "appendix screenshots, four of which are labelled '(1)' to '(5)' instead "
    "[caption.numbering].",
    "Captions are noun phrases, never sentences: the longest runs fifteen words and still "
    "contains no verb with a subject, and the two-part ones park the reading key in a second "
    "caption line instead of a legend [caption.words].",
    "No caption states a numerical result, a condition or a parameter value except Figure "
    "15, whose second line carries the two growth rates that distinguish its panels; "
    "everywhere else the numbers live in the body text or in the table [caption.conditions].",
    "Units are handled in three different places for the same kind of quantity: sometimes in "
    "the caption ('Unit: million'), sometimes inside a header cell ('C-p ratio (unit: "
    "million)'), and in the appendix sometimes in the header of a pasted screenshot "
    "[table.units_in_header].",
    "The house rule style is a hybrid, not booktabs and not a box: three horizontals "
    "(top, under-header, bottom) plus exactly one vertical rule that divides the stub from "
    "the data columns. Sixteen of the seventeen grids are built this way; the single "
    "exception is the second half of Table 4, which keeps the horizontals and drops the "
    "divider [table.rule_style].",
    "No table in the paper uses alternating row shading; the pasted spreadsheet screenshots "
    "in the appendix carry faint per-cell rules instead, which is a different device for the "
    "same job and arrives only because the image was not typeset [table.zebra].",
    "No merged cell and no diagonal header appears anywhere: where a label needs to span "
    "(types of languages, the six continents, the sixteen codes) the authors either let the "
    "cell wrap onto several lines or repeat the row label [table.merged_cells].",
    "Decimal alignment is never used even though Table 6 prints four- and five-decimal "
    "values in the same column; numbers are centred or right-aligned by cell, so digits do "
    "not line up [table.decimal_aligned].",
    "A table that crosses a page break loses all three of its identity markers: Table 4 and "
    "Table 6 both continue as headerless, captionless halves and Table 4 even drops the "
    "vertical rule, so the second half is only recognisable by column count [table.continued].",
    "Every exhibit in the body is a pasted raster image, not a redrawn vector graphic: the "
    "maps, pies, donuts and the paired bar chart all carry Excel or MATLAB screenshot "
    "styling, and the only vector artwork is the neighbourhood network [geometry.family].",
    "Legend placement follows artwork type: maps and the office-siting figures keep the key "
    "inside the frame, standalone pies and donuts push it outside to the right, and the "
    "composite pies abandon the legend altogether and label each slice inline "
    "[geometry.legend].",
    "No figure is three-dimensional and none carries a continuous colourbar: the two "
    "choropleths use discrete class swatches with the unit spelled on the legend instead "
    "[geometry.colorbar].",
    "Composite exhibits are quantities of six when they are geographic: Figures 9, 10, 11 "
    "and 16 each place exactly six pies at continent positions on a map, so the number of "
    "panels is the number of continents and the layout is cartographic rather than a grid "
    "[geometry.panel_count].",
    "Cross-references and captions disagree throughout: the body cites Figures 3, 14, 17 and "
    "18 and Table 7 and Table 9, none of which the paper ever prints, and in each case the "
    "content it refers to sits one number lower. No exhibit in this paper is ever correctly "
    "cited by number, so first_page is null for all twenty figures and all seventeen tables "
    "[mention.first_page].",
    "Lead-in sentences describe the subject and stop there: where an exhibit is announced at "
    "all it is announced as content ('the chart below is our result', 'below is the language "
    "distribution', 'are shownbelow:'), four times in that as-shown-in form and once "
    "parenthetically, and the figure-number-shows construction never occurs anywhere in the "
    "paper [mention.lead_pattern].",
    "The reading sentence always sits after the exhibit and converts it into a claim with a "
    "reason ('therefore, we divide Earth language data into six continents'), one paragraph "
    "per exhibit and never a bullet list under the artwork [mention.trail_sentence].",
    "Exhibit type tracks section kind rather than page position: model sections hold the "
    "network, the mechanism maps and the pie witnesses of one factor each, result sections "
    "hold the three pie composites plus the ranking and parameter tables, and sensitivity "
    "sections hold the five identically built three-row grids and the two closing composites "
    "[place.section_kind].",
    "Placement splits by exhibit kind: seventeen of the twenty figures sit in the top or "
    "middle third of their page and only three reach the bottom, while thirteen of the "
    "seventeen tables sit in the middle or bottom third, so the page reads figure-over-table "
    "[place.page_zone].",
]

NOTE = (
    "Two-part paper: Part I is a difference-equation speaker model for sixteen languages, "
    "Part II is a six-office siting model, and the exhibit grammar changes between them. "
    "Part I is schematic-heavy (mechanism map, neighbourhood network, GDP donut, internet "
    "pie) and its tables are data dumps that run past a page break. Part II is map-heavy "
    "(two choropleths with office pins) and its tables are small decision aids: the "
    "cost-profit interval table and the city ranking. Sensitivity analysis is a third "
    "grammar again: five copies of one three-row grid, each read back to the reader in a "
    "single paragraph, followed by two composite visuals.\n\n"
    "Three structural traps. First, the numbering has holes at Figure 3, Figure 14, Figures "
    "17-18, Table 7 and Table 9, and every hole is exactly where a cross-reference points, "
    "so an auditor who trusts the prose will look for exhibits that were never printed and "
    "miss the ones that were. Second, both page-crossing tables (Table 4 and Table 6) lose "
    "their header, caption and column rule on the second half, which means the continuation "
    "must be recorded as its own grid with caption_source none rather than read as prose. "
    "Third, Figure 5 is one printed object delivered as two separate region boxes with a "
    "single caption line running under both halves, so region counting alone overstates the "
    "figure count by one.\n\n"
    "Coverage note: all six display-equation images (the Malthus equation, the LangT sum, "
    "the three numbered model equations on page 9, the six-sum difference equation and the "
    "piecewise c-p test) are boxed by the region pass and none of them is an exhibit; they "
    "are excluded as not-an-exhibit, together with one prose region on page 13 that the "
    "detector mistook for artwork."
)
ALL: list[dict] = FIGURES + TABLES
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
    f"unclaimed {sorted(MEASURED - _claimed)} extra {sorted(_claimed - MEASURED)}")
assert len(ALL) + len(EXCLUDED) == len(MEASURED) == 43, (
    len(ALL), len(EXCLUDED), len(MEASURED))

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"key": k, "page": p, "bbox": b, "reason": r} for k, (p, b), r in EXCLUDED
    ],
    "rules": RULES,
    "note": NOTE,
}


def main() -> None:
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"figures {len(FIGURES)} tables {len(TABLES)} excluded {len(EXCLUDED)} "
          f"-> {out.name}")
    fam: dict[str, int] = {}
    for it in FIGURES:
        fam[it["geometry"]["family"]] = fam.get(it["geometry"]["family"], 0) + 1
    print("families", dict(sorted(fam.items())))
    legs: dict[str, int] = {}
    for it in FIGURES:
        legs[it["geometry"]["legend"]] = legs.get(it["geometry"]["legend"], 0) + 1
    print("legends", dict(sorted(legs.items())))
    pos = {"figure": {}, "table": {}}
    for it in FIGURES:
        pos["figure"][it["caption"]["position"]] = pos["figure"].get(
            it["caption"]["position"], 0) + 1
    for t in TABLES:
        pos["table"][t["caption"]["position"]] = pos["table"].get(
            t["caption"]["position"], 0) + 1
    print("caption side", pos)
    rules: dict[str, int] = {}
    for t in TABLES:
        rules[t["table"]["rule_style"]] = rules.get(t["table"]["rule_style"], 0) + 1
    print("rule styles", rules)
    widths = sorted({round(t["bbox"][2] - t["bbox"][0], 1) for t in TABLES})
    print("table widths pt", widths)
    print("cited exhibits", sum(1 for it in FIGURES if it["mention"]["first_page"]))
    print("numbered captions",
          sum(1 for it in FIGURES if it["caption"]["numbering"] != "none"))
    kinds: dict[str, int] = {}
    for it in ALL:
        kinds[it["place"]["section_kind"]] = kinds.get(it["place"]["section_kind"], 0) + 1
    print("section kinds", dict(sorted(kinds.items())))


if __name__ == "__main__":
    main()
