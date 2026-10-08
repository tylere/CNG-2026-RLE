<script setup lang="ts">
const props = defineProps<{
  placed?: boolean // already on the tree (later slides); otherwise it's attached at --as-attach-delay
}>()
</script>

<template>
  <!-- Acoustic recorder strapped to the trunk of the large deciduous tree at (337, 814) -->
  <!-- Scaled up and in safety orange so it reads clearly against the trunk and foliage -->
  <g transform="translate(337 768) scale(1.9)">
    <g class="acoustic-sensor" :class="{ placed: props.placed }">
      <rect x="-12" y="-2" width="24" height="4" rx="1" fill="#2a241b"/>
      <rect x="-8" y="-11" width="16" height="22" rx="3" fill="#ff8c1a" stroke="#5a2e00" stroke-width="1.2"/>
      <circle cx="0" cy="-4" r="3.2" fill="#1e1e1e"/>
      <circle cx="0" cy="-4" r="1.5" fill="#666"/>
      <rect x="-5" y="3" width="10" height="1.4" rx="0.7" fill="#5a2e00" opacity="0.6"/>
      <circle class="as-led" cx="4" cy="7.5" r="1.5" fill="#5dff7a"/>
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
