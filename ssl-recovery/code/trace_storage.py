"""Keep complete traces outside git; publish every run on a fixed 500-step grid."""
import csv,hashlib,itertools,json,os,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]

def store_traces(name,records):
 out=pathlib.Path(os.environ.get('SSL_RECOVERY_RAW_DIR','/tmp/ssl-recovery-raw'));out.mkdir(parents=True,exist_ok=True)
 raw=out/f'{name}_traces.json';raw.write_text(json.dumps(records));data=raw.read_bytes()
 def group(r):return (r['seed'],r['policy'],r.get('rho3',''))
 ends={}
 for r in records:ends[group(r)]=max(ends.get(group(r),0),r['step'])
 fields=['seed','policy','rho3','step','f_r2_1','f_r2_2','f_r2_3','t_r2_1','t_r2_2','t_r2_3','loss','teacher_gap']
 selected=[]
 for r in records:
  if r['step']%500 and r['step']!=ends[group(r)]:continue
  row={k:r.get(k,'') for k in fields}
  for j in [1,2,3]:
   if f'r2_{j}' in r:row[f'f_r2_{j}']=r[f'r2_{j}']
  selected.append(row)
 compact=ROOT/'results'/f'{name}_curves.csv'
 with compact.open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(selected)
 meta=dict(raw_path=str(raw),raw_bytes=len(data),raw_sha256=hashlib.sha256(data).hexdigest(),raw_rows=len(records),compact_path=compact.name,compact_rows=len(selected),selection='Every run: step divisible by 500, plus its final step. No outcome-based selection.',reason='Complete metrics are deterministic and regenerable; large repetitive traces remain outside git. All final values and recovery metrics stay in per-run summaries.')
 (ROOT/'results'/f'{name}_trace_manifest.json').write_text(json.dumps(meta,indent=2))
 return meta
