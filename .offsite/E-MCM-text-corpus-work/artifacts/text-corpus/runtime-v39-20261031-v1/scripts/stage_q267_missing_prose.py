"""Stage one source-checked missing OCR line and six complete Summary paragraphs.

No accepted generation, old OCR file, span-metric binding or receipt is mutated.
OCR/cross-engine page flags stay pending until a separate source-page review.
"""
import copy
import json
from collections import Counter
from pathlib import Path

from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261031-v30'
    out = base / 'reviews/20261031/q267-ocr-line-restoration-v1'
    if out.exists():
        raise ValueError('Create-only restoration exists; preserve it')
    catalog = Catalog(root)
    old = catalog.document('P-C-2025-2516178-573cdff6')
    if old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Existing source proofs need explicit replay')
    old_raw = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    pages = rows(old_raw)
    if file_hash(old_raw) != old['raw_pages_sha256']:
        raise ValueError('Accepted raw page binding changed')
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    original = base / 'ocr-2516178-page1-20261029-v1'
    manifest_path = original / 'manifest.json'
    manifest = read_json(manifest_path)
    page_path = original / 'page-0001.json'
    page = read_json(page_path)
    crop_path = base / 'reviews/20261031/q267-missing-line-ocr-crop-v2/result.json'
    crop = read_json(crop_path)
    expected = 'the last-block cross-validation approach, a type of time-series cross-validation.'
    if (file_hash(source) != old['source_sha256'] or manifest['source_sha256'] != old['source_sha256'] or
            file_hash(page_path) != manifest['pages'][0]['sha256'] or len(page['lines']) != 46 or
            crop['source_sha256'] != old['source_sha256'] or crop['raw_pages_sha256'] != old['raw_pages_sha256'] or
            crop['model_sha256'] != manifest['model_sha256'] or len(crop['lines']) != 1 or
            crop['lines'][0]['text'] != expected or crop['lines'][0]['score'] != 0.99303 or
            crop['pdf_clip'] != [70, 312, 525, 328] or crop['detection_enabled'] is not False or
            not page['lines'][18]['text'].endswith('we employed') or
            not page['lines'][19]['text'].startswith('Second, an evaluation')):
        raise ValueError('Exact inspected source/OCR insertion preimage differs')
    directory = base / 'reviews/20261031'
    evidence = directory / 'q267-opening-pages-v1'
    evidence_manifest = read_json(evidence / 'manifest.json')
    for name, sha in evidence_manifest['files'].items():
        if file_hash(evidence / name) != sha:
            raise ValueError('Actually inspected source evidence changed')
    proxy = directory / 'q267-first-task-crop-v2.jpg'
    if proxy.stat().st_size != 49246:
        raise ValueError('Actually inspected focused proxy differs')
    findings = {'schema': 'source-prose-layout-findings-v2', 'paper_id': old['paper_id'],
        'source_sha256': old['source_sha256'], 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'reviewer': 'Codex root;2026-10-31;both complete opening JPEGs,focused first-task crop and all46original OCR lines actually read',
        'checked_pages': [1, 2], 'source_boundary': 'Summary ends on page1 before Keywords; page2 is Contents, not Summary continuation.',
        'author_paragraphs': ['opening', 'First', 'Second', 'Third', 'Finally', 'In addition'],
        'missing_line': expected, 'insert_after_original_ocr_index': 18,
        'misclassified_prose_original_ocr_indices': [29, 37],
        'exact_quote_restoration': 'The printed great coach closing quote is U+201D; original OCR used a straight double quote.',
        'preserved_author_claims': ['2021 and2024 wording', 'classification95% versus overall68%',
            'sample coverage>0.95 versus values inside interval>70%', 'DID p-values0.03and0.05; no formula correctness review'],
        'evidence': [{'path': str(path), 'sha256': file_hash(path), 'bytes': path.stat().st_size}
            for path in (evidence / 'page-0001.jpg', evidence / 'page-0002.jpg', proxy, crop_path)],
        'rejected_diagnostic_preserved': str(directory / 'q267-missing-line-ocr-crop-v1/result.json'),
        'whole_paper_source_acceptance': False, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    inserted = {'text': expected, 'score': crop['lines'][0]['score'],
        'pdf_box': [[70, 312], [525, 312], [525, 328], [70, 328]],
        'geometry_origin': 'Manually checked PDF crop; single-line recognition without text detection.',
        'source_recovery_result_sha256': file_hash(crop_path)}
    revised = copy.deepcopy(page)
    revised['lines'].insert(19, inserted)
    revised['source_recovery'] = {'original_page_sha256': file_hash(page_path),
        'original_manifest_sha256': file_hash(manifest_path), 'crop_result_sha256': file_hash(crop_path),
        'only_change': 'One source-checked OCR line inserted at index19; all46original line objects unchanged.',
        'whole_page_review_status': 'source layout checked; page acceptance pending'}
    if revised['lines'][:19] + revised['lines'][20:] != page['lines']:
        raise ValueError('Existing OCR lines changed')
    # Only generated evidence is written; all source and old derived files stay intact.
    out.mkdir(parents=True)
    json_new(out / 'findings.json', findings)
    json_new(out / 'page-0001.json', revised)
    revised_manifest = {**manifest, 'pages': [{'page': 1, 'path': 'page-0001.json',
        'sha256': file_hash(out / 'page-0001.json'), 'line_count': 47, 'low_confidence_lines': 0}],
        'source_recovery': revised['source_recovery'], 'findings_sha256': file_hash(out / 'findings.json')}
    json_new(out / 'manifest.json', revised_manifest)
    revised_pages = copy.deepcopy(pages)
    first = revised_pages[0]
    first['lines'] = [line for line in first['lines'] if line.get('engine') != 'rapidocr']
    for number, value in enumerate(revised['lines']):
        points = value['pdf_box']
        box = [min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)]
        first['lines'].append({'line_id': f'p0001-ocr-l{number:04d}', 'native_block': -1,
            'page': 1, 'bbox': box, 'text': value['text'], 'font_size': max(5, (box[3]-box[1])*.95),
            'bold': value['text'].strip().lower() in {'summary', 'abstract', 'introduction', 'contents'},
            'spans': [], 'ocr_score': value['score'], 'engine': 'rapidocr'})
    first['ocr_evidence']['sha256'] = file_hash(out / 'page-0001.json')
    raw = b''.join((json.dumps(p, ensure_ascii=True, sort_keys=True)+'\n').encode() for p in revised_pages)
    write_new(out / 'prospective-pages.jsonl', raw)
    working, flow = prepare_flow_pages(old, pages, base / 'span-metrics-20261030-v1')
    working[0] = copy.deepcopy(first)
    meta = {key: old[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
        'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    meta['raw_pages_sha256'] = digest(raw)
    proof_evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': description}
        for path, description in ((out / 'findings.json', 'Actually inspected source-page prose/boundary findings.'),
            (crop_path, 'Exact locally recognized missing line; manually matched to original PDF crop.'),
            (out / 'manifest.json', 'New create-only page1 OCR evidence; all original46line objects preserved.'))]
    specs = [('form', 'front_matter', range(0, 7)), ('paper-title', 'title', [7]),
        ('summary-title', 'heading', [8]), ('summary-1', 'prose', range(9, 12)),
        ('summary-2', 'prose', range(12, 20)), ('summary-3', 'prose', range(20, 31)),
        ('summary-4', 'prose', range(31, 38)), ('summary-5', 'prose', range(38, 43)),
        ('summary-6', 'prose', range(43, 46)), ('keywords', 'keywords', [46])]
    by_id = {line['line_id']: line for line in first['lines']}
    groups = []
    reason = 'Six complete source-checked author paragraphs; restore missing validation line and two false-title prose fragments; separate form,title and keywords.'
    for name, kind, numbers in specs:
        ids = [f'p0001-ocr-l{number:04d}' for number in numbers]
        groups.append({'group_id': 'p1-' + name, 'kind': kind, 'source_line_ids': ids,
            'text_sha256': digest(' '.join(by_id[lid]['text'].strip() for lid in ids).encode()), 'reason': reason,
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'summary-title' else {})})
    evidence_files = {str(path): file_hash(path) for path in evidence.iterdir() if path.is_file()}
    evidence_files.update({str(path): file_hash(path) for path in
        (proxy, crop_path, crop_path.parent / 'missing-line-crop.png', out / 'findings.json', out / 'manifest.json', out / 'page-0001.json')})
    layout = {'schema': 'source-text-layout-review-v1', **{key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')},
        'reviewer': findings['reviewer'], 'reason': reason, 'paragraph_boundaries_checked': True,
        'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': proof_evidence, 'evidence_files': evidence_files, 'source_fidelity_approved': False,
        'remaining_uncertainties': ['OCR/cross-engine page flags require separate exact page-proof acceptance.', 'All later author chapters pending.'],
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, revised_pages, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    indexed = {block.get('layout_group_id'): block for block in candidate['blocks'] if block.get('layout_group_id')}
    replacements = {'p1-summary-2': [('pre- ', 'pre'), ('ici- ', 'ici')],
        'p1-summary-3': [('ver- ', 'ver')], 'p1-summary-4': [('differ- ', 'differ'), ('coach"', 'coach”')],
        'p1-summary-5': [('cipa- ', 'cipa'), ('ad- ', 'ad')]}
    ops = []
    for gid, changes in replacements.items():
        block = indexed[gid]
        text = block['text']
        chain = []
        for before, after in changes:
            if text.count(before) != 1:
                raise ValueError('Exact source wrap/quote preimage changed')
            changed = text.replace(before, after)
            op = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after, 'count': 1,
                'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Exact printed discretionary wrap or closing quote; genuine compounds and author wording preserved.'}
            ops.append(op); chain.append(op); text = changed
        ops.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'transcription_operations_sha256': digest(encoded(chain)),
            'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(text.encode()),
            'reason': 'All discretionary wraps in this complete source-checked paragraph restored.'})
    repair = {**{key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')},
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2], 'reason': reason,
        'operations': ops, 'evidence': proof_evidence, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, revised_pages)
    actual = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    actual.update(line['line_id'] for line in candidate['excluded_source_lines'])
    expected_ids = Counter(line['line_id'] for page in revised_pages for line in page['lines'])
    if actual != expected_ids or any(value != 1 for value in actual.values()):
        raise ValueError('Prospective source line ownership lost/duplicated')
    later = lambda doc: [(block['source_line_ids'], block['text'], block['kind'], block['issues'])
        for block in all_author_blocks(doc) if min(block['source_pages']) > 1]
    if later(old) != later(candidate):
        raise ValueError('Later author prose changed')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text = text_with_block_spans(selected)[0]
    if (len(ids) != 1 or sum(block['kind'] != 'heading' for block in selected) != 6 or
            text.count(crop['lines'][0]['text']) != 1 or not text.endswith('robustness in handling diverse scenarios.') or
            'contribution of different events to each country\'s medal-winning.' not in text or
            'Finally, the SHAP Summary Plot was utilized to analyze the mechanism through which' not in text):
        raise ValueError('Complete source Summary guard differs')
    review = {**{key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')},
        'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True,
        'paragraph_blocks': [block['block_id'] for block in section_blocks(candidate, ids) if block['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'literal_repairs': 'word-repairs.json', 'findings': 'findings.json'},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    for name, value in (('layout.json', layout), ('word-repairs.json', repair), ('source-review.json', review)):
        json_new(out / name, value)
    write_new(out / 'summary-preview.md', text + '\n')
    result = {'paper_id': old['paper_id'], 'parent_dataset_id': catalog.identity,
        'parent_raw_pages_sha256': old['raw_pages_sha256'], 'prospective_raw_pages_sha256': digest(raw),
        'original_ocr_lines_preserved': 46, 'inserted_source_ocr_lines': 1,
        'characters': len(text), 'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 6,
        'source_lines_accounted_once': True, 'later_author_text_unchanged': True,
        'paragraph_boundary_review': 'passed', 'source_page_flags_pending':
            [item for item in candidate['defects'] if item.get('page') == 1 and item.get('status') != 'resolved'],
        'span_metric_binding_transfer_still_required': True,
        'span_metrics_source_manifest_sha256': file_hash(base / 'span-metrics-20261030-v1/manifest.json'),
        'proof_sha256': {name: file_hash(out / name) for name in
            ('manifest.json', 'page-0001.json', 'layout.json', 'word-repairs.json', 'source-review.json', 'summary-preview.md')},
        'stager_sha256': file_hash(Path(__file__)), 'source_completeness_accepted': False,
        'whole_paper_source_acceptance': False, 'ai_reading_receipts_created': 0}
    json_new(out / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
