"""Restore one exact native/independent prose line misclassified as a caption.

No global caption heuristic, text rewriting or source-fidelity waiver is added.
Same-page paragraph seams remain explicitly pending in this bounded repair.
"""
from collections import Counter
import copy
from pathlib import Path
import re

from corpus_reader import Catalog
from corpus_queries import all_author_blocks
from source_absence_reviews import prepare_review_bundles
from source_text_repairs import apply_text_repairs, replay_block
from text_corpus import digest, file_hash, json_new, read_json, rows, text_with_block_spans, write_new


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261031-v27'
    directory = base / 'reviews/20261031'
    names = ('evidence', 'findings', 'repair', 'preflight')
    paths = {name: directory / f'q236-caption-prose-line-{name}-v1.json' for name in names}
    preview_path = directory / 'q236-caption-prose-line-preview-v1.md'
    if any(p.exists() for p in [*paths.values(), preview_path]):
        raise ValueError('Create-only recovery evidence exists; preserve it')
    catalog = Catalog(root)
    pid = 'P-C-2023-2309397-285a4e67'
    old = catalog.document(pid)
    meta = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    paper = root / 'papers' / pid
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    raw_path = paper / 'raw/pages.jsonl'
    independent_path = paper / 'raw/pdftotext.bin'
    if file_hash(source) != old['source_sha256'] or file_hash(raw_path) != old['raw_pages_sha256']:
        raise ValueError('Original PDF/native source binding differs')
    pages = rows(raw_path)
    members = [x for x in pages[0]['lines'] if x['native_block'] == 11 and x['text'].strip()]
    expected_ids = [f'p0001-n0011-l{n:04d}' for n in range(5)]
    if ([x['line_id'] for x in members] != expected_ids or
            any(abs(x['font_size'] - 12) > .001 for x in members) or
            any(abs(x['bbox'][0] - 90.024) > .01 for x in members) or
            any(abs(b['bbox'][1] - a['bbox'][1] - 15.6) > .01 for a, b in zip(members, members[1:]))):
        raise ValueError('Exact five-line continuous native paragraph differs')
    blocks = {b['block_id']: b for b in old['blocks']}
    a, missing, b = [blocks[f'b0000{n}'] for n in (13, 14, 15)]
    if (a['kind'] != 'prose' or missing['kind'] != 'caption' or b['kind'] != 'prose' or
            a['source_line_ids'] + missing['source_line_ids'] + b['source_line_ids'] != expected_ids or
            missing['text'] != 'Table 9. We also used the Association Rule Model based on Apriori algorithm to'):
        raise ValueError('Exact caption/prose misclassification preimage differs')
    independent = independent_path.read_bytes().decode('utf-8', 'strict').split('\f')[0]
    normalize = lambda text: re.sub(r'\s+', ' ', text).strip()
    paragraph = ' '.join(x['text'].strip() for x in members)
    if normalize(independent).count(paragraph) != 1:
        raise ValueError('Independent first-page text does not contain the complete exact paragraph once')
    if old.get('text_repair_reviews') or old.get('layout_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Additional existing paper-specific proofs need explicit replay before staging')
    selected_before = next(x for x in catalog.select('abstract') if x['paper_id'] == pid)
    before, _ = catalog.text_and_spans(selected_before)
    if selected_before['status'] != 'present-unverified' or missing['text'] in before:
        raise ValueError('Reader omission contract differs')
    evidence = {'schema': 'dual-extractor-prose-line-evidence-v1', **meta,
        'parent_dataset_id': catalog.identity, 'document_sha256': file_hash(paper / 'document.json'),
        'physical_page': 1, 'native_lines': members, 'full_native_paragraph': paragraph,
        'independent_first_page_text': independent, 'independent_file_sha256': file_hash(independent_path),
        'source_pdf_sha256_checked': file_hash(source),
        'inspection': 'Actually read first-page independent text and five native lines/coordinates/fonts; no JPEG inspection added in this context.',
        'scope': 'Prose ownership of one native line, not literal whole-page/section fidelity.',
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(paths['evidence'], evidence)
    findings = {'schema': 'bounded-source-prose-ownership-findings-v1', **meta,
        'reviewer': 'Codex root;2026-10-31;dual text extractors and exact native line geometry actually read',
        'checked_pages': [1],
        'finding': 'The Table9 token continues the previous prose sentence, followed on the same regularly spaced native line by an Apriori-method sentence which continues on the next line. The complete five-line paragraph occurs once in the independent first-page text. Classifying the middle line as a caption removes real author prose from both reader views.',
        'line_to_restore': missing['source_line_ids'], 'block_id': missing['block_id'],
        'evidence_sha256': file_hash(paths['evidence']), 'no_text_characters_changed': True,
        'remaining_uncertainties': ['Same-page paragraph seams around b000013/b000014/b000015 remain pending.',
            'Form/title/other source defects and all chapter boundaries are not waived by this single-line repair.'],
        'section_source_fidelity_approved': False, 'whole_paper_source_acceptance': False,
        'ai_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(paths['findings'], findings)
    sha = digest(missing['text'].encode('utf-8'))
    repair = {**meta, 'reviewer': findings['reviewer'], 'checked_pages': [1],
        'reason': 'Recover one intact author-prose line excluded by a false caption classification; preserve all source bytes and other flags.',
        'operations': [{'operation': 'classify', 'block_id': missing['block_id'],
            'from_kind': 'caption', 'to_kind': 'prose', 'before_text_sha256': sha, 'after_text_sha256': sha,
            'reason': 'Exact regular native paragraph geometry and independent paragraph text show an inline table reference and method sentence, not a caption.'}],
        'evidence': [{'path': str(paths[name]), 'sha256': file_hash(paths[name]),
                      'description': description} for name, description in (
            ('evidence', 'Source-bound first-page independent text and exact five native lines/geometry.'),
            ('findings', 'Actually read single-line prose/caption ownership and retained limitations.'))],
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(paths['repair'], repair)
    candidate = copy.deepcopy(old)
    apply_text_repairs(candidate, [repair])
    repaired = next(x for x in candidate['blocks'] if x['block_id'] == missing['block_id'])
    if replay_block(candidate, repaired, members[2]['text'].strip()) != missing['text']:
        raise ValueError('Exact raw-line replay differs')
    if candidate['defects'] != old['defects'] or any(
            {k: v for k, v in left.items() if k not in {'kind', 'pre_repair_kind', 'text_repair_review_ids'}} !=
            {k: v for k, v in right.items() if k not in {'kind', 'pre_repair_kind', 'text_repair_review_ids'}}
            for left, right in zip(old['blocks'], candidate['blocks'])):
        raise ValueError('Block text/source metadata or existing defects changed')
    if [(x['block_id'], x['kind']) for x in candidate['blocks'] if x['kind'] != blocks[x['block_id']]['kind']] != [('b000014', 'prose')]:
        raise ValueError('Unrelated kind changed')
    raw_ids = Counter(x['line_id'] for p in pages for x in p['lines'])
    used = Counter(lid for item in candidate['blocks'] for lid in item['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if raw_ids != used or any(n != 1 for n in used.values()):
        raise ValueError('Source-line accounting lost or duplicated')
    from corpus_queries import select_sections
    from text_corpus import section_blocks
    ids, excluded = select_sections(candidate, 'abstract')
    after, _ = text_with_block_spans(section_blocks(candidate, ids, excluded_roles=excluded))
    seam = a['text'] + '\n\n' + b['text']
    replacement = a['text'] + '\n\n' + missing['text'] + '\n\n' + b['text']
    if before.count(seam) != 1 or after != before.replace(seam, replacement):
        raise ValueError('Abstract changed beyond the one recovered intact line')
    old_author, _ = text_with_block_spans(all_author_blocks(old))
    new_author, _ = text_with_block_spans(all_author_blocks(candidate))
    if old_author.count(seam) != 1 or new_author != old_author.replace(seam, replacement):
        raise ValueError('Author view changed beyond the one recovered line')
    prepare_review_bundles([paths['repair']], identity_fields=('paper_id',), application_status='preflight only')
    result = {'paper_id': pid, 'parent_dataset_id': catalog.identity,
        'proof_sha256': file_hash(paths['repair']), 'source_lines_accounted_once': True,
        'literal_block_bytes_unchanged': True, 'other_kinds_and_defects_unchanged': True,
        'restored_block_id': missing['block_id'], 'restored_prose_characters': len(missing['text']),
        'reader_characters_before': len(before), 'reader_characters_after': len(after),
        'same_page_paragraph_continuity': 'pending; two seams remain visible',
        'section_source_fidelity_approved': False, 'whole_paper_source_acceptance': False,
        'ai_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(paths['preflight'], result)
    write_new(preview_path, '<!-- Bounded repaired preview; same-page seams/source acceptance remain pending. -->\n' + after + '\n')
    print(result, flush=True)


if __name__ == '__main__':
    main()
