# TACE / GOV Separation Architecture

## Status

```text
DOCUMENT_STATUS        = ARCHITECTURE_DECISION_RECORD
DECISION               = SEPARATE_TACE_AND_GOV
TACE_ROLE              = RESEARCH_ENGINEERING_CONTROL_LAYER
GOV_ROLE               = B2G_AUDITABLE_PRODUCT_LAYER
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Core decision

TACE and GOV must remain separate tracks.

```text
TACE = research and engineering engine for informational-thermodynamic AI control.
GOV  = auditable B2G product for governed public-service workflows.
```

They may share primitives later, but they must not share market language, ontology, claims or launch promises at this stage.

## Why separation is mandatory

TACE and GOV have opposite public surfaces.

```text
TACE speaks to:
research, metrics, simulation, entropy, cost, coherence, CVaR, AI control, benchmarks.

GOV speaks to:
public institutions, compliance, identity, workflow, audit, legal process, security, human review.
```

Mixing them weakens both:

```text
TACE becomes less rigorous if forced into sales language.
GOV becomes less credible if sold with thermodynamic or quantum-heavy vocabulary.
```

## Track 1 — TACE

### Definition

```text
TACE = Thermodynamic AI Control Engine
```

Defensible public definition:

```text
TACE is an informational control engine for measuring and reducing uncertainty, hallucination risk, semantic entropy, computational waste and operational tail risk in AI outputs.
```

### Function

TACE measures and governs AI outputs before they are accepted, shown, stored or promoted.

```text
Input:
text, logs, model outputs, embeddings, runtime metrics, cost, latency, temperature when available, variation across multiple responses.

Measurements:
Psi coherence, CVaR tail risk, semantic entropy, computational cost, response instability, replay variance.

Decisions:
PASS, REPAIR, COMPRESS, REGENERATE, ESCALATE, BLOCK.

Output:
optimized response, receipt, score, minimal rationale, ledger entry.
```

### MVP scope

```text
TACE-Core      = Python library for output control.
TACE-Bench     = benchmark with 100k simulated or replayed executions.
TACE-Agent     = wrapper for local/API LLMs applying gates before final output.
TACE-Dashboard = entropy, cost, Psi, CVaR, replay and cost-saving panel.
```

### Commercial metric

```text
Cost per valid decision.
```

Not:

```text
AI thinks better.
Infinite energy.
Thermodynamic breakthrough.
Physical heat-to-intelligence conversion.
```

### Physical R&D boundary

Any physical interpretation, including heat recovery, thermoelectric devices, Q-TEC, reservoir computing or hardware dissipation, belongs to:

```text
TACE-Physical-RD = HOLD_UNTIL_REAL_EXPERIMENT
```

The MVP is informational and computational, not a physical-energy claim.

## Track 2 — GOV

### Definition

```text
GOV = GOV.Assist Orchestrator
```

Defensible public definition:

```text
GOV is an auditable orchestrator for digital public-service workflows with identity, document validation, procedural guidance, protocoling, human review and replayable audit trails.
```

### Function

GOV turns a public-service request into a governed, auditable workflow.

```text
Input:
citizen/server request, documents, forms, status checks.

Identity:
gov.br/OIDC mock in MVP; real gov.br only with proper credential/partnership.

Process:
domain workflow engine, starting with RCPN.

AI:
triage, explanation, preliminary validation and form assistance only.

Execution:
versioned actions; no free command execution.

Audit:
append-only ledger with event hash, document hash, operator, timestamp and decision.

Output:
protocol, status, receipt and audit trail.
```

### MVP scope

```text
GOV.RCPN Assist
```

Candidate workflows:

```text
recognition of paternity
simple registry correction
second copy request
status consultation
preliminary document triage
```

No real production integration is required in the first MVP. Start with a demonstrable sandbox, official-looking mock flows, logs and audit reports.

### Modules

```text
GOV-Core            = FastAPI, auth, RBAC, workflow engine.
GOV-Skills          = procedure catalog with schema, permissions, risks and outputs.
GOV-Ledger          = hash-based audit, JSONL or SQLite/Postgres initially.
GOV-Identity-Bridge = OIDC mock now; gov.br later only with proper credentialing.
GOV-Review          = human review queue for sensitive cases.
GOV-Portal          = citizen/server interface.
```

### Identity and Web3 boundary

For government use, MetaMask/Web3 must remain optional.

```text
gov.br / OIDC / ICP-Brasil = primary public-sector identity path.
Web3 / blockchain          = optional hash witness layer.
MatMax Wallet              = optional receipt/witness interface, not civil identity source.
```

## Repository separation

Recommended repositories:

```text
matverse-tace/
  Research and engineering track.
  Entropy, risk, cost, coherence, AI control, benchmarks and replay.

gov-assist-orchestrator/
  B2G product track.
  Workflow, identity, audit, compliance, RCPN demo and human review.

shared-governance-kernel/
  Optional later.
  Only shared primitives: receipt, ledger, hash, replay, policy schema, PASS/HOLD/BLOCK.
```

The shared kernel must not force GOV to inherit TACE's thermodynamic vocabulary.

## Integration rule

GOV may use TACE internally, but TACE must appear inside GOV as a discreet component:

```text
Risk and Coherence Engine
```

Not as:

```text
thermodynamic AI engine for government
quantum governance engine
physical entropy converter
```

## Build order

```text
1. TACE v0.1
   Entropic control layer for AI outputs.
   Deliverable: library + benchmark + computational economy report.

2. GOV v0.1
   Auditable orchestrator for digital public services.
   Deliverable: GOV.RCPN Assist demo + ledger + mock identity + panel + legal-technical report.

3. Shared Governance Kernel
   Only after both tracks have clean contracts.
```

## Evidence requirements for TACE

```text
TACE_CORE_TESTS
TACE_BENCH_100K
COST_PER_VALID_DECISION_REPORT
ENTROPY_REDUCTION_REPORT
CVaR_RISK_REPORT
REPLAY_VARIANCE_REPORT
CLAIM_HYGIENE
MANIFEST
HASHES
```

## Evidence requirements for GOV

```text
RCPN_WORKFLOW_SPEC
AUTH_MODEL
RBAC_MATRIX
AUDIT_LEDGER_SAMPLE
HUMAN_REVIEW_FLOW
SECURITY_POLICY
LEGAL_SCOPE_BOUNDARY
CLAIM_HYGIENE
MANIFEST
HASHES
```

## Claim hygiene

### TACE allowed claims

```text
TACE measures and controls informational risk, semantic entropy, computational waste and tail risk in AI outputs.
TACE can be benchmarked by cost per valid decision, replay variance and risk reduction.
```

### TACE blocked claims

```text
TACE converts heat into intelligence.
TACE proves physical thermodynamic AI.
TACE guarantees truth.
TACE eliminates hallucination completely.
```

### GOV allowed claims

```text
GOV is an auditable workflow orchestrator for digital public-service procedures.
GOV can assist triage, document flow, protocoling, audit and human review in a sandbox/MVP.
```

### GOV blocked claims

```text
GOV is production-ready for government.
GOV is officially integrated with gov.br without credential/partnership.
GOV replaces public servants or legal review.
GOV provides legal decisions autonomously.
```

## Final verdict

```text
TACE = STAGE_RESEARCH_ENGINE
GOV  = STAGE_B2G_PRODUCT
MIXED_POSITIONING = BLOCK
SHARED_KERNEL = OPTIONAL_AFTER_CONTRACTS
NEXT_ACTION = create TACE-Core spec and GOV.RCPN Assist spec separately
```
