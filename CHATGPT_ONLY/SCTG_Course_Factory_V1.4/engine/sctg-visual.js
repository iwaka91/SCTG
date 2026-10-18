/* SCTG Visual Atelier V1.1 — original reusable Canvas 2D scene foundations.
   Ref: visual principles of Claude NUM09 + NUM10, NOT copied scenes/assets.
   A game still requires an authored mechanic, not just an attractive scene. */
(() => {
  'use strict';
  const TAU=Math.PI*2, clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
  const themes={
    literasi:{top:'#091b31',mid:'#315d76',horizon:'#e6a963',floor:'#12263e',mist:'#84d7db',gold:'#f8d28c',light:'#fff3c7',accent:'#69d9e3',label:'RUANG CERITA'},
    numerasi:{top:'#101732',mid:'#365277',horizon:'#d89f70',floor:'#152842',mist:'#8bb7e9',gold:'#f9df8c',light:'#ffefd3',accent:'#9ce2b0',label:'LABORATORIUM ANGKA'},
    sejarah:{top:'#15162e',mid:'#664b65',horizon:'#efa66c',floor:'#24223a',mist:'#d9a5ce',gold:'#ffd596',light:'#fff0c2',accent:'#e5c794',label:'GERBANG WAKTU'}
  };
  const rgba=(hex,a)=>{const h=hex.replace('#','');const c=h.length===3?h.split('').map(x=>x+x).join(''):h;return `rgba(${parseInt(c.slice(0,2),16)},${parseInt(c.slice(2,4),16)},${parseInt(c.slice(4,6),16)},${a})`};
  function rr(c,x,y,w,h,r){r=Math.max(0,Math.min(r,Math.abs(w)/2,Math.abs(h)/2));c.beginPath();c.moveTo(x+r,y);c.arcTo(x+w,y,x+w,y+h,r);c.arcTo(x+w,y+h,x,y+h,r);c.arcTo(x,y+h,x,y,r);c.arcTo(x,y,x+w,y,r);c.closePath()}
  function glow(c,x,y,r,col,pow=1){const gr=c.createRadialGradient(x,y,0,x,y,r);gr.addColorStop(0,rgba(col,Math.min(1,pow*.6)));gr.addColorStop(.35,rgba(col,pow*.18));gr.addColorStop(1,rgba(col,0));c.fillStyle=gr;c.fillRect(x-r,y-r,r*2,r*2)}
  function poly(c,pts,fill,stroke){c.beginPath();pts.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.closePath();c.fillStyle=fill;c.fill();if(stroke){c.strokeStyle=stroke;c.stroke()}}
  function grad(c,x,y,w,h,top,bottom){const g=c.createLinearGradient(x,y,x,y+h);g.addColorStop(0,top);g.addColorStop(1,bottom);c.fillStyle=g;c.fillRect(x,y,w,h)}
  function pill(c,x,y,w,h,fill,stroke,blur=0){c.save();c.shadowColor=stroke||fill;c.shadowBlur=blur;rr(c,x,y,w,h,Math.min(16,h*.35));c.fillStyle=fill;c.fill();if(stroke){c.strokeStyle=stroke;c.lineWidth=1.4;c.stroke()}c.restore()}
  function drawBackdrop(c,w,h,t,theme){
    const p=themes[theme],horizon=h*.59;grad(c,0,0,w,h,p.top,p.mid);const ygrad=c.createLinearGradient(0,h*.22,0,h);ygrad.addColorStop(0,'rgba(255,255,255,0)');ygrad.addColorStop(.45,rgba(p.horizon,.85));ygrad.addColorStop(1,rgba(p.floor,.6));c.fillStyle=ygrad;c.fillRect(0,0,w,h);
    glow(c,w*.77,h*.29,Math.max(w,h)*.4,p.horizon,.85);glow(c,w*.76,h*.26,h*.14,p.light,.95);
    c.fillStyle=rgba(p.light,.9);c.beginPath();c.arc(w*.76,h*.26,Math.min(w,h)*.035,0,TAU);c.fill();
    const hills=[{y:.59,scale:.07,col:rgba(p.floor,.25),speed:1},{y:.64,scale:.10,col:rgba(p.floor,.5),speed:2.4},{y:.73,scale:.11,col:rgba(p.floor,.92),speed:5}];
    hills.forEach((z,k)=>{c.beginPath();c.moveTo(0,h);for(let x=-10;x<=w+10;x+=10){const y=h*z.y+Math.sin(x/w*10+k*1.4+t*.04*z.speed)*h*z.scale*.28+Math.sin(x/w*17+k*3)*h*z.scale*.20;c.lineTo(x,y)}c.lineTo(w,h);c.closePath();c.fillStyle=z.col;c.fill()});
    const grd=c.createLinearGradient(0,h*.78,0,h);grd.addColorStop(0,rgba(p.floor,.15));grd.addColorStop(1,p.floor);c.fillStyle=grd;c.fillRect(0,h*.77,w,h*.23);
    for(let i=0;i<34;i++){const a=i*12.9898,x=((Math.sin(a+3)*9563.31)%1+1)%1*w,y=((Math.sin(a+9)*6851.47)%1+1)%1*h*.73;const f=.25+.75*(.5+.5*Math.sin(t*(.3+i%4*.16)+i));c.fillStyle=rgba(p.light,Math.min(.62,f*.48));c.beginPath();c.arc(x,y,(i%4===0?1.8:.8)*Math.min(1.3,w/750+0.4),0,TAU);c.fill()}
    const fog=c.createLinearGradient(0,h*.45,0,h*.85);fog.addColorStop(0,rgba(p.mist,0));fog.addColorStop(.48,rgba(p.mist,.19));fog.addColorStop(1,rgba(p.mist,0));c.fillStyle=fog;c.fillRect(0,h*.45,w,h*.43);
  }
  function isoSlab(c,x,y,w,h,p,depth){const d=depth;poly(c,[[x-w*.5,y],[x+w*.5,y],[x+w*.5+d,y+d*.54],[x-w*.5+d,y+d*.54]],p.top,rgba(p.gold,.6));poly(c,[[x-w*.5+d,y+d*.54],[x+w*.5+d,y+d*.54],[x+w*.5+d,y+d*.54+h],[x-w*.5+d,y+d*.54+h]],p.floor);poly(c,[[x+w*.5,y],[x+w*.5+d,y+d*.54],[x+w*.5+d,y+d*.54+h],[x+w*.5,y+h]],rgba(p.accent,.31));}
  function book(c,x,y,s,t,p){
    c.save();c.translate(x,y);c.rotate(Math.sin(t*.5)*.022);glow(c,0,-s*.15,s*1.15,p.gold,.52);c.fillStyle='rgba(2,6,18,.36)';c.beginPath();c.ellipse(0,s*.65,s*.85,s*.16,0,0,TAU);c.fill();
    poly(c,[[-s*.55,0],[-s*.06,-s*.08],[0,s*.04],[0,s*.44],[-s*.55,s*.27]],'#efdfbd',rgba(p.gold,.6));poly(c,[[0,s*.04],[s*.06,-s*.09],[s*.57,0],[s*.57,s*.27],[0,s*.44]],'#fff2d5',rgba(p.gold,.6));
    poly(c,[[-s*.55,0],[-s*.05,-s*.17],[0,s*.0],[0,s*.09],[-s*.53,s*.10]],'#a55d48');poly(c,[[0,0],[s*.05,-s*.17],[s*.55,0],[s*.54,s*.10],[0,s*.09]],'#f1bd66');
    c.strokeStyle='rgba(107,84,83,.42)';c.lineWidth=Math.max(.7,s*.01);for(let i=1;i<=3;i++){c.beginPath();c.moveTo(-s*.49,-s*.005+i*s*.07);c.lineTo(-s*.11,-s*.055+i*s*.07);c.moveTo(s*.12,-s*.048+i*s*.07);c.lineTo(s*.48,s*.025+i*s*.06);c.stroke()}
    c.strokeStyle=rgba(p.light,.75);c.lineWidth=2;c.beginPath();c.moveTo(0,0);c.lineTo(0,s*.43);c.stroke();c.restore();
  }
  function pillar(c,x,y,s,p){
    const grad1=c.createLinearGradient(x-s*.22,0,x+s*.25,0);grad1.addColorStop(0,'#283956');grad1.addColorStop(.3,'#7d8f9a');grad1.addColorStop(.7,'#dbbf98');grad1.addColorStop(1,'#374157');
    poly(c,[[x-s*.24,y],[x+s*.24,y],[x+s*.16,y-s*1.5],[x-s*.16,y-s*1.5]],grad1,rgba(p.light,.22));
    pill(c,x-s*.34,y-s*1.57,s*.68,s*.16,'#7e888e',rgba(p.gold,.3),2);pill(c,x-s*.31,y-s*.07,s*.62,s*.18,'#4d5a63',rgba(p.gold,.23));
    for(let k=-1;k<=1;k++){c.strokeStyle='rgba(255,244,209,.16)';c.lineWidth=1.1;c.beginPath();c.moveTo(x+k*s*.085,y-s*.12);c.lineTo(x+k*s*.085,y-s*1.47);c.stroke()}
  }
  function crystal(c,x,y,s,t,p){
    c.save();c.translate(x,y);const z=Math.sin(t*1.8)*s*.025;c.translate(0,z);glow(c,0,0,s*1.8,p.accent,.7);
    poly(c,[[0,-s],[-s*.38,-s*.22],[0,s*.45],[s*.43,-s*.22]],rgba(p.accent,.6),rgba(p.light,.7));poly(c,[[0,-s],[0,s*.45],[s*.43,-s*.22]],rgba(p.light,.31));poly(c,[[0,-s],[-s*.38,-s*.22],[0,s*.45]],rgba(p.floor,.18));c.restore();
  }
  function arch(c,x,y,s,p,t){
    glow(c,x,y-s*.7,s*1.25,p.accent,.55);const ring=c.createLinearGradient(x-s,y-s,x+s,y);ring.addColorStop(0,p.accent);ring.addColorStop(.5,p.gold);ring.addColorStop(1,p.light);
    c.save();c.lineWidth=s*.17;c.strokeStyle=ring;c.shadowColor=p.gold;c.shadowBlur=s*.2;c.beginPath();c.ellipse(x,y-s*.78,s*.68,s*.96,0,Math.PI,TAU);c.stroke();c.restore();
    c.save();c.beginPath();c.ellipse(x,y-s*.78,s*.57,s*.85,0,0,TAU);c.clip();const g=c.createRadialGradient(x,y-s*.67,3,x,y-s*.67,s*.76);g.addColorStop(0,rgba(p.light,.5));g.addColorStop(.55,rgba(p.accent,.28));g.addColorStop(1,rgba(p.accent,0));c.fillStyle=g;c.fillRect(x-s,y-s*2,s*2,s*2);c.strokeStyle=rgba(p.light,.22);for(let i=0;i<15;i++){c.beginPath();c.moveTo(x+Math.sin(i*4+t*.2)*s*.5,y-s*1.4);c.lineTo(x+Math.cos(i*2.7+t*.3)*s*.6,y-s*.25);c.stroke()}c.restore();
  }
  function scene(c,w,h,t,world,hotspot){
    const p=themes[world]||themes.literasi;drawBackdrop(c,w,h,t,world);
    const cx=w*(w<600?.51:.51),base=h*.8,u=Math.min(w*.85,h*.64,490);
    glow(c,cx,base,u*.7,p.gold,.25);
    c.fillStyle='rgba(0,0,0,.38)';c.beginPath();c.ellipse(cx+u*.04,base+u*.10,u*.77,u*.19,0,0,TAU);c.fill();
    isoSlab(c,cx,base-u*.05,u*1.24,u*.17,p,u*.14);
    const dx=hotspot?Math.sin(t*5)*4:0;
    if(world==='literasi'){
      const bookY=base-u*.18+Math.sin(t*.6)*u*.016;
      pillar(c,cx-u*.43,base-u*.06,u*.34,p);pillar(c,cx+u*.43,base-u*.06,u*.34,p);
      book(c,cx,bookY,u*.72,t,p);
      for(let i=0;i<7;i++){const a=t*.42+i*TAU/7,r=u*(.35+.09*Math.sin(i*9));const x=cx+Math.cos(a)*r,y=bookY-u*.28+Math.sin(a*1.1)*u*.2;glow(c,x,y,u*.09,p.gold,.23);c.fillStyle=p.light;c.beginPath();c.arc(x,y,Math.max(1.5,u*.008),0,TAU);c.fill()}
    }else if(world==='numerasi'){
      pillar(c,cx-u*.39,base-u*.04,u*.25,p);pillar(c,cx+u*.39,base-u*.04,u*.25,p);
      crystal(c,cx,base-u*.46,u*.39,t,p);for(let i=0;i<10;i++){const a=t*.4+i*TAU/10;const x=cx+Math.cos(a)*u*.51,y=base-u*.45+Math.sin(a)*u*.2;glow(c,x,y,u*.055,p.gold,.26)}
      c.strokeStyle=rgba(p.gold,.48);c.lineWidth=Math.max(1.2,u*.006);c.beginPath();c.ellipse(cx,base-u*.42,u*.55,u*.2,-.08,0,TAU);c.stroke();
    }else{
      pillar(c,cx-u*.38,base,u*.38,p);pillar(c,cx+u*.38,base,u*.38,p);arch(c,cx,base-u*.02,u*.65,p,t);
      for(let k=0;k<5;k++){const x=cx+Math.sin(t*.25+k)*u*.3;const y=base-u*.65+Math.cos(t*.3+k*4)*u*.24;glow(c,x,y,u*.1,p.gold,.34)}
    }
    if(hotspot){glow(c,cx,base-u*.54,u*.4,p.gold,.8);c.strokeStyle=rgba(p.light,.9);c.lineWidth=2;c.beginPath();c.ellipse(cx,base-u*.45,u*.53+dx,u*.23,0,0,TAU);c.stroke()}
    // Readability veil at left for overlaid titles on widescreen; bottom vignette for every size
    const v=c.createLinearGradient(0,0,w,0);v.addColorStop(0,'rgba(4,10,22,.36)');v.addColorStop(.45,'rgba(4,10,22,0)');v.addColorStop(1,'rgba(4,10,22,.10)');c.fillStyle=v;c.fillRect(0,0,w,h);
    const shade=c.createLinearGradient(0,h*.65,0,h);shade.addColorStop(0,'rgba(3,8,18,0)');shade.addColorStop(1,'rgba(3,8,18,.55)');c.fillStyle=shade;c.fillRect(0,h*.65,w,h*.35);
  }
  function mount(canvas,{world='literasi',onActivate=null,autoStart=true}={}){
    if(!canvas||!canvas.getContext)throw Error('SCTGVisual.mount memerlukan canvas');
    const c=canvas.getContext('2d',{alpha:false});if(!c)throw Error('Canvas 2D tidak tersedia');
    let active=true,run=false,raf=0,w=0,h=0,dpr=1,flash=0,tm=0,prev=0,paintAt=0;
    const reduced=()=>!!window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches;
    const resize=()=>{const r=canvas.getBoundingClientRect();w=Math.max(1,Math.round(r.width));h=Math.max(1,Math.round(r.height));dpr=window.SCTGPerformance?.size(w,h)||clamp(window.devicePixelRatio||1,1,2);canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);c.setTransform(dpr,0,0,dpr,0,0);draw()};
    function draw(){if(w&&h){c.clearRect(0,0,w,h);scene(c,w,h,tm,world,flash>0)}}
    function frame(ts){if(!run)return;const dt=prev?Math.min(.05,(ts-prev)/1000):0;prev=ts;if(!document.hidden&&active){if(!reduced())tm+=dt;flash=Math.max(0,flash-dt*1.3);if(!window.SCTGPerformance||window.SCTGPerformance.shouldDraw(ts,paintAt)){paintAt=ts;const before=performance.now();draw();window.SCTGPerformance?.observeFrame(performance.now()-before,dt*1000)}}raf=requestAnimationFrame(frame)}
    const pointer=(e)=>{const r=canvas.getBoundingClientRect();const x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;if(x>.12&&x<.89&&y>.18&&y<.94){flash=1.2;onActivate?.({x,y,world})}};
    canvas.addEventListener('pointerup',pointer);const obs=typeof ResizeObserver!=='undefined'?new ResizeObserver(resize):null;obs?.observe(canvas);addEventListener('resize',resize);addEventListener('sctg-performance-change',resize);resize();
    if(autoStart){run=true;raf=requestAnimationFrame(frame)}
    return {setWorld:(next)=>{if(themes[next])world=next;draw()},redraw:draw,setActive:v=>{active=!!v},getWorld:()=>world,destroy:()=>{run=false;cancelAnimationFrame(raf);obs?.disconnect();removeEventListener('resize',resize);removeEventListener('sctg-performance-change',resize);canvas.removeEventListener('pointerup',pointer)}};
  }
  window.SCTGVisual=Object.freeze({mount,themes:Object.freeze(themes),version:'1.3.0'});
})();
