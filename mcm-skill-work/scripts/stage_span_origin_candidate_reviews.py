"""Create an exact-ID transfer of the already checked page5 transcription."""
from pathlib import Path
from corpus_reader import Catalog
from rebind_literal_review import rebind
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import file_hash,json_new,make_document,read_json,rows


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    root=base/'reflow-20261030-v11';catalog=Catalog(root)
    old=catalog.document('P-A-2010-6749-395f556a')
    raw=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl')
    working,_=prepare_flow_pages(old,raw,base/'span-metrics-20261030-v1')
    new_layout=read_json(base/'reviews/20261030/q001-pages6-7-17-text-lanes-v1.json')
    apply_layout_reviews(old,working,old.get('layout_reviews',[])+[new_layout])
    meta={k:old[k] for k in ('paper_id','problem_type','year','queue_position','page_count',
                            'source_relative_path','source_sha256','raw_pages_sha256')}
    candidate=make_document(meta,working,improved=True)
    original=old['text_repair_reviews']
    if len(original)!=1 or original[0]['checked_pages']!=[5]:
        raise ValueError('Expected only the existing bounded page5 transcription')
    review=rebind(old,candidate,original[0])
    # Reuse the immutable parent's source evidence, preserving its bytes/hash.
    for proof in review['evidence']:
        path=root/proof['path']
        if file_hash(path)!=proof['sha256']:
            raise ValueError('Original source evidence changed')
        proof['path']=str(path)
    review['binding_transfer']['tool_sha256']=file_hash(Path(__file__).with_name('rebind_literal_review.py'))
    output=base/'reviews/20261030/q001-page5-prose-transcription-span-origin-v1.json'
    json_new(output,review)
    # Check the independently staged absence/layout bundles before a full audit.
    _,copies=prepare_review_bundles([base/'reviews/20261030/q005-abstract-absence-v1.json'],
                                  identity_fields=('paper_id','role'),application_status='prospective only')
    print({'literal_operation_ids_transferred':len(review['operations']),
           'new_source_review':False,'q005_preflight_files':len(copies),'output':str(output)})


if __name__=='__main__':
    main()
