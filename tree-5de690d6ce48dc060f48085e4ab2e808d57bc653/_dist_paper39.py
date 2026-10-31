"""Hand pass for P-C-2012-12218-14ded715 (criminal-network conspirator ranking, 19 pp).

The geometry pass measures 12 regions over 9 pages: the paper's six printed figures and
six of its seven printed tables.

    p4-r1   Figure 1  multi-graph of ten staff, nodes A to J round a ring
    p4-r2   Figure 2  supergraph of five topics, a pentagon with every node joined
    p6-r1   Table 1   priority list for the EZ case, nine names with CD metric and rank
    p6-r2   Figure 3  discriminating line for the EZ case
    p7-r1   Table 2   partial priority list for requirement 1, two side-by-side blocks
    p8-r1   Figure 4  discriminating line for requirement 1
    p9-r1   Table 3   partial priority list for requirement 2, two side-by-side blocks
    p9-r2   Figure 5  discriminating line for requirement 2
    p12-r1  Table 5   leadership list on fusion values, two blocks of twenty
    p13-r1  Figure 6  concept and property relations
    p14-r1  Table 6   partial outputs from the semantic web
    p15-r1  Table 7   partial outputs of the vector space model

Table 4 (`Partial Outputs of Centrality Analysis`, p11, twenty names by Degree, Closeness
and Betweenness) is printed but the layout pass finds no region on p11 at all, so it is
declared as a gap in the record note rather than invented.

Accounting: 6 figure items + 6 counted tables = 12 regions, unaccounted 0.

Families, read off cropped page proxies:

* `node-link-network` is Figures 1 and 2: ten labelled nodes on a dashed ring joined by
  arcs, with a small inset table of the P' paths, and a five-node pentagon with all ten
  edges and the topic labels on the nodes.
* `line` is Figures 3, 4 and 5: one open-circle marker per ranked person, joined into a
  staircase, against "CD Metric" and "Rank", with a horizontal dashed threshold line that
  marks the discriminating cut. Figure 3 labels every point, Figures 4 and 5 label none.
* `flowchart-or-schematic` is Figure 6: boxes for sub-concepts feeding a Concept box that
  nests major concepts, joined to Property and then to sub-properties, with the dashed
  "Range Concepts" arrow between concept and property.
* `table-grid` is all six measured tables. Five of them are laid out as two side-by-side
  blocks of the same columns, so the physical grid is twice as wide as its column set.

Usage: python -I tools/_dist_paper39.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2012-12218-14ded715"
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

SCEN = "2 Investigation Scenario Based on Crime Data"
DEFS = "2.3 Explanation of the Model"
TESTS = "2.4 Tests and Verifications"
CASE = "3 Analysis on the Current Case"
PRIOR = "3.1 Priority Lists of Potential Conspirators"
INFO = "3.2 Performance with More Accurate Information"
LEAD = "4 Searching for Leaders"
INTERP = "4.2 Interpretation of Results"
OPT = "5 Model Optimizing"
SEMANTIC = "5.1 Semantic Network Analysis"
BUILD = "5.1.1 Construction of Semantic Network"
CORROB = "5.2.4 Corroboration of Model Reasonableness"

# Figure 4 prints on p8 above the 3.2 heading while still belonging to requirement 1, and
# Tables 3 and Figure 5 print on p9 above the 4.1 heading while finishing requirement 2;
# Table 6 prints above the 5.2 heading and belongs to the semantic network it scores.
PATH = {
    4: [SCEN, DEFS],
    6: [SCEN, TESTS],
    7: [CASE, PRIOR],
    8: [CASE, PRIOR],
    9: [CASE, INFO],
    12: [LEAD, INTERP],
    13: [OPT, SEMANTIC, BUILD],
    14: [OPT, SEMANTIC],
    15: [OPT, "5.2 Text Analysis", CORROB],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic
VENTION = {4: 2, 6: 2, 7: 1, 8: 1, 9: 2, 12: 1, 13: 1, 14: 1, 15: 1}

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


def caption_block(text: str, numbering: str) -> dict:
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


def figure(page: int, reg: int, family: str, caption: str, *, numbers: bool = True,
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
        "panel_count": 1,
        "caption_verbatim": caption,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption, "Figure N:"),
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": "none",
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, caption: str, *, rows: int, cols: int,
          rule_style: str, numeric_cols: int, text_cols: int,
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
            "rows": rows, "cols": cols, "header_rows": 1,
            "rule_style": rule_style, "zebra": False, "merged_cells": False,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": True, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "column", "orientation": "portrait",
            "continued": False, "note_sentence": "",
        },
    })


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": None}


PAIR = mention(4, ["Figure 1 and 2"],
               "Figure 1 and 2 presented above display the transition from multi-graph "
               "to the corresponding supergraph.", "direct")
T3F5 = mention(8, ["Table 3", "Figure 5"],
               "The results are displayed in Table 3 and Figure 5.", "direct")
T5_MENTION = mention(11, ["Table 5"],
                     "We choose 40 staff members who possess the highest fusion value "
                     "from our analysis, results are in Table 5.", "direct")
T6_MENTION = mention(13, ["Table 6"],
                     "The partial results with top 40 derived from semantic web have "
                     "been exhibited in Table 6.", "direct")

TWO_BLOCKS = ("Laid out as two side-by-side blocks of the same columns, left block "
              "first, so the physical grid carries twice the column set. No rule between "
              "body rows, one rule under each block's header, one rule between the two "
              "blocks and a closing rule at the foot.")


def build() -> str:
    # 2.3 - the two network pictures
    figure(4, 1, "node-link-network",
           ctext(4, "Figure 1:", "Figure 2:"),
           numbers=False, labels=True, mention=PAIR,
           note="Ten nodes labelled A to J set round a dashed ring, joined by thin arcs - "
                "a few of them arrowed - and by thick dashed path arcs, with a small "
                "inset table at the lower right listing the five paths P'1 to P'5 against "
                "the nodes each passes through. No axes, no ticks, no legend outside that "
                "inset table.")
    figure(4, 2, "node-link-network",
           ctext(4, "Figure 2:", "Figure 1 and 2 presented"),
           numbers=False, labels=True, mention=PAIR,
           note="The supergraph: five nodes on a regular pentagon labelled P'1 to P'5 "
                "with all ten edges drawn, no arrowheads and no edge labels. Flat, no "
                "axes, no ticks, no legend. The two captions are printed on one line "
                "underneath the pair, which is why each is cut at the other's marker.")

    # 2.4 - the EZ case list and its discriminating line
    table(6, 1, ctext(6, "Table 1:", "The top three in the list"), rows=10, cols=3,
          rule_style="boxed", numeric_cols=2, text_cols=1,
          note="Single block: header 'Name | CD metric | Rank' over nine staff rows from "
               "Dave at the top to Jaye at the foot, with tied ranks printed once per "
               "tie group (four names at rank 1, three at rank 4, two at rank 6). Boxed "
               "with a rule between every row and every column - the only table in this "
               "paper that is fully ruled.")
    figure(6, 2, "line",
           ctext(6, "Figure 3:", "In order to determine a discriminating line"),
           labels=True,
           note="A staircase of open circles, one per ranked staff member, rising against "
                "'Rank' 1 to 10 and 'CD Metric' 0.5 to 1.5, with every point labelled by "
                "name - Dave, George, Ellen, Carol, Fred, Harry, Bob, Inez, Anne, Jaye - "
                "and one horizontal dashed line drawn at the biggest jump, which is the "
                "discriminating line the caption names. No legend.")

    # 3.1 - requirement 1
    table(7, 1, ctext(7, "Table 2:", "We note that the 11 persons"), rows=21, cols=4,
          rule_style="booktabs", numeric_cols=2, text_cols=2,
          note="Two blocks of 'Name | CD metric', twenty rows of names in all, the left "
               "block ending at Lars and the right at Francis, with no rank column and "
               "many repeated values. " + TWO_BLOCKS)
    figure(8, 1, "line",
           ctext(8, "Figure 4:", "Paul, Harvey, Ulf"),
           note="The same staircase on the larger list: about forty open circles against "
                "'Rank' 1 to 40 and 'CD-Metric' 0 to 0.5, long plateaus broken by jumps, "
                "and a horizontal dashed threshold line at the cut. No point labels and "
                "no legend. The caption is printed inside a sentence, between the words "
                "of the list of possible conspirators, so the crop shows prose on both "
                "sides of it.")

    # 3.2 - requirement 2
    table(9, 1, ctext(9, "Table 3:", "Figure 5:"), rows=21, cols=4,
          rule_style="booktabs", numeric_cols=2, text_cols=2, mention=T3F5,
          note="Two blocks of 'Name | CD metric', twenty rows of names, left block from "
               "Chris to Kim and right block from Beth to Beth. " + TWO_BLOCKS)
    figure(9, 2, "line",
           ctext(9, "Figure 5:", "4.1 Centrality Analysis"),
           mention=T3F5,
           note="Third staircase of open circles, about forty of them, on 'Rank' 1 to 40 "
                "against 'CD-Metric' 0 to 0.5, four visible plateaus and a dashed "
                "threshold line near 0.14. No point labels, no legend.")

    # 4.2 - the fusion values
    table(12, 1, ctext(12, "Table 5:", "5 Model Optimizing"), rows=21, cols=6,
          rule_style="booktabs", numeric_cols=4, text_cols=2, mention=T5_MENTION,
          note="Two blocks of 'Name | Fusion Value | Rank', ranks 1 to 20 on the left and "
               "21 to 40 on the right, twenty rows per block. Decimal-aligned to four "
               "places in the value column. " + TWO_BLOCKS)

    # 5.1.1 - the concept and property diagram
    figure(13, 1, "flowchart-or-schematic",
           ctext(13, "Figure 6:", "The relations exhibited above"),
           numbers=False, labels=True,
           note="Boxes joined by elbow connectors: two 'Sub-concept' boxes over "
                "'Major Concept' boxes inside a 'Concept' frame, joined to a 'Property' "
                "box which branches down to two 'Sub-property' boxes, with ellipses "
                "marking the omitted siblings and a dashed two-way arrow labelled "
                "'Range Concepts' between concept and property. No axes, no ticks, no "
                "legend.")

    # 5.1 and 5.2.4 - the two CD-metric printouts
    table(14, 1, ctext(14, "Table 6:", "5.2 Text Analysis"), rows=21, cols=4,
          rule_style="booktabs", numeric_cols=2, text_cols=2, mention=T6_MENTION,
          note="Two blocks of 'Name | CD Metric', twenty rows per block: the left column "
               "runs eleven zeros then jumps to 0.7423, the right climbs from 0.7437 to "
               "0.9770 in ties. " + TWO_BLOCKS)
    table(15, 1, ctext(15, "Table 7:", "amazing that the members"), rows=21, cols=4,
          rule_style="booktabs", numeric_cols=2, text_cols=2,
          note="Two blocks of 'Name | CD Metric', twenty rows per block, the left "
               "half zeros then 0.9174 and the right a long run at 0.9271. " + TWO_BLOCKS)

    rules = [
        "Table 4 prints on p11 and the layout pass finds no region on that page at all, "
        "so the 21-row by 4-column centrality grid is declared as a gap in the note "
        "rather than recorded from an invented bbox [table.rows].",
        "Five of the six measured tables are laid out as two side-by-side blocks of the "
        "same columns, so cols counts the physical grid - 4 for a two-block Name/CD pair "
        "and 6 for the two-block Name/Fusion/Rank list - not the column set "
        "[table.cols] [table.text_cols].",
        "Table 1 is the only fully ruled grid in the paper, boxed with a rule between "
        "every row and column; the other five carry a rule under each block header, no "
        "rules between body rows, and only a closing rule at the foot [table.rule_style].",
        "Figures 1 and 2 are network drawings with no axes, so they carry "
        "printed_numbers false; Figures 3, 4 and 5 are marker staircases with printed "
        "ticks on both axes [geometry.printed_numbers].",
        "Figure 6 is a box-and-arrow concept diagram rather than a node-link graph: the "
        "entities are labelled rectangles joined by elbow connectors, not points joined "
        "by edges [geometry.family].",
        "Figures 1 and 2 are captioned on one line ('Figure 1: Multi-graph Figure 2: "
        "Supergraph'), so each caption is cut at the other figure's marker, and Figure 4's "
        "caption is printed inside a running sentence [caption.verbatim].",
        "Four exhibits are named in running text: Figures 1 and 2 by the sentence under "
        "them, Table 3 and Figure 5 together on p8, Table 5 from p11 and Table 6 from "
        "p13, each one page before its exhibit [mention.lead_sentence].",
        "Figure 4 prints above the 3.2 heading but belongs to requirement 1, and Table 3 "
        "and Figure 5 print above the 4.1 heading while finishing requirement 2, so both "
        "follow use over placement [place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-12218-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twelve measured regions, twelve accounted: six figure items for the paper's "
            "six printed figures and six counted tables. Declared gap: p11 prints Table 4 "
            "(Partial Outputs of Centrality Analysis, twenty staff rows against Degree, "
            "Closeness and Betweeness) and the layout pass measures no region on that "
            "page, so the table is named here and left unrecorded; no other page carries "
            "an unmeasured exhibit."
        ),
    }
    out = PROXY / "pb39-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
