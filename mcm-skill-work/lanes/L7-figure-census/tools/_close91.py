"""Close paper 91 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2016-44398-137ab9e6"

ROW = (
    "| 91 | P-A-2016-44398-137ab9e6 | mcm-9a | closed 2026-10-24 sha 86107360a59ac02a "
    "layout 5859acfaec6d323c (figures=36 tables=12 excluded=16 unaccounted=0; 51 pages, 64 measured "
    "regions over 27 of them, resolving into THIRTY-SIX FIGURE ROWS, TWELVE TABLES AND SIXTEEN "
    "EXCLUSIONS; SIX PRINTED TABLES ARE DECLARED GAPS WITH NO MEASURED REGION AT ALL - Tables 2 and 3 "
    "on p14, Tables 4 and 5 on p23, Table 6 on p29, Table 16 on p44 - and pp14 and p23 carry no region "
    "whatsoever although the region pass reports 32 vector paths on each, so the paper prints eighteen "
    "tables and twelve are boxed; the sixteen exclusions are nine keys and colour bars boxed as their "
    "own regions (Figures 6, 10, 12's legends; Figures 7, 11, 13, 24's colour bars), four lettering "
    "strips of Figures 3 and 4 ('Layers of thermal insulation materials', 'Inside the tub', 'Outside "
    "the tub', 'ft ft2'), display inequality (45) on p34 and a body-text block on p49 as "
    "not-an-exhibit, and a duplicate slice of p49's banner; SEVEN EXHIBITS ARE MULTI-PANEL AND "
    "SIXTEEN OF THE THIRTY-SIX ROWS ARE THEIR PANELS - Figure 7 two fields on p17 sharing one "
    "unlabelled bar, Figure 11 five snapshots at 1/2/10/20/30 s split across pp24-25, Figure 13 two "
    "at 3/15 s, Figure 24 the four entrance arrangements in a 2x2 block - and not one of the sixteen "
    "panels prints an axis, a graduation or a value; CITATION IS THE THINNEST IN THE LANE: eleven "
    "figure rows and eleven of the twelve counted tables are named by no sentence at all, the standard "
    "introduction being a bare 'as follows' printed immediately before the caption, and of the "
    "twenty-five figure rows that do carry a pointer most are one of three fixed phrases ('the above "
    "figure', 'the following figure', 'the above picture'); ONE POINTER PRINTS THE WRONG NUMBER - p16 "
    "says 'The curve of residual is shown in Fig.5' for the figure its own caption numbers Fig.6, so "
    "Figure 6 has no correct pointer anywhere in fifty-one pages - and p45's introduction to Table 18 "
    "is truncated mid-clause ('From point of'), leaving that table named only by its caption; THE TEXT "
    "LAYER CANNOT RENDER THE SUBSCRIPTS, so seven figure captions arrive as glyph runs ('The change of "
    "q \\uf046 and 2 T over volume') and those seven are typed-from-crop while the other twenty-nine "
    "are text-layer; two caption defects named in the note - Table 15's caption omits the parameter it "
    "varies (it reads only 'The variation of parameters', h3 surviving only as a column head, so "
    "Tables 14 and 15 are indistinguishable from their captions) and Figure 21 keeps a space after the "
    "period ('Fig. 21') where every other label closes it up, while Table 7 drops the space ('Table7'); "
    "Figure 6 is a Fluent residual plot with NEITHER AXIS TITLED, its key box drawn INSIDE the plot at "
    "the upper right, no tolerance line anywhere, and at the 379 iterations where the prose declares "
    "the problem 'nearly convergent' five of its six residuals are still between 1e-03 and 1e-04; "
    "Figure 9 draws three trends on two bare-arrow axes with symbol ticks only and prints no numbers "
    "at all; Figures 15 to 22 are eight dual-ordinate plots pairing variables of different units on "
    "left and right scales with keys inside, Figure 20 the clearest abuse (one 'proportional' series "
    "dead flat at the top of its axis, the other moving across a window of 0.00035 kg/s), and Figures "
    "21 and 22 print 'The change of h3/(W/(m2K))' over ticks reading 50 to 70, the label and its "
    "numbers disagreeing about whether the abscissa is a percentage; Figure 17 labels its right "
    "ordinate 'the change of T2 /mi', a wreck of the degree sign, over five unordered tub shapes; "
    "Figure 5 is a Gambit screenshot whose grid aliases at print size; Figures 1, 2, 3, 4, 8, 18 and 23 "
    "are structural drawings carrying no data, and the modelling flow chart on p8 is the only exhibit "
    "in the paper that carries none of any kind; families line 12, heatmap-or-contour 13, "
    "flowchart-or-schematic 7, other 3, photo-or-raster-image 1, table-grid 12) |"
)

READ = (
    "| 91 | P-A-2016-44398-137ab9e6 | 51 | 64 | 36 | 12 | closed, `check.py` layout identical, "
    "unaccounted 0; 64 measured regions over 27 of 51 pages resolving into 36 figure rows, 12 tables "
    "and 16 exclusions, with six printed tables (2, 3, 4, 5, 6, 16) declared gaps that have no "
    "measured region even though pp14 and p23 report 32 paths each; the 16 exclusions are seven keys "
    "and colour bars boxed separately, four lettering strips of Figures 3 and 4, inequality (45), a "
    "p49 body-text block and a duplicate banner slice; seven multi-panel exhibits (Figures 7, 11, 13, "
    "24) supply 16 of the 36 rows and none of those panels prints an axis or a value; eleven figure "
    "rows and eleven tables are named by no sentence, and p16's residual pointer prints 'Fig.5' for "
    "the figure captioned Fig.6; seven captions mangled by subscript extraction were typed from "
    "crops; Figures 15-22 are eight dual-ordinate plots with unrelated left/right scales and Figures "
    "21-22 label a percentage abscissa with the swept coefficient's unit |"
)

prefix = f"| 91 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 91 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
