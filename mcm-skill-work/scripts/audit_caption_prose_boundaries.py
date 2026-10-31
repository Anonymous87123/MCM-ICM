"""Find source sentences potentially hidden by Figure/Table caption classification.

All papers/blocks are inspected. This is a source-review queue, never a classifier
override: genuine captions can contain these words and need page evidence too.
"""
import argparse
from collections import Counter
from pathlib import Path
import re
from corpus_reader import Catalog
from text_corpus import digest,file_hash,json_new


def suspicious_reference(text):
    return bool(re.match(r'^(?:Figure|Fig\.|Table)\s*\d+\s+(?:also\s+)?'
                         r'(?:is|are|was|were|tells?|shows?|which|can|illustrates?|demonstrates?|indicates?|suggests?)\b',text,re.I))


def audit(root):
    c=Catalog(root);records=[];totals=Counter()
    for paper in c.papers:
        doc=c.document(paper['paper_id']);findings=[]
        for i,block in enumerate(doc['blocks']):
            if block['kind']!='caption' or not suspicious_reference(block['text']):continue
            neighbors=[b for b in doc['blocks'][max(0,i-1):i+2] if b['block_id']!=block['block_id']]
            findings.append({'block_id':block['block_id'],'source_pages':block['source_pages'],
                'source_line_ids':block['source_line_ids'],'text_sha256':digest(block['text'].encode()),
                'neighbor_block_ids':[b['block_id'] for b in neighbors],
                'disposition':'Check source paragraph continuity; do not silently omit author reference sentences or reclassify genuine captions.'})
        totals.update(papers_checked=1,physical_pages=doc['page_count'],
                      papers_with_candidates=bool(findings),candidate_blocks=len(findings))
        if findings:records.append({'paper_id':doc['paper_id'],'queue_position':paper['queue_position'],
                                   'source_sha256':doc['source_sha256'],'findings':findings})
    return {'dataset_id':c.identity,'totals':dict(totals),'papers':records,
            'auditor_sha256':file_hash(Path(__file__)),'source_fidelity_approved':False,
            'formula_verification':'paused','figure_distillation':'paused'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--corpus-root',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True);a=p.parse_args()
    if a.report.exists():raise ValueError('Create-only report exists')
    r=audit(a.corpus_root.resolve());json_new(a.report,r)
    print({k:v for k,v in r.items() if k!='papers'},flush=True)
