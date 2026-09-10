# AlwaysOn Downloadable Backgrounds

This directory is the static content source for AlwaysOn downloadable image backgrounds.

## Catalog URLs

- Debug app build: `https://raw.githubusercontent.com/weijinw/weijinw.github.io/dev/alwayson/backgrounds/catalog.json`
- Release app build: `https://weijinw.github.io/alwayson/backgrounds/catalog.json`

The `dev` branch is the staging source. The `main` branch is production and is published by GitHub Pages.

## Layout

```text
alwayson/backgrounds/
├── catalog.json
├── packages/
│   └── <background-id>/
│       └── <version>/
│           ├── manifest.json
│           ├── definition.json
│           └── assets/
└── _dev/
    ├── README.md
    └── promotion.json
```

Each package version is immutable after it has been promoted to production. To update a background, create a new numeric version directory and update `catalog.json` to reference the new manifest.

Catalog entries may include a `category` string such as `Ambient`, `Nature`, `Abstract`, or `Places`. The app uses this metadata to group remote backgrounds in the Background Gallery. Keep category names short and reuse existing names when possible.

## Development workflow

1. Add or update a background under `packages/<background-id>/<version>/` on `dev`.
2. Add/update the corresponding entry in the `dev` `catalog.json`.
3. Add the candidate to `_dev/promotion.json` with status `testing`.
4. Test with an AlwaysOn Debug build.
5. Change the candidate status to `ready` after device testing is complete.
6. Promote only that package folder and its matching catalog entry to `main`.

Do not merge `_dev/` into `main`.

## Production promotion

For a candidate marked `ready` in `_dev/promotion.json`:

- Promote the exact `packagePath` listed for the candidate.
- Copy the matching background entry from the `dev` catalog into the `main` catalog.
- Do not promote other package folders or other `dev` catalog entries.
- Do not promote `_dev/`.

This keeps several experimental backgrounds on `dev` without accidentally publishing all of them to production.
