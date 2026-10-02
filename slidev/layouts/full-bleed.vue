<template>
  <div class="full-bleed-layout">
    <slot />
  </div>
</template>

<style scoped>
.full-bleed-layout {
  position: absolute;
  inset: 0;
  overflow: hidden;
  display: flex;
  align-items: stretch;
}

.full-bleed-layout > :deep(*) {
  width: 100%;
  height: 100%;
}
</style>
