# C-lane distill — progress ledger

Goal: 63 packages (queue positions 6-68) on top of the 5 papers already read in the skill
reference, to reach the 68-paper gate. One package per paper, five fields each, numbers
recounted from page images, not copied from the record. Writes: this directory only
(`PROGRESS.md` plus `P-C-*.md`). Renders go to `tmp/c-distill/<paper>/` and are not
deliverables.

Record path for every row: `lanes/L3-c-ledger/records/<paper>.json`, chapter
`model-establishment` unless noted. "Disagreement" is one line per page-versus-record conflict;
"—" means the page matched the record.

| queue | paper | printed pp (PDF) | groups / blocks | status | disagreement with the record |
|---|---|---|---|---|---|
| 6 | P-C-2011-11325-4609137d | 8-11 (2-5) | 19 / 28 | done | **rebuilt against the record's re-coded 19-group version** (the 13-group pack covered 76-102 only and had filed 2.1.2 under `strengths-limitations`; the new record keeps the calibration paragraph as unit 8 with job `limit`); chapter is printed 2 to 3.1 at folio −6 ("Page 2 of 20" on PDF 8, M = 20), 1,129 layout words over 19 units (59.4 each, 40.3 per block, median 51), no watermark and no QR tile on any of the four pages; **this chapter's own titles live in another chapter's block** - 74 (`introduction`) ends "…comparing the Nissa 2 Methodology 2.1 Mathematical Model" and 102 (`model-establishment`) ends "…levels from cars. 3 Results"; **only one `heading` block exists in the whole file** (104, "3.1 Economics of current BEVs vs. ICEs") while the twelve levels printing on pp. 8-11 are all tails, three of them split into a bare numeral ending one block and a five-word title block after it ("2.2.1" in 90 / 91, "2.2.3" in 96 / 97, "2.2.6" in 100 / 101); the record's heading string names three of those twelve; **(1)-(3) share one block with their subscripts flattened** ("dG 1 −G + αEE + αHH dt =rGG (1) KG") and (4) sits in 96 with its sum collapsed ("+ (4) (1 + i)t t=1"), while the unnumbered effective-rate display after (4) prints a capital `I` where (4) uses lower-case `i` [R]; **Table 2.1 is de-interleaved one cell out of phase** ("source G(0) = 246 × 106 number of ICE vehicles G(t) E(0) = .01 × 106 number of BEVs E(t)") and its `source` column prints a header with no entry for any row although block 75 cites the North American Transportation Statistics Database [R]; Table 2.2 costs seven blocks (caption, header and six rows in 80, one block per row after) for twelve rows and neither table keeps a column separator; "Honda Civic SI" (p8) against "Honda Civic Si" (p10); `L` and `SPPW` in (4) undefined; 440 GW ÷ 236 MW = 1,864.4 against the printed "1,865 generators" [R] closes; typos "dependant" (prose and Table 2.1 caption), "for an eight year life cycle", error orders set as leading superscripts "⁴y_{i+1} and ⁵y_{i+1}" |
| 7 | P-C-2011-11422-caf513f2 | 4-18 (4-18) | 35 / 55 | done | **rebuilt against the record's re-coded 35-group version** (the 30-group pack covered printed 4-14 and stopped before the cellular automaton, the macro model and the optimiser); folio 0 ("Page n of 20", M = 20), 3,315 layout words over 35 units (94.7 each, 60.3 per block, median 86), span `[4,18]` now right; the chapter owns **no `heading` and no `display` block**, while the six heading blocks printing inside its pages (53, 88, 90, 108, 115, 125 = sections 5, 7, 7.1, 7.6, 7.7, 8) belong to **no chapter at all**, and the other fifteen headings weld onto tails, five of them onto other chapters' blocks - including "4 On Types of Cars" at the end of `problem-analysis` block 49; pp. 9 and 16 carry no chapter words; the strings "Table" and "Figure" never occur on pp. 4-18, so eight table grids and nine figure panels are all uncaptioned and unnumbered; the p11 grid's cells rotate one place against their row labels (the carbon-monoxide Difference lands on the carbon-dioxide line, "Mercury" trails its own numbers) and the p13 quadrature is torn between a sentence's tail (`as: + 12i · L2`) and its display, losing the operator between fractions; p18's alpha = 200,000 Total Cost prints 1.28032 · 10¹¹ over components summing to 1.28033 · 10¹²; the p13 Current Production column sums to 38.300 QBTU against the 38.075 printed on p10, the seeding column is computed at t = 60 while the prose seeds in 2011 (t = 61), and F(t) = 12,200/(31 · 20) leaves the 20 underived where the chapter's own 2.49 ratio implies 77 mpg; eighteen set-off equations, none numbered (the record note says nineteen, counting a sentence as a line); the record's "five runs … 89 to 116" hides three orphan heading blocks, so the chapter is nine runs |
| 8 | P-C-2011-11893-6a9ea7d9 | 2-13, 15, 17 | 21 / 117 | done | notation and constraint tables torn row by row; unresolved LaTeX "figure*"; pp. 15 and 17 results-only |
| 9 | P-C-2011-8882-54492a1f | 3-23 (4-24) | 50 / 133 | done | span `[4,23]` misses p. 24 where groups 48-50 and Fig. 21 sit; Tables 2 and 11 absent from layout; block 104 routing text coded under results |
| 10 | P-C-2011-9089-838e50df | 1-15 (2-16) | 56 / 99 | done | group 56 sentence ends "in the next", completion in `results` block 132; two Figure.11; Table.5 reuses Table.4's title; pointers to nonexistent Figure.12 |
| 11 | P-C-2012-12218-14ded715 | 3-14 (4-15) | 30 / 61 | done | headings 2.2 and 2.3 glued to `assumptions` and `problem-analysis` blocks; groups 5, 22, 25, 29 second page carries only a header; Table 7 interrupts a sentence |
| 12 | P-C-2012-13215-607f0f06 | 2-12 (3-14) | 31 / 107 | done | span `[3,14]` one page too long; p. 4 holds no chapter block; folio systematically PDF−1 |
| 13 | P-C-2012-13855-8ff9127d | 4-9 | 27 / 71 | done | span overruns into Section 5 (blocks 103-107); Table 1 misprints cDRR as cDRS; block 107 welds a footnote to the Table 2 grid |
| 14 | P-C-2012-14531-6018365f | 4-13 (5-14) | 27 / 96 | done | all 16 displays typed `body`; pointers "Table 2.1"/"table 2.4" name printed Table 1/Table 3; headings 131 and 137 owned by no chapter |
| 15 | P-C-2012-15356-6b8f0a28 | 6-12, 15-17 | 36 / 63 | done | span `[6,17]` but the chapter is discontinuous: pp. 13-14 carry the `strengths-limitations` chapter (Fig. 6, "Evaluation and Discussion", Strength/Weakness bullets), so nothing of this chapter sits or was dropped there; groups 8, 11, 20 second page is a label or heading; "Task 1" title coded `assumptions`, "Task2" coded `results`, three headings owned by no chapter |
| 16 | P-C-2012-16075-4bbf9219 | 2-9 (4-11) | 39 / 106 | done | six-block hole at 62-67 (Figure 1) belongs to `problem-analysis`; folio offset of 2 (PDF 10 = "Page 8 of 20"); Table 1 captioned but never cited; display (4-7) IS numbered on the page - the defect is the dropped inline math, which truncates the citing sentence into blocks 135 and 136 ("According to the matrix (4-7) and equation Aw w" / ", we can figure out that the w = weight vector") |
| 17 | P-C-2012-17160-8b6c54d2 | 6-11 (5-12) | 30 / 53 | done | span `[5,12]` over-stated at both ends; chapter's own lead paragraph is unassigned block 26; heading 5.3 is unassigned block 74 |
| 18 | P-C-2013-18492-ab739371 | 3-14 (4-15) | 87 / 136 | done | layout run 58-193 holds 136 paragraphs, not 127: nine heading blocks (87, 113, 128, 135, 142, 145, 148, 165, 179) belong to no group; four ranges over-claimed by one page (58, 116, 154, 173); Figure 3.3.5-1 has no block and no group, only a caption welded to block 180; 21 blocks carry "数学中国"/"www.madio.net" watermark text mid-sentence |
| 19 | P-C-2013-21165-17e64d15 | 4-8 (5-9) | 26 / 57 | done | §1.5 Notations table (Table 2) coded into this chapter; blocks 48 and 89 owned by no group, so 57 is arithmetic over a 59-slot run; Table 3 never cited; body promises "seven concepts" and delivers five |
| 20 | P-C-2014-25318-eac62e81 | 3-9 (4-10) | 30 / 52 | done | five blocks (44, 70, 81, 85, 92) absorb the next page's running header, inflating four groups to two pages; Figure 3 and equation P(K>k)~k^-1.6 sit inside the span but belong to 4.4 `results`; one `read-figure` group (18) reads nothing, it is a forward pointer |
| 21 | P-C-2014-27688-856eb1b7 | 7-11 (8-12) | 31 / 41 | done | page 12 shared with 4.3.2 `results` (blocks 125-128 incl. Table 4), so span `[8,12]` covers only its first half; block 124's tail carries the 4.3.2 heading; group 17 recorded pp. 10-11 but closes on p. 10 |
| 22 | P-C-2014-28199-d39873d7 | 4-16 (4-16) | 41 / 58 | done | the chapter loses its own middle: blocks 60-88 (about 3.2 pages - Edros application, Table 3, movie-star application, Fig. 4, Table 4, Strengths/Weaknesses/Utility) belong to no chapter, hidden because blocks 59 and 116 swallow the next heading; chapter heading "Properties of Network" welded to unowned block 29; block 111 typed `heading` though it is the matrix, so a `read-figure` job reads a display; p. 16 uncovered; Fig. 4 and Table 4 never cited |
| 23 | P-C-2014-28747-f6ef544f | 3-11, 13-14 (5-16) | 84 / 99 | done | the 128-153 gap is this chapter's own §4.3 (`results` record claims it, ranges overlap), so the chapter is discontinuous and pp. 12 and 16 carry no group; "3 Symbol Description" welded to block 57 under `assumptions`; ten running heads absorbed into prose, block 125 separating a lead-in from eq (12); "4.1.1"/"4.1.2"/"4.1.3"/"4.2.2" numbers stranded at block tails; Fig. 1/Fig. 3 caption tails spliced into Fig. 2/Fig. 4; Table 5 never cited |

| 24 | P-C-2014-30221-7af27341 | 3-12 (3-12) | 69 / 80 | done | five ranges one page too long, each adding only the next page's running header; only block 19 is a clean heading, every other section title is welded to a prose tail; blocks 56-59, 67-68 and 105 are this chapter's own prose under `assumptions`/`results`/`future-improvements`; 8 of 11 `read-figure` jobs read tables, one reads no object; "5 Task 3" heading welded into a `results` block |
| 25 | P-C-2014-31262-1f9007fa | 3-10 (3-10) | 72 / 76 | done | blocks 15-19 are front matter inside the span and consume both the "2. BACKGROUND" and "3. METHODOLOGY" headings; block 14 (a page-2 contents line) owns the chapter's §1 opening; blocks 56 and 94 assigned to no group, so the sequence jumps 35→36 and 69→70; group 32 is a prose-less mid-heading fragment still given `interpret`; block 97 swallows "4. RESULT AND ANALYSIS" and "4.1 Task1"; no `read-figure` job anywhere, the whole argument is 29 displays |
| 26 | P-C-2015-33572-b32fb4b1 | 2-12 (3-13) | 100 / 136 | done | span `[3,10]` is three pages short: groups 64-100 sit on pp. 11-13; Table 1 has no block, caption and all eight cells serialised into blocks 54-57; Figure 1's labels are prose in blocks 73-76; six headings welded to prose tails; captions typed `body`, only the numbered headings typed `heading`; folio −1 |
| 27 | P-C-2015-33900-7f8065e8 | 2-10 (4-12) | 63 / 104 | done | p. 4 shared with `assumptions`: chapter 3 starts below Table 1 at block 43; Table 1 is owned whole and correctly (one `assumptions` group [34-42], `read-figure`), so its one-row-per-block shape is an extraction artefact, but the symbols it declares (d_ij, P_i, L_i, G, g) are used by chapter 3 for eleven pages without redefinition or forward reference; two rows ("Emu" = stuffed, "C" = frozen) belong to no model; group 34 announces "the LeaderRank Value LR as follows:" and no LR formula prints; `[4,12]` spans two chapters, p. 12 being all of chapter 4; prose cites "Equation (4)" for the printed (2); TC_all glossed as recruiting costs after being introduced as training costs; folio −2 |

| 29 | P-C-2015-37075-1d95d60d | 5-9 (6-10) | 41 / 70 | done | span correct for blocks 69-138 but over-reads: p. 6's top third is ch. 3 notation and p. 10's lower two thirds are `results`; the record's note says blocks 100 and 128 route the 4.2.1 and 4.3 headings, but those headings are at the tails of 99 and 127 and neither 100 nor 128 holds one; "4.1.3" numeral ends block 90 while its title alone is block 91, typed `body`; "5 Simulations" and "Added Assumptions for Simulations" print inside this chapter's block 138 while §5 itself is coded `results`; blocks 75 and 90 overstate by one page; only two numbered displays in the whole chapter; no `read-figure` job at all |
| 28 | P-C-2015-35778-39d71af2 | 2-12 (3-14) | 62 / 169 | done | nine headings typed `body` though the record books them as headings; Figure bodies have no blocks at all, captions only; 5 figures inside the span but only 3 `read-figure` jobs (groups 15, 19, 20), so two figures are read by nothing; folio −2 |
| 30 | P-C-2015-37284-dee063ba | 5-13 (6-14) | 67 / 115 | done | span overstates both ends: p. 6 is 60 per cent ch. 3 and p. 14 is twelve `results` blocks; both chapter headings (4, 4.1) sit at the tail of `problem-analysis` block 72; three of the record's note assignments name the wrong block for 4.2, 4.5 and "5. Application"; the "● Initialization" bullet has no block at all; both tables serialised into prose; one sentence (blocks 164-166) delivered in scrambled order; folio −1 |
| 31 | P-C-2015-39160-2b8963a3 | 7-11 (7-11) | 46 / 69 | done | fifteen of eighteen headings welded to prose tails, blocks 165/175/181 each carry two; both figures inside the span (2 on p. 10, 3 on p. 11) dropped from the layout entirely - no figure or caption block exists - and the chapter has no `read-figure` job; block 192 tears one section reference and one equation together; folio 0 |
| 32 | P-C-2016-42939-5fccbebc | 10-24 (11-25) | 52 / 59 | done | 47 consecutive blocks (149-195, pp. 19-25) sit inside the span but belong to `results`/`future-improvements`/`conclusion`/`strengths-limitations` - §5.3 to §7, references, Appendix; the two `read-figure` groups left for the Appendix (51-52) are 46 blocks after group 50 and cite Figures 9-10 that the body never mentions; chapter's own top heading ("3 Determining...") sits at the tail of `problem-analysis` block 91; Figure 7's caption welded into a `route` block so nothing reads it; block 126 fuses a heading with a caption; Table 2 captioned "Top 10" prints nine rows; block 104 writes "c_m = c_m/(...)" with the same symbol both sides; folio −1 |

| 33 | P-C-2016-47823-59d82231 | 8-14 (8-14) | 40 / 56 | done | eleven headings, zero `heading` blocks - every section title welded to a prose tail, "5 School Selecting" included (to `problem-analysis` block 84); §6.2.1's own body (blocks 141-147, eqs 15-17, Figure 4) is booked to `results`, so the model chapter ends on a heading with nothing under it; eq (1) names the imputed mean NULL_j while (2) calls the same mean x̄_j; block 115 is the only non-`body` block in the span and it is a figure caption typed `display`; record note says 115 "reads the Figure 3 axes", it reads the caption only; folio 0 |

| 34 | P-C-2016-50193-615bc62f | 9-13 (9-13) | 35 / 104 | done | record note puts the "3.1 Concept of ROI" heading in block 132; both 3 and 3.1 are welded into block 131 (`problem-analysis`, whose own note claims only the chapter heading), so two chapters book the same heading to different blocks and neither block holds the one it is credited with; only one `heading` block in the span (221, "3.2") and it is typed `route`; the 4x4 AHP matrix in block 176 is row-desynced and unusable for arithmetic; Figure 2's caption is the placeholder "Figure 2: general title." and both panel labels read "(a)/(b) Grey Predicting for Future ROI"; the chapter's last block (235) swallows "4 Model Construction"; equation numbers are paper-global so the chapter starts at (8); folio 0 |

| 35 | P-C-2016-52815-2e6f0093 | 5-12 (6-13) | 38 / 41 | done | span starts a page late - group 1 (block 31) prints on PDF p. 5 under "3 Model Components", which sits in `problem-analysis` block 30's tail; the chapter is interrupted: blocks 69-72 are "5 Problem Statement and Special Considerations" (`assumptions`) between 4.3 and 6.1, so the unit list is page-sequential not chapter-sequential; five headings fall in prose tails ("4" in `read-figure` block 60, 4.1 in 61, 4.2 in 64, 4.3 in 66, "6"/"6.1" in `assumptions` block 72) and the span's only `heading` block (69) is the other chapter's; PDF p. 10 is figures-only with no prose, so groups 26-27 have no citing sentence on their page; block 60 welds Figures 4 and 5 captions and then the section-4 heading; Figure 6's citation precedes it by a page and its caption is spliced mid-sentence into `derive` block 65, losing the sentence's object; no equation is numbered anywhere (24 set-off equations + the Algorithm 1 box, all unnumbered); block 54 merges 3.4 and 3.5; folio −1 |

| 36 | P-C-2017-55261-f877d0a0 | 4-14 (5-15) | 50 / 102 | done | chapter opens mid-page on PDF 5 (Table 1's five-row constants grid plus two `assumptions` bullets, blocks 55-64, above the chapter heading) and closes mid-page on PDF 15 (the `results` heading plus two paragraphs, blocks 167-169); the record's note claims "eight simulation tables" - seven print inside the chapter (2-8) and the eighth is the previous chapter's constants grid; captions print below their grids, so blocks 161 and 164 weld "Table 6"/"Table 7" captions to the heads of Tables 7/8 and units 48-49 each credit the preceding table's caption; the paper's own "results are tabulated in Tables 4 through 6" prints above Table 3, leaving Tables 3 and 4 uncited; every results table carries an unnumbered bold title above and a numbered caption below; only one `heading` block (65) - "Flow-Density-Mean Speed Model" is a `body` block, "Lane Change Model" is the tail of `read-figure` block 98 and the three Case labels are run-in; unit 14 [88, 90] is recorded before unit 15 [89] though block 89 prints first; unit 41's hole [144, 147, 148] is Table 5 interleaved into a split sentence; the record mislabels units 43 (prints density k′) and 45 (prints queue length) and unit 40's t_min is a time the page calls a "minimum gap distance"; display (2) prints the reciprocal of the space mean speed it defines, and (14)/(15) drop λ from the exponent; ten block tails end in "Team #55261 Page N of 28"; folio −1 |

| 37 | P-C-2017-55278-a011d0e2 | 4-11 (5-12) | 49 / 102 | done | chapter's own top heading ("2 The Models") is the tail of `assumptions` block 46, so the span opens below it; one of twelve headings is a `heading` block (47) - four own a `body` block each (72, 107, 119, 124) and seven are welded to prose tails (46, 48, 82, 89, 100, 130, 138); the 2.2.1 numeral ends block 71 while its title is all of block 72; groups 30 and 35 are heading-only units given `route`; kind field inverted - all nine equations typed `body` and the only `display` block (96) is a chart's tick text; Figure 1 is in the layout twice (blocks 95-96 hold axis labels and ticks, unit 18 does the reading); Figure 3's caption is welded into `define` block 139 with the artwork on p. 12 and no `read-figure` job; notation table 25 rows over 23 blocks (55 and 70 carry two rows each, header row inside 48) with every block ending on the next row's symbol; T_r and T_rh both declared "response time for a human driver" and T_r never used; record note credits the 2.4.1 heading to blocks 102-106 (it is 107) and 2.4.3 to 123 (it is 124); no equation numbered; block 148 welds "3 Analyzing the Model by Simulation"; folio −1 |

| 38 | P-C-2017-55583-34388031 | 3-7 (8-12) | 28 / 53 | done | printed title is "3 Model Construction" and it is welded to `assumptions` block 82's last notation-row ("Table 1: Notations. 3 Model Construction"), so the span opens headingless; span ends one page into `results` (blocks 136-144 on p. 12); block 135 fuses the (12) display of p. 11 with the "4 Model Extension and Simulation Analysis" heading of p. 12 in one block; only two `heading` blocks (83, 102) while "3.3"/"Car Velocity v"/"3.3.1" ride block 124's tail and "3.3.2" block 127's; record says unit 9 "points at Figure 1" - block 97 names no figure and both Figure 1 citations sit below the artwork on p. 9; Figure 2 has no `read-figure` job (caption welded to block 107's tail, grid on p. 10); unit 22 straddles p. 10/11 with both headings at the top of p. 11; t_response = 1 with no unit feeds equation (4); 60 mph -> 27 m/s -> "7 unit length per second" although 27/4 = 6.75; equations (11) and (12) are the same estimator in two forms (indexed mean vs bare Σ over a hard-coded 224); 224 road sections first print in the chapter (block 134), not in `results`; folio −5 |

| 39 | P-C-2017-55585-278f2f68 | 4-13 (6-15) | 72 / 162 | done | chapter's own two headings ("3 Choice and Basic Settings of the Model", "3.1 Choice of the Model", `heading` blocks 85-86 on p. 5) and its opening 290 words (blocks 87-88) are coded to `problem-analysis`, so the span opens mid-paragraph at 89; not one heading inside the span is a `heading` block - twelve headings all ride prose tails (3.2 into 88, 3.3 into 94, "4 Details of the Model" into 103, 4.1 into 104, 4.1.1 into 105, 4.1.2 into 126, 4.1.3 into 145, 4.2 into 181, 4.2.1 into 182, 4.2.2 into 193, 4.2.3 into 200, 4.2.4 into 232) and one of them, 4.2.4, is the tail of a display block (232, the second STEP line); the three `display`-kind blocks (117, 151, 180) are figure label clusters while all seventeen printed equations are `body`; equation numbering runs (3.1), (3.2) then jumps to (4.3) - **(4.1) and (4.2) print nowhere in the paper**; (4.3) and (4.7) each carry two equations under one tag; twelve unnumbered set-off implication lines plus four STEP lines in two pairs, the two STEP pairs indistinguishable in print although one is the NSDV procedure and one the SDV; Table 1 (9 rows over 11 blocks, tail running into Figure 1's key row) and Table 2 (4 rows over 6 blocks) are both captioned "Table 1"/"Table 2" and both cited as "Tab. 4.1.1"/"Tab. 4.2.1", numbers the pages never print; Figures 3, 4, 5, 7, 8 and the 9/10 pair are each split into an artwork unit and a caption unit, so fifteen `read-figure` units read ten figures and no job reads a quantity; block 249 welds Figure 9's and Figure 10's captions across the column gap, leaving "tions" under Figure 10; unit 32 holds a "• Deceleration" bullet with no body before Figure 4; eight units straddle page breaks (8, 12, 19, 26, 37, 44, 51, 70), unit 26 fusing Figure 3's caption on p. 9 with the next page's bullet; the 2.67 m/s2 acceleration does not follow from (3.1)/(3.2) - 4 m per 1.5 s is a speed, the acceleration is 1.78 m/s2; "ΔD_A" from p. 10 on for the table's "Δd_i"; Figure 2 gives Lane 1 "P_1,A ⩾ R" and Lane 5 "P_1,A ⩽ R", so equality prescribes both at once; Figure 10 writes "Δd_min" where Figure 8 writes "D_min"; p. 14 cross-reference "the same as those in ." has an empty referent; folio −2 |

| 40 | P-C-2018-72969-f2349d15 | 8-17 (8-17) | 40 / 55 | done | block 68, the 4.1 paragraph that proposes the Figure 2 taxonomy, was refiled to `problem-analysis`, so the chapter now opens on the printed `4.2` heading and the old stored window that overran both ends is gone; a whole block reprints across the p. 11/12 break - "(8)", "(9)", "(10)" and eleven prose lines print twice under the same numbers, and the layout keeps only the first copy, so blocks 92→93 step over the repeat; (11) and (12) print nowhere, the run jumps (10)→(13), and block 95 ends on "…Absolute Mean Error between two states i and j, denoted as" while the next leaf opens with (13) = `|G_i − G_j|/|G_i|`, a factor-similarity ratio that is not the promised AME, so that display is printed nowhere; the record's `heading` field is one section behind the print ("4.2 / 4.3 / 4.4" vs printed 4.2, 4.2.1, 4.2.2, 4.3, 4.4, 4.5); only two `heading` blocks (69, 109) while "4.2.1" is a zero-word block 70 with its title alone in 71, "4.2.2" rides Figure 5's caption block 89 with its title in 90, and "4.4" is welded to Table 4's grid dump (block 100); p. 17 prints the "Technique 2" subhead, two paragraphs and (20)-(23) between blocks 122 and 123 with no block of their own and no mention in the note; kind field inverted - all 24 printed displays typed `body`, the eight `display` blocks (78, 83, 103, 108, 111, 117-119) are figure ticks, table cells and diagram labels; a shop watermark prints in every running head and is welded into blocks 79, 98, 121; all four tables are `read-figure` units and Table 6's caption (107) is a block before its own grid (108); Figure 5 draws 18 unlabelled panels under "the placing order is the same as Table 3" while Table 3 has 20 items; block 72 announces "four typical time series" and names three; block 91 cites "Shown in Figure 4" for the fluctuation argument; block 122 starts mid-word ("t. An intuitive example…"); Figure 9 prints on p. 16 and is cited only on p. 17; block 123 cites "Fig. 10" which prints outside the span; equation (7) adds a standard deviation to a variance ("+ σ" against (4)'s σ²I, crop-verified); folio −3 |

| 41 | P-C-2018-73767-a72d3a8a | 7-19 (8-20) | 47 / 66 | done | printed chapter is section 5 and the span opens three pages early - block 61 starts at the top of p. 8 under "3.3 Data Synthesis and Classification" / "4 Energy Profile", and the chapter's own title "5 Model Construction 5.1 Decoupling Analysis" is welded into block 81's tail, so units 1-14 are the previous chapter's four-state profiles; the span's last unit 47 also welds "6 Testing Our Model 6.1 Predicting Reliability Test" and serialises Table 9 into prose; zero `heading` blocks in 66 - 5/5.1 into 81, 5.2 into 85, 5.3 into 97, 5.3.1 into 98, 5.3.2 into 103, 5.4/5.4.1 into 107, "5.4.2" flush against the (10) display in 114 (the note says 115), 5.4.3 into 118, 6/6.1 into 126 - while all three `display` blocks (90 "where" clause, 92 Table 5 grid, 101 table header row) are furniture and all 21 numbered displays are `body`; "5.4.3" prints twice on p. 18 ("Analyzing the Error" and "Predicting the Target Values"); equations (11)-(16), the BP learning rules of p. 17, have no block at all - block 118 ends "drive the core formulas" and 119 opens on p. 18; (21) is split across units 45 and 46 (number in block 124, expression in 125); cross-references print as placeholders - block 119's pointer is "the equation N", and "formula 15" is cited for both (20) and the ARMA line numbered (21); Table 5 is captioned "the regression results of Equation 1" though (1) is the average price and the grid holds eight regressions, and its ln(Pop) NM cells are starred while block 94 concludes population has no significant influence; Table 6 labels a row "(Csr)" whose formula prints Cnr, Figure 6 writes "Da" for "Dpa", and Cep = Tcs/Tpo is a share used as the per-capita environment term; Table 3's caption names Figure 2/Figure 3 while its rows label Figure 1's panels and Figure 2's bars; Table 4's "Quantitative Change" column holds levels with units; Figure 4's caption prints "FTE" for TFE; Figure 5 is over-read as solar/wind/hydro though its caption says CRE; Figures 1, 2, 3, 6 and Tables 2, 3, 4 have no citing sentence, and Figures 8/9/10 survive only as one caption line welded into the `route` unit 43; Table 7 (unit 33), Table 4 (unit 9) and Table 9 (unit 47) are serialised into their unit's prose while the caption gets its own block; block 82 ends "the stronger the" so the elasticity display prints before its own lead-in; the two-column measure breaks mid-word around the shop watermark ("syste/m", "comp/rehensively") in blocks 86-88, and the watermark is inside blocks 88, 96, 105, 117, 118, 124, 125, 126; p. 17's running head prints through a body line; folio −1 |

| 42 | P-C-2018-78577-919f0d0f | 9-13 (12-16) | 27 / 32 | done | rebuilt to the 2026-10-24 re-coding, which drops the old first unit: the chapter now begins at block 124, so the section title "4 Model for Overall Score 4.1 Overview of the Model" is a welded tail of `problem-analysis` block 123 and the coded chapter has no title of its own. 807 layout words over 27 units (29.9 per unit, 25.2 per block, median unit 29, unit range 5 to 68, 15 of 32 blocks 19 words or shorter, 28 `body` / 3 `display` / 1 `heading`); 24 of the 27 groups are a single block. Blocks 122-123 ("Mexico has recognized an economic interest…", "All of the four states have regulated policies…") are `problem-analysis` and share p. 12 with the span's first unit; five headings ride tails (4.2 into 128, 4.3/4.3.1 into 135, 4.3.2 into 138, 5/5.1 into 147) while the span's only `heading` block (144) is the 4.4 title with no prose and the 4.3.1 title is a zero-prose `body` block (136); unit 147 welds "5 Prediction of Energy Profiles 5.1 Model of ARIMA", so units 23-27 are the next chapter and block 156 ("5.2 Solution and Results of ARIMA") is a `heading` block in `results`; **Figure 9 prints as an empty frame** (0.0-1.0 "Overall Score" axis, smeared year axis, no series) and block 147 ranks the four states from it; two displays and their glosses belong to no block - (2) with "where x_i is the ith index…", (3) with "In order to make the data values range between 0 and 1…" and (4) with "To determine the coefficient k_i…" all print between blocks 131 and 132 on p. 13, and (6) with its thirty-word "where the former part is the autoregressive process…" prints after block 155 on p. 16 with no block at all; Tables 4 and 5 share one block with both captions ahead of both grids, so the citing sentence "as shown in Table 5" is followed by Table 4's caption first; Table 3's twelve cells are serialised into the sentence inside `read-figure` block 137 whose first half is the heading block 136; block 138 swaps the cumulative proportions ("0.93 for clean energy, and 0.98 for renewable" against the table's clean 0.93549/0.97887 and renewable 0.83952/0.93164); block 142 cites "as is shown in Table 3" for a rule over GE, U_r and U_c that Table 3 does not contain; Table 4's rows sum to 0.790, -0.552 and 0.222 although (5) normalises d_i over m indicators, and GE's weight is negative (-0.105 AHP, -0.389 Combination) with no sentence saying so; Figure 6 draws five leaves folding into three categories while block 126 says PCA gives "two energy indices – U_c and U_r", and Figure 7's curve puts its median guide at 0.62 while (4) sets u(median) = 0.5; the ARIMA bullet is torn mid-word over three blocks (149 "…method; •", 150 "…undeter-", 151 "…Autocorrela-", 152 "tion Function)"); units 25 and 26 are bare bullets with no body; the watermark sits inside blocks 128, 134, 141, 147; folio −3 |

| 43 | P-C-2018-80560-ad2eea75 | 5-14 (8-17) | 42 / 82 | done | block 125 is a four-page swamp - booked as one `limit` unit of 68 words on pages [12,15] it silently owns printed 10 and 11, which the text layer renders as nothing (10 words each, watermark and head only): reason two, the "5.2 Dynamic New Keynesian IS-LM Model" heading, the Keynes 1923 epigraph, two framing paragraphs, a ten-row uncaptioned parameter table headed "Detotation", a bare "• IS curve" bullet, then (8) to (12) and the unnumbered three-line "Big Picture" system whose third line is orphaned onto printed 12 - roughly 1,400 printed words inside a 68-word block; block 133 is recorded [15,16] but its lead-in and (13)(14)(15) print wholly on printed 12; "4 EROI Evaluation System / 4.1 EROI Definition" print between blocks 55 and 56 with no block, and "5 Predictive Modeling" is welded backwards into block 120 ("…Arizona and New Mexico. Predictive Modeling 5"), so the heading's number follows its words; ten captions are typed `heading` (101, 106, 111, 112, 115, 117, 119, 127, 134, 135) while real headings are `body` and printed 13 carries no prose block at all; three tables are captioned as figures - "Figure 7: The external cost of energy", "Figure 8: The influence rate of every end-use sector", "Figure 13: total EROI of Four states in 2009" - so block 100's "the following table" lands on a figure number; (10) and (15) print the same IS curve with θ_z and θ_x transposed, θ_i appears in the fitted set with no equation containing it, and the α vector gives six weights for five lags; "Figure 9-12" is cited for the prediction profiles that are Figures 15-18, Figure 14's 15-panel grid is never cited by number and its caption exists only in the raster (the string "Figure 14" is in no text page), while block 123's "The graph shows…JFACB (Row1, Col.2)" sits a page before the grid it means; three prose stretches print with no block on printed 12 ("The parameters (φ, λ, γ, θ_z, θ_x, θ_i) are therefore set…", "To further avoid redundancy we have chosen 10 MSNs…", "• Results of New Keynesian Model"); block 136 is the watermark alone (1 word, x0 = 0) and pairs with block 137 as unit 42; Figure 13's row reads AZ 37.27 / CA 50.32 / NM 38.96 / TX 39.49 while block 120 ranks "Texas, Arizona and New Mexico", putting NM below AZ against its own table; watermark also inside blocks 125 and 133; folio −3 |

| 44 | P-C-2018-82150-43b69981 | 8-12 (11-15) | 11 / 19 | done | first chapter in the lane with **zero numbered displays** - 22 unnumbered expression groups print (4 on p12, 8 on p13, 7 on p14, 3 on p15) and no sentence cites a formula by number, the only numeric cross-reference being "(refer to figure 4-10)"; the chapter's opening headings "4.3" and "4.3.1. Index Selection" both ride the tail of block 107, which the record files under `problem-analysis`, and "4.4 The prediction based on VAR Model" rides block 126's tail; **4.3.2 prints twice in one section** (block 115 "The EM-TOPSIS-PROMETHEE evaluation model", block 118's tail "The Final Ranks"); about a page and a half belongs to no block and no text page - after block 114's "…the standard structure." the print carries the A2 display with its where-line, the full A3 and A4 definitions, "Let S = [CA AZ NM TX]" and the whole Step 1-3 derivation (standardisation, p_ij, e_j/g_j, w_j and W, Z, Z+, Z-, TOPSIS distances, PROMETHEE preference and flows, S_t+), while text/pages holds 87 body words for PDF 13 and 89 for PDF 14 (printed 10-11) against roughly 330 and 200, and block 118 declares [13,14] with neither page inside it; units 6 and 7 are `read-figure` over tables (Table 4-2, Table 4-3) while unit 10 is a caption whose choropleth has no block, its labels surviving as "CA AZ NM TX" welded onto block 124; the layout files block 123 (the S_t+ continuation) before block 124 (the score header it continues), and 124 names the states "Arizona, California, New Mexico, Texas" over a grid headed CA AZ NM TX with a stray "t" before the header; "where Z_j+ = max_i(x′_ij), Z_j+ = min_i(x′_ij)" defines one symbol as both max and min, the PROMETHEE positive and negative flows print as the identical "(1/(m-1))Σπ(d_ak)", P(d) gives {1, d ≥ 0 ; 0, d ≤ 0} both values at d = 0, z_ij = w_j × x_ij is built on the raw matrix, "X′ = X = (x′_ij)" declares the standardised matrix equal to the raw one, p_ij runs on the raw A1 column that holds negatives, and w_j sums a j-term over i to n; Table 4-3 fails to reproduce from Table 4-2 in four of sixteen cells (NM A1 0.3636 vs 0.368, TX A1 0.741 vs 0.748, AZ A3 0.684 vs 0.689, NM A3 0.368 vs 0.376); the printed vectors φ+=[0.4109 1.0000 0.2248 0.3643] and D-=[0.3944 1.0000 0.2440 0.5490] cannot be the Z+ and Z- the formulas define (which must be W and the zero vector since every column spans 0 to 1) and each carries a raw 1.0000 in slot 2, yet the final scores do close with ζ = τ = ½; Figure 4-10's choropleth paints California palest and Texas darkest against the chapter's own ranking; the verdict paragraph says "Texas ranks second" then "Texas … is in the worst shape"; Figure 4-9 counts Nuclear as renewable and its Texas bar stops short of 100%; watermark splits sentences in blocks 108, 117, 118 and 120; folio −3 |
| 45 | P-C-2019-1900577-7ac4ae90 | 6-15 (7-16) | 45 / 55 | done | the chapter's own title "5 Model Development" prints at the top of p. 7 inside block 82, a 17-word `assumptions` bullet ("• Without external influence, an addicted population will continue their current trend of drug use [10]. 5 Model Development"), so the span owns no heading block - all 55 blocks are `body`, no block is typed `heading` or `caption`, and eight headings ride prose tails (5.1 into 85, 5.2 into 92, 5.3 into 99, 5.4 into 100, 5.5 into 110, 5.5.1 into 111, 5.5.2 into 115, 5.7 into 130) while 5.6 is split - the number welded to Table 2's caption in 120, the wording alone in block 121 with no prose behind it; **eight blocks claim a page they never reach** because the next page's folio string sits in their text (87 "7 of 24", 96 "8 of 24", 103 "9 of 24", 106 "10 of 24", 111 "11 of 24", 117 "12 of 24", 132 "14 of 24", 137 "15 of 24"), which widens `pages` to a two-page range although the prose stops on the first page in every case; display (3) is fragmented over three blocks and printed out of order - 90 ends "Ij X", 91 prints "Si = {j ∈N | 1 ≤j ≤n; j̸ = i} Pi = , (3)", 92 opens "r2 i,j jϵSi 5.2 Model Construction", so S_i precedes the sum it indexes and the heading welds to the last fragment - (4) splits over 97/98 ("∆Drugi = + 1 (4)" then "IiImax n,i nϵSi") and (5) prints its lead-in in 112 with only "r²_{n,i}" in 113, while (2) and the unnumbered Haversine formula sit inside prose blocks 86 and 89 with no set-off block at all; unit 12's prose calls the scale "the ratio between the median and current influence factor values [8]" (µ_I/I_i) while (4) divides by the product "I_i I_max", and neither µ_I nor I_max is defined anywhere in §5 - both are defined only in Table 1 on p. 6; arithmetic that does not close - unit 45 says residuals 41631 are "a 12.2% decrease from the 47408 … and a 3.9% decrease from the 45539" (actual 8.6%, and 3.9% is unit 20's baseline-versus-model figure), and unit 24 calls 0.786 → 0.913 a "16.6% increase" where it is 16.2%; unit 24 cites "(Figure 10)" for the baseline, which prints on PDF 25 with Figures 8 and 9 on PDF 18 and 25, all outside the span; unit 45 opens "With the adjusted model, as shown in Figure 7" and closes "(Figure 6)", and block 136 is Figure 6's caption, the non-adjusted comparison, while Figure 7's caption prints on p. 16 with no block in the span; Table 2 is uncited, its caption promises "2018-2025" while its rows run 2018/2020/2021/2023/2024, its header "Year Counties 2018" prints in block 118's prose tail and its caption in 120, and "Fairfax City County, VA" appears among the eleven already above threshold in 2017 (unit 31) while Table 2 lists "Fairfax, VA" as rising above in 2018; Table 3 is spread over 127 (citing sentence plus header row), 128 and 129 (rows .861/.790/.744) with its caption last in 130 where "5.7 Adjustments" welds onto it; Figure 5's caption "Trends in R2" describes two histograms and arrives in block 126's tail together with both panel labels and the folio ("13 of 24 Low median R2 value High median R2 value Figure 5: Trends in R2"), and Figures 2 and 6 report the same 2014-based prediction of 2015 as two different point clouds; symbol reuse across the chapter - m₁/m₂ are masses in (2) but slopes in (4)/(6)/(7), r is kilometres in Table 1 while r_{i,j} is metres, and r_{i,j}/r_{n,i} stand for one quantity; unedited prose - "proximity to to", "a exponential decay", "for a each factor", "Cuyajoga County", "the factors in Table 3 into our model"; this paper carries no shop watermark, so the only furniture inside blocks is the page footer, and folio = PDF − 1 (p. 7 = "6 of 24", p. 16 = "15 of 24", M = 24) |
| 46 | P-C-2019-1901213-f6750caa | 6-10 (7-11) | 26 / 32 | done | the chapter title "5 Model" and the word "Nomenclature" print at the foot of PDF 7 in no block at all, and the eight-row nomenclature grid is coded under `assumptions` as blocks 67-72, one row out of phase - each block holds one row's description followed by the next row's symbol (67 "Health of all counties in year t sorted by FIPS code xt =", 68 "Opioid problem … A = Adjacency matrix Q = Transition matrix δ =", 69 "Threshold … St ="), so the eight printed rows become seven blocks; **zero heading blocks** in the span - all 32 blocks are `body` and thirteen headings ride tails (5.1 into 75, 5.2 into 78, 5.2.1 into 80, 5.2.2 into 82, 5.2.3 into 86, 5.2.4 into 89, 5.3 into 91, 5.3.1 into 93, 5.3.2 into 95, 5.4 into 99, 5.4.1 into 100, 5.4.2 into 102, and "6 Solutions" into 104, so the next chapter's title is carried by a `model-establishment` unit); display (1) is a schematic whose label layer is its own record group - block 73 ends "= + (1) |{z} |{z}" and block 74 is only "|{z} Future Surrounding Internal opioid problem well being opioid problem" - and (3) is split so that its number and minimiser print after the equation ("X ∥xt+1 −Q′Axt∥ Q = min" in 90, "(3) Q′ t Here, the summation of the norms is over all t" in 91), while the unnumbered x_t display tears across 81/82 ("= 2nt −nt−1") and the adjacency entry across 83/84 ("( 1" then ", i̸ = j distance between county i and j ai,j = 1 , i = j"); unit 21 is one gloss cut into three groups of 11, 7 and 9 words ("where β2 are the parameters of the model that brings p(i)" / "→1 for infected counties and t p(i)" / "→0 for non-infected states. t 5.4 Combining the two models") and unit 4 is "We will use n(k)" (5 words) followed by "to denote this health measure of country k in year t", so a superscript ends a group; block 81 opens with its own object ("xt to represent the opioid problem of each county in year t."); (3) defines Q as a minimisation over Q′ while Q′ appears nowhere else; (6) mixes indices (x_{t+1} = θ·QAx_t + (1−θ)·S_{t+1}β1) and its θ is promised as "a parameter … we can choose … that minimizes the error" with the search printed three sections later as a corner - "We varied θ from 0 to 1 in steps of 0.001 and found that we get the best prediction when θ = 1 i.e., we only consider the external model", so the two-subsection fusion is discarded by its own fit; no figure and no table inside the span, and the first figure the results cite ("Figure 1 shows the spread of infected counties from year 2010 to 2016") is introduced nowhere in the chapter; typos "country k", "non-infected states" for counties, "logisitc"; no watermark or footer string inside any block; folio = PDF − 1 (p. 7 = "Page 6 of 29", M = 29) |
| 47 | P-C-2019-1901679-1f246132 | 8-15 (8-15) | 51 / 65 | done | no printed folio on any page - the head prints "4. PART I: CHARACTERISTICS OF THE EPIDEMIC … Control #1901679" with no page number, the head turns over to "5. PART II" on PDF 12 which still carries Part I matter (Figure 6, section 4.2), and only the contents (4→8, 4.1→10, 4.2→11, 5→12, 5.1→12, 5.2→13, 5.3→13, 5.4→14, 5.5→14, 6→15) gives the printed page, every entry equal to the PDF page, M = 29; **the same chapter codes its headings two ways at once** - 4, 5, 5.1 and 5.3 own `heading` blocks (85, 128, 129, 139) while 4.1/4.1.1/4.2/5.2/5.4/5.5 ride prose tails (97, 115, 124, 135, 144, 148) and 4.0.1 is split into 86's tail plus the title-only `body` block 87, so 5.2's whole string exists only inside block 135; **eight figures and no block holds any artwork** - Figures 2 and 7 print with no number and no caption, surviving only as the `display` blocks 91 and 146 ("(a) Prevalence of Opioid Abuse (b) Rates of Change of Opioid Abuse" / "(a) Error b/w Random Walk and Data (Noise) …") while the prose cites them as "Figure 2a" and "Figures 7a and 7b", and of the eight `read-figure` units (4, 8, 9, 23, 27, 30, 47, 51) seven hold only a caption or a label pair; both numbered displays sit inside one prose block in scrambled order (block 120: "number of counties of that class ∗ Aclass = (1) #neighbors classes X Apredicted −Areal Errtotal = (2)") and no sentence cites either number, while the one unnumbered display, the 6x6 penalty matrix, is mangled in block 107 ("| 1 LS 4 2 3 2 1 | 4 HS 1 3 2 3 2 | …" - row labels shifted into the numeric columns, brackets dropped); block 144 opens with the **unresolved LaTeX reference "As seen in Figure ?? below"** and says the error "decreases again after 4 years" where block 145 and Figure 7a peak at 2013; Figure 6's caption calls counts of counties a "Class Prevalence" and its axis carries five classes (High Decreasing missing) against the chapter's six, with three different orderings of the same set in one chapter (block 95 legend 1 LS 2 HS 3 LD 4 HD 5 LI 6 HI, Figure 6 axis LS HS LI HI LD, Figure 3's bare 1-6 column); cross-references point nowhere - block 127 to "section 5.6" (Part II ends at 5.5) and block 141 to "section 6.3" which is Sensitivity Analysis - and [20] is attached both to Brownlea's hepatitis model (95) and to Moran's I (119); block 131 writes "1.9 Hispanic or Latino Americans" with no unit and "nearly 107% annually", block 136 lists disability as both received and removed; block 150 welds "6. A SECOND MODELING APPROACH: Spatial Regression" onto Figure 8's caption while block 151 (booked to `results`) prints above the `heading` block 152 carrying that same title; running heads are welded into blocks 96, 118, 125, 133, 144, 150 and inflate units 9, 29 and 51 to two-page ranges; typos "Socioecononomic" (5.3 title and contents), "over fitting too the specific scenario", "Coounties", "Portion of Population"; text layer complete on all eight pages (304-828 words); printed page = PDF page |
| 48 | P-C-2019-1906204-4e0a421c | 3-16 (5-18) | 78 / 133 | done | the span covers 146 ids (33-178) but owns 133: **13 print inside the window under other chapters** - 37-41 under `assumptions` (PDF 6-7) and 136-143 under `results` (PDF 14-15), so unit 50 (block 133) ends "3.6 Evaluate County Opioid Problem in the Future 3.6.1" and the section that heading opens is `results` matter, the chapter resuming at block 144 with "3.7" on PDF 15 - a chapter boundary drawn through the middle of a section, not an uncoded gap; **the chapter opens inside 2.1.1** - block 33 is the text of "Use K-means to Divide Areas" typed `body` with the numeral 2.1.1 riding block 32's tail, and the chapter's own "3 Models" does not print until block 48; **four `heading` blocks exist in 30-180** (72, 97, 144, 179) and two headings are split numeral/text - 2.1.1 (numeral in 32, text block 33) and 3.5.1 (numeral stranded at the end of 128, text alone in 129), so a five-word `define` unit ends with the next section's number; the record's `heading` string lists nine headings where the print has eighteen, and renames 3.1 "Similarity" against the printed "Basic Model Description" with Similarity demoted to 3.1.3; **display halves stored in reverse reading order twice** - 58 holds the Corr numerator before 59's definition, 80 holds the Score summand before 79's "Scorei = j=0 and j̸=i"; the time-decay Total is not a display block at all but the tail of prose block 69 ("2016 X dataiνi−1 Total = i=2010"), the QP minimisation line is in no block (only 94's ", where ξi is slack … ζi > 0" survives) and xi is used there while the formula writes ζi; **Algorithm 1's line numbers attach to the line above** - 102 "simi_zones ← zi's all similar zones 4:", 103 "for Each Drug dj do 5: … 6:", 105 "for Each Training Sample sk do 8:" - so the nineteen-line listing reads one line late, and 103 merges lines 5 and 6; **a fraction lost its numerator into the previous block** - 107 ends "…find difference between predicted value and real value 13: 1 take" and 108 begins "0.01+(difference)2 as weight", the printed rule being 1/(0.01 + difference²), the same loss repeating at 121; **Table 2's grid and caption are different units with different jobs** - the ten rows print inside `interpret` block 164, the six-word caption is `read-figure` block 165, and the handoff sentence has an empty slot ("and the final result is ."); Table 3 is de-interleaved one row out of phase over 167-171 ("Female_householder_no_husband_present HC03_VC09" …), nine printed rows becoming five blocks plus a caption; Figure 7 costs five blocks (83-86 four `display` label clusters including the one-word "Methorphan", 87 the caption) and Figure 4 costs six (42-46, 7-25 words each), 15 of 78 units carrying no prose; arithmetic that does not close - Σ from 2010 to 2016 is seven terms against "six years of data(2010-2016)" (55, 69) and "100×69×6" (100, 110), "we divide the data in the table into 16 categories" against Table 2's ten rows, "the largest 5 nodes" (77) against Figure 6's printed `Candidate Set: 10 7 1`, and Table 1 printing HC03_VC08/VC09 where the prose item set lists HC03_VC10; figures 13-17 print on PDF 14-15 but are read by no unit of this chapter, so the chapter's twelve figures are 1-12 and 18 while Table 2's pointer dangles; **zero equation numbers** - twelve unnumbered set-off expressions, six of them split across blocks - and no prose sentence cites any object by number, every reference deictic; three `source` units are not sources (76, 77 are rows of a boxed factor list, 48 a kernels description) and three `derive` units derive nothing (71, 78, 178); a whole sentence prints twice in block 74 ("construct a propagation graph model" then "construct a propagation map model"); Figure 5's node labels render as `*`/`**` so no node is identifiable, Figure 3's legend labels 20 of 100 zones and is titled "Clustered Counties" under a "Clustered Zones" caption; no watermark, folio = PDF − 2 (p. 5 = "Page 3 of 38", M = 38 inside a 40-sheet file with two unnumbered front sheets) |
| 49 | P-C-2019-1922154-b7129095 | 2-14 (5-17) | 69 / 98 | done | the chapter title "2 Terminology, Symbols and Assumptions" and "2.1 Terms" print at the foot of PDF 5 inside block 48, a `problem-analysis` block that also carries Figure 1's caption and whose text layer stops at "2 Termino"; **the `assumptions` chapter's heading rides a `model-establishment` block** - "2.3 General Assumptions" is the tail of block 58, the same block that holds Table 1's last six rows, while the four assumption bullets are 59-71 under `assumptions`; two neighbour titles ride this chapter's last blocks ("3.3 Results & analysis" into 121, "4.4 Results & analysis" into 189) and this chapter's own three section-4 headings ride `results` block 151 ("4 Model Modification Considering Socio-economic Factors 4.1 Preprocess Data 4.1.1 Data overview"), so the seam cuts both ways; **three `heading` blocks in the whole paper** (72, 73, 84) and three heading strings stored as six-to-seven-word `body` blocks (74, 80, 85), every other heading welded to a prose tail; the record's `heading` string lists nine of the twenty-five levels that print on the span's pages; **the symbol table is booked one cell per group and its symbol column trails** - 55 ends "…The ith county Ci Cin", 56 is the environment-vector definition alone, 57 ends "…in the nth year n ri y", 58 collects six more pairs, so units 3-6 are table rows and every terms bullet is torn mid-sentence (opioids 49/50, heroin 51/52, HHI 53/54/55); **a fraction's denominator opens the next block alone** - 75 ends "…identified as follows: Xi= Xi-1 + Xi+1 (1)" and 76 begins with the bare "2" plus the where-clause; **no display owns a `display` block** - (1) rides 75, (2) 78, (3) 110, (4) 112, (5) 117, (7) 120-121, each stored as a scrambled inline run; **the equation numbering has a hole** - (1)-(5), then (7) on the CI formula, then (8)/(9) inside `results`, then (10)-(13) back here, and the string "(6)" occurs nowhere in the 23 text pages or on any raster page; **Table 4 de-interleaved one cell out of phase** (179 "Percent; Males 15 years and over - Never married（Mn） Marital status（MS）", 180 "…（Fn） Educational", 181 the five ancestry cells then "Ancestry(AN)", 184 "than "very well"(Lo) 4.3 Model Modification"), four printed factor rows becoming six blocks; Table 2 read by a `read-figure` unit and Table 3 split at the page break (caption and header p15, body p16); arithmetic that does not close or cannot be checked - the same data split four ways on adjacent pages (Table 2 rows 2010-2012/**2013-2016**, Table 3 header 2013-**2017**, block 168 "divided the 7-year census socio-economic data into 2010-2011 and 2012-2017", block 152 "each of the years 2010-2016"), "So we have 3003 groups environment(vector)" derived from nothing (462 counties with k=3 gives 462 vectors), the p9 tuple "(ri n, 1,2,3,4,5) should equal to the (rj n, 1,5,4,3,2,1)" comparing five components with six, display (3) putting two lower indices "i=0,j=0" under one sigma with upper limit k, and (4)/(7) reusing the outer index in the inner sum; Table 1's definition rows are reprinted verbatim as prose in 100-101, and Table 1 continues onto p6 with no repeated header; k is defined twice (neighbours vs counties in a state), Ci three times (county, case count, identification count), and display (8)'s n and divisor a are defined nowhere; **folio -3** (p. 5 = "Page 2 of 20", M = 20 printed in a 23-sheet file with three unnumbered front sheets), running head "Team # 1922154", no watermark |
| 50 | P-C-2020-2002116-f6f4a15a | 4-18 (5-19) | 63 / 101 | done | chapter opens before its own title - blocks 53-62 are the previous chapter's 2.2 notation lead and Table 1, and "3 Informative Evaluation Model" prints inside block 62, the last table row ("Reputation rate of product at some time Mapping 3 Informative Evaluation Model"); **the block ids are not contiguous** - three runs of the window's own pages (122-126 on PDF 11-12, 142-147 on 13-14, 159-185 on 15-19, 38 blocks) are coded to `results`, which removes 3.4, 4.2, 5.3, 6 and 6.1 from the chapter, so what it keeps is 3.1-3.3, 4, 4.1, 5, 5.1, 5.2, 6.2, 6.2.1 and PDF 14 carries no model prose except a watermark fragment; **three headings are fused with the document watermark inside `display` blocks** (114 "3.3 …", 122 "3.4 …", 148 "Predict Potential Success or Failure") and in 148 the numeral 5 exists on the page and in the text layer but in no block, while nine blocks carry the string `关注数学模型 MATHmodels 获取更多资讯` (63, 74, 82, 89, 100, 114, 129, 148, 191); two numerals are detached to their titles' previous unit (3.2.1 ends 82, title alone in 83; 6.2.1 is the zero-word block 187, title in 188) and 3.2.2/3.2.3/4.1/5.3 ride prose tails (86, 102, 128, 158); six `heading` blocks exist in the window (64, 72, 127, 150, 154, 186) against eleven printed headings, and the record's heading string lists fourteen levels, opens with the previous chapter's "2.2 Notations", abbreviates five titles and omits chapter 5 altogether; **Table 1 is de-interleaved one row out of phase** - 54 holds caption, header and row 1 then the next row's symbol "sid", each later block one definition, one type and the next symbol, and 62 the ninth definition plus the chapter title - nine rows where the record's note claims "the eleven symbols of Table 1"; **display (1) is interleaved, not merely split** - 67 ends "the vector encoding forms of s can be", 68 opens "s)T ∈R5 where the components defined by: formulated by VEC(s) = (vec1 s, …, vec5", so the where-clause precedes its own main clause; **four equation numbers lead the following prose block** ((2) as "2σ j" in 92, (15) in 136, (16) in 139, (17) in 153) and (12) is stored out of print order inside its unit (numerator tail 116, exponents 117, number and "Where the 1−" 118, fraction words 119); **two fractions print numerator and denominator in the wrong order** - (13) "∆REP := 1 X" then the summand then "2z(", and (11) a bare "1" at the end of 108 with the denominator "Σ e^{x_i}" opening 109; parenthesis and sign losses in (13) ("2z(" never closed), (17) (two stray closers) and (20) (extra overline); **equation (1) prints the exponent with a plus** - raster-verified "e to the plus abs(i−s)²/(2σ0)", the sign absent from the text layer - which peaks at the furthest rating and so voids both block 71 ("the 4-star rate has the highest probability to be rated 4 stars") and block 69 ("the bigger the more robust"), while (2) uses the opposite sign for the same Gaussian form; θ0 is defined in 134 and then set as θ = 0.5 with every equation using θ, Z in prose against "2z(" in (13), double-struck REP/PEN/IMP against plain REP in prose; (12) prints exp[β(Σ int log int)] where 119-120 gloss "−Σ … is the entropy", i.e. the negative of the printed exponent; 157 cites "Eq. (18) and Eq. (18)" where (19) is meant, and (13)-(16), (19), (20) are never cited; **nine of thirteen objects are read by no unit of the chapter** (Figures 5-13 and Table 2, pages 12-19, cited only from `results` blocks 124, 144, 146, 165, 173, 174, 183), Figure 8 is named by `define` unit 58 with no `read-figure` job, Figure 1 is read twice (prose 66 and caption 75) and Figure 2 costs five blocks including a one-word `display` (80 "Aggregation") plus the 3.2.1 numeral; typos "ration", "we category", "t0 = 10 is this literature", "k2 values how much", "destroys the reputations", "The longer the liner", "we covert", "difference occurs lease", "We employ our propose", "repetitively" for respectively; folio = PDF − 1 (p. 5 = "Page 4 of 38", M = 38 in 39 sheets), running head "Team # 2002116" |
| 51 | P-C-2020-2003717-4c901da6 | 8-14 (9-15) | 55 / 80 | done | **two section headings have no heading block and one block delivers two** - 3.1 is the tail of body block 127 ("… users preference vectors. 3.1 Weighted Rating Ratio"), 3.3 the tail of 147 which is otherwise Figure 9's caption, and block 160's tail prints the p11 watermark then "4 Problem 2 (b): Reputation Metric 4.1 Reputation Metric", while 3, 3.2, 4.2, 5, 5.1 own `heading` blocks (126, 134, 167, 173, 174) - five of ten printed levels, two storage styles in one chapter - and the three §5 subheadings ride caption or display tails (178 "… Figure 12 caption 1. Input Module", 191 "… 2. LSTM Module", 205 "… 3. Output Module"); **a printed paragraph is split mid-sentence between two chapters** - PDF 12 opens with `assumptions` blocks 161 "The reputation of a product is related to many factors (e.g." and 162 "the average star rating it receives, …" and the model chapter resumes at 163, so the record's window has a hole at exactly that pair; 124-125 (`problem-analysis`, top of PDF 9) and 208-213 (`results`, bottom of PDF 15) print inside the window's pages; **the equation numbering splits down the middle** - the three measures print six unnumbered set-off displays (w_rr_i 130, the argmin objective 140, ss_t 142, avg_i 143, std_i 144, PR_i 157) and the reputation and LSTM sections print (1)-(7), with **(8) landing in `results` block 210**, so the sequence closes in another chapter's block; every number prints beside its expression and no display is torn across blocks; **a table is stored three ways in one chapter** - Table 1 (150) and Table 2 (159) are one block each holding the whole three-panel grid, Table 3 is de-interleaved over five blocks for six rows (185 "… 𝑥1 {1,2,3,4,5} Star rating 𝑥2 [0,1] Helpful rating 𝑥3 {0,1}", 186 "This review is vine voice or not 𝑥4 {0,1}"), Table 4 over nine blocks for eleven rows with the last block cramming four (202 "The weight matrix for transitions 𝑏 The bias for transitions 𝜎 The sigmoid function tanh The hyperbolic tangent function"), and the four tables are read by `read-figure` jobs because the record has no read-table job; **equation (6)'s cell-candidate line reuses the output gate's weights** - "𝑔 = tanh(𝑊_ig𝑥 + 𝑏_ig + 𝑊_hoℎ + 𝑏_ho)" [R]; **std_i cannot be computed as printed** - its numerator is "Σ_{j∈A_i}(HN_j+1) × (ss_i − avg_i)²" [R], constant inside the sum, so it cannot reproduce Figure 9's panel (b); **the objective prints y_1 for y_t** [R] while the line above maps ra_t to y_t; **PR_i is defined twice** (152 "PR_i = PD_i/Σ_{j∈[8]}PD_j", 157 the γ-weighted ratio) and **PD_i drops the γ that consideration 1 promises**, so "hence" jumps a step, while γ^{1−t} grows rather than decays; "eight main product attributes" (149) against seven rows in Tables 1 and 2 [R] with the denominator summing over i ∈ [8]; 1_{it} never defined, ss_j indexed by a timestamp set; **arithmetic that closes** - Table 1 term counts 46 / 51 / 45 [R] matching "Lexicons of 46, 51 and 45 words", Table 2 PR columns each summing to 1.000 [R] - against "take up nearly 90 percentage", which is 0.916 for the hair dryer; **prose contradicts the artwork** - 169 "the larger the window size m is, more violently the reputation curves fluctuate" while Figure 11 (m = 500) is smoother than Figure 10 (m = 200) in every panel [R], and the three panels' x-axes span 0-10000 / 0-1400 / 0-17500 time steps so no common axis exists; **two units carry the next page's furniture** - 139 holds the p9 footer plus "Algorithm 1: Logistic Regression" (so the algorithm title belongs to unit 10, not 11) and 149 holds the p10 watermark plus Table 1's lead-in, which is why it is tagged [10,11] with no prose on 11; the watermark string "关注数学模型 MATHmodels 获取更多资讯 Page N" sits in 123, 139, 149, 160, 169, 177, 192, 213; typos "Sunhine", "users preference vectors", "the occuring ratio" (bolded mid-sentence in 131), "weighted rate radio", "we obtain the avg_i, avg_i values", "N is the number of dimension", "nearly 90 percentage", "The notations for equations above is shown"; **folio −1** (p. 9 = "Page 8", M = 41 printed pages in 42 sheets), running head "Team 2003717", orange QR watermark bottom-right on every page |

| 52 | P-C-2020-2004647-771d613e | 4-16 (5-17) | 95 / 137 | done | the chapter is printed 3 to 6 on thirteen pages at folio −1 ("Page 4 of 24" on PDF 5), 4,929 layout words over 95 units (mean 51.9, median 45) but 36.0 per block (median 21), the layout tearing every numbered equation into two to four blocks and booking each table row separately; **the layout never labels a display in this whole paper** - 136 `body` blocks plus one `heading`, although the chapter prints (1)-(23) contiguously, so every expression is a run inside prose; **one `heading` block in the chapter and its numeral trails its title** - block 90 reads "Deﬁnition of α—the Rating Vector 3.2" while 3.3.1 and 4.3.1 print as bare numerals closing the previous block (132 "… (the kth model of the ith-type products). 3.3.1", 170 "… are evaluated. 4.3.1") and 133/171 are title-only; 3.3.2 rides block 149's tail, 4.3 rides 168's, 4.1 156's, 4.2 161's, 5.1 186's, 5.2 192's, 5.3 196's, and every chapter title welds onto the last block of the section before it ("4 the Reputation Model" in 155, "5 the Successfulness Prediction Model" in 183, "6 Results" in 204), so the record note's claim that block 185 carries the chapter-5 heading is wrong - 185 ends "…predictions can be highly error-prone."; **equation numbers stored away from their expressions and one inside the watermark** - (1) ends 82, (2) opens 94 as "α(t)_{i,k,1} α(t)_{i,k,2} α(t)_{i,k,j} α(t)_{i,k,n} where α(t)", (3) ends 98, (4) opens 104, (15) opens 155 welded into "关注数学模型 MATHmodels 获取更多资讯 We also…", (18) opens 163, (21) is torn over 193-196 ("1 pi,k(t) = (21) ˆ Rep(t) 1 + e− i,k ˆ Rep(t) where −" then "i,k is the predicted reputation in the tth month", with the limits split as "i,k →+∞; while p(t) →0 if −" / "i,k →−∞"); **(20) serializes both fractions as a flat token run** ("τK(X, Y ) ≜P −Q P −Q P + Q = (20) N(N −1)/2") and (23) loses its left-hand side entirely (block 202 "i,k = 0.5 −0.1e−1 10 (t−τ) (23)" for a printed `threshold^{(t)}_{i,k} = 0.5 − 0.1 e^{−(1/10)(t−τ)}`) [R]; **(21)'s gloss is sign-shifted against its own formula** - the raster prints `p = 1/(1 + e^{−Rep̂})` and then "where −Rep̂ is the predicted reputation", "p(t) → 1 if −Rep̂ → +∞; while p(t) → 0 if −Rep̂ → −∞", describing Rep̂ → −∞ giving p → 1 [R]; **Table 2 has no row blocks at all** - only its caption (92) is stored, so the five star values and their mapped ratings exist on the raster only, while Table 1 costs twelve blocks for eighteen symbol rows, Table 3 three, Table 4 two, and Table 5 is flattened into its caption block with header, both outcome rows and three product columns surviving as one comma run and no comma at the three wrap points ("#392768822" / "#667171015", "#932955324" / "#945323010", "#671647927" / "#130912179"); **all four figures are caption-only** (2 at 175, 3 at 176, 4 at 183, 5 at 191) and Figure 5's `(a) (b)` labels are captured at the end of body block 190, one unit early, while Figure 4's fifteen bars (three groups, `top1`-`top5`, y 0-0.9) and Figure 5's two GPR panels (`original data` / `GPR model` / `95% confidence interval`, dashed `training` / `validate` / `test` separators) are read by no unit [R]; **claims that do not hold** - p17 writes "Hair dryer #767062995" where Table 5 prints "#768062995", the series is "trimmed … Jan. 2010 to Dec. 2014" and then predicts "after Jan. 2014" so the two windows overlap (caption calls the horizon "a few years" against ≈1-2), "most of the calculated correlations are over 0.6" covers 11 of 15 bars with 0.17 and 0.50 in the microwave group, and the pacifier group's "close to 0.8" leaves out its fifth bar at 0.71 [R]; the watermark is not just a folio carrier here - it clips body text on p14 ("votality; th…"), p16 ("…successfulness predic- / tions could be inaccurate") and p17 ("…models' num- / bers of orders"), is serialized inside 185, 192 and 202, and the printed total M = 24 does not close against blocks on PDF 26-29 that print "Page 26"/"Page 27" at the same offset; the record's twelve-level heading string omits 3.3.1, 3.3.2, 5.2, 5.3 and 6, renames 4.3 "Evaluation of the Models" against the printed "4.3 Model Evaluation", and capitalises "3 The RRBS Model" / "5 Successfulness Prediction" against "3 the RRBS Model" / "5 the Successfulness Prediction Model"; τ is overloaded (Kendall's τ_K, launch month τ) and j in β_{i,k,j} is never defined; typos "storng", "votality", "sperated", "ramaining", "an distinct interval", "the τth is month", "negativive" |
| 54 | P-C-2020-2009116-325ae826 | 6-16 (6-16) | 68 / 68 | done | **folio 0** - the head prints "Page 6 of 24" on PDF 6 and the PDF page is the printed page throughout, M = 24, so the eleven-page window is printed 2.2 to 4.1; **one printed paragraph per block and no multi-block unit anywhere** (4,441 words, mean 65.3, median 62.5, 167 down to 6 at the lone "3.2.1 Determination of star rating index CR" line, seven units under twenty words), the only objects cut out as blocks being four `display` blocks - two caption-only figure captions (77, 82), Table 3 (88) and the AR(p) equation with its glosses (96) - while **no `heading` block exists in the chapter at all**, so all thirteen printed levels ride prose tails ("2.2 Methodology" and "2.2.1 Data preprocessing" both end block 57, "3.2.1 …" is the whole of 98, "4. Task 3 4.1 Problem Analysis" closes 123) and blocks 52-55 (`introduction`/`assumptions`) and 124-125 (`results`) print inside the window; **tables cost almost no blocks and two of them lose every cell** - Table 1 and Table 2 sit inside block 85's word-cloud paragraph, the KMO grid inside 103, Tables 3 and 4 inside 104 and 105, Table 5 inside 122, so eight grids are stored with zero dedicated blocks, and the p9 star-frequency grid and the p12 7 × 7 correlation matrix have no cells in the text layer at all [R/T], Table 5 additionally dropping three PRODUCT_PARENT ids the raster prints (ameda 985518895, baby jogger 242140507, Vintage Teaberry 460235866) [R/T]; **two table series share one numbering inside one chapter** - task 1 prints Tables 1-3 on pp. 10-11 and task 2 prints Tables 1-5 on pp. 12-15, so "Table 3" names two different objects and the record's note tracks only the first series, and no prose cross-reference is numeric at all ("the table above" in 78, 86, 106; "the figure below" in 81, 126; "the following table" in 105) while 103 announces no table although the KMO grid follows it; **no equation is numbered in the chapter, yet the prose cites three numerals that belong to a bullet list** - the only printed "(1)", "(2)", "(3)" are the three sentiment dictionaries in blocks 62-64, and block 114 then writes "Substituting the above formulas (1), (2), (3) into" for F1, F2 and F3, which were never numbered; the AR(p) equation is stored reordered against the raster (`y_t = μ + Σ_{i=1..p} γ_i y_{t−i} + ε_t` becomes "𝑝 𝜖𝑡 𝑦𝑡= 𝜇+ ∑𝛾𝑖𝑦𝑡−𝑖+ 𝑖=1", limits and ε_t displaced) and the MA and ARMA forms are welded inside body block 97 [R]; **section numbering prints out of order** - "3.3 Problem Solving" closes block 97 and "3.2.1 Determination of star rating index CR" is the whole of 98, after it; **arithmetic that closes** - 18,939 − 8 − 14 − 1,674 = 17,243, 11,470 − 738 = 10,732, 1,615 − 79 = 1,536, all three keeping 10 variables, the p9 grid's row sums 1,536 / 10,732 / 17,243 matching the pie labels, Table 1's ratios and its 49,178 / 60,545 vote totals reproducing, and the CS substitution multiplying out term by term [R] - against **arithmetic that does not**: Table 3's cumulative column is off by 0.001 twice (31.025 + 22.117 = 53.142 against a printed 53.141; 69.739 against 69.738) and the p9 grid truncates to force each row to 100, printing 286/1,536 = 18.6% as "18%" [R]; **Table 5 is titled "Pacifier Top 10 Products" and lists nine rows**; the CS weights read 0.3 (day) / 0.3 (F1) / 0.1 (F2) / 0.3 (F3), contradicting block 110's ordering that voting is main, content second and identity last, and block 106 assigns `number` to both F2 and F3 while F3 prints "0.786v + 0.726vp" with no `n` in 109 and Table 4 puts `number`'s .503 only under column 2 [R]; **the p16 six-panel figure is uncaptioned, carries a "Sentiment" y axis with no tick labels, and no unit of the chapter reads it** [R]; the record's eight-level heading string against the print's thirteen writes "2 Task 1 overview" for "2.Task 1" and calls 3.1 "AR-ARIMA" where the page prints "3.1 Problem Analysis"; typos "satr_rating" (Figure 1 caption), "asused in the General Inquirer software", "the length of the contest。", "packer.csv" for pacifier.csv, "hair guy file", "hair player", "For microave", "sampling, o ld", "Amazon rolls", "parafierde", "conclusions.Among microwave oven products", and the dangling "half of the buyers are verified_purchase, almost no." |
| 55 | P-C-2020-2010638-c32c8549 | 5-15 (6-16) | 76 / 82 | done | **folio −1** - PDF 6 prints "Page 5 of 20", M = 20; 3,037 layout words over 76 units (40.0 each, 37.0 per block, unit median 31, block median 27, block range 1-128), 29 units under twenty words and three multi-block, because the layout returns every equation fragment, caption and table note as its own block; **not one of the ten tables owns a block and four lose their cells entirely** - Table 3's eight-row coefficient grid exists only on the raster (the text layer keeps caption 90 and note 91 and its caption prints *below* the grid), Table 10 keeps caption and three row labels while its fifteen eight-digit ids exist only on the raster and the microwave row prints 423421857 twice (four distinct brands against block 140's "only 5"), Table 2 keeps one of nine coefficients (74 caption+header, 75 the single -0.101**), Table 4 keeps two description cells while its caption is welded to the end of the 76-word LDA paragraph (99) and four of its six Greek letters are lost, Table 5 and 6 keep five words per theme with no probability column although block 111 promises "10 most frequently used words and their corresponding probability", and their header prints `Theme 1 Theme 2 Theme 3` twice across one row with nothing separating the halves; **Table 8 is five rows by six columns** - six criteria are headed but there is no `star ratings` row, so the AHP matrix is not square [R]; **the chapter's first heading prints in another chapter's block** (60, `problem-analysis`, tail "…which is obtained by dividing 'helpful votes' by 'total votes' 3.2 Word Segmentation and Sentiment Analysis") and of the fourteen printed headings only three own a `heading` block (96, 97, 122 - 96/97 is faithful because the page sets "Positioning" on a second line), two sit inside `display` watermark strips (63, 121) and the rest ride prose tails (70, 79, 98, 127, 132, 134 with 4.4 **and** 4.4.1 in one block, 139, 142); `heading` is also applied to a 76-word body paragraph (99), a table caption with cells (112) and a bullet (118); **sixteen numbered equations, (1)-(16), contiguous**, two of them set in full-width brackets ((11), (12)) so a grep for "(11)" finds nothing, and the storage tears the notation rather than the numerals - (4)'s brace collapses, (8)'s six-by-six fraction matrix vanishes leaving "A=", (9) loses its product sign, (15) its minus and (16)-(19) their radicals; three more, (17)-(19), print on p16 but sit in `results` blocks; **arithmetic that closes** - Table 1's count averages (4,841,870/18,939 = 255.66 -> 256 etc.), Table 9's three weight rows each summing to 1.000 with column sums adding to 3.00, the 70/30 split, and the appendix CR = 0.00857 (block 216) - against **claims that do not close**: the chapter never prints λmax, CI or CR although (13)-(14) define them, Table 7's RI row disagrees with the standard scale at five of nine entries (0.52/0.89/1.26/1.36/1.46 against 0.58/0.90/1.24/1.32/1.45) [R], (8) builds A = [W_i/W_j] from the weights it is meant to derive and its last row ends W6/W7, (9) prints Π^n_{i=1} where the product must run over j [R], (16)'s denominator squares x_ij twice under a numerator x_ij·x_ik [R], (4)'s four bands double-count 0.75/0.50/0.25, leave every negative compound unassigned and test `compound` under a "helpfulness ratings" left-hand side [R], Table 3 calls star-rating square "SS" where block 85 says "SQ" and reuses "CS" from the customer-satisfaction score (114) [R], Table 2 prints count coefficients of 0.356** and 0.332** against block 70's "light correlation" [R], block 94 reads -0.020** and +0.002** as an "inverted-U-type" relation and concludes reviews should be "of moderate length" when the fitted curve is a convex trough [R], block 92 says "each variable passed the significance test" over a table of blanks with no `ns` printed [R], and Table 1 heads two columns "Count" with no unit while "Helpful votes average" holds 0.827182, 5.62167 and 2.17908 [R]; two uncaptioned graphics print on p12 (a four-chevron Step strip and a six-node circular diagram numbered (1)-(6)) and no unit reads them [R]; the record's nine-level heading string omits 4.3.2, 4.3.3, 4.4, 4.4.1 and 4.4.2, truncates 4.3 and ends on the placeholder "5 Model 3 heading"; typos "Star Rating Distributon", "Multionmial" (equations 5 and 6), "auto-regession model", "NTLK emotional analyzer", "4.4System Clustering Analysis" (no space) [R], "We mainly uses cluster analysis", "The product reputation is consisted with star rating", "The probability of an event happening of an event", "summarized as Table.For reasons of space", plus six table and two figure captions with no space after the colon; the QR watermark sits bottom-right on every page and never clips body text |

| 56 | P-C-2021-2101166-038bd4c8 | 5-17 (5-17) | 125 / 125 | done | **one block per unit, 125 for 125** - no group spans two blocks, so nothing the layout tore was ever resolved: the fourteen Algorithm 1 lines are fourteen units (23-35) with the line numbers rotating into the preceding block's tail ("...do 3", "9 Add j into Nt+1; 10 end 11 ... end 12"), and ten of the fourteen numbered equations are left torn - (4)'s sum limits are unit 17 on their own, (11) stores "min" after its summand (`i∈I,j∈J dij, min (11)`), (12)'s three-line brace system splits across 162/163/164 with the numeral last, (13) loses its left-hand side entirely (166 is only `max{a(i), b(i)}, (13)`); folio 0 ("Page n of 25", M = 25), 4,373 layout words over 125 units (35.0 each, unit median 17, range 168 down to 5), 68 units under twenty words; **the only `display` blocks are caption strips** (59, 110, 129, 140, 168, 169) and none is an equation; **the chapter owns eight of the twelve heading blocks and welds the other four to tails**, one of them (3.1) onto block 58, the Table 1 block itself, while 132 and 155 are orphan `heading` blocks holding nothing but a watermark string and 183 carries the "6 Problem 4" heading that closes the chapter; Table 1 is split across blocks 58 and 61 with the whole of Figure 2 printed between its two halves and its two columns interleaved ("C the set of cells Ei Nt the set of nests Ci r the growth rate γ") so each symbol meets the wrong interpretation, Table 2's header is rotated in storage, and Table 3's thirty-five cells are flattened into unit 118's paragraph; **arithmetic that closes** - 19 = 11 + 8 downloaded, 19 x 4 = 76, 76 - 28 = 48, F = 17,382.96/5,346.42 = 3.2513 printed 3.25 with p = 0.0715 printed 0.072, (329.2 - 189.6)/329.2 = 42.4% printed "42%" - against **both Table 2 SS cells printed a decade high** (the row closes only at 10⁷, and 17,382.96 + 1.097 x 10⁷ = 1.099 x 10⁷), status counts summing to 2,126 against the 2,127 valid observations, Figure 6(a)'s bars summing to about 1,891 against 2,043 negatives and Figure 6(b)'s to 11 against "only 19" [R], "63 in total" against 73 in Table 3 and 72 in the two status counts, "minimum testing loss 0.0274" against a plotted 0.031 [R], "accuracy 0.8030 after 490 iterations" against a peak near 2,500 [R], "clusters from 2 to 9" against a figure that plots 2-8 [R], and x2 in R^{2C} beside (2⁴C, ...) in the same paragraph; **equation (7) cannot draw the curve it labels** - as printed f(t0) = N and f tends to 1 with a pole just before t0, while Figure 3(g) climbs to 600 [R]; advice 2 makes cluster 3 negative while advice 3 makes it possibly positive against its 0.0746/Rank 4; the QR panel covers text on six pages and **the printed "(12)" on p15 is half-printed on the pink fill** [R]; typos "haws", "male peak females", "this area.The expression", "A wild range", "according to 1", "deconcolution", "nerves", "siloette" five times, "closet cluster", "he may be positive" |
| 57 | P-C-2021-2101587-8b253851 | 6-12 (6-12) | 66 / 66 | done | **folio 0** - "Team # 2101587" and "Page N of 25" (M = 25), 2,045 layout words over 66 units (31.0 each, median 14.5, 38 units under twenty words), no group spans two blocks and none of the three `heading` blocks is a body paragraph; **the chapter starts and ends outside its own span** - its printed heading "3 Abbreviations and Symbols" is welded onto block 53 of `assumptions` with the numeral dropped, and its closing 5.4 heading (121) belongs to `results`, so the record's `pages [6, 11]` closes one page early while units 62-66 print on p12; of the thirteen printed headings three own `heading` blocks (71, 94, 101) and seven are tails (70, 72, 78, 90, 104, 108, 113); **Table 1 prints nineteen rows and the layout returns them as fifteen units plus a welded tail**, because every row is cut between its symbol and its description (unit 13 then carries no symbol, unit 14 two - `tn` and `T` - and unit 7 fuses two rows, "... coincidence indicator (used in AHP) CNN Convolutional Neural Network"), and the last description rides in front of the "4 " heading; **Tables 2 and 3 are flattened into one block** (91): caption 2, caption 3, `λi 3.02`, the column labels, row 1 with `CRj 0.016` injected after its values, the row labels detached, then `0.285 0.498 0.217 W`, while Table 3's two headerless rows and its `W` stub are never defined; Tables 4 and 5 carry the identical caption "ResNet Accuracy", Table 5 repeats Table 4's two rows cell for cell and bolds only its new row, and all three ResNet tables are box-ruled with an empty top-left cell; two displayed equations (Poisson on p7, min-max on p8), both unnumbered, no numbered equation anywhere; **arithmetic that closes** - the AHP weights 0.2849/0.4977/0.2174 print as 0.285/0.498/0.217, λmax 3.018 as `3.02`, CR 0.0158 as `0.016`, the three reciprocal pairs are exact, the thirteen species count thirteen, 18.30 to 25.23 is Table 4 to Table 5 - against **a matrix whose judgements are intransitive** (a12·a23 = 1.0 while a13 = 1.5), **every processed-row percentage an exact multiple of 1/107** (18.69 = 20/107, 27.10 = 29/107, 25.23 = 27/107, 90.65 = 97/107, 94.39 = 101/107, 92.52 = 99/107) so both processed rows were computed over all 107 images against the "one-tenth ... evaluation set" of p11, while the website row needs a denominator of at least 1,504 and the uploaded row at least 459, `99.60%` of 260 evaluation images being 258.96 and printed identically for three depths, "rose from 18.3% to 25.23%" mixing the uploaded row of Table 4 with the processed row of Table 5 and hiding ResNet34's 27.10, prose putting trees and terrain above distance while Table 3 gives Distance 0.285 > Elevation 0.217, an 8 km maximum patrol against a 10 km disc and a Figure 1 axis running to 20 km with no axis titles at all, Figure 6's `127 x 127` against the 125 and 123 its own kernel sizes imply and no pooling or loss layer although the sentence lists both, Figures 3 and 4 the same basemap with the same three hotspots (0.56 cross-correlation), Figure 5 never naming its year, Table 1's Description column right-aligned, `CRj` glossed as "The coincidence indicator (used in AHP)", "Analytic Hierarchy Processing"; typos "buggide.net" beside "bugguide.net", "to have see", "reports,and", "5.4 Result", "three different depth layers" |

| 58 | P-C-2021-2107815-45f0e8ba | 4-15 (4-15) | 115 / 117 | done | **folio 0** - "Team # 2107815" over "Page N of 25" (M = 25, the real page count), 4,106 layout words over 115 units (35.7 each, 35.1 per block, median 25, 45 units under twenty words and 15 under ten); blocks 92-99 are the 3.1 body and the 3.2 heading, filed under `problem-analysis`, so the chapter owns the headings but not the section, and none of its thirteen headings is stored as `heading` - each is merged into the preceding body block (91, 106, 110, 125, 131, 136, 145, 150, 167, 180, 191, 195), with `4.3.1`/`4.3.2` set at body size 12 pt against the 16/14 pt above them. Sixteen distinct equation numerals printed seventeen times: 5-6 to 5-10 do not exist and **4-5 prints twice** (blocks 122 and 132, 4-6 already spent on p7); the `<K/2` and `>=K/2` pair straddles p6-p7 with its "When:" orphaned. The p9 grid prints with **no number and no caption**, ten rows on p9 and three in `display` block 143 on p10, caption `Table.4-1` after both halves; its two confidence columns sum above 1 in eleven of thirteen rows. "positive ID is higher ... 84.6%" attaches the negative column's 11/13 to the positive side, which is 13/13. Fig.3-3 sums 15 and 2,286 against Fig.3-1's 11 and 68 (2,286 exceeds the whole 2,127-record set); Fig.4-2's circle is 13-15 km against the 30 km claim; Eq. 4-7's branches miss by 25 at d = 50.96; the outlier coordinate lost its leading 1. |
| 59 | P-C-2021-2107870-8021b684 | 4-16 (2-14) | 79 / 115 | done | **folio −2** - "Team 2107870" over "Page N of 23" (M = 23, 25 physical pages), 3,380 layout words over 79 units (42.8 per unit, 29.4 per block, median 22, 37 units under twenty words), the mean carried by two boxes (Algorithm 1 at 284 words, the keyword weighting at 259). **The record's `pages [7, 16]` excludes the chapter's own blocks**: units 1-14 print on PDF 4-5, which the folio calls pages 2-3, so the window opens three printed pages after the group list begins, and the shape matches the stored sample ("Stored count 12, coded 79") rather than the blocks. Only one heading is a `heading` block (163); `3 Image Classification` is welded to block 96, which belongs to `assumptions`. **No block is coded `display`**, so all nine displays sit inside prose blocks and only one is numbered, `(1)` on the Fisher equation, which prints the second spatial term as `d2N/dx2` twice and has lost its y-derivative. The chapter has no object captioned as a table: the nineteen-row k grid is captioned `Figure 2` and the Keras layer summary `Figure 4`, both stored as word runs. k = 17's accuracy 9/14 forces TN+FN = 5, the two probabilities two lines later are 7/12 and 5/12; c prints as 9.74 and as 30 km/year; the unification equation swaps lat and long, so its fifth case fires everywhere; Fig.5 and Fig.6 carry identical captions and neither orders its panels; Algorithm 1 numbers step 3 twice. |
| 60 | P-C-2021-2109298-1a718172 | 4-21 (4-21) | 103 / 114 | done | **folio 0** - "Team #2109298" over "Page N of 25" (M = 25), the chapter printing pp4-21 while the record window is [4, 20], so the field stops one page before its own end (units 102-103, blocks 181-182, print on p21 and block 182 carries the closing sentence and the `6 Further Improvements` heading). 4,755 layout words over 103 units (46.2 per unit, 41.7 per block, median 43, 24 units under twenty words, 14 under ten; 4,828 as stored, the 73-token gap being watermark runs). The chapter holds no heading for its own sections: `3 Data Exploration 3.1 Data` is the tail of block 29, which belongs to `assumptions`, so block 30 opens mid-section, and section 5's opening paragraph (121) is filed under `problem-analysis`, so `5 Identiﬁcation of Mistaken Classification` (120) is followed straight by `5.1` (126). Fifteen numbered displays, (1)-(15) with no break, every one inside a `body` block - the five `display` blocks hold panel labels and never equations - and `(13)` numbers a parameter list rather than an equation. The 2-D Gaussians `(2)` and `(11)` carry the 1-D normaliser `1/(√(2π)σ)`; `(5)` prints `N_cur(t) = N_cur(t) × r` at the same time index; `(13)`'s fitted curve tops out near 0.23 against Figure 17's 0-1400 counts. The grid fails on one axis: 45 cells of 12 km match the printed latitude band exactly, but 65 cells of 12 km need 780 km where the printed longitude band is 585 km. Figure 4 carries panel labels and nothing else - no caption, no number anywhere, and the prose cites it as "4a" - and panel-label blocks are stored in extraction order (Fig 2 as b, a, c, d; Fig 15 as a, d, c, b) against the printed a-b-c-d. The test window opens four months before training (2019-05-16 against 2019-09-19) and contains it whole. |
| 61 | P-C-2022-2200401-824b71b2 | 5-11 (6-12) | 6 / 23 | done | **folio −1** - "Team 2200401" flush left, "Page N" flush right, no `of M` (PDF 6 prints `Page 5`, PDF 12 prints `Page 11`), and the running head is clean on the page but swept into five block tails by the extraction (`Page 6` after Figure 1's caption in 66, `Page 9 5 Adaptive Periodic Grid Model` in 92, `Page 11 5.1.4 Results in ARIMA prediction` in 107). Six groups over 23 blocks, ids 63-69, 80-89, 90-92, 110-112; the two gaps are chapters - 70-79 is `Algorithm 1` under `algorithm`, 93-109 is the MA/ARIMA theory under `model-improvement`, and 109 also holds Figure 5's caption with the `5.2 APGM` heading that governs the chapter's last unit, so the chapter's one fitted model is filed under a section it does not open, two pages after the rest of it ends (unit 6 prints on p12, units 3-5 end on p10). 1,160 whitespace tokens over 6 units (193.3 per unit, 50.4 per block, median 192; the same blocks total 1,030 in the layout's `words` field), the mean carried by formula runs - unit 4 is seven blocks of which six are equations. **No block is `display`** and no equation carries a numeral: eight unnumbered displays, four of them split so a symbol (`l_0`, `num`, `log(1+r_0)`, `p̃_i^{t}`) lands in the preceding block. The isometric width prints as `(p_max − p_max)` twice, in-line as `l_0 = (p_max − p_max)/num_0` and displayed as `num_0 = (p_max − p_max)/l_0`, so the two definitions are circular and both evaluate to zero; `l_0`, "the minimum width of grid", is then set to `max{inf{g_1}, inf{g_num}}`, a maximum where the gaps require the smaller; `g_num`'s bound nests `1/(1/(1−α)^2 + r_0)` inside `1 − ·`; `α` is never defined and block 82 argues the opposite of the condition it appears in (`we have cannot make the width for every grid to be too small[12]`); the isometric grid-line formula divides by plain `num` while the count just derived is `num_0` and the input is `num_in`. The E.G. Coin toy closes 4×6+10 = 34, 34−28.72 = 5.43 and 5−1−2 = 2 coins but its closing valuation prints `5.43 + 5.26 + 2 × 7.48 = 25.95` where the summands give 25.65, and the text's 5-dollar crossing rule contradicts Figure 1's one-dollar grid; `0.731` against `0.595` is a profit ratio with no denominator, read off Figure 3 panels whose exchange axes run 2-12 and 0-50; Figure 2's panels are drawn on 1-7 and 1-8 axes; Figure 5 is pointed at from block 108 but its caption sits in block 109, outside the chapter; `ω = μ = 0.3`; the shift formula prints its time indices as literal braces. |

| 62 | P-C-2022-2200688-b6248fa6 | 5-9 (5-9) | 23 / 31 | done | **folio 0** - "Team 2200688" left, "Page N" right, no `of M`, swept into three block tails (`Page 7` in 58, `Page 8` in 65, `Page 9` in 73). 23 groups over blocks 43-73 with **no gaps**, the whole range: the assumption list (36-42) and the X-Prophet section (74-77) both print inside the page window and belong to other chapters, so the window's last page carries only a swept heading - block 73 stops on p9 right after `Page 9 4.1.3 Improvement Prophet - X-Prophet`, and the chapter ends mid-section. **No block is `heading` and none is `display`**; all five printed headings are block tails (48 `4 Model 4.1 Prediction Model`, 50 `4.1.1 Model Selection`, 53 `4.1.2 Prophet`, 73 `4.1.3`). 1,146 layout words over 23 units - 49.8 per unit, 37.0 per block, median 34, range 6 to 184, 1,276 whitespace tokens; 31 blocks carrying 16 equations, the densest chapter in the lane. Sixteen numbered displays (1)-(16), contiguous, every one in a `body` block, five separated from their own numeral ((3) with (2) in 58, (4)-(5) in the caption block 59, (6)'s numeral in 62 while its formula is in 61, (7)'s limits at the head of 64, (15) in 70). One figure (Figure 3, borrowed from [1], caption in 59) and one table (the ten-symbol notation table, blocks 43-48, uncited). Symbol reuse: `t` is the time index, the Laplace scale in (16) and the holidays prior scale in the table and in `k = Normal(0, t²)`; `k` is "the growth rate" in the table and (2)/(6) and an L-vector in (15) initialised with one scalar variance. (16) prints `exp(-|x-theta|/t)/2t` with no brackets, (13) prints a stray `*` where the summand's operator belongs, (6) is called segmented linear but is one straight line with a constant offset, and the transpose drifts between `z(t)'theta` in (2) and `z(t)theta`/`z(t)^T gamma` in (6). The notation table defines ten of the roughly twenty-five symbols used, omitting every symbol of the seasonal and holiday terms; the Fourier order drops 10 to 3 with no rule and the weekly case is introduced as "a weakly period". Figure 3's five box labels surface at the end of block 58 in scrambled order, the pointer sentence credits the figure with a "time series decomposition" it does not show, and the chapter's numbering starts at 3 because Figures 1-2 belong to earlier chapters while Figure 4 (the model's own X-Prophet flowchart) prints on p9 under `model-improvement` behind the broken pointer `The structure of X-Prophet is showed in4.`. |

| 63 | P-C-2022-2203120-59ecfcb7 | 5-10 (6-11) | 22 / 80 | done | **folio −1** - "Team # 2203120" left, "Page N of 23" right (PDF 6 prints `Page 5`, PDF 11 prints `Page 10`), no watermark or QR. **Window one printed page short**: block 142 spans PDF 10-11 and its glossary (W_j, m_j, A_j, λ, S_j, the three constraint readings and the C_1 note) prints on printed p10 with the `3.3` heading, outside `pages [6, 10]`. 22 groups over blocks 63-142 with no gaps; **no block is `heading` and none is `display`** - the two chapter headings `3.2` and `3.2.1` are welded to block 62 (owned by `data-preprocessing`), `3.2.2` to 113, `3.3` to 142. 1,474 layout words over 22 units - 67.0 per unit, 18.4 per block, median 57, range 5 to 174, 1,602 whitespace tokens; the last block alone carries 206 words of objective, five constraints, five-symbol glossary, three constraint readings and the next heading. Nine numbered displays (1)-(9), none in a `display` block, and the numbering separates from the formulas: (5) has `S_j = √…` in block 134 and its radicand in block 142 (eight blocks later), while the numerals (6)-(9) all sit in 142 above formulas stored in 135-141. Three figures (3, 4, 5) and three tables (2, 3, 4) inside the window and **zero `read-figure` jobs**. The decision coefficient (3) has lost its `1 −` (prints Σ(x−Y)²/Σ(y−Y)², glossed as "closer to 1 = better"), the white-noise p value near 0 is read as proof of white noise, the reading "gold level 2 ACF and level 1 PACF" would give ARIMA(1,1,2) while the text names ARIMA(2,1,1), and Figure 4(a) shows one ACF spike outside the band and at least four later PACF spikes, so neither panel truncates as reported. The trading model sells at `Y_g(i+1)` (next cycle's actual price), (6) and (7) define C_i and G_i from each other, (7)'s bitcoin branch reads `B_i = G_{i−1} + B_i × w_b × (1−α_b)` with B_i on both sides and the gold stock as its base, and (5)'s radicand compares `A_i` with the mean of 30 past `A_i`, so every summand is identical and S stops being a standard deviation. `j` carries cycle, day and look-back index in one subsection; λ is defined four blocks after the objective and never valued; the commission is stated as deducted from the amount paid but applied to the amount received in both branches. |

| 64 | P-C-2022-2204883-34c13ed1 | 4-14 (6-16) | 34 / 76 | done | **folio −2** - "Team # 2204883" left, "Page N of 23" right (PDF 6 prints `Page 4`, PDF 16 prints `Page 14`), no footer, watermark or QR tile on any page. 34 groups over blocks 88-163 with no gaps; **one `heading` block** (88, the `4.2` line) and **one `display` block** (116, Figure 4's panel letters). **The window ends on a page the chapter only reaches by a swept heading number**: block 163 spans PDF 15-16 for the sole purpose of carrying `4.3.3`, the chapter's prose stops on printed p13 at `...given by the model.`, and that heading's title and body (`4.3.3 The Result of Our Investment Strategy`) open `results` - one subsection heading split across two records; Figures 5 and 6 then print on the same page outside the field. Headings are swept onto tails throughout (`4.3 Investment Strategy Model Based on MLP` ends 118, `4.3.1 The MLP Model` ends 122, `4.3.2` ends 128 with its title opening 129, `4.3.3` ends 163) and the gate labels `i. Forget Gate` / `ii. Input Gate` / `iii. Output Gate` ride the tails of 91, 94, 99. 2,191 layout words over 34 units - 64.4 per unit, 28.8 per block, median 60.5, range 6 to 112, 2,807 whitespace tokens; four units are exactly 37 words (the four middle behaviours). Thirteen numbered displays (1)-(13), contiguous, none in a `display` block, plus at least fifteen unnumbered objects; (140)'s sentence ends printed p11 and its `min −P, R` display opens printed p12 under the header rule with no sentence above it. Four exhibits inside the field (Figures 2, 3, 4, Table 3 on printed pp4-7) and **one `read-figure` job**, which returns a verdict and no number. Five parameters are promised and three are scanned, and all three columns of Table 3 bottom out at `0.007261552` - the value at the initial combination, which is then adopted as the tuned setting. (10) is signed, so `min R` pays for selling; (11) multiplies the growth rate by the change in holdings, so an unwatched position earns nothing; the guard (13) drops the risk objective entirely; `model v-iv` repeats the endpoint of `model i-iv`; behaviours v/vi state `Δx_g = 0` and lose it from their `s.t.` rows. |

| 65 | P-C-2022-2212336-9ca07c5b | 5-10 (5-10) | 17 / 33 | done | **no folio at all** - printed pp5-10 carry no page number, no header, no footer, no watermark and no QR tile, so the record's `pages [5, 10]` is the only locator for anything in the chapter. **The chapter's blocks are not contiguous**: 53-76 then 87-95, because the whole `4.3`/`4.4` results section (blocks 77-86, 639 layout words, printed pp8-9) prints between the chapter's two halves under `results` - the field has two islands and the chapter's own page span contains another chapter's evidence. Kinds: 26 `body`, three `heading` (53 `4 Model I`, 54 `4.1`, 87 `5.1`) and four `display` (61, 70, 73, 95, all captions only); the other ten headings are block tails (`4.2` on 58, `4.2.1` on 62, `4.3.1` on 78, `4.3.3` on 82, `4.4` on 85, `5 Dynamic Programming...` on 86, `5.1.1` on 88, `5.1.2` on 91, `5.1.3` on 93, `5.2` on 95), so the same document files section headings two different ways. 963 layout words over 17 units - 56.6 per unit, 29.2 per block, median 58, range 5 to 145, 1,067 whitespace tokens; two units are over a hundred words and three are under twenty. **Two numbered displays for the whole chapter** - (1) at 57 and (2) at 64 - plus four LSTM gate equations (`f_t`, `C_t`, `o_t`, `h_t`) that exist only inside figure panels and are never numbered; (1) is shredded over blocks 55-58 and (2) over 63-68. Six flow charts inside the field and two `read-figure` jobs, neither of which returns a number. The named model is not the printed one: `ARIMA (p, d, q)` defines `d` as the number of differences and (2) has no difference operator, so the display is ARMA; the ARIMA+LSTM combination is never written as an equation, only drawn as arrows. `§5.1` declares dynamic programming across three subsections with no state variable, no transition, no value function and no equation; its flow chart decides on an `ROA` that no formula defines, subtracts a `cost` no section has introduced, has no sell branch, and loops `IF DAY<=1255` - five years of 251 gold trading days against 1,826 calendar days for bitcoin, leaving 571 days (31%) unaccounted. `Table 1` is used twice in the window (`Notations used in this paper` on p5, `Model performance evaluation table` on p9), and the chapter's own Step 3 figure is filed under `results` because its caption block carries the `4.3` heading. |
| 66 | P-C-2022-2218743-984f9ab2 | 6-15 (7-16) | 20 / 76 | done | **folio −1** - "Team # 2218743" left, "Page N of 23" right, header-only, printed = PDF − 1 (PDF 7 prints `Page 6 of 23`), so the record's `pages [7, 16]` is PDF numbering. **The cleanest field in the lane: 76 blocks, contiguous 61-136, no island** - and the most chaotic heading storage: 73 `body`, three `display` (69, 71, 80, panel labels only), **zero `heading`**, for a chapter nested four levels deep. Numbered titles are stored four ways: number and title together at a body tail (`4.1.3`, `4.2.3`, `4.3`, `4.4`, `4.4.3`, `4.4.4`); number at a tail with the title as the whole of the next block (`4.1.1`, `4.1.2`, `4.2.1`, `4.2.2`, `4.3.1`, `4.4.1`, `4.4.2`); number and title welded onto another chapter's **figure caption** (`4 Establishment andApplication of Investment Strategy Model 4.1 Predicting Asset Prices` on Figure 4's caption at 60, `4.2 Selecting Trading Dates Based on Market Conditions` on Figure 10's at 84); and title merged into its own first sentence (105). 3,060 layout words over 20 units - 153.0 per unit, 40.3 per block, median 145, range 10 to 445, flat-topped (eleven units between 83 and 203). **23 displayed equations, not one numbered**; the only numerals are `(1)`-`(4)`, the NSGA-II prose steps, and `1. / 2. / 3.`, the two objectives and the constraint bullet. Eight figure captions inside the field, two `read-figure` units, neither returning a value; no table anywhere in the chapter. Unit 17 (blocks 106-124, 445 words) builds weights, means, `C_t`, the portfolio CVaR, a four-row market-state brace and a three-row constraint system - and the market-state indicator `M_t`/`N_t` defined there is never used again: not in `eI_t`, not in the constraints, not in either CVaR. That brace also **inverts its own lead-in** - prose says trade when the market trends, the rows write `y_t = y_t` (holding unchanged) in the trending rows, and `y_t = y_t` is an identity, so no row can express a trade. `V = WᵀC⁻Wᵀ` prints (raster-confirmed); `eI_t` prices one trade at two prices, `(G_t − g_{t−1})y_t` against `−(y_t − y_{t−1})G_t`; `σ²⁻` is a single squared deviation while `σ²_{i,t}` is averaged over `t−2`; `d` is defined and then hard-wired as one printed differencing line; the residual pass rule (`p > 0.05`), its Figure 8 reading (`> 0.01`, "most" `> 0.05`) and its verdict ("all of which pass") disagree inside three sentences; `x_t, y_t, z_t` are never named as cash/gold/bitcoin. `0bjective` prints with a digit zero. Chapter closes on `4.4.4 Results Analysis` while the Figure 13 pointer, reading and caption (137-139) are owned by `results` - mirror of queue 64. |
| 67 | P-C-2022-2218931-a1aa7569 | 7-16 (7-16) | 26 / 113 | done | **folio offset 0** - "Team # 2218931" left, `Page N of 25` right, header rule only, nothing in the footer, no watermark or QR tile, so the record's `pages [7, 16]` is printed pp7-16 and the coded blocks occupy pp7-15. **113 blocks, contiguous 107-219, and every one of them `body`** - no `heading` kind, no `display` kind, in a chapter that prints seven numbered equations, two ruled algorithms and five figures; the printed hierarchy is 17.2 pt / 14.4 pt / 12 pt, so `4.1.3` is set at body size. **The chapter title survives in the text layer as `4 Qua`**: block 106 (the notation table's last row) ends `Long-term predicted price increase threshold for gold or bitcoin 4 Qua`, while the page prints `4 Quantitative Trading Decision Model` below the table's closing rule. 2,794 layout words over 26 units - 107.5 per unit, 24.7 per block (lowest in the lane), median 91, unit range 7 to 487, block range 5 to 126; 42 blocks print on p8, 40 on p14, 49 on p15 because every bullet and pseudocode line is its own block. **Seven numbered displays, (1)-(7), all flush right** - and every one belongs to the textbook half: (1)-(6) are the BP forward pass and the three update rules, (7) the Sharpe ratio; the two algorithms that carry the authors' own model contain no formula at all. (1) omits the input (`H_j = f(Σ_{i=1}^n W_ij + a_j)`) while (4) multiplies `x_i`; (2) sums over `i=1..n` with a `j`-indexed term where `Σ_{j=1}^L` is meant; `n` is the input count in the limits and the hidden width in step 1. (7) is a word fraction whose denominator fixes seven days for both assets against the five-day gold horizon used everywhere else. The Sharpe ratio is a `1`-threshold, a normalized weight and a cash share at once, with no risk-free rate in the chapter; `C` is cash and then "the amount of gold or bitcoin that can be bought today with cash held yesterday"; `0.99`/`0.98` print on every purchase with no gloss. Algorithm 2 tests `≥0.02 and ≥0.03` where the prose says "greater than 2% or ... greater than 3%", and buys on `if predicted gold is down or predicted BTC is down then Buy gold, BTC;` - the same signal its own selling stage sells on; it uses `Income`, `normalization` and `T_total`, none defined. `ν` is the damping scale in Algorithm 1 and "the error vector" in the gloss; `A` is called "Hessian matrix" though line 3 sets `A := J(x)ᵀJ(x)`; `τ`, `k_max`, `F`, `L`, `ϱ`, `h_{1m}`, `x₀` are never glossed. The novel half is outsourced: "we will not introduce too much mathematical knowledge involved in the algorithm" precedes 21 lines borrowed from K. Madsen et al. (2004), and the network is run through MATLAB's `Trainlm`. Validation is a random `70:15:15` split of a daily price series. Table 1's row for `f` is a dangling clause on the page ("An assumed functional relation which maps a parameter vector"). Block 167 welds `4.2` and `4.2.1` onto the p12 Figure 6 caption across the page break; Figure 7's caption is captured inside the p13 Sharpe paragraph; Figure 5's caption carries Figure 6's `(a)`/`(b)` labels. Four stages are announced, printed as `★` run-ins welded to the previous paragraph, and the selling stage is dismissed with "we will not go into details here". Chapter ends on Algorithm 2's `18 end`; the `$270836` sentence is block 220 under `results`. |
"| 68 | P-C-2022-2224507-b26b91d5 | 5-18 (5-18) | 28 / 132 | done | **no folio at all** - two readers scanned every one of pp5-18 and found no header, footer, rule, watermark or QR tile and no ink outside x 129-949 / y 141-1384, so the record's `pages [5, 18]` is the PDF index with no offset to recover; the document's only team identifier prints inside the p24 memo (`From:Team # 2224507`). "
"**132 blocks in two segments, 51-121 (70, block 53 removed) and 201-262 (62), with 79 blocks of another chapter between them** - 122-200 carry the RSI and MACD optimization results, Figure 8, `4.4 Optimal parameters and total assets` and Table 2, so the parameters the chapter's own model exists to produce are printed outside it, and the chapter resumes on p14 in the middle of 4.5.1, whose headings `4.5` and `4.5.1` are the tail of block 200 under `results`. All 132 are `body`: zero `heading`, zero `display`, and the whole 25-page document has exactly one `heading` block (block 2, the title). "
"3,299 layout words over 28 units - 117.8 per unit, 25.0 per block, median 120.5, unit range 35 to 312. **22 numbered displays inside the chapter, `(1)`-`(15)` and `(18)`-`(24)`**, with `(16)` and `(17)` printed on p13 inside the excluded range, so the chapter jumps from `(15)` to `(18)` with no note; not one display is stored as a `display` block, `(19)` alone spans 209-211. "
"The chapter is one template six times - DMA, RSI, MACD, TRIX, WR, BOLL each get a bold name, an expansion, a display, a gloss and a signal sentence - covering 945 of 3,299 words, and the seventh announced factor KDJ gets no section, no formula and no gloss but does get a Table 2 row carrying the RSI parameter triple `n = 2, I = 48, O = 65`. "
"`(1)` and `(7)`'s `MA_t` sum `i = 0..n` (n+1 terms) over `n`; `(7)` prints `MD_t = √(Σ (w_i MA_t)∗(w_i − MA_t)/n)`, a product where a squared deviation belongs; `(2)`'s `AMA = DMA/10` makes `(1)`'s own rule (`DMA > AMA → buy`) true iff `DMA > 0`; `(6)` prints `WMS = 100` at the cycle high while its sentence calls that "oversold ... a buy signal", inverting the polarity its RSI neighbour gets right. "
"`(8)`'s cash line adds cash on a buy (`+ (1−α)xB p`) and subtracts all cash on a sell (`− C_k q`), and `(10)`, its line-by-line restatement, swaps the two indicators (`+ (1−α)xB q − C_k p`), so the model and its gloss print opposite directions on consecutive pages; both read `B_{k+1}` into `C_{k+1}` while `(11)` reads `C_k` into `B_{k+1}`. The optimization declares no decision variables (`Z = max M_n` with `n`, `I`, `O` bounded by `1 ≤ n ≤ 100, 1 ≤ I < O ≤ 100` and never named as the choice), and `n` is at once the RSI window and the terminal day of `M_n`. `(15)` is announced with "the rest ... are the same as those described above, so we will not repeat them here" and then reprints the whole system under `gd`. "
"`(19)` sums `t` terms and divides by `t − 1` in all three lines, giving three formulas one numeral. `(20)` is `Min σ_t = √[(σ_t)²]` with no return term at all, subject to `0 ≤ H^btc + H^gd ≤ 1` and `H ≥ 0`, so the minimiser is the null portfolio; its covariance term silently switches from subscript `t` to `k`. `(16)`/`(17)` test only the signs of `DIF`/`DEA`, dropping the crossing the MACD prose requires, and are introduced as a change to "equation(7)", the Bollinger display. `(24)` is `(x_t − x_i)/x_i ∗ 100% < −20%` per asset while its gloss names an upright `x` and an upright `y` for a bitcoin pair and never glosses the gold pair. "
"Table 2 reports optimal parameters and five-year assets for seven factors when §4.3 models only RSI and MACD, and its MACD bitcoin yield `142.14%` contradicts the prose's `141.54%` for the same `$83,220` (the prose figure implies `$82,214`); its BOLL pair `$38,011` at `105.90%` implies `$37,007` (recomputed `107.0%`). Table 3, `Table of factor algorithms after parameter optimization`, prints no parameter value and no optimization: `DMA∗` adds the forecast `w′_{t+1}` to both sums with the same sign, so it cancels and the "optimized" index is `(1)` with both windows one term shorter. Figure 9's `Voters` box puts WR on Gold and BOLL on Bitcoin, the reverse of the paragraph's assignment. Figure 10's caption precedes any pointer sentence; Figure 12 prints at the foot of p18 but its caption and reading (`185.49%`, `0.51%`) are block 263 under `results`, and the baseline (`124,716.87`, `162.53%`) only appears in Table 4 on p19. The LSTM is three ungloosed gate lines with `μ` as the gate activation, `tan y(` for the tangent, `A′_t` and `A_t` for the two states, `F` without its subscript, and no citation anywhere. Disagreement: the record's note transcribes `(14)` as `1 <= I <= O <= 100` while the page prints `1 ≤ I < O ≤ 100`, and the note itself records `Stored count 27, coded 28, Delta +1`. |
"
"| 69 | P-C-2022-2229059-dacff43d | 8-11 (5-8) | 9 / 20 | done | **folio offset -3** - `Team # 2229059` left, `Page N of 21` right, one rule under the header and nothing in the footer, so the record's `pages [8, 11]` is printed pp5-8. "
"**20 blocks, contiguous 38-57, no island, and not one of the record's nine units has a heading to open on** - the document encodes **zero `heading` blocks in 147** (140 `body`, 7 `display`), and all seven `display` blocks are figure and table captions (35, 36, 59, 61, 64, 66, 70), none of them inside this chapter, so the nine printed subsections `3.1`-`3.9` exist only as text welded onto the tail of the previous subsection's last sentence. "
"1,270 layout words - 141.1 per unit, 63.5 per block, median 130, unit range 98 to 199, block range 6 (39 and 42) to 130 (55). **Eight displayed equations, and not one is numbered**: the brace for `M_t(n)` alone spans blocks 41-42, with `(difference between price and moving average)` stored as its own block. "
"`3.1` closes by issuing a sell signal on its own complement - "If both G_t(n) > 1 and P_t - A_t(n) > 1 then M_t(n) > 1 and a buy signal is issued ... Otherwise, a sell signal is issued" - while 3.4 calls its rule "simple and conservative" and requires `S > 0`, a profit test net of fees, so the two selling rules are irreconcilable and 3.8's daily procedure follows neither. "
"`M_t(n)` is defined as a two-case brace (`G_t(n)` **or** `P_t - A_t(n)`) and the next sentence requires "Both cases ... to be true", then asserts `M_t(n) > 1` without saying which value `M_t` took; the two thresholds are both `> 1` dollars on a price difference, so the filter is 1/1800 of gold and 1/10000 of bitcoin. "
"`S` divides the summed cost basis by the summation index (`S = (1 - f_a)·P - Σ_{i=0}^{n}(1 - f_{ai})C_i / i - L`) and the gloss rewrites it with the divisor corrected and three symbols changed (`f_g`, `C_n`, `/n`), so display and gloss disagree on every term; `S` also already contains the margin `L` it is then tested against. "
"`E = G_t(n) - C·(Σ_{i=0}^{n} G_t(i))/n` sums `G_t` over the window length instead of over time, so the "history of the model" is an average of n+1 window lengths and the 1,826-day series never enters; the sentence's number ("over 5 times") is in prose and the display's `C` is glossed only as "a scaling factor", then reused in 3.9 as a different "scalar constant". "
"`W = C·1/t^2` has no asset index, so it weights gold and bitcoin identically and cannot support "the bitcoin markers are considered much more heavily than the gold markers"; its `t` has no origin and no cap. The reversion criterion `∫_{μ-i}^{μ+i} P(x)dx > ∫_{μ-j}^{μ+j} P(x)dx for i > j > 0` is true of every non-negative `P`, defines neither the integrand nor `μ`, and reuses `i`, `j` from the summations. "
"Figure 3, the chapter's only exhibit, draws a rule the text does not state (below the moving average the flow chart buys unconditionally; the text requires two `> 1` thresholds conjunctively) and the chapter allocates it **no `read-figure` job**; 3.9 then justifies a cross-asset claim with `figure 2`, whose caption is `Bitcoin Price from 9/11/2016 to 9/10/2021` - one asset - where the two-asset chart is Figure 1. "
"`z` days, "a number of days", "a percentage of its maximum value" and `ΔP` are named and never valued, and they are the whole of the risk control. `3.8` opens "first check for 'no-buy' and extreme market conditions" and never routes the no-buy case anywhere; its extreme branch skips the rest of the program, so 3.5's release condition is tested by no line. `Daily Buy/Sell Order 3.8` is the one heading printed with its number after its title. "
"Block 57 spans pp11-12 and its tail is `4 The Model Results 4.1 General Result Figure 4: Our results.`, so the chapter ends carrying the next chapter's title, subsection number and figure caption. No record-vs-page disagreement found in this chapter: the nine groups align block for block and the note's quoted openings and closings match the page verbatim. |
"
"| 70 | P-C-2023-2300348-b8cdbed6 | 6-19 (5-18) | 41 / 61 | done | **folio offset -1** - `Team # 2300348` left, `Page N of 25` right, one rule under the header and nothing in the footer, so the record's `pages [6, 19]` is printed pp5-18. "
"**61 blocks in nine islands, with 30 blocks of the `results` chapter between them** - 50-69, 75-83, 88-91, 96-97, 101-107, 110-111, 113, 116-117, 124-138 - so two chapters alternate block by block across the same fourteen pages, and the captions of Figures 4, 6, 7, 8, 9 and of Tables 4, 5, 6, 7, 8, 9, 10, 11 are all outside the chapter, together with every number those exhibits produce (the deviation readings, `(2)`, Table 4, both correlation readings, both box-plot readings, and the `28 out of 30` / `93.33%` closing claim in blocks 139-140). "
"Kinds: 61 `body`, **zero `heading`, zero `display`** - the whole 26-page document has 191 blocks, 178 `body`, 7 `heading` (title x2, 75, 109, 141, 147, 191) and 6 `display` (all six are `(a)`/`(b)` panel labels) - and the chapter owns exactly one heading block (75, coded `route`) while printing seventeen. Four of its subsection headings are stored in another chapter's blocks: `5.3`/`5.3.1` in block 90, `5.3.2` in 95, `6.3` in 115, `7.4` in 139; `6.2` is `results`' standalone block 109. "
"2,558 layout words - 62.4 per unit, 41.9 per block, median 61 (unit median), unit range 8 to 136. **Ten numbered displays `(1)`-`(10)`, none stored as a `display` block**, `(1)` putting four lines under one number; jobs: 16 `define`, 9 `source`, 6 `compute`, 5 `route`, 4 `derive`, 1 `interpret`, and **no `read-figure`, no `compare`, no `check`, no `limit`, no `select`** in 41 units. "
"Table 11's `Sum` row is not a sum: it prints `6.51769% 23.30265% 30.29725%`, three cells lifted from Table 10, in a row whose own columns already sum to 360 and 100.0 one line above; its five percentages do not match its own counts (131/360 = 36.39% printed 36.2%, 152/360 = 42.22% printed 42.4%), and its `Valuable Percentage` column repeats `Percentage` in all five rows. "
"Two numbers are printed twice with different values: the Spearman coefficient is `-0.2956` in prose and `-0.3256` in Table 5's own row, and the forecast interval uses `2.01569%` where the sentence before it selected `2.1569%`. `δ` cannot be reproduced from the paper's inputs - `(8)` with `ω1 = ω2 = 0.5` and EERIE's Table 10 distribution gives `0.5·σ(4.0054) + 0.5·σ(2.40859) ≈ 0.9498`, not the reported `0.35916` - and `σ` carries three meanings (`Table 2`: the difficulty rate; `Table 3`: the sigmoid function; `(8)`: a multiplier on the weights, where the sentence says it normalises the data). "
"`(4)` is `fLetter = Σ_{1}^{5} f_{a,b,c...}` with a bare lower limit and no index; `(5)` is an arrow between two tuples; `(9)` and `(10)` give a distance and a residual with no minimisation, no centroid update and no convergence test, all three prose only; Table 10 has no column headers; Table 8 heads its third attribute `ref` while the prose uses `rep` five times. "
"Wrong references: `From Figure 3` for the deviation chart (Figure 4), `As shown in Table 2 below` for Table 4, `shown in Figure6(a) and Table3` and `shown in Figure6(b) and Table3` for Table 5, and `Section 4` for §5's score work three times. The word under test prints as `EERIE` in the `7.3` heading and `"ERRIE"` four lines below it. Disagreement: the record's note transcribes `(8)` as `δ = σω1 ∗ i ∗pi + σω2 ∗pX`, dropping the `Σ_{i=1}^{6}` and both limits that the page prints. |
"
"| 71 | P-C-2023-2301192-c71d36ff | 6-15 (5-15) | 10 / 76 | done | **folio offset 0, bare `Page N`** - `Team # 2301192` left, `Page N` right with **no total**, one rule under it, no footer, so printed = PDF and the record's `pages [6, 15]` is printed pp6-15; the chapter's own title block prints on p5, one page before its own range, and its last block on p15. "
"**76 blocks in six islands** - 55, 69-78, 88, 94-139, 144-151, 156-165 - with three other chapters woven in: `data-preprocessing` owns 56-68 (including `3.1`'s heading and the `3.2 Prophet Model` heading welded onto 68), `assumptions` owns 89-93, and `results` owns 79-87, 140-143 and 152-155. Kinds: 72 `body`, **4 `heading` (55, 144, 145, 156), zero `display`** - so of the chapter's thirteen printed headings, nine are the tail of somebody else's paragraph, including all four of `3.2`, `3.3`, `4.4` and `5`. "
"1,877 words of prose: 187.7 per unit, 24.7 per block, median 149, unit range 12 to 409, block range 4 to 119. The layout counts 1,891 because **seven blocks have the next page's running head welded on** (70, 76, 100, 120, 136, 147, 157), and 23 of the document's 236 blocks do. 53 of the 76 blocks are 19 words or shorter and 50 sit in a 6-19 word band: block boundaries follow printed line ends, so one paragraph in §3.4 is blocks 97/98/99 on one page. "
"**Eight numbered displays inside the chapter, `(1)`-`(4)` and `(6)`-`(9)`, none stored as a `display` block**, and no gap in the paper's twelve: `(5)` is the four-metric display on p8 where `MSE`, `RMSE`, `R²` and `MAPE` share one number, and `(12)` is the regression equation the chapter outsources to Appendix A. Jobs: 6 `define`, 2 `derive`, 1 `route`, 1 `source`, and **no `compute`, no `read-figure`, no `check`, no `compare`** in ten units. "
"§3.5.2 runs a real F test whose verdict sentence is in another chapter: `The F-statistic of the regression equation is 1.058 with a corresponding P-value of 0.379 (> α = 0.05), indicating that the regression equation does not exhibit statistical significance` is blocks 140-143 under `results` as `compare`, and no sentence anywhere in the chapter records what that verdict means for the six attributes the chapter has just built. "
"**Table 4 is on the wrong scale for the sentence that reads it**: the fitted series is the log transform (Figure 5 spans 9.5-12.8) and Table 4 prints `MSE 60340502`, `RMSE 7767.9149`, read as `the small RMSE and MSE can be considered`. `sqrt(60340502) = 7767.91` closes, so the table is internally consistent and externally wrong. The point forecast is also off-centre in its own interval: `14534` against `(13175, 16128)`, whose midpoint is 14,651.5. "
"**Table 6 and the paragraph under it disagree by 24%**: `MAE 3.2302` against `the mean absolute error (MAE) of the neural network is around 4`, with `MAPE 32.9194` glossed as `a high accuracy of the model`. **Table 7 and Figure 10 cannot be the same distribution**: identical caption `Predicted Result of "EERIE"`, the table's seven cells 0/6/18/29/27/15/5 summing to 100, the pie's six labels 23/32/22/6/4/12 summing to 99. "
"Attributes 5 and 6 are named and not defined - `5. the Sum of a Letter in a Word` gets one sentence with no formula and no source, `6. Part-of-Speech of a Word` gets three words and no content - and both enter the regression as regressors. Three assumptions print as `(1) (2) (3)` on p10, reusing the display-number glyphs of `(1)`-`(3)` on pp7-8. Table 3 lists five holidays, Figure 6's holiday panel shows three dips, one of them is read, and Easter is dated `2022/04/24`, the Orthodox date, where Western Easter 2022 was 2022/04/17. "
"Disagreement: the record gives this chapter `pages [6, 15]` while its title block 55 prints on p5; its note says `Stored count 8, coded 10, Delta +2`, and the 10 groups and their block membership match the page exactly - the two extra groups are §3.4's attribute paragraphs, which print one per attribute. "
"
"| 72 | P-C-2023-2307166-ec54f9ce | 7-17 (7-19) | 10 / 60 | done | **folio offset 1, `Page N of 24`** - `Team # 2307166` left, `Page N of 24` right, one rule under it, no footer, so printed = PDF − 1 and the chapter's text prints on printed pp6-18 while the record's `pages [7, 17]` starts on exactly the right leaf and stops two leaves short, omitting blocks 138-142 on PDF p19; p18 is a figure-only leaf whose only ink is the two captions welded into block 137, and p15 holds nothing of the chapter's (its eight blocks 116-123 are all `results`). "
"**60 blocks in four islands** - 55-68, 70-77, 84-110, 132-142 - with four other chapters woven in: `data-preprocessing` owns 69 and both of §3's opening headings (`3 Word Feature Engineering` and `3.1 Regularity` are welded onto its block 54), `notation` owns 78-79 which print as `4.2.1 Terminology`, `assumptions` owns 80-83 which print as `4.2.2 Assumptions`, and `results` owns 111-131 and 143 up, including §5, the `6 Predicting Score Distribution` heading welded onto 131, and §6.3. Kinds: 57 `body`, **3 `heading` (72, 73, 136), zero `display`** - eighteen headings print inside the coded pages and fifteen are welded, so the record's chapter boundary runs through §4.2 rather than between sections. "
"2,165 layout words: 216.5 per unit, 36.1 per block, median 182.5, unit range 120 to 374, block range 5 to 168. 31 of the 60 blocks are 19 words or shorter. No block in the range carries a running head welded into its text, so the layout's count and the page's count agree. Unit 7 is twenty blocks for 242 words because each of the four variables and four parameters is cut at the printed line - `Variable C(rowd) normal TPers who will get bored quickly; a fraction of them will be-` / `come the Quitted or the Loyal everyday.` "
"**Twelve displayed equations, none numbered, none stored as a `display` block.** The only parenthesised numbers in the chapter are `Covariance Matrix(1)` and `Covariance Matrix(2)`, welded panel labels on Figures 8 and 9, and nothing in the chapter ever cites an equation by number. Jobs: 4 `derive`, 2 `source`, 2 `compute`, 1 `define`, 1 `interpret`, and **no `read-figure`, no `check`, no `compare`, no `select`, no `limit`, no `mechanism`, no `handoff`** - eight figures print and no unit reads one. "
"**The SIR review's infection term has the wrong sign**: `dI(t)/dt = −β × S(t) × I(t)/N − γ × I(t)` on p12, where the PCQL model four blocks later writes the same flow as `+βP(t)(C(t)+L(t))/N`, so under the printed sign the infected compartment can only decay; and `A basic SIR Model consists of a system of four differential equations[3]:` is followed by three. **The record's note repeats the miscount**: it says group 6 (84-87) carries `the four differential equations`, but group 6 carries the three SIR equations and the four PCQL ones are in group 7 (88-107). "
"`Pur`'s summation has no index (`Σ_{j=1}^{n}` over a summand indexing only `i` and `i+1`, so every term is the same number), and the word-level sum then nests one sum inside another: `w_i = Σ_{j=1}^{n} Pur(c_{i,j})` sums over `j` a quantity that already sums over `j`, re-indexes `c_i` as `c_{i,j}`, and redeclares neither `i` nor `j` between the two displays. The standardisation formula prints a stray prime, `x*_ij = (x_ij − x̄)/sd(X_j)′`, with the numerator's mean unindexed against a denominator indexed by `j`. "
"**The fit prints its starting guess and never its answer.** `the initial parameters obtained by the genetic algorithm are shown in the following table` gives `1.77e-01 1.77e-02 1.04e-03 1.14e-03`, the Nelder-Mead refined values are never printed, no goodness of fit is given, and the `Mean 2.5% 97.5%` table beside it puts the bootstrap point estimate in a header slot as if it were a third quantile. Both tables are uncaptioned, as are the `2.3 Data Cleaning` table on p7, the EERIE attribute strip and the predicted-tries row on p20 - five uncaptioned tables in the paper against four captioned ones (`Table 5`-`Table 8`, pp15-16, all in `results`). "
"**`performs best at K=15` is not what Figure 10 plots**: the six cross-validation curves fall from about 17.5 and drift down through K=50 to a floor near 12.4, so the argmin sits at the right edge while a dashed rule marks K≈15; the legend is written `Both!Hard`, `UnW&Hard`, `W&Hard` and the `*:` note decodes `&`, `!`, `UnW` and `W` but never `Both` or `Hard`, with no asterisk on the page. **A sentence is severed by a whole figure-only page**: block 137 ends `so we need to conduct` on p17, p18 is ten tokens of captions, and block 138 resumes on p19 `further in these five variables filtering.` "
"Adjacent exhibits that the chapter never checks: Table 7 prints `***` beside `Pr(>|t|) 0.869`, the paragraph under Tables 5-6 reads the unweighted coefficient as `-0.01` where Table 6 prints `-0.148223` and gives its R² as 0.013 and `about 2%` and `about 1.2%` in one sentence, `5 Is Word Itself affect Hard Mode Ratio` prints as a `results` heading, and Figure 11's `the error range of the model is small` sits against visibly wide intervals on the two tallest bars. "
"Disagreement: the record gives the chapter `pages [7, 17]` while its blocks print to p19, and the record note's `Stored count 8, coded 10, Delta +2` is otherwise exact - all ten group boundaries and every opening and closing clause in the note match the page. "
"
"| 73 | P-C-2023-2307946-61b646ed | 5-21 (5-21) | 10 / 96 | done | **folio offset 1, `Page N of 25`** - `Team # 2307946` left, `Page N of 25` right under a single rule, no footer on any page, so printed = PDF − 1 and the record's `pages [5, 21]` is printed pp4-20; the chapter's first block prints on p5 and its last tail on p21, but **p7 and p15 hold nothing of the chapter's** (p7 closes `data-preprocessing` with Figure 4 and Table 2, p15 is `results` with Figure 10 and Figure 11), so the range is right at both ends and wrong in the middle. "
"**96 blocks in six islands** - 44; 62-79; 81-121; 128-141; 143-147; 152-168 - because `notation`, `data-preprocessing` and `results` are woven through it: 45-61 is `notation`/`data-preprocessing` (the notation table, §3.2, Figure 4, Table 2), 80 is a single `results` block carrying both `5 Extraction and Analyse Attributes of the Word` and `5.1`, 122-127 is `results` (Table 4, Figures 10-11, the `7 Model III` heading), 142 is one `results` block carrying `7.3 Model Refinement 7.3.1 Data Augmentation`, 148-151 is `results` (Table 5 and the `8 Model IV` heading) and 169-176 is `results`. Kinds: 93 `body`, **3 `heading` (62, 107, 108), zero `display`** - twenty-six headings print inside the coded span and **twenty-three are welded onto a paragraph tail**. "
"3,398 layout words: 339.8 per unit, 35.4 per block, median unit 296, unit range 17 to 697, block range 3 (`6.1 Introduction of LightGBM`) to 137 (block 85). 43 of the 96 blocks are 19 words or shorter. No block carries a printed `Page N` string and no page has a footer, so layout words are page words; unit 5 is 26 blocks for 697 words because the attribute list runs one attribute per printed line. "
"**Nine numbered displays, `(1)` to `(9)`; the chapter owns `(2)` to `(8)`** - `(2)` ARIMA(p,d,q) in block 73, `(3)` the lag vector in 117, `(4)` min-max in 118, `(5)`-`(8)` the k-means assign/update/criterion/convergence loop in 160-164; `(1)` is the ±3 sd outlier rule in `data-preprocessing` block 56 and `(9)` the average-tries sum in `results` block 169. Every tag is welded onto the last line of the prose, so `(3)` prints as the tail of a 6-word block that is only a variable list, `pctt−1, · · · , pctt−5; Xt, · · · , Xt−5 (3)`, with no left-hand side and no operator. Jobs: 3 `derive`, 3 `source`, 3 `define`, 1 `route`, and **no `read-figure` at all** - the chapter prints eleven exhibits, reads six of them inside other units and never gives one a unit of its own. "
"**The chapter's own evaluation is in another chapter.** §6.3 ends on the colon `the calculation results of each indicator within the training set and validation set are as follows:` and Table 4 is a `results` block, so the model that takes 321 words to design is scored outside the chapter; §7.3.1's data augmentation and all of §8.3-8.5 are `results` too, so no model in this chapter is ever evaluated inside it. **The failed augmentation is contradicted four blocks later**: `the above two models were retrained. However, ... did not improve significantly` against `Luckily, the results have been significantly improved.` "
"**`the ratio of training set : test set = 4 : 1` but Table 4 reports `Training set` and `validation set`** - a test set is declared and never scored, a validation set is scored and never in the ratio. **A second `Figure 1` caption prints on p17 above `Figure 13`** for the same graphic, restarting the figure numbering, and it has no block of its own, so the record drops it. **Table 3's footnotes 2 and 3 are the same sentence** (`This statistic excludes homophones`) under two different attributes, the superscript markers are lifted mid-cell in blocks 95 and 97, and footnote 5 ends the unit alone as `5 % of films containing the word`. "
"**Figure 9's `white and black dots` do not exist on the page** (dark grey and light green nodes, pale blue arrows), **Figure 5 has no smooth line** although `Made a scatter plot with a t smooth line` says it does and the clause has no subject, and **Figure 14 has no elbow at k=4** while the text argues one there. **`The resulting significant test statistic is -1.9608 while the p-value is 0.5934, which cannot reject the null hypothesis`** calls an insignificant statistic significant in its own sentence. "
"Disagreement: the record note `Stored count 10, coded 10, Delta 0` is exact - all ten group boundaries and every opening and closing clause in the note match the page - but the page range contains two leaves that belong entirely to other chapters. "
"
"| 74 | P-C-2023-2309397-285a4e67 | 5-22 (5-22) | 12 / 81 | done | **folio offset 0, `Page N of 25`** - `Team # 2309397` left, `Page N of 25` right under a thin rule, no footer, so printed = PDF and the record's `pages [5, 22]` is printed pp5-22; the chapter opens mid-page on §3.2's heading at about 46% of p5 (behind `3`, `3.1` and Table 2) and closes on block 178 at the foot of p22, where `8` and `8.1` print with no body under them, so the range is exact at both ends and its last leaf ends on a heading rather than a paragraph. "
"**81 blocks in seven islands** - 54-72 (19), 76-79 (4), 83-85 (3), 88-102 (15), 111-128 (18), 149-162 (14), 171-178 (8) - because four other chapters are woven through it: 53 closes `data-preprocessing` on p5; 73-75, 80-82, 86-87, 103-110 and 163-170 are `results`; 129-140 are `sensitivity-analysis` and 141-148 `error-analysis`. Kinds: 72 `body`, **5 `heading` (54, 88, 100, 149, 171), 4 `display` (61, 91, 112, 123)** - and all four `display` blocks are figure captions, so not one display *equation* is extracted for the eight numbered and twenty-odd unnumbered formulas the chapter prints. Sixteen numbered headings print inside the span and twelve are welded; block 88 is a heading block whose whole text is the fragment `Based on Multiple Linear Regression Model`, the second line of §4's title, whose first line prints on `results` block 87. "
"3,462 layout words: 288.5 per unit, 42.7 per block, median unit 224.5, unit range 89 to 663, block range 5 (block 61, Figure 4's caption) to 205 (block 57, the Phase 1 bullet with Figure 3's caption welded into it). 27 of the 81 blocks are 19 words or shorter. No block carries a printed `Page N` string and no page has a footer. **p12, p16 and p17 hold nothing of the chapter's** (p12 is §4.4 with Figure 10 and Tables 4-5, p16 the two sensitivity figures, p17 §5.4). "
"**Eight numbered displays, `(1)` to `(8)`, contiguous, seven inside the chapter; `(6)` is p17's uncertainty width and belongs to `sensitivity-analysis`.** Every tag is welded to the end of a body block, and the tags go to the cheap displays while the paper's central formulas go unnumbered - the ARIMA brace system, both weighting equations, the sample standard deviation, the general regression and its fitted `Ŷ`, the five-line spherical-coordinate block, the four p19 indicator formulas, the GMM density and its EM pair, and Sup/Conf/Lift. Jobs: 5 `derive`, 3 `define`, 2 `source`, 1 `interpret`, 1 `select`, and **no `read-figure`** - seven exhibits are captioned inside the chapter and none gets a unit of its own. "
"**The boundary hands away most of the paper's own evaluation**: §3.2.6 and §3.3 (73-87), §4.4 (103-110), §5.3 and §5.4 (129-148), §6.3 and §7.1 (163-170) all print as other chapters, and §4.3 is cut in half - its heading is in-chapter while Figure 10, Table 4, the regression equation and the fitted `Ŷ` are `results` blocks, so the chapter resumes at `4.4 Results Analysis`. **`Figure 11` is captioned and never cited**: the string occurs in exactly one block, its own caption. "
"**The word count prints two ways**: `356` four times in prose against 357 in Figure 9's caption, equation (3)'s index, Figure 10's ring counts and all three §5.4 summations. **`about 13% of the players could guess the word in 2 trys` contradicts Table 6's `11%`**, the only value that lets the row reach 100. **Figure 14's prose inverts the plot**: `more consistent across words when NF is 0.2 and above` over bands that widen monotonically. MAE is called a `weighted average` over an unweighted formula, R² is given the range `[0,1]` against a formula unbounded below, and the whole regression is declared significant at the 10% level in the paper's own words. "
"**The "dummy coding" is single-column label coding** (`X1 = {1 noun, 2 verb, 3 adjective, 4 others}`); one distance prints as `M' distance` and `Marxist distance`; the EM covariance line puts the subscript outside the sigma (`∑，j =`) and carries `μ_i` where `μ_j` is required; Table 10 announces `Sup of 0.5` and `Lift greater than 1` and prints only `Conf`; the ROC/RDC column is misnamed in the reading sentence; and the difficulty levels print as `IIII` and `IIIIII`. "
"Disagreement: the record note `Stored count 12, coded 12, Delta 0` is exact - all twelve group boundaries and every opening and closing clause match the page - but the layout welds both p21 captions into block 167 in reverse order (`Figure 16 ... Figure 15 ...`). "
"
"| 75 | P-C-2023-2310767-2f955db2 | 5-8 (5-8) | 12 / 27 | done | **folio offset 0, `Page N of 25`** - `Team # 2310767` left, `Page N of 25` right under a single rule, no footer, so printed = PDF and the record's `pages [5, 8]` is printed pp5-8. **The field is one island**: blocks 62-88 with no gap, the first chapter in this lane where neither neighbour pierces it - blocks 60-61 close `data-preprocessing` on p5 with the two data filters, block 89 opens `problem-analysis` on p8 with the COCA paragraph the vocabulary index needs. The chapter opens mid-p5 behind those two bullets and closes mid-p8 one block before COCA, so both range ends are shared pages. Kinds: 23 `body`, **2 `heading` (62, 63), 2 `display` (70, 73)**. "
"**Seven numbered headings print inside the span and only two own a block**: `4` and `4.1` are clean `heading` blocks, `4.1.1` is split across two body blocks (64 is the bare number with 0 words, 65 the title), and four are tails - `4.1.2` closes 66, `4.1.3` closes 79, `4.1.4` closes 82, `4.2` closes 84. **Three figures print and only two have a block**: Figure 4's raster sits at the head of p8 while its caption is the tail of body block 83 whose prose ends on p7, so the chapter's own headline exhibit is invisible to a `kind == display` count. "
"1,358 layout words: 113.2 per unit, 50.3 per block, median unit 112.5, unit range 44 to 189, block median 44, block range 0 (block 64, the bare `4.1.1`) to 159 (block 82, the five-item hybrid). Nine of the 27 blocks are 19 words or shorter and three of those nine are headings wearing body labels. **Three numbered displays, `(1)` and `(2)` welded into block 75 and `(3)` into block 77, and not one equation is a `display` block** - a chapter that prints the ARIMA pair, the Ljung-Box statistic and three figures extracts zero display equations, and the LSTM gates, the phase-space reconstruction and the combination step print as prose only. Jobs: 3 `derive`, 3 `define`, 1 each of `route`, `check`, `interpret`, `select`, `compute` - and **no `read-figure`** although three units read a figure. "
"**Three quantitative gates, no printed statistic**: the unit-root test is `we performed a unit root test` with no test named, the BIC order search is `calculated by computer programming loops` with no value in the chapter and no table anywhere in it, and the Ljung-Box verdict prints as `it is not white noise` with no `Q(m)`, no `m` and no p-value - the gate that licenses the whole ARIMA-LSTM handoff cannot be re-run from the page. Equally the embedding order appears as `the optimal number of reports is finally determined as 18`, a parameter wearing the name of a data quantity. The forecast itself is one line: `22577, with a prediction interval of [9614,43109]`, dated `March 1, 2023` on a figure whose x-axis runs 0-450 with no dates and no coverage level. "
"**The chapter reads its own Figure 2 against the caption**: the prose calls the two panels `the two time series` with `autocorrelation coefficients decay relatively slowly`, the caption calls them ACF and PACF plots, panel (b) is already the differenced series `r̄_t` whose definition arrives on the next page, and that subplot's x-axis carries the label `Partial Autocorrelation`. Figures 2 and 3 are cited as `figure2` and `figure3`, lowercase and unspaced. Frame overlap: `the residual part of this result is not well predicted reasonably well`; the ARIMA output is `not very volatile` and the combined output is praised as `more volatile and more realistic`. "
"Disagreement: the record note `Stored count 12, coded 12, Delta 0` is exact - all twelve group boundaries and every opening and closing clause match the page - and the one coding artefact is that no job is `read-figure` while three units read one. "
"
"
"| 76 | P-C-2023-2311035-1b2bc274 | 7-11 (6-10) | 12 / 36 | done | **folio offset −1, `Page N of 22`** - `Team # 2311035` left, `Page N of 22` right under a single rule, no footer, so printed = PDF − 1 and the record's `pages [7, 11]` is printed pp6-10. **One island**: blocks 58-93 with no gap, five pages all carrying chapter blocks (p7 58-62, p8 63-66, p9 67-71, p10 72-79, p11 80-93). Both range ends are mid-page and both neighbours print on the same leaves: block 57 is the last row of `notation`'s Table 1 (`Ew`) and carries `4 Task 1: Fundamental Model for Predicting Results 4.1 Data Cleaning` as its tail, so **the chapter's own title is not inside the chapter**, and block 94 is `results`, which opens with the tail-welded `5 Task 2: Model for Predicting Percentage Distribution`. The first coded block (58) is therefore 4.1's first sentence. Kinds: **35 `body`, 1 `display` (75), 0 `heading`**. "
"**Eight numbered headings print inside the span and none owns a `heading` block**: `4` and `4.1` close block 57 (outside the chapter), `4.2 Formulating the Model` closes 59, `4.2.1` closes 61 with its title `Long-term and Short-term Memory` alone in 62, `4.2.2 Data Normalization` closes 69, `4.2.3 Implementation of LSTM` closes 71, `4.2.4` closes 76 with `Prediction Interval from the Result` alone in 77, `4.3 Correlation between Hard-mode Percentage and Words` closes 79. A consumer keyed on `kind == heading` sees a chapter with no sections at all. "
"**The chapter's only `display` block holds neither a caption nor a formula**: block 75 is Figure 8's two panel labels. All six figure captions are typed `body` (61, 68, 91 stand alone; 63, 71, 76 are welded onto prose tails), so a `kind == display` count returns one exhibit against six printing figures and two tables. Table 1, which defines the `Ct`/`ht`/`it`/`wt` the chapter uses, is outside the chapter in blocks 50-57 and is never cited inside it; Table 2 sits in block 59, one block after the sentence that cites it, and one of its six rows corrects nothing (`favor (with space) → favor`). "
"1,014 layout words: 84.5 per unit, 28.2 per block, median unit 81.5, unit range 24 to 144, block median 14.5, block range 5 to 126 (block 70, the normalization argument). Twenty-two of the 36 blocks are 19 words or shorter: the four attribute bullets are torn one clause per block (81-83, 84, 85-86, 87-89) and four caption blocks stand nearly bare. **Two numbered displays, and `(1)` is split across two blocks** - the numeral closes block 64 (`and the formula is: (1)`) while `Ct = ft ∗Ct−1 + it ∗˜Ct` is the whole of block 65 - `(2)` is welded inside 78. **Three displayed formulas print inside pictures and carry no number at all**: the forget gate `ft = σ (Wf ·[ht−1, xt] + bf )` beside Figure 5, the output pair `ot = σ (Wo [ht−1, xt] + bo)` and `ht = ot ∗tanh (Ct)` beside Figure 6, and the regression `Ratio = β0 + β1 ∗f reqrankscale + β2 ∗ Head + β3 ∗ Continuous + β4 ∗ Letterf req + cons` inside the Figure 9 screenshot; none of `σ`, `tanh`, `β`, `factor` appears anywhere in the chapter's text layer, so those symbols exist only as raster. **No job is `read-figure`** although six units cite a figure and both tables are read. "
"**The arithmetic fails three times on its own printed numbers.** `21, 843.73 ± 1.96 × 560.21` is 1,098.01, so the interval is `[20745.72, 22941.74]`; the lower bound prints exactly that and the upper prints `22914.74` - the same digits transposed, off by 27. `39813 −27502 = 12311` is 30.9% of 39,813, not the `ratio of change is only 3.4%` claimed, and the denominator that would produce 3.4% (about 362,000, roughly Figure 8(b)'s y-axis top) is never printed - yet the whole normalization design rests on it. And the significance verdict compares against a table value instead of the software's own output: `The F-statistics is 1.69, less than 2.397 (α = 0.05)` sits beside the screenshot's `Prob > F = 0.1519`, then claims `the conclusions are the same if we turn to analyze those four t-statistics` while the same screenshot shows `Head  t = 2.47  P>|t| = 0.014` - significant at 5%, in the sentence that denies it; the model line also lists `cons` as a regressor. "
"**Blocks 92-93 store the verdict's sentence out of order**: 92 is `Therefore, words will not aﬀect the` and 93 opens `The F-statistics is 1.69, less than 2.397 (α = 0.05). percentage of scores reported in Hard Mode at 5% signiﬁcance level.`, so the evidence prints before the claim it supports and the claim's head and tail are split around it. Smaller state of the text layer: `ouput` twice (67, 69), `actication` (69), the one attribute named three ways across bullet label, prose and formula (`Consecutive letters` / `serial letters` / `Continuous`), a period inside five figure references (`Table.2`, `Figure.4`, `Figure.5`, `Figure.6`, `Figure.8`, `Figure.9`), `The LSTM model created in 4.2.2` for the model §4.2.3 builds, `the gamma distribution, which includes the natural constant term`, and Figure 8(a)'s x-axis labelled `Predicted number of reported results in 1/8/2023` against a caption and text that both say March 1st. "
"Disagreement: none in the boundaries - `Stored count 12, coded 12, Delta 0` is exact, all twelve group boundaries and every opening and closing clause match the page, and 36 blocks for 12 units is honest (the bullets and captions were cut). What the record cannot show is that the chapter is bookended by two other chapters' blocks, that no job reads a figure, and that its two gate formulas have no text-layer existence. "
"
"| 77 | P-C-2023-2311717-64b80c37 | 6-14 (6-14) | 25 / 102 | done | **folio offset 0, `Page N of 25`** - `Team # 2311717` left, `Page N of 25` right under a single rule, no footer, so the record's `pages [6, 14]` is printed pp6-14. **One island**: blocks 61-162 with no gap, and every page in the span carries chapter blocks (p6 1, p7 10, p8 13, p9 20, p10 8, p11 8, p12 28, p13 4, p14 4). The chapter is bookended by other chapters at both ends: block 60 (`data-preprocessing`) is Figure 2's caption **carrying the chapter's own title** (`Figure 2: Data pre-processing 5 Task 1: Report Number Prediction Model & Game Mode Selection Analysis`), and block 162's tail carries `6 Task 2: ...`, so both the start and the finish sit on a shared page. Kinds: **99 `body`, 1 `display` (62), 2 `heading` (63, 64)** - and all three non-body blocks are debris: 62 is the data-source footnote plus a watermark character, 63 and 64 are 0-word watermark fragments. "
"**Seven numbered headings print inside the span and none is a `heading` block**: `5.1 Data Exploration` closes block 65, which is the *continuation* of block 61's sentence begun on p6, so the chapter's first paragraph is torn at the page break with the heading after its second half; `5.2` closes 73; `5.2.1 The establishment of report number prediction model` is a 7-word body block alone (74) and `5.2.2 Establishing prediction intervals for future reported number results` an 8-word one (111); `5.3 Analysis of Game Mode Selection` **and** `5.3.1 Analysis of word attributes` share block 120's tail - two headings in one block; `5.3.2 ...` closes 151. "
"**Six numbered displays, one unnumbered, and only the numerals are in the text layer.** `(1)` inside 79, `(2)` inside 83, `(3)` inside 89, `(4)` and `(5)` both inside **107**, which stores the p9 tail and the p10 lead-in as one block so the page break falls inside it, `(6)` twice inside 110. The estimator `Ĝ(t; θ̂)` between 81 and 82 carries no number. Every formula is gone, so the glosses read as holes: `where the meaning of is the mean value of the number of reports on the day .`, `, with being the number of reports and being constants.`, `based on , as shown in equation (6)`. Block 159 serialises Figure 8(a)'s tick labels into prose (`14 Percentage of Hard Mode Results 12 50 12 10 10 100 8 150 Date 6 200 ...`). "
"2,881 layout words: 115.2 per unit, 28.2 per block, median unit 93, unit range **11 to 428**, block median 16, block range 0 (63, 64) to 158 (66). Sixty-two of the 102 blocks are 19 words or shorter (the seven attribute bullets are torn three to four blocks each). The word budget is lopsided in a way the record cannot show: unit 21 alone is 428 words (14.9%) for seven bullets of identical shape, while the entire modelling core S7-S15 - trend, Poisson, correction, interval - is 655 words, 190 of which go on the three popularity periods. Jobs: 6 `define`, 6 `derive`, **4 `read-figure`**, 3 `compute`, 2 `interpret`, 1 each of `limit`, `select`, `mechanism`, `compare` - and **no `check`**, in a chapter that prints an RMSE, an R² and two interval tables. "
"**The arithmetic fails where it matters.** Table 2 prints nine coefficients (`A1 1.57e+05`, `A2 9.69e+04`, `A3 4.846e+04`, `B1 33.01`, `B2 48.2`, `B3 5.864`, `C1 30.79`, `C2 75.31`, `C3 386.7`) while the parameter vector that glosses equation (1) as `θ = [A1, A2, A3, B1 ...C1, C2, C3]` prints eight slots, eliding `B2` and `B3`. The 75% interval `[7654, 20154]` is ±6,250 around a Poisson mean of 13,904 - standard deviation 118, so ±53σ - and cannot be a quantile of the `P̂k(t)` it is derived from; the 85% row `[5434, 23657]` has gaps of 8,470 and 9,753, so one level gives an exactly symmetric interval and the other an asymmetric one for the same rule; and (6)'s rule puts `β/2` inside the argmin, i.e. 37.5% one-sided mass where a two-sided 75% interval needs 12.5%. The correction is self-referential: `λ̇k(t) = λ(t) · f(k)` with `k` the number of reports, and `Ṗk(t) = λ̇k(t)^k / k! · e^{−λ̇k(t)}` then evaluates the intensity at the count it is meant to generate. Two prose claims die on their own table - `high percentages ... in the last three months of 2022` against `2022/9/16 parer 11.07%` in the top ten, `the first month of 2022` against `2022/2/13 robin 1.17%` in the bottom ten - and the attribute formulas double-normalise (`the percentage of words with the first letter "h" is p_h1/359`). "
"Disagreement: none - `Stored count 25, coded 25, Delta 0` is exact, and the record is explicit that (4) and (5) share a block, which is the p9/p10 merge in 107. The record's own two `define` units book a printed heading (`5.2.1`, a 7-word block) and a bullet list (125-151) as prose segments. "
"
"| 78 | P-C-2023-2314151-c97576e4 | 8-13 (7-12) | 16 / 74 | done | **folio offset −1, `Page N of 24`** - `Team # 2314151` left, `Page N of 24` right plus a centered footer number, so printed = PDF − 1 (PDF p8 reads `Page 7 of 24`). **One island**: blocks 73-146 with no gap across six leaves (PDF p8 21, p9 18, p10 11, p11 13, p12 15, p13 1). **The record's `pages [7, 11]` cannot hold its own blocks**: the first coded block (73) is on PDF p8 and fifteen of the record's blocks print on PDF pp12-13, so the range is one page long at the head and two short at the tail. Kinds: **72 `body`, 1 `display` (113), 1 `heading` (117)** - the sparsest coding in this lane, and the single real heading block belongs to `4.2`, while **the chapter's own `4 Task 1`, `4.1 Prophet algorithm` and `4.1.1 Background of the algorithm` are the tail of block 72**, a `data-preprocessing` block that is Table 5's grid. "
"1,496 layout words: 93.5 per unit, 20.2 per block, median unit 89.5, unit range 26 to 247, block median 15, block range 0 (block 118, the bare `4.2.1`) to 112 (block 125). Fifty-six of the 74 blocks are 19 words or shorter - the decomposition is glossed one symbol per block (78-82), Table 7 is torn one row per block (121-124), Table 8 into five blocks of names (134-138). **Nine numbered displays print and only four tags survive in the text layer**: `(2)` in 77, `(4)` in 93 - one block after its own expression, which sits untagged in 92 - `(6)` in 99, `(9)` in 130; `(1)` is not in the chapter at all (numbering opens at (2)) and `(3)`, `(5)`, `(7)`, `(8)` appear nowhere. Ten numbered headings print and eight of them are body blocks or tails (`4.1.2` closes 74, `4.1.3` closes 108, `4.1.4` closes 110, `4.2.1` alone in 118 with its title alone in 119, `4.2.2` inside 125, `4.2.3` closes 132). Jobs: 5 `derive`, 3 `compute`, 2 `compare`, 1 each of `limit`, `select`, `define`, `read-figure`, `check` - **no `interpret`**, although S16 exists only to interpret Table 9. "
"**Two models with no bridge**: S1-S12 (Prophet, 835 words, twelve units of which five derive the algorithm) and S13-S16 (partial correlation, 661 words, four units) share no variable, no dataset and no transition sentence - S13 opens straight on a heading. The only candidate bridge is S12's last sentence, `it predicts the report number interval for seventy days after January 1, 2023` - about March 12 - while Table 6 predicts `March 1, 2023`. "
"**The arithmetic, and the stat that collapses.** Table 6 prints `2023-03-01 | 14425.58926 | 10355.27753 | 18741.54302`; the prose quotes only `a range of 10355 to 18742` and **never states the point forecast** 14,425.59, and the interval's level is never named - only implied three pages earlier by `interval width to 0.80`. Then the Pearson screen refutes its own sentence: block 125 says `only the total ranking of word frequency of letters in words is strongly correlated`, while that row of Table 7 is `The sum of the frequencies of letters | 0.008176597 | 0.869535404`, the smallest R and largest P in the table - no correlation by the chapter's own bands, p = 0.87. Table 7's `Number of vowels` (+0.083460383) and `Number of consonants` (−0.083460383) carry exactly mirrored coefficients and identical P = 0.093068989, which is what a complement pair (`vowels + consonants = 5`) produces, so one column is redundant; the two `(non-repetition)` rows are not mirrored (−0.106284281/0.032271311 against 0.05075013/0.307685109). The control stage inherits it: block 139 claims `the P-values ... are much less than 0.05` while Table 8's fifth row is `Word commonness | -0.080926 | 0.103481297`, and Table 9 then labels that row `No correlation`. The bands also leave 0.09-0.1 unclassified (`0-0.09` then `0.1-0.3`). "
"**Table 8's numeric column is stored under Table 9**: the twelve numbers (`-0.319578`, `4.37009E-11`, ...) sit in block 146, after Table 9's caption and its name rows, so the layout presents a coefficient table with no coefficients and a degree table carrying scientific notation - and the same six coefficients print a third time inside Figure 5, a one-row strip with the values printed in the cells and a colour bar ticked `-1 / 0 / 1`. Naming is unstable across four forms for one statistic (`Higher-order partial correlation`, `high-order bias correlation`, `High-order partial correlation coefficient`, `higher-order biased correlation analysis`); raw identifiers print as prose (`percent_hard`, `n_changepoints`, `changepoint_prior_scale`, `ds`, `yhat`, `yhat_lower`, `yhat_upper`); `changeepoint` is misspelled once and spelled correctly nowhere; citations print as green live links (`Prophet[4]`, `[5]`, `[6]`). "
"Disagreement: the page range only. `Stored count 16, coded 16, Delta 0`, every boundary matches the printed text, and the note is candid that unit 5 opens and closes on the same sentence. What it cannot show is that the chapter's title and its first two section numbers print inside the previous chapter's table block, and that Table 8's numbers live four blocks after their header. "
"
"
"| 79 | P-C-2023-2318036-f96be15e | 6-13 (6-13) | 20 / 65 | done | **folio offset 0, `Page N of 24`** - `Team 2318036` left, `Page N of 24` right, no footer, so printed = PDF (p6 reads `Page 6 of 24`). **One island**: blocks 63-127 with no gap across eight leaves (PDF p6 3, p7 26, p8 16, p9 3, p10 6, p11 5, p12 6, p13 0 - block 127 starts on p12 and runs onto p13). **The record's `pages [6, 13]` holds here**, unlike the previous pack: first coded block on p6, last ends on p13. Kinds: **63 `body`, 2 `heading` (104 `5 Task 2: Predicting Daily Reports & Hard Mode Percentage`, 105 `5.1 Problem Analysis`), 0 `display`** - the first chapter in this lane with no display block at all, so nine numbered equations are every one of them stored inside a prose block. "
"**Two printed chapters coded as one**, and the record's heading says so itself (`4 Task 1 Indicators and 5 Task 2 T2PL`): units 1-11 define twelve word indicators, units 12-20 build the T2PL player model, forecast one day, and then regress something else. The chapter title `4 Task 1: Word Attribute Indicators` is the tail of block 62, a `data-preprocessing` block that closes the calendar-map discussion; `5.2` closes 106, `5.3` closes 110, `5.4` closes 112, `5.5` closes 120; and the chapter's own last block (127) carries the next chapter's start, `Figure 7: Box plot result 6 Task 3: Predicting Report Distribution 6.1 Problem Analysis`. "
"213 words a page, 1,705 in all: 85.2 per unit, 26.2 per block, median unit 70, unit range 9 to 256, block median 13, block range 2 (block 105, the bare `5.1`) to 222 (block 109). Fifty of the 65 blocks are 19 words or shorter - Table 3 is torn at every row (71-79 with the caption arriving last in 80), the four family bullets split mid-sentence twice (66-70), and the support threshold is cut from its own sentence (`with supporting degree` in 96, `10` in 97). **Nine tags print and three of them share one 15-word block**: `(1)`, `(2)`, `(3)` all inside 90, whose body reads `h i 𝐿𝐹(𝑐) = 0`, leaving block 91 with nothing but `Í 𝑐1∈𝐶 𝑊∈𝐷` and the glossary; `(4)` in 92, `(5)` in 107, `(6)` in 109, `(7)` in 111, `(8)` in 116, `(9)` in 117. Jobs: 5 `define`, 6 `derive`, 2 `compute`, 2 `interpret`, 1 each of `select` and `compare` - **no `read-figure`**, although four of the five figures are read aloud in 116, 119, 121 and 127. "
"**The bridge that is not there**: S2 ends `more likely fail to guess a word.` (103) and S3 opens on heading block 104, so the chapter's biggest jump - from word indicators to an epidemic model - is a heading with no sentence. The pivot inside S3 is the paper's best move: `this model failed to satisfy both the sharp decrease after peaking in February and mild decrease in the second half of the year`, then the mechanism, then the dropped assumption `Modelling all players having the same player leaving rate 𝛽might not work well`, then the split, then the name T2PL. "
"**The arithmetic, and what it lands on.** Point forecast `19367 users` on `2023.3.1`; the band printed from `MAPE = 0.083` is `[17760, 20976]`, whose centre is 19,368 and whose upper bound should be 20,974.5 - and equation (8) defines MAPE with a `100%` factor, so 0.083 is either 8.3% or 0.083% depending on which line you believe. Equation (7) minimises over `(𝛼, 𝛽, 𝛾, 𝑇0, 𝜏, 𝑝)` - six arguments - while the sentence above it estimates eight and Table 4 reports the two that were dropped, L₀ (30,000 to 29,918) and θ (0.02 to 0.0228). Table 4 is never discussed at all, which hides that **γ is the one parameter that does not move** (2 × 10⁻⁴ to 2.0 × 10⁻⁴) while seven others do - the general-player outflow was not identified, which undermines the claim two pages later that `majority of players will be loyal`. "
"**Twelve indicators, eight symbols, six regressors, one figure that refutes the sentence.** `we constructed 12 indicators` against an eight-row Table 3; twelve is reachable only by counting LF_i five times, and the regression then keeps F, N_c, LF4, LF_sum, N_FI2 and silently drops N_v, LF1-LF3, LF5, N_D1, N_D2. Block 119 says general players `decrease to a very low level at the end` and then gives `only 19% ... on 31 December 2022 and 21% on 1 March 2023` - rising, not very low, and dated a month past where Figure 5's axis stops; Figure 5's own curves put general at about 20,000 against loyal at about 8,000, so loyal is the smaller group, the opposite of `the majority of players will be loyal`. Figure 6 then plots `percent of loyal(%)` reaching about 80 on its right axis, two orders of magnitude away from Figure 5's own counts. Figure 3 and Figure 5 share the caption `two-type player dynamic system` over a four-box block diagram and a four-series time plot; Figure 7's prose says `Select the two attributes with the strongest salience` and never names them, while the panels are labelled N_c and LF_sum. "
"**Table 5 is clean; the layout's copy of it is not.** In the order the page prints, all six stars reproduce - t = 86.6, 2.25, 4.66, 2.58, 3.85, 2.45 - but the text layer stores the same six standard errors rotated one place (`(2.814e-12) (5.959e-4) (2.761e-4) (0.0111) (0.0113) (0.0110)`), under which P_H would carry t = 3.4 × 10¹¹ and N_FI2 t = 0.06 with a star. Anyone reading the JSON alone would report a defect the page does not have; this pack reports the rotation, not the table. "
"Disagreement: none on boundaries. `Stored count 20, coded 20`, island unbroken, page range correct, every unit boundary matching the printed text, and the note is candid that the `4 Task 1` heading sits in the previous block. What it cannot show is that its heading line covers two printed chapters and that its last unit carries the next one. "
"
"| 80 | P-C-2023-2318982-4176d64a | 5-19 (5-19) | 17 / 120 | done | **folio offset 0, `Page N of 25`** - `Team # 2318982` left, `Page N of 25` right, no footer, so printed = PDF (p5 reads `Page 5 of 25`). **Three islands over fifteen leaves**: 76-105 (30 blocks), 120-148 (29), 154-214 (61); the two gaps, 106-119 and 149-153, print inside the chapter's own page range but belong to `algorithm` and `results`. **The record's `pages [5, 19]` holds at both ends** - first coded block on p5, last on p19. Kinds: **120 `body`, 0 `heading`, 0 `display`** - no block of either non-prose kind, so all twelve captions and all 22 equation tags print inside prose blocks. "
"**The only chapter in the lane compiled from three runs of another chapter's text, and its two dividing headings are filed elsewhere.** `4.2 Effect of Word Attributes` is the tail of block 119 and `5 Task 2: Distribution based on Markov Chain Model` the tail of 153, both `results`-owned, so on the page each half is announced by a block the record assigns to a different chapter; eight more numbered headings close their own units (`4.1` in 76, `4.2.1` in 120, `4.2.2` in 131, `5.1` in 164, `5.2` in 171, `5.3` in 193, `5.4` in 201, `5.5` in 214) and `4 Task 1` is the tail of 75. Both models report their answer outside the chapter: `16529` with `[10517, 27007]` at 90% is block 118, and the fitted proportion q₁ = 0.63 with `[0.59, 0.67]` is a `results` block too. "
"**228 words a page, 3,414 in all: 200.8 per unit, 28.4 per block, median unit 136, unit range 24 to 704, block median 15, block range 5 to 151; seventy of the 120 blocks are 19 words or shorter.** Seven segments of 440 / 253 / 243 / 448 / 454 / 872 / 704 words: the two under 260 hold three of the chapter's four statistical decisions (ADF, Ljung-Box, the AICc search) and the two largest hold 46% of the words and both models' machinery, in neither case with a sentence saying what the machinery is for. **22 of the paper's 29 tags are here** - (1)(2)(3) then (5) to (23) - **and (4) is the same regression that (3) tags**, printed again on p14; (24) to (29) are `results`. Jobs: 7 `define`, 4 `check`, 3 `derive`, 2 `select`, 1 `compute` - five of the thirteen, and **no `read-figure`** although blocks 100-105, 133 and 141-146 read three exhibits aloud. "
"**The arithmetic that holds.** Table 2's ADF verdicts match the prose: -2.8951 with p = 0.1989 does not reject at α = 0.05, -5.0648 with p = 0.01 does, both at lag 6. Ljung-Box `253.36, p = 0.000` rejects white noise, which is what block 91 says. Table 4's two VIFs, 1.166984 and 1.341964, sit far under the threshold of 10 that block 147 names. On p19 both strategy distributions sum to 100, the mixture with q₁ = 0.63 reproduces the final vector entry by entry to three decimals, and the quoted `95% confidence interval of [0.59, 0.67]` is centred on 0.63. January 7 to December 31, 2022 plus 60 days does land on March 1, 2023. "
"**The arithmetic that does not.** (i) `d` is never valued - `the parameter d of the ARIMA model can be determined as step 1` - and the number 1 first appears inside `ARIMA(1,1,1)` two chapters later. (ii) Equation (1) prints its exponents as literal braces, `p̂{t}`, `ε{t−j}`, so the lag index sits in the base position. (iii) Equation (6) quantifies over the same index it names: `B_{i+1} = {j : ∃i ∈ B_i}`. (iv) Equation (16) is a bare fraction with no left-hand side, introduced by `I_i can be estimated by` and resumed by `which gives the transfer probability`. (v) Equation (28) weights one term only - the `X` term carries `l_X^{(r)}` while the six `i = 1...6` terms carry no `l_i^{(r)}`, although (27) defines it and nothing else uses it. (vi) `384 states` and `about 36,000` words are asserted with no enumeration shown; the only reproducible count on the page is `5 × 26 = 130`. (vii) The same equation prints as (3) on p12 and as (4) on p14 under `the final established multiple linear regression equation was determined to be`, with no new coefficient, fit statistic or data in between. "
"**Against the raster.** Figure 11 titles all four of its panels - `Residuals vs Fitted`, `Normal Q-Q`, `Scale-Location`, `Residuals vs Leverage` - and the prose still reads three of them by position, never mentioning the leverage panel or the `Cook's distance` contour drawn on it, so influence is the one assumption the chapter leaves untested. Figure 8's y axis is labelled `data2$results`, the R data frame and column where the quantity's name belongs; its `0` to `3e+05` scale is consistent with `16529` and its ribbon with the 90% interval, so the label is that figure's only defect. Figure 10 is a lower-triangular heatmap with rotated diagonal labels running `n_repeat` to `Prop` and a -1 to 1 colour bar, so `strong correlation` is a reading of cell colour, not of a printed coefficient. Figure 9 is a 2×3 grid - three density curves over three pie charts - with no panel labels and no title. Figure 12 is a coloured flow chart whose boxes carry `Initial distribution`, `State space`, `Transfer probability`, `Distribution of reported result` and whose arrows are labelled `determine` and `influence`, and no sentence in the chapter reads any of it. Figure 13 has no axes, no ticks, no legend and no printed numbers, so `a chain is shown below as a example` cannot be checked against it. "
"Disagreement: none on counts. `Stored count 17, coded 17, Delta 0`, the three runs match the layout exactly, and every unit boundary matches the printed text. What the record cannot express is that the chapter is compiled from three runs of another chapter's pages, that both section-dividing headings sit in `results`, that both models' answers are `results` blocks, and that its equations (3) and (4) are one equation. "
"| 81 | P-C-2023-2322645-8a06f4dc | 4-14 (4-14) | 18 / 73 | done | **folio offset 0, `Page N of 22`** - `Team # 2322645` left, `Page N of 22` right, no footer, so printed = PDF (p4 reads `Page 4 of 22`, p14 `Page 14 of 22`). **One island**: blocks 50-122 contiguous, 73 blocks over eleven leaves, with `data-preprocessing` owning 44-49 on p4 and `results` owning 123-124 from p14. **The record's `pages [4, 14]` holds.** Kinds: **64 `body`, 2 `heading`, 7 `display`** - and all seven displays are captions or extracted figure interiors (56, 73, 86, 87, 90, 91, 92), so **no display block holds an equation**. "
"**The best-behaved chapter in the lane and the worst-served by its layout.** It is a single argument in five moves - five word traits, two entropy measures, a Beta embedding, a Lasso screen, a three-submodel Bayesian model - with every unit a whole thought; and its seams are sentences that end in the next heading. `3 Word & Difficulty Representation`, the chapter's own title, is the tail of block 49, a `data-preprocessing` block; `4 Modeling Methodology` with `4.1 Lasso regression` closes 82; and fifteen of the seventeen numbered headings inside the leaves are welded into prose tails, `3.1` into 51, `3.2` into 52, `3.3` into 53, `3.4` into 54, `3.5.1` into 59, `3.5.2` into 63, `4.2` into 88, `4.2.2` into 102, `4.2.3` into 110, `4.2.4` into 115, `4.2.5` into 121. Only `3.5 Entropies` (57) and `3.6 Representation of word difficulty` (74) are `heading` blocks, and two run-in sub-headings - `Word difficulty` and `Day-of-week effects` - exist nowhere in the record. "
"**320.7 words a page, 3,528 in all: 196.0 per unit, 48.3 per block, median unit 181, unit range 43 to 413, block median 33, block range 1 to 154; twenty-nine of the 73 blocks are 19 words or shorter.** Seven segments of 514 / 979 / 676 / 261 / 714 / 311 / 73 words. Block starts per leaf run 4: 2, 5: 3, 6: 9, 7: 9, 8: 10, 9: 3, 10: 4, 11: 3, 12: 17, 13: 9, 14: 4 - and both troughs are floats: p10 carries 96 words under Figures 5 and 6, p11 carries 238 under Figure 7 and its 154-word caption, which is tied with the 154-word opening paragraph as the chapter's longest block. **Five equations are numbered and fourteen displays are not** - (1)-(5) all print on p12 with their tags in one flush-right column and inside their own blocks, and everything before and after them is unnumbered, including all three likelihoods. Jobs: 7 `define`, 4 `compute`, 4 `derive`, 1 `mechanism`, 2 `select` - five of the thirteen, **no `read-figure`** although five of seven figures are cited by number and Figure 7 is read only through its caption. "
"**The arithmetic that holds, and it holds better than in any pack so far.** All five printed cross-references resolve to the right equation - `as defined by Equation 1` is `dtry`, `Equation 2` is `dreports`, `Equation 4` is `Preports`, `Equation 5` is `Phardmoders`, `Equation 3` is `dhardmoders` - which no other chapter in this lane manages. The factor example checks (`shrinking from 4,000 to 1,000 words would have ft(g) = 4`), so does the Beta mean identity `E[p] = ηκ/(ηκ + (1 − η)κ) = η`, and the four Lasso survivors named in prose are exactly the four regressors x1 to x4 the later equations use. Figure 4's fitted pairs convert to α/(α + β) = 0.567, 0.530, 0.437 and 0.658: all inside Figure 5's printed support of 0.4 to 0.8, all around its peak near 0.55, and `Swill` hardest / `Saint` easiest in both exhibits. "
"**The arithmetic that does not.** (i) Seven outcomes are drawn from six probabilities, twice: `(t1, …, t7) ∼ Multinomial (n, 7, (p1, p2, p3, p4, p5, p7))` and `(p1, …, p5, p7) ∼ Dirichlet(7, (A1, …, A7))`, which then sets seven concentration parameters against six probabilities - and p12 prints it that way, so this is the paper, not the layout. (ii) Numbering stops at (5), so the twelve displays that constitute the three submodels cannot be referred to and are not. (iii) `λ ... set to 0.1 to obtain the desired number of parameters (four)` is the chapter's only model-selection step and it prints no coefficient path, no λ sequence and no output table - Figure 6 shows the inputs, nothing shows the output. (iv) `B ... Exponential(0.01) prior ... so as to allow it to be large` agrees with itself only if the argument is a rate, and the convention is never stated. (v) `which is has a long tail` is in the print. "
"**Two layout tears the page does not have.** The Positional Entropy equation prints as one clean centred line but is stored as three blocks in reverse order: `5 X` ends 61, the summand is 62, and `H(X) := i=1` opens 63. `ft(g) = n/n1` prints as one centred display and is cut at its bar - 65 ends `ft(g) = n`, 66 begins `n1`. The Beta density has the same disease with the fraction in front of its own left-hand side (block 75 ends `1 B(α, β)xα−1(1 −x)β−1, f(x; α, β) =`), and the Lasso cost function is stored as `!2 n P P X X X yi − |βj|, min xijβj + λ β i=1 j=1 j=1` where the page prints both summations stacked with limits above and below. "
"**Against the raster.** Figure 7's colours are load-bearing and invisible to extraction: blue the Try model, red the Reports model, yellow the Hardmoders model, green the α and β of the difficulty Beta, and its dimension labels (`7` beside `a0`, `a2`, `A`, `P`, `κ`; `5` under `γ`) are the only place a reader learns `d_try` is a 7-vector while `P_reports` is a 5-vector. Figure 6 is a flow diagram with a colour legend separating `Function`, `Data Table` and `Subset of Data`, and its callout prints the Shannon entropy formula a second time. Figure 5's dashed vertical line at about 0.51 is drawn and never explained in any caption or sentence. Figure 4's two series cross repeatedly, which is the visual case for the non-linear least-squares fit the prose gives one clause. And there is **no table anywhere in the chapter**: the only grid is Figure 1, captioned `Figure 1: Left: 30 Most common words based on overlap. Right: Frequency of Letters in the SGB wordbank`. "
"Disagreement: none on counts. `Stored count 18, coded 18, Delta 0`; the island is unbroken; every unit boundary matches the printed text; the `display` count of 7 is right. What the record cannot show is that the chapter's title belongs to `data-preprocessing`, that fifteen of seventeen headings are prose tails, that the two run-in sub-headings are invisible to the coding, and that its seven figures include one that is two tables and one that is a flow diagram carrying a formula. The record's heading line concatenates two printed chapter titles (`3 Word & Difficulty Representation` and `4 Modeling Methodology`), which is the honest symptom of that first defect. "
"| 82 | P-C-2024-2401298-07d37078 | 5-21 (5-18) | 20 / 118 | done | **folio offset 0, `Page N of 25`** - `Team # 2401298` left, `Page N of 25` right, no footer, so printed = PDF (leaf 5 reads `Page 5 of 25`, leaf 21 reads `Page 21 of 25`). **The record's `pages [5, 18]` is right at the near end and three leaves short at the far end**: the chapter's coded blocks print on p19, p20 and p21 - `5.2.4 Inference on Match Data` and `5.2.5 Advisement` plus the five strategy bullets on p19, `6 Problem 4 : Swings Prediction and Model Generaliza-tion` at the top of p20 with blocks 185-186, and `Figure 14`'s caption on p21 - so the printed extent is seventeen leaves, not fourteen. Kinds: **102 `body`, 11 `display`, 5 `heading`**. The eleven displays are nine figure captions (57, 67, 72, 75, 145, 148, 150, 154, 187), one equation (115, holding (9)), and one chapter title (180, holding `6 Problem 4`); thirteen of the fourteen numbered equations therefore print inside `body` blocks. "
"**Four models stapled together, and the record cannot see the seam material.** S1 units 1-2 (563 words) builds the points-difference then the probability-difference metric; S2 units 3-5 (517) picks the window and states H0; S3 units 6-7 (372) runs Ljung-Box and the runs test; S4 units 8-10 (535) fits the naive binomial by maximum likelihood and reports `lambda = 0.0624, s = 0.1742`; S5 units 11-12 (612) turns momentum into a residual `E := S - S` by equivalence and imports three latent variables; S6 units 13-14 (397) screens eleven features and draws the two networks; S7 units 15-18 (660) denoises, writes (12)-(14) and discretises; S8 units 19-20 (341) lists five strategies and then carries the next chapter's title, a watermark-only heading and a stray figure caption. Twelve of the chapter's sixteen printed numbered headings are welded into prose tails - `3.2` into 58, `3.3` into 69, `4` into 76, `4.1` into 77, `4.3` into 93, `5` into 99, `5.2` into 120, `5.2.1` into 127, `5.2.3` into 151, `5.2.4` into 171, `5.2.5` into 172, and `5.2.2` as a two-word body block of its own (146) - and two of those tails belong to `results` blocks. "
"**249.8 words a page, 3,997 in all: 199.8 per unit, 33.9 per block, median unit 187, unit range 92 to 374, median block 22, block range 0 to 172; forty-seven of the 118 blocks are 19 words or shorter.** Block starts per leaf run 5:7, 6:10, 7:5, 8:6, 9:11, 10:0, 11:14, 12:13, 13:10, 14:5, 15:5, 16:4, 17:7, 18:7, 19:9, 20:3, 21:2 - leaf 10 is the only zero, and its content is not in the chapter at all. **Fourteen displayed equations, tags unbroken 1-14** at p5, p6, p7, p9, p9, p11, p11, p12, p12, p12, p12, p17, p18, p18, every tag flush right on its equation's own line except (9), pushed one line down because the line already reaches the margin. **No unnumbered display equation anywhere in the chapter.** Jobs: 6 `define`, 5 `compute`, 5 `derive`, 1 `check`, 1 `select`, 1 `interpret`, 1 `handoff` - and **no `read-figure` job at all**, although the chapter carries eleven figures. "
"**Eleven figures and two tables, and the tabular half is broken.** Nine figure captions are display blocks; Figure 6's caption is welded into the tail of block 93 together with `4.3 Instantaneous Winning Rates` and a citation bracket (`Figure 6: feature importance 4.3 Instantaneous Winning Rates [4], we employed`); Figure 7's caption closes 137 and Table 3's caption opens 138. **Table 2 belongs to no chapter**: its caption is block 95, its column heads block 96, its cells block 97, and all three print on p10 inside the chapter's own range while the record files them under nothing. Table 1 is a `data-preprocessing` exhibit four leaves early. Three exhibits are never cited by number (Figures 4, 5, 11) and two are cited nowhere in the chapter (Figures 6, 14). "
"**Against the raster.** Figure 6's caption reads `feature importance` over a grouped bar chart of Ljung-Box and Wald-Wolfowitz p-values with a significance line at 0.05 - it is the section-4 result redrawn, and the caption names neither. Figures 12 and 14 print the **same caption word for word** (`Differences in Residual Effects and Entropy`) eight pages apart, and Figure 14 has only the two residual-effect panels while the entropy panel is missing. Figure 8 is promised as a heatmap at block 139, prints on p15, and is read by nobody - the five bold-labelled readings at 140-144 tabulate Table 3's importances instead. Figure 10's middle input boxes print so washed out they are barely legible. Table 2 prints `Player 2` in its first row where `Player 1` belongs, so the `around 1%` increase the prose reports is the within-column immediate bump (0.0104 and 0.0089) and cannot be assigned to a player. Table 3's eleven importances sum to 0.783 with seven of them carrying 0.642. And the print itself leaks markup - p17 reads `let it predict **the sum** of the effect in the next n points`. "
"Disagreement: the counts hold, the range does not. `Stored count 20, coded 20, Delta 0` is honest for the coding given: every group resolves, no block is double-owned, 118 of 118. What the record cannot show is that its `pages [5, 18]` stops before p19-21, that blocks 94-97 belong to no chapter, that block 181 is a zero-word watermark heading with no printed counterpart, that block 180 stores a chapter title as a `display` across a page break the page does not have, that two of the chapter's own headings are stored inside `results` blocks, and that its last group closes on a `conclusion` block (189, Figure 15 plus the `7 Model Analysis` heading). "
| 83 | P-C-2024-2401445-6a882749 | 6-20 (6-20) | 15 / 71 | done | **folio offset 0, `Page N of 26`** - `Team # 2401445` left, `Page N of 26` right, no footer, so printed = PDF (leaf 6 reads `Page 6 of 26`, leaf 20 reads `Page 20 of 26`). **Ten of the 71 blocks are in the record twice**: 74-83 sit in this chapter's groups 5, 6 and 7 *and* in `results`, so 15 groups resolve and 71 blocks are listed while only 61 belong to this chapter alone. **The `pages [6, 20]` claim holds page-wise and fails structurally**: block 195 on p20 is real, but it is the closing paragraph of `results` subsection 7.3, the paragraph immediately before it on the same page is `results` block 194, and the layout welds `8 Sensitivity Analysis` onto block 195's tail. Kinds: **69 `body`, 1 `display`, 1 `heading`** - the one display is block 51, the chapter title under the wordmark, and the one heading is block 101. "
**Four tasks in fifteen units, written as sub-tasks rather than as an argument.** S1 units 1-2 (439 words) builds the Dynamic Play Index and detours into gradient-boosted trees for one of its three terms; S2 units 3-7 (448) finishes that branch and chooses the weights `α = 0.28, β = 0.32, γ = 0.4`; S3 units 8-10 (482) proves momentum exists by simulating a world without it and measuring DTW distance; S4 units 11-12 (296) defines momentum, swing and turning point, then labels them with a random forest; S5 units 13-14 (533) adds an HMM and Situational Leverage; S6 unit 15 (58) is one paragraph on p20 that closes somebody else's section. **Twenty numbered headings print in these pages and the record stores one**: `4`, `4.1`, `4.1.1`, `4.1.2`, `4.1.3`, `4.1.4`, `4.2`, `5`, `5.1`, `5.2`, `5.3`, `6`, `6.1`, `6.1.1`, `6.1.2`, `6.1.3`, `6.2`, `6.3`, `6.4`, `6.5`, and six of the nineteen prose tails sit in blocks owned by other chapters (59, 73, 80, 82, 126, 149). Both printed model titles are borrowed: `6 Model II: Momentum Turning Point Identification and Prediction Model based on HMM-Random Forest` and `6.1 Definition` close block 126, a `results` block. "
**188.0 words a page, 2,256 in all - the thinnest chapter in the lane: 150.4 per unit, 31.8 per block, median unit 138, unit range 22 to 402, median block 27, block range 5 to 83; thirty-one of the 71 blocks are 19 words or shorter.** Block starts per leaf run 5:1, 6:3, 7:8, 8:3, 9:10, 10:2, 11:12, 12:7, 13:13, 15:4, 16:7, 20:1 - leaf 5 is a single title block, leaf 10 is two heading blocks and one sentence, and leaves 14 and 17-19 carry none of the chapter. **Fifteen displayed equations, nine numbered**: (1) p6, (2) p7, (3) p7, (4) p8, (5) p8, (6) p9, (7) p9, (8) p13, (9) p16, all tags flush right and all nine inside `body` blocks; the six untagged displays are the weights line on p9, the DTW recursion on p11, and `B1`, `B2`, `Π`, `B3` on p16. **Numbering stops at (9)** - p17-20 carry prose, figures and tables only. Jobs: 6 `define`, 4 `derive`, 2 `select`, 1 `compute`, 1 `limit`, and **no `read-figure`** although twelve exhibits print inside the chapter's page range. "
**The chapter needs six exhibits and owns four.** Figure 4's GBT diagram (62), Table 2's seven indicators (75, double-owned), Table 3's one-row grid search (139, caption and row inside the same body block) and Figure 9's HMM diagram (152) are its own; Figures 5, 6, 7, 8 and Table 4 - the four exhibits its evidence rests on - are `results` blocks, read by `results` paragraphs. **Table 3 is bought and never opened**: no sentence refers to it, and its row (`10 | 4 | 10 | 300`) contradicts the hyperparameter table drawn inside Figure 4 (Learning Rate 0.2, Max Depth 5, n_estimators 300). Figure 6's caption stops mid-phrase (`DPI plot of the final`), its in-figure title misspells `Ponits`, and its legend names the players `DPI of Play1` / `DPI of Play2`. "
**Against the raster.** Figure 7 is a two-storey composite - seven DTW path panels over seven bar pairs from 517/1685 to 550/2361 with percentage drops of -72% to -57% - and no caption or sentence names those bars or their colours, yet this exhibit is the whole of the Task-2 evidence. Figure 8 has no axis, only a `Decreasing Significance` arrow and a three-way legend. Figure 4 is two diagrams in one frame with the boosting formulas written inline. Table 2's last row prints the raw variable name `p1_winner` where the other six print formulas, and its `PWOL` column sums to 403.0 for a weighted average the paper never computes. The paper also contradicts itself in print: a hard-voting classifier is reported as `an accuracy of 77.6%` (p14), as per-class precision 0.74-0.84 / recall 0.74-0.88 / F1 0.76-0.84 (Table 5), and as accuracies 0.83 / 0.85 / 0.58 (Table 6), with no reconciliation, and p19's first sentence prints as `Tcted from he table below presetrants the performance of our model`. "
Disagreement: blocks are double-owned, headings are not coded, and the page range hides a section that is not the chapter's. `Stored count 15, coded 15` counts groups only; the honest block count for this chapter alone is 61, not 71. What the record cannot show is that 74-83 belong to `results` as well, that nineteen of twenty printed headings are prose tails, that both printed model titles live in a `results` block, that (2) and (3) are fragmented and (3)'s tag is attributed to the following page, that six displays carry no tag, and that its last group closes 7.3 of Task 4 rather than any of its own sections. "
| 84 | P-C-2024-2401919-3f4373c1 | 6-17 (6-17) | 14 / 68 | done | **folio offset 0, `Page N of 25`** - `Team # 2401919` left, `Page N of 25` right, no footer, so printed = PDF (leaf 6 reads `Page 6 of 25`, leaf 17 reads `Page 17 of 25`). **Twenty-one numbered headings print between `3` and `6.1`; five are stored as `heading`, two as `display` and fourteen welded into `body` blocks** - and five of the welded ones sit inside blocks the record files under `results`, so the chapter's own `4 Task3`, `4.1`, `4.2`, `4.4` and `5.3` are printed inside another chapter's paragraphs (98, 100, 114, 133); `5.2.1` is split so its number ends block 122 and its title is all of block 123. `3.3` (80) and `5 Task4` (116) are stored as `display` blocks because a watermark string fell inside them. Kinds: **57 `body`, 6 `display`, 5 `heading`**; the six displays are Figure 3's four flowchart boxes (65-68) plus those two headings. "
**Five tasks in fourteen units, each announced and then abandoned to `results`.** S1 units 1-3 (p6-7, 723 words) says what to measure and why one PCA-TOPSIS runs per player per match, then partitions performance into five aspects; S2 units 4-6 (p8-10, 313) goes from the serve count to dimensionless indicators to eighteen contribution rates stopping at component 6; S3 unit 7 (p11, 114) substitutes six components and prints the score identity; S4 units 8-10 (p12-14, 631) tests whether the score series is white noise; S5 units 11-13 (p14-16, 547) turns swings into a catastrophic sequence and predicts them with GM(1,1); S6 unit 14 (p17, 270) sets up grey relational analysis and stops on equation (17) without a result. **The chapter reads none of its own exhibits**: heat map (82-83), eigenvalue paragraphs (89-92), score trend (97) and ACF/PACF reading (104) are all `results` blocks, and no unit carries the `read-figure` job. "
**216.5 words a leaf, 2,598 in all: 185.6 per unit, 38.2 per block.** Unit words in order 127, 117, 479, 51, 102, 160, 114, 93, 234, 304, 156, 90, 301, 270 (median 141.5); block median 29, range 3 to 140, **28 of 68 blocks 19 words or shorter**. Leaf words 210, 190, 481, 51, 104, 114, 279, 105, 255, 409, 130, 270 - **p9 carries 51 words because six of its blocks belong to `results`**. **17 displayed equations, all numbered, all flush right**: (1) p8 standardisation, (2) p9 correlation, (3)(4) p9 contribution and cumulative rates, (5)(6) p11 weight matrix and score identity, (7) p13 H0, (8) p14 Ha, (9) Ljung-Box, (10) Box-Pierce, (11) rejection rule, (12) p15 level ratio, (13)(14)(15) p16 grey equation, whitening equation and closed form, (16)(17) p17 relational coefficient and grade; the AGO and mean sequences at the head of p16 carry no tag. Jobs: 4 `check`, 4 `derive`, 3 `define`, 1 `compute`, 1 `source`, 1 `define` late, and no `read-figure`. "
**Ten exhibits in the page range, five owned by the chapter.** Own: Figure 3's schematic (caption welded into block 69 with the `3.2` and `3.2.1` headings), Figure 4's radial bubble cluster (no caption block at all - the caption and the node labels are flattened into the head of block 70), Table 2 (caption, header cells and eighteen rows inside block 86), Figure 6's eigenvector table (caption 88) and Figure 8 (caption 103, after two in-figure tick strings and a watermark). Borrowed from `results`: Figure 5 heat map, Figure 7 score trend, Figure 9 turning plot, Table 3's eighteen correlations, and the four paragraphs that read Table 2 and Figure 6. Table 1 is cited once (`we have adopted the nomenclature presented in Table 1`) and never captioned in the body. "
**Against the raster.** Table 2's rates check out row by row (81.38 + 5.27 = 86.65, and 86.65% is the six-component cut) but **the chapter's weight list takes row 6 and row 7 as W5 and W6** - `W5 = 0.0527, W6 = 0.0363` - dropping component 5's 0.0556, so the vector multiplied in (6) is not the first six contributions, and no threshold is ever given for stopping at six. The object captioned `Figure 6` is a numeric table whose last row `SC` is six zeros, and the sentence reading it says `the table above` and speaks of `the eigenvalues` while its columns are eigenvectors. Figure 4 is a hand-styled bubble cluster with no axis, no legend, no scale, a duplicated `RP rate` and a duplicated `Sets won`, and two labels overflowing their bubbles. Figure 7's four dashed vertical markers are unlabelled and its in-image title duplicates its caption; Figure 8's panels carry tick numbers only; Figure 9's title reads `Predict Turn Point` against a caption saying `Predictive and Actual Turning plot`, and p16 announces it one leaf before it prints. The p-values are printed (`p_LB = 6.645 × 10^-13`, `p_BP = 2.087 × 10^-12`) with no `Q_LB` or `Q_BP` value anywhere, and the diagnosis prints `Δ = 0.0378` as second class and then calls `g0 = 0.9895` and `C0 = 0.1284` `both ... a First Class accuracy`, folding a second-class criterion into a first-class claim. "
Disagreement: none on counts, several on structure. `Stored count 14, coded 14` holds - the fourteen groups are contiguous in reading order and every id resolves - so the pack's block numbers are the layout's. What the record cannot show is that 23 blocks inside these twelve leaves belong to `data-preprocessing` and `results`, that five of the chapter's own numbered headings are inside four of those borrowed blocks, that `5.2.1`'s number and title are in different blocks, that two headings are `display` blocks because of a watermark, and that the chapter's last page carries Figure 9 (a `results` exhibit) between its own blocks 133 and 139. "
| 85 | P-C-2024-2403774-be4a823f | 10-21 (9-21) | 8 / 79 | done | **folio offset 0, `Page N of 23`** - `Team # 2403774` left, `Page N of 23` right, no footer, so printed = PDF. **The record's page range is one leaf late**: block 133, the chapter's own title behind two watermark strings, prints on p9 and is attributed `[9, 10]`, while `pages [10, 21]` starts the chapter on p10. **None of the six `display` blocks is a bare figure**: 133 is the title behind watermarks, 153 is the `Algorithm: Momentum Quantization` pseudocode box, 157 and 160 are captions fused to the `5 Task 2` and `5.2` headings, 176 is a caption fused to the `6 Bayesian ...` heading, and 201 carries **three captions in one 8-word block** (`Figure 12: Dilated Conv Figure 13: Causal Conv Figure 14: MSTCN`). Kinds: **72 `body`, 6 `display`, 1 `heading`** - the single heading is 177. 
**Six segments, each installing a different estimator for the same latent quantity.** S1 units 1-2 (p9-10, 294 words) defines momentum by the converse and builds the label; S2 unit 3 (p10-12, 856) fits XGBoost and ends on `the average MSE for the model was found to be 0.02`; S3 unit 4 (p13-14, 395) builds the random-match control and prints Table 5's comparison; S4 units 5-6 (p15-18, 762) detects inflection points with a Bayesian run-length model, explodes its symbol glossary into thirteen one-line blocks, and hands binary labels to a TCN; S5 unit 7 (p18-19, 280) specs the two-layer network and Table 6; S6 unit 8 (p21, 178) lists four remedies that are never run. **Nineteen numbered headings print between `4 Task 1` and `7.2 Model Evaluation`: 1 stored as `heading`, 4 as `display`, 14 welded into `body` tails, and 6 of those inside five `results` blocks** (195, 198, 219, 232, 239). `6.3.2` is never printed - the numbering jumps 6.3.1 to 6.3.3. 
**230.4 words a leaf, 2,765 in all: 345.6 per unit, 35.0 per block.** Unit words 128, 166, 856, 395, 423, 339, 280, 178 (median 309.5; the largest unit is 4.8 times the smallest). Block median 16, range 1 to 191, **43 of 79 blocks 19 words or shorter** - thirteen of them the Bayesian symbol glossary (180-192) and one of them the single word `6.1.1 Principle`. Leaf words 7, 545, 371, 227, 291, 104, 222, 132, 69, 419, 200, 178: **p9 carries seven words of this chapter and p20 carries none**. **10 displayed equations, numbered (4) to (13)** - the chapter's first equation is its fourth, because (1)-(3) belong to the earlier model chapter while this chapter's own bold steps are labelled `(1) Data Preprocessing` to `(7) Model Evaluation`, so the same small numbers print twice in four pages. **(4) is stored with its denominator missing** (`M_m0` opens block 138, just before the `4.2` heading) and **(10) is a five-line braced system restating (4), (6), (7) and (8)** under a single tag. Jobs: 3 `derive`, 2 `check`, 1 `define`, 1 `compute`, 1 `select`, 1 `limit`, and no `read-figure`. 
**Seventeen exhibits in the page range, nine owned by the chapter.** Own: the pseudocode box, Table 4, Table 6, Figure 7, Figure 8, Figure 9 and Figures 12-14. Borrowed from `results`: Figure 10, Figure 11, Figure 15, Figure 16, Figure 17, Table 5 and the paragraphs that read them; Figures 5 and 6 on p9 belong to `data-preprocessing`. **Cross-references are off by one five times** - `as shown in Figure 10 and Figure 11` (one figure, two panels), `as shown in Figure 12` (Figure 11), `as shown in Figure 13` twice (Figure 12), `as shown in Figure 15` (Figure 14) - and two sentences on p20 print the literal placeholder `Figure X:`. Figure 7, Figure 9 and Table 6 are never read by any sentence. 
**Against the raster.** Table 5's `random` row prints `MSE 0.136022, RMSE 0.368812, MAE 0.301388, R2 -2.54679, adj -2.55744`, while p14 states the same baseline as `0.125576`, `0.354367`, `0.297229` and `-2.2744` - about 8% lower, which inflates the advantage the table is cited to prove; the table also skips match 1310 (1309 then 1311), carries an `...` ellipsis row, and splits across the p14-p15 break with no repeated header. Table 6 prints `Leaning-Rate` with the value `le-4` (the `1` of `1e-4` lost) and states no kernel count, layer count or channel width. Figure 17's caption is stored as a `heading` block with the watermark in front of it (238). Figure 16's in-figure colour note overlaps its own tick labels and the `Spearman Correlation` axis title; Figure 11's y-axis labels sit under the diagonal watermark; Figure 6's note clips at the plot's right edge (`Note: The depth of color indicates the strei`). 
Disagreement: counts hold, the page field does not, and the page field matters. `Stored count 8, coded 8` resolves every id, but `pages [10, 21]` excludes p9 where the chapter's title prints, and p20 contributes no chapter block at all even though it is inside the range. What the record cannot show is that 34 blocks in these leaves belong to `results` (156, 170-175, 193-198, 219-239), 7 to `data-preprocessing` and 2 to `sensitivity-analysis`, that six of the chapter's own headings are inside four of those `results` blocks, that the last chapter block ends with the next chapter's `8 Sensitivity Analysis` heading welded on, and that `6.3.2` does not exist. 
| 86 | P-C-2024-2406176-bd7757f9 | 6-23 (6-23) | 12 / 110 | done | **folio offset 0, `Page N of 27`** - `Team # 2406176` left, `Page N of 27` right, so printed = PDF leaf on the twelve leaves two audits read (6-11, 12-17, 18-23). The layout runs to leaf 28 because the appendix does. **There is not one `display` block in 110**: 108 `body` plus 2 `heading` (75, 129), so every equation, the factor matrix and all three pseudocode boxes sit inside `body` and are torn wherever the block boundary falls. **Seven of the twenty-three numbered headings printed between p6 and p23 have no block at all** - this chapter's `5.4 Quantification of Momentum` (p11) and `6.3 Exploratory Factor Analysis` (p16), plus `6`, `6.1` (p15), `7` (p18), `8.1` (p21) and `8.4` (p22). 
**Eight segments, each a different model for the same quantity.** S1 units 1-2 (p6-7, 293 words) defines momentum by the Gilovich gap and prices the opponent with Elo; S2 unit 3 (p8-10, 413) solves for the first point with `Algorithm 1` and the dichotomy, ending mid-sentence on `the winning probability of both`; S3 units 4-5 (p10-11, 327) resumes that sentence after Figure 4 and builds the quasi-binomial updater with its weight `𝜂(𝑆𝑚) = 𝛼/(𝛼+ 𝑛)`; S4 units 6-7 (p11-12, 244) computes momentum as the gap and installs the CWP rival by `setting 𝜂(𝑆𝑚) = 1`; S5 unit 8 (p14, 126) smooths the curve with a Fourier fit; S6 units 9-10 (p16-18, 729) gates 25 indicators through Bartlett's test and regresses the trend on five factors; S7 unit 11 (p18-21, 840) clusters seven shot-choice strategies and prints (15)-(19) for a mixed-strategy Nash equilibrium; S8 unit 12 (p22-23, 104) waives the IID calibration for best-of-three and stops. **Six transitions are headings or leaf breaks, none is a sentence** - the two exceptions resume a broken clause (`players in the next point through the equation below`) or point backwards across a `results` leaf (`Beyond the generalization verification with the French Open dataset`). 
**256.3 words a unit, 28.0 a block, 192.3 a leaf: 3,076 words over sixteen leaves.** Unit words 133, 160, 413, 116, 211, 88, 156, 126, 442, 287, 840, 104 (median 185.5; the Nash unit is 9.5 times the shortest). Block median 17, range 5 to 181, **66 of 110 blocks 19 words or shorter and 14 are 9 words or shorter**; p19 alone starts twenty-one blocks because the seven strategy descriptions are chopped at about 19 words each. Chapter words by leaf 133, 179, 212, 230, 292, 153, 180, **0**, 126, **0**, 288, 404, 292, 279, 290, 42, 104, 104: **p13 holds only `results` and p15 only `data-preprocessing`, so two leaves inside the declared range carry none of this chapter.** **19 displayed equations, tagged (1) to (19); this chapter owns 18.** (1) tags two lines, (5) is a three-line braced system split across blocks 100-101 with the tag on the first, (13) is a matrix whose brackets survive as box glyphs, (14)'s tag precedes its own content, and **(12) prints inside a `data-preprocessing` block on p15 where it numbers three definitions at once** - `Aces_p𝑖`, `Break_p𝑖` and `Depth_CTL_p𝑖` - so the chapter's sequence appears to jump (11) to (13). Jobs: 7 `derive`, 1 `define`, 1 `select`, 1 `compute`, 1 `limit`, no `check`, no `read-figure`, no `compare`. 
**Twenty exhibits in pp6-24, twelve owned: nine figures and three pseudocode boxes, and no table at all.** Own: Figures 2, 3, 4, 5, 6, 8, 9, 10, 11 and Algorithms 1, 3, 4. Borrowed: Figure 7, Algorithm 2, Table 3 (all `results`), Figure 12 and 13 (`results`), Figure 14 (`memo`), Tables 1 and 2 (`notation`, `data-preprocessing`). **There is exactly one numbered exhibit citation in the chapter's 110 blocks** - `FromFigure 4 wecan see`, with all three spaces missing - and everything else is `the figure below`, `is indicated below`, `are shown in figure 10 below`, `is shown in figure 11 below`. **Figure 2's caption is stored in the same block as the `5.1` heading** behind three watermark strings, and Figure 12's caption carries `8.2` the same way. Three captions hold watermark strings of their own (98, 180, 206, 216). Table 3's caption is Table 1's caption reused verbatim over `D Value` and `p value`. 
**Against the raster.** Equation (12) covers three definitions with one tag, level with the second line, with a centred orphan `...` under it. Algorithm 1 never computes `𝑝𝑆𝐴(6,6)`, so the tiebreak branch is missing from the match sum; Algorithm 3 prints `The data is appropriate for factor analysis.; end else` with a full stop before a semicolon and an `end` before the `else`; Algorithm 4 announces linear regression and then `Calculate the predicted probabilities 1/(1+𝑒^{−X𝛽})`, returning `𝛽, ˆ MMT`, an identifier that appears nowhere else. **The same Bartlett pseudocode is printed twice** - Algorithm 3 on p16 and Algorithm 5 on p28 in the AI-usage report, prompt and answer included. **(18) and (19) print the same `arg max` condition**, told apart only by an asterisk on `p_{−i}`. **`Fig.x` reaches print twice** (p21 for Figure 12, p23 for Figure 14). The loadings bullets describe Factors 1, 2 and 4 and skip 3 and 5 after `Taking 3 factors as an example`, and the naming sentence breaks its commas with a full stop: `Factor 2 as ExtendedPlay. Factor 3 as Endurance,`. Figure 11's pie prints a labelled `0.0%` wedge for `Short-Ball Maneuver`; Figures 12 and 13 carry the identical caption `FSF model and SP model results`. 
Disagreement: counts hold, the page field is one leaf short, and one foreign block is double-listed. `Stored count 12, coded 12` resolves all 110 ids, but 226's last words print on p23 while the layout's `memo` block 228 continues onto p24, outside the declared range. What the record cannot show: 63 blocks in these eighteen leaves belong to six other chapters (`data-preprocessing` 27, `results` 20, `notation` 10, `limitations` 3, `assumptions` 1, `sensitivity-analysis` 1, `memo` 1), so 173 block slots map onto 172 physical blocks because **block 225 is listed in both `limitations` groups** (`[[224, 225], [225]]`); two of the chapter's eleven headings were never stored; the chapter's evidence (`111`, `115`, `120-128`, `133`, `181`, `217-223`) is read entirely in `results` blocks; and the record's own note is wrong on one point - it says group 12 contains `the 8.4 Key Indicators heading`, but 226 holds only prose and the welded `9 Sensitivity Analysis`, and `8.4` prints on p22 as a heading with no block. 
| 87 | P-C-2024-2406324-2b0f4e28 | 6-19 (7-17) | 11 / 67 | done | **folio offset 1, `Page N of 25`** - `Team 2406324` left, `Page N of 25` right on a rule under the head, printed = file page − 1 on all fourteen leaves (leaves 6-9, 10-13 and 14-19 read separately), so the record's `pages [6, 19]` means printed 5-18 and **both ends are wrong in opposite directions**: the title prints at the top of leaf 7, not 6, and the chapter's last sentence ends leaf 17, not 19. Block 32 is attributed `[6, 7]` for a title that prints wholly on leaf 7, which is what puts two words of this chapter on leaf 6. **63 `body`, 3 `heading` (33, 68, 78), and exactly one `display`** - block 32, and it is the chapter title, not mathematics. 
**Seven segments.** S1 units 1-2 (leaves 6-7, 183 words) names the chapter, imports momentum from physics and fixes `M(x) = α·G(x) + β·P(x) + ϵ`; S2 units 3-5 (7-9, 723) derives `G(x)` as a five-game EWMA with weights 0.4 / 0.25 / 0.05 split 0.5 between serving and receiving, rejects the linear map for a sigmoid, reuses the same weights at point level for `P(x)` and standardises; S3 units 6-7 (9-11, 500) turns the curve's corners into swings and filters them with four smoothing algorithms until `coif5` at level three survives; S4 unit 8 (11-12, 150) replaces "sharp corner" with zero first difference plus a second difference above 0.03; S5 unit 9 (12, 220) runs the run test; S6 unit 10 (12-16, 937) selects and repairs a prediction network; S7 unit 11 (16-18, 693) explains why that network cannot be read, substitutes XGBoost with SHAP, and converts the ranking into coaching advice. **Four of the seven joins open with a sentence that takes over, three are a heading or a caption.** The chapter's only connective that names what it carries is `Now that we have processed the data and obtained enough data for momentum and swings, we are ready to predict the future of a match.`; the S2→S3 join restates rather than links (`With our definition of momentum, we are now able to identify which player is performing better at any moment.`) and the S6→S7 join is a compliment (`Neural networks are well known for their excellent performance when working with large datasets.`). 
**309.6 words a unit, 44 a block, 262 a leaf: 3,406 words over thirteen leaves.** Unit words 106, 77, 214, 272, 237, 257, 243, 150, 220, 937, 693 (median 243; the prediction unit is 12.2 times the shortest). Block median 44, range 3 to 153, **23 of 67 blocks 19 words or shorter and 12 are 9 words or shorter** - almost all of the short ones are the k-means box, blocks 81-89 at 5 to 12 words each because each pseudocode line became its own paragraph. Block starts per leaf 6:1, 7:11, 8:6, 9:3, 10:3, 11:5, 12:7, 13:6, 14:13, 15:2, 16:4, 17:6; chapter words by leaf 2, 518, 316, 141, 186, 283, 487, 256, 316, 188, 302, 383, 28, **0** - leaf 6's two words are the title fragment and leaf 19 carries nothing of this chapter at all. **No equation in this chapter carries a number, on the page or in the layout**: the four centred displays (`M(x)`, the `G(x)` sum with its limits intact, the sigmoid with `0 ⩽ r_i ⩽ 1` on the same line, the `P(x)` sum) and the loss function are all unnumbered, so the record's note is wrong when it cites `equation (1)` and `equation (2)`. 
**Thirteen exhibits owned, nine figures and one algorithm, and not one numbered table.** Figures 4, 5, 7, 8, 9, 10, 11, 12, 13 and Algorithm 1 belong to the chapter; Figure 3 (`data-preprocessing`), Figure 6 with its reading (`results`), Figure 12's reading (`results`) and Figures 14-15 (`sensitivity-analysis`) do not. **Three numbered pointers and three of them wrong**: leaf 9 says `The core idea over the whole process is visualized in Figure 3 below.` over Figure 5's schematic, leaf 10 says `from the second set shown in Figure 4` for the curve Figure 6 holds, and leaf 16 says `as shown in Figure 8 above` for Figure 9. Every other pointer is correct by number, so this chapter cites by number and drifts by number. **Figure 12's caption labels a table, not a figure** - a coloured grid headed `Train Loss/Test Loss`, `GRU`, `RNN`, `LSTM` with rows No Transfer / Transfer with Clustering / Only Transfer with Clustering and cells from `0.01/0.09` to `0.02/0.02`, carrying no `Table N` of its own, read by a `results` paragraph as `the table (Figure 12)`. 
**Against the raster.** Nine printed headings and none of them lost, which is class 622's opposite: `4`, `4.1`, `4.2`, `4.3`, `5`, `5.1`, `5.2`, `5.3`, `6` all print as standalone bold lines with air above and below, and **six of them are stored as the last line of somebody else's block** - `4` behind two watermarks in the `display` block 32, `4.2` at the end of Figure 5's caption block 51, `4.3` at the end of 61, `5` at the end of 67, `5.3` at the end of Figure 12's caption block 93, `6` at the end of 102. Only 33, 68 and 78 are typed `heading`. **The layout loses the loss function's square root**: the page prints `L = √([Σ[P1−R1]² + Σ[P2−R2]²]/2N)` under a radical that encloses the whole bracket, while blocks 72-73 store two flattened fragments ending `... L = 2N`. **Algorithm 1 stops at line 9** (`Calculate the mean and update it as the new centroid`), the box closes there, and neither `for` loop nor the `while` is closed. The run test is read backwards - `The P value calculated by the run test is 0.000, far less than 0.05, which means the swings are random in the aspect of statistics` - and that sentence is the chapter's entire statistical evidence. The standardisation sets `α = 1, β = 0.05, γ = 0` for a formula written with `ϵ`. Figure 9's schematic prints none of the `32 + 32 + 16` / `16 + 2` numbers the prose attributes to it, Figure 13's bars print no values at all, and Figure 11's six panels carry no axis labels or ticks. 
Disagreement: counts hold, the page field is wrong at both ends, and three units have a block cut out of the middle. `Stored count 11, coded 11` resolves all 67 ids with no duplicate, and the 67 slots map onto 67 physical blocks. But `pages [6, 19]` starts one leaf early and ends two leaves late, block 102 is attributed `[17, 18]` for a paragraph that prints on leaf 17 alone, and **seventeen blocks inside the declared range belong to other chapters** (`data-preprocessing` 4, `results` 4, `sensitivity-analysis` 9) so the record routes around them by deleting slots - group 6 is `52+55+56+57`, group 9 is `64+65+67`, group 10 is `68…91+93`, with 53, 54, 66 and 92 dropped. Unit 6 is the one that matters: it announces `Figure 6 below` and both the caption and the reading it needs are the two `results` blocks the record cut out. 


| 88 | P-C-2024-2409404-a8d6763a | 6-16 (6-16) | 12 / 114 | done | **folio offset 0, `Page N of 25`** - `Team # 2409404` left, `Page N of 25` right on a rule, printed = PDF leaf on all eleven leaves (6-8, 9-12, 13-16 read by three separate audits), so `pages [6, 16]` is right at both ends: the chapter opens on leaf 6 and its last block ends on leaf 16 with the next chapter's title. **104 `body`, 9 `heading`, 1 `display`** - and the display is Table 6, a table; the heading-typed block 83 is the Figure 3 statistics table. Fourteen headings print in the range; only eight are typed `heading`. **Seven segments.** S1 units 1-2 (leaves 6-8, 544 words) defines momentum as a windowed sum of nine match statistics with window `β` and a serve discount `α`; S2 unit 3 (8-10, 692) reads the 2023 Wimbledon final through its statistics table, momentum curve and scatter, set by set; S3 units 4-6 (10-12, 877) runs a runs test and a chi-square test and declares momentum causal; S4 units 7-8 (12-14, 688) turns the momentum sign into the label `MS`, brings 43 factors through a PCA biplot and trains XGBoost on 30 matches with the observed match held back; S5 unit 9 (14-15, 348) normalises the factor importance and pairs 28 indicators into a ranking; S6 units 10-11 (15-16, 555) gives four pieces of tactical advice; S7 unit 12 (16, 46) gives the fifth and welds `6 Model Effect Analysis` onto block 182. **Six of the seven joins are headings and the seventh is a heading too.** The page check is the finding: every heading prints standalone with air above and below and its number in front (`4.1  The Runs Test —Stochastic Analysis`), and the ledger welds six of them onto the tail of the preceding paragraph (3.3 onto 81, 4 onto 91, 4.3 onto 111, 5.2 onto 132, 5.3 onto 134, 6 onto 182). **312.5 words a unit, 32.9 a block, 341 a leaf: 3,750 words over eleven leaves.** Unit words 358, 186, 692, 410, 113, 354, 457, 231, 348, 328, 227, 46 (median 338; the match read is 15 times the closing bullet). Block median 16, range 3 to 169, **71 of 114 blocks 19 words or shorter and 15 are 9 words or shorter**, and **47 blocks - 41% - begin with a lowercase letter** because they are the tail of a cut sentence; five end in a mid-word hyphen. Words by starting leaf 100, 381, 289, 466, 329, 409, 259, 399, 443, 402, 273. **Eleven numbered displays, `(1)` to `(11)`, none typed `display`.** (1) is a 12-word block whose summand has no dummy index on the page either - the same `i` is the player index and the upper limit; (2)-(6), (8) and (9) are typeset correctly and mangled only by the extractor; (7)'s braces are doubled on the page; (10)'s tag prints on top of the QR badge at the right margin, which is why it opens block 110 ahead of its own equation in block 109. **Ten exhibits owned, six figures and four tables, and the numbering holds**: every in-range pointer names its own object (Figure 3 in 82, Figure 4 and 5 in 87, Figure 6 in 118, Figure 7 in 136, Table 4 in 102, Table 5 in 110, Table 6 in 137). Table 3 is the one exhibit cited but not contained - printed on leaf 6 before the `3` heading, cited from block 116 on leaf 13. Figure captions print **below**, table captions **above**, and both are stored inside prose blocks, so the ledger loses the only signal that tells them apart. **Against the raster.** Figure 2 is clip-art with `Advantange` printed under the advantage ball; Figure 3 is a picture of a statistics table called `the graph` by the sentence that reads it; Figure 5's reference lines carry no legend and its `legend` is two continuous colour bars; Figure 6's loading arrows overprint into an illegible red pile and neither axis has numbers; Figure 7 prints no value on any of its 43 bars, its colour cut falls at the 28th bar although the 28 paired indicators are interleaved, and two clip-art icons sit on the plot; Table 5's eight sub-tables duplicate counts and permute labels (`p2W` over `p1N` rows), and no degrees of freedom or critical value prints anywhere, so `the χ2 for each test is greater` has nothing to be greater than. Table 6 floats to the top of leaf 15 and splits one sentence across the leaf boundary (`forecasting the` / `game's trajectory.`), which is why blocks 138 and 140 are cut apart. Equation (11) divides an `η`-indexed numerator by `max (FI)`. The runs test is read as `we can be 99 % certain that the alternative hypothesis, H0 will be rejected`, and `Derkovic` is named twice on leaf 9. Disagreement: counts hold and the page field holds, but the heading field does not. `Stored count 12, coded 12` resolves all 114 ids with no duplicate and no foreign block inside the range. The record's note is right about each unit's opening and closing sentence, and wrong twice: it says group 1 holds `the beta and alpha discussion` and group 3 the `Figure 3's technical statistics` in a ten-block read, both true, but it calls `the 4 heading` and `the 5.2 heading` headings although the layout stores both as paragraph tails, and it never mentions the six headings that have no typed block at all. `pages [6, 16]` is the first C chapter in this pool whose page field is correct at both ends. |

| 89 | P-C-2024-2409961-92b90752 | 6-16 (5-16 printed) | 12 / 77 | done | **folio offset −1, `Page N of 24`** - `Team # 2409961` left, `Page N of 24` right on a rule, printed = PDF leaf minus 1 on all twelve leaves (6-8, 9-12, 13-17 read by three separate audits), and the file carries 25 leaves for 24 printed pages. The record's field is therefore in printed numbers and the chapter runs printed 5-16: it opens on leaf 6 with `4 Instantaneous Scoring Rate Model` (after a stray `3.2 Data Cleaning` from the previous chapter) and ends on leaf 17 with `7 Generalization Testing 7.1 Basic Test` welded on, so `pages [6, 16]` starts one printed page late and ends exactly right - and equations (1) and (2), the tridiagonal system included, print on the page the field excludes. **71 `body`, 4 `display`, 2 `heading`** - and no display holds an equation: 70 is the heading `4.2`, 87 and 88 are two halves of Figure 7's chart, 123 is the bars of Figure 10. **Eight segments.** S1 units 1-2 (leaves 6-7, 501 words) builds the instrument - cubic spline (1)-(3), relative score curve, derivative as direction; S2 unit 3 (7-8, 277) reads it by sign, distance and server colouring; S3 units 4-5 (9-10, 468) tests independence with a central-limit argument and Figure 6's `bimodal peaks`; S4 unit 6 (10-11, 332) smooths the ISR into momentum with (4) and introduces GRU; S5 unit 7 (11-12, 121) gives five gate equations under one tag; S6 unit 8 (12-13, 177) adds player embeddings, (6)-(10) and the MSE loss; S7 units 9-10 (13-15, 746) reduces 47 dimensions to six attributes and runs integrated gradients (11); S8 units 11-12 (15-17, 941) selects twelve cheap indicators and inverts the network for `32*6` unknowns. **Six of the seven joins are headings, one is a caption, and one is a real connective** (`In this schematic, the calculation formula of each element is specified as follows:`); unit 8 opens on `Figure 9`'s caption, so a figure legend is the first thing a unit says. **296.9 words a unit, 46.3 a block, 297 a leaf: 3,563 words over twelve leaves.** Unit words 352, 149, 277, 99, 369, 332, 121, 177, 408, 338, 283, 658 (median 307.5; the closing derivation is 6.6 times the shortest). Block median 25, range 1 to 209, **35 of 77 blocks 19 words or shorter and 22 are 9 words or shorter**, twenty begin on a lowercase letter; words by starting leaf 276, 232, 263, 296, 289, 308, 132, 390, 336, 354, 446, 241. **Eleven numbered displays `(1)` to `(11)`, none typed `display`.** (2) is a tridiagonal matrix typed as running text; (5) is five lines of GRU algebra under one tag, level with the third line; (8)-(10) lose their subscripts and (10) prints its tag between them. Three defects are on the page, not in the extraction: (1)'s and (3)'s parentheses are text-height so the fractions burst out of them, (3) solves `f(t)` with a linear term in `x`, and (11) integrates over a dummy printed `a` while the integrand's variable is `alpha`. **Fourteen headings print and the ledger accounts for them five ways**: two typed `heading` (76, 82), six welded to a tail (61, 77, 83, 84, 131, 137), one typed `display` (70), three unstored as headings at all (107, 119, 126, body-size and unnumbered), and **the chapter title has no block** - `4 Instantaneous Scoring Rate Model` prints on leaf 6 and appears in no block of the 77. **Against the raster.** Figures 2 and 3 lose their plotted line behind their own markers and legend; Figure 4 is two panels whose left panel draws both players in identical black although its legend names two; Figure 4's caption reads `March Flow` and its x range is half that of Figures 2-3; Figure 6 is read as `bimodal peaks` and as a `wave peak` although it prints bars only, with at least five local maxima and no curve; Figure 7 leaves its zero line as an ordinary gridline so the sign flip the argument rests on is carried by fill colour alone; Figure 10 is the one exhibit with values printed on it (`-0.29 -0.03 0.23 -0.02 -0.31 0.02`); Figure 11 prints no value in any of its six heat maps; Figure 12's gold trophy covers the `Offensive` label on the Alcaraz card. Table 2's `Offensive` and `Skill` rows carry the same five indicators, and `Table 1` - a different table on printed page 4 - carries the same caption text. Ten figure citations, five right and five wrong (`Figure ??`, `Figure 16` three times for Figure 12, `Fig. 1`), all five wrong ones in the second half. Disagreement: the block field holds exactly and the page field does not. `Stored count 12, coded 12` resolves all 77 ids with no duplicate, no gap and no foreign block inside the groups, and the group boundaries fall where printed units fall. The page field is one printed page late at the start and the chapter title it should contain is stored nowhere, so the record codes a chapter whose own title, section 4.1 and equations (1)-(2) sit outside the range it declares. |

| 90 | P-C-2024-2410482-2f099d31 | 5-20 (4-19 printed) | 14 / 109 | done | **folio offset −1, `Page N` on a rule above the text column** - `Team 2410482` left, `Page N` right, printed = PDF leaf minus 1 on all sixteen leaves (leaf 5 prints `Page 4`, leaf 13 prints `Page 12`, leaf 20 prints `Page 19`). The record declares `pages [5, 20]` and titles itself `(pp. 5-20)`, and **those two statements describe different ranges**: the number matches the leaves, the parenthetical matches the printed series, and the chapter runs leaf 5 to leaf 20 = printed 4 to 19, so the chapter title on printed page 4 is inside the field and outside the prose. Fifteen running heads were extracted into the prose and one block off - the head opening leaf N+1 is appended to the tail of the block starting on leaf N, except block 118, a leaf-14 block that *begins* `Page 13 6 Momentum Projections,...`. **102 `body`, 7 `heading`, 0 `display`** - and the whole paper (206 blocks) contains no display at all, so all twenty numbered equations `(1)`-`(20)` are filed as prose and `(18)`, `(19)` and `(20)` share one 37-word block. **Eight segments**: 83 / 582 / 698 / 260 / 517 / 1,172 / 154 / 341 words over 6/15/20/10/17/33/2/6 blocks. 3,807 words, 271.9 a unit (median unit 247), median block 21, mean 34.9, longest 206 (block 119), shortest 0 (blocks 52 and 121, which hold only `4.1.1` and `6.1.1`), **54 of 109 blocks at 19 words or fewer and 23 at 9 or fewer**, twenty-one beginning lowercase, 48 ending without a full stop. Words by starting leaf 83, 265, 317, 204, 381, 373, 99, 241, 177, 383, 216, 273, 242, 118, 169, 266. **Twenty-one headings print and all four failure modes are the extractor's**: on the page every one stands alone with air above and below (`4.1.1` and `4.1.2` on printed page 5, `7 Extension Test` on printed page 19). Seven are typed `heading`; two are split into a 0-word number block plus a title block (52+53 = `4.1.1`, 121+122 = `6.1.1`); one keeps number and title in a 4-word body block (`4.2.1`); and eleven are welded to the tail of the block before, five of them across a group boundary - `4.1.2` ends G02 and the title opens G03 with no number, `6.1.4` closes G11 while its body sits in the other chapter, `6.2` closes block 152 in that chapter, and `6.3`, `6.3.1`, `6.3.2` close three bodies. The chapter heading is an untyped body block behind the head (118). **The chapter boundary does not match the paper's**: five blocks that print inside `[5, 20]` - Figure 4 and its reading (66-67), the momentum plot, its Chinese caption and its reading (98-100), the cross-validation table and its gloss (151-152) - are filed under a `results` chapter declared `[8, 18]`, a range wholly nested inside `[5, 20]`, and **block 100 is coded twice**, once inside `[98, 99, 100]` and once as a whole group. Chapter 7's heading prints standalone on printed page 19 and chapter 7's body starts inside block 161's tail, so G14 ends at 160 while 161-165 print in the range without belonging to it. **Against the raster.** Figure 2 is a four-quadrant diagram, not a plot, with no ticks and four numbered boxes. Figure 4 is a two-series line chart with no data labels, so the `21 games` and `38th game` readings cannot be checked off it. Figure 5's caption is the paper's only Chinese caption (`图 5:`), and the plot has no legend and no values. Figure 9's y-tick digits and both legend entries are illegible. **Figures 10 and 11 are 14x14 correlation matrices while the prose counts twelve factors**, adding `Swings of Momentum` and `Set Point(Game Point)`; they plot the same matrix twice with the numbers on opposite triangles (`figure1` upper, `figure2` lower) and one line of 6-point type reads `Significant level: 0.05`. Three tables print (score grid, regression, evaluation) and **none has a caption, a number or a citation**; the score grid is colour-coded blue and red with no legend. On the page: the regression table's `server and serve speed` interval prints `0.0052,0.0103)` with no opening parenthesis, `intercept` prints an empty interval cell, and the net-point row pairs coefficient `-0.251` with `T 0.704` and `p 0.402` against an interval excluding zero; `(17)` prints `M_t = M_t = μ + φM_{t−1} + ω_t`; `(10)` uses `γ` while the next sentence calls it `α`; `𝜔 = [0.5, 0.2, 0, 1, −0.1, 0.1]` gives six weights to five factors; `𝑟𝑡` is defined as 0 for a win and then fed to `(−1)^{𝑟𝑡}`; and the QR sticker prints inside the text column and cuts a line of body text on printed page 7. Disagreement: the block field holds exactly (109 slots, 109 distinct ids, no gap) and the page field does not - it is in leaves while the record's own parenthetical is in printed pages. Forty-eight blocks end mid-sentence or on a head, and 38 of the 109 carry a Chinese watermark (`微信号：MATHmodels`, `微信公众号：数学模型`, `关注数学模型 MATHmodels 获取更多资讯`) welded inside the paragraph it interrupted. |

| 93 | P-C-2024-2418251-0c8c04e5 | 4-18 (5-19) | 12 / 132 | done | **the page field is in leaves while the record's own parenthetical is in printed pages**: folio `Page N of 23` runs one behind the leaf, so `pages [5, 19]` is printed 4-18 and the chapter title prints on printed page 4, outside the declared range; **a nested `results` chapter at `pages [7, 18]` owns sixteen blocks that print inside leaves 5-19** - 71-75 (Figures 3-4, their captions and the serving MSE `0.012922` / `R² 0.56119`), 87-89 (Figure 7), 91 (Figure 8), 154 (the readings of Figures 11-12) and 178-183 (Table 11, Figure 14, `0.017458` / `0.66442`) - so the units skip holes inside themselves (G3 runs 70 then 76, G4 runs 90 then 92, G12 runs 177 then 184) and the three fit statistics that defend the models sit in blocks the chapter does not own [R]; the block field itself holds exactly (132 slots, 132 distinct ids, ascending, no duplicate); **the record's note for unit 2 asserts a numbering gap the page does not have** - `the equation numbering skips (7) and (8)`, while (7) prints in block 63 and (8) in block 65 inside that unit, 19 equations over 15 blocks, (5)(6) in 60 and (13)(14) in 128 and (15)(16) in 129; on the page **equation (11) prints `M_i = M_b + M_s + ΣM_c + ΣM_u` with two bare summation signs and no index**, so the per-game ledger has no stated summation domain, and **equation (16)'s matrix prints its second row as `r21 r22 r11`** with `r11` twice; **Table 8 heads both players' last column `Winning probability_P1`**, **Table 11 ends its Carlos Alcaraz forecast on `34.3283` twice**, Tables 9 and 10 close on the same `−0.654` for `Momentum_P2`, Table 5 prints `Principle Componets`, and chapter 6's Table 12 prints `Gmae_no.`; **the PCA input list names `Potential point_Serve` twice and omits `Potential point_Break of Serve`** (block 143); Figure 5's caption calls the receiver `the service player` and Figure 14's caption reads `A accumulated`; `R² 0.90142` (block 147) is scored against a quantity the chapter reports in four different units (per game, per set, accumulated, predicted); of the layout's nine `heading` blocks **six are not headings** (70, 81, 133, 165, 167 are table grids and 95 is the `• Serve:` bullet) and four of the five `display` blocks hold a watermark plus a section number or the next chapter's title; **every welded heading, split caption and flattened fraction here is extraction-side** - on the page all sixteen headings stand alone with air, Tables 2, 3, 6 and 7 line up under their printed headers (`Match_id Set_no. Game_no. Point_no. X1 X2 X3 Yp`), and Figures 11 and 12's captions, split into four fragments across blocks 150-153, each print whole [E]; 31 of the 132 blocks carry a Chinese watermark and none carries the folio, which is rendered outside the text layer |

| 94 | P-C-2024-2425454-a27c2efc | 6-19 (6-19) | 8 / 119 | done | **page base clean, offset 0** - `Team # 2425454` / `Page N of 25`, leaf 6 prints `Page 6` - so the field and the printed series agree; the neighbouring `data-preprocessing` chapter is the one that is off (field `pages [5, 5]`, its blocks 62-72 print on page 6) [R]; **the `results` chapter at `pages [9, 17]` owns 27 blocks and all 27 print inside `[6, 19]`**, so this is not a page or two of overlap but the whole chapter, and the model chapter's units skip exactly the block that reports the result at every one of its four numeric joins - 123-125 (Figure 5 and its reading), 142-146 (Figure 7 narrative), 159-170 (the `45.11%`, Table 2, `X = 5.566`, `P = 0.018`) and 196-202 (the `94%`, Table 3, Figures 12-13); **the `check` unit (147-158) states a hypothesis pair and a Z statistic and never states its verdict**, and the `derive` unit that builds the GSRF predictor (171-195) ends before the accuracy and the hyperparameters; the block field holds exactly and the groups are closed intervals (14/22/14/13/3/12/25/16 = 119 slots, 119 distinct ids, no hole inside any unit); **nine formula displays, two numbers** - only (1) and (2), both clean two-line pairs on the page, while the chapter's own definition of momentum, its leverage operator and the whole runs-test apparatus are unnumbered and the composite probability is left as `The above equation`; **three displays print wrong on the page and a fourth error sits in the sentence before (2)**: the lead-in names `ps and qs` where (2) prints `p_c`/`q_c`, the momentum fraction closes its denominator on `(1 − α)^t` with `t` defined nowhere, `P(r = 2k + 1)` prints `C(m−1, k−1)` twice and squares `C(n−1, k)`, and the alternative hypothesis prints `1P` for `1 − P`; **Figure 6 contradicts the bullets that describe it** (text 30-30 and 15-40, schematic 15-15 and 0-30), **Figures 10 and 11 carry the same caption** and it belongs to 11, **the confusion matrix prints `7 0 0 / 0 50 2 / 0 1 7`** = 64 of 67 = `95.5%` against the stated `94%` and against block 199's `none of the samples ... were categorized into another reversal point type` (two 0->1 and one 1->0), **Table 2 is cited as `Table 1`** and prints only `n11 n12 n21 n22`, **Table 3's stub row reads `Indicator Names | Values`**, Table 4 has no header row, and **Table 5 shades `brp1` on factor 2 at `0.502` while its factor-1 loading is `0.569`**; `elapsed_time` and `speed_mph` were kept among the top fifteen and load no higher than `0.253` and `0.211` on any factor; **the forest is fitted with `RandomForestRegressor` on a three-class label** two subsections after the text describes its `classification process` and `Voting`; `α = 0.33`, `N = 1000` and the grid's winning cell are asserted with no criterion printed; the indicator lists define `p1_ace`, `p1_double_fault` and `rally_count` twice each and give `p1_winner` the same definition as `p1_ace`; caption wording diverges from the body (`Short-Term Incentives` vs `short-term motivation`, `Screep`, `Rurning`, `Nomal points`, `Gridseach`); **every welded heading, split fraction and spliced watermark here is extraction-side** - all eighteen headings stand alone with air on the page and the twelve welds are the extractor's [E]; 15 of the 119 blocks are `•` fragments, 66 end without terminal punctuation and 28 carry a Chinese watermark; no block carries the folio, which is rendered outside the text layer |

| 95 | P-C-2025-2500759-cc793619 | 5-19 (5-19) | 7 / 73 | done | **page base clean, offset 0** - `Team # 2500759` / `Page N of 26`, leaf 5 prints `Page 5` - so the field and the printed series agree [R]; **three pages inside the declared range carry no text at all (printed 7, 18, 19), and the cause is a page-spanning block, not the record**: block 36 spans `[6, 8]` and the whole of printed page 7 - the four run-in lead-ins (`Feature design`, `Input feature reconstruction`, `Time series modeling and feature fusion`, `Loss function and joint optimization`) and **nine numbered displays, (1)-(5) including (4a)-(4c) and (5a)-(5c)** - lands in no block (`n_steps`, `Host_t`, `λ` appear nowhere in the document); block 123 spans `[17, 20]` and swallows pages 18-19, which hold `4 Problem 2: The ''Great Coach'' Effect`, `4.1 DID Modeling`, the brace-stacked (9) and **Table 4 `Results of the DID Model on the Great Coach Effect`** - no block contains `Table 4` or `DID`, and the paper's Problem 2 has **no record chapter at all**, so none can be written from this layout; **the word count is inflated 120% by an invisible stamp** - the field says 4,905, the text tokenises to 4,971 and **2,748 of those tokens are a single letter `m`**: a 37x37 lattice of `ArialMT` glyphs at 1.379 pt, 687 per affected page, on nine of the document's 26 leaves at measured zero ink (mean luminance 255.0, 0.00% of pixels below 128), four of those leaves inside this chapter, so 2,748 = 4 x 687 and the seven carrying blocks are that stamp cut by page boundaries (35's 501 + 36's 186 = 687; 88's 22 + 89's 365 + 90's 300 = 687) - real length **2,223 words over 73 blocks, 30.5 a block, median 13**, 45 of 73 at 19 words or fewer; **the `results` chapter at `pages [9, 20]` owns 34 blocks and 25 of them print inside `[5, 19]`** - 46-50, 77-81 and 109-123 - so the model chapter's last two units join across holes and **G7 (82-108, 27 blocks) cites no exhibit at all** while all six figures that report it (8-13) are captioned and read inside `results`; the block field holds exactly (73 slots, 73 distinct ids, ascending, closed intervals 26-29 / 30-31 / 32-36 / 37-40 / 41-45 / 51-76 / 82-108, no hole inside a unit); **not one block is typed `heading` or `display`** - all 73 are `body`, so eighteen printed headings are invisible and eleven are welded onto a preceding paragraph; **22 displays print in range and 13 are numbered, and only (6), (7) and (8) reach a block**; **four printed defects sit in the displays**: (8)'s own `t = |ρ| / sqrt(ρ²/(n − 2))` cancels to `sqrt(n − 2)` and cannot depend on rho, its rejection region prints `t > t_α(n − 2)` under a two-sided `H₁ : ρ ≠ 0`, `P-value = Φ((w⁺_j − μ_j)/σ_j)` is the upper tail only under `H₁ : θ_j < 1`, and the prose writes `w_j` where the display prints `w⁺_j` (the same `w` also labels the Spearman rejection region); **Table 3's top two statistics exceed the test's own maximum** - `GRD 538231` and `GHA 532048` against `1000 x 1001 / 2 = 500500`, with no effective `n` printed - and **MKD and BFA print identical `153243` / `1.22e-26`**, **Table 2 prints `AUS 19 (10.41, 16.13)` and `NZL 11 (4.82, 9.33)`, two intervals that exclude their own point estimates** while the other 38 hold, and **the p column is re-read as `probabilities of 0.847 and 0.684` with a larger p rewarded as better news** (`a larger P-value indicates a smaller probability of committing a Type II error`), against a table whose own largest p-values are the two rows the prose excludes; **Figure 5 grades the model on `MSE, MAE` where the chapter's metric is WMAE (6)**, **Figure 10 is a 15-row two-column table captioned as a figure** with two identical `Sports` headers and dotted labels (`3x3.Basketball`), **Figure 9 is announced as `the hexagonal importance mix plot` and is a beeswarm** whose two panels order the components differently, **Figure 8 quotes `0.210` below the bottom of its own colourbar for a sport (`Karate`) with no column**, and **Figure 4 stacks WMAE_Gold on WMAE_Total and plots per-`hidden_size` minima while the prose names `32x6` and `128x10`** (its numbers do match Fig. 3 exactly: `6.31/3.78`, `9.64/3.73`, `6.12/3.19`, and all six Fig. 3 rings mark true minima at 400 dpi); the exhibit numbering starts at 2 - **no Figure 1 and no Table 1 exist anywhere**; `Wlicoxon` in block 76; the prose calls France and the USA `the upcoming host nations, France in 2024 and the USA in 2028` in a January 2025 paper; **every weld, split fraction and spliced watermark here is extraction-side** - on the page all eighteen headings stand alone with air and (6), (7), (8) print as clean numbered displays [E]; 31 blocks begin lowercase, 57 of 73 end without terminal punctuation, 5 carry a Chinese watermark, and none carries the folio, which is rendered outside the text layer |

| 96 | P-C-2025-2501869-dbf7e00e | 6-21 (6-21) | 8 / 75 | done | **page base clean, offset 0** - `Team # 2501869` / `Page N of 25`, leaf 6 prints `Page 6`, so field and printed series agree [R]; **three leaves of the range are single full-page bitmaps, and every section on them is ink only** - pages 13, 15 and 20 (page 2 likewise, outside the range) are each one 1654 x 2339 inline image at 200 ppi with header and folio baked in, so `5.5 The Influence of Item Selection on the Number of Medals` and **Tables 5 and 6** (p13), **Figure 8**, its caption, `5.5.3` and the prose introducing Figure 9 (p15), and `6.2`, `6.2.1`, `6.2.2`, both `Step` labels, **equations (11) and (12)** and the unfilled placeholder `(cited literature)` (p20) exist in no text layer - `6.2` occurs **zero** times in the 123,402-byte text layer, and a text-only reader drops from `5.4` straight into `5.5.1`; the record is therefore missing no section, and the layout's page spans (103 `[12, 14]`, 144 `[19, 21]`) are how it steps over leaves that never had text, which is also why p15 starts no block; **the word count is inflated 94% by a dead vector twin** - the field says 4,247, and **2,061 tokens are single-letter `m` runs**, exactly 687 per affected leaf on printed 7, 8 and 10, cut by block boundaries into 53 whole, `22 + 222 + 443` across 56-58 and `38 + 649` across 83-84, measuring **zero ink at 400 dpi** (mean luminance 254.8-255.0, 0.00% below 200) because the run is a pgf/TikZ chart scaled to 13.8% and then painted over by the raster of the same figure, so real length is **2,186 words over 75 blocks, 29.1 a block, median 14**; **the layout's `display` type is used exactly twice in the whole 212-block document - blocks 98 and 151 - and both are 687-token runs of that twin**, so a display count taken from `kind` returns zero while twelve numbered displays actually print, **ten of them inside owned blocks** (1-8 in 54/62/65/69/72/75/77/79, (9)-(10) both in 138) and (11)-(12) on the raster leaf; **44 blocks print inside `[6, 21]` under other chapters** (33-41 `data-preprocessing`, 86-110 and 128-133 and 148-151 `results`), so `5.4`'s heading block 102, `5.5.1`'s body block 103, Figure 6's caption 99, Table 1's block 33 and the accuracy table's own rows 91-92 all belong to other records; **only three of the twenty printed headings are typed `heading`** (42, 43, 134, all correct), five print only on the bitmap leaves and twelve survive as welded tails; **Table 8 prints stars its own SDs exclude - about 28 of 61 starred cells, in both directions** (`3.42***` on `4.57` at t = 0.75, `1.828**` on `1.42` at t = 1.29, against `4.145**` at t = 23 and `0.745*` at t = 3.39), `Athletes [0,10]` carries an SD of exactly `0`, **`Observations noncensored 554` equals `Observations total 554`** in both Hurdle models, and five coefficients print digit-identical across two specifications with different SDs; **Tables 6, 8 and 11 report the same models with three different sets of numbers** (`529 / 1232` against `554 / 1289`, `Host country t` 1.566/12.520 against 1.354/5.520), Table 6 printing its `Medals_PCA(t-4)` row **twice**, copying `RCA`'s Tobit cells `1.828** / 1.07` into `Num_Events` and leaving `Constant` with no estimates, while Table 11 prints `2.314***` where Table 8 prints `9.314***` and relabels Table 8's `RCA` row `Medals_PCA`; **Table 1's own components sum to 5.03** against its printed `Total Medals` mean of `11.42`; **Table 3's Great Britain row prints `68` forecast with `63` lower and `53` upper**, the only interval in the table that fails to bracket its estimate, and its column mapping is recoverable only from the page [E]; the accuracy table under Table 3 has **no number, no caption and no column headers naming Hurdle or Tobit**, its parenthetical percentages are undefined and its note asks for bold forecasts in a table that has none; **Figure 10 is an unattributed screenshot of `Well-Log Data Set` and `Global Surface Temperature Anomalies`** presented after the sentence `Such obvious turning points can be identified using a Bayesian change-point detection`, **Figure 11 repeats Figure 10's caption** and marks `1996 Atlanta Olympics (Mary Lou Retton)` where Table 9 puts the gymnastics change point at `1984`, **Figure 8's legend names `Modern Pentathlon`/`Fencing`/`Weightlifting` for a three-colour stack repeated across ~33 disciplines and `Modern Pentathlon` is not on its axis**, **Figure 7's caption names RCA and no panel plots it**, Figure 6 has no legend and 4-5 pt colliding labels, Figure 5 carries two unlabelled dashed ellipses and inconsistent axis titles, Figure 4 prints no cell values so the `Modern Pentathlon` claim is checkable from neither exhibit, and Figure 12's caption and legend say `SLS` where the prose says `2SLS`; **(9) is a 3x1 times 1x3 outer product assigned to a scalar** and (10) sums `S_{t-4,i} e^{-i}`, mixing window and decay indices, with `a`, `b`, `c`, `K` and `N_Total` defined nowhere, while (2) **runs 72 pt past the text measure** so its last subscript is cut and its number drops to its own line; the gloss `c, lambda, rho, gamma, delta, zeta, kappa in R^3` puts seven scalars in a 3-vector; a bullet prints `which may affect its statistical significance, which may affect its statistical significance`; every weld, split heading and spliced watermark here is extraction-side [E] - on the page all five headings of pp. 6-11 set normally with their numbers spaced; 17 blocks begin lowercase, 48 of 75 end without terminal punctuation, and 12 carry Chinese watermark or sticker-label text, five of them splicing mid-sentence |

| 104 | P-C-2025-2514362-c904f1a9 | 7-17 (7-17) | 4 / 67 | done | **folio runs one behind the leaf** - `Team # 2514362` / `Page N of 26`, leaf 7 prints `Page 6`, so the record's pages 7-17 are printed 6-16 [R]; **the chapter is three islands and four of its own section titles are filed under other chapters** - group 1-2 print on leaf 7, group 3 on 10-12, group 4 on 15-17, and **37 blocks of other chapters print inside the declared range** (29 `results`, 6 `sensitivity-analysis`, 1 `assumptions`, 1 `notation`), of which results block `73` carries `4.2 Zero expansion negative binomial model (ZINB)` with `4.2.1 Model selection background` and sensitivity block `120` carries `5 Entropy model based on Bayesian Modification` with `5.1 Model Selection Background`; the document's own Section 4 title is filed under `assumptions` (block `46 [5, 7]` ends `Multi-level integrated forecasting model` with the number `4` dropped) and `4.1.3 Case Analysis` is welded to the tail of notation block `58`, the block that holds Table 1; **the chapter ends on a heading it does not own** - `4.2.3`'s number closes chapter block `104`, its title is results `105` and its finding (Cyprus 58.2%, Fiji 42.1%, Kuwait 33.5%) is results `106`, and `5.3 Case Analysis` closes the last block `145` the same way; **the model the chapter is named after is a table row, not a display** - `log(µ_it) = β0 + β1 History^w + β2 Host + β3 ΔE + β4 TimeTrend + β5 ColdWar + u_i + v_t` with `β1 ~ N(0.8, 0.1)`, `β2`-`β4 ~ N(0, 0.1)`, `β5 ~ N(0.15, 0.1)`, `u_i ~ N(0, σ_u²)`, `v_t ~ N(0, σ_v²)`, `σ ~ HalfNormal(1)` and the WMAE that `(1)` minimises exist only inside `Table 1` (notation block `58`, leaf 8), so **not one of the 21 numbered displays is that model**; **the chapter cites one exhibit in 67 blocks and it belongs to another chapter** - block `53` says `The specific formulas and limiting factors are shown in the Table 1.`, no block contains the word `Figure`, fourteen exhibits print on the declared leaves, and the record gives the chapter `select` plus three `derive` with no `read-table` job anywhere; **history is weighted twice in two incompatible ways** - Table 1's `History^w` is a normalised average over the last five Olympics, `Σ e^{−λ(k−1)} Y_{i,t−4k} / Σ e^{−λ(k−1)}` with `λ = 0.6`, while `(9)`'s `Athletes^w` is an unnormalised sum over the last three, `Σ_{k=1}^{3} e^{−0.5k} N_{i,t−4k}`, whose weights total `0.6065 + 0.3679 + 0.2231 = 1.1975`, so the chapter's own covariate runs 20% larger than the counts it adds; the only tuning is a three-point grid under one number, `λ = 0.4 → WMAE = 12.3`, `0.6 → 11.8 (Optimal)`, `0.8 → 12.6` (optimum is the middle candidate), and the tuned value is then baked into the feature as a constant; **two terms enter `(18)` undefined** - `(15)` defines `P_progress` and `(16)` its complement, but `P_progress|x` and `P_non-progress|x` print in `(18)` and appear in no equation, gloss or table, while the one weight that is written down, `(N_x + 1)/(N + 2)`, is the smoothed marginal and is consistent with `(15)`'s `+1/+2`; **the priors bind in one place and not another** - the results quote `β1 = 0.85`, `β4 = −0.12` and `β2 = 0.3`, which are 0.5, 1.2 and 3.0 prior standard deviations from their prior means, and the `σ_u = 0.2` they quote belongs to the mixed model in Table 1 while `(2)`-`(4)` carry no random effect at all; **1,374 of 3,121 tokens are the invisible `m` stamp (44.0%)** - 687 alone in block `57`, **the chapter's only `display`-typed block and not a display**, and 687 woven inside block `123` between `Laplace smooth-` and `ing mitigates bias` - leaving **1,746 real words over 67 blocks, 26.1 a block, median 17, longest 148 (`74`), shortest 0 (`57`)**, with **55 of the 67 blocks carrying no terminal punctuation**, 39 at 19 words or fewer and 15 at 9 or fewer, because five prior bullets become 19 blocks (80-98) and six run-in sub-headings become tails (`126`, `128`, `130`, `135`, `138`, `142`); four displays are cut in half mid-formula (`(17)` opens `H(M) = −` at the end of `131`, `(18)` opens on a bare `( Nx + 1 )` fraction, `(20)` and `(21)` lose their denominators), and on the page all four are single displays with the number flush right, `(4)` is a proper two-branch brace system, and `(21)` reads `S = IG × (1 − M^current/M^max)` [E]; the Chinese watermark string survives inside eight blocks (`49`, `51`, `74`, `76`, `79`, `135`, `138`, `142`), a QR panel overprints body text on leaves 8 and 14, every figure is a pasted bitmap whose in-image title disagrees with its caption in two cases (`Prediction vs. Actual` over `Predicted vs. Actual Gold Medal`; `Gold Medal Prediction Analysis` over `Olympic Gold Medal Predictions Analysis`), the two panel titles on leaf 9 are filed as block `65` immediately before Table 2's caption in `66`, and the Figure 8 and Figure 9 captions arrive in the reverse of their printed order (68 = Figure 9, 69 = Figure 8); **no leaf of 7-17 is a raster** - the five bitmaps are leaves 2, 6, 18, 21 and 27, and leaf 6 is the assumptions page the record already flags |
| 103 | P-C-2025-2513314-911e0476 | 7-14 (7-14) | 6 / 29 | done | **page base clean, offset 0** - `Team # 2513314` / `Page N of 22`, leaf 7 prints `Page 7`, so the record's `(pp. 7-14)` is right [R]; **the chapter is two islands five leaves apart and its own results chapter prints between them** - groups 1-3 sit on leaves 7-10 and groups 4-6 on leaves 13-14, and blocks `79`-`119` (41 `results` blocks carrying 5.3, 5.4, 5.5, Tables 2-4 and Figure 4) fall between `78` and `120`, so 67 of the 96 blocks overlapping the declared range belong to other chapters (43 `results`, 23 `data-preprocessing`, 1 `notation`) and two more results blocks (`134`, `135`) print inside it; **five of 22 leaves are full-page inline bitmaps** (2, 6, 9, 16, 17; zero text objects) and two carry chapter-adjacent content the text layer never sees - leaf 6 holds `4.1`, `4.2`, **Figure 3** and the `5 Task 1`/`5.1` titles, and leaf 9 holds **equations (8), (9), (10)** plus the run-in headings `Predictive Uncertainty and Discrete Outcomes.`, `Breaking the Ice Probability.`, `Uncertainty Measures for Medal Allocations.` and `Interpreting Regression Coefficients.` inside block `78 [8, 10]`, so the layout jumps `(7)` to `(11)` and the page is continuous 1 to 12; **every caption in this paper prints above its object** - the first pack in the lane where a caption-first rule reads correctly - which exposes the opposite defect: **`Table 4` is captioned, cited in `118` and `119`, quoted cell by cell and exists in no layout block on any leaf** (32 coefficient rows for the US, China, the UK and France, 128 printed numbers; `118` quotes the US `X7` `0.03123`/`0.98` and `119` the UK `X5` `0.02678, 95% CI: [0.00228, 0.05128]` and the French `0.02631`, all of them exact), so the paper's coach recommendation rests on a table a text-only reader never sees; **`Figure 5` does not exist** - captions print `Figure 1`, `2`, `3`, `4`, `6` and no `Figure 5` appears in any of the 22 leaves, while tables run 1 to 8 without a gap; **the model is specified with a constraint it never enforces** - `(5)` sets `θ_i = φ_i exp(x_i^T β_i)` and calls it the Dirichlet-Multinomial probability vector, but nothing divides by `Σ_j φ_j exp(x_j^T β_i)`, so as printed the multinomial parameter is an unnormalised positive number [E], and `τ` appears once inside `(2)` (`Σ_β = τ² I_p`, `τ² = 1`) and again never, while `Table 1` on leaf 5 lists seven symbols and not that one; **the evidence is chained table to table and breaks at each hop** - in `Table 2` `RMSE` and `√MSE` disagree for all six models in the All-Medals block by 0.01-0.07 while the Gold block's two columns agree to the digit, so the implied residual variance moves 45% and 34% inside fixed-RMSE rows, XGBoost beats the RNN on R² (0.84 vs 0.83) while losing on MSE (7.21 vs 7.05), and the adjusted-R² gaps of 0.01-0.05 imply no single (n, p); `Table 4` prints 8 of its 32 intervals at 0.86-3.30 standard errors instead of 1.96, three of them not centred on their own point estimate (US `X3`, UK `X1`, France `X1`); `Table 3` prints Haiti's interval as `[0.2112, 0.0.2698]`, two decimal points, so the lower bound exceeds the upper bound as printed; **1,374 of 2,442 tokens are the invisible `m` stamp (56.3%)**, 687 glyphs at 1.38 pt, alpha 0, on a 37x37 lattice in a 68 pt square, all of it in groups 1-3, which is why `65` is filed at 749 words and `73` at 319 against a chapter of **1,068 real words over 29 blocks, 36.8 a block, median 36, longest 77 (`121`), shortest 2 (`72`)**; **three blocks are `heading`-typed** (`64`, `120`, `126` at 17.2 and 14.3 pt) and no block is `display`-typed, so all nine displays that reach the layout are `body`-typed; the paper's run-in sub-headings are 12 pt body size inside the paragraph (`Model Setup.` inside `68`, `Posterior Distribution.` inside `69`), so `68` opens on the orphan fragment ` be the observed medal` with the heading welded behind it although the page reads in the correct order [E]; `78` ends on the Chinese watermark and the welded next heading `5.3 Projects of LA 2028`, and `6.2 Great Coach Affect the Medals` rides results block `134`; **footnote 1 is split from its own marker** - the text is welded into `123` as an unmarked clause, the marker closes `119`'s `improve their medal tallies. 1`, and the page sets it as a real 10 pt footnote at the foot of leaf 13 behind a partial rule [E]; **the coach half is sound and the medal half is not** - `(11) A = 6G+3S+1B` and `(12) X9 = Σ A_i` are used as defined, `1,103` coaches with `697` active match the two-or-more-countries rule, the six breakthrough probabilities average 0.4406 against a total-group 0.2895 as the prose claims, and `Figure 4`'s prose figures track the real 2024 tallies (US `126`->`146`, `40`->`53`; GB `65`->`60`, `14`->`12`; France `64`->`54`, `16`->`12`) - so the paper's data handling is clean where a table is arithmetic and broken where a table was rescaled from another table |
| 102 | P-C-2025-2510862-925774c8 | 6-20 (6-20) | 6 / 121 | done | **page base clean, offset 0** - `Team # 2510862` / `Page N of 25`, printed = leaf, so the record's `(pp. 6-20)` is right [R]; **four of the document's leaves are single full-page inline bitmaps** (2, 9, 16, 21, each `BI /W 1700 /H 2200` with zero text objects and zero paths), **one of them is chapter content the text layer never sees** - leaf 9 prints equations **(4)**, **(5)** and **(6)**, the headings `5.2 Prediction for the Olympics in 2028` and `5.2.1 Projections for the medal table in the Los Angeles, Olympics in 2028`, **Figure 4** (`Prediction for medal table in 2028`, a bitmap of the table: USA `56 41 36 133`, CHN `33 30 27 90`, AUS `25 20 28 73`) plus a gloss paragraph, while block `148 [8, 10]` steps over the leaf so the layout runs from `The integration formula is:Equation 4 Equation 5` straight to `R2 = 1 − (7)` - restore the leaf and the numbering is continuous 1 to 10, which makes **the one number missing from the whole 25-page document (11)**; **the extraction cuts at printed lines, so 121 blocks are a line count** - 103 blocks of 19 words or fewer, 23 of 9 or fewer, 102 without terminal punctuation, splits inside words (`110` `Light-` / `111` `GBM`, `105` `By com-` / `106` `bining`, `121` `pat-` / `123` `terns`), 1,935 real words over 121 blocks = **16.0 a block, median 13**; **three blocks are `heading`-typed, the first in this lane** (91, 92, 208), and yet four of the chapter's own section numbers and its task titles ride `results` blocks - the number `5.2.2` ends chapter block 153 while its title `Include prediction intervals for all results.` opens results block 154, and `6`, `7`, `7.1`, `7.3` and `8` ride 174, 192, 193, 204 and 207 although `8 Task 4` prints own-line at 1.5x bold; **the record's `select`-to-`derive` boundary is not a section boundary** - 118 ends `to avoid overfitting.` and 119 opens `By minimising this objective function, LightGBM optimises the parameters of the`, so the cut falls inside the first base model; **the six `display`-typed blocks (223-228) are one flowchart's boxes and not one equation**, so all eleven numbered displays that print are `body`-typed; **1,374 of 3,236 text tokens are the invisible `m` stamp** (42.5%), in 118 (687, the LightGBM where-clause), 213 (566 in four runs, the PSM-DID motive) and 214 (121, behind the bold pseudo-heading `Selection of Explanatory Variables, Explained Variables and Control Variables`), and the Chinese watermark prints inside seven blocks (93, 101, 148, 216, 222, 225, 265); **(4) and (5) are the same formula** - `f1(x_i) = y_i^LGBM = Σ_t f_t(x_i)` and `f3(x_i) = y_i^XGBoost = Σ_t f_t(x_i)` - while (6) weights four base learners separately, so two of the ensembled models are identical by construction; **`234` prints `In our data, the PSM model is:Equation 14 (13)`** in front of `P(greatcoach = 1|X) = logistic(Xβ)`, with both the words and the number on the raster, and `(14)` on the next leaf prints `Medal = β0 + β1 · DID + ∑ β2 · Control + β3 · time + r_i + ε_it` - a bare sigma with nothing to sum, four betas at body size on the baseline while `r_i` and `ε_it` on the same line are true subscripts, and `DID` as a single symbol where the gloss below defines it as `r_i × time`; **the chapter's only quantitative exhibit is captioned `Figure 5: Model evaluation results` while the sentence that introduces it says `The calculation results are shown in Table:`**, and the document contains exactly one numbered table (`Table 1`, two chapters earlier), so the grid cannot be cited by number anywhere; **that grid cannot be true** - `MSE/(1-R2)` gives five target variances (`0.53/0.22 = 2.41`, `0.62/0.27 = 2.30`, `0.37/0.14 = 2.64`, `0.39/0.16 = 2.44`, `0.32/0.12 = 2.67`, a 16% spread at a standard deviation of 1.5 medals), and the printed `MAPE 0.30` beside `MSE 0.32` needs a mean absolute error of 0.57 medals against an average country total above 189, where the same document prints 2024 gold counts of `40`, `40`, `18`, `20`, `16` and `15`; **the PSM-DID half is set up in full and never estimated** - treatment group, control group, `(13)`, nearest-neighbour matching, parallel-trend test and `(14)` - and it ends on `If significant and positive, it indicates that great coaching has a positive effect on the change in the number of medals won by USA Gymnastics.` with no coefficient, standard error, p-value or sample size in 121 blocks (`significan` occurs twice, both times inside that conditional), while the `Number of athletes` and `host country status` controls named in a bullet never return; **Figure 15 is one numbered figure holding two panels drawn on `Probability Density` scales of `2.00` and `5` over two different score ranges**, so the before/after comparison is made at two magnifications and the after panel's range excludes treated scores near `0.9` that the before panel shows - read at that detail the peaks are what separate (control near `0.25`, treated near `0.9`) while the shaded tails do cross between roughly `0.45` and `0.75`, and after matching the centres coincide while treated peaks at about `5` against the control's `3`; Figures 3, 4 and 14 are printed and never re-cited; the flowchart's own typos print (`Logist`, `asthe`, `hypothesisand`, `A symptotic`, `difierence`, `estimationis`, `matehed`) and its `No` label runs bottom-to-top |
| 101 | P-C-2025-2510185-3f933168 | 7-20 (7-20) | 6 / 69 | done | **page base clean, offset 0** - `Team #2510185` / `Page N of 24`, printed = leaf, so the record's `(pp. 7-20)` is right here [R]; **three of the span's fourteen leaves are full-page inline bitmaps** (10, 13 and 16, each `BI /W 1700 /H 2200` with zero text objects and zero paths) and two of them carry chapter evidence the text layer never sees - leaf 10 holds Figure 6 (three actual-vs-predicted panels), **Table 6** (`Performance Evaluation of Three Prediction Models`, R2 0.8063/0.8764/0.8792) and two paragraphs on 5-fold cross-validation, leaf 13 holds **Table 8** (15 countries by 9 columns of bounds), the heading `3.4.1 BP Neural Network Classifier`, its opening paragraph and Figure 8 (ROC, area 0.94), while leaf 16 is a raster of an ordinary typeset page; **the record's `Table 6 with the United States 50 and 137, China 39 and 90 and the intervals` is not Table 6** - it is the captionless skeleton of Table 8's gold columns printed mid-block in the flowchart soup of 76 (`43.47 55.22`, `30.84 42.18`, `13.40 28.54`, `11.28 23.06`, `10.66 32.53`, all exact at two decimals), so one exhibit is printed twice at two precisions and the caption loses its number; **twenty headings print own-line and none is a block** (zero `heading`-typed blocks), nine welded onto chapter tails, **five onto foreign blocks** - `3` onto `51` (`data-preprocessing`), `3.4` onto results 94, `3.5` onto 99, `4`/`4.1` onto 129, `4.3`/`4.3.1` onto 140 - and `3.4.1` exists only as ink on leaf 13; **no `read-figure` or `read-table` job** among the six (all derive/select) although 13 exhibit numbers are cited; 2,409 of 4,313 text tokens are the invisible `m` stamp (layout over-counts prose by 113%, 4,056 against 1,904 real words), whose visible twin is 689 half-opacity crimson cells on the even leaves 4-24; Table 7 prints Australia `17 15 17` as `50` (row sums 49) with a `-3` delta that then agrees with the wrong total, and the USA delta `+11` where `137 - 127 = +10`; Table 8 declares its Total intervals `predicted separately` and then breaks it by whole medals - nine of thirty offsets are `6.0`, `11.0`, `10.0`, `-4.0`, `-5.0`, `-8.0`, `-10.0`; Table 13's `Total` column is Table 14's predicted continuous total (5 values recurring verbatim) printed under gold/silver/bronze cells of zero, and Table 14 sums `0.57 + 0.45 + 0.72` to a printed `1.41` with China's men's swimming rows a byte-copy of its men's gymnastics rows; `0.288` becomes `28.8% to overall performance` with no denominator, and the EPI's `w1 w2 w3` are never assigned or fitted |
| 100 | P-C-2025-2510006-a0fb3dfb | 7-19 (8-20) | 8 / 111 | done | **page base offset -1** - footer is `Team # 2510006` over `Page N` with printed = leaf - 1 (leaf 8 prints `Page 7`, leaf 23 prints `Page 22`), 29 leaves total, so the record's leaves 8-20 are printed 7-19 and its heading parenthetical `(pp. 8-20)` is written as if printed equalled leaf [R]; **five of 29 leaves are full-page inline bitmaps** (2, 6, 7, 18, 21, each `BI /W 1700 /H 2200` with zero text objects and zero paths) and three of them carry chapter content - 6-7 hold the printed heading `3` and the assumptions list the text layer never sees, so the chapter's first machine-readable sentence is the fragment `participate in the previous Games.`, and leaf 18 holds Figure 20's heat map plus `5 Task 2: Great Coaches` and `5.1` inside the span of block 167 `[17, 19]` (group 7), while **the record's only `read-figure` job is filed on group 6, the one group with no exhibit**; 11 foreign `results` blocks print in range (103, 104, 151-159) holding Figures 16-19 and the old/new-event combination; one `heading` block (183) and one `display` block (134, four welded captions) in 111, so all 20 displayed equations are `body`-typed and none is numbered or cited by number; 4,125 of 7,882 text tokens are the invisible `m` stamp (687 glyphs at 1.38 pt, alpha 0, on leaves 9-11, 15, 16, 19, 20, 23) whose visible twin is 688 half-opacity crimson cells on leaves 8, 10, 12, 14, 16, 20, 22, 24, 26, 28; the 2028 US forecast is exact at both stages (`53.64 51.43 31.56 136.63` and `0.937 0.735 0.706 2.378`) and wrong in the addition - `31.56 + 0.706 = 32.266` printed as `32.37`, so the three colours sum to 139.10 against the claimed 139 - while all four coach P-values reproduce from `P = 1 - alpha`; Table 2 `generally increased` sits over `9, 6, 4, 8, 7, 0, 0, 4, 3, 10, 7`; Table 5 is captioned `Table Title`; `0.75 medal points` needs 1.5/2 where the printed rule gives 1.5/1; heat-map axes are not the chapter's six categories |
| 99 | P-C-2025-2507817-87c90f39 | 6-20 (6-20) | 8 / 125 | done | **page base clean, offset 0** - `Team#2507817` / `Page N of 25`, printed = leaf, so the record's pages 6-20 are printed 6-20 [R]; **two leaves of the range are full-page inline bitmaps** (10 and 11, each one `BI /W 1654 /H 2339` with zero XObjects) and they carry the chapter's own quality metrics - Figures 6, 7, 8, Tables 3, 4, 5, 6 and equations (3), (4), (5) - while spans 129 `[9, 12]` and 130 `[12, 12]` step over both; **63 foreign blocks print in the range** (9 `data-preprocessing` on page 6, 54 `results` on 9-12 and 14-16) holding Tables 7-11, the residual tests and the logistic coefficients, and two of the chapter's own headings live in them; no block typed `heading`, two `display`-typed blocks neither an equation, equations (0)-(16) all `body`-typed; 2,065 of 5,414 layout tokens are the invisible `m` stamp (1.62x) whose visible twin is 688 half-opacity crimson vector cells per leaf; Table 2 gold row sums 100.11%, `Recall 0.841` is `Accuracy 0.841` copied, interval `y +/- 15` where 1.993 x 7.123 = 14.20 |
| 98 | P-C-2025-2505964-9dbe18d6 | 14-24 (14-24) | 10 / 53 | done | **folio runs one behind the leaf** - `Team # 2505964` / `Page N of 24`, printed = leaf − 1, so the record's pages 14-24 are printed 13-23 [R]; **the record's heading names a subsection that never prints** - `3.1.6 to 3.4 Model Construction` while the range opens mid-sentence at 3.2.2 and 3.3.1, 3.3.2 and 3.3.4 are absent; **29 foreign blocks print inside the range** (59-67, 73-83, 94-99, 108-109) and hold the swimming fit, the elasticity series, the LOO tests and the USA/China regressions; **two leaves of the range and one before it are full-page inline bitmaps** (layout 13, 16, 20 = printed 12, 15, 19, each one `BI /W 1700 /H 2200 /BPC 8 /CS /RGB`), carrying Figure 8, Figure 11, Figure 15 and all of Table 5 - the Poisson 0.1912 / NegBin 0.2378 / ZIP 0.1626 comparison - while spans 52 `[12, 14]`, 68 `[15, 17]` and 83 `[19, 21]` step over each; two `display`-typed blocks, neither an equation, six equations all `body`-typed and unnumbered; 2,061 of 3,333 layout tokens are the invisible 687-span `m` stamp (blocks 54, 68, 93), 2.48x inflation; the same swimming data is fitted twice with different coefficients, Table 6 prints 10 gold in 5 events, and `an average of 1.16` is the mean of 2 and 1.33 |
| 97 | P-C-2025-2503389-d13d77af | 6-21 (6-21) | 14 / 127 | done | **page base clean, offset 0** - `Team # 2503389` / `Page N of 26`, leaf 6 prints `Page 6`, so field and printed series agree [R]; **three leaves are single full-page inline bitmaps** - pages 10, 17 and 18 are each one `BI /W 1654 /H 2339 /BPC 8 /CS /RGB` image with zero XObjects and zero vector paths, Letter inside an A4 document, baselines skewed and watermark baked in, so page 10 (`5.4`, `5.4.1`, `5.4.2`, **Figure 6** with its (a)/(b) subcaptions, the `Lower Bound = Percentile(2.5)` display), page 17 (`7.4`, `7.4.1`, **Table 9**) and page 18 (all of `8`, `8.1`, `8.2`, `8.2.1`, `8.2.2`, `8.3` and the `Φ = Σ wi Ni` weighting display) exist in no text layer; the layout steps over them with `100 [9, 11]` and `162 [16, 19]`, so a text-only reader goes from Table 3 to Table 4 and concludes 5.4 does not exist; **the word count is inflated 2.66x by an invisible QR** - the field says 7,373 and **4,809 tokens are single-letter `m` runs**, seven runs of exactly 687 on pages 7, 8, 9, 11, 14, 15 and 20, each 687 `ArialMT` spans at 1.38 pt on a 37 x 37 grid in a 68 pt square drawn at fill alpha zero, measuring mean 255 and dark fraction 0.0000 at 130 dpi, so real length is **2,767 words over 127 blocks, 21.8 a block, median 13**, and blocks 79 and 89 are the run alone; **the layout's `display` type fires four times and only once on an equation** (81, the `XHost` piecewise), while sixteen displays print and **not one carries an equation number**; the chapter is the most fragmented in the lane - 84 of 127 blocks at 19 words or fewer, 28 at 9 or fewer, 97 of the 125 text-bearing blocks with no terminal period, one unit printed as eighteen dash-led fragments; **only one block is typed `heading`** (122) while twenty headings print, one of them (`7 Strategic Importance Assessment Model for Olympic Sports`) inside block 140 that the layout types as `display` and whose text is the watermark string; **44 blocks print inside `[6, 21]` under other chapters** (68-72 `data-preprocessing`, 97-99 and 155-162 `results`), among them Figure 1's caption, Figure 10's caption and Table 8's three reading bullets; **the three contribution values are the same number** - `0.3/DUSA`, `6.9/DUK` and `1.3/DCHN` all print `= 1.7`, requiring denominators of 0.176, 4.06 and 0.76 that appear nowhere, and the paper reads the identity as evidence of convergence; **Table 6's LR row contradicts itself in three columns** - `88.09%` beside `4:1 (80% chance)`, where its own column gives 7.39:1, while RF's `94.12% -> 16:1` is exact; **Table 7 credits its 40/30/20/10 weights to PCA with expert validation and reports no PCA at all**, and gives three indicators a `x 100%` formula and `LAS = 1 - σ/μ` none, so three inputs enter the weighted sum on 0-100 and one on 0-1; **Table 10 gives UK Cycling to Dave Brailsford and the next page attributes it to Keiko Kageyama twice**; **Table 4 reports a `Multivariate Linear Model` with no intercept row** and never discusses its largest coefficient (Host Boost 13.10); `wMLR ≈ 0.6` implies MLR has the lower error, which the sentence after it denies; **Figure 2 reports `XHist` correlating 1.00 with the target** and the caption names three variables for a four-variable matrix, and the chapter ensembles instead of dropping the variable; Figure 9's modal bar is at 3 while its median marker is at 4 and only the bar reaches the prose; 125 says `5 countries` for 2020 where Figure 8's bar reads 6; Table 3 is captioned `2024 Olympic Medal Predictions` while the prose uses 2024 as the past baseline and Figure 6 runs to LA 2028, its rank-Δ column prints `-` for all of the top six, and 100 cites `Slovenia (1 gold, CI: 0-2)` from a table that stops at rank 10; **Figures 11-13 print `Caption for Britain`, `Caption for USA` and `Caption for China`** in a font unlike the body; `Table 1` is the only exhibit the chapter cites but does not own, printing on leaf 5; `relative to global performanceBernard2004` leaks a raw BibTeX key; every weld, split heading and spliced watermark here is extraction-side [E] - on the page Table 2 keeps its brace and stacked fractions, the Figure 7/Figure 8 caption jam is block order, and the headings set normally |

Ninety-six packages present (queue 6-52 and 54-104), checker red on twenty-eight packs, one more than the
previous run (`python -I -X utf8 -c "import sys;sys.path.insert(0,'tmp');import check_c_distill as c;c.main()"`
reports `96 packages checked, 28 failing`, checked 2026-10-24). That is 96 of the 112 coded C papers, 85.7%, so
the 60% gate is met; the remaining 16 are queue 105 onwards.

The twenty-eight red packs at this run, with the counts the checker prints (package against record, groups):
`P-C-2011-11325-4609137d` 19/13, `P-C-2011-11422-caf513f2` 35/30, `P-C-2012-14531-6018365f` 27/27 with a changed
job sequence, `P-C-2017-55583-34388031` 28/28 with a changed job sequence, `P-C-2019-1900577-7ac4ae90` 45/32,
`P-C-2019-1901213-f6750caa` 26/31, `P-C-2019-1901679-1f246132` 51/50, `P-C-2019-1906204-4e0a421c` 78/55,
`P-C-2020-2002116-f6f4a15a` 63/64, `P-C-2020-2009116-325ae826` 68/35, `P-C-2020-2003717-4c901da6` 55/42 and
`P-C-2020-2004647-771d613e` 95/88, `P-C-2020-2010638-c32c8549` 76/52, `P-C-2021-2101166-038bd4c8` 125/73,
`P-C-2021-2101587-8b253851` 66/41, `P-C-2021-2107815-45f0e8ba` 115/73, `P-C-2021-2107870-8021b684` 79/44,
`P-C-2021-2109298-1a718172` 103/74, `P-C-2022-2200401-824b71b2` 6/14, `P-C-2022-2200688-b6248fa6` 23/16 and
`P-C-2022-2203120-59ecfcb7` 22/24, and `P-C-2022-2212336-9ca07c5b` 17/16 and
`P-C-2022-2218743-984f9ab2` 20/46, `P-C-2022-2218931-a1aa7569` 26/44,
`P-C-2022-2224507-b26b91d5` 28/51 and `P-C-2022-2204883-34c13ed1` 34/49, plus
`P-C-2022-2229059-dacff43d` 9/13 and `P-C-2023-2300348-b8cdbed6` 41/38, which went red in the last two runs -
where the oldest three of them went red in four runs ago because the
record lane re-cut their chapters from its own page reads (its rows 62, 63 and 64: 2200401 6 to 14 groups,
2200688 23 down to 16, 2203120 22 up to 24), which leaves the finished packs stale against the new groups.
The record lane reports `stored_count` from the jobs-c store, a different basis from the record's group count,
so the two numbers are not expected to match; this checker compares package rows against the record's groups
and nothing else, and no pack among the three has been rebuilt. `P-C-2022-2204883-34c13ed1` joined the list when the
record lane closed its row 65 (16 stored groups to 49), and `P-C-2022-2212336-9ca07c5b` joined it in
this run (17 groups to 16, so the pack's 17-row table and 17-job line no longer match), then
`P-C-2022-2218743-984f9ab2` (20 groups to 46) and `P-C-2022-2218931-a1aa7569` (26 to 44) joined it in the
queue-101 run, `P-C-2022-2224507-b26b91d5` joined it in the queue-102 run (28 groups to 51, the record
re-cut at 22:08 today against a pack closed at 01:38), `P-C-2022-2229059-dacff43d` in the queue-103 run (9
groups to 13, the record re-cut when row 71 closed at `75ae09c5` against a pack closed at 01:46) and
`P-C-2023-2300348-b8cdbed6` in this one (41 groups to 38, its record re-cut at 23:34 today and still uncommitted
against a pack closed at 01:56), so ten papers now sit red purely because their record chapters were re-cut after
the pack closed. The previous run's paragraph named
only twenty-five of its twenty-six, `P-C-2022-2204883-34c13ed1` having been described in the sentence above it
instead of in the list; it is in the list now (34/49, its record re-cut at 20:27 against a pack closed at 00:44).

Five of them went red in the last three runs after being green before, with no pack edited.
`P-C-2020-2009116-325ae826`'s record moved from 68 groups to 35 under a finished pack, and
`P-C-2020-2010638-c32c8549` kept the same 82 blocks and the same `pages [6, 16]` while its record was regrouped
from 76 units to 52 - the working copy carries 742 added lines against a HEAD that still reads `a8db7e14 feat:
snapshot lane records and artifacts` - so a pack that was green an hour ago is now stale by 24 groups without a
line of it changing. `P-C-2021-2101166-038bd4c8` went from 73 groups to 125 and `P-C-2021-2101587-8b253851` from
41 to 66 in the same window, then `P-C-2021-2107815-45f0e8ba` fell from 115 to 73, so the churn is not confined
to old papers: it is re-coding in progress, and it moves in both directions (1900577 lost groups, 2101166 gained
them, 2107815 lost 42). The re-cut pair `P-C-2020-2003717-4c901da6` and `P-C-2020-2004647-771d613e` is held red
by standing decision; no pack among the others is rebuilt until the record side stops moving. `P-C-2024-2401298-07d37078` was the one record that moved mid-pack and its pack was
re-cut to the new coding (20 groups, 118 blocks, 3,997 words) in the same session, so it is green again.

**The red set is not stable from one checker run to the next.** Between two runs a few minutes apart on
2026-10-24 the count went from ten to eleven while four packs went red and three went green, with no pack edited
in between: `P-C-2019-1900577-7ac4ae90`, `P-C-2019-1901213-f6750caa`, `P-C-2019-1901679-1f246132` and
`P-C-2019-1906204-4e0a421c` returned to red, and `P-C-2014-25318-eac62e81` (31/30), `P-C-2018-72969-f2349d15`
(40/41) and `P-C-2018-78577-919f0d0f` (27/28) returned to green. The record lane is rewriting
`model-establishment` codings faster than any pack can be aligned to them, so the list above is a snapshot and
every number in it is the checker's own output at that run.

**At the 69-package checkpoint**, the six red packs were drift, not damage: 45 records were rewritten without a commit
between 2026-10-24 03:38 and 05:01
(newest `P-C-2019-1922154-b7129095` at 05:01), and six of those papers now carry a different chapter coding from the
one their pack was built against - `P-C-2018-78577-919f0d0f` (28 groups in the pack, 27 in the record),
`P-C-2019-1900577-7ac4ae90` (45 against 32), `P-C-2019-1901213-f6750caa` (26 against 31), `P-C-2019-1901679-1f246132`
(51 against 50), `P-C-2019-1906204-4e0a421c` (78 against 55) and `P-C-2019-1922154-b7129095` (69 groups both ways, the
job sequence changed). The pages did not move; the coding did.

**Five of those six records cannot be rebuilt to as they stand**, because their `model-establishment` groups are
numbered from 1 in chapter order instead of using the layout's global block ids - `P-C-2019-1900577-7ac4ae90` holds ids
1-54 for a chapter whose layout blocks are 76-136, `P-C-2019-1901213-f6750caa` ids 1-52 against 61-106,
`P-C-2019-1901679-1f246132` ids 1-73 against 97-173, `P-C-2019-1906204-4e0a421c` ids 1-67 against 42-132 and
`P-C-2019-1922154-b7129095` ids 1-101 against 87-191, while every other chapter in those same five records keeps global
ids. A pack aligned to such a record would print block numbers that no layout holds, so those five stay red until the
record side re-emits global ids. `P-C-2018-78577-919f0d0f` is the exception - its ids 124-155 are global - and its pack
was rebuilt to the new coding (27 groups, 32 blocks, 807 words, 24 of the 27 groups a single block, the section title
"4 Model for Overall Score" now sitting in `problem-analysis` block 123 instead of inside the chapter) and is green.

A seventh record, `P-C-2020-2002116-f6f4a15a`, was re-coded while this pack was being written (11:38) and carries the
same defect (ids 1-98 for a chapter printed from a global block range that starts at 87), so the checker stands at
`69 packages checked, 6 failing` - the five above plus this one - and no further rebuild is attempted until the record
side re-emits global ids. The defect was reported to the record lane with the offset table.

A further record moved while queue 82 was being built: `P-C-2020-2003717-4c901da6` was re-cut at 2026-10-24 14:17 from
55 groups to 42, but by supersession rather than drift - the new `note` keeps the old coding verbatim under
`PRIOR CODING (55 layout groups over pages 9 to 15, superseded by the page read above and kept verbatim)` and its
groups now carry global ids 126-213. That pack was built at 2026-10-23 16:48 against the earlier coding and is red on
counts alone (55 groups against 42). It is not rebuildable until the lane decides which of the two readings it keeps,
and the record side has since settled the folio question: a leaf-by-leaf scan of the paper's own page text gives
leaf 2 = `Page 1` through leaf 16 = `Page 15`, so printed = leaf - 1 and the pack's printed = leaf reading is wrong.
`P-C-2020-2004647-771d613e` is the ninth entry in the same wave: its record was remapped to ids 68-204 in 88 groups
before this pack was checked, so the record is current and the pack is stale - 95 groups built against the superseded
coding, which that entry keeps verbatim under its own `PRIOR CODING` note.

**Both re-cut packs stay red until the user authorises the repair, and the repair is not a re-read.** For
`P-C-2020-2003717-4c901da6` the offset finding leaves its block and group counts intact, so the whole fix is a
targeted correction of that package's page fields from printed = leaf to printed = leaf - 1, not a second visual pass
over seven leaves. For `P-C-2020-2004647-771d613e` the coding changed under the pack, so its five fields have to be
rewritten against the 88 page-read groups. Neither is queue work and neither is done here.

Row 38, `P-C-2017-55583-34388031`, was the last red one: its record was
re-written at 2026-10-24 02:02, after the package was built at 2026-10-23 13:10, so three job labels no longer matched
it - 8 `source+close:limit` (the unit opens `From article [3] we can see on the one hand` and closes on the exclusion of
lane changing), 12 `read-figure` (it reads Figure 1(a) then 1(b)) and 13 `route` (the printed 3.2 heading block, then
the announcement of the CA model and Figure 2). The record is authoritative, so the package was rewritten to it: the job
line, those three rows, and the three prose claims that had counted the reading jobs (Figure 1 now carries two reading
units, and the chapter has three `read-figure` units over two figures). Nothing on the pages changed - only the coding
did. `P-C-2011-11325-4609137d` was re-coded outside this session
from 13 to 19 groups and its pack was rebuilt against the new version on the same day; the same happened
to `P-C-2011-11422-caf513f2`, re-coded from 30 to 35 groups, whose pack was rebuilt the same way; later
`P-C-2014-25318-eac62e81` was re-coded from 30 to 31 groups (the record now cuts the chapter's last
printed paragraph at the page break, `interpret` then `limit`) and its pack was split to match after the
page was re-read, and `P-C-2012-14531-6018365f` had one job changed from `ext:claim` to `interpret`, its
pack's job line corrected.

Queue 53 (`P-C-2020-2007707-fbb79044`) is **not distillable**: its record is one of the unresolved
raster-only entries (every chapter carries 0 groups and 0 jobs, the `model-establishment` note reading
"Stored count 12, coded 0, Delta -12, structural: raster-only pages, no block index"), so there is no
block id to align a pack to and no job sequence to quote. It is skipped, and the gate of 68 packs is
therefore reached at queue 69.
(`python -I -X utf8 -c "import sys;sys.path.insert(0,'tmp');import check_c_distill as c;c.main()"`
from `mcm-skill-work`).

## Defect classes seen so far

1. A printed subsection can be coded under another chapter, so a page reader sees more
   model sections than the record's chapter holds (11325: 2.1.2 calibration).
2. Layout tears notation tables and constraint lists into one block per row, inflating the
   block count without adding units (11893: 117 blocks for 21 units).
3. Figures and tables with no number and no caption can live inside a prose block, so the
   layout exposes no `read-figure` job even though the page reads a figure (11422).
4. Unresolved LaTeX cross-references survive into the PDF ("figure*", 11893) and the layout
   copies them verbatim.
5. Equation text in the layout is unusable (subscripts and delimiters collapse). Every
   equation count has to come from the page image.
6. The stored chapter span can be wrong in both directions: short by a page (8882, 17160's
   lead paragraph), long by a page or more (11422, 13215, 15356's pp. 13-14, 17160's p. 12).
7. A single printed paragraph can be split across two chapters (9089 group 56 into `results`
   block 132), so neither chapter holds it whole.
8. Figure and table numbers are not reliable: a number can be reused (9089 two Figure.11),
   a table title can be copied from its neighbour (Table.5 headed "Emissions of a Typical
   Plant"), and pointers can use chapter-dot numbering that no caption carries (14531 "Table
   2.1", "table 2.4"), or name a number that does not exist (9089 "Figure.12").
9. Printed folio offsets vary by paper and are not constant: 0 (13855, 15356, 17160), −1
   (8882, 9089, 11893, 12218, 13215, 14531), −2 (16075). Page numbers must be read off the
   image.
10. Headings rarely own a block: they are glued to the tail of the preceding prose block, so
    chapter ownership of a section title is arbitrary (12218, 13855, 14531, 15356, 16075).
11. Chapters are physically interleaved: other chapters' tables, figures and prose sit inside
    the page run (9089, 12218, 13215, 14531, 15356, 16075).
12. Display kind is unreliable in the layout: all 16 displays in 14531 are typed `body`, and
    in 15356 the text layer keeps only 3 of 11 display lines.
13. Figure and table captions are captured as separate blocks from their art, often on the
    next page, and sometimes two captions are welded into one block (15356 blocks 91, 112).
14. A chapter can lose its own opening paragraph to no chapter at all (17160 block 26, the
    lead paragraph of section 4, and block 74, the 5.3 heading).
15. A chapter can be physically discontinuous: another chapter's pages sit between its parts,
    so a contiguous span hides a hole (15356 runs 6-12 then 15-17, with `strengths-limitations`
    on 13-14). "Carries nothing" is the wrong reading - check whether the pages are blank,
    another chapter's, or the chapter's own dropped text.
16. Inline math is dropped by the text layer and takes the sentence with it, splitting one
    citing sentence into two blocks with the equation and its delimiters gone (16075: "According
    to the matrix (4-7) and equation Aw w" / ", we can figure out that the w = weight vector").
    The remedy is to read the sentence off the page; the number itself can be intact.
17. Watermark overlays are captured as body text mid-sentence ("数学中国", "www.madio.net" at 21
    blocks in 18492), which corrupts quotes and inflates word counts slightly.
18. A multi-page run of the chapter's own prose can be assigned to no chapter at all, not just
    one paragraph: 28199 has 29 consecutive blocks (60-88, about 3.2 printed pages) that belong
    nowhere, because the block before the gap swallows the next section's heading. A record can
    therefore hold 41 groups and still be missing a third of the chapter's body.
    18b, the mirror image: a paragraph can be claimed by the chapter next door rather than left
    unowned - 15356 block 67 is the chapter's own opening paragraph but is booked to
    `assumptions` because the two headings that open the chapter sit at the tail of block 66;
    28199's whole 60-88 run is the same failure at scale, and 28747's §4.3 is claimed by
    `results` with overlapping ranges, so both chapters count the same pages.
19. A unit can announce a formula the page never prints: 33900 block 100 ends "we calculate the
    LeaderRank Value LR as follows:" and the next printed line is C_2i, which consumes LR. The
    record still spends a `derive` job on it, so the job vector is honest about the intent and
    the page is honest about the gap; the distill must say the derivation is missing rather than
    describe it.
20. A cross-reference can cite a number that exists elsewhere in the same paper: 33900's p. 10
    prose says "expressed as Equation (4)" over the equation printed (2), and (4) is the Poisson
    law four pages later. Unlike class 8 (a number that exists nowhere), this one checks out
    against the equation list and is only caught on the page.
21. Two chapters can share one page, and the notation declared in the earlier chapter's section is
    the later chapter's working vocabulary: 33900's p. 4 carries the end of `assumptions` (its §2.2
    lead-in and Table 1, blocks 33-42, owned whole and correctly as one `read-figure` group) above
    chapter 3's opening at block 43. Nothing is mis-coded - the boundary simply falls mid-page - but
    chapter 3 then uses d_ij, P_i, L_i, G and g for eleven pages without redefining or
    forward-referencing them, so a reader who trusts chapter ownership reports the symbols as
    undefined. A one-row-per-block table shape here is a layout artefact (as in 16075's shifted
    column) and must not be booked as a paper defect.
22. A record's own `note` can name the wrong block for a heading: 37075's note says block 100
    routes the 4.2.1 heading and block 128 the 4.3 heading, but both headings sit at the tails of
    99 and 127 and neither 100 nor 128 contains one. The block ranges stay right while the prose
    description of them is wrong, so the note cannot be used to locate a heading without the page.
23. A rank table's identifier column can agree on nothing while its names agree on five: 16075's
    Tables 2 and 3 give the same five people numbers differing by exactly one (Elsie 7/37, Alex
    21/22, Paul 43/44, Yao 67/68, Jean 18/19), and the only two identifiers the tables do share,
    20 and 49, belong to different people in each. Verified on the raster, so it is a paper defect;
    the neighbouring one-row symbol shift in the same paper's Table 1 is a layout artefact and must
    not be booked as one (instances cross-checked with mcm-11).
24. A declared span can contain a long run of blocks owned by *other named chapters*, not left
    unowned: 42939 runs 149-195 (47 blocks, six pages) through §5.3, §6, §7, the reference list and
    the Appendix heading, claimed by `results`, `future-improvements`, `conclusion` and
    `strengths-limitations`. Only the reference list and the Appendix belong to nobody. Unlike
    class 18 this is not a bookkeeping hole - those chapters are correctly coded - it is a span that
    was set by page number without checking where the chapter's argument stops.
25. A chapter can end with groups that are separated from its body by other chapters' pages, and
    the separation can be invisible in the group list: 42939's groups 51-52 sit 46 blocks after
    group 50, reading the Appendix captions of Figures 9 and 10, which the body cites nowhere.
    Booking them into the model chapter is defensible by topic and indefensible as a span.
26. A display can define a symbol in terms of itself: 42939 block 104 prints
    "c_m = c_m/(c1 + c2 + c3 + c4)", so the adjusted weight never gets distinct notation and the
    normalisation cannot be read off the page.
27. A caption welded into a heading-bearing block leaves the figure with no reader: 42939's
    Figure 7 caption shares block 144 with the "5.2.3" heading inside a `route` unit, so the
    piecewise approximation that all of §5.2.3 rests on has no `read-figure` job, while its
    predecessor Figure 6 does. The same block shape also fuses headings with captions outright
    (block 126: "…fROI_i 5.2.1 Figure 5: Demonstration of fROI_1").
28. Equation numbering can be paper-global rather than chapter-local, so the printed numbers carry an
    offset that no count may ignore: 50193's span runs (8) to (19) with no gap, because sections 1
    and 2 spent (1) to (7). Read the numbers, do not assume they start at (1).
29. A caption can survive into the final PDF as an unfilled placeholder with indistinguishable panel
    labels: 50193 block 235 reads "Figure 2: general title." and block 234 reads "(a) Grey Predicting
    for Future ROI (b) Grey Predicting for Future ROI" twice, so neither the caption nor the titles
    say what the panels show, and the recorded `read-figure` job reads the placeholder.
30. A matrix display can arrive row-desynced: 50193 block 176 holds the 4x4 AHP matrix as a torn run
    ("1 5 6 3 1 3 1 2 … 2 1 1 2 1 2 3 1 1 1 1 3 6 5") with the bracket glyphs as separate characters
    and rows no longer aligned to columns. Sixteen entries survive and the arithmetic does not, so a
    weight check has to be redone from the raster or the printed vectors.
31. Two chapters' notes can book the same heading to different blocks, so the heading is credited
    twice and held by neither claimant: 50193's `problem-analysis` note gives "3 ROI Evaluation
    System" to block 131 (correct, 131 also carries 3.1) and the model note gives "3.1" to block 132
    (which holds the body and display (8) only). A cross-chapter check is needed before a note's
    assignment is trusted.
32. A paper can number no equation at all, so the display count has nothing to check against and
    the only set-off objects besides equations are figure captions and a labelled code box: 52815
    prints 24 set-off equations on pp. 6-9, zero numbers on any of them, and one boxed "Algorithm 1"
    on p. 12. Under this condition every displayed-equation figure in the package is a raster count,
    and a paper's internal cross-reference like "equation (6)" does not exist.
33. A figure can print on a later page than the prose that cites it, with its caption spliced
    mid-sentence into a derivation block: 52815's block 62 (p. 11) says "see Figure 6" and "Both
    graphs above show", the two panels sit at the top of p. 12, and the caption is welded into block
    65 as "…the largest increase in Goodness on Figure 6: 2D Example of Optimizing Funding
    Distribution", which swallows the object of the sentence. The figure is inserted between
    "Goodness on" and the continuation fragment "each iteration until all our funds are depleted."
34. A page can carry figures and captions and no prose at all, so a read-figure unit booked to that
    page has no citing sentence to read: 52815's PDF p. 10 holds only Figures 3 and 4 with their
    captions, the bottom third blank, and the sentences citing both are on p. 9.
35. A chapter can be recorded in page order across an unrelated section, so its unit list interleaves
    another chapter's blocks rather than leaving a hole: 52815's `model-establishment` runs 3, 4, then
    section 5 (blocks 69-72, `assumptions`), then 6.1, all inside one 38-unit chapter recorded as
    `pages [6, 13]`. Unlike class 15 the intervening pages are fully claimed - by the other chapter -
    so nothing looks missing; the tell is a job or heading sequence that jumps from 4.3 to 6.1.
36. A caption set *below* its grid welds to the head of the next grid's block, so a read-figure unit
    holds one table's caption over another table's columns: 55261 blocks 161 and 164 begin "Table 6:
    Part one of simulation results." / "Table 7: Part two of simulation results." and then print the
    headers of Tables 7 and 8, so units 48-49 each credit the preceding table. Class 13 is the
    caption-detached case; this is the caption-detached-*and*-mis-attached case, and the record
    inherits the shift without any block count going wrong.
37. A paper's own table cross-reference can skip the table it introduces: 55261 block 130 ends
    "results are tabulated in Tables 4 through 6" directly above the Table 3 grid, so Tables 3 and 4
    have no correct citation anywhere and the phrase reaches into the shock-wave table on p. 15. This
    is the table analogue of class 20 and is only visible on the page, since every number cited exists.
38. A results table can print two captions - an unnumbered bold title inside the grid block above it
    and the numbered caption below it ("Light Traffic Simulation Results" over "Table 3: Results for
    light traffic") - so a record that quotes one cannot show the doubling, and a reader counting
    titles against numbers finds seven tables and eleven captions.
39. A display can be the reciprocal of the quantity its own sentence defines: 55261's equation (2)
    prints (1/n)Σ(1/u_i) under "The space mean speed, u_s, is given by", which is the reciprocal of the
    space mean speed, so the identity q = u_s·k in (3) cannot hold as printed. The same chapter's (14)
    and (15) print e^(−t) after defining λ = μ/t in the line between them. A symbol check has to be
    run against the definition sentence, not only against neighbouring equations.
40. Ten blocks of one chapter can end in the running header, which is a page break and not a
    paragraph end: 55261 blocks 70, 81, 88, 94, 99, 113, 124, 134, 144 and 157 all terminate in
    "Team #55261 Page N of 28", where N is the printed folio of the page the block continues onto,
    cutting one sentence after a colon ("Taking the total derivative of (9) yields:") and another
    mid-clause ("we set ∆d" / "equal to ∆d2").
41. A recorded block hole can be a table interleaved into a split sentence rather than an omission:
    55261's group 41 is [144, 147, 148], the skipped 145-146 are Table 5's grid and caption, and the
    sentence around them reads "…the vehicle reduces speed from u_o to u′. We" / Table 5 / "wish to
    measure the effect on traffic performance when an event such as this occurs." Unlike class 24 the
    intervening blocks belong to the same unit's own sentence.
42. Row labels can change name mid-run: 55261's Tables 2-5 print "Moderate traffic" and its Tables
    6-8 print "Medium traffic" for the same row, in the same chapter, with no note.
43. A record can describe a unit by the wrong dimension, so the note cannot be used to decide what a
    display is: 55261's unit 40 is t_min in seconds with a factor of 1/3, the printed prose calls the
    same quantity "the minimum gap distance" and (23) uses it as a time; unit 43 is called a
    "minimum safety distance" and prints a density, k′ = 1/d_stop(u′), in cars/mile; unit 45 is called
    an "average waiting time" and prints queue length and vehicle count.
44. A 1000 px proxy can lose subscripts and fake a misprint: 55261's equation (8) read
    "d_car + d_car − k/…" at review resolution and prints "d_zero + d_car − L/k", confirmed on a
    `--crop` of the original raster. Suspect symbols are booked as paper defects only after a crop.
45. A chart can enter the extraction twice - once as an image and once as its axis labels, tick
    numbers and legend recovered as body text - so the `read-figure` unit reads axis furniture and the
    actual reading is a second unit: 55278 blocks 95-96 hold "Car Arriving Frequency 5 Number of
    arriving cars per second 4 3 2 1 0 1 2 3 4 5 6 7 8 9 Peak Hours peak non-peak" and unit 18 reads
    the values. Block 96 is also the span's only `display` block while all nine real equations are
    typed `body`, so the kind field points at the opposite object.
46. A notation table's rows can outnumber its blocks and every block can end on the *next* row's
    symbol, so no block holds a symbol with its meaning: 55278 prints 25 rows over blocks 49-71, with
    block 55 carrying p and q and block 70 carrying P_c and "α, β, γ", and the header row inside
    block 48's tail. Block 49 reads "An indicator representing the car type on a cell v". A per-row
    reading of this table is impossible without the page.
47. A notation table can declare two symbols with one meaning and use only one: 55278 lists T_r
    ("Response time for a human driver to take action") and T_rh ("Response time for a human driver");
    T_rh carries the model in five places (G_S = T_rh·v) and T_r appears exactly once, in the table.
48. A figure can be cited only from inside the block that also carries its caption, with the artwork on
    the next page, so that figure gets no `read-figure` job while its neighbours have one: 55278's
    Figure 3 caption is the tail of `define` block 139, the diagram prints on p. 12, and the describing
    prose starts on p. 11. Class 27 is the same loss caused by a heading-bearing block; here the cause
    is the caption's position at the tail of a prose block.
49. A heading can be a whole unit, and a subsection's numeral can be in a different block from its
    title: 55278 groups 30 (block 119) and 35 (block 124) are the 2.4.2 and 2.4.3 titles and nothing
    else, each carrying a `route` job with no paragraph to route, and "2.2.1" closes block 71 while the
    title "Introducing Acceleration into Cellar Automata" is all of block 72.
50. A layout block can fuse the last display of one page with the next page's chapter heading, so the
    block's page range spans the break and block ownership suggests the heading belongs to the closed
    chapter: 55583 block 135 reads "(12) 4 Model Extension and Simulation Analysis" over pages 11-12,
    while on the page (12) is the last object of p. 11 and the heading is the first line of p. 12.
    Class 40 is the same fusion with the running header; here the second element is a heading.
51. A figure can be cited only *below* its own artwork, with no forward reference anywhere, so the
    read-figure unit precedes every sentence that refers to the object it reads: 55583's unit 10 holds
    Figure 1's panel labels and caption on p. 9 and the only citations are unit 12's "which is just as
    the Figure 1(a) shown above" and "which is shown in Figure 1(b) above", printed under the panels.
    The page-8 sentence that was supposed to point here ("Here is the structural difference…") names no
    figure, and the record's note inherits the assumption that it does.
52. A chapter title can be welded to the previous chapter's last table row, so the span opens
    headingless and the only copy of the title sits in a block owned by the closed chapter: 55583 block
    82 ends "Table 1: Notations. 3 Model Construction" and its page range is 7-8. The printed title may
    also differ from the record's chapter id ("Model Construction" vs `model-establishment`).
53. A parameter can be printed without dimensions and then used as a multiplier, and a unit conversion
    can be rounded and then treated as exact: 55583 gives "response time is from 0.3 seconds to 1.5
    seconds.Here we define t_response = 1" and equation (4) multiplies v_ins by it; and "60 mile/h,
    which is about 27 m/s, namely, 7 unit length per second" over the stated 4 m cell is 6.75, with
    p. 12 repeating 7 as exact.
54. Two definitions of the same estimator in one chapter can be written to different forms: 55583's
    (11) is an indexed mean "σ_t² = (1/m)Σ_m(v_ti − v̄)²" and (12) is a bare "σ_s² = (1/224)Σ(v_ti −
    v̄)²" with the sample size hard-coded and the index dropped, although the prose says the second is
    taken across road sections at a fixed time.
55. A section heading can be carried by a *display* block, so the heading has no block of its own and
    the unit that owns it is typed `define` on an equation: 55585's "4.2.4 Lane-Changing Rules for
    SDVs" is the tail of block 232, the second line of an unnumbered STEP display.
56. An equation series can open on a number that does not exist: 55585 runs (3.1), (3.2), then
    (4.3) to (4.15), and (4.1) and (4.2) are printed nowhere in the paper - unlike class 28, the gap
    is at the head of the series and no cross-reference points into it.
57. Two different procedures can print under identical step labels with nothing distinguishing them:
    55585 prints "STEP 1:"/"STEP 2:" twice on p. 14, once for the NSDV lane change (with LCP) and once
    for the SDV lane change (without), and the second pair repeats the numerals of the first.
58. Two side-by-side figure captions can be welded across the column gap, one caption's last word
    printing under the other figure's: 55585 block 249 reads "Figure 9: LCM for SDVs under Certain
    Condi- Figure 10: LCS for SDVs under Certain Conditions tions".
59. A table's caption number and the prose's citation of it can belong to different numbering schemes,
    so the object is not findable by either name: 55585 captions "Table 1" and "Table 2" while the
    citing sentences print "Tab. 4.1.1" and "Tab. 4.2.1", which appear on no page.
60. A bullet run-in heading can print with no body at all, the figure taking its place: 55585 p. 10
    prints "• Deceleration" and then Figure 4, the subsection's prose resuming only after the figure.
61. A rule figure can draw thresholds that differ from the thresholds its own cases state: 55585's
    Figures 3 and 4 bracket only D_max and D_min while the conditions they illustrate compare against
    D_min(SDV-SDV); and p. 10 computes "the acceleration of a vehicle is 2.67m/s2" from 4 m per 1.5 s,
    which is a speed - the acceleration is 1.78 m/s2 - and calls it "in line with daily experience".
62. A page can reprint the previous page's block verbatim under the same display numbers, and the
    layout can keep only one copy, so the block table has an unmarked hole: 72969 p. 12 repeats
    "(8)", "(9)", "(10)" and eleven prose lines from p. 11, and blocks 92 and 93 jump straight over
    the repeated run.
63. An equation series can skip numbers in the middle and leave its lead-in dangling: 72969 ends
    p. 12 on "…denoted as", (11) and (12) print nowhere, and (13) opens p. 13 - the display that
    answers the sentence arrives two numbers late.
64. A pirated-copy watermark can print in the running head and enter block text, so units end on a
    sales line instead of a sentence: 72969's "精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技
    巧、matlab程序代码资料等，尽在淘宝店铺： 闵大荒工科男的杂货铺！" is inside blocks 79, 98 and 121.
65. A figure's panel count can disagree with the table whose ordering it claims to follow, so the
    caption's key cannot be checked panel by panel: 72969's Table 3 has 20 items and Figure 5 draws
    18 unlabelled panels under "the placing order is the same as Table 3".
66. A stretch of printed page content can belong to no block at all, so the record's group list steps
    over it silently: 72969 p. 17 prints the subhead "Technique 2: 'Look Aside' Latitudinal
    Refinement", two paragraphs and displays (20)-(23) between block 122 and block 123.
67. A record's `heading` field can lag the printed section numbers by one: 72969 stores "4.2
    Characterization and Analysis / 4.3 Evaluation / 4.4 Prediction" while the pages print 4.2,
    4.2.1, 4.2.2, 4.3, 4.4 and 4.5.
68. An equation can add a standard deviation to a variance: 72969's (7) prints
    "σ²_* = K_2 − K_1K_0^{-1}K_1^T + σ" while (4) correctly writes the noise as σ²I.
69. One subsection number can print twice on a single page, so the chapter's numbering repeats
    instead of advancing: 73767 p. 18 prints "5.4.3 Analyzing the Error" and "5.4.3 Predicting the
    Target Values", the second welded as a tail.
70. A cross-reference can survive as an unfilled placeholder, so the paper cites itself by no name:
    73767 block 119 points at (20) as "the equation N", and "formula 15" is cited twice for two
    different displays - (20) on p. 19 and the ARMA line numbered (21) on p. 20.
71. A run of displays can have no block at all on a page whose prose does: 73767 p. 17 prints (11) to
    (16), the whole of the BP learning rules, between block 118's "drive the core formulas" and block
    119's "Topredict the dependent variable", so the derivation exists only in the raster.
72. A display can be torn across a page break and split between two record units, the number on one
    page and its expression on the next: 73767 block 124 ends with "(21)" at the foot of p. 19 and
    block 125 is the ARMA expression on p. 20.
73. A table's column of row names can disagree with the formulas beside them and with the figure that
    visualises them: 73767's Table 6 labels a row "(Csr)" whose formula prints Cnr = Wcs/Tpo, Figure 6
    writes "Da" for the table's "Dpa", and Cep = Tcs/Tpo is a share used as the per-capita environment
    term; and Table 5 is captioned "the regression results of Equation 1" when (1) is the average price
    and the grid holds eight regressions.
74. A conclusion sentence can contradict the star legend of the table it reads: 73767 block 94 says
    "population has no significant influence", while the ln(Pop) NM cells are starred `0.0361*` and
    `0.0421*` under a caption that defines `*` as 10% confidence.
75. Three figure captions can be welded into one line inside a prose unit, so none of the three figures
    is read by a `read-figure` job: 73767 block 119 carries "Figure 8: the fitting results Figure 9:
    Scenario one Figure 10: Scenario two" inside a `route` unit, and Figures 9 and 10 are then cited
    from units 44 and 45.
76. A two-column body measure can be broken mid-word around a watermark, so a word's head lands in one
    block and its tail in another after the sales line: 73767 blocks 86-88 print "syste / m" and
    "comp [watermark] rehensively".
77. A figure can print as an empty frame and still be the sole evidence for the chapter's conclusion:
    78577's Figure 9 shows axis titles and no series, and block 147 ranks CA, TX, NM, AZ "From Figure
    9".
78. Two tables can share one block with both captions ahead of both grids, so the citing sentence and
    the grid order disagree: 78577 block 143 prints "Table 4: Weights of Energy Indices" and "Table 5:
    Coefficients for Utility Functions" side by side after a sentence that names only Table 5.
79. A weight row can violate the normalisation its own formula imposes, and a negative weight can carry
    a direction the prose never states: 78577's (5) normalises d_i over m indicators while Table 4's
    rows sum to 0.790, -0.552 and 0.222, with GE entering at -0.105 and -0.389.
80. A cumulative-proportion sentence can swap the two categories its table distinguishes: 78577 block
    138 says "0.93 for clean energy, and 0.98 for renewable energy" where Table 3 prints clean at
    0.93549/0.97887 and renewable at 0.83952/0.93164.
81. A bullet list can be torn mid-word across three blocks, leaving a bullet glyph stranded at a block
    end: 78577 blocks 149-152 read "…difference method; •", "…undeter-", "…Autocorrela-", "tion
    Function) and PACF …".
82. A single block can silently own printed pages the text layer renders as nothing, so a 68-word unit
    holds about 1,400 printed words: 80560 block 125 is booked as one `limit` unit on [12,15] and its
    interior pages (printed 10-11) carry reason two, the 5.2 heading, the epigraph, two paragraphs, a
    ten-row parameter table and displays (8)-(12), while text/pages records 10 words per page.
83. The same equation can print twice with two parameters transposed and no sentence saying which is
    right: 80560's (10) prints "I_t = Ī + θ_zE_tx_t+1 + θ_xE_tπ_t+1" and its (15) the same left-hand
    side with θ_x on the gap and θ_z on inflation.
84. A parameter can be fitted in prose and appear in no equation: 80560 sets "(φ, λ, γ, θ_z, θ_x, θ_i)"
    from historical data and θ_i occurs nowhere; the same chapter's α vector gives six weights
    [0.5, 0.15, 0.1, 0.1, 0.1, 0.05] for five lags.
85. A second parameter table can print with no caption and no number between Table 1 and Table 2, and
    misspell the header the first one spells correctly: 80560's ten-row "Detotation | Definition"
    table sits on printed 10 with nothing referring to it.
86. A table can be captioned as a figure, so the prose's "the following table" lands on a figure
    number: 80560 prints "Figure 7: The external cost of energy", "Figure 8: The influence rate of
    every end-use sector" and "Figure 13: total EROI of Four states in 2009" over three grids.
87. A figure set can be cited by another set's numbers: 80560 block 130 says "We've also visualized our
    findings in Figure 9-12", which are the EROI curves of 4.3, while the prediction profiles it means
    are Figures 15-18.
88. A watermark can be its own record block and be paired with real prose in one unit: 80560 block 136
    is the shop line alone (1 word, x0 = 0) and unit 42 is "136-137".
89. A figure's caption can exist only in the raster, so no page of the text layer contains the string:
    80560's "Figure 14: Linear Regression for (15/43) factors in California" is in no
    text/pages file, and the grid it captions prints one page after the sentence that means it.
90. A chapter can print no numbered display at all, so nothing in it can be cross-referenced by number
    and the algebra is unaddressable: 82150 prints 22 expression groups across five pages, none
    numbered, and the only numeric pointer is "(refer to figure 4-10)".
91. A paragraph of derivation can print between two blocks with both the prose and the displays missing
    from the text layer, so a page and a half of print belongs to nothing: 82150's PDF 13 (printed 10)
    holds roughly 330 words and eight expression groups against 87 body words in the text layer, PDF 14
    (printed 11) 200 against 89, and block 118 declares [13,14] while containing neither page.
92. A symbol can be defined as maximum and minimum in the same line, and two distinct quantities can
    print as the identical formula: 82150's "where Z_j+ = max_i(x′_ij), Z_j+ = min_i(x′_ij)" and its
    PROMETHEE flows "(1/(m-1))Σπ(d_ak)" for both the positive and the negative.
93. A case split can leave one value owned by both branches: 82150's P(d) = {1, d ≥ 0 ; 0, d ≤ 0}
    assigns 1 and 0 at d = 0.
94. A vector printed as a result can be impossible under the chapter's own definitions, yet the
    arithmetic that consumes it can still close: 82150's Z+ must equal W and Z- must be zero because
    every column of Table 4-3 spans 0 to 1, but the printed φ+ and D- match neither, while
    (0.4109+0.3944)/2 = 0.4026 does give the printed S_t+.
95. A transformed table can fail to reproduce from its source under the paper's own formula in a few
    cells: 82150's Table 4-3 misses Table 4-2 in four of sixteen cells by 0.004-0.008 while the other
    twelve reproduce exactly.
96. A choropleth can shade its states against the ranking its own chapter prints: 82150's Figure 4-10
    paints California (top score) palest and Texas (second) darkest, with an illegible colour bar.
97. A record can file a sentence's continuation line before the line it continues, so a `compute` unit
    reads tail-first: 82150 stores block 123 ("S_t+=[…] (refer to figure 4-10) .") before block 124
    ("The final scores of four states … are:"), and the grid header arrives as "CA AZ NM TX" with a
    stray "t" in front of it.
98. A chapter's own title can print inside the last block of the previous chapter, so the span opens on
    prose taken mid-topic and owns no heading block at all: 1900577's "5 Model Development" is welded to
    block 82, a bullet the record files under `assumptions`, and all 55 blocks of the span are `body`.
99. A block's `pages` can be widened by the next page's folio string wedged into its own text, so the
    record claims a page the prose never reaches: 1900577's blocks 87, 96, 103, 106, 111, 117, 132 and
    137 each end on "N of 24" and each is booked as a two-page range.
100. A display can be fragmented over three blocks with the defined set printed after the sum that
    indexes it: 1900577's (3) reads "Ij X" | "Si = {j ∈N | 1 ≤j ≤n; j̸ = i} Pi = , (3)" | "r2 i,j jϵSi
    5.2 Model Construction", so the equals sign comes before its fraction and the heading rides the last
    fragment.
101. A chapter can cite a figure that prints outside its own span, so the comparison it reports is
    illustrated where the chapter is not: 1900577's unit 24 names "(Figure 10)" for the baseline, and
    Figure 10 prints on PDF 25 with Figures 8 and 9 on PDF 18 and 25.
102. One paragraph can credit the same result to two figure numbers, one of which is the other model's
    caption: 1900577's unit 45 opens "With the adjusted model, as shown in Figure 7" and closes
    "(Figure 6)", and Figure 6 is captioned as the non-adjusted comparison.
103. A percentage can be carried over from one comparison into the wrong pair, in the same sentence as
    one that does close: 1900577's unit 45 reports 47408 → 41631 as 12.2% (correct) and 45539 → 41631 as
    "3.9% decrease" (8.6%; 3.9% is the 47408 → 45539 figure printed six pages earlier).
104. A chapter's title and its nomenclature heading can print in no block at all, and the grid they head
    can be coded under the previous chapter: 1901213's "5 Model" and "Nomenclature" appear in no block,
    and the eight-row grid is blocks 67-72 under `assumptions`.
105. A two-column notation table can be recorded one row out of phase, so each block carries one row's
    description followed by the next row's symbol - seen twice now, 55278 (row 37, 25 rows over 23
    blocks) and 1901213: block 67 ends "Health of all counties in
    year t sorted by FIPS code xt =", block 68 opens "Opioid problem … A = Adjacency matrix Q =
    Transition matrix δ =", and the eight printed rows become seven blocks.
106. A display can be a schematic whose label layer becomes a record group of its own: 1901213 block 73
    ends "= + (1) |{z} |{z}" and block 74 is nothing but "Future Surrounding Internal opioid problem well
    being opioid problem", a ten-word `define` unit.
107. An equation number, its minimising subscript and its prime can print in the block after the
    equation: 1901213 block 90 ends "X ∥xt+1 −Q′Axt∥ Q = min" and block 91 begins "(3) Q′ t Here, the
    summation of the norms is over all t in our dataset."
108. A fitted mixing weight can return a corner that deletes half the model the chapter just built:
    1901213 promises "we can choose a θ that minimizes the error", and the search prints three sections
    later - "We varied θ from 0 to 1 in steps of 0.001 and found that we get the best prediction when
    θ = 1 i.e., we only consider the external model."
109. A chapter can code its own section headings two ways at once - some in `heading` blocks, some welded
    to prose tails, one split into numeral and title: 1901679 puts 4, 5, 5.1 and 5.3 in `heading`
    blocks, welds 4.1/4.1.1/4.2/5.2/5.4/5.5 to tails (97, 115, 124, 135, 144, 148), and splits 4.0.1
    into block 86's tail plus a title-only `body` block 87.
110. A figure can print with no number and no caption, surviving only as a pair of panel labels in a
    `display` block, while the prose cites it by letter: 1901679's Figures 2 and 7 are blocks 91 and 146
    ("(a) Prevalence of Opioid Abuse (b) Rates of Change of Opioid Abuse" / "(a) Error b/w Random Walk
    and Data (Noise) …"), cited as "Figure 2a" and "Figures 7a and 7b".
111. A cross-reference can print unresolved in the body text: 1901679 block 144 opens "As seen in
    Figure ?? below", and the figure it means is the uncaptioned Figure 7.
112. A chapter can open a later section with a paragraph of its own text above its heading, because the
    heading prints mid-page after the previous block: 1901679's block 151 (booked to `results`) prints
    above the `heading` block 152 that carries "6 A Second Modeling Approach: Spatial Regression".
113. A figure can plot fewer categories than the chapter defines, and one chapter can order the same set
    three different ways: 1901679 defines six classes but Figure 6's axis carries five (High Decreasing
    missing), block 95's legend orders them 1 LS, 2 HS, 3 LD, 4 HD, 5 LI, 6 HI, the Figure 6 axis orders
    LS HS LI HI LD, and Figure 3's legend prints the bare digits 1-6.
114. A paper can print no page number on any page, so page identity rests on a running head that names
    the part and a contents page that supplies the mapping: 1901679 prints "4. PART I: CHARACTERISTICS
    OF THE EPIDEMIC … Control #1901679" with no folio, the head turns over to "5. PART II" on a page
    that still carries Part I matter, and only the TOC's 4→8, 4.1→10, 4.2→11, 5→12 … 6→15 gives the
    printed page at all.
115. A chapter boundary can be drawn through the middle of a section, so the record's page window
    swallows a neighbour's blocks and the numbering looks broken when it is not: 1906204's span covers
    ids 33-178 but owns 133, with 37-41 under `assumptions` and 136-143 under `results`; block 133 ends
    "3.6 … 3.6.1" and the section those fragments open prints as `results` matter, the chapter resuming
    at 144.
116. A display half can be stored in the reverse of its reading order, so the block sequence prints a
    wrong formula: 1906204 block 58 holds "= E[(X −µX)(Y −µY )]" before block 59's "Corr(X,Y) =
    cov(X,Y) σXσY", and block 80 holds the Score summand before block 79's "Scorei = j=0 and j̸=i".
117. A fraction can lose its numerator into the block before it, leaving the text layer with a rule that
    has no reciprocal: 1906204 block 107 ends "…real value 13: 1 take" and block 108 begins
    "0.01+(difference)2 as weight of the current feature", the printed rule being
    1/(0.01 + difference²); the same loss repeats at block 121.
118. An algorithm listing's line numbers can attach to the line above, so the whole pseudocode reads one
    line late: 1906204 block 102 "simi_zones ← zi's all similar zones 4:", 103 "for Each Drug dj do 5: …
    6:", 105 "for Each Training Sample sk do 8:", and lines 5 and 6 merge into one block.
119. A table's grid and its caption can be booked as two units with two different jobs: 1906204's Table 2
    rows print inside `interpret` block 164 and its six-word caption is `read-figure` block 165, with the
    handoff sentence emptied - "and run the Apriori algorithm for each category, and the final result
    is ."
120. A display can exist only as the tail of a prose block, and a whole minimisation line can vanish from
    the text layer while its middle clause survives: 1906204's Total prints inside block 69
    ("…invoke time decay factor. 2016 X dataiνi−1 Total = i=2010") and the QP display keeps only block
    94's ", where ξi is slack, to separate projected data points from origin: ζi > 0".
121. Figure label layers can be booked one unit per label cluster, so a single map costs four or five
    record groups: 1906204's Figure 7 is blocks 83-86 (4, 22, 26 and 38 words, one of them the bare
    "Methorphan") plus its caption in 87, and Figure 4 is blocks 42-46 - 15 of the chapter's 78 units
    carrying no prose.
122. A numbered assumption list in parentheses can be mistaken for equation numbers by any text-layer
    scan: 1906204 announces "(1) Trend over time (2) Geographical factor (3) Drug identification size"
    and then writes "Factor (1)" and "factor (3)" inside later formulas, so the only parenthesised
    numbers on the page are labels and the chapter prints no numbered equation at all.

123. A display can lose a whole number from its sequence, in the text layer and on the page: 1922154
    numbers its formulas (1) to (5), then (7) for the concentration index, then (8)-(13) - and the
    string "(6)" occurs nowhere in the paper's 23 pages, so a reader counting formulas finds a gap the
    prose never mentions.
124. The heading/chapter seam cuts both ways: a chapter's own section headings can ride the last block
    of the chapter before it, and the next chapter's title can ride the last block of this one. 1922154's
    `results` block 151 ends "4 Model Modification … 4.1 Preprocess Data 4.1.1 Data overview", while
    model block 121 ends "3.3 Results & analysis" and block 189 "4.4 Results & analysis"; "2.3 General
    Assumptions" rides block 58, a `model-establishment` block that is Table 1's remainder, while the
    assumptions it heads are blocks 59-71 under `assumptions`.
125. A table's cells can be de-interleaved one row out of phase, so each block pairs a cell of one row
    with the group label of the next: 1922154 Table 4 prints four factor rows and the layer stores six
    blocks - 179 "Percent; Males 15 years and over - Never married（Mn） Marital status（MS）", 180
    "…（Fn） Educational", 181 the five ancestry cells then "Ancestry(AN)", 184 "than "very well"(Lo)
    4.3 Model Modification".
126. One dataset's year split can print four different ways on adjacent pages: 1922154 has Table 2 rows
    2010-2012 / 2013-2016, Table 3's header 2010-2012 / 2013-2017, block 168 "we divided the 7-year
    census socio-economic data into 2010-2011 and 2012-2017", and block 152 "each of the years
    2010-2016".
127. A symbol table's rows can be reprinted verbatim as prose two pages later, so one definition exists
    twice in two registers: 1922154's Table 1 cells and blocks 100-101 both carry "The environment
    (vector) related to ith county in the nth year" and "The growth rate of opioid usage in the ith
    county in the nth year", and no cross-reference says the prose is restating the table.

128. A conversion kernel can print with the sign that voids the property its own prose asserts. 2002116's
    display (1) prints `e^{+abs(i−s)²/(2σ0)}` (raster-verified; the text layer drops the sign and stores
    only "e 2σ0"), so the encoding peaks at the furthest rating, while the next page reads "the 4-star
    rate has the highest probability to be rated 4 stars, second-highest possibility to be rated as 3 or
    5 stars" and the sigma clause reads "the bigger the more robust".
129. Two kernels of the same decay form inside one chapter can carry opposite signs, so no single
    reading of the parameter reconciles them: 2002116's (1) uses a plus exponent for the star distance
    and (2) a minus exponent for the context-word distance, with sigma defined once.
130. A heading can be fused with the document watermark inside a `display` block, with the chapter
    numeral dropped: 2002116 blocks 114, 122 and 148 each hold the watermark string plus "3.3 …",
    "3.4 …" and "Predict Potential Success or Failure", and in 148 the "5" exists on the page and in the
    text layer but in no block, so the layout's own record of a chapter title is watermark plus title.
131. A section numeral can be detached from its title and left in the unit before it: 2002116's 3.2.1
    numeral ends block 82 while its title is the whole of block 83, and 6.2.1 is a zero-word block 187
    whose title occupies the next block, so a five-word `route` unit is an entire heading.
132. A notation table can be de-interleaved one row out of phase *and* absorb the chapter title: 2002116
    block 54 holds caption, header and row 1 then the next row's symbol "sid", each later block one
    definition, one type and the next symbol, and block 62 holds the ninth definition plus "3
    Informative Evaluation Model" - so the chapter title prints inside a table row.
133. An equation number can lead the block that carries the *following* prose: 2002116's (15) opens
    block 136 as "(15) Where the PEN(T, P) is the penalty factor", (16) opens 139, (17) opens 153, and
    (2) opens 92 as the fragment "2σ j" - so block order puts number before equation in four cases.
134. A multi-block display can be stored out of print order inside its own unit: 2002116's (12) runs
    numerator tail (116) - exponents (117) - number and "Where the 1−" (118) - fraction words (119) -
    entropy gloss (120), i.e. the coefficient's "1/" precedes the summand it divides and "2z(" follows
    it, the same inversion in (13) and (11).
135. A term can be printed without the minus its gloss states, so the displayed exponent is the negative
    of the described quantity: 2002116's (12) carries "exp[β(Σ int log int)]" while the gloss below
    reads "−Σ int_i R log(int_i R) is the entropy of the text context, the low the more clarity".
136. A symbol can be defined in prose with a subscript the equations then drop, and a constant change
    case between the two registers: 2002116 defines "Parameter θ0 ∈ [0, 1]" and immediately sets
    "θ = 0.5", every equation using θ; the normalisation constant is "Z" in prose and "2z(" in (13);
    REP/PEN/IMP print double-struck in the displays and plain "REP" in prose.
137. A record heading census can both abbreviate and drop: 2002116's `heading` string lists fourteen
    levels, opens with the previous chapter's "2.2 Notations", renders 3.2.1 as "Seed Words", 3.2.2 as
    "Contextual Entropy Block", 3.2.4 as "Proposed CE-VADER", 3.3 as "Combination of Measures" and 5.2
    as "Evaluating Success or Failure", and omits the chapter-5 title entirely - the one heading whose
    numeral the layout dropped.
138. A caption can assert a quantity the artwork does not carry: 2002116's Figure 13 is captioned as a
    "correlation between the star ratings with the helpful votes" over a five-spoke magnitude chart with
    no correlation axis, and Figure 8 is captioned as a "fuzzy evaluation system" over a crisp binary
    threshold tree with no membership functions.
139. A stated maximum can contradict the matrix printed beside it: 2002116 says "The maximum similarity
    is 14.3" in prose and in Figure 5's caption while the heat-map's maximum cell is 16.0, 14.3 being
    only the baseline (1,1)x(10,10) entry.

140. A printed paragraph can be split mid-sentence between two chapters, so each half belongs to a
    different record: 2003717's PDF 12 opens with the `assumptions` block "The reputation of a product is
    related to many factors (e.g." followed by "the average star rating it receives, …", and the model
    chapter resumes only at the next block with "Here we define a function R(ri)".
141. One body block can deliver two section headings after page furniture: 2003717's block 160 ends
    "… 关注数学模型 MATHmodels 获取更多资讯 Page 11 4 Problem 2 (b): Reputation Metric 4.1 Reputation
    Metric", so the chapter-4 title and its first subsection belong to the last unit of chapter 3.
142. A chapter can number half its equations and leave the other half unnumbered: 2003717 prints six
    unnumbered set-off displays (the weighted rating ratio, the argmin objective, ss_t, avg_i, std_i,
    PR_i) across its three measure sections and then (1)-(7) across its reputation and LSTM sections.
143. A chapter's number sequence can only close inside another chapter's block: 2003717's unit 55 ends at
    display (7) on p15 and (8) prints in `results` block 210 on the same page, so the model's own
    equations are (1)-(7) plus one belonging elsewhere.
144. One document can store four tables three different ways: 2003717's Table 1 and Table 2 are one block
    each holding a three-panel grid, Table 3 is one row out of phase over five blocks for six rows, and
    Table 4 packs its last four rows into one block ("The weight matrix for transitions b The bias for
    transitions σ The sigmoid function tanh The hyperbolic tangent function").
145. A gate equation can reuse another gate's weights: 2003717's display (6) prints the cell candidate as
    "g = tanh(W_ig x + b_ig + W_ho h + b_ho)", taking the output gate's hidden matrix and bias.
146. An index can be printed one letter off the one that makes the formula collapse: 2003717's std_i sums
    "(HN_j+1) × (ss_i − avg_i)²" over j ∈ A_i, so the term is constant inside the sum and the statistic
    cannot reproduce the spread panel it is drawn beside.
147. A subscript can print as the digit 1 where the index is t: 2003717's algorithm objective reads
    "S = argmin_S Σ_{t∈[T]}(y_1 − 1/(1+e^{Σ_{s∈S} s·1_s{re_t}}))²" while the line above maps ra_t to y_t.
148. A range can be asserted as closed when the function never attains its endpoints: 2003717's note says
    "the sigmoid function in logistic regression happens to symmetrically map R into [0, 1]", then maps
    five ratings onto {0, 0.25, 0.5, 0.75, 1} and leaves the printed score axis at -8 to +4.
149. A "hence" can skip the step that adds the discount: 2003717's consideration 1 promises "The older
    the review is, the less importance it is in PD_i", the printed PD_i carries no γ, and the PR_i that
    follows is γ-weighted - while γ^{1−t} with t a review index grows instead of decaying.
150. Prose can assert the opposite direction from the art: 2003717 says "the larger the window size m is,
    more violently the reputation curves fluctuate" while Figure 11 (m = 500) is smoother than Figure 10
    (m = 200) in every panel, and the three panels' axes span 0-10000 / 0-1400 / 0-17500 time steps so no
    common axis supports the comparison either.
151. A watermark string can carry the next page's folio and be booked as content: 2003717 stores
    "关注数学模型 MATHmodels 获取更多资讯 Page N" in blocks 123, 139, 149, 160, 169, 177, 192, 213, and in
    139 the N is the folio of the page after the block's start page, which is how unit 10 comes to own
    the next page's algorithm title.

152. A whole paper can come back with no `display` block at all: 2004647's model chapter is 136 `body`
    blocks plus one `heading`, yet it prints (1)-(23) contiguously, so every expression is a run inside
    prose and no display is stored as an object.
153. A display can lose its left-hand side in storage while the raster has it: 2004647's (23) prints
    `threshold^{(t)}_{i,k} = 0.5 − 0.1 e^{−(1/10)(t−τ)}` but block 202 begins "i,k = 0.5 −0.1e−1 10
    (t−τ) (23)", so the function name never appears in the text layer [R].
154. A chained equality can serialize as an open token run: 2004647's (20) is stored as "τK(X, Y ) ≜P −Q
    P −Q P + Q = (20) N(N −1)/2" - both fractions flattened, bars and grouping gone [R].
155. A gloss can be sign-shifted against its own formula: 2004647's (21) prints `p = 1/(1 + e^{−Rep̂})`
    and then glosses "where −Rep̂ is the predicted reputation", with "p(t) → 1 if −Rep̂ → +∞; while
    p(t) → 0 if −Rep̂ → −∞", which describes Rep̂ → −∞ giving p → 1 [R].
156. A table can be flattened into its caption block: 2004647's Table 5 keeps header, both outcome rows
    and three product columns as a single comma run, with no comma at the three wrap points, so cell
    boundaries cannot be recovered [R].
157. A caption block can carry the next section's title: 2004647's Figure 4 caption (183) ends with "5
    the Successfulness Prediction Model", and the record note credits that heading to block 185 instead,
    where nothing but "…predictions can be highly error-prone." prints.
158. A heading numeral can print after its title in the same block (2004647's only `heading` block reads
    "Deﬁnition of α—the Rating Vector 3.2") or alone at the tail of the preceding block (132 ends
    "…products). 3.3.1", 170 ends "…evaluated. 4.3.1"), so a five-word unit can be nothing but a numeral.
159. An equation number can be welded into the watermark string: 2004647's block 155 opens "(15) 关注数学
    模型 MATHmodels 获取更多资讯 We also take into account…", so the numeral and the tile share one run.
160. A figure's panel labels can be stored a unit before its caption: 2004647's "(a) (b)" sits at the end
    of body block 190 while Figure 5's caption is block 191.
161. A record's heading string can omit sub-levels the page prints: 2004647 lists twelve levels and drops
    3.3.1, 3.3.2, 5.2, 5.3 and 6, renames 4.3 "Evaluation of the Models" against the printed "4.3 Model
    Evaluation", and capitalises the article the page prints lower-case ("3 the RRBS Model").
162. Prose can cite an identifier one digit off its own table: 2004647's p17 writes "Hair dryer
    #767062995" where Table 5 prints "#768062995", the other three ids in the same sentence matching [R].
163. A watermark tile can clip body text rather than only carrying a folio: 2004647's bottom-right panel
    cuts words on p14 ("votality; th…"), p16 ("…successfulness predic- / tions could be inaccurate") and
    p17 ("…models' num- / bers of orders"), and the string is serialized inside blocks 185, 192 and 202.
164. A training window and its prediction window can overlap: 2004647 trims the series to "Jan. 2010 to
    Dec. 2014" and then predicts "its reputation after Jan. 2014", while the caption calls the horizon
    "a few years" for a one-to-two-year step.
165. A prose summary can round its own figure upward: 2004647 says "most of the calculated correlations
    are over 0.6" for 11 of Figure 4's 15 bars (two of the microwave group read 0.17 and 0.50) and calls
    the pacifier group "close to 0.8" with its fifth bar at 0.71 [R].

166. A chapter's own title can print at the end of a neighbouring chapter's block: 11325's "2 Methodology"
    and "2.1 Mathematical Model" both tail block 74, which the record labels `introduction`, and its own
    last block 102 ends "3 Results".
167. A heading can be split into a bare numeral that ends one block plus a five-word title-only block:
    11325 prints "2.2.1" at 90's tail with "Eﬀects of Changing Technology" alone in 91, and repeats the
    split at 96/97 ("2.2.3") and 100/101 ("2.2.6").
168. A table's column can print a header with no entries while the prose cites the source it should hold:
    11325's Table 2.1 has a `source` column with no cell filled, against block 75's "determined from
    current data for registered vehicles (North American Transportation Statistics Database, 2011)" [R].
169. A display can introduce a symbol case the formula does not use: 11325's effective-rate display prints
    `i = ieff = (1 + I/k)^k − 1` with a capital `I` while (4) on the same page uses lower-case `i` [R].
170. `heading` can be almost unused as a block kind: 11325 stores one heading block in 220 (block 104,
    "3.1 Economics of current BEVs vs. ICEs") while twelve levels print on pp. 8-11 as prose tails.

171. Two object-numbering series can run inside one chapter, so one number names two objects: 2009116's
    task 1 prints Tables 1-3 on pp. 10-11 and task 2 prints Tables 1-5 on pp. 12-15, and no prose pointer
    is numeric at all ("the table above" in 78, 86, 106; "the figure below" in 81, 126), so "Table 3"
    cannot be resolved from the text.
172. Prose can cite equation numbers that belong to a bullet list: 2009116 prints "(1)", "(2)", "(3)"
    only on the three sentiment dictionaries in blocks 62-64, and block 114 then writes "Substituting the
    above formulas (1), (2), (3) into" for F1, F2 and F3, which are numbered nowhere.
173. A table can be stored as a caption with every cell missing, and this recurs: 2009116's p9 star
    frequency grid and its p12 7 × 7 correlation matrix have no cells in the text layer, and 2010638's
    Table 3 keeps caption and note over an eight-row coefficient grid that exists only on the raster while
    its Table 10 keeps caption and three row labels over fifteen eight-digit ids [R/T].
174. A table titled "Top 10" can print nine rows: 2009116's Table 5 is "Pacifier Top 10 Products" with
    nine ranked entries, and its text layer additionally drops three PRODUCT_PARENT ids the raster prints
    (ameda 985518895, baby jogger 242140507, Vintage Teaberry 460235866) [R/T].
175. A percentage column can be truncated to force each row to 100: 2009116's p9 grid prints 286/1,536 =
    18.6% as "18%" [R].
176. A cumulative column can be off by the last digit of its own rounding: 2009116's Table 3 prints 53.141
    where 31.025 + 22.117 = 53.142, and 69.738 where the first three shares give 69.739 [R].
177. Section numbering can print out of order on the page: 2009116 closes block 97 with "3.3 Problem
    Solving" and then prints "3.2.1 Determination of star rating index CR" as the whole of block 98.
178. A component assignment can contradict the expression printed for it: 2009116's block 106 puts
    `number` in both F2 and F3, while block 109 prints "F3 = 0.786v + 0.726vp" with no `n` and Table 4
    carries `number`'s .503 only under column 2 [R].
179. A weight vector can contradict the prose ordering it is meant to encode: 2009116's CS weights are
    0.3 (day) / 0.3 (F1) / 0.1 (F2) / 0.3 (F3), against block 110's "voting information is the main
    factor …, followed by the content …, and finally the customer identity" [R].

180. A table's caption can print below the grid it labels: 2010638's Table 3 prints its caption and note
    under the eight rows, so the text layer's caption block arrives after the cells it names [R].
181. A header row can print the same three labels twice with nothing separating the halves: 2010638's
    Tables 5 and 6 each run `Theme 1  Theme 2  Theme 3` across one row twice, six columns for three
    themes, and no sentence says what divides the two halves [R].
182. A table can print half the cells its own prose promises: 2010638 promises "10 most frequently used
    words and their corresponding probability" per topic and the grids hold five words and no probability.
183. A table row can print the same identifier twice while the prose promises distinct items: 2010638's
    Table 10 microwave row prints 423421857 twice, four distinct brands against block 140's "only 5
    first-class brands of each product" [R].
184. A judgment matrix can print non-square, with a column whose row does not exist: 2010638's Table 8
    heads six criteria over five row labels, so no weight and no consistency ratio can follow from it [R].
185. An equation can define the matrix from the answer it is meant to produce: 2010638's (8) sets
    `A = [W_i/W_j]` out of the weights that (10)-(11) then recover from A, and the expert matrix of Table 8
    is never connected to it [R].
186. A product's dummy index can collide with its row index: 2010638's (9) prints `M_i = Π^n_{i=1} a_ij`,
    a product that must run over j [R].
187. A "cosine" can be printed with one variable squared in both factors: 2010638's (16) has denominator
    `√(Σ x_ij² · Σ x_ij²)` under a numerator `Σ x_ij x_ik`, so the second factor must be x_ik [R].
188. A piecewise definition can double-count its boundaries and leave part of the support unassigned:
    2010638's (4) closes and reopens at 0.75, 0.50 and 0.25 with `≤` on both sides and assigns nothing to
    compound scores below 0, a variable defined on [−1, 1] [R].
189. An abbreviation column can contradict the symbol the prose defines, or reuse a symbol that means
    something else in the same chapter: 2010638's Table 3 prints "SS" for star-rating square where block 85
    says "SQ", and prints "CS" for review-length square where block 114 uses CS for customer satisfaction
    [R].
190. A coefficient table can print blanks under a sentence claiming every variable is significant:
    2010638's block 92 says "each variable passed the significance test" over a Table 3 whose Model 1
    leaves count, CS and compound empty, and whose note defines an `ns` key no cell uses [R].
191. A negative linear term with a positive square term can be read as "inverted U" when it is convex:
    2010638's block 94 turns -0.020** and +0.002** into "reviews with high helpfulness ratings should be of
    moderate length", but a positive square term puts the maximum at the ends of the range [R].
192. An uncaptioned diagram can print with numbered nodes and be read by no unit: 2010638's p12 carries a
    four-chevron Step strip and a six-node circular diagram numbered (1)-(6), neither captioned nor coded.
193. A section numeral can print with no space after it: 2010638's p15 prints "4.4System Clustering
    Analysis" while the same heading is stored with the space [R].
194. Two columns of a descriptive table can share one header word with no unit: 2010638's Table 1 heads
    its last two columns "Count" and "Count average" over 4,841,870 / 256 and leaves "Helpful votes
    average" holding values that are sometimes below 1 and sometimes above 5 [R].
195. Section headings can be stored as blocks no chapter owns: 11422's 21 printed headings leave six
    `heading` blocks (53, 88, 90, 108, 115, 125) in the span of `model-establishment`, and not one of the
    six is claimed by any chapter object in the record, so the headings print and vanish.
196. A chapter can own neither a `heading` block nor a `display` block while printing twenty-one headings
    and eighteen equations: 11422 stores all 55 of its blocks as `body`, so every heading is a tail weld
    and every equation a run inside a sentence.
197. A chapter's pages can print nothing the chapter owns: 11422's pp. 9 and 16 carry a cellular-automaton
    screenshot, an Excel chart and a cost plot, and the chapter's own blocks stop before each page.
198. Table cells can rotate one place against their row labels in storage: 11422's block 94 puts the
    carbon-monoxide Difference at the end of the carbon-dioxide line, leaves the carbon-monoxide line two
    values short, and trails "Mercury" after its own three numbers [T].
199. An equation can be split between a sentence's tail and its own display: 11422's block 100 ends
    "as: + 12i · L2" - the numerator's last term - and block 101 opens with the display that needs it,
    losing the operator between the two fractions [R/T].
200. A table can print one figure a decade below its own components: 11422's p18 alpha = 200,000 grid
    prints Total Cost 1.28032 · 10¹¹ for seed 0.1 where Seed + Power Grid sum to 1.28033 · 10¹², and the
    other twenty cells of the same column close to 2 · 10⁻⁶ [R].
201. A column of one table can contradict a total printed three pages earlier: 11422's p13 Current
    Production column sums to 38.300 QBTU against the 38.075 the p10 prose reports for the same five
    sources [R].
202. A cost column can be evaluated at the wrong year relative to its own prose: 11422's seeding column is
    linear at 1.0327 · 10¹¹ per 1% at t = 60, while the text seeds "in 2011" (t = 61) and one row implies
    8.19333 · 10⁸ cars against 8.19600 · 10⁸ for every neighbour [R].
203. A conversion factor can be asserted with no derivation while the chapter's own data imply another:
    11422's F(t) = 12,200/(31 · 20) leaves the 20 unexplained, and the paper's own 2.49 energy ratio
    implies 31 · 2.49 = 77 mpg-equivalent [R].
204. A figure legend can occlude its own plot area: 11422's p17 legend box sits inside the axes over the
    lower-right marks from roughly alpha 60,000 to 100,000, while the p15 top panel's box sits outside the
    axes and hides nothing [R].
205. A chapter run description can claim contiguity across blocks another structure owns: 11422's record
    note says "five runs … 89 to 116", but 90, 108 and 115 are orphan heading blocks, so the chapter is
    nine runs.
206. A `display` block kind can mean "subfigure caption strip": 2101166's six display blocks (59, 110,
    129, 140, 168, 169) are all caption lines and none of them is an equation, so the kind name points the
    wrong way.
207. A heading can be welded onto the object it introduces: 2101166's "3.1 Method Overview" ends block
    58, the Table 1 block, so the heading arrives attached to the table it labels.
208. A `heading` block can hold nothing but a watermark string and belong to no chapter: 2101166's 132
    (0 words, "微信公众号：数学模型") and 155 (1 word, "微信号：MATHmodels"), both printed inside the
    chapter's own page range.
209. A table can be split by a figure printed between its halves: 2101166's Table 1 runs through blocks 58
    and 61 with both subcaptions and the caption of Figure 2 in between, and both halves interleave the
    table's two column pairs ("C the set of cells Ei Nt the set of nests Ci r the growth rate γ"), so
    each symbol meets an interpretation that belongs to its neighbour [R/T].
210. Algorithm line numbers can rotate into the preceding line's tail, because each pseudocode line is its
    own block: 2101166 stores "... do 3" ending block 83 and "9 Add j into Nt+1; 10 end 11 ... end 12"
    inside block 89, so every stored line opens mid-statement [T].
211. A numbered equation can lose its left-hand side in storage: 2101166's block 166 holds only
    `max{a(i), b(i)}, (13)` while the page prints S(i) = (b(i) - a(i)) / max{...} [R/T].
212. A table row can close only at a different exponent from the one it prints: 2101166's Table 2 prints
    both SS cells as 10⁸, but MS x df = 1.097 x 10⁷ and the column sums close only at 10⁷ [R].
213. A printed equation can be unable to draw the figure it accompanies: 2101166's (7) gives f(t₀) = N and
    f → 1 with a pole just before t₀, while Figure 3(g) climbs from 0 to 600 and the gloss calls N the
    "stable population" [R].
214. A superscript footnote marker can be absorbed into a numeral by the text layer: 2101166's p11 prints
    "the number of positive sightings is only 19" with a raised 3, and the layout stores "only 193" -
    a false contradiction unless the page is read [R/T].
215. A QR overlay can halve an equation number: 2101166's p15 prints (12) across the top border of the
    bottom-right panel, the lower half of the numerals on the pink fill [R].
216. Bar heights can contradict the counts they are meant to plot: 2101166's Figure 6(a) sums to about
    1,891 against the 2,043 negatives it describes, and Figure 6(b) to 11 against "only 19" [R].
217. A figure's axis title can contradict what the axis plots: 2101166's Figure 9(a) is titled "Loss" over
    an axis running 0.3 to 0.9 that carries the test-accuracy curve [R].
218. One cluster can be given two contradictory readings by consecutive pieces of advice: 2101166 tells
    the government that observations near "cluster 1 or 3" are "most likely to be negative" and that
    observations near "cluster 3 or 4" may be positive, while Table 3 gives cluster 3 a priority of 0.0746
    and Rank 4 [R].
219. A stated range can exceed the plotted one: 2101166 says "the number of clusters varies from 2 to 9"
    over a Figure 12(a) whose axis and seven markers stop at 8 [R].
220. A tensor shape can be given twice in one paragraph with incompatible exponents: 2101166 prints
    `x2 ∈ ℝ^{2C} × ℝ^{H/2} × ℝ^{W/2}` and, nine lines later, `(2⁴C, 2⁻⁴H, 2⁻⁴W)`.

221. Table cells can be cut between a row's symbol and its description, so each unit holds one description
    and the next row's symbol: 2101587's Table 1 prints nineteen rows and stores them as fifteen units,
    with the last description welded in front of the next heading, one unit carrying two symbols and one
    carrying none [R].
222. Two tables can be flattened into one block so their cells share units: 2101587's Tables 2 and 3
    store `λi 3.02` and `CRj 0.016` between the matrix's caption and its column labels, inject `CRj`
    after row 1's values and detach all three row labels, and Table 3's `W` stub is never defined [R].
223. Two tables with different content can carry the same caption: 2101587's Table 4 and Table 5 are both
    "ResNet Accuracy", and only Table 5's new row is set bold with no sentence explaining the emphasis [R].
224. Percentages can resolve to a denominator that contradicts the stated split: 2101587's processed rows
    are exact multiples of 1/107 (18.69 = 20/107 ... 92.52 = 99/107) although the text holds out one tenth,
    while its other rows need denominators of at least 1,504 and 459 - three set sizes inside one table [R].
225. A row can print the same value in all three columns: 2101587's Table 6 gives `99.60%` for 18, 34 and
    50 layers, and 99.60% of the 260 evaluation images it implies is 258.96, not an integer [R].
226. A heading can lose its numeral and attach to another chapter's block: 2101587's "3 Abbreviations and
    Symbols" is the tail of `assumptions` block 53, printing as "Abbreviations and Symbols" after the
    watermark string, so the chapter's own heading sits outside its block range [R].
227. A schematic's own labels can contradict its kernel arithmetic: 2101587's Figure 6 prints `127 x 127`
    twice where 7x7 kernels at stride 2 on 256 give 125 and 5x5 kernels on 127 give 123, drops the kernel
    count 64 to 16 while the map count rises, and shows no pooling or loss layer although the sentence
    above it lists both [R].
228. A figure's axis can run past the model's own support with no axis titles: 2101587 caps worker patrol
    at 8 km, searches a 10 km disc and plots Figure 1 to x = 20 km, the curve being the λ = 2 Poisson pmf
    with λ never printed and neither axis named [R].
229. Prose can invert the weights of its own AHP table: 2101587 says trees and terrain outweigh distance
    while Table 3 gives Distance 0.285 > Elevation 0.217, and its matrix is intransitive (a12·a23 = 1.0
    against a13 = 1.5) although CR = 0.016 certifies it [R].
230. Two result maps can be the same basemap with the same hotspots: 2101587's Figures 3 and 4 print the
    same Puget Sound relief and the same three lobes (0.56 cross-correlation), differing in core intensity
    only, so "existing nest" and "next year's nest" are told apart by colour [R].
231. A table can be read as a gain of the same model when it switches task: 2101587 calls 90.65% "a much
    more acceptable value" against 25.23% without saying the first is a binary task and the second a
    thirteen-class one [R].
232. A chapter can end a page short because the closing heading was given to the next chapter: 2101587's
    record says `pages [6, 11]` while units 62-66 print on p12 and the 5.4 heading is block 121 of
    `results`, the same truncation shape as 2010638's nine-level heading string [R/T].
233. A definitional gloss can name a statistic wrongly and survive into use: 2101587's Table 1 glosses `CRj`
    as "The coincidence indicator (used in AHP)" and p9 uses it as a consistency ratio, in a chapter that
    also expands AHP as "Analytic Hierarchy Processing" [R].

234. An equation numeral can be reused verbatim while the next numeral in sequence was already spent two
    pages earlier: 2107815 prints `(Eq. 4-5)` on p7 and again on p8 with identical content, and `(Eq. 4-6)`
    already carries the number between them, so the run reads 4-1..4-6, 4-5, 4-7 [R].
235. A piecewise function can be written over the wrong variable and fail to meet itself at its own branch
    point: 2107815's Eq. 4-7 defines confidence in `d`, divides its second branch by `x`, and at the shared
    boundary d = d_max + 30 = 50.9638 evaluates to -24.48 on the first branch and 0.50 on the second, while
    its own figure traces the second branch twice [R].
236. A case list can double-assign an interval and leave one case with no interval at all: 2107815's Eq. 4-3
    gives `Jun - Jul` to both a2 and a4 and puts November in both the zero branch and the a5 branch [R].
237. Figure panels can total a different population than the bar chart that introduces them, and exceed the
    stated dataset: 2107815's Fig.3-3 monthly labels sum to 15 for `POSITIVE ID` against Fig.3-1's 11, and to
    2,286 for `UNVIREFIED` against Fig.3-1's 68 and against the 2,127 records the footnote prints [R].
238. A map panel can be drawn at a scale that cannot contain the radius the prose claims, so the claim is
    unverifiable on the artifact itself: 2107815's Fig.4-2 circle spans about 0.12-0.14 degrees (13-15 km N-S,
    9-10 km E-W) against the paragraph's 30 km activity radius, and its y axis covers only 28 km in total;
    the sibling Fig.4-3 prints its distance axis as a bare `data` with no unit at all [R].
239. A coordinate can lose a leading digit and leave the figure that is supposed to show it: 2107815 prints
    `(48.777534 N, 22.418612 W)`, a longitude in the Atlantic where every other value is about 122.4 W, with a
    latitude below the 48.9-49.15 range of Fig.4-2's own axis [R].
240. A table can be split so the grid prints with no number and no caption while the caption prints after the
    continuation, one page later: 2107815's p9 grid (11 rows by 6 columns, header rules only, no bottom rule)
    carries no title at all, and `Table.4-1` prints on p10 after the three-row `display` block [R].
241. A per-column rate can be attached to the wrong column of the table that produces it: 2107815 says "the
    accuracy of positive ID is higher than that of negative ID, which is 84.6%", while its grid labels all
    thirteen positive-ID locations correctly (13/13) and 84.6% is the negative column's 11/13 [R].
242. A pair of per-row confidences can sum above 1 in most rows of a two-class table without any row being
    flagged: eleven of 2107815's thirteen Table.4-1 rows exceed 1 (up to 1.7987), and the only two that fall
    below 1 (0.9411, 0.9699) are correct classifications, so the error has no pattern a threshold explains [R].
243. Formatting can be the only marker of an error, invisible in the text layer: 2107815's single misclassified
    cell (Location_8, positive-ID inside the negative block, 0.749729) is the only result cell not set bold [R].
244. A heading level can be set at body size so the printed hierarchy flattens exactly where sub-subsections
    begin: 2107815 grades 16 pt for `4`/`5`, 14 pt for `4.2`/`4.3` and then 12 pt for `4.3.1`/`4.3.2`, with no
    other cue but the numeral [R].
245. An overlay panel can eat printed characters while the text layer keeps them: 2107815's 3.1 lead-in runs
    under the white QR field and then the opaque pink block on p4, so the line stops at "browsin" against the
    layout's whole sentence, and the p9 grid's last cell (`0.127481`) loses its closing digits the same way [R].
246. A closing sentence can name a different model than the one just trained: 2107815's p14 reports the CNN's
    91.75% test accuracy as "the text identification model can accurately complete the classification" [R].

247. A chapter's page window can exclude its own blocks, so the window looks copied from the stored sample
    rather than from the coded groups: 2107870's `pages [7, 16]` against blocks that print on PDF 4-16, i.e.
    folio pages 2-14, with the envelope sampled at twelve units while seventy-nine are coded [R/T].
248. A chapter title can be welded into a block another chapter owns, so the chapter holds its own name but no
    block that carries it: 2107870's `3 Image Classification` is the tail of block 96, filed under
    `assumptions`, one printed page after the chapter's real start [T].
249. A grid can be captioned as a figure and a figure can be nothing but a grid, so a chapter with two grids and
    six figures has no object captioned as a table at all: 2107870 captions its nineteen-row k sweep
    `Figure 2: k-Value Analysis` and its Keras `model.summary()` screenshot `Figure 4: CNN Model Summary` [R].
250. Two figures can carry verbatim identical captions and neither caption can order its own panels: 2107870's
    Figures 5 and 6 both read `Box Plots for Unlabeled, Positive, and Negative Probability Distributions.`
    while the panels run positive/negative/unlabeled and negative/positive/unlabeled [R].
251. A numbered display can be missing a derivative or a factor, with the numeral standing over the error:
    2107870's only numbered equation, the Fisher equation `(1)`, prints `d2N/dx2` for both spatial terms, so
    the y-derivative is gone [R].
252. A table's own row can contradict the probabilities derived from it two lines later, both printed on the
    same page: 2107870's k = 17 row (accuracy 9/14, FP = 0) forces TN + FN = 5, while P(TN) = 0.5833 and
    P(FN) = 0.4167 are 7/12 and 5/12 and need 12 [R].
253. A named probability can be defined as a count over the wrong class's count: 2107870 prints
    `P(TN) = TN/(FN+TN)`, which is neither specificity nor negative predictive value [R].
254. A threshold can be iterated across pages while the equation swaps its two quantities, so the criterion
    fires everywhere: 2107870's fifth case reads `1 if lat > -122.06 or long < 46.7`, where every Washington
    latitude exceeds -122.06 and every longitude is below 46.7, and the same bound prints as -121,
    -122.06 and -122.063 in three sentences, with 46.7 against 46.77 [R].
255. A symbol can serve as both a set's name and an index into itself: 2107870's unification equation conditions
    a case on `i in M_i` where `M_i` is the image mapping and `i` the GlobalID [R].
256. A chapter can number the background equation and leave its central metric unnumbered: 2107870 prints
    `(1)` on the Fisher equation of its last section and nothing on the five-case Model Unification Equation
    that every other section exists to feed [R].
257. A chapter's central equation can be cut by a block filed under another chapter, so the equation is whole
    on the page and in three pieces in the record: 2107870's unification runs block 181 (chapter), 182
    (`problem-analysis`) and 183 (chapter) [T].
258. Two algorithms in one chapter can disagree on the same preprocessing ratio, and neither figure is used:
    2107870's section 1.4(c) under-samples the majority to "equal amounts", Algorithm 2 to "two-thirds of
    their original sample-size" [R].
259. A step list can print the same step number twice: 2107870's Algorithm 1 runs 1, 2, 3, 3, 4, 5 [R].
260. A sentence can send the reader to a section number that the heading contradicts: 2107870's Algorithm 2
    says `see section 1.5` while the cleaning section is numbered 1.4 on the page that introduces it [R].
261. A figure can show a distribution with zero spread where the method promises a spread: 2107870's Figure 6
    negative panel collapses to a flat line at 0.50 with no whiskers, against a keyword scheme with eleven
    terms at 0.05 that would leave 0.30-0.85 reachable [R].
262. A labelled radius can be contradicted by the extent it is applied to on the next page: 2107870 says the
    area of interest "lies within 23.63 km circle" and, one paragraph later, that the furthest point "would be
    located 29.22 km away" [R].

263. A chapter's page window can stop one page before its own last groups: 2109298 records `pages [4, 20]`
    while units 102-103 print on p21, with the closing sentence and the next chapter's heading in block 182 [T].
264. A section's opening paragraph can be filed under the neighbouring chapter while its heading stays behind:
    2109298's `5 Identiﬁcation of Mistaken Classiﬁcation` (block 120) is followed on the page by block 121, the
    section's own opening paragraph, which the record assigns to `problem-analysis`, so the chapter jumps from
    `5` to `5.1` [T].
265. A chapter's own numbered section heading can be the tail of another chapter's block: 2109298's
    `3 Data Exploration 3.1 Data` closes block 29, owned by `assumptions`, and the chapter's first block opens
    mid-section with `Examining the data ﬁles` [T].
266. A figure can carry panel labels and no caption at all, and be cited by a bare panel letter: 2109298's
    Figure 4 exists only as `(a) report distribution (c) population statistics (b) population distribution` in a
    `display` block, the string `Figure 4` never occurs, and the prose cites it as `As we draw all the sightings
    on 4a` [R].
267. A grid can be specified so that its cell size and cell counts cannot cover its own printed bounding box:
    2109298 prints 12 km cells, 45 x 65 = 2925 cells, and the box (45.09-49.95 N, -124.65 to -116.87 W), where
    the latitude axis matches at 45 cells and the longitude axis needs 48.8 cells for 585 km, not 65 [R].
268. A per-step reproduction rate can contradict the seasonal growth stated as its own justification: 2109298
    sets `r_summer = 1.05` with one step = one day, i.e. 1.05^183 per half-year, and justifies it by "the peak
    of a new AGH colony is roughly triple of its initial amount at the beginning of the year" [R].
269. A difference equation can assign a quantity to itself at the same time index: 2109298 prints
    `N_cur(t) = N_cur(t) × r` as `(5)`, while `(6)` and `(7)` write `t+1` on the left [R].
270. A two-dimensional Gaussian can be normalised by the one-dimensional factor: 2109298's `(2)` and `(11)`
    both print `1/(√(2π)σ)` over a sum of two-dimensional exponentials [R].
271. An equation numeral can be spent on a parameter list, and the fitted parameters can sit orders of magnitude
    below the plotted series: 2109298 numbers `p = −0.18054375, q = ..., r = ..., c = ...` as `(13)`, and that
    curve tops out near 0.23 against Figure 17's bars up to 1370 [R].
272. A train/test split can overlap and invert: 2109298 trains on 2019-09-19 to 2020-05-15 and tests on
    2019-05-16 to 2020-10-01, so the test window opens four months earlier and contains the training window,
    against "we split all images by 'before and after a certain moment'" [R].
273. A table column can change unit without a note, and its values can be impossible percentiles: 2109298's
    Table 2 prints means as `15% / 5%` and the standard deviation beside them as `0.15 / 0.1`, which no
    distribution with a 25th percentile of 8.8% and a 75th of 16.6% admits, and the caption's "Each entry is of
    the form pos% / neg%" is false for that column [R].
274. A section can print the conditionals with their arguments exchanged: 2109298's 5.4 writes
    `P(R|H, I) = P(H|I)` and `P(R|H) = p/(p+q)` where `(8)` and `(10)` derive `P(H|R, I)` and `P(H|R)` [R].
275. One letter can bind three quantities and one word two: 2109298 uses `a` for the activity degree
    (`a_summer = 0.3`), for the weight in `a·P_bayes + (1−a)·P_image`, and for that weight in Figure 18's
    legend, where the parenthesised `alpha = 0.85` is the AUC and the caption calls the weight `α` [R].
276. A flowchart can state a sign condition that the parameter table contradicts: 2109298's Figure 6 prints
    `Reproduction; r<0 in winter; r>0 in summer` while 4.1.4 sets `r_winter = 0.995` [R].
277. Panel-label `display` blocks can be stored in extraction order rather than print order: 2109298 stores
    Figure 2's four labels as b, a, c, d and Figure 15's as a, d, c, b, both printing a-b-c-d [R].
278. A figure's caption block can be spliced into the middle of a sentence: 2109298's block 33 ends `we apply
    the Latent Dirichlet Allocation`, block 36 holds the panels and caption, block 37 resumes `(LDA) model [3],
    capable of extracting topics and keywords from texts.` on the same page [T].
279. An update can retain and distribute the same mass, inflating the total each step: 2109298's `(6)` keeps
    `(1−a)N` and `(7)` then hands `N(t+1) × T` to the neighbourhood with `ΣT = a`, so every cell keeps
    `(1−a)N` and its neighbours receive `a(1−a)N` that was never subtracted [R].
280. A width can print as a difference of a symbol with itself, in prose and in display, circular with the count
    it defines: 2200401's page 8 reads `the minimum width of grid l_0 = (p_max − p_max)/num_0` in-line and
    `num_0 = (p_max − p_max)/l_0` in the display below it, so both are zero at every count and each is defined
    from the other [R].
281. A quantity named a minimum can be defined as a maximum: 2200401's `l_0 = max{inf{g_1}, inf{g_num}}` is
    called "the minimum width of grid", but the gap conditions require the width not to exceed either gap, so
    the operator should be `min` [R].
282. A bound can nest one fraction inside another, under an oversized unmatched delimiter: 2200401's
    `g_num ⩾ (1 − 1/(1/(1−α)^2 + r_0)) p_max` puts `1/(1−α)^2 + r_0` in a denominator inside a subtraction,
    while the `g_1` bound beside it opens with an over-tall left delimiter that closes nothing [T].
283. One count can carry three symbols in four lines: 2200401 derives `num_0`, then divides the isometric
    grid-line formula by plain `num`, while the input count is `num_in` - the derived quantity is used under a
    name that belongs to another quantity [R].
284. A parameter can exist only inside an exponent and never be defined: 2200401's `α` appears only in
    `(1−α)^2`, is nowhere given a value or a meaning, and the prose that motivates it argues the opposite
    constraint ("we have cannot make the width for every grid to be too small") [R].
285. Comparison panels can be drawn on different y-axes with identical framing: 2200401's Figure 2 gives the
    isometric panel 1-7 and the proportional panel 1-8, so equal heights are different prices and the visual
    comparison the caption promises is not available [V].
286. The secondary axis that carries the compared count can differ between panels by a factor of four:
    2200401's Figure 3 plots `exchange times` on 2-12 for ISO and 0-50 for Pro, and the sentence drawn from the
    picture is a claim about which model exchanges more [V].
287. A figure caption and the section heading that governs the chapter's last unit can be stored in one short
    block owned by a neighbouring chapter: 2200401's block 109 holds `Figure 5: Prediction of ARIMA model` and
    `5.2 APGM` with six words total, so the chapter's one fitted model is filed under a section it does not open
    and whose heading it does not contain [T].
288. A pointer can point past its own chapter: 2200401's block 108 says `Our result of prediction is shown as
    the following Figure 5` while the caption and the figure's block sit outside the chapter's block list, six
    blocks after its end [T].
289. A time index can print as literal braces when `\{` is consumed as a glyph: 2200401's p12 shift formula
    reads `p̃_i^{{t}} = p_i + ω(MA^{{t}}(N) − MA^{{t−1}}(N)) + μ(ARIMA^{{t+1}} − ARIMA^{{t}})` [T].
290. Two adjacent x tick labels can print on top of each other: both of 2200401's Figure 3 panels end
    `2017-022017-03` with no gap between the last two month labels [V].
291. A worked toy can be wrong in a way its own follow-up line hides: 2200401's toy prints
    `5.43 + 5.26 + 2 × 7.48 = 25.95` (summands give 25.65) and the next line is arithmetically right for the
    printed 25.95, so the error carries forward without a visible break at the point it was made [R].
292. A step list can print its numbers out of order rather than duplicated: 2200401's Algorithm 1 runs
    1, 2, 3, 4, 5, 6, 7, 9, 8, 10, 11, with `9. Else a^{t} ← Hold` above `8. t ← t+1` - the neighbour of class
    259 (same number twice), and its Input/Output lines both stop the range at `T_start` [T].
293. One letter can carry three quantities across a single chapter: 2200688's `t` is the time index of every
    equation, the Laplace scale in (16) (`t > 0 denotes the scale parameter`) and the holidays prior scale both
    in the notation table and in `k = Normal(0, t²)` [R].
294. A letter can be a scalar in one section and a vector in another: 2200688's `k` is `the growth rate` in the
    table, (2) and (6), and `k = (k_1, ..., k_L)^T` in (15), initialised as `Normal(0, t²)` with one scalar
    variance for L components [R].
295. A density can print without brackets around its denominator, changing the expression: 2200688's (16) reads
    `f(x|θ, t) = exp(−|x − θ|/t)/2t`, which divides by 2 and multiplies by t where the Laplace density divides
    by 2t [T].
296. A summand can lose its operator to a stray asterisk: 2200688's (13) prints
    `c(t) = m(t)k = Σ_{i=1}^{L} * I_{l∈D_i}`, and `m(t)k` multiplies a vector by a vector with the product
    unstated [T].
297. A model named for a mechanism can contain none of it: 2200688 calls (6) `A model based on segmented linear
    functions` and prints `a(t) = (k + z(t)θ)·t + (m + z(t)^T γ)`, one straight line with a constant offset;
    segmentation re-enters only as the changepoint settings and never returns to the equation [R].
298. A transpose can drift between two forms of the same product on one page: 2200688's (2) multiplies
    `z(t)'θ`, (6) multiplies `z(t)θ` in one term and `z(t)^T γ` in the next, while (3) defines z(t) as a column
    vector [R].
299. A notation table can define ten of the chapter's twenty-five symbols and omit every symbol of the sections
    that follow: 2200688 lists a(t) to t and leaves out z(t), θ(t), γ(t), s, I, p, δ, x(t), a_i, b_i, L, D_i
    and the three changepoint settings [R].
300. A Fourier order can be cut between two cases with no rule: 2200688 sets I = 10 for the yearly period and
    I = 3 for `a sequence with a weakly period`, and no sentence says what chooses the order [R].
301. A prior scale can be described as an effect: 2200688 glosses β as `seasonality prior scale` and then says
    `a larger value of β indicates a more pronounced effect of seasonality`, which conflates a prior width with
    model behaviour [R].
302. A figure's box labels can be swept into an equation block in scrambled order: 2200688's block 58 ends
    `Page 7 Modeling Visually Forecast Inspect Evaluation Forecasts Surface Problems`, which is Figure 3's five
    boxes with `Visually Inspect Forecasts` split across the run and the boxes interleaved - the flowchart
    cousin of class 277 [T].
303. A borrowed figure can be cited in the body for something it does not show: 2200688's caption credits [1]
    with an analyst-in-the-loop workflow while the pointer sentence reads `As shown in Fig. 3. The algorithm is
    designed based on time series decomposition and machine learning fitting`, and no figure in the chapter
    shows a decomposition [V].
304. Figure numbering can start above 1 because earlier chapters spent the low numbers, so the modelling
    chapter's own diagram becomes a higher number and prints in the next chapter: 2200688's chapter starts at
    Figure 3, and Figure 4 (the X-Prophet flowchart) sits on p9 under `model-improvement` [T].
305. A heading can be the chapter's last block, leaving a section with no content behind it: 2200688's block 73
    ends `Page 9 4.1.3 Improvement Prophet - X-Prophet` and every word of that subsection prints under
    `model-improvement`, so the record's page window ends on a page the chapter does not occupy [T].
306. One equation can be split across two blocks eight apart: 2203120's (5) has `S_j = √…` in block 134 and its
    radicand `Σ_{j=i−30}^{i−1}(A_i − (ΣA_i)/30)²/30` in block 142, at the far end of the chapter [T].
307. The numerals of a whole subsection can be stored in one trailing block while the formulas they number sit in
    earlier blocks: 2203120 holds (6), (7), (8) and (9) in block 142 and the formulas in 135-141 [T].
308. A chapter's own notation glossary can print outside its page window: 2203120's block 142 spans PDF 10-11,
    so W_j, m_j, A_j, λ, S_j and the constraint readings print on printed p10 while `pages [6, 10]` stops at
    printed 9 [T].
309. A coefficient of determination can lose its `1 −` and keep its gloss: 2203120's (3) prints
    `R_i² = Σ(x_{i,j} − Y_(i))²/Σ(y_{i,j} − Y_(i))²` and the paragraph says `the closer the index value is to
    1, the higher the fitting performance`, which under that formula means the opposite [R].
310. A test can be read backwards: 2203120 states `The p value of the white noise test output of this model is
    very close to 0, indicating that ... it is a white noise`, where a p near zero rejects the white-noise null -
    and the chapter's own rule two blocks earlier says a pass means the information has been extracted [R].
311. A reading can name truncation levels that contradict both the fitted order and the printed panels:
    2203120 says gold uses `level 2 ACF and level 1 PACF` (which gives ARIMA(1,1,2) under its own Table 3),
    prints ARIMA(2,1,1), and Figure 4(a) shows one ACF spike outside the band and at least four later PACF
    spikes [R/V].
312. A recurrence can spend a value from the next period: 2203120's cash update uses `Y_g(i+1)` and
    `Y_b(i+1)`, the next cycle's actual price, to compute the proceeds of a sale [R].
313. Two recursions can define each other with no evaluation order: 2203120's `C_i = C_{i−1} − G_i × w_g` needs
    `G_i` and `G_i = G_{i−1} + C_i × w_g × (1 − α_g)` needs `C_i` [R].
314. A holdings recursion can start from the other asset and contain itself: 2203120's bitcoin line reads
    `B_i = G_{i−1} + B_i × w_b × (1 − α_b)` and its sell branch `G_{i−1} − G_{i−1} × m_b`, so bitcoin is
    seeded from the gold stock and `B_i` sits on both sides of its own equation [R].
315. A dispersion index can cancel to a constant multiple: 2203120's (5) squares `A_i − (Σ_{j=i−30}^{i−1}A_i)/30`
    inside a sum over the same window, so every summand is identical and `S_j` is no longer a standard deviation
    of the portfolio [R].
316. One index letter can carry three units inside one subsection: 2203120 uses `j` for the cycle in the
    objective and constraints, for the day in its own glossary (`A_j represents the total assets on day j`) and
    for the look-back index inside (5) [R].
317. A coefficient in the objective can be defined after the objective and never valued: 2203120's λ appears in
    (9) and is glossed four blocks later on the next printed page as `the coefficient of regular term`, with no
    value chosen anywhere [R].
318. A fee can be described as taken from one side and applied to the other: 2203120 says `The Commission is
    deducted from the amount paid instead of being given separately`, then multiplies the gold received by
    `(1 − α_g)` on a buy and the cash received by `(1 − α_g)` on a sell [R].
319. A truncation rule can be defined as a fraction inside a band: 2203120's NOTE reads `Truncation means falling
    within the confidence interval (95% of the points comply with the rule)`, which describes white noise
    rather than a cut-off in the ACF or PACF [R].
320. One heading can be split number-versus-title across two blocks: 2204883 prints `4.3.2` at the tail of 128 with
    the title `Investment Strategy Based on The MLP Model` opening 129 [R].
321. One heading can belong to two records: 2204883's `4.3.3` rides the tail of the chapter's last block 163, while
    the title and body `4.3.3 The Result of Our Investment Strategy` open `results`, so the window ends on a page
    whose only chapter content is a swept number [R].
322. A chapter can promise five parameters and tabulate three: 2204883 says `we adjust the values of these 5
    parameters separately`, naming `l`, `d`, `d′`, `λ`, `ϵ`, and Table 3 has columns for `d`, `d′`, `λ` only [T].
323. A parameter scan can return its own seed: all three of 2204883's Table 3 columns bottom out at `0.007261552`,
    which is the value at the initial combination `[l = 100, d = 10, d′ = 5, λ = 0.001, ϵ = 50]`, and that
    combination is then reported as the tuned setting [T].
324. An error metric can be measured on one asset and transferred by belief: 2204883 tunes on gold `since we believe
    that both prediction of gold price and bitcoin price reach the best result under the same parameter
    combination`, with no bitcoin column anywhere [T].
325. A risk term built from signed changes makes liquidation risk-reducing: 2204883's (10) is
    `R = (x′_g − x_g)S_g + (x′_b − x_b)S_b`, and in behaviour iv (`Δx_g ≤ 0, Δx_b ≤ 0`) both coefficients are
    negative, so `min R` pushes holdings to their constraint limits [R].
326. A risk measure can multiply a price SD by a dollar change: `S_g` in 2204883 is the standard deviation of the
    gold price level over ten days and (10) multiplies it by `x′_g − x_g`, so the product is not a risk and the
    portfolio's size never enters [R].
327. A return can be defined on trades rather than on holdings: 2204883's (11) multiplies the predicted growth rate
    by `x′_g − x_g`, so a position held unchanged contributes nothing and `max P` cannot tell holding from
    selling and re-buying [R].
328. A two-objective programme can be decided on one number: 2204883's guard (13) compares projected portfolio
    values only, so the risk objective is dropped at the last step before the decision [R].
329. A case range can repeat its own endpoint: `model i-iv` for gold trading days and `model v-iv` for the others,
    where the second range must be v-vi [R].
330. A case's defining condition can be missing from its own constraint block: 2204883's behaviours v and vi state
    `Δx_g = 0, Δx_b > 0` and their `s.t.` rows carry only the bitcoin bounds [R].
331. A display can be orphaned across a page break: 2204883's `and can be also written as` ends PDF 11 and
    `min −P, R` opens PDF 12 directly under the header rule with no sentence above it [R].
332. A case-split template can be repeated verbatim and never summarised: `According to equation (10), (11) and
    (12), the MLP model for this trading behavior can be built as:` six times over, with no table comparing the
    six programmes and no statement of which case binds which constraint [R].
333. An acronym can name the wrong method: `MLP(Multi-objective Linear Programming)` for a method abbreviated MOLP
    everywhere else, in a paper whose companion model is a neural network [R].
334. A section can announce a definition and then restate it: 2204883's block 122 ends with `4.3.1 The MLP Model`
    and block 123 defines the acronym again [R].
335. A budget constraint can exclude its own boundary: 2204883's `Δx_g + Δx_b < x_c` and the `<` in (13) make a
    portfolio that exactly spends its cash, or exactly ties after commission, unrepresentable - and a tie flips to
    the branch that pays the 1%/2% fee [R].
336. A chapter can skip another chapter's section inside its own page span: 2212336 owns blocks 53-76 and 87-95 while
    the `4.3`/`4.4` results section (blocks 77-86, 639 words, printed pp8-9) prints between its two halves under
    `results`, so the field is two islands and the id range has a ten-block hole [R].
337. One document can file its headings two ways: 2212336 has `4.1` and `5.1` as `kind: heading` while `4.2`, `4.2.1`,
    `4.3.1`, `4.3.3`, `4.4`, `5`, `5.1.1`-`5.1.3` and `5.2` are all block tails - the same class used inconsistently
    inside one chapter [T].
338. A named model can be absent from its own display: 2212336 defines `ARIMA (p, d, q)` with `d` as `the number of
    differences when the time series is stationary` and prints (2) with no difference operator at all, so the display
    is ARMA and `d` never enters [R].
339. A combination can exist only as arrows: 2212336 never writes ARIMA+LSTM as an equation, (1) leaves `f` undefined,
    and the union lives in Figure 2's six boxes plus a five-step sentence owned by another chapter [R].
340. One quantity can carry two cases: 2212336's Table 1 defines `Y_T` / `Ŷ_T` in capitals, (2) writes `y_t`, and the
    gloss calls `y_t` the current value - a third statement, with `y_t` absent from the table [T].
341. A diagnostic can be glossed as a parameter: 2212336's `γ_i` is called `the autocorrelation coefficient` while in
    (2) it multiplies `y_{t−i}`, so the gloss names what picks `p` and `q` rather than the coefficient itself [R].
342. A model section can declare dynamic programming and contain none: 2212336's `5.1.1`-`5.1.3` hold no state
    variable, no decision variable, no transition, no value function and no equation across three subsections [R].
343. A state can be written three ways in one subsection: `[C, G, B]` in the text, `a:=1000, b=0, c=0` in the chart and
    `KEEP[a,b,c]` as the stored state, with no statement that `a` is `C` [R].
344. A decision rule can rest on an undefined index: `ROA` drives both diamonds of 2212336's Figure 11 and appears in
    no formula, no notation table and no earlier sentence [R].
345. A flow chart can subtract a cost no section has introduced: `BTC ROA= BTC expected rate of return-cost` on
    2212336's printed p10, while transaction costs are handled in a later section [R].
346. A trading chart can contain no sell branch: 2212336's actions are `Buy BTC`, `Buy GOLD` and `KEEP[a,b,c]`, so over
    1,255 stages the strategy can add to a position and never exit one [R].
347. A horizon can silently pick one calendar: `IF DAY<=1255` is five years of 251 gold trading days, while the period
    9/10/16-9/10/21 is 1,826 days for bitcoin, leaving 571 days (31%) unaccounted and unmentioned [R].
348. One exhibit can be named three ways with two spellings of the method: 2212336 prints `5.1.3 Dynamic Planning Flow
    Chart` as the heading, `Dynamic planning flow chart is as below:` as the pointer and `Figure 11: Dynamic
    Programming Flow Chart` as the caption [R].
349. An equation can exist only as pixels: 2212336's four LSTM gate formulas (`f_t`, `C_t`, `o_t`, `h_t`) are drawn
    inside figure panels and never numbered, so the text layer yields two numbered displays for the whole chapter
    while the model's own equations cannot be transcribed [R].
350. A table number can be reused inside one window: `Table 1: Notations used in this paper` on p5 and `Table 1: Model
    performance evaluation table` on p9 of 2212336 [R].
351. A step's caption can be captured by the next chapter: 2212336's `Figure 7: Step 3 of LSTM 4.3 Volatile Asset
    Prediction Results` is one block, so the chapter's own third step is filed under `results` [R].
352. A notation table can define a later section's symbols first: three of 2212336's twelve rows (`CF_real`,
    `CF_nominal`, `r_f`) serve the DP results section, and none serves the DP formulation in the chapter [T].
353. A pointer can name the wrong asset: 2212336 writes `furcating asset price` in the Figure 3 pointer and
    `The model of stock price prediction` in the chart's terminal box, for a paper whose assets are bitcoin and gold
    [R].

354. A chapter's opening headings can be welded onto another chapter's figure caption: 2218743's block 60 is
    `Figure 4: Line graphs ... {bt} and {gt}. 4 Establishment andApplication of Investment Strategy Model 4.1
    Predicting Asset Prices`, so the chapter title and its first section title sit inside a caption [R].
355. A chapter can nest four levels deep and hold zero `heading` blocks: all 76 of 2218743's blocks are `body` or
    `display`, and every numbered title survives only as a body-block tail [T].
356. One chapter can store a numbered title four ways - number+title at a tail, number at a tail with the title as
    the next whole block, number+title welded onto a caption, and title merged into its own first sentence - with no
    rule distinguishing them (2218743) [T].
357. A section number can survive only as the last token of a 160-word paragraph: 2218743's block 85 ends `4.2.1` and
    block 86 is nothing but `Moving Average Long Arrangement Method` [R].
358. A figure's panel labels can arrive inside the preceding paragraph, one block before its caption: 2218743's block
    66 ends `(a) Gold price sequence {gt}. (b) Bitcoin price sequence {bt}.` and block 67 is the Figure 5 caption
    [R].
359. A figure can open its page with no lead-in and be discussed only after its caption: 2218743's Figure 12 [R].
360. A second objective can be announced and left without a display: 2218743 label `2. The second objective function:
    Minimum of investment risk (CVaR):` at 110, formula first appearing at 121, after the whole covariance machinery
    and after the `3. Constraint functions:` bullet has been welded to that paragraph's tail [R].
361. A case-split brace can invert the sentence above it and be a tautology: 2218743 writes `y_t = y_t` for `M_t = 1`
    where the prose says trade, and `y_t = y_t` cannot express any trade [R].
362. A state indicator can be introduced, defined piecewise and then used in no equation: 2218743's `M_t`, `N_t`
    appear in the brace and one decision sentence, never in `eI_t`, the constraints or either CVaR form [T].
363. One trade can be priced at two different prices: 2218743's `eI_t` uses `(G_t − g_{t−1})y_t` (yesterday's actual
    price on today's holding) while the cash row charges `−(y_t − y_{t−1})G_t` (the predicted price) [T].
364. Two risk matrices can be on two scales: 2218743's `σ²_{i,t}` is averaged over `t−2` returns and `σ²⁻_{i,t}` is a
    single squared deviation, and the `σ²⁻` covariance entry divides by `σ²_{i,t}σ²_{j,t}` [T].
365. A differencing parameter can be defined and then hard-wired as one printed line: 2218743 defines `d` as the
    number of differences and prints `r_t = r_t − r_{t−1}` followed by an ARMA on `r_t`, with no `d` in the formula
    [R].
366. A pass rule, the reading of its figure and its own verdict can disagree inside three sentences: 2218743 rules
    `p > 0.05`, accepts "greater than 0.01 and most ... greater than 0.05", and concludes "all of which pass" [R].
367. A criterion can be relaxed to a named subset without saying which members: 2218743 relaxes "the slopes of the 10
    moving averages are all positive" to "when the slopes of the 8 moving averages are positive", with no slope
    window and no sign threshold [T].
368. A heading can print with a digit zero and become unsearchable as typed: 2218743's `Establishment of Optimization
    0bjective Functions and Constraints` [R].
369. One chapter can announce two different indicator sets for the same construct: 2218743 walks `MA5, MA10, MA60,
    etc.` in the principle paragraph and then models ten periods `5th, 7th, 10th, 13th, 16th, 20th, 25th, 30th,
    60th, 120th` [R].
370. A chapter can close on its own section heading with all of that section's evidence filed under the next chapter:
    2218743 creates `4.4.4 Results Analysis` at block 136 while the Figure 13 pointer, reading and caption are
    blocks 137-139 under `results` - the mirror of class 319's queue-64 case [R].
371. Anti-defect, filed so it is not mis-scored: a dropped bar or overbar in extraction can make a display look
    self-referential. 2218743's block 68 reads `Let gt = gt −gt−1` while the raster prints `Let ḡ_t = g_t − g_{t−1}`,
    so the neighbouring `r_t = r_t − r_{t−1}` is not evidence of a self-defining equation [E].

372. A chapter title can survive the extraction as three letters: 2218931's block 106, the notation table's last row,
    ends `... threshold for gold or bitcoin 4 Qua`, while the page prints `4 Quantitative Trading Decision Model`
    below the table's closing rule [R].
373. A chapter can store all 113 of its blocks as `body` - no heading kind, no display kind - while printing seven
    numbered equations, two ruled algorithms and five figures, and while setting its three heading levels at 17.2,
    14.4 and 12 pt (body size) [T].
374. A notation table cell can be a dangling clause on the page: 2218931's row for `f` reads `An assumed functional
    relation which maps a parameter vector` and stops, with no continuation line [R].
375. A hidden-layer equation can omit its input: 2218931 prints `H_j = f(Σ_{i=1}^{n} W_ij + a_j)` with no `x_i`, and
    then multiplies by `x_i` four equations later [R].
376. A summation can carry the wrong index and the wrong limit: `O_k = Σ_{i=1}^{n} W_jk H_j + b_k` sums over the input
    count `n` a term indexed only by the hidden node `j` [R].
377. An output layer can drop the activation that the next equation differentiates: 2218931's (2) has no `f`, and
    (4)'s `(1 − H_j)` presumes a sigmoid the text never names [T].
378. One letter can carry two quantities a page apart: `n` is the input count in (1)-(4)'s limits and "the value of n
    that makes the model prediction effect optimal" (the hidden width) in step 1 [R].
379. A formula can be written as a word fraction, and its denominator can contradict the horizons stated elsewhere:
    2218931's (7) is `expected rate of return` over `std of gold or bitcoin over the past seven days`, while gold's
    horizon is five days in the text and in `std(gold value for the last 5 days)` in the algorithm [R].
380. One statistic can serve as threshold, weight and share: 2218931's Sharpe ratio is compared against a hard `1`,
    normalized into purchase ratios `p`, and multiplied by cash as `0.99 ∗ Sharpe Ratio ∗ C_{t−1}`, with no risk-free
    rate anywhere in the chapter [T].
381. A portfolio slot can be redefined four lines after it is introduced, and dollar amounts added to holdings: `C` is
    cash in `[C, G, B]` and then "the amount of gold or bitcoin that can be bought today with cash held yesterday",
    and the state after a purchase is `[0, 0.99p_1 ∗ C_{t−1} + G_{t−1}, ...]` [R].
382. Constants can print on every purchase with no gloss: 2218931's `0.99` and `0.98` never receive a sentence, and no
    transaction-cost rate is stated in the model [R].
383. A rule can flip both its connective and its inequality between prose and code: 2218931's text buys on "greater
    than 2% or ... greater than 3%"; its Algorithm 2 tests `short-term uptrend ≥ 0.02 and long-term uptrend ≥ 0.03`
    [R].
384. An algorithm can buy on the same signal its own chapter sells on: 2218931's line 15 is `if predicted gold is down
    or predicted BTC is down then` / `Buy gold, BTC;` against the selling stage's "Sell it when we predict a fall"
    [R].
385. Pseudocode can reference names the chapter never defines: 2218931's `Income`, the function `normalization` and
    `T_total`, plus `Sell gold, BTC at the Sharpe ratio` with no quantity and no line for the holding stage [R].
386. A symbol can hold two meanings in one chapter, and a definition can contradict its own code: 2218931's `ν` is
    the damping scale (`ν:=2`, `ν := 2 ∗ν`, reset in the accept branch) and also "the error vector"; `ε` is
    `x − x_new` and also the tolerances `ε₁`, `ε₂`; `A` is called "Hessian matrix" though line 3 sets
    `A := J(x)ᵀJ(x)`; `τ`, `k_max`, `F`, `L`, `ϱ`, `h_{1m}` and `x₀` are never glossed [R].
387. A subsection can decline to explain its own algorithm and substitute a borrowed listing: 2218931 writes "we will
    not introduce too much mathematical knowledge involved in the algorithm", then 21 lines from K. Madsen et al.
    (2004), and runs the network through MATLAB's `Trainlm` [R].
388. A time series can be validated by a random split: "the sample data is randomly divided for training, and the
    ratio of training, testing, and validation data is 70:15:15" on daily prices, while the decision model re-forecasts
    every day [T].
389. A flow chart and the numbered procedure it illustrates can share three of seven step names, with no numeral
    linking a box to a step: 2218931's chart has `Parameter Initialization`, `Enter a random sample`, `Error
    Calculation`, `Error back propagation`, `Update network parameters` and a stop diamond; the text has a structure
    step, a threshold update and no sampling step [R].
390. A figure caption can be captured by the previous page's paragraph: 2218931's `Figure 7: "Stand by" stage` prints
    under the p14 diagram but is stored as the closing words of the p13 paragraph about the Sharpe ratio [R].
391. A block spanning a page break can carry the next page's headings inside a caption: block 167 is `Figure 6:
    Predicted price and actual price comparison chart 4.2 Recurrent Decision Model 4.2.1 Model Description`, spanning
    pp12-13 [R].
392. Panel labels can be attached to the previous figure's caption: 2218931's Figure 5 block carries `(a) gold (b)
    bitcoin`, which belong to Figure 6 - verified on the raster, where Figure 5 has four `Training/Validation/Test/All`
    panels and no `(a)/(b)` [R].
393. A stage list can be announced as four stages, printed as starred run-ins welded to the ends of the preceding
    paragraphs, and then have one stage dismissed: 2218931's selling stage is "The changes in its investment
    portfolio are similar to the buying stage, so we will not go into details here" [R].
394. An exhibit can make its own claim unfalsifiable, and a state vector can mix units while citing the problem
    statement: 2218931's Figure 6 draws each series in one colour per panel, so "almost wholly overlap" cannot be
    checked, and `[C, G, B]` starts at `[1000, 0, 0]` "from the meaning of the question" [T].


    gives bitcoin `DMA, RSI, MACD, TRIX, WR` and gold `... BOLL`, while Figure 9's `Voters` box prints `Gold` over the
    WR list and `Bitcoin` over the BOLL list, so the one difference between the two systems lands on the wrong asset
    [R].
396. An "optimized" algorithm can be algebraically identical to the one it replaces: 2224507's
    `DMA(n₁,n₂,t)∗ = (Σ_{i=0}^{n₁−2} w_{t−i} + w′_{t+1}) − (Σ_{i=0}^{n₂−2} w_{t−i} + w′_{t+1})` adds the forecast to
    both sums with the same sign, so `w′_{t+1}` cancels and the "optimized" factor is the original with both windows
    one term shorter [R].
397. A table titled "after parameter optimization" can print no parameter and no optimization: 2224507's Table 3 has
    two rows, `DMA` and `WR`, and its cells hold the forecast-substituted formulas with every `n₁`, `n₂`, `n`, `k`
    still symbolic [R].
398. A factor can be reported with another factor's parameter names: 2224507's KDJ row prints `n = 2, I = 48, O = 65`,
    the RSI triple, for a factor that has no formula, no section and no gloss anywhere in the paper [R].
399. A model can report results for factors it never modelled: 2224507's §4.3 states that "the RSI and MACD factors are
    used as separate decision factors ... which are modeled for parameter optimization", and Table 2 then reports
    optimal parameters and five-year totals for seven factors [T].
400. A position model can minimise risk with no return term, so its optimum is to hold nothing: 2224507's
    `(20)` is `Min σ_t = √[(σ_t)²]` subject to `0 ≤ H^btc + H^gd ≤ 1` and `H ≥ 0`, in a subsection whose prose says
    the aim is "to maximize the return" [R].
401. A gloss can name a symbol the display does not contain, and then drop the other asset: 2224507's `(24)` is
    `(x_t − x_i)/x_i ∗ 100% < −20%` per asset, and the gloss reads "`x_t^btc x` is the current day's trading price and
    `x_i^btc y` is the previous day's trading price", inventing an upright `x` and `y` and never glossing `gd` [R].
402. A restatement can swap two indicator variables between the model and the gloss: 2224507's `(8)` has
    `C_{k+1} = C_k + (1−α)x_{k+1}B_{k+1}p_{k+1} − C_k q_{k+1}` and `(10)` has `... q_{k+1} − C_k p_{k+1}`, with the
    prose sentence matching `(10)` and not `(8)` [R].
403. A cash balance can be updated with both branches inverted: 2224507's `(8)` adds cash when the buy indicator fires
    and subtracts all cash when the sell indicator fires [T].
404. A dispersion can be printed as a product: 2224507's `MD_t = √(Σ_{i=0}^{n} (w_i MA_t) ∗ (w_i − MA_t) / n)` loses
    the minus sign in one factor and turns the square into a multiplication, and `MB_t` is then set to `MA_{t−1}` [R].
405. A rescale can make its own signal rule vacuous: with `AMA = DMA/10`, 2224507's "When DMA is greater than AMA, it is
    a buy signal" is true exactly when `DMA > 0` [T].
406. An indicator's signal sentence can invert the polarity of its own formula: 2224507's `WMS` is `100` at the cycle
    high and its sentence calls that "oversold and is a buy signal", one page after RSI's sentence got its direction
    right from the same template [R].
407. A document can encode one heading in 365 blocks: 2224507's chapter has three levels of printed hierarchy and zero
    `heading` blocks, and the only `heading` kind in the whole file is the title on page 1 [L].
408. A chapter can resume inside a subsection whose headings it does not own: 2224507's first coded block on p14 is
    the body of 4.5.1, whose `4.5` and `4.5.1` headings are the tail of block 200 under `results` [T].
409. A moving average can sum one term more than it divides by: 2224507's `(1)` and `(7)` run `i = 0..n` and divide by
    `n` [R].
410. A chapter's exhibit of its own headline result can be shown but read by the next chapter: 2224507's Figure 12
    prints at the foot of p18, its caption and reading (`185.49%`, `0.51%`) are block 263 under `results`, and the
    baseline it beats appears only in Table 4 on p19 [T].
411. A figure caption can precede every pointer to it: 2224507's Figure 10 prints under the `4.5.3` heading, the caption
    under the chart, and only then the sentence that reads it [R].
412. An LSTM can be printed with the wrong gate activation letter and two states under one symbol: 2224507's
    `(21)`-`(23)` use `μ(...)`, print `tan y(` for the hyperbolic tangent, name the candidate `A′_t` and the cell state
    `A_t`, write the forget factor as a bare `F`, and cite nothing [R].


413. A buy rule can issue a sell signal on its own complement, overriding the chapter's own selling rule: 2229059's 3.1
    ends "If both G_t(n) > 1 and P_t - A_t(n) > 1 then M_t(n) > 1 and a buy signal is issued ... Otherwise, a sell signal
    is issued", while 3.4 sells only "If S > 0", a profit test net of fees, and 3.8's procedure routes every sell through
    `S` and never through the momentum condition [T].
414. A two-case brace can be defined by disjunction and then required to be true in both cases: 2229059's
    `M_t(n) = { G_t(n) (gradient) ; P_t - A_t(n) (difference between price and moving average) }` is followed by "Both
    cases must be true for M_t(n) to return a buy signal" [R].
415. A formula's divisor can be the summation index: 2229059's `S = (1 - f_a)·P - Σ_{i=0}^{n}(1 - f_{ai})C_i / i - L`
    divides the summed cost basis by `i`, so the "average cost" is an average of the `C_i / i` [R].
416. A gloss can restate a display with every symbol changed and the divisor corrected: 2229059's display has
    `f_a, f_{ai}, C_i, /i` and its gloss prints `f_g, f_{gn}, C_n, /n`, so the two forms disagree on every term and
    neither is identified as the correction [R].
417. A profit indicator can subtract the margin it is then compared against: 2229059's `S` already contains `- L` and
    the rule is `S > 0`, so the test is on profit net of a margin rather than on profit [T].
418. An "average over the history" can sum over the window length instead of over time: 2229059's
    `E = G_t(n) - C·(Σ_{i=0}^{n} G_t(i))/n` passes the dummy index as `G_t`'s window argument, so the history of the
    model is n+1 window lengths from 0 to n and the 1,826-day series never enters [R].
419. A threshold can be printed as a number in prose and as an unglossed symbol in the display, then reused with another
    meaning: 2229059 prints "the gradient being over 5 times the average gradient ... over the history of the model",
    the display carries `C` glossed only as "a scaling factor", and 3.9 reuses `C` as "a scalar constant" in
    `W = C·1/t^2` with no statement that they are the same constant [R].
420. A cross-asset weight can contain no asset index: 2229059's `W = C·1/t^2` weights gold and bitcoin identically, and
    the sentence it is introduced to support is "When comparing the profitability between gold and bitcoin, the bitcoin
    markers are considered much more heavily than the gold markers" [R].
421. A weight whose variable has no origin and no cap cannot change any comparison: with 2229059's `W`, `t` is undefined
    and unbounded, so the factor decays without bound and rescales every signal identically [T].
422. A reversion criterion can be an inequality true of every non-negative function: 2229059's
    `∫_{μ-i}^{μ+i} P(x)dx > ∫_{μ-j}^{μ+j} P(x)dx for i > j > 0` says nothing about where the price is relative to the
    mean, and defines neither the integrand nor `μ`, which appears for the first time inside the limits [R].
423. A threshold in a price-difference test can be unitless and unscaled: 2229059's two conditions are `G_t(n) > 1` and
    `P_t - A_t(n) > 1`, so the filter is one dollar - 1/1800 of gold's level and 1/10000 of bitcoin's [T].
424. A flow chart can draw a different rule from the text it illustrates, with no `read-figure` unit to catch it:
    2229059's Figure 3 buys unconditionally below the moving average and asks about the slope only above it, while 3.1
    requires `G_t(n) > 1` and `P_t - A_t(n) > 1` conjunctively, and the chapter allocates Figure 3 no job at all [R].
425. A chapter can support a cross-asset claim with the single-asset figure: 2229059's 3.9 writes "As shown in figure 2,
    the assets can differ in the magnitude of movement", and Figure 2's caption is `Bitcoin Price from 9/11/2016 to
    9/10/2021`; the two-asset chart is Figure 1 under the `problem-analysis` chapter [T].
426. A procedure can lack the branch for the test it performs first: 2229059's 3.8 opens "first check for 'no-buy' and
    extreme market conditions. If no-active, then the model immediately moves to the sell indicators" and never says
    where the no-buy case goes, while its extreme branch skips the rest of the program, so 3.5's release condition
    ("until the price has regressed to a percentage of its maximum value ... or a price ΔP below") is reached by no line
    [T].
427. Risk control can be named entirely in unvalued parameters: 2229059 names `z` days, "a number of days", "a
    percentage of its maximum value" and `ΔP`, and gives a value to none of them [T].
428. A 21-page document can encode zero `heading` blocks: 2229059 prints nine numbered subsections and a chapter
    hierarchy on every page, and all 147 blocks are `body` (140) or `display` (7), the seven displays being captions
    [L].
429. A heading can print its number after its title: 2229059 prints `Daily Buy/Sell Order 3.8` where the other eight
    subsections print `3.N Title` [R].
430. A chapter's last block can carry the next chapter across a page break: 2229059's block 57 spans pp11-12 and ends
    `4 The Model Results 4.1 General Result Figure 4: Our results.` [L].


431. Two chapters can interleave block by block across one page range: 2300348's `model-establishment` (61 blocks, nine
    islands) and `results` (30 blocks) alternate from printed p8 to p18, so the model chapter's readings of its own
    exhibits are all coded as the results chapter's units [L].
432. A model chapter can name sixteen exhibits and allocate no reading job: 2300348 has 41 units - 16 `define`, 9
    `source`, 6 `compute`, 5 `route`, 4 `derive`, 1 `interpret` - and zero `read-figure`, zero `compare` [T].
433. A chapter's subsection headings can be stored inside another chapter's blocks: 2300348's `5.3`/`5.3.1` sit in
    `results` block 90, `5.3.2` in 95, `6.3` in 115 and `7.4` in 139, and `6.2` is `results`' standalone block 109 [L].
434. A chapter's own conclusion can print after its last coded block: 2300348's §7 ends at Table 11's body inside block
    138, and the `7.4 Accuracy Discussion` heading with the `28 out of 30` / `93.33%` paragraph are blocks 139-140 under
    `results` as `compare` [T].
435. A `Sum` row can carry cells from another table: 2300348's Table 11 prints `Sum 6.51769% 23.30265% 30.29725%`, three
    values lifted from Table 10 on the previous page, under columns that already sum to 360 and 100.0 [R].
436. A count column and its percentage column can disagree row by row while both totals look right: 2300348's Table 11
    prints 36.2/42.4/19.1/2/0.3 for 131/152/69/7/1 of 360, i.e. 36.39/42.22/19.17/1.94/0.28 [R].
437. A duplicated table column can be given a second name: 2300348's Table 11 prints `Valuable Percentage` identical to
    `Percentage` in all five rows [R].
438. One coefficient can be printed twice with two values: 2300348's prose says "the Spearman correlation coefficient is
    -0.2956" and Table 5's word-frequency row prints `-0.3256` [R].
439. A forecast interval can use a different error from the one just selected: 2300348 selects "the relative error rate
    of 2.1569% as the error interval" and prints `x_March1,2023 = 20367 ± 2.01569%` [T].
440. A normalisation can be applied to the weights instead of the data: 2300348's `(8)` prints `δ = σω1 ∗ Σ i ∗p_i +
    σω2 ∗p_X`, while its sentence says "we use the Sigmoid function to normalize these two data" [R].
441. One Greek letter can carry three definitions in one paper: 2300348's Table 2 prints `σ` as "the difficulty rate",
    Table 3 prints `σ` as "the sigmoid function", §7 uses `δ` for the difficulty rate, and `δ` never enters Table 2
    [R].
442. A defined index can be unreproducible from the paper's own inputs: 2300348's `(8)` with `ω1 = ω2 = 0.5` and
    EERIE's Table 10 distribution gives `0.5·σ(4.0054) + 0.5·σ(2.40859) = 0.9498`, not the reported `0.35916` [T].
443. A summation can have no index: 2300348's `(4)` prints `fLetter = Σ_{1}^{5} f_{a,b,c...}` - a bare lower limit, no
    index variable, and a summand subscripted with a truncated letter list [R].
444. A model can be defined as an arrow between two tuples: 2300348's `(5)` is
    `(fword, fletter, rep) −GSRF→ (1, 2, 3, 4, 5, 6, X)`, with nothing estimable written on the arrow and the grid
    search appearing only as Table 9's five cells [R].
445. A clustering section can print a distance and a residual and no objective: 2300348's `(9)` and `(10)` state no
    minimisation, and the centroid update and the convergence test exist only as prose sentences [R].
446. A table can be printed with no column headers: 2300348's Table 10 is seven bare numerals `1`…`X` and carries its
    `MSE:`/`MAE:` in 6-point type inside the table frame, off the seven-column grid [R].
447. A column header can contradict the paragraph above it: 2300348's Table 8 heads the third attribute `ref` while the
    prose uses `rep` five times in the same page and sets `rep = 1.5` [R].
448. Section references can be systematically one section off: 2300348 attributes the `score` work printed in §5.1 to
    "Section 4" in three separate blocks (101, 110, 126) [T].
449. A table and a figure can share one caption: 2300348's Table 6 and Table 7 print the same `Boxplot analysis between
    ... score` captions as Figures 7 and 8, over tables of median differences [R].
450. A difference table can print differences with no direction: 2300348's Tables 6 and 7 head their columns
    `Median difference1/2/3` and never say which group is subtracted from which [R].
451. A word under test can be spelled two ways on one page: 2300348's `7.3` heading prints `EERIE` and the sentence
    four lines below prints `"ERRIE"` [R].
452. A caption can be stored inside the block it captions, at the chapter's end: 2300348's block 138 carries the
    clustering run, the `(a)`/`(b)` labels, `Figure 10: Difficulty rate classification` and Table 11's body, while
    Table 11's caption is block 139 [L].

453. A chapter's own title block can print a page before the page range the record gives it: 2301192's block 55, the
    `3` heading, prints on printed p5 under the notation table while the record says `pages [6, 15]` [L].
454. Section headings can be stored in the tail of another chapter's paragraph: 2301192's `3.2 Prophet Model` is the
    tail of a `data-preprocessing` block (68), `3.3` the tail of a `results` block (84), and `4.4` and `5` the tails of
    `results` blocks 154 and 155, so nine of the chapter's thirteen printed headings are inside other chapters [L].
455. A page's running head can be welded onto the last line of the block that crosses the page break: 23 of 2301192's
    236 blocks end in `Page N`, seven of them in the model chapter (70, 76, 100, 120, 136, 147, 157), which inflates
    every word count that trusts the stored text by two words per break [L].
456. A one-line section title can be split into two heading blocks at the printed hyphen: 2301192's block 144 ends
    `... based on BP Neu-` and block 145 opens `ral Network`, so `4` occupies two blocks and `4.1` arrives as a third
    heading [L].
457. A metrics table can be computed on a different scale from the series the model was fit to: 2301192 fits the log
    transform (Figure 5 spans 9.5-12.8) and Table 4 reports `MSE 60340502`, `RMSE 7767.9149`, which the prose calls
    `the small RMSE and MSE` [R].
458. A point forecast can sit off the centre of its own prediction interval: 2301192 prints `14534` inside
    `(13175, 16128)`, whose midpoint is 14,651.5, with no statement that the interval is asymmetric [R].
459. A metrics table and the paragraph reading it can disagree by 24%: 2301192's Table 6 prints `MAE 3.2302` and the
    paragraph says the MAE `is 4`, while glossing `MAPE 32.9194` as `a high accuracy of the model` [R].
460. A test's verdict can be printed outside the chapter that runs the test: 2301192's F test is stated in §3.5.2 and
    its only verdict sentence (`F = 1.058`, `P = 0.379`) is `results` blocks 140-143, so the chapter's own argument
    stops one sentence short of its conclusion [T].
461. A hypothesis test can be run and then ignored by the rest of the paper: 2301192 concludes that word attributes
    have no significant impact on the hard-mode proportion, and §5.1 then classifies difficulty from the try
    distribution alone while §5.2 returns to the attributes, with no sentence recording the contradiction [T].
462. Two exhibits under one identical caption can print two different distributions: 2301192's `Table 7` cells
    0/6/18/29/27/15/5 sum to 100 and its `Figure 10` pie labels 23/32/22/6/4/12 sum to 99, both captioned
    `Predicted Result of "EERIE"`, and neither is named by the prose [R].
463. An attribute can be listed as a regressor and never defined: 2301192's `5. the Sum of a Letter in a Word` gets one
    sentence with no formula and no data source, and `6. Part-of-Speech of a Word` gets three words and no content,
    and both appear in equation `(8)` [T].
464. Assumption enumerators can reuse the display-equation glyphs: 2301192 prints `(1) (2) (3)` on p10 for its three
    player groups in a paper whose displays `(1) (2) (3)` already occupy pp7-8 [R].
465. A regression equation can be sent to an appendix while the section that needs it prints only the generic form:
    2301192's §3.5.1 prints `ŷ = β0 + β1x1 + ... + βmxm + ε` and says `Due to the length of the obtained regression
    equation, it is included in Appendix A`, where it prints as display `(12)` with standard errors and no F, no p
    and no n [T].
466. A holiday model can declare five holidays, plot three dips and read one: 2301192's Table 3 lists Valentine,
    Easter, Halloween, Thanksgiving and Christmas, Figure 6's holiday panel shows three visible dips, and the
    paragraph names only Valentine's Day [R].
467. A holiday date can be taken from the wrong calendar: 2301192's Table 3 prints `Easter 2022/04/24`, the Orthodox
    date, for an English-language Wordle corpus whose Western Easter in 2022 was 2022/04/17 [R].
468. A four-metric display can put four equations under one number: 2301192's `(5)` prints `MSE`, `RMSE`, `R²` and
    `MAPE` under a single right-aligned tag, and the printed `MAPE` line carries a stray `c` after `100%` [R].
469. Training and test ranges can share their boundary date: 2301192 splits `2022-01-07 to 2022-11-21` for training
    and `2022-11-21 to 2022-12-31` for test, so one day is in both [R].

470. A chapter boundary can run through a section's own subsections: 2307166's printed `4.2.1 Terminology` and `4.2.2 Assumptions`
    are coded under `notation` and `assumptions`, so `model-establishment` loses its own glossary and all four of its
    assumptions while the printed numbering keeps them inside chapter 4 [L].
471. A bootstrap table can put a point estimate where the reader expects a third quantile: 2307166 prints `Mean 2.5% 97.5%`
    over `14689.9 11173.04 17069.15`, so three columns hold one estimate and two bounds [R].
472. A fit can print its optimiser's starting guess and never its answer: 2307166 prints the genetic algorithm's
    `1.77e-01 1.77e-02 1.04e-03 1.14e-03`, and the Nelder-Mead values that minimise the MSE appear nowhere, with no
    goodness of fit given [R].
473. A word-level sum can nest one sum inside another and re-index without redeclaring: 2307166's `w_i = Σ_{j=1}^{n} Pur(c_{i,j})`
    sums over `j` a quantity already summed over `j`, and moves `c_i` to `c_{i,j}` between two adjacent displays [R].
474. A sentence can be severed by a figure-only page: 2307166's block 137 ends `so we need to conduct` on p17, p18 prints
    ten non-whitespace tokens (two captions) and nothing else, and block 138 resumes on p19 `further in these five
    variables filtering.` [R].
475. A tuning claim can contradict its own plot: 2307166 says `performs best at K=15` and the six curves fall to a floor
    near 12.4 that keeps drifting down to K=50, so the plotted argmin is at the right edge of the axis [R].
476. A figure legend can be code identifiers the footnote only half-decodes: 2307166's `Both!Hard` / `UnW&Hard` / `W&Hard`
    entries are glossed for `&`, `!`, `UnW` and `W` but never for `Both` or `Hard`, and the note opens `*:` with no
    asterisk anywhere on the caption or the figure [R].
477. A significance-star column can contradict its own p-value: 2307166's Table 7 prints `***` beside `Pr(>|t|) 0.869` [R].
478. A regression coefficient can be restated an order of magnitude small: 2307166's prose reads `-0.01` where its Table 6
    prints `-0.148223`, and the same sentence gives that fit's R² as 0.013, `about 2%` and `about 1.2%` [R].
479. A standardisation formula can print a stray prime and an unmatched index: 2307166's `x*_ij = (x_ij − x̄)/sd(X_j)′`
    indexes the denominator by `j` while the numerator's mean carries no `j`, and a prime sits between bracket and comma [R].
480. A record note can inherit the paper's own miscount: 2307166's note says group 6 `carries the four differential
    equations` while the page prints three SIR equations and the four PCQL ones are in group 7 [L].
481. A chapter's text can print two leaves past the record's page range while the range itself contains a leaf the chapter
    does not use: 2307166's `pages [7, 17]` omits blocks 138-142 on p19 and includes p15, whose eight blocks are all
    `results` [L].

482. One object can carry two captions under two numbers, the second restarting the figure count: 2307946 prints
    `Figure 1: (a) Shared-Bottom model. (b) One-gate MoE model. (c) Multi-gate MoE model.` directly above
    `Figure 13: MMoE's Advantage Shown by Comparison` over the same graphic, and the foreign caption has no layout
    block at all, so the record cannot contain it [R].
483. A chapter can end on the colon that introduces its own evaluation table when that table is coded to another
    chapter: 2307946's §6.3 stops at `the calculation results of each indicator within the training set and
    validation set are as follows:` and Table 4 is a `results` block, so the model is designed in one chapter and
    scored in another [L].
484. A table footnote can be duplicated verbatim under two different columns: 2307946 prints
    `2 This statistic excludes homophones` under `Phono_N` and `3 This statistic excludes homophones` under
    `OG_N`, qualifying two quantities with one sentence that says which rule applies to neither [R].
485. A numbered display can be a bare variable list: 2307946's `(3)` prints `pctt−1, pctt−2, · · · , pctt−5;
    Xt, Xt−1, · · · , Xt−5 (3)` with no left-hand side, no operator and no equals sign, and the prose afterwards
    calls it "the feature sequence", so an equation number is spent on a list of names [R].
486. A figure can be described with colours it does not use: 2307946 says `the white and black dots represent the
    leaves with the maximum and non-maximum split gains` over a diagram of dark grey and light green nodes with
    pale blue arrows and no white dots [R].
487. The split ratio and the results table can use different partition names: one block declares
    `the ratio of training set : test set = 4 : 1`, Table 4 reports `Training set` and `validation set`, so a
    declared test set is never scored and a scored validation set is never in the ratio [R].
488. Two adjacent results sentences can describe different stages with nothing marking the seam: 2307946 writes
    `the above two models were retrained. However, ... did not improve significantly` and, four blocks later,
    `Luckily, the results have been significantly improved.` - post-CTGAN versus post-OpenFE, unstated [L].
489. An adjective can contradict the number in its own clause: `The resulting significant test statistic is
    -1.9608 while the p-value is 0.5934, which cannot reject the null hypothesis` [R].
490. A section's body can sit in the coded chapter while its own headings sit in another: 2307946's §7.3 and
    §7.3.1 are body blocks 143-147 inside `model-establishment`, but both headings print on `results` block 142,
    the inverse of the usual whole-section hand-off [L].
491. A declared page range can be right at both ends and wrong in the middle: 2307946's `pages [5, 21]` starts and
    ends on the right leaves, yet p7 (Figure 4, Table 2) and p15 (Figure 10, Figure 11) hold nothing of the
    chapter's [L].

492. A results table can be read under a metric name its own column header does not use: 2309397 says `The ROC of
    words in difficulty level IIIII is 0.5941, the highest` over a Table 8 column headed `RDC`, and `ROC` is defined
    nowhere in the paper [R].
493. A figure can be captioned and never cited: in 2309397 the string `Figure 11` occurs in exactly one block in the
    whole document - its own caption - so the only exhibit showing the percentage distribution the next section
    models is never referred to [L].
494. A word count can print two ways with the prose on one side and every number on the other: 2309397's prose says
    `356` four times while Figure 9's caption, equation (3)'s index, Figure 10's ring counts and all three §5.4
    summations say 357 [R].
495. A record's chapter boundary can separate a section's heading from the body that heading introduces: 2309397's
    `4.3` heading block is in the chapter while Figure 10, Table 4, the general regression equation and the fitted
    `Ŷ` it produces are `results` blocks, so the chapter resumes only at `4.4 Results Analysis` [L].
496. A layout can weld two captions into one block in reverse page order: 2309397's block 167 reads
    `Figure 16: Accuracy of the model Figure 15: six attribute values of EERIE`, so any consumer trusting block order
    reports the two figures swapped [L].
497. A coded chapter can end on a heading: 2309397's last block carries `8 Model Evaluation and Improvement` and
    `8.1 Strengths and Weaknesses` with no body under either, and §8's text prints on the next leaf under
    `strengths-limitations` [L].
498. A metric can be called a weighted average over a formula that weights nothing: 2309397's
    `MAE is the weighted average of the absolute values of the differences` against a printed `1/N Σ|y_n − ŷ_n|` [R].
499. A prose reading can invert the trend of the figure it reads: 2309397 says COV distributions are `more consistent
    across words when NF is 0.2 and above` over bands that widen monotonically with NF [R].
500. A percentage in prose can contradict the table beside it, and the table's value be the one that reconciles:
    2309397's `about 13% of the players could guess the word in 2 trys` against `11%` in Table 6, the only value that
    makes the row sum to 100 [R].
501. A coding procedure can be named after a method it does not use: 2309397's "dummy coding" prints one numeric
    column per categorical variable (`X1 = {1 noun, 2 verb, 3 adjective, 4 others}`), so a four-class nominal
    regressor is forced onto one slope and its t-test measures nothing [R].
502. One distance can print under three names and be defined under none: 2309397 writes `M' distance` on p20 and
    `Marxist distance` on p21 for the same quantity [R].
503. An EM update can be corrupt in two independent ways: 2309397's covariance line prints the subscript outside the
    summation sign (`∑，j =`) and its numerator carries `μ_i` where `μ_j` is required [R].
504. A table can announce filter thresholds its own columns never print: 2309397 states `Sup of 0.5` and
    `Lift greater than 1` and then prints only `Conf`, with ten of twelve values exactly 1 [R].
505. A symbol can be reused across sections for a different object without a note: 2309397's `Y` is the Hard Mode
    percentage in §4 and `Y = (y1,···,y7)` in §5, while `X1-X7` are word attributes and `X = (x1,···,x7)` the
    attempt-share components [R].
506. A figure's values can disagree with the cluster table the text assigns the same word to: 2309397's radar gives
    EERIE `RDC = 0.11` while Table 8's level III mean is `0.4656`, and by RDC alone level I at `0.4158` is nearer [R].
507. A regression can be declared significant at the 10% level in its own words: 2309397's
    `the P-value of the model as a whole is 0.097, which is significant at the 10% level of significance` [R].
508. Difficulty levels can print as numerals that are not Roman: `IIII` and `IIIII`, in the table and in the running
    text [R].

509. A subheading can be welded to the end of the body block that precedes it: 2310767's `4.1.2 Building Predictive
    Models`, `4.1.3 ARIMA-LSTM Model`, `4.1.4 Analysis of Results` and `4.2 Construction of Word Attributes` all print as
    the tail of a body block, so a chapter with seven numbered headings owns only two `heading` blocks [L].
510. A heading can be split across two body blocks with the number alone in the first: 2310767 stores `4.1.1` as a
    zero-word `body` block and its title `Autoregressive Integrated Moving Average Model` as the next one [L].
511. A figure can print while owning no block at all: 2310767's Figure 4 raster sits at the head of p8 and its caption
    is the tail of body block 83, whose prose ends on p7, so the chapter's headline exhibit has no `display` block and
    a consumer keyed on `kind == display` counts two figures where the page prints three [L].
512. Prose and caption can name the same exhibit as two different kinds of plot: 2310767 calls Figure 2's panels `the
    two time series` while the caption calls them `Autocorrelation plot and Partial Autocorrelation plot` [R].
513. A panel can be read before the quantity it plots is defined: 2310767's Figure 2(b) is the differenced series
    `r̄_t`, which only block 72's `Let ¯rt = rt-rt−1` introduces on the next page, and block 69 reads both panels as
    trending series with slowly decaying coefficients [R].
514. A conversion can be written with one symbol on both sides: 2310767's `converting a non-stationary series rt into a
    stationary series rt by differencing of order d` [R].
515. A math subscript can be kerned into the middle of a word: 2310767 prints `converting` as `conver` + a subscript +
    `ing`, so the word has lost a letter to a formula fragment [R].
516. A repeated variable can be duplicated in a list: 2310767's `the lagged terms of the random error terms at and at`
    [R].
517. A test verdict can print without its statistic: 2310767's Ljung-Box gate states the acceptance rule (`greater than
    0.05`) and the verdict (`it is not white noise`) and never prints `Q(m)`, `m` or a p-value, so the failure that
    licenses the whole second model cannot be re-run [R].
518. A hybrid's second stage can be motivated by contradicting the first stage's own claim: 2310767 says the ARIMA
    `prediction results ... are not very volatile` and then sells the combined output as `more volatile and more
    realistic` [R].
519. A user-chosen parameter can be reported under the name of a data quantity: 2310767's phase-space reconstruction
    prints `the optimal number of reports is finally determined as 18`, an embedding order with no search and no
    candidates [R].
520. A forecast can be dated while its axis stays an index and its interval stays unqualified: 2310767 dates the point
    `March 1, 2023`, plots it on an x-axis running 0-450 with no date ticks, and prints `[9614,43109]` with no nominal
    coverage level [R].
521. A run-in label can be printed twice: 2310767's `Vocabulary usage index` is the tail of block 87 and the opening
    words of block 88, while the other two run-ins (`Number of syllables`, `Word Class`) print once [L].
522. A plot's axes can carry the neighbouring plot's name: 2310767's Figure 2(b) Autocorrelation subplot has the x-axis
    label `Partial Autocorrelation` [R].

523. A confidence interval can print its lower bound correctly and its upper bound with the same digits transposed, in
    one sentence: 2311035 prints `[20745.72, 22914.74]` for `21, 843.73 ± 1.96 × 560.21`, whose upper bound is 22941.74
    [R].
524. A normalization decision can rest on a ratio whose denominator is never printed: 2311035 justifies skipping Min-Max
    with `the ratio of change is only 3.4%, scaled by the maximum number` while its own two numbers give 30.9%, and the
    maximum is nowhere in the chapter [R].
525. A significance verdict can use a critical value in place of the p-value the software printed on the same page, and
    then deny a coefficient that its own screenshot reports as significant: 2311035's `The F-statistics is 1.69, less
    than 2.397 (α = 0.05)` beside `Prob > F = 0.1519`, then `the conclusions are the same` although `Head` has
    `P>|t| = 0.014` [R].
526. A regression's screenshot can list the intercept as a regressor of the model it reports: 2311035's model line ends
    `+ β4 ∗ Letterf req + cons`, so the constant enters the equation twice - once as `cons`, once as `β0` [R].
527. A distribution can be credited with a property it does not have: 2311035 names `the gamma distribution, which
    includes the natural constant term` as the reason to take a logarithm [R].
528. A cross-reference can name the wrong subsection for the model it cites: 2311035 writes `The LSTM model created in
    4.2.2 was trained for 150 times` while the model is the one §4.2.3 (`Implementation of LSTM`) builds [R].
529. A bullet's attribute can be named one way in its label, another in its prose and a third in the formula that uses
    it: 2311035's `Consecutive letters` / `serial letters` / `Continuous` are the same regressor [R].
530. A table of corrections can contain a row that corrects nothing: 2311035's Table 2 row `favor (with space) → favor`
    deletes a space, and its first row's source string opens with a stray `r` (`rprobe → probe`) [R].
531. A run of sentences can be stored out of order across blocks so that one sentence's head and tail are split around
    the evidence for it: 2311035's block 92 `Therefore, words will not aﬀect the` is separated from `percentage of
    scores ... at 5% signiﬁcance level` by the F sentence that decides it [L].
532. A chapter can print its own title inside the preceding chapter's last block, so the coded span opens mid-section
    with a subheading and no chapter head: 2311035's `4 Task 1 ... 4.1 Data Cleaning` is the tail of `notation` block 57
    and its first coded block is 4.1's first sentence [L].

533. A parameter vector can elide members that the paper's own coefficient table prints in full: 2311717 glosses
    θ as `[A1, A2, A3, B1 ...C1, C2, C3]`, eight slots for nine coefficients, dropping `B2` and `B3` into the ellipsis
    while Table 2 lists them [R].
534. A prediction interval can print bounds dozens of standard deviations away from the model that generated the
    point: 2311717's `[7654, 20154]` is ±6,250 around a Poisson mean of `13,904` (σ ≈ 118), so it cannot be a quantile
    of the distribution named in the equation it is derived from [R].
535. Two confidence levels of one printed rule can produce one symmetric and one asymmetric interval: 2311717's 75%
    row is ±6,250 exactly and its 85% row has gaps of 8,470 and 9,753 [R].
536. A corrected intensity can depend on the count it is supposed to generate: 2311717 defines `λ̇k(t) = λ(t)·f(k)` with
    `k` the number of reports and then evaluates `Ṗk(t)` at `λ̇k(t)`, so the same variable sits on both sides of the
    model [R].
537. A temporal claim over a table can be contradicted by that table: 2311717 says high Hard Mode percentages appear
    `in the last three months of 2022` while its top ten holds `2022/9/16 parer 11.07%`, and says low ones are in
    `the first month of 2022` while its bottom ten runs to `2022/2/13 [R].
538. A quantity already defined as a percentage can be divided by the sample size again: 2311717 defines `p_h1` as
    `the percentage of words with the first letter "h"` and then gives the attribute as `p_h1/359` [R].
539. A caption can be torn across two blocks with the second line alone: 2311717's Figure 4 caption is block 70
    (`...the number of reports and`) plus block 71 (`the popularity of the game`) [L].
540. Two numbered headings can share one block: 2311717's `5.3 Analysis of Game Mode Selection` and
    `5.3.1 Analysis of word attributes` both close block 120 [L].
541. A paragraph can be torn at the page break so that a heading lands after its second half: 2311717's block 61 (p6)
    and block 65 (p7) are one sentence, and `5.1 Data Exploration` follows block 65 [L].
542. A figure's tick labels can be serialised into a prose block: 2311717's block 159 carries Figure 8(a)'s axis numbers
    and both column headers as running text beside the sentence that cites Figure 8(b) [L].
543. A figure's panels can all share one bare axis name across three different scales: 2311717's Figure 7 labels every
    y-axis `attribute` while the eight panels run 3.5-5, 0-200, 0-0.15, 0-0.1, 0-0.2 and 0-1 [R].

544. A record's stored page range can fail to contain the blocks the record itself codes: 2314151 says `pages [7, 11]`
    while its first coded block is on PDF p8 and fifteen of its blocks print on PDF pp12-13 [L].
545. A chapter's own title and first section numbers can be printed inside a table block owned by the previous
    chapter: 2314151's `4 Task 1`, `4.1 Prophet algorithm` and `4.1.1 Background of the algorithm` are the tail of
    block 72, which is Table 5's grid and belongs to `data-preprocessing` [L].
546. A table's numeric column can be stored four blocks after its header, under a different table's caption: 2314151's
    Table 8 names sit in 134-138 and its twelve numbers in 146, after Table 9's caption and name rows [L].
547. A prose claim about a coefficient table can invert the table: 2314151 says `only the total ranking of word
    frequency of letters in words is strongly correlated` while that row holds the smallest R (0.008) and the largest
    P (0.87) of the six [R].
548. Two complementary variables can print exactly mirrored coefficients with identical P-values, so one column is
    derived rather than measured: 2314151's `Number of vowels` +0.083460383 and `Number of consonants` -0.083460383
    both with P = 0.093068989, consistent with `vowels + consonants = 5` [R].
549. A significance sentence can survive a row of its own table above the threshold it names: 2314151 claims `the
    P-values ... are much less than 0.05` while its Table 8 carries `Word commonness 0.103481297` [R].
550. A point forecast can be printed in a table and never quoted in prose: 2314151's `yhat = 14425.58926` appears only
    in Table 6's grid, and the text gives the interval `10355 to 18742` as its entire result [R].
551. A prediction interval's level can be left implicit in a software option and never named: 2314151 sets `interval
    width to 0.80` and then prints bounds two pages later with no percentage attached [R].
552. A figure can duplicate a table cell for cell: 2314151's Figure 5 is a one-row strip of six cells with the values
    printed inside them, the same six that Table 8 lists [R].
553. A correlation-strength scale can leave part of its range unclassified: 2314151's bands run `0-0.09` then
    `0.1-0.3`, so every absolute value in (0.09, 0.10) has no label [R].
554. A forecast horizon can be announced for a date the results table does not contain: 2314151's reading of Figure 4
    says `seventy days after January 1, 2023` (about March 12) while Table 6 predicts `2023-03-01` [R].

555. Two printed chapters can be coded as one entry whose heading names both: 2318036's heading reads `4 Task 1
    Indicators and 5 Task 2 T2PL` over a full task boundary the record marks with nothing but prose [L].
556. A chapter's last block can carry the next chapter's title and first sub-heading: 2318036 block 127 ends
    `Figure 7: Box plot result 6 Task 3: Predicting Report Distribution 6.1 Problem Analysis` [L].
557. A chapter can print nine numbered equations and contain no display block: 2318036's kinds are 63 `body`
    and 2 `heading`, and (1)(2)(3) all sit inside block 90 [L].
558. A layout can keep an equation's tag while destroying its body: 2318036 stores `h i 𝐿𝐹(𝑐) = 0` for three
    `∀`-quantified lines in block 90 and leaves block 91 with only `Í 𝑐1∈𝐶 𝑊∈𝐷` [L].
559. A layout can store a table row out of column order, so the row label lands inside its own row: 2318036's
    Table 4 reads `5 × 10⁻⁷ 2 × 10⁻³ 2 × 10⁻⁴ initial value 0.02 310000 30000 0.2 0.2` [L].
560. A layout can rotate a standard-error row relative to its coefficient row, making a sound table read as
    impossible: 2318036's Table 5 errors are stored `(2.814e-12) (5.959e-4) (2.761e-4) (0.0111) (0.0113)
    (0.0110)` while the page prints `(0.0111) (2.814e-12) ...`, and only the page order reproduces all six
    stars [L].
561. A MAPE can be defined as a percentage and then substituted as a fraction: 2318036's equation (8) prints a
    `100%` factor and block 117 uses `MAPE = 0.083`, so the accuracy is 8.3% or 0.083% depending on the line [R].
562. A prediction interval's centre can miss the point forecast it is built on: 2318036 prints `19367` and
    `[17760, 20976]`, whose centre is 19,368 and whose upper bound should be 20,974.5 [R].
563. An objective function can minimise over fewer parameters than the estimator estimates and the fit table
    reports: 2318036's equation (7) minimises over six of the eight and Table 4 reports the two it drops, L₀
    and θ [R].
564. A figure caption can be reused verbatim for a different figure: 2318036's Figure 3 and Figure 5 both read
    `two-type player dynamic system`, over a four-box block diagram and a four-series time plot [R].
565. Two figures on facing pages can disagree about the same share by two orders of magnitude: 2318036's
    Figure 5 puts loyal players at about 8,000 of some 540,000 and Figure 6's right axis puts the loyal share
    at about 80% [R].
566. A fitted parameter can fail to move with nothing in the text saying so: 2318036's Table 4 leaves γ at
    2 × 10⁻⁴ to 2.0 × 10⁻⁴ while seven others move, and no sentence mentions any fitted value [R].
567. An indicator count can exceed the table that defines it: 2318036 claims `12 indicators` over an eight-row
    Table 3, reachable only by counting LF_i five times, and the regression then uses six [R].
568. A figure-reading claim can name neither attribute its panels plot: 2318036 says `Select the two attributes
    with the strongest salience` and never names them, while the panels are labelled N_c and LF_sum [R].

569. A diagnostic figure can title all four of its panels and still be read by position: 2318982's Figure 11
    prints `Residuals vs Fitted`, `Normal Q-Q`, `Scale-Location` and `Residuals vs Leverage`, and the leverage
    panel, the only one carrying a labelled `Cook's distance` contour, is the one no sentence mentions [R].
570. A chapter's dividing heading can be the tail of another chapter's block: 2318982's `4.2 Effect of Word
    Attributes` and `5 Task 2: Distribution based on Markov Chain Model` print in bold and both sit inside
    blocks the record assigns to `results`, so the chapter has no `heading` block at all [L].
571. A numbered equation can be split from its own tag, and the split reads as two different defects: 2318982's
    displays end in blocks 77, 135 and 137 while their tags open 78, 136 and 138, so the JSON shows three
    untagged equations followed by three loose numbers while each page sets its tag in the right margin of
    the equation's own line [L].
572. An axis can print the plotting code's variable name: 2318982's Figure 8 y axis reads `data2$results`, the
    data frame and column, where the quantity's name belongs [R].
573. An equation can be re-printed as new: 2318982 prints `Y = 0.0750 - 0.0035X1 + 0.2663X2` as (3) and again
    as (4) under `the final established multiple linear regression equation was determined to be`, with no new
    coefficient, fit statistic or data between the two prints [R].
574. A criterion can be adopted and never reported: 2318982 abandons the ACF/PACF reading for an AICc-ordered
    search over `Hyndman-Khandakar`, then prints neither the candidate list nor the AICc of any candidate, so
    the evidence the paragraph promises to trust is the one thing it withholds [R].
575. A step can be numbered and never valued: 2318982's `the parameter d of the ARIMA model can be determined as
    step 1` is the whole of its differencing decision, and the value 1 first appears inside `ARIMA(1,1,1)`
    two chapters later [R].

576. A chapter's own title can be filed under the previous chapter: 2322645's `3 Word & Difficulty Representation`
    is the tail of a `data-preprocessing` block, and the record's heading line concatenates it with the second
    printed title, `4 Modeling Methodology`, to cover both [L].
577. An equation that prints as one clean centred line can be stored as three blocks in reverse order: 2322645's
    Shannon entropy line arrives as `5 X`, then the summand, then `H(X) := i=1` [L].
578. A fraction can be cut at its own bar: 2322645 stores `ft(g) = n` at the end of one block and `n1` at the
    start of the next, and stores the Beta density with its fraction in front of its left-hand side [L].
579. A chapter can print seventeen numbered headings and store two: 2322645's other fifteen live inside prose
    tails, and its two run-in sub-headings (`Word difficulty`, `Day-of-week effects`) appear in no block's
    kind at all [R].
580. The only tabular object in a chapter can be captioned as a figure: 2322645 prints two tables side by side
    under `Figure 1: Left: 30 Most common words based on overlap. Right: Frequency of Letters in the SGB
    wordbank`, and contains no numbered table at all [R].
581. A paper's own probability vector can be short one entry, twice: 2322645 draws a 7-vector from
    `(p1, p2, p3, p4, p5, p7)` in the Multinomial and hands the same six to seven concentration parameters in
    the Dirichlet, on the printed page [R].
582. A model-selection step can report its result and print none of its evidence: 2322645 sets `λ ... to 0.1 to
    obtain the desired number of parameters (four)` and prints no coefficient path, no λ sequence and no
    output table, so the one screen in the chapter is unverifiable from the paper [R].

583. A chapter can be cut three leaves short in the record: 2401298's coded blocks print on p19, p20 and p21 (a
    chapter title at the top of p20, the next chapter's `Figure 14` caption on p21) while the record says
    `pages [5, 18]` [R].
584. A block can belong to no chapter at all and still print inside a chapter's page range: 2401298's p10 carries
    the 88-word instantaneous-winning-rate definition, Table 2's caption, its column heads and its cells as
    blocks 94-97, and none of the four is owned by any chapter [L].
585. A `heading` block can be nothing but watermark: 2401298's block 181 has zero words, holds
    `微信公众号：数学模型`, and the page prints no heading at that position at all [L].
586. A chapter title can be stored as a `display` block spanning a page break the page does not have: block 180
    holds `6 Problem 4 : Swings Prediction and Model Generaliza-tion` with `[19, 20]` pages while the heading
    prints whole as the first element of p20 [L].
587. Two of a chapter's own headings can be stored inside another chapter's blocks: 2401298's
    `5 Problem 3: Momentum Prediction` is the tail of a `results` block (99) and `5.2.4 Inference on Match Data`
    the tail of another (171) [L].
588. Two figures can share one caption verbatim and the later copy be missing a panel: 2401298 prints
    `Differences in Residual Effects and Entropy` for Figure 12 on p18 and again for Figure 14 on p21, and
    Figure 14 has no entropy panel [R].
589. A figure caption can name the wrong object: 2401298's `Figure 6: feature importance` labels a grouped bar
    chart of Ljung-Box and Wald-Wolfowitz p-values with a significance line at 0.05 [R].
590. A chapter can promise a chart and then read a table: 2401298 announces `visualize the correlation between
    features using a correlation heatmap`, prints the heatmap four blocks later, and reads Table 3's
    importances in between, so the heatmap is read by nobody [R].
591. A table can print its first row under the wrong player: 2401298's Table 2 prints `Player 2` twice with no
    `Player 1` row, which detaches the paper's `increase ... by around 1%` claim from any player [R].
592. Markdown can leak into the printed page: p17 of 2401298 reads `let it predict **the sum** of the effect in
    the next n points` [R].

593. Ten blocks can be in two chapters at once: 2401445's blocks 74-83 sit in groups 5, 6 and 7 of
    `model-establishment` and in `results`, so the chapter's own block count of 71 cannot be true [L].
594. A chapter's printed model title can be stored in another chapter's block: 2401445's
    `6 Model II: Momentum Turning Point Identification and Prediction Model based on HMM-Random Forest` and
    `6.1 Definition` close block 126, which the record files under `results` [L].
595. A record can hold twenty printed numbered headings and store one: 2401445 types only
    `5 Task 2: Proving the Existence of Momentum` as a `heading` block, and six of the nineteen prose tails sit
    in blocks owned by other chapters [R].
596. A chapter's last group can be a paragraph that closes somebody else's subsection: 2401445's block 195 on
    p20 closes section 7.3, whose preceding paragraph and entire section belong to `results`, and the layout
    welds the next chapter's `8 Sensitivity Analysis` heading onto its end [L].
597. An equation tag can be split from its equation into the next page's paragraph: 2401445's (3) prints on p7
    while the block carrying the tag is attributed pages [7, 8], and (2)'s block opens `(2) m=1 where F(x)` with
    its left-hand side left behind in the previous block [L].
598. An exhibit can be bought and never opened: 2401445's Table 3 prints one grid-search row (`10 | 4 | 10 |
    300`) that no sentence in the paper refers to, and it contradicts the hyperparameter table drawn inside
    Figure 4 [R].
599. One classifier can be reported three ways that do not reconcile: 2401445 prints `an accuracy of 77.6%`,
    Table 5's per-class precision/recall/F1, and Table 6's accuracies 0.83 / 0.85 / 0.58 for the same model
    [R].
600. A figure caption can stop mid-noun-phrase: 2401445 prints `Figure 6: DPI plot of the final` [R].

601. A chapter's own numbered section headings can be stored inside another chapter's blocks:
    2401919's `4 Task3: The White Noise Tests for Our Model`, `4.1`, `4.2` and `4.4` print inside
    `results` blocks 98, 100 and 114, and its `5.3 Model Diagnosis` inside `results` block 133 [L].
602. One printed heading can be stored as two blocks: 2401919's `5.2 Utilize the Model to Obtain the
    Predicted Values` and the number `5.2.1` end block 122, while `Build Momentum Swings Grey Forecasting
    Model` - the title that number belongs to - is the whole of block 123 [L].
603. A heading can become a `display` block because a watermark string fell inside it: 2401919's
    `3.3 Determine Components and Weights` (80) and `5 Task4: Momentum Swings GM(1,1) Grey Prediction
    Model` (116) both store watermark text before the heading [L].
604. A chapter can print twenty-one numbered headings and store five: the rest are paragraph tails -
    `3.2.2` on 78, `3.4 Obtain the Scores and Visualization` on 94, `5.1.2` on 119 [R].
605. A weight list can substitute one table row for another and never say so: 2401919 prints
    `W5 = 0.0527, W6 = 0.0363`, which are Table 2's rows 6 and 7, dropping row 5's 0.0556, so the
    vector used in equation (6) is not the first six contribution rates [R].
606. A table can be captioned as a figure and read with the wrong noun: 2401919's `Figure 6` is an
    eigenvector table and the sentence reading it calls it `the table above` and its columns
    `the eigenvalues` [R].
607. A caption can be welded into the sentence that introduces its own object: 2401919's
    `Figure 4: Performance Assessment System` and the figure's node labels sit inside the opening of
    block 70, so the exhibit has no caption block and no reading unit [L].
608. A test can be reported with p-values and no statistic: 2401919 prints `p_LB = 6.645 × 10^-13` and
    `p_BP = 2.087 × 10^-12` and never prints `Q_LB` or `Q_BP`, so the reader cannot recompute either
    p-value [R].
609. A diagnosis can fold a second-class criterion into a first-class claim: 2401919 prints
    `Δ = 0.0378`, says it is `Second Class`, then calls `g0 = 0.9895` and `C0 = 0.1284`
    `both indicating a First Class accuracy` and concludes `a high level of accuracy` [R].

610. A chapter's title block can print on a leaf the record's page range excludes: 2403774's block 133
    is the `4 Task 1` title on p9 and is attributed `[9, 10]`, while `pages [10, 21]` starts the chapter on
    p10 [L].
611. A caption can share a block with a section heading, so the figure gets no caption block and the heading
    gets no heading block: 2403774's block 157 holds `Figure 7: ...` and `5 Task 2: The Momentum-Outcome
    Connection`, 160 holds Figure 8's caption with `5.2`, and 176 holds Figure 9's caption with
    `6 Bayesian Inflection point Detection and Prediction` [L].
612. Three captions can be stored as one block: 2403774's block 201 is `Figure 12: Dilated Conv Figure 13:
    Causal Conv Figure 14: MSTCN`, so none of the three has a caption of its own [L].
613. A formula can be stored with its denominator in the following block: 2403774 prints (4) as
    `Y_i = (m / M_m0)(1 - M_t) + M_t` but stores it as `Y_i = ( m ) (1 - M_t) + M_t`, with `M_m0` opening
    block 138 immediately before the `4.2` heading [L].
614. A summary equation can restate four earlier ones under a new number: 2403774's (10) is a five-line
    braced system that repeats (4), (6), (7) and (8) and carries one tag at the block's vertical centre [R].
615. A section number can be skipped and never printed: 2403774 prints `6.3.1 Design Details` then
    `6.3.3 Results`, with no 6.3.2 anywhere in the paper [R].
616. Cross-references can be off by one and literal placeholders can reach print: 2403774 says
    `as shown in Figure 12` for Figure 11, `as shown in Figure 13` twice for Figure 12, `as shown in Figure
    15` for Figure 14, `Figure 10 and Figure 11` for the two panels of Figure 10, and prints `shown in
    Figure X:` twice on p20 [R].
617. A caption can be stored as a `heading` block: 2403774's block 238 is typed `heading` and carries the
    watermark in front of `Figure 17: Visualization of women's singles scores and potential quantification`
    [L].
618. A table row can contradict the prose that cites it: 2403774's Table 5 prints the random baseline as
    `0.136022` MSE and `-2.54679` R-squared while p14 states `0.125576` and `-2.2744` for the same
    scenarios [R].
619. A hyperparameter can lose its exponent in the table: 2403774's Table 6 prints `Leaning-Rate` with the
    value `le-4`, and its caption as `Tabel 6:experimental parameter setting details` [R].
620. A table can skip a row and break across a page without repeating its header: 2403774's Table 5 runs
    `1309` then `1311`, carries an `...` ellipsis row, and loses its header when it continues on p15 [R].
621. Bold step labels can collide with equation numbers: 2403774 labels its seven XGBoost steps
    `(1) Data Preprocessing` through `(7) Model Evaluation` while its equations are numbered (4) to (13),
    so `(1)`, `(2)`, `(3)` and `(5)` each print twice within four pages [R].

622. A printed section heading can exist in no block at all: 2406176 prints `5.4 Quantification of
    Momentum` on p11 and `6.3 Exploratory Factor Analysis` on p16, the layout has no block for either, and
    seven of the twenty-three numbered headings printed between p6 and p23 are missing this way (`5.4`,
    `6.3`, `6`, `6.1`, `7`, `8.1`, `8.4`) [R].
623. A chapter can contain no `display` block at all, so every equation lives inside `body` and is torn
    wherever the block boundary falls: 2406176 stores 108 `body` and 2 `heading` and nothing else, and
    equation (5) is split across blocks 100 and 101 with its tag on the first [L].
624. One equation number can cover three unrelated definitions: 2406176's (12) tags `Aces_p𝑖`, `Break_p𝑖`
    and `Depth_CTL_p𝑖` at once on p15, sits level with the second line rather than centred, and is followed
    by an orphan centred `...` [R].
625. An equation's number can be printed before its own content: 2406176's (14) opens block 156, ahead of
    `𝑖 Indicators undergo z-score normalization` [L].
626. A matrix equation can be stored as box glyphs: 2406176's (13) keeps `𝑋1 𝜇1 𝛼11 ... ` where the
    brackets were [L].
627. Two subsections can print the same condition: 2406176's (18) and (19) both read
    `p∗𝑖∈arg max E[𝑢𝑖(...)]` and are told apart only by an asterisk on `p_{−i}` [R].
628. A body section number can contradict the table of contents: 2406176's TOC numbers the regression
    subsection `6.3` and the body prints `6.4`, while the body's own `6.3` is `Exploratory Factor
    Analysis`, which the TOC does not list [R].
629. A caption can be reused verbatim for a different table: 2406176's Table 3 is captioned `Significant
    symbols in this paper`, the notation table's caption, over columns `D Value` and `p value` [R].
630. The same pseudocode can be printed twice under two numbers: 2406176's Algorithm 3 (p16) and
    Algorithm 5 (p28, inside the AI-usage report with the prompt that produced it) are the same Bartlett
    routine [R].
631. A placeholder cross-reference can survive to print twice: 2406176 prints `Fig.x demonstrates ...`
    (p21, meaning Figure 12) and `As shown in Fig.x` (p23, meaning Figure 14) [R].
632. An algorithm can drop a branch that its own sum needs: 2406176's Algorithm 1 never computes
    `𝑝𝑆𝐴(6,6)`, so the `𝑃𝑖𝑗` sum stops at `𝑝𝑆𝐴(6,5)` and the tiebreak is missing [R].
633. A pseudocode line can describe a different model than its caption: 2406176's Algorithm 4 is captioned
    `Multivariate Linear Regression` and its inner line is `Calculate the predicted probabilities
    1/(1+𝑒^{−X𝛽})`, returning `𝛽, ˆ MMT`, an identifier that appears nowhere else [R].
634. A block can be listed twice inside one chapter's groups: 2406176's `limitations` chapter holds
    `[[224, 225], [225]]`, so 173 block slots cover 172 physical blocks [L].
635. A factor list can skip the factors it does not describe: 2406176's bullets cover Factors 1, 2 and 4
    after `Taking 3 factors as an example`, Factors 3 and 5 are never described, and all five are named
    anyway [R].
636. A caption can be welded to the next section's heading in a chapter that is not the one being read:
    2406176's Figure 12 caption block ends with `8.2 Model Generalization`, mirroring its own Figure 2
    caption ending with `5.1 Pre-match Win Prediction` [L].

637. A heading printed as a standalone bold line can be stored as the tail of a figure caption or a paragraph:
    2406324 prints `4.2`, `4.3`, `5`, `5.3` and `6` with air above and below on the page, and stores all five as
    the last line of another block (Figure 5's caption 51, 61, 67, Figure 12's caption 93, 102). This is class
    622's opposite: nothing is missing, the visual separation is [L].
638. A chapter title can be the chapter's only `display` block and span a page break the page does not have:
    2406324's block 32 is typed `display`, holds two watermark strings plus `4 Evaluation: Momentum and Swings`,
    is attributed `[6, 7]`, and the title prints wholly at the top of leaf 7 while the other 66 blocks are body
    or heading [L].
639. An extraction can drop a radical that encloses a whole expression: 2406324's loss prints as
    `L = √([Σ[P1−R1]² + Σ[P2−R2]²]/2N)` and is stored as two fragments ending `... L = 2N`, so the root and the
    fraction bar vanish and the denominator trails the numerator as a bare token [L].
640. A record note can cite equation numbers the page never prints: 2406324's note refers to `equation (1) in
    logistic form` and `the loss function of equation (2)`, and none of the five displays on leaves 7, 8 and 13
    carries a number at the margin [R].
641. A figure caption can label a table, and the prose that reads it can call it a table: 2406324's Figure 12
    caption sits on a coloured loss grid with no `Table N`, and the `results` paragraph that reads it says
    `in the table (Figure 12) below` [R].
642. A test's p-value can be read as confirming the hypothesis it rejects: 2406324 reports
    `The P value calculated by the run test is 0.000, far less than 0.05, which means the swings are random in the
    aspect of statistics`, and that sentence is the chapter's entire statistical evidence [R].
643. A standardisation sentence can set a symbol the formula does not contain: 2406324 fixes
    `α = 1, β = 0.05, γ = 0` for a formula written with `ϵ`, and `γ` appears nowhere else in the chapter [R].
644. An algorithm box can close without closing its loops: 2406324's Algorithm 1 ends at
    `9 Calculate the mean and update it as the new centroid`, the box closes there, and neither `for` nor the
    `while` is closed and nothing is returned [R].
645. Panel letters can be stranded inside a formula block: 2406324's `(a) (b)` sit in block 44 between the sigmoid
    and two watermark strings, while the page prints them under the two panels' own x-axis titles [L].
646. A schematic can carry none of the numbers its prose attributes to it: 2406324's Figure 9 prints none of
    `32 + 32 + 16` or `16 + 2`, which exist only in the sentence above it [R].
647. A page range can be wrong at both ends in opposite directions: 2406324 declares `pages [6, 19]` while the
    title prints at the top of leaf 7 and the last sentence ends leaf 17, so the range is one leaf early and two
    leaves late at once, and leaves 18-19 carry only `sensitivity-analysis` [L].

648. A heading can print standalone on the page and still be stored as the tail of the paragraph before it, six
     times in one chapter: 2409404's `3.3`, `4`, `4.3`, `5.2`, `5.3` and `6` all print bold on their own line with
     air above and below, and all six sit at the end of another block, so any index that trusts the layout text to
     find a section start finds nothing at six of the fourteen boundaries.

649. The heading count can be wrong in both directions at once: of 2409404's fourteen printed headings, eight are
     typed `heading` and one `heading` block (83) is the Figure 3 statistics table, so the typed count (9) and the
     printed count (14) have no term in common except coincidence.

650. A section number can migrate to the end of the title in the ledger while printing at its front: 2409404 stores
     `The Runs Test —Stochastic Analysis 4.1 微信公众号：数学模型` and `The Chi-square Test —Correlation Analysis 4.2
     微信号：MATHmodels`, where the page prints `4.1  The Runs Test —Stochastic Analysis` and the heading line ends
     at `Analysis` - the watermark is not part of the heading and the number is not trailing.

651. A caption can sit inside prose for every exhibit in a chapter, and the figure/table distinction can survive only
     in the placement: 2409404's six figure captions are below their figures and its four table captions above their
     tables, and all ten are the last run of text in a `body` block, so the ledger keeps neither the placement nor
     the kind.

652. A bullet can be one continuous paragraph on the page and forty line-blocks in the ledger: 2409404's §5.4 prints
     five bullets of ten to fourteen wrapped lines each with a bold lead-in, and the record's last three units carry
     42 blocks for those five bullets, eleven of them beginning on a lowercase letter.

653. A float can split a sentence across a leaf boundary, and the statement can then appear as two paragraphs with
     unrelated openings: 2409404's Table 6 occupies the top of leaf 15 between `accurately forecasting the` (leaf
     14) and `game's trajectory.` (under the table), and the record files them as blocks 138 and 140.

654. A table's sub-tables can duplicate each other with permuted labels: 2409404's Table 5 prints eight chi-square
     sub-tables where 1 and 3 carry the same counts and the same `151.617` / `9.167 × 10−32` pair with the 0/1
     columns swapped, 2 and 4 repeat with `150.065` / `1.962 × 10−31`, and the labels permute (`p2W` over `p1N`
     rows, `p1W` over `p2N` rows), so the intended assignment is unrecoverable from the page.

655. A chi-square test can be read without a reference value: 2409404 prints no degrees of freedom and no critical
     χ² anywhere, then writes `the χ2 for each test is greater`, which has nothing to be greater than, unlike the
     runs test whose `Z` column at least carries a sign.

656. A normalisation formula can index its numerator and take the maximum of a different symbol: 2409404 prints
     `FIη = 100 × pη / max (FI)`, and the sentence above it says `We then normalize the pi values`.

657. A correlation figure can carry no numbers and an unexplained colour cut: 2409404's Figure 7 prints no value on
     any of its 43 bars, colours 28 green then 15 grey at a dashed rule on the 28th bar, while the 28 paired
     indicators are interleaved with the 15 singles (PV third, SER seventh) - and two clip-art icons sit over the
     plot area.

658. A biplot can print loading arrows whose labels overprint each other and axes with no tick values: 2409404's
     Figure 6 left panel collapses `PCDR`, `P1BPW`, `P1PW`, `GNO`, `P1BP` and the rest into one red pile and leaves
     `PC1`/`PC2` unnumbered, with its `0`/`1` legend unexplained in the text.

659. A legend can be a continuous colour scale standing in for two categories: 2409404's Figure 5 keys
     Novak Djokovic and Carlos Alcaraz by two colour bars whose values (`15` to `−15`) repeat the y axis, and its
     dashed reference lines (red at 0, orange and black verticals) are explained nowhere.

660. A table can be pasted into the paper as a picture and then called a graph by the prose: 2409404's Figure 3 is a
     screenshot of a statistics table with bar backgrounds, captioned `Technical Statistics`, and read as `Based on
     the graph, it is evident that Alcaraz's serve is far superior`.

661. A heading can be typed as a table and a table as the only display: 2409404 types its Figure 3 statistics table
     `heading` and its Table 6 `display`, so the ledger's single display marks a table while a table marks a
     heading - two errors that cancel in the totals.

662. An equation can have a limit with no dummy index: 2409404's (1) prints `Σ` from `i−β+1` to `i` over terms
     indexed `i`, so the free player index and the upper limit are the same symbol and the sum has no variable.

663. An equation's tag can print on top of the page furniture and be extracted ahead of its own content: 2409404's
     `(10)` sits at the right margin over the QR badge at the foot of leaf 11, and the ledger puts it as the first
     token of block 110 while the equation it numbers ends block 109.

664. A sheet's page field can be right at both ends while the head count is not: 2409404 declares `pages [6, 16]`,
     verified leaf by leaf, and `Stored count 12, coded 12`, and still miscounts its own headings and describes two
     paragraph tails (`4`, `5.2`) as headings - correctness of the page field is no evidence about the rest of the
     record.

665. A record can be regrouped under a finished pack without touching the blocks: `P-C-2020-2010638-c32c8549` kept
     82 blocks and `pages [6, 16]` and moved from 76 units to 52, which turns a green pack red with no pack edit and
     no block change - only the group boundaries.

666. A chapter can open mid-leaf behind another chapter's heading: 2409961's leaf 6 prints `3.2 Data Cleaning`
     from the previous chapter, then `4 Instantaneous Scoring Rate Model` and `4.1` on the same leaf, so the
     printed page a chapter starts on is not a clean boundary - and a page field that names the section number's
     page can be one page late while looking right.

667. The chapter title can have no block at all: 2409961's `4 Instantaneous Scoring Rate Model` prints on leaf 6
     between `3.2 Data Cleaning` and `4.1` and appears in none of the 77 coded blocks, so the one heading every
     reader needs is the one the ledger cannot quote.

668. A folio offset can turn a correct-looking page field into a range that excludes the chapter's own mathematics:
     2409961 prints `Page N of 24` at offset -1 on 25 leaves, the record cites `pages [6, 16]` in printed numbers,
     and equations (1) and (2) therefore sit on a page the field says is not this chapter.

669. A paper can print headings at body size with no number, and the ledger then reads them as short paragraphs:
     2409961's `Classify the input of GRU` (107), `Quantitative Analysis of the Impact of GRU Input` (119) and
     `Selecting high-impact information from attributes` (126) are five- to eight-word blocks that are really
     section heads, so the hierarchy jumps from `6.1` to `6.2` with three unnumbered sections in between.

670. One caption can be reused verbatim on two different tables and then cited by the wrong number: 2409961's
     `Table 1` (symbols, printed page 4) and `Table 2` (aggregation dimensions, leaf 13) both carry `Notations used
     in this literature`, and the prose cites `as shown in Table 1:` for the second.

671. Two of a table's six rows can be duplicates with different labels: 2409961's `Offensive` and `Skill` rows list
     the same five indicators (`server, speed mph, serve width, serve depth, return depth`), so one aggregation
     dimension is counted twice.

672. A distribution can be called bimodal and read off a `wave peak` when the figure prints bars only: 2409961's
     Figure 6 has at least five local maxima, no fitted curve and no wave, and two separate paragraphs argue from
     its shape (and the dashed normal curves the argument needs are in Figure 5, one leaf earlier).

673. A zero crossing can be the chapter's central rule while the zero line is not drawn: 2409961's Figure 7 marks
     zero with an ordinary gridline and encodes the sign only as fill colour, so `when the average line crosses the
     0 axis` refers to a rule the reader has to reconstruct from two shades.

674. A two-panel figure can lose its own encoding in one panel: 2409961's Figure 4 draws both players with
     identical black markers in the left panel - with a legend that names `Player 1` and `Player 2` beside a single
     marker style - while the right panel is colour-coded.

675. An unrendered cross-reference can reach print: 2409961 writes `we can see in the Figure ??` for Figure 11, so
     the placeholder itself is the citation.

676. Citation drift can begin exactly where the argument stops and the advice starts: 2409961's first five figure
     citations name their own object and its last five do not (`Figure ??`, `Figure 16` three times for Figure 12,
     `Fig. 1`), so the error is not random noise but a property of the second half.

677. An equation can solve one variable under two names: 2409961's (3) prints `f(t) = yi + (...)x + mi/2 t2 + ...`
     with the validity interval `(ti <= t < ti+1)`, so the linear term is in `x` and every other term in `t`.

678. An integral's limits can be written in a different dummy from its integrand: 2409961's (11) prints the limits
     `a=0` and `1` over an integrand in `alpha`, so the notation does not close.

679. A figure caption can name a different object from the plot's own title every time: 2409961's Figures 2, 3, 4,
     5, 6, 7 and 10 each carry a caption and an in-plot title that disagree (`Relative Score Curve` vs `Cubic Spline
     Interpolation of the Given Data`, `March Flow` vs `Derivative of the Cubic Spline Interpolation`, ...), which
     gives one object three names once the prose adds its own.

680. A dimension can be counted in a way that does not close: 2409961 writes `47 dimensions ... after removing the
     5-dimensional information ... 39 dimensions of relevant information and 1 dimension of real-time score`, i.e.
     47-5 gives 42 and the paper reports 40.

681. A model can be identified against fewer matches than it has unknowns while saying both numbers: 2409961 derives
     `32*6` unknown quantities and then squares the system by asserting `there are only 31 sets of data`, so the
     unique solution it claims needs a match that does not exist in its own count.

682. A chart's printed values can be the only checkable exhibit in a chapter: 2409961 prints values on none of
     Figures 2, 3, 4, 5, 6, 7, 8, 9, 11 or 12 and on all six bars of Figure 10, so the one claim a reader can verify
     is the one the text uses least.

683. Page furniture can be captured one block off: in 2410482 each leaf carries `Team 2410482` and `Page N` on
     a rule above the text column, and the head that opens leaf N+1 is appended to the tail of the block that
     starts on leaf N, so a quote ends `... 关注数学模型 MATHmodels 获取更多资讯 Page 6` and cites the wrong page.

684. The one exception runs the other way and is worse: block 118 of 2410482 is a leaf-14 block that *begins*
     `Page 13 6 Momentum Projections,...`, so the head of the previous leaf arrives ahead of the chapter title
     it precedes and the chapter heading is buried behind a page number.

685. A watermark can sit inside the paragraph it interrupted, in 38 of 109 blocks in one chapter: 2410482's
     `微信号：MATHmodels` lands mid-sentence (`... shown in the following table: 微信公众号：数学模型 0 1 2 ...`),
     so any quote lifted from the layout can silently contain advertising.

686. A subsection number can be stored as a zero-word block of its own with its title in the next block:
     2410482 has `4.1.1` alone in block 52 and `Explanation of the Serving Scoring` in 53, and `6.1.1` alone in
     121 with `Introduction to State Space Model and Kalman Filter Algorithm` in 122.

687. A heading can be welded across a group boundary, so the number ends one unit and the title opens the next
     with no number at all: 2410482's `4.1.2` ends G02 and `Establishment and Predictive Outcomes of the Markov
     Model` opens G03, and 2410482's `6.1.4` ends G11 while the body under it is filed in another chapter.

688. One chapter's page range can wholly nest inside another's: 2410482 declares `model-establishment` at
     `[5, 20]` and `results` at `[8, 18]`, and the inner chapter holds both of the outer chapter's figures, their
     readings and its evaluation table, so "chapter" is not a page interval at all.

689. The same block can be coded twice inside one chapter: 2410482's `results` chapter holds block 100 both
     inside the group `[98, 99, 100]` and as the whole of a fourth group, and only the second-chapter copy is
     visible to a reader who walks the record in order.

690. A weight vector can carry more entries than the model has factors, on the page: 2410482 names `the five
     important factors`, defines `𝜔 = [𝜔1, 𝜔2, 𝜔3, 𝜔4, 𝜔5]` over five `X` components, and then sets
     `𝜔 = [0.5, 0.2, 0, 1, −0.1, 0.1]`.

691. A 0-1 dummy can be defined against the algebra that consumes it: 2410482 says `0 is taken if set t won and 1
     is taken if set t lost` and then writes `𝐿𝑡−1(−1)𝑟𝑡−1`, which rewards the wrong side.

692. A step size can be renamed between the display and the sentence under it, to a letter already in use:
     2410482's `(10)` reads `𝛽𝑛𝑒𝑤= 𝛽𝑜𝑙𝑑+ 𝛾𝜕ℓ/𝜕𝛽` and the next block says `𝛼is the optimized parameter`, while
     `𝛼` is the exponential decay constant of `(5)`.

693. A correlation figure can plot more variables than the prose counts: 2410482's body lists twelve factors and
     Figures 10 and 11 both carry fourteen axes, adding `Swings of Momentum` and `Set Point(Game Point)`.

694. Two figures can plot the same matrix twice and differentiate only by the side the numbers are printed on:
     2410482's `Figure 10: Correlation Analysis figure1` prints values in the upper triangle and `figure2` prints
     them in the lower, over identical rows.

695. A regression table row can contradict its own statistics on the page: 2410482's net-point row pairs
     coefficient `-0.251` with `T-statistic 0.704`, `p. value 0.402` and an interval `(-0.8384,-0.3358)` that
     excludes zero, and another row's interval prints `0.0052,0.0103)` with no opening parenthesis while the
     `intercept` interval cell is empty.

696. A QR sticker can be laid out inside the text column: on 2410482's printed page 7 it covers the last line of
     the diminishing-utility paragraph, so the sentence stops at `shows a decreasing` in both the raster and the
     extraction.

697. One record can use two page bases inside the same chapter: 2410482's field is `pages [5, 20]` in PDF-leaf
     numbers while its own heading reads `(pp. 5-20)` in printed numbers, and the paper's folio runs one behind
     the leaf.

698. A figure caption can be set in a different language from the paper: 2410482's `图 5: momentum trends of
     Novak Djokovic in 2023 Wimbledon Gentlemen's final` is the only Chinese caption among ten.

699. Captions can name the exhibit's genre instead of its content, and the genre can be the same for unlike
     objects: 2410482 captions one exhibit `chart`, two `schematic`, one `flow chart`, one `prognostic map`, and
     distinguishes its two matrices only as `figure1` and `figure2`.

700. A colour-coded table can carry its key nowhere: 2410482's score grid prints some cells in blue italic and
     others in red italic, and no legend, caption or sentence says what the two colours mean.

701. A five-column table can be flattened into two prose blocks with the header order scrambled: 2410482's
     evaluation table prints `indicators | MSE | RMSE | MAE | R²` over `0.0454 | 0.2131 | 0.1660 | 0.8902` and the
     layout renders it as `R2 indicators MSE RMSE MAE ... 0.8902`, so a checker who counts columns gets the
     wrong statistic.

702. A section heading can be welded onto the last block of the previous chapter's body while printing standalone
     on the page: 2410482's chapter 7 title arrives inside block 161's tail (`... to gain momentum. ExtensionTest
     ——InWomen'sTennisandTableTennisMatches 7`) although it has its own line and its own air on printed page 19.

703. A record's own note can assert an equation-numbering gap that the page does not have: 2418251's unit 2
     note reads `the equation numbering skips (7) and (8)` while (7) prints in block 63 and (8) in block 65,
     both inside that unit, which is how the chapter reaches (9) with nothing missing.

704. A ledger definition can print with stray summation signs and no index: 2418251's (11) is set as
     `M_i = M_b + M_s + ΣM_c + ΣM_u` with two bare sigmas and no limits, so the per-game total has no stated
     domain and the per-set sum in (12) has nothing to inherit.

705. A correlation matrix can print the same index twice on the page: 2418251's (16) sets its second row as
     `r21 r22 r11`, so the cell that should be `r2j` carries the first row's first entry.

706. A two-player comparison table can head both sides with the same column name: 2418251's Table 8 prints
     `Winning probability_P1` twice, once over each player's column, and no sentence names which side is which.

707. A forecast table can end on the same value twice: 2418251's Table 11 gives Carlos Alcaraz `34.3283` for
     each of his last two games, closing a ten-game ARIMA forecast on a repeated number.

708. A feature list can name one feature twice and drop another: 2418251's PCA input names `Potential
     point_Serve` twice and omits `Potential point_Break of Serve`, although the four events it defines are
     serve, continuous scoring, break of serve and unforced errors.

709. A heatmap can print no cell value at all: 2418251's Figure 9 covers every game row against three principal
     components and leaves all cells blank, with only the colour bar to read.

710. A figure can be laid out with oversized numerals printed over its own traces: 2418251's Figure 8 sets a
     grey `1` and a grey `2` across the plot twice each, and they occlude the five set series they label.

711. A figure can be laid out under a publisher's logo: 2418251's Figures 11, 12 and 14 sit behind a large
     pale-yellow circular watermark that covers the middle of the plot area.

712. A caption can name the wrong player role for its own plot: 2418251's Figure 5 reads `The fitting results
     for the service player's receiving probability` while the plot's own title is `Receiving player's winning
     probability` and the text above it discusses the receiver.

713. A model order can be published with no criterion and no search: 2418251 gives `p=4, d=1, q=4` as the
     ARIMA order with no AIC, no grid and no sentence saying why four lags.

714. Two tables with identical headers can be captioned as different quantities: 2418251's Tables 6 and 7 both
     print `Set_no. | Game_no. | M_b | M_s | M_c | M_u | Distance_run | Potential points | Momentum` and are
     captioned `momentum points and momentum data` and `potential points and momentum data`.

715. A chapter can close on the next chapter's title typed as a display block: 2418251's block 198 is a
     `display` whose whole content is a watermark plus `6 Verification and Application of the Model`.

716. A `heading`-typed block can be a bullet: 2418251's block 95 opens `• Serve:Serving is crucial in tennis`,
     the first of four feature bullets, and is one of six blocks typed `heading` that hold no heading.

717. A duplicate coefficient can close two different players' factor tables: 2418251's Tables 9 and 10 both end
     on `−0.654`, so the last factor's cross-player coefficient is reported once and printed twice.

718. A running folio can live outside the text layer entirely: 2418251 prints `Page N of 23` on every leaf and
     not one of the 132 blocks carries the string, where 2410482 carries it in 15 of 109 - so the same
     page-base check fails on one paper and passes on the other for a rendering reason, not a coding one.

719. A figure can contradict the worked example that defines it: 2425454's bullets take player A from `0-15` to
     `30-30` if he wins the point and to `15-40` if he loses it, while Figure 6 prints the realistic scenario as
     `15-15` and the opposite scenario as `0-30` - three of four scores differ from the text.

720. Two exhibits can share one caption and only one of them can be right: 2425454's Figure 10 and Figure 11 are
     both `GSRF Algorithm Flow Diagram`, and Figure 10 is a momentum time series, so the flowchart's caption is
     printed twice and the chart's caption is never printed.

721. A confusion matrix can contradict the accuracy stated one page earlier: 2425454's Figure 12 gives
     `7 0 0 / 0 50 2 / 0 1 7` - 64 of 67, i.e. 95.5% - against the `94%` the text claims for the same model.

722. A sentence claiming no error of a kind can be falsified by the matrix printed directly above it: 2425454
     says `none of the samples from any of the reversal point types were categorized into another reversal point
     type` while its own matrix shows two `Actual 0 -> Predicted 1` and one `Actual 1 -> Predicted 0`.

723. A table can be cited under a number it does not have: 2425454's text says `for each cell in Table 1
     calculate the expected frequency E`, and the table it means is captioned `Table 2`; no Table 1 exists in
     the chapter.

724. A contingency table can be printed as symbols only, and a statistic computed from it anyway: 2425454's
     Table 2 shows cells `n11 n12 n21 n22` and no observed frequency, while the text reports `X = 5.566` and
     `P = 0.018` for exactly that table.

725. A smoothing denominator can introduce an index the paper never defines: 2425454's momentum display closes its
     numerator on `(1 − α)^i` and its denominator on `(1 − α)^t`, so one fraction names its window two ways.

726. A combinatorial probability can reuse a term: 2425454's `P(r = 2k + 1)` prints `C(m−1, k−1)` twice and then
     `C(n−1, k) · C(n−1, k)`, so the odd-run distribution as printed is not the standard one.

727. A complement can be printed without its minus sign: 2425454's null hypothesis says `the probability of
     drawing Y as 1P`, which joins `P` and `1 − P` into one symbol.

728. A regression model can be fitted to class labels while the surrounding text describes classification:
     2425454 trains `RandomForestRegressor` on the `1 / 0 / −1` reversal label two subsections after describing
     the forest's `classification process`, `CLASS A`/`CLASS B`/`CLASS M` leaves and `Voting`, and the grid it
     reports is a classifier's grid searched on a regressor.

729. A table's shading can mark the smaller of two loadings: 2425454's Table 5 shades `brp1` on factor 2 at
     `0.502` although the same row prints `0.569` on factor 1, so the printed assignment contradicts the printed
     magnitude.

730. A threshold can be drawn and never named: 2425454's scree plot carries an unlabelled red dashed rule at about
     8%, and the text justifies the four-factor cut by `the contribution rate became quite small` without citing
     the line.

731. An importance chart can rank by colour with no key and no values: 2425454's Figure 13 prints one bar in red
     among 41 in blue, no legend, no value labels, and the prose then reads the red bar as `the total score of
     opponents`.

732. An indicator list can define two different variables under one name and give a third the first one's
     definition: 2425454 defines `p1_ace` twice (flag and total), `p1_double_fault` twice and `rally_count`
     twice, and describes `p1_winner` as `Whether player 1 hit an "unreturntable" ball`, which is `p1_ace`.

733. Caption vocabulary can diverge from the body's terminology twice in one chapter: 2425454 captions Figure 4
     `Short-Term Incentives ... as a Function of Order` where the body says `short-term motivation` and the axis
     says `Ordinal Number`, and captions Figure 14 `Screep plot`.

734. A schematic can print scores in unlabelled columns, so the reader cannot say which number is the set, the
     game or the point: 2425454's Figure 6 shows `PLAYER A 6 6 2 0` with no header row over the four columns.

735. Algorithm pseudocode can be misnumbered and mis-typed inside its own listing: 2425454's Algorithm 1 carries
     `Calculate scoring probability based on the formula.3` (a dangling reference), `until one side wins the
     match;;` (doubled semicolon), `for i 1 to n do` (missing assignment) and reuses the index `i` for both the
     outer score loop and the inner simulation loop.

736. A nested `results` chapter can be the entire chapter rather than an overlap: 2425454 declares `results` at
     `pages [9, 17]` and all 27 of its blocks print inside the model chapter's `[6, 19]`, so all four of the
     model chapter's numeric joins cross foreign blocks and every result - the runs-test verdict, the
     contingency chi-square, the forest's accuracy and its hyperparameters - is filed away from the unit that
     argues for it.

737. A layout block can span several pages and silently delete the middle one: 2500759's block 36 spans
     `[6, 8]`, and printed page 7 - four feature-design lead-ins plus nine numbered displays, (1) through (5) -
     appears in no block, so the chapter's entire formal model is missing while its page range covers it.

738. A paper section can be absent from the record because a page-spanning block ate its pages: 2500759's block
     123 spans `[17, 20]` and pages 18-19 hold `4 Problem 2: The Great Coach Effect`, the DID display (9) and
     Table 4; no block contains `DID` or `Table 4`, and the record has no chapter for that problem.

739. A word count can be inflated by an invisible text-layer stamp: 2500759 carries 687 `ArialMT` glyphs of the
     letter `m` at 1.379 pt in a 37x37 lattice on nine leaves, zero ink measured, and they add 2,748 of the
     chapter's 4,971 tokens - 120% inflation with no effect on the page.

740. A numbered test statistic can print in a form that cannot depend on the data: 2500759's Spearman display gives
     `t = |ρ| / sqrt(ρ²/(n − 2))`, which cancels to `sqrt(n − 2)`, so every sport would receive the same p-value.

741. A rank-sum table can print statistics above the test's own maximum: 2500759's Table 3 gives `w⁺` of `538231`
     and `532048`, but 1,000 bootstrap draws cap the signed rank sum at `1000 x 1001 / 2 = 500500`, and no
     effective sample size is printed anywhere.

742. A confidence-interval column can exclude its own point estimate: 2500759's Table 2 prints `AUS 19 (10.41,
     16.13)` and `NZL 11 (4.82, 9.33)`, so the third-ranked country's interval sits entirely below the point
     estimate of the fourth.

743. A p-value column can be relabelled as a probability and its ordering inverted: 2500759 reads Table 3's
     `0.847` and `0.684` as `probabilities of 0.847 and 0.684` and concludes that `a larger P-value indicates a
     smaller probability of committing a Type II error`.

744. A table row can be duplicated and survive proofing: 2500759's Table 3 prints `MKD 153243 1.22e-26` and
     `BFA 153243 1.22e-26`, identical to six and three significant figures.

745. A claim about how many rows cross a threshold can be falsified by the table directly beneath it: 2500759 says
     `only two countries ... had test statistics corresponding to P-values greater than 0.05` above a table whose
     `GRD` and `GHA` rows both print `1`.

746. A schematic can grade the model on a metric the paper never defines: 2500759's Figure 5 ends on `Evaluate
     model stability using metrics such as MSE, MAE, and cross-validation` while the whole loss discussion is
     built on WMAE, defined in (6) three paragraphs earlier.

747. A table can be captioned as a figure: 2500759's `Figure 10: Top 15 Sports Event Importance Score` is a
     15-row two-column table with two identical `Sports` headers, dotted sport names and unlabelled bars whose
     scales are not shared between the halves.

748. A figure can be described on the page by a shape it does not have: 2500759's block 112 calls Figure 9 `the
     hexagonal importance mix plot` and the figure is a beeswarm plus a bar panel, captioned `Cellular-Importance
     Mixed Plot`.

749. A heatmap can be read at a value below its own scale, for a category it does not plot: 2500759 reports
     `Skateboarding and Karate showcase a lower correlation for gold medals (0.210)` on a chart whose colourbar
     bottoms out at `0.24` and which has no Karate column.

750. A stacked bar can add two incompatible metrics and name a dimension it does not carry: 2500759's Figure 4
     stacks WMAE_Gold on WMAE_Total over `hidden_size` alone, while the sentence citing it names the
     `32x6` and `128x10` cells that only Figure 3's `patience` axis encodes.

751. A chapter section can cite no exhibit at all: 2500759's 27-block SHAP and Spearman unit names no figure, and
     the six figures that report its result are captioned and read inside the `results` chapter.

752. A paper's exhibit numbering can begin at two with nothing missing from the text layer: 2500759 has no
     `Figure 1` and no `Table 1` anywhere in 203 blocks, while Figures 2-17 and Tables 2-5 are all present.

753. A page can be a bitmap of itself, so a whole section can exist only as ink: 2501869 pages 13, 15 and 20
     are each one 1654 x 2339 inline image at 200 ppi with the folio baked in, and `5.5`, `5.5.3`, `6.2`, `6.2.1`,
     `6.2.2`, Tables 5-6, Figure 8 and equations (11)-(12) are in no text layer - `6.2` occurs zero times in the
     document's 123,402-byte text layer.

754. A layout block can span a raster leaf and make an unreadable page look like an empty one: 2501869's block 103
     spans `[12, 14]` and block 144 spans `[19, 21]`, so pages 13 and 20 are attributed to a neighbour, while page
     15 - between two blocks - starts no block at all and reads as a hole rather than as a scan.

755. A word count can be inflated by a dead vector twin of an embedded figure: 2501869 carries exactly 687
     single-character `ArialMT` spans per affected leaf, one per leaf on three in-chapter pages, which are a
     pgf/TikZ chart scaled to 13.8% and painted over by the raster of the same figure - zero ink at 400 dpi, and
     2,061 of the chapter's 4,247 layout tokens.

756. A layout's `display` type can mark only artifacts: 2501869's whole 212-block document has exactly two
     `display` blocks, 98 and 151, and both are 687-token runs of that invisible twin, so the type returns an
     equation count of zero against twelve numbered displays actually printed.

757. A significance star can contradict the standard deviation printed beside it, in both directions:
     2501869's Table 8 prints `3.42***` on an SD of `4.57` (t = 0.75) next to `4.145**` on `0.18` (t = 23), and
     about 28 of its 61 starred cells fail the ratio they claim.

758. A two-part model can report its censored count equal to its total: 2501869's Table 8 prints
     `Observations noncensored 554` against `Observations total 554` in both Hurdle models.

759. Three tables can report the same explanatory models with three different sample sizes: 2501869 gives
     `529 / 1232` in Table 6, `554 / 1289` in Table 8 and `554 / 1289` again in Table 11, with `Host country t`
     at `1.566*** / 12.520***` against `1.354*** / 5.520***`.

760. A row can be printed twice inside one regression table: 2501869's Table 6 prints
     `Medals_PCA(t-4) 3.725*** 0.12 3.42*** 4.57` as both its ninth and eleventh row.

761. One variable's cells can be copied into another's row: 2501869's Table 6 gives `Num_Events` the Tobit cells
     `1.828** / 1.07` that belong to its `RCA` row, verbatim.

762. A regression table can leave its intercept row with no estimates at all: 2501869's Table 6 prints
     `Constant` and four empty cells.

763. A descriptive table's parts can sum to less than half its own total: 2501869's Table 1 prints `Gold 1.59`,
     `Silver 1.59`, `Bronze 1.85` and `Total Medals 11.42`, with a total SD of `19.7028` against component SDs
     of 4.97, 4.83 and 4.83.

764. A confidence interval can print its upper bound below its lower bound: 2501869's Table 3 gives Great
     Britain a Hurdle forecast of `68` with lower CI `63` and upper CI `53` - the only row in the table whose
     interval fails to bracket its estimate.

765. A forecast-accuracy table can print with no number, no caption and no column headers: 2501869's page-11
     table is titled only `Rate of right forecasts for 2024 Paris Olympic Games`, and nothing in it says which
     column is Hurdle and which Tobit.

766. An accuracy table's own body can live in another chapter's blocks: 2501869's layout puts its title in block
     89 and two rows in 90, but `69.1% (107 countries)` in block 91 and the whole 56-country subset in block 92,
     both owned by `results`.

767. A figure can be an unattributed screenshot of third-party data presented as the paper's own result: 2501869's
     Figure 10 shows `Well-Log Data Set` and `Global Surface Temperature Anomalies` with no citation, directly
     after `Such obvious turning points can be identified using a Bayesian change-point detection`.

768. A figure can carry the previous figure's caption: 2501869 captions Figure 11 `Two Types of Change-Point`,
     which is Figure 10's caption, for a plot of original against processed medal score.

769. A figure's marked event can contradict the table beside it: 2501869's Figure 11 marks
     `1996 Atlanta Olympics (Mary Lou Retton)` where Table 9 puts the gymnastics change point at `1984`, and
     Retton competed in 1984.

770. A figure legend can name categories its axis does not contain: 2501869's Figure 8 legend lists
     `Modern Pentathlon`, `Fencing` and `Weightlifting` for a three-colour stack repeated across ~33
     disciplines, and `Modern Pentathlon` is not on the axis at all.

771. A figure caption can name a variable its panels do not plot: 2501869's `Figure 7 Comparison of RCA,
     Num_Events and Total by Country` prints two panels whose x-axes are `Number of Events` and `NAE`; no RCA
     appears.

772. An equation can overrun the text measure and lose its own number: 2501869's (2) runs about 72 pt past the
     block to the page edge, clipping the final subscript, and its `(2)` drops to a separate line below.

773. A coefficient gloss can put seven scalars into a 3-vector: 2501869 writes
     `c, lambda, rho, gamma, delta, zeta, kappa in R^3 are all coefficients, representing the value of
     X_{i,t}Theta for gold, silver and bronze`.

774. A bullet can print the same clause twice in one sentence: 2501869 prints `which may affect its statistical
     significance, which may affect its statistical significance and should be interpreted with caution.`

775. A caption can carry an unbalanced quotation mark: 2501869 prints
     `Figure 8 Top Contributing Sports to Medal Counts: the United States and Egypt"` with a closing quote and
     no opening one.

776. A contribution quotient can be printed identically for three different numerators and read as
     convergence: 2503389 prints `0.3/DUSA`, `6.9/DUK` and `1.3/DCHN` all `= 1.7` and concludes that the values
     "converge to 1.7"; the denominators those quotients need are 0.176, 4.06 and 0.76, and no D is printed anywhere.

777. A weighting scheme can be attributed to PCA with expert validation that is never run: 2503389's 40/30/20/10
     weights are described as "a hybrid weighting scheme, integrating Principal Component Analysis (PCA) with expert
     validation", and no loadings, eigenvalues, explained variance or panel appear anywhere in the paper.

778. A weighted-sum indicator table can put three inputs on one scale and the fourth on another: 2503389 gives NMP,
     GCP and ASD a `x 100%` formula and LAS `1 - σ/μ`, so three indicators enter the sum on 0-100 and one on 0-1.

779. An odds column can contradict both its accuracy column and its own parenthetical: 2503389 pairs `88.09%` with
     `4:1 (80% chance)`, where 0.8809/0.1191 = 7.39; only its Random Forest row (`94.12% -> 16:1`) is consistent.

780. A regression table can report a "Multivariate Linear Model" with no intercept row and never discuss its
     largest coefficient: 2503389's Table 4 prints four rows and no constant, and its Host Boost row (13.10, the
     largest) is absent from all three reading bullets.

781. A correlation matrix can show a predictor at exactly 1.00 against the target and the paper can keep it: 2503389's
     Figure 2 prints `XHist` vs `Award Winning Rate` as 1.00, rows 3 and 4 near-duplicate, and the variable is fed
     into an ensemble instead of being dropped.

782. A descriptive caption can name fewer variables than its matrix holds: 2503389 captions Figure 2
     `Correlation Matrix(XComp, XAth, and XHist)` for a 4 x 4 matrix whose fourth row and column is the target.

783. A caption can ship as an unfilled placeholder that names only a country: 2503389's Figures 11-13 print
     `Figure 11: Caption for Britain`, `Figure 12: Caption for USA` and `Figure 13: Caption for China` in a
     Computer Modern face unlike the Times body.

784. A forecast table can be dated to a year the surrounding prose treats as past: 2503389 captions Table 3
     `2024 Olympic Medal Predictions` while the prose compares against `64 in 2024` and `91 in 2024` as results and
     Figure 6 runs to `LA 2028`.

785. A change column can print a dash in exactly the rows the caption promises: 2503389's Table 3 caption offers
     "Rankings, Changes", and its rank-Δ column reads `-` for all of the top six.

786. A prose citation can name a country that is not in the table it cites: 2503389 writes `Slovenia (1 gold,
     CI: 0-2)` about a Table 3 that prints ten rows and stops at rank 10.

787. A fusion weight can be derived from errors that contradict the sentence introducing it: 2503389's
     `wMLR ≈ 0.6` implies PE2_MLR < PE2_NN, and the paragraph immediately after opens "it is clear that the MLP model
     suffers from higher errors".

788. A histogram's median marker and its tallest bar can sit one bin apart with only the bar reaching the prose:
     2503389's Figure 9 has its highest bar at 3 and its `Median: 4.00` marker at 4, and section 6.5 repeats only
     the 3.

789. A "correlation" scatter can be drawn as vertical strips, one per period, so the slope is between-periods and
     not between-units: 2503389's Figure 10 stacks every country at a handful of discrete x values and the prose
     reads the resulting slope as a nation-level relationship.

790. An invisible QR code can be typeset as text: 2503389 carries 687 single-letter `ArialMT` spans at 1.38 pt on a
     37 x 37 grid inside a 68 pt square drawn at fill alpha zero, one per affected leaf, measuring zero ink at
     130 dpi - 4,809 of the chapter's 7,373 layout tokens, and two owned blocks consist of nothing else.

791. A full-page inline bitmap is invisible to tooling that counts XObjects: 2503389's pages 10, 17 and 18 are each
     one `BI /W 1654 /H 2339 /BPC 8 /CS /RGB` inline image, so `get_images()` returns 0 and `get_drawings()` 0 while
     the leaf holds a whole section, a table and a figure - an auditor reading object counts alone reports the page
     as empty.

792. One dataset can be fitted twice and both fits reported as significant, with every downstream section using
     the second silently: 2505964 states `Intercept β0 ≈2.4595` and `Coefficient β1 ≈0.0517` at `p < 0.001` in
     3.3.3 and then Table 4 prints `0.7933` and `0.1912` at `p < 0.001`, and the elasticity series (0, 1.912,
     3.824), Figure 13, Figure 15 and every leave-one-out test inherit 0.1912 without one sentence reconciling them.

793. A printed exponent can lose a digit while keeping the right value: 2505964 writes `When exponentiated,
     e0.912 ≈1.211` against a coefficient of 0.1912 - e^0.1912 = 1.2107, so the result is correct and the exponent
     is off by a factor of 4.8, and no reader checking the coefficient against the sentence finds it.

794. A data table can report more gold medals than the events that were held: 2505964's Table 6 gives `10` gold in
     `5` table-tennis events for 2024 and `6` gold in `4` events for 1996 and 2000, with row sums that reconcile,
     so the cells are consistent with each other and impossible in the sport - the Poisson fit built on that column
     then reports the event count as insignificant.

795. An ordinal scale can be published and then abandoned inside the same section: 2505964 declares
     `0, Unable to win a medal / 1, Win a bronze medal / 2, Win a silver medal / 3, Win a gold medal` with
     `ϵ ∈[0, 3]`, then reports 1.33 and 1.67 as capabilities, averages them over Games and events, and sets `ϵ = 0`
     "for convenience", which removes the only term that could carry a coach's variation.

796. A stated average can match neither of its own operands: 2505964 prints `PAmerica,2008|c = 2` and
     `PAmerica,2012|c = 1.33, indicating ... an average of 1.16 across two Olympics`, where the mean of the two
     printed values is 1.665 and 1.16 is not derivable from any pair of numbers in the chapter.

797. A bullet list of "advantages" can describe a specification the equation does not contain: 2505964's model is
     `Yi = β0 + β1·X1i + β2·X2i + β3·X3i + ϵi` with X1 a host dummy and no product term, and the advantages say
     `The interaction term can capture the performance differences due to the main effects`.

798. A figure caption and a table caption can swap sides, so the data sits under the diagram's name: 2505964 opens a
     block with `Figure 12: The Process of Poisson Regression` and then lists the swimming rows
     `Year Gold_swim ... 1964 45 8 8 61 18.0`, answering with `Table 3: Olympic Swimming Medal Data` in the next
     block, and the flowchart named in the caption prints nowhere.

799. A prose cross-reference can name a table number that is not the table on the page: 2505964's robustness page
     prints Table 5 and the sentence above it says `Table 2 summarizes`.

800. A chapter's own quality metrics can exist only as ink on leaves that are images: 2507817's R², MAE and RMSE
     equations plus Tables 3-6 and Figures 6-8 sit on pages 10 and 11, each one full-page `BI /W 1654 /H 2339` inline
     image with no text layer and no layout block, so the block spans step over them (`129 [9, 12]`) and a text-layer
     reader goes from predictor importances straight to a residual test.

801. Equation numbering can start at (0) with an orphan carried in from the previous chapter, and the prose can cite the
     next number while printing the previous one: 2507817 opens page 6 with `x' = (x - x-bar)/SD` labelled (0), then says
     `ARIMA (p, d, q) can be expressed as equation (2)` over an equation printed as (1) - and (1) is ARMA, with no
     differencing term.

802. A table titled "Top 10" can list nine distinct rows with one country repeated: 2507817's Table 5 gives GBR twice at
     `26` among 51, 34, 29, 28, 26, 26, 20, 19, 15, 15, under a column header printed `old medals`; Table 6 prints
     eleven country columns under the same "Top 10" title.

803. A confidence interval can be widened by a whole unit against its own two printed factors: 2507817 states the
     total-medal interval as `y +/- 15` where `1.993 x 7.123 = 14.20`, while the gold pair rounds correctly
     (`2.404 x 2.908 = 6.99` to `7`).

804. A standard-error column can be the standard-deviation column copied to the last digit: 2507817's Table 8 gives
     SE(y) = `2.908` and `7.123`, the two SDs in Table 7, which no estimate of a mean can be.

805. A conclusion can assert a fit the same page contradicts: 2507817 writes `R² of both models is very close to 1` on
     page 11 beside its own cross-validation values `0.710` and `0.784`.

806. Coefficients can carry the opposite sign to every gloss that motivates them: 2507817 fits `ka -0.012` and
     `ke -0.068` at `p < 0.01` after four paragraphs arguing that more athletes and more events raise the probability of
     a medal, and never remarks on the reversal.

807. An evaluation table can duplicate one metric into another and define the first one wrongly: 2507817's Table 10
     prints `Recall 0.841` equal to `Accuracy 0.841`, while its confusion matrix gives 1029/1402 = 0.734 (0.883 with the
     labels swapped), its F1 is 0.839 against 0.8445 from its own precision and recall, and Accuracy is defined as
     `The proportion of positive samples to the total samples`.

808. A metric table can be welded into the sentence that announces it, so it has no caption of its own: 2507817's
     Table 10 arrives as `the classification evaluation metrics of the model are calculated as shown in the table below
     Table 10 Classification Evaluation Index Accuracy Recall Precision F1 0.841 0.841 0.848 0.839`, one block.

809. A visible QR watermark and an invisible text stamp can coexist on the same leaf: 2507817 carries 688 half-opacity
     crimson vector cells (`fill rgb(0.75, 0, 0.25)`, `ca 0.5`) in a 140 pt square at the bottom right of every page,
     plus the 687-token `m` run at fill alpha zero, so the page has 2,065 layout tokens that are not prose and 688 paths
     that are not drawings of content.

810. A chapter can begin mid-sentence because its own opening leaf is a photograph: 2510006's leaves 6 and 7 are
     each one `BI /W 1700 /H 2200` inline bitmap with zero text objects and zero paths, so the printed heading `3`
     and the whole assumptions list the record calls `assumptions` exist only as ink and the text layer resumes at
     `participate in the previous Games.`

811. A `read-figure` job can be filed on the one group that prints no exhibit while the figure it reads is on a raster
     leaf inside the next group's span: 2510006's group 6 (blocks 160-166) builds the 6x6 table and shows nothing,
     Figure 20 sits on leaf 18, and leaf 18 falls inside block `167 [17, 19]`, which the record files under group 7,
     so the reading and the prose that performs it are both ink the owning group never reaches.

812. Two different rules can share one symbol, one threshold and two coefficient counts: 2510006 defines `a^i_j` as
     predicted gold medals from `(-10, -4, 2, 8, 14, 20)/30` on leaf 8 and as predicted events participated from
     `(-8, -5, -2, 1, 4, 7, 10)/7` on leaf 11, under the same `|r| < 0.5` / `|r| >= 0.5` branch, with neither
     weight vector ever derived.

813. A forecast can be exact at both stages and mistranscribed in the addition: 2510006 prints old events
     `53.64, 51.43, 31.56, 136.63` and new events `0.937, 0.735, 0.706, 2.378`, both summing exactly, then prints
     bronze `32.37` where `31.56 + 0.706 = 32.266`, so its three colours sum to `139.10` against the `139` in the
     same sentence while the two totals do agree at `139.01`.

814. A gloss can quote a number its own printed rule cannot produce: 2510006 says `Lang Ping's contributions ... are
     respectively 0.75 medal points ... and 0.5 medal points` where Table 6 gives China `t = 3/2` and `m = 1`, which
     the chapter's own `(3g + 2s + b)/2` makes 1.5, so reaching 0.75 needs a divisor of 2 that no formula states.

815. A stacked fraction in a table cell can vanish into two integers for any text-layer reader: 2510006's Table 6
     prints `t` as `3/2`, `1/2` and `9/2`, so an extraction reports `3`, `1`, `9` and the halves disappear, which
     also breaks the one arithmetic in the chapter that otherwise reproduces exactly (all four P values from
     `P = 1 - alpha`).

816. A trend sentence can contradict the table printed under it: 2510006 writes `it is clear that the host country's
     medal count, both total and gold, has generally increased` over yearly host hauls of
     `9, 6, 4, 8, 7, 0, 0, 4, 3, 10, 7`, whose peak is 1984 and which is zero twice.

817. A figure's axis categories can be renamed away from the categories the text defines, leaving the matrix
     unmappable to its own `xij`: 2510006 defines `Water Sports, Ball Sports, Athletics, Technical Sports, Combat
     Sports, and Racing Sports` and Figure 20 is labelled `Ball Sports, Track & Field, Aquatic Sports, Gymnastics &
     Aerobics, Racquet & Rowing, Martial Arts`, so the pair the prose calls weakest has no printed counterpart.

818. A table caption can ship as its placeholder on the table the whole argument rests on: 2510006 prints
     `Table 5: Table Title`.

819. Caption side can be inconsistent inside one chapter with no rule to recover it: 2510006 sets Table 2 above its
     grid and Tables 3, 4, 5, 6 and 7 below theirs, while all eighteen figures are captioned below.

820. The invisible stamp can eat the one formula that carries the chapter's headline number: 2510006's weighted
     increase prints in the text layer as `Weighted Increase : Tboost = m m m m ... + ... + mt+nt m m m`, because
     the formula and 687 stamp glyphs share blocks 101 and 102.

821. A sensitivity table can show the branch firing and be read as a finding instead of as the rule: 2510006's
     Table 9 prints `USA 139 139 139 139 139` and `RUS 60 60 60 60 60` flat against `CHN 96 94 87 83 77` falling,
     exactly what a `0.5` cut produces, and the prose calls the flat rows `very stable`; the same table also prints
     USA gold `55` where the model's own combination gives `54.57`.

822. A captionless exhibit can be filed under a table number that names a different exhibit: 2510185's record calls
     the gold-interval grid printed inside flowchart block 76 `Table 6`, while the printed `Table 6` is the model
     performance table on raster leaf 10, and the block-76 grid is really Table 8's gold columns at two decimals -
     `43.47 55.22`, `30.84 42.18`, `13.40 28.54`, `11.28 23.06`, `10.66 32.53`.

823. A chapter's model-comparison evidence can live only in a photograph of a page: 2510185's leaf 10 carries Figure 6,
     Table 6 and two paragraphs on 5-fold cross-validation, and the strings `Performance Evaluation`, `5-fold
     cross-valid` and `Unlike medal ranking` return no block in the layout at all.

824. An independence declaration can be contradicted by the digits it defends: 2510185 writes `the Total prediction
     interval is not determined by the intervals for the three medal categories` and then prints Total bounds whose
     gap to their own three components is a whole number of medals in nine of thirty cases (`+6.0`, `+11.0`, `+10.0`,
     `-4.0`, `-5.0`, `-8.0`, `-10.0`), which is hand-editing, not separate estimation.

825. A `Total` column can carry a different quantity from the one its header names: 2510185's Table 13 prints
     `Gold Silver Bronze Total` as `0 0 0 2.41` and `0 0 0 3.85` - four of five rows total a nonzero figure on zero
     medals won - because the column is Table 14's predicted continuous total, and all five values recur verbatim in
     Table 14.

826. A results table can duplicate one event's rows under another event's name: 2510185's Table 14 gives China's
     `Men's swimming` the `Men's gymnastics` values byte for byte in both `G_C` variants (`0 0.50 1.33 0.50 2.41` and
     `1 1.05 1.31 1.33 3.85`), which leaves only two distinct China entries where four rows print.

827. A row sum and its delta can disagree in opposite directions, so the table proves neither: 2510185's Table 7
     prints Australia `17 15 17` as `50` with a `-3` delta that matches the wrong total (`50 - 53`), and prints the
     United States `+11` where `137 - 127 = +10`, the one row whose own numbers are consistent.

828. A chapter's own headings can be filed on blocks the record assigns to other chapters: 2510185 types zero
     `heading` blocks and welds `3` onto `data-preprocessing` block 51, `3.4` onto results 94, `3.5` onto 99, `4` and
     `4.1` onto 129, `4.3` and `4.3.1` onto 140, so five of its twenty titles are unreachable from its own rows and one
     (`3.4.1`) is ink on a raster leaf inside another chapter's block span.

829. An index can be defined, weighted by unassigned symbols and never computed, while its recommendations are
     asserted from history in the shape of its output: 2510185's `(4)` prints `EPI = w1 x Total_trend + w2 x
     Total_space + w3 x AAPI` and no sentence ever gives or fits a weight, `(6)` leaves its own `Total` denominator
     undefined, and the three country lists that follow carry no EPI value.

830. A feature importance can be quoted as a share of an undefined whole: 2510185 prints `the feature importance of
     "Great Coach" was 0.288` and then `contributing 28.8% to overall performance` with no denominator, no
     normalisation and no sentence saying what `overall performance` counts.

831. An extraction can cut a paper at printed line boundaries, so the record's block count is a line count and
     every per-block average is deflated: 2510862's 121 blocks hold 1,935 real words at 16.0 a block, 103 of them
     19 words or shorter, 102 without terminal punctuation, and the splits fall inside words (`110` ends `Light-`,
     `111` begins `GBM`), so a 25-block group is about eight sentences.

832. A record's `select`-to-`derive` boundary can fall inside a subsection when the chapter is reordered by the
     extraction rather than by the author: 2510862's group 2 ends on `to avoid overfitting.` and group 3 opens
     `By minimising this objective function, LightGBM optimises the parameters of the`, putting the cut in the
     middle of the first base model's description.

833. A chapter's headline number, three of its equations and two of its headings can exist only as ink on a leaf
     the layout steps over: 2510862's block `148 [8, 10]` jumps from `Equation 4 Equation 5` to `R2 = 1 − (7)`,
     and raster leaf 9 holds `(4)`-`(6)`, `5.2`, `5.2.1` and Figure 4's `USA 56 41 36 133`, so a text-only reader
     loses the paper's central prediction and sees an equation series with a hole where none exists.

834. Two base learners can be defined by one closed form and then weighted as if they were different models:
     2510862 prints `(4) f1(x_i) = y_i^LGBM = Σ_t f_t(x_i)` and `(5) f3(x_i) = y_i^XGBoost =
     Σ_t f_t(x_i)`, then ensembles all four learners in `(6)` with separate coefficients.

835. One formula can carry two numbers at once, printed on the page rather than implied by extraction: 2510862's
     block 234 reads `In our data, the PSM model is:Equation 14 (13)` in front of the logistic propensity score,
     and `(14)` then prints again against the DID model two leaves later.

836. A displayed regression can print a summation sign with nothing to sum, subscript half its parameters and
     write a regressor as one symbol the gloss defines as a product: 2510862's `(14)` puts a bare `∑` before
     `β2 · Control`, sets `β0`-`β3` on the baseline while `r_i` and `ε_it` on the same
     line are lowered, and prints `DID` alone where the next paragraph says `DID is a cross-multiplier term
     r_i * time`.

837. A model-comparison table can be arithmetically impossible while every later claim rests on it: 2510862's
     `R2`/`MSE` columns give `Var(y) = MSE/(1-R2)` as 2.41, 2.30, 2.64, 2.44 and 2.67 for five models scored on one
     response, a 16% spread implying a target whose standard deviation is 1.5 medals.

838. A MAPE cell can contradict the MSE cell beside it by two orders of magnitude: 2510862 prints `MAPE 0.30` for a
     model with `MSE 0.32`, i.e. an RMSE of 0.57 medal, which requires an average country total above 189 where
     the same document prints gold counts of 40, 40, 18, 20, 16 and 15.

839. The only genuinely tabular object can be captioned as a figure while its own introducing sentence calls it a
     table, leaving the document with no table numbering to cite: 2510862 prints `The calculation results are
     shown in Table:` followed by `Figure 5: Model evaluation results` in one block, and the paper's only numbered
     table is `Table 1` two chapters earlier.

840. A before/after comparison figure can draw its two panels at different magnifications, so the comparison the
     caption invites cannot be made from the image: 2510862's Figure 15 puts the before-matching panel on a
     `Probability Density` axis of `2.00` and the after-matching panel on `5`, over different propensity-score
     ranges, and its after panel's range excludes treated scores the before panel shows.

841. A method can be specified to the last test and never estimated, with the gap stated as a conditional:
     2510862 names the treatment group, the control group, the propensity model in `(13)`, nearest-neighbour
     matching, a parallel-trend test and the interaction in `(14)`, then writes `If significant and positive, it
     indicates that great coaching has a positive effect`, and no coefficient, standard error, p-value or sample
     size appears in 121 blocks (`significan` twice, both inside that conditional).

842. A Dirichlet-Multinomial parameter can be defined as a probability vector with no normalising
     denominator: 2513314's `(5)` reads `θ_i = φ_i exp(x_i^T β_i)` and the prose calls it the vector of
     multinomial probabilities, but nothing anywhere divides by `Σ_j φ_j exp(x_j^T β_i)`, so each country's
     parameter is an arbitrary positive number and the likelihood in `(6)` is not the model the section names.

843. An alpha-0 stamp can be the majority of a chapter's token count and swamp every per-block average: 2513314
     carries 1,374 `m` glyphs against 1,068 real words, 56.3% of tokens, all of them in the first three groups,
     which is why two blocks are filed at 749 and 319 words for 62 and 19 printed ones.

844. A record chapter can be two islands with its own results section printed between them: 2513314's groups 1-3
     sit on leaves 7-10 and groups 4-6 on leaves 13-14, and 41 `results` blocks (79-119) hold the whole of
     Sections 5.3-5.5, so 67 of the 96 blocks overlapping the declared range belong to other chapters.

845. A table can be captioned, cited twice, quoted cell by cell and exist in no layout block at all: 2513314's
     `Table 4` prints 32 coefficient rows with 128 numbers on leaf 13, blocks 118 and 119 quote five of its cells
     exactly, and no block on any leaf holds a row of it - so the section's recommendation rests on evidence the
     text layer does not contain.

846. Captions can print above their objects throughout, which makes a caption-first pairing rule correct for the
     first time in the lane and turns the usual weld into a non-defect: 2513314's Tables 2-4 and Figure 4 all set
     their captions above, so the layout's caption-first blocks are faithful rather than scrambled.

847. A model-comparison table can be internally impossible in one target and exact in the other, which is what
     distinguishes rescaling from estimation: 2513314's `Table 2` prints `RMSE` and `√MSE` that disagree by
     0.01-0.07 for all six All-Medals rows and agree to the digit for all six Gold rows, so the implied residual
     variance moves 45% and 34% inside fixed-RMSE rows.

848. One table's confidence intervals can be 0.86 to 3.30 standard errors wide, and three of them off-centre:
     2513314's `Table 4` prints 8 of 32 half-widths away from 1.96 SE, and US `X3`, UK `X1` and France `X1` do
     not even straddle their own point estimate - in the table the paper's third task is built on.

849. A published interval can carry two decimal points so that its lower bound exceeds its upper bound: 2513314's
     `Table 3` prints Haiti as `[0.2112, 0.0.2698]` on the page.

850. Figure numbering can have a hole while table numbering does not: 2513314 prints `Figure 1`, `2`, `3`, `4` and
     `6` across 22 leaves with no `Figure 5` anywhere, and no block or sentence ever cites the missing number.

851. A symbol can be introduced in one equation, given a value, and never listed or used again: 2513314's `τ`
     appears once inside `(2)` as `Σ_β = τ² I_p` with `τ² = 1`, is absent from the seven-symbol `Table 1` on leaf
     5, and never returns.

852. A chapter's central model can exist only as a table row while every numbered display belongs to a
     different model: 2514362's mixed-effects negative-binomial regression - the model Section 4.1 is named after
     - appears only inside `Table 1`, together with its five priors and two random effects, while all 21
     numbered displays are the zero-inflated and entropy machinery of Sections 4.2 and 5.

853. A record chapter can lose four of its own section titles to neighbouring chapters, one title per seam:
     2514362's `4.2`+`4.2.1` print in results block 73, `5`+`5.1` in sensitivity block 120, `4.1.3` at the tail of
     notation block 58 (the Table 1 block), and the document's own `4` at the tail of an `assumptions` block that
     spans `[5, 7]`.

854. A chapter can end on a heading it does not own: 2514362's last block `104` closes on the bare number
     `4.2.3`, whose title is the next chapter's block `105` and whose finding is block `106`.

855. One paper can weight the same history twice, normalised in one place and unnormalised in the other:
     2514362's `History^w` divides by `Σ e^{−λ(k−1)}` over five lags, while the chapter's own `Athletes^w` is
     `Σ_{k=1}^{3} e^{−0.5k} N_{i,t−4k}` with no denominator, so its weights total 1.1975 and the covariate is 20%
     larger than the counts it sums.

856. A tuned hyperparameter can be written back into a feature definition and disappear as an estimate: 2514362
     grid-searches `λ` over three values under one equation number, fixes `λ = 0.6`, and thereafter prints it as
     a constant inside `History^w` in `Table 1`.

857. A conditional probability can be used in an entropy formula and defined nowhere: 2514362 defines
     `P_progress` in `(15)` and its complement in `(16)`, then builds `(18)` from `P_progress|x` and
     `P_non-progress|x`, which appear in no equation, gloss or table.

858. A quoted posterior can sit three prior standard deviations from its own prior mean in one coefficient and
     half a standard deviation in another, which is the priors' doing rather than the data's: 2514362 reports
     `β2 = 0.3` against `N(0, 0.1)` and `β1 = 0.85` against `N(0.8, 0.1)`.

859. A model's reported variance component can belong to a model the chapter did not build: 2514362's results
     quote `σ_u = 0.2` for country heterogeneity, a parameter of the mixed model in `Table 1`, while the
     zero-inflated equations `(2)`-`(4)` that the chapter derives carry no random effect at all.

860. A `display`-typed block can be an invisible stamp and nothing else: 2514362's block `57` is 687 alpha-0 `m`
     glyphs at 1.38 pt, and it is the chapter's only `display` block, so the type fires once and never on an
     equation.

861. A figure caption can disagree with the title printed inside its own image: 2514362's `Figure 5: Prediction
     vs. Actual` sits over `Predicted vs. Actual Gold Medal (2012-2024)` and `Figure 6: Gold Medal Prediction
     Analysis` over `Olympic Gold Medal Predictions Analysis (2012-2024 Games)`, because every figure is a pasted
     bitmap carrying its own text.

862. In-image panel titles can be filed as the caption of the table beneath them: 2514362's `Top 15 Gold Medal
     Table Predictions` and `Top 15 Total Medal Table Predictions` are in-image text inside `Figure 7`, and the
     layout files them as block `65`, immediately before `Table 2`'s own caption in block `66`.

863. Two side-by-side captions can arrive in the reverse of their printed order: 2514362 prints `Figure 8`'s
     caption left and `Figure 9`'s right on leaf 10, while the layout files Figure 9 as block `68` and Figure 8
     as `69`.

864. A QR panel can physically overprint body text rather than sit beside it: 2514362 prints a magenta QR block
     at bottom right on leaves 8 and 14, and on leaf 14 it covers the last three lines of the paragraph that
     opens `From Figure 16 we can find out: ...`.

## Protocol actually followed

- `python -I -X utf8 tmp/c_prep.py <pid>` dumps the chapter and renders its pages.
- `make_review_proxy.py --max-width 1000 --max-bytes 450000`, one page per Read, default
  detail, never batched. `--crop L,T,R,B` on the original raster whenever a subscript,
  superscript or exponent is in doubt (class 44).
- For long chapters the page reading is delegated to a read-only subagent that reads every
  page in the span and returns a textual audit; the root agent writes the package from that
  audit and never summarises a page it has not seen.
- `python -I -X utf8 -c "import sys;sys.path.insert(0,'tmp');import check_c_distill as c;c.main()"`
  validates every package against its record: five sections, job sequence, group count, table
  row count.
