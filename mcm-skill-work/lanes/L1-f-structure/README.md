# L1 — type F body-structure lane (hand-coded paragraph jobs)

Scope: the 48 eligible type-F papers only, in queue order (year, path, filename).
Everything else in the corpus belongs to the other session and is read-only here.

## Hard boundaries

Writes stay inside this directory. Never written from here:

- `artifacts/**` (the other session owns it)
- `tmp/para-taxonomy.md`
- `~/.claude/skills/mcm-icm-master-skill/**`
- any A–E paper

Reads: `artifacts/corpus/manifest.jsonl`, `artifacts/language-units/P-F-*.json`,
`artifacts/papers/P-F-*/rendered/*.png`, and the source PDFs under
`F:\MCM\MCM-ICM-master` (path taken from the manifest).

## Method, one paper at a time

1. `tools/para_extract.py layout <pid>` — rebuild paragraph boundaries from PDF
   text geometry: modal body font size, modal left margin, modal line spacing, and
   the first-line indent. Writes `layout/<pid>.json`.
2. `tools/dump_paper.py <pid>` — compact reading list for hand reading.
3. Read every body chapter. Assign one job per block from the shared taxonomy.
4. `tools/record.py <pid>` — validates the vocabulary, fills each job's verbatim
   opening sentence from the layout, appends `jobs-f.jsonl`, writes `notes/<pid>.md`.
5. One visual check per paper: render the measured page, count paragraphs on the
   image, compare with the measured block count.

No batch classifier. No script ever decides a job. The scripts only measure
geometry and validate what was written by hand.

## Taxonomy

Snapshot of `tmp/para-taxonomy.md` at lane start: sha256
`03ab19a2db5ee7bf3fd59ba2cd177c03cf1883215cc1b253234e5f462bd87550`
(13 jobs: route, define, source, select, derive, compute, read-figure, compare,
check, limit, mechanism, interpret, handoff). If the other session edits it, the
hash mismatch is recorded in the paper note and the record still carries the
verbatim opening sentence, so a re-code stays cheap.

Two codes are marked outside the shared table and are always reported in `ext`:

- `ext:context` — background/context paragraph that neither routes a task nor
  defines a quantity. Type-F papers spend 2–3 blocks per introduction on this and
  the shared table has no job for it.
- `ext:claim` — a bare strength/deliverable claim (numbered conclusion items).
  `interpret` is for reading a computed quantity back; these items read nothing.

## Blocks, groups, and what the counts mean

- `blocks` — measured paragraph numbers. A **group** is one job; a group holds
  several numbers only when the measurement split one block (a heading detached
  from its body, or table rows). `literal_blocks` counts paragraphs, `group_count`
  counts coded blocks. `len(jobs) == len(blocks) == group_count`.
- `stored_count` — the corpus value (`len(paragraph_functions)`), kept only for
  cross-check. **It is not used to size anything.**

Measured against the stored corpus and the reason it cannot be used to size:

| paper | stored | literal | why |
| --- | --- | --- | --- |
| 2016-43181 | 73 blocks total | 106 body paragraphs | every stored string is `"<chapter> paragraph N: context -> evidence -> unresolved need -> paper response"`, i.e. one template repeated per block |
| 2016-44348 | 43 | — | stored strings are copy-edit marks (`the stray comma`, `the dropped letter`, `the spaced url`), not paragraph functions |
| 2025-2517199 | 70 | — | same template as 2016-43181 |
| corpus-wide | 36–50 per paper for 2016–2020, then 99–335 for 2020–2025 | — | the extraction method changed mid-corpus; the early records keep only part of the body |

So the lane's own verification is: `len(jobs) == group_count`, every block number
exists in the measured layout, every job has a verbatim opening sentence from the
same layout, and the measured page count matches the rendered page on one page per
paper. The stored counts are reported as a discrepancy column, never as a target.

## Reproducibility

`para_extract.py` is deterministic: same PDF, same numbers. Re-running it on a
coded paper must reproduce `layout/<pid>.json` byte-for-byte; if a rule changes,
every paper already coded is re-measured and the diff is written into its note.

### Rule change 1 — line-spacing floor (after paper 2)

The modal line spacing was the median of all gaps between body-sized lines. On
pages with inline math, superscripts sit on their own short line and produce a
half-line gap, so the median collapsed (paper 3, page 17: median 7.16 pt against
a real 14.4 pt) and `gap > 1.25 * spacing` became true for every line — whole
pages were split one line per block.

Fix: gaps below `0.8 * body_size` do not vote for the spacing.

Re-measurement of the papers coded before the change:

| paper | before | after | effect |
| --- | --- | --- | --- |
| 2016-43181 | 142 paragraphs | 142 | none, layout byte-identical |
| 2016-44348 | 230 paragraphs | 212 | blocks 116+ renumbered and merged; chapter 5-12 groups re-derived against the new layout, 122 → 129 groups |
| 2016-46634 | 247 paragraphs (first measurement) | 222 | coded after the fix |

## Visual checks

One page per paper, rendered page versus measured block count (the paper's own
footer numbering can be one lower than the index used here, because index 1 is
the summary sheet):

| paper | layout page | measured blocks on page | blocks counted on the render | pass |
| --- | --- | --- | --- | --- |
| 2016-43181 | 3 | 9 | 9 | yes |
| 2016-44348 | 3 | 11 | 11 | yes |
| 2016-46634 | 4 (footer "page 3 of 22") | 11 | 11 | yes |
| 2017-64486 | 22 (footer "Page 21 of 33") | 10 | 11 | yes (91%) — the printed "9 Migration Plan Analysis" heading is merged into the tail of block 233; the 8.2 and 9.1 headings are their own blocks (231, 235) |
| 2017-68940 | 13 (footer "Page 13 of 52") | 7 | 7 | yes |
| 2017-72197 | 23 (footer "20") | 4 paragraphs | 4 paragraphs | yes — the "J. CONCLUSIONS" heading is glued into block 119 on the previous page |
| 2017-72283 | 8 (footer "Page 7 of 24") | 4 paragraphs | 4 paragraphs | yes — the "2.4 Validation of the Model" heading is glued into block 89 |
| 2018-83744 | 15 (footer "9") | 10 blocks | 9 paragraph-level units | yes (90%) — blocks 137/138 are one paragraph split at the inline-math line; the running header (136) and the 2.6 heading (143) count as their own measured blocks |
| 2018-87280 | 14 (footer "Page 13 of 20") | 11 blocks, 9 of them prose | 9 prose paragraphs, 4 headings | yes — prose 9/9 exact; of the four headings only 5.3.1 (119) and 5.3.2 (121) are own blocks, 5.2 and 5.3 are glued into the tails of 115 and 118 |
| 2018-88508 | 15 (footer "Page 14 of 29") | 9 blocks | 11 visible units (6 prose, 3 displays, 1 caption, 1 heading) | yes — prose 6/6 exact; block 143 merges eq.(18) with "The relationship ..." and "Among them i represent ...", and block 148 merges the Fig.10 caption with the 4.3 heading and the "Unlike individual ..." paragraph |
| 2018-93036 | 20 (footer "Page 14 of 27") | 7 blocks | 7 text units (5 prose, 1 heading, 1 caption) plus one chart and one table body | yes — exact; the Fig.7 raster and the five Table 5 rows are images/rules, not measured paragraphs, so both sides count 7 |
| 2019-1904381 | 9 (footer "Page 8 of 27") | 8 blocks | 8 text units (2 prose, 2 numbered items of 2 lines each, 2 further prose, 2 numbered items of 1 line) plus two chart groups | yes — exact; block 87 merges the tail of item 2 with the "(a)(b) Figure 3: LM Curve shifts" caption, and the charts themselves carry no measured paragraph |
| 2019-1905127 | 12 (footer "Page 10 of 24") | 9 blocks | 9 text units (8 prose paragraphs, 1 heading) plus four equation displays | yes — exact; the displays sit between blocks, and blocks 84-86 are the three prose paragraphs that the inline math split one line at a time, so they still map 1:1 onto paragraphs |
| 2019-1916375 | 15 (footer "Page 14 of 22") | 11 blocks | 11 text units (2 prose, 4 headings, 1 "Assumptions:" label, 2 bullets, 1 prose plus the Fig.5 caption) | yes — exact; block 141/142 is one bullet split at the inline ε line, and blocks 145 and 147 each merge a heading with the paragraph that follows it |
| 2019-1916704 | 17 (footer "Page 15 of 19") | 10 blocks | 10 text units (6 prose, 2 headings, 1 table caption, 1 table body) plus three equation displays and one chart strip | yes — exact; the top paragraph and eqs (44)-(46) belong to block 236 which starts on page 16, and the Table 8 caption (238) and rows (239) are separate measured blocks just as they are separate objects on the page |
| 2020-2005623 | 16 (footer "Page 14 of 21") | 5 blocks start here (135–139) | 6 text units: 3 prose paragraphs, 2 figure captions, plus the tail of block 134 carried over from page 15 | yes — exact; every unit on the page is one measured block, and block 140 is listed as p16-17 only because its caption sits below the QR footer mark, so it starts on page 17 |
| 2020-2006291 | 10 (no printed page number; QR mark only) | 8 blocks (93–100) | 8 units: 1 paragraph split at a word (93 "…so the" / 94 "th calculation method…"), 1 formula+matrix block (95, whose tail also holds the "B7 Religion" label), 4 prose/caption lines (96, 97, 98, 99), 2 table bodies, plus the Table 3 rows carried over from page 9 | yes — exact; the Table 4 and Table 5 bodies are drawn as rules and rows, not measured paragraphs, so the counted units are the same 8 text blocks |
| 2020-2009139 | 9 (footer "Page 7 of 21") | 19 blocks start here (112–130) | 11 paragraph-level units: 4 numbered standards, the "5 Site selection" and "5.1 Countries in responsibility" headings, 2 prose paragraphs, 3 numbered responsibility factors, plus Table 4 carried over from page 8 (caption plus 11 country rows held in block 111) | yes — exact at paragraph level; each numbered item is split one printed line per block (112/113, 114/115, 117/118+119, 124/125, 126/127, 128/129/130), so 19 measured blocks are 11 units and Table 4's rows are a ruled table, not measured paragraphs |
| 2020-2013233 | 10 (footer "9 / 21") | 15 blocks start here (99–113) | 15 units: 5 paragraphs (education tail, medical, grain, pension, housing), 1 heading glued into block 103's tail, 1 PCA lead, 5 numbered indicators, 1 PCA explanation with the component-system display, 3 numbered conditions | yes — exact; the only merges are the "5.1.2 Model building" heading inside 103 and conditions (1)/(2) split across 111/112, and the display sits inside 110–111 as one measured block pair |
| 2021-2102185 | 10 (footer "Page 8 of 21") | 8 blocks start here (89–96) | 13 text units: the "4.1.5 Internationalization index" heading and formula (5) (both inside 88's tail, since 88 starts on page 9), paragraph 89, paragraph 90, the "4.2 Using TOPSIS-like algorithm" and "4.2.1 Crosswise contrast model" headings (both inside 90's tail), paragraph 91, the "First of all, we establish a matrix X" lead with matrix (6) in 92, paragraph 93, formula (7) in 94, matrix (8) with its lead sentence in 95, paragraph 96 | yes at paragraph level — 8 measured blocks are 6 paragraphs plus three displays and four headings, all of the headings and displays merged into the paragraph that introduces them |
| 2020-2013772 | 5 (footer "Page 4 of 22") | 13 blocks start here (42–54) | 8 paragraph-level units: the tail of assumption 4's bullet (42–43), assumption 5's bullet (44–47), assumption 6's bullet (48–50), the "3 Glossary and Symbols" heading with its 14-row table (both inside 50's tail), the "4 Models for Planning" heading (51), the "4.1 Number of People at Risk" heading (52), paragraph 53, paragraph 54 | yes at paragraph level — 13 measured blocks are 8 units, because every bullet is split one printed line per block; chapter 3 has no measured block of its own at all, its heading and its whole table live in 50's tail |
| 2020-2013733 | 14 (footer "Page 14 of 24") | 7 blocks start here (107–113) | 15 text units: 107 paragraph plus the "3.4.5 Employment" heading in its tail, 1 paragraph over 108–110, 3 equation displays (K1, K2, β4), the AHP paragraph, the Index equation, "Then we can use the model …" paragraph, the bold "Why will the selected area accept EDPs and who will undertake the costs?", "Some governments are unwilling …" paragraph, the "3.5 Charging Model" and "3.5.1 Basic idea" headings, 2 paragraphs of 113 | yes at block level, no at paragraph level — block 112 merges eleven visual units (2 equation tails, 1 display, 1 paragraph, 1 equation, 2 paragraphs, a bold question and 2 headings) because the layout rule treated the heading sizes and the bold line as body text; 7 measured blocks over 15 visual units |
| 2021-2103649 | 18 (footer "Page 18 of 25") | 25 blocks start here (206–230) | 13 text units: 3 vision bullets (2 lines each), 3 vision-rationale paragraphs (6-7 lines each), the "6.3 Treatment Plan" heading (226), the 6.3 routing paragraph (227, whose tail also holds the "6.3.1 Declaration for Our Policies" and "1. Short-term policies" headings), the short-term rationale paragraph (228), the "Reduce the cost of education for the poor" bullet (229), the policy body (230) | yes at paragraph level — 25 measured blocks are 13 units, because blocks 206–225 are six paragraphs split one printed line per block (bullet + body + bullet + body + bullet + body); block 227 merges two headings into a paragraph tail, and the QR watermark covers the last line of 230 |
| 2021-2106074 | 4 (footer "Page 4 of 25") | 16 blocks start here (22–37) | 12 text units: the Figure 1 structure diagram, the "Figure 1: The structure of our paper" caption with the "2 Assumption and Notation" and "2.1 Assumption" headings (all inside 22), the lead sentence (23), four two-line assumption bullets (24–31), the "2.2 Notation" heading with the table header (inside 32), and six notation rows carried by five blocks (33–37) | yes at unit level — 16 measured blocks are 12 units, because each assumption bullet is split one printed line per block and each table block glues the next symbol onto its row; the caption block 22 holds three separate objects (caption plus two headings) |
| 2021-2109443 | 14 (footer "Page 14 of 25") | 16 blocks start here (149–164) | 11 text units: the tail of the comparison paragraph (149), Table 7 with its title and nine country rows (150), the "We discover the following information:" lead (151), five finding bullets (152–153, 154, 155–156, 157–158, 159–161 with the "5.2 The Ideal Vision" heading in the last one), and three prose paragraphs (162, 163, 164) | yes at unit level — 16 measured blocks are 11 units, because each finding bullet is split one printed line per block and the nine-row table is one measured block |
| 2021-2122374 | 18 (footer "Team # 2122374 / Page 18") | 11 blocks start here (221-231) | 11 text units: the radar chart title (221), its legend (222), the axis label dump in two blocks (223-224), the Figure 10 caption (225), three prose paragraphs (226, 227, 228), the "4.3 Necessary of Policy with GM" heading (229), and two prose paragraphs (230, 231) | yes — exact, 11 measured blocks are 11 units; the axis dump is the only split (223 "pcy 0.8 dgr rmu 0.6 0.4 ad-d grc 0.2 0 ad-c pfe" and 224 "ad-b pou ad-a"), and page 18 also settles a read: block 228 says the four targeted indicators have *small* coefficient of variation, with targets 0.36357355 / 0.54955861 / 71.21904762 / 1.857142857 against Chile 0.114992569 / 0.281632653 / 15.4 / 0.3 |
| 2021-2123945 | 12 (footer "Page 12 of 25") | 7 blocks start here (134-140) | 7 units: the tail of the modulus/angle paragraph carried from page 11 with the "•For Delta S" marker (134), the Delta S paragraph (135), the "In sum" paragraph with the "4.4 Application of 3DVA Model" heading in its tail (136), the lead sentence plus both Figure 4/Figure 5 captions (137), the "concrete modulus and deviation angle" sentence (138), the Table 3 caption with its eight-country body (139), and the first interpretation paragraph (140) | yes — exact, 7 measured blocks are 7 units; block 137 merges a lead sentence, two 3D charts and their two captions into one block, and the page also yields the check the text was missing: the Figure 4 legend prints India (0.47, 0.54, 0.16), which recomputes to modulus 0.734 and 22.9 degrees against Table 3's 0.735 / 23.13 |
| 2022-2204803 | 14 (footer "Page 13 of 22") | 35 blocks start here (123-157) | 7 units: the one paragraph made of block 123 (premise) plus block 124 (division of labour), and six indicator bullets (Civ1 125-131, Civ2 132-137, Eco1 138-142, Eco2 143-149, Eco3 150-154, Eco4 155-159 whose last line falls on page 15) | yes — exact at paragraph level; 35 measured blocks are 7 units because every bullet is split one printed line per block, and the page confirms the Eco1 bullet prints the same two sentences twice ("Capital formation per capita: An increase in per capita income causes an increase in assets held per capita" after the identical opening), a copy-paste duplication the text layer alone could have produced; the "4.1 Funded by Nation" heading sits in block 122's tail |
| 2022-2208238 | 15 (no footer printed on the page) | 24 blocks start here (138-161) | 7 units: the tail of principle 2 (138-140, three printed lines), principle 3 "Third, it is important to establish a sound redistribution system" (141-146), the common-asset premise with the "three different ways out" lead (147-150), the three ✓ ways out (151-153 joint mining, 154-157 UN-held planetary area, 158-160 tender/auction), and the ECSC structure paragraph ending "and get the following structure.[6]" (161) | yes — exact at unit level; 24 measured blocks are 7 units because every bullet is split one printed line per block, and the page also settles two reads: block 161's tail carries the "Figure 11 each takes what he needs" caption in the text layer while the figure area on the rendered page is blank white, and the page carries no printed page number at all, so the page indices in the layout come from the raster order only |
| 2022-2209952 | 22 (footer "Team # 2209952 / Page 21 of 24") | 20 blocks start here (231-250) | 11 units: the tail of the 6.1 rationale carried from page 21, the three 6.1 policies (231-233, 234-235, 236-237), the "6.2 Encourage the Exploitation of Asteroid Resources" heading (238), the 6.2 rationale paragraph as one block (239), the three 6.2 policies (240-242, 243-244, 245-246 whose tail holds the "6.3 Strengthen the Supervision" heading), the 6.3 rationale (247) and the two 6.3 policies (248, 249-250) | yes — exact at unit level; 20 measured blocks are 11 units because every numbered policy is split one printed line per block while the two rationale paragraphs stay whole, and the page also settles the page numbering: the raster index is one ahead of the printed folio (raster 22 prints "Page 21 of 24"), so every layout page in this paper is printed page + 1 |
| 2022-2211240 | 18 (footer "Team # 2211240 / Page 18 of 25") | 32 blocks start here (182-213) | 7 units: the "The initial increase in inequity is largely due to the range of benefits" lead with the bold "Economy" heading glued into its tail (182), the Economy body (183-186), the "Technology" bullet (187-190), the "Ecology" bullet (191-198), the "In the long term, countries move toward greater equity" pivot (199), the "The Law of Diminishing Marginal Utility" bullet (200-203) and the "A redistribution system" bullet (204-213) | yes — exact at unit level; 32 measured blocks are 7 units because every bullet body is split one printed line per block and the lead sentence merges into the next bullet's heading, and the page settles the split I had wrong on first pass: 182 is its own framing unit (the chapter pivot) and the Economy channel starts at 183, so the group had to be cut there |
| 2022-2218577 | 20 (footer "Team # 2218577 / Page 20 of 25") | 6 blocks start here (146-149 and 150-152) | 9 units: three fragments of the level-ratio test whose equation was cut by the line breaker (146), the discrete grey equation x(0)(k)+az(0)(k)=b (147), the whitening equation with its solution (148), the "Finally, we can set k+1 = t" window sentence carrying the "5.3.1" heading (149), the "5.3.1 Let the Capable Work Harder" heading (150), the Figure 11 caption (151), and the "After adding the time factor" reading (152) | yes — exact at unit level; 6 measured blocks are 9 printed units because the level-ratio chain and the two equations are split across blocks 144-148 while the headings and captions stay whole, and the page settles one read: the raster prints "5.3.1 Let the Capable Work Harder" as its own line with the Figure 11 plot below it, so the heading cannot share a group with the caption — the record was split at 150/151 and again at 153/154 after this check, taking the paper from 120 to 123 groups with the block count unchanged at 160 |
| 2022-2220722 | 20 (no header or footer printed on the page) | 22 blocks start here (214-235) | 12 units: the Figure 10 caption with its four-quadrant reading (214-215), the "We recognize that some are extracting benefits from depleted resources" lead (216), seven loss bullets (217-218 environment, 219-220 medical, 221-222 economy, 223-224 distribution, 225 education, 226 gender, 227-228 science and technology), the "While other countries can use resources efficiently" lead with its single mirror bullet (229-231), the "Through the above comparative analysis" lead (232) and the three numbered conclusions (233-235, 236-237, 238) | yes — exact at unit level; 22 measured blocks are 12 units because every bullet and every conclusion item is split one printed line per block, and the page confirms the bullet structure the extraction tore apart (each bullet is a bold label plus one wrapped body line). The page also carries no printed page number and no "Team #" header, so the layout page index is raster order only, and it shows the 0.3154 OE cut line drawn at about OE 0.31 through the plotted points, which matches the text |
| 2022-2224021 | 12 (footer "Team # 2224021 / Page 12") | 8 blocks start here (167-174) | 7 units: the Advancer, Pursuer, Outsider (two blocks) and Others items of the clustering list (167-171), the Figure 7 map with the Figure 8 dendrogram and their captions (172), the Cobb-Douglas equation and elasticity paragraph (173), and the alpha/beta/A estimation paragraph whose tail carries the "5.2 Production Side" heading (174) | yes — exact at unit level; 8 measured blocks are 7 units, and the page settles two reads: the Leader/Advancer/Pursuer/Outsider/Others legend in Figure 7 and the numbered list 2)-5) on the page confirm that the clustering produced five classes, so block 165's "divide the countries into 41 categories" is a typo for five (the footnote inside 166 explains the fifth class); the page also prints a value the text layer dropped — "Take the United States as example, we derive that A-hat = 7.42" |
| 2023-2305794 | 12 (footer "Team 2305794 / Page 10") | 15 blocks (137-151) | 13 units: the consistency-test sentence with eq (8) and eq (9) inline, the RI = 1.26 / CR = 0.044 paragraph, the "(4)Calculate to obtain weights" heading with its weight sentence, the Minimum Relative Information Entropy bullet, the min-sum display with its constraints, the Lagrange Multiplier paragraph with eq (10), "In the following figures", "The main factor that matters most", and "Through rigorous calculations" | yes — block 139 starts mid-sentence on the page because eq (8) is cut out of the running text, so 15 measured blocks are 13 printed units; the page confirms CR = 0.044 < 0.1 with RI = 1.26 for n = 6, the six factor weights 0.475/0.257/0.135/0.068/0.033/0.033, and Switzerland 0.72, which is the only country score printed in the paper |
| 2023-2311258 | 13 (footer "Team # 2311258 / Page 13 of 25") | 29 blocks (124-152) | 11 units: the adjusted-loss-curve paragraph with eq (10), the resource-dependence bullet with eq (11), the diminishing-pressure paragraph, the subsidy bullet, the subsidy-pool paragraph with eq (12) and the "5.1.3 Game start" heading, "When GGDP is not used" with eq (13), "With the GGDP" with eq (14), "For any country" with eq (15) | yes at unit level, no at block level — 29 measured blocks are 11 printed units because three bullets and four display equations were cut one printed line per block (blocks 127-143 average 11 words). The page settles one read: the resource-dependence bullet is a single printed paragraph that carries the pressure definition and eq (11), so blocks 127-132 are one group with job derive rather than a limit group plus a derive group; it also confirms eq (14) prints F3 = -Ln(t) - Rs*p, i.e. the supporters pay the subsidy, so the printed condition F1 < F3 in (15) cannot hold and the game result in Table 2 has no consistent payoff algebra behind it |
| 2023-2311517 | 12 (footer "Team # 2311517 / Page 12 of 25") | 9 blocks (125-133) | 8 units: the tail line "than it was in the 1960s", the 5.3.2 heading with the correlation paragraph, the Figure 8 matrix with its caption, the 5.3.3 heading, "In our evaluation system", "Based on this method" with the four printed regression equations, "We conducted multiple regression analysis", and Table 3 | yes — 9 blocks are 8 units, the only split being the two headings that ride in the tails of 126 and 128. The page settles three reads: Figure 8 is an 11x11 correlation matrix (GHGE, WT, pH, OHC, SSTA, SI, IB, LI, BD, ND, SC) so the "11 secondary indicators" count is right; block 131 prints only four equations although the text announces five variables, so the sea-level equation exists only as a row of Table 3; and Table 3 confirms beta1 = -5.87E-15 for GHGE against beta2 = -0.054 for %DIF, i.e. GDP has no measurable effect on emissions in the paper's own regression |
| 2023-2315018 | 15 (footer 'Team # 2315018 / Page 15 of 24') | 5 blocks start here (152-156) | 7 text units: the eq (17) display with its lead-in tail in block 150, the 7.2.1 heading, the GDP-Loss paragraph, the 7.2.2 heading, the resistance-survey paragraph, the clustering-method paragraph, and two cluster bullets (155-156) | yes, exact | the page also fixes the cross-reference defect: block 154 says 'as shown in Figure 7' for the four-cluster scatter, but Figure 7 is the Expected global impact of the replacement on climate mitigation chart (caption at block 147), and the scatter never gets a caption 
| 2024-2409949 | 17 (footer 'Team #2409949 / Page 17 of 22') | 7 blocks start here (159-165) plus 166-170 on the same page | 8 units: Table 5 with its header and four variable rows, the OLS statement with eq (1), the VIF statement with eq (2) carrying both the R and VIF forms, the Table 6 results block, the ridge statement with eq (3), the weight computation with eq (4), and the ridge-trace paragraph | yes, exact | the render fixes the extraction errors: Table 5 prints x1-x4 as the four OVIs, Table 6 reports VIF 15.069 / 13.08 / 15.908 / 4.43 for n = 7, and eq (3)-(4) use k not lambda, so the 'VIF method' sentence in block 170 refers to a criterion ridge regression does not use 
| 2024-2413565 | 20 (footer 'Team # 2413565 / Page 20 of 25') | 10 blocks start here (207-216) | 9 units: the decoration-bullet tail carried from 206, the experimental bullet (208-209), the Figure 12 / Figure 13 pair (210), the summary paragraph (211), the fitted equation (212) printed as a display, the ranking paragraph (213), the 5.5 heading with its intro paragraph (214), the five-point setup paragraph (215), and eq (9) as a four-line brace display (216) | yes, exact | the render confirms the three-part split of the coefficient bullets and pins the fitted equation: Y = 1.527 - 0.147X1 + 0.164X2 + 0.812X3 - 1.811X4 + 2.651X5, so decoration trade (X4) carries the largest negative and experimental trade (X5) the largest positive coefficient, both on eight annual observations 
| 2024-2417340 | 9 (footer 'Team # 2417340 / Page 9 of 27') | 8 blocks start here (82-89) | 7 units: the Figure 2 caption under its two weight pies, the 5.3 heading with the three-client paragraph (83), the GA / INO / PAP bullets (84-86), the scoring paragraph (87), the Figure 3 radar chart with its caption (88), and the first line of the Figure 3 reading (89) | yes, exact | the render confirms the AHP outputs as pies, not tables: PUR 0.43 / PER 0.35 / SR 0.22 for strike factors and species diversity 0.44 / international reputation 0.33 / actual benefit 0.23 for benefits, and the radar shows PAP sitting furthest out on both PUR and SR while INO leads on CI and IN, which is what block 90 reads |
| 2024-2422054 | 17 (footer 'Team # 2422054 / Page 17 of 25') | 6 blocks start here (193-198) | 8 text units: the tail of the c4-c6 where-clause carried from 192, the budget paragraph (193), the two-line display (22)-(23), its where-clause (194), the equity paragraph with (24) (195), the (25) objective line (196), 'where Ggov is the goal of government' (197), and the first two lines of 198 | yes, exact | the render settles the equation-numbering question: (22) Bt = Bt-1 + dGDP_{t-1} and (23) = Bt-1 + rho(dInfra_t + dSub_t) are both printed, so nothing is missing between (21) and (23); it also shows rho defined only in the prose of 193 and absent from Table 1, the stock-minus-stock equals flow slip in (22), and the dropped word in 'comparing the income changes between low high-income groups' above (24) |
| 2024-2426941 | 7 (footer 'Team # 2426941 / Page 7 of 27') | 18 blocks start here (79-96) | 15 text units: the judgment-matrix line (79), Step 2 with (1)-(2) and its consistency verdict (80-81), Step 3 (82-83), the EWM bullet plus its lead (84-85), Steps 1-3 of EWM with (3)-(5) (86-88), the game-theory bullet (89), the (6) objective with its constraint line (90), the normalisation of lambda (91), the 4.4 heading (92), the TOPSIS paragraph (93), the D+ and D- definitions (94-95), and the score line with (7) and the Figure 4 caption (96) | yes, exact | the render verifies the AHP consistency arithmetic (n = 12, RI = 1.54, CR = 0.068 < 0.1) and pins three printed defects: eq (5) divides 1 - e_j by the sum of d_j, and d_j is never defined anywhere in the paper (it should be 1 - e_j); the game-theory objective is introduced as minimising deviations of 'W and b and c', two symbols that appear in no equation; and the paragraph above the 4.4 heading says the combined weights are 'shown in Figure 3', while Figure 3 is the alternative-clients graphic and the weights are Figure 4 |
| 2025-2504223 | 13 (footer 'Team # 2504223 / Page 13 of 25') | 12 blocks start here (123-134) | 15 visible units: the Figure 6 parallel-trend plot with its caption, the 6.1.4 heading, the 'model results obtained by solving' lead, 'For the attacking country:' with (9)-(13), and 'For the victim country:' with (14)-(18) | mapped, 73% by raw count | 11 of the 12 blocks carry the 15 units because the layout merges each group label into the preceding display (123 = lead + 'For the attacking country:', 128 = the (13) display + 'For the victim country:'), and 134 is a 689-token watermark block that prints nothing; the render also shows the parallel-trend plot failing its own test, with the pre-period coefficients climbing from about -1 at t = -4 to +0.3 at t = -1 before the dashed treatment line, and (18) printing 'id_it' for 'did_it' |
| 2025-2507789 | 22 (footer 'Team #2507789 / Page 22 of 25') | 13 blocks start here (135-147) | 17 visible units: the three numbered pathways with their formulas (135-139), the mediation paragraph with its four bulleted equations (140-144), the 7.4 heading and the figure caption glued into the tail of 144, the SEM diagram, and the first conclusion bullet (145-147) | mapped, 76% by raw count | 134 is a 726-token watermark block whose tail spills onto page 22; the render shows the SEM diagram contradicting its own text: it routes GDP->Metal, NetRate->Fire and Education->Water only, while block 136 states X_edu -> M, W and X_int -> F, E, and it draws five direct arrows into Y_Crime so the M -> F -> E chain of 141-143 is absent; the diagram carries none of the loadings of 133-134, and Y_Crime prints both alpha_Y and an undefined gamma_0 |
| 2025-2513705 | 15 | 10 blocks start here (128-137) | 14 visible units: the control-normalisation paragraph, the '3. Model Specification' heading, 'The DID model was formulated as follows', the DID equation display, the duplicate 'we utilized the Difference - in - Differences' paragraph, the 5.2 heading, '1. Cybercrime Criminal Legislation', the Australia/Ireland-versus-UK/New-Zealand arm, Table 2 with its caption, the R2 remarks line, the asterisk note, '2. Data Protection and Privacy Regulations' and that theme's arm | mapped, 71% by raw count | four headings and the table caption share their block with the paragraph they belong to (129 = heading + 'formulated as follows', 131 and 132 = two headings in one block, 134 = caption + table + the null row, 136 = heading + next arm), so every unit is accounted for; the render also supplies the equation the extraction lost (Y_it = alpha + b1 treated + b2 time + b3 treated x time + sum gamma_k X_kit + e), shows Table 2 printing 'null null null' for the after-period diff, and shows the R2 = 0.713 / adjusted 0.635 remark for an arm of two treated and two control countries |
| 2025-2517199 | 13 | 5 blocks (tail of 48, then 49-52) | 7 printed units | mapped, 71% by raw count - the '3.3 Model III...' chapter heading is glued into the tail of block 48 together with a watermark line, 49 is the 3.3.1 heading running alone, and 51 holds the TABLE III caption, the table and its nine numeric columns; every printed unit on the page is inside a measured block |
| 2025-2521039 | 18 | 7 blocks (153-159) | 7 printed units | yes - two China paragraphs, the Figure 13 caption, the '5.4 Theoretical Summary' heading and its three paragraphs; block 159 is clipped at the foot and continues on page 19 |
## Extraction gaps met so far

- 2025-2504223: five pages have no text layer. That paper's `extraction.json` lists `empty_or_near_empty_pages` = 2, 15, 16, 18, 25 with status `partial-text-review`. Page 2 is the contents and page 25 is the MEMO, so the memo chapter exists in the printed paper but has zero measured blocks; it is recorded in `records/P-F-2025-2504223-019dfa54.json` with empty `groups` and `jobs` rather than dropped. Pages 15, 16 and 18 hold the Figure 8 radar chart, sections 6.2-6.4 with equations (19) and (20), the Figure 11 forest map and section 6.6; I read all three on the render and described their content in the 6.2-6.5 chapter note, because no block exists there to code.
- 2025-2507789: `empty_or_near_empty_pages` = 2, 3, 4, 17, 18, status `partial-text-review`. Page 1 stops mid-abstract ('...practical, high-impact strategy'), so pages 2-4 hold the abstract tail and whatever else the authors put before section 2. Pages 17-18 hold sections 6, 6.1 and 6.2, i.e. the whole setup of Model II: the text jumps from the Five Elements classification list straight to '6.3 Impact of Policies vs. Cybercrime'. The model-establishment chapter for 6.3 and the strengths-limitations note both say so; no block is invented for the missing pages.
- 2025-2513705: `empty_or_near_empty_pages` = 2, 5, 6, 8, 11, 18, 31, status `partial-text-review`. Page 5 prints '2 Assumptions and Justifications' (three assumptions with justifications) and '3 Notations' with Table 1; page 6 prints chapter 4 with 4.1 Introduction, 4.2 Indicators Selection, 4.3 Data Analysis and 4.3.1 with the NCSI item; page 8 prints indicator '3. Legal Measures (Global Cybersecurity Index)' with Figures 3 and 4 and a two-country example; page 11 prints the Cyan and Yellow cluster profiles and '3. Integration with Individual Indicator Analyses'; page 18 prints 6.1, 6.1.1, 6.1.2 and 6.2 with 20 countries, Bartlett p = 0.000, two factors at 50.657% and 24.605% and a composite score of 0.673 x Factor 1 + 0.327 x Factor 2. Read on the render only, described in the notes of the neighbouring chapters (2, 3, 4.1-4.2, 4.3.1, 4.3.2, 6), and never given invented blocks. Page 31 is inside the AI-use appendix, which is out of scope.
- A chapter whose blocks are missing cannot be coded, so the ledger for such a paper shows fewer chapters than the printed contents. This is flagged rather than patched: writing blocks the layout does not contain would break the `layout/<pid>.json` contract.

- 2025-2517199: five pages have no text layer - 1, 2, 9, 10 and 12 (word counts 0). Pages 1-2 are the title sheet and abstract, so the text layer opens at block 1 = '1. Introduction' and block 2 = '1.1 Problem Background'. Pages 9-10 hold the whole of chapter 3 before 3.3: the '3. Model Establishment' heading, 3.1 Model I, equations (5) and the risk-index definition with its >2.0 / 2.0-1.5 / 1.5-0.5 / <0.5 bands and Figure 5's four ratio maps (contamination, discovered, severity, success), plus 3.2 Model II, 3.2.1 Policy Analysis and Classification (three policy areas and the A/B/C abbreviation paragraph) and 3.2.2 Cybercrime Timeline of Some Countries. Page 12 falls between 2.3 and the tail of block 48. All of it is described from the render in the introduction, results and model-establishment notes; no block is invented for those pages.
- 2025-2521039: five pages have no text layer - 2, 5, 15, 16 and 24 (word counts 0). The codable body runs from block 9 (keyword line plus '1 Introduction') to block 240 (last reference); blocks 241-286 are the 'Report on Use of AI' transcripts and are not coded. Page 2 is the table of contents and it is the paper's own inventory of what the text layer loses: 3 Interpretation of Symbols with Table 1, 4 / 4.1 / 4.2 with four paragraphs, 4.3.4 Pattern Analysis (whose heading appears nowhere in the text), 5.2.4 Comprehensive Scoring Analysis of Policy Effectiveness, 5.3 Pattern Analysis, 5.3.1 Analysis of GCI's Five Pillars with Figure 11, and 9 Memorandum. The paragraphs that read Figures 8 and 9 survive, but every scoring number the paper reports - the U.S. 0.32 and China -0.78 of the abstract and the per-country b3 of the DID section - lives on those pages. Each is described from the render in the notation, data-preprocessing, model-establishment, results and memo notes; no block is invented. The memo chapter is recorded with empty groups for that reason, and its note carries what page 24 prints (about 500 words, four recommendation bullets, three italic pillar sub-bullets).
## Scope exclusions

Five kinds of block are never coded into a chapter record, and each is counted so that the gap stays visible:

- **Abstract blocks.** The standing instruction is body chapters only. On papers where the summary sheet and
  the abstract are separate blocks (1-8 on 2025-2513705) they stay out of the ledger.
- **Appendix and AI-use blocks.** 2025-2513705 prints a 'Use of AI' appendix of ChatGPT transcripts from
  block 242 to 445: query prompts, long answer text, and advice on chart styling. It is not a body chapter and
  has no chapter in the corpus vocabulary, so blocks 242-445 are left uncoded. The body range 9-241 is coded
  completely (233 blocks, no duplicates, no holes) and the note on the last memo group records the extra-paper
  heading glued into block 241.
- **A second AI appendix.** 2025-2521039 prints 'Report on Use of AI' from block 241 to the end: ChatGPT queries about data sources, LaTeX image sizing, heading spacing and table formatting, then an 'Overall Experience' section. Blocks 241-286 are left uncoded; the body range 9-240 is coded completely (232 blocks, no duplicates, no holes). The title sheet (blocks 1-2), the Contents page (page 2) and the abstract (blocks 3-8) are also outside the ledger.
- **Contents pages, running heads and watermark banners.** No record codes them: 2017-64486 21-38, 2017-72197 15-19, 2018-83744 17/27-39/52/87/95/109/121/136/146/160/171/184/200/210/211/218/249, 2018-88508 27, 2018-93036 61-71, 2019-1905127 14, 2019-1916375 16-27 and 2024-2422054 26-32 are table-of-contents lines, page furniture or the shop banner that sits in the header of 2018-83744. They carry no paragraph function and blocking them would inflate the block counts.
- **Standalone reference sections.** Where a paper prints References as its own heading the list is left uncoded: 2016-44348 203-204, 2016-46634 207-216, 2023-2305794 294-305, 2024-2426941 289-295. Where the reference list is glued to the conclusion heading (2025-2517199 6 Conclusion and 7 Reference, 2025-2521039 8 Conclusions and References) it is coded inside that chapter as source blocks, so the rule is that references enter the ledger only when they share a chapter with conclusion text.

Where a paper prints an appendix that does belong to the argument, it is coded inside the chapter that
introduces it rather than given a chapter value of its own.

## Merge contract for the other session

Read `jobs-f.jsonl`, one record per paper-chapter. To pool with A–E:

- filter `ext` out, or adopt `context` / `claim` as jobs first;
- treat `chapter` as the corpus label (`model-establishment`, `memo`,
  `sensitivity-analysis`, …) and use `heading` for the paper's own wording;
- a chapter that occurs twice in one paper (static model, then dynamic model) is
  two records with the same `chapter` and different `heading`;
- promotion threshold (60% per type, 4 of 6 types) still needs the other types.
- every `chapter` value is one of the fourteen corpus labels. Thirteen records drafted earlier under local names were relabelled: `policy-letter` -> `recommendation` (2016-43181, 2016-44348), `sensitivity-robustness` -> `sensitivity-analysis` (2016-46634, 2017-64486), `problem-restatement`, `literature-review` and `problem-analysis` -> `introduction` (2017-64486, 2017-68940, 2022-2208238, 2022-2209952), with 2017-72197's definitional 'B. Defining Utopia' -> `notation`, and `metrics` / `model-improvement` -> `model-establishment` (2016-44348, 2018-83744). Blocks, groups and jobs are unchanged by the relabelling, and `heading` keeps the paper's own wording.

## Counting units: what each field counts

The ledger, `jobs-f.jsonl` and the merge outputs use three different units, and only
one of them is paragraphs. Mixing them silently produces nonsense rates.

`artifacts/paragraph-ledger.jsonl`, one row per paper-chapter (A–E, plus the older F rows):

- `stored_count` — units the corpus `chapter_layouts` claims for the chapter. This is
  an upstream artifact count and it is sometimes degenerate: `P-A-2015-32150-b7715ba1`
  stores a single unit named `setup` for a span of three pages holding 680 words.
- `located_count` — paragraphs located by hand in the rendered page when `stored_count`
  is unusable. Present only on rows where the upstream count was rejected.
- `segmentation` — present only on those same rows; names why the stored count was
  thrown out (`artifact-placeholder-names`, and so on).
- `jobs` — one job token per hand-coded block. This, not `stored_count`, is the
  paragraph population.
- `function_strings` — the stored `paragraph_functions` strings, verbatim, never used
  as a job label (see `merge/report.md` Result 2: they are per-paper text, not templates).

So `sum(len(jobs)) / sum(stored_count)` is not a paragraph rate. Where the upstream
count is degenerate the ratio exceeds 1 by construction: 48 of 93 A rows have more
jobs than stored units, and that is the intended outcome of a hand re-segmentation,
not a defect. Use `located_count` when present, `len(jobs)` otherwise.

`jobs-f.jsonl`, one record per paper-chapter (F, hand-coded):

- `stored_count` — stored units, kept only for comparison; `literal_blocks` — blocks
  measured from the PDF text coordinates; `group_count` — visual paragraphs after
  merging heading fragments and figure legends; `blocks` — the block span;
  `jobs` — one token per group, so `len(jobs) == group_count`; `units[].open` /
  `units[].close` — the verbatim opening and closing sentence of each group.

F's four counts are related but not equal (`stored_count` is frequently the odd one
out); `group_count` is the answer to "how many paragraphs is this chapter".

## Job tokens: 13 base, 2 extras, one composite form

`tmp/para-taxonomy.md` defines the 13 base jobs. Three things appear in the raw
`jobs` arrays that are not one of the 13, and a consumer that filters against the
13 silently loses about 500 of F's 6,794 blocks:

| form | count in `jobs-f.jsonl` | meaning | how to aggregate |
|---|---|---|---|
| `ext:context` | 172 | framing block that sets up a chapter's claim without doing model work | keep as its own column, or drop deliberately |
| `ext:claim` | 190 | assertion stated for the paper's own result, no evidence attached | same |
| `A+close:B` | 143 | block opening with function A whose closing sentence does function B | split on `+close:`, keep `A` |

`merge/jobs-by-type.csv` aggregates this way (base token only), which is why its F
column sums to 6,794 and why `ext:claim` reads 197 there rather than 190 — the seven
`ext:claim+close:*` blocks are counted under `claim`. Any other consumer must apply
the same rule or the totals will not reconcile. `unresolved` is not a job: it marks a
block an earlier pass could not name, it is dropped from sequences, and the row is
flagged in `metrics.json` → `ledger_rows_with_unresolved`.

## Refreshing the merge numbers

`merge/` is measured against a frozen copy of the ledger, not the live file, because
the encoding session appends to `artifacts/paragraph-ledger.jsonl` while an audit
runs. Nothing refreshed that copy, so `report.md`, `blocked.md` and
`blocked-papers.csv` drifted roughly 55 rows behind the ledger before this was
caught. Always run both steps, in this order:

```bash
python -I -X utf8 lanes/L1-f-structure/tools/freeze_ledger.py
python -I -X utf8 lanes/L1-f-structure/tools/audit_merge.py
```

`freeze_ledger.py` prints the row count and sha256 it froze; those two numbers are
the population every figure in `merge/` describes. `audit_merge.py` is deterministic
on a fixed snapshot: two runs give byte-identical `metrics.json` and
`jobs-by-type.csv`.
