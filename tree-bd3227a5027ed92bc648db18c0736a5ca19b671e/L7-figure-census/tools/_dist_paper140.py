"""Hand pass for P-F-2017-68940-3e5f9c47 (UTOPIA: 2100, Mars colony agent model).

Shape of the paper: a cover letter to the LIFE director, a NetLogo agent-based model of a
10,000-person colony, ten typeset grids of parameters and results, and a 23-page NetLogo code
appendix. 52 pages, 46 measured regions.

What the record has to say out loud:

1. The paper has almost no captions. Three of the eleven printed figures carry a numbered
   caption, and only two of the ten grids do. The other fourteen exhibits are announced by a
   deictic sentence ("... is illustrated below [37]:", "The following are the tax brackets ...
   as follows:") or by nothing at all - the p2 histogram is never mentioned in the text.
2. Every one of the ten grids is boxed with verticals at every cell boundary. There is no
   booktabs grid, no horizontal-rules-only grid and no shaded row anywhere in the paper.
3. Tables 1 and 2 are cited seventeen pages before they print: the sentence on p7 says they are
   "in the Appendix", and they are - on pp24 and 25.
4. The p20 triple and the p16 pair are one figure split into separately measured regions, so the
   panels of each set repeat a doc_order and carry is_panel_of.
5. Page size is not uniform: the layout's first page is US letter (612x792 pt) but the cover
   letter on p2 is A4 (595.28x841.89 pt), so area fractions are computed per page.

Usage: python -I tools/_dist_paper140.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-F-2017-68940-3e5f9c47"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    # figures
    "fig_age_cover": (2, [177.2, 620.0, 418.1, 780.6]),
    "fig_flow": (10, [79.2, 109.7, 532.8, 414.5]),
    "fig_world_infl": (10, [177.8, 541.9, 434.2, 717.0]),
    "fig_canada": (11, [249.3, 96.4, 362.7, 199.3]),
    "fig_cpi": (12, [177.8, 212.0, 434.2, 332.9]),
    "fig_age_a": (16, [73.3, 338.1, 304.1, 491.9]),
    "fig_age_b": (16, [307.9, 338.1, 538.7, 491.9]),
    "fig_3a": (20, [56.0, 424.2, 220.1, 505.7]),
    "fig_3b": (20, [223.9, 425.2, 388.0, 505.7]),
    "fig_3c": (20, [391.9, 425.6, 556.0, 505.7]),
    "fig_edu": (21, [249.3, 52.1, 362.7, 136.4]),
    # tables
    "tab_edu": (8, [197.1, 655.5, 414.9, 744.7]),
    "tab_prob": (9, [188.7, 96.6, 423.4, 132.3]),
    "tab_tax": (11, [147.8, 530.8, 464.2, 655.6]),
    "tab_minwage": (17, [180.3, 370.7, 431.7, 459.9]),
    "tab_leave": (18, [99.7, 326.8, 512.3, 537.2]),
    "tab_debt": (19, [180.6, 93.6, 431.4, 343.3]),
    "tab_invest": (19, [203.5, 432.7, 408.5, 557.5]),
    "tab_subgroups": (21, [49.6, 316.3, 562.4, 701.1]),
    "tab1": (24, [72.9, 105.5, 539.1, 515.6]),
    "tab2": (25, [64.8, 79.2, 547.2, 489.4]),
}

EXCLUDED = {
    "p1 sheet": (1, [0.0, -45.0, 612.0, 245.8]),
    "p2 banner": (2, [59.5, 52.5, 550.2, 100.9]),
    **{f"p{n} code": (n, [49.6, 71.0 if n == 26 else 55.7, 562.4,
                          743.9 if n == 26 else 737.1]) for n in range(26, 48)},
    "p48 code": (48, [49.6, 55.7, 562.4, 429.7]),
}

for _name, (_p, _b) in {**B, **EXCLUDED}.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 46, len(MEASURED)

HEAD = {k: f"未编号标题 {k}" for k in
        ("Model", "Results", "Sensitivity Analysis", "Appendix")}


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    w, h = DIMS[page]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < h / 3 else ("middle" if mid < 2 * h / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    return {
        "section_path": path,
        "section_numbered": False,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 1,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": False,
    }


def cap(v: str, numbering: str, *, units: bool = False, vars_: int = 0,
        conditions: bool = False, concludes: bool = False, voice: str = "none",
        position: str = "below") -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)) if v else 0,
        "units": units,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": conditions,
        "concludes": concludes,
        "voice": voice,
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


def geo(family: str, *, panels: int = 1, layout_: str = "1", shared: bool = False,
        legend: str = "none", colorbar: bool = False, three_d: str = "no",
        numbers: bool = True, labels: bool = False) -> dict:
    return {
        "family": family,
        "panel_count": panels,
        "panel_layout": layout_,
        "shared_axes": shared,
        "legend": legend,
        "colorbar": colorbar,
        "three_d": three_d,
        "printed_numbers": numbers,
        "data_labels": labels,
    }


def figure(key: str, family: str, caption: dict, men: dict, geom: dict, *,
           path: list[str], kind: str, src: str = "text-layer", panels: int = 1,
           of: str = "", note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "is_panel_of": of,
        "caption_verbatim": caption["verbatim"],
        "caption_source": src,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed",
         merged: bool = False, decimal: bool = False, numeric: int = 0, txt: int = 0,
         width: str = "column", note_sentence: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rules,
        "zebra": False,
        "merged_cells": merged,
        "diagonal_header": False,
        "units_in_header": False,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": False,
        "note_sentence": note_sentence,
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          src: str = "text-layer", note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": caption["verbatim"],
        "caption_source": src,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "table": g,
    }


def U(*labels: str) -> list[str]:
    return [f"未编号标题 {lab}" for lab in labels]


P_MODEL = [HEAD["Model"]]
S_CENSUS = U("Model", "The Census Data")
S_BIRTH = U("Model", "Birth and Death")
S_GLOBAL = U("Model", "Global Inﬂation")
S_TAXES = U("Model", "Economic Indicators & Essentials", "Taxes")
S_DEBT = U("Model", "Economic Indicators & Essentials", "Government Spending and Debt")
S_POPZERO = U("Model", "Characteristics of Population Zero")
S_MINWAGE = U("Results", "Optimal Salary and Minimum Wage Distribution")
S_LEAVE = U("Results", "Maternity and Paternity Leave")
S_SUBGROUPS = U("Results", "The Subgroups of the Workforce")
S_100Y = U("Results", "100-year")
S_SENS = [HEAD["Sensitivity Analysis"]]
S_APPX = [HEAD["Appendix"]]
S_COVER = U("Policy Advisory")

GEO_HIST = geo("histogram", numbers=True, labels=False)
GEO_HIST2 = geo("histogram", panels=2, layout_="1x2", numbers=True, labels=False)
GEO_HIST3 = geo("histogram", panels=3, layout_="1x3", numbers=True, labels=False)
GEO_LINE = geo("line", numbers=True, labels=False)

FIGURES = [
    figure("fig_age_cover", "histogram", NOCAP,
           mention(2, first=None, style=[]),
           GEO_HIST, path=S_COVER, kind="other", src="none",
           note="the only exhibit before the body text: an age histogram printed at the foot of "
                "the cover letter to the LIFE director, with axes age against count and no title, "
                "no legend and no caption. Nothing in the letter refers to it - the letter is "
                "prose only - so this is the paper's only completely uncited figure"),
    figure("fig_flow", "flowchart-or-schematic",
           cap("Figure 1: A Flowchart illustrating the life of individual agents in the model.",
               "Figure N:"),
           mention(10, first=10, style=["the following ﬂowchart"], pattern="as-shown-in",
                   lead="To illustrate the life cycle, we provide the following ﬂowchart."),
           geo("flowchart-or-schematic", numbers=False, labels=True),
           path=S_BIRTH, kind="model",
           note="a NetLogo-style state diagram of the agent life cycle: birth and education boxes, "
                "a workforce state, a stay-at-home-parent state and a retirement state, joined by "
                "labelled transition arcs. The arcs carry condition text rather than numbers, so "
                "printed_numbers is false and data_labels true"),
    figure("fig_world_infl", "line", NOCAP,
           mention(10, first=10, style=["illustrated below"], pattern="as-shown-in",
                   lead="US inﬂation from 1923 to 2012 is illustrated below [37]:"),
           geo("line", legend="inside", numbers=True),
           path=S_GLOBAL, kind="model", src="none",
           note="a pasted Gapminder screenshot rather than a drawn plot: the browser's own UI is "
                "printed inside the image - a country selector chip reading WORLD above a time "
                "scrubber bar - and the legend is that chip, not a plot legend. The series is a "
                "single thin line on a white field with no axis titles. Recorded as family 'line' "
                "because what is printed is a line chart; the medium is a screenshot"),
    figure("fig_canada", "line", NOCAP,
           mention(11, first=11, style=["the following ﬁgure"], pattern="as-shown-in",
                   lead="From the following ﬁgure, we see that Canada has a very stable inﬂation "
                        "rate [40]:"),
           GEO_LINE, path=S_GLOBAL, kind="model", src="none",
           note="a Canadian inflation series borrowed from a web source: no title, no axis titles, "
                "no legend, and x tick labels printed as bare two-digit years running 95 to 15 so "
                "that the axis is unreadable to a reader who does not already know the century"),
    figure("fig_cpi", "line", NOCAP,
           mention(12, first=12, style=["the following graph"], pattern="as-shown-in",
                   lead="To model inﬂation rates in our society, we consider the following graph "
                        "[53]:"),
           GEO_LINE, path=S_DEBT, kind="model", src="none",
           note="the paper's only figure with an in-plot title, printed inside the plot area as "
                "'CPI-U Annual % Change Last 10 Years September 1923 - 2012'. No legend, no axis "
                "titles, no caption, and the title duplicates in the plot what a caption would "
                "have said"),
    figure("fig_age_a", "histogram",
           cap("(a) The initial age distribution", "none"),
           mention(16, first=16, style=["Figure 2a"], pattern="as-shown-in",
                   lead="as seen in Figure 2a."),
           GEO_HIST2, path=S_POPZERO, kind="model", panels=2, of="Figure 2",
           note="left half of the Figure 2 pair: a ggplot histogram of the sampled initial ages. "
                "Its x axis label prints the literal call 'norm(10000, mean = 30, sd = 24)' "
                "because the code string was passed through instead of a variable label. The "
                "figure number in the text refers to a figure that prints no 'Figure 2' caption "
                "anywhere - only the two panel captions"),
    figure("fig_age_b", "histogram",
           cap("(b) The age distribution of Population Zero", "none"),
           mention(16, first=16, style=["Figure 2b"], pattern="as-shown-in",
                   lead="This age distribution is illustrated in Figure 2b and is designed"),
           GEO_HIST2, path=S_POPZERO, kind="model", panels=2, of="Figure 2",
           note="right half of the Figure 2 pair, same template as (a): bars against age with the "
                "same axis geometry. The two panels do not share a y scale - (b) is the smoother "
                "of the two and runs to a lower maximum count - so shared_axes is false"),
    figure("fig_3a", "histogram",
           cap("Figure 3: Age distributions across a 100-year model", "Figure N:"),
           mention(20, first=20, style=["Figure 3a"], pattern="as-shown-in",
                   lead="as seen in Figure 3a."),
           GEO_HIST3, path=S_100Y, kind="result", panels=3, of="Figure 3",
           note="first of three panels printed side by side under one figure caption. Its y axis "
                "runs to 200; the three panels are on separate scales (200 / 205 / 246) so they "
                "cannot be compared bar-for-bar without reading the ticks"),
    figure("fig_3b", "histogram",
           cap("Figure 3: Age distributions across a 100-year model", "Figure N:"),
           mention(20, first=20, style=["Figure 3b"], pattern="as-shown-in",
                   lead="of new generations completely take over, as seen in Figure 3b."),
           GEO_HIST3, path=S_100Y, kind="result", panels=3, of="Figure 3",
           note="middle panel of Figure 3, y axis to 205. Its panel caption is the printed letter "
                "(b) alone - the shared caption is the only prose this figure gets"),
    figure("fig_3c", "histogram",
           cap("Figure 3: Age distributions across a 100-year model", "Figure N:"),
           mention(20, first=20, style=["Figure 3c"], pattern="as-shown-in",
                   lead="eventually reach the steady state that is visible in Figure 3c"),
           GEO_HIST3, path=S_100Y, kind="result", panels=3, of="Figure 3",
           note="third panel of Figure 3, y axis to 246 and the widest spread of the three; the "
                "steady state the text points at is the flat tail of this panel"),
    figure("fig_edu", "line",
           cap("Figure 4: Notice the sudden drop then spike in the education metric", "Figure N:",
               voice="active"),
           mention(21, first=None, style=[]),
           geo("line", numbers=True),
           path=S_100Y, kind="result",
           note="the smallest figure in the paper at 0.020 of the page, about 113x84 pt: a "
                "single-series line with no axis titles and only four endpoint tick labels. It is "
                "cited by its caption alone - no sentence in the body names Figure 4"),
]

TABLES = [
    table("tab_edu", NOCAP,
          mention(8, first=8, style=[], pattern="direct",
                  lead="The probability that a worker becomes a stay-at-home parent depends upon "
                       "his/her gender and is inversely proportional to his/her level of education"),
          grid(5, 3, decimal=True, numeric=2, txt=1),
          path=S_CENSUS, kind="model", src="none",
          note="three columns of degree level against sex, four body rows (Associate, Bachelor, "
               "Master, Ph. D), two decimals per cell aligned on the point. No caption and no "
               "table number: the announcing sentence on the same page ends in the deixis 'level "
               "of education' and the grid supplies the data for it"),
    table("tab_prob", NOCAP,
          mention(9, first=9, style=[], pattern="direct",
                  lead="The probabilities p2, p4, p6, and p8 are set using the 2015 US Census "
                       "Bureau data on Educational Attainment: [28]:"),
          grid(2, 4, numeric=4, txt=0),
          path=S_CENSUS, kind="model", src="none",
          note="the paper's only two-row grid: one header row of degree names and one row of four "
               "counts (22537 46515 18683 6987). It has no caption and no number, and the sentence "
               "above it ends in a colon plus a bracketed citation - the grid is the rest of that "
               "sentence"),
    table("tab_tax", NOCAP,
          mention(11, first=11, style=[], pattern="direct",
                  lead="The following are the tax brackets and their corresponding rates:"),
          grid(7, 2, numeric=1, txt=1),
          path=S_TAXES, kind="model", src="none",
          note="the only grid whose cells hold algebra rather than numbers: six bracket rules "
               "against their rates, with fractions such as 'OTR 2 / 6' set as stacked fractions. "
               "A grid can carry typed mathematics in the value column, so numeric_cols is 1 and "
               "text_cols 1"),
    table("tab_minwage", NOCAP,
          mention(17, first=17, style=["the table above"], pattern="direct",
                  trail="In the table above, we see a deﬁnite positive correlation between "
                        "minimum wage and GDP", read=1),
          grid(5, 3, decimal=False, numeric=3, txt=0),
          path=S_MINWAGE, kind="result", src="none",
          note="four body rows stepping the minimum wage from 65000 to 80000 by 5000 with the "
               "income metric and GDP beside each. Cited only from below ('In the table above'), "
               "so the reader has to be looking back at the grid already"),
    table("tab_leave", NOCAP,
          mention(18, first=18, style=["the table above"], pattern="direct",
                  trail="In the table above, we see that the relationship between "
                        "maternity/paternity leave and the income", read=1),
          grid(12, 4, header=2, merged=True, decimal=True, numeric=2, txt=2, width="full"),
          path=S_LEAVE, kind="result", src="none",
          note="the widest grid and the only two-tier header: 'Maternity Leave - 10 Months' and "
               "'Paternity Leave - 3 Months' each span two columns, over a second header row "
               "pairing a month count with an income metric. Ten body rows, third-decimal values "
               "aligned on the point"),
    table("tab_debt", NOCAP,
          mention(19, first=19, style=[], pattern="direct",
                  lead="This relationship is described as follows:"),
          grid(14, 3, decimal=False, numeric=3, txt=0),
          path=S_SUBGROUPS, kind="result", src="none",
          note="the tallest grid: thirteen body rows stepping the tax rate from 30 to 90 by 5 "
               "against the income metric and government debt. Government debt falls "
               "monotonically across the whole column while the income metric barely moves"),
    table("tab_invest", NOCAP,
          mention(19, first=19, style=[], pattern="direct",
                  lead="The relationship between tax-rate and investment is as follows:"),
          grid(7, 2, decimal=False, numeric=2, txt=0),
          path=S_SUBGROUPS, kind="result", src="none",
          note="second grid on p19, six body rows of tax rate against innovator investment. It "
               "starts at a tax rate of 35 because that is where the innovators' row begins in "
               "the taller grid above - the two grids are read as one argument split into two "
               "blocks"),
    table("tab_subgroups", NOCAP,
          mention(21, first=21, style=[], pattern="direct",
                  lead="all of the following selection processes are highly sustainable"),
          grid(7, 3, decimal=False, numeric=1, txt=2, width="full"),
          path=S_SENS, kind="sensitivity", src="none",
          note="the sensitivity grid: six initial populations against a running description of "
               "each one's behaviour and a free-text verdict column. The middle column wraps to "
               "five and six lines per cell, so the grid is full width even though it holds only "
               "three columns"),
    table("tab1", cap("Table 1", "Table N", position="above"),
          mention(24, first=7, style=["Table 1"], pattern="as-shown-in",
                  lead="Our calculations can be are summarized in Table 1 and Table 2 in the "
                       "Appendix."),
          grid(23, 3, decimal=True, numeric=2, txt=1),
          path=S_APPX, kind="appendix",
          note="the appendix occupation table: 22 body rows, one per occupation, with the "
               "education level required and a workers-in-2015 value to four decimals. Caption is "
               "the bare word 'Table 1' above the grid - no colon, no descriptive phrase. The text "
               "layer prints one row's name before its numbers and loses the last row's numbers, "
               "so the reading order in the extraction is shifted; the raster prints each row on "
               "its own line"),
    table("tab2", cap("Table 2", "Table N", position="above"),
          mention(25, first=7, style=["Table 2"], pattern="as-shown-in",
                  lead="Our calculations can be are summarized in Table 1 and Table 2 in the "
                       "Appendix."),
          grid(23, 3, decimal=False, numeric=2, txt=1),
          path=S_APPX, kind="appendix",
          note="the same 22 occupations with an income and an income growth rate, integers with no "
               "decimal point, so unlike Table 1 it is not decimal-aligned. Its header prints "
               "'Income8' - a footnote marker has run into the column label"),
]

EXCLUDED_REGIONS = [
    {"page": p, "bbox": b, "reason": "not-an-exhibit", "note": n}
    for n, (p, b) in (
        ("p1 sheet", EXCLUDED["p1 sheet"]),
        ("p2 banner", EXCLUDED["p2 banner"]),
        *((f"p{n} code", EXCLUDED[f"p{n} code"]) for n in range(26, 49)),
    )
]

RULES = [
    "Twelve of the twenty-one exhibits print with caption_source 'none': four figures (p2, the p10 "
    "world series, p11, p12) and eight of the ten grids (pp8, 9, 11, 17, 18 and both grids on "
    "p19) [caption.verbatim].",
    "The two caption grammars do not mix: every figure caption that prints is a sentence with a "
    "'Figure N:' prefix, and the two table captions are the bare words 'Table 1' and 'Table 2' "
    "with no colon and no text [caption.numbering].",
    "Figure captions print below their exhibit and the two table captions print above theirs, so "
    "the side is set by exhibit type in this paper rather than by chapter [caption.position].",
    "No caption in the paper names a unit, a condition or a parameter, and only Figure 4 states "
    "anything a reader could act on ('Notice the sudden drop then spike') [caption.concludes].",
    "Captions are short: the three numbered figure captions run 8 to 13 words, the two p16 panel "
    "captions are 5 and 7 words, and each table caption is the two-word label alone "
    "[caption.words].",
    "The p16 pair and the p20 triple are each one figure split into separately measured regions, "
    "so both items in a pair and all three items in a triple repeat a doc_order and carry "
    "is_panel_of [place.doc_order].",
    "Neither set of panels shares a scale: the p16 pair is drawn on independent y maxima, and the "
    "p20 triple runs 200 / 205 / 246, so no figure in the paper is readable across its panels "
    "without reading the ticks [geometry.shared_axes].",
    "Six of the eleven figures are ggplot output - the six histograms - and all six print tick "
    "labels and nothing else. No figure in the paper prints a data label on a mark: charts are "
    "read off axes, never off labels [geometry.data_labels].",
    "No figure is three-dimensional, no figure carries a colourbar, and the only legend in the "
    "paper is the country chip baked into the Gapminder screenshot on p10 [geometry.legend].",
    "Two figures are screen captures rather than plots: the p10 world inflation series has a "
    "browser country selector and time scrubber printed inside it, and the p11 Canadian series "
    "prints bare two-digit year ticks (95 to 15). Both are recorded by what they show, not by how "
    "they were made [geometry.family].",
    "Every one of the ten grids is boxed: a rule at the top, a rule under the header, rules "
    "between body rows and verticals at every cell boundary. The paper contains no booktabs grid "
    "and no rules-only grid [table.rule_style].",
    "No grid is shaded - there is no zebra striping and no tinted cell in the paper, including "
    "the 22-row appendix tables where striping would have helped [table.zebra].",
    "Only the maternity/paternity grid merges cells, and it is also the only grid with two header "
    "rows: each leave type spans the two columns beneath it [table.merged_cells].",
    "Grid width tracks column count and cell text, not importance: the two 22-row appendix tables "
    "and the six-row sensitivity grid are full width because their cells wrap to several lines, "
    "the four-column leave grid is full width, and the four two- and three-column result grids "
    "stay in the column [table.width].",
    "The two result grids on p19 are one argument split into two blocks: the tax/investment grid "
    "starts at a tax rate of 35 because that is where the row range it continues begins "
    "[table.rows].",
    "Three of the ten grids are decimal-aligned - the education table (two decimals), the leave "
    "table (three decimals) and Table 1 (four decimals) - and the other seven hold integers or "
    "algebra and are not [table.decimal_aligned].",
    "Six grids are announced by a deictic sentence on their own page and cited by nothing else - "
    "'the following are the tax brackets', 'This relationship is described as follows:', 'as "
    "seen in Figure 2a.' - with no figure or table number in the announcing sentence "
    "[mention.style].",
    "Two grids are cited from below only ('In the table above, we see ...'), so the sentence that "
    "reads the grid comes after it and the sentence that announces it does not exist "
    "[mention.trail_sentence].",
    "Tables 1 and 2 are announced on p7 and print on pp24 and 25, a seventeen-page lead, because "
    "the announcing sentence sends the reader to the appendix rather than promising a nearby "
    "float [mention.lead_pages].",
    "Two exhibits are never cited at all - the cover-letter histogram on p2 and the "
    "education-metric line on p21, which is named by its caption alone - and every other exhibit "
    "is mentioned exactly once [mention.count].",
    "Exhibit size tracks nothing: the largest figure is the life-cycle flowchart at 0.285 of its "
    "page and the smallest is Figure 4 at 0.020, but the paper's headline comparison is carried "
    "by a 0.046 grid [place.area_frac].",
    "Section kinds follow the paper's own shape: the model chapter holds six figures and five "
    "grids, the results chapter five figures and four grids, sensitivity one grid, and the "
    "appendix the two 22-row tables [place.section_kind].",
]

NOTE = (
    "A 52-page NetLogo agent-based modelling paper with eleven printed figures and ten typeset "
    "grids, of which only three figures and two tables carry a caption. The caption set is two "
    "grammars: sentences prefixed 'Figure N:' below the figure, and the bare words 'Table 1' and "
    "'Table 2' above the grid. Every grid is boxed with verticals at every cell boundary, none is "
    "shaded, and only the four-column maternity/paternity grid merges cells or carries two header "
    "rows. Six grids are announced by deixis on their own page; two are read from below; Tables 1 "
    "and 2 are announced on p7 and print seventeen pages later in the appendix. The p16 pair and "
    "the p20 triple are measured as separate regions of one figure each, so two doc_orders repeat "
    "across panels and neither set shares a scale. Two figures are pasted screen captures with "
    "interface furniture printed inside them. The cover letter's p2 histogram is the paper's only "
    "wholly uncited exhibit, and the education-metric line on p21 is cited by caption alone."
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
    "fig_age_cover": 1, "tab_edu": 2, "tab_prob": 3, "fig_flow": 4, "fig_world_infl": 5,
    "fig_canada": 6, "tab_tax": 7, "fig_cpi": 8, "fig_age_a": 9, "fig_age_b": 9,
    "tab_minwage": 10, "tab_leave": 11, "tab_debt": 12, "tab_invest": 13,
    "fig_3a": 14, "fig_3b": 14, "fig_3c": 14, "fig_edu": 15, "tab_subgroups": 16,
    "tab1": 17, "tab2": 18,
}

_order = sorted(
    [(k, v) for k, v in DOC_ORDER.items()],
    key=lambda kv: (B[kv[0]][0], B[kv[0]][1][1], B[kv[0]][1][0]),
)
_seen_page: dict[int, int] = {}
for _key, _doc in _order:
    _page = B[_key][0]
    _seen_page[_page] = _seen_page.get(_page, 0) + 1
    for _e in FIGURES + TABLES:
        if _e["page"] == _page and _e["bbox"] == B[_key][1]:
            _e["place"]["doc_order"] = _doc
            _e["place"]["page_order"] = _seen_page[_page]


def main() -> int:
    from collections import Counter

    exhibits = FIGURES + TABLES
    assert all(e["place"]["doc_order"] for e in exhibits), "unnumbered exhibit"
    print("figures", len(FIGURES), "tables", len(TABLES), "excluded", len(EXCLUDED_REGIONS))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in exhibits)))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in exhibits)))
    print("fam", dict(Counter(e["family"] for e in FIGURES)))
    print("cap.src", dict(Counter(e["caption_source"] for e in exhibits)))
    print("cap.num", dict(Counter(e["caption"]["numbering"] for e in exhibits)))
    print("cap.pos", dict(Counter(e["caption"]["position"] for e in exhibits)))
    print("men.first", dict(Counter(e["mention"]["first_page"] for e in exhibits)))
    print("men.pat", dict(Counter(e["mention"]["lead_pattern"] for e in exhibits)))
    print("grid.rules", dict(Counter(t["table"]["rule_style"] for t in TABLES)))
    print("grid.rows", [t["table"]["rows"] for t in TABLES])
    print("area", [e["place"]["area_frac"] for e in exhibits])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
