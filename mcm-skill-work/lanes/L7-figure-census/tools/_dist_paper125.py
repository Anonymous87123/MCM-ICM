"""Hand pass for P-C-2017-55261-f877d0a0 (self-driving cars and lane changing, 15 figures, 8 tables).

Shape of the paper: one model chain — flow/density/speed, then a lane-change model, then a
traffic simulation — and every figure follows one of two templates. Nine figures are MATLAB
line plots with the axis titles printed; six are four-panel or three-panel data dumps out of
the traffic simulation, reused verbatim once per highway/road from the body into the appendix.

What the record has to say out loud:

1. The heading index of this paper is broken. `context_extract` found four bogus headings
   ("55261 F1 ________________", "1 X 1", "Appendix", "References"); the whole body is set in
   an unnumbered heading style, so every section path here is recorded as an unnumbered label
   (`section_numbered: false`) built from the real printed heading, never from a fabricated
   number.
2. The paper's own in-text numbering of the three result tables is one higher than the
   printed captions: the sentence "results are tabulated in Tables 4 through 6" introduces
   what is printed as Table 3, Table 4 and Table 5. The citations are counted and quoted as
   the sentence reads; the caption numbers stay as printed.
3. All 23 measured regions are exhibits — 15 figures and 8 tables, no fragments, no rules, no
   code pages. No region is excluded.

Usage: python -I tools/_dist_paper125.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2017-55261-f877d0a0"
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
    (5, 1),
    (7, 1),
    (8, 1),
    (9, 1),
    (12, 1), (12, 2),
    (13, 1),
    (14, 1),
    (15, 1), (15, 2), (15, 3),
    (16, 1),
    (17, 1),
    (18, 1),
    (19, 1),
    (20, 1),
    (23, 1),
    (24, 1),
    (25, 1),
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
           kind: str, legend: str = "none", three_d: str = "no",
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
          kind: str, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
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


# Body headings of this paper are printed unnumbered, and the heading index missed them
# all, so each path component is the real heading text behind an 未编号标题 prefix.
S_ASSUME = ["未编号标题 Assumptions and Justifications"]
S_FD = ["未编号标题 Model Design and Justification",
        "未编号标题 Flow-Density-Mean Speed Relations Model"]
S_LC = ["未编号标题 Model Design and Justification", "未编号标题 Lane Change Model"]
S_LIGHT = S_LC + ["未编号标题 Light Traffic Simulation Results"]
S_MOD = S_LC + ["未编号标题 Moderate Traffic Simulation Results"]
S_HEAVY = S_LC + ["未编号标题 Heavy Traffic Simulation Results"]
S_TEST = ["未编号标题 Model Testing and Error/Sensitivity Analysis"]
S_APP = ["未编号标题 Appendix"]

ALL = [
    figure(4, 1, "line",
           caption("Figure 1: Plot of typical traffic volume versus hour of day from a "
                   "traffic sensor stationed at a Seattle viaduct. Taken from [5].",
                   numbering="Figure N:"),
           mention(4, first=3, style=["Figure 1"], count=2,
                   lead=span(3, "Figure 1 shows", "versus time of day for weekends, "
                             "weekdays, and an average"),
                   pattern="figure-n-shows"),
           path=S_ASSUME, kind="assumption", legend="below",
           note="three series (Average Weekday / Average Day / Average Weekend Day) in one "
                "four-sided frame, horizontal gridlines only; the legend sits in a boxed "
                "strip under the x axis, and neither axis carries a title — the two axis "
                "quantities are named in the prose before the figure instead"),
    table(5, 1,
          caption("Table 1: Constants used in model", numbering="Table N:"),
          mention(5, first=5, style=["Table 1"], count=6,
                  lead=span(5, "Various numerical constants used in our model",
                            "listed in Table 1"),
                  pattern="direct"),
          grid(6, 4, header=1, rules="boxed", numeric=1, txt=3),
          path=S_ASSUME, kind="assumption",
          note="five constants over five body rows plus the header; the only table that "
               "writes units into the body cells ('15 ft', '0.049 ft/mph2', '0.7 sec') "
               "instead of into the header"),
    figure(7, 1, "line",
           caption("Figure 2: Flow versus density for percentage of self-driving/cooperative "
                   "cars P = 0 (blue), 10 (red), 50 (yellow), 90 (purple) and 100 (green).",
                   numbering="Figure N:", cond=True, vars_=1),
           mention(7, first=7, style=["Figures 2 and 3"], count=1,
                   lead="The results are shown in Figures 2 and 3.",
                   pattern="as-shown-in"),
           path=S_FD, kind="model",
           note="five curves in one frame, no legend: the colour-to-P mapping exists only in "
                "the caption; box on with inward ticks on all four sides, no gridlines"),
    figure(8, 1, "line",
           caption("Figure 3: Speed versus density for percentage of self-driving/cooperative "
                   "cars P = 0 (blue), 10 (red), 50 (yellow), 90 (purple) and 100 (green).",
                   numbering="Figure N:", cond=True, vars_=1),
           mention(8, first=7, style=["Figures 2 and 3"], count=1,
                   lead="The results are shown in Figures 2 and 3.",
                   pattern="as-shown-in"),
           path=S_FD, kind="model",
           note="companion of Figure 2: same five colours, same frame and tick style, same "
                "caption template with only the leading quantity changed"),
    figure(9, 1, "line",
           caption("Figure 4: Total derivative in mean speed for [χ = 0.1, f = 0.5] (blue), "
                   "[χ = 0.5, f = 0.1] (red), [χ = 0.5, f = 0.5] (yellow). Number of lanes "
                   "was taken to be constant at 3.",
                   numbering="Figure N:", cond=True, vars_=2, voice="passive"),
           mention(9, first=9, style=["Figure 4"], count=1,
                   lead=span(9, "This result is shown graphically", "in Figure 4"),
                   pattern="as-shown-in", read=1,
                   trail=span(9, "The effect is visibly greatest",
                              "at very low or very high densities")),
           path=S_FD, kind="model",
           note="three curves, all values negative; the plot starts at density ≈50 rather "
                "than at 0 because the derivative is only defined above k_max"),
    table(12, 1,
          caption("Table 2: Input data for lane changing model.", numbering="Table N:"),
          mention(12, first=12, style=["Table 2"], count=1,
                  lead=span(12, "calculated from the flow-density-mean speed model",
                            "shown below in Table 2"),
                  pattern="direct"),
          grid(4, 4, header=1, rules="boxed", units_hdr=True, numeric=3, txt=1),
          path=S_LC, kind="model",
          note="units on a second line inside the header cell, not in a separate unit row"),
    table(12, 2,
          caption("Table 3: Results for light traffic.", numbering="Table N:"),
          mention(12, first=12, style=["Tables 4 through 6"], count=1,
                  lead=span(12, "in the three cases outlined above",
                            "results are tabulated in Tables 4 through 6"),
                  pattern="direct", read=1,
                  trail=span(12, "In Case 3, we use", "to solve tc and other variables")),
          grid(4, 7, header=1, rules="boxed", units_hdr=True, numeric=6, txt=1),
          path=S_LIGHT, kind="result",
          note="the prose numbers this table one higher than its caption: 'results are "
               "tabulated in Tables 4 through 6' introduces what is printed as Tables 3-5"),
    table(13, 1,
          caption("Table 4: Results for moderate traffic.", numbering="Table N:"),
          mention(13, first=12, style=["Tables 4 through 6"], count=1,
                  lead=span(12, "in the three cases outlined above",
                            "results are tabulated in Tables 4 through 6"),
                  pattern="direct", read=1,
                  trail=span(13, "Similarly, we use", "close to dmin for Case 2")),
          grid(4, 7, header=1, rules="boxed", units_hdr=True, numeric=6, txt=1),
          path=S_MOD, kind="result",
          note="same 4x7 boxed template as Table 3 with only the three data rows changed; "
               "its in-text number is one lower than the caption"),
    table(14, 1,
          caption("Table 5: Results for heavy traffic.", numbering="Table N:"),
          mention(14, first=12, style=["Tables 4 through 6", "Table 5"], count=2,
                  lead=span(12, "in the three cases outlined above",
                            "results are tabulated in Tables 4 through 6"),
                  pattern="direct", read=1,
                  trail=span(14, "wish to measure the effect",
                             "when an event such as this occurs")),
          grid(4, 7, header=1, rules="boxed", units_hdr=True, numeric=6, txt=1),
          path=S_HEAVY, kind="result",
          note="third copy of the 4x7 result template; the only one of the three also named "
               "again in its own section ('we obtain the results shown in Table 5')"),
    table(15, 1,
          caption("Table 6: Part one of simulation results.", numbering="Table N:"),
          mention(15, first=15, style=["Tables 6 through 8"], count=1,
                  lead=span(15, "the results and effects for Case 1",
                            "shown in the following tables"),
                  pattern="direct", read=1,
                  trail=span(15, "We can see from Tables 6 through 8",
                             "a queue results from merging in Case 1")),
          grid(4, 5, header=1, rules="boxed", units_hdr=True, numeric=4, txt=1),
          path=S_HEAVY, kind="result",
          note="first of the three-part shock-wave table; keeps the heavy-traffic section "
               "as its parent because no new heading stands above it"),
    table(15, 2,
          caption("Table 7: Part two of simulation results.", numbering="Table N:"),
          mention(15, first=15, style=["Tables 6 through 8"], count=1,
                  lead=span(15, "the results and effects for Case 1",
                            "shown in the following tables"),
                  pattern="direct", read=1,
                  trail=span(15, "We can see from Tables 6 through 8",
                             "a queue results from merging in Case 1")),
          grid(4, 6, header=1, rules="boxed", units_hdr=True, numeric=5, txt=1),
          path=S_HEAVY, kind="result",
          note="six columns as printed in the text layer (Traffic type, u0, k0, q0, uw, ug)"),
    table(15, 3,
          caption("Table 8: Part three of simulation results.", numbering="Table N:"),
          mention(15, first=15, style=["Tables 6 through 8"], count=1,
                  lead=span(15, "the results and effects for Case 1",
                            "shown in the following tables"),
                  pattern="direct", read=1,
                  trail=span(15, "We can see from Tables 6 through 8",
                             "a queue results from merging in Case 1")),
          grid(4, 5, header=1, rules="boxed", units_hdr=True, numeric=4, txt=1),
          path=S_HEAVY, kind="result",
          note="the two right-hand headers print q/q0 and k/k0 as stacked fractions inside "
               "one cell each, so the header stays a single row and no cell is merged; "
               "the text layer splits those fractions into a stray 'q0 k0' line"),
    figure(16, 1, "line",
           caption("Figure 5: Branches of q − u curve.", numbering="Figure N:", vars_=2),
           mention(16, first=15, style=["Figure 5"], count=2,
                   lead=span(15, "the upper half of the q − u curve", "shown in Figure 5"),
                   pattern="as-shown-in", read=1,
                   trail=span(16, "Upon analyzing the empirical flow data",
                              "predicted by the curve in Figure 5")),
           path=S_TEST, kind="test",
           note="one continuous curve (upper and lower branch of the same relation) plus one "
                "dashed guide line; the two bold labels sit next to black arrows, there is no "
                "legend and no printed numeric value anywhere on the axes"),
    figure(17, 1, "line",
           caption("Figure 6: Example of expected deviation in flow distribution curve "
                   "arising from transition to lower branch of q − u curve, indicated by "
                   "arrow.", numbering="Figure N:", vars_=2, voice="passive"),
           mention(17, first=16, style=["Figure 6"], count=1,
                   lead=span(16, "in the flow distribution curve, for example",
                             "shown in Figure 6"),
                   pattern="direct"),
           path=S_TEST, kind="test",
           note="schematic companion of Figure 5: heavy stroke, L-shaped frame (two spines "
                "only), one arrow pointing at the deviation"),
    figure(18, 1, "scatter",
           caption("Figure 7: Traffic flux along Interstate 5, (a) Northbound, 12:50am; (b) "
                   "North- bound, 1:50pm; (c) Southbound, 12:50am; (d) Southbound, 1:50pm",
                   numbering="Figure N:", cond=True),
           mention(18, first=16, style=["Figures 7 and 8", "Figures 7 b and d"], count=2,
                   lead="Several representative plots are shown in Figures 7 and 8.",
                   pattern="as-shown-in"),
           path=S_TEST, kind="test", panels=4, layout="2x2",
           note="four scatter panels in two rows; panel (d) carries its own y range while "
                "a-c share one; no legend"),
    figure(19, 1, "line",
           caption("Figure 8: (a) Traffic flux; (b) Traffic flow; (c) Space mean speed over "
                   "the course of a 24-hour period at mile marker 155.18 on I-5 North. "
                   "Dashed red lines indicate the point at which empirical data exceed the "
                   "maximum prediction of our model.",
                   numbering="Figure N:", cond=True, voice="active"),
           mention(19, first=16, style=["Figures 7 and 8", "Figure 8 b"], count=2,
                   lead="Several representative plots are shown in Figures 7 and 8.",
                   pattern="as-shown-in", read=1,
                   trail=span(17, "As shown in Figure 8 b",
                              "throughout the day at most times")),
           path=S_TEST, kind="test", panels=3, layout="column of 3",
           note="three stacked panels with independent y axes; the dashed red line marks "
                "where the data leave the model's range"),
    figure(20, 1, "line",
           caption("Figure 9: Sensitivity of the proposed us vs k relationship to variations "
                   "from baseline values for (a) A; (b) trxn ; (c) dcar + dzero ; (d) uf ; and "
                   "(e) L. Values progress through 0, 50, 100, 150, and 200% of their "
                   "baseline values in the order blue, red, yellow, purple, green.",
                   numbering="Figure N:", cond=True, vars_=2, voice="active"),
           mention(20, first=20, style=["Figure 9"], count=1,
                   lead=span(20, "Results are depicted graphically", "curves in Figure 9"),
                   pattern="as-shown-in", read=1,
                   trail=span(20, "The behavior of these graphs",
                              "reflects common sense intuition")),
           path=S_TEST, kind="test", panels=5, layout="3 rows (2+2+1)",
           note="five one-parameter panels in rows of 2+2+1; every panel carries its own pair "
                "of axis titles, panel (e) alone runs to x=1400 and panel (d) to y=140, and "
                "the value-to-colour mapping (0/50/100/150/200%) exists only in the caption, "
                "so no panel prints a legend"),
    figure(23, 1, "scatter",
           caption("Figure 10: Traffic flux along Interstate 90, (a) Eastbound, 12:50am; (b) "
                   "East- bound, 1:50pm; (c) Westbound, 12:50am; (d) Westbound, 1:50pm",
                   numbering="Figure N:", cond=True),
           mention(23, first=None, style=[], count=0),
           path=S_APP, kind="appendix", panels=4, layout="2x2",
           note="appendix copy of the Figure 7 template for a second highway; zero numbered "
                "citations — the body only says 'additional figures ... are shown in the "
                "appendix'"),
    figure(24, 1, "line",
           caption("Figure 11: (a) Traffic flux; (b) Traffic flow; (c) Space mean speed over "
                   "the course of a 24-hour period at mile marker 14.32 on I-90 East. Dashed "
                   "red lines indicate the point at which empirical data exceed the maximum "
                   "prediction of our model.",
                   numbering="Figure N:", cond=True, voice="active"),
           mention(24, first=None, style=[], count=0),
           path=S_APP, kind="appendix", panels=3, layout="column of 3",
           note="appendix copy of the Figure 8 template; the only change across copies is "
                "the mile marker in the caption"),
    figure(25, 1, "scatter",
           caption("Figure 12: Traffic flux along Interstate 405, (a) Northbound, 12:50am; "
                   "(b) Northbound, 1:50pm; (c) Southbound, 12:50am; (d) Southbound, 1:50pm",
                   numbering="Figure N:", cond=True),
           mention(25, first=None, style=[], count=0),
           path=S_APP, kind="appendix", panels=4, layout="2x2",
           note="third copy of the four-panel flux template; here all four panels are drawn "
                "with identical per-panel limits"),
    figure(26, 1, "line",
           caption("Figure 13: (a) Traffic flux; (b) Traffic flow; (c) Space mean speed over "
                   "the course of a 24-hour period at mile marker 15.76 on I-405 North. "
                   "Dashed red lines indicate the point at which empirical data exceed the "
                   "maximum prediction of our model.",
                   numbering="Figure N:", cond=True, voice="active"),
           mention(26, first=None, style=[], count=0),
           path=S_APP, kind="appendix", panels=3, layout="column of 3",
           note="third copy of the three-panel template"),
    figure(27, 1, "scatter",
           caption("Figure 14: Traffic flux along State Road 520, (a) Eastbound, 12:50am; (b) "
                   "Eastbound, 1:50pm; (c) Westbound, 12:50am; (d) Westbound, 1:50pm",
                   numbering="Figure N:", cond=True),
           mention(27, first=None, style=[], count=0),
           path=S_APP, kind="appendix", panels=4, layout="2x2",
           note="fourth copy of the four-panel flux template"),
    figure(28, 1, "line",
           caption("Figure 15: (a) Traffic flux; (b) Traffic flow; (c) Space mean speed over "
                   "the course of a 24-hour period at mile marker 5.39 on SR-520 East. Dashed "
                   "red lines indicate the point at which empirical data exceed the maximum "
                   "prediction of our model.",
                   numbering="Figure N:", cond=True, voice="active"),
           mention(28, first=None, style=[], count=0),
           path=S_APP, kind="appendix", panels=3, layout="column of 3",
           note="fourth copy of the three-panel template"),
]

RULES = [
    "全篇只有两类图：MATLAB 折线图（[geometry.family]=line，Fig. 1–6、8–9、11、13、15）与"
    "交通仿真的多子图散布图（[geometry.family]=scatter，Fig. 7、10、12、14），没有三维图、"
    "没有热图、没有照片，[geometry.three_d]=no 在 15 张图上全部成立。",
    "数据图一律不印图例，颜色靠题注点名：[geometry.legend]=none 在 14 张图上成立，"
    "Fig. 2/3 的五条曲线只用题注里的 (blue)(red)(yellow)(purple)(green) 对应 P 值。",
    "唯一的例外是 Fig. 1，图例印在横轴下方的方框里（[geometry.legend]=below），"
    "因为它是从外部文献借来的图，不是本稿自己的作图模板。",
    "多子图一律按固定格式成组：要么四联 2×2（[geometry.panel_count]=4，"
    "[geometry.panel_layout]=2x2），要么竖排三联（[geometry.panel_count]=3，"
    "[geometry.panel_layout]=column of 3），从不出现第三种排布。",
    "四联图切分的是“方向×时段”，题注用 (a)…(d) 分列并把 12:50am 与 1:50pm 成对写出，"
    "所以 [caption.conditions]=True；竖排三联切分的是"
    "“交通流量/交通流密度/空间平均速度”，[caption.verbatim] 里 (a)(b)(c) 三段固定就位。",
    "竖排三联的各段独立纵轴，[geometry.shared_axes]=False；只有 Fig. 12 的四联把四格"
    "强制成同一坐标范围，其余四联允许某格（Fig. 7 的 (d)）单独换 y 范围。",
    "题注模板是“量 vs 量 for 参数=值 (颜色)”：Fig. 2/3/4 的题注先给坐标量再逐色列参数，"
    "[caption.variables]=True 且 [caption.variable_count]=2。",
    "正文引用集中在首次出现处，句式是 “Figure N shows …”（[mention.lead_pattern]="
    "figure-n-shows）或 “shown in Figure N”（as-shown-in）；附录 6 张图的 [mention.count]=0、"
    "[mention.first_page]=None，正文只用一句无编号的 additional figures 带过。",
    "两图同句引用时用复数并列：“Figures 2 and 3”、“Figures 7 and 8”，[mention.style] 保留复数写法，"
    "两张图各记 1 次，不因并列而少记。",
    "表一律满框细线全格网：外框加内部横竖线，[table.rule_style]=boxed 八张表一致，"
    "无斑马纹（[table.zebra]=False）、无合并单元格（[table.merged_cells]=False）、"
    "无对角表头（[table.diagonal_header]=False）。",
    "单位写在表头括号内（[table.units_in_header]=True，Table 2–8 全部）；"
    "Table 1 是唯一把单位随数值写进单元格的表。",
    "表的宽度一律占满版心（[table.width]=full），全部竖版（[table.orientation]=portrait），"
    "没有续表（[table.continued]=False）、没有表注行（[table.note_sentence] 为空串）。",
    "图的题注全部印在图的下方（[caption.position]=below），编号格式是 “Figure N:” 与 "
    "“Table N:”（[caption.numbering]），没有一张图把题注放在上方。",
    "结果表按节复制同一张模板：Light/Moderate/Heavy 三张表是同一个 4×7 格网"
    "（[table.rows]=4、[table.cols]=7），只换三行数据；正文给它们的编号比题注高一位，"
    "属原稿编号错误，[table.header_rows] 因此一律为 1。",
    "章节与图的配对是“一节一套”：假设节只放 1 张外部借图与 1 张常数表，流密速模型节放 3 张"
    "折线，变道节放 1 张输入表加 3 张结果表加 3 张冲击波表，检验节放 2 张曲线图、4 张实测图"
    "与 1 张灵敏度图，附录只放实测图副本（[place.section_path] 逐条记录，"
    "对应 [place.section_kind]=assumption/model/result/test/appendix）。",
    "图宽随子图数反向变化：单张折线图占满版心，四联图收窄到约 309pt，竖排三联最窄只占约 "
    "172pt（[place.area_frac] 在 Fig. 7 与 Fig. 8 上即可看出这一档差），"
    "所以“子图越多、图越窄”是这套模板的版面规律，不是排字失误。",
    "引出句只有固定几个句式，全部走 [mention.lead_sentence]：复数并列的 "
    "“The results are shown in Figures 2 and 3.”、指示式的 “This result is shown graphically "
    "… in Figure 4”、整组的 “Several representative plots are shown in Figures 7 and 8.”、"
    "以及表的 “results are tabulated in Tables 4 through 6”。",
    "读句跟在结果表之后、以 We 起头，一句覆盖三张表（[mention.trail_sentence]），"
    "所以 Table 6/7/8 共用同一句读句，[mention.read_sentences]=1；图后的读句则是 "
    "“The behavior of these graphs reflects common sense intuition”。",
    "附录图的衔接不靠编号：6 张副本的 [mention.count]=0、[mention.first_page]=None，"
    "正文只在检验节末尾用一句无编号的 “Additional figures for other highways are shown in "
    "the appendix.” 交代位置。",
    "全篇题注都不下结论：[caption.concludes]=False 在 23 条题注上成立；题注只交代画的是什么、"
    "参数取哪些值，判断留给正文，比如 Fig. 2 的题注只列五条曲线对应的 P 值。",
    "本稿正文标题不编号，[place.section_numbered]=False 在 23 条记录上全部成立，"
    "section_path 用“未编号标题 <真实标题>”承载；`1 X 1`、`55261 F1 ________________` "
    "这类由提取器造出来的假标题不得写进路径。",
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
