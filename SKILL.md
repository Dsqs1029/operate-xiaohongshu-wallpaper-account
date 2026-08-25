---
name: operate-xiaohongshu-wallpaper-account
description: Operate and improve Xiaohongshu and Douyin wallpaper content through competitor research, humanistic or refined Eastern-auspicious visual direction, high-resolution modern-phone wallpaper production, search-aware copywriting, creator-center draft preparation, cross-platform packaging, and post-performance diagnosis. Use when Codex is asked to plan, generate, upscale, prepare, cross-post, or analyze wallpaper content, especially for the user's GrainChief account.
---

# Operate a Xiaohongshu Wallpaper Account

Build a recognizable wallpaper account rather than publishing unrelated attractive images. Optimize the chain from qualified impressions to clicks, saves, and follows while preserving honest AI disclosure and user control over final publication.

Read [references/account-playbook.md](references/account-playbook.md) before choosing a visual direction, diagnosing performance, or preparing a post.

For GrainChief image generation, preview approval, set completion, watermarking, and export packaging, read [references/grainchief-image-production.md](references/grainchief-image-production.md).

## Non-negotiable requirements

- Target people actively looking for phone and lock-screen wallpapers.
- Make every wallpaper directly usable; do not confuse a decorative cover with the product.
- Separate the Xiaohongshu cover from the downloadable wallpaper product. Never require one file to serve both purposes.
- Default phone archive masters to at least 2160x4800 (9:20) and desktop archive masters to 3840x2160 (16:9). Keep a separate 1080x2400 distribution copy only when a platform or workflow needs it. Use a device-specific native resolution when the user supplies it; do not promise universal edge-to-edge fit across every phone.
- Keep an internal clean archive without title, watermark, border, or decorative frame. For GrainChief public wallpaper exports, add only the approved exact-position watermark through deterministic post-processing; never ask the image model to draw it.
- Create the Xiaohongshu cover as a separate 3:4 master, preferably 2160x2880, optimized for the search/profile feed. Export 1080x1440 only when needed.
- Package Douyin separately. Preserve the 9:20 clean master, then export an exact 1:2 upload copy at 2160x4320 when the current uploader accepts it, otherwise 1080x2160. Never crop the only master to satisfy Douyin.
- Keep the wallpaper's essential subject in the middle safe zone. Leave quiet space at the top for lock-screen time, camera cutouts, or a dynamic island, and keep essential detail away from the bottom system-control area.
- Before upload, inspect three states: Xiaohongshu 3:4 thumbnail, lock-screen crop, and home-screen crop. Reject any set where a face, person, vehicle, horizon, or narrative anchor is awkwardly cut.
- For photographic series, prefer specific place, time, weather, human traces, and emotional tension. For Eastern-auspicious series, translate a sourced idea into restrained form, material, composition, and sequence instead of pasting literal mystical symbols onto an image.
- Avoid generic AI luxury, plastic surfaces, excessive HDR, meaningless abstraction, repeated metallic-liquid motifs, bright fortune clichés, and hard supernatural claims.
- Use blue-gray as the visual base with one restrained warm yellow or amber anchor when appropriate.
- Preserve natural imperfection: film grain, slight motion blur, weather, shadow, worn materials, and believable optics.
- Do not copy another creator's exact images, title formula, watermark, signature, or composition. Transfer principles only.
- Do not let one successful metaphor become the whole account. Rotate among water, mountain, wood, gates or paths, celestial order, and other culturally grounded structures while keeping the account's material and color identity coherent.
- Use `东方壁纸` as the current title prefix. Do not use `玄学` in new titles unless the user explicitly asks to restore it; historical examples containing that word remain historical evidence only.
- Disclose AI-assisted visual creation in the body and use the platform content declaration when available.
- Never claim a camera, lens, location, or documentary event that did not exist.
- Never click the final **Publish** button on Xiaohongshu, Douyin, or another platform. Upload assets, fill all fields, verify the preview, and stop immediately before publication for the user to confirm.
- Do not promise traffic or diagnose an algorithm from a single post.

## Operating workflow

### 1. Inspect before creating

Use the creator center and visible account data when available. Record:

- impressions
- views
- cover click-through rate
- average viewing time
- likes, saves, comments, shares, and follows
- search queries and traffic-source mix
- publication age

Compare posts at similar ages. Treat follower base, pinned status, platform campaigns, and account history as confounders.

### 2. Choose one experiment

State the hypothesis and change one main variable per post whenever possible:

- cover composition
- visual subject
- color anchor
- title framing
- keyword layer
- carousel length

Keep the remaining system stable so the next diagnosis is meaningful.

### 3. Write the creative brief

Default to one dedicated cover plus four to six coherent clean wallpapers:

1. A separate 3:4 cover with immediate thumbnail recognition, emotional tension, and a clear wallpaper promise.
2. A first clean wallpaper that immediately fulfils the cover promise.
3. A second wallpaper that confirms the visual world.
4. A human trace or environmental detail.
5. A wider establishing scene or quieter variation.
6. A memorable closing wallpaper when the set needs six images.

Use a person, vehicle, lit window, ferry, station, road, bridge, or distant building as a small narrative subject. A human figure should usually occupy only 5-15% of the frame.

One image may test the reference creator's rotated full-screen presentation, but keep the other images upright and directly usable as wallpapers.

For the user's iterative GrainChief production loop, create one preview first. After explicit approval and the command `补全`, default to a coherent five-image product set: three phone wallpapers and two independently composed desktop wallpapers. Follow the detailed state and export rules in [references/grainchief-image-production.md](references/grainchief-image-production.md).

### 4. Generate and quality-check images

Use the `imagegen` skill for new raster images or edits. Inspect every output at full size and reject images with:

- malformed anatomy or geometry
- impossible reflections or lighting
- melted architecture, vehicles, text, or signage
- over-smoothed plastic texture
- crushed shadow detail or over-sharpened halos
- inconsistent color grading across the set
- important elements outside the thumbnail-safe area
- wallpaper dimensions that remain 9:16 when the intended product is a modern full-screen phone wallpaper
- cover text, borders, or branding accidentally baked into clean wallpaper files

Do not label an upscaled file as native 4K. Report actual pixel dimensions and whether detail was generated, super-resolved, or merely interpolated.

Use this resolution pipeline:

1. Generate or edit from the largest available source.
2. Prefer a true high-resolution render or an AI super-resolution pass before mechanical resizing.
3. Preserve texture, film grain, fine architecture, faces, wires, signage, and shadow detail at 100% zoom.
4. Reject waxy smoothing, ringing, doubled edges, invented text, or sharpened halos.
5. Use Lanczos or equivalent only for final exact sizing after detail quality is acceptable.
6. If the source is smaller than the delivery size and only ordinary interpolation is available, disclose that the file is resized rather than claiming higher detail.

For every batch, verify dimensions mechanically before upload. The default acceptance check is:

- clean master: at least 2160x4800 and exactly 9:20
- desktop master: exactly 3840x2160 and exactly 16:9
- Xiaohongshu cover master: at least 2160x2880 and exactly 3:4
- Xiaohongshu fallback cover: exactly 1080x1440
- clean distribution copy: at least 1080x2400 and exactly 9:20
- Douyin upload copy: at least 1080x2160 and exactly 1:2
- no clean wallpaper is silently resized back to 1080x1920

Run `python scripts/verify_wallpaper_assets.py --profile <profile> <files...>` before upload. Use `wallpaper-master`, `desktop-master`, `xhs-cover-master`, `wallpaper-distribution`, or `douyin-upload`.

### 5. Build search-aware copy

Separate search relevance from click persuasion:

- Keywords influence which audience receives the impression.
- Cover and title influence whether that audience clicks.
- Image quality and usefulness influence saves and follows.

Use three keyword layers:

1. Category anchor: `壁纸`, `手机壁纸`, `锁屏壁纸`.
2. Style: `人文摄影`, `电影感壁纸`, `蓝调壁纸`, `氛围感`.
3. Scene: `雨夜车站`, `海边公路`, `雪山缆车`, `旅行壁纸`, or the actual scene.

Do not assume `#壁纸` reaches everyone. Broad terms create a larger, more competitive, mixed-intent pool. Long-tail terms usually reduce volume but can improve relevance.

For a search-led wallpaper account, place the strongest category phrase early enough to survive title truncation. For the current GrainChief naming system, combine `东方壁纸` with a concrete scene and emotional hook, for example:

`东方壁纸｜雾谷有列车，远方正经过`

Use three to six relevant topics. Avoid hashtag stuffing and irrelevant camera-model terms.

### 6. Prepare the draft

Use the browser-control skill when working in the signed-in creator center.

1. For Xiaohongshu, upload the dedicated 3:4 cover first, followed by the clean 9:20 wallpapers in narrative order.
2. For Douyin, use a separate 1:2 copy and normally test three or four images rather than forcing all six into one post.
3. Fill the title, body, and topics.
4. Add a natural question that invites a useful comment, such as asking which image the user would set as the lock screen.
5. Include `本组为AI辅助视觉创作。`
6. Add the platform AI-content declaration when the control works.
7. Verify actual dimensions, image count, ordering, preview, visibility, and text.
8. Stop before the final Publish button and hand control to the user.

### 7. Diagnose after publication

Wait for an appropriate observation window, normally 24 hours for the first review. Record the publication age and distinguish recommendation signals by platform:

1. On Xiaohongshu, use impressions, cover CTR, views, average viewing time, saves, and follows. Do not call roughly 1,200-1,500 initial impressions "no distribution" for this account.
2. On Douyin image posts, do not invent a cover CTR when the dashboard does not provide one. Use `1 - swipe-away rate` as the first-frame stop rate, then average images viewed, saves, shares, and follows.
3. Adequate impressions but low CTR or stop rate: cover/title mismatch or weak first-frame recognition.
4. Adequate CTR or stop rate but low saves: attractive imagery without clear wallpaper utility.
5. Saves but few follows: weak account identity or no coherent series promise.
6. Short dwell or shallow carousel depth: repetitive sequence, misleading cover, or insufficient second-image payoff.

Use the account's July 2026 evidence as provisional working thresholds:

- Xiaohongshu: recent weighted view/impression rate was about 9.7%; aim for a reported cover CTR of at least 12% before calling a cover competitive.
- Douyin: aim for swipe-away rate at or below 40% and average carousel depth at or above 65%.
- Treat these as experiment targets, not platform guarantees or universal algorithm rules.

Do not change or delete a new post repeatedly during its first distribution window without a clear reason.

## Deliverables

For a content-production request, provide:

- the experiment hypothesis
- the dedicated cover and ordered clean wallpaper files with actual dimensions
- confirmation that thumbnail, lock-screen, and home-screen crops were checked
- title, body, and topics
- AI disclosure status
- the prepared creator-center draft stopped before publication
- the metric thresholds to review after 24 hours
