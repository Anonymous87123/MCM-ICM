"""Source-adjudicate q305native/OCRconflict; retain nine original paragraphs."""
import copy
import json
from collections import Counter
from pathlib import Path
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v39-20261031-v1'
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


def main():
    directory = STORE / 'reviews/20261031'
    output = directory / 'q305-summary-restoration-v1'
    if output.exists():
        raise ValueError('Create-only restoration exists;preserve it')
    root, prepared_root = STORE / 'reflow-20261031-v39', STORE / 'reflow-20261031-v38'
    catalog, prepared_parent = Catalog(root), Catalog(prepared_root)
    old = catalog.document('P-D-2021-2100112-1b2d1f1c')
    previous, current = copy.deepcopy(prepared_parent.document(old['paper_id'])), copy.deepcopy(old)
    old_scope, new_scope = previous.pop('scope_id'), current.pop('scope_id')
    if previous != current or old_scope == new_scope:
        raise ValueError('Prepared page transfer must change scope only')
    if any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews')):
        raise ValueError('Existing source reviews require explicit replay')
    original, evidence_folder = directory / 'q305-summary-ocr-v1', directory / 'q305-opening-pages-v1'
    original_manifest, original_page = read_json(original / 'manifest.json'), read_json(original / 'page-0001.json')
    prepared = read_json(evidence_folder / 'manifest.json')
    raw_path = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if (catalog.identity != 'd6b2d80eb3f7d220a15dc89eb949dcec0f94b4e3d247173417bda86d72e0bae1'
            or old['queue_position'] != 305 or prepared['dataset_id'] != prepared_parent.identity
            or file_hash(source) != old['source_sha256'] or file_hash(raw_path) != old['raw_pages_sha256']
            or prepared['source_sha256'] != old['source_sha256'] or prepared['raw_pages_sha256'] != old['raw_pages_sha256']
            or original_manifest['source_sha256'] != old['source_sha256'] or len(original_page['lines']) != 50
            or file_hash(original / 'page-0001.json') != '06eb80972e436e0f2f532d103adc5ad8492b0d6facefd020b9421bedabc58832'
            or file_hash(original / 'page-0001.json') != original_manifest['pages'][0]['sha256']):
        raise ValueError('Exact source/native/OCRidentity differs')
    for name, sha in prepared['files'].items():
        if file_hash(evidence_folder / name) != sha:
            raise ValueError('Actually read source evidence changed')
    pages = rows(raw_path)
    native = {line['line_id']: line for line in pages[0]['lines']}
    revised = copy.deepcopy(original_page)
    corrections = []
    for index, lid in [(9, 'p0001-n0011-l0000'), (28, 'p0001-n0015-l0000'), (31, 'p0001-n0015-l0003')]:
        corrected = native[lid]['text']
        if corrected == original_page['lines'][index]['text']:
            raise ValueError('Expected exact source-read OCRpunctuation/spacing difference')
        revised['lines'][index]['text'] = corrected
        corrections.append({'original_ocr_index': index, 'old_text': original_page['lines'][index]['text'],
            'source_transcription': corrected, 'corroborating_native_line_id': lid,
            'original_ocr_score_retained_as_original_only': original_page['lines'][index]['score'],
            'basis': 'Exact full source page actually read;native line corroborates printed punctuation and spacing,no author words rewritten.'})
    if any(revised['lines'][i] != original_page['lines'][i] for i in range(50) if i not in {9, 28, 31}):
        raise ValueError('Other47OCRline objects changed')
    revised['manual_source_transcriptions'] = corrections
    revised['review_status'] = 'All nine author paragraphs,complete keywords and page boundaries actually source-read;separate exact acceptance proof required.'
    output.mkdir(parents=True)
    findings = {'schema': 'source-prose-layout-findings-v2', 'paper_id': old['paper_id'],
        'source_sha256': old['source_sha256'], 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'reviewer': 'Codex root;2026-10-31;both complete opening JPEGs,all native page1lines and all50OCRlines actually read',
        'checked_pages': [1, 2], 'logical_author_paragraphs': 9,
        'source_boundary': 'Printed Summaryheading and nine author paragraphs onpage1;separate title/form/fullkeywords/watermark/footer.Page2Contents,no Summarycontinuation.',
        'source_conflict': 'Native-versus-pdftotext comparison remained unresolved after actual nine-paragraph layout repair.LocalOCRand source-image adjudication now retain complete paragraph text;independent automatic agreement is not claimed.',
        'transcriptions': corrections, 'preserved_spelling': ['characterstic', 'revolutionaires', 'summerize', 'stengths'],
        'preserved_claims': ['62.8percent', 'p-value smaller than0.001', 'no strong evidence p-value>0.1', 'ten dynamic influencers1960sto2010s'],
        'source_wraps': ['network', 'Centrality', 'measure', 'Mann-Whitney', 'distinguish'],
        'presentation_ligatures': 'OCRexpands ordinary alphabetic presentation ligatures to visible letters;exact native evidence remains preserved;the resulting complete prose must equal native prose under only this declared expansion and five source-checked wraps.',
        'prepared_evidence_scope_transfer': {'old_scope_id': old_scope, 'new_scope_id': new_scope, 'all_other_paper_fields_equivalent': True},
        'scope_boundary': 'Prose,source ownership and boundaries only;no figure interpretation,formula verification or statistical correctness acceptance.',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    json_new(output / 'page-0001.json', revised)
    manifest = {**original_manifest, 'pages': [{'page': 1, 'path': 'page-0001.json',
        'sha256': file_hash(output / 'page-0001.json'), 'line_count': 50,
        'low_confidence_lines': sum(l['score'] < .95 for l in revised['lines'])}],
        'source_recovery': {'original_manifest_sha256': file_hash(original / 'manifest.json'),
            'original_page_sha256': file_hash(original / 'page-0001.json'), 'findings_sha256': file_hash(output / 'findings.json'),
            'only_changes': 'Three source-read line texts;all50original boxes/scores and47other line objects unchanged.'}}
    json_new(output / 'manifest.json', manifest)
    prospective = copy.deepcopy(pages)
    first = prospective[0]
    if first.get('ocr_evidence') or not any('For Task 1' in l['text'] for l in first['lines']):
        raise ValueError('Exact native q305opening preimage differs')
    for line in first['lines']:
        line['superseded_by_ocr'] = True
    for index, value in enumerate(revised['lines']):
        points = value['pdf_box']
        box = [min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)]
        first['lines'].append({'line_id': f'p0001-ocr-l{index:04d}', 'native_block': -1, 'page': 1,
            'bbox': box, 'text': value['text'], 'font_size': max(5, (box[3]-box[1])*.95),
            'bold': value['text'].strip().lower() in {'summary', 'abstract', 'introduction', 'contents'},
            'spans': [], 'ocr_score': value['score'], 'engine': 'rapidocr'})
    first['ocr_status'] = 'candidate'
    first['ocr_evidence'] = {'path': 'raw/ocr/page-0001.json', 'sha256': file_hash(output / 'page-0001.json'),
        'models': manifest['model_sha256'], 'version': manifest['ocr_version']}
    raw = b''.join((json.dumps(page, ensure_ascii=True, sort_keys=True) + '\n').encode() for page in prospective)
    write_new(output / 'prospective-pages.jsonl', raw)
    metrics = STORE / 'span-metrics-20261031-q304-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    working[0] = copy.deepcopy(first)
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    meta = {key: old[key] for key in keys}
    meta['raw_pages_sha256'] = digest(raw)
    identity = {key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': desc,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, desc in [
        (evidence_folder / 'manifest.json', evidence_folder, 'Both actually read complete source JPEGs and exact native evidence.'),
        (original / 'manifest.json', original, 'All50original localOCRlines,boxesandconfidence scores.'),
        (output / 'findings.json', None, 'Complete nine-paragraph source and conflict adjudication.'),
        (output / 'manifest.json', None, 'Versioned source-adjudicated OCRmanifest.'),
        (output / 'page-0001.json', None, 'All50transcribed OCRlines with original confidence explicitly retained as original only.'),
        (Path(__file__), None, 'Exact create-only individual-paper restoration implementation.')]]
    files = {str(p): file_hash(p) for folder in (evidence_folder, original) for p in folder.iterdir() if p.is_file()}
    files.update({e['path']: e['sha256'] for e in evidence})
    by_id = {line['line_id']: line for line in first['lines']}
    definitions = [('form', 'front_matter', range(7)), ('title', 'title', [7]), ('heading', 'heading', [8]),
        ('summary1', 'prose', range(9, 12)), ('summary2', 'prose', range(12, 17)),
        ('summary3', 'prose', range(17, 22)), ('summary4', 'prose', range(22, 28)),
        ('summary5', 'prose', range(28, 32)), ('summary6', 'prose', range(32, 37)),
        ('summary7', 'prose', range(37, 41)), ('summary8', 'prose', range(41, 44)),
        ('summary9', 'prose', range(44, 47)), ('keywords', 'keywords', [47]), ('promotion', 'furniture', range(48, 50))]
    groups = []
    for name, kind, numbers in definitions:
        ids = [f'p0001-ocr-l{i:04d}' for i in numbers]
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': ids,
            'text_sha256': digest(' '.join(by_id[lid]['text'].strip() for lid in ids).encode()),
            'reason': 'Exact source-read Summaryparagraph and non-author source ownership.',
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})})
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': findings['reviewer'],
        'reason': 'Source-adjudicate native/OCRconflict and preserve all nine complete printed paragraphs.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': evidence, 'evidence_files': files, 'remaining_uncertainties': ['Fresh24page metric rebinding required.', 'All later chapter source acceptance pending.'],
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, prospective, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    blocks = {b.get('layout_group_id'): b for b in candidate['blocks']}
    replacements = {'summary2': [('net- w', 'netw'), ('al- ity', 'ality'), ('mea- s', 'meas')],
                    'summary3': [('Mann- W', 'Mann-W')], 'summary4': [('dis- t', 'dist')]}
    operations = []
    for group, pairs in replacements.items():
        block, literal = blocks[group], []
        text = block['text']
        for before, after in pairs:
            if text.count(before) != 1:
                raise ValueError('Exact source wrap preimage differs')
            changed = text.replace(before, after)
            operation = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after,
                'count': 1, 'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Actually source-read discretionary wrap;retain the genuine Mann-Whitneyhyphen.'}
            operations.append(operation); literal.append(operation); text = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])), 'before_text_sha256': digest(text.encode()),
            'after_text_sha256': digest(text.encode()), 'transcription_operations_sha256': digest(encoded(literal)),
            'reason': 'Every source-line wrap in this complete paragraph individually checked.'})
    repair = {**identity, 'reviewer': findings['reviewer'], 'checked_pages': [1, 2],
        'reason': 'Five exact source wraps only;no prose rewrite.', 'operations': operations, 'evidence': evidence,
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, prospective)
    actual = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    actual.update(l['line_id'] for l in candidate['excluded_source_lines'])
    if actual != Counter(l['line_id'] for p in prospective for l in p['lines']) or any(c != 1 for c in actual.values()):
        raise ValueError('Every native/OCRline must retain exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text = text_with_block_spans(selected)[0]
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    # Compare complete paragraph bytes with the actual native prose,using only declared presentation expansion/wraps.
    table = str.maketrans(dict(zip('ﬀﬁﬂﬃﬄﬅﬆ', ('ff', 'fi', 'fl', 'ffi', 'ffl', 'st', 'st'))))
    native_paras = [normalized_lines([l for l in pages[0]['lines'] if l['native_block'] == n])[0].translate(table)
                    for n in range(11, 20)]
    for group, pairs in replacements.items():
        at = int(group.removeprefix('summary')) - 1
        for before, after in pairs:
            native_paras[at] = native_paras[at].replace(before, after)
    expected = 'Summary\n\n' + '\n\n'.join(native_paras)
    if (text != expected or len(ids) != 1 or sum(b['kind'] != 'heading' for b in selected) != 9
            or {p for b in selected for p in b['source_pages']} != {1}
            or any(s not in text for s in ['62.8%', 'p-value smaller than 0.001', 'p-value > 0.1', 'characterstic', 'revolutionaires', 'summerize the stengths'])
            or any(s in text for s in ['Summary Sheet', 'MCM/ICM', 'Keywords:', '关注', 'MATHmodels'])):
        raise ValueError('Complete source-native-versus-OCRprose equality/paragraph guard failed')
    later = lambda d: [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(d) if min(b['source_pages']) > 1]
    if later(old) != later(candidate):
        raise ValueError('Later actual author body changed')
    proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1,
        'all_page_prose_and_boundaries_actually_read': True, 'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'],
        'raw_page_sha256': digest(encoded(first)), 'layout_groups_sha256': digest(encoded(groups)),
        'final_page_blocks_sha256': digest(encoded(page_blocks_signature(candidate, 1))),
        'reviewed_page_jpeg_sha256': prepared['files']['page-0001.jpg'], 'reviewed_page_jpeg_bytes': 394590}
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True, 'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'word-repairs.json'},
        'ocr_prose_page_reviews': [proof], 'section_source_fidelity_approved': True,
        'whole_paper_source_acceptance': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review]); apply_ocr_page_reviews(candidate, prospective)
    validate_ocr_page_reviews(candidate, prospective)
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-checked opening page retains a pending flag')
    json_new(output / 'layout.json', layout); json_new(output / 'word-repairs.json', repair); json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective source-checked prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n'); json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'characters': len(text), 'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 9,
        'original_ocr_lines': 50, 'unchanged_ocr_line_objects': 47, 'manually_source_transcribed_lines': [9, 28, 31],
        'literal_wrap_occurrences_repaired': 5, 'complete_native_prose_equal_after_declared_ligature_expansion_and_wraps': True,
        'source_lines_accounted_once': True, 'later_actual_author_body_unchanged': True,
        'selected_source_status': 'verified in prospective stage only', 'native_metric_binding_transfer_still_required': True,
        'new_ocr_override_not_yet_in_any_corpus': True, 'span_metrics_source_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['manifest.json', 'page-0001.json', 'findings.json',
            'layout.json', 'word-repairs.json', 'source-review.json', 'summary-preview.md', 'prospective-pages.jsonl']},
        'stager_sha256': file_hash(Path(__file__)), 'library_sha256': file_hash(RUNTIME / 'scripts/text_corpus.py'),
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True); print(result, flush=True)


if __name__ == '__main__':
    main()
