"""Hand pass for P-C-2017-55583-34388031 (cell-automaton model, self-driving share, 12 figures + 1 table).

Shape of the paper: assumptions and a notation table, then the CA model with two schematics
and one flow chart, then two simulation chapters that turn the model into effects on velocity
and equilibria, then the dedicated-lane assessment.

What the record has to say out loud:

1. The paper is one drawing template used twice. 4.1 prints three line charts with no legend
   at all; from 4.2 on every line chart carries its legend inside the plot frame. That switch
   is the only template change in the paper.
2. Fig 7 is a four-panel plan view in which the colour, not an axis, carries the value: each
   panel has its own jet colour bar, 0 to 25+, and the cell colour is the real-time speed of
   that road section. It is the only colour-scaled exhibit and the only multi-panel exhibit.
3. Captions print under the exhibit everywhere except Fig 2, whose caption sits above it as
   the first line of its page.
4. Seven of the twelve figures are cited one page *before* they print, because the figure is
   floated to the head of the next page; lead_pages is +1, never 0.
5. The layout pass attaches nine of the sixteen measured regions one section late, and drops
   the 4.1 heading entirely, so Fig 3's path is carried as an unnumbered path and every
   corrected attachment names the misattachment in its note.
6. Two extractor defects surfaced here and were repaired before this record was written: a
   long notation table whose closing rule sat past TABLE_GAP_PT was never measured, and an
   image block whose own white margin spans its caption was deleted as a caption box. Both
   are documented as rule change 7 in the lane README.

Usage: python -I tools/_dist_paper127.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2017-55583-34388031"
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
    (7, 1),
    (9, 1), (9, 2),
    (10, 1),
    (13, 1),
    (14, 1), (14, 2),
    (16, 1),
    (17, 1), (17, 2), (17, 3), (17, 4),
    (18, 1),
    (19, 1), (19, 2),
    (20, 1),
    (21, 1),
]

EXCLUDED = [
    {
        "page": 28,
        "bbox": REG[(28, 1)],
        "reason": "not-an-exhibit",
        "note": "the appendix page's heading band: the running header, a full-width rule and the "
                "word end as the document-end marker. Nothing is drawn.",
    },
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


def place(page: int, idx: int, path: list[str], kind: str, numbered: bool = True) -> dict:
    b = REG[(page, idx)]
    mid = (b[1] + b[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    same = [k for k in ORDER if k[0] == page]
    frac = (b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H)
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": ORDER.index((page, idx)) + 1,
        "page_order": same.index((page, idx)) + 1,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": frac > 0.5,
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
           kind: str, legend: str = "none", printed: bool = False,
           labels: bool = False, panels: int = 1, layout: str = "1",
           shared: bool = False, colorbar: bool = False, note: str = "",
           numbered: bool = True, of: int | None = None) -> dict:
    out = {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, idx, path, kind, numbered),
        "mention": men,
        "caption": cap,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": "no",
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }
    if of is not None:
        out["is_panel_of"] = of
    return out


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


P_ASSUME = ["2 Assumptions and Notations"]
P_NOTES = P_ASSUME + ["2.2 Notations"]
P_MODEL = ["3 Model Construction"]
P_31 = P_MODEL + ["3.1 The self-driving, cooperating car model"]
P_32 = P_MODEL + ["3.2 The mixed, dynamic road model"]
P_41 = ["未编号标题 4 Model Extension and Simulation Analysis",
        "未编号标题 4.1 Problem1: The effects of auto-driving cars in traffic network"]
P_EXT = ["4 Model Extension and Simulation Analysis"]
P_411 = P_EXT + ["4.1.1 Car Velocity/Performance v"]
P_412 = P_EXT + ["4.1.2 Space Daily Equilibria 1/σs2"]
P_42 = P_EXT + ["4.2 Problem2: The different effects on peak/average hours"]
P_421 = P_42 + ["4.2.1 Traffic Density Distribution of Time"]
P_422 = P_42 + ["4.2.2 Simulation"]
P_43 = P_EXT + ["4.3 Problem3: Dedicated lane assessment"]

MISATTACH = ("the layout pass attaches this region to the last heading printed above it, which is "
             "one section late; the true printed section is ")

ALL = [
    table(7, 1,
          caption("Table 1: Notations.", numbering="Table N:"),
          mention(7, first=None, style=[], count=0),
          grid(15, 3, header=1, rules="booktabs", txt=3),
          path=P_NOTES, kind="symbols",
          note="one header row (Symbol / Definition / Notes) and 14 data rows with a blank "
               "spacer line after the traffic-count row; three horizontal rules and no vertical "
               "rule at all, so it is booktabs style even though the paper's figures are not"),
    figure(9, 1, "flowchart-or-schematic",
           caption("Figure 1: The difference between self-driving and non-self-driving cars in "
                   "face of emergency situations"),
           mention(9, first=9, style=["Figure 1(a)", "Figure 1(b)"], count=2,
                   lead=span(9, "When two cars", "former car"), pattern="as-shown-in", read=2,
                   trail="they can always react in time when the speed of the former car changes"),
           path=P_31, kind="model", printed=True, panels=1, layout="row of 2",
           note="left panel (a): two road lines at t=t0 and t=t1 with one car rectangle each and "
                "a double-headed arrow labelled safe interval. Pure line work, no axes, no "
                "legend; the panel label prints under the drawing, outside the measured bbox"),
    figure(9, 2, "flowchart-or-schematic",
           caption("Figure 1: The difference between self-driving and non-self-driving cars in "
                   "face of emergency situations"),
           mention(9, first=9, style=["Figure 1(a)", "Figure 1(b)"], count=2,
                   lead=span(9, "When two cars", "former car"), pattern="as-shown-in", read=2,
                   trail="they can always react in time when the speed of the former car changes"),
           path=P_31, kind="model", printed=True, panels=1, layout="row of 2", of=1,
           note="right panel (b) of the same exhibit, recorded as its own region because the two "
                "halves are separate image blocks; the shared caption prints once, under the "
                "pair, so this entry repeats it" + MISATTACH + "3.1, not 3.2"),
    figure(10, 1, "flowchart-or-schematic",
           caption("Figure 2: The Cellular Automaton based road model", pos="above"),
           mention(10, first=9, style=["Figure2", "Figure 2"], count=2,
                   lead=span(9, "The following Figure2 shows", "used in our paper"),
                   pattern="direct", read=1,
                   trail="As shown in Figure 2, the yellow-colored blocks represents the "
                         "self-driving cars and the blue-colored blocks represent the "
                         "non-self-driving cars"),
           path=P_32, kind="model", legend="above", printed=False,
           note="the model's data structure drawn as a road: about 20 cell columns by 8 rows "
                "between two solid bands, cells filled yellow, blue or white, with a two-swatch "
                "legend printed ABOVE the grid. The caption also prints above, as the first line "
                "of the page, which makes this the only exhibit in the paper captioned on top"),
    figure(13, 1, "flowchart-or-schematic",
           caption("Figure 3: The flow chart indicating how we decide the velocity and position "
                   "of the car in next second"),
           mention(13, first=12, style=["Figure 3"], count=1,
                   lead=span(12, "Then we use the procedure showed in Figure 3",
                             "change in the next second"), pattern="direct", read=1),
           path=P_41, kind="model", printed=True, numbered=False,
           note="three decision diamonds and three assignment boxes with YES/NO edge labels, "
                "blue fills only; a true flow chart, not a road drawing. Its section, "
                "4.1 Problem1, is printed on page 12 but the heading index drops it entirely, so "
                "the path is carried unnumbered rather than pushed down into 4.1.1" + MISATTACH +
                "4.1, not 4.1.2"),
    figure(14, 1, "line",
           caption("Figure 4: Car velocity v versus self-driving ratio", vars_=2),
           mention(14, first=13, style=["Figure 4"], count=2,
                   lead="the 10%, 50%, 90% is emphasized in the Figure 4",
                   pattern="as-shown-in", read=1,
                   trail=span(13, "From the result, we can safely come", "percentage raises")),
           path=P_411, kind="result",
           note="single blue line, no legend, and the three sampled percentages are marked by "
                "enlarged circles rather than by extra series; vertical gridlines only, L-shaped "
                "frame, printed axis titles. First of the three pre-template charts"),
    figure(14, 2, "line",
           caption("Figure 5: Space daily variance σs2 versus self-driving ratio", vars_=2),
           mention(14, first=13, style=["Figure 5", "Figure5"], count=3,
                   lead="Figure 5 below shows the simulation results.",
                   pattern="figure-n-shows", read=1,
                   trail=span(13, "the car velocity variance decreases steadily",
                             "percent- age raises")),
           path=P_412, kind="result",
           note="same template as Figure 4: one blue curve, no legend, merged dots, vertical "
                "gridlines only. The in-text spelling loses the space ('Figure5') while the "
                "caption keeps it"),
    figure(16, 1, "line",
           caption("Figure 6: The traffic density function versus time", vars_=2),
           mention(16, first=15, style=["Figure6"], count=1,
                   lead="the function graph is shown in Figure6",
                   pattern="as-shown-in", read=1),
           path=P_421, kind="result",
           note="one smooth curve with no markers at all, which is how a fitted function is drawn "
                "rather than a simulation result; no legend, vertical gridlines only. Last of the "
                "three legend-less charts"),
    figure(17, 1, "heatmap-or-contour",
           caption("Figure 7: The difference between self-driving and non-self-driving cars when "
                   "in face of emergency situations"),
           mention(17, first=16, style=["Figure 7"], count=2,
                   lead=span(16, "In Figure 7, we use different colors", "real-time car velocity"),
                   pattern="direct", read=2,
                   trail=span(16, "As we can see from the graphs in Figure 7",
                             "traffic pressure at peak hours")),
           path=P_422, kind="result", colorbar=True, panels=1, layout="2x2",
           note="panel (a), no self-driving car. Four abstracted roads drawn as coloured cells "
                "with a jet colour bar at the right (0 to 25+, red is slow, blue is fast); the "
                "colour is the value, so there is no axis and no legend. Row-major order puts "
                "(a) top-left, (b) top-right, (c) bottom-left, (d) bottom-right"),
    figure(17, 2, "heatmap-or-contour",
           caption("Figure 7: The difference between self-driving and non-self-driving cars when "
                   "in face of emergency situations"),
           mention(17, first=16, style=["Figure 7"], count=2,
                   lead=span(16, "In Figure 7, we use different colors", "real-time car velocity"),
                   pattern="direct", read=2,
                   trail=span(16, "As we can see from the graphs in Figure 7",
                             "traffic pressure at peak hours")),
           path=P_422, kind="result", colorbar=True, panels=1, layout="2x2", of=8,
           note="panel (b), 10% self-driving: the same four roads, still mostly red and orange, "
                "same colour bar. Recorded as its own region because the four panels are four "
                "separate image blocks under one caption"),
    figure(17, 3, "heatmap-or-contour",
           caption("Figure 7: The difference between self-driving and non-self-driving cars when "
                   "in face of emergency situations"),
           mention(17, first=16, style=["Figure 7"], count=2,
                   lead=span(16, "In Figure 7, we use different colors", "real-time car velocity"),
                   pattern="direct", read=2,
                   trail=span(16, "As we can see from the graphs in Figure 7",
                             "traffic pressure at peak hours")),
           path=P_422, kind="result", colorbar=True, panels=1, layout="2x2", of=8,
           note="panel (c), 50% self-driving: the cells turn deep blue, which is the whole point "
                "of the sequence; same colour bar, and its lowest tick is clipped by the bbox"),
    figure(17, 4, "heatmap-or-contour",
           caption("Figure 7: The difference between self-driving and non-self-driving cars when "
                   "in face of emergency situations"),
           mention(17, first=16, style=["Figure 7"], count=2,
                   lead=span(16, "In Figure 7, we use different colors", "real-time car velocity"),
                   pattern="direct", read=2,
                   trail=span(16, "As we can see from the graphs in Figure 7",
                             "traffic pressure at peak hours")),
           path=P_422, kind="result", colorbar=True, panels=1, layout="2x2", of=8,
           note="panel (d), 90% self-driving: almost uniformly deep blue with one white cell. The "
                "four panels share one caption printed under the second row, next to the (c)/(d) "
                "panel labels"),
    figure(18, 1, "line",
           caption("Figure 8: The car velocity versus self-driving car percentage under different "
                   "den- sity conditions.", cond=True, vars_=2),
           mention(18, first=17, style=["Figure 8"], count=1,
                   lead=span(17, "From Figure 8", "the most obvious"),
                   pattern="direct", read=1),
           path=P_422, kind="result", legend="inside",
           note="first chart of the second template: three series (three density conditions) with "
                "a legend inside the plot at the lower right. The caption keeps the column-break "
                "hyphenation ('den- sity') verbatim" + MISATTACH + "4.2.2, not 4.2.3"),
    figure(19, 1, "line",
           caption("Figure 9: The velocity variance to time versus self-driving ratio.", vars_=2),
           mention(19, first=18, style=["Figure 9", "Figure9"], count=2,
                   lead="The corresponding curve is shown in Figure 9.",
                   pattern="as-shown-in", read=1,
                   trail=span(18, "From Figure9, we can clearly observe",
                             "decreases as the percent- age increases")),
           path=P_422, kind="result", legend="inside",
           note="two series, legend inside the plot at the upper right; vertical gridlines only" +
                MISATTACH + "4.2.2, not 4.2.3"),
    figure(19, 2, "line",
           caption("Figure 10: The car velocity variance to space versus time under different "
                   "self- driving ratios.", cond=True, vars_=3),
           mention(19, first=18, style=["Figure10"], count=2,
                   lead="The corresponding curve is shown in Figure10.",
                   pattern="as-shown-in", read=1,
                   trail=span(18, "From Figure10, the", "the percentage increases too")),
           path=P_422, kind="result", legend="inside",
           note="four series, one per self-driving ratio with the 0% line as reference, legend "
                "inside at the right; the only variance-versus-time chart in the paper, so its x "
                "axis is hours rather than a percentage" + MISATTACH + "4.2.2, not 4.2.3"),
    figure(20, 1, "line",
           caption("Figure 11: The car velocity versus self-driving ratio when there are lanes "
                   "dedi- cated to self-driving cars.", vars_=2),
           mention(20, first=20, style=["Figure 11"], count=1,
                   lead="The average car velocity performance is shown in Figure 11.",
                   pattern="as-shown-in", read=1),
           path=P_43, kind="evaluation", legend="inside",
           note="two series, with and without dedicated lanes, legend inside at the centre-right; "
                "the caption keeps the column-break hyphenation ('dedi- cated')"),
    figure(21, 1, "line",
           caption("Figure 12: The car velocity versus self-driving car percentage when there are "
                   "lanes dedicated to self-driving cars.", vars_=2),
           mention(21, first=20, style=["Figure 12"], count=1,
                   lead=span(20, "Also, the space daily equilibria performance is shown in Figure 12",
                             "Figure 12"),
                   pattern="as-shown-in", read=1),
           path=P_43, kind="evaluation", legend="inside",
           note="two series that cross near 70%, which is the crossing the text reads as the 68% "
                "dedicated-lane threshold" + MISATTACH + "4.3, not 4.3.1"),
]

RULES = [
    "全篇只有两种对象：折线图（[geometry.family]=line，8 张）与示意图（4 条记录都是 "
    "flowchart-or-schematic：Fig 1 的两半、图 2 的元胞网格、图 3 的流程图，另加 1 组 4 联 "
    "heatmap-or-contour），没有柱、没有散点、没有三维图（[geometry.three_d]=no 在全部记录上成立）。",
    "折线图每张只画 1-4 条曲线、单面板（[geometry.panel_count]=1 在 16 条记录上成立），"
    "四联只出现在 Fig 7（[geometry.panel_layout]=2x2）。",
    "折线图一律蓝线加点，抽样百分比靠放大圆点标注而不靠加曲线，所以全篇不印数值标签"
    "（[geometry.data_labels]=False 在 8 张折线图上成立）。",
    "模板在 4.2 处换代：4.1 的三张图（Fig 4/5/6）完全不印图例（[geometry.legend]=none），"
    "4.2 以后每张折线图都把图例印在图内（[geometry.legend]=inside，5 张），这是全篇唯一一次换模板。",
    "示意图是唯一的纯线框加印字对象：t=t0/t1、safe interval、YES/NO 都印在图上"
    "（[geometry.printed_numbers]=True 只在 Fig 1/2/3 的 3 条记录上成立）。",
    "只有 Fig 7 用颜色而不是坐标轴承载数值，右侧 jet 色标 0 到 25+ 编码该路段实时车速"
    "（[geometry.colorbar]=True 只在 Fig 7 的 4 个面板上成立）。",
    "题注一律印在图的下方（[caption.position]=below），唯一例外是 Fig 2，它的题注印在图上、"
    "成为该页第一行文字（[caption.position]=above）。",
    "题注只给量名与条件，从不下结论（[caption.concludes]=False 在 13 条题注上成立），"
    "编号格式统一 Figure N: 与 Table N:（[caption.numbering]），词数多为 6-14 词（[caption.words]）。",
    "题注里点变量的方式固定：先说纵轴再 versus 横轴（[caption.variables]=True 且 "
    "[caption.variable_count]=2 在 7 条题注上成立），条件写在 under different … 从句里"
    "（[caption.conditions]=True 在 Fig 8 与 Fig 10 上成立）。",
    "表只有一张，是符号表：单表头行加 14 行数据（[table.rows]=15、[table.cols]=3、"
    "[table.header_rows]=1），只有横线、无竖线、无斑马纹、无合并单元格"
    "（[table.rule_style]=booktabs、[table.zebra]=False、[table.merged_cells]=False）。",
    "单位不写在表头而是写进 Notes 列（[table.units_in_header]=False），所以表里没有可对齐的"
    "小数列（[table.numeric_cols]=0、[table.decimal_aligned]=False），全表占满版心"
    "（[table.width]=full）。",
    "引用密度低：13 个对象里只有 Table 1 从未被按编号引用（[mention.count]=0、"
    "[mention.first_page]=None），其余每张图被引 1-3 次（[mention.count]）。",
    "图被整块浮到下一页页首，所以引用几乎都落在图的上一页：[mention.lead_pages]=1 在 13 张图上成立"
    "（除 Fig 1 两半与 Fig 11 外全部），只有这两处图与引用同页。",
    "引出句只有一个模板：the corresponding curve is shown in Figure N 与 …performance is shown in "
    "Figure N（[mention.lead_pattern]=as-shown-in 在 8 条记录上成立），读句一律以 From Figure N 起头"
    "（[mention.trail_sentence]）。",
    "图与节一对一，敏感性分析节一张图都不放：4.1.1 与 4.1.2 各 1 张折线、4.2.1 放分布曲线、"
    "4.2.2 放 1 组四联加 3 张折线、4.3 放 2 张（[place.section_path]、[place.section_kind]），"
    "4.1.3 与 4.2.3 与 4.3.1 三节没有自己的图。",
    "版面索引有系统性偏差：p9 挂到 3.2、p13 挂到 4.1.2、p16 挂到 4.2.2、p18 与 p19 挂到 4.2.3、"
    "p21 挂到 4.3.1，都是取“该页最后一个标题”造成的晚挂一节；4.1 的标题（p12）提取器整条漏掉，"
    "Fig 3 因此用 [place.section_numbered]=False 的未编号路径承载，真实归属仍写在路径里。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": [e for e in ALL if "table" not in e],
    "tables": [e for e in ALL if "table" in e],
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": "hand pass",
}

if __name__ == "__main__":
    out = LANE / f".proxy/{PID}-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out} items={len(payload['items'])} tables={len(payload['tables'])} "
          f"excluded={len(EXCLUDED)} rules={len(RULES)}")
