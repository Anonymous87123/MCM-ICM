"""Hand pass for P-C-2011-10607-6ed4fd93 (electric vs conventional vehicles, 20 pages).

The paper prints eleven numbered figures and ten numbered tables. Every family below was
read off a cropped page proxy; the geometry pass only supplied the rectangles.

Four things drive the record:

* Family by ink. Figures 2, 3 and 4 are 3-D perspective point clouds, so the family is
  scatter (the surface-or-3D family is for rendered surfaces, and this paper prints none).
  Figures 8 and 9 are loss-chain schematics, Figure 1 is a coordinate sketch, so
  flowchart-or-schematic; Figure 10 is a labelled hierarchy graph, so node-link-network;
  Figure 7 is a two-series line chart.
* Table rules. Nine of the ten tables are three-line booktabs with alternating grey bands
  and no vertical rules; only the two AHP matrices (Tables 9 and 10) separate the stub
  column with a heavy vertical rule.
* Every caption prints below its exhibit. Table 1 is the one exception in appearance: the
  title is also repeated as a stub above the grid, but the numbered caption is the one below.
* Four numbered exhibits have no measured region: Figures 5 and 6 (p11), Figure 11 (p19)
  and Table 6 (p10) are declared and cited but leave nothing the extractor measures at
  25 pt. They are left unresolved rather than given invented bboxes.

Usage: python -I tools/_dist_paper22.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2011-10607-6ed4fd93"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

# Section IX is printed on pp. 18-19 but the heading extractor never returns it, so those
# exhibits carry the unnumbered form; the prefix is taken from schema.py itself so the two
# stay in step.
UNNUMBERED = re.search(r'startswith\("(.*?)"\)',
                       (LANE / "tools" / "schema.py").read_text(encoding="utf-8")).group(1)

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

COLLECT = "3.2 Data Collection"
CALC = "3.3 Results of the Calculation"
SENS = "3.4 Sensitivity Analysis"
SIM = "4.1.1.2 Simulation of Gaussian Plume Model"
SIMRES = "4.1.1.3 Results and Discussions of the Simulation"
PRED = "4.1.3 The Statistical Prediction of the Amount of Emissions"
NOISE = "4.2.1 Noise Pollution"
NORTON = "6.3 Results and Conclusion"
ENERGY = "8.1 The Comparison of the Energy Efficiency"
SEC9 = "IX.Determining the Weight of Different Electricity Generation"

KIND_OF = {COLLECT: "other", CALC: "solution", SENS: "sensitivity", SIM: "model",
           SIMRES: "evaluation", PRED: "other", NOISE: "other", NORTON: "evaluation",
           ENERGY: "other", SEC9: "model"}

PATH: dict[int, list[str]] = {
    5: [COLLECT],
    6: [CALC, SENS],
    8: [SIM], 9: [SIMRES], 10: [SIMRES, PRED], 11: [PRED], 12: [NOISE],
    15: [NORTON], 16: [ENERGY], 18: [SEC9], 19: [SEC9],
}

NUMBERED: dict[int, bool] = {5: True, 6: True, 8: True, 9: True, 10: True, 11: True,
                             12: True, 15: True, 16: True, 18: False, 19: False}

# Which heading each exhibit actually sits under, when the page carries two of them.
BELOW: dict[tuple[int, int], str] = {
    (6, 1): CALC, (6, 2): SENS,
    (10, 1): SIMRES, (10, 2): PRED,
}


def raw_lines(page: int) -> list[str]:
    return (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()


def caption_at(page: int, line: int) -> str:
    return schema.norm(raw_lines(page)[line])


CAPTIONS: dict[tuple[str, int], tuple[int, str]] = {
    ("t", 1): (5, caption_at(5, 44)),
    ("t", 2): (6, caption_at(6, 14)),
    ("t", 3): (6, caption_at(6, 33)),
    ("f", 1): (8, caption_at(8, 10)),
    ("t", 4): (8, caption_at(8, 45)),
    ("f", 2): (9, caption_at(9, 23)),
    ("f", 3): (9, caption_at(9, 33)),
    ("f", 4): (10, caption_at(10, 5)),
    ("t", 5): (10, caption_at(10, 34)),
    ("t", 7): (11, caption_at(11, 16)),
    ("t", 8): (12, caption_at(12, 21)),
    ("f", 7): (15, caption_at(15, 5)),
    ("f", 8): (16, caption_at(16, 39)),
    ("f", 9): (16, caption_at(16, 45)),
    ("f", 10): (18, caption_at(18, 14)),
    ("t", 9): (18, caption_at(18, 27)),
    ("t", 10): (19, caption_at(19, 16)),
}

PROSE = re.compile(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}")
AXIS_TICK = re.compile("−")
TABLE_CELL = re.compile(r"\d+\.\d+")
INLINE_CAPTION = re.compile(r"(Figure|Table)\s+\d+\s*[:.]")
RUNHEAD = re.compile(r"\[?Team\s*#?\s*\d+\]?\s*\[?Page\s*\d+\s*of\s*\d+\]?", re.I)


def scan(number: int, kind: str) -> tuple[list[int], list[str], int]:
    pats = ([re.compile(rf"(?i)\bfigures?\s+{number}\b"),
             re.compile(rf"(?i)\bfig\.?\s+{number}\b")] if kind == "figure"
            else [re.compile(rf"(?i)\btables?\s+{number}\b")])
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


def lead_sentence(number: int, kind: str) -> tuple[str, str]:
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
            elif "as shown" in low:
                pattern = "as-shown-in"
            elif re.match(r"^fig(ure)?\s+\d+\s+shows", low):
                pattern = "figure-n-shows"
            else:
                pattern = "direct"
            return text, pattern
    return "", "none"


def mention(number: int | None, page: int, kind: str = "figure") -> dict:
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


def caption_block(text: str) -> dict:
    numbering = "none"
    m = re.match(r"^(Figure|Table)\s+(\d+)([:.])?", text)
    if m:
        numbering = {(False, ":"): "Figure N:", (False, "."): "Figure N.",
                     (False, ""): "Figure N", (True, ":"): "Table N:",
                     (True, "."): "Table N.", (True, ""): "Table N"}[
                         (m.group(1) == "Table", m.group(3) or "")]
    vars_ = 1 if re.search(r"[A-Za-z]\s*[=~]", text) or "_" in text else 0
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": bool(re.search(r"\b(km|kg|dB|million|g|per)\b", text)),
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": bool(re.search(r"\b(under|with|without|fixed|varying)\b", text)),
        "concludes": bool(re.search(r"\b(which|so that|therefore)\b", text)),
        "voice": "none",
        "position": "below",
    }


ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}


def place(page: int, reg: int, order: int) -> dict:
    numbered = NUMBERED[page]
    if numbered:
        path = list(PATH[page])
        head = BELOW.get((page, reg), path[-1])
        path = [h for h in path if path.index(h) <= path.index(head)]
        kind = KIND_OF[head]
    else:
        path = [UNNUMBERED + " " + SEC9]
        kind = KIND_OF[SEC9]
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def figure(page: int, reg: int, family: str, number: int, *, conf: str = "high",
           panels: int = 1, layout: str = "1", legend: str = "none",
           labels: bool = False, shared_axes: bool = False, note: str = "") -> None:
    ORDER.append((page, reg))
    cap_page, text = CAPTIONS[("f", number)]
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": conf,
        "panel_count": panels,
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention(number, page),
        "caption": caption_block(text),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared_axes,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": True,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, number: int, rows: int, cols: int, *, header_rows: int = 1,
          numeric: int = 0, text_cols: int = 1, rule_style: str = "booktabs",
          zebra: bool = True, merged: bool = False, width: str = "full",
          units: bool = False, note: str = "") -> None:
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
        "caption": caption_block(cap),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
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
    table(5, 1, 1, 9, 3, numeric=2, units=True,
          note="Parameters against RAV 4EV and RAV4, eight parameter rows; the title is also "
               "repeated as a stub above the grid, and the numbered caption prints below it")
    table(6, 1, 2, 3, 10, numeric=9,
          note="nine parameter columns against the two vehicles, one header row and two data "
               "rows")
    table(6, 2, 3, 3, 5, numeric=4,
          note="percentage change in LCC per 5% parameter change, two vehicle rows")
    figure(8, 1, "flowchart-or-schematic", 1, labels=True,
           note="z/x/y coordinate sketch of a point source and its pollutant plume; a "
                "geometric drawing with no plotted data")
    table(8, 2, 4, 7, 4, numeric=3,
          note="four vehicle columns, of which the first is the vehicle type and the other "
               "three are CVs and the two EV fuel cycles")
    figure(9, 1, "scatter", 2,
           note="3-D perspective point cloud inside an x/y/z box; no surface is rendered, so "
                "the family is scatter")
    figure(9, 2, "scatter", 3,
           note="the same 3-D box for EVs (thermal power), fewer and lower points")
    figure(10, 1, "scatter", 4,
           note="the same 3-D box for EVs (natural gas), the sparsest cloud of the three")
    table(10, 2, 5, 3, 3, numeric=2,
          note="AP and GHG emissions per km for CVs and EVs, two data rows")
    table(11, 1, 7, 2, 7, numeric=6, zebra=False,
          note="world vehicle stock 2004-2009, one data row; the only unshaded table")
    table(12, 1, 8, 6, 6, header_rows=2, numeric=4, text_cols=2, merged=True,
          note="two-tier header: CVs and EVs each span an inside and an outside column, then "
               "four rows for the two speeds under uniform velocity and acceleration")
    figure(15, 1, "line", 7,
           note="two curves (CVs, EVs) against year; no axis titles and no legend box, the "
                "series are named by inline text on the curves, dotted gridlines at every tick")
    figure(16, 1, "flowchart-or-schematic", 8,
           note="loss chain crude → gasoline/diesel → driving power, with the energy-loss "
                "arrows drawn upward between boxes")
    figure(16, 2, "flowchart-or-schematic", 9,
           note="the same chain for EVs: thermal/nuclear/hydro → electricity → driving power")
    figure(18, 1, "node-link-network", 10, labels=True,
           note="AHP hierarchy: goal node O, five criteria C1-C5, four alternatives P1-P4, "
                "fully connected between criteria and alternatives")
    table(18, 2, 9, 6, 6, numeric=5, rule_style="vertical-rules",
          note="5x5 pairwise judging matrix; the stub column is separated by a heavy vertical "
               "rule, no rule between body rows")
    table(19, 1, 10, 9, 6, header_rows=2, numeric=5, rule_style="vertical-rules", merged=True,
          note="two header rows (criteria C1-C5 then their b_i), seven rows of alternatives and "
               "consistency statistics")

    rules = [
        "Family follows the ink: 3-D perspective point clouds are scatter, not surface-or-3D, "
        "because nothing in them is a rendered surface [geometry.family].",
        "Loss-chain drawings with boxes and arrows are flowchart-or-schematic even when they "
        "carry percentages on the arrows, and a labelled hierarchy with drawn edges is "
        "node-link-network [geometry.family].",
        "Nine of the ten tables are three-line booktabs with no vertical rules; only the two "
        "AHP matrices put a heavy rule between the stub column and the matrix [table.rule_style].",
        "Grey banding is the default: every table shades alternate rows except Table 7, which "
        "prints unshaded [table.zebra].",
        "Grouped headers are counted as header rows, so the noise table and the AHP alternative "
        "table carry two and their shaded bands start below that pair [table.header_rows].",
        "Every caption in this paper prints below its exhibit; Table 1 additionally repeats its "
        "title as a stub above the grid, and that stub is not the caption [caption.position].",
        "The numbering style is a period after the number for both families, with no space in "
        "Figure 10.The hierarchy diagram [caption.numbering].",
        "Prose cites most exhibits with a direct sentence, and occasionally inside brackets, so "
        "lead_pattern is direct except where the reference is parenthetical "
        "[mention.lead_pattern].",
        "Section IX is printed but never extracted as a heading, so those exhibits carry the "
        "unnumbered section form with the title copied from the text layer "
        "[place.section_numbered].",
    ]
    note = (
        "Four numbered exhibits are declared and cited but have no measured region: Figures 5 "
        "and 6 on p11, Figure 11 on p19 and Table 6 on p10. Nothing on those pages clears the "
        "extractor's 25 pt minimum side, so they stay unresolved instead of being given an "
        "invented bbox. Sections IX has no heading entry; its exhibits use the unnumbered form."
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
    out = PROXY / "pc22-payload.json"
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
            schema.check_quote(text, PID, [page - 1, page, page + 1], f"caption {kind}{number}",
                               limit=None)
        except schema.Bad as exc:
            print("BAD", exc)
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
