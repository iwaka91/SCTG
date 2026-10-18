/* Starter only: use SCTGFactory to build complete experience. NOT FINAL CANDIDATE. */
(() => {
  const courseCode='{{COURSE_CODE}}';
  const store=new SCTGFactory.SessionStore(courseCode,{identity:null,preferences:{theme:'auto'},progress:{}});
  const stage=new SCTGFactory.StageMode();
  const artWorld=({'LIT':'literasi','NUM':'numerasi','SEJ':'sejarah'})['{{SERIES}}']||'literasi';
  const visual=SCTGVisual.mount(document.getElementById('starterHero'),{world:artWorld,onActivate:()=>{}});
  const steps=[...document.querySelectorAll('[data-sctg-step]')];
  const nav=new SCTGFactory.StepNavigation({steps,onChange:n=>{visual.setActive(n===1);console.info('Step',n)}});
  document.getElementById('login').addEventListener('click',()=>{
    const name=document.getElementById('name').value.trim();if(!name)return;
    store.state.identity={name};store.save();nav.complete(1);nav.open(2);
  });
  // This starter intentionally does not pretend to be a complete course.
})();
