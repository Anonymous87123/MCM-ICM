"""Hand pass for P-B-2010-8362-bd23db32 (geographic profiling, 31 panels + 2 tables).

The paper is built around one picture repeated: a jet-ramp probability surface over the
same lat/long window, redrawn once per distance-decay function and once per weighting
choice, with the panel letter under the image and no main figure caption at all. Panels
(a)-(f) sit on pages 22-23 on a synthetic 0-100 grid; (g)-(t) on pages 28-32 on the real
Yorkshire window. Every surface carries black crime dots, and the Criminal Location
panels add a red star at the offender's true home. No colour bar anywhere: the ramp is
labelled only by the words high/low inside the picture.

Four unnumbered point schematics on pages 9-10 use a second grammar: red crime dots,
one dark mean-centre dot, two dashed standard-distance rings.

Two tables, both booktabs: the results table on page 25 and the 52-row appendix listing
on page 27. The page-25 crop covers only the header band of the results table, whose
body is ordinary text-layer type; the note records that.

Four measured vector strips are code listings and a displayed equation, not exhibits.

Usage: python -I tools/_dist_paper8.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2010-8362-bd23db32"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}


def clean(path: list[str]) -> list[str]:
    return [p for p in path if not re.search(r"\s\d+$", p)]


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def lines(page: int) -> list[str]:
    return [schema.norm(l) for l in (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()]


def cap_line(page: int, prefix: str) -> str:
    """One-line caption, e.g. 'Figure 1: A decay plot.' — these do not wrap."""
    return next(l for l in lines(page) if l.startswith(prefix))


def span(page: int, start: str, end: str) -> str:
    t = text(page)
    i = t.find(start)
    assert i >= 0, f"start {start!r} not on page {page}"
    j = t.find(end, i)
    assert j >= 0, f"end {end!r} not after start on page {page}"
    q = t[i:j + len(end)]
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def caption(v: str, source: str = "text-layer", *, vars_: int = 0,
            cond: bool = False, concl: bool = False) -> dict:
    return {
        "verbatim": v,
        "source": source,
        "numbering": "none",
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": False,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": cond,
        "concludes": concl,
        "voice": "none",
        "position": "below",
    }


def fig_caption(v: str, *, vars_: int = 0, cond: bool = False,
                concl: bool = False) -> dict:
    d = caption(v, "text-layer", vars_=vars_, cond=cond, concl=concl)
    d["numbering"] = "Figure N:"
    return d


def no_mention() -> dict:
    return {
        "first_page": None,
        "lead_pages": None,
        "style": [],
        "count": 0,
        "lead_sentence": "",
        "trail_sentence": "",
        "lead_pattern": "none",
        "read_sentences": 0,
        "gap_sentences": None,
    }


def entry(order: int, family: str, panels: int, panel_layout: str, capt: dict,
          men: dict | None = None, *, legend: str = "none",
          colorbar: bool = False, printed: bool = True, labels: bool = False,
          shared: bool = False, note: str = "", other_note: str = "") -> dict:
    s = BY_ORDER[order]
    item = {
        "page": s["page"],
        "bbox": s["bbox"],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": capt["verbatim"],
        "caption_source": ("none" if not capt["verbatim"]
                           else capt.get("source") or "text-layer"),
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
        "mention": men or no_mention(),
        "caption": capt,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": panel_layout,
            "shared_axes": shared,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": "no",
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    return item


def surface_sub(letter: str, v: str, *, cond: bool = True) -> dict:
    """The (a)-(t) sub-captions: assembled from two halves split by the column wrap."""
    d = caption(v, "typed-from-crop", cond=cond)
    d["sub_number"] = letter
    return d


ITEMS = [
    entry(1, "scatter", 1, "1", caption(""),
          printed=False, labels=True,
          note="uniform spread: about thirty red dots on a square lattice, one dark centre "
               "dot, two dashed standard-distance rings; no axes, no numbers, no name"),

    entry(2, "scatter", 1, "1", caption(""),
          printed=False, labels=True,
          note="ring spread: about twenty dots on a rounded square outline around the dark "
               "centre dot, with an inner and an outer dashed ring"),

    entry(3, "scatter", 1, "1", caption(""),
          printed=False, labels=True,
          note="linear spread: one horizontal row of red dots symmetric about the centre "
               "dot, two dashed rings cutting the row"),

    entry(4, "scatter", 1, "1", caption(""),
          printed=False, labels=True,
          note="clustering: two dense blocks of red dots either side of the centre dot, "
               "the inner dashed ring passing between the blocks"),

    entry(5, "line", 1, "1",
          fig_caption(cap_line(11, "Figure 1:"), vars_=0),
          {
              "first_page": 10,
              "lead_pages": 1,
              "style": ["Figure 1"],
              "count": 1,
              "lead_sentence": span(10, "assumes drop-off of likelihood", "(see Figure 1)"),
              "trail_sentence": "",
              "lead_pattern": "parenthetical",
              "read_sentences": 1,
              "gap_sentences": 1,
          },
          legend="inside",
          note="four decay curves on 0-10 with a boxed key upper right: Linear dashed, "
               "Normal peaked at 4, NE decaying, Truncated NE peaking at 2; y is labelled "
               "Crime Probability (Unnormalized)"),

    entry(6, "heatmap-or-contour", 1, "1",
          fig_caption(cap_line(13, "Figure 2:"), vars_=1),
          note="the paper's first probability surface: red core upper right, a red star "
               "at the offender's base, about a dozen black crime dots along the top band; "
               "no colour bar, the ramp is unlabelled"),

    entry(7, "heatmap-or-contour", 1, "1", caption(""), printed=True,
          note="killer-location surface on a synthetic 0-10 grid with two vertically "
               "stacked lobes and eleven dots; in-plot title only, no caption"),

    entry(8, "heatmap-or-contour", 2, "1x2",
          fig_caption(cap_line(18, "Figure 3:"), vars_=1),
          shared=True, printed=True,
          note="(a) No buffer. and (b) 30% buffer. sit under the two panels; the field "
               "is identical except that the 30% boundary buffer stops the mass piling up "
               "at the frame edge"),

    entry(10, "scatter", 1, "1",
          dict(fig_caption("Predicted Nth crime in red; actual Nth crime in black."),
               source="typed-from-crop"),
          note="Chester Turner kill dates on a 1986-2000 axis, red dots rising, one black "
               "star above the cloud; the caption is split by the column wrap and only "
               "reassembled here, hence typed-from-crop"),

    entry(11, "line", 1, "1", fig_caption(cap_line(21, "Figure 5:")),
          note="the time weight function on 0-100 days: one smooth decaying curve, title "
               "inside the frame, no legend, no key"),
]

SUB = [
    (12, "a", "(a) Next Crime Probability Plot with unweighted time, uncorrelated points.",
     "uncorrelated, unweighted: ridge running SSW-NNE, dots in two low/high-latitude "
     "clusters, in-plot title Uncorrelated Unweighted"),
    (13, "b", "(b) Next Crime Probability Plot with weighted time, uncorrelated points.",
     "uncorrelated, weighted: the same ridge split into two deep lobes; dots unmoved"),
    (14, "c", "(c) Next Crime Probability Plot with unweighted time, correlated points.",
     "correlated, unweighted: one elongated ellipse of mass from lat 10 to 80"),
    (15, "d", "(d) Next Crime Probability Plot with weighted time, correlated points.",
     "correlated, weighted: the most saturated field of the six, dark red over most of "
     "the frame"),
    (16, "e", "(e) Criminal Location Probability Plot with unweighted time, correlated points.",
     "offender-location surface, weak: one compact red peak at low latitude plus a second "
     "maximum near the top edge"),
    (17, "f", "(f) Criminal Location Probability Plot with weighted time, correlated points.",
     "offender-location surface, weighted: two clear maxima joined by a yellow saddle"),
    (20, "g", "(g) Criminal Location Probability Plot of Sutcliffe using Linear decay function.",
     "linear decay on the real Yorkshire window: one broad red peak near longitude -1.7, "
     "red star just above it"),
    (21, "h", "(h) Next Crime Probability Plot of Sutcliffe using Linear decay function.",
     "next-crime surface for the same model: a single concentric hotspot at -1.70, 53.82, "
     "dots ringing and inside it"),
    (22, "i", "(i) Criminal Location Probability Plot of Sutcliffe using Negative Exponential decay function.",
     "negative exponential: tight red kernel at -1.6, 53.82 with the dots chained north-south"),
    (23, "j", "(j) Next Crime Probability Plot of Sutcliffe using Negative Exponential decay function.",
     "next-crime surface for negative exponential: much broader red core reaching -1.55"),
    (24, "k", "(k) Criminal Location Probability Plot of Sutcliffe using Truncated Negative Exponential decay function.",
     "truncated negative exponential: the same core with a yellow tongue reaching west to -1.8"),
    (25, "l", "(l) Criminal Location Probability Plot of Sutcliffe using Truncated Negative Exponential decay function.",
     "next-crime surface for the truncated function: one diffuse blob, no sharp kernel"),
    (26, "m", "(m) Criminal Location Probability Plot of Sutcliffe using Plateaud Negative Exponential decay function.",
     "plateaued negative exponential: hot core at -1.6 with a narrow cyan neck west"),
    (27, "n", "(n) Next Crime Probability Plot of Sutcliffe using Plateaued Negative Exponential decay function.",
     "next-crime surface for the plateaued function: an even red disc over the window"),
    (28, "o", "(o) Criminal Location Probability Plot of Sutcliffe using Normal decay function.",
     "normal decay: banded core at -1.6 with the widest cyan halo of the set"),
    (29, "p", "(p) Next Crime Probability Plot of Sutcliffe using Normal function.",
     "next-crime surface for the normal function: one large diffuse hotspot right of centre"),
    (30, "q", "(q) Criminal Location Probability Plot of Sutcliffe using Negative Exponential decay function, time weighted.",
     "time-weighted negative exponential: mid-left bump plus one tight peak at -1.58"),
    (31, "r", "(r) Next Crime Probability Plot of Sutcliffe using Negative Exponential function, time weighted.",
     "time-weighted next-crime surface: broad red band filling the upper right"),
    (32, "s", "(s) Criminal Location Probability Plot of Sutcliffe using Negative Exponential decay function, time weighted.",
     "the Chester Turner page reuses the Sutcliffe wording; field near-identical to (q)"),
    (33, "t", "(t) Next Crime Probability Plot of Sutcliffe using Negative Exponential function, time weighted.",
     "the Chester Turner page again; red band across the upper right, near-identical to (r)"),
]

for order, letter, verbatim, note in SUB:
    ITEMS.append(entry(order, "heatmap-or-contour", 1, "1",
                       surface_sub(letter, verbatim), printed=True, note=note))

ITEMS.sort(key=lambda it: it["place"]["doc_order"])

TABLE_1_CAP = "Table 1: Search Costs / Error Distance using various functions for both the Sutcliffe and Chester Turner data."

TABLES = [
    {
        "page": 25,
        "bbox": BY_ORDER[18]["bbox"],
        "caption_verbatim": TABLE_1_CAP,
        "caption_source": "text-layer",
        "note": "the measured crop is only the header band of this table — the body is "
                "ordinary text-layer type, so the region and the table do not coincide",
        "place": {
            "section_path": clean(BY_ORDER[18]["section_path"]),
            "section_numbered": True,
            "section_kind": BY_ORDER[18]["section_kind"],
            "doc_order": BY_ORDER[18]["doc_order"],
            "page_order": BY_ORDER[18]["page_order"],
            "page_zone": BY_ORDER[18]["page_zone"],
            "area_frac": BY_ORDER[18]["area_frac"],
            "solo_page": False,
        },
        "mention": no_mention(),
        "caption": {
            "verbatim": TABLE_1_CAP,
            "numbering": "Table N:",
            "words": len(schema.words(TABLE_1_CAP)),
            "sentences": 1,
            "units": False,
            "variables": False,
            "variable_count": 0,
            "conditions": False,
            "concludes": False,
            "voice": "none",
            "position": "below",
        },
        "table": {
            "rows": 12,
            "cols": 5,
            "header_rows": 2,
            "rule_style": "booktabs",
            "zebra": False,
            "merged_cells": True,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": 4,
            "text_cols": 1,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    },
    {
        "page": 27,
        "bbox": BY_ORDER[19]["bbox"],
        "caption_verbatim": "",
        "caption_source": "none",
        "note": "appendix listing, no table caption: the title lives in the section head "
                "Appendix A Serial Killer Case Study Data",
        "place": {
            "section_path": clean(BY_ORDER[19]["section_path"]),
            "section_numbered": True,
            "section_kind": BY_ORDER[19]["section_kind"],
            "doc_order": BY_ORDER[19]["doc_order"],
            "page_order": BY_ORDER[19]["page_order"],
            "page_zone": BY_ORDER[19]["page_zone"],
            "area_frac": BY_ORDER[19]["area_frac"],
            "solo_page": False,
        },
        "mention": no_mention(),
        "caption": {
            "verbatim": "",
            "numbering": "none",
            "words": 0,
            "sentences": 0,
            "units": False,
            "variables": False,
            "variable_count": 0,
            "conditions": False,
            "concludes": False,
            "voice": "none",
            "position": "above",
        },
        "table": {
            "rows": 53,
            "cols": 4,
            "header_rows": 1,
            "rule_style": "booktabs",
            "zebra": False,
            "merged_cells": True,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": 2,
            "text_cols": 2,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    },
]

EXCLUDED = [
    (18, BY_ORDER[9]["bbox"], "fragment-of-other",
     "right panel (b) 30% buffer of Figure 3, the pair is one exhibit"),
    (14, [89.25, 417.94, 521.0, 530.52], "not-an-exhibit",
     "Program 1 listing, a ruled pseudocode float rather than a figure"),
    (17, [89.25, 592.2, 521.0, 649.48], "not-an-exhibit",
     "Program 2 listing, ruled pseudocode float"),
    (20, [89.25, 117.52, 521.0, 147.17], "not-an-exhibit",
     "Program 3 listing header band"),
    (20, [89.25, 621.1, 521.0, 692.82], "not-an-exhibit",
     "Program 3 listing tail"),
]

RULES = [
    "本题型的主图是一族概率面：同一经纬窗口被反复重绘，每次只换距离衰减函数或是否时间加权，"
    "图内标题固定写 Criminal Location Probability / Next Crime Probability，"
    "题注只补一句用哪个函数 [geometry.family]，[caption.verbatim]。",
    "概率面全篇不画色标、不画图例块，色阶含义靠正文事先交代；"
    "因此 colorbar 字段一律 false，量级差异改用相邻表格承载 [geometry.colorbar]，"
    "[table.rule_style]。",
    "面板用 (a)-(t) 小写括号字母编号、标在每张图下方，全篇没有主图题；"
    "一组二十张图跨五页连排，只靠子题注区分 [caption.numbering]，"
    "[caption.position]，[geometry.panel_count]。",
    "子题注句式固定：字母 + Criminal/Next Crime Probability Plot of <犯人> using <函数> "
    "[decay] function[，time weighted]；函数名换、句式不换 [caption.verbatim]。",
    "复制痕迹可作为反面模板：Chester Turner 那页的 (s)(t) 仍写 of Sutcliffe，"
    "与页内标题矛盾，只能靠页眉标题识别 [caption.verbatim]。",
    "示意图走另一套画法：红点=犯罪点、深点=均值中心、两条虚线=一倍与二倍标准差圆，"
    "四张（均匀、环形、线状、双簇）连画法都不改，且全部无刻度无编号 [geometry.family]，"
    "[geometry.printed_numbers]。",
    "概率面上叠的符号有分工：黑点=已知犯罪点，红色五角星=真凶实际居所，"
    "星标只出现在 Criminal Location Probability 图，Next Crime 图不标 [geometry.data_labels]。",
    "正文对这批图的引用极少（只有 Figure 1 一处括号回指），说明其余靠图内标题自明 "
    "[mention.lead_pattern]，[mention.count]。",
    "表格一律 booktabs：横线只在表头下与分组之间，无竖线、无隔行底纹；"
    "分组名合并在首列跨行 [table.rule_style]，[table.zebra]，[table.merged_cells]。",
    "附录数据表把 52 行按犯人分五组连排、只留一行表头、不另给表题，"
    "标识放在节标题里 [table.rows]，[caption.numbering]。",
    "图表按章分工：方法章放衰减函数曲线与四张示意散点，结果章放概率面与时间散点，"
    "附录放原始经纬度表 [place.section_kind]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": pg, "bbox": bbox, "reason": reason, "note": note}
        for pg, bbox, reason, note in EXCLUDED
    ],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload8.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items + {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out.name}")
