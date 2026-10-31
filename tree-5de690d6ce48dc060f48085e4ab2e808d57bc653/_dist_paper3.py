"""Hand pass for P-A-2010-7586-ff69029f (horsehide-bat physics, 15 figures).

Every quote is sliced out of the page text layer, never retyped, so the record's
sentence fields stay substrings of the page they claim. Captions are rebuilt line by
line from the text layer because this journal breaks them across two to three lines.

Geometry comes from the crops: p3r1 bat schematic, p4r1 three-key line chart, p7 the
compression photo beside a hysteresis loop, p8-p13 pairs of exit-velocity plots, p14
seven colour-keyed curves. The eight right-hand halves are measured as separate
regions but are the second panel of the exhibit to their left, so they are excluded
as fragment-of-other rather than counted twice.

Usage: python -I tools/_dist_paper3.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2010-7586-ff69029f"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def lines(page: int) -> list[str]:
    return [schema.norm(l) for l in (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()]


def cap(page: int, number: int) -> str:
    """Caption as printed: the 'Figure N:' line plus the lines it wraps onto."""
    ls = lines(page)
    start = next(i for i, l in enumerate(ls)
                 if re.match(rf"Figure\s+{number}:", l))
    out = [ls[start]]
    for nxt in ls[start + 1:]:
        if not nxt or re.match(r"Figure\s+\d", nxt) or re.match(r"\d+(\.\d+)?\s+[A-Z]{3,}", nxt):
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


def sent(page: int, needle: str) -> str:
    """The sentence around a needle: previous stop to next stop."""
    t = text(page)
    i = t.find(needle)
    assert i >= 0, f"{needle!r} not on page {page}"
    s = t.rfind(". ", 0, i)
    s = 0 if s < 0 else s + 2
    e = t.find(".", i + len(needle))
    e = len(t) if e < 0 else e + 1
    q = t[s:e].strip()
    w = list(re.finditer(r"\S+", q))
    while len(schema.words(q)) > 25 and len(w) > 1:
        q = q[w[1].start():].strip()
        w = list(re.finditer(r"\S+", q))
    return q


def place(order: int, path: list[str] | None = None, kind: str | None = None) -> dict:
    s = BY_ORDER[order]
    return {
        "section_path": path or s["section_path"],
        "section_numbered": True,
        "section_kind": kind or s["section_kind"],
        "doc_order": s["doc_order"],
        "page_order": s["page_order"],
        "page_zone": s["page_zone"],
        "area_frac": s["area_frac"],
        "solo_page": False,
    }


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


def geom(order: int, panels: int, layout: str, *, legend: str = "none",
         printed: bool = True, labels: bool = False) -> dict:
    return {
        "family": "line",
        "panel_count": panels,
        "panel_layout": layout,
        "shared_axes": False,
        "legend": legend,
        "colorbar": False,
        "three_d": "no",
        "printed_numbers": printed,
        "data_labels": labels,
    }


def mention(page: int, *, first: int | None, style: list[str], count: int,
            lead: str = "", trail: str = "", pattern: str = "none",
            read: int = 0, gap: int | None = None) -> dict:
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


def item(order: int, family: str, panels: int, capnum: int, *, confidence: str = "high",
         note: str = "", place_: dict | None = None, geom_: dict | None = None,
         mention_: dict | None = None, cap_: dict | None = None) -> dict:
    s = BY_ORDER[order]
    return {
        "page": s["page"],
        "bbox": s["bbox"],
        "family": family,
        "confidence": confidence,
        "panel_count": panels,
        "caption_verbatim": cap(s["page"], capnum),
        "caption_source": "text-layer",
        "note": note,
        "place": place_ or place(order),
        "mention": mention_,
        "caption": cap_,
        "geometry": geom_,
    }


ITEMS = [
    item(1, "flowchart-or-schematic", 1, 1,
         note="bat drawn as a black rod with three coloured annotation arrows "
              "(initial velocity, initial rotation, distance from center of mass)",
         geom_={"family": "flowchart-or-schematic", "panel_count": 1,
                "panel_layout": "1", "shared_axes": False, "legend": "none",
                "colorbar": False, "three_d": "no", "printed_numbers": False,
                "data_labels": True},
         mention_=mention(3, first=3, style=["Figure 1"], count=1,
                          lead=sent(3, "as in Figure 1."), pattern="as-shown-in",
                          read=1, gap=0),
         cap_=caption(3, 1, units=False, vars_=0, cond=False, concl=False,
                      voice="active")),

    item(2, "line", 1, 2,
         note="one axes, three keys under the x-axis: final velocity / effective "
              "mass / swing speed against l",
         geom_=geom(2, 1, "1", legend="below", printed=True),
         mention_=mention(4, first=None, style=[], count=0, read=1, gap=None),
         cap_=caption(4, 2, units=False, vars_=2, cond=True, concl=False,
                      voice="none")),

    item(3, "composite-panel", 2, 3,
         note="left is a grayscale photo of the ball against the wall, right is the "
              "hysteresis loop Force(N) vs Compression(m); the loop is the only "
              "figure in the paper with a labelled y-axis at the top right",
         geom_={"family": "composite-panel", "panel_count": 2,
                "panel_layout": "1x2", "shared_axes": False, "legend": "none",
                "colorbar": False, "three_d": "no", "printed_numbers": True,
                "data_labels": False},
         mention_=mention(7, first=7, style=["Figure 3b"], count=2,
                          lead=sent(7, "such as the ones shown in Figure 3b"),
                          trail=sent(8, "the area between the two curves in Figure 3b"),
                          pattern="as-shown-in", read=1, gap=1),
         cap_=caption(7, 3, units=True, vars_=0, cond=False, concl=True,
                      voice="passive")),

    item(4, "line", 2, 4,
         note="left force spike vs time (about 1.4 ms), right bat displacement "
              "waveform vs time at the 60 cm strike",
         geom_=geom(4, 2, "1x2", printed=True),
         mention_=mention(8, first=8, style=["Figure 4a", "Figure 4b"], count=2,
                          lead=sent(8, "the asymmetry of the plot in Figure 4a"),
                          trail=sent(8, "Figure 4b shows the answer"),
                          pattern="direct", read=1, gap=0),
         cap_=caption(8, 4, units=True, vars_=1, cond=True, concl=True,
                      voice="active")),

    item(5, "line", 2, 5,
         note="left free vs fixed barrel end, right the same sweep for a 110 cm "
              "bat; both panels keep their own axes, so the flat zone shows as a "
              "rescaled curve rather than a shared-axis continuation",
         geom_=geom(5, 2, "1x2", printed=True),
         mention_=mention(9, first=8, style=["Figure 5a", "Figure 5b"], count=2,
                          lead=sent(8, "In Figure 5a we show the effects"),
                          pattern="direct", read=1, gap=1),
         cap_=caption(9, 5, units=True, vars_=0, cond=True, concl=False,
                      voice="active")),

    item(6, "line", 1, 6,
         note="seven-ish solid model curves with square markers over descending "
              "dotted simple-model curves; two Brody maximum dots sit off the band",
         geom_=geom(6, 1, "1", printed=True),
         mention_=mention(9, first=9, style=["Figure 6"], count=3,
                          lead=sent(9, "In Figure 6 we present the results"),
                          trail=sent(10, "As evident from Figure 6"),
                          pattern="direct", read=1, gap=0),
         cap_=caption(9, 6, units=False, vars_=0, cond=True, concl=False,
                      voice="active")),

    item(7, "line", 2, 7,
         note="excess exit velocity over impact position; left with hysteresis, "
              "right without, where the crossing of the curves disappears",
         geom_=geom(7, 2, "1x2", printed=True),
         mention_=mention(10, first=10, style=["Figure 7a", "Figure 7b"], count=2,
                          lead=sent(10, "In Figure 7a we show"),
                          trail=sent(10, "recreated the plot in Figure 7b"),
                          pattern="direct", read=1, gap=0),
         cap_=caption(10, 7, units=False, vars_=0, cond=True, concl=True,
                      voice="active")),

    item(8, "line", 1, 8,
         note="stepped rigid-body line plus square markers for the model optimum, "
              "both rising with angular velocity",
         geom_=geom(8, 1, "1", printed=True, labels=False, legend="none"),
         mention_=mention(10, first=None, style=[], count=0, read=0, gap=None),
         cap_=caption(10, 8, units=False, vars_=0, cond=True, concl=False,
                      voice="active")),

    item(9, "line", 1, 9,
         confidence="medium",
         note="28 pt tall strip: the bat outline plotted as upper and lower profile "
              "curves over 0.84 m, knob wiggle at the left; axes print 0.03 and "
              "-0.03, so it is a plotted profile, not a drawing",
         geom_=geom(9, 1, "1", printed=True, labels=False),
         mention_=mention(10, first=10, style=["Figure 9"], count=1,
                          lead=span(10, "our bat profile", "wooden"),
                          pattern="parenthetical", read=0, gap=0),
         cap_=caption(10, 9, units=False, vars_=0, cond=False, concl=False,
                      voice="none")),

    item(10, "line", 2, 10,
         note="density sweep; solid is the original rho, left panel sweeps up "
              "(700 dotted, 1000 dashed), right panel sweeps down (640, 500)",
         geom_=geom(10, 2, "1x2", printed=True),
         mention_=mention(11, first=11, style=["Figure 10"], count=1,
                          lead=span(11, "the current density occupied",
                                    "(see Figure 10"),
                          pattern="parenthetical", read=0, gap=0),
         cap_=caption(11, 10, units=True, vars_=1, cond=True, concl=False,
                      voice="active")),

    item(11, "line", 2, 11,
         note="left Young's modulus at 0.8x/1x/1.25x, right handle thickness "
              "varied; same 0.3-0.8 m impact window in both",
         geom_=geom(11, 2, "1x2", printed=True),
         mention_=mention(11, first=11, style=["Figure 11"], count=1,
                          lead=span(11, "We also varied the Young", "(see Figure 11."),
                          pattern="parenthetical", read=1, gap=0),
         cap_=caption(11, 11, units=True, vars_=1, cond=True, concl=False,
                      voice="active")),

    item(12, "line", 1, 12,
         note="single panel, three curves for 30/40/50 m/s ball speed keyed only in "
              "the caption; the measured layout has one region here, so the "
              "'Left:' reading is a caption artefact, not a second panel",
         geom_=geom(12, 1, "1", printed=True),
         mention_=mention(12, first=11, style=["Figure 12"], count=1,
                          lead=span(11, "Finally we varied the velocity of the ball",
                                    "(see Figure 12."),
                          pattern="parenthetical", read=0, gap=0),
         cap_=caption(12, 12, units=True, vars_=0, cond=True, concl=False,
                      voice="active")),

    item(13, "line", 2, 13,
         note="left corked bat, right aluminum bat; both plots, two curves each, "
              "separate y-axes",
         geom_=geom(13, 2, "1x2", printed=True),
         mention_=mention(12, first=12, style=["Figure 13a", "Figure 13b"], count=2,
                          lead=sent(12, "The result is shown in Figure 13a"),
                          trail=span(12, "From the exit velocity graph",
                                     "(see Figure 13b)."),
                          pattern="direct", read=1, gap=0),
         cap_=caption(12, 13, units=False, vars_=0, cond=False, concl=False,
                      voice="none")),

    item(14, "line", 2, 14,
         note="two animation frames side by side, t=0.5 ms and t=1.05 ms printed "
              "inside each panel; aluminum dashed, wood solid",
         geom_=geom(14, 2, "1x2", printed=True, labels=True),
         mention_=mention(13, first=12, style=["Figure 14"], count=1,
                          lead=span(12, "we animated the displacement of the bats",
                                    "in Figure 14."),
                          pattern="direct", read=0, gap=0),
         cap_=caption(13, 14, units=True, vars_=1, cond=True, concl=False,
                      voice="passive")),

    item(15, "line", 1, 15,
         note="seven curves keyed by colour only, no legend box; the caption reads "
              "the stack from bottom to top at the left edge",
         place_=place(15, path=["4 SIMULATION AND ANALYSIS",
                                "4.3 Alternatives to Wooden Bats"], kind="solution"),
         geom_=geom(15, 1, "1", printed=True),
         mention_=mention(14, first=13, style=["Figure 15"], count=1,
                          lead=sent(13, "as shown in Figure 15"),
                          pattern="as-shown-in", read=0, gap=0),
         cap_=caption(14, 15, units=True, vars_=0, cond=True, concl=False,
                      voice="active")),
]

EXCLUDED = [
    (7, [308.49, 577.85, 537.81, 702.07], "hysteresis loop, right half of Figure 3"),
    (8, [308.49, 453.49, 519.09, 568.15], "displacement waveform, right half of Figure 4"),
    (9, [308.49, 111.24, 519.09, 230.86], "110 cm bat panel, right half of Figure 5"),
    (10, [308.49, 203.48, 519.09, 312.99], "no-hysteresis panel, right half of Figure 7"),
    (11, [308.49, 245.16, 519.09, 383.21], "downward density sweep, right half of Figure 10"),
    (11, [308.49, 432.03, 519.09, 570.09], "bat-shape sweep, right half of Figure 11"),
    (12, [308.49, 429.36, 537.81, 579.7], "aluminum bat, right half of Figure 13"),
    (13, [308.49, 107.86, 537.82, 249.13], "t=1.05 ms frame, right half of Figure 14"),
]

RULES = [
    "本题型的结果图几乎全是同一张「出口速度 vs 击打位置」曲线，只换扫描参数，"
    "因此图的族不是按外形选，而是按被扫参数选：一根轴、若干条线 [geometry.family]。",
    "参数扫描一律双栏并置：左栏原始参数或上行扫描，右栏另一组扫描，"
    "题注用 Left/Right 指栏而不画图例 [geometry.panel_layout]，[geometry.legend]。",
    "两栏各自保留完整坐标轴、不共享，扫动后的曲线只改变形状不改刻度范围，"
    "读者靠题注的 Left/Right 而不是靠共享轴去对读 [geometry.shared_axes]。",
    "线型说明写进题注：solid is…, dashed is…, dotted is…；全篇只有 Figure 2 用图例框，"
    "且图例压在图下 [geometry.legend]，[caption.words]。",
    "所有图注都在图下方、编号格式统一为 Figure N:，词数 7–40，"
    "曲线族图注 25–40 词，剖面图只有 7 词 [caption.position]，[caption.words]，[caption.numbering]。",
    "题注模板可直接观察到复用痕迹：Figure 7 第二栏仍写 Left:，Figure 10/11 的 Left/Right "
    "是后补的栏说明，说明作者先写整段参数说明再补左右 [caption.verbatim]。",
    "题注只在物理图像图上写结论（压缩肉眼可见、脉冲后段才起动），"
    "曲线族图注只报参数不下结论 [caption.concludes]。",
    "题目给单位的场合集中在毫秒、厘米、m/s、kg/m3、Hz；符号只在题注里出现一次"
    "（v_f、y10(t)、rho、Y、t）[caption.units]，[caption.variable_count]。",
    "章节分工固定：照片加滞回环放在模型章，其余曲线全放 4.1 模拟结果、4.2 参数空间、"
    "4.3 木质球棒替代品三节，正文没有把曲线图放进假设或符号节 [place.section_kind]。",
    "正文引出几乎都是括号回指 (see Figure N.，句号落在括号内，"
    "只有首图用 as in Figure 1 的直叙 [mention.lead_pattern]，[mention.style]。",
    "同一图的不同栏在正文里分别按 a/b 指称（Figure 5a/5b、Figure 13a/13b），"
    "引用写法带栏号 [mention.style]。",
    "图内不标数值：坐标刻度数字打印，曲线上的点只有 Figure 8 的模型预测方块和 "
    "Figure 6 的 Brody 极大点；图内文字只有 Figure 14 的 t=0.5 ms/1.05 ms 和 "
    "Figure 1 的三个参数箭头 [geometry.data_labels]，[geometry.printed_numbers]。",
    "全篇没有三维图、没有色标，颜色只在 Figure 15 用来区分七条频率曲线，"
    "且颜色含义写在题注的 from bottom to top 里 [geometry.three_d]，[geometry.colorbar]。",
    "版面：正文图都是半栏宽的两栏并置（约 0.05–0.07 版面），"
    "单栏图与 Figure 6/15 的整幅图各自独占行宽 [place.area_frac]。",
]

LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": [],
    "excluded_regions": [
        {"page": pg, "bbox": bbox, "reason": "fragment-of-other", "note": note}
        for pg, bbox, note in EXCLUDED
    ],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload3.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items, {len(EXCLUDED)} excluded -> {out.name}")
