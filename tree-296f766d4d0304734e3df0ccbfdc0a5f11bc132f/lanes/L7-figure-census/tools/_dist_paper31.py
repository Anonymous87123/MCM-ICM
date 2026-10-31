"""Hand pass for P-A-2012-15065-1cbc0cd9 (A Vector Tree Model, 29 pages).

The geometry pass measures 53 regions over 15 pages. The paper prints no captions and no
exhibit numbers at all: `context_extract` finds 0 captions and 0 mentions, so every row is
uncaptioned and every mention block is empty. Where a caption is printed at all it is set
inside a bordered box that is itself a measured region (p16-r3), and table captions are
inside the raster.

Families, read off cropped page proxies:

* The four leaf silhouettes at the head of p6 and the two outline pairs on p15-r1/p15-r2
  are flat labelled glyphs of the four leaf categories - not photographs, not plots - so
  they are recorded as `other` with a note saying what the glyph is.
* p6-r5 through p6-r10 are photographs of leaves laid on the 0.5 cm grid, two illustrations
  of three stages each (bare grid, occupied cells, simulating polygon).
* Everything drawn by hand is flowchart-or-schematic: the three dimension-rule panels, the
  printed decision flow chart, the annotated tree-structure illustration, the two branch
  transformation frames, the spherical-coordinate diagram, the sunlight/ground triangle and
  the ray-through-crown sketch.
* Every rendered 3D scene is surface-or-3D: the three tree profiles, the three earth-orbit
  figures, the two leaf-exposure scenes, the case-study camphor renders and the p23 profile
  trio.
* p16-r2 is a composite block (3D scatter plus two 2D scatter panels plus a caption box)
  and p23-r4 through p23-r7 are four small scatter plots of the leaf-mass regression.
* The p15/p16 table is a raster of a ruled table, so it is table-as-figure, split over the
  page break into two measured blocks.

Excluded: one magnified re-crop of a single box of the printed flow chart (p7-r5), the three
sub-pictures the extractor split out of the web illustration on p8, and the bordered caption
box that sits inside the p16 composite.

Usage: python -I tools/_dist_paper31.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2012-15065-1cbc0cd9"
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


def head(page: int, num: str) -> dict:
    for h in CTX["headings"]:
        if h["page"] == page and h["label"].split()[0] == num:
            return h
    raise KeyError((page, num))


PATH_NUMS: dict[int, list[tuple[int, str]]] = {
    6: [(5, "2"), (5, "2.1")],
    7: [(5, "2"), (5, "2.1")],
    8: [(5, "2"), (7, "2.2"), (8, "2.2.2")],
    9: [(5, "2"), (7, "2.2"), (8, "2.2.2"), (8, "2.2.2.1")],
    10: [(5, "2"), (7, "2.2"), (10, "2.2.3")],
    11: [(11, "3"), (11, "3.1")],
    12: [(11, "3"), (12, "3.2")],
    13: [(13, "4"), (13, "4.1")],
    14: [(13, "4"), (13, "4.1")],
    15: [(13, "4"), (15, "4.2")],
    16: [(16, "5")],
    20: [(16, "5"), (20, "5.3")],
    21: [(16, "5"), (20, "5.3"), (21, "5.3.1")],
    22: [(16, "5"), (20, "5.3"), (22, "5.3.2")],
    23: [(16, "5"), (20, "5.3"), (22, "5.3.2")],
}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []


def place(page: int, reg: int, order: int) -> dict:
    heads = [head(p, n) for p, n in PATH_NUMS[page]]
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": [h["label"] for h in heads],
        "section_numbered": True,
        "section_kind": heads[-1]["kind"],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, position: str = "below") -> dict:
    return {
        "verbatim": text,
        "numbering": "none",
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


def figure(page: int, reg: int, family: str, *, panels: int = 1, layout: str = "1",
           legend: str = "none", three_d: str = "no", numbers: bool = False,
           labels: bool = False, other_note: str = "", caption: str = "",
           note: str = "") -> None:
    ORDER.append((page, reg))
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption,
        "caption_source": "text-layer" if caption else "none",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                    "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                    "read_sentences": 0, "gap_sentences": None},
        "caption": caption_block(caption),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


COMPOSITE_NOTE = ("the two illustrations of section 2.1 are photographed leaves laid on a "
                  "0.5 cm square grid; each measured block is one stage of one illustration")


def build() -> str:
    # 2.1 leaf classification: four silhouette glyphs
    for reg, shape in ((1, "Elliptic"), (2, "Linear"), (3, "Deltoid"), (4, "Palmate")):
        figure(6, reg, "other",
               other_note=f"a flat green silhouette glyph of the {shape} leaf, the shape "
                          "category key of section 2.1, not a photograph and not a plot",
               note=f"one of the four leaf-category silhouettes printed at the head of p6: "
                    f"a filled {shape} leaf glyph on white with the category name as its "
                    "only label.")
    # the two grid illustrations, three measured stages each
    figure(6, 5, "photo-or-raster-image",
           note=f"{COMPOSITE_NOTE}: the bare photograph of a leaf on the grid, stage 1 of "
                "the first illustration.")
    figure(6, 6, "photo-or-raster-image",
           note=f"{COMPOSITE_NOTE}: the same leaf with the occupied grid cells filled in "
                "light green, stage 2 of the first illustration.")
    figure(6, 7, "photo-or-raster-image",
           note=f"{COMPOSITE_NOTE}: the same leaf with the black polygon joining the cell "
                "centres drawn over it, stage 3 of the first illustration - the simulating "
                "polygon the text describes.")
    figure(6, 8, "photo-or-raster-image",
           note=f"{COMPOSITE_NOTE}: the second leaf with its fitted polygon, stage 1 of the "
                "second illustration.")
    figure(6, 9, "photo-or-raster-image",
           note=f"{COMPOSITE_NOTE}: the second leaf with the filled cell mask, stage 2 of "
                "the second illustration.")
    figure(6, 10, "photo-or-raster-image",
           note=f"{COMPOSITE_NOTE}: the second leaf on the bare grid, stage 3 of the second "
                "illustration.")

    # p7 leaf index dimension panels and the decision flow chart
    figure(7, 1, "flowchart-or-schematic",
           note="leaf-index construction, panel 1: a green leaf silhouette with two vertical "
                "dimension rules and an outward arrow pair, labelled 'distance between leaf "
                "tip and longest-width-position'.")
    figure(7, 2, "flowchart-or-schematic",
           note="leaf-index construction, panel 2: the same dimension rules drawn on an "
                "elliptic leaf, so that D and L can be read off.")
    figure(7, 3, "flowchart-or-schematic",
           note="leaf-index construction, panel 3: the long narrow leaf case, the two rules "
                "far apart with the arrows pointing outward.")
    figure(7, 4, "flowchart-or-schematic",
           note="the printed decision flow chart of section 2.1: boxes joined by arrows, "
                "'Leaf polygon: convex?' splitting to Convex/Concave (Palmate), 'Leaf index' "
                "at 3.5 splitting to Linear, then the D/L ratio splitting to Elliptic and "
                "Deltoid. Drawn as vector outlines; the text inside the boxes measures as a "
                "separate block (p7-r5) that is excluded as a fragment of this chart.")
    excluded(7, 5, "fragment-of-other",
             "the middle box of the p7-r4 decision flow chart, re-cropped on its own: the "
             "'Ratio of distance between leaf tip and longest-width-position (D) to the leaf "
             "length (L)' box with arrow stubs top and bottom. Same exhibit as p7-r4, so "
             "counted once.")

    # p8 annotated tree structure, with three sub-pictures split out by the extractor
    figure(8, 1, "flowchart-or-schematic",
           note="the annotated 'STRUCTURE OF A TREE' illustration used for the 3D coordinate "
                "frame: leader-line labels (foliage, crown, bole, trunk, taproot, lateral "
                "roots and the rest) with an orange three-axis frame drawn on the stem, "
                "z running up the trunk. Three sub-pictures of the same artwork measure "
                "separately and are excluded as fragments.")
    excluded(8, 2, "fragment-of-other",
             "the tall narrow slice of the same tree illustration carrying the orange 'top' "
             "arrow and the canopy edge; its bbox sits inside p8-r1.")
    excluded(8, 3, "fragment-of-other",
             "the root-system band of the same illustration: branching roots with the "
             "'taproot' label, orange angle arrows and the clipped source credit "
             "'(http://www.infovisual.info/01/002_en.html)'. Same artwork as p8-r1.")
    excluded(8, 4, "fragment-of-other",
             "the root-collar band of the same illustration: basal flare with the 'trunk' and "
             "'lateral' labels and the orange angle arrows on the ground line; bbox inside "
             "p8-r1.")

    # p9 branch transformation frames
    figure(9, 1, "flowchart-or-schematic",
           note="the branch transformation frame for the angle rule: blue X, Y, Z axes with "
                "the rotated X' and Y' and the angles phi_i and omega_i marked.")
    figure(9, 2, "flowchart-or-schematic",
           note="the companion frame for the length and inclination rule: blue X, Y, Z axes "
                "with the tilted Z'' and Y'' and the angles theta_i and theta_l marked.")

    # 2.2.3 the three generated tree profiles
    figure(10, 1, "surface-or-3D", three_d="isometric",
           note="generated tree profile 1: a dense multicoloured segment canopy on one trunk, "
                "drawn in a dotted perspective box over a magenta ground ellipse.")
    figure(10, 2, "surface-or-3D", three_d="isometric",
           note="generated tree profile 2: a tall conifer, sparse tiered foliage on a single "
                "trunk, same perspective box and ground plot.")
    figure(10, 3, "surface-or-3D", three_d="isometric",
           note="generated tree profile 3: a broad flat umbrella canopy on a thin trunk, "
                "same perspective box and ground plot.")

    # 3.1 orbit figures and the spherical coordinate diagram
    figure(11, 1, "surface-or-3D", three_d="isometric",
           note="orbit of the sun, north-temperate example: a rendered globe with the "
                "yearly orbit drawn as stacked elliptical traces, the sun as a yellow dot, "
                "and the printed label 'Length of the day = 12.0 hours'.")
    figure(11, 2, "surface-or-3D", three_d="isometric",
           note="orbit of the sun, equatorial example: the same globe render with the orbit "
                "loops tilted parallel, sun upper right, same printed day-length label.")
    figure(11, 3, "surface-or-3D", three_d="isometric",
           note="orbit of the sun, arctic example: the same globe with four tall vertical "
                "loops and the sun overhead, same printed day-length label. The artwork is "
                "printed again verbatim on p12-r1.")
    figure(11, 4, "flowchart-or-schematic",
           note="the spherical-polar coordinate diagram for the brightness function: z axis, "
                "corner x and y axes, the solid radius vector r, and dashed arcs with "
                "arrowheads marking theta from z and phi in the xy plane; labels x, y, z, r, "
                "theta, phi. Monochrome line art.")

    # 3.2
    figure(12, 1, "surface-or-3D", three_d="isometric",
           note="the A/B sun-orbit figure of section 3.2: a verbatim re-use of the p11-r3 "
                "globe-and-loops artwork with two blue arrows added below it, printed again "
                "to show the shift from circle A to circle B between the solstices.")
    figure(12, 2, "flowchart-or-schematic",
           note="the sunlight-on-ground construction: two orange arrows labelled 'Sunlight' "
                "at inclination gamma over a blue 'Ground' line, a right triangle with the "
                "legs a and b, and the relation sin gamma = a/b set inside the drawing.")

    # 4.1
    figure(13, 1, "flowchart-or-schematic",
           note="the sunlight-exposure construction for a crown: a grey filled triangle crown "
                "on a slim trunk rectangle, one ray entering from the upper left labelled "
                "phi, and inside the crown a double-headed path from the entry point to the "
                "marked point P with the segment s labelled. Vector line art, monochrome.")
    figure(14, 1, "surface-or-3D", three_d="isometric", numbers=True,
           note="the modelled tree inside its coordinate box: branched skeleton, blue trunk, "
                "many small coloured leaf-cluster markers and magenta ground-projection "
                "points inside a red outline, three orange arrows under the title 'Direction "
                "of sunlight (Overhead)'. Tick numbers print on the box axes.")
    figure(14, 2, "surface-or-3D", three_d="isometric", numbers=True,
           note="the same scene from the side: canopy point cloud above the magenta ground "
                "leaf patch, the three orange 'Direction of sunlight (theta, phi)' arrows, "
                "axis numbers printed on the box.")

    # 4.2 matching, and the profile/leaf table
    figure(15, 1, "other", panels=2, layout="1x2",
           note="two leaf outlines labelled 'Elliptic' and 'Linear', the leaf-shape keys "
                "reprinted for section 4.2.",
           other_note="flat green leaf outline glyphs used as shape labels, neither "
                      "photographs nor plots")
    figure(15, 2, "other", panels=2, layout="1x2",
           note="two leaf outlines labelled 'Deltoid' and 'Palmate', the other half of the "
                "shape key.",
           other_note="flat green leaf outline glyphs used as shape labels, neither "
                      "photographs nor plots")
    figure(15, 3, "surface-or-3D", three_d="isometric",
           note="tree profile 1 of the matching study (semi-spherical): a rendered tree with "
                "a dense broad canopy on a dark trunk over a magenta ground ellipse.")
    figure(15, 4, "surface-or-3D", three_d="isometric",
           note="tree profile 2 (triangular/pine): a rendered conical tree widest at the "
                "base over a magenta ground patch.")
    figure(15, 5, "surface-or-3D", three_d="isometric",
           note="tree profile 3 (semi-spherical/banana): a rendered umbrella-crowned tree "
                "with near-horizontal low branches over the magenta ground patch.")
    figure(15, 6, "table-as-figure",
           labels=True,
           note="the profile/leaf comparison table, first half: a ruled raster table of "
                "rounded exposure ratios with a stub column of tree profiles ('Triangular: "
                "pine', 'Elliptic: poplar', 'Semi-spherical: banana') and leaf-shape icons "
                "in the stub. The grid is inside the raster, so the block is recorded as a "
                "table-as-figure exhibit rather than as a measured table.")
    figure(16, 1, "table-as-figure",
           labels=True,
           note="the second half of the same profile/leaf table, continued across the page "
                "break: the Palmate row (0.47, 0.62, 0.85) and the 'Shape chosen' and 'Real "
                "leaf shape' rows. Header row stays on p15, so this half carries no header.")
    figure(16, 2, "composite-panel", panels=4, layout="2x2", numbers=True,
           caption="This figure is the detailed implementation of poplar tree with Deltoid "
                   "leaves (numerical discretion is adopted).",
           note="the exposure figure for the chosen poplar/deltoid pairing: a 3D scatter of "
                "exposure against theta and phi, two 2D scatter panels of exposure against "
                "theta and against phi, and a bordered text box in the fourth quadrant, all "
                "inside one measured block. Tick numbers print on the three panels; no "
                "legend. The caption sentence prints inside the bordered box (p16-r3), which "
                "is why it is quoted from the text layer and not from a caption line.")
    excluded(16, 3, "fragment-of-other",
             "the bordered text box that holds the caption of the p16-r2 composite, sitting "
             "inside that block's bbox: 'This figure is the detailed implementation of "
             "poplar tree with Deltoid leaves (numerical discretion is adopted)'.")

    # 5.3 case study
    figure(20, 1, "surface-or-3D", three_d="isometric", numbers=True,
           note="the computer model of the case-study Cinnamomum camphora: a rendered tree "
                "inside a dotted coordinate box over a magenta shadow disc, tick numbers "
                "printed on the box axes.")
    figure(20, 2, "photo-or-raster-image",
           note="the outdoor photograph of the real Cinnamomum camphora in the park, with "
                "lawn, path and hedge and other trees behind it.")
    figure(21, 1, "flowchart-or-schematic",
           note="the sun-angle geometry for the crown: blue rays radiating from a central "
                "point through an orange circle. Vector line art, no axes and no plotted "
                "data, so schematic rather than line.")
    figure(22, 1, "surface-or-3D", three_d="isometric", numbers=True,
           note="the rendered camphor model again at the smaller scale used for the leaf-mass "
                "estimate, drawn from a slightly different angle, tick numbers on the box.")

    # p23 profile trio and the four regression scatter plots
    figure(23, 1, "surface-or-3D", three_d="isometric",
           note="crown profile 1 (semi-sphere): a rendered tree with a broad rounded crown "
                "over a magenta elliptical ground patch; the axis ticks are cut off by the "
                "crop.")
    figure(23, 2, "surface-or-3D", three_d="isometric",
           note="crown profile 2 (cone): a rendered tree with a sparse, narrow, drooping "
                "crown over the magenta ground patch.")
    figure(23, 3, "surface-or-3D", three_d="isometric",
           note="crown profile 3 (ellipsoid): a rendered tree with a blue-green canopy and "
                "magenta foliage markers over the ground ellipse.")
    figure(23, 4, "scatter", numbers=True,
           note="regression plot of the whole 30-tree data set: nine hollow markers rising "
                "with height, x 5-10 m, y 0-600, axis titles printed; 'Profile 2:' prints "
                "under it as the caption fragment.")
    figure(23, 5, "scatter", numbers=True,
           note="regression plot for profile 1: fifteen to eighteen hollow markers with a "
                "wide scatter and several near-vertical columns, y axis titled "
                "'Total_Leaf_Mass', y 0-1250.")
    figure(23, 6, "scatter", numbers=True,
           note="regression plot for profile 2: eight hollow markers in a tight monotone "
                "rise, y axis titled 'VAR00002', y 0-1250.")
    figure(23, 7, "scatter", numbers=True,
           note="regression plot for profile 3: nine hollow markers on a clean curve, y axis "
                "titled 'Total_Leaf_Mass', y 0-800.")

    rules = [
        "The paper prints no exhibit numbers and no caption lines, so every row is "
        "uncaptioned and every mention block is empty: first_page stays null rather than "
        "borrowing the nearest prose sentence [mention.first_page].",
        "The one caption the paper does print for a figure is set as a bordered text box "
        "inside the figure itself, so caption.verbatim quotes that sentence and the block "
        "holding the box is excluded as a fragment of the composite [caption.verbatim].",
        "Family follows the ink: a flat labelled leaf silhouette is neither a photograph nor "
        "a plot, so the six shape glyphs are recorded as other with an other_note saying "
        "what they are [geometry.family].",
        "Rendered scenes are surface-or-3D even when they are pictures of a real tree, "
        "because the ink is a computer rendering inside a projected axis box; only the one "
        "outdoor photograph of the camphor is photo-or-raster-image [geometry.family].",
        "The enum has no value for a perspective projection, so three_d reads isometric on "
        "every rendered scene and the notes say which of them print tick numbers "
        "[geometry.three_d].",
        "A raster of a ruled table is a table-as-figure exhibit, not a measured table: the "
        "p15/p16 profile comparison is split over the page break into two blocks and neither "
        "carries a measurable grid [geometry.family].",
        "One measured block can hold a whole multi-panel figure: p16-r2 carries a 3D scatter, "
        "two 2D scatters and a text box, recorded once as composite-panel with "
        "panel_count 4 [geometry.panel_count].",
        "A re-printed artwork is still an exhibit: p12-r1 repeats the p11-r3 globe and loops "
        "with two arrows added, and is recorded as its own item with the re-use named in the "
        "note rather than excluded as a duplicate [geometry.family].",
        "Section paths stop at the deepest extracted heading on the page, so the 2.2.2 "
        "sub-pictures carry 2.2.2.1 and the case-study pages carry 5.3.1 and 5.3.2 "
        "[place.section_path].",
    ]
    note = (
        "The paper numbers nothing: no Figure N, no Table N, no caption line anywhere in the "
        "text layer, so 48 measured exhibits are recorded uncaptioned and the record cannot "
        "report a printed-count gap. Two conventions carry weight here. First, the four leaf "
        "silhouettes on p6 and the outline pairs on p15 are shape keys, recorded as other "
        "rather than as photographs. Second, the 0.5 cm grid illustrations are photographed "
        "leaves with a vector overlay drawn on them; they stay photo-or-raster-image and are "
        "counted as the six measured stages of two illustrations, not as one exhibit. "
        "Unresolved: none by name - nothing in the paper is named and unmeasured - but the "
        "figure that the text calls 'the plot of data' on p23 has no printed caption, so its "
        "four panels are identified by the four printed 'Profile n:' fragments only."
    )
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": [],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": note,
    }
    out = PROXY / "pa31-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, 0 tables, "
          f"{len(payload['excluded_regions'])} excluded")
    bad = 0
    for (page, reg), item in sorted(ITEMS.items()):
        if item["caption_verbatim"]:
            try:
                schema.check_quote(item["caption_verbatim"], PID, [page - 1, page, page + 1],
                                   f"caption p{page}r{reg}", limit=None)
            except schema.Bad as exc:
                print("BAD", exc)
                bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
