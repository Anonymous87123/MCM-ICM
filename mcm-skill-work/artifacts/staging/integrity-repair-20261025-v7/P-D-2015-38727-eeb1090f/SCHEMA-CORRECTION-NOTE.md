# Superseded draft adapter — not installed

The first linked proposal preserved 41 units, 68 witnesses and 82 examples, but its observation adapter used an object for `source_basis`, a string for `applicability`, and extra metadata fields. These are incompatible with the authoritative `schemas/observation.schema.json`, even though the older cross-artifact validator checks only required keys and did not reject them.

No live installation or transaction occurred. This generation is retained as evidence, not silently overwritten. The corrected later adapter uses a nonempty `source_basis` string, array-valued applicability/counterevidence and exactly the observation schema's declared fields. Rich occurrence/variant information stays in the pattern registry and mapping. Explicit negative regression cases cover this adapter failure.
