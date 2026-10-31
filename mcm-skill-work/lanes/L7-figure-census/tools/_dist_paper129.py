"""Hand pass for P-D-2017-55285-1835cc0b (airport security-check queuing models, 31 figures + 2 tables).

Shape of the paper: assumptions and a notation table, then a basic model (inflow, attribute
generation, queuing, screening), then its results chapter, then three modifications (MPL,
PBQ, SP), each with a design schematic followed by effectiveness charts, then a sensitivity
chapter with contour maps, then an appendix chapter that holds seven plates the body never
cites.

What the record has to say out loud:

1. The paper runs one chart template per question and reuses it: total-time curves, then the
   same panel again for the standard deviation. Every pair is (T_avg, sigma_T) at the same
   abscissa, printed side by side, and the second of each pair is captioned "Standard
   Deviation" — the pairing is the paper's unit of evidence, not the single chart.
2. Four exhibits are pies with the six process shares, and the pie is used exactly where the
   question is "what fraction of the time went where" (3.3.2 and its before/after pair in
   4.1). Above four slices the authors switch to a 2-D contour instead (Fig 24, Figs 27-31),
   so the exhibit family follows the number of things being compared, not the data type.
3. Three exhibits are 3-D bar fields over the two advance-time parameters (Fig 16, Figs 25,
   26) and two are filled contours over the same parameters (Fig 24). The 3-D version is used
   for T_avg with a dense parameter grid, the contour for the difference between two
   passenger classes.
4. Body chapters carry a citation for every exhibit they print except three: Fig 3, Fig 10 and
   Fig 14 have no citing sentence at all, and the seven appendix plates (Figs 25-31) are
   never cited anywhere. A chart can exist in this paper without a sentence pointing at it.
5. Numbers printed inside the frame are a habit: Figs 2, 4 and 5 carry fitted-equation and
   statistics boxes, Figs 15 and 16 carry a title line inside the frame, and the two 3-D
   fields carry no key at all, so colour encodes height without saying so.
6. Captions print below every figure and above both tables, numbered "Figure N:" / "Table N:".
7. Two captions are broken by the authors, not by the extractor: Figs 13 and 14 carry the same
   caption text ("The Total Time curves under PBQ Model of Different Groups") although the
   right-hand chart plots sigma_T, and Figure 16's caption runs straight into the next body
   sentence ("...of the three groups do not match the relevant flow volumn of passengers, it
   does not have negative effects.") which is prose, not caption.

Usage: python -I tools/_dist_paper129.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2017-55285-1835cc0b"
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

# section labels, taken verbatim from the context index so the stored path is the printed one
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
    {
        "page": 8, "bbox": REG[(8, 3)], "reason": "fragment-of-other",
        "note": "one of seven bitmaps pasted inside Figure 1: the tall 'Step 7 / Additional "
                "Screen' block of the queuing diagram. The whole diagram is one raster "
                "region; these are the pieces it is assembled from.",
    },
    {
        "page": 8, "bbox": REG[(8, 4)], "reason": "fragment-of-other",
        "note": "the 'Step 1 / Reach Airport' passenger column pasted inside Figure 1.",
    },
    {
        "page": 8, "bbox": REG[(8, 5)], "reason": "fragment-of-other",
        "note": "the 'Step 2 / Wait For Document Check' block pasted inside Figure 1.",
    },
    {
        "page": 8, "bbox": REG[(8, 6)], "reason": "fragment-of-other",
        "note": "the 'Step 3 / Take Document Check' block pasted inside Figure 1.",
    },
    {
        "page": 8, "bbox": REG[(8, 7)], "reason": "fragment-of-other",
        "note": "the 'Step 4 / Wait For Screen' block pasted inside Figure 1.",
    },
    {
        "page": 8, "bbox": REG[(8, 8)], "reason": "fragment-of-other",
        "note": "the 'Step 5 / Prepare For Screen' block pasted inside Figure 1.",
    },
    {
        "page": 8, "bbox": REG[(8, 9)], "reason": "fragment-of-other",
        "note": "the 'Step 6 / Screen' block pasted inside Figure 1.",
    },
    {
        "page": 14, "bbox": REG[(14, 2)], "reason": "fragment-of-other",
        "note": "one of five passenger-group bitmaps pasted inside Figure 12: the first lane "
                "block of the PBQ diagram. The diagram is one vector cluster with these "
                "bitmaps laid over it.",
    },
    {
        "page": 14, "bbox": REG[(14, 3)], "reason": "fragment-of-other",
        "note": "second lane block pasted inside Figure 12.",
    },
    {
        "page": 14, "bbox": REG[(14, 4)], "reason": "fragment-of-other",
        "note": "third lane block pasted inside Figure 12.",
    },
    {
        "page": 14, "bbox": REG[(14, 5)], "reason": "fragment-of-other",
        "note": "fourth lane block pasted inside Figure 12.",
    },
    {
        "page": 14, "bbox": REG[(14, 6)], "reason": "fragment-of-other",
        "note": "fifth lane block pasted inside Figure 12.",
    },
    {
        "page": 16, "bbox": REG[(16, 3)], "reason": "fragment-of-other",
        "note": "the axes-and-dots area of the left-hand Figure 17, returned as its own region "
                "on top of the outer region that also covers the legend box; the outer region "
                "is the exhibit.",
    },
    {
        "page": 17, "bbox": REG[(17, 1)], "reason": "fragment-of-other",
        "note": "the blue person-and-desk clip art pasted into Figure 19; the diagram's arrows, "
                "queue boxes and dashed frame are vectors in the region that encloses this "
                "raster, so the raster is one layer of the exhibit, not an exhibit.",
    },
    {
        "page": 21, "bbox": REG[(21, 1)], "reason": "rule",
        "note": "not artwork: the two vector paths are the running-header rule and the rule "
                "under the line 'Our simulation codes written in C++:'. The band is the "
                "appendix heading block ('Appendices', 'Appendix A Simulation Code') sitting "
                "between two horizontal rules.",
    },
    {
        "page": 22, "bbox": REG[(22, 1)], "reason": "rule",
        "note": "not artwork: the three vector paths are the header rule and the rule that "
                "separates two C++ code blocks. The band is a strip of code listing.",
    },
    {
        "page": 31, "bbox": REG[(31, 1)], "reason": "rule",
        "note": "not artwork: the two vector paths are the header rule and the rule under the "
                "code block that ends page 30. The band holds the tail of the C++ listing plus "
                "the chapter heading '7 Other figures'.",
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
           other_note: str = "", note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "other_note": other_note or None,
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
          kind: str, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, idx, path, kind),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "booktabs", zebra: bool = False,
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
# The text layer keeps TeX ligatures (U+FB01 "fi", U+FB02 "fl"), so a hand-typed
# needle will not match. Fold both sides to the same form, remember where every
# folded character came from, and cut the quote out of the original string.

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
    """Locate a ligature-folded needle; return (page text, start, end) in real indices."""
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
    """Quote from `start` through the end of the word that `end` falls inside."""
    t, i, _ = _find(page, start)
    _, j, jend = _find(page, end, i)
    j = _to_word_end(page, jend)
    q = t[i:j].strip()
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


def cap(page: int, marker: str, end: str, *, after: int = 0, cut: bool = False) -> str:
    """Quote a caption: from `marker` ("Figure 13: ") through `end`.

    `cut=True` stops at the last character of `end`, for captions the typesetter
    broke mid-word against the next column ("... of Differ-Figure 11: ...").
    """
    t, i, _ = _find(page, marker, after)
    _, j, jend = _find(page, end, i)
    return t[i:(jend if cut else _to_word_end(page, jend))].strip()


def cite(page: int, start: str, end: str) -> str:
    return span(page, start, end)


# --- section paths, resolved from the context index -----------------------------
S22 = P("2", "2.2")
S322 = P("3", "3.2", "3.2.2")
S323 = P("3", "3.2", "3.2.3")
S331 = P("3", "3.3", "3.3.1")
S332 = P("3", "3.3", "3.3.2")
S333 = P("3", "3.3", "3.3.3")
S334 = P("3", "3.3", "3.3.4")
S412 = P("4", "4.1", "4.1.2")
S421 = P("4", "4.2", "4.2.1")
S422 = P("4", "4.2", "4.2.2")
S432 = P("4", "4.3", "4.3.2")
S51 = P("5", "5.1")
S52 = P("5", "5.2")
S53 = P("5", "5.3")
S71 = P("7", "7.1")
S72 = P("7", "7.2")

PIE_NOTE = ("a Highcharts pie, one wedge per process step, no percentages on the wedges and "
            "no leader lines: the six values are printed in a colour-swatch key below the pie, "
            "with a title line above it and the 'Highcharts.com' credit inside the region")

ALL = [
    table(6, 1, caption(cap(6, "Table 1: ", "Notations"), pos="above"),
          mention(6, first=6, style=["Table"], count=1, pattern="as-shown-in",
                  lead=span(6, "Here we list the symbols", "as shown in Table 1.")),
          grid(25, 2, header=1, txt=2),
          path=S22, kind="symbols",
          note="caption prints above the grid; the second column's wording slips one row by "
               "the end of the table (the 'T' row carries the description of the group total), "
               "so row-by-row the symbol and its gloss do not line up; several symbols print "
               "without their subscript pair (twaitA, twaitB, tcheck)"),
    table(8, 1, caption(cap(8, "Table 2: ", "Deviations"), pos="above"),
          mention(8, first=8, style=["Table"], count=1, pattern="direct",
                  lead=span(8, "The mean value", "Table 2")),
          grid(5, 3, header=1, units_hdr=True, numeric=2, txt=1),
          path=S322, kind="model",
          note="three columns with the units written into the header as attributes(ti), "
               "Mean Value(mu_i/s) and Standard Deviation(sigma_i/s); the lead sentence drops "
               "the noun ('The mean value and the standard are listed in Table 2')"),
    figure(8, 2, "flowchart-or-schematic",
           caption(cap(8, "Figure 1: ", "Model")),
           mention(8, first=8, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(8, "The first passenger", "as Figure 1 demonstrates.")),
           path=S323, kind="model", printed=True,
           note="seven numbered steps left to right, each step a box with a stick-figure row; "
                "the regular and Pre-Check tracks run in parallel below the step row and merge "
                "at the body scan; the step numbers are printed on the artwork, the only "
                "numbers on any of the three schematics in this paper"),
    figure(9, 1, "histogram",
           caption(cap(9, "Figure 2: ", "Total Time")),
           mention(9, first=9, style=["Figure"], count=1, pattern="direct",
                   lead=span(9, "We pick out 31678 samples", "plot Figure 2."),
                   trail=span(9, "According to Figure 2", "among the populations."),
                   read=1),
           path=S331, kind="result", printed=True,
           note="bins of the simulated total time, no legend; a title line 'Total Time "
                "Distribution' is printed inside the frame and a statistics box "
                "(Entries 31678 / Mean 518.6 / RMS 269.2) sits inside the upper right; the "
                "x-axis is labelled in seconds, so the mean 518.6 is seconds while the body "
                "text talks about minutes elsewhere"),
    figure(10, 1, "other",
           caption(cap(10, "Figure 3: ", "Process")),
           mention(10, first=9, style=["ﬁgure"], count=1, pattern="direct",
                   lead=span(9, "Then we consider the proportion", "figure 3."),
                   trail=span(9, "That is the main reason", "of the airport."), read=1),
           path=S332, kind="result", printed=True, labels=True, legend="below",
           other_note=PIE_NOTE,
           note="six wedges; the two largest are Waiting for Screening 98.11% and Preparing for "
                "Screening 0.66%, so the graphic makes one point and the other four wedges are "
                "unreadable"),
    figure(10, 2, "line",
           caption(cap(10, "Figure 4: ", "Rpassengers")),
           mention(10, first=9, style=["Figure"], count=1, pattern="figure-n-shows",
                   lead=span(9, "From Figure 4 and Figure 5", "the shape of letter"), read=1),
           path=S333, kind="result", printed=True, legend="inside",
           note="unconnected square markers with a separate fitted logistic curve through them, "
                "so the caption calls it a curve while the page draws points; an equation box "
                "inside the upper-left of the axes prints the fitted form, the adjusted "
                "R-squared 0.99315 and the five coefficients with their standard errors"),
    figure(10, 3, "line",
           caption(cap(10, "Figure 5: ", "Rpassengers")),
           mention(10, first=9, style=["Figure"], count=1, pattern="figure-n-shows",
                   lead=span(9, "From Figure 4 and Figure 5", "the shape of letter"), read=1),
           path=S333, kind="result", printed=True, legend="inside",
           note="same abscissa, same marker-plus-fit form as Figure 4, but the ordinate is the "
                "standard deviation; the equation box repeats the coefficient table with the "
                "label 'Stanard Error' misspelt in every row"),
    figure(11, 1, "line",
           caption(cap(11, "Figure 6: ", "Rlane")),
           mention(11, first=11, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(11, "As is shown in Figure 6", "Figure 7"), read=2),
           path=S334, kind="result", legend="outside-right",
           note="three simulated lane ratios plus their three fitted curves, so six legend "
                "entries in a box printed outside the axes; the y-axis prints a single numeral "
                "for a 0-5000 range, so the reader cannot calibrate the ordinate"),
    figure(12, 1, "line",
           caption(cap(12, "Figure 7: ", "Rlane")),
           mention(12, first=11, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(11, "As is shown in Figure 6", "Figure 7"), read=2),
           path=S334, kind="result", legend="inside",
           note="the standard-deviation partner of Figure 6: same marker-and-fit rendering, but "
                "the key moves inside the upper-right, and the ordinate is 0-4000 against "
                "Figure 6's 0-5000, so the same author draws one experiment twice with the "
                "legend in two places"),
    figure(13, 2, "line",
           caption(cap(13, "Figure 8: ", "Different")),
           mention(13, first=12, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(12, "As is shown in Figure 8", "significantly reduced."),
                   trail=span(12, "When the Nprepare reaches", "more crowded."), read=1),
           path=S412, kind="result", legend="inside",
           note="six series (Nprepare = 2..6 plus the un-linked case), key inside the "
                "upper-right; caption is broken by the typesetter: 'Figure 8: The Total Time Curves of "
                "Different' ends the left column and its last word, Nprepare, is printed after "
                "Figure 9's caption in the right column; five series, one per linkage size "
                "Nprepare = 2..6"),
    figure(13, 1, "line",
           caption(cap(13, "Figure 9: ", "Nprepare")),
           mention(13, first=12, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(12, "As is shown in Figure 8", "significantly reduced."), read=1),
           path=S412, kind="result", legend="inside",
           note="the standard-deviation partner, right of the pair: same x scale 0-5 s, same "
                "width, same inside-upper-right key; caption reads 'Curve' singular where "
                "Figure 8 reads 'Curves'"),
    figure(13, 3, "other",
           caption(cap(13, "Figure 10: ", "in Differ-", cut=True)),
           mention(13, style=[], count=0),
           path=S412, kind="result", printed=True, labels=True, legend="below",
           other_note=PIE_NOTE,
           note="no sentence in the paper points at this chart: the body claims 'we draw the "
                "proportion of the time in different processes again' and then cites Figure 11 "
                "only. Caption is broken across the column ('...in Differ-' + 'ent Process "
                "before MPL modification'); the wedges repeat Figure 3's numbers exactly "
                "(98.11%, 0.66%, 0.75%, 0.30%, 0.11%, 0.07%)"),
    figure(13, 4, "other",
           caption(cap(13, "Figure 11: ", "in Differ-", cut=True)),
           mention(13, first=12, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(12, "As is shown in Figure 11", "57.21%."), read=1),
           path=S412, kind="result", printed=True, labels=True, legend="below",
           other_note=PIE_NOTE,
           note="the same six wedges after the MPL change: waiting for screening falls 98.11% "
                "to 57.21% while preparing rises 0.66% to 18.05% and screening 0.75% to "
                "13.47%; caption broken across the column the same way as Figure 10's"),
    figure(14, 1, "flowchart-or-schematic",
           caption(cap(14, "Figure 12: ", "Model")),
           mention(14, first=13, style=["Figure"], count=1, pattern="direct",
                   lead=span(13, "Figure 12", "this new modification.")),
           path=S421, kind="model",
           note="two time nodes left to right; passengers are re-routed at each node between "
                "the emergency lane and the three regular lanes, and the re-routed groups are "
                "drawn as clip-art rows pasted over the vector arrows; no numbers anywhere on "
                "the artwork"),
    figure(14, 8, "line",
           caption(cap(14, "Figure 13: ", "under PBQ", cut=True)),
           mention(14, first=14, style=["Figure"], count=1, pattern="direct",
                   lead=span(14, "According to Figure 13", "(ta < 1s)"), read=1),
           path=S422, kind="result", legend="inside",
           note="five series (before PBQ, after PBQ for all passengers, for the priority and "
                "regular groups together, for the priority group alone, for the regular group "
                "alone), each chart carrying its own legend box inside the upper-left of the "
                "axes; caption broken across the column ('...under PBQ' + 'Model of Different "
                "Groups')"),
    figure(14, 7, "line",
           caption(cap(14, "Figure 14: ", "under PBQ", cut=True)),
           mention(14, style=[], count=0),
           path=S422, kind="result", legend="inside",
           note="the standard-deviation partner on the right, five series, own legend inside "
                "the upper-left. Two defects are printed, not extracted: the caption text is "
                "word-for-word Figure 13's, so the page carries the same sentence twice and "
                "nothing says the right-hand chart plots sigma_T; and the sigma_T curves dip "
                "below zero to about -4 min around t_a=2.4, which is impossible for a standard "
                "deviation, so the y-axis was stretched to -10 to fit them"),
    figure(15, 1, "heatmap-or-contour",
           caption(cap(15, "Figure 15: ", "first two groups")),
           mention(15, first=14, style=["Figure"], count=2, pattern="as-shown-in",
                   lead=span(14, "According to Figure 15", "lowing properties."),
                   trail=span(14, "As is shown in Figure 15", "the parameters change."), read=2),
           path=S422, kind="result", colorbar=True,
           note="filled 2-D colour map over the tad1-tad2 plane with a vertical colour bar; a "
                "title line 'Average Waiting Time of Different Advance Time' is printed inside "
                "the frame. The colour bar is labelled T_adv (min) and scaled 15-55 while the "
                "plotted quantity is T_avg, so the scale key names a variable that appears "
                "nowhere else in the paper"),
    figure(15, 2, "bar",
           caption(cap(15, "Figure 16: ", "three groups")),
           mention(15, first=14, style=["Figure"], count=2, pattern="as-shown-in",
                   lead=span(14, "According to Figure 15", "lowing properties."),
                   trail=span(15, "It is obvious that in Figure 16", "the average time"),
                   read=2),
           path=S422, kind="result", three_d="perspective-bars",
           note="the three-group version of Figure 15, drawn on a different device: a 3-D bar "
                "field on a perspective grid that occludes its own rear bars, with no colour "
                "bar, no legend and only a 35-37.2 z-tick range to calibrate it against. The caption runs "
                "straight into the next body sentence ('...of the three groups do not match "
                "the relevant flow volumn of passengers, it does not have negative effects.'), "
                "which is prose, not caption, and misspells 'volume'"),
    figure(16, 1, "scatter",
           caption(cap(16, "Figure 17: ", "of Differ-", cut=True)),
           mention(16, first=16, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(16, "As is shown in Figure 17", "are similar."), read=1),
           path=S432, kind="result", legend="inside",
           note="four series, one per share of elderly and child passengers (0, 10%, 20%, 30%), "
                "drawn as unconnected square markers with no fit curve, where Figures 4 and 5 "
                "plot the same kind of data as points plus a fitted curve; caption broken "
                "across the column ('...of Differ-' + 'ent Royp')"),
    figure(16, 2, "scatter",
           caption(cap(16, "Figure 18: ", "Curve of")),
           mention(16, first=16, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(16, "As is shown in Figure 17", "are similar."), read=1),
           path=S432, kind="result", legend="inside",
           note="standard-deviation partner, same four series, its own inside-upper-right key "
                "rather than one key shared by the pair; caption reads 'Curve' singular"),
    figure(17, 2, "flowchart-or-schematic",
           caption(cap(17, "Figure 19: ", "Lines")),
           mention(17, first=17, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(17, "This process is shown", "Figure 19."), read=1),
           path=S51, kind="model",
           note="eight passenger glyphs on the left, three of them stepping forward on a "
                "straight arrow, then curved arrows carrying them into four dashed queue boxes "
                "that each end at a desk-and-screen icon labelled 'Regular'; the word 'Regular' "
                "is printed four times on the artwork as an inline label, not as a legend"),
    figure(17, 3, "line",
           caption(cap(17, "Figure 20: ", "under M-", cut=True)),
           mention(17, first=17, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(17, "According to Figure 20", "significantly reduced."), read=1),
           path=S52, kind="sensitivity", legend="inside",
           note="six series (5/10/15% cut-in rates, each with and without the MPL change), "
                "legend box printed inside the upper right of the axes; caption broken across "
                "the column ('...under M-' + 'PL Model in Chinese Situation')"),
    figure(17, 4, "line",
           caption(cap(17, "Figure 21: ", "Curves")),
           mention(17, first=17, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(17, "According to Figure 20", "significantly reduced."), read=1),
           path=S52, kind="sensitivity", legend="inside",
           note="variance partner, same six series and the same inside-upper-right legend as "
                "Figure 20; caption stops at 'Curves' and the rest of the sentence is printed "
                "under Figure 20's column"),
    figure(18, 1, "line",
           caption(cap(18, "Figure 22: ", "under P-", cut=True)),
           mention(18, first=18, style=["Figure"], count=1, pattern="as-shown-in",
                   lead=span(18, "According to Figure 22", "significantly reduced"), read=1),
           path=S53, kind="sensitivity", legend="inside",
           note="the PBQ version of Figure 20 at two cut-in rates, ten legend entries in a box "
                "that fills the top band of the axes and is clipped by the right frame on the "
                "longest entries, so the key hides about a third of the plotting height; "
                "caption broken across the column ('...under P-' + 'BQ Model in Chinese "
                "Situation')"),
    figure(18, 2, "line",
           caption(cap(18, "Figure 23: ", "Curves")),
           mention(18, first=14, style=["Figure"], count=2, pattern="direct",
                   lead=span(18, "According to Figure 22", "significantly reduced"), read=1),
           path=S53, kind="sensitivity", legend="inside",
           note="variance partner: same ten-entry key inside the top band, duplicated rather "
                "than shared with Figure 22, and the y axis runs from -10 although a variance "
                "cannot be negative. The only exhibit in the body cited on two different pages "
                "(p14 pairs it with Figure 13, p18 pairs it with Figure 22)"),
    figure(18, 3, "heatmap-or-contour",
           caption(cap(18, "Figure 24: ", "After PBQ")),
           mention(18, first=18, style=["Figure"], count=1, pattern="direct",
                   lead=span(18, "From Figure 24", "PBQ model"),
                   trail=span(18, "the rate of cutting in lines", "consumed time."), read=1),
           path=S53, kind="sensitivity", colorbar=True,
           note="filled contour of the average waiting time over the cut-in-rate/time-interval "
                "plane, colour bar at the right, no legend; the in-figure title and the caption "
                "are the same sentence printed twice, and the in-figure copy uses a curly "
                "apostrophe where the caption uses a straight one"),
    figure(31, 2, "bar",
           caption(cap(31, "Figure 25: ", "Two Groups")),
           mention(31, style=[], count=0),
           path=S71, kind="appendix", three_d="perspective-bars",
           note="the standard-deviation partner of Figure 16, printed in the appendix with no "
                "sentence anywhere in the paper pointing at it; 3-D bar field, no colour bar, "
                "no legend"),
    figure(31, 3, "bar",
           caption(cap(31, "Figure 26: ", "All the Groups")),
           mention(31, style=[], count=0),
           path=S71, kind="appendix", three_d="perspective-bars",
           note="the three-group version of Figure 25, same 3-D bar device; the z-range is "
                "20.0-21.8 s against Figure 25's 8.5-12.5 s, so the two plates of the same "
                "quantity are drawn on scales that differ by a factor of two"),
    figure(32, 1, "heatmap-or-contour",
           caption(cap(32, "Figure 27: ", "After PBQ")),
           mention(32, style=[], count=0),
           path=S72, kind="appendix", colorbar=True,
           note="filled contour with a vertical colour bar, no legend, in-figure title = the "
                "caption sentence; uncited"),
    figure(32, 2, "heatmap-or-contour",
           caption(cap(32, "Figure 28: ", "PBQ Modification")),
           mention(32, style=[], count=0),
           path=S72, kind="appendix", colorbar=True,
           note="filled contour with a vertical colour bar; uncited, and its title line "
                "capitalises 'After' where the caption lower-cases it"),
    figure(32, 3, "heatmap-or-contour",
           caption(cap(32, "Figure 29: ", "PBQ Modification")),
           mention(32, style=[], count=0),
           path=S72, kind="appendix", colorbar=True,
           note="the before-PBQ counterpart of Figure 28; uncited"),
    figure(33, 1, "heatmap-or-contour",
           caption(cap(33, "Figure 30: ", "after PBQ Modification")),
           mention(33, style=[], count=0),
           path=S72, kind="appendix", colorbar=True,
           note="filled contour, colour bar, in-figure title 'Standard Deviations of Different "
                "Advance Time After PBQ Modification' while the caption says 'The Standard "
                "Deviations of Different Rcut ...'; uncited"),
    figure(33, 2, "heatmap-or-contour",
           caption(cap(33, "Figure 31: ", "before PBQ Modification")),
           mention(33, style=[], count=0),
           path=S72, kind="appendix", colorbar=True,
           note="the before-PBQ counterpart of Figure 30; uncited"),
]

_seen: dict[int, int] = {}
for _i, _e in enumerate(ALL, 1):
    _p = _e["page"]
    _seen[_p] = _seen.get(_p, 0) + 1
    _e["place"]["doc_order"] = _i
    _e["place"]["page_order"] = _seen[_p]

RULES = [
    "全篇 31 张图里折线/散点轴系图占 14 张（[geometry.family]=line 12 条、scatter 2 条），"
    "两参数色块图 7 张（heatmap-or-contour），三维柱场 3 张（bar + "
    "three_d=perspective-bars），"
    "示意图 3 张（flowchart-or-schematic，Figs 1/12/19），饼图 3 张（other，Figs 3/10/11），"
    "直方图 1 张（histogram，Fig 2）——图型是按要回答哪一句话选的，不是按数据形态选的。",
    "同一个实验总是成对印：均值一张、标准差一张，并排、同横轴（Figs 4/5、6/7、8/9、"
    "13/14、17/18、20/21、22/23 七对，共 14 张），所以 31 张图承载的问题数远少于图数；"
    "配对关系不落在任何字段里（[mention.count] 只统计被引次数）。读者要自己对齐两张图的量纲，"
    "因为每张图都自带一套坐标轴（[geometry.shared_axes]=False 在全部 31 条上成立）。",
    "两轴平面的参数扫描一律用热力/等高线加竖色标收进一张图："
    "（[geometry.family]=heatmap-or-contour 7 条，Figs 15/24/27/28/29/30/31），"
    "色标为真（[geometry.colorbar]=True 恰好在这 7 条上成立，其余 24 条全 False）。"
    "要同时压两个自变量时不上三维，先上二维色块。",
    "三维只在附录和 4.2.2 出现，且只用于同一量在两种参数下的对照："
    "（[geometry.three_d]=perspective-bars 3 条，Figs 16/25/26），三维但无色标、无图例，"
    "（[geometry.legend]=none 在这 3 条上成立），读者无从标定颜色。",
    "图例位置不统一，跟着作图软件走：图例在图内的 13 条（[geometry.legend]=inside，"
    "Figs 4/5/7/8/9/13/14/17/18/20/21 等），图外右侧 1 条（outside-right，Fig 6——"
    "它和 Fig 7 是同一个实验，键框却一个在外一个在内），饼图 3 条把色块清单压在图下"
    "（below，Figs 3/10/11），示意图 3 条、色块图 7 条、三维柱场 3 条与 Fig 2 直方图都不印图例"
    "（none 14 条）。",
    "饼图只给“时间花在哪儿”这一个问题：六块扇区、扇区上不印百分比、也不拉引线，"
    "六个数值印在图下方的色块清单里（[geometry.legend]=below，[geometry.printed_numbers]=True，"
    "Figs 3/10/11）；换到比较两类人群的差异，就不再切饼，改用图 24 那种色块图。",
    "图内印数字是少数派：31 条里 7 条把数值印进图框（[geometry.printed_numbers]=True："
    "Figs 1 的步骤号、2 的统计框、3/10/11 的清单、4/5 的拟合方程框），其余 24 条只剩刻度数字"
    "（[geometry.printed_numbers]=False）。想读具体数值只能看正文或表。",
    "题注一律在图下（[caption.position]=below 在 31 条图记录上成立），两张表的题注一律在表上"
    "（[caption.position]=above 在 2 条表记录上成立）；编号格式全篇只有 Figure N: 与 Table N: "
    "两种（[caption.numbering]），没有一处缩写。",
    "题注只报对象、不给结论、不给单位、不给条件（[caption.concludes]=False、"
    "[caption.units]=False、[caption.conditions]=False 在全部 33 条上成立），"
    "长度压在 3-15 词、一句（[caption.words]），模板是 The X Curves of Different Y / "
    "The Distribution of the X / The Percentage of Time in Different Process。",
    "题注点到变量的写法分两路：坐标轴图一定把自变量写进题注（[caption.variables]=True，"
    "Different Rpassenger / Different Rlane / Different Nprepare / Different Royp），"
    "示意图与饼图不点（[caption.variables]=False，Figs 1/12/19 与 3/10/11 六条）。",
    "引出句有固定句式：As is shown in Figure N（[mention.lead_pattern]=as-shown-in 15 条，"
    "最多），其次 According to Figure N 或 Figure N describes 这类直接点名"
    "（direct 7 条），图号当主语的只有 2 次（figure-n-shows，Figs 4/5 共用一句 From Figure 4 "
    "and Figure 5 we can view that…），另有 9 个对象没有引出句（none）。",
    "图基本印在哪页就在哪页被引：13 个对象 lead_pages=0（[mention.lead_pages]=0），"
    "10 个提前一页被引（lead_pages=1），只有 Fig 23 提前四页就被点名（lead_pages=4，"
    "p14 与 Fig 13 配对着引一次，p18 再引一次，[mention.count]=2）。",
    "被引次数没有长尾：21 个对象只被引 1 次（[mention.count]=1），3 个被引 2 次"
    "（Fig 15、Fig 16、Fig 23），9 个一次都没有（count=0：Figs 10/14 与附录 25-31），"
    "没有图被反复引用来撑论证。",
    "图后读句比图前引出句更常见：20 个对象带读句（[mention.read_sentences]>=1，其中 4 个带两句），"
    "13 个没有（read=0）——其中就包括所有 9 个零被引的对象，说明“无引出句”与“无读句”是同一批图。",
    "版式上没有一个对象独占一页：最大的是 Table 1 的 0.256、图里最大的是 Fig 1 的 0.19"
    "（[place.area_frac]），最小 0.028，全部达不到半页（[place.solo_page]=False 在 33 "
    "条上成立），"
    "因此 fig 的排布在页顶、页中、页底都有（[place.page_zone] 分布 top 11 / middle 15 / bottom 7），"
    "跟着文字流走，不做满页浮图。",
    "对象按章节性质落位：result 16 条、sensitivity 5 条、appendix 7 条、model 4 条、"
    "symbols 1 条（[place.section_kind]）。7 张带色标的色块图有 6 张落在敏感性节与附录"
    "（[place.section_path]：5.3 的 Fig 24 与 7.2 的 Figs 27-31），只有 Fig 15 夹在 4.2.2 "
    "的结果里——越往后写，“两个参数一起扫”这种问法越靠色块图回答。",
    "印刷缺陷照录不修：Figs 13/14 的题注逐字相同而右图印的是 sigma_T；Fig 14 的 sigma_T "
    "曲线掉到零以下约 -4 min（[caption.verbatim] 与 note）；Fig 16 的题注直接连到下句正文"
    "“...do not match the relevant flow volumn of passengers”；Fig 15 的色标写成 T_adv "
    "而图里画的是 T_avg（[geometry.colorbar] 与 note）。",
]

NOTE = (
    "Two structural facts drive every number in this record. First, the paper's unit of "
    "evidence is a pair of charts, not a chart: every experiment is printed twice, once for "
    "the mean and once for the standard deviation, side by side on a shared abscissa, so 31 "
    "plates encode 16 experiments and the reader must align two independent sets of axes. "
    "Second, the exhibit family follows the number of things being compared, not the data "
    "type: three or four categories get a line or marker chart, six shares of one total get a "
    "pie, and a two-parameter sweep gets filled colour bands with a colour bar, never a 3-D "
    "surface except in the appendix and in Figure 16, where the 3-D bars occlude their own "
    "rear rows and carry no colour key.\n\n"
    "The appendix chapter '7 Other figures' holds seven plates (Figures 25-31) that no "
    "sentence in the paper points at, and three body charts (Figures 3, 10, 14) are equally "
    "uncited; the record keeps mention.count=0 for all nine rather than inventing a "
    "citation.\n\n"
    "Printed defects kept visible: Figures 13 and 14 carry word-for-word identical captions "
    "although the right-hand chart plots sigma_T; Figure 14's sigma_T curves dip to about -4 "
    "min, impossible for a standard deviation, and the axis was stretched to -10 to fit them; "
    "Figure 15's colour bar is labelled T_adv while the plotted quantity is T_avg; Figure 16's "
    "caption runs straight into the next body sentence; Figures 8/9/10/11/13/14/16/17/18/20/"
    "21/22 are captioned across a column break, so each caption exists on the page only as "
    "two fragments and caption_verbatim stores the fragment that carries the figure "
    "number.\n\n"
    "Layout: 50 measured regions on 17 pages resolve to 33 exhibits (31 figures, 2 tables) "
    "plus 17 exclusions, unaccounted 0. Fourteen exclusions are bitmaps pasted inside a "
    "larger drawing; the other three are the ruled header bands of the code-listing pages 21, "
    "22 and 31, which the detector returns because a page rule is a long thin vector path."
)

FIGURES = [e for e in ALL if "table" not in e]
TABLES = [e for e in ALL if "table" in e]

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

if __name__ == "__main__":
    from collections import Counter

    def tally(key):
        return dict(Counter(key(e) for e in ALL if "table" not in e))

    print("rows", len(ALL), "excluded", len(EXCLUDED))
    print("family", tally(lambda e: e["geometry"]["family"]))
    print("legend", tally(lambda e: e["geometry"]["legend"]))
    print("three_d", tally(lambda e: e["geometry"]["three_d"]))
    print("colorbar", tally(lambda e: e["geometry"]["colorbar"]))
    print("panels", tally(lambda e: e["geometry"]["panel_count"]))
    print("printed", tally(lambda e: e["geometry"]["printed_numbers"]))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in ALL)))
    print("caption_position", dict(Counter(e["caption"]["position"] for e in ALL)))
    print("caption_words", sorted(e["caption"]["words"] for e in ALL))
    print("pattern", dict(Counter(e["mention"]["lead_pattern"] for e in ALL)))
    print("lead_pages", dict(Counter(e["mention"]["lead_pages"] for e in ALL)))
    print("count", dict(Counter(e["mention"]["count"] for e in ALL)))
    print("read", dict(Counter(e["mention"]["read_sentences"] for e in ALL)))
    print("area", sorted(round(e["place"]["area_frac"], 2) for e in ALL))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in ALL)))
    for e in ALL:
        assert "bbox" in e
    out = LANE / f".proxy/{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
