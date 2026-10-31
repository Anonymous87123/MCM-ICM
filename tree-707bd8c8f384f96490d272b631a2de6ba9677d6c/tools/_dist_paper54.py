"""Hand pass for P-A-2014-29911-ac64b43b (a cellular-automaton plus continuum study of the
keep-right-except-to-pass rule on a double-lane freeway, with Monte Carlo simulation, optimal
maximum velocity, three alternative rules and an intelligent-system "median" rule), 40 PDF pages.

Fifty-three measured regions over twenty-eight pages: 24 figure rows, 5 printed tables, and 24
exclusions.

    p5-r1   flowchart-or-schematic Figure 1: the keep-right-except-to-pass strip
    p6-r1   flowchart-or-schematic Figure 2: the particle-hopping strip
    p6-r2   table-grid             Table 1: notation (continues on p7)
    p7-r2   table-grid             Table 2: the acceleration/deceleration equations
    p8-r1   table-grid             Table 3: the basic rules
    p8-r2   table-grid             Table 4: lane-changing directions
    p8-r3   table-grid             Table 5: Monte Carlo procedures (continues on p9)
    p11-r1  line                   Figure 3: flow vs density
    p12-r1  line                   Figure 4: safety index vs density
    p13-r1  line                   Figure 5: energy consumption vs density
    p14-r1  line                   Figure 6: optimal maximum velocity, light traffic
    p15-r1  line                   Figure 7: optimal maximum velocity, heavy traffic
    p15-r2  line                   Figure 8: optimal maximum velocity, combined
    p16-r2  scatter                Figure 9: low-density visualisation, left panel
    p16-r1  scatter                Figure 9: right panel
    p17-r1  scatter                Figure 10: high-density visualisation, left panel
    p17-r2  scatter                Figure 10: right panel
    p19-r1  line                   Figure 11: flow vs average density
    p21-r1  surface-or-3D          Figure 12: low density, jam first on the fast lane
    p21-r2  surface-or-3D          Figure 13: low density, jam first on the slow lane
    p21-r3  surface-or-3D          Figure 14: normal or higher density
    p24-r1  line                   Figure 15: flow under three traffic rules
    p25-r1  line                   Figure 16: safety index under three rules
    p25-r2  line                   Figure 17: energy consumption under three rules
    p27-r2  flowchart-or-schematic Figure 18: the "Median" rule flowchart
    p28-r1  line                   Figure 19: flow, equipped vs not equipped
    p28-r2  line                   Figure 20: safety index, equipped vs not equipped
    p28-r3  line                   Figure 21: energy consumption, equipped vs not equipped
    p29-r1  flowchart-or-schematic Figure 22: online-algorithm illustration

Two tables break across a page and each is counted once, on its first region, with the
continuation region excluded `split-across-pages`; Figure 18's six label blocks are excluded
`fragment-of-other` because the whole flowchart is the one vector region on p27; and the twelve
appendix C++ listing bands on p32 to p40 are excluded `not-an-exhibit`.

Usage: python -I tools/_dist_paper54.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2014-29911-ac64b43b"
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

INTRO = "1 Introduction"
RIGHT = "3 Modeling for Right-Most Rule"
DISC = "3.1 Discrete Modeling for Right-Most Rule"
ESTAB = "3.1.1 Model Establishment"
SOLVE = "3.1.3 Model Solution and Analysis"
CONT = "3.2 Continuum Modeling for Right-Most Rule"
CSOLVE = "3.2.2 Model Solution and Analysis"
ALT = "4 Modeling for Alternative Freeway Traffic Rules"
CMP = "4.3 Comparison of Different Traffic Rules"
INTEL = "5 Modeling for Intelligent-System Control"
IMPROVE = "5.2 Possible Further Improvements"

PATH: dict[tuple[int, int], tuple[list[str], str]] = {
    (5, 1): ([INTRO], "introduction"),
    (6, 1): ([RIGHT, DISC, ESTAB], "model"),
    (6, 2): ([RIGHT, DISC, ESTAB], "model"),
    (7, 2): ([RIGHT, DISC, ESTAB], "model"),
    (8, 1): ([RIGHT, DISC, ESTAB], "model"),
    (8, 2): ([RIGHT, DISC, ESTAB], "model"),
    (8, 3): ([RIGHT, DISC, ESTAB], "model"),
}
for _key in [(11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (15, 2), (16, 1), (16, 2),
             (17, 1), (17, 2)]:
    PATH[_key] = ([RIGHT, DISC, SOLVE], "model")
for _key in [(19, 1), (21, 1), (21, 2), (21, 3)]:
    PATH[_key] = ([RIGHT, CONT, CSOLVE], "model")
for _key in [(24, 1), (25, 1), (25, 2)]:
    PATH[_key] = ([ALT, CMP], "other")
for _key in [(27, 2), (28, 1), (28, 2), (28, 3)]:
    PATH[_key] = ([INTEL], "model")
PATH[(29, 1)] = ([INTEL, IMPROVE], "other")

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

VENTIONS = {5: 1, 6: 2, 7: 1, 8: 3, 11: 1, 12: 1, 13: 1, 14: 1, 15: 2, 16: 2, 17: 2,
            19: 1, 21: 3, 24: 1, 25: 2, 27: 1, 28: 3, 29: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def mention(first_page: int, lead_pages: int, style: list[str], quote: str,
            pattern: str, count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": lead_pages, "style": list(style),
            "count": count, "lead_sentence": quote, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": 1, "gap_sentences": None}


def deictic(page: int, lead_pages: int, quote: str) -> dict:
    """A pointer that prints no exhibit number, counted as zero named citations."""
    return {"first_page": page, "lead_pages": lead_pages, "style": [], "count": 0,
            "lead_sentence": quote, "trail_sentence": "", "lead_pattern": "direct",
            "read_sentences": 1, "gap_sentences": None}


CAP = {
    1: 'Figure 1. Illustration of "Keep-Right-Except-To-Pass" Rule',
    2: 'Figure 2. Representation of the "Particle-Hopping" Model',
    3: "Figure 3. Relationship of Traffic Flow \U0001d444 and Vehicle Density \U0001d45b",
    4: "Figure 4. Relationship of Safety Index \U0001d6fc\U0001d460\U0001d44e\U0001d453"
       "\U0001d452 and Vehicle Density \U0001d45b (lower is safer)",
    5: "Figure 5. Relationship of Energy Consumption \U0001d4380 and Vehicle Density "
       "\U0001d45b (lower is better)",
    6: "Figure 6. Optimal Maximum Velocity (Light Traffic)",
    7: "Figure 7. Optimal Maximum Velocity (Heavy Traffic)",
    8: "Figure 8. Optimal Maximum Velocity (combined)",
    9: "Figure 9. Visualization at Low Density",
    10: "Figure 10. Visualization at High Density",
    11: "Figure 11. The Relationship of Traffic Flow \U0001d444 and Average Density "
        "\U0001d70c\u0305",
    12: "Figure 12. Low Density(Jam First Appeared on Fast Lane)",
    13: "Figure 13. Low Density(Jam First Appeared on Slow Lane)",
    14: "Figure 14. Normal or Higher Density",
    15: "Figure 15. Traffic Flow under Different Traffic Rules",
    16: "Figure 16. Safety Index under Different Traffic Rules (lower is safer)",
    17: "Figure 17. Average Energy Consumption under Different Traffic Rules (lower is better)",
    18: 'Figure 18. "Median" Illustration',
    19: "Figure 19. Relationship of Traffic Flow and Vehicle Density",
    20: "Figure 20. Relationship of Safety Index and Vehicle Density (lower is safer)",
    21: "Figure 21. Relationship of Average Energy Consumption and Vehicle Density "
        "(lower is better)",
    22: "Figure 22. Illustration of Online Algorithm",
}

T_CAP = {
    1: 'Table 1. Definition of Notation in "Particle-Hopping" Model',
    2: "Table 2. The Rule of Acceleration and Deceleration",
    3: "Table 3. The Basic Rules",
    4: "Table 4. The Rule of Lane Changing corresponding to the \u201crightmost\u201d rule",
    5: "Table 5. Monte Carlo Procedures",
}

MENTION = {
    1: mention(4, 1, ["Figure 1"], "See in Figure 1.", "direct"),
    2: mention(6, 0, ["Figure 2"], "Figure 2 is a vivid illustration of our model.",
               "figure-n-shows"),
    3: mention(11, 0, ["Figure 3"],
               "Apparently, the pattern in Figure 3 accords with realistic situation "
               "qualitatively.", "direct"),
    4: mention(11, 1, ["Figure 4"], "The result is shown in Figure 4.", "as-shown-in"),
    5: mention(13, 0, ["Figure 5"],
               "We again plot the average energy consumption against vehicle density in "
               "Figure 5.", "direct"),
    6: mention(14, 0, ["Figure 6", "Figure 7"], "in Figure 6 and Figure 7", "direct"),
    7: mention(14, 1, ["Figure 7"], "in Figure 6 and Figure 7", "direct"),
    8: mention(15, 0, ["Figure 8"], "As shown in Figure 8, the global maximum value of",
               "as-shown-in"),
    9: mention(16, 0, ["Figure 9", "Figure 10"], "respectively in Figure 9 and Figure 10",
               "direct"),
    10: mention(16, 1, ["Figure 10"], "respectively in Figure 9 and Figure 10", "direct"),
    11: mention(19, 0, ["Figure 11"], "we can plot the relationship as shown in Figure 11.",
                "as-shown-in"),
    12: mention(20, 1, ["Figure 12"],
                "According to Figure 12, any perturbations on the fast lane or the slow lane "
                "will quickly dissipate.", "direct"),
    13: mention(20, 1, ["Figure 13"],
                "as shown in Figure 13, a cluster in slow lane may quickly dissipate",
                "as-shown-in"),
    14: mention(21, 0, ["Figure 14"], "See in Figure 14.", "direct"),
    15: mention(24, 0, ["Figure 15"],
                "We plot traffic flow \U0001d444 against vehicle density \U0001d45b in "
                "Figure 15.", "direct"),
    16: mention(24, 1, ["Figure 16"],
                "We plot safety index \U0001d6fc\U0001d460\U0001d44e\U0001d453\U0001d452 "
                "against vehicle density \U0001d45b in Figure 16.", "direct"),
    17: mention(25, 0, ["Figure 17"],
                "We plot average energy consumption \U0001d4380 against vehicle density "
                "\U0001d45b in Figure 17.", "direct"),
    18: mention(27, 0, ["Figure 18"], "The rule is as stated in Figure 18.", "direct"),
    19: mention(27, 1, ["Figure 19"], "See in Figure 19-21.", "direct"),
    20: mention(27, 1, ["Figure 20"], "See in Figure 19-21.", "direct"),
    21: mention(27, 1, ["Figure 21"], "See in Figure 19-21.", "direct"),
    22: mention(29, 0, ["Figure 22"], "as shown in Figure 22", "as-shown-in"),
    101: mention(6, 0, ["Table 1"],
                 "The quantities involved in the simulation are shown in Table 1.",
                 "as-shown-in"),
    102: deictic(7, 0, "The rule of acceleration and deceleration is as follows:"),
    103: deictic(7, 1,
                "The permission rule for changing lane is much more complex and comprised of "
                "several basic rules."),
    104: deictic(7, 1,
                "The permission rule for changing lane is much more complex and comprised of "
                "several basic rules."),
    105: mention(8, 0, ["Table 5"],
                 "In Table 5, we present the specific steps of our Monte Carlo simulation:",
                 "direct"),
}


def printed(page: int, text: str) -> str:
    """Verify a caption string really prints on the page, once Unicode-normalised."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text))
    return text


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH[(page, reg)]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": PAGE_SEEN[page] + sum(VENTIONS[p] for p in VENTIONS if p < page),
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


def figure(page: int, reg: int, family: str, key: int, *, cap_page: int | None = None,
           text: str | None = None,
           panels: int = 1, layout: str = "1", legend: str = "none",
           three_d: str = "no", numbers: bool = True, labels: bool = False,
           note: str = "", other_note: str = "") -> None:
    ORDER.append((page, reg))
    cap = printed(page if cap_page is None else cap_page, CAP[key]) if text is None else text
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap,
        "caption_source": "text-layer" if cap else "none",
        "note": note,
        "place": place(page, reg),
        "mention": dict(MENTION[key]),
        "caption": caption_block(cap, "text-layer" if cap else "none", "below",
                                 "Figure N." if cap else "none"),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, key: int, *, cap_page: int | None = None, rows: int,
          cols: int, header_rows: int = 1,
          rules: str = "booktabs", zebra: bool = False, numeric_cols: int = 0,
          text_cols: int = 0, merged: bool = False, continued: bool = False,
          note: str = "") -> None:
    ORDER.append((page, reg))
    text = printed(page if cap_page is None else cap_page, T_CAP[key])
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": dict(MENTION[100 + key]),
        "caption": caption_block(text, "text-layer", "below", "Table N."),
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
    # --- section 1: the rule itself --------------------------------------------------------
    figure(5, 1, "flowchart-or-schematic", 1, numbers=False,
           note="The keep-right-except-to-pass rule drawn as a two-lane cell strip, two rows of "
                "ten cells with the row labels 'Left lane' and 'Right lane' at the left, some "
                "cells filled light blue and one right-pointing arrow in the left lane. No "
                "numbers, no scale, no legend; the row labels are the only annotation "
                "[geometry.printed_numbers].")

    # --- section 3.1.1: the discrete model -------------------------------------------------
    figure(6, 1, "flowchart-or-schematic", 2, numbers=False,
           note="The same two-lane cell strip with eight blue filled circles as cars above it, a "
                "curved lane-change arrow and a straight forward arrow: the paper's "
                "particle-hopping picture. No numbers and no legend; the left/right lane row "
                "labels carry the only text.")
    table(6, 2, 1, cap_page=7, rows=16, cols=2, rules="vertical-rules", text_cols=2,
          continued=True,
          note="The notation list: header 'Notation | Definition' over fifteen symbol rows "
               "(X(k), V(k), the four front/behind gaps, Vmax(k), Q, alpha_safe, L, T, Pd, Pc, n, "
               "N with 'N = 2nL'). Thick top rule, thin rule under the header, a thin rule "
               "between every body row, one full-height vertical rule between the two columns "
               "and a thick bottom rule, with no outer side frame, so `rule_style` is "
               "`vertical-rules`. Eleven rows print on p6 and the last four (Pd, Pc, n, N) on "
               "p7, so the row carries `continued` true and the p7 continuation region is "
               "excluded `split-across-pages`. The caption prints on p7 after the tail, followed "
               "by the parenthetical '(Terms marked with an asterisk (*) require pre-evaluation "
               "before the simulation begins)', which is kept here rather than in the quoted "
               "caption [table.continued].")
    table(7, 2, 2, rows=2, cols=1, header_rows=1, rules="booktabs", text_cols=1,
          note="The acceleration and deceleration rule as a framed pair of numbered equations, "
               "(i) 'If V(n) < Vmax, then V(n) = V(n) + 1' and (ii) 'If ran f < Pd, then "
               "V(n) = V(n) - 1', inside double top and double bottom rules with no internal "
               "rule, no vertical rule and no side frame. The table prints no header row at all "
               "- the two rows are the numbered equations (i) and (ii) - so `header_rows` takes "
               "the schema floor of 1 with the first equation standing in that slot, and "
               "`rule_style` is `booktabs`; the caption continues with the random-number gloss, "
               "which is kept in this note rather than in the quoted caption [table.header_rows].")

    # --- section 3.1.1: the lane-changing and procedure tables ------------------------------
    table(8, 1, 3, rows=4, cols=3, rules="vertical-rules", merged=True, text_cols=3,
          note="The three-column rule matrix: header 'Rule safety | Rule stay except blocked "
               "(Rule #0) | Rule change when possible (Rule #1)' over three body rows of "
               "inequalities in the front and behind gaps, Vmax and Pc. Two full-height "
               "internal vertical rules, a rule under the header, rules between the body rows "
               "and a thick bottom rule, no outer side frame. The third column's last two rows "
               "are one merged blank cell, so `merged_cells` is true and a census that assumes "
               "a fully populated 3x3 grid would overcount that column [table.merged_cells].")
    table(8, 2, 4, rows=3, cols=2, rules="vertical-rules", text_cols=2,
          note="The direction summary: header 'right -> left | left -> right' in bold italic "
               "over two body rows naming Rule safety, Rule #0 and Rule #1 in each direction. "
               "One full-height vertical rule between the columns, a rule under the header, one "
               "inter-row rule and a double bottom rule, no outer side frame.")
    table(8, 3, 5, cap_page=9, rows=20, cols=2, header_rows=1, rules="booktabs", text_cols=2,
          continued=True,
          note="The Monte Carlo procedure table, begun at the foot of p8 with its 'Input' row "
               "(lane length L, duration T) and continued over the whole of p9 with the "
               "'Output' row and Steps 1 to 18, whose caption prints on p9 after Step 18. Two "
               "columns - the step label "
               "and the step text - with no header row, so `header_rows` takes the schema floor "
               "of 1 with the Input row standing in that slot, ruling at the top and the foot "
               "only and no vertical rule. The paper prints no Step 12, skipping from Step 11 to "
               "Step 13, "
               "which is recorded here rather than repaired. The five p9 continuation regions "
               "are excluded `split-across-pages` and the table is counted once on this region "
               "[table.continued].")

    # --- section 3.1.3: the discrete results ------------------------------------------------
    figure(11, 1, "line", 3, legend="outside-right",
           note="One peaked curve of traffic flow against density, single series with round "
                "markers on a solid orange line, peak near n = 0.2 and a tail to n = 0.9. Both "
                "axes are numbered (x 0 to 1 by 0.2, y 0 to 1.4 by 0.2), horizontal gridlines "
                "only, and the legend sits OUTSIDE the frame at the right with a single entry "
                "left in Chinese, '\u7cfb\u52172', in an otherwise English figure. An in-figure "
                "title 'Traffic Flow Q against Vehicle density n' sits above the artwork "
                "[geometry.legend].")
    figure(12, 1, "line", 4, legend="outside-right",
           note="The safety index against density: one peaked curve with round markers, peak "
                "about 0.30 near n = 0.18, x 0 to 1 by 0.2 and y 0 to 0.35 by 0.05, no "
                "gridlines, the same single Chinese legend entry outside at the right.")
    figure(13, 1, "line", 5, legend="outside-right",
           note="Energy consumption against density: one monotone-rising curve that flattens "
                "after n = 0.4 with a small dip near n = 0.7, y 0 to 1000 by 100, same outside "
                "legend and same single series.")
    figure(14, 1, "line", 6, legend="inside",
           note="Phi against maximum velocity for light traffic: one rising series with round "
                "markers at integer Vmax from 1 to 6, saturating after Vmax = 3 at about 0.69, "
                "x 0 to 7 by 1 and y 0 to 0.8 by 0.1, faint gridlines both ways, legend INSIDE "
                "at the centre right. The artwork's own title says 'phi against maximum velocity "
                "V_max (light traffic)' - the caption's word 'optimal' is not drawn anywhere on "
                "the figure [caption.verbatim].")
    figure(15, 1, "line", 7, legend="inside",
           note="The heavy-traffic twin: flat near 0.55 to Vmax = 2, a steep rise to about 0.90 "
                "at Vmax = 3 and a slow decline after, y 0 to 1 by 0.1. The drawn curve carries "
                "two extra vertices near Vmax 2.5 and 3.5 that have no marker, so the path is "
                "not simply the marked points joined.")
    figure(15, 2, "line", 8, legend="inside",
           note="The combined case: phi rising to a plateau of about 0.72 from Vmax = 3, y 0 to "
                "0.8 by 0.1. The prose reads the optimum off this panel as Vmax = 5, which is "
                "where the plateau is first flat rather than where a maximum sits, and the "
                "combined peak (0.72) sits between the light (0.69) and heavy (0.90) panels "
                "rather than bracketing them.")
    figure(16, 2, "scatter", 9, legend="none", numbers=False,
           note="The left panel of the low-density visualisation: a sparse cloud of black dots "
                "forming thin diagonal streaks on white, no frame, no axes, no ticks and no "
                "labels of any kind. The text layer says the left subfigure is the left lane and "
                "the right subfigure the right lane, but the artwork carries no lane label, so "
                "the pairing is fixed by the measured x positions - this region starts at "
                "x = 165 against the other's x = 496 [geometry.panel_count].")
    figure(16, 1, "scatter", 9, text="", note="The right panel of Figure 9: the same dot-streak "
           "construction, visibly denser and more banded than the left panel. No axes, no "
           "legend, no printed numbers. Caption and citation are carried on the left panel only "
           "[caption.verbatim].")
    figure(17, 1, "scatter", 10, legend="none", numbers=False,
           note="The left panel of the high-density visualisation: a near-saturated black dot "
                "field with dark streaks and thin white gaps filling the frame, no axes and no "
                "labels. Left panel fixed by x = 146 against the other's x = 496 "
                "[geometry.panel_count].")
    figure(17, 2, "scatter", 10, text="", note="The right panel of Figure 10: the same saturated "
           "dot texture with a different streak orientation. Caption and citation sit on the "
           "left panel [caption.verbatim].")

    # --- section 3.2.2: the continuum results ----------------------------------------------
    figure(19, 1, "line", 11, legend="inside", labels=True,
           note="Three flow-density curves over average density, with critical points annotated "
                "in place - (rho_d1, q_d1), (rho_u1, q_u1) and the matching pair for the second "
                "lane - plus arrows on the x axis marking rho_c1, rho_c2, rho_c3 and rho_c, so "
                "`data_labels` is true. The fast lane is solid, the slow lane dashed and the "
                "average flow dash-dotted, keyed in a three-entry legend INSIDE the frame at the "
                "upper right. The x axis is 'Average density rho-bar/(veh/m)' 0 to 0.14 by 0.02 "
                "and the y axis 'Flow/(veh/s)' 0 to 0.6 by 0.1.")
    figure(21, 1, "surface-or-3D", 12, panels=2, layout="2x1", three_d="surface-mesh",
           legend="none",
           note="Two stacked 3-D mesh surfaces of density against distance and time, panel (a) "
                "above panel (b), with a single diagonal jam ridge in (a). Axes: 'Density"
                "/(veh/m)' 0 to 0.10 up the vertical, 'x/km' 0 to 30 receding and 't/min' 0 to "
                "100 to the right. The prose says (a) is the fast lane and (b) the slow lane; "
                "the panels carry only the letters [geometry.three_d].")
    figure(21, 2, "surface-or-3D", 13, panels=2, layout="2x1", three_d="surface-mesh",
           note="The same pair of 3-D meshes for the mirror case: (a) carries a mild local "
                "disturbance at low x and (b) stays nearly flat, the same three axes and the "
                "same absence of a legend.")
    figure(21, 3, "surface-or-3D", 14, cap_page=22, panels=2, layout="2x1",
           three_d="surface-mesh",
           note="The third of the continuum triple: both panels show strong periodic "
                "stop-and-go waves. This is the exhibit whose caption does not print with it - "
                "'Figure 14. Normal or Higher Density' opens p22 - so the art sits on p21 and "
                "the caption a page later [caption.position].")

    # --- section 4.3: the three rules compared ---------------------------------------------
    figure(24, 1, "line", 15, legend="inside",
           note="Traffic flow against density for the three rules: three marker-and-line series "
                "in blue, orange and grey, keyed inside at the right middle as 'free driving & "
                "free overtaking', 'keep-right-except-to-pass' and 'slow-cars-to-right', "
                "converging near density 0.25. x 0 to 0.35 by 0.05, y 0 to 1.4 by 0.2, in-figure "
                "title above the artwork.")
    figure(25, 1, "line", 16, legend="inside",
           note="The same three rules for the safety index: three colour-coded curves peaking "
                "around density 0.2, x 0 to 0.35, y 0 to 0.35 by 0.05, legend inside right.")
    figure(25, 2, "line", 17, legend="inside",
           note="The same three rules for energy consumption: three well-separated rising curves "
                "at high density, x 0 to 0.35, y 0 to 1800 by 200, legend inside right. This "
                "panel's y axis tops out at 1800 where the later Figure 21 uses 2000, a "
                "typesetting difference between the two comparison sets rather than a "
                "contradiction in the data.")

    # --- section 5: the intelligent-system rule ---------------------------------------------
    figure(27, 2, "flowchart-or-schematic", 18, numbers=False,
           note="The 'Median' rule as a decision flowchart: a start box 'Determine the speed of "
                "the kth car', a diamond 'V(k)=Vmedian?', two further diamonds ('Generate a "
                "random number in [0, 1]' and 'V(k)>Vmedian'), two action boxes ('Stay on left "
                "lane except blocked...' and 'Stay on right lane except blocked...') and 'End', "
                "with the branch conditions <0.5 and >0.5 printed on the connectors. The layout "
                "pass returns six further regions on p27 that are the individual label blocks of "
                "this same drawing, so the flowchart is one row here and those six are excluded "
                "`fragment-of-other` [geometry.panel_count].")
    figure(28, 1, "line", 19, legend="inside",
           note="Traffic flow against density with the median optimisation switched on and off: "
                "two nearly overlapping curves, 'Equipped' in blue and 'Not Equipped' in dark "
                "red, x 0 to 0.4 by 0.1 and y 0 to 1.5 by 0.5, legend inside right. The "
                "in-figure title wraps over two lines where the p24 and p25 titles do not.")
    figure(28, 2, "line", 20, legend="inside",
           note="The safety-index pair: 'Not Equipped' lying above 'Equipped' and the two "
                "converging near density 0.1, x 0 to 0.4 and y 0 to 0.35 by 0.05, legend inside "
                "right.")
    figure(28, 3, "line", 21, legend="inside",
           note="The energy-consumption pair, effectively superimposed and rising to about "
                "1600, y 0 to 2000 by 500 with the axis label wrapped over three lines - the "
                "only panel in the paper whose ordinate label needs three.")

    # --- section 5.2: the online-algorithm illustration -------------------------------------
    figure(29, 1, "flowchart-or-schematic", 22, numbers=False,
           note="A horizontal strip of equal cells with a few filled light blue, an ellipsis at "
                "each end and a single arrow pointing down into one cell - the gapless car flow "
                "the prose points at. The measured region catches the occupancy band only: the "
                "crop is cut off at its top edge, so the illustration extends beyond what the "
                "layout pass measured, and no cell carries a label or a number "
                "[geometry.printed_numbers].")

    # --- exclusions -------------------------------------------------------------------------
    excluded(7, 1, "split-across-pages",
             "The last four rows of Table 1 (Pd, Pc, n, N) continuing from p6 with no header "
             "repeat and closing with the table's bottom rule. Counted as part of Table 1, not "
             "as a second table.")
    for _reg in (1, 2, 3, 4, 5):
        excluded(9, _reg, "split-across-pages",
                 "One band of Table 5 on p9: the remainder of the Input cell, the Output row and "
                 "Steps 1 to 18 of the Monte Carlo procedure. Counted as part of Table 5, which "
                 "is recorded once on its p8 region.")
    for _reg in (1, 3, 4, 5, 6, 7):
        excluded(27, _reg, "fragment-of-other",
                 "A single label block of the Figure 18 flowchart - the start terminal, the "
                 "'V(k)=Vmedian?' diamond, the random-draw diamond, the 'V(k)>Vmedian' "
                 "comparison, or one of the two 'Apply rule' boxes. The complete drawing is the "
                 "one vector region on p27 that Figure 18 is recorded from.")
    for _page, _count in ((32, 1), (33, 3), (34, 1), (35, 1), (36, 2), (37, 1), (38, 1),
                          (39, 1), (40, 1)):
        for _reg in range(1, _count + 1):
            excluded(_page, _reg, "not-an-exhibit",
                     "A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, "
                     "CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure "
                     "or table number and no artwork.")

    rules = [
        "The numbering is flat with a stop - 'Figure 1.' to 'Figure 22.' and 'Table 1.' to "
        "'Table 5.' - so the stop forms of the enum fit every record and no exhibit is numbered "
        "without one [caption.numbering].",
        "Every caption in this paper survives in the text layer, including the captions of the "
        "raster figures, so no caption is typed from the crop [caption.verbatim].",
        "Every figure caption prints BELOW its artwork and every table caption below its grid as "
        "well - Tables 1 to 5 all close with their caption - against the lane's habit of "
        "captioning tables above, so the positions are recorded as printed "
        "[caption.position].",
        "Two tables break across a page boundary and each is counted once: Table 1 begins on p6 "
        "with eleven rows and finishes on p7 with four more before its caption, and Table 5 "
        "begins on p8 with its Input row and runs through p9 to Step 18. The continuation "
        "regions are excluded `split-across-pages` and the recorded rows carry `continued` true "
        "[table.continued].",
        "Figure 18 is one drawing whose eight label blocks were measured as seven regions: the "
        "whole flowchart is the vector region on p27 and the six small raster blocks - the start "
        "terminal, the three diamonds and the two action boxes - are excluded "
        "`fragment-of-other` rather than counted as exhibits [geometry.panel_count].",
        "Figures 9 and 10 are each two panels rather than one plate: the low- and high-density "
        "visualisations are measured as separate left and right regions, so each gets a row per "
        "panel, the left panel carrying the caption and the citation and the right panel neither "
        "[caption.verbatim].",
        "Figures 12, 13 and 14 are 3-D surface meshes of density over distance and time, two "
        "panels each with (a) the fast lane and (b) the slow lane, so they are recorded "
        "`surface-or-3D` with `three_d` `surface-mesh` instead of being forced into `line` "
        "[geometry.three_d].",
        "Figures 3, 4 and 5 carry a single-entry legend left in Chinese - '\u7cfb\u52172' - "
        "outside the frame at the right, in an otherwise English figure, and it is recorded "
        "where it is rather than translated [geometry.legend].",
        "Figures 15 to 17 key three traffic rules across three colours inside the frame, while "
        "Figures 19 to 21 key only 'Equipped' against 'Not Equipped' in two - the same "
        "flow/safety/energy triple plotted twice, once by rule and once by optimisation "
        "[geometry.family].",
        "Figure 11 is the only plot that writes values onto its own data - the critical points "
        "(rho_d, q_d) and (rho_u, q_u) of both lanes plus rho_c1, rho_c2, rho_c3 and rho_c "
        "arrows on the x axis - so `data_labels` is true there and false on the rest "
        "[geometry.data_labels].",
        "The tables were numbered against the prose rather than against the layout pass: three "
        "of the five - Table 2 (the framed acceleration rule), Table 3 (the rule matrix) and "
        "Table 4 (the direction summary) - are never cited by number at all, so Table 2 carries "
        "the deictic clause that introduces it and Tables 3 and 4 the sentence on p7 about the "
        "lane-changing rule, both with an empty style list and count 0 [mention.first_page].",
        "Figure 14 is the one exhibit whose caption and artwork part company across a page - the "
        "meshes close p21 and 'Figure 14. Normal or Higher Density' opens p22 [caption.position].",
        "The appendix on p32 to p40 is twelve bands of typed C++ source (gen.h, SaveBMP.h, "
        "lane.h, CA.cpp and the driver), all excluded `not-an-exhibit` because none of them is "
        "captioned, numbered or drawn [caption.numbering].",
    ]

    payload = {
        "paper": PID,
        "source": ("F:/MCM/MCM-ICM-master/2014\u7f8e\u8d5b\u7279\u7b49\u5956/"
                   "A-29911-Outstanding.pdf"),
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Fifty-three measured regions over twenty-eight of forty pages, resolving into 24 "
            "figure rows, 5 printed tables and 24 exclusions, with nothing unresolved and no "
            "declared gaps. Families: 13 `line` (the three rule-versus-density curves of Figures "
            "3 to 5, the three optimal-velocity curves of Figures 6 to 8, Figure 11's three "
            "flow curves and the two comparison sets of Figures 15 to 17 and 19 to 21), 5 "
            "`table-grid`, 4 `scatter` (the four panel rows of the density visualisations), 4 "
            "`flowchart-or-schematic` (the two cell strips, the Median flowchart and the online "
            "algorithm strip) and 3 `surface-or-3D` (the continuum model's 3-D density meshes, "
            "`three_d` `surface-mesh`, two panels each). Twenty-two printed figure numbers over "
            "24 rows, because Figures 9 and 10 are each measured as two panels. The numbering is "
            "flat with a stop throughout, all captions are in the text layer, and all twenty-nine "
            "exhibits caption below their art - tables included, against the lane's habit. Two "
            "tables break across pages and are counted once with `continued` true (Table 1 from "
            "p6 to p7, Table 5 from p8 to p9, the latter printing no Step 12); Figure 18 is one "
            "flowchart measured as seven regions, so six are `fragment-of-other`; and the "
            "appendix on p32 to p40 is twelve bands of typed C++ excluded `not-an-exhibit`. "
            "Faults worth carrying downstream: Figures 3, 4 and 5 keep a Chinese single-entry "
            "legend ('\u7cfb\u52172') in English artwork, Figures 6 to 8 are captioned 'Optimal "
            "Maximum Velocity' while the artwork only plots phi against Vmax with no optimum "
            "marked, Figure 14's caption prints on the page after its meshes, and Table 3 "
            "carries a merged blank cell in its third column."
        ),
    }
    out = PROXY / "pc54-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
