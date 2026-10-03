<template>
  <g class="weather-event">
    <g transform="translate(993.5 300)">
      <g class="storm">
        <path class="rain" style="animation-delay:-0.43s" d="M-60.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.21s" d="M-46.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.36s" d="M-32.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.10s" d="M-18.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.39s" d="M-4.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.47s" d="M10.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.47s" d="M24.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.34s" d="M38.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.34s" d="M52.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <path class="rain" style="animation-delay:-0.00s" d="M66.0 20 l-4 14" stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>
        <g transform="scale(0.85)">
          <ellipse cx="0" cy="0" rx="70" ry="20" fill="#3c424a"/>
          <circle cx="-30" cy="-12" r="26" fill="#555c65"/>
          <circle cx="8" cy="-24" r="32" fill="#555c65"/>
          <circle cx="42" cy="-8" r="22" fill="#555c65"/>
          <ellipse cx="0" cy="-4" rx="66" ry="16" fill="#555c65"/>
        </g>
      </g>
    </g>
    <polyline class="bolt" points="983.5,322.0 1005.5,380.0 985.5,410.0 1003.5,470.0 989.5,500.0 999.5,542.0" fill="none" stroke="#fff6c2" stroke-width="4" stroke-linejoin="round"/>
  </g>
</template>

<style scoped>
.storm {
  opacity: 0;
  animation: storm 45s both 14s infinite;
  animation-play-state: var(--play-state, paused);
}

.bolt {
  opacity: 0;
  animation: bolt 45s both 14s infinite;
  animation-play-state: var(--play-state, paused);
}

.rain {
  animation: rain 0.9s linear infinite;
  animation-play-state: var(--play-state, paused);
}

@keyframes storm {
  0%        { opacity: 0; transform: translateX(-80px); }
  12%       { opacity: 0.95; }
  40%       { opacity: 0.95; transform: translateX(20px); }
  50%, 100% { opacity: 0; transform: translateX(40px); }
}

@keyframes bolt {
  0%, 26.4%    { opacity: 0; }
  26.5%, 27%   { opacity: 1; }
  27.1%, 27.4% { opacity: 0; }
  27.5%, 28%   { opacity: 1; }
  28.1%, 100%  { opacity: 0; }
}

@keyframes rain {
  from { transform: translateY(0); opacity: 0.9; }
  to   { transform: translateY(240px); opacity: 0; }
}
</style>
