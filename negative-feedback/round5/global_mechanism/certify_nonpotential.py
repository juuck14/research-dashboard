"""Exact rational sign of a realizable K1 no-self integrating-factor obstruction."""
from fractions import Fraction as F
from pathlib import Path
import json, math

ROOT=Path(__file__).resolve().parent
r=[F(6,5),F(4,5),F(7,5)]
eps=F(1,20);t=3
def q(a,b):return eps/2+(1-eps)/(1+(a/b)**t)
def k(a,b):
    z=(a/b)**t
    return t*(1-eps)*z/(1+z)**2
A=[sum(q(r[i],r[j]) for j in range(3) if j!=i) for i in range(3)]
# C dot curl(C) = e/[9*prod(e+r_i)] * S, by differentiating
# logistic f_i=r_i/(e+r_i) and each two-candidate row probability.
S=(A[0]*r[0]*k(r[1],r[2])*(r[2]-r[1])
   +A[1]*r[1]*k(r[2],r[0])*(r[0]-r[2])
   +A[2]*r[2]*k(r[0],r[1])*(r[1]-r[0]))
assert S!=0
value=math.e*float(S)/(9*math.prod(math.e+float(v) for v in r))
result={'C':3,'K':1,'epsilon':'1/20','sampler_t':3,
        'Gram_off_diagonals':['log(6/5)','log(4/5)','log(7/5)'],
        'realizability':'unit diagonal and strict diagonal dominance; each absolute off-diagonal is below .4 and every row sum below .65',
        'rational_S_numerator':S.numerator,'rational_S_denominator':S.denominator,
        'S_nonzero_exact':True,'frobenius_formula':'exp(1)*S/[9 product_i(exp(1)+r_i)]',
        'frobenius_numeric_illustration':value,
        'conclusion':'No smooth positive scalar integrating factor turns this K1 Gram update one-form into an exact differential locally.',
        'scope':'constructed exact counterexample after exploratory FD; not a new harm result or top-journal importance proof'}
(ROOT/'nonpotential_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
