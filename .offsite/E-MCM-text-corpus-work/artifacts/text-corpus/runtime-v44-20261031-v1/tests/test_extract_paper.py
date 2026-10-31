from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "extract_paper.py"
SPEC = importlib.util.spec_from_file_location("extract_paper", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PageSelectionTests(unittest.TestCase):
    def test_all_pages(self):
        self.assertEqual(MODULE.parse_page_spec("all", 3), [1, 2, 3])

    def test_ranges_are_sorted_and_deduplicated(self):
        self.assertEqual(MODULE.parse_page_spec("3,1-2,2", 4), [1, 2, 3])

    def test_out_of_range_fails(self):
        with self.assertRaises(ValueError):
            MODULE.parse_page_spec("1,5", 4)

    def test_descending_range_fails(self):
        with self.assertRaises(ValueError):
            MODULE.parse_page_spec("3-1", 4)


class PageSplitTests(unittest.TestCase):
    def test_form_feed_split(self):
        pages, warnings = MODULE.split_pages("one\ftwo\f", 2)
        self.assertEqual(pages, ["one", "two"])
        self.assertEqual(warnings, [])

    def test_missing_pages_are_padded(self):
        pages, warnings = MODULE.split_pages("one\f", 3)
        self.assertEqual(pages, ["one", "", ""])
        self.assertEqual(len(warnings), 1)


if __name__ == "__main__":
    unittest.main()
