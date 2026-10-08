<script setup lang="ts">
import { useId } from 'vue'

const props = defineProps<{
  knocked?: boolean // knocked into the lake (set by the slide on click)
}>()

// Per-instance ids: Slidev keeps neighbouring slides mounted, and a url(#id) that
// resolves to a copy on a hidden slide paints nothing.
const uid = useId()
</script>

<template>
  <g class="camera-trap">
    <defs>
      <radialGradient :id="`${uid}-ct-ir-glow-g2`" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0" stop-color="#ff5500" stop-opacity="0.75"/>
        <stop offset="1" stop-color="#ff5500" stop-opacity="0"/>
      </radialGradient>
      <radialGradient :id="`${uid}-ct-flash-glow-g`" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0"   stop-color="#ffffff" stop-opacity="0.98"/>
        <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.6"/>
        <stop offset="1"   stop-color="#ffffff" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <!-- Camera trap device on tripod; translate(850 750) is scene position -->
    <g transform="translate(850 750)">
      <g class="ct-tripod" :class="{ 'ct-knocked': props.knocked }">
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
    <!-- Splash where the knocked-over tripod enters the lake -->
    <g v-if="props.knocked">
      <ellipse class="ct-splash" cx="760" cy="708" rx="10" ry="3" fill="none" stroke="#a9d6f2" stroke-width="2" vector-effect="non-scaling-stroke"/>
      <ellipse class="ct-splash ct-splash-2" cx="760" cy="708" rx="10" ry="3" fill="none" stroke="#a9d6f2" stroke-width="2" vector-effect="non-scaling-stroke"/>
    </g>
    <!-- IR glow and white flash overlays (scene coordinates) -->
    <ellipse class="ct-ir-flash" cx="950" cy="690" rx="260" ry="180"
      :fill="`url(#${uid}-ct-ir-glow-g2)`" opacity="0"/>
    <ellipse class="ct-flash" cx="870" cy="690" rx="500" ry="380"
      :fill="`url(#${uid}-ct-flash-glow-g)`" opacity="0"/>
  </g>
</template>

<style scoped>
/* --ct-flash-delay is inherited from EcosystemScene (set dynamically by the slide).
   --ct-fall-delay is overridable from the parent via :style */

/* Default: single 60s timeline — grow at 5s */
.ct-tripod {
  transform-box: fill-box;
  transform-origin: 50% 100%;
  animation: ct-tripod-timeline 60s linear 0s 1 both;
  animation-play-state: var(--play-state, paused);
  --ct-led-start: 6.5s;
}

/* Knocked over: replaces the timeline when the class is added, so the fall starts
   --ct-fall-delay after that moment (default 0.9s = when the deer's push makes contact) */
.ct-tripod.ct-knocked {
  animation: ct-tripod-fall 5s linear var(--ct-fall-delay, 0.9s) both;
  animation-play-state: var(--play-state, paused);
}

.ct-status-led {
  animation: ct-led-blink 2.5s ease-in-out var(--ct-led-start, 6.5s) infinite both;
  animation-play-state: var(--play-state, paused);
}

.ct-ir-led {
  animation: ct-ir-pulse 3s ease-in-out var(--ct-led-start, 6.5s) infinite both;
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

/* Grow at 5s (8.33%), when the ecologist arrives, and hold for the rest of slide 6 */
@keyframes ct-tripod-timeline {
  0%     { transform: scale(0); opacity: 1; }
  8.33%  { transform: scale(0); opacity: 1; animation-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1); }
  10.83% { transform: scale(1); opacity: 1; }
  100%  { transform: scale(1); opacity: 1; }
}

/* Knocked over: topples back into the lake, slides in, then sinks */
@keyframes ct-tripod-fall {
  0%   { transform: translate(0, 0) rotate(0deg); opacity: 1; animation-timing-function: ease-in; }
  22%  { transform: translate(0, 0) rotate(-82deg); opacity: 1; animation-timing-function: ease-out; }
  34%  { transform: translate(-30px, -46px) rotate(-82deg); opacity: 1; animation-timing-function: ease-in-out; }
  100% { transform: translate(-30px, -36px) rotate(-82deg); opacity: 0; }
}

/* Ripples start as the tripod hits the water (~1.1s into the fall) */
.ct-splash {
  opacity: 0;
  transform-box: fill-box;
  transform-origin: center;
  animation: ct-splash 2.4s ease-out calc(var(--ct-fall-delay, 0.9s) + 1.1s) both;
  animation-play-state: var(--play-state, paused);
}
.ct-splash-2 { animation-delay: calc(var(--ct-fall-delay, 0.9s) + 1.6s); }

@keyframes ct-splash {
  0%   { opacity: 0.9; transform: scale(1); }
  100% { opacity: 0; transform: scale(9); }
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
