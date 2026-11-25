# 2D / 2.5D Voiceover-Synced Explainer Styles (24+ Presets)

Production design tokens and SVG/Canvas/Remotion component recipes for 9:16 (1080×1920) and 16:9 (1920×1080) voiceover-synced explainers. Sync every visual beat to word-level VO timestamps (`frame = Math.round(t * fps)`), use spring physics (`damping: 12–16, stiffness: 160–200`), and maintain a subtle `1.00 → 1.03` camera drift.

---

## 1. Editorial & Data

| Preset | Background & Mood | Palette | Typography & Key Components |
| :--- | :--- | :--- | :--- |
| **ANGKA** | Warm cream math whiteboard (`#F5F2EA`) | Bg `#F5F2EA`, Ink `#111827`, Teal `#10B981`, Amber `#F59E0B` | Giant bold numerals + animated equation lines + checkmark/cross SVG badges |
| **GEOMETRIK** | Swiss minimalist poster (`#F7F5EE`) | Bg `#F7F5EE`, Circle `#FACC15`, Ink `#09090B` | Oversized black sans number centered inside expanding yellow circle + micro eyebrow tag |
| **LANTANG** | Pure pitch-black kinetic (`#0A0A0A`) | Bg `#0A0A0A`, Primary `#FFFFFF`, Accent `#EF4444` | Full-width stacked bold condensed type + vermilion red hero year/stat slam |
| **TITIK** | Dark dot-matrix probability grid (`#090D12`) | Bg `#090D12`, Cyan `#38BDF8`, Crimson `#F43F5E`, Grid `#1E293B` | Animated matrix of `10×10` or `N` dots lighting up sequentially + `99.9%` counter |
| **ARSIP** | Dark wood desk (`#17120E`) + paper card | Desk `#17120E`, Paper `#FAF8F5`, Marker `#EF4444` | Top-pinned calendar/document card + hand-drawn red SVG circle highlight + typewriter caption |
| **KLIPING** | Hot pink punk magazine collage (`#F472B6`) | Bg `#F472B6`, Paper `#FFFFFF`, Ink `#09090B`, Yellow `#FDE047` | Torn paper strips, cut-out photo boxes, ransom-note rotated word badges + halftone dots |
| **PAPAN** | Classroom green chalkboard (`#1E4D3B`) | Board `#1E4D3B`, Wood `#92400E`, Chalk `#F8FAFC` / `#FDE047` | Hand-drawn chalk stroke SVG reveal (`strokeDashoffset`) + wooden frame + wall clock |

---

## 2. Isometric 2.5D Simulation

| Preset | Background & Mood | Palette | Typography & Key Components |
| :--- | :--- | :--- | :--- |
| **RATING** | Warm cream simulation stage (`#FAF7F0`) | Bg `#FAF7F0`, Tile `#E7E0D3`, Gold `#FBBF24`, Ink `#18181B` | Isometric floating grid platform (`rotateX(55deg) rotateZ(-45deg)` or SVG iso) + characters + floating star-rating pills |
| **DEMO-TIKTOK** | Clean isometric city/crowd sim (`#FAF7F0`) | Bg `#FAF7F0`, Blue `#3B82F6`, Coral `#FB7185`, Ink `#18181B` | Isometric miniature buildings/crowd + floating notification cards + top simulation pill (`SIMULASI`) |
| **FLATLIFE** | Clean light editorial (`#FFFDF7`) | Bg `#FFFDF7`, Coral `#FB7185`, Indigo `#818CF8`, Yellow `#FACC15` | Side-by-side animated comparison bar columns + flat vector character holding boxes |

---

## 3. Tech, UI & Dark Mode

| Preset | Background & Mood | Palette | Typography & Key Components |
| :--- | :--- | :--- | :--- |
| **BLUEPRINT** | Classic CAD engineering sheet (`#0F3A68`) | Bg `#0F3A68`, Grid `#1D4ED8`, Line `#E0F2FE` | Thin `1px` technical grid + animated SVG schematic draw-on + monospace dimension callouts |
| **TERMINAL** | CRT hacker console (`#050A07`) | Bg `#050A07`, Phosphor `#22C55E`, Alert `#EF4444` | Monospace typing CLI + segmented OTP digit boxes + bold `ACCESS GRANTED` banner + faint scanlines |
| **CHAT** | Dark mobile security/story (`#1E293B`) | Bg `#1E293B`, Card `#FFFFFF`, Blue `#3B82F6`, Danger `#EF4444` | Realistic smartphone frame + WhatsApp/chat bubble stagger + warning icon callout (`.apk` / phishing) |
| **STALKING** | Deep midnight social UI (`#0B122B`) | Bg `#0B122B`, Gold `#FBBF24`, Card `#172554`, Red `#EF4444` | Dark analytics list card (`27x`, `19x`) + digital clock tick (`06:12 -> 06:59`) + alert pills |
| **PELUANG** | Deep midnight decision doors (`#0B122B`) | Bg `#0B122B`, Gold `#FBBF24`, Line `#93C5FD` | 3 arched choice doors (`31%`, `99%`, `54%`) + animated cursor click + subtle clock background |
| **CAIR** | Deep indigo liquid glass (`#1E1B4B`) | Bg `#09071A`, Orb `#818CF8`→`#EC4899`, Text `#FFFFFF` | Glowing soft radial gradient orb + frosted glass pill cards (`backdrop-filter: blur(16px)`) |
| **KASET** | Retro VHS tape blue (`#1D358A`) | Bg `#1D358A`, Gold `#FACC15`, Text `#FFFFFF` | VCR `PLAY ►` OSD monospace + horizontal scanlines + VHS cassette vector + bar comparison |

---

## 4. Handcrafted, Folklore & Organic

| Preset | Background & Mood | Palette | Typography & Key Components |
| :--- | :--- | :--- | :--- |
| **SKETSA** | Ruled notebook paper (`#FAF8F0`) | Paper `#FAF8F0`, Line `#CBD5E1`, Highlight `#FDE047`, Ink `#18181B` | Hand-drawn stick-figure SVG (`stroke-linecap: round`) + yellow translucent spotlight cones |
| **HIKAYAT** | Warm backlit *wayang* silhouette (`#451A03`) | Sky `#D97706`→`#FDE68A`, Silhouette `#1C0A00` | Multi-plane parallax mountain/boat/character silhouettes with warm radial backlight |
| **BABAD** | Warm peach sunburst (`#FED7AA`) | Bg `#FED7AA`, Rays `#FFF7ED`, Robe `#DC2626`, Gold `#FACC15` | Rotating radial sunburst stripes + bold-outlined chibi historical vector character |
| **SEMESTA** | Starry midnight folklore (`#0F172A`) | Bg `#0F172A`, Gold `#FBBF24`, Cream `#FEF3C7` | Twinkling starfield + ornate gold-bordered illustration card + traditional motif accents |
| **TUBUH** | Pastel rose anatomy (`#FDA4AF`) | Bg `#FDA4AF`, Organ `#F472B6`, Ink `#18181B`, Flame `#F97316` | Cute bold-outlined organ/brain mascot + comic speech/action cards |
| **LEMPUNG** | Soft sage clay studio (`#D6E2DC`) | Bg `#D6E2DC`, Clay `#FDE047`, Shadow `rgba(0,0,0,0.18)` | Soft 3D-shaded claymorphic rounded characters (inner highlight + soft ambient drop shadow) |

---

## 5. Retro, Gaming & Geography

| Preset | Background & Mood | Palette | Typography & Key Components |
| :--- | :--- | :--- | :--- |
| **PIKSEL** | 16-bit SNES RPG screen (`#1E1B4B`) | Bg `#1E1B4B`, Box `#0F172A`, Gold `#FACC15`, Pixel `#FFFFFF` | Crisp `image-rendering: pixelated` pixel font + RPG dialogue box + `A LANJUT` / `B LEWATI` buttons |
| **MABAR** | Bright sky-blue gacha game (`#38BDF8`) | Bg `#38BDF8`, Card `#FFFFFF`, Gold `#FACC15`, Ink `#09090B` | Stacked gacha pull notification cards + blocky voxel/Minecraft-style gamer avatar + `10x!` badge |
| **PETA** | Vintage atlas cream/seafoam (`#E2ECE9`) | Ocean `#E2ECE9`, Land `#F5D061`, Route `#EF4444`, Ink `#1E293B` | SVG GeoJSON/island polygons + animated dashed biogeography line (`stroke-dashoffset`) + map pins |