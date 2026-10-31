"""Hand pass for P-B-2017-70545-8e86fcfa (toll-plaza merging geometry, 12 figures, 3 tables).

Shape of the paper: the model chapter draws the plaza itself over and over, once per claim.
Figures 1-2 are the two "open" cases (two booths, three booths), Figure 3 the two/three egress
lanes merging into one, Figures 4-6 the dimensioned plaza with 8 booths into 3 lanes (Figure 6
adds heavy traffic), Figure 9 the symmetric-gore area estimate, Figure 12 the final shape.
Figure 11 is the only plotted exhibit set: three vector sensitivity panels side by side.
Tables 1-2 report statistics; the paper's third table, the notation glossary in section 3,
carries no caption at all.

What the record has to say out loud:

1. Six measured regions are wrappers, not exhibits: on pages 8, 9, 10, 15 and 19 a vector box
   encloses the surrounding prose plus the caption plus the drawing, and the drawing is
   measured again as a raster inside it. The wrapper is excluded as `duplicate` and the inner
   raster is the item, so the drawing is counted once.
2. Figure 6 is drawn twice on page 10, 24.8 pt apart (y 320.26 and y 320.26 with different
   x extents, one clipped at the right margin). The prose cites it once; the second copy is
   excluded as `duplicate`.
3. The throughput comparison on p12 is a box plot, not the bar chart the extracted text
   suggests: three notched boxes with whiskers and outlier crosses. Family by crop, not by
   prose. Figure 10 prints two panels with independent y scales (one spans -2.0 to 0.0, the
   other 0.10 to -0.10), so the pair carries no shared axis.

Usage: python -I tools/_dist_paper124.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2017-70545-8e86fcfa"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    # sort by (top, left): Figures 1 and 2 share one caption line and sit on two different
    # baselines, so the top coordinate alone would put the right-hand drawing first; the
    # three Figure 11 panels share one baseline and are ordered by their left edge.
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

# document order of every measured region, wrappers included, so doc_order and page_order
# count what a reader turns past rather than what survived as an exhibit.
ORDER = [
    (5, 1),
    (7, 1), (7, 2), (7, 3), (7, 4),
    (8, 1), (8, 2),
    (9, 1), (9, 2),
    (10, 1), (10, 2), (10, 3),
    (12, 1),
    (13, 1),
    (14, 1),
    (15, 1), (15, 2), (15, 3),
    (17, 1), (17, 2),
    (18, 3), (18, 2), (18, 1),
    (19, 1), (19, 2),
]

S3 = "3 Notations"
S4 = "4 Models"
S42 = "4.2 Control Time Model (CTM)"
S43 = "4.3 Waiting Area Model(WAM)"
S5 = "5 Analysis and Results"
S51 = "5.1 Throughput"
S511 = "5.1.1 Throughput of existing model"
S514 = "5.1.4 Comparison and hypothesis tests of throughputs"
S52 = "5.2 Accident prevention"
S53 = "5.3 Cost"
S7 = "7 Sensitivity test"
S71 = "7.1 Sensitivity test of throughput"
S72 = "7.2 Sensitivity test of fixed cost"
S8 = "8 Conclusion"


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
            pos: str = "below", voice: str = "none", sentences: int | None = None) -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)) if sentences is None else sentences,
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
           other_note: str = "", confidence: str = "high",
           src: str = "text-layer") -> dict:
    item = {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": confidence,
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": src,
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
    return item


def table(page: int, idx: int, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer" if cap["verbatim"] else "none",
        "note": note,
        "place": place(page, idx, path, kind),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed", zebra: bool = False,
         merged: bool = False, diag: bool = False, units_hdr: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "full",
         orient: str = "portrait", continued: bool = False, note: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rules,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diag,
        "units_in_header": units_hdr,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": orient,
        "continued": continued,
        "note_sentence": note,
    }


CAP1 = "Figure 1: Either A or B is open"
CAP2 = "Figure 2: Either C, D or E is open"
CAP3 = "Figure 3: Two or three tollbooth egress lanes merge into one lane"
CAP4 = "Figure 4: B = 8 tollbooth egress lanes merge into L = 3 lanes"
CAP5 = "Figure 5: B = 8 tollbooth egress lanes merge into L = 3 lanes"
CAP6 = "Figure 6: B = 8 tollbooth egress lanes merge intoL = 3 lanes in heavy traffic"
CAP7 = "Figure 7: Comparison of throughput of models"
CAP8 = "Figure 8: P ET of existing model and P ET of control time model"
CAP9 = "Figure 9: Estimation of A by symmetry of shaded area"
CAP10 = ("Figure 10: Sensitivity of throughput in terms of mean and standard deviation of "
         "service time.")
CAP11 = ("Figure 11: Sensitivity of fixed cost in terms of vm , r and B always above 1, and "
         "the decreasing speed is very low, which means that D is always sensitive in terms "
         "of B.")
CAP12 = "Figure 12: Shape and merging pattern of merging area"

PLAZA = ("plan view of the toll plaza: a column of booth cells at the left, a dB dimension "
         "arrow over the booth column and a dL dimension arrow over the downstream lane, an "
         "arrow labelled Direction of traffic flow pointing right, and a D dimension down the "
         "middle of the merging funnel; no axis, no grid, no legend, no shading")

TWO_BOOTH_LEAD = span(6, "the second vehicle t0 seconds after the first vehicle",
                      "Figure 2")

ITEMS = [
    figure(7, 2, "map-or-plan-view",
           caption(CAP1),
           mention(7, first=6, style=["Figure 1"], count=1, pattern="as-shown-in",
                   lead=TWO_BOOTH_LEAD, read=1,
                   trail=span(7, "In this way, the regulated merging of the vehicles",
                              "would be more efficient")),
           path=[S4, S42], kind="model",
           note="left-hand drawing of the pair, the caption's case A or B: two lane bands "
                "stacked, each holding one boxed TOLLBOOTH rectangle on a dashed gate line "
                "with a right-pointing arrow, and the letters A and B printed just past the "
                "gate; pale green band fill, no dimension labels, no D. The two drawings on "
                "this page share one caption line, which the caption finder extracts as a "
                "single Figure 1 string"),

    figure(7, 1, "map-or-plan-view",
           caption(CAP2),
           mention(7, first=6, style=["Figure 2"], count=1, pattern="as-shown-in",
                   lead=TWO_BOOTH_LEAD, read=1,
                   trail=span(7, "In this way, the regulated merging of the vehicles",
                              "would be more efficient")),
           path=[S4, S42], kind="model",
           note="right-hand drawing of the pair, the caption's case C, D or E: three lane "
                "bands stacked, each holding one boxed TOLLBOOTH rectangle on a dashed gate "
                "stroke with a right-pointing arrow, and the letters C, D, E printed at the "
                "top-right of the three bands; pale blue band fill, height 118 pt against "
                "Figure 1's 93 pt because of the third band"),

    figure(7, 4, "map-or-plan-view",
           caption(CAP3),
           mention(7, first=7, style=[], count=0, read=1,
                   lead=span(7, "They then immediately starts merging",
                             "two consecutive tangent circle arcs")),
           path=[S4, S42], kind="model",
           note="left-hand drawing of the Figure 3 pair: two egress lanes converging into one, "
                "drawn as a single dashed-then-solid curve with one right-pointing arrow; no "
                "booth cells, no letters, no dimension labels"),

    figure(7, 3, "map-or-plan-view",
           caption(CAP3),
           mention(7, first=7, style=[], count=0, read=1,
                   lead=span(7, "They then immediately starts merging",
                             "two consecutive tangent circle arcs")),
           path=[S4, S42], kind="model",
           note="right-hand drawing of the Figure 3 pair: three egress lanes converging into "
                "one, drawn as two S-curves (one dashed entering from the lower left) meeting "
                "a single arrow; no booth cells, no letters. Same caption as the left panel, "
                "one caption line printed under both"),

    figure(8, 2, "map-or-plan-view",
           caption(CAP4, vars_=2),
           mention(8, first=8, style=[], count=0, read=1,
                   lead=span(8, "We call the mapping", "merging pattern")),
           path=[S4, S42], kind="model",
           note=PLAZA + "; eight booth cells into three lanes, the D dimension drawn from the "
                "booth line to the end of the plaza, and a dimension annotation of the "
                "greatest lower bound D under it; the vector wrapper above it carries the "
                "prose and the caption of the same drawing"),

    figure(9, 2, "map-or-plan-view",
           caption(CAP5, vars_=2),
           mention(9, first=9, style=["Figure 5"], count=1, pattern="as-shown-in", read=1,
                   lead=span(9, "whether it is better to build a waiting area",
                             "as shown in Figure 5)"),
                   trail=span(9, "We will test and compare this model",
                              "whether it is efficient or not")),
           path=[S4, S43], kind="model",
           note=PLAZA + "; the only drawing with a box labelled Waiting area, hatched inside "
                "and set beside the booth column, which is exactly what the caption does not "
                "say and the prose does"),

    figure(10, 2, "map-or-plan-view",
           caption(CAP6, vars_=2),
           mention(10, first=10, style=["Figure 6"], count=1, pattern="as-shown-in", read=1,
                   lead=span(10, "merged from two lanes", "cashier work continually"),
                   trail=span(10, "The toll collection service time",
                              "can be seen as a sum of random variables")),
           path=[S5, S51, S511], kind="model",
           note=PLAZA + "; the same plaza as Figures 4 and 5 with vehicle glyphs queued at the "
                "booths and in the funnel. Drawn twice on this page: this copy at x 89.8-472.0 "
                "and a second at x 114.6-496.8, otherwise identical, both under one caption"),

    figure(12, 1, "box-or-violin",
           caption(CAP7),
           mention(12, first=12, style=["Figure 7"], count=2, pattern="as-shown-in", read=1,
                   lead=span(12, "After computer simulation with N = 1000 times",
                             "shown in Figure 7"),
                   trail=span(13, "It can be seen from Figure 7",
                              "di↵er slightly among models")),
           path=[S5, S51, S514], kind="assumption", printed=True,
           note="three notched box plots, one per model, filled red, green and blue with a "
                "black median line, dashed whiskers with caps and x outlier markers; y axis "
                "titled Throughput veh/(h.lane) with ticks 450 to 500 by 10, x ticks the three "
                "model names; no gridlines, a full rectangular frame, no legend and no value "
                "labels. Read as a bar chart from the text layer alone; the crop shows the "
                "notched boxes"),

    figure(14, 1, "histogram",
           caption(CAP8),
           mention(14, first=14, style=["Figure 8"], count=1, pattern="as-shown-in", read=1,
                   lead=span(14, "the P ET of existing model", "shown in Figure 8"),
                   trail=span(14, "a significant part of P ET", "more likely to happen")),
           path=[S5, S52], kind="result", legend="outside-right", printed=True,
           note="two histograms overlaid with alpha transparency, salmon for the control time "
                "model and teal for the existing model, one-unit bins, no outlines; x titled "
                "PET with ticks 0 to 25 by 5, y titled count with 0, 100, 200 labelled and "
                "minor ticks at 50 and 150; legend outside right titled Model; ggplot panel "
                "with both gridlines and no frame lines"),

    figure(15, 3, "map-or-plan-view",
           caption(CAP9),
           mention(15, first=15, style=["Figure 9"], count=1, pattern="as-shown-in", read=1,
                   lead=span(15, "We can estimate area of land (A)", "as shown in Figure 9"),
                   trail=span(15, "Tollbooth construction cost can be divided",
                              "automated tollbooths")),
           path=[S5, S53], kind="result",
           note=PLAZA + "; the gore between the outermost trajectory and the plaza boundary is "
                "filled with blue hatching and mirrored about the lane axis, which is the "
                "symmetry the caption names; the shaded area is A"),

    figure(17, 1, "line",
           caption(CAP10, vars_=2),
           mention(17, first=17, style=[], count=0, pattern="as-shown-in", read=1,
                   lead=span(17, "As shown in 10", "constant 1"),
                   trail=span(17, "The inverse ratio relationship", "with respect to T")),
           path=[S7, S71], kind="test", printed=True,
           note="left panel of the pair: y titled Sensitivity of throughput with ticks -2.0, "
                "-1.0 and 0.0 labelled and two more between them, x 0 to 4, x title Mean of "
                "service time; one thin solid line lying exactly on zero, no markers, no "
                "gridlines, four-sided frame, no legend. The pair does not share a y scale"),

    figure(17, 2, "line",
           caption(CAP10, vars_=2),
           mention(17, first=17, style=[], count=0, pattern="as-shown-in", read=1,
                   lead=span(17, "As shown in 10", "constant 1"),
                   trail=span(17, "due to the law of large number", "sensitivity is zero")),
           path=[S7, S71], kind="test", printed=True,
           note="right panel: y titled Sensitivity of throughput with ticks 0.10, 0.00 and "
                "-0.10 labelled and two more between them, x 0 to 4, x title Standard deviation "
                "of service time; the line again sits on zero. The prose cites the pair as As "
                "shown in 10, a number with no Figure word, so style stays empty"),

    figure(18, 3, "line",
           caption(CAP11, vars_=3),
           mention(18, first=18, style=["Figure 11"], count=1, pattern="as-shown-in", read=1,
                   lead=span(18, "We calculate the sensitivity of the fixed cost",
                             "we get the graph as following"),
                   trail=span(18, "always above 1", "sensitive in terms of B")),
           path=[S7, S72], kind="test",
           note="left panel of three: sensitivity of fixed cost against the number of booths "
                "B, x 3 to 20, y 0.1 to 0.7; printed axis title Sensitivity of Fixed Cost and "
                "the letter B under the axis; no legend, no markers"),

    figure(18, 2, "line",
           caption(CAP11, vars_=3),
           mention(18, first=18, style=["Figure 11"], count=1, pattern="as-shown-in", read=1,
                   lead=span(18, "We calculate the sensitivity of the fixed cost",
                             "we get the graph as following"),
                   trail=span(18, "So the radius only have little",
                              "final result")),
           path=[S7, S72], kind="test",
           note="middle panel: sensitivity against the turning radius r, x 100 to 300, y 0.05 "
                "to 0.20, letter r under the axis; the curve is almost flat, which is why the "
                "prose calls the radius a small influence"),

    figure(18, 1, "line",
           caption(CAP11, vars_=3),
           mention(18, first=18, style=["Figure 11"], count=1, pattern="as-shown-in", read=1,
                   lead=span(18, "We calculate the sensitivity of the fixed cost",
                             "we get the graph as following"),
                   trail=span(18, "which shows that the cost is",
                              "not sensitive to the speed limit")),
           path=[S7, S72], kind="test",
           note="right panel: sensitivity against the speed limit vm, x labelled v with ticks 6 "
                "to 20 (the extractor drops the subscript), y 1.1 to 1.4; the only panel whose "
                "curve stays above 1, which is what the caption's always above 1 refers to"),

    figure(19, 2, "map-or-plan-view",
           caption(CAP12),
           mention(19, first=19, style=[], count=0, read=1,
                   lead=span(19, "Take the example of B = 8, L = 3",
                             "the shape and merging pattern are as follows"),
                   trail=span(19, "Note that in no case will cars",
                              "stated in our control time model")),
           path=[S8], kind="evaluation",
           note=PLAZA + "; the worked example B = 8 into L = 3 redrawn in the conclusion with "
                "the three prescribed trajectories, first exhibit the paper puts inside a "
                "numbered section after the sensitivity chapter"),
]

TABLES = [
    table(5, 1, caption("", numbering="none", sentences=0),
          mention(5, first=5, style=[], count=0),
          grid(12, 3, header=1, rules="boxed", units_hdr=True, txt=3, width="full"),
          path=[S3], kind="symbols",
          note="the notation glossary is the paper's only captionless table: the section "
               "heading 3 Notations is all the label it gets, so caption_verbatim is empty and "
               "caption_source says none. Header row Notation / Definition / Unit, then eleven "
               "symbol rows (L, B, D, dl, db, r, Th, t0, vm, as, ab); the unit column mixes "
               "N/A, m, s and m/s and is a header column rather than a per-cell suffix"),

    table(13, 1, caption("Table 1: Statistics of two models", numbering="Table N:"),
          mention(13, first=13, style=[], count=0, read=1,
                  lead=span(13, "Therefore, we conduct hypothesis test",
                            "5% level of significance"),
                  trail=span(13, "Therefore, H0 is not rejected",
                             "of means of throughputs")),
          grid(4, 5, header=1, rules="boxed", decimal=True, numeric=4, txt=1),
          path=[S5, S51, S514], kind="assumption",
          note="header Model / Size / Mean / S.d. / SEM, then one row per model (existing, "
               "control time, waiting area), each size 1000; means, standard deviations and "
               "standard errors printed to three decimals and aligned on the point. The "
               "caption names two models while the table lists three"),

    table(15, 1, caption("Table 2: Accident rate of each model", numbering="Table N:"),
          mention(15, first=14, style=["Table 2"], count=1, pattern="as-shown-in", read=1,
                  lead=span(14, "The expectations of accident rate", "are shown in Table 2"),
                  trail=span(14, "The control time model can reduce", "13.66%")),
          grid(3, 2, header=1, rules="boxed", units_hdr=True, decimal=True, numeric=1,
               txt=1, width="half"),
          path=[S5, S53], kind="result",
          note="header Model / Accident per 100,000 vehicles, then two rows 53.024 and "
               "61.416; the rate unit lives in the header so the body cells are bare numbers "
               "aligned to three decimals. The table is cited one page before it is printed, "
               "and the prose says the control time model reaches 61.416 while the sentence "
               "beside it claims the model reduces the accident rate by 13.66%"),
]

EXCLUDED = [
    {"page": 8, "bbox": REG[(8, 1)], "reason": "duplicate",
     "note": "vector box around the prose, the Figure 4 caption and the drawing; the drawing "
             "is measured again as the raster inside it"},
    {"page": 9, "bbox": REG[(9, 1)], "reason": "duplicate",
     "note": "same wrapper around the Figure 5 prose, caption and drawing"},
    {"page": 10, "bbox": REG[(10, 1)], "reason": "duplicate",
     "note": "same wrapper around the Figure 6 prose, caption and drawing"},
    {"page": 10, "bbox": REG[(10, 3)], "reason": "duplicate",
     "note": "second copy of the Figure 6 drawing, 24.8 pt to the right of the first, clipped "
             "at the right margin"},
    {"page": 15, "bbox": REG[(15, 2)], "reason": "duplicate",
     "note": "same wrapper around the Figure 9 prose, caption and drawing"},
    {"page": 19, "bbox": REG[(19, 1)], "reason": "duplicate",
     "note": "same wrapper around the Figure 12 prose, caption and drawing"},
]

RULES = [
    "模型章把同一张平面图换着说法重画，Figure 4、Figure 5、Figure 6、Figure 9、Figure 12 五张落在同一 4 Models/5 Analysis and Results 路径下，[geometry.family] 一律 map-or-plan-view。",
    "平面图统一带三样尺寸标注：booth 列的 dB、车道端的 dL、广场纵深的 D，[geometry.printed_numbers]=True 说的就是这三处数字。",
    "平面图没有坐标轴、没有网格、没有图例，[geometry.legend]=none 且 [geometry.shared_axes]=False，五张无一例外。",
    "参数对照用同题注下的并列画法：Figure 3 两块共用一句 [caption.verbatim]，靠 [place.page_order] 区分左右。",
    "同一页先放两份不同工况的图再放一句合并题注时，题注被抽成一条字符串：Figure 1 与 Figure 2 的 caption 落在同一行，[caption.words] 只按各自半句算。",
    "三视图（Figure 11）把敏感度拆成三块并列，每块只标一个自变量，[geometry.panel_count]=1 而 [place.page_order] 记 1 到 3，三块共用一句题注。",
    "敏感度块的 y 轴标题只写在最左一块，[geometry.legend]=none，图例靠轴标题与自变量字母承担。",
    "折线图只印轴标题与轴刻度，没有数据点标记，[geometry.data_labels]=False，[geometry.three_d]=no。",
    "正文引用靠 as shown in Figure N 的从句，[mention.lead_pattern]=as-shown-in 出现在 Figure 5、Figure 6、Figure 9、Figure 11、Table 2 五处。",
    "平面图有三种不提编号的引出法：先讲模型再画图（Figure 3 用 They then immediately starts merging…），先定义再画图（Figure 4 用 We call the mapping f a merging pattern），先举例再画图（Figure 12 用 the shape and merging pattern are as follows），这三种的 [mention.style] 都是空列表。",
    "图前引出句可以与图同页也可跨页：Figure 1 与 Figure 2 的引出句在 p6、图在 p7，[mention.lead_pages]=1；Table 2 的引用在 p14、表印在 p15，同样为 1。",
    "表统统加框：三张表 [table.rule_style]=boxed，含外框与列间竖线，没有三线表。",
    "表头行恒为一行，[table.header_rows]=1，且没有合并单元格与隔行底纹：[table.merged_cells]=False、[table.zebra]=False。",
    "单位写在表头里：Table 2 的 Accident per 100,000 vehicles 与符号表的 Unit 列都记 [table.units_in_header]=True，表体只留数字或符号。",
    "数值列按小数点对齐，[table.decimal_aligned]=True 出现在 Table 1 与 Table 2；符号表只有整数与符号，记 False。",
    "表宽随内容收缩：统计表占满栏宽记 [table.width]=full，两列事故率表只有约三分之二，记 half。",
    "唯一无题注的表是第 3 节的符号表：它只有章节标题当标签，[caption.verbatim] 为空串、caption_source=none，[caption.numbering]=none。",
    "统计量比较用箱线图而不是柱状图：Figure 7 是三个带缺口的箱体加虚线须与 x 形离群点，[geometry.family]=box-or-violin，只靠文本层会误判成 bar。",
    "分布比较用半透明叠加直方图：Figure 8 两组单宽分箱叠画在同一坐标，[geometry.legend]=outside-right 且图例标题为 Model，[geometry.family]=histogram。",
    "同一个图的并列两块不共享坐标轴时诚实记 False：Figure 10 左右两块的 y 轴分别 -2.0~0.0 与 0.10~-0.10，[geometry.shared_axes]=False，靠 [place.page_order] 区分左右。",
    "平面图之外的三件数据图都带完整矩形边框且无网格线，[geometry.legend]=none，只有直方图例外保留 ggplot 的双向网格。",
]

payload = {"paper": PID, "layout_sha256": LAYOUT["layout_sha256"],
           "items": ITEMS, "tables": TABLES,
           "excluded_regions": EXCLUDED, "rules": RULES,
           "note": "hand pass, 25 measured regions -> 16 figures, 3 tables, 6 excluded; the "
                   "layout that first measured this paper lost Figures 7, 8 and 10 to off-page "
                   "fill rects, so this record was made after the extractor was fixed"}

out = PROXY / f"{PID}-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"wrote {out} items={len(ITEMS)} tables={len(TABLES)} rules={len(RULES)}")
