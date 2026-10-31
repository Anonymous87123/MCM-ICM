"""Hand pass for P-C-2010-8088-e7ab6731 (photodegradation of polyethylene, 6 "figures" + 1 appendix table).

This team numbers its displays in two parallel series — Figure N: and Diagram N: — and it
promotes plain display equations to figures: Figure 2 is the wavelength calculation,
Figure 5 is a unit-conversion chain, Figure 1 is the structural formula. Only Figure 3 (the
radical reaction scheme) and the two diagrams are drawings. Because those equation figures
are typeset text, the layout pass does not separate them from the body: Figure 1, Figure 3
and Figure 5 have no measured region and cannot be placed by this census. Recorded as a
gap, not patched.

Every caption sits ABOVE its exhibit, in both series, with a colon after the number —
the reverse of the two 2010 C-team papers already distilled.

The appendix spreadsheet (Appendix A) is a printed table in the text layer with a
variable/units/description/value block, but it also has no measured region, so no table
block is recorded.

Usage: python -I tools/_dist_paper13.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2010-8088-e7ab6731"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
REG = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: x["bbox"][1]), 1):
        REG[(pg["page"], i)] = r["bbox"]

PAGE_W, PAGE_H = 612.0, 792.0

ORDER = [(4, 1), (5, 2), (5, 1), (6, 1), (6, 2), (7, 1), (7, 2), (7, 3), (7, 4), (8, 1)]

S_PHOTO = "未编号标题：III Photolytic Degradation of Polyethylene"
S_LTM = "未编号标题：VI Low transmittance Model"


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
        "section_numbered": False,
        "section_kind": kind,
        "doc_order": ORDER.index((page, idx)) + 1,
        "page_order": same.index((page, idx)) + 1,
        "page_zone": z,
        "area_frac": round((b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H), 3),
        "solo_page": False,
    }


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


def figure(page: int, idx: int, family: str, cap: dict, men: dict, *, path: str,
           kind: str, legend: str = "none", three_d: str = "no",
           printed: bool = True, labels: bool = False, note: str = "",
           other_note: str = "") -> dict:
    it = {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, idx, [path], kind),
        "mention": men,
        "caption": cap,
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
    if other_note:
        it["other_note"] = other_note
    return it


ITEMS = [
    figure(4, 1, "other",
           caption("Figure 2: Calculation of", "Figure N:", "above"),
           mention(4, first=4, style=["Figure 2"], count=1,
                   lead="See Figure 2 for calculation of .",
                   trail=span(4, "When polyethylene is exposed to ultraviolet light",
                              "single bonds are cleaved"),
                   pattern="direct", read=1),
           path=S_PHOTO, kind="model",
           note="a single display equation: the de Broglie/Planck combination 6.626*10-34 "
                "kg m2/s times 3*10^8 m/s over 5.78*10-19 kg m2/s2, equal to 344 nm; the "
                "caption says only Calculation of and the symbol it calculates (lambda) is "
                "a glyph the text layer does not hold",
           other_note="an equation promoted to a numbered figure — no axes, no marks, no "
                      "legend; the exhibit is the typeset formula itself"),

    figure(6, 2, "flowchart-or-schematic",
           caption("Diagram 1: Finding the Effective Solar Radius", "none", "above"),
           mention(6, first=6, style=["Diagram 1"], count=2,
                   lead=span(6, "This is depicted in Diagram 1 below", "below"),
                   trail=span(7, "As you can see from Diagram 1", "effective solar radius"),
                   pattern="direct", read=1),
           path=S_LTM, kind="model", printed=False, labels=True,
           note="geometry schematic: a circle cut by a horizontal Ocean Surface line with a "
                "dashed water-line arc, a projected ellipse above carrying the area formula, "
                "and a right triangle inside the sphere marking r, the angle x, pi/2 - x "
                "and r cos(pi/2 - x); no numbers, all labels are symbols"),

    figure(8, 1, "line",
           caption("Diagram 2: The Relationship between Mass of Sphere and Time", "none",
                   "above"),
           mention(8, first=8, style=["Diagram 2"], count=1,
                   lead="Rate of degradation can be visualized in Diagram 2.",
                   pattern="direct"),
           path=S_LTM, kind="result",
           note="Excel line chart, one blue series falling from 9.1 g to 3.2 g, plotted "
                "area framed, horizontal gridlines only, y axis Mass (g) 0-10 and x axis "
                "Time (years) labelled every two years from 1 to 49, series named by the "
                "in-plot title Mfinal(t) instead of a legend"),
]

RULES = [
    "本题型把公式当图：Figure 2 是波长算式、Figure 5 是单位换算链、Figure 1 是结构式，"
    "只有 Figure 3 的机理式和两张 Diagram 是图形 [geometry.family]，[geometry.printed_numbers]。",
    "编号走两条并行序列——图用 Figure N:、示意图用 Diagram N:，两套各自记数、互不接续 "
    "[caption.numbering]，[caption.verbatim]。",
    "题注一律在展品上方，编号后加冒号再写短语（Figure 2: Calculation of；"
    "Diagram 1: Finding the Effective Solar Radius）[caption.position]，[caption.numbering]。",
    "题注只报「这是什么」，字数 4-10 词，不给单位、不给参数条件、不下结论 "
    "[caption.words]，[caption.units]，[caption.conditions]。",
    "正文引出全是明写式：See Figure N for …、can be seen in Figure 3、"
    "This is depicted in Diagram 1 below、can be visualized in Diagram 2 "
    "[mention.lead_pattern]，[mention.count]。",
    "引用与图同页，只有 Diagram 1 在图后的下一页再被读一次（As you can see from Diagram 1）"
    "[mention.lead_pages]，[mention.trail_sentence]。",
    "公式图不带数值标注，也不打印坐标轴刻度，因此 printed_numbers 只在 Diagram 2 为真 "
    "[geometry.printed_numbers]，[geometry.data_labels]。",
    "两张图形展品都是单面板、单系列、无图例：Diagram 1 用符号标注代替图例，"
    "Diagram 2 用图内标题 Mfinal(t) 代替图例 [geometry.legend]，[geometry.panel_count]。",
    "Diagram 2 用 Excel 默认版式：外框、仅横向网格线、轴标题 Mass (g)/Time (years) 带单位、"
    "横轴每两年标一个刻度 [geometry.printed_numbers]，[caption.units]。",
    "缺口：Figure 1、Figure 3、Figure 5 与 Appendix A 的变量表在版面上未形成可测量区域，"
    "本次未落条目，保留不补 [place.page_zone]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": [],
    "excluded_regions": [
        {"page": 5, "bbox": REG[(5, 2)], "reason": "not-an-exhibit",
         "note": "display equation in the body: the polar triple integral for the "
                 "submerged volume"},
        {"page": 5, "bbox": REG[(5, 1)], "reason": "not-an-exhibit",
         "note": "display equation in the body: the triple integral of the degradation rate"},
        {"page": 6, "bbox": REG[(6, 1)], "reason": "not-an-exhibit",
         "note": "display equation in the body: the mass/volume relation of two concentric "
                 "spheres"},
        {"page": 7, "bbox": REG[(7, 1)], "reason": "not-an-exhibit",
         "note": "display equation in the body: the rearranged radius formula"},
        {"page": 7, "bbox": REG[(7, 2)], "reason": "not-an-exhibit",
         "note": "display equation in the body: the unit-conversion chain that defines K"},
        {"page": 7, "bbox": REG[(7, 3)], "reason": "not-an-exhibit",
         "note": "display equation in the body: the polar double integral over area and time"},
        {"page": 7, "bbox": REG[(7, 4)], "reason": "not-an-exhibit",
         "note": "display equation in the body: the unit list closing the derivation"},
    ],
    "note": "Figure 1 (structure of polyethylene), Figure 3 (radical reaction scheme) and "
            "Figure 5 (unit conversion) are declared and cited in the text but have no "
            "measured region — their bodies are typeset text or equation glyphs, so the "
            "layout pass cannot separate them from the page. The Appendix A spreadsheet "
            "(variable / units / description / value) is likewise text-layer only. All four "
            "are recorded as gaps. The section headings are roman-numbered (III, VI) but "
            "absent from the extracted heading index, so section_path uses the 未编号标题 "
            "form with the numeral copied from the text layer.",
    "rules": RULES,
}

out = PROXY / f"{PID}-payload13.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items, 0 tables -> {out.name}")
