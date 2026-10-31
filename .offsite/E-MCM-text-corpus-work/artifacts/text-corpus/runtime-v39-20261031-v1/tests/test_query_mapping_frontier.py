from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_query_mapping_frontier import audit
from test_text_corpus import fixture
from text_corpus import file_hash


class MappingFrontierTests(unittest.TestCase):
    def test_unmapped_parts_keep_every_paper_and_do_not_turn_into_absence_or_samples(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog = fixture(root, count=3)
            before = {str(p): file_hash(p) for p in root.rglob('*.json')}
            report = audit(root, ('abstract', 'task_1', 'problem_analysis'))
            self.assertEqual(report['totals']['papers_checked'], 3)
            self.assertEqual(report['totals']['empty_unresolved_paper_query_pairs'], 6)
            self.assertEqual(report['query_status_counts']['task_1'], {'unresolved': 3})
            self.assertEqual([p['paper_id'] for p in report['papers']], [p['paper_id'] for p in catalog.papers])
            for paper in report['papers']:
                self.assertEqual(paper['empty_unresolved_queries'], ['task_1', 'problem_analysis'])
                self.assertEqual(paper['source_local_verified_absent_queries'], [])
                self.assertEqual(len(paper['complete_stored_chapter_map']), 2)
                self.assertEqual(paper['complete_stored_chapter_map'][0]['printed_title_or_candidate_label'], 'Summary')
                self.assertEqual(paper['complete_stored_chapter_map'][1]['parent_id'], 's1')
            self.assertFalse(report['source_fidelity_approved'])
            self.assertFalse(report['ai_reading_acceptance'])
            self.assertEqual(before, {str(p): file_hash(p) for p in root.rglob('*.json')})


if __name__ == '__main__':
    unittest.main()
