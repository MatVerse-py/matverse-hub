# MatVerse Research Infrastructure — Zenodo Community Prototype

## Status

```text
COMMUNITY_STATUS      = READY_TO_CREATE_ON_ZENODO_UI
PLATFORM_ROLE         = PROTOTYPE_PUBLIC_ARCHIVE_LAYER
PRODUCTION_READINESS  = HOLD
PUBLIC_VALIDATION     = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP      = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

The Zenodo community is the public archival layer for MatVerse research infrastructure. It groups software releases, protocols, scientific infrastructure packages, curation reports, evidence packs, and platform prototypes under one governed record space.

The community is not a production claim. It is a curated public archive for alpha-stage scientific and technical artifacts related to MatVerse, IQG, Omega Gate, evidence governance, artifact engineering, proof-of-execution workflows, and portable scientific infrastructure.

## Recommended Zenodo community fields

```text
Community name:
MatVerse Research Infrastructure

Identifier suggestion:
matverse-research-infrastructure

Short description:
Public archive for MatVerse / IQG alpha-stage scientific software, evidence governance protocols, artifact engineering, and portable research infrastructure.

Owner / creator:
Mateus Arêas
ORCID: https://orcid.org/0009-0008-2973-4047
```

## About page draft

MatVerse Research Infrastructure is a curated Zenodo community for alpha-stage scientific software, protocols, evidence packs, and research infrastructure artifacts related to the MatVerse / IQG ecosystem.

The community organizes public artifacts around verifiable scientific computing, artifact engineering, causal provenance, DOI-based preservation, evidence governance, Omega Gate admissibility, proof-of-execution workflows, and portable scientific infrastructure.

Records in this community may include software releases, protocols, benchmark packages, reproducibility materials, documentation bundles, governance reports, and curated platform prototypes. Inclusion in this community means the artifact is relevant to the MatVerse research infrastructure and has passed minimal archival hygiene checks. It does not imply production readiness, external validation, institutional certification, or proof of digital life.

## Curation policy draft

Submissions may be accepted when they satisfy all applicable criteria:

1. The artifact has clear human authorship.
2. The artifact has no exposed sensitive operational material.
3. The artifact has explicit scope and version.
4. The artifact has sufficient metadata for citation and reuse.
5. The artifact is relevant to MatVerse, IQG, artifact engineering, evidence governance, Omega Gate, Proof of Execution, portable scientific infrastructure, or related scientific software.
6. Alpha-stage artifacts are clearly marked as alpha, non-production, or experimental.
7. Strong claims require independent public evidence.

Submissions should be held when they include raw working exports, personal working directories, duplicate nested packages, unresolved placeholders, or unverifiable claims.

## Initial collection plan

```text
1. MatVerse Hub v0.1.1-alpha
   DOI: 10.5281/zenodo.20343556
   Status: PUBLISHED / COMMUNITY_SEED

2. portable-scientific-infrastructure.zip
   Status: PASS_CANDIDATE
   Action: extract, sanitize, manifest, release as portable infrastructure prototype

3. POep.zip
   Status: HOLD_PUBLIC / PASS_INTERNAL
   Action: extract publish_package only and release clean Proof of Execution Protocol package

4. POep2.zip
   Status: STAGE_GOVERNANCE
   Action: use as governance cleanup evidence, not first-class software release

5. Matverse.zip
   Status: HOLD / INTERNAL_ONLY
   Action: mine for curated artifacts, do not publish raw corpus

6. doi.zip
   Status: BLOCK_PUBLICATION
   Action: keep internal only; do not publish
```

## Acceptance states

```text
PASS       = ready for community submission
STAGE      = useful but requires metadata or cleanup
HOLD       = internal or incomplete; not public yet
BLOCK      = not publishable in current form
```

## Prototype platform interpretation

This community acts as the first public prototype of the MatVerse platform archive. It is not merely a folder of files. It is a governed publication surface where each artifact must pass minimal checks for authorship, citation, scope, versioning, provenance, claim hygiene, and safety before joining the public record.

The intended platform chain is:

```text
GitHub release → Zenodo DOI → Community curation → Citation metadata → Public archive → Later validation/replay/evidence packs
```

## Safe public claim

MatVerse Research Infrastructure is a curated Zenodo community prototype for alpha-stage MatVerse / IQG scientific software, artifact engineering, evidence governance, Proof of Execution materials, and portable research infrastructure.

## Blocked public claims

```text
production-ready platform
externally validated scientific infrastructure
institutionally certified system
proof of digital life
complete proof of MatVerse as final science
```
