"""q325 source restoration with explicitly bounded independent-engine watermark inserts."""
from collections import Counter
from difflib import SequenceMatcher
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
from text_corpus import digest, file_hash, json_new, make_document, normalized_lines, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def later(document):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues'])
            for b in all_author_blocks(document) if min(b['source_pages']) > 1]


def main():
    parent = STORE / 'reflow-20261031-v46'
    directory = STORE / 'reviews/20261031'
    output = directory / 'q325-native-summary-v2'
    if output.exists():
        raise ValueError('Create-only stage exists;preserve it')
    folder = directory / 'q325-opening-pages-v1'
    prepared = read_json(folder / 'manifest.json')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v46.json')
    old = catalog.document('P-D-2025-2507692-249f88dd')
    raw = parent / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if (accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']
            or prepared['dataset_id'] != catalog.identity or old['queue_position'] != 325 or old['page_count'] != 25
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw) != old['raw_pages_sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted native source binding required')
    for name, sha in prepared['files'].items():
        if file_hash(folder / name) != sha:
            raise ValueError('Actually read source evidence changed')
    pages = rows(raw)
    if (len(pages) != 25 or len(pages[0]['lines']) != 737 or pages[0].get('ocr_evidence')
            or pages[0]['comparison']['status'] != 'agreement'
            or pages[0]['comparison']['word_multiset_agreement'] != 0.990826):
        raise ValueError('Expected25physical pages/737native opening lines and engine agreement')
    micro = [line for line in pages[0]['lines'] if line['native_block'] < 359]
    if (len(micro) != 687 or any(line['text'] != 'm' or len(line['spans']) != 1
            or line['font_size'] != 1.3789234161376953 or line['bbox'][0] < 5
            or line['bbox'][2] > 75 or line['bbox'][1] < 717 or line['bbox'][3] > 787 for line in micro)):
        raise ValueError('Exact687microtext lines/size/page-margin position required')
    def active(numbers):
        return [line for line in pages[0]['lines'] if line['native_block'] in numbers and line['text'].strip()]
    paragraph_lines = [active([n]) for n in range(369, 375)]
    prose_lines = [line for paragraph in paragraph_lines for line in paragraph]
    comparison_path = parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin'
    comparison = comparison_path.read_bytes().decode('utf-8', 'strict').split(chr(12))[0]
    prose_tokens = ' '.join(line['text'].strip() for line in prose_lines).split()
    comparison_tokens = comparison.split()
    start = comparison_tokens.index(prose_tokens[0])
    # The printed Summary ends before the complete Keyword line.
    end = comparison_tokens.index('Keywords:', start)
    comparison_prose = comparison_tokens[start:end]
    inserts = []
    for tag, a, b, c, d in SequenceMatcher(None, prose_tokens, comparison_prose, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        if tag != 'insert' or a != b:
            raise ValueError('Independent engine cannot delete,replace or reorder any author-prose token')
        inserts.append(comparison_prose[c:d])
    expected_inserts = [['学'], ['数'], ['：'], ['el', 's'], ['号'], ['od'], ['众'], ['Hm'],
        ['公'], ['AT', '信'], ['微', 'M'], ['：'], ['号'], ['信'], ['微']]
    if len(prose_lines) != 33 or inserts != expected_inserts:
        raise ValueError('Only the15actually read interleaved watermark groups are permitted')
    output.mkdir(parents=True)
    reviewer = 'Codex root;2026-10-31;both complete opening JPEGs/all50main native lines and full independent page1text read;687identical margin objects bounded'
    findings = {'paper_id': old['paper_id'], 'source_sha256': old['source_sha256'],
        'raw_pages_sha256': old['raw_pages_sha256'], 'reviewer': reviewer, 'checked_pages': [1, 2],
        'logical_author_paragraphs': 6,
        'source_boundary': 'Six complete paragraphs:motivation,ProblemsI/II/III,safety,and sensitivity/limitations/future work.Two-line title,Summary heading and all five native Keyword fragments(one printed line) separately retained.Page2Contents,no continuation.Form,Chinese watermark and687tiny lower-left m objects retained as furniture.',
        'preserved_printed_wording': ['data-driven', 'user-friendliness', 'short-term', 'real-world',
            'Although construction would cause short-term disruptions', 'Some assumptions deviate from the real-world situation',
            'may compromise the accuracy of analysis results', 'Future research could center on refining these assumptions'],
        'margin_microtext': {'line_count': 687, 'all_text_exactly': 'm', 'font_size': 1.3789234161376953,
            'bbox_union': [min(l['bbox'][0] for l in micro), min(l['bbox'][1] for l in micro),
                max(l['bbox'][2] for l in micro), max(l['bbox'][3] for l in micro)],
            'disposition': 'Preserved once as furniture;excluded only from default author-prose query.'},
        'independent_engine': {'complete_author_tokens_equal_in_order': True, 'author_tokens_deleted_or_replaced': 0,
            'exact_watermark_insert_groups': expected_inserts,
            'failed_v1_preserved': str(directory / 'q325-native-summary-v1'),
            'reason': 'Independent layout interleaves rotated Chinese/MATHmodels watermark pieces;all author tokens match in order,with only these exact source-read extras.'},
        'only_text_normalization': 'Restore six printed paragraph boundaries.No OCR,literal edits or author rewriting.The short-term disruption concession and assumptions/accuracy limitations remain intact.',
        'formula_verification': 'paused', 'figure_distillation': 'paused',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': reason,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, reason in [
        (folder / 'manifest.json', folder, 'Both source-read JPEGs/all main prose and bounded margin objects.'),
        (output / 'findings.json', None, 'Complete paragraphs and exact independent-engine watermark insertions.'),
        (Path(__file__), None, 'Individual source-layout restoration with no prose deletion/replacement.')]]
    files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    files[str(comparison_path)] = file_hash(comparison_path)
    specs = [('advertising', 'furniture', active([359, 360])),
        ('form', 'front_matter', active(range(361, 366))), ('title', 'title', active([366, 367])),
        ('heading', 'heading', active([368])),
        *[(f'summary{i+1}', 'prose', lines) for i, lines in enumerate(paragraph_lines)],
        ('keywords', 'keywords', active([375])), ('margin_microtext', 'furniture', micro)]
    groups = []
    for name, kind, lines in specs:
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': [line['line_id'] for line in lines],
            'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
            'reason': 'Complete source-read paragraphs and once-only line ownership;exact margin objects preserved.',
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
    resolve_exact_comparisons(candidate, pages, comparison_path.read_bytes())
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
    if (text != 'Summary\n\n' + '\n\n'.join(paragraphs) or len(ids) != 1
            or len([b for b in selected if b['kind'] != 'heading']) != 6
            or any(word not in text for word in findings['preserved_printed_wording'])
            or any(word in text for word in ['Summary Sheet', 'Keywords:', 'MCM/ICM', 'MATHmodels', '关注数学模型', '获取更多资讯', 'm m m'])
            or later(old) != later(candidate)):
        raise ValueError('Complete native prose equality,source wording or unchanged-later-body guard failed')
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json'},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read opening page retains an unresolved flag')
    json_new(output / 'layout.json', layout)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',),
        application_status='prospective source-checked native prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n')
    json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'characters': len(text),
        'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 6, 'native_page1_lines': 737,
        'source_lines_accounted_once': True, 'raw_pages_unchanged': True,
        'independent_complete_prose_tokens_equal_in_order': True, 'independent_prose_native_lines': 33,
        'independent_engine_exact_watermark_insert_groups': 15,
        'complete_native_prose_equal_after_declared_source_wraps': True,
        'later_actual_author_body_unchanged': True, 'ocr_used': False,
        'author_wraps_repaired': 0, 'margin_microtext_lines_preserved_as_furniture': 687,
        'native_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['layout.json', 'source-review.json', 'findings.json', 'summary-preview.md']},
        'stager_sha256': file_hash(Path(__file__)), 'source_stage_only': True,
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
