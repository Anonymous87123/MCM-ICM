# v13 promotion rejected — preserve all evidence

Dataset `4202b5277a50958f1acc017c8265a88ff9a40cb10bc0a081a84b53ca8805a71e`
is structurally valid, but is NOT the accepted successor to v12.

The whole-scope comparison found a classifier regression: requiring the page
number on the same native line as a leader stopped recognizing many previously
recognized Contents pages. Contents boundary candidates fell from345 to143;
section candidates rose from18,524 to20,355, including false body headings from
Contents. The resulting machine-draft counts cannot be used as source progress.

Three new regression tests first reproduced failures. The corrected implementation
preserves split-line leaders, also recognizes middle-dot leaders, bounds singular
Reference matching so Reference Frame is not bibliography, and recognizes the
source-printed Nomenclatures / A Letter to... roles. The first corrected full
formal suite had285 passing tests. Two additional prospective-audit guards now
require per-page preservation of old Contents candidates, not just aggregate counts.

V13's catalog, SQLite, frozen inputs, integrity report and all staged reviews stay
unchanged. The source-reviewed q94 absence and q1 paragraph groups remain usable
as separately bound evidence; they do not make this generation fit for promotion.
V12 remains the last non-regressing candidate until a new immutable build and its
whole-scope checks pass. No live installation, legacy transaction/progress write,
whole-paper source acceptance, formula validation or chart interpretation occurred.
