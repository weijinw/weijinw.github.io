# App Collection Website

This repository hosts a GitHub Pages site for a small collection of independent iPhone apps.

## Published routes

- `/` — app collection
- `/support/` — shared support form
- `/fitcycles/` — FitCycles product page
- `/fitcycles/privacy-policy/` — FitCycles privacy policy
- `/speedlens/` — SpeedLens product page
- `/speedlens/privacy-policy/` — SpeedLens privacy policy
- `/alwayson/` — AlwaysOn Desk Clock product page
- `/alwayson/privacy-policy/` — AlwaysOn Desk Clock privacy policy

## Structure

```text
/
├── index.html
├── styles.css
├── 404.html
├── sitemap.xml
├── robots.txt
├── support/
│   ├── index.html
│   ├── styles.css
│   └── support.js
├── shared/
│   └── app-base.css
├── fitcycles/
├── speedlens/
├── alwayson/
└── scripts/
    ├── check_site.py
    └── test_support.js
```

Each app keeps its own HTML, theme stylesheet, assets, and privacy policy. Shared product-page layout and responsive rules live in `shared/app-base.css`.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

## Validate the site

```bash
python3 scripts/check_site.py
node scripts/test_support.js
```

The static validator checks internal links, linked assets, local anchors, CSS imports, page titles, meta descriptions, and image accessibility and sizing attributes. The support-form test checks app selection, subject prefixes, mailto construction, return paths, and form wiring. GitHub Actions runs both checks for pushes to `main` and for pull requests.

## Add another app

1. Create a new app directory with `index.html`, `styles.css`, `assets/`, and `privacy-policy/index.html`.
2. Import `../shared/app-base.css` from the app stylesheet and keep only theme and app-specific rules locally.
3. Add the app to the root `index.html` collection.
4. Add the app to `support/support.js` and the support-page app selector.
5. Add product, support, and privacy links.
6. Add the product and privacy URLs to `sitemap.xml`.
7. Run both validation commands before publishing.
