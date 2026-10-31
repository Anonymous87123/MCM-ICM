"""One-off: assemble paper 10 coder rows into the merged payload file.

Paper 10 is table-dominant: six printed tables among thirteen measured regions, and only
three exhibits. Figure 2's flow chart has its labels rasterised as tiny per-word images,
so four small regions sit inside it and are excluded as parts of the chart. Figures 1 and
3 are Excel-style charts with a data grid attached under the axis; they are still one
exhibit each, not a table.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

CAP_F1 = ("Figure1 Abundance of floating plastics in the North Pacific Ocean during"
          " 1975-2001")
CAP_F2 = "Figure2 simulation of the pollution abatement process"
CAP_F3 = "Figure3 Risk degrees of different types of plastic"

ROWS = [
    (3, 1, "line", "high", 1, False, CAP_F1, "", "",
     "four diamond markers joined by a curve, y Abundance (pieces/km2), category x axis with an attached value grid under the plot"),
    (4, 1, "", "high", 1, True,
     "Table 1 Variables and definitions", "", "",
     "printed table laid out two-up: Variable / definition twice, split by a vertical rule"),
    (5, 1, "flowchart-or-schematic", "high", 1, False, CAP_F2, "", "",
     "five sharp rectangles, four rounded steps, about ten single-headed arrows and two feedback arrows; labels are rasterised word images"),
    (5, 2, "", "high", 1, False, "", "in-body-diagram", "",
     "rasterised label word inside the Figure 2 flow chart"),
    (5, 3, "", "high", 1, False, "", "in-body-diagram", "",
     "rasterised label word inside the Figure 2 flow chart"),
    (5, 4, "", "high", 1, False, "", "in-body-diagram", "",
     "rasterised label word inside the Figure 2 flow chart"),
    (5, 5, "", "high", 1, False, "", "in-body-diagram", "",
     "rasterised label word inside the Figure 2 flow chart"),
    (6, 1, "", "high", 1, True,
     "Table2 Abundance of plastic pieces and tar found in the North Pacific gyre", "",
     "", "printed table: Mesh-size(mm) / Total-abundance, six size bins plus a Total row"),
    (6, 2, "", "high", 1, True,
     "Table3 Effect measurement decision matrix", "", "",
     "printed table: Alternative 1-6 columns, rows factor A Total_abundance and factor B Mesh-size(mm)"),
    (8, 1, "", "high", 1, True,
     "Table4 Abundance by type and size of plastic pieces and tar in the North Pacific gyre",
     "", "",
     "printed table with a diagonal corner cell, six material columns, rows Alternative 3 to Alternative 6"),
    (8, 2, "", "high", 1, True,
     "Table5 Regulation data of table 4", "", "",
     "printed table, same structure as Table 4 with regulated decimal values"),
    (8, 3, "bar", "high", 1, False, CAP_F3, "", "",
     "six 3D-perspective columns, y Risk degree 0 to 0.7, category labels in a grid under the axis"),
    (10, 1, "", "high", 1, True,
     "Table 6 The specific solutions to the three standards", "", "",
     "printed table with a diagonal corner cell, columns for HRP, MRP and LRP policy, four solution rows"),
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
    path = P / "P-C-2010-6947-c5305f34-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
