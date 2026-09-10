# Background Packages

Each downloadable background lives in its own immutable versioned directory:

```text
packages/<background-id>/<version>/
├── manifest.json
├── definition.json
└── assets/
```

Rules:

- `<background-id>` must be the same stable ID used by the catalog, manifest, and definition.
- `<version>` is a positive integer.
- Never overwrite a version that has already been promoted to `main`; create the next version instead.
- `manifest.json` points to the definition and asset URLs for that exact version.
- `definition.json` uses the existing AlwaysOn `ImageBackgroundDefinition` schema.
- Asset logical names referenced by `definition.json` must all be declared by the manifest.
- Keep every production package self-contained so an older installed version can continue to work and be used as fallback.
