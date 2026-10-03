<template>
  <g transform="translate(-260.0 870.0)">
    <g class="skunk" style="--sx:2120.0px; --sy:0.0px">
      <g transform="scale(1.4)">
        <ellipse cx="0" cy="2" rx="26" ry="5" fill="rgba(0,0,0,0.3)"/>
        <rect class="leg leg-a" x="-14" y="-10" width="5" height="11" fill="#15171a"/>
        <rect class="leg leg-b" x="-6" y="-10" width="5" height="11" fill="#15171a"/>
        <rect class="leg leg-b" x="10" y="-10" width="5" height="11" fill="#15171a"/>
        <rect class="leg leg-a" x="17" y="-10" width="5" height="11" fill="#15171a"/>
        <path class="tail" d="M-18 -16 Q-40 -22 -38 -46 Q-36 -62 -20 -58 Q-28 -46 -16 -30 Z" fill="#15171a"/>
        <path class="tail" d="M-24 -26 Q-34 -40 -27 -54" stroke="#f2f2f2" stroke-width="4" fill="none" stroke-linecap="round"/>
        <ellipse cx="2" cy="-17" rx="22" ry="11" fill="#15171a"/>
        <ellipse cx="23" cy="-15" rx="9" ry="7" fill="#15171a"/>
        <path d="M-16 -24 Q2 -32 22 -21" stroke="#f2f2f2" stroke-width="4" fill="none" stroke-linecap="round"/>
        <circle cx="26" cy="-16" r="1.6" fill="#f2f2f2"/>
        <circle cx="31" cy="-13" r="1.8" fill="#3a3a3a"/>
      </g>
    </g>
  </g>
</template>

<style scoped>
.skunk {
  opacity: 0;
  animation: skunk-walk 75s linear 8s infinite both;
  animation-play-state: var(--play-state, paused);
}

.leg-a {
  transform-box: fill-box;
  transform-origin: 50% 0%;
  animation: leg 0.6s ease-in-out infinite alternate;
  animation-play-state: var(--play-state, paused);
}

.leg-b {
  transform-box: fill-box;
  transform-origin: 50% 0%;
  animation: leg 0.6s ease-in-out -0.6s infinite alternate;
  animation-play-state: var(--play-state, paused);
}

@keyframes skunk-walk {
  0%        { opacity: 0; transform: translate(0, 0); }
  1%        { opacity: 1; }
  79%       { opacity: 1; transform: translate(var(--sx), var(--sy)); }
  80%, 100% { opacity: 0; transform: translate(var(--sx), var(--sy)); }
}

@keyframes leg {
  from { transform: rotate(-18deg); }
  to   { transform: rotate(18deg); }
}
</style>
