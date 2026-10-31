"""One-off: assemble paper 2 coder rows into the merged payload file."""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

# page, region, family, confidence, panels, is_table, caption, caption_source, note
ROWS = [
    (6, 1, "other", "high", 1, False, "Figure 1 the pivot point[1]", "typed",
     "hand-drawn ink illustration of a batter with swing arcs and a red pivot-point circle; no axes or diagram boxes"),
    (7, 1, "flowchart-or-schematic", "high", 2, False, "Figure 2", "typed",
     "two-panel free-body diagram of the bat: force F, moment M, distances d and c, CM and P points"),
    (8, 1, "flowchart-or-schematic", "high", 2, False, "Figure 3 speed before and after collision", "typed",
     "two-panel free-body diagram, bat and ball before and after collision with v1, w1, v2, w2"),
    (10, 1, "flowchart-or-schematic", "high", 1, False, "Figure 4 simplified model of a bat", "typed",
     "dimension-line schematic with Lcm, L1, L2, d, c, b"),
    (12, 1, "line", "high", 1, False, "Figure 5", "text",
     "single axes, three smooth curves vs b/cm with legend comfort index, velocity index, objective function"),
    (14, 1, "line", "high", 1, False, "Figure 6", "text",
     "one axes, about seven marker series (data3-data9 plus lambda 0.1/0.2) vs b/cm"),
    (15, 1, "line", "high", 1, False, "Figure 7", "text",
     "single monotone rising curve b/cm vs lambda"),
    (16, 1, "line", "high", 1, False, "Figure 8", "text",
     "single near-linear curve b/cm vs change rate of mass"),
    (16, 2, "line", "high", 1, False, "Figure 9", "text",
     "single straight increasing line, v2 vs change rate of mass, full axes box"),
    (17, 1, "line", "high", 1, False, "Figure 10", "text",
     "three paraboliform curves in one axes, legends -10% / 0 / +10% swing speed"),
    (18, 1, "photo-or-raster-image", "high", 1, False, "Figure 11", "text",
     "wide shallow continuous-tone photograph of a sawn-open Louisville Slugger bat on grass, no axes; the Assumption text below is the next section heading"),
    (19, 1, "flowchart-or-schematic", "high", 1, False, "Figure 12 simplified model of a corked bat", "text",
     "stepped-cylinder line drawing with L_cm, L1, L2, d, c, b, radii r and R, CM dot, dashed cork cavity"),
    (22, 1, "line", "high", 1, False, "Figure 13", "text",
     "framed chart not a table: single descending curve b/cm vs length of rubber; the Table 9 caption above and Table 10 row clipped at the top belong to other exhibits"),
    (23, 1, "line", "high", 1, False, "Figure 14", "text",
     "single descending curve v2 vs length of rubber, full axes box"),
    (24, 1, "line", "high", 1, False, "Figure 15", "text",
     "single curve with a shallow dip near x=15 then slight rise"),
    (25, 1, "line", "high", 1, False, "Figure 16 location of Sweet Zone vs. length of rubber", "text",
     "two nearly flat slightly descending curves, upper and lower Sweet Zone limits"),
    (26, 1, "flowchart-or-schematic", "high", 1, False, "Figure 17 simplified model for an aluminum bat", "text",
     "dimensioned line drawing with L_cm, L1, L2, r, R, t, d, c, b; raster-embedded schematic"),
    (28, 1, "line", "high", 1, False, "Figure 18", "text",
     "three index curves with legend and two peak arrows; census fragment flag is a false positive, axes complete"),
    (29, 1, "line", "high", 1, False, "Figure 19 property of wooden bat", "text",
     "inverted-U objective function vs b/cm with horizontal cutoff near 0.84 and crossing arrows at 46.09 and 53.87"),
    (30, 1, "line", "high", 1, False, "Figure 20 property of aluminum bat", "text",
     "same objective-function shape as Figure 19, cutoff near 0.84, crossings at 43.95 and 52.77"),
    (31, 1, "line", "high", 1, False, "Figure 21", "text",
     "single straight descending sensitivity line v2 vs change rate of t"),
]

# Booktabs tables found by rule change 6. A table with its own caption above it is
# counted; one without is the tail of a table whose caption is on the other page.
TABLES = [
    (11, 1, "Table 1", "ruled table: header row b/cm 68.2-b over row e, 6 columns"),
    (12, 2, "Table 2", "header row b(cm) E_batter E_ball v2(cm/s) f; 5 data rows continue on p13"),
    (13, 2, "Table 3", "header Value of objective / Comfort index / Exit velocity / formula / Sweet point"),
    (16, 3, "Table 4", "header row Change of the mass of a bat(in ratio); 3 data rows continue on p17"),
    (18, 1, "Table 5", "swing speed change vs exit speed, 3 rows"),
    (21, 1, "Table 6", "Length of cork 0-20 vs mass of bat"),
    (21, 2, "Table 7", "Length of cork 0-20 vs length from center of mass to the pivot"),
    (21, 3, "Table 8", "Length of cork 0-20 vs moment of inertia J"),
    (22, 1, "Table 9", "Length of cork 0-20 vs swing speed"),
    (22, 2, "Table 10", "Length of cork 0-20 vs b; row v2 continues on p23"),
    (23, 3, "Table 12", "Length of cork 0-20 vs the most comfortable hitting point; last row on p24"),
    (25, 2, "Table 13", "X 0-20 vs lower limit, upper limit, span of the sweet zone"),
    (28, 2, "Table 14", "b(cm) E_batter E_ball v2(cm/s) f, 3 data rows"),
    (30, 2, "Table 15", "change of t vs location of sweet spot, exit velocity, change of exit velocity, 3 rows"),
]

CONTINUATIONS = [
    (13, 1, "5 rows of Table 2, header on p12"),
    (17, 1, "3 body rows of Table 4, header on p16"),
    (23, 1, "header repeated and row v2 of Table 10, caption on p22"),
    (24, 1, "row 'hitting point' of Table 12, caption on p23"),
    (31, 1, "2 tail rows and the closing rule of Table 15, header on p30"),
]


# figure rows were coded against the pre-rule-6 layout; these are their new indices
REMAP_OLD = {(17, 1): 2, (18, 1): 2, (22, 1): 3, (23, 1): 2, (24, 1): 2, (31, 1): 2}


def main() -> None:
    out = [
        {
            "page": page, "region": REMAP_OLD.get((page, region), region),
            "family": family, "confidence": conf,
            "panel_count": panels, "table": table, "caption_verbatim": cap,
            "caption_source": "text-layer" if src == "text" else "typed-from-crop",
            "excluded": None,
            "other_note": note if family == "other" else None, "note": note,
        }
        for page, region, family, conf, panels, table, cap, src, note in ROWS
    ]
    for page, region, cap, note in TABLES:
        out.append({
            "page": page, "region": region, "family": "table-grid", "confidence": "high",
            "panel_count": 1, "table": True, "caption_verbatim": cap,
            "caption_source": "text-layer", "excluded": None, "other_note": None,
            "note": note,
        })
    for page, region, note in CONTINUATIONS:
        out.append({
            "page": page, "region": region, "family": "", "confidence": "high",
            "panel_count": 1, "table": True, "caption_verbatim": "",
            "caption_source": "none", "excluded": "split-across-pages",
            "other_note": None, "note": note,
        })
    path = P / "P-A-2010-7571-1ac2a627-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
