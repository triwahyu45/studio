---
name: STUDIO
description: Unified local AI Video Director & production studio combining Talking-Head Auto-Editor (20 presets + 15 named effects + analyze_footage.py), 24+ 2D/2.5D Explainer Motion Graphics, 19+ Procedural 3D Three.js r186+ & Remotion styles, Video Director 5-stage pipeline (Loud-word beat tables, #00FF00/#000000 asset prompting, SFX-only mode, Pre-Final Visual Self-QA), and 15-repo Open-Source Video Stack.
---

# AI Video Studio (Unified Director & Local Production Suite)

Complete, 100% free local code-driven video production suite (FFmpeg, `faster-whisper`, Remotion, Three.js r186+, Playwright/Canvas2D) — zero paid SaaS subscriptions or diffusion slop.
- **Sibling Boundaries**: **`DIRECTOR`** owns creative direction, treatments, 11-block blueprints, and 3-pass critic QA; **`ATELIER`** owns headless Blender PBR/Cycles rendering; **`SONIC`** owns TTS, `earshot` SFX, ducking, and `-14 LUFS` audio mastering.

---

## Routing Matrix (Pick Your Production Mode)

| Video Need | Primary Workflow & Reference | Key Output |
| :--- | :--- | :--- |
| **Talking-Head / Creator Edit / Longform Clipper** | [`references/talking-head-presets.md`](references/talking-head-presets.md) + [`scripts/analyze_footage.py`](scripts/analyze_footage.py) | 60fps/30fps MP4 with silence auto-cut, 5-dim viral clip scoring, cursor tracking, depth-text behind speaker (`DEPTH`, `LUMEN`), & 15 named effects |
| **2D / 2.5D Voiceover Explainer** | [`references/mograph-24-styles.md`](references/mograph-24-styles.md) | Frame-synced 9:16 or 16:9 explainers across 24+ editorial, isometric, tech UI, folklore, retro, & map presets |
| **Procedural 3D Motion (Three.js r186+)** | [`references/motion3d-19-styles.md`](references/motion3d-19-styles.md) + **`KURA`** | Pick-first 3D assets via `kura` MCP, exploded hardware (`PRECISION`, `BONGKAR`), Zack D (`ZACK-EXPLAINER`), 8-bit (`PIXEL-8BIT`), `STUDIO-BENCH`, `SIM-GRID`, & R3F/WebGPU guardrails |
| **Reference Deconstruction & Directing** | [`references/video-director-pipeline.md`](references/video-director-pipeline.md) | `yt-dlp` + `ffprobe` + `Loud word` beat tables, `#00FF00`/`#000000` free asset prompts, SFX-only SaaS/Vox grammar, & Pre-Final Visual Self-QA |
| **Open-Source Video Tooling & Benchmarks** | [`references/open-source-video-stack.md`](references/open-source-video-stack.md) | 15-repo stack (`claude-shorts`, `threejs-skills`, `OpenMontage`, `MotionClone`, `Barty-Bart`, render speed benchmarks) |
| **Audio, TTS & `-14 LUFS` Mastering** | Delegate to **`SONIC`** + [`references/3d-kinematics-engine.md`](references/3d-kinematics-engine.md) + [`references/vertical-9-16-recipes.md`](references/vertical-9-16-recipes.md) | Multi-provider TTS, `earshot`/Openverse SFX, sidechain BGM ducking, `-14 LUFS`, & 9:16 web kinematics |
| **Remotion, Cartoon 3D Shorts & Sketch-to-3D** | [`references/remotion-and-story-shorts.md`](references/remotion-and-story-shorts.md) | React/Three.js Remotion compositions (`1080x1920` / `--scale 1.3333`), 45–70s `words.json` synced story shorts, & marker sketch reveals |

---

## Non-Negotiable Production Rules

1. **Pre-Final Visual Self-QA Gate**: Render a fast test pass/contact sheet first and inspect for text overlap, label collision, hard bottom edges on screen-blended fire/effects, cropped push-in text, and `#00FF00` halos before final render.
2. **Audio & Loudness**: Prefer **SFX-ONLY (no music)** for SaaS Launch & Vox Editorial cuts, or duck BGM under narration; verify `-14 LUFS` & H.264/AAC via `ffprobe`.
3. **Safe Margins (9:16)**: Keep captions inside `top >= 14%`, `bottom <= 78%`, `right >= 120px` on `1080x1920`.
4. **`KURA` Pick-First 3D Asset Loop**: Always query `kura` MCP (`search_assets`) first -> pick local or `fetch_cc0_asset` -> build procedural `.js` only when missing and persist via `save_asset` -> on user revision, call `revise_asset` so upgrades persist for all future videos.
---

## Mandatory Self-Audit & Revise-Before-Delivery Gate

Before delivering any video:
1. Render a fast test pass / contact sheet first and inspect via `read_file` for text overlap, cropped push-ins, hard effect edges, or `#00FF00` halos.
2. Fix every defect found, then run final render and verify resolution, fps, H.264/AAC, and `-14 LUFS` via `ffprobe`.
