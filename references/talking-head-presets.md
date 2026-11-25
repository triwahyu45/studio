# Talking-Head Editor — 20 Visual Presets & Flagship HUD Tokens

Design tokens reverse-engineered for 1080×1920 (9:16) and 1920×1080 (16:9) talking-head creator videos.

---

## Group A: Depth / Text-Behind-Speaker (Requires Subject Cutout Matte)

| Preset | Backdrop / Grade | Typography & Layering | Accent & Palette | Caption / Lower-Third |
| :--- | :--- | :--- | :--- | :--- |
| **DEPTH** | Bright natural room footage | Giant stacked repeated bold sans behind speaker: top rows outline-only, hero row solid `#2563EB` | Bg: natural, Outline: `#111827`, Accent: `#2563EB` | Clean minimal or omitted during giant text beat |
| **LUMEN** | Warm indoor footage | Backlit condensed display text behind head with warm amber outer glow (`0 0 28px #F59E0B`) | Glow: `#F59E0B` → `#FEF08A`, Sub-accent: `#EF4444` | Small bold red-orange speaker/topic tag |
| **POSTER** | Deep royal blue studio (`#1D4ED8`) | Giant uppercase poster headline (`EMPAT PRINSIP`) behind speaker + translucent `15%` echo rows | Studio: `#1D4ED8`, Hero: `#FFFFFF` / `#FACC15` | Minimal bottom subtitle |
| **STORYTELLER** | Moody dark-vignetted footage | Gold uppercase eyebrow (`#FBBF24`) + giant crisp white editorial serif/sans (`Privasi.`) behind head | Eyebrow: `#FBBF24`, Headline: `#FFFFFF`, Vignette: `#09090B` | Clean centered white caption |
| **TYPESET** | Vivid indigo/violet (`#4F46E5`→`#6D28D9`) | Mixed italic serif + bold geometric sans behind speaker with thin wireframe echo text | Backdrop: `#4F46E5`/`#6D28D9`, Text: `#FFFFFF` | Small clean bottom subtitle |

---

## Group B: Caption-First Creator Styles

| Preset | Visual Vibe | Caption Geometry & Animation | Palette | Micro-Graphics / HUD |
| :--- | :--- | :--- | :--- | :--- |
| **BOLD** | High-contrast blurred/dimmed intro or punchy cut | Uppercase bold sans + crimson highlight pill badge above (`tetap sepi`) | Badge: `#EF4444`, Main Text: `#FACC15` | Optional blur fade-in on hook |
| **CALM** | Soft warm-graded natural footage | Delicate white italic serif centered lower-third, gentle opacity fade | Text: `#FFFFFF`, Shadow: `rgba(0,0,0,0.45)` | Zero clutter, slow 1.00→1.03 drift |
| **CLEAN** | Soft daylight footage | Clean small white sans subtitle at lower-third | Icons/Text: `#FFFFFF`, Subtle stroke | 3 minimal white linear icons + micro-labels floating above head |
| **CREATOR-POP** | Dynamic diagonal before/after split wipe | Bold yellow-outlined punchy uppercase (`MENTAHANNYA DAN`) + tilted pill badge (`MENTAH`) | Yellow: `#FACC15`, Stroke: `#09090B`, Pill: `#FFFFFF` | Diagonal white wipe line (`rotate(12deg)`) |
| **IMPACT** | High-energy talking-head | Stacked uppercase white words + neon lime-yellow square highlight box on hero word (`AI`) | Box: `#D9F99D` / `#BEF264`, Text in box: `#09090B`, Other: `#FFFFFF` | Subtle spark/ember particles |
| **PODCAST** | Moody studio interview framing | Clean left-aligned white sans subtitle at lower-third | Text: `#FFFFFF`, Icons: `#E4E4E7` | 3 crisp top telemetry icons + labels (`konsisten`, `setahun`, `berkembang`) |
| **SYSTEM** | Clean talking-head | Floating dark charcoal pill (`#18181B`) above speaker with neon lime-yellow text (`AI doang.`) | Pill: `#18181B`, Text: `#D9F99D` | Clean rounded pill (`border-radius: 14px`) |

---

## Group C: Full-Screen & Card B-Roll Cutaways

| Preset | Cutaway Type | Layout & Components | Palette | Audio / Motion Cue |
| :--- | :--- | :--- | :--- | :--- |
| **GRAPHITE** | Full-screen matte data card | Giant orange stat (`24 jam`) + animated horizontal progress bar + micro labels | Bg: `#111315`, Accent: `#F97316`, Text: `#F4F4F5` | Count-up spring + bar fill + soft tick SFX |
| **INTERFACE** | Full-screen iOS iMessage mockup | Top circular avatar + crisp sent (`#3B82F6`) & received (`#E2E8F0`) chat bubbles + input bar | Bg: `#F8FAFC`, Sent: `#3B82F6`, Recv: `#E2E8F0` | Pop-in bubble stagger + iOS send/recv click SFX |
| **MARKER** | Pure black typographic card | Minimal white line icon top-left + stacked bright yellow highlighter-tape strips | Bg: `#09090B`, Tape: `#FDE047`, Text: `#09090B` | Strip wipe left→right + marker swipe SFX |
| **MOGRAPH-MIX** | Dark neon glassmorphic UI card | Pill badges + glowing rounded icon card (`#A855F7`) + coral/orange headline | Bg: `#0F0728`→`#3B0764`, Accent: `#FB923C` | Spring scale pop + warm sub-whoosh |
| **MOGRAPH-MIX-FLAT** | Talking-head + graphic HUD | White camera corner brackets + floating dot pill + bold black/orange split word box | Box: `#09090B`, Accent: `#F97316`, Text: `#FFFFFF` | Fast punch-in (`1.06x`) on emphasis |
| **NOTED** | Blurred footage + sticky note | Tilted off-white paper note taped at top + numbered checklist (`01..04`) + bottom subtitle | Paper: `#FAF9F6`, Highlight: `#FDE047`, Ink: `#18181B` | Paper slide-in + pencil check animation |
| **PRESS** | Vintage newspaper front-page | Bold serif headline + thin horizontal rules + left framed talking-head box + right column lines | Paper: `#F3EFE6`, Ink: `#1C1917` | Subtle paper grain + type reveal |
| **SPOTLIGHT** | Deep obsidian-emerald stat card | Radial spotlight + italic serif eyebrow + giant yellow-white stat (`24 jam`) + line icon | Bg: `#0B110E`, Accent: `#FACC15`, Text: `#FFFFFF` | Radial light pulse + whoosh |

---

## Flagship Compositing Tricks (from `edit-sesudah.mp4`)

1. **Camera Viewfinder HUD**: Corner white brackets + red dot `REC` top-left + `RAW` pill top-right + running `00:00:04:28` timecode bottom-left.
2. **Floating AI Prompt Bar**: Rounded white pill (`border-radius: 9999px`, soft shadow) with sparkle icon + typed prompt (`Edit video mentahan ini`) + lime-green checkmark badge (`#BEF264`) on completion.
3. **Sliding-Highlight Caption Pill**: Rounded white pill container (`#FFFFFF`, `border-radius: 16px`, `padding: 10px 20px`) with bold uppercase dark text (`#09090B`) where a sliding neon lime-green box (`#D9F99D`) tracks the currently spoken word.

---

## Pro Named Effects Library (15 MotionSmith-Inspired Effects)

Reusable modular effects you can mix into any talking-head or motion-graphic cut:

| Effect ID | Visual Behavior | Implementation Recipe |
| :--- | :--- | :--- |
| **`text-behind-subject`** | Giant bold headline placed behind speaker's head/shoulders | Z-order: Background -> Giant Text -> Cutout Speaker Matte (`rembg`/MediaPipe) |
| **`glass-stat-card`** | Frosted glass card at chest height with self-drawing SVG graph + live counter | `backdrop-filter: blur(14px)`, `rgba(255,255,255,0.12)` border, animated SVG `strokeDashoffset` |
| **`odometer-number-roll`** | Per-digit vertical wheel roll; right-most digits spin fastest | Mask overflow-hidden digit columns with staggered `translateY` spring |
| **`stat-stack-big-number`** | Giant numeral (e.g. `73%`) stacked over a tiny 1-line caption | `120–160px` bold grotesk numeral + `18px` muted caption (`margin-top: 8px`) |
| **`freeze-frame-sticker-outline`** | White flash freezes frame, bg desaturates to grey, speaker gets thick white cutout border + mono-caps name tag | `brightness(2)->1` flash, `saturate(0)` bg, dilated alpha matte stroke (`#FFFFFF`, `6px`) |
| **`over-the-shoulder-proof`** | Camera pushes over left shoulder for BEFORE card, swings to right shoulder for AFTER card, settles center | Animated 2D/3D camera pan/scale (`translate3d` + `scale`) + spring proof cards |
| **`tier-list-build`** | `S/A/B/C/D` tier list behind speaker; items drop into rows while status pill flips `ranking -> ranked` | Background grid layer + staggered item drop + pill text/color flip |
| **`color-grade-wipe`** | Flat log footage swept by a glowing vertical line revealing cinematic color grade | Split `clip-path: inset(0 X% 0 0)` synced to glowing `2px` vertical bar |
| **`slow-creep-snap-zoom`** | Gradual `1.00 -> 1.06` push-in over `2–3s`, then hard `1.15x` snap zoom on the Loud Word | Linear/ease-in creep followed by 4-frame `spring()` snap + sub-hit SFX |
| **`spotlight-dim`** | Dims speaker & background (`brightness(0.35)`) while glowing white/red headline pops center | Animated dark scrim + radial glow text (`text-shadow`) |
| **`checklist-tick`** | Vertical step list where each row ticks green at the exact spoken word timestamp | Staggered row opacity + SVG checkmark draw synced to `words[].start` |
| **`red-strike`** | Phrase gets an animated red strikethrough line drawn across it, then the real answer slides in below | `#EF4444` `scaleX(0->1)` strike bar + lower-line `translateY` reveal |
| **`serif-accent` / `italic-lead-in` / `name-tag`** | Small bold lead + glowing red italic serif word; light italic lead over bold italic word behind head; thin red bar + mono-caps speaker name + small title | Mix grotesque + italic `Playfair Display` + `JetBrains Mono` uppercase tag |
| **`face-track-brackets` + `blur-in-words` + `follow-pill-endcard`** | Corner HUD tracking brackets on face, Gaussian `8px->0px` de-blur word entrance, animated `Follow -> Following` pill + cursor click, and footage-shrink-to-avatar end card | Animated corner SVGs + `filter: blur()` keyframe + centered rounded-square end card |
| **`circular-iris-orbit`** | Circular speaker iris mask centered inside glowing concentric orbital rings with floating topic pills | `clip-path: circle(22%)` + rotating dashed/glowing SVG rings + orbiting pill badges |
