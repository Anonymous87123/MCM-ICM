import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_integrity_snapshot as audit


class IntegritySnapshotTests(unittest.TestCase):
    def test_existing_audit_is_create_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            path.write_bytes(b"previous audit")
            with mock.patch.object(audit.compliance, "load_progress") as loader:
                with self.assertRaises(FileExistsError):
                    audit.audit(path)
                loader.assert_not_called()
            self.assertEqual(path.read_bytes(), b"previous audit")

    def test_fingerprint_detects_changed_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "record.json"
            path.write_bytes(b"generation one")
            with mock.patch.object(audit, "ROOT", root):
                before = audit.fingerprints([path])
                path.write_bytes(b"generation two")
                self.assertNotEqual(before, audit.fingerprints([path]))

    def test_snapshot_includes_visual_gate_and_whole_evidence_corpus(self):
        with tempfile.TemporaryDirectory() as directory:
            artifact = Path(directory)
            (artifact / "observations").mkdir()
            extra = artifact / "observations/other-paper.jsonl"
            extra.write_bytes(b"{}\n")
            with mock.patch.object(audit, "ART", artifact):
                paths = audit.source_paths(["paper-a"])
            self.assertIn(extra, paths)
            self.assertIn(artifact / "papers/paper-a/extraction.json", paths)
            self.assertIn(artifact / "transactions/history.jsonl", paths)
            self.assertIn(artifact / "type-branches/F/rules.jsonl", paths)


if __name__ == "__main__":
    unittest.main()
