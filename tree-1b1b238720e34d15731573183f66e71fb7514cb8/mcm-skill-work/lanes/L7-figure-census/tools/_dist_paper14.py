"""Hand pass for P-A-2011-11199-cfe6d809 (half-pipe design, 18 figures + 0 printed tables).

The paper is one long design argument and the floats walk with it: three background figures
(television hours, half-pipe components, Olympic dimensions) open the introduction, then one
figure per model step — candidate profiles, the cycloid construction, the free-body diagram,
the flat-oval cross-section — and then the result block, where every simulation is shown as
a four-panel plot followed by a summary table that the authors caption as a figure.

Two layout facts decide the exclusions. The free-body diagram on page 7 is one vector
drawing with six rasterised label strips stacked inside it, and the Fig.5 machine document
carries a nested raster crop of its own dimension table; the two landing photographs on
page 18 sit inside the Figure 18 grid. Each of those is a fragment of the exhibit that
measures them, so the vector region is the exhibit and the inner copy is excluded.

Four of the eighteen figures are tables in disguise (Figures 3, 11, 13, 18) and are recorded
as table-as-figure with their grid read off the crop, because the table block only exists
for printed tables.

Usage: python -I tools/_dist_paper14.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2011-11199-cfe6d809"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
REG = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: x["bbox"][1]), 1):
        REG[(pg["page"], i)] = r["bbox"]

PAGE_W, PAGE_H = 612.0, 792.0

ORDER = [
    (2, 1), (2, 2), (3, 1), (3, 3), (3, 2), (3, 4),
    (5, 1), (6, 1),
    (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
    (10, 1),
    (11, 1), (11, 2),
    (12, 1), (12, 2),
    (13, 1),
    (14, 1), (14, 2),
    (15, 1),
    (18, 1), (18, 2), (18, 3),
    (21, 1),
]

S_INTRO = "未编号标题：I. Introduction"
S_CURR = "未编号标题：I.2 Current Half-Pipe Engineering & Dimensions"
S_M12 = "未编号标题：Vertical Air Model 1.2 – No Friction (Fixed Height & Fixed Width)"
S_FRIC = "未编号标题：II.2 Models with Friction"
S_M23 = "未编号标题：Vertical Air Model 2.3 – “Flat Oval” (Friction Included)"
S_RES = ("未编号标题：II.3 Results & Comparison of Models Including Friction "
         "(Models 2.1 – 2.3)")
S_LIM = ("未编号标题：II.4 Considerations & Limitations of Models Including Friction "
         "(Models 2.1 – 2.3)")
S_PUMP = "未编号标题：Rotational Model 2 – (Pumping)"


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


def place(page: int, idx: int, path: str, kind: str) -> dict:
    b = REG[(page, idx)]
    mid = (b[1] + b[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": [path],
        "section_numbered": False,
        "section_kind": kind,
        "doc_order": ORDER.index((page, idx)) + 1,
        "page_order": same.index((page, idx)) + 1,
        "page_zone": z,
        "area_frac": round((b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H), 3),
        "solo_page": False,
    }


def caption(v: str, *, position: str = "below", units: bool = False, vars_: int = 0,
            cond: bool = False, concl: bool = False, voice: str = "none") -> dict:
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


def panel_plot(page: int, idx: int, num: int, first: int, cap: dict, lead: str,
               *, path: str, kind: str, note: str) -> dict:
    return figure(
        page, idx, "line", cap,
        mention(page, first=first, style=[f"Figure {num}"], count=1, lead=lead,
                pattern="as-shown-in"),
        path=path, kind=kind, panels=4, layout="2x2", note=note)


ITEMS = [
    figure(2, 1, "bar",
           caption("Figure 1: Average Viewer Hours per Day of Competition, Turin 2006 "
                   "Olympic Winter Gamesiv"),
           mention(2, first=2, style=["Figure 1"], count=1,
                   lead=span(2, "At the Turin 2006 Olympic Winter Games",
                             "(Figure 1)."),
                   pattern="parenthetical"),
           path=S_INTRO, kind="introduction", legend="below",
           note="stacked columns, one per sport, two series (blue average prime-time hours "
                "over yellow average non-prime-time hours), keyed in a box across the foot "
                "of the plot; y axis 0-160,000,000 in comma-grouped numerals, sport names "
                "rotated under the category axis, no axis titles"),

    figure(2, 2, "flowchart-or-schematic",
           caption("Figure 2: Components of a Half-Pipe (Not to Scale)v"),
           mention(2, first=2, style=["Figure 2"], count=1,
                   lead=span(2, "To understand half-pipe engineering dimensions",
                             "(Figure 2)."),
                   trail=span(2, "The “deck” can only be used", "paltry scores"),
                   pattern="parenthetical", read=1),
           path=S_CURR, kind="other", printed=False, labels=True,
           note="one cross-section profile plus dashed construction curves, with the part "
                "names written inside the drawing (DECK, COPING, VERT, TRANSITION, FLAT "
                "BOTTOM) and dimension arrows instead of ticks"),

    figure(3, 1, "table-as-figure",
           caption("Figure 3: Half-Pipe Dimensions for 1998, 2002, 2006, and 2010 Winter "
                   "Olympic Gamesvi,vii,viii,ix"),
           mention(3, first=3, style=["Figure 3"], count=2,
                   lead=span(3, "in each of the last four Olympics", "(Figure 3)."),
                   trail=span(3, "a general trend has been an increase", "coping"),
                   pattern="parenthetical", read=1),
           path=S_CURR, kind="other", labels=True,
           note="six columns (Year, Host City, Length (m), Gradient (deg), Width (m), Inner "
                "Wall Height (m)) and four data rows; three header rows including a merged "
                "Olympic Event band over the two stub columns and an Approximate Course "
                "Specifications band over the four numeric columns, with Average and Inner "
                "Wall printed as a middle band over their own columns, so merged cells are "
                "present; header cells filled navy with white type, body rows ruled "
                "horizontally with one vertical group divider, no zebra shading; the three "
                "units sit in the header, and n/a fills the two unknown cells"),

    figure(3, 3, "photo-or-raster-image",
           caption("Figure 4: ‘Super Pipe’ Snow-Carving Machinex"),
           mention(3, first=3, style=["Figure 4"], count=1,
                   lead=span(3, "The most popular courses recently", "(Figure 4)."),
                   pattern="parenthetical"),
           path=S_CURR, kind="other", printed=False, labels=True,
           note="photograph of a pipe wall with a coloured cutting path overlaid "
                "(blue-to-red-to-yellow over four labelled segments) and the machine's "
                "profile names written beside it (Quarter Pipe Extension, New 22 Foot "
                "Monster, 18 Foot Monster, Base, 22 Ft., 18 Ft.)"),

    figure(3, 2, "flowchart-or-schematic",
           caption("Figure 5: Recommended Half-Pipe Dimensions, Zaugg AG & International "
                   "Ski Federationxi"),
           mention(3, first=3, style=["Figure 5"], count=2,
                   lead=span(3, "has published a document outlining", "(Figure 5)."),
                   trail=span(3, "It is clear from the above Figure 5",
                              "interesting one"),
                   pattern="parenthetical", read=1),
           path=S_CURR, kind="other", printed=False, labels=True,
           note="the machine maker's drawing page reproduced as one vector object: three "
                "panels (perspective pipe, cross-section, drop-in ramps) with brown hatched "
                "ground and numbered callouts 1-10 keyed to a dimension list; the raster "
                "crop of that list inside the same region is excluded as a fragment"),

    figure(5, 1, "line",
           caption("Figure 6: Three Sample Candidate Profiles for Half-Pipe with Fixed "
                   "Height and Widthxiii"),
           mention(5, first=5, style=["Figure 6"], count=1,
                   lead=span(5, "Three possible profiles for such a half-pipe",
                             "in Figure 6."),
                   trail=span(5, "This profile would be dangerous", "at the corners"),
                   pattern="as-shown-in", read=1),
           path=S_M12, kind="model", printed=False, labels=True,
           note="three candidate cross-sections drawn in one frame — one solid curve and two "
                "straight-chord profiles — with dashed chords and the dimension letters h, l, "
                "x, y written in the drawing; no axes and no numeric ticks"),

    figure(6, 1, "flowchart-or-schematic",
           caption("Figure 7: Construction of a Cycloidxiv"),
           mention(6, first=6, style=["Figure 7"], count=1,
                   lead=span(6, "the curve traced by a red dot", "(Figure 7)."),
                   pattern="parenthetical"),
           path=S_M12, kind="model", printed=False,
           note="geometric construction: overlapping light guide circles with radial spokes, "
                "the traced cycloid drawn heavy, and the generating point marked; the "
                "labels the authors describe in the text are not printed in the drawing"),

    figure(7, 1, "flowchart-or-schematic",
           caption("Figure 8: Free-Body Diagram of Snowboarder at a Particular Angle, , "
                   "Relative to the Horizontal Axis"),
           mention(7, first=7, style=["Figure 8"], count=1,
                   lead=span(7, "We use the following free-body diagram",
                             "(Figure 8)."),
                   pattern="parenthetical"),
           path=S_FRIC, kind="model", printed=False, labels=True,
           note="inclined plane with the rider drawn as a box, force arrows labelled Normal "
                "Force F_N, Frictional Force F_f and Gravitational Force F_g = mg, the "
                "dashed decomposition into mgsin(theta) = F_gy and mgcos(theta) = F_gx, the "
                "angle theta, a velocity arrow, and x+ / y+ axis markers; six rasterised "
                "label strips stacked inside the same region are excluded as fragments"),

    figure(10, 1, "flowchart-or-schematic",
           caption("Figure 9: Illustrative “Flat Oval” Shape"),
           mention(10, first=10, style=["Figure 9"], count=1,
                   lead=span(10, "is used to connect two small quarter circles",
                             "(Figure 9)."),
                   pattern="parenthetical"),
           path=S_M23, kind="model", printed=False, labels=True,
           note="cross-section drawing of the flat-oval profile: quarter circles joined by a "
                "horizontal line, labelled only with the letters w, b, r; no axes"),

    panel_plot(11, 1, 10, 10,
               caption("Figure 10: Speed vs. Arc Length Travelled on Four Sample Curves "
                       "(Fixed Width & “Entry Speed”)", cond=True),
               span(10, "The plots of speed as a function of arc length", "Figure 10."),
               path=S_RES, kind="result",
               note="four panels in a 2x2 grid, one curve each (black, red, green, blue), "
                    "each panel its own speed (m/s) against arc length travelled (m) axes "
                    "with printed ticks, no legend and no shared axis"),

    figure(11, 2, "table-as-figure",
           caption("Figure 11: Resultant Sample Curve Statistics for Four Sample Curves "
                   "(Fixed Width & “Entry Speed”)", cond=True),
           mention(11, first=11, style=["Figure 11"], count=1,
                   lead=span(11, "which outlines the final speed", "(Figure 11)."),
                   trail=span(11, "Models 2.1 and 2.3", "higher exit speeds"),
                   pattern="parenthetical", read=1),
           path=S_RES, kind="result", labels=True,
           note="four columns (Model, Curve Shape, Exit Speed (m/s), Arc Length (m)) and four "
                "data rows; one navy header row, full box with vertical rules on every "
                "column edge, cream shading down the Model column, units in the header, no "
                "merged cells"),

    panel_plot(12, 1, 12, 11,
               caption("Figure 12: Speed vs. Arc Length Travelled on Four Sample Curves "
                       "(Fixed Arc Length & “Entry Speed”)", cond=True),
               span(11, "Now we repeat the plots as above", "(Figure 12)."),
               path=S_RES, kind="result",
               note="the same 2x2 panel grammar as Figure 10 re-run on the fixed-arc-length "
                    "constraint: one curve per panel, own axes, no legend"),

    figure(12, 2, "table-as-figure",
           caption("Figure 13: Resultant Sample Curve Statistics for Four Sample Curves "
                   "(Fixed Arc Length & “Entry Speed”)", cond=True),
           mention(12, first=12, style=["Figure 13"], count=1,
                   lead=span(12, "as well as the width", "(Figure 13)."),
                   pattern="parenthetical"),
           path=S_RES, kind="result", labels=True,
           note="twin of Figure 11 with the last column changed from Arc Length (m) to Course "
                "Width (m): four columns, navy header row, full box with vertical rules, "
                "cream Model column, units in the header"),

    figure(13, 1, "scatter",
           caption("Figure 14: Speed vs. Width of 200 Sample Curves (Fixed “Entry Speed”)",
                   cond=True),
           mention(13, first=12, style=["Figure 14"], count=2,
                   lead=span(12, "how the four different sample curves", "(Figure 14)."),
                   trail=span(13, "we feel confident about drawing conclusions", "Figure 14"),
                   pattern="parenthetical", read=2),
           path=S_RES, kind="result",
           note="point cloud of 200 simulated curves printed as four colour groups (green "
                "long flat ovals, blue short flat ovals, black semicircles, cycloids) with "
                "no legend box — the colours are decoded in the following sentence — and the "
                "scatter stays in one frame rather than four panels"),

    figure(14, 1, "line",
           caption("Figure 15: Kinetic Energy upon Exiting Cross-Section of Long Oval Shape "
                   "(Model 2.3) vs. ( / )"),
           mention(14, first=14, style=["Figure 15"], count=1,
                   lead=span(14, "for varying values of", "(Figure 15)."),
                   trail=span(14, "It is clear from the above graph",
                              "the connecting horizontal line"),
                   pattern="parenthetical", read=1),
           path=S_RES, kind="result",
           note="single black curve with open circle markers, kinetic energy at exit 126-136 "
                "against the base length as a percentage of width 0.2-0.8, in-plot title "
                "Efficiency of different types of oval half pipes instead of a legend"),

    figure(14, 2, "line",
           caption("Figure 16: Kinetic Energy upon Exiting Course Cross-Section of Long Oval "
                   "Shape (Model 2.3) vs."),
           mention(14, first=14, style=["Figure 16"], count=1,
                   lead=span(14, "If we re-plot the data", "Figure 16"),
                   pattern="parenthetical"),
           path=S_RES, kind="result",
           note="the same single-series panel re-plotted against total arc length 20-26, "
                "same open circle markers and same in-plot title; the caption is cut off at "
                "vs. because the re-plotted variable is a symbol the text layer does not "
                "carry"),

    figure(15, 1, "line",
           caption("Figure 17: Kinetic Energy upon Exiting Course Cross-Section of all Four "
                   "Sample Curves vs. (Fixed )", cond=True),
           mention(15, first=15, style=["Figure 17"], count=1,
                   lead=span(15, "The following graph shows what the effects",
                             "coefficient of friction"),
                   pattern="parenthetical"),
           path=S_LIM, kind="sensitivity",
           note="four curves swept over the coefficient of friction 0.05-0.20 against kinetic "
                "energy at exit 0-140, colours keyed by position in the figure order rather "
                "than a legend, the steepest curve leaving the frame past 0.13"),

    figure(18, 1, "table-as-figure",
           caption("Figure 18: Illustrative Empirical Evidence that Landing Further Inside "
                   "Half-Pipe Allows for more Rotation (and thus a Higher Score/Performance "
                   "Ranking), Vancouver 2010 Winter Olympic Games", concl=True),
           mention(18, first=18, style=["Figure 18"], count=1,
                   lead=span(18, "we see empirically that this theoretical posit",
                             "(Figure 18)."),
                   pattern="parenthetical"),
           path=S_PUMP, kind="test", labels=True,
           note="comparison grid: three columns (Athlete Name then one per rider) against "
                "five body rows (Picture of Landing, Country of Representation, Trick "
                "Performed, Overall Score, Overall Final Olympic Standings); header row "
                "bold with a rule under it, full box with vertical column rules, no zebra "
                "and no merged cells, with two photographs pasted into the landing row that "
                "are measured as separate regions and excluded as fragments"),
]

RULES = [
    "本题型的图跟着论证走：三张背景图（收视、构件、历届尺寸）开篇，"
    "随后每推进一步模型就配一张剖面图或受力图，结果章再成对出现「四联图 + 汇总表」"
    "[place.section_kind]，[geometry.family]。",
    "结果图一律四联 2x2 面板、每面板一条曲线，四条曲线靠颜色区分而面板各自独立坐标轴 "
    "[geometry.panel_count]，[geometry.panel_layout]，[geometry.shared_axes]。",
    "全文图内不设图例框：颜色含义写在紧随其后的正文句里，或改用图内标题"
    "（Efficiency of different types of oval half pipes）[geometry.legend]，"
    "[mention.trail_sentence]。",
    "四张「图」其实是表（Figure 3、11、13、18），与图共用一套编号与题注，表体通栏"
    "排在正文之间而不另起一页 [caption.numbering]，[place.solo_page]。",
    "表格化图形的表头是分层合并的：Figure 3 用 Olympic Event、Approximate Course "
    "Specifications 两条横跨表头压住列名；单位一律写在表头，所以题注仍保持 8-20 词的"
    "短语长度、不重复单位 [caption.words]，[caption.units]。",
    "题注一律在图下、编号后带冒号，长度 8-20 词，把「固定了什么条件」写进括号 "
    "（Fixed Width & “Entry Speed”）[caption.position]，[caption.conditions]，"
    "[caption.words]。",
    "正文引出以括号回指为主（(Figure N) 直接挂在句末），少数用 are outlined in / given by / "
    "can be seen in 的顺叙句 [mention.lead_pattern]，[mention.count]。",
    "图前一句话先交代「要画什么」，图后一句话立刻解读趋势并给结论，读图句数多为 1-2 句 "
    "[mention.lead_sentence]，[mention.read_sentences]。",
    "曲线图不画数据标签、只印坐标轴刻度；示意图与剖面图则相反——不印任何数字、"
    "把所有标注写成文字塞进图里 [geometry.printed_numbers]，[geometry.data_labels]。",
    "剖面与受力图用细黑线加实心箭头，靠字母标号（h、l、x、y、w、b、r、theta）而非数值"
    "表达几何关系 [geometry.printed_numbers]，[geometry.family]。",
    "没有三维图、没有色标，全部二维平面绘制 [geometry.three_d]，[geometry.colorbar]。",
    "同一张图的分层元素会被版面测量拆成多条区域（Figure 8 的文字层、Figure 5 的画中表格、"
    "Figure 18 的落点照片），正文一律以矢量主区为展品、内嵌切片作废 "
    "[place.area_frac]，[place.doc_order]。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": [],
    "excluded_regions": [
        {"page": 3, "bbox": REG[(3, 4)], "reason": "fragment-of-other",
         "note": "nested raster crop of the dimension list inside the Figure 5 drawing"},
        {"page": 7, "bbox": REG[(7, 2)], "reason": "fragment-of-other",
         "note": "rasterised label strip inside the Figure 8 free-body diagram"},
        {"page": 7, "bbox": REG[(7, 3)], "reason": "fragment-of-other",
         "note": "rasterised label strip inside the Figure 8 free-body diagram"},
        {"page": 7, "bbox": REG[(7, 4)], "reason": "fragment-of-other",
         "note": "rasterised label strip inside the Figure 8 free-body diagram"},
        {"page": 7, "bbox": REG[(7, 5)], "reason": "fragment-of-other",
         "note": "rasterised label strip inside the Figure 8 free-body diagram"},
        {"page": 7, "bbox": REG[(7, 6)], "reason": "fragment-of-other",
         "note": "rasterised label strip inside the Figure 8 free-body diagram"},
        {"page": 7, "bbox": REG[(7, 7)], "reason": "fragment-of-other",
         "note": "rasterised label strip inside the Figure 8 free-body diagram"},
        {"page": 18, "bbox": REG[(18, 2)], "reason": "fragment-of-other",
         "note": "landing photograph pasted into the Figure 18 grid"},
        {"page": 18, "bbox": REG[(18, 3)], "reason": "fragment-of-other",
         "note": "landing photograph pasted into the Figure 18 grid"},
        {"page": 21, "bbox": REG[(21, 1)], "reason": "rule",
         "note": "double horizontal rule under the running head, no exhibit content"},
    ],
    "note": "Section headings are roman-numbered (I., I.2, II.2, II.3, II.4, Vertical Air "
            "Model 1.2/2.3, Rotational Model 2) but the heading index only caught one false "
            "positive (18 Foot Monster, from a label inside the Figure 4 drawing), so every "
            "section_path uses the 未编号标题 form with the numeral copied from the text "
            "layer. Four figures are tables (3, 11, 13, 18): the grid is read off the crop "
            "and stated in the note because the table block is reserved for printed tables.",
    "rules": RULES,
}

out = PROXY / f"{PID}-payload14.json"
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print(f"{len(ITEMS)} items, 0 tables -> {out.name}")
