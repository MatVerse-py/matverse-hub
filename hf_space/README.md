---
title: MatVerse Memory Registry
emoji: 🧠
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: "5.24.0"
python_version: "3.10"
app_file: app.py
pinned: false
fullWidth: true
header: default
short_description: Landing page oficial e dashboard público de prova do MatVerse.
---

# MatVerse Memory Registry: Landing Page Oficial e Dashboard de Prova

Bem-vindo ao MatVerse Memory Registry, o hub central para a governança e prova pública de artefatos digitais do MatVerse. Este Space serve como a landing page oficial, um dashboard público de artefatos soberanos e um verificador interativo do Ω-Gate.

## Funcionalidades

*   **Landing Institucional**: Informações sobre o MatVerse, sua missão e arquitetura.
*   **Prova Pública com Ω-Gate**: Verifique a admissibilidade de artefatos digitais usando o operador Ω, thresholds, ledger e replay.
*   **Dashboard de Artefatos Soberanos**: Visualize e explore os artefatos registrados no MatVerse.
*   **Verificador Local de Admissibilidade**: Uma interface interativa para testar a conformidade de novos artefatos com as regras de governança do MatVerse.

## Como Usar o Verificador Ω-Gate

O verificador Ω-Gate permite que você insira os metadados de um artefato e obtenha uma decisão de `PASS`, `BLOCK` ou `REVIEW` com base nas políticas de governança do MatVerse. As métricas consideradas incluem:

*   **Ψ (Psi)**: Coerência semântica.
*   **Θ̂ (Theta Normalizado)**: Performance e latência.
*   **CVaR (Conditional Value at Risk)**: Risco de cauda.
*   **PoLE (Proof of Latent Evolution)**: Prova de evolução latente.

### Fórmula do Ω-Gate

$\Omega = 0.4\Psi + 0.3\hat{\Theta} + 0.2(1-\text{CVaR}) + 0.1\text{PoLE}$

### Política de Decisão

*   $\Psi < 0.85 \lor \text{CVaR} > 0.05 \Rightarrow \text{BLOCK}$
*   $\Omega \ge 0.85 \Rightarrow \text{PASS}$
*   $\text{caso contrário} \Rightarrow \text{CONDITIONAL}$

## Estrutura do Repositório

*   `README.md`: Este arquivo, contendo a configuração do Space e informações gerais.
*   `app.py`: O código-fonte da aplicação Gradio que implementa a landing page, o dashboard e o verificador Ω-Gate.
*   `proof_data.json`: Dados de prova e metadados de artefatos para demonstração.
*   `requirements.txt`: Dependências Python necessárias para o Space.

## Contribuição

Para contribuir, por favor, siga as diretrizes de governança do MatVerse e utilize o Ω-Gate para validar suas propostas antes de submeter. Qualquer alteração deve manter ou aumentar o valor de Ω ($\Delta\Omega \ge 0$).

---

**MatVerse: Construindo a Infraestrutura Soberana para a Civilização Digital.**
