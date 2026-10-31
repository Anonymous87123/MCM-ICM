"""Create-only, byte-bounded physical page evidence for prose restoration."""
import argparse
from pathlib import Path

import pymupdf

from corpus_reader import Catalog
from make_review_proxy import main as make_proxy
from text_corpus import file_hash, json_new, read_json, rows, write_new


def prepare(root, queue, numbers, output):
    if output.exists():
        raise ValueError('Source evidence directory exists; preserve it')
    catalog = Catalog(root)
    paper = next(p for p in catalog.papers if p['queue_position'] == queue)
    doc = catalog.document(paper['paper_id'])
    if not numbers or len(set(numbers)) != len(numbers) or any(n<1 or n>doc['page_count'] for n in numbers):
        raise ValueError('Invalid physical page list')
    scope = read_json(root/'scope.json')
    source = Path(scope['source_root'])/doc['source_relative_path']
    if file_hash(source) != doc['source_sha256']:
        raise ValueError('Source PDF bytes changed')
    raw = root/'papers'/doc['paper_id']/'raw/pages.jsonl'
    if file_hash(raw) != doc['raw_pages_sha256']:
        raise ValueError('Frozen native text changed')
    pages = rows(raw)
    output.mkdir(parents=True)
    evidence = []
    with pymupdf.open(source) as pdf:
        if len(pdf) != doc['page_count']:
            raise ValueError('Source physical page count differs')
        for number in numbers:
            prefix = f'page-{number:04d}'
            raster = output/(prefix+'.png')
            page = pdf[number-1]
            write_new(raster,page.get_pixmap(dpi=200,alpha=False).tobytes('png'))
            proxy = output/(prefix+'.jpg')
            make_proxy(['--input',str(raster),'--output',str(proxy),'--max-bytes','450000'])
            json_new(output/(prefix+'-native.json'),pages[number-1])
            json_new(output/(prefix+'-blocks.json'),[b for b in doc['blocks'] if number in b['source_pages']])
            evidence.append({'page':number,'rotation':page.rotation,'rect':list(page.rect),
                'raster':raster.name,'proxy':proxy.name,'proxy_bytes':proxy.stat().st_size,
                'inspection_status':'prepared; not yet visually reviewed'})
    files = {p.name:file_hash(p) for p in output.iterdir() if p.is_file()}
    result = {'dataset_id':catalog.identity,'queue_position':queue,
        **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256','page_count')},
        'source_relative_path':doc['source_relative_path'],'pages':evidence,'files':files,
        'purpose':'Only recover author prose, source ownership and paragraph/section boundaries.',
        'source_fidelity_approved':False,'ai_processing_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'}
    json_new(output/'manifest.json',result)
    print({'paper_id':doc['paper_id'],'pages':numbers,'output':str(output),'source_fidelity_approved':False},flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root',type=Path,required=True)
    parser.add_argument('--queue',type=int,required=True)
    parser.add_argument('--pages',type=int,nargs='+',required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    prepare(args.corpus_root.resolve(),args.queue,args.pages,args.output.resolve())
