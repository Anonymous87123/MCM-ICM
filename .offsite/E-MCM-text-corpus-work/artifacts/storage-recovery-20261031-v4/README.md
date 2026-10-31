# F: storage recovery — completed and verified

## Outcome

- Before recovery, F: had 585,728 bytes available.
- At the end of the last deduplication pass: 99,273,576,448 bytes available.
- A later final volume check reported 98,890,084,352 bytes available (about
  92.1 GiB / 98.9 GB). Available space is a live volume measurement, not a
  promise that unrelated system/process activity cannot change it.
- No version directory, paper, source PDF, section, reading run, observation,
  transaction history, or SQLite database was deleted.
- The same 51 generation/package directories contain the same 1,128,586 file
  paths by per-root count and the same 123,098,056,594 logical bytes. Before/after
  per-root file counts and logical byte counts have ZERO differences.
- Hardlinks preserve the file paths and bytes but share physical allocation;
  summing folder sizes in Explorer can still double-count this shared content.

## Verified operations

| Journal | Committed replacements | Independent complete SHA-256 verification |
| --- | ---: | --- |
| `../storage-recovery-20261031-probe2/replacements.tsv` | 1 | PASS, 1 path |
| `../storage-recovery-20261031-v3/replacements.tsv` | 72,869 | PASS, 72,869 paths / 6,495 physical files |
| `replacements.tsv` | 19,932 | PASS, 19,932 paths / 5,167 physical files |
| Total | 92,802 | All committed paths match their recorded original content hashes |

Each journal's `verification.txt` contains the machine-generated result. The
one pending PREPARE at the end of v3 is the safely rejected overlong temporary
path, not a lost file or a successful replacement. V4 shortened temporary names
and completed the full pass, skipping 72,870 already-shared paths.

An initial lossless NTFS compression of the oldest preview package provided
emergency working space. Full details and cause evidence are in
`../storage-recovery-20261031-v3/README.md`.

## Source/history protection

`../storage-recovery-20261031-v3/protected-corpus-validation.json` was regenerated
with `--verify-pdfs --work-root F:/MCM/mcm-skill-work` and passed:

- 435 papers, 11,552 physical pages, 955,272 source lines;
- 2,619 protected historical inputs unchanged;
- no structural/hash errors; original PDF verification requested and passed;
- text source fidelity remains unaccepted, as before. No new AI reading receipt
  or full-paper closure was created by this storage operation.

The frozen v49 dataset ID is
`e15fd3492c2b7a6e8b7278a8f3765e2e0d2c98d1d869e63f876010a97f71ed8b`.
This validation does NOT replace the still-pending v49 reader transport test.

## Prevention and maintenance

- F:/MCM/AGENTS.md now forbids new full corpus/package outputs on F: and requires
  a positive allocation estimate, 2x headroom and at least 20 GiB reserved free
  space before a new large E: build or package.
- The new `assert_corpus_storage_budget.ps1` preflight passed nine positive and
  negative checks. Frozen historical builder code was not modified, so callers
  must execute this preflight; it is not an automatically injected hook.
- Frozen hardlinked files MUST NOT be edited/truncated in place. Corrections
  must use a NEW version/path. Unique evidence and all previous versions remain.

Final helper SHA-256:

- `reclaim_f_corpus_duplicates.ps1`:
  `ae20c8284edbd937d6d52ec1dd7c9771daeb51fb2bb7008c27b47034054e4f0a`
- `assert_corpus_storage_budget.ps1`:
  `db5fa637f37ba12de8923b42751b70e4569964bd03bd25ea04d6a35ab0eabace`

Other projects, unrelated processes, installed skills, formula verification and
figure distillation were not touched. Large corpus construction remains stopped
for this cleanup turn; the long-term learning/database objective is not complete.
