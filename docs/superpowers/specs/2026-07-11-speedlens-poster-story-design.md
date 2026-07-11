# SpeedLens Poster Story Design

## Goal

Reframe the three existing SpeedLens marketing images as the primary product story on the homepage instead of displaying them as full-width screenshots or generic screenshot cards.

## Scope

This change affects only the SpeedLens homepage layout and its homepage-specific styles and validation. The SpeedLens privacy-policy page and the AlwaysOn site remain unchanged.

Existing assets are used as-is:

- `speedlens/assets/hero-capture.png`
- `speedlens/assets/review-frame.png`
- `speedlens/assets/timestamp-output.png`

No image editing, cropping, recompression, or replacement is part of this change.

## Product Story

The homepage keeps the existing SpeedLens header, product positioning, feature cards, support section, and footer. The three portrait marketing posters become a sequential product narrative.

The page flow is:

1. Header.
2. Hero with product positioning and the `Capture & Track` poster.
3. Existing core-value section.
4. Existing feature-card section.
5. `How SpeedLens works` three-step story.
6. Support section.
7. Footer.

The current two-card screenshot section is removed.

`hero-capture.png` intentionally appears in both the hero and story step 01. The hero uses it as the immediate product visual; step 01 reuses it to anchor the complete capture → review → export sequence. No other poster is duplicated.

## Hero

The hero remains a two-column layout on desktop.

The left column keeps the current hero copy and actions:

- `Sports video, focused`
- `Capture fast action. Find the moment that matters.`
- Current hero description.
- `See how it works` and `Get support` actions.

The right column displays `hero-capture.png` as a centered portrait marketing poster.

The poster must retain its complete artwork and native aspect ratio. It must not be stretched to fill the column or cropped with `object-fit: cover`.

Desktop hero poster presentation:

- `max-height: 680px`
- `width: auto`
- `max-width: 100%`
- centered in its column

The cyan border/glow treatment remains restrained so the poster itself stays dominant.

On tablet and mobile, the poster appears above the hero copy. On mobile it may use `width: 100%` and natural height because the viewport width constrains the poster appropriately.

## Three-Step Product Story

Add a section after the existing feature cards with the eyebrow `How SpeedLens works` and heading `From capture to the highlight.`

The story contains three numbered rows.

### 01 — Capture & Track

Image:

`hero-capture.png`

Copy:

**Capture fast action with the subject in view.**

`Keep camera controls close at hand and see the tracked subject directly in the capture frame.`

Desktop layout: poster left, copy right.

### 02 — Record & Review

Image:

`review-frame.png`

Copy:

**Move through the recording to find the moment.**

`Review recorded video and frame thumbnails to inspect the part of the action you need.`

Desktop layout: copy left, poster right.

### 03 — Export Highlights

Image:

`timestamp-output.png`

Copy:

**Turn review work into a focused output.**

`Use Track, Tag, and Crop tools, then choose crop and Tag & Timestamp options for processed video output.`

Desktop layout: poster left, copy right.

The third step may use the existing warm timing-orange accent for its step number or small detail. Orange must remain secondary to the cyan SpeedLens identity.

## Poster Presentation

The marketing images are portrait posters with their own embedded headings and device frames. The website must treat them as finished artwork rather than raw screenshots.

For all three story posters on desktop:

- preserve native aspect ratio
- `max-height: 760px`
- `width: auto`
- `max-width: 100%`
- center within the image column
- no forced equal-height crops
- no duplicate captions directly under the image

The adjacent copy explains product behavior. It must not repeat the poster's baked-in title as a large competing heading.

Poster containers may use a subtle surface, border, and glow consistent with the existing SpeedLens site. The container must not add a large empty framed rectangle around the narrow poster.

## Responsive Behavior

At widths above `820px`, each story row uses two columns with alternating image/copy placement.

At `820px` and below:

- each story row becomes one column
- poster appears before copy for all three steps, regardless of desktop alternation
- story poster `max-height` becomes `640px`
- story copy stays left aligned

At `560px` and below:

- poster width becomes `100%`
- height remains automatic
- no fixed or minimum poster height
- story row spacing is reduced to fit the existing mobile rhythm

## Accessibility

Each poster remains a real `<img>` with descriptive `alt` text.

Alt text must describe the product UI shown rather than repeat the baked-in poster headline:

- Capture poster: `SpeedLens capture interface showing camera controls and a tracked skateboarder.`
- Review poster: `SpeedLens recorded-video review interface with playback controls and frame thumbnails.`
- Export poster: `SpeedLens review and process-output interface showing Track, Tag, and Crop modes plus crop and Tag and Timestamp output options.`

The surrounding text provides the product explanation, so alt text should stay factual and concise.

## Product-Claim Boundaries

Homepage copy may describe behavior supported by the current SpeedLens source:

- camera capture controls
- tracked-subject overlay during capture
- recorded-video review
- frame timeline / frame selection
- Track, Tag, and Crop review modes
- crop-to-tracked-subject output option
- Include Tag & Timestamp output option

The page must not add unsupported claims such as AI-powered tracking, automatic athlete identity recognition, cloud backup, or guaranteed frame-rate performance.

## Validation

Extend `speedlens/validate_site.py` so the site fails validation unless:

- the hero references `hero-capture.png`
- the three-step section contains `How SpeedLens works`
- the three step numbers `01`, `02`, and `03` are present
- all three product images are referenced in the story
- the story contains `Track, Tag, and Crop`
- the story contains `Tag &amp; Timestamp` in HTML source
- the stylesheet contains the poster-story layout hooks and responsive breakpoint rules

Final verification must also confirm:

- `speedlens/privacy-policy/index.html` is unchanged
- no `alwayson/` file is modified
- all relative image references resolve to committed files
- `/speedlens/` and `/speedlens/privacy-policy/` return HTTP 200 from a local static server

## Non-Goals

This change does not:

- edit the poster artwork
- add JavaScript or animation
- create an image carousel
- add App Store badges or download links
- change privacy wording
- change the global multi-app site structure
- modify the AlwaysOn site
