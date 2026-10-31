"""Hand pass for P-B-2012-15420-8b46b980 (Big Long River schedules, 21 pp).

The geometry pass measures 10 regions over 10 pages. Eight are the paper's eight printed
figures; the other two are printed numeric grids the paper never numbers:

    p4-r1   inline vessel-type table (Motor / Non-Motor against 2010-2007)
    p5-r1   Figure 1  histogram of campsite spacings
    p7-r1   Figure 2  naive-model schedule grid, three steps
    p8-r1   Figure 3  priority-model schedule grid, three steps
    p11-r1  Figure 4  one density-perturbation schedule
    p12-r1  Figure 5  bone growth, four panels (Bones / Intermediate / Max / Final)
    p13-r1  Figure 6  bone growth with motor and oar trips
    p14-r1  model comparison table, 23 rows by 7 columns
    p15-r1  Figure 7  225-campsite schedule with its two histograms
    p16-r1  Figure 8  225-campsite schedule, Bones1 against Bones2

Accounting: 6 figure items + 3 composite items + 2 counted tables = 10 regions,
unaccounted 0.

Families, read off cropped page proxies:

* `histogram` is Figure 1: navy bins, axis titles "Frequency" and "Distance in Miles",
  in-plot title "Observed Distance Between Campsites Along 3 Rivers".
* `flowchart-or-schematic` is Figures 2 and 3: three side-by-side day-by-campsite grids
  labelled "step 1", "step 2", "step 3", the cells filled red, green and blue for the three
  trips. No axes, no tick numbers, no legend - colour is the only encoding (paper 34's
  strips are the same call).
* `line` is Figures 4 and 6: hundreds of overplotted trajectories, Day/Campsite and
  Night/Campsite axes, printed tick numbers, no legend.
* `composite-panel` is Figures 5, 7 and 8, each a single measured region holding several
  separately titled panels: 2x2 for Figure 5, and a wide "Schedule" panel over a
  "Histogram of Trip Lengths" and a "Histogram of Campsites Used" for Figures 7 and 8.

Captions are quoted from the text layer where the printed caption line runs on into the
paper's prose; the cut points are named in each item note.

Usage: python -I tools/_dist_paper37.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2012-15420-8b46b980"
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

ASSUME = "3 Assumptions"
MODELS = "4 Models"
NAIVE = "4.1 Naı̈ve model"
PRIOR = "4.2 Priority Model"
DENS = "4.3 Density Perturbation Algorithm"
BONE = "4.4 Bone Growth Model"
TESTS = "5 Testing and Results"
COMPARE = "5.1 Model Comparison"
BONERES = "5.3 Bone Growth Model Results"

PATH = {
    4: [ASSUME],
    5: [ASSUME, "3.4 Distribution and Approximate Number of Campsites"],
    7: [MODELS, NAIVE],
    8: [MODELS, PRIOR],
    11: [MODELS, DENS],
    12: [MODELS, BONE],
    13: [MODELS, BONE],
    14: [TESTS, COMPARE],
    15: [TESTS, BONERES],
    16: [TESTS, BONERES],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic
VENTION = {4: 1, 5: 1, 7: 1, 8: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def ctext(page: int, start: str, stop: str | None = None) -> str:
    """The printed caption as the text layer carries it, cut at `start`..`stop`."""
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


def caption_block(text: str, numbering: str = "Figure N:") -> dict:
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
        "position": "below",
    }


def figure(page: int, reg: int, family: str, caption: str, *, panels: int = 1,
           layout: str = "1", legend: str = "none", numbers: bool = True,
           labels: bool = False, mention: dict | None = None, note: str = "") -> None:
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
        "caption": caption_block(caption),
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
          text_cols: int = 1, merged: bool = False, caption_source: str = "text-layer",
          numbering: str = "none", note: str = "") -> None:
    ORDER.append((page, reg))
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": caption,
        "caption_source": caption_source,
        "note": note,
        "place": place(page, reg),
        "mention": dict(NULL_MENTION),
        "caption": caption_block(caption, numbering),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rule_style, "zebra": False, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "column", "orientation": "portrait",
            "continued": False, "note_sentence": "",
        },
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": None}


STEPS = ("Three day-by-campsite grids side by side, each with its own axes frame: a 'Day' "
         "label over the three columns, a rotated 'Campsite' label against the six rows and "
         "'step n' printed under each block. Filled cells are red, green and blue, one "
         "colour per trip; no tick numbers and no legend, so the numbers of days and "
         "campsites are only countable from the cells.")


def build() -> str:
    # 3.1 - the inline vessel table
    table(4, 1, "", rows=3, cols=5, rule_style="boxed", numeric_cols=4, text_cols=1,
          caption_source="none",
          note="Inline grid quoted in the assumptions, its own lead-in being 'The following "
               "table is the River Trip Statistics for the Colorado River for 2010, 2009, "
               "2008, and 2007': header 'Vessel Type 2010 2009 2008 2007' over the two rows "
               "Motor 415/409/426/425 and Non-Motor 183/183/184/181. Boxed, full rules, no "
               "caption line and no printed table number.")

    # 3.4 - the spacing histogram
    figure(5, 1, "histogram",
           ctext(5, "Figure 1:", "The campsite distribution is therefore assumed"),
           note="About fifteen contiguous navy bars, frequency against distance in miles, "
                "in-plot title 'Observed Distance Between Campsites Along 3 Rivers'; y axis "
                "'Frequency' 0-140, x axis 'Distance in Miles' 0-10. Heights collapse from "
                "about 126 in the first bin to near zero, which is the point the text uses "
                "to justify a uniform spacing. No legend.")

    # 4.1 and 4.2 - the two schedule step diagrams
    figure(7, 1, "flowchart-or-schematic",
           ctext(7, "Figure 2:", "If failure for all n then"),
           panels=3, layout="1x3", numbers=False, labels=True,
           note="Naive model, three steps: step 1 places a single red trip on the diagonal, "
                "step 2 adds the green trip and forces red off a cell, step 3 adds the blue "
                "trip. " + STEPS)
    figure(8, 1, "flowchart-or-schematic",
           ctext(8, "Figure 3:", "The Algorithm Input:"),
           panels=3, layout="1x3", numbers=False, labels=True,
           note="Priority model on the same three-step layout: the red trip keeps its top "
                "cell in every step, the green and blue trips fill below it, and the last "
                "step ends with the full staggering the naive model fails to reach. " + STEPS)

    # 4.3 - the density-perturbation schedule
    figure(11, 1, "line",
           ctext(11, "Figure 4:", "period with 200 campsites"),
           mention=mention(10, ["Figure 4"],
                           "Figure 4 shows one result from this algorithm.", "direct"),
           note="One density-perturbation schedule drawn as hundreds of overplotted coloured "
                "threads, each thread a trip, rising across Day 0-180 against Campsite "
                "0-200; axis titles 'Day' and 'Campsite', printed ticks on both, no legend. "
                "The caption (three sentences long) reports 1978 trips in 180 days with 200 "
                "campsites and no two trips on one campsite.")

    # 4.4 - the bone growth figures
    figure(12, 1, "composite-panel",
           ctext(12, "Figure 5:", "1. Start with an intial"),
           panels=4, layout="2x2", labels=True,
           mention=mention(12, ["Figure 5"],
                           "(See the lower two graphs in Figure 5).", "parenthetical"),
           note="Bone growth in a 2x2 panel grid titled 'Bones', 'Intermediate', 'Max' and "
                "'Final': thin flat-topped traces rising then saturating near campsite 150, "
                "each panel on Camp against Time with ticks 0-200 and 0-45. Panels one to "
                "three are blue, the final panel green; no legend. Caption stops before the "
                "algorithm's numbered step list that follows it.")
    figure(13, 1, "line",
           ctext(13, "Figure 6:", "This model can be extended"),
           mention=mention(13, ["Figure 6"],
                           "An example of this modification is shown in Figure 6.", "direct"),
           note="Bone growth with both trip types in one axes: dense blue swaths and thin "
                "magenta traces sawing across Night 0-60 against Campsite 0-160, in-plot "
                "title 'Bone Growth with Motors and Oars'. Blue is motor, purple is oar, and "
                "the caption says so because there is no legend.")
    # 5.1 - the comparison table
    table(14, 1, "", rows=23, cols=7, rule_style="boxed", numeric_cols=5, text_cols=2,
          caption_source="none",
          note="Model comparison grid introduced by 'We obtained the following results in "
               "the tables below': header 'Model | Y | Distr | # of Trips | % Open | Avg # "
               "Crossovers | Var from Distr -1e4' over 22 data rows in seven blocks (Y = 45, "
               "150 and 225 with Uniform and Triangle, plus the single D.Pertb. row at 200). "
               "Boxed with full vertical rules and a heavy rule between blocks; the last "
               "column header carries the -1e4 scale factor rather than a unit row.")

    # 5.3 - the two saturating pictures
    figure(15, 1, "composite-panel",
           ctext(15, "Figure 7:", "5.3 Bone Growth Model Results"),
           panels=3, layout="1+2", labels=True,
           mention=mention(15, ["Figure 7"],
                           "An example of one of the result is shown in Figure 7.", "direct"),
           note="Three panels in one region: a wide 'Schedule' panel of multicoloured "
                "threads (Day Number 0-200 against Campsite Number 0-250), and beneath it "
                "'Histogram of Trip Lengths' (blue bars, Trip Length 5-20 against Frequency "
                "0-300) and 'Histogram of Campsites Used' (a single jagged blue line, Camp "
                "Number 0-250). All three print tick numbers; no legend.")
    figure(16, 1, "composite-panel",
           ctext(16, "Figure 8:", "6 Analysis of Results"),
           panels=3, layout="1+2", labels=True,
           mention=mention(15, ["Figure 8"],
                           "a triangle distribution as seen in the Lower Left of Figure 8.",
                           "parenthetical"),
           note="The same three-panel layout with two models overlaid: the 'Schedule' panel "
                "interleaves red and blue dash columns, 'Histogram of Trip Lengths' shows "
                "paired red and blue bars, and 'Histogram of Campsites Used' carries two "
                "jagged lines. Blue is Bones1 and red is Bones2, per the caption; no legend "
                "inside the frame.")

    rules = [
        "Two measured regions are printed numeric grids the paper never numbers - the "
        "inline vessel-type counts on p4 and the 23-row model comparison on p14 - so they "
        "are recorded in the table block as table-grid with caption_source none "
        "[table.rows].",
        "Figures 2 and 3 are three-panel day-by-campsite step diagrams with no axes, no "
        "tick numbers and no legend, so panel_count is 3 and the family is "
        "flowchart-or-schematic rather than table-as-figure [geometry.panel_count].",
        "Figure 1 is a binned frequency histogram, not a bar chart of categories: axis "
        "titles 'Frequency' and 'Distance in Miles' [geometry.family].",
        "Figures 5, 7 and 8 are one measured region each holding several separately titled "
        "panels - 2x2 for Figure 5, a wide panel over two smaller ones for Figures 7 and 8 - "
        "so each is a single composite-panel row with panel_count 4, 3 and 3 "
        "[geometry.panel_count] [geometry.data_labels].",
        "Figures 4 and 6 carry printed tick numbers on both axes and no legend; Figure 6's "
        "colour key is given in the caption instead [geometry.printed_numbers] "
        "[geometry.legend].",
        "Captions that run on into prose are cut at the named sentence: Figure 4 before "
        "'period with 200 campsites', Figure 5 before the numbered step list, Figure 6 "
        "before 'This model can be extended', Figure 8 before '6 Analysis of Results' "
        "[caption.verbatim].",
        "Five figures are cited in running text within one page of the exhibit: Figure 4 "
        "from p10, Figures 5 and 6 on their own page, Figure 7 on its own page and Figure 8 "
        "from p15 [mention.lead_sentence].",
        "The p14 comparison table is used by 5.1 Model Comparison, which prints above it, "
        "so the use rule and the placement rule agree [place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-15420-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Ten measured regions, ten accounted: eight figure items, of which three are "
            "single-region composite panels, plus two counted tables. The paper numbers "
            "eight figures and all eight are measured; the two tables are printed numeric "
            "grids the paper never numbers (p4 vessel counts, p14 model comparison) and are "
            "recorded as table-grid with caption_source none. Declared gap: p1 carries 25 "
            "vector paths the layout pass leaves unmeasured; it is the cover page and holds "
            "no exhibit."
        ),
    }
    out = PROXY / "pb37-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
