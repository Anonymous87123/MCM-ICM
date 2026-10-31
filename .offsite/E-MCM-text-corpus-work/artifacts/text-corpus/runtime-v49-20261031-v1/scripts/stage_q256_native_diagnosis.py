"""Record a source-bound abstract omission without guessing its repaired layout."""
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import file_hash, json_new, rows


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    output = base / 'reviews/20261031/q256-native-boundary-diagnosis-v1.json'
    if output.exists():
        raise ValueError('Create-only diagnosis exists; preserve it')
    catalog = Catalog(base / 'reflow-20261031-v28')
    pid = 'P-C-2025-2501869-dbf7e00e'
    doc = catalog.document(pid)
    selected = next(item for item in catalog.select('abstract') if item['paper_id'] == pid)
    text, _ = catalog.text_and_spans(selected)
    blocks = {block['block_id']: block for block in doc['blocks']}
    false = blocks['b000017']
    section = next(section for section in doc['sections'] if section['section_id'] == false['section_id'])
    if (len(text) != 2483 or not text.endswith('United States, the') or false['kind'] != 'heading' or
            section['role'] != 'introduction' or false['source_line_ids'] != ['p0001-n0010-l0011'] or
            false['text'] != 'United Kingdom, and France should prioritize the introduction of multinational coaches in'):
        raise ValueError('Exact false heading/omitted tail preimage differs')
    raw = catalog.root / 'papers' / pid / 'raw/pages.jsonl'
    if file_hash(raw) != doc['raw_pages_sha256']:
        raise ValueError('Native binding differs')
    pages = rows(raw)
    native_question2 = [line for line in pages[0]['lines'] if line['native_block'] == 10 and line['text'].strip()]
    native_question3 = [line for line in pages[0]['lines'] if line['native_block'] == 11 and line['text'].strip()]
    if (blocks['b000016']['source_line_ids'] + false['source_line_ids'] + blocks['b000018']['source_line_ids'] !=
            [line['line_id'] for line in native_question2] or
            blocks['b000019']['source_line_ids'] != [line['line_id'] for line in native_question3]):
        raise ValueError('Exact omitted native paragraph ownership differs')
    result = {'schema': 'native-boundary-diagnosis-awaiting-layout-v1',
        **{key: doc[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')},
        'parent_dataset_id': catalog.identity,
        'document_sha256': file_hash(catalog.root / catalog.by_id[pid]['document']),
        'reviewer': 'Codex root;2026-10-31;delivered candidate and omitted readable native prose actually read',
        'delivered_candidate_characters': len(text), 'delivered_candidate_sha256': selected['text_sha256'],
        'false_heading': {'block_id': false['block_id'], 'section_id': section['section_id'],
                         'role': section['role'], 'source_line_ids': false['source_line_ids'], 'text': false['text']},
        'native_question2': native_question2, 'native_question3': native_question3,
        'omitted_readable_blocks_actually_read': [
            {key: blocks[bid][key] for key in ('block_id', 'text', 'source_line_ids', 'source_pages')}
            for bid in ('b000017', 'b000018', 'b000019')],
        'findings': ['A normal coaching sentence contains introduction and is incorrectly promoted to an Introduction heading. The abstract reader therefore omits its continuation and allQuestion3prose, although native source text retains them.',
            'Sourcepage2OCRContents also has false body headings. Individual physicalpages1–3are prepared but NOTvisually inspected in this context.',
            'Sourcepage1contains many m-glyph lines. Their provenance/ownership must be checked visually; do not delete them or infer author text by guess.'],
        'required_next_step': 'After context compaction, inspect the prepared three bounded JPEGs and restore complete page/paragraph/section ownership through a new explicit source-bound layout proof.',
        'section_source_fidelity_approved': False, 'whole_paper_source_acceptance': False,
        'source_mutations': 0, 'ai_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output, result)
    print({'paper_id': pid, 'abstract_tail_omission_confirmed': True,
           'omitted_readable_blocks': 3, 'layout_review_pending': True, 'source_mutations': 0}, flush=True)


if __name__ == '__main__':
    main()
