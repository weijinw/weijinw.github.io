# Heart Baseline Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a review-ready Heart Baseline homepage card, full product page, support integration, and privacy policy.

**Architecture:** Extend the existing dependency-free static site. Reuse `shared/app-base.css` for page structure, keep Heart Baseline theme rules local, and extend the shared support configuration rather than creating a second form.

**Tech Stack:** HTML, CSS, vanilla JavaScript, Python static validation, Node support tests.

## Global Constraints

- Show Heart Baseline as `Coming soon` with no App Store link.
- Keep product claims informational and non-diagnostic.
- Preserve existing responsive and accessible patterns.
- Do not add dependencies or backend services.

---

### Task 1: Homepage and shared support integration

**Files:**
- Modify: `index.html`, `styles.css`, `support/index.html`, `support/support.js`, `scripts/test_support.js`

- [x] Add a Heart Baseline card with product, support, and privacy links.
- [x] Add the `heart-baseline` support option, subject prefix, and return path.
- [x] Extend support tests, run `node scripts/test_support.js`, and confirm they pass.

### Task 2: Product page, assets, and privacy policy

**Files:**
- Create: `heart-baseline/index.html`, `heart-baseline/styles.css`, `heart-baseline/privacy-policy/index.html`
- Create: `heart-baseline/assets/home.jpg`, `daily.jpg`, `history.jpg`, `watch-setup.jpg`

- [x] Copy the supplied screenshots into stable asset filenames.
- [x] Build the dark charcoal/red product page with hero, features, four-image story, support, and privacy links.
- [x] Add an accurate privacy policy covering local storage, Apple Health reads, Watch Connectivity, deletion, and no developer data collection.
- [x] Check mobile and desktop layouts in a local browser.

### Task 3: Site metadata and final validation

**Files:**
- Modify: `README.md`, `sitemap.xml`

- [x] Add the Heart Baseline routes to documentation and the sitemap.
- [x] Run `python3 scripts/check_site.py` and `node scripts/test_support.js`; confirm both pass.
- [x] Inspect the final diff for broken links, inaccurate claims, missing image metadata, and unrelated changes.

### Task 4: Homepage screenshot fan

**Files:**
- Modify: `styles.css`

- [x] Overlap the three Heart Baseline screenshots around a shared center point, with the center screenshot above the side screenshots.
- [x] Rotate the left and right screenshots outward and keep the artwork background transparent.
- [x] Reduce the rotation and overlap at the mobile breakpoint.
- [x] Run the site validators and inspect the card at desktop and mobile widths.
