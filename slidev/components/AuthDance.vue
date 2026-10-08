<script setup lang="ts">
// A mosh pit of services, bumping, jumping and flailing.
// Point: getting these services to work together (auth) is the hard part.
import { reactive, computed, watch, onUnmounted } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const dancers = [
  { key: 'gcp', label: 'Google Cloud', icon: '/images/google_cloud_mark.svg' },
  { key: 'github', label: 'GitHub', icon: '/images/github_mark.svg' },
  { key: 'cdn', label: 'CDN' },
  { key: 'storage', label: 'Object storage' },
  { key: 'dev', label: 'Dev environment' },
]

// Body geometry (origin = between the feet on the ground)
const W = 250           // card width
const SH = -165         // shoulder height
const ARM = 70          // arm length

// Mosh pit: everyone wanders the floor on random paths, bumps into each other, jumps and flails.
const FLOOR = { x0: 170, x1: 1430, y0: 600, y1: 830 }   // where feet can be
const rand = (lo: number, hi: number) => lo + Math.random() * (hi - lo)

const state = dancers.map((_, i) => ({
  x: FLOOR.x0 + (i + 0.5) * (FLOOR.x1 - FLOOR.x0) / dancers.length, y: rand(FLOOR.y0 + 60, FLOOR.y1),
  vx: 0, vy: 0, tx: 0, ty: 0, nextT: 0,          // target and when to pick a new one
  jumpT: rand(0.5, 2), jumpH: 0,                  // next jump time, current height
  arms: [rand(-80, 80), rand(-80, 80)], armT: [rand(-80, 80), rand(-80, 80)], nextArm: 0,
  ph: rand(0, 6.28),
}))
const pose = reactive(dancers.map(() => ({ x: 0, y: 0, s: 1, aL: 60, aR: 60, lL: 0, lR: 0, z: 0, tilt: 0 })))

let last = 0
function update(t: number) {
  const dt = Math.min(0.05, Math.max(0, t - last)); last = t
  state.forEach((S, i) => {
    // New random target every 0.8–2.2 s
    if (t >= S.nextT) { S.tx = rand(FLOOR.x0, FLOOR.x1); S.ty = rand(FLOOR.y0, FLOOR.y1); S.nextT = t + rand(0.8, 2.2) }
    // Steer towards target with jitter
    S.vx += ((S.tx - S.x) * 2.2 + rand(-900, 900)) * dt
    S.vy += ((S.ty - S.y) * 2.2 + rand(-500, 500)) * dt
    // Bump: push away from anyone too close
    state.forEach((O, j) => {
      if (j === i) return
      const dx = S.x - O.x, dy = (S.y - O.y) * 2.5, d = Math.hypot(dx, dy) || 1
      if (d < 230) { const f = (230 - d) * 14 * dt; S.vx += dx / d * f * 18; S.vy += dy / d * f * 4 }
    })
    S.vx *= 0.9; S.vy *= 0.9
    S.x = Math.min(FLOOR.x1, Math.max(FLOOR.x0, S.x + S.vx * dt))
    S.y = Math.min(FLOOR.y1, Math.max(FLOOR.y0, S.y + S.vy * dt))
    // Random jumps
    if (t >= S.jumpT) { S.jumpH = rand(60, 130); S.jumpT = t + rand(0.9, 2.4) }
    const sinceJump = 1 - (S.jumpT - t) / 2.4
    const hop = Math.max(0, S.jumpH * Math.sin(Math.min(1, sinceJump * 2.4) * Math.PI))
    // Flailing arms: new random targets often, eased toward
    if (t >= S.nextArm) { S.armT = [rand(-85, 75), rand(-85, 75)]; S.nextArm = t + rand(0.15, 0.5) }
    S.arms[0] += (S.armT[0] - S.arms[0]) * Math.min(1, dt * 12)
    S.arms[1] += (S.armT[1] - S.arms[1]) * Math.min(1, dt * 12)

    const P = pose[i]
    const s = 0.62 + 0.38 * (S.y - FLOOR.y0) / (FLOOR.y1 - FLOOR.y0)   // further back = smaller
    P.x = S.x; P.y = S.y - hop * s; P.s = s
    P.aL = S.arms[0]; P.aR = S.arms[1]
    const step = 18 * Math.sin(t * 11 + S.ph)
    P.lL = hop > 5 ? -20 : step; P.lR = hop > 5 ? 20 : -step
    P.tilt = Math.max(-12, Math.min(12, S.vx * 0.02)) + 4 * Math.sin(t * 7 + S.ph)
    P.z = S.y
  })
}

const order = computed(() => dancers.map((d, i) => ({ d, i })).sort((a, b) => pose[a.i].z - pose[b.i].z))

// Arm/leg endpoints
const arm = (side: -1 | 1, deg: number) => {
  const r = deg * Math.PI / 180
  return { x1: side * W / 2, y1: SH, x2: side * (W / 2 + ARM * Math.cos(r)), y2: SH + ARM * Math.sin(r) }
}
const leg = (side: -1 | 1, deg: number) => {
  const r = deg * Math.PI / 180, hx = side * 42, hy = -105, L = 100
  return { x1: hx, y1: hy, x2: hx + L * Math.sin(r), y2: hy + L * Math.cos(r) }
}

// Run only while this slide is showing
const { $page } = useSlideContext()
const { currentPage } = useNav()
let raf = 0, t0 = 0
watch(() => currentPage.value === $page.value, (active) => {
  cancelAnimationFrame(raf)
  if (!active) return
  t0 = performance.now()
  const loop = (now: number) => { update((now - t0) / 1000); raf = requestAnimationFrame(loop) }
  raf = requestAnimationFrame(loop)
}, { immediate: true })
update(0)
onUnmounted(() => cancelAnimationFrame(raf))
</script>

<template>
  <div class="auth-dance">
    <div class="title a-rise">
      <span class="statement">The hardest part? <span class="hl">Authentication</span></span>
      <span class="statement-sub muted">getting these services to dance together</span>
    </div>

    <svg class="floor" viewBox="0 0 1600 900">
      <!-- Back wall and dance floor -->
      <rect x="0" y="470" width="1600" height="10" fill="rgba(242,244,246,0.06)"/>
      <path d="M0 900 L240 480 L1360 480 L1600 900 Z" fill="rgba(65,139,217,0.07)"/>

      <g v-for="{ d, i } in order" :key="d.key" :transform="`translate(${pose[i].x} ${pose[i].y}) scale(${pose[i].s}) rotate(${pose[i].tilt} 0 -150)`">
        <!-- Legs and feet -->
        <g v-for="side in ([-1, 1] as const)" :key="`leg${side}`">
          <line v-bind="leg(side, side < 0 ? pose[i].lL : pose[i].lR)" class="limb"/>
          <ellipse :cx="leg(side, side < 0 ? pose[i].lL : pose[i].lR).x2 + side * 8" :cy="leg(side, side < 0 ? pose[i].lL : pose[i].lR).y2" rx="20" ry="9" fill="#8a93a3"/>
        </g>
        <!-- Arms and hands -->
        <g v-for="side in ([-1, 1] as const)" :key="`arm${side}`">
          <line v-bind="arm(side, side < 0 ? pose[i].aL : pose[i].aR)" class="limb"/>
          <circle :cx="arm(side, side < 0 ? pose[i].aL : pose[i].aR).x2" :cy="arm(side, side < 0 ? pose[i].aL : pose[i].aR).y2" r="11" fill="#f4f5f7"/>
        </g>
        <!-- Body: the service card -->
        <foreignObject :x="-W / 2" y="-240" :width="W" height="135">
          <div class="card">
            <img v-if="d.icon" :src="d.icon" alt="" class="icon" />
            <svg v-else-if="d.key === 'cdn'" viewBox="0 0 64 64" class="icon">
              <circle cx="32" cy="32" r="22" fill="none" stroke="#418BD9" stroke-width="4"/>
              <ellipse cx="32" cy="32" rx="10" ry="22" fill="none" stroke="#418BD9" stroke-width="3"/>
              <path d="M10 32 H54 M14 21 H50 M14 43 H50" stroke="#418BD9" stroke-width="3"/>
              <circle cx="8" cy="12" r="5" fill="#e0595a"/><circle cx="56" cy="12" r="5" fill="#e0595a"/>
              <circle cx="8" cy="54" r="5" fill="#e0595a"/><circle cx="56" cy="54" r="5" fill="#e0595a"/>
            </svg>
            <svg v-else-if="d.key === 'storage'" viewBox="0 0 64 64" class="icon">
              <ellipse cx="32" cy="14" rx="22" ry="7" fill="#5bb58a"/>
              <path d="M10 14 L16 54 Q32 62 48 54 L54 14 Q32 22 10 14 Z" fill="#3f8f69"/>
              <ellipse cx="32" cy="14" rx="22" ry="7" fill="none" stroke="#2c6b4d" stroke-width="2"/>
              <path d="M14 30 Q32 37 50 30" fill="none" stroke="#2c6b4d" stroke-width="2"/>
            </svg>
            <svg v-else viewBox="0 0 64 64" class="icon">
              <!-- Laptop with a terminal prompt -->
              <rect x="10" y="12" width="44" height="30" rx="3" fill="#1D232B"/>
              <path d="M17 22 L23 27 L17 32" fill="none" stroke="#5dff7a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M27 33 H36" stroke="#5dff7a" stroke-width="3" stroke-linecap="round"/>
              <path d="M4 46 H60 L56 52 H8 Z" fill="#8a93a3"/>
            </svg>
            <span class="label">{{ d.label }}</span>
          </div>
        </foreignObject>
      </g>
    </svg>
  </div>
</template>

<style scoped>
.auth-dance { position: absolute; inset: 0; }

.title {
  position: absolute; top: 44px; left: 0; right: 0; z-index: 1;
  display: flex; flex-direction: column; align-items: center; gap: 0.6rem; text-align: center;
}

.floor { position: absolute; inset: 0; width: 100%; height: 100%; }
.limb { stroke: #f4f5f7; stroke-width: 12; stroke-linecap: round; }

.card {
  box-sizing: border-box; width: 100%; height: 100%;
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px;
  background: #f4f5f7; border-radius: 18px;
  box-shadow: 0 8px 22px rgba(0, 0, 0, 0.45);
}
.icon { width: 54px; height: 54px; display: block; }
.label { font-size: 26px; font-weight: 700; color: #1D232B; white-space: nowrap; line-height: 1; }
</style>
