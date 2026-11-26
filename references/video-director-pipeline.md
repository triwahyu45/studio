# Video Director 5-Stage Pipeline (`@t1mline` Reference-to-Render System)

A structured directing workflow that turns an AI coding agent from a passive "prompted editor" (which produces generic AI slop) into a **Video Director** (`75%` systematic craft + `25%` creator idea & taste).

---

## Stage 1 — Reference Video Deconstruction (`yt-dlp` + `ffprobe` + `read_file`)

Never study a reference Reel, TikTok, or Short by stepping through screenshots in a browser—it is slow, laggy, and misses fast cuts and audio cues.

1. **Download directly to scratch:**
   ```powershell
   yt-dlp --no-playlist -f "bv*+ba/b" --merge-output-format mp4 -o "<scratch>\ref.%(ext)s" "<URL>"
   ```
   - **Instagram Blocked Fallback (`Instagram sent an empty media response`):** Intercept the `video/` stream URL cleanly with Playwright (`page.on("response", ...)` matching `content-type: video/`, stripping `&bytestart`) to download the full 1080p MP4 stream.
2. **Probe technical specs:**
   ```powershell
   ffprobe -v error -show_entries format=duration,bit_rate:stream=codec_type,codec_name,width,height,r_frame_rate -of json "<scratch>\ref.mp4"
   ```
3. **Watch natively via `read_file`** on `ref.mp4` and extract a **Style Bible**:
   - **Beat Sheet & Cut Rhythm:** Exact timestamp of every hook, escalation, match-cut, and payoff (typically a visual shift every 1.0–2.5 s).
   - **Color & Surface System:** Primary dark/warm canvas hexes, single bold accent color (e.g. `#E63946` red / `#00F0FF` cyan), paper/corkboard/glass textures.
   - **Typography Hierarchy:** Display weight, highlight box style, tabular counters, and kinetic entry timing.
   - **Motion Grammar:** Bezier easing curves, spring damping, whip-pan transitions, match-cut camera zooms (e.g. zooming through a monitor into a 3D scene).
   - **SFX Map:** Risers, whooshes, mechanical clicks, bass hits, and voice pacing.

---

## Stage 2 — Story & Voiceover Script (`01 / SCRIPT`)

Write a tight, spoken-word script structured around clear narrative tension before touching code:
1. **Visual Hook (0–3 s):** Open with a bold "What if..." or physical match-cut on Frame 1.
2. **The Wrong Way / Contrast:** Show why naive prompting produces slop (explicitly contrast bad vs. intentional craft).
3. **The Mechanism / Shift:** Reveal the structured system (`01`–`05` pillars) with concrete proof.
4. **75 / 25 Creative Split:** The director system handles 75% of execution (pacing, curves, captions, sound), leaving 25% for the creator's idea and taste.
5. **Word-Budget Check & Loud-Word Beat Table:** Target ~140–170 WPM and structure every beat in a `Time | What happens | Loud word` table where each `2.5–4.0 s` beat designates **one Loud word** (e.g., `SECONDS`, `spark`, `died`, `survived`) that triggers the hero visual emphasis (scale jump, highlighter wipe, red glow, or stamp slam) + frame-locked SFX hit.

---

## Stage 2.5 — Free Asset Generation Prompting (Chroma-Key & Screen-Blend)

When generating custom foreground objects or atmospheric overlays with free tools (Google Flow or `image-generator` subagent) for 2.5D parallax compositing:
- **Foreground Cutout Objects (`#00FF00` Chroma-Key):**
  Append `"isolated on a plain flat pure green #00FF00 background, the whole object visible with a margin, no cast shadow on the green, even flat light, no text, no letters, no numbers, no logos, no watermark, no frame, no border"` → key out cleanly in Remotion/Canvas or FFmpeg (`chromakey=0x00FF00:0.18:0.08`).
- **Fire / Spark / Glow Overlays (`#000000` Screen-Blend):**
  Append `"isolated on a plain pure black background, the whole effect visible with a margin, no frame, no border"` → composite via CSS/Canvas `mix-blend-mode: screen` or FFmpeg `blend=all_mode=screen`, with a soft-feathered bottom alpha gradient so no hard edge appears.
- **Consistent Lighting Lock:** Repeat identical key-light direction (e.g., `"soft light from the upper left"`), film grain, and target aspect ratio (`9:16` or `4:3`) across every plate in the project.

---

## Stage 3 — Storyboard & Code-Driven 2D/3D Animation (`02 / STORYBOARD` + `03 / ANIMATION`)

Build scenes deterministically in **Remotion + Three.js / React / CSS** (zero After Effects or manual keyframes):
- **Storyboard Grid (`02`):** Plan 6–12 numbered panels (`01`..`12`) specifying **Anchor Object**, **Camera Vector**, and **Transition Type** (whip-pan, zoom-through-screen, spotlight reveal, card fan-out).
- **3×4 Visual Storyboard Pre-Vis:** For 45–60s vertical explainers, break the script into **10–12 scenes (3–5s each)** and generate **1 unified 3×4 Storyboard Grid image** via the `image-generator` subagent before writing 3D scene code so spatial staging, metaphors, and character poses lock in upfront and cut revision rounds.
- **2D Motion Graphics:**
  - Corkboard / evidence pins + animated SVG red-yarn / circle strokes (`strokeDashoffset`).
  - Realistic UI mockups (chat prompt bar, NLE timeline, YouTube player, comment feed) rendered in clean HTML/Tailwind—never static low-res screenshots.
  - Bezier curve graphs, progress meters (`75%` / `25%`), and numeric countdown tickers.
  - **SaaS Launch Grammar:** 1 accent color + neutral grotesk (`Inter Tight`/`Inter`, `Geist`, `Instrument Sans`, `Bricolage Grotesque`, `Plus Jakarta Sans`), UI components that morph across **one continuous camera space**, **halftone dot-ripple** transitions, **3D UI slab tilt** (`2D -> 3D isometric`), tactile 3D hardware (`keycap macro-pad + LCD`), and **SFX-ONLY (NO MUSIC)**.
  - **Vox Editorial Collage Grammar:** Physical paper/newspaper objects on a desk, **torn-paper wipe transitions**, **yellow highlighter sweep**, **digit-by-digit odometer roll** (right-most digits spin fastest), **colour-drain desaturation** on dramatic beats, **animated partly on 2s** (`12/15 fps` tactile cadence inside `30 fps` render), and **SFX-ONLY (NO MUSIC)**.
  - **Interactive SaaS Demo Card + Cutout Presenter (`@awananimasi.id`):** Graph-paper dark/saturated grid canvas (`#0F172A`, `#2E1065`, `#064E3B`, `#FACC15`, `#EA580C`), top-right `01..09` icon progress pill bar, macOS-framed live UI card with tab switching & animating charts, plus bottom-corner cutout presenter + pixel mascot helper with speech bubbles.
- **3D Worlds & Camera Moves:**
  - Stylized 3D scenes (voxel/low-poly desk, director chair, holographic curved UI screens, floating 3D cartridge/handheld) with continuous orbital drift and eased dolly-ins.
  - Custom easing curves (`cubic-bezier` / `spring()`)—never linear motion on hero transitions.

---

## Stage 4 — Talking-Head Auto-Edit & Kinetic Captions (`04 / CAPTIONS`)

When footage includes a talking head or voiceover track:
1. **Word-Level Timing:** Extract word timestamps via Whisper / `faster-whisper` or `prepare_voice.py`.
2. **Dynamic Captions:** Highlight the active keyword with a contrasting pill/box (`LIKE A DIRECTOR.`) synced to the exact spoken frame.
3. **Punch Zooms & B-Roll:** Apply 1.08–1.15× scale punch-ins on emphasis words and cut away to code-rendered B-roll diagrams/UI cards every 2–4 s.

---

## Stage 5 — Sound Design & Verified Render (`05 / SOUND`)

1. **Frame-Synced SFX & SFX-Only Mode:** Layer risers before reveals, whooshes on whip-pans, mechanical clicks on UI typing/buttons, paper rips, odometer ticks, and sub-hits on title slams. For SaaS Launch & Vox Editorial cuts, prefer **SFX-ONLY (zero background music)** for maximum authority and crispness.
2. **Audio Mix & Loudness:** When music is used, duck it under narration (`sidechaincompress` or `-18 dB` music bed) and verify integrated loudness (`-14` to `-18 LUFS`).
3. **Mandatory Pre-Final Visual Self-QA Gate & Verify:** Render a fast test pass / contact sheet **first** and visually inspect via `read_file` for 5 defects before final render:
   - (1) text or stroke overlap,
   - (2) label/card collisions,
   - (3) hard bottom edge on screen-blended fire/effects,
   - (4) text cropped during camera push-in,
   - (5) green `#00FF00` chroma-key halo.
   Fix all defects, then run final render and verify `MP4` with `ffprobe` (resolution, fps, H.264/AAC) before delivering.
4. **Fast `--qa-only` 5-Point Calibration & 30fps Draft -> 60fps Final:** Run a fast `--qa-only` pass (~15s) outputting `qa_sheet.jpg` + `cover.png` (4:5 safe check) to audit 5 points: (1) header/logo margin, (2) 2D B-roll clear of character head, (3) 3D character/prop proportions, (4) bottom-safe subtitles locked to canonical script spelling, and (5) visual/pose/background variety every `<= 3s`. Use `30fps` for motion drafts and `60fps` (`1080×1920`, H.264 + AAC) for the approved final render.
