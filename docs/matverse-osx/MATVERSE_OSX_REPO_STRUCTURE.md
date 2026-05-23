# MatVerse.OSX Repository Structure (Proposta)

```text
matverse/
├── notebook-sovereign-osx/
├── iqg-runtime/
├── tace/
├── gov-assist-orchestrator/
└── shared-governance-kernel/
```

## Subestruturas essenciais
- notebook-sovereign-osx: UX, hardware profile, secure boot, vault, mesh
- iqg-runtime: primordial, svca, mnb-engine, omega-gate, motor, ledger, replay, evidence-pack
- shared-governance-kernel: receipt, ledger, policy, hash, merkle

## Regra de separação
TACE e GOV com fronteiras explícitas; integração somente por kernel compartilhado.
