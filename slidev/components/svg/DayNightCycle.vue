<template>
  <g class="day-night-cycle">
    <rect class="daysky" x="-320" y="-260" width="2240" height="900"/>
    <ellipse class="glow dawn" cx="60" cy="560" rx="900" ry="360" fill="url(#side-glow)"/>
    <ellipse class="glow dusk" cx="1540" cy="560" rx="900" ry="360" fill="url(#side-glow)"/>
    <g class="sun"><circle cx="800" cy="70" r="95" fill="url(#side-sun)"/><circle cx="800" cy="70" r="46" fill="#FFD626"/></g>
    <rect class="night" x="-320" y="-260" width="2240" height="1420" fill="#05070d"/>
    <g class="eyes"><g class="blink" style="animation-duration:5.3s; animation-delay:-3.2s"><circle cx="1095.7" cy="636.4" r="6.0" fill="#b8ff6a" opacity="0.22"/><circle cx="1095.7" cy="636.4" r="2.4" fill="#b8ff6a"/></g></g>
    <g class="eyes"><g class="blink" style="animation-duration:5.2s; animation-delay:-3.1s"><circle cx="1097.6" cy="778.4" r="8.0" fill="#ffd84a" opacity="0.22"/><circle cx="1097.6" cy="778.4" r="3.2" fill="#ffd84a"/><circle cx="1118.4" cy="778.4" r="8.0" fill="#ffd84a" opacity="0.22"/><circle cx="1118.4" cy="778.4" r="3.2" fill="#ffd84a"/></g></g>
    <g class="eyes"><g class="blink" style="animation-duration:6.2s; animation-delay:-4.9s"><circle cx="503.0" cy="732.0" r="7.0" fill="#ff9a6a" opacity="0.22"/><circle cx="503.0" cy="732.0" r="2.8" fill="#ff9a6a"/><circle cx="515.0" cy="732.0" r="7.0" fill="#ff9a6a" opacity="0.22"/><circle cx="515.0" cy="732.0" r="2.8" fill="#ff9a6a"/></g></g>
    <g class="eyes late"><g class="blink" style="animation-duration:6.4s; animation-delay:-2.0s"><circle cx="1329.0" cy="493.1" r="8.0" fill="#FFD626" opacity="0.22"/><circle cx="1329.0" cy="493.1" r="3.2" fill="#FFD626"/><circle cx="1341.0" cy="493.1" r="8.0" fill="#FFD626" opacity="0.22"/><circle cx="1341.0" cy="493.1" r="3.2" fill="#FFD626"/></g></g>
    <rect class="flash" x="-320" y="-260" width="2240" height="1420" fill="#ffffff"/>
  </g>
</template>

<style scoped>
/* transform-box and pivot for the sun's arc */
.sun {
  transform-box: view-box;
  transform-origin: 800px 1150px;
}

/* All day/night elements share the 60s cycle */
:is(.sun, .daysky, .glow, .night, .eyes, .night-pose) {
  animation-duration: 60s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-fill-mode: both;
  animation-play-state: var(--play-state, paused);
}

.sun { animation-name: sun-arc; }

@keyframes sun-arc {
  0%, 8%    { transform: rotate(-58deg); opacity: 0; }
  8.5%      { opacity: 1; }
  86%       { transform: rotate(58deg); opacity: 1; }
  87%, 100% { transform: rotate(58deg); opacity: 0; }
}

.daysky { fill: #0b0e14; }
.daysky { animation-name: day-sky; }

@keyframes day-sky {
  0%, 8%    { fill: #0b0e14; }
  14%       { fill: #2a2a45; }
  20%       { fill: #3f4862; }
  30%, 70%  { fill: #36597d; }
  80%       { fill: #4a3a55; }
  90%       { fill: #24233a; }
  96%, 100% { fill: #0b0e14; }
}

.glow { opacity: 0; }
.glow.dawn { animation-name: glow-dawn; }
.glow.dusk { animation-name: glow-dusk; }

@keyframes glow-dawn {
  0%, 8%    { opacity: 0; }
  16%       { opacity: 1; }
  25%       { opacity: 0.5; }
  33%, 100% { opacity: 0; }
}

@keyframes glow-dusk {
  0%, 68%   { opacity: 0; }
  78%       { opacity: 0.6; }
  85%       { opacity: 1; }
  94%, 100% { opacity: 0; }
}

.night { opacity: 0.88; }
.night { animation-name: night-veil; }

@keyframes night-veil {
  0%, 8%    { opacity: 0.88; }
  14%       { opacity: 0.55; }
  21%       { opacity: 0.18; }
  30%, 70%  { opacity: 0; }
  80%       { opacity: 0.2; }
  90%       { opacity: 0.55; }
  96%, 100% { opacity: 0.88; }
}

:is(.eyes, .night-pose).late { opacity: 0; }
.eyes { animation-name: eyes-at-night; }
.eyes.late { animation-name: eyes-in-evening; }

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

/* flash rect is handled by the storm/lightning cycle (Task 5 WeatherEvent) */
.flash { opacity: 0; }
</style>
