#!/usr/bin/env bash
set -euo pipefail

TAG="v0.1.1-alpha"
TARGET="main"
TITLE="MatVerse Hub v0.1.1-alpha — Scientific Governance & Public Witness Layer"
NOTES_FILE="RELEASE_NOTES_v0.1.1-alpha.md"
ASSET_FILE="MATVERSE_sober_clean_release_v0_1_1_alpha.zip"
REPO="MatVerse-py/matverse-hub"
PRERELEASE=true

if [[ "${1:-}" == "--help" ]]; then
  cat <<USAGE
Uso:
  GITHUB_TOKEN=... ./scripts/publish_release_v0.1.1-alpha.sh [--asset path/to/asset.zip]

Descrição:
  Publica o pre-release ${TAG} via API do GitHub sem depender de gh CLI.
  - Cria tag/release em ${TARGET}
  - Usa o conteúdo de ${NOTES_FILE} como body
  - Anexa asset opcional
USAGE
  exit 0
fi

if [[ -n "${1:-}" && "${1:-}" == "--asset" ]]; then
  ASSET_FILE="${2:-}"
fi

if [[ ! -f "$NOTES_FILE" ]]; then
  echo "ERRO: não encontrei $NOTES_FILE" >&2
  exit 1
fi

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "ERRO: defina GITHUB_TOKEN para publicar release via API." >&2
  exit 2
fi

BODY_JSON=$(python3 - <<'PY'
import json, pathlib
notes = pathlib.Path('RELEASE_NOTES_v0.1.1-alpha.md').read_text(encoding='utf-8')
payload = {
  'tag_name': 'v0.1.1-alpha',
  'target_commitish': 'main',
  'name': 'MatVerse Hub v0.1.1-alpha — Scientific Governance & Public Witness Layer',
  'body': notes,
  'prerelease': True,
  'draft': False,
}
print(json.dumps(payload))
PY
)

API="https://api.github.com/repos/${REPO}"

echo "Criando/atualizando release ${TAG} em ${REPO}..."
RESP_FILE=$(mktemp)
HTTP_CODE=$(curl -sS -o "$RESP_FILE" -w '%{http_code}' \
  -X POST "${API}/releases" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -d "$BODY_JSON")

if [[ "$HTTP_CODE" == "422" ]]; then
  echo "Release/tag já existe. Buscando release existente para upload de asset..."
  RELEASE_JSON=$(curl -sS \
    -H "Authorization: Bearer ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "${API}/releases/tags/${TAG}")
else
  RELEASE_JSON=$(cat "$RESP_FILE")
fi

UPLOAD_URL=$(printf '%s' "$RELEASE_JSON" | python3 - <<'PY'
import json,sys
obj=json.load(sys.stdin)
url=obj.get('upload_url','').split('{')[0]
print(url)
PY
)
HTML_URL=$(printf '%s' "$RELEASE_JSON" | python3 - <<'PY'
import json,sys
obj=json.load(sys.stdin)
print(obj.get('html_url',''))
PY
)

if [[ -z "$UPLOAD_URL" ]]; then
  echo "ERRO: não consegui resolver upload_url. Resposta:" >&2
  cat "$RESP_FILE" >&2 || true
  exit 3
fi

if [[ -f "$ASSET_FILE" ]]; then
  ASSET_NAME=$(basename "$ASSET_FILE")
  echo "Enviando asset: $ASSET_NAME"
  curl -sS -X POST "${UPLOAD_URL}?name=${ASSET_NAME}" \
    -H "Authorization: Bearer ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github+json" \
    -H "Content-Type: application/zip" \
    --data-binary @"$ASSET_FILE" >/dev/null
else
  echo "Asset opcional não encontrado: $ASSET_FILE (seguindo sem anexar)."
fi

echo "Concluído. Release: ${HTML_URL:-https://github.com/${REPO}/releases/tag/${TAG}}"
