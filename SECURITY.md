# Security Policy

## Credential handling

Never place credentials in commits, issues, pull requests, comments, prompts, notebooks, dashboards, terminal transcripts, generated reports, or repository files.

Use a silent environment variable workflow when running local indexing.

## If a credential was exposed

1. Revoke or rotate it immediately.
2. Remove local references from logs, notebooks, shell history, and generated artifacts.
3. Create a new credential with minimum required scope.
4. Re-run the workflow without printing the credential.
5. Record the incident as BLOCK_SECURITY.

## MatVerse decision semantics

PASS: workflow executed and generated evidence without secrets.

WARN: rate limit, private repository, or insufficient permission.

BLOCK_LAB: repository missing, no access, or invisible after retest.

BLOCK_SECURITY: exposed credential, unsafe log, or artifact containing secret material.

DROP_NEGATIVE: useful failure recorded as negative memory.
