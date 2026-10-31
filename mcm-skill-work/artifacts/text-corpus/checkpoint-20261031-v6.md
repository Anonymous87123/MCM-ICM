# Complete text corpus checkpoint — 2026-10-31,v6

Goal ACTIVE: all435papers/11,552physicalpages; continuous traceable author prose,
exhaustive section reader, separate installable skill and actual AI reading of ALL
author chapters. Main agent only. Preserve sources, all old/failed generations,
legacy history/artifacts, installed skills and unrelated work. Formula correctness
and figure interpretation paused; OCR/page checks only for prose and boundaries.

## Accepted immutable corpus: v24

`reflow-20261031-v24`, dataset
`366a6ea8d0faf2a4e5ab2737590cb931c53ccfcc0344d7b21673697fc9b05569`.
Integrity DONE/PASS/errors0:435papers/11552pages/954866source lines exactly
accounted;292254blocks/18522candidate sections;5boundary reviews;
2619protected legacy preimages unchanged. Source completeness FALSE; zero
whole-paper source acceptance;427nonempty abstract candidates/6source-local
absences/2empty unresolved(q11/q169);only4source-verified abstracts.

V24applies individually inspected q88pages1–5 andq92pages1–3. Q88complete
Summary Statement plus Executive Summary through physicalpage4:5283characters,
12logical paragraphs;5literal repairs and exact addition cross-page word link.
Q92complete Summary Statement:2045characters/3paragraphs, cover/furniture
separated. Later bodies unreviewed. All preceding generations retained.

`reader-transport-reconstruction-20261031-v24-v1.json` DONE/PASS:
abstract/all_author_text each435targets,1310996/20102805characters,
437/5878batches,40/535resume replays; byte-exact reassembly and budgets pass.
Zero AI receipts/source acceptance from this test. Frozen runtime:
`transport-runtime-v24-20261031-v1/scripts/`.

## Separate preview v11 DONE/PASS

`artifacts/skill-packages/text-corpus-preview-20261031-v11/mcm-icm-master-skill`
contains v24,22878files. Smoke report `package-smoke-v11-20261031/report.json`:
default relative attachment works from unrelated cwd,435targets; missing database
fails closed; pending replay identical;0AIacks/full acceptance FALSE.
Installed base skill unchanged; no installation authorized/performed.

## Actual reading: old v16 / frozen previewv8 ONLY

Run `reading-runs/abstract-preview-20261030-v16`,ID
541d2520dc494e22a4ae952bd718d398,dataset
7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65.
116acks000000–000115; cursorpaper_index114,char0;throughq114.
111nonempty candidates processed,2existing absences(q5/q94),q11empty unresolved;
4source-verified-and-processed. No pending batch;nextq115notrequested.
All observations manual after text reading. Candidate processing is not source
completeness. Never mix runtime/query policies or sum overlapping reading runs.

Use packagedpreviewv8 corpus_reader.py with old reflow-20261030-v16 root for
next/ack/status. Current mutable runtime correctly rejects the old query policy.

Recent defects recorded in observations: q93damaged poster/sidebar order and
Strengths; q96Summary cut at 'less flexibility in their', following page continues;
q102/q112cross-page furniture inserted into prose; q107nontechnical article
wrongly scoped as abstract; q110same-page Summary internal headings escape query
and Contents pages are misclassified; q114Contents entry included as abstract,
actual Executive Summary physical29–30,s0041misclassified conclusion.
No formula/figure/model correctness judgments or new language cards/history.

## Tests / next work

Latest core tests331pytestPASS/329unittestOK. Guarded zero-space word join
requires exact compound plus separately logged terminal hyphen repair; source
fragments and offsets retained. No edits after that test run yet.

All435cap census v24finds5candidate transitions; these are hypotheses, not5
proved omissions. Prepared JPEG/native evidence NOT YET visually inspected:
q093physical1–3,q096physical1–5,q110physical1–4. Previous context used8JPEGs;
this checkpoint itself used no new images.

Next: add a continuous author-only Markdown plus source-span view (full.md
remains the all-block evidence export), in a NEW immutable generation; restore
q96/q93/q110individually, thenq114; continue actual reading fromq115.
No live build/package/transport jobs at this checkpoint. Do not poll completed
sessions71296/30899/2390. No cleanup, legacy transactions or installed writes.
