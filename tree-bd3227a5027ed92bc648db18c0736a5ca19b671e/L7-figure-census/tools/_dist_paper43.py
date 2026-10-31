"""Hand pass for P-C-2012-15356-6b8f0a28 (the iRank model of suspicion plus a semantic
network extension, 20 pp).

The geometry pass measures 15 regions over 12 pages: ten figure rows, five table rows.

    p2-r1   Figure 1  topics per person, conspirator against non-conspirator, three categories
    p3-r1   Figure 2  the same pair for conspiratorial topics, two categories
    p4-r1   the symbol glossary, Symbol | Definition | Formula, with no printed number
    p8-r1   Figure 3  closeness against the two groups, with the abnormal nodes ringed
    p9-r1   Table 1   Task 1 action counts, two side-by-side blocks under one title row
    p9-r2   Table 2   the nine highest iR scores in Task 1, transposed to two rows
    p10-r1  Figure 4  the iR bar ranking with a threshold rule drawn across it
    p11-r1  Figure 5  neighbourhood connectivity against average shortest path length
    p12-r1  Table 3   Task 2 action counts, the same two-block layout as Table 1
    p12-r2  Table 4   the sixteen highest iR scores in Task 2, two columns by eighteen rows
    p12-r3  an uncaptioned paired-bar chart printed beside Table 4
    p13-r1  Figure 6  the criminal network with node colour and size carrying the iR value
    p15-r1  Figure 7a the semantic-analysis workflow, Text to Network to Answer
    p17-r1  Figure 8  two one-node panels showing how the link weights give alpha
    p19-r1  Figure 7b the infection model, fifteen numbered cells

The paper prints two exhibits numbered Figure 7 - the workflow on p15 and the infection model
on p19 - so both are recorded and the second one's note says so. Every caption prints below
its exhibit and every heading is unnumbered.

Accounting: 10 figure rows + 5 counted tables = 15 regions, unaccounted 0.

Families, read off cropped page proxies:

* `bar` is Figures 1, 2 and 4 and the uncaptioned chart on p12: grey paired bars on a
  category axis, and in Figure 4 and the p12 chart a heavy horizontal rule drawn across the
  bars as a threshold.
* `scatter` is Figures 3 and 5, both dot clouds with a hand-drawn ellipse round the
  outlying points and a label in plain text beside it.
* `flowchart-or-schematic` is Figure 7a (three framed stages joined by arrows) and Figure 8
  (two panels of block arrows carrying printed weights and the alpha formula).
* `node-link-network` is Figure 6 (83 numbered nodes on a yellow to orange ramp) and the
  p19 infection model (15 numbered nodes on a grey ramp).
* `table-grid` is the glossary and Tables 1 to 4.

Usage: python -I tools/_dist_paper43.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2012-15356-6b8f0a28"
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
HEADKIND = {f"未编号标题 {k}": v for k, v in HEADKIND.items()}

INTRO = "未编号标题 Introduction"

# The paper prints four headings in all - Summary, Introduction, Assumptions and
# References - and none of them carries a number, so every row is routed to the opening
# Introduction section rather than to a numbered chain.
PATH = {p: [INTRO] for p in (2, 3, 4, 8, 9, 10, 11, 12, 13, 15, 17, 19)}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# recorded regions per page, counted first so doc_order stays monotonic
VENTION = {2: 1, 3: 1, 4: 1, 8: 1, 9: 2, 10: 1, 11: 1, 12: 3, 13: 1, 15: 1, 17: 1, 19: 1}

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
        "section_numbered": False,
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
          rule_style: str, numeric_cols: int, text_cols: int, width: str = "full",
          merged: bool = False, caption_source: str = "text-layer",
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
        "caption": caption_block(caption, numbering),
        "table": {
            "rows": rows, "cols": cols, "header_rows": 1,
            "rule_style": rule_style, "zebra": False, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": width, "orientation": "portrait",
            "continued": False, "note_sentence": "",
        },
    })


def build() -> str:
    # Introduction - the two message-count comparisons
    figure(2, 1, "bar",
           ctext(2, "Figure 1: Comparison of number of topics"),
           numbering="Figure N:", legend="outside-right",
           mention_block=mention(3, ["Figure 1"],
                                 "In Figure 1, from the total number of conversations "
                                 "(left bar), we can", "direct"),
           note="Paired bars - dark for conspirators, pale for non-conspirators - over three "
                "category labels, TOTEL, OUT and IN, with the two-entry key inside the frame "
                "at the right. The axis line carries tick marks but no tick numbers and no "
                "axis titles, so heights are only comparable inside the panel.")
    figure(3, 1, "bar",
           ctext(3, "Figure 2: Messages with conspiratorial topics", " Another pattern"),
           numbering="Figure N:", legend="outside-right",
           note="The same paired-bar treatment narrowed to two categories, OUT and IN, with "
                "the conspirator bar about six times the non-conspirator bar in both. Tick "
                "marks but no tick numbers, no axis titles, key at the right inside the "
                "frame.")

    # the unnumbered symbol glossary
    table(4, 1, "", numbering="none", rows=25, cols=3, rule_style="vertical-rules",
          numeric_cols=0, text_cols=3, caption_source="none",
          note="An unnumbered glossary: 'Symbol | Definition | Formula' over twenty-four "
               "symbols, from G and N down through the message counters ms_n, mr_n, ts_n and "
               "tr_n to the harmonic series hs and hr and the closeness heuristic d. The "
               "Formula column is filled on only half the rows. A closed box with vertical "
               "rules between the three columns, a rule above and under the header and no "
               "rules between body rows; nothing prints as a table number, so the record "
               "carries an empty caption.")

    # Analysis - the abnormal nodes and the two Task 1 tables
    figure(8, 1, "scatter",
           ctext(8, "Figure 3 Abnormal nodes", " Step 2: Iteration"),
           numbering="Figure N",
           note="A dense dot cloud - about a hundred identical black markers - rising along "
                "the diagonal, with the axis titled 'Degree of cSW' on x and 'Degree of iSW' "
                "on y. Ticks carry no numbers. Nine of the outlying low-right points are "
                "circled by a hand-drawn black ellipse labelled 'abnormal nodes' in plain "
                "text, and two further points sit outside the ellipse. The caption carries no "
                "colon after the number, unlike every other caption in the paper.")
    table(9, 1, ctext(9, "Table 1:", " Assume t"), numbering="Table N:",
          rows=6, cols=8, rule_style="boxed", numeric_cols=2, text_cols=6, merged=True,
          note="Two side-by-side blocks of 'Sender | Topic | Receiver | Count' under one "
               "merged title row reading 'Task 1 Statistics', repeated header included, four "
               "body rows per block: the n_c and n_n sender/receiver pairs on the left and "
               "the l_c topic pairs on the right, counts 26, 6, 5 and 10 against 31, 3, 28 "
               "and 7. Dashes stand in for the empty cell of each triple. Closed box, "
               "vertical rules, and a rule between every pair of rows.")
    table(9, 2, ctext(9, "Table 2: Significant suspects"), numbering="Table N:",
          rows=3, cols=10, rule_style="boxed", numeric_cols=9, text_cols=1,
          note="Transposed to two rows: a stub column of row labels, 'Node #' and 'iR', then "
               "nine data columns - 81, 51, 16, 33, 57, 60, 28, 79, 10 with scores from "
               "0.8571 down to 0.4790. Ten physical columns by three rows, closed box with "
               "vertical rules and one rule between the two data rows.")

    # Task 1 reading - the iR bars and the connectivity cloud
    figure(10, 1, "bar",
           ctext(10, "Figure 4: Suspicious level shown by IR", " To distinguish"),
           numbering="Figure N:",
           note="About eighty plain grey vertical bars sorted in ascending order by iR, so "
                "the profile steps up to a plateau and then jumps at the right where the "
                "conspirators bunch. A heavy black horizontal rule is drawn across the bars "
                "at about mid height as the cut between suspicious and not. No ticks, no "
                "numbers, no axis titles, no legend.")
    figure(11, 1, "scatter",
           ctext(11, "Figure 5: the correlation between neighborhood connectivity",
                 " Obviously,"),
           numbering="Figure N:",
           note="Sixty-odd black markers over 'AverageShortestPathLength' (0 to 7.5 by 0.5) "
                "against 'NeighbourhoodConnectivity' (0 to 22 by 1), dotted gridlines on both "
                "axes. Two high points near 2.5 to 3.5 on x are enclosed by a hand-drawn "
                "ellipse labelled 'leadership' in plain text, and a handful of isolated "
                "points sit far right at low connectivity.")

    # Task 2 - the matching tables and the chart beside its own table
    table(12, 1, ctext(12, "Table 3:", " From the"), numbering="Table N:",
          rows=6, cols=8, rule_style="boxed", numeric_cols=2, text_cols=6, merged=True,
          note="Structurally Table 1 again: two blocks of 'Sender | Topic | Receiver | "
               "Count' under one merged title row, four body rows per block, counts 29, 9, 6 "
               "and 3 against 38, 5, 33 and 9. The title row inside the grid reads 'Task 2 "
               "Statistics' while the printed caption says 'in Task 1' - the paper's own "
               "mismatch, kept as printed and stated here.")
    table(12, 2, ctext(12, "Table 4: The significant suspects"), numbering="Table N:",
          rows=18, cols=2, rule_style="boxed", numeric_cols=1, text_cols=1,
          note="'Node # | iR' over seventeen rows, 16 at 0.94099 down to 15 at 0.41772, "
               "closed box with a vertical rule between the two columns and a rule between "
               "every pair of rows. The region also spans the paired-bar chart printed to its "
               "right, which is recorded on its own row at p12-r3.")
    figure(12, 3, "bar", "", numbering="none", caption_source="none",
           note="An uncaptioned paired-bar chart printed to the right of Table 4 and larger "
                "than the copy visible inside Table 4's region: alternating blue-grey and "
                "green bars per node, rising left to right with a jump at the far right, one "
                "heavy black horizontal threshold rule across the plot, full frame, no ticks, "
                "no numbers, no axis titles, no legend. No sentence cites it, so it is "
                "recorded with an empty caption and an empty mention block.")

    # 4 Analysis continued - the network and the workflow
    figure(13, 1, "node-link-network",
           ctext(13, "Figure 6: Visualization of the Criminal Network",
                 " Evaluation and Discussion"),
           numbering="Figure N:", labels=True,
           note="All 83 nodes on a regular grid, each labelled with its ID and drawn as a "
                "circle whose fill runs from yellow through orange and whose radius grows "
                "with the printed iR value, over grey unweighted edges. Four small red "
                "squares and one green circle mark individuals singled out in the text. No "
                "axes, no ticks, no legend - the colour and size key is explained only in the "
                "surrounding prose.")
    figure(15, 1, "flowchart-or-schematic",
           ctext(15, "Figure 7: Semantic Network Analysis Work Flow", " In the first step"),
           numbering="Figure N:", labels=True,
           note="Three framed stages in a row - 'Text' holding a pasted snippet of the raw "
                "message log, 'Network Representation' holding a small three-node graph, and "
                "'Answer' holding a three-bar 3-D block chart - joined left to right by "
                "arrows labelled 'Extraction' and 'Query'. A process schematic, not a data "
                "plot; the only numbers are the two stage labels.")

    # Improved model - the worked alpha example
    figure(17, 1, "flowchart-or-schematic",
           ctext(17, "Figure 8: The suspicious link contributes more",
                 " The correlation"),
           numbering="Figure N:", panels=2, layout="1x2", labels=True,
           note="Two one-node panels, each an open circle with three thick block arrows "
                "leaving it - one red pointing up and two green to the right and down - "
                "annotated with the link weights and the resulting alpha. Left: 2, 1 and 1 "
                "with alpha_1c = 2/(2+1+1) = 0.5. Right: 0.9, 0.1 and 0 with alpha_1c = "
                "0.9/(0.9+0.1+0) = 0.9. No axes, no data series, no legend; the arithmetic is "
                "printed under each panel.")

    # the appendix exhibit that repeats the Figure 7 number
    figure(19, 1, "node-link-network",
           ctext(19, "Figure 7: The Model of the Infection Cells"),
           numbering="Figure N:", labels=True,
           note="Fifteen numbered cells, 0 to 14, drawn as circles on a grey ramp from near "
                "white to near black with the radius following the same order, joined by thin "
                "straight edges plus long curved arcs and self-loops that sweep outside the "
                "cluster. No axes, no weights, no legend; the grey key is not printed "
                "anywhere. This is the paper's second exhibit numbered Figure 7 - the "
                "workflow on p15 is the first - so both are recorded and the duplicate "
                "numbering is left as printed.")

    rules = [
        "The paper prints two different exhibits both numbered Figure 7, the workflow on p15 "
        "and the infection model on p19, and each is recorded on its own row rather than "
        "renumbered [caption.numbering].",
        "One caption in the paper has no colon after its number - 'Figure 3 Abnormal nodes "
        "observed by correlation ...' - so its numbering reads `Figure N` while every other "
        "figure caption reads `Figure N:` [caption.numbering].",
        "The symbol glossary on p4 carries no printed number and no caption line at all, so "
        "it is counted as a table with an empty caption and `caption_source: none` "
        "[table.rows] [caption.verbatim].",
        "Tables 1 and 3 are two side-by-side blocks under one merged title row reading 'Task "
        "1 Statistics' and 'Task 2 Statistics', so each is one table with a merged cell, not "
        "two [table.merged_cells].",
        "Table 3's in-grid title says Task 2 while its printed caption says 'in Task 1'; the "
        "caption is quoted as printed and the mismatch is stated in the row note "
        "[caption.verbatim].",
        "The paired-bar chart beside Table 4 on p12 is printed with no number and no caption "
        "and is cited by no sentence, so it is recorded with an empty caption and an empty "
        "mention block rather than being folded into the table [mention.count].",
        "Only Figure 1 is cited in running text ('In Figure 1, from the total number of "
        "conversations'); the other fourteen rows are read through their captions alone "
        "[mention.lead_sentence].",
        "Almost every figure in this paper is a pasted raster, so the axis titles are the "
        "only readable scale and several carry tick marks with no tick numbers; those rows "
        "take printed_numbers false even where gridlines appear [geometry.printed_numbers].",
        "The paper prints four headings and none carries a number, so every row is routed to "
        "the unnumbered Introduction section with section_numbered false "
        "[place.section_numbered].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-15356-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Fifteen measured regions, fifteen accounted: ten figure rows for nine numbered "
            "figures plus one uncaptioned chart, and five counted tables for four numbered "
            "tables plus the unnumbered symbol glossary. No region is excluded and no printed "
            "exhibit is missing from the pass. Two exhibits carry the number Figure 7 - the "
            "workflow on p15 and the infection model on p19 - and both are recorded as "
            "printed."
        ),
    }
    out = PROXY / "pb43-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
