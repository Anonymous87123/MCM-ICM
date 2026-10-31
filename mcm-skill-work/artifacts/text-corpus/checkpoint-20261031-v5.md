# Complete text corpus checkpoint — 2026-10-31,v5

Goal ACTIVE/unlimited:435papers/11,552physicalpages, continuous traceable prose,
exhaustive section reader, separate installable skill and actual AI reading of ALL
author chapters. Abstracts are only a checkpoint. Main agent/no new agents. Keep
all sources, old/failed generations, legacy history/artifacts and installed skills.
Formula correctness/figure interpretation paused; OCR/page checks only for prose.

## Latest accepted immutable corpus: v23

`reflow-20261031-v23`, dataset
`1050c96afd789a52e08a3e73f1b1a1d293c572f645765275e0e75c81d992479a`.
Integrity report DONEexit0/PASS/errors0:435papers/11,552pages/954,866source lines
exactly accounted,292,254blocks/18,521candidate sections/5boundary reviews,
2,619protected legacy preimages unchanged. Source completeness FALSE; zero
whole-paper source acceptance.427nonempty abstract candidates/6source-local
absences/2empty unresolved(q11/q169), only4source-verified abstracts. Source flags
remain explicit; do not count all machine paragraphs as source-verified prose.

V23applies individually checked q55/q58paragraphs and15literal repairs. Previous
q53complete summary/newspaper and earlier repairs retained. V22andallolder data
remain unchanged.

V23frozen runtime: `transport-runtime-v23-20261031-v1/scripts/`. The exact two
affected queries abstract/all_author_text DONEPASS in
`reader-transport-reconstruction-20261031-v23-v1.json`, each435targets,
1,309,306/20,102,961characters,436/5878batches,40/535resume replays.0AIreceipts.
V22six-query and v20all19query reports retained. Do not sum overlapping queries.

## LIVE job: v24 build — session71296

`python -X utf8 scripts/build_text_corpus_v24.py`
Output `reflow-20261031-v24`, expected report
`integrity-reflow-20261031-v24.json`. Last output: indexing completed candidate
dataset366a6ea8d0faf2a4e5ab2737590cb931c53ccfcc0344d7b21673697fc9b05569,
435/11552/292254blocks/18522sections; final validation still running.
POLL SAME71296; do not restart or promote until terminal PASS.

Do not edit the13frozen modules or driver while running:
source_span_metrics.py,text_corpus.py,preview_span_origin_flow.py,
source_text_repairs.py,source_layout_reviews.py,source_absence_reviews.py,
resegment_text_corpus.py,corpus_queries.py,corpus_reader.py,
source_paragraph_reviews.py,index_text_corpus.py,validate_text_corpus.py,
verify_reader_transport.py,plusbuild_text_corpus_v24.py.

Full prospectivev17DONEPASS:435/11552/954866,Contents352→352,0errors/replay
conflicts,4new proofs bound. Build checks all unrelated433abstract hashes unchanged.

## Individual q88/q92 repairs staged for v24

All5q88source pages1–5and3q92pages1–3actually inspected individually.

q88P-B-2010-8362-bd23db32:
- Cover/control/date/page numbers separately retained.
- Literal Summary Statement, page2,3paragraphs/1754characters.
- Literal Executive Summary, pages3–4,9logical author paragraphs including
salutation/closing,10source fragments/3527characters. Old query stopped at
`In addi-` and wrongly omitted page4. Now includes the complete operational
instructions and final wish of luck. Normalized abstract union5283characters.
-5source-literal edits:locations,missing space in drop off in, terminal addi-
hyphen removal,running,computers. Printed complied/asess retained.
- Exact guarded word link joins addi+tion; both repaired fragments/source offsets
remain unchanged. Later source pages6–33remain unreviewed.

q92P-B-2011-12114-03fd7440:
- Cover/control/date/page numbers separately retained; complete literal Summary
Statement page2,3paragraphs/2045characters. Page3Contents. No wording repairs.
- Later body unreviewed.

Proofs/findings/preflights `reviews/20261031/q088-opening-*` andq092equivalents;
stagers `stage_q088_opening_repair.py`, `stage_q092_opening_repair.py`.
Firstq88bundle check rejected a duplicate paper key because layout/paragraph
registries were combined. Corrected separate validation; existing3proof bytes
were compared/reused, never overwritten. Preflight nowDONEPASS.

## Core change / tests

`title_role` recognizes only literal opening Summary Statement(page≤3).
Paragraph separator may be empty ONLY with exact checked compound word and a
separately logged terminal hyphen repair with matching before/after hashes.
Ordinary checked space joins unchanged. No automatic lowercase/page-position
word joining. Rendering/independent transport both preserve exact block spans.

New3tests first RED,nowPASS; targeted5PASS. Full latest:
**331pytestPASS15.44s /329unittestOK14.316s**.
Use `python -m pytest tests -q`; an initial unscoped `pytest -q` crawled artifact
copies and was explicitly stopped as a known helper, then the scoped suite passed.
No tests/files were deleted. Expected negative fixture prints statusfail normally.

## Separate preview package v10 DONE

`artifacts/skill-packages/text-corpus-preview-20261031-v10/mcm-icm-master-skill`
is acceptedv22preview,notv23/v24.22804files; base installed skill untouched.
SmoketestDONEPASS from unrelatedcwdC:/Users/Lenovo:relative attachment loads,
435targets,missing database fails without fragment fallback,pending resume
identical,0AIacks. Report `package-smoke-v10-20261031/report.json`.
Installed base is C:/Users/Lenovo/.claude/skills/mcm-icm-master-skill.
Do not install/overwrite it. Packagev11forv24has NOT started yet.

## Actual reading: old immutable v16 / previewv8 runtime ONLY

Run `reading-runs/abstract-preview-20261030-v16`, runID
541d2520dc494e22a4ae952bd718d398,dataset
7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65.
Current100acks000000–000099,cursorpaper_index100,char0:throughq100.
97nonempty candidates fully processed;2existing absences(q5/q94),q11empty
unresolved.4source-verified-and-processed. No pending batch. Nextq101notyet
requested. Every observation manually written after actual text reading; no
automatic acknowledgments. Candidate traversal is NOT source completeness.

Use only:
`python artifacts/skill-packages/text-corpus-preview-20261030-v8/mcm-icm-master-skill/scripts/corpus_reader.py --corpus-root artifacts/text-corpus/reflow-20261030-v16 next --run-dir artifacts/text-corpus/reading-runs/abstract-preview-20261030-v16`
Same runtime/rootforack/status. Do not mix old receipts/new datasets/policies.
Do not sum other old abstract/all-author reading runs.

New observations000088–000099coverq88–100. Important defects recorded:
q88realExecutiveSummarycut, q89title/page contamination, q91typosvsrecognition
uncertain, q92cover/header,q93damagedposter/sidebar interleaving and Strengths
sentence, q95frontmatter/paragraphs,q96realSummarycut at less flexibility in
their, q97inline display prose flow,q98missing first-page prose fragments/form
labels/escaped percent/footer,q99wraps/footer,q100false purpose-paragraph break
and uncertain fourth-model omission. No missing sentence invented from duplicates.

## All-paper cap census / next individual source cases

`audit_summary_page_cap.py` checkedall435stored documents and found6inferred
body transitions immediately after an abstract. Complete report:
`reviews/20261031/summary-page-cap-census-v23-v1.json`.
q54,q88,q96,q113,q213,q397. These are hypotheses, not6proven omissions.
q88/q96literal continuations are evident in following stored full-text blocks;
q88physicallychecked/fixinv24. q54/q213heavywatermark/body scope needs source;
q113/q397may be legitimate title transitions but remain source-unverified.

Prepared but NOT YET VISUALLY INSPECTED this segment:
- `q093-opening-pages-v1`,physical1–3. Page1alreadyRapidOCRcandidate(86lines,
version3.9.2),notnative-only; do NOT blindly rerun the same OCR. Need individual
poster/main-prose lanes and damaged Strengths sentence restoration.
- `q096-opening-pages-v1`,physical1–5. Page3Summaryendsmid-sentence;page4native
continues potential destination sites than motor boats. Need source check,
complete Summary and separate memo ownership. No source acceptance yet.

This context used **8JPEGs/1,304,148bytes**:q88p1–5,q92p1–3. NO MORE IMAGES
until compaction. Prepared q93/q96JPEGs have NOT enteredcontext. No rawPNG,
newagents,legacytransactions,installedwrites,deletes or cleanup.

Next:poll71296;afterPASSfreezev24runtime,affectedtransport,andnewseparate
previewpackage/smoke as appropriate. Continueactualreadingq101onwards;after
freshcontextimagebudget repairq96/q93individually and remaining defects. All
author chapters/source acceptance remain required; goal staysACTIVE.
