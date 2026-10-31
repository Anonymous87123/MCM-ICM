"""Freeze actually checked q333 opening lanes and decimal chapter boundaries."""
from pathlib import Path

from corpus_queries import select_sections
from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest, file_hash, json_new, make_document, rows, section_blocks


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261030-v16'
    output = base / 'reviews/20261030/q333-opening-layout-v1.json'
    report = base / 'reviews/20261030/q333-opening-layout-preflight-v1.json'
    if output.exists() or report.exists():
        raise ValueError('Create-only proof/report already exists; preserve it')
    doc = Catalog(root).document('P-E-2017-61502-f0a50d47')
    pages = rows(root / 'papers' / doc['paper_id'] / 'raw/pages.jsonl')
    selected = []

    def add(number, definitions):
        active = [x for x in pages[number-1]['lines']
                  if x['text'].strip() and not x.get('superseded_by_ocr')]
        groups = []
        for name, kind, predicate, opening in definitions:
            members = [x for x in active if predicate(x)]
            if not members:
                raise ValueError('Empty source-bound group: ' + name)
            groups.append({'group_id': name, 'kind': kind,
                'source_line_ids': [x['line_id'] for x in members],
                'text_sha256': digest(' '.join(x['text'].strip() for x in members).encode()),
                'reason': 'Actually checked opening page; preserve author wording and separate source objects without interpreting them.',
                **({'opens_section': opening} if opening else {})})
        selected.append({'page': number, 'groups': groups})

    add(1, [
        ('p1-form', 'front_matter', lambda x: x['native_block'] in (1,2,3,4,6), None),
        ('p1-title', 'title', lambda x: x['native_block'] == 8, None),
        *[(f'p1-paragraph-{n-9}', 'prose', lambda x,n=n: x['native_block'] == n, None)
          for n in range(10,14)],
        ('p1-assumptions-lead', 'prose', lambda x: x['native_block'] == 14 and
         x['line_id'] in ('p0001-n0014-l0000','p0001-n0014-l0001'), None),
        ('p1-assumption-1', 'list', lambda x: x['native_block'] == 14 and
         x['line_id'] in [f'p0001-n0014-l{n:04d}' for n in range(2,6)], None),
        ('p1-assumption-2', 'list', lambda x: x['native_block'] == 14 and
         x['line_id'] in [f'p0001-n0014-l{n:04d}' for n in range(6,10)], None),
        ('p1-assumption-3', 'list', lambda x: x['native_block'] == 14 and
         x['line_id'] in [f'p0001-n0014-l{n:04d}' for n in range(10,13)], None),
        ('p1-upper-caption', 'caption', lambda x: x['native_block'] == 15, None),
        ('p1-right-object-labels', 'source_object', lambda x: x['native_block'] >= 17, None),
        ('p1-lower-caption', 'caption', lambda x: x['native_block'] == 16, None)])
    add(2, [
        ('p2-header', 'furniture', lambda x: x['native_block'] == 0, None),
        ('p2-introduction', 'heading', lambda x: x['line_id']=='p0002-n0001-l0000',
         {'role':'introduction','level':1}),
        ('p2-introduction-prose', 'prose', lambda x: x['native_block']==1 and
         x['line_id']!='p0002-n0001-l0000', None),
        ('p2-principles-heading', 'heading', lambda x: x['line_id']=='p0002-n0002-l0001',
         {'role':'other','level':2}),
        ('p2-principles-lead', 'prose', lambda x: x['native_block']==2 and
         x['line_id']!='p0002-n0002-l0001', None),
        ('p2-cited-principles', 'source_object', lambda x: x['native_block']==3, None),
        ('p2-author-grouping', 'prose', lambda x: x['native_block']==4, None),
        ('p2-objective', 'heading', lambda x: x['line_id']=='p0002-n0005-l0000',
         {'role':'other','level':2}),
        ('p2-objective-prose', 'prose', lambda x: x['native_block']==5 and
         x['line_id']!='p0002-n0005-l0000', None)])
    add(3, [
        ('p3-header', 'furniture', lambda x: x['native_block']==0, None),
        ('p3-methodology', 'heading', lambda x: x['line_id']=='p0003-n0001-l0000',
         {'role':'other','level':1}),
        ('p3-methodology-prose', 'prose', lambda x: x['native_block']==1 and
         x['line_id']!='p0003-n0001-l0000', None),
        ('p3-caption', 'caption', lambda x: x['native_block'] in (3,4,5), None),
        ('p3-scale-prose', 'prose', lambda x: x['native_block']==6, None),
        ('p3-displayed-object', 'source_object', lambda x: x['native_block']==7 or
         x['line_id']=='p0003-n0008-l0000', None),
        ('p3-weighting-prose', 'prose', lambda x: x['native_block']==8 and
         x['line_id']!='p0003-n0008-l0000', None)])
    folder = base / 'source-reviews/q333-opening-20261030-v1'
    findings = base / 'reviews/20261030/q333-opening-layout-findings-v1.json'
    review = {'schema':'source-text-layout-review-v1',
        **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root; 2026-10-30; individual pages1,2,3 JPEGs actually inspected',
        'reason':'Restore untitled summary left-column prose and printed 1.0/1.1/2.0 hierarchy; retain all form, object and caption text separately.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':selected,
        'evidence':[
            {'path':str(folder/'manifest.json'),'bundle_root':str(folder),
             'sha256':file_hash(folder/'manifest.json'),'description':'All three bounded source page proxies actually checked.'},
            {'path':str(findings),'sha256':file_hash(findings),
             'description':'Actual page boundaries, lane observations and explicit limits.'}],
        'evidence_files':{str(p):file_hash(p) for p in folder.iterdir() if p.is_file()},
        'remaining_uncertainties':['Only pages1-3 checked; later heading conventions and whole-paper prose remain pending.'],
        'application_status':'Staged for a new immutable generation; v16 and all reading receipts untouched.',
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_ = prepare_flow_pages(doc,pages,base/'span-metrics-20261030-v1')
    applied = apply_layout_reviews(doc,working,[review])
    candidate = make_document({k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
    candidate['layout_reviews'] = applied
    validate_layout_reviews(candidate,pages)
    ids,excluded = select_sections(candidate,'abstract')
    abstract = section_blocks(candidate,ids,excluded_roles=excluded)
    if {p for b in abstract for p in b['source_pages']} != {1}:
        raise ValueError('Abstract still inherits body text')
    if [b['kind'] for b in abstract] != ['prose']*5+['list']*3:
        raise ValueError('Opening prose/bullet classification differs')
    intro = next(s for s in candidate['sections'] if s['title']=='1.0 Introduction')
    objective = next(s for s in candidate['sections'] if s['title']=='1.1 Objective')
    method = next(s for s in candidate['sections'] if s['title']=='2.0 Methodology')
    if intro['parent_id'] is not None or objective['parent_id']!=intro['section_id'] or method['parent_id'] is not None:
        raise ValueError('Checked decimal chapter hierarchy differs')
    json_new(output,review)
    _,copies = prepare_review_bundles([output],identity_fields=('paper_id',),application_status='preflight only')
    json_new(report,{'paper_id':doc['paper_id'],'parent_dataset_id':Catalog(root).identity,
        'review_sha256':file_hash(output),'checked_pages':[1,2,3],
        'layout_groups':sum(len(x['groups']) for x in selected),
        'portable_evidence_files':len(copies),'abstract_pages':[1],
        'abstract_blocks':len(abstract),'abstract_characters':len('\n\n'.join(b['text'] for b in abstract)),
        'checked_hierarchy_pass':True,'raw_line_accounting_pass':True,
        'source_fidelity_approved':False,'ai_reading_receipts_created':0})
    print(report.read_text(encoding='utf-8'))


if __name__ == '__main__':
    main()
