<script setup lang="ts">
import { ref } from 'vue'
import { onSlideLeave } from '@slidev/client'
import { useEcologistPosition } from '../composables/useEcologistPosition'
import Ecologist from './svg/Ecologist.vue'

const { save } = useEcologistPosition()
const ecoL = ref<InstanceType<typeof Ecologist> | null>(null)

onSlideLeave(() => {
  if (ecoL.value?.el) {
    const matrix = new DOMMatrix(getComputedStyle(ecoL.value.el).transform)
    save(matrix.m41)
  }
})
</script>

<template>
  <EcosystemScene>
    <Ecologist ref="ecoL" side="left" mode="wander" />
    <Ecologist side="right" mode="wander" />
    <text x="800" y="38" text-anchor="middle" font-size="60" font-weight="700" class="a-fade" style="--d:0.9s">How do we measure</text>
    <text x="800" y="140" text-anchor="middle" font-size="120" font-weight="700" class="a-fade" style="--d:0.1s">Ecosystems</text>
    <text x="1185" y="140" text-anchor="start" font-size="120" font-weight="700" fill="#FFD626" class="a-fade" style="--d:1.5s">?</text>
  </EcosystemScene>
</template>
