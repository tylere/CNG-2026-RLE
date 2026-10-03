<template>
  <g class="camera-trap">
    <!-- Gradient defs for flash glow effects -->
    <defs>
      <radialGradient id="ct-ir-glow-g2" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0" stop-color="#ff5500" stop-opacity="0.75"/>
        <stop offset="1" stop-color="#ff5500" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="ct-flash-glow-g" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0"   stop-color="#ffffff" stop-opacity="0.98"/>
        <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.6"/>
        <stop offset="1"   stop-color="#ffffff" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <!-- Camera trap device on tripod -->
    <g transform="translate(850 750)">
      <g class="ct-tripod" opacity="0">
        <line x1="0" y1="-92" x2="-46" y2="0" stroke="#555" stroke-width="5" stroke-linecap="round"/>
        <line x1="0" y1="-92" x2="6" y2="2" stroke="#555" stroke-width="5" stroke-linecap="round"/>
        <line x1="0" y1="-92" x2="44" y2="-5" stroke="#555" stroke-width="5" stroke-linecap="round"/>
        <!-- Camera body; lens faces right (toward the deer at x=1132) -->
        <rect x="-4" y="-128" width="60" height="40" rx="5" fill="#1c1c1c" stroke="#333" stroke-width="1.5"/>
        <circle class="ct-ir-led" cx="50" cy="-116" r="4" fill="#3a0000" opacity="0.3"/>
        <circle class="ct-ir-led" cx="50" cy="-107" r="4" fill="#3a0000" opacity="0.3"/>
        <circle class="ct-ir-led" cx="42" cy="-116" r="4" fill="#3a0000" opacity="0.3"/>
        <circle class="ct-ir-led" cx="42" cy="-107" r="4" fill="#3a0000" opacity="0.3"/>
        <circle cx="36" cy="-108" r="11" fill="#222" stroke="#555" stroke-width="2"/>
        <circle cx="36" cy="-108" r="7" fill="#111"/>
        <circle cx="36" cy="-108" r="3.5" fill="#080818"/>
        <circle cx="39" cy="-111" r="1.8" fill="rgba(255,255,255,0.22)"/>
        <circle class="ct-status-led" cx="52" cy="-126" r="3" fill="#ff2200" opacity="0.7"/>
      </g>
    </g>
    <!-- IR glow and white flash overlays -->
    <ellipse class="ct-ir-flash" cx="950" cy="690" rx="260" ry="180"
      fill="url(#ct-ir-glow-g2)" opacity="0"/>
    <ellipse class="ct-flash" cx="870" cy="690" rx="500" ry="380"
      fill="url(#ct-flash-glow-g)" opacity="0"/>
  </g>
</template>

<style scoped>
.ct-tripod {
  animation: ct-tripod-appear 1.2s ease-out 16s both;
  animation-play-state: var(--play-state, paused);
}

.ct-status-led {
  animation: ct-led-blink 2.5s ease-in-out 16s infinite both;
  animation-play-state: var(--play-state, paused);
}

.ct-ir-led {
  animation: ct-ir-pulse 3s ease-in-out 16s infinite both;
  animation-play-state: var(--play-state, paused);
}

.ct-flash {
  animation: ct-flash-fire 0.8s ease-out 62s both;
  animation-play-state: var(--play-state, paused);
}

.ct-ir-flash {
  animation: ct-ir-glow-fire 1.4s ease-out 62s both;
  animation-play-state: var(--play-state, paused);
}

@keyframes ct-tripod-appear {
  from { opacity: 0; transform: translateY(-14px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes ct-led-blink {
  0%, 85%, 100% { opacity: 0.7; }
  90%           { opacity: 0.05; }
}

@keyframes ct-ir-pulse {
  0%, 100% { opacity: 0.25; }
  50%      { opacity: 0.55; }
}

@keyframes ct-flash-fire {
  0%   { opacity: 0; }
  6%   { opacity: 1; }
  25%  { opacity: 0; }
  45%  { opacity: 0.55; }
  70%  { opacity: 0; }
  100% { opacity: 0; }
}

@keyframes ct-ir-glow-fire {
  0%   { opacity: 0; }
  8%   { opacity: 1; }
  100% { opacity: 0; }
}
</style>
