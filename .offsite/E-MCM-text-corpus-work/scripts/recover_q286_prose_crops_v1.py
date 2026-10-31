"""Two local source-bound OCR crops for q286's already inspected prose only."""
import importlib.metadata
import importlib.util
from pathlib import Path
import sys

sys.path.insert(0, r'F:\MCM\mcm-skill-work\scripts')
from corpus_reader import Catalog
from make_review_proxy import main as make_proxy
from text_corpus import file_hash, json_new, read_json, write_new


def main():
    import numpy as np
    import pymupdf
    from rapidocr import RapidOCR
    root = Path(r'F:\MCM\mcm-skill-work\artifacts\text-corpus\reflow-20261031-v34')
    output = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus\reviews\20261031\q286-prose-crops-v1')
    if output.exists():
        raise ValueError('Create-only crop evidence exists; preserve it')
    catalog = Catalog(root)
    doc = catalog.document('P-D-2017-68942-f0b0893e')
    source = Path(read_json(root / 'scope.json')['source_root']) / doc['source_relative_path']
    if file_hash(source) != doc['source_sha256']:
        raise ValueError('Source PDF changed')
    models = Path(importlib.util.find_spec('rapidocr').origin).parent / 'models'
    paths = {stage: models / name for stage, name in {'Det': 'PP-OCRv6_det_small.onnx', 'Rec': 'PP-OCRv6_rec_small.onnx', 'Cls': 'ch_ppocr_mobile_v2.0_cls_mobile.onnx'}.items()}
    if any(not path.is_file() for path in paths.values()):
        raise ValueError('Pinned local models missing; no implicit download')
    params = {f'{stage}.model_path': str(path) for stage, path in paths.items()}
    params.update({'Global.text_score': 0.0, 'EngineConfig.onnxruntime.intra_op_num_threads': 2, 'EngineConfig.onnxruntime.inter_op_num_threads': 1})
    engine = RapidOCR(params=params)
    output.mkdir(parents=True)
    values = []
    with pymupdf.open(source) as pdf:
        page = pdf[0]
        for index, clip in [(30, [119, 351.8, 484, 363.0]), (37, [119, 429.8, 484, 442.7])]:
            pix = page.get_pixmap(dpi=360, clip=pymupdf.Rect(clip), alpha=False, colorspace=pymupdf.csRGB)
            array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
            result = engine(array, use_det=False, use_cls=False, use_rec=True)
            raster = output / f'line-{index:02d}.png'
            proxy = output / f'line-{index:02d}.jpg'
            write_new(raster, pix.tobytes('png'))
            make_proxy(['--input', str(raster), '--output', str(proxy), '--max-bytes', '450000'])
            values.append({'original_ocr_index': index, 'pdf_clip': clip, 'dpi': 360,
                'raster_sha256': file_hash(raster), 'proxy_sha256': file_hash(proxy), 'proxy_bytes': proxy.stat().st_size,
                'lines': [{'text': text, 'score': float(score)} for text, score in zip(result.txts or [], result.scores if result.scores is not None else [])],
                'inspection_status': 'prepared; not yet inspected'})
    value = {'paper_id': doc['paper_id'], 'parent_dataset_id': catalog.identity,
        'source_sha256': doc['source_sha256'], 'raw_pages_sha256': doc['raw_pages_sha256'],
        'ocr_version': importlib.metadata.version('rapidocr'), 'model_sha256': {stage: file_hash(path) for stage, path in paths.items()},
        'physical_page': 1, 'crops': values, 'source_fidelity_approved': False, 'ai_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output / 'result.json', value)
    print(value, flush=True)


if __name__ == '__main__':
    main()
