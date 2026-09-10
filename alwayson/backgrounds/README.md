# AlwaysOn Downloadable Backgrounds

This directory is the static content source for AlwaysOn downloadable image backgrounds.

## Catalog URLs

- Debug app build: `https://raw.githubusercontent.com/weijinw/weijinw.github.io/dev/alwayson/backgrounds/catalog.json`
- Release app build: `https://weijinw.github.io/alwayson/backgrounds/catalog.json`

The `dev` branch is the staging/release-candidate source. The `main` branch is production and is published by GitHub Pages. If `dev` is deleted after a merge, recreate it from the current `main` before starting the next background release cycle.

Catalog and package metadata use relative resource URLs, so the same metadata files work unchanged on both branches.

## Layout

```text
alwayson/backgrounds/
├── catalog.json
└── packages/
    └── <background-id>/
        └── <version>/
            ├── manifest.json
            ├── definition.json
            └── assets/
```

Each package version is immutable after it has been promoted to production. To update a background, create a new numeric version directory and update `catalog.json` to reference the new manifest.

Catalog entries may include a `category` string such as `Ambient`, `Nature`, `Abstract`, or `Places`. The app uses this metadata to group remote backgrounds in the Background Gallery. Keep category names short and reuse existing names when possible.

## Development workflow

1. Start `dev` from the current `main` branch.
2. Add or update backgrounds under `packages/<background-id>/<version>/` on `dev` and update `catalog.json` as needed.
3. Test the complete `dev` catalog with an AlwaysOn Debug build.
4. Keep only production-ready downloadable-background changes on `dev`. Use separate feature branches for experiments that are not intended for the next release.
5. Before promotion, review the full `dev → main` diff and verify that catalog, manifest, definition, and asset references resolve correctly.
6. Merge `dev` directly into `main` without rewriting metadata URLs or selectively copying package/catalog files.

No separate promotion metadata is required under `alwayson/backgrounds/`.

## Production promotion

Promotion is branch-level: the reviewed `dev` state is merged directly into `main`.

- Treat the entire downloadable-background diff on `dev` as the release candidate.
- Do not keep experimental backgrounds on `dev` if they are not ready to publish.
- Keep catalog and manifest resource URLs relative so metadata remains branch-neutral.
- Do not rewrite URLs during promotion.
- After the merge, `main` is the production source consumed by Release builds.
