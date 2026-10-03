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
  <EcosystemScene trees-grown>
    <Ecologist ref="ecoL" side="left" mode="wander" immediate />
    <Ecologist side="right" mode="wander" immediate />
    <text x="800" y="330" text-anchor="middle" font-size="60px" font-weight="700" fill="#F2F4F6" class="a-fade" style="--d:0.9s">How do we observe</text>
    <text x="800" y="430" text-anchor="middle" font-size="120px" font-weight="700" fill="#F2F4F6"><tspan class="a-fade" style="--d:0.1s">Ecosystems</tspan><tspan class="a-fade" style="--d:1.5s">?</tspan></text>
  </EcosystemScene>
</template>
