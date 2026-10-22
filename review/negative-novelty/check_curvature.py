"""Independent exact square-angle curvature verification, no sampling."""
import json,math
from pathlib import Path
import numpy as np
from scipy.special import expit,softmax

def field(theta,k,eps):
 c=math.cos(2*theta);cp=-2*math.sin(2*theta)
 scores=np.array([1.,c,-c,-1.]);ds=np.array([0.,cp,-cp,0.])
 q=(1-eps)*softmax(k*scores)+eps/4
 return float(np.dot(q,expit(scores-1)*ds))
rows=[]
for k in [-10.,-2.,-1.,0.,1.]:
 eps=.1;Z=math.exp(k)+math.exp(-k)+2;q0=(1-eps)/Z+eps/4
 lp=expit(-1);lpp=lp*(1-lp)
 frozen=8*q0*lpp;reaction=8*(1-eps)*k*lp/Z
 h=1e-5;fd=(field(math.pi/4+h,k,eps)-field(math.pi/4-h,k,eps))/(2*h)
 rows.append(dict(kappa=k,eps=eps,frozen=frozen,reaction=reaction,adaptive=frozen+reaction,finite_difference=fd,error=abs(fd-frozen-reaction)))
path=Path(__file__).with_name('curvature_check.json');path.write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
