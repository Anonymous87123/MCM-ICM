# Superseded before any installation

This create-only generation preserved the source and passed link checks, but subsequent full-field inspection found stale duplicate annotations: `rhetorical_move` still held the old function, and `features.transition` still held old information order for changed units. The narrow link validator does not check these duplicates, so its pass was insufficient for attribution consistency. No original artifact or this generation's hashed bytes were overwritten.

The working recipe and tests were corrected to synchronise the duplicate annotations and compare the entire result with the reviewed revision. A later create-only generation must be used. This pack was never installed or appended as a closure; preserve it as evidence of the failed attempt.
