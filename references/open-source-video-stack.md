# Open-Source Video Editing & Motion Stack (15-Repo Matrix)

Distilled workflows and benchmarks from the 15 open-source GitHub repositories featured in `@aiagently`'s Claude Video Editor stack. Zero paid SaaS dependencies.

---

## 1. Verified 15-Repo Matrix

| # | Repository | Status / Local Coverage | Unique Craft / Value |
| :--- | :--- | :--- | :--- |
| 01 | `yt-dlp/yt-dlp` | **Installed locally** | Reference video & audio download for Stage 1 deconstruction |
| 02 | `openai/whisper` (`faster-whisper`) | **Installed locally** | Word-level timestamps (`analyze_footage.py`) for captions & cut snapping |
| 03 | `kajisho5/ffmpeg-skill` | **Installed locally** (`ffmpeg-skill`) | Deterministic FFmpeg cutting, probing, loudness, & export |
| 04 | `ychol-kr/claude-ffmpeg-skill` | 404 (not found on GitHub) | Covered by `ffmpeg-skill` |
| 05 | `kurbaltaev/ghost-editor` | 404 (not found on GitHub) | Covered by `talking-head-editor` |
| 06 | `agricidaniel/claude-shorts` | **Active (★510)** | 10-step longform-to-shortform clipper, 5-dim viral rubric, cursor tracking |
| 07 | `cloudai-x/threejs-skills` | **Active (★4.3k)** | Three.js `r186` + R3F `9.8` + `WebGPURenderer`/TSL anti-hallucination APIs |
| 08 | `impertio-studio/threejs-claude-skill-package` | 404 (not found on GitHub) | Covered by `ai-animation-styles` + `remotion` |
| 09 | `iart-ai/motion-skills` | **Active (★2.1k)** | 56 modular skills across 19 packs (Manim, WebGL, safe areas, true loops) |
| 10 | `Barty-Bart/motion-graphics` | **Active (★1.5k)** | Single-job skills: `motion-broll`, `object-separation`, `explainer-engaging` (one-take) |
| 11 | `mattypark/Motion-graphics-skill` | **Active (★141)** | Local Canvas/SVG/Three.js/GSAP director + talking-head editor |
| 12 | `LPengYang/MotionClone` | **Active (★569, ICLR 2025)** | Training-free motion cloning via sparse temporal attention guidance |
| 13 | `Bujiazi/MotionClone` | Duplicate of #12 (`LPengYang/MotionClone`) | Same ICLR 2025 MotionClone paper |
| 14 | `heygen-com/hyperframes` | **Installed / Hubbed** (`ai-video-generation-hub`) | HTML/CSS/GSAP multi-track timeline renderer (note: ~23 min for 15s brief) |
| 15 | `zhuyansen/awesome-claude-video-skills` | **Active (★2.6k)** | 16 end-to-end timed benchmarks & security-graded catalog (`agentskillshub.top`) |

---

## 2. Longform-to-Shortform Viral Clipper (`agricidaniel/claude-shorts`)

When converting long podcasts, interviews, or screen-recordings into 9:16 Reels/Shorts/TikToks:
1. **Preflight & Transcribe**: Validate media + disk space, run GPU `faster-whisper` for word-level timestamps.
2. **Auto-Classify Content**: Detect `talking-head`, `screen recording`, or `podcast` framing.
3. **5-Dimension Viral Scoring Rubric** (score 8–12 candidate clips, present ranked table with rationale):
   - **Hook strength** (0–3s scroll-stopper)
   - **Coherence** (self-contained without prior context)
   - **Emotion** (curiosity, surprise, tension, conviction)
   - **Value density** (insights per second)
   - **Payoff** (clean, memorable closing punchline)
4. **Audio-Aware Boundary Snapping**: Never cut mid-word or mid-sentence. Snap clip start/end to exact word boundaries, sentence endings, and audio silences.
5. **Screen-Recording Cursor Tracking**: Detect mouse cursor via frame differencing and smoothly pan the 9:16 crop window to follow active UI interaction.

---

## 3. Single-Job Commercial Formats & Render Benchmarks (`Barty-Bart` & `awesome-claude-video-skills`)

- **`explainer-high-energy` (12–20s)**: Beat-locked kinetic typography and geometric shape transitions for fast product hype.
- **`explainer-default` (45–90s)**: Clean product UI rebuilt in HTML/React and animated up close while in use.
- **`explainer-engaging` (10–30s, One-Take Continuity)**: One continuous hero element (e.g. a drop, cursor, card, or orb) travels uninterrupted through the entire product workflow with zero hard cuts.
- **Measured Real SFX**: Pair visual beats with measured real-world sound effects (mechanical clicks, paper, subtle whoosh) — never cheap synthetic beeps.
- **Turnaround Benchmark Rule**: For fast 15s promos, prefer **Remotion / Canvas2D (~2–5 min)** over heavy HyperFrames (~23 min) or multi-pass illustrated kits (~22 min) unless HTML/GSAP multi-track composition is specifically required.

---

## 4. Training-Free Motion Transfer (`LPengYang/MotionClone`)

For generative diffusion video when cloning camera/subject motion from a reference clip:
- Use **MotionClone**'s sparse temporal attention guidance (ICLR 2025) to transfer motion trajectories directly from a reference video without fine-tuning or slow DDIM video inversion.

---

## 5. Agentic Multi-Pipeline Video Production (`OpenMontageInc/OpenMontage`)

- **Paste-A-Video Entry Point**: Accepts a reference video URL/file first, analyzes structure and pacing, then routes into one of 12 specialized agentic production pipelines (explainer, product demo, short-form, documentary, etc.).
- **Local Complement**: Use OpenMontage's pipeline separation pattern (Research -> Script -> Asset Gen -> Timeline Assembly -> Multi-Provider Render) alongside our local Remotion/FFmpeg/Three.js Director stack.