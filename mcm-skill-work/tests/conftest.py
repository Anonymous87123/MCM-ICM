"""Make `scripts.*` importable no matter which directory pytest runs from.

Without this, `import scripts` resolves to the namespace package shipped with
pywin32 in site-packages, and every test that imports a `scripts` module fails
to collect.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
