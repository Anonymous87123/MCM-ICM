"""Hand pass for P-C-2017-55278-a011d0e2 (cell-automaton model, self-driving share, 21 figures + 1 table).

Shape of the paper: one cell-automaton model, then two simulation chapters that turn it into
effects, then a sensitivity chapter. Every result figure is the same Highcharts line chart,
exported with its own printed title inside the picture and its legend in a strip under the
plot, and the figures come in pairs: the left half is the whole-day run and the right half is
the peak-hour run of the same quantity.

What the record has to say out loud:

1. Only one table exists in the whole paper (Table 1, acceleration/deceleration
   probabilities), and it is the only exhibit whose caption prints above instead of below.
2. Eleven headings are attached one section too late by the layout pass, because
   `path_for(page)` takes the last heading on the page. Every affected record keeps the true
   printed section and names the misattachment in its note.
3. Two figures print before the text that numbers them (Fig. 8 and Fig. 12), so their
   `mention.lead_pages` are negative: the citation arrives a page after the figure.
4. All 22 measured regions are exhibits — 21 figures and 1 table. No region is excluded.

Usage: python -I tools/_dist_paper126.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2017-55278-a011d0e2"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

# reading order: left to right, then top to bottom, on every page
ORDER = [
    (6, 1),
    (8, 1),
    (10, 1),
    (11, 1),
    (12, 1),
    (14, 1), (14, 2),
    (15, 2), (15, 1), (15, 3), (15, 4),
    (16, 2), (16, 1),
    (17, 1),
    (18, 1),
    (19, 2), (19, 1), (19, 3),
    (20, 2), (20, 1),
    (21, 1),
    (22, 1), (22, 2),
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
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": ORDER.index((page, idx)) + 1,
        "page_order": same.index((page, idx)) + 1,
        "page_zone": z,
        "area_frac": round((b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H), 3),
        "solo_page": (b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H) > 0.5,
    }


def caption(v: str, *, numbering: str = "Figure N:", cond: bool = False,
            concl: bool = False, units: bool = False, vars_: int = 0,
            pos: str = "below", voice: str = "none") -> dict:
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
           kind: str, legend: str = "below", three_d: str = "no",
           printed: bool = False, labels: bool = False, panels: int = 1,
           layout: str = "1", shared: bool = False, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
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


def table(page: int, idx: int, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, note: str = "", source: str = "text-layer") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
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


P_MODELS = ["2 The Models"]
P_GEN = P_MODELS + ["2.3 Generation Model"]
P_FOLLOW1 = P_MODELS + ["2.4 Vehicle-Following Model", "2.4.1 The follower car is Human Driven"]
P_LANE = P_MODELS + ["2.5 Lane-Changing Model"]
P_INTER = P_MODELS + ["2.6 Intersection Model"]
P_SIM = ["3 Analyzing the Model by Simulation"]
P_32 = P_SIM + ["3.2 Effects of Percentage of Self-Driving Vehicles"]
P_33 = P_SIM + ["3.3 Effects of Lane Number"]
P_34 = P_SIM + ["3.4 Effects of Dedicated Lanes for Self-Driving Cars"]
P_35 = P_SIM + ["3.5 Effects of Traffic Volume"]
P_REAL = ["4 Apply to the Real Data"]
P_411 = P_REAL + ["4.1 Percentage of Self-Driving Vehicles",
                  "4.1.1 Average Velocity During a Whole Day"]
P_412 = P_REAL + ["4.1 Percentage of Self-Driving Vehicles",
                  "4.1.2 Average Velocity During Peak Hours"]
P_413 = P_REAL + ["4.1 Percentage of Self-Driving Vehicles", "4.1.3 Traffic Density"]
P_414 = P_REAL + ["4.1 Percentage of Self-Driving Vehicles",
                  "4.1.4 Average Velocity at Intersections"]
P_42 = P_REAL + ["4.2 Dedicated Lanes"]
P_SENS = ["5 Sensitivity Analysis"]
P_51 = P_SENS + ["5.1 Lane-Changing Probability Pc"]
P_52 = P_SENS + ["5.2 Coefficients α, β, and γ in Vehicle Following Model"]
P_53 = P_SENS + ["5.3 Error of Self-Driving Systems"]

MISATTACH = ("the layout pass attaches this region to the last heading printed on its page, "
             "which is one section late; the true printed section is ")

ALL = [
    table(6, 1,
          caption("", numbering="none"),
          mention(6, first=None, style=[], count=0),
          grid(26, 2, header=1, rules="booktabs", txt=2),
          path=P_MODELS + ["2.2 Notations"], kind="symbols", source="none",
          note="the notation table has no printed caption at all: it starts immediately under "
               "the 2.2 Notations heading, first line already the header row of symbols, so it "
               "carries no number and no title line and cannot be cited by number"),
    figure(8, 1, "line",
           caption("Figure 1: Car Arriving Frequency (N=200,000)", cond=True, vars_=1),
           mention(8, first=8, style=["Figure 1"], count=1, pattern="none", read=1,
                   trail=span(8, "From Figure 1, when p = 1",
                              "on average during peak hours")),
           path=P_GEN, kind="model",
           note="two series only (peak / non-peak) with circle and diamond markers; the "
                "printed title inside the picture is 'Car Arriving Frequency' and the legend "
                "sits in a strip under the x axis"),
    table(10, 1,
          caption("Table 1: Acceleration and Deceleration Probabilities when G > GS",
                  numbering="Table N:", cond=True, vars_=2, pos="above"),
          mention(10, first=None, style=[], count=0),
          grid(3, 8, header=1, rules="booktabs", numeric=7, txt=1),
          path=P_FOLLOW1, kind="model",
          note="the paper's only table and its only caption printed ABOVE the exhibit; three "
               "rules plus one vertical rule that separates the stub column of symbols (v, Pa, "
               "Pd) from the value columns, so it is a three-line grid with a stub divider "
               "rather than a full box"),
    figure(11, 1, "flowchart-or-schematic",
           caption("Figure 2: Conditions for Lane-Changing"),
           mention(11, first=11, style=["Figure 2"], count=1,
                   lead=span(11, "in the case of Figure 2", "then car A can change to lane 1"),
                   pattern="direct", read=1),
           path=P_LANE, kind="model", legend="none", printed=True,
           note="three lanes drawn as a corridor with dash-dot lane dividers and four vehicle "
                "cells A-D; the gaps G_AC, G_AB and G_AD are printed as double-headed arrows, "
                "no flow arrows and no legend" + MISATTACH + "2.5 Lane-Changing Model, not 2.6"),
    figure(12, 1, "map-or-plan-view",
           caption("Figure 3: Cloverleaf Interchange"),
           mention(12, first=12, style=["Figure 3"], count=1,
                   lead="Figure 3 shows the traffic flow on a cloverleaf interchange.",
                   pattern="figure-n-shows", read=1),
           path=P_INTER, kind="model", legend="inside", printed=True,
           note="plan view of a cloverleaf: two carriageways with printed Lane 1-4 labels, five "
                "vehicle positions A-E, yellow arrows for flow direction and blue arrows for "
                "the ramp route, plus an inside-upper-right legend for the two arrow types"),
    figure(14, 1, "line",
           caption("Figure 4: Average Passing Time"),
           mention(14, first=13, style=["Figure 4 and Figure 5", "In Figure 4"], count=3,
                   lead="Figure 4 and Figure 5 show the results.",
                   pattern="figure-n-shows", read=1,
                   trail=span(14, "When self-driving percentage is low",
                              "as indicated in Figure 4")),
           path=P_32, kind="result",
           note="left half of a side-by-side pair; the caption for both halves prints on one "
                "line under the pair, so this record quotes only the left clause" + MISATTACH
                + "3.2 Effects of Percentage of Self-Driving Vehicles, not 3.3"),
    figure(14, 2, "line",
           caption("Figure 5: Traffic Density"),
           mention(14, first=13, style=["Figure 4 and Figure 5", "In Figure 5"], count=2,
                   lead="Figure 4 and Figure 5 show the results.",
                   pattern="figure-n-shows", read=1,
                   trail=span(14, "In Figure 5, as the percentage", "cars increases")),
           path=P_32, kind="result",
           note="right half of the pair that Figure 4 opens; same two series and same legend" +
                MISATTACH + "3.2, not 3.3"),
    figure(15, 2, "line",
           caption("Figure 6: Impact of Lane Number", cond=True),
           mention(15, first=14, style=["Figure 6 and Figure 7"], count=2,
                   lead="We have two important observations based on Figure 6 and Figure 7.",
                   pattern="direct", read=1,
                   trail=span(14, "Both in Figure 6 and Figure 7",
                              "the three curves get closer to each other")),
           path=P_33, kind="result",
           note="left half of the lane-number pair, three series (3/4/5 lanes); the (Whole Day) "
                "qualifier prints on a second line under the caption and is not part of the "
                "caption line itself"),
    figure(15, 1, "line",
           caption("Figure 7: Impact of Lane Nmber", cond=True),
           mention(15, first=14, style=["Figure 6 and Figure 7"], count=2,
                   lead="We have two important observations based on Figure 6 and Figure 7.",
                   pattern="direct", read=1,
                   trail=span(14, "Both in Figure 6 and Figure 7",
                              "the three curves get closer to each other")),
           path=P_33, kind="result",
           note="right half of the pair (Peak Hours); the caption keeps the printed typo "
                "'Nmber' verbatim"),
    figure(15, 3, "line",
           caption("Figure 8: Impact of Dedicated", cond=True),
           mention(15, first=16, style=["Figure 8 and Figure 9"], count=1,
                   lead=span(16, "From Figure 8 and Figure 9",
                             "dedicated lanes may hurt the traffic capacity"),
                   pattern="direct", read=1),
           path=P_34, kind="result",
           note="left half of the dedicated-lane pair; the caption continues on a second line "
                "as 'Lanes (Whole Day)'. The figure prints before the paragraph that numbers "
                "it, so first_page is later than the page" + MISATTACH + "3.4 is correct here"),
    figure(15, 4, "line",
           caption("Figure 9: Impact of Dedicated", cond=True),
           mention(15, first=16, style=["Figure 8 and Figure 9", "in Figure 9"], count=3,
                   lead=span(16, "From Figure 8 and Figure 9",
                             "dedicated lanes may hurt the traffic capacity"),
                   pattern="direct", read=1,
                   trail=span(16, "For ex- ample, in Figure 9",
                              "passing time of 80s")),
           path=P_34, kind="result",
           note="right half of the pair (Peak Hours); the most-cited figure of the paper, "
                "read three times in one paragraph"),
    figure(16, 2, "line",
           caption("Figure 10: Impact of Traffic Volume", cond=True),
           mention(16, first=None, style=[], count=0),
           path=P_35, kind="result",
           note="left half of the traffic-volume pair, five series for 100k-500k vehicles; never "
                "cited by number" + MISATTACH
                + "3.5 Effects of Traffic Volume, not 4 Apply to the Real Data"),
    figure(16, 1, "line",
           caption("Figure 11: Impact of Traffic Volume", cond=True),
           mention(16, first=None, style=[], count=0),
           path=P_35, kind="result",
           note="right half of the pair (Peak Hours), five series; never cited by number" +
                MISATTACH + "3.5, not 4"),
    figure(17, 1, "line",
           caption("Figure 12: Average Traffic Flow Velocity During a Whole Day"),
           mention(17, first=18, style=["Figure 12"], count=1,
                   lead=span(18, "Compared with Figure 12",
                             "more significant impact for peak hour traffic flow"),
                   pattern="direct", read=1),
           path=P_411, kind="result",
           note="one of only two single (ungrouped) figures in the simulation chapters; four "
                "routes in one plot, legend below"),
    figure(18, 1, "line",
           caption("Figure 13: Average Traffic Flow Velocity During Peak Hours"),
           mention(18, first=None, style=[], count=0),
           path=P_412, kind="result",
           note="the peak-hour twin of Figure 12 and, like it, cited only through its twin" +
                MISATTACH + "4.1.2 Average Velocity During Peak Hours, not 4.1.3"),
    figure(19, 2, "line",
           caption("Figure 14: Impact of Self-Driving", cond=True),
           mention(19, first=18, style=["Figure 14 and Figure 15"], count=1,
                   lead=span(18, "From Figure 14 and Figure 15",
                             "reduce the traffic density of each road"),
                   pattern="direct", read=1),
           path=P_413, kind="result",
           note="left half of the traffic-density pair (Whole Day); four routes, legend below" +
                MISATTACH + "4.1.3 Traffic Density, not 4.1.4"),
    figure(19, 1, "line",
           caption("Figure 15: Impact of Self-Driving", cond=True),
           mention(19, first=18, style=["Figure 14 and Figure 15", "In Figure 15"], count=2,
                   lead=span(18, "From Figure 14 and Figure 15",
                             "reduce the traffic density of each road"),
                   pattern="direct", read=1,
                   trail=span(18, "In Figure 15, the traffic density decreases rapidly",
                              "when the percentage of self-driving is low")),
           path=P_413, kind="result",
           note="right half of the pair (Peak Hours), cited twice in the opening paragraph" +
                MISATTACH + "4.1.3, not 4.1.4"),
    figure(19, 3, "line",
           caption("Figure 16: Simulation of Highway Intersection"),
           mention(19, first=None, style=[], count=0),
           path=P_414, kind="result",
           note="the intersection run compared against the two straight-road routes; three "
                "series, and the only figure whose title says 'Simulation' while its body is "
                "an ordinary line chart rather than a picture of the intersection"),
    figure(20, 2, "line",
           caption("Figure 17: Impact of Dedicated", cond=True),
           mention(20, first=20, style=["Figure 17 and Figure 18"], count=1,
                   lead="Figure 17 and Figure 18 show the average velocity of Interstate 5 "
                        "with different number of dedicated lanes for self-driving cars.",
                   pattern="figure-n-shows", read=1),
           path=P_42, kind="result",
           note="left half of the Interstate-5 dedicated-lane pair (Whole Day), three series "
                "(0/1/2 dedicated lanes)" + MISATTACH + "4.2 Dedicated Lanes, not 5.1"),
    figure(20, 1, "line",
           caption("Figure 18: Impact of Dedicated", cond=True),
           mention(20, first=20, style=["Figure 17 and Figure 18"], count=1,
                   lead="Figure 17 and Figure 18 show the average velocity of Interstate 5 "
                        "with different number of dedicated lanes for self-driving cars.",
                   pattern="figure-n-shows", read=1),
           path=P_42, kind="result",
           note="right half of the pair (Peak Hours)" + MISATTACH + "4.2, not 5.1"),
    figure(21, 1, "line",
           caption("Figure 19: Sensitivity of Lane-Changing Probability"),
           mention(21, first=None, style=[], count=0),
           path=P_51, kind="sensitivity",
           note="three series for Pc = 0.2 / 0.5 / 0.8, never cited by number" + MISATTACH
                + "5.1 Lane-Changing Probability Pc, not 5.3"),
    figure(22, 1, "line",
           caption("Figure 20: Sensitivity of α, β and γ", vars_=3),
           mention(22, first=21, style=["Figure 20"], count=1,
                   lead="The results are shown in Figure 20.",
                   pattern="as-shown-in", read=1),
           path=P_52, kind="sensitivity",
           note="five series, one per α/β/γ combination, all five named in the legend; the "
                "figure floats to the top of p22 although its discussion sits in 5.2, so the "
                "section path follows the section that owns it rather than the heading above "
                "the region (5.3 starts at the foot of p21)"),
    figure(22, 2, "line",
           caption("Figure 21: Impact of Self-Driving System Error",
                   vars_=0, cond=True),
           mention(22, first=22, style=["Figure 21"], count=1,
                   lead="The result is shown in Figure 21.",
                   pattern="as-shown-in", read=1),
           path=P_53, kind="sensitivity",
           note="three series (perfect / random acceleration 10% / random deceleration 10%); "
                "the legend keeps the printed misspelling 'dcceleration'"),
]

RULES = [
    "全篇 22 个对象里 19 张是同一套 Highcharts 线图（[geometry.family]=line），只有 Fig. 2 的"
    "车辆间距示意图（flowchart-or-schematic）与 Fig. 3 的苜蓿叶立交平面图（map-or-plan-view）例外。",
    "线图一律把图例印在绘图区下方的一条带里（[geometry.legend]=below 在 19 张线图上成立），"
    "图例本身就是变量说明：whole day / peak hours、3 / 4 / 5 lanes、0 / 1 / 2 dedicated lanes。",
    "线图只画左侧与下侧轴线，没有上框和右框，也没有竖直网格线（[geometry.shared_axes]=False，"
    "全篇 [geometry.three_d]=no、[geometry.colorbar]=False）。",
    "每张线图都画标记点并连线，不印数值标签（[geometry.data_labels]=False 全篇成立）；"
    "图内另有一行大标题（如 'Impact of Self-Driving Cars on Average Passing Time'），"
    "与图下的题注不是同一句话。",
    "只有两张示意图在图形内部印标注文字：Fig. 2 的 G_AC / G_AB / G_AD 间距箭头与车辆字母，"
    "Fig. 3 的 Position A-E、Lane 1-4 与两色流量箭头，[geometry.printed_numbers]=True 只在这两张上成立。",
    "结果图成对出现、左右并排，用第二个空位区分整日与高峰：(Whole Day) 在左、(Peak Hours) 在右，"
    "[caption.conditions]=True 在这些成对图上成立，两半的题注合成一行印在下方。",
    "题注只交代画的是什么量，从不下结论（[caption.concludes]=False 在 22 条题注上成立），"
    "并且极短：多数题注连标号只有 4-7 个词（[caption.words]）。",
    "题注位置几乎一律在图的下方（[caption.position]=below），唯一例外是全篇唯一的表 Table 1，"
    "它的题注印在表的上方（[caption.position]=above）。",
    "编号引用密度低：22 个对象里有 6 个从未被正文按编号引用（[mention.count]=0、"
    "[mention.first_page]=None），其余多在首次讨论处引 1-3 次。",
    "两图同句并列引用是常态：'Figure 4 and Figure 5 show the results.'、"
    "'From Figure 14 and Figure 15 ...'，[mention.style] 保留并列写法，两半各记一次。",
    "图可以先印、引用后到：Fig. 8 与 Fig. 12 的首次编号引用都落在图的下一页，"
    "[mention.lead_pages] 因此为负值（-1），记录不把它改写成 0。",
    "引出句只用几个模板：'Figure N shows ...'（[mention.lead_pattern]=figure-n-shows）、"
    "'From Figure N and Figure M, ...'（direct）、'In Figure N, ...' 与 "
    "'The result is shown in Figure N.'（as-shown-in）。",
    "全篇唯一的表走三线表加一条栏首分隔竖线（[table.rule_style]=booktabs），"
    "无斑马纹、无合并单元格（[table.zebra]=False、[table.merged_cells]=False）。",
    "符号表是唯一不编号、不给题注的表：它紧接 2.2 Notations 标题排下，"
    "第一行就是 Symbol/Meaning 栏头（[table.header_rows]=1、[caption.numbering]=none），"
    "25 行符号只给含义不给取值（[table.rows]=26、[table.cols]=2）。",
    "表的规模由速度取值个数决定：栏首列是符号（v、Pa、Pd），后接 7 个速度列，"
    "所以是 3 行 8 列（[table.rows]=3、[table.cols]=8），而不是按工况分行。",
    "表的单位不进表头（[table.units_in_header]=False），概率是无量纲纯数、速度由栏首列符号隐含，"
    "所以 Table 1 是全篇唯一不写单位也不写表注的表（[table.note_sentence] 为空串）。",
    "版面宽度按“图成对/单张”两档：并排两半各占版心一半，单张图占满版心，"
    "[place.area_frac] 在 Fig. 4 与 Fig. 12 上正好差一倍。",
    "图表与节的对应是“一节一对”：3.x 的效果节每节一对（整日/高峰），4.1.x 的实测节也按同样的"
    "整日-高峰配成对或单张，[place.section_path] 逐条记到小节级。",
    "版面索引有系统性偏差：提取器取“该页最后一个标题”，令 Fig 2、4、5、10、11、13、14、15、"
    "17、18、19 全部挂晚一节（[place.section_path] 已按真实印刷标题改正，note 里写明原挂靠），"
    "Fig. 20 则是浮图被推到 5.3 标题之后、实际仍归 5.2。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": [e for e in ALL if "table" not in e],
    "tables": [e for e in ALL if "table" in e],
    "excluded_regions": [],
    "rules": RULES,
    "note": "hand pass",
}

if __name__ == "__main__":
    out = LANE / f".proxy/{PID}-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out} items={len(payload['items'])} tables={len(payload['tables'])} "
          f"rules={len(RULES)}")
