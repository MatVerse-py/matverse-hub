# Registry — Part 1: GitHub + Google Drive

## Purpose
This directory is the public index for the first lineage integration between GitHub and Google Drive.

## Operating rule
A source discovered in Drive or GitHub is an input to review. It is not automatically a canonical claim, a validated result, or a release-ready artifact.

## Role separation
- Google Drive: source origin and document archive.
- GitHub: code, tests, workflows, releases, and replay surface.
- MatVerse Hub: public Atlas and sanitized registry surface.

## Observed integration anchors
- `MatVerse-py/matverse-hub`: active public Atlas candidate.
- `MatVerse-py/acoa`: active public research and governance candidate.
- `MatVerse-py/matverse-u-kernel`: active private constitutional-kernel candidate; verification remains pending.
- `MatVerse-py/organismo`: archived historical reference; no new work is assigned to it.

## Required promotion path
1. Export the original source bytes in the private runtime.
2. Compute an immutable artifact hash.
3. Extract claims and invariants.
4. Map each claim to implementation, test, or explicit specification state.
5. Review contradictions and provenance.
6. Record a human governance decision and receipt.
7. Publish only sanitized manifests here.

## Current state
`DRAFT_RECONCILIATION`
