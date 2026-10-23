"""Hand pass for P-A-2014-26911-00c95da0 (a coaching-great evaluation paper: metric hierarchy,
Google Trends sketches, AHP plus grey-relation/MaxEnt weights, sensitivity and universality
testing), 22 PDF pages.

Eight measured regions over five pages, and every one an exhibit: 3 figure rows and 5 printed
tables. No exclusions, no declared gaps.

    p10-r1  line                  Figure 1: Google Trends sketch of Knute Rockne
    p10-r2  line                  Figure 2: Google Trends sketch of Mike Krzyzewski
    p12-r1  flowchart-or-schematic Figure 3: the AHP evaluation hierarchy
    p15-r1  table-grid            Table 1: Top 5 College Coaches
    p16-r1  table-grid            Table 2: weights in football
    p16-r2  table-grid            Table 3: weights in basketball
    p16-r3  table-grid            Table 4: weights in baseball
    p17-r1  table-grid            Table 5: Top 5 Women's Volleyball College Coaches

The five tables are pasted raster images: the grid AND its caption are pixels, so nothing of
either is in the text layer and every caption is typed from the crop.

Usage: python -I tools/_dist_paper52.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2014-26911-00c95da0"
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

MODELS = "5 Models"
PRE = "5.2 Data Preprocessing"
TIME = "5.2.2 Modification of the Timeline"
AHP = "5.3 Subjective Weights Analysis: Analytical Hierarchy Process"
RES = "6 Results"
TEST = "7 Model Testing"
UNIV = "7.2 Universality Testing"

PATH: dict[int, tuple[list[str], str]] = {
    10: ([MODELS, PRE, TIME], "model"),
    12: ([MODELS, AHP], "result"),
    15: ([RES], "result"),
    16: ([RES], "result"),
    17: ([TEST, UNIV], "test"),
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

VENTION = {10: 2, 12: 1, 15: 1, 16: 3, 17: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}

CAP_101 = "Figure 1: Google Trends Trend Sketch of Knute Rockne(1918-30)"
CAP_102 = "Figure 2: Google Trends Trend Sketch of Mike Krzyzewski(1976-2010)"
CAP_123 = "Figure 3: The Hierarchy of the Evaluation System in AHP"
T1 = "Table 1: Top 5 College Coaches"
T2 = "Table 2: Weights of the Evaluation System in Football"
T3 = "Table 3: Weights of the Evaluation System in Basketball"
T4 = "Table 4: Weights of the Evaluation System in Baseball"
T5 = "Table 5:Top 5 Women’s Volleyball College Coaches"

# The one numbered citation in the paper sits on p12, names Figure 2, and introduces the
# hierarchy that is printed there as Figure 3 - so it points two pages BACKWARD from its page.
M_FIG2 = {
    "first_page": 12, "lead_pages": -2, "style": ["Figure 2"], "count": 1,
    "lead_sentence": "As is vividly shown in Figure 2, AHP provides a systematic assessment",
    "trail_sentence": "", "lead_pattern": "as-shown-in", "read_sentences": 1,
    "gap_sentences": None}


def printed(page: int, text: str) -> str:
    """Verify a caption string really prints on the page, once Unicode-normalised."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text))
    return text


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH[page]
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
        "caption": caption_block(caption_text, source, "below", numbering),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rules, "zebra": zebra, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "full", "orientation": "portrait",
            "continued": continued, "note_sentence": "",
        },
    })


def build() -> str:
    # --- section 5.2.2: the two Google Trends sketches ------------------------------------
    figure(10, 1, "line", printed(10, CAP_101), source="text-layer", numbering="Figure N:",
           position="below",
           note="A Google Trends screenshot pasted in as a raster: one thin blue line of relative "
                "search interest from 2005 to 2013, x labelled at 2005, 2007, 2009, 2011 and "
                "2013, y axis carrying no scale and no labels at all, three faint horizontal "
                "gridlines and no frame box. Seven peaks are lettered A to G in place instead of "
                "being explained by a legend, and the letters are not keyed anywhere on the "
                "figure [geometry.legend]. The line rises steeply in 2004-05, then decays with "
                "spikes, which is the slowly declining trend the prose describes.")
    figure(10, 2, "line", printed(10, CAP_102), source="text-layer", numbering="Figure N:",
           position="below",
           note="The same Google Trends screenshot construction for the second coach: one blue "
                "line over the same 2005-2013 axis, no y scale, faint horizontal gridlines, no "
                "frame and no legend. Fourteen peaks are lettered A to N in place; the tallest "
                "spikes sit in 2010-2013 rather than at the start of the record, which is the "
                "retirement peak the prose predicts. The p12 sentence that names 'Figure 2' "
                "describes the hierarchy drawn there as Figure 3, so this row is the number the "
                "prose points at with a ten-page gap [mention.lead_pages].",
           mention=M_FIG2)

    # --- section 5.3: the AHP hierarchy ----------------------------------------------------
    figure(12, 1, "flowchart-or-schematic", printed(12, CAP_123), source="text-layer",
           numbering="Figure N:", position="below",
           note="The evaluation hierarchy as a box-and-arrow chart on a raster: a red 'College "
                "Coaching Legends' goal at the top, three green criteria below it - Teams' "
                "performance, Player's performance, Coach's Personal Prestige - seven leaf "
                "boxes under those (Winning Percentage, Stability, Significant Victories, "
                "Personal Honors, Draftee Number, Personal Honor, Clicking Rate), and two blue "
                "'Policy Decisions' boxes at the foot with edges running up into the leaves. No "
                "numbers, no scale, no legend. The prose introduces it with a sentence whose "
                "number is missing ('the following Index Hierarchy Relationship Figure is "
                "displayed in Figure') and then cites 'Figure 2' - the p10 sketch - for it, so "
                "the row carries an empty mention and the miscitation is recorded on Figure 2 "
                "[mention.first_page].")

    # --- section 6: the five printed tables -------------------------------------------------
    table(15, 1, T1, source="typed-from-crop", numbering="Table N:", rows=6, cols=4,
          header_rows=1, rules="vertical-rules", zebra=True, numeric_cols=1, text_cols=3,
          note="The shortlist table, pasted in as a raster: header 'Ranking | Football | "
               "Basketball | Baseball' over five ranked rows (1 Tom Osborne / John Wooden / "
               "Cliff Gustafson down to 5 Bear Bryant / Clair Bee / Bibb Falk). A full-width "
               "dark blue header band with white bold labels, body rows tinted alternately light "
               "blue and white, faint rules between the rows, thin vertical rules between all "
               "four columns and a closed frame, so `rule_style` is `vertical-rules` and `zebra` "
               "is true. The only numeric column is the printed rank. Its caption prints BELOW "
               "the grid, which is the reverse of the lane's table rule [caption.position].")
    table(16, 1, T2, source="typed-from-crop", numbering="Table N:", rows=4, cols=2,
          header_rows=1, rules="vertical-rules", zebra=True, numeric_cols=1, text_cols=1,
          note="The weight vector for football: header 'Parameter | Weight' over three rows - "
               "AHP Weight, Maxent&GRC Weight, Comprehensive Weight - each weight being a "
               "seven-entry bracketed vector (0.28,0.11,0.25,0.08,0.03,0.20,0.07 for AHP). A "
               "vertical rule separates the two columns, rules run between the rows and the "
               "grid is closed, so `rule_style` is `vertical-rules`, and the body rows are "
               "tinted alternately light blue and white, so `zebra` is true. Caption below the "
               "grid, typed from the crop.")
    table(16, 2, T3, source="typed-from-crop", numbering="Table N:", rows=4, cols=2,
          header_rows=1, rules="vertical-rules", zebra=True, numeric_cols=1, text_cols=1,
          note="The same construction for basketball. Its AHP row repeats the football AHP "
               "vector exactly, which is the point of the method - the subjective weights are "
               "shared across sports and only the objective Maxent&GRC weights change "
               "(0.14,0.13,0.10,0.15,0.30,0.19 here against 0.14,0.10,0.25,0.29,0.08,0.14 for "
               "football). Caption below the grid, typed from the crop.")
    table(16, 3, T4, source="typed-from-crop", numbering="Table N:", rows=4, cols=2,
          header_rows=1, rules="vertical-rules", zebra=True, numeric_cols=1, text_cols=1,
          note="The same construction for baseball, again starting from the shared AHP vector "
               "and a fresh Maxent&GRC row (0.18,0.25,0.19,0.16,0.10,0.11). Caption below the "
               "grid, typed from the crop. The three weight tables sit at the top of p16, above "
               "the heading that opens section 7, because they belong to the section 6 sentence "
               "that announces them.")
    table(17, 1, T5, source="typed-from-crop", numbering="Table N:", rows=6, cols=3,
          header_rows=1, rules="vertical-rules", zebra=True, numeric_cols=1, text_cols=2,
          note="The universality-test result: header 'Ranking | Coach | College & Tenure' over "
               "five ranked coaches (Russ Rose, Don Shaw, John Dunning, Mick Haley, Dave Shoji) "
               "with tenure spans such as 'Pacific 1985-00,Stanford 2001-11'. Same blue header "
               "band, alternating tints and vertical rules as Table 1. Its caption prints below "
               "the grid and, unlike Tables 1 to 4, with NO space after the colon - 'Table 5:Top "
               "5 Women's Volleyball College Coaches' - so the quoted caption keeps the tight "
               "colon and the typographic apostrophe of the raster.")

    rules = [
        "The paper numbers its exhibits flatly - 'Figure 1:' to 'Figure 3:' and 'Table 1:' to "
        "'Table 5:' - so the colon form of the enum fits every record [caption.numbering].",
        "All five tables are pasted rasters: the grid, its blue header band and its caption line "
        "are pixels, so no caption text is in the text layer and every one is recorded with "
        "`caption_source: 'typed-from-crop'` [caption.verbatim].",
        "All five table captions print BELOW their grids, against the lane's convention that "
        "tables caption above, so the position is recorded as printed rather than normalised "
        "[caption.position].",
        "All five tables share one construction - a solid blue header band, alternating light "
        "blue body tints and thin vertical rules between the columns - so all five are "
        "`vertical-rules` with `zebra` true, and none is booktabs [table.rule_style].",
        "The three weight tables share one AHP row verbatim across football, basketball and "
        "baseball - the same seven-entry vector - because the subjective weights are common to "
        "all sports, while the Maxent&GRC row differs in each [table.rows].",
        "p10's two charts are Google Trends screenshots with no y axis scale, no frame and no "
        "legend; the peak letters A to G and A to N are in-figure annotations that are never "
        "keyed, so `legend` is `none` [geometry.legend].",
        "Figure 3 is a box-and-arrow hierarchy on a raster, recorded `flowchart-or-schematic` "
        "because every node is a labelled rectangle joined by drawn edges, not an unboxed "
        "node-link drawing [geometry.family].",
        "The paper's only numbered citation is broken: p12 says 'As is vividly shown in Figure "
        "2' while introducing the hierarchy printed on that page as Figure 3, so the mention is "
        "recorded on Figure 2 with `lead_pages` -2 and Figure 3's block is left empty "
        "[mention.lead_pages].",
        "The p10 sketches and the p12 hierarchy are all rasters with captions that survive in "
        "the text layer, while the p15-p17 tables are rasters whose captions do not - so "
        "`caption_source` is read per exhibit and not assumed from `kind` "
        "[caption.verbatim].",
        "Every heading is numbered except the stray 'Model' line on p16 and the 'References' "
        "line, so `section_path` quotes the printed numbered headings and `section_numbered` is "
        "true throughout [place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2014\u7f8e\u8d5b\u7279\u7b49\u5956/A-26911-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Eight measured regions over five pages of a 22-page paper, and every one is an "
            "exhibit: 3 figure rows and 5 printed tables, no exclusions and no declared gaps. "
            "The exhibit count is tiny because all but three pages are prose, equations and "
            "references. Two families: 2 `line` (the Google Trends sketches on p10, blue lines "
            "with no y scale and unkeyed peak letters) and 1 `flowchart-or-schematic` (the AHP "
            "hierarchy on p12, box-and-arrow), plus 5 `table-grid`. Every exhibit uses the "
            "colon form and flat numbering, Figure 1 to Figure 3 and Table 1 to Table 5. All "
            "five tables are pasted raster images whose captions are pixels too, so all five are "
            "typed from the crop and all five print their caption BELOW the grid, against the "
            "lane's table convention. All five share one construction - blue header band, "
            "alternating tints, thin vertical rules - so all five are `vertical-rules` with "
            "`zebra` true, and Table 5 alone prints a tight colon ('Table 5:Top 5 ...') with no "
            "space. The three weight "
            "tables repeat one AHP weight vector verbatim across the three sports. The paper's "
            "only numbered citation is wrong: p12 cites 'Figure 2' for the hierarchy that is "
            "printed there as Figure 3, so the mention sits on Figure 2 with lead_pages -2 and "
            "the hierarchy itself has none."
        ),
    }
    out = PROXY / "pc52-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
