<template>
  <svg class="canvas" viewBox="0 0 1600 900"
       aria-label="Earth Engine exchanges data with GeoParquet and COG files in object storage, which Lonboard renders in the browser">
    <g v-click>
      <rect class="node" x="560" y="230" width="480" height="300" rx="18"/>
      <path d="M740 300 H860 L845 400 H755 Z" fill="none" stroke="#F2F4F6" stroke-width="5" stroke-linejoin="round"/>
      <text x="800" y="460" text-anchor="middle" font-size="36" font-weight="700">GeoParquet · COG</text>
      <text x="800" y="505" text-anchor="middle" font-size="26" fill="rgba(242,244,246,0.7)">object storage</text>
    </g>
    <g v-click>
      <rect class="node" x="70" y="280" width="340" height="200" rx="18"/>
      <text x="240" y="375" text-anchor="middle" font-size="36" font-weight="700">Earth Engine</text>
      <text x="240" y="420" text-anchor="middle" font-size="26" fill="rgba(242,244,246,0.7)">read &amp; write</text>
      <path class="edge draw" pathLength="1" d="M420 360 H550"/>
      <path class="edge draw" style="--d:0.2s" pathLength="1" d="M550 400 H420"/>
      <path d="M536 348 L556 360 L536 372 Z M434 388 L414 400 L434 412 Z" fill="#FFD626" class="a-fade"/>
    </g>
    <g v-click>
      <path class="edge draw" pathLength="1" d="M1050 380 H1180"/>
      <path d="M1166 368 L1186 380 L1166 392 Z" fill="#FFD626"/>
      <rect class="node key" x="1190" y="260" width="340" height="240" rx="18"/>
      <rect x="1290" y="290" width="140" height="100" rx="8" fill="none" stroke="#F2F4F6" stroke-width="4"/>
      <path d="M1290 312 H1430" stroke="#F2F4F6" stroke-width="4"/>
      <text x="1360" y="440" text-anchor="middle" font-size="36" font-weight="700">Lonboard</text>
      <text x="1360" y="480" text-anchor="middle" font-size="26" fill="rgba(242,244,246,0.7)">in the browser</text>
    </g>
    <g v-click>
      <text x="800" y="700" text-anchor="middle" font-size="44" font-weight="700" fill="#FFD626">Static hosting · GitHub Pages</text>
    </g>
  </svg>
</template>
