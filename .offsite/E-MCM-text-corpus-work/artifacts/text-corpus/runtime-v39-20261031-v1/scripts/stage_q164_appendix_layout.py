"""Freeze actual pages10/11: bibliography and a bottom-labelled appendix sheet."""
from pathlib import Path

from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest, file_hash, json_new, make_document, rows


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261030-v14'
    output = base / 'reviews/20261030/q164-pages10-11-appendix-layout-v1.json'
    if output.exists():
        raise ValueError('Create-only proof exists; preserve it')
    doc = Catalog(root).document('P-C-2010-8088-e7ab6731')
    pages = rows(root / 'papers' / doc['paper_id'] / 'raw/pages.jsonl')
    selected = []

    def add(number, definitions):
        active = [x for x in pages[number-1]['lines'] if x['text'].strip() and not x.get('superseded_by_ocr')]
        groups = []
        for name, kind, predicate, opening in definitions:
            members = [x for x in active if predicate(x)]
            groups.append({'group_id': name, 'kind': kind,
                'source_line_ids': [x['line_id'] for x in members],
                'text_sha256': digest(' '.join(x['text'].strip() for x in members).encode()),
                'reason': 'Actual pages10/11 source proxy checked; retain all literals and object-before-bottom-label order.',
                **({'opens_section': opening} if opening else {})})
        selected.append({'page': number, 'groups': groups})

    add(10, [
        ('p10-header', 'furniture', lambda x: x['native_block'] == 0, None),
        ('p10-author-continuation', 'prose', lambda x: x['native_block'] == 1, None),
        ('p10-references-heading', 'heading', lambda x: x['native_block'] == 3, {'role':'references','level':1}),
        ('p10-bibliography', 'source_object', lambda x: x['native_block'] == 4, None)])
    add(11, [
        ('p11-header', 'furniture', lambda x: x['native_block'] == 0, None),
        ('p11-appendix-sheet', 'source_object', lambda x: x['native_block'] not in (0,1),
         {'role':'appendix','level':1,'trailing_label_group_id':'p11-printed-appendix-label'}),
        ('p11-printed-appendix-label', 'caption', lambda x: x['native_block'] == 1, None)])
    folder = base / 'source-reviews/q164-whole-source-20261030-v1'
    findings = base / 'reviews/20261030/q164-pages10-11-layout-findings-v1.json'
    review = {'schema':'source-text-layout-review-v1',
        **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root;2026-10-30;overview03 pages10/11 actually inspected',
        'reason':'Separate bibliography and the following bottom-labelled spreadsheet appendix without moving its printed label or interpreting table/formula values.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':selected,
        'evidence':[
            {'path':str(folder/'manifest.json'),'bundle_root':str(folder),'sha256':file_hash(folder/'manifest.json'),
             'description':'Frozen11-page bundle; this proof actually checks ONLY overview03/pages10/11.'},
            {'path':str(findings),'sha256':file_hash(findings),'description':'Actual bounded source findings and remaining limitations.'}],
        'evidence_files':{str(p):file_hash(p) for p in folder.iterdir() if p.is_file()},
        'remaining_uncertainties':['No other source page, full-section fidelity or whole-paper acceptance approved.'],
        'application_status':'Staged for a new immutable generation; v14 untouched.',
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_ = prepare_flow_pages(doc,pages,base/'span-metrics-20261030-v1')
    applied = apply_layout_reviews(doc,working,[review])
    candidate = make_document({k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
    candidate['layout_reviews'] = applied
    validate_layout_reviews(candidate,pages)
    appendix = next(s for s in candidate['sections'] if s['origin']=='reviewed-trailing-appendix-label')
    owned = [b for b in candidate['blocks'] if b['section_id']==appendix['section_id']]
    if [b['kind'] for b in owned] != ['source_object','caption']:
        raise ValueError('Appendix ownership changed or default prose polluted')
    json_new(output,review)
    _,copies = prepare_review_bundles([output],identity_fields=('paper_id',),application_status='preflight only')
    print({'source_checked_pages':[10,11],'groups':7,'portable_evidence_files':len(copies),
           'appendix_label_kept_after_object':True,'whole_paper_acceptance':False})


if __name__ == '__main__':
    main()
