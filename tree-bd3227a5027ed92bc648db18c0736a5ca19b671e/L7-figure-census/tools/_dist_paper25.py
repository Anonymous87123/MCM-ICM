"""Hand pass for P-C-2011-11893-6a9ea7d9 (electric vehicles, 24 pages, 34 regions).

The paper labels its exhibits "Fig. N" and "Tbl. N". context_extract.py matches only
"figure|fig|table", so every "Tbl." label had to be read out of the page text by hand;
that is why the table captions below are typed rather than lifted from ctx.

Families, read off the cropped page proxies:

* p2 r1  - block diagram: three aspect bands feeding three model boxes: flowchart.
* p5 r2  - perspective wireframe surface (axes P, S and D) with three trajectories
  riding on it, so surface-or-3D with three_d surface-mesh, not a flat line chart.
* p7 r1, p7 r2, p11 r2, p12 r1, p13 r2, p17 r2 - connected series: line. p13 r2 is a
  raster of the energy-network diagram, so it is photo-or-raster-image.
* p8 r2  - embedded bitmap carrying a source URL: photo-or-raster-image.
* p11 r1 - discrete real-data points with a fitted curve through them: scatter.
* p15 r2, p16 r1, p17 r1, p18 r2 - grouped columns over named categories: bar. p17 r1
  has fourteen series (eta = 0.5 ... 4) grouped over six named supply sources.
* p19 r1 - three pie charts (BEV, PHEV, HEV) with one shared swatch legend. The
  vocabulary has no pie class, so it is other with an explicit other_note.

Tables: seven are numbered Tbl. 1 - Tbl. 7; the rest are the paper's unlabelled
"Notations" blocks, which are still ruled two-column tables and are counted as tables.

Usage: python -I tools/_dist_paper25.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2011-11893-6a9ea7d9"
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
MENTIONS = CTX["mentions"]

# Heading labels exactly as context_extract.py printed them. The paper's own numbering
# is broken (the ODE chapter is numbered "2" twice), so the labels look odd but they are
# what check_place.py resolves against.
INTRO = "未编号标题 Introduction"
ASSUME = "未编号标题 Assumptions"
DETERM = "1 The determination of variables"
PHEV = "4 PHEV and Tax"
OIL = "5 Impact on oil stock"
ELEC = "6 Computation of Electricity Margin"
ORDINARY = "2 Estimated Number of Ordinary Cars"
BASIC = "1 The Solution of the Basic Model"
SENS_ORD = "2 Sensitivity Analysis for Ordinary Condition"
SENS_EV = "3 Sensitivity Analysis for BEV, HEV, and PHEV"
REFS = "未编号标题 References"

KIND_OF = {
    INTRO: "introduction", ASSUME: "assumption", PHEV: "model", OIL: "result",
    ELEC: "solution", ORDINARY: "model", BASIC: "model", SENS_ORD: "sensitivity",
    SENS_EV: "sensitivity", REFS: "appendix",
}

PATH: dict[tuple[int, int], str] = {
    (2, 1): INTRO,
    (3, 1): ASSUME,
    (5, 1): PHEV, (5, 2): PHEV,
    (6, 1): OIL,
    (7, 1): OIL, (7, 2): ELEC,
    (8, 1): ELEC, (8, 2): ELEC, (8, 3): ELEC,
    (9, 1): ELEC, (9, 2): ELEC,
    (10, 1): ELEC,
    (11, 1): ORDINARY, (11, 2): ORDINARY,
    (12, 1): ORDINARY, (12, 2): ORDINARY,
    (13, 1): ORDINARY, (13, 2): ASSUME,
    (14, 1): BASIC,
    (15, 1): BASIC, (15, 2): BASIC,
    (16, 1): SENS_ORD,
    (17, 1): SENS_ORD, (17, 2): SENS_ORD,
    (18, 1): SENS_EV, (18, 2): SENS_EV,
    (19, 1): SENS_EV, (19, 2): SENS_EV, (19, 3): SENS_EV, (19, 4): SENS_EV,
    (19, 5): SENS_EV,
    (22, 1): REFS, (22, 2): REFS,
}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []


def place(page: int, reg: int, order: int) -> dict:
    path = PATH[(page, reg)]
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": [path],
        "section_numbered": not path.startswith("未编号"),
        "section_kind": KIND_OF[path],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def null_mention() -> dict:
    """No in-body reference resolves to this exhibit; only its printed label exists."""
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def snippet(page: int, token: str, *, before: int = 6, after: int = 12) -> str:
    """A verbatim window of the page text that contains `token` and stays under 25 words.

    schema.check_quote wants an exact substring of the page text, so the window is taken
    from the page text itself, not from the sentence the ctx dump printed.
    """
    text = schema.norm(schema.page_text(PID, page))
    at = text.index(schema.norm(token))
    cut = text.rfind(". ", 0, at)
    start = cut + 2 if cut != -1 else 0
    tail = text.find(". ", at)
    end = tail + 1 if tail != -1 else len(text)
    window = text[start:end].split()
    where = schema.norm(text[start:at]).split()
    lo = max(0, len(where) - before)
    hi = min(len(window), len(where) + len(schema.norm(token).split()) + after)
    return " ".join(window[lo:hi])


def figure_mention(page: int, number: int, pattern: str) -> dict:
    hits = [m for m in MENTIONS if m["kind"].startswith("fig") and m["number"] == number]
    if not hits:
        return null_mention()
    first = hits[0]["page"]
    return {
        "first_page": first,
        "lead_pages": page - first,
        "style": sorted({m["spelling"] for m in hits}),
        "count": len(hits),
        "lead_sentence": snippet(first, f"Fig. {number}"),
        "trail_sentence": "",
        "lead_pattern": pattern,
        "read_sentences": len(hits),
        "gap_sentences": None,
    }


def table_mention(page: int, label: str, first: int | None = None) -> dict:
    """Tables are named only by their own printed label; no prose sentence cites them
    except Tbl. 6, which p16 refers to as "(listed in Tbl. 6)"."""
    if first is None:
        return null_mention()
    return {
        "first_page": first,
        "lead_pages": page - first,
        "style": [label],
        "count": 1,
        "lead_sentence": f"(listed in {label})",
        "trail_sentence": "",
        "lead_pattern": "parenthetical",
        "read_sentences": 1,
        "gap_sentences": None,
    }


def caption_block(text: str, source: str, numbering: str) -> dict:
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)) if text else 0,
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        # Every label in this paper is set under its exhibit; the unlabelled blocks take
        # the same side as the placeholder so the field keeps a legal value.
        "position": "below",
    }


def figure(page: int, reg: int, family: str, number: int, *, legend: str = "none",
           three_d: str = "no", panels: int = 1, layout: str = "1",
           printed: bool = True, labels: bool = False, pattern: str = "direct",
           other_note: str = "", note: str = "") -> None:
    ORDER.append((page, reg))
    label = f"Fig. {number}"
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": label,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": figure_mention(page, number, pattern),
        "caption": caption_block(label, "text-layer", "Fig. N"),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, rows: int, cols: int, *, header: int = 1,
          numeric: int = 0, text_cols: int = 2, units: bool = False,
          merged: bool = False, continued: bool = False, label: str = "",
          numbered: bool = True, note: str = "") -> None:
    ORDER.append((page, reg))
    source = "text-layer" if label else "none"
    TABLES[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": label,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": table_mention(page, label) if numbered else null_mention(),
        "caption": caption_block(label, source, "Table N." if label else "none"),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header,
            "rule_style": "vertical-rules",
            "zebra": False,
            "merged_cells": merged,
            "diagonal_header": False,
            "units_in_header": units,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": "full",
            "orientation": "portrait",
            "continued": continued,
            "note_sentence": "",
        },
    }


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def build() -> str:
    figure(2, 1, "flowchart-or-schematic", 1, pattern="as-shown-in",
           printed=False, note="three aspect bands (economy, environment, society) feed "
                "three model boxes through labelled arrows; the whole scheme is drawn "
                "as rounded bands and block arrows")
    figure(5, 2, "surface-or-3D", 2, legend="none", three_d="surface-mesh",
           note="perspective wireframe surface with the two horizontal axes P and S and "
                "D as the vertical axis; three coloured trajectories with circular, "
                "square and cross markers ride on the mesh and their intersections are "
                "the equilibrium points")
    figure(7, 1, "line", 3, legend="inside",
           note="two accumulating series D(HEV) and D(CV) against year from 1980 to 2070, "
                "keyed inside the top right")
    figure(7, 2, "line", 4, legend="inside",
           note="three electricity-margin curves labelled beside the lines: no additional "
                "thermal electricity, 16hpd full load and 20hpd full load")
    figure(8, 2, "photo-or-raster-image", 5, printed=False,
           note="embedded bitmap of a daily electricity-demand chart with the source "
                "Lawrence Berkeley National Laboratory and the mpoweruk.com url printed "
                "under it; the ink is a raster, not paths")
    figure(11, 1, "scatter", 6, legend="inside",
           note="real-data points against a fitted curve, keyed 'fitting curve' and "
                "'real data'; y axis 'Number of Ordinary Cars'")
    figure(11, 2, "line", 7, legend="inside",
           note="two rising series, estimated number of electric cars and estimated "
                "number of ordinary cars, with the corresponding real-data series")
    figure(12, 1, "line", 8, legend="inside",
           note="six series a0' = a0 ... a0' = 1.5 a0 fanning out over t; x1 on the y axis")
    figure(13, 2, "photo-or-raster-image", 9, legend="none", printed=False,
           note="raster picture of the energy network with one x11 label; the prose calls "
                "it the distribution of the energy network, and the ink is a bitmap")
    figure(15, 2, "bar", 10, legend="inside", printed=False,
           note="grouped columns of energy by supply sector under the original condition "
                "and under three restriction variants, values 0-120")
    figure(16, 1, "bar", 11, legend="inside", printed=False,
           note="six constraint combinations along the category axis, total environmental "
                "cost PALL on the value axis; the combinations are named in the legend only")
    figure(17, 1, "bar", 12, legend="outside-right", pattern="none",
           note="fourteen clustered series (eta = 0.5 to 4) over six named supply sources "
                "and energy transmission; two 'Critical Point: eta = 0.85' annotations "
                "point at the coal and transmission groups; y axis 0-40 quadrillion Btu")
    figure(17, 2, "line", 13, legend="none",
           note="a single PALL curve against eta with the critical point at eta = 0.85 "
                "marked; y axis ticks 48-60, no key box")
    figure(18, 2, "bar", 14, legend="inside", printed=False,
           note="pollution of the original mix against BEV, PHEV and HEV under their own "
                "constraints; four labelled categories")
    figure(19, 1, "other", 15, legend="inside", panels=3, layout="2x2",
           printed=False, labels=True,
           other_note="three pie charts (BEV, PHEV, HEV) sharing one swatch legend; the "
                      "family vocabulary has no pie class, and composite-panel would only "
                      "describe the tiling, so the ink is recorded as other",
           note="percent labels on every wedge; the shared legend sits bottom right, the "
                "third pie bottom left")

    table(3, 1, 11, 2, text_cols=2, numbered=False,
          note="the first 'Notations' block: eleven symbols against their definitions, "
               "one vertical rule after the symbol column and a rule between every row")
    table(5, 1, 3, 4, header=1, numeric=3, text_cols=1, units=True, label="Tbl. 1",
          note="the two equilibrium-point vehicles (PHEV and CV) with price, supply and "
               "demand; units sit in the header cells")
    table(6, 1, 2, 5, numeric=4, text_cols=1, label="Tbl. 2",
          note="a two-row band: P_rise across the top, the resulting change of D_cv along "
               "the bottom; no header row")
    table(8, 1, 2, 4, header=1, numeric=3, text_cols=1, label="Tbl. 3",
          note="three thermal-electricity scenarios across the header, the average lambda "
               "from 2002 to 2006 as 12%, 28% and 42% in the body")
    table(8, 3, 2, 4, header=1, numeric=3, text_cols=1, units=True, label="Tbl. 4",
          note="the same four columns as Tbl. 1 for a 38.5% PHEV / 61.5% CV mix")
    table(9, 1, 7, 2, text_cols=2, numbered=False, continued=False,
          note="the second 'Notations' block: seven symbols of the competing differential "
               "equation model, same ruled layout as the first")
    table(9, 2, 2, 2, text_cols=2, numbered=False, continued=True,
          note="the last two symbol rows (a2, a1) of the Tbl. 5 block, cut off at the "
               "foot of p9 and completed by the four rows on p10")
    table(10, 1, 4, 2, text_cols=2, label="Tbl. 5", continued=True,
          note="the four a0/b2/b1/b0 rows that finish the notation block begun on p9; the "
               "Tbl. 5 label is printed under the last row")
    table(12, 2, 5, 2, text_cols=2, numbered=False,
          note="the linear-programming 'Notations' block: x_ij, x_c, B_j, A_i and P_ij")
    table(13, 1, 7, 2, text_cols=2, numbered=False,
          note="the efficiency 'Notations' block: eta_1, eta_2, eta, O_100, E, E_100 and "
               "P_ALL")
    table(14, 1, 2, 4, header=1, numeric=2, text_cols=2, label="Tbl. 6",
          note="the constraint table starts at the foot of p14 with the header and row 1 "
               "only; eight more numbered constraints follow on p15")
    table(15, 1, 8, 4, numeric=1, text_cols=3, label="Tbl. 6", continued=True,
          note="constraints 2 to 8 of Tbl. 6, no repeated header; the Tbl. 6 label is "
               "printed under the last row")
    table(18, 1, 7, 3, header=1, numeric=1, text_cols=2, merged=True, label="Tbl.7",
          note="the BEV, PHEV and HEV constraint sets; the type cell of each set is merged "
               "over its two constraint rows")
    table(22, 1, 10, 11, header=3, numeric=10, text_cols=1, numbered=False,
          note="appendix data for 1980-2006: year, S, P and D, with the year header "
               "repeated three times as the block runs across the page")
    table(22, 2, 3, 12, header=1, numeric=11, text_cols=1, numbered=False,
          note="appendix data for 1999-2009: number of electric cars (x10^6) and of "
               "conventional cars (x10^8)")

    excluded(19, 2, "fragment-of-other",
             "the BEV pie of the Fig. 15 composite; it lies inside the composite bbox and "
             "was measured again as its own region")
    excluded(19, 3, "fragment-of-other",
             "the PHEV pie of the same Fig. 15 composite, measured again inside it")
    excluded(19, 4, "fragment-of-other",
             "the HEV pie of the same Fig. 15 composite, measured again inside it")
    excluded(19, 5, "fragment-of-other",
             "the five-swatch colour legend of the Fig. 15 composite, which sits inside "
             "the composite bbox")

    rules = [
        "Exhibit labels are the bare strings 'Fig. N' and 'Tbl. N' with no caption body, "
        "so every caption is a two-word text-layer label and the tables keep the same "
        "form [caption.verbatim].",
        "The paper abbreviates Table as 'Tbl.'; the numbering field uses the closest "
        "closed-enum member, 'Table N.', and the verbatim keeps the abbreviation "
        "[caption.numbering].",
        "Every label in this paper is set below its exhibit, so position is below for "
        "figures and tables alike [caption.position].",
        "Family follows the ink rather than the label: p5 r2 is a perspective wireframe "
        "surface and p7 r1, p11 r2, p12 r1, p13's curve and p17 r2 are connected series, "
        "so they are recorded as surface-or-3D and line respectively "
        "[geometry.family].",
        "p5 r2 has a receding depth axis and a mesh drawn in perspective, so the "
        "three_d field is surface-mesh rather than a flat two-axis plot "
        "[geometry.three_d].",
        "The p8 r2 demand chart is an embedded bitmap with a printed source url and the "
        "p13 r2 network picture is a bitmap too, so both are photo-or-raster-image "
        "[geometry.family].",
        "p11 r1 draws discrete real-data points under a fitted curve, so it is scatter "
        "while its neighbour p11 r2 is line [geometry.family].",
        "Four exhibits are grouped columns over named categories with the series named "
        "only in a key: p15 r2, p16 r1, p17 r1 and p18 r2, so they are bar "
        "[geometry.family].",
        "The Fig. 15 exhibit is three pie charts with one shared key; the vocabulary has "
        "no pie class, so it is recorded as other with an explicit other_note and "
        "panel_count 3 [geometry.panel_count].",
        "Key placement is read off each frame: most figures box their key inside, the "
        "p17 r1 legend sits outside at the right because fourteen series will not fit, "
        "and single-series p17 r2 has no key at all [geometry.legend].",
        "Four regions on p19 are the individual pies and the swatch legend of the Fig. 15 "
        "composite, measured again inside its bbox; they are excluded as fragments, not "
        "counted as extra figures [place.page_order].",
        "Every measured block in this paper is a fully ruled grid with vertical rules "
        "between the columns, so rule_style is vertical-rules throughout "
        "[table.rule_style].",
        "No table shades alternate rows, so zebra is false everywhere [table.zebra].",
        "Tbl. 7 merges the type cell over each pair of constraint rows, so merged_cells "
        "is true for that table only [table.merged_cells].",
        "The appendix table on p22 repeats its year header three times as the block runs "
        "across the page, so header_rows is 3 there [table.header_rows].",
        "Only Tbl. 1, Tbl. 4 and the p22 appendix blocks print units in the header cells; "
        "the rest leave the unit in the prose [table.units_in_header].",
        "Only Tbl. 6 is referred to in the body text ('listed in Tbl. 6' on p16); every "
        "other table is named only by its own printed label, so those mention blocks are "
        "the null form [mention.lead_pattern].",
        "Fig. 12 has no in-body reference anywhere, only the printed label, so its "
        "mention block is the null form while the label still supplies the caption "
        "[mention.first_page].",
        "Two exhibits are split across a page break: Tbl. 6 starts at the foot of p14 and "
        "continues on p15, and the notation block runs from p9 r2 to p10 r1; both halves "
        "are counted as tables and marked continued [table.continued].",
        "Section paths follow the printed heading the region actually sits under: Fig. 3 "
        "is above the '6. Computation of Electricity Margin' heading on p7 so it belongs "
        "to section 5, and the p19 pies sit above the Conclusion heading so they stay in "
        "the EV sensitivity section [place.section_path].",
    ]
    note = (
        "The paper's own numbering is broken: the ordinary-versus-electric-car chapter is "
        "printed as '2' a second time, and two headings that context_extract.py picked up "
        "('2 D(CV)' on p7, '56 Critical Point:' on p17, '5 Power sector to xc 10' on p15) "
        "are axis or table text, not headings; those regions are filed under the real "
        "heading above them. 'Tbl.' labels are invisible to context_extract.py, so "
        "Tbl. 1 to Tbl. 7 were read from the page text by hand. Five unlabelled "
        "'Notations' blocks are ruled two-column tables and are counted as tables, which "
        "is why this paper has fifteen tables against seven printed table numbers."
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
    out = PROXY / "pc25-payload.json"
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
