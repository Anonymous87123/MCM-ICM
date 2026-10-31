"""Bind every malformed-text frontier page to local OCR evidence, never apply it."""
import argparse
from collections import Counter
import math
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import file_hash, json_new, read_json


def verify_manifest(path, paper, expected_pages):
    manifest = read_json(path)
    if (manifest['paper_id']!=paper['paper_id'] or manifest['source_sha256']!=paper['source_sha256'] or
            sorted(p['page'] for p in manifest['pages'])!=sorted(set(expected_pages))):
        raise ValueError('OCR source or complete frontier-page scope differs')
    counts = Counter()
    for item in manifest['pages']:
        file = (path.parent/item['path']).resolve()
        if not file.is_relative_to(path.parent.resolve()) or file_hash(file)!=item['sha256']:
            raise ValueError('OCR page evidence missing, escaping or changed')
        page = read_json(file)
        if (page['page']!=item['page'] or page['review_status']!='pending' or
                len(page['lines'])!=item['line_count']):
            raise ValueError('OCR page metadata differs or is not an unverified candidate')
        if any(not math.isfinite(x['score']) or not 0<=x['score']<=1 or not x.get('pdf_box') for x in page['lines']):
            raise ValueError('OCR confidence/coordinates invalid')
        low = sum(x['score']<.95 for x in page['lines'])
        if low!=item['low_confidence_lines']:
            raise ValueError('OCR confidence census changed')
        counts.update(pages=1,ocr_lines=len(page['lines']),low_confidence_lines=low)
    return manifest,dict(counts)


def bind(root, frontier_path, ocr_root):
    catalog = Catalog(root)
    frontier = read_json(frontier_path)
    if frontier['dataset_id']!=catalog.identity:
        raise ValueError('Malformed-text frontier belongs to another data version')
    totals = Counter()
    papers = []
    for paper in frontier['papers']:
        record = catalog.by_id[paper['paper_id']]
        doc = catalog.document(paper['paper_id'])
        if (paper['document_sha256']!=record['document_sha256'] or
                any(paper[k]!=doc[k] for k in ('source_sha256','raw_pages_sha256'))):
            raise ValueError('Frontier document/raw/source preimage changed')
        path = ocr_root/paper['paper_id']/'attempt-0001/manifest.json'
        manifest,counts = verify_manifest(path,paper,paper['physical_pages'])
        totals.update(papers=1,**counts)
        papers.append({'paper_id':paper['paper_id'],'queue_position':paper['queue_position'],
            'document_sha256':record['document_sha256'],'source_sha256':doc['source_sha256'],
            'manifest_path':str(path.resolve()),'manifest_sha256':file_hash(path),
            'model_sha256':manifest['model_sha256'],'ocr_version':manifest['ocr_version'],
            'physical_pages':paper['physical_pages'],'counts':counts,'affected_blocks':paper['blocks'],
            'disposition':'OCR is a literal candidate with boxes/confidences. Compare each affected prose region to its source; never replace whole augmented pages or infer formula/figure semantics.'})
    if totals['pages']!=frontier['totals']['affected_paper_pages']:
        raise ValueError('Not every malformed-text source-page location has OCR evidence')
    return {'schema':'unicode-ocr-evidence-binding-v1','dataset_id':catalog.identity,
        'frontier_sha256':file_hash(frontier_path),'binder_sha256':file_hash(Path(__file__)),
        'totals':dict(totals),'papers':papers,'literal_repairs_applied':0,'source_fidelity_approved':False,
        'ai_reading_receipts_created':0,'formula_verification':'paused','figure_distillation':'paused'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root',type=Path,required=True)
    parser.add_argument('--frontier',type=Path,required=True)
    parser.add_argument('--ocr-root',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise ValueError('Create-only OCR binding report exists; preserve it')
    result = bind(args.corpus_root.resolve(),args.frontier.resolve(),args.ocr_root.resolve())
    json_new(args.report,result)
    print({k:v for k,v in result.items() if k!='papers'},flush=True)
