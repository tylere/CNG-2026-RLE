<script setup lang="ts">
const props = defineProps<{
  tripodGrown?: boolean
}>()
</script>

<template>
  <g class="camera-trap">
    <defs>
      <radialGradient id="ct-ir-glow-g2" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0" stop-color="#ff5500" stop-opacity="0.75"/>
        <stop offset="1" stop-color="#ff5500" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="ct-flash-glow-g" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0"   stop-color="#ffffff" stop-opacity="0.98"/>
        <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.6"/>
        <stop offset="1"   stop-color="#ffffff" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <!-- Camera trap device on tripod; translate(850 750) is scene position -->
    <g transform="translate(850 750)">
      <g class="ct-tripod" :class="{ 'ct-immediate': props.tripodGrown }">
        <!-- Tripod legs: all meet at apex (0,-92) -->
        <line x1="0" y1="-92" x2="-46" y2="0" stroke="#555" stroke-width="5" stroke-linecap="round"/>
        <line x1="0" y1="-92" x2="6" y2="2" stroke="#555" stroke-width="5" stroke-linecap="round"/>
        <line x1="0" y1="-92" x2="44" y2="-5" stroke="#555" stroke-width="5" stroke-linecap="round"/>
        <!-- Camera body centered horizontally on tripod apex (x=0); lens faces right -->
        <rect x="-30" y="-128" width="60" height="40" rx="5" fill="#1c1c1c" stroke="#333" stroke-width="1.5"/>
        <circle class="ct-ir-led" cx="24" cy="-116" r="4" fill="#3a0000" opacity="0.3"/>
        <circle class="ct-ir-led" cx="24" cy="-107" r="4" fill="#3a0000" opacity="0.3"/>
        <circle class="ct-ir-led" cx="16" cy="-116" r="4" fill="#3a0000" opacity="0.3"/>
        <circle class="ct-ir-led" cx="16" cy="-107" r="4" fill="#3a0000" opacity="0.3"/>
        <circle cx="10" cy="-108" r="11" fill="#222" stroke="#555" stroke-width="2"/>
        <circle cx="10" cy="-108" r="7" fill="#111"/>
        <circle cx="10" cy="-108" r="3.5" fill="#080818"/>
        <circle cx="13" cy="-111" r="1.8" fill="rgba(255,255,255,0.22)"/>
        <circle class="ct-status-led" cx="26" cy="-126" r="3" fill="#ff2200" opacity="0.7"/>
      </g>
    </g>
    <!-- IR glow and white flash overlays (scene coordinates) -->
    <ellipse class="ct-ir-flash" cx="950" cy="690" rx="260" ry="180"
      fill="url(#ct-ir-glow-g2)" opacity="0"/>
    <ellipse class="ct-flash" cx="870" cy="690" rx="500" ry="380"
      fill="url(#ct-flash-glow-g)" opacity="0"/>
  </g>
</template>

<style scoped>
/* --ct-flash-delay is inherited from EcosystemScene (set dynamically by the slide).
   --ct-fall-delay is overridable from the parent via :style */

/* Default: single 60s timeline — grow at 15s, fall at ~46s */
.ct-tripod {
  transform-box: fill-box;
  transform-origin: 50% 100%;
  animation: ct-tripod-timeline 60s linear 0s 1 both;
  animation-play-state: var(--play-state, paused);
  --ct-led-start: 16.5s;
}

/* Already-grown (slide 7): skip grow; fall at --ct-fall-delay (default 46s) */
.ct-tripod.ct-immediate {
  animation: ct-tripod-fall 1.8s ease-in var(--ct-fall-delay, 46s) both;
  animation-play-state: var(--play-state, paused);
  --ct-led-start: 0s;
}

.ct-status-led {
  animation: ct-led-blink 2.5s ease-in-out var(--ct-led-start, 16.5s) infinite both;
  animation-play-state: var(--play-state, paused);
}

.ct-ir-led {
  animation: ct-ir-pulse 3s ease-in-out var(--ct-led-start, 16.5s) infinite both;
  animation-play-state: var(--play-state, paused);
}

.ct-flash {
  animation: ct-flash-fire 0.8s ease-out var(--ct-flash-delay, 44s) both;
  animation-play-state: var(--play-state, paused);
}

.ct-ir-flash {
  animation: ct-ir-glow-fire 1.4s ease-out var(--ct-flash-delay, 44s) both;
  animation-play-state: var(--play-state, paused);
}

/* Grow at 15s (25%) and hold — tripod stays standing for the full slide 6 duration */
@keyframes ct-tripod-timeline {
  0%    { transform: scale(0); opacity: 1; }
  25%   { transform: scale(0); opacity: 1; animation-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1); }
  27.5% { transform: scale(1); opacity: 1; }
  100%  { transform: scale(1); opacity: 1; }
}

/* Fall animation for tripodGrown mode: starts at full scale, topples left */
@keyframes ct-tripod-fall {
  from { transform: scale(1) rotate(0deg); opacity: 1; }
  60%  { transform: scale(1) rotate(-78deg); opacity: 0.8; animation-timing-function: ease-out; }
  to   { transform: scale(1) rotate(-85deg); opacity: 0; }
}

@keyframes ct-led-blink {
  0%, 85%, 100% { opacity: 0.7; }
  90%           { opacity: 0.05; }
}

@keyframes ct-ir-pulse {
  0%, 100% { opacity: 0.25; }
  50%      { opacity: 0.55; }
}

@keyframes ct-flash-fire {
  0%   { opacity: 0; }
  6%   { opacity: 1; }
  25%  { opacity: 0; }
  45%  { opacity: 0.55; }
  70%  { opacity: 0; }
  100% { opacity: 0; }
}

@keyframes ct-ir-glow-fire {
  0%   { opacity: 0; }
  8%   { opacity: 1; }
  100% { opacity: 0; }
}
</style>
