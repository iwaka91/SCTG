import json,sys,tempfile,unittest
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'cli'))
from visual_gate import init,verify

class CourseFactory14(unittest.TestCase):
    def test_user_review_recorded_and_benchmarks_unchanged(self):
        review=(ROOT/'feedback/2026-10-18/LIT10_POST_RELEASE_REVIEW.md').read_text()
        self.assertIn('8,2/10',review);self.assertIn('8/10',review)
        from check_benchmarks import check
        self.assertEqual([],check())
    def test_five_gates_require_playable_mechanic_and_cinematic_proof(self):
        with tempfile.TemporaryDirectory() as temp:
            d=Path(temp);html=d/'test.html';html.write_text('<p>test</p>')
            form=d/'gate.json';data=init(html,form)
            self.assertEqual('SCTG-5-GATES-1.2',data['schema'])
            problems=verify(html,form)[1]
            self.assertTrue(any(p.startswith('GAMEPLAY:') for p in problems))
            self.assertTrue(any(p.startswith('CINEMATIC:') for p in problems))
    def test_builder_embeds_mechanic_and_typography(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'index.html'
            cmd=['python',str(ROOT/'cli/factory.py'),'build','--src',str(ROOT/'courses/DEMOQA/course.html'),'--out',str(out)]
            subprocess.run(cmd,check=True,capture_output=True,text=True)
            text=out.read_text()
            self.assertIn('window.SCTGSteering',text)
            self.assertIn('.sctg-cine-typography',text)
            self.assertIn('window.SCTGPerformance',text)
    def test_demonstration_input_and_stage(self):
        with sync_playwright() as p:
            browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-gpu','--disable-dev-shm-usage'])
            try:
                html=(ROOT/'demos/STEERING_CINEMATIC_V1_4.html').read_text()
                for w,h in [(390,700),(1280,650)]:
                    page=browser.new_page(viewport={'width':w,'height':h})
                    errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
                    page.set_content(html)
                    page.wait_for_function('!!window.__sctgDemoField')
                    x=page.evaluate('window.__sctgDemoField.pos.x')
                    page.locator('#left').hover()
                    page.mouse.down();page.wait_for_timeout(400);page.mouse.up()
                    x2=page.evaluate('window.__sctgDemoField.pos.x')
                    self.assertLess(x2,x-.03,f'left steering failed {w} px')
                    self.assertEqual(page.locator('#cine').get_attribute('hidden'),'')
                    page.locator('#showIntro').click()
                    self.assertTrue(page.locator('#cine').is_visible())
                    self.assertEqual(page.locator('#cinContinue').is_enabled(),False)
                    font=page.locator('#cinText').evaluate('(e)=>getComputedStyle(e).fontSize')
                    self.assertGreaterEqual(float(font.replace('px','')),25)
                    page.wait_for_timeout(900)
                    self.assertTrue(page.locator('#cinText').is_visible())
                    self.assertFalse(errors,f'{w}x{h}: {errors}')
                    page.close()
            finally:browser.close()

if __name__=='__main__':unittest.main()

class FeedbackLedgerTests(unittest.TestCase):
    def test_rating_requires_explicit_input_and_never_overwrites(self):
        sys.path.insert(0,str(ROOT/'cli'))
        from feedback_loop import record
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'lit10.json'
            record('LIT10','v1.3','lulus',8,8.2,'Course dinilai layak rilis namun kelemahan game-like dan sinematik tetap ada.',out)
            val=json.loads(out.read_text())
            self.assertEqual(val['overall_user_rating'],8.2)
            self.assertEqual(val['changes_implemented'],[])
            with self.assertRaises(FileExistsError):
                record('LIT10','v1.3','lulus',8,8.2,'Jangan timpa data ulasan yang sudah tercatat sebelumnya.',out)
