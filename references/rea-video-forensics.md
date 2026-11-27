# Shot-Level Video Forensics & `VIDEO.md` Reverse-Engineering (`rea-video`)

> Adapted from [`JuneYaooo/rea-video`](https://github.com/JuneYaooo/rea-video) (`Apache-2.0`) and routed into our 100% free local-first flagship stack (`STUDIO`, `DIRECTOR`, `SAMURAI`, `KURA`, `ATELIER`, `SONIC`, `SIGNAL`, `NOVA`).

---

## 1. Install & Windows Setup Gotchas

- **Requirements**: Python `3.10–3.14` + `ffmpeg` on `PATH`.
- **Install**:
  ```bash
  pip install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video"
  # Optional local speech recognition when no burned-in captions exist:
  pip install "rea-video[ocr,asr] @ git+https://github.com/JuneYaooo/rea-video"
  rea-video prefs lang en
  ```
- **Windows Gotchas**:
  - If `opencv-python` conflicts with headless OpenCV on Python <= 3.12: `pip uninstall -y opencv-python && pip install --force-reinstall --no-deps "opencv-python-headless>=4.8,<5"`.
  - For PDF export (`rea-video pdf`), set `REA_CHROME` if Chrome/Edge is outside default `Program Files` / `%LOCALAPPDATA%`.

---

## 2. Zero-API-Key Agent-Vision Workflow

Runs completely offline with zero paid VLM keys (optional `--vlm` uses `$GEMINI_API_KEY` if desired):

```bash
# 1. Coarse grid survey & transition timing
rea-video survey ref.mp4 -o out/ref

# 2. Offline pixel/audio/OCR breakdown -> produces VIDEO.md + video/ + shots/
rea-video decompose ref.mp4 -o out/ref --lang en

# 3. Inspect compact summary (check VLM: status & low-confidence shots)
rea-video summary out/ref/breakdown.json

# 4. Agent visual review on contact sheets (shots/shot_XXX.jpg)
rea-video review out/ref
# Inspect shots/shot_XXX.jpg via read_file, fill out/ref/review_answers.json
# (label_probs, evidence, narrative, performance, cast, story, overlay_text)
rea-video apply-review out/ref --by agent
```

---

## 3. 4-Layer Token-Saving `VIDEO.md` Reading Protocol

Never load `breakdown.json` (~190k tokens) or `report.md` (human-facing) into agent context. Read `VIDEO.md` layer by layer:

| Layer | File | Approx. Tokens | What It Gives You |
| :--- | :--- | :--- | :--- |
| **1. Card** | `VIDEO.md` frontmatter | ~300 | `made_mix` (production method %), `confidence`, `readers` |
| **2. Map** | `VIDEO.md` body | ~1–2k | Verdict, storyline, remake summary, uncertain shots, file map |
| **3. Timeline & Topic** | `video/timeline.md`, `rhythm.md`, `sound.md`, `look.md`, `packaging.md`, `remake.md` | ~2–4k | 1 line/shot (`~` = inferred vs measured), BPM, cuts/min, lighting setups, SRT/text styling |
| **4. Shot Proof** | `video/shots/<id>.md` + `shots/shot_XXX.jpg` | Targeted | Per-shot keyframes, evidence, and remake prompts (open only for specific shots) |

---

## 4. Production-Method Verdicts -> Local Flagship Routing

Each shot receives one of 11 production verdicts. Route the remake straight into our free local-first flagships:

| `rea-video` Shot Verdict | Local Flagship Remake Route |
| :--- | :--- |
| **Motion Graphics / Code / 2D Animation / UI** | **`STUDIO`** (Remotion / Canvas2D) or **`DIRECTOR` + `SAMURAI`** |
| **3D Render** | **`KURA`** (pick-first 3D assets) + **`STUDIO`** (Three.js r186+) or **`ATELIER`** (Blender PBR) |
| **Live Action / Talking Head / Tabletop** | Follow measured framing + 12 lighting setups (`look.md`) + **`STUDIO`** Talking-Head Auto-Editor |
| **AI-Generated Video / Motion-Driven Dance** | Offload to local/Colab **`Wan 2.1`** (`STACK` / `NOVA`) instead of paid cloud video APIs |
| **Sound / Music / BPM / SFX Stems** | **`SONIC`** (`earshot` / Openverse SFX, `-14 LUFS` mastering) |
| **Subtitles & Hook Packaging (`packaging/subtitles.srt`)** | **`SIGNAL`** (`/yt-edit`, `/yt-chapters`, `/yt-package`) |

---

## 5. Ethical Guardrail & Mandatory Cleanup

- **Transform, Never Copy**: Keep the measured pacing, cut rhythm, and transition structure — replace **100% of script, brand, visuals, and message** with original creator content.
- **Post-Study Cleanup**: Immediately delete `out/ref/` raw frames, stems, and source `.mp4` after extracting learnings into your project spec.
