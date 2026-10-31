"""Hand pass for P-B-2010-7947-b6007ae0 (geographic profiling, 8 figures + 2 tables).

Two exhibit idioms dominate. Probability surfaces are drawn as continuous rainbow rasters
with a vertical colour bar outside the axes, labelled high/low at the ends and with the
rotated phrase Next Crime Probability, and are shown as (a)/(b) pairs — or, for the
aggregation sweep, as five (a)-(e) panels whose weights are stated in the sub-caption
rather than in the caption. Comparators use a bare framed plot instead: horizontal bars
with confidence whiskers, a line with error bars, and point maps carrying a rectangle or
an ellipse overlay.

Both tables are three columns with vertical rules, one header row, no zebra, and a
caption above; neither shows units in the header.

Measured panels after the first of each pair are excluded as fragments of the exhibit;
so are the four extra panels of the aggregation sweep.

Usage: python -I tools/_dist_paper7.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2010-7947-b6007ae0"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}


def clean(path: list[str]) -> list[str]:
    """Drop the table-of-contents copies that carry the page number in the label."""
    return [p for p in path if not re.search(r"\s\d+$", p)]


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def lines(page: int) -> list[str]:
    return [schema.norm(l) for l in (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()]


def capt(kind: str, page: int, number: int) -> str:
    ls = lines(page)
    pattern = rf"{kind}\s+{number}:"
    start = next(i for i, l in enumerate(ls) if re.match(pattern, l))
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


def caption(v: str, *, units: bool, vars_: int, cond: bool, concl: bool,
            voice: str) -> dict:
    return {
        "verbatim": v,
        "numbering": "Figure N:",
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": units,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": cond,
        "concludes": concl,
        "voice": voice,
        "position": "below",
    }


def table_caption(v: str, *, cond: bool, vars_: int) -> dict:
    return {
        "verbatim": v,
        "numbering": "Table N:",
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": False,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": cond,
        "concludes": False,
        "voice": "none",
        "position": "above",
    }


def mention(page: int, *, first: int, style: list[str], count: int, lead: str,
            pattern: str, read: int, gap: int, trail: str = "") -> dict:
    return {
        "first_page": first,
        "lead_pages": page - first,
        "style": style,
        "count": count,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": gap,
    }


def entry(order: int, family: str, panels: int, layout: str, capt_: dict,
          men: dict, *, legend: str = "none", colorbar: bool = False,
          three_d: str = "no", printed: bool = True, labels: bool = False,
          shared: bool = False, note: str = "", other_note: str = "") -> dict:
    s = BY_ORDER[order]
    item = {
        "page": s["page"],
        "bbox": s["bbox"],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": capt_["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": {
            "section_path": clean(s["section_path"]),
            "section_numbered": True,
            "section_kind": s["section_kind"],
            "doc_order": s["doc_order"],
            "page_order": s["page_order"],
            "page_zone": s["page_zone"],
            "area_frac": s["area_frac"],
            "solo_page": False,
        },
        "mention": men,
        "caption": capt_,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    return item


ITEMS = [
    entry(2, "flowchart-or-schematic", 1, "1",
          caption(capt("Figure", 11, 1), units=False, vars_=2, cond=False,
                  concl=False, voice="none"),
          mention(11, first=10, style=["Figure 1"], count=1,
                  lead=span(10, "We discretize A into sectors", "discretization process"),
                  pattern="direct", read=0, gap=1),
          printed=False, labels=True,
          note="a k-by-k grid of squares labelled S(i,j) with vertical ellipses between "
               "the blocks and a brace marked with the side length delta s at the left; "
               "no axes, the labels are the content"),

    entry(3, "heatmap-or-contour", 2, "1x2",
          caption(capt("Figure", 16, 2), units=False, vars_=0, cond=True,
                  concl=False, voice="passive"),
          mention(16, first=15, style=["Figure 2"], count=1,
                  lead=span(15, "For an illustrative example", "see Figure 2"),
                  pattern="direct", read=1, gap=1),
          colorbar=True, printed=True, shared=True,
          note="(a) is a single red core at the origin, (b) a ring of ten separated hot "
               "spots on the unit crime circle; both on a -2..2 square, colour bar outside "
               "the axes reading high to low"),

    entry(5, "heatmap-or-contour", 2, "1x2",
          caption(capt("Figure", 17, 3), units=False, vars_=0, cond=True,
                  concl=False, voice="passive"),
          mention(17, first=16, style=["Figure 3"], count=1,
                  lead=span(16, "For an example of this", "see Figure 3"),
                  trail=span(17, "We modify the following spatial models",
                             "weight- ing factors"),
                  pattern="direct", read=1, gap=1),
          colorbar=True, printed=True, shared=True,
          note="(a) an ellipse smeared symmetrically about the eastward path, (b) the same "
               "path with the density shifted to its eastern end by the temporal weight"),

    entry(7, "bar", 1, "1",
          caption(capt("Figure", 18, 4), units=False, vars_=0, cond=False,
                  concl=False, voice="passive"),
          mention(18, first=18, style=["Figure 4"], count=1,
                  lead=span(18, "This can be found in Table 2", "Figure 4"),
                  trail=span(18, "All of our models significantly", "superior to any other"),
                  pattern="direct", read=1, gap=0),
          printed=True,
          note="twelve horizontal bars on a 0..0.5 Hit Score axis with red confidence "
               "whiskers; Uniform Random is full length, all real methods sit near 0.10"),

    entry(8, "line", 1, "1",
          caption(capt("Figure", 19, 5), units=False, vars_=0, cond=True,
                  concl=False, voice="none"),
          mention(19, first=19, style=["Figure 5"], count=1,
                  lead=span(19, "Next we investigate the performance", "as seen in Figure 5"),
                  trail=span(19, "No patterns emerge", "observed more crimes"),
                  pattern="as-shown-in", read=1, gap=0),
          printed=True,
          note="one blue polyline with filled markers and vertical 50% confidence bars "
               "over 3..13 crimes; the bars are wider than the trend, which is the point"),

    entry(10, "heatmap-or-contour", 5, "3x2",
          caption(capt("Figure", 21, 6), units=False, vars_=0, cond=True,
                  concl=False, voice="passive"),
          mention(21, first=20, style=["Figure 6"], count=1,
                  lead=span(20, "Examples of this model", "found in Figure 6"),
                  trail=span(22, "In an aggregate model this is not the case",
                             "another model"),
                  pattern="direct", read=1, gap=3),
          colorbar=True, printed=True, shared=True,
          note="five panels (a)-(e) stepping the exponential-decay weight 0.00 to 1.00 "
               "against the circle-center weight 1.00 to 0.00; each keeps its own colour "
               "bar and the 48 km bar, the hot area slides between the two methods' cores"),

    entry(15, "map-or-plan-view", 2, "1x2",
          caption(capt("Figure", 23, 7), units=False, vars_=0, cond=False,
                  concl=False, voice="none"),
          mention(23, first=14, style=["Figure 7"], count=2,
                  lead=span(23, "These rudimentary models", "seen in Figure 7"),
                  trail=span(23, "method of identifying an area of high probability",
                             "rectangle or ellipse"),
                  pattern="direct", read=1, gap=1),
          printed=True,
          note="the same eleven murder points on a lat/long window with a 20 km bar, once "
               "inside standard-deviation rectangles and once inside the ellipses; no "
               "colour bar, the shapes carry the message"),

    entry(17, "composite-panel", 2, "1x2",
          caption(capt("Figure", 24, 8), units=False, vars_=0, cond=True,
                  concl=True, voice="passive"),
          mention(24, first=23, style=["Figure 8(a)", "Figure 8"], count=2,
                  lead=span(23, "See Figure 8 for an application", "Peter Sutcliffe"),
                  trail=span(23, "The known crimes had a hit score",
                             "10.6% using this model"),
                  pattern="direct", read=1, gap=2),
          colorbar=True, printed=True,
          note="(a) is a Google Static Maps base map with the murder points, (b) the "
               "probability surface on the same window; the caption then reads the result "
               "out loud, naming Bradford as the highest-risk area"),
]

TABLE_CAP_1 = capt("Table", 9, 1)
TABLE_CAP_2 = capt("Table", 20, 2)

TABLES = [
    {
        "page": 9,
        "bbox": BY_ORDER[1]["bbox"],
        "caption_verbatim": TABLE_CAP_1,
        "caption_source": "text-layer",
        "note": "ten rows against the temporal exponential decay accuracy score; the "
                "description column wraps to four and five lines while the two number "
                "columns stay one line each",
        "place": {
            "section_path": clean(BY_ORDER[1]["section_path"]),
            "section_numbered": True,
            "section_kind": "introduction",
            "doc_order": BY_ORDER[1]["doc_order"],
            "page_order": BY_ORDER[1]["page_order"],
            "page_zone": BY_ORDER[1]["page_zone"],
            "area_frac": BY_ORDER[1]["area_frac"],
            "solo_page": False,
        },
        "mention": mention(9, first=9, style=["Table 1"], count=2,
                           lead=span(9, "A listing of the crimes", "found in Table 1"),
                           pattern="direct", read=1, gap=0),
        "caption": table_caption(TABLE_CAP_1, cond=True, vars_=0),
        "table": {
            "rows": 10,
            "cols": 3,
            "header_rows": 1,
            "rule_style": "vertical-rules",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": 2,
            "text_cols": 1,
            "width": "column",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    },
    {
        "page": 20,
        "bbox": BY_ORDER[9]["bbox"],
        "caption_verbatim": TABLE_CAP_2,
        "caption_source": "text-layer",
        "note": "twelve rows, one per model, numbers right-aligned inside columns that are "
                "divided by rules; the header carries the statistic name rather than a unit",
        "place": {
            "section_path": clean(BY_ORDER[9]["section_path"]),
            "section_numbered": True,
            "section_kind": BY_ORDER[9]["section_kind"],
            "doc_order": BY_ORDER[9]["doc_order"],
            "page_order": BY_ORDER[9]["page_order"],
            "page_zone": BY_ORDER[9]["page_zone"],
            "area_frac": BY_ORDER[9]["area_frac"],
            "solo_page": False,
        },
        "mention": mention(20, first=18, style=["Table 2"], count=1,
                           lead=span(18, "This can be found in Table 2", "Table 2"),
                           trail=span(18, "All of our models", "outperform the random model"),
                           pattern="direct", read=1, gap=2),
        "caption": table_caption(TABLE_CAP_2, cond=False, vars_=0),
        "table": {
            "rows": 12,
            "cols": 3,
            "header_rows": 1,
            "rule_style": "vertical-rules",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": 2,
            "text_cols": 1,
            "width": "column",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    },
]

EXCLUDED = [
    (4, "fragment-of-other", "right panel (b) of Figure 2"),
    (6, "fragment-of-other", "right panel (b) of Figure 3"),
    (11, "fragment-of-other", "panel (b) of the Figure 6 weight sweep"),
    (12, "fragment-of-other", "panel (c) of the Figure 6 weight sweep"),
    (13, "fragment-of-other", "panel (d) of the Figure 6 weight sweep"),
    (14, "fragment-of-other", "panel (e) of the Figure 6 weight sweep"),
    (16, "fragment-of-other", "right panel (b) of Figure 7, the ellipse overlay"),
    (18, "fragment-of-other", "right panel (b) of Figure 8, the probability surface"),
]

RULES = [
    "本题型把概率场画成连续彩虹栅格，色标一律竖排在坐标框外、顶端 high 底端 low、"
    "旁注 Next Crime Probability，题注不再解释色序 [geometry.colorbar]，[geometry.legend]。",
    "同一模型的两种设定用 (a)/(b) 并排，权重不同的五连图用 (a)-(e) 三行排布，"
    "具体权值写在子题注里而不写进主题注 [geometry.panel_layout]，[geometry.panel_count]。",
    "对照实验用另一种画法：单选题式的横条图配红色置信须、单折线配误差棒，"
    "两者都带完整坐标刻度，与概率场图不共用一套样式 [geometry.printed_numbers]，"
    "[geometry.family]。",
    "地图类图不画色标而画形状：标准差矩形与椭圆直接叠在经纬度散点上，"
    "靠几何形状而非灰度传意 [geometry.family]，[geometry.colorbar]。",
    "图 8 是唯一复合面板：左半是 Google 底图散点，右半是同一窗口的概率面，"
    "底图与场图并置 [geometry.panel_layout]。",
    "正文引出几乎全是直陈式（see Figure N、can be found in Figure N、as seen in Figure N），"
    "全篇没有 Figure N shows [mention.lead_pattern]。",
    "图后解读句只解释图形本身：先说图中变量含义（In this figure k is equal to...），"
    "再说结果强弱（No patterns emerge...），最后才给判断 [mention.trail_sentence]。",
    "Figure 7 在方法章就被提前引用（See Figure 7 for an illustration of these percentile "
    "areas），实际出现在案例章，前置距离跨 9 页，是全篇最长的引言-图距 [mention.first_page]，"
    "[mention.lead_pages]。",
    "图 8 的题注越界写结论（suggests that the Bradford area is at the highest risk of "
    "attack），是唯一在题注里下判断的图 [caption.concludes]。",
    "表格固定三列：第一列文字描述、后两列数值，全部带竖线分隔、单行表头、无隔行底纹、"
    "无合并单元格，数值列不按小数点对齐 [table.rule_style]，[table.zebra]，"
    "[table.merged_cells]，[table.decimal_aligned]。",
    "表题在表上方、图题在图下方，两条都用冒号编号；表题只说统计量名称，"
    "单位与样本量都留在表头里 [caption.position]，[caption.numbering]，"
    "[table.units_in_header]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": BY_ORDER[order]["page"], "bbox": BY_ORDER[order]["bbox"],
         "reason": reason, "note": note}
        for order, reason, note in EXCLUDED
    ],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload7.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items + {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out.name}")
