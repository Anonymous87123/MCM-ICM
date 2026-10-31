# Complete text corpus checkpoint - 2026-10-31, v1

Goal ACTIVE: all435 papers/11,552 pages, continuous traceable source text,
exhaustive section reader, separate installable skill, and actual AI reading of
ALL corresponding substantive chapters. Abstracts are the first checkpoint.
Root only; no new agents. Formula correctness and chart interpretation paused.
Preserve every existing generation, artifact, installed file and transaction.

## Completed immutable datasets

- Latest v17: `reflow-20261030-v17`, dataset
  `da7a1a9751192380e4ad169cb570f8d7b9ade8ed44e9b3fae744332fd2bf6667`.
  `integrity-reflow-20261030-v17.json` PASS/errors0:435 papers,11,552 pages,
  954,866 raw lines,292,454 blocks,18,523 candidate sections,5 boundary reviews,
  2,619 protected legacy inputs unchanged. Source completeness FALSE; zero
  whole-paper source acceptance. No full learning closure or history changes.
- V17 interrupted after index/export; do NOT rerun. `finalize_text_corpus_v17.py`
  verified all frozen hashes/source proofs and completed full validation, exit0.
  Recovery report `finalization-recovery-v17-20261031-v1.json` retained.
- V16 dataset `7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65`
  complete, structural PASS,292,456 blocks. Its actual reading run stays pinned
  here; never reuse its cursor against v17 or later generations.
- No live build/transport/package process remains as of this checkpoint.
  Old handles2868/42944/5975/6158/18096/63262/58797/56758 are completed or absent.
  Rebuild only from original `native-20261029-v1` and53 accepted OCR manifests,
  never from an already OCR-augmented raw tree.

## Source repairs and pending scope

- V17 applied4 checked proofs: q6 determine word join; q12 page1 Summary vs page2
  cover and two bullet transcriptions; q333 page1 left-column Summary and pages2/3
  printed1.0/1.1/2.0 hierarchy. All raw lines retained exactly once.
  q12 abstract2129chars/page1; q333 abstract2073chars/page1, formerly42535chars
  spanning17 pages. These bounded checks are NOT full section/paper acceptance.
- Q14 summary/handout layout is STAGED ONLY:
  `reviews/20261030/q014-summary-handout-layout-v1.json`; actual pages1/2 checked.
  Separate marketing handout retains author prose with explicit column flow.
  Candidate Summary2677chars/page1 rather than4222incl handout. Needs next build.
- Previous q164 appendix, q165 prose/absence, q170 absence proofs already applied;
  do not repeat. Six source-local abstract absences,427 nonempty candidates and
  two empty unresolved(q11/q169) remain distinct. Whole-source overview work on
  q11/q169 incomplete; do not claim absence. Unicode OCR3papers/19blocks/11pages
  prepared but unverified/unapplied,766lines/152low-confidence. Preserve.
- V17 open flags include18,518 boundary reviews,9,745 hyphen reviews,5,482 private
  glyph reviews,5,116 cross-page joins,1,850 cross-engine conflicts,352 Contents,
  469 inline prose flow,223 OCR candidates,90 columns,19 unresolvedUnicode blocks.
  Flags overlap, are not a count of proven errors, and source fidelity is unpassed.

## Reader, actual reading, package

- Query policy frozen in v16/v17:
  `c26f5c67458329152efdc1d4cbc48df604d0b90cf890c44216a2ffcd8df1ff2f`.
  Author queries exclude descendant Contents/References/AI disclosure. Existing
  source-bound canonical section_text must remain stable for review hashes.
- V16 machine transport all15queries/435targets PASS, exact reassembly/restart,
 6000 token UTF8-byte upper-bound/32KiB. Abstract1,359,825chars450batches;
  all-author20,104,003chars5878batches. No AI receipts from machine tests.
- Actual v16 abstract run `reading-runs/abstract-preview-20261030-v16`, runID
  `541d2520dc494e22a4ae952bd718d398`:23 receipts throughq28,26 nonempty candidate
  abstracts processed,4 source-verified, q5 absent andq11 unresolved separately.
  Pending batch000023/q29 was fully read; its observation has now been saved,
  acknowledge exact saved marker next. No source-fidelity promotion.
- V11 author23acks/q1 candidateEND and v10 abstract25 candidates are separate
  old-version runs, never add them to the v16 counts.
- Preview v8 package `artifacts/skill-packages/text-corpus-preview-20261030-v8/`
  holds v16,22653 payload files. Packaged validation and unrelated-cwd default
  lookup/missing-library refusal/start-next-resume smoke PASS; smoke creates0acks.
  49 installed-skill preimages unchanged, no installation. Final source and all
  chapter reading acceptance remain pending.
- Latest full suites:315 pytest PASS/313 unittest OK. Always specify `tests`:
  bare pytest recursively collects huge artifacts. Its own stalled process was
  stopped; no files deleted. Plan protocol most recent PASS0.

## Immediate code task - confirmed real export/query mismatch

`export_document` and SQLite sections still use canonical section_text, so author
chapter exports can include nested non-author sections despite corrected reader
policy. Explicit non-author requests also drop actual typed references/contents/
ai_disclosure/source_object bodies because section_blocks allows PROSE_KINDS only.
Existing tests use prose-typed fixtures and missed this. Fix derived export/query
views with real-kind tests, keep canonical review hashes stable. New immutable
generation must bind new query policy and include stagedq14 proof. Full prospective
raw-line/review replay required before building. Do not mutate old generations.

Continue sequential actual reading with substantive per-paper observations; pending
delivery is not processing. Save structured source issues without inventing repair
or acceptance. Full objective remains ACTIVE, not complete or blocked.
