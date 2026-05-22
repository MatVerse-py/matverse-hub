# MatVerse Benchmark Core Release Plan

## Status

```text
DOCUMENT_STATUS        = RELEASE_PLAN
TARGET_ARTIFACT        = MatVerse Benchmark Core
TARGET_VERSION         = v0.1.1-alpha
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
REFERENCE_DOI          = 10.5281/zenodo.20343556
CURRENT_STATE          = PASS_LOCAL_TESTED / STAGE_TO_PASS
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

MatVerse Benchmark Core is the next recommended public artifact after MatVerse Hub. Its role is to provide a clean, local-tested benchmark and work-evidence core for the MatVerse Scientific Platform.

This plan does not approve raw ZIP publication. It defines the path from clean local bundle to GitHub release, Zenodo DOI and community inclusion.

## Current evidence

```text
Raw source uploads:
benck(1).zip
benck(2).zip

Raw SHA256:
9a921a42e79b4ea9bfa9078a3e1a64ab63a120216f41e000bfc0f84eee4f2406

Raw state:
BLOCK_RAW

Clean bundle:
matverse_benchmark_core_v0_1_1_alpha_clean.zip

Clean bundle SHA256:
a7f01e70685a5e9de2bfee2a0d845c0f12125cf4ed91388d45e2df8593ec8c52

Local validation:
Syntax check = PASS
pytest test_causal_engine.py = 6 passed
```

## Why this artifact first

Benchmark Core is the best next release candidate because it has:

```text
cleaned source package
raw bundle excluded
cache and bytecode removed
nested ZIP removed
local syntax validation
local tests passing
clear relationship to work-evidence generation
lower publication risk than MCP/server bundles
```

## Publication boundary

Raw ZIPs remain blocked.

```text
benck(1).zip = BLOCK_RAW
benck(2).zip = BLOCK_RAW
```

Only the clean bundle can advance after final review.

```text
matverse_benchmark_core_v0_1_1_alpha_clean.zip = STAGE_TO_PASS
```

## Required metadata before release

The release package must include:

```text
README.md
CITATION.cff
codemeta.json
MANIFEST.json
HASHES.sha256
RELEASE_NOTES_v0.1.1-alpha.md
CLAIM_HYGIENE.md or equivalent section
TEST_REPORT.md or equivalent test summary
```

## Acceptance gates

```text
G1_SAFE_STRUCTURE        = PASS
G2_SECRET_SCAN           = PASS
G3_RAW_FILES_REMOVED     = PASS
G4_HASH_MANIFEST         = PASS
G5_TESTS_LOCAL           = PASS
G6_CITATION_METADATA     = PASS
G7_CLAIM_HYGIENE         = PASS
G8_RELEASE_NOTES         = PASS
G9_HUMAN_AUTHORSHIP      = PASS
G10_NON_PRODUCTION_LABEL = PASS
```

No artifact should advance if any gate returns BLOCK.

## Suggested GitHub release fields

```text
Tag:
v0.1.1-alpha

Title:
MatVerse Benchmark Core v0.1.1-alpha — Work Evidence Benchmark Layer

Pre-release:
ON

Body:
RELEASE_NOTES_v0.1.1-alpha.md

Asset:
matverse_benchmark_core_v0_1_1_alpha_clean.zip
```

## Suggested Zenodo metadata

```text
Title:
MatVerse Benchmark Core

Version:
v0.1.1-alpha

Resource type:
Software

Creators:
Mateus Arêas
ORCID: https://orcid.org/0009-0008-2973-4047

Description:
MatVerse Benchmark Core is an alpha-stage local-tested benchmark and work-evidence layer for the MatVerse Scientific Platform. It supports the transformation of benchmark execution into structured evidence suitable for later ledger, replay, receipt and DOI workflows.

Keywords:
MatVerse, IQG, benchmark core, work evidence, artifact engineering, evidence governance, Omega Gate, scientific software
```

## Community target

```text
Community:
MatVerse Research Infrastructure

Seed dependency:
MatVerse Hub v0.1.1-alpha
DOI: 10.5281/zenodo.20343556
```

## Work-proof classification

```text
Domain:
Scientific / Platform Benchmarking

Proof family:
PoSW-MV + PoNW-MV support

Work unit:
benchmark execution, causal engine test, local validation report

Evidence output:
test report, hash manifest, clean source bundle, release metadata

Public record:
GitHub release + Zenodo DOI after final review
```

## Safe public claim

MatVerse Benchmark Core v0.1.1-alpha is an alpha-stage local-tested benchmark and work-evidence component for the MatVerse Scientific Platform.

## Blocked claims

```text
production-ready benchmark system
externally validated benchmark
proof of digital life
financial proof
quantum hardware validation
raw ZIP ready for DOI
agent or model authorship
```

## Release sequence

```text
1. Review clean bundle contents.
2. Confirm metadata files are present and aligned.
3. Confirm HASHES.sha256 matches final package.
4. Confirm local tests and syntax report.
5. Create GitHub release as pre-release.
6. Let Zenodo archive the release.
7. Capture DOI.
8. Add DOI badge and identifiers after DOI generation.
9. Associate record with MatVerse Research Infrastructure community.
10. Keep production and external validation claims on HOLD.
```

## Final decision

```text
BENCHMARK_CORE_NEXT_RELEASE = RECOMMENDED
RAW_ZIP_PUBLICATION         = BLOCK
CLEAN_BUNDLE_STATUS         = STAGE_TO_PASS
NEXT_ACTION                 = final review then GitHub pre-release
```
