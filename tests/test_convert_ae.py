import pandas as pd
from pathlib import Path
import subprocess, sys

def test_ae_conversion(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    mapping = repo_root / 'mappings' / 'ae_mapping.yaml'
    input_csv = repo_root / 'data' / 'sample_raw' / 'ae.csv'
    out_csv = tmp_path / 'ae_tlf.csv'
    cmd = [sys.executable, str(repo_root / 'convert.py'),
           '--mapping', str(mapping),
           '--input', str(input_csv),
           '--output', str(out_csv)]
    subprocess.check_call(cmd)
    out = pd.read_csv(out_csv)
    assert 'SUBJECT_ID' in out.columns
    assert len(out) == 2
    assert out.loc[0, 'AE_TERM'] == 'Headache'
