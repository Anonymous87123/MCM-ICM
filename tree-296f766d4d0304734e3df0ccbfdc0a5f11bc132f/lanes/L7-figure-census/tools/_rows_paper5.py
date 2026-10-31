"""One-off: assemble paper 5 coder rows into the merged payload file.

Every exhibit is one raster image block, one caption below it. Captions sit under the
graphic in this paper, not above, so a caption is matched to the region directly above
its line. Six of the twelve exhibits are probability heatmaps that also carry a
node-link or point overlay; the overlay is named in the note and does not change the
family.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

# page, region, family, confidence, panels, is_table, caption, excluded, other_note, note
ROWS = [
    (8, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 1: The unstable behavior of a naive best fit circle.", "", "",
     "open circle of x marks, a hollow arrow, then an arc of x marks; no axes"),
    (9, 1, "node-link-network", "high", 1, False,
     "Figure 2: A circle in the road metric induced by the graph for the Manchester"
     " Leeds area of England. The highway system graph is black and the circle is grey.",
     "", "",
     "black nodes joined by black edges; the grey pixel staircase ring is the road-metric circle"),
    (10, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 3: This shows the distance from Sutcliffe's house under the road metric with"
     " an overlay of our graph representation of the nearby highway system. Sutcliffe's"
     " house is at the house symbol. Red corresponds to a very short distance", "", "",
     "blocky rainbow grid, red core, black node-link overlay and an x at the house point"),
    (11, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 4: This shows the estimated probability distribution for the 20th attack"
     " knowing the first 19. The dots represent the attacks and the 'x' denotes the actual"
     " location of the 20th attack. Red indicates the highest probability and", "", "",
     "blocky rainbow grid, yellow-red lobe upper centre, black attack dots and one x"),
    (12, 1, "node-link-network", "high", 1, False,
     "Figure 5: The best fit circle of the attack locations under the road metric. The"
     " circle is shown in black, the graph is shown in grey, and the kill locations are"
     " shown in red.", "", "",
     "grey nodes and edges, black pixel ring as the fitted circle, red kill dots"),
    (12, 2, "heatmap-or-contour", "high", 1, False,
     "Figure 6: The probability density estimated by Rossmo's model for the perpetrator's"
     " residence. Red indicates the highest probability. The actual location of Sutcliffe's"
     " house is shown with the house symbol.", "", "",
     "blocky rainbow grid, same colormap as Figure 4, attack dots, house symbol"),
    (13, 1, "surface-or-3D", "high", 1, False,
     "Figure 7: Rossmo's probability estimate as a surface.", "", "",
     "wireframe 3D box, unlabelled axes, single shaded surface rising to one peak"),
    (14, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 8: The distance from Wayne Williams' residence under the road metric.", "", "",
     "blocky rainbow grid with red hotspot, black road network drawn over the grid"),
    (14, 2, "heatmap-or-contour", "high", 1, False,
     "Figure 9: This shows our computed probability distribution for the 22nd attack"
     " knowing the first 21. The actual location of the 22nd attack is shown as an 'x'.",
     "", "",
     "blocky rainbow grid, attack dots and one x; the Figure 8 caption line sits just above"
     " the crop"),
    (15, 1, "node-link-network", "high", 1, False,
     "Figure 10: The best fit circle for the Atlanta child murders data.", "", "",
     "grey nodes and edges, black squares, red dots as a third layer; no axes"),
    (15, 2, "heatmap-or-contour", "medium", 1, False,
     "Figure 11: A colorized representation of the prediction made by Rossmo's model for"
     " the location of the criminal's residence with the locations of the crimes overlaid."
     " Wayne Williams' residence is represented by the house symbol.", "", "",
     "blocky rainbow grid, red block at centre, crime dots and a hollow house marker"),
    (16, 1, "surface-or-3D", "high", 1, False,
     "Figure 12: Rossmo's probability estimate as a surface.", "", "",
     "same wireframe box as Figure 7, flatter surface with a small left ridge"),
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
    path = P / "P-B-2010-7273-e234c9a6-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
