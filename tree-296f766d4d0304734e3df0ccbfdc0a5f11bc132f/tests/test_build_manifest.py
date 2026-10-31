from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build_manifest.py"
SPEC = importlib.util.spec_from_file_location("build_manifest", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ClassificationTests(unittest.TestCase):
    def classify(self, value: str):
        return MODULE.classify(Path(value))

    def test_old_outstanding_filename_is_eligible(self):
        record = self.classify("2010\u7f8e\u8d5b\u7279\u7b49\u5956/A-6749-Outstanding.pdf")
        self.assertTrue(record["eligible_paper"])
        self.assertEqual(record["problem_type"], "A")
        self.assertEqual(record["award_status"], "outstanding")
        self.assertEqual(record["year"], "2010")

    def test_finalist_in_other_award_folder_is_eligible(self):
        record = self.classify(
            "2013\u7f8e\u8d5b\u7279\u7b49\u5956/\u5176\u4ed6\u5956\u9879/C-21165-Finalist.pdf"
        )
        self.assertTrue(record["eligible_paper"])
        self.assertEqual(record["document_role"], "award-paper-finalist")
        self.assertEqual(record["problem_type"], "C")

    def test_meritorious_is_excluded(self):
        record = self.classify(
            "2013\u7f8e\u8d5b\u7279\u7b49\u5956/\u5176\u4ed6\u5956\u9879/A-19064-Meritorious.pdf"
        )
        self.assertFalse(record["eligible_paper"])
        self.assertEqual(record["document_role"], "other-award-paper")

    def test_plain_numeric_pdf_in_type_folder_is_eligible(self):
        record = self.classify("2020\u7f8e\u8d5b\u7279\u7b49\u5956/D/2013140.pdf")
        self.assertTrue(record["eligible_paper"])
        self.assertEqual(record["problem_type"], "D")
        self.assertEqual(record["award_evidence"], "primary-type-folder")

    def test_named_2018_folder_is_eligible(self):
        record = self.classify(
            "2018\u7f8e\u8d5b\u7279\u7b49\u5956/E\u98987\u7bc7/E72968-SPEC.pdf"
        )
        self.assertTrue(record["eligible_paper"])
        self.assertEqual(record["problem_type"], "E")

    def test_problem_document_is_context(self):
        record = self.classify(
            "2024\u7f8e\u8d5b\u7279\u7b49\u5956/problems/2024_MCM_Problem_A.pdf"
        )
        self.assertFalse(record["eligible_paper"])
        self.assertEqual(record["document_role"], "problem-statement")
        self.assertEqual(record["problem_type"], "A")

    def test_result_document_is_context(self):
        record = self.classify(
            "2010\u7f8e\u8d5b\u7279\u7b49\u5956/Results/ICM-2010-Results.pdf"
        )
        self.assertFalse(record["eligible_paper"])
        self.assertEqual(record["document_role"], "results-document")

    def test_y_folder_is_out_of_scope(self):
        record = self.classify("2023\u7f8e\u8d5b\u7279\u7b49\u5956/Y/2312345.pdf")
        self.assertFalse(record["eligible_paper"])
        self.assertEqual(record["document_role"], "out-of-scope-problem-type")

    def test_conflicting_path_and_filename_is_quarantined(self):
        record = self.classify("2024\u7f8e\u8d5b\u7279\u7b49\u5956/A/B-12345-Outstanding.pdf")
        self.assertFalse(record["eligible_paper"])
        self.assertEqual(record["classification_status"], "conflict")
        self.assertEqual(record["document_role"], "unknown-quarantine")

    def test_non_pdf_data_is_context(self):
        record = self.classify("2019\u7f8e\u8d5b\u7279\u7b49\u5956/problems/data.csv")
        self.assertFalse(record["eligible_paper"])
        self.assertEqual(record["document_role"], "problem-dataset")


class SummaryTests(unittest.TestCase):
    def test_summary_counts_eligible_types(self):
        records = [
            {
                "eligible_paper": True,
                "problem_type": "A",
                "year": "2020",
                "relative_path": "a.pdf",
                "file_size_bytes": 10,
                "sha256": "a" * 64,
                "file_extension": ".pdf",
                "document_role": "award-paper-primary",
                "pdfinfo_status": "ok",
                "text_probe_class": "text-rich",
                "classification_status": "classified",
            },
            {
                "eligible_paper": False,
                "problem_type": None,
                "year": "2020",
                "relative_path": "b.csv",
                "file_size_bytes": 5,
                "sha256": "b" * 64,
                "file_extension": ".csv",
                "document_role": "problem-dataset",
                "pdfinfo_status": "not-applicable",
                "text_probe_class": "not-applicable",
                "classification_status": "not-classified",
            },
        ]
        summary = MODULE.build_summary(records)
        self.assertEqual(summary["record_count"], 2)
        self.assertEqual(summary["eligible_paper_count"], 1)
        self.assertEqual(summary["candidate_counts_by_type"]["A"], 1)
        self.assertEqual(summary["candidate_counts_by_type"]["F"], 0)

    def test_document_id_is_path_scoped_and_content_id_is_hash_scoped(self):
        root = Path("C:/corpus")
        digest = "a" * 64
        relative_one = "2020/A/one.pdf"
        relative_two = "2020/A/two.pdf"
        first = "D-" + MODULE.hashlib.sha256(relative_one.encode("utf-8")).hexdigest()[:12]
        second = "D-" + MODULE.hashlib.sha256(relative_two.encode("utf-8")).hexdigest()[:12]
        self.assertNotEqual(first, second)
        self.assertEqual("C-" + digest[:12], "C-aaaaaaaaaaaa")


if __name__ == "__main__":
    unittest.main()
