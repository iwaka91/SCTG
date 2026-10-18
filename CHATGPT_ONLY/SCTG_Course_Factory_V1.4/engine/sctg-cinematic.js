/* Cinematic sequencing. Each course MUST supply ORIGINAL scene rendering and narrative. */
(() => {
  'use strict';
  class CinematicDirector {
    constructor({canvas,beats,beatLabel,continueButton,replayButton,skipButton,
      renderScene,onBeat=()=>{},onComplete=()=>{},onClose=()=>{},
      fastMode=()=>false,sound=()=>{},finishedFlag=()=>false,setFinishedFlag=()=>{}}){
      if(!Array.isArray(beats)||beats.length<4||beats.length>6)throw Error('SCTG requires 4–6 cinematic beats');
      this.canvas=canvas;this.beats=beats;this.label=beatLabel;this.continueButton=continueButton;
      this.replayButton=replayButton;this.skipButton=skipButton;this.renderScene=renderScene;
      this.onBeat=onBeat;this.onComplete=onComplete;this.onClose=onClose;
      this.fastMode=fastMode;this.sound=sound;this.finishedFlag=finishedFlag;this.setFinishedFlag=setFinishedFlag;
      this.reduced=matchMedia('(prefers-reduced-motion:reduce)').matches;
      this.current=-1;this.timer=null;this.loop=null;this.finished=false;this.enabled=false;
      this.continueButton.disabled=true;this.replayButton.addEventListener('click',()=>this.replay());
      this.continueButton.addEventListener('click',()=>this.advance());
      this.skipButton?.addEventListener('click',()=>{if(this.fastMode())this.advance(true)});
    }
    start({replay=false}={}){
      if(this.finishedFlag()&&!replay)return false;
      this.enabled=true;this.finished=false;this.current=-1;this.continueButton.disabled=true;
      if(this.skipButton)this.skipButton.hidden=!this.fastMode();
      this.loop=new window.SCTGFactory.CanvasLoop(this.canvas,(ctx,frame)=>this.renderScene(ctx,{...frame,beat:this.current,progress:this.current/Math.max(1,this.beats.length-1),reducedMotion:this.reduced}));
      this.loop.start();this.next();return true;
    }
    next(){
      clearTimeout(this.timer);this.current++;
      if(this.current>=this.beats.length){this.finish();return;}
      const raw=this.beats[this.current];const line=typeof raw==='string'?raw:(raw.variants?.[Math.floor(Math.random()*raw.variants.length)]||raw.text);
      this.label.textContent=line;
      // Animate large, centered typographic beats only when course opts into the V1.4 stage CSS.
      if(this.label.classList?.contains('sctg-cine-typography')){
        this.label.classList.remove('sctg-cine-enter');
        if(!this.reduced){void this.label.offsetWidth;this.label.classList.add('sctg-cine-enter');}
      }
      this.onBeat({index:this.current,text:line});this.sound('cinematic-beat');
      const count=line.trim().split(/\s+/).filter(Boolean).length;
      const duration=this.fastMode()?2:Math.max(3,count/2.5+1);
      this.timer=setTimeout(()=>this.next(),duration*1000);
    }
    finish(){this.finished=true;this.continueButton.disabled=false;this.setFinishedFlag(true);this.onComplete();
      // CTA remains still; do not auto-advance.
    }
    advance(skip=false){if(skip&&!this.fastMode())return;if(!skip&&!this.finished)return;
      clearTimeout(this.timer);this.loop?.destroy();this.loop=null;this.enabled=false;this.setFinishedFlag(true);this.onClose();
    }
    replay(){clearTimeout(this.timer);if(this.loop){this.loop.destroy();this.loop=null;}this.start({replay:true});}
    destroy(){clearTimeout(this.timer);this.loop?.destroy();}
  }
  window.SCTGCinematic=Object.freeze({CinematicDirector});
})();
