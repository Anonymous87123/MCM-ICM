"""Hand pass for P-B-2010-7273-e234c9a6 (crime-site geometry, 12 figures).

One idiom runs through the whole paper: every picture is a framed panel with no axes
at all — no ticks, no numbers, no axis titles — and the caption carries the entire
key (which layer is black, which is grey, which marker is the house). Families split
three ways: raster heatmaps with a rainbow ramp and markers overlaid, node-link road
graphs with marker overlays, and two filled 3D surfaces in a bare box.

Captions wrap onto two or three lines; each is rebuilt line by line from the text
layer so the quoted string stays a substring of the page.

Usage: python -I tools/_dist_paper5.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2010-7273-e234c9a6"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))
SKEL = json.loads((PROXY / f"{PID}-skel.json").read_text(encoding="utf-8"))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
BY_ORDER = {it["doc_order"]: it for it in SKEL}


def head(prefix: str) -> str:
    return next(h["label"] for h in CTX["headings"] if h["label"].startswith(prefix))


H4 = head("4 Best Fit Circle")
H41 = next(h["label"] for h in CTX["headings"]
           if h["label"].startswith("4.3 Application"))
H5 = next(h["label"] for h in CTX["headings"]
          if h["label"].startswith("5 Case Studies") and h["page"] == 10)
H51 = next(h["label"] for h in CTX["headings"] if h["label"].startswith("5.1 Yorkshire"))
H511 = next(h["label"] for h in CTX["headings"] if h["label"].startswith("5.1.1"))
H514 = next(h["label"] for h in CTX["headings"] if h["label"].startswith("5.1.4"))
H52 = next(h["label"] for h in CTX["headings"] if h["label"].startswith("5.2 Atlanta"))
H523 = next(h["label"] for h in CTX["headings"] if h["label"].startswith("5.2.3"))
H524 = next(h["label"] for h in CTX["headings"] if h["label"].startswith("5.2.4"))
H6 = next(h["label"] for h in CTX["headings"]
          if h["label"].startswith("6 Improving") and h["page"] == 16)
H62 = next(h["label"] for h in CTX["headings"] if h["label"].startswith("6.2"))


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


def sent(page: int, needle: str) -> str:
    t = text(page)
    i = t.find(needle)
    assert i >= 0, f"{needle!r} not on page {page}"
    e = t.find(".", i + len(needle))
    e = len(t) if e < 0 else e + 1
    q = t[i:e].strip()
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def caption(page: int, number: int, *, units: bool, cond: bool, concl: bool,
            voice: str) -> dict:
    v = cap(page, number)
    return {
        "verbatim": v,
        "numbering": "Figure N:",
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": units,
        "variables": False,
        "variable_count": 0,
        "conditions": cond,
        "concludes": concl,
        "voice": voice,
        "position": "below",
    }


def mention(page: int, *, first: int, style: list[str], count: int, lead: str,
            trail: str = "", pattern: str, read: int, gap: int) -> dict:
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


def entry(order: int, family: str, path: list[str], kind: str, capt: dict,
          men: dict, *, three_d: str = "no", note: str = "") -> dict:
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
        "place": {
            "section_path": path,
            "section_numbered": True,
            "section_kind": kind,
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
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": "none",
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": False,
            "data_labels": False,
        },
    }


ITEMS = [
    entry(1, "flowchart-or-schematic", [H4, H41], "model",
          caption(8, 1, units=False, cond=False, concl=True, voice="none"),
          mention(8, first=7, style=["Figure 1"], count=1,
                  lead=sent(7, "Consider the example in Figure 1"),
                  pattern="direct", read=1, gap=1),
          note="three x marks on a circle, hollow arrow, then an arc through the "
               "same marks; drawn with no axes or frame"),

    entry(2, "node-link-network", [H4, H41], "model",
          caption(9, 2, units=False, cond=True, concl=False, voice="passive"),
          mention(9, first=8, style=["Figure 2"], count=1,
                  lead=sent(8, "In Figure 2, we show an example"),
                  pattern="direct", read=1, gap=0),
          note="black node-link highway graph inside a grey pixel-staircase ring: "
               "the road-metric circle is drawn as grid cells, not as a curve"),

    entry(3, "heatmap-or-contour", [H5, H51, H511], "other",
          caption(10, 3, units=False, cond=True, concl=False, voice="active"),
          mention(10, first=10, style=["Figure 3"], count=1,
                  lead=sent(10, "Figure 3 shows a color plot"),
                  pattern="figure-n-shows", read=0, gap=0),
          note="coarse rainbow raster, red core, hollow house marker, black "
               "node-link overlay; framed, no axes, no colour bar"),

    entry(4, "heatmap-or-contour", [H5, H51, H514], "evaluation",
          caption(11, 4, units=False, cond=True, concl=False, voice="active"),
          mention(11, first=11, style=["Figure 4"], count=1,
                  lead=sent(11, "The results are shown in Figure 4"),
                  pattern="as-shown-in", read=0, gap=0),
          note="magenta-to-red raster with the attack dots and one x; the caption "
               "states the ramp direction (red high, purple low) instead of a bar"),

    entry(5, "node-link-network", [H5, H51, H514], "evaluation",
          caption(12, 5, units=False, cond=False, concl=False, voice="passive"),
          mention(12, first=11, style=["Figure 5"], count=1,
                  lead=span(11, "As was discussed earlier", "shown in Figure 5"),
                  pattern="as-shown-in", read=1, gap=1),
          note="grey road graph, black pixel ring as the fitted circle, red dots "
               "for the kill sites; three layers keyed only in the caption"),

    entry(6, "heatmap-or-contour", [H5, H51, H514], "evaluation",
          caption(12, 6, units=False, cond=False, concl=False, voice="passive"),
          mention(12, first=11, style=["Figure 6"], count=1,
                  lead=span(11, "A colorized plot is shown in Figure 6", "Figure 6"),
                  pattern="as-shown-in", read=1, gap=1),
          note="same ramp as Figure 4, house symbol at the true residence, attack "
               "dots over the density"),

    entry(7, "surface-or-3D", [H5, H52, H523], "model",
          caption(13, 7, units=False, cond=False, concl=False, voice="none"),
          mention(13, first=11, style=["Figure 7"], count=1,
                  lead=span(11, "a plot of the estimated function as a surface",
                            "Figure 7"),
                  pattern="as-shown-in", read=0, gap=2),
          three_d="surface-mesh",
          note="filled blue surface in a bare wire box: one peak, no ticks, no "
               "colour bar, axes unlabelled"),

    entry(8, "heatmap-or-contour", [H5, H52, H524], "evaluation",
          caption(14, 8, units=False, cond=True, concl=False, voice="none"),
          mention(14, first=13, style=["Figure 8"], count=1,
                  lead=sent(13, "The distance from Williams"),
                  pattern="as-shown-in", read=0, gap=1),
          note="rainbow distance raster with the whole road network drawn over it "
               "as a black node-link layer"),

    entry(9, "heatmap-or-contour", [H5, H52, H524], "evaluation",
          caption(14, 9, units=False, cond=True, concl=False, voice="active"),
          mention(14, first=13, style=["figure 9"], count=1,
                  lead=sent(13, "The results are shown in figure 9."),
                  pattern="as-shown-in", read=0, gap=1),
          note="lowest-quality raster of the set: the hot cells break into separate "
               "red and orange blocks rather than one lobe"),

    entry(10, "node-link-network", [H5, H52, H524], "evaluation",
          caption(15, 10, units=False, cond=False, concl=False, voice="none"),
          mention(15, first=13, style=["Figure 10"], count=1,
                  lead=sent(13, "This is shown in Figure 10"),
                  pattern="as-shown-in", read=0, gap=2),
          note="four layers at once: grey road graph, thick highlighted edges, black "
               "square cluster, red dots; heavier than Figure 5"),

    entry(11, "heatmap-or-contour", [H5, H52, H524], "evaluation",
          caption(15, 11, units=False, cond=False, concl=False, voice="passive"),
          mention(15, first=14, style=["Figure 11"], count=1,
                  lead=span(14, "A colorized illustration of the results", "Figure 11"),
                  pattern="as-shown-in", read=0, gap=1),
          note="red block at the centre, crime dots, hollow house marker"),

    entry(12, "surface-or-3D", [H6, H62], "model",
          caption(16, 12, units=False, cond=False, concl=False, voice="none"),
          mention(16, first=14, style=["Figure 12"], count=1,
                  lead=span(14, "a representation of the results as a surface",
                            "Figure 12"),
                  pattern="as-shown-in", read=0, gap=2),
          three_d="surface-mesh",
          note="same box as Figure 7 but flatter, with a small left ridge; the "
               "surface stops in ragged triangles where the data end"),
]

RULES = [
    "本题型的图一律是无坐标图：没有刻度、没有数字、没有轴题，"
    "整张面板的读法全由题注承担 [geometry.printed_numbers]，[caption.words]。",
    "图注固定三件事：这张图是什么、每种颜色/符号代表哪一层、真实位置用哪个符号；"
    "颜色说明不画成色标而写成句子（Red indicates the highest probability）"
    "[caption.conditions]，[geometry.colorbar]。",
    "热图用同一套彩虹色表（品红→蓝→青→绿→黄→红），"
    "全篇不印色标，色序靠题注一句话交代 [geometry.family]，[geometry.colorbar]。",
    "概率密度图与网络图交替出现：先给距离/密度热图，再用节点-连线图叠出道路网和拟合圆，"
    "同一位置的三种表达轮流出现 [geometry.family]。",
    "节点-连线图是分层叠加的：灰色道路网在下，黑色方块/红点/环在上，"
    "层数越多说明结论越综合 [geometry.family]，[place.page_zone]。",
    "三维只用于「概率面」，且只有两张（Figure 7、Figure 12），"
    "都是空盒框里的实心面、无刻度无色标 [geometry.three_d]。",
    "正文引出全部是 as shown in / is shown in 的顺叙，"
    "唯一一次 Figure N shows 用在第一张色图 [mention.lead_pattern]，[mention.style]。",
    "引用写法连大小写都不统一：五张图用 Figure N，Figure 9 一处写作小写 figure 9 "
    "[mention.style]。",
    "题注位置固定在图下方，编号格式 Figure N:，词数跨度大（7-34 词），"
    "带图例说明的题注反而更长 [caption.position]，[caption.words]，[caption.numbering]。",
    "图表按章节用途分工：方法章放示意图与理论面，案例章放密度热图与拟合圆，"
    "改进章再放一张验证面 [place.section_kind]。",
    "图为半栏宽、成对竖排在页面中上区，两张图一页是常态 [place.area_frac]，"
    "[place.page_zone]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": [],
    "excluded_regions": [],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload5.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items -> {out.name}")
