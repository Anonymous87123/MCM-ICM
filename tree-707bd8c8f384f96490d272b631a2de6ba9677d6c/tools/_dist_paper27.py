"""Hand pass for P-C-2011-9089-838e50df (What will Electric Vehicle Bring to the World?, 20 pages).

Twenty-nine measured regions: thirteen figures, fifteen tables and one fragment of Table 1
that continues onto p2. Every exhibit in this paper is labelled as "Figure.N" or "Table.N"
with a full stop between the word and the number, a form the caption pattern in
context_extract.py does not match, so the ctx dump reports captions=0 and mentions=0 and
both were rebuilt here from the page text by hand.

Families, table shapes and legends were read off the cropped page proxies, one crop per
reading.

Usage: python -I tools/_dist_paper27.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2011-9089-838e50df"
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
PAGES = list(range(1, 21))

SOL = "2 Solutions"
IMP = "2.1 Impacts of Widespread use of EVs"
ECO = "2.1.1 Economical Impacts"
ENV = "2.1.2 Environmental Impacts"
HEALTH = "2.1.3 Health Impacts Resulted from Environmental Changes"
SOCIAL = "2.1.4 Social Effects"
KEYS = "2.1.7 Key Factors"
FOSSIL = "2.2 Reduction of Fossil Fuels Using"
GRID = "2.3 Optimization of Energy Grid"

KIND_OF = {SOL: "solution", IMP: "other", ECO: "other", ENV: "other",
           HEALTH: "result", SOCIAL: "other", KEYS: "other", FOSSIL: "other",
           GRID: "other"}


def path_for(page: int, reg: int) -> list[str]:
    """Filed under the heading the region is printed below.

    Two pages split across a heading: p14 carries Table 15 and Figure 10 (section 2.2)
    above its own '2.3' heading and the AHP structure below it, and page 5 carries
    Figures 4 and 5 above '2.1.2' (which sits two thirds of the way down the text).
    """
    if page == 1:
        return [SOL]
    if page in (3, 4, 5):
        return [SOL, IMP, ECO]
    if page in (6, 8):
        return [SOL, IMP, ENV]
    if page == 9:
        return [SOL, IMP, HEALTH]
    if page == 10:
        return [SOL, IMP, SOCIAL]
    if page == 12:
        return [SOL, IMP, KEYS]
    if page == 13:
        return [SOL, FOSSIL]
    if page == 14:
        return [SOL, FOSSIL] if reg <= 2 else [SOL, GRID]
    return [SOL, GRID]


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
        "section_numbered": True,
        "section_kind": KIND_OF[path[-1]],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def sentence_at(page: int, token: str, *, before: int = 8, after: int = 11) -> str:
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
    if "shown in" in low or "shown as" in low:
        return "as-shown-in"
    if re.search(r"\b(shows|show|depicts|pictures|illustrates|exhibit)\b", low):
        return "figure-n-shows"
    return "direct"


def mention_for(token: str, page: int) -> dict:
    """Count the printed references to one exhibit label.

    The label is written 'Figure.N' with a full stop and no space, so the pattern is
    escaped literally and pinned with a negative lookahead: 'Figure.1' must not match
    inside 'Figure.10'.
    """
    pat = re.compile(re.escape(token) + r"(?!\d)")
    pages = [p for p in PAGES if pat.search(schema.page_text(PID, p))]
    if not pages:
        return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}
    count = sum(len(pat.findall(schema.page_text(PID, p))) for p in PAGES)
    first = pages[0]
    lead = sentence_at(first, token)
    return {
        "first_page": first,
        "lead_pages": page - first,
        "style": [token],
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
        "units": "Unit:" in text,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": "above",
    }


def figure(page: int, reg: int, label: str, family: str, text: str, *,
           legend: str = "none", printed: bool = True,
           other_note: str = "", note: str = "") -> None:
    ORDER.append((page, reg))
    n = len(ORDER)
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, n),
        "mention": mention_for(label, page),
        "caption": caption_block(text, "Figure N."),
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
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, rows: int, cols: int, label: str, *,
          header: int = 1, numeric: int = 0, text_cols: int = 0,
          units: bool = False, note: str = "") -> None:
    ORDER.append((page, reg))
    TABLES[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": label,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention_for(label.split(" ")[0], page),
        "caption": caption_block(label, "Table N."),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header,
            "rule_style": "boxed",
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
    # Figures: (page, reg, label token, family, caption, kwargs)
    ROWS = [
        (3, 1, "Figure.1", "line", "Figure.1 Global EV Numbers",
         {"note": "Seven annual points, 2000-2006, diamond markers."}),
        (4, 1, "Figure.2", "line", "Figure.2 Predicted Global EV Sales",
         {"note": "Fitted projection 2010-2020 with fine 'I'-shaped error bars."}),
        (4, 2, "Figure.3", "bar", "Figure.3 Predicted Global Number of EVs",
         {"note": "Ten blue columns, one per year 2011-2020."}),
        (5, 1, "Figure.4", "line", "Figure.4 Predicted Oils Import in USA", {}),
        (5, 2, "Figure.5", "line", "Figure.5 Ratio of Crude Oil Price to Natural Gas Price",
         {"legend": "inside",
          "note": "'History' and 'Projections' are labelled inside the panel, split at 2007."}),
        (6, 5, "Figure.6", "bar", "Figure.6 the Value of E",
         {"note": "Yearly columns 1970-2008, y in millions."}),
        (8, 1, "Figure.7", "bar",
         "Figure.7 Projection of Global Vehicle Number against Global EV Number",
         {"legend": "outside-right"}),
        (8, 2, "Figure.8", "bar",
         "Figure.8 Prediction of CO2e Emission in the Next Decade (Unit: Million Tons)",
         {"legend": "outside-right", "printed": False,
          "note": "Two bar series per year, 2011-2020; the y axis carries ticks but no "
                  "printed numbers."}),
        (10, 1, "Figure.9", "flowchart-or-schematic",
         "Figure.9 Relationship around Social impacts", {"printed": False,
          "note": "Box hierarchy: Social Impacts branching to Social Benefits and Social "
                  "Costs, three leaf boxes under each."}),
        (14, 2, "Figure.10", "bar", "Figure.10 Oils Savings in the Next Decade",
         {"note": "Ten columns, 2011-2020, y in billion barrels."}),
        (14, 3, "Figure.11", "flowchart-or-schematic", "Figure.11 AHP Structure",
         {"printed": False,
          "note": "Overall Evaluation Index branching up into Environment, Society, "
                  "Business and Individuals."}),
        # The paper prints 'Figure.11' twice: the AHP structure above and this chart on
        # p17. Both are recorded under their printed label.
        (17, 1, "Figure.11", "other",
         "Figure.11 Amount and Type of Electricity Generation in 2020 in USA",
         {"printed": False,
          "other_note": "Exploded 3-D doughnut of four generation slices, labelled by "
                        "outside callouts (Hydropower 7%, Wind Power 3%, Thermal Power "
                        "66%, Nuclear Power 24%)."}),
        (17, 2, "Figure.12", "line",
         "Figure.12 Amount and Type of Electricity Generation in the Next Decade in USA",
         {"legend": "outside-right",
          "note": "Four series 2011-2020: thermal, nuclear, hydropower, wind."}),
    ]
    for page, reg, label, family, text, kw in ROWS:
        figure(page, reg, label, family, text, **kw)

    # Tables: (page, reg, rows, cols, caption, kwargs)
    TAB = [
        (1, 1, 3, 2, "Table.1 Contrasts among Three Types of EVs",
         {"numeric": 0, "text_cols": 2,
          "note": "Header plus the HEV and PHEV rows; the BEV row is printed on p2 and is "
                  "excluded as a split continuation."}),
        (4, 3, 3, 11, "Table.2 Production and Import of Oil in USA (Unit: Thousand Barrels Daily)",
         {"numeric": 10, "text_cols": 1, "units": True}),
        (6, 1, 2, 4, "Table.3 Emissions of One CV(Unit: g/km)",
         {"numeric": 4, "text_cols": 0, "units": True}),
        (6, 2, 2, 4, "Table.4 Emissions of a Typical Plant (Unit: g/kW·h)",
         {"numeric": 4, "text_cols": 0, "units": True}),
        (6, 3, 2, 5, "Table.5 Emissions of a Typical Plant (Unit: %)",
         {"numeric": 5, "text_cols": 0, "units": True}),
        (6, 4, 2, 4, "Table.6 Indirect Emissions of One EV (Unit: g/km)",
         {"numeric": 4, "text_cols": 0, "units": True}),
        (9, 1, 11, 3, "Table.7 Savings of Healthcare Costs by Different Energy Grid",
         {"numeric": 1, "text_cols": 2}),
        (10, 2, 4, 4, "Table.8 Costs and Benefits of Electric Vehicles",
         {"numeric": 2, "text_cols": 2}),
        (10, 3, 7, 3, "Table.9 DMU Terms", {"numeric": 1, "text_cols": 2}),
        (12, 1, 4, 4, "Table.10 Results of Sensitivity Analysis",
         {"numeric": 2, "text_cols": 2}),
        (13, 1, 4, 10, "Table.11 Consumption of CV",
         {"numeric": 9, "text_cols": 1,
          "note": "Two stacked half-tables of nine years each; the unit is printed as "
                  "'10^11 J per vehicle' but the exponent is lost in the text layer."}),
        (13, 2, 2, 11, "Table.12 Scenario One’s Consumption (Unit: billion barrels)",
         {"numeric": 10, "text_cols": 1}),
        (13, 3, 4, 10, "Table.13 CV’s Mileage (Unit: km)",
         {"numeric": 9, "text_cols": 1,
          "note": "Two stacked half-tables of nine years each."}),
        (13, 4, 2, 11, "Table.14 Scenario Two’s Consumption (Unit: billion barrels)",
         {"numeric": 10, "text_cols": 1}),
        (14, 1, 2, 11, "Table.15 Oils Savings Estimated (Unit: billion barrels)",
         {"numeric": 10, "text_cols": 1}),
    ]
    for page, reg, rows, cols, label, kw in TAB:
        table(page, reg, rows, cols, label, **kw)

    excluded(2, 1, "split-across-pages",
             "The BEV row of Table 1, printed alone at the head of p2 because the table "
             "runs off p1; the measured block carries no header row of its own.")

    rules = [
        "Every exhibit label is printed as 'Figure.N' or 'Table.N' with a full stop and "
        "no space, which the caption pattern in context_extract.py does not match, so "
        "all captions were typed in from the page text [caption.verbatim].",
        "The numbering field uses the closest closed-enum member, 'Figure N.' and "
        "'Table N.', while the verbatim quote keeps the paper's own 'Figure.N' form "
        "[caption.numbering].",
        "Captions are printed above their exhibits on every page of this paper, so "
        "position is above for figures and tables alike [caption.position].",
        "Family follows the ink: the column charts on pp. 4, 6, 8 and 14 are recorded as "
        "bar, the two box-and-arrow diagrams as flowchart-or-schematic, and the 3-D "
        "doughnut on p17 as other [geometry.family].",
        "The p17 doughnut is a single exploded 3-D pie with callout labels rather than a "
        "plotted chart, so it carries an other_note naming its form [geometry.family].",
        "Legend position was read per block: Figs. 7, 8 and 12 put a key outside at the "
        "right, Fig. 5 labels its two segments inside the panel, and the remaining charts "
        "and diagrams carry no key [geometry.legend].",
        "Fig. 8's y axis carries tick marks but no printed numbers, so printed_numbers is "
        "false for that block [geometry.printed_numbers].",
        "Every table is enclosed by a full outer frame with inner rules, so rule_style is "
        "boxed [table.rule_style].",
        "Tables 11 and 13 are each printed as two stacked half-tables with a repeated "
        "Year header row, so they are recorded as four rows of nine year-columns plus the "
        "row label [table.rows].",
        "Units sit in the caption line ('Unit: g/km', 'Unit: billion barrels'), not in the "
        "header row, so units_in_header is false throughout [table.units_in_header].",
        "Table 1 runs off p1 and prints its last row alone at the head of p2, which is why "
        "the recorded block carries only the header and two type rows [table.rows].",
        "The paper prints two different exhibits as 'Figure.11' (the AHP structure on p14 "
        "and the 2020 generation mix on p17); both keep their printed label in the caption "
        "quote [caption.verbatim].",
        "Pages 14 and 5 each carry a heading below some of their exhibits, so the p14 "
        "table and bar chart are filed under 2.2 and the AHP diagram under 2.3, and both "
        "p5 charts under 2.1.1 rather than under 2.1.2 [place.section_path].",
    ]
    note = (
        "The whole caption layer of this paper is invisible to context_extract.py: labels "
        "are written 'Figure.1' and 'Table.1', with a full stop between the word and the "
        "number, and the caption pattern expects the number directly after the word. The "
        "ctx dump therefore reports captions=0 and mentions=0, and both were rebuilt by "
        "hand from the page text, including the reference counts, which use the same "
        "literal 'Figure.N' token. Twenty-nine measured regions resolve to thirteen "
        "figures, fifteen tables and one excluded strip: Table 1 runs off the foot of p1 "
        "and prints its BEV row alone at the head of p2. The paper also reprints the label "
        "'Figure.11' on p17 for a different exhibit than the AHP structure that already "
        "carried it on p14. Table 11's unit prints as '10^11 J per vehicle', whose exponent "
        "is lost in the text layer, so the caption quote stops at the title."
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
    out = PROXY / "pc27-payload.json"
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
