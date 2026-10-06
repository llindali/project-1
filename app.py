"""Local driver workbench. No packages, credentials or hosting required."""
import json
from http.server import HTTPServer,BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse,parse_qs
import model
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  u=urlparse(self.path)
  if u.path=='/api':
   try:
    q=parse_qs(u.query);p={k:float(v[0]) for k,v in q.items() if k in model.BASE}
    r=model.run(p)
    if q.get('failure')==['1']:
     r['statements'][2]['cash']+=1000
     prev=r['statements'][1];bad=model.s.checks(r['statements'][2],prev)
     raise ValueError('Deliberate accounting corruption: '+str({k:v for k,v in bad.items() if abs(v)>.01}))
    r['base_value']=model.run()['valuation']['per_share'];r['status']='PASS: all statement and FCFF checks'
    payload=json.dumps(r);status=200
   except (ValueError,KeyError) as e:payload=json.dumps({'error':str(e)});status=422
   self.send_response(status);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(payload.encode())
  elif u.path in ('/','/index.html'):
   self.send_response(200);self.send_header('Content-Type','text/html');self.end_headers();self.wfile.write(Path(__file__).with_name('index.html').read_bytes())
  else:self.send_error(404)
if __name__=='__main__':
 print('Open http://127.0.0.1:8000 — Ctrl+C to stop',flush=True)
 HTTPServer(('127.0.0.1',8000),Handler).serve_forever()
