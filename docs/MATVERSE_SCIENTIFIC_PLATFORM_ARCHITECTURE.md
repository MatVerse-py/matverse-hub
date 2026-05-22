# MatVerse Scientific Platform Architecture

## Status

```text
DOCUMENT_STATUS        = STAGE_ARCHITECTURE_CANON
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
REFERENCE_DOI          = 10.5281/zenodo.20343556
PLATFORM_ROLE          = SCIENTIFIC_PLATFORM_FOR_VERIFIABLE_TRAILS
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Definition

MatVerse Scientific Platform is a governed scientific infrastructure for transforming ideas, hypotheses, papers, code, datasets, connectors, agents, research pipelines, proofs, claims and economic primitives into verifiable trails.

The platform does not replace ORCID, GitHub, Zenodo, Hugging Face, ArXiv, blockchain or external repositories. It coordinates them as evidence-bearing organs:

```text
ORCID        = human authorship and identity
GitHub       = code, release, workflow, evidence and replay surface
Zenodo       = DOI archive and citable public record
Hugging Face = datasets, models, demos and research surfaces
ArXiv        = research discovery / preprint reference layer
Blockchain   = timestamp/hash witness, not truth oracle
MatVerse     = causal governance layer connecting all of them
```

## Core constitutional chain

```text
Raw information
  ↓
Research / claim / code / event candidate
  ↓
MNB representation
  ↓
Omega Gate decision
  ↓
Ledger / receipt
  ↓
Replay
  ↓
Evidence Pack
  ↓
DOI / registry / community curation
```

## Macro architecture

```text
MatVerse Scientific Platform
├── Identity & Authorship
│   ├── ORCID
│   └── human creator registry
│
├── Scientific Work Layer
│   ├── Research Trail
│   ├── Paper Vivo
│   ├── Evidence Pack
│   ├── Benchmark Core
│   └── ProofPack
│
├── Governance Layer
│   ├── ACOA
│   ├── Atlas
│   ├── Cassandra
│   ├── Gate
│   ├── Claim Hygiene
│   └── Release Gate
│
├── Security / Shield Layer
│   ├── MNB-Shield
│   ├── RedeVault
│   ├── SecretRef policy
│   ├── provenance checks
│   └── defensive audit trails
│
├── Economic / Omega-Capitals Layer
│   ├── Omega-Capitals thesis
│   ├── research assets
│   ├── proof-backed funding trails
│   ├── grant / capital readiness
│   └── economic work evidence
│
├── Quantum / QeX Layer
│   ├── VQD-FMO benchmark plan
│   ├── Q-DOI records
│   ├── Q-Receipts
│   ├── Q-Replay
│   └── backend evidence packs
│
├── Connector Intelligence Layer
│   ├── Connector Registry
│   ├── UUID Access Broker
│   ├── Audit Ledger
│   ├── Claim Gate
│   └── Card-API console
│
├── Research Nodes
│   ├── Genesis Node
│   ├── ArXiv Pipeline Manager
│   ├── MxV Symbios
│   └── human review queue
│
└── Public Archive Layer
    ├── GitHub releases
    ├── Zenodo DOI records
    ├── Zenodo community
    ├── Software Heritage
    └── public citation metadata
```

## Work-proof families

Each platform organ generates its own proof of work. These are not interchangeable. Each one has a different evidence type, validation gate and public output.

| Domain | Proof family | Work unit | Evidence output | Public record |
|---|---|---|---|---|
| Scientific | PoSW-MV, Proof of Scientific Work | hypothesis, experiment, benchmark, paper, dataset | evidence pack, citation, replay, benchmark report | DOI / Paper Vivo / Zenodo |
| Economic | PoEW-MV, Proof of Economic Work | funding trail, grant, research asset, capital allocation | valuation memo, receipts, budget lineage, impact report | Omega-Capitals registry / DOI support pack |
| Governance | PoGW-MV, Proof of Governance Work | policy, decision, claim, gate, release approval | decision receipt, claim table, release gate report | governance registry |
| Security / Shield | PoSecW-MV, Proof of Security Work | scan, redaction, vault, threat model, mitigation | security report, secret scan, hash manifest, incident receipt | Shield / RedeVault evidence pack |
| Quantum | Q-PoW / Q-DOI | circuit, backend run, QIR, counts, mitigation, observable | Q-receipt, Q-replay, backend report, raw/mitigated hashes | Q-DOI / quantum evidence pack |
| Connector | PoCW-MV, Proof of Connector Work | connector registration, grant, audit event | connector receipt, grant receipt, audit ledger | connector registry |
| Research Discovery | PoRW-MV, Proof of Research Work | ArXiv discovery, source review, claim extraction | source registry, review memo, human decision | research trail |
| Platform / Node | PoNW-MV, Proof of Node Work | public node state, uptime, interface, source registry | node receipt, status report, release metadata | Genesis Node release |

## Omega-Capitals link

Omega-Capitals is the economic interface of the platform. It should not be described as a financial promise or investment return. It is a framework for turning scientific artifacts into proof-backed research assets.

Allowed interpretation:

```text
Omega-Capitals = economic governance layer for research assets whose value is backed by evidence, DOI records, lineage, reproducibility, public metadata and claim hygiene.
```

Blocked interpretation:

```text
profit guarantee
security token by default
financial return promise
valuation without evidence
```

Economic work proof must include:

```text
asset identity
source artifact
DOI or release reference
claim boundaries
cost lineage
funding purpose
risk status
human review
receipt hash
```

## Governance link

Governance is the decision organ of the platform. It converts raw ambition into admissible public claims.

```text
Atlas      = invariants and ontology
Cassandra  = interpretation and routing
ACOA       = audit, policy and admissibility
Gate       = PASS / HOLD / BLOCK / ESCALATE
Ledger     = decision memory
Replay     = decision reproducibility
```

Governance proof must include:

```text
claim id
artifact id
policy used
evidence class
decision
reason
reviewer or system path
receipt hash
```

## Shield / Security link

Shield is the defensive organ. It does not attack. It protects provenance, secrets, evidence, connectors, nodes and publication surfaces.

```text
MNB-Shield = protection of MNB integrity
RedeVault  = vault for authorized network/evidence artifacts
SecretRef  = reference-only secret pattern
Claim Gate = prevents overclaim and unsafe publication
```

Security proof must include:

```text
scan scope
sanitization actions
redaction report
blocked paths
hash manifest
residual risk
publication decision
```

## Quantum and Q-DOI link

The quantum layer must remain evidence-first. A Q-DOI is not a decorative DOI for quantum language. It is a DOI record for a quantum experiment package.

Q-DOI candidate requires:

```text
experiment name
backend or simulator class
circuit / QIR / notebook
shots or simulation parameters
raw counts hash
mitigation configuration
observable result
replay script
MANIFEST.json
HASHES.sha256
claim hygiene
```

VQD-FMO remains STAGE_EXPERIMENTAL until real backend execution or reproducible simulation evidence exists.

Allowed claim:

```text
VQD-FMO is a quantum benchmark plan for VQE-CVaR, error mitigation and backend scheduling.
```

Blocked claim:

```text
VQD-FMO has been validated on real quantum hardware without backend evidence.
```

## Platform states

```text
PASS       = public-ready under the declared scope
STAGE      = useful, structured, but needs cleanup or metadata
HOLD       = incomplete, internal or awaiting evidence
BLOCK      = not publishable in current form
QUARANTINE = sensitive, unsafe or claim-risk material
```

## Release discipline

No raw ZIP package should become a public DOI record.

Required before public release:

```text
README.md
CITATION.cff
codemeta.json
MANIFEST.json
HASHES.sha256
RELEASE_NOTES.md
claim hygiene section
human authorship only
no raw user_input_files
no exposed sensitive operational material
no nested work bundles unless justified
non-production status when alpha
external validation status explicit
```

## Current seed and next candidates

```text
Seed:
MatVerse Hub v0.1.1-alpha
DOI: 10.5281/zenodo.20343556

Next candidates:
1. Benchmark Core clean bundle
2. Genesis Node clean bundle
3. Connector Intelligence Layer clean bundle
4. ArXiv / MxV Symbios research pipeline
5. VQD-FMO only after experiment evidence
```

## Safe public formulation

MatVerse Scientific Platform is a governed research infrastructure for transforming scientific, economic, governance, security, connector and quantum work into verifiable evidence trails, DOI records, receipts, replay artifacts and curated public releases.

## Blocked public formulations

```text
production-ready platform
externally validated without external evidence
proof of digital life
financial return guarantee
quantum hardware validation without execution evidence
raw bundles ready for DOI
agent or model authorship
```
