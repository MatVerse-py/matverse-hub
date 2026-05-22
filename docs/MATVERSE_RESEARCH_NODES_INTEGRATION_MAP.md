# MatVerse Research Nodes Integration Map

## Status

```text
DOCUMENT_STATUS        = STAGE_INTEGRATION_MAP
REFERENCE_RELEASE      = MatVerse Hub v0.1.1-alpha
REFERENCE_DOI          = 10.5281/zenodo.20343556
PLATFORM_LAYER         = MatVerse Scientific Platform
NODE_LAYER             = STAGE_TO_PASS
PRODUCTION_READINESS   = HOLD
PUBLIC_VALIDATION      = HOLD_EXTERNAL_REQUIRED
HUMAN_AUTHORSHIP       = Mateus Arêas / ORCID 0009-0008-2973-4047
```

## Purpose

This document integrates the newly reviewed environment, ArXiv, MxV Symbios and Genesis Node artifacts into the MatVerse scientific platform roadmap.

The goal is to distinguish between:

```text
raw uploaded bundles
clean public candidates
human-reviewed research pipeline
public node interface prototype
deployment automation that must remain blocked
```

No raw ZIP package is approved for direct DOI publication.

## Reviewed uploads

```text
env.zip
= combined export containing MNB deployment dashboard, ArXiv pipeline UI, MxV Symbios UI, nested ZIPs and user_input_files.

node.zip
= Genesis Node React/Vite source bundle with generated dist output and raw user_input_files.
```

## Artifact classification

| Artifact | State | Function | Action |
|---|---|---|---|
| env.zip | BLOCK_RAW | Combined environment/deploy/research export | Do not publish raw |
| MNB deployment dashboard | HOLD_SECURITY | UI pattern for environment/deploy variables | Do not publish as public frontend; redesign around protected secrets and human review |
| MatVerse ArXiv Pipeline Manager | STAGE_TO_PASS | Human-in-the-loop research discovery and staging UI | Keep as research organizer, not deploy automator |
| MxV Symbios | STAGE_TO_PASS | MatVerse + ArXiv research core prototype | Keep as research platform interface |
| node.zip | HOLD_RAW | Genesis Node source plus generated output and raw input files | Do not publish raw |
| MatVerse Genesis Node clean bundle | STAGE_TO_PASS | Alpha public node interface prototype | Review/build check before release |
```

## Clean bundles produced outside repository

```text
matverse_genesis_node_v0_1_0_alpha_clean.zip
= cleaned Genesis Node source bundle excluding generated dist and raw input files.

matverse_arxiv_symbios_research_pipeline_v0_1_0_alpha_clean.zip
= cleaned research pipeline bundle including ArXiv Pipeline Manager and MxV Symbios only.
```

## Security decision

The environment-variable dashboard pattern is not approved for public release because secret values must not be entered into or stored by a public frontend.

Required policy:

```text
Secrets stay in protected platform secret stores.
Frontend code must not contain or persist secret values.
OpenAPI may name headers, but must not include secret values.
Deployment is organized by the pipeline, but execution remains human-reviewed.
Private keys must never be pasted into chat, Markdown, public HTML, repositories, or browser localStorage.
```

## Research pipeline interpretation

ArXiv should be treated as a research source and discovery substrate, not as an automatic publication target.

Allowed pipeline:

```text
ArXiv discovery
  ↓
research queue
  ↓
claim extraction
  ↓
human review
  ↓
MNB representation
  ↓
Omega Gate decision
  ↓
evidence pack candidate
  ↓
manual publication decision
```

Blocked pipeline:

```text
ArXiv discovery
  ↓
automatic deploy
  ↓
automatic publication
```

## Genesis Node interpretation

Genesis Node should be treated as an alpha public interface prototype. It can present identity, node status, boot sequence and platform narrative, but it must not claim to be a production blockchain node, externally validated runtime, or proof of digital life.

Allowed claim:

```text
MatVerse Genesis Node v0.1.0-alpha is an alpha interface prototype for presenting a public MatVerse node concept.
```

Blocked claims:

```text
production-ready node
externally validated node
live blockchain node
proof of digital life
agent authorship
```

## Integration architecture

```text
MatVerse Scientific Platform
  ↓
MatVerse Hub v0.1.1-alpha / DOI seed
  ↓
MatVerse Research Infrastructure community
  ↓
Research Nodes
  ├── Genesis Node interface prototype
  ├── ArXiv Pipeline Manager
  └── MxV Symbios research core
  ↓
Human review
  ↓
MNB / Omega Gate / Ledger / Replay
  ↓
Evidence Pack / DOI candidate
```

## Next actions

```text
1. Keep env.zip and node.zip internal.
2. Review the two clean bundles.
3. Do not publish the environment-variable dashboard as a public frontend.
4. Use ArXiv/MxV bundle as research organizer only.
5. Use Genesis Node clean bundle as alpha interface prototype candidate.
6. Run build/lint checks before any release.
7. Publish only after README, CITATION, codemeta, MANIFEST, HASHES and release notes are verified.
8. Associate accepted releases with MatVerse Research Infrastructure community.
```
