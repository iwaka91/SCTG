#!/usr/bin/env python3
"""SCTG V4.3: browser-backed release gate. Never equate a rendered DOM with a playable course.

Usage: python cli/qa.py --html courses/NUM01/index.html --profile courses/NUM01/qa-profile.json --out reports/NUM01
Requires Python playwright + Chromium. No online requests used.
"""
import argparse
import contextlib
import datetime as dt
import functools
import hashlib
import http.server
import json
import math
import os
from pathlib import Path
import re
import shutil
import socketserver
import threading
import time
from typing import Any
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

ROOT=Path(__file__).resolve().parents[1]
MATRIX=[
 ('Genggam_360x560',360,560),('Genggam_390x700',390,700),('Genggam_430x780',430,780),
 ('Genggam_600x900',600,900),('Genggam_768x1024',768,1024),
 ('Panggung_1024x768',1024,768),('Panggung_1366x768',1366,768),
 ('Panggung_1920x1080',1920,1080),('Panggung_1280x650',1280,650),
 ('Batas_899x700',899,700),('Batas_900x499',900,499),('Batas_900x500',900,500),
 ('LandscapeHP_800x360',800,360)
]
REQUIRED_SCENES=['cover','reading','game','typing','silent','boss','certificate']
REQUIRED_FLOWS=['normal','ez','fasil','reset','resume']
REQUIRED_MANUAL=['pedagogy','visual','game_feel','cinematic','accessibility']
MAX_TIMEOUT=5000

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address=True
    daemon_threads=True

@contextlib.contextmanager
def serve(directory):
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,directory=str(directory),**kwargs)
        def log_message(self,*args): pass
    with Server(('127.0.0.1',0),Quiet) as httpd:
        thread=threading.Thread(target=httpd.serve_forever,daemon=True)
        thread.start()
        try: yield f'http://127.0.0.1:{httpd.server_address[1]}'
        finally: httpd.shutdown();thread.join(timeout=3)

def result(scope, status, description, evidence=None):
    return {'scope':scope,'status':status,'description':description,'evidence':evidence}

def act(page, steps, errors, label='setup'):
    """Declarative actions, no eval or arbitrary script injection in profiles."""
    for idx, a in enumerate(steps):
        kind=a.get('action')
        try:
            if kind=='click': page.locator(a['selector']).first.click(timeout=int(a.get('timeout_ms',MAX_TIMEOUT)))
            elif kind=='fill': page.locator(a['selector']).first.fill(str(a['value']),timeout=MAX_TIMEOUT)
            elif kind=='check': page.locator(a['selector']).first.check(timeout=MAX_TIMEOUT)
            elif kind=='select': page.locator(a['selector']).first.select_option(str(a['value']),timeout=MAX_TIMEOUT)
            elif kind=='press': page.locator(a['selector']).first.press(a['key'],timeout=MAX_TIMEOUT)
            elif kind=='wait': page.wait_for_timeout(min(30000,int(a.get('ms',500))))
            elif kind=='text':
                actual=page.locator(a['selector']).first.inner_text(timeout=MAX_TIMEOUT)
                if a['contains'] not in actual: raise AssertionError(f"Expected '{a['contains']}', got '{actual[:180]}'")
            elif kind=='visible':
                if not page.locator(a['selector']).first.is_visible(): raise AssertionError('Element not visible')
            elif kind=='tap':
                rect=page.locator(a['selector']).first.bounding_box()
                if not rect: raise AssertionError('Element has no bounding box')
                x=rect['x']+rect['width']*float(a.get('x',.5));y=rect['y']+rect['height']*float(a.get('y',.5))
                page.mouse.click(x,y)
            else: raise ValueError(f'Unsupported action: {kind}')
        except Exception as e:
            errors.append(f'{label} #{idx+1} {kind}: {str(e)[:260]}')
            return False
    return True

def measurement(page):
    return page.evaluate('''() => {
      const e=document.documentElement, b=document.body, w=innerWidth,h=innerHeight;
      const top=[...document.querySelectorAll('body *')]
        .filter(x=>{const r=x.getBoundingClientRect();return r.width>0&&r.height>0&&(r.left < -1 || r.right > w+1)})
        .filter(x=>getComputedStyle(x).position!=='fixed'&&getComputedStyle(x).visibility!=='hidden')
        .slice(0,8).map(x=>({tag:x.tagName,id:x.id,cls:String(x.className).slice(0,70),left:Math.round(x.getBoundingClientRect().left),right:Math.round(x.getBoundingClientRect().right)}));
      return {width:w,height:h,scrollWidth:e.scrollWidth,bodyScrollWidth:b.scrollWidth,
        scrollHeight:e.scrollHeight,overflowX:Math.max(e.scrollWidth,b.scrollWidth)-w,
        overflowY:e.scrollHeight-h,oversizeElements:top};
    }''')

def canvas_has_paint(page,sel):
    return page.locator(sel).first.evaluate('''el => {
      if(!(el instanceof HTMLCanvasElement))return {ok:false,error:'not canvas'};
      if(el.width<16||el.height<16)return {ok:false,error:'canvas too small',width:el.width,height:el.height};
      try{
        const ctx=el.getContext('2d',{willReadFrequently:true});
        const data=ctx.getImageData(0,0,el.width,el.height).data;
        let count=0; const shades=new Set(); const step=Math.max(1,Math.floor((el.width*el.height)/800));
        for(let p=0;p<el.width*el.height;p+=step){const i=p*4;if(data[i+3]>8){count++;shades.add([data[i]>>5,data[i+1]>>5,data[i+2]>>5].join(','));}}
        return {ok:count>=5&&shades.size>=3,alphaSamples:count,shades:shades.size,width:el.width,height:el.height};
      }catch(e){return {ok:false,error:String(e)}}
    }''')

def bootstrap(page,html_source,source_url=None,transport='http'):
    if transport=='http':
        if not source_url:raise RuntimeError('HTTP transport requires local server URL')
        page.goto(source_url,wait_until='domcontentloaded',timeout=15000)
    else:
        # Restricted sandbox environments block file:// and localhost navigation.
        # Storage emulation is only suitable for regression triage, never release certification.
        page.evaluate("""() => {
          const data={};
          const mock={getItem:k=>Object.prototype.hasOwnProperty.call(data,k)?data[k]:null,
            setItem:(k,v)=>data[k]=String(v),removeItem:k=>delete data[k],clear:()=>Object.keys(data).forEach(k=>delete data[k]),key:i=>Object.keys(data)[i]||null};
          Object.defineProperty(window,'localStorage',{configurable:true,value:mock});
          Object.defineProperty(window,'sessionStorage',{configurable:true,value:mock});
        }""")
        page.set_content(html_source,wait_until='domcontentloaded',timeout=15000)
    page.wait_for_timeout(150)

def run_scene(page,html_source,source_url,transport,scene_name,spec,label,output,shot=True):
    errors=[]
    bootstrap(page,html_source,source_url,transport)
    if not act(page,spec.get('actions',[]),errors,scene_name):
        return [result(f'{scene_name}/{label}','FAIL','Failed to navigate to scene',errors)]
    page.wait_for_timeout(int(spec.get('settle_ms',180)))
    m=measurement(page)
    findings=[]
    if m['overflowX']>1:
        findings.append(result(f'{scene_name}/{label}','FAIL',f"Horizontal overflow = {m['overflowX']}px",m))
    else:
        findings.append(result(f'{scene_name}/{label}','PASS','No horizontal document overflow',m))
    if spec.get('no_page_scroll') and m['overflowY']>1:
        findings.append(result(f'{scene_name}/{label}','FAIL',f"Vertical page scrolling in game/reading = {m['overflowY']}px",m))
    elif spec.get('no_page_scroll'):
        findings.append(result(f'{scene_name}/{label}','PASS','No vertical document scroll',m))
    if spec.get('target'):
        target=page.locator(spec['target']).first
        try:
            if not target.is_visible(): raise AssertionError('target hidden')
            findings.append(result(f'{scene_name}/{label}','PASS','Target visible'))
        except Exception as e: findings.append(result(f'{scene_name}/{label}','FAIL','Target not visible',str(e)))
    if spec.get('canvas'):
        try:
            c=canvas_has_paint(page,spec['canvas'])
            findings.append(result(f'{scene_name}/{label}','PASS' if c['ok'] else 'FAIL','Canvas painted with diverse colors' if c['ok'] else 'Canvas blank/invalid',c))
        except Exception as e: findings.append(result(f'{scene_name}/{label}','FAIL','Canvas check crashed',str(e)))
    if 'typing' in spec:
        target=spec['typing']; selector=target.get('selector')
        try:
            el=page.locator(selector).first
            el.focus();el.fill('Tes keyboard tetap aktif ABC123')
            before=el.input_value()
            page.set_viewport_size({'width':m['width'],'height':max(330,m['height']-260)})
            page.wait_for_timeout(300)
            after=page.locator(selector).first.input_value()
            active=page.locator(selector).first.evaluate('(el)=>document.activeElement===el')
            passed=(before==after and active)
            findings.append(result(f'{scene_name}/{label}','PASS' if passed else 'FAIL','Keyboard resize retains input focus and unsubmitted value',{'before':before,'after':after,'focusRetained':active}))
            page.set_viewport_size({'width':m['width'],'height':m['height']})
        except Exception as e:
            findings.append(result(f'{scene_name}/{label}','FAIL','Keyboard test failed',str(e)))
    if spec.get('silent'):
        conf=spec['silent']; target=conf['button'];seconds=float(conf.get('observe_seconds',3.5))
        try:
            page.evaluate('''() => {window.__sctg_qa={scroll:0,sounds:0,focus:0};
              const orig=window.scrollTo.bind(window);window.scrollTo=(...a)=>{window.__sctg_qa.scroll++;return orig(...a)};
              document.addEventListener('focusin',()=>window.__sctg_qa.focus++);
              const A=window.AudioContext||window.webkitAudioContext;
              if(A&&A.prototype.createOscillator){const f=A.prototype.createOscillator;A.prototype.createOscillator=function(...a){window.__sctg_qa.sounds++;return f.apply(this,a)}};
            }''')
            page.wait_for_timeout(int(seconds*1000))
            st=page.evaluate('window.__sctg_qa')
            enabled=page.locator(target).first.is_enabled()
            passed=(st['scroll']==0 and st['sounds']==0 and st['focus']==0 and enabled)
            findings.append(result(f'{scene_name}/{label}','PASS' if passed else 'FAIL','Timer unlock silent without scroll, focus jump or sound',{'calls':st,'enabled':enabled}))
        except Exception as e: findings.append(result(f'{scene_name}/{label}','FAIL','Silent timer probe failed',str(e)))
    if spec.get('download'):
        conf=spec['download']
        try:
            with page.expect_download(timeout=10000) as ev:
                page.locator(conf['selector']).first.click(timeout=5000)
            file=ev.value; data=file.path().read_bytes()
            ok=file.suggested_filename.lower().endswith('.pdf') and data.startswith(b'%PDF-') and b'%%EOF' in data[-1024:] and len(data)>=100
            findings.append(result(f'{scene_name}/{label}','PASS' if ok else 'FAIL','PDF is downloadable and has valid signature/trailer',{'filename':file.suggested_filename,'bytes':len(data)}))
        except Exception as e:findings.append(result(f'{scene_name}/{label}','FAIL','PDF download verification failed',str(e)))
    if spec.get('touch_targets'):
        for sel in spec['touch_targets']:
            try:
                b=page.locator(sel).first.bounding_box();minimum=56 if label.startswith('Panggung') else 48
                ok=b is not None and b['height']>=minimum and b['width']>=minimum
                findings.append(result(f'{scene_name}/{label}','PASS' if ok else 'FAIL',f'Touch target >= {minimum}px for {sel}',b))
            except Exception as e:findings.append(result(f'{scene_name}/{label}','FAIL','Touch target inspection failed',str(e)))
    if spec.get('interaction'):
        conf=spec['interaction']
        try:
            before=page.locator(conf['watch']).first.inner_text()
            rect=page.locator(conf['selector']).first.bounding_box()
            page.mouse.click(rect['x']+rect['width']*float(conf.get('x',.5)),rect['y']+rect['height']*float(conf.get('y',.5)))
            page.wait_for_timeout(int(conf.get('wait_ms',500)))
            after=page.locator(conf['watch']).first.inner_text()
            ok=before!=after if conf.get('must_change',True) else True
            findings.append(result(f'{scene_name}/{label}','PASS' if ok else 'FAIL','Input produces observable game state change',{'before':before[:90],'after':after[:90]}))
        except Exception as e:findings.append(result(f'{scene_name}/{label}','FAIL','Game interaction probe failed',str(e)))
    if shot:
        try:
            png=output/f'{scene_name}_{label}.png';page.screenshot(path=str(png),full_page=False,animations='disabled')
        except Exception as e:findings.append(result(f'{scene_name}/{label}','FAIL','Screenshot failed',str(e)))
    return findings

def report_json(report,out):
    out.mkdir(parents=True,exist_ok=True)
    (out/'qa-result.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    lines=[f'# SCTG QA — {report["course"]}', '', f'**Status:** {report["status"]}', f'**Date:** {report["timestamp"]}', '',
           '## Auto gate', '', '| Gate | PASS | FAIL | BLOCKED |', '|---|---:|---:|---:|']
    by={}
    for item in report['findings']:
        gate=item['scope'].split('/')[0];by.setdefault(gate,{'PASS':0,'FAIL':0,'BLOCKED':0})[item['status']]+=1
    for key,v in by.items(): lines.append(f'| {key} | {v["PASS"]} | {v["FAIL"]} | {v["BLOCKED"]} |')
    lines+=['','## Kegagalan dan hal yang belum teruji','']
    for item in report['findings']:
        if item['status']!='PASS':lines.append(f'- **{item["status"]}** {item["scope"]}: {item["description"]}'+(f' — `{str(item["evidence"])[:400]}`' if item.get('evidence') else ''))
    if all(i['status']=='PASS' for i in report['findings']):lines.append('Tidak ada kegagalan pada cakupan otomatis yang dijalankan. Penilaian estetika tetap membutuhkan pemeriksaan manusia.')
    lines+=['','## Batas verifikasi','',
        '- Browser headless bukan pengganti uji Android fisik / IFP fisik.',
        '- Canvas berwarna tidak membuktikan game playable; skenario game harus membuktikan respons input.',
        '- Skor estetika 9,8/10 tidak dapat dihasilkan otomatis secara jujur.',
        '- Pemeriksaan PDF harus melalui skenario unduh + pemeriksaan berkas valid; tanpa skenario status tetap BLOCKED.',
        '- Screenshot Tahap A wajib dinilai secara visual, bukan hanya dibuat.', '']
    (out/'QA_REPORT.md').write_text('\n'.join(lines),encoding='utf-8')

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--html',required=True,type=Path)
    ap.add_argument('--profile',type=Path)
    ap.add_argument('--out',required=True,type=Path)
    ap.add_argument('--fast',action='store_true',help='Test 390x700, 1280x650, 900x500 only. Never qualifies as full release QA.')
    ap.add_argument('--transport',choices=['http','sandbox'],default='http',help='http=real localhost origin for release; sandbox=mock storage, restricted environments only, always BLOCKED')
    args=ap.parse_args(argv)
    html=args.html.resolve();out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
    if not html.exists():ap.error(f'HTML not found: {html}')
    profile=json.loads(args.profile.read_text(encoding='utf-8')) if args.profile else {}
    findings=[]
    raw=html.read_text(encoding='utf-8')
    if '<meta name="viewport"' not in raw.lower():findings.append(result('static','FAIL','Missing viewport meta'))
    else:findings.append(result('static','PASS','Viewport metadata present'))
    external=re.findall(r'<(?:script|link)[^>]+(?:src|href)\s*=\s*["\'](https?://[^"\']+)',raw,re.I)
    if external:findings.append(result('static','FAIL','External scripts or styles in single-file product',external))
    else:findings.append(result('static','PASS','No external scripts or styles'))
    if '<html' not in raw.lower() or '</html>' not in raw.lower():findings.append(result('static','FAIL','Invalid document structure'))
    for marker in ('TODO:', 'PLACEHOLDER', 'BELUM DIIMPLEMENTASIKAN', '<!-- SCTG:'):
        if marker in raw: findings.append(result('static','FAIL','Unfinished content marker found',marker))
    matrix=MATRIX if not args.fast else [x for x in MATRIX if x[0] in ('Genggam_390x700','Panggung_1280x650','Batas_900x500')]
    capture={'cover':{'Genggam_390x700','Panggung_1280x650'},'game':{'Genggam_390x700','Panggung_1280x650'},'reading':{'Panggung_1280x650'},'boss':{'Genggam_390x700'},'cinematic':{'Genggam_390x700'}}
    server_manager=serve(html.parent) if args.transport=='http' else contextlib.nullcontext(None)
    with server_manager as server, sync_playwright() as p:
        browser=p.chromium.launch(executable_path=os.getenv('CHROMIUM_PATH') or shutil.which('chromium') or None,headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
        for name,sc in profile.get('scenes',{}).items():
            if not isinstance(sc,dict) or not sc.get('target'):
                findings.append(result(f'{name}/profile','BLOCKED','Scene lacks a target selector and/or actions'))
                continue
            # Cover and game on entire requested matrix; other scenes only at relevant sizes but still observable.
            relevant=matrix if name in ('cover','game') else [x for x in matrix if x[0] in ('Genggam_390x700','Panggung_1280x650')]
            for label,w,h in relevant:
                context=browser.new_context(viewport={'width':w,'height':h},device_scale_factor=1)
                page=context.new_page();js_errors=[]
                page.on('pageerror',lambda error:js_errors.append(str(error)))
                shot=label in capture.get(name,set())
                findings.extend(run_scene(page,raw,f'{server}/{html.name}' if server else None,args.transport,name,sc,label,out,shot))
                if js_errors:findings.append(result(f'{name}/{label}','FAIL','Uncaught JavaScript errors',js_errors[:8]))
                else:findings.append(result(f'{name}/{label}','PASS','No uncaught JS errors'))
                context.close()
        for flowname,spec in profile.get('flows',{}).items():
            context=browser.new_context(viewport={'width':390,'height':700})
            page=context.new_page();errors=[];js_errors=[]
            page.on('pageerror',lambda e:js_errors.append(str(e)))
            bootstrap(page,raw,f'{server}/{html.name}' if server else None,args.transport)
            ok=act(page,spec.get('actions',[]),errors,flowname)
            if ok and spec.get('assert'):
                ok=act(page,spec['assert'],errors,flowname+' assertions')
            if js_errors:ok=False;errors.extend(js_errors)
            findings.append(result(f'flow/{flowname}','PASS' if ok else 'FAIL','Browser flow complete' if ok else 'Flow failed',errors or None))
            context.close()
        browser.close()
    # Strict coverage gate: required names cannot silently go missing.
    for name in REQUIRED_SCENES:
        spec=profile.get('scenes',{}).get(name)
        if not spec:
            findings.append(result(f'{name}/coverage','BLOCKED','Required scene missing from QA profile'))
        else:
            cap={'game':'interaction','typing':'typing','silent':'silent','certificate':'download','boss':'interaction','reading':'no_page_scroll'}
            if name in cap and not spec.get(cap[name]):
                findings.append(result(f'{name}/coverage','BLOCKED',f'Required behavioral probe missing: {cap[name]}'))
    if profile.get('cinematics',True) and not profile.get('scenes',{}).get('cinematic'):
        findings.append(result('cinematic/coverage','BLOCKED','Cinematic scene must be checked unless explicitly not used in design'))
    for name in REQUIRED_FLOWS:
        flow=profile.get('flows',{}).get(name)
        if not flow or not flow.get('actions') or not flow.get('assert'):
            findings.append(result(f'flow/{name}','BLOCKED','Required end-to-end flow/assertions missing from QA profile'))
    for name in REQUIRED_MANUAL:
        if name not in profile.get('manual_review',{}):findings.append(result(f'manual/{name}','BLOCKED','Human/AI visual or pedagogy review absent'))
        else:
            item=profile['manual_review'][name]
            if isinstance(item,dict) and item.get('status')=='approved' and item.get('evidence'):
                findings.append(result(f'manual/{name}','PASS','Review evidenced',item['evidence']))
            else:findings.append(result(f'manual/{name}','BLOCKED','Review not approved with evidence'))
    if args.fast:findings.append(result('matrix','BLOCKED','Fast subset is not full SCTG matrix'))
    if args.transport=='sandbox':findings.append(result('origin','BLOCKED','Sandbox uses simulated localStorage; native persistence and downloads not certified'))
    status='FINAL_CANDIDATE_QA_PASSED' if findings and all(x['status']=='PASS' for x in findings) else 'NOT_RELEASE_READY'
    report={'course':profile.get('title',html.stem),'html':str(html),'timestamp':dt.datetime.now(dt.timezone.utc).isoformat(),
            'status':status,'sha256':hashlib.sha256(html.read_bytes()).hexdigest(),'transport':args.transport,'matrix':matrix,'findings':findings,'summary':{k:sum(x['status']==k for x in findings) for k in ('PASS','FAIL','BLOCKED')}}
    report_json(report,out)
    print(f'[{status}] PASS={report["summary"]["PASS"]} FAIL={report["summary"]["FAIL"]} BLOCKED={report["summary"]["BLOCKED"]}')
    print(f'Report: {out/"QA_REPORT.md"}')
    return 0 if status=='FINAL_CANDIDATE_QA_PASSED' else 2

if __name__=='__main__':raise SystemExit(main())
