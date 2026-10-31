"""Hand pass for P-D-2017-68942-f0b0893e (TSA checkpoint NetLogo study, 12 figures + 17 tables).

Shape of the paper: one schematic of the checkpoint zones (Fig 1), one Q-Q pair (Fig 2), one
arrival histogram (Fig 3), two NetLogo screenshots (Figs 4-5), four throughput line charts
(Figs 6-8 and 7), and five grouped-bar result charts (Figs 9-12). Seventeen tables, almost all
wait-time matrices around one average-throughput ratio table.

What the record has to say out loud:

1. The prose cites by the wrong numbers. Three sentences call the zone schematic "Figure 4";
   the WTMD bar chart on page 15 is announced and then read as "Figure 11"; the slow-traveller
   table is read as "Figure 15"; and section 8.1 refers to its own table as "Table ??" - a
   cross-reference that was never resolved before printing. The rows record the printed
   spellings; the notes say what the number actually points at.
2. Fifteen of the seventeen tables share one style: fully boxed grid with vertical rules on
   every column, a grey header row, no zebra striping, caption below. Not one table in the
   paper is booktabs. The deviation is Table 1, whose Zone column is merged into four tall
   cells with scattered grey row fills instead of a regular pattern.
3. Merged cells are the norm, not the exception: nine of seventeen tables merge the
   generation-probability column over a five-row block, and two tables stack a second header
   row (Tables 9 and 13).
4. Nine tables are never cited at all (1, 2, 3, 5, 8, 11, 12, 16, 17) and five figures never
   are (4, 5, 8, 10, 11) - among them both NetLogo screenshots.
5. The four figure blanks are two shapes only: a multi-series line chart with the legend
   inside the plot at the top right (Figs 6, 7, 8) and a grouped bar chart with a single
   horizontal legend row printed below the x-axis title (Figs 9, 10, 11, 12).
6. Tables 16 and 17 are the same grid printed twice, 30% and 40%, at the very end of the
   document before appendix A - captioned "WTMD 30%" and "WTM 40%", the second acronym
   truncated.

Usage: python -I tools/_dist_paper133.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2017-68942-f0b0893e"
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
    if _n not in HEAD:
        HEAD[_n] = _l


def P(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


EXCLUDED = [
    {"page": 1, "bbox": REG[(1, 1)], "reason": "not-an-exhibit",
     "note": "the MCM summary sheet, rendered as one full-page raster. It carries the team "
             "control number, the abstract and the office-use stub - no figure, no table, no "
             "artwork anywhere on the page."},
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


def mention(page: int, *, first: int | None = None, style: list[str] | None = None,
            count: int = 0, lead: str = "", pattern: str = "none", read: int = 0,
            trail: str = "") -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style or [],
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
           note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "other_note": None,
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
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(page: int, idx: int, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, note: str = "", numbered: bool = True) -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, idx, path, kind, numbered),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed", zebra: bool = False,
         merged: bool = False, diag: bool = False, units_hdr: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "column",
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
    q = t[i:_to_word_end(page, jend)].strip()
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def cap(page: int, marker: str, end: str, *, after: int = 0) -> str:
    t, i, _ = _find(page, marker, after)
    _, j, jend = _find(page, end, i)
    return t[i:_to_word_end(page, jend)].strip()


S1 = P("1")
S2 = P("2")
S31 = P("3", "3.1")
S32 = P("3", "3.2")
S41 = P("4", "4.1")
S52 = P("5", "5.2")
S53 = P("5", "5.3")
S6 = P("6")
S61 = P("6", "6.1")
S71 = P("7", "7.1")
S72 = P("7", "7.2")
S73 = P("7", "7.3")
S74 = P("7", "7.4")
S75 = P("7", "7.5")
S76 = P("7", "7.6")
S77 = P("7", "7.7")
S81 = P("8", "8.1")
S82 = P("8", "8.2")
S83 = P("8", "8.3")
S84 = P("8", "8.4")
S_APP = ["未编号标题：Appendix"]

ALL = [
    figure(2, 1, "flowchart-or-schematic",
           caption(cap(2, "Figure 1:", "TSA Screening Process")),
           mention(2, first=3, style=["Figure 4"], count=3,
                   lead="Airport security checkpoints can be divided into four major zones, as "
                        "demonstrated in Figure 4.",
                   pattern="parenthetical", read=1,
                   trail=span(3, "Our solution identifies the problems",
                              "shown above in Figure 4")),
           path=S1, kind="introduction", legend="inside",
           note="a four-band zone diagram of the checkpoint drawn as a NetLogo world with labels "
                "overlaid: blue Zone A with the two entrance cells, pale-grey Zone B, green "
                "Zone C and a small red Zone D. Two heavy blue block arrows only. A titled "
                "'Legend' box sits inside the artwork at the upper right with four glyph "
                "entries (TSA agent, luggage screening, millimeter wave body scanner, X-ray "
                "body scanner). No numeral anywhere, no axes, no scale. Colour carries the zone "
                "identity. The prose calls this drawing 'Figure 4' in all three citations"),
    figure(5, 1, "scatter",
           caption(cap(5, "Figure 2:", "body scan (right) times")),
           mention(5, first=5, style=["Figure 2"], count=1,
                   lead=span(5, "We used the Shapiro-Wilk normality test",
                             "given passenger data."),
                   pattern="parenthetical", read=1,
                   trail=span(5, "the Q-Q plots showed linear trends",
                              "deviations (Figure 2)")),
           path=S31, kind="assumption", panels=2, layout="1x2", shared=True, printed=True,
           note="two MATLAB Q-Q panels side by side, each with open-circle markers, a thin red "
                "reference line and printed axis titles ('Theoretical Quantiles', 'Sample "
                "Quantiles'). Both panels run x -2..2 and y 5..20, so the pair shares its scales; "
                "both are titled 'Normal Q-Q Plot', so only the caption says which is which. No "
                "legend, no gridlines, full frame"),
    figure(7, 1, "bar",
           caption(cap(7, "Figure 3:", "over time")),
           mention(7, first=4, style=["Figure 3"], count=2,
                   lead=span(4, "According to the given data, the arrival times",
                             "short time periods (Figure 3)."),
                   pattern="parenthetical", read=1),
           path=S41, kind="model", labels=True, printed=True,
           note="nine vertical bars in one steel-blue fill over the categorical axis 0:01-0:09, "
                "y 0-20, with the chart's own title 'Arrivals (all)' printed inside the frame. "
                "The caption promises 'PreCheck and regular' but the artwork draws a single "
                "series. One annotation only - the value 11.37 written against a horizontal "
                "reference line. No legend"),
    figure(8, 1, "photo-or-raster-image",
           caption(cap(8, "Figure 4:", "passengers are generated."), voice="active"),
           mention(8, style=[], count=0),
           path=S52, kind="model",
           note="a crop of the NetLogo world view only - no interface widgets, no monitors, no "
                "plot. Four colour bands, eight orange person glyphs, three red hexagons, three "
                "yellow WTMD bars and six brown station glyphs. Patch borders are not drawn, so "
                "there is no visible grid, and there is no axis, legend or colourbar"),
    figure(9, 1, "photo-or-raster-image",
           caption(cap(9, "Figure 5:", "simulation in progress."), voice="active"),
           mention(9, style=[], count=0),
           path=S53, kind="model",
           note="the whole NetLogo interface: about twenty-four green sliders and purple buttons "
                "in the left column, the world view in the centre with agents mid-queue, and ten "
                "monitor boxes at the right showing counts and averages. Numbers appear only as "
                "widget values and monitor readouts; nothing is plotted"),
    figure(10, 1, "line",
           caption(cap(10, "Figure 6:", "1221 conﬁguration"), units=True),
           mention(10, first=10, style=["Figure 6"], count=1,
                   pattern="parenthetical", read=1,
                   trail=span(10, "For conﬁguration 1221, the average throughput",
                              "0.36 and 0.54")),
           path=S6, kind="result", legend="inside", printed=True,
           note="four raw Excel-series lines, one per generation probability, in blue / "
                "red-orange / orange / green, identical width and no markers. Legend inside the "
                "plot at the upper right without a frame. Printed axis titles 'Throughput "
                "(PAX/min)' and 'Time (min)', y 0-16, x 0-250, light major gridlines both ways, "
                "chart title 'Average Throughput (1221)' inside. No data labels, no fit"),
    figure(12, 2, "line",
           caption(cap(12, "Figure 7:", "2243 conﬁguration"), units=True),
           mention(12, first=12, style=["Figure 7"], count=1,
                   pattern="parenthetical", read=1,
                   trail=span(12, "For conﬁguration 2243, the average throughput",
                              "0.54 and 0.72")),
           path=S6, kind="result", legend="inside", printed=True,
           note="same template as Figure 6 with the 2243 series: four lines, legend inside at "
                "the upper right, y 0-24 step 6, x 0-200 step 40, and the x title now reads "
                "'Time (minutes)' instead of 'Time (min)'"),
    figure(13, 2, "line",
           caption(cap(13, "Figure 8:", "varing numbers of PreCheck oﬃcers"), units=True),
           mention(13, style=[], count=0),
           path=S61, kind="result", legend="inside", printed=True,
           note="three lines (one, two and three PreCheck document-checkers), legend inside at "
                "the upper right, y 0-16, x 0-120. The in-chart title collapses to 'Average "
                "Throughput' with no configuration qualifier"),
    figure(15, 1, "bar",
           caption(cap(15, "Figure 9:", "Passing Through WTMDs.")
                   + " " + cap(15, "All data is expressed", "standard deviation.", after=1),
                   voice="passive"),
           mention(15, first=15, style=["Figure 11"], count=2,
                   lead="Figure 11 shows the results.", pattern="direct", read=1,
                   trail=span(15, "The beneﬁts of increasing WTMD usage",
                              "all generation probabilites.")),
           path=S73, kind="result", legend="below", printed=True,
           note="grouped vertical columns, four series (20/30/40/50% WTMD use), legend printed as "
                "one horizontal row below the x-axis title. y 'Average Wait Time (sec)' 0-4000 "
                "step 500, x 'Generation Probability' with five categories. No data labels. The "
                "sentence that introduces it and the sentence that reads it both call it "
                "'Figure 11'"),
    figure(17, 1, "bar",
           caption(cap(17, "Figure 10:", "with PreCheck.")
                   + " " + cap(17, "All data is expressed", "standard deviation.", after=1),
                   voice="passive"),
           mention(17, style=[], count=0),
           path=S76, kind="result", legend="below", printed=True,
           note="grouped columns, four series, legend in one horizontal row below the x-axis "
                "title, y 0-7000 step 1000, five x categories. The caption is word-for-word the "
                "same as Figure 11's"),
    figure(17, 2, "bar",
           caption(cap(17, "Figure 11:", "with PreCheck.", after=1)
                   + " " + cap(17, "All data is expressed", "standard deviation.", after=2),
                   voice="passive"),
           mention(17, style=[], count=0),
           path=S77, kind="result", legend="below", printed=True,
           note="same template as Figure 10 but visibly a different plot: three x categories "
                "(0.09 and 0.18 dropped), y 0-4000 instead of 0-7000, and a different colour "
                "assignment. Legend one horizontal row below the x-axis title. Its number is "
                "used in the prose for the WTMD chart on page 15"),
    figure(19, 2, "bar",
           caption(cap(19, "Figure 12:", "patdown probabilities.")
                   + " " + cap(19, "All data is expressed", "standard deviation.", after=1),
                   voice="passive"),
           mention(19, first=19, style=["Figure 12"], count=1, pattern="direct", read=1,
                   trail=span(19, "a 1% or 2% amount of travelers deferring a millimeter wave scan",
                              "not aﬀect the wait time standard deviations signiﬁcantly.")),
           path=S83, kind="result", legend="below", printed=True,
           note="grouped columns with three series (0%, 1% and 2% pat-down probability), legend "
                "as one widely spaced horizontal row below the x-axis title, y 0-4000 step 500, "
                "five x categories. No data labels"),
]

TABLES = [
    table(3, 1, caption(cap(3, "Table 1:", "screening process"), numbering="Table N:"),
          mention(3, style=[], count=0),
          grid(15, 3, merged=True, txt=3, numeric=0, width="full"),
          path=S2, kind="model",
          note="the zone/queue/process listing. Three columns, one header row and fourteen body "
                "rows, but four of those body rows are spacers: the Zone cell is merged over "
                "four rows for A, seven for B and three for C, and the Queue cell is merged over "
                "each queue's processes. Fully boxed with vertical rules; scattered light-grey "
                "fills on three body rows instead of a regular zebra band, plus a solid grey "
                "fill behind the merged zone cells. No numerals, no units"),
    table(5, 2, caption(cap(5, "Table 2:", "regular passengers"), numbering="Table N:"),
          mention(5, style=[], count=0),
          grid(15, 3, merged=True, units_hdr=True, numeric=1, txt=2, width="column"),
          path=S32, kind="assumption",
          note="fourteen body rows in three columns, zone cell merged per zone (A 2, B 7, C 2, "
                "D 3). Fully boxed with vertical rules, no zebra, grey fill only behind the "
                "merged zone cells. Unit written into the header as 'Time (s)'. Values are "
                "right-aligned but not decimal-aligned ('11.2' next to '2'), and one cell holds "
                "a hyphenated range ('5-7')"),
    table(10, 2, caption(cap(10, "Table 3:", "1221 conﬁguration"), numbering="Table N:"),
          mention(10, style=[], count=0),
          grid(3, 3, units_hdr=True, decimal=True, numeric=2, txt=1, width="column"),
          path=S6, kind="result",
          note="two data rows by three columns, header wrapped over two lines, fully boxed with "
                "vertical rules, no zebra (grey header row only). Units in the header on both "
                "value columns, decimals aligned to two places"),
    table(10, 3, caption(cap(10, "Table 4:", "1221 conﬁguration", after=1), numbering="Table N:"),
          mention(10, first=11, style=["Table 4"], count=1, pattern="direct", read=1,
                  lead=span(11, "From Table 4, it is clear",
                            "is line q3")),
          grid(11, 6, merged=True, decimal=True, numeric=4, txt=2, width="full"),
          path=S6, kind="result",
          note="ten data rows by six columns: two merged generation-probability blocks of five "
                "queue lines each. Fully boxed with a rule between every row; the merged "
                "probability cells and the header row are grey-filled, the body is white. No "
                "units in the header - 'sec' appears only in the caption. Decimals aligned"),
    table(11, 1, caption(cap(11, "Table 5:", "2243 conﬁguration"), numbering="Table N:"),
          mention(11, style=[], count=0),
          grid(5, 3, units_hdr=True, decimal=True, numeric=2, txt=1, width="column"),
          path=S6, kind="result",
          note="four data rows, three columns, fully boxed, grey header row, units in the "
                "header, decimals aligned. Never cited in the prose"),
    table(11, 2, caption(cap(11, "Table 6:", "2243 conﬁguration"), numbering="Table N:"),
          mention(11, first=12, style=["table 6"], count=1, pattern="parenthetical", read=1,
                  lead=span(12, "Our PreCheck passengers in table 6",
                            "bottleneck in the scanner queue")),
          grid(21, 4, merged=True, units_hdr=True, decimal=True, numeric=3, txt=1,
               width="column"),
          path=S6, kind="result",
          note="twenty data rows by four columns, four merged probability blocks of five lines, "
                "fully boxed. Header says '(PAX)' on both measured columns while the caption "
                "says these are wait times in seconds - the header unit and the caption unit "
                "disagree"),
    table(12, 1, caption(cap(12, "Table 7:", "2243 conﬁguration"), numbering="Table N:"),
          mention(12, first=12, style=["table 7"], count=1, pattern="direct", read=1,
                  lead=span(12, "From the regular passengers described in table 7",
                            "scanner queue (q2).")),
          grid(21, 4, merged=True, units_hdr=True, decimal=True, numeric=3, txt=1,
               width="column"),
          path=S6, kind="result",
          note="same grid as Table 6 (twenty rows, four merged blocks) and the same header/caption "
                "unit conflict: '(PAX)' in the header, '(sec)' in the caption. Starts at the top "
                "of page 12 but is not a continuation - Table 6 closed with its caption on the "
                "previous page"),
    table(13, 1, caption(cap(13, "Table 8:", "numbers of PreCheck oﬃcers"), numbering="Table N:"),
          mention(13, style=[], count=0),
          grid(4, 4, units_hdr=True, decimal=True, numeric=3, txt=1, width="column"),
          path=S61, kind="result",
          note="three data rows by four columns, fully boxed, grey header row, units in the "
                "header ('(sec)', '(sec)', '(PAX/min)'), decimals aligned. The prose reads the "
                "table without ever naming it"),
    table(14, 1, caption(cap(14, "Table 9:", "original throughputs"), numbering="Table N:"),
          mention(14, first=14, style=["Table 9"], count=1, pattern="figure-n-shows", read=0,
                  lead="Table 9 shows the change in average throughput from each of the "
                       "modiﬁcations."),
          grid(7, 6, header=2, merged=True, decimal=True, numeric=5, txt=1, width="full"),
          path=S71, kind="result",
          note="two header rows: 'Generation Probability' merged down both of them, 'More WTMD "
                "Use' merged across its three sub-columns 30/40/50. Five data rows, fully boxed. "
                "No units anywhere. Two missing values are printed as an en dash. The probability "
                "column is written as integers 9/18/36/54/72 where every other table writes "
                "0.09/0.18/..."),
    table(14, 2, caption(cap(14, "Table 10:", "an extra metal detector"), numbering="Table N:"),
          mention(14, first=14, style=["Table 10"], count=1, pattern="direct", read=1,
                  trail="Thus, we can conclude that adding an extra metal detector is strictly "
                        "beneﬁcial."),
          grid(4, 5, units_hdr=True, decimal=True, numeric=4, txt=1, width="full"),
          path=S72, kind="result",
          note="three data rows by five columns, the header block wrapped over four lines, fully "
                "boxed with a rule after every body row, grey header row only. '(sec)' repeated "
                "in each of the four measurement headers, decimals aligned"),
    table(16, 1, caption(cap(16, "Table 11:", "an Extra Scanner"), numbering="Table N:"),
          mention(16, style=[], count=0),
          grid(6, 6, units_hdr=True, numeric=5, txt=1, width="full"),
          path=S74, kind="result",
          note="five data rows by six columns at nearly the full text width, fully boxed, grey "
                "header row. Units in four of the headers; values right-aligned at two decimals "
                "but not decimal-aligned. The prose discusses its content while citing only "
                "Table 9"),
    table(16, 2, caption(cap(16, "Table 12:", "Faster Pat-downs"), numbering="Table N:"),
          mention(16, style=[], count=0),
          grid(6, 6, units_hdr=True, numeric=5, txt=1, width="full"),
          path=S75, kind="result",
          note="same grid and same width as Table 11 with the pat-down columns instead of the "
                "extra scanner. Fully boxed, grey header row, units in four headers, no decimal "
                "alignment"),
    table(18, 1, caption(cap(18, "Table 13:", "Old Throughputs"), numbering="Table N:"),
          mention(18, first=18, style=["Table ??"], count=1, pattern="figure-n-shows", read=0,
                  lead="Table ?? shows the change in average throughput from each new passenger "
                       "behavior."),
          grid(7, 5, header=2, merged=True, numeric=4, txt=1, width="column"),
          path=S81, kind="result",
          note="two header rows with 'More Pat-downs' merged over its 1% and 2% sub-columns, five "
                "data rows, fully boxed. About 40% of the text width - the narrowest table in the "
                "paper. The cross-reference that introduces it was never resolved before "
                "printing: it is literally 'Table ??'"),
    table(19, 1, caption(cap(19, "Table 14:", "Individuals Who Cut"), numbering="Table N:"),
          mention(19, first=18, style=["Table 14"], count=1, pattern="parenthetical", read=1,
                  lead=span(18, "Comparing the data at various arrival densities",
                            "standard deviations of wait time.")),
          grid(6, 6, units_hdr=True, numeric=5, txt=1, width="full"),
          path=S82, kind="result",
          note="five data rows by six columns, fully boxed, grey header row, '(sec)' in the four "
                "measurement headers, values right-aligned, no zebra"),
    table(20, 1, caption(cap(20, "Table 15:", "Slow Travelers"), numbering="Table N:"),
          mention(20, first=20, style=["Figure 15"], count=1, pattern="direct", read=1,
                  lead=span(20, "From Figure 15, we can see that the addition of slow travelers",
                            "standard deviation of screening process.")),
          grid(6, 6, units_hdr=True, numeric=5, txt=1, width="full"),
          path=S84, kind="result",
          note="five data rows by six columns, fully boxed. The last header has lost its word: it "
                "reads 'Standard Deviation w/ Travelers (sec)' where the parallel header reads "
                "'w/ Slow Travelers'. The sentence that reads the table calls it 'Figure 15'"),
    table(23, 1, caption(cap(23, "Table 16:", "WTMD 30%"), numbering="Table N:"),
          mention(23, style=[], count=0),
          grid(26, 4, merged=True, units_hdr=True, decimal=True, numeric=3, txt=1,
               width="column"),
          path=S_APP, kind="appendix", numbered=False,
          note="twenty-five data rows by four columns - five merged generation-probability "
                "blocks of five queue lines each - printed on its own page immediately before "
                "the appendix A code listing. Fully boxed with heavier rules between blocks, "
                "grey header and merged cells, '(PAX)' in the header. Never cited"),
    table(24, 1, caption(cap(24, "Table 17:", "WTM 40%"), numbering="Table N:"),
          mention(24, style=[], count=0),
          grid(26, 4, merged=True, units_hdr=True, decimal=True, numeric=3, txt=1,
               width="column"),
          path=S_APP, kind="appendix", numbered=False,
          note="the same grid as Table 16 reprinted at 40%, differing only in the numbers, in the "
                "caption percentage and in the acronym - the caption truncates WTMD to 'WTM'. One "
                "value breaks the column format: the 0.72 Total row prints '2038.1' with a single "
                "decimal where every other cell has two"),
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
    "版式跟着论证阶段走：1 张 zone 示意图负责“系统长什么样”，1 组 Q-Q 分面负责正态性检验，1 张"
    "到达直方图负责输入分布，2 张 NetLogo 截图负责“模型怎么跑”，4 张折线负责各组配置的吞吐"
    "时间序列，5 张分组柱负责改动的效果对比 [geometry.family]。",
    "折线与分组柱是两套固定模板，图例位置就是模板指纹：折线图（Fig 6/7/8）图例印在绘图区右上角"
    "内侧、带印刷轴题 'Throughput (PAX/min)'；分组柱（Fig 9/10/11/12）图例印成 x 轴标题下方的"
    "单行横排。legend 分布因此正好三三开：inside 4（含 Fig 1 自带的 'Legend' 框）、"
    "below 4、none 4 [geometry.legend]。",
    "全篇没有分面共享坐标轴以外的三维与色标：唯一的双联版是 Fig 2 的 Q-Q 对，两栏都跑 x −2..2、"
    "y 5..20，因此 shared_axes 只有这一条为 true；没有一张图带 colorbar，没有一张三维图 "
    "[geometry.panel_count][geometry.shared_axes][geometry.three_d][geometry.colorbar]。",
    "表格只有一种主样式：17 张表 17 张都是“外框 + 每条列线 + 每行横线”的全包围网格，灰底只在"
    "表头行和合并的生成概率列上，没有一张 booktabs、没有一张隔行底纹 [table.rule_style]"
    "[table.zebra]。",
    "合并单元格是常态不是例外：9 张表把“Generation Probability”纵向合并成五行一块，2 张表"
    "（Table 9、Table 13）叠了第二层表头并把子列横向合并 [table.merged_cells]"
    "[table.header_rows]。",
    "单位写在表头而不是题注：13 张表把 '(sec)'、'(PAX)'、'(PAX/min)' 写进表头，4 张不写"
    "（Table 1/13 是纯文字表、Table 9 以比值表示、Table 4 把 'sec' 留在题注里）；Table 6/7 "
    "出现表头写 PAX、题注写 sec 的自相矛盾 [table.units_in_header]。",
    "表的宽度随题量走而不是随列数走：8 张多列结果表占 60-100% 版心（width=full），9 张窄表只占"
    "40-60% 并居中（width=column）；全篇 17 张表一律纵向，没有一张横排，没有续表 [table.width]"
    "[table.orientation][table.continued]。",
    "题注位置是硬规矩：29 个条目 29 个在下，没有一例在上 [caption.position]；编号一律 "
    "'Figure N:' / 'Table N:' 半角冒号，无一处括注式编号 [caption.numbering]。",
    "题注分两类：图表题注是名词短语（4-24 词、多数 1 句、不写单位、不下结论），截图题注改写成主动句"
    "“This screenshot shows…”，4 张柱图题注则在句号后补一句被动式“All data is expressed as the "
    "mean + the standard deviation.”，句数因此是 1 句 25 条、2 句 4 条；voice 是 active 2、"
    "passive 4、none 23 "
    "[caption.voice][caption.sentences]。",
    "题注里一个变量也不点：variable_count 全为 0；(left)/(right)、'(sec)'、'(PAX/min)' 这类"
    "定位与单位信息单独走 units 字段，Fig 6/7/8 是唯一把单位写进题注的三张图 "
    "[caption.variables][caption.units]。",
    "指代整体错位：正文 3 处把 zone 示意图叫 'Figure 4'，WTMD 柱图（Fig 9）在前后两句里被叫 "
    "'Figure 11'，慢速旅客表（Table 15）被叫 'Figure 15'，8.1 节的交叉引用没解析就印成了 "
    "'Table ??'；按印刷拼写记 style，靠 note 说明实际指向哪个展品 [mention.style]。",
    "近半数展品全文无人指：12 张图里 5 张（Fig 4、5、8、10、11）与 17 张表里 9 张（Table 1、2、3、"
    "5、8、11、12、16、17）first_page=null，全靠“From Table 9…”这类只提一张表的句子代表整段结果 "
    "[mention.first_page]。",
    "首次提及页通常等于展品页（lead_pages=0 共 10 个），例外是 zone 示意图（排在 p2、正文到 p3 "
    "才提，lead_pages=-1）、到达直方图（p4 预告、p7 才印，lead_pages=3）与两张 1221/2243 的表"
    "（lead_pages=-1）[mention.lead_pages]。",
    "图前引出句很短、图后解读句最多一句：lead_pattern 分布 none 14、parenthetical 7、direct 6、"
    "figure-n-shows 2；read_sentences 为 1 的 13 个、0 的 16 个，没有一个条目连读两句 "
    "[mention.lead_pattern][mention.read_sentences]。",
    "章节性质决定密度：result 章（第 6/7/8 章）吃掉 20 件展品，model 章（第 2/4/5 章）4 件，"
    "assumption 2 件、introduction 1 件、appendix 2 件；敏感性没有单列章节，全部塞在 7.x 的"
    "改造小节里 [place.section_kind]。",
    "排除项只有一处：p1 是 MCM summary sheet 整页光栅，既无图也无表，记为 not-an-exhibit；"
    "除此之外 29 个测量区域全部对上 29 个印刷展品，没有分面碎片、没有重复框、没有题注条带 "
    "[place.area_frac]。",
]

NOTE = (
    "12 figures and 17 tables on 37 pages against 30 measured regions and 1 exclusion. The "
    "single exclusion is page 1, the MCM summary sheet rendered as one full-page raster; every "
    "other measured region is a printed exhibit, so this paper has no fragmentation at all - no "
    "panel split, no duplicate box, no caption strip. The prose cites by the wrong numbers: three "
    "sentences call the zone schematic 'Figure 4', the WTMD chart is introduced and read as "
    "'Figure 11', the slow-traveller table as 'Figure 15', and section 8.1 refers to its own "
    "table as 'Table ??'. Nine tables (1, 2, 3, 5, 8, 11, 12, 16, 17) and five figures (4, 5, 8, "
    "10, 11) are never cited. Tables 16 and 17 are one grid reprinted at 30% and 40%, parked "
    "before appendix "
    "A with no section heading of their own. Not one table is booktabs; all are fully boxed with "
    "vertical rules, grey headers and no zebra striping, and nine merge the generation-probability "
    "column over a five-row block."
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

    rows = ALL + TABLES
    print("figures", len(ALL), "tables", len(TABLES), "excluded", len(EXCLUDED))
    for k in ("family", "legend", "panel_count", "shared_axes", "three_d", "colorbar",
              "printed_numbers", "data_labels"):
        print(k, dict(Counter(e["geometry"][k] for e in ALL)))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in rows)))
    print("section", dict(Counter(" > ".join(e["place"]["section_path"]) for e in rows)))
    for k in ("position", "numbering", "voice", "words", "sentences", "units", "variables",
              "conditions", "concludes"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in rows)))
    for k in ("first_page", "lead_pages"):
        print("mention." + k, dict(Counter(e["mention"][k] for e in rows)))
    print("pattern", dict(Counter(e["mention"]["lead_pattern"] for e in rows)))
    print("count", dict(Counter(e["mention"]["count"] for e in rows)))
    print("read", dict(Counter(e["mention"]["read_sentences"] for e in rows)))
    print("rules", dict(Counter(t["table"]["rule_style"] for t in TABLES)))
    print("zebra", dict(Counter(t["table"]["zebra"] for t in TABLES)))
    print("merged", dict(Counter(t["table"]["merged_cells"] for t in TABLES)))
    print("hdr", dict(Counter(t["table"]["header_rows"] for t in TABLES)))
    print("units_hdr", dict(Counter(t["table"]["units_in_header"] for t in TABLES)))
    print("width", dict(Counter(t["table"]["width"] for t in TABLES)))
    print("orient", dict(Counter(t["table"]["orientation"] for t in TABLES)))
    print("cont", dict(Counter(t["table"]["continued"] for t in TABLES)))
    print("area", sorted(e["place"]["area_frac"] for e in rows))
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
