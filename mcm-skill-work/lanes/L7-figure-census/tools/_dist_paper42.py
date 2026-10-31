"""Hand pass for P-C-2012-14531-6018365f (logistic regression plus LeaderRank on the
83-person message network, 20 pp).

The geometry pass measures 12 regions over 10 pages: five figures, five tables, and the
summary sheet's title block.

    p1-r1   the summary-sheet title block - page furniture, not an exhibit
    p3-r1   Figure 1  the whole network, 83 nodes in three colours
    p7-r1   Figure 2  a target diagram of the possession rate per person
    p8-r1   Table 1   the topic adjacency matrix of the seven known conspirators
    p10-r1  Table 2   the top ten of the priority list, transposed into two stacked blocks
    p10-r2  Figure 3  probability of being criminal against rank
    p11-r1  Figure 4  the topic semantic diffusion framework
    p13-r1  Table 3   every topic ranked by similarity to the known suspicious topics
    p15-r1  Figure 5  betweenness centrality against degree centrality
    p17-r1  Table 5   the top ten before and after the requirement-2 change
    p18-r1  Figure 6  Kendall's tau against the misclassification probability
    p18-r2  Figure 7  probability under requirement 1 against probability under requirement 2

Table 4 (`Partial results of LeaderRank on G'TS`, four ranked leaders with their scores)
prints at the foot of p15 with no measured region, so it is a declared gap; Figure 5
occupies the only measured band on that page.

Accounting: 5 figure items + 5 counted tables = 10 accounted, 1 excluded, 11 of 12 measured
regions recorded and the twelfth declared in the note, unaccounted 0.

Families, read off cropped page proxies:

* `node-link-network` is Figure 1, 83 unlabelled circles, red for the known conspirators and
  blue for the known non-conspirators, edges coloured by the same key.
* `scatter` is Figure 2 (a polar target diagram with marker glyphs carrying the two identity
  classes), Figure 5 (three coloured series over a dashed threshold pair) and Figure 7 (six
  marker classes over a 45-degree identity line).
* `line` is Figure 3 (one marker-per-person curve with three managers highlighted on top of
  it) and Figure 6 (two series against a misclassification axis).
* `flowchart-or-schematic` is Figure 4, rounded message boxes feeding chevron dictionary
  entries and on to undetermined messages.
* `table-grid` is Tables 1, 2, 3 and 5.

Usage: python -I tools/_dist_paper42.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2012-14531-6018365f"
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

INTRO = "1 Introduction"
ML = "2 A Machine Learning Solution to Criminal Pri-"
FEAT = "2.1 Feature formulation"
RESULTS2 = "2.3 Results"
SEMANTIC = "2.4 Semantic model enhancement"
LEADER = "3 Identifying the leader of the conspiracy"
EMPIRICAL = "3.5 Empirical support"
EVAL = "4 Evaluating the Model"
SENS = "4.1 Sensitivity analysis"
PRIORITY = "4.1.1 Priority list"
INFLATION = "4.1.2 Probability inflation"

# Table 1 prints above the 2.2.1 heading and Figure 5 below the 3.5 one, but both are used
# by the sections named here, so use wins over placement as everywhere else in the lane.
PATH = {
    3: [INTRO],
    7: [ML, FEAT],
    8: [ML, FEAT],
    10: [ML, RESULTS2],
    11: [ML, SEMANTIC],
    13: [ML, SEMANTIC],
    15: [LEADER, EMPIRICAL],
    17: [EVAL, SENS, PRIORITY],
    18: [EVAL, SENS, PRIORITY],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# recorded regions per page, counted first so doc_order stays monotonic
VENTION = {3: 1, 7: 1, 8: 1, 10: 2, 11: 1, 13: 1, 15: 1, 17: 1, 18: 2}

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


def place(page: int, reg: int, route: list[str] | None = None) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route = list(route) if route else PATH[page]
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


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": None}


def figure(page: int, reg: int, family: str, caption: str, *, numbering: str,
           panels: int = 1, layout: str = "1", legend: str = "none",
           numbers: bool = True, labels: bool = False,
           mention_block: dict | None = None,
           route: list[str] | None = None, note: str = "") -> None:
    ORDER.append((page, reg))
    blocking = dict(mention_block) if mention_block else dict(NULL_MENTION)
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
        "place": place(page, reg, route),
        "mention": blocking,
        "caption": caption_block(caption, numbering),
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


def table(page: int, reg: int, caption: str, *, numbering: str, rows: int, cols: int,
          rule_style: str, numeric_cols: int, text_cols: int, width: str = "full",
          mention_block: dict | None = None, note: str = "") -> None:
    ORDER.append((page, reg))
    blocking = dict(mention_block) if mention_block else dict(NULL_MENTION)
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
        "caption": caption_block(caption, numbering),
        "table": {
            "rows": rows, "cols": cols, "header_rows": 1,
            "rule_style": rule_style, "zebra": False, "merged_cells": False,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": width, "orientation": "portrait",
            "continued": False, "note_sentence": "",
        },
    })


def build() -> str:
    # 1 Introduction - the whole network
    figure(3, 1, "node-link-network",
           ctext(3, "Figure 1: The 83-employee network", " Criminal networks"),
           numbering="Figure N:", labels=False, numbers=False,
           mention_block=mention(3, ["Figure 1"],
                                 "As illustrated in Figure 1, criminals and conspirators "
                                 "tend to form",
                                 "direct"),
           note="All 83 employees as plain circles with no labels: pale yellow for the "
                "unidentified, red for the known conspirators and blue for the known "
                "non-conspirators, joined by curved edges in the same three colours over a "
                "light background. No axes, no ticks, no legend inside the frame - the key "
                "is parenthetical in the caption itself.")

    # 2.1 Feature formulation - the possession-rate target diagram
    figure(7, 1, "scatter",
           ctext(7, "Figure 2: Possession rate of neighboring accomplices distribution",
                 " \u2022 Number of current"),
           numbering="Figure N:", legend="inside", labels=True,
           mention_block=mention(6, ["Figure 2"],
                                 "As shown in Figure 2, we calculate the possession rate of "
                                 "its confederacy among all its", "direct"),
           note="A target diagram rather than a cartesian plot: four concentric circles "
                "ticked 0, 0.25, 0.5, 0.75 and 1 with a dashed cross and arrowheads on both "
                "axes, so a person's possession rate reads as radius. Seven blue stars for "
                "the known conspirators (Yao, Ulf, Paul, Eric, Jean, Alex, Harvey) crowd the "
                "inner rings; eight red stars for the known non-conspirators (Gard, Erlin, "
                "Chris, Este, Derlene, Tran, Paige, Jia) sit further out. Names are printed "
                "beside every marker and the two-entry key sits inside the frame at the "
                "lower left.")

    # 2.2.1 print position, 2.1 use - the topic adjacency matrix
    table(8, 1, ctext(8, "Table 1: Topics among known conspirators", " 2.2.1 Logistic"),
          numbering="Table N:", rows=8, cols=8, rule_style="boxed",
          numeric_cols=7, text_cols=1,
          mention_block=mention(7, ["Table 2.1"],
                                "Table 2.1 is the topics mentioned between known "
                                "conspirators.", "direct"),
          note="A square adjacency matrix of the seven known conspirators - Jean, Alex, "
               "Elsie, Poul, Ulf, Yao and Harvey - with the same seven names as the column "
               "header and as the first column, so the top-left cell is blank and the grid "
               "is eight by eight. Cells hold the topic numbers of the messages between the "
               "pair, a star marking the conspiratorial topics and several cells listing "
               "three topics at once; the matrix is asymmetric where only one direction was "
               "logged. Fully ruled, every row and every column. The text cites it as "
               "'Table 2.1', which is a misnumbering of Table 1 carried into the record as "
               "the citing spelling.")

    # 2.3 Results - the transposed top ten and the rank curve
    table(10, 1, ctext(10, "Table 2: Top 10 in the priority list",
                       " Figure 3 illustrates"),
          numbering="Table N:", rows=6, cols=6, rule_style="booktabs",
          numeric_cols=5, text_cols=1,
          mention_block=mention(9, ["Table 2"],
                                "The top 10 suspicious are shown in Table 2, where managers "
                                "are marked by a star", "direct"),
          note="Two stacked blocks, each transposed: a Name row of five people, then a "
               "Node No. row (10, 20, 34, 3, 17 in the first block) and a Probability of "
               "conspiracy row (0.555 down to 0.299). Six physical columns, six rows, a rule "
               "under every row and a heavier rule between the two blocks; no vertical "
               "rules. A star after a name marks a manager.")
    figure(10, 2, "line",
           ctext(10, "Figure 3: Probability of conspiracy", " 2 As more than one nodes"),
           numbering="Figure N:", legend="inside",
           mention_block=mention(10, ["Figure 3"],
                                 "Figure 3 illustrates the probability of criminal "
                                 "involvement estimated by h\u03b8 (x) versus the "
                                 "corresponding rank in the priority list", "direct"),
           note="One marker-per-person curve falling from 1 at rank 1 to about 0.02 at rank "
                "82, with three managers lifted out of the curve as separate open markers - "
                "Gretchen as a red circle at rank 32, Jerome as a diamond, Dolores as a "
                "square - each keyed in a boxed legend inside the frame at the upper right. "
                "Axes: 'Rank in the priority list' ticked 10 to 70 and 'Probability of being "
                "criminal' ticked 0 to 1 by 0.1, over dotted gridlines.")

    # 2.4 Semantic model enhancement - framework, then its result table
    figure(11, 1, "flowchart-or-schematic",
           ctext(11, "Figure 4: Framework of topic semantic", " Lexical ambiguity"),
           numbering="Figure N:", legend="inside", numbers=False, labels=True,
           mention_block=mention(12, ["Figure 4"],
                                 "As seen in Figure 4, a conspiratorial dictionary is",
                                 "direct", count=2),
           note="A left-to-right schematic: rounded Conspiratorial Message 1 to x boxes feed "
                "chevron-shaped 'suspicious word 1' to 'suspicious word n' entries inside a "
                "bracket labelled Conspiratorial Dictionary, and arrows leave the bracket "
                "for rounded Undetermined Message 1 to m boxes. Ellipses stand for the runs "
                "of indices. A two-entry Legend box (chevron for a new conspiratorial "
                "message, crossed arrow for a new non-conspiratorial one) sits inside the "
                "frame at the lower left. Cited from the next page, from two sentences.")
    table(13, 1, ctext(13, "Table 3: Rank of all topics", " conspiratorial dictionary and"),
          numbering="Table N:", rows=9, cols=3, rule_style="boxed",
          numeric_cols=3, text_cols=0,
          note="'Rank | Topic Number | Similarity to known suspicious topics' over eight "
               "rows: the three conspiratorial topics 11, 7 and 13 on top at 0.750 and two "
               "0.667 scores, the innocuous topics in the middle, and one bottom row that "
               "lumps eight topics into a single cell at similarity 0. Fully ruled. No "
               "sentence cites it, so the mention block is empty.")

    # 3.5 Empirical support - the centrality scatter
    figure(15, 1, "scatter",
           ctext(15, "Figure 5: The joint distribution of betweenness centrality"),
           numbering="Figure N:", legend="inside",
           mention_block=mention(16, ["Figure 5"],
                                 "Figure 5 illustrates the joint distribution of betweenness "
                                 "centrality CB and degree", "direct"),
           note="Fifteen markers in three colours keyed inside the frame at the upper left - "
                "black for the known conspirators, blue for the high-probability remainder "
                "and one red for Yao, the inferred leader - over 'Betweenness centrality' "
                "ticked 0.00 to 0.05 and 'Degree centrality' ticked 8 to 20. Two dotted "
                "gridlines carry a heavier dashed cut at about 13.6 degree and 0.028 "
                "betweenness, so the plot is read as four quadrants. One region only, even "
                "though Table 4 prints on the same page.")

    # 4.1.1 and 4.1.2 - the sensitivity tables and figures
    table(17, 1, ctext(17, "Table 5: Change with top 10", " Then Kendall"),
          numbering="Table N:", rows=10, cols=6, rule_style="booktabs",
          numeric_cols=5, text_cols=1,
          mention_block=mention(16, ["Table 5"],
                                "their new places at 12th, 14th and 16th respectively, as "
                                "illustrated in Table 5.", "direct"),
          note="Two stacked blocks of the same ten people after the requirement-2 change, "
               "transposed like Table 2: single-letter row labels down the first column - "
               "Rank (previous), Prob. of conspiracy (previous), Rank (new), Prob. of "
               "conspiracy (new) - and five people across, six physical columns by ten rows. "
               "A rule under every row, a heavier rule between the blocks, no vertical "
               "rules. The previous-probability row of the second block repeats the first "
               "block's five values verbatim under five different names, which looks like a "
               "typesetting slip in the paper rather than a result.")
    figure(18, 1, "line",
           ctext(18, "Figure 6: The expected Kendall", " 1 0.9 Probability"),
           numbering="Figure N:", legend="inside",
           mention_block=mention(17, ["Figure 6"],
                                 "Figure 6 depicts the expected Kendall\u2019s tau versus",
                                 "direct", count=2),
           note="Two series over eight unevenly spaced x values: a black open-circle line "
                "for the conspirator set and a red asterisk line for the non-conspirators, "
                "both starting at tau = 1 and both falling to about 0.83, crossing near "
                "0.4. Axes: 'Probability of wrong classification' 0 to 0.5 and 'Kendall's "
                "tau' 0.8 to 1.0, dotted gridlines, boxed legend inside the upper right.")
    figure(18, 2, "scatter",
           ctext(18, "Figure 7: Criminal probabilities", " The analysis suggests"),
           numbering="Figure N:", legend="inside",
           route=[EVAL, SENS, INFLATION],
           mention_block=mention(17, ["Figure 7"],
                                 "Figure 7 illustrates the change with estimated conspiracy "
                                 "probability", "direct"),
           note="Before-and-after scatter against a dashed 45-degree line: 'Probability of "
                "being a conspirator (Requirement 1)' on x and '...(Requirement 2)' on y, "
                "both 0 to 1. Six marker classes keyed in a boxed legend at the lower right "
                "- green crosses for the training set, blue crosses for the unknown nodes, "
                "and separate glyphs for Chris, Gretchen, Jerome and Dolores. Nearly every "
                "point stays below 0.4 on both axes, so most of the frame is empty.")

    # the summary sheet's drawn title block
    EXCLUDED.append({
        "page": 1,
        "bbox": REG[(1, 1)],
        "reason": "background",
        "note": "The summary sheet's drawn title block, half the page tall and picked up "
                "because the title and the 'Problem Clarification' band are set as vector "
                "paths. Page furniture, not an exhibit.",
    })

    rules = [
        "The summary sheet's title block is measured as a region on p1 but is page "
        "furniture, so it is excluded `background`; the paper's own exhibits start on p3 "
        "[place.area_frac].",
        "Table 4 (`Partial results of LeaderRank on G'TS`) prints on p15 with no measured "
        "region at all, and is named in the record note as a declared gap [table.rows].",
        "Tables 2 and 5 are transposed: the people run across the columns and the row "
        "labels down the first column, so the grid is wider than it is tall and the body "
        "carries words in one column and numbers in the rest [table.numeric_cols] "
        "[table.text_cols].",
        "Table 1 is a square adjacency matrix with the same seven names as header and as "
        "first column and a blank top-left cell, fully ruled; Tables 3 and 5 use the other "
        "two rule styles, a closed box for Table 3 and horizontal rules only for Table 5 "
        "[table.rule_style].",
        "Figure 2 is a polar target diagram - concentric rings ticked 0 to 1 with a dashed "
        "cross - so it is recorded as scatter with printed_numbers true and data_labels "
        "true, its two identity classes keyed inside the frame [geometry.family] "
        "[geometry.legend].",
        "Figures 1 to 7 carry only the bare caption form `Figure N:` with no period after "
        "the number, and every caption prints below its exhibit [caption.numbering] "
        "[caption.position].",
        "Two exhibits are cited from the page before they print and one is cited from the "
        "page after, so four rows carry a non-zero or negative `lead_pages`: Figure 4 at "
        "-1, Figure 5 at -1, Table 1 and the rest at +1 [mention.lead_pages].",
        "The text cites Table 1 as 'Table 2.1', which is a misnumbering; the record keeps "
        "the citing spelling in `mention.style` and says so in the row note "
        "[mention.style].",
        "Every heading is numbered except the axis-label fragments the heading pass picks "
        "up, where the run of numbers is a printed tick string rather than prose. All ten "
        "recorded rows use a numbered chain and section_numbered is true "
        "[place.section_numbered].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-14531-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twelve measured regions, twelve accounted: five figure items, five counted "
            "tables, one summary-sheet title block excluded `background`, and one printed "
            "table with no region. Declared gap: Table 4 (`Partial results of LeaderRank on "
            "G'TS`, four ranked leaders with their scores) prints at the foot of p15 and the "
            "layout pass measures nothing there, since Figure 5 fills the only band. Every "
            "printed figure is measured. The text also cites Table 1 as 'Table 2.1'."
        ),
    }
    out = PROXY / "pb42-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
