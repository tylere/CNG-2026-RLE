<script setup lang="ts">
const props = defineProps<{
  placed?: boolean // already on the tree (later slides); otherwise it's attached at --as-attach-delay
}>()
</script>

<template>
  <!-- Acoustic recorder strapped to the trunk of the large deciduous tree at (337, 814) -->
  <g transform="translate(337 772)">
    <g class="acoustic-sensor" :class="{ placed: props.placed }">
      <rect x="-11" y="-2" width="22" height="4" rx="1" fill="#3a3528"/>
      <rect x="-8" y="-11" width="16" height="22" rx="3" fill="#4f6b3a" stroke="#2c3a22" stroke-width="1.2"/>
      <circle cx="0" cy="-4" r="3" fill="#1e1e1e"/>
      <circle cx="0" cy="-4" r="1.4" fill="#555"/>
      <circle class="as-led" cx="4" cy="6" r="1.4" fill="#5dff7a"/>
    </g>
  </g>
</template>

<style scoped>
.acoustic-sensor {
  transform-box: fill-box;
  transform-origin: center;
  animation: as-attach 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) var(--as-attach-delay, 3.5s) both;
  animation-play-state: var(--play-state, paused);
}
.acoustic-sensor.placed { animation: none; }

.as-led {
  animation: as-led 3s ease-in-out 1s infinite both;
  animation-play-state: var(--play-state, paused);
}

@keyframes as-attach {
  from { opacity: 0; transform: scale(0.4); }
  to   { opacity: 1; transform: scale(1); }
}

@keyframes as-led {
  0%, 90%, 100% { opacity: 0.15; }
  94%           { opacity: 1; }
}
</style>
