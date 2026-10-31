"""Hand pass for P-B-2017-70174-8bf62421 (NetLogo toll-plaza agent model, 11 figures, no tables).

Shape of the paper: Figure 1 is the pseudo-code flowchart that opens the model chapter;
Figure 2 prints the three merge-lane patterns as three side-by-side NetLogo world frames;
Figure 3 prints the three road sizes the same way; Figure 4 is a table rendered as a
picture (satisfaction ratings); Figure 5 is a screenshot of the BehaviorSpace dialog;
Figures 6-10 are five NetLogo plot exports (three series each, legend outside right);
Figure 11 is a screenshot of the model interface.

Three things this paper does that the record has to say out loud:

1. No exhibit is ever cited by its number. The prose says "shown below", "the above figure",
   "the figure" or nothing at all, so `mention.style` is empty and `lead_pattern` is none
   except where a sentence literally ends in "shown below" / "can be seen below".
   Figures 7 and 11 carry no lead sentence at all and record `first_page: null`.
2. Figures 2 and 3 are three separate measured regions under one caption. Each panel is its
   own item with `panel_count` 1 and shares the caption, the way the paper 121 pass recorded
   its two-panel Figure 1.
3. Figure 4 is a table drawn as a raster image (two columns, alternating row shading), not a
   chart, so it is `table-as-figure`, and the shading - not a bold font - is what the text
   calls "the bold areas in the above figure".

Usage: python -I tools/_dist_paper123.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2017-70174-8bf62421"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    # sort by (top, left): the three panels of Figures 2 and 3 share one y, so the top
    # coordinate alone leaves their order to the file and the left edge alone would
    # reverse two stacked plots on one page.
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

ORDER = [
    (7, 1),
    # reading order, not file order: the three Figure 2 frames sit on three slightly
    # different baselines, so sorting by top coordinate alone puts the right panel first.
    (11, 2), (11, 3), (11, 1),
    (12, 1), (12, 2), (12, 3), (12, 4),
    (13, 1),
    (14, 1), (14, 2),
    (15, 1), (15, 2),
    (16, 1), (16, 2),
]

S4 = "4 Toll Booth Plaza Model"
S42 = "4.2 NetLogo Model"
S5 = "5 Model Analysis"
S52 = "5.2 An Example Comparison: Roads of 3 Sizes"
S53 = "5.3 Data Collection"
S6 = "6 Sensitivity Analysis"
S61 = "6.1 Sensitivity with Respect to Patience"
# Figures 8 and 9 are printed on p15 ABOVE the 6.3 heading that also lands on p15, so the
# context dump attaches them to 6.3; they belong to 6.2, whose nine-word title the heading
# pass now keeps. The section_path says 6.2, the note explains the disagreement.
S62 = "6.2 Sensitivity with Respect to Number of Self Driving Cars"
S63 = "6.3 Sensitivity to Number of Cars in the System"
S7 = "7 Strengths and Weaknesses"


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


def caption(v: str, *, numbering: str = "Figure N:", cond: bool = False,
            concl: bool = False, units: bool = False, vars_: int = 0,
            pos: str = "below", voice: str = "none") -> dict:
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
        "position": pos,
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
           printed: bool = False, labels: bool = False, panels: int = 1,
           layout: str = "1", shared: bool = False, note: str = "",
           other_note: str = "", confidence: str = "high", panel_of: int = 0) -> dict:
    item = {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": confidence,
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
    if other_note:
        item["other_note"] = other_note
    if panel_of:
        # this region is a panel of the exhibit whose item number is panel_of, so the shared
        # caption is a copy of the first panel's line and not a second printing of it
        item["is_panel_of"] = panel_of
    return item


CAP2 = "Figure 2: Three Merge Lane Patterns: 1. Symmetric, 2. Merge Up, 3. Merge Down"
CAP3 = ("Figure 3: Road Size Comparison: 1. 3 lane, 4 booths with symmetric fanning "
        "2. 4 lane, 6 booths with symmetric fanning 3. 6 lanes, 9 booths with symmetric fanning")
CAP8 = ("Figure 8: Accumulated Cars that have rejoined normal traffic vs. ticks for a six "
        "lane in, 9 toll booth symmetric layout")
CAP9 = ("Figure 9: Accumulated Cars that have rejoined normal traffic vs. ticks for a three "
        "lane in, four toll booth symmetric layout")

NETLOGO = ("top-down NetLogo world frame: green ground, grey lane bands separated by dashed "
           "white lines, red hatching along the road edges, blue car glyphs, a yellow/red/green "
           "striped booth column near the left third; no axis, no scale, no lettering")

ITEMS = [
    figure(7, 1, "flowchart-or-schematic",
           caption("Figure 1: Pseudo-Code for the toll plaza model"),
           mention(7, first=6, style=[], count=0, pattern="as-shown-in",
                   lead=span(6, "a pseudo-code flow chart", "provided below")),
           path=[S4, S42], kind="model",
           note="hexagon START and STOP-at-500-ticks terminals, rounded rectangles for the "
                "procedures, blue hexagons for the three decisions, pink circles for the YES "
                "and NO branches, two orange side tabs labelled SETUP Procedure and GO "
                "Procedure, and a green TICK triangle on the return edge"),

    figure(11, 1, "map-or-plan-view",
           caption(CAP2),
           mention(11, first=11, style=[], count=0,
                   lead=span(11, "The three merging strip patterns", "were:")),
           path=[S5, S52], kind="model",
           note=NETLOGO + "; right panel of the three, the caption's pattern 3 Merge Down: "
                "the top edge steps down five times while the bottom edge stays straight"),

    figure(11, 2, "map-or-plan-view",
           caption(CAP2),
           mention(11, first=11, style=[], count=0,
                   lead=span(11, "The three merging strip patterns", "were:")),
           path=[S5, S52], kind="model", panel_of=2,
           note=NETLOGO + "; left panel of the three, the caption's pattern 1 Symmetric: the "
                "funnel closes in equal steps from the top and from the bottom"),

    figure(11, 3, "map-or-plan-view",
           caption(CAP2),
           mention(11, first=11, style=[], count=0,
                   lead=span(11, "The three merging strip patterns", "were:")),
           path=[S5, S52], kind="model", panel_of=2,
           note=NETLOGO + "; middle panel of the three, the caption's pattern 2 Merge Up: the "
                "bottom edge steps up five times while the top edge stays straight"),

    figure(12, 1, "map-or-plan-view",
           caption(CAP3),
           mention(12, first=11, style=[], count=0,
                   lead=span(11, "The following lane comparison", "analysis:")),
           path=[S5, S52], kind="model",
           note=NETLOGO + "; left panel, the caption's size 1 (3 lane, 4 booths); the lane "
                "bands are the widest of the three panels because the funnels are longest"),

    figure(12, 2, "map-or-plan-view",
           caption(CAP3),
           mention(12, first=11, style=[], count=0,
                   lead=span(11, "The following lane comparison", "analysis:")),
           path=[S5, S52], kind="model", panel_of=5,
           note=NETLOGO + "; middle panel, the caption's size 2 (4 lane, 6 booths)"),

    figure(12, 3, "map-or-plan-view",
           caption(CAP3),
           mention(12, first=11, style=[], count=0,
                   lead=span(11, "The following lane comparison", "analysis:")),
           path=[S5, S52], kind="model", panel_of=5,
           note=NETLOGO + "; right panel, the caption's size 3 (6 lanes, 9 booths); the "
                "densest of the three frames"),

    figure(12, 4, "table-as-figure",
           caption("Figure 4: Comparison Satisfaction Ratings for 3 Highways of Different "
                   "Sizes: highways of different sizes are compared with symmetric merging, "
                   "upward merging, and downward merging. In each case, symmetric merging is "
                   "the most satisfactory.",
                   concl=True, voice="passive"),
           mention(12, first=12, style=[], count=0, read=1,
                   lead=span(12, "We then combined the scores", "lane design"),
                   trail=span(12, "As shown by the bold areas", "regardless of road size")),
           path=[S5, S52], kind="model", printed=True,
           note="a table printed as a picture, not a chart: header row Lane Design / "
                "Satisfaction Rating, then three row groups (3 Lanes 4 Booths, 4 Lanes 6 "
                "Booths, 6 Lanes 9 Booths) each with symmetric / Merge Up / Merge Down; the "
                "symmetric row of every group is filled darker blue, which is what the prose "
                "calls the bold areas; nine numeric cells to nine decimals, alternating light "
                "shading on the values, no rules, no axis"),

    figure(13, 1, "other",
           caption("Figure 5: Behavior Space set up for experiment run"),
           mention(13, first=13, style=[], count=0, pattern="as-shown-in", read=1,
                   lead=span(13, "An image of the Behavior Space terminal", "shown below"),
                   trail=span(13, "One can see that this allows us", "at every tick")),
           path=[S5, S53], kind="other",
           other_note="screenshot of a NetLogo BehaviorSpace dialog window, not a chart and "
                      "not a plan view: fields for the varying sliders, a reporters pane and "
                      "the OK/Cancel buttons",
           note="titled Experiment, experiment name 3 lane 4 booth, vary pane listing the "
                "slider ranges, measure pane listing seven reporters, repetitions 1, time "
                "limit 500; the numbers are GUI values, not plotted data"),

    figure(14, 1, "line",
           caption("Figure 6: Merges vs. Tick for a three lane in 4 toll booth symmetric layout"),
           mention(14, first=13, style=[], count=0, read=1,
                   lead=span(13, "To test its affect on the system", "against time"),
                   trail=span(14, "it can be seen that the model is rather sensitive",
                              "the patience rises")),
           path=[S6, S61], kind="sensitivity", legend="outside-right", printed=True,
           note="NetLogo plot export, three jagged rising series (orange, blue, grey) with no "
                "markers; plot title Accumulated Merges vs. Time, y 0-500 by 50, x Ticks "
                "Elapsed 0-480 by 32; horizontal gridlines only, left and bottom axes drawn "
                "without a top or right rule; key at the right outside the plot"),

    figure(14, 2, "line",
           caption("Figure 7: Merges vs. Tick for a six lane in 9 toll booth symmetric layout"),
           mention(14, first=None, style=[], count=0, read=1,
                   trail=span(14, "The data from a higher lane simulation", "corroborates")),
           path=[S6, S61], kind="sensitivity", legend="outside-right", printed=True,
           note="same plot export as Figure 6 with a tenfold y range (0-10000 by 1000); the "
                "prose never introduces it, the caption alone carries it"),

    figure(15, 1, "line",
           caption(CAP8),
           mention(15, first=14, style=[], count=0, read=1,
                   lead=span(14, "An initial sweep was done",
                             "nine toll layout with a medium traffic level"),
                   trail=span(15, "As can be seen from the figure",
                              "throughput of the system")),
           path=[S6, S62], kind="sensitivity", legend="outside-right", printed=True,
           note="three near-identical curves that lie flat on zero until about tick 190 and "
                "then rise; y 0-350 by 50, x 0-480 by 32; legend outside right with the three "
                "self-driving shares. Printed on p15 above the 6.3 heading that also sits on "
                "that page, so the context dump files it under 6.3; section_path follows the "
                "printed order and says 6.2"),

    figure(15, 2, "line",
           caption(CAP9),
           mention(15, first=15, style=[], count=0, pattern="as-shown-in", read=1,
                   lead=span(15, "This same experiment was run",
                             "symmetric layout with medium traffic as well"),
                   trail=span(15, "We see the same pattern emerge once more",
                              "negligible on the system")),
           path=[S6, S62], kind="sensitivity", legend="outside-right", printed=True,
           note="the same three curves on the small layout, y 0-140 by 20, x 0-480 by 32, "
                "rougher than Figure 8 but the same flat-then-rise shape. Same p15/6.3 filing "
                "caveat as Figure 8: it is a 6.2 exhibit printed above the 6.3 heading"),

    figure(16, 1, "line",
           caption("Figure 10: Accumulated Efficiency vs. ticks for a four lane in, six booth "
                   "symmetric layout"),
           mention(16, first=15, style=[], count=0, read=1,
                   lead=span(15, "In order to determine the effect of number of cars",
                             "defined for the system"),
                   trail=span(16, "there seems to be a fairly consistent drop off",
                              "number of cars")),
           path=[S6, S63], kind="sensitivity", legend="outside-right", printed=True,
           note="y axis is a ratio, 0-0.8 by 0.1, x 0-476 by 34; the three series separate "
                "downwards in the order low / medium / high number of cars"),

    figure(16, 2, "map-or-plan-view",
           caption("Figure 11: NetLogo Interface"),
           mention(16, first=None, style=[], count=0),
           path=[S7], kind="evaluation", printed=True,
           note="full interface screenshot: left control column with the setup / go once / go "
                "buttons and ten sliders and switches, right world view with the plaza funnel; "
                "the slider values are GUI state, not data. The prose never cites it, it sits "
                "under the Strengths list as evidence that the model has a friendly interface"),
]

RULES = [
    "模型章开篇给流程图：4.2 NetLogo Model 一节点上先放一张 pseudo-code 流程图，[place.section_path] 与 [geometry.family]=flowchart-or-schematic 对上。",
    "对照实验的形状用同一题注下的三联图：Figure 2 三种并道、Figure 3 三种路宽，[place.page_order] 从 1 数到 3 区分左中右，[caption.verbatim] 三块共用一句。",
    "模拟世界截图一律平铺俯视、无坐标轴无图例，[geometry.family]=map-or-plan-view 且 [geometry.printed_numbers]=False。",
    "只有 GUI 截图例外：Figure 5 的 BehaviorSpace 对话框没有俯视图，落在 [geometry.family]=other 并带 other_note。",
    "数据图统一是 NetLogo 导出的折线，三条序列、无数据点标记，[geometry.family]=line 且 [geometry.data_labels]=False。",
    "折线图图例一律在绘图区外右侧，[geometry.legend]=outside-right，五张图无例外。",
    "折线图只画水平网格与左、下两条轴，没有上右边框，[geometry.shared_axes]=False。",
    "灵敏度一节的图按参数分组，每节两图共用一套图例文案，[place.section_kind]=sensitivity。",
    "正文从不按编号引用图：全篇 [mention.style] 为空列表，[mention.count]=0，引用一律靠 shown below / the above figure / the figure 这类指示语。",
    "first_page 只跟引出句：Figure 7 与 Figure 11 没有引出句，[mention.first_page]=None，即便 Figure 7 题注后面紧跟一句解读也不回填该字段。",
    "图与引出句可以跨页：Figure 1 的引出句在 p6、图在 p7，[mention.lead_pages]=1；Figure 8 与 Figure 10 同样为 1。",
    "表以图片形式印刷时记 table-as-figure 而不是 table-grid：Figure 4 是两列表格截图，[geometry.printed_numbers]=True 表示数值是印在图里的。",
    "题注统一 Figure N: 冒号式并印在图下方，[caption.position]=below，[caption.numbering]=Figure N:。",
    "题注里只有 Figure 4 下结论并给出一句比较，[caption.concludes]=True，其余题注只命名不给结论。",
    "图是按印刷顺序归章的，不是按页：Figure 8 与 Figure 9 印在 p15 的 6.3 标题之上，[place.section_path] 记 6.2，而抽取器按页归属成 6.3，note 里写明这处分歧。",
    "占版面的份额靠内容分类而非图型：三联图的单块只有 [place.area_frac]=0.015，单张折线图约 0.067。",
]

payload = {"paper": PID, "layout_sha256": LAYOUT["layout_sha256"],
           "items": ITEMS, "tables": [],
           "excluded_regions": [], "rules": RULES,
           "note": "hand pass, 15 measured regions -> 11 figures, 0 tables; no exhibit is "
                   "cited by number in the prose; re-recorded after the heading pass kept the "
                   "nine-word title, so Figures 8 and 9 now sit under 6.2"}

out = PROXY / f"{PID}-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"wrote {out} items={len(ITEMS)} tables=0 rules={len(RULES)}")
