/* SCTG Course Factory ChatGPT — foundation, not a visual or pedagogical substitute.
   Architectural invariants:
   - Never replace focused input on resize, visualViewport change or timer expiry.
   - Reading timer has silent completion and pauses on hidden/closed items.
   - Render active canvas only, with DPR-aware resize.
   - Do not replace course-specific gameplay with quiz dressed as game. */
(() => {
  'use strict';
  const STORE_PREFIX='sctg:v4.3:';
  const deepCopy = o => JSON.parse(JSON.stringify(o));
  function safeParse(raw, fallback) { try { return JSON.parse(raw); } catch { return fallback; } }
  const openJson = (key, fallback) => deepCopy(safeParse(localStorage.getItem(STORE_PREFIX+key), fallback));
  const saveJson = (key, data) => localStorage.setItem(STORE_PREFIX+key, JSON.stringify(data));

  // State object: merge local progress, but only from an explicit "Lanjutkan Progres" decision.
  class SessionStore {
    constructor(courseId, defaults={}) { this.id=courseId; this.defaults=deepCopy(defaults); this.state=deepCopy(defaults); }
    hasSaved() { return !!localStorage.getItem(STORE_PREFIX+this.id); }
    resume() { this.state=Object.assign(deepCopy(this.defaults), openJson(this.id, {})); return this.state; }
    save() { saveJson(this.id,this.state); }
    reset({identity=false,preferences=false}={}) {
      const keepId=identity?{}:{identity:this.state.identity};
      const keepPrefs=preferences?{}:{preferences:this.state.preferences};
      this.state=Object.assign(deepCopy(this.defaults),keepId,keepPrefs); this.save();
      return this.state;
    }
    clear() { localStorage.removeItem(STORE_PREFIX+this.id); this.state=deepCopy(this.defaults); }
  }

  // Each timer is a continuous-visibility countdown; user controls progression.
  class SilentGate {
    constructor({key, content, button, indicator, seconds, onSave=()=>{}, onDone=()=>{}, visible=()=>true, sound=()=>{}}) {
      this.key=key; this.content=content; this.button=button; this.indicator=indicator;
      this.remaining=Math.max(0,Math.ceil(seconds)); this.onSave=onSave; this.onDone=onDone;
      this.visible=visible; this.sound=sound; // sound intentionally never called on completion
      this.open=false; this.done=false; this.timer=null; this.last=0;
      this.button.disabled=true; this.button.setAttribute('aria-disabled','true');
      this.content.addEventListener('toggle', () => {
        if ('open' in this.content) this.setOpen(this.content.open);
      });
      document.addEventListener('visibilitychange',()=>{ if(document.hidden) this.pause(); else if(this.open) this.start(); });
      this.paint();
    }
    snapshot() { return {remaining:this.remaining,done:this.done}; }
    restore(st) { this.remaining=Math.max(0,Number(st?.remaining??this.remaining)); this.done=!!st?.done; this.paint(); if(this.done)this.unlock(); }
    setOpen(open) { this.open=!!open; if(this.open) this.start(); else this.pause(); }
    paint() { if(this.indicator) this.indicator.textContent=this.done?'✅':`${Math.ceil(this.remaining)} dtk`; }
    start() { if(!this.open||this.done||this.timer||document.hidden||!this.visible())return;
      this.last=performance.now();
      this.timer=setInterval(()=>this.tick(),130);
    }
    tick() {
      if(!this.open||document.hidden||!this.visible()) {this.pause();return;}
      const now=performance.now(), delta=Math.max(0,(now-this.last)/1000); this.last=now;
      const old=Math.ceil(this.remaining); this.remaining=Math.max(0,this.remaining-delta);
      if(Math.ceil(this.remaining)!==old) {this.paint();this.onSave(this.snapshot());}
      if(this.remaining<=0) this.complete();
    }
    pause() {if(this.timer)clearInterval(this.timer);this.timer=null;this.onSave(this.snapshot());}
    complete() {this.done=true;this.pause();this.unlock();this.paint();this.onSave(this.snapshot());this.onDone();}
    unlock() {this.button.disabled=false;this.button.setAttribute('aria-disabled','false'); /* DO NOT focus, toast, beep, scroll, pulse, or replace DOM. */ }
    destroy() { this.pause(); }
  }
  function readingSeconds(text, {divisor=3,min=5,fast=false}={}) {
    return fast?2:Math.max(min,Math.ceil(text.trim().split(/\s+/).filter(Boolean).length/divisor));
  }
  class StageMode {
    constructor({root=document.documentElement,onChange=()=>{}}={}) {
      this.root=root;this.onChange=onChange;this.mode=null;
      this.media=matchMedia('(orientation: landscape) and (min-width: 900px) and (min-height: 500px)');
      this.listener=()=>this.update();this.media.addEventListener('change',this.listener);this.update();
    }
    update(){const next=this.media.matches?'panggung':'genggam';if(next===this.mode)return;
      this.mode=next;this.root.dataset.sctgMode=next;this.onChange(next);
      // Never rerender the active input tree or reset state here.
    }
    destroy(){this.media.removeEventListener('change',this.listener);}
  }
  class CanvasLoop {
    constructor(canvas, render, {onTap=()=>{}, onKey=()=>{}}={}){
      this.canvas=canvas;this.ctx=canvas.getContext('2d');this.render=render;
      this.active=false;this.raf=0;this.last=0;this.w=0;this.h=0;
      this.observer=new ResizeObserver(()=>this.resize());this.observer.observe(canvas);
      this.perfListener=()=>this.resize();
      window.addEventListener('sctg-performance-change',this.perfListener);
      this.resize();
      canvas.addEventListener('pointerdown',ev=>{
        const box=canvas.getBoundingClientRect();
        onTap({x:(ev.clientX-box.left)/box.width,y:(ev.clientY-box.top)/box.height,event:ev});
      });
      canvas.tabIndex=canvas.tabIndex>=0?canvas.tabIndex:0;
      canvas.addEventListener('keydown',ev=>onKey(ev));
      document.addEventListener('visibilitychange',()=>{if(document.hidden)this.stop();});
    }
    resize(){const rect=this.canvas.getBoundingClientRect();const dpr=window.SCTGPerformance?.size(rect.width,rect.height)||Math.min(2,window.devicePixelRatio||1);
      this.w=rect.width;this.h=rect.height;
      if(this.canvas.width!==Math.round(this.w*dpr)||this.canvas.height!==Math.round(this.h*dpr)){
        this.canvas.width=Math.max(1,Math.round(this.w*dpr));this.canvas.height=Math.max(1,Math.round(this.h*dpr));
      }
      this.ctx.setTransform(dpr,0,0,dpr,0,0);
      if(this.active)this.render(this.ctx,{width:this.w,height:this.h,dt:0,time:performance.now()});
    }
    frame=(time)=>{if(!this.active)return;const dt=Math.min(.06,(time-this.last)/1000||0);this.last=time;
      if(this.w>0&&this.h>0&&(!window.SCTGPerformance||window.SCTGPerformance.shouldDraw(time,this.paintAt||0))){const before=performance.now();this.render(this.ctx,{width:this.w,height:this.h,dt,time});this.paintAt=time;window.SCTGPerformance?.observeFrame(performance.now()-before,dt*1000);}
      this.raf=requestAnimationFrame(this.frame);
    };
    start(){if(this.active)return;this.active=true;this.last=performance.now();this.resize();this.raf=requestAnimationFrame(this.frame);}
    stop(){this.active=false;if(this.raf)cancelAnimationFrame(this.raf);this.raf=0;}
    destroy(){this.stop();this.observer.disconnect();window.removeEventListener('sctg-performance-change',this.perfListener);}
  }
  class StepNavigation {
    constructor({steps,menu,onChange=()=>{},initial=1,allowAny=()=>false}) {
      this.steps=steps;this.menu=menu;this.onChange=onChange;this.allowAny=allowAny;
      this.current=initial;this.unlocked=initial;this.completed=new Set();this.open(initial,{force:true});
    }
    canOpen(n){return this.allowAny()||n<=this.unlocked;}
    open(n,{force=false}={}) {
      if(!force&&!this.canOpen(n))return false;
      this.steps.forEach((node,i)=>{node.hidden=(i+1!==n);node.classList.toggle('active',i+1===n);});
      this.current=n;this.onChange(n);return true;
    }
    complete(n){this.completed.add(n);this.unlocked=Math.max(this.unlocked,Math.min(this.steps.length,n+1));}
  }
  window.SCTGFactory=Object.freeze({SessionStore,SilentGate,StageMode,CanvasLoop,StepNavigation,readingSeconds});
})();
