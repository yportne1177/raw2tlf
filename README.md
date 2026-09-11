# raw2tlf
Raw data to tlf
# raw2tlf

Simple converter that transforms raw clinical CSVs into TLF-style CSV outputs.

## Quickstart

Create a virtual environment and install dependencies:

# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

Run the converter on sample data:
python convert.py --mapping mappings/ae_mapping.yaml --input data/sample_raw/ae.csv --output data/sample_tlf/ae_tlf.csv

Run tests:
pytest -q

## Contributing
- Fork the repo, create a feature branch, add tests, and open a PR.
