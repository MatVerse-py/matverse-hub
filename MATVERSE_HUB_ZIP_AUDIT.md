# MatVerse Hub ZIP Audit — v0.1.0-alpha readiness

## Input

- File: `matverse-hub-main.zip`
- Size: `24641` bytes
- SHA-256: `8f95f700284af3dba159982893b1166b2ea78b3a973daf5a61b3c5eb75b5ecdf`
- Entries: `18`
- Files: `14`
- Directories: `4`
- Uncompressed size: `53743` bytes

## Decision

```text
ALPHA_RELEASE_READINESS   = PASS
ZENODO_ARCHIVAL_READINESS = PASS
PRODUCTION_READINESS      = HOLD
PUBLIC_VALIDATION         = HOLD_EXTERNAL_REQUIRED
```

## Structural findings

The ZIP is small, clean and structurally coherent. It contains one top-level directory: `matverse-hub-main`.

Observed components:

```text
README.md
SECURITY.md
artifact_engineering_report.md
omega_gate_validator.py
dashboard.py
index-repos.py
scripts/index-repos-v2.py
scripts/dashboard_static.py
docs/INDEXING_GUIDE_v2.md
hf_space/app.py
hf_space/README.md
hf_space/requirements.txt
hf_space/proof_data.json
```

## Hygiene checks

```text
ZipSlip/path traversal       = PASS
.venv / node_modules / cache = NOT_FOUND
__pycache__ / .pyc           = NOT_FOUND
.env / private keys          = NOT_FOUND
basic secret scan            = PASS
Python syntax compile        = PASS
```

Python files compiled with return code 0. The local Python runtime emitted unrelated environment startup warnings, but compilation itself returned success for every `.py` file.

## Missing release hardening files

```text
LICENSE        = MISSING
CITATION.cff   = MISSING
codemeta.json  = MISSING
CHANGELOG.md   = MISSING
RELEASE_NOTES  = MISSING
MANIFEST.json  = MISSING
HASHES.sha256  = MISSING
```

I generated suggested versions for the key release-support files in this supplement package.

## Claim hygiene

Allowed:

```text
Archived alpha release of MatVerse Hub as public governance and witness layer.
```

Blocked:

```text
Externally validated platform.
Production-ready public runtime.
Institutionally closed science.
Proof of digital life.
Final truth status.
```

## Recommendation

Publish as:

```text
tag: v0.1.0-alpha
pre-release: true
release title: MatVerse Hub v0.1.0-alpha — Scientific Governance & Public Witness Layer
```

Then let Zenodo archive the GitHub release and generate the DOI. After DOI generation, add the DOI badge to `README.md`.
