"""Integrity of evidence-bearing files; does not rerun or invent experiments."""
from pathlib import Path
import re,json,csv,hashlib,platform
ROOT=Path(__file__).resolve().parent
errors=[];links=0;py=0;js=0;cs=0;manifest=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    if p.name not in ['artifact_manifest.json','artifact_qa.json']:
        data=p.read_bytes();manifest.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    if p.suffix=='.md':
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text()):
            if '://' in target or target.startswith('#'):continue
            dest=target.split('#')[0]
            if not dest:continue
            links+=1
            if not (p.parent/dest).exists():errors.append(f'Broken link {p.relative_to(ROOT)} -> {target}')
    elif p.suffix=='.py':
        py+=1
        try:compile(p.read_text(),str(p),'exec')
        except Exception as e:errors.append(f'Python syntax {p}: {e}')
    elif p.suffix=='.json':
        js+=1
        try:json.loads(p.read_text())
        except Exception as e:errors.append(f'JSON {p}: {e}')
    elif p.suffix=='.csv':
        cs+=1
        with p.open() as f:
            reader=csv.reader(f);header=next(reader)
            if any(len(row)!=len(header) for row in reader):errors.append(f'CSV shape {p}')

read=lambda path:json.loads((ROOT/path).read_text())
d=read('dynamics/results/summary.json')
assert d['runs']==16 and d['passed']==16
enc=read('encoder/results/summary.json')
assert enc['runs']==36 and not enc['warmup_failures']
assert enc['criteria']['warmup/primary']['passed']==1
assert enc['criteria']['warmup/confirmation']['passed']==3
assert len(read('encoder/results/models.json'))==36
groups=read('theory/results/denominator_summary.json')['groups']
assert {(r['kind'],r['positive']):r['first_stable_K'] for r in groups}=={('natural',0):8,('natural',1):5,('matched',0):14,('matched',1):9}
review=read('review/results/summary.json')
assert review['ordered_tuple_fd_checks']==62
report={'scope':'Artifact integrity and saved-result consistency; not a new experimental replication',
        'python':platform.python_version(),'markdown_local_links':links,'python_sources':py,'json_files':js,'csv_files':cs,
        'manifest_files':len(manifest),'dynamics_criteria_passed':16,'encoder_runs':36,
        'strong_encoder_endpoint':'failed: primary1/3,confirmation3/3',
        'errors':errors,'passed':not errors}
(ROOT/'artifact_qa.json').write_text(json.dumps(report,indent=2)+'\n')
(ROOT/'artifact_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(report,indent=2))
assert not errors,errors
