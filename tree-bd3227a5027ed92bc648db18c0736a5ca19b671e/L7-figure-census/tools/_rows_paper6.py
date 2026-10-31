"""One-off: assemble paper 6 coder rows into the merged payload file.

Paper 6 is a two-method paper: a centroid method (Figures 2-7) and a cluster method
(Figures 8-14), each method shown as a flow chart, then a heat map over a 3D surface
pair per offender. Three exhibit classes needed judgement:

- p1 r1 is the MCM summary sheet band, not a figure: excluded.
- p17 r2-r7 and p26 r2 are label lines rasterised as small images inside a flow chart,
  so they are parts of the chart above them, not separate exhibits: excluded.
- p27 r1 is a dendrogram. The closed vocabulary has no dendrogram member and
  node-link-network would be wrong (it is a linkage tree over a numeric axis), so it is
  recorded as `other` with the shape named.
- p37 r1 is a printed table, not a figure: recorded as table-grid.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

# page, region, family, confidence, panels, is_table, caption, excluded, other_note, note
ROWS = [
    (1, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "MCM summary sheet band: control number, problem chosen, title, abstract text"),
    (13, 1, "map-or-plan-view", "high", 1, False,
     "Figure 1: Comparison of crime sequence for violent offender in LeBeau[9] and"
     " scatter plot of same data found through pixel analysis.", "", "",
     "left panel; boxed plan view with north arrow, 0-1 mi scale bar, star/square/triangle points"),
    (13, 2, "scatter", "high", 1, False,
     "Figure 1: Comparison of crime sequence for violent offender in LeBeau[9] and"
     " scatter plot of same data found through pixel analysis.", "", "",
     "right panel; x and y location in 5ft increments, ~17 open circles plus one star"),
    (17, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 2: Algorithm Flow Chart for Centroid Method", "", "",
     "vertical flow: Create Search Domain, Find Centroid, Build Likelihood Crater, Adjust for Temporal Trends, Weight by Previous Crimes, Output Likelihoods"),
    (17, 2, "", "high", 1, False, "", "in-body-diagram", "",
     "label line rasterised inside the Figure 2 flow chart"),
    (17, 3, "", "high", 1, False, "", "in-body-diagram", "",
     "label line rasterised inside the Figure 2 flow chart"),
    (17, 4, "", "high", 1, False, "", "in-body-diagram", "",
     "label line rasterised inside the Figure 2 flow chart"),
    (17, 5, "", "high", 1, False, "", "in-body-diagram", "",
     "label line rasterised inside the Figure 2 flow chart"),
    (17, 6, "", "high", 1, False, "", "in-body-diagram", "",
     "label line rasterised inside the Figure 2 flow chart"),
    (17, 7, "", "high", 1, False, "", "in-body-diagram", "",
     "label line rasterised inside the Figure 2 flow chart"),
    (19, 1, "line", "high", 1, False,
     "Figure 3: Example gamma probability density functions.", "", "",
     "(a) k=1 theta=.5; x 0-2.0, y labelled pdf, one smooth decaying curve"),
    (19, 2, "line", "high", 1, False,
     "Figure 3: Example gamma probability density functions.", "", "",
     "(b) k=4 theta=10; x 0-100, y labelled pdf, one smooth hump"),
    (20, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 4: Heat Map showing cratering technique applied to the crime sequence of"
     " Peter Sutcliffe", "", "",
     "jet heat raster over 0-600 location axes, crime points overlaid, colour bar"),
    (21, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 5: Offender C, Centroid Model Output", "", "",
     "(a) heat map, 0-80 location axes, single central hotspot, colour bar, crimes/next-crime legend"),
    (21, 2, "surface-or-3D", "high", 1, False,
     "Figure 5: Offender C, Centroid Model Output", "", "",
     "(b) 3D surface of the same likelihood, wireframe base, one broad peak"),
    (23, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 6: Offender B, Centroid Model Output", "", "",
     "(a) heat map, annulus-shaped hot ring, axis titles print x and y swapped"),
    (23, 2, "surface-or-3D", "high", 1, False,
     "Figure 6: Offender B, Centroid Model Output", "", "",
     "(b) 3D surface, near-vertical central spike, wireframe base"),
    (24, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 7: Offender A, Centroid Model Output", "", "",
     "(a) heat map, compact central hot blob, next-crime point sits well left of it"),
    (24, 2, "surface-or-3D", "high", 1, False,
     "Figure 7: Offender A, Centroid Model Output", "", "",
     "(b) 3D surface, narrow central spike, wireframe base"),
    (26, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 8: Algorithm Flow Chart for Cluster Method", "", "",
     "vertical flow with a hexagon For each cluster and a feedback arrow back into it"),
    (26, 2, "", "high", 1, False, "", "in-body-diagram", "",
     "boxed label rasterised inside the Figure 8 flow chart"),
    (27, 1, "other", "high", 1, False,
     "Figure 9: Dendrogram for Offender B", "",
     "dendrogram: a linkage tree with leaf indices on x and Gold Distance 0-8 on y; a hierarchical clustering tree, which the closed vocabulary has no member for",
     "single blue tree with about eight merger levels, no legend"),
    (28, 1, "line", "high", 1, False,
     "Figure 10: Offender B average Silhouette Values Vs Number of Clusters", "", "",
     "one line with four markers at 2, 2.5, 3, 4 clusters, y 0.3-1.0"),
    (28, 2, "scatter", "high", 1, False,
     "Figure 11: Offender B Crime Points Sorted into Four Clusters", "", "",
     "about 14 diamonds in four colour groups, no legend, x and y location 100-220"),
    (32, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 12: Offender C, Cluster Model Output", "", "",
     "(a) heat map, one warm blob, crimes and next-crime markers, colour bar"),
    (32, 2, "surface-or-3D", "high", 1, False,
     "Figure 12: Offender C, Cluster Model Output", "", "",
     "(b) 3D bell-shaped surface of the same likelihood"),
    (33, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 13: Offender B, Cluster Model Output", "", "",
     "(a) heat map, two to three warm blobs, crimes and next-crime markers"),
    (33, 2, "surface-or-3D", "high", 1, False,
     "Figure 13: Offender B, Cluster Model Output", "", "",
     "(b) 3D surface, one tall central spike plus secondary bumps"),
    (34, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 14: Offender A, Cluster Model Output", "", "",
     "(a) heat map, one warm blob, next-crime star far left of it"),
    (34, 2, "surface-or-3D", "high", 1, False,
     "Figure 14: Offender A, Cluster Model Output", "", "",
     "(b) 3D surface, one dominant spike plus a small secondary one"),
    (36, 1, "line", "high", 1, False,
     "Figure 15: Running Mean of Effectiveness Multiplier", "", "",
     "two curves, Cluster dash-star and Centroid solid, legend readable"),
    (36, 2, "line", "high", 1, False,
     "Figure 16: Effectiveness Multiplier vs. Crime Predicted", "", "",
     "two curves, Cluster spike near crime 9, Centroid smoother, y 0-25"),
    (37, 1, "", "high", 1, True,
     "Offender | kappa-bar_S | kappa_S : C 6.65 15.82 / B 8.473 22.95 / A 12.25 0.001",
     "", "",
     "printed three-column table, vertical rules and a header rule, no closing rule"),
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
    path = P / "P-B-2010-7507-24d34e5d-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
