"""Restore q322's source-read three-paragraph Summary without rewriting prose."""
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
    parent = STORE / 'reflow-20261031-v46'
    directory = STORE / 'reviews/20261031'
    output = directory / 'q322-native-summary-v1'
    if output.exists():
        raise ValueError('Create-only stage exists;preserve it')
    folder = directory / 'q322-opening-pages-v1'
    prepared = read_json(folder / 'manifest.json')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v46.json')
    old = catalog.document('P-D-2024-2419588-1cc62ede')
    raw = parent / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if (accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']
            or prepared['dataset_id'] != catalog.identity or old['queue_position'] != 322 or old['page_count'] != 27
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw) != old['raw_pages_sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted native source binding required')
    for name, sha in prepared['files'].items():
        if file_hash(folder / name) != sha:
            raise ValueError('Actually read source evidence changed')
    pages = rows(raw)
    if (len(pages) != 27 or len(pages[0]['lines']) != 49 or pages[0].get('ocr_evidence')
            or pages[0]['comparison']['status'] != 'agreement'
            or pages[0]['comparison']['word_multiset_agreement'] != 0.98524):
        raise ValueError('Expected27physical pages/49complete native opening lines and engine agreement')
    output.mkdir(parents=True)
    reviewer = 'Codex root;2026-10-31;both complete opening JPEGs and all49native page1lines actually read'
    findings = {'paper_id': old['paper_id'], 'source_sha256': old['source_sha256'],
        'raw_pages_sha256': old['raw_pages_sha256'], 'reviewer': reviewer, 'checked_pages': [1, 2],
        'logical_author_paragraphs': 3,
        'source_boundary': 'Page1has three complete author paragraphs:two-model opening,control/2017assessment/stakeholder functions,then explicit limitations and future work.Two-line title and full three-line Keywords separate.Chinese watermark/QRfurniture retained separately.Page2Content,no continuation.27physical pages.Coverprints C but parent-directory typeD is unchanged.',
        'preserved_printed_wording': ['21%', 'Equilibrium Stakeholder Satisfaction (ESS) Model', 'Model Predictive Control (MPC)',
            'the need for improved adaptation to extreme weather events', 'hydro-power',
            'the need for empirical validation of stakeholder satisfaction functions', 'Future work should focus'],
        'only_text_normalization': 'Nine individually source-read author wraps:Stakeholder,preferences,Predictive,environmentalists,companies,promise,social,simplification,capture.Plus one Keyword wrap Sensitivity.Genuine hydro-power retained.All limitations and need for empirical validation preserved.No author rewriting;no OCR.',
        'formula_verification': 'paused', 'figure_distillation': 'paused',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': reason,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, reason in [
        (folder / 'manifest.json', folder, 'Both actually read source JPEGs and all49native opening lines.'),
        (output / 'findings.json', None, 'Three complete paragraphs with explicit limitations/future work;full Keywords and unchanged source wording.'),
        (Path(__file__), None, 'Individual native source-layout restoration implementation.')]]
    files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    def active(numbers):
        return [line for line in pages[0]['lines'] if line['native_block'] in numbers and line['text'].strip()]
    paragraph_lines = [active([number]) for number in range(7, 10)]
    comparison_path = parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin'
    comparison = comparison_path.read_bytes().decode('utf-8', 'strict').split(chr(12))[0]
    independent_lines = [line.strip() for line in comparison.splitlines() if line.strip()]
    independent_position = 0
    prose_lines = [line for paragraph in paragraph_lines for line in paragraph]
    if len(prose_lines) != 21:
        raise ValueError('Expected all21source-read author-prose lines')
    for line in prose_lines:
        independent_position = independent_lines.index(line['text'].strip(), independent_position) + 1
    files[str(comparison_path)] = file_hash(comparison_path)
    specs = [('advertising', 'furniture', active([0, 1, 19, 20, 21, 22])),
        ('form', 'front_matter', active(range(14, 19))), ('title', 'title', active([4, 5])),
        ('heading', 'heading', active([6])),
        *[(f'summary{i+1}', 'prose', lines) for i, lines in enumerate(paragraph_lines)],
        ('keywords', 'keywords', active([10]))]
    groups = []
    for name, kind, lines in specs:
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': [line['line_id'] for line in lines],
            'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
            'reason': 'Complete source-read three-paragraph/Keyword/furniture line ownership.',
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})})
    identity = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer,
        'reason': findings['only_text_normalization'], 'paragraph_boundaries_checked': True,
        'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': evidence, 'evidence_files': files, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count',
        'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    replacements = {'summary1': [('Stake- h', 'Stakeh'), ('fer- e', 'fere')],
        'summary2': [('Pre- d', 'Pred'), ('ron- m', 'ronm'), ('com- p', 'comp')],
        'summary3': [('prom- i', 'promi'), ('so- c', 'soc'), ('sim- p', 'simp'), ('cap- t', 'capt')],
        'keywords': [('tiv- i', 'tivi')]}

    operations = []
    for block in candidate['blocks']:
        if block.get('layout_group_id') not in replacements:
            continue
        value = block['text']
        literals = []
        for before, after in replacements[block['layout_group_id']]:
            if value.count(before) != 1:
                raise ValueError('Exact source-read wrap preimage differs')
            changed = value.replace(before, after)
            operation = {'block_id': block['block_id'], 'operation': 'literal_replace',
                'old': before, 'new': after, 'count': 1,
                'before_text_sha256': digest(value.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Individually source-read printed wrap;genuine hyphen retained where present.'}
            operations.append(operation)
            literals.append(operation)
            value = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'before_text_sha256': digest(value.encode()), 'after_text_sha256': digest(value.encode()),
            'transcription_operations_sha256': digest(encoded(literals)),
            'reason': 'All printed line wraps in this source paragraph actually checked.'})
    repair = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2],
        'reason': findings['only_text_normalization'], 'operations': operations, 'evidence': evidence,
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, pages)
    owned = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    owned.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if owned != Counter(line['line_id'] for page in pages for line in page['lines']) or any(n != 1 for n in owned.values()):
        raise ValueError('Every native source line must have exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    text = text_with_block_spans(selected)[0]
    paragraphs = [normalized_lines(lines)[0] for lines in paragraph_lines]
    for group, pairs in replacements.items():
        if group == 'keywords':
            continue
        at = int(group.removeprefix('summary')) - 1
        for before, after in pairs:
            paragraphs[at] = paragraphs[at].replace(before, after)
    if (text != 'Summary\n\n' + '\n\n'.join(paragraphs) or len(ids) != 1
            or len([b for b in selected if b['kind'] != 'heading']) != 3
            or any(word not in text for word in findings['preserved_printed_wording'])
            or any(word in text for word in ['Summary Sheet', 'Keywords:', 'MCM/ICM', 'MATHmodels', '关注数学模型', '获取更多资讯'])
            or later(old) != later(candidate)):
        raise ValueError('Complete native prose equality,source wording or unchanged-later-body guard failed')
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'word-wrap-repairs.json'},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read opening page retains an unresolved flag')
    json_new(output / 'layout.json', layout)
    json_new(output / 'source-review.json', review)
    json_new(output / 'word-wrap-repairs.json', repair)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',),
        application_status='prospective source-checked native prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n')
    json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'characters': len(text),
        'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 3, 'native_page1_lines': 49,
        'source_lines_accounted_once': True, 'raw_pages_unchanged': True,
        'independent_prose_lines_equal_in_order': 21,
        'complete_native_prose_equal_after_declared_source_wraps': True,
        'later_actual_author_body_unchanged': True, 'ocr_used': False,
        'author_wraps_repaired': 9, 'keyword_wraps_repaired': 1, 'genuine_hyphen_line_spaces_closed': 0, 'native_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['layout.json', 'source-review.json', 'findings.json', 'summary-preview.md', 'word-wrap-repairs.json']},
        'stager_sha256': file_hash(Path(__file__)), 'source_stage_only': True,
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
