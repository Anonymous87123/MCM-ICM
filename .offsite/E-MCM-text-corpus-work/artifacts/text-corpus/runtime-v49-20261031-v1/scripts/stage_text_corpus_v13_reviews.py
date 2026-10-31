"""Freeze already checked prose repairs and q94's complete local absence census.

Create-only. Merging old layout proofs changes packaging, not their checked groups.
No formula/chart semantics or new whole-paper approval is inferred.
"""
from pathlib import Path
import copy

from corpus_reader import Catalog
from rebind_literal_review import rebind
from source_absence_reviews import prepare_absence_reviews,prepare_review_bundles
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest,encoded,file_hash,json_new,make_document,read_json,rows


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    root=base/'reflow-20261030-v12';catalog=Catalog(root);reviews=base/'reviews/20261030'
    outputs=[reviews/n for n in ('q001-merged-text-lanes-v2.json',
        'q001-page5-prose-transcription-v13-binding-v1.json','q094-abstract-absence-v1.json')]
    if any(p.exists() for p in outputs):
        raise ValueError('Create-only staged review exists; inspect, do not overwrite')
    old=catalog.document('P-A-2010-6749-395f556a')
    paths=[reviews/'q001-pages6-7-17-text-lanes-v1.json',reviews/'q001-pages25-31-text-lanes-v1.json']
    parts=[read_json(p) for p in paths];merged=copy.deepcopy(parts[0])
    for key in ('paper_id','source_sha256','raw_pages_sha256'):
        if any(r[key]!=old[key] for r in parts):raise ValueError('Merged source identities differ')
    merged['pages']=sorted([p for r in parts for p in r['pages']],key=lambda p:p['page'])
    if len({p['page'] for p in merged['pages']})!=len(merged['pages']):
        raise ValueError('Overlapping source layout reviews')
    merged['evidence']=[p for r in parts for p in r['evidence']]
    merged['evidence_files']={str(Path(r['evidence'][0]['bundle_root'])/n):sha
        for r in parts for n,sha in r['evidence_files'].items()}
    merged['remaining_uncertainties']=[v for r in parts for v in r['remaining_uncertainties']]
    merged['reviewer']='Codex root;2026-10-30;lossless merge of two existing checked prose-layout proofs'
    merged['reason']='Preserve every checked group on physical pages6,7,17,25,31; do not infer new source acceptance.'
    merged['application_status']='Staged new generation only; immutable parents preserved.'
    merged['merged_inputs']={str(p):file_hash(p) for p in paths}
    pages=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl')
    working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(old,working,[merged])
    keys=('paper_id','problem_type','year','queue_position','page_count','source_relative_path',
          'source_sha256','raw_pages_sha256')
    candidate=make_document({k:old[k] for k in keys},working,improved=True)
    candidate['layout_reviews']=applied;validate_layout_reviews(candidate,pages)
    original=old['text_repair_reviews']
    if len(original)!=1:raise ValueError('Expected the one existing q1 literal proof')
    repair=rebind(old,candidate,original[0])
    for proof in repair['evidence']:
        path=root/proof['path']
        if file_hash(path)!=proof['sha256']:raise ValueError('Literal evidence changed')
        proof['path']=str(path)
    repair['binding_transfer']['tool_sha256']=file_hash(Path(__file__).with_name('rebind_literal_review.py'))
    q94=catalog.document('P-B-2012-13074-8fc549d2')
    census_path=reviews/'q094-full-native-prose-census-v1.json';census=read_json(census_path)
    if (census['source_sha256']!=q94['source_sha256'] or census['raw_pages_sha256']!=q94['raw_pages_sha256'] or
            [p['page'] for p in census['pages']]!=list(range(1,23))):
        raise ValueError('Full22-page manual census source/coverage differs')
    folder=base/'source-reviews/q094-whole-source-20261030-v1';manifest=read_json(folder/'manifest.json')
    if (manifest['source_sha256']!=q94['source_sha256'] or manifest['raw_pages_sha256']!=q94['raw_pages_sha256'] or
            [p['physical_page'] for p in manifest['files'] if p.get('physical_page')]!=list(range(1,23))):
        raise ValueError('Q94 complete page-image evidence differs')
    source=Path(read_json(root/'scope.json')['source_root'])
    copies=[p for p in source.rglob('*13074*') if p.is_file()]
    if len(copies)!=1 or file_hash(copies[0])!=q94['source_sha256']:
        raise ValueError('Local alternative-source inventory differs; inspect before absence claim')
    absence={'schema':'source-absence-review-v1',**{k:q94[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'role':'abstract','reviewer':census['reviewer'],'page_count':22,'checked_pages':list(range(1,23)),
        'reason':census['whole_source_abstract_finding']+' The separately printed Conclusions and management Letter are not relabelled as Abstract. This is only source-local absence, not external archive completeness or whole-paper fidelity.',
        'full_native_prose_read':True,'physical_page_heading_layout_checked':True,
        'independent_text_check':{'path':f"papers/{q94['paper_id']}/raw/pdftotext.bin",
            'sha256':file_hash(root/'papers'/q94['paper_id']/'raw/pdftotext.bin'),
            'status':'Independent extraction retained; no full-page equality or formula certification.'},
        'alternative_copy_check':{'manifest_sha256':file_hash(work/'artifacts/corpus/manifest.jsonl'),
            'matching_file_count':1,'result':'All604 frozen records and source-root filename inventory checked; only this22-page source found.'},
        'evidence':[{'path':str(folder/'manifest.json'),'bundle_root':str(folder),
            'sha256':file_hash(folder/'manifest.json'),'description':'All22 native pages and source images retained; eight bounded JPEGs actually checked for prose/heading layout only.'},
            {'path':str(census_path),'sha256':file_hash(census_path),'description':'Actual per-page prose/heading census and unresolved limitations.'}],
        'application_status':'Staged for new generation; no immutable parent or learning history changed.',
        'formula_verification':'paused','figure_distillation':'paused'}
    for path,value in zip(outputs,(merged,repair,absence)):json_new(path,value)
    prepared,copies=prepare_review_bundles([outputs[0]],identity_fields=('paper_id',),application_status='prospective')
    absent,absence_copies=prepare_absence_reviews([outputs[2]])
    from source_absence_reviews import apply_absence_reviews
    apply_absence_reviews(copy.deepcopy(q94),absent)
    print({'q1_layout_pages':[p['page'] for p in merged['pages']],
        'q1_retained_groups':sum(len(p['groups']) for p in merged['pages']),
        'q1_transferred_literal_operations':len(repair['operations']),
        'portable_layout_files':len(copies),'q94_portable_absence_files':len(absence_copies),
        'new_whole_paper_source_acceptance':False})


if __name__=='__main__':main()
