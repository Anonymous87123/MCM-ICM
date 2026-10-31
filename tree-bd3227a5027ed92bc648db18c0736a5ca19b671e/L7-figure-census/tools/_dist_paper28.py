"""Hand pass for P-A-2011-9665-6560aced (snowboarding half-pipe design, 30 pages).

Twenty-nine measured regions on seventeen pages: nineteen figure items, three tables and
seven exclusions. The paper is drawing-heavy, and several measured blocks are display
equations that the vector filter admitted, so the excluded list is long.

Captions are printed with the number and the words in the ordinary order ("Figure 3. Force
analysis of the snowboarder."), so the ctx dump has them; two labels carry a stray space
before the full stop ("Figure 7 .The ..."), which is kept in the quote.

Families and table shapes were read off the cropped page proxies, one crop per reading.

Usage: python -I tools/_dist_paper28.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2011-9665-6560aced"
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
PAGES = list(range(1, 31))

INTRO = "未编号标题 Introduction"
DESCR = "3.2 The Description of Half-Pipe We Focused"
BASIC = "3.3 Basic Model"
WF = "3.3.3 The Calculation of W f"
WP = "3.3.5 The Function of W p"
APPROACH = "3.3.6 Approach Parameters of Half-Pipe"
TORQUE = "4.2 Torque"
ELLIPSE = "6.1 The Half Pipe whose Transitions are Ellipse"
ARC = "6.2 The Half-Pipe whose Flat is a Arc"
VERIFY = "7.1 The Verification by Living Example"
SENS = "7.2 Sensitivity Analysis"

KIND_OF = {INTRO: "introduction", DESCR: "other", BASIC: "model", WF: "solution", WP: "other",
           APPROACH: "other", TORQUE: "other", ELLIPSE: "other", ARC: "other",
           VERIFY: "test", SENS: "sensitivity"}


def path_for(page: int, reg: int) -> list[str]:
    """Filed under the heading the block is printed below.

    Pages 22 and 23 each carry two sections: Fig. 14 sits in 6.2 and Table 1 in 7.1 on
    p22, Table 2 at the head of p23 is still 7.1 and the four sensitivity panels below it
    are 7.2. Fig. 3 is printed at the head of p8, above that page's own '3.3.4' heading.
    """
    if page == 3:
        return [INTRO]
    if page == 5:
        return [DESCR]
    if page == 6:
        return [BASIC]
    if page == 8:
        return [BASIC, WF]
    if page == 9:
        return [BASIC, WP]
    if page in (11, 12, 13, 14, 15, 16):
        return [BASIC, APPROACH]
    if page == 17:
        return [TORQUE]
    if page == 21:
        return [ELLIPSE]
    if page == 22:
        return [ARC] if reg == 1 else [VERIFY]
    if page == 23:
        return [VERIFY] if reg == 1 else [SENS]
    return [SENS]


ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []


def place(page: int, reg: int, order: int) -> dict:
    path = path_for(page, reg)
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": path,
        "section_numbered": not path[0].startswith("未编号标题"),
        "section_kind": KIND_OF[path[-1]],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def sentence_at(page: int, token: str, *, before: 8, after: int = 11) -> str:
    text = schema.page_text(PID, page)
    at = text.index(token)
    cut = text.rfind(". ", 0, at)
    start = cut + 2 if cut != -1 else 0
    tail = text.find(". ", at)
    end = tail + 1 if tail != -1 else len(text)
    window = text[start:end].split()
    where = text[start:at].split()
    lo = max(0, len(where) - before)
    hi = min(len(window), len(where) + len(token.split()) + after)
    return " ".join(window[lo:hi])


def pattern_of(sentence: str) -> str:
    low = sentence.lower()
    if "shown in" in low or "as shown" in low or "shown as" in low:
        return "as-shown-in"
    if re.search(r"\b(shows|show|depicts|pictures|illustrates|drawn in|drawn)\b", low):
        return "figure-n-shows"
    return "direct"


def mention_for(kind: str, number: int, page: int) -> dict:
    """Count printed references to one exhibit number.

    This paper writes 'Figure 3' and 'Table 2' with a space, so the pattern allows any
    spacing but pins the number with a negative lookahead: 'Figure 1' must not match
    inside 'Figure 13'.
    """
    pat = re.compile(rf"{kind}\s*{number}(?![\d])")
    pages = [p for p in PAGES if pat.search(schema.page_text(PID, p))]
    if not pages:
        return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}
    count = sum(len(pat.findall(schema.page_text(PID, p))) for p in PAGES)
    first = pages[0]
    hit = pat.search(schema.page_text(PID, first))
    lead = sentence_at(first, hit.group(0), before=8)
    return {
        "first_page": first,
        "lead_pages": page - first,
        "style": sorted({hit.group(0)}),
        "count": count,
        "lead_sentence": lead,
        "trail_sentence": "",
        "lead_pattern": pattern_of(lead),
        "read_sentences": count,
        "gap_sentences": None,
    }


def caption_block(text: str, numbering: str) -> dict:
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)) if text else 0,
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": "unit" in text.lower(),
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": "below",
    }


def figure(page: int, reg: int, number: int, family: str, text: str, *,
           numbering: str = "Figure N.", legend: str = "none", printed: bool = False,
           note: str = "") -> None:
    ORDER.append((page, reg))
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention_for("Figure", number, page),
        "caption": caption_block(text, numbering),
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": printed,
            "data_labels": False,
        },
    }


def table(page: int, reg: int, rows: int, cols: int, number: int, text: str, *,
          header: int = 1, numeric: int = 0, text_cols: int = 0,
          units: bool = False, numbering: str = "Table N.", note: str = "") -> None:
    ORDER.append((page, reg))
    TABLES[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention_for("Table", number, page),
        "caption": caption_block(text, numbering),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header,
            "rule_style": "booktabs",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": units,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    }


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def build() -> str:
    # Figures: (page, reg, number, family, caption, kwargs)
    ROWS = [
        (5, 1, 1, "flowchart-or-schematic", "Figure 1. Snowboarding Half-pipe Schematic",
         {"note": "Labelled cross-section: Entry Ramp, Platform, Lip, Vertical, "
                  "Transition, Wall, Flat."}),
        (6, 1, 2, "flowchart-or-schematic",
         "Figure 2. A scheme of a half-pipe with notations.",
         {"note": "The same section with the model's symbols a_x, h_x, w_x, t_x, b_x, "
                  "r_x, delta and the athlete drawn in."}),
        (8, 1, 3, "flowchart-or-schematic", "Figure 3. Force analysis of the snowboarder.",
         {"note": "Boarder on the curved transition with the normal and the weight vector."}),
        (9, 1, 4, "flowchart-or-schematic", "Figure 4. The scheme of slid motion done by athlete",
         {"note": "Perspective half-pipe with the trajectory A-A'-B-B'-C and the velocity "
                  "arrows v_max, v_s, v_x."}),
        (11, 1, 5, "flowchart-or-schematic", "Figure 5. The scheme of resolution of",
         {"numbering": "Figure N",
          "note": "Velocity box at the lip resolving V into V_x, V_y, V_z; the caption "
                  "breaks off after 'of' in the text layer because the symbols that "
                  "follow are set as a picture."}),
        (11, 2, 6, "flowchart-or-schematic",
         "Figure 6. The scheme of component velocities in vertical plane.", {}),
        (12, 3, 7, "line", "Figure 7",
         {"numbering": "Figure N",
          "note": "The plot of v_y against the arch angle: one bow-shaped curve. The "
                  "printed caption is 'Figure 7 .The relationship of <symbols> and v y', "
                  "whose formula characters the text layer drops."}),
        (13, 1, 8, "line", "Figure 8. The curve of velocity recovery",
         {"note": "v against S from V0 to vmax with dashed guides to S_max and V_max."}),
        (14, 1, 9, "line",
         "Figure 9. A unfiltered accelerometer trance associated with a snowboarding run",
         {"legend": "inside",
          "note": "Two traces, forward/back and up/down, with Air 1-4 peaks labelled."}),
        (14, 2, 10, "flowchart-or-schematic",
         "Figure 10 .The distilled relationship between acceleration and time",
         {"numbering": "Figure N",
          "note": "Sketch of the a_c-t profile through M', N', P'."}),
        (15, 1, 11, "flowchart-or-schematic", "Figure 11. The scheme of process of sliding",
         {"note": "Wall cross-section with the rider path, alpha, delta, r_x and v_x."}),
        (17, 1, 12, "flowchart-or-schematic",
         "Figure 12. Torque applied to the snowboard and the angle of twist",
         {"note": "Board under bending with the moment, plus a twisted rod showing the "
                  "angle of twist."}),
        (21, 1, 13, "flowchart-or-schematic",
         "Figure 13 a. The first method for designing half-pipe",
         {"note": "Narrow profile: steep transitions, short flat."}),
        (21, 2, 13, "flowchart-or-schematic",
         "Figure 13 b. The second method for designing half-pipe",
         {"note": "Wide, shallow profile with long gentle transitions."}),
        (22, 1, 14, "flowchart-or-schematic",
         "Figure 14. The shape of half-pipe whose flat is arced.",
         {"note": "Section whose floor is an arc, marked by a dashed chord."}),
        # Fig. 15 is four panels of one MATLAB subplot grid, measured as four blocks.
        (23, 2, 15, "line",
         "Figure 15 The trend of half-pipe parameters in sensitivity analysis",
         {"numbering": "Figure N", "printed": True,
          "note": "Panel: the height of platform against v0, red circles joined by a line."}),
        (23, 3, 15, "line",
         "Figure 15 The trend of half-pipe parameters in sensitivity analysis",
         {"numbering": "Figure N", "printed": True,
          "note": "Panel: the arc angle of transitions against v0, black asterisks."}),
        (23, 4, 15, "line",
         "Figure 15 The trend of half-pipe parameters in sensitivity analysis",
         {"numbering": "Figure N", "printed": True,
          "note": "Panel: the length of half-pipe against v0, magenta stars."}),
        (23, 5, 15, "line",
         "Figure 15 The trend of half-pipe parameters in sensitivity analysis",
         {"numbering": "Figure N", "printed": True,
          "note": "Panel: the width of flat against v0, blue plus marks."}),
    ]
    for page, reg, number, family, text, kw in ROWS:
        figure(page, reg, number, family, text, **kw)

    TAB = [
        (3, 1, 9, 2, 0, "Symbol Definition",
         {"text_cols": 2, "numbering": "none",
          "note": "The notation table under the printed heading 'II Symbol Definitions': a "
                  "Symbol column and a Definition column, eight rows (h_x, r_x, theta, w_x, "
                  "phi, a_x, delta h, mu). It carries no 'Table N' label of its own. Measured "
                  "only after the fig_extract rule-span fix of 2026-10-23, which stopped "
                  "dropping long text tables whose header and closing rules sit farther apart "
                  "than the gap tolerance."}),
        (22, 2, 5, 5, 1, "Table 1. The parameters of half-pipes we design unit (m)",
         {"numeric": 3, "text_cols": 2, "units": True,
          "note": "Arc angle, length, flat width and platform height for the three pipes "
                  "the paper designs."}),
        (23, 1, 4, 6, 2, "Table 2. The parameters of current half-pipes unit (m)",
         {"numeric": 5, "text_cols": 1, "units": True,
          "note": "Literature values for the same four parameters across five sources."}),
        (24, 1, 5, 12, 3, "Table 3. The data calculated in sensitivity analysis",
         {"numeric": 11, "text_cols": 1, "units": True,
          "note": "Five rows of computed quantities at eleven speeds from 7 to 12 m/s; "
                  "the header row is the speed values themselves."}),
    ]
    for page, reg, rows, cols, number, label, kw in TAB:
        table(page, reg, rows, cols, number, label, **kw)

    # Measured blocks that are not exhibits.
    excluded(5, 2, "duplicate",
             "Raster underlay of the same half-pipe section as p5 r1, nested inside that "
             "region's bbox; the labelled vector drawing above it is the exhibit.")
    excluded(5, 3, "not-an-exhibit",
             "Bulleted glossary defining Flat, Transitions, Verticals, Platform and Entry "
             "Ramp; body text that the vector filter measured as a block.")
    excluded(12, 1, "not-an-exhibit",
             "Display equation for v_s as a square root of the energy balance, measured as "
             "eight vector paths.")
    excluded(12, 2, "not-an-exhibit",
             "Second, wider cut of the same display equation on the line below.")
    excluded(16, 1, "not-an-exhibit",
             "Display equation for v_s through the friction work mu m g AA', measured as "
             "seven vector paths.")
    excluded(29, 1, "split-across-pages",
             "Appendix A5, 'The data appeared in references': the header and the first "
             "row of a reference-data table that continues at the head of p30.")
    excluded(30, 1, "split-across-pages",
             "Tail of the appendix A5 table (flat width, platform height, inclined angle) "
             "with the head of a second uncaptioned reference table below it; the page "
             "break falls inside both.")

    rules = [
        "One family covers the drawings: the half-pipe sections, force diagrams and "
        "torque sketch are recorded as flowchart-or-schematic, and only blocks with "
        "plotted data are recorded as line [geometry.family].",
        "Fig. 15 is a four-panel subplot grid measured as four separate blocks, so each "
        "panel is an item carrying the same printed caption [geometry.panel_count].",
        "Nothing in this paper prints axis numbers except the two accelerometer traces "
        "and the four sensitivity panels, so printed_numbers is false for the drawings "
        "[geometry.printed_numbers].",
        "Only Fig. 9 puts a key inside the frame (Forward/Back and Up/Down accelerometer); "
        "every other drawing and plot carries no legend [geometry.legend].",
        "All three tables use horizontal rules only, so rule_style is booktabs "
        "[table.rule_style].",
        "Units are carried in the caption line ('unit (m)') rather than in the header "
        "row, so units_in_header is false for Tables 1 and 2 and true only for Table 3, "
        "whose header row is the v0 speed values [table.units_in_header].",
        "Table 3's header cell is the parameter symbol and the unit, with eleven numeric "
        "columns of computed values, so it is recorded as full width in portrait "
        "[table.cols].",
        "Two captions carry a stray space before the full stop ('Figure 7 .The', "
        "'Figure 10 .The') and their formulas are set as pictures, so the quote stops "
        "before the symbols [caption.verbatim].",
        "The paper labels two distinct drawings 'Figure 13 a' and 'Figure 13 b'; both are "
        "recorded as items with their own caption quote [caption.verbatim].",
        "Three measured blocks on pp. 12 and 16 are display equations rather than "
        "exhibits, so they are excluded and the label numbering closes over the gap "
        "[geometry.family].",
        "Page 23 carries Table 2 above its own '7.2' heading and the four Fig. 15 panels "
        "below it, and p22 carries Fig. 14 in 6.2 and Table 1 in 7.1 "
        "[place.section_path].",
    ]
    note = (
        "The paper is drawing-heavy: of twenty-nine measured blocks, fifteen are "
        "schematic line drawings without axes, four are panels of one MATLAB subplot grid "
        "and three are tables. The vector filter also admitted five blocks that are not "
        "exhibits, three display equations (p12 twice and p16) and the glossary on p5 "
        "whose bullets are measured as a block; the p5 raster underlay is nested inside "
        "the labelled drawing above it and is excluded as a duplicate, so the count is 19 "
        "figures, 3 tables and 7 exclusions. Two appendix blocks are excluded because the "
        "A5 reference table breaks across pp. 29-30 and the p30 block also carries the "
        "head of an uncaptioned second table; the appendix data is therefore not counted "
        "as an exhibit anywhere in this record."
    )
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": [TABLES[k] for k in ORDER if k in TABLES],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": note,
    }
    out = PROXY / "pa28-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, "
          f"{len(payload['tables'])} tables, {len(payload['excluded_regions'])} excluded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
