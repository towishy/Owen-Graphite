#!/usr/bin/env python3
"""Contrast audit for key Owen Graphite foreground/background pairs."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Pair:
    name: str
    foreground: str
    background: str
    minimum: float = 4.5


PAIRS = [
    Pair("light body text", "#1a1a1a", "#ffffff"),
    Pair("light muted text", "#6b7280", "#ffffff"),
    Pair("light external link", "#334155", "#ffffff"),
    Pair("light table header", "#374151", "#f3f4f6"),
    Pair("light report callout", "#334155", "#f8fafc"),
    Pair("light risk callout", "#78350f", "#fffbeb"),
    Pair("light recommendation callout", "#064e3b", "#f0fdf4"),
    Pair("dark body text", "#e5e7eb", "#1f2024"),
    Pair("dark muted text", "#9ca3af", "#1f2024"),
    Pair("dark external link", "#cbd5e1", "#1f2024"),
    Pair("dark table header", "#f3f4f6", "#1f2937"),
    Pair("dark report callout", "#e5e7eb", "#111827"),
    Pair("dark search highlight", "#ffedd5", "#7c2d12"),
]


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError(f"expected 6-digit hex color, got {value!r}")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def channel_luminance(channel: int) -> float:
    normalized = channel / 255
    if normalized <= 0.03928:
        return normalized / 12.92
    return ((normalized + 0.055) / 1.055) ** 2.4


def relative_luminance(color: str) -> float:
    red, green, blue = hex_to_rgb(color)
    return 0.2126 * channel_luminance(red) + 0.7152 * channel_luminance(green) + 0.0722 * channel_luminance(blue)


def contrast_ratio(foreground: str, background: str) -> float:
    first = relative_luminance(foreground)
    second = relative_luminance(background)
    lighter = max(first, second)
    darker = min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def audit_pairs(pairs: list[Pair]) -> list[str]:
    failures = []
    for pair in pairs:
        ratio = contrast_ratio(pair.foreground, pair.background)
        status = "OK" if ratio >= pair.minimum else "FAIL"
        print(f"{status}: {pair.name}: {ratio:.2f}:1 ({pair.foreground} on {pair.background}, min {pair.minimum:.1f})")
        if ratio < pair.minimum:
            failures.append(pair.name)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true", help="Only print failing pairs.")
    args = parser.parse_args()

    if args.quiet:
        failures = []
        for pair in PAIRS:
            ratio = contrast_ratio(pair.foreground, pair.background)
            if ratio < pair.minimum:
                print(f"FAIL: {pair.name}: {ratio:.2f}:1 ({pair.foreground} on {pair.background})")
                failures.append(pair.name)
    else:
        failures = audit_pairs(PAIRS)

    if failures:
        print(f"ERROR: contrast audit failed for {len(failures)} pair(s): {', '.join(failures)}")
        return 1
    print(f"OK: contrast audit passed ({len(PAIRS)} pairs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
