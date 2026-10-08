<script setup lang="ts">
import { useId } from 'vue'

// Per-instance marker id (see svg/Mountains.vue for why)
const props = defineProps<{
  noClicks?: boolean // show everything at once (v-click="false" registers no click)
  highlightMaps?: boolean // spotlight the "Ecosystem map data" box
}>()

const arrowId = `${useId()}-arrow`
const arrow = `url(#${arrowId})`
</script>

<template>
  <div style="position:relative; width:100%; height:100%">
  <svg class="canvas" viewBox="0 0 1600 900" style="width:100%;height:100%"
       aria-label="Workflow overview: IUCN standards inform code repositories, which compute RLE criteria from ecosystem map data and feed a publishing workflow">
    <defs>
      <!-- Tip sits exactly on the path's end point; sized in stroke widths (4px edge → 20px head) -->
      <marker :id="arrowId" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="5" markerHeight="5" orient="auto">
        <path d="M0 0 L10 5 L0 10 Z" fill="#FFD626"/>
      </marker>
    </defs>
    <!-- IUCN standards (always visible) -->
    <g>
      <text class="label" x="70" y="80">IUCN STANDARDS</text>
    </g>
    <!-- Code repositories -->
    <g v-click="!props.noClicks">
      <path class="edge draw" pathLength="1" :marker-end="arrow" d="M370 265 C 450 265, 450 215, 550 215"/>
      <path class="edge draw" style="--d:0.2s" pathLength="1" :marker-end="arrow" d="M440 590 C 490 590, 490 435, 550 435"/>
      <text class="label" x="540" y="120">GITHUB REPOSITORIES</text>
      <rect x="520" y="140" width="420" height="640" rx="16" fill="none" stroke="rgba(242,244,246,0.25)" stroke-width="2" stroke-dasharray="10 8"/>
      <rect class="node" x="550" y="170" width="360" height="90" rx="14"/>
      <text x="730" y="226" text-anchor="middle" font-size="32px" font-family="Berkeley Mono, monospace">rle-python</text>
      <rect class="node" x="550" y="390" width="360" height="90" rx="14"/>
      <text x="730" y="446" text-anchor="middle" font-size="32px" font-family="Berkeley Mono, monospace">iucn-get-data</text>
    </g>
    <!-- Data + calculations -->
    <g v-click="!props.noClicks">
      <rect class="node" x="1060" y="60" width="440" height="190" rx="14"/>
      <image href="/images/colombia_ecosystems.png" x="1350" y="72" width="122" height="166"/>
      <text x="1090" y="140" font-size="34px" font-weight="700">Ecosystem</text>
      <text x="1090" y="184" font-size="34px" font-weight="700">map data</text>
      <path class="edge draw" pathLength="1" :marker-end="arrow" d="M910 215 C 990 215, 990 390, 1060 390"/>
      <path class="edge draw" style="--d:0.15s" pathLength="1" :marker-end="arrow" d="M910 435 C 990 435, 990 420, 1060 420"/>
      <path class="edge draw" style="--d:0.3s" pathLength="1" :marker-end="arrow" d="M1280 250 L1280 330"/>
      <rect class="node key" x="1060" y="330" width="440" height="150" rx="14"/>
      <text x="1280" y="397" text-anchor="middle" font-size="34px" font-weight="700">RLE criteria</text>
      <text x="1280" y="441" text-anchor="middle" font-size="34px" font-weight="700">calculations</text>
    </g>
    <!-- Assessment template repository -->
    <g v-click="!props.noClicks">
      <rect class="node" x="550" y="610" width="360" height="130" rx="14"/>
      <text x="730" y="665" text-anchor="middle" font-size="32px" font-family="Berkeley Mono, monospace">TEMPLATE-</text>
      <text x="730" y="705" text-anchor="middle" font-size="32px" font-family="Berkeley Mono, monospace">rle-assessment</text>
    </g>
    <!-- Publishing -->
    <g v-click="!props.noClicks">
      <path class="edge draw" pathLength="1" :marker-end="arrow" d="M1280 480 L1280 590"/>
      <path class="edge draw" style="--d:0.15s" pathLength="1" :marker-end="arrow" d="M910 675 C 980 675, 990 660, 1060 660"/>
      <rect class="node key" x="1060" y="590" width="440" height="150" rx="14"/>
      <text x="1280" y="657" text-anchor="middle" font-size="34px" font-weight="700">Scientific &amp; technical</text>
      <text x="1280" y="701" text-anchor="middle" font-size="34px" font-weight="700">publishing</text>
      <!-- Out to the world: off the right edge of the slide -->
      <path class="edge draw" style="--d:0.3s" pathLength="1" :marker-end="arrow" d="M1500 665 L1600 665"/>
    </g>
    <!-- Spotlight on the ecosystem map data box (recap slide) -->
    <g v-if="props.highlightMaps" class="maps-hl">
      <rect x="1046" y="46" width="468" height="218" rx="22" fill="none" stroke="#FFD626" stroke-width="9"/>
    </g>
  </svg>
  <!-- IUCN standards as 3-D objects (HTML, since CSS 3-D transforms don't apply inside SVG) -->
  <span class="book face-right" style="--pages:177; position:absolute; left:140px; top:110px">
    <img src="/images/iucn_rle_guidelines_2024_cover.jpg" style="width:220px; height:311px" alt="Cover of the IUCN Red List of Ecosystems guidelines" class="shadow" />
  </span>
  <span class="book face-right screen" style="--pages:220; position:absolute; left:70px; top:478px">
    <img src="/images/global_ecosystems_explore.jpg" style="width:360px; height:225px" alt="Explore page of the Global Ecosystem Typology website" class="shadow" />
  </span>
  </div>
</template>

<style scoped>
.maps-hl {
  filter: drop-shadow(0 0 14px rgba(255, 214, 38, 0.9)) drop-shadow(0 0 32px rgba(255, 214, 38, 0.6));
  transform-box: fill-box;
  transform-origin: center;
  animation: maps-hl-in 0.6s ease-out 1s both, maps-hl-pulse 1.6s ease-in-out 1.6s 3;
}
@keyframes maps-hl-in {
  from { opacity: 0; transform: scale(1.15); }
  to   { opacity: 1; transform: scale(1); }
}
@keyframes maps-hl-pulse {
  0%, 100% { transform: scale(1); }
  50%      { transform: scale(1.04); }
}
</style>
