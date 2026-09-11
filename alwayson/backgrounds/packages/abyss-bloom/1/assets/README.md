# Abyss Bloom assets

Abyss Bloom is a four-state ambient bloom loop derived from the original Abyss Bloom artwork. The frames are animation keyframes of one locked scene, not independently generated illustrations.

## Canonical canvases

The original base artwork defines the canonical canvas sizes for this package. Every frame in an orientation must use exactly the same size:

- Landscape: `1672 × 941`
- Portrait: `941 × 1672`

Do not upscale the sequence to `2560 × 1440` / `1440 × 2560` just to normalize dimensions. Preserving the original composition and pixel geometry is more important for this asset set.

Use PNG, sRGB, no embedded text. Keep the upper/central clock area subdued enough for foreground readability.

## Source artwork and sequence

The fully opened state is the original Abyss Bloom artwork. The other states are derived from those same source pixels so the background, crop, bloom center, and surrounding structures stay fixed.

| Frame | Landscape | Portrait | Visual state |
| --- | --- | --- | --- |
| 0 | `AbyssBloomLandscape.png` | `AbyssBloomPortrait.png` | subdued / faint bloom |
| 1 | `AbyssBloomLandscape1.png` | `AbyssBloomPortrait1.png` | brighter / opening transition |
| 2 | `AbyssBloomLandscape2.png` | `AbyssBloomPortrait2.png` | original artwork at full strength |
| 3 | `AbyssBloomLandscape3.png` | `AbyssBloomPortrait3.png` | subdued / fading loop bridge |

The intended loop is:

`faint → opening → full bloom → fade → faint`

Frame 3 should remain visually close to frame 0 so the final crossfade back to frame 0 is difficult to notice.

## Composition lock

For all four frames of an orientation:

- Keep the camera, crop, background, bloom center, and surrounding structures fixed.
- Derive states from the same original master image; do not redraw or independently regenerate the scene.
- Preserve the original Abyss Bloom visual style, texture, color palette, and detail.
- Keep background pixels unchanged wherever possible.
- Change bloom energy, brightness, saturation, softness, or local visibility rather than replacing the flower with a different shape.
- Avoid geometry changes that create doubled petals or objects during a crossfade.
- Do not change canvas dimensions between states.

A useful review test is to overlay adjacent frames at 50% opacity. Static edges should coincide exactly or nearly exactly, and the bloom should read as one object changing energy rather than two different illustrations.

## Timing

The package metadata uses this approximate rhythm:

- Frame 0 → 1: 5 s
- Frame 1 → 2: 6 s
- Frame 2 hold: 2 s
- Frame 2 → 3: 8 s
- Frame 3 hold: 1 s
- Frame 3 → 0: 3 s

Motion metadata is intentionally identical across frames so crossfades do not add independent camera drift on top of the bloom animation.
