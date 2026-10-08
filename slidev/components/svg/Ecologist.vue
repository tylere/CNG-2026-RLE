<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  side: 'left' | 'right'
  mode: 'wander' | 'camera-trap'
  initialX?: number
  immediate?: boolean
}>()

// In wander mode: use original SVG positions. In camera-trap: use initialX from position bridge.
const startX = computed(() =>
  props.initialX ?? (props.side === 'left' ? 360 : 1240)
)

// Expose so the slide can read the mid-animation CSS transform on leave.
const groupRef = ref<SVGGElement | null>(null)
defineExpose({ el: groupRef })

const isWalking = ref(false)
let prevX = 0
let rafId = 0

function tick() {
  if (groupRef.value) {
    const mat = new DOMMatrix(getComputedStyle(groupRef.value).transform)
    isWalking.value = Math.abs(mat.m41 - prevX) > 0.05
    prevX = mat.m41
  }
  rafId = requestAnimationFrame(tick)
}

onMounted(() => { rafId = requestAnimationFrame(tick) })
onUnmounted(() => cancelAnimationFrame(rafId))
</script>

<template>
  <!-- Single root so a parent's :style (e.g. --eco-l-start-tx) is applied and inherited -->
  <g>
  <!-- Left ecologist: clipboard and pencil -->
  <g v-if="side === 'left'" :transform="`translate(${startX} 870)`">
  <g
    ref="groupRef"
    :class="['ecologist', 'eco-l', mode === 'camera-trap' ? 'eco-l-ct' : '', props.immediate ? 'immediate' : '', isWalking ? 'walking' : '']"
  >
    <ellipse cx="4" cy="-1" rx="24" ry="7" fill="rgba(0,0,0,0.32)"/>
    <rect class="leg leg-b" x="-14" y="-58" width="11" height="58" rx="4" fill="#4a5a6e"/>
    <rect class="leg leg-a" x="3" y="-58" width="11" height="58" rx="4" fill="#3d4f61"/>
    <ellipse cx="-8" cy="-2" rx="10" ry="5" fill="#3a2a18"/>
    <ellipse cx="9" cy="-2" rx="10" ry="5" fill="#3a2a18"/>
    <rect x="-16" y="-108" width="34" height="52" rx="5" fill="#5a7a45"/>
    <rect x="-12" y="-98" width="10" height="12" rx="2" fill="#4a6a35" opacity="0.8"/>
    <line x1="-16" y1="-94" x2="-34" y2="-74" stroke="#4a5a6e" stroke-width="10" stroke-linecap="round"/>
    <rect x="-48" y="-84" width="20" height="26" rx="3" fill="#e8d898" stroke="#999" stroke-width="1.5"/>
    <rect x="-48" y="-84" width="20" height="4" rx="1" fill="#c8a830"/>
    <line x1="-45" y1="-76" x2="-31" y2="-76" stroke="#bbb" stroke-width="1.2"/>
    <line x1="-45" y1="-71" x2="-31" y2="-71" stroke="#bbb" stroke-width="1.2"/>
    <line x1="-45" y1="-66" x2="-31" y2="-66" stroke="#bbb" stroke-width="1.2"/>
    <line x1="18" y1="-94" x2="34" y2="-72" stroke="#4a5a6e" stroke-width="10" stroke-linecap="round" class="eco-write"/>
    <line x1="34" y1="-72" x2="26" y2="-58" stroke="#f0c030" stroke-width="4" stroke-linecap="round" class="eco-write"/>
    <line x1="26" y1="-58" x2="23" y2="-53" stroke="#e8e8c0" stroke-width="3" stroke-linecap="round" class="eco-write"/>
    <rect x="-7" y="-118" width="14" height="12" rx="4" fill="#c8a880"/>
    <circle cx="2" cy="-133" r="17" fill="#c8a880"/>
    <circle cx="-4" cy="-135" r="2.5" fill="#444"/>
    <circle cx="9" cy="-135" r="2.5" fill="#444"/>
    <ellipse cx="2" cy="-148" rx="26" ry="6" fill="#8b5e14"/>
    <path d="M-14,-153 Q-14,-175 2,-177 Q18,-175 18,-153 Z" fill="#a07020"/>
    <rect x="-14" y="-154" width="32" height="6" rx="2" fill="#5c3a10"/>
    <rect x="18" y="-78" width="14" height="16" rx="3" fill="#8b7a3a" opacity="0.9"/>
    <line x1="18" y1="-78" x2="18" y2="-94" stroke="#8b7a3a" stroke-width="3"/>
  </g>
  </g>

  <!-- Right ecologist: camera; note the scale(-1 1) flip is on the outer wrapper -->
  <g v-if="side === 'right'" :transform="`translate(${startX} 868) scale(-1 1)`">
  <g
    ref="groupRef"
    :class="['ecologist', 'eco-r', mode === 'camera-trap' ? 'eco-r-ct' : '', props.immediate ? 'immediate' : '', isWalking ? 'walking' : '']"
  >
    <ellipse cx="4" cy="-1" rx="24" ry="7" fill="rgba(0,0,0,0.32)"/>
    <rect class="leg leg-b" x="-14" y="-58" width="11" height="58" rx="4" fill="#5c4a3a"/>
    <rect class="leg leg-a" x="3" y="-58" width="11" height="58" rx="4" fill="#503e30"/>
    <ellipse cx="-8" cy="-2" rx="10" ry="5" fill="#2a2010"/>
    <ellipse cx="9" cy="-2" rx="10" ry="5" fill="#2a2010"/>
    <rect x="-16" y="-108" width="34" height="52" rx="5" fill="#c87a40"/>
    <rect x="-12" y="-100" width="10" height="14" rx="2" fill="#a85f28" opacity="0.8"/>
    <rect x="2" y="-100" width="10" height="14" rx="2" fill="#a85f28" opacity="0.8"/>
    <line x1="-16" y1="-94" x2="-26" y2="-115" stroke="#5c4a3a" stroke-width="10" stroke-linecap="round" class="eco-cam-arm"/>
    <line x1="18" y1="-94" x2="26" y2="-115" stroke="#5c4a3a" stroke-width="10" stroke-linecap="round" class="eco-cam-arm"/>
    <rect x="-30" y="-126" width="36" height="22" rx="4" fill="#222" class="eco-cam-arm"/>
    <circle cx="-6" cy="-115" r="8" fill="#333" class="eco-cam-arm"/>
    <circle cx="-6" cy="-115" r="5" fill="#1a1a2a" class="eco-cam-arm"/>
    <circle cx="-6" cy="-115" r="2.5" fill="#0a0a18" class="eco-cam-arm"/>
    <rect x="2" y="-126" width="6" height="5" rx="1" fill="#444" class="eco-cam-arm"/>
    <rect x="-32" y="-128" width="8" height="5" rx="1" fill="#fff" class="cam-flash" opacity="0"/>
    <rect x="-7" y="-118" width="14" height="12" rx="4" fill="#d0b090"/>
    <circle cx="2" cy="-133" r="17" fill="#d0b090"/>
    <ellipse cx="-4" cy="-135" rx="3" ry="2" fill="#333"/>
    <ellipse cx="9" cy="-135" rx="3" ry="2" fill="#333"/>
    <ellipse cx="2" cy="-148" rx="20" ry="5" fill="#2a4a9a"/>
    <ellipse cx="2" cy="-150" rx="18" ry="8" fill="#3a5aaa"/>
    <path d="M-18,-149 Q-28,-148 -26,-144 Q-16,-146 -18,-149 Z" fill="#2a4a9a"/>
    <path d="M-28,-120 Q0,-108 26,-120" stroke="#6a5a40" stroke-width="3" fill="none"/>
  </g>
  </g>
  </g>
</template>

<style scoped>
.ecologist { opacity: 0; }

.ecologist.eco-l {
  animation: eco-l-wander 120s linear 1s both;
  animation-play-state: var(--play-state, paused);
}

.ecologist.eco-r {
  animation: eco-r-wander 120s linear 3s both;
  animation-play-state: var(--play-state, paused);
}

/* immediate: skip the walk-in, start already visible at position 0 */
.ecologist.eco-l.immediate,
.ecologist.eco-r.immediate {
  animation-delay: -10s;
  animation-fill-mode: none;
}

.ecologist.eco-l-ct {
  animation: eco-l-ct-sequence 60s linear 0s 1 both;
  animation-play-state: var(--play-state, paused);
}

.ecologist.eco-r-ct {
  animation: eco-r-ct-sequence 60s linear 0s 1 both;
  animation-play-state: var(--play-state, paused);
}

.eco-write {
  animation: eco-write 1.8s ease-in-out 15s infinite both;
  animation-play-state: var(--play-state, paused);
}

/* Camera-trap slide: work the arms while attaching the acoustic sensor (2.6–6.2s) */
.ecologist.eco-l-ct .eco-write {
  animation: eco-write 0.9s ease-in-out 2.6s 4 both;
  animation-play-state: var(--play-state, paused);
}

.cam-flash {
  opacity: 0;
  animation: cam-flash 10s ease-out 16s infinite both;
  animation-play-state: var(--play-state, paused);
}

.leg-a, .leg-b {
  transform-box: fill-box;
  transform-origin: 50% 0%;
  transition: transform 0.2s ease-out;
}

.walking .leg-a {
  animation: leg 0.6s ease-in-out infinite alternate;
  animation-play-state: var(--play-state, paused);
  transition: none;
}

.walking .leg-b {
  animation: leg 0.6s ease-in-out -0.6s infinite alternate;
  animation-play-state: var(--play-state, paused);
  transition: none;
}

@keyframes eco-l-wander {
  0%    { opacity: 0; transform: translateX(-330px); }  /* just inside the slide edge, fading in */
  1%    { opacity: 1; }
  8%    { opacity: 1; transform: translateX(0); }
  18%   { transform: translateX(0); }
  22%   { transform: translateX(180px); }
  31%   { transform: translateX(180px); }
  35%   { transform: translateX(-100px); }
  44%   { transform: translateX(-100px); }
  48%   { transform: translateX(0); }
  57%   { transform: translateX(0); }
  61%   { transform: translateX(80px); }
  70%   { transform: translateX(80px); }
  74%   { transform: translateX(-100px); }
  83%   { transform: translateX(-100px); }
  87%   { transform: translateX(180px); }
  96%   { transform: translateX(180px); }
  100%  { transform: translateX(0); }
}

@keyframes eco-r-wander {
  0%    { opacity: 0; transform: translateX(-330px); }  /* just inside the slide edge, fading in */
  1%    { opacity: 1; }
  8%    { opacity: 1; transform: translateX(0); }
  20%   { transform: translateX(0); }
  24%   { transform: translateX(-80px); }
  33%   { transform: translateX(-80px); }
  37%   { transform: translateX(100px); }
  47%   { transform: translateX(100px); }
  51%   { transform: translateX(0); }
  60%   { transform: translateX(0); }
  64%   { transform: translateX(60px); }
  73%   { transform: translateX(60px); }
  77%   { transform: translateX(-80px); }
  86%   { transform: translateX(-80px); }
  90%   { transform: translateX(0); }
  100%  { transform: translateX(0); }
}

@keyframes eco-l-ct-sequence {
  /* While the right eco sets up the tripod: walk from the saved slide-5 position to just left of
     the big tree at x≈337, so the right hand reaches the trunk (0–4.17% = 0–2.5s;
     screen_x = 360 + translateX), attach the acoustic sensor (to 10.33% = 6.2s) */
  0%      { opacity: 1; transform: translateX(var(--eco-l-start-tx, 0px)); }
  4.17%   { opacity: 1; transform: translateX(-63px); }
  10.33%  { opacity: 1; transform: translateX(-63px); }
  /* Walk off screen left over next ~14s (10.33–33.33% = 6.2–20s) */
  33.33%  { opacity: 0; transform: translateX(-500px); }
  100% { opacity: 0; transform: translateX(-500px); }
}

@keyframes eco-r-ct-sequence {
  /* Walk from saved position to camera at x=850 (0–8.33% = 0–5s).
     screen_x = 1240 - CSS_translateX; so x=850 → translateX=390 */
  0%      { opacity: 1; transform: translateX(var(--eco-r-start-tx, 0px)); }
  8.33%   { opacity: 1; transform: translateX(390px); }
  /* Hold to place tripod (8.33–10.33% = 5–6.2s) */
  10.33%  { opacity: 1; transform: translateX(390px); }
  /* Walk off screen right (10.33–33.33% = 6.2–20s).
     screen_x = 1240 - (-480) = 1720 */
  33.33%  { opacity: 0; transform: translateX(-480px); }
  100% { opacity: 0; transform: translateX(-480px); }
}

@keyframes eco-write {
  0%, 100%  { transform: translate(0, 0); }
  25%       { transform: translate(-3px, -4px); }
  50%       { transform: translate(4px, -2px); }
  75%       { transform: translate(-2px, 3px); }
}

@keyframes cam-flash {
  0%, 4%, 100% { opacity: 0; }
  1%           { opacity: 0.9; }
  2%           { opacity: 0; }
  3%           { opacity: 0.7; }
}

@keyframes leg {
  from { transform: rotate(-18deg); }
  to   { transform: rotate(18deg); }
}
</style>
