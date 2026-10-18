/* SCTG Adaptive Performance V1.3 — autonomous, offline, no student controls.
   Use frame cost and animation-frame cadence; never change learning state or timers. */
(()=>{'use strict';
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
// Internal rendering tiers, NOT student-selectable game quality settings.
const tiers=Object.freeze({
 hemat:Object.freeze({fps:16,pixels:240000,dpr:1,particles:.20,shadows:false}),
 standar:Object.freeze({fps:24,pixels:520000,dpr:1.45,particles:.55,shadows:true}),
 ultra:Object.freeze({fps:30,pixels:900000,dpr:1.8,particles:.85,shadows:true})
});
const ORDER=['hemat','standar','ultra'];
const reduce=()=>{try{return !!matchMedia('(prefers-reduced-motion: reduce)').matches}catch(_){return false}};
const cores=Number(navigator.hardwareConcurrency)||0,mem=Number(navigator.deviceMemory)||0;
// Missing hardware APIs are normal on Android and Safari. Start conservatively.
let level=(reduce()||(cores>0&&cores<=4)||(mem>0&&mem<=3))?0:1;
let samples=0, totalCost=0, slow=0, good=0, since=performance.now(), lastSwitch=since;
function reset(ts){samples=0;totalCost=0;slow=0;good=0;since=ts}
function announce(){try{dispatchEvent(new CustomEvent('sctg-performance-change',{detail:{adaptive:true}}))}catch(_){}}
function move(next,ts){next=clamp(next,0,ORDER.length-1);if(next===level)return;
 level=next;lastSwitch=ts;reset(ts);announce()}
function observeFrame(cost,rafGap=0){
 if(document.hidden){reset(performance.now());return}
 const ts=performance.now();if(!Number.isFinite(cost)||cost<0||cost>2000)return;
 // A first-frame gradient/cache build is not representative of steady rendering.
 if(cost>180){move(Math.max(0,level-1),ts);return}
 samples++;totalCost+=cost;
 const current=tiers[ORDER[level]],budget=1000/current.fps;
 const struggling=cost>Math.max(9,budget*.65)||(rafGap>36&&rafGap<600);
 if(struggling)slow++;else good++;
 if(samples<36||ts-lastSwitch<1800)return;
 const mean=totalCost/samples,slowRatio=slow/samples;
 // Downshift promptly when work takes too long or animation consistently stutters.
 if(level>0&&ts-since>=2200&&(mean>budget*.48||slowRatio>.42)){
   move(level-1,ts);return;
 }
 // Upgrade only after a long, genuinely smooth period; avoid oscillation.
 if(level<2&&!reduce()&&samples>=110&&ts-since>=14000&&ts-lastSwitch>=16000&&
   mean<Math.min(5,budget*.16)&&slowRatio<.08){move(level+1,ts);return}
 if(samples>=700)reset(ts);
}
function visibilityReset(){reset(performance.now())}
document.addEventListener('visibilitychange',visibilityReset);
try{matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change',()=>{if(reduce())move(0,performance.now())})}catch(_){}
const api={version:'1.3.0',get mode(){return ORDER[level]},get config(){return {...tiers[ORDER[level]]}},
 size(w,h,dpr=window.devicePixelRatio||1){let s=tiers[ORDER[level]];return clamp(Math.min(dpr,s.dpr,Math.sqrt(s.pixels/Math.max(1,w*h))),.65,1.8)},
 shouldDraw(ts,prev=0){return !prev||ts-prev>=1000/tiers[ORDER[level]].fps},observeFrame};
// No public setMode, dropdown or persisted manual setting. Course alone controls its content.
window.SCTGPerformance=Object.freeze(api);
})();
