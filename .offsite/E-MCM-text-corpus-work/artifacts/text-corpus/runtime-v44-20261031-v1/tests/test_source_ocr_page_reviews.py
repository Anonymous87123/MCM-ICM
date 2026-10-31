"""OCR acceptance requires final, complete source-page prose and survives no tamper."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews
from source_ocr_page_reviews import CODES, apply_ocr_page_reviews, page_blocks_signature, validate_ocr_page_reviews
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, section_blocks, section_text


class SourceOCRPageReviewsTests(unittest.TestCase):
    def fixture(self, comparison='disagreement', reference=False):
        meta = {'paper_id': 'synthetic-ocr-prose', 'source_sha256': 'a'*64, 'raw_pages_sha256': 'b'*64}
        lines = [{'line_id': name, 'text': text, 'page': 1, 'native_block': -1,
                  'bbox': [72, y, 520, y+12], 'font_size': 12, 'bold': name == 'heading',
                  'engine': 'rapidocr', 'spans': [], 'ocr_score': 0.99}
                 for name, text, y in [('heading', 'Summary', 100),
                     ('author', 'A source-checked complete author paragraph.', 140),
                     ('keywords', 'Keywords: exact source', 180)]]
        pages = [{'page': 1, 'width': 595, 'height': 842, 'lines': lines,
                  'ocr_status': 'candidate', 'ocr_evidence': {'sha256': 'd'*64},
                  'comparison': {'status': comparison}}]
        groups = [{'group_id': line['line_id'], 'kind': kind, 'source_line_ids': [line['line_id']],
                   'text_sha256': digest(line['text'].encode()), 'reason': 'Synthetic source check.'}
                  for line, kind in zip(lines, ('heading', 'prose', 'keywords'))]
        groups[0]['opens_section'] = {'role': 'abstract', 'level': 1}
        if reference:
            line = {'line_id': 'reference', 'text': '[1] Named Author. Cited source.', 'page': 1,
                    'native_block': -1, 'bbox': [72, 220, 520, 232], 'font_size': 12,
                    'bold': False, 'engine': 'rapidocr', 'spans': [], 'ocr_score': .99}
            lines.append(line)
            groups.append({'group_id': 'reference', 'kind': 'source_object', 'source_line_ids': ['reference'],
                           'text_sha256': digest(line['text'].encode()), 'reason': 'Synthetic bibliographic footnote.'})
        layout = {'schema': 'source-text-layout-review-v1', **meta, 'reviewer': 'test-only',
                  'reason': 'Complete synthetic page.', 'paragraph_boundaries_checked': True,
                  'reading_lanes_checked': True, 'evidence_files': {'checked-page.jpg': 'c'*64},
                  'pages': [{'page': 1, 'groups': groups}]}
        working = copy.deepcopy(pages)
        applied = apply_layout_reviews(meta, working, [layout])
        doc = make_document(meta, working, improved=True)
        doc['layout_reviews'] = applied
        if reference:
            block = next(block for block in doc['blocks'] if block.get('layout_group_id') == 'reference')
            apply_text_repairs(doc, [{**meta, 'reviewer': 'test-only', 'checked_pages': [1],
                'reason': 'Separate source-bound bibliographic footnote.',
                'evidence': [{'path': 'checked-page.jpg', 'sha256': 'c'*64, 'description': 'Synthetic source binding.'}],
                'operations': [{'block_id': block['block_id'], 'operation': 'classify',
                    'from_kind': 'source_object', 'to_kind': 'references',
                    'before_text_sha256': digest(block['text'].encode()), 'after_text_sha256': digest(block['text'].encode()),
                    'reason': 'Retain separately from author prose.'}]}])
        sid = next(section['section_id'] for section in doc['sections'] if section['title'] == 'Summary')
        review = {**meta, 'section_id': sid, 'text_sha256': digest(section_text(doc, [sid]).encode()),
                  'reviewer': 'test-only', 'checked_pages': [1], 'section_boundaries_checked': True,
                  'paragraph_boundaries_checked': True,
                  'paragraph_blocks': [block['block_id'] for block in section_blocks(doc, [sid]) if block['kind'] != 'heading']}
        proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1,
                 'all_page_prose_and_boundaries_actually_read': True,
                 'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'],
                 'raw_page_sha256': digest(encoded(pages[0])),
                 'layout_groups_sha256': digest(encoded(groups)),
                 'final_page_blocks_sha256': digest(encoded(page_blocks_signature(doc, 1))),
                 'reviewed_page_jpeg_sha256': 'c'*64, 'reviewed_page_jpeg_bytes': 1000}
        if reference:
            proof['separate_reference_blocks'] = [{'block_id': block['block_id'],
                'text_sha256': digest(block['text'].encode()),
                'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
                'bibliographic_reference_actually_read': True}]
        review['ocr_prose_page_reviews'] = [proof]
        apply_reviews(doc, [review])
        return doc, pages

    def test_only_explicit_full_page_proof_resolves_ocr_flags(self):
        doc, pages = self.fixture()
        self.assertEqual(sum(item.get('status') != 'resolved' and item['code'] in CODES for item in doc['defects']), 2)
        unrelated = copy.deepcopy([item for item in doc['defects'] if item['code'] not in CODES])
        apply_ocr_page_reviews(doc, pages)
        validate_ocr_page_reviews(doc, pages)
        self.assertTrue(Catalog.review_valid(doc, next(section for section in doc['sections'] if section['title'] == 'Summary')))
        self.assertTrue(all(item.get('status') == 'resolved' for item in doc['defects'] if item['code'] in CODES))
        self.assertEqual([item for item in doc['defects'] if item['code'] not in CODES], unrelated)
        self.assertEqual(pages[0]['comparison']['status'], 'disagreement')
        self.assertEqual(pages[0]['ocr_status'], 'candidate')
        with self.assertRaises(ValueError):
            apply_ocr_page_reviews(doc, pages)

    def test_native_template_agreement_cannot_accept_ocr_replacement(self):
        doc, pages = self.fixture(comparison='agreement')
        self.assertEqual({d['code'] for d in doc['defects'] if d['code'] in CODES and d.get('status') != 'resolved'}, CODES)
        apply_ocr_page_reviews(doc, pages)
        validate_ocr_page_reviews(doc, pages)
        self.assertEqual(pages[0]['comparison']['status'], 'agreement')
        self.assertTrue(all(d.get('status') == 'resolved' for d in doc['defects'] if d['code'] in CODES))

    def test_separately_declared_bibliographic_footnote_is_preserved(self):
        doc, pages = self.fixture(reference=True)
        before = copy.deepcopy(next(block for block in doc['blocks'] if block['kind'] == 'references'))
        apply_ocr_page_reviews(doc, pages)
        validate_ocr_page_reviews(doc, pages)
        self.assertEqual(next(block for block in doc['blocks'] if block['kind'] == 'references'), before)
        section = next(section for section in doc['sections'] if section.get('review'))
        self.assertNotIn('[1] Named Author', section_text(doc, [section['section_id']]))

    def test_reference_missing_stale_or_unbound_declaration_fails(self):
        for change in ('missing', 'duplicate', 'text', 'lines', 'not_read', 'classification', 'identity', 'kind', 'undeclared'):
            with self.subTest(change=change):
                doc, pages = self.fixture(reference=True)
                review = next(section['review'] for section in doc['sections'] if section.get('review'))
                proof = review['ocr_prose_page_reviews'][0]
                declaration = proof['separate_reference_blocks'][0]
                if change == 'missing':
                    proof.pop('separate_reference_blocks')
                elif change == 'duplicate':
                    proof['separate_reference_blocks'].append(copy.deepcopy(declaration))
                elif change == 'text':
                    declaration['text_sha256'] = 'e'*64
                elif change == 'lines':
                    declaration['source_line_ids_sha256'] = 'e'*64
                elif change == 'not_read':
                    declaration['bibliographic_reference_actually_read'] = False
                elif change == 'classification':
                    doc['text_repair_reviews'] = []
                elif change == 'identity':
                    doc['text_repair_reviews'][0]['raw_pages_sha256'] = 'e'*64
                elif change == 'kind':
                    next(block for block in doc['blocks'] if block['kind'] == 'references')['kind'] = 'mixed'
                else:
                    declaration['block_id'] = 'unknown'
                with self.assertRaises(ValueError):
                    apply_ocr_page_reviews(doc, pages)

    def test_unreviewed_ocr_also_requires_new_comparison(self):
        _, pages = self.fixture(comparison='agreement')
        meta = {'paper_id': 'synthetic-ocr-prose', 'source_sha256': 'a'*64, 'raw_pages_sha256': 'b'*64}
        doc = make_document(meta, copy.deepcopy(pages), improved=True)
        self.assertTrue(CODES.issubset({d['code'] for d in doc['defects'] if d.get('status') != 'resolved'}))
        native = copy.deepcopy(pages)
        native[0]['ocr_status'] = 'not-run'
        native[0].pop('ocr_evidence')
        doc = make_document(meta, native, improved=True)
        self.assertNotIn('cross_engine_review', {d['code'] for d in doc['defects']})

    def test_raw_text_lane_image_or_object_tamper_fails_closed(self):
        original, pages = self.fixture()
        apply_ocr_page_reviews(original, pages)
        for target in ('raw', 'text', 'lane', 'image', 'object', 'orphan'):
            with self.subTest(target=target):
                doc, raw = copy.deepcopy(original), copy.deepcopy(pages)
                if target == 'raw':
                    raw[0]['lines'][1]['text'] += ' altered'
                elif target == 'text':
                    next(block for block in doc['blocks'] if block['kind'] == 'prose')['text'] += ' altered'
                elif target == 'lane':
                    doc['layout_reviews'][0]['pages'][0]['groups'][1]['source_line_ids'] = ['keywords']
                elif target == 'image':
                    doc['layout_reviews'][0]['evidence_files']['checked-page.jpg'] = 'e'*64
                elif target == 'object':
                    next(block for block in doc['blocks'] if block['kind'] == 'prose')['kind'] = 'mixed'
                else:
                    next(section for section in doc['sections'] if section.get('review'))['review'].pop('ocr_prose_page_reviews')
                with self.assertRaises(ValueError):
                    validate_ocr_page_reviews(doc, raw)

    def test_portable_bundle_must_explicitly_include_the_inspected_page_image(self):
        original, pages = self.fixture()
        meta = {key: original[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            provenance, jpeg = folder / 'provenance.txt', folder / 'checked-page.jpg'
            provenance.write_bytes(b'synthetic source record')
            jpeg.write_bytes(b'synthetic JPEG binding only; no actual source review')
            for include_image in (False, True):
                with self.subTest(include_image=include_image):
                    layout = copy.deepcopy(original['layout_reviews'][0])
                    layout['evidence_files'][str(jpeg)] = file_hash(jpeg)
                    layout['evidence'] = [{'path': str(provenance), 'sha256': file_hash(provenance),
                                           'description': 'Synthetic provenance.'}]
                    if include_image:
                        layout['evidence'].append({'path': str(jpeg), 'sha256': file_hash(jpeg),
                                                   'description': 'Synthetic image declaration.'})
                    path = folder / f'layout-{include_image}.json'
                    json_new(path, layout)
                    bundled, _ = prepare_review_bundles([path], identity_fields=('paper_id',), application_status='test-only')
                    working = copy.deepcopy(pages)
                    applied = apply_layout_reviews(meta, working, bundled)
                    doc = make_document(meta, working, improved=True)
                    doc['layout_reviews'] = applied
                    review = copy.deepcopy(next(section['review'] for section in original['sections'] if section.get('review')))
                    review['ocr_prose_page_reviews'][0]['reviewed_page_jpeg_sha256'] = file_hash(jpeg)
                    review['ocr_prose_page_reviews'][0]['reviewed_page_jpeg_bytes'] = jpeg.stat().st_size
                    apply_reviews(doc, [review])
                    if include_image:
                        apply_ocr_page_reviews(doc, pages)
                        validate_ocr_page_reviews(doc, pages)
                    else:
                        with self.assertRaisesRegex(ValueError, 'image, final text or source-lane'):
                            apply_ocr_page_reviews(doc, pages)


if __name__ == '__main__':
    unittest.main()
