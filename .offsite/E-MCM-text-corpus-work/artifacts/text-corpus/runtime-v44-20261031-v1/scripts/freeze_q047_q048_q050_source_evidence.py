"""Include the actually checked page/native evidence directly in staged repairs."""
from pathlib import Path

from text_corpus import file_hash,json_new,read_json


def main():
    directory=Path(__file__).resolve().parents[1]/'artifacts/text-corpus/reviews/20261031'
    names=[(47,'q047-summary-repair-v1.json','q047-summary-repair-v2.json'),
           (48,'q048-summary-repair-v1.json','q048-summary-repair-v2.json'),
           (50,'q050-summary-banner-repair-v1.json','q050-summary-banner-repair-v2.json')]
    if any((directory/new).exists() for _,_,new in names):
        raise ValueError('Create-only evidence repair exists; preserve it')
    for queue,old,new in names:
        proof=read_json(directory/old)
        proof['supersedes_staged_proof_sha256']=file_hash(directory/old)
        proof['evidence_attachment_note']='Direct portable bounded JPEG and native-page bytes included; operation text/classification unchanged.'
        folder=directory/f'q{queue:03d}-summary-page-v1'
        for name,description in [('page-0001.jpg','Actually inspected byte-bounded physical page1 JPEG for author text ownership.'),
                                 ('page-0001-native.json','Source-bound exact native line IDs, coordinates and fonts for physical page1.')]:
            path=folder/name
            proof['evidence'].append({'path':str(path),'sha256':file_hash(path),'description':description})
        json_new(directory/new,proof)
        print({'queue':queue,'new_staged_proof':new,'source_operations_unchanged':True,
               'source_fidelity_approved':False},flush=True)


if __name__=='__main__':
    main()
