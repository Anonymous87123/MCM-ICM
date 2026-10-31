# Residue ledger — every number in `quote-levels.md`, named to a file:line

Scope of this file: the three sections of `lanes/L9-merge-dryrun/reports/quote-levels.md` that state a
number — *Reconciliation with the census* (lines 66-88), *Quotation cross-check* (lines 90-92) and
*Leftover quote rows and stale references* (lines 94-96) — plus the tables those sections lean on
(*Rows per lane*, *Level distribution*, *Level by evidence class*, *Four separately reported counts*).

Rule applied throughout: a number is `named` only when it has been re-read from the file that carries
it, `explained` when the recomputation disagrees and the cause is named row by row, `open` when neither.
No cell is left blank and no number is carried over from an earlier report.

## Run log — deterministic hash checkpoints

Both scripts run in this order: `python -I tmp/levels_l9.py`, then `python -I tmp/levels_md.py`.
`levels_l9.py` rewrites `reports/quote-levels.jsonl` and `reports/leftover-quotes.json`; `levels_md.py`
rewrites `reports/quote-levels.md`.

| checkpoint | rows named in this file | quote-levels.jsonl sha256 | leftover-quotes.json sha256 | quote-levels.md sha256 |
|---|---|---|---|---|
| baseline (before any record) | 0 | 30dfead58225ba5a9ab36b758bcac6216f6240a366bc0bc774214abae88f5ec7 | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 | ed865a455aa4b3c44fa330631421306104f00fd23f8a14301d79b4d75672dd91 |
| after B01-B10 | 10 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after B11-B20 | 20 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after B21-B30 | 30 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after B31-B40 | 40 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after B41-B50 | 50 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after B51-B60 | 60 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after B61-B70 | 70 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after B71-B76 | 76 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after C01-C30 | 106 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after C31-C59 | 135 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after D01-D40 | 175 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after E01-E27, F01-F45 | 247 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |
| after §5 rung table, §6 ocr table, §7 gap rows | 247 + 14 + 72 + 2 | 30dfead58225ba5a… | 37517e5f3dc66819… | ed865a455aa4b3c4… |

The baseline pair of runs produced byte-identical JSON to `stdout` as well (`cmp` clean), so a hash
change below is a real change, not run-to-run noise.

At the last checkpoint `quote-levels.md` moves from ed865a455aa4b3c4… to 0f4bed938be387a8… while
`quote-levels.jsonl` and `leftover-quotes.json` stay byte-identical. Cause, checked before going on:
the peer lane rewrote `tmp/levels_md.py` so its prose numbers are computed from the census files and
`reports/quote-check.json` instead of typed in, and `tmp/levels_l9.py` to emit that file. No record,
layout or quote file changed, and the rewritten md prints the same reconciliation cells this file
counts. Line anchors did not move: the regenerated file is still 97 lines with the same headings at
the same numbers. Every claim quoted in §1-§7 below is quoted as it stood at ed865a45…; where the
regeneration changed a number, the row says so.

A second regeneration moved `quote-levels.md` to 7610a863… with `quote-check.json` at fccbdd62…: the
peer replaced the mechanism sentences §5 and §6 contradict (the glue cause and the ocr split row) and
added `quote_mismatch_in_block` / `quote_mismatch_normalised_only` / `quote_mismatch_absent` to
`quote-check.json`. Data layer unmoved at 30dfead5… / 37517e5f…, and its three counts reproduce §8
exactly: 205 / 41 / 1 over the 247 rows.

## Checklist — numbers copied out of the three sections

Column *md:line* is the line in `quote-levels.md` that prints the number. Column *evidence* is the file
that carries it; `quote-levels.jsonl` line ranges are first/last line of the rows with that level in
that lane, `levels-*.json` line numbers are the census key that states the compared value.

### Rows per lane (md lines 7-17)

| id | md:line | number | claim | evidence | status |
|---|---|---|---|---|---|
| R1 | 9 | 3,232 | A rows here | `quote-levels.jsonl`:1-3232 (all `type` A) | named |
| R2 | 9 | 3,232 | A census rows | no census file for A; value is the A row count itself (md line 17 says A has no ladder level) | named |
| R3 | 9 | +0 | A difference | same two files | named |
| R4 | 10 | 10,333 | B rows here | `quote-levels.jsonl`:3233-13565 | named |
| R5 | 10 | 10,333 | B census rows | `lanes/L7-quote-backfill/reports/levels-b.json`:6 | named |
| R6 | 10 | +0 | B difference | same | named |
| R7 | 11 | 10,397 | C rows here | `quote-levels.jsonl`:13566-23962 | named |
| R8 | 11 | 10,397 | C census rows | `levels-c.json`:6 | named |
| R9 | 11 | +0 | C difference | same | named |
| R10 | 12 | 5,308 | D rows here | `quote-levels.jsonl`:23963-29270 | named |
| R11 | 12 | 5,308 | D census rows | `levels-d.json`:6 | named |
| R12 | 12 | +0 | D difference | same | named |
| R13 | 13 | 5,024 | E rows here | `quote-levels.jsonl`:29271-34294 | named |
| R14 | 13 | 5,024 | E census rows | `levels-e.json`:6 | named |
| R15 | 13 | +0 | E difference | same | named |
| R16 | 14 | 6,794 | F rows here | `quote-levels.jsonl`:34295-41088 | named |
| R17 | 14 | 6,794 | F census rows | `levels-f.json`:6 | named |
| R18 | 14 | +0 | F difference | same | named |
| R19 | 15 | 41,088 | total rows here | `quote-levels.jsonl`:1-41088 | named |
| R20 | 15 | 41,088 | total census rows | 3,232 + 10,333 + 10,397 + 5,308 + 5,024 + 6,794 | named |
| R21 | 17 | 3,232 | A rows carry the quote in the lane record | `quote-levels.jsonl`:1-3232, every row `level` = `in-record` | named |
| R22 | 17 | five | census files cover B to F | `levels-b.json` … `levels-f.json`, one per lane | named |
| R23 | 17 | 0 | `quote_shortfall` in `stats.json` | `lanes/L9-merge-dryrun/reports/stats.json`: `totals.quote_shortfall` = 0 | named |
| R24 | 17 | C seven rows / D one row | the difference the repairs left | contradicted as a description of the join: the census files were regenerated too (`levels-c.json`:6 = 10,397, `levels-d.json`:6 = 5,308), so the table shows +0 and no subtraction is needed. The seven and the one are the unit counts the repairs removed, see `residue.md` §5 | explained |

### Level distribution (md lines 23-34)

`here` cells are counted off `quote-levels.jsonl`; the `all` column is the row sum. Every cell below was
recounted from the same file, so the evidence line range is the one printed with the level in the
reconciliation table (§ bottom rungs). Levels absent from a lane are printed 0 and were recounted as 0.

| id | md:line | number | claim | evidence | status |
|---|---|---|---|---|---|
| D-exact | 23 | 0 / 7,950 / 8,325 / 4,806 / 4,555 / 5,906 / 31,542 | exact by lane and all | `quote-levels.jsonl` B 3233-13565, C 13566-23962, D 23963-29270, E 29271-34294, F 34295-41088; A has none | named |
| D-nfkc | 24 | 0 / 850 / 814 / 9 / 14 / 28 / 1,715 | nfkc by lane and all | same file, level `nfkc` | named |
| D-squeezed | 25 | 0 / 486 / 435 / 138 / 93 / 218 / 1,370 | squeezed by lane and all | same file, level `squeezed` | named |
| D-span | 26 | 0 / 551 / 428 / 225 / 226 / 362 / 1,792 | span by lane and all | same file, level `span` | named |
| D-gapped | 27 | 0 / 143 / 117 / 57 / 52 / 124 / 493 | gapped by lane and all | same file, level `gapped` | named |
| D-ocr | 28 | 0 / 4 / 0 / 0 / 0 / 0 / 4 | ocr-only by lane and all | same file, level `ocr-only` | named |
| D-ntl | 29 | 0 / 68 / 0 / 0 / 0 / 0 / 68 | no-text-layer by lane and all | same file, level `no-text-layer` | named |
| D-gap | 30 | 0 / 0 / 0 / 0 / 0 / 2 / 2 | text-gap by lane and all | same file, level `text-gap` (F 36892, 39710 are the two rows) | named |
| D-unv | 31 | 0 / 281 / 181 / 73 / 84 / 154 / 773 | unverified by lane and all | same file, level `unverified` | named |
| D-lo | 32 | 0 / 0 / 97 / 0 / 0 / 0 / 97 | layout-only by lane and all | same file, level `layout-only` | named |
| D-ir | 33 | 3,232 / 0 / 0 / 0 / 0 / 0 / 3,232 | in-record | same file, level `in-record` | named |
| D-total | 34 | 3,232 / 10,333 / 10,397 / 5,308 / 5,024 / 6,794 / 41,088 | rows by lane and all | same file | named |

### Level by evidence class (md lines 40-51)

| id | md:line | number | claim | evidence | status |
|---|---|---|---|---|---|
| E-exact | 40 | 72 / 31,045 / 292 / 133 / 31,542 | exact by class | `quote-levels.jsonl`, `evidence_class` × `level` | named |
| E-nfkc | 41 | 3 / 1,700 / 0 / 12 / 1,715 | nfkc by class | same | named |
| E-squeezed | 42 | 0 / 1,358 / 2 / 10 / 1,370 | squeezed by class | same | named |
| E-span | 43 | 0 / 1,773 / 6 / 13 / 1,792 | span by class | same | named |
| E-gapped | 44 | 1 / 488 / 0 / 4 / 493 | gapped by class | same | named |
| E-ocr | 45 | 0 / 4 / 0 / 0 / 4 | ocr-only by class | same | named |
| E-ntl | 46 | 0 / 68 / 0 / 0 / 68 | no-text-layer by class | same | named |
| E-tgap | 47 | 0 / 2 / 0 / 0 / 2 | text-gap by class | same, the two F rows | named |
| E-unv | 48 | 0 / 749 / 19 / 5 / 773 | unverified by class | same | named |
| E-lo | 49 | 0 / 95 / 2 / 0 / 97 | layout-only by class | same | named |
| E-ir | 50 | 0 / 3,232 / 0 / 0 / 3,232 | in-record by class | same | named |
| E-total | 51 | 76 / 40,514 / 321 / 177 / 41,088 | class totals | `stats.json`: `totals.evidence_class` prints the same four numbers | named |

### Four separately reported counts (md lines 59-62)

| id | md:line | number | claim | evidence | status |
|---|---|---|---|---|---|
| C-ntl | 59 | 0 / 68 / 0 / 0 / 0 / 0 / 68 | no-text-layer | `quote-levels.jsonl`, level `no-text-layer` | named |
| C-ocr | 60 | 0 / 4 / 0 / 0 / 0 / 0 / 4 | ocr-only | same, level `ocr-only` | named |
| C-unv | 61 | 0 / 281 / 181 / 73 / 84 / 154 / 773 | unverified | same, level `unverified` | named |
| C-lo | 62 | 0 / 0 / 97 / 0 / 0 / 0 / 97 | layout-only | same, level `layout-only` | named |
| C-sum | 64 | 72 | ocr-only plus no-text-layer, against the census 72 | see §3 | explained |

### Quotation cross-check and leftovers (md lines 92-96)

| id | md:line | number | claim | evidence | status |
|---|---|---|---|---|---|
| Q-rows | 92 | 37,856 | B to F rows compared | 41,088 - 3,232 (`quote-levels.jsonl`:1-3232) | named |
| Q-mis | 92 | 257 | rows whose stored quote differs | contradicted at ed865a45…: the recomputation returns 247, named row by row in §4; the 257 was typed at `tmp/levels_md.py`:178. Regenerated at 0f4bed93…, the same sentence now reads 247 from `reports/quote-check.json` | explained |
| Q-pct | 92 | 0.7 percent | share of mismatching rows | 247/37,856 = 0.65 percent; the 0.7 is the rounded form of the stale 257/37,856 = 0.68. Regenerated, the line prints 0.65 | explained |
| Q-sha | 92 | 0 mismatches, 0 dangling | stored quote hashes re-verified against the L7 files | `quote-levels.jsonl` every row carries `quote_sha256`; re-hash of the cited string checked row by row in §4 (each row's `stored_quote` is the string at the cited line) | named |
| L-unc | 96 | 0 | quote rows cited by no projection row | `lanes/L9-merge-dryrun/reports/leftover-quotes.json` is `[]` | named |
| L-stale | 96 | 0 | rows citing a line the quote file no longer has | `tmp/levels_l9.py` writes `stale_refs` from a `None` quote; the run reports `stale_refs: 0` | named |

## 4. Quote strings that differ — one row each

Recomputed with `tmp/levels_l9.py`'s own `Paper`/`pick`, then the stored string was read back from the
exact line the projection cites and the two were printed side by side by
`lanes/L9-merge-dryrun/tools/quote_mismatch_list.py` (`reports/residue-mismatches.jsonl`). Every row
below was judged from that side-by-side print, not from an earlier report.

Count: **247** rows (B 76, C 59, D 40, E 27, F 45), against the 257 the report states — see Q-mis.

Cause labels used, defined once:
- `ladder-shorter` — one string is a strict prefix of the other: the ladder's candidate ends at a colon,
  an equation or a wrapped line and the L7 string continues past it.
- `head-skipped` — the ladder's pick starts inside the block instead of at its opening words, because the
  opening words carry glyphs the text layer does not hold.
- `label-dropped` — the stored string keeps a printed label the ladder's candidate strips.
- `column-order` — the block is a multi-column or hyphenated wrap and the two passes took different line
  slices of the same block.
- `other-sentence` — both strings are sentences of the same block and the two passes picked different ones.
- `glued-token` — the divergence is at a join between two words; the glued form is quoted verbatim.

### B lane (76)

| id | paper | ch/group | block | L7 file:line | stored/ladder chars | cause | status |
|---|---|---|---|---|---|---|---|
| B01 | P-B-2010-8479-b934962b | ch10/g3 | 90 | quotes-b.jsonl:504 | 81 / 76 | column-order — address column: stored `262 Alexander Esau 1878 Hutchinson`, ladder `367 Stacy Moskowitz 86th St` | named |
| B02 | P-B-2011-9440-95f0fa40 | ch6/g4 | 100 | quotes-b.jsonl:880 | 81 / 71 | other-sentence — stored `Reachability. The reachable area`, ladder `Every point in the considered area` | named |
| B03 | P-B-2012-15420-8b46b980 | ch6/g6 | 65 | quotes-b.jsonl:1288 | 52 / 49 | glued-token — ladder stops at `in the`, stored carries `in the Na` (the `Naïve` glyph run) | named |
| B04 | P-B-2013-21185-c7f22f59 | ch7/g21 | 167 | quotes-b.jsonl:1576 | 101 / 98 | other-sentence — stored `and statistical convenience…`, ladder `By calculatingα of each province` | named |
| B05 | P-B-2014-26333-27e7d8ab | ch14/g27 | 463 | quotes-b.jsonl:2072 | 52 / 45 | glued-token — stored `(different pexit)`, ladder `(different` | named |
| B06 | P-B-2014-26333-27e7d8ab | ch14/g29 | 465 | quotes-b.jsonl:2074 | 56 / 49 | glued-token — stored `(different pexit)`, ladder `(different` | named |
| B07 | P-B-2014-28414-5bd5b982 | ch8/g3 | 154 | quotes-b.jsonl:2313 | 119 / 85 | head-skipped — stored `for each of the XXiiii`, ladder `we could concluded the fuzzy matrix` | named |
| B08 | P-B-2014-28414-5bd5b982 | ch8/g7 | 159 | quotes-b.jsonl:2317 | 90 / 69 | ladder-shorter — ladder ends at `evaluation grade:`, stored adds `ggjj= 1 −eejj (4.15)` | named |
| B09 | P-B-2014-28414-5bd5b982 | ch8/g10 | 163 | quotes-b.jsonl:2320 | 83 / 52 | other-sentence — stored `The playoff performance (XX3)`, ladder `The weights for each aspect` | named |
| B10 | P-B-2014-28875-728f6f07 | ch6/g2 | 116 | quotes-b.jsonl:2445 | 139 / 127 | ladder-shorter — ladder ends at `metrics formula is`, stored adds `x ( i , j )` | named |
| B11 | P-B-2014-28875-728f6f07 | ch6/g4 | 118 | quotes-b.jsonl:2447 | 88 / 60 | ladder-shorter — ladder ends at `excellent type`, stored adds `indicators is x ( i , j )` | named |
| B12 | P-B-2015-32879-2c587e51 | ch18/g2 | 260 | quotes-b.jsonl:2931 | 48 / 46 | column-order — stored `portion of the globe`, ladder `mediate power loss to a sustained glide` | named |
| B13 | P-B-2015-32879-2c587e51 | ch18/g3 | 262 | quotes-b.jsonl:2932 | 135 / 134 | column-order — stored `plane, standard cruising altitudes`, ladder `craft. This map is constructed` | named |
| B14 | P-B-2015-32879-2c587e51 | ch18/g4 | 263 | quotes-b.jsonl:2933 | 45 / 40 | column-order — stored `namic model allows for your search efforts`, ladder `mation and data from the search. The dy-` | named |
| B15 | P-B-2015-32879-2c587e51 | ch18/g5 | 264 | quotes-b.jsonl:2934 | 47 / 45 | column-order — stored `paths and geographic coordinates`, ladder `your pilots in the search effort will be com-` | named |
| B16 | P-B-2015-32879-2c587e51 | ch18/g6 | 265 | quotes-b.jsonl:2935 | 44 / 40 | column-order — stored `meeting your needs in any further search`, ladder `We hope that this model is sufficient in` | named |
| B17 | P-B-2015-38720-26d38781 | ch1/g3 | 5 | quotes-b.jsonl:3066 | 66 / 62 | other-sentence — stored `Gaussian normal distribution bounded by`, ladder `Projecting a commercial airplane’s flight path` | named |
| B18 | P-B-2015-38720-26d38781 | ch5/g6 | 184 | quotes-b.jsonl:3128 | 49 / 29 | other-sentence — stored `The time controllers first suspect a problem`, ladder `Time of First Alert ( T = τ )` | named |
| B19 | P-B-2015-38720-26d38781 | ch5/g11 | 204 | quotes-b.jsonl:3133 | 48 / 44 | glued-token — ladder ends `to A`, stored carries `to A (d` | named |
| B20 | P-B-2015-39173-b8260835 | ch11/g16 | 125 | quotes-b.jsonl:3375 | 47 / 44 | glued-token — ladder ends `if`, stored carries `if h2` | named |
| B21 | P-B-2017-56731-a60a9459 | ch8/g30 | 94 | quotes-b.jsonl:4146 | 376 / 367 | ladder-shorter — ladder ends `merging point is:`, stored adds `2(k+ 1)Φ` | named |
| B22 | P-B-2017-56731-a60a9459 | ch8/g31 | 95 | quotes-b.jsonl:4147 | 82 / 74 | ladder-shorter — ladder ends `merging point is:`, stored adds `2(k+ 1)` | named |
| B23 | P-B-2017-68303-6c8a9ede | ch8/g9 | 66 | quotes-b.jsonl:4307 | 69 / 73 | ladder-longer — stored ends `∑n`, ladder extends to `∑n k=1` | named |
| B24 | P-B-2017-69427-b04ae242 | ch6/g6 | 95 | quotes-b.jsonl:4433 | 77 / 69 | head-skipped — stored starts `Where,K is the coefficient`, ladder starts `is the coefficient` | named |
| B25 | P-B-2017-69427-b04ae242 | ch12/g8 | 186 | quotes-b.jsonl:4503 | 92 / 81 | other-sentence — stored `vehicle driver is r . At this point`, ladder `; the headway of the rear and front vehicles` | named |
| B26 | P-B-2017-70545-8e86fcfa | ch9/g6 | 113 | quotes-b.jsonl:4756 | 114 / 65 | other-sentence — stored `PETi<tr Considering the total delayed time`, ladder `the mean time needed of a vehicle` | named |
| B27 | P-B-2018-77238-4380ec81 | ch6/g6 | 55 | quotes-b.jsonl:5166 | 100 / 96 | other-sentence — stored `Pi2j1), and people in the same country`, ladder `differ from country to country` | named |
| B28 | P-B-2018-77238-4380ec81 | ch9/g13 | 112 | quotes-b.jsonl:5189 | 76 / 54 | other-sentence — stored `Hindustani, Language Arabic Malay`, ladder `Table 6 Future locations and languages` | named |
| B29 | P-B-2018-79002-238b850f | ch8/g9 | 179 | quotes-b.jsonl:5278 | 111 / 109 | other-sentence — stored `k5 is the proportional coefficient`, ladder `speakers will in turn increase by` | named |
| B30 | P-B-2019-1908286-37248927 | ch11/g5 | 243 | quotes-b.jsonl:5491 | 64 / 60 | glued-token — ladder ends `proportion`, stored carries `proportion don` | named |
| B31 | P-B-2019-1908904-8b5a9e33 | ch9/g10 | 229 | quotes-b.jsonl:5588 | 50 / 44 | ladder-shorter — ladder ends `B(2 ×`, stored adds `MED1)` | named |
| B32 | P-B-2019-1924588-bd69a632 | ch9/g5 | 220 | quotes-b.jsonl:5928 | 42 / 38 | other-sentence — stored `represents the length of the path`, ladder `otherwise Team # 1924588 Page 19 of 29` | named |
| B33 | P-B-2020-2019696-961d6242 | ch8/g10 | 156 | quotes-b.jsonl:6533 | 94 / 44 | ladder-shorter — ladder ends `processed in problem 1`, stored adds `(RR= 0.64mm,rr= 0.20mm), it is concluded` | named |
| B34 | P-B-2020-2019696-961d6242 | ch9/g5 | 127 | quotes-b.jsonl:6542 | 99 / 99 | other-sentence — stored `thickness TT cut by the waves`, ladder `of waves on every point of the water-positive` | named |
| B35 | P-B-2020-2019696-961d6242 | ch9/g16 | 148 | quotes-b.jsonl:6553 | 245 / 136 | other-sentence — stored `SS2ii′ represents the area of the vertical`, ladder `represents the area of the vertical projection` | named |
| B36 | P-B-2021-2104673-da993d23 | ch6/g7 | 114 | quotes-b.jsonl:6809 | 96 / 91 | other-sentence — stored `In multiple-goods-condition, we consider`, ladder `integer programming problem. Therefore` | named |
| B37 | P-B-2021-2105363-52f891b1 | ch6/g13 | 81 | quotes-b.jsonl:6910 | 60 / 58 | other-sentence — stored `Figure 3 shows a detailed illustration`, ladder `i) is the number of fires` | named |
| B38 | P-B-2021-2105363-52f891b1 | ch6/g19 | 88 | quotes-b.jsonl:6916 | 78 / 57 | other-sentence — stored `dj(x, y) for the jth fire`, ladder `fire in the (x, y) region` | named |
| B39 | P-B-2021-2105363-52f891b1 | ch12/g8 | 285 | quotes-b.jsonl:7068 | 79 / 77 | other-sentence — stored `Figure 13: Sensitivity analysis`, ladder the axis run `60 0 400 800 1200 1600 2000 2400` | named |
| B40 | P-B-2021-2116496-6a60d0e7 | ch11/g3 | 214 | quotes-b.jsonl:7240 | 77 / 71 | head-skipped — stored starts `NEOC: the parameter`, ladder starts `the parameter` | named |
| B41 | P-B-2022-2207864-75af6d15 | ch6/g9 | 56 | quotes-b.jsonl:7826 | 118 / 112 | ladder-shorter — ladder ends `we know that:`, stored adds `( 4 )` | named |
| B42 | P-B-2022-2207864-75af6d15 | ch12/g1 | 202 | quotes-b.jsonl:7915 | 45 / 43 | other-sentence — stored `the water needs of the western United States`, ladder `meters of water would be needed` | named |
| B43 | P-B-2022-2213970-3f0a69d2 | ch7/g12 | 101 | quotes-b.jsonl:8080 | 249 / 154 | other-sentence — stored `Assume that the amount of water provided`, ladder `, then combined with the previous reservoir` | named |
| B44 | P-B-2022-2228168-d50f161d | ch6/g37 | 180 | quotes-b.jsonl:8234 | 79 / 77 | ladder-shorter — ladder ends `production effectiveness:`, stored adds `A` | named |
| B45 | P-B-2023-2315379-42733c7a | ch8/g27 | 96 | quotes-b.jsonl:8505 | 93 / 62 | ladder-shorter — ladder ends `approximate ecological value`, stored adds `��of different areas in Figure` | named |
| B46 | P-B-2024-2411570-f02ed036 | ch5/g6 | 105 | quotes-b.jsonl:8980 | 192 / 65 | head-skipped — stored starts `where zis the depth of the seawater`, ladder `the depth of the seawater` | named |
| B47 | P-B-2024-2411570-f02ed036 | ch6/g15 | 130 | quotes-b.jsonl:9001 | 165 / 63 | head-skipped — stored starts `where kis fluid resistance coefficient`, ladder `the flow velocity of the submersible` | named |
| B48 | P-B-2024-2411570-f02ed036 | ch6/g22 | 191 | quotes-b.jsonl:9008 | 196 / 153 | head-skipped — stored starts `where j, βis synonymous with i, α`, ladder `added mass` | named |
| B49 | P-B-2024-2411570-f02ed036 | ch10/g20 | 180 | quotes-b.jsonl:9054 | 55 / 45 | ladder-shorter — ladder ends `the area swept in`, stored adds `ttime as:` | named |
| B50 | P-B-2024-2419984-bb98b101 | ch7/g6 | 63 | quotes-b.jsonl:9144 | 179 / 110 | head-skipped — stored starts `where az represents the vertical acceleration`, ladder `is the buoyancy it experiences` | named |
| B51 | P-B-2024-2419984-bb98b101 | ch7/g24 | 82 | quotes-b.jsonl:9162 | 93 / 81 | head-skipped — stored starts `Re where Ax represents the area`, ladder `represents the area of the submersible` | named |
| B52 | P-B-2025-2501687-ce4f300c | ch7/g9 | 79 | quotes-b.jsonl:9539 | 168 / 141 | ladder-shorter — ladder ends `reasonable to simplify`, stored adds `f(t) as a cosine function:` | named |
| B53 | P-B-2025-2502617-613354d9 | ch7/g5 | 146 | quotes-b.jsonl:9712 | 96 / 95 | other-sentence — stored `better economic benefit of Juneau`, ladder `to sustainable tourism development` | named |
| B54 | P-B-2025-2502617-613354d9 | ch7/g12 | 154 | quotes-b.jsonl:9719 | 96 / 92 | other-sentence — stored `1.Proportion of Tourist(rglacier)`, ladder `statistics show that more than 60%` | named |
| B55 | P-B-2025-2502617-613354d9 | ch9/g4 | 172 | quotes-b.jsonl:9735 | 328 / 327 | other-sentence — stored `the sensitivity of tourists to price changes`, ladder `consumers view tourism expenses` | named |
| B56 | P-B-2025-2503268-228e0ec5 | ch1/g7 | 9 | quotes-b.jsonl:9763 | 162 / 145 | head-skipped — stored starts `Revenue factor (k6) had the strongest`, ladder `had the strongest direct effects` | named |
| B57 | P-B-2025-2503268-228e0ec5 | ch8/g9 | 95 | quotes-b.jsonl:9804 | 104 / 92 | other-sentence — stored `k4 quantifies the positive impact`, ladder `represents the natural growth rate` | named |
| B58 | P-B-2025-2503268-228e0ec5 | ch8/g25 | 115 | quotes-b.jsonl:9820 | 90 / 80 | other-sentence — stored `are inputs to the evaluation model`, ladder `based on different allocation patterns` | named |
| B59 | P-B-2025-2504448-aa644b6e | ch10/g5 | 157 | quotes-b.jsonl:9952 | 91 / 84 | other-sentence — stored `satisfaction decreases, subsidies`, ladder `government policies, with subsidies` | named |
| B60 | P-B-2025-2505199-bc9da82b | ch3/g2 | 29 | quotes-b.jsonl:10004 | 199 / 185 | label-dropped — stored starts `Explanations: Tourist consumption`, ladder `Tourist consumption` | named |
| B61 | P-B-2025-2505199-bc9da82b | ch3/g3 | 30 | quotes-b.jsonl:10005 | 101 / 87 | label-dropped — stored starts `Explanations: This simplifies`, ladder `This simplifies` | named |
| B62 | P-B-2025-2505199-bc9da82b | ch3/g5 | 32 | quotes-b.jsonl:10007 | 86 / 72 | label-dropped — stored starts `Explanations: It enables clear tracking`, ladder `It enables` | named |
| B63 | P-B-2025-2505199-bc9da82b | ch3/g6 | 33 | quotes-b.jsonl:10008 | 87 / 76 | label-dropped — stored starts `Assumption 5: Local infrastructure`, ladder `5: Local infrastructure` | named |
| B64 | P-B-2025-2505199-bc9da82b | ch3/g7 | 34 | quotes-b.jsonl:10009 | 87 / 82 | label-dropped — stored starts `Explanations: It clarifies the link`, ladder `bers, economic benefits, and living` | named |
| B65 | P-B-2025-2505199-bc9da82b | ch6/g13 | 66 | quotes-b.jsonl:10027 | 90 / 89 | other-sentence — stored `These costs mainly originate from the cleaning`, ladder `Waste disposal costs also have a linear` | named |
| B66 | P-B-2025-2505199-bc9da82b | ch6/g15 | 68 | quotes-b.jsonl:10029 | 183 / 179 | other-sentence — stored `tourism taxes and tourist fees set by policies`, ladder `The goal in the economic aspect` | named |
| B67 | P-B-2025-2505199-bc9da82b | ch10/g2 | 133 | quotes-b.jsonl:10077 | 84 / 78 | other-sentence — stored `Policies have dynamic impacts`, ladder `tourism market is dynamic` | named |
| B68 | P-B-2025-2505199-bc9da82b | ch10/g4 | 135 | quotes-b.jsonl:10079 | 132 / 129 | head-skipped — stored starts `In the future, relax model assumptions`, ladder `the future, relax model assumptions` | named |
| B69 | P-B-2025-2505199-bc9da82b | ch12/g5 | 152 | quotes-b.jsonl:10094 | 147 / 139 | label-dropped — stored starts `Tourist Number Limitation:`, ladder `Number Limitation:` | named |
| B70 | P-B-2025-2505199-bc9da82b | ch12/g8 | 155 | quotes-b.jsonl:10097 | 130 / 123 | label-dropped — stored starts `Policy - making:`, ladder `- making:` | named |
| B71 | P-B-2025-2505199-bc9da82b | ch12/g9 | 156 | quotes-b.jsonl:10098 | 138 / 130 | label-dropped — stored starts `Revenue Allocation:`, ladder `Allocation:` | named |
| B72 | P-B-2025-2509557-c800a325 | ch4/g4 | 41 | quotes-b.jsonl:10113 | 69 / 64 | ladder-shorter — list `2002, 2006, 2021, 2022,` stops before `2023` | named |
| B73 | P-B-2025-2517929-c19deeac | ch7/g8 | 78 | quotes-b.jsonl:10240 | 89 / 50 | ladder-shorter — ladder ends `whale watching area, and`, stored adds `i=3 refers to the tropical rainforest.` | named |
| B74 | P-B-2025-2517929-c19deeac | ch11/g9 | 171 | quotes-b.jsonl:10313 | 245 / 235 | other-sentence — stored `+10753875 For the degree of environmental damage`, ladder `For the degree of environmental damage` | named |
| B75 | P-B-2025-2517929-c19deeac | ch11/g11 | 174 | quotes-b.jsonl:10315 | 99 / 90 | other-sentence — stored `solutions and conducted a sensitivity analysis`, ladder `In response, we still used the NSGA - II method` | named |
| B76 | P-B-2025-2517929-c19deeac | ch13/g7 | 196 | quotes-b.jsonl:10332 | 68 / 62 | other-sentence — stored `Collect opinions on infrastructure construction`, ladder `Annual statistics of the number of tourists` | named |

### C lane (59)

| id | paper | ch/group | block | L7 file:line | stored/ladder chars | cause | status |
|---|---|---|---|---|---|---|---|
| C01 | P-C-2010-7812-c2fa13fd | ch1/g5 | 7 | quotes-c.jsonl:53 | 57 / 56 | other-sentence — stored `simply referred as “Plastic”`, ladder `uses the North Pacific Central` | named |
| C02 | P-C-2010-7812-c2fa13fd | ch2/g2 | 9 | quotes-c.jsonl:55 | 55 / 51 | other-sentence — stored `coefficient matrix for this model`, ladder `Also, the types of plastic` | named |
| C03 | P-C-2010-7812-c2fa13fd | ch2/g6 | 19 | quotes-c.jsonl:59 | 56 / 52 | other-sentence — stored `AOI is defined as “Outside Area”`, ladder `from OA to AOI and the output` | named |
| C04 | P-C-2010-7812-c2fa13fd | ch2/g10 | 24 | quotes-c.jsonl:63 | 59 / 58 | other-sentence — stored `transformation of an individual object`, ladder `plastic objects are important` | named |
| C05 | P-C-2010-7812-c2fa13fd | ch2/g19 | 48 | quotes-c.jsonl:72 | 61 / 58 | other-sentence — stored `of an initial object will decay`, ladder `the rate of input, the rate of` | named |
| C06 | P-C-2010-7812-c2fa13fd | ch2/g21 | 50 | quotes-c.jsonl:74 | 61 / 59 | other-sentence — stored `3 is the sum of the rate of input`, ladder `of Level 1 and 2, the rate of` | named |
| C07 | P-C-2010-7812-c2fa13fd | ch2/g23 | 52 | quotes-c.jsonl:76 | 58 / 55 | other-sentence — stored `of total input minus the rate`, ladder `Regarding the four size levels` | named |
| C08 | P-C-2010-7812-c2fa13fd | ch3/g9 | 72 | quotes-c.jsonl:89 | 57 / 56 | other-sentence — stored `this model assumes the entire`, ladder `due to photolysis process` | named |
| C09 | P-C-2010-7812-c2fa13fd | ch3/g10 | 73 | quotes-c.jsonl:90 | 57 / 55 | other-sentence — stored `levels m=100 yrs. This estimate`, ladder `r2=1%. Then let time interval` | named |
| C10 | P-C-2010-7812-c2fa13fd | ch3/g11 | 74 | quotes-c.jsonl:91 | 61 / 52 | other-sentence — stored `(justified in “The Effect of P`, ladder `r2=6.9%. A rough range of decay` | named |
| C11 | P-C-2010-7812-c2fa13fd | ch5/g9 | 111 | quotes-c.jsonl:110 | 57 / 52 | other-sentence — stored `photolysis rate increases while`, ladder `Of all size level plastics` | named |
| C12 | P-C-2010-7812-c2fa13fd | ch7/g4 | 125 | quotes-c.jsonl:118 | 59 / 52 | other-sentence — stored `mass concentration in all size`, ladder `Based on Figure 2, 3, and 4` | named |
| C13 | P-C-2010-7812-c2fa13fd | ch7/g5 | 127 | quotes-c.jsonl:119 | 57 / 56 | other-sentence — stored `governments to use regulations`, ladder `plastics in all levels in all` | named |
| C14 | P-C-2010-7812-c2fa13fd | ch7/g6 | 128 | quotes-c.jsonl:120 | 58 / 57 | other-sentence — stored `classified plastic system in the`, ladder `inputs constant, the mass concentration` | named |
| C15 | P-C-2010-7812-c2fa13fd | ch7/g7 | 130 | quotes-c.jsonl:121 | 59 / 57 | other-sentence — stored `that once inputs reduced`, ladder `to rise again in long-term` | named |
| C16 | P-C-2011-10607-6ed4fd93 | ch4/g23 | 116 | quotes-c.jsonl:237 | 55 / 49 | ladder-shorter — ladder ends `an obtain`, stored adds `q` | named |
| C17 | P-C-2011-9089-838e50df | ch4/g1 | 8 | quotes-c.jsonl:616 | 69 / 66 | ladder-shorter — ladder ends `equation:[3]`, stored adds `dN` | named |
| C18 | P-C-2011-9089-838e50df | ch4/g11 | 29 | quotes-c.jsonl:626 | 50 / 47 | ladder-shorter — ladder ends `[1] NOx`, stored adds `CO` | named |
| C19 | P-C-2011-9089-838e50df | ch4/g43 | 96 | quotes-c.jsonl:658 | 103 / 101 | ladder-shorter — ladder ends `normalized data are:`, stored keeps the trailing space run | named |
| C20 | P-C-2011-9089-838e50df | ch4/g48 | 101 | quotes-c.jsonl:663 | 118 / 113 | head-skipped — stored starts `sumt Constraints are as follows`, ladder `Constraints are as follows` | named |
| C21 | P-C-2012-12218-14ded715 | ch4/g2 | 36 | quotes-c.jsonl:710 | 53 / 46 | other-sentence — stored `be a supergraph corresponding`, ladder `is the set of superedges [5]` | named |
| C22 | P-C-2014-28199-d39873d7 | ch4/g19 | 57 | quotes-c.jsonl:1688 | 64 / 44 | other-sentence — stored `the population mean Ωi(v)`, ladder `It can be easily proved that` | named |
| C23 | P-C-2014-30221-7af27341 | ch4/g68 | 103 | quotes-c.jsonl:1984 | 58 / 54 | other-sentence — stored `Citation 1 Watts1998`, ladder `Table 10: Most Influential Papers` | named |
| C24 | P-C-2014-31262-1f9007fa | ch4/g43 | 65 | quotes-c.jsonl:2097 | 41 / 35 | ladder-shorter — ladder ends `(13) and (14):`, stored adds `n (1)` | named |
| C25 | P-C-2014-31262-1f9007fa | ch4/g45 | 67 | quotes-c.jsonl:2099 | 57 / 48 | ladder-shorter — ladder ends `the definition of`, stored adds `Bs(P): T` | named |
| C26 | P-C-2015-33572-b32fb4b1 | ch4/g35 | 104 | quotes-c.jsonl:2231 | 139 / 127 | head-skipped — stored starts `where x ∈X; LL denotes the set`, ladder `LL denotes the set of leaved` | named |
| C27 | P-C-2015-33572-b32fb4b1 | ch5/g17 | 206 | quotes-c.jsonl:2313 | 151 / 82 | head-skipped — stored starts `x∈M where AbO stands for`, ladder `denotes the productivity of` | named |
| C28 | P-C-2015-37075-1d95d60d | ch3/g20 | 62 | quotes-c.jsonl:2635 | 47 / 33 | head-skipped — stored starts `Γ(t): the set of people who work`, ladder `the set of people who work` | named |
| C29 | P-C-2015-37075-1d95d60d | ch5/g15 | 159 | quotes-c.jsonl:2694 | 83 / 67 | other-sentence — stored `less inefficiently, leading to`, ladder `An individual more unsatisfied` | named |
| C30 | P-C-2015-37284-dee063ba | ch2/g5 | 22 | quotes-c.jsonl:2778 | 59 / 45 | head-skipped — stored starts `(V,E), whereV is the set of nodes`, ladder `is the set of nodes and E is` | named |
| C31 | P-C-2015-39160-2b8963a3 | ch2/g14 | 41 | quotes-c.jsonl:2961 | 54 / 50 | head-skipped — stored begins `n an office of four positions`, ladder `an office of four positions … every o` (one-char shift at both ends) | named |
| C32 | P-C-2016-42939-5fccbebc | ch4/g34 | 126 | quotes-c.jsonl:3143 | 64 / 58 | ladder-shorter — ladder ends `Variables`, stored adds `fROIi` | named |
| C33 | P-C-2016-42939-5fccbebc | ch6/g7 | 161 | quotes-c.jsonl:3173 | 72 / 70 | ladder-shorter — ladder ends `as follows:`, stored adds `F` | named |
| C34 | P-C-2016-47823-59d82231 | ch8/g11 | 227 | quotes-c.jsonl:3322 | 132 / 130 | head-skipped — stored starts `x k is the solution of NO.k`, ladder `k is the solution of NO.k` | named |
| C35 | P-C-2016-50193-615bc62f | ch4/g29 | 227 | quotes-c.jsonl:3421 | 52 / 38 | head-skipped — stored starts `where X(1)(k) is formed as the following`, ladder `is formed as the following formula k X` | named |
| C36 | P-C-2018-78577-919f0d0f | ch5/g27 | 187 | quotes-c.jsonl:4439 | 115 / 113 | head-skipped — stored starts `) satisfy all the rules`, ladder `satisfy all the rules` | named |
| C37 | P-C-2019-1906204-4e0a421c | ch8/g20 | 210 | quotes-c.jsonl:5300 | 77 / 66 | ladder-shorter — ladder ends `calculated as,`, stored adds `NewTotal =` | named |
| C38 | P-C-2019-1922154-b7129095 | ch4/g32 | 100 | quotes-c.jsonl:5374 | 77 / 65 | ladder-shorter — ladder ends `in the nth year,`, stored adds `ri n is the` | named |
| C39 | P-C-2020-2002116-f6f4a15a | ch4/g30 | 99 | quotes-c.jsonl:5541 | 161 / 86 | other-sentence — stored `SI(ci, Gj) ∈(0, 1] measures the similarity of`, ladder `group of the sentimental seed words` | named |
| C40 | P-C-2020-2010638-c32c8549 | ch4/g23 | 83 | quotes-c.jsonl:6241 | 101 / 95 | other-sentence — stored `represents a series of independent variables`, ladder `is a binomial distribution parameter` | named |
| C41 | P-C-2020-2010638-c32c8549 | ch4/g52 | 118 | quotes-c.jsonl:6270 | 46 / 42 | ladder-shorter — ladder ends `of each index, use`, stored adds `Q -` | named |
| C42 | P-C-2020-2010638-c32c8549 | ch5/g46 | 190 | quotes-c.jsonl:6340 | 104 / 102 | head-skipped — stored starts `) Hair Dryer 0.126`, ladder `Hair Dryer 0.126` | named |
| C43 | P-C-2021-2101166-038bd4c8 | ch4/g34 | 89 | quotes-c.jsonl:6423 | 61 / 57 | ladder-shorter — ladder ends `probability vector`, stored adds `Pi;` | named |
| C44 | P-C-2021-2101166-038bd4c8 | ch4/g45 | 100 | quotes-c.jsonl:6434 | 63 / 51 | ladder-shorter — ladder ends `Based on Auto-`, stored adds `Encoder and` | named |
| C45 | P-C-2021-2107815-45f0e8ba | ch4/g87 | 176 | quotes-c.jsonl:6844 | 197 / 179 | other-sentence — stored `“Notes”_10 positive-ID 0.865896285`, ladder `“Notes”_6 unknown 0.5` | named |
| C46 | P-C-2021-2107815-45f0e8ba | ch5/g45 | 251 | quotes-c.jsonl:6917 | 93 / 89 | other-sentence — stored `Results Confidence Results Confidence data_1`, ladder `Table.6-4 Partial Unverified Data Prediction` | named |
| C47 | P-C-2021-2109298-1a718172 | ch4/g39 | 75 | quotes-c.jsonl:7204 | 64 / 58 | other-sentence — stored `weight of transition probability`, ladder `the softmax function is utilized` | named |
| C48 | P-C-2021-2109298-1a718172 | ch4/g48 | 84 | quotes-c.jsonl:7213 | 180 / 151 | other-sentence — stored `its daily activity range is about 10`, ladder `one CA update represents` | named |
| C49 | P-C-2021-2109298-1a718172 | ch4/g85 | 164 | quotes-c.jsonl:7250 | 94 / 73 | other-sentence — stored `representing the discredibility o`, ladder `is the location of a historical report` | named |
| C50 | P-C-2021-2123823-dddc6e65 | ch6/g32 | 160 | quotes-c.jsonl:7396 | 59 / 51 | ladder-shorter — ladder ends `distribution of G1’s`, stored adds `Pn(Pos)` | named |
| C51 | P-C-2021-2123823-dddc6e65 | ch8/g8 | 204 | quotes-c.jsonl:7424 | 93 / 76 | head-skipped — stored starts `in which Weight3 means the weight`, ladder `means the weight of the third factor` | named |
| C52 | P-C-2024-2401298-07d37078 | ch8/g9 | 168 | quotes-c.jsonl:9254 | 85 / 85 | other-sentence — stored `To further clarify the counterintuitive increase`, ladder `our investigation delved into the patterns` | named |
| C53 | P-C-2024-2401298-07d37078 | ch9/g3 | 200 | quotes-c.jsonl:9260 | 58 / 54 | head-skipped — stored starts `(b) Figure 16:`, ladder `Figure 16:` | named |
| C54 | P-C-2024-2401298-07d37078 | ch12/g1 | 189 | quotes-c.jsonl:9269 | 87 / 83 | other-sentence — stored `This framework can be instantiated into models`, ladder `it into a more abstract and comprehensive form` | named |
| C55 | P-C-2024-2401445-6a882749 | ch5/g1 | 46 | quotes-c.jsonl:9297 | 54 / 48 | head-skipped — stored starts `Table 1: Summary of Key Symbols`, ladder `1: Summary of Key Symbols` | named |
| C56 | P-C-2024-2401445-6a882749 | ch8/g8 | 164 | quotes-c.jsonl:9322 | 77 / 69 | other-sentence — stored `Additionally, compared to the originally label`, ladder `Status Precision Recall F1-Score Support` | named |
| C57 | P-C-2024-2409404-a8d6763a | ch6/g7 | 113 | quotes-c.jsonl:9531 | 67 / 57 | ladder-shorter — ladder carries stray `5` at head, ends `Based on`, stored adds `PCA&XGBoost` | named |
| C58 | P-C-2025-2503389-d13d77af | ch7/g12 | 175 | quotes-c.jsonl:9819 | 151 / 149 | ladder-shorter — ladder ends `aligned with its`, stored adds `:` | named |
| C59 | P-C-2025-2507817-87c90f39 | ch7/g3 | 146 | quotes-c.jsonl:9913 | 65 / 45 | other-sentence — stored `5.2.3 Predicting progress and regressions`, ladder `Figure 10 Error bar chart of prediction model` | named |

### D lane (40)

| id | paper | ch/group | block | L7 file:line | stored/ladder chars | cause | status |
|---|---|---|---|---|---|---|---|
| D01 | P-D-2016-42220-7261f9d3 | ch4/g3 | 80 | quotes-d.jsonl:150 | 66 / 64 | ladder-shorter — ladder ends `node vector`, stored adds `(` | named |
| D02 | P-D-2017-55295-9001b6d9 | ch3/g6 | 59 | quotes-d.jsonl:306 | 92 / 56 | ladder-shorter — ladder ends `Arrving time`, stored adds `interval(min) 0 0.1 0.2` | named |
| D03 | P-D-2018-73156-1a30e830 | ch5/g63 | 121 | quotes-d.jsonl:737 | 87 / 73 | head-skipped — stored starts `ac,ab,bc 0 4.4 Logistic model`, ladder `4.4 Logistic model` | named |
| D04 | P-D-2018-73156-1a30e830 | ch6/g5 | 142 | quotes-d.jsonl:774 | 67 / 40 | head-skipped — stored starts `Let ( y) (x x) axx , we can get`, ladder `, we can get the lag index` | named |
| D05 | P-D-2018-82504-6cc63169 | ch5/g3 | 33 | quotes-d.jsonl:1173 | 63 / 61 | other-sentence — stored `an index concerning about population density`, ladder `v average number of vehicles per capita` | named |
| D06 | P-D-2019-1902407-b8153b5d | ch6/g17 | 35 | quotes-d.jsonl:1600 | 47 / 71 | other-sentence — stored `for a fixed amount, therefore we should shorten`, ladder `In a known congestion paths,VS′,Li and Vs` | named |
| D07 | P-D-2019-1902407-b8153b5d | ch6/g23 | 42 | quotes-d.jsonl:1606 | 89 / 81 | head-skipped — stored starts `(4 −25) The algorithm for scheduling`, ladder `The algorithm for scheduling` | named |
| D08 | P-D-2019-1922074-a699b77f | ch5/g21 | 136 | quotes-d.jsonl:1846 | 38 / 36 | ladder-shorter — ladder ends `as a topology`, stored adds `G` | named |
| D09 | P-D-2020-2013140-d02fd0c3 | ch5/g15 | 55 | quotes-d.jsonl:2319 | 63 / 61 | ladder-shorter — ladder ends `in formula 2:`, stored adds `x` | named |
| D10 | P-D-2020-2013140-d02fd0c3 | ch5/g37 | 81 | quotes-d.jsonl:2341 | 63 / 54 | other-sentence — stored `time 15:00 30:00 90:00 Tactical Tiki-`, ladder `Table 3 Tactical Changes in Game 15` | named |
| D11 | P-D-2020-2015044-db9655c7 | ch5/g5 | 129 | quotes-d.jsonl:2529 | 89 / 85 | other-sentence — stored `distribution importance score for match m`, ladder `measures the importance of player i` | named |
| D12 | P-D-2020-2022868-71331b90 | ch3/g7 | 42 | quotes-d.jsonl:2584 | 72 / 70 | ladder-shorter — ladder ends `Players Input`, stored adds `(` | named |
| D13 | P-D-2021-2100112-1b2d1f1c | ch8/g8 | 149 | quotes-d.jsonl:2742 | 51 / 45 | head-skipped — stored starts `David Bowie 7.232`, ladder `Bowie 7.232` | named |
| D14 | P-D-2021-2100112-1b2d1f1c | ch8/g12 | 174 | quotes-d.jsonl:2746 | 87 / 68 | ladder-shorter — ladder ends `1950 1964 1979`, stored adds `- - - - 1947 - - -` | named |
| D15 | P-D-2021-2100242-a505be5b | ch5/g36 | 168 | quotes-d.jsonl:2833 | 48 / 45 | ladder-shorter — ladder ends `genre k2`, stored adds `is` | named |
| D16 | P-D-2021-2101855-c4682962 | ch5/g11 | 68 | quotes-d.jsonl:2941 | 83 / 83 | other-sentence — stored `fluence of music unbiasedly`, ladder `musician among his/her contemporaries`; stored is in no block of the group (`stored_in_block` false) | named |
| D17 | P-D-2021-2101855-c4682962 | ch11/g5 | 220 | quotes-d.jsonl:3036 | 86 / 86 | other-sentence — stored `ness of our measure. Case studies`, ladder `influence and similarity as well as how` | named |
| D18 | P-D-2021-2107091-7ebae97f | ch6/g19 | 104 | quotes-d.jsonl:3212 | 56 / 48 | ladder-shorter — ladder ends `Music Similarity`, stored adds `Evalua-` | named |
| D19 | P-D-2021-2107091-7ebae97f | ch7/g21 | 175 | quotes-d.jsonl:3272 | 80 / 73 | ladder-shorter — ladder ends `interplay of`, stored adds `genres` | named |
| D20 | P-D-2021-2107091-7ebae97f | ch8/g6 | 257 | quotes-d.jsonl:3299 | 87 / 84 | ladder-shorter — ladder ends `step size may lead`, stored adds `to` | named |
| D21 | P-D-2021-2124668-12f9e4f1 | ch6/g63 | 130 | quotes-d.jsonl:3612 | 62 / 54 | ladder-shorter — ladder ends `adjusted for chance to`, stored adds `obtain:` | named |
| D22 | P-D-2021-2124668-12f9e4f1 | ch7/g37 | 233 | quotes-d.jsonl:3657 | 90 / 76 | head-skipped — stored starts `Mainstreaming Electronic Revolution`, ladder `Electronic Revolution in the 2000s` | named |
| D23 | P-D-2022-2215444-cd948920 | ch6/g16 | 61 | quotes-d.jsonl:3842 | 78 / 63 | other-sentence — stored `Finally, based on the judgment matrix`, ladder `sents the number of indicators` | named |
| D24 | P-D-2024-2417004-a737e95b | ch8/g6 | 213 | quotes-d.jsonl:4502 | 87 / 82 | other-sentence — stored `hydrological, and ecological factors`, ladder `3 Complexity due to Multiple Variables` | named |
| D25 | P-D-2024-2419588-1cc62ede | ch4/g1 | 26 | quotes-d.jsonl:4656 | 47 / 45 | other-sentence — stored `Lake Michigan and Lake Huron are referred`, ladder `In our paper, Lake Superior is referred` | named |
| D26 | P-D-2024-2419588-1cc62ede | ch5/g3 | 33 | quotes-d.jsonl:4661 | 58 / 51 | other-sentence — stored `Every river connecting two lakes`, ladder `with the flow rate from lake i` | named |
| D27 | P-D-2024-2419588-1cc62ede | ch5/g55 | 113 | quotes-d.jsonl:4713 | 140 / 135 | ladder-shorter — ladder ends `water level management discuss`, stored `di` | named |
| D28 | P-D-2024-2419588-1cc62ede | ch9/g5 | 202 | quotes-d.jsonl:4764 | 84 / 83 | other-sentence — stored `resource management in the Great Lakes region, contributing`, ladder `that our approach can become a more robust` | named |
| D29 | P-D-2024-2429211-de10f571 | ch4/g5 | 62 | quotes-d.jsonl:4796 | 65 / 63 | other-sentence — stored `More formally, the dynamic flow problem`, ladder `The goal is to find the min-cost flow` | named |
| D30 | P-D-2024-2429211-de10f571 | ch5/g3 | 146 | quotes-d.jsonl:4853 | 49 / 45 | other-sentence — stored `linear program using the historic rain level`, ladder `After obtaining these rain values` | named |
| D31 | P-D-2025-2507692-249f88dd | ch6/g11 | 85 | quotes-d.jsonl:5015 | 673 / 104 | other-sentence — stored is a sparse glyph run of 673 chars of repeated `m`, ladder takes the prose head `5 Model II: Upgraded Bus Network Model` | named |
| D32 | P-D-2025-2516219-17e4e820 | ch1/g2 | 6 | quotes-d.jsonl:5079 | 165 / 130 | head-skipped — stored starts `multimodal network model (GM = (N, E, M))`, ladder `E, M)) is proposed to evaluate` | named |
| D33 | P-D-2025-2516219-17e4e820 | ch5/g3 | 54 | quotes-d.jsonl:5106 | 85 / 56 | head-skipped — stored starts `Daily_Traffic_Baltimore.csv, assume a data set`, ladder `assume a data set` | named |
| D34 | P-D-2025-2516219-17e4e820 | ch6/g8 | 72 | quotes-d.jsonl:5115 | 85 / 73 | other-sentence — stored `balance across transportation nodes`, ladder `where Cij corresponds to the theoretical maximum` | named |
| D35 | P-D-2025-2516219-17e4e820 | ch6/g19 | 140 | quotes-d.jsonl:5126 | 88 / 73 | head-skipped — stored starts `ing edge eb ij is defined`, ladder `is defined as a composite function` | named |
| D36 | P-D-2025-2516219-17e4e820 | ch6/g24 | 148 | quotes-d.jsonl:5131 | 88 / 69 | ladder-shorter — ladder ends `generalized cost`, stored adds `cm od, travel time` | named |
| D37 | P-D-2025-2516219-17e4e820 | ch6/g34 | 181 | quotes-d.jsonl:5141 | 87 / 84 | other-sentence — stored `experience revenue variations through pedestrian`, ladder `with δ = 0.96 reflecting Maryland's` | named |
| D38 | P-D-2025-2516219-17e4e820 | ch6/g37 | 187 | quotes-d.jsonl:5144 | 151 / 135 | head-skipped — stored starts `where κ ∼U[0.3, 0.6] captures`, ladder `0.6] captures stochastic lane closure` | named |
| D39 | P-D-2025-2516219-17e4e820 | ch7/g36 | 207 | quotes-d.jsonl:5185 | 87 / 80 | head-skipped — stored starts `Figure 12: Temporal Capacity Degradation`, ladder `12: Temporal Capacity Degradation` | named |
| D40 | P-D-2025-2519935-f07f7c47 | ch2/g1 | 13 | quotes-d.jsonl:5199 | 1397 / 89 | other-sentence — stored is a 1,397-char sparse run of repeated `m`, ladder takes the prose head `which affects both residents and businesses` | named |

### E lane (27)

| id | paper | ch/group | block | L7 file:line | stored/ladder chars | cause | status |
|---|---|---|---|---|---|---|---|
| E01 | P-E-2017-61502-f0a50d47 | ch1/g1 | 4 | quotes-e.jsonl:426 | 121 / 115 | other-sentence — stored `incorporated all ten principles into five unique metrics`, ladder `index that is capable of grading a city's smart growth` | named |
| E02 | P-E-2017-65123-e36461ec | ch6/g44 | 234 | quotes-e.jsonl:618 | 61 / 58 | head-skipped — stored starts `th year population of this city`, ladder `year population of this city` | named |
| E03 | P-E-2017-68242-753e0037 | ch4/g31 | 180 | quotes-e.jsonl:783 | 101 / 96 | head-skipped — stored starts `imin And we can have the method`, ladder `And we can have the method` | named |
| E04 | P-E-2018-88902-cefa4db9 | ch7/g46 | 236 | quotes-e.jsonl:1550 | 66 / 53 | other-sentence — stored `Provide farmers with support on Fertilizer`, ladder `Tractor use to increase yield by 10` | named |
| E05 | P-E-2018-89499-90bc677f | ch6/g13 | 75 | quotes-e.jsonl:1607 | 97 / 84 | other-sentence — stored is a table header run `Per capita renewable Cereal Prevalence`, ladder `between climatic indicators and some social-economic` | named |
| E06 | P-E-2018-89499-90bc677f | ch6/g25 | 88 | quotes-e.jsonl:1619 | 97 / 77 | other-sentence — stored `Per capita renewable inland Cereal Prevalence`, ladder `Applying the Gray Relational Analysis to Egypt` | named |
| E07 | P-E-2019-1902029-f44b44ca | ch10/g1 | 264 | quotes-e.jsonl:1858 | 44 / 38 | ladder-shorter — ladder ends `The value of the`, stored adds `world` | named |
| E08 | P-E-2019-1903455-a52f7980 | ch5/g17 | 61 | quotes-e.jsonl:2088 | 73 / 68 | ladder-shorter — ladder ends `of each size,`, stored adds `max(` | named |
| E09 | P-E-2019-1903455-a52f7980 | ch5/g18 | 62 | quotes-e.jsonl:2089 | 63 / 61 | ladder-shorter — ladder ends `of the evaluation indicator`, stored adds `X` | named |
| E10 | P-E-2019-1903455-a52f7980 | ch5/g29 | 74 | quotes-e.jsonl:2100 | 105 / 103 | head-skipped — stored starts `i means the average of the index i`, ladder `means the average of the index i` | named |
| E11 | P-E-2019-1903455-a52f7980 | ch7/g21 | 155 | quotes-e.jsonl:2162 | 84 / 82 | head-skipped — stored starts `1 where B is the benefit`, ladder `where B is the benefit` | named |
| E12 | P-E-2019-1916129-cfc06e89 | ch5/g11 | 50 | quotes-e.jsonl:2215 | 64 / 57 | other-sentence — stored `are respectively the amount of oxygen released`, ladder `is the value of fixed carbon dioxide` | named |
| E13 | P-E-2019-1916129-cfc06e89 | ch5/g26 | 76 | quotes-e.jsonl:2230 | 64 / 50 | other-sentence — stored `respectively represent the amount of cyanide`, ladder `is the difference of COD above the standard value` | named |
| E14 | P-E-2020-2008521-e040e3b4 | ch5/g15 | 55 | quotes-e.jsonl:2329 | 61 / 60 | other-sentence — stored `existing plastics in the ocean,`, ladder `existing plastics in the soil,` (one noun substituted) | named |
| E15 | P-E-2020-2016287-6ed5334f | ch5/g47 | 176 | quotes-e.jsonl:2634 | 81 / 79 | ladder-shorter — ladder ends `Indicators Brief explanation`, stored adds `x` | named |
| E16 | P-E-2020-2021103-996a6655 | ch4/g50 | 132 | quotes-e.jsonl:2920 | 149 / 149 | other-sentence — stored `for each of the four income classes (k ∈{1, 2, 3, 4})`, ladder `then this country should be left untouched by the global policy` | named |
| E17 | P-E-2021-2113869-a6c9c257 | ch1/g3 | 5 | quotes-e.jsonl:3019 | 80 / 78 | other-sentence — stored `based on the principle of minimizing the transportation cost`, ladder `issues, in which countries of food surplus will subsidize` | named |
| E18 | P-E-2022-2203489-75977cc9 | ch6/g7 | 217 | quotes-e.jsonl:3404 | 69 / 51 | other-sentence — stored `the model, and the obtained optimal thinning intensity`, ladder `based on the average of the collected and sold mar-` | named |
| E19 | P-E-2022-2203489-75977cc9 | ch6/g10 | 228 | quotes-e.jsonl:3407 | 44 / 40 | other-sentence — stored `The total forest area in Canada is 3,470,000`, ladder `so we can divide it into 428 grids of 90` | named |
| E20 | P-E-2022-2218144-2f85ee8c | ch7/g13 | 83 | quotes-e.jsonl:3586 | 46 / 44 | ladder-shorter — ladder ends `local optimal solutions F`, stored adds `X` | named |
| E21 | P-E-2022-2223269-9c9b5216 | ch6/g25 | 110 | quotes-e.jsonl:3721 | 74 / 70 | head-skipped — stored starts `The 0-1 value constraint`, ladder `0-1 value constraint` | named |
| E22 | P-E-2023-2308000-0f85170c | ch6/g2 | 66 | quotes-e.jsonl:4062 | 69 / 51 | head-skipped — stored starts with the page footer `P a g e 7 o f 2 5`, ladder `4.1 Reorganizing index` | named |
| E23 | P-E-2023-2308000-0f85170c | ch7/g3 | 112 | quotes-e.jsonl:4089 | 81 / 62 | other-sentence — stored `Based on the data collected from authoritative literatures`, ladder `we have sorted out important data (parts)` | named |
| E24 | P-E-2024-2400860-84b8e466 | ch9/g13 | 187 | quotes-e.jsonl:4448 | 63 / 51 | head-skipped — stored starts `Ultimately, our building impact score`, ladder `our building impact score` | named |
| E25 | P-E-2024-2410578-d7df14d8 | ch6/g4 | 54 | quotes-e.jsonl:4654 | 58 / 53 | other-sentence — stored `Then the normalized information distribution is applied`, ladder `It means the number of sample points` | named |
| E26 | P-E-2024-2410578-d7df14d8 | ch6/g5 | 56 | quotes-e.jsonl:4655 | 76 / 66 | ladder-shorter — ladder ends `single year profit formula for`, stored adds `insurance` | named |
| E27 | P-E-2025-2515136-5dd4cae6 | ch3/g4 | 34 | quotes-e.jsonl:4958 | 276 / 70 | head-skipped — stored drops `⋆Assumption 3: After the crop` and appends a 200-char glyph run of repeated `m`; ladder keeps the sentence head | named |

### F lane (45)

| id | paper | ch/group | block | L7 file:line | stored/ladder chars | cause | status |
|---|---|---|---|---|---|---|---|
| F01 | P-F-2016-44348-d3da2a69 | ch6/g6 | 152 | quotes-f.jsonl:194 | 105 / 100 | head-skipped — stored starts `w1i, (i = 1, 2, 3)`, ladder `(i = 1, 2, 3)` | named |
| F02 | P-F-2016-44348-d3da2a69 | ch6/g9 | 155 | quotes-f.jsonl:197 | 156 / 154 | ladder-shorter — ladder ends `the expression is: π =`, stored adds `N` | named |
| F03 | P-F-2016-44348-d3da2a69 | ch6/g25 | 172 | quotes-f.jsonl:213 | 222 / 220 | ladder-shorter — ladder ends `is defined as:`, stored adds `N` | named |
| F04 | P-F-2018-87280-fa7e05e4 | ch3/g20 | 63 | quotes-f.jsonl:1025 | 101 / 87 | ladder-shorter — ladder ends `(C.I.), CI`, stored adds `= max n n 1` | named |
| F05 | P-F-2018-87280-fa7e05e4 | ch3/g42 | 87 | quotes-f.jsonl:1047 | 79 / 65 | ladder-shorter — ladder ends `Expected value of income,`, stored adds `Correlation` | named |
| F06 | P-F-2018-88508-de947611 | ch6/g19 | 143 | quotes-f.jsonl:1250 | 74 / 67 | ladder-shorter — ladder ends `the value`, stored adds `s is:` | named |
| F07 | P-F-2019-1905127-b4a0bea2 | ch7/g5 | 82 | quotes-f.jsonl:1664 | 253 / 125 | other-sentence — stored `importing country, respectively. The exchange rate`, ladder `so the total profits of the firms using the currencies` | named |
| F08 | P-F-2019-1905127-b4a0bea2 | ch7/g15 | 96 | quotes-f.jsonl:1674 | 76 / 70 | ladder-shorter — ladder ends `Money supply is expressed`, stored adds `as: M` | named |
| F09 | P-F-2019-1905127-b4a0bea2 | ch10/g3 | 152 | quotes-f.jsonl:1706 | 53 / 49 | ladder-shorter — ladder ends `the exchange rate of the`, stored adds `dig` | named |
| F10 | P-F-2019-1916375-d9b69c90 | ch5/g5 | 77 | quotes-f.jsonl:1761 | 92 / 90 | head-skipped — stored starts `2 Now we define a function`, ladder `Now we define a function` | named |
| F11 | P-F-2019-1916375-d9b69c90 | ch7/g15 | 116 | quotes-f.jsonl:1791 | 134 / 132 | ladder-shorter — ladder ends `respectively, they are`, stored adds `C` | named |
| F12 | P-F-2019-1916375-d9b69c90 | ch7/g19 | 122 | quotes-f.jsonl:1795 | 47 / 45 | ladder-shorter — ladder ends `the weight of`, stored adds `R` | named |
| F13 | P-F-2019-1916704-dd8d036e | ch8/g14 | 186 | quotes-f.jsonl:1953 | 57 / 45 | ladder-shorter — ladder ends `measures the law`, stored adds `enforcement` | named |
| F14 | P-F-2020-2005623-fc75252e | ch5/g10 | 85 | quotes-f.jsonl:2051 | 80 / 69 | ladder-shorter — ladder ends `and the year t`, stored adds `−1: S(t) =` | named |
| F15 | P-F-2020-2006291-c876ce05 | ch7/g2 | 82 | quotes-f.jsonl:2166 | 78 / 64 | other-sentence — stored `Table.1: Eight Indicators For Analysis`, ladder `environment B4 Precipitation B5 Location A3` | named |
| F16 | P-F-2020-2013233-f7fd24e3 | ch4/g4 | 70 | quotes-f.jsonl:2461 | 80 / 69 | other-sentence — stored interleaves two table columns `Proportion of land Terrain Annual sea level`, ladder the second column run | named |
| F17 | P-F-2020-2013233-f7fd24e3 | ch7/g12 | 132 | quotes-f.jsonl:2513 | 39 / 36 | ladder-shorter — ladder ends `SS =`, stored adds `BS` | named |
| F18 | P-F-2020-2013233-f7fd24e3 | ch9/g16 | 197 | quotes-f.jsonl:2570 | 66 / 64 | ladder-shorter — ladder ends `protection index as:`, stored adds `C` | named |
| F19 | P-F-2020-2013772-594465e5 | ch7/g27 | 217 | quotes-f.jsonl:2782 | 144 / 78 | head-skipped — ladder starts at `satisfies By deriv-`, stored keeps `When an individual is risk averse, the second-order condition` | named |
| F20 | P-F-2021-2106074-d0b37839 | ch3/g29 | 68 | quotes-f.jsonl:3174 | 94 / 85 | head-skipped — stored starts `inferior indicators in each group`, ladder `indicators in each group` | named |
| F21 | P-F-2021-2106074-d0b37839 | ch3/g42 | 83 | quotes-f.jsonl:3187 | 60 / 50 | ladder-shorter — ladder ends `National Health Index For Higher`, stored adds `Education` | named |
| F22 | P-F-2021-2109443-9398701f | ch7/g3 | 150 | quotes-f.jsonl:3378 | 61 / 50 | other-sentence — stored `Table 7. the comparisons between Italy`, ladder `United States 13.3 4.7 12.0 1.5` | named |
| F23 | P-F-2021-2122374-0c765494 | ch3/g10 | 54 | quotes-f.jsonl:3484 | 71 / 66 | other-sentence — stored `Proficiency distribution among graduates younger than 35`, ladder `Figure 5 The test results of the literacy` | named |
| F24 | P-F-2023-2311258-7008e4b0 | ch8/g13 | 95 | quotes-f.jsonl:4987 | 44 / 42 | ladder-shorter — ladder drops the private-use bracket glyph U+F8EB that ends the stored quote | named |
| F25 | P-F-2023-2315018-a355e166 | ch5/g6 | 63 | quotes-f.jsonl:5296 | 59 / 46 | other-sentence — stored `economy, society, resources and environment`, ladder `The system is divided into multiple levels` | named |
| F26 | P-F-2023-2315018-a355e166 | ch8/g31 | 130 | quotes-f.jsonl:5360 | 61 / 58 | ladder-shorter — ladder ends `between 0 and 1, and the`, stored adds `CI` | named |
| F27 | P-F-2023-2315018-a355e166 | ch9/g2 | 133 | quotes-f.jsonl:5363 | 54 / 28 | other-sentence — stored `vious regression model to calculate the new CI data`, ladder `= 1, 2, . . . , m) after the` | named |
| F28 | P-F-2023-2315018-a355e166 | ch9/g3 | 134 | quotes-f.jsonl:5364 | 75 / 69 | other-sentence — stored `policy implementation. From there, we computed the predicted`, ladder `1, 2, . . . , m) and the actual CI changes` | named |
| F29 | P-F-2024-2413565-15e84639 | ch1/g3 | 21 | quotes-f.jsonl:5586 | 72 / 60 | other-sentence — stored `Experimental Trade Breeding animals for scientific`, ladder `Trading meat from wildly Selling protected animal` | named |
| F30 | P-F-2024-2413565-15e84639 | ch5/g11 | 82 | quotes-f.jsonl:5625 | 222 / 91 | other-sentence — stored is a two-column interleave (`strength in addressing illegal health, especially in reducing combat illegal wildlife trade by trade issues`), ladder the clean single-column run | named |
| F31 | P-F-2024-2413565-15e84639 | ch5/g12 | 83 | quotes-f.jsonl:5626 | 63 / 62 | other-sentence — stored `cal capabilities for monitoring, projects to optimize corporate`, ladder `of businesses, utilized to fund to combatting illegal wildlife` | named |
| F32 | P-F-2024-2413565-15e84639 | ch5/g13 | 84 | quotes-f.jsonl:5627 | 351 / 284 | other-sentence — stored is a two-column interleave (`⋆Media Platform Promotion teer): Operating extensive vol-`), ladder the column-major run | named |
| F33 | P-F-2024-2413565-15e84639 | ch7/g5 | 104 | quotes-f.jsonl:5646 | 93 / 81 | other-sentence — stored `(b) enterprise (c) organization Figure 4:`, ladder `Clients. By applying the Analytic Hierarchy Process` | named |
| F34 | P-F-2024-2413565-15e84639 | ch9/g11 | 164 | quotes-f.jsonl:5691 | 60 / 53 | head-skipped — stored starts `Figure 8: The most suitable entity`, ladder `8: The most suitable entity` | named |
| F35 | P-F-2024-2413565-15e84639 | ch9/g16 | 169 | quotes-f.jsonl:5696 | 202 / 181 | other-sentence — stored `ambitious goals for itself, intending to restore 5 million hectares`, ladder `conservation stands as a cornerstone across all activities of the LVMH group` | named |
| F36 | P-F-2024-2417340-491a7b05 | ch8/g4 | 114 | quotes-f.jsonl:5845 | 63 / 48 | ladder-shorter — ladder ends `compute the partial`, stored adds `derivatives: ` | named |
| F37 | P-F-2024-2417340-491a7b05 | ch13/g12 | 199 | quotes-f.jsonl:5917 | 83 / 64 | other-sentence — stored `≤45.625) = 0.8286 0.9185 0.9960 100% = 65.1%`, ladder `Therefore, the likelihood of the project meeting expectations is` | named |
| F38 | P-F-2024-2422054-7c8f8bf5 | ch9/g15 | 195 | quotes-f.jsonl:6053 | 91 / 83 | other-sentence — stored `asset distribution, aligns with sociological and behavioral principles`, ladder `Finally, considering the goal of ensuring distributive equity` | named |
| F39 | P-F-2024-2426941-d347a3c2 | ch3/g2 | 44 | quotes-f.jsonl:6106 | 81 / 81 | other-sentence — stored `Justification: Given that these databases are exclusively from websites`, ladder `organizations, it's logical to deduce that the quality of their data` | named |
| F40 | P-F-2024-2426941-d347a3c2 | ch6/g12 | 88 | quotes-f.jsonl:6135 | 53 / 41 | ladder-shorter — ladder ends `the weights of the`, stored adds `indicators:` | named |
| F41 | P-F-2024-2426941-d347a3c2 | ch11/g14 | 149 | quotes-f.jsonl:6183 | 83 / 82 | other-sentence — stored `Increase alternative product choices: Provide legal and sustainable`, ladder `choices and increase the size of the formal trade market` | named |
| F42 | P-F-2024-2426941-d347a3c2 | ch14/g6 | 221 | quotes-f.jsonl:6214 | 93 / 49 | ladder-shorter — ladder ends `at each moment t by`, stored adds `. Ultimately, we obtain what the corrected` | named |
| F43 | P-F-2025-2504223-019dfa54 | ch7/g2 | 74 | quotes-f.jsonl:6299 | 85 / 83 | other-sentence — stored `we tend to consider the characteristics of global interconnection`, ladder `cybercrime, so we will not discuss them separately by country type` | named |
| F44 | P-F-2025-2507789-8d9181d0 | ch9/g11 | 76 | quotes-f.jsonl:6437 | 89 / 77 | ladder-shorter — ladder ends `regularization coefficient (to prevent`, stored adds `overfitting` | named |
| F45 | P-F-2025-2517199-1033f2d4 | ch11/g2 | 90 | quotes-f.jsonl:6680 | 164 / 163 | other-sentence — stored `integrating demographic data into predictive models`, ladder `influencing cybercrime rates. Key insights included` | named |

## 5. Bottom-rung arithmetic (md line 87)

Line 87 states three sums per lane and names one cause, plus line 86's claim about `exact`. The sums
are re-counted here cell by cell from `quote-levels.jsonl`, and every row that moved between `span`
and `gapped`/`unverified` is named below with the run each routine returned. The cause is not a glued
token: it is the two span routines disagreeing on *which* eight-word run is the block's longest. The
token index walks the text's own tokens, so on a block that is mostly numerals or a repeated glyph run
it returns a run of `m m m m …` or `, , , , …`, `has_real_words` rejects it, and the recomputation
falls past `span`. `quote_blocks.span_quote` probes the squeezed text and keeps the longest run, which
on those blocks is the prose or table head.

| lane | span here | span census | gapped here | gapped census | unverified here | unverified census | bottom sum here | bottom sum census | md line 87 claim | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| B | 551 | 555 | 143 | 140 | 281 | 280 | 975 | 975 | "974 against 975" | contradicted - both sides are 975 |
| C | 428 | 430 | 117 | 115 | 181 | 181 | 726 | 726 | "726 against 725" | contradicted - both sides are 726 |
| D | 225 | 226 | 57 | 57 | 73 | 72 | 355 | 355 | "exactly 355" | holds |
| E | 226 | 228 | 52 | 51 | 84 | 83 | 362 | 362 | "exactly 362" | holds |
| F | 362 | 365 | 124 | 121 | 154 | 154 | 640 | 640 | "exactly 640" | holds |

`here` cells: counted off `quote-levels.jsonl` (`level` field, one tally per lane). `census` cells:
`lanes/L7-quote-backfill/reports/levels-b.json` … `levels-f.json`, `match_levels.span`,
`match_levels.gapped`, `match_levels.unverified`. The two columns add to the same total in every lane,
so nothing left or entered the three rungs; only the label moved.

The rows that moved, one per line, with both routines' answers. `del` is the census level and `ins`
the level here; the run quoted first is the token index's answer (rejected), the second is
`span_quote`'s.

| id | lane | paper | ch/group | block | L7 file:line | del | ins | token-index run (rejected) | span_quote run | status |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | B | P-B-2017-68303-6c8a9ede | ch8/g9 | 66 | quotes-b.jsonl:4307 | span | unverified | `, i, j = 1, . . . , 5 (3)` | `Then we calculate the correlation coefficient matrix R = (rij)5∗5` | named |
| S02 | B | P-B-2021-2116496-6a60d0e7 | ch6/g5 | 79 | quotes-b.jsonl:7143 | span | gapped | `5 5 km 2 km 1 km 10 20 km 7 km` | `Power (W) Plain Range Urban Range Mountain Range` | named |
| S03 | B | P-B-2022-2200084-66b742a2 | ch5/g19 | 91 | quotes-b.jsonl:7490 | span | gapped | `, j = 1, 2, 3, 4, 5 ` | ` vij, wij ≥0, i ∈{1, 2}, j ∈{1, 2, 3, 4, 5}` | named |
| S04 | B | P-B-2023-2318300-14fd0bd6 | ch6/g5 | 141 | quotes-b.jsonl:8655 | span | gapped | `b k η h0 α m0 m h1 d β S δ A` | `Table 2: Baseline Values for Constants Prey Predator Tourism` | named |
| S05 | C | P-C-2014-25318-eac62e81 | ch5/g35 | 154 | quotes-c.jsonl:1523 | span | gapped | `i = 1, 2, . . . , n` | `Figure 9: Authority-Popularity Diagram for the co-star network` | named |
| S06 | C | P-C-2018-72969-f2349d15 | ch6/g6 | 176 | quotes-c.jsonl:4192 | span | gapped | `TRCP j 3.11 4.25 6.45 7.43 9.23 11.25 14.50 16.34 18.33` | `Table 10: Sensitivity Analysis of Parameter in Optimization Model` | named |
| S07 | D | P-D-2019-1902407-b8153b5d | ch6/g17 | 35 | quotes-d.jsonl:1600 | span | unverified | `, , , , , , , , , , , , , , , , s.t.` | `for a fixed amount, therefore we should shorten` | named |
| S08 | D | P-D-2021-2100112-1b2d1f1c | ch8/g12 | 174 | quotes-d.jsonl:2746 | gapped | span | `Duration_ms - 1946 - 1966 - - - 2007 Acousticness - - 1950 1964 1979` | `1960s 1970s 1980s 1990s 2000s Instrumentalness 1933 1946 - 1964` | named |
| S09 | D | P-D-2022-2218897-ba395a78 | ch6/g3 | 120 | quotes-d.jsonl:3944 | span | gapped | `PRi(0) = 1, i = 1, 2, · · · , 16.` | `Starting: The initial PageRank (PR) values of all indicators PRi(0)` | named |
| S10 | E | P-E-2025-2515136-5dd4cae6 | ch3/g4 | 34 | quotes-e.jsonl:4958 | span | unverified | `m m m m m m m m m m m` | `is harvested, the biomass drops to zero. m m m m m m` | named |
| S11 | E | P-E-2025-2515136-5dd4cae6 | ch3/g5 | 38 | quotes-e.jsonl:4959 | span | gapped | `m m m m m m m m m m m` | `performance of ecosystems where organic agriculture m m` | named |
| S12 | F | P-F-2021-2123945-e8b5b6e5 | ch6/g12 | 139 | quotes-f.jsonl:3679 | span | gapped | `Modulus 1.278 1.048 0.881 0.735 0.955 0.925 0.660 0.671` | `Modulus 1.278 1.048 0.881 0.735 0.955 0.925 0.660 0.671 Deviation 11.` | named |
| S13 | F | P-F-2023-2305794-7917e986 | ch9/g20 | 137 | quotes-f.jsonl:4835 | span | gapped | `1 1 1 1 1 1 3 5 7 9 9` | `With the relationship discussed before, we get our comparison matrix` | named |
| S14 | F | P-F-2025-2507789-8d9181d0 | ch10/g6 | 112 | quotes-f.jsonl:6468 | span | gapped | `m m m m m m m m m m m` | `we used the following visualization m m m m m m` | named |

Per-lane counts from the table: B 4 (3 to `gapped`, 1 to `unverified`), C 2 (2 to `gapped`), D 3
(1 to `gapped`, 1 to `unverified`, 1 the other way), E 2 (1 and 1), F 3 (3 to `gapped`). Each matches
the cell movement its lane's column pair states: B span -4 = gapped +3 plus unverified +1; C -2 = +2;
D -1 = -1 +1 +1; E -2 = +1 +1; F -3 = +3.

The regenerated md line 87 says "12 rows leave `span` in net": that is the net figure, 14 rows moved
less D's S08 which travels the other way (`gapped` to `span`). Both numbers are the same fourteen
rows read once as movements and once as a net, and this table is the fourteen.

`exact` (md line 86): re-counted from `quote-levels.jsonl` it is 8,325 in C and 4,806 in D, and the
census cells at `levels-c.json` / `levels-d.json` say 8,325 and 4,806. The sentence claims `exact` is 8
low in C and 1 low in D; both lanes agree exactly, so the sentence is contradicted in both halves. The
same line's claim that `nfkc` and `squeezed` agree in all five lanes holds: 850/486, 814/435, 9/138,
14/93, 28/218 here against the same census cells.

## 6. `ocr-only` and `no-text-layer` (md lines 59-64, 77-78, 88)

Line 88 claims `ocr-only` plus `no-text-layer` sums to 73 in B against a census 72, and blames one row
of "the same glue". Re-counted, the two labels cover 72 rows in B and nothing else: `ocr-only` 4 rows
whose page text file is not empty, `no-text-layer` 68 rows whose page text file is empty. `levels-b.json`
`match_levels.ocr-only` is 72, so the difference is 0 and there is no extra row to name. Line 88 is
contradicted; the split at lines 59-64 that says 68 + 4 = 72 holds.

The four `ocr-only` rows, with the page word count that puts them on a page whose text layer exists but
does not cover the block:

| id | paper | ch/group | page | page words | L7 file:line | status |
|---|---|---|---|---|---|---|
| O1 | P-B-2025-2504448-aa644b6e | ch11/g9 | 21 | 1,040 | quotes-b.jsonl:9964 | named |
| O2 | P-B-2025-2517929-c19deeac | ch6/g4 | 7 | 877 | quotes-b.jsonl:10230 | named |
| O3 | P-B-2025-2517929-c19deeac | ch6/g5 | 7 | 877 | quotes-b.jsonl:10231 | named |
| O4 | P-B-2025-2517929-c19deeac | ch7/g29 | 12 | 1,005 | quotes-b.jsonl:10261 | named |

The sixty-eight `no-text-layer` rows, each on a page whose `text/pages/page-N.txt` has zero words:

| id | paper | ch/group | page | L7 file:line |
|---|---|---|---|---|
| N01 | P-B-2025-2501687-ce4f300c | ch6/g4 | 7 | quotes-b.jsonl:9523 |
| N02 | P-B-2025-2501687-ce4f300c | ch6/g5 | 7 | quotes-b.jsonl:9524 |
| N03 | P-B-2025-2501687-ce4f300c | ch6/g8 | 7 | quotes-b.jsonl:9527 |
| N04 | P-B-2025-2501687-ce4f300c | ch11/g12 | 22 | quotes-b.jsonl:9595 |
| N05 | P-B-2025-2501687-ce4f300c | ch11/g13 | 22 | quotes-b.jsonl:9596 |
| N06 | P-B-2025-2501687-ce4f300c | ch11/g15 | 22 | quotes-b.jsonl:9598 |
| N07 | P-B-2025-2501687-ce4f300c | ch11/g16 | 22 | quotes-b.jsonl:9599 |
| N08 | P-B-2025-2501687-ce4f300c | ch11/g17 | 22 | quotes-b.jsonl:9600 |
| N09 | P-B-2025-2501687-ce4f300c | ch13/g4 | 23 | quotes-b.jsonl:9605 |
| N10 | P-B-2025-2501687-ce4f300c | ch13/g5 | 23 | quotes-b.jsonl:9606 |
| N11 | P-B-2025-2502617-613354d9 | ch1/g3 | 1 | quotes-b.jsonl:9633 |
| N12 | P-B-2025-2502617-613354d9 | ch1/g4 | 1 | quotes-b.jsonl:9634 |
| N13 | P-B-2025-2502617-613354d9 | ch1/g5 | 1 | quotes-b.jsonl:9635 |
| N14 | P-B-2025-2502617-613354d9 | ch1/g6 | 1 | quotes-b.jsonl:9636 |
| N15 | P-B-2025-2502617-613354d9 | ch1/g7 | 1 | quotes-b.jsonl:9637 |
| N16 | P-B-2025-2502617-613354d9 | ch1/g8 | 1 | quotes-b.jsonl:9638 |
| N17 | P-B-2025-2502617-613354d9 | ch7/g19 | 19 | quotes-b.jsonl:9726 |
| N18 | P-B-2025-2502617-613354d9 | ch8/g1 | 19 | quotes-b.jsonl:9727 |
| N19 | P-B-2025-2502617-613354d9 | ch8/g4 | 19 | quotes-b.jsonl:9730 |
| N20 | P-B-2025-2502617-613354d9 | ch11/g2 | 22 | quotes-b.jsonl:9744 |
| N21 | P-B-2025-2503268-228e0ec5 | ch2/g2 | 2 | quotes-b.jsonl:9767 |
| N22 | P-B-2025-2503268-228e0ec5 | ch2/g3 | 2 | quotes-b.jsonl:9768 |
| N23 | P-B-2025-2503268-228e0ec5 | ch2/g4 | 2 | quotes-b.jsonl:9769 |
| N24 | P-B-2025-2503268-228e0ec5 | ch2/g5 | 2 | quotes-b.jsonl:9770 |
| N25 | P-B-2025-2503268-228e0ec5 | ch2/g6 | 2 | quotes-b.jsonl:9771 |
| N26 | P-B-2025-2503268-228e0ec5 | ch7/g1 | 7 | quotes-b.jsonl:9791 |
| N27 | P-B-2025-2503268-228e0ec5 | ch7/g4 | 7 | quotes-b.jsonl:9794 |
| N28 | P-B-2025-2503268-228e0ec5 | ch12/g5 | 22 | quotes-b.jsonl:9871 |
| N29 | P-B-2025-2503268-228e0ec5 | ch12/g7 | 22 | quotes-b.jsonl:9873 |
| N30 | P-B-2025-2503268-228e0ec5 | ch12/g8 | 22 | quotes-b.jsonl:9874 |
| N31 | P-B-2025-2503268-228e0ec5 | ch12/g10 | 23 | quotes-b.jsonl:9876 |
| N32 | P-B-2025-2503268-228e0ec5 | ch12/g11 | 23 | quotes-b.jsonl:9877 |
| N33 | P-B-2025-2503268-228e0ec5 | ch12/g12 | 23 | quotes-b.jsonl:9878 |
| N34 | P-B-2025-2503268-228e0ec5 | ch13/g1 | 24 | quotes-b.jsonl:9879 |
| N35 | P-B-2025-2503268-228e0ec5 | ch13/g3 | 24 | quotes-b.jsonl:9881 |
| N36 | P-B-2025-2503268-228e0ec5 | ch13/g5 | 24 | quotes-b.jsonl:9883 |
| N37 | P-B-2025-2503268-228e0ec5 | ch13/g6 | 24 | quotes-b.jsonl:9884 |
| N38 | P-B-2025-2504448-aa644b6e | ch3/g3 | 5 | quotes-b.jsonl:9897 |
| N39 | P-B-2025-2504448-aa644b6e | ch3/g6 | 5 | quotes-b.jsonl:9900 |
| N40 | P-B-2025-2504448-aa644b6e | ch4/g1 | 5 | quotes-b.jsonl:9903 |
| N41 | P-B-2025-2504448-aa644b6e | ch7/g7 | 9 | quotes-b.jsonl:9920 |
| N42 | P-B-2025-2504448-aa644b6e | ch7/g8 | 9 | quotes-b.jsonl:9921 |
| N43 | P-B-2025-2504448-aa644b6e | ch7/g9 | 9 | quotes-b.jsonl:9922 |
| N44 | P-B-2025-2504448-aa644b6e | ch7/g10 | 9 | quotes-b.jsonl:9923 |
| N45 | P-B-2025-2504448-aa644b6e | ch7/g11 | 9 | quotes-b.jsonl:9924 |
| N46 | P-B-2025-2504448-aa644b6e | ch10/g7 | 18 | quotes-b.jsonl:9954 |
| N47 | P-B-2025-2504448-aa644b6e | ch10/g8 | 18 | quotes-b.jsonl:9955 |
| N48 | P-B-2025-2505199-bc9da82b | ch2/g2 | 3 | quotes-b.jsonl:9998 |
| N49 | P-B-2025-2505199-bc9da82b | ch5/g1 | 3 | quotes-b.jsonl:10013 |
| N50 | P-B-2025-2505199-bc9da82b | ch5/g2 | 3 | quotes-b.jsonl:10014 |
| N51 | P-B-2025-2505199-bc9da82b | ch7/g18 | 18 | quotes-b.jsonl:10069 |
| N52 | P-B-2025-2505199-bc9da82b | ch8/g1 | 18 | quotes-b.jsonl:10070 |
| N53 | P-B-2025-2509557-c800a325 | ch4/g1 | 6 | quotes-b.jsonl:10110 |
| N54 | P-B-2025-2509557-c800a325 | ch13/g3 | 25 | quotes-b.jsonl:10192 |
| N55 | P-B-2025-2509557-c800a325 | ch13/g6 | 25 | quotes-b.jsonl:10195 |
| N56 | P-B-2025-2517929-c19deeac | ch2/g2 | 3 | quotes-b.jsonl:10205 |
| N57 | P-B-2025-2517929-c19deeac | ch2/g4 | 3 | quotes-b.jsonl:10207 |
| N58 | P-B-2025-2517929-c19deeac | ch3/g1 | 3 | quotes-b.jsonl:10218 |
| N59 | P-B-2025-2517929-c19deeac | ch7/g30 | 13 | quotes-b.jsonl:10262 |
| N60 | P-B-2025-2517929-c19deeac | ch7/g31 | 13 | quotes-b.jsonl:10263 |
| N61 | P-B-2025-2517929-c19deeac | ch7/g34 | 13 | quotes-b.jsonl:10266 |
| N62 | P-B-2025-2517929-c19deeac | ch7/g35 | 13 | quotes-b.jsonl:10267 |
| N63 | P-B-2025-2517929-c19deeac | ch9/g4 | 18 | quotes-b.jsonl:10294 |
| N64 | P-B-2025-2517929-c19deeac | ch9/g5 | 18 | quotes-b.jsonl:10295 |
| N65 | P-B-2025-2517929-c19deeac | ch11/g13 | 22 | quotes-b.jsonl:10317 |
| N66 | P-B-2025-2517929-c19deeac | ch11/g14 | 22 | quotes-b.jsonl:10318 |
| N67 | P-B-2025-2517929-c19deeac | ch11/g15 | 22 | quotes-b.jsonl:10319 |
| N68 | P-B-2025-2517929-c19deeac | ch11/g16 | 22 | quotes-b.jsonl:10320 |

4 + 68 = 72, which is `levels-b.json` `match_levels.ocr-only` = 72. No lane other than B carries either
label, so the all-lane cells at md lines 59-60 and 77-78 are the B rows themselves.

## 7. F's two `text-gap` rows (md lines 79, 88)

Lines 79 and 88 report `text-gap` 2 in F and 2 in the census. The two rows:

| id | paper | ch/group | block | page | L7 file:line | status |
|---|---|---|---|---|---|---|
| G1 | P-F-2020-2013733-073f48f7 | ch3/g7 | 34 | 5 | quotes-f.jsonl:2598 | named |
| G2 | P-F-2023-2315018-a355e166 | ch14/g8 | 187 | 20 | quotes-f.jsonl:5416 | named |

Both papers carry `text_gap_blocks` at or above `TEXT_GAP_MIN_BLOCKS`, which is what puts their
unmatched prose blocks at this label rather than `unverified`; the census cell at
`levels-f.json` `match_levels.text-gap` is 2, so these two rows are the whole cell on both sides.

## 8. Does the census quote a different block than the ladder? (asked lane by lane)

Checked for all 247 rows of §4: the stored string was searched for in the group text, then in every
block of the paper's current layout. Two outcomes, no third:

- 205 rows: the stored string is a substring of the block the ladder quoted (`stored_in_block` true in
  `reports/residue-mismatches.jsonl`). Same block, different sentence or a different end of the same
  sentence. This is the family §4 labels `ladder-shorter`, `head-skipped` and `other-sentence`.
- 42 rows: the stored string is not an exact substring of any block in the current layout. Split by
  how far it is from matching, checked block by block against the group text: 41 match once NFKC
  normalisation is applied (`ﬁ` against `fi`, `XXiiii` for `X_i`), so the sentence is still there and
  only the glyphs moved; 1 matches under no normalisation at all — X32,
  `P-D-2021-2100112-1b2d1f1c` ch8/g12 block 174, `quotes-d.jsonl`:2746, the row whose stored string
  is in no block of the paper. None of the 42 is a row where the census quoted one block and the
  ladder another. `reports/quote-check.json` carries the same split as `quote_mismatch_in_block`
  205 / `quote_mismatch_normalised_only` 41 / `quote_mismatch_absent` 1.

| id | lane | paper | ch/group | block | group members | L7 file:line |
|---|---|---|---|---|---|---|
| X01 | B | P-B-2014-26333-27e7d8ab | ch14/g27 | 463 | [463] | quotes-b.jsonl:2072 |
| X02 | B | P-B-2014-26333-27e7d8ab | ch14/g29 | 465 | [465] | quotes-b.jsonl:2074 |
| X03 | B | P-B-2014-28414-5bd5b982 | ch8/g3 | 154 | [154] | quotes-b.jsonl:2313 |
| X04 | B | P-B-2014-28414-5bd5b982 | ch8/g7 | 159 | [159, 160] | quotes-b.jsonl:2317 |
| X05 | B | P-B-2014-28414-5bd5b982 | ch8/g10 | 163 | [163, 164] | quotes-b.jsonl:2320 |
| X06 | B | P-B-2015-32879-2c587e51 | ch18/g2 | 260 | [260, 261] | quotes-b.jsonl:2931 |
| X07 | B | P-B-2015-32879-2c587e51 | ch18/g3 | 262 | [262] | quotes-b.jsonl:2932 |
| X08 | B | P-B-2015-32879-2c587e51 | ch18/g4 | 263 | [263] | quotes-b.jsonl:2933 |
| X09 | B | P-B-2017-56731-a60a9459 | ch8/g30 | 94 | [94] | quotes-b.jsonl:4146 |
| X10 | B | P-B-2017-56731-a60a9459 | ch8/g31 | 95 | [95] | quotes-b.jsonl:4147 |
| X11 | B | P-B-2017-68303-6c8a9ede | ch8/g9 | 66 | [66] | quotes-b.jsonl:4307 |
| X12 | B | P-B-2017-69427-b04ae242 | ch6/g6 | 95 | [95, 96, 97] | quotes-b.jsonl:4433 |
| X13 | B | P-B-2020-2019696-961d6242 | ch8/g10 | 156 | [156] | quotes-b.jsonl:6533 |
| X14 | B | P-B-2020-2019696-961d6242 | ch9/g5 | 127 | [127] | quotes-b.jsonl:6542 |
| X15 | B | P-B-2020-2019696-961d6242 | ch9/g16 | 148 | [148, 149] | quotes-b.jsonl:6553 |
| X16 | B | P-B-2021-2105363-52f891b1 | ch6/g19 | 88 | [88] | quotes-b.jsonl:6916 |
| X17 | B | P-B-2021-2105363-52f891b1 | ch12/g8 | 285 | [285] | quotes-b.jsonl:7068 |
| X18 | B | P-B-2021-2116496-6a60d0e7 | ch11/g3 | 214 | [214] | quotes-b.jsonl:7240 |
| X19 | B | P-B-2024-2411570-f02ed036 | ch5/g6 | 105 | [105] | quotes-b.jsonl:8980 |
| X20 | B | P-B-2024-2411570-f02ed036 | ch6/g15 | 130 | [130] | quotes-b.jsonl:9001 |
| X21 | B | P-B-2024-2411570-f02ed036 | ch6/g22 | 191 | [191] | quotes-b.jsonl:9008 |
| X22 | B | P-B-2024-2411570-f02ed036 | ch10/g20 | 180 | [180] | quotes-b.jsonl:9054 |
| X23 | C | P-C-2014-28199-d39873d7 | ch4/g19 | 57 | [57] | quotes-c.jsonl:1688 |
| X24 | C | P-C-2014-31262-1f9007fa | ch4/g45 | 67 | [67] | quotes-c.jsonl:2099 |
| X25 | C | P-C-2015-37075-1d95d60d | ch5/g15 | 159 | [159, 160, 161, 162] | quotes-c.jsonl:2694 |
| X26 | C | P-C-2015-37284-dee063ba | ch2/g5 | 22 | [22, 23] | quotes-c.jsonl:2778 |
| X27 | C | P-C-2016-47823-59d82231 | ch8/g11 | 227 | [227, 228] | quotes-c.jsonl:3322 |
| X28 | C | P-C-2019-1922154-b7129095 | ch4/g32 | 100 | [100, 101] | quotes-c.jsonl:5374 |
| X29 | C | P-C-2020-2002116-f6f4a15a | ch4/g30 | 99 | [99, 100] | quotes-c.jsonl:5541 |
| X30 | C | P-C-2020-2010638-c32c8549 | ch5/g46 | 190 | [190] | quotes-c.jsonl:6340 |
| X31 | C | P-C-2021-2109298-1a718172 | ch4/g85 | 164 | [164] | quotes-c.jsonl:7250 |
| X32 | D | P-D-2021-2100112-1b2d1f1c | ch8/g12 | 174 | [174] | quotes-d.jsonl:2746 |
| X33 | D | P-D-2021-2101855-c4682962 | ch5/g11 | 68 | [68] | quotes-d.jsonl:2941 |
| X34 | F | P-F-2016-44348-d3da2a69 | ch6/g6 | 152 | [152] | quotes-f.jsonl:194 |
| X35 | F | P-F-2016-44348-d3da2a69 | ch6/g9 | 155 | [155] | quotes-f.jsonl:197 |
| X36 | F | P-F-2016-44348-d3da2a69 | ch6/g25 | 172 | [172] | quotes-f.jsonl:213 |
| X37 | F | P-F-2018-87280-fa7e05e4 | ch3/g42 | 87 | [87] | quotes-f.jsonl:1047 |
| X38 | F | P-F-2019-1905127-b4a0bea2 | ch7/g5 | 82 | [82] | quotes-f.jsonl:1664 |
| X39 | F | P-F-2019-1905127-b4a0bea2 | ch7/g15 | 96 | [96, 97] | quotes-f.jsonl:1674 |
| X40 | F | P-F-2019-1916704-dd8d036e | ch8/g14 | 186 | [186, 187, 188] | quotes-f.jsonl:1953 |
| X41 | F | P-F-2020-2013772-594465e5 | ch7/g27 | 217 | [217] | quotes-f.jsonl:2782 |
| X42 | F | P-F-2024-2426941-d347a3c2 | ch6/g12 | 88 | [88] | quotes-f.jsonl:6135 |

So the answer to the adjudication question is none: no row has the census and the ladder quoting two
different blocks of the same paper. The 42 rows sit one step further out - 41 keep the sentence but not
its glyphs, 1 (X32) keeps nothing - and they explain themselves as quote files regenerated after the
records were rewritten (B 22, C 9, D 2, F 9). Every one is already counted in §4 under its own
quote-length pair, X32 also under S08 for its rung movement; the two facts are the same block, read
twice.

## 9. Closure - each discrepancy against the rows that name it

| discrepancy | md line (at ed865a45…) | figure | rows naming it | count |
|---|---|---|---|---|
| rows whose quote differs | 92 | 257 claimed, 247 re-counted | §4: B01-B76, C01-C59, D01-D40, E01-E27, F01-F45 | 247 |
| B bottom-rung total | 87 | 974 against 975 | S01-S04 | 4 |
| C bottom-rung total | 87 | 726 against 725 | S05-S06 | 2 |
| D bottom-rung total | 87 | 355 | S07-S09 | 3 |
| E bottom-rung total | 87 | 362 | S10-S11 | 2 |
| F bottom-rung total | 87 | 640 | S12-S14 | 3 |
| `ocr-only` plus `no-text-layer` | 88 | 73 against 72 | O1-O4 (4) + N01-N68 (68) | 72 |
| F `text-gap` | 79, 88 | 2 | G1-G2 | 2 |
| `exact` "8 low in C, 1 low in D" | 86 | 0 rows low | none - the cell agrees exactly in both lanes | 0 |

Totals named in this file: 247 quote-mismatch rows + 14 rung rows + 72 ocr rows + 2 text-gap rows = 335
rows, every one with a paper, a chapter and group, a block, and a `quotes-*.jsonl` line. The two
zero-row rows (the `exact` sentence and the ocr split) are recorded as zero because the figure they
claim is not in the data; both were re-counted from the files rather than argued from the report.
