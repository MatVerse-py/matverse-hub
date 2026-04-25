#!/usr/bin/env python3
"""
MatVerse Repository Indexing / Visibility Trigger v2.

This script queries GitHub Code Search with `repo:OWNER/REPO import` and writes
JSON/JSONL evidence. It never proves ChatGPT/OpenAI visibility by itself.

Token handling:
  export GH_TOKEN="..."      # or GITHUB_TOKEN
  python3 scripts/index-repos-v2.py --delay 1.0

Never paste tokens into shell history, issues, PRs, chats, logs, or files.
"""
from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

DEFAULT_REPOS = [
    "MatVerse-py/ODA-QF", "MatVerse-py/Pose", "MatVerse-py/matverse-u-os",
    "MatVerse-py/matverse-u-kernel", "MatVerse-py/matverse-u-docs",
    "MatVerse-py/matverse-u-lua", "MatVerse-py/matverse-u-gate",
    "MatVerse-py/matverse-u-network", "MatVerse-py/matverse-twin-core",
    "MatVerse-py/bunker-genesis-mirror", "MatVerse-py/matverse-secure-loader",
    "MatVerse-py/svca-lab-genesis", "MatVerse-py/svca-lab",
    "MatVerse-py/acoa", "MatVerse-py/organismo", "MatVerse-py/SuperKernel-6.0",
    "MatVerse-py/MatVerse-Page", "MatVerse-py/delta-circuit-ignite",
    "MatVerse-py/IA.GOV", "MatVerse-py/Symbiodroid", "MatVerse-py/mnbs-seed",
    "MatVerse-py/matverse-landing-page", "MatVerse-py/matverse-mcp-server",
    "MatVerse-py/gpt-cassndra--pilot", "MatVerse-py/Core.Eng",
    "MatVerse-py/matverse-u-verifier", "MatVerse-py/github-url-validator",
    "MatVerse-py/matverse-github-resolver", "MatVerse-py/matverse-nexus-pwa",
    "MatVerse-py/matverse-hub", "MatVerse-py/matverse-dataset-governance-pipeline",
    "MatVerse-py/matverse-stack-production", "MatVerse-py/matverse-organism",
    "MatVerse-py/skills", "MatVerse-py/KiloMan", "MatVerse-py/mem-nano-bit",
    "MatVerse-py/symbiOSclauw", "MatVerse-py/Untitled-Document",
    "MatVerse-py/infra-root", "MatVerse-py/matverse-quantum-experiment-data",
    "MatVerse-Hub/SymbiOS", "MatVerse-Hub/Superkernel",
    "MatVerse-Hub/matverse-M-CSQI", "MatVerse-Hub/Prime",
    "MatVerse-Hub/apk-uploader-pro", "MatVerse-Hub/Prim", "MatVerse-Hub/Captals",
    "MatVerse-Hub/DEv", "MatVerse-Hub/twin", "matverse-acoa/mvo-test-results",
    "matverse-acoa/svca-inescapavel", "matverse-acoa/QEX", "matverse-acoa/papers",
    "matverse-acoa/Gate", "matverse-acoa/Cassandra", "matverse-acoa/Atlas",
    "matverse-acoa/Organismo", "matverse-acoa/core", "matverse-acoa/matverse_ouroboros",
    "matverse-acoa/matverse", "matverse-acoa/matverse-v5-sovereign",
    "matverse-acoa/csi-organism-manager", "MatVerse-U/MatVerse-U-OpenBox",
    "MatVerse-U/Symbios", "Symbios-Matverse/matversechain-scan",
    "Symbios-Matverse/matverse-core",
]

@dataclass
class RepoResult:
    repo: str
    query: str
    status: str
    http_status: Optional[int]
    total_count: Optional[int]
    message: str
    ts_utc: str
    rate_remaining: Optional[str] = None
    rate_reset: Optional[str] = None


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_repos(path: Optional[str]) -> list[str]:
    if not path:
        return list(dict.fromkeys(DEFAULT_REPOS))
    repos = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            repos.append(line)
    return list(dict.fromkeys(repos))


def github_search_code(repo: str, token: Optional[str], timeout: int = 20) -> RepoResult:
    query = f"repo:{repo} import"
    url = "https://api.github.com/search/code?" + urllib.parse.urlencode({"q": query, "per_page": 1})
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "matverse-indexer-v2", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace") or "{}")
            total = data.get("total_count")
            status = "SEARCH_OK_RESULTS" if isinstance(total, int) and total > 0 else "SEARCH_OK_NO_RESULTS"
            msg = "GitHub Search respondeu. Não prova sincronização OpenAI/ChatGPT."
            return RepoResult(repo, query, status, resp.status, total, msg, utc_now(), resp.headers.get("x-ratelimit-remaining"), resp.headers.get("x-ratelimit-reset"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            detail = json.loads(raw).get("message", raw[:240])
        except Exception:
            detail = raw[:240]
        if e.code in (401, 403) and not token:
            status, msg = "AUTH_REQUIRED_OR_RATE_LIMITED", "Busca de código exige token ou bateu rate limit. Execute com GH_TOKEN/GITHUB_TOKEN."
        elif e.code == 403:
            status, msg = "FORBIDDEN_OR_RATE_LIMITED", f"GitHub retornou 403: {detail}"
        elif e.code == 404:
            status, msg = "REPO_NOT_FOUND_OR_NO_ACCESS", "Repo não encontrado ou token sem acesso."
        elif e.code == 422:
            status, msg = "QUERY_INVALID_OR_EMPTY_REPO", f"Query inválida, repo vazio ou sem índice pesquisável: {detail}"
        else:
            status, msg = "HTTP_ERROR", f"HTTP {e.code}: {detail}"
        return RepoResult(repo, query, status, e.code, None, msg, utc_now(), e.headers.get("x-ratelimit-remaining"), e.headers.get("x-ratelimit-reset"))
    except Exception as exc:
        return RepoResult(repo, query, "CLIENT_ERROR", None, None, str(exc), utc_now())


def summarize(results: list[RepoResult]) -> dict:
    counts = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    soft_success = counts.get("SEARCH_OK_RESULTS", 0) + counts.get("SEARCH_OK_NO_RESULTS", 0)
    return {"ts_utc": utc_now(), "total": len(results), "soft_success": soft_success, "hard_fail": len(results) - soft_success, "counts": counts, "note": "soft_success não prova sincronização OpenAI. Aguarde 5-10 min e verifique Settings > Apps > GitHub."}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repos-file")
    parser.add_argument("--out", default="indexing_results.json")
    parser.add_argument("--jsonl", default="indexing_results.jsonl")
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    repos = load_repos(args.repos_file)
    print(f"MatVerse Indexer v2 | repos={len(repos)} | token={'yes' if token else 'no'}")
    print("Status honesto: SEARCH_OK_* não é prova de sincronização OpenAI; é gatilho/verificação de GitHub Search.")
    print("-" * 80)

    results = []
    jsonl_path = Path(args.jsonl)
    if jsonl_path.exists():
        jsonl_path.unlink()
    for i, repo in enumerate(repos, 1):
        result = github_search_code(repo, token)
        results.append(result)
        with jsonl_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(result), ensure_ascii=False) + "\n")
        print(f"[{i:03d}/{len(repos):03d}] {repo} -> {result.status} ({result.http_status})")
        print(f"    {result.message}")
        if i < len(repos):
            time.sleep(args.delay)

    output = {"summary": summarize(results), "results": [asdict(r) for r in results]}
    Path(args.out).write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(output["summary"], indent=2, ensure_ascii=False))
    print(f"Saved: {args.out}")
    print(f"Ledger: {args.jsonl}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
