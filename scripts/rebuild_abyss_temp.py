#!/usr/bin/env python3
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "alwayson/backgrounds/packages/abyss-bloom/1/assets"

PAIRS = [
    ("AbyssBloomLandscape", (1672, 941)),
    ("AbyssBloomPortrait", (941, 1672)),
]

# How much of the original bloom remains inside the local bloom region.
# Frame 2 intentionally preserves the original master exactly.
STATE_STRENGTH = [0.36, 0.68, 1.0, 0.30]


def focal_center(image: Image.Image) -> tuple[int, int]:
    """Estimate the luminous/saturated bloom center with a gentle center prior."""
    sample = image.convert("HSV")
    sample.thumbnail((180, 180), Image.Resampling.LANCZOS)
    w, h = sample.size
    pixels = sample.load()

    total = 0.0
    sx = 0.0
    sy = 0.0
    for y in range(h):
        ny = (y / max(1, h - 1) - 0.56) / 0.58
        for x in range(w):
            nx = (x / max(1, w - 1) - 0.50) / 0.62
            _, s, v = pixels[x, y]
            sat = s / 255.0
            val = v / 255.0
            prior = math.exp(-1.8 * (nx * nx + ny * ny))
            weight = max(0.0, sat - 0.12) * (0.20 + val ** 1.4) * (0.35 + 0.65 * prior)
            if weight > 0:
                total += weight
                sx += weight * x
                sy += weight * y

    if total <= 1e-6:
        return image.width // 2, int(image.height * 0.58)

    cx = sx / total / max(1, w - 1) * (image.width - 1)
    cy = sy / total / max(1, h - 1) * (image.height - 1)
    return int(round(cx)), int(round(cy))


def bloom_mask(size: tuple[int, int], center: tuple[int, int], portrait: bool) -> Image.Image:
    w, h = size
    cx, cy = center

    # Large, feathered region: background outside the bloom stays pixel-identical.
    if portrait:
        rx, ry = int(w * 0.39), int(h * 0.28)
    else:
        rx, ry = int(w * 0.31), int(h * 0.40)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=max(18, int(min(w, h) * 0.055))))
    return mask


def subdued_version(master: Image.Image) -> Image.Image:
    # Keep the original colors/texture; only lower bloom energy and detail.
    faded = ImageEnhance.Color(master).enhance(0.70)
    faded = ImageEnhance.Brightness(faded).enhance(0.70)
    soft = faded.filter(ImageFilter.GaussianBlur(radius=max(1.5, min(master.size) / 900)))
    return Image.blend(faded, soft, 0.28)


def render_states(master_path: Path, base_name: str, expected_size: tuple[int, int]) -> None:
    with Image.open(master_path) as src:
        master = src.convert("RGB")

    if master.size != expected_size:
        raise RuntimeError(
            f"{master_path.name}: expected original master {expected_size}, got {master.size}"
        )

    center = focal_center(master)
    mask = bloom_mask(master.size, center, portrait=master.height > master.width)
    faded = subdued_version(master)

    print(f"MASTER {master_path.name}: {master.width}x{master.height}, focal={center}")

    for index, strength in enumerate(STATE_STRENGTH):
        suffix = "" if index == 0 else str(index)
        output = ASSETS / f"{base_name}{suffix}.png"

        if index == 2:
            frame = master.copy()
        else:
            local = Image.blend(faded, master, strength)
            frame = Image.composite(local, master, mask)

            # Frame 3 is the quiet loop bridge; keep it slightly closer to frame 0.
            if index == 3:
                frame = ImageEnhance.Brightness(frame).enhance(0.985)

        if frame.size != expected_size:
            raise RuntimeError(f"Generated wrong size for {output.name}: {frame.size}")

        frame.save(output, format="PNG", optimize=True, compress_level=9)
        print(f"WROTE {output.name}: {frame.width}x{frame.height}")


def main() -> None:
    for base_name, expected_size in PAIRS:
        master_path = ASSETS / f"{base_name}.png"
        render_states(master_path, base_name, expected_size)


if __name__ == "__main__":
    main()
