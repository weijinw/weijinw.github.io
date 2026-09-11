from __future__ import annotations

from pathlib import Path
import hashlib

import cv2
import numpy as np
from PIL import Image

ROOT = Path("alwayson/backgrounds/packages/abyss-bloom/1/assets")

SPECS = {
    "Landscape": [((285, 120), (350, 300)), ((1490, 760), (430, 360))],
    "Portrait": [((185, 140), (320, 340)), ((805, 1300), (360, 460))],
}

EXPECTED_SIZE = {
    "Landscape": (1672, 941),
    "Portrait": (941, 1672),
}

STATES = {
    "": 0.10,   # closed / compact
    "1": 0.48,  # partially open
    "3": 0.30,  # partially closing loop bridge
}

FLOWER_CROPS = {
    "Landscape": [(0, 0, 700, 400), (1050, 400, 1672, 941)],
    "Portrait": [(0, 0, 600, 500), (430, 850, 941, 1672)],
}


def pinch_flower(image: np.ndarray, center, radii, openness: float) -> np.ndarray:
    """Fold an existing bloom inward without moving the scene or replacing pixels."""
    h, w = image.shape[:2]
    cx, cy = center
    rx, ry = radii

    x0 = max(0, int(cx - rx))
    x1 = min(w, int(cx + rx) + 1)
    y0 = max(0, int(cy - ry))
    y1 = min(h, int(cy + ry) + 1)

    yy, xx = np.mgrid[y0:y1, x0:x1].astype(np.float32)
    dx = (xx - cx) / rx
    dy = (yy - cy) / ry
    radius = np.sqrt(dx * dx + dy * dy)
    inside = radius < 1.0

    # Inverse radial warp. Closed states sample from farther out in the original
    # bloom, pulling petal texture and contours inward. The warp decays to zero
    # at the ellipse boundary so the surrounding scene remains locked.
    scale = 0.66 + 0.34 * openness
    feather = np.clip(1.0 - radius * radius, 0.0, 1.0)
    factor = 1.0 + (1.0 / scale - 1.0) * (feather ** 1.15)

    map_x = cx + (xx - cx) * factor
    map_y = cy + (yy - cy) * factor
    map_x = np.where(inside, map_x, xx).astype(np.float32)
    map_y = np.where(inside, map_y, yy).astype(np.float32)

    warped = cv2.remap(
        image,
        map_x,
        map_y,
        interpolation=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REFLECT101,
    )

    # Feather the local morph into the untouched image. This avoids a visible
    # ellipse edge and keeps static background structures aligned.
    alpha = np.clip((1.0 - radius) / 0.14, 0.0, 1.0)
    alpha = (alpha * inside) ** 0.7
    alpha = alpha[..., None].astype(np.float32)

    original_patch = image[y0:y1, x0:x1].astype(np.float32)
    warped_patch = warped.astype(np.float32)
    mixed = original_patch * (1.0 - alpha) + warped_patch * alpha

    # Slightly quiet outer luminous petals as the bloom closes. Geometry remains
    # the primary change; this only helps the folded form read naturally.
    quiet = (1.0 - openness) * 0.12
    if quiet > 0:
        radial = np.clip((radius - 0.38) / 0.55, 0.0, 1.0) * (1.0 - radius)
        radial = np.clip(radial * 4.0, 0.0, 1.0) * inside
        luminance = original_patch.max(axis=2) / 255.0
        gate = np.clip((luminance - 0.12) / 0.45, 0.0, 1.0)
        mixed *= 1.0 - quiet * (radial * gate)[..., None]

    result = image.copy()
    result[y0:y1, x0:x1] = np.clip(mixed, 0, 255).astype(np.uint8)
    return result


def edge_correlation(path_a: Path, path_b: Path, crop) -> float:
    a = np.asarray(Image.open(path_a).convert("L"), dtype=np.float32) / 255.0
    b = np.asarray(Image.open(path_b).convert("L"), dtype=np.float32) / 255.0
    x0, y0, x1, y1 = crop
    a = a[y0:y1, x0:x1]
    b = b[y0:y1, x0:x1]
    a = (a - a.mean()) / (a.std() + 1e-6)
    b = (b - b.mean()) / (b.std() + 1e-6)
    ga = np.hypot(np.diff(a, axis=1)[:-1, :], np.diff(a, axis=0)[:, :-1])
    gb = np.hypot(np.diff(b, axis=1)[:-1, :], np.diff(b, axis=0)[:, :-1])
    return float(np.corrcoef(ga.ravel(), gb.ravel())[0, 1])


def main() -> None:
    full_bloom_sha = {}

    for orientation in ("Landscape", "Portrait"):
        full_path = ROOT / f"AbyssBloom{orientation}2.png"
        full_bloom_sha[orientation] = hashlib.sha256(full_path.read_bytes()).hexdigest()
        full = np.asarray(Image.open(full_path).convert("RGB"))

        if Image.open(full_path).size != EXPECTED_SIZE[orientation]:
            raise SystemExit(f"Unexpected full-bloom size for {orientation}")

        for suffix, openness in STATES.items():
            output = full.copy()
            for center, radii in SPECS[orientation]:
                output = pinch_flower(output, center, radii, openness)
            Image.fromarray(output).save(
                ROOT / f"AbyssBloom{orientation}{suffix}.png",
                format="PNG",
                optimize=True,
            )

    # Acceptance checks: all dimensions remain canonical, the original full-bloom
    # frame remains byte-identical, and the flower edges must differ enough to
    # prove this is a geometric opening rather than a brightness-only sequence.
    for orientation in ("Landscape", "Portrait"):
        for suffix in ("", "1", "2", "3"):
            path = ROOT / f"AbyssBloom{orientation}{suffix}.png"
            if Image.open(path).size != EXPECTED_SIZE[orientation]:
                raise SystemExit(f"Wrong size: {path}")

        full_path = ROOT / f"AbyssBloom{orientation}2.png"
        if hashlib.sha256(full_path.read_bytes()).hexdigest() != full_bloom_sha[orientation]:
            raise SystemExit(f"Full bloom changed: {orientation}")

        for crop in FLOWER_CROPS[orientation]:
            c0 = edge_correlation(
                ROOT / f"AbyssBloom{orientation}.png", full_path, crop
            )
            c1 = edge_correlation(
                ROOT / f"AbyssBloom{orientation}1.png", full_path, crop
            )
            c3 = edge_correlation(
                ROOT / f"AbyssBloom{orientation}3.png", full_path, crop
            )
            print(
                f"{orientation} crop={crop} edge-correlation "
                f"closed={c0:.3f} opening={c1:.3f} closing={c3:.3f}"
            )
            if c0 >= 0.85:
                raise SystemExit("Frame 0 is still too similar to full bloom")
            if not (c0 < c1 < 0.85):
                raise SystemExit("Frame 1 is not a geometric intermediate")
            if not (c0 < c3 < 0.85):
                raise SystemExit("Frame 3 is not a geometric closing bridge")


if __name__ == "__main__":
    main()
