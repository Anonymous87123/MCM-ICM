"""Transfer unchanged q1 page5 source proof after the TOC regression correction."""
from pathlib import Path
from corpus_reader import Catalog
from rebind_literal_review import rebind
from source_layout_reviews import apply_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import file_hash,json_new,make_document,read_json,rows


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    root=base/'reflow-20261030-v12';catalog=Catalog(root);pid='P-A-2010-6749-395f556a'
    old=catalog.document(pid);raw=rows(root/'papers'/pid/'raw/pages.jsonl')
    working,_=prepare_flow_pages(old,raw,base/'span-metrics-20261030-v1')
    merged=read_json(base/'reviews/20261030/q001-merged-text-lanes-v2.json')
    apply_layout_reviews(old,working,[merged])
    keys=('paper_id','problem_type','year','queue_position','page_count','source_relative_path',
          'source_sha256','raw_pages_sha256')
    candidate=make_document({k:old[k] for k in keys},working,improved=True)
    previous=old['text_repair_reviews']
    if len(previous)!=1:raise ValueError('Expected one existing bounded literal source proof')
    review=rebind(old,candidate,previous[0])
    for proof in review['evidence']:
        path=root/proof['path']
        if file_hash(path)!=proof['sha256']:raise ValueError('Source proof changed')
        proof['path']=str(path)
    review['binding_transfer']['tool_sha256']=file_hash(Path(__file__).with_name('rebind_literal_review.py'))
    output=base/'reviews/20261030/q001-page5-prose-transcription-v14-binding-v1.json'
    json_new(output,review)
    print({'transferred_literal_operations':len(review['operations']),'new_source_review':False,'output':str(output)})


if __name__=='__main__':main()
