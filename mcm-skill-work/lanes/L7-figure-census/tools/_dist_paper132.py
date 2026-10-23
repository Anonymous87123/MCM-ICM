"""Hand pass for P-D-2017-67316-f37f83c8 (TSA checkpoint queueing, 16 figures + 6 tables).

Shape of the paper: a schematic of the two-lane queueing network (Figs 1-2), a Gantt view of
one passenger's path (Fig 3), density fits for the arrival and service processes (Figs 4-6),
a MATLAB flow chart (Fig 7), a single-day passenger-flow curve (Fig 8), an airport map
(Fig 9), three result tables printed as "figures" (Figs 10, 13, 14), one staffing chart
(Fig 11), one infographic (Fig 12) and two culture-comparison flow curves (Figs 15-16).

What the record has to say out loud:

1. Numbering is "Figure N" with no colon and no period; table captions are "Table N" the
   same way. Nothing is parenthesised.
2. Three of the sixteen "figures" are printed tables: Figure 10 (ruleless, zebra-banded,
   11 columns of positions needed), Figure 13 (missed flights over ten experiments) and
   Figure 14 (means and variances). Their rows carry family table-as-figure, which is the
   only place in the lane where the caption word and the exhibit form disagree.
3. Four of the six printed tables - Tables 1, 2, 3 and 4 - have no measured region at all.
   The layout pass returns paths on those pages (48 on page 9, 36 on page 11) but no
   rectangle, so they cannot be given a bbox; they are declared gaps here instead of being
   invented.
4. Figure 12 is one woven infographic returned as seventeen nested raster boxes: three
   slogan bars, a smiley disc and three speech bubbles. The row carries the disc, six boxes
   are recorded as fragments of the one drawing and ten as duplicates of those six.
5. Three captions (Figs 6, 8, 9) are printed as a band that the detector also returns as a
   raster region; those three bands are excluded as caption-background.
6. Captions print below every exhibit. Captions for Figures 6, 8, 9, 15 and 16 are typed
   from the crop: Figure 6 is hyphenated across a line, Figure 8 and Figure 9 wrap around a
   two-column body, and Figures 15/16 interleave on one text-layer line and carry mangled
   math italics.

Usage: python -I tools/_dist_paper132.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2017-67316-f37f83c8"
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


# --- exclusions ----------------------------------------------------------------
_CAPTION_BAND = ("the caption band of {fig}, printed as a strip the detector also returns as a "
                 "raster region. It carries no artwork, only the caption line that the row "
                 "already stores.")

EXCLUDED = [
    {"page": 3, "bbox": REG[(3, 1)], "reason": "fragment-of-other", "note": "dummy"},
]
EXCLUDED = [
    {"page": 4, "bbox": REG[(4, 1)], "reason": "fragment-of-other",
     "note": "the tail of row 1 of the unnumbered symbol table: the table starts on page 3 "
             "and its first Specification cell is broken by the page break, so this band is "
             "the continuation of the same row, not a second table."},
    {"page": 4, "bbox": REG[(4, 2)], "reason": "fragment-of-other",
     "note": "the Γ(α) row of the same symbol table, returned as its own band because the "
             "zebra fill is drawn per row rather than as one block."},
    {"page": 7, "bbox": REG[(7, 2)], "reason": "caption-background",
     "note": _CAPTION_BAND.format(fig="Figure 6")},
    {"page": 10, "bbox": REG[(10, 2)], "reason": "caption-background",
     "note": _CAPTION_BAND.format(fig="Figure 8")},
    {"page": 12, "bbox": REG[(12, 2)], "reason": "caption-background",
     "note": _CAPTION_BAND.format(fig="Figure 9")},
    {"page": 17, "bbox": REG[(17, 1)], "reason": "not-an-exhibit",
     "note": "a letter to the security manager set inside a drawn green frame. The frame is "
             "real, but the block carries no number, no caption and no artwork - it is body "
             "text in a box, and the box breaks across the page break."},
    {"page": 18, "bbox": REG[(18, 1)], "reason": "fragment-of-other",
     "note": "the continuation of the framed letter that starts on page 17; the side rails "
             "and the closing bottom rail are part of the same box."},
]

_FRAG = {
    2: "the first slogan bar ('Fewer missed flights!') of Figure 12",
    3: "the first speech bubble ('Great! Fewer risks!') of Figure 12",
    7: "the second slogan bar ('Longer remaining time!') of Figure 12",
    8: "the second speech bubble ('Easy boarding.') of Figure 12",
    12: "the third slogan bar ('Smaller variance!') of Figure 12",
    13: "the third speech bubble ('Sounds fair!') of Figure 12",
}
_DUP = {
    4: 2, 6: 2, 5: 3, 9: 7, 11: 7, 10: 8, 14: 12, 15: 12, 16: 13, 17: 13,
}
for _idx, _txt in _FRAG.items():
    EXCLUDED.append({
        "page": 14, "bbox": REG[(14, _idx)], "reason": "fragment-of-other",
        "note": f"{_txt}, returned as a separate raster box inside the one drawing.",
    })
for _idx, _src in _DUP.items():
    EXCLUDED.append({
        "page": 14, "bbox": REG[(14, _idx)], "reason": "duplicate",
        "note": f"a near-exact copy of the box recorded at p14 r{_src}; the extractor emits "
                "each element of the Figure 12 collage more than once.",
    })


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


def caption(v: str, *, numbering: str = "Figure N", cond: bool = False,
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
          kind: str, source: str = "text-layer", note: str = "",
          numbered: bool = True) -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "place": place(page, idx, path, kind, numbered),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed", zebra: bool = False,
         merged: bool = False, diag: bool = False, units_hdr: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "full",
         orient: str = "portrait", continued: bool = False, note_sentence: str = "") -> dict:
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
        "note_sentence": note_sentence,
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
S12 = P("1.2")
S41 = P("4.1")
S43 = P("4.3")
S431 = P("4.3", "4.3.1")
S433 = P("4.3", "4.3.3")
S52 = P("5.2")
S71 = P("7.1")
S812 = P("8.1.2")
S821 = P("8.2.1")
S822 = P("8.2.2")
S91 = P("9.1")
S92 = P("9.2")
S101 = P("10.1")
S_SYM = ["未编号标题：Symbols and Notations"]

ALL = [
    figure(3, 1, "flowchart-or-schematic",
           caption(cap(3, "Figure 1 ", "number of servers."), voice="active"),
           mention(3, first=3, style=["the above ideas"], count=1,
                   lead=span(3, "The following diagram illustrate", "more visual way:")),
           path=S12, kind="introduction",
           note="three-column block diagram: an 'Impacts' column, a stacked 'Improving "
                "Directions' column (Passenger Arrival / Service Pattern / Queueing "
                "Discipline) and a 'Modifications & Measures' bullet column, with a grey "
                "'Culture-related Factors' band under the middle stack. Two clip-art icons "
                "(clock, scales). No legend, no axes, no numbers"),
    figure(4, 3, "flowchart-or-schematic",
           caption(cap(4, "Figure 2 ", "checkpoint")),
           mention(4, first=4, style=["the diagram above"], count=1, pattern="as-shown-in",
                   trail=span(4, "The detailed security check process",
                              "in the diagram above."),
                   read=1),
           path=S41, kind="model",
           note="floor-plan layout with four lettered blocks A-D in a 2x2 arrangement: "
                "columns 'Precheck Process' and 'Non-precheck Process', rows 'Queueing Phase "
                "1' and 'Queueing Phase 2', with Exit and Additional Screening at the bottom. "
                "Person pictograms on the paths, dashed panel outlines. Only letters are "
                "printed, never a number"),
    figure(5, 1, "flowchart-or-schematic",
           caption(cap(5, "Figure 3 ", "sequence diagram")),
           mention(5, first=4, style=["procedure sequence diagram", "Figure 3"], count=2,
                   lead=span(4, "To better clarify the whole process",
                             "is given below:"),
                   read=0),
           path=S41, kind="model", legend="below",
           note="Gantt-style sequence diagram: two stacked rows of chained segments A-E and "
                "F-H over a faint vertical time grid, with a yellow hatch marking Phase 1. "
                "The key is not a legend box but eight running-text lines printed after the "
                "caption ('A: time waiting for the document check, ... H: other possible body "
                "checks'), so legend=below with eight entries. No numeric scale anywhere"),
    figure(6, 2, "histogram",
           caption(cap(6, "Figure 4 ", "non-pre-check arrivals")),
           mention(6, first=6, style=["histograms above"], count=1, pattern="as-shown-in",
                   trail=span(6, "According to the histograms above", "exponential distribution"),
                   read=1),
           path=S431, kind="model", printed=True,
           note="six bars over a 0-80 second axis, y 0-20, tan fill with a darker outline, no "
                "fitted curve, no axis titles. The body text never names Figure 4 or Figure 5 "
                "- it refers to 'the histograms above'"),
    figure(6, 1, "histogram",
           caption(cap(6, "Figure 5 ", "pre-check arrivals")),
           mention(6, first=6, style=["histograms above"], count=1, pattern="as-shown-in",
                   trail=span(6, "According to the histograms above", "exponential distribution"),
                   read=1),
           path=S431, kind="model", printed=True,
           note="seven bars over a 0-50 second axis, y 0-30. Printed as its own figure with "
                "its own caption beside Figure 4, not as its second panel: the two frames "
                "differ in width, in x range and in bin width, so bar heights are not "
                "comparable across the pair"),
    figure(7, 1, "histogram",
           caption("Figure 6 Histogram of the service time in Phase 2, to- gether with a PDF "
                   "plot of an Erlang distribution."),
           mention(7, first=7, style=["the histogram"], count=1,
                   lead="besides the histogram does not obey ex- ponential distribution, "
                        "apparently."),
           path=S433, kind="model", printed=True, source="typed-from-crop",
           note="four wide bins over 0-80 s, y 0-0.030, pale bars with black outlines and one "
                "blue Erlang density curve overlaid; no legend, so the curve is identified "
                "only by the caption. Caption typed from the crop because 'together' is broken "
                "across a line as 'to- gether'"),
    figure(8, 1, "flowchart-or-schematic",
           caption(cap(8, "Figure 7 ", "simulation speciﬁcation")),
           mention(8, style=[], count=0,
                   lead=span(8, "To build up the numeric solution", "Erlangian queueing.")),
           path=S52, kind="model",
           note="top-to-bottom flow chart from a 'Begin' terminator to an 'End' terminator "
                "through twelve process boxes and two decision diamonds (blue process, green "
                "decision, orange terminator). No legend box, no axes, no numbers. The paper "
                "never names Figure 7"),
    figure(10, 1, "line",
           caption("Figure 8 Varying passenger ﬂow in a time period, from 6:30 a.m. to 16:40 "
                   "p.m., O’Hare International Airport, Jan. 18, 2017"),
           mention(10, first=11, style=["Figure 8"], count=1, pattern="parenthetical",
                   trail=span(11, "The shown plotted graph (Figure 8)",
                              "to 16:40 p.m."),
                   read=1),
           path=S71, kind="model", printed=True, source="typed-from-crop",
           note="one noisy single-series curve inside a four-sided frame, x 0-700, y 300-1000, "
                "no axis titles, no legend, no markers. Caption typed from the crop: it wraps "
                "around the two-column body, so the text layer interleaves caption and body"),
    figure(12, 1, "map-or-plan-view",
           caption("Figure 9 O’Hare Terminal Map, © 2012 Chicago Department of Aviation, URL: "
                   "http://www.ﬂychicago.com/OHare/EN/AtAirport/map/default.aspx (Chicago "
                   "Department of Aviation, 2012)"),
           mention(12, first=12, style=["the O’Hare terminal map"], count=1,
                   lead=span(12, "Security checkpoints to terminals",
                             "the O’Hare terminal map.")),
           path=S812, kind="solution", source="typed-from-crop",
           note="pasted bitmap of the airport plan (soft resampling, faint uniform grid), "
                "terminals labelled 1/2/3/5 with parking glyphs, colour used semantically per "
                "terminal. No axes, no scale bar, no legend. The caption carries the source "
                "URL and is typed from the crop for the same wrap reason as Figure 8"),
    figure(13, 1, "table-as-figure",
           caption(cap(13, "Figure 10 ", "queue length converge")),
           mention(13, first=12, style=["Our result is"], count=1,
                   lead=span(12, "We trial the number of servers",
                             "find the appropriate ratio.")),
           path=S821, kind="result", printed=True,
           note="a printed table published under a figure number: six rows (header + five) by "
                "eleven columns, no rules at all, separation by alternating light-blue zebra "
                "bands only, units written inside the header ('(min)' and '/h'), centred "
                "values. One entry reads '6172' where its neighbours are of order 10-100"),
    figure(13, 2, "line",
           caption(cap(13, "Figure 11 ", "in blue and Phase 2 in green")),
           mention(13, first=13, style=["every hour"], count=1,
                   lead="we evaluate the duty assignment at each checkpoint every hour.",
                   trail=span(13, "Allocating fewer staﬀ at the troughs",
                              "at relatively low cost."),
                   read=1),
           path=S822, kind="result", printed=True,
           note="two series with round markers on a fine both-ways grid, x labelled with ten "
                "clock times 6:30 to 15:30, y 0-7. No legend box and no axis titles: series "
                "identity is given only by the caption ('Phase 1 in blue and Phase 2 in "
                "green')"),
    figure(14, 1, "other",
           caption(cap(14, "Figure 12 ", "Passenger satisfaction")),
           mention(14, first=14, style=["the above aspects"], count=1,
                   lead=span(14, "We now prove that this approach",
                             "with our simulation.")),
           path=S91, kind="result",
           other_note="a drawn infographic rather than a chart: three slogan bars, a smiley "
                      "disc and three speech bubbles joined by a spray of droplets, with the "
                      "slogans set as artwork text and no axis, scale or number anywhere",
           note="the detector returns this one drawing as seventeen nested raster boxes. The "
                "row carries the smiley disc at the centre; the three bars and three bubbles "
                "are recorded as fragments of the same drawing and ten further boxes as "
                "duplicates of those six"),
    figure(15, 1, "table-as-figure",
           caption(cap(15, "Figure 13 ", "missed their ﬂights.")),
           mention(15, first=15, style=["Our results are as follows"], count=1,
                   lead="Our results are as follows:",
                   trail="10 experiments are done here.", read=1),
           path=S91, kind="result", printed=True,
           note="the second table published as a figure: three rows by twelve columns, one "
                "italic stub column without vertical rules plus eleven numeric columns, a "
                "header rule, a box around the data block and a uniform light-green fill "
                "rather than zebra stripes"),
    figure(15, 2, "table-as-figure",
           caption(cap(15, "Figure 14 ", "remaining time")),
           mention(15, first=15, style=["And the means and the variances of remaining time"],
                   count=1, lead="And the means and the variances of remaining time:",
                   trail=span(15, "Means are almost the same", "won’t vary"),
                   read=1),
           path=S91, kind="result", printed=True,
           note="the third table published as a figure: three rows by three columns, header "
                "rule plus a box around the data block, light-green data cells, variance "
                "written in scientific notation (6.8787 x 10^6). No unit anywhere"),
    figure(16, 1, "line",
           caption("Figure 15 Smooth passenger ﬂow, μ is 150 minutes earlier the departure, "
                   "and σ = 40.", cond=True, vars_=2),
           mention(16, first=16, style=["the following plotted graph"], count=1,
                   pattern="as-shown-in",
                   lead=span(16, "Case for countries that are not so punctual",
                             "the following plotted graph.")),
           path=S101, kind="result", printed=True, source="typed-from-crop",
           note="single thin blue curve in a four-sided frame with inward ticks, x 0-600, "
                "y 500-1100, no axis titles and no legend. Caption typed from the crop: it and "
                "Figure 16's caption are interleaved on one text-layer line and the mu/sigma "
                "glyphs come through as private-use characters"),
    figure(16, 2, "line",
           caption("Figure 16 Rough passenger ﬂow, where μ is 90 minutes earlier, and "
                   "σ = 20.", cond=True, vars_=2),
           mention(16, first=16, style=["the following plotted graph"], count=1,
                   pattern="as-shown-in",
                   lead=span(16, "Case for countries that are not so punctual",
                             "the following plotted graph.")),
           path=S101, kind="result", printed=True, source="typed-from-crop",
           note="same frame and x range as Figure 15 with y 200-1400; the two curves are "
                "printed side by side but numbered separately, so each gets its own row"),
]

TABLES = [
    table(3, 2, caption("", numbering="none"),
          mention(3, style=[], count=0),
          grid(9, 2, header=1, rules="no-rules", zebra=True, txt=2, numeric=0,
               continued=True),
          path=S_SYM, kind="assumption", source="none", numbered=False,
          note="eight data rows under one header row, two columns, no box and no vertical "
               "rules, one thin rule under the header, alternating light-grey zebra bands. The "
               "first row is severed by the page break and resumes on page 4 without a "
               "repeated header; that continuation band and the Γ(α) row are recorded as "
               "fragments of this row's table"),
    table(13, 3, caption(cap(13, "Table 5 ", "done for 5 times"), numbering="Table N"),
          mention(13, first=13, style=["The test is done via simulation"], count=1,
                  lead="A sensitivity test is made for our model. The test is done via "
                       "simulation.",
                  trail=span(14, "We find that when the passenger flow decreases",
                             "deceases by 69.9%."),
                  read=1),
          grid(4, 4, header=1, rules="boxed", zebra=True, numeric=3, txt=1,
               note_sentence="Table 5 Sensitivity test result, simulations for each case are "
                             "done for 5 times"),
          path=P("8.2.3"), kind="sensitivity",
          note="four rows by four columns: one stub column plus three experimental conditions "
               "(Original / Decreased flow / Increased service ability). Full box with column "
               "and row rules, alternating light-green zebra below the header, no units, "
               "centred values"),
    table(15, 3, caption("Table 6 Number of passengers that missed the ﬂight (10 hours) and "
                         "variance of remaining time, α = 0.5", numbering="Table N"),
          mention(15, first=15, style=["Below is our result"], count=1,
                  lead="Below is our result.",
                  trail=span(15, "We find the partial priority discipline",
                             "raising passenger satisfaction."),
                  read=1),
          grid(4, 3, header=1, rules="boxed", zebra=True, numeric=2, txt=1),
          path=S92, kind="result", source="typed-from-crop",
          note="four rows by three columns, one unstubbed header cell plus the two measured "
               "columns; rules run full width across the stub, vertical rules only inside the "
               "data block; the first and third data rows are tinted and the middle row is "
               "white. Units appear only in the caption ('10 hours'). Caption typed from the "
               "crop because the alpha glyph is a math italic"),
]

for _n, _e in enumerate(ALL + TABLES, 1):
    _e["place"]["doc_order"] = _n
_by_page: dict[int, list[dict]] = {}
for _e in ALL + TABLES:
    _by_page.setdefault(_e["page"], []).append(_e)
for _entries in _by_page.values():
    for _i, _e in enumerate(_entries, 1):
        _e["place"]["page_order"] = _i

RULES = [
    "版式跟着论证阶段走：4 张 flowchart-or-schematic 分别承担“总纲（Fig 1）、检查点结构（Fig "
    "2）、单个旅客流程（Fig 3）、仿真程序（Fig 7）”，3 张 histogram 全部用在“数据服从什么分布”"
    "这一步，4 张 line 全部是扫描或对比结果，3 张 table-as-figure 把结果直接印成表 [geometry.family]。",
    "题注词与展品形态会脱钩：Fig 10/13/14 印刷在“Figure N”编号下，实际是表格网格，"
    "family 记为 table-as-figure；另外 6 张真实表格里，只有 Table 5、Table 6 与无编号记号表"
    "三张在版面上有网格，Table 1—4 检测器一个矩形也不给，登记为缺口 [geometry.family]。",
    "图例在本篇几乎不用：16 张图里只有 Fig 3 有图例，而且是“图注之后接八行 A:–H: 正文”，"
    "记为 legend=below、8 个条目；Fig 11 的两条序列身份、Fig 6 的曲线身份都只写在题注里，"
    "版面上没有图例框。legend 分布因此是 below 1 个、none 15 个 [geometry.legend]。",
    "没有分面：16 张图 16 个 panel_count=1，左右并排的两张图各自编号（Fig 4/Fig 5、"
    "Fig 15/Fig 16），所以 shared_axes 一律为 false——本篇的并排版式不是分面而是两个独立条目 "
    "[geometry.panel_count][geometry.shared_axes]。",
    "三维为零、色标为零：全篇没有曲面、透视柱或色标，热图只出现在表格的底色上而不是"
    "数据映射上 [geometry.three_d][geometry.colorbar]。",
    "框内数字由坐标轴决定：10 张带刻度，6 张不带——Fig 1 只有文字分栏、Fig 2 只有 A–D 字母、"
    "Fig 3 只有 A–H 片段与一条无标尺的时间网格、Fig 7 只有流程框、Fig 9 只有航站楼名、"
    "Fig 12 只有标语；没有任何一张图把数值标在数据点上 [geometry.printed_numbers]"
    "[geometry.data_labels]。",
    "题注位置是硬规矩：19 个条目 19 个在下，没有一例在上 [caption.position]；"
    "编号一律“Figure N”/“Table N”，既没有冒号也没有句点，全篇没有一处括注式编号 "
    "[caption.numbering]。",
    "题注是短标签而不是句子：词数 4-24、句数 1（唯一的 0 词 0 句是无编号记号表，它根本没有"
    "题注），19 条里没有一条写单位、没有一条下结论；"
    "单位要么写进表头（'Time since the initial (min)'、'Passenger flow /h'），"
    "要么写进题注括注（Table 6 的 '(10 hours)'）[caption.words][caption.units]"
    "[caption.concludes]。",
    "参数进了题注就会点变量：Fig 15/16 把“μ is 150 minutes earlier…and σ = 40”整句塞进题注，"
    "variables=true、variable_count=2、conditions=true，是 19 条里唯一给条件的两条；"
    "其余 17 条只报题目 [caption.variables][caption.conditions]。",
    "引用靠方位指代：19 个条目里只有 Fig 3 与 Fig 8 被编号点过名，其余 17 个靠“the above "
    "ideas”“the diagram above”“the histograms above”“Our result is…”“Below is our result.”"
    "这类指代，因此 lead_pattern 以 none 为主（13 条），as-shown-in 5 条、parenthetical 1 条"
    "[mention.lead_pattern][mention.count]。",
    "首次提及页经常早于图页：Fig 3 与 Fig 10 在前一页的正文里就被预告（lead_pages=1），"
    "Fig 8 反而晚一页才点名（lead_pages=-1）；其余 14 个 lead_pages=0，"
    "另有 2 个条目（Fig 7 与记号表）全文无人指，first_page=null [mention.lead_pages]。",
    "图前引出句与图后解读句都不超过一句：14 个条目有图前句、9 个有图后解读句，"
    "read_sentences 分布是 1 句 9 个、0 句 10 个，没有一个条目读到第 2 句 "
    "[mention.read_sentences]。",
    "章节性质与展品量：result 章（第 8/9/10 章）8 件、model 章（第 4/5/7 章）7 件、"
    "solution 与 introduction 各 1 件、sensitivity 只放 1 张表、assumption 只有无编号记号表 "
    "1 件 [place.section_kind]。",
    "排除项来自三处而不是一处：16 个是 Fig 12 拼贴图里被重复量出的图形块（6 fragment + 10 "
    "duplicate），3 个是印成条带的题注（Fig 6/8/9），其余 4 个是记号表的跨页续行两段与"
    "跨页绿框信函两段 [place.area_frac]。",
]

NOTE = (
    "16 figures and 3 tables on 22 pages against 42 measured regions and 23 exclusions. Three "
    "of the sixteen figures are printed tables (Figures 10, 13, 14) and carry family "
    "table-as-figure. Four of the six printed tables - Tables 1, 2, 3 and 4 - have no measured "
    "region: the layout pass returns paths but no rectangle on those pages, so no bbox exists "
    "for them and they are declared gaps rather than invented. Figure 12 is one woven "
    "infographic returned as seventeen nested rasters: the row carries the smiley disc, six "
    "boxes are fragments of the same drawing and ten are duplicates. Three caption bands "
    "(Figures 6, 8, 9) are excluded as caption-background because the detector also returns "
    "the printed caption strip as a raster. Five captions are typed from the crop: Figure 6 is "
    "hyphenated across a line, Figures 8 and 9 wrap around a two-column body, and Figures 15 "
    "and 16 interleave on one text-layer line with mangled math italics. The prose names only "
    "two of the nineteen exhibits by number."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ALL,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}


def main() -> int:
    from collections import Counter

    def agg(key: str, bucket: str = "geometry") -> Counter:
        return Counter(e[bucket][key] for e in ALL)

    rows = ALL + TABLES
    print("figures", len(ALL), "tables", len(TABLES), "excluded", len(EXCLUDED))
    for k in ("family", "legend", "three_d", "colorbar", "printed_numbers", "panel_count",
              "shared_axes", "data_labels"):
        print(k, dict(agg(k)))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in rows)))
    print("section", dict(Counter(" > ".join(e["place"]["section_path"]) for e in rows)))
    for k in ("position", "numbering", "voice", "words", "sentences", "variables",
              "variable_count", "conditions", "units", "concludes"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in rows)))
    print("pattern", dict(Counter(e["mention"]["lead_pattern"] for e in rows)))
    print("first", dict(Counter(e["mention"]["first_page"] for e in rows)))
    print("lead_pages", dict(Counter(e["mention"]["lead_pages"] for e in rows)))
    print("count", dict(Counter(e["mention"]["count"] for e in rows)))
    print("read", dict(Counter(e["mention"]["read_sentences"] for e in rows)))
    print("area", sorted(e["place"]["area_frac"] for e in rows))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in rows)))
    print("source", dict(Counter(e["caption_source"] for e in rows)))
    print("rules", dict(Counter(t["table"]["rule_style"] for t in TABLES)))
    print("zebra", dict(Counter(t["table"]["zebra"] for t in TABLES)))
    print("grids", [(t["page"], t["table"]["rows"], t["table"]["cols"]) for t in TABLES])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
