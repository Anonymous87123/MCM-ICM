"""Create-only successor to v12; v13 stays preserved as a rejected regression."""
from pathlib import Path
import os
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import digest,encoded,file_hash,json_new,read_json
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1];os.chdir(work);base=work/'artifacts/text-corpus'
    parent=base/'reflow-20261030-v12';output=base/'reflow-20261030-v14'
    request=base/'build-request-reflow-20261030-v14.json'
    report_path=base/'integrity-reflow-20261030-v14.json'
    if any(p.exists() for p in (output,request,report_path)):
        raise ValueError('Create-only build state exists; inspect, never overwrite or restart')
    audit_path=base/'span-origin-flow-full-20261030-v6.json';audit=read_json(audit_path)
    catalog=Catalog(parent);scope=read_json(parent/'scope.json');totals=audit['totals']
    if (audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            totals['papers']!=435 or totals['pages']!=11552 or totals['source_lines']!=954866 or
            totals['contents_pages_before']!=345 or totals['contents_pages_after']<345):
        raise ValueError('Whole-scope source ownership/review/Contents-preservation audit has not passed')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:raise ValueError('Audited implementation changed: '+name)
    for name,sha in audit['review_input_sha256'].items():
        if file_hash(Path(name))!=sha:raise ValueError('Audited review changed: '+name)
    native=base/'native-20261029-v1'
    if Catalog(native).identity!=scope['parent_dataset_id']:raise ValueError('Original native generation required')
    fields=('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
            'absence_review_sha256','layout_review_sha256');inputs={}
    for field in fields:
        inputs[field]=[]
        for name,sha in scope[field].items():
            path=Path(name)
            if file_hash(path)!=sha:raise ValueError('Existing frozen input changed: '+name)
            inputs[field].append(path)
    reviews=base/'reviews/20261030';pid='P-A-2010-6749-395f556a'
    body=reviews/'q001-pages25-31-text-lanes-v1.json'
    merged_path=reviews/'q001-merged-text-lanes-v2.json';merged=read_json(merged_path)
    previous_layouts=[p for p in inputs['layout_review_sha256'] if read_json(p)['paper_id']==pid]
    if len(previous_layouts)!=1:raise ValueError('Expected one previous q1 layout bundle')
    parts=[previous_layouts[0],body]
    if merged['merged_inputs']!={str(p):file_hash(p) for p in parts}:raise ValueError('Merge source bindings differ')
    originals=[read_json(p) for p in parts]
    if (merged['pages']!=sorted([p for r in originals for p in r['pages']],key=lambda p:p['page']) or
            merged['evidence']!=[p for r in originals for p in r['evidence']]):
        raise ValueError('Lossless proof merge changed checked groups/evidence')
    inputs['layout_review_sha256'][inputs['layout_review_sha256'].index(previous_layouts[0])]=merged_path
    replacement=reviews/'q001-page5-prose-transcription-v14-binding-v1.json'
    previous=catalog.document(pid)['text_repair_reviews']
    if (len(previous)!=1 or read_json(replacement)['binding_transfer']['previous_review_sha256']!=
            digest(encoded(previous[0]))):raise ValueError('Literal proof transfer does not bind v12')
    repairs=[p for p in inputs['text_repair_sha256'] if read_json(p)['paper_id']==pid]
    if len(repairs)!=1:raise ValueError('Expected one old q1 literal proof')
    inputs['text_repair_sha256'][inputs['text_repair_sha256'].index(repairs[0])]=replacement
    inputs['absence_review_sha256'].append(reviews/'q094-abstract-absence-v1.json')
    metrics=base/'span-metrics-20261030-v1'
    bindings={field:{str(p):file_hash(p) for p in paths} for field,paths in inputs.items()}
    json_new(request,{'native_dataset_id':Catalog(native).identity,'previous_candidate_dataset_id':catalog.identity,
        'rejected_generation':'reflow-20261030-v13','prospective_report_sha256':file_hash(audit_path),
        'driver_sha256':file_hash(Path(__file__)),
        'stage_driver_sha256':file_hash(Path(__file__).with_name('stage_text_corpus_v14_binding.py')),
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),'inputs':bindings,
        'prospective_layout_representation':'Existing q1 pages6/7/17 plus disjoint pages25/31; exact lossless merge verified.',
        'new_source_acceptance':False,'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],metrics)
    print(index(output),flush=True);result=validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0)!=totals['contents_pages_after']:
        raise ValueError('Built Contents census differs from the prospective audit; preserve failed candidate')
    for mapping in bindings.values():
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):raise ValueError('Review/OCR input changed during build')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:raise ValueError('Audited implementation changed during build')
    json_new(report_path,result);print(result,flush=True)
    if not result['structural_integrity_pass']:raise ValueError('Preserve failed candidate; no promotion')


if __name__=='__main__':main()
