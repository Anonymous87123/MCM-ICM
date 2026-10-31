from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import validate_language_anticopy as anticopy


def brute_force_longest_run(left: str, right: str) -> int:
    left_words = anticopy.words(left)
    right_words = anticopy.words(right)
    best = 0
    for left_start in range(len(left_words)):
        for right_start in range(len(right_words)):
            run = 0
            while (
                left_start + run < len(left_words)
                and right_start + run < len(right_words)
                and left_words[left_start + run] == right_words[right_start + run]
            ):
                run += 1
            best = max(best, run)
    return best


class ValidateLanguageAnticopyTests(unittest.TestCase):
    def test_indexed_longest_run_matches_reference_algorithm(self) -> None:
        cases = [
            ("alpha beta gamma delta", "zero beta gamma one"),
            ("repeat repeat alpha repeat beta", "repeat alpha repeat"),
            ("punctuation, Does Not Matter!", "does not matter here"),
            ("no shared sequence", "entirely different words"),
            ("a b a b a", "b a b a b"),
        ]
        for left, right in cases:
            with self.subTest(left=left, right=right):
                self.assertEqual(
                    anticopy.longest_run(left, right),
                    brute_force_longest_run(left, right),
                )

    def test_main_builds_the_source_index_once_for_all_units(self) -> None:
        unit = {
            "language_unit_id": "LU-1",
            "features": {
                "original_instantiations": [
                    {"text": "First independent example remains fully original."},
                    {"text": "Second unrelated illustration uses separate content."},
                ]
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = root / "record.json"
            source = root / "source.pdf"
            record.write_text(
                json.dumps({"units": [unit, {**unit, "language_unit_id": "LU-2"}]}),
                encoding="utf-8",
            )
            source.write_text("A source with language absent from both examples.", encoding="utf-8")
            output = io.StringIO()
            original = anticopy.build_source_profile
            with patch.object(
                anticopy, "build_source_profile", wraps=original
            ) as build_profile, redirect_stdout(output):
                result = anticopy.main(["--record", str(record), "--source", str(source)])

        report = json.loads(output.getvalue())
        self.assertEqual(result, 0)
        self.assertEqual(report["unit_count"], 2)
        self.assertEqual(report["status"], "pass")
        build_profile.assert_called_once()


if __name__ == "__main__":
    unittest.main()
