# MatVerse Hub: Central de Governança e Prova Pública

[![Release v0.1.1-alpha](https://img.shields.io/badge/Release-v0.1.1--alpha-orange?style=flat-square)](https://github.com/MatVerse-py/matverse-hub/releases/tag/v0.1.1-alpha)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20343556.svg)](https://doi.org/10.5281/zenodo.20343556)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red?style=flat-square)](SECURITY.md)

**Autor**: Mateus Alves Arêas — [ORCID: 0009-0008-2973-4047](https://orcid.org/0009-0008-2973-4047)

> ⚠️ Este software está em estágio **alpha**. Não é recomendado para uso em produção.

Este repositório é o núcleo de governança e prova pública do organismo MatVerse. Ele consolida a engenharia de artefatos, a validação de admissibilidade via Ω-Gate e a integração com plataformas de deploy soberano.

## Estrutura do Repositório

- `artifact_engineering_report.md`: Relatório detalhado da engenharia de artefatos do MatVerse, seguindo o formato canônico.
- `omega_gate_validator.py`: Script Python que implementa o Ω-Gate universal para validação de admissibilidade de artefatos.
- `hf_space/`: Código-fonte e configuração para o Hugging Face Space (Landing Page e Dashboard).
- `matverse_ledger.jsonl`: (Em breve) Registro imutável de todas as decisões e provas do sistema.

## Governança Soberana

O MatVerse opera sob o princípio fundamental de que a execução é subordinada à lei algorítmica. Cada ação proposta deve ser validada pelo Ω-Gate para garantir que a coerência sistêmica não seja degradada ($\Delta\Omega \ge 0$).

### Métricas do Ω-Gate

- **Ψ (Psi)**: Coerência semântica e estrutural.
- **Θ̂ (Theta Normalizado)**: Performance operacional.
- **CVaR (Conditional Value at Risk)**: Risco de cauda e segurança.
- **PoLE (Proof of Latent Evolution)**: Prova de evolução e aprendizado.

## Como Contribuir

Para propor alterações ou novos artefatos, utilize o `omega_gate_validator.py` para verificar a admissibilidade. Apenas artefatos com decisão `PASS` são elegíveis para deploy soberano.

---

**MatVerse: Construindo a Infraestrutura Soberana para a Civilização Digital.**
