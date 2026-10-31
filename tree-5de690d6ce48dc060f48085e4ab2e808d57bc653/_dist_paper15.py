"""Hand pass for P-A-2011-12149-cb2b7105 (half-pipe vertical air, 12 figures + 2 uncaptioned tables).

The paper runs four models in sequence and the exhibits follow that order: one schematic per
model (energy, 2D force, 3D force), then the MATLAB result plots, then the testing photographs
and the appendix renderings. Two features are worth distilling:

  * Every model schematic carries an equation block pasted into its top-left corner, so the
    figure and the force equations are read as one object.
  * The result plots are stock MATLAB output: an in-plot title stands in for the legend, axis
    titles carry the unit (m), and the three 3D views use isometric axis triads with marker
    traces rather than surfaces.

Two body tables (pages 9 and 12) are printed without any caption or "Table N" reference, so
they are recorded in the table block with caption_source "none". Figures 11 and 12, by
contrast, are tables that the team numbered and captioned as figures; they stay in the figure
block as table-as-figure. The appendix figures 9-12 are never cited by number in the body —
figures 9 and 10 are only referred to on page 2, nineteen pages before they appear.

Usage: python -I tools/_dist_paper15.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2011-12149-cb2b7105"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
REG = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: x["bbox"][1]), 1):
        REG[(pg["page"], i)] = r["bbox"]

PAGE_W, PAGE_H = 612.0, 792.0

ORDER = [(4, 1), (6, 1), (7, 1), (9, 1), (10, 1), (11, 1), (12, 1), (12, 2),
         (14, 1), (14, 2), (21, 1), (21, 2), (22, 1), (23, 1)]

H_MODELS = "2 Models"
H_ENERGY = "2.1 Conservation of Energy"
H_2D = "2.2 Two Dimensional Force Model"
H_3D = "2.3 Comprehensive Three Dimensional Force Model"
H_RES = "3 Results"
H_RES2D = "3.2 Two Dimensional Force Model Results"
H_RES3D = "3.3 Comprehensive Three Dimensional Force Model Results"
H_TEST = "4 Testing Methods"
H_PHYS = "4.1 Physical Testing"
H_APP = "6 Appendix"
H_APF1 = "6.1 Figures"
H_APF2 = "6.2 Figures"


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


def caption(v: str, *, cond: bool = False, concl: bool = False,
            units: bool = False, vars_: int = 0) -> dict:
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
           layout: str = "1", note: str = "") -> dict:
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
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(page: int, idx: int, men: dict, *, path: list[str], kind: str, grid: dict,
          note: str) -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": "",
        "caption_source": "none",
        "note": note,
        "place": place(page, idx, path, kind),
        "mention": men,
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
            "position": "below",
        },
        "table": grid,
    }


ITEMS = [
    figure(4, 1, "flowchart-or-schematic",
           caption("Figure 1: Energy Model Diagram"),
           mention(4, first=3, style=["figure 1"], count=3,
                   lead=span(3, "the kinetic energy used to launch a snowboarder",
                             "(figure 1)"),
                   pattern="parenthetical"),
           path=[H_MODELS, H_ENERGY], kind="model", printed=False,
           note="frictionless half-pipe side elevation: mass block on the left lip, dashed "
                "height levels for h and h0, a dashed launch path with the velocity arrow v "
                "and the take-off angle theta, and the typewritten line Mass, m, on a "
                "frictionless half-pipe. under the drawing instead of a caption"),

    figure(6, 1, "flowchart-or-schematic",
           caption("Figure 2: Two dimensional Force Model"),
           mention(6, first=3, style=["figure 2"], count=3,
                   lead=span(6, "each shape can be analyzed side by side", "(figure 2)"),
                   pattern="parenthetical"),
           path=[H_MODELS, H_2D], kind="model", printed=False, labels=True,
           note="one composite object: a four-line force equation block in the top-left "
                "(Fs = N*mu + Fair, N = mgcos(theta) + Fc, Fs = mg, ma = sum F) pasted over "
                "the half-pipe profile view, which carries the part names DECK, COPING, VERT, "
                "TRANSITION, FLAT BOTTOM, the z(t) and y(t) axes, a blue section profile and "
                "red/black force arrows on a boxed rider, under the heading HALF-PIPE / VERT "
                "RAMP PROFILE VIEW"),

    figure(7, 1, "flowchart-or-schematic",
           caption("Figure 3: zx plane for 3D Force Model"),
           mention(7, first=7, style=["figure 3"], count=1,
                   lead=span(7, "we shifted the axis used to define", "(figure 3)"),
                   pattern="parenthetical"),
           path=[H_MODELS, H_3D], kind="model", printed=False, labels=True,
           note="the same equation block as Figure 2 carried over, now over a rotated-axis "
                "force diagram: the original x and z axes in black, the shifted pair drawn as "
                "red lines and labelled New x axis / New z axis / Shifted axis = red line, "
                "with green arrows for N, Fs, mg and ma and the angle phi at the slope"),

    figure(10, 1, "line",
           caption("Figure 4: Dispacement in the YZ Plane"),
           mention(10, first=None, style=[], count=0,
                   trail=span(10, "This can be seen in the following graph", "displacement.")),
           path=[H_RES, H_RES2D], kind="result",
           note="stock MATLAB line chart titled YZ Path Without Work, three curves in red, "
                "black and green over one frame, y axis Vertical Distance (m) running 0 to "
                "-10 and x axis Horizontal Distance (m) -10 to 10, ticks every 2 m, no legend "
                "and no data labels"),

    figure(11, 1, "line",
           caption("Figure 5: Dispacement in the YZ Plane Adding Work"),
           mention(11, first=None, style=[], count=0,
                   trail=span(11, "we can verify that the function yielding",
                              "greatest vertical air.")),
           path=[H_RES, H_RES2D], kind="result",
           note="twin of Figure 4 retitled YZ Path With Added Work with the same three "
                "colours; the x axis now runs -10 to 20 so the free-flight arc past the far "
                "lip fits inside the frame, still no legend"),

    figure(12, 1, "scatter",
           caption("Figure 6: Ariel View of Three Dimensional Displacement"),
           mention(12, first=11, style=["figure 6"], count=1,
                   lead=span(11, "the displacement in the x, y and the z direction",
                             "(figure 6)"),
                   pattern="parenthetical"),
           path=[H_RES, H_RES3D], kind="result", three_d="isometric",
           note="red plus-marker traces of the rider path drawn against an isometric axis "
                "triad: the y axis is a flat arrow, the x axis runs down the page and the z "
                "axis stands up, with tick marks printed along the two horizontal axes and no "
                "grid or surface"),

    figure(14, 1, "photo-or-raster-image",
           caption("Figure 7: Physical Model Testing"),
           mention(14, first=13, style=["figure 7"], count=1,
                   lead=span(13, "and send a marble down the halfpipe", "correctly(figure 7)"),
                   pattern="parenthetical"),
           path=[H_TEST, H_PHYS], kind="test", printed=False, labels=True,
           note="indoor bench test photographed head-on: PVC pipe frame with a white fabric "
                "sheet pulled into a ramp profile, two blue callout boxes lettered Slope of "
                "Mountain and Slope of transition with green and yellow arrows pointing at the "
                "fabric edges"),

    figure(14, 2, "scatter",
           caption("Figure 8: 3 Dimensional Graph of Snowboarder’s Displacement"),
           mention(14, first=13, style=["figure 8"], count=1,
                   lead="We found that the path the marble followed was almost exactly "
                        "mirrored the three dimensional graph of the snowboarder’s "
                        "displacement(figure 8).",
                   pattern="parenthetical"),
           path=[H_TEST, H_PHYS], kind="test", three_d="isometric",
           note="six red plus-marker traces in parallel arcs inside one frame, drawn against "
                "an embedded isometric axis triad marked z, y and +X/-X; the tick columns run "
                "0-300 and 0-8 down the left and -5 to 25 along the top, so the axes are "
                "printed but untitled and unitless"),

    figure(21, 1, "flowchart-or-schematic",
           caption("Figure 9: Snowboard halfpipe"),
           mention(21, first=2, style=["figure 9"], count=1,
                   lead=span(2, "A snowboarding halfpipe is a basic halfpipe", "(figure 9)"),
                   pattern="parenthetical"),
           path=[H_APP, H_APF1], kind="appendix", labels=True,
           note="textbook-style cutaway illustration under a black HALF PIPE header bar: "
                "snowboarder on a shaded pipe section with leader-line labels Entry ramp, "
                "Platform/Deck, Lip, Vertical, Transition, Flat, Wall and dimension arrows "
                "reading 50-100m, 3m, 3-5m, 13-18m, plus red dotted flight trajectories"),

    figure(21, 2, "flowchart-or-schematic",
           caption("Figure 10: Basic (no slope in XZ plane) halfpipe"),
           mention(21, first=2, style=["figure 10"], count=1,
                   lead=span(2, "A basic halfpipe consists of two concave ramps", "(figure 10)"),
                   pattern="parenthetical"),
           path=[H_APP, H_APF1], kind="appendix", three_d="isometric", printed=False,
           labels=True,
           note="shaded CAD rendering of the half-pipe solid on a tan ground plane, with the "
                "X (green), Y (red) and Z (blue) axis lines drawn through it and no other "
                "labels, dimensions or ticks"),

    figure(22, 1, "table-as-figure",
           caption("Figure 11: Basic (Velocity Data for the Comprehensive Three Dimensional "
                   "Force Model"),
           mention(22, first=None, style=[], count=0),
           path=[H_APP, H_APF1], kind="appendix", panels=3, layout="column of 3",
           labels=True,
           note="three small tables stacked vertically and each given its own coloured title "
                "band and tint: X and Y Velocities for a Circle (r=10) in blue, Y and Z "
                "Velocities for a Parabola (y=0.07X^2-7) in green, Velocity for a parabola "
                "(y=0.1X^2-10) in orange; every one has Cycle Number, phi, Y velocity (m/s), "
                "Z velocity (m/s) columns with the unit in the header and no rules or shading "
                "cells other than the coloured bands; the caption is cut by an unbalanced "
                "bracket, the printed text reads Basic (Velocity Data ... (Model, which is "
                "what the record keeps"),

    figure(23, 1, "table-as-figure",
           caption("Figure 12: y and z velocities"),
           mention(23, first=None, style=[], count=0),
           path=[H_APP, H_APF2], kind="appendix", labels=True,
           note="one bordered grid: Shape, Angle of Mountain Slope (degrees), Y Velocity "
                "(m/s), Z velocity (m/s) over six body rows, Parabola 1, Parabola 2 and Circle "
                "each at 25 and 45 degrees; full frame with every cell ruled, units in the "
                "header, values to three decimals"),
]

TABLES = [
    table(9, 1,
          mention(9, first=None, style=[], count=0,
                  lead=span(9, "By breaking the velocity into y and z components",
                            "three different functions."),
                  trail=span(9, "In order to be able to compare these three functions",
                             "same (z,y)")),
          path=[H_RES, H_RES2D], kind="result",
          grid={"rows": 3, "cols": 6, "header_rows": 1, "rule_style": "boxed",
                "zebra": False, "merged_cells": False, "diagonal_header": False,
                "units_in_header": True, "decimal_aligned": False, "numeric_cols": 4,
                "text_cols": 2, "width": "full", "orientation": "portrait",
                "continued": False, "note_sentence": ""},
          note="uncaptioned and unreferenced results table printed straight into the text: "
               "Function, Z Velocity (m/s), Y Velocity (m/s), Line Color, Initial Position "
               "(m), Center over three rows (Parabola 2, Circle, Parabola 1); fully gridded "
               "with rules between every column, all cells centred, no shading. A second, "
               "smaller two-column table (Shape Name / Formula) sits directly under it inside "
               "the same measured region and is not measured separately"),

    table(12, 2,
          mention(12, first=None, style=[], count=0,
                  lead=span(12, "we evaluate the velocities this time", "both y and z directions."),
                  trail=span(12, "we can verify that the function yielding", "vertical air.")),
          path=[H_RES, H_RES3D], kind="result",
          grid={"rows": 3, "cols": 4, "header_rows": 1, "rule_style": "boxed",
                "zebra": False, "merged_cells": False, "diagonal_header": False,
                "units_in_header": True, "decimal_aligned": True, "numeric_cols": 3,
                "text_cols": 1, "width": "half", "orientation": "portrait",
                "continued": False, "note_sentence": ""},
          note="the 3D counterpart of the page-9 table, again with no caption and no Table "
               "reference: phi (degrees), Shape, Y Velocity (m/s), Z Velocity (m/s) over "
               "Parabola 1, Parabola 2 and Circle at a fixed 45 degrees; boxed grid with a "
               "rule under the header and between every column, values aligned to three "
               "decimals, set at roughly half the text measure"),
]

RULES = [
    "每个模型示意图都把力的方程组直接贴在图的左上角，图与公式是一体，读数顺序是先公式后图形 "
    "[geometry.data_labels]，[caption.words]。",
    "示意图共用一套词汇标注（DECK、COPING、VERT、TRANSITION、FLAT BOTTOM；"
    "New x axis、Shifted axis = red line），只印符号不印数字 [geometry.printed_numbers]，"
    "[geometry.family]。",
    "结果曲线图沿用 MATLAB 默认版式：图内标题（YZ Path Without Work、YZ Path With Added Work）"
    "顶替图例，坐标轴标题带单位 (m)，不设图例框、不标数据点 [geometry.legend]，"
    "[mention.trail_sentence]。",
    "同一组三条曲线换条件只改标题不改配色：红黑绿三色在两页里重复使用，"
    "x 轴范围随是否加入功而扩展到 20 m [geometry.family]，[place.page_order]。",
    "三维结果不用曲面网格，而用 + 标记的点迹画在等距三箭头坐标架上，六条轨迹并排一帧 "
    "[geometry.three_d]，[geometry.panel_count]。",
    "题注一律排在图下、Figure N: 冒号式、2-9 词的名词短语，只报图名、不给单位、不下结论，"
    "连 Dispacement、Ariel 这类错拼也照录 [caption.position]，[caption.numbering]，"
    "[caption.words]。",
    "正文引出以括号回指 (figure N) 为主，且常挂在长句末尾；两张结果图（Figure 4、5）"
    "连图号都不引，只用 the following graph 这种顺叙句带出 [mention.lead_pattern]，"
    "[mention.count]。",
    "引用距图面的页差两极：正文图多在引用后 0-1 页出现，Figure 2 早三页，"
    "附录的 Figure 9、10 在引言页就被引用、十九页后才出现 [mention.lead_pages]，"
    "[mention.first_page]。",
    "两张无题注的表直接插在结果正文里当数据表，全框线、单位写在表头、百分号先给条件行"
    "（45 度）再给两列速度 [table.rule_style]，[table.units_in_header]，"
    "[table.rows]。",
    "编号为图的表（Figure 11、12）沿用图的编号与题注体例，Figure 11 还把三张彩色小表竖排"
    "叠成一张图、三张各自带标题色带 [geometry.panel_count]，[geometry.family]。",
    "实验验证用照片而非绘图：PVC 管加布面搭出的坡面照，用两个蓝框标注 Slope of Mountain 与 "
    "Slope of transition，与仿真点迹图同页并列 [geometry.family]，[place.page_order]。",
    "附录图页只有图与题注、没有正文说明，题注紧贴图形下沿，图号在正文里从不出现 "
    "[place.section_kind]，[caption.position]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [],
    "note": "14 measured regions account for 12 figures and 2 uncaptioned body tables. "
            "Figures 11 and 12 are tables the team numbered as figures and stay in the figure "
            "block as table-as-figure. Page 9's region contains two stacked tables (six-column "
            "results plus a two-column Shape/Formula key); they are one measured region and "
            "are recorded once. Figure 11's caption is broken in the original — the printed "
            "text reads 'Basic (Velocity Data for the Comprehensive Three Dimensional Force "
            "Model' with no closing bracket, recorded verbatim.",
    "rules": RULES,
}

out = PROXY / f"{PID}-payload15.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items, {len(TABLES)} tables -> {out.name}")
