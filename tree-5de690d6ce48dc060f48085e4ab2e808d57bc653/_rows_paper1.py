"""One-off: assemble paper 1 coder rows into the merged payload file.

Rows are the visual verdicts returned by the crop readers; this file only joins them
and normalises fields. Final region indices are the post-fix measured indices.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

# page, region, family, confidence, panels, is_table, caption, caption_source, excluded, other_note, note
ROWS = [
    (6, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 1. Illustration of theoretical derivation", "typed", "", "",
     "bat schematic, velocity vectors vf/vi, angles, L and b arrows"),
    (11, 1, "line", "medium", 4, False,
     "Figure 2. Longitudinal sections and cross sections for Hoop Modes of standard bat [Russell",
     "typed", "", "", "three stacked hoop-mode traces on a shared 0-34 axis, same family so panel_count 4"),
    (11, 2, "flowchart-or-schematic", "high", 1, False,
     "Figure 3. scheme for double spring model", "typed", "", "",
     "spring-element diagram, k_ball/e_ball and k_bat/e_bat"),
    (13, 1, "table-grid", "high", 1, True,
     "Table 1 The interrelationship between parameters and effects on BBS", "typed", "", "",
     "ruled 6-column table, arrows and smiley cells"),
    (15, 1, "line", "medium", 1, False,
     "Figure 4  The Data used for Fitting Formula, cited from Bahill and Freitas paper", "typed", "", "",
     "two fitted curves with square data points"),
    (16, 1, "flowchart-or-schematic", "medium", 1, False,
     "Figure 5. A typical example of corked bat", "typed", "", "", "hatched cross-section, h d L arrows"),
    (17, 1, "table-grid", "high", 1, True,
     "Table 2 Data used for simulation", "typed", "", "", "ruled 3-column parameter table"),
    (18, 1, "line", "high", 1, False,
     "Figure 6. The plot of the sweet spot location as the ball speed v_i ranges from 31m/s to 50 m/s.",
     "text", "", "", "framed axes, flat tip reference plus gently decreasing sweet-spot line"),
    (18, 2, "", "high", 1, False, "", "none", "fragment-of-other", "",
     "band inside r1: sweet-spot annotation text and arrow"),
    (19, 1, "line", "high", 1, False,
     "Figure 7. The plot of the sweet spot location as the swinging speed V_i ranges from 19m/s to 29 m/s.",
     "text", "", "", "same template as Figure 6, two lines"),
    (20, 1, "line", "high", 1, False,
     "Figure 8. The plot of the sweet spot as swinging angular velocity ranges from 43 to 61 s-1.",
     "text", "", "", "two lines vs angular velocity, coarser ticks"),
    (21, 1, "line", "high", 1, False, "", "none", "", "",
     "single curve v1(BBS) vs bat position, sweet spot and tip labelled"),
    (22, 1, "line", "high", 1, False, "", "none", "", "",
     "three curves e_ball 0.4/0.5/0.6 vs k_ball/k_bat, log x"),
    (23, 1, "line", "high", 1, False,
     "Figure 11  The maximum BBS (v_max) is a function of equivalent BBCOP", "typed", "", "",
     "three curves with e_ball arrows"),
    (23, 2, "flowchart-or-schematic", "high", 1, False,
     "The procedure to simulate is shown as following", "typed", "", "",
     "three-row block flow diagram through Equations 18, 14, 4"),
    (24, 1, "line", "high", 1, False,
     "Figure 12  The relationship between omega_i and J is illuminated by an empirical equation.",
     "typed", "", "", "single decreasing line"),
    (24, 2, "line", "high", 1, False,
     "Figure 13  The Location of sweet spot is determined by moment of inertia", "typed", "", "",
     "single rising line"),
    (25, 1, "line", "high", 1, False, "", "none", "", "",
     "single rising line v1max vs J, Figure 14 caption below crop"),
    (26, 1, "line", "high", 1, False,
     "Figure 15  The plot of swinging bat speed V_i as the function of the corked bat mass M",
     "typed", "", "", "single decreasing curve"),
    (26, 2, "line", "high", 1, False,
     "Figure 16. The plot of sweet spot location as the function of the corked bat mass M.",
     "text", "", "", "single monotone-decreasing curve"),
    (27, 1, "line", "high", 1, False,
     "Figure 17. The maximum BBS v_f,max as the function of the corked bat mass M.", "text", "", "",
     "single saturating curve"),
    (27, 2, "line", "high", 1, False,
     "Figure 18 The plot of batted-ball speed v_f and swinging bat speed V_i as the function of the corked bat mass M.",
     "text", "", "", "framed axes, saturating v_f plus dashed V_i, pasted inset at lower right coded as r3"),
    (27, 3, "", "high", 1, False, "", "none", "fragment-of-other", "",
     "grayscale Ideal Bat Weight screenshot pasted inside Figure 18 axes"),
    (28, 1, "surface-or-3D", "high", 1, False,
     "Figure 19 Figure in a wireframe mesh style, rho_cork = 450 kg/m3", "text", "", "",
     "3D surf, colorbar, base contours, datatip 48.74"),
    (29, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 20 Same Figure in contour style.", "text", "", "",
     "flat labelled contour map 48.58-48.72"),
    (29, 2, "surface-or-3D", "high", 1, False,
     "Figure 21 rho_rubber = 1100 kg/m3", "text", "", "", "3D surf, colorbar 48.75-49"),
    (30, 1, "heatmap-or-contour", "high", 1, False,
     "Figure 22 Figure in contour style", "text", "", "", "flat labelled contours 48.77-49.02"),
    (32, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 23. Illustration of a typical metal bat, cited Nguyen 2004", "text", "", "",
     "patent-style labelled line drawing with reference numerals"),
    (33, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 24. Illustration of useful conclusions drawn from foregoing models.", "text", "", "",
     "three shaded groups linked by arrows with a line-style legend"),
    (33, 2, "table-grid", "high", 1, True,
     "Table 3. The design parameters of the special aluminum bat.", "text", "", "",
     "ruled table, header plus 8 property rows"),
    (34, 1, "flowchart-or-schematic", "medium", 1, False,
     "Figure 25. Illustration of the special metal bat design.", "text", "", "",
     "mechanical cross-section with dimension callouts and A-A end view"),
    (34, 2, "table-grid", "high", 1, True,
     "Table 4. Contrast of wood and metal bats including Crisco-Greenwald Cage Study", "text", "", "",
     "ruled table, continues onto page 35"),
    (35, 1, "", "medium", 1, True, "", "none", "split-across-pages", "",
     "continuation of Table 4 from page 34"),
    (37, 1, "table-grid", "high", 1, True,
     "Table 5. A Comparison between Solid Wood Bat and Aluminum Bat (customized)", "text", "", "",
     "ruled 4-column table, values repeat Table 3, separately numbered"),
    (37, 2, "", "medium", 1, False, "", "none", "fragment-of-other", "",
     "upper panel of Figure 26, bat cross-section bitmap"),
    (37, 3, "composite-panel", "medium", 2, False,
     "Figure 26. Cross section of typical inner cavity style of aluminum bat and its estimated mass distribution function.",
     "text", "", "", "Figure 26 spans r2+r3: cross-section schematic above an m(z) line plot"),
    (38, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 27. Cross section of this special and simple case of aluminum bat", "text", "", "",
     "hatched cross-section with original/removed mass legend"),
    (40, 1, "flowchart-or-schematic", "high", 1, False,
     "Figure 28. The evolution of collision models", "text", "", "",
     "boxed schematic of collision models 1-4 with spring symbols"),
    (41, 1, "line", "high", 4, False,
     "Figure 29. Illustration of bending vibration of the bat in different modes or frequencies",
     "text", "", "", "four stacked mode-shape traces, same family so panel_count 4"),
    (42, 1, "line", "high", 1, False,
     "Figure 30. The distribution of vibration energy for an impact of a 90-mph ball on the standard wood bat",
     "text", "", "", "single piecewise line"),
    (42, 2, "line", "high", 1, False,
     "Figure 31. The plot of eeff for an impact of a 90-mph ball on the standard wood bat",
     "text", "", "", "single line, plateau then drop"),
    (50, 1, "line", "high", 1, False, "", "none", "", "",
     "semi-log plot, three curves e_ball 0.6/0.5/0.4, uncaptioned"),
    (51, 1, "other", "high", 1, False, "", "none", "",
     "MATLAB source-code listing in a ruled box (meshgrid, J1/J2, meshc)", "code appendix, not a chart"),
    (52, 1, "other", "high", 1, False, "", "none", "",
     "continuation of the MATLAB code listing from page 51", "code appendix, not a chart"),
]


def main() -> None:
    out = []
    for page, region, family, conf, panels, table, caption, src, excluded, other, note in ROWS:
        row = {
            "page": page, "region": region, "family": family, "confidence": conf,
            "panel_count": panels, "table": table, "caption_verbatim": caption,
            "caption_source": "text-layer" if src == "text" else (
                "typed-from-crop" if src == "typed" else "none"),
            "excluded": excluded or None, "other_note": other or None, "note": note,
        }
        out.append(row)
    path = P / "P-A-2010-6749-395f556a-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
