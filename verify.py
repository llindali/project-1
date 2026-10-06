"""Reproducibility and interface checks; no external dependencies."""
import datetime,json,subprocess,tempfile,shutil,threading,urllib.request,urllib.error
from pathlib import Path
import app

def main():
 root=Path(__file__).parent;lines=['Cold run UTC '+datetime.datetime.now(datetime.timezone.utc).isoformat(),'Fresh Python venv; no packages installed.']
 with tempfile.TemporaryDirectory() as td:
  dst=Path(td)/'project';shutil.copytree(root,dst,ignore=shutil.ignore_patterns('.git','__pycache__','.venv'));env=Path(td)/'env';subprocess.run(['python','-m','venv',str(env)],check=True);py=str(env/'bin/python')
  if not Path(py).exists():py=str(env/'Scripts/python.exe')
  for args in [['model.py'],['peers.py'],['-m','unittest','-v']]:
   r=subprocess.run([py]+args,cwd=dst,capture_output=True,text=True);lines+=['Command: python '+' '.join(args),'Exit: '+str(r.returncode),r.stdout,r.stderr]
   if r.returncode:raise RuntimeError('Cold run failed; inspect console')
 (root/'output/cold-run.log').write_text('\n'.join(lines))
 server=app.HTTPServer(('127.0.0.1',0),app.Handler);threading.Thread(target=server.serve_forever,daemon=True).start();port=server.server_address[1];checks=[]
 try:
  for q in ['', '?rd_ratio=.22','?failure=1','']:
   try:
    r=urllib.request.urlopen(f'http://127.0.0.1:{port}/api'+q);d=json.load(r);checks.append({'query':q,'status':r.status,'value':d['valuation']['per_share']})
   except urllib.error.HTTPError as e:checks.append({'query':q,'status':e.code,'message':json.load(e)})
 finally:server.shutdown();server.server_close()
 assert [r['status'] for r in checks]==[200,200,422,200]
 assert checks[1]['value']<checks[0]['value'] and checks[-1]['value']==checks[0]['value']
 (root/'output/interface-check.log').write_text(json.dumps(checks,indent=2));print('Cold run and interface change/failure/recovery passed.')
if __name__=='__main__':main()
