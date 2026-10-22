"""Independent surrogate formula audit, protocol amendment 1."""
import json
from pathlib import Path
import numpy as np
ts=np.linspace(0,np.pi,10001)
R=np.array([[np.cos(ts),-np.sin(ts)],[np.sin(ts),np.cos(ts)]]).transpose(2,0,1)
c=2**-.5
out=[]
for k in 10.**-np.arange(1,9):
    A=np.array([[1.,0],[0,1],[c,c],[c,-c],[k,0],[0,k]])
    C=np.einsum('ij,njk->nik',A,R)
    value=np.abs(C[:,:,0]*C[:,:,1]).sum(1)
    exact=(1+k*k)*np.abs(np.sin(2*ts))+np.abs(np.cos(2*ts))
    out.append(dict(kappa=float(k),max_error=float(np.max(np.abs(value-exact))),
                    near_minimum_gap=float((1+k*k)-1),predicted_gap=float(k*k)))
p=Path(__file__).parent/'results'/'surrogate_audit.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
