"""Bind seven individually transcribed wrap flags without changing source text."""
import copy
from pathlib import Path

from corpus_queries import all_author_blocks, select_sections, selected_blocks
from corpus_reader import Catalog
from preview_span_origin_flow import merge_text_repairs
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_layout_reviews import apply_layout_reviews
from source_paragraph_reviews import apply_paragraph_reviews, validate_paragraph_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs, validate_hyphen_resolutions
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, text_with_block_spans


def main():
    base = Path(__file__).resolve().parents[1] / 'artifacts/text-corpus'
    root = base / 'reflow-20261031-v26'
    directory = base / 'reviews/20261031'
    catalog = Catalog(root)
    scope = read_json(root / 'scope.json')
    result_path = directory / 'q114-q116-wrap-resolution-preflight-v1.json'
    outputs = [directory / f'q{n:03d}-summary-word-repairs-v2.json' for n in (114, 116)]
    if any(p.exists() for p in (*outputs, result_path)):
        raise ValueError('Create-only proof/preflight exists; preserve it')
    pending = []
    contracts = []
    for number, output in zip((114, 116), outputs):
        paper = next(p for p in catalog.papers if p['queue_position'] == number)
        old = catalog.document(paper['paper_id'])
        original_path = directory / f'q{number:03d}-summary-word-repairs-v1.json'
        if scope['text_repair_sha256'].get(str(original_path.resolve())) != file_hash(original_path):
            raise ValueError('Original accepted proof binding differs')
        original = read_json(original_path)
        previous = [r for r in old['text_repair_reviews']
                    if r['operations'] == original['operations'] and
                    r['checked_pages'] == original['checked_pages']]
        if len(previous) != 1:
            raise ValueError('Exact accepted portable proof required')
        proof = copy.deepcopy(original)
        proof['binding_transfer'] = {
            'previous_review_sha256': digest(encoded(previous[0])),
            'previous_external_file_sha256': file_hash(original_path),
            'parent_dataset_id': catalog.identity,
            'reason': 'Same literal transcriptions and source evidence; append exact per-block wrap-resolution operations.'}
        by_id = {b['block_id']: b for b in old['blocks']}
        touched = sorted({op['block_id'] for op in original['operations']})
        for bid in touched:
            block = by_id[bid]
            if 'hyphen_join_review' not in block['issues']:
                raise ValueError('Expected existing stale wrap flag is missing')
            chain = [op for op in original['operations'] if op['block_id'] == bid and op['operation'] == 'literal_replace']
            sha = digest(block['text'].encode())
            proof['operations'].append({
                'operation': 'resolve_hyphen_join_review', 'block_id': bid,
                'before_text_sha256': sha, 'after_text_sha256': sha,
                'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
                'transcription_operations_sha256': digest(encoded(chain)),
                'reason': 'Every printed wrap in this exact paragraph was individually checked and literally transcribed in the preceding operations; no pending wrapped fragment remains. Other defects stay open.'})
        pages = rows(root / 'papers' / old['paper_id'] / 'raw/pages.jsonl')
        working, _ = prepare_flow_pages(old, pages, base / 'span-metrics-20261030-v1')
        meta = {k: old[k] for k in ('paper_id', 'problem_type', 'year', 'queue_position',
                                   'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
        layouts = apply_layout_reviews(meta, working, old.get('layout_reviews', []))
        new = make_document(meta, working, improved=True)
        new['layout_reviews'] = layouts
        resolve_exact_comparisons(new, pages, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
        apply_text_repairs(new, merge_text_repairs(old.get('text_repair_reviews', []), [proof], old['paper_id']))
        apply_paragraph_reviews(new, old.get('paragraph_join_reviews', []))
        validate_paragraph_reviews(new)
        apply_reviews(new, [s['review'] for s in old['sections'] if s.get('review')])
        validate_hyphen_resolutions(new)
        for doc in (old, new):
            ids, excluded = select_sections(doc, 'abstract')
            doc['_comparison_abstract'] = text_with_block_spans(selected_blocks(doc, {
                'section_ids': ids, 'excluded_roles': sorted(excluded)}))[0]
        if (old['_comparison_abstract'] != new['_comparison_abstract'] or
                text_with_block_spans(all_author_blocks(old))[0] != text_with_block_spans(all_author_blocks(new))[0] or
                [(b['block_id'], b['source_line_ids']) for b in old['blocks']] !=
                [(b['block_id'], b['source_line_ids']) for b in new['blocks']]):
            raise ValueError('A metadata-only wrap resolution changed author text or line ownership')
        old_open = [d for d in old['defects'] if d.get('status') != 'resolved' and
                    not (d['code'] == 'hyphen_join_review' and d.get('block_id') in touched)]
        new_open = [d for d in new['defects'] if d.get('status') != 'resolved']
        if old_open != new_open:
            raise ValueError('Unrelated defect was changed/cleared')
        if len(touched) != (6 if number == 114 else 1):
            raise ValueError('Exact reviewed flag count differs')
        for evidence in proof['evidence']:
            if file_hash(Path(evidence['path'])) != evidence['sha256']:
                raise ValueError('Previously inspected source evidence changed')
        contracts.append({'paper_id': old['paper_id'], 'queue_position': number,
            'abstract_sha256': digest(old['_comparison_abstract'].encode()),
            'abstract_characters': len(old['_comparison_abstract']), 'flags_resolved': len(touched),
            'block_ids': touched, 'source_lines_unchanged': True, 'author_text_unchanged': True,
            'other_open_defects_unchanged': True})
        pending.append((output, proof))
    for path, proof in pending:
        json_new(path, proof)
    result = {'schema': 'individual-reviewed-wrap-resolution-preflight-v1',
        'parent_dataset_id': catalog.identity, 'contracts': contracts,
        'proof_files': {str(p.resolve()): file_hash(p) for p in outputs},
        'source_fidelity_approved': False, 'whole_paper_acceptances_added': 0,
        'ai_reading_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(result_path, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
