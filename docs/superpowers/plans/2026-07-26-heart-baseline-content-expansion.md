# Heart Baseline Content Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two compact explanatory sections to the Heart Baseline product page so visitors understand why focused checks are useful and how the app workflow works.

**Architecture:** Extend the existing static HTML page with one text-led section and one three-step workflow section placed between the hero and the current feature grid. Add only page-specific CSS in `heart-baseline/styles.css`, reusing the shared typography, spacing, color tokens, and existing responsive breakpoints.

**Tech Stack:** Static HTML5, CSS Grid, existing shared CSS in `shared/app-base.css`, GitHub Pages.

## Global Constraints

- Preserve the existing dark Heart Baseline theme.
- Keep the change compact and visually calm; this is not a redesign.
- Add no screenshots, illustrations, icons, gradients, or new accent colors.
- Keep the existing medical disclaimer unchanged.
- Make no diagnosis, prediction, treatment, clinical-baseline, or medical-interpretation claims.
- Do not change the homepage, privacy policy, App Store link, release status, Google Analytics, or structured metadata.
- Ensure no horizontal overflow at desktop, tablet, or mobile widths.

---

### Task 1: Add the explanatory content structure

**Files:**
- Modify: `heart-baseline/index.html`, immediately after the closing `</section>` of the hero and before the existing `<section class="section shell" id="features">` block.

**Interfaces:**
- Consumes: Existing `.section`, `.shell`, `.section-heading`, and `.eyebrow` styles from `shared/app-base.css`.
- Produces: `.focused-checks-section`, `.workflow-section`, `.workflow-steps`, and `.workflow-step` elements styled in Task 2.

- [ ] **Step 1: Verify the current page lacks the new sections**

Inspect `heart-baseline/index.html` and confirm it contains neither `id="why-focused-checks"` nor `id="how-it-works"`.

Expected: both identifiers are absent.

- [ ] **Step 2: Insert the “Why focused checks” section**

Add this exact HTML after the hero:

```html
    <section class="section shell focused-checks-section" id="why-focused-checks" aria-labelledby="why-focused-checks-title">
      <div class="section-heading">
        <p class="eyebrow">Why focused checks</p>
        <h2 id="why-focused-checks-title">A deliberate moment, under more consistent conditions.</h2>
        <p>Apple Watch measures heart rate throughout the day, often while you are moving, resting, or doing different activities. Heart Baseline gives you a deliberate moment to sit still and capture a short check under more consistent conditions.</p>
      </div>
    </section>
```

- [ ] **Step 3: Insert the “How it works” section**

Add this exact HTML immediately after the focused-checks section:

```html
    <section class="section shell workflow-section" id="how-it-works" aria-labelledby="how-it-works-title">
      <div class="section-heading">
        <p class="eyebrow">How it works</p>
        <h2 id="how-it-works-title">From a quiet moment to a useful record.</h2>
      </div>
      <div class="workflow-steps">
        <article class="workflow-step">
          <span class="workflow-number">01</span>
          <h3>Choose a duration</h3>
          <p>Select a one-, two-, three-, or five-minute check.</p>
        </article>
        <article class="workflow-step">
          <span class="workflow-number">02</span>
          <h3>Capture with Apple Watch</h3>
          <p>Stay still while Apple Watch gathers heart-rate readings and iPhone mirrors the progress.</p>
        </article>
        <article class="workflow-step">
          <span class="workflow-number">03</span>
          <h3>Review on iPhone</h3>
          <p>Review the average, range, chart, individual readings, and daily context.</p>
        </article>
      </div>
    </section>
```

- [ ] **Step 4: Verify semantic order and unchanged release elements**

Confirm the page order is hero → why-focused-checks → how-it-works → features. Confirm the App Store URL remains `https://apps.apple.com/us/app/heart-baseline/id6790179236`, the text remains `Available on the App Store`, and the existing disclaimer text is unchanged.

- [ ] **Step 5: Commit the content change**

```bash
git add heart-baseline/index.html
git commit -m "feat: explain Heart Baseline focused checks"
```

### Task 2: Add compact responsive styling

**Files:**
- Modify: `heart-baseline/styles.css`, after the `.availability span` rule and before the existing `.hero-shot, .story-poster` block.

**Interfaces:**
- Consumes: `--line`, `--muted`, `--accent-strong`, existing section spacing, and the `820px` and `560px` breakpoints.
- Produces: A three-column workflow on wider screens and a single-column workflow on smaller screens.

- [ ] **Step 1: Confirm the workflow classes are currently unstyled**

Inspect `heart-baseline/styles.css` and confirm `.workflow-steps`, `.workflow-step`, and `.workflow-number` do not exist.

Expected: all three selectors are absent.

- [ ] **Step 2: Add the base section and workflow styles**

Insert:

```css
.focused-checks-section .section-heading {
  max-width: 820px;
}

.focused-checks-section .section-heading p:last-child {
  max-width: 72ch;
  margin-bottom: 0;
}

.workflow-section .section-heading {
  margin-bottom: clamp(28px, 4vw, 42px);
}

.workflow-steps {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: clamp(24px, 3vw, 38px);
  border-top: 1px solid var(--line);
}

.workflow-step {
  min-width: 0;
  padding-top: 24px;
}

.workflow-number {
  display: block;
  margin-bottom: 18px;
  color: var(--accent-strong);
  font-family: ui-monospace, "SFMono-Regular", Menlo, monospace;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.16em;
}

.workflow-step h3 {
  margin-bottom: 12px;
  font-size: clamp(1.35rem, 2vw, 1.85rem);
}

.workflow-step p {
  max-width: 34ch;
  margin-bottom: 0;
  color: var(--muted);
}
```

- [ ] **Step 3: Add tablet and mobile responsive behavior**

Inside the existing `@media (max-width: 820px)` block, add:

```css
  .workflow-steps {
    grid-template-columns: 1fr;
    gap: 0;
  }

  .workflow-step {
    padding-block: 24px;
    border-bottom: 1px solid var(--line);
  }

  .workflow-step:last-child {
    border-bottom: 0;
  }
```

Inside the existing `@media (max-width: 560px)` block, add:

```css
  .workflow-section .section-heading {
    margin-bottom: 24px;
  }
```

- [ ] **Step 4: Verify layout constraints**

Check that all grid columns use `minmax(0, 1fr)`, every workflow item has `min-width: 0`, body copy has bounded line lengths, and the mobile layout is one column. Confirm no width, transform, or negative margin is introduced by the new styles.

- [ ] **Step 5: Commit the style change**

```bash
git add heart-baseline/styles.css
git commit -m "style: add Heart Baseline workflow sections"
```

### Task 3: Final page verification

**Files:**
- Verify: `heart-baseline/index.html`
- Verify: `heart-baseline/styles.css`

**Interfaces:**
- Consumes: The completed HTML and CSS from Tasks 1 and 2.
- Produces: A deployable GitHub Pages update with no other product-page behavior changed.

- [ ] **Step 1: Validate required content**

Confirm the final HTML includes exactly one occurrence of each:

```text
id="why-focused-checks"
id="how-it-works"
class="workflow-steps"
Choose a duration
Capture with Apple Watch
Review on iPhone
```

- [ ] **Step 2: Validate protected content**

Confirm the final HTML still includes:

```text
G-66SH9RSJPW
https://apps.apple.com/us/app/heart-baseline/id6790179236
Available on the App Store
For general wellness and informational use.
```

- [ ] **Step 3: Validate responsive CSS**

Confirm the final CSS includes the three-column workflow rule, the `820px` single-column override, and no selector that changes the existing hero, story screenshots, disclaimer, or support layout beyond their current rules.

- [ ] **Step 4: Inspect the final commit diff**

The implementation diff must contain only:

```text
heart-baseline/index.html
heart-baseline/styles.css
```

The plan and design documentation commits are separate documentation-only changes.

- [ ] **Step 5: Record the final implementation commit**

Report the latest implementation commit SHA and summarize the two new sections and responsive behavior.
