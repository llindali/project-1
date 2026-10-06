"""Run only after Linda writes and freezes her own AI-off prediction."""
import json,subprocess,datetime
from pathlib import Path
import model
p=Path('evidence/human-prediction.json')
if not p.exists():raise SystemExit('STOP: human prediction absent. See docs/student-actions.md. No locked test executed.')
r=json.loads(p.read_text())
required=['prediction','decision_effect','input','old','new','units','timestamp','ai_off_attestation']
if not all(k in r for k in required) or not r['prediction'] or r['ai_off_attestation'] is not True:raise SystemExit('Incomplete human-authored prediction; test refused')
commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
if subprocess.check_output(['git','status','--porcelain','--',str(p)],text=True).strip():raise SystemExit('Prediction must be committed before execution')
if r['input'] not in model.BASE or r['old']!=model.BASE[r['input']]:raise SystemExit('Input/baseline does not match model')
before=model.run()['valuation'];after=model.run({r['input']:r['new']})['valuation']
result={'prediction_record':r,'precommit':commit,'execution_timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'before':before,'after':after,'reconciliation':'Linda must explain agreement/divergence and actual decision effect after execution.'}
Path('output/locked-test-result.json').write_text(json.dumps(result,indent=2));print('Saved output/locked-test-result.json; complete human reconciliation.')
