# STUDIO — Local AI Video Director & Production Suite

AI Agent Skill for **Antigravity**, **Claude Code**, and **OpenAI Codex**. End-to-end local video production: talking-head auto-editor (20 presets + depth-text), 24+ 2D/2.5D motion graphics, 19+ procedural 3D Three.js styles, multi-provider TTS, BGM ducking, and 9:16 vertical kinematics.

---

## Quick Install (Claude Code / Codex / Antigravity)

Clone this skill into your agent's global or project skills directory:

| Agent | Global Install Path | Project-Local Path |
| :--- | :--- | :--- |
| **Antigravity** | Global Antigravity skills dir | `.agents/skills/STUDIO` |
| **Claude Code** | `~/.claude/skills/STUDIO` | `.claude/skills/STUDIO` |
| **OpenAI Codex** | `~/.codex/skills/STUDIO` | `.agents/skills/STUDIO` |

```bash
# Example (Antigravity / Claude Code / Codex — pick your path):
git clone https://github.com/triwahyu45/STUDIO.git ~/.claude/skills/STUDIO
```

---

## Requirements & Dependencies (For Agents)

- **Runtime / Tools**: **Python 3.10+**, **FFmpeg**, **Node.js 18+** (for Remotion/Three.js), **faster-whisper** (local STT), **Playwright** (optional IG/web reference capture)
- **MCP Servers**: Optional: `kura` (3D asset vault + 8 external repos), `ffmpeg-skill` / `kinocut` (timeline/cut helpers); pair with `SONIC` (`earshot`, `edge-tts-mcp`) for audio
- **Related Skills**: Pairs with [`KURA`](https://github.com/triwahyu45/KURA) (3D asset vault), [`DIRECTOR`](https://github.com/triwahyu45/DIRECTOR), [`SAMURAI`](https://github.com/triwahyu45/SAMURAI), [`SONIC`](https://github.com/triwahyu45/SONIC) (audio/TTS/SFX), & [`ATELIER`](https://github.com/triwahyu45/ATELIER) (Blender PBR)
- **API Keys / Secrets**: None for local mode (`faster-whisper`, `FFmpeg`, Three.js/Remotion).

```json
{
  "mcpServers": {
    "edge-tts-mcp": {
      "command": "uvx",
      "args": ["--with", "mcp[cli]<2", "--from", "edge-tts-mcp==0.1.1", "edge_tts_mcp"]
    }
  }
}
```

---

## Included Files

- `SKILL.md` — Router, non-negotiable production rules, & Self-Audit Gate
- `scripts/analyze_footage.py` — Silence & viral clip scoring analyzer
- `references/` — `talking-head-presets.md`, `mograph-24-styles.md`, `motion3d-19-styles.md`, `video-director-pipeline.md`, `rea-video-forensics.md`, `3d-kinematics-engine.md`, `vertical-9-16-recipes.md`, `remotion-and-story-shorts.md`, `open-source-video-stack.md`

## When to Trigger / Search Keywords

`studio`, `talking-head edit`, `reels`, `tiktok`, `youtube shorts`, `explainer video`, `remotion`, `tts`, `audio ducking`, `cut dead air`, `rea-video`, `VIDEO.md`, `shot breakdown`
