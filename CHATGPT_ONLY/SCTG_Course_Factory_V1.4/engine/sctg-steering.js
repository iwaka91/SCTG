/* SCTG Factory V1.4 — directional motion mechanic (not drag-and-drop).
   The pointer steers the PLAYER; learning objects remain fixed in the world.
   Course author must create new TP-aligned scenes and reflection/feedback. */
(() => {
  'use strict';
  const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
  class SteeringField {
    constructor({canvas,targets=[],hazards=[],speed=.31,onCollect=()=>{},onHazard=()=>{},onWin=()=>{},
      onState=()=>{},start={x:.5,y:.84},instructions='Arahkan penjelajah ke bukti'}={}){
      if(!canvas||!canvas.getContext)throw new Error('SteeringField requires canvas');
      this.canvas=canvas;this.ctx=canvas.getContext('2d');this.speed=speed;this.instructions=instructions;
      this.startPoint={...start};this.pos={...start};this.target=null;this.holding=null;
      this.move={x:0,y:0};this.targets=targets.map((t,i)=>({...t,id:String(t.id??i),found:false}));
      this.hazards=hazards.map((h,i)=>({...h,id:String(h.id??i)}));
      this.onCollect=onCollect;this.onHazard=onHazard;this.onWin=onWin;this.onState=onState;
      this.status='ready';this.hits=0;this.lastHazard=-100000;this.last=performance.now();this.raf=0;
      this.pointers=new Map();this.buttons=[];
      this.handleDown=e=>{if(this.status==='won')return;e.preventDefault();this.canvas.setPointerCapture?.(e.pointerId);this.pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});this.updatePointer(e);};
      this.handleMove=e=>{if(!this.pointers.has(e.pointerId))return;e.preventDefault();this.updatePointer(e);};
      this.handleUp=e=>{this.pointers.delete(e.pointerId);if(this.pointers.size===0)this.target=null;};
      this.handleKeyDown=e=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)){this.keys.add(e.key);e.preventDefault();}};
      this.handleKeyUp=e=>{this.keys.delete(e.key);};this.keys=new Set();
      canvas.style.touchAction='none';canvas.tabIndex=canvas.tabIndex>=0?canvas.tabIndex:0;
      canvas.addEventListener('pointerdown',this.handleDown);canvas.addEventListener('pointermove',this.handleMove);
      canvas.addEventListener('pointerup',this.handleUp);canvas.addEventListener('pointercancel',this.handleUp);
      canvas.addEventListener('keydown',this.handleKeyDown);canvas.addEventListener('keyup',this.handleKeyUp);
      this.resizeObserver=new ResizeObserver(()=>this.draw());this.resizeObserver.observe(canvas);
      this.boundFrame=t=>this.frame(t);this.start();
    }
    updatePointer(e){const b=this.canvas.getBoundingClientRect();this.target={x:clamp((e.clientX-b.left)/b.width,0,1),y:clamp((e.clientY-b.top)/b.height,0,1)};}
    bindControls(map){for(const [direction,element] of Object.entries(map)){
        if(!element)continue;
        const down=e=>{e.preventDefault();this.holding=direction;};
        const up=()=>{if(this.holding===direction)this.holding=null;};
        element.addEventListener('pointerdown',down);element.addEventListener('pointerup',up);
        element.addEventListener('pointercancel',up);element.addEventListener('pointerleave',up);
        this.buttons.push({element,down,up});
      }return this;
    }
    start(){if(this.status==='won')return;this.status='playing';this.last=performance.now();if(!this.raf)this.raf=requestAnimationFrame(this.boundFrame);this.onState(this.snapshot());}
    pause(){if(this.status==='playing'){this.status='paused';this.target=null;this.holding=null;this.onState(this.snapshot());}}
    snapshot(){return {status:this.status,position:{...this.pos},collected:this.targets.filter(t=>t.found).map(t=>t.id),hits:this.hits,total:this.targets.length};}
    update(dt){if(this.status!=='playing'||document.hidden)return;
      let dx=0,dy=0;
      for(const key of this.keys){if(key==='ArrowLeft')dx--;if(key==='ArrowRight')dx++;if(key==='ArrowUp')dy--;if(key==='ArrowDown')dy++;}
      if(this.holding==='left')dx--;if(this.holding==='right')dx++;if(this.holding==='up')dy--;if(this.holding==='down')dy++;
      if(!dx&&!dy&&this.target){dx=this.target.x-this.pos.x;dy=this.target.y-this.pos.y;if(Math.hypot(dx,dy)<.025){dx=0;dy=0;}}
      const norm=Math.hypot(dx,dy)||1;this.pos.x=clamp(this.pos.x+dx/norm*this.speed*dt,.06,.94);this.pos.y=clamp(this.pos.y+dy/norm*this.speed*dt,.06,.94);
      for(const t of this.targets){if(!t.found&&Math.hypot(this.pos.x-t.x,this.pos.y-t.y)<(t.radius??.072)){
        t.found=true;this.onCollect(t,this.snapshot());this.onState(this.snapshot());
      }}
      const now=performance.now();for(const h of this.hazards){if(now-this.lastHazard>900&&Math.hypot(this.pos.x-h.x,this.pos.y-h.y)<(h.radius??.063)){
        this.lastHazard=now;this.hits++;this.pos={...this.startPoint};this.target=null;this.onHazard(h,this.snapshot());this.onState(this.snapshot());break;
      }}
      if(this.targets.length&&this.targets.every(t=>t.found)){this.status='won';this.target=null;this.holding=null;this.onWin(this.snapshot());this.onState(this.snapshot());}
    }
    frame(t){if(this.status==='destroyed')return;this.raf=requestAnimationFrame(this.boundFrame);
      const dt=Math.min(.07,Math.max(0,(t-this.last)/1000));this.last=t;
      // Adaptive renderer affects drawing rate only, never movement speed or scoring.
      this.update(dt);if(!window.SCTGPerformance||window.SCTGPerformance.shouldDraw(t,this.lastDraw||0)){
        this.draw();this.lastDraw=t;
      }
    }
    draw(){const box=this.canvas.getBoundingClientRect(),w=box.width,h=box.height;if(w<1||h<1)return;
      const dpr=window.SCTGPerformance?.size(w,h)||Math.min(1.5,window.devicePixelRatio||1);
      const cw=Math.max(1,Math.round(w*dpr)),ch=Math.max(1,Math.round(h*dpr));
      if(this.canvas.width!==cw||this.canvas.height!==ch){this.canvas.width=cw;this.canvas.height=ch;}
      const c=this.ctx;c.setTransform(dpr,0,0,dpr,0,0);c.clearRect(0,0,w,h);
      const bg=c.createLinearGradient(0,0,w,h);bg.addColorStop(0,'#071a25');bg.addColorStop(1,'#225368');c.fillStyle=bg;c.fillRect(0,0,w,h);
      c.strokeStyle='rgba(181,239,238,.13)';c.lineWidth=1;
      for(let i=0;i<10;i++){const yy=h*i/9;c.beginPath();c.moveTo(0,yy);c.lineTo(w,yy);c.stroke();}
      for(let i=0;i<9;i++){const xx=w*i/8;c.beginPath();c.moveTo(xx,0);c.lineTo(xx,h);c.stroke();}
      const orb=(x,y,r,color)=>{const g=c.createRadialGradient(x-r*.28,y-r*.3,1,x,y,r);g.addColorStop(0,'#ffffff');g.addColorStop(.22,color);g.addColorStop(1,'#102a37');c.fillStyle=g;c.beginPath();c.arc(x,y,r,0,Math.PI*2);c.fill();};
      for(const hzd of this.hazards){const x=hzd.x*w,y=hzd.y*h,r=(hzd.radius??.063)*Math.min(w,h);orb(x,y,r,'#ff6969');c.strokeStyle='#ffcfb7';c.lineWidth=2;c.beginPath();c.moveTo(x-r/3,y-r/3);c.lineTo(x+r/3,y+r/3);c.moveTo(x+r/3,y-r/3);c.lineTo(x-r/3,y+r/3);c.stroke();}
      for(const t of this.targets){const x=t.x*w,y=t.y*h,r=(t.radius??.072)*Math.min(w,h);orb(x,y,r,t.found?'#567277':'#ffdb71');c.fillStyle='#fff';c.textAlign='center';c.font='bold 11px system-ui';c.fillText(t.found?'✓':(t.label||'BUKTI'),x,y+r+16);}
      const x=this.pos.x*w,y=this.pos.y*h,r=Math.max(13,Math.min(w,h)*.04);c.fillStyle='rgba(0,0,0,.4)';c.beginPath();c.ellipse(x+3,y+r*.9,r*1.05,r*.35,0,0,Math.PI*2);c.fill();orb(x,y,r,'#51d9f7');
      c.strokeStyle='#e8ffff';c.lineWidth=2;c.beginPath();c.moveTo(x-r*.45,y);c.lineTo(x+r*.45,y);c.moveTo(x,y-r*.45);c.lineTo(x,y+r*.45);c.stroke();
      if(this.status==='won'){c.fillStyle='rgba(4,19,23,.7)';c.fillRect(0,h*.4,w,h*.17);c.fillStyle='#fff';c.textAlign='center';c.font=`bold ${Math.min(28,w*.06)}px system-ui`;c.fillText('MISI SELESAI!',w/2,h*.49);}
    }
    reset(){this.pos={...this.startPoint};for(const t of this.targets)t.found=false;this.hits=0;this.lastHazard=-100000;this.target=null;this.holding=null;this.status='playing';this.onState(this.snapshot());if(!this.raf){this.last=performance.now();this.raf=requestAnimationFrame(this.boundFrame);}}
    destroy(){this.status='destroyed';cancelAnimationFrame(this.raf);this.raf=0;this.resizeObserver.disconnect();this.canvas.removeEventListener('pointerdown',this.handleDown);this.canvas.removeEventListener('pointermove',this.handleMove);this.canvas.removeEventListener('pointerup',this.handleUp);this.canvas.removeEventListener('pointercancel',this.handleUp);this.canvas.removeEventListener('keydown',this.handleKeyDown);this.canvas.removeEventListener('keyup',this.handleKeyUp);for(const b of this.buttons){b.element.removeEventListener('pointerdown',b.down);b.element.removeEventListener('pointerup',b.up);b.element.removeEventListener('pointercancel',b.up);b.element.removeEventListener('pointerleave',b.up);}this.buttons=[];}
  }
  window.SCTGSteering=Object.freeze({SteeringField});
})();
