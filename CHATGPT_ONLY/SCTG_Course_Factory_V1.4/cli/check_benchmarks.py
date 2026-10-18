#!/usr/bin/env python3
"""Confirm both read-only Claude benchmarks are byte-for-byte unchanged."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'benchmarks/MANIFEST.json'
def check():
    m=json.loads(MANIFEST.read_text(encoding='utf-8'));errs=[]
    if [x['id'] for x in m['references']]!=['NUM09','NUM10']:errs.append('Expected independent NUM09 + NUM10 refs')
    for ent in m['references']:
        p=ROOT/'benchmarks'/ent['path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=ent['sha256']:errs.append(f"Benchmark changed/missing: {ent['id']}")
        if ent.get('source_zip'):
            q=ROOT/'benchmarks'/ent['source_zip']
            if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=ent['source_zip_sha256']:errs.append('Source ZIP changed')
    return errs
if __name__=='__main__':
    problems=check();print('BENCHMARKS: '+('VERIFIED' if not problems else 'FAILED'));[print(' - '+x) for x in problems]
    raise SystemExit(2 if problems else 0)
