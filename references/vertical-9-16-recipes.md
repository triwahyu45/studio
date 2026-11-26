# 9:16 Vertical Video (1080x1920) Animation Recipes

Guidelines for building high-engagement vertical short films and explainer reels.

---

## 1. Canvas Dimensions & Coordinate Layout
- Canvas Width: `1080px`, Canvas Height: `1920px`.
- Aspect Ratio: `9:16`.
- Safe Zone:
  - Header: `y = 80` to `y = 350`.
  - Main Stage: `y = 380` to `y = 1450`.
  - Captions & Footer: `y = 1480` to `y = 1820`.

---

## 2. Dynamic Animation Techniques

### A. Camera Shake on Impact (e.g. Robot Kicks Ball)
```javascript
let shakeX = 0, shakeY = 0;
if (currentTime > impactTime && currentTime < impactTime + 0.3) {
  const intensity = (1 - (currentTime - impactTime) / 0.3) * 15;
  shakeX = (Math.random() - 0.5) * intensity;
  shakeY = (Math.random() - 0.5) * intensity;
}
ctx.save();
ctx.translate(shakeX, shakeY);
// draw scene
ctx.restore();
```

### B. Speed Lines (Action Rush)
```javascript
function drawSpeedLines(ctx, cx, cy, radius, numLines) {
  ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
  ctx.lineWidth = 2;
  for (let i = 0; i < numLines; i++) {
    const angle = Math.random() * Math.PI * 2;
    const r1 = radius + Math.random() * 50;
    const r2 = r1 + 80 + Math.random() * 100;
    ctx.beginPath();
    ctx.moveTo(cx + Math.cos(angle) * r1, cy + Math.sin(angle) * r1);
    ctx.lineTo(cx + Math.cos(angle) * r2, cy + Math.sin(angle) * r2);
    ctx.stroke();
  }
}
```

### C. Kinetic Subtitle Highlighting (TikTok/Reels Style)
Render text with large bold typography (font-size: 38-44px), highlighting the active spoken word in neon yellow/cyan with a drop shadow.

### D. Zero-Flash Asset Preloading in Headless Render
Always inject images into a hidden DOM container and block frame capture on `window.imagesLoaded`:
```javascript
const totalImgs = Object.keys(assets).length;
let loadedCount = 0;
Object.values(assets).forEach(img => {
  if (img.complete && img.naturalHeight !== 0) loadedCount++;
  else img.onload = () => { loadedCount++; if (loadedCount === totalImgs) window.imagesLoaded = true; };
});
```
This guarantees zero asset flicker or transparent frames across multi-worker browser rendering.

---

## 3. High-End Tech Explainer Layout (Sekilo Karbon Formula & DOM Typography)

To eliminate Canvas 2D font distortion and thick stroke artifacting, use real DOM CSS Flexbox/Grid on top of or alongside canvas simulations:

### A. Proportional CSS Typography Stack
- Font Family: `'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`.
- Modern Glassmorphic Cards:
  ```css
  background: rgba(15, 26, 34, 0.88);
  border: 1.5px solid rgba(255, 255, 255, 0.12);
  border-radius: 24px;
  backdrop-filter: blur(20px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
  ```

### B. 6-Beat Narrative Anatomy
1. **Hook**: Direct question or bold statement with real high-res robot action photo.
2. **Leaderboard / Prestige**: Country/competition badges, ranking table, and big metric stats (`24 TIM KAMPUS | 100% OTONOM`).
3. **Core Question**: Giant punchy inquiry ("Kok robot bisa tahu?").
4. **Sensory Breakdown Flowchart**: Visual step cards with glowing connector dots (`Kamera AI -> Sensor Induktif -> Sensor Jarak`).
5. **Actuator & Physics Simulation**: Top-down arena view showing conveyor sorting and 4-wheel mecanum vector arrows.
6. **Closing Pride Card**: Team podium photo and inspiring national impact statement.

---

## 4. 5-Zone Brand-Chibi 3D Layout & Separate 4:5 Feed Cover

### 5 Mandatory Vertical Zones (`1080×1920`)
1. **Header Zone**: Compact avatar, `@username`, and brand logo cleanly inset from top and side margins.
2. **Upper 2D B-Roll Zone**: High-contrast info cards or real screenshots framed inside clean 2D browser/UI cards — **must never overlap the 3D character's head**.
3. **Center 3D Stage**: Expressive 3D character (lip-sync + pose changes) with diegetic 3D props (floating boards, scales, monitors) and **>= 5 distinct bokeh 3D room/world backgrounds** rotating every `<= 3s`.
4. **Active-Word Subtitle Zone**: Translucent glass/pill container with bold active-word color highlight.
5. **Empty Bottom Safe Zone**: Strictly clear of TikTok/Reels/Shorts bottom UI buttons.

### Separate 4:5 Instagram Feed Cover (`cover.png`)
- Always generate a dedicated `cover.png` alongside the 9:16 video with a **centered 4:5 safe crop box** (max **2-line headline** + centered 3D hero character) so the thumbnail never crops awkwardly on Instagram profile grids.
