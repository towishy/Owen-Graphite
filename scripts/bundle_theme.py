#!/usr/bin/env python3
"""Bundle dev CSS modules into the Obsidian theme.css entrypoint."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEV = ROOT / "dev"
ORDER_FILE = DEV / "_order.txt"
DEFAULT_OUTPUT = ROOT / "theme.css"


def ordered_module_paths(order_file: Path = ORDER_FILE) -> list[Path]:
    if not order_file.is_file():
        raise FileNotFoundError(f"missing module order file: {order_file}")

    paths: list[Path] = []
    for raw_line in order_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        module_path = order_file.parent / line
        if not module_path.is_file():
            raise FileNotFoundError(f"missing CSS module listed in {order_file.name}: {line}")
        paths.append(module_path)

    if not paths:
        raise ValueError(f"no CSS modules listed in {order_file}")
    return paths


def bundle_bytes(order_file: Path = ORDER_FILE) -> bytes:
    return b"".join(path.read_bytes() for path in ordered_module_paths(order_file))


def write_bundle(output: Path = DEFAULT_OUTPUT, order_file: Path = ORDER_FILE) -> Path:
    output.write_bytes(bundle_bytes(order_file))
    return output


def check_bundle(output: Path = DEFAULT_OUTPUT, order_file: Path = ORDER_FILE) -> bool:
    return output.is_file() and output.read_bytes() == bundle_bytes(order_file)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if theme.css is not the current dev bundle.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Bundle output path.")
    parser.add_argument("--order", type=Path, default=ORDER_FILE, help="Module order file.")
    args = parser.parse_args()

    if args.check:
        if not check_bundle(args.output, args.order):
            raise SystemExit(f"ERROR: {args.output} is not up to date with {args.order}")
        print(f"OK: {args.output.relative_to(ROOT)} matches dev bundle")
        return 0

    output = write_bundle(args.output, args.order)
    print(f"OK: bundled {len(ordered_module_paths(args.order))} modules -> {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())