# TTS Providers Configuration & Customization

This guide details how to configure and call the three supported TTS engines.

---

## 1. Google Gemini API TTS (Default Free Tier)

Gemini 3.8 Flash TTS provides expressive speech synthesis with zero subscription cost via Google AI Studio API key (`GEMINI_API_KEY`).

### Supported Pre-set Voices
- `Puck`: Energetic, vibrant, youthful male voice (ideal for sports/tech host).
- `Kore`: Clear, professional, warm female voice (ideal for analyst/explainer).
- `Fenrir`: Deep, authoritative male voice.
- `Aoede`: Expressive, storytelling female voice.
- `Charon`: Serious, calm male voice.
- `Zephyr`: Bright, modern voice.

### Shell Execution via `gemini-api` CLI
```bash
# Single Speaker with Acting Style
gemini-api tts "Selamat datang di Kontes Robot Indonesia!" \
  --voice Puck \
  --style "energetic sports host shouting excitedly" \
  --language id-ID \
  --out dimas_line.wav

# Two-Speaker Dialogue
gemini-api tts "Dimas [excited]: Robot KRSBI berhasil mencetak gol! Sarah: Tendangan terarah yang luar biasa!" \
  --multi-speaker "Dimas=Puck,Sarah=Kore" \
  --language id-ID \
  --out dialogue.wav
```

---

## 2. Fish Audio API (Optional Ultra-Realistic Voice)

Fish Audio (`fish.audio`) provides state-of-the-art zero-shot voice cloning and emotional Indonesian/multilingual speech synthesis.

### API Integration (Python)
```python
import requests

url = "https://api.fish.audio/v1/tts"
headers = {
    "Authorization": f"Bearer {FISH_AUDIO_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "text": "Robot soccer KRSBI melesat dengan roda omni!",
    "reference_id": "<model_or_clone_id>",
    "format": "wav",
    "mp3_bitrate": 192,
    "latency": "normal"
}

res = requests.post(url, json=payload, headers=headers)
with open("fish_voice.wav", "wb") as f:
    f.write(res.content)
```

---

## 3. Microsoft Edge-TTS Neural (Zero-Key Fast Fallback)

Used whenever an API key is not supplied. Generates neural speech locally without rate limits.

### High-Energy Tweaked Settings
```bash
# Energetic Male Host (+15% rate, +2Hz pitch)
uvx edge-tts --voice "id-ID-ArdiNeural" --rate="+15%" --pitch="+2Hz" --text "..." --write-media out1.mp3

# Crisp Female Analyst (+10% rate)
uvx edge-tts --voice "id-ID-GadisNeural" --rate="+10%" --pitch="+1Hz" --text "..." --write-media out2.mp3
```
