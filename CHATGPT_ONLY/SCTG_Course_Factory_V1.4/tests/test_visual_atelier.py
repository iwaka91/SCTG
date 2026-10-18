import json
import hashlib
import tempfile
import unittest
from pathlib import Path
from playwright.sync_api import sync_playwright
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'cli'))
from visual_gate import init,verify
from check_benchmarks import check

class VisualAtelierTests(unittest.TestCase):
    def test_both_benchmarks_immutable(self):
        self.assertEqual(check(),[])
        m=json.loads((ROOT/'benchmarks/MANIFEST.json').read_text())
        self.assertEqual([r['id'] for r in m['references']],['NUM09','NUM10'])
    def test_default_quality_gate_rejects(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d)
            html=d/'course.html';html.write_text('<html>...</html>')
            review=d/'review.json';init(html,review)
            self.assertFalse(verify(html,review)[0]); html.write_text('<html>modified</html>')
            self.assertIn('Hash HTML berbeda dari HTML yang dinilai',verify(html,review)[1])
    def test_quality_gate_rejects_fake_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d)
            html=d/'course.html';html.write_text('<html>...</html>')
            review=d/'review.json';v=init(html,review)
            for gate in v['gates'].values():
                gate.update(verdict='ya',review_notes='Klaim panjang yang belum punya bukti screenshot sebenarnya untuk dinilai.',evidence=['tidak_ada.png'])
            review.write_text(json.dumps(v));self.assertFalse(verify(html,review)[0])
    def test_canvas_demo_is_playable_visual_preview(self):
        with sync_playwright() as p:
            browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
            for w,h in ((390,700),(1280,650)):
                page=browser.new_page(viewport={'width':w,'height':h})
                errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
                page.set_content((ROOT/'demos/VISUAL_ATELIER_SHOWCASE.html').read_text(encoding='utf-8'))
                page.wait_for_timeout(700)
                alpha=page.locator('#scene').evaluate('''el => { const c=el.getContext('2d');const i=c.getImageData(el.width/2|0,el.height/2|0,1,1);return i.data[3] }''')
                self.assertEqual(alpha,255)
                self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth-innerWidth'),1)
                page.locator('[data-world="sejarah"]').click()
                self.assertIn('Gerbang',page.locator('#headline').inner_text())
                page.locator('#scene').click(position={'x':w*.5,'y':h*.7},force=True)
                self.assertIn('merespons',page.locator('#status').inner_text())
                self.assertEqual(errors,[])
                page.close()
            browser.close()
if __name__=='__main__':unittest.main()
