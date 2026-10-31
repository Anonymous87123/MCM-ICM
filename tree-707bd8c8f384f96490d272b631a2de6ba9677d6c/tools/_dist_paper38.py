"""Hand pass for P-B-2012-15878-825774ea (cellular-automaton rafting, 23 pp).

The geometry pass measures 20 regions over 12 pages. Twelve are the paper's eight
printed figures - Figures 5 to 8 are each printed as a 3-D surface above its own
contour map, so the four of them occupy eight regions - and eight are the paper's six
printed tables, Table 6 being printed as three stacked grids under one caption:

    p4-r1   Table 1  model constants, Oar-Propelled against Motor Raft
    p8-r1   Table 2  static against dynamic scheduling strategies
    p9-r1   Figure 1 one-dimensional river array with four visitors
    p11-r1  Figure 2 simulation loop, Queue to Perform Calculations
    p11-r2  Figure 3 decision-flow implementation of the loop
    p12-r1  Table 3  implementations A to G
    p13-r1  Figure 4 constant-velocity banner, boats and downstream arrows
    p14-r1  Table 4  first experiment, four implementations by five metrics
    p14-r2  Table 5  second experiment, unidirectional bumping
    p15-r1  Figure 5  surface, average boat interactions per person
    p15-r2  Figure 5  contour of the same field
    p16-r1  Figure 6  surface, percentage of visitors rejected
    p16-r2  Figure 6  contour of the same field
    p17-r1  Figure 7  surface, percentage off schedule
    p17-r2  Figure 7  contour of the same field
    p18-r1  Figure 8  surface, visitors accommodated per season
    p18-r2  Figure 8  contour of the same field
    p19-r1  Table 6  environmental degradation, number of visitors
    p19-r2  Table 6  the same degradation sweep, percentage off schedule
    p19-r3  Table 6  the same degradation sweep, percentage rejected

Accounting: 12 figure items + 8 counted tables = 20 regions, unaccounted 0.

Families, read off cropped page proxies:

* `flowchart-or-schematic` is Figures 1 to 4: a ten-cell river strip with four named
  visitors and a "Downstream" arrow, the five-box simulation loop with its return
  arrow, the decision diamond of the concrete implementation, and the banner of
  cartoon boats over photo-textured water with two equal downstream arrows (paper 35's
  raster schematic is the same call). None of the four has axes, ticks or a legend.
* `surface-or-3D` is the upper panel of Figures 5 to 8: a perspective wireframe mesh
  over a coloured base plane, a vertical response axis, printed tick numbers on all
  three axes and a vertical colour bar at the right edge.
* `heatmap-or-contour` is the lower panel of the same four figures: the identical field
  drawn flat as coloured iso-lines on a Lambda-by-Y plane, with a boxed swatch key at
  the upper right instead of a colour bar.
* `table-grid` is all six printed tables, including Table 6's three stacked grids.

Captions are quoted from the text layer and cut at an explicit stop, named in each item
note, because the caption line is followed on the same page by ordinary prose.

Usage: python -I tools/_dist_paper38.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2012-15878-825774ea"
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

ASSUME = "3 Our Assumptions"
DYN = "6.2 The Dynamic Strategy"
MODEL = "7 The Model: A Cellular Automaton-like Strategy"
RULES = "7.2 Governing Rules for the Model"
IDEAL = "7.3 An Ideal Implementation of the Model"
CONTROL = "7.4 Control Implementations"
METRICS = "8 Clarifying the Metrics"
RESULTS = "9 Results"
INTER = "9.1 Number of Interactions"
REJECT = "9.2 Number of Visitor Rejections"
OFFSCHED = "9.3 Off-Schedule Completions"
CAPACITY = "9.4 Carrying Capacity"
DEGRADE = "10.1 Environmental Degradation"

# Figure 2 is the generalised rule set, so it is filed under 7.2 even though the 7.3
# heading prints above it; Table 3 is the control-implementation summary and is filed
# under 7.4 although the heading of section 8 sits lower on the same page.
PATH = {
    4: [ASSUME],
    8: [DYN],
    9: [MODEL],
    11: [MODEL, RULES],
    12: [MODEL, CONTROL],
    13: [METRICS],
    14: [RESULTS],
    15: [RESULTS, INTER],
    16: [RESULTS, REJECT],
    17: [RESULTS, OFFSCHED],
    18: [RESULTS, CAPACITY],
    19: [DEGRADE],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic
VENTION = {4: 1, 8: 1, 9: 1, 11: 2, 12: 1, 13: 1, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 3}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def ctext(page: int, start: str, stop: str) -> str:
    """The printed caption as the text layer carries it, cut at `start`..`stop`."""
    text = schema.page_text(PID, page)
    i = text.find(start)
    if i < 0:
        raise KeyError((page, start))
    cut = text[i:]
    j = cut.find(stop)
    if j < 0:
        raise KeyError((page, stop))
    return cut[:j].strip()


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


def caption_block(text: str, numbering: str, position: str = "below") -> dict:
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


def figure(page: int, reg: int, family: str, caption: str, *, legend: str = "none",
           colorbar: bool = False, three_d: str = "no", numbers: bool = False,
           labels: bool = False, position: str = "below",
           mention: dict | None = None, note: str = "") -> None:
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
        "panel_count": 1,
        "caption_verbatim": caption,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption, "Figure N:", position),
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, caption: str, *, rows: int, cols: int,
          header_rows: int = 1, rule_style: str = "boxed", numeric_cols: int = 0,
          text_cols: int = 1, merged: bool = False,
          mention: dict | None = None, note: str = "") -> None:
    ORDER.append((page, reg))
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
        "caption": caption_block(caption, "Table N:"),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rule_style, "zebra": False, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "column", "orientation": "portrait",
            "continued": False, "note_sentence": "",
        },
    })


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": None}


SURFACE = ("Three axes with printed tick numbers - Lambda and Y across the base and the "
           "response variable up the side - a perspective wireframe mesh drawn over a "
           "coloured base plane, and a vertical colour bar at the right edge.")
CONTOUR = ("The same field drawn flat: coloured iso-value lines on a plain Lambda-by-Y "
           "grid with both axis tick numbers printed, no vertical axis, and a boxed "
           "colour-swatch key at the upper right in place of a colour bar.")

T1_MENTION = mention(10, ["Table 1"],
                     "the moving constraints of the visitor (as defined in Table 1)",
                     "parenthetical")
T45_MENTION = mention(14, ["Tables 4 and 5"],
                      "From examining the results in Tables 4 and 5, we note the following:",
                      "direct")


def build() -> str:
    # 3 - the constants grid, cited six pages later from 7.1
    table(4, 1, ctext(4, "Table 1:", "\u2022 While rafting"), rows=4, cols=3,
          numeric_cols=2, text_cols=1, mention=T1_MENTION,
          note="Header is a blank stub over 'Oar-Propelled Raft' and 'Motor Raft'; the "
               "three body rows are Minimum Velocity 3 mph / 3 mph, Maximum Velocity "
               "5 mph / 10 mph and Duration of Rafting 4 - 8 hours / 4 - 8 hours, so the "
               "units sit inside the cells rather than in the header. Boxed, with a rule "
               "between every row and every column. The only running-text citation is on "
               "p10, six pages after the grid, which is why the mention lead_pages is "
               "negative.")

    # 6.2 - the static against dynamic comparison
    table(8, 1, ctext(8, "Table 2:", "While the static model offers"), rows=6, cols=3,
          rule_style="booktabs", text_cols=3,
          note="Blank stub over 'Static Model' and 'Dynamic Model'; five body rows - "
               "Types of Trips Offered, Frequency of Offered Trips, Maximum Possible "
               "Visitors, Chance of Conflict, Chance of Early or Late Completions - all "
               "carrying words, no numbers at all. Only a rule under the header and a "
               "rule between the stub and the two data columns; no box and no rule "
               "between body rows, so this is the one table in the paper that is not "
               "framed.")

    # 7 - the river array diagram
    figure(9, 1, "flowchart-or-schematic",
           ctext(9, "Figure 1:", "Each cell represents"),
           labels=True,
           note="One horizontal strip of ten contiguous cells numbered (1) to (10) under "
                "the strip, with a single arrow below it labelled 'Downstream'. Cells 2, "
                "5, 9 and 10 hold the four named visitors, each with its own type and "
                "trip length: 'Visitor (Rover, 12 Day)', 'Visitor (Motor, 8 Day)', "
                "'Visitor (Motor, 13 Day)', 'Visitor (Rover, 17 Day)'. Drawn line art, no "
                "axes, no ticks, no legend. Caption stops before the body prose that "
                "explains the cells.")

    # 7.2 - the generalised rule loop
    figure(11, 1, "flowchart-or-schematic",
           ctext(11, "Figure 2:", "Note that both the Moving"),
           labels=True,
           note="Five shaded process boxes chained left to right - Queue, Load River, "
                "Move Tourists, Resolve Conflicts, Perform Calculations - with a return "
                "arrow under the chain back into Queue, the first arrow annotated "
                "'Pois(\u03bb)', and 'Iterate for 180 Days' printed under the return path. "
                "No axes, no ticks, no legend. Filed under 7.2 Governing Rules because "
                "it draws the generalised rules; the 7.3 heading prints above the box but "
                "below this figure.")

    # 7.3 - the concrete implementation flow
    figure(11, 2, "flowchart-or-schematic",
           ctext(11, "Figure 3:", "In this particular implementation"),
           labels=True,
           note="Six process boxes and one decision diamond: 'Queue: Desired trip "
                "offered?' branches IF NO to 'Visitor Rejected' and IF YES down to Load "
                "River, Move Visitors: y*, Resolve Conflicts (If \u03b2A > \u03b2B Bump "
                "B) and Evaluate Visitors; IF YES returns to 'Populate Reservoir of "
                "Completed Visitors', IF NO drops to 'Perform Calculations' and loops back "
                "to the decision. The condition labels are printed red and green inside "
                "the frame, not in a key.")

    # 7.4 - the seven implementations
    table(12, 1, ctext(12, "Table 3:", "Since our model allows"), rows=8, cols=4,
          text_cols=4,
          note="Header 'Implementation | y* recalculated? | Initial Bump Direction | "
               "Unidirectional Bumping?' over the seven rows A (Ideal) through G (Exp. 2 "
               "Control). Every cell is a word - Yes, No, N/A, Random, Downstream, "
               "Upstream - so numeric_cols is 0. Boxed with full column rules.")

    # 8 - the constant-velocity banner
    figure(13, 1, "flowchart-or-schematic",
           ctext(13, "Figure 4:", "Thus, we need only consider"),
           labels=True, position="above",
           note="A raster banner: mottled photo-textured water with a cartoon rafter in a "
                "red boat at the left, a second cartoon in a wooden boat part way along, "
                "and two long rightward arrows of the same length showing equal "
                "displacement, i.e. constant velocity. No printed text anywhere in the "
                "region, no axes, no legend - the only encoding is the boat positions and "
                "the arrows, so it is a movement schematic rather than a photograph of "
                "data (the same call as paper 35's raster boat-placement schematic). Its "
                "caption is the one caption in this paper printed above its exhibit.")

    # 9 - the two experiment tables
    table(14, 1, ctext(14, "Table 4:", "We tested these implementations"),
          rows=5, cols=6, numeric_cols=5, text_cols=1, mention=T45_MENTION,
          note="Header 'Implementation | No. of Visitors | % Rejections | % Off Schedule "
               "| % Early | % Late' over four rows: A (Ideal), B (Constant y*), C (No "
               "Bump Rule) and D (Constant y*, No Bump Rule). Row labels wrap to two "
               "lines in the lower two rows. Boxed, one column of words and five of "
               "numbers; the percentage sign is in the header, the values are not.")
    table(14, 2, ctext(14, "Table 5:", "We tested these implementations"),
          rows=5, cols=5, numeric_cols=4, text_cols=1, mention=T45_MENTION,
          note="Header 'Implementation | No. of Visitors | % Rejections | Interactions "
               "per Visitor | % Off Schedule' over A (Ideal), E (Unidirectional "
               "Downstream Bumping), F (Unidirectional Upstream Bumping) and G "
               "(Unidirectional Random Bump). Boxed. Both experiment tables are cited "
               "together by the sentence after them, so the two rows share one mention.")

    # 9.1 to 9.4 - each figure as surface over contour
    figure(15, 1, "surface-or-3D",
           ctext(15, "Figure 5:", "Cellular Automaton Rafting Simulation"),
           legend="outside-right", colorbar=True, three_d="surface-mesh", numbers=True,
           note="Upper panel of Figure 5: the interaction count drawn as a perspective "
                "wireframe over a coloured base plane. Lambda 2 to 16 on one base axis, "
                "Y 50 to 250 on the other, Interactions 1 to 10 up the vertical, all "
                "three with tick numbers; colour bar at the right; in-plot title 'Avg "
                "Boat Interactions per Tourists'. " + SURFACE)
    figure(15, 2, "heatmap-or-contour",
           ctext(15, "Figure 5:", "Cellular Automaton Rafting Simulation"),
           legend="outside-right", numbers=True,
           note="Lower panel of the same figure: the identical interaction field as "
                "coloured iso-lines, Y 0 to 250 across and Lambda 1 to 15 up, in-plot "
                "title 'Avg. Boat Interactions Per Trip', and a legend box outside the "
                "plot on the right listing the 2 to 10 levels. " + CONTOUR)

    figure(16, 1, "surface-or-3D",
           ctext(16, "Figure 6:", "Cellular Automaton Rafting Simulation"),
           legend="outside-right", colorbar=True, three_d="surface-mesh", numbers=True,
           note="Upper panel of Figure 6: percentage rejected as a perspective wireframe. "
                "Y 0 to 250 on the front axis, Lambda 2 to 20 on the depth axis, % "
                "Rejections 0 to 90 up the vertical, all with tick numbers; colour bar "
                "at the right; in-plot title '% Rejected'. " + SURFACE)
    figure(16, 2, "heatmap-or-contour",
           ctext(16, "Figure 6:", "Cellular Automaton Rafting Simulation"),
           legend="outside-right", numbers=True,
           note="Lower panel: the same rejection field as coloured iso-lines on a "
                "Lambda-by-Y plane, title '% Rejected', and a legend box outside the plot "
                "listing the 5 to 90 levels. " + CONTOUR)

    figure(17, 1, "surface-or-3D",
           ctext(17, "Figure 7:", "We here consider"),
           legend="outside-right", colorbar=True, three_d="surface-mesh", numbers=True,
           note="Upper panel of Figure 7: the off-schedule percentage as a perspective "
                "wireframe. Y 50 to 250 on the front axis, Lambda 2 to 14 on the depth "
                "axis, % Off Schedule 0 to 60 up the vertical, all with tick numbers; "
                "colour bar at the right; the title '% Off Schedule' appears both above "
                "the surface and against the vertical axis. " + SURFACE)
    figure(17, 2, "heatmap-or-contour",
           ctext(17, "Figure 7:", "We here consider"),
           legend="outside-right", numbers=True,
           note="Lower panel: the same off-schedule field as coloured iso-lines, title "
                "'% Off-Schedule' (hyphenated here, two words above), and a legend box "
                "outside the plot headed '% Off Schedule' with levels from about 2 to 62. "
                + CONTOUR)

    figure(18, 1, "surface-or-3D",
           ctext(18, "Figure 8:", "Implementation A of our model is 1102"),
           legend="outside-right", colorbar=True, three_d="surface-mesh", numbers=True,
           note="Upper panel of Figure 8: visitors accommodated per season as a "
                "perspective wireframe. Lambda 2 to 14 on the front axis, Y 56 to 250 on "
                "the depth axis, 100 to 1000 up the vertical, all with tick numbers; "
                "colour bar at the right; in-plot title 'Tourists'. " + SURFACE)
    figure(18, 2, "heatmap-or-contour",
           ctext(18, "Figure 8:", "Implementation A of our model is 1102"),
           legend="outside-right", numbers=True,
           note="Lower panel: the same capacity field as coloured iso-lines, and a legend "
                "box outside the plot headed 'Tourists' with levels from about 200 to "
                "980. The in-plot title here reads 'Visitors' while the legend header "
                "reads 'Tourists' and the axis title reads 'Tourists'. " + CONTOUR)

    # 10.1 - one table printed as three stacked grids under one caption
    t6 = ctext(19, "Table 6:", "From these tables")
    table(19, 1, t6, rows=5, cols=5, numeric_cols=4, text_cols=1, merged=True,
          note="First of the three stacked grids that carry Table 6. Stub column headed "
               "'Number of Visitors' beside a header cell holding only the symbol "
               "'\u03bb' spanning the four value columns; the stub then reads \u03b1 = 0, "
               "10, 20 and 30, so the four columns are the \u03bb settings, although "
               "their individual \u03bb values are not printed anywhere in the grid. "
               "Boxed; the \u03b1 = 0 row runs 769, 910, 973 and 1071 across the four "
               "columns.")
    table(19, 2, t6, rows=5, cols=5, numeric_cols=4, text_cols=1, merged=True,
          note="Middle grid of Table 6: same five-by-five frame, stub '% Off Schedule', "
               "the same four-column '\u03bb' header cell and the same \u03b1 = 0, 10, "
               "20, 30 rows; entries 1.8 to 54. Boxed.")
    table(19, 3, t6, rows=5, cols=5, numeric_cols=4, text_cols=1, merged=True,
          note="Bottom grid of Table 6: stub '% Rejected Visitors', same frame and same "
               "\u03b1 rows; entries 0.5 to 75.1. The single caption is printed under "
               "this third grid and covers all three.")

    rules = [
        "Figures 5 to 8 are each printed as two measured regions - a 3-D surface above "
        "its own contour map - under one caption, so each figure is recorded twice, the "
        "upper row as surface-or-3D with three_d surface-mesh and a colour bar and the "
        "lower row as heatmap-or-contour with a swatch key instead [geometry.three_d] "
        "[geometry.colorbar].",
        "Figures 1 to 4 are drawn schematics with no axes, tick numbers or legend, so "
        "none of the four carries printed_numbers; Figure 4 is a raster banner whose only "
        "content is boat positions and two equal arrows, and it is recorded as "
        "flowchart-or-schematic on paper 35's raster-schematic precedent rather than as "
        "a photograph [geometry.printed_numbers] [geometry.family].",
        "Figure 4's caption is printed above the banner, the only such caption in this "
        "paper, so its caption position is above while every other exhibit is below "
        "[caption.position].",
        "Table 6 is one printed table laid out as three stacked grids (number of "
        "visitors, percentage off schedule, percentage rejected) sharing one caption, so "
        "it is recorded as three counted tables whose caption is the one printed line "
        "[table.rows] [table.merged_cells].",
        "Every column of Table 6 is a \u03bb setting whose \u03bb value is not printed; "
        "the header carries the symbol alone and the row factor is \u03b1, which is why "
        "the grid has a merged header cell and no complete column labels [table.merged_cells].",
        "Only two exhibits are named in running text at all: Table 1 is called back to "
        "from p10, six pages after the grid, so its mention lead_pages is negative, and "
        "Tables 4 and 5 are named together in the sentence that follows them on p14 "
        "[mention.lead_pages].",
        "Captions that are followed on the same page by ordinary prose are cut at a "
        "named stop: 'Each cell represents' for Figure 1, 'Note that both the Moving' "
        "for Figure 2, 'In this particular implementation' for Figure 3, 'Thus, we need "
        "only consider' for Figure 4, 'While the static model offers' for Table 2, "
        "'Since our model allows' for Table 3, 'We tested these implementations' for "
        "Tables 4 and 5, 'We here consider' for Figure 7, 'Implementation A of our model "
        "is 1102' for Figure 8 and 'From these tables' for Table 6 [caption.verbatim].",
        "Figure 2 draws the generalised rules and is filed under 7.2 even though the 7.3 "
        "heading prints above it, and Table 3 summarises the control implementations and "
        "is filed under 7.4 although the number of section 8 is printed lower on the same "
        "page [place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-15878-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twenty measured regions, twenty accounted: twelve figure rows for the "
            "paper's eight printed figures (Figures 5 to 8 are each a surface over a "
            "contour, so two rows apiece) and eight counted tables for six printed tables "
            "(Table 6 is three stacked grids under one caption). Both registers printed "
            "in this paper are measured in full - no printed exhibit is missing and no "
            "region is excluded. Declared gap: none. The three figures on p9, p11 and "
            "p13 are keyed as raster by the layout pass because each is a single image "
            "object, but Figures 1 to 3 are drawn line art that the paper embedded as "
            "pictures."
        ),
    }
    out = PROXY / "pb38-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
