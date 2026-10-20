"""One-at-a-time output-span ranks under explicitly different bounded ranges."""
import datetime,json
from pathlib import Path
import model
SETS={
 'original':{'growth_shift':(-.05,.05),'rd_ratio':(.18,.22),'capex_shift':(-.02,.02),'inventory_shift':(-50.,50.)},
 'narrow_growth':{'growth_shift':(-.005,.005),'rd_ratio':(.18,.22),'capex_shift':(-.02,.02),'inventory_shift':(-50.,50.)},
 'wide_rd_inventory':{'growth_shift':(-.05,.05),'rd_ratio':(.18,.24),'capex_shift':(-.02,.02),'inventory_shift':(-50.,100.)}}

def calculate():
 base=model.run();sets={}
 for name,ranges in SETS.items():
  rows=[]
  for key,(lo,hi) in ranges.items():
   assert model.BOUNDS[key][0]<=lo<hi<=model.BOUNDS[key][1]
   ends=[]
   for x in (lo,hi):
    r=model.run({key:x});last=r['statements'][-1]
    ends.append({'input':x,'profit_2031':last['operating_income'],'fcff_2031':last['fcff'],'per_share':r['valuation']['per_share']})
   rows.append({'driver':key,'low':lo,'high':hi,'endpoints':ends,'spans':{m:abs(ends[1][m]-ends[0][m]) for m in ('profit_2031','fcff_2031','per_share')}})
  ranks={m:[r['driver'] for r in sorted(rows,key=lambda r:r['spans'][m],reverse=True)] for m in ('profit_2031','fcff_2031','per_share')}
  sets[name]={'drivers':rows,'rankings':ranks}
 assert model.run()==base,'Sensitivity execution mutated the base'
 return {'execution_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'execution_mode':'AI-assisted additional range comparison; not a human locked prediction','valuation_date':str(model.DATE),'units':'profit/FCFF USD millions; value/share USD; ratio inputs fractions; inventory shifts days','method':'Rank by absolute low-to-high endpoint output span; one driver changes at a time; all others restored to BASE. Tied spans do not imply an economically meaningful ordering.','basis':'Original ranges match saved own-model sensitivity. Narrow-growth range is a controlled local comparison, not a confidence interval. Wider R&D/inventory ranges use existing model bounds as exploratory stresses, not independently established probabilities.','base_per_share':base['valuation']['per_share'],'sets':sets}

if __name__=='__main__':
 d=calculate();Path('output/range-ranking.json').write_text(json.dumps(d,indent=2)+'\n')
 lines=['# Range-ranking comparison','',d['method'],'',d['basis'],'','All values are model results, not evidence that the economic assumptions are true.','']
 for name,s in d['sets'].items():
  lines+=['## '+name,'','| Driver | Low | High | 2031 EBIT span, $m | 2031 FCFF span, $m | Value/share span, $ |','|---|---:|---:|---:|---:|---:|']
  for r in s['drivers']:lines.append('| '+r['driver']+' | '+str(r['low'])+' | '+str(r['high'])+' | '+' | '.join(f"{r['spans'][m]:,.2f}" for m in ('profit_2031','fcff_2031','per_share'))+' |')
  for m,rank in s['rankings'].items():lines+=['',m+': '+' > '.join(rank)]
 lines+=['','## Interpretation','','These comparisons explicitly test range dependence. Narrowing growth changes its measured span without changing the model or investment evidence. Compare the recorded ranks rather than asserting a universal dominant driver. EBIT ignores the capex/inventory changes because these inputs have no direct feedback into the fixed operating-margin path; their zero EBIT spans are tied. Value and FCFF rankings need not match. Watch/defer and all base assumptions remain unchanged.']
 Path('docs/Range-Ranking.md').write_text('\n'.join(lines)+'\n')
 print(json.dumps({k:s['rankings'] for k,s in d['sets'].items()},indent=2))
