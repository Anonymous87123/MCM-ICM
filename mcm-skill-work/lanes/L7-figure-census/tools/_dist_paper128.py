"""Hand pass for P-C-2017-55585-278f2f68 (cellular-automaton traffic model with SDVs, 20 figures + 4 tables).

Shape of the paper: assumptions, a notation table, then the following model and the multilane
model, each built as a rule schematic per behaviour (accelerate / decelerate / hold / lane
change), then two simulation chapters, an application chapter that puts the model on real
interstates, a sensitivity chapter with two tables, and a letter to a governor that carries
one uncaptioned map.

What the record has to say out loud:

1. Section 4.1.2-4.2.4 are a rule manual: every rule gets a lane-strip schematic whose lanes
   are the rows, with the D_min / D_max brackets drawn as annotation arrows above the strip.
   Nine figures use that one template (Figs 2-10), so the census has to show that the template
   is the paper's content, not a repeated decoration.
2. No plotted exhibit appears before chapter 5. Every chart sits in chapters 5-7, and the
   switch from schematic to chart happens exactly at 5.1.
3. Fig 11 and Fig 15 are the same exhibit twice: a time-space picture in which each dot is a
   vehicle and each row is a lane, one for the single-lane model and one for the four-lane
   model. Both are raster screenshots with the legend drawn inside the bitmap.
4. Fig 12 is the only three-dimensional exhibit in the paper: a perspective scatter of the
   speed / flow / SDV-share cloud, coloured by speed, with a vertical colour bar instead of a
   legend.
5. Two pairs of printed figures share one measured region because they are printed side by
   side and their drawing clusters join: Figs 13+14 on page 16 and Figs 16+17 on page 18. Each
   row says so, panel_count is 2, and the caption is the printed half-line that belongs to that
   figure, not a reconstructed sentence.
6. Captions print below every figure and above every table. The numbering is uniformly
   "Figure N:" / "Table N:".
7. Four exhibits are first cited a page before they print (Figs 6, 7, 9, 10, 16, 17) and one is
   first cited a page after it prints (Fig 18), because the float moves across the page break.

Printed defects this record keeps visible instead of repairing:
- The text line that introduces Table 1 and Fig. 1 cites them as "Tab. 4.1.1" and "Fig. 1",
  i.e. it uses the section number as the table number. The tables are numbered 1 and 2.
- Table 2 is introduced the same way, as "Tab. 4.2.1".
- The caption of Fig. 20 says "Interstates 90, 402 and State Route 520"; the third panel inside
  the figure is labelled "Interstate 405". The caption is wrong, the figure is what was drawn.
- The text introducing Fig. 15 says "one of the results of the Following Model" while the
  figure and its caption are the multilane model.
- Figs 9, 13, 14 and 16 are printed with their captions split across two columns, so the
  caption line as printed is a fragment. The fragment is quoted, the reconstruction is in note.

Usage: python -I tools/_dist_paper128.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2017-55585-278f2f68"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

EXCLUDED = [
    {
        "page": 7, "bbox": REG[(7, 2)], "reason": "fragment-of-other",
        "note": "the pasted SDV icon that Figure 1 draws as one of its own vehicles: a raster "
                "block of 77 x 44 pt sitting on the diagram's left edge, two points outside the "
                "measured cluster it belongs to. The exhibit is measured by the cluster, this is "
                "the bitmap inside it.",
    },
    {
        "page": 10, "bbox": REG[(10, 2)], "reason": "fragment-of-other",
        "note": "one of three equal 254 x 32 pt raster strips stacked inside Figure 4; they are "
                "the vehicle bitmaps of the deceleration figure, not exhibits.",
    },
    {
        "page": 10, "bbox": REG[(10, 3)], "reason": "fragment-of-other",
        "note": "second of the three raster strips inside Figure 4.",
    },
    {
        "page": 10, "bbox": REG[(10, 4)], "reason": "fragment-of-other",
        "note": "third of the three raster strips inside Figure 4; it hangs 6 pt below the "
                "measured cluster, which is why the fusion test kept it as its own region.",
    },
    {
        "page": 11, "bbox": REG[(11, 2)], "reason": "fragment-of-other",
        "note": "raster strip inside the Figure 5 lane diagram.",
    },
    {
        "page": 11, "bbox": REG[(11, 3)], "reason": "fragment-of-other",
        "note": "second raster strip inside the Figure 5 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 2)], "reason": "fragment-of-other",
        "note": "raster strip inside the Figure 7 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 3)], "reason": "fragment-of-other",
        "note": "second raster strip inside the Figure 7 lane diagram; it overlaps the first, the "
                "two together being the vehicle row.",
    },
    {
        "page": 13, "bbox": REG[(13, 4)], "reason": "fragment-of-other",
        "note": "third raster strip inside the Figure 7 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 6)], "reason": "fragment-of-other",
        "note": "raster strip inside the Figure 8 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 7)], "reason": "fragment-of-other",
        "note": "second raster strip inside the Figure 8 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 8)], "reason": "fragment-of-other",
        "note": "third raster strip inside the Figure 8 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 9)], "reason": "fragment-of-other",
        "note": "fourth raster strip inside the Figure 8 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 10)], "reason": "fragment-of-other",
        "note": "fifth raster strip inside the Figure 8 lane diagram.",
    },
    {
        "page": 13, "bbox": REG[(13, 11)], "reason": "fragment-of-other",
        "note": "sixth raster strip inside the Figure 8 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 3)], "reason": "fragment-of-other",
        "note": "raster strip inside the Figure 9 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 4)], "reason": "fragment-of-other",
        "note": "second raster strip inside the Figure 9 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 5)], "reason": "fragment-of-other",
        "note": "raster strip inside the Figure 10 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 6)], "reason": "fragment-of-other",
        "note": "second raster strip inside the Figure 10 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 7)], "reason": "fragment-of-other",
        "note": "third raster strip inside the Figure 9 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 8)], "reason": "fragment-of-other",
        "note": "third raster strip inside the Figure 10 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 9)], "reason": "fragment-of-other",
        "note": "fourth raster strip inside the Figure 10 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 10)], "reason": "fragment-of-other",
        "note": "fourth raster strip inside the Figure 9 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 11)], "reason": "fragment-of-other",
        "note": "fifth raster strip inside the Figure 10 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 12)], "reason": "fragment-of-other",
        "note": "fifth raster strip inside the Figure 10 lane diagram.",
    },
    {
        "page": 15, "bbox": REG[(15, 14)], "reason": "fragment-of-other",
        "note": "the key block drawn inside the Figure 11 raster: the SDV square, the NSDV "
                "square, the clock glyph and the speed arrow. It is part of the picture, and the "
                "picture is measured by its own region.",
    },
    {
        "page": 15, "bbox": REG[(15, 15)], "reason": "duplicate",
        "note": "a second and third copy of the same 99 x 55 pt key block returned by the page's "
                "image list; all three copies carry one bbox, so the census holds them as one "
                "region.",
    },
    {
        "page": 15, "bbox": REG[(15, 17)], "reason": "fragment-of-other",
        "note": "the clock column of the Figure 11 raster, drawn inside the picture as a time "
                "axis key.",
    },
    {
        "page": 17, "bbox": REG[(17, 2)], "reason": "fragment-of-other",
        "note": "an inset inside the Figure 15 raster: the zoomed callout labelled B (an "
                "SDV-Train). The raster is the exhibit.",
    },
    {
        "page": 17, "bbox": REG[(17, 3)], "reason": "fragment-of-other",
        "note": "second inset inside the Figure 15 raster, the zoomed callout labelled A "
                "(overtaking).",
    },
    {
        "page": 24, "bbox": REG[(24, 1)], "reason": "rule",
        "note": "the appendix opening band: the 'Appendices' title, the bold 'Appendix A: Matlab "
                "Program for Visualization' line and the full-width rule under it. Two page-wide "
                "paths, no drawn content, and no box around the listing below it.",
    },
    {
        "page": 25, "bbox": REG[(25, 1)], "reason": "rule",
        "note": "the appendix heading band: 'Appendix B: C++ Program for Simulation' between two "
                "full-width rules. No frame around the C++ listing.",
    },
]


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
           kind: str, legend: str = "none", printed: bool = False,
           labels: bool = False, panels: int = 1, layout: str = "1",
           shared: bool = False, colorbar: bool = False, three_d: str = "no",
           note: str = "", numbered: bool = True, source: str = "text-layer") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "place": place(page, idx, path, kind, numbered),
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
          kind: str, note: str = "", source: str = "text-layer") -> dict:
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


# --- section paths, as printed in the numbered heading lines -------------------------------
P_DET = "4 Details of the Model"
P_FOL = "4.1 Following Model"
P_MUL = "4.2 Multilane Traffic Model"
P_RES = "5 Analysis of the Results Obtained from the Model Simulation"
P_SENS = "7 Sensitivity Analysis"

P_TAB1 = [P_DET, P_FOL, "4.1.1 Variables"]
P_FOL_NSDV = [P_DET, P_FOL, "4.1.2 Following Rules for NSDVs"]
P_FOL_SDV = [P_DET, P_FOL, "4.1.3 Following Rules for SDVs"]
P_TAB2 = [P_DET, P_MUL, "4.2.1 Variables"]
P_MUL_NSDV = [P_DET, P_MUL, "4.2.3 Lane-Changing Rules for NSDVs"]
P_MUL_SDV = [P_DET, P_MUL, "4.2.4 Lane-Changing Rules for SDVs"]
P_R_NEXT = [P_RES, "5.1 Results of Following Model"]
P_R_MULTI = [P_RES, "5.2 Results of the Multilane Traffic Model"]
P_R_LANE = [P_RES, "5.3 SDV Lane"]
P_APPL = ["6 Appliance of the Model"]
P_SENS_LCP = [P_SENS, "7.1 Choice of the Parameters in LCP"]
P_SENS_LIM = [P_SENS, "7.2 Different Speed Limit"]
P_LETTER = ["10 A Letter"]

SCHEMA_NOTE = ("lane-strip schematic: one row per lane, vehicles on the rows, the D_min/D_max "
               "brackets drawn as annotation arrows over the strip, the rule label of each lane "
               "printed at the right end of its row")

ALL = [
    table(7, 1,
          caption("Table 1: Main Variables Used in the Following Model", numbering="Table N:"),
          mention(7, first=7, style=["Tab."], count=1, read=0,
                  trail=span(7, "Main variables used in the Following Model are shown in",
                             "Fig. 1.")),
          grid(10, 3, numeric=0, txt=1, width="full"),
          path=P_TAB1, kind="symbols",
          note="three columns (symbol, definition, unit) over nine symbols; the unit is its own "
               "column, not a bracket in the header. The introducing sentence numbers it "
               "'Tab. 4.1.1' — the section number used as a table number."),

    figure(7, 3, "flowchart-or-schematic",
           caption("Figure 1: Diagram of Main Variables Used in the Following Model"),
           mention(7, first=7, style=["Fig."], count=1, read=0,
                   trail=span(7, "Main variables used in the Following Model are shown in",
                              "Fig. 1.")),
           path=P_TAB1, kind="symbols", legend="below", printed=True,
           note="the same nine symbols drawn on a two-lane strip: A/B/C/D with v and Δd printed "
                "on the diagram, an SDV and an NSDV icon, and a back-light key (bi=1 / bi=0) in "
                "a legend row between the drawing and the caption. It is the notation table "
                "drawn instead of read."),

    figure(8, 1, "flowchart-or-schematic",
           caption("Figure 2: Following Rules for NSDVs"),
           mention(8, first=8, style=["Fig."], count=4, pattern="as-shown-in", read=2,
                   lead=span(8, "As shown in Lane 1 in Fig. 2", "Fig. 2"),
                   trail=span(8, "And this is Lane 2 in Fig. 2.", "Fig. 2.")),
           path=P_FOL_NSDV, kind="model", legend="outside-right", printed=True,
           note="five lanes, one per rule branch: two deceleration lanes, two acceleration "
                "lanes, one hold lane, each row ending in its own rule label instead of a key "
                "box — which is why the legend reads outside-right and not inside. " +
                SCHEMA_NOTE),

    figure(9, 1, "flowchart-or-schematic",
           caption("Figure 3: Following Rules for SDVs: Acceleration"),
           mention(9, first=9, style=["Fig."], count=5, pattern="direct", read=4,
                   lead=span(9, "The three vehicles in Lane 4 from Fig. 3", "Fig. 3"),
                   trail=span(10, "which is the situation in Lane 1 in Fig. 3", "Fig. 3")),
           path=P_FOL_SDV, kind="model", legend="outside-right", printed=True,
           note="four acceleration lanes; row labels print the condition (a_F=1 on Lane 4) and a "
                "brace under Lane 4 marks the SDV-Train. " + SCHEMA_NOTE),

    figure(10, 1, "flowchart-or-schematic",
           caption("Figure 4: Following Rules for SDVs: Deceleration"),
           mention(10, first=10, style=["Fig."], count=3, pattern="parenthetical", read=3,
                   lead=span(10, "which is the situation in Lane 1 in Fig. 4", "Fig. 4"),
                   trail=span(11, "which is the situation in Lane 3 in Fig. 4", "Fig. 4.")),
           path=P_FOL_SDV, kind="model", legend="outside-right", printed=True,
           note="three deceleration lanes, all three row labels reading 'Deceleration'. The "
                "vehicle bitmaps are pasted rasters inside the vector strip, which is why the "
                "page yields three extra raster regions. " + SCHEMA_NOTE),

    figure(11, 1, "flowchart-or-schematic",
           caption("Figure 5: Following Rules for SDVs: Hold"),
           mention(11, first=11, style=["Fig."], count=1, pattern="as-shown-in", read=1,
                   lead=span(11, "Two different situations are shown in Fig. 5", "Fig. 5")),
           path=P_FOL_SDV, kind="model", legend="outside-right", printed=True,
           note="two hold lanes, one behind an NSDV and one behind an SDV-Train with a_F=0. " +
                SCHEMA_NOTE),

    table(11, 4,
          caption("Table 2: Additional Variables Used in the Multilane Traffic Model",
                  numbering="Table N:"),
          mention(11, first=11, style=["Tab."], count=1, read=0,
                  trail=span(11, "Besides variables listed in Tab. 4.1.1", "Fig. 6.")),
          grid(5, 3, numeric=0, txt=1, width="half"),
          path=P_TAB2, kind="symbols",
          note="four more variables over the same three columns; half the text width, unlike "
               "Table 1. Introduced as 'Tab. 4.2.1'."),

    figure(12, 1, "flowchart-or-schematic",
           caption("Figure 6: Diagram of Additional Variables Used in the Multilane Traffic "
                   "Model"),
           mention(12, first=11, style=["Fig."], count=2, pattern="as-shown-in", read=1,
                   lead=span(12, "As showed in Fig. 6", "Fig. 6")),
           path=P_TAB2, kind="symbols", legend="below", printed=True,
           note="two-lane grid with Δd_A,E and the lane index l printed on the diagram, plus a "
                "three-item turn-signal key under the grid (both off / right / left, ci=0/1/-1). "
                "Row labels absent here, so unlike Figs 2-5 the key sits under the drawing."),

    figure(13, 1, "flowchart-or-schematic",
           caption("Figure 7: LCM for NSDVs under Certain Conditions"),
           mention(13, first=12, style=["Fig."], count=1, pattern="as-shown-in", read=1,
                   lead=span(12, "Some of the circumstances are shown in Fig. 7.", "Fig. 7.")),
           path=P_MUL_NSDV, kind="model", legend="outside-right", printed=True,
           note="two stacked two-lane cases (E-vs-A-B and the same with vA<vB), first case "
                "marked with a printed cross on the blocked lane, LCM_A brace on Lane 1. " +
                SCHEMA_NOTE),

    figure(13, 5, "flowchart-or-schematic",
           caption("Figure 8: LCS for NSDVs under Certain Conditions"),
           mention(13, first=13, style=["Fig."], count=1, pattern="as-shown-in", read=1,
                   lead=span(13, "A few of the circumstances are shown in Fig. 8.", "Fig. 8.")),
           path=P_MUL_NSDV, kind="model", legend="outside-right", printed=True,
           note="three stacked cases showing the three failure modes of LCS_A (Δd_A,E < "
                "D_min(vA), c_C=-1, and the passing case). The printed caption line ends at "
                "'Conditions'; the bullet that follows it in the text layer belongs to the next "
                "paragraph, not to the caption. " + SCHEMA_NOTE),

    figure(15, 1, "flowchart-or-schematic",
           caption("Figure 9: LCM for SDVs under Certain Condi-"),
           mention(15, first=14, style=["Fig."], count=1, pattern="as-shown-in", read=1,
                   lead=span(14, "Some of the circumstances are shown in Fig. 9 and Fig. 10.",
                             "Fig. 10.")),
           path=P_MUL_SDV, kind="model", legend="outside-right", printed=True,
           note="left column of the two-column pair. The caption is hyphenated across the column "
                "break: as printed it is 'Figure 9: LCM for SDVs under Certain Condi-', and the "
                "tail 'tions' surfaces in the text layer after Figure 10's own caption, so the "
                "fragment is quoted as printed and not patched. " + SCHEMA_NOTE),

    figure(15, 2, "flowchart-or-schematic",
           caption("Figure 10: LCS for SDVs under Certain Conditions"),
           mention(15, first=14, style=["Fig."], count=1, pattern="as-shown-in", read=1,
                   lead=span(14, "Some of the circumstances are shown in Fig. 9 and Fig. 10.",
                             "Fig. 10.")),
           path=P_MUL_SDV, kind="model", legend="outside-right", printed=True,
           note="right column of the pair; five cases, each with its condition printed along the "
                "row (cB=-1, Δd_A,E<Δd_min, tB=0, cC=-1, cG=-1). " + SCHEMA_NOTE),

    figure(15, 13, "scatter",
           caption("Figure 11: One of the Results of Following Model Simulation"),
           mention(15, first=15, style=["Fig."], count=1, pattern="figure-n-shows", read=1,
                   lead=span(15, "Fig. 11 shows one of the results of the Following Model",
                             "Following Model"),
                   trail=span(15, "in which each dot represents a vehicle", "time")),
           path=P_R_NEXT, kind="result", legend="inside", printed=True,
           note="raster screenshot, not vector: dots are vehicles, one row per lane, x is time. "
                "Two measured brackets are printed on the picture (Δd=22 cell, Δd=10 cell) and "
                "the key block (SDV / NSDV squares, clock, speed arrow) is drawn inside the "
                "bitmap, returned three times by the image list."),

    figure(16, 1, "scatter",
           caption("Figure 12: Correlations Among Average Speed, the Percentage of SDVs and the "
                   "Traffic Flow"),
           mention(16, first=16, style=["Fig."], count=2, pattern="as-shown-in", read=1,
                   lead=span(16, "shown in a three dimension map in Fig. 12", "Fig. 12"),
                   trail=span(16, "As we can find in Fig. 12", "smooth surface")),
           path=P_R_NEXT, kind="result", colorbar=True, three_d="isometric",
           note="the only 3-D exhibit in the paper: speed on the vertical axis, SDV percentage "
                "and traffic flow on the two floor axes, points coloured by speed with a "
                "vertical colour bar and no legend. The family is scatter because the object is "
                "a point cloud, not a fitted surface — the text calls it 'a continuous smooth "
                "surface' but no surface is drawn."),

    figure(16, 2, "composite-panel",
           caption("Figure 13: Relationship between Average Speed and"),
           mention(16, first=16, style=["Fig."], count=5, pattern="as-shown-in", read=2,
                   lead=span(16, "Some typical curves of that are shown in Fig. 13.", "Fig. 13."),
                   trail=span(16, "In Fig. 13, we can see clearly that the percentage of SDVs",
                              "the traffic")),
           path=P_R_NEXT, kind="result", legend="inside", panels=2, layout="1x2",
           note="one measured region holding two separately captioned charts printed side by "
                "side, hence composite-panel and panel_count 2: Figures 13 and 14. Captions are "
                "split across the column break and quoted as printed — 'Figure 13: Relationship "
                "between Average Speed and' then 'the Traffic Flow under Certain Ratios of "
                "SDVs' — and Figure 14's fragment is 'Figure 14: Relationship between Maxi-' "
                "continuing 'mum Traffic Flow and Percentage of SDVs'. Left panel: five curves "
                "for P_SDV = 0/10/50/70/90% with the key inside, tipping points marked with "
                "printed crosses. Right panel: maximum flow against SDV percentage, no key of "
                "its own, so the five series are identified only by the key of Figure 13 beside "
                "them."),



    figure(17, 1, "scatter",
           caption("Figure 15: One of the Results of the Multilane Traffic Model Simulation"),
           mention(17, first=17, style=["Fig."], count=3, pattern="as-shown-in", read=2,
                   lead=span(17, "In Fig. 15 is one of the results of the Following Model",
                             "of the Following Model"),
                   trail=span(17, "In section A of Fig. 15, an overtaking happens",
                              "Multilane Traffic Model.")),
           path=P_R_MULTI, kind="result", legend="inside", printed=True,
           note="the multilane twin of Fig. 11: four lanes of dots over time, with two zoomed "
                "callouts pasted into the raster (A overtaking, B an SDV-Train). The text calls "
                "it 'the Following Model' although it is the multilane simulation. The two "
                "callouts are separate raster regions inside the screenshot."),

    figure(18, 1, "composite-panel",
           caption("Figure 16: Relationships Between Total Traffic"),
           mention(18, first=17, style=["Fig."], count=3, pattern="as-shown-in", read=1,
                   lead=span(17, "Obviously, a highway with more lanes has a larger total "
                             "traffic flow", "Fig. 16"),
                   trail=span(18, "As we can see in Fig. 17", "about 50%")),
           path=P_R_MULTI, kind="result", legend="inside", panels=2, layout="1x2",
           note="one measured region holding Figures 16 and 17 printed side by side, hence "
                "composite-panel and panel_count 2. Captions as printed are the fragments "
                "'Figure 16: Relationships Between Total Traffic' continuing 'Flow and the "
                "Percentage of SDVs', and 'Figure 17: Relationships Between Relative Traffic' "
                "continuing 'Flow Per Lane and the Percentage of SDVs'. Left: five curves, one "
                "per lane count 1-5, key inside. Right: relative flow on a 0.97-1.01 axis, a "
                "vertical range thirty times smaller than its neighbour's while both start at "
                "0% on x."),



    figure(18, 2, "line",
           caption("Figure 18: The Influence of Setting an SDV Lane"),
           mention(18, first=19, style=["Fig."], count=2, pattern="as-shown-in", read=1,
                   lead=span(19, "As shown in Fig. 18", "Fig. 18"),
                   trail=span(20, "Fig. 18 suggests that when the percentage of SDVs is larger "
                              "than about 30%", "SDV Lane should be built")),
           path=P_R_LANE, kind="result", legend="inside",
           note="ten curves: five lane counts, each plain and with one dedicated SDV lane. The "
                "only single-panel figure in chapter 5. First cited on the page after it prints."),

    figure(19, 1, "line",
           caption("Figure 19: Appliance of Our Model on Interstate 5"),
           mention(19, first=19, style=["Fig."], count=3, read=1,
                   trail=span(20, "From Fig. 19 and Fig. 20", "extremely high traffic flow")),
           path=P_APPL, kind="solution", legend="inside", panels=2, layout="1x2",
           note="two panels, DECR (left) and INCR (right), each with the measured flow in black "
                "against simulated P_SDV = 100/50/0%, key inside the right panel only. The "
                "measured black curve carries no marker, so the reading sentence is the only "
                "place the two are distinguished."),

    figure(19, 2, "line",
           caption("Figure 20: Appliance of Our Model on Interstates 90, 402 and State Route 520"),
           mention(19, first=19, style=["Fig."], count=3, read=1,
                   trail=span(20, "From Fig. 19 and Fig. 20", "extremely high traffic flow")),
           path=P_APPL, kind="solution", panels=6, layout="2x3",
           note="six panels in a 2x3 grid: rows DECR / INCR, columns the three roads. No key at "
                "all and no per-panel caption, so the panel identity rests entirely on the two "
                "printed row labels and the three printed column labels. The caption names "
                "'Interstates 90, 402 and State Route 520' while the third-column panel is "
                "labelled 'Interstate 405' inside the figure."),

    table(20, 1,
          caption("Table 3: the Influence of the Changing of the Parameters in LCP in 3-lane "
                  "Road", numbering="Table N:"),
          mention(20, first=20, style=["Tab."], count=1, pattern="direct", read=0,
                  lead=span(20, "By changing the parameters by 15%", "in the following Tab. 3")),
          grid(8, 6, numeric=5, txt=1, width="full", decimal=True),
          path=P_SENS_LCP, kind="sensitivity",
          note="one row per perturbation of one LCP parameter (two directions each), never a "
               "block of joint perturbations: robustness is shown factor by factor. The last "
               "two rows are the ones that move (P2 3 up +4.7%, down -7.9%) while everything "
               "else stays inside 0.4%, so the table contradicts the sentence that introduces "
               "it only in the fourth digit."),

    table(20, 2,
          caption("Table 4: the Influence of the Changing of the Speed Limit",
                  numbering="Table N:"),
          mention(20, first=20, style=["Tab."], count=1, pattern="direct", read=0,
                  lead=span(20, "And in Tab. 4, we can find that our model performs quite well",
                             "different kind of road")),
          grid(4, 4, numeric=3, txt=1, units_hdr=True, width="full"),
          path=P_SENS_LIM, kind="sensitivity",
          note="the whole sensitivity study of the speed limit is three rows: original, -50%, "
               "+50%. The unit of the dependent variable is in the header ('Average Time(turns)') "
               "which is the only place in the paper a unit sits in a header rather than a column."),

    figure(22, 1, "map-or-plan-view", caption("", numbering="none"),
           mention(22, first=22, style=[], count=1, pattern="as-shown-in", read=1,
                   lead=span(22, "As the figure shows", "shows")),
           path=P_LETTER, kind="other", printed=True,
           source="none",
           note="a map of the Seattle area with the four studied roads lettered, sitting in the "
                "page margin of the letter to the governor. Uncaptioned, unnumbered, and cited "
                "only as 'the figure', the one exhibit in the paper with no number at all."),
]

RULES = [
    "全篇两张皮：第 4 章是示意图（[geometry.family]=flowchart-or-schematic，11 条记录），"
    "第 5 章起是折线图（[geometry.family]=line，3 条记录：Figs 18/19/20）加 2 张栅格时间-空间图"
    "（[geometry.family]=scatter，Figs 11/15）、2 个双图合并区（[geometry.family]=composite-panel，"
    "p16 与 p18）和 1 张地图（[geometry.family]=map-or-plan-view），"
    "章节边界就是图型边界，5.1 之前没有一张坐标系图。",

    "第 4 章的示意图是同一个模板复制九次：每条规则一行车道、行末印规则名、上方印 Dmin/Dmax 括线"
    "（[geometry.printed_numbers]=True 在 Figs 2-10 的 9 条记录上成立），"
    "所以“图多”不等于“信息多”，九张图只承载一个符号系统。",

    "模板的图例位置随模板换代：车道条带图靠行末文字标注、不用键框，记作外置右"
    "（[geometry.legend]=outside-right 在 Figs 2-10 的 9 条记录上成立）；"
    "Fig 1 与 Fig 6 用键框，且键框画在图形下方（[geometry.legend]=below 在 2 条记录上成立），"
    "因为这两张没有逐行文字可用。",

    "第 5 章的图一律把图例印在图内（[geometry.legend]=inside 在 Figs 11/13/16/18/19 上成立），"
    "唯一不印图例的是 Fig 20 的 6 联图（[geometry.legend]=none），它的面板身份靠行、列标签，"
    "不靠图例。",

    "三维只用了一次：全篇只有 Fig 12 是三维（[geometry.three_d]=isometric，其余记录全是 no），"
    "而它同时是唯一带色标的图（[geometry.colorbar]=True 只在 Fig 12 上成立）。"
    "要画三变量关系时才上三维加色标，二维能用就不用。",

    "多面板只在第 5 章出现，且只为并排比较服务：2 联 3 次（[geometry.panel_layout]=1x2 在 "
    "p16 双图区、p18 双图区与 Fig 19 上成立），6 联 1 次（[geometry.panel_layout]=2x3，Fig 20），"
    "第 4 章 9 张示意图全部单面板（[geometry.panel_count]=1）。",

    "共用坐标轴全篇不存在（[geometry.shared_axes]=False 在全部 19 条记录上成立）："
    "即使是 Figs 13/14 与 Figs 16/17 这样并排打印的成对图，也各自带自己的横纵轴标签，"
    "读者必须自己对齐两者的量纲。",

    "题注在图下、表上，无一例外（[caption.position]=below 在 19 条图记录上成立、"
    "above 在 4 条表记录上成立），编号格式全篇统一为 Figure N: 与 Table N:"
    "（[caption.numbering]），没有一处写 Fig. N。",

    "题注只报对象不报结论（[caption.concludes]=False 在全部题注上成立），"
    "句长 6-15 词、单句（[caption.words]），只有 Fig 20 点名了三个具体地点"
    "（[caption.words]=14），其余都由变量与修饰语构成："
    "Relationships Between X and Y 或 X for Y under certain conditions。",

    "题注点变量的方式不统一：折线图用 Relationships Between … and …（[caption.variables]），"
    "示意图改用 Rules for … 或 Diagram of … Variables（[caption.variables]=False 在 Figs 2-10 "
    "的 9 条记录上成立，因为图里没有可比的自变量）——图型换代，题注句式跟着换代。",

    "表只有四张，全是符号表或敏感性小表，全部 booktabs 单双线、无竖线、无斑马纹、无合并单元格、"
    "无对角表头（[table.rule_style]=booktabs、[table.zebra]=False、[table.merged_cells]=False、"
    "[table.diagonal_header]=False 在 4 条表记录上成立），占版心宽度 [table.width] 分 full 与 half 两档。",

    "单位的位置两套写法并存：符号表把单位单列成第三列（[table.units_in_header]=False 在 Table 1/2 "
    "上成立），敏感性小表把单位挂进表头括号（[table.units_in_header]=True 只在 Table 4 上成立，"
    "'Average Time(turns)'）。同一篇里两种写法，没有看出选择依据。",

    "表的规模说明用途：两张符号表 10 行与 5 行、3 列（[table.rows]、[table.cols]），"
    "两张敏感性表 8 行 6 列与 4 行 4 列，行数上限由“一次只动一个参数”的写法决定，"
    "不是由数据量决定——敏感性分析被压成每参数两行。",

    "引用密度的规律跟着图型走：示意图按车道逐条引，Fig 2 被引 4 次、Fig 3 被引 5 次、"
    "Fig 4 被引 3 次（[mention.count]）；第 5 章的图多数整体引 2-3 次（[mention.count]=2 或 3 "
    "在 Figs 18/19/20 与 p18 双图区上成立），没有一个超出 5 次。",

    "跨页引用有固定方向：19 个对象里 13 个在印出那一页就首次被引（[mention.lead_pages]=0），"
    "5 个提前一页（[mention.lead_pages]=1：Figs 6/7/9/10 与 p18 双图区），"
    "只有 Fig 18 晚一页（[mention.lead_pages]=-1）——浮图总是被往前推，只有一例被往后甩。",

    "引出句只有一个模板：as shown in Fig. N 或 … is shown in Fig. N"
    "（[mention.lead_pattern]=as-shown-in 在 13 条记录上成立），三个变体各一次："
    "Fig 11 用图号作主语（[mention.lead_pattern]=figure-n-shows）、Fig 3 直接点名"
    "（[mention.lead_pattern]=direct）、Fig 4 把引用塞进条件清单的从句里"
    "（[mention.lead_pattern]=parenthetical），其余 3 个只有读句没有引出句"
    "（[mention.lead_pattern]=none）。",

    "图后紧跟解读句，且解读句总是把图里的定性形状读成结论而不是复述数值"
    "（[mention.trail_sentence]）：19 个对象里 18 个带读句（[mention.read_sentences]>=1），"
    "只有 Fig 1 没有；读句一律以 As we can find / As we can see / In Fig. N 起头，"
    "Fig 3 的读句最多（[mention.read_sentences]=4），因为它逐条车道解释四种加速条件。",

    "全篇没有一张表格当图、没有一张照片、没有一张网络图、没有一张直方图："
    "19 条图记录只落在 [geometry.family] 的 5 个取值上（flowchart-or-schematic 11、"
    "composite-panel 2、line 3、scatter 2、map-or-plan-view 1），"
    "分布信息一律折线化（Figs 13/14/16/17），时间-空间信息一律栅格截图（Figs 11/15），"
    "关系信息一律示意图（第 4 章）——选型是按要回答什么问题、不是按图好不好画决定的。",

    "印刷缺陷不修，只记：Table 1/2 被正文按节号引用为 Tab. 4.1.1 与 Tab. 4.2.1"
    "（[caption.numbering] 仍是 Table N:）；Fig 20 的题注写 402 而图内第三列印 405"
    "（[caption.verbatim] 与 note）；Fig 15 的引出句把它叫 Following Model"
    "（[mention.lead_sentence]）。这些是原文的事实，记录照录并在 note 里点名。",
]

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": [e for e in ALL if "table" not in e],
    "tables": [e for e in ALL if "table" in e],
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": "hand pass",
}

# doc_order is the exhibit's rank in the paper, page_order its rank on its own page; the two
# pairs printed side by side (Figs 13+14, 16+17) share a region but keep their printed order.
_seen: dict[int, int] = {}
for _i, _e in enumerate(ALL, 1):
    _p = _e["page"]
    _seen[_p] = _seen.get(_p, 0) + 1
    _e["place"]["doc_order"] = _i
    _e["place"]["page_order"] = _seen[_p]

if __name__ == "__main__":
    out = LANE / f".proxy/{PID}-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out} items={len(payload['items'])} tables={len(payload['tables'])} "
          f"excluded={len(EXCLUDED)} rules={len(RULES)}")
