"""Close paper 189 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2019-1902727-2e04a61b"

ROW = (
    "| 189 | P-A-2019-1902727-2e04a61b | mcm-9a | closed 2026-10-25 sha 2e04a61b "
    "layout de33570f7676b44b (figures=7 tables=7 excluded=1 unaccounted=0; 24 pages, 15 measured "
    "regions, fourteen exhibits resolving into seven figure rows and seven table rows; THE PAPER "
    "PRINTS NO TABLE 1 - p13 cites 'table 1' for the integral regression model that is equation "
    "(16), and the only unnumbered grid is the notation block on p5, captioned by its own section "
    "heading; THE LOGISTIC CONTRADICTS ITS OWN DATA - eq (4) returns 112.45 kg at age 1 against the "
    "text's 35 kg, no real (wm, r0) satisfies w(0)=10, w(1)=35, w(3)=14000, and the asymptote "
    "1.481e6 kg is 1481 tonnes; Figure 1 DOES draw eq (4), digitised to within 0.03 x 10^5 of the "
    "yearly samples joined by chords, so the plate is faithful and the prose is not, and the dragon "
    "clip art covers ages 2 to 9 where a reader would check; THE SAME FACTOR 1.115 RECURS THREE "
    "TIMES - eq (7)'s 4868598 against q0·wm^{3/4}/80^{3/4} = 4366737, and the sheep counts 296297 "
    "(p11) against 266609 (p13) with forage 533335 against 479896 kg/day; TABLE 3 DOES NOT MULTIPLY "
    "OUT - yield times area gives 338859/279768/279779 kg/day against the 479896 kg/day its own "
    "text requires, i.e. each printed area feeds 58 to 71 per cent of the flock, and the yields "
    "implied by dividing demand by area (4686/7352/3617 g/(m2 yr)) are 2.1, 3.3 and 1.6 times Table "
    "5's own 2200 g/(m2 yr) ceiling for tropical rain forest; TABLE 2 IS A COEFFICIENT LIST IN A "
    "MEASUREMENT LAYOUT - every body cell is a Legendre expansion, the header names meteorological "
    "elements where the cells are keyed by response coefficients aT/aR/aS, the caption calls them "
    "sensitivity coefficients where p11's hi(t) is a different quantity, and arid temperature is a "
    "bare hyphen so the arid region is fitted on two elements and the other two on three; FIGURE 5 "
    "KEYS COUNTRIES WHERE THE PAPER WORKS IN CLIMATES - Egypt/Australia/Iceland appear once in 24 "
    "pages, on p22, fifteen pages after the plate, and nothing maps them to Table 2's arid/temperate/"
    "arctic rows; its three panels run on three different scales (200 units, 6 and 1.8) with no "
    "ordinate unit, so equal-looking amplitudes are magnifications 100x apart; FIGURE 6 UNDER-DRAWS "
    "TABLE 3 BY 0.72/0.71/0.23 while preserving the ordering, and its fourth panel is a red box "
    "labelled '100 Standard Olympic Track Field' measuring about 1x1 km; FIGURE 7's caption promises "
    "a weight panel and an intake panel and both panels are titled 'Daily Intake(kcal)'; the two "
    "sensitivity grids print ten offsets +5 to -5 with no 0% row, no column is monotone in the "
    "offset, Table 6 gives +4% and -4% identical values at ages 2, 3 and 5, and Figure 7 prints only "
    "three of the ten offsets; the single refused region is the closing letter's addressee block, "
    "measured because the letter's header rules bracket it; families table-grid 7, line 4, "
    "flowchart-or-schematic 2, map-or-plan-view 1) |"
)

READ = (
    "| 189 | P-A-2019-1902727-2e04a61b | 24 | 15 | 7 | 7 | closed, `check.py` layout identical, "
    "unaccounted 0; 15 measured regions, 14 exhibits and 1 refusal - the closing letter's addressee "
    "block; no Table 1 is printed anywhere; eq (4) returns 112.45 kg at age 1 against the text's 35 "
    "kg and the three stated points admit no real solution, while Figure 1 draws eq (4) faithfully; "
    "the factor 1.115 recurs in eq (7)'s constant and in the two sheep counts 296297/266609; Table "
    "3's yield times area feeds only 58 to 71 per cent of the flock its own text requires, and its "
    "implied yields exceed Table 5's 2200 g/(m2 yr) ceiling; Table 2 is a Legendre coefficient list "
    "under a meteorological header with arid temperature left a bare hyphen; Figure 5 keys Egypt/"
    "Australia/Iceland against the paper's arid/temperate/arctic and puts its three panels on three "
    "different scales; Figure 6 draws 0.72/0.71/0.23 of Table 3's areas; both of Figure 7's panels "
    "are titled Daily Intake although the caption promises a weight panel |"
)

prefix = f"| 189 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 189 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
