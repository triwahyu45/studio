#!/usr/bin/env python3
"""Analyze raw talking-head footage using ffprobe, ffmpeg silencedetect, and optional faster-whisper."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


def probe_media(video_path: Path) -> dict[str, Any]:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration,size,bit_rate:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels",
        "-of",
        "json",
        str(video_path),
    ]
    raw = subprocess.check_output(cmd, text=True)
    data = json.loads(raw)
    v_stream = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    a_stream = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), {})

    fps_raw = v_stream.get("r_frame_rate", "30/1")
    num, den = (int(x) for x in fps_raw.split("/")) if "/" in fps_raw else (int(fps_raw), 1)
    fps = round(num / den, 3) if den else 30.0

    return {
        "file": str(video_path),
        "duration": round(float(data.get("format", {}).get("duration", 0.0)), 3),
        "width": v_stream.get("width"),
        "height": v_stream.get("height"),
        "fps": fps,
        "video_codec": v_stream.get("codec_name"),
        "has_audio": bool(a_stream),
        "audio_codec": a_stream.get("codec_name"),
        "sample_rate": int(a_stream["sample_rate"]) if a_stream.get("sample_rate") else None,
    }


def detect_silences(video_path: Path, noise_db: float, min_dur: float, total_dur: float) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        str(video_path),
        "-af",
        f"silencedetect=noise={noise_db}dB:d={min_dur}",
        "-f",
        "null",
        "-",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    stderr = proc.stderr

    silences: list[dict[str, float]] = []
    cur_start: float | None = None
    for line in stderr.splitlines():
        m_start = re.search(r"silence_start:\s*([0-9.]+)", line)
        if m_start:
            cur_start = float(m_start.group(1))
        m_end = re.search(r"silence_end:\s*([0-9.]+)\s*\|\s*silence_duration:\s*([0-9.]+)", line)
        if m_end and cur_start is not None:
            silences.append({
                "start": round(cur_start, 3),
                "end": round(float(m_end.group(1)), 3),
                "duration": round(float(m_end.group(2)), 3),
            })
            cur_start = None
    if cur_start is not None and total_dur > cur_start:
        silences.append({
            "start": round(cur_start, 3),
            "end": round(total_dur, 3),
            "duration": round(total_dur - cur_start, 3),
        })

    # Compute keep_segments (non-silent speech segments)
    keep: list[dict[str, float]] = []
    cursor = 0.0
    pad = 0.08
    for s in silences:
        seg_end = min(total_dur, s["start"] + pad)
        if seg_end - cursor > 0.15:
            keep.append({"start": round(cursor, 3), "end": round(seg_end, 3)})
        cursor = max(cursor, s["end"] - pad)
    if total_dur - cursor > 0.15:
        keep.append({"start": round(cursor, 3), "end": round(total_dur, 3)})

    return silences, keep


def transcribe_words(video_path: Path, model_name: str) -> tuple[list[dict[str, Any]], str | None]:
    try:
        from faster_whisper import WhisperModel  # type: ignore
    except ImportError:
        return [], "faster-whisper not installed; install with `pip install faster-whisper` for word-level timestamps"

    model = WhisperModel(model_name, compute_type="int8")
    segments, info = model.transcribe(str(video_path), word_timestamps=True)
    words: list[dict[str, Any]] = []
    for seg in segments:
        for w in getattr(seg, "words", []) or []:
            words.append({
                "word": w.word.strip(),
                "start": round(w.start, 3),
                "end": round(w.end, 3),
            })
    return words, f"transcribed ({info.language}, {len(words)} words)"


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze talking-head footage for auto-cut and word-synced captions.")
    parser.add_argument("input_video", type=Path, help="Path to input video file")
    parser.add_argument("-o", "--output", type=Path, default=Path("edit_plan.json"), help="Output JSON path (default: edit_plan.json)")
    parser.add_argument("--silence-db", type=float, default=-35.0, help="Silence threshold in dB (default: -35.0)")
    parser.add_argument("--silence-dur", type=float, default=0.4, help="Minimum silence duration in seconds (default: 0.4)")
    parser.add_argument("--transcribe", action="store_true", help="Extract word-level timestamps via faster-whisper if installed")
    parser.add_argument("--model", default="small", help="faster-whisper model size (default: small)")
    args = parser.parse_args()

    if not args.input_video.exists():
        print(f"Error: file not found: {args.input_video}", file=sys.stderr)
        return 1

    meta = probe_media(args.input_video)
    if meta["has_audio"]:
        silences, keep_segments = detect_silences(args.input_video, args.silence_db, args.silence_dur, meta["duration"])
    else:
        silences, keep_segments = [], [{"start": 0.0, "end": meta["duration"]}]

    words: list[dict[str, Any]] = []
    note: str | None = None
    if args.transcribe:
        if meta["has_audio"]:
            words, note = transcribe_words(args.input_video, args.model)
        else:
            note = "input video has no audio stream; skipped transcription"

    plan = {
        "media": meta,
        "silences": silences,
        "keep_segments": keep_segments,
        "words": words,
        "note": note,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.output} | {meta['width']}x{meta['height']} @ {meta['fps']}fps | dur={meta['duration']}s | keep_segments={len(keep_segments)} | words={len(words)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
