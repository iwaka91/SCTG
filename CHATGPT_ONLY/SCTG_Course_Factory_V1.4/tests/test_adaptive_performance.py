import pathlib,unittest,subprocess,tempfile
R=pathlib.Path(__file__).resolve().parents[1]
class AdaptivePerformanceTests(unittest.TestCase):
 def test_builder_includes_adaptive_engine(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);(p/'course.html').write_text((R/'starter/course.html').read_text().replace('{{COURSE_TITLE}}','Demo').replace('{{COURSE_CODE}}','LIT99'))
   (p/'course.css').write_text('');(p/'course.js').write_text('')
   out=p/'built.html'
   r=subprocess.run(['python',str(R/'cli/factory.py'),'build','--src',str(p/'course.html'),'--out',str(out)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stderr)
   html=out.read_text();self.assertIn('SCTGPerformance',html)
   self.assertIn('observeFrame',html)
   self.assertNotIn('sctg_performance_mode',html)
 def test_automatic_not_user_selected(self):
  src=(R/'engine/sctg-performance.js').read_text()
  for term in ('hemat','standar','ultra','observeFrame','shouldDraw','visibilitychange'):
   self.assertIn(term,src)
  for forbidden in ('setMode(', 'localStorage.', 'sctg_performance_mode'):
   self.assertNotIn(forbidden,src)
 def test_lit10_cannot_select_mode(self):
  # LIT10 is separately delivered, but its runtime should be the same engine.
  c=pathlib.Path('/mnt/data/LIT10_Misteri_Dokumen_Palsu_SCTG43_v1_3_Otomatis.html')
  if not c.exists():return
  s=c.read_text();self.assertNotIn('id="perfMode"',s);self.assertNotIn('id="perfChoice"',s)
  self.assertNotIn('setMode(next)',s);self.assertIn('observeFrame(performance.now()-paintStart,rafGap)',s)
