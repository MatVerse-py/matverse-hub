# MatVerse URANO Launch Roadmap

## Status

```text
DOCUMENT_STATUS        = ROADMAP_GOVERNANCE_PLAN
SOURCE_BUNDLE          = Skill Creator Instructions.zip
SOURCE_REPORT          = Análise do Roadmap de Lançamento do MatVerse
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
REFERENCE_DOI          = 10.5281/zenodo.20343556
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
RAW_ARCHIVE_PUBLICATION = BLOCK
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

This document records the governed launch roadmap for MatVerse / URANO. It converts the roadmap report into a release discipline document.

The roadmap is not a production claim. It is a staged plan with risk gates, evidence requirements and explicit publication boundaries.

## Raw bundle policy

The uploaded bundle contains a nested `Archive.zip` and multiple planning/skill files. The nested archive remains blocked for raw public release.

```text
Archive.zip = BLOCK_RAW
Reason      = nested archive, raw working material, unstandardized metadata and elevated publication risk
Issue       = audit: Archive.zip blocked by Omega-Gate raw publication policy
```

No raw ZIP should be uploaded to GitHub Releases, Zenodo or public distribution.

## Launch phases

### Phase 1 — Alpha / Beta: URANO Cloud early adopters

Goal:

```text
Validate URANO Cloud with a restricted early-adopter group.
Focus: Omega-Gate behavior, GitHub/Zenodo integration, dashboard usability and evidence-pack flow.
```

Primary risks:

```text
Omega-Gate false positives / false negatives
third-party API instability
user learning curve for Psi, Theta, CVaR and PoLE
secret exposure through immature connector flows
```

Required gates:

```text
G1_SECRETREF_ONLY        = PASS
G2_SIMULATION_MODE       = PASS
G3_FEEDBACK_LOOP         = PASS
G4_CONNECTOR_ABSTRACTION = PASS
G5_CLAIM_HYGIENE_UI      = PASS
```

Exit criteria:

```text
early-adopter feedback captured
Omega decision logs exportable
no secret values exposed in frontend or docs
GitHub/Zenodo connector flows operate through safe references
evidence packs generated in draft mode
```

### Phase 2 — General Availability: URANO Cloud

Goal:

```text
Open URANO Cloud with expanded connectors, dashboards and evidence workflows.
```

Primary risks:

```text
ledger scalability
multi-tenant isolation
support burden
connector drift
public overclaiming
```

Required gates:

```text
G1_TENANT_ISOLATION      = PASS
G2_LEDGER_SCALING_PLAN   = PASS
G3_AUDIT_LOG_EXPORT      = PASS
G4_RATE_LIMITING         = PASS
G5_STATUS_PAGE           = PASS
G6_PUBLIC_CLAIM_POLICY   = PASS
```

Exit criteria:

```text
tenant boundaries tested
auditable ledger export available
connector failure modes documented
dashboard can explain PASS / HOLD / BLOCK without hidden claims
support runbook published
```

### Phase 3 — URANO Sovereign: on-premise / hybrid

Goal:

```text
Offer URANO as local-first / hybrid infrastructure for regulated environments.
```

Primary risks:

```text
security certification burden
customer-specific deployment complexity
private-key / API-key handling
compliance requirements
integration with internal systems
```

Required gates:

```text
G1_LOCAL_FIRST_RUNTIME      = PASS
G2_SECRET_VAULT_INTEGRATION = PASS
G3_OFFLINE_REPLAY           = PASS
G4_AUDIT_BUNDLE_EXPORT      = PASS
G5_ADMIN_POLICY_MODEL       = PASS
G6_DEPLOYMENT_HARDENING     = PASS
```

Exit criteria:

```text
on-premise installation reproducible
secrets never enter public UI
replay works offline
administrator policy is explicit
security model documented
customer deployment checklist available
```

### Phase 4 — OP Store expansion

Goal:

```text
Create a marketplace / registry of Proof Organisms (OPs) and tools for domain-specific OP creation.
```

Primary risks:

```text
unvetted OPs
unsafe domain claims
quality control
supply-chain risk
confusion between app and proof organism
```

Required gates:

```text
G1_OP_SCHEMA             = PASS
G2_OP_SIGNING            = PASS
G3_OP_RISK_CLASS         = PASS
G4_OP_REPLAY_TEST        = PASS
G5_OP_CLAIM_BOUNDARY     = PASS
G6_OP_REVIEW_WORKFLOW    = PASS
```

Exit criteria:

```text
OP package schema defined
OP review workflow active
OPs labeled by domain and risk
unsafe OPs blocked from public registry
replay/test evidence attached to each OP candidate
```

## Product architecture alignment

```text
URANO Cloud
  = managed SaaS surface for early users and public dashboards

URANO Sovereign
  = local-first / hybrid version for regulated or private environments

OP Store
  = registry of domain-specific Proof Organisms

MatVerse Hub
  = public governance and witness layer

Zenodo Community
  = public archive / DOI curation surface
```

## Skill Creator integration

The uploaded bundle includes a `matverse.skill` file and skill-creation guidance materials. These are useful as source material, but not as a public release bundle.

Recommended use:

```text
1. Extract skill instructions into a clean skill spec.
2. Remove raw transcripts and nested archives.
3. Add SKILL.md, README.md, MANIFEST.json, HASHES.sha256 and claim hygiene.
4. Publish only the clean derived skill package after review.
```

Candidate skill name:

```text
matverse-urano-launch-governance-skill
```

Skill purpose:

```text
Evaluate, stage and audit URANO launch artifacts across Cloud, Sovereign and OP Store phases using Omega-Gate, claim hygiene, SecretRef policy and evidence-pack requirements.
```

## Roadmap risk matrix

| Phase | Risk | Severity | Decision |
|---|---|---:|---|
| Alpha/Beta | Omega-Gate false decisions | High | STAGE with feedback loop |
| Alpha/Beta | Third-party API drift | Medium | STAGE with connector gateway |
| Alpha/Beta | Learning curve | Medium | STAGE with guided UX |
| GA Cloud | Ledger scaling | High | HOLD until scale plan |
| GA Cloud | Multi-tenant isolation | Critical | BLOCK until tested |
| Sovereign | Secret/key handling | Critical | SecretRef-only |
| Sovereign | Compliance/certification | High | HOLD until audit pack |
| OP Store | Unsafe OP packages | Critical | BLOCK without OP review gate |
| OP Store | Claim inflation | High | Claim hygiene required |

## Evidence requirements

Before any release phase moves to PASS_PUBLIC, the following must exist:

```text
README.md
CITATION.cff when scientific artifact
codemeta.json when software artifact
MANIFEST.json
HASHES.sha256
RELEASE_NOTES.md
CLAIM_HYGIENE.md
TEST_REPORT.md or validation report
SECRET_SCAN summary
REPLAY_REPORT when applicable
EVIDENCE_PACK when applicable
human authorship metadata only
```

## Safe public statement

MatVerse / URANO is a staged scientific-software platform roadmap for governed research workflows, evidence packs, Omega-Gate decisions, connector integration and future Proof Organism applications.

## Blocked public statements

```text
production-ready
externally validated
institutionally closed
safe for regulated deployment without certification
automatic publication system
raw Archive.zip ready for release
proof of digital life
financial return guarantee
```

## Final decision

```text
URANO_LAUNCH_ROADMAP     = STAGE_GOVERNED
ARCHIVE_ZIP_RAW          = BLOCK
SKILL_CREATOR_MATERIAL   = STAGE_SOURCE_MATERIAL
URANO_CLOUD              = ALPHA_BETA_PLAN
URANO_SOVEREIGN          = HOLD_SECURITY_CERTIFICATION
OP_STORE                 = STAGE_SCHEMA_REQUIRED
NEXT_ACTION              = create clean launch-governance skill spec
```
