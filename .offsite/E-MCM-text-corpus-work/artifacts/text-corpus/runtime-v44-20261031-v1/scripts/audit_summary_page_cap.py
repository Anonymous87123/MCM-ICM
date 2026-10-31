"""Inventory every inferred page-cap transition; no source acceptance or edits."""
import argparse
from pathlib import Path
from corpus_reader import Catalog
from text_corpus import digest,file_hash,json_new,section_blocks,text_with_block_spans


def audit(root,report):
    if report.exists():
        raise ValueError('Create-only cap inventory exists; preserve it')
    catalog=Catalog(root);before=file_hash(root/'catalog.json');findings=[]
    for paper in catalog.papers:
        doc=catalog.document(paper['paper_id']);sections=doc['sections']
        for i,current in enumerate(sections):
            if current.get('origin')!='inferred-body' or i==0 or sections[i-1]['role']!='abstract':
                continue
            previous=sections[i-1]
            left=section_blocks(doc,[previous['section_id']]);right=section_blocks(doc,[current['section_id']])
            a,spans=text_with_block_spans(left);b,following=text_with_block_spans(right)
            findings.append({'paper_id':paper['paper_id'],'queue_position':paper['queue_position'],
                'document_sha256':paper['document_sha256'],
                'previous_section_id':previous['section_id'],'previous_title':previous['title'],
                'inferred_body_section_id':current['section_id'],
                'previous_pages':sorted({p for x in left for p in x['source_pages']}),
                'following_pages':sorted({p for x in right for p in x['source_pages']}),
                'previous_tail':a[-180:],'following_start':b[:180],
                'previous_text_sha256':digest(a.encode()),'following_text_sha256':digest(b.encode()),
                'status':'source review required; inferred page cap is not evidence that the summary ends',
                'source_sha256':doc['source_sha256'],'raw_pages_sha256':doc['raw_pages_sha256']})
    if file_hash(root/'catalog.json')!=before:
        raise ValueError('Corpus changed during inventory')
    result={'dataset_id':catalog.identity,'catalog_sha256':before,'papers_checked':len(catalog.papers),
        'candidate_transitions':len(findings),'papers_requiring_source_check':len({x['paper_id'] for x in findings}),
        'findings':findings,'source_fidelity_approved':False,'ai_reading_receipts_created':0,
        'meaning':'Complete census of the stored inferred-body transitions immediately after an abstract. Each is a boundary hypothesis, not proof of omission or of actual source absence.'}
    json_new(report,result)
    print({k:v for k,v in result.items() if k!='findings'},flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--corpus-root',type=Path,required=True);p.add_argument('--report',type=Path,required=True)
    a=p.parse_args();audit(a.corpus_root.resolve(),a.report.resolve())
