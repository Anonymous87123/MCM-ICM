"""Create bounded whole-source heading/layout evidence, without source approval.

Native page text is retained separately. Contact sheets are only for heading and
paragraph-layout inspection; all formulas/charts remain outside the review scope.
"""
import argparse
import io
from pathlib import Path
import pymupdf
from PIL import Image,ImageDraw
from corpus_reader import Catalog
from make_review_proxy import build_proxy
from text_corpus import file_hash,json_new,read_json,rows,write_new


def prepare(root,queue,output):
    if output.exists():
        raise ValueError('Create-only evidence already exists')
    catalog=Catalog(root)
    record=next(p for p in catalog.papers if p['queue_position']==queue)
    doc=catalog.document(record['paper_id'])
    source=Path(read_json(root/'scope.json')['source_root'])/doc['source_relative_path']
    if file_hash(source)!=doc['source_sha256']:
        raise ValueError('Source PDF changed')
    pages=rows(root/'papers'/doc['paper_id']/'raw/pages.jsonl')
    output.mkdir(parents=True)
    evidence=[]
    with pymupdf.open(source) as pdf:
        if len(pdf)!=len(pages):
            raise ValueError('Source physical page count changed')
        for start in range(0,len(pdf),3):
            sheet=Image.new('RGB',(2400,1200),'#dddddd')
            draw=ImageDraw.Draw(sheet)
            numbers=[]
            for offset in range(min(3,len(pdf)-start)):
                number=start+offset+1;numbers.append(number)
                page=pdf[number-1]
                pix=page.get_pixmap(dpi=130,alpha=False)
                png=pix.tobytes('png')
                pngpath=output/f'page-{number:04d}.png'
                write_new(pngpath,png)
                textpath=output/f'page-{number:04d}.txt'
                write_new(textpath,'\n'.join(x['text'] for x in pages[number-1]['lines'])+'\n')
                im=Image.open(io.BytesIO(png)).convert('RGB')
                im.thumbnail((780,1150))
                sheet.paste(im,(offset*800+(800-im.width)//2,35))
                draw.text((offset*800+15,10),f'PHYSICAL PAGE {number}',fill='black')
                evidence.append({'physical_page':number,'raw_png':pngpath.name,'raw_png_sha256':file_hash(pngpath),
                    'native_text':textpath.name,'native_text_sha256':file_hash(textpath)})
            data,_,quality=build_proxy(sheet,max_width=2400,max_height=1200,max_bytes=450000,start_quality=88)
            name=f'overview-{start//3:02d}.jpg';write_new(output/name,data)
            evidence.append({'overview':name,'physical_pages':numbers,'bytes':len(data),
                'sha256':file_hash(output/name),'quality':quality})
    result={'dataset_id':catalog.identity,'paper_id':doc['paper_id'],'source_sha256':doc['source_sha256'],
        'raw_pages_sha256':doc['raw_pages_sha256'],'page_count':len(pages),'files':evidence,
        'review_status':'prepared, not yet read or approved','formula_verification':'paused','figure_distillation':'paused'}
    json_new(output/'manifest.json',result)
    print({'paper_id':doc['paper_id'],'pages':len(pages),'overviews':(len(pages)+2)//3,
           'overview_bytes':sum(x.get('bytes',0) for x in evidence),'source_approved':False})


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--corpus-root',type=Path,required=True);p.add_argument('--queue',type=int,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();prepare(a.corpus_root.resolve(),a.queue,a.output.resolve())
