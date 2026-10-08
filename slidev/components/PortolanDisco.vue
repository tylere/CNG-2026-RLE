<script setup lang="ts">
// A Portolan stick figure on a 70s dance floor, in three acts once `start` becomes true:
//   dark   – everything still and dim; Portolan stands facing away (no logo visible)
//   lights – the room lights slowly come up and Portolan turns around
//   groove – the floor and mirror ball light up and Portolan starts the disco point
import { ref, watch, onUnmounted } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const tiles = Array.from({ length: 4 * 7 }, (_, i) => ({ c: i % 7, r: Math.floor(i / 7) }))
const tileColors = ['#e0595a', '#FFD626', '#418BD9', '#5bb58a', '#c85fa0']

const props = defineProps<{ start?: boolean }>()

// Timeline (seconds after `start`)
const LIGHTS_AT = 0.3
const TURN_AT = 1.9
const GROOVE_AT = 3.1

const phase = ref<'dark' | 'lights' | 'turn' | 'groove'>('dark')
const { $page } = useSlideContext()
const { currentPage } = useNav()
let timers: ReturnType<typeof setTimeout>[] = []
const clear = () => { timers.forEach(clearTimeout); timers = [] }
watch(() => currentPage.value === $page.value && !!props.start, (go) => {
  clear()
  phase.value = 'dark'
  if (!go) return
  timers.push(setTimeout(() => (phase.value = 'lights'), LIGHTS_AT * 1000))
  timers.push(setTimeout(() => (phase.value = 'turn'), TURN_AT * 1000))
  timers.push(setTimeout(() => (phase.value = 'groove'), GROOVE_AT * 1000))
}, { immediate: true })
onUnmounted(clear)
</script>

<template>
  <svg viewBox="0 0 700 760" class="disco" :class="`phase-${phase}`" aria-label="A Portolan stick figure disco dancing under a mirror ball">
    <g class="room">
      <!-- Light-up dance floor (perspective rows) -->
      <g v-for="t in tiles" :key="`${t.c}-${t.r}`">
        <polygon
          class="tile"
          :style="{ '--tile': tileColors[(t.c * 3 + t.r * 2) % tileColors.length], animationDelay: `${-((t.c + t.r * 3) % 5) * 0.4}s` }"
          :points="(() => {
            const y0 = 600 + t.r * 38, y1 = y0 + 36
            const w0 = 60 + t.r * 12, w1 = 60 + (t.r + 1) * 12
            const x = (w: number, c: number) => 350 + (c - 3.5) * w
            return `${x(w0, t.c) + 2},${y0} ${x(w0, t.c + 1) - 2},${y0} ${x(w1, t.c + 1) - 2},${y1} ${x(w1, t.c) + 2},${y1}`
          })()"
        />
      </g>

      <!-- Mirror ball and light beams -->
      <line x1="350" y1="0" x2="350" y2="40" stroke="#8a93a3" stroke-width="3"/>
      <g class="beams">
        <polygon points="350,80 120,600 200,600" fill="rgba(255,214,38,0.10)"/>
        <polygon points="350,80 540,600 620,600" fill="rgba(200,95,160,0.10)"/>
        <polygon points="350,80 320,600 400,600" fill="rgba(65,139,217,0.10)"/>
      </g>
      <g transform="translate(350 82)">
        <circle class="ball" r="42" fill="#c9ced6"/>
        <g class="facets">
          <path v-for="k in 6" :key="`v${k}`" :d="`M${-42 + k * 12} -40 Q${-42 + k * 12 + (k - 3.5) * 4} 0 ${-42 + k * 12} 40`" fill="none" stroke="#8a93a3" stroke-width="1.5"/>
        </g>
        <path d="M-41 -12 H41 M-42 0 H42 M-41 12 H41 M-36 -24 H36 M-36 24 H36" stroke="#8a93a3" stroke-width="1.5"/>
        <circle class="sparkle" cx="-16" cy="-18" r="5" fill="#fff"/>
        <circle class="sparkle s2" cx="20" cy="8" r="4" fill="#fff"/>
      </g>

      <!-- The dancer: origin between the feet on the floor -->
      <g transform="translate(350 640)">
        <g class="hips">
          <!-- Legs and flared trouser cuffs -->
          <rect class="leg leg-l" x="-48" y="-120" width="13" height="118" rx="6.5" fill="#f4f5f7"/>
          <rect class="leg leg-r" x="35" y="-120" width="13" height="118" rx="6.5" fill="#f4f5f7"/>
          <path class="leg leg-l" d="M-56 -8 H-27 L-23 2 H-60 Z" fill="#c85fa0"/>
          <path class="leg leg-r" d="M27 -8 H56 L60 2 H23 Z" fill="#c85fa0"/>

          <!-- Arms: hand on hip (left), disco point (right); hanging down until the groove -->
          <g transform="translate(-125 -185)">
            <rect class="arm arm-hip" x="-82" y="-6.5" width="82" height="13" rx="6.5" fill="#f4f5f7"/>
          </g>
          <g transform="translate(125 -185)">
            <g class="arm arm-point">
              <rect x="0" y="-6.5" width="96" height="13" rx="6.5" fill="#f4f5f7"/>
              <circle cx="98" cy="0" r="10" fill="#f4f5f7"/>
            </g>
          </g>

          <!-- Body: the Portolan card, which flips from its plain back to its logo side -->
          <g class="flip">
            <rect x="-125" y="-262" width="250" height="140" rx="18" fill="#f4f5f7"/>
            <g class="back">
              <rect x="-125" y="-262" width="250" height="140" rx="18" fill="#d9dde3"/>
              <path d="M-90 -230 H90 M-90 -192 H90 M-90 -154 H90" stroke="#c4c9d1" stroke-width="3"/>
            </g>
            <g class="front">
              <image href="/images/portolan_logo_mark.svg" x="-28" y="-250" width="56" height="56"/>
              <text x="0" y="-150" text-anchor="middle" fill="#1D232B" style="font-size:34px; font-weight:700; font-family:'iA Writer Quattro S', sans-serif">Portolan</text>
            </g>
          </g>
        </g>
      </g>
    </g>
  </svg>
</template>

<style scoped>
.disco { width: 100%; height: 100%; overflow: visible; }

/* ---------- Room lighting ---------- */
.room { filter: brightness(0.22) saturate(0.4); transition: filter 2.5s ease-in-out; }
.phase-lights .room, .phase-turn .room, .phase-groove .room { filter: brightness(1) saturate(1); }

/* ---------- Floor, ball and beams: dark and still until the groove ---------- */
.tile { fill: var(--tile); opacity: 0.2; transition: opacity 1s; }
.phase-groove .tile { animation: tile-flash 2s steps(1) infinite; }
@keyframes tile-flash {
  0%, 100% { opacity: 0.25; }
  40%      { opacity: 0.9; }
  60%      { opacity: 0.25; }
}

.beams { opacity: 0; transition: opacity 1.2s; transform-origin: 350px 80px; }
.phase-groove .beams { opacity: 1; animation: beams 4s ease-in-out infinite alternate; }
@keyframes beams { from { transform: rotate(-10deg); } to { transform: rotate(10deg); } }

.ball { transition: fill 1s; }
.phase-groove .ball { fill: #e4e8ee; }
.facets { transform-box: fill-box; transform-origin: center; }
.phase-groove .facets { animation: spin 2.4s linear infinite; }
@keyframes spin { from { transform: scaleX(1); } 50% { transform: scaleX(-1); } to { transform: scaleX(1); } }
.sparkle { opacity: 0; transform-box: fill-box; transform-origin: center; }
.phase-groove .sparkle { animation: sparkle 1.2s ease-in-out infinite; }
.sparkle.s2 { animation-delay: -0.6s; }
@keyframes sparkle { 0%, 100% { opacity: 0.2; transform: scale(0.5); } 50% { opacity: 1; transform: scale(1.4); } }

/* ---------- Turning around ---------- */
.flip { transform-box: fill-box; transform-origin: center; }
.back { opacity: 1; }
.front { opacity: 0; }
.phase-turn .flip { animation: flip 1s ease-in-out both; }
.phase-turn .back { animation: hide-half 1s both; }
.phase-turn .front { animation: show-half 1s both; }
.phase-groove .back { opacity: 0; }
.phase-groove .front { opacity: 1; }
@keyframes flip { 0%, 100% { transform: scaleX(1); } 50% { transform: scaleX(0.04); } }
@keyframes hide-half { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }
@keyframes show-half { 0%, 49% { opacity: 0; } 50%, 100% { opacity: 1; } }

/* ---------- Grooving ---------- */
.hips { transform-box: view-box; transform-origin: 0 0; }
.phase-groove .hips { animation: sway 1.6s ease-in-out infinite; }
@keyframes sway {
  0%, 100% { transform: translateX(-14px) rotate(-4deg); }
  50%      { transform: translateX(14px) rotate(4deg); }
}

.arm, .leg { transform-box: fill-box; transition: transform 0.6s ease-out; }

/* Disco point: up to the right, then down across the body (hangs down when still) */
.arm-point { transform-origin: 0% 50%; transform: rotate(80deg); }
.phase-groove .arm-point { animation: point 1.6s cubic-bezier(0.6, 0, 0.3, 1) infinite; }
@keyframes point {
  0%, 40%   { transform: rotate(-55deg); }
  50%, 90%  { transform: rotate(150deg); }
  100%      { transform: rotate(-55deg); }
}

/* Hand on hip (hangs down when still) */
.arm-hip { transform-origin: 100% 50%; transform: rotate(-80deg); }
.phase-groove .arm-hip { animation: hip 1.6s ease-in-out infinite; }
@keyframes hip {
  0%, 100% { transform: rotate(-60deg); }
  50%      { transform: rotate(-48deg); }
}

/* Knee pops, alternating legs */
.leg { transform-origin: 50% 0%; }
.phase-groove .leg-l { animation: pop-l 1.6s ease-in-out infinite; }
.phase-groove .leg-r { animation: pop-r 1.6s ease-in-out infinite; }
@keyframes pop-l { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(14deg); } }
@keyframes pop-r { 0%, 100% { transform: rotate(-14deg); } 50% { transform: rotate(0deg); } }
</style>
