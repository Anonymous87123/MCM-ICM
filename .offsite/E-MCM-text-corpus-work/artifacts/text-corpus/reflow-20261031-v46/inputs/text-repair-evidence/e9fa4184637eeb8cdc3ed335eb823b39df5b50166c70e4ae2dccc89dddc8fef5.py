"""Source-bound native restoration of q317's complete five-paragraph Summary."""
import copy
from collections import Counter
from pathlib import Path
import sys

STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v44-20261031-v1'
sys.path.insert(0, str(RUNTIME / 'scripts'))
from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, normalized_lines, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def later(document):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(document) if min(b['source_pages']) > 1]


def main():
    parent = STORE / 'reflow-20261031-v45'
    directory = STORE / 'reviews/20261031'
    output = directory / 'q317-native-summary-v1'
    if output.exists():
        raise ValueError('Create-only output exists;preserve it')
    evidence_folder = directory / 'q317-opening-pages-v1'
    prepared = read_json(evidence_folder / 'manifest.json')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v45.json')
    old = catalog.document('P-D-2023-2300229-f57e1b5d')
    raw = parent / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if (accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']
            or prepared['dataset_id'] != catalog.identity or old['queue_position'] != 317 or old['page_count'] != 25
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw) != old['raw_pages_sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted native source binding required')
    for name, sha in prepared['files'].items():
        if file_hash(evidence_folder / name) != sha:
            raise ValueError('Actually read source evidence changed')
    pages = rows(raw)
    if (len(pages[0]['lines']) != 45 or pages[0].get('ocr_evidence')
            or pages[0]['comparison']['status'] != 'agreement' or pages[0]['comparison']['word_multiset_agreement'] != 1):
        raise ValueError('Expected45complete native lines and independent-engine agreement')
    output.mkdir(parents=True)
    reviewer = 'Codex root;2026-10-31;both complete opening source JPEGs and all45native page1lines actually read'
    findings = {'paper_id': old['paper_id'], 'source_sha256': old['source_sha256'],
        'raw_pages_sha256': old['raw_pages_sha256'], 'reviewer': reviewer,
        'checked_pages': [1, 2], 'logical_author_paragraphs': 5,
        'source_boundary': 'Page1Summary has five complete author paragraphs:opening,relationship graph,temporal allocation,unexpected-event rerun,and sensitivity.Two-line title,form and one-lineKeywords separate.Page2Contents,no continuation.Two blank native lines separately accounted.',
        'preserved_printed_wording': ['Goal 3 and Goal4', '82%', '78%', '5 goals', '3 goals', 'hyperparameters C and D', 'C and D are 0.041 and 0.028'],
        'only_text_normalization': 'Five source-read discretionary wraps plus four missing printed Latin C/D labels restored.LocalOCR corroborates all prose with coordinates/confidence;native/independent agreement alone missed these labels.Genuine trade-off and COVID-19 retained.No formula correctness or author rewrite.',
        'formula_verification': 'paused', 'figure_distillation': 'paused',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': reason,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, reason in [
        (evidence_folder / 'manifest.json', evidence_folder, 'Both actually read source JPEGs and all45native page1lines.'),
        (output / 'findings.json', None, 'Complete five-paragraph boundary and source-wording adjudication.'),
        (Path(__file__), None, 'Individual native restoration implementation.')]]
    ocr_folder = directory / 'q317-summary-ocr-v1'
    ocr_manifest = read_json(ocr_folder / 'manifest.json')
    ocr_page = read_json(ocr_folder / 'page-0001.json')
    if (ocr_manifest['source_sha256'] != old['source_sha256'] or len(ocr_page['lines']) != 40
            or file_hash(ocr_folder / 'page-0001.json') != '2a52d1f44043e92ed8e8e31309cab1c51b58837286674d11484dab7c6d28ab40'
            or ocr_manifest['pages'][0]['sha256'] != file_hash(ocr_folder / 'page-0001.json')):
        raise ValueError('Exact fully read OCR corroboration required')
    evidence.append({'path': str(ocr_folder / 'manifest.json'), 'bundle_root': str(ocr_folder),
        'sha256': file_hash(ocr_folder / 'manifest.json'),
        'description': 'All40localOCRlines actually read;original coordinates/confidence retained.C/D present in OCR/source but absent in both native engines.'})
    files = {str(p): file_hash(p) for p in evidence_folder.iterdir() if p.is_file()}
    files.update({str(p): file_hash(p) for p in ocr_folder.iterdir() if p.is_file()})
    files.update({item['path']: item['sha256'] for item in evidence})
    groups = []
    for name, kind, numbers in [('form', 'front_matter', range(5)), ('title', 'title', [7, 8]),
            ('heading', 'heading', [9]), ('summary1', 'prose', range(10, 14)),
            ('summary2', 'prose', range(14, 23)), ('summary3', 'prose', range(23, 31)),
            ('summary4', 'prose', range(31, 36)), ('summary5', 'prose', range(36, 39)),
            ('keywords', 'keywords', [39])]:
        lines = [line for line in pages[0]['lines'] if line['native_block'] in numbers and line['text'].strip()]
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': [line['line_id'] for line in lines],
            'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
            'reason': 'Actually source-read five-paragraph/native-line ownership.',
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})})
    identity = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer,
        'reason': 'Restore five complete source-read paragraphs,five wraps and four missing C/D labels;retain Keywords,title and form separately.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
        'pages': [{'page': 1, 'groups': groups}], 'evidence': evidence, 'evidence_files': files,
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True); candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    replacements = {'summary1': [('inde- p', 'indep')], 'summary2': [('Algo- r', 'Algor')],
        'summary3': [('Cham- p', 'Champ'), ('Indo- n', 'Indon')],
        'summary5': [('Cham- p', 'Champ'), ('s and', 's C and'), ('and in', 'and D in'), ('of and', 'of C and'), ('d are', 'd D are')]}
    operations = []
    for block in candidate['blocks']:
        if block.get('layout_group_id') not in replacements:
            continue
        text = block['text']
        literals = []
        for before, after in replacements[block['layout_group_id']]:
            if text.count(before) != 1:
                raise ValueError('Exact source-read wrap preimage differs')
            changed = text.replace(before, after)
            operation = {'block_id': block['block_id'], 'operation': 'literal_replace',
                'old': before, 'new': after, 'count': 1,
                'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Source-read discretionary printed line wrap;no author word rewrite.'}
            operations.append(operation); literals.append(operation)
            text = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(text.encode()),
            'transcription_operations_sha256': digest(encoded(literals)),
            'reason': 'All physical line wraps in this source paragraph actually checked.'})
    repair = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2],
        'reason': findings['only_text_normalization'], 'operations': operations, 'evidence': evidence,
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair]); validate_layout_reviews(candidate, pages)
    owned = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    owned.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if owned != Counter(line['line_id'] for page in pages for line in page['lines']) or any(n != 1 for n in owned.values()):
        raise ValueError('Every native line needs exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    text = text_with_block_spans(selected)[0]
    paragraphs = [normalized_lines([line for line in pages[0]['lines'] if line['native_block'] in numbers])[0]
                  for numbers in (range(10, 14), range(14, 23), range(23, 31), range(31, 36), range(36, 39))]
    for group, pairs in replacements.items():
        at = int(group.removeprefix('summary')) - 1
        for before, after in pairs:
            paragraphs[at] = paragraphs[at].replace(before, after)
    ocr_paragraphs = [' '.join(x['text'].strip() for x in ocr_page['lines'][start:end])
                      for start, end in ((10,14),(14,23),(23,31),(31,36),(36,39))]
    for at, pairs in [(0,[('inde- p','indep')]),(1,[('Algo- r','Algor')]),
                      (2,[('Cham- p','Champ'),('Indo- n','Indon')]),(4,[('Cham- p','Champ')])]:
        for before, after in pairs:
            if ocr_paragraphs[at].count(before) != 1:
                raise ValueError('Original OCR wrap preimage changed')
            ocr_paragraphs[at] = ocr_paragraphs[at].replace(before, after)
    if paragraphs != ocr_paragraphs:
        raise ValueError('Full native-plus-declared-repairs differs from independently read OCR/source prose')
    if (text != 'Summary\n\n' + '\n\n'.join(paragraphs) or len(ids) != 1
            or len([b for b in selected if b['kind'] != 'heading']) != 5
            or any(word not in text for word in findings['preserved_printed_wording'])
            or any(word in text for word in ['Summary Sheet', 'Keywords:', 'Methods of Measuring Priority', 'MCM/ICM'])
            or later(old) != later(candidate)):
        raise ValueError('Complete native equality,source wording or unchanged-later-body guard failed')
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'word-wrap-repairs.json'},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read page1retains an unresolved flag')
    json_new(output / 'layout.json', layout); json_new(output / 'word-wrap-repairs.json', repair)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective source-checked native prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n'); json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'characters': len(text),
        'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 5, 'native_page1_lines': 45,
        'source_lines_accounted_once': True, 'raw_pages_unchanged': True,
        'complete_native_prose_equal_after_declared_source_wraps': True,
        'later_actual_author_body_unchanged': True, 'ocr_used': True, 'ocr_raw_override_used': False, 'ocr_role': 'Source-bound corroboration;all native lines preserved',
        'author_wraps_repaired': 5, 'missing_inline_latin_labels_restored': 4, 'native_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['layout.json', 'word-wrap-repairs.json', 'source-review.json', 'findings.json', 'summary-preview.md']},
        'stager_sha256': file_hash(Path(__file__)), 'source_stage_only': True,
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True); print(result, flush=True)


if __name__ == '__main__':
    main()
