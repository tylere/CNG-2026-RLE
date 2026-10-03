<template>
  <g class="clouds">
    <g transform="translate(0 250)"><g class="cloud" style="--t:150s; --d:-30s; opacity:0.85"><g transform="scale(0.9)"><ellipse cx="0" cy="0" rx="70" ry="20" fill="#c9d0d8"/><circle cx="-30" cy="-12" r="26" fill="#e3e8ee"/><circle cx="8" cy="-24" r="32" fill="#e3e8ee"/><circle cx="42" cy="-8" r="22" fill="#e3e8ee"/><ellipse cx="0" cy="-4" rx="66" ry="16" fill="#e3e8ee"/></g></g></g>
    <g transform="translate(0 330)"><g class="cloud" style="--t:115s; --d:-80s; opacity:0.85"><g transform="scale(0.65)"><ellipse cx="0" cy="0" rx="70" ry="20" fill="#c9d0d8"/><circle cx="-30" cy="-12" r="26" fill="#e3e8ee"/><circle cx="8" cy="-24" r="32" fill="#e3e8ee"/><circle cx="42" cy="-8" r="22" fill="#e3e8ee"/><ellipse cx="0" cy="-4" rx="66" ry="16" fill="#e3e8ee"/></g></g></g>
    <g transform="translate(0 385)"><g class="cloud" style="--t:175s; --d:-130s; opacity:0.85"><g transform="scale(0.8)"><ellipse cx="0" cy="0" rx="70" ry="20" fill="#c9d0d8"/><circle cx="-30" cy="-12" r="26" fill="#e3e8ee"/><circle cx="8" cy="-24" r="32" fill="#e3e8ee"/><circle cx="42" cy="-8" r="22" fill="#e3e8ee"/><ellipse cx="0" cy="-4" rx="66" ry="16" fill="#e3e8ee"/></g></g></g>
    <g transform="translate(0 290)"><g class="cloud" style="--t:130s; --d:-50s; opacity:0.85"><g transform="scale(0.55)"><ellipse cx="0" cy="0" rx="70" ry="20" fill="#c9d0d8"/><circle cx="-30" cy="-12" r="26" fill="#e3e8ee"/><circle cx="8" cy="-24" r="32" fill="#e3e8ee"/><circle cx="42" cy="-8" r="22" fill="#e3e8ee"/><ellipse cx="0" cy="-4" rx="66" ry="16" fill="#e3e8ee"/></g></g></g>
  </g>
</template>

<style scoped>
.cloud {
  animation: cloud-drift var(--t, 120s) linear var(--d, 0s) infinite both;
  animation-play-state: var(--play-state, paused);
}

@keyframes cloud-drift {
  from { transform: translateX(-250px); }
  to   { transform: translateX(1850px); }
}
</style>
