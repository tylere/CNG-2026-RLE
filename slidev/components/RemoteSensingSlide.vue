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

    <!-- Satellite: high altitude, slight arc, left to right, 8s at t=36s -->
    <g class="satellite-vehicle">
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

    <!-- Aircraft: Cessna high-wing prop plane, right to left (nose faces left), 16s at t=18s -->
    <g class="aircraft-vehicle">
      <g transform="translate(0 360)">
        <!-- Fuselage: boxy cabin tapering to pointed nose (left) and narrow tail (right) -->
        <path d="M-68,0 C-55,-6 -15,-9 30,-7 L58,-3 L58,3 L30,7 C-15,9 -55,6 -68,0 Z" fill="#c8d4e8"/>
        <!-- Cabin windows -->
        <rect x="-22" y="-7" width="18" height="11" rx="2" fill="#dae8f4" opacity="0.85"/>
        <rect x="0" y="-7" width="15" height="11" rx="2" fill="#dae8f4" opacity="0.85"/>
        <!-- High straight wing (on top, runs left-right perpendicular to fuselage) -->
        <!-- Near wing half (toward viewer = below fuselage in top-down perspective) -->
        <polygon points="-18,7 38,7 50,32 28,32" fill="#b0c2dc"/>
        <!-- Far wing half (away from viewer = above fuselage) -->
        <polygon points="-18,-7 38,-7 50,-32 28,-32" fill="#b8cce0"/>
        <!-- Wing struts (characteristic Cessna: attach low fuselage to high wing) -->
        <line x1="5" y1="7" x2="12" y2="32" stroke="#8898b0" stroke-width="2" stroke-linecap="round"/>
        <line x1="5" y1="-7" x2="12" y2="-32" stroke="#8898b0" stroke-width="2" stroke-linecap="round"/>
        <!-- Horizontal stabilizer (small tail planes) -->
        <polygon points="45,3 34,3 38,18 50,14" fill="#a8b8cc"/>
        <polygon points="45,-3 34,-3 38,-18 50,-14" fill="#a8b8cc"/>
        <!-- Vertical tail fin (visible from top as raised edge) -->
        <polygon points="50,0 42,-3 48,-22 56,-8" fill="#9098ac"/>
        <!-- Engine cowl (round, at nose) -->
        <ellipse cx="-70" cy="0" rx="9" ry="7" fill="#808898"/>
        <!-- Spinning propeller disc -->
        <ellipse cx="-82" cy="0" rx="3" ry="26" fill="rgba(200,210,225,0.38)" stroke="#5a606e" stroke-width="1.5"/>
        <!-- Sensor pod under fuselage belly -->
        <ellipse cx="-10" cy="0" rx="12" ry="5" fill="#20283e" opacity="0.8"/>
      </g>
    </g>

    <!-- Drone: above tree canopy, left to right, 14s at t=2s -->
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
/* Drone: left → right above tree canopy (y=460), 14s at t=20s (5s after tripod falls at t=15s) */
.drone-vehicle {
  animation: drone-fly 14s linear 20s both;
  animation-play-state: var(--play-state, paused);
}

/* Cessna: right → left at mid altitude (y=360), 16s at t=36s (after drone exits at t=34s) */
.aircraft-vehicle {
  animation: aircraft-fly 16s linear 36s both;
  animation-play-state: var(--play-state, paused);
}

/* Satellite: left → right with gentle arc at high altitude (y=110), 8s at t=54s */
.satellite-vehicle {
  animation: satellite-fly 8s ease-in-out 54s both;
  animation-play-state: var(--play-state, paused);
}

@keyframes drone-fly {
  from { transform: translateX(-120px); }
  to   { transform: translateX(1720px); }
}

@keyframes aircraft-fly {
  from { transform: translateX(1800px); }
  to   { transform: translateX(-200px); }
}

/* Arc: enter and exit at same height; 25px higher at midpoint to suggest orbital curvature */
@keyframes satellite-fly {
  0%   { transform: translateX(-160px) translateY(0px); }
  50%  { transform: translateX(800px)  translateY(-28px); }
  100% { transform: translateX(1760px) translateY(0px); }
}
</style>
