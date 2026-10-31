"""Hand pass for P-C-2010-7812-c2fa13fd (size-classified marine plastic, 11 figures + 6 tables).

Two-column pages, and the floats were set into that column flow, so the text layer
interleaves caption lines with body lines. Every caption whose line is split that way is
marked `typed-from-crop`; captions that the layer keeps whole stay `text-layer`.

The paper's figures divide cleanly by what varies. Figures 2-4 step the input rate for
Levels 1-3, Figures 5-7 step the input distribution D1/D2/D3 for Levels 1-3, Figure 8 is
the total, and Figures 9-11 turn the same three levels into wireframe surfaces over input
and decay rate. All eleven are plot-tool output: black-only, no legend box, the series
identified by in-plot italic labels with leader lines.

Tables are all fully boxed, captioned below, one column wide. Table 3's caption was set at
the top of the opposite column from its body; that split is recorded in the note rather
than repaired. Table 2 and Table 6 print no header row at all - the first row is data.

Figure 11's plot is the third surface on page 7 but its caption was pushed to page 8, so
its citation trail and the caption page disagree; recorded as is.

Usage: python -I tools/_dist_paper11.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2010-7812-c2fa13fd"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
REG = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda r: r["bbox"][1]), 1):
        REG[(pg["page"], i)] = r["bbox"]

S_MODEL = "未编号标题：Classified Plastic Concentration Model"
S_INPUT = "未编号标题：Plastic Input"
S_SIZES = "未编号标题：The Classification of the Sizes of Plastic Objects"
S_LEVELS = "未编号标题：Size Levels of Plastic Object"
S_ABS = "未编号标题：Effect of the Absolute Input Rate"
S_DIST = "未编号标题：Effect of the Distribution of Input"
S_PHOTO = "未编号标题：Factors Affect Photolysis Rate r2"
S_COMP = "未编号标题：Comparative Effect of r2 and I on Plastic Concentration"
S_PRE = "未编号标题：Plastic Wastes Pre-Dump Treatment"


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


def caption(v: str, numbering: str, position: str, source: str, *,
            units: bool = False, vars_: int = 0, cond: bool = False,
            concl: bool = False, voice: str = "none") -> dict:
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


def zone(page: int, idx: int) -> tuple[str, float, int]:
    """Page zone and area share from the measured region itself."""
    bbox = REG[(page, idx)]
    top, bottom = bbox[1], bbox[3]
    mid = (top + bottom) / 2
    height = 792.0
    z = "top" if mid < height / 3 else ("middle" if mid < 2 * height / 3 else "bottom")
    area = round((bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (612.0 * 792.0), 3)
    order = sum(1 for (p, i) in REG if p == page and i < idx) + 1
    return z, area, order


def place(page: int, idx: int, path: str, kind: str) -> dict:
    z, area, order = zone(page, idx)
    return {
        "section_path": [path],
        "section_numbered": False,
        "section_kind": kind,
        "doc_order": doc_order(page, idx),
        "page_order": order,
        "page_zone": z,
        "area_frac": area,
        "solo_page": False,
    }


PAGE_INDEX = sorted(REG)


def doc_order(page: int, idx: int) -> int:
    return PAGE_INDEX.index((page, idx)) + 1


def figure(page: int, idx: int, family: str, cap: dict, men: dict, *, path: str,
           kind: str, legend: str = "none", three_d: str = "no",
           printed: bool = True, labels: bool = False, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": cap["verbatim"],
        "caption_source": cap.pop("_source"),
        "note": note,
        "place": place(page, idx, path, kind),
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


def table(page: int, idx: int, cols: int, rows: int, header_rows: int, *,
          numeric: int, text_cols: int, cap: dict, men: dict, path: str,
          kind: str, merged: bool = False, units_header: bool = False,
          note_sentence: str = "", note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": cap.pop("_source"),
        "note": note,
        "place": place(page, idx, path, kind),
        "mention": men,
        "caption": cap,
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": "boxed",
            "zebra": False,
            "merged_cells": merged,
            "diagonal_header": False,
            "units_in_header": units_header,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": "column",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": note_sentence,
        },
    }


def cap_typed(v: str, numbering: str = "Figure N.", position: str = "below",
              **kw) -> dict:
    c = caption(v, numbering, position, "typed-from-crop", **kw)
    c["_source"] = "typed-from-crop"
    return c


def cap_layer(v: str, numbering: str, position: str = "below", **kw) -> dict:
    c = caption(v, numbering, position, "text-layer", **kw)
    c["_source"] = "text-layer"
    return c


F2 = cap_typed("Figure 2. Predicted concentration change of Level 1 plastic under "
               "various Size 1 input (I1=1, 0.1, 0.001kg/km2yr).")
F3 = cap_typed("Figure 3. Predicted concentration change of Level 2 plastic under "
               "various Size 1 input (I1=1, 0.1, 0.001kg/km2yr).")
F4 = cap_layer("Figure 4. Predicted concentration change of Level 3 plastic under "
               "various Size 1 input (I1=1, 0.1, 0.001kg/km2yr).", "Figure N.")
F5 = cap_typed("Figure 5. Predicted concentration change of Level 1 plastic under "
               "different distribution of input (D1, D2, D3).")
F6 = cap_typed("Figure 6. Predicted concentration change of Level 2 plastic under "
               "different distribution of input (D1, D2, D3).")
F7 = cap_typed("Figure 7. Predicted concentration change of Level 3 plastic under "
               "different distribution of input (D1, D2, D3).")
F8 = cap_layer("Figure 8. Predicted change of the total plastic concentration under "
               "different distribution of input (D1, D2, D3).", "Figure N.")
SURF = ("Figure %d. Predicted concentration change of Level %d plastic with photolysis "
        "rate of 1%%/yr-15%%/yr under input 0.08kg/km2yr-0.12kg/km2yr.")
F9 = cap_typed(SURF % (9, 1))
F10 = cap_typed(SURF % (10, 2))
F11 = cap_typed(SURF % (11, 3))

ITEMS = [
    figure(2, 1, "flowchart-or-schematic",
           cap_layer("Figure 1. Plastic inputs.", "Figure N.", "above"),
           mention(2, first=2, style=["Figure 1"], count=1,
                   lead=span(2, "See Figure 1 below", "below"), pattern="direct",
                   read=0),
           path=S_INPUT, kind="model", printed=False, labels=True,
           note="one blue ellipse (Human) funneling through a fat arrow into two "
                "rectangle groups (AOI, OA) joined by a double-headed Balance arrow; "
                "the lower half of the same diagram is measured as a separate region and "
                "excluded as a fragment"),

    figure(5, 2, "line", F2,
           mention(5, first=9, style=["Figure 2"], count=1,
                   lead=span(5, "with different input rates",
                             "C3 (t)")),
           path=S_ABS, kind="result",
           note="three black curves (solid, dotted, dashed) over 0-100 yr; the three "
                "input rates are named by italic in-plot labels I1 I2 I3 with leader "
                "lines, not by a legend box"),

    figure(5, 3, "line", F3,
           mention(5, first=9, style=["Figure 3"], count=1,
                   lead=span(5, "with different input rates",
                             "C3 (t)")),
           path=S_ABS, kind="result",
           note="same three-curve grammar on the Level 2 axis, 0-20 kg/km2"),

    figure(5, 1, "line", F4,
           mention(5, first=9, style=["Figure 4"], count=1,
                   lead=span(5, "with different input rates",
                             "C3 (t)")),
           path=S_ABS, kind="result",
           note="same grammar on the Level 3 axis; the right-column figure of the page"),

    figure(6, 2, "line", F5,
           mention(6, first=6, style=["Figure 5"], count=1,
                   lead=span(6, "The effect of the three distribution",
                             "Figure 5, 6 and 7")),
           path=S_DIST, kind="result",
           note="distribution trial: three black curves labelled in-plot D1 D2 D3, "
                "Level 1 axis 0-12 kg/km2"),

    figure(6, 3, "line", F6,
           mention(6, first=6, style=["Figure 6"], count=1,
                   lead=span(6, "The effect of the three distribution",
                             "Figure 5, 6 and 7")),
           path=S_DIST, kind="result",
           note="Level 2 axis 0-10 kg/km2, same three distributions"),

    figure(6, 4, "line", F7,
           mention(6, first=6, style=["Figure 7"], count=1,
                   lead=span(6, "The effect of the three distribution",
                             "Figure 5, 6 and 7")),
           path=S_DIST, kind="result",
           note="Level 3 axis 0-100 kg/km2; the yield of this level is physically "
                "uncontrollable, which the text uses to justify stopping here"),

    figure(6, 1, "line", F8,
           mention(6, first=None, style=[], count=0),
           path=S_DIST, kind="result",
           note="total concentration summed over levels, 0-120 kg/km2, the only figure "
                "in the distribution block that is not one level"),

    figure(7, 1, "surface-or-3D", F9,
           mention(7, first=8, style=["Figure 9"], count=1,
                   lead=span(8, "Compared among", "Figure 9, 10, and 11")),
           path=S_PHOTO, kind="sensitivity", three_d="surface-mesh",
           note="black wireframe surface, axes Level 1 Input 0.08-0.12, Chemical Decay "
                "Rate 0-0.10, concentration up the vertical; no colour, no legend"),

    figure(7, 2, "surface-or-3D", F10,
           mention(7, first=8, style=["Figure 10"], count=1,
                   lead=span(8, "Compared among", "Figure 9, 10, and 11")),
           path=S_COMP, kind="sensitivity", three_d="surface-mesh",
           note="same surface grammar on the Level 2 axis; in-plot title C2 vs. l1 r2 "
                "instead of a legend"),

    figure(7, 3, "surface-or-3D", F11,
           mention(7, first=8, style=["Figure 11"], count=1,
                   lead=span(8, "Compared among", "Figure 9, 10, and 11")),
           path=S_COMP, kind="sensitivity", three_d="surface-mesh",
           note="Level 3 surface, title C3 vs. l1 r2; its caption was pushed to the top "
                "of page 8, so caption page and exhibit page differ"),
]

TABLES = [
    table(1, 1, 6, 4, 2, numeric=0, text_cols=6, merged=True,
          cap=cap_typed("Table 1. Source-coefficient matrix. C: plastic source from "
                        "consumers; I: plastic source from industries; S: plastic source "
                        "from shipping; F: plastic source from fishing.", "Table N."),
          men=mention(1, first=1, style=["Table 1"], count=2,
                      lead=span(1, "coefficient matrix for this model",
                                "as the followings:"), pattern="none"),
          path=S_MODEL, kind="model",
          note="two-row header: Sources spans both header rows, Plastic Wastes Inputs "
               "spans Type1..TypeN; the stub column then lists C I S F, so the body is "
               "all symbols and no numbers"),

    table(2, 3, 3, 4, 1, numeric=0, text_cols=3,
          cap=cap_typed("Table 2. Category of the Sizes of Plastics.", "Table N."),
          men=mention(2, first=None, style=[], count=0,
                      lead=span(2, "ranges or categories",
                                "as listed below:")),
          path=S_SIZES, kind="model",
          note="no column-label row at all: the first line is already Level 1, so the four "
               "rows are the size classes in superscript notation; header_rows is held at "
               "the schema floor of 1, the panel prints none"),

    table(4, 3, 3, 4, 1, numeric=2, text_cols=1,
          cap=cap_layer("Table 3. Size Level in Length (m).", "Table N.", "below"),
          men=mention(4, first=8, style=["Table 3"], count=2),
          path=S_LEVELS, kind="model",
          note="caption was set at the top of the right column while the body sits at the "
               "foot of the left column; the region measures the body only, so caption "
               "and table are split by the column break"),

    table(4, 1, 3, 4, 1, numeric=2, text_cols=1,
          cap=cap_layer("Table 4. Size Level in Volume (m3).", "Table N.", "below"),
          men=mention(4, first=None, style=[], count=0),
          path=S_LEVELS, kind="model",
          note="same three columns as Table 3 but the middle column is the volume range; "
               "this is the table whose caption sits directly above it"),

    table(4, 2, 2, 4, 1, numeric=1, text_cols=1, units_header=True,
          cap=cap_layer("Table 5. Degradation rates of different plastic products in "
                        "size range 5*10-6m-5*10-4m, which represents the size of the "
                        "marine environment.", "Table N.", "below", units=True),
          men=mention(4, first=None, style=[], count=0,
                      lead=span(4, "plastic in the ocean varies from",
                                "450 years")),
          path=S_LEVELS, kind="model",
          note="product against years-to-decay, unit written into the header as "
               "Degradation Rate (year); the caption then re-states the size range"),

    table(9, 1, 2, 4, 1, numeric=0, text_cols=2,
          cap=cap_layer("Table 6. Pre-dump Treatment and Concentration", "Table N.",
                        "below"),
          men=mention(9, first=None, style=[], count=0,
                      trail=span(9, "This table implies 3 things", "3 things:")),
          path=S_PRE, kind="evaluation",
          note="decision matrix with no column-label row: four levels down the stub and D1/D2 "
               "stated as words in the second column, so nothing numeric is tabulated; "
               "header_rows held at the schema floor of 1"),
]

RULES = [
    "本题型两栏排版，图表插入栏内、宽度只有一栏，正文自动绕排，"
    "结果是每条题注在文本层都被正文截成两段 [table.width]，[caption.verbatim]。",
    "图与表都靠题注自明：全篇没有 Figure N shows 句式，"
    "引用集中在对比句里（Based on Figure 2, 3, and 4；Compared among Figure 9, 10, and 11）"
    "[mention.lead_pattern]，[mention.count]。",
    "同一组图按「改变哪一个参数」排成三连：Figure 2-4 改输入速率、Figure 5-7 改输入分布，"
    "每条曲线按 Level 1/2/3 逐页递进 [geometry.family]，[place.section_kind]。",
    "折线图一律黑白三线（实线/点线/虚线），不画图例框，"
    "系列名用斜体字加引线直接写在曲线上（I1 I2 I3 或 D1 D2 D3）[geometry.legend]。",
    "进入灵敏度讨论后图形换成三维线框曲面：横轴输入、纵轴衰减率、竖轴浓度，"
    "无颜色、无色标、无网格底纹 [geometry.three_d]，[geometry.colorbar]。",
    "两张示意图用蓝色填充块区分「主体」与「区域」，箭头一律加粗，"
    "反馈关系用双向箭头 [geometry.data_labels]。",
    "图题一律 Figure N. 带句点、置于图下；表题 Table N. 也在表下，"
    "本刊式样与常见「表题在上」相反 [caption.position]，[caption.numbering]。",
    "题注长度被拆成两截，短则三词（Figure 1. Plastic inputs.）、"
    "长则二十余词并带参数取值 [caption.words]。",
    "表格全部四边全框（boxed）、单栏宽、竖版、不续表，无隔行底纹 [table.rule_style]，"
    "[table.zebra]，[table.continued]。",
    "两张表干脆不设表头行（Table 2、Table 6），首行即数据 [table.header_rows]。",
    "表头合并只出现在 Table 1：Sources 纵跨两行、Plastic Wastes Inputs 横跨 Type1..TypeN "
    "[table.merged_cells]。",
    "单位写进表头的只有 Table 5（Degradation Rate (year)），其余把单位留在题注 "
    "[table.units_in_header]，[caption.units]。",
    "表体数值以科学计数区间为主，不按小数点对齐 [table.decimal_aligned]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [
        {"page": 2, "bbox": REG[(2, 2)], "reason": "fragment-of-other",
         "note": "lower half of the Figure 1 flow diagram, the AOI/OA balance boxes"},
    ],
    "rules": RULES,
}

out = PROXY / f"{PID}-payload11.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items + {len(TABLES)} tables -> {out.name}")
