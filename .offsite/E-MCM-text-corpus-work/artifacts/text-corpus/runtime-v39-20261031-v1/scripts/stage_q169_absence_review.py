"""Bind complete actual native/layout coverage to source-local abstract absence."""
import copy
from pathlib import Path
import re

from corpus_reader import Catalog
from source_absence_reviews import apply_absence_reviews, prepare_absence_reviews
from text_corpus import file_hash, json_new, read_json, rows


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261031-v27'
    directory = base / 'reviews/20261031'
    output = directory / 'q169-abstract-absence-v1.json'
    combined_path = directory / 'q169-whole-source-layout-findings-v1.json'
    if output.exists() or combined_path.exists():
        raise ValueError('Create-only evidence exists; preserve it')
    doc = Catalog(root).document('P-C-2011-8882-54492a1f')
    folder = base / 'source-reviews/q169-whole-source-20261030-v1'
    manifest_path = folder / 'manifest.json'
    manifest = read_json(manifest_path)
    census_path = base / 'reviews/20261030/q169-full-native-prose-census-v1.json'
    census = read_json(census_path)
    finding_paths = [directory / f'q169-pages{part}-layout-findings-v1.json'
                     for part in ('1-3', '4-15', '16-27')]
    findings = [read_json(path) for path in finding_paths]
    identity = ('paper_id', 'source_sha256', 'raw_pages_sha256')
    if any(any(item[k] != doc[k] for k in identity) for item in [manifest, census, *findings]):
        raise ValueError('Frozen source identities differ')
    pages = list(range(1, 28))
    coverage = [p for item in findings for p in item['checked_physical_pages']]
    if (doc['page_count'] != 27 or census['native_prose_read_pages'] != pages or
            coverage != pages or manifest['page_count'] != 27):
        raise ValueError('Exact native and actual heading/layout coverage required')
    by_name = {item['overview']: item for item in manifest['files'] if item.get('overview')}
    inspected = [{'file': 'overview-00.jpg', 'sha256': findings[0]['overview_sha256'],
                  'physical_pages': findings[0]['checked_physical_pages']}]
    inspected += [item for finding in findings[1:] for item in finding['overviews_actually_checked']]
    if [item['file'] for item in inspected] != [f'overview-{n:02d}.jpg' for n in range(9)]:
        raise ValueError('Actual overview coverage lost or repeated')
    for item in inspected:
        declared = by_name[item['file']]
        if item['sha256'] != declared['sha256'] or item['physical_pages'] != declared['physical_pages']:
            raise ValueError('Actually inspected overview binding differs')
    for item in manifest['files']:
        for field, sha in (('native_text', 'native_text_sha256'), ('raw_png', 'raw_png_sha256'), ('overview', 'sha256')):
            if item.get(field) and file_hash(folder / item[field]) != item[sha]:
                raise ValueError('Prepared source evidence changed')
        if item.get('overview') and (item['bytes'] > 450000 or
                (folder / item['overview']).stat().st_size != item['bytes']):
            raise ValueError('Proxy byte guard differs')
    records_path = work / 'artifacts/corpus/manifest.jsonl'
    records = rows(records_path)
    team = re.compile(r'(?<!\d)8882(?!\d)')
    matches = [record for record in records if team.search(record['file_name'])]
    source = Path(read_json(root / 'scope.json')['source_root'])
    candidates = [path for path in source.rglob('*8882*') if path.is_file()]
    exact = [path for path in candidates if team.search(path.name)]
    if (len(records) != 604 or len(matches) != 1 or matches[0]['sha256'] != doc['source_sha256'] or
            len(exact) != 1 or file_hash(exact[0]) != doc['source_sha256']):
        raise ValueError('Alternative local source inventory differs')
    raw = root / 'papers' / doc['paper_id'] / 'raw/pages.jsonl'
    if file_hash(raw) != doc['raw_pages_sha256']:
        raise ValueError('Native source changed')
    independent = root / 'papers' / doc['paper_id'] / 'raw/pdftotext.bin'
    if re.search(r'\b(?:abstract|summary)\b', independent.read_bytes().decode('utf-8', 'strict'), re.I):
        raise ValueError('Unreviewed independent synopsis occurrence')
    finding = ('The local27-page PDF starts with Contents, then explicit Introduction, Assumptions, '
               'Brief View, Simulation, Energy Demand/Supply, Impacts, Conclusion and References. '
               'The opening roadmap belongs to Introduction; Conclusion belongs to its explicit '
               'closing chapter. All native prose and all physical page headings/layouts were '
               'actually checked. No independent headed or unheaded abstract/summary exists.')
    combined = {'schema': 'whole-source-heading-layout-findings-v1', **{k: doc[k] for k in identity},
        'reviewer': 'Codex root;2026-10-30/31;all27 native prose pages and complete physical heading/layout coverage actually checked',
        'checked_physical_pages': pages, 'overviews_actually_checked': inspected,
        'bounded_findings_sha256': {str(path): file_hash(path) for path in finding_paths},
        'whole_source_abstract_finding': finding, 'whole_paper_source_fidelity_approved': False,
        'ai_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(combined_path, combined)
    evidence = [
        {'path': str(manifest_path), 'bundle_root': str(folder), 'sha256': file_hash(manifest_path),
         'description': 'Complete27-page native/raster evidence and all9 actually inspected bounded overview JPEGs.'},
        {'path': str(census_path), 'sha256': file_hash(census_path),
         'description': 'Earlier actual27-page native-prose census; old layout-pending limitation remains preserved.'},
        {'path': str(combined_path), 'sha256': file_hash(combined_path),
         'description': 'Later complete physical heading/layout coverage with exact inspected-image bindings.'}]
    evidence += [{'path': str(path), 'sha256': file_hash(path),
                  'description': 'Preserved actual bounded heading/layout findings.'} for path in finding_paths]
    proof = {'schema': 'source-absence-review-v1', **{k: doc[k] for k in identity},
        'role': 'abstract', 'reviewer': combined['reviewer'], 'page_count': 27, 'checked_pages': pages,
        'reason': finding + ' Source-local only; no external completeness or whole-paper fidelity claim.',
        'full_native_prose_read': True, 'physical_page_heading_layout_checked': True,
        'independent_text_check': {'path': f"papers/{doc['paper_id']}/raw/pdftotext.bin", 'sha256': file_hash(independent),
            'status': 'StrictUTF8;zero Abstract/Summary word occurrences. Not literal whole-text acceptance.'},
        'alternative_copy_check': {'manifest_sha256': file_hash(records_path), 'manifest_records': len(records),
            'matching_file_count': len(exact), 'substring_candidates': [
                {'relative_path': path.relative_to(source).as_posix(), 'sha256': file_hash(path),
                 'same_team_token': bool(team.search(path.name))} for path in candidates],
            'result': 'All604 records and local filename candidates checked; only the same27-page PDF.'},
        'evidence': evidence, 'application_status': 'Staged for immutable generation; parent/history/receipts unchanged.',
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output, proof)
    prepared, copies = prepare_absence_reviews([output])
    apply_absence_reviews(copy.deepcopy(doc), prepared)
    print({'paper_id': doc['paper_id'], 'source_checked_pages': 27, 'portable_evidence_files': len(copies),
           'abstract_absence': 'staged source-local only', 'whole_paper_acceptance': False}, flush=True)


if __name__ == '__main__':
    main()
