#!/usr/bin/env python3
from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", ".github", "__pycache__"}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, int]] = []
        self.resources: list[tuple[str, int]] = []
        self.ids: set[str] = set()
        self.images: list[tuple[dict[str, str], int]] = []
        self.has_title = False
        self.has_description = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        line, _ = self.getpos()

        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)

        if tag == "a" and values.get("href"):
            self.links.append((values["href"], line))
        elif tag == "img" and values.get("src"):
            self.resources.append((values["src"], line))
            self.images.append((values, line))
        elif tag == "link" and values.get("href"):
            self.resources.append((values["href"], line))
        elif tag == "script" and values.get("src"):
            self.resources.append((values["src"], line))
        elif tag == "title":
            self.has_title = True
        elif (
            tag == "meta"
            and values.get("name", "").lower() == "description"
            and values.get("content")
        ):
            self.has_description = True


def iter_files(pattern: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(pattern)
        if not any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts)
    )


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


def resolve_target(source: Path, raw_url: str) -> tuple[Path | None, str]:
    parts = urlsplit(raw_url)
    if parts.scheme.lower() in EXTERNAL_SCHEMES or parts.netloc:
        return None, ""
    if not parts.path:
        return source, unquote(parts.fragment)

    decoded_path = unquote(parts.path)
    if decoded_path.startswith("/"):
        target = ROOT / decoded_path.lstrip("/")
    else:
        target = source.parent / decoded_path

    target = target.resolve()
    if decoded_path.endswith("/") or target.is_dir():
        target = target / "index.html"

    return target, unquote(parts.fragment)


def validate_html() -> tuple[list[str], dict[Path, PageParser]]:
    errors: list[str] = []
    pages: dict[Path, PageParser] = {}

    for path in iter_files("*.html"):
        parser = parse_page(path)
        pages[path.resolve()] = parser
        relative = path.relative_to(ROOT)

        if not parser.has_title:
            errors.append(f"{relative}: missing <title>")
        if not parser.has_description:
            errors.append(f"{relative}: missing meta description")

        for attrs, line in parser.images:
            for required in ("alt", "width", "height"):
                if not attrs.get(required):
                    errors.append(f"{relative}:{line}: image missing {required}")

    for path, parser in list(pages.items()):
        relative = path.relative_to(ROOT.resolve())
        for raw_url, line in parser.links + parser.resources:
            target, fragment = resolve_target(path, raw_url)
            if target is None:
                continue
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{relative}:{line}: target leaves repository {raw_url!r}")
                continue
            if not target.exists():
                errors.append(f"{relative}:{line}: missing target {raw_url!r}")
                continue
            if fragment and target.suffix.lower() in {".html", ".htm"}:
                target_parser = pages.get(target.resolve()) or parse_page(target)
                if fragment not in target_parser.ids:
                    errors.append(
                        f"{relative}:{line}: missing anchor #{fragment} "
                        f"in {target.relative_to(ROOT)}"
                    )

    return errors, pages


IMPORT_PATTERN = re.compile(
    r"@import\s+(?:url\(\s*)?[\"']?([^\"')\s;]+)",
    re.IGNORECASE,
)


def validate_css() -> list[str]:
    errors: list[str] = []
    for path in iter_files("*.css"):
        relative = path.relative_to(ROOT)
        content = path.read_text(encoding="utf-8")
        for match in IMPORT_PATTERN.finditer(content):
            raw_url = match.group(1)
            target, _ = resolve_target(path, raw_url)
            if target is not None and not target.exists():
                line = content.count("\n", 0, match.start()) + 1
                errors.append(f"{relative}:{line}: missing CSS import {raw_url!r}")
    return errors


def main() -> int:
    html_errors, pages = validate_html()
    errors = html_errors + validate_css()

    if errors:
        print("Site validation failed:")
        for error in sorted(errors):
            print(f"- {error}")
        return 1

    print(f"Site validation passed: {len(pages)} HTML pages checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
