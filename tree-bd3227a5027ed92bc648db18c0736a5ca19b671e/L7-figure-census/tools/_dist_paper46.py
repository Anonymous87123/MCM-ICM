"""Hand pass for P-A-2013-20559-c8c96095 (the optimal baking-pan algorithm: lattice packing,
a heat model fitted to a calorimetry experiment, and an efficiency sweep, 16 pp).

The geometry pass measures 5624 regions, but page 2 paints a full-page mock advertisement as a
repeated raster tile and 5614 of those regions collapse to sixteen distinct squares. The whole
paper therefore accounts for 26 unique regions:

    10 figure rows + 16 p2 advertisement regions + 0 tables = 26, unaccounted 0.

    p5-r1   Figure 1   lattice pattern for octagons
    p5-r2   Figure 2   tessellating pattern for squares (right-hand panel)
    p5-r3   Figure 2   tessellating pattern for hexagons (left-hand panel)
    p6-r1   Figure 3   side length, apothem and radius of a regular polygon
    p8-r1   Figure 4   setup of the calorimetry experiment
    p11-r1  Figure 7   the table of tallies, printed as a grid
    p13-r1  Figure 8   efficiency against polygon sides, varying alpha
    p13-r2  Figure 9   the same, varying beta
    p14-r1  Figure 10  the same, varying gamma
    p14-r2  Figure 11  the same, varying c-rho

Declared gaps: Figures 5 and 6 print on p8 as typed Time/Temperature rows inside the body text
("Time (min) 0 10 20 30 40 50 / Temperature (C) 22 72 99 102 104 116"), with a caption line and
no measured region at all - a declared gap, never an invented bbox.

Figure 2 is one printed number over two separately measured panels side by side, so it takes one
row per panel with the printed number repeated (paper 40 and paper 44 precedent); the extractor's
reading order puts the right-hand square grid first because it sits 40 pt higher on the page.

Page 2 is not an exhibit page. It is a parody advertisement for "Polythermal Bakeware" - live
typeset text over a wood-grain background made of one raster tile repeated thousands of times,
with three photographic insets. Its twelve tiled squares are excluded `background` and its four
inset panels `not-an-exhibit`.

Usage: python -I tools/_dist_paper46.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2013-20559-c8c96095"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
MEASURED: dict[tuple[int, tuple[float, ...]], list[float]] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")
    for r in pg["regions"]:
        key = (pg["page"], tuple(round(v, 1) for v in r["bbox"]))
        MEASURED.setdefault(key, r["bbox"])

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

SPACE = "未编号标题 Space Optimization"
HEAT = "未编号标题 Heating of Polygons"
CALOR = "未编号标题 Heat Transfer Coefficient Calculations"
OPT = "未编号标题 Optimal Shapes"
SENS = "未编号标题 Sensitivity with respect to heating parameter"

PATH = {
    5: ([SPACE], "model"),
    6: ([HEAT], "model"),
    8: ([CALOR], "model"),
    11: ([OPT], "result"),
    13: ([SENS], "sensitivity"),
    14: ([SENS], "sensitivity"),
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# recorded regions per page, counted first so doc_order stays monotonic
VENTION = {5: 3, 6: 1, 8: 1, 11: 1, 13: 2, 14: 2}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}

CAPTIONS = {
    5: ["Figure 1: Lattice pattern for octagons.",
        "Figure 2: Tessellating patterns for squares and hexagons"],
    6: ["Figure 3: Diagram showing the side length (S), apothem (r), and Radius (R) of a "
        "regular polygon."],
    8: ["Figure 4: Setup of calorimetry experiment."],
    11: ["Figure 7: Table of tallies for different shapes over all tested pan areas."],
    13: ["Figure 8: Efficiency of various shapes with different values for \u03b1.",
         "Figure 9: Efficiency of various shapes with different values for \u03b2."],
    14: ["Figure 10: Efficiency of various shapes with different values for \u03b3.",
         "Figure 11: Efficiency of various shapes with different values for c\u03c1."],
}


def caption(page: int, index: int) -> str:
    """The caption as the text layer prints it, checked to be on the page."""
    text = CAPTIONS[page][index]
    body = schema.page_text(PID, page)
    if schema.norm(text) not in body:
        raise KeyError((page, text[:40]))
    return text


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH[page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": False,
        "section_kind": kind,
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


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": None}


def figure(page: int, reg: int, family: str, caption_text: str, *, numbering: str,
           panels: int = 1, layout: str = "1", legend: str = "none",
           numbers: bool = False, labels: bool = False, other_note: str = "",
           mention_block: dict | None = None, note: str = "") -> None:
    ORDER.append((page, reg))
    blocking = dict(mention_block) if mention_block else dict(NULL_MENTION)
    if blocking["first_page"] is not None and blocking["lead_pages"] is None:
        blocking["lead_pages"] = page - blocking["first_page"]
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption_text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption_text, numbering),
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
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def excluded(page: int, bbox_key: tuple[float, ...], reason: str, note: str) -> None:
    key = (page, tuple(round(float(v), 1) for v in bbox_key))
    if key not in MEASURED:
        raise KeyError(key)
    EXCLUDED.append({"page": page, "bbox": MEASURED[key], "reason": reason, "note": note})


def build() -> str:
    # --- the three line drawings, plus the definition diagram --------------------------
    figure(5, 1, "other", caption(5, 0), numbering="Figure N:",
           other_note="lattice packing diagram: twelve outlined octagons laid in four offset "
                      "columns so their corners interlock and leave small square gaps at the "
                      "joins; a printed pattern, not a plot and not a photograph",
           mention_block=mention(4, ["Figure 1"],
                                 "utilized lattice packing as shown in Figure 1",
                                 "as-shown-in"),
           note="Twelve regular octagons in four columns of three, each column shifted half a "
                "cell against its neighbour so the slanted edges interlock and four small "
                "squares are left open at the crossings. Black hairline outline on white, no "
                "fill, no axes, no ticks, no labels, no scale - a lattice packing diagram that "
                "illustrates the space-maximising construction of the algorithm.")

    figure(5, 2, "other", caption(5, 1), numbering="Figure N:",
           layout="1 of 2",
           other_note="tessellation diagram: a thick-ruled three by three field of squares, "
                      "the packing case the lattice construction falls back on; a printed "
                      "pattern, not a plot",
           mention_block=mention(4, ["Figure 2"],
                                 "squares and hexagons as shown in Figure 2",
                                 "as-shown-in"),
           note="The right-hand panel of the printed figure: a three by three field of large "
                "squares drawn with rules noticeably heavier than the octagon lattice beside "
                "it, every cell empty. This is the tessellating case the paper uses for pan "
                "shapes whose lattice packing degenerates - squares need no gap for airflow, "
                "which the text says explicitly. One of two panels under a single printed "
                "number.")

    figure(5, 3, "other", caption(5, 1), numbering="Figure N:",
           layout="2 of 2",
           other_note="tessellation diagram: fifteen outlined hexagons in offset columns, the "
                      "six-sided packing case; a printed pattern, not a plot",
           mention_block=mention(5, ["Figure 2"],
                                 "With the hexagonal tessellation seen in Figure 2",
                                 "as-shown-in"),
           note="The left-hand panel of the same printed figure: hexagons in four offset "
                "columns, drawn at the same weight as Figure 1's octagons and empty inside, the "
                "six-sided case the algorithm falls back on when a polygon has no multiple of "
                "four sides. One caption covers both panels and both rows quote it; the "
                "extractor returns the square panel first only because it sits 40 pt higher.")

    figure(6, 1, "other", caption(6, 0), numbering="Figure N:",
           labels=True,
           other_note="geometry definition diagram: one regular hexagon with its radius, its "
                      "apothem and its side length marked; an annotated polygon, not a plot",
           note="A single regular hexagon with three construction marks: a radius R from the "
                "centre to the right-hand vertex, an apothem r from the centre horizontally to "
                "the midpoint of the right edge, and the side length S labelled outside the "
                "upper right edge, all in italic serif. Line drawing only - no axes, no data, "
                "no fill, no second polygon - printed to define the three lengths the packing "
                "formula uses in the next section.")

    # --- the experiment schematic -----------------------------------------------------
    figure(8, 1, "flowchart-or-schematic", caption(8, 0), numbering="Figure N:",
           labels=True,
           mention_block=mention(7, ["Figure 4"],
                                 "a calorimetry experiment was done using the set up as shown "
                                 "in Figure 4", "as-shown-in"),
           note="The calorimetry rig drawn in heavy black outline: two nested cups with a lid "
                "over the mouth, a probe lead running out of the lid to a separate rectangular "
                "meter box on the right that prints '30.0C'. A hand-drawn apparatus schematic "
                "for the temperature measurement described on the next page - no axes, no "
                "scale, no key.")

    # --- the printed tally grid, numbered as a figure ---------------------------------
    figure(11, 1, "table-as-figure", caption(11, 0), numbering="Figure N:",
           numbers=True,
           mention_block=mention(11, ["Figure 7"],
                                 "for each pan shape over all pan areas tested for a given "
                                 "choice of weights and obtained the following results",
                                 "direct"),
           note="A printed tally grid, not a plot: a header row 'p | 4 | 6 | 18 | 20 | "
                "circle' over eleven body rows for p from 0.00 to 1.00 in steps of 0.10, every "
                "cell a small integer count of wins. Vertical rules stand between every column "
                "and a horizontal rule under every row, but no rule closes the grid at the top, "
                "the bottom or the right. It stays in the figure block because the paper "
                "numbers it as Figure 7.")

    # --- the four efficiency sweeps ---------------------------------------------------
    line_geom = dict(numbers=True, legend="inside")
    figure(13, 1, "line", caption(13, 0), numbering="Figure N:",
           note="Four series plotted as markers joined by straight lines against 'Polygon "
                "Sides' (4 to 20, tick every 2) and 'Efficiency' (0.84 to 1, tick every 0.02), "
                "with light horizontal gridlines and a boxed legend inside the frame at the "
                "right keying alpha = 1.8e-7, 9.0e-8, 1.8e-8 and 1.8e-9. Every series climbs "
                "and then flattens, the slowest at the lowest alpha - the sensitivity the "
                "section argues is small enough to leave the ranking intact.",
           **line_geom)
    figure(13, 2, "line", caption(13, 1), numbering="Figure N:",
           note="The same axes and gridlines with four series for beta = 1.0e-5, 2.5e-5, "
                "5.0e-5 and 2.5e-4. The spread between the curves is far wider than in Figure "
                "8 and the lowest beta starts below 0.84, which is the point of the pair: the "
                "efficiency is sensitive to beta and nearly insensitive to alpha. Legend "
                "inside the frame on the right; no series is labelled on the plot itself.",
           **line_geom)
    figure(14, 1, "line", caption(14, 0), numbering="Figure N:",
           note="Seven series on the same axes for gamma from 1.0e-8 to 4.0e-4, the densest "
                "sweep in the paper: the curves fan out between 0.84 and 0.92 at four sides and "
                "converge near 0.99 by eighteen. Legend inside the frame at the right, light "
                "horizontal gridlines only, no axis title beyond the two the other sweeps "
                "carry.",
           **line_geom)
    figure(14, 2, "line", caption(14, 1), numbering="Figure N:",
           note="Three series ('Double c x rho', 'Normal c x rho', 'Half c x rho') on the same "
                "axes, the y range widened to 0.75-1 so the halved value at 0.80 is visible. "
                "This is the one sweep the text reads out loud - halving c-rho lifts efficiency "
                "by about 15 % - and the widest separation of any of the four charts, which is "
                "why the paper treats it as the parameter worth fixing first. Legend inside the "
                "frame at the right.",
           **line_geom)

    # --- page 2: the parody advertisement ---------------------------------------------
    TILE = ("One 122.8 pt square of the raster texture the p2 advertisement tiles across its "
            "lower half: the geometry pass returns 5614 tiles on this page, which collapse to "
            "twelve distinct squares in two bands. Texture only - no axes, no number, no "
            "caption, nothing the paper refers to.")
    TILES = [(525.1, -122.9, -0.1, 647.9), (525.1, -0.1, 122.8, 647.9),
             (525.1, 122.8, 245.7, 647.9), (525.1, 245.7, 368.6, 647.9),
             (525.1, 368.6, 491.5, 647.9), (525.1, 491.5, 614.3, 647.9),
             (647.9, -122.9, -0.1, 770.8), (647.9, -0.1, 122.8, 770.8),
             (647.9, 122.8, 245.7, 770.8), (647.9, 245.7, 368.6, 770.8),
             (647.9, 368.6, 491.5, 770.8), (647.9, 491.5, 614.3, 770.8)]
    for top, left, right, bottom in TILES:
        excluded(2, (left, top, right, bottom), "background", TILE)

    INSET = ("An inset panel of the full-page mock advertisement that fills p2 - a parody bakeware "
             "ad printed live over wood-grain artwork, with a headline, a contact block and three "
             "photographs. No caption, no printed number, and no sentence anywhere in the paper "
             "refers to the page.")
    excluded(2, (8.9, 8.9, 131.8, 131.8), "not-an-exhibit",
             "The upper-left tile of the advertisement artwork, carrying the word 'Stop' from "
             "the headline 'Stop Worrying About Pans'. Part of the page's display type, not an "
             "exhibit.")
    excluded(2, (81.0, 180.0, 279.0, 324.0), "not-an-exhibit",
             "A photographic inset of the mock advertisement - a pan photographed on the "
             "wood-grain background. " + INSET)
    excluded(2, (306.0, 495.0, 540.0, 639.0), "not-an-exhibit",
             "The lower-right inset of the mock advertisement, printed directly above the fake "
             "telephone numbers 000.111.2222 and 000.111.3333. " + INSET)
    excluded(2, (234.0, 657.0, 378.0, 783.0), "not-an-exhibit",
             "The inset that sits on top of the tiled lower band, the only advertisement element "
             "the texture does not cover. " + INSET)

    rules = [
        "Figures 1, 2 and 3 are line drawings rather than plots - a lattice pattern, two "
        "tessellations and one labelled polygon - so they carry family `other` with an "
        "`other_note` naming the drawing [geometry.family].",
        "Figure 2 prints one caption over two separately measured panels standing side by side, "
        "so it takes one row per panel and both rows quote the same caption, the printed number "
        "repeated [caption.verbatim].",
        "Figure 7 is a printed tally grid that the paper numbers as a figure, so it stays in the "
        "figure block as `table-as-figure` rather than moving to the table list "
        "[geometry.family].",
        "Every caption in the paper prints below its exhibit and none of them states a unit or "
        "draws a conclusion, the tally grid included [caption.position].",
        "Figures 8 to 11 are four sweeps of one efficiency curve over the same axes - Polygon "
        "Sides on x, Efficiency from 0.84 to 1 on y - differing only in the parameter varied, so "
        "all four are `line` and each carries a legend inside its frame [geometry.legend].",
        "Only four of the eleven printed figures are named in the running text - Figures 1, 2, 4 "
        "and 7 - and the four efficiency charts are never cited by number at all [mention.count].",
        "Figure 3 is a definition diagram and no sentence points at it, so its mention block is "
        "empty [mention.first_page].",
        "The paper prints no numbered section headings, so `section_path` uses the printed "
        "sub-headings ('Space Optimization', 'Heating of Polygons', 'Heat Transfer Coefficient "
        "Calculations', 'Optimal Shapes', 'Sensitivity with respect to heating parameter') in the "
        "unnumbered form [place.section_numbered].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2013\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "A-20559-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER],
        "tables": [],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twenty-six unique measured regions, all accounted: ten figure rows for eleven "
            "printed figures (Figure 2 is one caption over two measured panels) and sixteen "
            "regions on p2, which is a full-page parody advertisement rather than an exhibit "
            "page - twelve raster tiles of its wood-grain background are `background` and four "
            "inset panels are `not-an-exhibit`. The page reports 5614 raw regions because that "
            "texture is painted as thousands of overlapping tiles; they collapse to twelve "
            "distinct squares. Figures 5 and 6 print on p8 as typed Time/Temperature rows inside "
            "the body text with a caption line but no measured region, so they are declared gaps, "
            "not invented bboxes. The paper prints no tables of its own calling: the one grid, "
            "Figure 7, is numbered as a figure."
        ),
    }
    out = PROXY / "pb46-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
