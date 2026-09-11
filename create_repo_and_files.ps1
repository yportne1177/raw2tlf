param(
  [string]$Root = "concept-to-sdtm",
  [string]$Remote = "https://github.com/your-org/your-repo.git"
)

Set-StrictMode -Version Latest

# compute root path and report it
$rootPath = Join-Path (Get-Location) $Root
Write-Host "Creating repo skeleton at $rootPath"

# Create folders
New-Item -ItemType Directory -Path $Root -Force | Out-Null
Set-Location $Root
$dirs = @(
  "mappings\lab","mappings\ae","mappings\ex",
  "runner\templates",
  "databricks\notebooks","databricks\udfs",
  "tests\fixtures",
  "ci"
)
foreach ($d in $dirs) { New-Item -ItemType Directory -Path $d -Force | Out-Null }

# Write README.md
@"
# Concept to SDTM

A minimal repo to go from a biomedical concept to SDTM using declarative YAML mapping and a Databricks runner.

## Repository layout

```text
concept-to-sdtm/
├─ README.md
├─ LICENSE
├─ mappings/
│  ├─ lab/
│  │  └─ anc_mapping.yaml
│  ├─ ae/
│  │  └─ myocardial_infarction.yaml
│  └─ ex/
│     └─ infusion_exposure.yaml
├─ runner/
│  ├─ mapping_runner.py
│  ├─ templates/
│  │  ├─ lb_template.sql.j2
│  │  ├─ ae_template.sql.j2
│  │  └─ ex_template.sql.j2
│  └─ utils.py
├─ databricks/
│  ├─ notebooks/
│  │  ├─ 01_ingest_and_canonicalize.sql
│  │  ├─ 02_run_mapping_runner.py
│  │  └─ 03_postprocess_and_audit.sql
│  └─ udfs/
│     └─ conversion_udfs.py
├─ tests/
│  ├─ fixtures/
│  │  ├─ landing_lab.csv
│  │  ├─ landing_ae.csv
│  │  └─ landing_ex.csv
│  └─ test_mapping_runner.py
└─ ci/
   └─ pipeline.yml
"@ > README.md
