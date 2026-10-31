# Checkpoint v27 — storage recovery, no reading advancement

Latest user priority: urgently recover F: after disk exhaustion. Recovery is
complete. Report: `../storage-recovery-20261031-v4/README.md`.

## Storage

- About 92 GiB / 99 GB of F: free space recovered, by lossless compression and
  SHA-256-verified NTFS hardlinks among frozen generated versions/packages.
- All 51 version/package directories retained; per-root file counts and logical
  byte counts match before/after exactly (1,128,586 paths, 123,098,056,594 bytes).
- 92,802 committed replacement paths independently rehashed: PASS.
- Original PDFs and all 2,619 protected historical inputs checked: PASS.
- No cleanup of originals, old learning outputs, reading runs/observations,
  transaction history, SQLite files, installed skills, or other projects.
- Read F:/MCM/AGENTS.md storage guard before any further build. No new complete
  corpus/package outputs on F:. Use the E: preflight with a real allocation
  estimate. Frozen hardlinks MUST NEVER be edited in place; use a new path.

## Exact database boundary

- Fully transport-tested checkpoint remains v48:
  `E:/MCM-text-corpus-work/artifacts/text-corpus/reflow-20261031-v48`, dataset
  `aaf55eb868a5960b60ba33baa87772579f18e35d8bbaad1e82e1efd69684b078`.
- V49 finished and structural/source-PDF/legacy validation passes. Dataset
  `e15fd3492c2b7a6e8b7278a8f3765e2e0d2c98d1d869e63f876010a97f71ed8b`:
  435 papers, 11,552 pages, 955,272 source lines, 290,380 blocks, 18,456 sections,
  48 verified boundaries, zero structural errors. Q327–330 summary source stages
  promoted. Source-completeness acceptance is still FALSE.
- V49 abstract/all-author transport reconstruction is NOT YET RUN. Do not count
  the storage validation as that test. Use frozen runtime-v49 for v49 validation;
  runtime tests previously passed (359 pytest / 357 unittest), not rerun here.
- Next source review queue paper is q331. Do not resume repeated full-copy
  builds without the new storage policy/headroom/reuse.

## Exact actual-reading boundary (unchanged during cleanup)

- All-author preview run remains frozen v46, using runtime-v44:
  `E:/MCM-text-corpus-work/artifacts/text-corpus/reading-runs/all-author-preview-20261031-v46`.
- Run ID `edfb83df62f84dc1ae49963b02270c5b`; dataset
  `14b2a806afc77d65652f359bdc1901959bc69869ff12935f3bd344a80f6b2e59`.
- 45 acknowledgements (000000–000044); cursor paper_index=3, char_offset=4136.
- Pending batch 000045 was actually read but has NO observation or ACK. Its
  completion marker is
  `d4d82f4a8b1717bb9fac9ce7691266c3897f6d5522fc89cc4192f28bdc7196c2`.
- Paper q4 `P-A-2010-7920-06d31c2b`, range 4136–6841. Read prose includes
  assumptions/return-to-qualifications, staged plan, baseball-audience objectives
  (answer, clarity, applicability, resiliency), evidence vs readability, and
  competing sweet-spot definitions. Preserve/flag draft bullet-heading and
  cross-page boundary defects. Record a real source-bound observation before ACK.
- Three candidate papers processed completely; source-verified complete papers
  remain zero. No cross-version receipts may be transferred.
- Older v16 abstract E: run remains 450 ACKs / 427 nonempty candidates processed,
  not original-source full-read acceptance. Mandatory corrections142/149/310
  still apply; original F: run remains untouched.

No new agents, installations, legacy learning transactions, full-paper closures,
formula correctness work or chart distillation. Long-term objective remains active.
