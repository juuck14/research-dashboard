"""Late-added natural exponential and DCL checks requested by the root.

These checks were specified after the original audit and are recorded as such.
They use the independently implemented ordered-tuple oracle from audit.py.
"""
from audit import finite_difference,predicted,save_csv,OUT
import numpy as np
import json

fd=[];moments=[]
for k in [1,2,4,5]:
    for positive in [0.,1.]:
        fd.extend(finite_difference(k,0.,1e-5,False,float(np.log(4)),.3,positive))
for k in [4,5,7,8]:
    for positive in [0.,1.]:
        numbers,_=predicted(k,0.,float(np.log(4)),.3,positive)
        moments.append(dict(K=k,positive=positive,**numbers))
save_csv('natural_dcl_ordered_fd.csv',fd)
save_csv('natural_dcl_moments.csv',moments)
summary={'ordered_fd_checks':len(fd),'max_eigen_error':max(x['max_eigen_error'] for x in fd),
         'max_stationary_residual':max(x['stationary_residual'] for x in fd),
         'natural_Info_K4':next(x for x in moments if x['K']==4 and x['positive']==1),
         'natural_Info_K5':next(x for x in moments if x['K']==5 and x['positive']==1),
         'natural_DCL_K7':next(x for x in moments if x['K']==7 and x['positive']==0),
         'natural_DCL_K8':next(x for x in moments if x['K']==8 and x['positive']==0)}
(OUT/'natural_dcl_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
assert summary['max_eigen_error']<2e-7
