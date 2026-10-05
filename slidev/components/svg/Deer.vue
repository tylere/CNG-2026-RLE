<script setup lang="ts">
const props = defineProps<{
  cameraTrap?: boolean
  atCamera?: boolean
}>()
</script>

<template>
  <g class="deer-container" :class="{ 'ct-approach': props.cameraTrap, 'at-camera': props.atCamera }">
    <g transform="translate(1132.0 720.0) scale(1.1)">
      <ellipse cx="6" cy="2" rx="34" ry="6" fill="rgba(0,0,0,0.28)"/>
      <rect x="-20" y="-28" width="5" height="28" fill="#6f4e32"/>
      <rect x="-11" y="-28" width="5" height="28" fill="#976c46"/>
      <rect x="14" y="-28" width="5" height="28" fill="#6f4e32"/>
      <rect x="22" y="-28" width="5" height="28" fill="#976c46"/>
      <ellipse cx="4" cy="-36" rx="28" ry="13" fill="#976c46"/>
      <ellipse cx="31" cy="-40" rx="4" ry="6" fill="#f0e8dc"/>
      <g class="drink">
        <polygon points="-18,-44 -30,-70 -21,-74 -8,-38" fill="#976c46"/>
        <ellipse cx="-31" cy="-74" rx="12" ry="7" transform="rotate(-20 -31 -74)" fill="#976c46"/>
        <polygon points="-24,-80 -18,-90 -16,-78" fill="#6f4e32"/>
        <path d="M-27 -80 Q-30 -96 -40 -100 M-29 -91 L-22 -98 M-23 -80 Q-16 -95 -8 -98" stroke="#6f4e32" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <circle cx="-33" cy="-76" r="1.8" fill="#1a1a1a"/>
        <circle cx="-42" cy="-71" r="2" fill="#1a1a1a"/>
      </g>
    </g>
  </g>
</template>

<style scoped>
.drink {
  transform-box: view-box;
  transform-origin: -14px -40px;
  animation: drink 9s ease-in-out 9s infinite both;
  animation-play-state: var(--play-state, paused);
}

/* Walk toward camera (right of it at x=950, foreground at y=800).
   --deer-ct-delay defaults to 32s; override via :style for earlier approach. */
.deer-container.ct-approach {
  animation: deer-approach 12s ease-in-out var(--deer-ct-delay, 32s) both;
  animation-play-state: var(--play-state, paused);
}

/* Start already at camera position (for slides continuing from camera-trap) */
.deer-container.at-camera {
  transform: translateX(-182px) translateY(80px);
}

@keyframes drink {
  0%, 8%    { transform: rotate(0deg); }
  20%       { transform: rotate(-62deg); }
  26%       { transform: rotate(-56deg); }
  32%       { transform: rotate(-62deg); }
  38%       { transform: rotate(-56deg); }
  44%       { transform: rotate(-62deg); }
  58%, 100% { transform: rotate(0deg); }
}

@keyframes deer-approach {
  from { transform: translateX(0) translateY(0); }
  to   { transform: translateX(-182px) translateY(80px); }
}
</style>
