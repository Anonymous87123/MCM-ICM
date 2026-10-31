"""Close paper 181 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-E-2019-1902054-4ff1f32f"

ROW = (
    "| 181 | P-E-2019-1902054-4ff1f32f | mcm-9a | closed 2026-10-24 sha 4ff1f32f "
    "layout b2e4320c8ac7cf52 (figures=10 tables=0 excluded=0 unaccounted=0; 17 pages, running header "
    "'Team 1902054', ten measured regions over nine of them and every one an exhibit, so ten figure rows "
    "with no tables and nothing refused; THE PAPER PRINTS NO TABLE AT ALL, so its three cases rest on "
    "prose coefficients and nothing in it is recomputable except the callouts; SIX OF THE TEN ROWS ARE "
    "NAMED BY NO SENTENCE (Figures 1, 2, 3, 6, 7, 10 - the two model plates, the satellite pair, the "
    "stacked column and the two case plates), Figure 6 is reached only by the deictic 'we can use the "
    "following graph', and Figure 10 only by its caption's tail; ONE CITATION NAMES THE WRONG FIGURE - "
    "p14 sends the reader to 'May(Figure 3)' while discussing the panda distribution map that is Figure "
    "9 on that page; THE TWO MODEL PLATES ARE ONE STATEMENT DRAWN TWICE ON TWO SCALES - Figure 1's "
    "ordinate runs -30 to 50 against Figure 2's -50 to 50, and the ecological term is written '+E(A)' in "
    "the first plate's callouts and '-V(A)' in the second's, so the pair cannot be laid over each other; "
    "SOFTWARE OUTPUT IS TYPESET AS A RESULT - Figure 5 prints three callout boxes reading (4284.776, 0), "
    "(5980.428, 1771.08) and (12399.999, 0), a numeric root search handed to the compositor to three "
    "decimals, while the prose rounds the first two to 4285 and 5980 and NEVER MENTIONS THE SECOND ZERO "
    "CROSSING at 12400, which is the upper bound of viable area; NO AXIS ANYWHERE CARRIES A UNIT - "
    "Figures 8 and 10 have no axis title, no unit, no legend and no annotation at all, Figure 4 prints "
    "'2091' and '4500' without the km2 its citing sentence supplies, and Figure 5's ordinate is bare; "
    "FIGURE 6 DOES NOT COMPOSE - its four-entry legend mixes a net change (green) with its own "
    "components (benefit, cost, ecological value), no bar carries a number, and read off the grid the "
    "After column's parts total about 2700 against a Net bar of about 2100 with Before about -600, and "
    "its in-art title sets the exponent as a caret ('6000 km^2'); Figure 7 is a smokestack photograph "
    "with no data, date, source or location, captioned 'Air pollution in Shanghui' (the city misspelt) "
    "and named by no sentence; Figure 9 is the paper's only map, two projected-metre heatmap panels "
    "headed 'Before Livestock' and 'After Livestock' over the SAME extent but with two duplicated "
    "unnamed 0-to-1 colour ramps, near-zero cells indistinguishable from the page, unlabelled point "
    "layers, no CRS, no scale bar and no north arrow, and the comparison it exists to make - fewer "
    "circles in the central corridor afterwards - is annotated nowhere; Figure 3's satellite pair "
    "carries no scale bar, north arrow, source line or common landmark; the one thing the paper gets "
    "exactly right is cross-plate agreement - Figure 4's callouts 2091 and 4500 match its citing "
    "sentence's 2091 km2 and 4500 km2, and Figure 5's first two boxes match the prose's 4285 and 5980; "
    "region order is reading order here, unlike the two preceding papers; families line 6, "
    "photo-or-raster-image 2, bar 1, map-or-plan-view 1) |"
)

READ = (
    "| 181 | P-E-2019-1902054-4ff1f32f | 17 | 10 | 10 | 0 | closed, `check.py` layout identical, "
    "unaccounted 0; ten measured regions over 9 of 17 pages, every one an exhibit, so 10 figure rows and "
    "no table anywhere in the paper; six rows named by no sentence (Figures 1, 2, 3, 6, 7, 10) and p14 "
    "cites 'May(Figure 3)' while reading Figure 9; Figures 1 and 2 are one statement on two ordinates "
    "(-30..50 against -50..50) with the ecological term relabelled +E(A) to -V(A); Figure 5 typesets "
    "solver coordinates (4284.776, 0) and (12399.999, 0) and the prose drops the second zero crossing; "
    "Figure 6 mixes a net with its components and does not compose; no axis in the paper carries a unit "
    "|"
)

prefix = f"| 181 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 181 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
