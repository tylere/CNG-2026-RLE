<script setup lang="ts">
import { computed } from 'vue'
import Deer from './svg/Deer.vue'
import AcousticSensor from './svg/AcousticSensor.vue'
import { useDeerPosition } from '../composables/useDeerPosition'

// Resume the deer where slide 6 left it, finishing the walk at the same pace (12s for the full walk).
const { progress } = useDeerPosition()
const p = computed(() => progress.value ?? 0)
const walkS = computed(() => Math.max(0.01, (1 - p.value) * 12))
const deerStyle = computed(() => ({
  '--deer-ct-delay': '2s',
  '--deer-ct-duration': `${walkS.value}s`,
  '--deer-start-x': `${-182 * p.value}px`,
  '--deer-start-y': `${80 * Math.min(p.value, 1)}px`,
}))
</script>

<template>
  <!-- Scene: tripod gone (knocked into the lake on slide 6), ecologists gone.
       Drone, aircraft, and satellite survey the area in sequence. -->
  <EcosystemScene trees-grown no-deer>
    <!-- Deer continues from where slide 6 left it (2s delay), under the night veil -->
    <template #under-night>
      <!-- Acoustic sensor attached on slide 6 -->
      <AcousticSensor placed />
      <Deer camera-trap :style="deerStyle" />
    </template>

    <!-- Survey vehicles fly across in sequence.
         Satellite first (farthest/highest = paints behind others), then aircraft, then drone. -->

    <!-- Satellite: high altitude, constant speed with a slight arc, left to right, 10s from t=13s -->
    <g class="satellite-vehicle">
      <g class="satellite-arc">
      <g transform="translate(0 110)">
        <!-- Body -->
        <rect x="-20" y="-20" width="40" height="40" rx="5" fill="#c0c8d8" stroke="#8898b0" stroke-width="2.5"/>
        <!-- Body panel detail -->
        <rect x="-15" y="-15" width="12" height="30" rx="2" fill="#b0b8cc"/>
        <rect x="3" y="-15" width="12" height="30" rx="2" fill="#b0b8cc"/>
        <!-- Solar panel left: 3 cells -->
        <rect x="-93" y="-11" width="66" height="22" rx="3" fill="#1a2c50" stroke="#2a4a88" stroke-width="1.5"/>
        <line x1="-71" y1="-11" x2="-71" y2="11" stroke="#2a4a88" stroke-width="1.5"/>
        <line x1="-49" y1="-11" x2="-49" y2="11" stroke="#2a4a88" stroke-width="1.5"/>
        <!-- Connection boom left -->
        <rect x="-27" y="-4" width="7" height="8" rx="1" fill="#505868"/>
        <!-- Solar panel right: 3 cells -->
        <rect x="27" y="-11" width="66" height="22" rx="3" fill="#1a2c50" stroke="#2a4a88" stroke-width="1.5"/>
        <line x1="49" y1="-11" x2="49" y2="11" stroke="#2a4a88" stroke-width="1.5"/>
        <line x1="71" y1="-11" x2="71" y2="11" stroke="#2a4a88" stroke-width="1.5"/>
        <!-- Connection boom right -->
        <rect x="20" y="-4" width="7" height="8" rx="1" fill="#505868"/>
        <!-- Sensor/antenna pointing down -->
        <line x1="0" y1="20" x2="0" y2="32" stroke="#9ab0c8" stroke-width="2.5"/>
        <ellipse cx="0" cy="32" rx="9" ry="5" fill="none" stroke="#9ab0c8" stroke-width="2"/>
      </g>
      </g>
    </g>

    <!-- Aircraft: Cessna high-wing prop plane, right to left (nose faces left), 16s at t=3s -->
    <g class="aircraft-vehicle">
      <!-- Side view, facing left (direction of flight) -->
      <g transform="translate(0 360) scale(1.25)">
        <!-- Tail: fin and horizontal stabilizer -->
        <polygon points="40,-9 54,-34 66,-34 66,-6" fill="#c9d3e3"/>
        <rect x="46" y="-6" width="24" height="4" rx="2" fill="#b3c0d4"/>
        <!-- Fuselage -->
        <path d="M-68,-2 C-66,-11 -56,-16 -44,-17 L20,-17 L64,-8 L68,-3 L64,1 L28,4 C-10,8 -48,9 -64,5 Z" fill="#eef2f8"/>
        <path d="M-62,-1 L64,-4" stroke="#3a6ea5" stroke-width="2.5"/>
        <!-- Cabin windows -->
        <polygon points="-44,-13 -24,-14 -24,-5 -50,-5" fill="#5b7fa6"/>
        <rect x="-20" y="-14" width="18" height="9" rx="1.5" fill="#5b7fa6"/>
        <!-- High wing (edge-on) and strut -->
        <rect x="-48" y="-22" width="72" height="6" rx="3" fill="#c9d3e3"/>
        <line x1="16" y1="-16" x2="4" y2="5" stroke="#9aa6b8" stroke-width="1.6"/>
        <!-- Landing gear -->
        <line x1="-16" y1="6" x2="-20" y2="16" stroke="#6b7480" stroke-width="2.5"/>
        <circle cx="-21" cy="18" r="4.5" fill="#2a2d33"/>
        <line x1="-58" y1="5" x2="-58" y2="15" stroke="#6b7480" stroke-width="2"/>
        <circle cx="-58" cy="17" r="3.5" fill="#2a2d33"/>
        <!-- Spinner and spinning propeller -->
        <ellipse cx="-70" cy="-2" rx="6" ry="5" fill="#8a929e"/>
        <ellipse class="prop" cx="-75" cy="-2" rx="2" ry="18" fill="rgba(220,228,240,0.45)"/>
      </g>
    </g>

    <!-- Drone: above tree canopy, left to right with two hovering stops, 16s from t=8s -->
    <g class="drone-vehicle">
      <g transform="translate(0 460)">
        <!-- Central body -->
        <rect x="-11" y="-11" width="22" height="22" rx="5" fill="#2a2a3a"/>
        <!-- 4 diagonal arms -->
        <line x1="-11" y1="-11" x2="-36" y2="-36" stroke="#3a3a50" stroke-width="4" stroke-linecap="round"/>
        <line x1="11" y1="-11" x2="36" y2="-36" stroke="#3a3a50" stroke-width="4" stroke-linecap="round"/>
        <line x1="-11" y1="11" x2="-36" y2="36" stroke="#3a3a50" stroke-width="4" stroke-linecap="round"/>
        <line x1="11" y1="11" x2="36" y2="36" stroke="#3a3a50" stroke-width="4" stroke-linecap="round"/>
        <!-- Motor mounts -->
        <circle cx="-36" cy="-36" r="6" fill="#4a4a60"/>
        <circle cx="36" cy="-36" r="6" fill="#4a4a60"/>
        <circle cx="-36" cy="36" r="6" fill="#4a4a60"/>
        <circle cx="36" cy="36" r="6" fill="#4a4a60"/>
        <!-- Rotor discs -->
        <ellipse cx="-36" cy="-36" rx="22" ry="6" fill="rgba(180,190,210,0.3)" stroke="#5a5a70" stroke-width="1.5"/>
        <ellipse cx="36" cy="-36" rx="22" ry="6" fill="rgba(180,190,210,0.3)" stroke="#5a5a70" stroke-width="1.5"/>
        <ellipse cx="-36" cy="36" rx="22" ry="6" fill="rgba(180,190,210,0.3)" stroke="#5a5a70" stroke-width="1.5"/>
        <ellipse cx="36" cy="36" rx="22" ry="6" fill="rgba(180,190,210,0.3)" stroke="#5a5a70" stroke-width="1.5"/>
        <!-- Camera pod below body -->
        <circle cx="0" cy="16" r="9" fill="#1a1a2e" stroke="#3a3a50" stroke-width="2"/>
        <circle cx="0" cy="16" r="5" fill="#0a0a1e"/>
        <!-- Status light -->
        <circle cx="0" cy="-5" r="3" fill="#22cc44"/>
      </g>
    </g>
  </EcosystemScene>
</template>

<style scoped>
/* Drone: left → right above tree canopy (y=460), 16s from t=8s with two hovering stops */
.drone-vehicle {
  animation: drone-fly 16s linear 8s both;
  animation-play-state: var(--play-state, paused);
}

/* Cessna: right → left at mid altitude (y=360), 16s starting at t=3s */
.aircraft-vehicle {
  animation: aircraft-fly 16s linear 3s both;
  animation-play-state: var(--play-state, paused);
}

/* Satellite: left → right at constant speed, high altitude (y=110), 10s from t=13s */
.satellite-vehicle {
  animation: satellite-fly 10s linear 13s both;
  animation-play-state: var(--play-state, paused);
}

/* Fly, hover, fly, hover, fly: easing into and out of each stop */
@keyframes drone-fly {
  0%        { transform: translateX(-120px); animation-timing-function: ease-out; }
  28%, 42%  { transform: translateX(520px);  animation-timing-function: ease-in-out; }
  68%, 80%  { transform: translateX(1080px); animation-timing-function: ease-in; }
  100%      { transform: translateX(1720px); }
}
/* Gentle bob while hovering/flying */
.drone-vehicle > g {
  animation: drone-bob 1.6s ease-in-out infinite alternate;
  animation-play-state: var(--play-state, paused);
}
@keyframes drone-bob {
  from { transform: translate(0, 460px); }
  to   { transform: translate(0, 466px); }
}

.prop {
  transform-box: fill-box;
  transform-origin: center;
  animation: prop-spin 0.12s linear infinite;
  animation-play-state: var(--play-state, paused);
}
@keyframes prop-spin {
  0%, 100% { transform: scaleY(1); }
  50%      { transform: scaleY(0.25); }
}

@keyframes aircraft-fly {
  from { transform: translateX(1800px); }
  to   { transform: translateX(-200px); }
}

/* Constant speed across; the inner arc group rises and falls smoothly to suggest orbital curvature */
@keyframes satellite-fly {
  from { transform: translateX(-160px); }
  to   { transform: translateX(1760px); }
}
.satellite-arc {
  animation: satellite-arc 5s ease-in-out 13s 2 alternate both;
  animation-play-state: var(--play-state, paused);
}
@keyframes satellite-arc {
  from { transform: translateY(0); }
  to   { transform: translateY(-28px); }
}
</style>
