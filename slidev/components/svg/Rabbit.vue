<template>
  <g class="rabbit-container">
    <g transform="translate(509.0 743.0)">

      <!-- Nested SVG clips all rabbit content at local y=30.
           Peek groups pushed 81px down (hidden) have content at y>30 → invisible.
           Peek groups at (0,0) (visible) have content at y<30 → visible. -->
      <svg x="-60" y="-70" width="120" height="100" overflow="hidden" viewBox="-60 -70 120 100">

        <!-- Layer 1: rabbit body — renders behind the bush -->
        <g class="peek" style="--d:12s; --p:19s; --dx:0px; --dy:81px">
          <circle cx="0" cy="12" r="15" fill="#b9b4ac"/>
          <circle class="eye" cx="-6" cy="9" r="2.3" fill="#2a2a2a"/>
          <circle class="eye" cx="6" cy="9" r="2.3" fill="#2a2a2a"/>
          <circle cx="0" cy="16" r="2" fill="#d98c8c"/>
        </g>

        <!-- Layer 2: bush — renders after body, before ears -->
        <ellipse cx="4" cy="2" rx="42" ry="10" fill="rgba(0,0,0,0.22)"/>
        <circle cx="0"  cy="-35" r="28" fill="#29522b"/>
        <circle cx="22" cy="-28" r="20" fill="#29522b"/>
        <circle cx="-18" cy="-29" r="18" fill="#29522b"/>
        <circle cx="8"  cy="-48" r="18" fill="#29522b"/>
        <circle cx="-10" cy="-45" r="15" fill="#29522b"/>
        <circle cx="0"  cy="-39" r="20" fill="#3b763e"/>
        <circle cx="18" cy="-32" r="14" fill="#3b763e"/>
        <circle cx="-14" cy="-33" r="12" fill="#3b763e"/>
        <circle cx="6"  cy="-52" r="12" fill="#3b763e"/>
        <circle cx="-2" cy="-53" r="5"  fill="#568959"/>
        <circle cx="14" cy="-40" r="4"  fill="#568959"/>

        <!-- Layer 3: rabbit ears — renders after bush so they peek above the foliage -->
        <g class="peek" style="--d:12s; --p:19s; --dx:0px; --dy:81px">
          <ellipse cx="-8" cy="-20" rx="6" ry="22" fill="#b9b4ac"/>
          <ellipse cx="8"  cy="-20" rx="6" ry="22" fill="#b9b4ac"/>
          <ellipse cx="-8" cy="-20" rx="2.5" ry="15" fill="#e3a2a2"/>
          <ellipse cx="8"  cy="-20" rx="2.5" ry="15" fill="#e3a2a2"/>
        </g>

      </svg>
    </g>
  </g>
</template>

<style scoped>
.peek {
  opacity: 0;
  animation: peek-hide var(--p, 19s) ease-in-out var(--d, 12s) infinite both;
  animation-play-state: var(--play-state, paused);
}

@keyframes peek-hide {
  0%        { opacity: 0; transform: translate(var(--dx), var(--dy)); }
  2%        { opacity: 1; transform: translate(var(--dx), var(--dy)); }
  8%, 30%   { opacity: 1; transform: translate(0, 0); }
  37%       { opacity: 1; transform: translate(var(--dx), var(--dy)); }
  39%, 100% { opacity: 0; transform: translate(var(--dx), var(--dy)); }
}

</style>
