# Development Promotion Metadata

This directory exists only on the `dev` branch and must never be promoted to `main`.

`promotion.json` is the release checklist for downloadable backgrounds. It records which background/version is being tested and the exact package path that should be promoted when ready.

Recommended statuses:

- `testing` — available to Debug builds, still being evaluated.
- `ready` — approved for production promotion.
- `released` — already promoted to `main`; may be kept temporarily for history.

A production promotion consists of:

1. the candidate's exact `packagePath`, and
2. its matching entry from `alwayson/backgrounds/catalog.json`.

Never merge this `_dev` directory to `main`.
