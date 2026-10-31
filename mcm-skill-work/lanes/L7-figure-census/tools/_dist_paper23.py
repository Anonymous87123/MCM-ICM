"""Hand pass for P-C-2011-11325-4609137d (EV adoption scenarios, 26 pages).

The paper prints eight figures (3.1-3.8) and five tables (0.1, 2.1, 2.2, 3.1, 3.2). The
geometry pass measures ten regions, which resolve to exactly eight figures and two tables:
every figure has one region, Tables 2.1 and 3.1 are measured, and Tables 0.1, 2.2 and 3.2
leave nothing at 25 pt, so they stay unresolved by name rather than by invented bbox.

Families, read off cropped page proxies:

* Figures 3.1-3.5 are one chart format repeated for five scenarios: four monochrome series
  (Gasoline dashed, BEV solid, PHEV dotted, Total fine-dotted), boxed legend inside the
  bottom-right corner, dashed gridlines on both axes, no axis titles.
* Figures 3.6-3.8 switch to colour, five series (Base, Expensive Coal, Investment,
  Expensive Oil, Best Case) and horizontal solid gridlines only. 3.6 puts its legend to the
  right of the frame, 3.7 inside the top-right corner, 3.8 inside the top-left corner; 3.7
  and 3.8 carry axis titles, 3.6 carries one on the y axis only.

Table caption side splits by family: every table caption prints above its grid, every figure
caption below its exhibit.

Usage: python -I tools/_dist_paper23.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2011-11325-4609137d"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

METHOD = "2 Methodology"
MODEL = "2.1 Mathematical Model"
NUMERIC = "2.1.1 Numerical Method"
RESULTS = "3 Results"
POP = "3.2 Population Model Results"
EMISS = "3.3 Emissions"
CO2 = "3.3.2 CO2"
OIL = "3.4 Oil consumption"
POWER = "3.5 Electricity Demand"

KIND_OF = {METHOD: "model", MODEL: "model", NUMERIC: "model", RESULTS: "solution",
           POP: "solution", EMISS: "evaluation", CO2: "evaluation", OIL: "evaluation",
           POWER: "evaluation",
           "3.2.1 Base Scenario": "solution",
           "3.2.2 Scenario 1: Heavy investment in electric vehicles": "solution",
           "3.2.3 Scenario 2: Electricity becomes more expensive": "solution",
           "3.2.4 Scenario 3: Oil prices rise": "solution",
           "3.2.5 Scenario 4: Best case for BEVs": "solution"}

PATH: dict[int, list[str]] = {
    9: [METHOD, MODEL, NUMERIC],
    12: [RESULTS],
    13: [RESULTS, POP, "3.2.1 Base Scenario"],
    14: [RESULTS, POP, "3.2.2 Scenario 1: Heavy investment in electric vehicles"],
    15: [RESULTS, POP, "3.2.3 Scenario 2: Electricity becomes more expensive"],
    16: [RESULTS, POP, "3.2.4 Scenario 3: Oil prices rise"],
    17: [RESULTS, POP, "3.2.5 Scenario 4: Best case for BEVs"],
    19: [RESULTS, EMISS, CO2],
    20: [RESULTS, OIL],
}


def raw_lines(page: int) -> list[str]:
    return (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()


def joined(page: int, first: int, last: int) -> str:
    return schema.norm(" ".join(raw_lines(page)[first:last + 1]))


CAPTIONS: dict[tuple[str, str], tuple[int, str]] = {
    ("t", "0.1"): (3, joined(3, 39, 39)),
    ("t", "2.1"): (9, joined(9, 3, 3)),
    ("t", "2.2"): (9, "Table 2.2: Definitions of the parameters used and their units."),
    ("f", "3.1"): (13, joined(13, 30, 32)),
    ("t", "3.1"): (12, joined(12, 20, 21)),
    ("f", "3.2"): (14, joined(14, 48, 50)),
    ("f", "3.3"): (15, joined(15, 35, 37)),
    ("f", "3.4"): (16, joined(16, 35, 37)),
    ("f", "3.5"): (17, joined(17, 32, 36)),
    ("t", "3.2"): (18, joined(18, 6, 6)),
    ("f", "3.6"): (19, joined(19, 36, 38)),
    ("f", "3.7"): (20, joined(20, 38, 39)),
    ("f", "3.8"): (20, joined(20, 77, 78)),
}

PROSE = re.compile(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}")
AXIS_TICK = re.compile("−")
TABLE_CELL = re.compile(r"\d+\.\d+")
INLINE_CAPTION = re.compile(r"(Figure|Table)\s+\d+(\.\d+)?\s*[:.]")
RUNHEAD = re.compile(r"\[?Team\s*#?\s*\d+\]?\s*\[?Page\s*\d+\s*of\s*\d+\]?", re.I)


def scan(number: str, kind: str) -> tuple[list[int], list[str], int]:
    num = re.escape(number)
    pats = ([re.compile(rf"(?i)\bfigures?\s+{num}\b"),
             re.compile(rf"(?i)\bfig\.?\s+{num}\b")] if kind == "figure"
            else [re.compile(rf"(?i)\btables?\s+{num}\b")])
    pages: set[int] = set()
    found: list[str] = []
    count = 0
    for page in range(1, LAYOUT["page_count"] + 1):
        text = schema.page_text(PID, page)
        for pat in pats:
            for m in pat.finditer(text):
                pages.add(page)
                found.append(schema.norm(m.group()))
                count += 1
    return sorted(pages), found, count


def lead_sentence(number: str, kind: str) -> tuple[str, str]:
    pat = re.compile(rf"[Ff]igure\s+{number}" if kind == "figure"
                     else rf"[Tt]able\s+{number}")
    for page in range(1, LAYOUT["page_count"] + 1):
        for unit in schema.page_units(PID, page):
            unit = RUNHEAD.sub("", unit)
            if not pat.search(unit) or INLINE_CAPTION.match(unit):
                continue
            hit = next((s for s in schema.sentences(unit)
                        if pat.search(s) and PROSE.search(s)
                        and AXIS_TICK.search(s) is None
                        and len(TABLE_CELL.findall(s)) < 3
                        and INLINE_CAPTION.search(s) is None
                        and s.count("(") < 2), "")
            if not hit:
                continue
            parts = hit.split()
            text = " ".join(parts[:schema.MAX_QUOTE_WORDS])
            while len(schema.words(text)) > schema.MAX_QUOTE_WORDS:
                parts = parts[:-1]
                text = " ".join(parts[:schema.MAX_QUOTE_WORDS])
            low = text.lower()
            if re.search(r"\(fig(ure)?\s+\d+", low) or "(see table" in low \
                    or "(see fig" in low:
                pattern = "parenthetical"
            elif "as shown in" in low:
                pattern = "as-shown-in"
            elif re.match(r"^fig(ure)?\s+\d+\s+shows", low):
                pattern = "figure-n-shows"
            else:
                pattern = "direct"
            return text, pattern
    return "", "none"


def mention(number: str | None, page: int, kind: str = "figure") -> dict:
    if number is None:
        return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}
    pages, found, count = scan(number, kind)
    first = pages[0] if pages else None
    sent, pattern = lead_sentence(number, kind)
    label = "Figure" if kind == "figure" else "Table"
    return {"first_page": first,
            "lead_pages": None if first is None else page - first,
            "style": sorted(set(found)) or [f"{label} {number}"],
            "count": count,
            "lead_sentence": sent, "trail_sentence": "",
            "lead_pattern": pattern,
            "read_sentences": 1 if sent else 0,
            "gap_sentences": None if first is None else abs(page - first)}


def caption_block(text: str, position: str) -> dict:
    numbering = "none"
    m = re.match(r"^(Figure|Table)\s+(\d+(?:\.\d+)?)([:.])?", text)
    if m:
        numbering = {(False, ":"): "Figure N:", (False, "."): "Figure N.",
                     (False, ""): "Figure N", (True, ":"): "Table N:",
                     (True, "."): "Table N.", (True, ""): "Table N"}[
                         (m.group(1) == "Table", m.group(3) or "")]
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": bool(re.search(r"\b(km|kg|MWh|million|per|tons)\b", text)),
        "variables": False,
        "variable_count": 0,
        "conditions": bool(re.search(r"\b(under|with|without|fixed|varying)\b", text)),
        "concludes": bool(re.search(r"\b(which|so that|therefore)\b", text)),
        "voice": "none",
        "position": position,
    }


ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}


def place(page: int, reg: int, order: int) -> dict:
    path = list(PATH[page])
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


def figure(page: int, reg: int, number: str, *, legend: str = "inside",
           labels: bool = False, note: str = "") -> None:
    ORDER.append((page, reg))
    cap_page, text = CAPTIONS[("f", number)]
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": "line",
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention(number, page),
        "caption": caption_block(text, "below"),
        "geometry": {
            "family": "line",
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": True,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, number: str, rows: int, cols: int, *, numeric: int = 0,
          text_cols: int = 1, rule_style: str = "booktabs", zebra: bool = False,
          merged: bool = False, units: bool = False, width: str = "full",
          note: str = "") -> None:
    ORDER.append((page, reg))
    cap_page, cap = CAPTIONS[("t", number)]
    TABLES[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention(number, page, "table"),
        "caption": caption_block(cap, "above"),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": 1,
            "rule_style": rule_style,
            "zebra": zebra,
            "merged_cells": merged,
            "diagonal_header": False,
            "units_in_header": units,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": width,
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    }


def build() -> str:
    table(9, 1, "2.1", 4, 4, numeric=2, text_cols=2,
          note="variable, representation, initial condition and source for the three "
               "population variables; three data rows and no shading")
    table(9, 2, "2.2", 11, 4, numeric=2, text_cols=2,
          note="parameter, variable symbol, value and units for the ten rate and capacity "
               "constants; ten data rows, dimensionless and 1/year units printed in the "
               "units column. Measured only after the fig_extract rule-span fix of "
               "2026-10-23.")
    table(12, 1, "3.1", 11, 3, numeric=3, rule_style="vertical-rules", width="half",
          note="ten perturbation rows against Leaf, Civic and the cost differential; the grid "
               "is fully framed with a vertical rule between every column")
    figure(13, 1, "3.1",
           note="four series on a semi-log axis: Gasoline dashed, BEV solid, PHEV dotted, "
                "Total fine-dotted; y title 'Number of cars (millions)', x title 'Simulation "
                "year'; dashed gridlines both axes; boxed legend inside the bottom-right corner")
    figure(14, 1, "3.2",
           note="same chart format as Figure 3.1 at ten times the initial BEV and PHEV stock")
    figure(15, 1, "3.3",
           note="same format; Gasoline and PHEV run nearly coincident and cross twice")
    figure(16, 1, "3.4",
           note="same format; both the BEV and the PHEV series sit above the base case")
    figure(17, 1, "3.5",
           note="same format; the Total series is the highest curve for most of the range")
    figure(19, 1, "3.6", legend="outside-right",
           note="five colour series (Base, Expensive Coal, Investment, Expensive Oil, Best "
                "Case), y title 'CO2/year (Million Metric Tons)', x title 'Simulation Year', "
                "legend to the right of the frame, solid horizontal gridlines only")
    figure(20, 1, "3.7", legend="inside",
           note="the same five colour series for oil, y title 'Barrels of Oil (in millions)', "
                "x title 'Simulation Year', legend inside the top-right corner")
    figure(20, 2, "3.8", legend="inside",
           note="the same five colour series for electricity, y title 'Electricity Use "
                "(MWh)', x title 'Simulation Year', legend inside the top-left corner")

    rules = [
        "Family follows the ink: eight figures are smoothed multi-series curves with no "
        "markers and no bars, so all eight are line [geometry.family].",
        "Scenarios 1-4 repeat the base-case chart format exactly, so line style, legend "
        "placement and gridlines carry across Figures 3.1-3.5 rather than being re-guessed "
        "per page [geometry.legend].",
        "Legend placement is read off the frame, not off the tick labels: 3.6 sets its keys "
        "beyond the right edge of the axes, 3.7 inside the top-right corner, 3.8 inside the "
        "top-left, and 3.1-3.5 inside the bottom-right [geometry.legend].",
        "Table captions print above their grid and figure captions below their exhibit, so "
        "caption.position splits by family in this paper [caption.position].",
        "Table rules: Tables 2.1 prints three-line booktabs and Table 3.1 is fully framed "
        "with a vertical rule between every column, so rule_style differs per table "
        "[table.rule_style].",
        "No table in this paper shades alternate rows, and none of them merges cells "
        "horizontally [table.zebra].",
        "Numbering is chapter-scoped (Table 2.1, Figure 3.6) with a period after the number "
        "and a colon after the label [caption.numbering].",
        "Prose cites exhibits in running text, most often inside brackets, so lead_pattern "
        "is parenthetical wherever the reference sits in parentheses "
        "[mention.lead_pattern].",
        "Section paths stop at the deepest extracted heading; the printed section 3.1 has no "
        "heading entry, so Table 3.1 carries the chapter path [place.section_path].",
    ]
    note = (
        "Three numbered tables are declared and cited but have no measured region: Table 0.1 "
        "on p3, Table 2.2 on p9 and Table 3.2 on p18. Their rules are drawn too faintly to "
        "clear the 25 pt minimum side, so they are left unresolved rather than given an "
        "invented bbox. Section 3.1 (the economic sensitivity analysis) is printed but never "
        "extracted as a heading, so Table 3.1 sits on the chapter path."
    )
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": [TABLES[k] for k in ORDER if k in TABLES],
        "excluded_regions": [],
        "rules": rules,
        "note": note,
    }
    out = PROXY / "pc23-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, "
          f"{len(payload['tables'])} tables")
    bad = 0
    for (kind, number), (page, text) in CAPTIONS.items():
        try:
            schema.check_quote(text, PID, [page - 1, page, page + 1],
                               f"caption {kind}{number}", limit=None)
        except schema.Bad as exc:
            print("BAD", exc)
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
