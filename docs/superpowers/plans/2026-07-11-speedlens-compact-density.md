# SpeedLens Compact Density Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce oversized typography and excessive vertical whitespace on the SpeedLens homepage without changing its content, section order, privacy page, poster assets, or the AlwaysOn site.

**Architecture:** Keep the existing static HTML and poster-story structure unchanged. Tighten the page entirely through `speedlens/styles.css`, while `speedlens/validate_site.py` becomes the regression contract for the approved compact type scales and spacing values and rejects the oversized values that caused the problem.

**Tech Stack:** HTML5, CSS, Python 3 standard library, GitHub Pages.

## Global Constraints

- This is a homepage density and typography pass only.
- Modify `speedlens/styles.css` and `speedlens/validate_site.py` only.
- Do not change `speedlens/index.html` content or structure.
- Do not change `speedlens/privacy-policy/index.html`.
- Do not change the three poster image assets.
- Do not modify any `alwayson/` file.
- Use the approved compact product page direction: reduce scale and spacing roughly 25–35% without turning the page into a dense utility dashboard.
- Preserve semantic HTML, keyboard focus states, dark-mode contrast, `prefers-reduced-motion`, relative links, and poster native aspect ratios.
- Add no JavaScript or animation changes.
- Preserve privacy-page visual typography; `.policy-intro` remains `clamp(1.04rem, 1.6vw, 1.2rem)`.

---

### Task 1: Lock the compact-density regression contract

**Files:**
- Modify: `speedlens/validate_site.py`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: the current `speedlens/styles.css`, homepage, privacy page, and existing asset paths.
- Produces: `python3 speedlens/validate_site.py` exits `0` only when the compact density values are present and the obsolete oversized homepage values are absent.

- [ ] **Step 1: Extend the stylesheet requirements with the approved compact values**

In `speedlens/validate_site.py`, replace the complete stylesheet requirement list inside the final `require_text(styles, [...])` call with exactly:

```python
        [
            "--accent: #36d7ff;",
            "--timing: #ff9d3d;",
            ".hero-shot",
            ".story-list",
            ".story-step",
            ".story-poster",
            ".story-step-reverse",
            "clamp(2.6rem, 4.4vw, 4.1rem)",
            "clamp(1.9rem, 3.2vw, 3.2rem)",
            "clamp(1.7rem, 2.5vw, 2.5rem)",
            "clamp(1rem, 1.25vw, 1.12rem)",
            "padding-block: clamp(40px, 5vw, 60px)",
            ".section { padding-block: 60px; }",
            "max-height: 560px;",
            "max-height: 620px;",
            "gap: clamp(44px, 6vw, 72px)",
            "margin-block: 20px 60px",
            "clamp(2.35rem, 11vw, 3.4rem)",
            ".policy-intro { color: var(--muted); font-size: clamp(1.04rem, 1.6vw, 1.2rem); }",
            "@media (max-width: 820px)",
            "@media (max-width: 560px)",
            "prefers-reduced-motion",
        ],
```

- [ ] **Step 2: Add an obsolete-density guard before the final `if errors:` block**

Insert exactly:

```python
    obsolete_density_values = [
        "min-height: min(700px, calc(100vh - 72px))",
        "clamp(3rem, 5.4vw, 5.6rem)",
        "clamp(2.2rem, 4vw, 4.35rem)",
        "clamp(2rem, 3.2vw, 3.5rem)",
        ".section { padding-block: 96px; }",
        "max-height: 680px;",
        "max-height: 760px;",
        "gap: clamp(72px, 10vw, 132px)",
        "min-height: 250px;",
    ]
    for value in obsolete_density_values:
        if value in styles:
            errors.append(f"styles still contain obsolete density value: {value}")
```

- [ ] **Step 3: Run the validator to verify RED**

Run:

```bash
python3 speedlens/validate_site.py
```

Expected: exit `1`. The output must contain missing-required-text errors for the new compact values and obsolete-density errors for the current large `h1`, `h2`, story heading, section padding, hero/story poster heights, story gap, and feature-card minimum height.

- [ ] **Step 4: Commit the density validator contract**

```bash
git add speedlens/validate_site.py
git commit -m "Validate SpeedLens compact density"
```

---

### Task 2: Compact the SpeedLens homepage typography and rhythm

**Files:**
- Modify: `speedlens/styles.css`
- Test: `speedlens/validate_site.py`

**Interfaces:**
- Consumes: the Task 1 validator contract and the existing unchanged `speedlens/index.html` structure.
- Produces: the same SpeedLens homepage hierarchy with smaller display type, shorter poster caps, denser sections/cards/story rows, and unchanged privacy typography.

- [ ] **Step 1: Compact the hero grid and display typography**

Replace:

```css
  gap: clamp(34px, 5vw, 72px);
  min-height: min(700px, calc(100vh - 72px));
  padding-block: clamp(54px, 7vw, 82px);
```

with:

```css
  gap: clamp(28px, 4vw, 52px);
  padding-block: clamp(40px, 5vw, 60px);
```

Replace:

```css
h1 { margin-bottom: 26px; font-size: clamp(3rem, 5.4vw, 5.6rem); font-weight: 650; }
h2 { margin-bottom: 20px; font-size: clamp(2.2rem, 4vw, 4.35rem); font-weight: 620; }
```

with:

```css
h1 { margin-bottom: 22px; font-size: clamp(2.6rem, 4.4vw, 4.1rem); font-weight: 650; }
h2 { margin-bottom: 16px; font-size: clamp(1.9rem, 3.2vw, 3.2rem); font-weight: 620; }
```

- [ ] **Step 2: Split homepage body-copy sizing from the privacy intro**

Replace:

```css
.hero-lede,
.section-heading > p:last-child,
.support-section p,
.policy-intro { color: var(--muted); font-size: clamp(1.04rem, 1.6vw, 1.2rem); }
```

with exactly:

```css
.hero-lede,
.section-heading > p:last-child,
.support-section p { color: var(--muted); font-size: clamp(1rem, 1.25vw, 1.12rem); }
.policy-intro { color: var(--muted); font-size: clamp(1.04rem, 1.6vw, 1.2rem); }
```

This keeps the privacy-page intro at its existing scale.

- [ ] **Step 3: Compact hero actions and the hero poster**

Replace:

```css
.hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 34px; }
```

with:

```css
.hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 24px; }
```

In `.hero-shot img`, replace:

```css
  max-height: 680px;
```

with:

```css
  max-height: 560px;
```

- [ ] **Step 4: Compact general sections and feature cards**

Replace:

```css
.section { padding-block: 96px; }
.section-heading { max-width: 760px; margin-bottom: 52px; }
```

with:

```css
.section { padding-block: 60px; }
.section-heading { max-width: 760px; margin-bottom: 32px; }
```

Replace the complete `.feature-card` block:

```css
.feature-card {
  min-height: 250px;
  padding: 30px;
  border: 1px solid var(--line);
  border-radius: var(--radius-medium);
  background: linear-gradient(145deg, var(--surface-strong), rgba(255, 255, 255, 0.02));
}
```

with:

```css
.feature-card {
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: var(--radius-medium);
  background: linear-gradient(145deg, var(--surface-strong), rgba(255, 255, 255, 0.02));
}
```

Replace:

```css
.feature-kicker { display: block; margin-bottom: 54px; color: var(--accent-strong); font-size: 0.76rem; font-weight: 700; letter-spacing: 0.16em; }
```

with:

```css
.feature-kicker { display: block; margin-bottom: 24px; color: var(--accent-strong); font-size: 0.76rem; font-weight: 700; letter-spacing: 0.16em; }
```

- [ ] **Step 5: Compact the three-step story**

Replace:

```css
.story-list {
  display: grid;
  gap: clamp(72px, 10vw, 132px);
}
```

with:

```css
.story-list {
  display: grid;
  gap: clamp(44px, 6vw, 72px);
}
```

In `.story-step`, replace:

```css
  gap: clamp(40px, 7vw, 96px);
```

with:

```css
  gap: clamp(32px, 5vw, 64px);
```

In `.story-poster img`, replace:

```css
  max-height: 760px;
```

with:

```css
  max-height: 620px;
```

In `.story-number`, replace:

```css
  margin-bottom: 28px;
```

with:

```css
  margin-bottom: 18px;
```

Replace:

```css
.story-copy h3 {
  margin-bottom: 20px;
  font-size: clamp(2rem, 3.2vw, 3.5rem);
}
```

with:

```css
.story-copy h3 {
  margin-bottom: 14px;
  font-size: clamp(1.7rem, 2.5vw, 2.5rem);
}
```

Replace the story-copy paragraph size:

```css
  font-size: clamp(1.04rem, 1.5vw, 1.18rem);
```

with:

```css
  font-size: clamp(1rem, 1.2vw, 1.1rem);
```

- [ ] **Step 6: Compact support and footer spacing**

In `.support-section`, replace:

```css
  margin-block: 28px 96px;
  padding: 44px;
```

with:

```css
  margin-block: 20px 60px;
  padding: 32px;
```

Delete this rule entirely:

```css
.support-section h2 { font-size: clamp(2.5rem, 4vw, 4rem); }
```

In `.site-footer`, replace:

```css
  padding-block: 30px 42px;
```

with:

```css
  padding-block: 24px 32px;
```

- [ ] **Step 7: Compact tablet and mobile rhythm**

In `@media (max-width: 820px)`, replace:

```css
  .story-step { grid-template-columns: 1fr; gap: 30px; }
```

with:

```css
  .story-step { grid-template-columns: 1fr; gap: 24px; }
```

Replace:

```css
  .story-poster img { max-height: 640px; }
```

with:

```css
  .story-poster img { max-height: 560px; }
```

Replace:

```css
  .support-section { padding: 32px; }
```

with:

```css
  .support-section { padding: 28px; }
```

In `@media (max-width: 560px)`, replace:

```css
  h1 { margin-bottom: 20px; font-size: clamp(2.65rem, 14vw, 4.2rem); }
```

with:

```css
  h1 { margin-bottom: 18px; font-size: clamp(2.35rem, 11vw, 3.4rem); }
```

Replace:

```css
  .section { padding-block: 70px; }
```

with:

```css
  .section { padding-block: 48px; }
```

Add immediately after that rule:

```css
  .story-list { gap: 44px; }
  .story-poster img { width: 100%; height: auto; max-height: none; }
```

Replace:

```css
  .feature-card { min-height: 220px; padding: 24px; }
```

with:

```css
  .feature-card { padding: 22px; }
```

Replace:

```css
  .support-section { margin-bottom: 72px; padding: 26px; }
```

with:

```css
  .support-section { margin-bottom: 52px; padding: 22px; }
```

- [ ] **Step 8: Run the validator and density guard to verify GREEN**

Run:

```bash
python3 speedlens/validate_site.py
python3 - <<'PY'
from pathlib import Path

styles = Path("speedlens/styles.css").read_text(encoding="utf-8")
for required in [
    "clamp(2.6rem, 4.4vw, 4.1rem)",
    "clamp(1.9rem, 3.2vw, 3.2rem)",
    "clamp(1.7rem, 2.5vw, 2.5rem)",
    "clamp(1rem, 1.25vw, 1.12rem)",
    "padding-block: clamp(40px, 5vw, 60px)",
    ".section { padding-block: 60px; }",
    "max-height: 560px;",
    "max-height: 620px;",
    "gap: clamp(44px, 6vw, 72px)",
    "margin-block: 20px 60px",
    "clamp(2.35rem, 11vw, 3.4rem)",
    ".policy-intro { color: var(--muted); font-size: clamp(1.04rem, 1.6vw, 1.2rem); }",
]:
    assert required in styles, required
for obsolete in [
    "min-height: min(700px, calc(100vh - 72px))",
    "clamp(3rem, 5.4vw, 5.6rem)",
    "clamp(2.2rem, 4vw, 4.35rem)",
    "clamp(2rem, 3.2vw, 3.5rem)",
    ".section { padding-block: 96px; }",
    "max-height: 680px;",
    "max-height: 760px;",
    "gap: clamp(72px, 10vw, 132px)",
    "min-height: 250px;",
]:
    assert obsolete not in styles, obsolete
print("SpeedLens compact density checks passed")
PY
```

Expected:

```text
SpeedLens site validation passed
SpeedLens compact density checks passed
```

- [ ] **Step 9: Commit the compact styling pass**

```bash
git add speedlens/styles.css
git commit -m "Compact SpeedLens page density"
```

---

### Task 3: Verify unchanged content, privacy, assets, routes, and scope

**Files:**
- Verify unchanged: `speedlens/index.html`
- Verify: `speedlens/styles.css`
- Verify: `speedlens/validate_site.py`
- Verify unchanged: `speedlens/privacy-policy/index.html`
- Verify unchanged: `speedlens/assets/hero-capture.png`
- Verify unchanged: `speedlens/assets/review-frame.png`
- Verify unchanged: `speedlens/assets/timestamp-output.png`

**Interfaces:**
- Consumes: Tasks 1 and 2.
- Produces: a verified Pages-ready SpeedLens homepage density pass with no content, privacy, asset, or AlwaysOn changes.

- [ ] **Step 1: Run the validator fresh**

```bash
python3 speedlens/validate_site.py
```

Expected:

```text
SpeedLens site validation passed
```

- [ ] **Step 2: Verify protected file hashes**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib

protected = {
    "speedlens/index.html": "60cb9c6d9283e1d86dcd94179719fd08a0897af9",
    "speedlens/privacy-policy/index.html": "6228299fe1858ce3eb891d3d3d57fd1edc060fc7",
}

# Git blob SHA = SHA1("blob <size>\\0" + bytes)
def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = f"blob {len(data)}\0".encode() + data
    return hashlib.sha1(payload).hexdigest()

for name, expected in protected.items():
    actual = git_blob_sha(Path(name))
    assert actual == expected, (name, actual, expected)
print("SpeedLens protected text blobs passed")
PY
```

Expected:

```text
SpeedLens protected text blobs passed
```

- [ ] **Step 3: Verify the three poster assets are unchanged from the pre-pass GitHub blob SHAs**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib

protected = {
    "speedlens/assets/hero-capture.png": "7bb3bad5967b502375475497c730f27eddf74204",
    "speedlens/assets/review-frame.png": "ae32011a74fe5f609f6eadd1fb2b953dc2813b4e",
    "speedlens/assets/timestamp-output.png": "ff83d379bd6cdeec161eac8a4ce7495a23d03b36",
}

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = f"blob {len(data)}\0".encode() + data
    return hashlib.sha1(payload).hexdigest()

for name, expected in protected.items():
    actual = git_blob_sha(Path(name))
    assert actual == expected, (name, actual, expected)
print("SpeedLens poster blobs passed")
PY
```

Expected:

```text
SpeedLens poster blobs passed
```

- [ ] **Step 4: Verify local Pages routes**

Run:

```bash
set -euo pipefail
python3 -m http.server 8000 --directory . >/tmp/speedlens-compact-http.log 2>&1 &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null || true' EXIT
curl --retry 10 --retry-connrefused --retry-delay 1 --fail http://127.0.0.1:8000/speedlens/ >/dev/null
curl --retry 10 --retry-connrefused --retry-delay 1 --fail http://127.0.0.1:8000/speedlens/privacy-policy/ >/dev/null
printf 'SpeedLens compact routes passed\n'
```

Expected final line:

```text
SpeedLens compact routes passed
```

- [ ] **Step 5: Verify GitHub change scope**

Compare the approved compact-density spec head to the final head:

```bash
git diff --name-only 4cb899be448ee263f6a0f9a14f15732272d38585..HEAD
```

Expected implementation paths are limited to:

```text
docs/superpowers/plans/2026-07-11-speedlens-compact-density.md
speedlens/styles.css
speedlens/validate_site.py
```

There must be no `speedlens/index.html`, `speedlens/privacy-policy/`, `speedlens/assets/`, or `alwayson/` path in the implementation diff.
