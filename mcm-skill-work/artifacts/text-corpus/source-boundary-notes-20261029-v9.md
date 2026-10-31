# Prose boundary review notes — v9 work, 2026-10-29

These notes record actual root-agent source checks. They do not certify complete
paragraph recovery, promote a whole paper, or resume non-text learning.

## q40: a real next section, not omitted abstract prose

- Paper `P-A-2018-86103-6d21eb9d`, physical page2.
- Source SHA256: `6d21eb9d0f1f13d61ef2df427746944e466a909d1ca692aac1a62a7e186d89fe`.
- Raw pages SHA256: `52c265e39183f0709c9150e58d841aaea7ea6f2b96607e010d2588e4d559f6f8`.
- Read the complete native page text and viewed
  `source-reviews/q040-abstract-page2-20261029-v1/page-0002.jpg` (316,718bytes).
- The page is a two-column short report. Its printed Abstract covers the upper
  left paragraph only. The separately printed Ocean wave model follows below;
  Transmission loss analysis starts the right column at the Abstract's height.
  Neither is an internal abstract heading. Do not absorb the whole page into Abstract.
- Therefore the envelope scanner's same-page warning is a reviewed false positive
  for abstract completeness, not an instruction to change the selection. It remains
  visible in the unannotated machine audit, rather than being silently removed.
- Other defects remain: generic Transmission loss analysis heading recognition,
  caption continuation classification, column-flow fidelity. No figure content was
  interpreted and no source-fidelity section approval is issued here.

## q174: structured Summary Sheet, layout still requires recovery

- Paper `P-C-2012-14531-6018365f`, physical page1.
- Source SHA256: `6018365f4456b37f2608d0c147748b8d16c8133c583091697e0e16041a894c66`.
- Raw pages SHA256: `5c06833474723f11d6d41044b75945f0143c9bc02e7eec1d4e324c626109d15d`.
- Read the complete native page text/coordinates and viewed its408,640byte proxy.
- The page is explicitly an official Summary Sheet. Problem Clarification,
  Assumptions, Model Design and Justification, Results and Sensitivity Analysis,
  Strengths and Weaknesses Discussion are structured summary lead-ins, not body
  chapters. The generic Summary-Sheet child-heading rule restores their parent scope
  as a candidate, with a new unresolved scope-review flag.
- Left KEY CONCEPT / KEY TECHNIQUES labels and their short entries are author
  callouts. They must be retained separately from the continuous right-column
  prose, not inserted by vertical coordinate into its sentences. This column/sidebar
  recovery is NOT yet implemented or accepted. The paper title also needs its own
  metadata boundary. Do not call this abstract source-verified.

## q182: internal Results belongs to Summary Sheet

- Paper `P-C-2014-28199-d39873d7`, physical page1.
- Source SHA256: `d39873d74e6588aee414def4d6ad5e344906c0a12650f9ab28970ad883fd9289`.
- Raw pages SHA256: `efc28fa25b9be1a15246a9e621648ab12bc2b855b78c23de83d6160aa464602b`.
- Read the complete native page text/coordinates and viewed its313,765byte proxy.
- The official Summary Sheet has Problem Clarification, Model Design and Results
  as internal headings; Results must not end the abstract query. The new parent
  rule recovers this scope as a candidate. Model Design and Problem Clarification
  still need exact heading/paragraph structure, and the diagram/caption stays
  separately retained without semantic review. No full abstract approval is issued.

## q162: complete source-local absence review staged

- Read all native text of physical pages1–10, not merely title/first paragraph.
- Checked five bounded page overviews covering every physical page, supplementing
  full text reading; searched all frozen604 manifest entries and source-root
  filenames for an in-scope alternative copy.
- `reviews/20261029/q162-abstract-absence-v1.json` records a source-local abstract
  absence conclusion with PDF/raw/evidence bindings. The document starts directly
  with Problem and Introduction and contains no independent summary elsewhere.
- This new review is staged, not applied to immutable v9. Thus v9's eight empty
  abstract queries remain unresolved in its own catalog until a guarded new build
  explicitly ingests the proof. It is not an abstract reading receipt or whole-paper
  source acceptance.

## Request-body and preservation

Eight proxies viewed in this context, each at most450,000bytes, total3,198,621bytes.
No more image calls in this context. All original images, prior generations and
legacy/installed artifacts are preserved. Formula checks/chart distillation stay paused.
