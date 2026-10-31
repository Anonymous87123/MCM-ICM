# Failed create-only proposal attempt — retained

Only `recipe.py` was created. No proposal files were generated and no live artifact was modified.

The first linking recipe incorrectly passed candidate 01's four preserved examples to an existing anti-copy function that deliberately requires exactly two examples per **language unit**. Its shared run was only 2, but the pair-count check correctly failed. This is an adapter error, not evidence of copying.

The corrected recipe scans the two original unit-level pairs separately, retaining all four examples in their shared pattern. The checker is unchanged, and no example is discarded merely to make the check pass. A later generation must use another create-only directory; this failed attempt is not overwritten.
