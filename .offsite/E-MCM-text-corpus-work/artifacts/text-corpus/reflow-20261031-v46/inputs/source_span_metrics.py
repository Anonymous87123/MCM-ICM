"""Derive candidate reading boxes from exact, separately frozen PDF baselines.

Only typography is reconstructed. No symbol, formula or visual meaning is
inferred. Native evidence is unchanged and every changed box remains reviewable.
"""
from __future__ import annotations
import copy
from collections import Counter
from pathlib import Path
from extract_text_span_metrics import native_preimage
from text_corpus import digest,encoded,file_hash,read_json,rows


def normal_metric(metric):
    return .5 <= metric['ascender'] <= 1.8 and -.6 <= metric['descender'] <= .1


def page_reference(page,metrics):
    votes=Counter();examples={}
    by_id={x['line_id']:x for x in metrics['lines']}
    for line in page['lines']:
        item=by_id.get(line['line_id'])
        if not item:
            continue
        for span,metric in zip(line['spans'],item['spans']):
            if 6<=span['size']<=24 and normal_metric(metric) and any(c.isalpha() for c in span['text']):
                key=(span['font'],round(span['size'],1),metric['ascender'],metric['descender'])
                votes[key]+=sum(c.isalpha() for c in span['text'])
                examples[key]={'font':span['font'],'ascender':metric['ascender'],
                               'descender':metric['descender'],'source_line_id':line['line_id']}
    return examples[votes.most_common(1)[0][0]] if votes else None


def flow_line(line,record,reference,evidence_sha256):
    if (not line['text'].strip() or record['writing_mode']!=0 or
            abs(record['direction'][0]-1)>.01 or abs(record['direction'][1])>.01):
        return line
    spans=line['spans'];metrics=record['spans']
    # A trailing space can carry the same corrupt font metrics as a visible
    # glyph and pull an otherwise ordinary heading above the preceding sentence.
    unusual=[i for i,(s,m) in enumerate(zip(spans,metrics)) if s['text'] and
             m['ascender']-m['descender']>2.5 and s['bbox'][3]-s['bbox'][1]>s['size']*2.5]
    if not unusual:
        return line
    size=max(spans[i]['size'] for i in unusual)
    ordinary=[i for i,(s,m) in enumerate(zip(spans,metrics)) if normal_metric(m) and s['size']>=size*.85]
    if ordinary:
        origins=[metrics[i]['origin'][1] for i in ordinary]
        if max(origins)-min(origins)>size*.5:
            return line  # Multi-baseline prose must not be collapsed.
        top=min(spans[i]['bbox'][1] for i in ordinary)
        bottom=max(spans[i]['bbox'][3] for i in ordinary)
        basis='normal spans on the same PDF baseline, including literal whitespace'
    elif reference:
        # Native formula-only line positions can also intrude into prose when a
        # font advertises enormous ascenders. Retain its complete glyph text and
        # vertical range; use actual origins and page-local ordinary-font metrics
        # solely to locate the line. Scripts do not decide what the formula means.
        base=[i for i in unusual if spans[i]['size']>=size*.95]
        origins=[metrics[i]['origin'][1] for i in base]
        top=min(metrics[i]['origin'][1]-reference['ascender']*spans[i]['size'] for i in base)
        bottom=max(metrics[i]['origin'][1]-reference['descender']*spans[i]['size'] for i in base)
        basis='native span origins and the dominant ordinary font on this physical page'
    else:
        return line
    if bottom<=top:
        return line
    bbox=[line['bbox'][0],top,line['bbox'][2],bottom]
    return dict(line,bbox=bbox,flow_geometry_candidate={
        'rule':'pdf-span-origin-flow-v1','source_line_id':line['line_id'],
        'raw_bbox':list(line['bbox']),'flow_bbox':bbox,'basis':basis,
        'source_metrics_sha256':evidence_sha256,'metrics_record_sha256':digest(encoded(record)),
        'origin_y_range':[min(origins),max(origins)],'ordinary_span_indices':ordinary,
        'page_font_reference':reference if not ordinary else None,
        'review_status':'machine candidate; prose layout still requires source check'})


def prepare_flow_pages(document,pages,metrics_root:Path):
    folder=metrics_root/'papers'/document['paper_id']
    complete=read_json(folder/'COMPLETE.json');payload=folder/'span-metrics.jsonl'
    sha=file_hash(payload)
    if (complete['paper_id']!=document['paper_id'] or complete['source_sha256']!=document['source_sha256'] or
            complete['raw_pages_sha256']!=document['raw_pages_sha256'] or
            complete['page_count']!=len(pages) or complete['files']['span-metrics.jsonl']!=sha):
        raise ValueError('Source span metrics do not bind this native evidence')
    metrics=rows(payload)
    if [x['page'] for x in metrics]!=list(range(1,len(pages)+1)):
        raise ValueError('Span metrics physical-page coverage differs')
    result=copy.deepcopy(pages);changed=[]
    for page,m in zip(result,metrics):
        originals={x['line_id']:x for x in page['lines'] if x['native_block']>=0}
        items={x['line_id']:x for x in m['lines']}
        if len(items)!=len(m['lines']) or set(items)!=set(originals):
            raise ValueError('Span metric native-line coverage differs')
        for lid,item in items.items():
            line=originals[lid]
            if native_preimage(line)!=item['native_preimage_sha256'] or len(item['spans'])!=len(line['spans']):
                raise ValueError('Span metric line preimage differs: '+lid)
        reference=page_reference(page,m)
        for i,line in enumerate(page['lines']):
            if line['line_id'] not in items or line.get('superseded_by_ocr'):
                continue
            candidate=flow_line(line,items[line['line_id']],reference,sha)
            page['lines'][i]=candidate
            if candidate is not line:
                changed.append({'page':page['page'],**candidate['flow_geometry_candidate']})
    return result,{'schema':'source-span-origin-flow-candidate-v1','paper_id':document['paper_id'],
        'source_sha256':document['source_sha256'],'raw_pages_sha256':document['raw_pages_sha256'],
        'metrics_sha256':sha,'changed_lines':changed,'source_fidelity_approved':False}


def validate_flow_evidence(root,document,pages):
    """Replay local geometry evidence; never convert it into source acceptance."""
    marker=document.get('span_origin_flow')
    scope=read_json(root/'scope.json')
    expected_manifest=scope.get('span_metrics_manifest_sha256')
    if not marker and not expected_manifest:
        return
    if not marker or not expected_manifest:
        raise ValueError('Span-origin evidence declaration missing')
    evidence=root/'inputs/span-metrics';manifest=evidence/'manifest.json'
    complete=evidence/'papers'/document['paper_id']/'COMPLETE.json'
    if (file_hash(manifest)!=expected_manifest or
            read_json(manifest)['files'].get(document['paper_id'])!=file_hash(complete)):
        raise ValueError('Span-origin manifest binding changed')
    _,flow=prepare_flow_pages(document,pages,evidence)
    # Page number belongs to the report envelope, while the line-bound repair
    # record derives its physical page from its source line ID/block ownership.
    expected={x['source_line_id']:{k:v for k,v in x.items() if k!='page'} for x in flow['changed_lines']}
    if (marker.get('schema')!='source-span-origin-flow-candidate-v1' or
            marker.get('metrics_sha256')!=flow['metrics_sha256'] or
            marker.get('changed_lines')!=len(expected) or marker.get('source_fidelity_approved') is not False):
        raise ValueError('Span-origin candidate declaration differs')
    used={lid for b in document['blocks'] for lid in b['source_line_ids']}
    actual=[]
    for defect in document['defects']:
        if defect['code']=='inline_math_prose_flow_review':
            actual.extend(x for x in defect['inference'] if x.get('rule')=='pdf-span-origin-flow-v1')
    wanted=[x for lid,x in expected.items() if lid in used]
    if Counter(encoded(x) for x in actual)!=Counter(encoded(x) for x in wanted):
        raise ValueError('Span-origin page geometry replay differs')
    for block in document['blocks']:
        for repair in block.get('repairs',[]):
            if repair.get('operation')=='prose_flow_geometry_candidate' and repair.get('rule')=='pdf-span-origin-flow-v1':
                item={k:v for k,v in repair.items() if k!='operation'}
                if item!=expected.get(item.get('source_line_id')) or item['source_line_id'] not in block['source_line_ids']:
                    raise ValueError('Span-origin block geometry replay differs')
