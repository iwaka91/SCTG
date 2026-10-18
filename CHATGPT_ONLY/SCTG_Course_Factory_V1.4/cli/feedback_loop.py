#!/usr/bin/env python3
"""Create a truthful, traceable user-evaluation ledger entry for one course.

Does not assign ratings or change course source; human supplies actual values.
Factory improvements are recorded and later tested explicitly, not 'learned' magically.
"""
import argparse
from datetime import datetime, timezone
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def record(course,version,technical,visual,rating,notes,out=None):
    if not re.fullmatch(r'[A-Z0-9_-]{3,40}',course):raise ValueError('Invalid course code')
    if technical not in ('lulus','belum_lulus'):raise ValueError('Technical status must be stated')
    for n in (visual,rating):
        if not 0 <= float(n) <= 10:raise ValueError('Rating out of 0–10')
    if len(notes.strip())<40:raise ValueError('Human review notes must be specific')
    destination=Path(out) if out else ROOT/'feedback'/f'{course}_{version}_review.json'
    if destination.exists():raise FileExistsError('Never overwrite prior review: '+str(destination))
    destination.parent.mkdir(parents=True,exist_ok=True)
    entry={'schema':'SCTG-FEEDBACK-1.0','course':course,'version':version,
        'received_at_utc':datetime.now(timezone.utc).isoformat(),
        'technical_user_verdict':technical,'visual_user_rating':float(visual),
        'overall_user_rating':float(rating),'user_notes':notes,
        'factory_lessons':[],'changes_implemented':[],'regression_tests':[],
        'status':'review_recorded',
        'notice':'Never auto-fabricate course ratings or infer that publication/deployment occurred.'}
    destination.write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return destination
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--course',required=True);p.add_argument('--version',required=True)
    p.add_argument('--technical',choices=['lulus','belum_lulus'],required=True)
    p.add_argument('--visual',type=float,required=True);p.add_argument('--rating',type=float,required=True)
    p.add_argument('--notes',required=True);p.add_argument('--out',type=Path)
    a=p.parse_args()
    print(record(a.course,a.version,a.technical,a.visual,a.rating,a.notes,a.out))
