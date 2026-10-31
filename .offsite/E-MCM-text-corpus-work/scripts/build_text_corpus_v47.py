"""Promote individually source-read q319-322; preserve all unrelated bytes/selections."""
from collections import Counter
import os
from pathlib import Path
import shutil
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v44-20261031-v1'
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
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues'])
            for b in all_author_blocks(doc) if min(b['source_pages']) > 1]


def main():
    os.chdir(WORK)
    parent, output = STORE / 'reflow-20261031-v46', STORE / 'reflow-20261031-v47'
    request = STORE / 'build-request-reflow-20261031-v47.json'
    report = STORE / 'integrity-reflow-20261031-v47.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Preserve existing create-only build')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree;no cleanup authorized')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v46.json')
    if (catalog.identity != '14b2a806afc77d65652f359bdc1901959bc69869ff12935f3bd344a80f6b2e59'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Exact accepted v46 required')
    directory = STORE / 'reviews/20261031'
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    extra = {field: [] for field in fields}
    targets, frozen_stages = {}, {}
    totals, defects = dict(accepted['totals']), Counter(accepted['defects'])
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    earlier = Catalog(STORE / 'reflow-20261031-v45')
    for queue, pid, pages, length, paragraphs, wraps, sha, stager_sha in [
        (319, 'P-D-2023-2304962-b6a95eaf', 25, 2991, 7, 4,
         'b6ab3b03cbda279b6bd4cd94aa42be17f99a50a0c427d05050d339c6173022c6',
         'ece08d0287ce838bccd806620d25b5d42fcc66d76e234d32362849da430b57c7'),
        (320, 'P-D-2024-2417004-a737e95b', 25, 2711, 8, 4,
         '30183ae7c606a6c84cdb10ebfb3f5c9a58178cfde431f3920ad1fe2021ddb3e3',
         '79f9b82e4c4f9b437e0ecc16113d301636733e0c8d1316ce7b0515e4506c0c08'),
        (321, 'P-D-2024-2417831-f399a6df', 25, 3020, 7, 5,
         '888be40bd29bac2c70729b80a9d61ada7b487569281228bff42ce0251931576f',
         'a2151a5f272b0f12560beaa44502c1d7bc1fda7502ba0c0b5cb9adf12d713baf'),
        (322, 'P-D-2024-2419588-1cc62ede', 27, 1643, 3, 9,
         'dab743d967702360bf0c9d6c567c0b499ee5ae1c576240a8fe2f131db2e70f86',
         '91bbab2e1b2b6e52a64c9374bf82db268cab42c69484f9c837823d544d22a9af')]:
        stage = directory / f'q{queue}-native-summary-v1'
        preflight_path = stage / 'preflight.json'
        p = read_json(preflight_path)
        old, candidate = catalog.document(pid), read_json(stage / 'candidate.json')
        if (p['paper_id'] != pid or old['queue_position'] != queue or old['page_count'] != pages
                or p['parent_dataset_id'] != (earlier.identity if queue <= 320 else catalog.identity)
                or p['source_sha256'] != old['source_sha256']
                or p['raw_pages_sha256'] != old['raw_pages_sha256'] or not p['raw_pages_unchanged']
                or p['characters'] != length or p['logical_author_paragraphs'] != paragraphs
                or p['text_sha256'] != sha or p['stager_sha256'] != stager_sha
                or not p['complete_native_prose_equal_after_declared_source_wraps']
                or not p['source_lines_accounted_once'] or not p['later_actual_author_body_unchanged']
                or p['author_wraps_repaired'] != wraps or p['whole_paper_source_acceptance']
                or p['ai_receipts_created']
                or p['native_metrics_manifest_sha256'] != file_hash(metrics / 'manifest.json')):
            raise ValueError('Exact individual source-read/native-preserving stage required')
        if p['ocr_used']:
            raise ValueError('All four stages are native-only')
        if queue <= 320:
            preimage = earlier.document(pid)
            changed = {key for key in set(preimage) | set(old) if preimage.get(key) != old.get(key)}
            if (changed != {'scope_id'}
                    or preimage['scope_id'] != 'c8a9e8cfc69cc766dedb2fadfd5e216ebe37b60ecdc5754fa4cc56a6d8aa2a63'
                    or old['scope_id'] != '960bf99280f06de911967885d9f50c5cc9baabd4d23f31357e3e70aefc6ae8ad'):
                raise ValueError('Frozen v45stage permits only the exact v46scope identity change;all source/content fields must match')
        if (queue in (319, 321) and p['genuine_hyphen_line_spaces_closed'] != 1
                or queue == 320 and (p['full_author_paragraphs'] != 7 or p['standalone_lead_in_blocks'] != 1
                    or p['independent_prose_lines_equal_in_order'] != 31)
                or queue == 321 and p['independent_prose_lines_equal_in_order'] != 39
                or queue == 322 and (p['keyword_wraps_repaired'] != 1
                    or p['independent_prose_lines_equal_in_order'] != 21)):
            raise ValueError('Exact paragraph/lead-in/Keyword/source-line assertions required')
        stager = Path(__file__).with_name(f'stage_q{queue}_native_summary_v1.py')
        frozen_stages.update({str(stage / name): value for name, value in p['proof_sha256'].items()})
        frozen_stages.update({str(preflight_path): file_hash(preflight_path),
            str(stage / 'candidate.json'): file_hash(stage / 'candidate.json'), str(stager): stager_sha})
        summary = (stage / 'summary-preview.md').read_text(encoding='utf-8').removesuffix('\n')
        author = summary + '\n\n' + text_with_block_spans(
            [block for block in all_author_blocks(old) if min(block['source_pages']) > 1])[0]
        if (len(summary) != length or digest(summary.encode()) != sha or later(old) != later(candidate)
                or text_with_block_spans(all_author_blocks(candidate))[0] != author):
            raise ValueError('Complete restored selection or later author body differs')
        targets[pid] = {'abstract': summary, 'all_author_text': author}
        extra['source_review_sha256'].append(stage / 'source-review.json')
        extra['layout_review_sha256'].append(stage / 'layout.json')
        extra['text_repair_sha256'].append(stage / 'word-wrap-repairs.json')
        defects.subtract(pending(old))
        defects.update(pending(candidate))
        totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        totals['sections'] += len(candidate['sections']) - len(old['sections'])
        totals['boundary_verified'] += 1
    if any(file_hash(Path(path)) != sha for path, sha in frozen_stages.items()):
        raise ValueError('Frozen individual proof changed')
    defects = {key: value for key, value in defects.items() if value}
    scope, inputs = read_json(parent / 'scope.json'), {field: [] for field in fields}
    for field in fields:
        for path, sha in scope.get(field, {}).items():
            if file_hash(Path(path)) != sha:
                raise ValueError('Existing accepted evidence changed')
            inputs[field].append(Path(path))
        inputs[field].extend(extra[field])
        if len({str(path.resolve()) for path in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 62:
        raise ValueError('All62existing OCR raw inputs must remain unchanged')
    names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py', 'source_text_repairs.py',
        'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py', 'corpus_queries.py',
        'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py', 'extract_text_span_metrics.py',
        'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(RUNTIME / 'scripts' / name) for name in names}
    if frozen != read_json(STORE / 'build-request-reflow-20261031-v46.json')['implementation_sha256']:
        raise ValueError('Production runtime must remain unchanged')
    bindings = {field: {str(path.resolve()): file_hash(path) for path in paths} for field, paths in inputs.items()}
    previous = {family: {item['paper_id']: item for item in catalog.select(family)}
                for family in ('abstract', 'all_author_text')}
    if any(previous['abstract'][pid]['status'] != 'present-unverified' for pid in targets):
        raise ValueError('Exactly four previously unverified summaries required')
    native = WORK / 'artifacts/text-corpus/native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native corpus changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'individual_source_stage_sha256': frozen_stages, 'raw_pages_sha256_overrides': {},
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_totals': totals, 'expected_open_defects': defects,
        'change': 'Only individually source-read q319-322 native Summary layouts/wraps.q320standalonelead-in retained;q321/322full Keyword lines separated from advertising;q322limitations and Ccover/Ddirectory disagreement preserved.All435raw/all431other selections/statuses/all later author body unchanged.No runtime change.Frozen q319/q320v45stages permit only the exact scope_id change to acceptedv46;every other target-document field must be identical.',
        'source_boundary_reviews_added': 4, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (RUNTIME / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v47.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            pid, before = item['paper_id'], previous[family][item['paper_id']]
            if pid not in targets:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated431paper selection/status changed')
            elif (built.text_and_spans(item)[0] != targets[pid][family]
                    or item['status'] != ('verified' if family == 'abstract' else before['status'])):
                raise ValueError('Complete restored selection/status differs')
    for pid in catalog.by_id:
        old, new = catalog.document(pid), built.document(pid)
        if new['raw_pages_sha256'] != old['raw_pages_sha256']:
            raise ValueError('Unexpected raw source change')
        if pid in targets and later(old) != later(new):
            raise ValueError('Later author body changed')
    result = validate(output, WORK, True)
    if (result['totals'] != totals or result['defects'] != defects
            or not result['structural_integrity_pass'] or result['source_completeness_accepted']):
        raise ValueError('Unexpected counts/flags/acceptance;preserve failed candidate')
    for group in [frozen_stages, *bindings.values(),
                  {str(RUNTIME / 'scripts' / name): sha for name, sha in frozen.items()}]:
        if any(file_hash(Path(path)) != sha for path, sha in group.items()):
            raise ValueError('Frozen proof/runtime changed')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
