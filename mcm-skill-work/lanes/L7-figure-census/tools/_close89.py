"""Close paper 89 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-C-2015-39160-2b8963a3"

ROW = (
    "| 89 | P-C-2015-39160-2b8963a3 | mcm-9a | closed 2026-10-24 sha 6838ad178f9e6ea4 "
    "layout 793e082d3444b836 (figures=8 tables=0 excluded=0 unaccounted=0; 17 pages, 9 measured "
    "regions over 6 of them, and THE NINE RESOLVE INTO EIGHT EXHIBITS because p4 carries the "
    "identical box [33.8,264.1,296.3,502.6] twice, so Figure 1's raster is measured twice and the "
    "distinct-key count is eight; NO TABLE OF ANY KIND - 'Table' appears twelve times in the text "
    "layer and never with a number; NOT ONE CAPTION DESCRIBES ITS FIGURE - every caption is the "
    "bare label 'Figure N', two words, no title, no unit, no variable list, the emptiest caption set "
    "this lane has recorded, and Figures 2 and 3 print even that inside the raster so both are "
    "typed-from-crop; THE TEXT LAYER INTERLEAVES THE FIGURE'S OWN AXIS LABELS AND TICKS INTO THE "
    "PROSE on pp13-14, so the sentences naming Figures 6, 7 and 8 arrive spliced ('When HR is not "
    "able to work on at least 2/3 of Figure 7 the current vacant 160 positions, the number 150 140 "
    "Number of Vacancies of vacancies compounds/increases 130 120 every year') and the pointer "
    "quotes are kept exactly as printed; FIGURE 2 IS NEVER NAMED anywhere in the paper - its label "
    "survives only as pixels inside its own raster, so it carries count 0 with first_page null "
    "while the other seven are all cited; Figure 4 is described on p11 and prints on p12 and Figure "
    "8 is named on p13 and prints on p14, both positive lead_pages; families scatter 4, bar 1, line "
    "1, node-link-network 1, other 1; Figure 1 is the ICM supervision network as three stacked "
    "bands of nodes 0-17 with no key to which band is which relation, and its caption is the only "
    "one printed BELOW; Figure 2 is satisfaction against churn count with a fitted decay curve left "
    "completely unkeyed - no label, no legend, no equation; Figure 3 is a clean linear ridge of "
    "squares with no fitted line in a section whose claim is that the relation holds; Figure 4 is a "
    "greyscale two-slice pie with no percentages, folded into other with an other_note; Figure 5 "
    "puts three units on one 0-90 axis in two greys too close to tell apart over a full grid; "
    "Figures 6 and 7 use diamonds not lines, Figure 6's story is the flat part of a staircase at 37 "
    "with no ceiling marked and Figure 7's is a regime change at year 22 with no break marked, and "
    "Figure 7's y axis starts at 60; Figure 8 is a 100% stacked column of 30 years that draws no "
    "reference line at the 80% threshold every sentence citing it is about; Figure 6 sets all its "
    "text bold, axis titles included) |"
)

READ = (
    "| 89 | P-C-2015-39160-2b8963a3 | 17 | 9 | 8 | 0 | closed, `check.py` layout identical, "
    "unaccounted 0; 9 measured regions over 6 of 17 pages, but 8 exhibits because p4 measures the "
    "identical bbox twice and the distinct-key count merges it; no table of any kind; every caption "
    "is the bare label 'Figure N' with no title, no unit and no description, and Figures 2 and 3 "
    "print theirs inside the raster so both are typed-from-crop; the text layer splices each "
    "figure's axis labels and ticks into the prose on pp13-14, so those pointer quotes are kept as "
    "printed; Figure 2 is never named anywhere while the other seven are each cited at least once; "
    "families scatter 4, bar 1, line 1, node-link-network 1, other 1; Figure 5 puts three units on "
    "one axis in two indistinguishable greys, Figures 6 and 7 mark neither the 37 ceiling nor the "
    "year-22 break their prose turns on, and Figure 8 draws no line at the 80% it argues about |"
)

prefix = f"| 89 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 89 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
