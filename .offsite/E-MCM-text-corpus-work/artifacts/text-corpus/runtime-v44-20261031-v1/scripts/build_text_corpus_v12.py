"""Batch the frozen baseline/lane/absence repairs into a NEW preview generation."""
from pathlib import Path
import os
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import digest,encoded,file_hash,json_new,read_json
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1];os.chdir(work)
    base=work/'artifacts/text-corpus';parent=base/'reflow-20261030-v11'
    output=base/'reflow-20261030-v12';report_path=base/'integrity-reflow-20261030-v12.json'
    request=base/'build-request-reflow-20261030-v12.json'
    if output.exists() or report_path.exists() or request.exists():
        raise ValueError('Create-only build already has state; inspect it, do not restart/overwrite')
    audit_path=base/'span-origin-flow-full-20261030-v4.json';prospective=read_json(audit_path)
    cat=Catalog(parent);scope=read_json(parent/'scope.json')
    if (prospective['parent_dataset_id']!=cat.identity or prospective['errors'] or
            prospective['review_replay_conflicts'] or prospective['totals']['papers']!=435 or
            prospective['totals']['pages']!=11552 or prospective['totals']['source_lines']!=954866):
        raise ValueError('Full-scope prospective flow/review audit has not passed')
    for name,sha in prospective['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Audited implementation changed: '+name)
    for name,sha in prospective['review_input_sha256'].items():
        if file_hash(Path(name))!=sha:
            raise ValueError('Audited explicit review changed: '+name)
    native=base/'native-20261029-v1'
    if Catalog(native).identity!=scope['parent_dataset_id']:
        raise ValueError('Original native generation identity differs')
    inputs={}
    for field in ('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
                  'absence_review_sha256','layout_review_sha256'):
        inputs[field]=[]
        for name,sha in scope[field].items():
            p=Path(name)
            if file_hash(p)!=sha:
                raise ValueError('Frozen input changed: '+name)
            inputs[field].append(p)
    review=base/'reviews/20261030'
    old_review=cat.document('P-A-2010-6749-395f556a')['text_repair_reviews']
    replacement=review/'q001-page5-prose-transcription-span-origin-v1.json'
    if (len(old_review)!=1 or read_json(replacement)['binding_transfer']['previous_review_sha256']!=
            digest(encoded(old_review[0]))):
        raise ValueError('Literal transfer does not bind the immutable previous review')
    matches=[p for p in inputs['text_repair_sha256'] if read_json(p)['paper_id']=='P-A-2010-6749-395f556a']
    if len(matches)!=1:
        raise ValueError('Expected exactly one previous page5 literal proof')
    inputs['text_repair_sha256'][inputs['text_repair_sha256'].index(matches[0])]=replacement
    inputs['layout_review_sha256'].append(review/'q001-pages6-7-17-text-lanes-v1.json')
    inputs['absence_review_sha256'].append(review/'q005-abstract-absence-v1.json')
    metrics=base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':Catalog(native).identity,'previous_candidate_dataset_id':cat.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'inputs':{k:{str(p):file_hash(p) for p in paths} for k,paths in inputs.items()},
        'source_acceptance':False,'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
              inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],metrics)
    print(index(output),flush=True)
    result=validate(output,work,True);json_new(report_path,result)
    print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Preserve failed candidate for diagnosis; no promotion')


if __name__=='__main__':
    main()
