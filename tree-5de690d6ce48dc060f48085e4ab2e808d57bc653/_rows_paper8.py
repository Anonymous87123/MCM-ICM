"""One-off: assemble paper 8 coder rows into the merged payload file.

Paper 8 draws twenty raster probability panels, lettered (a) to (t) across pages 22-32,
all on bare longitude/latitude frames with no basemap, so none of them is a map. Three
regions are typeset program listings (pages 14, 17, 20) and are not exhibits, and two
printed tables carry data (pages 25 and 27), the second one unnumbered.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

CAP_DECAY = "Figure 1: A decay plot."
CAP_PROB = "Figure 2: Example of a probability distribution. Red star signifies actual criminal's base."
CAP_BUF = "Figure 3: Varying buffer percentages to illustrate boundary conditions."
CAP_KILL = "Figure 4: Predicted Nth crime in red; actual Nth crime in black."
CAP_WEIGHT = "Figure 5: A decay plot."

ROWS = [
    (9, 1, "scatter", "high", 1, False, "", "", "",
     "about thirty crime points on three dashed reference rings, one centre marker; no axes"),
    (9, 2, "scatter", "high", 1, False, "", "", "",
     "twelve crime points forming a square ring around a centre marker, two dashed circles; no axes"),
    (10, 1, "scatter", "high", 1, False, "", "", "",
     "nine crime points on one line through the centre marker, two dashed circles; no axes"),
    (10, 2, "scatter", "high", 1, False, "", "", "",
     "about sixty crime points in two dense blocks flanking the centre marker; no axes"),
    (11, 1, "line", "high", 1, False, CAP_DECAY, "", "",
     "four decay curves (Linear, Normal, NE, Truncated NE) with legend, x Distance From Crime Scene, y Crime Probability"),
    (13, 1, "heatmap-or-contour", "high", 1, False, CAP_PROB, "", "",
     "blue-to-red density raster on Longitude/Latitude axes, two hot spots, crime dots and a red star"),
    (14, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "typeset program listing: Program 1 Criminal Location Finding Algorithm"),
    (15, 1, "heatmap-or-contour", "high", 1, False, "", "", "",
     "figure-eight density raster on an abstract 0-10 grid mislabelled Longitude/Latitude, nine square points"),
    (17, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "tail of the Program 1 listing, typeset pseudocode with no graphical marks"),
    (18, 1, "heatmap-or-contour", "high", 1, False, CAP_BUF, "", "",
     "panel (a) No buffer; density raster over real lat/long, two hot regions, crime dots"),
    (18, 2, "heatmap-or-contour", "high", 1, False, CAP_BUF, "", "",
     "panel (b) 30% buffer; same axes, one consolidated hot region"),
    (19, 1, "scatter", "high", 1, False, CAP_KILL, "", "",
     "kill number against year, about nine rising points and one black star for the actual crime"),
    (20, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "header block of the Program 3 typeset listing"),
    (20, 2, "", "high", 1, False, "", "not-an-exhibit", "",
     "body of the Program 3 typeset listing, no graphical marks"),
    (21, 1, "line", "high", 1, False, CAP_WEIGHT, "", "",
     "one smooth decaying weight curve, x Time (Days), y Weight, no markers"),
    (22, 1, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (a) Uncorrelated Unweighted; jet density over bare 0-100 pseudo-coordinates, oblique red ridge"),
    (22, 2, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (b) Uncorrelated Weighted; larger shifted red core plus a second lobe"),
    (22, 3, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (c) Correlated Unweighted; single continuous ridge with a long red core"),
    (22, 4, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (d) Correlated Weighted; broader red band with two lobes"),
    (23, 1, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (e) Correlated Unweighted; bimodal, two separate red maxima"),
    (23, 2, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (f) Correlated Weighted; two red lobes joined by a yellow band"),
    (25, 1, "", "high", 1, True,
     "Table 1: Search Costs / Error Distance using various functions for both the Sutcliffe"
     " and Chester Turner data.", "", "",
     "printed table: Method rows Linear and Neg. Exp., four value columns of slash-pairs, Sutcliffe group header"),
    (27, 1, "", "high", 1, True, "", "", "",
     "printed table of crime coordinates and dates for Zodiac Killer, Grim Sleeper and Jack the Ripper; unnumbered"),
    (28, 1, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (g) Sutcliffe Linear decay; smooth raster on real lat/long, one broad red core"),
    (28, 2, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (h) Sutcliffe Linear decay, next crime; one large red core, no basemap"),
    (29, 1, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (i) negative exponential; two separated red lobes"),
    (29, 2, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (j) next crime, negative exponential; single red core"),
    (29, 3, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (k) truncated negative exponential; two lobes joined by a thin yellow throat"),
    (29, 4, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (l) single red core; the in-figure title says next-crime although the caption says criminal-location"),
    (30, 1, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (m) plateaued negative exponential; two lobes joined by a broad ridge"),
    (30, 2, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (n) single large red core, barely separable from (h)"),
    (30, 3, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (o) normal decay; joined ridge, slightly broader than (m)"),
    (30, 4, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (p) single red core on a plain frame"),
    (31, 1, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (q) time-weighted negative exponential; two separated red lobes, red star present"),
    (31, 2, "heatmap-or-contour", "high", 1, False, "", "", "",
     "panel (r) next crime; single red core"),
    (32, 1, "heatmap-or-contour", "medium", 1, False, "", "", "",
     "panel (s) visually identical to (q), captioned Sutcliffe under the Chester Turner heading"),
    (32, 2, "heatmap-or-contour", "medium", 1, False, "", "", "",
     "panel (t) visually identical to (r), same caption mismatch"),
]


def main() -> None:
    out = []
    for page, region, family, conf, panels, table, caption, excluded, other, note in ROWS:
        out.append({
            "page": page, "region": region, "family": family, "confidence": conf,
            "panel_count": panels, "table": table, "caption_verbatim": caption,
            "caption_source": "text-layer" if caption else "none",
            "excluded": excluded or None, "other_note": other or None, "note": note,
        })
    path = P / "P-B-2010-8362-bd23db32-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
