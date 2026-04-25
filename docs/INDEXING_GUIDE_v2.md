# MatVerse GitHub Indexing Guide v2

## Objective

Run GitHub Code Search checks for the MatVerse repositories using the query pattern `repo:OWNER/REPO import`.

## Validation chain

GitHub Search response -> wait 5 to 10 minutes -> GitHub App access check -> ChatGPT visibility check.

## Outputs

- indexing_results.json
- indexing_results.jsonl
- indexing_dashboard.html

## Status semantics

- SEARCH_OK_RESULTS: GitHub Search returned results.
- SEARCH_OK_NO_RESULTS: GitHub Search responded without matches.
- AUTH_REQUIRED_OR_RATE_LIMITED: authorization missing or API limit reached.
- FORBIDDEN_OR_RATE_LIMITED: permission problem or API limit.
- REPO_NOT_FOUND_OR_NO_ACCESS: repository missing or inaccessible.
- QUERY_INVALID_OR_EMPTY_REPO: invalid query, empty repo, or not searchable.
- HTTP_ERROR: generic HTTP error.
- CLIENT_ERROR: local or network error.

## Security rule

Do not place credentials in commands, commits, issues, pull requests, logs, notebooks, dashboards, or generated artifacts. If a credential was exposed, rotate it before any new test.

## MatVerse decisions

PASS: search response and evidence generated without secrets.
WARN: private repo, rate limit, or insufficient permission.
BLOCK_LAB: repo missing, no access, or still invisible after retest.
BLOCK_SECURITY: exposed credential or unsafe log.
DROP_NEGATIVE: useful failure recorded as negative memory.
