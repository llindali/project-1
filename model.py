"""Integrated Lilly statements and FCFF DCF; USD millions, shares millions."""
import copy, datetime, json, math
from pathlib import Path
import legacy_statements as s

DATE = datetime.date(2026, 9, 8)
PRICE = 1123.91  # Lab 8 dated close; confirmation requested
BRIDGE = dict(cash=8950., investments=3856., debt=54908., shares=893.7)
BOUNDS = {'growth_shift':(-.10,.10),'rd_ratio':(.18,.24),'capex_shift':(-.02,.04),
          'inventory_shift':(-50.,100.),'wacc':(.07,.12),'terminal_growth':(.01,.04)}
BASE = dict(growth_shift=0.,rd_ratio=.20,capex_shift=0.,inventory_shift=0.,wacc=.09,terminal_growth=.025)
# Extend the inherited 2026 bridge to five full forecast years, 2027-2031.
for name,last in [('GROWTH',.07),('MARGIN',.84),('SGA_GP',.18),('RD',.20),('IPRD',4000.),('CAPEX',.08),('DAYS',330.),('ACQUISITIONS',0.),('NEW_DEBT',0.),('BUYBACKS',0.)]:
 setattr(s,name,tuple(getattr(s,name))+(last,))

def project(params=None):
 p=BASE| (params or {})
 for key,(lo,hi) in BOUNDS.items():
  if not math.isfinite(p[key]) or not lo<=p[key]<=hi:raise ValueError(f'{key} outside defended range [{lo}, {hi}]')
 years=[];previous=s.OPENING
 old_growth,old_days=s.GROWTH,s.DAYS
 try:
  s.GROWTH=(old_growth[0],)+tuple(v+p['growth_shift'] for v in old_growth[1:])
  s.DAYS=tuple(v+p['inventory_shift'] for v in old_days)
  for i in range(6):
   y=s.project_year(previous,i,rd_ratio=p['rd_ratio'],capex_ratio=s.CAPEX[i]+p['capex_shift'])
   for name,gap in s.checks(y,previous).items():
    if abs(gap)>.01:raise ValueError(f"FY{y['year']} {name}: {gap:.4f}")
   # Undo levered taxes using the exact tax convention; acquired IPR&D remains non-deductible.
   y['unlevered_tax']=max(0.,y['operating_income']+y['iprd'])*s.TAX
   y['fcff']=y['operating_income']-y['unlevered_tax']+y['depreciation']+y['amortization']-y['capex']-y['delta_wc']-y['acquisitions']
   identity=y['cfo']+y['cfi']+y['interest']+y['tax']-y['unlevered_tax']
   if abs(identity-y['fcff'])>.01:raise ValueError('FCFF operating/equity reconciliation failed')
   y['total_assets']=s.assets(y)
   y['total_liabilities_equity']=s.liabilities_equity(y)
   y['checks']=s.checks(y,previous)
   years.append(y);previous=y
 finally:s.GROWTH,s.DAYS=old_growth,old_days
 return years

def value(years,params=None):
 p=BASE|(params or {});w,g=p['wacc'],p['terminal_growth']
 if not math.isfinite(w+g) or w<=g or g<0:raise ValueError('Require finite WACC > terminal growth >= 0')
 stub=(datetime.date(2026,12,31)-DATE).days/365
 # Business-acquisition cash was spent in H1; exclude it from remaining-2026 cash.
 pv_stub=(years[0]['fcff']+years[0]['acquisitions'])*stub/(1+w)**stub
 explicit=sum(y['fcff']/(1+w)**(stub+i) for i,y in enumerate(years[1:],1))
 last=years[-1]
 # Explicit sustainable reinvestment convention: 20% incremental ROIC, R&D remains expensed.
 nopat=last['operating_income']-last['unlevered_tax']
 terminal_fcff=nopat*(1+g)*(1-g/.20)
 if terminal_fcff<=0:raise ValueError('Nonpositive terminal cash flow: reject perpetuity')
 pv_terminal=terminal_fcff/(w-g)/(1+w)**(stub+5)
 ev=pv_stub+explicit+pv_terminal
 equity=ev+BRIDGE['cash']+BRIDGE['investments']-BRIDGE['debt']
 return dict(ev=ev,equity=equity,per_share=equity/BRIDGE['shares'],pv_stub=pv_stub,pv_explicit=explicit,pv_terminal=pv_terminal,terminal_share=pv_terminal/ev,terminal_fcff=terminal_fcff,bridge=BRIDGE,market_price=PRICE)

def run(params=None):
 years=project(params);return {'parameters':BASE|(params or {}),'statements':years,'valuation':value(years,params)}

def reverse_growth():
 lo,hi=-.10,.10
 for _ in range(60):
  mid=(lo+hi)/2
  if run({'growth_shift':mid})['valuation']['per_share']<PRICE:lo=mid
  else:hi=mid
 result=run({'growth_shift':(lo+hi)/2})
 if abs(result['valuation']['per_share']-PRICE)>.01:return {'status':'Price outside bounded growth search; no supported root','low':run({'growth_shift':-.10})['valuation']['per_share'],'high':run({'growth_shift':.10})['valuation']['per_share']}
 return {'growth_shift':(lo+hi)/2,'per_share':result['valuation']['per_share'],'revenue_2031':result['statements'][-1]['revenue'],'status':'solved'}

def all_outputs():
 base=run()
 cases={'downside':{'growth_shift':-.08,'rd_ratio':.22,'capex_shift':.02,'inventory_shift':80.,'wacc':.10,'terminal_growth':.02},'base':{},'upside':{'growth_shift':.05,'rd_ratio':.19,'wacc':.08,'terminal_growth':.03}}
 scenarios={}
 for name,p in cases.items():
  try:scenarios[name]=run(p)['valuation']
  except ValueError as e:scenarios[name]={'status':'FAILED: '+str(e)}
 sensitivity=[{'wacc':w,'g':g,'per_share':value(base['statements'],{'wacc':w,'terminal_growth':g})['per_share']} for w in (.08,.09,.10) for g in (.02,.025,.03)]
 drivers={}
 for key,values in {'rd_ratio':(.18,.20,.22),'capex_shift':(-.02,0.,.02),'growth_shift':(-.05,0.,.05),'inventory_shift':(-50.,0.,50.)}.items():
  rows=[]
  for v in values:
   r=run({key:v});last=r['statements'][-1];rows.append({'input':v,'profit_2031':last['operating_income'],'fcff_2031':last['fcff'],'per_share':r['valuation']['per_share']})
  drivers[key]=rows
 return {'valuation_date':str(DATE),'units':'USD millions except per-share USD; shares millions','base':base,'scenarios':scenarios,'wacc_growth':sensitivity,'driver_sensitivity':drivers,'reverse_dcf':reverse_growth(),'source_status':'Primary annual financials, Q2 LLY shares/bridge and September 8 market closes checked; personal assumption/receipt review pending','recommendation':'watch/defer; do not initiate before source and evidence gaps are closed'}

if __name__=='__main__':
 out=all_outputs();Path('output').mkdir(exist_ok=True);Path('output/visible_output.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ('base','driver_sensitivity','wacc_growth')},indent=2));print('Base value/share:',out['base']['valuation']['per_share'])
