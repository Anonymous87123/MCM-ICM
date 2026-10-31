"""Hand pass for P-B-2017-68303-6c8a9ede (toll-plaza layout, 14 figures + 4 tables).

Shape of the paper: one schematic pair (Figure 1, normal and stipulated merging pattern)
opens section 3, Table 1 fixes the simulation parameters, and one VISSIM screenshot per
kind (Figures 2-10) shows the eight layouts. Table 2 collects the eight simulation runs,
Table 3 the PCA evaluation ranking, Table 4 the symbol list for section 5. Sections 5.3
and 6 close with one schematic (Figure 11), one screenshot (Figure 12) and two sensitivity
plots (Figures 13, 14).

Three measurement facts worth recording rather than smoothing over:

1. Table 1 is measured only as its header band (a 26 pt vector region); the seven data
   rows sit in the text layer below and are not a measured region. The bbox therefore
   covers the header rule pair, and `note` says so. The row count is read from the crop of
   the page top, not from the region.
2. Figures 3-10 are eight crops of the same VISSIM window, each captioned "Kind N: ...";
   the caption is the only thing that differs, so it carries the panel identity.
3. Figure 1 is a two-panel pair (normal / stipulated) sharing one caption; each panel is
   its own measured region and is recorded as its own item.

Usage: python -I tools/_dist_paper121.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2017-68303-6c8a9ede"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
REG = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: x["bbox"][1]), 1):
        REG[(pg["page"], i)] = r["bbox"]

PAGE_W = LAYOUT["page_size"][0] if "page_size" in LAYOUT else 595.28
PAGE_H = LAYOUT["page_size"][1] if "page_size" in LAYOUT else 841.89

ORDER = [
    (5, 1), (5, 2),
    (6, 1), (6, 2), (6, 3), (6, 4),
    (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
    (8, 1), (10, 1), (11, 1),
    (13, 1), (15, 1),
    (18, 1), (18, 2),
]

S3 = "3 Simulation Model"
S4 = "4 Evaluation Model"
S41 = "4.1 Index variables"
S5 = "5 Find the Optimum Solution"
S52 = "5.2 Differential Equation Model"
S53 = "5.3 Linear Programming Model"
S6 = "6 Effects and Adjustment"
S62 = "6.2 Add Autonomous Vehicles"
S8 = "8 Conclusion"
S81 = "8.1 Strengths"


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
        "solo_page": False,
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
           layout: str = "1", shared: bool = False, note: str = "",
           confidence: str = "high", panel_of: int = 0) -> dict:
    item = {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": confidence,
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
    if panel_of:
        item["is_panel_of"] = panel_of
    return item


def table(page: int, idx: int, cap: dict, men: dict, *, path: list[str], kind: str,
          rows: int, cols: int, header_rows: int = 1, rule_style: str = "booktabs",
          zebra: bool = False, merged: bool = False, diagonal: bool = False,
          units_hdr: bool = False, decimal: bool = False, numeric: int = 0,
          textc: int = 0, width: str = "full", orient: str = "portrait",
          continued: bool = False, note_sentence: str = "", note: str = "") -> dict:
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
            "rule_style": rule_style,
            "zebra": zebra,
            "merged_cells": merged,
            "diagonal_header": diagonal,
            "units_in_header": units_hdr,
            "decimal_aligned": decimal,
            "numeric_cols": numeric,
            "text_cols": textc,
            "width": width,
            "orientation": orient,
            "continued": continued,
            "note_sentence": note_sentence,
        },
    }


VISSIM = ("top-down VISSIM screenshot: grey roadway, three approach lanes below, "
          "eight tollbooths across the top edge, coloured cars as data-free marks")

ITEMS = [
    figure(5, 1, "flowchart-or-schematic",
           caption("Figure 1: normal and stipulated merging pattern"),
           mention(5, first=5, style=[], count=0,
                   lead="The stipulation may reduce the risk of collision."),
           path=[S3], kind="model",
           note="left panel of the pair: solid lines only, eight red cars on the bottom "
                "approaches and three blue cars on the top lane, the merging lines drawn "
                "straight from tollbooth to lane"),

    figure(5, 2, "flowchart-or-schematic",
           caption("Figure 1: normal and stipulated merging pattern"),
           mention(5, first=5, style=[], count=0,
                   lead="The stipulation may reduce the risk of collision."),
           path=[S3], kind="model", panel_of=1,
           note="right panel of the same pair: the diagonal connectors are drawn as dashed "
                "lanes, which is what the caption calls the stipulated pattern"),

    figure(6, 2, "map-or-plan-view",
           caption("Figure 2: Set collision areas"),
           mention(6, first=6, style=[], count=0, read=1,
                   trail=span(6, "Afterwards, we set travel time", "values of delay")),
           path=[S3], kind="model",
           note="plan view of the whole simulated area: the funnel below the tollbooths is "
                "painted grey and the conflict zones are lifted out in yellow and green"),

    figure(6, 3, "map-or-plan-view",
           caption("Figure 3: Kind 1: Sp1,Sz1,Mp1"),
           mention(6, first=6, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 1 of the eight"),

    figure(6, 4, "map-or-plan-view",
           caption("Figure 4: Kind 2: Sp1,Sz2,Mp1"),
           mention(6, first=6, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 2 of the eight"),

    figure(7, 1, "map-or-plan-view",
           caption("Figure 5: Kind 3: Sp1,Sz1,Mp2"),
           mention(7, first=7, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 3 of the eight"),

    figure(7, 2, "map-or-plan-view",
           caption("Figure 6: Kind 4: Sp1,Sz2,Mp2"),
           mention(7, first=7, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 4 of the eight"),

    figure(7, 3, "map-or-plan-view",
           caption("Figure 7: Kind 5: Sp2,Sz1,Mp1"),
           mention(7, first=7, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 5 of the eight"),

    figure(7, 4, "map-or-plan-view",
           caption("Figure 8: Kind 6: Sp2,Sz2,Mp1"),
           mention(7, first=7, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 6 of the eight"),

    figure(7, 5, "map-or-plan-view",
           caption("Figure 9: Kind 7: Sp2,Sz1,Mp2"),
           mention(7, first=7, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 7 of the eight"),

    figure(7, 6, "map-or-plan-view",
           caption("Figure 10: Kind 8: Sp2,Sz2,Mp2"),
           mention(7, first=7, style=[], count=0,
                   lead=span(6, "Then, we simulate eight kinds", "above classification")),
           path=[S3], kind="model", note=VISSIM + "; kind 8 of the eight"),

    figure(13, 1, "flowchart-or-schematic",
           caption("Figure 11: Simple model for calculation"),
           mention(13, first=13, style=["figure 11"], count=1,
                   lead=span(13, "We build a simple model", "travel path"), read=1),
           path=[S5, S53], kind="model",
           note="single diagram of two lane rows with the geometric shorthand d, SD and H "
                "marked, drawn to support Equation 15 above the caption"),

    figure(15, 1, "map-or-plan-view",
           caption("Figure 12: Testing Simulation"),
           mention(15, first=15, style=[], count=0),
           path=[S6], kind="other",
           note="one more VISSIM frame, printed at the head of section 6 without a sentence "
                "that reads it; caption is the only text that names it"),

    figure(18, 1, "bar",
           caption("Figure 13: Reduced cost"),
           mention(18, first=17, style=["figure 13"], count=1, read=1,
                   lead="The result is shown in figure 13."),
           path=[S8, S81], kind="evaluation", printed=True, labels=True,
           note="bar chart, y axis 0.000-3.000 with a comma decimal separator, x axis the "
                "eleven configurations t11 to t63, value labels printed above each bar, no "
                "legend box, drawn in the strengths section"),

    figure(18, 2, "bar",
           caption("Figure 14: Change range of variables"),
           mention(18, first=17, style=["figure 14"], count=1, read=1,
                   lead="The result is shown in figure 14."),
           path=[S8, S81], kind="evaluation", printed=True, labels=True,
           legend="above",
           note="diverging tornado bar chart on one zero line: blue bars up for Increase and "
                "orange bars down for Decrease, y axis -3.000 to 1.500, value labels printed "
                "at every bar end, key set above the plot"),
]

TABLES = [
    table(6, 1,
          caption("Table 1: Parameters", numbering="Table N:", pos="above"),
          mention(6, first=6, style=[], count=0,
                  lead=span(5, "we set the number of lanes", "the same as the example")),
          path=[S3], kind="model",
          rows=8, cols=3, header_rows=1, rule_style="booktabs",
          numeric=2, textc=1, width="full", note_sentence="",
          note="measured region is the header band only (26 pt): the seven data rows below "
               "it are plain text, so rows=8 is read off the page crop, not off the region "
               "bbox; no vertical rules, no zebra, units carried inside the value cells"),

    table(8, 1,
          caption("Table 2: simulation data of 8 kinds of models", numbering="Table N:",
                  pos="above"),
          mention(8, first=8, style=[], count=0),
          path=[S4, S41], kind="result",
          rows=9, cols=6, header_rows=1, rule_style="boxed",
          units_hdr=True, decimal=True, numeric=5, textc=1, width="full",
          orient="landscape",
          note="header wraps to three lines over the same columns; delay(s) is the only "
               "column with its unit inside the header, the other units sit under the "
               "column name; eight numbered data rows, no totals row"),

    table(10, 1,
          caption("Table 3: Evaluation Result of Models", numbering="Table N:", pos="above"),
          mention(10, first=9, style=["Table 3"], count=1,
                  lead=span(9, "According to the principle components", "cost")),
          path=[S4, S41], kind="result",
          rows=5, cols=6, header_rows=1, rule_style="booktabs",
          numeric=4, textc=0, width="half",
          note="two rank/model/score triplets printed side by side under one caption, so the "
               "grid is six columns wide and four data rows deep; scores carry four decimals "
               "and are right-aligned within the column, not decimal-point aligned"),

    table(11, 1,
          caption("Table 4: Symbols", numbering="Table N:", pos="above"),
          mention(11, first=11, style=[], count=0),
          path=[S5, S52], kind="symbols",
          rows=15, cols=2, header_rows=1, rule_style="booktabs",
          numeric=0, textc=2, width="full",
          note="symbol/meaning glossary, one symbol per row down to O(t, B); meanings wrap "
               "to two lines, no units column, no zebra. Measured region is the header band "
               "only (26 pt), so rows=15 is read off the page text, not off the bbox"),
]

RULES = [
    "章节与图型的对应：3 Simulation Model 一节点上 8 个同级截图（Figure 2-10），都是同一 VISSIM 窗口的俯视图，[place.section_path] 与 [geometry.family] 一一对上。",
    "八种布局只靠题注区分：题注末段是 Kind N 编号与 Sp/Sz/Mp 三参数三元组，[caption.verbatim] 是唯一身份字段。",
    "截图一律无坐标轴、无图例、无数据标注，[geometry.printed_numbers]=False 且 [geometry.legend]=none。",
    "示意图与截图分开记：Figure 1 两联、Figure 11 一张为 flowchart-or-schematic，[geometry.family] 用该值而非 map-or-plan-view。",
    "题注统一 Figure N: 冒号式，[caption.numbering] 恒为 `Figure N:`，不含单位、不含变量、不下结论。",
    "表题注同样冒号式并印在表格上方，[caption.position]=above；图题注印在图下方，[caption.position]=below。",
    "表头单位有两种写法：Table 2 把 delay(s) 单位塞进表头、其余单位另起一行，[table.units_in_header]=True。",
    "表格线型一律 booktabs（上下粗线 + 表头细线，无竖线），[table.rule_style]=booktabs，[table.zebra]=False。",
    "表 3 把两组 rank/model/score 并排成六列，[table.cols]=6 而不是 3，行数是每组 4 行。",
    "引出句多为间接指代：`The result is shown in figure 13.`，[mention.lead_pattern]=none 表示没有 Figure N shows 式句式。",
    "图与正文的页差可以非零：Figure 13/14 在 p17 被提及、印在 p18，[mention.lead_pages]=1。",
    "同一 caption 覆盖两块实测区域时按面板各记一条，[place.page_order] 区分左右。",
    "Table 1 的实测区域只有 26 pt 表头带，[table.rows] 与 bbox 高度不一致，必须在 note 里交代，不得据 bbox 反推行数。",
    "计数只算正文带编号的引用，题注本身不算：全篇只有 Figure 11、Figure 13、Figure 14、Table 3 各被正文点到一次，[mention.count]=1，其余十五项一律 0 且 [mention.style]=[]。",
    "共享题注的第二块用 is_panel_of 标明：Figure 1 两联只有一句 [caption.verbatim]，右联记 panel_of=1，说明该串是复制而非第二次印刷。",
    "一句话引出整组图时六块共用同一句：Figure 5-10 的 [mention.lead_sentence] 都是 Then, we simulate eight kinds…，不因复用而留空。",
]

payload = {"paper": PID, "layout_sha256": LAYOUT["layout_sha256"],
           "items": ITEMS, "tables": TABLES,
           "excluded_regions": [], "rules": RULES,
           "note": "hand pass, 19 measured regions -> 15 figure items + 4 tables; "
                   "family_counts counts regions, so its sum is items + tables"}

out = PROXY / f"{PID}-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"wrote {out} items={len(ITEMS)} tables={len(TABLES)} rules={len(RULES)}")
