# Reproduction after the interrupted upload

The original published checkpoint remains256f7e94225174aac36eeb0667a8f6a9741992a1. Its82 round5 files are intact. Later unpublished raw files were pruned during an interruption; they are not claimed byte-for-byte recovered. The full global proof was restored from its recorded derivation and independently reviewed again. Critical experiments and independent checks below were newly executed2026-10-25.

From repository root, with Python3.12 and NumPy2.3.5/SciPy1.17.0:

```bash
python -m pip install numpy==2.3.5 scipy==1.17.0
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python negative-feedback/round5/recovery/population_rerun.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python negative-feedback/round5/recovery/independent_check.py
```

The population script imports the checkpoint's round3/neural/oracle.py; the independent script does not import it. Protocols were saved before the respective executions. Both commands overwrite their owned new outputs; run in a disposable copy to retain original recovery outputs. No GPU, external dataset or credential is needed.

- [Full theorem](theory_value/global_count_recovery.md) and [new independent proof review](recovery/proof_review.md).
- [Population protocol](recovery/protocol.md), [code](recovery/population_rerun.py), [all16 arrays/metrics/spectra](recovery/population_rerun.json), [stdout](recovery/population_rerun.log).
- [Independent protocol](recovery/independent_protocol.md), [separate direct tuple code](recovery/independent_check.py), [complete JSON](recovery/independent_check.json), [CSV](recovery/independent_cases.csv), [results](recovery/independent_results.md).
- [Recovery provenance and limits](recovery/STATUS.md). Historical conversation summaries are distinguished from current executable evidence.
