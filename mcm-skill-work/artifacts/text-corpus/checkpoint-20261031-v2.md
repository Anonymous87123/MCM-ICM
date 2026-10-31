# Complete text corpus checkpoint - 2026-10-31, v2

Goal ACTIVE:435 papers/11,552 pages, complete traceable chapter/paragraph text,
exhaustive reader, separate installable skill and ACTUAL AI reading of ALL
corresponding substantive sections. Abstracts are the first checkpoint, not final.
User added: when broad scripts repeatedly fail, restore papers individually.
Root only/no new agents. Formula correctness/figure interpretation paused. Keep
all old artifacts, failed generations, source files, installed skill and history.

## Latest completed immutable candidate: v18

- `reflow-20261031-v18`, dataset
  `46fd48b11dcdb0d09589c8cd3c430c2683a0bf1b68dafe76281a01e0c7899910`.
- `integrity-reflow-20261031-v18.json` PASS/errors0:435 papers/11,552 pages,
 954,866 raw lines accounted once,292,424 blocks,18,524 candidate sections,
 5 boundary reviews,2,619 protected legacy inputs unchanged. All18,524 chapter
 Markdown/SQLite/FTS views now compared to their authoritative derived texts.
- Source completeness FALSE, zero whole-paper source acceptance.427 nonempty
 abstract candidates/6 source-local absences/2 empty unresolved(q11/q169).
 Do not confuse complete source accounting with readable-source completeness.
- V18 applies checked q14 Summary/handout boundary (2677chars/page1), retaining
 handout author prose separately; all v17 q6/q12/q333 fixes remain applied.
- V17 and its recovered successful finalization are preserved. Do not rerun
 any completed v16/v17/v18 build. V13 remains rejected and preserved.

## Query/export defect fixed and frozen in v18

- New chapter Markdown and SQLite text share production reader policy, excluding
 nested Contents/References/AI reports from default author chapters. Full.md and
 structured source keep all material. Canonical section_text source-review hashes
 remain unchanged, while documents mark `chapter_view_policy:query-selected-v1`.
 Old generations without that field validate using their old canonical exports.
- Explicit non-author role/title requests now retrieve actual typed references,
 contents, AI-disclosure, source_object and caption bodies; page furniture stays
 separate. Old tests used prose-typed fixtures and missed real omissions; red
 regression tests now pass. Non-author bytes cannot inherit an old author-only
 source review. Exact chapter IDs prevent duplicate-title export contamination.
- Query policy `5f6b5f8fc49384cd697cdf76eda42c7d67892066c33bb1a4dd13221853222b9a`.
 Frozen v18 reader `5972c56b4c65cfa2f4b934d8b9664d98dd2f5cac4a9e0db2d9280ac44b5b166b`;
 library `9b2e64be1f758ace2e3ae0883e93a9a2ebfa3da9242b42c1d1efc4402fd2ce03`.

## V18 full transport reconstruction COMPLETE

`reader-transport-reconstruction-20261031-v18-v1.json`, exit0, all18 queries each
435 targets, full reassembly/resume/6000-token UTF8-byte upper bound/32KiB PASS.
No AI receipts or source acceptance created. Frozen runtime (four modules):
`transport-runtime-v18-20261031-v1/scripts/`; the current working library has since
changed for q32, so use frozen runtime to reproduce v18 checks.

- Abstract1,317,778chars/439batches/40resume replays.
- All-author20,102,568chars/5878batches/535replays.
- Explicit References980,521chars/726batches; Contents1,220,581/849;
 AI disclosure130,281/139. These are separate non-author requests, not author reads.
- Do not sum overlapping query texts or call these machine tests actual AI reading.
 Full15 author/query-family counts and exact per-paper hashes remain in the report.

## Current LIVE build: v19 - DO NOT restart/edit frozen modules

- Authoritative unified exec session **77373**, started
 `python scripts/build_text_corpus_v19.py`. It is rebuilding original native+
 53 accepted OCR manifests, create-only `reflow-20261031-v19`.
- Full prospective `span-origin-flow-full-20261031-v12.json` completed PASS:
435/11,552/954,866, errors0/review replay0, Contents352->352. Exact5 new proofs
bound. Driver/request `build-request-reflow-20261031-v19.json` frozen.
- New proofs are individually checked q29 word joins; q30 complete5 paragraphs
and inline raw-fragment placement; q31 preserve Summary+Abstract while separating
form/date; q32 preserve actual abstract child continuation before midpage Contents.
- Do NOT modify source_span_metrics.py,text_corpus.py,preview_span_origin_flow.py,
source_text_repairs.py,source_layout_reviews.py,source_absence_reviews.py,
resegment_text_corpus.py,corpus_queries.py,corpus_reader.py,index_text_corpus.py,
validate_text_corpus.py or build_text_corpus_v19.py until terminal success/failure.
- On completion inspect `integrity-reflow-20261031-v19.json`, not assumed counts.
Poll the SAME77373 handle. Missing/sparse output is not a reason to rerun.

## Individually checked q29–q32 repair scope

Source evidence/findings/proofs in `reviews/20261031/`, stage scripts:
`stage_q029_q030_q031_opening_repairs.py`, `stage_q032_mixed_contents_repair.py`.
Both preflights PASS, zero source acceptances or AI receipts.

- q29 P-A-2016-44845-998bce33: actual page1 how-/ever and deriv-/ing joined;
 candidate1978chars instead1982. No other wording/ligature rewrite.
- q30 P-A-2016-46830-92f43919: actual page1 five paragraphs; raw symbol fragments
placed within their surrounding sentences. Candidate2490chars/page1/6blocks.
Symbols/private glyphs/numeric correctness retained UNVERIFIED, no formula work.
- q31 P-A-2016-48649-e4d30266: actual pages1/2; Summary6 paragraphs+Abstract2,
both preserved, form/team/date separate. Source really prints January28,2014;
retain that metadata without changing canonical2016 path. Candidate2925chars.
- q32 P-A-2016-54164-57a2b533: actual physical pages1–4 checked. Page1 has seven
author paragraphs after submission instructions; page2 separate cover; page3
1 Abstract with genuine1.1 Non-Technical Explanation continues on page4 ABOVE
Contents. Old whole-page Contents inference stole FIVE author paragraph fragments.
New source-checked group transition defers Contents until its actual heading,
preserving Contents-page review flag. Red test reproduced omission; now passes.
Candidate7516chars/pages1,3,4/26blocks/23author paragraph fragments, instead6518.
Also source-checked tem-/perature joined. Cross-page logical paragraph join is
explicitly still PENDING (sentence remains in adjacent fragments); don't certify
full continuity or source fidelity. Later pages remain unreviewed.
- New library hash for v19 is
`3867c31c79df6a653f63f1bbc085deb48daa6f5dd4968b76142f227031394a94`.
No general heading heuristic was weakened to erase Contents candidates.

## Actual AI reading - v16, fixed old runtime, no mixed cursors

- Run `reading-runs/abstract-preview-20261030-v16`, ID
`541d2520dc494e22a4ae952bd718d398`, dataset
`7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65`.
- **38 manually acknowledged batches000000–000037**, cursorpaper_index42/offset0:
throughq42,40 nonempty candidate abstracts fully processed,4 source-verified,
q5 verified absence/q11 empty unresolved separately. No pending batch. Nextq43.
- All newly read batches saved substantive per-paper observations/source issues
viaapply_patch BEFORE manualack. Q32 required2batches; old candidate fully read
but its missing page4 source text is not covered by those receipts.
- New working policy differs from v16; continue the SAME run only with its
unmodified previewv8 frozen runtime:
`python artifacts/skill-packages/text-corpus-preview-20261030-v8/mcm-icm-master-skill/scripts/corpus_reader.py --corpus-root artifacts/text-corpus/reflow-20261030-v16 next --run-dir artifacts/text-corpus/reading-runs/abstract-preview-20261030-v16`
Use same executable/root for ack/status. Do NOT call current reader to resume it,
reuse cursor against v18/v19, autoack, or combine version-specific reading counts.
- Oldv11 all-author23acks/q1end andv10 abstracts are separate preserved runs.
New batch-observed issues fromq29 onward stored in receipts; no automatic repair
closure/source approval has been inferred. Final all-chapter reading unaccepted.

## Packaging, checks, safety

- Latest installed-independent package remains previewv8/v16; no v18/v19 package,
no installed-skill overwrite. Previous smoke passed unrelated-cwd/default paths,
missing-library refusal,next/resume,0acks.49 installed preimages last checked
unchanged then; currentv18 validation freshly checked2,619 legacy preimages.
- Latest full suites **321pytest PASS15.70s /319unittest OK13.977s**. Explicit
`tests` path mandatory to avoid huge recursive artifact collection. Expected
negative-fixture statusfail output is not a suite failure. Most recent planPASS0.
- All old build/tests sessions completed, except currentv19 session77373.
Fullprospective35972 and v18transport83968 both completed exit0. Do not repoll
or restart completed jobs. No legacy history/progress transactions or cleanup.
- This context transported **8JPEGs/1,971,921bytes**: q29p1 291754;q30p1 303867;
q31p1 250083/p2 138157;q32p2 44502/p3 355876/p4 238704/p1 348978.
**NO MORE IMAGES until compaction.** PNGs stayed local. No subagents created.
- One accidentally overbroad rg command from PowerShell quoting was stopped by
its exact ownPID49044; no files deleted. Quote rg patterns with single quotes and
explicit file arguments. Do not dump Codex JSONL or base64.

Next: poll77373; validate real v19 outcome; preserve pending source/join/mapping
frontiers; continue actualq43 reading and individual source restoration in next
fresh image context. Whole database/source fidelity/all-chapter AI acceptance
remain unfinished; goal stays ACTIVE.
