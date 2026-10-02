<template>
  <g class="beaver-scene">
    <!-- Dam structure (static until animation grows it) -->
    <g class="dam">
      <ellipse cx="515" cy="689" rx="36" ry="7" fill="#6b4a2b"/>
      <line x1="481.0" y1="686.4" x2="495.0" y2="676.0" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="488.0" y1="686.0" x2="502.0" y2="674.1" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="495.0" y1="692.8" x2="509.0" y2="674.3" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="502.0" y1="692.1" x2="516.0" y2="676.5" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="509.0" y1="686.0" x2="523.0" y2="676.6" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="516.0" y1="689.1" x2="530.0" y2="674.3" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="523.0" y1="689.3" x2="537.0" y2="674.0" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="530.0" y1="687.4" x2="544.0" y2="678.3" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
      <line x1="537.0" y1="691.8" x2="551.0" y2="675.1" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>
    </g>
    <!-- Fish jumping in central pond -->
    <g transform="translate(760.0 712.0)">
      <ellipse class="splash s1" cx="0" cy="0" rx="14" ry="5" fill="none" stroke="#bfe0f5" stroke-width="2"/>
      <ellipse class="splash s2" cx="56" cy="0" rx="14" ry="5" fill="none" stroke="#bfe0f5" stroke-width="2"/>
      <g class="fish">
        <path d="M-14 0 Q-4 -9 10 -2 L18 -8 L16 0 L18 8 L10 2 Q-4 9 -14 0 Z" fill="#f08a3c"/>
        <circle cx="-8" cy="-1" r="1.6" fill="#1a1a1a"/>
      </g>
    </g>
    <!-- Sapling being felled (log-move wraps log-fall) -->
    <g transform="translate(610 748)">
      <g class="log-move" style="--mx:-35px; --my:-58px">
        <g class="log-fall">
          <g class="grow" style="--d:1.5s">
            <polygon points="-5.2,0.0 -2.9,-66.7 2.9,-66.7 5.2,0.0" fill="#725132"/>
            <path d="M0 -47.7 L-19.0 -71.9 M0 -54.6 L17.2 -77.1" stroke="#725132" stroke-width="2.8" stroke-linecap="round" fill="none"/>
            <circle cx="0.0" cy="-73.6" r="24.8" fill="#3c602d"/>
            <circle cx="19.3" cy="-75.9" r="15.4" fill="#3c602d"/>
            <circle cx="8.7" cy="-61.8" r="20.1" fill="#3c602d"/>
            <circle cx="-6.2" cy="-61.0" r="17.2" fill="#3c602d"/>
            <circle cx="-18.1" cy="-75.8" r="17.3" fill="#3c602d"/>
            <circle cx="-7.1" cy="-85.7" r="18.8" fill="#3c602d"/>
            <circle cx="7.2" cy="-85.3" r="17.8" fill="#3c602d"/>
            <circle cx="-3.5" cy="-77.1" r="21.4" fill="#568a41"/>
            <circle cx="17.2" cy="-78.1" r="13.2" fill="#568a41"/>
            <circle cx="5.9" cy="-64.6" r="17.3" fill="#568a41"/>
            <circle cx="-8.6" cy="-63.4" r="14.8" fill="#568a41"/>
            <circle cx="-20.5" cy="-78.2" r="14.9" fill="#568a41"/>
            <circle cx="-9.8" cy="-88.3" r="16.2" fill="#568a41"/>
            <circle cx="4.7" cy="-87.8" r="15.3" fill="#568a41"/>
            <circle cx="-12.8" cy="-91.7" r="6.6" fill="#6d9a5b"/>
            <circle cx="-11.4" cy="-66.5" r="6.0" fill="#6d9a5b"/>
          </g>
        </g>
      </g>
    </g>
    <!-- Wood chips flying off during chewing -->
    <g transform="translate(616 748)">
      <g class="chips">
        <circle class="chip" style="animation-delay:0.00s" cx="-1.3" cy="-6.8" r="2.2" fill="#d9b38c"/>
        <circle class="chip" style="animation-delay:-0.13s" cx="-4.1" cy="-8.5" r="2.2" fill="#d9b38c"/>
        <circle class="chip" style="animation-delay:-0.26s" cx="-0.5" cy="-9.3" r="2.2" fill="#d9b38c"/>
        <circle class="chip" style="animation-delay:-0.39s" cx="-1.4" cy="-13.3" r="2.2" fill="#d9b38c"/>
        <circle class="chip" style="animation-delay:-0.52s" cx="1.0" cy="-11.6" r="2.2" fill="#d9b38c"/>
      </g>
    </g>
    <!-- Beaver -->
    <g transform="translate(650.0 752.0)">
      <g class="beaver" style="--mx:-35px; --my:-58px">
        <g transform="scale(1.25)">
          <ellipse cx="2" cy="1" rx="26" ry="4" fill="rgba(0,0,0,0.28)"/>
          <ellipse cx="25" cy="-5" rx="15" ry="5" fill="#3b2a1d"/>
          <ellipse cx="0" cy="-12" rx="21" ry="12" fill="#6b4428"/>
          <ellipse cx="-10" cy="-1" rx="5" ry="3" fill="#3b2a1d"/>
          <ellipse cx="9" cy="-1" rx="5" ry="3" fill="#3b2a1d"/>
          <g class="beaver-head">
            <circle cx="-19" cy="-17" r="10" fill="#6b4428"/>
            <circle cx="-15" cy="-26" r="3" fill="#3b2a1d"/>
            <circle cx="-23" cy="-19" r="1.7" fill="#111"/>
            <circle cx="-29" cy="-15" r="2.4" fill="#111"/>
            <rect x="-28" y="-11" width="4" height="4" fill="#e3a83a"/>
          </g>
        </g>
      </g>
    </g>
  </g>
</template>

<style scoped>
/* Beaver story: 30s cycle, starts 9s in */
.beaver,
.log-fall,
.log-move,
.chips,
.dam {
  animation-duration: 30s;
  animation-delay: 9s;
  animation-fill-mode: both;
  animation-play-state: var(--play-state, paused);
}

.log-fall,
.chip {
  transform-box: fill-box;
  transform-origin: 50% 100%;
}

.beaver,
.chips,
.dam { opacity: 0; }

.beaver     { animation-name: beaver; }
.log-fall   { animation-name: log-fall; }
.log-move   { animation-name: log-move; }
.chips      { animation-name: chips; }
.dam        { animation-name: dam; }

.beaver-head {
  transform-box: fill-box;
  transform-origin: 80% 80%;
  animation: chew 0.3s ease-in-out infinite alternate;
  animation-play-state: var(--play-state, paused);
}

.chip {
  animation: chip-hop 0.65s ease-out infinite;
  animation-play-state: var(--play-state, paused);
}

/* Fish jumping in pond */
.fish,
.splash { opacity: 0; }

.fish {
  animation: fish-jump 23s ease-in-out 12s infinite both;
  animation-play-state: var(--play-state, paused);
}

.splash.s1 {
  animation: splash 23s ease-out 12s infinite both;
  animation-play-state: var(--play-state, paused);
}

.splash.s2 {
  animation: splash 23s ease-out 12.9s infinite both;
  animation-play-state: var(--play-state, paused);
}

@keyframes beaver {
  0%        { opacity: 0; transform: translate(-10px, -12px); }
  5%        { opacity: 1; transform: translate(-10px, -17px); }
  12%, 48%  { opacity: 1; transform: translate(0, 0); }
  80%, 86%  { opacity: 1; transform: translate(var(--mx), var(--my)); }
  96%       { opacity: 1; transform: translate(-10px, -17px); }
  100%      { opacity: 0; transform: translate(-10px, -12px); }
}

@keyframes log-fall {
  0%, 30%   { transform: rotate(0deg); }
  32%       { transform: rotate(-3deg); }
  34%       { transform: rotate(3deg); }
  36%       { transform: rotate(-4deg); }
  38%       { transform: rotate(2deg); }
  40%       { transform: rotate(0deg); animation-timing-function: ease-in; }
  46%, 100% { transform: rotate(-86deg); }
}

@keyframes log-move {
  0%, 50%   { transform: translate(0, 0); }
  80%, 100% { transform: translate(var(--mx), var(--my)); }
}

@keyframes chips {
  0%, 14%   { opacity: 0; }
  15%, 38%  { opacity: 1; }
  40%, 100% { opacity: 0; }
}

@keyframes dam {
  0%, 80%   { opacity: 0; }
  86%, 100% { opacity: 1; }
}

@keyframes chew {
  from { transform: rotate(0deg); }
  to   { transform: rotate(-8deg); }
}

@keyframes chip-hop {
  from { transform: translate(0, 0); opacity: 1; }
  to   { transform: translate(-12px, -18px); opacity: 0; }
}

@keyframes fish-jump {
  0%          { opacity: 0; transform: translate(0, 0) rotate(-55deg); }
  0.5%        { opacity: 1; }
  2%          { transform: translate(28px, -62px) rotate(0deg); }
  4%          { opacity: 1; transform: translate(56px, 0) rotate(55deg); }
  4.5%, 100%  { opacity: 0; transform: translate(56px, 0) rotate(55deg); }
}

@keyframes splash {
  0%    { opacity: 0.9; transform: scale(0.4); }
  6%    { opacity: 0; transform: scale(2.2); }
  100%  { opacity: 0; transform: scale(2.2); }
}
</style>
