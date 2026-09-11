# raw2tlf

Simple converter that transforms raw clinical CSVs into TLF-style CSV outputs.

Quickstart (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python convert.py --mapping mappings\ae_mapping.yaml --input data\sample_raw\ae.csv --output data\sample_tlf\ae_tlf.csv
pytest -q
