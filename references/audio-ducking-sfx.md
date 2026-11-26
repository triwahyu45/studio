# Audio Ducking and Sound Effects Synthesis

Professional audio engineering for code-rendered videos.

---

## 1. Automatic BGM Ducking with FFmpeg

To automatically lower background music volume when speech occurs:

```bash
ffmpeg -y \
  -i dialogue.wav \
  -i bgm.wav \
  -filter_complex "[1:a]volume=0.25[music]; [0:a][music]amix=inputs=2:duration=first:dropout_transition=2[out]" \
  -map "[out]" master_audio.wav
```

---

## 2. Generating High-Energy Procedural BGM (Python / NumPy)

You can generate electronic driving beats, basslines, and synth arpeggios directly using NumPy without any external music files:

```python
import numpy as np
import scipy.io.wavfile as wav

sr = 44100
duration = 30.0
t = np.linspace(0, duration, int(sr * duration), endpoint=False)

# Kick beat at 128 BPM
bpm = 128
beat_period = 60.0 / bpm
kick_trigger = (t % beat_period) < 0.12
kick = np.sin(2 * np.pi * 55 * np.exp(-t % beat_period * 20)) * kick_trigger

# Hi-hat on eighth notes
hat_trigger = (t % (beat_period / 2)) < 0.04
hat = (np.random.rand(len(t)) * 2 - 1) * hat_trigger * 0.15

# Synthwave Bassline
bass_freq = 110 # A2
bass = 0.2 * np.sin(2 * np.pi * bass_freq * t) * (0.5 + 0.5 * np.sin(2 * np.pi * (bpm/120) * t))

mix = kick * 0.4 + hat * 0.2 + bass * 0.3
wav.write("synth_bgm.wav", sr, (mix * 32767).astype(np.int16))
```

---

## 4. Free Zero-Key Audio & SFX Stack (`earshot`, `opus-sound-layer`, `Openverse`)

Prefer real acoustic SFX and CC0/CC-licensed recordings over pure sine synthesis whenever an authentic foley, UI click, whoosh, or ambient bed is needed:

1. **`earshot` MCP (`Leonxlnx/earshot`, MIT)** — Local audio design & foley studio (922 procedural sound designs, 252 film SFX bank, 20 MCP tools).
   - Inspect/generate/layer SFX directly via the `earshot` MCP tools, or CLI: `earshot doctor`, `earshot search <query>`, `earshot render ...`.
   - Use for UI clicks, cinematic risers/whooshes, mechanical impacts, and acoustic stingers with zero cloud API keys.
2. **`opus-sound-layer` (`Bodila51/opus-sound-layer`, MIT)** — 1,139 CC0 public-domain field recordings & foley layers ready for commercial use without attribution.
3. **Openverse Audio API (`api.openverse.org`)** — 5.2M+ Creative Commons audio tracks & SFX with **zero API key required**:
   ```bash
   curl -s "https://api.openverse.org/v1/audio/?q=cinematic+ambient&license_type=commercial&page_size=5"
   ```
   - Filter `license_type=commercial` (or `cc0` / `pdm`) and inspect `results[].url` + `results[].license` before downloading and muxing with Section 1 FFmpeg ducking.
