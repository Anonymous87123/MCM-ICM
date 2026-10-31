"""Create v11 from frozen native evidence, preserving all prior generations."""
from pathlib import Path
import os
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash,json_new,read_json
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1]
    os.chdir(work)
    base=work/'artifacts/text-corpus'
    parent=base/'reflow-20261030-v10'
    output=base/'reflow-20261030-v11'
    report_path=base/'integrity-reflow-20261030-v11.json'
    if output.exists() or report_path.exists():
        raise ValueError('Create-only generation or report already exists; inspect existing process/state')
    scope=read_json(parent/'scope.json')
    prospective=read_json(base/'prospective-reflow-20261030-v11d.json')
    if prospective['errors'] or prospective['parent_dataset_id']!=Catalog(parent).identity:
        raise ValueError('Whole-scope prospective audit failed or belongs to another parent')
    for name,sha in prospective['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Prospective implementation changed: '+name)
    native=base/'native-20261029-v1'
    if Catalog(native).identity!=scope['parent_dataset_id']:
        raise ValueError('Original native generation differs')
    inputs={}
    for field in ('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
                  'absence_review_sha256','layout_review_sha256'):
        inputs[field]=[]
        for name,sha in scope[field].items():
            path=Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Frozen input changed: '+name)
            inputs[field].append(path)
    review=base/'reviews/20261030'
    inputs['source_review_sha256'].append(review/'q010-abstract-v1.json')
    inputs['text_repair_sha256'].append(review/'q001-page5-prose-transcription-v1.json')
    inputs['absence_review_sha256'].append(review/'q167-abstract-absence-v1.json')
    json_new(base/'build-request-reflow-20261030-v11.json',{
        'native_dataset_id':Catalog(native).identity,'previous_candidate_dataset_id':Catalog(parent).identity,
        'prospective_report_sha256':file_hash(base/'prospective-reflow-20261030-v11d.json'),
        'driver_sha256':file_hash(Path(__file__)),
        'inputs':{k:{str(p):file_hash(p) for p in paths} for k,paths in inputs.items()},
        'source_acceptance':False,'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
              inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'])
    print(index(output),flush=True)
    result=validate(output,work,True)
    json_new(report_path,result)
    print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Derived corpus integrity failed; preserve generation for diagnosis')


if __name__=='__main__':
    main()
