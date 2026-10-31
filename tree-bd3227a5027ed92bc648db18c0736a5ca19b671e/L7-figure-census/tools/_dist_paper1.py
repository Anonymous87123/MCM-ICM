"""Paper 1 distillation rows, hand-coded from the crops and the text layer.

Judgement calls written here, each backed by what a crop showed:

- Figure 2 (p11) was carried as `line` in the census. It is not a plot: eight circular
  cross-sections above three longitudinal bat profiles with a 0-34 scale, i.e. a
  schematic drawing. Corrected to `flowchart-or-schematic` with panel_count 4.
- p51 and p52 are boxed MATLAB listings, not exhibits. They move from items to
  excluded / not-an-exhibit (the paper-8 precedent for program listings).
- Tables 1 and 5 share one layout: full grid with vertical separators, one merged cell
  in the "Outline Shape" row, units inside the cells. Table 2 is booktabs. Table 4 is a
  single-row booktabs table with units in its header.
- The paper prints "Figure 2 shows the scheme for model" for the exhibit whose own
  caption is "Figure 3. scheme for double spring model": the reference and the caption
  disagree. The mention keeps the printed spelling and the note records the clash.
- No caption in this paper sits above its exhibit; every one is below or beside.

Sentences are pulled out of the text layer by needle, never retyped, so each quote is an
exact substring and the record's quote check is meaningful.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2010-6749-395f556a"
SKEL = LANE / ".proxy" / f"{PID}-skel.json"
CTX = LANE / ".proxy" / f"{PID}-ctx.json"


def sent(page: int, needle: str) -> str:
    for unit in schema.page_units(PID, page):
        for part in re.split(r"(?<=[.!?])\s+", unit):
            if needle in part:
                return part.strip()
    raise SystemExit(f"no sentence with {needle!r} on page {page}")


def span(page: int, start: str, end: str) -> str:
    """Contiguous slice of the page text from `start` through `end`, never retyped.

    Used where the text layer runs several sentences into one unit (typeset maths
    breaks the sentence split), so a full sentence would blow the 25-word cap.
    """
    for unit in schema.page_units(PID, page):
        i = unit.find(start)
        if i < 0:
            continue
        j = unit.find(end, i)
        if j < 0:
            continue
        return unit[i:j + len(end)]
    raise SystemExit(f"no span {start!r} .. {end!r} on page {page}")


def cap(page: int, number: int) -> str:
    ctx = json.loads(CTX.read_text(encoding="utf-8"))
    for c in ctx["captions"]:
        if c["page"] == page and c["number"] == number:
            return c["text"]
    raise SystemExit(f"no caption {number} on page {page}")


# (page, family, panels, layout, shared, legend, cbar, 3d, printed, labels)
FIG_GEOM = {
    6: ("flowchart-or-schematic", 1, "1", False, "none", False, "no", False, False),
    11: None,  # two exhibits on this page, handled below by doc order
    15: ("line", 1, "1", False, "inside", False, "no", True, True),
    16: ("flowchart-or-schematic", 1, "1", False, "none", False, "no", False, False),
    18: ("line", 1, "1", False, "none", False, "no", True, True),
    19: ("line", 1, "1", False, "none", False, "no", True, True),
    20: ("line", 1, "1", False, "none", False, "no", True, True),
    21: ("line", 1, "1", False, "none", False, "no", True, False),
    22: ("line", 1, "1", False, "none", False, "no", True, True),
    23: ("line", 1, "1", False, "none", False, "no", True, True),
    24: ("line", 1, "1", False, "none", False, "no", True, True),
    25: ("line", 1, "1", False, "none", False, "no", True, True),
    26: ("line", 1, "1", False, "none", False, "no", True, True),
    27: ("line", 2, "1 + inset", False, "inside", False, "no", True, True),
    28: ("surface-or-3D", 1, "1", False, "none", True, "surface-mesh", True, True),
    29: ("heatmap-or-contour", 1, "1", False, "none", False, "no", True, True),
    30: ("heatmap-or-contour", 1, "1", False, "none", False, "no", True, True),
    32: ("flowchart-or-schematic", 2, "1x2", False, "none", False, "no", True, True),
    33: ("flowchart-or-schematic", 1, "1", False, "inside", False, "no", False, False),
    34: ("flowchart-or-schematic", 2, "1x2", False, "none", False, "no", True, True),
    37: ("composite-panel", 2, "1x2 stacked", False, "none", False, "no", False, False),
    38: ("flowchart-or-schematic", 1, "1", False, "outside-right", False, "no", False, False),
    40: ("flowchart-or-schematic", 4, "column of 4", False, "none", False, "no", True, True),
    41: ("line", 4, "column of 4", True, "none", False, "no", True, True),
    42: ("line", 1, "1", False, "none", False, "no", True, False),
    50: ("line", 1, "1", False, "inside", False, "no", True, True),
}

# doc_order -> fields the crops decided, in the order the blocks read them
FIG = {
    1: dict(fam="flowchart-or-schematic", panels=1, layout="1", shared=False,
            legend="none", cbar=False, three_d="no", printed=False, labels=False,
            cap=("Figure 1. Illustration of theoretical derivation", "below", False, 0,
                 False, False, "none"),
            lead=None, trail=span(7, "are the angles of the directions", "."),
            pattern="as-shown-in",
            first=7, count=1, read=1,
            note="side view of bat and ball with velocity vectors and angle arcs"),
    2: dict(fam="flowchart-or-schematic", panels=4, layout="1x8 above 1x3", shared=True,
            legend="inside", cbar=False, three_d="no", printed=True, labels=True,
            cap=(cap(11, 2), "below", False, 0, False, False, "none"),
            lead=None, trail=None, pattern="none", first=None, count=0, read=0,
            note="eight hoop cross-sections over three longitudinal mode profiles, "
                 "frequencies 1428/1887/2520 Hz, common 0-34 scale; carried as line in "
                 "the census, corrected to a schematic"),
    3: dict(fam="flowchart-or-schematic", panels=2, layout="1x2", shared=False,
            legend="none", cbar=False, three_d="no", printed=False, labels=False,
            cap=(cap(11, 3), "below", False, 0, False, False, "none"),
            lead=sent(11, "shows the scheme for model"), trail=None,
            pattern="figure-n-shows", first=11, count=1, read=0,
            note="ball with spring and corked bat with spring, double-spring model; the "
                 "body text calls this scheme Figure 2 while the caption says Figure 3"),
    5: dict(fam="line", panels=1, layout="1", shared=False, legend="inside", cbar=False,
            three_d="no", printed=True, labels=True,
            cap=(cap(15, 4), "below", True, 0, False, False, "none"),
            lead=None, trail=span(25, "our data obtained from calculation", "experimental data"),
            pattern="none", first=25, count=1, read=1,
            note="speed vs bat weight, data points plus a fitted falling line, cited "
                 "experiment; the only figure in the paper reused as validation later"),
    6: dict(fam="flowchart-or-schematic", panels=1, layout="1", shared=False,
            legend="none", cbar=False, three_d="no", printed=False, labels=False,
            cap=(cap(16, 5), "below", False, 0, False, False, "none"),
            lead=sent(16, "quantitative method is needed"), trail=None, pattern="direct",
            first=16, count=1, read=1,
            note="longitudinal section of a corked bat with hatched shell, mass centre "
                 "and dimension letters"),
    8: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
            three_d="no", printed=True, labels=True,
            cap=(cap(18, 6), "below", True, 2, True, False, "none"),
            lead=None, trail=sent(18, "still has a distance of about 0.15m from the tip"),
            pattern="parenthetical", first=18, count=2, read=1,
            note="two near-horizontal lines (tip of the bat, sweet spot) over ball speed"),
    9: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
            three_d="no", printed=True, labels=True,
            cap=(cap(19, 7), "below", True, 2, True, False, "none"),
            lead=None, trail=sent(19, "In the same manner"),
            pattern="parenthetical", first=19, count=2, read=1,
            note="same two-line layout as Figure 6, swinging speed on x"),
    10: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(20, 8), "below", True, 2, True, False, "none"),
             lead=None, trail=sent(20, "similarly, the"),
             pattern="parenthetical", first=19, count=2, read=1,
             note="same two-line layout, angular velocity on x"),
    11: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=False,
             cap=(cap(21, 9), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="single hump-shaped curve of BBS against impact location, mirrored axes"),
    12: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(22, 10), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="three S-curves labelled e_ball 0.4/0.5/0.6 on a log x axis"),
    13: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(23, 11), "below", True, 2, True, False, "none"),
             lead=sent(22, "which is illustrated in Figure 11"), trail=None,
             pattern="as-shown-in", first=22, count=1, read=1,
             note="three sigmoid curves, e_ball labels with leader arrows, log x"),
    14: dict(fam="flowchart-or-schematic", panels=1, layout="1", shared=False,
             legend="none", cbar=False, three_d="no", printed=True, labels=True,
             cap=("", "below", False, 0, False, False, "none"),
             lead=span(23, "The procedure to simulate", "as following"),
             trail=None, pattern="as-shown-in", first=23, count=1, read=0,
             note="block diagram J -> Eq 18 -> omega -> Eq 14 -> b -> Eq 4 -> v; "
                  "unnumbered, its three inner labels carry Figure 12/13/14 tags"),
    15: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(24, 12), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="single descending line, J on x, angular velocity on y"),
    16: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(24, 13), "below", True, 3, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="single rising line, J on x, sweet-spot location on y; caption states "
                  "the fixed V_i, v_i and M"),
    17: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(25, 14), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="single rising line, J on x, maximum BBS on y"),
    18: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(26, 15), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="single falling curve, corked mass on x, bat speed on y"),
    19: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(26, 16), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="single decaying curve with a flat tail, corked mass on x"),
    20: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=(cap(27, 17), "below", True, 2, True, False, "none"),
             lead=sent(25, "we easily obtain the similar result"),
             trail=sent(25, "getting slow with the increase of mass"),
             pattern="direct", first=25, count=2, read=2,
             note="single saturating curve, corked mass on x, maximum BBS on y"),
    21: dict(fam="line", panels=2, layout="1 + inset", shared=False, legend="inside",
             cbar=False, three_d="no", printed=True, labels=True,
             cap=(cap(27, 18), "below", True, 2, True, False, "none"),
             lead=sent(25, "as Figure 18 shows"), trail=None,
             pattern="as-shown-in", first=25, count=1, read=1,
             note="two curves on one axis plus an Ideal Bat Weight inset, the only "
                  "two-variable overlay among the single-curve figures"),
    22: dict(fam="surface-or-3D", panels=1, layout="1", shared=False, legend="none",
             cbar=True, three_d="surface-mesh", printed=True, labels=True,
             cap=("Figure 19 Figure in a wireframe mesh style.", "below", True, 2, True,
                  False, "none"),
             lead=span(28, "In Figure 19, we set the density", "stuffed material"), trail=None,
             pattern="direct", first=28, count=1, read=1,
             note="3D mesh surface with colour bar, projected contours on the floor and "
                  "a data cursor readout"),
    23: dict(fam="heatmap-or-contour", panels=1, layout="1", shared=False, legend="none",
             cbar=False, three_d="no", printed=True, labels=True,
             cap=("Figure 20 Same Figure in contour style.", "below", False, 2, False,
                  False, "none"),
             lead=None, trail=None, pattern="none", first=30, count=1, read=1,
             note="same surface as Figure 19 in 2D, level values printed on the curves, "
                  "no colour bar"),
    24: dict(fam="surface-or-3D", panels=1, layout="1", shared=False, legend="none",
             cbar=True, three_d="surface-mesh", printed=True, labels=True,
             cap=(cap(29, 21), "below", True, 2, True, False, "none"),
             lead=span(28, "In Figure 21, the density", "stuffed material"), trail=None,
             pattern="direct",
             first=28, count=1, read=1,
             note="second 3D mesh surface, rubber density, colour bar and floor contours"),
    25: dict(fam="heatmap-or-contour", panels=1, layout="1", shared=False, legend="none",
             cbar=False, three_d="no", printed=True, labels=True,
             cap=(cap(30, 22), "below", False, 2, False, False, "none"),
             lead=None, trail=None, pattern="none", first=30, count=1, read=1,
             note="2D contour twin of Figure 21, level values printed, no colour bar"),
    26: dict(fam="flowchart-or-schematic", panels=2, layout="1x2", shared=False,
             legend="none", cbar=False, three_d="no", printed=True, labels=True,
             cap=(cap(32, 23), "below", False, 0, False, False, "none"),
             lead=sent(31, "Figure 23 is an illustration of a typical metal bat"),
             trail=None, pattern="direct", first=31, count=1, read=0,
             note="patent-style drawing of a metal bat with a cross-section inset and "
                  "numbered callouts"),
    27: dict(fam="flowchart-or-schematic", panels=1, layout="1", shared=False,
             legend="inside", cbar=False, three_d="no", printed=False, labels=False,
             cap=(cap(33, 24), "below", False, 0, False, False, "none"),
             lead=sent(32, "We picture a logic relationship"), trail=None,
             pattern="direct", first=32, count=2, read=2,
             note="three-column block diagram (contrast objectives, intermediate "
                  "variable, behaviour) with an arrow-key legend"),
    29: dict(fam="flowchart-or-schematic", panels=2, layout="1x2", shared=False,
             legend="none", cbar=False, three_d="no", printed=True, labels=True,
             cap=(cap(34, 25), "below", False, 0, False, False, "none"),
             lead=sent(39, "Through calculation we obtain a diagram of the demo bat"),
             trail=None, pattern="direct", first=39, count=1, read=1,
             note="engineering drawing of the hollowed bat with dimensions"),
    32: dict(fam="composite-panel", panels=2, layout="1x2 stacked", shared=False,
             legend="none", cbar=False, three_d="no", printed=False, labels=False,
             cap=(cap(37, 26), "below", False, 0, False, False, "none"),
             lead=sent(37, "One of the possibilities is shown in Figure 26"), trail=None,
             pattern="direct", first=37, count=1, read=1,
             note="schematic of a cavity bat above a freehand mass-distribution curve"),
    33: dict(fam="flowchart-or-schematic", panels=1, layout="1", shared=False,
             legend="outside-right", cbar=False, three_d="no", printed=False, labels=False,
             cap=(cap(38, 27), "below", False, 0, False, False, "none"),
             lead=sent(38, "we adopt a simple and special"), trail=None,
             pattern="direct", first=38, count=1, read=1,
             note="cross-section with original and removed mass swatches"),
    34: dict(fam="flowchart-or-schematic", panels=4, layout="column of 4", shared=False,
             legend="none", cbar=False, three_d="no", printed=True, labels=True,
             cap=(cap(40, 28), "below", False, 0, False, False, "none"),
             lead=sent(39, "Literature review indicates"),
             trail=sent(39, "the latter two"), pattern="parenthetical", first=39,
             count=2, read=2,
             note="four rows #1-#4 of collision-model schematics, two of them with "
                  "hysteresis loops"),
    35: dict(fam="line", panels=4, layout="column of 4", shared=True, legend="none",
             cbar=False, three_d="no", printed=True, labels=True,
             cap=(cap(41, 29), "below", False, 0, False, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="four bending modes 1-4 with Hz values on one 0-34 scale"),
    36: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=False,
             cap=(cap(42, 30), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="vibration energy percent against distance from knob"),
    37: dict(fam="line", panels=1, layout="1", shared=False, legend="none", cbar=False,
             three_d="no", printed=True, labels=False,
             cap=(cap(42, 31), "below", True, 2, True, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="e_eff against distance from knob, rising then falling"),
    38: dict(fam="line", panels=1, layout="1", shared=False, legend="inside", cbar=False,
             three_d="no", printed=True, labels=True,
             cap=("", "below", False, 0, False, False, "none"),
             lead=None, trail=None, pattern="none", first=None, count=0, read=0,
             note="three saturating curves over log k_ball/k_bat, e_ball labelled by "
                  "leader arrows, two bracket annotations 1886.5 and 5.5; sits in "
                  "Appendix II, no caption"),
}

TABLES = {
    4: dict(cap="Table 1 The interrelationship between parameters and effects on BBS",
            # the text layer splits "Table" as "Tab le 1." here (ligature); the quote is
            # copied from the layer as it stands so the substring check stays meaningful
            lead=sent(13, "list the above analysis results"), first=13, count=1,
            table=dict(rows=6, cols=6, header_rows=1, rule_style="boxed", zebra=False,
                       merged_cells=False, diagonal_header=False, units_in_header=False,
                       decimal_aligned=False, numeric_cols=0, text_cols=6, width="full",
                       orientation="portrait", continued=False, note_sentence=""),
            note="symbolic table: parameter rows against effect columns, arrows and "
                 "emoticon faces in the cells"),
    7: dict(cap=cap(17, 2), lead=sent(18, "listed in Table 2"), first=18, count=1,
            table=dict(rows=8, cols=3, header_rows=1, rule_style="booktabs", zebra=False,
                       merged_cells=False, diagonal_header=False, units_in_header=False,
                       decimal_aligned=False, numeric_cols=1, text_cols=2, width="full",
                       orientation="portrait", continued=False, note_sentence=""),
            note="Property / Description / Value, eight simulation inputs with units in "
                 "the value cells"),
    28: dict(cap="Table 3. The design parameters of the special aluminum bat.",
             lead=None, first=None, count=0,
             table=dict(rows=7, cols=4, header_rows=1, rule_style="boxed", zebra=False,
                        merged_cells=True, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=2, text_cols=2, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="wood vs aluminium parameters, one merged row, units inside the cells"),
    30: dict(cap=cap(34, 4), lead=None, first=None, count=0,
             table=dict(rows=2, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=True,
                        decimal_aligned=False, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=True, note_sentence=""),
             note="two material rows, all six columns carry units in the header; the "
                  "metal-bat row runs over to the top of p35"),
    31: dict(cap=cap(37, 5), lead=None, first=None, count=0,
             table=dict(rows=7, cols=4, header_rows=1, rule_style="boxed", zebra=False,
                        merged_cells=True, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=2, text_cols=2, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="identical layout to Table 3, restated for the customized bat"),
}

RULES = [
    "图解集中在建模与求解节，假设节和符号节零图 [place.section_kind]",
    "力学示意一律侧视剖面：不印刻度数字，靠尺寸字母和矢量箭头读 [geometry"
    ".printed_numbers]",
    "曲线图必印刻度数字；同一自变量的兄弟图共用纵轴单位与刻度，纵轴只标一次 "
    "[geometry.shared_axes]",
    "三维曲面只在双变量参数扫描时出现，且必配一张同数据的二维等高线孪生图 "
    "[geometry.three_d]",
    "三维图带色标，二维等高线不带；色标是判断三维的唯一硬指标 [geometry.colorbar]",
    "题注全部在图下方，编号统一 Figure N. 加冒号式副标题 [caption.position]",
    "题注超过十字就把固定条件写进去（where/given + 参数值），短题注只给名词短语 "
    "[caption.conditions]",
    "引出句以括号回指为主，主谓句只在首次提及时用一次 [mention.lead_pattern]",
    "同族连续图靠 similarly / In the same manner 承接，不重写引出句 "
    "[mention.trail_sentence]",
    "数据表用全框线，booktabs 只留给单行参数表 [table.rule_style]",
    "单位写进数据格，只有单行表才把单位提上表头 [table.units_in_header]",
    "数值列小数点对齐、文本列靠左；两态对照表用一行合并单元格合并同材料行 "
    "[table.decimal_aligned]",
]

EXCLUDED = [
    (51, [84.24, 157.32, 511.44, 767.88], "not-an-exhibit",
     "p51 boxed MATLAB listing, not an exhibit; sits in Appendix III Codes for MATLAB"),
    (52, [84.24, 72.00, 511.44, 292.68], "not-an-exhibit",
     "p52 continuation of the MATLAB listing"),
]

# Measured regions that are not exhibits of their own, with the reason the record uses.
FRAGMENTS = [
    (18, [203.96, 604.89, 419.15, 633.69], "fragment-of-other",
     "axis strip inside the Figure 6 bbox, already counted in its panel geometry"),
    (27, [372.75, 579.75, 464.80, 659.25], "fragment-of-other",
     "Ideal Bat Weight inset inside the Figure 18 bbox, counted as its second panel"),
    (35, [83.94, 72.02, 503.51, 122.32], "split-across-pages",
     "metal-bat row of Table 4 carried over to the top of p35; the table is one "
     "exhibit spanning p34-p35"),
    (37, [147.52, 294.14, 453.24, 333.80], "fragment-of-other",
     "upper panel of Figure 26 (bat section A-A with m(z)), laid out above the curve "
     "panel and separated by the layout extractor"),
]


def geometry(entry: dict) -> dict:
    return {"family": entry["fam"], "panel_count": entry["panels"],
            "panel_layout": entry["layout"], "shared_axes": entry["shared"],
            "legend": entry["legend"], "colorbar": entry["cbar"],
            "three_d": entry["three_d"], "printed_numbers": entry["printed"],
            "data_labels": entry["labels"]}


def caption_block(entry: dict) -> dict:
    text, position, units, variables, cond, concl, voice = entry["cap"]
    return {"verbatim": text, "numbering": numbering(text), "words": len(schema.words(text)),
            "sentences": max(1, len([s for s in re.split(r"(?<=[.!?])\s+", text) if s])),
            "units": units, "variables": bool(variables), "variable_count": variables,
            "conditions": cond, "concludes": concl, "voice": voice,
            "position": position}


def numbering(text: str) -> str:
    if not text:
        return "none"
    if re.match(r"^Figure\s+\d+\s*:", text):
        return "Figure N:"
    if re.match(r"^Figure\s+\d+\s*\.", text):
        return "Figure N."
    if re.match(r"^Figure\s+\d+", text):
        return "Figure N"
    if re.match(r"^Table\s+\d+\s*:", text):
        return "Table N:"
    if re.match(r"^Table\s+\d+\s*\.", text):
        return "Table N."
    if re.match(r"^Table\s+\d+", text):
        return "Table N"
    return "none"


def main() -> None:
    skel = json.loads(SKEL.read_text(encoding="utf-8"))
    by_order = {e["doc_order"]: e for e in skel}
    items, tables, excluded = [], [], []
    for order, entry in sorted(FIG.items()):
        base = by_order[order]
        page = base["page"]
        mention = {
            "first_page": entry["first"],
            "lead_pages": None if entry["first"] is None else page - entry["first"],
            "style": [] if entry["first"] is None else
                     [f"Figure {re.match(r'^[^0-9]*([0-9]+)', entry['cap'][0]).group(1)}"
                      if entry["cap"][0] else ""],
            "count": entry["count"],
            "lead_sentence": entry["lead"] or "",
            "trail_sentence": entry["trail"] or "",
            "lead_pattern": entry["pattern"],
            "read_sentences": entry["read"],
            "gap_sentences": base["gap_auto"],
        }
        mention["style"] = [s for s in mention["style"] if s]
        items.append({
            "page": page, "bbox": base["bbox"], "family": entry["fam"],
            "confidence": "high", "panel_count": entry["panels"], "table": False,
            "caption_verbatim": entry["cap"][0],
            "caption_source": "text-layer" if entry["cap"][0] else "none",
            "excluded": None, "other_note": None, "note": entry["note"],
            "place": {"section_path": base["section_path"],
                      "section_numbered": base["section_numbered"],
                      "section_kind": base["section_kind"],
                      "doc_order": base["doc_order"], "page_order": base["page_order"],
                      "page_zone": base["page_zone"], "area_frac": base["area_frac"],
                      "solo_page": base["solo_page"]},
            "mention": mention, "caption": caption_block(entry),
            "geometry": geometry(entry),
        })
    for order, entry in sorted(TABLES.items()):
        base = by_order[order]
        page = base["page"]
        tbl = dict(entry["table"])
        tables.append({
            "page": page, "bbox": base["bbox"], "family": "table-grid",
            "caption_verbatim": entry["cap"],
            "caption_source": "text-layer",
            "note": entry["note"],
            "place": {"section_path": base["section_path"],
                      "section_numbered": base["section_numbered"],
                      "section_kind": base["section_kind"],
                      "doc_order": base["doc_order"], "page_order": base["page_order"],
                      "page_zone": base["page_zone"], "area_frac": base["area_frac"],
                      "solo_page": base["solo_page"]},
            "mention": {"first_page": entry["first"],
                        "lead_pages": None if entry["first"] is None
                        else page - entry["first"],
                        "style": [f"Table {re.match(r'^[^0-9]*([0-9]+)', entry['cap']).group(1)}"],
                        "count": entry["count"],
                        "lead_sentence": entry["lead"] or "", "trail_sentence": "",
                        "lead_pattern": "direct" if entry["lead"] else "none",
                        "read_sentences": 1 if entry["lead"] else 0,
                        "gap_sentences": base["gap_auto"]},
            "caption": {"verbatim": entry["cap"], "numbering": numbering(entry["cap"]),
                        "words": len(schema.words(entry["cap"])),
                        "sentences": max(1, len([s for s in
                                                 re.split(r"(?<=[.!?])\s+", entry["cap"])
                                                 if s])),
                        "units": False, "variables": False, "variable_count": 0,
                        "conditions": False, "concludes": False, "voice": "none",
                        "position": "above"},
            "table": tbl,
        })
    for page, bbox, reason, note in EXCLUDED:
        excluded.append({"page": page, "bbox": bbox, "reason": reason, "note": note})
    for page, bbox, reason, note in FRAGMENTS:
        excluded.append({"page": page, "bbox": bbox, "reason": reason, "note": note})

    payload = {
        "paper": PID,
        "layout_sha256": json.loads(
            (LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))["layout_sha256"],
        "items": items, "tables": tables, "excluded_regions": excluded,
        "rules": RULES,
        "note": "distillation backfill: captions below, tables differentiated by rule "
                "style, two code listings excluded",
    }
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"items {len(items)} tables {len(tables)} excluded {len(excluded)} -> {out}")
    over = []
    for block in items + tables:
        for key in ("lead_sentence", "trail_sentence"):
            value = block["mention"][key]
            if value and len(schema.words(value)) > schema.MAX_QUOTE_WORDS:
                over.append((block["place"]["doc_order"], key, len(schema.words(value)),
                             value[:70].encode("ascii", "replace").decode()))
    for row in over:
        print("  over cap:", row)


if __name__ == "__main__":
    main()
