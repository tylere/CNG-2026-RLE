<template>
  <g class="rabbit-container">
    <!-- Rabbit peeks from below ground level -->
    <g transform="translate(509.0 743.0) scale(1.0)">
      <g class="peek" style="--d:12s; --p:19s; --dx:0px; --dy:81px">
        <ellipse cx="-8" cy="-20" rx="6" ry="22" fill="#b9b4ac"/>
        <ellipse cx="8" cy="-20" rx="6" ry="22" fill="#b9b4ac"/>
        <ellipse cx="-8" cy="-20" rx="2.5" ry="15" fill="#e3a2a2"/>
        <ellipse cx="8" cy="-20" rx="2.5" ry="15" fill="#e3a2a2"/>
        <circle cx="0" cy="12" r="15" fill="#b9b4ac"/>
        <circle cx="-6" cy="9" r="2.3" fill="#2a2a2a"/>
        <circle cx="6" cy="9" r="2.3" fill="#2a2a2a"/>
        <circle cx="0" cy="16" r="2" fill="#d98c8c"/>
      </g>
    </g>
    <!-- Rabbit visible at night (ears fully visible above ground) -->
    <g transform="translate(509.0 743.0) scale(1.0)">
      <g class="night-pose">
        <ellipse cx="-8" cy="-40" rx="6" ry="22" fill="#b9b4ac"/>
        <ellipse cx="8" cy="-40" rx="6" ry="22" fill="#b9b4ac"/>
        <ellipse cx="-8" cy="-40" rx="2.5" ry="15" fill="#e3a2a2"/>
        <ellipse cx="8" cy="-40" rx="2.5" ry="15" fill="#e3a2a2"/>
        <circle cx="0" cy="-8" r="15" fill="#b9b4ac"/>
        <circle cx="-6" cy="-11" r="2.3" fill="#2a2a2a"/>
        <circle cx="6" cy="-11" r="2.3" fill="#2a2a2a"/>
        <circle cx="0" cy="-4" r="2" fill="#d98c8c"/>
      </g>
    </g>
  </g>
</template>

<style scoped>
.peek {
  opacity: 0;
  animation: peek-hide var(--p, 19s) ease-in-out var(--d, 12s) infinite both;
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
