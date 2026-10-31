"""Hand pass for P-F-2017-72197-93a3c66b (A Martian Utopia, Gov-Corp and Nordic welfare).

Shape of the paper: ten lettered sections A-J, nine body figures drawn in Excel, one Mathematica
plot, a landscape weighted-decision-matrix page, three Excel-dashboard screenshots in the
appendix, and five uncaptioned full-page reprints of the body charts as the last three pages.
35 pages, 22 measured regions.

What the record has to say out loud:

1. Two independent numbering runs. The body numbers its captions "Figure N." and runs 1 to 9;
   the appendix restarts at "Figure 1:" to "Figure 3:" and switches the punctuation from a
   period to a colon. A reader who trusts the printed numbers will collide the two runs.
2. The running text is offset by one from the printed captions from Figure 4 onward: p13 cites
   "Figure 5" for the caption "Figure 4", p17 cites "figure6 and 7" for the captions "Figure 5"
   and "Figure 6", p19 cites only "(see Figure)", and p21 cites "Figure 10" for the caption
   "Figure 9".
3. Every body caption prints below its artwork; every appendix screenshot caption prints above
   its capture - the side flips with the appendix, not with the exhibit type.
4. "Figure 7." is a bare number: the only caption in either run that names nothing at all.
5. p26 is the paper's only landscape page and the only grid. The region detector splits it into
   three bands; they are one table with a repeated header band.
6. pp33-35 carry no text layer at all: five uncaptioned plates that reprint body charts at full
   page width, so the appendix duplicates exhibits the body already numbered.

Usage: python -I tools/_dist_paper141.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-F-2017-72197-93a3c66b"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    "f1": (7, [154.8, 401.8, 457.2, 583.5]),
    "f2": (8, [154.8, 365.2, 457.2, 518.5]),
    "f3": (9, [154.8, 287.8, 457.2, 404.9]),
    "f4": (13, [154.8, 204.6, 457.2, 385.8]),
    "f5": (18, [154.8, 86.4, 457.2, 239.4]),
    "f6": (18, [154.8, 280.3, 457.2, 438.5]),
    "f7": (19, [154.8, 365.9, 457.2, 548.4]),
    "f8": (20, [154.8, 419.7, 457.2, 602.1]),
    "f9": (21, [154.8, 204.3, 457.2, 385.7]),
    "m1": (26, [114.1, 59.9, 326.1, 119.3]),
    "m2": (26, [114.1, 149.0, 326.1, 469.1]),
    "m3": (26, [114.1, 499.3, 326.1, 701.1]),
    "a1": (27, [71.5, 118.7, 540.5, 346.1]),
    "a2": (28, [107.4, 86.9, 534.9, 254.7]),
    "a3": (28, [108.0, 474.5, 532.3, 629.9]),
    "a4": (30, [148.3, 175.2, 407.7, 323.2]),
    "p33a": (33, [72.0, 72.0, 433.0, 289.0]),
    "p33b": (33, [72.0, 299.0, 434.4, 515.5]),
    "p34a": (34, [72.0, 72.0, 435.4, 289.0]),
    "p34b": (34, [72.0, 290.9, 434.4, 507.4]),
    "p35a": (35, [72.0, 72.0, 434.9, 289.0]),
}

EXCLUDED = {"p29 footnotes": (29, [72.0, 79.6, 532.2, 157.7])}

for _name, (_p, _b) in {**B, **EXCLUDED}.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 22, len(MEASURED)

SECTIONS = {
    "C": "C. POPULATION ZERO: DEMOGRAPHICS FOR SUSTAINABILITY",
    "D": "D. ADDRESSING INCOME INEQUALITY",
    "E": "E. EDUCATION: LIVING AND LEARNING ON MARS",
    "H": "H. IN THE LONG RUN: 100 YEAR VISION",
    "APPX": "Appendix – Discussion of Variables in the Equity/ Childcare Model",
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
         merged: bool = False, zebra: bool = False, decimal: bool = False,
         numeric: int = 0, txt: int = 0, width: str = "column",
         orientation: str = "portrait", note_sentence: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rules,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": False,
        "units_in_header": False,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": orientation,
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


C = [SECTIONS["C"]]
D = [SECTIONS["D"]]
E = [SECTIONS["E"]]
H = [SECTIONS["H"]]
APPX = [SECTIONS["APPX"]]

FIGURES = [
    figure("f1", "line", cap("Figure 1. Distribution of Human Capital within Human Capital",
                             "Figure N."),
           mention(7, first=7, style=["Figure 1"], pattern="as-shown-in",
                   lead="The resulting distribution was of human capital can be found in "
                        "Figure 1."),
           geo("line", numbers=True),
           path=C, kind="model",
           note="an Excel step chart of the human capital curve: in-plot title '2100 - "
                "Population Zero', y axis titled 'Human Capital Level', x axis with neither a "
                "title nor tick labels, gridlines on both axes and a thin frame. A rank-ordered "
                "curve printed as a staircase because human capital is accumulated in whole "
                "units. The caption repeats the word 'Human Capital' twice"),
    figure("f2", "bar", cap("Figure 2. Demographic Distribution of Population Zero", "Figure N."),
           mention(8, first=8, style=[], pattern="direct",
                   lead="This ﬁnal distribution is pictured below."),
           geo("bar", legend="outside-right", numbers=True),
           path=C, kind="model",
           note="thirteen vertical bars, one per five-year age group plus a 'More' bucket, in "
                "the same Excel template: in-plot title 'Population Zero', y 'Population', x "
                "'Age Group (5yrs)', and a single-chip legend 'Frequency' printed to the right "
                "of the plot frame"),
    figure("f3", "flowchart-or-schematic",
           cap("Figure 3. Income Distribution and Policy Implementation", "Figure N."),
           mention(9, first=9, style=[], pattern="direct",
                   lead="Such assumptions led us to create the model of GDP shown above:"),
           geo("flowchart-or-schematic", numbers=False, labels=True),
           path=D, kind="model",
           note="the paper's only drawn diagram: a wage curve against people with the axes "
                "labelled 'Wage' and 'People', cut into labelled regions - 'Not In Labor Force', "
                "'In Labor Force', 'Deficit' shaded red, 'Tax' shaded orange and 'GDP' shaded "
                "blue. Nothing is quantified, so printed_numbers is false and data_labels true"),
    figure("f4", "line", cap("Figure 4. Human Capital Distribution at 2110", "Figure N."),
           mention(13, first=13, style=["Figure 5"], pattern="as-shown-in",
                   lead="Running these distributions through the simulated Population Zero "
                        "through the year 2110, we found a distribution of human capital as "
                        "displayed in Figure 5."),
           geo("line", numbers=True),
           path=E, kind="model",
           note="the same Excel staircase as Figure 1 with the year as the in-plot title "
                "'2110'. Its caption says Figure 4 while the sentence above it promises "
                "Figure 5 - the first place the body's numbering and its citations part company"),
    figure("f5", "bar", cap("Figure 5. Age Distribution at 2150", "Figure N."),
           mention(18, first=17, style=["ﬁgure6 and 7"], pattern="as-shown-in",
                   lead="The resulting age distributions of 2150 and 2200 are shown below in "
                        "ﬁgure6 and 7."),
           geo("bar", legend="outside-right", numbers=True),
           path=H, kind="result",
           note="upper of two bar charts printed side by side at the top of p18, in the Figure "
                "2 template. In-plot title 'Age Distribution, +50 yrs' against a caption that "
                "says 2150, x 'Age Group (5yrs)' with labels rotated 45 degrees, single-chip "
                "legend 'Frequency' to the right. Age group 11 has a tick but no bar"),
    figure("f6", "bar", cap("Figure 6. Age Distribution at 2200", "Figure N."),
           mention(18, first=17, style=["ﬁgure6 and 7"], pattern="as-shown-in",
                   lead="The resulting age distributions of 2150 and 2200 are shown below in "
                        "ﬁgure6 and 7."),
           geo("bar", legend="outside-right", numbers=True),
           path=H, kind="result",
           note="lower of the p18 pair: same bars, same legend, in-plot title 'Age Distribution, "
                "+100 yrs'. Its x axis is titled 'Age Group, 5 yrs' - the comma replaces the "
                "bracketed form used in Figure 5, so the two halves of one pair do not even share "
                "an axis string. Age group 4 has a tick but no bar"),
    figure("f7", "line", cap("Figure 7.", "Figure N."),
           mention(19, first=19, style=["see Figure"], pattern="parenthetical",
                   lead="(see Figure), as signiﬁcantly more women quit their jobs"),
           geo("line", legend="below", numbers=True),
           path=H, kind="result",
           note="a three-series line chart with round markers - grey Total, orange Females, blue "
                "Males - titled in the plot 'Portion of Population to Exit Job for Childcare', "
                "with a legend printed inside the frame below the plot. The only caption in "
                "either numbering run that carries no description at all: the words are the "
                "number and a full stop, and the sentence that follows the caption is about "
                "poleis, not about the plot"),
    figure("f8", "line", cap("Figure 8. Average Societal Human Capital Over Time", "Figure N."),
           mention(20, first=None, style=[]),
           geo("line", numbers=True),
           path=H, kind="result",
           note="a single-series line, in-plot title 'Average Human Capital of Adult Population', "
                "y axis titled 'Human Capital level' in lower case where every other chart prints "
                "'Level', x 'Year' with ticks 2100 to 2200. Never cited in the running text"),
    figure("f9", "line", cap("Figure 9. Human Capital Distribution at 2200", "Figure N."),
           mention(21, first=21, style=["Figure 10"], pattern="as-shown-in",
                   lead="Another point of note is the increasing inequality of human capital as "
                        "the simulation continues as seen in Figure 10."),
           geo("line", numbers=True),
           path=H, kind="result",
           note="the same rank-ordered staircase as Figures 1 and 4, titled '2200'. The curve "
                "ends by climbing vertically into the top-right corner of the frame, so the last "
                "points are clipped by the plot box while the x axis runs on to about 11000 with "
                "no tick or label there. Cited as Figure 10"),
    figure("a1", "table-as-figure", cap("Figure 1: Sample Equity Model Dashboard:", "Figure N:",
                                        position="above"),
           mention(27, first=14, style=["Figure 1 of Appendix UL1"], pattern="as-shown-in",
                   lead="Sample ﬁndings can be seen in Figure 1 of Appendix UL1."),
           geo("table-as-figure", numbers=True, labels=True),
           path=APPX, kind="appendix",
           note="a pasted Excel worksheet, not a drawn figure: an INPUTS block of eleven named "
                "parameters and a RESULTS block headed 2100 to 2110 with four rows of ratios out "
                "of the workforce. Worksheet gridlines, grey header cells and colour-filled "
                "input cells are printed, plus empty cells extending right and below. A large "
                "solid black rectangle occludes the right-hand half of the dashboard. The "
                "caption's trailing colon promises content that the black block hides"),
    figure("a2", "table-as-figure",
           cap("Figure 2: Sample Individual Model Execution:", "Figure N:", position="above"),
           mention(28, first=None, style=[]),
           geo("table-as-figure", numbers=True, labels=True),
           path=APPX, kind="appendix",
           note="a second Excel capture: three named inputs (children 2, female salary 32000, "
                "male salary 43000), a Cost of Childcare comparison block and an output cell "
                "reading 'Exit? 0'. The only exhibits in the paper that print a decision rule in "
                "cells rather than in prose"),
    figure("a3", "table-as-figure",
           cap("Figure 3: Sample Aggregate Model Execution (partial):", "Figure N:",
               position="above"),
           mention(28, first=None, style=[]),
           geo("table-as-figure", numbers=True, labels=True),
           path=APPX, kind="appendix",
           note="the third Excel capture: the base of a Monte Carlo table with fifteen visible "
                "rows and fourteen columns, columns for rand, children, female and male salary, "
                "then three AVGS cells (0.1056, 0.0506, 0.055), exit and f-exit and m-exit "
                "indicators, with the next block headed YEAR 2101. The caption itself says the "
                "table is partial"),
    figure("a4", "line", NOCAP,
           mention(30, first=10, style=[], pattern="parenthetical",
                   lead="Curve of Actual wages, modeled wages, model-ﬁt analysis in appendix"),
           geo("line", numbers=True),
           path=APPX, kind="appendix", src="none",
           note="Mathematica notebook output rather than a chart made for the paper: the code "
                "cells that drew it print above the plot, and the plot itself is the wage curve "
                "with the 20000 minimum as a horizontal orange line and the shortfall filled pale "
                "blue. No axis titles, no legend, no caption; y ticks use a space as thousands "
                "separator"),
    figure("p33a", "line", NOCAP,
           mention(33, first=None, style=[]),
           geo("line", numbers=True),
           path=APPX, kind="appendix", src="none",
           note="one of five uncaptioned plates: a full-width reprint of the average-human-capital "
                "series already numbered Figure 8 in the body, here titled in the plot 'Average "
                "Human Capital of Adult Population' with both axes titled. Printed on a page with "
                "no text layer at all"),
    figure("p33b", "line", NOCAP,
           mention(33, first=None, style=[]),
           geo("line", numbers=True),
           path=APPX, kind="appendix", src="none",
           note="lower plate on p33: a reprint of Figure 1 ('2100 - Population Zero') with the "
                "same untitled x axis as the body original, printed at about four times the body "
                "size and still uncaptioned"),
    figure("p34a", "line", NOCAP,
           mention(34, first=None, style=[]),
           geo("line", numbers=True),
           path=APPX, kind="appendix", src="none",
           note="upper plate on p34: a reprint of Figure 4, in-plot title '2110', y 60 to 260, x "
                "ticks 1800 to 9800 with no x title - the same defects as the body version, "
                "scaled up"),
    figure("p34b", "line", NOCAP,
           mention(34, first=None, style=[]),
           geo("line", numbers=True),
           path=APPX, kind="appendix", src="none",
           note="lower plate on p34: the 2150 age distribution as a staircase, in-plot title "
                "'2150', y 60 to 360 and x with no tick labels at all - the only chart in the "
                "paper whose x axis is completely unlabelled"),
    figure("p35a", "line", NOCAP,
           mention(35, first=None, style=[]),
           geo("line", numbers=True),
           path=APPX, kind="appendix", src="none",
           note="the last plate: the 2200 distribution, in-plot title '2200', y 60 to 310, x "
                "ticks 1700 to 9700 with no title. These five plates carry more ink than any "
                "captioned exhibit in the paper and none of the paper's numbers"),
]

TABLES = [
    table("m1", cap("Weighted Decison Matrix Model", "none", position="below"),
          mention(26, first=12, style=[], pattern="direct",
                  lead="A full version of this matrix and model can be seen in the Appendices."),
          grid(3, 13, header=1, merged=True, zebra=False, numeric=11, txt=2,
               width="half", orientation="landscape"),
          path=APPX, kind="appendix",
          note="first of the three bands the region detector cut out of p26: the weight strip "
               "that heads the matrix, two data rows ('Short Run Valuation' and 'Long Run "
               "Valuation', both printed with their row labels sliced to 'ort Run Valuati' and "
               "'ng Run Valuatio') under a row of five value names and seven application names. "
               "This is the only landscape page in the paper, and the only grid of any kind"),
    table("m2", cap("Weighted Decison Matrix Model", "none", position="below"),
          mention(26, first=12, style=[], pattern="direct",
                  lead="A full version of this matrix and model can be seen in the Appendices."),
          grid(26, 13, header=1, merged=True, zebra=False, numeric=8, txt=5,
               width="half", orientation="landscape"),
          path=APPX, kind="appendix",
          note="the body of the same matrix: twenty-five academic disciplines, each scored 0 or 1 "
               "against five value columns and eight application columns, with the "
               "'Values / Applications' header band repeated above it. Cells carry drawn rules "
               "and coloured weight fills, so the shading is a scale on the values rather than "
               "row striping"),
    table("m3", cap("Weighted Decison Matrix Model", "none", position="below"),
          mention(26, first=12, style=[], pattern="direct",
                  lead="A full version of this matrix and model can be seen in the Appendices."),
          grid(26, 2, header=1, merged=False, zebra=False, decimal=False, numeric=2, txt=0,
               width="half", orientation="landscape"),
          path=APPX, kind="appendix",
          note="the tail of the same matrix, printed as a detached two-column block of short-run "
               "and long-run scores with a green-yellow-orange-red cell colour scale. It is where "
               "raw spreadsheet precision leaks into the paper - 0.316111, 0.389444, "
               "0.055555556 - and the title line 'Weighted Decison Matrix Model', misspelled, "
               "prints under it"),
]

EXCLUDED_REGIONS = [
    {"page": p, "bbox": b, "reason": "not-an-exhibit", "note": n}
    for n, (p, b) in (("p29 footnotes", EXCLUDED["p29 footnotes"]),)
]

RULES = [
    "Two independent numbering runs share one paper: the body captions run 'Figure 1.' to "
    "'Figure 9.' with a period, and the appendix restarts at 'Figure 1:' to 'Figure 3:' with a "
    "colon, so the same number names two different exhibits [caption.numbering].",
    "Every body caption prints below its artwork and all three appendix captions print above "
    "their capture, so caption side follows the part of the paper, not the kind of exhibit "
    "[caption.position].",
    "From Figure 4 onward the running text is one ahead of the printed captions: p13 cites "
    "'Figure 5' for the caption 'Figure 4', p17 cites 'figure6 and 7' for the captions 'Figure 5' "
    "and 'Figure 6', p19 cites only '(see Figure)', and p21 cites 'Figure 10' for the caption "
    "'Figure 9' [mention.style].",
    "One caption names nothing at all: 'Figure 7.' is a number and a full stop, printed under a "
    "three-series plot that the following sentence never describes [caption.words].",
    "Captions are short and nominal - 6 to 9 words in the body, 6 to 7 in the appendix, 4 for the "
    "matrix title - and not one names a unit, a variable or a condition, or states a conclusion "
    "[caption.units].",
    "Five uncaptioned plates sit on the three pages that carry no text layer at all (pp33-35), "
    "each reprinting a body chart at full page width, so the appendix duplicates Figures 1, 4, 5, "
    "6, 8 and 9 as plates that neither a caption nor a citation reaches [caption.verbatim].",
    "The only grid in the paper sits on the only landscape page, and it is printed as three "
    "stacked bands that the region detector measured separately; the 'Values / Applications' "
    "header band repeats above both the weight strip and the main grid [table.orientation].",
    "The matrix is drawn, not captured: cells are bounded by rules and filled with weight "
    "colours, there is no worksheet chrome, and the shading encodes the value rather than "
    "alternating rows [table.zebra].",
    "Only the matrix's two score columns are decimal-aligned, and they are the only place raw "
    "spreadsheet precision reaches print (0.316111, 0.055555556) [table.decimal_aligned].",
    "The matrix title is also its caption: 'Weighted Decison Matrix Model' prints under the last "
    "band, misspelled, with no label number of any kind [table.note_sentence].",
    "Eight of the nine body figures come out of one Excel chart engine - five line charts, "
    "three of them staircases of the human-capital distribution, and three bar charts of age - "
    "sharing one frame, one gridline style and one font [geometry.family].",
    "Only one body figure is a drawn diagram rather than a chart - the wage/People diagram of "
    "Figure 3 - and it is the only exhibit in the paper whose content is labelled regions rather "
    "than plotted values [geometry.data_labels].",
    "Legends are used sparingly and always as a single chip: 'Frequency' to the right of the "
    "frame on the three bar charts, and one inside-frame legend below the plot on the "
    "three-series line chart [geometry.legend].",
    "No exhibit in the paper is three-dimensional, none carries a colourbar, and the only colour "
    "scale is the conditional fill inside the decision matrix [geometry.colorbar].",
    "In-plot titles stand in for captions: eight of the nine body charts repeat their year or "
    "population name inside the frame, and in one case title and caption disagree (Figure 5 is "
    "titled '+50 yrs' but captioned 2150) [geometry.printed_numbers].",
    "Axis titling is inconsistent across one template: 'Human Capital Level' in Figures 1, 4 and "
    "9 against 'Human Capital level' in Figure 8, and 'Age Group (5yrs)' against 'Age Group, 5 "
    "yrs' across the two halves of the p18 pair [geometry.shared_axes].",
    "The appendix captures are screenshots, not drawings: worksheet gridlines, grey header cells, "
    "colour-filled inputs and empty cells print inside the measured region, and one dashboard is "
    "half covered by a solid black rectangle [geometry.data_labels].",
    "One exhibit is notebook output rather than a figure: the Mathematica plot on p30 prints the "
    "code cells that drew it directly above the curve, and the plot has no axis titles, no legend "
    "and no caption [caption.verbatim].",
    "Three charts clip or mislabel their own axes: Figure 9's curve rises into the frame "
    "corner and is cut off while its x axis runs on unlabelled, Figure 7 breaks its own "
    "two-decimal tick format by printing 0.1 over a 0.03-to-0.09 ladder, and the p34 plate has "
    "an x axis with no tick labels at all [geometry.printed_numbers].",
    "The citation grammar splits three ways: a numbered reference ('can be found in Figure 1', "
    "'as displayed in Figure 5'), a pure deictic ('pictured below', 'shown above:'), and one "
    "parenthetical '(see Figure)' with no number at all [mention.lead_pattern].",
    "Body figures are cited on their own page; the appendix dashboard is cited on p14 and prints "
    "on p27, a thirteen-page lead announced by the words 'in Figure 1 of Appendix UL1' even "
    "though the appendix is printed under a different title [mention.lead_pages].",
    "Exhibit size is uniform by part, not by importance: the nine body figures are all drawn in "
    "one fixed column at 0.07 to 0.11 of the page, while the five uncaptioned appendix plates "
    "take 0.16 each and say less than any captioned figure [place.area_frac].",
]

NOTE = (
    "A 35-page policy paper with nine body figures, one landscape decision-matrix grid, four "
    "appendix captures and five uncaptioned plates. The body draws every figure in the same Excel "
    "engine - step charts for human capital, single-chip 'Frequency' bars for age and education - "
    "with in-plot titles standing in for captions and one drawn wage/People diagram as the only "
    "labelled exhibit. Captions print below in the body and above in the appendix, and the two "
    "runs number independently: 'Figure 1.' to 'Figure 9.' with a period, then 'Figure 1:' to "
    "'Figure 3:' with a colon. From Figure 4 the running text is consistently one number ahead of "
    "the printed captions, and Figure 7's caption is the bare number with no description. The "
    "single grid is on the single landscape page and is measured as three bands of one table, "
    "with a repeated header and a title under the last band. Pages 33 to 35 have no text layer: "
    "they reprint body charts as full-page plates with no captions and no numbers."
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
    "f1": 1, "f2": 2, "f3": 3, "f4": 4, "f5": 5, "f6": 6, "f7": 7, "f8": 8, "f9": 9,
    "m1": 10, "m2": 10, "m3": 10,
    "a1": 11, "a2": 12, "a3": 13, "a4": 14,
    "p33a": 15, "p33b": 16, "p34a": 17, "p34b": 18, "p35a": 19,
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
    print("cap.src", dict(Counter(e["caption_source"] for e in exhibits)))
    print("cap.num", dict(Counter(e["caption"]["numbering"] for e in exhibits)))
    print("cap.pos", dict(Counter(e["caption"]["position"] for e in exhibits)))
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
