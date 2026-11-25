# 3D Kinematics & Parallel Rendering Engine

Advanced techniques for deterministic 3D animation, robot kinematics visualization, and 4x accelerated video frame rendering in headless browsers.

---

## 1. Robust 3D LookAt Camera Matrix

Never use naive Euler pitch-yaw rotation for 3D canvas cameras; elevation angles cause targets to drift and shift models off-screen. Always use a vector LookAt basis:

```javascript
class Vec3 {
  constructor(x, y, z) { this.x = x; this.y = y; this.z = z; }
}

function setupCamera(eye, target, up = new Vec3(0, 1, 0)) {
  const f = normalize(new Vec3(target.x - eye.x, target.y - eye.y, target.z - eye.z));
  const r = normalize(cross(f, up));
  const u = cross(r, f);
  return { eye, target, r, u, f };
}

function project(p, cam, fov = 1100, cx = 540, cy = 960) {
  const prel = new Vec3(p.x - cam.eye.x, p.y - cam.eye.y, p.z - cam.eye.z);
  const xc = dot(prel, cam.r);
  const yc = dot(prel, cam.u);
  const zc = dot(prel, cam.f);
  if (zc <= 20) return null;
  const scale = fov / zc;
  return { x: cx + xc * scale, y: cy - yc * scale, scale: scale, zc: zc };
}
```
*Benefit: Target `(0, 0, 0)` is guaranteed to project dead-center at `(cx, cy)` at every azimuth orbit angle.*

---

## 2. Robotics Kinematics Modules

### A. 3-DOF Analytical Inverse Kinematics (Manipulator Arm)
```javascript
const dx = tx - shoulder.x;
const dy = ty - shoulder.y;
const dz = tz - shoulder.z;

const theta1 = Math.atan2(dz, dx); // Base yaw
const rDist = Math.hypot(dx, dz);
const dReach = Math.min(Math.hypot(rDist, dy), L1 + L2 + L3 - 10);

const cosTheta3 = (dReach * dReach - L1 * L1 - L2 * L2) / (2 * L1 * L2);
const theta3 = Math.acos(Math.max(-1, Math.min(1, cosTheta3)));
const theta2 = Math.atan2(dy, rDist) - Math.atan2(L2 * Math.sin(theta3), L1 + L2 * Math.cos(theta3));
```

### B. 3-Wheel Holonomic Omni-Drive Kinematics
```javascript
// Wheels spaced at 0°, 120°, 240°
const wheelAngles = [0, 120, 240];
wheelAngles.forEach((wAngle, idx) => {
  const rad = wAngle * Math.PI / 180;
  const tanA = rad + Math.PI / 2; // Tangent wheel velocity vector
  const wx = chassisCenter.x + Math.cos(rad) * radius;
  const wz = chassisCenter.z + Math.sin(rad) * radius;
  // Draw tangent velocity vector v_i = -vx*sin(rad) + vy*cos(rad) + R*omega
});
```

### C. Bipedal Gait & Zero Moment Point (ZMP)
Oscillate hip/knee angles in antiphase with foot trajectory ground clearance, projecting the ZMP marker dynamically under the support polygon.

---

## 3. Parallel Multi-Worker Frame Rendering (3.4x Faster)

Instead of single-threaded Playwright screenshot loops (4-5 fps), slice the timeline across 4 background headless Edge/Chromium workers using Python `multiprocessing`:

```python
from multiprocessing import Process
from playwright.sync_api import sync_playwright

def render_slice(worker_id, start_frame, end_frame):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1920})
        page.goto(html_url)
        for i in range(start_frame, end_frame):
            page.evaluate(f"renderFrame({i / 30.0})")
            page.screenshot(path=f"frames/frame_{i:04d}.png")
        browser.close()
```
*Result: 1,410 frames rendered in 85s instead of 290s.*
