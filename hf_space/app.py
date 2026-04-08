import gradio as gr
from dataclasses import dataclass, field
from packaging.version import Version
from typing import List, Literal, Dict, Any
import json
import numpy as np

# --- Ω-Gate Logic (from pasted_content.txt and matverse-artifact-engineering skill) ---

Decision = Literal["PASS", "BLOCK", "REVIEW", "CONDITIONAL"]

SAFE_SOLC_MIN = Version("0.8.32")

@dataclass
class ContractBuildMeta:
    name: str
    compiler_version: str
    is_third_party: bool
    verified_exact_match: bool
    has_known_bug_warning: bool

@dataclass
class ReviewResult:
    decision: Decision
    reasons: List[str]

def normalize_solc(v: str) -> Version:
    v = v.strip().removeprefix("v").split("+")[0]
    return Version(v)

def review_contract(meta: ContractBuildMeta) -> ReviewResult:
    reasons: List[str] = []
    decision: Decision = "PASS"

    solc = normalize_solc(meta.compiler_version)

    if solc < SAFE_SOLC_MIN:
        decision = "BLOCK"
        reasons.append(
            f"Compiler antigo: {meta.compiler_version}. Baseline mínima exigida: {SAFE_SOLC_MIN}"
        )

    if meta.has_known_bug_warning:
        if decision == "PASS":
            decision = "BLOCK"
        reasons.append(
            "Etherscan marcou warning de compiler bug conhecido. Rebuild obrigatório com versão corrigida."
        )

    if meta.is_third_party:
        if decision == "PASS":
            decision = "REVIEW"
        reasons.append(
            "Contrato parece ser dependência/upstream. Não publicar como artefato soberano sem classificação explícita."
        )

    if not meta.verified_exact_match:
        if decision == "PASS":
            decision = "BLOCK"
        reasons.append("Contrato não está em Exact Match verificado.")

    if not reasons:
        reasons.append("Build admissível.")

    return ReviewResult(decision=decision, reasons=reasons)


# Universal Omega Gate (simplified for Gradio demo)
MIN_SOLC_UNIVERSAL = Version("0.8.32")

@dataclass
class Artifact:
    id: str
    platform: str  # evm, github, hf, docker
    compiler: str = None
    hash: str = None
    verified: bool = False
    warnings: List[str] = field(default_factory=list)
    provenance: str = None

def normalize_universal(v: str) -> Version:
    if not v:
        return Version("0.0.0")
    return Version(v.replace("v", "").split("+")[0])

def omega_gate_universal(a: Artifact) -> Dict[str, Any]:
    reasons = []
    score = 1.0
    decision: Decision = "PASS"

    if a.platform == "evm" and a.compiler:
        if normalize_universal(a.compiler) < MIN_SOLC_UNIVERSAL:
            reasons.append("Compiler antigo")
            score -= 0.4
            decision = "BLOCK"

    if a.warnings and len(a.warnings) > 0:
        reasons.append("Warnings detectados")
        score -= 0.3
        if decision == "PASS": decision = "BLOCK"

    if a.provenance != "trusted":
        reasons.append("Origem não confiável")
        score -= 0.2
        if decision == "PASS": decision = "REVIEW"

    if not a.verified:
        reasons.append("Não verificado")
        score -= 0.2
        if decision == "PASS": decision = "REVIEW"

    # MatVerse specific Omega calculation (simplified for demo)
    # Ω = 0.4Ψ + 0.3Θ̂ + 0.2(1−CVaR) + 0.1PoLE
    # For this demo, we'll map the score to Omega conceptually
    omega_score = score # Simplified mapping

    if omega_score < 0.6:
        decision = "BLOCK"
    elif omega_score < 0.85:
        decision = "REVIEW"
    else:
        decision = "PASS"

    if not reasons:
        reasons.append("OK")

    return {"decision": decision, "reasons": reasons, "omega_score": round(omega_score, 3)}


# --- Gradio Interface ---

def verify_artifact(artifact_id, platform, compiler, is_verified, warnings_str, provenance):
    warnings_list = [w.strip() for w in warnings_str.split(',') if w.strip()]
    artifact = Artifact(
        id=artifact_id,
        platform=platform,
        compiler=compiler,
        verified=is_verified,
        warnings=warnings_list,
        provenance=provenance
    )
    result = omega_gate_universal(artifact)
    return result["decision"], f"Ω Score: {result['omega_score']}\nReasons: {', '.join(result['reasons'])}"


# Dummy data for dashboard (replace with actual data loading in a real scenario)
proof_data = json.load(open("proof_data.json"))

def get_dashboard_data():
    # In a real scenario, this would fetch data from a ledger or database
    return proof_data


with gr.Blocks() as demo:
    gr.Markdown(
        """
        # MatVerse Memory Registry: Landing Page Oficial e Dashboard de Prova

        Bem-vindo ao MatVerse Memory Registry, o hub central para a governança e prova pública de artefatos digitais do MatVerse. Este Space serve como a landing page oficial, um dashboard público de artefatos soberanos e um verificador interativo do Ω-Gate.

        ## Verificador Ω-Gate
        Use esta ferramenta para verificar a admissibilidade de artefatos digitais.
        """
    )

    with gr.Tab("Verificador Ω-Gate"):
        with gr.Row():
            artifact_id_input = gr.Textbox(label="ID do Artefato", value="contract_001")
            platform_input = gr.Dropdown(label="Plataforma", choices=["evm", "github", "hf", "docker"], value="evm")
        with gr.Row():
            compiler_input = gr.Textbox(label="Versão do Compilador (se aplicável)", value="v0.8.23")
            is_verified_input = gr.Checkbox(label="Verificado (Exact Match)", value=True)
        with gr.Row():
            warnings_input = gr.Textbox(label="Warnings (separados por vírgula)", value="solidity_bug")
            provenance_input = gr.Dropdown(label="Proveniência", choices=["trusted", "external", "unknown"], value="external")
        
        verify_button = gr.Button("Verificar Admissibilidade")
        
        decision_output = gr.Textbox(label="Decisão do Ω-Gate")
        reasons_output = gr.Textbox(label="Detalhes/Razões")

        verify_button.click(
            verify_artifact,
            inputs=[artifact_id_input, platform_input, compiler_input, is_verified_input, warnings_input, provenance_input],
            outputs=[decision_output, reasons_output]
        )
    
    with gr.Tab("Dashboard de Artefatos Soberanos"):
        gr.Markdown("## Dashboard de Artefatos Soberanos")
        dashboard_data = get_dashboard_data()
        
        # Display data in a more readable format, e.g., a table or individual components
        gr.Markdown("### Artefatos Registrados")
        
        # Example of displaying data from proof_data.json
        if dashboard_data:
            for artifact_key, artifact_details in dashboard_data.items():
                with gr.Accordion(f"Artefato: {artifact_key}"):
                    gr.JSON(artifact_details)
        else:
            gr.Markdown("Nenhum dado de artefato disponível.")

    gr.Markdown(
        """
        --- 
        **MatVerse: Construindo a Infraestrutura Soberana para a Civilização Digital.**
        """
    )


if __name__ == "__main__":
    demo.launch()
