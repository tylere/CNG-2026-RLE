<template>
  <g class="day-night-cycle">
    <rect class="daysky" x="-320" y="-260" width="2240" height="900"/>
    <!-- Stars: visible at night, fade when the sun comes up -->
    <g class="stars">
      <circle cx="152" cy="78"  r="1.5" fill="white"/>
      <circle cx="291" cy="48"  r="2.0" fill="white"/>
      <circle cx="441" cy="112" r="1.5" fill="white"/>
      <circle cx="523" cy="68"  r="1.0" fill="white"/>
      <circle cx="634" cy="38"  r="2.0" fill="white"/>
      <circle cx="762" cy="92"  r="1.5" fill="white"/>
      <circle cx="871" cy="58"  r="2.0" fill="white"/>
      <circle cx="982" cy="102" r="1.0" fill="white"/>
      <circle cx="1104" cy="48"  r="2.0" fill="white"/>
      <circle cx="1223" cy="82"  r="1.5" fill="white"/>
      <circle cx="1342" cy="52"  r="1.0" fill="white"/>
      <circle cx="1431" cy="98"  r="2.0" fill="white"/>
      <circle cx="203"  cy="152" r="1.0" fill="white"/>
      <circle cx="381"  cy="178" r="1.5" fill="white"/>
      <circle cx="602"  cy="198" r="2.0" fill="white"/>
      <circle cx="781"  cy="162" r="1.0" fill="white"/>
      <circle cx="953"  cy="188" r="1.5" fill="white"/>
      <circle cx="1153" cy="172" r="2.0" fill="white"/>
      <circle cx="1352" cy="158" r="1.0" fill="white"/>
      <circle cx="108"  cy="258" r="1.0" fill="white"/>
      <circle cx="452"  cy="282" r="1.5" fill="white"/>
      <circle cx="803"  cy="248" r="1.0" fill="white"/>
      <circle cx="1202" cy="272" r="1.5" fill="white"/>
      <circle cx="1498" cy="252" r="1.0" fill="white"/>
    </g>
    <ellipse class="glow dawn" cx="60" cy="560" rx="900" ry="360" fill="url(#side-glow)"/>
    <ellipse class="glow dusk" cx="1540" cy="560" rx="900" ry="360" fill="url(#side-glow)"/>
    <g class="sun"><circle cx="800" cy="70" r="95" fill="url(#side-sun)"/><circle cx="800" cy="70" r="46" fill="#FFD626"/></g>
  </g>
</template>

<style scoped>
/* transform-box and pivot for the sun's arc */
.sun {
  transform-box: view-box;
  transform-origin: 800px 1150px;
}

/* All day/night background elements share the 60s cycle */
:is(.sun, .daysky, .glow, .stars) {
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

/* Night veil, eyes, and flash moved to DayNightOverlay.vue (renders after Forest) */

.stars { animation-name: star-fade; }

@keyframes star-fade {
  0%, 7%    { opacity: 1; }
  16%, 88%  { opacity: 0; }
  96%, 100% { opacity: 1; }
}
</style>
