"""Directed-rounding finite-sum certificates for natural and DCL controls."""
from certify_cutoff import I,PRECISION
from math import comb,factorial
from pathlib import Path
import json

n=50
partial=sum((I(1)/factorial(k) for k in range(n+1)),I(0))
e=I(partial.lo,(partial+I(1)/(n*factorial(n))).hi)
a=1/e;b=a*a
# log(4)=4 atanh(1/3), with a positive geometric bound on the remainder.
x=I(1)/3
nlog=90
logpartial=sum((4*x**(2*k+1)/(2*k+1) for k in range(nlog)),I(0))
logtail=4*x**(2*nlog+1)/((2*nlog+1)*(1-x*x))
log4=I(logpartial.lo,(logpartial+logtail).hi)

def threshold(k,q,positive):
    u,v,w=q
    m1=I(0);m2=I(0)
    for self_n in range(k+1):
        for adj_n in range(k-self_n+1):
            opp_n=k-self_n-adj_n
            probability=comb(k,self_n)*comb(k-self_n,adj_n)*u**self_n*(2*v)**adj_n*w**opp_n
            denominator=positive+self_n+a*adj_n+b*opp_n
            m1=m1+probability*adj_n/denominator
            m2=m2+probability*adj_n/(denominator*denominator)
    return 1-a*m2/m1

natural_q=[I('.103'),I('.187'),I('.523')]
natural_eta=I(112)*log4/187
z=b+2+e*e
matched_q=[I('.025')+I('.9')*p for p in [b/z,1/z,e*e/z]]
matched_eta=I('.99')/(z*matched_q[1])
rows=[]
for kind,q,eta,positive,ks in [
        ('natural',natural_q,natural_eta,1,[4,5]),
        ('natural',natural_q,natural_eta,0,[7,8]),
        ('matched',matched_q,matched_eta,0,[13,14])]:
    pair=[]
    for k in ks:
        t=threshold(k,q,positive);margin=t-eta
        rows.append(dict(kind=kind,positive=positive,K=k,eta=eta.as_dict(),
                         threshold=t.as_dict(),margin=margin.as_dict()))
        pair.append(margin)
    assert pair[0].hi<0<pair[1].lo
natural_normal=b*natural_q[2]-a*natural_q[1]
assert natural_normal.lo>0
output=dict(precision=PRECISION,log4_interval=log4.as_dict(),
            natural_normal_condition=natural_normal.as_dict(),results=rows,
            certificate_passed=True)
destination=Path(__file__).resolve().parent/'results'/'control_interval_certificate.json'
destination.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
