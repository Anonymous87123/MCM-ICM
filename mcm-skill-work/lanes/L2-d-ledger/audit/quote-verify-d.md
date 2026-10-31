# D lane — quote rows verified against the records

Scope: read-only join. `lanes/L7-quote-backfill/quotes-d.jsonl` was not edited; every
defect found there is reported, not repaired. The only writes were to
`lanes/L2-d-ledger/records/**`, and only for the one defect that was mine.

## Inputs

| file | rows | papers | sha256 |
|---|---|---|---|
| `lanes/L7-quote-backfill/quotes-d.jsonl` (L7, re-emitted 00:41 today) | 5309 | 55 | `f4e0e253818f9e21…` |
| `lanes/L2-d-ledger/jobs-d.jsonl` (units, after the duplicate repair) | 5308 units | 55 | — |

## Join key

L7's `block_index` is **not** a layout paragraph number. It is the 0-based ordinal of the
unit inside its chapter, so the join key is `(paper, chapter, ordinal)` with the rows
sorted by `block_index` and the units taken in `groups` order. Joining on the layout block
number instead produces 5008 false misses, which is how the first pass of this check went
wrong before the field was inspected.

## Result

| check | count |
|---|---|
| units in D records | 5308 |
| quote rows in `quotes-d.jsonl` | 5309 |
| unit/row pairs joined | 5308 |
| pairs whose chapter and job agree | 5305 |
| pairs with a different job | 3 |
| units with no quote row | 0 |
| orphan quote rows | 1 |
| quote rows that fold to nothing | 1 |
| quotes found inside the unit's own block span | 5231 |
| quotes not found inside the unit's block span | 76 |

## The 76 quotes outside their unit

Two causes, separated by testing whether the quote belongs to the neighbouring unit
instead. Found in the neighbour's span means a real offset; found nowhere means the quote
was extracted from the PDF layer rather than from the paragraph text.

* **2 offset rows**, both in `P-D-2021-2101855-c4682962 / conclusion`, both explained in
  the next section.
* **74 glyph and table rows**. The quote is a display equation, a table's cell text or a
  figure caption that L7 lifted from the page while the paragraph layer renders the same
  content with private-use glyphs, reordered cells or a watermark inside the string. The
  unit ordinal and the job still agree, so the row points at the right unit; only the
  quote string cannot be substring-tested. Examples: `P-D-2019-1902407-b8153b5d`
  model-establishment 29 (`The objective function is W= …`), `P-D-2018-73156-1a30e830`
  model-establishment 29 (`Constraint of vehicles`), `P-D-2017-68942-f0b0893e` results 1
  (`Table 3: Wait time data for the 1221 configuration …`).

These are not misalignments and I am not asking L7 for them. They are the same class the
lane already records as an alien-glyph case on its own side.

## The one real misalignment: P-D-2021-2101855-c4682962 / conclusion

Caused by this session's duplicate-block repair, not by L7. Block 209 was claimed by both
`conclusion` and `strengths-limitations`; it went to `strengths-limitations`, so the
conclusion chapter now has four units where L7 emits five rows:

* orphan row: `chapter_index` for `conclusion`, `block_index` 4, job `check` — the row for
  the unit that no longer exists;
* the three job mismatches (`limit`/`route`, `select`/`limit`, `check`/`select`) are the
  ordinal shift that follows from the same deletion, not three separate defects;
* the two offset quotes are the same shift seen through the text.

Action for L7, on its next D emit: regenerate `quotes-d.jsonl` from the current records.
The chapter's row count goes 5 to 4 and every row after the deletion moves up one ordinal.

## The one empty quote

`P-D-2024-2417831-f399a6df / model-establishment / block_index 9` carries the quote `.` —
a single period, which folds to nothing.

Cause was in my record, not in L7: that unit's `open` was a stray period in front of the
benefit-function sentence. It passed `check.py` because a period is a non-empty string.
Fixed in the record by giving the unit a hand anchor on the sentence itself, keyed to its
first block:

```
"quotes": {"72": "The benefit function of ship- ping revenue can be expressed by"}
```

The anchor keeps the printed hyphenation, because the folded form of `ship- ping` is
`ship-ping` and a de-hyphenated anchor does not fold into the page text.

L7's row for that unit still quotes the old opening, so it should be re-emitted together
with the row-count change above; its ordinal is unchanged, so this is a text refresh, not a
staging change.

## Lane state behind these numbers

```
papers 55
55 problems none
55 layout sha256 identical
TOTAL 5308 units, 0 misses
```

`verify_quotes.py` reports 0 misses over the lane after the anchor, and the duplicate
number counter is empty for all 55 records.

## Residual: units whose opening is a heading or a formula

MCM1 tests opens and closes against the recomputed first and last sentence of the unit, not
just against non-emptiness. In D that test passes by construction, because `record.py`
derives `open` from `first_sentence(clean_text(block))` and `close` from
`closed_sentence(...)`; the only opens it does not derive are the anchored ones. A stricter
scan was run anyway, flagging every unit whose open or close carries fewer than 12 letters
or fewer than three words and is not anchored: 12 opens and 51 closes.

All 63 are verbatim page strings, and they fall into three classes, none of them the bare
period that turned up in P-D-2024-2417831-f399a6df:

* 5 open on a printed heading, because the layer starts the group on a block that carries
  a subsection head (`1.1 Background`, `Assumptions`, `5.1 Strengths`, `2.1 Assumptions`,
  `7.1.1 Bv7 Algorithm`) before its prose;
* 5 open on a display equation (`Δ(t) = E {L (t + 1) − L (t) | Q (t)}`, `d (x, y) = …`,
  `Ri,j = Pi,j + Pj,i`, `PR(A) = PR(B) + PR(C)`, `x0 · G′ = x0 · G + Δx`);
* 1 opens on a pseudocode line (`for e in E do`), and 51 close on an equation tail or on a
  two-word corpus sentence.

They are left as recorded: each is the page's own first or last sentence for that block,
and the lane's convention keeps a head printed inside a coded block with that block. No
anchor was added, because an anchor would replace a verbatim page string with a hand-picked
neighbour clause and make the record less faithful, not more.
