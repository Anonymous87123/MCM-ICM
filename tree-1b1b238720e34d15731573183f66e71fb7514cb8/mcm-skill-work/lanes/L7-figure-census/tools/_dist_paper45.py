"""Hand pass for P-C-2012-17160-8b6c54d2 (a circuit-analogy ranking of the 83 employees plus a
clustering model, 23 pp).

This paper prints no figures at all: every exhibit is a table. The geometry pass measures ten
regions over nine pages, and the paper prints six numbered tables plus one unnumbered appendix
listing that runs over three pages, so the accounting is

    6 numbered tables + 3 appendix fragments = 9 table rows, plus one formula block excluded.

    p7-r1   Table 1   whether each duplicated name lands in one cluster, for k = 2 to 5
    p8-r1   Table 2   what the two clusters hold for k = 2, by p2p, p2t and both
    p14-r1  Table 3   the 15 guiltiest unknowns, original data against Chris/Topic 1 guilty
    p16-r1  Table 4   the 10 guiltiest unknowns, once per known conspirator left out
    p16-r2  Table 5   the 10 guiltiest unknowns, once per known topic left out
    p17-r1  Table 6   the same ranking with duplicated names kept apart against merged
    p21-r1  appendix  the listing of all 82 employees, first fragment
    p22-r1  appendix  the listing continued
    p23-r1  appendix  the listing, last seven entries

Excluded: the displayed conductance formula on p10, which is set as a block of vector type
rather than artwork - `in-body-diagram` on the paper 41 and mcm-65 precedent.

Caption positions: every numbered caption prints below its grid. The appendix listing has no
caption line at all - only the appendix title and a lead-in paragraph - so its three rows carry
an empty caption and `caption_source: none`.

Usage: python -I tools/_dist_paper45.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2012-17160-8b6c54d2"
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

CLUSTER = "4 Clustering Model"
VALID = "4.3 Validating Parameters"
RESULTS = "6 Results of Model"
IMMEDIATE = "6.1 Immediate Results"
ROBUST = "6.2 Robustness of Results"
LEAVE = "6.2.1 Leave-One-Out Testing"
MERGE = "6.2.2 Merging Repeated Names"
APPENDIX = "未编号标题 A Complete Listing of Results"

PATH = {
    7: [CLUSTER, VALID],
    8: [CLUSTER, VALID],
    14: [RESULTS, IMMEDIATE],
    16: [RESULTS, ROBUST, LEAVE],
    17: [RESULTS, ROBUST, MERGE],
    21: [APPENDIX],
    22: [APPENDIX],
    23: [APPENDIX],
}
NUMBERED = {p: p not in (21, 22, 23) for p in PATH}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# recorded regions per page, counted first so doc_order stays monotonic
VENTION = {7: 1, 8: 1, 14: 1, 16: 2, 17: 1, 21: 1, 22: 1, 23: 1}

ORDER: list[tuple[int, int]] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}

APP_RULE = "boxed"


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
        "section_numbered": NUMBERED[page],
        "section_kind": "other" if not NUMBERED[page] else HEADKIND[route[-1]],
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


def table(page: int, reg: int, caption: str, *, numbering: str, rows: int, cols: int,
          rule_style: str, numeric_cols: int, text_cols: int,
          header_rows: int = 1, merged: bool = False, continued: bool = False,
          caption_source: str = "text-layer", position: str = "below",
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
    table(7, 1,
          ctext(7, "Table 1: The table below shows", " with node 38 Beth"),
          numbering="Table N:", rows=6, cols=5, rule_style="boxed",
          numeric_cols=4, text_cols=1,
          mention_block=mention(6, ["Table 1"], "The results are shown in Table 1", "direct"),
          note="A 5 by 5 grid of the words 'same' and 'different': column headings k = 2 to 5 "
               "across, the five duplicated names Elsie, Jerome, Gretchen, Beth and Neal down "
               "the stub. A double vertical rule stands between the stub and the first data "
               "column, and every row and column is closed. The caption prints below the grid "
               "and is a two-sentence statement of purpose rather than a title.")

    table(8, 1,
          ctext(8, "Table 2: The composition of clusters", " know to be guilty"),
          numbering="Table N:", rows=4, cols=3, rule_style="boxed",
          numeric_cols=0, text_cols=3,
          mention_block=mention(8, ["Table 2"],
                                "For k = 2 clusters, we get the results shown in Table 2",
                                "direct"),
          note="Three columns - a blank stub, then Cluster 1 and Cluster 2 - over three rows "
               "for p2p, p2t and both. Every cell is a phrase of the form '5 guilty, 2 "
               "innocent [7 total]', so the grid is textual; the caption states that too much "
               "is known about the clusters to read them as numbers.")

    table(14, 1,
          ctext(14, "Table 3: The 15 guiltiest employees", " The left half shows"),
          numbering="Table N:", rows=17, cols=6, rule_style="booktabs",
          numeric_cols=4, text_cols=2, merged=True,
          mention_block=mention(13, ["Table 3"],
                                "In Table 3 we list the results from our model for two cases",
                                "direct"),
          note="Two three-column blocks, 'Node # | Name | Guilt (V)', under italic group "
               "headings 'Chris Innocent, Topic 1 unknown' and 'Chris and Topic 1 Guilty'. "
               "Fifteen rows each, ranked by guilt from 51 Dayi at 1 down to 69 Han at 0.8748 "
               "on the right. Horizontal rules only - above the group headings, under the "
               "column headings and under the last row - with no verticals.")

    table(16, 1,
          ctext(16, "Table 4: The 10 guiltiest people", " The person left out"),
          numbering="Table N:", rows=12, cols=16, rule_style="boxed",
          numeric_cols=8, text_cols=8, merged=True,
          mention_block=mention(15, ["Table 4"],
                                "The results for leaving out known conspirators is shown in "
                                "Table 4", "direct"),
          note="Eight Name/Guilt (V) blocks side by side in two bands of four - None, Harvey, "
               "Yao and Jean over Paul, Alex, Elsie and Ulf - each band under its own italic "
               "group heading, ten ranked rows below. Sixteen physical columns by twelve rows. "
               "Closed box, every row and column ruled. The person left out is named in the "
               "group heading and the same ten names repeat across all eight blocks.")

    table(16, 2,
          ctext(16, "Table 5: The 10 guiltiest people", " The topic left out"),
          numbering="Table N:", rows=12, cols=8, rule_style="boxed",
          numeric_cols=4, text_cols=4, merged=True,
          mention_block=mention(15, ["Table 5"],
                                "those for leaving out known conspiratorial topics is shown in "
                                "Table 5", "direct"),
          note="Four Name/Guilt (V) blocks - None, Topic 7, Topic 11, Topic 13 - under one "
               "italic group-heading row, ten ranked rows below. Eight physical columns by "
               "twelve rows, closed box. Topic 13 is the only block where the ranking changes "
               "high up: Seeni leads the unknowns at 0.9157 instead of Fanti.")

    table(17, 1,
          ctext(17, "Table 6: The left side of the table", " we frequently exchanged"),
          numbering="Table N:", rows=12, cols=4, rule_style="boxed",
          numeric_cols=2, text_cols=2, merged=True,
          note="Two Name/Guilt (V) blocks, 'Not Merged' and 'Merged', under italic group "
               "headings with ten ranked rows below. The two rankings separate only from the "
               "fifth place down - Phille rises to fourth once the repeated names are merged. "
               "No sentence cites this table; the discussion runs on without naming it.")

    # the appendix listing: one table over three pages, no caption line anywhere
    table(21, 1, "", numbering="none", rows=34, cols=3, rule_style=APP_RULE,
          numeric_cols=2, text_cols=1, caption_source="none",
          note="The appendix listing under the unnumbered title 'A Complete Listing of "
               "Results': a header row 'Node # | Name | Guilt (V)' over thirty-three ranked "
               "employees, from 7 Elsie at 1 down to 36 Priscilla at 0.7724. The entries in "
               "italics at the head and foot are the people given to be guilty or innocent. "
               "No caption line prints anywhere on the page - only the appendix title and a "
               "lead-in paragraph - so the caption is empty.")
    table(22, 1, "", numbering="none", rows=42, cols=3, rule_style=APP_RULE,
          numeric_cols=2, text_cols=1, caption_source="none", continued=True,
          note="The listing continued: forty-two more ranked rows, 29 Wayne at 0.7708 down to "
               "0 Chris at 0. No header row prints on this page - the grid resumes straight "
               "under the page header - and there is no caption. The last entry is italic, "
               "being one of the employees given to be innocent.")
    table(23, 1, "", numbering="none", rows=7, cols=3, rule_style=APP_RULE,
          numeric_cols=2, text_cols=1, caption_source="none", continued=True,
          note="The last seven entries of the listing, all at V = 0 and all in italics, with "
               "no header row - 2 "
               "Paige, 48 Darlene, 64 Tran, 65 Jia, 68 Ellin, 74 Gard, 78 Este. No header row "
               "and no caption. The three fragments together carry the whole 82-employee "
               "listing the appendix promises.")

    EXCLUDED.append({
        "page": 10,
        "bbox": REG[(10, 1)],
        "reason": "in-body-diagram",
        "note": "The displayed node-to-topic conductance formula, c_ni,tj = Itopics(m)(tj) x "
                "1{ni in {tx(m), rx(m)}} summed over m in M, set as a block of vector type "
                "inside the running text of 5.2.3. A displayed equation, not an exhibit: no "
                "number, no caption, no surrounding frame.",
    })

    rules = [
        "Every exhibit in this paper is a table - no figure prints anywhere - so "
        "`family_counts` is `table-grid` alone [caption.verbatim].",
        "The appendix listing runs over three pages as one table with no caption line at all; "
        "each measured fragment is its own row with an empty caption, and the later two carry "
        "`continued` [table.continued].",
        "Table 3 prints horizontal rules only, above the group headings, under the column "
        "headings and under the last row, with no verticals, so its rule style is `booktabs` "
        "against `boxed` everywhere else in the paper [table.rule_style].",
        "Tables 4, 5 and 6 are several Name/Guilt blocks side by side under one group-heading "
        "row, so `cols` is the physical grid - 16, 8 and 4 - and `merged_cells` is true "
        "[table.cols].",
        "Table 2's cells are phrases ('5 guilty, 2 innocent [7 total]') rather than numbers, so "
        "its numeric column count is zero [table.numeric_cols].",
        "The caption of every numbered table prints below the grid and states its purpose in "
        "full sentences, which is why five of the six run past twenty words [caption.position].",
        "The displayed conductance formula on p10 is a block of vector type inside the running "
        "text, excluded `in-body-diagram` rather than counted as an exhibit; every counted "
        "exhibit here is a ruled grid [table.rule_style].",
        "Table 6 is never cited in running text - the discussion moves on without naming it - "
        "so its mention block is empty [mention.count].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "C-17160-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Ten measured regions, ten accounted: nine table rows for six numbered tables and "
            "three fragments of the unnumbered appendix listing, plus the p10 conductance "
            "formula excluded as `in-body-diagram`. The paper prints no figures at all, so the "
            "item list is empty and `family_counts` is `table-grid` nine. The appendix has no "
            "caption line - only the unnumbered title 'A Complete Listing of Results' and a "
            "lead-in paragraph - so its three rows carry empty captions."
        ),
    }
    out = PROXY / "pb45-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
