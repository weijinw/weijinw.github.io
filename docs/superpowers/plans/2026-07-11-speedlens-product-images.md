# SpeedLens Product Images Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the temporary CSS camera composition with the committed SpeedLens capture screenshot and add a focused two-image review/timestamp product section.

**Architecture:** Keep the existing static site structure and privacy page unchanged. `speedlens/index.html` consumes the three committed PNG assets directly, `speedlens/styles.css` frames those images responsively, and `speedlens/validate_site.py` enforces the image references, asset existence, screenshot copy, and CSS hooks.

**Tech Stack:** HTML5, CSS, Python 3 standard library, GitHub Pages.

## Global Constraints

- Plain static HTML and CSS.
- No JavaScript framework.
- No package manager or build system.
- No analytics or tracking.
- Use relative links so the site works correctly under `/speedlens/` on GitHub Pages.
- Do not modify `alwayson/`.
- Preserve `speedlens/privacy-policy/index.html` byte-for-byte.
- Support desktop, tablet, and mobile layouts.
- Use semantic HTML and descriptive image `alt` text.
- Maintain visible keyboard focus states and readable dark-mode contrast.
- Respect `prefers-reduced-motion`.
- Use the approved screenshot section from `docs/superpowers/specs/2026-07-11-speedlens-site-design.md`.
- Use the committed assets exactly as named: `hero-capture.png`, `review-frame.png`, and `timestamp-output.png`.
- Keep product copy within behavior verified in `weijinw/speed-track`: exact-frame timeline selection and Track/Tag/Crop review modes in `VideoReviewView.swift`; optional `Include Tag & Timestamp` export configuration in `QueueView.swift`.

---

### Task 1: Extend the static validator for product images

**Files:**
- Modify: `speedlens/validate_site.py`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: the SpeedLens homepage, stylesheet, privacy page, and three product PNGs.
- Produces: `python3 speedlens/validate_site.py`, which exits `0` only when the image integration contract is present.

- [ ] **Step 1: Add asset existence checks before changing the page**

After loading the policy, add:

```python
    for asset_name in [
        "hero-capture.png",
        "review-frame.png",
        "timestamp-output.png",
    ]:
        require_file(ROOT / "assets" / asset_name, errors)
```

- [ ] **Step 2: Add screenshot copy and image-path requirements**

Extend the homepage required-text list with:

```python
            "Review the action",
            "Move from the whole play to the exact frame.",
            "Track, Tag, or Crop",
            "Include Tag &amp; Timestamp",
            './assets/hero-capture.png',
            './assets/review-frame.png',
            './assets/timestamp-output.png',
```

Replace the stylesheet requirement:

```python
            ".capture-frame",
```

with:

```python
            ".hero-shot",
            ".workflow-grid",
            ".workflow-card",
```

- [ ] **Step 3: Run the validator to verify RED**

Run:

```bash
python3 speedlens/validate_site.py
```

Expected: exit `1` with missing homepage screenshot-copy/image-path requirements and missing `.hero-shot`, `.workflow-grid`, and `.workflow-card` requirements. There must be no `missing required file: assets/...` errors.

- [ ] **Step 4: Commit the validator contract**

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
- Consumes: the Task 1 validator contract and the three PNG assets.
- Produces: a real-product hero and a responsive two-card review/timestamp screenshot section.

- [ ] **Step 1: Replace the decorative hero composition**

Replace the complete `.capture-frame` hero element with:

```html
      <figure class="hero-shot">
        <img src="./assets/hero-capture.png" alt="SpeedLens sports video capture interface on iPhone.">
      </figure>
```

- [ ] **Step 2: Add the screenshot section before support**

Insert:

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

- [ ] **Step 3: Replace decorative-camera CSS with real-image framing**

Delete the rules from `.capture-frame {` through `.capture-corner-bottom-right { ... }` and insert:

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

After `.timing-kicker`, add:

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

- [ ] **Step 4: Update responsive layout hooks**

In `@media (max-width: 820px)`, use:

```css
  .hero-shot { order: -1; }
  .feature-grid,
  .workflow-grid,
  .support-section { grid-template-columns: 1fr; }
```

Remove the obsolete `.capture-frame`, `.capture-topline`, `.capture-bottomline`, and `.motion-field` mobile rules.

- [ ] **Step 5: Run GREEN verification**

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

- [ ] **Step 6: Run the screenshot copy guard**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

homepage = Path("speedlens/index.html").read_text(encoding="utf-8")
for forbidden in ["AI-powered", "automatic athlete tracking", "cloud backup"]:
    assert forbidden not in homepage, forbidden
for required in ["Track, Tag, or Crop", "Include Tag &amp; Timestamp"]:
    assert required in homepage, required
print("SpeedLens screenshot copy guard passed")
PY
```

Expected:

```text
SpeedLens screenshot copy guard passed
```

- [ ] **Step 7: Commit the product image integration**

```bash
git add speedlens/index.html speedlens/styles.css
git commit -m "Show SpeedLens product screenshots"
```

---

### Task 3: Verify route, assets, privacy, and scope

**Files:**
- Verify: `speedlens/index.html`
- Verify: `speedlens/styles.css`
- Verify: `speedlens/validate_site.py`
- Verify unchanged: `speedlens/privacy-policy/index.html`
- Verify: `speedlens/assets/hero-capture.png`
- Verify: `speedlens/assets/review-frame.png`
- Verify: `speedlens/assets/timestamp-output.png`

**Interfaces:**
- Consumes: Tasks 1 and 2.
- Produces: a verified Pages-ready SpeedLens screenshot integration.

- [ ] **Step 1: Run the validator fresh**

```bash
python3 speedlens/validate_site.py
```

Expected: `SpeedLens site validation passed`.

- [ ] **Step 2: Verify every relative image reference resolves**

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
assert parser.sources == [
    "./assets/hero-capture.png",
    "./assets/review-frame.png",
    "./assets/timestamp-output.png",
]
for source in parser.sources:
    assert (root / source.removeprefix("./")).is_file(), source
print("SpeedLens image references passed")
PY
```

Expected: `SpeedLens image references passed`.

- [ ] **Step 3: Verify privacy is unchanged**

```bash
git hash-object speedlens/privacy-policy/index.html
```

Expected:

```text
6228299fe1858ce3eb891d3d3d57fd1edc060fc7
```

- [ ] **Step 4: Verify change scope**

Compare `54a09b66b4bd43ea189f238ba7a90c286e3c77d6` to final `main`. Implementation changes must be limited to:

```text
speedlens/index.html
speedlens/styles.css
speedlens/validate_site.py
```

The plan document may also appear. `alwayson/` and `speedlens/privacy-policy/index.html` must not be modified.

- [ ] **Step 5: Verify routes from a local static server**

Start:

```bash
python3 -m http.server 8000
```

Then run:

```bash
set -euo pipefail
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/ >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/privacy-policy/ >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/assets/hero-capture.png >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/assets/review-frame.png >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/assets/timestamp-output.png >/dev/null
echo "SpeedLens routes and asset paths passed"
```

Expected: `SpeedLens routes and asset paths passed`.
