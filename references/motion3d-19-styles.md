# Procedural 3D Three.js + Remotion / Playwright Styles (19+ Presets)

Production blueprints for rendering 60fps/30fps procedural 3D shorts (9:16 `1080×1920` or 16:9 `1920×1080`) locally using **Three.js** inside **Remotion** (`@remotion/three`) or **Playwright WebGL** + **FFmpeg**, without diffusion models.

---

## 1. Exploded Hardware & Architectural Cutaways

| Preset | Scene & Lighting Rig | Geometry, Materials & Animation | HUD & Typography |
| :--- | :--- | :--- | :--- |
| **PRECISION** | Studio off-white (`#E8E8E6`), soft `RectAreaLight` + hemisphere fill | High-detail PBR exploded hardware stack (`MeshStandardMaterial` matte/anodized metal) separating vertically along Y-axis with smooth spring | Thin hairline `#71717A` leader lines + uppercase tracked micro-specs (`01 SEAMLESS DESIGN`) |
| **BONGKAR** | Pure bright white studio (`#F8FAFC`), soft ground contact shadow | Exploded mechanical parts (frame, engine, wheels, fairing) fanning out in 3D space with gentle hover oscillation | Bold top title (`BONGKAR`) + italic sub-label + bottom dark caption |
| **TIMEFORGE** | Clean light gradient (`#F1F5F9`→`#E2E8F0`), crisp key light | Sleek 3D device/product rotating and morphing across eras over a curved bottom timeline dial | Giant year (`2026`) + circular UI dial + bottom arc timeline (`1990..2026`) |
| **INNERWORKS** | Bright isometric architectural studio (`#F1F5F9`) | Cutaway multi-floor shaft/machine with animated elevator car, pulleys, cables, and gears | Clean top pill indicator (`LANTAI 3`) + crisp technical arrows |
| **BEDAH** | Natural daylight directional sun + soft sky fill | 3D cross-section building sitting atop multi-layered soil/rock subsurface cutaway (`#78350F` / `#451A03`) | Clean lower-third narration subtitle |
| **BUILDFORGE** | Soft daylight architectural viz | Procedural house assembly: foundation → columns → walls → glass → roof snapping into place with spring bounce | Minimal top-left chapter tag (`04 RUMAH HIDUP`) |

---

## 2. Voxel, HD-2D & Miniature Worlds

| Preset | Scene & Lighting Rig | Geometry, Materials & Animation | HUD & Typography |
| :--- | :--- | :--- | :--- |
| **VOXELVERSE** | Cozy interior: warm `PointLight` desk lamp (`#F59E0B`) + cool ambient fill | Blocky voxel character + room props (`BoxGeometry` grid) with subtle breathing/head-turn animation | Optional glowing monitor code screen + cinematic shadow depth |
| **PIXELSTORY** | Octopath-inspired HD-2D: warm golden `PointLight` + radial bloom + tilt-shift DoF | Crisp 2D pixel-art character sprite (`NearestFilter`, billboarded plane) inside a rich 3D lit wood/stone room | Warm glowing floating orb particles + soft vignette |
| **WORLDFORGE-ROMA** | Golden-hour directional sun (`#FDBA74`) + crisp `PCFSoftShadowMap` | Procedural `InstancedMesh` classical terracotta-roof city grid + marble forum columns + slow aerial dolly/orbit | Bold wide-tracked white uppercase title (`R O M A`) |
| **WORLDFORGE-MARS** | Rusty Martian sun + atmospheric orange-red fog (`#9A3412`) | Procedural sci-fi geodesic habitat domes, pressurized tubes, solar arrays, and red terrain heightmap | Clean aerial orbit camera over dusty surface |
| **NEGERI** | Bright daylight isometric orthocam | Low-poly green terrain tiles, miniature houses, roads, and trees popping up sequentially | Floating white rounded HUD card (`POPULASI 12.029 warga`) + top day pill (`HARI 1`) |
| **VOXEL-TERMINAL SPLIT** | Split-screen dark terminal (`#0B0F14`) + crisp isometric pastel/clay 3D voxel stage | Top/bottom or left/right split: animated CLI/code typewriter with syntax-highlighted output synced to an isometric 3D voxel/clay miniature scene reacting to each command | Monospace status pill (`EXEC 01`) + subtle scanline/cursor pulse (`> _`) |

---

## 3. Tactile Diorama & Silhouette

| Preset | Scene & Lighting Rig | Geometry, Materials & Animation | HUD & Typography |
| :--- | :--- | :--- | :--- |
| **PAPERWORLD** | Multi-plane diorama stage with warm glowing inner window (`#FDE047`) + rim shadow | Layered paper-cutout planes (`DoubleSide`, subtle paper bump texture) + hanging string stars/moon swaying gently | Soft depth-of-field + cozy fairy-tale atmosphere |
| **STORYBOOK** | Warm nursery spotlight | Stitched felt/fabric texture planes (`roughness: 0.95`) with visible dashed stitch borders + cute cutout character | Flat storybook framing + warm saturated primary colors |
| **CHRONICLE** | Dramatic backlit volcanic orange-red sky (`#C2410C`→`#7C2D12`) | Pitch-black 3D foreground silhouettes (palm trees, figures, mountain) + glowing purple/white lightning & ash particles | Clean uppercase header (`KERAJAAN TAMBORA`) + crisp lower subtitle |

---

## 4. 3D Stylized Character Comedy / Drama & Cel-Shaded Comic

| Preset | Scene & Lighting Rig | Geometry, Materials & Animation | HUD & Typography |
| :--- | :--- | :--- | :--- |
| **CHARACTERFLOW** | Bright studio 3-point lighting | Smooth matte-clay capsule/sphere 3D characters (`roughness: 0.7`) + animated floating white thought-bubble | Clean pill dialogue/thought bubble above character |
| **CINESTORY** | Moody dramatic 3-point rim + cool fill | Close-up expressive 3D character storytelling with subtle eye/head micro-motion & shallow DoF | High-contrast yellow-on-dark highlighted subtitle (`Damar terdiam.`) |
| **NEKAT** | Bright saturated comedy lighting | Chubby stylized 3D character driving/reacting inside crowded chaotic scene (e.g. dozens of instanced cats) | Top-center dark pill counter (`KUCING 1.024`) + bold outlined subtitle |
| **CERDIK** | Warm indoor key light + soft shadow | 2D/3D cel-shaded flat-face character with crisp black ink outlines (directly compatible with `cartoon-3d-short` skill) | Bold clean centered white subtitle |
| **PANELVERSE** | Flat comic page lighting (`#F5EFE0` paper) | Animated 3-panel vertical comic strip with speedline sunbursts (`#EF4444`/`#FACC15`) & panel-by-panel reveal | Crisp black comic panel borders (`4px solid #09090B`) |
| **TIPIKAL** | Bright cel-shaded street scene | Bold black-outlined cel-shaded characters on scooter/street + animated white comic speech bubbles | Top dual-color banner (`TIPE-TIPE PENGENDARA MOTOR`) |

---

## 5. Three.js r186+ Anti-Hallucination Guardrails (`cloudai-x/threejs-skills`)

When generating procedural 3D scenes with modern **Three.js (`r186+`)**, **React Three Fiber (`9.8+`)**, and **drei (`10.7+`)**, avoid outdated r160 APIs:
- **Environment Maps**: Use `HDRLoader` (replaces deprecated `RGBELoader`).
- **Frame Timing**: Use `Timer` (replaces `Clock` for deterministic/clean delta timing).
- **Post-Processing**: Use `RenderPipeline` (replaces legacy `PostProcessing` / `EffectComposer` patterns).
- **Renderer**: WebGL 1 support is removed; target `WebGLRenderer` (WebGL 2) or `WebGPURenderer` with **TSL (Three Shading Language)** for custom shaders/materials.
- **High-Count Instancing**: Use `BatchedMesh` / `InstancedMesh` for cityscapes (`WORLDFORGE-ROMA`, `WORLDFORGE-MARS`) and crowd/prop scenes (`NEKAT`) to keep 60fps render times fast.
