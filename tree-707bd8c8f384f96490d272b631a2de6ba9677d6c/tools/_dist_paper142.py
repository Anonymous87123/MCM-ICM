"""Hand pass for P-F-2017-72283-776dd1c3 (Mars colony: Population Zero).

25 pages, 14 measured regions: 4 captioned MATLAB line figures, 5 uncaptioned vector charts,
4 tables and the p1 summary sheet (exclusion).

What the record has to say out loud:

1. Captions split by exhibit type, not by part of the paper: all four figure captions print
   BELOW their artwork, all four table captions ABOVE their grid.
2. Five of the nine figures print no caption and no number at all - the two scatter plots on
   p10, the Lorenz curve on p13 and the two migration curves on pp20-21.
3. The caption/number boundary is a drawing-tool boundary: every captioned figure is a raster
   MATLAB screenshot and every uncaptioned chart is a vector plot whose axis titles sit at the
   ends of the axes.
4. Two citation grammars run side by side: numbered ("Looking at Figure 3", "as follows in
   Table 1") and deictic ("We see in the figure below", "The lower curve above", "This graph
   shows").
5. One citation is mis-numbered: the p18 sentence that summarizes the gender/age weights says
   "summarized in Table 4" while Table 3 is the grid printed directly under it, so Table 3 is
   never cited and Table 4 is announced twice.
6. The vector charts put their axis titles at the axis ends instead of beside them, print no
   plot title, and use a space as thousands separator; the MATLAB screenshots use in-plot
   titles, conventional axis titles and plain integers.

Usage: python -I tools/_dist_paper142.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-F-2017-72283-776dd1c3"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    "f1": (6, [148.8, 60.1, 446.4, 255.1]),
    "f2": (6, [144.6, 306.7, 450.6, 501.7]),
    "s1": (10, [91.7, 252.4, 304.1, 383.7]),
    "s2": (10, [93.9, 539.1, 354.6, 698.3]),
    "lorenz": (13, [80.0, 232.2, 347.0, 397.3]),
    "f3": (14, [131.9, 510.4, 463.4, 679.9]),
    "f4": (15, [116.4, 160.6, 478.9, 321.6]),
    "t1": (18, [157.6, 81.9, 437.7, 156.1]),
    "t2": (18, [57.6, 214.6, 551.6, 288.4]),
    "t3": (18, [73.7, 543.8, 521.6, 632.5]),
    "t4": (19, [120.7, 253.6, 474.6, 372.3]),
    "m1": (20, [98.1, 220.9, 360.9, 383.3]),
    "m3": (21, [94.4, 224.5, 327.9, 368.8]),
}

EXCLUDED = {"p1 summary sheet": (1, [40.0, 42.0, 570.0, 753.0])}

for _name, (_p, _b) in {**B, **EXCLUDED}.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 14, len(MEASURED)

S = {
    "s2": "2 Selecting Population Zero",
    "s2_3": "2.3 Planning the community",
    "s3": "3 Factors of a Successful Society",
    "s3_3": "3.3 Developing the Models",
    "s3_31": "3.3.1 Education",
    "s3_32": "3.3.2 Income",
    "s3_34": "3.3.4 Racial Equality",
    "s4": "4 Forming a Global Model",
    "s4_3": "4.3 Developing the Model",
    "s4_4": "4.4 Validation of the model",
    "s5": "5 Accounting for Additional Migrations",
    "s5_1": "5.1 Scenario 1: A One-time Migration",
    "s5_3": "5.3 Scenario 3: Gradual Migration",
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


def cap(v: str, numbering: str, *, position: str = "below", vars_: int = 0) -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)) if v else 0,
        "units": False,
        "variables": vars_ > 0,
        "variable_count": vars_,
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
        labels: bool = False) -> dict:
    return {
        "family": family,
        "panel_count": 1,
        "panel_layout": "1",
        "shared_axes": False,
        "legend": legend,
        "colorbar": False,
        "three_d": "no",
        "printed_numbers": numbers,
        "data_labels": labels,
    }


def figure(key: str, family: str, caption: dict, men: dict, geom: dict, *,
           path: list[str], kind: str, src: str = "text-layer", note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "is_panel_of": "",
        "caption_verbatim": caption["verbatim"],
        "caption_source": src,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }


def grid(rows: int, cols: int, *, header: int = 1, numeric: int = 0, txt: int = 1,
         width: str = "full") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": "boxed",
        "zebra": False,
        "merged_cells": False,
        "diagonal_header": False,
        "units_in_header": False,
        "decimal_aligned": False,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": False,
        "note_sentence": "",
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": caption["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "table": g,
    }


PLAN = [S["s2"], S["s2_3"]]
EDU = [S["s3"], S["s3_3"], S["s3_31"]]
INC = [S["s3"], S["s3_3"], S["s3_32"]]
RACE = [S["s3"], S["s3_3"], S["s3_34"]]
GLOB = [S["s4"], S["s4_3"]]
VALID = [S["s4"], S["s4_4"]]

FIGURES = [
    figure("f1", "line",
           cap("Figure 1: Simulation of Ages over Time With an Initial Population Not Containing "
               "Children", "Figure N:", vars_=2),
           mention(6, first=5, style=[], pattern="direct",
                   lead="We see in the ﬁgure below that around 40 years after the start of the "
                        "civilization, there is a"),
           geo("line", legend="inside", numbers=True),
           path=PLAN, kind="result",
           note="upper of two raster MATLAB screenshots on p6, the paper's first exhibits: a "
                "four-series line chart in blue, green, red and olive titled nothing in the frame, "
                "axis titles 'Number of Citizens' and 'Elapsed Time in Years', and a boxed legend "
                "inside the plot at upper right labelling the four age bands 0-18, 19-35, 36-65 "
                "and 66-100 in the series colours. The chart sits at the top of the page although "
                "the sentence that introduces it is on p5, so the exhibit is displaced one page "
                "forward from its lead"),
    figure("f2", "line",
           cap("Figure 2: Simulation of Optimal Population Distribution over Time With an Initial "
               "Population", "Figure N:", vars_=2),
           mention(6, first=5, style=[], pattern="direct",
                   lead="We see in the ﬁgure below that around 40 years after the start of the "
                        "civilization, there is a"),
           geo("line", legend="inside", numbers=True),
           path=PLAN, kind="result",
           note="the second screenshot on p6, same engine, same four series and the same boxed "
                "in-plot legend, and the same axes down to the tick text - only the data differ, "
                "the 66-100 band starting at zero and rising to about 110. Two exhibits this "
                "alike are numbered separately rather than treated as panels"),
    figure("s1", "scatter", NOCAP,
           mention(10, first=10, style=[], pattern="direct",
                   lead="established a negative correlation between unemployment among young "
                        "people and happiness"),
           geo("scatter", numbers=True),
           path=EDU, kind="model", src="none",
           note="uncaptioned vector scatter of EU-28 2013 points, about twenty five dots in a pale "
                "blue with a single straight fit line, y from 7.2 to 7.8. Printed with no frame "
                "at all: only the left and bottom axes are drawn, the axis titles are pasted at "
                "the axis ENDS ('Happiness' over the top of the y axis, 'Unemployment Rate' to "
                "the right of the x axis), and one x tick prints as 10 with a stray asterisk-like "
                "mark. No plot title, no caption, no legend"),
    figure("s2", "scatter", NOCAP,
           mention(10, first=10, style=[], pattern="direct",
                   lead="two possible ﬁts for the relationship between education and GDP per "
                        "capita"),
           geo("scatter", numbers=True),
           path=EDU, kind="model", src="none",
           note="lower of the two uncaptioned scatters, GDP per Capita against Years of Education "
                "in the hundreds of points, carrying what the prose describes as two fits - a "
                "linear and a quadratic curve - with no legend to tell them apart, so the two "
                "curves appear as a narrow pencil. Same end-of-axis title placement and the same "
                "frameless style; the y ticks print as space-separated thousands (20 000, "
                "80 000)"),
    figure("lorenz", "line", NOCAP,
           mention(13, first=13, style=[], pattern="direct",
                   trail="The lower curve above represents our income distribution", read=3),
           geo("line", numbers=True),
           path=INC, kind="result", src="none",
           note="the paper's Gini exhibit: two near-identical curves running from 0,0 to 1,1 - the "
                "perfect-equality diagonal and the colony's income distribution - printed "
                "uncaptioned and unlabelled, with no plot title and no axis titles at all, only "
                "bare 0.2 to 1.0 ticks on both axes. Because nothing keys the two curves, the "
                "sentence under it has to say which one is which"),
    figure("f3", "line",
           cap("Figure 3: Simulation of Dissimilarity Over Time for Equal Income Model",
               "Figure N:", vars_=2),
           mention(14, first=14, style=["Figure 3"], pattern="direct",
                   lead="Looking at Figure 3, we see that dissimilarity increases over time"),
           geo("line", legend="outside-right", numbers=True),
           path=RACE, kind="result",
           note="a MATLAB screenshot carrying all ten pairwise race dissimilarities as ten "
                "coloured series, with an in-plot title in dark red at the top left 'Dissimilarity "
                "between Races in Jobs Over Time', axis titles 'Dissimilarity Rating' and 'Years', "
                "and a legend parked outside the frame to the right whose ten italic entries "
                "('Dissimilarity between A and B' through 'D and E') run wider than the plot "
                "itself. The curves are jagged rather than smoothed, so the trend the caption "
                "claims is only visible as an envelope"),
    figure("f4", "line",
           cap("Figure 4: Simulation of Dissimilarity Over Time for Stratiﬁed Income Model",
               "Figure N:", vars_=2),
           mention(15, first=None, style=[]),
           geo("line", legend="outside-right", numbers=True),
           path=RACE, kind="result",
           note="the stratified-income rerun of Figure 3: same ten series, same outside-right "
                "legend, same frame. Two differences go unannounced - the in-plot title is "
                "dropped altogether, and the axis titles shorten to 'Dissimilarity' and 'Elapsed "
                "Time in Years', so the pair that a reader will compare does not share a word on "
                "either axis. Never cited anywhere in the paper"),
    figure("m1", "scatter", NOCAP,
           mention(20, first=None, style=[]),
           geo("scatter", numbers=True),
           path=[S["s5"], S["s5_1"]], kind="result", src="none",
           note="scenario 1's population trajectory, printed as dots with no connecting line - the "
                "closest thing in the paper to a simulation output plotted point by point. "
                "Frameless like the other vector charts, axis titles at the axis ends "
                "('Population' over the y axis, 'Years' past the end of the x axis), y ticks in "
                "space-separated thousands from 24 000 to 36 000. No caption, no legend, no title, "
                "and the paragraph above it never names it"),
    figure("m3", "line", NOCAP,
           mention(21, first=21, style=[], pattern="direct",
                   trail="This graph shows that our model is robust towards gradual migrations of "
                          "individuals from", read=2),
           geo("line", numbers=True),
           path=[S["s5"], S["s5_3"]], kind="result", src="none",
           note="scenario 3's gradual-migration curve, the only uncaptioned chart drawn as a "
                "connected line rather than dots: a sharp peak at about 30 000 then a flat "
                "plateau, over an x axis of 0 to 300 'Years since influx'. Same frameless "
                "end-labelled style; the prose before it says 'as shown in the following figure' "
                "and the prose after it calls it 'this graph', so the exhibit is tied down on both "
                "sides by deixis alone"),
]

TABLES = [
    table("t1", cap("Table 1: Weightings of Reponses", "Table N:", position="above"),
          mention(18, first=17, style=["Table 1"], pattern="as-shown-in",
                  lead="For these ﬁrst question, we weight the responses as follows in Table 1."),
          grid(4, 2, numeric=1, txt=1, width="half"),
          path=GLOB, kind="model",
          note="the paper's smallest grid: two columns (Response, Weight) and four Likert rows "
               "scoring 3, 2, 1, 0, printed about 60 per cent of the text width and centred. The "
               "only grid whose numeric column is a bare integer scale"),
    table("t2", cap("Table 2: Weighting of Priorities for U.S. Individuals of Distinct Income "
                    "Levels", "Table N:", position="above"),
          mention(18, first=17, style=["Table 2"], pattern="as-shown-in",
                  lead="We obtained the following results, which are summarized in Table"),
          grid(3, 6, numeric=5, txt=1),
          path=GLOB, kind="model",
          note="three income bands (Top 10%, Middle tier, Bottom 48%) against the five metrics "
               "Education, Economic Efficiency, Economic Equality, Social Equality and Happiness "
               "Index, every cell a 0.xx weight. Full text width, and the header cells wrap onto "
               "two lines inside a single header row"),
    table("t3", cap("Table 3: Weighting of Priorities for U.S. Individuals Based on Gender and "
                    "Age", "Table N:", position="above"),
          mention(18, first=None, style=[]),
          grid(4, 6, numeric=5, txt=1),
          path=GLOB, kind="model",
          note="the same five metrics against four demographic rows (Men, Women, Working Adults, "
               "Retired Adults). The sentence that summarizes this grid prints immediately above "
               "it but says 'summarized in Table 4', so the table the reader is looking at is the "
               "only one in the paper that no sentence names"),
    table("t4", cap("Table 4: Happiness Index Values Before/After EE/SE Tradeo↵", "Table N:",
                    position="above"),
          mention(19, first=18, style=["Table 4"], pattern="as-shown-in",
                  lead="We obtained the following results summarized in Table 4.",
                  trail="analysis are shown in Table 4 below."),
          grid(7, 3, numeric=2, txt=1),
          path=VALID, kind="result",
          note="the tradeoff summary: seven social categories (the three income bands from Table 2 "
               "plus the four demographic rows from Table 3) against Original and After EE/SE "
               "Tradeoff happiness values. The only grid where the decimal point wanders - the "
               "five-decimal 0.78709 sits visibly right of the six-decimal cells around it. The "
               "caption's 'Tradeoff' prints with an ff ligature the text layer renders as a "
               "return arrow"),
]

EXCLUDED_REGIONS = [
    {"page": p, "bbox": b, "reason": "not-an-exhibit", "note": n}
    for n, (p, b) in (("p1 summary sheet", EXCLUDED["p1 summary sheet"]),)
]

RULES = [
    "One numbering form covers every captioned exhibit - 'Figure N:' and 'Table N:' with a colon "
    "- so the paper has a single label grammar across both exhibit kinds [caption.numbering].",
    "Caption side follows the exhibit type, not the part of the paper: all four figure captions "
    "print BELOW their artwork and all four table captions print ABOVE their grid "
    "[caption.position].",
    "Five of the nine figures print no caption and no number at all - the two scatters on p10, "
    "the Lorenz curve on p13 and the two migration curves on pp20-21 - so a reader who trusts the "
    "numbering will believe the paper has four figures [caption.verbatim].",
    "The captioned/uncaptioned boundary is a drawing-tool boundary: every captioned figure is a "
    "raster MATLAB screenshot and every uncaptioned chart is a vector plot with no frame whose "
    "axis titles sit at the axis ends, so the tool that drew the exhibit decided whether it got a "
    "number [geometry.family].",
    "Two citation grammars run side by side and never mix within a sentence - a numbered "
    "reference ('Looking at Figure 3', 'as follows in Table 1') for the four numbered figures and "
    "the tables, and pure deixis ('We see in the figure below', 'The lower curve above', 'This "
    "graph shows') for the five unnumbered charts [mention.lead_pattern].",
    "Two of the nine figures are never cited at all - Figure 4 and the scenario-1 population "
    "curve on p20 - and both are the second member of a pair whose first member is discussed "
    "[mention.first_page].",
    "One citation is mis-numbered: the p18 sentence that summarizes the gender/age weights reads "
    "'summarized in Table 4' while Table 3 is the grid printed directly beneath it, so Table 3 is "
    "the only table no sentence names and Table 4 is announced twice, on p18 and again on p19 "
    "[mention.style].",
    "Tables are announced one page before they print (p17 for p18, p18 for p19) while figures "
    "print on or after their lead page, so the table numbering and the figure numbering run on "
    "different displacements [mention.lead_pages].",
    "Captions are longer than this lane's average - 11 to 14 words for the four figures, 5 to 13 "
    "for the four tables - and none states a unit, a condition or a conclusion, so length is "
    "spent on naming the experiment, not on interpreting it [caption.words].",
    "Legends appear on four of the nine figures and only ever one way: a boxed inside legend at "
    "upper right on the two p6 screenshots, and an outside-right legend on the dissimilarity pair "
    "whose ten italic entries are wider than the plot they belong to [geometry.legend].",
    "Nothing in the paper is three-dimensional, nothing carries a colourbar, and the only colour "
    "encoding is series hue - there is no sequential scale anywhere in nine figures and four "
    "tables [geometry.colorbar].",
    "Two chart engines have two dialects: the MATLAB screenshots carry in-plot titles and "
    "'Number of Citizens' / 'Elapsed Time in Years'-style axis titles with plain integer ticks, "
    "while the vector charts carry no plot title, paste the axis title at the end of the axis, "
    "and print space-separated thousands (20 000, 36 000) [geometry.printed_numbers].",
    "The same experiment reported twice is not reported the same way: Figure 4 drops the in-plot "
    "title Figure 3 prints and shortens 'Dissimilarity Rating' to 'Dissimilarity' and 'Years' to "
    "'Elapsed Time in Years', so the pair a reader will compare shares no axis word on either "
    "side [geometry.shared_axes].",
    "Charts that need a key mostly do not get one: the p10 GDP scatter prints two fitted curves, "
    "linear and quadratic, with no legend to tell which is which, and the Lorenz curve prints two "
    "unlabelled curves side by side, leaving the prose to say 'the lower curve above' "
    "[geometry.legend].",
    "All four grids are one style - a full outer box, a rule under the single header row and a "
    "rule between every body row - so the paper has no booktabs, no vertical-rules-only grid and "
    "no rule-less grid [table.rule_style].",
    "No grid is shaded, none merges a cell, none has a two-tier header, none carries a diagonal "
    "split, and none prints a unit in the header - the tables are as uniform as the figures are "
    "not [table.merged_cells].",
    "Not one table has a note line under its grid and not one continues onto a second page, so "
    "the four grids sit entirely inside the page their caption opens [table.continued].",
    "Table width is the only table variable: 60 per cent of the text width for the two-column "
    "Likert scale against full width for the two five-metric grids, with no change of type size "
    "[table.width].",
    "Only Table 4 has a decimal that wanders - its five-decimal 0.78709 sits right of the "
    "six-decimal cells around it - because no grid aligns on the decimal point at all "
    "[table.decimal_aligned].",
    "Exhibit size is set by tool, not by importance: the four raster screenshots run 0.11 to 0.12 "
    "of a page, the five vector charts 0.05 to 0.09, and the smallest thing in the paper is Table "
    "1's four-row Likert scale at 0.04 [place.area_frac].",
    "Placement follows displacement: the two p6 figures sit at the top of the page because their "
    "lead sentence is on p5, and every chart whose lead is on the same page sits in the middle or "
    "foot of it - the only other top-of-page exhibit is the uncited Figure 4 [place.page_zone].",
    "The summary sheet is a control page, not an exhibit: p1's whole-page block is the MCM summary "
    "form and is the paper's only excluded region, so 13 of the 14 measured regions are content "
    "[place.doc_order].",
]

NOTE = (
    "A 25-page Mars-colony paper with two drawing tools and two numbering habits. Four MATLAB "
    "screenshots carry the only figure captions in the paper, all printed below their artwork with "
    "the single form 'Figure N:'; five vector charts - two scatters, a Lorenz curve and two "
    "migration curves - print with no caption and no number at all, and are tied down by deixis "
    "instead ('We see in the figure below', 'The lower curve above', 'This graph shows'). The "
    "four tables use the same colon form, print their captions above their grids, and are "
    "uniformly boxed with a rule under the header and between every body row, unshaded, unmerged, "
    "with no note line and no continuation. One cross-reference is wrong: the sentence printed "
    "over Table 3 says 'summarized in Table 4', which leaves Table 3 uncited and Table 4 announced "
    "twice. The two chart dialects are stable within themselves - the screenshots title their "
    "plots and print plain integers, the vector charts put the axis title at the end of the axis "
    "and print space-separated thousands - and the one pair a reader will compare, Figures 3 and "
    "4, shares no axis word on either side."
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
    "f1": 1, "f2": 2, "s1": 3, "s2": 4, "lorenz": 5, "f3": 6, "f4": 7,
    "t1": 8, "t2": 9, "t3": 10, "t4": 11, "m1": 12, "m3": 13,
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
