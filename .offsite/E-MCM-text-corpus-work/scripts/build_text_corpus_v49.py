"""Promote source-read q327-330 and narrowly tested unused-spacing-path fix."""
from collections import Counter
import os
from pathlib import Path
import shutil
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v49-20261031-v1'
sys.path.insert(0, str(RUNTIME / 'scripts'))
from corpus_queries import all_author_blocks
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import digest, file_hash, json_new, read_json, text_with_block_spans, write_new
from validate_text_corpus import validate


def pending(doc):
    return Counter(d['code'] for d in doc['defects'] if d.get('status') != 'resolved')


def later(doc):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(doc) if min(b['source_pages']) > 1]


def main():
    os.chdir(WORK)
    parent, output = STORE / 'reflow-20261031-v48', STORE / 'reflow-20261031-v49'
    request, report = [STORE / name for name in ('build-request-reflow-20261031-v49.json', 'integrity-reflow-20261031-v49.json')]
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Preserve existing create-only build')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree;no cleanup authorized')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v48.json')
    if (catalog.identity != 'aaf55eb868a5960b60ba33baa87772579f18e35d8bbaad1e82e1efd69684b078'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Exact accepted v48 required')
    test_report_path = STORE / 'runtime-v49-validation-20261031-v1.json'
    tests = read_json(test_report_path)
    old_runtime = read_json(STORE / 'build-request-reflow-20261031-v48.json')['implementation_sha256']
    frozen = {name: file_hash(RUNTIME / 'scripts' / name) for name in old_runtime}
    changed = {name for name in frozen if frozen[name] != old_runtime[name]}
    if (len(frozen) != 15 or changed != {'text_corpus.py'}
            or frozen['text_corpus.py'] != 'ce392bb513036e8a9915f94b437ef5397bacb026714abc99ed3d43b4c23fb641'
            or tests['new_test']['sha256'] != file_hash(RUNTIME / tests['new_test']['path'])
            or [r.get('passed', r.get('ran')) for r in tests['observed_execution']] != [11, 359, 357]
            or any(r['exit_code'] for r in tests['observed_execution'])):
        raise ValueError('Exactly one tested production-code change required')
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256', 'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    extra = {field: [] for field in fields}
    targets, frozen_stages = {}, {str(test_report_path): file_hash(test_report_path)}
    totals, defects = dict(accepted['totals']), Counter(accepted['defects'])
    earlier = Catalog(STORE / 'reflow-20261031-v47')
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    stages = [
        (327, 'P-D-2025-2519935-f07f7c47', 27, 1, 3233, 6, '3604811af36b896facd4febac11d7e89593d5c8b8561638abe14891546023fbe', '26d69bf8dcd67ac01798861861954c09d4028c42a2658bf30ffb7dae5d77a3d7', 'word-wrap-repairs.json'),
        (328, 'P-E-2016-43443-82025ab9', 23, 1, 2449, 1, 'a6884e1df8379a578a9ee9651e8f5b3fe35c320dd403d8f5832c3e218f13b70d', 'c7e024ff3cba71d0519bd782c2dcb4b83d888c86c202856ce66432a2dd501e03', 'ligature-repairs.json'),
        (329, 'P-E-2016-49630-af20ebac', 23, 2, 2557, 4, 'e93c99479a31751f86a638d71ecacd4af9c5219a92e9b00aa77df09d36f2973b', '429afb6e9f702d6771caa7928be30a8c8eb7fb7aecddca527e5469ad366f10a9', 'glyph-repairs.json'),
        (330, 'P-E-2016-52831-df9e4468', 18, 1, 2106, 4, 'b62ae3c68083059c996d7526056b13ca81e715b7a2586b7b924a77e85a7b99fb', '07a28bec24493da953fb67097086dcd844b9e68d21f3469fd3b2807eb964dc63', None)]
    for queue, pid, pages, version, length, paragraphs, sha, stager_sha, repair in stages:
        stage = STORE / f'reviews/20261031/q{queue}-native-summary-v{version}'
        p = read_json(stage / 'preflight.json')
        old, candidate = catalog.document(pid), read_json(stage / 'candidate.json')
        if (p['paper_id'] != pid or old['queue_position'] != queue or old['page_count'] != pages
                or p['parent_dataset_id'] != (earlier.identity if queue < 329 else catalog.identity)
                or p['source_sha256'] != old['source_sha256'] or p['raw_pages_sha256'] != old['raw_pages_sha256']
                or not p['raw_pages_unchanged'] or not p['source_lines_accounted_once']
                or not p['later_actual_author_body_unchanged'] or p['whole_paper_source_acceptance'] or p['ai_receipts_created'] or p['ocr_used']
                or p['characters'] != length or p['logical_author_paragraphs'] != paragraphs
                or p['text_sha256'] != sha or p['stager_sha256'] != stager_sha
                or p['native_metrics_manifest_sha256'] != file_hash(metrics / 'manifest.json')):
            raise ValueError('Exact individual source-read stage required')
        if queue < 329:
            before = earlier.document(pid)
            changes = {k for k in set(before) | set(old) if before.get(k) != old.get(k)}
            if (changes != {'scope_id'} or before['scope_id'] != '7ade617d1073c41ab21f31dfb14c5a5e41b2b23b8c42f4e74344f264adbf0d01'
                    or old['scope_id'] != '9fe78442563c1eeafcf81754aff7d0d3b93886d222374ac6dce669d83f696e4f'):
                raise ValueError('v47stage permits exact scope-only preimage change;all content/source identical')
        if (queue == 327 and (p['author_wraps_repaired'] != 3 or p['margin_microtext_lines_preserved_as_furniture'] != 687 or p['independent_prose_lines_equal_in_order'] != 36)
                or queue == 328 and (p['ligatures_expanded'] != 5 or not p['no_author_heading_invented'] or p['independent_prose_lines_equal_in_order_after_ligatures_and_whitespace'] != 31)
                or queue == 329 and (p['printed_glyphs_transcribed'] != 2 or p['independent_prose_lines_equal_in_order_after_one_comparison_spacing'] != 27)
                or queue == 330 and (not p['complete_native_prose_equal_without_literal_edits'] or not p['no_author_heading_invented'] or p['independent_prose_lines_equal_in_order_after_comparison_whitespace'] != 23)):
            raise ValueError('Exact source paragraph/wrap/typography comparison assertions required')
        stager = Path(__file__).with_name(f'stage_q{queue}_native_summary_v{version}.py')
        frozen_stages.update({str(stage / name): value for name, value in p['proof_sha256'].items()})
        frozen_stages.update({str(stage / 'preflight.json'): file_hash(stage / 'preflight.json'), str(stage / 'candidate.json'): file_hash(stage / 'candidate.json'), str(stager): stager_sha})
        summary = (stage / 'summary-preview.md').read_text(encoding='utf-8').removesuffix('\n')
        author = summary + '\n\n' + text_with_block_spans([b for b in all_author_blocks(old) if min(b['source_pages']) > 1])[0]
        if (len(summary) != length or digest(summary.encode()) != sha or later(old) != later(candidate)
                or text_with_block_spans(all_author_blocks(candidate))[0] != author):
            raise ValueError('Complete restored selection or later body differs')
        targets[pid] = {'abstract': summary, 'all_author_text': author}
        extra['source_review_sha256'].append(stage / 'source-review.json')
        extra['layout_review_sha256'].append(stage / 'layout.json')
        if repair:
            extra['text_repair_sha256'].append(stage / repair)
        defects.subtract(pending(old)); defects.update(pending(candidate))
        totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        totals['sections'] += len(candidate['sections']) - len(old['sections'])
        totals['boundary_verified'] += 1
    spacing_pid = 'P-B-2010-8362-bd23db32'
    spacing_doc = catalog.document(spacing_pid)
    spacing_flags = [d for d in spacing_doc['defects'] if d['code'] == 'expanded_line_spacing_review' and d.get('page') in {3, 4}]
    if len(spacing_flags) != 2 or any(d.get('status') == 'resolved' for d in spacing_flags):
        raise ValueError('Exact two unused existing spacing flags required')
    for page in (3, 4):
        layouts = [r for r in spacing_doc.get('layout_reviews', []) if any(q['page'] == page for q in r['pages'])]
        if len(layouts) != 1 or not layouts[0]['paragraph_boundaries_checked'] or not layouts[0]['reading_lanes_checked']:
            raise ValueError('Known spacing-only effect requires frozen explicit source layout')
    defects['expanded_line_spacing_review'] -= 2
    defects = {key: value for key, value in defects.items() if value}
    if any(v < 0 for v in defects.values()) or any(file_hash(Path(path)) != sha for path, sha in frozen_stages.items()):
        raise ValueError('Frozen individual proof changed or invalid expected counts')
    scope, inputs = read_json(parent / 'scope.json'), {field: [] for field in fields}
    for field in fields:
        for path, sha in scope.get(field, {}).items():
            if file_hash(Path(path)) != sha:
                raise ValueError('Existing accepted evidence changed')
            inputs[field].append(Path(path))
        inputs[field].extend(extra[field])
        if len({str(p.resolve()) for p in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 62:
        raise ValueError('All62existing OCR raw inputs must remain unchanged')
    bindings = {field: {str(path.resolve()): file_hash(path) for path in paths} for field, paths in inputs.items()}
    previous = {family: {x['paper_id']: x for x in catalog.select(family)} for family in ('abstract', 'all_author_text')}
    if any(previous['abstract'][pid]['status'] != 'present-unverified' for pid in targets):
        raise ValueError('Exactly four previously unverified summaries required')
    native = WORK / 'artifacts/text-corpus/native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native corpus changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'individual_source_stage_sha256': frozen_stages, 'raw_pages_sha256_overrides': {},
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'), 'expected_totals': totals, 'expected_open_defects': defects,
        'change': 'Only source-read q327-330 Summaries;q327three wraps/687margin objects;q328five typography ligatures/no heading;q329two printed alpha transcriptions/no semantics;q330four untitled paragraphs/no literal edits.Only tested code change skips unused spacing heuristic on exact source-reviewed groups.Two preexisting spacing-only flags on P-B-2010-8362 pages3/4 no longer generated;all its other data identical.All435raw,431other selections/statuses,later author body unchanged.Failedq329v1preserved.',
        'source_boundary_reviews_added': 4, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
        inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (RUNTIME / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v49.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            pid, before = item['paper_id'], previous[family][item['paper_id']]
            if pid not in targets:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated431selection/status changed')
            elif (built.text_and_spans(item)[0] != targets[pid][family]
                    or item['status'] != ('verified' if family == 'abstract' else before['status'])):
                raise ValueError('Complete restored selection/status differs')
    for pid in catalog.by_id:
        old, new = catalog.document(pid), built.document(pid)
        if new['raw_pages_sha256'] != old['raw_pages_sha256'] or later(old) != later(new):
            raise ValueError('Raw source or later actual author body changed')
        if pid not in targets:
            expected = dict(old)
            expected['scope_id'] = new['scope_id']
            if pid == spacing_pid:
                expected['defects'] = [d for d in old['defects'] if d not in spacing_flags]
            if expected != new:
                raise ValueError('Unrelated paper changed beyond exact scope/two declared unused flags')
    result = validate(output, WORK, True)
    if (result['totals'] != totals or result['defects'] != defects
            or not result['structural_integrity_pass'] or result['source_completeness_accepted']):
        raise ValueError('Unexpected counts/flags/acceptance;preserve failed output')
    for group in [frozen_stages, *bindings.values(), {str(RUNTIME / 'scripts' / name): sha for name, sha in frozen.items()}]:
        if any(file_hash(Path(path)) != sha for path, sha in group.items()):
            raise ValueError('Frozen proof/runtime changed')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
