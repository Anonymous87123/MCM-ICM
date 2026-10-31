"""Source-bound q327 six-paragraph Summary restoration; no body/raw changes."""
from collections import Counter
from pathlib import Path
import sys

STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
sys.path.insert(0, str(STORE / 'runtime-v44-20261031-v1/scripts'))
from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, normalized_lines, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def later(document):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues'])
            for b in all_author_blocks(document) if min(b['source_pages']) > 1]


def main():
    parent = STORE / 'reflow-20261031-v47'
    folder = STORE / 'reviews/20261031/q327-opening-pages-v1'
    output = STORE / 'reviews/20261031/q327-native-summary-v1'
    if output.exists():
        raise ValueError('Create-only stage exists;preserve it')
    catalog, prepared = Catalog(parent), read_json(folder / 'manifest.json')
    accepted = read_json(STORE / 'integrity-reflow-20261031-v47.json')
    old = catalog.document('P-D-2025-2519935-f07f7c47')
    raw = parent / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if (accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']
            or prepared['dataset_id'] != catalog.identity or old['queue_position'] != 327 or old['page_count'] != 27
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw) != old['raw_pages_sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted source binding required')
    if any(file_hash(folder / name) != sha for name, sha in prepared['files'].items()):
        raise ValueError('Actually read evidence changed')
    pages = rows(raw)
    if (len(pages) != 27 or len(pages[0]['lines']) != 736 or pages[0].get('ocr_evidence')
            or pages[0]['comparison']['status'] != 'agreement'
            or pages[0]['comparison']['word_multiset_agreement'] != 0.99211):
        raise ValueError('Expected27physical pages/736native opening lines and engine agreement')
    micro = [line for line in pages[0]['lines'] if line['native_block'] >= 17]
    if (len(micro) != 687 or any(line['text'] != 'm' or len(line['spans']) != 1
            or line['font_size'] != 1.3789234161376953 or line['bbox'][0] < 5
            or line['bbox'][2] > 75 or line['bbox'][1] < 767 or line['bbox'][3] > 837 for line in micro)):
        raise ValueError('Exact687margin objects required;all retained as furniture')
    def active(numbers):
        return [line for line in pages[0]['lines'] if line['native_block'] in numbers and line['text'].strip()]
    paragraphs = [active([n]) for n in range(10, 16)]
    prose = [line for paragraph in paragraphs for line in paragraph]
    comparison_path = parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin'
    independent = [s.strip() for s in comparison_path.read_bytes().decode('utf-8', 'strict').split(chr(12))[0].splitlines() if s.strip()]
    position = 0
    if len(prose) != 36:
        raise ValueError('All36source-read prose lines required')
    for line in prose:
        position = independent.index(line['text'].strip(), position) + 1
    output.mkdir(parents=True)
    reviewer = 'Codex root;2026-10-31;both complete source JPEGs/all49main native lines/full independent prose read;all687margin objects exactly bounded'
    identity = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    findings = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2], 'logical_author_paragraphs': 6,
        'source_boundary': 'Opening,data preprocessing,Tasks1/2/3,and closing are six complete printed paragraphs.Two-line title,Summary heading and full Keywords separately owned.Page2Contents,no continuation.27physical pages retained.All687lower-left1.378923416pt m objects and watermarks retained separately,not deleted.',
        'preserved_printed_wording': ['354,420', '9,953', 'Finally, we uniform different road names.',
            'Harbor Tunnel Thurway', 'increases by 14%', 'declines by 25%', 'increases by 18.3%',
            'decreases by 82.9%', 'approximately 65 minutes', 'averaging around 2.31 times'],
        'only_text_normalization': 'Restore six paragraph boundaries and three individually source-read discretionary wraps:place-ment,decom-position,con-firmed.Preserve genuine multi-layer/core-bridge/k-shell/inter-layer compounds and all grammar/result-strength claims verbatim.No OCR,formula correctness or chart interpretation.',
        'margin_microtext': {'line_count': 687, 'all_text_exactly': 'm', 'font_size': 1.3789234161376953,
            'bbox_union': [min(x['bbox'][0] for x in micro), min(x['bbox'][1] for x in micro), max(x['bbox'][2] for x in micro), max(x['bbox'][3] for x in micro)],
            'disposition': 'Preserved once as furniture;excluded only from author prose.'},
        'independent_prose_lines_equal_in_order': 36, 'formula_verification': 'paused',
        'figure_distillation': 'paused', 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': reason,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, reason in [
        (folder / 'manifest.json', folder, 'Both source-read opening JPEGs,all main native prose and exact margin-object guard.'),
        (output / 'findings.json', None, 'Six complete source paragraphs/three discretionary wraps;all687margin objects retained.'),
        (Path(__file__), None, 'Individual source-bound layout and wrap restoration.')]]
    files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    files[str(comparison_path)] = file_hash(comparison_path)
    specs = [('advertising', 'furniture', active([0, 1])), ('form', 'front_matter', active(range(2, 7))),
        ('title', 'title', active([7, 8])), ('heading', 'heading', active([9])),
        *[(f'summary{i+1}', 'prose', lines) for i, lines in enumerate(paragraphs)],
        ('keywords', 'keywords', active([16])), ('margin_microtext', 'furniture', micro)]
    groups = [{'group_id': name, 'kind': kind, 'source_line_ids': [line['line_id'] for line in lines],
        'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
        'reason': 'Source-read complete paragraphs and exactly-once source-line ownership.',
        **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})}
        for name, kind, lines in specs]
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer,
        'reason': findings['only_text_normalization'], 'paragraph_boundaries_checked': True,
        'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}], 'evidence': evidence,
        'evidence_files': files, 'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, comparison_path.read_bytes())
    replacements = {'summary4': [('place- m', 'placem'), ('decom- p', 'decomp')], 'summary6': [('con- f', 'conf')]}
    operations = []
    for block in candidate['blocks']:
        if block.get('layout_group_id') not in replacements:
            continue
        value, literals = block['text'], []
        for before, after in replacements[block['layout_group_id']]:
            if value.count(before) != 1:
                raise ValueError('Exact source wrap preimage differs')
            changed = value.replace(before, after)
            op = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after,
                'count': 1, 'before_text_sha256': digest(value.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Individually source-read discretionary prose wrap;genuine compounds retained.'}
            operations.append(op)
            literals.append(op)
            value = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'before_text_sha256': digest(value.encode()), 'after_text_sha256': digest(value.encode()),
            'transcription_operations_sha256': digest(encoded(literals)), 'reason': 'Every printed wrap in this paragraph individually checked.'})
    repair = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2], 'reason': findings['only_text_normalization'],
        'operations': operations, 'evidence': evidence, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, pages)
    owned = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    owned.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if owned != Counter(line['line_id'] for page in pages for line in page['lines']) or any(n != 1 for n in owned.values()):
        raise ValueError('Every native line must have exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    text = text_with_block_spans(selected)[0]
    expected = [normalized_lines(lines)[0] for lines in paragraphs]
    for name, pairs in replacements.items():
        at = int(name.removeprefix('summary')) - 1
        for before, after in pairs:
            expected[at] = expected[at].replace(before, after)
    if (text != 'Summary\n\n' + '\n\n'.join(expected) or len(ids) != 1
            or len([b for b in selected if b['kind'] != 'heading']) != 6
            or any(word not in text for word in findings['preserved_printed_wording'])
            or any(word in text for word in ['Summary Sheet', 'Keywords:', 'MCM/ICM', 'MATHmodels', 'm m m'])
            or later(old) != later(candidate)):
        raise ValueError('Complete prose/source wording/unchanged-later-body guard failed')
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'word-wrap-repairs.json'},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Opening page retains unresolved flags')
    for name, data in [('layout.json', layout), ('source-review.json', review), ('word-wrap-repairs.json', repair)]:
        json_new(output / name, data)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='Prospective source-checked Summary only;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n')
    json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'characters': len(text), 'text_sha256': digest(text.encode()),
        'logical_author_paragraphs': 6, 'native_page1_lines': 736, 'source_lines_accounted_once': True,
        'raw_pages_unchanged': True, 'independent_prose_lines_equal_in_order': 36,
        'complete_native_prose_equal_after_declared_source_wraps': True, 'later_actual_author_body_unchanged': True,
        'ocr_used': False, 'author_wraps_repaired': 3, 'margin_microtext_lines_preserved_as_furniture': 687,
        'native_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['layout.json', 'source-review.json', 'findings.json', 'summary-preview.md', 'word-wrap-repairs.json']},
        'stager_sha256': file_hash(Path(__file__)), 'source_stage_only': True,
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
