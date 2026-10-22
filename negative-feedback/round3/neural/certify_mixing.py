"""Exact upper-window bracket via existing independently reviewed interval arithmetic."""
from pathlib import Path
import sys,json
from math import comb,factorial
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]/'round2'/'review'))
from certify_cutoff import I,PRECISION

n=50;partial=sum((I(1)/factorial(k) for k in range(n+1)),I(0))
e=I(partial.lo,(partial+I(1)/(n*factorial(n))).hi);a=1/e;b=a*a
u,v,w=I('.103'),I('.187'),I('.523');rho=I('.05');rows=[]
for K in [11,12]:
    b0=b1=b2=I(0)
    for U in range(K+1):
        for N in range(K-U+1):
            W=K-U-N;p=comb(K,U)*comb(K-U,N)*u**U*(2*v)**N*w**W;D=1+U+a*N+b*W
            b0=b0+p*U/D;b1=b1+p*a*N/(2*D);b2=b2+p*b*W/D
    total=b0+2*b1+b2;xi=(b0-b2)/total;margin=rho-xi
    rows.append({'K':K,'critical_mixing':xi.as_dict(),'rho_minus_critical':margin.as_dict(),
                 'normal_curvature_m4':((b1+b2-total*(1-rho)/2)/4).as_dict()})
assert I(rows[0]['rho_minus_critical']['lower']).lo>0
assert I(rows[1]['rho_minus_critical']['upper']).hi<0
limit=(u-b*w)/(u+2*a*v+b*w)
output={'precision':PRECISION,'e_interval':e.as_dict(),'rho':'.05','upper_bracket':rows,
        'critical_mixing_limit':limit.as_dict(),'passed':True,
        'scope':'Combined with strict mixing threshold monotonicity and prior K4/5 balance certificate, full square stability holds exactly for K5..11.'}
(ROOT/'results'/'mixing_interval_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
