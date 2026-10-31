"""Hand pass for P-B-2012-13074-8fc549d2 (Big Long River scheduling, 22 pp).

The geometry pass measures 18 regions over 14 pages. The paper numbers every exhibit
`Chart1` … `Chart15` — no space, no period — so the context dump found no captions and no
mentions at all, and the printed label had to be read off the crops and quoted from the
text layer by hand. `schema.NUMBERINGS` has no "Chart N" value, so every row here carries
`numbering: "none"` and the printed label survives in `caption.verbatim`.

Accounting: 4 figure items + 11 counted tables + 3 excluded continuations = 18, nothing
else measured, nothing unaccounted. Fifteen printed labels attach to fifteen counted
exhibits, one label each:

    Chart1  p2-r1   printed table, the 26 trip types by propulsion and duration
    Chart2  p4-r1   flowchart, the three-branch schedule method
    Chart3  p6-r1   schedule grid, Y=425, six-day cycle
    Chart4  p7-r1   skeleton orbit of trip type 3, a marked axis
    Chart5  p7-r2   skeleton orbit of type i, the same axis generalised
    Chart6  p8-r1   schedule grid for one campsite set of two trip types
    Chart7  p9-r1   the first two days' schedule, trip type against route code
    Chart8  p10-r1  schedule grid for one campsite set of three trip types
    Chart9  p11-r1  flowchart, the Part 2 model in five boxes
    Chart10 p15-r1  the whole Y=150 schedule, one calendar in four measured bands
    Chart11 p17-r1  carrying capacity over eight runs
    Chart12 p17-r2  trip-type counts and percentages, the paper's only boxed table
    Chart13 p18-r1  carrying capacity against the first trip type, three column pairs
    Chart14 p18-r2  carrying capacity against trip hours per day
    Chart15 p18-r3  carrying capacity against the small-probability threshold

Chart10 is printed as one calendar from 1 March to 31 August across pp. 12-15. The caption
sits under the last band (p15), the Sun.-Sat. header under the first (p12), so the table is
counted once on its caption-bearing band and the three earlier bands are excluded
`split-across-pages` rather than counted three more times.

Families, read off cropped page proxies:

* `flowchart-or-schematic` is the p4 decision tree (Judge Y >= 306, then boxed boxes joined
  by Method / develop arrows), the p11 five-box pipeline, and the two p7 marked axes — a
  number line with filled dots at Start, 1, 26, 51, … and formula labels above the dots.
  The axes plot no data: they show the campsite positions that make up an orbit, so they
  are schematics, not `line` charts.
* `table-grid` is the other eleven counted exhibits. Nine are grids of route strings
  (`Start -> 3 -> 6 -> … -> End`) or trip codes in boxed cells; Chart1 and Charts 11-15 are
  ordinary numeric tables. The paper prints no zebra shading anywhere.

Usage: python -I tools/_dist_paper33.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2012-13074-8fc549d2"
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


def cline(page: int, start: str, stop: str | None = None) -> str:
    """The printed caption as the text layer carries it, cut at `start`..`stop`."""
    raw = (LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
           / f"page-{page:04d}.txt").read_text(encoding="utf-8", errors="replace")
    for line in raw.splitlines():
        line = schema.norm(line)
        if start not in line:
            continue
        cut = line[line.index(start):]
        if stop and stop in cut:
            cut = cut[: cut.index(stop)]
        return cut.strip()
    raise KeyError((page, start))


PATH = {
    2: ["2 Definitions"],
    4: ["5.2 Development of the model"],
    6: ["5.2 Development of the model",
        "5.2.1 Every campsite set for every single trip type"],
    7: ["5.2 Development of the model",
        "5.2.2 Every campsite set for every multiple trip types"],
    8: ["5.2 Development of the model",
        "5.2.2 Every campsite set for every multiple trip types"],
    9: ["5.2 Development of the model",
        "5.2.2 Every campsite set for every multiple trip types"],
    10: ["5.2 Development of the model",
         "5.2.3 One campsite set for all trip types"],
    11: ["6.1 Method", "6.1.2 Key ideas"],
    12: ["6.2 Development of the model", "6.2.2 Best schedule using Greedy algorithm"],
    13: ["6.2 Development of the model", "6.2.2 Best schedule using Greedy algorithm"],
    14: ["6.2 Development of the model", "6.2.2 Best schedule using Greedy algorithm"],
    15: ["6.2 Development of the model", "6.2.2 Best schedule using Greedy algorithm"],
    17: ["8 Testing of the model----Sensitivity analysis"],
    18: ["8 Testing of the model----Sensitivity analysis",
         "8.1 Stability with varying trip types chosen in 6"],
}

PATH[19] = PATH[18] + ["8.1 Stability with varying trip types chosen in 6"]
PATH[20] = PATH[18] + ["8.2 The sensitivity analysis of the assumption 4\u2463"]
PATH[21] = PATH[18] + ["8.3 The sensitivity analysis of the assumption 4\u2465"]

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic across the
# excluded bands that carry no payload entry of their own
VENTION = {2: 1, 4: 1, 6: 1, 7: 2, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1,
           15: 1, 17: 2, 19: 3}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def place(page: int, reg: int, path: list[str] | None = None) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route = path or PATH[page]
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


def caption_block(text: str, position: str = "below") -> dict:
    return {
        "verbatim": text,
        "numbering": "none",
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


def figure(page: int, reg: int, family: str, caption: str = "", *,
           panels: int = 1, layout: str = "1", legend: str = "none",
           numbers: bool = False, labels: bool = False,
           mention: dict | None = None, note: str = "",
           path: list[str] | None = None, position: str = "below") -> None:
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
        "caption_source": "text-layer" if caption else "none",
        "note": note,
        "place": place(page, reg, path),
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
          text_cols: int = 1, width: str = "full", continued: bool = False,
          note: str = "", mention: dict | None = None,
          path: list[str] | None = None, position: str = "below") -> None:
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
        "place": place(page, reg, path),
        "mention": blocking,
        "caption": caption_block(caption, position),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rule_style, "zebra": False, "merged_cells": False,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": width, "orientation": "portrait",
            "continued": continued, "note_sentence": "",
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


def build() -> str:
    # 2 Definitions - the trip-type numbering table
    table(2, 1, cline(2, "Chart1", "(6)"),
          rows=2, cols=14, rule_style="booktabs", numeric_cols=13, text_cols=1,
          mention=mention(2, ["chart"],
                          "(5) For better description we assign a natural number to every"
                          " trip type, from 1 to 26, as shown in the following chart.",
                          "as-shown-in"),
          note="Two rows against thirteen numbered columns plus the propulsion label: "
               "Oar-powered holds the odd durations 1-25, Motorized the even 2-26, and the "
               "header row prints only 6-18 because the first five cells sit empty. Three "
               "horizontal rules, no vertical rules.")

    # 5.2 - the method decision tree
    figure(4, 1, "flowchart-or-schematic", cline(4, "Chart2", "Note for"),
           layout="3 columns", labels=True,
           mention=mention(4, ["chart below"],
                           "As we can see from the chart below, the distance between two"
                           " adjacent campsites in", "as-shown-in"),
           note="Decision tree of the whole schedule method: a 'Judge Y >= 306' box splits "
                "into Yes / No, the Yes branch runs three stacked boxes joined by 'Method' "
                "arrows (1 campsite set - 1 trip type, Divide into separate campsite set, "
                "Best schedule for a certain campsite set, Arrange campsite sets), the No "
                "branch runs 1 campsite set - multiple trip types down through 2 and 3 trip "
                "types to 'same propulsion' and across to Allocation of 13 groups, Best "
                "schedule for a certain campsite set and Arrange campsite sets. Boxed "
                "boxes, plain arrows, no shading.")

    # 5.2.1 - the Y=425 schedule
    table(6, 1, cline(6, "Chart3", "(\u2172)"),
          rows=6, cols=14, rule_style="vertical-rules", text_cols=14, continued=True,
          mention=mention(6, ["chart3"], "As shown above in chart3", "as-shown-in"),
          note="Schedule grid: a 'Day' column against the campsite numbers 1-13 with a "
               "trailing ellipsis, each cell holding the three routes of one day "
               "('Start -> 3 -> 6 -> 9 -> 12 -> 15 -> 16 -> End'). Days 1-6 are the printed "
               "six-day cycle, separated by a thick rule and bracketed '6 Days / 16 Trips'; "
               "the band also holds the first three route rows of day 7 below the bracket, "
               "and the day column ends in a vertical ellipsis. Vertical rules and a boxed "
               "frame, no zebra.")

    # 5.2.2 - the two skeleton orbits
    figure(7, 1, "flowchart-or-schematic", cline(7, "Chart4", "Since"),
           numbers=True, labels=True,
           mention=mention(7, ["chart"],
                           "Apparently the following six campsites constitute the skeleton"
                           " orbit of trip type 3, as shown in the chart", "as-shown-in"),
           note="A single horizontal number line drawn with a thick black rule: filled "
                "dots at Start, 1, 26, 51 and the two closing formulas "
                "25(|Y/25|-1)+1 and 25|Y/25|+1, an ellipsis in the middle and Y / End at the "
                "right. No axes, no plotted data - it is a schematic of which campsites form "
                "the orbit of trip type 3.")
    figure(7, 2, "flowchart-or-schematic", cline(7, "Chart5"),
           numbers=True, labels=True,
           mention=mention(7, ["chart"],
                           "the skeleton orbit of type i, as shown in chart:", "as-shown-in"),
           note="The same number line generalised to trip type i: black dots at Start, at "
                "each 7|Y/7| block boundary and at End, blue triangles between them, and the "
                "two formulas (k|Y/7|)/7 and (k|Y/7|)/7+1 printed above every block. "
                "Schematic, not a plot; the caption line sits just under the axis and the "
                "band clips its top at the prose line above.")

    # 5.2.2 - the two-trip-type schedule
    table(8, 1, cline(8, "Chart6", "As one can see"),
          rows=6, cols=17, rule_style="vertical-rules", text_cols=17, continued=True,
          note="Same grid form as Chart3 for one campsite set shared by two trip types: a "
               "'Day' column against campsites 0-15 plus ellipsis, three routes per day, "
               "the six-day cycle bracketed '6 Days / 15 Trips', days 7 and 8 continuing "
               "under the bracket inside the band and a vertical ellipsis closing the day "
               "column. Vertical rules, boxed frame, no zebra.")

    # 5.2.2 - the two-day route table
    table(9, 1, cline(9, "Chart7", "In the chart above"),
          rows=26, cols=3, rule_style="boxed", text_cols=3,
          note="Route table for the first two days: the date column (1, 2) against trip "
               "type and the campsite route, e.g. 'O-7' -> '21, 42, 63, 84, 105, 126'. "
               "Twenty-six trip types, thirteen oar-powered then thirteen motorized, with "
               "the 'M-6' cell of each day carrying the printed day number 1 and 2 instead "
               "of a blank. Full boxed grid, no zebra. The paragraph under it decodes "
               "'I j-k' as count, propulsion and duration.")

    # 5.2.3 - the three-trip-type schedule
    table(10, 1, cline(10, "Chart8", "Then it is similar"),
          rows=8, cols=20, rule_style="vertical-rules", text_cols=20, continued=True,
          note="Same grid form again for one campsite set shared by three trip types: a "
               "'Day' column against campsites 0-18 plus ellipsis, three routes per day, "
               "the eight-day cycle bracketed '8 Days / 18 Trips', days 9 and 10 continuing "
               "under the bracket inside the band. Vertical rules, boxed frame, no zebra.")

    # 6.1.2 - the Part 2 pipeline
    figure(11, 1, "flowchart-or-schematic", cline(11, "Chart9"),
           layout="column of 5", labels=True,
           note="Five stacked boxes down the lower third of the page, each holding a short "
                "phrase (the three subparts of the Part 2 model: recursive probability, "
                "Jordan formula with the minimax stopping rule, and the X-trips-given case). "
                "Raster crop of plain boxed shapes, no arrows, no shading.")

    # 6.2.2 - the Y=150 calendar, four measured bands
    excluded(12, 1, "split-across-pages",
             "first band of Chart10: the Sun.-Sat. header row and the single week of "
             "1-3 March. The calendar continues on p13; the caption sits on p15.")
    excluded(13, 1, "split-across-pages",
             "second band of Chart10: nine week rows, 4 March to 5 May, printed without "
             "repeating the weekday header.")
    excluded(14, 1, "split-across-pages",
             "third band of Chart10: ten week rows, 6 May to 14 July, headerless, the "
             "bottom row clipped by the measured region.")
    table(15, 1, cline(15, "Chart10", "6.2.3"),
          rows=27, cols=7, rule_style="boxed", text_cols=7,
          note="The whole Y=150 schedule as one month calendar: seven weekday columns and "
               "twenty-seven week rows from 1 March to 31 August, each cell holding the "
               "day's trips ('3 M-6s', '1 O-8', '1 O-8'), month names printed in the first "
               "cell of each month's opening week and the day numbers above the trip cells. "
               "The measured band is the fourth of four and holds the 15 July - 31 August "
               "rows; its header row is the Sun.-Sat. line printed on p12, and the three "
               "earlier bands are excluded as split-across-pages. Full boxed grid, no zebra. "
               "The prose that introduces it ('The whole schedule is shown as the following "
               "chart:') stands on p12, three pages before the caption, so no in-text "
               "mention is recorded.")

    # 8 - the sensitivity tables
    table(17, 1, cline(17, "Chart11", "Trip type i"),
          rows=1, cols=9, rule_style="booktabs", numeric_cols=8, text_cols=1,
          note="One body row: 'Run times' 1-8 against 'Carrying capacity' 482, 486, 493, "
               "493, 476, 474, 485, 475. Horizontal rules only.")
    table(17, 2, cline(17, "Chart12", "Comparing with the results"),
          rows=27, cols=4, rule_style="boxed", numeric_cols=2, text_cols=2,
          note="Trip-type census: label column (the trip type, with merged 'Oar-powered' / "
               "'Motorized' group cells beside it), 'The number of trip type i' and 'The "
               "percentage of trip type i', twenty-six types plus three Total rows "
               "(2616 / 67.7%, 1248 / 32.3%, 3864). The only fully boxed sensitivity table.")

    # 8.1-8.3 - one table per subsection, each on its own path
    table(18, 1, cline(18, "Chart13", "From the data"),
          rows=8, cols=6, header_rows=2, rule_style="booktabs", numeric_cols=3,
          text_cols=3, path=PATH[19],
          note="Three side-by-side column pairs, each headed 'The first trip type / "
               "Carrying capacity' over two header rows: the 24 allowed first-trip types "
               "with their schedule size, eight rows per pair. Horizontal rules only.")
    table(18, 2, cline(18, "Chart14", "8.3 The sensitivity"),
          rows=1, cols=6, rule_style="booktabs", numeric_cols=5, text_cols=1, path=PATH[20],
          note="One body row: 'Trip hour per day' 7, 7.5, 8, 8.5, 9 against 'Carrying "
               "capacity' 454, 484, 560, 483, 488. Horizontal rules only.")
    table(18, 3, cline(18, "Chart15", "9 Evaluation"),
          rows=1, cols=4, rule_style="booktabs", numeric_cols=3, text_cols=1, path=PATH[21],
          note="One body row: 'Small probability' 0.01, 0.025, 0.05 against 'Carrying "
               "capacity' 215, 376, 500 - the 0.05 column is the threshold the whole paper "
               "assumes. Horizontal rules only.")

    rules = [
        "Every exhibit in this paper is numbered \"ChartN\" with no space and no period, so "
        "the caption finder saw zero captions and zero mentions; each label was read off "
        "the crop and quoted from the text layer [caption.verbatim].",
        "schema.NUMBERINGS carries no \"Chart N\" value, so all fifteen rows set "
        "numbering to \"none\" and the printed label survives only in the quote "
        "[caption.numbering].",
        "The caption prints under the drawing for fourteen exhibits and over it for none, "
        "except Chart2 whose caption line sits under the tree and Chart10 whose caption sits "
        "under the last of its four bands [caption.position].",
        "Chart10 is one calendar printed across pp. 12-15; the Sun.-Sat. header is on p12 "
        "and the caption on p15, so it is counted once on the caption-bearing p15 band with "
        "header_rows 1 standing for the header three pages above, and the three earlier "
        "bands are excluded split-across-pages [table.header_rows].",
        "The schedule grids of Charts 3, 6 and 8 are boxed with vertical rules and print an "
        "ellipsis in both directions, so rows and cols count the labelled rows and columns "
        "only [table.rows] [table.cols].",
        "Charts 3, 6 and 8 continue past the bracketed cycle inside the measured band, and "
        "their day column ends in an ellipsis, so continued is set for all three "
        "[table.continued].",
        "The two p7 skeleton orbits are marked axes with formula labels, not plots, so they "
        "are flowchart-or-schematic rather than line [geometry.family].",
        "Charts 11-15 are booktabs-style numeric tables with horizontal rules only; Chart12 "
        "is the single boxed one [table.rule_style].",
        "Chart13 is three column pairs under a two-row header, hence cols 6 and "
        "header_rows 2 [table.header_rows].",
        "No exhibit in the paper carries zebra shading, a legend or a colour bar "
        "[table.zebra] [geometry.legend].",
        "Section paths follow printed use: Chart7 is read by the paragraph under it inside "
        "5.2.2, and Charts 13-15 belong to 8.1, 8.2 and 8.3 respectively "
        "[place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-13074-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Eighteen measured regions, eighteen accounted: four figure items, eleven "
            "counted tables, three excluded continuations of Chart10. Fifteen printed "
            "\"ChartN\" labels attach one-to-one to the fifteen counted exhibits, and the "
            "paper prints no other exhibit, so the count is region level and label level at "
            "once. Charts 1, 3, 6, 7, 8 and 10 are grids of route strings rather than "
            "numbers, and Charts 3, 6, 8 and 10 are single exhibits whose bodies run past "
            "the measured band or across page turns. Chart12 is the only boxed sensitivity "
            "table; Charts 11, 13, 14 and 15 use horizontal rules only. Nothing measured "
            "was left unaccounted and no region needed inventing."
        ),
    }
    out = PROXY / "pb33-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
