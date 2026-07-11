# Root Homepage Design

Date: 2026-07-10

## Goal

Add a polished repository-root homepage for `weijinw.github.io` so the root URL no longer returns 404 and visitors can discover the independent iOS apps hosted in this GitHub Pages repository.

The homepage presents a curated collection of useful, thoughtfully designed apps. It must not introduce a personal identity, studio name, company name, logo, or invented umbrella brand.

## Scope

Create only the root homepage assets needed for the new site entry point. Preserve the existing app sites and their routes:

- `./speedlens/`
- `./alwayson/`

Do not modify their HTML, CSS, privacy pages, or existing assets unless a later implementation issue proves a root-page requirement cannot otherwise be met.

## Visual Direction

Use the approved **Direction A: Editorial app collection**.

The root page uses a warm, light neutral background and restrained dark typography. It should feel calm, premium, and editorial rather than like a generic startup landing page.

The page itself stays visually neutral. App identity comes from existing product artwork and one restrained accent color per card:

- SpeedLens: cyan-blue derived from the existing product site (`#36d7ff`).
- AlwaysOn Desk Clock: violet derived from the existing product site (`#7d83ff`).

Avoid gradients, glow effects, glassmorphism, floating decorative shapes, stock imagery, fake device mockups, and elaborate animation. Use subtle 1px borders, restrained shadows, strong typography, and generous but not excessive whitespace.

## Page Structure

### Header

A compact header approximately 64px tall.

- No brand name or logo.
- `Apps` anchor linking to the app showcase.
- `Support` email link to `mailto:welkin.wong@gmail.com`.

The header should remain simple and visually quiet.

### Hero

Use the exact heading:

> Small apps. Thoughtfully made.

Supporting copy explains that these are focused apps designed for everyday use. The copy must be modest and factual, with no exaggerated claims.

The hero should be compact rather than viewport-height: approximately 320–400px on desktop, with a desktop heading around 64px and a mobile heading around 42px.

Do not add a hero illustration, newsletter form, testimonials, pricing, founder biography, statistics, or extra calls to action.

### App Showcase

Use a responsive section with repeated semantic `<article class="app-card">` structures so another app can be added later by duplicating one article and assigning its accent variable.

Each card contains product artwork, product status, app name, description, and explicit actions. The entire card is not a single giant link.

#### SpeedLens

Status: `Available on the App Store`

Description:

> A focused iPhone camera for recording sports video and reviewing clips on-device.

Use existing artwork from `./speedlens/assets/hero-capture.png`.

Links:

- Product: `./speedlens/`
- Privacy: `./speedlens/privacy-policy/`
- App Store: `https://apps.apple.com/us/app/speedlens/id6787802030`

The primary action is an active `Download on the App Store` link. It must clearly identify the App Store destination, open in a new tab, and use safe external-link attributes.

Desktop layout: text on the left and artwork on the right.

#### AlwaysOn Desk Clock

Status: `Coming soon`

Description:

> Turns an iPhone into a calm, customizable desk display for time, calendar, weather, and upcoming events.

Use existing artwork from `./alwayson/assets/app-preview.png`.

Links:

- Product: `./alwayson/`
- Privacy: `./alwayson/privacy-policy/`

Do not add an App Store link. `Coming soon` is a static, non-interactive status treatment and must not look like a button.

Desktop layout: artwork on the left and text on the right, creating an alternating editorial rhythm.

### Footer

Use a minimal footer with explicit links for:

- SpeedLens
- SpeedLens privacy
- AlwaysOn Desk Clock
- AlwaysOn privacy
- Support email

Do not add copyright ownership language that introduces a studio or company identity.

## Responsive Behavior

### Approximately 1440px

- Constrain content to a comfortable editorial max width.
- Show each app card as a large two-column composition.
- Artwork occupies approximately 45–50% of each card.
- Alternate artwork/text order between the two cards.

### Approximately 768px

- Convert cards to balanced stacked layouts.
- Preserve readable spacing and strong artwork presence.
- Keep explicit actions easy to identify and tap.

### Approximately 375px

- Stack all content in a single column.
- Artwork appears first in each card, followed by status, title, description, and actions.
- Prevent horizontal overflow.
- Allow action groups to wrap cleanly.
- Maintain touch-friendly target sizing.

## Interaction and Accessibility

- Meet WCAG AA contrast requirements for text and interactive elements.
- Provide a clearly visible 2px keyboard focus treatment with suitable offset.
- Use descriptive image alt text based on the actual existing product artwork.
- Use semantic landmarks and heading hierarchy.
- Apply refined hover states to links and cards.
- Card hover movement is limited to approximately 2–3px.
- Do not rely on hover to reveal information.
- Respect `prefers-reduced-motion`; disable nonessential transitions and hover movement when reduced motion is requested.
- The `Coming soon` status is non-interactive and visually distinct from links/buttons.

## Technical Design

Use plain semantic HTML and CSS. No JavaScript or dependencies are required.

Create root-scoped files:

- `./index.html`
- `./styles.css`

The root CSS is isolated from the two product sites. Existing `speedlens/styles.css` and `alwayson/styles.css` remain unchanged.

Use only relative URLs for internal navigation and assets so local previews and GitHub Pages work consistently.

The document head includes:

- a descriptive `<title>`
- a meta description
- a canonical `<link>` for `https://weijinw.github.io/`
- Open Graph title, description, type, and `og:url` metadata for the public GitHub Pages root

The repository has no neutral existing favicon. Do not invent a logo, reuse either app's identity as the collection identity, or add a broken favicon reference. The root page intentionally omits a custom favicon declaration until a neutral favicon asset exists.

No build process is introduced.

## Link and Failure Handling

Because this is a static page, there is no runtime error state or data flow.

Implementation must avoid fragile links:

- Internal product and privacy links are relative and verified against existing repository paths.
- The SpeedLens App Store URL is used exactly as supplied and verified before completion.
- AlwaysOn contains no App Store link.
- Missing decorative assets must not be invented. If the selected existing artwork is unavailable at implementation time, omit the artwork rather than introduce stock imagery or a fake mockup.

## Validation

Before completion:

1. Confirm root `index.html` exists on the target branch and is the GitHub Pages root entry point.
2. Confirm `./speedlens/` resolves.
3. Confirm `./speedlens/privacy-policy/` resolves.
4. Confirm `./alwayson/` resolves.
5. Confirm `./alwayson/privacy-policy/` resolves.
6. Confirm the SpeedLens App Store URL is `https://apps.apple.com/us/app/speedlens/id6787802030`.
7. Confirm the SpeedLens card has the App Store CTA.
8. Confirm the AlwaysOn card has no App Store URL or CTA.
9. Check visual layouts at approximately 375px, 768px, and 1440px.
10. Check keyboard navigation and visible focus styles.
11. Check reduced-motion behavior.
12. Confirm existing app-site files and unrelated repository content were not changed.

## Success Criteria

The repository root loads a polished, lightweight product index instead of 404. Visitors can understand the collection, discover both apps, reach each product and privacy page, download SpeedLens from the correct App Store listing, and contact support. The design remains easy to extend with future app cards without introducing a framework or umbrella brand.