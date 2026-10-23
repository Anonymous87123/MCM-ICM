"""One-off: assemble paper 7 coder rows into the merged payload file.

Paper 7 is all vector drawings: two printed tables, one sector-grid schematic, one
horizontal bar chart, one line with confidence bars, one embedded basemap, and the rest
heat maps. The five heat maps of Figure 6 are five measured regions and five items.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

# page, region, family, confidence, panels, is_table, caption, excluded, other_note, note
ROWS = [
    (9, 1, "", "high", 1, True,
     "Table 1: Description of data sets with accuracy score for temporal exponential decay model.",
     "", "",
     "printed table: Description / Number of Crimes / Accuracy of Temporal Exponential Decay Model, nine data-set rows"),
    (11, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 1: The discretization of a square search area into sectors. In this figure k"
     " is equal to the side length of the search area divided by ds.", "", "",
     "grid of boxed cells S_1,1 to S_k,k with a bracket marked ds; no axes, no data"),
    (16, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 2: Comparison of prioritized search areas of a hypothetical criminal"
     " committing crimes along the unit circle given by a centralization method and a"
     " decay method.", "", "",
     "left panel; jet raster, radial blob, eight crime dots on a ring, colour bar, axes -3.2 to 3.2"),
    (16, 2, "heatmap-or-contour", "high", 1, False,
     "Figure 2: Comparison of prioritized search areas of a hypothetical criminal"
     " committing crimes along the unit circle given by a centralization method and a"
     " decay method.", "", "",
     "right panel; same axes and colour bar, annulus-shaped red field with crime dots on the inner ring"),
    (17, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 3: Prioritized search area for a hypothetical serial criminal travelling east"
     " over time, as given by the exponential decay and temporal exponential decay models.",
     "", "",
     "left panel; horizontal elliptical streak along y=0, dash-dot crime markers, colour bar"),
    (17, 2, "heatmap-or-contour", "high", 1, False,
     "Figure 3: Prioritized search area for a hypothetical serial criminal travelling east"
     " over time, as given by the exponential decay and temporal exponential decay models.",
     "", "",
     "right panel; ellipse shifted right with a separate compact hotspot at its right end"),
    (18, 1, "bar", "high", 1, False,
     "Figure 4: Comparison of the relative performance of each of our models on all of our"
     " data sets.", "", "",
     "horizontal bars with red error whiskers, x axis Hit Score 0.0-0.5, method names on y"),
    (19, 1, "line", "high", 1, False,
     "Figure 5: Hit score by number of crimes observed using a exponential decay model and"
     " 50% confidence intervals.", "", "",
     "single series with round markers and vertical 50% CI bars, x 2-14 crimes, y 0.00-0.35"),
    (20, 1, "", "high", 1, True,
     "Table 2: Models with associated hit scores and 95% confidence intervals.", "", "",
     "printed table: Model / Hit Score / 95% Confidence, eleven model rows"),
    (21, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 6: Prioritized search areas resulting from using different weights in the"
     " aggregation model of a circle center and exponential decay for the Beltway Sniper.",
     "", "", "panel (a); compact red core at centre, crime dots near it, 10 km scale bar"),
    (21, 2, "heatmap-or-contour", "high", 1, False,
     "Figure 6: Prioritized search areas resulting from using different weights in the"
     " aggregation model of a circle center and exponential decay for the Beltway Sniper.",
     "", "", "panel (b); elongated north-south hot oval, points on a near-vertical string"),
    (21, 3, "heatmap-or-contour", "medium", 1, False,
     "Figure 6: Prioritized search areas resulting from using different weights in the"
     " aggregation model of a circle center and exponential decay for the Beltway Sniper.",
     "", "", "panel (c); oval core shifted up-right, points clustered on and above it"),
    (21, 4, "heatmap-or-contour", "medium", 1, False,
     "Figure 6: Prioritized search areas resulting from using different weights in the"
     " aggregation model of a circle center and exponential decay for the Beltway Sniper.",
     "", "", "panel (d); dimmest and most compact core of the four upper panels"),
    (21, 5, "heatmap-or-contour", "high", 1, False,
     "Figure 6: Prioritized search areas resulting from using different weights in the"
     " aggregation model of a circle center and exponential decay for the Beltway Sniper.",
     "", "", "panel (e); narrowest spread, red core with a small yellow-green halo"),
    (23, 1, "scatter", "medium", 1, False,
     "Figure 7: Standard deviation rectangles and ellipses for the murders committed by"
     " Peter Sutcliffe.", "", "",
     "left panel; about five points in a lat/long frame with two nested axis-aligned rectangles, 20 km scale bar"),
    (23, 2, "scatter", "medium", 1, False,
     "Figure 7: Standard deviation rectangles and ellipses for the murders committed by"
     " Peter Sutcliffe.", "", "",
     "right panel; same points with two concentric tilted ellipses and a cross at the centre"),
    (24, 1, "map-or-plan-view", "high", 1, False,
     "Figure 8: Comparison of the prioritized search area produced by the temporal"
     " exponential decay model to the map of the geographical area of murders committed by"
     " Peter Sutcliffe.", "", "",
     "top panel; hill-shaded basemap with place labels (Leeds, Bradford, Sheffield...) and about twelve overlaid crime circles"),
    (24, 2, "heatmap-or-contour", "high", 1, False,
     "Figure 8: Comparison of the prioritized search area produced by the temporal"
     " exponential decay model to the map of the geographical area of murders committed by"
     " Peter Sutcliffe.", "", "",
     "bottom panel; raster probability surface, one hot core with a tail to the lower left, 20 km scale bar"),
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
    path = P / "P-B-2010-7947-b6007ae0-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
