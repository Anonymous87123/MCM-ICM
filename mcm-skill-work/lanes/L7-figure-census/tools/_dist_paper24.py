"""Hand pass for P-C-2011-11422-caf513f2 (electric cars, 20 pages).

This paper prints no captions at all: the text layer contains not one "Figure N" or
"Table N" token, the exhibits are introduced only as "the following table" or "are shown
below", and one chart carries its title baked into the image raster. So every exhibit is
recorded with `caption_source: none` (or `typed-from-crop` for that one) and an empty
verbatim caption, and `mention` carries the null form -- there is no numbering to resolve.

Families, read off cropped page proxies:

* p6 r1, p7 r1 - two versions of the coupled-differential-equation chart: three series
  (E_n red solid, G_n blue dotted, C(n) green dashed) with the key set outside the left
  edge of the axes; p7 raises the seeding proportion.
* p9 r1 - a screenshot of the cellular-automaton grid, blue cells on white, with the
  spreadsheet chrome still visible at the top: photo-or-raster-image.
* p9 r2 - the seeding chart printed inside the same raster, six colour series 5%-30%,
  key outside the right edge, and the title "Cellular Automata Model of Spreading of
  Electric Cars Based on Initial Seeding" set in the image.
* p10 r1 - a pie chart of the 2009 electricity mix, key outside the right edge.
* p15 r1/r3, p16 r1, p17 r1 - connect-the-dots cost charts against the alpha value.
* The measured tables are Word-style grids: full frame, a rule between every column, no
  row shading anywhere in the paper.

Usage: python -I tools/_dist_paper24.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2011-11422-caf513f2"
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

MICRO = "6 Microeconomic Model"
GLOBAL_ = "6.1 Global Influence Model"
LOCAL = "6.2 Localized Behavior"
CA = "6.2.1 Cellular automata"
MACRO = "7 Macroeconomic Model: Meeting the Energy"
ENERGY = "7.1 Current Energy Source and Demand"
POLL = "7.2 Current Pollution rates"
COST = "7.4 Quantizing Cost"
ALPHA = "7.7 Using Alpha to Determine Cost, and Vice Versa"
EXAMPLE = "7.8 Example Calculation"
SAVED = "7.9 Fossil Fuels Saved"
MESH = "8 Meshing the Micro and Macro Models"

KIND_OF = {GLOBAL_: "model", CA: "model", ENERGY: "other", POLL: "other",
           COST: "model", ALPHA: "solution", EXAMPLE: "solution",
           SAVED: "result", MESH: "result"}

PATH: dict[tuple[int, int], list[str]] = {
    (6, 1): [MICRO, GLOBAL_],
    (7, 1): [MICRO, GLOBAL_],
    (7, 2): [MICRO, GLOBAL_],
    (9, 1): [MICRO, LOCAL, CA],
    (9, 2): [MICRO, LOCAL, CA],
    (10, 1): [MACRO, ENERGY],
    (11, 1): [MACRO, POLL],
    (11, 2): [MACRO, POLL],
    (13, 1): [MACRO, COST],
    (15, 1): [MACRO, ALPHA],
    (15, 3): [MACRO, ALPHA],
    (16, 1): [MACRO, EXAMPLE],
    (17, 1): [MACRO, SAVED],
    (18, 1): [MESH], (18, 2): [MESH], (18, 3): [MESH],
    (19, 1): [MESH], (19, 2): [MESH],
}

IN_IMAGE_TITLE = ("Cellular Automata Model of Spreading of Electric Cars Based on "
                  "Initial Seeding")

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []


def place(page: int, reg: int, order: int) -> dict:
    path = PATH[(page, reg)]
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": KIND_OF[path[-1]],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def no_mention() -> dict:
    """This paper numbers nothing, so there is no reference to resolve."""
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def caption_block(text: str, source: str) -> dict:
    return {
        "verbatim": text,
        "numbering": "none",
        "words": len(schema.words(text)) if text else 0,
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        # No caption means no side; the lane placeholder is "below", stated in the rules.
        "position": "below",
    }


def figure(page: int, reg: int, family: str, *, legend: str = "none",
           title: str = "", other_note: str = "", note: str = "") -> None:
    ORDER.append((page, reg))
    source = "typed-from-crop" if title else "none"
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": title,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": no_mention(),
        "caption": caption_block(title, source),
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": True,
            "data_labels": False,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, rows: int, cols: int, *, numeric: int = 0,
          text_cols: int = 1, units: bool = False, width: str = "full",
          note: str = "") -> None:
    ORDER.append((page, reg))
    TABLES[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": "",
        "caption_source": "none",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": no_mention(),
        "caption": caption_block("", "none"),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": 1,
            "rule_style": "vertical-rules",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": units,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": width,
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    }


def build() -> str:
    figure(6, 1, "line", legend="outside-left",
           note="three coupled series over t_n; the keys E_n, G_n and C(n) sit left of the "
                "frame and the x axis is labelled t_n, no axis title on y")
    figure(7, 1, "line", legend="outside-left",
           note="the same three series with a larger seeding proportion: C(n) climbs past "
                "G_n before t_n = 70")
    table(7, 2, 8, 3, numeric=2, text_cols=1,
          note="seed proportion, seeding cost and E in 2060, seven seeding levels")
    figure(9, 1, "photo-or-raster-image",
           note="screenshot of the cellular-automaton grid with the viewer chrome still "
                "visible at the top; the ink is a raster image, not paths")
    figure(9, 2, "line", legend="outside-right", title=IN_IMAGE_TITLE,
           note="six series (5% to 30% seeding) rising to 2060, title and key both baked "
                "into the image raster; y axis 'Percentage of Total Cars the are Electric'")
    figure(10, 1, "other", legend="outside-right",
           other_note="pie chart of the 2009 electricity mix; the family vocabulary has no "
                      "pie class and a pie is neither bars nor a line, so it is recorded as "
                      "other rather than forced into bar",
           note="five sectors (Petroleum, Natural Gas, Coal, Renewable Energy, Nuclear "
                "Energy) with the key right of the circle")
    table(11, 1, 7, 4, numeric=3,
          note="pounds per mile by pollutant for the electric and gasoline car plus the "
                "difference; six pollutants")
    table(11, 2, 7, 2, numeric=1,
          note="pounds saved per year by pollutant, each row an algebraic expression in "
                "E and C(t) rather than a number")
    table(13, 1, 6, 4, numeric=3,
          note="current production, maximum production and current cost per QBTU for the "
                "five power sources")
    figure(15, 1, "line", legend="outside-right",
           note="six colour series against the alpha value, square and diamond markers "
                "joined by thin lines, y axis 'Quadrillion BTUs'")
    excluded(15, 2, "fragment-of-other",
             "legend box of the p15 multi-series chart; it sits beyond the right edge of the "
             "axes and the extractor measured it as its own region")
    figure(15, 3, "line",
           note="one series: total cost against the alpha value, y axis 'Cost ($)'; the "
                "curve is a flat run, one step, then a straight rise")
    figure(16, 1, "line",
           note="one series of cost against alpha with a red annotation arrow marking the "
                "worked example at alpha = 37500; no legend and no gridlines")
    figure(17, 1, "line", legend="inside",
           note="five series (Petroleum, Natural Gas, Coal, Renewable, Nuclear) in "
                "quadrillion BTUs against alpha, key boxed inside the bottom-right corner, "
                "dashed horizontal gridlines")
    table(18, 1, 8, 4, numeric=3,
          note="costs at alpha = 0; the 'If α = 0' line above the grid is a condition, not "
                "a caption")
    table(18, 2, 8, 4, numeric=3,
          note="costs at alpha = 50,000; the condition line above the grid is 'If α = "
                "50, 000:'")
    table(18, 3, 8, 4, numeric=3,
          note="costs at alpha = 200,000; the condition line above the grid is 'If α = "
                "200, 000:'")
    table(19, 1, 8, 4, numeric=3,
          note="the alpha = 500,000 block, continuing on the next page with no repeated "
                "condition line")
    table(19, 2, 6, 2, numeric=1,
          note="the fuel mix for a 10% seed at alpha = 200,000, five energy sources")

    rules = [
        "This paper numbers no exhibit: the text layer has no Figure or Table token and the "
        "prose says only 'the following table' or 'are shown below', so every item carries "
        "caption_source none and the null mention form [caption.numbering].",
        "One chart has its title set inside the image instead of in the text layer, so that "
        "one item is typed-from-crop rather than none [caption.verbatim].",
        "A captionless exhibit has no side; position is recorded as below as the lane "
        "placeholder so the field keeps a legal value [caption.position].",
        "Family follows the ink: connect-the-dots cost curves, the two coupled-equation "
        "charts and the six-series seeding chart are line; the cellular-automaton page is a "
        "screenshot, so photo-or-raster-image [geometry.family].",
        "The pie chart of the 2009 electricity mix is recorded as other with an explicit "
        "other_note, because the vocabulary has no pie class and calling it bar would "
        "misdescribe the ink [geometry.family].",
        "Legend placement is read off the frame: the two coupled-equation charts put their "
        "keys left of the axes, the seeding chart and the pie right of them, and the p17 "
        "chart boxes its key inside the bottom-right corner [geometry.legend].",
        "Every measured table is the same Word-style grid: full outer frame with a rule "
        "between every column, so rule_style is vertical-rules for all nine "
        "[table.rule_style].",
        "No table in this paper shades its rows, and none merges cells; the condition lines "
        "above the three cost tables are read as conditions, not as header rows "
        "[table.zebra].",
        "Two measured regions belong to one exhibit on p15: the chart frame and the legend "
        "box beside it, so the legend is excluded as a fragment of the chart rather than "
        "counted as a second figure [place.page_order].",
    ]
    note = (
        "Two exhibits are declared in prose and never measured: the 'Proportion of Seeds / E "
        "in 2060' table printed at the top of p18 and the seeding-cost table block at "
        "alpha = 500,000 continues from p18 onto p19, where only the p19 half is measured. "
        "The pie chart is recorded as other because the family vocabulary has no pie class. "
        "Table counts are counted from the crops, so the p18 blocks start below their 'If α = "
        "...' condition line."
    )
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": [TABLES[k] for k in ORDER if k in TABLES],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": note,
    }
    out = PROXY / "pc24-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, "
          f"{len(payload['tables'])} tables, {len(payload['excluded_regions'])} excluded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
