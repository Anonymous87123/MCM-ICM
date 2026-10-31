"""Hand pass for P-C-2010-8048-a080a4e2 (marine debris / monk seal, 14 figures + 1 table).

Single-column text, but every float is set as a small half-width panel and the page pairs
two of them side by side, so five of the twenty measured regions are raster copies of the
vector chart next to them (p3 r2, p6 r3, p9 r2/r4/r6). Those are excluded as fragments;
the vector region is the exhibit.

Figure grammar is Excel-throughout: column charts, plain line charts of two or three
series, and three perspective 3D column charts (Figure 8 and the two square panels of
Figures 12-13). Five diagrams are drawn from rectangles with arrowed links, including two
hierarchy trees (Figures 9-10) and the input-output / feedback pair (Figures 1 and 14).

Callouts are thin and formulaic: "as show in Fig.2", "showed in Fig.14", "show in Fig.5",
plus one "Figure 4 shows" and one parenthetical "(Fig.1)" / "(Show in Fig.3)". The
comparison panels 11-13 are cited as a range twice, once before and once after.

Two sub-headings, 3.1 and 3.2, hold Figures 3-6 but the context extractor did not pick
their titles up (they carry inline maths), so those floats are placed under their parent
heading "3 Model for Impacts on Ocean Ecosystem"; the missing titles are recorded in the
record note rather than guessed into the path.

Usage: python -I tools/_dist_paper12.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2010-8048-a080a4e2"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
REG = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: x["bbox"][1]), 1):
        REG[(pg["page"], i)] = r["bbox"]

PAGE_W, PAGE_H = 595.32, 841.92

README_ORDER = [
    (2, 1), (3, 1), (3, 2),
    (5, 2), (5, 1), (5, 4), (5, 3),
    (6, 2), (6, 1), (6, 3),
    (7, 1), (7, 2), (7, 3),
    (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6),
    (10, 1),
]

H_DESC = "2 Description and Analysis"
H_MODEL = "3 Model for Impacts on Ocean Ecosystem"
H_RES = "3.3 Result Analysis"
H_EVAL = "4 Ocean System Evaluation Model"
H_AHP = "4.1 Analytical Hierarchy Process"
H_R43 = "4.3 Result"
H_FB = "4.5 Feedback Ocean System"


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


def zone(page: int, idx: int) -> tuple[str, float, int]:
    bbox = REG[(page, idx)]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    area = round((bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (PAGE_W * PAGE_H), 3)
    same = [k for k in README_ORDER if k[0] == page]
    return z, area, same.index((page, idx)) + 1


def place(page: int, idx: int, path: list[str], kind: str) -> dict:
    z, area, order = zone(page, idx)
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": README_ORDER.index((page, idx)) + 1,
        "page_order": order,
        "page_zone": z,
        "area_frac": area,
        "solo_page": False,
    }


def caption(v: str, numbering: str, position: str, *, units: bool = False,
            vars_: int = 0, cond: bool = False, concl: bool = False,
            voice: str = "none") -> dict:
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
        "position": position,
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


def figure(page: int, idx: int, family: str, cap: dict, men: dict, *,
           path: list[str], kind: str, legend: str = "none", three_d: str = "no",
           printed: bool = True, labels: bool = False, panels: int = 1,
           layout: str = "1", note: str = "") -> dict:
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
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(page: int, idx: int, cols: int, rows: int, header_rows: int, *,
          numeric: int, text_cols: int, cap: dict, men: dict, path: list[str],
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
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": "booktabs",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    }


ITEMS = [
    figure(2, 1, "flowchart-or-schematic",
           caption("Fig.1 input-output ocean system", "Fig. N", "below"),
           mention(2, first=2, style=["Fig.1"], count=1,
                   lead=span(2, "we first abstract the Ocean System", "(Fig.1)."),
                   pattern="parenthetical"),
           path=[H_DESC], kind="model", printed=False, labels=True,
           note="one box labelled Ocean System with the pair Input: Debris above and "
                "Output: Impacts below, hollow arrowheads pointing in and out, plus a "
                "vertical double-headed arrow carrying Movement and Accumulation; no "
                "axes, no legend"),

    figure(3, 1, "bar",
           caption("Fig.2 Number of Hawaiian Monk Seal Entanglements Observed", "Fig. N",
                   "below", voice="passive"),
           mention(3, first=3, style=["Fig.2"], count=2,
                   lead=span(3, "The annual number of Hawaiian monk seal entanglements",
                             "as show in Fig.2"),
                   trail=span(3, "a sequence about the entanglements",
                              "can be generated"),
                   pattern="as-shown-in", read=1),
           path=[H_MODEL], kind="model",
           note="single series of black columns over 1985-1999, y axis 0-25 with no axis "
                "title, chart title Number of Entanglements printed inside the plot; the "
                "enlarged raster copy on the same page is a fragment of this chart"),

    figure(5, 2, "bar",
           caption("Fig.3 Original and Grey Predictive Data", "Fig. N", "below"),
           mention(5, first=4, style=["Fig.3"], count=1,
                   lead=span(4, "we obtain the certain growth trend sequence",
                             "(Show in Fig.3)."),
                   pattern="parenthetical"),
           path=[H_MODEL], kind="result", legend="inside",
           note="two series in one frame: solid blue columns for the observed counts and "
                "a red fitted curve for the grey-model trend, keyed by a small colour "
                "block plus text at the top left inside the axes"),

    figure(5, 1, "line",
           caption("Fig.4 Smooth Random Change Trend", "Fig. N", "below"),
           mention(5, first=5, style=["Figure 4"], count=1,
                   lead=span(5, "Figure 4 shows smooth random change trend", "sequence Z 0"),
                   pattern="figure-n-shows"),
           path=[H_MODEL], kind="result",
           note="one blue line oscillating about zero on a -6 to 8 vertical axis, no "
                "series key because only one series is drawn"),

    figure(5, 4, "bar",
           caption("Fig.5 Autocorrelation and Partial Correlation", "Fig. N", "below"),
           mention(5, first=5, style=["Fig.5", "Figure 5"], count=2,
                   lead=span(5, "Taking the sequence Z 0 as the sample", "show in Fig.5"),
                   trail=span(5, "coefficient denoted by", "is censored"),
                   pattern="as-shown-in", read=1),
           path=[H_MODEL], kind="result", panels=2, layout="1x2",
           note="two half-width panels side by side, barred autocorrelations on the left "
                "and partial correlations on the right, each with grey stems and dashed "
                "confidence bands and its own in-plot title; axes are not shared, each "
                "panel repeats the lag axis"),

    figure(5, 3, "line",
           caption("Fig.6 Smooth Random Change Trend", "Fig. N", "below"),
           mention(5, first=5, style=["Fig.6"], count=1,
                   lead=span(5, "With the help of EViews", "shows in Fig.6"),
                   pattern="as-shown-in"),
           path=[H_MODEL], kind="result", legend="inside",
           note="two series over 2000-2014 with a key box at the top right inside the "
                "axes; the same caption text as Fig.4 because it continues the same "
                "sequence"),

    figure(6, 2, "line",
           caption("Fig.7 Comparative Result Diagram", "Fig. N", "below"),
           mention(6, first=6, style=["Fig.7"], count=1,
                   lead=span(6, "Result of the comparison between the actual", "is shown in Fig.7"),
                   trail=span(6, "the change trends of the two data", "are similar"),
                   pattern="as-shown-in", read=1),
           path=[H_RES], kind="result", legend="inside",
           note="actual against predictive series over 1985-1999, two colours keyed in a "
                "box at the top left inside the axes"),

    figure(6, 1, "bar",
           caption("Fig.8 Amount of Recovered Fishing Gear", "Fig. N", "below"),
           mention(6, first=6, style=["Fig.8"], count=1,
                   lead=span(6, "This difference can be explained by Fig.8",
                             "begins to increase"),
                   trail=span(6, "Correspondingly", "will decrease"),
                   pattern="direct", read=1),
           path=[H_RES], kind="result", three_d="perspective-bars",
           note="perspective 3D columns on a receding base, categories 96/97 to 04, "
                "vertical axis 0-140,000 with the comma-grouped numerals printed, and a "
                "full chart title inside the plot instead of a legend; the raster copy "
                "beside it repeats the same chart"),

    figure(7, 1, "flowchart-or-schematic",
           caption("Fig.9 Debris", "Fig. N", "below"),
           mention(7, first=7, style=["Fig.9"], count=1,
                   lead=span(7, "We divide the Debris and Impacts", "as Fig.9-10 show"),
                   pattern="as-shown-in"),
           path=[H_EVAL, H_AHP], kind="model", printed=False, labels=True,
           note="three-level hierarchy: Debris on top, Direct Data and Indirect Data "
                "below it, five leaf boxes under those; plain rectangles wired with "
                "solid-headed elbow arrows, every node labelled in place"),

    figure(7, 2, "flowchart-or-schematic",
           caption("Fig.10 Impacts", "Fig. N", "below"),
           mention(7, first=7, style=["Fig.10"], count=1,
                   lead=span(7, "We divide the Debris and Impacts", "as Fig.9-10 show"),
                   pattern="as-shown-in"),
           path=[H_EVAL, H_AHP], kind="model", printed=False, labels=True,
           note="two-level version of the same grammar: Impacts on top, Ocean Ecosystem "
                "and Coastal Economy below, same box-and-elbow-arrow drafting as Fig.9"),
]

TABLES = [
    table(7, 3, 4, 5, 1, numeric=0, text_cols=4,
          cap=caption("Table1. Symbols definitions", "Table N.", "above"),
          men=mention(7, first=7, style=["Table1"], count=1,
                      lead=span(7, "Where, our symbols are defined", "Table1"),
                      pattern="direct"),
          path=[H_EVAL, H_AHP], kind="symbols",
          note="abbreviation glossary set as two abbreviation/meaning pairs across four "
                "columns, five body rows, top rule and a rule under the single header row "
                "with a closing rule below; no vertical rules, no shading, no merged "
                "cells, no units to print"),
]

ITEMS += [
    figure(9, 1, "line",
           caption("Fig.11 Result of E V i", "Fig. N", "below"),
           mention(9, first=8, style=["Fig.11"], count=2,
                   lead=span(8, "The results show", "Fig.11-13."),
                   trail=span(9, "From the above Fig.11-13", "as follows"),
                   pattern="as-shown-in", read=2),
           path=[H_EVAL, H_R43], kind="result", legend="inside",
           note="three series over 1990-2006 keyed by a legend strip at the bottom inside "
                "the axes; the series names are split across rasterised glyphs so the "
                "crop is what settles the count"),

    figure(9, 3, "bar",
           caption("Fig.12 Result of f ( E Vi ) Based on Predictive Data", "Fig. N", "below"),
           mention(9, first=8, style=["Fig.12"], count=2,
                   lead=span(8, "The results show", "Fig.11-13."),
                   trail=span(10, "Analyzing Fig.12 and Fig.13", "since 2000 year"),
                   pattern="as-shown-in", read=2),
           path=[H_EVAL, H_R43], kind="result", three_d="perspective-bars",
           note="perspective 3D stacked columns, two series (square of predictive impacts "
                "and square of discarded debris) stacked in one column per year, years "
                "labelled 1997-2007, no legend box because the series are named in the "
                "chart title area"),

    figure(9, 5, "bar",
           caption("Fig.13 Result of f ( E Vi ) Based on Actual Data", "Fig. N", "below"),
           mention(9, first=8, style=["Fig.13"], count=2,
                   lead=span(8, "The results show", "Fig.11-13."),
                   trail=span(10, "From Fig.13, we find", "of Ocean System"),
                   pattern="as-shown-in", read=2),
           path=[H_EVAL, H_R43], kind="result", three_d="perspective-bars",
           note="twin of Fig.12 with the actual impacts stacked under the discarded debris; "
                "same perspective base, same two-series stack, different second series"),

    figure(10, 1, "flowchart-or-schematic",
           caption("Fig.14 Ocean as a Feedback System", "Fig. N", "below"),
           mention(10, first=10, style=["Fig.14"], count=1,
                   lead=span(10, "we regard the Ocean System as a Feedback System",
                             "Fig.14"),
                   pattern="as-shown-in"),
           path=[H_EVAL, H_FB], kind="solution", printed=False, labels=True,
           note="Fig.1 redrawn as a loop: Ocean System between Input: Debris and Output: "
                "Impacts, with Recovery feeding back and a summing junction drawn as a "
                "circled cross carrying + and - signs"),
]

RULES = [
    "本题型没有「结果一张大图」的写法，全部结果拆成两列并排的小面板，"
    "每面板一条题注，因而同一页出现三四条题注并列 [place.page_order]，[place.page_zone]。",
    "数值图一律 Excel 默认样式：单轴、无轴标题、图名列在图内，"
    "纵轴只印数字不印单位，单位写在正文或题注之外 [geometry.printed_numbers]，"
    "[geometry.data_labels]。",
    "三维只在柱状图上出现（perspective-bars），共三处：Figure 8 单系列透视柱、"
    "Figure 12/13 双系列透视堆叠柱；折线图与层次图一律平面 [geometry.three_d]。",
    "双系列图把图例做成图内小方框，位置随图变（左上、右下、右上都有），"
    "单系列图干脆不画图例、改用图内标题 [geometry.legend]。",
    "只有 Figure 5 是多面板（1x2 并排的自相关/偏相关），"
    "两面板各带自己的横轴标签，不共享坐标轴 [geometry.panel_count]，[geometry.shared_axes]。",
    "层次与系统图用无填充矩形加实心箭头，节点名写在框内、不给数值，"
    "因此 printed_numbers 为假而 data_labels 为真 [geometry.data_labels]，"
    "[geometry.family]。",
    "题注格式是 Fig.N 加短语、无冒号、一律在图下；表题是 Table1. 加短语、在表上 "
    "[caption.numbering]，[caption.position]。",
    "图题极短（4-10 词），只报数据是什么，不给单位、不给参数、不下结论 "
    "[caption.words]，[caption.units]，[caption.concludes]。",
    "正文引出以 as show in / show in / showed in 的顺叙式为主，另有一处 Figure 4 shows "
    "和一处 (Fig.1) 括号回指 [mention.lead_pattern]，[mention.count]。",
    "同一批图先引用、后成图：Figure 3 在上一页就说 Show in Fig.3，"
    "Figure 11-13 在结果章开头一次点三名、图页在下一页 [mention.lead_pages]，"
    "[mention.first_page]。",
    "图后解读句几乎总以 From Fig.N / From the above Fig.11-13 起头，"
    "把趋势读成一句话再落结论 [mention.trail_sentence]，[mention.read_sentences]。",
    "全文只有一张表：缩写表用三线（booktabs）、无竖线、无底纹、单表头行、"
    "四个文本列、通栏宽 [table.rule_style]，[table.cols]，[table.width]。",
    "表无单位、无合并单元格、无续表，靠两列「缩写/含义」并排把条目压进一行 "
    "[table.units_in_header]，[table.merged_cells]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": 3, "bbox": REG[(3, 2)], "reason": "fragment-of-other",
         "note": "enlarged raster copy of the Fig.2 column chart"},
        {"page": 6, "bbox": REG[(6, 3)], "reason": "fragment-of-other",
         "note": "raster copy of the Fig.8 perspective column chart"},
        {"page": 9, "bbox": REG[(9, 2)], "reason": "fragment-of-other",
         "note": "raster copy of the Fig.11 line chart"},
        {"page": 9, "bbox": REG[(9, 4)], "reason": "fragment-of-other",
         "note": "raster copy of the Fig.12 stacked column chart"},
        {"page": 9, "bbox": REG[(9, 6)], "reason": "fragment-of-other",
         "note": "raster copy of the Fig.13 stacked column chart"},
    ],
    "note": "Sections 3.1 (GM (1, 1) Model Predicts Certain Growth Trend of Sequence X 0) "
            "and 3.2 (Time Series Analysis Predicts Smooth Random Change Trend of X0) hold "
            "Figures 3-6 but are absent from the extracted heading list, so those four "
            "floats are placed under their parent heading; the titles are copied here from "
            "the text layer, not from the heading index.",
    "rules": RULES,
}

out = PROXY / f"{PID}-payload12.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(payload['items'])} items + {len(TABLES)} tables -> {out.name}")
