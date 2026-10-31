from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_plan_protocol.py"
SPEC = importlib.util.spec_from_file_location("validate_plan_protocol", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PlanProtocolValidationTests(unittest.TestCase):
    def test_live_plan_passes_language_first_protocol_lint(self):
        plan = Path(__file__).resolve().parents[2] / "plan.md"
        self.assertEqual(MODULE.validate_text(plan.read_text(encoding="utf-8")), [])

    def test_legacy_model_first_step_is_rejected(self):
        plan = Path(__file__).resolve().parents[2] / "plan.md"
        text = plan.read_text(encoding="utf-8") + "\nStep 7 - Reconstruct Every Core Model\n"
        errors = MODULE.validate_text(text)
        self.assertTrue(any("banned legacy workflow" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
