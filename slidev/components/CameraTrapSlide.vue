<script setup lang="ts">
import { computed } from 'vue'
import { useEcologistPosition } from '../composables/useEcologistPosition'
import Ecologist from './svg/Ecologist.vue'
import CameraTrap from './svg/CameraTrap.vue'

const { position } = useEcologistPosition()

// Fall back to default entry positions if user skipped the measure slide
const ecoLStartX = computed(() => position.value?.x ?? 360)
</script>

<template>
  <EcosystemScene trees-grown>
    <Ecologist side="left" mode="camera-trap" :initial-x="ecoLStartX" />
    <Ecologist side="right" mode="camera-trap" />
    <CameraTrap />
  </EcosystemScene>
</template>
