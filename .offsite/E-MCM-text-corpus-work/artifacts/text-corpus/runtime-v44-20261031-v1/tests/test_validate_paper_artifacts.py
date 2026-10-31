from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_paper_artifacts.py"
SPEC = importlib.util.spec_from_file_location("validate_paper_artifacts", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ObservationCorpusTests(unittest.TestCase):
    def write_jsonl(self, path: Path, records: list[dict[str, str]]) -> None:
        path.write_text(
            "".join(json.dumps(record) + "\n" for record in records),
            encoding="utf-8",
        )

    def test_index_combines_current_and_prior_papers(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            current_path = directory / "current.jsonl"
            prior_path = directory / "prior.jsonl"
            current = [{"observation_id": "O-A-current", "paper_id": "P-A-current"}]
            self.write_jsonl(current_path, current)
            self.write_jsonl(
                prior_path,
                [{"observation_id": "O-A-prior", "paper_id": "P-A-prior"}],
            )

            index = MODULE.build_observation_index(current_path, current, directory)

            self.assertEqual(set(index), {"O-A-current", "O-A-prior"})

    def test_duplicate_id_in_corpus_fails(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            current_path = directory / "current.jsonl"
            prior_path = directory / "prior.jsonl"
            current = [{"observation_id": "O-A-shared", "paper_id": "P-A-current"}]
            self.write_jsonl(current_path, current)
            self.write_jsonl(
                prior_path,
                [{"observation_id": "O-A-shared", "paper_id": "P-A-prior"}],
            )

            with self.assertRaisesRegex(ValueError, "duplicate observation_id"):
                MODULE.build_observation_index(current_path, current, directory)


class ProtocolV2CrossValidationTests(unittest.TestCase):
    def test_declared_language_count_must_match_record(self):
        card = {
            "paper_id": "P-A-2010-6749-395f556a",
            "protocol_v2_records": {
                "language": {
                    "path": "artifacts/language-units/P-A-2010-6749-395f556a.json",
                    "schema_version": 3,
                    "unit_count": 19,
                    "chapters": ["abstract"],
                    "review_status": "validated",
                }
            },
        }
        language_record = {
            "schema_version": 3,
            "paper_id": card["paper_id"],
            "available_chapters": ["abstract"],
            "units": [{"language_unit_id": f"LU-A-{index}"} for index in range(18)],
            "review_status": "validated",
        }

        errors = MODULE.validate_protocol_v2_records(card, language_record, None)

        self.assertTrue(any("unit_count" in error for error in errors))

    def test_declared_model_counts_and_status_must_match_record(self):
        card = {
            "paper_id": "P-A-2010-6749-395f556a",
            "protocol_v2_records": {
                "models": {
                    "path": "artifacts/model-units/P-A-2010-6749-395f556a.json",
                    "model_count": 2,
                    "equation_count": 3,
                    "review_status": "validated",
                }
            },
        }
        model_record = {
            "paper_id": card["paper_id"],
            "models": [
                {"model_id": "M-A-1", "governing_equations": [{"equation_id": "EQ-1"}]},
                {"model_id": "M-A-2", "governing_equations": [{"equation_id": "EQ-2"}]},
            ],
            "review_status": "source-checked",
        }

        errors = MODULE.validate_protocol_v2_records(card, None, model_record)

        self.assertTrue(any("equation_count" in error for error in errors))
        self.assertTrue(any("review_status" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
