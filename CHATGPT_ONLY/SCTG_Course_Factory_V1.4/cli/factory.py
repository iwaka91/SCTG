#!/usr/bin/env python3
"""SCTG Course Factory for ChatGPT: scaffold, one-file packager, and fail-closed release."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
from visual_gate import verify as verify_visual_gates
from check_benchmarks import check as check_benchmarks
ROOT=Path(__file__).resolve().parents[1]

def init_course(args):
    code=args.code.strip().upper()
    if not re.fullmatch(r'[A-Z0-9_-]{3,40}',code):raise SystemExit('Code must have 3–40 ASCII letters/digits/_/-')
    dest=ROOT/'courses'/code
    if dest.exists(): raise SystemExit(f'Already exists: {dest}')
    errors=check_benchmarks()
    if errors:raise SystemExit('Benchmark integrity failure: '+', '.join(errors))
    dest.mkdir(parents=True)
    (dest/'course.html').write_text((ROOT/'starter/course.html').read_text(encoding='utf-8').replace('{{COURSE_CODE}}',code).replace('{{COURSE_TITLE}}',args.title),encoding='utf-8')
    (dest/'course.js').write_text((ROOT/'starter/course.js').read_text(encoding='utf-8').replace('{{COURSE_CODE}}',code).replace('{{SERIES}}',args.series),encoding='utf-8')
    (dest/'course.css').write_text((ROOT/'starter/course.css').read_text(encoding='utf-8'),encoding='utf-8')
    profile=json.loads((ROOT/'profiles/SCHEMA_TEMPLATE.json').read_text(encoding='utf-8'))
    profile['title']=f'{code}: {args.title}'
    (dest/'qa-profile.json').write_text(json.dumps(profile,ensure_ascii=False,indent=2),encoding='utf-8')
    (dest/'DESIGN_BRIEF.md').write_text(f'# {code} — {args.title}\n\n**Series:** {args.series}\n\n## TP & Uji Kelayakan\nTuliskan 1–3 TP, peta mengajar–melatih–menguji, CP/kerangka AKM, dan bukti kelayakan.\n\n## Art direction\nPalet, komposisi, storyboard 4–6 beat untuk dua sinematik, keunikan dunia.\n\n## Game design\nBuat minimal 3 calon MEKANIK berbeda sebelum memilih satu. Game utama WAJIB kendali bermakna (gerak/geser navigasi, target, benturan, rute, sumber daya, atau ruang yang berubah) dan BUKAN kuis berkostum. Jelaskan state, konsekuensi, menang/coba lagi, ketergantungan pada TP, dan Jeda Paham bila refleks.\n\n## Penilaian visual\nBandingkan dengan benchmark NUM09 + NUM10 tanpa menyalin identitas tematiknya.\n\n## Sinematik\nTipografi besar, fokus di tengah, transisi mulus, kamera/objek bergerak, dan CTA terpisah. Sesuaikan dengan TP.\n',encoding='utf-8')
    (dest/'VISUAL_BLUEPRINT.md').write_text((ROOT/'docs/VISUAL_BLUEPRINT_TEMPLATE.md').read_text(encoding='utf-8').replace('[KODE COURSE]',code),encoding='utf-8')
    print(f'Created: {dest}\nNext: complete DESIGN_BRIEF + VISUAL_BLUEPRINT, implement all steps, QA + five Ya/Tidak gates. NOT a finished course.')

def package(args):
    src=Path(args.src).resolve();dst=Path(args.out).resolve()
    if src.is_dir(): src=src/'course.html'
    if not src.exists():raise SystemExit(f'Source missing: {src}')
    html=src.read_text(encoding='utf-8')
    if '<!-- SCTG:CORE -->' not in html: raise SystemExit('Missing <!-- SCTG:CORE --> placeholder; cannot package safely.')
    errors=check_benchmarks()
    if errors:raise SystemExit('Benchmark integrity failure: '+', '.join(errors))
    css=(ROOT/'engine/sctg-layout.css').read_text(encoding='utf-8')+'\n'+(ROOT/'engine/sctg-visual.css').read_text(encoding='utf-8')+'\n'+(ROOT/'engine/sctg-cinematic-typography.css').read_text(encoding='utf-8')+'\n'+(src.parent/'course.css').read_text(encoding='utf-8')
    js=(ROOT/'engine/sctg-core.js').read_text(encoding='utf-8')+'\n'+(ROOT/'engine/sctg-cinematic.js').read_text(encoding='utf-8')+'\n'+(ROOT/'engine/sctg-performance.js').read_text(encoding='utf-8')+'\n'+(ROOT/'engine/sctg-visual.js').read_text(encoding='utf-8')+'\n'+(ROOT/'engine/sctg-steering.js').read_text(encoding='utf-8')+'\n'+(src.parent/'course.js').read_text(encoding='utf-8')
    html=html.replace('<!-- SCTG:CSS -->','<style>\n'+css+'\n</style>')
    html=html.replace('<!-- SCTG:CORE -->','<script>\n'+js.replace('</script','<\\/script')+'\n</script>')
    if re.search(r'<!-- SCTG:',html):raise SystemExit('Unresolved build markers')
    dst.parent.mkdir(parents=True,exist_ok=True);dst.write_text(html,encoding='utf-8')
    print(f'Built single HTML: {dst} ({dst.stat().st_size:,} bytes)')

def release(args):
    report_path=Path(args.report).resolve(); html=Path(args.html).resolve(); out=Path(args.out).resolve()
    if not report_path.exists() or not html.exists():raise SystemExit('Missing HTML or QA report')
    errors=check_benchmarks()
    if errors:raise SystemExit('RELEASE BLOCKED: benchmark integrity failure: '+', '.join(errors))
    report=json.loads(report_path.read_text(encoding='utf-8'))
    if report.get('status')!='FINAL_CANDIDATE_QA_PASSED':
        raise SystemExit(f'RELEASE BLOCKED: QA status={report.get("status")}. Run full QA and resolve every FAIL/BLOCKED.')
    if Path(report.get('html','')).resolve()!=html:raise SystemExit('RELEASE BLOCKED: QA evaluated a different HTML file')
    if report.get('sha256') != hashlib.sha256(html.read_bytes()).hexdigest():raise SystemExit('RELEASE BLOCKED: HTML was modified after QA')
    if report.get('transport') != 'http':raise SystemExit('RELEASE BLOCKED: sandbox simulation cannot certify real localStorage')
    if not args.visual_review:raise SystemExit('RELEASE BLOCKED: five binary gates evidence not supplied --visual-review')
    ready,issues=verify_visual_gates(html,args.visual_review)
    if not ready:raise SystemExit('RELEASE BLOCKED: five Ya/Tidak gates: '+ '; '.join(issues))
    raw=html.read_text(encoding='utf-8')
    for marker in ('TODO:', 'PLACEHOLDER', 'BELUM DIIMPLEMENTASIKAN', '<!-- SCTG:'):
        if marker in raw:raise SystemExit(f'RELEASE BLOCKED: unfinished marker {marker}')
    out.mkdir(parents=True,exist_ok=True)
    target=out/'index.html';shutil.copy2(html,target)
    shutil.copy2(args.visual_review,out/'visual-review.json')
    shutil.copy2(report_path,out/'qa-result.json')
    if (report_path.parent/'QA_REPORT.md').exists():shutil.copy2(report_path.parent/'QA_REPORT.md',out/'QA_REPORT.md')
    review=json.loads(Path(args.visual_review).read_text(encoding='utf-8'))
    for gate in review['gates'].values():
        for rel in gate.get('evidence',[]):
            srcfile=(Path(args.visual_review).parent/rel).resolve()
            dstfile=out/rel
            dstfile.parent.mkdir(parents=True,exist_ok=True)
            if not dstfile.exists():shutil.copy2(srcfile,dstfile)
    (out/'RELEASE_INFO.md').write_text('# Final Candidate — SCTG V4.3 / Factory V1.4\n\nFull browser QA and five binary Ya/Tidak gates passed on this HTML. Golden references NUM09 + NUM10 unchanged. Rating subjective is given only by Toto Gutomo after review. Android/IFP field verification is separate. No automatic visual score.\n',encoding='utf-8')
    print(f'FINAL CANDIDATE PACKAGE: {target}\nNot automatically deployed.')

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(required=True,dest='cmd')
    init=sub.add_parser('init');init.add_argument('code');init.add_argument('--title',required=True);init.add_argument('--series',choices=('SEJ','LIT','NUM','BANG'),required=True);init.set_defaults(func=init_course)
    pack=sub.add_parser('build');pack.add_argument('--src',required=True);pack.add_argument('--out',required=True);pack.set_defaults(func=package)
    release_p=sub.add_parser('release');release_p.add_argument('--html',required=True);release_p.add_argument('--report',required=True);release_p.add_argument('--out',required=True);release_p.add_argument('--visual-review',type=Path,required=True);release_p.set_defaults(func=release)
    args=p.parse_args();args.func(args)
if __name__=='__main__':main()
