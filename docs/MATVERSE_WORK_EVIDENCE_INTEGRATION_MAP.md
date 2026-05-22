# MatVerse Work Evidence Integration Map

## Status

```text
DOCUMENT_STATUS        = STAGE_INTEGRATION_MAP
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
REFERENCE_DOI          = 10.5281/zenodo.20343556
PLATFORM_LAYER         = MatVerse Scientific Platform
WORK_EVIDENCE_LAYER    = STAGE_TO_PASS
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

This document integrates the current platform artifacts and work-evidence candidates into the MatVerse scientific platform roadmap.

The goal is to separate:

```text
public platform anchor
clean source candidates
local work-evidence candidates
experimental quantum plans
raw bundles blocked from publication
```

No raw ZIP package is approved for direct public publication.

## Observed source materials

```text
Texto colado.txt
= GitHub to Zenodo release flow, DOI preservation logic, claim hygiene for archived scientific software.

packinfra.zip
= MatVerse Connector Intelligence Layer prototype, with Connector Registry, access broker, audit ledger, claim gate and Card-API console.

benck(1).zip / benck(2).zip
= byte-identical MatVerse benchmark/proof-of-work core package, raw uploads blocked until cleaned.

vqd_fmo_hardware_benchmark_plan.md
= VQD-FMO quantum hardware benchmark plan with VQE-CVaR, error mitigation, multi-backend scheduler and Rust compiler module.
```

## Platform interpretation

```text
MatVerse Hub v0.1.1-alpha
  ↓
MatVerse Research Infrastructure community
  ↓
Connector Intelligence Layer
  ↓
Benchmark / Work Evidence Core
  ↓
VQD-FMO Experimental Benchmark Plan
  ↓
Evidence packs / DOI records / later external validation
```

## Artifact classification

| Artifact | State | Function | Publication action |
|---|---|---|---|
| MatVerse Hub v0.1.1-alpha | PASS | Public alpha anchor with DOI | Community seed |
| packinfra.zip | HOLD_RAW | Connector Intelligence Layer raw prototype | Do not publish raw |
| MatVerse Connector Intelligence Layer clean bundle | STAGE_TO_PASS | Governed connector registry, broker, ledger and claim-gate console | Review, build check, release later |
| benck(1).zip | BLOCK_RAW | Raw benchmark core upload | Do not publish raw |
| benck(2).zip | BLOCK_RAW | Duplicate raw benchmark core upload | Deduplicate, do not publish raw |
| MatVerse Benchmark Core clean bundle | PASS_LOCAL_TESTED / STAGE_TO_PASS | Local benchmark and work-evidence core | Candidate for next clean release |
| vqd_fmo_hardware_benchmark_plan.md | STAGE_EXPERIMENTAL | Quantum hardware benchmark plan | Keep as paper/experiment plan until real backend execution |
```

## Work evidence pipeline

The local work-evidence track should be interpreted as:

```text
task / event / benchmark
  ↓
MNB representation
  ↓
Omega Gate decision
  ↓
ledger entry
  ↓
receipt
  ↓
replay check
  ↓
evidence pack
  ↓
release / DOI after sanitation
```

## Clean bundle gates

A package can advance from STAGE_TO_PASS to PASS_PUBLICATION_READY only after:

```text
source inventory complete
raw working files removed
user_input_files removed
nested ZIPs removed or justified
cache and bytecode removed
README present
CITATION.cff present
codemeta.json present
MANIFEST.json present
HASHES.sha256 present
release notes present
syntax/build/test report present
claim hygiene present
human authorship only
non-production status explicit
external validation status explicit
```

## VQD-FMO experimental track

The VQD-FMO plan remains experimental until hardware execution exists.

Required future evidence:

```text
backend name
job id or equivalent public reference when safe
shots
circuit depth
error mitigation configuration
raw counts hash
mitigated observable hash
CVaR report
Psi_FMO report
Omega backend score
replay notebook or script
MANIFEST.json
HASHES.sha256
```

Allowed claim:

```text
VQD-FMO is a hardware benchmark plan for testing VQE-CVaR, error mitigation and backend scheduling for FMO-inspired quantum experiments.
```

Blocked claim:

```text
VQD-FMO has been validated on real quantum hardware.
```

## Claim hygiene

Allowed:

```text
MatVerse Hub v0.1.1-alpha is archived on Zenodo with DOI 10.5281/zenodo.20343556.
Clean bundles can become platform artifacts after sanitation and metadata alignment.
Benchmark Core is locally tested after cleanup.
VQD-FMO is an experimental benchmark plan.
```

Blocked:

```text
production-ready
externally validated
proof of digital life
raw bundle ready for DOI
all connectors verified
quantum hardware validated without real execution evidence
agent authorship
```

## Next actions

```text
1. Create Zenodo community: MatVerse Research Infrastructure.
2. Add MatVerse Hub v0.1.1-alpha as seed record.
3. Review Connector Intelligence Layer clean bundle.
4. Review Benchmark Core clean bundle.
5. Select one clean bundle as next release candidate.
6. Keep raw ZIPs blocked.
7. Keep VQD-FMO as experimental plan until real backend evidence exists.
```
