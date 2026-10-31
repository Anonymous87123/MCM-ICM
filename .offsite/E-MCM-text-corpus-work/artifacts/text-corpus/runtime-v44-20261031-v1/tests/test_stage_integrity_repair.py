import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import stage_integrity_repair as repair


class StageIntegrityRepairTests(unittest.TestCase):
    def test_create_only_preserves_existing_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            repair.put_new(path, b"original")
            with self.assertRaises(FileExistsError):
                repair.put_new(path, b"replacement")
            self.assertEqual(path.read_bytes(), b"original")

    def test_link_correction_preserves_substantive_data_and_counts(self):
        card = {"models": [{"equation": "x=y"}], "protocol_v2_records": {
            "language": {"unit_count": 61, "chapters": ["abstract"]},
            "models": {"model_count": 2, "equation_count": 9},
        }}
        before = copy.deepcopy(card)
        result = repair.canonical_links(card, "P-F-2022-example-aaaaaaaa", {}, {"schema_version": 2})
        self.assertEqual(card, before)
        self.assertEqual(result["models"], before["models"])
        self.assertEqual(result["protocol_v2_records"]["language"]["unit_count"], 61)
        self.assertEqual(result["protocol_v2_records"]["models"]["equation_count"], 9)
        self.assertEqual(result["protocol_v2_records"]["models"]["schema_version"], 2)
        self.assertEqual(result["protocol_v2_records"]["language"]["path"],
                         "artifacts/language-units/P-F-2022-example-aaaaaaaa.json")


if __name__ == "__main__":
    unittest.main()
