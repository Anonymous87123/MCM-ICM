# D lane — duplicate block references repaired

Scope: `lanes/L2-d-ledger/records/*.json` only. Nothing outside the lane was written.

## Method

For each of the 55 records, a `Counter` was taken over every block number in every group
of every chapter:

```
Counter(n for ch in record for g in ch["groups"] for n in g)
```

Any block number reaching a count of 2 is claimed twice inside one paper. Before the
repair that set was three blocks over three papers, six blocked rows in L9 (one row per
claiming chapter per block), which matches the `duplicate-block-ref 6 rows over 3 papers`
figure in `lanes/L9-merge-dryrun/reports/stats.json`.

The 52 other papers were already clean: their builders assert
`sorted(coded) == range(1, max+1) minus UNC`, which forbids a repeat by construction.

## The three cases

All three are the same print defect: one layer block carries the closing prose of chapter
N and the heading (sometimes only the heading) of chapter N+1, so both chapters had
legitimately reached for it. The lane's standing convention decides the owner — a heading
printed inside a body block stays with that block, and the block belongs to the chapter
whose prose it carries. Each fix therefore drops the *other* chapter's claim on it.

### P-D-2016-49436-4c3ef010 — block 192

Claimed by `results` group 7 `[185…192]` and `strengths-limitations` group 0 `[192…201]`.
Block 192 reads as the closing paragraph of the media-versus-person comparison and ends
with `10. Strengths and Weaknesses 10.1 Strengths`.

Resolution: block 192 stays with `results`, whose note already recorded that the group
closes on the strengths section heading. `strengths-limitations` group 0 becomes
`[193…201]`, still two groups against the stored one, so `Delta +1` is unchanged. The note
now states that the block belongs to the results chapter and carries only the 10 and 10.1
heads in its tail.

### P-D-2017-55285-1835cc0b — block 181

Claimed by `sensitivity-analysis` group 2 `[175…181]` and `strengths-limitations` group 0
`[181…187]`. Block 181 is the China verdict that closes the PBQ sensitivity run, followed
by `6 Conclusion 6.1 Strengths and Weaknesses 6.1.1 Strengths`.

Resolution: block 181 stays with `sensitivity-analysis`, whose note already recorded the
group as ending on that verdict. `strengths-limitations` becomes `[182…187]`, still one
group against the stored one, so `Stored count 1 matches` is unchanged. The note now
states that the block belongs to the sensitivity chapter and that the strengths chapter
starts at 182.

### P-D-2021-2101855-c4682962 — block 209

Claimed by `conclusion` group 0 `[209]` — a group of that one block — and
`strengths-limitations` group 5 `[207, 208, 209]`. Block 209 carries the last weakness
sentence (`musicians across periods under different circumstances.`) and the chapter 8
heading `8 微信号：MATHmodels Further Discussion`.

Resolution: block 209 stays with `strengths-limitations`, whose prose it carries. The
`conclusion` chapter loses a group that held nothing but that block, so it drops from five
groups to four `[[210], [211], [212], [213]]` against the stored two: `Delta +2`, not the
previous `Delta +3`, and the note now gives the cause. This is the only case where the
repair changes a unit count; its consequences for the quote layer are recorded in
`quote-verify-d.md`.

## Result

| check | before | after |
|---|---|---|
| papers with a duplicated block number | 3 | 0 |
| duplicated block numbers | 3 (blocks 192, 181, 209) | 0 |
| L9 `duplicate-block-ref` rows | 6 | 0 |
| block count per affected paper | 204 / 186 / 217 | unchanged |
| units in the lane | 5309 | 5308 |

The −1 is the dropped `conclusion` group in P-D-2021-2101855-c4682962. No block lost
coverage: 209 is still coded, in the chapter that owns its text.

`record.py` was re-run for each of the four edited papers, so `jobs-d.jsonl` and
`notes/<pid>.md` were regenerated from the corrected records:

```
wrote P-D-2016-49436-4c3ef010 7 chapters, 27 groups, 204 blocks, 7049 clean words
wrote P-D-2017-55285-1835cc0b 10 chapters, 31 groups, 186 blocks, 6930 clean words
wrote P-D-2021-2101855-c4682962 13 chapters, 132 groups, 217 blocks, 6823 clean words
wrote P-D-2024-2417831-f399a6df 11 chapters, 139 groups, 210 blocks, 6925 clean words
```

(Note: `record.py` takes one paper id, not a list. Passing three ids processes only the
first and leaves the other two rows in `jobs-d.jsonl` stale, so the four runs above were
issued separately.)

Every delta reason survives the edit. The chapter whose group count drops below the
stored `paragraph_count` — `conclusion` in P-D-2021-2101855-c4682962 — still carries an
explicit delta sentence naming the stored count and the printed groups.

## Lane-wide verification after the repair

```
papers 55
55 problems none
55 layout sha256 identical
TOTAL 5308 units, 0 misses
```

Two consecutive runs of `check.py` print the same per-paper sha256 for all 55 papers, and
the duplicate counter is empty for all 55 records.
