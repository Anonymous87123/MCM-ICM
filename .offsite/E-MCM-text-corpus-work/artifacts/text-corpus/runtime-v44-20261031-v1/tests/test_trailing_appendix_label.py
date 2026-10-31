import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from text_corpus import digest, make_document, section_text
from test_text_corpus import line


class TrailingAppendixLabelTests(unittest.TestCase):
    def fixture(self):
        meta = {'paper_id': 'synthetic', 'source_sha256': 'a'*64,
                'raw_pages_sha256': 'b'*64, 'page_count': 1}
        lines = [line('Spreadsheet cells retained without interpretation', block=1),
                 line('Appendix A: Source spreadsheet', y=500, block=2, bold=True)]
        pages = [{'page': 1, 'width': 800, 'height': 612, 'lines': lines,
                  'comparison': {'status': 'agreement'}}]
        groups = [{'group_id': name, 'kind': kind, 'source_line_ids': [value['line_id']],
                   'text_sha256': digest(value['text'].encode()), 'reason': 'Synthetic source fixture.'}
                  for name, kind, value in zip(('object', 'label'), ('source_object', 'caption'), lines)]
        groups[0]['opens_section'] = {'role': 'appendix', 'level': 1, 'trailing_label_group_id': 'label'}
        review = {'schema': 'source-text-layout-review-v1', **meta,
                  'reviewer': 'synthetic-test-only', 'reason': 'Retain label after its object.',
                  'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
                  'evidence_files': {'synthetic': 'c'*64}, 'pages': [{'page': 1, 'groups': groups}]}
        return meta, pages, review

    def test_trailing_printed_label_owns_object_without_moving_or_duplicating_its_text(self):
        meta, pages, review = self.fixture()
        original = copy.deepcopy(pages)
        applied = apply_layout_reviews(meta, pages, [review])
        document = make_document(meta, pages, improved=True)
        document['layout_reviews'] = applied
        validate_layout_reviews(document, original)
        appendix = next(s for s in document['sections'] if s['role'] == 'appendix')
        self.assertEqual(appendix['title'], original[0]['lines'][1]['text'])
        self.assertEqual(appendix['boundary_status'], 'pending')
        self.assertEqual(appendix['origin'], 'reviewed-trailing-appendix-label')
        self.assertEqual([b['kind'] for b in document['blocks']], ['source_object', 'caption'])
        self.assertEqual([b['source_line_ids'] for b in document['blocks']],
                         [[x['line_id']] for x in original[0]['lines']])
        self.assertTrue(all(b['section_id'] == appendix['section_id'] for b in document['blocks']))
        self.assertEqual(section_text(document, [appendix['section_id']]), '')
        appendix['source_label_line_ids'] = []
        with self.assertRaisesRegex(ValueError, 'opening ownership'):
            validate_layout_reviews(document, original)

    def test_trailing_label_must_be_same_page_immediately_following_appendix_caption(self):
        for mutation in ('missing', 'wrong-role', 'wrong-kind', 'wrong-title', 'intervening'):
            meta, pages, review = self.fixture()
            groups = review['pages'][0]['groups']
            if mutation == 'missing':
                groups[0]['opens_section']['trailing_label_group_id'] = 'unknown'
            elif mutation == 'wrong-role':
                groups[0]['opens_section']['role'] = 'references'
            elif mutation == 'wrong-kind':
                groups[0]['kind'] = 'prose'
            elif mutation == 'wrong-title':
                pages[0]['lines'][1]['text'] = 'A source explanation, not an appendix label.'
                groups[1]['text_sha256'] = digest(pages[0]['lines'][1]['text'].encode())
            else:
                groups.insert(1, copy.deepcopy(groups[1]))
                groups[1]['group_id'] = 'intervening'
            with self.assertRaisesRegex(ValueError, 'section opening invalid'):
                apply_layout_reviews(meta, pages, [review])


if __name__ == '__main__':
    unittest.main()
