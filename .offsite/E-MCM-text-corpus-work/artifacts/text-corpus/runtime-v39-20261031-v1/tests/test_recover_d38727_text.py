import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import recover_d38727_text as recovery


class D38727TextRecoveryTests(unittest.TestCase):
    def test_encoded_surrogate_pair_becomes_one_scalar(self):
        raw = "before \ud835\udc65 after".encode("utf-8", errors="surrogatepass")
        text, report = recovery.recover(raw)
        self.assertEqual(text, "before \U0001d465 after")
        self.assertEqual(report["recovered_pairs"], 1)
        self.assertEqual(report["unresolved"], [])
        text.encode("utf-8", errors="strict")

    def test_unpaired_surrogate_is_tagged_not_guessed_or_dropped(self):
        raw = "x\ud8351\udc36".encode("utf-8", errors="surrogatepass")
        text, report = recovery.recover(raw)
        self.assertEqual(text, "x[UNPAIRED-U+D835]1[UNPAIRED-U+DC36]")
        self.assertEqual(report["recovered_pairs"], 0)
        self.assertEqual(len(report["unresolved"]), 2)

    def test_valid_utf8_remains_unchanged_and_other_invalid_bytes_fail(self):
        text = "plain text \U0001f680 and \u03b1"
        self.assertEqual(recovery.recover(text.encode("utf-8"))[0], text)
        with self.assertRaises(UnicodeDecodeError):
            recovery.recover(b"bad\xff")

    def test_page_count_mismatch_is_not_padded_into_success(self):
        self.assertEqual(recovery.physical_pages(b"a\r\n\fb\f", 2), [b"a\n", b"b"])
        with self.assertRaisesRegex(ValueError, "physical page count"):
            recovery.physical_pages(b"one page", 19)

    def test_legacy_question_mark_view_is_separate_from_recovery(self):
        raw = "\ud835".encode("utf-8", errors="surrogatepass")
        self.assertEqual(recovery.legacy_view(raw), "?")
        self.assertIn("UNPAIRED", recovery.recover(raw)[0])

    def test_existing_output_is_not_modified(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            old = path / "old.txt"
            old.write_bytes(b"retained")
            with mock.patch.object(recovery.storage, "read_json") as reader:
                with self.assertRaises(FileExistsError):
                    recovery.build(path)
                reader.assert_not_called()
            self.assertEqual(old.read_bytes(), b"retained")


if __name__ == "__main__":
    unittest.main()
