from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_model_units.py"
SPEC = importlib.util.spec_from_file_location("validate_model_units", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def condition(status: str = "not-applicable", details: list[str] | None = None) -> dict[str, object]:
    return {"status": status, "details": details or []}


def variable(symbol: str, role: str) -> dict[str, object]:
    return {
        "symbol": symbol,
        "normalized_name": symbol.strip("\\"),
        "role": role,
        "unit": "dimensionless",
        "definition": f"Definition of {symbol}",
        "source_status": "explicit-defined",
    }


def model_unit(model_id: str = "MU-A-2011-9665-ENERGY-001") -> dict[str, object]:
    return {
        "model_id": model_id,
        "page": 7,
        "section": "Dynamics analysis",
        "family": "mechanistic energy balance",
        "purpose": "Relate platform height to takeoff speed.",
        "base_or_modification": "paper-specific",
        "summary": "Balances gravitational potential energy and dissipative work.",
        "variables": [variable("m", "parameter"), variable("g", "parameter"), variable("h", "input"), variable("v", "output")],
        "inputs": ["m", "g", "h"],
        "outputs": ["v"],
        "governing_equations": [
            {
                "equation_id": "EQ-A-2011-9665-ENERGY-001",
                "page": 7,
                "label": None,
                "source_expression": "mgh = 1/2 mv^2",
                "normalized_latex": "m g h = \\frac{1}{2} m v^2",
                "purpose": "Close the energy balance.",
                "variable_symbols": ["m", "g", "h", "v"],
                "source_type": "paper",
                "visual_checked": True,
                "transcription_confidence": "high",
            }
        ],
        "equation_status": {"status": "present", "reason": "The paper prints the governing balance."},
        "objectives": ["maximize takeoff height"],
        "constraints": ["positive platform height"],
        "conditions": {
            "initial": condition("present", ["The athlete begins from rest."]),
            "boundary": condition(),
            "equilibrium": condition(),
        },
        "parameter_estimation": {
            "status": "omitted-by-paper",
            "method": "No calibration method is reported.",
            "parameters": ["m", "g"],
        },
        "algorithm": {
            "status": "implemented",
            "steps": ["Substitute the design height.", "Solve the balance for takeoff speed."],
            "software": ["MATLAB"],
            "convergence_criteria": "not-applicable",
        },
        "assumptions": ["Mechanical losses not represented in this baseline are negligible."],
        "identifiability_feasibility": {
            "status": "partial",
            "analysis": "The symbolic solution is feasible, but parameter calibration is not demonstrated.",
        },
        "handoff_outputs": ["v"],
        "validation_refs": ["p. 18 numerical example"],
        "computational_cost": "Closed-form evaluation.",
        "strengths": ["Exposes the physical energy pathway."],
        "limitations": ["Loss terms are omitted in the baseline."],
        "missing_details": ["Parameter provenance is not reported."],
    }


def valid_record() -> dict[str, object]:
    first = model_unit()
    second = model_unit("MU-A-2011-9665-FLIGHT-002")
    second["page"] = 11
    second["handoff_outputs"] = []
    return {
        "schema_version": 2,
        "paper_id": "P-A-2011-9665-6560aced",
        "problem_type": "A",
        "year": "2011",
        "source_sha256": "a" * 64,
        "models": [first, second],
        "dependency_edges": [
            {
                "from_model_id": first["model_id"],
                "to_model_id": second["model_id"],
                "handoff": "takeoff speed v",
            }
        ],
        "review_status": "validated",
    }


class ModelUnitValidationTests(unittest.TestCase):
    def test_valid_formula_level_record_passes(self):
        self.assertEqual(MODULE.validate_record(valid_record()), [])

    def test_equation_variables_must_resolve_to_model_variables(self):
        record = valid_record()
        record["models"][0]["governing_equations"][0]["variable_symbols"].append("rho")

        errors = MODULE.validate_record(record)

        self.assertTrue(any("undefined variable rho" in error for error in errors))

    def test_present_equation_requires_visual_check_and_normalized_latex(self):
        record = valid_record()
        equation = record["models"][0]["governing_equations"][0]
        equation["visual_checked"] = False
        equation["normalized_latex"] = ""

        errors = MODULE.validate_record(record)

        self.assertTrue(any("visual_checked" in error for error in errors))
        self.assertTrue(any("normalized_latex" in error for error in errors))

    def test_empty_equations_require_explicit_non_present_status_and_reason(self):
        record = valid_record()
        model = record["models"][0]
        model["governing_equations"] = []
        model["equation_status"] = {"status": "present", "reason": ""}

        errors = MODULE.validate_record(record)

        self.assertTrue(any("equation_status" in error for error in errors))

    def test_algorithm_and_conditions_cannot_be_silently_empty(self):
        record = valid_record()
        model = record["models"][0]
        model["algorithm"] = {"status": "implemented", "steps": [], "software": [], "convergence_criteria": ""}
        model["conditions"]["initial"] = {}

        errors = MODULE.validate_record(record)

        self.assertTrue(any("algorithm steps" in error for error in errors))
        self.assertTrue(any("conditions.initial" in error for error in errors))

    def test_dependency_edges_must_reference_known_distinct_models(self):
        record = valid_record()
        record["dependency_edges"].append(
            {
                "from_model_id": record["models"][0]["model_id"],
                "to_model_id": "MU-A-2011-9665-MISSING-999",
                "handoff": "unknown",
            }
        )
        record["dependency_edges"].append(
            {
                "from_model_id": record["models"][0]["model_id"],
                "to_model_id": record["models"][0]["model_id"],
                "handoff": "self",
            }
        )

        errors = MODULE.validate_record(record)

        self.assertTrue(any("unknown model" in error for error in errors))
        self.assertTrue(any("self dependency" in error for error in errors))

    def test_manifest_identity_and_page_bounds_are_enforced(self):
        record = valid_record()
        record["models"][0]["page"] = 31
        manifest = {
            "paper_id": record["paper_id"],
            "problem_type": "A",
            "year": "2011",
            "sha256": "b" * 64,
            "page_count": 30,
        }

        errors = MODULE.validate_record(record, manifest)

        self.assertTrue(any("source_sha256 differs" in error for error in errors))
        self.assertTrue(any("page exceeds" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
