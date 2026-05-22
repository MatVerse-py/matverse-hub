# MatVerse Platform Server Integration Map

## Status

```text
DOCUMENT_STATUS        = STAGE_INTEGRATION_MAP
PLATFORM_PROTOTYPE     = ACTIVE
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
ZENODO_DOI             = 10.5281/zenodo.20343556
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

This document integrates the current server-side artifacts into the MatVerse scientific platform roadmap. It does not publish raw ZIP files. It classifies each artifact by role, publication readiness, and integration path.

The goal is to evolve MatVerse from a DOI-archived alpha software release into a curated platform prototype composed of:

```text
Zenodo Community → MatVerse Hub → IQG Server → MCP Interface → Skill Governance → Evidence/Replay Packages
```

## Existing public anchor

```text
MatVerse Hub v0.1.1-alpha
DOI: 10.5281/zenodo.20343556
Role: first public archived alpha software release
Status: COMMUNITY_SEED
```

## New uploaded server artifacts reviewed

```text
Markdown.md colado                         = release process log / governance memory
serv2.zip                                  = combined MCP + IQG integration package with raw bundled inputs
matverse-mcp-server-main.zip               = TypeScript/React/tRPC MCP interface candidate
DEv-main.zip                               = MatVerse Skill Governance Layer candidate
matverse_iqg_server_v0_1_0.zip             = FastAPI local-first IQG backend candidate
matverse_server_pack_v0_1_0.zip            = dependency-light Node governance server reference
matverse-hub-main.zip                      = historical MatVerse Hub source package
```

## Technical reading

### 1. MatVerse IQG Server

```text
Artifact: matverse_iqg_server_v0_1_0.zip
Role: local-first causal backend / API v1
Language: Python / FastAPI
Core path: event → MNB → Omega Gate → ledger → receipt → replay → evidence pack
Syntax check: PASS_REPORTED
Publication status: PASS_CANDIDATE_AFTER_SANITIZATION
```

Recommended integration:

```text
Create repository: matverse-iqg-server
Release candidate: v0.1.0-alpha
Archive target: Zenodo community after hygiene pass
Do not expose runtime configuration values
Keep .env.example as template only
```

### 2. MatVerse MCP Server

```text
Artifact: matverse-mcp-server-main.zip
Role: MCP / UI / tRPC surface for ledger and MNB operations
Language: TypeScript / React / tRPC
Publication status: HOLD_PUBLIC
Reason: requires dependency audit, UI build check, and removal of nonessential generated/runtime materials
```

Recommended integration:

```text
Create repository: matverse-mcp-server
Connect to IQG Server through adapter layer
Do not publish as DOI until dependency and build checks pass
```

### 3. MatVerse Skill Governance Layer

```text
Artifact: DEv-main.zip
Role: governance layer for skills, connectors, consent, Omega Gate, ledger and replay
Language: Python
Syntax check: PASS_REPORTED
Publication status: PASS_CANDIDATE_AFTER_SANITIZATION
```

Recommended integration:

```text
Create repository: matverse-skill-governance
Use as policy/gate layer before MCP or IQG execution
Archive as alpha software after README, CITATION, MANIFEST and HASHES are aligned
```

### 4. MatVerse Server Pack

```text
Artifact: matverse_server_pack_v0_1_0.zip
Role: minimal Node HTTP governance server reference
Language: Node.js / native HTTP
Publication status: STAGE
Reason: useful as reference implementation, but public deploy remains blocked
```

Recommended integration:

```text
Keep as reference implementation
Extract architecture docs and tests
Avoid presenting as production SaaS
```

### 5. Combined Integration Bundle

```text
Artifact: serv2.zip
Role: combined MCP + IQG integration bundle
Publication status: BLOCK_RAW / STAGE_AS_SOURCE
Reason: contains nested ZIPs and raw input bundles
```

Recommended integration:

```text
Do not publish raw
Use only to reconstruct clean integration plan
Extract separate clean repos/packages from its components
```

### 6. Historical Hub Package

```text
Artifact: matverse-hub-main.zip
Role: historical source package for MatVerse Hub
Publication status: SUPERSEDED_BY_ZENODO_RELEASE
Current DOI: 10.5281/zenodo.20343556
```

## Platform architecture after integration

```text
[Community Layer]
Zenodo Community: MatVerse Research Infrastructure
  ↓
[Archive Layer]
Zenodo DOI records / GitHub Releases / CITATION / MANIFEST / HASHES
  ↓
[Hub Layer]
MatVerse Hub: public governance and witness layer
  ↓
[Backend Layer]
MatVerse IQG Server: MNB, Omega Gate, ledger, receipt, replay, evidence pack
  ↓
[Interface Layer]
MatVerse MCP Server: user/app/tRPC interface for governed operations
  ↓
[Governance Layer]
Skill Governance: connector policy, consent, risk, receipts, replay
  ↓
[Reference Layer]
Server Pack: local Node reference for governance server patterns
```

## Integration order

```text
1. Create Zenodo community: MatVerse Research Infrastructure
2. Add MatVerse Hub v0.1.1-alpha as community seed
3. Sanitize and publish portable scientific infrastructure package
4. Sanitize and publish MatVerse IQG Server v0.1.0-alpha
5. Sanitize and publish MatVerse Skill Governance Layer v0.1.0-alpha
6. Stage MCP Server after dependency/build review
7. Stage Node Server Pack as reference implementation only
8. Keep combined bundles and raw corpora internal
```

## Safety and authorship policy

```text
Do not expose secrets, runtime values, credentials, tokens, private configuration, or raw operational dumps.
Do not publish raw user_input_files or bundled working directories.
Do not list agents, tools, bots, or models as authors.
Use human authorship only: Mateus Arêas / ORCID 0009-0008-2973-4047.
Keep alpha artifacts marked as non-production.
Keep external validation claims on HOLD until independent evidence exists.
```

## Publication states

```text
PASS_CANDIDATE_AFTER_SANITIZATION = can become public release after cleanup and metadata alignment
STAGE                             = useful but not ready as DOI package
HOLD_PUBLIC                       = internal until build/security/provenance checks pass
BLOCK_RAW                         = raw ZIP must not be published
SUPERSEDED                         = preserved by newer DOI/release
```

## Immediate next action

The next public artifact should not be a raw server bundle. The next public artifact should be a cleaned, minimal package from one of these tracks:

```text
Priority 1: portable scientific infrastructure
Priority 2: MatVerse IQG Server
Priority 3: MatVerse Skill Governance Layer
Priority 4: Proof of Execution clean package
```

The combined server integration should be represented by documentation and clean repos, not by uploading raw ZIP bundles.
