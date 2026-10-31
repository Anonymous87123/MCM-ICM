"""Hand pass for P-D-2017-55295-9001b6d9 (Bangkok airport security-check queueing, 19 figures + 5 tables).

Shape of the paper: a parameter chapter (2), two model chapters (tandem M/G/c, queueing
network), a simulation-and-validation chapter (4), then three routing modifications
(greedy on backlogs, backpressure, drift-plus-penalty) and a sensitivity chapter that
replays the same three metrics under cultural norms.

What the record has to say out loud:

1. One chart template carries the whole paper: queue length over time, one polyline per
   queueing node, legend outside right with 18-20 entries in two columns. It is printed
   five times (Figs 6, 10, 12, 15 and, with two series, Fig 8), and the metric panels are
   always a pair (throughput | variance) printed side by side under one caption.
2. The three schematics (Figs 3, 4, 9) and the fourth (Fig 11) are the same drawing:
   two boxes "ID Check" / "Screening Check", a Regular/Pre-check split, arrows. What
   changes between them is only the arrow topology, which is the whole argument of
   chapter 5. None of them carries a number except the check-point counts N_A1..N_B2.
3. Fig 5 is the only raster in the paper: an isometric airport floor plan pasted in to
   justify the parameter source. It is a map, not a data exhibit.
4. Captions print below every one of the 19 figures and below all five tables; the
   numbering is "Figure N:" / "Table N:" throughout, and no caption states a unit.
5. Two printed captions are interleaved by the extractor on page 12 (Figs 7 and 8 share
   one text-layer line) and one is hyphenated across the line break (Fig 19), so those
   three are typed from the crop, not read from the text layer.
6. Nine exhibits are cited by no sentence at all or only once, and the citation habit is
   post-hoc: the prose names the figure after it has been read ("After analyzing Figure
   6 and 7 ...", "We can see from Table 4 that ..."), never before.
7. Figure 18 is one captioned exhibit printed as two measured regions; the left panel
   carries the row and the right panel is recorded as a fragment of the same exhibit.

Usage: python -I tools/_dist_paper130.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2017-55295-9001b6d9"
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


# the detector reads a table-row pair on page 16 as a heading numbered "6", and because
# that label ends in letters it then outranks the printed chapter title; restore it.
HEAD["6"] = "6 Sensitivity Analysis"


def P(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


EXCLUDED = [
    {
        "page": 21, "bbox": REG[(21, 2)], "reason": "fragment-of-other",
        "note": "the right-hand panel of Figure 18. The pair is one printed exhibit under "
                "one caption, returned by the detector as two side-by-side regions; the "
                "Figure 18 row carries the left panel's bbox and panel_count 2, and this is "
                "the second panel.",
    },
    {
        "page": 21, "bbox": REG[(21, 4)], "reason": "fragment-of-other",
        "note": "the three-entry legend box drawn inside the right-hand panel of Figure 18 "
                "(Control group / With family checkpoint / W/o family checkpoint), returned "
                "as a region nested in that panel.",
    },
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


def table(page: int, idx: int, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, source: str = "text-layer", note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
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
    j = f.find(needle, after)
    assert j >= 0, f"{needle!r} not on page {page}"
    return t, idx[j], idx[j + len(needle) - 1] + 1


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


def cap(page: int, marker: str, end: str, *, after: int = 0, cut: bool = False) -> str:
    t, i, _ = _find(page, marker, after)
    _, j, jend = _find(page, end, i)
    return t[i:(jend if cut else _to_word_end(page, jend))].strip()


# --- section paths -------------------------------------------------------------
S21 = P("2", "2.1")
S22 = P("2", "2.2")
S23 = P("2", "2.3")
S3 = P("3")
S31 = P("3", "3.1")
S32 = P("3", "3.2")
S42 = P("4", "4.2")
S43 = P("4", "4.3")
S51 = P("5", "5.1")
S522 = P("5", "5.2", "5.2.2")
S531 = P("5", "5.3", "5.3.1")
S532 = P("5", "5.3", "5.3.2")
S621 = P("6", "6.2.1")
S622 = P("6", "6.2.2")
S623 = P("6", "6.2.3")
S624 = P("6", "6.2.4")

LONG_LEGEND = ("twenty legend entries in two columns of ten, one per queueing node "
               "(PreIDQ0, RegIDQ0-2, PreScreenQ00-03, RegScreenQ00-Q23)")
TWO_LEGEND = "two entries outside right (ID Check Queue, Screening Check Queue)"
INSIDE_TWO = "two entries inside the frame at the right (Variance, Throughput)"
SCHEMATIC = ("two boxed station groups 'ID Check' and 'Screening Check', a Regular / "
             "Pre-check split and arrows between them; the only numerals are the "
             "check-point counts on the dividing labels")

ALL = [
    figure(6, 1, "flowchart-or-schematic",
           caption(cap(6, "Figure 1: ", "Nodes")),
           mention(6, first=5, style=["Figure 1"], count=1, pattern="parenthetical",
                   lead=span(5, "We also adopt M/G/c queue", "Figure 1(b))")),
           path=S21, kind="other", panels=2, layout="1x2", printed=True, labels=True,
           note="the detector measured only panel (b), the M/G/c node: panel (a), the "
                "M/G/1 node, is printed to its left and is outside the region, so the row "
                "carries panel_count 2 and the bbox of the second panel only"),
    table(6, 2, caption(cap(6, "Table 1: ", "Problems"), numbering="Table N:"),
          mention(6, first=6, style=["Table 1"], count=1, pattern="direct",
                  lead=span(6, "The specific numbers", "Table 1.")),
          grid(6, 3, header=1, numeric=1, txt=2),
          path=S22, kind="other",
          note="boxed frame with a header rule and no interior vertical rules; the value "
               "column mixes scalars and (mean, variance) tuples and is centred, not "
               "decimal-aligned, so the tuples and the scalars do not line up"),
    figure(6, 3, "histogram",
           caption(cap(6, "Figure 2: ", "Mathematica")),
           mention(6, style=[], count=0),
           path=S22, kind="other", panels=4, layout="1x4", printed=True,
           note="four histograms in one row, no legend and no sub-labels; the body text "
                "never names Figure 2, so the plate is used as supporting evidence for "
                "the Mathematica fit without being cited"),
    table(7, 1, caption(cap(7, "Table 2: ", "Counters"), numbering="Table N:"),
          mention(7, first=7, style=["Table 2"], count=1, pattern="as-shown-in",
                  lead=span(7, "Therefore we set the number of check points", "Table 2.")),
          grid(3, 3, header=1, numeric=2, txt=1, width="half"),
          path=S23, kind="other",
          note="the paper's one headline table: three rows, boxed, two integers per "
               "passenger class; it is the only exhibit that states the deployment "
               "decision the whole model rests on"),
    table(8, 1, caption(cap(8, "Table 3: ", "Notations"), numbering="Table N:"),
          mention(8, style=[], count=0),
          grid(10, 2, header=1, txt=2),
          path=S3, kind="symbols",
          note="ten rows of symbol and gloss, boxed, uncited: the notation table is the "
               "only exhibit in the paper that no sentence points at"),
    figure(8, 2, "flowchart-or-schematic",
           caption(cap(8, "Figure 3: ", "Model")),
           mention(8, first=8, style=["Figure 3"], count=1, pattern="as-shown-in",
                   lead=span(8, "As Figure 3 demonstrates", "tandem array."),
                   trail=span(8, "The first M/G/c queueing node", "NA check points."),
                   read=1),
           path=S31, kind="model", printed=True, labels=True, note=SCHEMATIC),
    figure(9, 1, "flowchart-or-schematic",
           caption(cap(9, "Figure 4: ", "Model")),
           mention(9, first=9, style=["Figure 4"], count=1, pattern="as-shown-in",
                   lead=span(9, "The queueing network in real-life airport", "Figure 4."),
                   trail=span(9, "Every queueing node is an M/G/1 queueing",
                              "every check point."),
                   read=1),
           path=S32, kind="model", printed=True, labels=True, note=SCHEMATIC),
    figure(10, 1, "map-or-plan-view",
           caption(cap(10, "Figure 5: ", "System")),
           mention(10, first=10, style=["Figure 5"], count=1, pattern="as-shown-in",
                   lead=span(10, "Other parameters are set after", "Figure 5.")),
           path=S42, kind="model", three_d="isometric", labels=True,
           note="the only raster exhibit in the paper: a pasted isometric floor plan of the "
                "terminal with LEVEL 4 / Departures, the concourse tags A1-A6 to G1-G5 and "
                "circled position markers; no data, no key, and it exists to name where the "
                "parameters come from"),
    table(11, 1, caption(cap(11, "Table 4: ", "Process"), numbering="Table N:"),
          mention(11, first=10, style=["Table 4"], count=2, pattern="as-shown-in",
                  lead=span(10, "The result of our simulation", "Table 4."),
                  trail=span(11, "We can see from Table 4", "average waiting time"),
                  read=1),
          grid(6, 4, header=1, numeric=3, txt=1, units_hdr=True, decimal=True),
          path=S43, kind="evaluation",
          note="the validation table: five airports, the arrivals and the website wait "
               "range in the left columns, the model's own wait time decimal-aligned in the "
               "last; units are printed inside the header as (minute), not in the caption"),
    figure(12, 1, "line",
           caption(cap(12, "Figure 6: ", "Model")),
           mention(12, first=12, style=["Figure 6"], count=3, pattern="direct",
                   trail=span(12, "After analyzing Figure 6 and 7",
                              "presence of suspicious people."),
                   read=2),
           path=S43, kind="evaluation", legend="outside-right", printed=True,
           note="the paper's base template: queue length against time, one polyline per "
                "queueing node, twenty entries in the legend, no gridlines, no title line"),
    figure(12, 2, "line",
           caption("Figure 7: The Longest Queue with Suspicious Passenger",
                   pos="below"),
           mention(12, first=12, style=["Figure 7"], count=2, pattern="direct",
                   trail=span(12, "Contrasting the Figure 7 with", "88 minutes"),
                   read=1),
           path=S43, kind="evaluation", printed=True, source="typed-from-crop",
           note="the caption is typed from the crop: the text layer interleaves it with "
                "Figure 8's caption on one line. Two dashed vertical markers at 88 and 152 "
                "minutes show the suspicious arrivals the body text then reads off"),
    figure(12, 3, "line",
           caption("Figure 8: The Number of PAX in Queue in Tandem M/G/c Queueing Model"),
           mention(12, first=12, style=["Figure 8"], count=2, pattern="direct",
                   trail=span(12, "In Figure 8, passengers wait", "every queue node"),
                   read=1),
           path=S43, kind="evaluation", legend="outside-right", printed=True,
           source="typed-from-crop",
           note="two series only, and the caption is typed from the crop for the same "
                "interleaving reason; the trace is the raw simulation output, hundreds of "
                "spikes, with the screening series filled"),
    figure(13, 1, "flowchart-or-schematic",
           caption(cap(13, "Figure 9: ", "Backlogs")),
           mention(13, first=13, style=["Figure 9"], count=1, pattern="as-shown-in",
                   lead=span(13, "As Figure 9 demonstrated", "check points")),
           path=S51, kind="other", printed=True, labels=True,
           note=SCHEMATIC + "; this is the same drawing as Figure 4 with the screening "
                "arrows crossed, which is the only change the chapter argues for"),
    figure(14, 1, "bar",
           caption(cap(14, "Figure 10: ", "Backlogs")),
           mention(14, first=13, style=["Figure 10"], count=2, pattern="direct",
                   lead=span(13, "The results are illustrated", "Figure 10."),
                   trail=span(13, "The greedy algorithm achieves", "less then 16"),
                   read=1),
           path=S51, kind="other", legend="outside-right", printed=True,
           note="the same time-series template, drawn as overlaid bars instead of "
                "polylines, twenty entries; the y axis now tops out at 15 because the "
                "routing flattens the queue"),
    figure(16, 1, "flowchart-or-schematic",
           caption(cap(16, "Figure 11: ", "Routing")),
           mention(16, first=15, style=["Figure 11"], count=1, pattern="as-shown-in",
                   lead=span(15, "The diagram of the queueing network", "Figure 11.")),
           path=S522, kind="other", labels=True,
           note="the third variant of the same two-station drawing: pre-check passengers "
                "may now queue before the regular check points, so the split line opens; "
                "no numerals at all on this one"),
    figure(16, 2, "bar",
           caption(cap(16, "Figure 12: ", "Routing")),
           mention(16, first=16, style=["Figure 12"], count=2, pattern="figure-n-shows",
                   lead=span(16, "Figure 12 demonstrates the results", "backpressure routing."),
                   trail=span(16, "Compared to Figure 10", "the same."),
                   read=1),
           path=S522, kind="other", legend="outside-right", printed=True,
           note="same overlaid-bar template as Figure 10, sixteen check nodes instead of "
                "twenty; the caption states no metric, so the numbers the chapter argues "
                "from sit in the body sentence"),
    figure(17, 1, "line",
           caption(cap(17, "Figure 13: ", "Suspicious Passengers)")),
           mention(17, first=16, style=["Figure 13a"], count=2, pattern="as-shown-in",
                   lead=span(16, "As illustrated in Figure 13a", "denotes the arrival"),
                   trail=span(16, "the longest line is almost the same", "rather stable."),
                   read=1),
           path=S531, kind="solution", panels=2, layout="1x2", printed=True,
           note="a (a)/(b) pair inside one measured region, one panel per routing "
                "algorithm; the caption names the dashed line, so the two markers are "
                "explained once for both panels"),
    figure(17, 2, "line",
           caption(cap(17, "Figure 14: ", "total)")),
           mention(17, first=16, style=["Figure 14"], count=1, pattern="parenthetical",
                   lead=span(16, "We also explore the optimal ratio", "Figure 14)")),
           path=S531, kind="solution", panels=2, layout="1x2", shared=True, printed=True,
           note="throughput | variance side by side against the same abscissa, no legend, "
                "secondary y axis on the right panel only; the condition of the experiment "
                "(16 check points in total) is printed in the caption, not on the plot"),
    figure(18, 1, "bar",
           caption(cap(18, "Figure 15: ", "Algorithm")),
           mention(18, first=18, style=["Figure 15"], count=2, pattern="as-shown-in",
                   lead=span(18, "The results of drift-plus-penalty", "Figure 15."),
                   trail=span(18, "This algorithm sacrifice", "pre-check users."),
                   read=1),
           path=S532, kind="solution", legend="outside-right", printed=True,
           note="the overlaid-bar template again, twenty entries, y axis back to 20: the "
                "penalised routing raises the backlogs it was supposed to protect"),
    figure(19, 1, "line",
           caption(cap(19, "Figure 16: ", "total)")),
           mention(19, first=18, style=["Figure 16"], count=1, pattern="parenthetical",
                   lead=span(18, "We explore the optimal ratio", "Figure 16)")),
           path=S532, kind="solution", panels=2, layout="1x2", shared=True, printed=True,
           note="the same throughput | variance pair as Figure 14 with different data; the "
                "figure is printed at the top of page 19, one page after the sentence that "
                "cites it, and it still belongs to the chapter it left behind"),
    figure(20, 1, "line",
           caption(cap(20, "Figure 17: ", "parameter V")),
           mention(20, first=20, style=["Figure 17"], count=1, pattern="as-shown-in",
                   lead=span(20, "The result of this experiment", "Figure 17."),
                   trail=span(20, "We can see that the throughput", "variance increases"),
                   read=1),
           path=S621, kind="sensitivity", legend="inside", printed=True,
           note="two metrics on two y axes in one frame instead of two panels: the left "
                "axis carries variance (0-1200) and the right throughput (4.50-7.50), and "
                "the legend sits inside the frame - the paper's only inside legend besides "
                "Figure 18"),
    table(21, 1, caption(cap(21, "Table 5: ", "systems"), numbering="Table N:"),
          mention(21, first=21, style=["Table 5"], count=1, pattern="direct",
                  lead=span(21, "Table 5 shows the variance", "normal system."),
                  trail=span(21, "We can see that the system which allows cutting",
                             "does not."),
                  read=1),
          grid(3, 3, header=1, numeric=2, txt=1, units_hdr=True, decimal=True, width="half"),
          path=S622, kind="other",
          note="three rows, units inside the header (Variance(min2), Throughput(PAX/min)), "
               "decimals aligned; the only table whose rows are experimental conditions "
               "rather than parameters"),
    figure(21, 3, "line",
           caption(cap(21, "Figure 18: ", "ratio")),
           mention(21, first=21, style=["Figure 18"], count=3, pattern="figure-n-shows",
                   lead=span(21, "Figure 18 shows the variance", "different ratios."),
                   trail=span(21, "We see from Figure 18", "of the airport."),
                   read=1),
           path=S623, kind="other", panels=2, layout="1x2", legend="inside", printed=True,
           note="one captioned exhibit printed as two measured regions: variance | "
                "throughput side by side, three-entry legend inside the right panel. The "
                "row's bbox is the left panel; the right panel is recorded as a fragment of "
                "the same exhibit, and the legend box nested in it as a second fragment"),
    figure(22, 1, "line",
           caption("Figure 19: System variance and throughput with respect to the variance "
                   "of arrival distribution"),
           mention(22, first=22, style=["Figure 19"], count=2, pattern="figure-n-shows",
                   lead=span(22, "Figure 19 illustrates how variance", "arrival distribution."),
                   trail=span(22, "Basically, Figure 19 tells us", "better performance."),
                   read=1),
           path=S624, kind="other", legend="inside", printed=True,
           source="typed-from-crop",
           note="same dual-axis single frame as Figure 17; the caption is typed from the "
                "crop because the typesetter hyphenated 'distri- bution' across a line break"),
]

for _n, _e in enumerate(ALL, 1):
    _e["place"]["doc_order"] = _n
_by_page: dict[int, list[dict]] = {}
for _e in ALL:
    _by_page.setdefault(_e["page"], []).append(_e)
for _entries in _by_page.values():
    for _i, _e in enumerate(_entries, 1):
        _e["place"]["page_order"] = _i

FIGURES = [e for e in ALL if "table" not in e]
TABLES = [e for e in ALL if "table" in e]

RULES = [
    "图族跟着论证任务走，不跟着数据走：9 张 line 全是“指标随时间或参数变化”的结果图，"
    "5 张 flowchart-or-schematic 全是模型示意，1 张 map-or-plan-view 是唯一一张用来"
    "交代参数来源的地图，唯一 1 张 histogram 只用在“拟合效果”这一处 [geometry.family]。",
    "同一张图在章节不同位置换渲染而模板不变：队列长度图 4 次用折线（Fig 6/7/8 与 Fig 13 "
    "的 a/b 对照），3 次用叠柱（Fig 10/12/15），族标注随之由 line 变 bar，但“时间在 x、"
    "每条队列一条序列、图例在右”三件事一字未改 [geometry.family][geometry.panel_layout]。",
    "图例位置由序列数决定：18–20 条队列序列的 5 张图一律 outside-right 排两列，"
    "2–3 条序列的 3 张图一律 inside，没有一张图例在下方或上方 [geometry.legend]。",
    "“两指标 + 一个自变量”的叙事有两种版式：取一两个代表性取值时用双 y 轴单框"
    "（Fig 17/19，legend=inside），要沿整个自变量扫描时拆成 left|right 两分面"
    "（Fig 14/16，panel_count=2，共享横轴）；两种版式的题注句式完全相同 "
    "[geometry.panel_count][geometry.legend]。",
    "分面只有两种用途：吞吐|方差的指标对（3 个条目），和一图两算法/两配置的 (a)/(b) 对照"
    "（Fig 1、Fig 13）；除 Fig 1 挂在第 2 章的队列定义上，其余 4 个都在方法章与敏感性章，"
    "第 4 章的结果段落一张分面图都没有 [place.section_path][geometry.panel_count]。",
    "共享坐标轴是分面图的选择性习惯：两个吞吐|方差对共用横轴（变量都是“TSA regular "
    "check points”），而 (a)/(b) 对照虽然共用 Time/min 却记为不共享——共享只在两分面"
    "比较同一自变量的不同指标时才声明 [geometry.shared_axes]。",
    "三维只出现一次，且不是数据的三维：唯一的 isometric 是曼谷机场的等距平面图，"
    "全文没有一个曲面或透视柱，变量维度最多到 2，所以 colorbar 也一次没用 [geometry.three_d]"
    "[geometry.colorbar]。",
    "框内印刷数字是折线/柱状模板的固定件：17 张图带坐标刻度与框内标签，只有 2 张不带——"
    "Fig 11 只有站名，Fig 5 只有楼层与指廊标号，两张都是不给任何计量的示意图 "
    "[geometry.printed_numbers]。",
    "题注位置是硬规矩：24 个条目 24 个在下，图与表一视同仁，没有一例在上 "
    "[caption.position]；编号一律 “Figure N:” / “Table N:” 加冒号 [caption.numbering]。",
    "题注只报题目不报参数：词数 3–18、句数恒为 1、没有一条写单位或结论，"
    "单位和实验条件要么进坐标轴、要么进表头、要么进方法句，只有 Fig 14/16 把"
    "“16 check points in total”塞进题注括注 [caption.words][caption.units][caption.conditions]。",
    "引出句式以 as-shown-in 为主（10 条，模板 “As Figure N demonstrates/demonstrated”），"
    "其次 direct（6 条）、figure-n-shows（3 条，“Figure N shows/demonstrates”）、"
    "parenthetical（3 条，正文句末括注 “(Figure N)”）[mention.lead_pattern]。",
    "一半以上的图在版面上就位才被提到：15 张首次提及页等于图页，7 张提前一页预告"
    "（引言句和正文分开排页），没有一张晚于图页才对上号 [mention.lead_pages]。",
    "图后解读句是模板化的两步：先 1 句“We can see/see from Figure N that …”读图，"
    "再 1 句解释原因；13 条条目 read_sentences=1，只有底线对照的 Fig 6 连读 2 句 "
    "[mention.read_sentences]。",
    "引用密度两极：12 张只被提 1 次，8 张被提 2 次，2 张被提 3 次（Fig 6、Fig 18，都是"
    "被反复回读的基准图），另有 2 个条目 0 引用——Table 3（记号表）与 Fig 2（拟合结果）全文无人指 "
    "[mention.count]。",
    "表型统一到一种：5 张表全是 boxed 外框加表头横线，无内竖线；无隔行底纹、无合并单元格、"
    "无对角表头 [table.rule_style][table.zebra][table.merged_cells][table.diagonal_header]。",
    "表头承担单位与精度：唯一 4 列表（验证表）把 (minute) 写进表头并把模型列小数对齐，"
    "两张 3 列结果表也把 Variance(min2)/Throughput(PAX/min) 写进表头 [table.units_in_header]"
    "[table.decimal_aligned]；表的宽度随行数走——两张 3 行小表只占半栏，"
    "10 行记号表与 6 行验证表占满栏 [table.width]。",
    "章节性质与展品量成正比：evaluation 章 4 件、solution 章 4 件、model 章 3 件，"
    "sensitivity 章只放 1 件最关键的参数扫描，记号表单独挂在章首模型节 [place.section_kind]。",
]

NOTE = (
    "24 exhibits on 25 pages: 19 figures and 5 tables against 26 measured regions and 2 "
    "exclusions. The two exclusions are both on page 21 and both belong to Figure 18 - the "
    "right-hand panel of that one captioned pair, and the three-entry legend box drawn "
    "inside it. Nine exhibits are cited once or not at all: Table 3 and Figure 2 carry no "
    "citing sentence anywhere in the paper, and Figures 2, 3, 5, 8, 11, 13 and 15 are each "
    "named a single time. Three captions are not text-layer substrings - Figures 7 and 8 "
    "share one interleaved text-layer line on page 12 and Figure 19 is hyphenated across a "
    "line break - so those three are typed from the crop."
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
    print("printed", dict(agg("printed_numbers")))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in ALL)))
    print("section", dict(Counter(" > ".join(e["place"]["section_path"]) for e in ALL)))
    for k in ("position", "numbering", "voice", "words", "sentences"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in ALL)))
    print("pattern", dict(Counter(e["mention"]["lead_pattern"] for e in ALL)))
    print("first", dict(Counter(e["mention"]["first_page"] for e in ALL)))
    print("count", dict(Counter(e["mention"]["count"] for e in ALL)))
    print("read", dict(Counter(e["mention"]["read_sentences"] for e in ALL)))
    print("area", sorted(e["place"]["area_frac"] for e in ALL))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in ALL)))
    print("rules", dict(Counter(t["table"]["rule_style"] for t in TABLES)))
    print("width", dict(Counter(t["table"]["width"] for t in TABLES)))
    print("rows", [(t["page"], t["table"]["rows"], t["table"]["cols"]) for t in TABLES])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
