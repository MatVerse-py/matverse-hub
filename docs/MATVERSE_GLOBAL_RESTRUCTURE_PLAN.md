# MatVerse Global Restructure Plan

## Status

```text
DOCUMENT_STATUS        = GLOBAL_RESTRUCTURE_PLAN
TARGET_SCOPE           = MatVerse / IQG / URANO / TACE / GOV / QeX / Shield / ProofPack / OP Store
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
REFERENCE_DOI          = 10.5281/zenodo.20343556
RAW_ZIP_PUBLICATION    = BLOCK
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Core principle

The MatVerse ecosystem must be reorganized by function, evidence level and publication readiness.

The new structure must separate:

```text
science from product
runtime from interface
research from B2G deployment
raw source bundles from clean public releases
local evidence from public validation
identity/authorship from agent/tool execution
```

No raw ZIP bundle should be treated as a release artifact.

## Canonical top-level model

```text
MatVerse
= constitution / scientific field / causal governance layer

IQG
= governable intelligence organism operating inside MatVerse

URANO
= scientific operating workbench / notebook OS

ACOA / Governance
= admissibility, audit, policy and release gates

Symbios / SymbioIQG
= operational interface and experience layer

MNB
= causal unit / gene of governable knowledge

Omega Gate
= selection and admissibility operator

Ledger / Replay
= inheritance and continuity proof

Evidence Pack / ProofPack
= exportable proof product
```

## New repository topology

The ecosystem should move from a many-bundle structure to a clear multi-repository architecture.

```text
matverse-hub/
  Public governance hub, DOI seed, platform docs and release registry.

matverse-urano/
  URANO Notebook OS, OSX, Browser, WebX, OP apps, MNB Calculator and workbench UI.

matverse-benchmark-core/
  Benchmark Core, local work-evidence engine and Monte Carlo / OP Risk Simulator.

matverse-proofpack/
  Public product for turning AI outputs into evidence packs.

matverse-tace/
  TACE research-engineering track: entropy, cost, coherence, CVaR, AI output control.

gov-assist-orchestrator/
  GOV B2G product track: workflows, identity bridge, RCPN demo, ledger and human review.

matverse-shield/
  SecretRef, security scanning, redaction, RedeVault, provenance and defensive evidence.

matverse-qex/
  Quantum / hybrid classical-quantum experiments, VQD-FMO, Q-Receipts, Q-Replay, Q-DOI.

matverse-connector-intelligence/
  Connector Registry, UUID Access Broker, Grant Manager, Audit Ledger and Claim Gate.

matverse-research-nodes/
  Genesis Node, ArXiv Pipeline Manager, MxV Symbios and research-node prototypes.

matverse-op-store/
  OP schema, OP registry, OP review workflow, OP signing and domain OP packages.

shared-governance-kernel/
  Optional shared primitives only: receipt, ledger, hash, replay, policy schema, PASS/HOLD/BLOCK.
```

## Monorepo internal folder pattern

Each repository should use the same clean pattern when applicable.

```text
repo/
├── README.md
├── CITATION.cff
├── codemeta.json
├── MANIFEST.json
├── HASHES.sha256
├── RELEASE_NOTES.md
├── CLAIM_HYGIENE.md
├── SECURITY.md
├── docs/
├── src/
├── tests/
├── examples/
├── scripts/
├── evidence/
│   ├── TEST_REPORT.md
│   ├── REPLAY_REPORT.json
│   ├── LEDGER_SAMPLE.jsonl
│   └── EVIDENCE_PACK_MANIFEST.json
└── .github/
    └── workflows/
```

No repository should include:

```text
raw user_input_files
nested raw archives
private keys
tokens
.env with real values
cache directories
bytecode
build outputs as source of truth
unreviewed transcripts
```

## Functional architecture

```text
MatVerse Scientific Platform
├── 00_identity_authorship
│   ├── ORCID
│   ├── CITATION.cff
│   ├── codemeta.json
│   └── human authorship registry
│
├── 01_scientific_work
│   ├── Research Trail
│   ├── Paper Vivo
│   ├── Benchmark Core
│   ├── Evidence Pack
│   └── QeX experimental reports
│
├── 02_governance
│   ├── ACOA
│   ├── Omega Gate
│   ├── Claim Hygiene
│   ├── Release Gate
│   ├── Auditor Skill
│   └── Body-D / Body-A / Body-X
│
├── 03_runtime
│   ├── IQG runtime
│   ├── MNB engine
│   ├── Ledger
│   ├── Replay
│   ├── FastAPI / local runtime
│   └── backend bridge
│
├── 04_urano_workbench
│   ├── URANO OS
│   ├── URANO OSX
│   ├── URANO Browser
│   ├── WebX
│   ├── MCP Gateway
│   ├── OP Store
│   ├── MNB Calculator
│   ├── MatMax Wallet
│   └── IQG Chat
│
├── 05_security_shield
│   ├── SecretRef
│   ├── RedeVault
│   ├── redaction
│   ├── secret scan
│   ├── provenance scan
│   └── incident receipts
│
├── 06_economic_omega_capitals
│   ├── research assets
│   ├── funding trails
│   ├── budget lineage
│   ├── impact reports
│   └── risk boundary
│
├── 07_tace
│   ├── TACE Core
│   ├── TACE Bench
│   ├── TACE Agent
│   └── TACE Dashboard
│
├── 08_gov
│   ├── GOV Core
│   ├── GOV RCPN Assist
│   ├── GOV Ledger
│   ├── GOV Identity Bridge
│   ├── GOV Review
│   └── GOV Portal
│
├── 09_quantum_qex
│   ├── QIR bridge
│   ├── VQD-FMO
│   ├── Q-Receipt
│   ├── Q-Replay
│   └── Q-DOI evidence pack
│
├── 10_public_archive
│   ├── GitHub releases
│   ├── Zenodo DOI
│   ├── Zenodo community
│   ├── Hugging Face
│   ├── Software Heritage
│   └── blockchain witness
│
└── 11_products
    ├── ProofPack
    ├── URANO Cloud
    ├── URANO Sovereign
    ├── GOV Assist
    └── OP Store
```

## Artifact states

```text
PASS
  Public-ready under declared scope.

PASS_LOCAL
  Locally tested or reported; not necessarily public/external.

STAGE
  Useful, structured, needs cleanup, tests or metadata.

HOLD
  Incomplete, internal, awaiting evidence or decision.

BLOCK
  Not publishable or unsafe in current form.

QUARANTINE
  Sensitive, secret-risk, claim-risk or contaminated material.

SUPERSEDED
  Historical artifact replaced by a newer DOI/release.
```

## Current artifact routing

```text
MatVerse Hub v0.1.1-alpha
  → matverse-hub
  → PASS / DOI_SEED

Benchmark Core clean
  → matverse-benchmark-core
  → NEXT_RELEASE_CANDIDATE

Genesis Node clean
  → matverse-research-nodes
  → STAGE_TO_PASS

Connector Intelligence Layer clean
  → matverse-connector-intelligence
  → STAGE_TO_PASS

ArXiv / MxV Symbios clean
  → matverse-research-nodes
  → STAGE_TO_PASS

URANO Notebook / NOTE.zip
  → matverse-urano
  → RAW BLOCK / CLEAN DERIVATIVE REQUIRED

TACE
  → matverse-tace
  → STAGE_RESEARCH_ENGINE

GOV
  → gov-assist-orchestrator
  → STAGE_B2G_PRODUCT

Shield / SecretRef / RedeVault
  → matverse-shield
  → REQUIRED_SECURITY_LAYER

QeX / VQD-FMO
  → matverse-qex
  → STAGE_EXPERIMENTAL

Archive.zip
  → BLOCK_RAW
  → issue #18 remediation path
```

## Release order

Recommended release sequence:

```text
1. MatVerse Hub v0.1.1-alpha        = DONE / DOI seed
2. Benchmark Core v0.1.1-alpha      = NEXT
3. Genesis Node v0.1.0-alpha        = after build review
4. Connector Intelligence Layer      = after build/dependency review
5. ArXiv / MxV Symbios Pipeline      = after research-scope cleanup
6. URANO Notebook clean              = after package split and tests
7. TACE Core v0.1                    = after benchmark report
8. GOV.RCPN Assist v0.1              = after legal/compliance boundary
9. QeX / VQD-FMO                     = only after reproducible experiment evidence
10. OP Store                         = only after OP schema and signing policy
```

## TACE / GOV separation

TACE and GOV must not be mixed.

```text
TACE = research-engineering control layer.
GOV  = B2G auditable product layer.
```

GOV may use TACE internally as a discreet `Risk and Coherence Engine`, but GOV must not use thermodynamic or quantum-heavy language in public-sector positioning.

## URANO structure

```text
URANO Notebook
├── OS
│   ├── MNB Kernel
│   ├── Omega Gate
│   ├── Ledger
│   ├── Replay
│   ├── SecretRef
│   └── OP Registry
│
├── OSX
│   ├── Desktop
│   ├── Apps
│   ├── Widgets
│   ├── Telemetry
│   └── Causal Geometry
│
├── Browser
│   ├── Source capture
│   ├── DOI resolver
│   ├── arXiv capture
│   └── Claim extractor
│
├── WebX
│   ├── platform connectors
│   ├── node mesh
│   ├── MCP
│   └── API gateway
│
├── OP Store
│   ├── OP Scientific
│   ├── OP Economic
│   ├── OP Shield
│   ├── OP Governance
│   ├── OP Health
│   ├── OP Quantum
│   ├── OP Network
│   └── OP Publication
│
└── Tools
    ├── MNB Calculator
    ├── MatMax Wallet
    ├── IQG Chat
    ├── ProofPack Export
    ├── Evidence Pack Builder
    └── DOI Publisher
```

## OP schema baseline

```yaml
op_id:
name:
domain: scientific | economic | shield | governance | health | quantum | network | publication | product | legal
version:
entrypoint:
inputs:
outputs:
risk_class: low | medium | high | critical
requires_human_review: true
requires_replay: true
requires_hash: true
claim_boundary:
evidence_outputs:
ledger_policy:
release_policy:
```

## Governance loops

Every artifact must pass through three loops:

```text
Learning Loop
  Did this create useful knowledge?

Governance Loop
  Is it admissible, safe and claim-bounded?

Architecture Loop
  Where does it belong in the system?
```

## Merge / PR discipline

Open PRs with `mergeable=false` should not be forced.

```text
PR #19 = URANO launch roadmap governance plan = open / conflict or mergeability issue
PR #20 = TACE / GOV separation architecture = open / conflict or mergeability issue
```

Resolution options:

```text
1. Rebase branches on latest main.
2. Recreate documents from current main.
3. Merge manually through GitHub UI if conflicts are trivial.
4. Prefer one consolidated restructure PR if multiple docs collide.
```

## Claim hygiene

Allowed public claims:

```text
MatVerse is a scientific platform for verifiable trails of research, evidence, governance, publication and replay.
URANO is a staged scientific workbench architecture.
TACE is a research-engineering control layer for AI outputs.
GOV is a staged B2G workflow orchestrator concept.
Benchmark Core is the next clean public release candidate.
```

Blocked claims:

```text
production-ready platform
externally validated platform
proof of digital life
financial return guarantee
gov.br integration without credential/partnership
quantum hardware validation without backend evidence
raw ZIPs ready for DOI
agent or model authorship
```

## Immediate actions

```text
A1. Close or fix PR #19 and PR #20 mergeability.
A2. Create issue: global ecosystem restructure tracker.
A3. Prepare Benchmark Core release in dedicated repo or release path.
A4. Create Zenodo community: MatVerse Research Infrastructure.
A5. Move clean bundles into the correct repo lanes.
A6. Keep raw ZIPs quarantined.
A7. Create TACE-Core spec separately.
A8. Create GOV.RCPN Assist spec separately.
A9. Define OP package schema.
A10. Add OP Risk Simulator to URANO roadmap.
```

## Final verdict

```text
GLOBAL_RESTRUCTURE_PLAN = PASS_DESIGN
RAW_BUNDLES             = BLOCK
NEXT_RELEASE            = Benchmark Core clean
NEXT_PRODUCT_SPEC       = GOV.RCPN Assist
NEXT_RESEARCH_SPEC      = TACE-Core
NEXT_PLATFORM_SPEC      = URANO Notebook clean architecture
NEXT_SECURITY_SPEC      = MatVerse Shield / SecretRef
NEXT_QUANTUM_SPEC       = QeX Q-DOI evidence protocol
```
