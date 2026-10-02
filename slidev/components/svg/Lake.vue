<template>
  <g class="lake">
    <!-- Left beaver pond + stream (drawn before trees) -->
    <polygon points="339.0,546.3 296.8,574.0 367.4,601.1 333.2,633.6 437.0,664.7 535.7,708.1 544.3,687.9 443.0,647.3 342.8,622.4 376.6,594.9 303.2,570.0 341.0,549.7" fill="#2f6f9e"/>
    <polyline class="flow" points="340.0,548.0 300.0,572.0 372.0,598.0 338.0,628.0 440.0,656.0 540.0,698.0" stroke="#7fc0ea" stroke-width="2.5" fill="none" stroke-linejoin="round"/>
    <!-- Central pond where deer drinks (drawn after trees in z-order; EcosystemScene places this group late) -->
    <g class="central-pond">
      <ellipse cx="800.0" cy="706.0" rx="314.0" ry="51.0" fill="#9c8a62"/>
      <ellipse cx="800.0" cy="706.0" rx="300.0" ry="42.0" fill="url(#side-water)"/>
      <ellipse cx="1076.8" cy="726.6" rx="4.2" ry="2.2" fill="#8a8f96"/><ellipse cx="1076.1" cy="726.8" rx="4.7" ry="2.2" fill="#958f86"/><ellipse cx="515.8" cy="724.1" rx="4.6" ry="2.2" fill="#958f86"/><ellipse cx="814.5" cy="752.9" rx="3.4" ry="2.2" fill="#8a8f96"/><ellipse cx="1066.1" cy="729.7" rx="4.2" ry="2.2" fill="#6f747b"/><ellipse cx="769.6" cy="752.8" rx="4.3" ry="2.2" fill="#958f86"/><ellipse cx="857.6" cy="752.2" rx="4.0" ry="2.2" fill="#8a8f96"/><ellipse cx="540.7" cy="680.6" rx="2.9" ry="2.2" fill="#8a8f96"/><ellipse cx="512.7" cy="722.9" rx="3.0" ry="2.2" fill="#7b8088"/><ellipse cx="662.6" cy="663.9" rx="4.5" ry="2.2" fill="#958f86"/><ellipse cx="492.3" cy="707.9" rx="2.7" ry="2.2" fill="#7b8088"/><ellipse cx="661.2" cy="664.0" rx="3.3" ry="2.2" fill="#7b8088"/><ellipse cx="875.0" cy="660.4" rx="3.9" ry="2.2" fill="#7b8088"/><ellipse cx="516.4" cy="687.7" rx="4.6" ry="2.2" fill="#7b8088"/><ellipse cx="937.2" cy="663.9" rx="3.7" ry="2.2" fill="#7b8088"/><ellipse cx="500.4" cy="695.1" rx="3.1" ry="2.2" fill="#958f86"/><ellipse cx="990.4" cy="669.1" rx="4.3" ry="2.2" fill="#958f86"/><ellipse cx="616.8" cy="743.8" rx="2.6" ry="2.2" fill="#7b8088"/><ellipse cx="723.5" cy="660.5" rx="3.7" ry="2.2" fill="#6f747b"/><ellipse cx="855.2" cy="752.2" rx="4.9" ry="2.2" fill="#958f86"/><ellipse cx="538.4" cy="681.2" rx="3.1" ry="2.2" fill="#8a8f96"/><ellipse cx="1105.1" cy="699.6" rx="2.9" ry="2.2" fill="#8a8f96"/><ellipse cx="1018.2" cy="739.2" rx="4.0" ry="2.2" fill="#958f86"/><ellipse cx="1106.5" cy="710.6" rx="4.7" ry="2.2" fill="#958f86"/><ellipse cx="887.6" cy="751.1" rx="3.1" ry="2.2" fill="#958f86"/><ellipse cx="1081.9" cy="687.1" rx="2.9" ry="2.2" fill="#958f86"/><ellipse cx="1066.3" cy="682.4" rx="3.2" ry="2.2" fill="#6f747b"/><ellipse cx="500.2" cy="695.2" rx="4.2" ry="2.2" fill="#6f747b"/><ellipse cx="1105.8" cy="700.3" rx="3.4" ry="2.2" fill="#6f747b"/><ellipse cx="923.6" cy="749.1" rx="3.6" ry="2.2" fill="#8a8f96"/><ellipse cx="492.6" cy="709.0" rx="4.5" ry="2.2" fill="#7b8088"/><ellipse cx="955.4" cy="746.6" rx="4.2" ry="2.2" fill="#6f747b"/><ellipse cx="1107.9" cy="704.7" rx="4.5" ry="2.2" fill="#7b8088"/><ellipse cx="1058.1" cy="680.4" rx="4.9" ry="2.2" fill="#7b8088"/>
      <path d="M590.0 718.0 m-9 0 a9 4.5 0 1 0 18 0 l-9 0 z" fill="#4f8a3c"/>
      <path d="M615.0 728.0 m-9 0 a9 4.5 0 1 0 18 0 l-9 0 z" fill="#4f8a3c"/>
      <path d="M990.0 698.0 m-9 0 a9 4.5 0 1 0 18 0 l-9 0 z" fill="#4f8a3c"/>
      <path d="M950.0 726.0 m-9 0 a9 4.5 0 1 0 18 0 l-9 0 z" fill="#4f8a3c"/>
      <ellipse class="ripple" style="animation-delay:0s" cx="860.0" cy="700.0" rx="16" ry="6" fill="none" stroke="#9fd0ee" stroke-width="1.5"/>
      <ellipse class="ripple" style="animation-delay:1.7s" cx="710.0" cy="718.0" rx="16" ry="6" fill="none" stroke="#9fd0ee" stroke-width="1.5"/>
      <ellipse class="ripple" style="animation-delay:3.1s" cx="780.0" cy="688.0" rx="16" ry="6" fill="none" stroke="#9fd0ee" stroke-width="1.5"/>
      <ellipse class="drink-ripple" cx="1072.0" cy="695.2" rx="10" ry="4" fill="none" stroke="#bfe0f5" stroke-width="1.5"/>
    </g>
  </g>
</template>

<style scoped>
.flow {
  stroke-dasharray: 6 14;
  animation: flow 1.6s linear infinite;
  animation-play-state: var(--play-state, paused);
}

@keyframes flow {
  to { stroke-dashoffset: -20; }
}

.ripple {
  transform-box: fill-box;
  transform-origin: 50% 50%;
  animation: ripple 5s ease-out infinite both;
  animation-play-state: var(--play-state, paused);
}

@keyframes ripple {
  from { opacity: 0.8; transform: scale(0.3); }
  to   { opacity: 0; transform: scale(2); }
}

.drink-ripple {
  transform-box: fill-box;
  transform-origin: 50% 50%;
  opacity: 0;
  animation: drink-ripple 9s ease-out 9s infinite both;
  animation-play-state: var(--play-state, paused);
}

@keyframes drink-ripple {
  0%, 20%  { opacity: 0; transform: scale(0.4); }
  22%      { opacity: 1; }
  48%      { opacity: 0; transform: scale(2.4); }
  100%     { opacity: 0; transform: scale(2.4); }
}
</style>
