"""Create-only source-local absence proof after actual20-page prose/layout reading."""
import copy
from pathlib import Path
import re

from corpus_reader import Catalog
from source_absence_reviews import apply_absence_reviews, prepare_absence_reviews
from text_corpus import file_hash, json_new, read_json, rows


def main():
    work = Path(__file__).resolve().parents[1]
    base = work/'artifacts/text-corpus'
    root = base/'reflow-20261030-v14'
    reviews = base/'reviews/20261030'
    output = reviews/'q170-abstract-absence-v1.json'
    if output.exists():
        raise ValueError('Create-only proof exists; preserve it')
    doc = Catalog(root).document('P-C-2011-9089-838e50df')
    census_path = reviews/'q170-full-native-prose-census-v1.json'
    findings_path = reviews/'q170-whole-source-layout-findings-v1.json'
    census,findings = read_json(census_path),read_json(findings_path)
    folder = base/'source-reviews/q170-whole-source-20261030-v1'
    manifest = read_json(folder/'manifest.json')
    pages = list(range(1,21))
    if any(any(value[k]!=doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256'))
           for value in (census,findings,manifest)):
        raise ValueError('Frozen source identities changed')
    proxies = [p for p in manifest['files'] if p.get('overview')]
    if (census['native_prose_read_pages']!=pages or findings['checked_physical_pages']!=pages or
            [p for g in findings['overviews_actually_checked'] for p in g['pages']]!=pages or
            [p['overview'] for p in proxies]!=[g['file'] for g in findings['overviews_actually_checked']] or
            len(proxies)!=7):
        raise ValueError('Actual full-page review coverage differs')
    for item in manifest['files']:
        for field,sha in (('native_text','native_text_sha256'),('raw_png','raw_png_sha256'),('overview','sha256')):
            if item.get(field) and file_hash(folder/item[field])!=item[sha]:
                raise ValueError('Checked source evidence changed')
    if any(p['bytes']>450000 or (folder/p['overview']).stat().st_size!=p['bytes'] for p in proxies):
        raise ValueError('Proxy transport guard differs')
    records = rows(work/'artifacts/corpus/manifest.jsonl')
    team = re.compile(r'(?<!\d)9089(?!\d)')
    matching = [r for r in records if team.search(r['file_name'])]
    source = Path(read_json(root/'scope.json')['source_root'])
    inventory = [p for p in source.rglob('*9089*') if p.is_file()]
    exact = [p for p in inventory if team.search(p.name)]
    if (len(records)!=604 or len(matching)!=1 or matching[0]['sha256']!=doc['source_sha256'] or
            len(exact)!=1 or file_hash(exact[0])!=doc['source_sha256']):
        raise ValueError('Local alternative-source inventory changed')
    independent = root/'papers'/doc['paper_id']/'raw/pdftotext.bin'
    if re.search(r'\b(?:abstract|summary)\b',independent.read_bytes().decode('utf-8','strict'),re.I):
        raise ValueError('Unreviewed independent abstract/summary occurrence')
    proof = {'schema':'source-absence-review-v1',
        **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'role':'abstract','reviewer':findings['reviewer'],'page_count':20,'checked_pages':pages,
        'reason':findings['whole_source_abstract_finding']+' Source-local only, not external completeness or whole-paper fidelity.',
        'full_native_prose_read':True,'physical_page_heading_layout_checked':True,
        'independent_text_check':{'path':f"papers/{doc['paper_id']}/raw/pdftotext.bin",'sha256':file_hash(independent),
            'status':'Strict UTF-8; zero Abstract/Summary word occurrences. Not a whole-text fidelity certificate.'},
        'alternative_copy_check':{'manifest_sha256':file_hash(work/'artifacts/corpus/manifest.jsonl'),
            'manifest_records':len(records),'matching_file_count':len(exact),
            'substring_candidates':[{'relative_path':p.relative_to(source).as_posix(),'sha256':file_hash(p),
                                     'same_team_token':bool(team.search(p.name))} for p in inventory],
            'result':'All604 records and local filename candidates checked; only the same20-page source.'},
        'evidence':[
            {'path':str(folder/'manifest.json'),'bundle_root':str(folder),'sha256':file_hash(folder/'manifest.json'),
             'description':'All20 native texts/source rasters; all7 bounded overviews actually inspected for headings/layout.'},
            {'path':str(census_path),'sha256':file_hash(census_path),'description':'Earlier full native-prose reading; old pending-image limitation preserved.'},
            {'path':str(findings_path),'sha256':file_hash(findings_path),'description':'Later actual complete heading/layout check.'}],
        'application_status':'Staged for a new immutable generation; no parent/history/progress modified.',
        'formula_verification':'paused','figure_distillation':'paused'}
    json_new(output,proof)
    prepared,copies = prepare_absence_reviews([output])
    apply_absence_reviews(copy.deepcopy(doc),prepared)
    print({'paper_id':doc['paper_id'],'source_checked_pages':20,'portable_evidence_files':len(copies),
           'abstract_absence':'staged source-local only','whole_paper_acceptance':False})


if __name__ == '__main__':
    main()
