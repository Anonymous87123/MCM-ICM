"""Exact prose-page acceptance after local OCR AND actual source-page reading.

This never claims agreement between native extraction and OCR. A review binds
one final page transcription, all source lanes and its inspected JPEG. Pages
containing formulas/objects or uncovered author chapters remain pending.
"""
import re

from corpus_reader import Catalog
from source_layout_reviews import validate_layout_reviews
from text_corpus import PROSE_KINDS, digest, encoded, section_blocks


RESOLUTION = 'explicit source-checked OCR prose page; independent agreement not claimed'
CODES = {'cross_engine_review', 'ocr_candidate_source_review'}
ALLOWED_KINDS = {'front_matter', 'furniture', 'title', 'heading', 'prose', 'list', 'author_callout', 'keywords'}


def page_blocks_signature(document, number):
    return [{'block_id': block['block_id'], 'section_id': block['section_id'], 'kind': block['kind'],
             'source_line_ids': block['source_line_ids'], 'text': block['text']}
            for block in document['blocks'] if number in block['source_pages']]


def check_page_proof(document, pages, review, proof):
    number = proof.get('page')
    sections = [section for section in document['sections'] if section['section_id'] == review.get('section_id')]
    if (proof.get('schema') != 'source-checked-ocr-prose-page-v1' or type(number) is not int or
            not 1 <= number <= len(pages) or number not in review.get('checked_pages', []) or
            proof.get('all_page_prose_and_boundaries_actually_read') is not True or
            proof.get('resolved_codes') != sorted(CODES) or len(sections) != 1 or
            not Catalog.review_valid(document, sections[0]) or
            review.get('source_sha256') != document['source_sha256'] or
            review.get('raw_pages_sha256') != document['raw_pages_sha256']):
        raise ValueError('Incomplete or stale source-checked OCR prose-page proof')
    raw = pages[number-1]
    if (raw['page'] != number or raw.get('ocr_status') != 'candidate' or not raw.get('ocr_evidence') or
            not any(line.get('engine') == 'rapidocr' for line in raw['lines']) or
            proof.get('raw_page_sha256') != digest(encoded(raw))):
        raise ValueError('OCR prose-page proof does not bind exact raw page evidence')
    layouts = [(layout, page) for layout in document.get('layout_reviews', [])
               for page in layout['pages'] if page['page'] == number]
    if len(layouts) != 1:
        raise ValueError('OCR prose-page acceptance requires one complete reviewed source layout')
    layout, layout_page = layouts[0]
    validate_layout_reviews(document, pages)
    image_sha = proof.get('reviewed_page_jpeg_sha256', '')
    image_bytes = proof.get('reviewed_page_jpeg_bytes')
    if (not re.fullmatch(r'[0-9a-f]{64}', image_sha) or type(image_bytes) is not int or
            not 1 <= image_bytes <= 450000 or
            not any(path.lower().endswith(('.jpg', '.jpeg')) and sha == image_sha
                    for path, sha in layout['evidence_files'].items()) or
            proof.get('layout_groups_sha256') != digest(encoded(layout_page['groups'])) or
            proof.get('final_page_blocks_sha256') != digest(encoded(page_blocks_signature(document, number)))):
        raise ValueError('OCR prose-page image, final text or source-lane binding changed')
    covered = {block['block_id'] for block in section_blocks(document, [review['section_id']])}
    page_blocks = [block for block in document['blocks'] if number in block['source_pages']]
    if not page_blocks or not any(block['kind'] in {'prose', 'list', 'author_callout'} for block in page_blocks):
        raise ValueError('OCR prose-page proof lacks actual author paragraphs')
    for block in page_blocks:
        if (block['source_pages'] != [number] or block['kind'] not in ALLOWED_KINDS or
                block.get('issues') or (block['kind'] in PROSE_KINDS and block['block_id'] not in covered)):
            raise ValueError('OCR page contains pending, mixed/object or uncovered author material')
    return number


def declared_proofs(document):
    seen = set()
    result = []
    for section in document['sections']:
        review = section.get('review', {})
        for proof in review.get('ocr_prose_page_reviews', []):
            number = proof.get('page')
            if type(number) is not int or number in seen:
                raise ValueError('Duplicate/invalid source-checked OCR prose-page declaration')
            seen.add(number)
            result.append((review, proof))
    return result


def apply_ocr_page_reviews(document, pages):
    pending = []
    for review, proof in declared_proofs(document):
        number = check_page_proof(document, pages, review, proof)
        for code in CODES:
            matches = [item for item in document['defects'] if item['code'] == code and item.get('page') == number]
            if len(matches) != 1 or matches[0].get('status') == 'resolved':
                raise ValueError('OCR prose-page resolution requires exactly one open flag per declared code')
            pending.append((matches[0], review, proof))
    for item, review, proof in pending:
        item.update(status='resolved', resolution=RESOLUTION,
                    source_page_review_sha256=digest(encoded(proof)), section_review_sha256=digest(encoded(review)))
    validate_ocr_page_reviews(document, pages)


def validate_ocr_page_reviews(document, pages):
    expected = {}
    for review, proof in declared_proofs(document):
        number = check_page_proof(document, pages, review, proof)
        for code in CODES:
            expected[(number, code)] = (digest(encoded(proof)), digest(encoded(review)))
    actual = {}
    for item in document['defects']:
        if item.get('resolution') != RESOLUTION:
            continue
        key = (item.get('page'), item['code'])
        if item.get('status') != 'resolved' or key in actual:
            raise ValueError('Invalid/duplicate OCR prose-page resolution')
        actual[key] = (item.get('source_page_review_sha256'), item.get('section_review_sha256'))
    if actual != expected:
        raise ValueError('OCR prose-page resolutions differ from exact source proofs')
