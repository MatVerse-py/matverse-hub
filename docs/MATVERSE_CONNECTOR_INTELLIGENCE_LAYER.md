# MatVerse Connector Intelligence Layer

## Status

```text
DOCUMENT_STATUS        = STAGE_INTEGRATION_NOTE
ARTIFACT_STATUS        = STAGE_TO_PASS
SOURCE_UPLOAD          = packinfra.zip
CLEAN_BUNDLE           = matverse_connector_intelligence_layer_v0_1_0_alpha_clean.zip
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
ZENODO_DOI             = 10.5281/zenodo.20343556
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

The MatVerse Connector Intelligence Layer is a prototype for governed connector management in the MatVerse platform. It models connector registration, reference-based connector identity, ephemeral action grants, append-only audit entries, claim gating, and a Card-API console.

This document records the integration state only. It does not approve raw package publication.

## Components

```text
Connector Registry      = connector identity, type, scopes, status, risk and reference metadata
UUID Access Broker      = short-lived action authorization
Audit Ledger            = event, action, status, hash and receipt trail
Claim Gate              = blocks strong claims without evidence
Card-API Console        = visual console for connector status, grants, ledger and claims
```

## Connector states

```text
VERIFIED      = tested with evidence
DECLARED      = registered but not tested
FAILED        = tested and failed
UNAVAILABLE   = no tool or permission available for verification
```

## Sanitization decision

```text
raw packinfra.zip       = HOLD_RAW
clean source bundle     = STAGE_TO_PASS
user_input_files        = REMOVED_FROM_CLEAN_BUNDLE
generated dist output   = REMOVED_FROM_CLEAN_BUNDLE
agent authorship        = NOT_INCLUDED
production claim        = BLOCKED
external validation     = HOLD_EXTERNAL_REQUIRED
```

## Publication path

```text
1. Keep raw packinfra.zip internal.
2. Use the cleaned source bundle for review.
3. Run dependency and build checks.
4. Confirm no raw operational material is included.
5. Add README, CITATION, codemeta, MANIFEST, HASHES and release notes.
6. Publish only after PASS review.
7. Associate future DOI with MatVerse Research Infrastructure community.
```

## Relationship to current platform map

```text
Zenodo Community
  ↓
MatVerse Hub v0.1.1-alpha
  ↓
MatVerse Connector Intelligence Layer
  ↓
Connector Registry / Broker / Ledger / Claim Gate
  ↓
Future Supabase-backed persistence and audit integration
```

## Safe claim

MatVerse Connector Intelligence Layer is an alpha prototype for governed connector registry, ephemeral grants, audit ledger, and claim-gating interfaces within the MatVerse platform.

## Blocked claims

```text
production-ready
externally validated
all connectors verified
complete security proof
proof of digital life
raw bundle ready for DOI
```
