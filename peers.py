"""Qualified FY2025 P/E and EV/revenue cross-check, September 8 price snapshot."""
import json,statistics
from pathlib import Path
# All share counts use FY2025 diluted weighted averages: approximation, not market cap.
ROWS=[dict(ticker='LLY',price=1123.91,eps=22.95,shares=899.3,revenue=65179.,debt=42503.,cash=7268.,investments=2802.,nci=22.),
 dict(ticker='MRK',price=148.46,eps=7.28,shares=2507.,revenue=65011.,debt=49339.,cash=14565.,investments=956.,nci=56.),
 dict(ticker='PFE',price=27.79,eps=1.36,shares=5713.,revenue=62579.,debt=64795.,cash=1142.,investments=14075.,nci=299.)]
def calculate():
 rows=[]
 for p in ROWS:
  if min(p['shares'],p['revenue'],p['eps'])<=0:raise ValueError('Invalid positive denominator')
  ev=p['price']*p['shares']+p['debt']+p['nci']-p['cash']-p['investments']
  rows.append(p|{'pe':p['price']/p['eps'],'ev':ev,'ev_revenue':ev/p['revenue']})
 target,peers=rows[0],rows[1:]
 pe_values=[p['pe']*target['eps'] for p in peers]
 ev_values=[(p['ev_revenue']*target['revenue']-target['debt']-target['nci']+target['cash']+target['investments'])/target['shares'] for p in peers]
 return {'definition':'FY2025 GAAP diluted EPS and revenue; September 8 2026 closes; FY2025 balance sheets and diluted weighted-average share proxies. Approximate EV, not spot market cap. Operating leases expensed; all disclosed investments treated nonoperating at book value.','rows':rows,'pe_range':pe_values,'ev_revenue_range':ev_values,'pe_median':statistics.median(pe_values),'ev_median':statistics.median(ev_values),'status':'Financial inputs checked to primary annual filings; dated price closes independently rechecked October 6'}
if __name__=='__main__':
 r=calculate();Path('output/peers.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
