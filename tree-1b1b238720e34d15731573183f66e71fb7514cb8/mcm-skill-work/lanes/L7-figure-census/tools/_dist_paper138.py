"""Hand pass for P-E-2017-71672-f2a1a712 (smart growth metric, Boulder and Canberra).

Shape of the paper: a ten-principle metric merged into a fractional success level L, applied to
two cities' current plans, then to two proposed plans, then to each initiative alone. A LaTeX
paper of 23 pages with five printed tables and no figures at all.

What the record has to say out loud:

1. Zero figures. The measurement returns five regions on five pages and every one of them is a
   table. This is the first paper in the lane whose figure list is empty, so `items` is empty and
   the whole record is the table half of the schema.
2. Every table caption prints below its grid and every caption is numbered with a colon
   ("Table 1:"). The colon form is the only numbering this paper uses.
3. The four metric tables are one template four times: a two-column Metric/Value grid of eleven
   data rows whose last row is an italic, ruled-off "L". Only their values differ.
4. Two of those four print their values badly in the text layer. p14 drops the P7 value and p17
   drops the P5 value, so a reader who trusted the text layer would report a one-row misalignment
   that the raster does not print - both grids are clean.
5. Four of the five tables are announced a page before they print (pp8, 10 and 17 for pp9, 11
   and 18), because the floats push to the next page; the two that print on their own page are
   the proposed Boulder and proposed Canberra grids.

Usage: python -I tools/_dist_paper138.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-E-2017-71672-f2a1a712"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((LANE / f".proxy/{PID}-ctx.json").read_text(encoding="utf-8"))

MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}
PAGE_W = LAYOUT["pages"][0]["width"]
PAGE_H = LAYOUT["pages"][0]["height"]

HEAD: dict[str, str] = {}
for _h in CTX["headings"]:
    _n, _l = _h.get("number"), _h.get("label")
    if not _n or not _l or not _l.startswith(_n + " "):
        continue
    if _n not in HEAD:
        HEAD[_n] = _l


def H(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


S_31 = H("3", "3.1")
S_32 = H("3", "3.2")
S_41 = H("4", "4.1")
S_42 = H("4", "4.2")
S_43 = H("4", "4.3")

B = {
    "tab1": (9, [262.5, 131.6, 347.8, 306.8]),
    "tab2": (11, [262.5, 131.6, 347.8, 306.8]),
    "tab3": (14, [262.5, 338.1, 347.8, 512.0]),
    "tab4": (17, [262.5, 183.8, 347.8, 358.9]),
    "tab5": (18, [189.8, 131.6, 420.4, 233.4]),
}

for _name, (_p, _b) in B.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B), f"{len(MEASURED)} measured regions, {len(B)} mapped"


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (PAGE_W * PAGE_H)
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 1,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": False,
    }


def tcap(v: str) -> dict:
    """Every caption here is a 'Table N:' line printed under its grid."""
    return {
        "verbatim": v,
        "numbering": "Table N:",
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": "below",
    }


def mention(page: int, *, first: int | None, style: list[str], lead: str,
            pattern: str, trail: str = "", read: int = 0) -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": 1 if first else 0,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def table(key: str, cap: dict, men: dict, grid: dict, *, path: list[str], kind: str,
          note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, merged: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "column",
         note_sentence: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": "boxed",
        "zebra": False,
        "merged_cells": merged,
        "diagonal_header": False,
        "units_in_header": False,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": False,
        "note_sentence": note_sentence,
    }


TABLES = [
    table("tab1", tcap("Table 1: Table of individual metrics and ﬁnal success level for the "
                       "current growth plan of Boulder, CO, USA"),
          mention(9, first=8, style=["Table 1"], pattern="figure-n-shows",
                  lead="Table 1 summarizes the metrics described above, as well as the ﬁnal "
                       "success level of 0.7753."),
          grid(12, 2, numeric=1, txt=1),
          path=S_31, kind="result",
          note="the Boulder current-plan grid: 'Metric | Value' with eleven data rows P1-P10 and "
               "L, the L row ruled off from the ten principle rows above it and set in italic "
               "rather than bold. Announced at the foot of p8 and floated to the top of p9, so it "
               "prints a page after its own citation. Value 0.7753"),
    table("tab2", tcap("Table 2: Table of individual metrics and ﬁnal success level for the "
                       "current growth plan of Canberra, ACT, AUS"),
          mention(11, first=10, style=["Table 2"], pattern="figure-n-shows",
                  lead="Table 2 summarizes the metrics described above, as well as the ﬁnal "
                       "success level of 0.5882."),
          grid(12, 2, numeric=1, txt=1),
          path=S_32, kind="result",
          note="the same template for Canberra's current plan, cited at the foot of p10 and "
               "printing at the top of p11. Value 0.5882, the lower of the two current plans; its "
               "P3 row (0.2) is the only metric where Canberra beats Boulder on the current plan"),
    table("tab3", tcap("Table 3: Table of individual metrics and ﬁnal success level for our "
                       "proposed growth plan for Boulder, CO, USA"),
          mention(14, first=14, style=["Table 3"], pattern="as-shown-in",
                  lead="The results of our proposed growth plan for Boulder are summarized in "
                       "Table 3, including a computed success level of L = 0.8338",
                  trail="Our proposed growth plan for Canberra includes", read=1),
          grid(12, 2, numeric=1, txt=1),
          path=S_41, kind="solution",
          note="proposed Boulder plan, value 0.8338. The text layer loses the P7 value ('1') and "
               "runs 'P7 P8 1 / P9 0.45', which reads as a one-row misalignment; the raster prints "
               "P7=1 on its own row and every value on its label's row, so the defect is in the "
               "extraction, not the page"),
    table("tab4", tcap("Table 4: Table of individual metrics and ﬁnal success level for our "
                       "proposed growth plan for Canberra, ACT, AUS"),
          mention(17, first=17, style=["Table 4"], pattern="as-shown-in",
                  lead="The results of our proposed development plan for Canberra",
                  trail="We see from the results from the two previous subsections that our plan "
                        "for Boulder results in a higher success level", read=1),
          grid(12, 2, numeric=1, txt=1),
          path=S_42, kind="solution",
          note="proposed Canberra plan, value 0.7443. The text layer loses the P5 value ('0.8') "
               "and prints 'P5 P6 0.8 / P7 0.5706', the opposite shift to Table 3's; the raster is "
               "clean. The announcing sentence is hyphenated across a line break ('summa- rized'), "
               "which is why the quoted lead stops before it"),
    table("tab5", tcap("Table 5: Table of the effects of individual initiatives on success level "
                       "for Boulder, CO, USA and Canberra, ACT, AUS"),
          mention(18, first=17, style=["Table 5"], pattern="as-shown-in",
                  lead="The results are summarized in Table 5, where ∆L is the success level L of "
                       "the city’s current growth plan",
                  trail="We rank our initiatives for Boulder from best to worst in the order E, "
                        "C, D, A, B.", read=1),
          grid(6, 5, header=2, merged=True, decimal=True, numeric=4, txt=1, width="half"),
          path=S_43, kind="result",
          note="the only wide grid: five columns under a two-tier header ('Initiative | Boulder | "
               "Canberra' over 'L ΔL | L ΔL'), five body rows A-E, and the only table in the "
               "paper whose figures share a decimal point. Both signed ΔL columns print their "
               "negatives with a minus sign and align on it. No L row here - the table ends at "
               "initiative E"),
]

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": [],
    "tables": TABLES,
    "excluded_regions": [],
    "rules": [
        "This paper prints no figures at all: all five measured regions are tables, so the "
        "figure list is empty and every geometry field the schema defines is unused here "
        "[table.rows].",
        "All five captions print below their grid, the inverse of the sibling paper three rows "
        "up this queue where every table caption printed above; the side is per paper, never per "
        "table [caption.position].",
        "Every caption is numbered with a colon - 'Table 1:' through 'Table 5:' - and no other "
        "numbering form appears anywhere in the paper [caption.numbering].",
        "All five grids are boxed the same way: top rule, a doubled rule under the header, a rule "
        "between every body row, a closing rule at the foot, and verticals at every cell boundary "
        "[table.rule_style].",
        "No grid is shaded; there is no zebra striping and no coloured cell anywhere in the paper "
        "[table.zebra].",
        "Four of the five tables are one template four times - a two-column Metric/Value grid "
        "with eleven data rows whose last row, L, is ruled off and italicised - so only Table 5 "
        "differs in shape [table.rows].",
        "Only Table 5 carries two header rows, because it needs a city band over an L/ΔL line; "
        "the four metric grids carry a single 'Metric | Value' header [table.header_rows].",
        "Only Table 5 merges cells, spanning each city name over its two value columns; the four "
        "metric grids have no spanning cell [table.merged_cells].",
        "Only Table 5 aligns its figures on a decimal point - the four metric grids centre their "
        "values, so 0.05 and 0.5535 do not share a point column [table.decimal_aligned].",
        "Widths are decided by the number of columns, not by importance: the four metric grids are "
        "a narrow centred block of about 0.14 of the page while Table 5 takes about half the text "
        "width [table.width].",
        "Four of the five tables print a page after the sentence that announces them (pp8, 10 "
        "and 17 for pp9, 11 and 18), and the two that print on their own page are the two "
        "proposed-plan grids [mention.lead_pages].",
        "Each table is named exactly once in the running text and the citation always carries the "
        "number - this paper has no uncited exhibit and no exhibit cited by deixis alone "
        "[mention.count].",
        "Two citation grammars: 'Table N summarizes ...' with the table as subject, and '... are "
        "summarized in Table N' with the table as a prepositional object [mention.lead_pattern].",
        "The house citation form is the capitalised 'Table N' with no colon (the colon belongs to "
        "the caption line only) [mention.style].",
        "Captions run 19 to 20 words and are single sentences of the form 'Table of ... for "
        "<plan> of <city>'; none states a unit, a condition or a conclusion, and all are nominal "
        "phrases with no verb [caption.words].",
        "Two of the four metric grids show a one-row shift in the text layer - p14 drops the P7 "
        "value and p17 drops the P5 value - and in both cases the raster prints every value on its "
        "label's row, so the shift is an extraction artefact and not a printed defect "
        "[table.numeric_cols].",
        "The record carries no note sentences at all: not one of the five grids prints a note "
        "line under it, and the only prose about each table follows it in the running text "
        "[table.note_sentence].",
        "Exhibit size never tracks exhibit importance here - the table that carries the paper's "
        "headline comparison (Table 5) is the largest, but the three plan grids that state the "
        "success levels the abstract quotes are the three smallest at 0.031 of the page each "
        "[place.area_frac].",
        "Each grid belongs to one subsection and follows it: the two current-plan grids under the "
        "result kind of sections 3.1 and 3.2, the two proposed-plan grids under the solution kind "
        "of 4.1 and 4.2, and the initiative comparison back under result in 4.3 "
        "[place.section_kind].",
        "No table continues across a page turn in this paper, even though four of the five floats "
        "move off their announcing page [table.continued].",
    ],
    "note": (
        "A LaTeX paper of 23 pages with five printed tables and no figures at all - the first "
        "paper in this lane whose figure list is empty. All five grids are boxed the same way "
        "(top rule, doubled header rule, a rule between every body row, closing rule, verticals at "
        "every cell boundary), none is shaded, and all five captions print below their grid, the "
        "inverse of the sibling paper three rows up the queue. Four of the five tables are one "
        "two-column Metric/Value template repeated for the two current and two proposed plans, "
        "each with eleven data rows and an italic, ruled-off L row; only Table 5 differs, with a "
        "two-tier header over five columns and the paper's only decimal-aligned figures. Four of "
        "the five print a page after their announcing sentence. Two grids lose a value in the text "
        "layer (P7 on p14, P5 on p17) and both print cleanly in the raster - the only misalignment "
        "this paper has is an extraction artefact."
    ),
}

for _n, _e in enumerate(sorted(TABLES, key=lambda x: x["page"]), 1):
    _e["place"]["page_order"] = 1
    _e["place"]["doc_order"] = _n


def main() -> int:
    from collections import Counter

    print("figures 0 tables", len(TABLES), "excluded 0")
    print("kind", dict(Counter(e["place"]["section_kind"] for e in TABLES)))
    for k in ("position", "numbering", "voice", "words", "sentences", "units", "variables",
              "conditions", "concludes"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in TABLES)))
    for k in ("first_page", "lead_pages", "count", "lead_pattern", "read_sentences"):
        print("mention." + k, dict(Counter(e["mention"][k] for e in TABLES)))
    for k in ("rule_style", "zebra", "merged_cells", "header_rows", "units_in_header",
              "decimal_aligned", "width", "orientation", "continued", "rows", "cols"):
        print("table." + k, dict(Counter(t["table"][k] for t in TABLES)))
    print("area", [e["place"]["area_frac"] for e in TABLES])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
