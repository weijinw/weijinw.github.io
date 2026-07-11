# SpeedLens Poster Story Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Present the three committed SpeedLens portrait marketing posters as a constrained hero visual and an alternating three-step capture → review → export product story.

**Architecture:** Keep the existing static-site routes, feature cards, privacy page, and support section. Update only the SpeedLens homepage markup, homepage-specific CSS, and static validator. Reuse the three committed PNGs without editing or recompression.

**Tech Stack:** HTML5, CSS, Python 3 standard library, GitHub Pages.

## Global Constraints

- Plain static HTML and CSS.
- No JavaScript framework.
- No package manager or build system.
- No analytics or tracking.
- Use relative links so the site works correctly under `/speedlens/` on GitHub Pages.
- Do not modify `alwayson/`.
- Preserve `speedlens/privacy-policy/index.html` unchanged.
- Use the committed assets exactly as named: `hero-capture.png`, `review-frame.png`, and `timestamp-output.png`.
- Do not edit, crop, recompress, or replace the poster artwork.
- Desktop hero poster maximum height is `680px`.
- Desktop story poster maximum height is `760px`.
- At `820px` and below, story poster maximum height is `640px` and every poster appears before its copy.
- At `560px` and below, poster width is `100%` with automatic height and no fixed or minimum poster height.
- Product copy may describe camera capture controls, tracked-subject overlay during capture, recorded-video review, frame timeline/frame selection, Track/Tag/Crop review modes, crop-to-tracked-subject output, and Include Tag & Timestamp output.
- Do not add AI-powered tracking, automatic athlete identity recognition, cloud backup, or guaranteed frame-rate claims.

---

### Task 1: Tighten the static validator around the poster story

**Files:**
- Modify: `speedlens/validate_site.py`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: the current homepage, stylesheet, privacy page, and three committed PNG assets.
- Produces: `python3 speedlens/validate_site.py` exits `0` only when the approved three-step story and poster-layout hooks are present.

- [ ] **Step 1: Replace the old screenshot-section expectations with the poster-story contract**

In the homepage required-text list, replace:

```python
            "Review the action",
            "Move from the whole play to the exact frame.",
            "Track, Tag, or Crop",
            "Include Tag &amp; Timestamp",
            './assets/hero-capture.png',
            './assets/review-frame.png',
            './assets/timestamp-output.png',
```

with:

```python
            "How SpeedLens works",
            "From capture to the highlight.",
            "Capture fast action with the subject in view.",
            "Move through the recording to find the moment.",
            "Turn review work into a focused output.",
            "Track, Tag, and Crop",
            "Tag &amp; Timestamp",
            'class="story-step"',
            'class="story-step story-step-reverse"',
            'class="story-step story-step-timing"',
            './assets/hero-capture.png',
            './assets/review-frame.png',
            './assets/timestamp-output.png',
```

In the stylesheet required-text list, replace:

```python
            ".workflow-grid",
            ".workflow-card",
```

with:

```python
            ".story-list",
            ".story-step",
            ".story-poster",
            ".story-step-reverse",
            "max-height: 680px;",
            "max-height: 760px;",
            "max-height: 640px;",
```

- [ ] **Step 2: Run the validator to verify RED**

Run:

```bash
python3 speedlens/validate_site.py
```

Expected: exit `1` with missing homepage text for `How SpeedLens works`, `From capture to the highlight.`, the three story-copy lines, and story-step classes; and missing stylesheet text for `.story-list`, `.story-step`, `.story-poster`, `.story-step-reverse`, and the poster maximum-height values. Asset-file checks must remain green.

- [ ] **Step 3: Commit the validator contract**

```bash
git add speedlens/validate_site.py
git commit -m "Validate SpeedLens poster story"
```

---

### Task 2: Replace screenshot cards with the three-step poster narrative

**Files:**
- Modify: `speedlens/index.html`
- Modify: `speedlens/styles.css`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: the Task 1 validator contract and the three PNG files under `speedlens/assets/`.
- Produces: the constrained hero poster plus the alternating three-row `How SpeedLens works` section.

- [ ] **Step 1: Update the hero poster alt text**

Replace the hero image markup with:

```html
      <figure class="hero-shot">
        <img src="./assets/hero-capture.png" alt="SpeedLens capture interface showing camera controls and a tracked skateboarder.">
      </figure>
```

- [ ] **Step 2: Replace the complete current workflow section with the approved story section**

Replace the section beginning with:

```html
    <section class="section shell" aria-labelledby="workflow-title">
```

and ending immediately before:

```html
    <section class="support-section shell" id="support" aria-labelledby="support-title">
```

with exactly:

```html
    <section class="section story-section shell" aria-labelledby="story-title">
      <div class="section-heading">
        <p class="eyebrow">How SpeedLens works</p>
        <h2 id="story-title">From capture to the highlight.</h2>
        <p>Keep the workflow close to the action: capture, review the moment, then create the output you need.</p>
      </div>

      <div class="story-list">
        <article class="story-step">
          <figure class="story-poster">
            <img src="./assets/hero-capture.png" alt="SpeedLens capture interface showing camera controls and a tracked skateboarder.">
          </figure>
          <div class="story-copy">
            <span class="story-number">01</span>
            <h3>Capture fast action with the subject in view.</h3>
            <p>Keep camera controls close at hand and see the tracked subject directly in the capture frame.</p>
          </div>
        </article>

        <article class="story-step story-step-reverse">
          <figure class="story-poster">
            <img src="./assets/review-frame.png" alt="SpeedLens recorded-video review interface with playback controls and frame thumbnails.">
          </figure>
          <div class="story-copy">
            <span class="story-number">02</span>
            <h3>Move through the recording to find the moment.</h3>
            <p>Review recorded video and frame thumbnails to inspect the part of the action you need.</p>
          </div>
        </article>

        <article class="story-step story-step-timing">
          <figure class="story-poster">
            <img src="./assets/timestamp-output.png" alt="SpeedLens review and process-output interface showing Track, Tag, and Crop modes plus crop and Tag and Timestamp output options.">
          </figure>
          <div class="story-copy">
            <span class="story-number">03</span>
            <h3>Turn review work into a focused output.</h3>
            <p>Use Track, Tag, and Crop tools, then choose crop and Tag &amp; Timestamp options for processed video output.</p>
          </div>
        </article>
      </div>
    </section>

```

- [ ] **Step 3: Constrain the hero poster instead of expanding it to the column width**

Replace the current `.hero-shot` and `.hero-shot img` rules with:

```css
.hero-shot {
  display: flex;
  justify-content: center;
  margin: 0;
}

.hero-shot img {
  display: block;
  width: auto;
  max-width: 100%;
  max-height: 680px;
  height: auto;
  border: 1px solid rgba(54, 215, 255, 0.24);
  border-radius: var(--radius-large);
  background: #071015;
  box-shadow: 0 36px 120px rgba(0, 0, 0, 0.5), 0 0 90px rgba(54, 215, 255, 0.1);
}
```

- [ ] **Step 4: Replace the workflow-card CSS with poster-story CSS**

Delete the rules from `.workflow-grid {` through `.workflow-card-timing figcaption strong { ... }` inclusive and insert:

```css
.story-list {
  display: grid;
  gap: clamp(72px, 10vw, 132px);
}

.story-step {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 0.72fr);
  align-items: center;
  gap: clamp(40px, 7vw, 96px);
}

.story-step-reverse .story-poster { order: 2; }
.story-step-reverse .story-copy { order: 1; }

.story-poster {
  display: flex;
  justify-content: center;
  margin: 0;
}

.story-poster img {
  display: block;
  width: auto;
  max-width: 100%;
  max-height: 760px;
  height: auto;
  border: 1px solid rgba(54, 215, 255, 0.18);
  border-radius: var(--radius-medium);
  background: #020506;
  box-shadow: 0 28px 90px rgba(0, 0, 0, 0.42);
}

.story-copy { max-width: 470px; }

.story-number {
  display: block;
  margin-bottom: 28px;
  color: var(--accent-strong);
  font-family: ui-monospace, "SFMono-Regular", Menlo, monospace;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.16em;
}

.story-copy h3 {
  margin-bottom: 20px;
  font-size: clamp(2rem, 3.2vw, 3.5rem);
}

.story-copy p {
  margin-bottom: 0;
  color: var(--muted);
  font-size: clamp(1.04rem, 1.5vw, 1.18rem);
}

.story-step-timing .story-number { color: var(--timing); }
```

- [ ] **Step 5: Update responsive poster behavior**

In `@media (max-width: 820px)`, replace:

```css
  .hero-shot { order: -1; }
  .feature-grid,
  .workflow-grid,
  .support-section { grid-template-columns: 1fr; }
```

with:

```css
  .hero-shot { order: -1; }
  .feature-grid,
  .support-section { grid-template-columns: 1fr; }
  .story-step { grid-template-columns: 1fr; gap: 30px; }
  .story-step-reverse .story-poster,
  .story-step-reverse .story-copy { order: initial; }
  .story-poster { order: -1; }
  .story-poster img { max-height: 640px; }
  .story-copy { max-width: 620px; }
```

In `@media (max-width: 560px)`, after `.hero { padding-top: 24px; }`, insert:

```css
  .hero-shot img,
  .story-poster img { width: 100%; max-height: none; }
  .story-list { gap: 76px; }
  .story-step { gap: 24px; }
  .story-number { margin-bottom: 18px; }
```

- [ ] **Step 6: Run validator, HTML parse, and claim guard to verify GREEN**

Run:

```bash
python3 speedlens/validate_site.py
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Parser(HTMLParser):
    pass

homepage = Path("speedlens/index.html").read_text(encoding="utf-8")
Parser().feed(homepage)
for forbidden in [
    "AI-powered",
    "automatic athlete identity recognition",
    "cloud backup",
    "guaranteed frame-rate",
]:
    assert forbidden not in homepage, forbidden
for required in [
    "How SpeedLens works",
    "Track, Tag, and Crop",
    "Tag &amp; Timestamp",
]:
    assert required in homepage, required
print("SpeedLens poster story checks passed")
PY
```

Expected:

```text
SpeedLens site validation passed
SpeedLens poster story checks passed
```

- [ ] **Step 7: Commit the homepage and stylesheet**

```bash
git add speedlens/index.html speedlens/styles.css
git commit -m "Present SpeedLens as a three-step product story"
```

---

### Task 3: Verify assets, routes, privacy, and change scope

**Files:**
- Verify: `speedlens/index.html`
- Verify: `speedlens/styles.css`
- Verify: `speedlens/validate_site.py`
- Verify unchanged: `speedlens/privacy-policy/index.html`
- Verify assets: `speedlens/assets/hero-capture.png`, `speedlens/assets/review-frame.png`, `speedlens/assets/timestamp-output.png`

**Interfaces:**
- Consumes: Tasks 1 and 2.
- Produces: a verified GitHub Pages-ready SpeedLens poster-story homepage.

- [ ] **Step 1: Run the validator fresh**

```bash
python3 speedlens/validate_site.py
```

Expected:

```text
SpeedLens site validation passed
```

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
for source in parser.sources:
    assert source.startswith("./"), source
    assert (root / source.removeprefix("./")).is_file(), source
assert parser.sources.count("./assets/hero-capture.png") == 2
assert parser.sources.count("./assets/review-frame.png") == 1
assert parser.sources.count("./assets/timestamp-output.png") == 1
print("SpeedLens poster image references passed")
PY
```

Expected:

```text
SpeedLens poster image references passed
```

- [ ] **Step 3: Verify privacy blob SHA remains unchanged**

Run:

```bash
git hash-object speedlens/privacy-policy/index.html
```

Expected:

```text
6228299fe1858ce3eb891d3d3d57fd1edc060fc7
```

- [ ] **Step 4: Start a local server and verify both routes and all three image assets**

Run:

```bash
python3 -m http.server 8000
```

Then in a second terminal:

```bash
set -euo pipefail
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/ >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/privacy-policy/ >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/assets/hero-capture.png >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/assets/review-frame.png >/dev/null
curl --fail --silent --show-error http://127.0.0.1:8000/speedlens/assets/timestamp-output.png >/dev/null
echo "SpeedLens poster routes passed"
```

Expected:

```text
SpeedLens poster routes passed
```

- [ ] **Step 5: Verify change scope from the approved poster-story design head**

Compare commit `42b8e6b9e6e0a6fbef5abc0e3ac8941f788d4261` to the final implementation head. Implementation paths must be limited to:

```text
speedlens/index.html
speedlens/styles.css
speedlens/validate_site.py
```

The plan document itself may also appear. `alwayson/` and `speedlens/privacy-policy/index.html` must not appear.
