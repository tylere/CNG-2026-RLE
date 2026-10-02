<template>
  <svg class="canvas" viewBox="0 0 1600 900"
       aria-label="Three assessment metrics: ecosystem extent, rate of decline, and area of occupancy">
    <g v-click>
      <path d="M150 360 C 170 250, 300 220, 380 270 S 520 300, 500 420 S 420 590, 300 560 S 120 480, 150 360 Z"
            fill="rgba(91,181,138,0.35)" stroke="#5bb58a" stroke-width="4"/>
      <text x="330" y="700" text-anchor="middle" font-size="44" font-weight="700">Extent</text>
    </g>
    <g v-click>
      <path d="M640 220 L640 580 L960 580" fill="none" stroke="rgba(242,244,246,0.5)" stroke-width="3"/>
      <path class="draw" style="--d:0.3s" pathLength="1"
            d="M660 260 C 740 270, 780 330, 830 400 S 910 520, 950 545"
            fill="none" stroke="#e0595a" stroke-width="6" stroke-linecap="round"/>
      <text x="800" y="700" text-anchor="middle" font-size="44" font-weight="700">Rate of decline</text>
    </g>
    <g v-click>
      <g fill="rgba(255,214,38,0.35)" stroke="none">
        <rect x="1130" y="280" width="70" height="70"/><rect x="1200" y="280" width="70" height="70"/>
        <rect x="1060" y="350" width="70" height="70"/><rect x="1130" y="350" width="70" height="70"/>
        <rect x="1200" y="350" width="70" height="70"/><rect x="1270" y="350" width="70" height="70"/>
        <rect x="1130" y="420" width="70" height="70"/><rect x="1200" y="420" width="70" height="70"/>
        <rect x="1270" y="420" width="70" height="70"/><rect x="1200" y="490" width="70" height="70"/>
      </g>
      <path d="M1090 390 C 1100 300, 1200 270, 1250 310 S 1330 370, 1320 450 S 1260 560, 1220 540 S 1080 470, 1090 390 Z"
            fill="rgba(91,181,138,0.35)" stroke="#5bb58a" stroke-width="4"/>
      <g stroke="rgba(242,244,246,0.35)" stroke-width="2">
        <path d="M1060 210 V630 M1130 210 V630 M1200 210 V630 M1270 210 V630 M1340 210 V630 M1410 210 V630"/>
        <path d="M1060 210 H1410 M1060 280 H1410 M1060 350 H1410 M1060 420 H1410 M1060 490 H1410 M1060 560 H1410 M1060 630 H1410"/>
      </g>
      <text x="1235" y="700" text-anchor="middle" font-size="44" font-weight="700">Area of occupancy</text>
    </g>
    <text class="label" x="800" y="110" text-anchor="middle">WHAT AN ASSESSMENT COMPUTES</text>
  </svg>
</template>
