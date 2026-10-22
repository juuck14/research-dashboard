"""Scalar symbolic formula audit, independent of the rank sampler code."""
from pathlib import Path
import csv,json,math

OUT=Path(__file__).resolve().parent/'results'
EPS=.1
sigmoid=lambda x:1/(1+math.exp(-x))
r=sigmoid(-1);s=sigmoid(-2)
v=(1+EPS)/6
w=(2-EPS)/3

def velocity(delta,tolerance):
    # Adjacent scores are +-cos(2theta), theta=pi/4+delta.
    score=math.cos(math.pi/2+2*delta)
    derivative=-2*math.sin(math.pi/2+2*delta)
    if abs(2*score)<=tolerance:
        qminus=qplus=v
    elif score<0:
        qminus=1/3;qplus=EPS/3
    else:
        qminus=EPS/3;qplus=1/3
    grad=qminus*sigmoid(score-1)*derivative-qplus*sigmoid(-score-1)*derivative
    return -grad/4

rows=[]
for delta in [1e-3,1e-6,1e-10,1e-13,1e-14]:
    for tolerance in [0.,1e-12]:
        rows.append(dict(delta=delta,tie_tolerance=tolerance,
                         theta_velocity=velocity(delta,tolerance),
                         limit=(1-EPS)*r/6))
with (OUT/'quantile_tolerance.csv').open('w') as handle:
    writer=csv.DictWriter(handle,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
summary=dict(frozen_normal_ab_curvature=w*s-v*r,
             frozen_stability_epsilon_upper=(4*s-r)/(2*s+r),
             one_sided_limit=(1-EPS)*r/6,
             tolerance_1e12_at_delta_1e14=velocity(1e-14,1e-12),
             ideal_at_delta_1e14=velocity(1e-14,0.))
(OUT/'quantile_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
assert summary['frozen_normal_ab_curvature']>0
assert summary['tolerance_1e12_at_delta_1e14']<0
assert summary['ideal_at_delta_1e14']>0
