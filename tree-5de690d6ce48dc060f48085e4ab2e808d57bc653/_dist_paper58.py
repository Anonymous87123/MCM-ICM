"""Hand pass for P-B-2014-26333-27e7d8ab (a 2014 B paper that builds a two-lane
lane-changing model, an extended "Ring Road" cellular automaton and a refined model
with ramps, then ranks overtaking rules with a fuzzy synthetic evaluation over
lanes / speed limits / signalling / intelligent systems), 54 PDF pages.

Sixty-three measured regions over thirty-four pages, all accounted for: thirty-three
figures, twelve printed tables, and the right-hand panel of every two-panel figure
refused as a fragment of the same exhibit. One printed exhibit carries no region at
all and is declared a gap rather than invented (Table 3, page 16).

    page    region   what it is
    8       r1       Table 1  symbol table, constants block
    9       r1       Table 2  symbol table, variables block
    11      r1       Figure 1 two-lane picture of a change to the left lane
    13      r1       Figure 2 the mirror picture, change back to the right lane
    16      r1       Figure 3 "Clarification of some denotes"; Table 3 is printed
                     ABOVE it at y=290-360 with no measured region - declared gap
    18      r1       Figure 4 flow chart of the cellular automaton, whole page
    20      r1       Figure 5 satellite photograph of a real interchange
    22      r1-r2    Figure 6 time-space diagrams, occupancy 0.1 and 0.4
    24      r1       Figure 7 total flow rate against occupancy
    25      r1-r2    Figure 8 flow rate of each lane (3 and 4 lanes)
    25      r3       Figure 9 average speed against occupancy
    26      r1-r2    Figure 10 average speed of each lane
    26      r3-r4    Figure 11 lane utilisation ratio of each lane
    27      r1       Figure 12 sharp braking frequency against occupancy
    28      r1       Figure 13 shift ratio against occupancy
    28      r2       Figure 14 satisfaction against occupancy
    29      r1       Figure 15 standard deviation of speed against occupancy
    30      r1-r2    Figure 16 flow rate and average speed under maximum limits
    31      r1-r2    Figure 17 sharp braking and shift ratio under maximum limits
    31      r3-r4    Figure 18 lane utilisation ratio under maximum limits
    32      r1-r2    Figure 19 flow rate and average speed under minimum limits
    33      r1-r2    Figure 20 sharp braking and shift ratio under minimum limits
    33      r3-r4    Figure 21 lane utilisation ratio under minimum limits
    34      r1-r2    Figure 22 flow rate and average speed with and without signalling
    35      r1-r2    Figure 23 sharp braking and shift ratio with and without signalling
    37      r1-r2    Figure 24 flow rate and average speed, five basic rules
    38      r1       Figure 25 sharp braking frequency, five basic rules
    39      r1-r2    Figure 26 satisfaction and standard deviation, five basic rules
    40      r1       Table 4  criteria of the basic rules in light traffic
    41      r1       Table 5  relative deviations, light traffic
    41      r2       Table 6  relative deviations, heavy traffic
    43      r1       Table 7  relative deviations of all nine rules
    44      r1       Table 8  sensitivity, percentages of vehicles, light
    44      r2       Table 9  sensitivity, percentages of vehicles, heavy
    45      r1       Table 10 sensitivity, randomisation probability, light
    45      r2       Table 11 sensitivity, randomisation probability, heavy
    46      r1       Table 12 sensitivity, willingness to change lane, light
    46      r2       Table 13 sensitivity, willingness to change lane, heavy
    48      r1-r2    Figure 27 flow rate and average speed with intelligent systems
    49      r1-r2    Figure 28 sharp braking and shift ratio with intelligent systems
    49      r3-r4    Figure 29 lane utilisation ratio with intelligent systems
    50      r1       Figure 30 flow rate against p_exit
    51      r1       Figure 31 average speed against p_exit
    51      r2-r3    Figure 32 lane utilisation ratio against p_exit
    52      r1       Figure 33 failure ratio against p_exit

Usage: python -I tools/_dist_paper58.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2014-26333-27e7d8ab"
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

NOTATION = "3 Notations"
BASIC = "5.1 The Basic Lane-changing Model"
LEFT = "5.1.1 Changing to the Left Lane"
RIGHT = "5.1.2 Changing Back to the Right Lane"
RING = "5.2 The Extended “Ring Road” Model"
LAWS = "5.2.3 Laws Governing the Cellular Automaton"
REFINED = "5.3 The Refined Model with Ramps"
RAMPS = "5.3.1 Adding Entrance and Exit Ramps"
FACTORS = "6 Results: Influencing Factors"
LANES = "6.2 Number of Lanes"
FLOW216 = "6.2.1 Flow Rate"
SPEED216 = "6.2.2 Average Speed"
UTIL216 = "6.2.3 Lane Utilization Ratio"
BRAKE216 = "6.2.4 Sharp Braking Frequency"
SHIFT216 = "6.2.5 Shift Ratio"
SAT216 = "6.2.6 Satisfaction"
STD216 = "6.2.7 Standard Deviation of Speed"
MAXLIM = "6.3 Maximum Speed Limit"
FLOWSPEED163 = "6.3.1 Flow Rate and Average Speed"
BRAKESHIFT163 = "6.3.2 Sharp Braking Frequency and Shift Ratio"
UTIL163 = "6.3.3 Lane Utilization Ratio"
MINLIM = "6.4 Minimum speed limit"
FLOWSPEED164 = "6.4.1 Flow Rate and Average Speed"
BRAKESHIFT164 = "6.4.2 Sharp Braking Frequency and Shift Ratio"
UTIL164 = "6.4.3 Lane Utilization Ratio"
SIGNAL = "6.5 Signal Before Shifting"
FLOWSPEED165 = "6.5.1 Flow Rate and Average Speed"
BRAKESHIFT165 = "6.5.2 Sharp Braking Frequency and Shift Ratio"
OPTIMAL = "7 Results: the Optimal Rule"
CRITERIA = "7.2 Criteria and Single Criterion Analysis for Basic Rules"
TRAFFICFLOW172 = "7.2.1 Traffic Flow Criteria: Flow Rate and Speed"
SAFETY172 = "7.2.2 Safety Criterion: Sharp Braking Frequency"
EXPERIENCE172 = "7.2.3 Experience Criterion: Satisfaction and Standard Deviation of Speed"
FSE = "7.3 Fuzzy Synthetic Evaluation for Basic Rules"
ALTERNATIVES = "7.3.1 Identify Alternatives and Attributes"
FSERESULTS = "7.3.4 The Results"
CONCLUSIONS76 = "7.6 Conclusions"
SENS = "8 Sensitivity Analysis"
SENSVEH = "8.1 Percentages of Vehicles"
SENSRAND = "8.2 Probability of Randomization"
SENSWILL = "8.3 Probability of Willing to Change Lane"
DISCUSS = "9 Further Discussions"
INTELLIGENT = "9.2 Modifications for An Intelligent System"
INTFLOW = "9.2.1 Flow Rate and Average Speed"
INTBRAKE = "9.2.2 Sharp Braking Frequency and Shift Ratio"
INTUTIL = "9.2.3 Lane Utilization Ratio"
RAMPEXTRA = "9.3 Additional Research on the Refined Model with Ramps"
PEXITFLOW = "9.3.1 Flow Rate"
PEXITSPEED = "9.3.2 Average Speed"
PEXITUTIL = "9.3.3 Lane Utilization Ratio"
PEXITFAIL = "9.3.4 Failure Ratio"

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def place(page: int, reg: int, path: list[str], kind: str) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(path),
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": c["region"],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def none_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          trail: str = "", read: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": lead, "trail_sentence": trail,
            "lead_pattern": "direct", "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, numbering: str, position: str) -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": 1 if verbatim else 0,
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap: str, mention: dict,
           path: list[str], kind: str, *, panels: int = 1, layout: str = "1",
           legend: str = "none", labels: bool = False, note: str = "") -> None:
    word = q(cap, page)
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": word,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, path, kind),
        "mention": mention,
        "caption": caption(word, "Figure N", "below"),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": True,
            "data_labels": labels,
        },
    })


def table(page: int, reg: int, rows: int, cols: int, cap: str, mention: dict,
          path: list[str], kind: str, *, header_rows: int = 1, rules: str = "booktabs",
          merged: bool = False, num: int = 0, txt: int = 0, decimal: bool = False,
          note_sentence: str = "", note: str = "") -> None:
    word = q(cap, page)
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": word,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, path, kind),
        "mention": mention,
        "caption": caption(word, "Table N", "above"),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": rules,
            "zebra": False,
            "merged_cells": merged,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": decimal,
            "numeric_cols": num,
            "text_cols": txt,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": note_sentence,
        },
    })


def exclude(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "region": reg, "bbox": REG[(page, reg)],
                     "reason": reason, "note": note})


def second_panel(page: int, reg: int, owner_reg: int, which: str) -> None:
    """One printed figure number over two panels: the right-hand panel is the same row."""
    b, o = REG[(page, reg)], REG[(page, owner_reg)]
    exclude(page, reg, "fragment-of-other",
            f"the second panel of {which} at x {b[0]:.0f}-{b[2]:.0f}; the figure prints one "
            f"number and one caption below the pair, so it is counted once, on the left "
            f"panel at x {o[0]:.0f}-{o[2]:.0f}")


def build() -> str:
    # ---- 3 Notations: the two symbol tables -----------------------------------
    table(8, 1, 5, 3, "Table 1 Symbol Table–Constants",
          cited(8, 8, ["Table 1"], 1,
                "All the variables and constants used in this paper are listed in Table 1 and Table 2."),
          [NOTATION], "symbols", header_rows=2, merged=True, txt=3,
          note_sentence="All the variables and constants used in this paper are listed in Table 1 and Table 2.",
          note="booktabs with three rules (under the caption, under the header, at the "
               "foot) and no verticals; the first header row is the single merged group "
               "label Constants, so header_rows=2; one of only two tables in the paper "
               "that carry a group row")
    table(9, 1, 35, 3, "Table 2 Symbol Table–Variables",
          cited(8, 9, ["Table 2"], 1,
                "All the variables and constants used in this paper are listed in Table 1 and Table 2."),
          [NOTATION], "symbols", header_rows=2, merged=True, txt=3,
          note="the whole page is this table; same booktabs construction and same merged "
               "group row, this time labelled Variables; thirty-five variable rows in four "
               "blank-separated blocks that print no rule between them, so the block "
               "breaks are white space only")

    # ---- 5.1 the basic lane-changing model ------------------------------------
    figure(11, 1, "flowchart-or-schematic", "Figure 1 Change-to-the-left-lane",
           cited(11, 11, ["Figure 1"], 1,
                 "Figure 1 illustrates the situation that the red car tends to change to the left lane."),
           ["5 The Keep-Right-Except-To-Pass Model", BASIC, LEFT], "other",
           note="two-lane road band with the subject car in red, the neighbours in grey, "
                "dashed lane dividers and dimension arrows for D_l,b,gap / D_l,f,gap / gap; "
                "no axes and no data, so it is a schematic, not a plot")
    figure(13, 1, "flowchart-or-schematic", "Figure 2 Change-back-to-the-right-lane",
           cited(12, 13, ["Figure 2"], 1,
                 "Figure 2 illustrates this change-back-to-the-right-lane situation."),
           ["5 The Keep-Right-Except-To-Pass Model", BASIC, RIGHT], "other",
           note="the same picture mirrored: the red car sits in the left lane and the "
                "arrows now measure D_r,b,gap and D_r,f,gap; the caption prints at the top "
                "of page 13 under the running head, the artwork below it, still below the "
                "art the figure belongs to")
    figure(16, 1, "flowchart-or-schematic", "Figure 3 Clarification of some denotes",
           none_mention(),
           ["5 The Keep-Right-Except-To-Pass Model", RING, LAWS], "other",
           note="three-lane band with grey vehicles and the subject car in red, labelled "
                "vehicle_ij / lfgap_ij / lbgap_ij / rfgap_ij / rbgap_ij / gap_ij; the "
                "labels sit on a light blue full-bleed slab, so the crop reads like a "
                "screenshot rather than a white-background drawing. NEVER CITED BY NUMBER")
    figure(18, 1, "flowchart-or-schematic", "Figure 4 Flow chart of cellular automaton",
           cited(19, 18, ["Figure 4"], 1, "The algorithm is diagrammed in Figure 4."),
           ["5 The Keep-Right-Except-To-Pass Model", RING, LAWS], "other",
           note="whole-page flow chart, green Start and red Stop terminals over yellow "
                "action boxes and decision diamonds with loop-back arrows; the page carries "
                "no other text than the running head and the caption, and the prose cites "
                "it one page later, so the citation runs a page behind the art")
    figure(20, 1, "photo-or-raster-image", "Figure 5 A real freeway section containing ramps",
           cited(20, 20, ["Figure 5"], 1,
                 "Figure 5 demonstrates a real freeway section containing ramps."),
           ["5 The Keep-Right-Except-To-Pass Model", REFINED, RAMPS], "other",
           note="satellite photograph of a cloverleaf interchange over farmland; the only "
                "raster photograph in the paper and the only exhibit that is not drawn")

    # ---- 6 Results: influencing factors --------------------------------------
    figure(22, 1, "line", "Figure 6",
           none_mention(),
           [FACTORS], "result", panels=2, layout="1x2",
           note="two time-space diagrams, occupancy 0.1 and 0.4, each a dense fan of "
                "vehicle trajectories (location 0-2000 against time-step 0-1000); the two "
                "sub-captions (a) and (b) print under the panels and the number FIGURE 6 "
                "under them. THE PROSE CITES IT AS Figure 8 - page 22 reads 'The time space "
                "diagram (Figure 8) demonstrates these two kinds of traffic flow' - so the "
                "paper's first two-space diagram is never named by its own number")
    figure(24, 1, "line", "Figure 7 Total flow rate under the condition of different occupancies (3 & 4 lanes)",
           cited(24, 24, ["Figure 7"], 1, "From Figure 7, we can see that the optimal occupancy"),
           [FACTORS, LANES, FLOW216], "other", legend="inside",
           note="line chart with diamond markers, occupancy 0.1-0.6 against total flow "
                "0-2; two series only despite the caption promising 3 and 4 lanes; the "
                "4-lane curve runs above the 3-lane curve everywhere and both peak at 0.3 "
                "or just before it")
    figure(25, 1, "line", "Figure 8",
           cited(22, 25, ["Figure 8"], 1, "The time space diagram (Figure 8)"),
           [FACTORS, LANES, FLOW216], "other", panels=2, layout="1x2", legend="inside",
           note="flow rate of each lane, (a) 3 lanes and (b) 4 lanes, occupancy on x and "
                "flowrate 0-0.5 on y, one series per lane; the only citation of this "
                "number is the page-22 sentence that points at the time-space diagram, so "
                "its named mention leads the art by three pages")
    figure(25, 3, "line", "Figure 9 Average speed under the condition of different occupancies (3 & 4 lanes)",
           cited(25, 25, ["Figure 9"], 1,
                 "This common sense can be justified from the speed-occupancy Figure 9."),
           [FACTORS, LANES, SPEED216], "other", legend="inside",
           note="average speed 0-6 against occupancy, two series that lie almost exactly "
                "on top of each other; the paper's own reading of this is that the curves "
                "for 3 and 4 lanes coincide")
    figure(26, 1, "line", "Figure 10",
           none_mention(),
           [FACTORS, LANES, SPEED216], "other", panels=2, layout="1x2", legend="inside",
           note="average speed of each lane, (a) 3 lanes and (b) 4 lanes, three series on "
                "y 0-6 falling monotonically, cleanly separated left to right; NEVER CITED "
                "BY NUMBER")
    figure(26, 3, "line", "Figure 11",
           cited(27, 26, ["Figure 11"], 1,
                 "From the Figure 11, we can know that the lane utilization ratio"),
           [FACTORS, LANES, UTIL216], "other", panels=2, layout="1x2", legend="inside",
           note="lane utilisation ratio of each lane, (a) 3 lanes and (b) 4 lanes, y 0-1; "
                "the bottom y tick label 0 is cropped off the axis, so the printed scale "
                "starts at 0.1")
    figure(27, 1, "line", "Figure 12 Sharp braking frequency under the condition of different occupancies",
           none_mention(),
           [FACTORS, LANES, BRAKE216], "other", legend="inside",
           note="sharp braking frequency 0-0.1 against occupancy, an inverted U peaking "
                "near 0.3; NEVER CITED BY NUMBER")
    figure(28, 1, "line", "Figure 13 Shift ratio under the condition of different occupancies (3 & 4 lanes)",
           none_mention(),
           [FACTORS, LANES, SHIFT216], "other", legend="inside",
           note="shift ratio 0-0.1 against occupancy, both series collapsing between 0.1 "
                "and 0.2 and then flat, crossing just after 0.2; NEVER CITED BY NUMBER")
    figure(28, 2, "line", "Figure 14 Satisfaction under the condition of different occupancies (3 & 4 lanes)",
           none_mention(),
           [FACTORS, LANES, SAT216], "other", legend="inside",
           note="satisfaction 0-1 against occupancy, monotone decay, the two series "
                "overlapping so closely that one hides the other; NEVER CITED BY NUMBER")
    figure(29, 1, "line", "Figure 15 Std. deviation of speed.png under the condition of different occupancies (3 & 4 lanes)",
           none_mention(),
           [FACTORS, LANES, STD216], "other", legend="inside",
           note="standard deviation of speed 0-2 against occupancy, a mild inverted U; the "
                "printed caption still carries the source file name, 'Std. deviation of "
                "speed.png'; NEVER CITED BY NUMBER")

    # ---- 6.3 maximum speed limit ---------------------------------------------
    figure(30, 2, "bar", "Figure 16",
           cited(30, 30, ["Figure 16"], 1,
                 "We can clearly see that the results meet our expectations from the Figure 16."),
           [FACTORS, MAXLIM, FLOWSPEED163], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) flow rate and (b) average speed in light and heavy traffic under no "
                "limit, 5 cell/s and 4 cell/s; light and heavy are two adjacent bars inside "
                "one panel, never two panels; every bar carries its value, 4.552/1.496, "
                "4.139/1.504, 3.483/1.495 on the speed panel. THE DETECTOR NUMBERED THIS "
                "PAGE RIGHT TO LEFT, so the row is the left panel r2 and the refused "
                "fragment is r1")
    figure(31, 1, "bar", "Figure 17",
           cited(31, 31, ["Figure 17"], 1,
                 "Figure 17 demonstrate that the maximum speed limit can effectively reduce"),
           [FACTORS, MAXLIM, BRAKESHIFT163], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) sharp braking frequency and (b) shift ratio against the three maximum "
                "limits, light and heavy paired; the legend box sits inside the axes and "
                "the top bar label on the right pair comes within a few points of its lower "
                "edge")
    figure(31, 3, "bar", "Figure 18",
           cited(32, 31, ["Figure 18"], 1,
                 "From Figure 18, we can conclude that the utilization ratio"),
           [FACTORS, MAXLIM, UTIL163], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) lane utilisation ratio in light traffic and (b) in heavy traffic under "
                "the three maximum limits, three bars per category (1st/2nd/3rd lane); only "
                "one traffic regime per panel by design; the axis is drawn to 0.8 but the "
                "topmost label sits at 0.601 just under the legend")
    figure(32, 1, "bar", "Figure 19",
           cited(32, 32, ["Figure 19"], 1, "We can clearly conclude that from Figure 19"),
           [FACTORS, MINLIM, FLOWSPEED164], "other", panels=2, layout="1x2",
           legend="inside",
           note="(a) flow rate and (b) average speed under no minimum limit and a 3 cell/s "
                "minimum; only two x categories, so the panel prints four bars and a lot of "
                "white space; the minimum limit barely moves light traffic and lifts heavy "
                "traffic, the mirror of Figure 16")
    figure(33, 1, "bar", "Figure 20",
           cited(33, 33, ["Figure 20"], 1, "Figure 20 illustrates this conclusion."),
           [FACTORS, MINLIM, BRAKESHIFT164], "other", panels=2, layout="1x2",
           legend="inside",
           note="(a) sharp braking frequency and (b) shift ratio under the minimum limit; "
                "the heavy-traffic sharp braking bar falls BELOW the light one once the "
                "limit is imposed, the one crossover among the speed-limit figures")
    figure(33, 3, "bar", "Figure 21",
           cited(34, 33, ["Figure 21"], 1, "The results are shown in Figure 21."),
           [FACTORS, MINLIM, UTIL164], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) lane utilisation ratio in light traffic and (b) in heavy traffic under "
                "the minimum limit; the y axis is drawn to 0.7 but the printed tick labels "
                "stop at 0.6, and the legend is tall enough to reach two thirds of the plot "
                "height, with the 0.519 label abutting its left border")
    figure(34, 1, "bar", "Figure 22",
           cited(34, 34, ["Figure 22"], 1, "Figure 22 illustrates this change."),
           [FACTORS, SIGNAL, FLOWSPEED165], "other", panels=2, layout="1x2",
           legend="inside",
           note="(a) flow rate and (b) average speed with and without the signal-before-"
                "shifting mechanism; y 0-1.5 only, the narrowest scale in the figure set, "
                "and no x-axis title")
    figure(35, 1, "bar", "Figure 23",
           cited(35, 35, ["Figure 23"], 1, "Figure 23 demonstrates this statement."),
           [FACTORS, SIGNAL, BRAKESHIFT165], "other", panels=2, layout="1x2",
           legend="above", labels=True,
           note="(a) sharp braking frequency and (b) shift ratio with and without "
                "signalling; the only figure in the paper whose legend is placed ABOVE the "
                "axes rather than inside them, and its plot frame is narrower than the other "
                "bar panels because of it")

    # ---- 7 the optimal rule ---------------------------------------------------
    figure(37, 1, "bar", "Figure 24",
           cited(39, 37, ["Figure 24(a)"], 1,
                 "Figure 26(a) describes satisfaction and it is coherent with the speed Figure 24(a)."),
           [OPTIMAL, CRITERIA, TRAFFICFLOW172], "other", panels=2, layout="1x2",
           legend="inside",
           note="(a) flow rate and (b) average speed for the five basic rules, light and "
                "heavy paired per rule; NO value labels on any bar, unlike Figures 16-23 "
                "and 27-33. Its only named citation is a back-reference on page 39 that "
                "calls it Figure 24(a), two pages after the art")
    figure(38, 1, "bar", "Figure 25 Sharp braking frequency in light & heavy traffic (different rules)",
           cited(38, 38, ["Figure 25"], 1, "The results are presented in Figure 25."),
           [OPTIMAL, CRITERIA, SAFETY172], "other", legend="inside",
           note="single full-width panel, five rules against sharp braking frequency 0-0.12 "
                "with light and heavy paired; no value labels, so the ranking has to be read "
                "off the bar heights")
    figure(39, 1, "bar", "Figure 26",
           cited(39, 39, ["Figure 26"], 1,
                 "Figure 26(a) describes satisfaction and it is coherent with the speed Figure 24(a)."),
           [OPTIMAL, CRITERIA, EXPERIENCE172], "other", panels=2, layout="1x2",
           legend="inside",
           note="(a) satisfaction and (b) standard deviation of speed for the five basic "
                "rules; the satisfaction axis is labelled 0-1 in steps of 0.2 but drawn to "
                "about 1.2, leaving the top tick blank; no value labels. This is the figure "
                "whose heading 7.2.3 the heading detector missed, so the section path comes "
                "from the printed line")
    table(40, 1, 5, 6, "Table 4 Criteria of Basic Rules in Light Traffic",
          cited(40, 40, [], 0,
                "The values of each attributes of each alternative are listed as follows:"),
          [OPTIMAL, FSE, ALTERNATIVES], "evaluation", rules="vertical-rules", txt=1, num=5,
          note="five rules against five criteria; horizontal rules only except ONE internal "
               "vertical between the rule stub and the first criterion column; no zebra, no "
               "merged cells; the header cell over the flow-rate column wraps to two lines; "
               "the paragraph after it points at 'Table ??' for the ideal alternative, a "
               "broken cross-reference, and the next caption 'Table 4' is the only caption "
               "inside the region")
    table(41, 1, 1, 6, "Table 5 Relative deviations of different rules in light traffic",
          cited(41, 41, [], 0, "The relative deviation in both cases are listed below"),
          [OPTIMAL, FSE, FSERESULTS], "result", rules="vertical-rules", txt=5, num=1,
          note="one data row (F_i) against five rule names, so this is the same matrix as "
               "Table 4 transposed; rule names wrap to two lines; single vertical stub rule, "
               "no zebra")
    table(41, 2, 1, 6, "Table 6 Relative deviations of different rules in heavy traffic",
          none_mention(),
          [OPTIMAL, FSE, FSERESULTS], "result", rules="vertical-rules", txt=5, num=1,
          note="same construction and same one-row shape as Table 5, heavy traffic; its "
               "caption line, not the prose, is what introduces it, and the sentence 'The "
               "relative deviation in both cases are listed below' is recorded on Table 5 "
               "only")
    table(43, 1, 9, 4, "Table 7 Relative deviations of different rules in light & heavy traffic",
          none_mention(),
          [OPTIMAL, CONCLUSIONS76], "evaluation", rules="vertical-rules", txt=1, num=3,
          note="nine rules (five basic plus four improved) against light, heavy and overall; "
               "the widest stub cell 'partial-assigned-lane-and-keep-right' nearly touches "
               "the vertical rule; uncited by number, and it sits under 7.6 Conclusions "
               "although it reports the 7.5 evaluation")

    # ---- 8 sensitivity analysis ----------------------------------------------
    table(44, 1, 7, 6, "Table 8 Sensitivity analysis—percentages of vehicles(light traffic)",
          cited(43, 44, ["Table 8 and Table 9"], 1,
                "we change the percentage of large vehicles(40%) by up to 15% to obtain the changes in our criteria.(Table 8 and Table 9)"),
          [SENS, SENSVEH], "sensitivity", rules="vertical-rules", txt=1, num=5, decimal=True,
          note="seven perturbation rows (-15% to +15%) against five criteria; the percent "
               "stub column has NO header text, the header cell is blank; values centred, "
               "mixed sign and magnitude, so nothing lines up on the decimal point even "
               "though they are all percentages")
    table(44, 2, 7, 6, "Table 9 Sensitivity analysis—percentages of vehicles(heavy traffic)",
          cited(43, 44, ["Table 8 and Table 9"], 1,
                "we change the percentage of large vehicles(40%) by up to 15% to obtain the changes in our criteria.(Table 8 and Table 9)"),
          [SENS, SENSVEH], "sensitivity", rules="vertical-rules", txt=1, num=5,
          note="the heavy-traffic twin of Table 8, identical construction down to the blank "
               "stub header; the two are cited as one pointer on page 43")
    table(45, 1, 7, 6, "Table 10 Sensitivity analysis—probability of randomization(light traffic)",
          cited(44, 45, ["Table 10 and Table 11"], 1,
                "We change it by up to 15% and the sharp braking frequency shows a 15.75% deviation, which is ac- ceptable.(Table 10 and Table 11)"),
          [SENS, SENSRAND], "sensitivity", txt=1, num=5,
          note="same seven-row perturbation grid, this time with NO internal vertical rule - "
               "booktabs horizontal rules only; two header cells wrap ('sharp breaking "
               "frequency', 'std. deviation of speed'); the stub header is blank again")
    table(45, 2, 7, 6, "Table 11 Sensitivity analysis—probability of randomization(heavy traffic)",
          cited(44, 45, ["Table 10 and Table 11"], 1,
                "We change it by up to 15% and the sharp braking frequency shows a 15.75% deviation, which is ac- ceptable.(Table 10 and Table 11)"),
          [SENS, SENSRAND], "sensitivity", txt=1, num=5,
          note="twin of Table 10; its caption begins about 45 points below the bottom of "
               "Table 10's region, which is why the Table 10 crop carries no foreign caption")
    table(46, 1, 7, 6, "Table 12 Sensitivity analysis—probability of willing to change lane(light traffic)",
          none_mention(),
          [SENS, SENSWILL], "sensitivity", txt=1, num=5,
          note="same grid and same booktabs construction; the prose never cites this number "
               "and page 47's later pointer prints only '(tableand table. )', the two "
               "numbers lost from the sentence")
    table(46, 2, 7, 6, "Table 13 Sensitivity analysis—probability of willing to change lane(heavy traffic)",
          none_mention(),
          [SENS, SENSWILL], "sensitivity", txt=1, num=5,
          note="twin of Table 12, same blank stub header and same uncited state")

    # ---- 9 further discussions -----------------------------------------------
    figure(48, 2, "bar", "Figure 27",
           cited(48, 48, ["Figure 27"], 1, "This is consistent with the speed fig-"),
           [DISCUSS, INTELLIGENT, INTFLOW], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) flow rate and (b) average speed for the human, semi-intelligent and "
                "complete intelligent systems, light and heavy paired, value labels on every "
                "bar. THE DETECTOR NUMBERED THIS PAGE RIGHT TO LEFT, so the row is the left "
                "panel r2. The pointer to it on page 48 is hyphenated across a line break, "
                "'speed fig- ure.(Figure 27)'")
    figure(49, 1, "bar", "Figure 28",
           cited(48, 49, ["Figure 28"], 1,
                 "The intelligent system will certainly increase shift ratio. (Figure 28)"),
           [DISCUSS, INTELLIGENT, INTBRAKE], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) sharp braking frequency and (b) shift ratio for the three systems; the "
                "prose cites it one page before the art")
    figure(49, 4, "bar", "Figure 29",
           none_mention(),
           [DISCUSS, INTELLIGENT, INTUTIL], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) lane utilisation ratio in light traffic and (b) in heavy traffic for "
                "the three systems, three bars per category; the detector numbered this row "
                "right to left, so the row is the left panel r4; NEVER CITED BY NUMBER")
    figure(50, 1, "bar", "Figure 30 Flow rate in light & heavy traffic (different pexit )",
           none_mention(),
           [DISCUSS, RAMPEXTRA, PEXITFLOW], "other", legend="inside", labels=True,
           note="single panel, three p_exit categories (0.05 / 0.2 / 0.5) with light and "
                "heavy paired; the caption prints 'pexit' unsubscripted with a space before "
                "the closing bracket; NEVER CITED BY NUMBER")
    figure(51, 1, "bar", "Figure 31 Average speed in light & heavy traffic (different pexit )",
           none_mention(),
           [DISCUSS, RAMPEXTRA, PEXITSPEED], "other", legend="inside", labels=True,
           note="single panel; heavy-traffic speed collapses at p_exit 0.5 while light "
                "traffic is flat; NEVER CITED BY NUMBER")
    figure(51, 2, "bar", "Figure 32",
           none_mention(),
           [DISCUSS, RAMPEXTRA, PEXITUTIL], "other", panels=2, layout="1x2",
           legend="inside", labels=True,
           note="(a) lane utilisation ratio in light traffic and (b) in heavy traffic "
                "against p_exit, three lanes per category; label precision is inconsistent "
                "('0.06' and '0.05' beside three-decimal values elsewhere); NEVER CITED BY "
                "NUMBER")
    figure(52, 1, "bar", "Figure 33 Failure ratio in light & heavy traffic (different pexit )",
           cited(52, 52, ["Figure 33"], 1,
                 "Figure 33 demonstrate that in the case of light traffic, pexit is an irrelevant factor."),
           [DISCUSS, RAMPEXTRA, PEXITFAIL], "other", legend="inside", labels=True,
           note="single panel, three p_exit categories with light and heavy paired; the y "
                "axis is drawn past 0.6 but its top tick is unlabelled")

    # ---- the refused second panels of the eighteen two-panel figures ----------
    second_panel(22, 2, 1, "Figure 6")
    second_panel(25, 2, 1, "Figure 8")
    second_panel(26, 2, 1, "Figure 10")
    second_panel(26, 4, 3, "Figure 11")
    second_panel(30, 1, 2, "Figure 16")
    second_panel(31, 2, 1, "Figure 17")
    second_panel(31, 4, 3, "Figure 18")
    second_panel(32, 2, 1, "Figure 19")
    second_panel(33, 2, 1, "Figure 20")
    second_panel(33, 4, 3, "Figure 21")
    second_panel(34, 2, 1, "Figure 22")
    second_panel(35, 2, 1, "Figure 23")
    second_panel(37, 2, 1, "Figure 24")
    second_panel(39, 2, 1, "Figure 26")
    second_panel(48, 1, 2, "Figure 27")
    second_panel(49, 2, 1, "Figure 28")
    second_panel(49, 3, 4, "Figure 29")
    second_panel(51, 3, 2, "Figure 32")

    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": ITEMS,
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": [
            "Every figure caption in the paper prints BELOW its artwork, including the two "
            "on pages 11 and 13 whose art fills the top of the page, while every table "
            "caption prints ABOVE its grid, so position never varies inside a family "
            "[caption.position]",
            "Nothing is punctuated: the numbering runs bare 'Figure N' and 'Table N' from "
            "the first to the last of the forty-five captured exhibits and 'FIGURE' never "
            "appears [caption.numbering]",
            "Eighteen of the thirty-three figures print one number and one caption over two "
            "side-by-side panels, so the paper shows fifty-one chart panels under "
            "thirty-three numbers and every second panel is refused as a fragment rather "
            "than counted twice [geometry.panel_count]",
            "The occupancy sweeps, Figures 6 to 15, are flat 2-D line plots in MATLAB "
            "default styling: one axes, no gridlines, no in-plot title and a boxed legend "
            "inside the upper right corner [geometry.family]",
            "Every comparison figure from 16 to 33 is a grouped bar chart in which light "
            "and heavy traffic are two adjacent bars inside ONE panel, never two panels, so "
            "the split-to-two-panels decision is made only by the (a)/(b) sub-captions and "
            "never by the two traffic regimes [geometry.panel_count]",
            "There is no 3-D, no surface and no perspective anywhere in the paper; the "
            "closest thing to a perspective drawing is Figure 4's flat flow chart "
            "[geometry.three_d]",
            "The bar panels from 16 to 23 and 27 to 33 print a numeric value above nearly "
            "every bar, which lets the reader recover the numbers, while the rule-comparison "
            "panels 24 to 26 print none at all [geometry.data_labels]",
            "Eleven of the thirty-three figures are never cited by number in the prose: 3, "
            "6, 10, 12, 13, 14, 15, 29, 30, 31 and 32 [mention.count]",
            "Five cited figures are named a page or two away from the art - Figure 4 is "
            "diagrammed on page 18 and cited on 19, Figure 11 drawn on 26 and cited on 27, "
            "Figure 18 drawn on 31 and cited on 32, Figure 21 drawn on 33 and cited on 34, "
            "and Figure 24 drawn on 37 but first named only as 'Figure 24(a)' on 39 - so "
            "those rows carry negative lead_pages [mention.lead_pages]",
            "The paper's first exhibit number is misapplied: the page-22 sentence that "
            "introduces the two time-space diagrams calls them '(Figure 8)', which is the "
            "flow-rate-of-each-lane figure printed three pages later, leaving Figure 6 with "
            "no named citation at all and giving Figure 8 a lead of three pages [mention.style]",
            "The two symbol tables are the only merged-cell tables in the paper, each "
            "carrying a single spanning group row - Constants on page 8, Variables on page 9 "
            "- over a second, ordinary header row [table.merged_cells]",
            "Two table constructions are in use: the six evaluated-rule and sensitivity "
            "tables on pages 40 to 44 keep one internal vertical rule between the stub and "
            "the first data column, while the four sensitivity tables on pages 45 and 46 "
            "carry horizontal rules only [table.rule_style]",
            "No table is shaded, no table is continued across a page break, and no table "
            "prints a note row; every grid is portrait and full measure [table.zebra]",
            "Cells wrap rather than abbreviate: rule names, 'sharp breaking frequency' and "
            "'std. deviation of speed' all break over two lines, and the percent stub of the "
            "sensitivity tables prints no header at all [table.header_rows]",
        ],
        "note": (
            "Family tally: bar 18, line 10, flowchart-or-schematic 4, photo-or-raster-image "
            "1, table-grid 12. The paper is a simulation report, so thirty-three exhibits "
            "are chart panels and only four are drawings. Declared gap, not a row: TABLE 3, "
            "'Characteristics of Vehicles' on page 16, is printed and captioned at y=290-300 "
            "with a booktabs grid under it holding four rows (Car 1 cell 6 cells/sec 60%, Bus "
            "2 cells 5 cells/sec 30%, Truck 2 cells 3 cells/sec 10%), but the detector "
            "returned no region for it - the page's only measured region is the Figure 3 "
            "raster below it - so the table is named here instead of being given an invented "
            "bbox. The paper therefore prints THIRTEEN tables and twelve are measured. Table "
            "3 prints its caption above its grid like every other table."
        ),
    }
    out = PROXY / "pc58-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
