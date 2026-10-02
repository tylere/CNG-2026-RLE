<script setup lang="ts">
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'
import DayNightCycle from './svg/DayNightCycle.vue'
import Clouds from './svg/Clouds.vue'
import Mountains from './svg/Mountains.vue'
import Forest from './svg/Forest.vue'
import Lake from './svg/Lake.vue'
import Birds from './svg/Birds.vue'
import WeatherEvent from './svg/WeatherEvent.vue'
import Deer from './svg/Deer.vue'
import Fox from './svg/Fox.vue'
import Rabbit from './svg/Rabbit.vue'
import Owl from './svg/Owl.vue'
import Beaver from './svg/Beaver.vue'
import Skunk from './svg/Skunk.vue'
import Porcupine from './svg/Porcupine.vue'

// $page is the static page number of the slide this component lives in (Ref<number>).
// currentPage updates reactively as the user navigates.
const { $page } = useSlideContext()
const { currentPage } = useNav()
const isActive = computed(() => currentPage.value === $page.value)
</script>

<template>
  <svg
    viewBox="-320 -260 1920 1160"
    class="ecosystem-scene"
    :class="{ active: isActive }"
    aria-label="Animated ecosystem scene"
    style="width:100%;height:100%"
  >
    <!-- Background layers (bottom to top) -->
    <Mountains />
    <DayNightCycle />
    <Clouds />

    <!-- Mid: left beaver pond before trees -->
    <Lake />

    <!-- Trees -->
    <Forest />

    <!-- Fauna above trees -->
    <Deer />
    <Beaver />

    <!-- Central pond above trees (z-order: after trees so it overlays correctly) -->
    <!-- Lake's .central-pond group is already inside Lake.vue; EcosystemScene
         delegates z-order to component ordering above -->

    <Birds />
    <WeatherEvent />

    <!-- Peeking animals -->
    <Fox />
    <Rabbit />
    <Owl />

    <!-- Walkers cross the front -->
    <Skunk />
    <Porcupine />

    <!-- Slot for slide-specific overlays (ecologist, camera trap, text) -->
    <slot />
  </svg>
</template>

<style scoped>
.ecosystem-scene {
  --play-state: paused;
  display: block;
  background: #1D232B;
}

.ecosystem-scene.active {
  --play-state: running;
}
</style>
