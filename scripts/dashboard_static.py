#!/usr/bin/env python3
"""
Generate a static low-resource HTML dashboard from indexing_results.json.
No Dash, no pandas, no browser framework.
"""

from __future__ import annotations

from collections import Counter
import html
import json
from pathlib import Path

INFILE = Path("indexing_results.json")
OUTFILE = Path("indexing_dashboard.html")


def badge(status: str) -> str:
    if status.startswith("SEARCH_OK"):
        cls = "ok"
    elif "RATE" in status or "AUTH" in status or "FORBIDDEN" in status:
        cls = "warn"
    else:
        cls = "bad"
    return f'<span class="badge {cls}">{html.escape(status)}</span>'


def main() -> int:
    if not INFILE.exists():
        raise SystemExit("indexing_results.json não encontrado. Rode scripts/index-repos-v2.py primeiro.")

    data = json.loads(INFILE.read_text(encoding="utf-8"))
    results = data.get("results", [])
    summary = data.get("summary", {})
    counts = Counter(r.get("status", "UNKNOWN") for r in results)

    rows = []
    for r in results:
        rows.append(
            "<tr>"
            f"<td>{html.escape(r.get('repo', ''))}</td>"
            f"<td>{badge(r.get('status', 'UNKNOWN'))}</td>"
            f"<td>{html.escape(str(r.get('http_status', '')))}</td>"
            f"<td>{html.escape(str(r.get('total_count', '')))}</td>"
            f"<td>{html.escape(r.get('message', ''))}</td>"
            "</tr>"
        )

    count_items = "".join(f"<li>{html.escape(k)}: {v}</li>" for k, v in sorted(counts.items()))

    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>MatVerse Indexing Dashboard</title>
<style>
body {{ background:#05070A; color:#E5E7EB; font-family: Inter, system-ui, sans-serif; margin:32px; }}
code, table {{ font-family:'JetBrains Mono','IBM Plex Mono',monospace; }}
.panel {{ background:#0D1117; border:1px solid #1F2937; border-radius:14px; padding:20px; margin:16px 0; }}
h1 {{ color:#22D3EE; }}
.muted {{ color:#94A3B8; }}
.badge {{ padding:4px 8px; border-radius:999px; font-size:12px; }}
.ok {{ background:#052e16; color:#22C55E; }}
.warn {{ background:#451a03; color:#F59E0B; }}
.bad {{ background:#450a0a; color:#EF4444; }}
table {{ width:100%; border-collapse:collapse; margin-top:16px; font-size:13px; }}
td, th {{ border-bottom:1px solid #1F2937; padding:10px; text-align:left; vertical-align:top; }}
</style>
</head>
<body>
<h1>MatVerse Repository Indexing Dashboard</h1>
<p class="muted">Dashboard estático gerado localmente. Não prova sincronização OpenAI; mostra respostas da GitHub Search API.</p>
<div class="panel">
<h2>Resumo</h2>
<pre>{html.escape(json.dumps(summary, indent=2, ensure_ascii=False))}</pre>
<ul>{count_items}</ul>
</div>
<div class="panel">
<h2>Resultados</h2>
<table>
<thead><tr><th>Repo</th><th>Status</th><th>HTTP</th><th>Total</th><th>Mensagem</th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
</div>
</body>
</html>
"""
    OUTFILE.write_text(doc, encoding="utf-8")
    print(f"Dashboard salvo em: {OUTFILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
