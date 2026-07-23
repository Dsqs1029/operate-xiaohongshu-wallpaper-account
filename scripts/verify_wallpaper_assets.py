#!/usr/bin/env python3
"""Verify wallpaper asset dimensions and aspect ratios before upload."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image


PROFILES = {
    "wallpaper-master": (9, 20, 2160, 4800),
    "xhs-cover-master": (3, 4, 2160, 2880),
    "wallpaper-distribution": (9, 20, 1080, 2400),
    "douyin-upload": (1, 2, 1080, 2160),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check image dimensions against a wallpaper delivery profile."
    )
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("files", nargs="+", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ratio_w, ratio_h, min_width, min_height = PROFILES[args.profile]
    failures = 0

    for path in args.files:
        try:
            with Image.open(path) as image:
                width, height = image.size
        except Exception as exc:
            failures += 1
            print(f"FAIL {path}: cannot read image ({exc})")
            continue

        ratio_ok = width * ratio_h == height * ratio_w
        size_ok = width >= min_width and height >= min_height
        status = "PASS" if ratio_ok and size_ok else "FAIL"
        details = [f"{width}x{height}"]
        if not ratio_ok:
            details.append(f"expected exact {ratio_w}:{ratio_h}")
        if not size_ok:
            details.append(f"minimum {min_width}x{min_height}")
        print(f"{status} {path}: {', '.join(details)}")
        failures += status == "FAIL"

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
