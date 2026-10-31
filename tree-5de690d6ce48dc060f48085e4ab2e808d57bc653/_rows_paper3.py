"""One-off: assemble paper 3 coder rows into the merged payload file.

Paper 3 prints every exhibit as a raster image, so the geometry pass found all 23
image blocks and no vector rule table. Eight of the fifteen figures are two-panel:
the left panel carries the item (composite-panel, panel_count 2) and the right
panel is excluded as a fragment of the same exhibit.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

# page, region, family, confidence, panels, is_table, caption, excluded, other_note, note
ROWS = [
    (3, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 1: Arrows point in the positive direction for the corresponding parameter.",
     "", "",
     "labelled bat diagram: initial velocity, rotation, center-of-mass distance"),
    (4, 1, "line", "high", 1, False,
     "Figure 2: vf as a function of l.", "", "",
     "three curves in one axes: final velocity, effective mass, swing speed vs l"),
    (7, 1, "composite-panel", "high", 2, False,
     "Figure 3: Left: An image of a ball hitting a rigid wall. The compression is easily"
     " visible. Right: A hysteresis curve used in our modeling.", "", "",
     "Figure 3 spans r1+r2; r1 is the grayscale compression photo, r2 the hysteresis loop"),
    (7, 2, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 3, force vs compression hysteresis loop"),
    (8, 1, "composite-panel", "high", 2, False,
     "Figure 4: Left: The force between the ball and the bat as a function of time."
     " Right: The waveform of the y10(t) when the bat is struck at 60 cm.", "", "",
     "Figure 4 spans r1+r2; r1 is the force spike, r2 the displacement waveform"),
    (8, 2, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 4, y10(t) waveform"),
    (9, 1, "composite-panel", "high", 2, False,
     "Figure 5: Left: Exit velocity vs. impact position for a free boundary (solid line)"
     " and fixed boundary (dashed line). Right: The same graph for a free 110 cm bat.",
     "", "",
     "Figure 5 spans r1+r2; both panels are exit velocity vs impact position"),
    (9, 2, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 5, exit velocity vs position for the 110 cm bat"),
    (9, 3, "line", "high", 1, False,
     "Figure 6: Exit velocity vs. impact position at various initial angular velocities of"
     " the bat. Our model predicts the solid curves, while the dashed lines represent the"
     " simple model. The dots are at the points where Brody's solution is maximized.",
     "", "",
     "family of solid curves with dashed simple-model curves and Brody dots"),
    (10, 1, "composite-panel", "high", 2, False,
     "Figure 7: Left: Exit velocity minus impact velocity vs. impact position at various"
     " initial angular velocities of the bat. Right: The same plot without a hysteresis"
     " curve. The effect disappears.", "", "",
     "Figure 7 spans r1+r2; excess exit velocity, with and without hysteresis"),
    (10, 2, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 7, same curves without the hysteresis term"),
    (10, 3, "line", "high", 1, False,
     "Figure 8: Optimal impact position vs. angular velocity. The line is the rigid-body"
     " prediction, while the points are our model's prediction.", "", "",
     "one predicted line plus square markers for the model"),
    (10, 4, "other", "medium", 1, False, "Figure 9: The profile of our bat.", "",
     "thin bat side-profile silhouette between +/-0.03 marks; a shape drawing, no axes",
     "aspect-10 strip, 28 pt tall; the whole bat profile, not a fragment"),
    (11, 1, "composite-panel", "high", 2, False,
     "Figure 10: Exit velocity vs. impact position for various densities. The solid line is"
     " the original rho = 649 kg/m3. Left: Dotted is 700, dashed is 1000. Right: Dotted is"
     " 640, dashed is 500.", "", "",
     "Figure 10 spans r1+r2; density sweeps above and below the original"),
    (11, 2, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 10, lower-density sweep"),
    (11, 3, "composite-panel", "high", 2, False,
     "Figure 11: Left: Varying the value of Y. Solid is Y = 1.1814e10. Dashed is 1.25 times"
     " as much. Dotted is 0.8 times. Right: Varying the shape of the bat.", "", "",
     "Figure 11 spans r3+r4; Young's modulus sweep and bat shape sweep"),
    (11, 4, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 11, bat shape variants as solid/dashed/dotted"),
    (12, 1, "line", "high", 1, False,
     "Figure 12: Varying the velocity of the ball. Solid is the original 40 m/s. Dashed is"
     " 50 m/s while dotted is 60 m/s.", "", "",
     "three curves peaking near 0.7 m impact position"),
    (12, 2, "composite-panel", "high", 2, False,
     "Figure 13: Left: Corked Bat Right: aluminum bat.", "", "",
     "Figure 13 spans r2+r3; corked-bat and aluminum-bat exit velocity curves"),
    (12, 3, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 13, aluminum bat"),
    (13, 1, "composite-panel", "high", 2, False,
     "Figure 14: Plots of the displacement of an aluminum bat (dashed) and wood bat (solid)"
     " being hit by a ball 60 cm from the handle end.", "", "",
     "Figure 14 spans r1+r2; two displacement snapshots t=0.5 ms and t=1.05/1.10 ms"),
    (13, 2, "", "high", 1, False, "", "fragment-of-other", "",
     "right panel of Figure 14, second displacement snapshot"),
    (14, 1, "line", "high", 1, False,
     "Figure 15: Exit velocity vs. impact position at different hoop frequencies.", "", "",
     "seven coloured exit-velocity curves, wood bat plus five hoop frequencies"),
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
    path = P / "P-A-2010-7586-ff69029f-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
