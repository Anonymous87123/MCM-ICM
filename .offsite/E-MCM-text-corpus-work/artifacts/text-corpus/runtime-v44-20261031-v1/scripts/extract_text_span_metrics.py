"""Preserve missing PDF baseline metrics in a NEW source-bound sidecar corpus.

Never changes native/OCR text. Every fresh native line/span must exactly match
the frozen extraction before its origin/direction/metrics can be associated with
that line ID. This is typography evidence, not source reading or formula review.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import pymupdf
from corpus_reader import Catalog
from text_corpus import digest,encoded,file_hash,json_new,read_json,rows,write_new

FLAGS=pymupdf.TEXTFLAGS_DICT & ~pymupdf.TEXT_PRESERVE_IMAGES
SPAN_KEYS=('text','bbox','font','size','flags')


def native_preimage(line):
    return digest(encoded({k:line[k] for k in ('line_id','text','bbox','spans')}))


def match_page(raw, fresh):
    expected={x['line_id']:x for x in raw['lines'] if x['native_block']>=0}
    found={};result=[]
    for bi,block in enumerate(fresh['blocks']):
        if block['type']!=0:
            continue
        for li,line in enumerate(block['lines']):
            if not line['spans']:
                continue
            lid=f"p{raw['page']:04d}-n{bi:04d}-l{li:04d}"
            old=expected.get(lid)
            spans=[{k:s[k] for k in SPAN_KEYS} for s in line['spans']]
            # JSON turns native tuple bboxes into lists; canonical serialization
            # handles that representation difference, never fuzzy text matching.
            if old is None or encoded(spans)!=encoded(old['spans']) or list(line['bbox'])!=old['bbox']:
                raise ValueError('Fresh PDF line/span preimage differs: '+lid)
            text=''.join(s['text'] for s in spans)
            if text!=old['text']:
                raise ValueError('Fresh PDF text differs: '+lid)
            found[lid]=True
            result.append({'line_id':lid,'native_preimage_sha256':native_preimage(old),
                'direction':list(line['dir']),'writing_mode':line['wmode'],
                'spans':[{'origin':list(s['origin']),'ascender':s['ascender'],
                          'descender':s['descender']} for s in line['spans']]})
    if set(found)!=set(expected):
        raise ValueError('Native source-line coverage differs on page'+str(raw['page']))
    return {'page':raw['page'],'lines':result}


def extract(catalog,paper,source_root,output):
    pid=paper['paper_id'];doc=catalog.document(pid)
    target=output/'papers'/pid
    source=source_root/doc['source_relative_path']
    if file_hash(source)!=doc['source_sha256']:
        raise ValueError('Source PDF hash differs: '+pid)
    if (target/'COMPLETE.json').is_file():
        done=read_json(target/'COMPLETE.json')
        if (done['source_sha256']!=doc['source_sha256'] or done['raw_pages_sha256']!=doc['raw_pages_sha256'] or
                file_hash(target/'span-metrics.jsonl')!=done['files']['span-metrics.jsonl']):
            raise ValueError('Completed metric evidence changed: '+pid)
        return done
    if target.exists():
        raise ValueError('Incomplete metrics retained; inspect and choose a new output: '+pid)
    rawpath=catalog.root/'papers'/pid/'raw/pages.jsonl'
    if file_hash(rawpath)!=doc['raw_pages_sha256']:
        raise ValueError('Frozen raw evidence changed: '+pid)
    pages=rows(rawpath);result=[]
    with pymupdf.open(source) as pdf:
        if len(pdf)!=len(pages):
            raise ValueError('Physical page denominator differs: '+pid)
        for page,raw in zip(pdf,pages):
            result.append(match_page(raw,page.get_text('dict',flags=FLAGS,sort=False)))
    # No directory or partial sidecar is created until every source preimage
    # agrees. The native text corpus remains immutable even on a failed paper.
    payload=b''.join((json.dumps(p,ensure_ascii=True,sort_keys=True)+'\n').encode() for p in result)
    write_new(target/'span-metrics.jsonl',payload)
    done={'schema':'pdf-span-metrics-v1','paper_id':pid,'source_sha256':doc['source_sha256'],
        'raw_pages_sha256':doc['raw_pages_sha256'],'page_count':len(pages),
        'native_lines':sum(len(p['lines']) for p in result),
        'spans':sum(len(l['spans']) for p in result for l in p['lines']),
        'files':{'span-metrics.jsonl':digest(payload)},
        'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    json_new(target/'COMPLETE.json',done)
    return done


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--corpus-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--limit',type=int)
    a=p.parse_args();catalog=Catalog(a.corpus_root.resolve());output=a.output.resolve()
    if a.limit is not None and a.limit<1:
        raise ValueError('Positive prototype limit required')
    parent_scope=read_json(catalog.root/'scope.json')
    scope={'schema':'pdf-span-metrics-scope-v1','parent_dataset_id':catalog.identity,
        'paper_ids':[p['paper_id'] for p in catalog.papers],'paper_count':len(catalog.papers),
        'page_count':sum(p['page_count'] for p in catalog.papers),'pymupdf_version':pymupdf.VersionBind,
        'text_flags':FLAGS,'extractor_sha256':file_hash(Path(__file__))}
    if (output/'scope.json').is_file():
        if read_json(output/'scope.json')!=scope:
            raise ValueError('Frozen metric scope/implementation changed; use a new version')
    else:
        if output.exists():
            raise ValueError('Output exists without scope; do not overwrite')
        json_new(output/'scope.json',scope)
        write_new(output/'inputs/extract_text_span_metrics.py',Path(__file__).read_bytes())
    records=[]
    for paper in catalog.papers[:a.limit]:
        done=extract(catalog,paper,Path(parent_scope['source_root']),output);records.append(done)
        if len(records)%25==0 or a.limit:
            print(json.dumps({'metrics_papers':len(records),'target':len(catalog.papers),
                              'last_queue_position':paper['queue_position']}),flush=True)
    result={'parent_dataset_id':catalog.identity,'papers':len(records),
        'physical_pages':sum(r['page_count'] for r in records),
        'native_lines':sum(r['native_lines'] for r in records),'spans':sum(r['spans'] for r in records),
        'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    if len(records)==len(catalog.papers):
        result['files']={p['paper_id']:file_hash(output/'papers'/p['paper_id']/'COMPLETE.json') for p in catalog.papers}
        json_new(output/'manifest.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='files'}),flush=True)


if __name__=='__main__':
    main()
