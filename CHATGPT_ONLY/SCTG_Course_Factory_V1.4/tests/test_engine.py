import unittest
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
ENGINE=(ROOT/'engine/sctg-core.js').read_text(encoding='utf-8')
CSS=(ROOT/'engine/sctg-layout.css').read_text(encoding='utf-8')
class RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager=sync_playwright().start()
        cls.browser=cls.manager.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
    @classmethod
    def tearDownClass(cls):cls.browser.close();cls.manager.stop()
    def setUp(self):
        self.page=self.browser.new_page(viewport={'width':390,'height':700})
        self.page.set_content(f'''<!doctype html><html><head><style>{CSS}</style></head><body>
          <input id="typing"><button id="silent" class="sctg-read-button" disabled>Continue</button>
          <span id="timer"></span><div id="read">Bacaan satu</div>
          <div class="sctg-game-screen"><div class="sctg-question">Question</div>
          <div class="sctg-arena"><canvas id="cv"></canvas></div>
          <div class="sctg-actions">Actions</div></div>
          <script>{ENGINE}</script></body></html>''')
    def tearDown(self):self.page.close()
    def test_silent_gate_and_focus(self):
        self.page.evaluate('''() => {
            window.probe={done:0};
            window.gate=new SCTGFactory.SilentGate({key:'test',content:document.querySelector('#read'),button:document.querySelector('#silent'),indicator:document.querySelector('#timer'),seconds:1,onDone:()=>window.probe.done++});
            window.gate.setOpen(true);
        }''')
        self.page.locator('#typing').fill('Belajar numerasi')
        self.page.set_viewport_size({'width':390,'height':440})
        self.page.wait_for_timeout(1400)
        self.assertEqual(self.page.locator('#typing').input_value(),'Belajar numerasi')
        self.assertTrue(self.page.locator('#typing').evaluate('(el)=>document.activeElement===el'))
        self.assertTrue(self.page.locator('#silent').is_enabled())
        self.assertEqual(self.page.evaluate('window.probe.done'),1)
    def test_hidden_gate_pauses(self):
        self.page.evaluate('''() => {
          window.gate=new SCTGFactory.SilentGate({key:'pause',content:document.querySelector('#read'),button:document.querySelector('#silent'),indicator:document.querySelector('#timer'),seconds:3});
          window.gate.setOpen(true);
        }''')
        self.page.wait_for_timeout(350)
        self.page.evaluate('window.gate.setOpen(false)')
        a=self.page.evaluate('window.gate.remaining')
        self.page.wait_for_timeout(450)
        b=self.page.evaluate('window.gate.remaining')
        self.assertAlmostEqual(a,b,delta=.15)
    def test_canvas_and_auto_layout(self):
        self.page.evaluate('''() => {
          window.stage=new SCTGFactory.StageMode();
          window.model={taps:0};
          window.loop=new SCTGFactory.CanvasLoop(document.querySelector('#cv'),(ctx,s)=>{ctx.fillStyle='#183b24';ctx.fillRect(0,0,s.width,s.height);ctx.fillStyle='#ffd46c';ctx.fillRect(20,20,90,80)}, {onTap:()=>window.model.taps++});
          loop.start();
        }''')
        self.page.wait_for_timeout(300)
        painted=self.page.locator('#cv').evaluate('c => c.getContext("2d").getImageData(21,21,1,1).data[3]')
        self.assertEqual(painted,255)
        self.page.locator('#cv').click(position={'x':10,'y':10})
        self.assertEqual(self.page.evaluate('window.model.taps'),1)
        self.assertEqual(self.page.locator('html').get_attribute('data-sctg-mode'),'genggam')
        self.page.set_viewport_size({'width':900,'height':500})
        self.page.wait_for_function("document.documentElement.dataset.sctgMode === 'panggung'")
        self.assertEqual(self.page.locator('html').get_attribute('data-sctg-mode'),'panggung')

if __name__=='__main__':unittest.main()
