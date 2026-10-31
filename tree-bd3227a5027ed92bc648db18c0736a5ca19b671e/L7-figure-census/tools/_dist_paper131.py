"""Hand pass for P-D-2017-56632-67f41f43 (TSA security-line queueing, 10 figures, no tables).

Shape of the paper: a schematic of a two-lane queueing network (chapter 2), five
probability-density exhibits used to justify the distributional assumptions (2.1),
a simulation whose output is plotted as four parameter scans (chapter 4.1-4.2), a
profit heat map (4.3.1) and one discipline comparison (4.3.2). Ten printed figures,
zero tables.

What the record has to say out loud:

1. Every figure carries one number but half of them are printed as a left|right pair
   under that single number: Figures 2, 4, 5, 6, 7, 8, 9, 10 are two panels side by
   side, and "(left)" / "(right)" is written only in the caption, never on the plate.
2. The eight right-hand panels are recorded as fragments of the same exhibit, not as
   separate rows, because they carry no second number. Ten rows, ten printed numbers.
3. Ten other measured regions are not exhibits at all: six boxed Assumption blocks,
   one random-variable definition box, two boxed equations and one pseudo-code
   listing. The detector returns each as a rectangle on the page, so each is excluded
   with a measured bbox and a reason.
4. The body prose refers to a figure by pointing at the page ("depicted below",
   "can be seen below", "the plots above", "the heat maps below") far more often than
   by number: only Figures 1, 4, 5, 6 and 10 are ever named, and Figure 4 is first
   named a page after it prints.
5. Captions print below every one of the ten exhibits, use "Figure N:" throughout,
   never state a unit and never state a conclusion.
6. Two captions (Figures 2 and 4) are hyphenated across a line break by the typesetter
   ("inter- arrival", "pas- senger"), so they are typed from the crop rather than
   read from the text layer.

Usage: python -I tools/_dist_paper131.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2017-56632-67f41f43"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((LANE / f".proxy/{PID}-ctx.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

HEAD: dict[str, str] = {}
for _h in CTX["headings"]:
    _n, _l = _h.get("number"), _h.get("label")
    if not _n or not _l or not _l.startswith(_n + " "):
        continue
    if _n not in HEAD or (HEAD[_n].split()[-1].isdigit() and not _l.split()[-1].isdigit()):
        HEAD[_n] = _l


def P(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


EXCLUDED = [
    {"page": 6, "bbox": REG[(6, 1)], "reason": "not-an-exhibit",
     "note": "boxed 'Assumption 1' paragraph with its italic Remark, set as a ruled text "
             "block on the page. The detector returns the rule as a region; there is no "
             "artwork inside it."},
    {"page": 6, "bbox": REG[(6, 2)], "reason": "not-an-exhibit",
     "note": "boxed 'Assumption 2' paragraph with its italic Remark, immediately below "
             "Assumption 1. Same ruled block, no artwork."},
    {"page": 7, "bbox": REG[(7, 1)], "reason": "not-an-exhibit",
     "note": "boxed 'Assumption 3' paragraph with its italic Remark, at the head of page 7."},
    {"page": 8, "bbox": REG[(8, 3)], "reason": "not-an-exhibit",
     "note": "the ruled definition box that introduces the random variables X, W and Y "
             "(time in the mm wave scan, time scanning one piece of luggage, and their "
             "product). Algebra, not a display."},
    {"page": 8, "bbox": REG[(8, 4)], "reason": "not-an-exhibit",
     "note": "boxed 'Assumption 5' paragraph with its Remark (X and Y independent)."},
    {"page": 10, "bbox": REG[(10, 1)], "reason": "not-an-exhibit",
     "note": "boxed 'Assumption 6' paragraph with its Remark (a passenger always has "
             "someone to wait behind)."},
    {"page": 11, "bbox": REG[(11, 1)], "reason": "in-body-diagram",
     "note": "boxed display equation (5), the average wait time in queue 1, framed so that "
             "the Remark on page 10 can refer back to the boxed equations."},
    {"page": 11, "bbox": REG[(11, 2)], "reason": "in-body-diagram",
     "note": "boxed display equation (6), the average wait time in queue 2."},
    {"page": 13, "bbox": REG[(13, 1)], "reason": "in-body-diagram",
     "note": "Algorithm 1 pseudo-code listing framed as a ruled block (Result line, "
             "array initialisation, the arrival/check/scan assignment loop). The only "
             "region in the paper that looks like a figure but holds program text."},
    {"page": 18, "bbox": REG[(18, 1)], "reason": "not-an-exhibit",
     "note": "boxed 'Assumption 7' paragraph with its Remark (staffing is the only cost)."},
    {"page": 6, "bbox": REG[(6, 4)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 2 (regular passengers). One printed number "
             "covers the pair, so the Figure 2 row carries the left panel and this is the "
             "second panel, not a second exhibit."},
    {"page": 8, "bbox": REG[(8, 2)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 4 (regular passengers), same treatment as "
             "Figure 2: one number, two panels."},
    {"page": 14, "bbox": REG[(14, 2)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 5 (average time in queue 2)."},
    {"page": 15, "bbox": REG[(15, 2)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 6 (wait time against the number of scan "
             "stations k)."},
    {"page": 16, "bbox": REG[(16, 2)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 7 (wait time against the number of scan "
             "stations k)."},
    {"page": 17, "bbox": REG[(17, 2)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 8 (variance in the scan station queue)."},
    {"page": 18, "bbox": REG[(18, 3)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 9 (regular passengers). Each heat map carries "
             "its own colour bar in the gutter to its right, so the pair is one number, two "
             "panels and two independent colour scales."},
    {"page": 19, "bbox": REG[(19, 2)], "reason": "fragment-of-other",
     "note": "the right-hand panel of Figure 10 (variance against the fraction of fast "
             "passengers)."},
]


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def place(page: int, idx: int, path: list[str], kind: str, numbered: bool = True) -> dict:
    b = REG[(page, idx)]
    mid = (b[1] + b[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    frac = (b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H)
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 0,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": frac > 0.5,
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


def mention(page: int, *, first: int | None = None, style: list[str], count: int,
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
           kind: str, legend: str = "none", printed: bool = False,
           labels: bool = False, panels: int = 1, layout: str = "1",
           shared: bool = False, colorbar: bool = False, three_d: str = "no",
           source: str = "text-layer", other_note: str = "", note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "other_note": other_note or None,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
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
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


# --- quoting -------------------------------------------------------------------
_LIG = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"}


def _fold(s: str) -> tuple[str, list[int]]:
    out: list[str] = []
    idx: list[int] = []
    for i, ch in enumerate(s):
        rep = _LIG.get(ch, ch)
        for c in rep:
            out.append(c)
            idx.append(i)
    return "".join(out), idx


def _find(page: int, needle: str, after: int = 0) -> tuple[str, int, int]:
    t = text(page)
    f, idx = _fold(t)
    n, _ = _fold(needle)
    j = f.find(n, after)
    assert j >= 0, f"{needle!r} not on page {page}"
    return t, idx[j], idx[j + len(n) - 1] + 1


def _to_word_end(page: int, pos: int) -> int:
    t = text(page)
    k = t.find(" ", pos)
    return len(t) if k < 0 else k


def span(page: int, start: str, end: str) -> str:
    t, i, _ = _find(page, start)
    _, j, jend = _find(page, end, i)
    j = _to_word_end(page, jend)
    q = t[i:j].strip()
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def cap(page: int, marker: str, end: str, *, after: int = 0) -> str:
    t, i, _ = _find(page, marker, after)
    _, j, jend = _find(page, end, i)
    return t[i:_to_word_end(page, jend)].strip()


# --- section paths -------------------------------------------------------------
S2 = P("2")
S211 = P("2", "2.1", "2.1.1")
S212 = P("2", "2.1", "2.1.2")
S411 = P("4", "4.1", "4.1.1")
S412 = P("4", "4.1", "4.1.2")
S42 = P("4", "4.2")
S431 = P("4", "4.3", "4.3.1")
S432 = P("4", "4.3", "4.3.2")

PAIR_BELOW = ("one printed number covers two panels printed side by side; the row carries "
              "the left panel's bbox and the right panel is recorded as a fragment of the "
              "same exhibit")

ALL = [
    figure(5, 1, "flowchart-or-schematic",
           caption(cap(5, "Figure 1: ", "respectively.")),
           mention(5, first=5, style=["Figure 1", "depicted below"], count=2, pattern="none",
                   lead=span(5, "We model the airport security line",
                             "depicted below.")),
           path=S2, kind="model",
           note="vector drawing, no axes and no scale: two stacked lanes (blue regular, "
                "green precheck), each lane an entry arrow, queue Q1, server S1, queue Q2, "
                "server S2 and an exit arrow, with lambda superscripts on the arrival "
                "arrows. Only letters are printed, never a number"),
    figure(6, 3, "histogram",
           caption("Figure 2: The exponential ﬁt (using Matlab’s expfit function) to "
                   "the inter-arrival times of precheck (left) and regular (right) "
                   "passengers overlaid onto the corresponding histograms.",
                   voice="passive"),
           mention(6, first=6, style=["Depicted below"], count=1, pattern="none",
                   lead=span(6, "Depicted below are histograms",
                             "given data ﬁle."),
                   trail=span(6, "They strongly resemble the shape",
                              "the next key assumption."),
                   read=1),
           path=S211, kind="model", panels=2, layout="1x2", printed=True,
           source="typed-from-crop",
           note="left precheck (green bars, x 0-70, y 0-25) and right regular (blue bars, "
                "x 0-90, y 0-30), each with one black exponential-fit curve; no legend, and "
                "the two panels do not share a scale. Caption typed from the crop because "
                "the typesetter broke 'inter-arrival' across a line ('inter- arrival')"),
    figure(7, 2, "histogram",
           caption(cap(7, "Figure 3: ", "histogram."), voice="passive"),
           mention(7, style=[], count=0),
           path=S212, kind="model", printed=True,
           note="single panel, teal histogram on the left axis (Count) with the kernel "
                "density curve read off a second right-hand axis (Probability Density); no "
                "legend and no panel label. The paper never names Figure 3, before or after "
                "it prints"),
    figure(8, 1, "composite-panel",
           caption("Figure 4: The kernel density estimate of precheck (left) vs. regular "
                   "(right) passenger time spent in service station 2 (scanning).",
                   voice="passive"),
           mention(8, first=9, style=["Figure 4"], count=2, pattern="parenthetical",
                   trail=span(9, "This density was computed and plotted",
                              "estimates of fX and fW"),
                   read=1),
           path=S212, kind="model", panels=2, layout="1x2", legend="inside", printed=True,
           source="typed-from-crop",
           note="the two panels are not the same chart: left holds three overlaid density "
                "curves (X-Ray Scan, mm Wave Scan, Combined Scan) with a three-entry legend "
                "inside, right holds a histogram on a dual axis with no legend. Both axes "
                "are Time (sec). Caption typed from the crop because 'passenger' is broken "
                "across a line ('pas- senger')"),
    figure(14, 1, "line",
           caption(cap(14, "Figure 5: ", "respectively."), voice="passive"),
           mention(14, first=14, style=["Figure 5"], count=1, pattern="figure-n-shows",
                   trail=span(14, "It appears that they follow the same trend",
                              "from 50 to 4050."),
                   read=2),
           path=S411, kind="result", panels=2, layout="1x2", legend="inside", printed=True,
           shared=True,
           note="validation plate: simulated (blue) against theoretical (orange), two-entry "
                "legend inside each panel, x 'Number of Passengers' 0-4500 on both. Left y "
                "is Time Spent in Q1 (sec), right y is Time Spent in Q2 (sec) with a 1e4 "
                "multiplier, which is why the two panels are not on a common scale"),
    figure(15, 1, "line",
           caption(cap(15, "Figure 6: ", "(right)."), vars_=2),
           mention(15, first=15, style=["seen below", "Figure 6"], count=2, pattern="none",
                   lead=span(15, "The results from our simulation can be seen below", "below."),
                   trail=span(15, "The estimated transition values given by (8)",
                              "on the same plot in Figure 6."),
                   read=1),
           path=S411, kind="result", panels=2, layout="1x2", legend="inside", printed=True,
           note="four-series log-y scan, legend inside upper right with four entries (C = "
                "1..4 left, k = 1..4 right), plus four colour-coded vertical marker lines "
                "whose values are printed only in the body text, never on the plot"),
    figure(16, 1, "line",
           caption(cap(16, "Figure 7: ", "(right)."), vars_=2),
           mention(16, first=16, style=["seen below"], count=1, pattern="none",
                   lead=span(16, "The results from our simulation of regular passengers",
                             "seen below."),
                   trail=span(16, "The average wait time of a passenger in the scanning",
                              "dependent on both c and k."),
                   read=1),
           path=S412, kind="result", panels=2, layout="1x2", legend="inside", printed=True,
           note="same four-series log-y template as Figure 6 applied to the scan station, "
                "four unlabelled colour-coded marker lines per panel; the paper never names "
                "Figure 7, it points at it with 'can be seen below'"),
    figure(17, 1, "line",
           caption(cap(17, "Figure 8: ", "= 1."), vars_=2, cond=True),
           mention(17, first=17, style=["the plots above"], count=1, pattern="as-shown-in",
                   trail=span(17, "As seen in the plots above",
                              "as arrival rate increases."),
                   read=1),
           path=S42, kind="result", panels=2, layout="1x2", legend="inside", printed=True,
           shared=True,
           note="variance scans, four c-series per panel, shared x 'Arrival Rate "
                "(sec/passenger)' 0-40; y is 'Variance (sec^2)' with a 1e8 multiplier on the "
                "left and a 1e9 multiplier on the right, so the two panels look comparable "
                "but are three orders apart"),
    figure(18, 2, "heatmap-or-contour",
           caption(cap(18, "Figure 9: ", "(right)."), vars_=2),
           mention(18, first=18, style=["heat maps below"], count=1, pattern="none",
                   trail=span(18, "For the TSA precheck line, the most cost-e",
                              "and 3 scanning stations"),
                   read=1),
           path=S431, kind="result", panels=2, layout="1x2", printed=True, colorbar=True,
           shared=True,
           note="two 10x10 cell heat maps, x 'Scan Stations (k)' and y 'Check Stations (c)' "
                "on both, profit in $/sec. Each panel carries its own colour bar standing in "
                "the inter-panel gutter: +-0.15 for precheck, +-0.08 for regular, so the two "
                "maps cannot be read against one another by colour"),
    figure(19, 1, "line",
           caption(cap(19, "Figure 10: ", "(blue)."), vars_=1),
           mention(19, first=19, style=["Figure 10"], count=1, pattern="direct",
                   trail=span(19, "Contrary to our initial hypotheses",
                              "wait time and higher variance."),
                   read=1),
           path=S432, kind="sensitivity", panels=2, layout="1x2", legend="inside",
           printed=True, shared=True,
           note="log-y discipline comparison, two-entry legend inside each panel (FIFO "
                "Discipline blue, Priority Discipline orange), x 'Fraction Population Slow' "
                "0-1 on both; left y is Time (log(sec)), right y is Variance (sec^2)"),
]

for _n, _e in enumerate(ALL, 1):
    _e["place"]["doc_order"] = _n
_by_page: dict[int, list[dict]] = {}
for _e in ALL:
    _by_page.setdefault(_e["page"], []).append(_e)
for _entries in _by_page.values():
    for _i, _e in enumerate(_entries, 1):
        _e["place"]["page_order"] = _i

FIGURES = list(ALL)
TABLES: list[dict] = []

RULES = [
    "图族跟着论证任务走：唯一一张 flowchart-or-schematic 是队列网络的模型示意，"
    "2 张 histogram 只用在“拟合得好不好”这一处（Fig 2/3），1 张 composite-panel 是"
    "左右两栏不同图型拼在一个编号下（Fig 4），5 张 line 全是参数扫描与验证，"
    "1 张 heatmap-or-contour 是唯一的二维损失面 [geometry.family]。",
    "“一个编号两个分面”是本篇的默认版式：10 个条目里 8 个是 left|right 双联版"
    "（Fig 2/4/5/6/7/8/9/10），只有 Fig 1 与 Fig 3 单幅；分面上的 (left)/(right) 只写在"
    "题注里，版面上一个字也不印 [geometry.panel_count][geometry.panel_layout]。",
    "左右分面多数不共享坐标轴，共享只在“同一自变量、同一量程、只换指标”时才成立："
    "Fig 5（乘客数 0-4500）、Fig 8（到达率 0-40）、Fig 9（站点数 1-10）、Fig 10"
    "（慢速乘客比例 0-1）记为共享；Fig 2/4 两侧量程不同、Fig 6/7 两侧换的是 c 与 k，"
    "一律记为不共享 [geometry.shared_axes]。",
    "图例位置由序列数决定：2-4 条序列的 6 张图例全部 inside 右上，唯一的多序列无图例版"
    "是 Fig 2 的双直方图，Fig 1 是示意图因而无图例，全篇没有一例 outside 图例 "
    "[geometry.legend]。",
    "三维为零、色标只在热图出现：所有图都是二维平面，唯一带 colorbar 的是 Fig 9 的两张"
    "热图，且每个分面各带一条、量程不同（±0.15 / ±0.08），这类色标立在两栏之间的"
    "装订缝里 [geometry.three_d][geometry.colorbar]。",
    "框内印刷数字是折线模板的固定件：9 张带刻度与轴题，唯一不带的 Fig 1 只印 λ、Q、S "
    "与 Enter/Check/Scan/Exit 等文字；没有任何一张图把数值直接标在数据点上 "
    "[geometry.printed_numbers][geometry.data_labels]。",
    "题注位置是硬规矩：10 个条目 10 个在下，没有一例在上 [caption.position]；"
    "编号一律 “Figure N:” 加半角冒号 [caption.numbering]。",
    "题注只报题目不报量：词数 19-29、句数 1-2，10 条没有一条写单位，也没有一条下结论；"
    "只有 Fig 5 的题注例外地用第二句交代配色（蓝色模拟、橙色理论）"
    "[caption.words][caption.units][caption.concludes]。",
    "题注把参数写进括注而不是写进句子：Fig 6/7 用 “for various values of c (left) and "
    "k (right)” 点出两个自变量，Fig 9 用 “for TSA precheck (left) and Regular passengers "
    "(right)” 点出两个自变量，Fig 10 点出“the fraction of fast passengers”；条件只在 "
    "Fig 8 出现一次（“constant k = 1”），其余 9 条不给任何条件 [caption.variables]"
    "[caption.conditions]。",
    "正文靠方位指代而不靠编号：10 个条目里只有 Fig 1/4/5/6/10 被编号点过名，其余 5 张"
    "全靠 “depicted below”“can be seen below”“the plots above”“the heat maps below” "
    "这类指代，引出句式因此以 none 为主（6 条），点名的 4 条分散成 parenthetical"
    "（Fig 4）、figure-n-shows（Fig 5）、as-shown-in（Fig 8）与 direct（Fig 10）"
    "[mention.lead_pattern][mention.count]。",
    "首次提及页几乎总等于图页（8 个 lead_pages=0），两个例外：Fig 4 排在第 8 页页首，"
    "正文到第 9 页才第一次写 “the left plot in Figure 4”，lead_pages=-1；Fig 3 从头到尾"
    "没有一句指向它，first_page=null [mention.lead_pages]。",
    "图前引出句与图后解读句分工清楚：4 张有真正的图前句（Fig 1/2/6/7，全部是不带编号的"
    "方位句），Fig 9 的图前句因为超过 25 词被弃引；图后解读句一律 1 句，只有验证图 "
    "Fig 5 连读 2 句 [mention.read_sentences]。",
    "章节性质决定展品密度：model 章（第 2 章）吃掉 4 张密度/示意图，result 章（第 4 章）"
    "5 张，sensitivity 只留 1 张纪律对照，全篇没有一张表 [place.section_kind]。",
    "十块被检测器当成图量出来的版心其实不是展品：6 个带框 Assumption 段、1 个随机变量"
    "定义框、2 个带框公式和 1 段伪代码，因此全篇 28 个 region 里只有 10 个是展品，"
    "其余 18 个（含 8 个右分面）全部登记为排除项 [place.area_frac]。",
]

NOTE = (
    "10 exhibits on 22 pages: ten figures and no tables against 28 measured regions and 18 "
    "exclusions. Eight of the ten figures are one printed number covering two side-by-side "
    "panels, so the right-hand panel of each pair is recorded as a fragment of the same "
    "exhibit rather than as a row: the row count equals the printed-number count. Ten of the "
    "excluded regions are not artwork at all - six boxed Assumption paragraphs, the X/W/Y "
    "definition box, the two boxed equations (5) and (6) and the Algorithm 1 pseudo-code "
    "listing. The prose mostly does not cite figures by number: five of the ten are never "
    "named anywhere, and Figure 4 is named for the first time on the page after it prints. "
    "Figures 2 and 4 carry captions the typesetter hyphenated across a line break, so those "
    "two are typed from the crop."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}


def main() -> int:
    from collections import Counter

    def agg(key: str, bucket: str = "geometry") -> Counter:
        return Counter(e[bucket][key] for e in FIGURES)

    print("figures", len(FIGURES), "tables", len(TABLES), "excluded", len(EXCLUDED))
    for k in ("family", "legend", "three_d", "colorbar", "printed_numbers", "panel_count",
              "shared_axes", "data_labels"):
        print(k, dict(agg(k)))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in ALL)))
    print("section", dict(Counter(" > ".join(e["place"]["section_path"]) for e in ALL)))
    for k in ("position", "numbering", "voice", "words", "sentences", "variables",
              "variable_count", "conditions", "units", "concludes"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in ALL)))
    print("pattern", dict(Counter(e["mention"]["lead_pattern"] for e in ALL)))
    print("first", dict(Counter(e["mention"]["first_page"] for e in ALL)))
    print("lead_pages", dict(Counter(e["mention"]["lead_pages"] for e in ALL)))
    print("count", dict(Counter(e["mention"]["count"] for e in ALL)))
    print("read", dict(Counter(e["mention"]["read_sentences"] for e in ALL)))
    print("area", sorted(e["place"]["area_frac"] for e in ALL))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in ALL)))
    print("source", dict(Counter(e["caption_source"] for e in ALL)))
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
