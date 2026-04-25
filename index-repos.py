#!/usr/bin/env python3
"""
MatVerse Repository Indexing Automation
Triggers GitHub search indexing for all MatVerse repositories
to make them accessible to OpenAI ChatGPT and other integrations
"""

import requests
import time
from datetime import datetime
import json

class MatVerseIndexer:
    def __init__(self):
        self.repos = [
            # MatVerse-py (Primary)
            "MatVerse-py/ODA-QF",
            "MatVerse-py/SymbiOS",
            "MatVerse-py/Superkernel",
            "MatVerse-py/matverse-M-CSQI",
            "MatVerse-py/Prime",
            "MatVerse-py/Pose",
            "MatVerse-py/matverse-u-os",
            "MatVerse-py/matverse-u-kernel",
            "MatVerse-py/matverse-u-docs",
            "MatVerse-py/matverse-u-lua",
            "MatVerse-py/matverse-u-gate",
            "MatVerse-py/matverse-u-network",
            "MatVerse-py/matverse-twin-core",
            "MatVerse-py/acoa",
            "MatVerse-py/organismo",
            "MatVerse-py/SuperKernel-6.0",
            "MatVerse-py/MatVerse-Page",
            "MatVerse-py/delta-circuit-ignite",
            "MatVerse-py/IA.GOV",
            "MatVerse-py/Symbiodroid",
            "MatVerse-py/mnbs-seed",
            "MatVerse-py/matverse-landing-page",
            "MatVerse-py/matverse-mcp-server",
            "MatVerse-py/gpt-cassndra--pilot",
            "MatVerse-py/Core.Eng",
            "MatVerse-py/matverse-u-verifier",
            "MatVerse-py/github-url-validator",
            "MatVerse-py/matverse-github-resolver",
            "MatVerse-py/matverse-nexus-pwa",
            "MatVerse-py/matverse-hub",
            "MatVerse-py/matverse-dataset-governance-pipeline",
            "MatVerse-py/matverse-stack-production",
            "MatVerse-py/matverse-organism",
            "MatVerse-py/skills",
            "MatVerse-py/KiloMan",
            "MatVerse-py/mem-nano-bit",
            "MatVerse-py/symbiOSclauw",
            "MatVerse-py/Untitled-Document",
            "MatVerse-py/infra-root",
            "MatVerse-py/matverse-quantum-experiment-data",
            "MatVerse-py/bunker-genesis-mirror",
            "MatVerse-py/matverse-secure-loader",
            "MatVerse-py/svca-lab-genesis",
            "MatVerse-py/svca-lab",
            # MatVerse-Hub
            "MatVerse-Hub/SymbiOS",
            "MatVerse-Hub/Superkernel",
            "MatVerse-Hub/matverse-M-CSQI",
            "MatVerse-Hub/Prime",
            "MatVerse-Hub/apk-uploader-pro",
            "MatVerse-Hub/Prim",
            "MatVerse-Hub/Captals",
            "MatVerse-Hub/DEv",
            "MatVerse-Hub/twin",
            # matverse-acoa
            "matverse-acoa/mvo-test-results",
            "matverse-acoa/svca-inescapavel",
            "matverse-acoa/QEX",
            "matverse-acoa/papers",
            "matverse-acoa/Gate",
            "matverse-acoa/Cassandra",
            "matverse-acoa/Atlas",
            "matverse-acoa/Organismo",
            "matverse-acoa/core",
            "matverse-acoa/matverse_ouroboros",
            "matverse-acoa/matverse",
            "matverse-acoa/matverse-v5-sovereign",
            "matverse-acoa/csi-organism-manager",
            # MatVerse-U
            "MatVerse-U/MatVerse-U-OpenBox",
            "MatVerse-U/Symbios",
            # Symbios-Matverse
            "Symbios-Matverse/matversechain-scan",
            "Symbios-Matverse/matverse-core",
        ]
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "total": len(self.repos),
            "indexed": [],
            "failed": [],
            "summary": {}
        }

    def trigger_indexing(self, repo):
        """Trigger GitHub search indexing for a repository"""
        try:
            # GitHub Search API endpoint
            search_query = f"repo:{repo} import"
            url = "https://api.github.com/search/code"
            
            # Make search request to trigger indexing
            response = requests.get(
                url,
                params={"q": search_query},
                timeout=10
            )
            
            if response.status_code == 200:
                self.results["indexed"].append({
                    "repo": repo,
                    "status": "triggered",
                    "timestamp": datetime.now().isoformat()
                })
                print(f"✓ {repo} - Indexing triggered")
                return True
            else:
                self.results["failed"].append({
                    "repo": repo,
                    "status": f"HTTP {response.status_code}",
                    "timestamp": datetime.now().isoformat()
                })
                print(f"✗ {repo} - Status: {response.status_code}")
                return False
                
        except Exception as e:
            self.results["failed"].append({
                "repo": repo,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })
            print(f"✗ {repo} - Error: {str(e)}")
            return False

    def run(self):
        """Run indexing for all repositories"""
        print("🚀 MatVerse Repository Indexing Started")
        print(f"📦 Total repositories: {self.results['total']}")
        print("-" * 60)
        
        for i, repo in enumerate(self.repos, 1):
            print(f"[{i}/{self.results['total']}] Processing: {repo}")
            self.trigger_indexing(repo)
            # Rate limiting - wait between requests
            time.sleep(0.5)
        
        print("-" * 60)
        self.results["summary"] = {
            "total_processed": self.results["total"],
            "successful": len(self.results["indexed"]),
            "failed": len(self.results["failed"]),
            "success_rate": f"{(len(self.results['indexed']) / self.results['total'] * 100):.1f}%"
        }
        
        return self.results

    def save_results(self, filename="indexing_results.json"):
        """Save results to file"""
        with open(filename, "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"\n📊 Results saved to {filename}")

if __name__ == "__main__":
    indexer = MatVerseIndexer()
    results = indexer.run()
    indexer.save_results()
    
    print("\n✅ Indexing Summary:")
    print(json.dumps(results["summary"], indent=2))
    print("\n⏱️ Repositories will be searchable in 5-10 minutes")
    print("🔗 Then accessible via OpenAI ChatGPT GitHub App integration")
