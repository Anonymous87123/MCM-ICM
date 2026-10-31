"""Hand pass for P-A-2012-14297-5cb8073e (leaf morphology and tree modelling, 45 pages).

Thirty-nine measured regions across twenty-two pages: sixteen figure items, twelve table
blocks and eleven exclusions. The paper prints nine table labels for those twelve blocks
because three tables break over a page boundary, and it numbers none of the split halves.

Captions are printed with the number attached ("Figure 1 Shape of Leaves", "Table 6 3-D
Model for Opposite Arrangement"), so the ctx dump found all of them. The "Figure 2." hit on
p3 is a sentence end, not a caption; the real Fig. 2 caption sits at the head of p4.

Families, panel counts and table shapes were read off the cropped page proxies, one crop per
reading.

Usage: python -I tools/_dist_paper29.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2012-14297-5cb8073e"
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
PAGES = list(range(1, 46))

INTRO = "Introduction"
S21 = "2.1 Descriptive Model of Leaf Shape"
S22 = "2.2 Model of cell growth and physiological activities"
S222 = "2.2.2 Model for physiological activities"
S23 = "2.3 Model of leaf arrangement & branching structure"
S231 = "2.3.1 Leaf arrangement"
S24 = "2.4 Model of the tree characteristics"

KIND_OF = {INTRO: "introduction", S21: "model", S22: "model", S222: "model",
           S23: "model", S231: "model", S24: "model"}


def path_for(page: int, reg: int) -> list[str]:
    """Filed under the heading the block is printed below.

    Fig. 9 is at the head of p13, above that page's own "2.2" heading, so it stays in 2.1.
    The three table halves on pp. 8, 38 and 41 keep the section of the half they continue.
    """
    if page in (3, 4):
        return [INTRO]
    if 7 <= page <= 13:
        return [S21]
    if page == 15:
        return [S22, S222]
    if page == 21:
        return [S22, S222]
    if page in (24, 25, 26):
        return [S23, S231]
    return [S24]


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
    if "shown in" in low or "as shown" in low:
        return "as-shown-in"
    if re.search(r"\b(shows|show|depicts|illustrates|drawn in|make up|presents)\b", low):
        return "figure-n-shows"
    return "direct"


def mention_for(kind: str, number: int, page: int) -> dict:
    """Count printed references to one exhibit number.

    The paper writes "Figure 5", "Figure12" and "Table 6" with uneven spacing, so the
    pattern allows any spacing and pins the number with a negative lookahead: "Figure 1"
    must not match inside "Figure 15".
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


def caption_block(text: str, numbering: str, *, position: str = "below",
                  words: int | None = None) -> dict:
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)) if words is None else words,
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": bool(re.search(r"\b(cm|m/s|m2|kg|rad|J)\b", text)),
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": position,
    }


def figure(page: int, reg: int, number: int, family: str, text: str, *, panels: int = 1,
           layout: str = "1", numbering: str = "Figure N", legend: str = "none",
           printed: bool = False, labels: bool = False, three_d: str = "no",
           position: str = "below", confidence: str = "high", note: str = "") -> None:
    ORDER.append((page, reg))
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": confidence,
        "panel_count": panels,
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": mention_for("Figure", number, page),
        "caption": caption_block(text, numbering, position=position),
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


def table(page: int, reg: int, rows: int, cols: int, number: int, text: str, *,
          header: int = 1, numeric: int = 0, text_cols: int = 1, units: bool = False,
          rule: str = "boxed", width: str = "full", continued: bool = False,
          numbering: str = "Table N", position: str = "above", note: str = "") -> None:
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
        "caption": caption_block(text, numbering, position=position),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header,
            "rule_style": rule,
            "zebra": False,
            "merged_cells": True,
            "diagonal_header": False,
            "units_in_header": units,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": width,
            "orientation": "portrait",
            "continued": continued,
            "note_sentence": "",
        },
    }


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def build() -> str:
    figure(3, 1, 1, "flowchart-or-schematic", "Figure 1 Shape of Leaves", panels=10,
           layout="2x5",
           labels=True,
           note="Ten labelled leaf silhouettes in a two-row grid: Ovate, Palmately-lobed, "
                "Pandurate, Peltate, Reniform, Rhomboid, Runcinate, Sagittate, Spathulate, "
                "Sublate; monochrome line art with the name under each outline.")
    figure(4, 1, 2, "flowchart-or-schematic", "Figure 2 Leaf Venation", panels=3,
           layout="row of 3", labels=True,
           note="Three venation drawings drawn side by side: parallel, pinnate, palmate.")
    figure(4, 2, 3, "flowchart-or-schematic", "Figure 3 Leaf Arrangement", panels=4,
           layout="row of 4", labels=True,
           note="Four phyllotaxy drawings with the species named under each: Opposite "
                "(Arenaria), Alternate (Prunus), Decussate (Syringa), Whorled (Lilium); "
                "source credit printed below the row.")
    figure(9, 1, 4, "line", "Figure 4 Shape function of Orbicular leaves (a=5)", printed=True,
           note="Polar axes with the shape function traced in green, the black arc marking "
                "the cell-division margin; r = 5 annotated at the centre.")
    figure(10, 1, 5, "line", "Figure 5 Shape function of Reniform Leaves (a = 5)",
           printed=True,
           note="Polar frame with the reniform curve traced in colour, black arc marking the "
                "cell-division margin.")
    figure(11, 1, 6, "line", "Figure 6 Shape function of lobed Leaves (a = 3, b=2, k=5)",
           printed=True,
           note="Polar frame with the five-lobed rose r = 3 + 2 sin(5 theta), same green "
                "curve and black margin as the earlier shape plots.")
    figure(11, 2, 7, "line",
           "Figure 7 Shape function of Palmate Leaves (a = 3.8, b=1.2, k=5)", printed=True,
           note="Polar frame with the five-petal rose r = 3.8 + 1.2 sin(5 theta).")
    figure(12, 1, 8, "line", "Figure 8 Shape Function of Elliptic Leaves (a=10, k=1/4)",
           printed=True,
           note="Polar frame with two arcs r = 10 sin(theta) +- 10 cos(theta) closing into an "
                "elliptic lens; formula labels set inside the axes.")
    figure(13, 1, 9, "line", "Figure 9 Shape Function of Flabellate Leaves (a=5)", printed=True,
           note="Polar sector r = 5 between theta = pi/4 and 3 pi/4, green arc closed by two "
                "black radii.")
    figure(15, 1, 10, "flowchart-or-schematic", "Figure 10 Photosynthesis Process",
           panels=4, layout="2x2",
           note="Four colour panels of the photosynthesis chain: light-dependent reactions "
                "in the thylakoid membrane, the whole chloroplast with the light-independent "
                "reactions, and two numbered close-ups of the ATP synthase; arrows and "
                "molecule labels, no axes.")
    figure(21, 1, 11, "flowchart-or-schematic", "Figure 11 Illustration of Transpiration",
           labels=True,
           note="Colour scheme of water uptake: leaf, stem xylem and root hair with arrows "
                "for the transpiration stream and callout labels; no axes.")
    figure(24, 1, 12, "flowchart-or-schematic",
           "Figure12 Three Types of Leaf Arrangements Projected on a Plane", panels=12,
           layout="loose 4-row flow of 12 panels", legend="inside", labels=True,
           note="Twelve lettered panels (a)-(l) of the three arrangements seen from above, "
                "with a small symbol key telling topmost from lower leaves.")
    figure(24, 2, 13, "flowchart-or-schematic", "Figure 13 Standardized Overlapping Leaves",
           labels=True,
           note="Geometric construction: two intersecting circles of radius r whose centres "
                "are 2m apart, the rhombus O1-O2-C and the shaded overlap lens, with the "
                "angles alpha, beta and m annotated.")
    figure(31, 1, 14, "flowchart-or-schematic",
           "Figure 14 Estimate Volume of the Tree by Round Platform", labels=True,
           note="Stem-and-phyllotaxis model with dimension lines L1, L2, T, x and the angle "
                "theta; the round platform is the swept surface.")
    # p35 measures Fig. 15 and Fig. 16 as a single block; one region, one item.
    figure(35, 1, 15, "line", "Figure 15 Regression Results of the Growth Model", panels=2,
           layout="column of 2", printed=True,
           note="One measured block holding both printed plots: kei against S(perimeter) "
                "with square markers and a fitted U-curve, and product against time with "
                "square markers, error bars and a fitted exponential. The second plot is "
                "the paper's Figure 16, 'Regression Result of Photosynthesis model'; the "
                "two cannot be separated because the region is a single drawing cluster.")
    figure(36, 1, 17, "heatmap-or-contour", "Figure 17 Finite Volume Method", panels=2,
           layout="main + inset", legend="inside",
           note="Hexagonal cell lattice with cells shaded for the cell state, a dashed red "
                "boundary and the i/j rays; a numbered hexagon inset acts as the key.")

    table(7, 1, 4, 3, 1, "Table 1 Representative Plant with Various Leaf Types", text_cols=2,
          note="Header plus three rows: leaf-shape name, a photograph of the plant, and the "
               "full taxonomic hierarchy with common name. The table continues on p8.")
    table(8, 1, 4, 3, 1, "Table 1 Representative Plant with Various Leaf Types", header=1, text_cols=2, continued=True,
          note="Continuation of Table 1 without a repeated header: Lobed, Palmate, "
               "Elliptic, Flabellate. The page prints no caption, so the quote is the label "
               "from p7.")
    table(25, 1, 2, 2, 2, "Table 2: Computation of Overlapping Areas", numbering="Table N:",
          rule="booktabs", text_cols=2,
          note="Two columns headed 'Convex-margin Leaves' and 'Concave-margin Leaves' over a "
               "single data row; each cell holds the overlap formula with a pair of leaf "
               "diagrams beside it. One vertical rule separates the two columns.")
    table(26, 1, 3, 2, 3, "Table 3: Overlapping under Different Leaf Arrangements",
          header=1, numbering="Table N:", text_cols=2,
          note="No column header words: the arrangement names Alternate, Opposite and Whorled "
               "are row labels down the left column and each row's right cell holds the "
               "arrangement drawing and its overlap formula. Alternate and Opposite share one "
               "merged cell; the single header row counted here is the first label band, not a "
               "column heading.")
    table(36, 2, 5, 7, 5, "Table 5 2-D Model", header=2, numeric=3, text_cols=3,
          note="Two header rows: '2-D Model' spans the table, then Input data, Output data, "
               "True value and Error; three data bands, and the Output, True-value and Error "
               "cells merge across the bands.")
    table(37, 1, 7, 7, 6, "Table 6 3-D Model for Opposite Arrangement", header=2,
          numeric=3, text_cols=3,
          note="Same two-tier grid as Table 5 with five input rows for the opposite "
               "arrangement.")
    table(37, 2, 5, 7, 7, "Table 7 3-D Model for Alternative Arrangement", header=2,
          numeric=3, text_cols=3,
          note="Three input rows for the alternate arrangement; the table runs on to p38.")
    table(38, 1, 2, 7, 7, "Table 7 3-D Model for Alternative Arrangement", header=1, continued=True, numeric=3, text_cols=3,
          note="Continuation of Table 7: the last two input rows (light incident angle pi/3, "
               "number of leaves on the branch, 20) that fell onto p38; no caption repeats, so "
               "the quote is the label from p37.")
    table(38, 2, 5, 7, 8, "Table 8 3-D Model for Whorled Arrangement", header=2,
          numeric=3, text_cols=3,
          note="Three input rows for the whorled arrangement.")
    table(39, 1, 11, 5, 9, "Table 9 Tree Profile/Branching Structure under Wind Influence",
          header=2, numeric=3, text_cols=2,
          note="Nine input rows (wind coefficient, blade area, wind speed, branch count, "
               "branch length, measured angle, shear modulus, old and new radius) against a "
               "computed torque, a measured angle and the error.")
    table(40, 1, 7, 7, 11, "Table 11 Crown Volume and Mass Estimation", header=2, numeric=3, text_cols=3,
          note="Five input rows (leaf radius, petiole length, highest crown level, trunk "
               "angle, leaf number) with the crown volume and mass estimates; the table runs "
               "on to p41.")
    table(41, 1, 6, 7, 11, "Table 11 Crown Volume and Mass Estimation", header=1, continued=True, numeric=3, text_cols=3,
          note="Continuation of Table 11: branch count, branch diameter, lowest-level length, "
               "form coefficient, wood density and gravity that fell onto p41; no caption "
               "repeats, so the quote is the label from p40.")

    for page, regs in ((7, (2, 3, 4)), (8, (2, 3, 4, 5)), (25, (2, 3)), (26, (2, 3))):
        for reg in regs:
            excluded(page, reg, "fragment-of-other",
                     "Leaf illustration set inside a table cell of the block measured above "
                     "it: a plant photograph on pp. 7-8, a leaf-pair diagram or a ray-and-shadow "
                     "sketch on pp. 25-26. Measured as its own raster, part of the table.")

    rules = [
        "Leaf-shape plots are recorded as line only where the crop shows a coordinate "
        "frame; the silhouette and phyllotaxy figures carry no axes [geometry.printed_numbers].",
        "Multi-panel figures of one family keep that family and carry the panel count "
        "instead of being recorded as composite-panel [geometry.panel_count].",
        "Illustrations embedded inside a table are measured as their own raster blocks but "
        "are part of the table above them, so they are excluded rather than counted as "
        "photo-or-raster-image exhibits [geometry.family].",
        "All twelve table blocks are fully gridded, so rule_style is boxed [table.rule_style].",
        "Three tables print in two halves across a page break; the second half is recorded "
        "with continued true and the label of the half it belongs to [table.continued].",
        "The paper prints labels 1, 2, 3, 5, 6, 7, 8, 9 and 11 only; there is no Table 4 or "
        "Table 10 anywhere, and the numbering is not a census artefact "
        "[caption.numbering].",
        "Captions sit above the table and below the figure throughout, so caption.position "
        "follows the printed side rather than the lane default [caption.position].",
        "The p35 block is a single drawing cluster holding both Figure 15 and Figure 16, "
        "so it is recorded once, with the second plot named in the note "
        "[caption.verbatim].",
        "The three continuation halves repeat no header row on the page, but header_rows "
        "cannot fall below one, so each keeps 1 and its note says the header sits on the "
        "previous page [table.header_rows].",
    ]
    note = (
        "Thirty-nine measured regions resolve to sixteen figure items, twelve table blocks "
        "and eleven exclusions. The exclusions are all photographs set inside a table: three "
        "in Table 1 on p7, four in its p8 half, two in Table 2 and two in Table 3. Twelve "
        "table blocks carry only nine printed labels because Tables 1, 7 and 11 each break "
        "over a page turn and the second half prints without a caption. The paper prints no "
        "Table 4 and no Table 10. p35 measures as one block but prints two figures, recorded "
        "as one item with the second plot named in the note; the in-text reference to "
        "'(Figure 1)' on p31 is a misnumber for Fig. 14 and is left as printed."
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
    out = PROXY / "pa29-payload.json"
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
