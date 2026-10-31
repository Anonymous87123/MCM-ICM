"""Individually restore q315's six source-read paragraphs; create-only."""
import copy
import json
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
from source_ocr_page_reviews import apply_ocr_page_reviews, page_blocks_signature, validate_ocr_page_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, normalized_lines, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def later(doc):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(doc) if min(b['source_pages']) > 1]


def main():
    root = STORE / 'reflow-20261031-v44'
    directory = STORE / 'reviews/20261031'
    output = directory / 'q315-summary-restoration-v2'
    if output.exists():
        raise ValueError('Create-only stage exists; preserve it')
    catalog = Catalog(root)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v44.json')
    old = catalog.document('P-D-2022-2218897-ba395a78')
    original = directory / 'q315-summary-ocr-v1'
    evidence_folder = directory / 'q315-opening-pages-v1'
    prepared = read_json(evidence_folder / 'manifest.json')
    original_manifest = read_json(original / 'manifest.json')
    original_page = read_json(original / 'page-0001.json')
    raw_path = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity
            or old['queue_position'] != 315 or old['page_count'] != 23
            or prepared['dataset_id'] != catalog.identity
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or original_manifest['source_sha256'] != old['source_sha256']
            or old['raw_pages_sha256'] != '489524e531d78d7bb86e5dd5e57cb7c29bcf23574f85842ef5bae11772d9bc3d'
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw_path) != old['raw_pages_sha256']
            or len(original_page['lines']) != 49
            or file_hash(original / 'page-0001.json') != '278f5f9ece3598ba59e741d2cdeb883160113b45dc14375253478eaf6440d9ef'
            or file_hash(original / 'page-0001.json') != original_manifest['pages'][0]['sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted source/native/OCR identity required')
    for name, sha in prepared['files'].items():
        if file_hash(evidence_folder / name) != sha:
            raise ValueError('Actually read evidence changed')
    pages = rows(raw_path)
    if len(pages) != 23 or len(pages[0]['lines']) != 49 or pages[0].get('ocr_evidence'):
        raise ValueError('23 physical pages and49 native opening lines required')
    revised = copy.deepcopy(original_page)
    replacements = {
        15: 'In Requirement 1, we first define several sub-indicators respectively for people,',
        19: 'we provide. Then, we utilize mapping function to transform each indicator into a',
        27: 'timization respectively in terms of people, technology, and process. Suggestions are',
        42: 'which can be applied to different companies′ D&A system. Besides, we estimate how',
    }
    corrections = []
    for at, replacement in replacements.items():
        before = revised['lines'][at]['text']
        if (at in (15, 19, 27) and original_page['lines'][at]['score'] >= .65) or (at == 42 and "companies'" not in before):
            raise ValueError('Exact OCR correction preimage differs')
        revised['lines'][at]['text'] = replacement
        corrections.append({'ocr_index': at, 'before': before, 'after': replacement,
            'reason': 'Complete source page and matching native line actually read; preserve original wording/prime glyph.'})
    for at, (before, after) in enumerate(zip(original_page['lines'], revised['lines'])):
        left, right = copy.deepcopy(before), copy.deepcopy(after)
        left.pop('text'); right.pop('text')
        if left != right or (at not in replacements and before != after):
            raise ValueError('All49 boxes/scores and45 other line objects must be unchanged')
    revised['manual_source_transcriptions'] = corrections
    revised['review_status'] = 'Six complete author paragraphs and both opening pages actually read;four source transcriptions,original49 boxes/scores retained.'
    output.mkdir(parents=True)
    reviewer = 'Codex root;2026-10-31;both complete source JPEGs,all49 native lines and49 OCR lines actually read'
    findings = {'paper_id': old['paper_id'], 'source_sha256': old['source_sha256'],
        'parent_raw_pages_sha256': old['raw_pages_sha256'], 'reviewer': reviewer, 'checked_pages': [1, 2],
        'physical_page_count': 23, 'printed_body_last_page': 22,
        'page_count_correction': 'Earlier checkpoint confused printed body page22 with physical page count23;all bindings use23 physical pages.',
        'logical_author_paragraphs': 6,
        'source_boundary': 'Page1 Summary has opening,Requirements1-4,and closing paragraph.No Keywords printed.Form and two-line title separate.Page2 Contents,no Summary continuation.',
        'transcriptions': corrections,
        'source_wraps': ['multi- layer->multi-layer retains genuine compound hyphen', 'op- timization->optimization',
            'pri- marily->primarily', 'dy- namic->dynamic', 'as- pects->aspects'],
        'presentation_only': 'Expand ordinary alphabetic ligatures and restore one source-read space after inline infinity glyph;no formula correctness claim.',
        'preserved_printed_wording': ['International Cargo Movement cooperation', 'costumers', 'Pagerank', 'an one-page', 'companies′'],
        'source_conflict': 'Native/pdftotext mismatch adjudicated against local OCR and source page;three low-score OCR lines completely mistranscribed.',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output / 'findings.json', findings)
    json_new(output / 'page-0001.json', revised)
    manifest = {**original_manifest, 'pages': [{'page': 1, 'path': 'page-0001.json',
        'sha256': file_hash(output / 'page-0001.json'), 'line_count': 49,
        'low_confidence_lines': sum(x['score'] < .95 for x in revised['lines'])}],
        'source_recovery': {'original_manifest_sha256': file_hash(original / 'manifest.json'),
            'original_page_sha256': file_hash(original / 'page-0001.json'), 'findings_sha256': file_hash(output / 'findings.json'),
            'only_changes': 'Four source-read line transcriptions;all49 boxes/scores and45 other line objects unchanged.Scores are original model scores,not estimates for corrected text.'}}
    json_new(output / 'manifest.json', manifest)
    prospective = copy.deepcopy(pages)
    first = prospective[0]
    for line in first['lines']:
        line['superseded_by_ocr'] = True
    for at, value in enumerate(revised['lines']):
        points = value['pdf_box']
        box = [min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)]
        first['lines'].append({'line_id': f'p0001-ocr-l{at:04d}', 'native_block': -1, 'page': 1, 'bbox': box,
            'text': value['text'], 'font_size': max(5, (box[3]-box[1])*.95),
            'bold': value['text'].strip().lower() == 'summary', 'spans': [], 'ocr_score': value['score'], 'engine': 'rapidocr'})
    first['ocr_status'] = 'candidate'
    first['ocr_evidence'] = {'path': 'raw/ocr/page-0001.json', 'sha256': file_hash(output / 'page-0001.json'),
        'models': manifest['model_sha256'], 'version': manifest['ocr_version']}
    raw = b''.join((json.dumps(page, ensure_ascii=True, sort_keys=True) + '\n').encode() for page in prospective)
    write_new(output / 'prospective-pages.jsonl', raw)
    metrics = STORE / 'span-metrics-20261031-q312-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    working[0] = copy.deepcopy(first)
    meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    meta['raw_pages_sha256'] = digest(raw)
    identity = {k: meta[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    evidence = [{'path': str(p), 'sha256': file_hash(p), 'description': description,
        **({'bundle_root': str(bundle)} if bundle else {})} for p, bundle, description in [
        (evidence_folder / 'manifest.json', evidence_folder, 'Both actually read opening JPEGs and all native lines.'),
        (original / 'manifest.json', original, 'All49 original OCR line objects actually read.'),
        (output / 'findings.json', None, 'Complete six-paragraph source-conflict and boundary adjudication.'),
        (output / 'manifest.json', None, 'Source-transcribed OCR binding.'),
        (output / 'page-0001.json', None, 'Four source transcriptions;all original boxes/scores.'),
        (Path(__file__), None, 'Individual create-only restoration implementation.')]]
    files = {str(p): file_hash(p) for folder in (evidence_folder, original) for p in folder.iterdir() if p.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    groups = []
    for name, kind, indexes in [('form', 'front_matter', range(7)), ('title', 'title', [7, 8]),
            ('heading', 'heading', [9]), ('summary1', 'prose', range(10, 15)),
            ('summary2', 'prose', range(15, 23)), ('summary3', 'prose', range(23, 30)),
            ('summary4', 'prose', range(30, 40)), ('summary5', 'prose', range(40, 46)), ('summary6', 'prose', range(46, 49))]:
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': [f'p0001-ocr-l{i:04d}' for i in indexes],
            'text_sha256': digest(' '.join(revised['lines'][i]['text'].strip() for i in indexes).encode()),
            'reason': 'Actually source-read paragraph/form/title ownership.',
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})})
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer,
        'reason': 'Restore all six complete author paragraphs;separate form/title and preserve original wording.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': evidence, 'evidence_files': files, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True); candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, prospective, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    wraps = {'summary2': ('i- l', 'i-l'), 'summary3': ('op- t', 'opt'),
        'summary4': ('pri- m', 'prim'), 'summary5': ('dy- n', 'dyn'), 'summary6': ('as- p', 'asp')}
    operations = []
    for block in candidate['blocks']:
        if block.get('layout_group_id') not in wraps:
            continue
        before, after = wraps[block['layout_group_id']]
        text = block['text']
        if text.count(before) != 1:
            raise ValueError('Exact source wrap preimage differs')
        changed = text.replace(before, after)
        literal = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after, 'count': 1,
            'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
            'reason': 'Actually read printed line wrap;retain genuine multi-layer hyphen.'}
        operations.extend([literal, {'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'before_text_sha256': digest(changed.encode()), 'after_text_sha256': digest(changed.encode()),
            'transcription_operations_sha256': digest(encoded([literal])), 'reason': 'All source paragraph wraps actually checked.'}])
    repair = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2], 'reason': 'Five source-read wraps only;no author rewrite.',
        'operations': operations, 'evidence': evidence, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair]); validate_layout_reviews(candidate, prospective)
    owned = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    owned.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if owned != Counter(line['line_id'] for page in prospective for line in page['lines']) or any(n != 1 for n in owned.values()):
        raise ValueError('Every native/OCR line must have exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    text = text_with_block_spans(selected)[0]
    table = str.maketrans(dict(zip('ﬀﬁﬂﬃﬄﬅﬆ', ('ff', 'fi', 'fl', 'ffi', 'ffl', 'st', 'st'))))
    paragraphs = [normalized_lines([line for line in pages[0]['lines'] if line['native_block'] == n])[0].translate(table) for n in range(8, 14)]
    for group, (before, after) in wraps.items():
        at = int(group.removeprefix('summary')) - 1
        paragraphs[at] = paragraphs[at].replace(before, after)
    if paragraphs[3].count('M/M∞data') != 1:
        raise ValueError('Exact glyph-adjacent prose preimage differs')
    paragraphs[3] = paragraphs[3].replace('M/M∞data', 'M/M∞ data')
    if (text != 'Summary\n\n' + '\n\n'.join(paragraphs) or len(ids) != 1
            or sum(b['kind'] != 'heading' for b in selected) != 6
            or any(value not in text for value in findings['preserved_printed_wording'])
            or any(value in text for value in ['Summary Sheet', 'Keywords', 'Towards the Evaluation', 'Contents', '2218897'])
            or later(old) != later(candidate)):
        raise ValueError('Complete native equality,source wording,boundary or later-body guard failed')
    proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1,
        'all_page_prose_and_boundaries_actually_read': True, 'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'],
        'raw_page_sha256': digest(encoded(first)), 'layout_groups_sha256': digest(encoded(groups)),
        'final_page_blocks_sha256': digest(encoded(page_blocks_signature(candidate, 1))),
        'reviewed_page_jpeg_sha256': prepared['files']['page-0001.jpg'], 'reviewed_page_jpeg_bytes': 393512}
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'word-wrap-repairs.json'},
        'ocr_prose_page_reviews': [proof], 'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review]); apply_ocr_page_reviews(candidate, prospective)
    validate_ocr_page_reviews(candidate, prospective)
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read opening retains unresolved flags')
    json_new(output / 'layout.json', layout); json_new(output / 'word-wrap-repairs.json', repair)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective checked prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n'); json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'characters': len(text), 'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 6, 'physical_pages': 23,
        'original_ocr_lines': 49, 'unchanged_ocr_line_objects': 45, 'manually_source_transcribed_lines': sorted(replacements),
        'original_boxes_and_scores_unchanged': 49, 'author_wraps_repaired': 5,
        'complete_native_prose_equal_after_declared_ligatures_space_and_wraps': True,
        'source_lines_accounted_once': True, 'later_actual_author_body_unchanged': True,
        'native_metric_binding_transfer_still_required': True, 'new_ocr_override_not_yet_in_any_corpus': True,
        'span_metrics_source_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['manifest.json', 'page-0001.json', 'findings.json', 'layout.json',
            'word-wrap-repairs.json', 'source-review.json', 'summary-preview.md', 'prospective-pages.jsonl']},
        'stager_sha256': file_hash(Path(__file__)), 'library_sha256': file_hash(RUNTIME / 'scripts/text_corpus.py'),
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True); print(result, flush=True)


if __name__ == '__main__':
    main()
