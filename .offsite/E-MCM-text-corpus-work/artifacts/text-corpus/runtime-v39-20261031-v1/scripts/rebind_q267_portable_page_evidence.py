"""Bind inspected q267 JPEG/native/OCR evidence into a portable proof bundle."""
import copy
from pathlib import Path

from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_ocr_page_reviews import apply_ocr_page_reviews, validate_ocr_page_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import file_hash, json_new, make_document, read_json, rows


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    parent = base / 'reflow-20261031-v32'
    catalog = Catalog(parent)
    previous = base / 'reviews/20261031/q267-source-page-acceptance-v1'
    output = base / 'reviews/20261031/q267-source-page-acceptance-v2'
    if output.exists():
        raise ValueError('Create-only source proof exists; preserve it')
    preflight = read_json(previous / 'preflight.json')
    if preflight['parent_dataset_id'] != catalog.identity:
        raise ValueError('Exact accepted parent required')
    for name, sha in preflight['proof_sha256'].items():
        if file_hash(Path(name)) != sha:
            raise ValueError('Previously staged source proof changed')
    old = catalog.document(preflight['paper_id'])
    stage = base / 'reviews/20261031/q267-ocr-line-restoration-v2'
    metrics = base / 'span-metrics-20261031-q267-v2'
    pages = rows(stage / 'prospective-pages.jsonl')
    if file_hash(stage / 'prospective-pages.jsonl') != preflight['new_raw_pages_sha256']:
        raise ValueError('Exact prospective raw source changed')
    layout = read_json(previous / 'layout.json')
    bundles = [base / 'reviews/20261031/q267-opening-pages-v1', stage,
        base / 'reviews/20261031/q267-missing-line-ocr-crop-v2', base / 'ocr-2516178-page1-20261029-v1']
    for folder in bundles:
        source = folder / ('result.json' if 'ocr-crop-v2' in folder.name else 'manifest.json')
        matches = [proof for proof in layout['evidence'] if Path(proof['path']).resolve() == source.resolve()]
        if matches:
            matches[0]['bundle_root'] = str(folder)
        else:
            layout['evidence'].append({'path': str(source), 'sha256': file_hash(source), 'bundle_root': str(folder),
                'description': 'Complete source-bound native/OCR/page-image evidence retained for portable replay.'})
    focused = base / 'reviews/20261031/q267-first-task-crop-v2.jpg'
    layout['evidence'].append({'path': str(focused), 'sha256': file_hash(focused),
        'description': 'Actually read bounded crop of missing first-task prose line.'})
    output.mkdir(parents=True)
    json_new(output / 'layout.json', layout)
    layouts, copies = prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',),
        application_status='applied source-checked prose lanes; no whole-paper acceptance')
    image_sha = read_json(previous / 'source-review.json')['ocr_prose_page_reviews'][0]['reviewed_page_jpeg_sha256']
    if not any(name.endswith('.jpg') and sha == image_sha for name, (_, sha) in copies.items()):
        raise ValueError('Actually inspected complete page JPEG missing from portable bundle')
    meta = {key: old[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
        'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    meta['raw_pages_sha256'] = preflight['new_raw_pages_sha256']
    working, _ = prepare_flow_pages(meta, pages, metrics)
    applied = apply_layout_reviews(meta, working, layouts)
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    repair = read_json(previous / 'word-repairs.json')
    review = read_json(previous / 'source-review.json')
    apply_text_repairs(candidate, [repair])
    apply_reviews(candidate, [review])
    apply_ocr_page_reviews(candidate, pages)
    validate_layout_reviews(candidate, pages)
    validate_ocr_page_reviews(candidate, pages)
    json_new(output / 'word-repairs.json', repair)
    json_new(output / 'source-review.json', review)
    result = copy.deepcopy(preflight)
    result.update(stager_sha256=file_hash(Path(__file__)),
        supersedes_unapplied_preflight_sha256=file_hash(previous / 'preflight.json'),
        portability_rejection='V1review declared image hashes only in evidence_files; portable bundler correctly kept only explicit evidence declarations, so complete page JPEG was absent.',
        portable_evidence_files_checked=len(copies), portable_page_jpeg_included=True,
        proof_sha256={str((output / name).resolve()): file_hash(output / name)
            for name in ('layout.json', 'word-repairs.json', 'source-review.json')})
    json_new(output / 'preflight.json', result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
