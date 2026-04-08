from dataclasses import dataclass
from packaging.version import Version
from typing import List, Literal, Dict, Any
import numpy as np

Decision = Literal["PASS", "BLOCK", "REVIEW"]

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
    # Ex.: "v0.8.23+commit.f704f362" -> Version("0.8.23")
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
        if decision == "PASS": # Only block if not already blocked by compiler version
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
        if decision == "PASS": # Only block if not already blocked
            decision = "BLOCK"
        reasons.append("Contrato não está em Exact Match verificado.")

    if not reasons:
        reasons.append("Build admissível.")

    return ReviewResult(decision=decision, reasons=reasons)


# Universal Omega Gate from the second part of the provided content
MIN_SOLC_UNIVERSAL = Version("0.8.32")

@dataclass
class Artifact:
    id: str
    platform: str  # evm, github, hf, docker
    compiler: str = None
    hash: str = None
    verified: bool = False
    warnings: List[str] = None
    provenance: str = None

def normalize_universal(v: str) -> Version:
    if not v:
        return Version("0.0.0") # Default to a very old version if none is provided
    return Version(v.replace("v", "").split("+")[0])

def omega_gate_universal(a: Artifact):
    reasons = []
    score = 1.0

    # 1. Compiler check
    if a.compiler:
        if a.platform == "evm" and normalize_universal(a.compiler) < MIN_SOLC_UNIVERSAL:
            reasons.append("compiler antigo")
            score -= 0.4

    # 2. Warnings
    if a.warnings and len(a.warnings) > 0:
        reasons.append("warnings detectados")
        score -= 0.3

    # 3. Provenance
    if a.provenance != "trusted":
        reasons.append("origem não confiável")
        score -= 0.2

    # 4. Verification
    if not a.verified:
        reasons.append("não verificado")
        score -= 0.2

    # decisão
    if score < 0.6:
        return "BLOCK", reasons, score

    if score < 0.85:
        return "REVIEW", reasons, score

    return "PASS", ["ok"], score

def execute_action(artifact: Artifact, action_func):
    decision, reasons, score = omega_gate_universal(artifact)

    if decision == "BLOCK":
        raise Exception(f"BLOCKED: {artifact.id} -> {reasons}")

    if decision == "REVIEW":
        print(f"REVIEW REQUIRED: {artifact.id} -> {reasons}")
        return None

    print(f"EXECUTING: {artifact.id} ({artifact.platform})")
    return action_func()

# Dummy functions for actions
def deploy_evm(bytecode):
    print(f"Deploying EVM contract with bytecode: {bytecode[:10]}...")
    return "tx_hash_placeholder"

def push_repo():
    print("Pushing to GitHub repository...")
    return "commit_hash_placeholder"

def deploy_space():
    print("Deploying Hugging Face Space...")
    return "space_url_placeholder"

def deploy_container():
    print("Deploying Docker container...")
    return "container_id_placeholder"


if __name__ == "__main__":
    print("--- Executando Ω-Gate para contrato EVM (exemplo 1) ---")
    meta_contract_1 = ContractBuildMeta(
        name="EIP7702StatelessDeleGator",
        compiler_version="v0.8.23+commit.f704f362",
        is_third_party=True,
        verified_exact_match=True,
        has_known_bug_warning=True,
    )
    result_contract_1 = review_contract(meta_contract_1)
    print(f"Resultado do Contrato 1: {result_contract_1}\n")

    print("--- Executando Ω-Gate Universal para artefato EVM (exemplo 2) ---")
    artifact_evm = Artifact(
        id="contract_001",
        platform="evm",
        compiler="v0.8.23",
        verified=True,
        warnings=["solidity_bug"],
        provenance="external"
    )
    try:
        execute_action(artifact_evm, lambda: deploy_evm("bytecode_example"))
    except Exception as e:
        print(e)
    print("\n")

    print("--- Executando Ω-Gate Universal para artefato GitHub (exemplo 3) ---")
    artifact_github = Artifact(
        id="repo_matverse_core",
        platform="github",
        compiler=None,
        verified=True,
        warnings=[],
        provenance="trusted"
    )
    try:
        execute_action(artifact_github, lambda: push_repo())
    except Exception as e:
        print(e)
    print("\n")

    print("--- Executando Ω-Gate Universal para artefato Hugging Face (exemplo 4) ---")
    artifact_hf = Artifact(
        id="matverse_space",
        platform="hf",
        compiler=None,
        verified=False, # Not verified yet
        warnings=[],
        provenance="trusted"
    )
    try:
        execute_action(artifact_hf, lambda: deploy_space())
    except Exception as e:
        print(e)
    print("\n")

    print("--- Executando Ω-Gate Universal para artefato Docker (exemplo 5) ---")
    artifact_docker = Artifact(
        id="matverse_container",
        platform="docker",
        compiler="python3.9", # Example of a compiler version for Docker image build
        verified=True,
        warnings=[],
        provenance="trusted"
    )
    try:
        execute_action(artifact_docker, lambda: deploy_container())
    except Exception as e:
        print(e)
    print("\n")

    print("--- Executando Ω-Gate Universal para artefato EVM (exemplo 6 - PASS) ---")
    artifact_evm_pass = Artifact(
        id="contract_002",
        platform="evm",
        compiler="v0.8.32",
        verified=True,
        warnings=[],
        provenance="trusted"
    )
    try:
        execute_action(artifact_evm_pass, lambda: deploy_evm("bytecode_example_pass"))
    except Exception as e:
        print(e)
    print("\n")
