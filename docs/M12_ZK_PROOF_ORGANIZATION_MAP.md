# M12 ZK-Proof Organization Map

## Status

```text
DOCUMENT_STATUS        = ORGANIZATION_MAP
MODULE_NAME            = M12 ZK-Proof System
PARENT_LAYER           = MatVerse ZK / PQC Evidence Layer
ZK_STATUS              = STAGE_TECHNICAL_CANDIDATE
PQC_STATUS             = DESIGN_MIGRATION_LAYER
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
RAW_PUBLICATION        = BLOCK_UNTIL_CLEAN_RELEASE
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

M12 is the first concrete technical candidate for the MatVerse ZK track.

Its role is to move from ordinary hash/replay trust toward cryptographic verification of off-chain computations using ZK proofs.

M12 must be organized as a technical proof system, not as a broad platform narrative.

## Core distinction

```text
Hash proves that an artifact existed.
Replay proves that an execution can be reproduced.
ZK proof proves that a computation satisfied constraints without requiring trust in the executor.
PQC protects the long-term validity of signatures and evidence trails against future quantum cryptanalysis.
```

Therefore:

```text
M12 = ZK verification module.
ZK/PQC Layer = broader evidence-security architecture.
URANO = workbench that may call M12.
GOV = may use M12 for selective verification.
TACE = may use M12 to prove control constraints.
QeX/Q-DOI = may use M12/PQC for quantum evidence receipts later.
```

## Recommended repository

```text
matverse-m12-zk-proof/
```

Alternative if kept under QeX/security lane:

```text
matverse-zk-pqc-evidence/
└── m12-zk-proof/
```

Do not place M12 inside GOV or TACE directly. GOV and TACE may consume M12 as a dependency.

## Clean directory structure

```text
matverse-m12-zk-proof/
├── README.md
├── CITATION.cff
├── codemeta.json
├── MANIFEST.json
├── HASHES.sha256
├── RELEASE_NOTES.md
├── CLAIM_HYGIENE.md
├── SECURITY.md
├── package.json
│
├── circuits/
│   ├── omega.circom
│   ├── omega_main.circom
│   └── lib/
│       └── omega_template.circom
│
├── contracts/
│   └── OmegaVerifier.sol
│
├── scripts/
│   ├── compile.sh
│   ├── setup_trusted.sh
│   ├── generate_proof.sh
│   ├── verify_proof.sh
│   ├── run_tests.sh
│   └── generate_inputs.js
│
├── inputs/
│   └── examples/
│       └── omega_valid.example.json
│
├── test/
│   └── run_tests.js
│
├── docs/
│   ├── TECHNICAL_SPEC.md
│   ├── TRUSTED_SETUP.md
│   ├── ONCHAIN_VERIFICATION.md
│   ├── ZK_LIMITATIONS.md
│   └── PQC_MIGRATION_NOTES.md
│
├── evidence/
│   ├── TEST_REPORT.md
│   ├── CIRCUIT_INFO.json
│   ├── PROOF_SAMPLE_MANIFEST.json
│   └── VERIFICATION_REPORT.json
│
└── build/
    └── .gitkeep
```

## Build artifact policy

Generated artifacts must not be treated as source of truth.

```text
build/*.r1cs             = generated
build/*_js/              = generated
build/*.zkey             = generated / sensitive ceremony context
build/*.ptau             = generated / ceremony artifact
build/proof.json         = generated sample proof
build/public.json        = generated sample public input
```

For public release, either:

```text
1. exclude build artifacts and provide reproducible scripts; or
2. include only a small sample proof bundle under evidence/ with clear manifest and hashes.
```

Never publish toxic-waste-adjacent material or private ceremony entropy.

## M12 pipeline

```text
Omega constraint specification
  ↓
Circom circuit
  ↓
R1CS compilation
  ↓
trusted setup / ceremony
  ↓
witness generation
  ↓
Groth16 proof generation
  ↓
local verification
  ↓
Solidity verifier generation
  ↓
on-chain verification candidate
  ↓
receipt / ledger / evidence pack
```

## Ω* circuit scope

The current M12 circuit should remain narrowly scoped.

```text
Ω*(psi, cvar, time, overfit)
= psi - 0.5*cvar - 0.2*time - 0.3*overfit >= threshold
```

Recommended fixed-point representation:

```text
range: [0, 1e9]
float usage: BLOCK
integer/fixed-point arithmetic: REQUIRED
input bounds: REQUIRED
```

## Public claim boundary

Allowed claim:

```text
M12 is a staged ZK-SNARK proof-system candidate for verifying an Ω-style constraint computation using Circom/Groth16 and an on-chain verifier architecture.
```

Blocked claims:

```text
M12 is production-ready.
M12 removes all trust assumptions.
M12 is externally audited.
M12 is post-quantum secure.
Groth16 trusted setup is harmless.
ZK proof alone proves real-world truth.
```

## ZK / PQC positioning

M12 currently belongs to the ZK track.

```text
M12-ZK = concrete circuit/proof candidate.
M12-PQC = future migration track for signatures, receipt verification and long-term evidence protection.
```

Important:

```text
Groth16 is not post-quantum secure by default.
A ZK proof can still rely on classical cryptographic assumptions.
PQC must be added as a separate signature/receipt/migration layer.
```

## Required evidence before PASS_PUBLIC

```text
circuit compiles from clean checkout
R1CS info captured
sample valid proof generated
sample invalid proof rejected
verify_proof.sh returns correct exit codes
OmegaVerifier.sol compiles
trusted setup assumptions documented
no secret values or private entropy published
MANIFEST.json covers release files
HASHES.sha256 covers release files
TEST_REPORT.md exists
CLAIM_HYGIENE.md exists
```

## Integration with MatVerse components

### URANO

```text
URANO can call M12 as OP ZK Proof.
Notebook cell → Ω inputs → proof generation → verification report → evidence pack.
```

### GOV

```text
GOV can use M12 for selective verification of workflow constraints.
Example: prove process conditions were satisfied without exposing raw documents.
```

### TACE

```text
TACE can use M12 to prove an output-control constraint was satisfied.
Example: prove entropy/risk/time/overfit threshold passed.
```

### Shield

```text
Shield owns secret scan, build artifact policy, ceremony-risk policy and cryptographic inventory.
```

### QeX / Q-DOI

```text
QeX may use M12-style proof packaging for experiment receipts, but Q-DOI needs separate quantum evidence schema.
```

## Security notes

Groth16 requires trusted setup. M12 must explicitly document:

```text
trusted setup procedure
ceremony assumptions
toxic waste risk
who contributed entropy
whether the setup is demo-only or production-grade
```

If this cannot be documented, the release status must remain:

```text
STAGE_DEMO_ONLY
```

## Release recommendation

```text
Release type:
alpha / pre-release

Suggested tag:
v0.1.0-alpha

Suggested title:
MatVerse M12 ZK-Proof System v0.1.0-alpha — Ω Constraint Verification Prototype

Public readiness:
STAGE_TO_PASS only after local compile/test report.
```

## Relationship to global restructure

```text
matverse-hub
  = documentation and DOI seed

matverse-m12-zk-proof
  = standalone ZK proof module

matverse-shield
  = crypto inventory, SecretRef and PQC migration policy

shared-governance-kernel
  = receipt/ledger/replay primitives only
```

## Final verdict

```text
M12_ZK_PROOF_SYSTEM        = STAGE_TECHNICAL_CANDIDATE
ZK_REAL_IMPLEMENTATION     = PARTIAL / REQUIRES BUILD EVIDENCE
PQC_SECURITY               = NOT_IMPLEMENTED / DESIGN_TRACK
RAW_PUBLICATION            = BLOCK_UNTIL_CLEAN_RELEASE
NEXT_ACTION                = create clean matverse-m12-zk-proof package with tests and evidence report
```
