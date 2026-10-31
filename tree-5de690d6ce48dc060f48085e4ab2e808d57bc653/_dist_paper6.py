"""Hand pass for P-B-2010-7507-24d34e5d (crime geography, 16 figures + 1 table).

The paper runs one template eleven times: a plan-view jet heatmap with a colour bar
and an in-plot legend, and — for the model-output figures — its paired 3D surface
directly beneath it. Captions stay one line and name the offender, the model and the
(a)/(b) panels; the in-plot titles carry the numbers ("effectiveness ratio 15.8163"),
which is why the caption never repeats them.

Two flow charts, a dendrogram, a silhouette line, a four-colour cluster scatter, and
one 3x4 table with vertical rules. The six measured boxes inside the Figure 2 chart are
fragments of the chart, and each paired surface is a fragment of its plan-view heat map;
page 1 is the contest control sheet.

Usage: python -I tools/_dist_paper6.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2010-7507-24d34e5d"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}


def clean(path: list[str]) -> list[str]:
    """Drop the table-of-contents copies that carry the page number in the label."""
    out = []
    for part in path:
        if re.search(r"\s\d+$", part) and len(part) > 12:
            continue
        out.append(part)
    return out


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def lines(page: int) -> list[str]:
    return [schema.norm(l) for l in (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()]


def cap(page: int, number: int) -> str:
    ls = lines(page)
    start = next(i for i, l in enumerate(ls) if re.match(rf"Figure\s+{number}:", l))
    out = [ls[start]]
    for nxt in ls[start + 1:]:
        if not nxt or re.match(r"Figure\s+\d", nxt):
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


def caption(page: int, number: int, *, units: bool, vars_: int, cond: bool,
            concl: bool, voice: str) -> dict:
    v = cap(page, number)
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


def mention(page: int, *, first: int | None, style: list[str], count: int,
            lead: str = "", pattern: str = "none", read: int = 0,
            gap: int | None = None) -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": count,
        "lead_sentence": lead,
        "trail_sentence": "",
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": gap,
    }


def entry(order: int, family: str, panels: int, layout: str, capt: dict,
          men: dict, *, legend: str = "none", colorbar: bool = False,
          three_d: str = "no", printed: bool = True, labels: bool = False,
          confidence: str = "high", note: str = "",
          other_note: str = "") -> dict:
    s = BY_ORDER[order]
    item = {
        "page": s["page"],
        "bbox": s["bbox"],
        "family": family,
        "confidence": confidence,
        "panel_count": panels,
        "caption_verbatim": capt["verbatim"],
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
        "caption": capt,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
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


def pair(order: int, capt: dict, men: dict, *, legend: str = "inside",
         note: str = "") -> dict:
    """The recurring (a) heat map over (b) surface: one exhibit, two measured rows."""
    return entry(order, "composite-panel", 2, "2x1", capt, men,
                 legend=legend, colorbar=True, three_d="surface-mesh",
                 printed=True, note=note)


ITEMS = [
    entry(2, "composite-panel", 2, "1x2",
          caption(13, 1, units=False, vars_=0, cond=False, concl=False,
                  voice="passive"),
          mention(13, first=12, style=["Figure 1"], count=1,
                  lead=span(12, "The clearest spacial", "(see Figure 1)"),
                  pattern="parenthetical", read=1, gap=1),
          legend="inside", printed=True,
          note="left is the journal map of Offender B's rapes and burglaries with "
               "its own symbol key, right is the scatter re-plotted in 50 m grid "
               "units from the same data"),

    entry(3, "flowchart-or-schematic", 1, "1",
          caption(17, 2, units=False, vars_=0, cond=False, concl=False, voice="none"),
          mention(17, first=16, style=["Figure 2"], count=1,
                  lead=span(16, "Figure 2 is the algorithm", "single anchor point"),
                  pattern="figure-n-shows", read=1, gap=1),
          printed=False, labels=True,
          note="six boxes in one top-down chain, terminators blue rectangles, "
               "processes ovals, the weighting step outlined green"),

    entry(4, "line", 2, "1x2",
          caption(19, 3, units=False, vars_=1, cond=False, concl=False, voice="none"),
          mention(19, first=18, style=["Figure 3"], count=1,
                  lead=span(18, "Figure 3 displays two plots", "shape of the"),
                  pattern="figure-n-shows", read=1, gap=1),
          printed=True,
          note="two gamma densities side by side, k=1 and k=4, each on its own "
               "L-frame axes with pdf against r; the parameters are printed under "
               "the panels as (a)/(b), not in the caption"),

    entry(6, "heatmap-or-contour", 1, "1",
          caption(20, 4, units=False, vars_=0, cond=True, concl=False, voice="active"),
          mention(20, first=19, style=["Figure 4"], count=1,
                  lead=span(19, "Applying this method to the set of crime locations",
                            "Figure 4"),
                  pattern="as-shown-in", read=1, gap=1),
          legend="inside", colorbar=True, printed=True,
          note="the only heat map without a paired surface: point-source centroid on "
               "500 m grid units, colour bar times 10^5"),

    pair(7, caption(21, 5, units=False, vars_=0, cond=False, concl=False,
                    voice="none"),
         mention(21, first=None, style=[], count=0, read=0, gap=None),
         note="Offender C under the centroid model: crater heat map on a 50 m grid, "
              "1.8e-3 peak, the surface underneath shows the same single spike"),

    pair(9, caption(23, 6, units=False, vars_=0, cond=False, concl=False,
                    voice="none"),
         mention(23, first=22, style=["Figure 6"], count=1,
                 lead=span(22, "Our second test data-set", "(see Figure 6)"),
                 pattern="parenthetical", read=1, gap=1),
         note="annular crater: the heat map has a hole at the centre and the "
              "surface shows the matching notch at the apex; the (b) sub-caption "
              "still says Offender C, a copy error"),

    pair(11, caption(24, 7, units=False, vars_=0, cond=False, concl=False,
                     voice="none"),
         mention(24, first=22, style=["Figure 7"], count=1,
                 lead=span(22, "In this case, the last crime", "(see Figure 7)"),
                 pattern="parenthetical", read=1, gap=2),
         note="Offender A: the outlier crime sits outside the density core, and the "
              "(b) sub-caption is again the wrong offender"),

    entry(13, "flowchart-or-schematic", 1, "1",
          caption(26, 8, units=False, vars_=0, cond=False, concl=False, voice="none"),
          mention(26, first=25, style=["Figure 8"], count=1,
                  lead=span(25, "A sketch of the algorithm can be seen in Figure 8",
                            "Figure 8"),
                  pattern="as-shown-in", read=1, gap=1),
          printed=False, labels=True,
          note="nine boxes: terminator, cluster-and-group, a purple for-each hexagon, "
               "four purple process ovals, combine, terminator, plus a purple loop "
               "arrow returning from the temporal step to the for-each box"),

    entry(14, "other", 1, "1",
          caption(27, 9, units=False, vars_=0, cond=False, concl=False, voice="none"),
          mention(27, first=25, style=["Figure 9"], count=1,
                  lead=span(25, "The dendrogram for Offender B is seen in Figure 9",
                            "Figure 9"),
                  pattern="as-shown-in", read=1, gap=2),
          printed=True,
          other_note="dendrogram: a merge tree, not a network of entities — 15 "
                     "numbered leaves on the x axis, Gap Distance on the y, root at 8",
          note="upright tree, tallest merge near Gap Distance 6.2, lowest near 1.0"),

    entry(15, "line", 1, "1",
          caption(28, 10, units=False, vars_=0, cond=True, concl=False, voice="none"),
          mention(28, first=27, style=["Figure 10"], count=1,
                  lead=span(27, "A sample plot of average Silhouette", "Figure 10"),
                  pattern="as-shown-in", read=1, gap=1),
          printed=True,
          note="one solid curve over 1.5-4.5 clusters with three markers at k=2,3,4; "
               "framed on all four sides unlike the density plots"),

    entry(16, "scatter", 1, "1",
          caption(28, 11, units=False, vars_=0, cond=True, concl=False, voice="passive"),
          mention(28, first=27, style=["Figure 11"], count=1,
                  lead=span(27, "The cluster groupings computed", "Figure 11"),
                  pattern="as-shown-in", read=1, gap=1),
          printed=True,
          note="fifteen points in four colour classes on 100 m units; colour carries "
               "cluster identity, not magnitude, so it is a categorical scatter"),

    pair(17, caption(32, 12, units=False, vars_=0, cond=False, concl=False,
                     voice="none"),
         mention(32, first=None, style=[], count=0, read=0, gap=None),
         note="cluster model for Offender C: elongated NE-SW core, two-shouldered "
              "surface, ratio 15.8163 in the in-plot title"),

    pair(19, caption(33, 13, units=False, vars_=0, cond=False, concl=False,
                     voice="none"),
         mention(33, first=30, style=["Figure 13"], count=1,
                 lead=span(30, "Testing with Offender B", "(see Figure 13)"),
                 pattern="parenthetical", read=1, gap=3),
         note="three separate hot cores in the plan view, three peaks on the surface"),

    pair(21, caption(34, 14, units=False, vars_=0, cond=False, concl=False,
                     voice="none"),
         mention(34, first=30, style=["Figure 14"], count=1,
                 lead=span(30, "the cluster model fares no better", "(see Figure 14)"),
                 pattern="parenthetical", read=1, gap=4),
         note="one hot core plus a narrow secondary spike; ratio 0.0010833, the "
              "failure case"),

    entry(23, "line", 1, "1",
          caption(36, 15, units=False, vars_=0, cond=False, concl=False, voice="none"),
          mention(36, first=36, style=["Figure 15"], count=3,
                  lead=span(36, "In Figure 15 we see", "for Offender C"),
                  pattern="direct", read=1, gap=0),
          legend="inside", printed=True,
          note="running mean of the multiplier for both methods, key in a white box "
               "upper right"),

    entry(24, "line", 1, "1",
          caption(36, 16, units=False, vars_=0, cond=True, concl=False, voice="none"),
          mention(36, first=36, style=["Figure 16"], count=1,
                  lead=span(36, "In Figure 16 we see", "for Offender C"),
                  pattern="direct", read=1, gap=0),
          legend="inside", printed=True,
          note="per-crime multiplier, same key and same two methods; the blue curve "
               "spikes to 22 at crime 9 while the green one peaks at crime 5"),
]

TABLE = {
    "page": 37,
    "bbox": BY_ORDER[25]["bbox"],
    "caption_verbatim": "",
    "caption_source": "none",
    "note": "the only table: three offenders against the two multiplier statistics, "
            "no caption and no note line, numbers centred rather than decimal aligned",
    "place": {
        "section_path": clean(BY_ORDER[25]["section_path"]),
        "section_numbered": True,
        "section_kind": "result",
        "doc_order": BY_ORDER[25]["doc_order"],
        "page_order": BY_ORDER[25]["page_order"],
        "page_zone": BY_ORDER[25]["page_zone"],
        "area_frac": BY_ORDER[25]["area_frac"],
        "solo_page": False,
    },
    "mention": mention(37, first=None, style=[], count=0, read=0, gap=None),
    "caption": {
        "verbatim": "",
        "numbering": "none",
        "words": 0,
        "sentences": 0,
        "units": False,
        "variables": True,
        "variable_count": 2,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": "above",
    },
    "table": {
        "rows": 4,
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
}

EXCLUDED = [
    (1, [5.52, 27.18, 573.12, 172.78], "background",
     "MCM control sheet, not an exhibit"),
    (13, [283.18, 81.03, 513.58, 267.71], "fragment-of-other",
     "right panel of Figure 1, the pixel-analysis scatter"),
    (17, [253.53, 76.05, 357.66, 115.92], "fragment-of-other",
     "box 1 of the Figure 2 flow chart"),
    (17, [253.53, 127.31, 357.66, 167.99], "fragment-of-other",
     "box 2 of the Figure 2 flow chart"),
    (17, [253.53, 179.38, 357.66, 219.24], "fragment-of-other",
     "box 3 of the Figure 2 flow chart"),
    (17, [253.53, 230.63, 357.66, 270.5], "fragment-of-other",
     "box 4 of the Figure 2 flow chart"),
    (17, [253.53, 281.89, 357.66, 322.57], "fragment-of-other",
     "box 5 of the Figure 2 flow chart"),
    (17, [253.53, 333.96, 357.66, 373.82], "fragment-of-other",
     "box 6 of the Figure 2 flow chart"),
    (19, [312.97, 85.8, 516.53, 211.61], "fragment-of-other",
     "right panel (b) of Figure 3, the k=4 density"),
    (21, [162.0, 324.29, 450.01, 507.66], "fragment-of-other",
     "lower panel (b) of Figure 5, the surface"),
    (23, [162.0, 326.77, 450.01, 550.84], "fragment-of-other",
     "lower panel (b) of Figure 6, the surface"),
    (24, [162.0, 292.88, 450.0, 498.89], "fragment-of-other",
     "lower panel (b) of Figure 7, the surface"),
    (26, [306.0, 138.95, 355.24, 328.62], "fragment-of-other",
     "vector slice of the Figure 8 flow chart's middle boxes"),
    (32, [126.0, 343.08, 486.0, 559.08], "fragment-of-other",
     "lower panel (b) of Figure 12, the surface"),
    (33, [126.0, 382.2, 486.0, 626.45], "fragment-of-other",
     "lower panel (b) of Figure 13, the surface"),
    (34, [126.0, 343.12, 486.0, 588.34], "fragment-of-other",
     "lower panel (b) of Figure 14, the surface"),
]

RULES = [
    "本题型用一套固定模板反复出图：上图是平面热图（喷流色表 + 右侧色标 + 图内图例），"
    "下图是同一密度场的三维曲面，两图共用一个题注、(a)/(b) 标在图上而不写进题注 "
    "[geometry.panel_layout]，[geometry.colorbar]。",
    "热图一律带色标且色标顶端印科学计数倍数（x 10^4 / x 10^-3），"
    "题注不再重复数量级 [geometry.colorbar]，[caption.words]。",
    "图内图例固定放在右上角白框里，条目只有 Crimes / Next Crime 或 Cluster / Centred，"
    "map 面板则用 Rape/Burglary/Residence [geometry.legend]。",
    "题注极短（4-14 词），只写「谁 + 哪个模型 + (a)(b)」；"
    "数值结果（effectiveness ratio）写进图内标题，因此题注不下结论 [caption.words]，"
    "[caption.concludes]。",
    "同一题注被复制时连犯人不改：Figure 6、Figure 7 的 (b) 子标题仍写 Offender C，"
    "可从图内标题与题注的矛盾看出 [caption.verbatim]。",
    "算法用纵向流程图上而下走，框形分工固定：矩形=端点，椭圆=处理，六边形=循环，"
    "循环箭头用紫色单线回指 [geometry.panel_layout]，[geometry.data_labels]。",
    "聚类结果先给树状图（叶节点用案件编号），再给轮廓值曲线选簇数，"
    "最后给四色散点展示分簇，三步固定顺序 [geometry.family]。",
    "引用几乎全是括号回指 (see Figure N) 或 is shown in / is seen in 的顺叙，"
    "只有三处用 Figure N is/ displays 作主语 [mention.lead_pattern]。",
    "第三章之后图全部落在结果小节（7.2、8.2、9.1），"
    "算法图落在方法小节，指标体系图落在度量小节 [place.section_kind]。",
    "图为版心内单栏宽度（120-360 pt），成对图竖排占半页，"
    "没有一张图独占整页 [place.area_frac]，[place.solo_page]。",
    "全篇只有一张表，三列（犯人 + 两个统计量）、竖线分隔、无表题、无表注，"
    "数值居中不对齐小数点 [table.rule_style]，[table.decimal_aligned]，"
    "[table.note_sentence]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": [TABLE],
    "excluded_regions": [
        {"page": pg, "bbox": bbox, "reason": reason, "note": note}
        for pg, bbox, reason, note in EXCLUDED
    ],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload6.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items + 1 table, {len(EXCLUDED)} excluded -> {out.name}")
