# SpeedLens Support Site Design

## Goal

Create a public SpeedLens product/support site inside `weijinw/weijinw.github.io` that matches the structural consistency and polish of the existing AlwaysOn Desk Clock site while giving SpeedLens its own camera, motion, and timing identity.

The site will replace the current Google Sites support presence once the new pages are verified and published.

## Site Structure

The SpeedLens site will live at:

```text
speedlens/
├── index.html
├── styles.css
├── assets/
└── privacy-policy/
    └── index.html
```

Published routes:

```text
https://weijinw.github.io/speedlens/
https://weijinw.github.io/speedlens/privacy-policy/
```

The app-specific folder keeps SpeedLens isolated from AlwaysOn and leaves room for additional app sites in sibling folders.

## Source Content

Before implementation, the source material for SpeedLens will be added to the repository by the user. This should include the current support/product copy, the current privacy-policy copy, and any screenshots or product images that should be reused.

The implementation will treat the supplied repository content as the source of truth. Copy will be reorganized and lightly edited for clarity, but factual claims and privacy statements will not be invented.

## Page Architecture

The homepage will follow the same information hierarchy used successfully by the AlwaysOn site:

1. Header with SpeedLens branding and Home / Privacy Policy navigation.
2. Product-first hero with a concise value proposition and primary product image.
3. Core-value section explaining why SpeedLens exists.
4. Feature cards focused on SpeedLens's real product capabilities.
5. Product screenshot section with two to four focused screenshots when suitable source images are available.
6. Support section with the support email address.
7. Footer with SpeedLens, Support, and Privacy Policy links.

The privacy-policy page will use the same navigation and footer structure while prioritizing readable long-form policy content.

## Visual Direction

The SpeedLens pages should feel related to the AlwaysOn site through typography, spacing discipline, rounded surfaces, restrained navigation, responsive behavior, and overall editorial quality.

SpeedLens will use its own visual identity:

- Near-black background.
- Electric cyan or cold blue as the primary accent.
- Warm timing orange as a restrained secondary accent where timing or frame-analysis details need emphasis.
- System / SF-style typography consistent with the existing site.
- Dark, high-contrast image treatment.
- Visual language inspired by video frames, motion, frame numbers, timing, and review tools.
- Tone: precise, fast, technical, and product-focused.

The page must not simply recolor the AlwaysOn page. Shared design principles are intentional, but SpeedLens should read as a distinct camera product.

## Content Principles

The homepage will emphasize concrete user value rather than generic camera-app language.

Potential feature groupings will be selected from the supplied source content and verified product capabilities, such as:

- High-frame-rate or sports-focused capture.
- Frame numbers and stopwatch/timestamp tools.
- Tracking or review workflow.
- Export or downstream analysis value.

Only capabilities supported by the supplied repository content or verified app behavior will be presented as shipping features.

## Privacy Policy

The SpeedLens privacy-policy page will be generated from the supplied SpeedLens policy content.

The implementation must preserve the policy's substantive meaning, including data-access, collection, retention, third-party service, and contact statements. Reformatting for readability is allowed; unsupported legal or privacy claims are not.

## Responsive and Accessibility Requirements

- Support desktop, tablet, and mobile layouts.
- Use semantic HTML landmarks and headings.
- Provide descriptive image `alt` text.
- Maintain visible keyboard focus states.
- Preserve readable contrast on the dark visual system.
- Keep navigation and support links usable on narrow screens.
- Respect `prefers-reduced-motion` for any transition or motion treatment.

## Implementation Constraints

- Plain static HTML and CSS.
- No JavaScript framework.
- No package manager or build system unless a later requirement clearly justifies one.
- No analytics or tracking.
- Use relative links so the site works correctly under `/speedlens/` on GitHub Pages.
- Do not modify the AlwaysOn site except where a deliberate shared-site navigation change is separately approved.

## Validation

Implementation verification should confirm:

- Homepage and privacy-policy files exist at the expected paths.
- Relative navigation links resolve correctly.
- Product image references point to committed assets.
- Support email links use `mailto:`.
- Privacy-policy headings and substantive content match the supplied policy source.
- Both `/speedlens/` and `/speedlens/privacy-policy/` are reachable in local static-server testing.
- Responsive CSS includes narrow-screen behavior and reduced-motion handling.

## Success Criteria

The result should be a production-ready public SpeedLens support site that:

- feels consistent with the developer's existing AlwaysOn site,
- has a clearly distinct SpeedLens identity,
- is ready for GitHub Pages hosting,
- provides a stable public support URL,
- provides a stable app-specific privacy-policy URL,
- and can replace the current Google Sites pages after verification.
