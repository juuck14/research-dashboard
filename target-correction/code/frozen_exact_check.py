#!/usr/bin/env python3
"""Check an existing finite-time trajectory against exact logistic solution."""
from pathlib import Path
import csv,json,math

p=Path(__file__).resolve().parents[1]/'results'
summary=json.loads((p/'summary.json').read_text())
c=summary['frozen_contrast'];r,e,s=c['rho'],c['eta'],c['initial'];k=r*s-e
rows=list(csv.DictReader((p/'frozen_vs_ema.csv').open()))
frozen=[x for x in rows if x['teacher']=='frozen']
err=[]
for x in frozen:
 t=float(x['time']); exact=math.sqrt(k/(1+(k/(s*s)-1)*math.exp(-2*k*t)))
 err.append(abs(float(x['w'])-exact))
result={'max_finite_time_solution_error':max(err),'final_time':float(frozen[-1]['time']),
 'observed_frozen_final':float(frozen[-1]['w']),
 'asymptotic_frozen_equilibrium':math.sqrt(k),
 'observed_ema_final':float([x for x in rows if x['teacher']=='EMA'][-1]['w'])}
(p/'frozen_exact_check.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
