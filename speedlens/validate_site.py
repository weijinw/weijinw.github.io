from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href is not None:
            self.links.append(href)


def require_file(path: Path, errors: list[str]) -> str:
    if not path.is_file():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def require_text(
    content: str, required: list[str], label: str, errors: list[str]
) -> None:
    for item in required:
        if item not in content:
            errors.append(f"{label} missing required text: {item}")


def require_links(
    content: str, required: list[str], label: str, errors: list[str]
) -> None:
    parser = LinkParser()
    parser.feed(content)
    for href in required:
        if href not in parser.links:
            errors.append(f"{label} missing required link: {href}")


def main() -> int:
    errors: list[str] = []

    homepage = require_file(ROOT / "index.html", errors)
    styles = require_file(ROOT / "styles.css", errors)
    policy = require_file(ROOT / "privacy-policy" / "index.html", errors)

    for asset_name in [
        "hero-capture.png",
        "review-frame.png",
        "timestamp-output.png",
    ]:
        asset_path = ROOT / "assets" / asset_name
        if not asset_path.is_file():
            errors.append(f"missing required file: {asset_path.relative_to(ROOT)}")

    require_text(
        homepage,
        [
            "SpeedLens",
            "Capture fast action. Find the moment that matters.",
            "Built for action, not social posting.",
            "Record sports video",
            "Review on your device",
            "Optional GPS metadata",
            "Need help?",
            "welkin.wong@gmail.com",
            "How SpeedLens works",
            "From capture to the highlight.",
            "Capture fast action with the subject in view.",
            "Move through the recording to find the moment.",
            "Turn review work into a focused output.",
            "Track, Tag, and Crop",
            "Tag &amp; Timestamp",
            'class="story-step"',
            'class="story-step story-step-reverse"',
            'class="story-step story-step-timing"',
            './assets/hero-capture.png',
            './assets/review-frame.png',
            './assets/timestamp-output.png',
        ],
        "homepage",
        errors,
    )
    require_links(
        homepage,
        ["./privacy-policy/", "mailto:welkin.wong@gmail.com"],
        "homepage",
        errors,
    )

    require_text(
        policy,
        [
            "Privacy Policy",
            "Information Collection and Use",
            "Third Party Access",
            "Opt-Out Rights",
            "Data Retention Policy",
            "Children",
            "Security",
            "Changes",
            "Your Consent",
            "Contact Us",
            "2026-07-06",
            "welkin.wong@gmail.com",
        ],
        "privacy policy",
        errors,
    )
    require_links(
        policy,
        ["../", "mailto:welkin.wong@gmail.com"],
        "privacy policy",
        errors,
    )

    require_text(
        styles,
        [
            "--accent: #36d7ff;",
            "--timing: #ff9d3d;",
            ".hero-shot",
            ".story-list",
            ".story-step",
            ".story-poster",
            ".story-step-reverse",
            "max-height: 680px;",
            "max-height: 760px;",
            "max-height: 640px;",
            "@media (max-width: 820px)",
            "@media (max-width: 560px)",
            "prefers-reduced-motion",
        ],
        "styles",
        errors,
    )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("SpeedLens site validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
