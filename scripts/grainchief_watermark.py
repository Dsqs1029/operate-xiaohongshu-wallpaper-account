#!/usr/bin/env python3
"""Apply the approved GrainChief full-canvas watermark templates."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageOps


SKILL_ROOT = Path(__file__).resolve().parents[1]
WATERMARK_ASSET_DIR = SKILL_ROOT / "assets" / "watermark"
DEFAULT_VERTICAL_TEMPLATE = (
    WATERMARK_ASSET_DIR
    / "grainchief-watermark-position-template-vertical-2160x4800.png"
)
DEFAULT_HORIZONTAL_TEMPLATE = (
    WATERMARK_ASSET_DIR
    / "grainchief-watermark-position-template-horizontal-3840x2160-v2.png"
)


def load_template(path: Path) -> Image.Image:
    with Image.open(path) as image:
        template = image.convert("RGBA")
    if template.getchannel("A").getbbox() is None:
        raise ValueError(f"Watermark template has no visible pixels: {path}")
    return template


def template_for_canvas(
    size: tuple[int, int],
    vertical_template: Image.Image,
    horizontal_template: Image.Image,
) -> Image.Image:
    width, height = size
    template = vertical_template if height > width else horizontal_template
    template_width, template_height = template.size

    if width * template_height != height * template_width:
        raise ValueError(
            f"Canvas {width}x{height} does not match the selected "
            f"watermark aspect ratio {template_width}:{template_height}"
        )

    if template.size != size:
        template = template.resize(size, Image.Resampling.LANCZOS)
    return template


def apply_grainchief_watermark(
    image: Image.Image,
    vertical_template: Image.Image,
    horizontal_template: Image.Image,
) -> Image.Image:
    base = ImageOps.exif_transpose(image).convert("RGBA")
    template = template_for_canvas(
        base.size,
        vertical_template,
        horizontal_template,
    )
    base.alpha_composite(template)
    return base


def save_watermarked(
    source: Path,
    destination: Path,
    vertical_template: Image.Image,
    horizontal_template: Image.Image,
) -> None:
    with Image.open(source) as image:
        result = apply_grainchief_watermark(
            image,
            vertical_template,
            horizontal_template,
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.suffix.lower() in {".jpg", ".jpeg"}:
        result.convert("RGB").save(
            destination,
            "JPEG",
            quality=95,
            subsampling=0,
        )
    else:
        result.convert("RGB").save(destination, "PNG", optimize=True)


def verify_watermark_region(
    clean_path: Path,
    watermarked_path: Path,
    vertical_template: Image.Image,
    horizontal_template: Image.Image,
) -> tuple[int, int, int, int]:
    with Image.open(clean_path) as image:
        clean = ImageOps.exif_transpose(image).convert("RGB")
    with Image.open(watermarked_path) as image:
        watermarked = ImageOps.exif_transpose(image).convert("RGB")

    if clean.size != watermarked.size:
        raise ValueError(
            f"Clean and watermarked sizes differ: "
            f"{clean.size} != {watermarked.size}"
        )

    template = template_for_canvas(
        clean.size,
        vertical_template,
        horizontal_template,
    )
    expected_bbox = template.getchannel("A").getbbox()
    actual_bbox = ImageChops.difference(clean, watermarked).getbbox()
    if actual_bbox != expected_bbox:
        raise ValueError(
            f"Watermark region mismatch for {watermarked_path}: "
            f"{actual_bbox} != {expected_bbox}"
        )
    if actual_bbox is None:
        raise ValueError(f"No watermark difference found: {watermarked_path}")
    return actual_bbox


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add the approved GrainChief watermark to wallpaper files."
    )
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--vertical-template",
        type=Path,
        default=DEFAULT_VERTICAL_TEMPLATE,
    )
    parser.add_argument(
        "--horizontal-template",
        type=Path,
        default=DEFAULT_HORIZONTAL_TEMPLATE,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    vertical_template = load_template(args.vertical_template)
    horizontal_template = load_template(args.horizontal_template)

    for source in args.inputs:
        if not source.exists():
            raise FileNotFoundError(source)

        if args.output_dir:
            destination = args.output_dir / source.name
        else:
            destination = source.with_name(
                f"{source.stem}-watermarked{source.suffix}"
            )

        save_watermarked(
            source,
            destination,
            vertical_template,
            horizontal_template,
        )
        print(destination)


if __name__ == "__main__":
    main()
