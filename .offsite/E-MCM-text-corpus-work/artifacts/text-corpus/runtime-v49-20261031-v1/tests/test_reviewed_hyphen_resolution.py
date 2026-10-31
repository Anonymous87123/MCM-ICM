import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_text_repairs import apply_text_repairs, replay_block, validate_hyphen_resolutions
from text_corpus import digest, encoded


class ReviewedHyphenResolutionTests(unittest.TestCase):
    def fixture(self, original='PTV- VISSIM'):
        changed = original.replace('PTV- V', 'PTV-V')
        block = {'block_id': 'b1', 'kind': 'prose', 'text': original,
                 'source_pages': [1], 'source_line_ids': ['p1-left', 'p1-right'],
                 'issues': ['hyphen_join_review']}
        doc = {'paper_id': 'p', 'source_sha256': 'source', 'raw_pages_sha256': 'raw',
               'blocks': [block], 'defects': [
                   {'code': 'hyphen_join_review', 'block_id': 'b1', 'page': 1},
                   {'code': 'cross_engine_review', 'page': 1}]}
        literal = {'operation': 'literal_replace', 'block_id': 'b1', 'old': 'PTV- V',
                   'new': 'PTV-V', 'count': 1, 'reason': 'Printed compound checked',
                   'before_text_sha256': digest(original.encode()),
                   'after_text_sha256': digest(changed.encode())}
        resolution = {'operation': 'resolve_hyphen_join_review', 'block_id': 'b1',
                      'reason': 'All printed wrap fragments in this paragraph checked',
                      'before_text_sha256': digest(changed.encode()),
                      'after_text_sha256': digest(changed.encode()),
                      'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
                      'transcription_operations_sha256': digest(encoded([literal]))}
        review = {'paper_id': 'p', 'source_sha256': 'source', 'raw_pages_sha256': 'raw',
                  'reviewer': 'source reviewer', 'reason': 'Individually checked source',
                  'checked_pages': [1], 'operations': [literal, resolution],
                  'evidence': [{'description': 'Bounded page review', 'sha256': 'a' * 64}]}
        return doc, review

    def test_explicit_resolution_preserves_compound_and_other_open_defects(self):
        doc, review = self.fixture()
        apply_text_repairs(doc, [review])
        self.assertEqual(doc['blocks'][0]['text'], 'PTV-VISSIM')
        self.assertEqual(doc['blocks'][0]['issues'], [])
        self.assertEqual(doc['defects'][0]['status'], 'resolved')
        self.assertNotIn('status', doc['defects'][1])
        self.assertEqual(replay_block(doc, doc['blocks'][0], 'PTV- VISSIM'), 'PTV-VISSIM')
        validate_hyphen_resolutions(doc)

    def test_literal_repair_alone_does_not_clear_legacy_flag(self):
        doc, review = self.fixture()
        review['operations'].pop()
        apply_text_repairs(doc, [review])
        self.assertEqual(doc['blocks'][0]['issues'], ['hyphen_join_review'])
        self.assertNotIn('status', doc['defects'][0])

    def test_partial_transcription_cannot_approve_remaining_wrap(self):
        for text in ('PTV- VISSIM and inter- actions', 'PTV- VISSIM rec-'):
            with self.subTest(text=text):
                doc, review = self.fixture(text)
                with self.assertRaisesRegex(ValueError, 'pending wrapped fragment'):
                    apply_text_repairs(doc, [review])

    def test_wrong_lines_chain_missing_transcription_or_extra_operation_reject(self):
        for change in ('lines', 'chain', 'missing', 'extra', 'duplicate-defect'):
            with self.subTest(change=change):
                doc, review = self.fixture()
                if change == 'lines':
                    review['operations'][-1]['source_line_ids_sha256'] = '0' * 64
                elif change == 'chain':
                    review['operations'][-1]['transcription_operations_sha256'] = '0' * 64
                elif change == 'missing':
                    review['operations'].pop(0)
                elif change == 'extra':
                    review['operations'].append(copy.deepcopy(review['operations'][0]))
                else:
                    doc['defects'].append(copy.deepcopy(doc['defects'][0]))
                with self.assertRaises(ValueError):
                    apply_text_repairs(doc, [review])

    def test_later_text_line_or_resolution_metadata_tampering_rejects(self):
        doc, review = self.fixture()
        apply_text_repairs(doc, [review])
        for change in ('text', 'lines', 'flag', 'proof'):
            with self.subTest(change=change):
                altered = copy.deepcopy(doc)
                if change == 'text':
                    altered['blocks'][0]['text'] += ' changed'
                elif change == 'lines':
                    altered['blocks'][0]['source_line_ids'].reverse()
                elif change == 'flag':
                    altered['blocks'][0]['issues'].append('hyphen_join_review')
                else:
                    altered['defects'][0]['text_repair_review_sha256'] = '0' * 64
                with self.assertRaisesRegex(ValueError, 'no longer binds'):
                    validate_hyphen_resolutions(altered)


if __name__ == '__main__':
    unittest.main()
