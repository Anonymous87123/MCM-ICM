"""Hand pass for P-C-2010-6947-c5305f34 (marine plastic risk, 3 figures + 6 tables).

This team never writes a callout. Across ten pages there is exactly one in-text reference
to an exhibit — "The logic of the simulation process is detailed in Figure 2." — and every
other figure and table is simply dropped in with a bare caption. The lead sentence for
those is the colon-ended sentence that hands over the data ("The data we need are as
follows:", "Regulate the data in table 4 follow the formulate above and we have:").

Both pictures that carry numbers are Excel default output: a line chart and a 3D-perspective
column chart, each with an Excel "data table" strip of values printed under the category
axis instead of data labels. The third picture is a rectangle/ellipse flow chart.

Tables are ruled by horizontal lines on every row plus at most one vertical rule; none is
fully boxed, none is shaded, none continues across a page. Three of them carry a diagonal
corner cell (plastic/alternative, Policy/Solution).

The Table 1 region is two panels of the same 4-column layout printed side by side inside
one measured region, so it is counted once with cols=4 and rows=5.

Usage: python -I tools/_dist_paper10.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2010-6947-c5305f34"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}

H_INTRO = "未编号标题：Introduction"
H_ASSUME = "未编号标题：Assumptions"
H_DISC = "未编号标题：Discussion"


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


def cap(page: int, start: str, end: str) -> str:
    """A caption runs from its label to the last word the text layer puts on that line."""
    t = text(page)
    i = t.find(start)
    assert i >= 0, f"{start!r} not on page {page}"
    j = t.find(end, i)
    assert j >= 0, f"{end!r} not after start on page {page}"
    return t[i:j + len(end)]


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
            gap: int | None = None, trail: str = "") -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": count,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": gap,
    }


def place(order: int, path: list[str], kind: str, numbered: bool) -> dict:
    s = BY_ORDER[order]
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": s["doc_order"],
        "page_order": s["page_order"],
        "page_zone": s["page_zone"],
        "area_frac": s["area_frac"],
        "solo_page": False,
    }


def figure(order: int, family: str, capt: dict, men: dict, *, path: list[str],
           kind: str, numbered: bool, legend: str = "none", three_d: str = "no",
           printed: bool = True, labels: bool = False, note: str = "") -> dict:
    s = BY_ORDER[order]
    return {
        "page": s["page"],
        "bbox": s["bbox"],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": capt["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(order, path, kind, numbered),
        "mention": men,
        "caption": capt,
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(order: int, cols: int, rows: int, header_rows: int, rule: str, *,
          numeric: int, text_cols: int, capt: dict, men: dict, path: list[str],
          kind: str, numbered: bool, diagonal: bool = False,
          merged: bool = False, units_header: bool = False, width: str = "full",
          note_sentence: str = "", note: str = "") -> dict:
    return {
        "page": BY_ORDER[order]["page"],
        "bbox": BY_ORDER[order]["bbox"],
        "caption_verbatim": capt["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(order, path, kind, numbered),
        "mention": men,
        "caption": capt,
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": rule,
            "zebra": False,
            "merged_cells": merged,
            "diagonal_header": diagonal,
            "units_in_header": units_header,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": width,
            "orientation": "portrait",
            "continued": False,
            "note_sentence": note_sentence,
        },
    }


ITEMS = [
    figure(1, "line", caption(cap(3, "Figure1", "1975-2001"), "Figure N", "below"),
           mention(3, first=None, style=[], count=0,
                   lead=span(3, "we know that the abundance", "every few years")),
           path=[H_INTRO], kind="introduction", numbered=False, legend="below",
           labels=True,
           note="Excel line chart of one series over four years (1975 1988 1999 2001) on a "
                "0-200000 abundance axis; the values are printed as a data-table strip "
                "under the category axis, not on the markers, and the series key sits in "
                "that same strip"),

    figure(3, "flowchart-or-schematic",
           caption(cap(5, "Figure2", "abatement process"), "Figure N", "above"),
           mention(5, first=4, style=["Figure 2"], count=1,
                   lead=span(4, "The logic of the simulation", "Figure 2."),
                   trail=span(5, "To determine the risk degree", "taken into consideration"),
                   pattern="direct", read=1, gap=1),
           path=[H_ASSUME], kind="assumption", numbered=False, printed=False,
           labels=True,
           note="five rectangles and four ellipses wired with single-headed arrows, one "
                "feedback loop back to the top block; every label is rasterised text "
                "inside the shape, and the four label words at the right edge are separate "
                "measured regions excluded as fragments of this chart"),

    figure(8, "bar", caption(cap(8, "Figure3", "types of plastic"), "Figure N", "below"),
           mention(8, first=None, style=[], count=0,
                   lead=span(8, "Then the risk degrees of different", "as follows")),
           path=[H_ASSUME], kind="assumption", numbered=False, legend="below",
           three_d="perspective-bars", labels=True,
           note="Excel 3D-perspective column chart, six categories on a receding base, "
                "risk degree 0-0.7 on the vertical axis, values again printed as an Excel "
                "data-table strip under the categories, series key below"),
]

TABLES = [
    table(2, 4, 5, 1, "booktabs", numeric=0, text_cols=4,
          capt=caption(cap(4, "Table 1", "Variables and definitions"), "Table N", "above"),
          men=mention(4, first=None, style=[], count=0),
          path=[H_INTRO], kind="introduction", numbered=False,
          note="two copies of the same two-column variable/definition layout printed side "
               "by side inside one measured region; the only vertical rule is the divider "
               "between the panels, and a fourth rule closes the stack above the last row"),

    table(4, 2, 7, 1, "booktabs", numeric=1, text_cols=1, units_header=True,
          capt=caption(cap(6, "Table2", "North Pacific gyre"), "Table N", "above"),
          men=mention(6, first=None, style=[], count=0,
                      lead=span(6, "The data we need are as follows", "as follows")),
          path=[H_ASSUME], kind="assumption", numbered=False,
          note="six mesh-size bins plus a Total row; the mesh unit is the only thing in "
               "the header, the abundance unit is stated in the caption"),

    table(5, 8, 2, 1, "boxed", numeric=6, text_cols=2,
          capt=caption(cap(6, "Table3", "decision matrix"), "Table N", "above"),
          men=mention(6, first=None, style=[], count=0,
                      lead=span(6, "Each group data can be regarded", "valid data."),
                      trail=span(6, "When the size of the plastic is fixed",
                                 "likely it is ingested")),
          path=[H_ASSUME], kind="assumption", numbered=False, merged=True,
          note="the only fully gridded table in the paper: rules on every row and between "
               "every column, with the Alternative header merged across the two stub cells"),

    table(6, 7, 4, 1, "boxed", numeric=6, text_cols=1,
          capt=caption(cap(8, "Table4", "North Pacific gyre"), "Table N", "above"),
          men=mention(8, first=None, style=[], count=0,
                      lead=span(8, "By the research of Moore", "as follows:"),
                      trail=span(8, "Regulate the data in table 4", "and we have")),
          path=[H_ASSUME], kind="assumption", numbered=False, diagonal=True,
          note="one vertical rule after the stub column and a full-width rule on every "
               "row; the corner cell is split on the diagonal with plastic above and "
               "alternative below, and the six material names wrap to two or three lines"),

    table(7, 7, 4, 1, "boxed", numeric=6, text_cols=1,
          capt=caption(cap(8, "Table5", "Regulation data of table 4"),
                       "Table N", "above"),
          men=mention(8, first=None, style=[], count=0,
                      lead=span(8, "Regulate the data in table 4", "and we have:"),
                      trail=span(8, "Then the risk degrees", "as follows")),
          path=[H_ASSUME], kind="assumption", numbered=False, diagonal=True,
          note="Table 4 normalized to four decimal places, same diagonal corner and same "
               "single stub rule; the values are all 4 d.p. so decimal alignment cannot "
               "be told apart from plain right alignment"),

    table(9, 4, 4, 1, "boxed", numeric=0, text_cols=4,
          capt=caption(cap(10, "Table 6", "three standards"), "Table N", "above"),
          men=mention(10, first=None, style=[], count=0,
                      lead=span(10, "The specific solutions", "as follow:")),
          path=[H_DISC], kind="evaluation", numbered=False, diagonal=True,
          note="policy matrix: stub column plus HRP/MRP/LRP, one rule per row, diagonal "
               "corner Policy over Solution, money and percentages written as text inside "
               "the cells; a Note row closes the table and cites the US environment law",
          note_sentence=cap(10, "Note: The penalty", "United States.")),
]

RULES = [
    "本文的图与表几乎没有正文引出：全篇只有一句 Figure 2 的直陈式引用，"
    "其余九件展品都靠自明题注落地 [mention.count]，[mention.lead_pattern]。",
    "没有引用时，引出句退化为冒号句（The data we need are as follows:、"
    "Regulate the data in table 4 follow the formulate above and we have:），"
    "悬念只交代下一步做什么，不交代图里能看到什么 [mention.lead_sentence]。",
    "图题位置不统一：流程图题注在图上、两张 Excel 图题注在图下，表题一律在表上 "
    "[caption.position]。",
    "编号格式图用 Figure N 无冒号（Figure1、Figure2），表用 Table N 带或不带空格"
    "（Table2 / Table 1），全文不统一 [caption.numbering]。",
    "两张数值图都是 Excel 默认样式：一个折线、一个透视柱，数值不标在点上，"
    "而是复制成坐标轴下方的一行数据表 [geometry.data_labels]，[geometry.three_d]。",
    "三维只出现在 Figure 3 的透视柱列（perspective-bars），底面沿透视线后退，"
    "没有曲面网格、没有色标 [geometry.three_d]，[geometry.colorbar]。",
    "示意图用矩形与椭圆区分「过程」与「方法」，箭头单向、只留一处回到顶部形成闭环 "
    "[geometry.family]，[geometry.data_labels]。",
    "图的版面全宽、单面板竖排，三张图各占半页，没有并排多面板的写法 "
    "[place.area_frac]，[geometry.panel_layout]。",
    "表格一律只用横线（每行一条）加至多一条竖线，只有 Table 3 是全网格，"
    "全篇没有隔行底纹 [table.rule_style]，[table.zebra]。",
    "三张表用对角表头把行列两个维度压进一个格子（plastic/alternative、"
    "Policy/Solution），并在同一格内换行而非拆成两行表头 [table.diagonal_header]，"
    "[table.header_rows]。",
    "单位写法分裂：Table 2 把 (mm) 放进表头、把 pieces km2 交给题注，"
    "Table 6 把 $50000 与百分比直接写进单元格 [table.units_in_header]，[caption.units]。",
    "表都是通栏、竖版、单页，无续表，Table 1 把同构两栏并排塞进一张表 [table.width]，"
    "[table.orientation]。",
    "Table 6 自带 Note 行引用外部法规，是唯一把出处写进表体的表 [table.note_sentence]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": 5, "bbox": [296.04, 175.2, 364.86, 218.76],
         "reason": "fragment-of-other",
         "note": "rasterised label word inside the Figure 2 flow chart"},
        {"page": 5, "bbox": [419.7, 175.2, 488.46, 218.76],
         "reason": "fragment-of-other",
         "note": "rasterised label word inside the Figure 2 flow chart"},
        {"page": 5, "bbox": [296.04, 262.08, 364.86, 305.64],
         "reason": "fragment-of-other",
         "note": "rasterised label word inside the Figure 2 flow chart"},
        {"page": 5, "bbox": [419.7, 262.08, 488.46, 305.64],
         "reason": "fragment-of-other",
         "note": "rasterised label word inside the Figure 2 flow chart"},
    ],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload10.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items + {len(TABLES)} tables -> {out.name}")
