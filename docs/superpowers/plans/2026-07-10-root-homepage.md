# Root Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a polished, lightweight editorial homepage at the GitHub Pages repository root that fixes the root 404 and presents SpeedLens and AlwaysOn Desk Clock without changing either existing app site.

**Architecture:** Create a root-only `index.html` and root-only `styles.css`. The HTML uses semantic header, hero, app showcase, repeated app-card articles, and footer structures; CSS owns the neutral editorial visual system, per-card accent variables, responsive layouts, focus states, and reduced-motion behavior. Existing `speedlens/` and `alwayson/` files remain untouched and are referenced only through relative links and existing artwork paths.

**Tech Stack:** HTML5, CSS3, GitHub Pages, Chromium headless validation, Python 3 standard library for static link/content checks.

## Global Constraints

- Use plain semantic HTML and CSS; no JavaScript or dependencies.
- Preserve `./speedlens/` and `./alwayson/` and do not modify their existing HTML, CSS, privacy pages, or assets.
- Do not use a personal name, studio name, company name, logo, or invented umbrella brand.
- Hero heading must be exactly `Small apps. Thoughtfully made.`
- Use only relative URLs for internal navigation and assets.
- SpeedLens App Store URL must be exactly `https://apps.apple.com/us/app/speedlens/id6787802030`.
- AlwaysOn Desk Clock must not have an App Store link.
- Meet WCAG AA contrast requirements, provide visible keyboard focus styles, descriptive alt text, and respect `prefers-reduced-motion`.
- Do not add gradients, glassmorphism, floating decorative shapes, stock imagery, fake device mockups, or elaborate animation.
- Omit a custom favicon rather than inventing a neutral brand mark or reusing either app's identity; suppress a broken browser favicon request with a blank data-URL icon.

---

### Task 1: Build the root editorial homepage

**Files:**
- Create: `index.html`
- Create: `styles.css`
- Preserve: `speedlens/**`
- Preserve: `alwayson/**`

**Interfaces:**
- Consumes: existing artwork at `./speedlens/assets/hero-capture.png` and `./alwayson/assets/app-preview.png`; existing product and privacy routes under `./speedlens/` and `./alwayson/`.
- Produces: a root GitHub Pages entry point at `./index.html` and an isolated root stylesheet at `./styles.css`.

- [ ] **Step 1: Verify the root entry point is still missing before implementation**

Run:

```bash
test ! -f index.html && printf 'PASS: root index.html is absent before implementation\n'
```

Expected:

```text
PASS: root index.html is absent before implementation
```

- [ ] **Step 2: Create the semantic root homepage**

Create `index.html` with exactly this content:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A curated collection of focused iPhone apps designed for everyday use, including SpeedLens and AlwaysOn Desk Clock.">
  <meta property="og:title" content="Small apps. Thoughtfully made.">
  <meta property="og:description" content="Focused iPhone apps designed for everyday use.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://weijinw.github.io/">
  <meta name="theme-color" content="#f5f3ee">
  <title>Small apps. Thoughtfully made.</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="./styles.css">
</head>
<body>
  <header class="site-header">
    <nav class="header-nav shell" aria-label="Primary navigation">
      <a href="#apps">Apps</a>
      <a href="mailto:welkin.wong@gmail.com">Support</a>
    </nav>
  </header>

  <main>
    <section class="hero shell" aria-labelledby="hero-title">
      <div class="hero-copy">
        <p class="eyebrow">Focused apps for everyday use</p>
        <h1 id="hero-title">Small apps. Thoughtfully made.</h1>
        <p class="hero-lede">A small collection of focused apps designed to be useful in everyday moments, with clear purpose and attention to how they feel in use.</p>
      </div>
    </section>

    <section class="apps shell" id="apps" aria-labelledby="apps-title">
      <div class="section-heading">
        <p class="eyebrow">Apps</p>
        <h2 id="apps-title">Useful tools, each with a focused job.</h2>
      </div>

      <div class="app-list">
        <article class="app-card app-card-speedlens">
          <div class="app-copy">
            <p class="app-status"><span class="status-dot" aria-hidden="true"></span>Available on the App Store</p>
            <h3>SpeedLens</h3>
            <p class="app-description">A focused iPhone camera for recording sports video and reviewing clips on-device.</p>
            <div class="app-actions" aria-label="SpeedLens links">
              <a class="button button-primary" href="https://apps.apple.com/us/app/speedlens/id6787802030" target="_blank" rel="noopener noreferrer">Download on the App Store <span aria-hidden="true">↗</span><span class="visually-hidden"> (opens in a new tab)</span></a>
              <a class="text-link" href="./speedlens/">Product page</a>
              <a class="text-link" href="./speedlens/privacy-policy/">Privacy</a>
            </div>
          </div>
          <figure class="app-artwork">
            <img src="./speedlens/assets/hero-capture.png" alt="SpeedLens capture interface showing camera controls and a tracked skateboarder.">
          </figure>
        </article>

        <article class="app-card app-card-alwayson app-card-reverse">
          <div class="app-copy">
            <p class="app-status app-status-soon">Coming soon</p>
            <h3>AlwaysOn Desk Clock</h3>
            <p class="app-description">Turns an iPhone into a calm, customizable desk display for time, calendar, weather, and upcoming events.</p>
            <div class="app-actions" aria-label="AlwaysOn Desk Clock links">
              <a class="text-link" href="./alwayson/">Product page</a>
              <a class="text-link" href="./alwayson/privacy-policy/">Privacy</a>
            </div>
          </div>
          <figure class="app-artwork">
            <img src="./alwayson/assets/app-preview.png" alt="AlwaysOn Desk Clock showing time, weather, calendar, and upcoming events on a landscape iPhone display.">
          </figure>
        </article>
      </div>
    </section>
  </main>

  <footer class="site-footer shell">
    <nav class="footer-links" aria-label="App and support links">
      <a href="./speedlens/">SpeedLens</a>
      <a href="./speedlens/privacy-policy/">SpeedLens privacy</a>
      <a href="./alwayson/">AlwaysOn Desk Clock</a>
      <a href="./alwayson/privacy-policy/">AlwaysOn privacy</a>
      <a href="mailto:welkin.wong@gmail.com">Support</a>
    </nav>
  </footer>
</body>
</html>
```

- [ ] **Step 3: Create the isolated editorial stylesheet**

Create `styles.css` with exactly this content:

```css
:root {
  color-scheme: light;
  --bg: #f5f3ee;
  --surface: #fbfaf7;
  --text: #1f201b;
  --muted: #5f6158;
  --line: rgba(31, 32, 27, 0.13);
  --line-strong: rgba(31, 32, 27, 0.22);
  --max-width: 1180px;
  --radius-large: 30px;
  --radius-medium: 18px;
  --shadow: 0 22px 60px rgba(41, 38, 29, 0.08);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", sans-serif;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  min-width: 320px;
  margin: 0;
  color: var(--text);
  background: var(--bg);
  font-size: 16px;
  line-height: 1.6;
}

a {
  color: inherit;
}

img {
  display: block;
  max-width: 100%;
}

.shell {
  width: min(calc(100% - 48px), var(--max-width));
  margin-inline: auto;
}

.site-header {
  border-bottom: 1px solid var(--line);
}

.header-nav {
  display: flex;
  min-height: 64px;
  align-items: center;
  justify-content: flex-end;
  gap: 28px;
  font-size: 0.92rem;
  font-weight: 620;
}

.header-nav a,
.footer-links a,
.text-link {
  text-decoration-color: transparent;
  text-underline-offset: 0.3em;
  transition: color 160ms ease, text-decoration-color 160ms ease;
}

.header-nav a:hover,
.footer-links a:hover,
.text-link:hover {
  text-decoration-color: currentColor;
}

:focus-visible {
  outline: 2px solid #5550b8;
  outline-offset: 4px;
  border-radius: 5px;
}

.hero {
  display: flex;
  min-height: 360px;
  align-items: center;
  padding-block: 72px 76px;
}

.hero-copy {
  max-width: 760px;
}

.eyebrow {
  margin: 0 0 16px;
  color: var(--muted);
  font-size: 0.76rem;
  font-weight: 720;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

h1,
h2,
h3,
p {
  margin-top: 0;
}

h1,
h2,
h3 {
  letter-spacing: -0.045em;
  line-height: 1.02;
}

h1 {
  max-width: 10ch;
  margin-bottom: 24px;
  font-size: clamp(2.65rem, 5.2vw, 4.25rem);
  font-weight: 650;
}

h2 {
  max-width: 14ch;
  margin-bottom: 0;
  font-size: clamp(2rem, 3.5vw, 3.25rem);
  font-weight: 620;
}

h3 {
  margin-bottom: 18px;
  font-size: clamp(2.25rem, 4vw, 4rem);
  font-weight: 640;
}

.hero-lede {
  max-width: 640px;
  margin-bottom: 0;
  color: var(--muted);
  font-size: clamp(1.05rem, 1.45vw, 1.22rem);
}

.apps {
  padding-block: 20px 96px;
}

.section-heading {
  margin-bottom: 34px;
}

.app-list {
  display: grid;
  gap: 28px;
}

.app-card {
  --accent: #086c82;
  --accent-soft: #e8f4f5;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  grid-template-areas: "copy artwork";
  min-height: 470px;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: var(--radius-large);
  background: var(--surface);
  box-shadow: var(--shadow);
  transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
}

.app-card:hover {
  transform: translateY(-3px);
  border-color: var(--line-strong);
  box-shadow: 0 26px 70px rgba(41, 38, 29, 0.1);
}

.app-card-alwayson {
  --accent: #5550b8;
  --accent-soft: #eeedf9;
}

.app-card-reverse {
  grid-template-areas: "artwork copy";
}

.app-copy {
  grid-area: copy;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  padding: clamp(36px, 5vw, 62px);
}

.app-status {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  margin-bottom: 28px;
  color: var(--accent);
  font-size: 0.79rem;
  font-weight: 720;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
}

.app-status-soon {
  padding: 7px 11px;
  border: 1px solid var(--line);
  border-radius: 999px;
  color: var(--muted);
  background: transparent;
  letter-spacing: 0.05em;
}

.app-description {
  max-width: 41ch;
  margin-bottom: 30px;
  color: #52544d;
  font-size: clamp(1.02rem, 1.25vw, 1.14rem);
}

.app-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px 20px;
}

.button {
  display: inline-flex;
  min-height: 48px;
  align-items: center;
  justify-content: center;
  gap: 7px;
  padding: 0 19px;
  border: 1px solid var(--accent);
  border-radius: 999px;
  font-weight: 680;
  text-decoration: none;
  transition: transform 160ms ease, background 160ms ease, border-color 160ms ease;
}

.button:hover {
  transform: translateY(-2px);
}

.button-primary {
  color: #fff;
  background: var(--accent);
}

.text-link {
  color: var(--text);
  font-weight: 650;
}

.app-artwork {
  grid-area: artwork;
  display: flex;
  min-width: 0;
  min-height: 100%;
  align-items: center;
  justify-content: center;
  margin: 0;
  padding: clamp(22px, 3.5vw, 44px);
  background: var(--accent-soft);
}

.app-artwork img {
  width: 100%;
  max-height: 390px;
  object-fit: contain;
  border: 1px solid rgba(31, 32, 27, 0.1);
  border-radius: var(--radius-medium);
  box-shadow: 0 18px 44px rgba(31, 32, 27, 0.13);
}

.site-footer {
  padding-block: 30px 42px;
  border-top: 1px solid var(--line);
}

.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 12px 24px;
  color: var(--muted);
  font-size: 0.88rem;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

@media (max-width: 820px) {
  .shell {
    width: min(calc(100% - 40px), var(--max-width));
  }

  .hero {
    min-height: 330px;
    padding-block: 58px 64px;
  }

  .apps {
    padding-bottom: 72px;
  }

  .app-card,
  .app-card-reverse {
    grid-template-columns: 1fr;
    grid-template-areas:
      "artwork"
      "copy";
    min-height: 0;
  }

  .app-artwork {
    min-height: 340px;
  }

  .app-artwork img {
    max-height: 320px;
  }
}

@media (max-width: 560px) {
  .shell {
    width: min(calc(100% - 32px), var(--max-width));
  }

  .header-nav {
    min-height: 58px;
    gap: 22px;
  }

  .hero {
    min-height: 0;
    padding-block: 54px 58px;
  }

  h1 {
    font-size: clamp(2.6rem, 13vw, 3.15rem);
  }

  h2 {
    font-size: clamp(2rem, 10vw, 2.7rem);
  }

  h3 {
    font-size: clamp(2.15rem, 11vw, 3rem);
  }

  .apps {
    padding-top: 10px;
    padding-bottom: 56px;
  }

  .section-heading {
    margin-bottom: 24px;
  }

  .app-list {
    gap: 20px;
  }

  .app-card {
    border-radius: 24px;
  }

  .app-artwork {
    min-height: 250px;
    padding: 20px;
  }

  .app-artwork img {
    max-height: 260px;
    border-radius: 14px;
  }

  .app-copy {
    padding: 30px 24px 34px;
  }

  .app-status {
    margin-bottom: 22px;
  }

  .app-description {
    margin-bottom: 26px;
  }

  .app-actions {
    align-items: flex-start;
  }

  .button {
    width: 100%;
  }

  .site-footer {
    padding-block: 24px 34px;
  }

  .footer-links {
    flex-direction: column;
    align-items: flex-start;
    gap: 9px;
  }
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }

  .app-card,
  .button,
  .header-nav a,
  .footer-links a,
  .text-link {
    transition: none;
  }

  .app-card:hover,
  .button:hover {
    transform: none;
  }
}
```

- [ ] **Step 4: Run static content and route-reference checks**

Run:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

html = Path('index.html').read_text()
css = Path('styles.css').read_text()

assert 'Small apps. Thoughtfully made.' in html
assert './speedlens/' in html
assert './speedlens/privacy-policy/' in html
assert './alwayson/' in html
assert './alwayson/privacy-policy/' in html
assert 'https://apps.apple.com/us/app/speedlens/id6787802030' in html
assert html.count('apps.apple.com') == 1
assert 'Download on the App Store' in html
assert 'prefers-reduced-motion' in css
assert ':focus-visible' in css
assert 'linear-gradient' not in css
assert 'radial-gradient' not in css

for path in [
    Path('speedlens/index.html'),
    Path('speedlens/privacy-policy/index.html'),
    Path('alwayson/index.html'),
    Path('alwayson/privacy-policy/index.html'),
    Path('speedlens/assets/hero-capture.png'),
    Path('alwayson/assets/app-preview.png'),
]:
    assert path.exists(), path

class Parser(HTMLParser):
    pass
Parser().feed(html)
print('PASS: static homepage checks')
PY
```

Expected:

```text
PASS: static homepage checks
```

- [ ] **Step 5: Commit the root homepage implementation**

Run:

```bash
git add index.html styles.css
git commit -m "Add editorial app collection homepage"
```

Expected: one commit containing only the two new root homepage files.

---

### Task 2: Validate routes, responsive layouts, and accessibility behavior

**Files:**
- Validate: `index.html`
- Validate: `styles.css`
- Validate only: `speedlens/**`
- Validate only: `alwayson/**`

**Interfaces:**
- Consumes: the root static homepage from Task 1.
- Produces: verification evidence that the root entry point loads, internal links resolve, the App Store URL is exact, AlwaysOn has no App Store CTA, and the layout behaves correctly at 375px, 768px, and 1440px.

- [ ] **Step 1: Start a local static server and confirm all internal routes return HTTP 200**

Run in the repository root:

```bash
python3 -m http.server 8000 >/tmp/weijinw-homepage-http.log 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID"' EXIT
sleep 1
for path in / /speedlens/ /speedlens/privacy-policy/ /alwayson/ /alwayson/privacy-policy/; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "http://127.0.0.1:8000${path}")
  printf '%s %s\n' "$code" "$path"
  test "$code" = "200"
done
```

Expected:

```text
200 /
200 /speedlens/
200 /speedlens/privacy-policy/
200 /alwayson/
200 /alwayson/privacy-policy/
```

- [ ] **Step 2: Verify the published SpeedLens App Store URL resolves**

Run:

```bash
curl -sSIL --max-time 20 'https://apps.apple.com/us/app/speedlens/id6787802030' | head -n 1
```

Expected: an HTTP success or redirect status from Apple, not a DNS, timeout, or 404 failure.

- [ ] **Step 3: Capture desktop, tablet, and mobile layouts with Chromium**

With the local server still running, run:

```bash
chromium --headless --disable-gpu --hide-scrollbars --run-all-compositor-stages-before-draw --screenshot=/tmp/home-375.png --window-size=375,1200 http://127.0.0.1:8000/
chromium --headless --disable-gpu --hide-scrollbars --run-all-compositor-stages-before-draw --screenshot=/tmp/home-768.png --window-size=768,1200 http://127.0.0.1:8000/
chromium --headless --disable-gpu --hide-scrollbars --run-all-compositor-stages-before-draw --screenshot=/tmp/home-1440.png --window-size=1440,1200 http://127.0.0.1:8000/
file /tmp/home-375.png /tmp/home-768.png /tmp/home-1440.png
```

Expected: three valid PNG screenshots.

Inspect the screenshots and verify:

- 375px: no horizontal overflow; each card shows artwork first; actions wrap; the App Store CTA is touch-sized and full width.
- 768px: cards are stacked artwork/copy compositions with balanced spacing.
- 1440px: cards are two-column compositions; SpeedLens is copy-left/artwork-right; AlwaysOn is artwork-left/copy-right; artwork occupies approximately half the card.

- [ ] **Step 4: Verify keyboard focus and reduced-motion CSS behavior statically**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
css = Path('styles.css').read_text()
assert ':focus-visible' in css
assert 'outline: 2px solid #5550b8;' in css
assert '@media (prefers-reduced-motion: reduce)' in css
assert '.app-card:hover,\n  .button:hover {\n    transform: none;' in css
print('PASS: focus and reduced-motion rules')
PY
```

Expected:

```text
PASS: focus and reduced-motion rules
```

- [ ] **Step 5: Confirm only intended root and planning files changed from the pre-homepage state**

Run:

```bash
git show --name-only --format='' HEAD
git status --short
```

Expected:

```text
index.html
styles.css
```

`git status --short` should be empty. Existing files under `speedlens/` and `alwayson/` must not appear in the homepage implementation commit.

- [ ] **Step 6: Verify the GitHub Pages root after the implementation commit is present on `main`**

Run:

```bash
git branch --show-current
git ls-tree --name-only HEAD index.html styles.css
```

Expected:

```text
main
index.html
styles.css
```

The root homepage is complete when the repository root serves `index.html`, all internal routes resolve, the SpeedLens App Store destination is exact and present once, AlwaysOn has no App Store link, responsive screenshots pass visual inspection, focus/reduced-motion rules are present, and no existing app-site file was changed.
