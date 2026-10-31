# L7 hand sample — review record

Reviewed 2026-10-23 by the lane owner, on the samples written by `tools/spot_check.py`
(stride sampling, 30 rows per lane, hand read against each paper). Five lanes carry a
quote layer: B, C, D (chapter ledgers) and E, F (closed lanes, backfilled in this pass).

Run recorded here: `quote_blocks.py` B/C/D/E/F all exit 0 (9.9 s / 7.5 s / 7.2 s /
5.2 s / 9.8 s), then `coverage.py`, then `spot_check.py` for the same five lanes. Sample
drawn from the quote files as they stand after that run:

| lane | sample | quote file | sampled | readable | flagged suspect |
| --- | --- | --- | --- | --- | --- |
| B | 30 | 10,333 rows | 30 | 30 | 15 |
| C | 30 | 10,397 rows | 30 | 30 | 10 |
| D | 30 | 5,308 rows | 30 | 30 | 10 |
| E | 30 | 5,024 rows | 30 | 30 | 10 |
| F | 30 | 6,794 rows | 30 | 30 | 7 |
| total | 150 | 37,856 rows | 150 | 150 | 52 |

`coverage.py` after the same run: every lane reports `rows == coded_groups at emit`,
shortfall 0, empty 0, dup 0, zero groups added since emit (B 10,333 / C 10,397 /
D 5,308 / E 5,024 / F 6,794).

**Hit rate in the sample: 30 of 30 per lane, 150 of 150 in total.** Each sampled row was
re-derived from its paper's records and layout and came back byte-identical at the level
the sample reports; no row carries an unresolved level (`?`). The sample contains no
paraphrase, no invented text and no quote absent from its paper. "Flagged suspect" is not a
miss count — it counts rows whose quote is verbatim but not a clean sentence, which is the
class a second reader has to judge.

## What the flagged rows are

| lane | classes among the flagged (count) |
| --- | --- |
| B | 3 section-heading or section-number opens (`2.1 Amelia Earhart…`, `4.3 The relationship…`, `Summary`), 2 label-only opens (`Figure 28`, `(7) all games`), 1 notation row, 1 code listing (an R main loop), 5 mid-sentence or colon-terminated starts, 1 gapped run from a memo header through the uploader watermark into `1 Introduction`, 1 `ocr-only` prose row |
| C | 3 heading opens (`Definition of Φ…`, `Tag Encoding of String Type Data`, `9.1 Tests of the stacking model`), 1 caption (`Figure 4: Model overview`), 1 colon-terminated label (`Simplifying Assumptions :`), 2 mid-sentence starts, 1 span inside a figure's own lettering (`GP R Pr edic tion To predict`), 1 span on an equation lead, 1 span cut at a line-break hyphen (`Random For-`) |
| D | 1 section-number open (`5.3 Sensitivity Analysis and Model Validation`), 1 chart-lettering row, 1 notation row (`unverified`), 1 figure caption (`Figure 7: Total Similarity…`), 1 gapped run joining two subplot labels (`(b) Phase of the FFT result`), 1 gapped run from a label row into `5 Model 3: …`, 3 mid-sentence or mid-clause starts, 1 span mid-sentence, 1 squeezed row carrying math glyphs (`푑represents the service radius…`) |
| E | 1 reference-list entry, 1 equation-following sentence (`… bocean, bland in Equation 20 are constants`), 1 heading (`10.3 Conclusions for Finnish Food System`), 4 mid-sentence or mid-clause starts, 1 span inside a two-column notation table, 1 notation lead (`Where, R : Growth rate…`) |
| F | 1 glued heading (`1.1Background`), 1 table/list row (`Performing Arts: Artistic forms…`), 1 numbered-item open (`4) Review the integrity…`), 3 mid-sentence or mid-clause starts, 1 span mid-clause, 1 gapped run through a comma-separated symbol row (`IR, PK, TR, SY, AR, CN …`) |

- **Caption, heading and label opens.** The first block of a chapter is often the figure
  caption or the section heading, so the quote is a label rather than a sentence. The
  layout offers no better first block; the level is `exact` because the label does verify
  verbatim. Same cause for a bare section number such as `4.3` or an equation tag `(25)`.
- **Bullet and list-item opens.** A block starting with `•`, `●` or `4)` quotes the marker
  plus the item. Verbatim, marker is furniture.
- **Mid-sentence block starts.** The layout begins a block mid-sentence, so the quote starts
  lowercase and carries no terminal punctuation. Verbatim; this is the dominant reason a row
  is flagged, and it is not a matching failure.
- **Equation and notation leads.** Symbol soup quoted as-is, level `unverified` when it
  carries no sentence at all, `exact` when the notation row does verify.
- **Code and reference entries.** An appendix block of an R listing or a bibliography entry
  is one block, so the quote is one line of code or one reference. Verbatim.
- **Hyphenated and figure-internal spans.** A span may start after a line-break hyphen
  (`Random For-`) or quote a figure's own lettering.
- **Gapped runs over furniture.** A memo header, the uploader watermark and the next heading
  can join into one in-order run; a comma-separated symbol row reads as a word list. Words
  are verbatim and in order, the run crosses block-internal furniture, and the `gapped`
  level exists so this class stays findable.

## Defect fixed in this pass: quotes opened by the uploader watermark

The watermark (`微信号`, `关注数学模型`, `获取更多资讯`, `MATHmodels`) is printed as three widely
spaced lines, so the layout emits it as its own block and it lands as the first block of a
coded group. Measured before the fix: 206 rows opened on the stamp. Fix in
`tools/quote_blocks.py` (`is_stamp_only`, `strip_leading_stamp`): a stamp-only first block
hands the quote to the first block of the same group that carries the paper's own text, and
a stamp glued to the head of a real block is trimmed off the head. Now 120 rows carry a
stamp, **none at the start of its quote** (smallest offset 2 characters), all of them
inside `span` or `gapped` runs where cutting would tear a hole in the run's own claim of
word order. Counted, not edited.

## Defect fixed in this pass: symbol-only span and gapped matches

`P-D-2025-2516219-17e4e820` produced a `span` quote of `m m m m …` against a matrix. The
ladder accepts it (`m` occurs everywhere) and the row says nothing. Fix: a `span` or
`gapped` match must carry at least two distinct words of three letters or more
(`has_real_words`), otherwise the block falls through to the label its content deserves.
The same guard rejects symbol-only blocks before the gapped search is attempted, which also
made the pass slower rather than faster, so the search is now anchored on words of at least
three characters with at most 20 candidate origins (`GAP_MIN_ANCHOR`, `GAP_MAX_ORIGINS`).
Measured effect: the five-lane pass runs in 40 s total instead of stalling for tens of
minutes on D and E, and the `gapped` counts are unchanged (B 140 / C 115 / D 57 / E 51 /
F 121) — the guard removed search work, not quotes.

## Defect found in the previous pass (F, still in force)

Backfilling F surfaced two prose blocks that no ladder step could verify:
`P-F-2020-2013733-073f48f7` block 34 and `P-F-2023-2315018-a355e166` block 187, both
`kind: body`, both with real sentences, both absent from their paper's `full.txt` — not
reordered, absent. A spot count of the same papers found 19 and 8 body blocks respectively
with no eight-word span anywhere in the text layer, so those papers' text layers drop whole
paragraphs.

The generator used to abort on such a block, which is the correct behaviour for a lost
sentence in a clean paper but the wrong behaviour for a paper whose text layer is known to
be gappy. Rule added (`tools/quote_blocks.py`, `text_gap_blocks`): when a prose block fails
every contiguous step **and** the paper's own text layer has at least three body blocks
with no eight-word span, the block is quoted from the layout and labelled `text-gap`, which
`coverage.md` defines as "paper's text layer drops whole paragraphs; this block quoted from
the layout". A prose block that fails with no such evidence still aborts the lane. Two F
rows carry the label.

## Defect found in an earlier pass (B, still in force)

`P-B-2025-2502617-613354d9` abstract block 2: layout read from page images with the text
layer never covering the abstract, so the prose block fell through to `gapped` and stitched
scattered words into `the of the tourism industry in Juneau and`. On an `ocr_layout` paper a
prose block that fails the four contiguous steps is now labelled `ocr-only` before `gapped`
is tried; the row now quotes the block's own opening. Fifteen B rows moved `gapped` →
`ocr-only`; 72 B rows carry the label.

## Quote hygiene counts, whole lanes (not just the sample)

Measured over the emitted files after the run above:

| lane | rows | quotes under 20 chars | rows carrying the uploader watermark | no terminal punctuation | of those, lowercase start |
| --- | --- | --- | --- | --- | --- |
| B | 10,333 | 671 | 35 over 15 papers | 4,064 | 391 |
| C | 10,397 | 645 | 32 over 12 papers | 3,603 | 323 |
| D | 5,308 | 397 | 16 over 11 papers | 1,651 | 143 |
| E | 5,024 | 356 | 7 over 7 papers | 1,702 | 163 |
| F | 6,794 | 479 | 30 over 16 papers | 2,773 | 261 |

`short_quotes` is the same count `reports/coverage.json` publishes; it exists so the merge
session can see how many rows lean on a label, a section number or an equation tag. The
watermark column is down from 206 rows before this pass to 120, and every remaining one is
mid-quote. The no-terminal-punctuation column is expected for `span`, `gapped`,
`unverified`, `layout-only`, `ocr-only` and `text-gap` rows — those quote a run of words,
not a sentence — and the lowercase-start column isolates the mid-sentence block start, which
is the one worth a second read.

No boundary check needed a rendered page in this pass, so no proxy images were made.
