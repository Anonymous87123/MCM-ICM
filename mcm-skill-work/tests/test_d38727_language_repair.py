import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import stage_d38727_language_repair as repair


class D38727LanguageRepairTests(unittest.TestCase):
    def fixture(self, parent):
        root = parent / "work"
        root.mkdir()
        raw = b"synthetic source, never a real paper"
        source = parent / "MCM-ICM-master/fixture.pdf"
        source.parent.mkdir()
        source.write_bytes(raw)
        sha = repair.storage.digest(raw)
        paths = {
            "artifacts/corpus/manifest.jsonl": json.dumps({
                "paper_id": repair.PID, "problem_type": "D", "year": "2015",
                "relative_path": "fixture.pdf", "sha256": sha, "page_count": 19,
            }) + "\n",
            "artifacts/transactions/history.jsonl": "{}\n",
            "artifacts/progress.jsonl": "{}\n",
            f"artifacts/papers/{repair.PID}/extraction.json": "{}\n",
        }
        for kind, ext in [("language-units", "json"), ("paper-cards", "json"),
                          ("learning-audits", "json"), ("model-units", "json"),
                          ("observations", "jsonl")]:
            paths[f"artifacts/{kind}/{repair.PID}.{ext}"] = "{}\n"
        pages = {n: [] for n in range(1, 20)}
        for spec in repair.MECHANISMS:
            for page, _, _, excerpt in spec["occurrences"]:
                pages[page].append(excerpt)
        for n, excerpts in pages.items():
            paths[f"artifacts/papers/{repair.PID}/text/pages/page-{n:04d}.txt"] = "\n\n".join(excerpts)
        for name, text in paths.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return root, sha

    def test_existing_output_is_not_overwritten_or_read_as_a_new_run(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            keep = output / "previous.json"
            keep.write_bytes(b"original")
            with mock.patch.object(repair.language, "find_manifest_record") as loader:
                with self.assertRaises(FileExistsError):
                    repair.build(output)
                loader.assert_not_called()
            self.assertEqual(keep.read_bytes(), b"original")

    def test_witness_normalization_does_not_erase_semantic_changes(self):
        self.assertEqual(repair.normalized("Earth’s\n  archive"), "Earth's archive")
        self.assertNotEqual(repair.normalized("score 5.0"), repair.normalized("score 6.0"))
        self.assertNotEqual(repair.normalized("not improved"), repair.normalized("improved"))

    def test_build_preserves_live_inputs_and_missing_layout_gate(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root, sha = self.fixture(parent)
            before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
            output = parent / "candidate"
            with mock.patch.object(repair, "ROOT", root), mock.patch.object(repair, "SHA", sha), contextlib.redirect_stdout(io.StringIO()):
                repair.build(output)
            record = json.loads((output / "language-units.draft.json").read_text(encoding="utf-8"))
            report = json.loads((output / "validation.json").read_text(encoding="utf-8"))
            self.assertEqual(record["review_status"], "draft")
            self.assertEqual(record["layout_review_status"], "pending")
            self.assertNotIn("chapter_layouts", record)
            self.assertEqual(len(report["full_record_errors_retained"]), 7)
            self.assertEqual(report["status"], "draft-incomplete-not-committable")
            self.assertEqual(report["unit_structure_errors"], [])
            self.assertEqual(report["anticopy_failures"], [])
            self.assertEqual(report["original_example_count"], 2 * report["unit_count"])
            self.assertEqual(report["distinct_candidate_patterns"], report["unit_count"] - 1)
            for path, raw in before.items():
                self.assertEqual(path.read_bytes(), raw, str(path))
            for kind, ext in [("language-units", "json"), ("paper-cards", "json"),
                              ("learning-audits", "json"), ("model-units", "json"),
                              ("observations", "jsonl")]:
                self.assertEqual((output / "before" / f"{kind}.{ext}").read_bytes(),
                                 (root / f"artifacts/{kind}/{repair.PID}.{ext}").read_bytes())

    def test_changed_source_word_rejects_candidate_without_live_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root, sha = self.fixture(parent)
            page = root / f"artifacts/papers/{repair.PID}/text/pages/page-0001.txt"
            page.write_text("no confirmed witnesses", encoding="utf-8")
            before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
            with mock.patch.object(repair, "ROOT", root), mock.patch.object(repair, "SHA", sha):
                with self.assertRaisesRegex(ValueError, "unconfirmed source excerpt"):
                    repair.build(parent / "rejected")
            for path, raw in before.items():
                self.assertEqual(path.read_bytes(), raw, str(path))
            self.assertFalse((parent / "rejected/language-units.draft.json").exists())


if __name__ == "__main__":
    unittest.main()
