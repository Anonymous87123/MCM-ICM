"""Hand pass for P-B-2012-13955-a0e5e63c (Big Long River scheduling, 18 pp).

The geometry pass measures 12 regions over 10 pages. The paper numbers eleven exhibits
`Figure 2.1` … `Figure 4.4` and prints them in four groups:

    Figure 2.1  p7-r1   campsite-occupancy strip, group B moves up to campsite 6
    Figure 2.2  p7-r2   the same strip one step later, caption on the top of p8
    Figure 2.3  p8-r1   the strip at the river's end, campsite 170 … Off the River
    Figure 2.4  p9-r1   full-page flowchart of the scheduling algorithm
    Figure 3.1  p10-r1  printed table, campsite numbers and priorities per night
    Figure 3.2  p11-r1  group locations against night, four step polylines
    Figure 3.3  p11-r2  priority against night, four spiky polylines
    Figure 4.1  p12-r1  printed table of eleven simulation runs
    Figure 4.2  p13-r1  printed 5x5 table of peak capacity against Y and R
    Figure 4.3  p14-r1  filled contour plot of the fitted surface
    Figure 4.4  p15-r1  printed 5x4 table of capacity against D and R

Accounting: 7 figure items + 4 counted tables + 1 exclusion = 12 regions. Eleven printed
numbers attach one-to-one to the eleven counted exhibits.

Four of the eleven numbers sit on printed tables (3.1, 4.1, 4.2, 4.4). The lane rule is
that a table printed as a grid uses `table-grid` even when the paper numbers it as a
figure, so those four are recorded in the table block and the paper contributes 0
`table-as-figure` rows.

The twelfth region, p16-r1, is a measured box holding nothing but section 6.1's heading
and one paragraph of running prose; it is excluded `not-an-exhibit`.

Families, read off cropped page proxies:

* `flowchart-or-schematic` is the three campsite strips and the p9 algorithm flowchart.
  The strips are ruled two-row diagrams — "Campsite #:" over "Group Assigned:" — with two
  colour-filled cells and a "Downstream ->" arrow; no axes, no plotted marks.
* `line` is Figures 3.2 and 3.3: four series each, printed tick numbers, series legend
  outside the frame, axis titles "Campsite Number" / "Priority" against "Night".
* `heatmap-or-contour` is Figure 4.3: five labelled contour curves over a smooth five-band
  colour wash, axis titles "Number of campsites on river" and the five R ratios.

Usage: python -I tools/_dist_paper34.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2012-13955-a0e5e63c"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}
HEADKIND = {h["label"]: h["kind"] for h in CTX["headings"]}


def ctext(page: int, start: str, stop: str | None = None) -> str:
    """The printed caption as the text layer carries it, cut at `start`..`stop`.

    Captions here run over two to four printed lines, so this cuts the normalised page
    text rather than one line.
    """
    text = schema.page_text(PID, page)
    i = text.find(start)
    if i < 0:
        raise KeyError((page, start))
    cut = text[i:]
    if stop:
        j = cut.find(stop)
        if j < 0:
            raise KeyError((page, stop))
        cut = cut[:j]
    return cut.strip()


PATH = {
    7: ["2 Methods", "2.2 Priority"],
    8: ["2 Methods", "2.3 Priorities & Other Considerations"],
    9: ["2 Methods", "2.3 Priorities & Other Considerations"],
    10: ["3 Scheduling Simulation"],
    11: ["3 Scheduling Simulation"],
    12: ["4 Case Study", "4.1 The Grand Canyon"],
    13: ["4 Case Study",
         "4.2 Sensitivity Analysis of Carrying Capacity With Respect to R and Y"],
    14: ["4 Case Study",
         "4.2 Sensitivity Analysis of Carrying Capacity With Respect to R and Y"],
    15: ["4 Case Study",
         "4.3 Sensitivity Analysis of Carrying Capacity With Respect to R and D"],
    16: ["6 Limitations and Error Analysis", "6.1 Carrying Capacity Overestimation"],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic
VENTION = {7: 2, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route = PATH[page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": HEADKIND[route[-1]],
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, position: str, numbering: str = "Figure N:") -> dict:
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": position,
    }


def figure(page: int, reg: int, family: str, caption: str, *, panels: int = 1,
           layout: str = "1", legend: str = "none", numbers: bool = False,
           labels: bool = False, mention: dict | None = None, note: str = "",
           position: str = "below") -> None:
    ORDER.append((page, reg))
    blocking = dict(mention) if mention else dict(NULL_MENTION)
    if blocking["first_page"] is not None and blocking["lead_pages"] is None:
        blocking["lead_pages"] = page - blocking["first_page"]
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption, position),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, caption: str, *, rows: int, cols: int,
          header_rows: int = 1, rule_style: str = "boxed", numeric_cols: int = 0,
          text_cols: int = 1, merged: bool = False, mention: dict | None = None,
          note: str = "", position: str = "below") -> None:
    blocking = dict(mention) if mention else dict(NULL_MENTION)
    if blocking["first_page"] is not None and blocking["lead_pages"] is None:
        blocking["lead_pages"] = page - blocking["first_page"]
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": caption,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption, position),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rule_style, "zebra": False, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "full", "orientation": "portrait",
            "continued": False, "note_sentence": "",
        },
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            trail: str = "", count: int = 1, gap: int | None = None) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": trail,
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": gap}


STRIP = ("a full-width two-row strip inside a light frame: the top row prints the header "
         "cell 'Campsite #:' followed by the six numbered campsites, the bottom row prints "
         "'Group Assigned:' and holds one text cell per campsite, two of the cells filled "
         "pale blue and orange, and a 'Downstream ->' arrow sits at the left edge. No "
         "axes and no plotted marks: every value is printed inside its cell.")


def build() -> str:
    # 2.2 Priority - the three occupancy strips
    figure(7, 1, "flowchart-or-schematic",
           ctext(7, "Figure 2.1:", "Campsite #:"),
           labels=True,
           note="State strip for campsite 6: the furthest open campsite is campsite 6, "
               "Groups A, B and C can all reach it, and the strip fills cell 6 orange and "
               "cell 2 pale blue with 'Group A P_A = 1.1', 'Group B P_B = 1.5 (moves to "
               "campsite 6)' and 'Group C P_C = .8' under the campsites. " + STRIP)
    figure(7, 2, "flowchart-or-schematic",
           ctext(8, "Figure 2.2:", "2.3 Priorities"),
           labels=True,
           note="The same strip one step later, printed at the foot of p7 with its caption "
               "opened on p8: camp 5 is now the furthest open campsite and holds 'Group A "
               "P_A = 1.1 (moves to campsite 5)', camp 1 carries the pale-blue cell, camp 6 "
               "holds Group B, and two cells read 'Open'. " + STRIP)
    figure(8, 1, "flowchart-or-schematic",
           ctext(8, "Figure 2.3:", None),
           labels=True,
           note="The end-of-river strip: campsites 170, 171, an ellipsis, 223, 224 and 'Off "
               "the River', with 'Group D: P_D = 1.1, t_D = 12, d_D = 11 (doesn't move off "
               "the river)' under campsite 170 and the orange 'Furthest Open Camp Site' cell "
               "under 'Off the River'. Caption is the last text on p8. " + STRIP)

    # 2.4 - the algorithm flowchart
    figure(9, 1, "flowchart-or-schematic",
           ctext(9, "Figure 2.4:", None),
           layout="1", legend="inside", labels=True,
           note="Full-page flowchart titled 'Scheduling Algorithm' with a grey 'Legend' box "
                "at the top right listing n, a, d, p, c, G. Rounded boxes run 'Simulation "
                "Starts: Start With Campsite at Final Exit' -> 'Find the (next) Empty "
                "Campsite Up River From the Input Campsite (Call It c)' -> circle "
                "'Determine Set G' (fed by 'Groups on River' and 'Groups on Waitlist') -> "
                "'Find Group with Highest Priority in the Set G (Call It g)' -> 'Move g to "
                "c', with a red diamond 'n = n + 1' carrying the rotated test 'If n = last "
                "day of simulation', then 'Return Simulation Results:' branching to three "
                "outcome boxes. Green, pale blue, red and grey fills; condition text on the "
                "arrows. The caption line prints above the diagram at the top of p9.")

    # 3.1 - the priority table
    table(10, 1, ctext(10, "Figure 3.1:", "I.e. the column labeled"),
          rows=20, cols=9, rule_style="vertical-rules", numeric_cols=4, text_cols=5,
          note="Printed grid carrying its own title, 'Campsite numbers and priority values "
               "for each group': a night index column against four group pairs g1/P1 … "
               "g4/P4, twenty night rows, the 'n =' row skipped and the cells holding "
               "campsite integers, priority decimals, blanks and the word 'OFF'. A rotated "
               "stub label reads 'Number of nights spent on river'. Full boxed grid.")

    # 3.2 and 3.3 - the two line plots
    figure(11, 1, "line", ctext(11, "Figure 3.2:", None),
           legend="outside-right", numbers=True, labels=True,
           note="'Group locations (Figure 3.1)' plot: four thick coloured step polylines, "
                "one per group, rising in stairs across Night 0-19 on a printed 0-50 "
                "campsite axis with light grey gridlines at every five units; a right-hand "
                "legend keys Group 1-4 by colour; axis titles 'Campsite Number' and "
                "'Night'. No markers on the lines.")
    figure(11, 2, "line", ctext(11, "Figure 3.3:", None),
           legend="outside-right", numbers=True, labels=True,
           note="'Priority (Figure 3.1)' plot: four thin coloured polylines of priority "
                "against Night 0-19, spiky rather than smooth, P1-P4 keyed by a right-hand "
                "legend; y axis prints 0 to 4.5 in steps of 0.5 with grey gridlines, axis "
                "titles 'Priority' and 'Night'. Values are said to converge to p = 1.")

    # 4.1 - the simulation table
    table(12, 1, ctext(12, "Figure 4.1:", "We conclude that"),
          rows=11, cols=5, rule_style="boxed", numeric_cols=4, text_cols=1,
          note="Eleven simulation runs: 'Simulation #' 1-11 against 'Groups/day' 6 … 21, "
               "'Completed trips.' 996 … 3306, 'Late Trips' 0 … 14 and 'Total left on "
               "waitlist' 0 … 109. Two header cells wrap onto a second line. Full boxed "
               "grid with vertical rules.")

    # 4.2 and 4.3 - the sensitivity pair
    table(13, 1, ctext(13, "Figure 4.2:", "Since the peak carrying capacities"),
          rows=5, cols=6, header_rows=2, rule_style="boxed", numeric_cols=5, text_cols=1,
          merged=True,
          mention=mention(13, ["Figure 4.2"],
                          "To deal with these unknowns, we create the following table, "
                          "Figure 4.2.", "direct", count=2),
          note="Cross-tabulation of peak capacity M: a spanned header 'Number of campsites "
               "on river, Y' over the columns 100.00, 150.00, 200.00, 250.00, 300.00, a "
               "spanned stub 'Ratio, R (oar : motor)' over the five rows 1:4, 1:2, 1:1, "
               "2:1, 4:1, and two-decimal cell values. Boxed grid with vertical rules, "
               "merged header and stub cells.")
    figure(14, 1, "heatmap-or-contour", ctext(14, "Figure 4.3:", "Figure 4.3 is useful"),
           numbers=True, labels=True,
           mention=mention(13, ["Figure 4.3"],
                           "Figure 4.3 is a contour diagram of this surface.", "direct"),
           note="Filled contour plot of the fitted surface: a smooth wash in five colour "
                "bands from cream at the top to purple at the bottom, overlaid with five "
                "thin grey contour curves labelled 3500, 3000, 2500, 2000 and 1500 at their "
                "crests. Y axis prints 100-300 campsites, x axis the five ratio categories "
                "1:4 … 4:1. No legend and no colour bar; the caption names the ridge along "
                "R = 1:1.")

    # 4.4 - the trip-length table
    table(15, 1, ctext(15, "Figure 4.4:", "Figure 4.4 is intended"),
          rows=5, cols=5, header_rows=2, rule_style="vertical-rules", numeric_cols=4,
          text_cols=1, merged=True,
          mention=mention(15, ["Figure 4.4"],
                          "The results of this simulation are displayed in Figure 4.4.",
                          "direct"),
          note="Peak capacity against trip-length mix: a spanned header 'Distribution of "
               "trip lengths, D' over the columns 12, 12-18, 6-12, 6-18, a spanned stub "
               "'Ratio (oar : motor)' over the rows 1:4 … 4:1, integer cell values (2004, "
               "1998, 2541, 2362 in the first row). Horizontal rules above and below, "
               "vertical rules around the stub column.")

    # 6.1 - prose measured as a box
    excluded(16, 1, "not-an-exhibit",
             "measured block holding only the 6.1 heading and one paragraph of running "
             "prose about carrying-capacity overestimation; no graphic on it.")

    rules = [
        "Four of the eleven printed figures are printed tables (3.1, 4.1, 4.2, 4.4), so "
        "they are recorded in the table block as table-grid and this paper contributes no "
        "table-as-figure rows [table.rows].",
        "The three campsite strips are ruled occupancy diagrams with colour-filled cells "
        "and a Downstream arrow, so they are flowchart-or-schematic rather than plots "
        "[geometry.family].",
        "Figures 3.2 and 3.3 carry a series legend outside the frame and printed tick "
        "numbers on both axes [geometry.legend] [geometry.printed_numbers].",
        "Figure 4.3 is a filled contour plot with five inline contour labels and no colour "
        "bar [geometry.colorbar] [geometry.data_labels].",
        "Figure 2.3's caption is the last text on p8 while its strip is at the bottom of "
        "p8, and Figure 2.2's caption opens p8 above the strip of p7: captions are quoted "
        "from the page that carries them [caption.verbatim].",
        "Figure 2.4's caption prints above the flowchart at the top of p9, the only "
        "exhibit in this paper whose caption sits above it [caption.position].",
        "Figure 4.2 and Figure 4.4 each carry a two-row header with spanned and stub cells, "
        "so header_rows is 2 and merged_cells is true [table.header_rows] "
        "[table.merged_cells].",
        "The three rule styles in the paper are boxed grids (3.1, 4.1, 4.2), vertical "
        "rules with a stub column (3.1, 4.4) and no zebra shading anywhere "
        "[table.rule_style] [table.zebra].",
        "Only Figures 4.2, 4.3 and 4.4 are cited in running text; the strip figures are "
        "read only through their captions [mention.lead_sentence].",
        "p16-r1 measures as a box but holds section 6.1's heading and one prose paragraph, "
        "so it is excluded not-an-exhibit rather than recorded as a figure "
        "[place.area_frac].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-13955-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twelve measured regions, twelve accounted: seven figure items, four counted "
            "tables and one exclusion. The paper prints eleven numbered exhibits and all "
            "eleven are measured, four of them as printed tables (3.1, 4.1, 4.2, 4.4) "
            "recorded in the table block under the grid-numbered-as-a-figure rule. The "
            "three campsite strips are one diagram form printed three times, each with its "
            "own caption and number, so they are three items and not one split exhibit; "
            "Figure 2.2's caption is the first line of p8 and Figure 2.3's is the last line "
            "of the same page. p16-r1 measures as a block but carries only section 6.1's "
            "heading and a paragraph of prose, so it is excluded."
        ),
    }
    out = PROXY / "pb34-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
