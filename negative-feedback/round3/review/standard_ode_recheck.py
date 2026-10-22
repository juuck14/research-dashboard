"""Replay the author's standard ODE control without altering its result file.

This is independent execution, not a second oracle or gradient implementation.
"""
from pathlib import Path
import sys

review = Path(__file__).resolve().parent
neural = review.parent/'neural'
sys.path.insert(0, str(neural))
path = neural/'standard_ode_check.py'
source = path.read_text().replace("OUT=ROOT/'results'", 'OUT=Path('+repr(str(review))+')')
source = source.replace('standard_ode_check.json', 'standard_ode_recheck.json')
exec(compile(source, str(path), 'exec'), {'__file__':str(path), '__name__':'__main__'})
