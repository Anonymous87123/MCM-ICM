"""Hand pass for P-A-2014-25142-c5c79dc7 (a cellular-automata freeway paper: minimum safe gap,
overtaking probability, keep-right versus unrestricted rules, danger index, speed-limit
sensitivity), 34 pp.

Twenty-nine measured regions over 18 pages: 18 figure rows, 1 printed table and 10 exclusions
(the typed MATLAB listing bands on p27-p34). The arithmetic `check.py` enforces is 18 + 1 + 10.

    p5-r1   table    Table 1: Notation
    p11-r1  line     Figure 1: safe-gap versus velocity
    p12-r1  other    Figure 2: the overtaking velocity triangle
    p15-r1  line     Figure 3: tempo-spatial distribution of vehicles
    p16-r2  line     Figure 4: average velocity, 2 lanes (left of the pair)
    p16-r1  line     Figure 5: average velocity, 3 lanes (right of the pair)
    p17-r1  line     Figure 6: average velocity of fast cars
    p18-r2  bar      Figure 7: density in each lane, 2 lanes keep-right (left)
    p18-r1  bar      Figure 8: density in each lane, 2 lanes unrestricted (right)
    p18-r4  bar      Figure 9: density in each lane, 3 lanes keep-right (left)
    p18-r3  bar      Figure 10: density in each lane, 3 lanes unrestricted (right)
    p19-r1  bar      Figure 11: passing events under different rules
    p20-r2  bar      Figure 12: danger index, 2 lanes (left)
    p20-r1  bar      Figure 13: danger index, 3 lanes (right)
    p20-r3  line     Figure 14: average velocity, speed limits, keep-right (left)
    p20-r4  line     Figure 15: average velocity, speed limits, unrestricted (right)
    p21-r1  bar      Figure 16: danger index, speed limits, keep-right (left)
    p21-r2  bar      Figure 17: danger index, speed limits, unrestricted (right)
    p24-r1  line     Figure 18: average velocity under an intelligent system

Excluded: the ten typed MATLAB listing bands on p27, p29, p30, p31 (3), p32 (2), p33, p34.

Declared gaps: Tables 2 and 3 (p10, acceleration and deceleration probabilities for fast and
slow vehicles) and Tables 4 and 5 (p23, the same two probabilities under the intelligent system)
print caption lines and typed cell rows in the text layer but `fig_extract` measures no region on
either page, so they are recorded as a gap rather than given an invented bbox.

Usage: python -I tools/_dist_paper51.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2014-25142-c5c79dc7"
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

TERM = "1.1 Terminology"
DI = "2.4.3 Danger Index"
IMPL = "4 Model Implementation with Computer"
VAL = "5 Data Analysis and Model Validation"
AV = "5.1 Average Velocity"
FAST = "5.2 Average Velocity of Fast Cars"
DENS = "5.3 Density"
OVER = "5.4 Overtaking Rate"
DANGER = "5.5 Danger Index"
SENS = "6 Sensitivity Evaluation of the Model under Differ-"
INTEL = "8 Transportation under Intelligent System"
RESULT = "8.3 Result of Intelligent System"

PATH: dict[int, tuple[list[str], str]] = {
    5: ([TERM], "symbols"),
    11: ([DI], "other"),
    12: ([DI], "other"),
    15: ([IMPL], "model"),
    16: ([VAL, AV], "test"),
    17: ([VAL, FAST], "test"),
    18: ([VAL, DENS], "test"),
    19: ([VAL, OVER], "test"),
    24: ([INTEL, RESULT], "result"),
}
PATH_ONE = {
    (20, 1): ([VAL, DANGER], "test"),
    (20, 2): ([VAL, DANGER], "test"),
    (20, 3): ([SENS], "evaluation"),
    (20, 4): ([SENS], "evaluation"),
    (21, 1): ([SENS], "evaluation"),
    (21, 2): ([SENS], "evaluation"),
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

VENTION = {5: 1, 11: 1, 12: 1, 15: 1, 16: 2, 17: 1, 18: 4, 19: 1, 20: 4, 21: 2, 24: 1,
           27: 1, 29: 1, 30: 1, 31: 3, 32: 2, 33: 1, 34: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}

# The paired captions print on a single text line and each column is broken mid-word, so a row
# quotes the fragment that carries its own figure number and the tail lives in its note.
CAP_111 = "Figure 1: Relationship between safe-gap and velocity"
CAP_122 = "Figure 2: Velocity Analysis when facing emergency."
CAP_153 = "Figure 3: Tempo-Spatial Distribution of Vehicles"
CAP_164 = "Figure 4: Average Velocity under Different"
CAP_165 = "Figure 5: Average Velocity under Different"
CAP_176 = "Figure 6: Average Velocity of Fast cars"
CAP_187 = "Figure 7: Density of Traffic in Each Lanes(2"
CAP_188 = "Figure 8: Density of Traffic in Each Lanes(2"
CAP_189 = "Figure 9: Density of Traffic in Each Lanes(3"
CAP_1810 = "Figure 10: Density of Traffic in Each Lanes(3"
CAP_1911 = "Figure 11: Passing Events With Different Rules(3 lanes, 300s)"
CAP_2012 = "Figure 12: Danger Index under Differen-"
CAP_2013 = "Figure 13: Danger Index under Differen-"
CAP_2014 = "Figure 14: Average Velocity under Different"
CAP_2015 = "Figure 15: Average Velocity under Different"
CAP_2116 = "Figure 16: Danger Index under Differen-"
CAP_2117 = "Figure 17: Danger Index under Differen-"
CAP_2418 = "Figure 18: Average Velocity under Different Rules in an Intelligent System"

M_DANGER = {
    "first_page": 12, "lead_pages": 0, "style": ["figure 2"], "count": 1,
    "lead_sentence": "As is shown in the figure 2, V0 denotes the velocity before overtaking, "
                     "V1 denotes the velocity in the overtaking process",
    "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
    "gap_sentences": None}
M_AV4 = {
    "first_page": 16, "lead_pages": 0, "style": ["figure 4"], "count": 2,
    "lead_sentence": "are shown in the figure 4 and figure 5",
    "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
    "gap_sentences": None}
M_AV5 = {
    "first_page": 16, "lead_pages": 0, "style": ["figure 5", "figure 4 and 5"], "count": 2,
    "lead_sentence": "are shown in the figure 4 and figure 5",
    "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
    "gap_sentences": None}


def printed(page: int, text: str) -> str:
    """Verify a caption string really prints on the page, once Unicode-normalised."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text))
    return text


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH_ONE.get((page, reg)) or PATH[page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, source: str, position: str, numbering: str) -> dict:
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


def figure(page: int, reg: int, family: str, caption_text: str = "", *, source: str = "none",
           numbering: str = "none", position: str = "below", panels: int = 1,
           layout: str = "1", legend: str = "none", colorbar: bool = False,
           numbers: bool = True, labels: bool = False, other_note: str = "", note: str = "",
           mention: dict | None = None) -> None:
    ORDER.append((page, reg))
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg),
        "mention": mention or dict(NULL_MENTION),
        "caption": caption_block(caption_text, source, position, numbering),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, caption_text: str = "", *, source: str = "none",
          numbering: str = "none", rows: int, cols: int, header_rows: int = 1,
          rules: str = "booktabs", zebra: bool = False, numeric_cols: int = 0,
          text_cols: int = 0, merged: bool = False, continued: bool = False, note: str = "",
          mention: dict | None = None) -> None:
    ORDER.append((page, reg))
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": caption_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg),
        "mention": mention or dict(NULL_MENTION),
        "caption": caption_block(caption_text, source, "above", numbering),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rules, "zebra": zebra, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "full", "orientation": "portrait",
            "continued": continued, "note_sentence": "",
        },
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note})


def build() -> str:
    # --- section 1: the notation table ---------------------------------------------------
    table(5, 1, printed(5, "Table 1: Notation"), source="text-layer", numbering="Table N:",
          rows=19, cols=2, header_rows=1, rules="booktabs", numeric_cols=0, text_cols=2,
          note="The symbol list: header 'Symbol | Meaning' over eighteen entries - V, Vm, Vl, "
               "V0, V1, G, Gs, G0, Tr, Po, Pa, Pb, f, d, D, a, ap, ad - with the symbols set in "
               "italic and their subscripts set below the baseline. Three horizontal rules - "
               "above the header, under the header and closing at the foot - with no rule "
               "between rows and no vertical rule, so `rule_style` is `booktabs` and three "
               "vector paths carry them. The caption prints above the grid. Every row is prose, "
               "not a number, so `numeric_cols` is 0. This is live vector text, not a pasted "
               "image.")

    # --- section 2.4.3: the safe-gap curve and the overtaking triangle ---------------------
    figure(11, 1, "line", printed(11, CAP_111), source="text-layer", numbering="Figure N:",
           position="below",
           note="Two analytic curves on one frame, safe gap against velocity: Gs rising from 10 "
                "at rest on the 0.7-friction line, and the second curve for the lane-changing "
                "case (Gs = 10 + 3.4V) above it, with a dashed vertical guide drawn at the "
                "200 km/h normal-driving ceiling and the region beyond it left as extrapolation. "
                "No legend, no gridlines, no in-plot title; the two labels V and Gs sit beside "
                "the curves themselves.")
    figure(12, 1, "other", printed(12, CAP_122), source="text-layer", numbering="Figure N:",
           position="below",
           note="A labelled velocity triangle rather than a plot: three vectors drawn "
                "head-to-tail for the overtaking vehicle, V1 along the lane, V0 before the "
                "lane change and the difference a off it, with the component ap parallel to the "
                "lane marked and the angle at which the vehicle crosses called out. No axes, no "
                "ticks, no scale, no gridlines and no legend [geometry.family].",
           other_note="A geometric vector diagram - the velocity triangle used to split the "
                      "overtaking acceleration into its along-lane and across-lane components. "
                      "It is a labelled schematic with no axes and no plotted data, so it is "
                      "recorded `other` rather than forced into `line` or "
                      "`flowchart-or-schematic`.",
           mention=M_DANGER)

    # --- section 4: the tempo-spatial picture ---------------------------------------------
    figure(15, 1, "line", printed(15, CAP_153), source="text-layer", numbering="Figure N:",
           position="below", legend="none",
           note="The cellular-automaton output as a tempo-spatial diagram: red trajectories for "
                "smaller cars and green for larger vehicles, each vehicle's position over time "
                "traced as a sloping line, x axis 'Time(s)' 0 to 1000 and y axis 'Distance' 0 to "
                "1000, every third column marking one time cycle. No legend box - the colour key "
                "is in the prose paragraph above the caption, which states that red is a smaller "
                "car and green a larger one [geometry.legend]. The caption line that prints "
                "directly above the numbered one ('Figure spatiotemporal diagram of vehicles, "
                "expectation of inflow rate is 0.5 veh/s, the ratio of smaller cars to larger "
                "vehicles is 1, three-lane') carries no figure number and is part of the body "
                "text, so only the numbered line is quoted as the caption.")

    # --- section 5.1: average velocity, the first caption pair ----------------------------
    figure(16, 2, "line", printed(16, CAP_164), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="left of pair",
           note="Average velocity against inflow rate for the two-lane freeway, one line per "
                "rule, x axis 'E(veh/s)' and y axis 'V(m/s)', legend boxed inside the upper "
                "left ['V(m/s)' versus 'E(veh/s)']. This is the left-hand chart of the pair; the "
                "tail of its caption, printed on the following text line, reads 'Rules(2 lanes)' "
                "and belongs to this row [caption.verbatim].",
           mention=M_AV4)
    figure(16, 1, "line", printed(16, CAP_165), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="right of pair",
           note="The same velocity-versus-inflow plot for the three-lane freeway, same axis "
                "titles, same boxed legend inside the upper left. Right-hand chart of the pair; "
                "the caption tail on the next text line reads 'Rules(3 lanes )' and belongs "
                "here. The two charts share a frame style but not a y scale, so the scale is "
                "read per region [geometry.shared_axes].",
           mention=M_AV5)

    # --- section 5.2-5.4: fast cars, density, overtaking rate -----------------------------
    figure(17, 1, "line", printed(17, CAP_176), source="text-layer", numbering="Figure N:",
           position="below", legend="inside",
           note="Average velocity of the faster cars against inflow rate in the three-lane "
                "model, one line per rule, legend boxed inside the upper left, x 'E(veh/s)' and "
                "y 'V(m/s)'. The curve dips at low inflow and then climbs through the 0-0.5 "
                "veh/s range, which is the overtaking-desire effect the prose describes.")

    # p18 prints two caption pairs over two rows of two charts; within each row the left chart
    # carries the keep-right figure number and the right chart the unrestricted one, read off
    # the crop x positions.
    figure(18, 2, "bar", printed(18, CAP_187), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="left of row 1",
           note="Per-lane traffic density on the two-lane freeway under keep-right: vertical "
                "columns grouped by inflow rate, two series ('left lane' black, 'right lane' "
                "red) with a boxed legend inside the upper left, x 'E(veh/s)' on the tick set "
                "0.1, 0.3, 0.5, 0.7, 1.0, 1.4, 1.8, 2.5, 3.0 and y 'D (veh/m)' labelled 0.00 to "
                "0.08 by 0.02 up to an axis top near 0.10. No gridlines, no in-plot title. "
                "Left-hand chart of the first pair; the caption tail on the next line reads "
                "'lanes, keep-right)' [caption.verbatim].")
    figure(18, 1, "bar", printed(18, CAP_188), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="right of row 1",
           note="The same grouped column construction for the two-lane unrestricted case, same "
                "axis titles and the same nine x ticks and the same inside-upper-left legend, "
                "but this chart labels every 0.01 tick up to 0.10 where its neighbour labels "
                "0.02 steps, so the two panels of the pair are not interchangeable. Right-hand "
                "chart of the first pair; caption tail 'lanes, unrestricted)'.")
    figure(18, 4, "bar", printed(18, CAP_189), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="left of row 2",
           note="Density per lane on the three-lane freeway under keep-right: three series "
                "('left lane' black, 'middle lane' red, 'right lane' blue) with the boxed legend "
                "inside the upper left, y 'D (veh/m)' 0.000 to 0.095 in 0.005 steps and the same "
                "nine x ticks. This is the panel that shows the unbalanced load the prose "
                "reports, the keep-right column in the right lane running far above the other "
                "two. Left-hand chart of the second pair; caption tail 'lanes, keep-right)'. The "
                "top edge of the crop carries a stray mark from the caption line above it, not "
                "chart content.")
    figure(18, 3, "bar", printed(18, CAP_1810), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="right of row 2",
           note="Density per lane on the three-lane freeway under the unrestricted rule, three "
                "series, legend inside the upper left, y 'D (veh/m)' 0.00 to 0.07 by 0.01 - a "
                "narrower range than its left-hand neighbour. Right-hand chart of the second "
                "pair; caption tail 'lanes, unrestricted)'.")

    figure(19, 1, "bar", printed(19, CAP_1911), source="text-layer", numbering="Figure N:",
           position="below", legend="inside",
           note="Passing events counted over five simulated minutes: stacked vertical columns, "
                "one column per inflow rate, three series stacked bottom to top in yellow, red "
                "and blue ('unrestricted(left)', 'unrestricted(right)', 'keep-right'), with a "
                "single horizontal legend row inside the upper left of the frame. x 'E(veh/s)' "
                "on the tick set 0.1, 0.3, 0.5, 0.7, 1.0, 1.4, 1.8, 2.5, 3.0, 3.6; the y axis "
                "carries no title at all, only ticks 0 to 25000 by 5000, and there are no "
                "gridlines. The only stacked column chart on the paper.")

    # --- section 5.5 and 6: danger index, then the speed-limit sensitivity ----------------
    figure(20, 2, "bar", printed(20, CAP_2012), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="left of row 1",
           note="Danger index on the two-lane freeway: grouped columns, two series ('unstrict' "
                "black, 'keep-right' red) with the boxed legend inside the upper RIGHT - the "
                "only panel in this group that puts it there - over y 'Danger Index' 0 to 700 by "
                "100 and x 'E(veh/s)'. No gridlines, no title. Left-hand chart of the first "
                "pair; the caption is broken mid-word in both columns and the tail printed on "
                "the next line reads 't Rules(2 lanes)' [caption.verbatim].")
    figure(20, 1, "bar", printed(20, CAP_2013), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="right of row 1",
           note="The same danger-index comparison for three lanes, two series, legend inside "
                "the upper left, y 'Danger Index' 0 to about 900 in 200 steps and the same x "
                "tick set. Right-hand chart of the first pair; caption tail 't Rules(3 lanes)'.")
    figure(20, 3, "line", printed(20, CAP_2014), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="left of row 2",
           note="Average velocity under three upper speed limits on the keep-right three-lane "
                "freeway: polylines, legend inside the upper right naming 'Speed limits 29m/s' "
                "(black squares), '32m/s' (red circles) and '38m/s' (blue triangles), y 'V(m/s)' "
                "10 to 32 by 2 and x 'E(veh/s)' 0.0 to 4.0 by 0.5. The printed legend says 29m/s "
                "where the prose says the limits were changed from 32 to 28 and 36, so the "
                "panel's own key contradicts the sentence. Left-hand chart of the second pair; "
                "caption tail 'Speed Limits(3 lanes, keep-right)'.")
    figure(20, 4, "line", printed(20, CAP_2015), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="right of row 2",
           note="The same velocity-versus-inflow plot under the unrestricted rule, legend "
                "inside the upper right naming 28m/s, 32m/s and 36m/s, y 'V(m/s)' 8 to 30 by 2, "
                "x 0.0 to 4.0 by 0.5. This is the panel whose key matches the prose. Right-hand "
                "chart of the second pair; its caption tail prints as 'Speed Limits(3 lanes, "
                "unrestricted' with the closing parenthesis missing from the text layer, so the "
                "quote stops at the fragment carrying the number.")

    figure(21, 1, "bar", printed(21, CAP_2116), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="left of pair",
           note="Danger index under the three speed limits, keep-right three-lane freeway: "
                "grouped columns, three series keyed inside the upper left as 'Speed limits "
                "28m/s', '32m/s' and '36m/s', y 'Danger Index' 0 to 700 by 100, x 'E(veh/s)'. "
                "No gridlines. Left-hand chart of the pair; the caption breaks mid-word and the "
                "tail on the next line reads 't Speed Limits(3 lanes, keep-right)'.")
    figure(21, 2, "bar", printed(21, CAP_2117), source="text-layer", numbering="Figure N:",
           position="below", legend="inside", layout="right of pair",
           note="The same three-limit danger-index comparison under the unrestricted rule, three "
                "series, legend inside the upper left, but on a y axis that runs 0 to 1000 by "
                "100 instead of 0 to 700 - the wider range is the only difference in the frame. "
                "Right-hand chart of the pair; caption tail 't Speed Limits(3 lanes, "
                "unrestricted)'.")

    # --- section 8.3: the intelligent system ---------------------------------------------
    figure(24, 1, "line", printed(24, CAP_2418), source="text-layer", numbering="Figure N:",
           position="below", legend="inside",
           note="Average velocity under the new intelligent-system rule against inflow rate, "
                "lines keyed by rule with the legend inside the frame, x 'E(veh/s)' and y "
                "'V(m/s)'. The caption is the only one in the paper that names a whole drawing "
                "in words rather than a comparison, and it prints on one line with no tail.")

    # --- appendix: the typed MATLAB listings ----------------------------------------------
    excluded(27, 1, "not-an-exhibit",
             "A typed MATLAB listing band under the heading 'Simulating different inflow "
             "rates function:' - the driver, savefile and speedmax assignments. Code, not an "
             "exhibit: no number, no caption.")
    excluded(29, 1, "not-an-exhibit",
             "A second typed listing band, the lane/xdistance explanation block "
             "(v=road1(lane,xdistance,1)). Code, not an exhibit.")
    excluded(30, 1, "not-an-exhibit",
             "The 'Inflow:' listing band: the poissrnd call and the road re-initialisation. "
             "Code, not an exhibit.")
    excluded(31, 1, "not-an-exhibit",
             "The 'Acceleration:' listing band. Code, not an exhibit.")
    excluded(31, 2, "not-an-exhibit",
             "The 'Deceleration:' listing band. Code, not an exhibit.")
    excluded(31, 3, "not-an-exhibit",
             "The 'Deal with urgent deceleration:' listing band. Code, not an exhibit.")
    excluded(32, 1, "not-an-exhibit",
             "The 'Judge whether to overtake:' listing band. Code, not an exhibit.")
    excluded(32, 2, "not-an-exhibit",
             "The 'Free-driving style:' listing band, carrying the A and B probability matrices "
             "as typed source text. Code, not an exhibit.")
    excluded(33, 1, "not-an-exhibit",
             "The 'Count the traffic flow:' listing band. Code, not an exhibit.")
    excluded(34, 1, "not-an-exhibit",
             "The largest listing band of the appendix, the body of the function "
             "[Xd,density]= Xdensity(...) with its summary comment. Code, not an exhibit: it is "
             "six vector paths of monospaced source text and carries no number and no caption.")

    rules = [
        "Every exhibit in this paper is numbered flatly - 'Figure 1:' to 'Figure 18:' and "
        "'Table 1:' - so the colon form of the enum fits throughout and no record needs "
        "`numbering` set to `none` [caption.numbering].",
        "Seven of the eighteen figures print their captions two to a text line, because each "
        "pair sits side by side and each column is broken mid-word; a row therefore quotes only "
        "the fragment that carries its own figure number and carries the printed tail in its "
        "note [caption.verbatim].",
        "The side-by-side pairs are still separate measured regions with separate frames, so "
        "each panel is a row of its own with a `left of pair` / `right of pair` layout rather "
        "than one `composite-panel` [geometry.panel_layout].",
        "In every pair the left-hand chart takes the earlier figure number and the right-hand "
        "chart the later one, read off the crop x positions: p18 row 1 is Figure 7 left and "
        "Figure 8 right, p20 row 1 is Figure 12 left and Figure 13 right [caption.verbatim].",
        "Figure 2 is a labelled velocity triangle with no axes, no ticks and no plotted data, so "
        "it is recorded `other` with an `other_note` naming the drawing instead of being forced "
        "into `line` [geometry.family].",
        "Table 1 prints its caption above the grid and all eighteen figures print theirs below "
        "the artwork, the split the lane records for every paper [caption.position].",
        "The danger-index and density charts are `bar` on the ink - grouped or stacked vertical "
        "columns - while the velocity charts on the same pages are `line` polylines, so the "
        "family is read per region and not from the caption's wording [geometry.family].",
        "Figure 11 is the paper's only stacked column chart and the only drawing with no y-axis "
        "title at all, so its scale is recorded from the tick set alone [geometry.printed_numbers].",
        "Figure 14's legend names speed limits 29m/s, 32m/s and 38m/s while the prose says the "
        "limit was changed to 28 and 36; the discrepancy is recorded in the note rather than "
        "resolved, because the ink is authoritative [geometry.legend].",
        "Tables 2 and 3 (p10) and Tables 4 and 5 (p23) print caption lines and typed cell rows "
        "but return no measured region from the layout pass, so they are declared gaps and are "
        "not given an invented bbox [table.rows].",
        "The ten appendix listing bands on p27-p34 are typed MATLAB source printed as vector "
        "text: they print no caption line and carry no figure number, so they are excluded "
        "`not-an-exhibit` rather than given an empty caption block [caption.numbering].",
        "Only Figures 2, 4 and 5 are cited by number in the prose ('as is shown in the figure 2', "
        "and the p16 sentence naming figures 4 and 5 together); the other fifteen are introduced "
        "by deictic prose or by their captions alone, so their `mention` blocks are empty "
        "[mention.count].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2014\u7f8e\u8d5b\u7279\u7b49\u5956/A-25142-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twenty-nine measured regions over eighteen pages, all accounted: 18 figure rows, 1 "
            "printed table and 10 exclusions. Eighteen figures carry flat numbers 'Figure 1:' to "
            "'Figure 18:' with no numbered headings in the captions themselves, and the paper's "
            "headings are numbered, so `section_path` quotes the printed headings including the "
            "one that breaks mid-word at the column edge ('6 Sensitivity Evaluation of the Model "
            "under Differ-'). Seven captions print two to a line, one per column, so each row "
            "quotes the fragment carrying its own number and keeps the printed tail in its note; "
            "the two runs on p18 and the two on p20 are read left-to-right against the figure "
            "numbers. Families: 9 `bar` (the four per-lane density panels, the danger-index "
            "panels, the stacked passing-event counts), 8 `line` (the safe-gap curve, the "
            "tempo-spatial "
            "diagram, the velocity sweeps and the intelligent-system plot), 1 `other` (the "
            "velocity triangle). The paper prints four further tables - acceleration and "
            "deceleration probabilities on p10 and the same two under the intelligent system on "
            "p23 - whose caption lines and typed cell rows are in the text layer but whose pages "
            "return no measured region; they are declared gaps. The ten appendix page bands are "
            "typed MATLAB source and are excluded. Only Figures 2, 4 and 5 are named in prose. "
            "Figure 14's legend names 29m/s, 32m/s and 38m/s against the prose's 28 and 36, and "
            "Figure 15's caption tail loses its closing parenthesis in the text layer; both are "
            "recorded as printed."
        ),
    }
    out = PROXY / "pc51-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
