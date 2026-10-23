"""Hand pass for P-B-2011-9440-95f0fa40 (radio repeater network in mountainous Utah, 41 pages).

The paper prints fifteen numbered figures and ten numbered tables. Every family below was
read off a cropped page proxy; the geometry pass only supplied the rectangles.

Five things drive the record:

* Family split on the placement drawings. Figures 4, 6, 7 and 11 carry only point markers on
  a unitless -40..40 frame and are recorded as scatter; Figures 5 and 12 tile the disc with
  unfilled polygon cells and are recorded as map-or-plan-view; Figures 2, 3 and 1 are
  hexagon geometry diagrams, so flowchart-or-schematic. Figures 8, 9 and 10 are labelled
  nodes joined by drawn edges (a graph, its two spanning trees, its two route sets), so
  node-link-network. Figures 13 and 14 are line charts, Figure 15 is a terrain raster.
* Long tables. Table 4 (p17-p18) is measured as ten narrow horizontal fragments, Table 2
  (p14-p15), Table 6 (p26-p29), Table 8 (p30-p32), Table 9 (p38-p39) and Table 10 (p39-p40)
  each continue onto a later page or page band. One record per exhibit: the caption-bearing
  region is the table, every further fragment is excluded as split-across-pages, and
  `continued` is set on the row count of the whole table.
* Overlapping regions. The small raster rectangles measured inside Table 2's diagram column
  (p14 r2-r4, p15 r2-r9) are that table's own cells; they are excluded as fragment-of-other
  so the table is not double counted.
* Caption strings. Several captions are split by the typesetter (Figure 13's "Naï ve",
  Figure 14's three-way column split). Each quote is the longest run of printed lines that
  is still a substring of the page text; Figure 14 needs the short form because its full
  caption interleaves with the facing column.
* Placement. Pages 19-23 print axis tick numbers that the heading extractor reads as
  headings ("0 R1 R6", "20 R8 R11"); the section path is taken from the printed running
  order instead of that index.

Usage: python -I tools/_dist_paper21.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2011-9440-95f0fa40"
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

SECTION = "4 Analysis"
SUBSECTION = "4.4 Naïve Solution"
MODEL = "3 Model"
COMM = "4.1 Communication Radius"
ALGO = "5 Algorithm"
SIM = "6 Simulation Results"
SIM1000 = "6.3 N=1000, R=40"
SIM10000 = "6.4 N=10000, R=40"
SENS = "7 Sensitivity Analysis"
SENS71 = "7.1 Sensitivity of Parameters"
SENS72 = "7.2 User Density Fluctuation"
SENS73 = "7.3 Effects of Landscape: Discussing the Mountainous Areas"
CONCL = "8 Conclusion and Discussion"

KIND_OF = {MODEL: "model", SECTION: "result", COMM: "other", SUBSECTION: "solution",
           ALGO: "solution", SIM: "solution", SIM1000: "other", SIM10000: "other",
           SENS: "sensitivity", SENS71: "sensitivity", SENS72: "other", SENS73: "other",
           CONCL: "evaluation"}

PATH: dict[int, list[str]] = {
    7: [MODEL],
    10: [SECTION, COMM],
    14: [SECTION, SUBSECTION], 15: [SECTION, SUBSECTION], 16: [SECTION, SUBSECTION],
    17: [SECTION, SUBSECTION], 18: [SECTION, SUBSECTION],
    19: [ALGO], 20: [ALGO], 21: [ALGO], 22: [ALGO], 23: [ALGO],
    24: [SIM], 25: [SIM], 26: [SIM],
    29: [SIM, SIM1000], 30: [SIM, SIM10000],
    33: [SENS, SENS71], 34: [SENS, SENS72], 35: [SENS, SENS73],
    38: [CONCL], 39: [CONCL],
}


def raw_lines(page: int) -> list[str]:
    return (PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace").splitlines()


def joined(page: int, first: int, last: int) -> str:
    """Printed caption lines, first to last inclusive, as one normalised string."""
    return schema.norm(" ".join(raw_lines(page)[first:last + 1]))


CAPTIONS: dict[tuple[str, int], str] = {
    ("f", 1): joined(7, 11, 12),
    ("t", 1): joined(10, 22, 22),
    ("t", 2): joined(14, 21, 23),
    ("f", 2): joined(16, 26, 29),
    ("t", 3): joined(17, 3, 3),
    ("t", 4): joined(17, 20, 22),
    ("f", 3): joined(18, 26, 28),
    ("f", 4): joined(19, 44, 45),
    ("f", 5): joined(19, 83, 83),
    ("f", 6): joined(20, 52, 55),
    ("f", 7): joined(21, 50, 52),
    ("f", 8): joined(22, 41, 42),
    ("f", 9): joined(22, 76, 78),
    ("f", 10): joined(23, 63, 65),
    ("f", 11): joined(24, 33, 36),
    ("t", 5): joined(25, 3, 3),
    ("f", 12): joined(26, 26, 28),
    ("t", 6): joined(26, 30, 30),
    ("t", 7): joined(29, 19, 19),
    ("t", 8): joined(30, 3, 3),
    ("f", 13): joined(33, 20, 23),
    # Figure 14's caption is set in three interleaved column pieces; only this run is a
    # contiguous substring of the page, so the short form is what can be quoted.
    ("f", 14): ("Figure 14: The Comparison between the least numbers of required repeaters "
                "obtained by the ve solution."),
    ("f", 15): joined(36, 3, 4),
    ("t", 9): joined(38, 11, 11),
    ("t", 10): joined(39, 25, 25),
}

PROSE = re.compile(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}")
AXIS_TICK = re.compile("−")
TABLE_CELL = re.compile(r"\d+\.\d+")
INLINE_CAPTION = re.compile(r"(Figure|Table)\s+\d+\s*[:.]")
RUNHEAD = re.compile(r"Team\s*#\s*\d+\s*Page\s*\d+\s*/\s*\d+\s*", re.I)


def spellings(number: int, kind: str) -> list[re.Pattern]:
    if kind == "figure":
        return [re.compile(rf"(?i)\bfigures?\s+{number}\b"),
                re.compile(rf"(?i)\bfig\.?\s+{number}\b")]
    return [re.compile(rf"(?i)\btables?\s+{number}\b")]


def scan(number: int, kind: str) -> tuple[list[int], list[str], int]:
    """Pages that name the exhibit, the spellings used on them, and the raw hit count."""
    pats = spellings(number, kind)
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
            if re.search(r"\(fig(ure)?\s+\d+", low) or "(see fig" in low \
                    or "(see table" in low:
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
    on_page = sorted({f for f in found if f"{number}" in f}) if found else []
    sent, pattern = lead_sentence(number, kind)
    return {"first_page": first,
            "lead_pages": None if first is None else page - first,
            "style": on_page or [f"{'Figure' if kind == 'figure' else 'Table'} {number}"],
            "count": count,
            "lead_sentence": sent, "trail_sentence": "",
            "lead_pattern": pattern,
            "read_sentences": 1 if sent else 0,
            "gap_sentences": None if first is None else abs(page - first)}


def caption_block(text: str, position: str) -> dict:
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
        "units": bool(re.search(r"\b(m|miles|MHz|dB|W|%)\b", text)),
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": bool(re.search(r"\b(under|with|without|fixed|varying)\b", text)),
        "concludes": bool(re.search(r"\b(which|so that|therefore)\b", text)),
        "voice": "none",
        "position": position,
    }


ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}
ORDER: list[tuple[int, int]] = []


def place(page: int, reg: int, order: int) -> dict:
    path = PATH[page]
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": list(path),
        "section_numbered": True,
        "section_kind": KIND_OF[path[-1]],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def figure(page: int, reg: int, family: str, panels: int, conf: str, number: int, *,
           layout: str = "1", legend: str = "none", labels: bool = False,
           shared_axes: bool = False, note: str = "") -> dict:
    ORDER.append((page, reg))
    text = CAPTIONS[("f", number)]
    return {
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
        "caption": caption_block(text, "below"),
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
          numeric: int = 0, text: int = 2, rule_style: str = "boxed",
          zebra: bool = True, units_in_header: bool = False, width: str = "full",
          continued: bool = False, note: str = "") -> dict:
    ORDER.append((page, reg))
    cap = CAPTIONS[("t", number)]
    return {
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
            "header_rows": header_rows,
            "rule_style": rule_style,
            "zebra": zebra,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": units_in_header,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text,
            "width": width,
            "orientation": "portrait",
            "continued": continued,
            "note_sentence": "",
        },
    }


EXCLUDED: list[dict] = []


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def build() -> str:
    ITEMS[(7, 1)] = figure(
        7, 1, "flowchart-or-schematic", 1, "high", 1, labels=True,
        note="one user u1, the circle of radius r around it and the repeaters inside that "
             "circle; a geometry diagram rather than a plotted data set")
    TABLES[(10, 1)] = table(
        10, 1, 1, 23, 6, numeric=3, text=3, zebra=False,
        note="three Call No./ERP pairs repeated across the page, 22 callsign rows under one "
             "header row; no shading, every cell bordered")
    TABLES[(14, 1)] = table(
        14, 1, 2, 14, 3, numeric=2, text=1, continued=True,
        note="M against the best covering radius for M=1..13; rows 6-13 continue on p15, where "
             "the diagram column is drawn with an extra spacer rule, so the physical grid there "
             "reads as four columns while the header has three")
    ITEMS[(16, 1)] = figure(
        16, 1, "flowchart-or-schematic", 1, "high", 2,
        note="twelve repeater points on the centres of a regular hexagon grid inside the "
             "40-mile circle; raster paste")
    TABLES[(17, 1)] = table(
        17, 1, 3, 13, 6, numeric=5, text=1,
        note="one header row over two lines for the two frequency columns, twelve repeater rows")
    TABLES[(17, 2)] = table(
        17, 2, 4, 13, 4, numeric=4, text=0, rule_style="booktabs", continued=True,
        note="two side-by-side blocks of M and best radius, one rule under the header and "
             "row separation by shading only; the geometry pass measured the body as ten "
             "narrow fragments (p17 r2-r9, p18 r1-r2), all but the first excluded")
    ITEMS[(18, 3)] = figure(
        18, 3, "flowchart-or-schematic", 1, "high", 3,
        note="108-repeater hexagonal cellular network as vector hexagons with the 40-mile "
             "circle inscribed; no plotted data")
    ITEMS[(19, 1)] = figure(
        19, 1, "scatter", 1, "high", 4, labels=True,
        note="30 labelled repeater sites R1-R30 on a unitless -40..40 frame")
    ITEMS[(19, 2)] = figure(
        19, 2, "map-or-plan-view", 1, "medium", 5, labels=True,
        note="the same 30 sites with the Voronoi partition drawn as unfilled polygon edges: "
             "the ink is a planar subdivision, not a set of markers")
    ITEMS[(20, 1)] = figure(
        20, 1, "scatter", 1, "high", 6, labels=True,
        note="the same configuration with the circumscribed circle of every Voronoi area and "
             "the centres marked; markers and circles over a bare coordinate frame")
    ITEMS[(21, 1)] = figure(
        21, 1, "scatter", 1, "medium", 7, labels=True,
        note="circles plus one annotation arrow per site showing the direction of movement")
    ITEMS[(22, 1)] = figure(
        22, 1, "node-link-network", 1, "high", 8, labels=True,
        note="21 repeater nodes Rp1-Rp21 joined by a green edge wherever two repeaters are "
             "within R; a nearly complete graph")
    ITEMS[(22, 2)] = figure(
        22, 2, "node-link-network", 2, "high", 9, layout="1x2", labels=True,
        shared_axes=True,
        note="panels (a) maximum spanning tree and (b) minimum spanning tree of the same graph, "
             "each labelled on its own -40..40 frame")
    ITEMS[(23, 1)] = figure(
        23, 1, "node-link-network", 2, "high", 10, layout="1x2", labels=True,
        shared_axes=True,
        note="panels (a) and (b) show the signal routes left in the maximum and the minimum "
             "spanning tree: blue reserved edges and red dashed removed edges over the graph")
    ITEMS[(24, 1)] = figure(
        24, 1, "scatter", 1, "medium", 11,
        note="11-repeater solution pasted as a raster: repeater points and the small red "
             "circles of their receiving range inside the 40-mile circle")
    TABLES[(25, 1)] = table(
        25, 1, 5, 12, 6, numeric=5, text=1,
        note="header plus the eleven repeaters of the Figure 11 solution")
    ITEMS[(26, 1)] = figure(
        26, 1, "map-or-plan-view", 1, "high", 12, note="104-site Voronoi tessellation of the disc, "
        "sites unlabelled, cells drawn as red polygon walls inside the blue boundary")
    TABLES[(26, 2)] = table(
        26, 2, 6, 105, 6, numeric=5, text=1, continued=True,
        note="header plus the 104 repeaters, continued over p27, p28 and p29 (rows 16-104), "
             "each continuation excluded as split-across-pages")
    TABLES[(29, 2)] = table(
        29, 2, 7, 12, 6, numeric=5, text=1,
        note="header plus the eleven repeaters of the 6.3 solution; same coordinates as Table 5 "
             "with different frequencies and PL tones")
    TABLES[(30, 1)] = table(
        30, 1, 8, 105, 6, numeric=5, text=1, continued=True,
        note="header plus the 104 repeaters of the 6.4 solution, continued over p31 and p32 "
             "(rows 40-104)")
    ITEMS[(33, 1)] = figure(
        33, 1, "line", 1, "high", 13, legend="inside",
        note="three series (proposed algorithm, naïve solution 1, naïve solution 2): "
             "least number of repeaters against the number of users")
    ITEMS[(34, 1)] = figure(
        34, 1, "line", 1, "high", 14, legend="inside",
        note="normalised repeater count M/max M against the user communication range r, one "
             "curve for N=1000 and one for N=10000")
    ITEMS[(35, 1)] = figure(
        35, 1, "photo-or-raster-image", 1, "high", 15,
        note="aerial raster of mountain ridges and a valley settlement with four tower icons "
             "and red line-of-sight arrows drawn over it; caption printed at the top of p36")
    TABLES[(38, 1)] = table(
        38, 1, 9, 27, 3, numeric=2, text=1, zebra=False, continued=True,
        note="Parameter / Brief Description / Value-Range, 19 parameter rows here and 7 more "
             "on p39 r1, which is excluded as split-across-pages")
    TABLES[(39, 2)] = table(
        39, 2, 10, 22, 2, numeric=0, text=2, zebra=False, width="half", continued=True,
        note="Symbol / Description glossary, 13 rows here and 8 more on p40 r1, excluded as "
             "split-across-pages")

    for r in range(2, 5):
        excluded(14, r, "fragment-of-other",
                 "hexagon thumbnail pasted into the diagram column of Table 2 "
                 "(region p14 r1), not a separate exhibit")
    excluded(15, 1, "split-across-pages",
             "rows 6-13 of Table 2; the header and rows 1-5 are region p14 r1")
    for r in range(2, 10):
        excluded(15, r, "fragment-of-other",
                 "hexagon thumbnail inside the Table 2 continuation (region p15 r1)")
    for r in range(3, 10):
        excluded(17, r, "split-across-pages",
                 "Table 4 body rows; the column headings and first row are region p17 r2")
    for r in (1, 2):
        excluded(18, r, "split-across-pages",
                 "last Table 4 body rows, continuing the p17 fragments")
    excluded(27, 1, "split-across-pages", "Table 6, repeater rows 16-56")
    excluded(28, 1, "split-across-pages", "Table 6, repeater rows 57-97")
    excluded(29, 1, "split-across-pages", "Table 6, repeater rows 98-104")
    excluded(31, 1, "split-across-pages", "Table 8, repeater rows 40-80")
    excluded(32, 1, "split-across-pages", "Table 8, repeater rows 81-104")
    excluded(39, 1, "split-across-pages",
             "Table 9 parameter rows P_u,out to P_r,in; same three-column grid as region p38 r1")
    excluded(40, 1, "split-across-pages", "Table 10 symbol rows after item 13")
    excluded(34, 2, "not-an-exhibit",
             "typeset display formula (a square root in N, S_v and Phi) split out of the "
             "surrounding paragraph; an equation, not a figure")

    rules = [
        "Family follows the ink, not the frame: point-marker panels on the unitless -40..40 "
        "frame read scatter, panels whose ink is a polygon subdivision of the disc read "
        "map-or-plan-view, and labelled nodes joined by drawn edges read node-link-network "
        "[geometry.family].",
        "Hexagon geometry drawings of the cellular scheme are schematics even when they sit "
        "beside real numbers, because they carry no plotted data values [geometry.family].",
        "Every repeater-coordinate table is a full grid, so rule_style is boxed; Table 4, which "
        "prints one rule under the header and separates rows by shading, is booktabs "
        "[table.rule_style].",
        "Row shading, not rules, tells the coordinate tables apart from the two glossary "
        "tables: the former alternate shaded rows, the latter do not [table.zebra].",
        "A table that runs past its page keeps one record: the caption-bearing region is the "
        "table, later fragments are excluded as split-across-pages, and `continued` carries "
        "the flag while rows counts the whole table [table.continued].",
        "A table caption sits above its body and directly under the previous exhibit's last "
        "row, so caption position is above for every table and below for every figure, "
        "including Figure 15 whose caption is printed at the top of the next page "
        "[caption.position].",
        "Where the geometry pass measured a parent table and its interior cells separately, "
        "the interior rectangles are the table's own diagram cells: they are excluded as "
        "fragment-of-other instead of being counted as a composite panel [geometry.panel_count].",
        "Captions broken up by the typesetter are quoted as the longest run of printed lines "
        "that is still contiguous page text, which is why Figure 14 is quoted short "
        "[caption.verbatim].",
        "Section paths come from the printed heading order, not the extracted heading index, "
        "because axis tick numbers on pp. 19-23 are indexed as headings [place.section_path].",
        "Prose introduces most exhibits with a direct reference and occasionally inside "
        "brackets, so lead_pattern is direct except where the reference is parenthetical "
        "[mention.lead_pattern].",
    ]
    note = (
        "Ten numbered tables, six of which continue onto a later region; 29 measured regions "
        "are continuation fragments, table cells or a display formula rather than exhibits. "
        "Figure 14's caption is unreconstructable in full because the typesetter interleaved "
        "it with the facing column, so its shortest contiguous run is recorded. Table 4 was "
        "measured as ten narrow horizontal strips and is recorded once, on p17 r2."
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
    out = PROXY / "pb21-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, "
          f"{len(payload['tables'])} tables, {len(payload['excluded_regions'])} excluded")
    for key, text in CAPTIONS.items():
        page = ITEMS_NUMBER[key]
        try:
            schema.check_quote(text, PID, [page - 1, page, page + 1], f"caption {key}",
                               limit=None)
        except schema.Bad as exc:
            print("BAD", exc)
            return 1
    return 0


ITEMS_NUMBER = {("f", 1): 7, ("t", 1): 10, ("t", 2): 14, ("f", 2): 16, ("t", 3): 17,
                ("t", 4): 17, ("f", 3): 18, ("f", 4): 19, ("f", 5): 19, ("f", 6): 20,
                ("f", 7): 21, ("f", 8): 22, ("f", 9): 22, ("f", 10): 23, ("f", 11): 24,
                ("t", 5): 25, ("f", 12): 26, ("t", 6): 26, ("t", 7): 29, ("t", 8): 30,
                ("f", 13): 33, ("f", 14): 34, ("f", 15): 36, ("t", 9): 38, ("t", 10): 39}

if __name__ == "__main__":
    sys.exit(main())
