"""Hand pass for P-C-2012-13855-8ff9127d (suspiciousness propagation on a message network, 19 pp).

The geometry pass measures 14 regions over 11 pages: ten ruled tables, one network drawing,
and three typeset pseudocode boxes.

    p4-r1   Table 1   the symbols and their values, three open columns
    p6-r1   Algorithm 1, a pseudocode box - not an exhibit
    p7-r1   Algorithm 2, a pseudocode box - not an exhibit
    p8-r1   Algorithm 3, a pseudocode box - not an exhibit
    p10-r1  Table 2   the 83-person priority list, four blocks of ID | S value
    p10-r2  Table 3   the 15 topic R values, four blocks of ID | R value
    p11-r1  Table 5   marked, conspiratorial and total messages for the five senior staff
    p12-r1  Table 6   suspicious contacts of the top 20, four blocks of ID | count
    p14-r1  Figure 1  the whole communication network around Chris
    p14-r2  Table 7   Chris's interlocutors, identity, message count and topics
    p15-r1  Table 9   the 15 initial R values, three blocks of Topic No. | R value
    p16-r1  Table 10  the priority list after topic analysis, three blocks of ID | S | Rank | Change
    p17-r1  Table 11  the priority list at DRS = DRR = 1, five blocks of ID | S value
    p17-r2  Table 12  the priority list at DRR = 0, five blocks of ID | S value

Three of the paper's thirteen tables are printed as bare columns with no rules drawn and are
measured by nothing, so they are declared gaps: Table 4 (p11, five staff rows against S),
Table 8 (the head of p15, From / To message pairs) and Table 13 (p19, the appendix
comparison). Table 5 and Table 9 occupy the measured bands on p11 and p15 instead.

Accounting: 1 figure item + 10 counted tables = 11 accounted, 3 excluded, 14 measured,
unaccounted 0.

Families, read off cropped page proxies and the text layer's cell counts:

* `node-link-network` is Figure 1 alone: 83 numbered nodes on grey, yellow and red edges.
* `table-grid` is the other ten measured regions.
* The three Algorithm boxes are pseudocode under a printed title bar, the class paper 8
  established for program listings, so they are excluded `not-an-exhibit`.

Usage: python -I tools/_dist_paper41.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2012-13855-8ff9127d"
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

MODELS = "4 Models and Methodology"
DEFS = "4.1 Definitions"
RESULTS = "5 Results and Analyses"
REQ1 = "5.1 Requirement 1"
SENIOR = "5.1.2 Senior Managers"
LEADERS = "5.1.3 Conspiracy Leaders"
EVAL = "6 Evaluation and Further Discussions"
SENS = "6.2 Model Sensitivity"
REQ2 = "6.2.1 Requirement 2: Changing Prior Knowledge"
INITIAL = "6.2.2 Initial Value for R function"
DECAY = "6.2.3 Decay rate"
REQ4 = "6.3 Requirement 4: Model Scalability and Other Applications"

# every heading in this paper is numbered, so each path is a numbered heading chain
PATH = {
    4: [MODELS, DEFS],
    10: [RESULTS, REQ1, SENIOR],
    11: [RESULTS, REQ1, SENIOR],
    12: [RESULTS, REQ1, LEADERS],
    14: [EVAL, SENS, REQ2],
    15: [EVAL, SENS, INITIAL],
    16: [EVAL, SENS, DECAY],
    17: [EVAL, REQ4],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# recorded regions per page, counted first so doc_order stays monotonic
VENTION = {4: 1, 10: 2, 11: 1, 12: 1, 14: 2, 15: 1, 16: 1, 17: 2}

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
           numbers: bool = False, labels: bool = False,
           mention_block: dict | None = None, note: str = "") -> None:
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
        "place": place(page, reg),
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
    # 4.1 - the symbol glossary
    table(4, 1, ctext(4, "Table 1: Model Definitions"),
          numbering="Table N:", rows=15, cols=3, rule_style="booktabs",
          numeric_cols=1, text_cols=2, width="full",
          note="A three-column glossary, 'Name | Definition | Value or Expression', over "
               "fourteen symbols from P_N and M_N down to cDR_S and cDR_R. The Definition "
               "column is prose, the last column mixes plain numbers (83, 910 with an "
               "alpha, 15), set expressions and inequalities (0 <= S_i <= 1) and equations "
               "(cDR_S = (DR_S)^n with a gamma). Open sides, a rule above and under the "
               "header and one at the foot. No citing sentence anywhere in the text, so its "
               "mention block is empty.")

    # 5.1.2 - the priority list and the topic table it rests on
    table(10, 1, ctext(10, "Table 2: Priority list for Requirement 1", "ID R value"),
          numbering="Table N:", rows=22, cols=8, rule_style="vertical-rules",
          numeric_cols=8, text_cols=0,
          mention_block=mention(9, ["Table 2"],
                                "a priority list of all 83 people is produced, which is "
                                "shown in Table 2.", "direct"),
          note="Four side-by-side blocks of 'ID | S value', twenty-one rows each, so the "
               "physical grid is eight columns and the body reads down each block in turn: "
               "49, 18, 21, ... in the first, 38, 50, 30, ... in the second. Eight people "
               "sit at exactly 1 and fourteen at exactly 0. Vertical rules between every "
               "column inside a closed box, one rule under the header, none between body "
               "rows.")
    table(10, 2, ctext(10, "Table 3: Suspiciousness of topics(R values) for Requirement 1",
                       "We find out that among"),
          numbering="Table N:", rows=8, cols=8, rule_style="vertical-rules",
          numeric_cols=8, text_cols=0,
          mention_block=mention(9, ["Table 3"],
                                "And the R value for all topics are shown in Table 3.",
                                "direct"),
          note="The same four-block layout for the fifteen topics: 'ID | R value' repeated "
               "four times, the last block holding only three pairs, so the grid is eight "
               "columns by eight rows with blank trailing cells. Rule set identical to "
               "Table 2.")

    # 5.1.2 continues - the two senior-staff tables
    table(11, 1, ctext(11, "Table 5: Messages of Senior Managers", "When analyzing"),
          numbering="Table N:", rows=6, cols=4, rule_style="booktabs",
          numeric_cols=3, text_cols=1, width="column",
          mention_block=mention(11, ["Table 5"],
                                "The data is displayed in Table 5.", "direct"),
          note="'Name & ID | Marked Msgs | Conspiratorial Msgs | Total Msgs' over the five "
               "senior staff - Gretchen No.4, Dolores No.10, Jerome No.16, Gretchen No.32 "
               "and Jerome No.34. The name and the person's number share one cell, so the "
               "grid is four columns, not five. Unlike the two priority tables this one is "
               "open-sided: a rule above the header, one under it and one at the foot.")
    table(12, 1, ctext(12, "Table 6: # of Suspicious contacts",
                       "From the Table 6"),
          numbering="Table N:", rows=6, cols=8, rule_style="vertical-rules",
          numeric_cols=8, text_cols=0,
          mention_block=mention(12, ["Table 6"],
                                "The statistics of the top 20 people in the priority list "
                                "is shown in Table 6.", "direct", count=2),
          note="'ID | #' repeated four times, five rows per block, twenty of the top twenty "
               "holders with the count of probable conspirators they wrote to about the "
               "conspiratorial topics - 3, 4, 7 and 10 reach four or more. Closed box with "
               "vertical rules, one header rule, no row rules. The caption itself is broken "
               "over a line break at 'conspirato- rial topics', so the quote stops before the "
               "hyphen.")

    # 6.2.1 - the network drawing and Chris's message record
    figure(14, 1, "node-link-network",
           ctext(14, "Figure 1: All connections with Chris(Node 0) and topic 1",
                 "Interlocutor No."),
           numbering="Figure N:", labels=True,
           mention_block=mention(14, ["Figure 1"],
                                 "This can also be verified by the illustration in Figure 1 "
                                 "that nodes mentioned above are either interlocutors of t1 "
                                 "(yellow links) or contacts",
                                 "direct"),
           note="The whole network as a hairball: 83 blue-ringed nodes labelled with their "
                "IDs 0 to 82, a thin grey edge per message pair, yellow edges for the "
                "interlocutors of topic 1 and red edges for Chris's own contacts, with the "
                "seven known conspirators filled red. Chris (node 0) sits at the top. No "
                "axes, no ticks, no legend inside the frame - the colour key is spelled out "
                "in the sentence that cites it.")
    table(14, 2, ctext(14, "Table 7: Chris", "To give a specific illustration"),
          numbering="Table N:", rows=5, cols=4, rule_style="booktabs",
          numeric_cols=2, text_cols=2, width="column",
          mention_block=mention(14, ["Table 7"],
                                "which can be seen in Table 7 and 8.", "direct", count=2),
          note="'Interlocutor No. | Identity | Number of messages | Topics' over four "
               "interlocutors: 32 Unknown, 21 conspirator, 2 non-conspirator and 68 "
               "non-conspirator. The Topics cell holds a comma-separated list of topic "
               "numbers, so it counts as numeric. Open sides and three horizontal rules. "
               "Same sentence cites Table 8, which is a declared gap on p15.")

    # 6.2.2 - the initial R values
    table(15, 1, ctext(15, "Table 9: R value initiation after topic analysis",
                       "These R values in Table 9"),
          numbering="Table N:", rows=6, cols=6, rule_style="vertical-rules",
          numeric_cols=6, text_cols=0,
          mention_block=mention(15, ["Table 9"],
                                "These R values in Table 9 is given based on a somehow "
                                "casual deduction.", "direct"),
          note="Three side-by-side blocks of 'Topic No. | R value' for the fifteen topics, "
               "so six physical columns by five body rows. These are hand-set priors, not "
               "model output: 0.6, 0.4, 0.1, 0.2, 0.5 in the first block, and both t11 and "
               "t13 at 1. The R values are written inconsistently - bare '1' and '0' beside "
               "one-decimal values. Vertical rules at both ends and between the blocks, "
               "continuous rules above and under the header and at the foot, none between "
               "rows.")

    # 6.2.3 - the two decay settings
    table(16, 1, ctext(16, "Table 10: Priority list after topic analysis", "6.2.3 Decay rate"),
          numbering="Table N:", rows=28, cols=12, rule_style="booktabs",
          numeric_cols=12, text_cols=0,
          mention_block=mention(15, ["Table 10"],
                                "As shown in Table 10, an initiation of R value can cause "
                                "considerable effect on the priority list", "direct"),
          note="The richest table in the paper: three blocks of 'ID | S | Rank | Change', "
               "twelve physical columns by twenty-seven body rows, ranking all 83 people "
               "four decimal places and printing the rank change as a signed integer. Nine "
               "people reach exactly 1.0000 after topic analysis and eight fall to 0. No "
               "vertical rules anywhere - three horizontal rules only.")
    table(17, 1, ctext(17, "Table 11: Priority list when setting DRS",
                       "ID S value"),
          numbering="Table N:", rows=18, cols=10, rule_style="vertical-rules",
          numeric_cols=10, text_cols=0,
          mention_block=mention(16, ["Table 11"],
                                "The resulting priority list is shown in Table 11.",
                                "direct"),
          note="Five blocks of 'ID | S value', ten physical columns by seventeen body rows. "
               "With both decay rates at 1 the list collapses towards certainty - the first "
               "block is all 1s and the neighbouring blocks carry 0.999999 and 0.974359 - so "
               "the printed precision grows where the values bunch. Closed box, vertical "
               "rules, header rule, no row rules.")
    table(17, 2, ctext(17, "Table 12: Priority list when setting DRR",
                       "6.3 Requirement 4"),
          numbering="Table N:", rows=18, cols=10, rule_style="vertical-rules",
          numeric_cols=10, text_cols=0,
          mention_block=mention(16, ["Table 12"],
                                "The results are shown in Table 12.", "direct"),
          note="The same five-block layout as Table 11 at DRR = 0: ten physical columns, "
               "seventeen body rows, everything at six decimals and eleven people at exactly "
               "0. Rule set identical to Table 11.")

    # the three pseudocode boxes
    for page, name, body in (
        (6, "Algorithm 1", "Top view of the whole methodology"),
        (7, "Algorithm 2", "Si Algorithm for calculating"),
        (8, "Algorithm 3", "Algorithm for calculating"),
    ):
        EXCLUDED.append({
            "page": page,
            "bbox": REG[(page, 1)],
            "reason": "not-an-exhibit",
            "note": f"A typeset {name} box, '{body}', with Initialization and phase steps "
                    f"under a printed title bar. Pseudocode, not a data grid or a drawing: "
                    f"the class paper 8 established for program listings.",
        })

    rules = [
        "Nine of the ten counted tables are printed as several side-by-side blocks of the "
        "same two or four columns, so `cols` counts the physical grid and `rows` the deepest "
        "block: Table 2 is four blocks of two columns, Tables 11 and 12 five blocks "
        "[table.cols] [table.rows].",
        "Two rule styles split the paper. Tables 2, 3, 6, 9, 11 and 12 sit in a closed box "
        "with vertical rules between every column and no rules between body rows; Tables 1, "
        "5, 7 and 10 are open-sided with three horizontal rules only [table.rule_style].",
        "Three of the thirteen printed tables are bare text columns with no rules drawn and "
        "no measured region: Table 4 on p11, Table 8 at the head of p15 and Table 13 on p19 "
        "[table.rows].",
        "Table 1 is the only table no sentence cites; Tables 2, 3, 4, 5, 6, 9, 10, 11 and 12 "
        "are each named once and Tables 6, 7, 8 and 13 more than once, Table 13 from a page "
        "four before the appendix prints it [mention.lead_sentence] [mention.count].",
        "Every caption in the paper is the numbered form with a colon, `Table N:` or "
        "`Figure N:`, and every caption prints below its exhibit; captions run from three "
        "words to a full sentence and only Table 8 states a condition [caption.position] "
        "[caption.numbering].",
        "Three regions on p6, p7 and p8 are typeset Algorithm boxes, not exhibits, and are "
        "excluded `not-an-exhibit`; a pseudocode listing has no drawing, so no geometry "
        "rule can catch it and only the header bar has ink [place.area_frac].",
        "Figure 1 is a node-link hairball with 83 labelled nodes and no axes, so it carries "
        "printed_numbers false and data_labels true; its colour key lives in the citing "
        "sentence rather than in a legend [geometry.printed_numbers] [geometry.legend].",
        "Every heading in the paper is numbered, so `section_path` is a numbered chain and "
        "section_numbered is true throughout [place.section_numbered].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-13855-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Fourteen measured regions, fourteen accounted: ten counted tables, one figure "
            "item for the paper's only figure, and three typeset Algorithm boxes excluded "
            "`not-an-exhibit`. Declared gaps: Table 4 on p11 (five senior staff against "
            "their S values), Table 8 at the head of p15 (the From/To message pairs for "
            "topic 1) and Table 13 on p19 (the appendix comparison of old and new ranks) are "
            "printed as unruled text columns that the layout pass cannot measure. Table 5 "
            "and Table 9 fill the measured bands on p11 and p15 respectively. No printed "
            "figure is missing."
        ),
    }
    out = PROXY / "pb41-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
