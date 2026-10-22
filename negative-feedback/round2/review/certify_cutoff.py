"""Outward-rounded Decimal interval certificate for K=8/9.

The only transcendental constant is e. Its exact factorial-series bounds are
propagated through all operations using directed rounding at 70 decimal digits.
No float e or float probabilities are used.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from math import factorial, comb
from pathlib import Path
import json

PRECISION=70
def rd(operation,rounding):
    with localcontext() as context:
        context.prec=PRECISION;context.rounding=rounding
        return operation()

class I:
    def __init__(self,low,high=None):
        if isinstance(low,I):self.lo,self.hi=low.lo,low.hi;return
        self.lo=Decimal(str(low));self.hi=self.lo if high is None else Decimal(str(high))
    def __add__(self,other):
        other=I(other)
        return I(rd(lambda:self.lo+other.lo,ROUND_FLOOR),rd(lambda:self.hi+other.hi,ROUND_CEILING))
    __radd__=__add__
    def __neg__(self):
        # Decimal unary minus rounds in the ambient context; copy_negate is exact.
        return I(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self,other):return self+-I(other)
    def __rsub__(self,other):return I(other)+-self
    def __mul__(self,other):
        other=I(other)
        products=[(x,y) for x in [self.lo,self.hi] for y in [other.lo,other.hi]]
        return I(min(rd(lambda:x*y,ROUND_FLOOR) for x,y in products),
                 max(rd(lambda:x*y,ROUND_CEILING) for x,y in products))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=I(other)
        assert other.lo>0 or other.hi<0
        inverse=I(rd(lambda:1/other.hi,ROUND_FLOOR),rd(lambda:1/other.lo,ROUND_CEILING))
        return self*inverse
    def __rtruediv__(self,other):return I(other)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=I(1)
        for _ in range(n):out=out*self
        return out
    def as_dict(self):return {'lower':str(self.lo),'upper':str(self.hi)}

def main():
    n=50
    partial=sum((I(1)/factorial(k) for k in range(n+1)),I(0))
    # For n>=1, sum_{k=n+1}^infty 1/k! < 1/(n*n!).
    tail=I(1)/(n*factorial(n))
    e=I(partial.lo,(partial+tail).hi)
    a=1/e;b=a*a
    z=b+2+e*e
    t0=b/z;t1=1/z;t2=e*e/z
    u=I('.025')+I('.9')*t0
    v=I('.025')+I('.9')*t1
    w=I('.025')+I('.9')*t2
    eta=I('.99')/(z*v)
    results={}
    for k in [8,9]:
        moment1=I(0);moment2=I(0)
        for self_n in range(k+1):
            for adj_n in range(k-self_n+1):
                opp_n=k-self_n-adj_n
                probability=comb(k,self_n)*comb(k-self_n,adj_n)*u**self_n*(2*v)**adj_n*w**opp_n
                denominator=1+self_n+a*adj_n+b*opp_n
                moment1=moment1+probability*adj_n/denominator
                moment2=moment2+probability*adj_n/(denominator*denominator)
        threshold=1-a*moment2/moment1
        curvature=a*moment1*(threshold-eta)
        results[k]={'threshold':threshold,'curvature':curvature,'margin':threshold-eta}
    assert results[8]['threshold'].lo < results[8]['threshold'].hi
    assert results[9]['threshold'].lo < results[9]['threshold'].hi
    assert results[8]['threshold'].hi < eta.lo
    assert eta.hi < results[9]['threshold'].lo
    normal_condition=b*w-a*v
    ratio_condition=t2/t0-1/a
    assert normal_condition.lo>0
    assert ratio_condition.lo>0
    output={'precision':PRECISION,'factorial_series_terms':n+1,
            'e_interval':e.as_dict(),'eta_interval':eta.as_dict(),
            'normal_condition_Bw_minus_Av':normal_condition.as_dict(),
            'ratio_condition_t2_over_t0_minus_e':ratio_condition.as_dict(),
            'K8':{key:value.as_dict() for key,value in results[8].items()},
            'K9':{key:value.as_dict() for key,value in results[9].items()},
            'certificate_passed':True}
    destination=Path(__file__).resolve().parent/'results'/'cutoff_interval_certificate.json'
    destination.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
