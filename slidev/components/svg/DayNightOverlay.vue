<template>
  <g class="day-night-overlay">
    <!-- Night veil — darkens terrain, trees, and animals at night.
         Must render AFTER Forest so it sits above the ground layer. -->
    <rect class="night" x="-320" y="-260" width="2240" height="1420" fill="#05070d"/>
    <!-- Glowing animal eyes visible through the darkness -->
    <g class="eyes"><g class="blink" style="animation-duration:5.3s; animation-delay:-3.2s"><circle cx="1095.7" cy="636.4" r="6.0" fill="#b8ff6a" opacity="0.22"/><circle cx="1095.7" cy="636.4" r="2.4" fill="#b8ff6a"/></g></g>
    <g class="eyes"><g class="blink" style="animation-duration:5.2s; animation-delay:-3.1s"><circle cx="1097.6" cy="778.4" r="8.0" fill="#ffd84a" opacity="0.22"/><circle cx="1097.6" cy="778.4" r="3.2" fill="#ffd84a"/><circle cx="1118.4" cy="778.4" r="8.0" fill="#ffd84a" opacity="0.22"/><circle cx="1118.4" cy="778.4" r="3.2" fill="#ffd84a"/></g></g>
    <g class="eyes"><g class="blink" style="animation-duration:6.2s; animation-delay:-4.9s"><circle cx="503.0" cy="732.0" r="7.0" fill="#ff9a6a" opacity="0.22"/><circle cx="503.0" cy="732.0" r="2.8" fill="#ff9a6a"/><circle cx="515.0" cy="732.0" r="7.0" fill="#ff9a6a" opacity="0.22"/><circle cx="515.0" cy="732.0" r="2.8" fill="#ff9a6a"/></g></g>
    <g class="eyes late"><g class="blink" style="animation-duration:6.4s; animation-delay:-2.0s"><circle cx="1329.0" cy="493.1" r="8.0" fill="#FFD626" opacity="0.22"/><circle cx="1329.0" cy="493.1" r="3.2" fill="#FFD626"/><circle cx="1341.0" cy="493.1" r="8.0" fill="#FFD626" opacity="0.22"/><circle cx="1341.0" cy="493.1" r="3.2" fill="#FFD626"/></g></g>
    <!-- Lightning flash (controlled by WeatherEvent via CSS variable) -->
    <rect class="flash" x="-320" y="-260" width="2240" height="1420" fill="#ffffff"/>
  </g>
</template>

<style scoped>
/* Run continuously (not gated by --play-state) so all ecosystem slides share the same clock */
:is(.night, .eyes) {
  animation-duration: 60s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-fill-mode: both;
  animation-play-state: running;
  animation-delay: -18s;
}

.night { opacity: 0.88; animation-name: night-veil; }

@keyframes night-veil {
  0%, 8%    { opacity: 0.88; }
  14%       { opacity: 0.55; }
  21%       { opacity: 0.18; }
  30%, 70%  { opacity: 0; }
  80%       { opacity: 0.2; }
  90%       { opacity: 0.55; }
  96%, 100% { opacity: 0.88; }
}

.eyes { animation-name: eyes-at-night; }
.eyes.late { opacity: 0; animation-name: eyes-in-evening; }

@keyframes eyes-at-night {
  0%, 7%    { opacity: 1; }
  12%, 90%  { opacity: 0; }
  96%, 100% { opacity: 1; }
}

@keyframes eyes-in-evening {
  0%, 90%   { opacity: 0; }
  96%, 100% { opacity: 1; }
}

.blink {
  transform-box: fill-box;
  transform-origin: 50% 50%;
  animation-name: blink;
  animation-iteration-count: infinite;
  animation-play-state: var(--play-state, paused);
}

@keyframes blink {
  0%, 90%   { transform: scaleY(1); }
  94%       { transform: scaleY(0.1); }
  98%, 100% { transform: scaleY(1); }
}

.flash { opacity: 0; }
</style>
