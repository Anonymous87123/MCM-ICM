"""Close paper 94 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2016-48649-e4d30266"

ROW = (
    "| 94 | P-A-2016-48649-e4d30266 | mcm-9a | closed 2026-10-24 sha cca74e2b8513c35d "
    "layout 8b1cf3af756f145e (figures=28 tables=6 excluded=1 unaccounted=0; 44 pages, 35 measured "
    "regions over 25 of them, resolving into TWENTY-EIGHT FIGURE ROWS, SIX TABLE ROWS AND ONE "
    "EXCLUSION; the paper prints ELEVEN numbered tables and only SIX were boxed - Tables 1 and 2 "
    "(pp6-7), Table 5 (p26), Table 6 (p28) and Table 8 (p29) print caption, header and data under no "
    "measured region because their grids are open rule sets that close no rectangle, so five tables "
    "are declared gaps; every exhibit is labelled 'Graph N:', a form the numbering vocabulary does "
    "not name, so all 28 figure rows carry numbering 'none' and keep the printed number separately, "
    "while the six tables print 'Table N:'; the eight ANSYS exhibits (Graphs 1 and 3 to 11) are one "
    "visual idiom - grey solids and colour fields on a dark navy ground with no axes anywhere - and "
    "ONLY GRAPH 5 PRINTS A SCALE BAR (0.000 to 0.070 m), the two colour-bar pairs reading 3.13e+02 to "
    "3.18e+02 and 3.12e+02 to 3.18e+02 WITH NO UNIT ON ANY OF THE FOUR; Graphs 2 and 8 are model "
    "trees, Graphs 12 to 16 and 17 to 26 are sixteen MATLAB curves of which not one prints a data "
    "value on a mark and Graphs 23 to 26 repeat the same five-curve repeat-plot so closely that "
    "Graph 23's five lines sit inside a 2 pt band, and Graph 27 is the paper's only raster, a rendered "
    "bubble-layer slab; citation is uneven - Graphs 2, 16, 17, 18, 19, 20, 21 and 22 are named by no "
    "sentence (all of them the section-6.1 sweeps, where the pointer degenerates into 'the "
    "corresponding graph'), Tables 10 and 11 are introduced two and three pages before they print by "
    "one sentence on p30, and Graphs 3 and 4 run the other way (named on p15, printed on p16); the one "
    "exclusion is p24's display equation 1/sqrt(sum((t_i - t_mean)^2)/n), boxed because its fraction "
    "bar and radical counted as drawn paths; FOUR ARITHMETIC AND UNIT DEFECTS PRINT - Table 4's row "
    "mixes 'Temp(k)', 'Temp(K)' and 'Temp(ºC)' while its 40.4178 could not be the conversion of any "
    "Kelvin value beside it, Table 10 reports the same run as Table 9 with a different heat flux "
    "(1.5652 W against 1.4406 W) on identical volume temperatures, Table 7 prints the CI comfortable "
    "degree as 10.0621 where p27 derives 10.6021, and Table 11 repeats Table 10's 298 K row exactly "
    "and leaves a stray 'Table' word under its grid; the prose carries the same carelessness - Graph "
    "13's in-plot title misspells 'Water-Buthtub' over a correct caption, Graph 24's caption says "
    "'volume area', and Graph 26's pointer reads 'the material of the bathtub have larger effect on "
    "the total heat loss than the surface or the material of the bathtub', carried over from the "
    "material section; families line 16, surface-or-3D 5, heatmap-or-contour 4, "
    "flowchart-or-schematic 2, photo-or-raster-image 1, table-grid 6) |"
)

READ = (
    "| 94 | P-A-2016-48649-e4d30266 | 44 | 35 | 28 | 6 | closed, `check.py` layout identical, "
    "unaccounted 0; 35 measured regions over 25 of 44 pages resolving into 28 figure rows, 6 tables "
    "and 1 exclusion, with five of the paper's eleven printed tables (Tables 1, 2, 5, 6, 8) declared "
    "gaps because their open rule sets close no rectangle; every exhibit is a 'Graph N:' outside the "
    "numbering vocabulary, so the figure rows record numbering 'none'; only Graph 5 carries a scale "
    "bar and none of the four colour bars is unit-labelled; eight graphs (2, 16 to 22) are named by no "
    "sentence; Table 4 mixes 'Temp(k)', 'Temp(K)' and 'Temp(ºC)' and prints a Celsius value no Kelvin "
    "cell converts to, Table 10 contradicts Table 9 on one shared run's heat flux, and Table 7 drops a "
    "digit from 10.6021 to 10.0621 |"
)

prefix = f"| 94 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 94 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
