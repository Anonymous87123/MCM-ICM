"""Inventory every title-classified opening-summary block, without changing it."""
import argparse
from pathlib import Path
from corpus_reader import Catalog
from corpus_queries import select_sections
from text_corpus import file_hash, json_new


def audit(root, report):
    if report.exists():
        raise ValueError('Create-only title ownership inventory exists')
    catalog=Catalog(root);before=file_hash(root/'catalog.json');findings=[]
    for paper in catalog.papers:
        doc=catalog.document(paper['paper_id']);ids,_=select_sections(doc,'abstract')
        selected=set(ids)
        for section in doc['sections']:
            if section['parent_id'] in selected:
                selected.add(section['section_id'])
        prior=[]
        for position,block in enumerate(doc['blocks']):
            if block['section_id'] not in selected:
                continue
            if block['kind']=='title':
                after=next((b for b in doc['blocks'][position+1:] if
                    b['section_id'] in selected and b['kind'] in {'prose','list','mixed','author_callout'}),None)
                findings.append({'paper_id':paper['paper_id'],'queue_position':paper['queue_position'],
                    'document_sha256':paper['document_sha256'],'block_id':block['block_id'],
                    'source_line_ids':block['source_line_ids'],'source_pages':block['source_pages'],
                    'text':block['text'],'author_candidate_blocks_before':len(prior),
                    'previous_author_tail':prior[-1]['text'][-160:] if prior else None,
                    'next_author_start':after['text'][:160] if after else None,
                    'status':'Source ownership unreviewed. This includes real paper titles and possible misclassified prose; no automatic reclassification.'})
            if block['kind'] in {'prose','list','mixed','author_callout'}:
                prior.append(block)
    if file_hash(root/'catalog.json')!=before:
        raise ValueError('Corpus changed during inventory')
    result={'dataset_id':catalog.identity,'papers_checked':len(catalog.papers),
        'title_blocks':len(findings),'papers_with_title_blocks':len({x['paper_id'] for x in findings}),
        'findings':findings,'source_fidelity_approved':False,'ai_receipts_created':0,
        'meaning':'Complete inventory of title blocks owned by candidate abstract sections. Not a count of proven missing paragraphs.'}
    json_new(report,result);print({k:v for k,v in result.items() if k!='findings'},flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--corpus-root',type=Path,required=True);p.add_argument('--report',type=Path,required=True)
    a=p.parse_args();audit(a.corpus_root.resolve(),a.report.resolve())
