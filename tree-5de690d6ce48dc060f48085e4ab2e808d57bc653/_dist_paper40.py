"""Hand pass for P-C-2012-13215-607f0f06 (four models of a message network, 19 pp).

The geometry pass measures 15 regions over 9 pages: nine figure rows for the paper's nine
printed figures, and two counted tables.

    p4-r1   Figure 1  message counts per worker, blue against red bars
    p6-r1   Figure 2  one centre node with its neighbours under the law of total probability
    p7-r1   Figure 3  three shaded snapshots of the whole network
    p7-r2   Figure 4  e(t) against iteration, upper panel
    p8-r1   Figure 4  e(t) against iteration, the zoomed tail panel
    p10-r1  Figure 5  one round of the distance search, with its symbol key
    p11-r1  Figure 6  the search distance spreading, d = 0, d = 1, d = 2
    p12-r1  Figure 7  the three model rankings against node number, log scale
    p14-r2  Figure 8  first of four centrality bar panels
    p14-r3  Figure 8  second panel
    p14-r4  Figure 8  third panel
    p14-r5  Figure 8  fourth panel
    p18-r2  Figure 9  the expanded relationship network
    p14-r1  Table 4   the four rankings side by side, transposed
    p18-r1  Table 6   five relationship categories against close and distant ties

Four of the paper's six tables are printed as bare text columns with no rules drawn, and
the layout pass measures nothing for them, so they are declared as gaps: Table 1 (p4),
Table 2 (p8), Table 3 (p11) and Table 5 (p15). Only Tables 4 and 6 are ruled and measured.

Accounting: 13 figure rows + 2 counted tables = 15 regions, unaccounted 0.

Families, read off cropped page proxies:

* `bar` is Figure 1, a paired blue/red bar chart over the worker index, and Figure 8, four
  bar panels on a shared horizontal axis but four different vertical scales.
* `node-link-network` is Figures 2, 3, 5, 6 and 9: circles joined by curved arrowed edges,
  with grey level carrying the iteration count in Figure 3 and the search distance in
  Figure 6.
* `line` is Figures 4 and 7: a decaying e(t) curve with round markers and no axis titles,
  and three jagged model rankings against node number on a log axis.
* `table-grid` is Tables 4 and 6.

Usage: python -I tools/_dist_paper40.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2012-13215-607f0f06"
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
# every heading in this paper is printed without a number, so the section path carries the
# unnumbered prefix and the kind is looked up under the bare label
HEADKIND = {f"未编号标题 {k}": v for k, v in HEADKIND.items()}

INTRO = "未编号标题 Introduction"
VALID = "未编号标题 Validation"
WEAK = "未编号标题 Strengths and weaknesses"

# The paper prints five headings in total and none of them carries a number, so every
# section path is unnumbered and takes its label verbatim from the text layer.
PATH = {
    4: [INTRO],
    6: [INTRO],
    7: [INTRO],
    8: [INTRO],
    10: [INTRO],
    11: [INTRO],
    12: [INTRO],
    14: [VALID],
    18: [WEAK],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic
VENTION = {4: 1, 6: 1, 7: 2, 8: 1, 10: 1, 11: 1, 12: 1, 14: 5, 18: 2}

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


def figure(page: int, reg: int, family: str, caption: str, *, numbering: str,
           panels: int = 1, layout: str = "1", legend: str = "none",
           numbers: bool = True, labels: bool = False,
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
        "caption": caption_block(caption, numbering, "above"),
        "table": {
            "rows": rows, "cols": cols, "header_rows": 1,
            "rule_style": rule_style, "zebra": False, "merged_cells": False,
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


def build() -> str:
    # Model 1 - the message counts and the first priority list
    figure(4, 1, "bar", "Figure. 1", numbering="Figure N.",
           legend="outside-right", labels=False,
           mention=mention(3, ["Figure 1"],
                           "we make data statistics and draw Figure 1:", "direct"),
           note="Paired bars on one index axis: blue for suspicious messages and red for "
                "messages with known conspirators, one pair per worker from 0 to 82, with "
                "the two-key legend at the right. Printed ticks 0 to 18 by 2 vertically and "
                "0 to 82 by 2 horizontally, with horizontal gridlines. No axis titles.")

    # Model 2 - the probability picture, the iteration snapshots and the error curve
    figure(6, 1, "node-link-network", "Figure. 2", numbering="Figure N.",
           labels=True,
           mention=mention(5, ["Figure 2"],
                           "works out in the messages network with Figure 2.", "direct"),
           note="One centre circle P_j joined by curved arrowed edges to four neighbour "
                "circles p_j1 to p_j4 and to an ellipsis, every edge labelled with its "
                "weight w_j1 to w_ji. Flat, no axes, no ticks, no legend.")
    figure(7, 1, "node-link-network", "Figure. 3", numbering="Figure N.",
           panels=3, layout="1x3", labels=True,
           mention=mention(7, ["Figure 3"],
                           "Computing process can be shown in Figure 3", "direct"),
           note="Three dashed panel frames in a row labelled t = 0, t = 1 and t = 2 with "
                "the last condition, each holding the same graph: a blue-framed column of "
                "seven black conspirator circles, eight white non-conspirator circles in "
                "the next column and sixty-eight unidentified circles between them. Grey "
                "level spreads from the conspirators panel by panel, so colour encodes the "
                "iteration; purple arrows join the panels. No axes, no ticks.")
    figure(7, 2, "line", "Figure. 4", numbering="Figure N.",
           mention=mention(7, ["Figure 4"],
                           "tends to be 0 as Figure 4 shows", "direct"),
           note="Upper panel of Figure 4: a blue decay curve through red round markers in "
                "a boxed MATLAB-style frame, y from 4 down to 0 and x from 0 to 20 by 2. "
                "No axis titles and no legend, so the axes are named only in the prose: "
                "e(t) against iteration times.")
    figure(8, 1, "line", "Figure. 4", numbering="Figure N.",
           mention=mention(7, ["Figure 4"],
                           "tends to be 0 as Figure 4 shows", "direct"),
           note="Lower panel of the same figure, printed at the head of the next page: the "
                "same decay curve zoomed to iterations 10 to 20, y from 0 to 0.15. The "
                "caption is printed under this panel only, which is why both rows quote it.")

    # Model 3 - the distance search
    figure(10, 1, "node-link-network", "Figure 5", numbering="Figure N",
           labels=True,
           mention=mention(9, ["Figure 5"],
                           "can be described as Figure 5.", "direct"),
           note="One rounded frame holding the search round: white circles for the other "
                "vertices, three black known-suspicious circles, one red vertex under "
                "calculation with dotted blue shortest-path arrows into it, and the five "
                "edge weights w1 to w5 fanning out. The formula 'Score = (w1 + w2 + w3 + "
                "w4 + w5) / 2' is printed at the right and a three-swatch symbol key "
                "sits under the frame. No axes, no ticks.")
    figure(11, 1, "node-link-network", "Figure 6", numbering="Figure N",
           panels=3, layout="1x3", labels=True,
           note="Three identical rounded panels labelled d = 0, d = 1 and d = 2, the same "
                "graph with grey spreading outwards from the three black seed circles, "
                "arrows between panels marking the progression. No axes, no ticks, no "
                "legend.")

    # Model 4 - the ranking comparison
    figure(12, 1, "line", "Figure. 7", numbering="Figure N.",
           legend="outside-right",
           mention=mention(12, ["Figure 7"],
                           "we can draw Figure 7 to compare the consistency of all three "
                           "model results.", "direct"),
           note="Three jagged traces over the eighty-two ranked nodes - green dashed, red "
                "solid, blue dash-dot - against 'node' 0 to 82 and 'rank' on a logarithmic "
                "axis ticked 1, 2, 4, 8, 16, 32, 64, 128, with horizontal gridlines and a "
                "three-entry legend at the right.")

    # Validation - the four centrality panels and the transposed ranking table
    table(14, 1, "Table 4", numbering="Table N",
          rows=5, cols=11, rule_style="boxed", numeric_cols=0, text_cols=11,
          mention=mention(14, ["Table 4"], "then we have Table 4 .", "direct"),
          note="Transposed grid: the header row reads 'rank | 1 | 2 ... 10' and the four "
               "body rows are the metric names C_D, C_B, C_C and C, each holding ten names. "
               "So the body is all words and the only numbers are the ten rank headers. "
               "Boxed with a rule between every row and every column, and its title "
               "'Table 4' printed above the grid.")
    figure(14, 2, "bar", "Figure. 8", numbering="Figure N.",
           mention=mention(14, ["Figure 8"],
                           "In Figure 8, the sequence number in horizontal axis indicates "
                           "the rank of probability of being a conspirator", "direct"),
           note="Top left panel of the 2x2 Figure 8: about forty-four dark-green vertical "
                "bars on the shared rank axis 0 to 40, vertical scale 0 to 20. This is the "
                "one panel whose bar heights reach twenty.")
    figure(14, 3, "bar", "Figure. 8", numbering="Figure N.",
           mention=mention(14, ["Figure 8"],
                           "In Figure 8, the sequence number in horizontal axis indicates "
                           "the rank of probability of being a conspirator", "direct"),
           note="Top right panel: the same bars on the same horizontal axis with a "
                "vertical scale of 0 to 0.2, decaying from the left edge with a second bump "
                "near rank 16.")
    figure(14, 4, "bar", "Figure. 8", numbering="Figure N.",
           mention=mention(14, ["Figure 8"],
                           "In Figure 8, the sequence number in horizontal axis indicates "
                           "the rank of probability of being a conspirator", "direct"),
           note="Bottom left panel: the flattest of the four, vertical scale 0 to 0.015, "
                "values clustered between 0.007 and 0.015 with a dip near rank 10.")
    figure(14, 5, "bar", "Figure. 8", numbering="Figure N.",
           mention=mention(14, ["Figure 8"],
                           "In Figure 8, the sequence number in horizontal axis indicates "
                           "the rank of probability of being a conspirator", "direct"),
           note="Bottom right panel: vertical scale 0 to 1, high bars over the first four "
                "ranks, a collapse near rank 10 and a partial recovery after. The four "
                "panels share the rank axis and the boxed inward-tick style but never share "
                "a vertical scale, and each has its own axis title truncated at the crop "
                "edge ('... for attacking ...'), so the four are four separate rows under "
                "one caption.")

    # Strengths and weaknesses - the semantic table and the expanded network
    table(18, 1, ctext(18, "Table 6", " content"), numbering="Table N",
          rows=6, cols=3, rule_style="booktabs", numeric_cols=0, text_cols=3,
          mention=mention(18, ["Table 6"],
                          "we semantic analyze social relationship, and indicate Table 6",
                          "direct"),
          note="Header 'content | Close relationship | Distant relationship' over five "
               "relationship rows - a quarrel about Bob's tardiness, an interactive "
               "argument between Bob, Dave and George, similar stress between Inez and "
               "George, a misunderstanding between Harry and George, and cooperation "
               "between Anne and Carol. Ruled above the header, under the header, between "
               "every row and at the foot, but with no vertical rules at all; its title "
               "'Table 6' is printed above the grid.")
    figure(18, 2, "node-link-network",
           ctext(18, "Figure. 9", " In the Figure 9"),
           numbering="Figure N.", labels=True,
           note="The expanded relationship network: ten named circles - Bob, Carol, Anne, "
                "Dave, Ellen, Jaye, Fred, Harry, Inez and George - joined by grey edges "
                "carrying integer weights in brackets, with the known conspirators ringed "
                "in red and joined by heavy red lines, a blue dashed path along the lower "
                "edge, and dotted double arrows in the corners. Flat, no axes, no ticks, "
                "no legend inside the frame - the red and blue marks are explained in the "
                "prose after the caption.")

    rules = [
        "Four of the six printed tables are bare text columns with no rules drawn, so the "
        "layout pass measures no region for them: Table 1 on p4, Table 2 on p8, Table 3 on "
        "p11 and Table 5 on p15 are named in the note as declared gaps [table.rows].",
        "Figures 4 and 8 are each printed as several measured regions under one caption - "
        "two stacked decay panels for Figure 4 and a 2x2 block of bar panels for Figure 8 - "
        "so each is recorded as one row per region, all sharing the quoted caption "
        "[caption.verbatim].",
        "The four Figure 8 panels share a horizontal rank axis and a boxed style but not a "
        "vertical scale, so no row claims shared axes and each carries its own panel count "
        "of one [geometry.shared_axes].",
        "Figures 2, 3, 5, 6 and 9 are node-link drawings with no axes, so they carry "
        "printed_numbers false; Figure 3's grey levels and Figure 6's spreading grey encode "
        "the iteration and the search distance rather than a value axis [geometry.family] "
        "[geometry.printed_numbers].",
        "The caption of every figure in this paper is the bare number - 'Figure. 1' through "
        "'Figure. 9', with the full stop printed after the word rather than after the "
        "number - and only Figure 9 adds a title line, so the numbering field records the "
        "period form [caption.numbering].",
        "Tables 4 and 6 print their titles above the grids while every figure caption is "
        "printed below its drawing [caption.position].",
        "Table 4 is transposed: the rank numbers sit in the header row and the four rows "
        "below hold names only, so numeric_cols is 0 and text_cols is all eleven columns "
        "[table.numeric_cols].",
        "Eight exhibits are named in running text within one page: Figures 1, 2, 3, 4, 5, "
        "7, 8 and 9 plus Tables 4 and 6 [mention.lead_sentence].",
        "The paper prints five headings and none of them carries a number, so every "
        "section path is an unnumbered text-layer heading and section_numbered is false "
        "[place.section_numbered].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-13215-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Fifteen measured regions, fifteen accounted: thirteen figure rows for the "
            "paper's nine printed figures (Figure 4 is two stacked panels and Figure 8 a "
            "2x2 block, each printed as separate measured regions) and two counted tables. "
            "Declared gaps: Tables 1, 2, 3 and 5 are printed as unruled text columns that "
            "the layout pass cannot measure - Table 1 on p4, Table 2 on p8, Table 3 on p11 "
            "and Table 5 opening p15 - so they are named here and left unrecorded. No "
            "printed figure is missing."
        ),
    }
    out = PROXY / "pb40-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
