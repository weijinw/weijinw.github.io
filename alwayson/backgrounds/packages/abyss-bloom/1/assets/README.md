# Abyss Bloom assets

Abyss Bloom is a four-state ambient bloom loop. The frames are animation keyframes of one locked scene, not four independently composed illustrations.

## Required canvases

Every frame in an orientation must use exactly the same canvas size:

- Landscape: `2560 × 1440`
- Portrait: `1440 × 2560`

Use PNG, sRGB, no embedded text. Keep the upper/central clock area subdued enough for foreground readability.

## Sequence

The four states are:

| Frame | Landscape | Portrait | Visual state |
| --- | --- | --- | --- |
| 0 | `AbyssBloomLandscape.png` | `AbyssBloomPortrait.png` | faint / small beginning bloom |
| 1 | `AbyssBloomLandscape1.png` | `AbyssBloomPortrait1.png` | partially opened bloom |
| 2 | `AbyssBloomLandscape2.png` | `AbyssBloomPortrait2.png` | fully opened / brightest bloom |
| 3 | `AbyssBloomLandscape3.png` | `AbyssBloomPortrait3.png` | dissolved / nearly faded loop bridge |

The intended loop is:

`faint → opening → full bloom → fade → faint`

Frame 3 should be visually close to frame 0 except that it may retain a larger, very low-energy residual glow. This makes the final crossfade back to frame 0 difficult to notice.

## Composition lock

For all four frames of an orientation:

- Keep the camera, crop, background, horizon, bloom center, and major surrounding structures fixed.
- Keep the same background pixels wherever possible.
- Change the bloom state rather than generating a new composition.
- The bloom may grow/open between frames 0–2, but its anchor point must not move.
- Frame 3 should fade/dissolve the frame-2 bloom without introducing a new shape or camera position.
- Avoid large geometry changes that create doubled objects during a crossfade.

When generating or editing frames, start from one master composition and derive the other states from it. Do not generate each frame independently.

A useful review test is to overlay adjacent frames at 50% opacity. Static background edges should nearly coincide and the bloom should read as one object changing state, not two different objects.

## Timing

The package metadata uses this approximate rhythm:

- Frame 0 → 1: 5 s
- Frame 1 → 2: 6 s
- Frame 2 hold: 2 s
- Frame 2 → 3: 8 s
- Frame 3 hold: 1 s
- Frame 3 → 0: 3 s

Motion metadata is intentionally identical across frames so crossfades do not add independent camera drift on top of the bloom animation.
