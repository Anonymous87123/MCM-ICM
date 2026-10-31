"""Hand pass for P-F-2017-64486-62f12f04 (Mars colony workforce / UTOPIA:2100).

Shape of the paper: a ten-parameter society model fed by PUMS 2015 census records, an AHP weighting
of GDP and Happiness indices, a hundred-year agent simulation of 10000 migrants, an equilibrium
search over minimum wage and parental leave, and a migration-plan comparison. 34 pages, 25 printed
figures, 8 printed tables.

What the record has to say out loud:

1. Nearly every exhibit is a tool export. Figures 4-11 are eight untuned distribution plots pasted
   as one 4x2 block, Figure 1 is a Word drawing that still carries its text-selection highlights,
   Figure 2 is a word-cloud generator export, Figures 12/15/17/19-21/24-25 come out of spreadsheets
   and plotting defaults, and Figures 13/16/18 are shape-tool drawings. Only the five tables are
   typeset.
2. The caption side is uniform and is the inverse of the sibling paper one row up the queue: all 25
   figure captions below their artwork, all table captions above their grid.
3. Three tables print with no measured region and are declared gaps, not patched: Tables 2 and 3 at
   the top of p9 (only Table 4, at the foot of the same page, returns a box) and Table 7 on p20.
4. Three pages of figure caption text come back interleaved - p11's four caption pairs, p15's pair
   and p17's pair - so eleven captions are typed from the crop.
5. Cross-reference faults: Figures 10 and 11 are never cited by number, Figures 14 and 16 are never
   cited at all, Figure 23 is cited a page after it prints, and the prose calls the class-transition
   chart "Table 5" on p16 while Table 5 is the income-distribution grid.
6. Three regions are not exhibits and are excluded: the ICM summary-sheet control block on p1 and
   the two MATLAB code slabs of the appendix (p27, p34).

Usage: python -I tools/_dist_paper139.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-F-2017-64486-62f12f04"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((LANE / f".proxy/{PID}-ctx.json").read_text(encoding="utf-8"))

MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}
PAGE_W = LAYOUT["pages"][0]["width"]
PAGE_H = LAYOUT["pages"][0]["height"]

# The heading index is polluted by the printed table of contents (p3) and by hyphenated
# continuation lines, so take the last occurrence of each number that starts with it.
HEAD: dict[str, str] = {}
for _h in CTX["headings"]:
    _n, _l = _h.get("number"), _h.get("label")
    if not _n or not _l or not _l.startswith(_n + " "):
        continue
    HEAD[_n] = _l


def H(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


B = {
    # figures, in printed order
    "fig1": (6, [116.1, 72.0, 476.2, 266.8]),
    "fig2": (7, [165.4, 572.4, 426.9, 742.5]),
    "fig3": (10, [201.8, 72.0, 390.5, 185.4]),
    "fig4": (11, [50.7, 72.0, 277.4, 201.2]),
    "fig5": (11, [308.8, 72.0, 535.6, 201.2]),
    "fig6": (11, [50.7, 237.9, 277.4, 367.1]),
    "fig7": (11, [308.8, 237.9, 535.6, 367.1]),
    "fig8": (11, [50.7, 406.4, 277.4, 535.5]),
    "fig9": (11, [308.8, 406.4, 535.6, 535.5]),
    "fig10": (11, [50.7, 572.3, 277.4, 701.5]),
    "fig11": (11, [308.8, 572.3, 535.6, 701.5]),
    "fig12": (13, [43.6, 72.0, 568.1, 348.0]),
    "fig13": (15, [60.2, 72.0, 201.9, 213.7]),
    "fig14": (15, [235.8, 90.1, 576.0, 201.2]),
    "fig15": (17, [43.6, 72.0, 270.4, 204.1]),
    "fig16": (17, [261.2, 91.5, 572.9, 140.1]),
    "fig17": (18, [43.6, 323.6, 602.1, 493.7]),
    "fig18": (19, [290.9, 73.0, 568.7, 241.8]),
    "fig19": (19, [45.6, 114.7, 272.4, 199.4]),
    "fig20": (19, [50.7, 498.1, 277.5, 629.6]),
    "fig21": (19, [308.8, 497.2, 535.6, 630.6]),
    "fig22": (21, [50.1, 441.9, 262.8, 561.4]),
    "fig23": (21, [285.9, 416.4, 555.1, 514.6]),
    "fig24": (23, [43.6, 72.0, 582.2, 257.9]),
    "fig25": (23, [43.6, 527.8, 582.2, 697.8]),
    # tables with a measured region
    "tab1": (8, [43.6, 91.5, 563.6, 569.0]),
    "tab4": (9, [122.4, 279.2, 472.9, 509.4]),
    "tab5": (16, [126.1, 656.1, 469.2, 714.3]),
    "tab6": (18, [123.5, 93.1, 471.8, 311.8]),
    "tab8": (24, [48.6, 206.5, 546.7, 290.5]),
    # excluded regions
    "summary": (1, [70.9, 72.0, 524.4, 157.0]),
    "code1": (27, [40.3, 274.8, 558.2, 768.3]),
    "code2": (34, [40.3, 75.6, 558.4, 548.6]),
}

for _name, (_p, _b) in B.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B), f"{len(MEASURED)} measured regions, {len(B)} mapped"


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (PAGE_W * PAGE_H)
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


def caption(v: str, *, numbering: str = "Figure N:", pos: str = "below",
            units: bool = False, vars_: int = 0, cond: bool = False,
            concl: bool = False, voice: str = "none") -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": units,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": cond,
        "concludes": concl,
        "voice": voice,
        "position": pos,
    }


def mention(page: int, *, first: int | None, style: list[str], lead: str = "",
            pattern: str, trail: str = "", read: int = 0) -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": 1 if first else 0,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def figure(key: str, fam: str, cap: dict, men: dict, geo: dict, *, path: list[str],
           kind: str, source: str = "text-layer", note: str = "",
           other_note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "other_note": other_note,
        "family": fam,
        "confidence": geo["confidence"],
        "panel_count": geo["panel_count"],
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": cap,
        "geometry": {"family": fam, **geo},
    }


def table(key: str, cap: dict, men: dict, grid: dict, *, path: list[str], kind: str,
          note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def geo(*, panels: int = 1, layout: str = "single", shared: bool = False,
        legend: str = "none", colorbar: bool = False, three_d: str = "no",
        axes: str = "no axes", numbers: bool = False, labels: bool = False) -> dict:
    return {
        "panel_count": panels,
        "panel_layout": layout,
        "shared_axes": shared,
        "legend": legend,
        "colorbar": colorbar,
        "three_d": three_d,
        "printed_numbers": numbers,
        "data_labels": labels,
        "axes": axes,
        "confidence": "high",
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "booktabs",
         zebra: bool = False, merged: bool = False, diag: bool = False,
         units: bool = False, decimal: bool = False, numeric: int = 0, txt: int = 0,
         width: str = "full", note_sentence: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rules,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diag,
        "units_in_header": units,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": False,
        "note_sentence": note_sentence,
    }


# ---- text-layer quotes -------------------------------------------------------

Q_FIG = {
    1: "Figure 1: Hierarchy Figure",
    2: "Figure 2: Word cloud: the ﬁgure shows equality is the most concerned factor.",
    3: "Figure 3: Selection Criteria",
    4: "Figure 4: Random sample: distribution of annual income",
    5: "Figure 5: Population Zero: distribution of annual income",
    6: "Figure 6: Random sample: distribution of weekly working hour",
    7: "Figure 7: Population Zero: distribution of weekly working hour",
    8: "Figure 8: Random sample: distribution of educational level",
    9: "Figure 9: Population Zero: distribution of educational level",
    10: "Figure 10: Random sample: distribution of age",
    11: "Figure 11: Population Zero: distribution of age",
    12: "Figure 12: Database structure, algorithm and a sample result of the model."
        "(a)population of certain kind of people each year(AL=alive,D=dead,AD=adult,M=male,"
        "F=female,W=people whose income under minimal wage); (b)sex ratio of male/female each "
        "year; (c)rate of unemployment(un), rehire(reh) and retire(ret) each year; (d)population "
        "of newly born children each year; (e)Gross Domestic Product(GDP) and Net Domestic "
        "Product(NDP) each year; (f)GDP per capita each year; (g)histogram of age distribution "
        "of Population Zero(start) and population after 100 years(end); (h) Average happiness "
        "index each year",
    13: "Figure 13: Family Network:The red bidirectional arrows represent marriages and the grey "
        "directional arrows show the parenthood.",
    14: "Figure 14: Marriage ratio increases in the ﬁrst 60 years and moves to a stabilization.",
    15: "Figure 15: The NDP-minimum wage curve from the 7th to 10th year of evolution",
    16: "Figure 16: Class Transition Of Family Class",
    17: "Figure 17: The 3 axes show the data of standard deviation, minimum wage and average "
        "family income respectively.",
    18: "Figure 18: Families of Class A,B,C,D,E have equal chance to transit to parental leave",
    19: "Figure 19: Average income, and standard deviation and minimum wage change by parental "
        "leave pay.",
    20: "Figure 20: Happiness across age",
    21: "Figure 21: Happiness across education",
    22: "Figure 22: 24-people linkage graph",
    23: "Figure 23: Age distribution: The proportion of different age groups has ”pulse”, "
        "because children under 16 are not included in Population Zero. There is a 16-year age "
        "gap between the ﬁrst generation of Mars-born babies and the youngest immigrants of "
        "Population Zero.",
    24: "Figure 24: Results of different migrantional plan.(a)Population diagram of Population "
        "Zero with ten thousands migrants in year 10, 20, 30, 40 and 50; (b)GDP diagram of "
        "UTOPIA:2100 in year 10, 20, 30, 40 and 50;(c) Age distribution in year 50 of "
        "UTOPIA:2100 in comparison with no migration",
    25: "Figure 25: Results of option 1 and option 2 to move 50000 migrants to UTOPIA:2100."
        "(a)Population",
}
# Ten captions come back split across the two columns they sit under, so the printed sentence is
# typed from the crop and the row note carries the text-layer form that failed the check.
TYPED = {4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15}

Q_TAB = {
    1: "Table 1: Parameter List",
    2: "Table 2: Comparison matrix of happiness hierarchy I-II",
    3: "Table 3: Criteria weights of hierarchy I-II",
    4: "Table 4: Criteria weights of hierarchy II-III",
    5: "Table 5: Distribution Of Annual Family Income (Wmin is the minimum wage)",
    6: "Table 6: Calculation Of nk",
    7: "Table 7: Added Parameters",
    8: "Table 8: Result for robustness analysis at 1% random noise of initial value (mean and "
       "stardard value at year 50 of 30 independent runs); IP for initial population, MW for "
       "minimal wage, PLP for parental leave pay.Unbiased parameters: IP=10000; MW=5000; "
       "PLP=40000; Other parameters: retire age is 65; rate of natural unemployment is 5%; "
       "no migration from earth after year 0",
}

# ---- section paths -----------------------------------------------------------

S_32 = H("3", "3.2")
S_34 = H("3", "3.4")
S_42 = H("4", "4.2")
S_431 = H("4", "4.3", "4.3.1")
S_51 = H("5", "5.1")
S_55 = H("5", "5.5")
S_62 = H("6", "6.2")
S_63 = H("6", "6.3")
S_71 = H("7", "7.1")
S_81 = H("8", "8.1")
S_82 = H("8", "8.2")
S_91 = H("9", "9.1")
S_92 = H("9", "9.2")
S_10 = H("10")

# ---- figures -----------------------------------------------------------------

FIG: dict[int, dict] = {}

FIG[1] = figure(
    "fig1", "node-link-network", caption(Q_FIG[1]),
    mention(6, first=5, style=["Fig.1"], pattern="as-shown-in",
            lead="The Fig.1 below illustrates a clear structure",
            trail="To simplify the 3-tier basic parameter, we design a comprehensive index "
                  "system", read=1),
    geo(layout="three text columns (Tiers / Parameters / Factors), connectors between them",
        axes="none - column headers Tiers, Parameters, Factors"),
    path=S_32, kind="model",
    note="a three-tier hierarchy drawn in Word, printed at the top of p6 with the section 3.3 "
         "heading starting under its caption. The drawing still carries the artefact of that "
         "process: eleven blue text-selection highlight boxes are parked over the parameter "
         "labels ('Personal Sa|vings Rate', 'Real Pe|rsonal Income', 'Mini|mum Wage'), and two "
         "coloured dots sit beside 'Income' and 'GDP or Happiness' and key nothing. Connector "
         "lines run through the label column and attach mid-word")

FIG[2] = figure(
    "fig2", "other", caption(Q_FIG[2]),
    mention(7, first=7, style=["Fig.2"], pattern="as-shown-in",
            lead="To better visualize the most concerned factors, we generated a word cloud as "
                 "shown in Fig.2."),
    geo(layout="one cloud, words set at arbitrary angles and four typefaces",
        axes="none - no scale, no counts, no corpus size"),
    path=S_34, kind="evaluation",
    other_note="a word cloud: a type-setting of term frequencies with no axis, no legend and no "
               "quantitative encoding, so it belongs to no plot family",
    note="a word-cloud generator export, printed alone under section 3.4 and cited once, in the "
         "sentence that explains it. The claim it makes - that equality is the most concerned "
         "factor - is carried by relative type size, which is not measured anywhere in the paper")

FIG[3] = figure(
    "fig3", "flowchart-or-schematic", caption(Q_FIG[3]),
    mention(10, first=10, style=["Fig.3"], pattern="as-shown-in",
            lead="The classiﬁcation procedure and the numbers of each type are speciﬁed in Fig.3.",
            trail="We deﬁne innovators as individual under 40 and own bachelor degrees or "
                  "higher.", read=1),
    geo(layout="one tree: candidate pool, then two branches, then four, then eight leaves",
        axes="none", numbers=True, labels=True),
    path=S_42, kind="solution",
    note="the selection tree, drawn on a grey editor grid that is part of the pasted image - the "
         "grid is visible behind every box - with a yellow highlight behind the root node and "
         "eight count boxes tinted at the leaves (3150, 3150, 350, 350, 1350, 1350, 150, 150). "
         "Those eight numbers are the only quantitative content of the figure and they are "
         "printed nowhere else")

FIG[4] = figure(
    "fig4", "histogram", caption(Q_FIG[4]),
    mention(11, first=10, style=["Fig.4"], pattern="as-shown-in",
            lead="As is show in Fig.4 and Fig.5, Population Zero has a higher average annual "
                 "income and a lower standard deviation of 46844.11 dollars"),
    geo(layout="one panel, top-left of a 4x2 block", axes="density against PINCP"),
    path=S_431, kind="result", source="typed-from-crop",
    note="the 'random sample' half of the annual-income pair. The text layer prints the two "
         "captions of the pair split across the columns they sit under - 'Figure 4: Random "
         "sample: distribution of annual' then 'Figure 5: ...' then the words 'income income' - "
         "so the printed sentence is typed from the crop. Y ticks print as 0.0e+00 to 1.5e-05 at "
         "about 4 pt and are unreadable at print size")

FIG[5] = figure(
    "fig5", "histogram", caption(Q_FIG[5]),
    mention(11, first=10, style=["Fig.5"], pattern="as-shown-in",
            lead="As is show in Fig.4 and Fig.5, Population Zero has a higher average annual "
                 "income and a lower standard deviation of 46844.11 dollars"),
    geo(layout="one panel, top-right of the same 4x2 block", axes="density against PINCP"),
    path=S_431, kind="result", source="typed-from-crop",
    note="the 'Population Zero' half of the annual-income pair, same panel shape and same y "
         "limits as Figure 4, with no visual encoding that distinguishes the two populations - "
         "only the caption says which is which")

FIG[6] = figure(
    "fig6", "histogram", caption(Q_FIG[6]),
    mention(11, first=10, style=["Fig.6"], pattern="as-shown-in",
            lead="From Fig.6 and Fig.7, we can not tell a huge difference between the random "
                 "sample and Population Zero."),
    geo(layout="one panel, second row left", axes="density against WKHP"),
    path=S_431, kind="result", source="typed-from-crop",
    note="weekly working hours for the random sample; the tallest spike sits at about 40 hours "
         "and the rest of the panel is an empty tail, which is the point the prose draws from "
         "the pair: working hours do not separate the two populations")

FIG[7] = figure(
    "fig7", "histogram", caption(Q_FIG[7]),
    mention(11, first=10, style=["Fig.7"], pattern="as-shown-in",
            lead="From Fig.6 and Fig.7, we can not tell a huge difference between the random "
                 "sample and Population Zero."),
    geo(layout="one panel, second row right", axes="density against WKHP"),
    path=S_431, kind="result", source="typed-from-crop",
    note="weekly working hours for Population Zero, drawn to the same shape as Figure 6")

FIG[8] = figure(
    "fig8", "histogram", caption(Q_FIG[8]),
    mention(11, first=10, style=["Fig.8"], pattern="as-shown-in",
            lead="Population Zero have a higher average education level(shown in Fig.8 and "
                 "Fig.9), since we have a strong preference for innovators"),
    geo(layout="one panel, third row left", axes="density against the education variable"),
    path=S_431, kind="result", source="typed-from-crop",
    note="education level for the random sample. The printed caption breaks the word 'educational' "
         "across a line ('educa- / tional'), which is a second reason the text layer cannot "
         "supply it")

FIG[9] = figure(
    "fig9", "histogram", caption(Q_FIG[9]),
    mention(11, first=10, style=["Fig.9"], pattern="as-shown-in",
            lead="Population Zero have a higher average education level(shown in Fig.8 and "
                 "Fig.9), since we have a strong preference for innovators"),
    geo(layout="one panel, third row right", axes="density against the education variable"),
    path=S_431, kind="result", source="typed-from-crop",
    note="education level for Population Zero, the higher-average half of the pair")

FIG[10] = figure(
    "fig10", "histogram", caption(Q_FIG[10]),
    mention(11, first=None, style=[], pattern="none",
            trail="In terms of age distribution, we believe a younger group have a stronger "
                  "ability to innovate", read=1),
    geo(layout="one panel, fourth row left", axes="density against AGEP"),
    path=S_431, kind="result", source="typed-from-crop",
    note="age distribution for the random sample. Never cited by number: the prose discusses the "
         "pair in the sentence that opens p11 without naming Figure 10 or Figure 11, so both "
         "rows carry a null first page and an empty style list")

FIG[11] = figure(
    "fig11", "histogram", caption(Q_FIG[11]),
    mention(11, first=None, style=[], pattern="none",
            trail="In terms of age distribution, we believe a younger group have a stronger "
                  "ability to innovate", read=1),
    geo(layout="one panel, fourth row right", axes="density against AGEP"),
    path=S_431, kind="result", source="typed-from-crop",
    note="age distribution for Population Zero, the only pair whose two panels do not share "
         "their y range (0.02 against 0.04), which is what lets the reader see the age advantage "
         "the prose claims")

FIG[12] = figure(
    "fig12", "composite-panel", caption(Q_FIG[12]),
    mention(13, first=12, style=["Fig.12"], pattern="as-shown-in",
            lead="Here we present the general algorithm and a sample result of one-hundred-year "
                 "evolution shown in Fig.12."),
    geo(panels=8, layout="eight lettered plots (a)-(h) in two columns, flanked left by a "
         "database table and in the middle by a flowchart",
        legend="inside", axes="each panel titled (Year or Age against population, ratio, GDP)"),
    path=S_51, kind="result",
    note="one printed frame that carries three different things: a captured spreadsheet of the "
         "person records at left, a flowchart of the model in the middle, and the eight lettered "
         "result plots at right. Counted as one composite exhibit of eight panels. The caption "
         "runs thirteen lines under it and enumerates (a) to (h), so the panel count is checked "
         "against the caption and not against the count of boxes. The spreadsheet's own footnote "
         "'*: Corresponding data of Population Zero can be found in PUMS database.' is stranded "
         "inside the figure frame")

FIG[13] = figure(
    "fig13", "node-link-network", caption(Q_FIG[13]),
    mention(15, first=14, style=["Fig.13"], pattern="parenthetical",
            lead="To have a clear view of marriage and parenthood relationship among citizens",
            trail="Apparently, marriage linkages are far more sparse than parent hood linkages.",
            read=1),
    geo(layout="40 numbered nodes, grey edges, red bidirectional arrows drawn over them",
        axes="none"),
    path=S_55, kind="model", source="typed-from-crop",
    note="the family network of 40 citizens. Node numbers only - no node symbols - with the "
         "marriage arrows added afterwards in a heavier red stroke that lands on top of the "
         "numbers, so several citizen IDs are unreadable. The caption's 'grey directional "
         "arrows' carry no visible arrowheads")

FIG[14] = figure(
    "fig14", "line", caption(Q_FIG[14]),
    mention(15, first=None, style=[], pattern="none"),
    geo(axes="Marriage Ratio against Year"),
    path=S_55, kind="result", source="typed-from-crop",
    note="marriage ratio against year, one series, no markers, printed beside Figure 13. Never "
         "cited anywhere in the paper by number or by deixis: the only prose about it is its own "
         "caption")

FIG[15] = figure(
    "fig15", "line", caption(Q_FIG[15]),
    mention(17, first=16, style=["Fig.15"], pattern="as-shown-in",
            lead="We input different value of minimum wages and ﬁnd that it is negatively "
                 "correlative with the Net Domestic Product, as is shown in Fig.15"),
    geo(layout="one plot with four series, one per year of the run", legend="above",
        axes="Net Domestic Product on the x axis; the y axis prints bare ticks and no title"),
    path=S_62, kind="result", source="typed-from-crop",
    note="four curves, one per evolution year, printed beside Figure 16. Three defects visible "
         "in print: the y axis has no title - a small 'wage' text box is clipped against the "
         "right end of the x axis - a leftover series name 'net_domestic_product' sits inside "
         "the plot area above the axis title, and the x axis starts at 10,000 with no break mark")

FIG[16] = figure(
    "fig16", "flowchart-or-schematic", caption(Q_FIG[16]),
    mention(17, first=None, style=[], pattern="none"),
    geo(layout="five class nodes on a grey baseline with transition arrows between neighbours",
        axes="none"),
    path=S_62, kind="model",
    note="the class-transition diagram. Never cited by number, and the one place the paper "
         "mis-references an exhibit: p16 says 'the class transition chart Table 5:' but Table 5 "
         "is the income-distribution grid on the same page and this chart is Figure 16. The "
         "lambda and mu labels are pasted text boxes, the mu-1 label floats off its arrow, and "
         "no arrowhead survives, so the direction of every transition is a guess from the "
         "caption")

FIG[17] = figure(
    "fig17", "surface-or-3D", caption(Q_FIG[17]),
    mention(18, first=17, style=["Fig.17"], pattern="figure-n-shows",
            lead="Using a controlled elitist genetic algorithm[14], we ﬁnd out the optimal "
                 "solution, Fig.17 gives detailed information about all the feasible solutions "
                 "after 50 iterations."),
    geo(panels=3, layout="three unlettered 3-D panels side by side", three_d="perspective-bars",
        axes="standard deviation of income, minimum wage, average family income"),
    path=S_62, kind="result",
    note="the Pareto front drawn three times, one axis pair per panel, unlettered so the text "
         "cannot refer to a single panel. The measured box overruns the right page edge by 7 pt "
         "(602.1 against a 595.28 pt page) but the artwork does not: the overrun comes from the "
         "uneven panel widths, not from clipped content")

FIG[18] = figure(
    "fig18", "node-link-network", caption(Q_FIG[18]),
    mention(19, first=17, style=["Fig.18"], pattern="as-shown-in",
            lead="The State Transition Chart should be altered, as is shown in Fig.18."),
    geo(layout="six nodes A-E plus P, joined by labelled lambda/mu transition arcs",
        axes="none"),
    path=S_63, kind="model",
    note="the amended state diagram: the five income classes plus class P for families on parental "
         "leave, drawn in a shape tool with gradient-filled nodes, pasted mu/lambda text boxes and "
         "two stray lowercase 'p' boxes overlapping the arcs near C. Cited two pages before it "
         "prints, from section 6.2, while the figure sits under 6.3")

FIG[19] = figure(
    "fig19", "line", caption(Q_FIG[19]),
    mention(19, first=18, style=["Fig.19"], pattern="as-shown-in",
            lead="The result is presented in Fig.19.",
            trail="Parental leave pay doesn’t affect average family income much.", read=1),
    geo(layout="one plot carrying average income, standard deviation and minimum wage",
        legend="inside", axes="Dollars against Parental leave pay ($)"),
    path=S_63, kind="result",
    note="three outcomes against parental leave pay, the figure the paper's own bullet list then "
         "reads out. The boxed key names Average income, Standard deviation and Minimum income, "
         "and the exponent annotations are broken in two different ways in the one chart - "
         "'x 10^000' on the y axis and 'x 10000' at the right end of the x axis")

FIG[20] = figure(
    "fig20", "line", caption(Q_FIG[20]),
    mention(19, first=19, style=["Fig20"], pattern="figure-n-shows",
            lead="Fig20 shows that young people and old people are slight happier than middle "
                 "age people."),
    geo(axes="Happiness against Age"),
    path=S_71, kind="result",
    note="happiness across age bands with markers, the left half of the pair that ends p19. A "
         "spreadsheet default export: the plot carries an in-plot title that repeats its caption, "
         "its y ticks mix '1' with 0.95 / 0.9 / 0.85, and an unlabelled dotted orange reference "
         "line crosses it")

FIG[21] = figure(
    "fig21", "line", caption(Q_FIG[21]),
    mention(19, first=19, style=["Fig21"], pattern="figure-n-shows",
            lead="Fig21 shows that people with education level like a regular high school "
                 "diploma are less happier."),
    geo(axes="Happiness against SCHL"),
    path=S_71, kind="result",
    note="happiness across education levels with markers, the right half of the pair. Its y tick "
         "labels mix a decimal comma with a point ('1,200' above '1.000'), so the top tick reads "
         "as one thousand two hundred, and its x axis prints the raw variable code SCHL where the "
         "caption says education")

FIG[22] = figure(
    "fig22", "node-link-network", caption(Q_FIG[22]),
    mention(21, first=21, style=["Fig.22"], pattern="figure-n-shows",
            lead="Fig.22 shows the connection of individual with ID number 1 to 24 in the 10th "
                 "year of evolution."),
    geo(layout="24 nodes on a ring, numbered 1 to 24, thin edges across the circle",
        axes="none", numbers=True),
    path=S_81, kind="model",
    note="the interpersonal network laid out on a circle, pasted with its own cream background "
         "rectangle, which is what separates it from Figure 23 beside it")

FIG[23] = figure(
    "fig23", "histogram", caption(Q_FIG[23]),
    mention(21, first=22, style=["Fig.23"], pattern="as-shown-in",
            lead="This result in a discontinuous age distribution in Fig.23."),
    geo(axes="proportion against age, 0 to 100"),
    path=S_82, kind="result",
    note="age distribution with the two decade gaps the caption explains. The paper cites it on "
         "p22, a page after it prints, so its lead is negative; it also prints before the "
         "section 8.2 heading that discusses it")

FIG[24] = figure(
    "fig24", "composite-panel", caption(Q_FIG[24]),
    mention(23, first=22, style=["Fig.24"],
            pattern="as-shown-in",
            lead="The reason is that those immigrants arriving at year 10 and 30 ﬁlling the "
                 "blank of the age gap of Population Zero"),
    geo(panels=3, layout="three lettered panels (a)-(c) side by side", legend="inside",
        axes="year against population, GDP and age distribution"),
    path=S_91, kind="result",
    note="the migration-year comparison, three panels lettered in the caption and nowhere on the "
         "artwork, each with its own boxed key ('none' then 10/20/30/40/50). Panel (b)'s axis "
         "title prints 'GPD($)' for GDP, and panel (c)'s histogram is binned fine enough to read "
         "as hairline spikes rather than bars. Cited on p22 inside a sentence the text layer "
         "breaks with a hyphen, so the quoted lead is the contiguous part of it")

FIG[25] = figure(
    "fig25", "composite-panel", caption(Q_FIG[25]),
    mention(23, first=23, style=["Fig.25"], pattern="as-shown-in",
            lead="Using the evolution model, we ﬁnd that option 1 is much better than option2 "
                 "both on population and GDP in two hundred year range(Fig.25)."),
    geo(panels=3, layout="three lettered panels (a)-(c) side by side", legend="inside",
        axes="year against population, GDP and GDP per person"),
    path=S_92, kind="result",
    note="option 1 against option 2, keyed 'opt1' solid and 'opt2' dashed in every panel. Panel "
         "(c)'s y axis starts at 3 while (a) and (b) start at zero, so the three panels do not "
         "share a baseline, and (b) repeats the 'GPD($)' misspelling. Its caption prints "
         "'(a)Population dia- gram;(b)GDP diagram;(c) GDP per person diagram', so the verbatim "
         "quote stops before the hyphen and the remainder is described here")

FIGURES = [FIG[n] for n in sorted(FIG)]

# ---- tables ------------------------------------------------------------------

TABLES = [
    table("tab1", caption(Q_TAB[1], numbering="Table N:", pos="above"),
          mention(8, first=5, style=["Tab.1"], pattern="as-shown-in",
                  lead="The Fig.1 below illustrates a clear structure"),
          grid(33, 7, header=1, rules="booktabs", numeric=0, txt=7),
          path=S_34, kind="model",
          note="the parameter frame: Name, Symbol, Type, Tier, Factor, Dict[6] and Unit, one "
               "header row and 32 body rows down to Weekly Working Hours. The unit is not folded "
               "into the header - a dedicated Unit column carries $, Year, Person and Hour. The "
               "grid reads cleanly end to end - no value sits under a wrong header, and the code "
               "heading prints as the odd token 'Dict[6]' - with two wobbles in the raster: it is "
               "announced three pages before it prints, on p5 inside the Fig.1 sentence, and "
               "floats to the top of p8; the "
               "'Dict[6]' heading prints noticeably left of the column of codes under it (AGEP, "
               "FINCP, SCHL, ACN1P, NPF, FES, SEX, MAR, OCCP, PINCP, WKHP), and one Type cell "
               "prints 'Interger'"),
    table("tab4", caption(Q_TAB[4], numbering="Table N:", pos="above"),
          mention(9, first=8, style=["Tab.4"], pattern="as-shown-in",
                  lead="Finally, all the weights are shown in Tab.3 and Tab.4."),
          grid(16, 4, header=1, rules="booktabs", decimal=True, numeric=2, txt=2),
          path=S_34, kind="model",
          note="the second weight table, fifteen parameters against GDP, Happiness and the tier "
               "they belong to. Its Tier column repeats a label on every row (Income eight "
               "times, Education twice, Equality five) rather than merging the runs, and every "
               "value is padded to three decimals so the column aligns on the point. The two "
               "tables above it on the same page - Tables 2 and 3 - print with no measured "
               "region"),
    table("tab5", caption(Q_TAB[5], numbering="Table N:", pos="above", vars_=1),
          mention(16, first=16, style=["Table 5"], pattern="direct",
                  lead="Each year families move among the 5 classes with certain probability, "
                       "the class transition chart"),
          grid(4, 6, header=1, rules="vertical-rules", numeric=5, txt=1),
          path=S_62, kind="model",
          note="the class income ladder: Class, then A to E, with an Income($) row, a Proportion "
               "row and a Cumulative Proportion row. One stub vertical rule between the label "
               "column and the data, closed by three horizontal rules and no outer frame. The "
               "unit lives in the stub ('Income($)'), not in the header, and the caption carries "
               "the symbol definition '(Wmin is the minimum wage)'. Its citation is the one "
               "mis-reference in the paper: the prose calls the class transition chart 'Table 5' "
               "and then this grid prints under that name"),
    table("tab6", caption(Q_TAB[6], numbering="Table N:", pos="above"),
          mention(18, first=17, style=["Tab.6"], pattern="as-shown-in",
                  lead="The calculation of nk is also speciﬁed in Tab.6"),
          grid(15, 2, header=1, rules="vertical-rules", txt=2),
          path=S_62, kind="model",
          note="five unlabelled blocks of three rows (Class, Income($), Adjusted Proportion), one "
               "per class A to E, with the formula for that class's share in the value column. No "
               "header row at all, so header_rows counts the leading 'Class | A' row and the row "
               "note says so. Class E's formula prints 'n5 = 10% + 25%4 - 10%mu1' with the lambda "
               "in front of the 4 dropped, compared with the four blocks above it. The caption "
               "shares its baseline with the stub header cell in the text layer, which prints the "
               "token 'Class' before the caption line"),
    table("tab8", caption(Q_TAB[8], numbering="Table N:", pos="above"),
          mention(24, first=24, style=["Tab.8"], pattern="as-shown-in",
                  lead="Results are shown in the Tab.8."),
          grid(6, 11, header=2, rules="booktabs", merged=True, numeric=10, txt=1),
          path=S_10, kind="test",
          note="the robustness grid: three noise rows (IP, MW, PLP) plus an unbiased row, against "
               "five outcome pairs, each outcome name merged over its mean and std column and the "
               "stub '1% noise' merged over both header rows. The only two-header table in the "
               "paper and the only one with merged cells. Every cell is centred, so the columns "
               "are not decimal-aligned, and each magnitude is written inside its cell as "
               "'m * 10^n' rather than in a shared exponent header. The caption line is the "
               "table's own note, naming every parameter and its baseline value, and it prints "
               "'pay.Unbiased' with no space after the stop"),
]

# ---- exclusions --------------------------------------------------------------

EXCLUDED = []
for _key, _reason, _note in [
    ("summary", "not-an-exhibit",
     "the ICM summary-sheet control block: Team Control Number 64486, Problem Chosen F, and the "
     "T1-T4 / F1-F4 office-use boxes. A printed form, cited by nothing, on a page that carries "
     "the paper's abstract underneath it"),
    ("code1", "not-an-exhibit",
     "the first slab of the appendix MATLAB listing (A.1 MATLAB Script Of Evolution Model). The "
     "detector returns the code block as a region because every glyph run measures like a table "
     "cell; it is a program, it captions nothing and nothing cites it"),
    ("code2", "not-an-exhibit",
     "the last slab of the same MATLAB listing on the final page. Same case as the p27 slab, and "
     "the interior pages of the listing (p28 to p33) return no region at all although they print "
     "the same 291 glyph paths per page"),
]:
    _p, _b = B[_key]
    EXCLUDED.append({"page": _p, "bbox": _b, "reason": _reason, "note": _note})

# ---- payload -----------------------------------------------------------------

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": [
        "Distribution plots carry this paper: nine of the twenty-five figures are histograms, the "
        "eight-panel block of Figures 4-11 plus the age distribution of Figure 23 "
        "[geometry.family].",
        "Seven figures are drawings rather than plots: four node-link diagrams (Figures 1, 13, 18 "
        "and 22), two schematics (Figures 3 and 16) and the word cloud of Figure 2, and the rest "
        "of the line and histogram exhibits are tool defaults [geometry.family].",
        "Only four of the twenty-five figures carry more than one panel - Figure 12 with eight, "
        "Figures 17, 24 and 25 with three each - while the ten plots printed as five facing pairs "
        "on pp11, 15, 17 and 19 stay separate single-panel exhibits [geometry.panel_count].",
        "Five figures print a legend at all and four of them put it inside the frame (Figure 12 "
        "keys its series per panel, Figures 19, 24 and 25 carry a bordered key in the top right); "
        "only Figure 15 puts its key above the plot area, and the eight-panel distribution block, "
        "which needs a key most, prints none [geometry.legend].",
        "Exactly one exhibit is three-dimensional - Figure 17, three perspective panels of stems "
        "over a floor plane - and no other figure in the paper carries a third axis "
        "[geometry.three_d].",
        "No figure prints a colourbar and no encoding in the paper uses a colour scale; every "
        "colour in the exhibits comes from a pasted background, a shape fill or a series line "
        "[geometry.colorbar].",
        "Caption side is uniform and splits by exhibit type: all twenty-five figure captions "
        "print below their artwork and all five recorded table captions print above their grid, "
        "with no exception in the paper [caption.position].",
        "One numbering form covers every exhibit - 'Figure N:' for the figures and 'Table N:' for "
        "the tables, number then colon then space - and no other spelling appears anywhere "
        "[caption.numbering].",
        "Caption length is decided by caption type, not by exhibit size: fourteen are short labels "
        "of four to nine words ('Figure 1: Hierarchy Figure', 'Figure 7: Population Zero: "
        "distribution of weekly working hour'), six are sentence captions of 13 to 18 words that "
        "state a finding, and the four composite exhibits run 16 to 83 words because each panel "
        "has to be named [caption.words].",
        "Twenty-four captions are a single sentence; the exception is Figure 23 at two sentences, "
        "and it is also the only caption that explains why the picture looks the way it does "
        "[caption.sentences].",
        "Only one caption defines a symbol - 'Table 5: Distribution Of Annual Family Income "
        "(Wmin is the minimum wage)' - and it is the paper's only caption-level variable "
        "definition; the other four recorded tables leave their symbols to the body text "
        "[caption.variables].",
        "Twenty-one of the twenty-five figures are cited by number; the four that are not are "
        "Figures 10 and 11, discussed in a sentence that never names them, and Figures 14 and 16, "
        "discussed nowhere at all [mention.count].",
        "The lead is normally one page: thirteen figures and two tables are announced the page "
        "before they print, six print on the page that announces them, Figure 18 is announced two "
        "pages early, Table 1 is announced three pages early, and Figure 23 is cited a page after "
        "it prints - the paper's only negative lead [mention.lead_pages].",
        "Citation spellings group by chapter rather than by author: 'Fig.1' to 'Fig.12' carry a "
        "stop, 'Fig20' and 'Fig21' drop both the stop and the space, 'Fig.22' to 'Fig.25' restore "
        "them, and every table is cited as 'Tab.N' [mention.style].",
        "Four lead grammars: sixteen exhibits are announced with an as-shown-in construction, "
        "four with 'FigN shows that ...', one parenthetically ('... among citizens(Fig.13)'), and "
        "four have no lead sentence because the exhibit is never cited [mention.lead_pattern].",
        "Rule style follows the table's job, not the author's taste: booktabs for the parameter "
        "list and the two data grids (Tables 1, 4 and 8), and three horizontal rules plus a "
        "single stub vertical for the two class grids (Tables 5 and 6) [table.rule_style].",
        "Not one recorded table is shaded - no zebra striping and no tinted cell in any of the "
        "five - although the pasted spreadsheet capture inside Figure 12 does carry a grey header "
        "band [table.zebra].",
        "Only Table 8 merges cells: each outcome name spans its mean and std columns and the stub "
        "spans both header rows. Every other grid repeats its label on each row instead, which is "
        "why Table 4 prints its tier name fifteen times [table.merged_cells].",
        "Only one grid aligns its figures on a decimal point - Table 4, where every value is "
        "padded to three decimals. Table 1 has no free numeric column and Table 8's values are "
        "'m * 10^n' strings centred in their cells, so the paper has exactly one decimal-aligned "
        "table [table.decimal_aligned].",
        "One grid prints two header rows (Table 8) and one prints none at all, so Table 6's "
        "leading block-label row is counted as its header and the row note records the "
        "substitution [table.header_rows].",
        "Units are handled three different ways and no table repeats the choice: Table 1 gives "
        "them a dedicated Unit column, Table 5 writes them inside the stub ('Income($)'), and "
        "Table 8 writes a magnitude into every cell as 'm * 10^n' rather than stating one exponent "
        "in the header [table.units_in_header].",
        "Exhibits are reported from the section that states their numbers: seventeen figure rows "
        "and no table sit in a result kind, six figures and four tables in a model kind, and the "
        "only solution-kind and evaluation-kind exhibits are Figure 3 and Figure 2 "
        "[place.section_kind].",
        "Exhibit size tracks the shape of the data rather than its importance: the parameter "
        "table takes half a page (0.495) and the eight-panel composite 0.289, while the "
        "twenty-one single-panel exhibits run from 0.03 to 0.14 of a page, the plots that carry "
        "the paper's claims sitting at the bottom of that range and the Word hierarchy at the top "
        "[place.area_frac].",
        "Placement follows the page rather than the section: fourteen exhibits sit in the top "
        "third, nine in the middle and seven in the bottom third, and the bottom group is always "
        "the tail of a discussion - five of the seven are cited on the page they print on (Table 5 "
        "among them, closing p16) and two are the uncited panels of the p11 block - so a page-foot "
        "position marks the end of a section rather than a displaced float [place.page_zone].",
        "Three printed tables have no measured region and are declared gaps rather than patched: "
        "Tables 2 and 3 at the top of p9, whose boxes the detector does not return even though "
        "Table 4 at the foot of the same page does, and Table 7 on p20 [table.rows].",
        "Eleven captions are reconstructed rather than read, because the text layer interleaves "
        "each pair of side-by-side captions and frees their tails - p11's four pairs, p15's pair "
        "and p17's pair - so those rows carry typed-from-crop and the row note keeps the failed "
        "text-layer form [caption.verbatim].",
    ],
    "note": (
        "A 34-page Mars-colony paper - ten-parameter society model, AHP weights, a hundred-year "
        "agent simulation of 10000 migrants, an equilibrium search over minimum wage and parental "
        "leave, a migration-plan comparison - with 25 printed figures and 8 printed tables, and "
        "almost nothing drawn for print. Nine figures are histograms, three are composite panels "
        "and seven are drawings, and the tool provenance shows in every one: Figure 1 is a Word "
        "hierarchy still carrying eleven blue text-selection highlights, Figure 2 is a word-cloud "
        "export, Figures 4-11 are untuned plotting defaults whose y ticks print at about 4 pt, "
        "Figures 12/15/17/19-21/24-25 are spreadsheet and plotting exports, and Figures 13/16/18 "
        "are pasted shape diagrams, while Figure 3 still shows its editor grid. Caption side is "
        "uniform and mirrors the sibling paper one row up the queue in reverse: all 25 figure "
        "captions below, all table captions above. Eleven captions cannot be read from the text "
        "layer at all, because each pair of side-by-side captions prints interleaved across the "
        "two columns it sits under, so those rows are typed from the crop. Four figures are never "
        "cited by number (10 and 11 in a sentence that does not name them, 14 and 16 not even by "
        "deixis), Figure 23 is cited a page after it prints, and the paper mis-references one "
        "exhibit outright: p16 calls the class-transition chart Table 5, which is the "
        "income-distribution grid printed under that sentence. Three printed tables - Tables 2 and "
        "3 at the top of p9, Table 7 on p20 - return no measured region and are declared gaps, and "
        "three regions are not exhibits at all: the ICM summary-sheet control block on p1 and the "
        "two MATLAB code slabs of the appendix."
    ),
}


def main() -> int:
    from collections import Counter

    assert len(FIGURES) == 25 and len(TABLES) == 5 and len(EXCLUDED) == 3
    print("figures", len(FIGURES), "tables", len(TABLES), "excluded", len(EXCLUDED))
    for name, block in (("fig", FIGURES), ("tab", TABLES)):
        print(name, "kind", dict(Counter(e["place"]["section_kind"] for e in block)))
        for k in ("position", "numbering", "voice", "words", "sentences", "units",
                  "concludes"):
            print(" ", name, "cap." + k, dict(Counter(e["caption"][k] for e in block)))
        for k in ("first_page", "lead_pages", "count", "lead_pattern", "read_sentences"):
            print(" ", name, "men." + k, dict(Counter(e["mention"][k] for e in block)))
    for k in ("family", "panel_count", "legend", "colorbar", "three_d", "shared_axes"):
        print("geo." + k, dict(Counter(e["geometry"][k] for e in FIGURES)))
    for k in ("rows", "cols", "header_rows", "rule_style", "zebra", "merged_cells",
              "decimal_aligned", "width"):
        print("table." + k, dict(Counter(t["table"][k] for t in TABLES)))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in FIGURES + TABLES)))
    print("area", sorted(e["place"]["area_frac"] for e in FIGURES + TABLES))
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


for _n, _e in enumerate(sorted(FIGURES + TABLES, key=lambda x: (x["page"], x["bbox"][1],
                                                                x["bbox"][0])), 1):
    _e["place"]["doc_order"] = _n
_page_prev, _order = None, 0
for _e in sorted(FIGURES + TABLES, key=lambda x: (x["page"], x["bbox"][1], x["bbox"][0])):
    if _e["page"] != _page_prev:
        _page_prev, _order = _e["page"], 0
    _order += 1
    _e["place"]["page_order"] = _order


if __name__ == "__main__":
    raise SystemExit(main())
