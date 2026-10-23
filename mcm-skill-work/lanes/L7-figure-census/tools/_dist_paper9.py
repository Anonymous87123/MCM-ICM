"""Hand pass for P-B-2010-8479-b934962b (geographic profiling, 6 figures + 5 tables).

Two picture grammars. The centrographic results are plain lat/long dot plots inside a red
diamond boundary — Figure 1 is a five-panel run of them (2x3 with one cell empty), and
Figure 5 is the DC-sniper version. The rational-choice results draw the risk field as
shaded cells with red raised columns standing on it, keyed by a small list of symbol
entries at the right edge (Attack Sites, Berkowitz's Home, 7th Attack).

Every table is fully boxed — vertical and horizontal rules on all cell edges — one header
row, no zebra shading. Only Table 2 prints its unit, and it puts it in the header (km);
Table 5 puts km2 inside the cells instead.

Table 6 (Buono & Bianchi) is captioned and referenced but has no measured region: its
body is ordinary text-layer type, so it cannot be placed by this census. Recorded as a
gap, not patched.

Usage: python -I tools/_dist_paper9.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2010-8479-b934962b"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}

H_5DATA = "5 Data"
H_62 = "6.2 Rational Serial Criminal Model"
H_63 = "6.3 Combined Models"


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def lines(page: int) -> list[str]:
    return [schema.norm(l) for l in (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()]


def cap(kind: str, page: int, number: int) -> str:
    ls = lines(page)
    start = next(i for i, l in enumerate(ls) if re.match(rf"{kind}\s+{number}:", l))
    out = [ls[start]]
    for nxt in ls[start + 1:]:
        if not nxt or re.match(rf"{kind}\s+\d", nxt):
            break
        out.append(nxt)
    return " ".join(out)


def span(page: int, start: str, end: str) -> str:
    t = text(page)
    i = t.find(start)
    assert i >= 0, f"start {start!r} not on page {page}"
    j = t.find(end, i)
    assert j >= 0, f"end {end!r} not after start on page {page}"
    q = t[i:j + len(end)]
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def caption(v: str, numbering: str, *, position: str = "below", units: bool = False,
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


def place(order: int, path: list[str], kind: str) -> dict:
    s = BY_ORDER[order]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": s["doc_order"],
        "page_order": s["page_order"],
        "page_zone": s["page_zone"],
        "area_frac": s["area_frac"],
        "solo_page": False,
    }


def figure(order: int, family: str, panels: int, panel_layout: str, capt: dict,
           men: dict, *, path: list[str] = None, kind: str = "result",
           legend: str = "none", colorbar: bool = False, three_d: str = "no",
           printed: bool = True, labels: bool = False, note: str = "") -> dict:
    s = BY_ORDER[order]
    return {
        "page": s["page"],
        "bbox": s["bbox"],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": capt["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(order, path or [H_62], kind),
        "mention": men,
        "caption": capt,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": panel_layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(order: int, cols: int, rows: int, header_rows: int, *, numeric: int,
          text_cols: int, units_in_header: bool = False, decimal: bool = False,
          width: str = "column", path: list[str] = None, kind: str = "result",
          note: str = "", cap_obj: dict, men: dict) -> dict:
    v = cap_obj["verbatim"]
    return {
        "page": BY_ORDER[order]["page"],
        "bbox": BY_ORDER[order]["bbox"],
        "caption_verbatim": v,
        "caption_source": "text-layer",
        "note": note,
        "place": place(order, path or [H_62], kind),
        "mention": men,
        "caption": cap_obj,
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": "boxed",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": units_in_header,
            "decimal_aligned": decimal,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": width,
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    }


ITEMS = [
    figure(5, "scatter", 5, "2x3",
           caption(cap("Figure", 14, 1), "Figure N:"),
           mention(14, first=19, style=["Figure 1"], count=1,
                   lead=span(19, "Looking at the data", "in Figure 1"),
                   trail=span(19, "meaning that as more data", "becoming more accurate"),
                   pattern="as-shown-in", read=1, gap=1),
           note="five estimates of the same centrographic run, 2x3 with the bottom-right "
                "cell empty; blue crime dots and one black point inside a red diamond "
                "boundary, axes Latitude vs Longitude"),

    figure(6, "surface-or-3D", 1, "1",
           caption(cap("Figure", 15, 2), "Figure N:", vars_=0),
           mention(15, first=15, style=["Figure 2"], count=1,
                   lead=span(15, "The re- sulting jeopardy surface is shown in Figure 2",
                             "overlaid"),
                   pattern="as-shown-in", read=1, gap=0),
           legend="outside-right", three_d="perspective-bars",
           note="blue risk field with red raised columns over the target zone; key at the "
                "right lists Attack Sites, Berkowitz's Home (orange square) and Previous "
                "Home (green triangle)"),

    figure(8, "surface-or-3D", 1, "1",
           caption(cap("Figure", 17, 3), "Figure N:"),
           mention(17, first=16, style=["Figure 3"], count=1,
                   lead=span(16, "The resulting jeopardy surface is plotted in Figure 3",
                             "Figure 3"),
                   pattern="as-shown-in", read=1, gap=1),
           legend="outside-right", three_d="perspective-bars",
           note="one long north-south ridge of red columns over the blue field, dump sites "
                "as green triangles strung along the crest"),

    figure(9, "heatmap-or-contour", 1, "1",
           caption(cap("Figure", 17, 4), "Figure N:"),
           mention(17, first=16, style=["Figure 4"], count=1,
                   lead=span(16, "to try to predict the location", "(Figure 4)"),
                   pattern="parenthetical", read=1, gap=1),
           legend="outside-right", three_d="perspective-bars",
           note="shaded zones with four stepped diamond markers marking candidate search "
                "blocks; one black dot is the 7th attack, the only key entry"),

    figure(10, "scatter", 1, "1",
           caption(cap("Figure", 18, 5), "Figure N:"),
           mention(18, first=None, style=[], count=0, read=0, gap=None),
           path=[H_63],
           note="ten navy dots inside a red diamond boundary on the DC window, two "
                "outliers south-west and one east"),

    figure(11, "heatmap-or-contour", 1, "1",
           caption(cap("Figure", 18, 6), "Figure N:"),
           mention(18, first=None, style=[], count=0, read=0, gap=None),
           path=[H_63], legend="outside-right", three_d="perspective-bars",
           note="the same faceted diamond grammar as Figure 4 on the DC window; key has a "
                "single entry, Final Shooting"),
]

TABLES = [
    table(1, 6, 9, 1, numeric=4, text_cols=2, path=[H_5DATA], kind="other",
          cap_obj=caption(cap("Table", 12, 1), "Table N:", position="below"),
          men=mention(12, first=12, style=["Table 1"], count=1,
                      lead=span(12, "we converted the street addresses", "(Table 1)"),
                      pattern="parenthetical", read=1, gap=0),
          note="the raw input table: kill number, coordinates, days since the first "
               "attack, victims, street addresses; every cell framed"),

    table(2, 2, 6, 1, numeric=2, text_cols=0, units_in_header=True,
          cap_obj=caption(cap("Table", 13, 2), "Table N:", position="below",
                          units=True),
          men=mention(13, first=12, style=["Table 2"], count=2,
                      lead=span(12, "we calculated the distance", "(Table 2)"),
                      pattern="parenthetical", read=1, gap=1),
          note="five error distances to ten decimal places, unit printed in the header"),

    table(3, 4, 6, 1, numeric=4, text_cols=0,
          cap_obj=caption(cap("Table", 13, 3), "Table N:", position="below",
                          vars_=3),
          men=mention(13, first=13, style=["Table 3"], count=1,
                      lead=span(13, "we perform a linear regression", "(Table 3)"),
                      pattern="parenthetical", read=1, gap=0),
          note="longitudinal regression: intercept, R2 and p per estimate; N/A fills the "
               "first p cell"),

    table(4, 4, 6, 1, numeric=4, text_cols=0,
          cap_obj=caption(cap("Table", 13, 4), "Table N:", position="below",
                          vars_=3),
          men=mention(13, first=13, style=["Table 4"], count=2,
                      lead=span(13, "in both the longitudinal", "(Table 4)"),
                      pattern="parenthetical", read=1, gap=0),
          note="latitudinal twin of Table 3, same four columns and same N/A convention"),

    table(7, 4, 3, 1, numeric=3, text_cols=1,
          cap_obj=caption(cap("Table", 16, 5), "Table N:", position="below",
                          units=True),
          men=mention(16, first=16, style=["Table 5"], count=2,
                      lead="The results are tabulated in Table 5.".strip(),
                      pattern="direct", read=1, gap=0),
          note="two candidate homes against hunting area, hit score and search area; the "
               "km2 unit sits inside the cells, not in the header"),
]

RULES = [
    "本题型的图走两套语法：定位类结果画成经纬度散点加红色菱形边界，"
    "概率类结果画成着色栅格上立起红色柱列 [geometry.family]，[geometry.three_d]。",
    "三维只以透视柱形出现（perspective-bars），没有曲面网格；柱高即概率，"
    "由裁剪图确认而非题注推断 [geometry.three_d]。",
    "概率图的图例不放在图内，而是在右侧单列符号表（Attack Sites / Home / 7th Attack），"
    "条目随图变化、数量极少 [geometry.legend]。",
    "同一模型的多次迭代用多面板并排（Figure 1 为 2x3 留空一格），"
    "面板间不共享坐标轴，靠经纬度刻度自行比对 [geometry.panel_count]，"
    "[geometry.shared_axes]。",
    "图题统一 Figure N: 起头、置于图下方，句式固定为 Attack sites, jeopardy surface, "
    "and homes of X [caption.verbatim]，[caption.position]。",
    "正文引出以 as shown in / plotted in 的顺叙为主，括号回指只用在预测图 "
    "(Figure 4) 与表格 [mention.lead_pattern]。",
    "Figure 1 的引用落后图 5 页（图在结果章开头、讨论在 7 章），"
    "是本题型里唯一的大跨度回指 [mention.first_page]，[mention.lead_pages]。",
    "表格全部是四边框线（boxed），横竖线都画、无隔行底纹、无合并单元格；"
    "数值靠右排而不按小数点对齐 [table.rule_style]，[table.zebra]，"
    "[table.decimal_aligned]。",
    "单位只出现一次且写在表头（(km)），其余表把 km2、% 直接写进单元格，"
    "表头只放变量名 [table.units_in_header]。",
    "表宽都是单栏宽（251-321 pt），不跨栏、不分页续表 [table.width]，"
    "[table.continued]。",
    "缺口：Table 6（Buono & Bianchi）只有题注与引用，正文体未形成可测量的区域，"
    "因此本条未落表块；缺口保留不补，参照 Table 5 的表型 [table.rule_style]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload9.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items + {len(TABLES)} tables -> {out.name}")
