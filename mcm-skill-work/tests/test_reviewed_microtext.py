"""Regression: checked source furniture must survive before layout replay."""
import copy
from collections import Counter
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from corpus_queries import all_author_blocks
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from text_corpus import digest, make_document, text_with_block_spans


class ReviewedMicrotextTests(unittest.TestCase):
    def setUp(self):
        self.meta = {'paper_id': 'synthetic-marginal-grid', 'source_sha256': 'a' * 64,
                     'raw_pages_sha256': 'b' * 64}
        lines = [
            {'line_id': 'summary', 'text': 'Summary', 'page': 1, 'native_block': 0,
             'bbox': [240, 100, 320, 116], 'font_size': 14, 'bold': True},
            {'line_id': 'author', 'text': 'A full author paragraph remains in its original source order.',
             'page': 1, 'native_block': 1, 'bbox': [72, 140, 520, 152], 'font_size': 12, 'bold': False},
            *[{'line_id': f'micro-{n}', 'text': 'm', 'page': 1, 'native_block': 2 + n,
               'bbox': [5, 810 + n * 3, 7, 811.3 + n * 3], 'font_size': 1.3, 'bold': False}
              for n in range(3)]]
        self.pages = [{'page': 1, 'width': 595, 'height': 842, 'lines': lines,
                       'comparison': {'status': 'agreement'}}]
        originals = {line['line_id']: line['text'] for line in lines}
        groups = []
        for name, kind, ids in [('summary', 'heading', ['summary']), ('author', 'prose', ['author']),
                                ('grid', 'furniture', [f'micro-{n}' for n in range(3)])]:
            groups.append({'group_id': name, 'kind': kind, 'source_line_ids': ids,
                'text_sha256': digest(' '.join(originals[lid] for lid in ids).encode()),
                'reason': 'Synthetic checked ownership for the microtext regression.'})
        groups[0]['opens_section'] = {'role': 'abstract', 'level': 1}
        self.review = {'schema': 'source-text-layout-review-v1', **self.meta,
            'reviewer': 'synthetic-test-only', 'reason': 'Tiny margin grid is retained separately.',
            'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
            'evidence_files': {'synthetic-proof.txt': 'c' * 64},
            'pages': [{'page': 1, 'groups': groups}]}

    def test_checked_micro_furniture_retained_once_without_polluting_author_text(self):
        pages = copy.deepcopy(self.pages)
        applied = apply_layout_reviews(self.meta, pages, [self.review])
        document = make_document(self.meta, pages, improved=True)
        document['layout_reviews'] = applied
        validate_layout_reviews(document, self.pages)
        assigned = Counter(lid for block in document['blocks'] for lid in block['source_line_ids'])
        assigned.update(item['line_id'] for item in document['excluded_source_lines'])
        self.assertEqual(assigned, Counter(line['line_id'] for line in self.pages[0]['lines']))
        grid = next(block for block in document['blocks'] if block.get('layout_group_id') == 'grid')
        self.assertEqual((grid['kind'], grid['text']), ('furniture', 'm m m'))
        self.assertEqual(document['excluded_source_lines'], [])
        self.assertEqual(text_with_block_spans(all_author_blocks(document))[0],
            'Summary\n\nA full author paragraph remains in its original source order.')
        self.assertTrue(all(section['boundary_status'] == 'pending' for section in document['sections']))

    def test_unreviewed_grid_keeps_existing_exclusion_and_review_flag(self):
        document = make_document(self.meta, copy.deepcopy(self.pages), improved=True)
        self.assertEqual({item['line_id'] for item in document['excluded_source_lines']},
                         {f'micro-{n}' for n in range(3)})
        self.assertEqual(sum(item['code'] == 'margin_microtext_exclusion_review'
                             for item in document['defects']), 1)
        changed = copy.deepcopy(self.review)
        changed['pages'][0]['groups'][-1]['source_line_ids'].pop()
        with self.assertRaises(ValueError):
            apply_layout_reviews(self.meta, copy.deepcopy(self.pages), [changed])


if __name__ == '__main__':
    unittest.main()
