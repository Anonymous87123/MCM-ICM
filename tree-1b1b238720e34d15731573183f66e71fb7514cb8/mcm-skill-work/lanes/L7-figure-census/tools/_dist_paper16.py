"""Hand pass for P-A-2011-9159-41b0c737 (halfpipe shape optimisation, 23 figures + 1 symbol table).

The shape of this paper is a fan-out: after the two survey figures (a competition photograph
and the cross-section diagram) and the symbol table, every later result is a small single-factor
plot. Section 4.2 emits three left/right pairs (Et-a and Et-b, one pair per friction regime),
section 4.3 emits six single-factor sensitivity curves, and section 5 closes with the 3D sketch
and two slope-angle figures. Panels are measured as separate regions but share one caption, and
that caption is the same sentence repeated verbatim in three places — the only mark of which
regime a pair belongs to is the second sentence of the caption ("Only the snow friction is
considered" and so on), which sits after the caption line and is not part of the quoted caption.

Two vocabulary notes. The team writes Fig N: with no period, so the census enum value Fig. N is
used for every caption; the table caption is written Tab 1:, which has no enum value at all, so
the caption is quoted but its numbering is recorded as none.

Page 19 prints two captions side by side and the text layer interleaves them line by line, so
only the first line of each is a quotable substring — recorded as such, not reconstructed.

Usage: python -I tools/_dist_paper16.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2011-9159-41b0c737"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
REG = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: x["bbox"][1]), 1):
        REG[(pg["page"], i)] = r["bbox"]

PAGE_W, PAGE_H = 612.0, 792.0

ORDER = [
    (5, 1), (6, 1), (7, 1),
    (12, 1), (12, 2), (12, 3), (12, 4),
    (13, 1), (13, 2),
    (14, 1), (14, 2),
    (15, 1), (15, 2),
    (16, 1), (16, 2), (16, 3),
    (17, 1), (17, 2), (17, 3), (17, 4),
    (18, 1), (18, 2),
    (19, 1), (19, 2),
]

S_INTRO = "1 Introduction"
S_SYM = "2 Symbols, Hypothesis and Explanations"
S_SYM1 = "2.1 Symbols Used in this Paper"
S_2D = "4 Application in 2D Case"
S_Q1 = "4.1 Quarter-Circle Type"
S_Q2 = "4.2 Quarter Ellipse Type"
S_Q21 = "4.2.1 Snow Friction Only"
S_Q22 = "4.2.2 Snow Friction and Collision"
S_Q23 = "4.2.3 Snow Friction, Air Friction and Collision"
S_SENS = "4.3 Sensitivity"
S_3D = "5 Application in 3D Case"


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


def caption(v: str, *, numbering: str = "Fig. N", cond: bool = False,
            concl: bool = False, units: bool = False, vars_: int = 0) -> dict:
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
        "voice": "none",
        "position": "below",
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
           printed: bool = True, labels: bool = False, panels: int = 1,
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


def curve(page: int, idx: int, cap: dict, men: dict, *, path: list[str], kind: str,
          series: int = 1, note: str, legend: str = "none", panels: int = 1,
          layout: str = "1", shared: bool = False) -> dict:
    return figure(page, idx, "line", cap, men, path=path, kind=kind, legend=legend,
                  printed=True, panels=panels, layout=layout, shared=shared,
                  note=note)


PARAM_NOTE = ("single black curve with circular markers; a plain framed box in the plot corner "
              "lists the fixed parameters (not series keys), so there is no legend proper")

ITEMS = [
    figure(5, 1, "photo-or-raster-image",
           caption("Fig 1: Snowboard competetion[1]"),
           mention(5, first=5, style=["Fig 1"], count=1),
           path=[S_INTRO], kind="introduction", printed=False,
           note="press photograph of a rider in flight above the pipe wall, printed in the "
                "right column with the caption line set at the foot of the left column, so the "
                "figure interrupts the introductory paragraph mid-sentence"),

    figure(6, 1, "flowchart-or-schematic",
           caption("Fig 2: Cross section of the halfpipe, perpendicular to the ground"),
           mention(6, first=6, style=["Fig. 2"], count=1,
                   lead="Symbols and corresponding parameters are shown in Tab. 1 and Fig. 2.",
                   pattern="direct"),
           path=[S_SYM, S_SYM1], kind="symbols", printed=False, labels=True,
           note="full-width engineering cross-section: deck, vert, transition and bottom named "
                "in lowercase inside the drawing, the rider drawn twice (launching left, "
                "landing right), dimension arrows for h0, hi, hf, x0, W and w, and plain black "
                "arrows for the direction of travel"),

    figure(12, 1, "line",
           caption("Fig 3: R∗ -w curve"),
           mention(12, first=11, style=["Fig. 3"], count=1,
                   lead=span(11, "For f = 9.0m", "Fig. 3"),
                   pattern="as-shown-in", read=1),
           path=[S_2D, S_Q1], kind="other",
           note="one black curve, dead flat across the frame at R* = 3.83 m: y axis R* 2.5-5.0, "
                "x axis w (m) 4-14; a framed box in the top right lists hi = 9 m, mu = 0.1 and "
                "x0 = 0.5 m, the conditions under which the curve was produced"),

    figure(12, 2, "line",
           caption("Fig 4: R∗ -µ curve"),
           mention(12, first=11, style=["Fig. 4"], count=1,
                   lead="The result is in Fig. 4.", pattern="as-shown-in", read=1),
           path=[S_2D, S_Q1], kind="other",
           note="one black curve falling from R* = 6.0 to 3.8 as mu runs 0.03-0.12, with the "
                "parameter box (w = 9 m, hi = 9 m, x0 = 0.5 m) in the top right"),

    curve(12, 3,
          caption("Fig 5: R∗ -hi curve"),
          mention(12, first=11, style=["Fig. 5"], count=1,
                  lead=span(11, "Our result in Fig. 5 shows", "gradient 0.16."),
                  pattern="figure-n-shows", read=1),
          path=[S_2D, S_Q1], kind="other",
          note="one black curve rising almost linearly in hi with the gradient 0.16 the text "
               "quotes; parameter box (w = 9 m, mu = 0.1, x0 = 0.5 m) at the lower right"),

    curve(12, 4,
          caption("Fig 6: R∗ -x0 curve"),
          mention(12, first=11, style=["Fig. 6"], count=1,
                  lead=span(11, "According to our numerical results in Fig. 6", "to decrease."),
                  pattern="as-shown-in", read=1),
          path=[S_2D, S_Q1], kind="other",
          note="one saturating black curve against the landing position x0, flattening at the "
               "pipe height; parameter box (w = 9 m, hi = 9 m, mu = 0.1) at the lower right"),

    curve(13, 1,
          caption("Fig 7: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(13, first=13, style=["Fig. 7"], count=1,
                  lead=span(13, "It is shown in Fig. 7 that", "tends to zero"),
                  pattern="figure-n-shows", read=1),
          path=[S_Q2, S_Q21], kind="other", series=3, legend="inside",
          note="left panel of a side-by-side pair: three curves in black (b = 4.5 m), red "
               "(b = 3.6 m) and blue (b = 2.7 m) that collapse onto each other after the "
               "sharp drop; the legend box in the upper right carries the three series keys "
               "and, underneath and undivided from them, the fixed mu = 0.1 and Ei = 6.6 kJ"),

    curve(13, 2,
          caption("Fig 7: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(13, first=13, style=["Fig. 7"], count=1,
                  lead=span(13, "It is shown in Fig. 7 that", "tends to zero"),
                  pattern="figure-n-shows", read=1),
          path=[S_Q2, S_Q21], kind="other", series=3, legend="inside",
          note="right panel of Fig. 7: three curves, black (a = 6.3 m), red (a = 4.5 m) and "
               "blue (a = 2.7 m), each decaying then levelling; same legend box, keys on top "
               "and the fixed mu, Ei below them"),

    curve(14, 1,
          caption("Fig 8: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(14, first=14, style=["Fig. 8"], count=2,
                  lead="By re-conducting the calculation before, we get Fig. 8.",
                  pattern="as-shown-in", read=1,
                  trail=span(14, "for each a in Fig. 8", "b gets larger.")),
          path=[S_Q2, S_Q22], kind="other", series=3, legend="above",
          note="left panel of Fig. 8, the collision regime: three curves (black, red, blue) "
               "with a peak marked by an upward arrow on each; the key box sits above the axes "
               "and spans the panel width, listing the series keys, the fixed parameters and a "
               "separate Peak arrow key"),

    curve(14, 2,
          caption("Fig 8: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(14, first=14, style=["Fig. 8"], count=2,
                  lead="By re-conducting the calculation before, we get Fig. 8.",
                  pattern="as-shown-in", read=1,
                  trail=span(14, "for each a in Fig. 8", "b gets larger.")),
          path=[S_Q2, S_Q22], kind="other", series=3, legend="inside",
          note="right panel of Fig. 8: three near-coincident curves (black, red, blue) against "
               "b, legend box inside at mid-right with the series keys plus mu, Ei and x0"),

    curve(15, 1,
          caption("Fig 9: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(15, first=15, style=["Fig. 9"], count=1,
                  lead=span(15, "Our result in Fig. 9 shows", "on the boundary."),
                  pattern="figure-n-shows", read=1),
          path=[S_Q2, S_Q23], kind="other", series=3, legend="above",
          note="left panel of Fig. 9, air friction added: three curves (black, red, blue) with "
               "peak arrows; legend above the axes spanning the panel, series keys plus the "
               "fixed parameters and the Peak key"),

    curve(15, 2,
          caption("Fig 9: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(15, first=15, style=["Fig. 9"], count=1,
                  lead=span(15, "Our result in Fig. 9 shows", "on the boundary."),
                  pattern="figure-n-shows", read=1),
          path=[S_Q2, S_Q23], kind="other", series=3, legend="inside",
          note="right panel of Fig. 9: three curves against b that converge then split, legend "
               "inside at the right edge with keys and fixed parameters"),

    curve(16, 1,
          caption("Fig 10: a∗ -x0 curve"),
          mention(16, first=16, style=["Fig. 10"], count=1,
                  lead=span(16, "The result is shown in Fig. 10", "Fig. 10"),
                  pattern="as-shown-in"),
          path=[S_SENS], kind="sensitivity",
          note="sensitivity sweep for x0: " + PARAM_NOTE + " (mu = 0.1, b = 5.4 m, "
               "Ei = 6.6 kJ, alpha = 0.75 Ns/m3); U-shaped with a minimum near x0 = 0.45 m, "
               "the turn the text calls surprising"),

    curve(16, 2,
          caption("Fig 11: a∗ -hi curve"),
          mention(16, first=16, style=["Fig. 11"], count=1,
                  lead="The result is shown in Fig. 11.", pattern="as-shown-in"),
          path=[S_SENS], kind="sensitivity",
          note="sensitivity sweep for hi: " + PARAM_NOTE + "; the curve falls monotonically "
               "and the text reports s = -2.110 at h0 = 9.0 m"),

    curve(16, 3,
          caption("Fig 12: a∗ -α curve"),
          mention(16, first=16, style=["Fig. 12"], count=1,
                  lead=span(16, "The result is shown in Fig. 12", "Fig. 12"),
                  pattern="as-shown-in"),
          path=[S_SENS], kind="sensitivity",
          note="sensitivity sweep for alpha: " + PARAM_NOTE + "; the curve rises almost "
               "linearly, which is how the paper shows wind barely moves a* (s = 0.011)"),

    curve(17, 1,
          caption("Fig 13: a∗ -h0 curve"),
          mention(17, first=16, style=["Fig. 13"], count=1,
                  lead="Our result in Fig. 13 shows that a∗ is sensitive to h0 , and s=2.374.",
                  pattern="figure-n-shows"),
          path=[S_SENS], kind="sensitivity",
          note="sensitivity sweep for h0: " + PARAM_NOTE + "; the strongest of the six, "
               "s = 2.374"),

    curve(17, 2,
          caption("Fig 14: a∗ -µ curve"),
          mention(17, first=16, style=["Fig. 14"], count=1,
                  lead="Changes of µ will affect the energy loss significantly as shown in "
                       "Fig. 14.",
                  pattern="as-shown-in"),
          path=[S_SENS], kind="sensitivity",
          note="sensitivity sweep for mu: " + PARAM_NOTE + "; nearly flat until 0.10 then "
               "rising steeply"),

    curve(17, 3,
          caption("Fig 15: a∗ -Ei curve"),
          mention(17, first=16, style=["Fig. 15"], count=1,
                  lead="The result is shown in Fig. 15, and s = -2.110.",
                  pattern="as-shown-in"),
          path=[S_SENS], kind="sensitivity",
          note="sensitivity sweep for Ei: " + PARAM_NOTE + "; duplicates the hi curve, which "
               "the text explains by calling the two factors equivalent when no rotation is "
               "involved"),

    figure(17, 4, "flowchart-or-schematic",
           caption("Fig 16: 3D halfpipe"),
           mention(17, first=17, style=["Fig. 16"], count=2,
                   lead="Fig. 16 is our sketch for a 3-dimensional halfpipe.", pattern="direct"),
           path=[S_3D], kind="other", printed=False, labels=True, three_d="isometric",
           note="line-drawn isometric sketch of the pipe as a long trough inside a rectangular "
                "casing, with dimension arrows for L, W and h0 and a dashed diagonal marking "
                "the slope angle phi; no axes, no ticks, no numbers"),

    curve(18, 1,
          caption("Fig 17: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(18, first=18, style=["Fig. 17"], count=1,
                  lead=span(18, "a∗ and b∗ are calculated numerically", "result is in Fig. 17."),
                  pattern="as-shown-in", read=1),
          path=[S_3D], kind="other", series=3, legend="outside-right",
          panels=3, layout="column of 3", shared=True,
          note="left half of Fig. 17: three stacked frames sharing one a (m) axis but each with "
               "its own narrow Ei (kJ) scale (8.60-8.70, 5.5-5.7, 2.2-2.4), one curve per frame "
               "for phi = 0 (black), 15 (red) and 30 degrees (blue), each with a peak arrow; the "
               "key box sits outside at the right of the stack"),

    curve(18, 2,
          caption("Fig 17: Left: Et -a curve under different b; Right: Et -b curve under "
                  "different a."),
          mention(18, first=18, style=["Fig. 17"], count=1,
                  lead=span(18, "a∗ and b∗ are calculated numerically", "result is in Fig. 17."),
                  pattern="as-shown-in", read=1),
          path=[S_3D], kind="other", series=3, legend="above",
          note="right half of Fig. 17: one frame, three curves for phi = 0, 15 and 30 degrees "
               "against b (m), no peak arrows; key box above the axes spanning the panel width, "
               "series keys plus fixed parameters"),

    curve(19, 1,
          caption("Fig 18: Left: Et -a curve under differ-"),
          mention(19, first=18, style=["Fig. 18"], count=1,
                  lead=span(18, "It turns out that a steeper slope", "shown in Fig. 18."),
                  pattern="as-shown-in", read=1),
          path=[S_3D], kind="other",
          note="sensitivity of a* to the slope angle: one black marker curve falling with phi, "
               "parameter box at the upper right. The caption is printed in two columns beside "
               "Fig. 19's and the text layer interleaves them line by line, so only its first "
               "line is quotable — the rest of the sentence reads 'ent b; Right: Et -b curve "
               "under differ- ent a.' and continues with the second sentence The snow friction "
               "and collision are considered"),

    curve(19, 2,
          caption("Fig 19: Left: Et -a curve under differ-"),
          mention(19, first=19, style=["Fig. 19"], count=1,
                  lead=span(19, "We calculate the hf", "in Fig. 19"),
                  pattern="as-shown-in", read=1),
          path=[S_3D], kind="other",
          note="the hf-phi curve with a horizontal reference line at hi = 9 m and an in-plot "
               "callout reading intersection point (17.1 degrees, 9 m); no legend box, the two "
               "annotations stand in for it. Caption text layer interleaved with Fig. 18's, so "
               "only the first line is quoted"),
]

TABLES = [
    {
        "page": 7,
        "bbox": REG[(7, 1)],
        "caption_verbatim": "Tab 1: Symbols used in this paper",
        "caption_source": "text-layer",
        "note": "two-column symbol glossary with the symbol column set in italic math and the "
                "quantity column in roman; nine body rows from m to L, one header row, a rule "
                "above and below and a doubled rule under the header, plus a single vertical "
                "rule between the two columns and no outer frame at the sides; no units, no "
                "numerals, no shading",
        "place": place(7, 1, [S_SYM, S_SYM1], "symbols"),
        "mention": mention(7, first=6, style=["Tab. 1"], count=1,
                           lead="Symbols and corresponding parameters are shown in Tab. 1 and "
                                "Fig. 2.",
                           pattern="direct"),
        "caption": caption("Tab 1: Symbols used in this paper", numbering="none"),
        "table": {"rows": 9, "cols": 2, "header_rows": 1, "rule_style": "vertical-rules",
                  "zebra": False, "merged_cells": False, "diagonal_header": False,
                  "units_in_header": False, "decimal_aligned": False, "numeric_cols": 0,
                  "text_cols": 2, "width": "full", "orientation": "portrait",
                  "continued": False, "note_sentence": ""},
    },
]

RULES = [
    "题注统一走 Fig N: 缩写体例（原稿无句点，本次按省缺记作 Fig. N），一律排在图形正下方，"
    "并排的左右两图共用一条题注、用 Left:/Right: 分栏 [caption.numbering]，"
    "[caption.position]，[caption.verbatim]。",
    "同一句题注在三种摩擦情形下逐字复用（Fig 7、8、9 完全同文），区分情形靠题注后面紧跟的"
    "第二句 The snow friction and collision are considered，不靠图号 [caption.words]，"
    "[caption.verbatim]。",
    "单曲线图不设图例，而在图角放一个方框列固定参数（hi=9m、µ=0.1、x0=0.5m），"
    "读者要把它当条件读，而不是当系列键 [geometry.legend]，[geometry.data_labels]。",
    "只有多曲线图（Fig 7-9、17）才给真图例，且方框上半部是系列键（b=4.5/3.6/2.7m）、"
    "下半部接着列固定参数，两部分不分隔 [geometry.legend]，[geometry.family]。",
    "4.2 三种摩擦情形各出一对 Et-a / Et-b 图，左右并排同高、共用题注，"
    "只有曲线形状与峰值箭头变化 [geometry.panel_count]，[place.page_order]。",
    "4.3 敏感性一节一个因子一张小图（Fig 10-15），单曲线加圆点标记，"
    "纵轴恒为 a*(m)、横轴换因子，文字里配一个 s 值 [place.section_kind]，"
    "[geometry.printed_numbers]。",
    "Fig 18 左图把三条 φ 曲线拆成三段竖排、共享同一横轴 a(m)，每段各自压缩量程以求拉开差异 "
    "[geometry.panel_count]，[geometry.shared_axes]。",
    "唯一的立体图（Fig 16）是线描等距透视图，只标 L、W、h0、φ 与虚线坡度，不画坐标箭头也不印刻度 "
    "[geometry.three_d]，[geometry.printed_numbers]。",
    "全套图形无三维曲面、无色标、无数据标签，颜色只承担红黑蓝三色区分 "
    "[geometry.three_d]，[geometry.colorbar]。",
    "正文引出以 The result is in Fig. N 为主，另有 Our result in Fig. N shows that…、"
    "It is shown in Fig. N that…、as shown in Fig. N 三种轮换 [mention.lead_pattern]，"
    "[mention.count]。",
    "引用与图面几乎同页或超前 1 页，只有 p12 排的两行四图被前移到 p11 末尾引用 "
    "[mention.lead_pages]，[mention.first_page]。",
    "符号表 Tab 1 不并入图号序列、题注在下、三线加一条竖分隔线，紧随其后就是假设清单 "
    "[table.rule_style]，[table.header_rows]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": 1, "bbox": REG[(1, 1)], "reason": "not-an-exhibit",
         "note": "summary-sheet control block: Team Control Number 9159, Problem Chosen A and "
                 "the office-use fill lines above the summary-sheet heading; page furniture"},
    ],
    "note": "25 measured regions: 23 figure regions (the panel pairs of Figs 7, 8, 9 and 17 "
            "are measured separately but share one caption), one symbol table (Tab 1) and the "
            "summary-sheet control block on page 1, which is excluded as page furniture. The "
            "team prints captions as Fig N: with no period, so every caption is recorded under "
            "the Fig. N enum; Tab 1: has no enum value and is recorded as numbering none with "
            "the caption still quoted verbatim. On page 19 the two captions are set side by "
            "side and the text layer interleaves them line by line, so only the first line of "
            "each is quotable and is recorded as such.",
    "rules": RULES,
}

out = PROXY / f"{PID}-payload16.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items, {len(TABLES)} tables -> {out.name}")
