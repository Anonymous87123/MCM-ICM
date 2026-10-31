"""Inventory every early contents-page candidate that leaks into author queries.

This never edits a document, drops a line, or establishes source absence. Dotted
and hyphen leaders are discovery signals; every repair still needs source checks.
"""
import argparse
from collections import Counter,defaultdict
from pathlib import Path
import re
from corpus_reader import Catalog
from text_corpus import PROSE_KINDS,file_hash,json_new


def audit(root):
    catalog=Catalog(root);papers=[];totals=Counter()
    for record in catalog.papers:
        doc=catalog.document(record['paper_id']);by_page=defaultdict(list)
        sections={s['section_id']:s for s in doc['sections']}
        for block in doc['blocks']:
            if len(block['source_pages'])==1 and block['source_pages'][0]<=5:
                by_page[block['source_pages'][0]].append(block)
        def within_contents(sid):
            seen=set()
            while sid:
                if sid in seen or sid not in sections:
                    raise ValueError('Invalid frozen section hierarchy')
                seen.add(sid);s=sections[sid]
                if s['role']=='contents':return True
                sid=s['parent_id']
            return False
        findings=[]
        for page,blocks in by_page.items():
            explicit=any(re.fullmatch(r'(?:table of )?contents?',b['text'].strip(),re.I) for b in blocks)
            leaders=[b for b in blocks if re.search(r'(?:[.\-]\s*){6,}\s*\d+\s*$',b['text'])]
            if not (explicit or len(leaders)>=8):continue
            leaked=[b for b in blocks if b['kind'] in PROSE_KINDS and not within_contents(b['section_id'])]
            if leaked:
                findings.append({'physical_page':page,'explicit_contents_label':explicit,
                    'leader_block_ids':[b['block_id'] for b in leaders],
                    'leaked_block_ids':[b['block_id'] for b in leaked],
                    'affected_section_ids':sorted({b['section_id'] for b in leaked}),
                    'meaning':'Candidate contents text enters default author-section selection; inspect full source page before repair.'})
        totals.update(papers_checked=1,physical_pages=doc['page_count'],
                      papers_with_candidate_leakage=bool(findings),candidate_pages=len(findings))
        if findings:
            papers.append({'paper_id':doc['paper_id'],'queue_position':record['queue_position'],
                           'source_sha256':doc['source_sha256'],'document_sha256':record['document_sha256'],
                           'findings':findings})
    return {'dataset_id':catalog.identity,'totals':dict(totals),'papers':papers,
            'auditor_sha256':file_hash(Path(__file__)),'source_fidelity_approved':False,
            'formula_verification':'paused','figure_distillation':'paused'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--corpus-root',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True);a=p.parse_args()
    if a.report.exists():raise ValueError('Create-only report exists')
    result=audit(a.corpus_root.resolve());json_new(a.report,result)
    print({k:v for k,v in result.items() if k!='papers'},flush=True)
