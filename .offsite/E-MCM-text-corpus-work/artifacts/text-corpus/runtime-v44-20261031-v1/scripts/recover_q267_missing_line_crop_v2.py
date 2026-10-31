"""Local source-bound OCR of q267's actually inspected missing prose line only."""
import importlib.metadata
import importlib.util
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import file_hash, json_new, read_json, write_new


def main():
    import numpy as np
    import pymupdf
    from rapidocr import RapidOCR

    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    output = base / 'reviews/20261031/q267-missing-line-ocr-crop-v2'
    if output.exists():
        raise ValueError('Create-only crop evidence exists; preserve it')
    root = base / 'reflow-20261031-v30'
    catalog = Catalog(root)
    document = catalog.document('P-C-2025-2516178-573cdff6')
    source = Path(read_json(root / 'scope.json')['source_root']) / document['source_relative_path']
    if file_hash(source) != document['source_sha256']:
        raise ValueError('Source PDF changed')
    models = Path(importlib.util.find_spec('rapidocr').origin).parent / 'models'
    names = {'Det': 'PP-OCRv6_det_small.onnx', 'Rec': 'PP-OCRv6_rec_small.onnx',
             'Cls': 'ch_ppocr_mobile_v2.0_cls_mobile.onnx'}
    paths = {stage: models / name for stage, name in names.items()}
    if any(not path.is_file() for path in paths.values()):
        raise ValueError('Pinned local OCR models missing; no download')
    params = {f'{stage}.model_path': str(path) for stage, path in paths.items()}
    params.update({'Global.text_score': 0.0, 'EngineConfig.onnxruntime.intra_op_num_threads': 2,
                   'EngineConfig.onnxruntime.inter_op_num_threads': 1})
    engine = RapidOCR(params=params)
    clip = [70, 312, 525, 328]
    dpi = 360
    with pymupdf.open(source) as pdf:
        page = pdf[0]
        if page.rotation or not page.rect.contains(pymupdf.Rect(clip)):
            raise ValueError('Exact unrotated page crop required')
        pix = page.get_pixmap(dpi=dpi, clip=pymupdf.Rect(clip), alpha=False, colorspace=pymupdf.csRGB)
    array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
    result = engine(array, use_det=False, use_cls=False, use_rec=True)
    values = []
    if result.txts is not None:
        for text, score in zip(result.txts, result.scores):
            values.append({'text': text, 'score': float(score),
                'recognition_input_pdf_clip': clip, 'box_origin': 'manually checked source crop; detection disabled'})
    output.mkdir(parents=True)
    raster = output / 'missing-line-crop.png'
    write_new(raster, pix.tobytes('png'))
    value = {'schema': 'source-bound-prose-ocr-crop-v1', 'paper_id': document['paper_id'],
        'parent_dataset_id': catalog.identity, 'source_sha256': document['source_sha256'],
        'raw_pages_sha256': document['raw_pages_sha256'], 'physical_page': 1,
        'pdf_clip': clip, 'dpi': dpi, 'width_pixels': pix.width, 'height_pixels': pix.height,
        'raster_sha256': file_hash(raster), 'ocr_version': importlib.metadata.version('rapidocr'),
        'model_sha256': {stage: file_hash(path) for stage, path in paths.items()},
        'lines': values, 'purpose': 'Recover missing author line after we employed; image previously inspected.',
        'detection_enabled': False, 'classification_enabled': False,
        'not_applied_to_any_corpus': True, 'source_fidelity_approved': False, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output / 'result.json', value)
    print(value, flush=True)


if __name__ == '__main__':
    main()
