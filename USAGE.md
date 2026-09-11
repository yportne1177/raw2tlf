# Usage and Developer Instructions

This file contains the detailed, step-by-step instructions for using and developing this repository.

---

## 1. Quick overview

This repository provides:
- A Python converter (convert.py) that applies YAML mappings to input data.
- Example mappings in mappings/.
- Example inputs in examples/ and data/.
- Unit tests in tests/.
- A PowerShell helper create_repo_and_files.ps1 to scaffold a project skeleton.

---

## 2. Prepare your environment (Windows)

1. Open PowerShell and go to the repo root:
   Set-Location C:\repo\raw2tlf

2. Create and activate a Python virtual environment:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip

3. Install Python dependencies:
   pip install -r requirements.txt

---

## 3. Inspect the code before running anything

- Show the top of the converter to find usage or help text:
  Get-Content convert.py -TotalCount 200

- Look for argparse or a main block to find CLI options.
- Open a mapping YAML to understand source→target mappings:
  notepad mappings\lab\anc_mapping.yaml

---

## 4. Run the converter (example)

Replace the arguments below with the actual CLI options shown by python convert.py --help:

python convert.py --input examples/sample_input.csv --mapping mappings/lab/anc_mapping.yaml --output out/

Check the out/ folder for generated SDTM-style files.

---

## 5. Run tests

# Ensure venv is active
.\.venv\Scripts\Activate.ps1
pip install pytest
pytest -q

If tests fail, copy the failing traceback and paste it here for the single next command to fix it.

---

## 6. Common maintenance tasks

Convert file encodings to UTF-8 if GitHub warns about UTF-16LE:
Get-Content README.md -Raw -Encoding Unicode | Set-Content README.md -Encoding UTF8

If the script created a nested folder concept-to-sdtm and you want its contents at repo root (preview first):
Get-ChildItem -Path .\concept-to-sdtm -Recurse | Select-Object FullName
Move-Item -Path .\concept-to-sdtm\* -Destination . -Force
Remove-Item -Recurse -Force .\concept-to-sdtm

---

## 7. Git workflows

Safe: push changes on a branch and open a PR:
git fetch origin
git checkout -b publish/all-files
git add .
git commit -m "chore: publish repository files and usage instructions"
git push -u origin publish/all-files
Start-Process "https://github.com/yportne1177/raw2tlf/compare/main...publish/all-files"

Direct push to main (only if you are certain):
git checkout main
git add .
git commit -m "chore: update repo files"
git push origin main

---

## 8. If something goes wrong

- git commit says “nothing to commit”: run git status --porcelain and inspect output.
- Remote errors: run git remote -v and git ls-remote origin to diagnose.
- Script blocked by policy: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

---

## 9. Next recommended steps

1. Run the converter on a sample input to confirm behavior.
2. Open and read tests/test_mapping_runner.py to see concrete examples.
3. If you want, create a small example mapping and input, run the converter, and commit the results to a feature branch.
