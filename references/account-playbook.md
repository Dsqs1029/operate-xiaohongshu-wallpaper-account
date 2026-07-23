# Account playbook

## Contents

- User requirements
- Historical account baselines
- Reference-account findings
- Visual system
- Search and CTR model
- Resolution and export pipeline
- Cross-platform distribution diagnosis
- Next-series specification

## User requirements

- The audience is people searching for wallpapers, not a general art audience.
- Images must feel premium, clear, emotionally specific, and usable as phone wallpapers.
- Move toward humanistic photography rather than generic objects or metallic-liquid abstraction.
- Learn from strong creators without copying their exact work.
- Separate the platform cover from the wallpaper product.
- Default modern-phone wallpaper masters to at least 2160x4800 (9:20), or use the user's device-native resolution when supplied.
- Use a separate 2160x2880 (3:4) Xiaohongshu cover master; export 1080x1440 only when needed.
- Preserve the 9:20 master and export a separate 1:2 Douyin copy instead of destructively cropping the master.
- Check Xiaohongshu thumbnail, lock-screen, and home-screen crops before upload.
- Prepare platform drafts completely but always stop before final publication.
- Let the user perform the final Publish action.
- After publication, use evidence rather than intuition to diagnose low traffic.

## Historical account baselines

Use these as dated historical context, not permanent targets:

| Post | Impressions | Views | Cover CTR | Likes | Saves | Other |
|---|---:|---:|---:|---:|---:|---|
| Blue summer wallpapers | 1,012 | 120 | 9.9% | 7 | 2 | Average view 4s |
| Snow wallpapers | 1,343 | 114 | 8.4% | 4 | 0 | 1 share |
| Mist landscapes | 1,288 | 86 | 6.7% | 4 | 1 | — |
| Blue city before dawn | 1,527 | 192 | 10.6% | 6 | 2 | 1 follow, 1 share, average view 7s |
| Blue with lemon yellow | 1,489 | 167 | 10.8% | 4 | 0 | Average view 4s |

Interpretation:

- The blue-summer direction improved both CTR and post-click interaction.
- A practical next CTR milestone is above 12%, but do not treat it as guaranteed.
- Improving cover recognition remains more important than adding more broad hashtags.
- The six most recent posts through 2026-07-22 received 7,471 impressions and 728 views, a weighted view/impression rate of about 9.7%.
- The account's two historical high-exposure examples had reported cover CTRs of 12.6% and 17.2%. Use 12% as a provisional experiment target, not an algorithmic law.

## Reference-account findings

Reference: [Forever永远](https://xhslink.com/m/3rikDtaRKmN), inspected in July 2026.

Observed account positioning:

- About 19,000 followers and 228,000 total likes and saves at inspection time.
- Bio and content consistently reinforce `蓝调时刻`, photography, introversion, loneliness, sunset, and emotional resonance.
- The account behaves as a recognizable blue-hour photography series rather than a generic wallpaper feed.

Observed post examples:

| Post | Likes | Saves | Comments | Notes |
|---|---:|---:|---:|---|
| 安静和热烈好像同时上演 | 7,586 | 1,820 | 224 | Seven images; strong full-screen format and emotional question |
| Blue Hour｜蓝调下的剪影 | 2,885 | 680 | 58 | Nine images; minimal silhouette and blue-hour geometry |
| 我拍到了回忆里的夏天 | 170 | 37 | 8 | Similar tags and palette but weaker immediate cover impact |

The first two observed posts had saves equal to roughly 24% of likes. Treat this as evidence of collection value, not a universal benchmark.

Important conclusion: high- and low-interaction posts used many of the same tags, including photography, atmosphere, and blue-hour terms. Tags alone did not explain the performance gap. Cover strength, specific scene, emotional framing, format novelty, and accumulated account identity mattered more.

The high-performing post did not need `壁纸` in its title or tags for the platform to associate it with `胶片壁纸`. Image semantics and user behavior can contribute to search association. This does not make keywords irrelevant; it means keywords are only one layer.

## Image-ratio finding and correction

The inspected reference carousel used exact 1080x1920 source images, a 9:16 ratio. Several images placed a rotated landscape photograph inside the portrait canvas, encouraging users to turn the phone for a full-screen view.

This is evidence about that creator's platform presentation, not proof that 9:16 fills a modern phone screen. The first production batch incorrectly reused 1080x1920 as the downloadable wallpaper size; the user confirmed that it did not fill the device screen. Do not repeat that assumption.

Use platform-specific deliverables:

- Xiaohongshu cover master: 2160x2880 (3:4), composed for search/profile thumbnails; 1080x1440 is the fallback export.
- Clean wallpaper master: at least 2160x4800 (9:20), or the exact native resolution supplied by the user.
- Clean wallpaper fallback export: 1080x2400 (9:20).
- Douyin upload copy: exact 1:2, preferably 2160x4320 when accepted, otherwise 1080x2160.

For clean wallpapers, keep the narrative anchor in the middle safe zone, leave quiet space for lock-screen time and camera cutouts, and protect the bottom from system-control overlap. Preview every file as a lock screen and a home screen before upload.

No single aspect ratio fits every device without any crop. Describe 1080x2400 as the account default, not a universal guarantee.

Use the rotated presentation selectively because the user's product promise is directly usable wallpaper. A rotated cover may increase curiosity while reducing immediate utility.

## Visual system

Core direction: cinematic humanistic wallpaper with believable documentary details.

Prefer:

- blue hour, dawn, rain, snow, fog, coastal weather
- stations, ferries, cable cars, old buses, roads, windows, bridges, small buildings
- small distant figures rather than conventional portraits
- large environmental negative space
- blue-gray or silver-blue palette with one amber/yellow anchor
- gentle film grain, restrained contrast, and believable shadow detail

Avoid:

- generic tourist postcards
- empty landscapes without a narrative subject
- fake luxury gloss, neon overload, purple-blue gradient slop
- large AI-generated text or illegible signage
- copying the reference creator's yellow `Forever` signature or `Blue Hour` title formula

## Search and CTR model

Use this causal model:

`keyword relevance -> qualified impressions -> cover/title click -> carousel value -> save/follow`

Do not equate hashtags with search queries. A search query is active user intent; a hashtag is one metadata and navigation signal. Broad category terms improve discoverability but can lower audience precision. Style and scene modifiers narrow the audience and clarify the promise.

Avoid inserting camera models or locations for search traffic unless they are truthful and central to the content. Irrelevant equipment terms can cause the platform to suggest the wrong search intent.

## Resolution and export pipeline

Treat resolution and detail as separate qualities:

- A larger pixel grid does not automatically contain more detail.
- Prefer generating or super-resolving a clean master before exact resizing.
- Ordinary interpolation may create the required dimensions but must not be described as a native high-resolution render.
- Inspect hair, faces, rails, wires, windows, vehicle edges, signage, film grain, and shadow texture at 100% zoom.
- Reject waxy smoothing, doubled edges, halos, invented lettering, and inconsistent grain.
- Keep lossless PNG or maximum-quality source files as masters; create platform copies from those masters.
- Never repeatedly resize an already compressed platform copy.

Mechanically verify every file with `scripts/verify_wallpaper_assets.py`.

## Cross-platform distribution diagnosis

Snapshot observed on 2026-07-23:

### Xiaohongshu

The post `天亮以前，城市只剩下蓝色｜6张人文壁纸` had:

- 1,527 impressions
- 192 views
- 10.6% reported cover CTR
- 6 likes, 2 saves, 1 share, and 1 follow
- 7 seconds average viewing time

Interpretation: the platform supplied a normal first test pool for this account. The post did not demonstrate that distribution was withheld; it more likely stopped before the next recommendation tier. Compare its 10.6% CTR with the account's 12.6% and 17.2% high-exposure examples.

### Douyin

After about 12 hours, the matching six-image post had:

- 36 plays
- 51.11% swipe-away rate
- 2.6 of 6 images viewed on average
- 1 like and no saves, shares, comments, or follows

Douyin did not expose a cover CTR for this image post. Use the stop rate, `100% - swipe-away rate`, instead. The observed stop rate was 48.89%, and carousel depth was about 43%.

The account's stronger `后门两人组` example had a 35.06% swipe-away rate and 2.8 of 4 images viewed, or roughly 70% depth. Use these comparisons to prioritize the first image and sequence length.

Working experiment targets:

- Xiaohongshu reported cover CTR: at least 12%.
- Douyin swipe-away rate: at most 40%.
- Douyin average carousel depth: at least 65%.
- For Douyin, test three or four images rather than automatically reposting all six.

Do not infer shadow banning from one post. Separate insufficient initial distribution from weak first-pool response, and record publication age before drawing conclusions.

## Next-series specification

Working concept for the next experiment: a new humanistic wallpaper series with an explicit full-screen product promise in the title and cover.

Suggested sequence:

1. Rain-wet blue-hour station, one distant traveler, one warm lamp.
2. Ferry or cable car crossing a cold landscape.
3. Old bus on a coastal road after rain.
4. Convenience-store window with a lone silhouette.
5. Quiet pedestrian bridge before sunrise.
6. Train leaving the city with a large blue sky or sea field.

Suggested search-led title pattern:

`9:20满屏壁纸｜[specific emotional scene]`

Suggested topics:

`#手机壁纸 #锁屏壁纸 #高清壁纸 #满屏壁纸 #人文摄影`
