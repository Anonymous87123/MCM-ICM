"""Whole-scope inventory of explicit non-author headings misrouted as author text."""
import argparse
from collections import Counter
from pathlib import Path
import re
from corpus_reader import Catalog
from corpus_queries import all_author_blocks
from text_corpus import HEADING_NUMBER,file_hash,json_new


def expected_exclusion(title):
    t=re.sub(r'^\s*'+HEADING_NUMBER+r'\s+','',title).strip()
    if re.fullmatch(r'(?:references?|bibliograph(?:y|ies)|works cited|参考文献|参考资料)[.:：]?',t,re.I):
        return 'references'
    if re.fullmatch(r'(?:table of )?contents?[.:：]?',t,re.I):
        return 'contents'
    return None


def audit(root):
    catalog=Catalog(root);papers=[];totals=Counter()
    for record in catalog.papers:
        doc=catalog.document(record['paper_id']);author={b['block_id'] for b in all_author_blocks(doc)}
        findings=[]
        for section in doc['sections']:
            role=expected_exclusion(section['title'])
            if not role or role==section['role']:continue
            retained=[b for b in doc['blocks'] if b['section_id']==section['section_id']]
            leaked=[b['block_id'] for b in retained if b['block_id'] in author]
            if leaked:
                findings.append({'section_id':section['section_id'],'printed_title':section['title'],
                    'current_role':section['role'],'candidate_role':role,
                    'physical_pages':sorted({p for b in retained for p in b['source_pages']}),
                    'source_line_ids':[lid for b in retained if b['kind']=='heading' for lid in b['source_line_ids']],
                    'leaked_block_ids':leaked,
                    'disposition':'Preserve all source blocks; correct normalized role after source-heading/boundary check.'})
        totals.update(papers_checked=1,physical_pages=doc['page_count'],
                      papers_with_candidates=bool(findings),candidate_sections=len(findings))
        if findings:papers.append({'paper_id':doc['paper_id'],'queue_position':record['queue_position'],
                                   'source_sha256':doc['source_sha256'],'findings':findings})
    return {'dataset_id':catalog.identity,'totals':dict(totals),'papers':papers,
            'auditor_sha256':file_hash(Path(__file__)),'source_fidelity_approved':False,
            'formula_verification':'paused','figure_distillation':'paused'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--corpus-root',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True);a=p.parse_args()
    if a.report.exists():raise ValueError('Create-only report exists')
    r=audit(a.corpus_root.resolve());json_new(a.report,r)
    print({k:v for k,v in r.items() if k!='papers'},flush=True)
