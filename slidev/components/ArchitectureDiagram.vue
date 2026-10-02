<template>
  <svg class="canvas" viewBox="0 0 1600 900"
       aria-label="Workflow overview: IUCN standards inform code repositories, which compute RLE criteria from ecosystem map data and feed a publishing workflow">
    <!-- IUCN standards (always visible) -->
    <g>
      <text class="label" x="70" y="80">IUCN STANDARDS</text>
      <image href="../images/iucn_guidelines_cover.png" x="70" y="110" width="220" height="311"/>
      <rect x="70" y="470" width="360" height="248" rx="8" fill="#fff"/>
      <image href="../images/get_hierarchy.png" x="80" y="480" width="340" height="228"/>
    </g>
    <!-- Code repositories -->
    <g v-click>
      <path class="edge draw" pathLength="1" d="M300 265 C 400 265, 420 215, 540 215"/>
      <path class="edge draw" style="--d:0.2s" pathLength="1" d="M440 590 C 490 590, 490 435, 540 435"/>
      <text class="label" x="540" y="120">GITHUB REPOSITORIES</text>
      <rect x="520" y="140" width="420" height="640" rx="16" fill="none" stroke="rgba(242,244,246,0.25)" stroke-width="2" stroke-dasharray="10 8"/>
      <rect class="node" x="550" y="170" width="360" height="90" rx="14"/>
      <text x="730" y="226" text-anchor="middle" font-size="32" font-family="Berkeley Mono, monospace">iucn-get-data</text>
      <rect class="node" x="550" y="390" width="360" height="90" rx="14"/>
      <text x="730" y="446" text-anchor="middle" font-size="32" font-family="Berkeley Mono, monospace">rle-python-gee</text>
      <rect class="node" x="550" y="610" width="360" height="130" rx="14"/>
      <text x="730" y="665" text-anchor="middle" font-size="32" font-family="Berkeley Mono, monospace">TEMPLATE-</text>
      <text x="730" y="705" text-anchor="middle" font-size="32" font-family="Berkeley Mono, monospace">rle-assessment</text>
    </g>
    <!-- Data + calculations -->
    <g v-click>
      <rect class="node" x="1060" y="60" width="440" height="190" rx="14"/>
      <image href="../images/colombia_ecosystems.png" x="1350" y="72" width="122" height="166"/>
      <text x="1090" y="140" font-size="34" font-weight="700">Ecosystem</text>
      <text x="1090" y="184" font-size="34" font-weight="700">map data</text>
      <path class="edge draw" pathLength="1" d="M910 215 C 990 215, 990 390, 1060 390"/>
      <path class="edge draw" style="--d:0.15s" pathLength="1" d="M910 435 C 990 435, 990 420, 1060 420"/>
      <path class="edge draw" style="--d:0.3s" pathLength="1" d="M1280 250 L1280 330"/>
      <rect class="node key" x="1060" y="330" width="440" height="150" rx="14"/>
      <text x="1280" y="397" text-anchor="middle" font-size="34" font-weight="700">RLE criteria</text>
      <text x="1280" y="441" text-anchor="middle" font-size="34" font-weight="700">calculations</text>
    </g>
    <!-- Publishing -->
    <g v-click>
      <path class="edge draw" pathLength="1" d="M1280 480 L1280 590"/>
      <path class="edge draw" style="--d:0.15s" pathLength="1" d="M910 675 C 980 675, 990 660, 1060 660"/>
      <rect class="node key" x="1060" y="590" width="440" height="150" rx="14"/>
      <text x="1280" y="657" text-anchor="middle" font-size="34" font-weight="700">Scientific &amp; technical</text>
      <text x="1280" y="701" text-anchor="middle" font-size="34" font-weight="700">publishing</text>
    </g>
  </svg>
</template>
