# Complete text corpus checkpoint - 2026-10-30, v6

Goal ACTIVE: complete435-paper/11,552-page text corpus, exhaustive section reader,
installable new skill and ACTUAL reading of all corresponding author chapters.
Abstracts are the first checkpoint, not the final scope. Root only, no new agents.
No formula correctness, table-value checking or chart interpretation. Page proxies
and local OCR recover prose and ownership only. Preserve every old artifact,
generation, installed skill, failed draft, reading run and legacy transaction.

## Current completed immutable candidate: v15

- `reflow-20261030-v15/`, dataset
  `702f392ed59c6afcc612871bd626e630ca0a89928ed30638b87f8f7f65a8b0bd`.
- `scripts/build_text_corpus_v15.py` completed exit0;
  `integrity-reflow-20261030-v15.json`: structural PASS/errors0, all435 PDFs,
  11,552 physical pages,954,866 source lines accounted exactly once,292,456 blocks,
  18,523 section candidates,5 source-boundary reviews.2,619 legacy inputs unchanged.
- `source_completeness_accepted:false`. ZERO whole-paper source acceptance.
  Structured source, continuous full/section Markdown and SQLite exist for all435,
  but this is accounting/extraction completeness, not complete readable prose.
-427 nonempty abstract candidates;6 source-local absences(q5/q94/q162/q165/q167/q170);
  2 empty unresolved(q11/q169). Absence is not an abstract read. The strict verified
  nonempty selection count is4, not427. No source checks were waived.
- Parent v14 is preserved. Failed v13 remains rejected for split-line Contents
  regression; never promote or delete it. v15 prospective
  `span-origin-flow-full-20261030-v7.json`:435/11,552/954,866, errors0/replay0,
 352 prior Contents pages retained. It binds the exact four added source proofs.
- Rebuild ONLY from `native-20261029-v1` plus the same53 frozen OCR manifests.
  Do not reaugment an augmented raw tree: duplicate OCR IDs would result.

## Source-bound changes applied in v15

- q164 `P-C-2010-8088-e7ab6731`: actual overview03/pages10/11 checked.
  Page10 author continuation retained before `X References`; bibliography excluded
  from default author prose. Page11 is a landscape spreadsheet with its printed
  Appendix A label BELOW the object. Rotation0/actual source coordinates confirmed;
  no blind move of the label to the top. Source object remains before its label,
  both owned by the appendix instead of bibliography. All raw lines retained once.
  `q164-pages10-11-layout-findings-v1.json` and
  `q164-pages10-11-appendix-layout-v1.json`;7 groups/28 portable evidence files.
  Only these2 pages source-checked here; no other page/full-section approval.
- Source layout schema now permits a tightly bounded `source_object` immediately
  followed by a source-checked appendix caption through `trailing_label_group_id`.
  It preserves literal position and records the label's raw IDs. Non-appendix,
  wrong-kind/title, missing/nonadjacent label proofs reject. Tests red first/pass.
- q165 full20-page abstract-absence proof and pages9/10 prose repair are now APPLIED,
  no longer merely staged.27 groups preserve Figure2/3/4 author explanations and the
  complete Table5 reference sentence, separate source objects/captions. Page8/11
  mixed-source problems still pending. Old then-unread census limitations preserved.
- q170 `P-C-2011-9089-838e50df`: all20 native pages were previously read; all7
  bounded overviews are now actually checked. Direct Introduction -> Solutions ->
  Assessments -> Conclusions/Suggestions -> References, no independent abstract.
  Local conclusions are not substituted for abstracts.604-record filename/token
  inventory found only this20-page source; independent strict UTF-8 extraction has
  zero Abstract/Summary word occurrences. New findings/absence proof applied;
 50 portable files. Source-local only, no external-archive completeness claim.
- Shared HEADING_NUMBER role normalization now covers bare Roman `X References`.
  Bounded body-font colon-Appendix heading candidates retained; q352 pages25/27 are
  NOT source-approved just because the detection rule recognizes them.

## Current live build: v16 - DO NOT restart or modify frozen modules

- Unified exec session **2868** is still the existing authoritative process handle.
  It ran309 pytest PASS14.38s, then full prospective audit, then started
  `scripts/build_text_corpus_v16.py`. Last observed child PID61160, created13:51:25;
  latest poll reached q375,400 paper dirs, no catalog/integrity report yet.
  Check/poll this SAME handle first. Sparse output is not a reason to rerun.
- `span-origin-flow-full-20261030-v8.json` completed:435/11,552/954,866,
  errors0/review replay0,352->352 Contents pages. It now fingerprints query/reader
  implementations as well as source/resegment code. `review_input_sha256:{}` means
  v16 replays the exact already-frozen v15 source proofs, not new source approvals.
- `build-request-reflow-20261030-v16.json` is frozen. Output create-only
  `reflow-20261030-v16/`, final report expected
  `integrity-reflow-20261030-v16.json`. No successful build/promotion claimed yet.
- Do NOT modify these frozen files while session2868 is running:
  `source_span_metrics.py`, `text_corpus.py`, `preview_span_origin_flow.py`,
  `source_text_repairs.py`, `source_layout_reviews.py`, `source_absence_reviews.py`,
  `resegment_text_corpus.py`, `corpus_queries.py`, `corpus_reader.py`.
- After terminal success, read the actual integrity report/dataset ID before
  reporting counts, testing transport, starting new runs or packaging. If it fails,
  preserve all state and diagnose; never overwrite/restart the existing directory.

## Corrected query policy being frozen in v16

Actual full-scope audit found8 papers/10 paper-query pairs/63 unique blocks of
explicitly non-author descendant subtrees leaking through named author queries.
`query-non-author-subtrees-20261030-v14-v1.json` and v15-v1 preserve the old policy.

- `corpus_queries.py` now excludes nested Contents/References/AI disclosure from
  EVERY default author query, including explicit tasks and exact author titles.
  All author children stay included; mention of references/AI inside an author
  paragraph is NOT filtered. Explicit non-author role/title queries still return
  separately preserved non-author text. Nothing is deleted from the corpus.
- Policy hash `c26f5c67458329152efdc1d4cbc48df604d0b90cf890c44216a2ffcd8df1ff2f`.
  Candidate audit `query-non-author-subtrees-20261030-v15-policy-candidate-v3.json`
  binds it and finds0 papers/0 pairs/0 leaking blocks. This does NOT certify other
  unclassified object leakage or correct source hierarchy.
- New reader sessions bind `query_policy_sha256` and reject policy change on
  resume/build. Strict start blocks when the frozen data query policy differs
  from the live reader; only explicitly labelled unverified preview may proceed.
  V15 therefore is NOT a strict data/reader release under the new policy. Waitv16.
- New package guard rejects mixed-policy packages even in preview. The route and
  reading reference templates describe nested exclusions, policy/version checks,
  no-card fallback, full observations/receipts and no automatic acknowledgments.
- Old run bytes/receipts remain untouched. `reader-policy-existing-run-compatibility-
  20261030-v11-v2.json`: all23 saved deliveries reconstruct exactly, no differences,
  all saved files unchanged, zero new receipts or AI reading acceptance.

## Real full-corpus transport reconstruction completed for v14

`reader-transport-reconstruction-20261030-v14-v1.json` (6,000 token ceiling) and
`reader-transport-reconstruction-20261030-v14-v2-small-budget.json` (3,000) both
complete/exit0. Each tests the exact production pure `build_batch` path for15
query families and435 targets, UTF-8 wire/end marker/budgets/ordered source spans,
per-paper hash reconstruction and deterministic resume. They create NO session,
delivery, observation or processing-receipt files; diagnostic reports only.

- Old-policy abstracts:1,359,841 chars;450 batches at6000,990 at3000.
- Old-policy all-author text:20,109,167 chars;5,880 batches/535 resume replays at6000;
 13,828 batches/1,258 replays at3000. All character/byte hashes match.
- Overlapping query texts must NOT be summed as unique text/AI reading. These
  tests do not approve mapping/fidelity/understanding and must not be relabelled
  as v16 tests. Rerun on v16 after it completes with its new frozen query policy.
- `verify_reader_transport.py` now binds query policy in its simulated session.

## Whole-scope remaining defects / mapping frontier

V15 diagnostics cover all435/11,552 and are NOT source approvals; flags overlap.

- `section-candidate-audit-20261030-v15.json`:6 absences,2 empty unresolved,
 58 multipage abstract checks,2 fragmentation,33 possible form-contamination,
 1 envelope warning(q40 already source-checked false-positive; don't repeat).
- `contents-section-leakage-20261030-v15.json`:43 papers/44 candidate pages.
- `caption-prose-boundaries-20261030-v15.json`:122 papers/206 candidate blocks,
  reduced from123/209 through the actual q165 fixes, not a broad regex exemption.
- `non-author-section-leakage-20261030-v15.json`:0 explicit misnormalized
  non-author heading candidates. This is different from query-descendant leakage.
- `unicode-text-frontier-20261030-v15.json`:3 papers(q148/q237/q387),19 blocks,
 11 page locations,161 malformed codepoints. Some are inside author explanation.
- `query-mapping-frontier-20261030-v15-policy-candidate-v1.json`: complete18,523
  stored chapter maps;2,755 empty-unresolved paper-query pairs, all435 papers have
  at least one. Unknown means NOT YET MAPPED/ESTABLISHED, never genuine absence.
  New-policy Introduction405 present/30 unresolved; restatement194/241;
  analysis34/401; assumptions400/35; notation270/165; tasks1-4 present76/74/77/54,
  unresolved359/361/358/381; model/solution427/8; sensitivity/validation338/97;
  improvements/evaluation396/39; appendix157/278. All435 author-text candidates
  remain present-unverified. Removal of false Contents-only matches can increase
  unresolved counts without loss of raw source text.
- Open V15 flags: boundary18,518, hyphen9,746, private glyph5,484, cross-page5,116,
  cross-engine1,850, Contents352, inline-flow469, margin251, OCR223, columns90,
  spacing57, Summary-subheading5, openingLetter1, unresolvedUnicode19.

## Local OCR completed - UNVERIFIED, never whole-page applied

All3 local jobs completed exit0. Frozen artifacts:
`ocr-unicode-frontier-20261030-v1/<paper-id>/attempt-0001/`.

- q148 `P-B-2023-2315379-42733c7a`: pages5/8/9/10/11/13/15.
- q237 `P-C-2023-2310767-2f955db2`: page13.
- q387 `P-E-2025-2517273-98509d3b`: pages8/10/16.
- `unicode-ocr-evidence-binding-20261030-v14-v1.json`: exact full frontier coverage,
 3 papers/11 pages/766 OCR lines/152 lines below.95 confidence. Every page hash,
  source, coordinates/confidence census checked. Original frontier contexts bound.
  Literal repairs applied0; source approvals0; AI receipts0. The binder has2 tests.
- Pinned local RapidOCR3.9.2 models; no implicit model downloads, rasters only in
  local memory. New OCR is NOT among the53 accepted build manifests. Compare each
  damaged author region with source, preserve surrounding prose and uncertainty;
  don't infer symbols or reapply entire OCR pages to an augmented generation.

## Next source checks - no remaining image budget in this segment

- q333 `P-E-2017-61502-f0a50d47`: newly isolated real abstract hierarchy defect.
  Current `1.0 Introduction`/`1.1 Objective`/`2.0 Methodology` are children of inferred
  summary; abstract query wrongly expands to120 blocks/42,535 chars/pages1-17.
  `q333-abstract-parentage-frontier-v1.json` preserves diagnosis. Source JPEGs
  prepared in `source-reviews/q333-opening-20261030-v1/`, pages1/2/3, but UNREAD.
  Inspect them in next fresh segment; establish printed0-suffixed numbering and
  true abstract end before repairing hierarchy. Do not flatten real summary
  subheadings or infer task numbers from chapter numbers. Stage with other proofs,
  rather than rebuilding the entire corpus after every local correction.
- q11 `P-A-2012-14990-e2428f0d`: all42 native pages already read. Actual overview09
  pages28-30 now additionally checked; page29 is NOT blank but a reproduced
  third-party table, no independent author synopsis. Page30 author paragraph
  resumes below the continued object. `q011-pages28-30-layout-findings-v1.json`
  records the bounded check, not table values or whole-source absence. Previous
  opening1-3 proof preserved. Other whole-source overviews remain UNREAD.
- q169 `P-C-2011-8882-54492a1f`: all27 native pages already read; all9 full-source
  overviews still UNREAD. No source-local abstract absence approval.
- q165/q170 complete absence/layout checks must not be redone. q164 pages1-9 still
  unreviewed by its bounded2-page proof. Preserve exact limitations.

## Actual AI reading and packaging

- V11 actual all-author run remains23 manually acknowledged batches, cursor1/0,
  q1 candidate end,389 unique blocks/41 candidate sections. Source-verified complete
  author-text papers0. V10 abstract25 candidates throughq27 are separate old-version
  readings. Never sum versions or reuse their cursors in v16.
- No v14/v15/v16 actual-reading run created. No new processing receipts this segment.
  After v16 succeeds, establish its own version-bound run, read each full batch,
  save substantive per-paper observations, and only then manually acknowledge.
- Latest package still v7/v11 at
  `artifacts/skill-packages/text-corpus-preview-20261030-v7/mcm-icm-master-skill/`.
  No new package/install this segment. Installed base actually at
  `C:/Users/Lenovo/.claude/skills/mcm-icm-master-skill/`;49 original preimages freshly
  checked unchanged. New templates/package guard are tested working-code changes.
- After v16 success and transport tests, create a separate v8 preview package,
  NEVER overwrite v7 or installed base. Test relative attachment lookup from an
  unrelated cwd, missing DB failure, policy guard and actual bounded next output.
  Final package remains blocked by source fidelity AND actual all-chapter reading,
  not by permissions. Skill-creator used for precise routing/invariants; PDF skill
  used for source text/paragraph boundaries only.

## Fresh verification and safety

- Latest full pytest:309 PASS14.22s. Latest unittest:307 OK15.071s. Plan protocol
  PASS/errors0 with `--plan F:/MCM/plan.md`. Expected negative-fixture stdout is not
  a suite failure. Earlier mistaken no-argument plan invocation preserved in tool
  output; correct invocation subsequently passed. No need to rerun completed tests
  merely because a test fixture prints fail.
- Fresh after-test check:2,619 protected legacy preimages unchanged;49 installed
  master-skill preimages unchanged. No legacy history/progress updates, cleanup,
  source PDF mutation, existing artifact overwrite or child agent used.
- This segment actually transported8 JPEGs: q164 overview03 255,033 bytes;
  q170 overviews01-06 2,374,847 bytes; q11 overview09 265,672 bytes; total2,895,552.
  NO MORE IMAGES until compaction. Never batch images/output PNG/base64 or Codex
  session JSONL. New prepared q333 JPEGs have NOT entered model context.
- All previous local jobs completed except session2868/v16 build. Poll it first,
  then continue source restoration and real reading; the long-term goal is ACTIVE.
