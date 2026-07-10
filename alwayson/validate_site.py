from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys


class PageInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.images: list[str] = []
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"] or "")
        if tag == "img" and attributes.get("src"):
            self.images.append(attributes["src"] or "")

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.text_parts.append(text)

    @property
    def text(self) -> str:
        return " ".join(self.text_parts)


def inspect_page(path: Path) -> PageInspector:
    inspector = PageInspector()
    inspector.feed(path.read_text(encoding="utf-8"))
    return inspector


def validate_homepage(root: Path) -> list[str]:
    errors: list[str] = []
    homepage = root / "index.html"
    stylesheet = root / "styles.css"
    preview = root / "assets" / "app-preview.png"

    for path in (homepage, stylesheet, preview):
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(root)}")

    if errors:
        return errors

    inspector = inspect_page(homepage)
    required_text = (
        "AlwaysOn Desk Clock",
        "A calm desk display for the iPhone you already own.",
        "Need help?",
        "welkin.wong@gmail.com",
    )
    for text in required_text:
        if text not in inspector.text:
            errors.append(f"homepage missing text: {text}")

    if "./privacy-policy/" not in inspector.links:
        errors.append("homepage must link to ./privacy-policy/")

    if "mailto:welkin.wong@gmail.com" not in inspector.links:
        errors.append("homepage must include support mailto link")

    required_images = (
        "./assets/app-preview.png",
        "./assets/edit-mode.png",
        "./assets/widget-gallery.png",
    )
    for image in required_images:
        if image not in inspector.images:
            errors.append(f"homepage must use {image}")

    return errors


def validate_privacy_policy(root: Path) -> list[str]:
    errors: list[str] = []
    policy = root / "privacy-policy" / "index.html"

    if not policy.is_file():
        return ["missing required file: privacy-policy/index.html"]

    inspector = inspect_page(policy)
    required_text = (
        "Privacy Policy",
        "Information Collection and Use",
        "Calendar",
        "Weather and Location",
        "Third-Party Services",
        "Data Retention and Deletion",
        "Your Choices",
        "Children",
        "Security",
        "Changes",
        "Contact Us",
        "July 10, 2026",
        "welkin.wong@gmail.com",
    )
    for text in required_text:
        if text not in inspector.text:
            errors.append(f"privacy policy missing text: {text}")

    if "../" not in inspector.links:
        errors.append("privacy policy must link back to ../")

    if "mailto:welkin.wong@gmail.com" not in inspector.links:
        errors.append("privacy policy must include contact mailto link")

    return errors


def validate_deployment(root: Path) -> list[str]:
    errors: list[str] = []
    readme = root / "README.md"
    workflow = root.parent / ".github" / "workflows" / "pages.yml"

    if not readme.is_file():
        errors.append("missing required file: README.md")
    if not workflow.is_file():
        errors.append("missing required file: ../.github/workflows/pages.yml")
        return errors

    workflow_text = workflow.read_text(encoding="utf-8")
    required_workflow_text = (
        'paths:',
        '"support/**"',
        'actions/configure-pages@v5',
        'actions/upload-pages-artifact@v4',
        'path: ./support',
        'actions/deploy-pages@v4',
        'pages: write',
        'id-token: write',
        'python3 support/validate_site.py',
    )
    for text in required_workflow_text:
        if text not in workflow_text:
            errors.append(f"pages workflow missing text: {text}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parent
    errors = [
        *validate_homepage(root),
        *validate_privacy_policy(root),
        *validate_deployment(root),
    ]
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("support site validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
