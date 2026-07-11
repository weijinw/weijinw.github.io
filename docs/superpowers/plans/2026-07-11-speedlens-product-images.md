# SpeedLens Product Images Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the temporary CSS camera composition with the committed SpeedLens capture screenshot and add a focused two-image review/timestamp product section.

**Architecture:** Keep the existing static site structure and privacy page unchanged. `speedlens/index.html` will consume the three committed PNG assets directly, while `speedlens/styles.css` will provide responsive image framing consistent with the approved SpeedLens visual system. `speedlens/validate_site.py` will enforce the three image references, the screenshot-section copy, asset existence, and the new CSS hooks.

**Tech Stack:** HTML5, CSS, Python 3 standard library, GitHub Pages.

## Global Constraints

- Plain static HTML and CSS.
- No JavaScript framework.
- No package manager or build system.
- No analytics or tracking.
- Use relative links so the site works correctly under `/speedlens/` on GitHub Pages.
- Do not modify `alwayson/`.
- Preserve the current SpeedLens privacy-policy page unchanged.
- Support desktop, tablet, and mobile layouts.
- Use semantic HTML and descriptive image `alt` text.
- Maintain visible keyboard focus states and readable dark-mode contrast.
- Respect `prefers-reduced-motion`.
- Product screenshot section is already approved by `docs/superpowers/specs/2026-07-11-speedlens-site-design.md` when suitable source images are available.
- Use the committed assets exactly as named: `hero-capture.png`, `review-frame.png`, and `timestamp-output.png`.
- Product copy must stay within behavior verified in `weijinw/speed-track` source: exact-frame timeline selection and Track/Tag/Crop review modes in `VideoReviewView.swift`; optional `Include Tag & Timestamp` export configuration in `QueueView.swift`.

---

### Task 1: Extend the static validator for product images

**Files:**
- Modify: `speedlens/validate_site.py`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: `speedlens/index.html`, `speedlens/styles.css`, `speedlens/privacy-policy/index.html`, and the three files under `speedlens/assets/`.
- Produces: `python3 speedlens/validate_site.py` exits `0` only when the homepage references the approved product images and screenshot-section contract.

- [ ] **Step 1: Add asset and screenshot-section requirements before changing the page**

In `main()`, after loading the policy, add exactly:

```python
    for asset_name in [
        "hero-capture.png",
        "review-frame.png",
        "timestamp-output.png",
    ]:
        require_file(ROOT / "assets" / asset_name, errors)
```

Extend the homepage required-text list with exactly:

```python
            "Review the action",
            "Move from the whole play to the exact frame.",
            "Track, Tag, or Crop",
            "Include Tag & Timestamp",
            './assets/hero-capture.png',
            './assets/review-frame.png',
            './assets/timestamp-output.png',
```

Replace the stylesheet requirements:

```python
            ".capture-frame",
```

with:

```python
            ".hero-shot",
            ".workflow-grid",
            ".workflow-card",
```

- [ ] **Step 2: Run the validator to verify RED**

Run:

```bash
python3 speedlens/validate_site.py
```

Expected: exit `1` with homepage missing-text errors for the screenshot copy/image paths and stylesheet missing-text errors for `.hero-shot`, `.workflow-grid`, and `.workflow-card`. There must be no `missing required file: assets/...` errors because all three PNGs are already committed.

- [ ] **Step 3: Commit the validator contract**

```bash
git add speedlens/validate_site.py
git commit -m "Validate SpeedLens product images"
```

---

### Task 2: Integrate the capture, review, and timestamp screenshots

**Files:**
- Modify: `speedlens/index.html`
- Modify: `speedlens/styles.css`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: the Task 1 validator contract and the three committed PNG files.
- Produces: a real-product hero image plus a two-card product screenshot section under `/speedlens/`.

- [ ] **Step 1: Replace the decorative hero composition with the real capture screenshot**

Replace the complete `<div class="capture-frame" ...>...</div>` hero block with exactly:

```html
      <figure class="hero-shot">
        <img src="./assets/hero-capture.png" alt="SpeedLens sports video capture interface on iPhone.">
      </figure>
```

- [ ] **Step 2: Add the product screenshot section before the support section**

Insert exactly before `<section class="support-section shell" ...>`:

```html
    <section class="section shell" aria-labelledby="workflow-title">
      <div class="section-heading">
        <p class="eyebrow">Review the action</p>
        <h2 id="workflow-title">Move from the whole play to the exact frame.</h2>
        <p>Review the video close to its frames, then use the tools that fit the moment you are working on.</p>
      </div>

      <div class="workflow-grid">
        <figure class="workflow-card">
          <img src="./assets/review-frame.png" alt="SpeedLens video review interface with frame timeline and review controls.">
          <figcaption>
            <strong>Work at the frame you selected.</strong>
            <span>Use the timeline to select a frame, then work in Track, Tag, or Crop mode.</span>
          </figcaption>
        </figure>
        <figure class="workflow-card workflow-card-timing">
          <img src="./assets/timestamp-output.png" alt="SpeedLens processed video frame with tag and timestamp context.">
          <figcaption>
            <strong>Keep timing context in the result.</strong>
            <span>Enable Include Tag &amp; Timestamp when exporting a processed video.</span>
          </figcaption>
        </figure>
      </div>
    </section>

```

- [ ] **Step 3: Replace the obsolete decorative-camera CSS with real-image framing**

Delete the CSS rules from `.capture-frame {` through `.capture-corner-bottom-right { ... }` inclusive.

Insert exactly in their place:

```css
.hero-shot {
  margin: 0;
  overflow: hidden;
  border: 1px solid rgba(54, 215, 255, 0.24);
  border-radius: var(--radius-large);
  background: #071015;
  box-shadow: 0 36px 120px rgba(0, 0, 0, 0.5), 0 0 90px rgba(54, 215, 255, 0.1);
}

.hero-shot img {
  display: block;
  width: 100%;
  height: auto;
}
```

After the feature-card rules and before `.support-section`, add exactly:

```css
.workflow-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.workflow-card {
  margin: 0;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: var(--radius-medium);
  background: rgba(0, 0, 0, 0.28);
}

.workflow-card img {
  display: block;
  width: 100%;
  height: auto;
  background: #020506;
}

.workflow-card figcaption {
  display: grid;
  gap: 6px;
  padding: 20px 22px 22px;
}

.workflow-card figcaption strong {
  font-size: 1.08rem;
}

.workflow-card figcaption span {
  color: var(--muted);
}

.workflow-card-timing {
  border-color: rgba(255, 157, 61, 0.22);
}

.workflow-card-timing figcaption strong {
  color: #ffd09f;
}
```

In `@media (max-width: 820px)`, replace:

```css
  .capture-frame { order: -1; min-height: 330px; }
  .feature-grid,
  .support-section { grid-template-columns: 1fr; }
```

with:

```css
  .hero-shot { order: -1; }
  .feature-grid,
  .workflow-grid,
  .support-section { grid-template-columns: 1fr; }
```

In `@media (max-width: 560px)`, delete these obsolete lines:

```css
  .capture-frame { min-height: 260px; }
  .capture-topline,
  .capture-bottomline { right: 20px; left: 20px; font-size: 0.62rem; }
  .motion-field { inset: 64px 28px 58px; }
```

- [ ] **Step 4: Run the validator and HTML parser to verify GREEN**

Run:

```bash
python3 speedlens/validate_site.py
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Parser(HTMLParser):
    pass

Parser().feed(Path("speedlens/index.html").read_text(encoding="utf-8"))
print("SpeedLens homepage HTML parsed")
PY
```

Expected:

```text
SpeedLens site validation passed
SpeedLens homepage HTML parsed
```

- [ ] **Step 5: Run the product claim guard**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

homepage = Path("speedlens/index.html").read_text(encoding="utf-8")
for forbidden in [
    "AI-powered",
    "automatic athlete tracking",
    "cloud backup",
]:
    assert forbidden not in homepage, forbidden
for required in [
    "Track, Tag, or Crop",
    "Include Tag &amp; Timestamp",
]:
    assert required in homepage, required
print("SpeedLens screenshot copy guard passed")
PY
```

Expected:

```text
SpeedLens screenshot copy guard passed
```

- [ ] **Step 6: Commit the product image integration**

```bash
git add speedlens/index.html speedlens/styles.css
git commit -m "Show SpeedLens product screenshots"
```

---

### Task 3: Verify route, asset, privacy, and change scope

**Files:**
- Verify: `speedlens/index.html`
- Verify: `speedlens/styles.css`
- Verify: `speedlens/validate_site.py`
- Verify unchanged: `speedlens/privacy-policy/index.html`
- Verify assets: `speedlens/assets/hero-capture.png`, `speedlens/assets/review-frame.png`, `speedlens/assets/timestamp-output.png`

**Interfaces:**
- Consumes: Tasks 1 and 2.
- Produces: a verified Pages-ready SpeedLens site with the approved product screenshot section.

- [ ] **Step 1: Run the validator fresh**

```bash
python3 speedlens/validate_site.py
```

Expected:

```text
SpeedLens site validation passed
```

- [ ] **Step 2: Verify relative image references resolve to files**

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

root = Path("speedlens")
html = (root / "index.html").read_text(encoding="utf-8")

class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources = []
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            source = dict(attrs).get("src")
            if source:
                self.sources.append(source)

parser = Images()
parser.feed(html)
for source in parser.sources:
    assert source.startswith("./"), source
    path = root / source.removeprefix("./")
    assert path.is_file(), path
print("SpeedLens image references passed")
PY
```

Expected:

```text
SpeedLens image references passed
```

- [ ] **Step 3: Verify the privacy page is byte-for-byte unchanged from pre-task SHA**

Run:

```bash
git hash-object speedlens/privacy-policy/index.html
```

Expected:

```text
6228299fe1858ce3eb891d3d3d57fd1edc060fc7
```

- [ ] **Step 4: Verify change scope**

Compare the pre-image-integration `main` commit `54a09b66b4bd43ea189f238ba7a90c286e3c77d6` to the final head. Expected implementation paths are limited to:

```text
speedlens/index.html
speedlens/styles.css
speedlens/validate_site.py
```

The plan document may also appear in the broader commit range. `alwayson/` and `speedlens/privacy-policy/index.html` must not appear as modified implementation files.

- [ ] **Step 5: Verify both routes with a local static server**

```bash
python3 -m http.server 8000
```

In a second shell:

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
