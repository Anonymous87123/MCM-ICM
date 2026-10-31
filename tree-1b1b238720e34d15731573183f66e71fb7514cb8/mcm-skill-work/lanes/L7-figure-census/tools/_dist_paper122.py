"""Hand pass for P-B-2017-69427-b04ae242 (toll-plaza design, 13 figures, 10 tables, 3 annexes).

Shape of the paper: every model section prints a table of parameters, then a plan-view
drawing of the plaza, then a chart of the result, in that order, and the paper repeats the
same three drawing types (Fan in / Fan out fans, a numbered-lane network, a traffic-flow
plan) at four different scales. The appendices read differently: three service-level
classification grids and three program listings, framed with grey title bars.

What the record has to say out loud:

1. The appendix annexes carry no figure or table number. Their only label is a grey band
   printed inside the frame ("Annex 1 Service level classification based on average queue
   length"), so `caption.numbering` is `none` and the band text is quoted instead.
2. Pages 27 and 28 hold program listings, and the LINGO.lg4 listing is split across the page
   break: three lines of it reappear bare at the top of p28. Code is not an exhibit here.

Usage: python -I tools/_dist_paper122.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2017-69427-b04ae242"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

ORDER = [
    (4, 1),
    (7, 1), (7, 2), (7, 3),
    (10, 1),
    (11, 1),
    (12, 1), (12, 2), (12, 3),
    (15, 1), (15, 2), (15, 3), (15, 4),
    (16, 1),
    (17, 1),
    (18, 1), (18, 2), (18, 3),
    (19, 1), (19, 2),
    (20, 1), (20, 2), (20, 3),
    (21, 1), (21, 2), (21, 3),
    (22, 1),
    (24, 1),
    (26, 1),
    (27, 1),
    (28, 1),
]


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def span(page: int, start: str, end: str) -> str:
    t = text(page)
    i = t.find(start)
    assert i >= 0, f"start {start!r} not on page {page}"
    j = t.find(end, i)
    assert j >= 0, f"end {end!r} not after start on page {page}"
    q = t[i:j + len(end)]
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def place(page: int, idx: int, path: list[str], kind: str) -> dict:
    b = REG[(page, idx)]
    mid = (b[1] + b[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    same = [k for k in ORDER if k[0] == page]
    numbered = not path[0].startswith("未编号标题")
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": ORDER.index((page, idx)) + 1,
        "page_order": same.index((page, idx)) + 1,
        "page_zone": z,
        "area_frac": round((b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H), 3),
        "solo_page": (b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H) > 0.5,
    }


def caption(v: str, *, numbering: str = "Fig. N", cond: bool = False,
            concl: bool = False, units: bool = False, vars_: int = 0,
            pos: str = "below", voice: str = "none", sentences: int | None = None) -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)) if sentences is None else sentences,
        "units": units,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": cond,
        "concludes": concl,
        "voice": voice,
        "position": pos,
    }


def mention(page: int, *, first: int | None, style: list[str], count: int,
            lead: str = "", pattern: str = "none", read: int = 0,
            trail: str = "") -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": count,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def figure(page: int, idx: int, family: str, cap: dict, men: dict, *, path: list[str],
           kind: str, legend: str = "none", three_d: str = "no",
           printed: bool = False, labels: bool = False, panels: int = 1,
           layout: str = "1", shared: bool = False, note: str = "",
           other_note: str = "", confidence: str = "high", panel_of: int = 0,
           src: str = "text-layer") -> dict:
    item = {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": confidence,
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": src,
        "note": note,
        "place": place(page, idx, path, kind),
        "mention": men,
        "caption": cap,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    if panel_of:
        item["is_panel_of"] = panel_of
    return item


def table(page: int, idx: int, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer" if cap["verbatim"] else "none",
        "note": note,
        "place": place(page, idx, path, kind),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed", zebra: bool = False,
         merged: bool = False, diag: bool = False, units_hdr: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "full",
         orient: str = "portrait", continued: bool = False, note: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rules,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diag,
        "units_in_header": units_hdr,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": orient,
        "continued": continued,
        "note_sentence": note,
    }


# the appendix pages sit past the References entry and have no numbered heading of
# their own, so their section_path is the unnumbered label the context dump emits
SUP = "未编号标题 References"

P1 = ["1 Introduction", "1.1 Background"]
P_SYM = ["4 Symbols and Definitions"]
P_B = ["4 Calculation of the number of toll lanes B"]
P_M = ["5 The Model"]
P_SENS = ["5 The Model", "5.1 Model I: The Determination of the Toll Lane Number B",
          "5.1.5 Sensitivity Analysis——Parameter Sensitivity of DHV"]
P_524 = ["5 The Model", "5.2.4 Model Calculation and Result Analysis"]
P_532 = ["5 The Model",
         "5.3 Model Ⅲ: An Optimization Model for the Minimum Cost of Toll Plaza",
         "5.3.2 Supplementary Assumptions and Justification"]
P_534 = ["5 The Model",
         "5.3 Model Ⅲ: An Optimization Model for the Minimum Cost of Toll Plaza",
         "5.3.4 Model Calculation and Result Analysis"]
P_61 = ["6 Testing the Model", "6.1 Influence of Traffic Flow on Model"]
# the 6.2 heading (influence of the share of autonomous vehicles) prints mid-page on
# p19 and the layout pass never picked it up, so the two p19 exhibits are filed under
# the next heading it does know; the note on each record says where they really belong
P_63 = ["6 Testing the Model",
        "6.3 The Influence of the Proportion of Three Tollbooths on the Model"]
P_72 = ["7 Case Study on New Jersey 's Freeway Toll Plaza",
        "7.2 The Structural Analysis of the Parameters"]
P_73 = ["7 Case Study on New Jersey 's Freeway Toll Plaza",
        "7.3 Model Application and Result Analysis"]
P_8 = ["8 Conclusions"]
P_11 = ["11 A letter to the New Jersey Highway Authority"]
P_SUP = [SUP]

ALL = [
    figure(4, 1, "map-or-plan-view",
           caption("Fig. 1 A plan graph of the toll plaza"),
           mention(4, first=None, style=[], count=0),
           path=P1, kind="introduction",
           note="the layout filed this region under 1.2 Previous Research, but the "
                "caption sits above that heading, at the end of 1.1 Background, so the "
                "path records 1.1 and the defect is the same last-heading-on-page "
                "attachment the lane already reported",
           src="text-layer"),
    table(7, 1,
          caption("Table 1 Symbols and Definitions", numbering="Table N"),
          mention(7, first=7, style=[], count=0,
                  lead=span(7, "In the section, we use some symbols", "as follows:"),
                  pattern="direct"),
          grid(6, 4, header=1, rules="vertical-rules", txt=4,
               note="P.s. Other symbols instructions will be given in the text."),
          path=P_SYM, kind="symbols",
          note="two symbol/meaning pairs per row, eleven symbols over five body rows; "
               "the header row is the only shaded band"),
    figure(7, 3, "flowchart-or-schematic",
           caption("Fig. 2 Flow chart of overall analysis"),
           mention(7, first=7, style=["Fig. 2"], count=1,
                  lead=span(7, "Before diving into the specific modeling steps",
                            "shown in Fig. 2"),
                  pattern="as-shown-in"),
           path=P_M, kind="model",
           note="six ellipses joined by two curly braces and one hollow down-arrow; the "
                "only figure in the paper that is a step diagram rather than a plan view"),
    table(10, 1,
          caption("Table 2 a traffic lane intensity value", numbering="Table N"),
          mention(10, first=None, style=[], count=0),
          grid(10, 5, header=2, rules="vertical-rules", merged=True, diag=True,
               decimal=True, numeric=4, txt=1),
          path=P_B, kind="solution",
          note="lookup grid: the corner cell is split by one diagonal with traffic "
               "intensity ns above and vehicle lane N below, Service Level q/s spans the "
               "four data columns, and the two header rows carry 0.5/1.0/1.5/2.0. The "
               "prose cross-reference just before it, (Table 5[14]), points at another "
               "paper's table via reference [14], not at this paper's Table 5"),
    table(11, 1,
          caption("Table 3 Calculation results", numbering="Table N"),
          mention(11, first=11, style=[], count=0,
                  lead=span(11, "By calculating and querying the traffic strength values",
                            "we get the following results:"),
                  pattern="direct"),
          grid(2, 3, header=1, rules="booktabs", units_hdr=True, numeric=3),
          path=P_SENS, kind="sensitivity",
          note="the measured region is the header band only (Traffic volume per hour "
               "(vehicles/h) / Traffic intensity (vehicles/h) / Toll lanes); the single "
               "result row 4578 / 0.7716 / 7 sits in the prose band below it and was not "
               "measured separately, so the row count is taken from the text layer"),
    figure(12, 1, "line",
           caption("Fig. 3 The relationship between traffic volume and toll lanes"),
           mention(12, first=None, style=[], count=0,
                  trail=span(12, "From the figure above",
                             "the number of toll lanes are positively related"),
                  read=1),
           path=P_SENS, kind="sensitivity", legend="outside-right",
           note="the layout filed this chart under 5.2.3, but it is the sensitivity plot "
                "of 5.1.5 and prints above the 5.2 heading; Excel chart with diamond "
                "markers, four-sided light-grey box and a flat step from 5 to 5 around "
                "1900-2650 veh/h"),
    table(15, 1,
          caption("Table 4 Parameter index", numbering="Table N"),
          mention(15, first=15, style=[], count=0,
                  lead=span(15, "There are three main lanes", "as follows:"),
                  pattern="direct"),
          grid(4, 4, header=1, rules="booktabs", units_hdr=True, numeric=3, txt=1,
               note=""),
          path=P_524, kind="model",
          note="measured region is the header strip (Charging Ways / Lane width（m）/ "
               "Speed（km/h）/ Capacity（vehicles per hour）); the three body rows are the "
               "fragment excluded on p15, so rows come from the text layer"),
    figure(15, 3, "node-link-network",
           caption("Fig. 4 Network diagram"),
           mention(15, first=15, style=[], count=0,
                  lead=span(15, "Then we turn the toll plaza into a graph theory",
                            "we get the following results:"),
                  pattern="direct"),
           path=P_524, kind="model", printed=True,
           note="raster, not vector: an oval network with the twenty-two lanes printed as "
                "node numbers 1-22 plus the source S and sink T, no axes and no legend"),
    table(15, 4,
          caption("Table 5 Performance analysis of toll plaza", numbering="Table N"),
          mention(15, first=15, style=[], count=0,
                  lead=span(15, "We use Lingo (code: LINGO.lg4 and LINGO1.lg4)",
                            "is as follows:"),
                  pattern="direct"),
          grid(6, 3, header=1, rules="vertical-rules", merged=True, units_hdr=True,
               numeric=2, txt=1),
          path=P_524, kind="model",
          note="the Path column is merged over row pairs and the Total Accident Rate "
               "column is one cell merged over all five paths, so the grid is 6 rows but "
               "carries five results"),
    figure(16, 1, "map-or-plan-view",
           caption("Fig. 5 Traffic flow diagram"),
           mention(16, first=1, style=["Fig.5"], count=1,
                  lead=span(1, "Similarly, by using the data of the highway tollbooths",
                            "we obtain the program of merging pattern (Shown in Fig.5)"),
                  pattern="parenthetical"),
           path=P_532, kind="assumption",
           note="the undimensioned member of the fan in / fan out family; the p15 "
                "sentence The traffic flow diagram is as follows: introduces it but "
                "carries no number, so mention records the abstract's numbered citation"),
    figure(17, 1, "map-or-plan-view",
           caption("Fig. 6 Traffic flow diagram"),
           mention(17, first=1, style=["Fig.6"], count=1,
                  lead=span(1, "Likewise, using the data from the highway tollbooths",
                            "we obtain the smallest toll plaza (Shown in Fig.6)"),
                  pattern="parenthetical",
                  trail=span(18, "we can see from the figure that the width of toll lane",
                             "is 50m"),
                  read=1),
           path=P_534, kind="model", printed=True,
           note="same drawing as Fig. 5 with dimension chains added: 50m lane width, "
                "22.5m main lane, 65.25m acceleration and deceleration, 48m toll lane"),
    table(18, 1,
          caption("Table 6 Traffic flow and accident rate data", numbering="Table N"),
          mention(18, first=18, style=[], count=0,
                  lead=span(18, "we change the traffic flow, so as to get the maximum "
                            "traffic flow and traffic accident rate under each flow",
                            "as follows:"),
                  pattern="direct",
                  trail=span(18, "From the table we can see that with the traffic flow",
                             "the collision rate is also increasing"),
                  read=1),
          grid(2, 13, header=1, rules="booktabs", numeric=12, txt=1),
          path=P_61, kind="model",
          note="a data strip rather than a headed table: row labels Traffic flow and "
               "Accident rate（%） sit in the stub column and the twelve values run across "
               "as columns. The sentence that reads it out says From the table, so the "
               "trail belongs here and not to Fig. 7 immediately below"),
    figure(18, 2, "map-or-plan-view",
           caption("Fig. 7 Traffic flow diagram"),
           mention(18, first=18, style=[], count=0,
                  lead=span(18, "The traffic flow diagram is as follows:", "as follows:"),
                  pattern="direct"),
           path=P_61, kind="model",
           note="the undimensioned drawing again, one page after the dimensioned Fig. 6"),
    figure(18, 3, "line",
           caption("Fig. 8 Relationship between traffic flow and maximum flow"),
           mention(18, first=None, style=[], count=0,
                  trail=span(19, "The picture above depicts the relationship",
                             "the maximum flow rate"),
                  read=1),
           path=P_61, kind="model", legend="inside",
           note="MATLAB line chart, one series Maximum traffic with open circular "
                "markers, four-sided frame, no gridlines, legend printed inside the "
                "upper right; the reading sentence opens the next page"),
    table(19, 1,
          caption("Table 7 Performance analysis of toll plaza", numbering="Table N"),
          mention(19, first=19, style=[], count=0,
                  lead=span(19, "according to the previous procedure, using MATLAB",
                            "which are as follows:"),
                  pattern="direct"),
          grid(6, 3, header=1, rules="vertical-rules", merged=True, units_hdr=True,
               numeric=2, txt=1),
          path=P_63, kind="model",
          note="same 6x3 template as Table 5 (merged Path pairs, one merged rate cell); "
               "it belongs to 6.2, whose heading the layout missed, hence the 6.3 path"),
    figure(19, 2, "map-or-plan-view",
           caption("Fig. 9 Vehicle shunt after automatic driving"),
           mention(19, first=19, style=[], count=0,
                  lead=span(19, "The one-sided shunt mode is shown below:",
                            "is shown below:"),
                  pattern="as-shown-in",
                  trail=span(19, "From the results above, we can know that the traffic "
                             "flow of electronic tollbooths will increase",
                             "the number of autonomous vehicles increases"),
                  read=1),
           path=P_63, kind="model", printed=True,
           note="one-sided shunt version of the fan drawing, dimensioned 62.25m / 48m / "
                "62.25m; also belongs to 6.2 rather than 6.3"),
    table(20, 1,
          caption("Table 8 Model results", numbering="Table N"),
          mention(20, first=20, style=[], count=0,
                  lead=span(20, "According to the method of determining the toll lanes",
                            "we get the new program"),
                  pattern="direct"),
          grid(4, 3, header=1, rules="booktabs", txt=3,
               note=""),
          path=P_72, kind="result",
          note="the measured region is the closing row only (The Length of Acceleration "
               "Area / 57.31m / 65.25m); the header Program / New Program / Previous "
               "Program and the Number of Tollbooths row were never split off as a region, "
               "so the 4x3 shape comes from the text layer and the grid is checked from "
               "the bottom row that survived"),
    figure(20, 2, "map-or-plan-view",
           caption("Fig. 10 Traffic convergence"),
           mention(20, first=20, style=[], count=0,
                  lead=span(20, "we can get the following vehicle confluence model",
                            "vehicle confluence model"),
                  pattern="direct",
                  trail=span(20, "We can know from the figure above",
                             "the entire toll area will be reduced"),
                  read=1),
           path=P_72, kind="result", printed=True,
           note="dimensioned 57.31m / 48m / 57.31m, the acceleration length the new "
                "program in Table 8 produces"),
    table(20, 3,
          caption("Table 9 Highway Data of New Jersey", numbering="Table N"),
          mention(20, first=20, style=[], count=0,
                  lead=span(20, "We query the data of the number of lanes, lane width",
                            "the length of deceleration area"),
                  pattern="direct"),
          grid(2, 4, header=1, rules="booktabs", units_hdr=True, numeric=4),
          path=P_72, kind="result",
          note="header/body rule is missing, so the header is separated by white space "
               "alone and the table reads as a two-rule booktabs block"),
    figure(21, 1, "line",
           caption("Fig. 11 The changes of day traffic flow in New Jersey"),
           mention(21, first=None, style=[], count=0,
                  trail=span(21, "From the figure, we can get the conclusion",
                             "reaches a peak around seven o 'clock am"),
                  read=1),
           path=P_73, kind="model", legend="outside-right",
           note="Excel line chart pasted with its own thin grey border box: one smoothed "
                "series, no markers, horizontal gridlines only, left+bottom axis lines, "
                "legend outside on the right"),
    table(21, 2,
          caption("Table 10 The Results of Model Application", numbering="Table N"),
          mention(21, first=21, style=[], count=0,
                  lead=span(21, "The results are as follows", "as follows"),
                  pattern="direct"),
          grid(2, 3, header=1, rules="booktabs", numeric=2, txt=1, width="column"),
          path=P_73, kind="model",
          note="the narrow variant of the results table: same figures as the p24 table "
               "but without the Length of Acceleration Area column"),
    figure(21, 3, "map-or-plan-view",
           caption("Fig. 12 Design of tollbooth with different accelerations"),
           mention(21, first=1, style=["Fig.12"], count=1,
                  lead=span(1, "we get its shape about toll plaza",
                            "the figure of merge pattern (See Fig.12)"),
                  pattern="parenthetical"),
           path=P_73, kind="model", printed=True,
           note="the only plan view with colour: the booths are orange filled "
                "parallelograms across a dashed plaza footprint, dimensioned 26m wide, "
                "131m long, 44.8 tilt"),
    figure(22, 1, "bar",
           caption("Fig. 13 Comparison of design schemes with existing schemes"),
           mention(22, first=22, style=[], count=0,
                  lead=span(22, "the following figure is the result of their comparison",
                            "result of their comparison"),
                  pattern="direct",
                  trail=span(22, "From the graph we can see that our scheme",
                             "the number of toll lanes reduced"),
                  read=1),
           path=P_8, kind="evaluation", legend="outside-right",
           note="grouped column chart, two series (calculated value / actual value) over "
                "five categories, no title and no axis titles, legend outside on the "
                "right, horizontal gridlines only"),
    table(24, 1,
          caption("", numbering="none"),
          mention(24, first=None, style=[], count=0),
          grid(2, 4, header=1, rules="booktabs", numeric=3, txt=1),
          path=P_11, kind="other",
          note="captionless: no table number or title anywhere on p24, so the caption "
               "block is empty. It is the four-column extension of Table 10, adding "
               "Length of Acceleration Area 61.28 m"),
    figure(26, 1, "table-as-figure",
           caption("Annex 1 Service level classification based on average queue length",
                   numbering="none", pos="above"),
           mention(26, first=None, style=[], count=0),
           path=P_SUP, kind="other", panels=2, layout="two annex grids stacked",
           note="one measured region holding two framed annex tables, Annex 1 (average "
                "queue length) and Annex 2 (average delay time); each is 5x2 boxed with "
                "no header band, no zebra and no merged cells, and neither carries a "
                "number: the label is the grey band printed inside the frame",
           src="text-layer"),
    figure(27, 1, "table-as-figure",
           caption("Annex 3 Service level classification based on average delay time",
                   numbering="none", pos="above"),
           mention(27, first=None, style=[], count=0),
           path=P_SUP, kind="other",
           note="Annex 3's band repeats Annex 2's wording word for word, but the body "
                "under it is not a classification table at all: it is a pasted A= printout, "
                "a matrix of 1000/800/700/727/703/645 entries and blank cells, followed on "
                "the same region by the LINGO.lg4 listing with grey Filename and Function "
                "bands. The region carries one entry because the code shares the box",
           src="text-layer"),
]

EXCLUDED = [
    (7, 2, "fragment-of-other",
     "a single cell of Table 1 (S' / Safety distance of moving vehicle) split off from "
     "the table body and measured as its own region"),
    (12, 2, "not-an-exhibit",
     "three lines of body prose under 5.2 Model II, no drawing in the box"),
    (12, 3, "not-an-exhibit",
     "seven lines of body prose under 5.2.1 Modeling Ideas, no drawing in the box"),
    (15, 2, "fragment-of-other",
     "the two closing data rows of Table 4 (Semi-automatic charge 703, Labor charges "
     "624); the header band is the recorded table"),
    (28, 1, "not-an-exhibit",
     "program listings only: the bare three-line tail of LINGO.lg4, then LINGO1.lg4 "
     "and the MATLAB sir.m / iil.m listings"),
]


def excluded_regions() -> list[dict]:
    return [{"page": p, "bbox": REG[(p, i)], "reason": r, "note": n}
            for p, i, r, n in EXCLUDED]

RULES = [
    "表型按节复制：5.2.4 的 Table 5 与 6.3 的 Table 7 是同一张横向模板（6 行 3 列、"
    "竖线全网格、Path 列跨行合并、Total Accident Rate 列一格跨全表、单位写在表头），"
    "换的只是数值 [table.rule_style] [table.merged_cells]。",
    "同底图复用靠尺寸链区分版本：Fig. 5 与 Fig. 7 不标尺寸，Fig. 6、Fig. 9、Fig. 10"
    " 在同一个 fan in/fan out 底图上加 50m/65.25m/48m、62.25m、57.31m 的尺寸链"
    " [geometry.printed_numbers] [geometry.family]。",
    "图号引用几乎只出现在题注和摘要：13 张图里只有 Fig. 2 在正文被编号引用，"
    "Fig. 5/6/12 的编号引用全部落在摘要的括号里，其余 count 为 0 "
    "[mention.count] [mention.lead_pattern]。",
    "无编号引出的图仍有引出句：图前的 The traffic flow diagram is as follows: 一类句式"
    "只填 lead_sentence，不把计数抬到 1，也不改 first_page 的含义 [mention.lead_sentence]。",
    "读句跟数据不跟图：Table 6 下面那句 From the table we can see... 说的是表，"
    "紧接其后的 Fig. 7 没有读句 [mention.trail_sentence]。",
    "表的引出句是单一模板：Table 3/4/5/6/7/8/10 一律用 ...as follows: 或 which are "
    "shown in the following table 收尾 [mention.lead_pattern]。",
    "附录三张 Annex 表不带表号，唯一标签是框内灰底标题带，numbering 记 none "
    "[caption.numbering] [caption.verbatim]。",
    "Appendix 标签有错位：Annex 3 的标题照抄 Annex 2（都写 average delay time），"
    "但正文是 A= 矩阵粘贴，说明附录标题带与内容脱钩 [caption.verbatim]。",
    "Excel 粘贴图沿用同一套默认样式：Fig. 3、Fig. 11、Fig. 13 图例都在图外右侧，"
    "只有水平网格线，且整幅图带一圈细灰边框 [geometry.legend]。",
    "代码清单不进入图表普查：p28 整页只有 LINGO 与 MATLAB 清单的尾部和两份新清单，"
    "按 not-an-exhibit 排除；p27 的清单与 Annex 3 矩阵共用同一区域，只记一条 "
    "[geometry.family]。",
]

payload = {"paper": PID, "layout_sha256": LAYOUT["layout_sha256"],
           "items": [e for e in ALL if "table" not in e],
           "tables": [e for e in ALL if "table" in e],
           "excluded_regions": excluded_regions(), "rules": RULES,
           "note": "hand pass"}

out = PROXY / f"{PID}-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"wrote {out} items={len(payload['items'])} tables={len(payload['tables'])} "
      f"rules={len(RULES)} excluded={len(payload['excluded_regions'])}")
