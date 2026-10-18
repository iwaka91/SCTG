#!/usr/bin/env python3
"""Five binary SCTG quality gates, evidence-first; never fabricates human rating.

init: write blank questionnaire tied to an exact HTML SHA.
check: reject missing or non-binary approvals, missing local evidence, stale HTML.
This validates EVIDENCE COMPLETENESS, not beauty. Human must really inspect results.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct

GATES={
 'visual_3d':'Visual dan identitas artistik, pseudo-3D dan memanjakan mata',
 'playable_game':'Gameplay/mekanik interaktif benar-benar dapat dimainkan',
 'pedagogy_sctg43':'Pedagogi SCTG V4.3 terpenuhi',
 'cinematic_ux':'Sinematik dan pengalaman pengguna',
 'technical_accessibility':'Stabilitas teknis dan aksesibilitas'
}

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def init(html,out):
    payload={'schema':'SCTG-5-GATES-1.2','html_sha256':digest(html),'html_name':Path(html).name,
        'reference_benchmarks':['NUM09','NUM10'],
        'note':'Isian awal FAIL-CLOSED. Isi Ya/Tidak setelah melihat bukti fisik nyata. Pengguna memberikan rating SUBJEKTIF setelah 5 Ya.',
        'gates':{k:{'verdict':'belum','evidence':[],'review_notes':''} for k in GATES},
        'gameplay_proof':{k:'' for k in ('primary_mechanic','direct_player_control','world_state_change','meaningful_consequence','win_and_retry','tp_dependency','secondary_interaction')},
        'cinematic_proof':{k:'' for k in ('central_typography','smooth_transition','scene_action','beat_storyboard')},
        'user_rating':None}
    Path(out).parent.mkdir(parents=True,exist_ok=True)
    Path(out).write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return payload

def _evidence_exists(base,entry):
    if not isinstance(entry,str) or not entry.strip():return False
    p=(base/entry).resolve()
    try:p.relative_to(base.resolve())
    except ValueError:return False
    if not p.is_file() or p.stat().st_size<16:return False
    if p.suffix.lower()=='.png':
        try:
            h=p.open('rb').read(24)
            if h[:8]!=b'\x89PNG\r\n\x1a\n':return False
            w,ht=struct.unpack('>II',h[16:24])
            if w<300 or ht<240:return False
        except (OSError,ValueError,struct.error):return False
    return True

def verify(html,path):
    html,path=Path(html),Path(path)
    if not path.is_file():return False,['Form 5 gerbang belum ada']
    try:r=json.loads(path.read_text(encoding='utf-8'))
    except (ValueError,UnicodeError) as e:return False,[f'Form JSON tidak valid: {e}']
    problems=[]
    if r.get('schema')!='SCTG-5-GATES-1.2':problems.append('Schema tidak cocok')
    if r.get('html_sha256')!=digest(html):problems.append('Hash HTML berbeda dari HTML yang dinilai')
    if r.get('reference_benchmarks')!=['NUM09','NUM10']:problems.append('Harus membandingkan dengan kedua benchmark')
    gates=r.get('gates',{})
    if set(gates)!=set(GATES):problems.append('Lima gerbang tidak lengkap/punya gerbang ekstra')
    for k,desc in GATES.items():
        v=gates.get(k,{})
        if v.get('verdict')!='ya':problems.append(f'{k}: harus Ya (bukan {v.get("verdict")})')
        if len(v.get('review_notes','').strip())<35:problems.append(f'{k}: ulasan spesifik minimal 35 karakter')
        ev=v.get('evidence',[])
        if not isinstance(ev,list) or not ev:problems.append(f'{k}: bukti kosong')
        else:
            for e in ev:
                if not _evidence_exists(path.parent,e):problems.append(f'{k}: bukti tidak ada/invalid: {e}')
    # Semantic checks cannot be inferred from a screenshot: a real reviewer must
    # demonstrate that the course is played, not merely answered.
    gp=r.get('gameplay_proof',{})
    for k in ('primary_mechanic','direct_player_control','world_state_change',
              'meaningful_consequence','win_and_retry','tp_dependency','secondary_interaction'):
        v=gp.get(k,'')
        if not isinstance(v,str) or len(v.strip())<30:
            problems.append(f'GAMEPLAY: {k} needs a concrete observed description (min 30 chars)')
    cp=r.get('cinematic_proof',{})
    for k in ('central_typography','smooth_transition','scene_action','beat_storyboard'):
        v=cp.get(k,'')
        if not isinstance(v,str) or len(v.strip())<30:
            problems.append(f'CINEMATIC: {k} needs a concrete observed description (min 30 chars)')
    # User rating is optional: not manufactured or required to be scored by an automated gate.
    return not problems,problems

def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(required=True,dest='action')
    for name in ('init','check'):
        x=sub.add_parser(name);x.add_argument('--html',type=Path,required=True)
        x.add_argument('--review',type=Path,required=True)
    args=p.parse_args()
    if args.action=='init':init(args.html,args.review);print(f'Form WAITING: {args.review}')
    else:
        yes,errors=verify(args.html,args.review)
        print('5 GATES: '+('READY_FOR_USER_RATING' if yes else 'BLOCKED'))
        for error in errors:print(' -',error)
        return 0 if yes else 2
    return 0
if __name__=='__main__':raise SystemExit(main())
