"""Hand pass for P-A-2014-29282-f92c8e1b (the keep-right-except-to-pass traffic-rule paper: a
cellular-automaton freeway simulation, three proposed rules, an AHP evaluation and an
intelligent-driver comparison), 30 PDF pages.

Thirty-three measured regions over nineteen pages: 22 figure rows, 9 printed tables, and 2
exclusions on the summary sheet.

    p1-r1  excluded  summary-sheet control-number form grid
    p1-r2  excluded  summary-sheet title band
    p4-r1  flowchart-or-schematic Figure 1: the logic framework
    p7-r1  flowchart-or-schematic Figure 2: following vs overtaking(i¡j)
    p9-r1  line                  Figure 3: state proportions over transitions
    p11-r1 flowchart-or-schematic Figure 4: road condition in heavy traffic
    p12-r1 flowchart-or-schematic Figure 5: the simulated freeway
    p14-r1 flowchart-or-schematic Figure 6: the "Go" process
    p14-r2 flowchart-or-schematic Figure 7: the "Return" process
    p15-r1 flowchart-or-schematic Figure 8: general simulation flowchart
    p16-r1 flowchart-or-schematic Figure 9: sub flowchart of the "Go" process
    p17-r1 table-grid            Table 1: simulation results
    p17-r2 scatter               Figure 10: danger index vs lambda
    p17-r3 scatter               Figure 11: average traffic speed vs lambda
    p17-r4 scatter               Figure 12: traffic flow vs lambda
    p17-r5 scatter               Figure 13: OSL effect vs lambda
    p18-r1 scatter               Figure 14: USL effect vs lambda
    p19-r1 flowchart-or-schematic Figure 15: light-traffic strip
    p19-r2 flowchart-or-schematic Figure 16: heavy-traffic strip
    p19-r3 table-grid            Table 2: sensitivity in p1
    p20-r1 table-grid            Table 3: sensitivity in p2
    p20-r2 table-grid            Table 4: sensitivity in d
    p21-r1 table-grid            Table 5: evaluation of the new rules
    p23-r1 table-grid            Table 6: normalized evaluation indexes
    p23-r2 line                  Figure 17: radar view of the indexes
    p24-r1 table-grid            Table 7: Saaty scale
    p24-r2 table-grid            Table 8: AHP weights
    p25-r1 table-grid            Table 9: comprehensive index
    p26-r1 flowchart-or-schematic Figure 18: RHT and LHT systems
    p28-r1 line                  Figure 19: comparison in traffic flow
    p28-r2 line                  Figure 20: comparison in ATS
    p28-r3 line                  Figure 21: comparison in USL effect
    p28-r4 line                  Figure 22: comparison in OSL effect

Every caption in this paper survives in the text layer, so no caption is typed from the crop.
Families are read off the crops: `scatter` for the five blue-dot-plus-red-fit panels, `line`
for the three-series state plot and the four two-curve comparisons, `line` also for the radar
(record `P-A-2022-2209466-5952dd05` page 9 sets that precedent), and
`flowchart-or-schematic` for the eleven drawn strips and box-and-arrow diagrams.

Usage: python -I tools/_dist_paper53.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2014-29282-f92c8e1b"
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
RULE3 = "3 The Keep-Right-Except-To-Pass Rule"
LIGHT = "3.2 Performance In Light Traffic"
MODEL = "4 A Simulation Model: Cellular Automation"
ALGO = "4.3 Algorithm Descriptions"
CALC = "4.4 Calculation And Results"
NEW = "5 A New Traffic Rule"
CMP = "5.3 Comparison"
FURTHER = "6 Further Topics"

# Route keyed by region, because p19 carries two sections: the light-traffic strip conclusion
# at the top of the page and the sensitivity tables at the bottom.
PATH: dict[tuple[int, int], tuple[list[str], str]] = {
    (4, 1): ([INTRO], "introduction"),
    (7, 1): ([RULE3, LIGHT, "3.2.2 A State Transition Approach"], "result"),
    (9, 1): ([RULE3, LIGHT, "3.2.3 A Numerical Test And Conclusion"], "result"),
    (11, 1): ([RULE3, "3.3 Performance In Heavy Traffic"], "result"),
    (12, 1): ([MODEL, "4.2 Notations"], "model"),
    (14, 1): ([MODEL, ALGO], "model"),
    (14, 2): ([MODEL, ALGO], "model"),
    (15, 1): ([MODEL, ALGO], "model"),
    (16, 1): ([MODEL, ALGO], "model"),
    (17, 1): ([MODEL, CALC], "result"),
    (17, 2): ([MODEL, CALC], "result"),
    (17, 3): ([MODEL, CALC], "result"),
    (17, 4): ([MODEL, CALC], "result"),
    (17, 5): ([MODEL, CALC], "result"),
    (18, 1): ([MODEL, CALC], "result"),
    (19, 1): ([MODEL, "4.5 Small Conclusion"], "result"),
    (19, 2): ([MODEL, "4.5 Small Conclusion"], "result"),
    (19, 3): ([MODEL, "4.6 Sensitivity Analysis"], "sensitivity"),
    (20, 1): ([MODEL, "4.6 Sensitivity Analysis"], "sensitivity"),
    (20, 2): ([MODEL, "4.6 Sensitivity Analysis"], "sensitivity"),
    (21, 1): ([NEW, "5.2 Simulation Results"], "result"),
    (23, 1): ([NEW, CMP], "evaluation"),
    (23, 2): ([NEW, CMP], "evaluation"),
    (24, 1): ([NEW, CMP], "evaluation"),
    (24, 2): ([NEW, CMP], "evaluation"),
    (25, 1): ([NEW, CMP], "evaluation"),
    (26, 1): ([FURTHER, "6.1 Applicability In Left-Hand Traffic Countries"], "result"),
    (28, 1): ([FURTHER, "6.2 Intelligent Traffic", "6.2.2 Simulation And Results"], "result"),
    (28, 2): ([FURTHER, "6.2 Intelligent Traffic", "6.2.2 Simulation And Results"], "result"),
    (28, 3): ([FURTHER, "6.2 Intelligent Traffic", "6.2.2 Simulation And Results"], "result"),
    (28, 4): ([FURTHER, "6.2 Intelligent Traffic", "6.2.2 Simulation And Results"], "result"),
}

# The three sensitivity tables are never cited by number; one deictic pointer on p19 covers all
# three - "and results are shown in following tables" - so each block carries that pointer with no
# printed number, count 0 and an empty style list.
DEICTIC = {"first_page": 19, "lead_pages": 0, "style": [], "count": 0,
           "lead_sentence": "and results are shown in following tables",
           "trail_sentence": "", "lead_pattern": "direct", "read_sentences": 1,
           "gap_sentences": None}
DEICTIC_NEXT = dict(DEICTIC, lead_pages=1)

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# Exhibit count per page, for doc_order.
VENTION = {4: 1, 7: 1, 9: 1, 11: 1, 12: 1, 14: 2, 15: 1, 16: 1, 17: 5, 18: 1, 19: 3,
           20: 2, 21: 1, 23: 2, 24: 2, 25: 1, 26: 1, 28: 4}

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


CAP = {
    1: "Figure 1: The logic framework of our paper.",
    2: "Figure 2: The choice between following and overtaking(i\u00a1j).",
    3: "Figure 3: Proportions of cars in different states after several transitions.",
    4: "Figure 4: Road condition when traffic is heavy.",
    5: "Figure 5: Description of the simulated freeway.",
    6: "Figure 6: The \u201cGo\u201d process.",
    7: "Figure 7: The \u201cReturn\u201d process.",
    8: "Figure 8: The general process of the simulation.",
    9: "Figure 9: Sub flowchart of the \u201cGo\u201d process.",
    10: "Figure 10: Danger index vs. \u03bb.",
    11: "Figure 11: Average traffic speed vs. \u03bb.",
    12: "Figure 12: Traffic flow vs. \u03bb.",
    13: "Figure 13: OSL effect vs. \u03bb.",
    14: "Figure 14: USL effect vs. \u03bb.",
    15: "Figure 15: A printscreen of simulation in light traffic, green lines represent cars.",
    16: "Figure 16: A printscreen of simulation in heavy traffic, green lines represent cars.",
    17: "Figure 17: A view of evaluation indexes for each traffic rule.",
    18: "Figure 18: RHT and LHT traffic systems.",
    19: "Figure 19: Comparison in traffic flow.",
    20: "Figure 20: Comparison in ATS.",
    21: "Figure 21: Comparison in USL effect.",
    22: "Figure 22: Comparison in OSL effect.",
}

T_CAP = {
    1: "Table 1: Simulation results.",
    2: "Table 2: Sensitivity analysis of the parameter p1 .",
    3: "Table 3: Sensitivity analysis of the parameter p2 .",
    4: "Table 4: Sensitivity analysis of the parameter d.",
    5: "Table 5: Evaluation of the new rules.",
    6: "Table 6: Values of the five normalized evaluation indexes.",
    7: "Table 7: The meaning of Saaty\u2019s scale for AHP preference.",
    8: "Table 8: Values of weights.",
    9: "Table 9: Values of the comprehensive evaluation index.",
}

# Numbered citations. `lead_pages` is the exhibit page minus the citing page, so a citation
# that looks forward on the page it is printed on is positive and a backward one negative.
MENTION = {
    1: mention(3, 1, ["Figure 1"],
               "The basic logic framework of our paper is shown in Figure 1.", "as-shown-in"),
    2: mention(7, 0, ["Figure 2"],
               "Figure 2 illustrates how an overtaking takes place.", "figure-n-shows"),
    3: mention(9, 0, ["Figure 3"],
               "From Figure 3 we can clearly see that the proportion vector equals to", "direct"),
    4: mention(10, 1, ["Figure 4"],
               "Figure 4 shows how the heavy traffic system works.", "figure-n-shows"),
    5: mention(12, 0, ["Figure 5"],
               "We only consider two lanes of the forward direction (see Figure 5).",
               "parenthetical"),
    6: mention(13, 1, ["Figure 6"], "as we showed in the Figure 6", "as-shown-in"),
    7: mention(13, 1, ["Figure 7"], "see Figure 7", "parenthetical"),
    8: mention(13, 2, ["Figure 8"], "Figure 8 shows the general process of the simulation.",
               "figure-n-shows"),
    9: mention(14, 2, ["Figure 9"], "as is shown in Figure 9", "as-shown-in"),
    10: mention(18, -1, ["Figure 10"], "As can be seen in Figure 10", "as-shown-in"),
    11: mention(18, -1, ["Figure 11"],
                "As is shown in Figure 11,one of the criteria to evaluate the traffic condition",
                "as-shown-in"),
    12: mention(18, -1, ["Figure 12"],
                "Figure 12 shows the relation between the traffic flow and arrival rate.",
                "figure-n-shows"),
    13: mention(18, -1, ["Figure 13", "Figure 14"],
                "Figure 13 and Figure 14 show the under- or over-posted speed limits",
                "figure-n-shows"),
    14: mention(18, 0, ["Figure 14"],
                "Figure 13 and Figure 14 show the under- or over-posted speed limits",
                "figure-n-shows"),
    15: mention(18, 1, ["Figure 15"],
                "we can clearly see from the Figure 15 that cars in the right lane are much "
                "more than cars", "as-shown-in"),
    16: mention(19, 0, ["Figure 16"], "the result is shown in Figure 16", "as-shown-in"),
    17: mention(22, 1, ["Figure 17"],
                "We use a radar chart of Figure 17 to display our results.", "direct"),
    18: mention(26, 0, ["Figure 18"], "as the following Figure 18 shows", "figure-n-shows"),
    19: mention(28, 0, ["Figure 19"], "Results are shown from Figure 19 to Figure 22.", "direct"),
    20: mention(28, 0, ["Figure 20"], "Results are shown from Figure 19 to Figure 22.", "direct"),
    21: mention(28, 0, ["Figure 21"], "Results are shown from Figure 19 to Figure 22.", "direct"),
    22: mention(28, 0, ["Figure 22"], "Results are shown from Figure 19 to Figure 22.", "direct"),
    101: mention(17, 0, ["Table 1"], "results are listed below in Table 1", "direct"),
    102: DEICTIC,
    103: DEICTIC_NEXT,
    104: DEICTIC_NEXT,
    105: mention(21, 0, ["Table 5"], "We show the results in Table 5.", "direct"),
    106: mention(22, 1, ["Table 6"],
                "The values of all evaluation indexes are listed below in Table 6.", "direct"),
    107: mention(23, 1, ["Table 7"],
                "According to Table 7, we can easily build a 5*5 reciprocal matrix", "direct"),
    108: mention(24, 0, ["Table 8"], "Table 8 shows the values of", "figure-n-shows"),
    109: mention(24, 1, ["Table 9"], "See Table 9.", "direct"),
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
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, position: str) -> dict:
    return {
        "verbatim": text,
        "numbering": "Figure N:" if text.startswith("Figure") else "Table N:",
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


def figure(page: int, reg: int, family: str, key: int, *, position: str = "below",
           panels: int = 1, layout: str = "1", legend: str = "none", colorbar: bool = False,
           numbers: bool = True, labels: bool = False, other_note: str = "",
           note: str = "") -> None:
    ORDER.append((page, reg))
    text = printed(page, CAP[key])
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": dict(MENTION[key]),
        "caption": caption_block(text, position),
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


def table(page: int, reg: int, key: int, *, rows: int, cols: int, header_rows: int = 1,
          rules: str = "booktabs", zebra: bool = False, numeric_cols: int = 0,
          text_cols: int = 0, merged: bool = False, continued: bool = False,
          note: str = "") -> None:
    ORDER.append((page, reg))
    text = printed(page, T_CAP[key])
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": dict(MENTION[100 + key]),
        "caption": caption_block(text, "above"),
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
    # --- page 1: the summary sheet ---------------------------------------------------------
    excluded(1, 1, "not-an-exhibit",
             "The summary-sheet form: the 'Team Control Number / For office use only' grid and "
             "the 29282 entry in 159 vector paths. A contest-office form, not a paper exhibit, "
             "so it carries no caption and no figure number.")
    excluded(1, 2, "not-an-exhibit",
             "The summary-sheet title band - the contest name, the team number and the one-line "
             "summary heading printed in two vector paths. A ruling line, not an exhibit.")

    # --- section 1: the roadmap ------------------------------------------------------------
    figure(4, 1, "flowchart-or-schematic", 1, numbers=False, labels=True,
           note="The paper's roadmap as a left-to-right box-and-arrow tree on a raster: eleven "
                "labelled boxes in three levels, branching into the two rule options and "
                "funnelling three performance boxes into a right-hand 'simulation model' box on "
                "dashed arrows labelled 'test'. No numbers and no legend; the level labels are "
                "the only annotation [geometry.printed_numbers].")

    # --- section 3.2: the transition model --------------------------------------------------
    figure(7, 1, "flowchart-or-schematic", 2, numbers=False, labels=True,
           note="A two-lane road strip drawn as a raster with three yellow car cells in four "
                "positions: red arrows branch upward into an overtaking path in the left lane "
                "and stay in-lane on a following path, each labelled with its probability, "
                "'probability p(vi-vj)' and 'probability 1-p(vi-vj)', plus a 'forward "
                "direction' arrow. The caption itself is corrupted in the text layer - it "
                "prints 'overtaking(i\u00a1j)' where the art shows the subscripts vi and vj - and "
                "the caption is recorded exactly as printed [caption.verbatim].")
    figure(9, 1, "line", 3, legend="inside",
           note="Three marker-and-line series on a fully dotted grid, inside a boxed legend at "
                "the upper right: state 3 climbing to 1.0, state 2 decaying from 0.5 and state "
                "1 from 0.2, all flat by roughly the sixth transition. Axes are numbered, x 0 "
                "to 20 in steps of 2 and y 0 to 1 in steps of 0.1. The caption promises "
                "proportions 'after several transitions' while twenty transitions are plotted "
                "[geometry.printed_numbers].")

    # --- section 3.3: heavy traffic ----------------------------------------------------------
    figure(11, 1, "flowchart-or-schematic", 4, numbers=False, labels=True,
           note="A congested two-lane road strip: five yellow car cells labelled 'speed:v3' and "
                "'speed:v4', with three dimension brackets each marked 'D' over the safe "
                "distance between cars. Drawn art, no photograph, and no numeric scale.")

    # --- section 4.2: the cellular automaton ------------------------------------------------
    figure(12, 1, "flowchart-or-schematic", 5, numbers=False,
           note="The simulated freeway as a long blue-outlined rectangle split by dashed cell "
                "dividers, a hatched entrance cell at the left with an 'arriving cars / "
                "entrance' arrow, a cell width labelled 'L' and a spanning arrow above labelled "
                "'S cells (S\u00d7L)'. Letters only, no numbers.")

    # --- section 4.3: the two half-steps and the flowcharts ---------------------------------
    figure(14, 1, "flowchart-or-schematic", 6, numbers=False, labels=True,
           note="The 'Go' process: a two-lane strip with the rear and ahead cars adjacent, a "
                "short vertical red arrow off the rear car and a red forward arrow off the lead "
                "car, and two brackets marked 'D' over the 'no car' gaps. No numbers.")
    figure(14, 2, "flowchart-or-schematic", 7, numbers=False, labels=True,
           note="The 'Return' process uses the same strip and the same 'D' bracket notation as "
                "Figure 6 but mirrors the motion: the vertical red arrow points down and the "
                "brackets sit below the lanes. A near-duplicate of Figure 6, not an identical "
                "plate [geometry.panel_count].")
    figure(15, 1, "flowchart-or-schematic", 8, numbers=True,
           note="A tall vertical decision flowchart, about sixteen nodes in one column with a "
                "left-hand feedback loop, carrying an in-figure title 'Flowchart of simulation' "
                "at the upper left. Branch exits are lettered Y/N, and the parameter boxes print "
                "the actual settings - T=2000, S=1000, p1=0.3, p2=0.7, d=2, t=0, and 2\u00d7S - "
                "so numbers are printed in this diagram even though no axis exists "
                "[geometry.printed_numbers].")
    figure(16, 1, "flowchart-or-schematic", 9, numbers=False,
           note="The 'Go' sub-flowchart: eight decision nodes in one column with an in-figure "
                "title 'Sub flowchart of \u201cGo\u201d process'. Branch exits are Y/N and the "
                "condition boxes print cell expressions such as 'cells(2,i)>cells(2,j)+1' and "
                "'j=i-D...i+D' rather than values, so no numbers are printed "
                "[geometry.printed_numbers].")

    # --- section 4.4: the simulation results -------------------------------------------------
    table(17, 1, 1, rows=6, cols=3, rules="vertical-rules", numeric_cols=2, text_cols=1,
          note="'Arrival rate \u03bb | 0.25 | 0.4' with the lambda given bare and unitless over "
               "five criteria rows (Danger index, Average traffic speed, Traffic flow), OSL "
               "effect, USL effect). Full-width top and bottom rules with a rule under the "
               "header and a rule after every body row, two internal vertical rules and no "
               "outer side frame, so `rule_style` is `vertical-rules`; the ground is uniformly "
               "white, so `zebra` is false. The fourth criterion prints with a stray closing "
               "parenthesis, 'Traffic flow)', and its label is lower-cased where Table 5 "
               "capitalises the same index [caption.verbatim].")
    figure(17, 2, "scatter", 10, legend="inside",
           note="Blue data dots with a red fitted curve: the danger index rises to a hump near "
                "1.45 around \u03bb = 0.15 and then decays to about 0.6. The x axis is "
                "'lambda(vehicles per second)' and the y axis 'Danger index(times per vehicle)', "
                "with the legend boxed inside at the upper right. A raster paste, so the dots "
                "are pixels rather than vector marks [geometry.family].")
    figure(17, 3, "scatter", 11, legend="inside",
           note="The same construction for average speed: blue dots along a red fit decaying "
                "from about 4.0 at the low end to an asymptote near 3.33, x 'lambda(vehicles "
                "per second)', y 'Average traffic speed(m/s)', legend inside at the upper "
                "right.")
    figure(17, 4, "scatter", 12, legend="inside",
           note="Traffic flow against arrival rate: blue dots tracking a red fit that rises "
                "almost linearly from about 0.25 to 1.55, x 'lambda(vehicles per second)', y "
                "'Traffic flow(vehicles per second)', legend inside at the upper left.")
    figure(17, 5, "scatter", 13, legend="inside",
           note="The OSL effect on a red fit that climbs almost straight from about 0.4 to "
                "2.75, y axis titled 'OSL_effect' with the underscore printed literally, legend "
                "inside at the upper left.")
    figure(18, 1, "scatter", 14, legend="inside",
           note="The USL effect on a red fit rising steadily from about 0.2 to 1.5, y axis "
                "'USL_effect'. This is the only one of the five plots whose caption sits on "
                "page 18 with its art, while Figures 10 to 13 are captioned on the same page "
                "but drawn a page earlier [mention.lead_pages].")

    # --- section 4.5: the light- and heavy-traffic strips ------------------------------------
    figure(19, 1, "flowchart-or-schematic", 15, numbers=False,
           note="Captioned as a 'printscreen' but drawn as art: a sparse two-lane strip with "
                "thin green car bars, nearly all of them in the lower lane, and a red 'forward "
                "direction' arrow. No axes, no legend, no numbers [geometry.legend].")
    figure(19, 2, "flowchart-or-schematic", 16, numbers=False,
           note="The same strip under heavy traffic: long green car bars packed into both "
                "lanes, again with the red 'forward direction' arrow at the right and no axes "
                "or legend.")

    # --- section 4.6: sensitivity ------------------------------------------------------------
    table(19, 3, 2, rows=6, cols=6, rules="booktabs", numeric_cols=5, text_cols=1,
          merged=True, continued=False,
          note="Header 'p1 | DI | ATS | TL | OSL | USL' with p set in italic and the 1 as a "
               "subscript, over a single full-width merged row 'p1 = 0.3(original value)' and "
               "four data rows (0.2, 0.25, 0.35, 0.4) holding percentage changes. Top rule, "
               "header rule, a rule under the merged row and a bottom rule, with no rule "
               "between the four data rows and no vertical rules at all, so `rule_style` is "
               "`booktabs` and `merged_cells` is true [table.rule_style].")
    table(20, 1, 3, rows=6, cols=6, rules="booktabs", numeric_cols=5, text_cols=1,
          merged=True,
          note="The same construction for p2: merged row 'p2 = 0.7(original value)' over data "
               "rows 0.6, 0.65, 0.75, 0.8. Every other cell carries two decimals but the 0.75 "
               "row prints '11.6%' with one [table.rows].")
    table(20, 2, 4, rows=6, cols=6, rules="booktabs", numeric_cols=5, text_cols=1,
          merged=True,
          note="The same construction for d, whose merged row reads 'd = 2(original value)' "
               "over data rows 1.6, 1.8, 2.2, 2.4 - the only one of the three sensitivity "
               "tables whose values are symmetric about the original setting [table.merged_cells].")

    # --- section 5: the new rules ------------------------------------------------------------
    table(21, 1, 5, rows=6, cols=5, rules="vertical-rules", numeric_cols=4, text_cols=1,
          note="Header with a blank first cell over 'the old rule | New Rule 1 | New Rule 2 | "
               "New Rule 3', then five index rows (Traffic Flow, Danger Index, Average Traffic "
               "Speed, USL Effect, OSL Effect). One vertical rule between the label column and "
               "the data columns, rules under the header and at the foot, no inter-row rules "
               "and no outer side frame [table.cols]. Danger Index under New Rule 2 prints '0' "
               "where every neighbour carries four decimals.")

    # --- section 5.3: the AHP evaluation -----------------------------------------------------
    table(23, 1, 6, rows=6, cols=5, rules="vertical-rules", numeric_cols=4, text_cols=1,
          note="The normalized indexes: same blank-headed column layout as Table 5 over five "
               "rows (TFI, SI, ATSI, USLI, OSLI). The single vertical separator sits between "
               "the label column and the data columns, and several cells print '0' or '1.0000' "
               "where their neighbours carry mixed decimals [table.numeric_cols].")
    figure(23, 2, "line", 17, legend="outside-right", numbers=True,
           other_note="radar/spider chart: five category spokes (TFI, SI, ATSI, USLI, OSLI) "
                      "with concentric ring gridlines, radial ticks 0, 0.2, 0.4, 0.6, 0.8 and 1 "
                      "printed along the top spoke, four closed polylines labelled The Old "
                      "Rule, New Rule 1, New Rule 2 and New Rule 3, and the key set outside the "
                      "frame at the right",
           note="The four rules compared as four closed polylines on a five-spoke radar. No "
                "rectilinear axes exist, so the row is recorded under the closest family the "
                "lane has - `line`, the same call made for the radar on page 9 of "
                "P-A-2022-2209466-5952dd05 - and the radar construction is stated in "
                "`other_note` instead of being invented as a family [geometry.family].")
    table(24, 1, 7, rows=8, cols=2, rules="booktabs", numeric_cols=0, text_cols=2,
          note="Saaty's preference scale: 'Scale | Meaning' over seven rows - the odd scales 1, "
               "3, 5, 7, 9, the even scales given as one row '2, 4, 6, 8', and 'Reciprocals'. "
               "Top rule, header rule and bottom rule only, no inter-row and no vertical rules "
               "[table.rule_style]. The even-scale row spells 'judgements' with a British e.")
    table(24, 2, 8, rows=2, cols=6, rules="vertical-rules", numeric_cols=5, text_cols=1,
          note="The AHP weight vector in one row: header 'Single Evaluation Index | TFI | SI | "
               "ATSI | USLI | OSLI' over a single body row 'Weight | 0.3502 | 0.3001 | 0.1723 | "
               "0.0944 | 0.0830'. Five vertical rules between all adjacent columns with no "
               "outer side frame; the header names the index family rather than describing the "
               "column below it [table.header_rows].")
    table(25, 1, 9, rows=2, cols=5, rules="vertical-rules", numeric_cols=4, text_cols=1,
          note="The comprehensive index: header 'Traffic Rule | Old Rule | New Rule 1 | New "
               "Rule 2 | New Rule 3' over one row 'EIC | 0.4092 | 0.7078 | 0.9219 | 0.4123', "
               "with italic E and a subscript C. Four vertical rules between adjacent columns. "
               "The first column heading says 'Traffic Rule' while its only cell is the "
               "composite index itself, so the header does not describe its column "
               "[caption.verbatim].")

    # --- section 6: further topics -----------------------------------------------------------
    figure(26, 1, "flowchart-or-schematic", 18, panels=2, layout="1x2", numbers=False,
           note="Two four-lane diagrams side by side, drawn as raster art: yellow car boxes "
                "with red centre dots and up and down arrows, sub-labelled 'New Rule 2 in LHT' "
                "and 'New Rule 2 in RHT', with a four-way direction cross labelled "
                "forward/backward/left/right between them instead of a legend. The caption "
                "promises 'RHT and LHT traffic systems' and the art illustrates only New Rule "
                "2, with the left-hand panel printed first [geometry.panel_count].")
    figure(28, 1, "line", 19, legend="inside",
           note="Two straight lines comparing the intelligent-driver system against the plain "
                "system: blue solid and red dashed, the dashed one slightly higher, ending near "
                "1.58 against 1.50. Axes 'lambda(vehicles per second)' and 'Traffic flow"
                "(vehicles per second)', legend inside at the upper left.")
    figure(28, 2, "line", 20, legend="inside",
           note="The same pair for average speed: two decaying curves, the red dashed above the "
                "blue, flattening near 3.45 and 3.32, y axis 'Average traffic speed(m/s)'.")
    figure(28, 3, "line", 21, legend="inside",
           note="The USL effect pair: two widely separated straight lines, the red dashed "
                "running from about 0.5 to 2.75 well above the blue from 0.18 to 1.5 - the "
                "widest gap of the four comparisons.")
    figure(28, 4, "line", 22, legend="inside",
           note="The OSL effect pair: two nearly coincident straight lines from about 0.45 to "
                "2.7, the red dashed only marginally above the blue, which is the closeness the "
                "prose remarks on.")

    rules = [
        "The paper numbers its exhibits flatly and with a colon - 'Figure 1:' to 'Figure 22:' "
        "and 'Table 1:' to 'Table 9:' - so the colon forms fit every record and no exhibit is "
        "numbered 'Fig' [caption.numbering].",
        "Every figure caption prints BELOW its art and every table caption ABOVE its grid, and "
        "the positions are recorded as printed [caption.position].",
        "Pages 17 and 28 each print two captions to a line, so each panel gets its own row and "
        "the fragment quoted for it is the one carrying its own figure number "
        "[caption.verbatim].",
        "Figures 10 to 14 are the only `scatter` rows: blue data dots read off a raster paste "
        "with a red fitted curve drawn through them, five panels sharing one frame style "
        "[geometry.family].",
        "Figure 17 is a five-spoke radar with four closed polylines and no rectilinear axis at "
        "all, so it is recorded `line` on the precedent of the radar on page 9 of "
        "P-A-2022-2209466-5952dd05 and its construction is spelled out in `other_note` rather "
        "than approximated by a family the enum does not have [geometry.family].",
        "Figures 15 and 16 are captioned 'a printscreen of simulation' but the art is a drawn "
        "two-lane strip of green bars with a red direction arrow, not a screenshot, so both are "
        "recorded `flowchart-or-schematic` and the misdescription is kept in the note "
        "[geometry.family].",
        "Figure 18 declares two panels - LHT and RHT - and the art sub-labels them 'New Rule 2 "
        "in LHT' and 'New Rule 2 in RHT', while the caption claims to show the two traffic "
        "systems in general [geometry.panel_count].",
        "Legends sit inside the frame at a corner in all nine of the plot rows and outside at "
        "the right in the radar; the strips and box diagrams carry none, and the direction "
        "cross in Figure 18 is an in-figure annotation rather than a key [geometry.legend].",
        "The two flowcharts print numbers - Figure 8 lists T=2000, S=1000, p1=0.3, p2=0.7, d=2 "
        "and 2\u00d7S in its parameter boxes - while Figures 1, 2, 4, 5, 6, 7, 9 and 18 carry "
        "letters and expressions only [geometry.printed_numbers].",
        "The three sensitivity tables share one construction: a full-width merged "
        "'original value' row over four data rows, horizontal rules only, so all three are "
        "`booktabs` with `merged_cells` true and `zebra` false [table.merged_cells].",
        "Table 1 is the paper's one dense grid - a rule after every body row and two internal "
        "vertical rules, but still no outer side frame - so it is `vertical-rules` like Tables "
        "5, 6, 8 and 9, and Tables 5 and 6 carry a single separator between the label column "
        "and the data [table.rule_style].",
        "The citations run both ways: Figures 10 to 13 are captioned on page 17 and discussed "
        "on page 18, and Tables 6, 7 and 9 plus Figure 17 are each cited one page before the "
        "page their grids or art are printed on, so those blocks carry a negative "
        "`lead_pages` [mention.lead_pages].",
        "Tables 2, 3 and 4 are never cited by number anywhere in the prose; the only pointer is "
        "the p19 clause 'results are shown in following tables', a deictic reference printing no "
        "number, so all three blocks record that clause with an empty style list and count 0 "
        "rather than a figure the paper never prints [mention.first_page].",
    ]

    payload = {
        "paper": PID,
        "source": ("F:/MCM/MCM-ICM-master/2014\u7f8e\u8d5b\u7279\u7b49\u5956/"
                   "A-29282-Outstanding.pdf"),
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Thirty-three measured regions over nineteen of thirty pages, and they resolve into "
            "22 figure rows, 9 printed tables and 2 exclusions on the summary sheet, with no "
            "unresolved and no declared gaps. Families: 11 `flowchart-or-schematic` (the p4 "
            "roadmap, the two-lane strips of Figures 2, 4, 6, 7, 15, 16 and 18, the freeway "
            "schematic of Figure 5 and the two decision flowcharts of Figures 8 and 9), 6 "
            "`line` (Figure 3's three-series state plot, the radar of Figure 17 and the four "
            "two-curve comparisons of Figures 19 to 22), 5 `scatter` (Figures 10 to 14, blue "
            "dots under a red fitted curve) and 9 `table-grid`, so 22 figures and 9 tables "
            "average 10.3 exhibits over the nineteen density pages and just over one per page "
            "across the whole paper. Every caption survives in the text layer here, so none is "
            "typed from the crop, and the numbering is flat with a colon throughout. The radar "
            "of Figure 17 is the one shape the enum does not name: it is recorded `line` on the "
            "same call made for page 9 of P-A-2022-2209466-5952dd05, with its five spokes, ring "
            "gridlines and outside-right key stated in `other_note`. Faults worth carrying "
            "downstream: Figure 2's caption is corrupted to 'overtaking(i\u00a1j)', Figures 15 "
            "and 16 are called printscreens though they are drawn strips, Figure 18's caption "
            "promises both traffic systems but the art illustrates only New Rule 2, Table 1 "
            "prints 'Traffic flow)' with a stray parenthesis, and Table 9's first column is "
            "headed 'Traffic Rule' over the composite index."
        ),
    }
    out = PROXY / "pc53-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
