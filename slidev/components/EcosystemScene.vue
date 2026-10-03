<script setup lang="ts">
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'
import DayNightCycle from './svg/DayNightCycle.vue'
import DayNightOverlay from './svg/DayNightOverlay.vue'
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

const props = defineProps<{
  treesGrown?: boolean
}>()

// $page is the static page number of the slide this component lives in (Ref<number>).
// currentPage updates reactively as the user navigates.
const { $page } = useSlideContext()
const { currentPage } = useNav()
const isActive = computed(() => currentPage.value === $page.value)
</script>

<template>
  <svg
    viewBox="0 0 1600 900"
    overflow="visible"
    class="ecosystem-scene"
    :class="{ active: isActive, 'trees-grown': props.treesGrown }"
    aria-label="Animated ecosystem scene"
    style="width:100%;height:100%"
  >
    <!-- Background layers (bottom to top): sky first so mountains/terrain render in front -->
    <DayNightCycle />
    <Mountains />
    <Clouds />

    <!-- Water bodies -->
    <Lake />

    <!-- Fauna sorted by ground-contact y (smaller y = further away = renders first/behind).
         Skunk and Porcupine are foreground walkers so they render after Forest. -->
    <Owl />        <!-- y≈528 perched on branch, furthest back -->
    <Deer />       <!-- y≈720 at lake -->
    <Rabbit />     <!-- y≈750 at burrow (bush built into component) -->
    <Beaver />     <!-- y≈754 near left pond -->
    <Fox />        <!-- y≈810 peeking from behind trees -->

    <!-- Trees (y≈800–890); animals above render behind forest, animals below render in front -->
    <Forest />

    <!-- Foreground walkers in front of forest -->
    <Skunk />      <!-- y≈871 -->
    <Porcupine />  <!-- y≈873 -->

    <!-- Above-canopy elements -->
    <Birds />
    <WeatherEvent />

    <!-- Night veil + animal eyes rendered above terrain/forest so they darken the ground correctly -->
    <DayNightOverlay />

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
