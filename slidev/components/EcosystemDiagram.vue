<script setup lang="ts">
import { useId } from 'vue'

// Per-instance marker id (see svg/Mountains.vue for why)
const arrow = `${useId()}-arrow`

// Earthworm burrows in the bottom-right soil strip (screen x)
const worms = [970, 1090, 1210, 1330]

// Two undulation poses (same command structure so SMIL can morph between them);
// head at x=0, tail runs along +x into the soil
const wormA = 'M0 0 C20 -12 40 12 60 0 S95 -10 120 0'
const wormB = 'M0 0 C20 12 40 -12 60 0 S95 10 120 0'

// Pebbles in the soil strip: [cx, cy, r]
const pebbles = [[920, 888, 3], [1030, 892, 4], [1150, 886, 2.5], [1270, 890, 3.5], [1400, 887, 3], [1500, 893, 4]]
</script>

<template>
  <svg class="canvas" viewBox="0 0 1600 900" style="width:100%;height:100%"
       aria-label="An ecosystem: a biotic complex and an abiotic environment interacting within a physical space">
    <defs>
      <marker :id="arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M0 0 L10 5 L0 10 Z" fill="#FFD626"/>
      </marker>
    </defs>

    <text class="label" x="800" y="100" text-anchor="middle">WHAT IS AN ECOSYSTEM?</text>

    <!-- Physical space -->
    <g v-click="3">
      <rect x="150" y="150" width="1300" height="640" rx="40"
            fill="rgba(242,244,246,0.03)" stroke="rgba(242,244,246,0.5)" stroke-width="3" stroke-dasharray="14 10"/>
      <text class="label" x="190" y="760">PHYSICAL SPACE</text>
    </g>

    <!-- Biotic complex -->
    <g class="a-fade" style="--d:0.2s">
      <circle cx="520" cy="460" r="220" fill="rgba(91,181,138,0.18)" stroke="#5bb58a" stroke-width="4"/>
      <text x="520" y="455" text-anchor="middle" font-size="48px" font-weight="700">Biotic</text>
      <text x="520" y="510" text-anchor="middle" font-size="48px" font-weight="700">complex</text>
      <text x="520" y="560" text-anchor="middle" font-size="22px" opacity="0.7">plants · animals · microbes</text>
    </g>

    <!-- Abiotic environment -->
    <g class="a-fade" style="--d:0.6s">
      <circle cx="1080" cy="460" r="220" fill="rgba(65,139,217,0.15)" stroke="#418BD9" stroke-width="4"/>
      <text x="1080" y="455" text-anchor="middle" font-size="48px" font-weight="700">Abiotic</text>
      <text x="1080" y="510" text-anchor="middle" font-size="48px" font-weight="700">environment</text>
      <text x="1080" y="560" text-anchor="middle" font-size="22px" opacity="0.7">climate · water · soil · light</text>
    </g>

    <!-- Interactions within each component -->
    <g v-click="1">
      <path d="M548 340 A 30 30 0 1 1 520 310" fill="none" stroke="#FFD626" stroke-width="4" :marker-end="`url(#${arrow})`"/>
      <path d="M1108 340 A 30 30 0 1 1 1080 310" fill="none" stroke="#FFD626" stroke-width="4" :marker-end="`url(#${arrow})`"/>
    </g>

    <!-- Interactions between them -->
    <g v-click="2">
      <path d="M685 305 Q 800 195 915 305" fill="none" stroke="#FFD626" stroke-width="5" stroke-linecap="round" :marker-end="`url(#${arrow})`"/>
      <path d="M915 615 Q 800 725 685 615" fill="none" stroke="#FFD626" stroke-width="5" stroke-linecap="round" :marker-end="`url(#${arrow})`"/>
      <text x="800" y="215" text-anchor="middle" font-size="28px" font-weight="700" style="fill:#FFD626">interactions</text>
    </g>

    <!-- Ecosystem engineers: biota that reshape the abiotic environment.
         Animations start when v-click removes .slidev-vclick-hidden. -->
    <g v-click="4" class="engineers">
      <!-- Beaver peeking in from the left edge -->
      <g transform="translate(0 470)">
        <g class="beaver-peek">
          <ellipse cx="-20" cy="30" rx="70" ry="45" fill="#6b4428"/>
          <ellipse cx="50" cy="66" rx="14" ry="8" fill="#3b2a1d"/>
          <circle cx="60" cy="0" r="38" fill="#6b4428"/>
          <circle cx="38" cy="-32" r="10" fill="#3b2a1d"/>
          <ellipse cx="86" cy="14" rx="16" ry="11" fill="#8a5a36"/>
          <circle cx="72" cy="-10" r="5" fill="#111"/>
          <circle cx="73.5" cy="-11.5" r="1.5" fill="#fff"/>
          <rect x="80" y="22" width="12" height="14" rx="2" fill="#e3a83a"/>
          <line x1="86" y1="22" x2="86" y2="36" stroke="#b07d22" stroke-width="1.5"/>
          <ellipse class="beaver-nose" cx="96" cy="4" rx="9" ry="7" fill="#111"/>
        </g>
      </g>

      <!-- Coral rising from the bottom edge (left half) -->
      <g transform="translate(230 900)">
        <g class="coral-rise" style="--d:0.2s">
          <path d="M0 0 L0 -45 L-24 -72 L-30 -92 M0 -45 L20 -80 M-12 -58 L-36 -66 M8 -64 L28 -70"
                fill="none" stroke="#ff7f6e" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
      </g>
      <g transform="translate(350 900)">
        <g class="coral-rise" style="--d:0.5s">
          <path d="M-55 0 A55 48 0 0 1 55 0 Z" fill="#e8a33d"/>
          <path d="M-40 -8 Q-30 -30 -15 -16 T15 -22 T40 -8 M-30 -26 Q-10 -48 10 -34 T32 -26"
                fill="none" stroke="#b9781f" stroke-width="3" stroke-linecap="round"/>
        </g>
      </g>
      <g transform="translate(480 900)">
        <g class="coral-rise" style="--d:0.8s">
          <path d="M0 0 C-50 -28 -60 -72 -30 -88 C-10 -96 10 -96 30 -88 C60 -72 50 -28 0 0 Z" fill="rgba(200,95,160,0.35)"/>
          <path d="M0 0 L-40 -74 M0 0 L-18 -90 M0 0 L4 -92 M0 0 L26 -88 M0 0 L44 -68"
                fill="none" stroke="#c85fa0" stroke-width="3.5" stroke-linecap="round"/>
        </g>
      </g>
      <g transform="translate(600 900)">
        <g class="coral-rise" style="--d:1.1s">
          <rect x="-34" y="-62" width="16" height="62" rx="8" fill="#f4b860"/>
          <rect x="-12" y="-92" width="16" height="92" rx="8" fill="#f4b860"/>
          <rect x="10" y="-74" width="16" height="74" rx="8" fill="#f4b860"/>
          <rect x="32" y="-48" width="16" height="48" rx="8" fill="#f4b860"/>
        </g>
      </g>
      <g transform="translate(710 900)">
        <g class="coral-rise" style="--d:1.4s">
          <path d="M0 0 L0 -40 L-20 -64 L-22 -88 M0 -40 L24 -66 L30 -90 M24 -66 L44 -74"
                fill="none" stroke="#ff9a8a" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
      </g>
      <g transform="translate(820 900)">
        <g class="coral-rise" style="--d:1.7s">
          <path d="M-44 0 A44 36 0 0 1 44 0 Z" fill="#7fbf9a"/>
          <path d="M-30 -8 Q-20 -26 -6 -14 T26 -12" fill="none" stroke="#4e8f6a" stroke-width="3" stroke-linecap="round"/>
        </g>
      </g>

      <!-- Amazon rainforest along the right edge, standing on the soil strip -->
      <g transform="translate(1530 872)">
        <g class="amazon-grow" style="--d:0.3s">
          <circle cx="-55" cy="-110" r="20" fill="#173d22"/>
          <circle cx="-48" cy="-175" r="24" fill="#1f4d2b"/>
          <circle cx="-10" cy="-140" r="30" fill="#173d22"/>
          <circle cx="25" cy="-195" r="28" fill="#1f4d2b"/>
          <circle cx="58" cy="-150" r="26" fill="#173d22"/>
          <circle cx="62" cy="-225" r="22" fill="#173d22"/>
          <circle cx="-45" cy="-230" r="20" fill="#173d22"/>
          <circle cx="0" cy="-235" r="26" fill="#173d22"/>
          <circle cx="35" cy="-100" r="26" fill="#1f4d2b"/>
          <circle cx="-25" cy="-80" r="26" fill="#1f4d2b"/>
          <circle cx="-54" cy="-45" r="22" fill="#173d22"/>
          <circle cx="0" cy="-50" r="28" fill="#173d22"/>
          <circle cx="52" cy="-48" r="26" fill="#173d22"/>
        </g>
      </g>
      <g transform="translate(1580 872)">
        <g class="amazon-grow" style="--d:1.4s">
          <polygon points="-5,0 -2.5,-230 2.5,-230 5,0" fill="#8a7a66"/>
          <path d="M0 -215 L-24 -232 M0 -220 L22 -236" stroke="#8a7a66" stroke-width="4" stroke-linecap="round"/>
          <ellipse cx="0" cy="-240" rx="44" ry="16" fill="#2f6b3a"/>
          <ellipse cx="-20" cy="-248" rx="26" ry="12" fill="#3f8a4a"/>
          <ellipse cx="20" cy="-246" rx="28" ry="12" fill="#3f8a4a"/>
          <ellipse cx="0" cy="-254" rx="28" ry="11" fill="#5aa05a"/>
        </g>
      </g>
      <g transform="translate(1515 872)">
        <g class="amazon-grow" style="--d:1.1s">
          <path d="M-22 0 Q-8 -10 -5 -40 L5 -40 Q8 -10 22 0 Z" fill="#8a7a66"/>
          <polygon points="-6,0 -3,-290 3,-290 6,0" fill="#8a7a66"/>
          <path d="M0 -275 L-30 -296 M0 -280 L28 -300" stroke="#8a7a66" stroke-width="4" stroke-linecap="round"/>
          <ellipse cx="0" cy="-302" rx="50" ry="18" fill="#2f6b3a"/>
          <ellipse cx="-24" cy="-310" rx="30" ry="14" fill="#3f8a4a"/>
          <ellipse cx="24" cy="-308" rx="32" ry="14" fill="#3f8a4a"/>
          <ellipse cx="0" cy="-318" rx="34" ry="13" fill="#5aa05a"/>
        </g>
      </g>
      <g transform="translate(1488 872)">
        <g class="amazon-grow" style="--d:0.5s">
          <polygon points="-4,0 -2,-150 2,-150 4,0" fill="#6e5e4a"/>
          <circle cx="-6" cy="-160" r="26" fill="#1f4d2b"/>
          <circle cx="12" cy="-178" r="24" fill="#2e6b3a"/>
          <circle cx="4" cy="-150" r="22" fill="#2e6b3a"/>
          <circle cx="-4" cy="-184" r="18" fill="#3f8a4a"/>
        </g>
      </g>
      <g transform="translate(1562 872)">
        <g class="amazon-grow" style="--d:0.7s">
          <polygon points="-4,0 -2,-120 2,-120 4,0" fill="#6e5e4a"/>
          <circle cx="0" cy="-130" r="30" fill="#1f4d2b"/>
          <circle cx="-18" cy="-140" r="20" fill="#2e6b3a"/>
          <circle cx="20" cy="-146" r="22" fill="#2e6b3a"/>
          <circle cx="2" cy="-156" r="18" fill="#3f8a4a"/>
        </g>
      </g>
      <g transform="translate(1530 872)">
        <g class="amazon-grow" style="--d:0.9s">
          <path d="M0 0 Q4 -50 -2 -110" fill="none" stroke="#7d6b55" stroke-width="3"/>
          <path d="M-2 -110 Q-24 -122 -40 -100 M-2 -110 Q-20 -132 -38 -128 M-2 -110 Q16 -130 36 -124 M-2 -110 Q22 -118 38 -96 M-2 -110 Q-2 -132 4 -140"
                fill="none" stroke="#4f8f45" stroke-width="4" stroke-linecap="round"/>
        </g>
      </g>
      <g transform="translate(1530 872)">
        <g class="amazon-grow" style="--d:0.2s">
          <circle cx="-62" cy="-14" r="16" fill="#2e6b3a"/>
          <circle cx="-38" cy="-20" r="20" fill="#3f8a4a"/>
          <circle cx="-10" cy="-14" r="16" fill="#2e6b3a"/>
          <circle cx="16" cy="-22" r="22" fill="#3f8a4a"/>
          <circle cx="46" cy="-16" r="18" fill="#2e6b3a"/>
          <circle cx="70" cy="-20" r="20" fill="#3f8a4a"/>
        </g>
      </g>

      <!-- Earthworms rising out of a soil strip along the bottom right.
           rotate(90) turns the worm so its head points up and its tail runs down into the soil. -->
      <g v-for="(x, i) in worms" :key="i" :transform="`translate(${x} 874) rotate(90)`">
        <g class="worm-emerge" :style="{ '--d': `${0.4 + i * 0.35}s` }">
          <path :d="wormA" fill="none" stroke="#e09a9a" stroke-width="13" stroke-linecap="round">
            <animate attributeName="d" :values="`${wormA};${wormB};${wormA}`" dur="1.4s" :begin="`${-i * 0.5}s`"
                     repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
          </path>
          <path :d="wormA" fill="none" stroke="#a85f5f" stroke-width="13" stroke-dasharray="1.5 7" opacity="0.45">
            <animate attributeName="d" :values="`${wormA};${wormB};${wormA}`" dur="1.4s" :begin="`${-i * 0.5}s`"
                     repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
          </path>
          <circle cx="1" cy="2" r="2" fill="#f6c4c4"/>
        </g>
      </g>
      <path d="M880 900 L880 878 Q920 866 980 872 T1100 871 T1220 873 T1340 869 T1460 872 T1600 870 L1600 900 Z" fill="#4a3220"/>
      <circle v-for="(p, k) in pebbles" :key="k" :cx="p[0]" :cy="p[1]" :r="p[2]" fill="#6b4d33"/>
      <ellipse v-for="(x, i) in worms" :key="`hole${i}`" :cx="x" cy="873" rx="10" ry="4" fill="#22170e"/>
    </g>
  </svg>
</template>

<style scoped>
.beaver-peek,
.worm-emerge,
.coral-rise,
.amazon-grow {
  animation-fill-mode: both;
  animation-delay: var(--d, 0s);
}
.beaver-peek { transform: translateX(-170px); }
.worm-emerge { transform: translateX(10px); }
.coral-rise  { transform: translateY(130px); }
.amazon-grow {
  transform: scale(0);
  transform-box: fill-box;
  transform-origin: 50% 100%;
}

.engineers:not(.slidev-vclick-hidden) .beaver-peek {
  animation-name: beaver-peek;
  animation-duration: 1.4s;
  animation-timing-function: cubic-bezier(0.2, 0.7, 0.2, 1);
}
.engineers:not(.slidev-vclick-hidden) .worm-emerge {
  animation-name: worm-emerge;
  animation-duration: 2.4s;
  animation-timing-function: ease-out;
}
.engineers:not(.slidev-vclick-hidden) .amazon-grow {
  animation-name: amazon-grow;
  animation-duration: 1.5s;
  animation-timing-function: cubic-bezier(0.3, 1.3, 0.5, 1);
}
.engineers:not(.slidev-vclick-hidden) .coral-rise {
  animation-name: coral-rise;
  animation-duration: 1.6s;
  animation-timing-function: cubic-bezier(0.2, 0.7, 0.2, 1);
}

.beaver-nose {
  transform-box: fill-box;
  transform-origin: center;
  animation: nose-twitch 1.8s ease-in-out infinite;
}

@keyframes beaver-peek {
  from { transform: translateX(-170px); }
  to   { transform: translateX(0); }
}

@keyframes worm-emerge {
  from { transform: translateX(10px); }
  to   { transform: translateX(-70px); }
}

@keyframes amazon-grow {
  from { transform: scale(0); }
  to   { transform: scale(1); }
}

@keyframes coral-rise {
  from { transform: translateY(130px); }
  to   { transform: translateY(0); }
}

@keyframes nose-twitch {
  0%, 80%, 100% { transform: scale(1); }
  85%           { transform: scale(1.2, 0.85); }
  90%           { transform: scale(0.9, 1.1); }
}
</style>
