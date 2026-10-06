"""Verify the frozen R&D proposal with explicitly disclosed AI-assisted execution."""
import json,subprocess,datetime
from pathlib import Path
import model
p=Path('evidence/rd-prediction-record.json')
assert not subprocess.check_output(['git','status','--porcelain','--',str(p)],text=True).strip()
r=json.loads(p.read_text());assert r['old']==model.BASE[r['input']]
before=model.run()['valuation']
normal_bounds=model.BOUNDS[r['input']]
try:
 model.run({r['input']:r['new']})
except ValueError as exc:
 guard_failure=str(exc)
else:
 guard_failure=None
try:
 # Isolated exploratory range extension; shipped workbench bounds stay unchanged.
 model.BOUNDS[r['input']]=(min(normal_bounds[0],r['new']),normal_bounds[1])
 after=model.run({r['input']:r['new']})['valuation']
finally:
 model.BOUNDS[r['input']]=normal_bounds
result={'prediction_record':r,'precommit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'execution_timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'execution_mode':'AI-assisted; not a human AI-off locked test','normal_bounds':normal_bounds,'guard_failure':guard_failure,'range_exception':'17% exploratory stress test outside normal 18%–24% range; production bounds unchanged','before':before,'after':after,'delta_per_share':after['per_share']-before['per_share'],'percent_change':100*(after['per_share']/before['per_share']-1)}
Path('output/rd-assisted-test-result.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
