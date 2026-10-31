import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import commit_integrity_repair as repair


class CommitIntegrityRepairTests(unittest.TestCase):
    def test_wrong_preimage_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            path.write_bytes(b"other session's work")
            with self.assertRaises(ValueError):
                repair.replace_checked(path, b"replacement", repair.stage.digest(b"old"))
            self.assertEqual(path.read_bytes(), b"other session's work")

    def test_matching_hash_is_not_a_transaction(self):
        event = {"paper_id": "paper-a", "after": {"repair_run": "run-a"}}
        self.assertTrue(repair.committed_correction([event], "paper-a", "run-a"))
        self.assertFalse(repair.committed_correction([event], "paper-a", "run-b"))
        self.assertFalse(repair.committed_correction([], "paper-a", "run-a"))

    def test_final_binding_is_checked_after_rolling(self):
        history = [{"event_id": "event-a"}]
        order = []
        with mock.patch.object(repair.tx, "load_history", return_value=history), \
             mock.patch.object(repair.rolling, "validate_window", side_effect=lambda *a: order.append("rolling") or {"status": "pass"}), \
             mock.patch.object(repair.update_progress, "atomic_write"), \
             mock.patch.object(repair.tx, "validate_history", side_effect=lambda *a: order.append("chain") or []), \
             mock.patch.object(repair.tx, "validate_declared_artifacts", side_effect=lambda *a: order.append("binding") or []):
            result = repair.verify_live_tail()
        self.assertEqual(order, ["rolling", "chain", "binding"])
        self.assertEqual(result["latest_event"], "event-a")


if __name__ == "__main__":
    unittest.main()
