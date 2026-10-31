"""Restore q328's untitled single-paragraph Summary without inventing a heading."""
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
from text_corpus import digest, file_hash, json_new, make_document, normalized_lines, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def later(doc):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(doc) if min(b['source_pages']) > 1]


def main():
    parent = STORE / 'reflow-20261031-v47'
    folder, output = [STORE / ('reviews/20261031/' + name) for name in ('q328-opening-pages-v1', 'q328-native-summary-v1')]
    if output.exists():
        raise ValueError('Preserve existing create-only stage')
    catalog, prepared = Catalog(parent), read_json(folder / 'manifest.json')
    old = catalog.document('P-E-2016-43443-82025ab9')
    accepted = read_json(STORE / 'integrity-reflow-20261031-v47.json')
    raw = parent / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity
            or prepared['dataset_id'] != catalog.identity or old['queue_position'] != 328 or old['page_count'] != 23
            or prepared['source_sha256'] != old['source_sha256'] or file_hash(source) != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or file_hash(raw) != old['raw_pages_sha256']
            or any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews'))):
        raise ValueError('Exact accepted source preimage required')
    if any(file_hash(folder / name) != sha for name, sha in prepared['files'].items()):
        raise ValueError('Source-read evidence changed')
    pages = rows(raw)
    if (len(pages) != 23 or len(pages[0]['lines']) != 59 or pages[0].get('ocr_evidence')
            or pages[0]['comparison']['status'] != 'agreement'
            or pages[0]['comparison']['word_multiset_agreement'] != 0.975446):
        raise ValueError('Expected23physical pages/59native opening lines')
    form = [line for line in pages[0]['lines'] if line['native_block'] < 8 and line['text'].strip()]
    prose = [line for line in pages[0]['lines'] if line['native_block'] == 8 and line['text'].strip()]
    comparison_path = parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin'
    independent = [s.strip() for s in comparison_path.read_bytes().decode('utf-8', 'strict').split(chr(12))[0].splitlines() if s.strip()]
    position, glyphs = 0, Counter()
    if len(form) != 28 or len(prose) != 31:
        raise ValueError('All28template and31author lines required')
    for line in prose:
        value = ' '.join(line['text'].split())
        glyphs.update(c for c in value if c in 'ﬁﬂ')
        position = independent.index(value.replace('ﬁ', 'fi').replace('ﬂ', 'fl'), position) + 1
    if glyphs != Counter({'ﬁ': 4, 'ﬂ': 1}):
        raise ValueError('Exactly five source-read typography ligatures required')
    output.mkdir(parents=True)
    identity = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    reviewer = 'Codex root;2026-10-31;both complete opening JPEGs/all59native lines/complete independent page1prose actually read'
    findings = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2], 'logical_author_paragraphs': 1,
        'source_boundary': 'One continuous untitled author paragraph below28competition-template lines.No Summary/Abstract heading invented.Page2has the separate paper title,date,control number and Contents;no Summary continuation.All23physical pages retained.',
        'only_text_normalization': 'Join31printed wrap lines into the one source paragraph.Expand four fi and one fl typography ligatures,all independently read in printed prose.No words,grammar,internal spaces,years,claims or genuine long-term hyphen rewritten.No OCR.',
        'preserved_printed_wording': ['ecosystem of all available water carries serious environmental consequences',
            'around half of its current level by 2031', 'cumulative impact of the proposed infrastructure improvements to be minimal',
            'from 2083 to 2084', 'pushes the year India hits zero EWR back to 2097', 'large cultural shifts in demand'],
        'independent_prose_lines_equal_in_order_after_ligatures_and_whitespace': 31,
        'formula_verification': 'paused', 'figure_distillation': 'paused', 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': reason,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, reason in [
        (folder / 'manifest.json', folder, 'Both source-read JPEGs/all59native opening lines.'),
        (output / 'findings.json', None, 'Untitled one-paragraph boundary and five typography ligatures.'),
        (Path(__file__), None, 'Individual create-only source stager;no invented heading.')]]
    files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    files[str(comparison_path)] = file_hash(comparison_path)
    groups = [{'group_id': name, 'kind': kind, 'source_line_ids': [x['line_id'] for x in lines],
        'text_sha256': digest(' '.join(x['text'].strip() for x in lines).encode()),
        'reason': 'Source-read template/prose boundary;one printed author paragraph;no heading invented.'}
        for name, kind, lines in [('form', 'front_matter', form), ('summary1', 'prose', prose)]]
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer,
        'reason': findings['only_text_normalization'], 'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
        'pages': [{'page': 1, 'groups': groups}], 'evidence': evidence, 'evidence_files': files,
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, comparison_path.read_bytes())
    block = next(b for b in candidate['blocks'] if b.get('layout_group_id') == 'summary1')
    value, operations = block['text'], []
    for before, after, count in [('ﬁ', 'fi', 4), ('ﬂ', 'fl', 1)]:
        if value.count(before) != count:
            raise ValueError('Exact ligature preimage differs')
        changed = value.replace(before, after)
        operations.append({'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before,
            'new': after, 'count': count, 'before_text_sha256': digest(value.encode()), 'after_text_sha256': digest(changed.encode()),
            'reason': 'Source-read fi/fl typography expansion,not author rewriting.'})
        value = changed
    repair = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2], 'reason': findings['only_text_normalization'],
        'operations': operations, 'evidence': evidence, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, pages)
    owned = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    owned.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if owned != Counter(line['line_id'] for page in pages for line in page['lines']) or any(n != 1 for n in owned.values()):
        raise ValueError('Every native source line must have exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    text = text_with_block_spans(selected)[0]
    expected = normalized_lines(prose)[0].replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    if (text != expected or len(ids) != 1 or len(selected) != 1 or selected[0]['kind'] != 'prose'
            or any(word not in text for word in findings['preserved_printed_wording'])
            or any(word in text for word in ['Summary Sheet', 'MCM/ICM', 'Contents', 'Type a summary'])
            or later(old) != later(candidate)):
        raise ValueError('Complete untitled source prose equality/later-body guard failed')
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'ligature-repairs.json'},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read opening page retains unresolved flags')
    for name, data in [('layout.json', layout), ('source-review.json', review), ('ligature-repairs.json', repair)]:
        json_new(output / name, data)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='Prospective source-checked untitled Summary only;not a corpus build')
    write_new(output / 'summary-preview.md', text + '\n')
    json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'characters': len(text), 'text_sha256': digest(text.encode()),
        'logical_author_paragraphs': 1, 'native_page1_lines': 59, 'source_lines_accounted_once': True,
        'raw_pages_unchanged': True, 'independent_prose_lines_equal_in_order_after_ligatures_and_whitespace': 31,
        'complete_native_prose_equal_after_declared_ligature_expansions': True, 'ligatures_expanded': 5,
        'no_author_heading_invented': True, 'later_actual_author_body_unchanged': True, 'ocr_used': False,
        'native_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['layout.json', 'source-review.json', 'findings.json', 'summary-preview.md', 'ligature-repairs.json']},
        'stager_sha256': file_hash(Path(__file__)), 'source_stage_only': True, 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
