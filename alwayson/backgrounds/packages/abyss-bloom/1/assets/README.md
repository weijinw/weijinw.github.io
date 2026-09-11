# Abyss Bloom assets

Abyss Bloom is a four-state ambient flower-opening loop derived from the original Abyss Bloom artwork. The frames are animation keyframes of one locked scene, not independently generated illustrations.

## Canonical canvases

The original base artwork defines the canonical canvas sizes for this package. Every frame in an orientation must use exactly the same size:

- Landscape: `1672 × 941`
- Portrait: `941 × 1672`

Do not upscale the sequence to `2560 × 1440` / `1440 × 2560` just to normalize dimensions. Preserving the original composition and pixel geometry is more important for this asset set.

Use PNG, sRGB, no embedded text. Keep the upper/central clock area subdued enough for foreground readability.

## Source artwork and sequence

Frame 2 is the untouched original Abyss Bloom artwork at full bloom. Frames 0, 1, and 3 are derived from that same source image with local geometric petal warps so the flowers visibly open and close while the background, crop, bloom centers, and surrounding structures stay fixed.

| Frame | Landscape | Portrait | Visual state |
| --- | --- | --- | --- |
| 0 | `AbyssBloomLandscape.png` | `AbyssBloomPortrait.png` | closed / compact bloom |
| 1 | `AbyssBloomLandscape1.png` | `AbyssBloomPortrait1.png` | partially open transition |
| 2 | `AbyssBloomLandscape2.png` | `AbyssBloomPortrait2.png` | original artwork, fully open |
| 3 | `AbyssBloomLandscape3.png` | `AbyssBloomPortrait3.png` | partially closing loop bridge |

The intended loop is:

`closed → opening → full bloom → closing → closed`

Frame 3 should bridge back toward frame 0 so the final crossfade is calm and difficult to notice.

## Composition lock

For all four frames of an orientation:

- Keep the camera, crop, background, flower centers, and surrounding structures fixed.
- Derive states from the same original master image; do not redraw or independently regenerate the scene.
- Preserve the original Abyss Bloom visual style, texture, color palette, and detail.
- Keep the central clock area and non-flower background unchanged wherever possible.
- Change the flowers through local petal geometry: fold/pull petals inward for closed states and progressively restore the original geometry as the bloom opens.
- Frame 2 must remain the original full-bloom artwork.
- Brightness or saturation changes may support the transition, but they must not be the only difference between frames.
- Avoid unrelated geometry changes that create doubled petals or moving background objects during a crossfade.
- Do not change canvas dimensions between states.

A useful review test is to compare normalized flower edges between frame 0 and frame 2. The petal contours should be visibly different, while static background structures and the clock area remain aligned.

## Timing

The package metadata uses this approximate rhythm:

- Frame 0 → 1: 5 s
- Frame 1 → 2: 6 s
- Frame 2 hold: 2 s
- Frame 2 → 3: 8 s
- Frame 3 hold: 1 s
- Frame 3 → 0: 3 s

Motion metadata is intentionally identical across frames so crossfades do not add independent camera drift on top of the bloom animation.
