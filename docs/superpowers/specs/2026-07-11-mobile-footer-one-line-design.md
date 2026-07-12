# One-Line Mobile Footer Design

## Goal

Keep the shared product footer on a single horizontal line on mobile across all pages that use `shared/app-base.css`.

## Scope

This is a shared CSS-only change. It applies to FitCycles, SpeedLens, AlwaysOn, and their privacy-policy pages through the existing `.site-footer` and `.footer-links` styles.

## Current Behavior

At `max-width: 560px`, `.site-footer` switches to `flex-direction: column`, which places the product name above the footer links. The footer therefore occupies multiple lines on mobile.

## Approved Design

Update the existing `@media (max-width: 560px)` block in `shared/app-base.css` so that:

- `.site-footer` remains a horizontal flex row.
- The product name and footer links are vertically centered.
- `justify-content: space-between` continues to keep the product name on the left and links on the right.
- The footer uses a smaller mobile gap and a slightly smaller font size where needed to fit at the repository's 320px minimum viewport.
- `.footer-links` uses `flex-wrap: nowrap`.
- Footer text and links do not wrap.

## Constraints

- Modify only `shared/app-base.css`.
- Do not change HTML, footer labels, links, routes, desktop behavior, or page-specific styles.
- Keep the existing mobile breakpoint at `560px`.
- Preserve accessibility and readable tap targets.
- Apply the fix directly to `main`, as approved by the user.

## Validation

- Verify the mobile media query no longer sets `.site-footer { flex-direction: column; }`.
- Verify `.site-footer` and `.footer-links` remain one line at widths down to 320px.
- Verify desktop footer behavior is unchanged.
- Run `python3 scripts/check_site.py`.
- Review the final diff to confirm only `shared/app-base.css` changed for the implementation.

## Out of Scope

- Redesigning footer content
- Hiding or abbreviating product names or links
- Changing header mobile behavior
- Per-product footer overrides
