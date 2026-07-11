# SpeedLens Compact Density Design

## Goal

Reduce the SpeedLens homepage's oversized typography and excessive vertical whitespace while preserving the approved three-step capture → review → export story and the current product content.

## Scope

This is a homepage density and typography pass only.

Modify:

- `speedlens/styles.css`
- `speedlens/validate_site.py` only as needed to validate the new density contract

Do not change:

- `speedlens/index.html` content or structure
- `speedlens/privacy-policy/index.html`
- poster image assets
- any `alwayson/` file

## Direction

Use the approved **compact product page** direction: reduce scale and spacing roughly 25–35% without turning the page into a dense utility dashboard.

The page should feel faster, more technical, and more appropriate for SpeedLens while retaining the current visual hierarchy.

## Typography

Reduce the large display type ranges:

- Hero `h1`: from `clamp(3rem, 5.4vw, 5.6rem)` to `clamp(2.6rem, 4.4vw, 4.1rem)`.
- Section `h2`: from `clamp(2.2rem, 4vw, 4.35rem)` to `clamp(1.9rem, 3.2vw, 3.2rem)`.
- Story `h3`: from `clamp(2rem, 3.2vw, 3.5rem)` to `clamp(1.7rem, 2.5vw, 2.5rem)`.
- Support-section `h2`: use the general `h2` scale instead of a larger `2.5rem`–`4rem` override.

Body copy remains readable and should only be reduced slightly:

- Hero, section-heading, support, and policy-intro large body copy: change to `clamp(1rem, 1.25vw, 1.12rem)`.
- Story copy: change to `clamp(1rem, 1.2vw, 1.1rem)`.

The policy page is not a visual target for this pass. Shared type rules may affect its inherited `h2` only where the policy page already has a more specific override; policy-specific sizing remains unchanged.

## Hero Density

Remove the forced hero minimum height.

Change the hero from:

- `min-height: min(700px, calc(100vh - 72px))`
- `padding-block: clamp(54px, 7vw, 82px)`

To:

- no `min-height`
- `padding-block: clamp(40px, 5vw, 60px)`

Reduce the hero grid gap from `clamp(34px, 5vw, 72px)` to `clamp(28px, 4vw, 52px)`.

Reduce the hero actions top margin from `34px` to `24px`.

Reduce the hero poster maximum height from `680px` to `560px`.

The hero remains two columns on desktop and poster-first on tablet/mobile.

## Section Rhythm

Reduce general section padding from `96px` to `60px`.

Reduce `.section-heading` bottom margin from `52px` to `32px`.

Keep all existing section order and content.

## Feature Cards

Remove the artificial card height:

- delete `min-height: 250px`

Reduce card padding from `30px` to `24px`.

Reduce the feature number bottom margin from `54px` to `24px`.

Keep the current two-column desktop and one-column mobile behavior.

Do not remove feature cards in this pass.

## Three-Step Story Density

Reduce the story-list gap from `clamp(72px, 10vw, 132px)` to `clamp(44px, 6vw, 72px)`.

Reduce the story-step column gap from `clamp(40px, 7vw, 96px)` to `clamp(32px, 5vw, 64px)`.

Reduce story poster maximum height from `760px` to `620px`.

Reduce story number bottom margin from `28px` to `18px`.

Reduce story-heading bottom margin from `20px` to `14px`.

Keep the alternating desktop placement and poster-first tablet/mobile layout.

At `820px` and below:

- story gap between poster and copy becomes `24px`
- poster maximum height becomes `560px`

At `560px` and below:

- poster remains `width: 100%`
- height remains automatic
- story-list gap becomes `44px`
- section padding becomes `48px`

## Support and Footer Density

Reduce support-section outer spacing from `margin-block: 28px 96px` to `margin-block: 20px 60px`.

Reduce support padding from `44px` to `32px` on desktop.

At `820px` and below, reduce support padding from `32px` to `28px`.

At `560px` and below, reduce support padding from `26px` to `22px` and bottom margin from `72px` to `52px`.

Reduce footer vertical padding from `30px 42px` to `24px 32px`.

## Responsive Typography

The current mobile `h1` override `clamp(2.65rem, 14vw, 4.2rem)` is still too large. Replace it with:

`clamp(2.35rem, 11vw, 3.4rem)`.

Do not add a mobile `h2` override unless the general scale proves insufficient; YAGNI for this pass.

## Accessibility and Behavior

Preserve:

- semantic HTML
- current keyboard focus states
- readable dark-mode contrast
- `prefers-reduced-motion`
- all current relative links
- the poster images' native aspect ratios

No JavaScript or animation changes are part of this work.

## Validation

Extend `speedlens/validate_site.py` so the stylesheet must contain the new compact-density values:

- `clamp(2.6rem, 4.4vw, 4.1rem)`
- `clamp(1.9rem, 3.2vw, 3.2rem)`
- `clamp(1.7rem, 2.5vw, 2.5rem)`
- `padding-block: clamp(40px, 5vw, 60px)`
- `.section { padding-block: 60px; }`
- `max-height: 560px;`
- `max-height: 620px;`
- `gap: clamp(44px, 6vw, 72px)`
- `margin-block: 20px 60px`
- `clamp(2.35rem, 11vw, 3.4rem)`

Validation must also guard against the obsolete density values that caused the current problem:

- `min-height: min(700px, calc(100vh - 72px))`
- `clamp(3rem, 5.4vw, 5.6rem)`
- `clamp(2.2rem, 4vw, 4.35rem)`
- `clamp(2rem, 3.2vw, 3.5rem)`
- `.section { padding-block: 96px; }`
- `max-height: 680px;`
- `max-height: 760px;`
- `gap: clamp(72px, 10vw, 132px)`
- `min-height: 250px;`

Final verification must confirm:

- `speedlens/index.html` is unchanged
- `speedlens/privacy-policy/index.html` is unchanged
- the three PNG assets are unchanged
- no `alwayson/` file is modified
- `python3 speedlens/validate_site.py` passes
- `/speedlens/` and `/speedlens/privacy-policy/` return HTTP 200 from a local static server

## Non-Goals

This pass does not:

- change homepage copy
- change homepage section order
- remove the feature cards
- alter poster artwork
- add App Store links
- add JavaScript
- redesign the privacy page
- modify the AlwaysOn site
