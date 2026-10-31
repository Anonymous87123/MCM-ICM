"""Hand pass for P-A-2010-7920-06d31c2b (sweet spot, 3 diagrams + 6 graphs).

Two exhibit idioms here. Figures 1-3 are hand line-art with a bare "Figure N" label
under the drawing. Graphs A-F are matplotlib-style plots whose only printed text is
an in-axes title above the frame plus a "Graph X" tag at the side, and whose axis
titles use a vertical bar as the unit separator (v_f | m/s). The graph numbers are
interleaved into the prose by the two-column wrap, so a graph's surrounding sentence
exists on the page only in pieces; those quotes are taken as the longest contiguous
run that the text layer actually contains, and the break is noted.

Seven measured strips are displayed equations, not exhibits.

Usage: python -I tools/_dist_paper4.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2010-7920-06d31c2b"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}


def head(prefix: str) -> str:
    return next(h["label"] for h in CTX["headings"] if h["label"].startswith(prefix))


H5 = head("5 Model A")
H6 = head("6 Model B")
H7 = head("7 Discussion")
H8 = next(h["label"] for h in CTX["headings"]
          if h["label"].startswith("8 Sensitivity") and h["page"] == 16)


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


def sent(page: int, needle: str) -> str:
    """From the needle to the end of its sentence.

    Walking back to the previous full stop is unsafe on these pages: the graph
    numbers are wrapped into the column, so the previous stop can sit a dozen
    figures away. The quote therefore starts at the needle.
    """
    t = text(page)
    i = t.find(needle)
    assert i >= 0, f"{needle!r} not on page {page}"
    e = t.find(".", i + len(needle))
    e = len(t) if e < 0 else e + 1
    q = t[i:e].strip()
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def caption(v: str, numbering: str, position: str, *, units: bool, vars_: int,
            cond: bool, concl: bool, voice: str, source: str) -> dict:
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


def mention(page: int, *, first: int, style: list[str], count: int, lead: str,
            trail: str = "", pattern: str, read: int, gap: int, note: str = "") -> dict:
    m = {
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
    if note:
        m["note"] = note
    return m


def entry(order: int, family: str, panels: int, layout: str, caption_verbatim: str,
          capt: dict, geom_extra: dict, place_path: list[str], place_kind: str,
          men: dict, *, confidence: str = "high", note: str = "",
          source: str = "text-layer") -> dict:
    s = BY_ORDER[order]
    geometry = {
        "family": family,
        "panel_count": panels,
        "panel_layout": layout,
        "shared_axes": False,
        "legend": "none",
        "colorbar": False,
        "three_d": "no",
        "printed_numbers": False,
        "data_labels": False,
    }
    geometry.update(geom_extra)
    return {
        "page": s["page"],
        "bbox": s["bbox"],
        "family": family,
        "confidence": confidence,
        "panel_count": panels,
        "caption_verbatim": caption_verbatim,
        "caption_source": source,
        "note": note,
        "place": {
            "section_path": place_path,
            "section_numbered": True,
            "section_kind": place_kind,
            "doc_order": s["doc_order"],
            "page_order": s["page_order"],
            "page_zone": s["page_zone"],
            "area_frac": s["area_frac"],
            "solo_page": False,
        },
        "mention": men,
        "caption": capt,
        "geometry": geometry,
    }


ITEMS = [
    entry(1, "flowchart-or-schematic", 1, "1", "Figure 1",
          caption("Figure 1", "Figure N", "below", units=False, vars_=0, cond=False,
                  concl=False, voice="none", source="text-layer"),
          {"data_labels": False},
          [H5], "model",
          mention(6, first=6, style=["Figure 1"], count=2,
                  lead=span(6, "The translational force initiated by the ball",
                            "at all points"),
                  pattern="parenthetical", read=1, gap=0),
          note="bat outline with five upward force arrows and the ball beneath it; "
               "the label sits under the drawing, not over it"),

    entry(2, "flowchart-or-schematic", 1, "1", "Figure 2",
          caption("Figure 2", "Figure N", "below", units=False, vars_=0, cond=False,
                  concl=False, voice="none", source="text-layer"),
          {"data_labels": True},
          [H5], "model",
          mention(6, first=6, style=["Figure 2"], count=1,
                  lead=span(6, "When the ball hits the bat", "rotational force"),
                  pattern="parenthetical", read=1, gap=0),
          note="same bat outline with a large curved rotation arrow and the words "
               "Center of Mass under the barrel"),

    entry(3, "line", 1, "1", "Final Speeds at Given Distance from Pivot",
          caption("Final Speeds at Given Distance from Pivot", "none", "above",
                  units=False, vars_=0, cond=True, concl=False, voice="none",
                  source="typed-from-crop"),
          {"printed_numbers": True},
          [H6], "model",
          mention(9, first=9, style=["Graph A"], count=1,
                  lead="This assumption is represented in",
                  pattern="direct", read=0, gap=0,
                  note="the lead breaks at the graph numbers wrapped into the column"),
          source="typed-from-crop",
          note="single curve of v_f against b, peak at b about 0.55 m; title inside "
               "the frame, Graph A tag at the right edge; axis titles v_f | m/s, b | m"),

    entry(4, "flowchart-or-schematic", 3, "1x3", "Figure 3",
          caption("Figure 3", "Figure N", "below", units=False, vars_=0, cond=False,
                  concl=False, voice="none", source="text-layer"),
          {},
          [H7], "evaluation",
          mention(15, first=15, style=["Figure 3"], count=3,
                  lead=span(15, "Taken together, this makes it possible",
                            "when struck by"),
                  trail=sent(15, "The resulting deformation takes the pattern"),
                  pattern="direct", read=1, gap=0),
          note="three-frame line drawing: circle, intermediate ellipse, elongated "
               "ellipse, joined by two arrows; the quadrupole deformation sequence"),

    entry(5, "surface-or-3D", 1, "1", "Sweet Spot due to Initial Velocities",
          caption("Sweet Spot due to Initial Velocities", "none", "above",
                  units=False, vars_=0, cond=True, concl=False, voice="none",
                  source="typed-from-crop"),
          {"three_d": "surface-mesh", "printed_numbers": True},
          [H8], "sensitivity",
          mention(17, first=17, style=["Graph B"], count=2,
                  lead="The graph is shown below",
                  trail=sent(17, "The darker area of Graph B"),
                  pattern="direct", read=1, gap=0),
          source="typed-from-crop",
          note="box-framed 3D grid: v (MPH) up the back axis, omega along the front "
               "axis, 0-60 on both; one shaded region marks the admissible "
               "combinations; no colour bar, shading is a flat fill"),

    entry(6, "line", 1, "1", "Final Speed vs. Bat Mass",
          caption("Final Speed vs. Bat Mass", "none", "above",
                  units=True, vars_=0, cond=True, concl=False, voice="none",
                  source="typed-from-crop"),
          {"printed_numbers": True},
          [H8], "sensitivity",
          mention(18, first=18, style=["Graph C"], count=1,
                  lead=span(18, "When the final velocity was tested against the mass",
                            "graph was produced"),
                  trail=sent(18, "As the mass of the bat increases"),
                  pattern="direct", read=1, gap=0),
          source="typed-from-crop",
          note="one rising straight line, v_f 53.48-53.54 over M 0.88-0.92 kg"),

    entry(7, "line", 1, "1", "Final Speed vs. Initial Bat Velocity",
          caption("Final Speed vs. Initial Bat Velocity", "none", "above",
                  units=True, vars_=0, cond=True, concl=False, voice="none",
                  source="typed-from-crop"),
          {"printed_numbers": True},
          [H8], "sensitivity",
          mention(18, first=18, style=["Graph D"], count=1,
                  lead=span(18, "When the final velocity was tested against the "
                            "initial velocity of the bat", "graph was produced"),
                  trail=sent(19, "As the initial bat velocity is increased"),
                  pattern="direct", read=1, gap=0),
          source="typed-from-crop",
          note="one rising straight line, v_f 53-57 over V_i 30-45 m/s"),

    entry(8, "line", 1, "1", "Final Speed vs. Moment of Inertia",
          caption("Final Speed vs. Moment of Inertia", "none", "above",
                  units=True, vars_=0, cond=True, concl=False, voice="none",
                  source="typed-from-crop"),
          {"printed_numbers": True},
          [H8], "sensitivity",
          mention(19, first=19, style=["Graph E"], count=1,
                  lead=span(19, "When the final velocity was tested against the "
                            "moment of inertia", "graph was produced"),
                  trail=span(19, "This plot indicates a weak sensitivity",
                             "moment of inertia"),
                  pattern="direct", read=1, gap=0),
          source="typed-from-crop",
          note="one near-flat rising line, v_f 53.3-53.7 over I 0.18-0.22 kg m2"),

    entry(9, "line", 1, "1", "Final Speed vs. Initial Ball Velocity",
          caption("Final Speed vs. Initial Ball Velocity", "none", "above",
                  units=True, vars_=0, cond=True, concl=False, voice="none",
                  source="typed-from-crop"),
          {"printed_numbers": True},
          [H8], "sensitivity",
          mention(20, first=19, style=["Graph F"], count=1,
                  lead=span(19, "When the final velocity was tested against the "
                            "initial velocity of the ball", "graph was produced"),
                  trail=sent(20, "It appears that the final velocity"),
                  pattern="direct", read=1, gap=0),
          source="typed-from-crop",
          note="one rising straight line, v_f 44-52 over v_i 32-42 m/s; y origin "
               "shifted to 44 so the slope fills the frame"),
]

EQUATIONS = [
    (7, [249.17, 575.47, 410.83, 618.67], "momentum, angular momentum and restitution"),
    (8, [231.41, 412.85, 381.31, 452.83], "solved expression for b"),
    (9, [218.09, 195.62, 393.19, 223.94], "v_f solved as a fraction"),
    (9, [208.73, 636.22, 402.91, 666.58], "derivative set to zero"),
    (10, [231.41, 102.02, 381.31, 141.98], "square-root form"),
    (10, [172.22, 443.69, 440.35, 480.43], "numeric substitution"),
    (12, [225.29, 582.55, 385.99, 608.59], "same form as the first v_f expression"),
    (13, [217.49, 169.22, 393.67, 208.22], "nested fraction"),
    (17, [163.94, 621.43, 447.31, 674.98], "wide bracketed fraction"),
]

RULES = [
    "本题型的图分两套模板：手绘线稿只带一个 Figure N 标签（词数 2），"
    "软件图只带图框内的标题和一个 Graph X 侧标，两套都不写整句题注 "
    "[caption.words]，[caption.position]。",
    "Figure 标签一律压在线稿下方，Graph 标签一律在框外右侧或左下，"
    "标题则压在框顶——标签位置由谁生成决定，不是由作者排版决定 [caption.position]。",
    "软件图的坐标轴文字用竖线当单位分隔符（v_f | m/s、I | kg m2），"
    "单位写在轴文字里而不写进题注 [caption.units]。",
    "图框内不放图例：单曲线图靠标题自明，三维图靠深浅着色标出可行域，"
    "没有色标 [geometry.legend]，[geometry.colorbar]。",
    "整个灵敏度一节用同一句式引出每张图：When the final velocity was tested against "
    "the X of the bat, the following graph was produced [mention.lead_sentence]。",
    "图后一句解释一律是 As the X increases, so does the final speed 的因果直陈，"
    "再点出敏感的强弱 [mention.trail_sentence]，[mention.read_sentences]。",
    "只有三维图给参数扫描面（初速 x 角速度），用阴影域表示约束后的可行组合，"
    "其余五张都是单变量一维曲线 [geometry.three_d]，[geometry.panel_count]。",
    "章节分工：两张受力线稿放在 Model A 概念节，单幅曲线放在 Model B 推导后的检验处，"
    "形变三联线稿放在 Discussion，一维参数扫描全部集中在 Sensitivity Analysis "
    "[place.section_kind]。",
    "正文引用这些图不用编号而是用指示语（the following graph、shown below、"
    "the second frame of Figure 3），全篇没有一次 Figure N shows [mention.lead_pattern]。",
    "线稿的标签直接写在图下方且与图同区，因此正文里 Figure 1 会出现在句子中间"
    "（struck by Figure 3 a baseball），引用位置落在词流里而非句末 [mention.style]。",
    "版面：所有图都不独占页，最大的三维图占 0.15 版面，其余 0.02-0.13 "
    "[place.area_frac]，[place.solo_page]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": [],
    "excluded_regions": [
        {"page": pg, "bbox": bbox, "reason": "not-an-exhibit",
         "note": f"displayed equation, {note}"}
        for pg, bbox, note in EQUATIONS
    ],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload4.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items, {len(EQUATIONS)} excluded -> {out.name}")
