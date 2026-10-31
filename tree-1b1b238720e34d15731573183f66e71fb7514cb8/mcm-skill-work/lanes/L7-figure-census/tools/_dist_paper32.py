"""Hand pass for P-A-2012-16831-ec8f03fd (leaf shape, tree architecture, leaf mass, 54 pp).

The geometry pass measures 58 regions over 26 pages. The paper prints 28 figure labels
and 11 table labels, but only nine of those labels sit on a measurable block, and the
prose names just five numbers (Figure3, Figure 4, Figure 6, Figure 7, Figure 15).

Accounting: 54 figure items + 4 measured tables = 58, nothing excluded, because this
paper has no rules, cover rasters or page furniture that the extractor mistook for art.

Families, read off cropped page proxies:

* `flowchart-or-schematic` carries every line drawing: the two p5 parameter sketches, the
  sunlight geometry and the two leaf-dimension sketches of p12, the two-diamond overlap
  construction (p15 to p16-r4), the p22 h/d profile, the two p29 crown drawings and the
  p35 cone icon.
* `line` covers the curve plots: the MATLAB training-performance trace (p9-r1), the three
  hand-phyllotaxy stems (p11), the p14 blade pair, the SU-SAAngle curve figure (p17 and
  its verbatim re-print on p19), the six p20 overlap curves and the p27 critical-point
  curve. The p38-r2 comparison, drawn as marker polylines, is `line` too.
* `scatter` is the MATLAB regression cloud (p9-r2), the four p31 branch-pattern clouds,
  the p33 linear-fit cloud and the p38 fitted scatter.
* `node-link-network` is the p6 dendrogram and the p8 layer schematic.
* `composite-panel` is the leaf-bitmap plate: four measured blocks of labelled `.bmp`
  thumbnails, each its own grid.
* `photo-or-raster-image` is the leaf-scan montages (p9, p10), the annotated tree of p25
  and the cut-out tree of p35.
* `surface-or-3D` is the p12 plate model, the p14 plate scene and the two MATLAB
  illumination surfaces.
* `bar` is the p33-r2 block, which holds two bar panels under one printed caption line.
* The four measured tables are `table-grid`, each recorded from the band the extractor
  could see, with `continued` set where the body runs past that band.

Usage: python -I tools/_dist_paper32.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2012-16831-ec8f03fd"
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
HEADKIND = {h["label"]: h["kind"] for h in CTX["headings"]}


def cline(page: int, start: str, stop: str | None = None) -> str:
    """The printed caption as the text layer carries it, cut at `start`..`stop`."""
    raw = (LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
           / f"page-{page:04d}.txt").read_text(encoding="utf-8", errors="replace")
    for line in raw.splitlines():
        line = schema.norm(line)
        if start not in line:
            continue
        cut = line[line.index(start):]
        if stop and stop in cut:
            cut = cut[: cut.index(stop)]
        return cut.strip()
    raise KeyError((page, start))


ALTERNATIVES = ["2 Model of Leaf Description",
                "2.2 Leaf Classification Model",
                "2.2.2 The Process of Classification based on cluster analysis"]
NEURAL = ["2 Model of Leaf Description", "2.3 Model Testing Using Neural Network"]
RELATION = ["3 Model of the Relation", "Introduction", "Assumptions"]
CASE1 = RELATION + ["3.1 Building the Model", "3.1.1 Case 1: Horizontal Blade"]
CASE2 = RELATION + ["3.1 Building the Model", "3.1.2 Case 2: Inclined Leaf Blade"]
LIGHT = ["4 Model of the Relation", "Introduction", "Assumptions", "4.1 Light Distribution"]
SIZE = ["4 Model of the Relation", "Introduction", "Assumptions", "4.2 Leaf Size Model"]
PATTERN = ["5 Model of the Relation", "5.1 Introduction", "5.2 Logistic Regression Model"]
BRANCH = PATTERN + ["5.4 Relations of Leaf Shape and Branch Pattern"]
MASS = ["6 Model of Leaf Mass", "6.1 A Basic Volumetric Model"]

PATH = {
    5: ["2 Model of Leaf Description", "2.2 Leaf Classification Model",
        "2.2.1 Leaf Description"],
    6: ALTERNATIVES, 7: ALTERNATIVES,
    8: NEURAL, 9: NEURAL, 10: NEURAL,
    11: RELATION, 12: RELATION,
    14: CASE1, 15: CASE1, 16: CASE1, 17: CASE1, 19: CASE1,
    20: CASE2,
    22: CASE2 + ["3.2 Further Discussion"],
    25: LIGHT, 26: SIZE, 27: SIZE,
    28: SIZE + ["4.3 Result and Analysis"],
    29: PATTERN, 30: PATTERN + ["5.3 Testing of the Model"],
    31: BRANCH, 33: BRANCH,
    35: MASS, 36: ["6 Model of Leaf Mass", "6.2 An Improvement of the Model"],
    38: ["6 Model of Leaf Mass", "6.3 Allometric Equation Model",
         "6.3.2 A more accurate model considering the biological mechanism"],
}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

VENTION = {5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1, 15: 1, 16: 1,
           17: 1, 19: 1, 20: 1, 22: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1,
           31: 1, 33: 1, 35: 1, 36: 1, 38: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def place(page: int, reg: int | None) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    path = PATH[page]
    c = CTXREG[(page, reg)] if reg is not None else None
    return {
        "section_path": list(path),
        "section_numbered": True,
        "section_kind": HEADKIND[path[-1]],
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, numbering: str | None = None, position: str = "below") -> dict:
    if numbering is None:
        numbering = "none"
        if text.startswith("Table"):
            numbering = "Table N." if text.startswith("Table ") and text[6:7] != " " else "none"
        elif text.startswith("Figure"):
            numbering = "Figure N." if text.startswith("Figure ") else "Figure N"
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


def figure(page: int, reg: int, family: str, caption: str = "", *, numbering=None,
           panels: int = 1, layout: str = "1", legend: str = "none", three_d: str = "no",
           numbers: bool = False, labels: bool = False, colorbar: bool = False,
           mention: dict | None = None, note: str = "") -> None:
    ORDER.append((page, reg))
    pos = place(page, reg)
    blocking = dict(mention) if mention else dict(NULL_MENTION)
    if blocking["first_page"] is not None and blocking["lead_pages"] is None:
        blocking["lead_pages"] = page - blocking["first_page"]
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption,
        "caption_source": "text-layer" if caption else "none",
        "note": note,
        "place": pos,
        "mention": blocking,
        "caption": caption_block(caption, numbering),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }


def table(page: int, reg: int, caption: str, *, rows: int, cols: int,
          header_rows: int = 1, rule_style: str = "booktabs", zebra: bool = False,
          numeric_cols: int = 0, text_cols: int = 1, width: str = "full",
          continued: bool = False, note: str = "") -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": caption,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": dict(NULL_MENTION),
        "caption": caption_block(caption, None, "above"),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rule_style, "zebra": zebra, "merged_cells": False,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": width, "orientation": "portrait",
            "continued": continued, "note_sentence": "",
        },
    })


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            trail: str = "", count: int = 1, gap: int | None = None) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": trail,
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": gap}


def build() -> str:
    # 2.2.1 - the NR and LEA sketches, captions printed as one baseline
    figure(5, 1, "flowchart-or-schematic", cline(5, "Figure 1.", "Figure 2."),
           labels=True,
           note="the non-serrated-ratio sketch: a green lobed leaf outline with the centroid "
                "marked and the concave (Cci) and convex (Cvj) margin points joined in "
                "pairs by short tie-lines, the drawing behind eq1 of the NR definition.")
    figure(5, 2, "flowchart-or-schematic", cline(5, "Figure 2."),
           labels=True,
           note="the leaf-extended-angle sketch: a smooth ovate leaf with its midrib drawn "
                "and two construction lines meeting below the petiole at the printed "
                "label 'Extended Angle'.")
    # 2.2.2 - the dendrogram of the 32-leaf clustering
    figure(6, 1, "node-link-network", cline(6, "Figure 3."),
           numbers=True, labels=True,
           mention=mention(5, ["Figure3", "Figure 3"],
                           "The result of clustering is displayed in Figure3.",
                           "as-shown-in",
                           "Figure 3 shows that the 32 samples can be classified into "
                           "4 clusters.", count=2),
           note="R `hclust` dendrogram, title 'ward method', y axis 'Height' with ticks "
                "0-25, thirty leaf classes as rotated leaves, and thin red grouping bars "
                "marking the four clusters cut out of the tree. The caption below the "
                "15.4 x 14.9 pt plot is the only one on the page.")
    # the leaf-bitmap plate, four measured bands
    figure(6, 2, "composite-panel", panels=9, layout="2x5", labels=True,
           note="leaf-image plate block 1: nine grayscale leaf silhouettes in hairline "
                "boxes, each with its printed file name (Class50.bmp and the rest), under "
                "the printed heading 'type 1'.")
    figure(6, 3, "composite-panel", panels=5, layout="1x5", labels=True,
           note="leaf-image plate block 2: five elongated leaf silhouettes with file names "
                "under the printed heading 'type 2'.")
    figure(6, 4, "composite-panel", panels=7, layout="2x5", labels=True,
           note="leaf-image plate block 3: seven leaf silhouettes with file names, no "
                "heading of its own - the plate runs on from 'type 2' with no printed "
                "boundary.")
    figure(7, 1, "composite-panel", panels=9, layout="2x5", labels=True,
           note="leaf-image plate block 4: the last nine silhouettes of the plate, carrying "
                "the 'Type 4' heading that the text layer prints at the top of p6; the "
                "plate is one exhibit split over the page break, not four figures.")
    # 2.3 - network schematic and classifying flow chart
    figure(8, 1, "node-link-network", cline(8, "Figure 4."),
           labels=True,
           mention=mention(7, ["Figure 4"],
                           "The BPNN architecture used as the classifier for this research "
                           "(Figure 4)", "parenthetical"),
           note="three-layer network schematic: a column of four input circles, a column of "
                "three hidden circles with vertical dots, a single decision circle, and "
                "edges fanning between the layers; the layer names print beside them.")
    figure(8, 2, "flowchart-or-schematic", cline(8, "Figure 5."),
           labels=True,
           note="one-row process chart, seven boxes joined by arrows: Start, Get 32 leaf "
                "images from database, Coefficient extraction, Data preprocessing, Build "
                "neural network, Classify 8 images, Classification analysis. Its own label "
                "prints under it but no prose sentence ever names Figure 5.")
    # MATLAB outputs and the leaf montages of the classification demonstration
    figure(9, 1, "line", cline(9, "Figure 6", "Figure 7"),
           numbers=True, legend="inside", labels=True,
           mention=mention(8, ["Figure 6"],
                           "Figure 6 and Figure 7 are final results output from MatLab.",
                           "direct"),
           note="MATLAB training-performance plot: a falling blue Train trace on a log "
                "error axis, dotted Best and Goal lines, circled end point, and the "
                "printed 'Best Training Performance is 0.0094668 at epoch 13'.")
    figure(9, 2, "scatter", cline(9, "Figure 7"),
           numbers=True, legend="inside", labels=True,
           mention=mention(8, ["Figure 7"],
                           "Figure 6 and Figure 7 are final results output from MatLab.",
                           "direct"),
           note="MATLAB regression plot: open circles on the diagonal Fit line against the "
                "dashed Y=T reference, titled 'Training: R=0.99691', with the printed "
                "relation 'Output ~= 0.98*Target+0.043'.")
    figure(9, 3, "photo-or-raster-image", panels=10, layout="2x5", labels=True,
           note="leaf-scan montage 'Type 1': ten grayscale leaf silhouettes with their file "
                "names, the newly classified ones ringed by a blue rounded box - the "
                "rectangular frames the prose describes.")
    figure(9, 4, "photo-or-raster-image", panels=10, layout="2x5", labels=True,
           note="leaf-scan montage 'Type 2': ten silhouettes, five loose above and five "
                "inside a blue box below, with 'type 2' printed at the top and 'Type2' at "
                "the bottom edge.")
    figure(10, 1, "photo-or-raster-image", cline(10, "Figure 9."),
           panels=8, layout="2x5", labels=True,
           note="leaf-scan montage 'Type 3': eight silhouettes, five above and three below, "
                "the last (Class59.bmp) ringed in blue; this is the group the prose says is "
                "classified wrongly.")
    figure(10, 2, "photo-or-raster-image", cline(10, "Figure 9."),
           panels=10, layout="2x5", labels=True,
           note="leaf-scan montage 'Type 4': ten silhouettes in two rows of five with "
                "Class21.bmp ringed in blue. Both p10 blocks sit under the one printed "
                "caption, and the text layer shows no Figure 8 anywhere.")
    # 3 introduction - the phyllotaxis trio, printed left to right as r3, r2, r1
    figure(11, 3, "line", cline(11, "Figure 10."),
           labels=True,
           note="phyllotaxis panel 1 of 3 (leftmost): a stem with five green leaf outlines "
                "attached alternately on either side, the distichous arrangement.")
    figure(11, 2, "line", cline(11, "Figure 10."),
           labels=True,
           note="phyllotaxis panel 2 of 3 (middle): two pairs of green-filled lanceolate "
                "leaves whose bases wrap the stem, the decussate arrangement.")
    figure(11, 1, "line", cline(11, "Figure 10."),
           labels=True,
           note="phyllotaxis panel 3 of 3 (rightmost): the same stem in perspective with "
                "arrows striking the leaf planes and the inline tag 'Sunlight'. The three "
                "panels sit side by side in one row and share the single caption.")
    # 3 model - the plate scene and the three definition sketches
    figure(12, 1, "surface-or-3D", cline(12, "Figure 11."),
           three_d="perspective-bars",
           note="rendered plate model: three pale rectangular blades cantilevered "
                "alternately off a blue vertical post over a grey CAD ground grid, with "
                "cast shadows and an RGB axis triad at the base.")
    figure(12, 2, "flowchart-or-schematic", cline(12, "Figure 12."),
           labels=True,
           note="definition sketch 1 of 3: the z-up coordinate frame with the horizontal "
                "plane baseline, a tilted sunlight ray and the angles alpha and beta "
                "marked with right-angle ticks.")
    figure(12, 3, "flowchart-or-schematic", cline(12, "Figure 12."),
           labels=True,
           note="definition sketch 2 of 3: one leaf drawn as a diamond on the vertical "
                "axis through a circled 'Shoot', with dimension brackets for width, length "
                "and petiole.")
    figure(12, 4, "flowchart-or-schematic", cline(12, "Figure 12."),
           labels=True,
           note="definition sketch 3 of 3: two leaf pairs on the z axis about Y, an "
                "'Internode' point, the internode depth delta-h and the angle gamma. The "
                "three sketches are separate drawings under one caption.")
    table(12, 5, cline(12, "Table 1."), rows=2, cols=4, header_rows=1,
          rule_style="booktabs", zebra=True, numeric_cols=1, text_cols=3,
          continued=True,
          note="variable-definition table: the measured band holds the header row "
               "('Variable name / Corresponding note / Value rage / Physical Meaning') and "
               "the SA-Angle row only. The body runs on at the top of p13 with the "
               "SD-Angle, Leaf-Index, p-length, LI-Angle and Inter-length rows and the "
               "closing note, where p13 shows 48 paths and no measured region, so this "
               "block is the head of Table 1 and not the whole table.")
    # 3.1.1 horizontal blade
    figure(14, 1, "line", cline(14, "Figure 13."),
           panels=2, layout="1x2", labels=True,
           note="the two-case key: left, two pairs of horizontal lens-shaped leaves in one "
                "plane; right, two pairs of narrow lance-shaped leaves angled upward. The "
                "printed headings 'Horizontal Blade' and 'Inclined blade' sit above it.")
    figure(14, 2, "surface-or-3D", three_d="perspective-bars",
           note="the rendered inclined-blade scene: a mauve vertical pole carrying pale "
                "blades in two tiers over a light ground grid with cast shadows; no printed "
                "caption of its own.")
    figure(15, 1, "flowchart-or-schematic", cline(15, "Figure 14."),
           numbers=True, legend="inside", labels=True,
           note="the overlap construction: two 45-degree rotated squares crossing at the "
                "origin, solid for the down layer and dash-dot for the upper layer, the "
                "three overlap labels OL1-OL3 and a hatched region, with a full coordinate "
                "frame - the only panel of this figure.")
    figure(16, 1, "flowchart-or-schematic", cline(16, "Figure 15."),
           numbers=True, labels=True,
           mention=mention(16, ["Figure 15"],
                           "Figure 15 shows displacement with SDAngle=45,90,135 degree.",
                           "figure-n-shows"),
           note="displacement panel 1 of 3: the same two-diamond construction with the "
                "upper layer shifted down-right and a 'Displacement' arrow at the bottom.")
    figure(16, 2, "flowchart-or-schematic", cline(16, "Figure 15."),
           numbers=True, legend="inside", labels=True,
           mention=mention(16, ["Figure 15"],
                           "Figure 15 shows displacement with SDAngle=45,90,135 degree.",
                           "figure-n-shows"),
           note="displacement panel 2 of 3: the offset increased, boxed 'upper / down' "
                "key at mid-right, the same displacement arrow.")
    figure(16, 3, "flowchart-or-schematic", cline(16, "Figure 15."),
           numbers=True, labels=True,
           mention=mention(16, ["Figure 15"],
                           "Figure 15 shows displacement with SDAngle=45,90,135 degree.",
                           "figure-n-shows"),
           note="displacement panel 3 of 3: the largest offset, arrow at the base. The "
                "three panels print in one row and carry the single caption that the "
                "sentence 'Figure 15 shows displacement with SDAngle=45,90,135 degree' "
                "describes.")
    figure(16, 4, "flowchart-or-schematic", cline(16, "Figure 16."),
           labels=True,
           note="the magnification of one corner: two thick strokes meeting at A, the "
                "dash-dot trace back to B, the intersection C and the double-headed "
                "arrow - what the text calls magnifying 'the second figure' to show the OL "
                "sidelength.")
    # 3.1.1 result curves, figure and its re-print
    figure(17, 1, "line", cline(18, "Figure 17."),
           numbers=True, legend="inside",
           note="SU-SAAngle curves for the three leaf indices (dotted 1:1, dash-dot 2:1, "
                "solid 8:1), all peaking near SAAngle 0.5 pi and dipping around 0.15 and "
                "0.8 pi. The artwork fills the foot of p17 and its caption prints at the "
                "top of p18, above Table 2.")
    figure(19, 1, "line", cline(19, "Figure 17."),
           numbers=True, legend="inside",
           note="the same three curves printed again for the petiole case, under the same "
                "printed number and the same caption, this time above Table 3. Curve for "
                "curve identical to p17-r1, but it is a re-print with its own place in the "
                "argument, so it is counted as its own exhibit.")
    # 3.1.2 inclined blade - six panels in three cases of two
    figure(20, 1, "line", cline(20, "Figure 18. SDAngle is 0"),
           numbers=True, legend="inside", labels=True,
           note="SDAngle 0 case, left panel (leaf index 8:1): the two shade profiles on "
                "the coordinate frame with the OL1-OL3 loops marked.")
    figure(20, 2, "line", cline(20, "Figure 18. SDAngle is 0"),
           numbers=True, legend="inside", labels=True,
           note="SDAngle 0 case, right panel (leaf index 1:1): the wider frame with the "
                "three loops; the caption prints at the foot of this panel.")
    figure(20, 4, "line", cline(20, "Figure 18. SDAngle is 45 degree"),
           numbers=True, legend="inside", labels=True,
           note="SDAngle 45 case, left panel: the profile cut by an oblique band with OL2 "
                "above and OL1 below.")
    figure(20, 3, "line", cline(20, "Figure 18. SDAngle is 45 degree"),
           numbers=True, legend="inside", labels=True,
           note="SDAngle 45 case, right panel: the rotated frame, the profile strongly "
                "elongated with the origin at the right edge.")
    figure(20, 6, "line", cline(21, "Figure 19."),
           numbers=True, legend="inside", labels=True,
           note="SDAngle 90 case, left panel: the traces collapsing to a cusp at the "
                "origin, with tick-bar callouts on the OL labels. Its caption is the "
                "'Figure 19. SDAngle is 90 degree' line printed at the top of p21.")
    figure(20, 5, "line", cline(21, "Figure 19."),
           numbers=True, legend="inside", labels=True,
           note="SDAngle 90 case, right panel: the compact stacked arrangement of the two "
                "loops. The paper prints 'Figure 18' on both its first two cases and "
                "'Figure 19' on the third.")
    figure(22, 1, "flowchart-or-schematic", cline(22, "Figure 19. a common case"),
           numbers=True, labels=True,
           note="the common-case profile: a thick closed leaf outline pointed at the "
                "origin with a hatched interior, the vertical line d, the height h and a "
                "full coordinate frame - the rectangular d x h approximation the prose "
                "describes. Re-uses the number 19 a second time.")
    # 4.1 to 4.3
    figure(25, 1, "photo-or-raster-image", cline(25, "Figure 20."),
           labels=True,
           note="the annotated tree: a colour photograph-style canopy on a brown trunk with "
                "black dimension arrows for the height h and the canopy width D, and the "
                "printed words 'Testing point' and 'Trunk'.")
    figure(26, 1, "surface-or-3D", cline(26, "Figure 21."),
           three_d="surface-mesh", colorbar=True, numbers=True,
           note="MATLAB surface of relative illumination intensity over height and radius, "
                "with a colour bar, titled 'light distibution within a tree'.")
    figure(27, 1, "line", cline(27, "Figure 21."),
           numbers=True, labels=True,
           note="the critical-point curve: one rising S-curve from (5, 0.2) to (20, 1.0) "
                "with dashed guides annotated 'Min light needed', 'Min size' and 'Critical "
                "point'. This is the second figure printed under the number 21.")
    figure(28, 1, "surface-or-3D", cline(28, "Figure 22."),
           three_d="surface-mesh", colorbar=True, numbers=True,
           note="MATLAB surface of leaf area over height and radius in mm2, colour bar "
                "45-60, titled 'leaf area distribution'.")
    # 5 branch pattern
    figure(29, 1, "flowchart-or-schematic", cline(29, "Figure 23."),
           labels=True,
           note="orthotropic crown drawing: a hand-drawn trunk with one horizontal branch "
                "whose curved arms end in level fan-shaped leaf clusters.")
    figure(29, 2, "flowchart-or-schematic", cline(29, "Figure 23."),
           labels=True,
           note="plagiotropic crown drawing: a V-forked branch whose arms carry clusters of "
                "long narrow leaves angled up and out. The two drawings are the first use of "
                "the number 23.")
    table(30, 1, cline(30, "Table 5."), rows=3, cols=6, header_rows=1,
          rule_style="no-rules", zebra=True, numeric_cols=5, text_cols=1,
          note="classification-result table: the measured band holds the header sliver, the "
               "green-filled 'Correct-classified species' row (126 93 90 105 414) and the "
               "accuracy row (0.99 0.85 0.88 0.89 0.91). Drawn with fills and no rules.")
    figure(31, 2, "scatter", cline(31, "Figure 23. differences"),
           numbers=True, legend="inside",
           note="branch-pattern cloud 1 of 4 (left of the first row): petiole length against "
                "blade length, plus signs for plagiotropic and open squares for "
                "orthotropic, legend box in the top right.")
    figure(31, 1, "scatter", cline(31, "Figure 23. differences"),
           numbers=True, legend="inside",
           note="branch-pattern cloud 2 of 4 (right of the first row): the same two series "
                "with a wider x range and a sliver of the neighbouring frame at the edge.")
    figure(31, 3, "scatter", cline(31, "Figure 23. differences"),
           numbers=True, legend="inside",
           note="branch-pattern cloud 3 of 4 (left of the second row): the denser cloud with "
                "y clamped at 7, some squares tinted pale blue.")
    figure(31, 4, "scatter", cline(31, "Figure 23. differences"),
           numbers=True, legend="inside",
           note="branch-pattern cloud 4 of 4 (right of the second row): a tight low cluster "
                "with a few high outliers. All four share the one printed caption, the "
                "second use of the number 23.")
    figure(33, 1, "scatter", cline(33, "Figure 23. relation"),
           numbers=True, legend="inside",
           note="petiole length against length-width ratio with a red least-squares line "
                "through the open squares, R2=0.86 in the prose. Third use of the number "
                "23, this time with different words.")
    figure(33, 2, "bar", cline(33, "Figure 24.", "figure 25."),
           panels=2, layout="1x2", numbers=True, legend="inside",
           note="two bar panels in one measured block: the left panel counts simple versus "
                "compound-leaved species in the four areas (SA-P through NQ-O, scale 0-100) "
                "and the right panel the plagiotropic/orthotropic split (scale 0-250). The "
                "left is Figure 24 and the right is the only 'figure 25.' the paper prints: "
                "lower case, tucked inside the Figure 24 line, with no caption of its own.")
    # 6 leaf mass
    figure(35, 1, "photo-or-raster-image", cline(35, "Figure 26."),
           note="the cut-out tree against white: trunk, branches and a dense green canopy "
                "with soft photographic edges and a faint ground shadow, no annotation of "
                "any kind.")
    figure(35, 2, "flowchart-or-schematic", cline(35, "Figure 26."),
           labels=True,
           note="the volumetric-model icon: a thin-outline cone seen slightly from below "
                "with its internal dashed axis, the labels h and r, and a thick green bar "
                "standing for the trunk.")
    table(35, 3, cline(35, "Table 9."), rows=2, cols=10, header_rows=1,
          rule_style="booktabs", zebra=True, numeric_cols=9, text_cols=1,
          continued=True,
          note="leaf-mass estimation table: the measured band is the green-ruled header "
               "('tree, CH(m), CR(m), Cylinder, Vertical ellipsoid, Paraboloid, Cone, "
               "Sphere, Pyramid, measured LM(g)') plus the top of the first data row; the "
               "fourteen oak rows run past the block and its own summary row reappears "
               "above Table 10.")
    table(36, 1, cline(36, "Table 10."), rows=2, cols=7, header_rows=1,
          rule_style="booktabs", zebra=True, numeric_cols=6, text_cols=1,
          note="the comparison table's summary row: the stub 'mean fraction to MLM' with "
               "1.80, 1.18, 1.09, 0.60, 3.44 and 1.75 for the six solids. The header row "
               "prints just above the measured band.")
    # 6.3 allometric model
    figure(38, 1, "scatter", cline(38, "Figure 27."),
           numbers=True, legend="inside",
           note="leaf mass against DBH: nine measured crosses with one smooth red fitted "
                "curve, R2=0.98 in the prose; x 5-45 cm, y 0-2.5e4 g.")
    figure(38, 2, "line", cline(38, "Figure 28."),
           numbers=True, legend="inside",
           note="the two-model comparison: plus signs for the measured leaf mass, black "
                "squares for the equation 1 estimates and green/blue triangles for "
                "equation 2, joined by faint polylines, with both axes titled.")

    rules = [
        "One caption baseline can carry two labels: p5 prints 'Figure 1. NR' and "
        "'Figure 2. LEA' side by side under two 99 pt rasters, so each row quotes only its "
        "own half of that line [caption.verbatim].",
        "The prose names five numbers only - Figure3, Figure 4, Figure 6, Figure 7 and "
        "Figure 15 - so the other rows keep mention.first_page null instead of borrowing a "
        "caption line that happens to sit on the exhibit page [mention.first_page].",
        "Number reuse is the norm here: Figure 18 covers two cases, Figure 19 two, Figure 21 "
        "two and Figure 23 four, so a printed number is an attribution aid and never a count "
        "[caption.numbering].",
        "A caption printed on the following page still belongs to the artwork above the page "
        "break: p17-r1 takes the caption at the top of p18 and p20-r6 takes the one at the "
        "top of p21 [caption.position].",
        "Labels skip numbers: Figure 8 is never printed, and a lower-case 'figure 25.' is "
        "tucked inside the Figure 24 caption line without ever getting a caption of its own "
        "[caption.verbatim].",
        "A labelled grid of separate leaf scans is a composite-panel, not a photo-or-raster "
        "image, because every thumbnail carries its own printed file name [geometry.family].",
        "A rendered scene with a ground grid and cast shadows reads perspective-bars, while a "
        "MATLAB illumination map reads surface-mesh with a colour bar [geometry.three_d].",
        "A table whose measured band holds only a header and one row is still one table-grid "
        "entry, with table.continued true where the body runs past the block "
        "[table.continued].",
        "Seven printed tables - Tables 2, 3, 4, 6, 7, 8 and 11 - are laid out as rule-less "
        "text with no measured region at all, so the four table-grid entries in this record "
        "are a lower bound on the printed tables [table.rule_style].",
        "Section paths stop at the deepest heading printed on the page, so the two p5 "
        "sketches carry 2.2.1 while the dendrogram below the heading carries 2.2.2 "
        "[place.section_path].",
    ]
    note = (
        "Twenty-six pages carry art: 58 measured regions, of which 54 are figure blocks and "
        "four are the bands of printed tables. The paper numbers 28 figures and 11 tables, "
        "but numbers and blocks do not correspond. Four numbers are printed twice and one "
        "four times (18, 19, 21, 23), Figure 8 is skipped, and 'figure 25.' is printed lower "
        "case inside the Figure 24 caption line, so eleven printed labels attach to fifteen "
        "blocks. Five prose sentences name an exhibit by number; every other caption is a "
        "label the text never repeats. Three exhibits are identified by position only: the "
        "leaf-bitmap plate runs from p6 to p7 with its 'type 1' to 'Type 4' headings spread "
        "over four measured bands, and the p9 and p10 leaf montages carry no number until "
        "the Figure 9 line under the p10 pair. Unmeasured: the tail of Table 1 (p13, 48 "
        "paths), Tables 2 to 4 and 6 to 8 (p18, p19, p21, p32 - p32 shows 154 paths and no "
        "measured region), Table 11, and the unnumbered sensitivity table on p23 (28 paths, "
        "no region) - all print as rule-less text with no layout block of their own and are "
        "named in the findings rather than invented as rows. Nothing else in the paper is "
        "named and unmeasured."
    )
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": [],
        "rules": rules,
        "note": note,
    }
    out = PROXY / "pa32-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, "
          f"{len(payload['tables'])} tables, 0 excluded")
    bad = 0
    for (page, reg), item in sorted(ITEMS.items()):
        if item["caption_verbatim"]:
            try:
                schema.check_quote(item["caption_verbatim"], PID, [page - 1, page, page + 1],
                                   f"caption p{page}r{reg}", limit=None)
            except schema.Bad as exc:
                print("BAD", exc)
                bad += 1
    for n, t in enumerate(TABLES, 1):
        try:
            schema.check_quote(t["caption_verbatim"], PID,
                               [t["page"] - 1, t["page"], t["page"] + 1],
                               f"table {n} caption", limit=None)
        except schema.Bad as exc:
            print("BAD", exc)
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
