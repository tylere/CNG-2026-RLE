<template>
  <g class="owl-container">
    <!-- Peek owl: hides at --dy offset, peeks out on cycle -->
    <g transform="translate(1335.0 497.6) scale(0.75)">
      <g class="peek" style="--d:35s; --p:21s; --dx:0px; --dy:55px">
        <path d="M-20 40 L-20 -10 L-16 -26 L-7 -17 L7 -17 L16 -26 L20 -10 L20 40 Z" fill="#8a7a66"/>
        <circle cx="-8" cy="-6" r="8" fill="#cbbb9f"/>
        <circle cx="8" cy="-6" r="8" fill="#cbbb9f"/>
        <circle cx="-8" cy="-6" r="4.5" fill="#FFD626"/>
        <circle cx="8" cy="-6" r="4.5" fill="#FFD626"/>
        <circle class="eye" cx="-8" cy="-6" r="2" fill="#1a1a1a"/>
        <circle class="eye" cx="8" cy="-6" r="2" fill="#1a1a1a"/>
        <polygon points="-3,2 3,2 0,8" fill="#e3a83a"/>
      </g>
    </g>
    <!-- Night-pose owl: visible at night (late = appears only in evening portion of cycle) -->
    <g transform="translate(1335.0 497.6) scale(0.75)">
      <g class="night-pose late">
        <path d="M-20 40 L-20 -10 L-16 -26 L-7 -17 L7 -17 L16 -26 L20 -10 L20 40 Z" fill="#8a7a66"/>
        <circle cx="-8" cy="-6" r="8" fill="#cbbb9f"/>
        <circle cx="8" cy="-6" r="8" fill="#cbbb9f"/>
        <circle cx="-8" cy="-6" r="4.5" fill="#FFD626"/>
        <circle cx="8" cy="-6" r="4.5" fill="#FFD626"/>
        <circle class="eye" cx="-8" cy="-6" r="2" fill="#1a1a1a"/>
        <circle class="eye" cx="8" cy="-6" r="2" fill="#1a1a1a"/>
        <polygon points="-3,2 3,2 0,8" fill="#e3a83a"/>
      </g>
    </g>
  </g>
</template>

<style scoped>
.peek {
  opacity: 0;
  animation: peek-hide var(--p, 21s) ease-in-out var(--d, 35s) infinite both;
  animation-play-state: var(--play-state, paused);
}

.night-pose {
  animation-duration: 60s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-fill-mode: both;
  animation-name: eyes-at-night;
  animation-play-state: var(--play-state, paused);
}

.night-pose.late {
  opacity: 0;
  animation-name: eyes-in-evening;
}

@keyframes peek-hide {
  0%        { opacity: 0; transform: translate(var(--dx), var(--dy)); }
  2%        { opacity: 1; transform: translate(var(--dx), var(--dy)); }
  8%, 30%   { opacity: 1; transform: translate(0, 0); }
  37%       { opacity: 1; transform: translate(var(--dx), var(--dy)); }
  39%, 100% { opacity: 0; transform: translate(var(--dx), var(--dy)); }
}

@keyframes eyes-at-night {
  0%, 7%    { opacity: 1; }
  12%, 90%  { opacity: 0; }
  96%, 100% { opacity: 1; }
}

@keyframes eyes-in-evening {
  0%, 90%   { opacity: 0; }
  96%, 100% { opacity: 1; }
}
</style>
