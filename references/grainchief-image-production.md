# GrainChief Image Production

Use this reference when the user asks to make, preview, revise, complete, resize, watermark, or package GrainChief wallpaper images.

## Contents

- Conversation state
- Standard product set
- Visual direction
- Prompt construction
- Large-environment picture-book recipe
- Reference-image use
- Resolution and export
- Exact watermark workflow
- Deterministic scripts
- Quality checks
- Copy handoff

## Conversation state

Treat the user's short commands as workflow state:

- `做图`, `出预览图`, or a new theme: create one representative preview only.
- Specific feedback such as `太深`, `太淡`, `水墨感过强`, `材质不对`, or `只变换颜色`: change that variable first and preserve approved invariants.
- `可以`, `这个可以`, or `继续`: the direction is approved, but do not silently create an unrelated series.
- `补全`: complete the approved direction into the standard product set.
- `文案`: return copy only, ready to paste; do not regenerate or reopen image work.

Do not generate a large batch before the first visual direction is approved. One good preview is cheaper to judge and makes later variants more coherent.

## Standard product set

Unless the user specifies another count, `补全` means:

1. phone 01: the approved preview
2. phone 02: a new composition that confirms the visual world
3. phone 03: a new composition with a distinct spatial idea
4. desktop 01: a true 16:9 establishing scene
5. desktop 02: a true 16:9 quieter or wider variation

Deliver:

- three phone wallpapers at exactly `2160x4800`
- two desktop wallpapers at exactly `3840x2160`
- clean archive copies
- public copies with the approved GrainChief watermark
- one contact sheet containing all five public copies

Desktop wallpapers must be composed as horizontal scenes. Do not create them by merely widening or cropping a vertical wallpaper.

## Visual direction

The account should feel contemporary, restrained, and collectible rather than like generic AI art.

Prefer:

- one clear visual idea that survives a small feed thumbnail
- large environmental scale with one small narrative subject
- controlled contrast: quiet negative space plus one readable dark or warm anchor
- blue-gray, silver-blue, mineral green, muted coral, warm cream, charcoal, and restrained amber
- matte pigment, paper grain, dry printed texture, colored-pencil detail, film grain, weather, or worn material
- clean, stable silhouettes and believable spatial depth
- composition designed around lock-screen time and desktop icons

Avoid:

- oily AI rendering, plastic gloss, fake HDR, glass reflections, over-sharpened halos
- one-note gray-yellow backgrounds or images so pale that the thumbnail loses its subject
- oversaturated neon, vulgar gold, orange overload, purple-blue gradient slop
- heavy ink wash, uncontrolled watercolor bleed, or a generic old-style Chinese-painting treatment
- random backgrounds, decorative clutter, repeated tiny motifs, meaningless abstraction
- literal coins, ingots, Bagua, talismans, or pasted mystical symbols
- malformed vehicles, rails, bridges, architecture, hands, faces, text, or signage
- copied reference composition, signature, title system, watermark, or subject stack

When the user says an image is not attractive, diagnose the most visible cause before changing the theme:

- flat image: increase foreground-middle-background separation or strengthen the single narrative anchor
- too dark: lift the environment while preserving one deep structural area
- too pale: add one stronger silhouette or controlled color anchor
- too much ink wash: replace diffuse washes with matte printed color blocks and fine dry texture
- too artificial: simplify the scene, reduce gloss and atmospheric effects, and restore natural imperfection

## Prompt construction

Use the built-in image generation tool for normal generation and reference-based variants.

Generate each distinct asset in a separate call. For a completed set, use the approved preview as a style reference and explicitly state its role:

`preserve palette, material, print texture, contrast, subject scale, and editorial tone; create a new composition rather than a crop or near-copy`

Prompts should define:

1. intended wallpaper format and orientation
2. environment and primary visual idea
3. narrative subject and its percentage of the frame
4. top lock-screen quiet zone or desktop icon space
5. foreground, middle ground, and background
6. controlled palette with one accent
7. material and print texture
8. invariants inherited from the approved preview
9. explicit avoid list

Never ask image generation to render the GrainChief watermark, title, logo, or border. Add the exact watermark after generation.

## Large-environment picture-book recipe

For a mature `大环境绘本` wallpaper:

- environment occupies about `88-92%`
- train, vehicle, house, person, or other story clue occupies about `5-10%`
- upper `25-35%` remains calm and low-detail for lock-screen time
- foreground gives scale, middle ground carries the story, background creates distance
- use a restrained warm amber subject against dusty blue, muted sage, cream, and charcoal
- use matte gouache-like color fields, fine colored-pencil detail, subtle screen-print irregularity, and natural paper grain
- keep the result editorial and mature, not cute or anime-like

Useful composition variations:

- a tiny train crossing a long valley bridge
- a train following a lakeside curve
- a train emerging from a mountain tunnel
- a small road, ferry, cable car, lit window, or distant building inside a vast environment

Reject:

- giant foreground subjects
- childish cartoon or anime styling
- fantasy castles or excessive buildings
- dramatic sunset as a shortcut for impact
- impossible tracks, repeated carriages, melted bridge arches, or ornamental clutter

## Reference-image use

Extract principles from a reference, not its recognizable identity.

Lock only the requested invariants:

- palette
- texture and material
- contrast level
- scale relationship
- density
- emotional tone

Change:

- camera position
- terrain or spatial grammar
- subject route and pose
- foreground framing
- dominant negative-space shape

When the user says `只变换颜色`, keep composition and geometry stable. When the user asks for new content, do not recolor or extend the old composition.

## Resolution and export

Preserve generated source files before resizing.

Default output tree:

```text
<series-root>/
|-- source/
|-- phone-wallpaper-clean-2160x4800/
|-- phone-wallpaper-watermarked-2160x4800/
|-- desktop-wallpaper-clean-3840x2160/
|-- desktop-wallpaper-watermarked-3840x2160/
`-- preview/
    `-- grainchief-watermarked-set-preview.jpg
```

Use lossless PNG for source, clean archive, and public wallpaper exports. Use a high-quality JPEG only for the contact sheet when file size matters.

Resize to the exact delivery canvas with Lanczos only after visual quality is accepted. If the generated source is smaller than the final canvas and no super-resolution pass was performed, describe the export as interpolated or resized. Never call it native 4K.

## Exact watermark workflow

The approved position templates are skill assets:

- `assets/watermark/grainchief-watermark-position-template-vertical-2160x4800.png`
- `assets/watermark/grainchief-watermark-position-template-horizontal-3840x2160-v2.png`

Rules:

1. Keep a clean internal archive.
2. Public GrainChief wallpaper exports receive the matching full-canvas transparent template.
3. Alpha-composite the whole template directly.
4. Do not separately recalculate text size, offset, shadow, opacity, or placement.
5. For another resolution with the same aspect ratio, resize the entire template to the target canvas before compositing.
6. Reject an output if its aspect ratio does not match the selected template.
7. Verify that the clean-versus-public difference bounding box exactly equals the template alpha bounding box.

Use [scripts/grainchief_watermark.py](../scripts/grainchief_watermark.py) for one or more existing exports.

## Deterministic scripts

Add the watermark to existing files:

```bash
python scripts/grainchief_watermark.py \
  path/to/phone.png \
  path/to/desktop.png \
  --output-dir path/to/watermarked
```

Complete an approved set from exactly three phone sources and two desktop sources:

```bash
python scripts/complete_grainchief_set.py \
  --output-root path/to/series \
  --phone phone-01.png phone-02.png phone-03.png \
  --desktop desktop-01.png desktop-02.png
```

The completion script:

- copies source files into the series archive
- exports exact phone and desktop dimensions
- preserves clean copies
- adds the approved watermark templates
- verifies dimensions and watermark regions
- creates a five-image contact sheet

Use `--overwrite` only when the user explicitly wants to replace an existing export.

## Quality checks

Before reporting completion, inspect:

- train, vehicle, bridge, rail, architecture, anatomy, and reflections at high detail
- consistent palette and material across all five images
- readable thumbnail subject without making it too large
- quiet top area for mobile lock screens
- protected bottom system-control area
- desktop icon breathing room
- no baked-in text, logo, border, or fake watermark from image generation
- exact public dimensions
- exact watermark difference region
- contact-sheet rhythm and repetition

Report actual output dimensions and whether the sources were generated, super-resolved, or interpolated.

## Copy handoff

Current title rule:

`东方壁纸｜[concrete image], [restrained emotional line]`

Do not use `玄学` in new titles unless the user explicitly changes this rule.

For `文案`, return:

- one title
- a short body grounded in the visible scene
- one natural preference question
- `本组为AI辅助视觉创作。`
- three to six relevant topics

Avoid hard efficacy, fortune, wealth, or supernatural promises. Describe visual details, mood, wallpaper use, and a gentle emotional association.
