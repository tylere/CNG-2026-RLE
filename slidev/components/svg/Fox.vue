<template>
  <g class="fox-container">
    <!-- Fox peeks from behind tree -->
    <g transform="translate(1108.0 781.0) scale(1.3)">
      <g class="peek" style="--d:10s; --p:17s; --dx:50px; --dy:8px">
        <polygon points="-24,-28 -12,-8 12,-8 24,-28 22,2 0,22 -22,2" fill="#d9662b"/>
        <polygon points="-20,-22 -13,-10 -8,-10" fill="#2a1c14"/>
        <polygon points="20,-22 13,-10 8,-10" fill="#2a1c14"/>
        <polygon points="-22,2 -8,6 0,22" fill="#f3ece2"/>
        <polygon points="22,2 8,6 0,22" fill="#f3ece2"/>
        <circle cx="-8" cy="-2" r="2.6" fill="#2a1c14"/>
        <circle cx="8" cy="-2" r="2.6" fill="#2a1c14"/>
        <circle cx="0" cy="19" r="3" fill="#2a1c14"/>
      </g>
    </g>
    <!-- Fox visible at night -->
    <g transform="translate(1108.0 781.0) scale(1.3)">
      <g class="night-pose">
        <polygon points="-24,-28 -12,-8 12,-8 24,-28 22,2 0,22 -22,2" fill="#d9662b"/>
        <polygon points="-20,-22 -13,-10 -8,-10" fill="#2a1c14"/>
        <polygon points="20,-22 13,-10 8,-10" fill="#2a1c14"/>
        <polygon points="-22,2 -8,6 0,22" fill="#f3ece2"/>
        <polygon points="22,2 8,6 0,22" fill="#f3ece2"/>
        <circle cx="-8" cy="-2" r="2.6" fill="#2a1c14"/>
        <circle cx="8" cy="-2" r="2.6" fill="#2a1c14"/>
        <circle cx="0" cy="19" r="3" fill="#2a1c14"/>
      </g>
    </g>
  </g>
</template>

<style scoped>
.peek {
  opacity: 0;
  animation: peek-hide var(--p, 17s) ease-in-out var(--d, 10s) infinite both;
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
</style>
