<script setup lang="ts">
import { ref, computed, watch, nextTick } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'
import { useEcologistPosition } from '../composables/useEcologistPosition'
import Ecologist from './svg/Ecologist.vue'
import CameraTrap from './svg/CameraTrap.vue'
import Deer from './svg/Deer.vue'

const { position } = useEcologistPosition()
const ecoLStartTx = computed(() => position.value?.lx ?? 0)
const ecoRStartTx = computed(() => position.value?.rx ?? 0)

const { $page } = useSlideContext()
const { currentPage } = useNav()

// Deer starts approaching when dusk begins in the continuous day/night cycle.
// Dusk is at 70% of the 60s cycle (= 42s from cycle start).
// Flash fires 12s later, at the end of the deer's 12s approach.
const deerDelayS = ref(32)

watch(
  () => currentPage.value === $page.value,
  (isActive) => {
    if (!isActive) return
    nextTick(() => {
      // Any .daysky element works — all share the same continuous clock.
      const el = document.querySelector('.daysky')
      if (!el) return
      const anim = el.getAnimations()[0]
      if (!anim || anim.currentTime == null) return
      const cycleMs = 60000
      const duskMs = 42000 // 70% of 60s = dusk begins
      const nowMs = ((anim.currentTime % cycleMs) + cycleMs) % cycleMs
      let delayMs = duskMs - nowMs
      if (delayMs < 0) delayMs = 0    // already at/past dusk — start immediately
      if (delayMs > 45000) delayMs = 32000 // dusk too far off — use fallback
      deerDelayS.value = Math.round(delayMs) / 1000
    })
  },
  { immediate: true }
)

// --ct-flash-delay is set on EcosystemScene so both CameraTrap and the startled eyes can read it
const deerDelay = computed(() => `${deerDelayS.value}s`)
const flashDelay = computed(() => `${deerDelayS.value + 12}s`)
</script>

<template>
  <!-- --ct-flash-delay cascades from EcosystemScene SVG root to CameraTrap and startled-eyes -->
  <EcosystemScene trees-grown camera-trap no-deer
    :style="{ '--ct-flash-delay': flashDelay }">
    <Ecologist side="left" mode="camera-trap" :style="`--eco-l-start-tx: ${ecoLStartTx}px`" />
    <Ecologist side="right" mode="camera-trap" :style="`--eco-r-start-tx: ${ecoRStartTx}px`" />
    <!-- Deer rendered in slot so it appears above the forest in z-order -->
    <Deer camera-trap :style="{ '--deer-ct-delay': deerDelay }" />
    <CameraTrap />
    <!-- "Camera Trap" label fades in as the tripod grows at ~15s -->
    <text class="ct-label" x="800" y="450" text-anchor="middle"
      font-size="80px" font-weight="700" fill="#F2F4F6" font-family="'iA Writer Quattro S', sans-serif">
      Camera Trap
    </text>
    <!-- Startled eyes: scale 3.5× at flash time, hold 3s, shrink back -->
    <g class="startled-eyes">
      <!-- Deer eye at foreground position (original 1095.7,636.4 shifted −182px X +80px Y) -->
      <g class="s-eye">
        <circle cx="914" cy="716" r="6" fill="#b8ff6a" opacity="0.22"/>
        <circle cx="914" cy="716" r="2.4" fill="#b8ff6a"/>
      </g>
      <!-- Animal pair in forest behind original deer position -->
      <g class="s-eye">
        <circle cx="1097" cy="778" r="8" fill="#ffd84a" opacity="0.22"/>
        <circle cx="1097" cy="778" r="3.2" fill="#ffd84a"/>
        <circle cx="1118" cy="778" r="8" fill="#ffd84a" opacity="0.22"/>
        <circle cx="1118" cy="778" r="3.2" fill="#ffd84a"/>
      </g>
      <!-- Fox pair on the left -->
      <g class="s-eye">
        <circle cx="503" cy="732" r="7" fill="#ff9a6a" opacity="0.22"/>
        <circle cx="503" cy="732" r="2.8" fill="#ff9a6a"/>
        <circle cx="515" cy="732" r="7" fill="#ff9a6a" opacity="0.22"/>
        <circle cx="515" cy="732" r="2.8" fill="#ff9a6a"/>
      </g>
      <!-- Owl pair high in the canopy -->
      <g class="s-eye">
        <circle cx="1329" cy="493" r="8" fill="#FFD626" opacity="0.22"/>
        <circle cx="1329" cy="493" r="3.2" fill="#FFD626"/>
        <circle cx="1341" cy="493" r="8" fill="#FFD626" opacity="0.22"/>
        <circle cx="1341" cy="493" r="3.2" fill="#FFD626"/>
      </g>
    </g>
  </EcosystemScene>
</template>

<style scoped>
.ct-label {
  opacity: 0;
  animation: ct-label-show 6s ease 15s both;
  animation-play-state: var(--play-state, paused);
}

@keyframes ct-label-show {
  0%   { opacity: 0; }
  15%  { opacity: 1; }
  80%  { opacity: 1; }
  100% { opacity: 0; }
}

/* Eyes snap to 3.5× at flash time (--ct-flash-delay inherited from ancestor SVG),
   hold for 3s (60% of 5s), then shrink back to faintly visible */
.startled-eyes .s-eye {
  transform-box: fill-box;
  transform-origin: center;
  opacity: 0;
  /* forwards, not both: during the delay the eyes must stay hidden, not show the 0% keyframe */
  animation: eye-startle 5s ease-out var(--ct-flash-delay, 44s) forwards;
  animation-play-state: var(--play-state, paused);
}

@keyframes eye-startle {
  0%   { opacity: 1; transform: scale(3.5); }
  60%  { opacity: 0.9; transform: scale(3.5); }
  100% { opacity: 0.2; transform: scale(1); }
}
</style>
