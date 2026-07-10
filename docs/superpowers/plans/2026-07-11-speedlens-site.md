# SpeedLens Support Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a production-ready SpeedLens product/support site and privacy-policy page under `/speedlens/` in `weijinw/weijinw.github.io`.

**Architecture:** Keep SpeedLens isolated in its own app folder, using plain static HTML and CSS plus a small standard-library Python validator. The homepage follows the established AlwaysOn information hierarchy but uses a distinct near-black, electric-cyan camera/motion identity. The privacy-policy page is rendered from `weijinw/speed-track/docs/privacy-policy.md` on `main`, preserving its substantive meaning and effective date.

**Tech Stack:** HTML5, CSS, Python 3 standard library, GitHub Pages.

## Global Constraints

- Plain static HTML and CSS.
- No JavaScript framework.
- No package manager or build system unless a later requirement clearly justifies one.
- No analytics or tracking.
- Use relative links so the site works correctly under `/speedlens/` on GitHub Pages.
- Do not modify the AlwaysOn site except where a deliberate shared-site navigation change is separately approved.
- Support desktop, tablet, and mobile layouts.
- Use semantic HTML landmarks and headings.
- Provide descriptive image or decorative-region accessibility treatment.
- Maintain visible keyboard focus states and readable dark-mode contrast.
- Respect `prefers-reduced-motion` for transition or motion treatment.
- Privacy source of truth: `weijinw/speed-track/docs/privacy-policy.md` on `main`, currently effective `2026-07-06`.
- Do not invent unsupported product, collection, retention, third-party, or privacy claims.

---

## File Map

- Create `speedlens/index.html` — SpeedLens product/support homepage.
- Create `speedlens/styles.css` — SpeedLens-only visual system and responsive layout.
- Create `speedlens/privacy-policy/index.html` — readable HTML rendering of the SpeedLens policy source.
- Create `speedlens/validate_site.py` — static file/content/link validator using only Python standard library.

The first release intentionally does not add screenshots because no committed SpeedLens product image source is available. The hero uses a decorative CSS camera-frame composition rather than a fake app screenshot. Real screenshots can be added later without changing the route structure.

---

### Task 1: Add the SpeedLens static-site validator

**Files:**
- Create: `speedlens/validate_site.py`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: files rooted at `speedlens/`.
- Produces: CLI command `python3 speedlens/validate_site.py` that exits `0` and prints `SpeedLens site validation passed` only when required homepage and privacy content is present.

- [ ] **Step 1: Write the validator before the site files exist**

Create `speedlens/validate_site.py` with exactly:

```python
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href is not None:
            self.links.append(href)


def require_file(path: Path, errors: list[str]) -> str:
    if not path.is_file():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def require_text(
    content: str, required: list[str], label: str, errors: list[str]
) -> None:
    for item in required:
        if item not in content:
            errors.append(f"{label} missing required text: {item}")


def require_links(
    content: str, required: list[str], label: str, errors: list[str]
) -> None:
    parser = LinkParser()
    parser.feed(content)
    for href in required:
        if href not in parser.links:
            errors.append(f"{label} missing required link: {href}")


def main() -> int:
    errors: list[str] = []

    homepage = require_file(ROOT / "index.html", errors)
    styles = require_file(ROOT / "styles.css", errors)
    policy = require_file(ROOT / "privacy-policy" / "index.html", errors)

    require_text(
        homepage,
        [
            "SpeedLens",
            "Capture fast action. Find the moment that matters.",
            "Built for action, not social posting.",
            "Record sports video",
            "Review on your device",
            "Optional GPS metadata",
            "Need help?",
            "welkin.wong@gmail.com",
        ],
        "homepage",
        errors,
    )
    require_links(
        homepage,
        ["./privacy-policy/", "mailto:welkin.wong@gmail.com"],
        "homepage",
        errors,
    )

    require_text(
        policy,
        [
            "Privacy Policy",
            "Information Collection and Use",
            "Third Party Access",
            "Opt-Out Rights",
            "Data Retention Policy",
            "Children",
            "Security",
            "Changes",
            "Your Consent",
            "Contact Us",
            "2026-07-06",
            "welkin.wong@gmail.com",
        ],
        "privacy policy",
        errors,
    )
    require_links(
        policy,
        ["../", "mailto:welkin.wong@gmail.com"],
        "privacy policy",
        errors,
    )

    require_text(
        styles,
        [
            "--accent: #36d7ff;",
            "--timing: #ff9d3d;",
            ".capture-frame",
            "@media (max-width: 820px)",
            "@media (max-width: 560px)",
            "prefers-reduced-motion",
        ],
        "styles",
        errors,
    )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("SpeedLens site validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Run the validator to verify RED**

Run:

```bash
python3 speedlens/validate_site.py
```

Expected: exit `1` with errors including:

```text
ERROR: missing required file: index.html
ERROR: missing required file: styles.css
ERROR: missing required file: privacy-policy/index.html
```

- [ ] **Step 3: Commit the validator**

```bash
git add speedlens/validate_site.py
git commit -m "Add SpeedLens site validator"
```

---

### Task 2: Build the SpeedLens homepage and visual system

**Files:**
- Create: `speedlens/index.html`
- Create: `speedlens/styles.css`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: the validator contract from Task 1.
- Produces: `/speedlens/` homepage and a shared SpeedLens stylesheet consumed by the homepage and privacy page.

- [ ] **Step 1: Create the homepage with verified product claims**

Create `speedlens/index.html` with exactly:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="SpeedLens is a focused iPhone camera for recording sports video and reviewing clips on your device.">
  <title>SpeedLens — Sports Video, Focused</title>
  <link rel="stylesheet" href="./styles.css">
</head>
<body>
  <header class="site-header">
    <a class="brand" href="./" aria-label="SpeedLens home">
      <span class="brand-mark" aria-hidden="true"></span>
      <span>SpeedLens</span>
    </a>
    <nav class="site-nav" aria-label="Primary navigation">
      <a aria-current="page" href="./">Home</a>
      <a href="./privacy-policy/">Privacy Policy</a>
    </nav>
  </header>

  <main>
    <section class="hero shell" aria-labelledby="hero-title">
      <div class="hero-copy">
        <p class="eyebrow">Sports video, focused</p>
        <h1 id="hero-title">Capture fast action. Find the moment that matters.</h1>
        <p class="hero-lede">
          SpeedLens is a focused iPhone camera for recording sports video and reviewing clips on your device. Your videos and review data stay with you.
        </p>
        <div class="hero-actions">
          <a class="button button-primary" href="#features">See how it works</a>
          <a class="button button-secondary" href="#support">Get support</a>
        </div>
      </div>

      <div class="capture-frame" role="img" aria-label="Decorative sports camera frame with motion guides and recording indicators.">
        <span class="capture-corner capture-corner-top-left" aria-hidden="true"></span>
        <span class="capture-corner capture-corner-top-right" aria-hidden="true"></span>
        <span class="capture-corner capture-corner-bottom-left" aria-hidden="true"></span>
        <span class="capture-corner capture-corner-bottom-right" aria-hidden="true"></span>
        <div class="capture-topline" aria-hidden="true">
          <span class="record-indicator"><span class="record-dot"></span> REC</span>
          <span>SPORTS CAPTURE</span>
        </div>
        <div class="motion-field" aria-hidden="true">
          <span class="motion-line motion-line-one"></span>
          <span class="motion-line motion-line-two"></span>
          <span class="motion-line motion-line-three"></span>
          <span class="focus-box"></span>
        </div>
        <div class="capture-bottomline" aria-hidden="true">
          <span>ON DEVICE</span>
          <span class="timing-label">READY</span>
        </div>
      </div>
    </section>

    <section class="section shell" aria-labelledby="value-title">
      <div class="section-heading">
        <p class="eyebrow">Made for the sideline</p>
        <h2 id="value-title">Built for action, not social posting.</h2>
        <p>Open the camera, record the play, save the video, and review it on the device you already have with you.</p>
      </div>
    </section>

    <section class="section shell" id="features" aria-labelledby="features-title">
      <div class="section-heading">
        <p class="eyebrow">Focused tools</p>
        <h2 id="features-title">The capture workflow stays close to the video.</h2>
        <p>SpeedLens uses iPhone camera, microphone, Photos, and optional Location access only for the features you choose to use.</p>
      </div>

      <div class="feature-grid">
        <article class="feature-card">
          <span class="feature-kicker">01</span>
          <h3>Record sports video</h3>
          <p>Use the iPhone camera to preview and record fast-moving sports moments without turning the experience into a social feed.</p>
        </article>
        <article class="feature-card">
          <span class="feature-kicker">02</span>
          <h3>Audio when you need it</h3>
          <p>Microphone access can be used to record audio with your videos when that context matters.</p>
        </article>
        <article class="feature-card">
          <span class="feature-kicker">03</span>
          <h3>Review on your device</h3>
          <p>Save, index, and play back videos on your device. Recorded video, metadata, settings, and review data are not sent to the developer.</p>
        </article>
        <article class="feature-card">
          <span class="feature-kicker timing-kicker">04</span>
          <h3>Optional GPS metadata</h3>
          <p>Grant Location access only when you want SpeedLens to add GPS metadata to recorded videos.</p>
        </article>
      </div>
    </section>

    <section class="support-section shell" id="support" aria-labelledby="support-title">
      <div>
        <p class="eyebrow">Support</p>
        <h2 id="support-title">Need help?</h2>
        <p>Questions, feedback, and bug reports are welcome. Include your iPhone model and iOS version when they are relevant.</p>
      </div>
      <a class="support-email" href="mailto:welkin.wong@gmail.com">
        <span>Email support</span>
        <strong>welkin.wong@gmail.com</strong>
      </a>
    </section>
  </main>

  <footer class="site-footer shell">
    <p>SpeedLens</p>
    <div class="footer-links">
      <a href="mailto:welkin.wong@gmail.com">Support</a>
      <a href="./privacy-policy/">Privacy Policy</a>
    </div>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Create the SpeedLens visual system**

Create `speedlens/styles.css` with exactly:

```css
:root {
  color-scheme: dark;
  --bg: #04070a;
  --surface: rgba(255, 255, 255, 0.05);
  --surface-strong: rgba(255, 255, 255, 0.08);
  --line: rgba(255, 255, 255, 0.11);
  --text: #f4fbff;
  --muted: #9aaab4;
  --accent: #36d7ff;
  --accent-strong: #9beeff;
  --timing: #ff9d3d;
  --max-width: 1180px;
  --radius-large: 32px;
  --radius-medium: 22px;
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", sans-serif;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }

body {
  min-width: 320px;
  margin: 0;
  color: var(--text);
  background:
    radial-gradient(circle at 78% 8%, rgba(54, 215, 255, 0.15), transparent 28rem),
    radial-gradient(circle at 12% 54%, rgba(18, 83, 112, 0.18), transparent 25rem),
    var(--bg);
  font-size: 16px;
  line-height: 1.6;
}

a { color: inherit; }
.shell { width: min(calc(100% - 40px), var(--max-width)); margin-inline: auto; }

.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  min-height: 72px;
  padding: 0 max(20px, calc((100vw - var(--max-width)) / 2));
  border-bottom: 1px solid var(--line);
  background: rgba(4, 7, 10, 0.8);
  backdrop-filter: blur(22px);
}

.brand,
.site-nav a,
.footer-links a { text-decoration: none; }

.brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.brand-mark {
  width: 15px;
  height: 15px;
  border: 2px solid var(--accent);
  border-radius: 4px;
  box-shadow: 0 0 24px rgba(54, 215, 255, 0.72);
  transform: rotate(45deg);
}

.site-nav,
.footer-links { display: flex; align-items: center; gap: 22px; }
.site-nav { color: var(--muted); font-size: 0.92rem; }

.site-nav a:hover,
.site-nav a:focus-visible,
.site-nav a[aria-current="page"],
.footer-links a:hover,
.footer-links a:focus-visible { color: var(--text); }

:focus-visible {
  outline: 2px solid var(--accent-strong);
  outline-offset: 4px;
  border-radius: 6px;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
  align-items: center;
  gap: clamp(34px, 5vw, 72px);
  min-height: min(700px, calc(100vh - 72px));
  padding-block: clamp(54px, 7vw, 82px);
}

.hero-copy { max-width: 580px; }
.eyebrow {
  margin: 0 0 14px;
  color: var(--accent-strong);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

h1, h2, h3, p { margin-top: 0; }
h1, h2, h3 { letter-spacing: -0.04em; line-height: 1.04; }
h1 { margin-bottom: 26px; font-size: clamp(3rem, 5.4vw, 5.6rem); font-weight: 650; }
h2 { margin-bottom: 20px; font-size: clamp(2.2rem, 4vw, 4.35rem); font-weight: 620; }
h3 { margin-bottom: 14px; font-size: 1.45rem; }

.hero-lede,
.section-heading > p:last-child,
.support-section p,
.policy-intro { color: var(--muted); font-size: clamp(1.04rem, 1.6vw, 1.2rem); }

.hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 34px; }
.button {
  display: inline-flex;
  min-height: 48px;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
  border: 1px solid var(--line);
  border-radius: 999px;
  font-weight: 650;
  text-decoration: none;
  transition: transform 160ms ease, background 160ms ease, border-color 160ms ease;
}
.button:hover { transform: translateY(-2px); }
.button-primary { border-color: rgba(54, 215, 255, 0.7); background: var(--accent); color: #021017; }
.button-secondary { background: var(--surface); }

.capture-frame {
  position: relative;
  min-height: 390px;
  overflow: hidden;
  border: 1px solid rgba(54, 215, 255, 0.24);
  border-radius: var(--radius-large);
  background:
    linear-gradient(rgba(54, 215, 255, 0.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(54, 215, 255, 0.045) 1px, transparent 1px),
    radial-gradient(circle at 65% 45%, rgba(54, 215, 255, 0.12), transparent 36%),
    #071015;
  background-size: 42px 42px, 42px 42px, auto, auto;
  box-shadow: 0 36px 120px rgba(0, 0, 0, 0.5), 0 0 90px rgba(54, 215, 255, 0.1);
}

.capture-topline,
.capture-bottomline {
  position: absolute;
  right: 28px;
  left: 28px;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  color: #c6d5dc;
  font-family: ui-monospace, "SFMono-Regular", Menlo, monospace;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
}
.capture-topline { top: 24px; }
.capture-bottomline { bottom: 24px; }
.record-indicator { display: inline-flex; align-items: center; gap: 8px; color: #f5fbff; }
.record-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--timing); box-shadow: 0 0 14px rgba(255, 157, 61, 0.7); }
.timing-label { color: var(--timing); }

.motion-field { position: absolute; inset: 72px 44px 68px; }
.motion-line {
  position: absolute;
  display: block;
  height: 2px;
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, rgba(54, 215, 255, 0.9), transparent);
  transform: rotate(-12deg);
}
.motion-line-one { top: 28%; left: 2%; width: 72%; }
.motion-line-two { top: 50%; left: 18%; width: 78%; opacity: 0.68; }
.motion-line-three { top: 68%; left: 8%; width: 58%; opacity: 0.42; }
.focus-box {
  position: absolute;
  top: 20%;
  right: 14%;
  width: 34%;
  aspect-ratio: 1 / 0.72;
  border: 1px solid rgba(54, 215, 255, 0.62);
  box-shadow: inset 0 0 28px rgba(54, 215, 255, 0.05), 0 0 28px rgba(54, 215, 255, 0.08);
}
.capture-corner { position: absolute; z-index: 3; width: 22px; height: 22px; border-color: var(--accent); }
.capture-corner-top-left { top: 18px; left: 18px; border-top: 2px solid; border-left: 2px solid; }
.capture-corner-top-right { top: 18px; right: 18px; border-top: 2px solid; border-right: 2px solid; }
.capture-corner-bottom-left { bottom: 18px; left: 18px; border-bottom: 2px solid; border-left: 2px solid; }
.capture-corner-bottom-right { right: 18px; bottom: 18px; border-right: 2px solid; border-bottom: 2px solid; }

.section { padding-block: 96px; }
.section-heading { max-width: 760px; margin-bottom: 52px; }
.feature-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; }
.feature-card {
  min-height: 250px;
  padding: 30px;
  border: 1px solid var(--line);
  border-radius: var(--radius-medium);
  background: linear-gradient(145deg, var(--surface-strong), rgba(255, 255, 255, 0.02));
}
.feature-card p { max-width: 54ch; margin-bottom: 0; color: var(--muted); }
.feature-kicker { display: block; margin-bottom: 54px; color: var(--accent-strong); font-size: 0.76rem; font-weight: 700; letter-spacing: 0.16em; }
.timing-kicker { color: var(--timing); }

.support-section {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(300px, 0.65fr);
  gap: 36px;
  align-items: center;
  margin-block: 28px 96px;
  padding: 44px;
  border: 1px solid rgba(54, 215, 255, 0.25);
  border-radius: var(--radius-large);
  background: radial-gradient(circle at 100% 0%, rgba(54, 215, 255, 0.16), transparent 20rem), var(--surface);
}
.support-section h2 { font-size: clamp(2.5rem, 4vw, 4rem); }
.support-section p { max-width: 60ch; margin-bottom: 0; }
.support-email {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: var(--radius-medium);
  background: rgba(0, 0, 0, 0.28);
  text-decoration: none;
}
.support-email span { color: var(--muted); font-size: 0.84rem; }
.support-email strong { overflow-wrap: anywhere; font-size: clamp(1rem, 2vw, 1.25rem); }

.site-footer {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  padding-block: 30px 42px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 0.88rem;
}
.site-footer p { margin-bottom: 0; }

.policy-shell { width: min(calc(100% - 40px), 820px); margin-inline: auto; padding-block: 88px 120px; }
.policy-header { margin-bottom: 64px; }
.policy-header h1 { font-size: clamp(3rem, 7vw, 5.4rem); }
.policy-content { color: #dfe9ed; }
.policy-content h2 { margin-top: 56px; margin-bottom: 18px; font-size: clamp(1.7rem, 3vw, 2.5rem); }
.policy-content p,
.policy-content li { color: #b3c0c7; }
.policy-content ul { padding-left: 22px; }
.policy-content a { color: var(--accent-strong); }

@media (max-width: 820px) {
  .hero { grid-template-columns: 1fr; min-height: auto; gap: 24px; padding-block: 36px; }
  .hero-copy { max-width: none; }
  .capture-frame { order: -1; min-height: 330px; }
  .feature-grid,
  .support-section { grid-template-columns: 1fr; }
  .support-section { padding: 32px; }
}

@media (max-width: 560px) {
  .site-header { min-height: auto; align-items: flex-start; padding-block: 18px; }
  .brand { max-width: 170px; }
  .site-nav { flex-direction: column; align-items: flex-end; gap: 4px; }
  h1 { margin-bottom: 20px; font-size: clamp(2.65rem, 14vw, 4.2rem); }
  .hero { padding-top: 24px; }
  .capture-frame { min-height: 260px; }
  .capture-topline,
  .capture-bottomline { right: 20px; left: 20px; font-size: 0.62rem; }
  .motion-field { inset: 64px 28px 58px; }
  .section { padding-block: 70px; }
  .feature-grid { grid-template-columns: 1fr; }
  .feature-card { min-height: 220px; padding: 24px; }
  .support-section { margin-bottom: 72px; padding: 26px; }
  .site-footer { flex-direction: column; }
  .footer-links { flex-wrap: wrap; }
  .policy-shell { padding-block: 56px 88px; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .button { transition: none; }
}
```

- [ ] **Step 3: Run the validator to verify the homepage/styles errors are gone but policy remains RED**

Run:

```bash
python3 speedlens/validate_site.py
```

Expected: exit `1`; no homepage or stylesheet required-text errors; remaining errors are for `privacy-policy/index.html`.

- [ ] **Step 4: Run a syntax-level HTML parse check**

Run:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Parser(HTMLParser):
    pass

for path in [Path("speedlens/index.html")]:
    Parser().feed(path.read_text(encoding="utf-8"))
    print(f"parsed {path}")
PY
```

Expected:

```text
parsed speedlens/index.html
```

- [ ] **Step 5: Commit the homepage and stylesheet**

```bash
git add speedlens/index.html speedlens/styles.css
git commit -m "Add SpeedLens support homepage"
```

---

### Task 3: Render the SpeedLens privacy policy from the app repository source

**Files:**
- Create: `speedlens/privacy-policy/index.html`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: `speedlens/styles.css` and policy source `weijinw/speed-track/docs/privacy-policy.md` on `main`.
- Produces: `/speedlens/privacy-policy/` with policy sections and wording matching the source policy's substantive meaning.

- [ ] **Step 1: Confirm the source policy still matches the reviewed SHA before copying**

Run in a checkout that has GitHub access:

```bash
gh api repos/weijinw/speed-track/contents/docs/privacy-policy.md?ref=main --jq '.sha'
```

Expected reviewed SHA:

```text
4b0906d10caf0813c365c37a5bc4379cd288d6f6
```

If the SHA differs, re-read the new policy before implementation and preserve the new source instead of silently copying the reviewed version.

- [ ] **Step 2: Create the privacy-policy page**

Create `speedlens/privacy-policy/index.html` with exactly:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Privacy Policy for SpeedLens.">
  <title>Privacy Policy — SpeedLens</title>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header class="site-header">
    <a class="brand" href="../" aria-label="SpeedLens home">
      <span class="brand-mark" aria-hidden="true"></span>
      <span>SpeedLens</span>
    </a>
    <nav class="site-nav" aria-label="Primary navigation">
      <a href="../">Home</a>
      <a aria-current="page" href="./">Privacy Policy</a>
    </nav>
  </header>

  <main class="policy-shell">
    <header class="policy-header">
      <p class="eyebrow">SpeedLens</p>
      <h1>Privacy Policy</h1>
      <p class="policy-intro">This Privacy Policy applies to the SpeedLens app (hereby referred to as the "Application") for mobile devices, created by Weijin Wang (hereby referred to as the "Service Provider") as a Free service. This service is intended for use "AS IS".</p>
    </header>

    <article class="policy-content">
      <h2>Information Collection and Use</h2>
      <p>The Application is designed with privacy in mind. The Application does not collect, transmit, sell, or share personal data, analytics data, advertising data, or usage data with the Service Provider or any third party.</p>
      <p>SpeedLens uses device features only to provide its core functionality:</p>
      <ul>
        <li>Camera access is used to preview and record sports video.</li>
        <li>Microphone access may be used to record audio with videos.</li>
        <li>Photo Library access is used to save, index, and play back videos on your device.</li>
        <li>Location access, if granted, is used to add GPS metadata to recorded videos.</li>
      </ul>
      <p>Recorded videos, video metadata, app settings, and review data remain on your device or in your Photo Library. The Service Provider does not receive or store this information.</p>

      <h2>Third Party Access</h2>
      <p>The Application does not use third-party services, SDKs, or APIs that collect, use, or share your information. No data is transmitted to external services, and no third parties have access to user information through the Application.</p>

      <h2>Opt-Out Rights</h2>
      <p>You can stop all use of the Application by uninstalling it from your device using the standard process available on your mobile device or through the mobile application marketplace.</p>
      <p>You can also control access to device permissions, including Camera, Microphone, Photos, and Location, in the iOS Settings app. Some Application features may not work if required permissions are disabled.</p>

      <h2>Data Retention Policy</h2>
      <p>The Application does not collect or retain user data on servers controlled by the Service Provider.</p>
      <p>Videos, settings, and related data created or used by the Application may remain on your device or in your Photo Library until you delete them. You are responsible for managing or deleting local videos and files from your device or Photo Library.</p>

      <h2>Children</h2>
      <p>The Service Provider does not use the Application to knowingly solicit data from or market to children under the age of 13. The Application does not collect personal information from any users, including children.</p>
      <p>If you are a parent or guardian and you have concerns about your child's use of the Application, please contact the Service Provider.</p>

      <h2>Security</h2>
      <p>The Application does not transmit user data to the Service Provider or store user data on external servers. Data such as recorded videos and app settings remains on your device or in your Photo Library and is protected by the security features of your device and Apple account.</p>

      <h2>Changes</h2>
      <p>This Privacy Policy may be updated from time to time for any reason. The Service Provider will notify users of changes by updating this page with the new Privacy Policy. You are advised to consult this Privacy Policy regularly for any changes, as continued use is deemed approval of all changes.</p>
      <p>This Privacy Policy is effective as of 2026-07-06.</p>

      <h2>Your Consent</h2>
      <p>By using the Application, you consent to this Privacy Policy.</p>

      <h2>Contact Us</h2>
      <p>If you have any questions regarding privacy while using the Application, or have questions about the Service Provider's practices, please contact the Service Provider via email at <a href="mailto:welkin.wong@gmail.com">welkin.wong@gmail.com</a>.</p>
    </article>
  </main>

  <footer class="site-footer shell">
    <p>SpeedLens</p>
    <div class="footer-links">
      <a href="mailto:welkin.wong@gmail.com">Support</a>
      <a href="../">Home</a>
    </div>
  </footer>
</body>
</html>
```

- [ ] **Step 3: Run the site validator to verify GREEN**

Run:

```bash
python3 speedlens/validate_site.py
```

Expected:

```text
SpeedLens site validation passed
```

- [ ] **Step 4: Verify policy heading parity against the source Markdown**

From a checkout that contains `speed-track` as a sibling directory, run:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

source = Path("../speed-track/docs/privacy-policy.md").read_text(encoding="utf-8")
html = Path("speedlens/privacy-policy/index.html").read_text(encoding="utf-8")

headings = [
    line.removeprefix("## ").strip()
    for line in source.splitlines()
    if line.startswith("## ")
]

missing = [heading for heading in headings if f"<h2>{heading}</h2>" not in html]
assert not missing, f"missing privacy headings: {missing}"
assert "2026-07-06" in source and "2026-07-06" in html
print("SpeedLens privacy policy parity passed")
PY
```

Expected:

```text
SpeedLens privacy policy parity passed
```

- [ ] **Step 5: Commit the privacy page**

```bash
git add speedlens/privacy-policy/index.html
git commit -m "Add SpeedLens privacy policy page"
```

---

### Task 4: Perform final local route and change-scope verification

**Files:**
- Verify: `speedlens/index.html`
- Verify: `speedlens/styles.css`
- Verify: `speedlens/privacy-policy/index.html`
- Verify: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: all previous tasks.
- Produces: verified Pages-ready routes `/speedlens/` and `/speedlens/privacy-policy/`.

- [ ] **Step 1: Run the static validator fresh**

```bash
python3 speedlens/validate_site.py
```

Expected:

```text
SpeedLens site validation passed
```

- [ ] **Step 2: Start a local static server**

Run:

```bash
python3 -m http.server 8000
```

Expected: server listens on port `8000` from the repository root.

- [ ] **Step 3: Verify both routes return HTTP 200 in a second terminal**

Run:

```bash
set -euo pipefail
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/ >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/privacy-policy/ >/dev/null
echo "SpeedLens routes passed"
```

Expected:

```text
SpeedLens routes passed
```

- [ ] **Step 4: Verify page copy does not exceed the reviewed privacy/product claims**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

homepage = Path("speedlens/index.html").read_text(encoding="utf-8")
for forbidden in [
    "AI-powered",
    "automatic athlete tracking",
    "60 FPS",
    "burned-in timestamp",
    "frame-accurate stopwatch",
    "cloud backup",
]:
    assert forbidden not in homepage, forbidden
print("SpeedLens claim guard passed")
PY
```

Expected:

```text
SpeedLens claim guard passed
```

- [ ] **Step 5: Verify the implementation did not modify AlwaysOn**

Run:

```bash
git diff --name-only HEAD~3..HEAD
```

Expected changed site implementation paths are limited to:

```text
speedlens/index.html
speedlens/styles.css
speedlens/privacy-policy/index.html
speedlens/validate_site.py
```

The existing design and plan documents may appear when comparing a broader commit range, but `alwayson/` must not appear.

- [ ] **Step 6: Check Git status**

```bash
git status --short
```

Expected: no uncommitted SpeedLens implementation changes.

- [ ] **Step 7: Publish and verify GitHub Pages**

Push `main`, allow the existing `weijinw.github.io` Pages deployment to publish, then verify:

```text
https://weijinw.github.io/speedlens/
https://weijinw.github.io/speedlens/privacy-policy/
```

Do not replace the Google Sites or App Store privacy URL until both public routes load successfully.
