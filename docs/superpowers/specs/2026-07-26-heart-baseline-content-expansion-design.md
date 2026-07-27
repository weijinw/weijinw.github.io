# Heart Baseline Product Page: Light Content Expansion

## Goal

Expand the Heart Baseline product page just enough to explain the product idea and workflow more clearly, while preserving the page's calm, compact visual character.

The page should remain conversion-oriented and easy to scan. This is a small content improvement, not a redesign.

## Scope

Add two new sections between the hero and the existing `Focused by design` feature section:

1. `Why focused checks`
2. `How it works`

No new screenshots, illustrations, navigation changes, FAQ, requirements section, or privacy section are included in this iteration.

## Page Order

1. Existing hero
2. New `Why focused checks` section
3. New `How it works` section
4. Existing `Focused by design` feature grid
5. Existing screenshot story section
6. Existing medical disclaimer
7. Existing support section

## Section 1: Why Focused Checks

### Purpose

Explain why Heart Baseline exists and distinguish intentional checks from passive heart-rate readings without making medical claims.

### Content direction

The section should explain that Apple Watch gathers heart-rate readings throughout the day under changing conditions, while Heart Baseline lets the user deliberately pause, stay still, and capture a short check under more consistent conditions.

Suggested copy:

> Apple Watch measures heart rate throughout the day, often while you are moving, resting, or doing different activities. Heart Baseline gives you a deliberate moment to sit still and capture a short check under more consistent conditions.

### Presentation

- Text-led section
- Reuse the existing section heading pattern
- Keep the body copy to one short paragraph
- No card container or additional illustration

## Section 2: How It Works

### Purpose

Make the complete workflow understandable within a few seconds.

### Steps

1. **Choose a duration**
   Select a one-, two-, three-, or five-minute check.

2. **Capture with Apple Watch**
   Stay still while Apple Watch gathers heart-rate readings and iPhone mirrors the progress.

3. **Review on iPhone**
   Review the average, range, chart, individual readings, and daily context.

### Presentation

- Three compact steps in a horizontal row on larger screens
- Stack vertically on narrow screens
- Use simple step numbers and text
- Reuse existing typography, spacing, borders, and responsive breakpoints
- Avoid introducing a visually heavy card treatment

## Visual Direction

- Preserve the existing dark Heart Baseline theme
- Reuse current spacing and typography tokens
- Maintain generous whitespace
- Keep the new sections visually quieter than the screenshot story section
- Avoid icons, illustrations, gradients, or new accent colors

## Content and Safety Constraints

- Describe the app as a general wellness and informational tool
- Do not imply diagnosis, prediction, treatment, or medical interpretation
- Do not claim that a focused check establishes a clinical baseline
- Describe results factually: average, minimum, maximum, range, samples, chart, and daily context
- Keep the existing medical disclaimer unchanged

## Files Expected to Change

- `heart-baseline/index.html`
- `heart-baseline/styles.css`

No homepage or privacy-policy changes are required.

## Responsive Behavior

- Desktop and tablet: the three workflow steps appear in one row when space allows
- Mobile: workflow steps stack into one column
- New text must not create horizontal overflow
- Existing hero, screenshots, and actions remain unchanged

## Verification

After implementation:

- Confirm both sections appear between the hero and existing feature grid
- Confirm the App Store link and current release status remain unchanged
- Check desktop, tablet, and mobile layouts
- Confirm no horizontal overflow
- Confirm heading hierarchy remains logical
- Confirm the new copy makes no medical claims
- Confirm Google Analytics and existing structured metadata remain intact

## Out of Scope

- Expanded privacy explanation
- Usage examples such as morning or bedtime checks
- Device and permission requirements
- FAQ
- Additional App Store call to action
- New screenshots
- Homepage content changes
