# AlwaysOn Support Site

Static support and privacy website for AlwaysOn Desk Clock.

## Validate

From the repository root:

```bash
python3 support/validate_site.py
```

Expected output:

```text
support site validation passed
```

## Preview locally

From the repository root:

```bash
python3 -m http.server 8000 --directory support
```

Open:

- `http://localhost:8000/`
- `http://localhost:8000/privacy-policy/`

The site uses relative links so the same files work from the local server and from the GitHub Pages project path.

## Deploy

Changes under `support/**` trigger `.github/workflows/pages.yml` on `main`. The workflow validates the site, uploads `support/` as the Pages artifact, and deploys that artifact as the website root.
