import copy,unittest
import model
class Checks(unittest.TestCase):
 def test_known_answer(self):
  self.assertEqual(150*(1-.25)+40-60-15,77.5)
  self.assertEqual((1000+100-250-20-10)/100,8.2)
 def test_statements(self):
  r=model.run();self.assertEqual([y['year'] for y in r['statements'][1:]],[2027,2028,2029,2030,2031])
  for y in r['statements']:
   self.assertLess(max(abs(g) for g in y['checks'].values()),.01)
 def test_wacc(self):
  ys=model.project();self.assertGreater(model.value(ys,{'wacc':.08})['per_share'],model.value(ys,{'wacc':.10})['per_share'])
 def test_growth(self):
  self.assertGreater(model.run({'growth_shift':.01})['valuation']['per_share'],model.run()['valuation']['per_share'])
 def test_terminal_growth(self):
  ys=model.project();self.assertGreater(model.value(ys,{'terminal_growth':.03})['per_share'],model.value(ys,{'terminal_growth':.02})['per_share'])
 def test_bridge(self):
  v=model.run()['valuation'];self.assertAlmostEqual(v['ev']+8950+3856-54908,v['equity'])
 def test_reverse(self):self.assertAlmostEqual(model.reverse_growth()['per_share'],model.PRICE,places=5)
 def test_refuse_bounds(self):
  with self.assertRaises(ValueError):model.run({'rd_ratio':.9})
 def test_refuse_perpetuity(self):
  with self.assertRaises(ValueError):model.value(model.project(),{'wacc':.02,'terminal_growth':.03})
 def test_corruption(self):
  ys=model.project();ys[2]['cash']+=1000
  self.assertEqual(round(model.s.checks(ys[2],ys[1])['Assets - liabilities - equity']),1000)
 def test_negative_fcff_retained(self):
  ys=model.project();ys[1]['fcff']=-10000
  self.assertLess(model.value(ys)['pv_explicit'],model.value(model.project())['pv_explicit'])
if __name__=='__main__':unittest.main()
