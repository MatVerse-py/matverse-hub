# MatVerse Hub Indexing Guide

## 1. Definição fundacional

Este guia define o protocolo de indexação do `MatVerse-py/matverse-hub` para tornar o repositório legível, auditável e recuperável por agentes, conectores, mecanismos de busca semântica e sistemas de governança do ecossistema MatVerse.

O objetivo não é apenas expor arquivos para leitura. O objetivo é transformar o repositório em um índice verificável de conhecimento operacional.

Analogia técnica: este guia funciona para o MatVerse Hub como um `robots.txt` constitucional combinado com um `MANIFEST.in` semântico e um ledger de curadoria.

## 2. Escopo de indexação

### 2.1 Arquivos de alta prioridade

Indexar sempre:

```text
README.md
INDEXING_GUIDE.md
manifest.json
matverse.layer.json
CONSTITUTION.md
ARCHITECTURE.md
MAINTENANCE.md
CHANGELOG.md
LICENSE
src/**
api/**
core/**
services/**
schemas/**
docs/**
proofs/**
governance/**
routes/**
```

### 2.2 Arquivos de média prioridade

Indexar quando existirem metadados úteis:

```text
*.py
*.ts
*.tsx
*.js
*.jsx
*.json
*.yaml
*.yml
*.md
Dockerfile
docker-compose.yml
railway.json
.github/workflows/**
```

### 2.3 Arquivos a ignorar

Nunca indexar como conhecimento canônico:

```text
node_modules/**
dist/**
build/**
.next/**
.cache/**
.venv/**
venv/**
__pycache__/**
*.pyc
*.log
.env
.env.*
*.pem
*.key
*.sqlite
*.db
```

Motivo: esses arquivos são derivados, secretos, temporários ou ambientes locais. Indexá-los aumenta ruído, risco e custo semântico.

## 3. Camadas MatVerse mapeadas

Cada arquivo indexado deve ser classificado em exatamente uma camada primária e, quando necessário, em camadas secundárias.

```text
MATVERSE      → ciência, leis, MNB, campo e totalidade
SYMBIODROID   → HM, experimentos, memória local, dados e segurança
SYMBIOS       → experiências, OS/OSX e continuidade humano-organismo
ACOA          → arquitetura de governança coerente
IA-GOV        → agentes, IA, claims, ferramentas e execução
QEX           → execução quântico-clássica, MNB_Q e QCP
CASSANDRA     → ponte comunicadora entre estados e domínios
ATLAS         → topologia, taxonomia, invariantes e mapa científico
OMEGA_GATE    → decisão PASS/ESCALATE/BLOCK
LEDGER        → memória causal, hash, Merkle, replay e prova
```

## 4. Manifesto mínimo por repositório

Todo repositório do ecossistema deve conter um `matverse.layer.json` com este formato mínimo:

```json
{
  "repository": "owner/name",
  "layer": "matverse|symbiodroid|symbios|acoa|ia_gov|qex|cassandra|atlas|omega_gate|ledger|infra|product|lab|legacy",
  "status": "canonical|runtime|lab|legacy|archived|quarantine",
  "role": "descrição objetiva da função",
  "primary_outputs": ["artifact", "api", "manifest", "proof", "dataset"],
  "evidence": {
    "has_readme": true,
    "has_tests": false,
    "has_runtime": false,
    "has_ledger": false,
    "has_replay": false
  },
  "governance": {
    "psi_min": 0.85,
    "cvar_max": 0.05,
    "omega_min": 0.85
  }
}
```

## 5. MNB de indexação

Cada item indexado deve gerar uma unidade mínima de memória verificável:

```text
MNB = (e, Ψ, C, τ, h)
```

Onde:

```text
e = embedding ou representação vetorial do conteúdo
Ψ = coerência semântica em [0,1]
C = custo computacional ou tamanho do artefato
τ = persistência temporal estimada
h = hash SHA-256 canônico
```

Regra de hash:

```text
h = SHA256(canonical_json({path, content_hash, layer, role, timestamp_causal}))
```

Nunca usar `hash()` de linguagem runtime para identidade canônica. O hash precisa ser estável entre máquinas, processos e execuções.

## 6. Ω-Gate de indexação

O score de admissibilidade do item indexado é:

```text
Ω = 0.4·Ψ + 0.3·Θ̂ + 0.2·(1−CVaR) + 0.1·PoLE
```

Critérios:

```text
PASS      → Ψ >= 0.85 AND CVaR <= 0.05 AND Ω >= 0.85 AND evidence=true
REVIEW    → evidência existe, mas uma métrica está abaixo do limiar
BLOCK     → sem evidência, sem hash, sem replay quando replay for obrigatório, ou claim acima da prova
```

## 7. PoSE, PoLE e Ledger

### 7.1 PoSE

PoSE registra que uma regra semântica foi aplicada ao artefato:

```text
artifact → semantic_policy → decision → receipt
```

### 7.2 PoLE

PoLE só pode ser positivo se houver evolução verificável:

```text
PoLE = 1 ⇔ ΔΨ >= 0 AND ΔCVaR <= 0 AND ledger_growth > 0
```

### 7.3 Ledger

Toda decisão relevante deve gerar um registro:

```json
{
  "index": 0,
  "prev_hash": "GENESIS",
  "path": "README.md",
  "layer": "matverse",
  "decision": "PASS",
  "psi": 0.91,
  "cvar": 0.02,
  "omega": 0.92,
  "payload_hash": "sha256:...",
  "entry_hash": "sha256:..."
}
```

## 8. Audit bundle

Ao final da indexação, gerar um bundle auditável:

```text
index_audit_bundle/
├── manifest.json
├── files_indexed.json
├── mnb_registry.jsonl
├── omega_decisions.jsonl
├── ledger.jsonl
├── merkle_root.txt
└── report.md
```

Campos mínimos de `manifest.json`:

```json
{
  "repository": "MatVerse-py/matverse-hub",
  "branch": "fix/indexing-v2",
  "indexed_at": "ISO-8601",
  "files_seen": 0,
  "files_indexed": 0,
  "files_blocked": 0,
  "merkle_root": "sha256:pending",
  "decision": "PASS|REVIEW|BLOCK"
}
```

## 9. Protocolo de execução

```text
SCAN → CLASSIFY → HASH → SCORE → DECIDE → LEDGER → BUNDLE → REPORT
```

Detalhamento:

```text
SCAN      → localizar arquivos permitidos
CLASSIFY  → mapear camada MatVerse
HASH      → gerar SHA-256 canônico
SCORE     → calcular Ψ, Θ̂, CVaR, PoLE e Ω
DECIDE    → PASS, REVIEW ou BLOCK
LEDGER    → registrar decisão em JSONL encadeado
BUNDLE    → gerar pacote de auditoria
REPORT    → publicar sumário legível
```

## 10. Comando local recomendado

```bash
python tools/index_repo.py \
  --repo . \
  --branch fix/indexing-v2 \
  --out index_audit_bundle
```

Quando `tools/index_repo.py` ainda não existir, use este guia como especificação funcional para implementá-lo.

## 11. Critérios de fechamento

O repositório pode ser considerado indexado quando:

```text
1. README.md existe
2. INDEXING_GUIDE.md existe
3. matverse.layer.json existe ou manifest.json cobre a camada
4. todos os arquivos indexados têm SHA-256
5. cada arquivo tem camada primária
6. todo claim forte tem evidência textual ou é marcado como hipótese
7. audit bundle é gerado
8. decisão final é PASS ou REVIEW, nunca silêncio
```

## 12. Decisão atual

```text
repository = MatVerse-py/matverse-hub
branch = fix/indexing-v2
status = REVIEW
motivo = guia de indexação criado; falta implementar indexador executável e audit bundle real
próximo passo = criar tools/index_repo.py e matverse.layer.json
```
