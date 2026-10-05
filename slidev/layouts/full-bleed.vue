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
  /* In-flow flex items grow to fill the canvas. Absolutely positioned
     children are out of flex flow so this rule does not affect them,
     letting them size from their explicit positioning constraints. */
  flex: 1 1 auto;
}
</style>
