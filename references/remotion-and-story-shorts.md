# Remotion, Cartoon 3D Story Shorts & Sketch-to-3D

> Sub-module for `STUDIO` covering Remotion programmatic React/Three.js video, 45–70s 2D-in-3D story shorts, hand-drawn sketch-to-3D marker reveals, and portrait explainer verification.

---

## 1. Remotion Verified CLI & Composition Rules

- **Scaffold & Preview**: `npx create-video@latest --yes --blank --no-tailwind my-video` -> `npx remotion studio --no-open`.
- **Render Commands**:
  - Standard MP4: `npx remotion render <comp-id> out/video.mp4`
  - 2K Vertical 9:16: `npx remotion render <comp-id> out/video.mp4 --scale 1.3333` (from `1080x1920` base -> `1440x2560`)
  - Stills QA: `npx remotion render <comp-id> out/frames --frames=0,30,60`
- **3D & Transitions**: `npm i @remotion/three three @react-three/fiber @remotion/transitions @remotion/paths`. Always drive Three.js animations strictly from Remotion `useCurrentFrame()` / `fps` (never `requestAnimationFrame` or wall-clock time).

---

## 2. 2D-Characters-in-3D-World Story Shorts (45–70s, 9:16)

- **Script Beat Formula (~3.7 words/s)**:
  1. **Hook (1 line)**: Surprising true fact immediately in motion (zero throat-clearing).
  2. **Setting**: Year, place, stakes.
  3. **Escalating Action (3–4 beats)**: Each beat raises physical or absurd tension.
  4. **Snap + Deadpan Double Line**: Visual climax + *"Luckily... / Unluckily..."* contrast.
  5. **Everyday Analogy + Consequence + Callback Twist**: Explain physics/mechanism simply, show rule it created, and close with callback punchline.
- **Frame-Exact Audio/Visual Sync**: Generate voiceover first, extract exact word timings (`words.json`), and time every camera kick, prop swap, and character reaction **0–3 frames before its trigger word**. Never overlay on-screen captions when visuals already tell the story.
- **Audio Mix Baseline**: Keep narration dry/unchanged (`0 dB`), SFX around `-6 dB`, and duck BGM cleanly under speech before final `-14 LUFS` normalize.
- **4-Round Visual Verifier Loop**: Extract stills at key beats (`HOOK`, `SNAP`, `ANALOGY`, `OUTRO`), inspect via `read_file` for clipped props/dark frames/muddy silhouettes, and iterate lighting/camera FOV until clean.

---

## 3. Sketch-to-3D & Portrait Motion-Graphic Honesty Gate

- **Sketch-to-3D Reveals**: Pair hand-drawn marker construction outlines/strokes with subtle paper grain so 3D geometry feels sketched-on dynamically instead of static CAD turntables.
- **Self-Check Before Reporting Done**: Confirm zero hallucinated statistics/names in voiceover scripts, inspect rendered still frames at 9:16 (`1080x1920`), and verify `ffprobe` codec + loudness (`-14 LUFS`, `TP <= -1 dB`).
