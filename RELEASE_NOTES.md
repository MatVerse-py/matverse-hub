# MatVerse Hub v0.1.0-alpha — Release Notes

## Decision

`PASS_FOR_ALPHA_RELEASE`

This package is suitable for an alpha GitHub release and Zenodo archival DOI, with pre-release status enabled.

## Scope

This release preserves the initial MatVerse Hub repository as a public governance and witness layer for the MatVerse / IQG scientific platform.

Included repository components observed in the uploaded ZIP:

- `README.md`
- `SECURITY.md`
- `artifact_engineering_report.md`
- `omega_gate_validator.py`
- `dashboard.py`
- `index-repos.py`
- `scripts/index-repos-v2.py`
- `scripts/dashboard_static.py`
- `docs/INDEXING_GUIDE_v2.md`
- `hf_space/app.py`
- `hf_space/README.md`
- `hf_space/requirements.txt`
- `hf_space/proof_data.json`

## Audit summary

- ZIP SHA-256: `8f95f700284af3dba159982893b1166b2ea78b3a973daf5a61b3c5eb75b5ecdf`
- ZIP size: `24641` bytes
- ZIP entries: `18`
- Files: `14`
- Path traversal check: `PASS`
- Dirty artifact scan: `PASS`
- Basic secret scan: `PASS`
- Python syntax compile: `PASS`
- Tests discovered: `NOT_FOUND`

## Release status

Allowed claim:

> MatVerse Hub v0.1.0-alpha is an archived alpha public governance and witness layer for the MatVerse / IQG scientific platform.

Blocked claim:

> This release proves external scientific validation, production readiness, institutional closure, or proof of digital life.

## Required improvements before non-alpha release

- Add an explicit `LICENSE`
- Add `CITATION.cff`
- Add `codemeta.json`
- Add canonical `MANIFEST.json`
- Add `HASHES.sha256`
- Add test suite for `omega_gate_validator.py`
- Replace demo/fake hashes in `hf_space/proof_data.json` with clearly labeled seed/demo records or real evidence records
- Add reproducible evidence pack
- Add ledger/replay artifact if claiming runtime proof
