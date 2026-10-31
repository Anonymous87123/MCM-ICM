"""Source-bound native restoration of q313's complete four-paragraph Summary."""
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
    parent = STORE / 'reflow-20261031-v44'
    directory = STORE / 'reviews/20261031'
    output = directory / 'q313-native-summary-v1'
    if output.exists():
        raise ValueError('Create-only output exists;preserve it')
    evidence_folder = directory / 'q313-opening-pages-v1'
    prepared = read_json(evidence_folder / 'manifest.json')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v44.json')
    old = catalog.document('P-D-2022-2208928-f4cfe761')
    raw = parent / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if (accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']
            or prepared['dataset_id'] != catalog.identity or old['queue_position'] != 313 or old['page_count'] != 22
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw) != old['raw_pages_sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted native source binding required')
    for name, sha in prepared['files'].items():
        if file_hash(evidence_folder / name) != sha:
            raise ValueError('Actually read source evidence changed')
    pages = rows(raw)
    if (len(pages[0]['lines']) != 39 or pages[0].get('ocr_evidence')
            or pages[0]['comparison']['status'] != 'agreement' or pages[0]['comparison']['word_multiset_agreement'] != 1):
        raise ValueError('Expected39complete native lines and independent-engine agreement')
    output.mkdir(parents=True)
    reviewer = 'Codex root;2026-10-31;both complete opening source JPEGs and all39native page1lines actually read'
    findings = {'paper_id': old['paper_id'], 'source_sha256': old['source_sha256'],
        'raw_pages_sha256': old['raw_pages_sha256'], 'reviewer': reviewer,
        'checked_pages': [1, 2], 'logical_author_paragraphs': 4,
        'source_boundary': 'Page1Summaryhas four complete author paragraphs;two-line Keywords form one separate group.Cover form and title separate.Page2Contents,no Summarycontinuation.',
        'preserved_printed_wording': ['DAS Accessment Model', 'Fuzzy Sythetic Evaluation Model', 'Entrophy Weight Method', 'DAS Assessment Model'],
        'only_text_normalization': 'Ordinary alphabetic presentation ligatures expanded through counted,hash-bound literal operations.No author spelling/grammar rewrite,no discretionary wraps found.',
        'formula_verification': 'paused', 'figure_distillation': 'paused',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': reason,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, reason in [
        (evidence_folder / 'manifest.json', evidence_folder, 'Both actually read source JPEGs and all native page1lines.'),
        (output / 'findings.json', None, 'Complete four-paragraph boundary and source-wording adjudication.'),
        (Path(__file__), None, 'Individual native restoration implementation.')]]
    files = {str(p): file_hash(p) for p in evidence_folder.iterdir() if p.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    groups = []
    for name, kind, numbers in [('form', 'front_matter', range(5)), ('title', 'title', [5]),
            ('heading', 'heading', [6]), *[(f'summary{i-6}', 'prose', [i]) for i in range(7, 11)],
            ('keywords', 'keywords', [11])]:
        lines = [line for line in pages[0]['lines'] if line['native_block'] in numbers]
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': [line['line_id'] for line in lines],
            'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
            'reason': 'Actually source-read four-paragraph/native-line ownership.',
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})})
    identity = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer,
        'reason': 'Restore full four-paragraph Summary;retain complete two-line Keywords and separate title/form.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
        'pages': [{'page': 1, 'groups': groups}], 'evidence': evidence, 'evidence_files': files,
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    metrics = STORE / 'span-metrics-20261031-q312-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True); candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    table = dict(zip('ﬀﬁﬂﬃﬄﬅﬆ', ('ff', 'fi', 'fl', 'ffi', 'ffl', 'st', 'st')))
    operations = []
    for block in candidate['blocks']:
        if block.get('layout_group_id') not in {f'summary{i}' for i in range(1, 5)}:
            continue
        text = block['text']
        for before, after in table.items():
            if before not in text:
                continue
            changed = text.replace(before, after)
            operations.append({'block_id': block['block_id'], 'operation': 'literal_replace',
                'old': before, 'new': after, 'count': text.count(before),
                'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Source-read ordinary alphabetic presentation ligature;no author word rewrite.'})
            text = changed
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
    paragraphs = [normalized_lines([line for line in pages[0]['lines'] if line['native_block'] == n])[0].translate(str.maketrans(table)) for n in range(7, 11)]
    if (text != 'Summary\n\n' + '\n\n'.join(paragraphs) or len(ids) != 1
            or len([b for b in selected if b['kind'] != 'heading']) != 4
            or any(word not in text for word in findings['preserved_printed_wording'])
            or any(word in text for word in ['Summary Sheet', 'Keywords:', 'AHP-EWM Method, Vector', 'MCM/ICM'])
            or later(old) != later(candidate)):
        raise ValueError('Complete native equality,source wording or unchanged-later-body guard failed')
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'alphabetic-ligature-repairs.json'},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read page1retains an unresolved flag')
    json_new(output / 'layout.json', layout); json_new(output / 'alphabetic-ligature-repairs.json', repair)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective source-checked native prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n'); json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'characters': len(text),
        'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 4, 'native_page1_lines': 39,
        'source_lines_accounted_once': True, 'raw_pages_unchanged': True,
        'complete_native_prose_equal_after_declared_ligature_expansion': True,
        'later_actual_author_body_unchanged': True, 'ocr_used': False,
        'ligature_operations': len(operations), 'native_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['layout.json', 'alphabetic-ligature-repairs.json', 'source-review.json', 'findings.json', 'summary-preview.md']},
        'stager_sha256': file_hash(Path(__file__)), 'source_stage_only': True,
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True); print(result, flush=True)


if __name__ == '__main__':
    main()
