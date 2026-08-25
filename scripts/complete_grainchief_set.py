#!/usr/bin/env python3
"""Finish a GrainChief set from three phone and two desktop source images."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

from grainchief_watermark import (
    DEFAULT_HORIZONTAL_TEMPLATE,
    DEFAULT_VERTICAL_TEMPLATE,
    load_template,
    save_watermarked,
    verify_watermark_region,
)


PHONE_SIZE = (2160, 4800)
DESKTOP_SIZE = (3840, 2160)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create clean and watermarked GrainChief exports plus a "
            "five-image contact sheet."
        )
    )
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--phone", nargs=3, type=Path, required=True)
    parser.add_argument("--desktop", nargs=2, type=Path, required=True)
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace existing exports in the output root.",
    )
    return parser.parse_args()


def fit_and_save(source: Path, destination: Path, size: tuple[int, int]) -> None:
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        if image.width * size[1] != image.height * size[0]:
            print(
                f"warning: fitting {source.name} from "
                f"{image.width}x{image.height} to {size[0]}x{size[1]}"
            )
        fitted = ImageOps.fit(
            image,
            size,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    fitted.save(destination, "PNG", optimize=True)


def refuse_overwrite(paths: list[Path], overwrite: bool) -> None:
    if overwrite:
        return
    existing = [path for path in paths if path.exists()]
    if existing:
        formatted = "\n".join(str(path) for path in existing)
        raise FileExistsError(
            "Refusing to replace existing exports without --overwrite:\n"
            f"{formatted}"
        )


def copy_source(source: Path, destination: Path) -> None:
    if not source.exists():
        raise FileNotFoundError(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def create_contact_sheet(
    phone_files: list[Path],
    desktop_files: list[Path],
    destination: Path,
) -> None:
    canvas = Image.new("RGB", (2400, 1600), "#d9ddd9")
    draw = ImageDraw.Draw(canvas)

    phone_size = (360, 800)
    phone_positions = ((70, 400), (460, 400), (850, 400))
    for path, position in zip(phone_files, phone_positions, strict=True):
        with Image.open(path) as image:
            thumbnail = ImageOps.fit(
                image.convert("RGB"),
                phone_size,
                method=Image.Resampling.LANCZOS,
            )
        draw.rectangle(
            (
                position[0] - 5,
                position[1] - 5,
                position[0] + phone_size[0] + 5,
                position[1] + phone_size[1] + 5,
            ),
            fill="#f2f0e9",
        )
        canvas.paste(thumbnail, position)

    desktop_size = (1050, 591)
    desktop_positions = ((1280, 110), (1280, 899))
    for path, position in zip(desktop_files, desktop_positions, strict=True):
        with Image.open(path) as image:
            thumbnail = ImageOps.fit(
                image.convert("RGB"),
                desktop_size,
                method=Image.Resampling.LANCZOS,
            )
        draw.rectangle(
            (
                position[0] - 5,
                position[1] - 5,
                position[0] + desktop_size[0] + 5,
                position[1] + desktop_size[1] + 5,
            ),
            fill="#f2f0e9",
        )
        canvas.paste(thumbnail, position)

    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, "JPEG", quality=94, subsampling=0)


def export_set(args: argparse.Namespace) -> None:
    root = args.output_root.resolve()
    source_dir = root / "source"
    phone_clean_dir = root / "phone-wallpaper-clean-2160x4800"
    phone_public_dir = root / "phone-wallpaper-watermarked-2160x4800"
    desktop_clean_dir = root / "desktop-wallpaper-clean-3840x2160"
    desktop_public_dir = root / "desktop-wallpaper-watermarked-3840x2160"
    preview_path = root / "preview" / "grainchief-watermarked-set-preview.jpg"

    phone_clean = [
        phone_clean_dir / f"{index:02d}-phone-2160x4800.png"
        for index in range(1, 4)
    ]
    phone_public = [
        phone_public_dir / path.name for path in phone_clean
    ]
    desktop_clean = [
        desktop_clean_dir / f"desktop-{index:02d}-3840x2160.png"
        for index in range(1, 3)
    ]
    desktop_public = [
        desktop_public_dir / path.name for path in desktop_clean
    ]
    source_paths = [
        *(
            source_dir / f"phone-{index:02d}-source{source.suffix.lower()}"
            for index, source in enumerate(args.phone, start=1)
        ),
        *(
            source_dir / f"desktop-{index:02d}-source{source.suffix.lower()}"
            for index, source in enumerate(args.desktop, start=1)
        ),
    ]

    refuse_overwrite(
        [
            *source_paths,
            *phone_clean,
            *phone_public,
            *desktop_clean,
            *desktop_public,
            preview_path,
        ],
        args.overwrite,
    )

    for source, destination in zip(
        [*args.phone, *args.desktop],
        source_paths,
        strict=True,
    ):
        copy_source(source.resolve(), destination)

    vertical_template = load_template(DEFAULT_VERTICAL_TEMPLATE)
    horizontal_template = load_template(DEFAULT_HORIZONTAL_TEMPLATE)

    for source, clean, public in zip(
        args.phone,
        phone_clean,
        phone_public,
        strict=True,
    ):
        fit_and_save(source, clean, PHONE_SIZE)
        save_watermarked(
            clean,
            public,
            vertical_template,
            horizontal_template,
        )
        bbox = verify_watermark_region(
            clean,
            public,
            vertical_template,
            horizontal_template,
        )
        print(f"verified {public}: {PHONE_SIZE}, watermark={bbox}")

    for source, clean, public in zip(
        args.desktop,
        desktop_clean,
        desktop_public,
        strict=True,
    ):
        fit_and_save(source, clean, DESKTOP_SIZE)
        save_watermarked(
            clean,
            public,
            vertical_template,
            horizontal_template,
        )
        bbox = verify_watermark_region(
            clean,
            public,
            vertical_template,
            horizontal_template,
        )
        print(f"verified {public}: {DESKTOP_SIZE}, watermark={bbox}")

    create_contact_sheet(phone_public, desktop_public, preview_path)
    print(f"preview {preview_path}")


def main() -> None:
    export_set(parse_args())


if __name__ == "__main__":
    main()
