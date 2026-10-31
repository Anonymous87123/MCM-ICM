"""Recover q330's four untitled Summary paragraphs; preserve all native wording."""
from collections import Counter
from pathlib import Path
import sys

STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
sys.path.insert(0, str(STORE / 'runtime-v49-20261031-v1/scripts'))
from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest, file_hash, json_new, make_document, normalized_lines, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def later(doc):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(doc) if min(b['source_pages']) > 1]


def main():
    parent = STORE / 'reflow-20261031-v48'
    folder, output = [STORE / ('reviews/20261031/' + name) for name in ('q330-opening-pages-v1', 'q330-native-summary-v1')]
    if output.exists():
        raise ValueError('Create-only stage exists;preserve it')
    catalog, prepared = Catalog(parent), read_json(folder / 'manifest.json')
    old = catalog.document('P-E-2016-52831-df9e4468')
    accepted = read_json(STORE / 'integrity-reflow-20261031-v48.json')
    raw = parent / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity
            or prepared['dataset_id'] != catalog.identity or old['queue_position'] != 330 or old['page_count'] != 18
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw) != old['raw_pages_sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted native source binding required')
    if any(file_hash(folder / name) != sha for name, sha in prepared['files'].items()):
        raise ValueError('Actually read source evidence changed')
    pages = rows(raw)
    if (len(pages) != 18 or len(pages[0]['lines']) != 49 or pages[0].get('ocr_evidence')
            or pages[0]['comparison']['status'] != 'agreement'
            or pages[0]['comparison']['word_multiset_agreement'] != 1.0):
        raise ValueError('Expected18physical pages/49native opening lines')
    def active(numbers):
        return [x for x in pages[0]['lines'] if x['native_block'] in numbers and x['text'].strip()]
    paragraphs = [active(numbers) for numbers in (range(20, 27), range(27, 33), range(33, 39), range(39, 43))]
    prose = [line for paragraph in paragraphs for line in paragraph]
    comparison_path = parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin'
    independent = [s.strip() for s in comparison_path.read_bytes().decode('utf-8', 'strict').split(chr(12))[0].splitlines() if s.strip()]
    position = 0
    if len(prose) != 23 or len(active(range(18))) != 19:
        raise ValueError('All23author lines and19template lines required')
    for line in prose:
        position = independent.index(' '.join(line['text'].split()), position) + 1
    output.mkdir(parents=True)
    identity = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    reviewer = 'Codex root;2026-10-31;both complete opening JPEGs/all49native lines/complete independent page1prose actually read'
    findings = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2], 'logical_author_paragraphs': 4,
        'source_boundary': 'Four complete untitled Summary paragraphs:quoted motivation/tasks,baseline/refinement,applicability/forecast/climate omission repair,and intervention scenario.Underlined paper title separate;no author Summary heading or Keywords invented.Page2repeats title then Contents,no continuation.All18physical pages retained.',
        'only_text_normalization': 'Join printed wrap lines within the four source paragraphs.No literal edits,grammar rewriting,hyphen changes or whitespace polishing.Native double spaces,citation and opening quotation retained.No OCR/formula/figure assessment.',
        'preserved_printed_wording': ['43.7%', '71.6%', 'Our model did not directly account for climate change',
            'a climate-corrected forecast model', 'resulting in a 3.78% increase in water access.'],
        'independent_prose_lines_equal_in_order_after_comparison_whitespace': 23,
        'formula_verification': 'paused', 'figure_distillation': 'paused', 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': reason,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, reason in [
        (folder / 'manifest.json', folder, 'Both actually read opening JPEGs/all49native lines.'),
        (output / 'findings.json', None, 'Four untitled source paragraphs;baseline/refinement and climate limitation retained.'),
        (Path(__file__), None, 'Individual create-only boundary/layout stager without literal edits.')]]
    files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    files[str(comparison_path)] = file_hash(comparison_path)
    specs = [('form', 'front_matter', active(range(18))), ('title', 'title', active([18])),
        *[(f'summary{i+1}', 'prose', lines) for i, lines in enumerate(paragraphs)]]
    groups = [{'group_id': name, 'kind': kind, 'source_line_ids': [x['line_id'] for x in lines],
        'text_sha256': digest(' '.join(x['text'].strip() for x in lines).encode()),
        'reason': 'Source-read full paragraph/form/title ownership.No invented author heading.'} for name, kind, lines in specs]
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer, 'reason': findings['only_text_normalization'],
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': evidence, 'evidence_files': files, 'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, comparison_path.read_bytes())
    validate_layout_reviews(candidate, pages)
    owned = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    owned.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if owned != Counter(line['line_id'] for page in pages for line in page['lines']) or any(n != 1 for n in owned.values()):
        raise ValueError('Every native line,including blanks,must have exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    text = text_with_block_spans(selected)[0]
    if (text != '\n\n'.join(normalized_lines(lines)[0] for lines in paragraphs) or len(ids) != 1 or len(selected) != 4
            or any(b['kind'] != 'prose' for b in selected)
            or any(word not in text for word in findings['preserved_printed_wording'])
            or any(word in text for word in ['Summary Sheet', 'MCM/ICM', 'Contents', 'Type a summary', 'Tackling Water Scarcity:'])
            or later(old) != later(candidate)):
        raise ValueError('Complete untitled native prose equality/source wording/later-body guard failed')
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json'}, 'section_source_fidelity_approved': True,
        'whole_paper_source_acceptance': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read opening page retains pending flag')
    json_new(output / 'layout.json', layout)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='Prospective source-checked untitled Summary only;not a corpus build')
    write_new(output / 'summary-preview.md', text + '\n')
    json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'characters': len(text), 'text_sha256': digest(text.encode()),
        'logical_author_paragraphs': 4, 'native_page1_lines': 49, 'source_lines_accounted_once': True, 'raw_pages_unchanged': True,
        'independent_prose_lines_equal_in_order_after_comparison_whitespace': 23, 'complete_native_prose_equal_without_literal_edits': True,
        'no_author_heading_invented': True, 'later_actual_author_body_unchanged': True, 'ocr_used': False,
        'native_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['layout.json', 'source-review.json', 'findings.json', 'summary-preview.md']},
        'stager_sha256': file_hash(Path(__file__)), 'source_stage_only': True, 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
