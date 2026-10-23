"""Hand pass for P-C-2012-16075-4bbf9219 (ECNAM: an expanded criminal network analysis model
with a semantic/text extension, 22 pp).

The geometry pass measures 20 regions over 11 pages, and two printed exhibits return no region
at all (Table 1 on p5 and Table 8 on p19 - the detector sees dozens of paths on both pages but no
rectangle). Accounting: 13 figure rows + 7 counted tables = 20 regions, unaccounted 0.

    p6-r1   Figure 1   the message network, 83 named nodes, conspiracies in red
    p11-r1  Figure 2   the likelihood rank of the worked example, 10 marked points
    p12-r1  Figure 3(a) the 83-person likelihood ranking as computed first
    p12-r2  Figure 3(b) the same ranking recomputed with Gretchen promoted
    p14-r1  Figure 4   original and new ranking side by side
    p16-r2  Figure 5   the ranking with and without Text Analysis
    p17-r1  Figure 6   four basic properties of the conspirators' network
    p18-r1  Figure 7   the conspirators' network with size and colour carrying the score
    p19-r2  Figure 8   topic 7 node layout
    p19-r3  Figure 8   topic 11 node layout
    p19-r4  Figure 8   topic 13 node layout
    p20-r1  Figure 9   the three topic indexes as grouped bars
    p20-r2  Figure 10  the top five conspirators with their neighbours

    p13-r1  Table 2    the 14 conspirators Fisher Discriminant names
    p13-r2  Table 3    the 14 conspirators ECNAM names
    p14-r2  Table 4    the top 8 under the new scenario against the original
    p16-r1  Table 5    the topic weights, second half (the first half is on p15)
    p16-r3  Table 6    the top 8 with and without Text Analysis
    p19-r1  Table 7    degree, betweenness, closeness and leader score for the top 5
    p21-r1  Table 9    the five indexes for the same five people

Declared gaps, both because the page returns no measured region even though the table prints:
Table 1 (Symbol description, p5) and Table 8 (indexes of topic 7, 11, 13, p19).

Figure numbering here is panel level: the paper prints ten figure numbers, and Figure 3 and
Figure 8 are each printed as separately framed panels, so those get one row per measured panel
with the printed number repeated (lane convention, paper 40 precedent). Figures 4 and 5 are one
measured raster each holding two panels, so they stay one row with panel_count 2.

Usage: python -I tools/_dist_paper44.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2012-16075-4bbf9219"
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

A1 = "1.1 Problem Background"
A2 = "1.2 Our Work"
SYM = "3.2 Symbol Description"
MODEL = "4 Expanding Criminal Network Analysis Model"
NODE = "4.2.1 Node-level"
LINK = "4.2.2 Link-level"
EXPR = "4.2.3 The Expression of ECNAM"
VERIF = "4.3.1 Verification of ECNAM"
REQ1 = "4.3.2 Result of Requirement 1"
FISH = "4.4 Fisher Discrimination and ECNAM"
CLUES = "5 New Clues Discovered"
TEXT = "6.2 Application of Text Analysis in ECNAM"
COMP = "6.3 Comparison and Analysis"
BASIC = "7.1.1 Basic properties of conspirators’ network"
LEADER = "7.1.2 Leader detection of conspirators’ network"
TOPIC = "7.1.3 Analysis of three suspicious topic"
TOPFIVE = "7.1.4 Top Conspirators Analysis"

PATH = {
    6: [A1, A2, MODEL, NODE],
    11: [A1, MODEL, VERIF],
    12: [A1, MODEL, VERIF, REQ1],
    13: [A1, MODEL, FISH],
    14: [A1, CLUES],
    16: [A1, TEXT, COMP],
    17: [A1, BASIC],
    18: [A1, LEADER],
    19: [A1, TOPIC],
    20: [A1, TOPFIVE],
    21: [A1, TOPFIVE],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# recorded regions per page, counted first so doc_order stays monotonic
VENTION = {6: 1, 11: 1, 12: 2, 13: 2, 14: 2, 16: 3, 17: 1, 18: 1, 19: 4, 20: 2, 21: 1}

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


def caption_block(text: str, numbering: str, position: str = "below",
                  source: str = "text-layer") -> dict:
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
           caption_source: str = "text-layer",
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
        "caption_source": caption_source,
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
          rule_style: str, numeric_cols: int, text_cols: int,
          header_rows: int = 1, merged: bool = False, continued: bool = False,
          caption_source: str = "text-layer", position: str = "above",
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
        "caption_source": caption_source,
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption, numbering, position),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rule_style, "zebra": False, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "full", "orientation": "portrait",
            "continued": continued, "note_sentence": "",
        },
    })


def build() -> str:
    figure(6, 1, "node-link-network",
           ctext(6, "Figure 1: An overview of the network", " Secondly"),
           numbering="Figure N:", labels=True,
           note="All 83 workers as labelled circles - the 23 known conspirators filled solid "
                "red, the rest pale cyan - joined by thin violet edges and by heavy red edges "
                "for the suspicious message traffic named in the caption. Layout is a "
                "force-directed cloud with no axes, no ticks, no scale and no key; the caption "
                "carries the only encoding statement in the paper.")
    figure(11, 1, "line",
           ctext(11, "Figure 2: likelihood rank of the example", " From the result shown"),
           numbering="Figure N:", numbers=True, labels=True,
           mention_block=mention(11, ["Figure 2"],
                                 "we can get the result shown in Figure 2", "direct"),
           note="Ten black markers joined by a single blue line, x 'rank' 1 to 10, y "
                "'Likelihood(%)' 0 to 100 by 10, dashed gridlines on both axes and a panel "
                "title 'Likelihood rank of being part of the conspiracy'. Every point is "
                "annotated with a name, Dave at 100% falling to Bob under 5%, so the marked "
                "points are the whole data set rather than a sample.")
    figure(12, 1, "scatter",
           ctext(12, "Figure 3(a): Original result", " Figure 3(b)"),
           numbering="Figure N:", numbers=True, labels=True,
           mention_block=mention(12, ["Figure 3"],
                                 "we can get the result as shown in Figure 3", "direct"),
           note="Eighty-three blue star markers, unconnected, sorted by score: x 'Rank' 0 to "
                "100, y 'Likelihood(%)' 0 to 100, dashed gridlines, panel title 'Likelihood "
                "Rank of being part of the conspiracy'. The seven known conspirators are "
                "labelled in red - Elsie at the top, then Alex, Yao, Paul, Jean, Ulf and "
                "Harvey at ranks 25 to 30 - and the profile collapses to near zero past rank "
                "50. This is the left panel of a pair; (b) prints beside it under its own "
                "sub-caption and is recorded on its own row.")
    figure(12, 2, "scatter",
           ctext(12, "Figure 3(b): Gretchen is a conspirator", " From Figure 3(a)"),
           numbering="Figure N:", numbers=True, labels=True,
           mention_block=mention(12, ["Figure 3"],
                                 "we can figure out the result as shown in Figure 3(b)",
                                 "parenthetical"),
           note="The same eighty-three point star-marker plot recomputed with Gretchen "
                "promoted to conspirator, same axes and gridlines and the same red name "
                "annotations; Gretchen's marker climbs into the named group near 55%, which is "
                "the change the prose describes. Unlike (a) it carries no in-plot title and no axis "
                "titles, and its named set adds Delores. Recorded as the second row under one "
                "printed number, following the lane's panel-level rule.")
    table(13, 1, ctext(13, "Table 2: The result of Fisher Discriminant", " Number 7"),
          numbering="Table N:", rows=4, cols=8, rule_style="boxed",
          numeric_cols=7, text_cols=1,
          mention_block=None,
          note="Two stacked blocks with no header row, each a stub label ('Number', 'Name') "
               "followed by seven values: 7 10 13 16 17 18 20 / Elsie Dolores Marion Jerome "
               "Neal Jean Crystal, then 21 37 43 47 49 54 67 / Alex Elsie Paul Christina "
               "Harvey Ulf Yao. Fourteen conspirators, seven per block. The prose introduces it "
               "with 'The conspirators identified by Fisher Discriminant are:' and never names "
               "the number.")
    table(13, 2, ctext(13, "Table 3: The result of ECNAM", " Order 1"),
          numbering="Table N:", rows=6, cols=8, rule_style="boxed",
          numeric_cols=7, text_cols=1,
          note="Two stacked blocks: an 'Order' stub with 1 to 7 and 8 to 14, then 'Number' "
               "with 8 22 4 68 45 44 20 and 3 33 19 9 25 23 49, then 'Name' with Elsie Alex "
               "Sherri Yao Patricia Paul Kristine and Paige Gretchen Jean Hazel Franklin Eric "
               "Darlene. Fourteen names against Fisher's fourteen, only partly overlapping. No "
               "header row; the prose names no number.")
    figure(14, 1, "scatter",
           ctext(14, "Figure 4: The result of new clues", " Table 4"),
           numbering="Figure N:", panels=2, layout="1x2", numbers=True, labels=True,
           mention_block=mention(14, ["figure 4"],
                                 "the result is shown as figure 4 and table 4", "direct"),
           note="Two star-marker panels side by side under one raster, captioned 'Original "
                "likelihood rank' and 'New likelihood rank', each with 'Rank' on x, "
                "'Likelihood(%)' on y and dashed gridlines. The right panel carries the same "
                "seven red conspirator names plus Gretchen and Harvey, and the ordering changes "
                "at the top. Printed as one image, so one row with panel_count 2.")
    table(14, 2, ctext(14, "Table 4: the top 8 identified conspirators", " Rank 1"),
          numbering="Table N:", rows=3, cols=9, rule_style="boxed",
          numeric_cols=8, text_cols=1, merged=True,
          mention_block=mention(14, ["table 4"],
                                "the result is shown as figure 4 and table 4", "direct"),
          note="'Rank 1 to 8' across a merged header row, then a 'New' row - Sherri Gretchen "
               "Patricia Julia Kristine Darlene Franklin, with an empty final cell - and an "
               "'Original' row - Sherri Patricia Kristine Gretchen Hazel Franklin Eric "
               "Darlene. Both entries are names in the score columns, so this is a ranking "
               "grid rather than a numeric one; the two scored rows are not given.")

    # a table split over a page turn, then the two comparison exhibits
    table(16, 1, ctext(15, "Table 5: the weight of those 15 topics", " Topic number"),
          numbering="Table N:", rows=3, cols=9, rule_style="boxed",
          numeric_cols=8, text_cols=1, merged=False, continued=True,
          note="The second half of one table: 'Weight 0.25 0.25 0 0.25 0.5 0.25 0.75 0' over "
               "'Topic number 9 10 11 12 13 14 15' and 'Weight 0.25 0 0.75 0.25 1.0 0.25 0.5', "
               "the trailing cell empty on the last two rows. The caption and the first half - "
               "'Topic number 1 2 3 4 5 6 7 8' and its weight row - print at the foot of p15, "
               "where the detector returns no region, so only the p16 continuation is measured "
               "and `continued` is true.")
    figure(16, 2, "scatter",
           ctext(16, "Figure 5: the result of using and not using Text Analysis", " In order"),
           numbering="Figure N:", panels=2, layout="1x2", numbers=True, labels=True,
           mention_block=mention(16, ["Figure 5"],
                                 "solutions shown in Figure 5 and Table 5", "direct"),
           note="Two star-marker panels side by side in one raster: 'Not Using Text Analysis' "
                "in blue and 'Using Text Analysis' in red, both with 'Rank' 0 to 100 on x and "
                "'Likelihood(%)' on y and the same eight red name annotations. In the red panel "
                "the profile is compressed - more people above 50% - which is the effect the "
                "prose reports.")
    table(16, 3, ctext(16, "Table 6: the result of the two scenarios", " Rank 1"),
          numbering="Table N:", rows=5, cols=9, rule_style="boxed",
          numeric_cols=8, text_cols=1, merged=True,
          mention_block=mention(16, ["table 6"],
                                "are listed as table 6 shows", "direct"),
          note="'Rank 1 to 8' across a merged header row, then four body rows in two pairs: "
               "Name / New Score for the Text-Analysis run - Sherri 97.70% down to Hazel "
               "60.15% - and Name / Old Score for the original - Sherri 73.18% down to Julia "
               "48.44%. The prose explains in a parenthesis that 'New' is the Text-Analysis "
               "result and the other two rows are not.")

    # 7 Simulation and Analysis - the four properties and the scored network
    figure(17, 1, "composite-panel",
           ctext(17, "Figure 6: result of basic information of each node"),
           numbering="Figure N:", panels=4, layout="2x2", numbers=True,
           mention_block=mention(18, ["figure 6"],
                                 "Basic Conclusion based on figure 6", "direct"),
           note="Four framed panels in a 2x2 block for the four properties the prose "
                "describes: scatter of Degree against Number of nodes, scatter of Number of "
                "neighbors against Closeness centrality, scatter of Number of neighbors against "
                "Betweenness centrality, and a plain bar panel of Path length against Frequency. "
                "All four print tick numbers and axis titles and none prints a legend, so the "
                "block mixes plot types and takes family `composite-panel`; recorded as one "
                "raster with four panels rather than four rows.")
    figure(18, 1, "node-link-network",
           ctext(18, "Figure 7: conspirator networks"),
           numbering="Figure N:", labels=True,
           mention_block=mention(19, ["figure 7"],
                                 "From figure 7 and table 7, we can conclude that", "direct"),
           note="The conspirators-only network: nodes on a red ramp, radius growing with the "
                "leader-detect score, pink edges for message traffic. The caption states the "
                "encoding - bigger node, higher score; redder node, higher score - and there is "
                "no printed key, scale or axis inside the panel.")
    figure(19, 2, "node-link-network",
           ctext(19, "Figure 8: the visualized node layout of topic 7, 11, 13", " Table 8"),
           numbering="Figure N:",
           note="Left panel of three: the topic 7 network, about twenty-five red nodes of "
                "varying radius over thin pink edges, with a couple of isolated nodes chained "
                "off the main cluster. No axes, no labels, no key. Three separately framed "
                "panels under one printed number, so one row each.")
    figure(19, 3, "node-link-network",
           ctext(19, "Figure 8: the visualized node layout of topic 7, 11, 13", " Table 8"),
           numbering="Figure N:",
           note="Middle panel of three: the topic 11 network, the densest of the set - about "
                "thirty red nodes with the largest radii in the figure and many crossing pink "
                "edges, plus two nodes outside the cluster joined by one long edge each. No "
                "axes, labels or key.")
    figure(19, 4, "node-link-network",
           ctext(19, "Figure 8: the visualized node layout of topic 7, 11, 13", " Table 8"),
           numbering="Figure N:",
           note="Right panel of three: the topic 13 network, about thirty red nodes on a wider "
                "spread with one very large node near the top and two isolated chains at the "
                "right edge. No axes, labels or key. Table 8, which lists the three indexes for "
                "these same topics, follows on the same page but has no measured region and is "
                "declared a gap.")
    figure(20, 1, "bar",
           ctext(20, "Figure 9: indexes of topic 7, 11, 13", " Conclusion"),
           numbering="Figure N:", legend="inside",
           note="Grouped bars, three topics by three series - Active Index in periwinkle, Nodes "
                "Related Index in crimson, Average Score Index in pale yellow - over a grey "
                "plot area with horizontal gridlines and a key box inside the frame at the "
                "right. Every y-axis label prints as the placeholder '/\u901a\u7528\u683c\u5f0f' "
                "because the typeface the chart was pasted with is missing, so no scale is "
                "readable; the values live in Table 8 and in the prose instead. The caption "
                "duplicates Table 8's caption word for word.")
    figure(20, 2, "node-link-network",
           ctext(20, "Figure 10: top five conspirator nodes with their neighbors"),
           numbering="Figure N:", labels=True,
           note="Five conspirators picked out of the network with their immediate neighbours, "
                "node radius and colour holding the final score, edges for the message traffic. "
                "The caption states the encoding; no printed key, scale or axis inside the "
                "panel.")

    table(19, 1, ctext(19, "Table 7: indexes and leader detect score", " Index Name"),
          numbering="Table N:", rows=6, cols=6, rule_style="booktabs",
          numeric_cols=5, text_cols=1,
          mention_block=None,
          note="'Index | Name | Degree | Betweenness | Closeness | Leader Detect Score' over "
               "five rows: 3 Sherri 0.7407 0.1824 0.1015 1.0247, 7 Elsie, 67 Yao, 21 Alex, 32 "
               "Gretchen down to 0.8148. The score is the plain sum of the three indexes, which "
               "the row arithmetic confirms. Cited two pages of prose later, from p19.")
    table(21, 1, ctext(21, "Table 9: indexes and score of top five conspirator nodes",
                       " Index Name"),
          numbering="Table N:", rows=6, cols=7, rule_style="booktabs",
          numeric_cols=6, text_cols=1,
          note="'Index | Name | Data | Degree | Betweenness | Closeness | Score' over the same "
               "five people: 7 Elsie 7.8 0.24 0.10 0.04 100.00 down to 44 Patricia 70.88. The "
               "header prints seven labels while every body row carries six values, so one column "
               "prints without values - the paper's own slip, kept as printed.")

    rules = [
        "Figure 3 and Figure 8 print one number each over panels that are framed separately, "
        "so each framed panel gets its own row and repeats the printed number "
        "[caption.numbering].",
        "Figures 4 and 5 print as one raster holding two unframed panels, so each is a single "
        "row with panel_count 2 rather than two rows [geometry.panel_count].",
        "Table 5 runs over a page turn - caption and first half at the foot of p15, "
        "continuation at the head of p16 - and only the p16 half is measured, so that row "
        "carries `continued` and the note says where the rest prints [table.continued].",
        "Table 9's header prints seven labels over six columns of values, counted as printed "
        "rather than corrected [table.cols].",
        "Figure 9's y-axis prints '/\u901a\u7528\u683c\u5f0f' placeholder text on every tick "
        "because the pasted chart's typeface is missing, so `printed_numbers` is false even "
        "though ticks are drawn and the values are given in Table 8 [geometry.printed_numbers].",
        "Figure 9 repeats Table 8's caption - 'indexes of topic 7, 11, 13' - word for word, "
        "quoted as printed [caption.verbatim].",
        "Table 2 and Table 3 are introduced by a bare colon sentence ('The conspirators "
        "identified by Fisher Discriminant are:') and no numbered citation, so their mention "
        "blocks are empty [mention.count].",
        "Two printed tables return no measured region at all: Table 1 finishes p5 and Table 8 "
        "sits under Figure 8 on p19, so both are declared gaps rather than invented bboxes "
        "[caption.verbatim].",
        "Figures 6, 7 and 10 state their encoding in the caption only - no scale, key or axis "
        "label is printed inside the panel [geometry.legend].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-16075-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": [],
        "rules": rules,
        "note": (
            "Twenty measured regions, twenty accounted: thirteen figure rows for ten printed "
            "figure numbers (Figure 3 split into its two framed panels and Figure 8 into its "
            "three) and seven counted tables for nine printed table numbers. Table 1 on p5 and "
            "Table 8 on p19 print but return no measured region, so both are declared gaps and "
            "no bbox is invented for them. Table 5 is split over the p15/p16 turn and only its "
            "second half is measured."
        ),
    }
    out = PROXY / "pb44-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
