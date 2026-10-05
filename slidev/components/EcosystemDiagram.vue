<script setup lang="ts">
import { useId } from 'vue'

// Per-instance marker id (see svg/Mountains.vue for why)
const arrow = `${useId()}-arrow`
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
  </svg>
</template>
