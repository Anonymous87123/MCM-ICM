"""One-off: assemble paper 9 coder rows into the merged payload file.

Paper 9 is table-heavy: five of eleven measured regions are printed tables, three of them
on page 13. Page 16 prints Tables 5 and 6, but only Table 5's header and body rows were
measured, so the record carries one table there and the README carries the gap.

Page 14 is five scatter sub-plots of the same family with a shared caption, so it stays
`scatter` with panel_count 5 rather than becoming composite-panel.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

CAP_F1 = ("Figure 1: Simulation results for the centrographic model with the Hillside"
          " Strangler data set [4].")
CAP_F2 = ("Figure 2: Attack sites, jeopardy surface, and homes of David Berkowitz, the"
          " \"Son of Sam,\" using the Berkowitz data set [24].")
CAP_F3 = ("Figure 3: Attack sites, jeopardy surface, and home of Angelo Buono [7], one"
          " half of the \"Hillside Strangler\" duo.")
CAP_F4 = ("Figure 4: Prediction results with the RSC model for the 7th Berkowitz kill"
          " using the first six kills from the Berkowitz data [24].")
CAP_F5 = ("Figure 5: Simulation results for the centrographic model with the DC Sniper"
          " data [2].")
CAP_F6 = ("Figure 6: Prediction results with the RSC model for the last DC Sniper kill"
          " using the previous kills from the DC Sniper data [2].")

ROWS = [
    (12, 1, "", "high", 1, True,
     "Table 1: Example data set: Berkowitz murders [36, 3]", "", "",
     "printed table: Kill# / Longitude / Latitude / RelativeDay / Victim(s) / Address, eight kills"),
    (13, 1, "", "high", 1, True,
     "Table 2: Distance between center of predicted area and actual location of"
     " subsequent kill, measured with Manhattan metric. Hillside data set [19].", "", "",
     "printed table: Kill# / Distance from center of predicted area (km), five rows"),
    (13, 2, "", "high", 1, True,
     "Table 3: Linear regression data for the centrographic model, x-direction"
     " (longitudinal). Hillside data set [19].", "", "",
     "printed table: Kill# / a-hat_x / R2 / p, five rows"),
    (13, 3, "", "high", 1, True,
     "Table 4: Linear regression data for the centrographic model, y-direction"
     " (latitudinal). Hillside data set [19].", "", "",
     "printed table: Victim# / a-hat_y / R2 / p, five rows"),
    (14, 1, "scatter", "high", 5, False, CAP_F1, "", "",
     "five unframed scatter sub-plots in a 2+2+1 grid, shared Longitude/Latitude axes, blue squares plus one red diamond each"),
    (15, 1, "heatmap-or-contour", "medium", 1, False, CAP_F2, "", "",
     "blocky blue pixel raster with red patches, colour-classed overlay, attack-site and home markers, no basemap"),
    (16, 1, "", "high", 1, True,
     "Table 5: Performance of RSC model on data for David Berkowitz [24]", "", "",
     "measured fragment is Table 5: Home / Hunting Area / Hit Score % / Search Area, rows Bronx and Yonkers; Table 6 on the same page has no measured region"),
    (17, 1, "heatmap-or-contour", "medium", 1, False, CAP_F3, "", "",
     "tall portrait panel, blocky raster with a broad red vertical band, body-dump and home markers, no basemap"),
    (17, 2, "heatmap-or-contour", "medium", 1, False, CAP_F4, "", "",
     "colour-classed regions with curved boundaries (red, green, purple, grey) plus nested contour rings; not rectangular quadrants"),
    (18, 1, "scatter", "high", 1, False, CAP_F5, "", "",
     "single unframed scatter, Longitude/Latitude, eight dark dots, one black dot and one red diamond"),
    (18, 2, "heatmap-or-contour", "medium", 1, False, CAP_F6, "", "",
     "colour-classed green/red/purple regions, nested rectangular contour rings, final-shooting marker"),
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
    path = P / "P-B-2010-8479-b934962b-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
