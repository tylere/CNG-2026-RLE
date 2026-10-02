# Slidev Port Design

**Date:** 2026-10-02  
**Author:** Tyler Erickson  
**Status:** Approved

## Overview

Port the CNG Forum 2026 presentation from Quarto/reveal.js to Slidev. The driving goal is a component library of SVG primitives so that individual elements (animals, characters, diagrams) can be modified in one place and composed into multiple slides — supporting an ongoing workflow where AI edits existing SVG elements or adds them to new slides.

**Source:** `index.qmd` (26 slides, 1,695 lines), `custom.scss` (1,260 lines of animation CSS)  
**Target:** `slidev/` subdirectory using Vue SFCs as the SVG animation pattern

## Project Layout

```
slidev/
├── slides.md
├── package.json
├── components/
│   ├── svg/                    # SVG element components — render <g> fragments only
│   │   ├── DayNightCycle.vue   # sun arc, sky color cycle, night veil, eyes
│   │   ├── Clouds.vue          # drifting cloud groups
│   │   ├── Mountains.vue       # background ridgeline + rocks
│   │   ├── Forest.vue          # conifer + deciduous tree groups with grow animation
│   │   ├── Lake.vue            # water body, ripple, flow, stream
│   │   ├── Birds.vue           # flying bird groups (ltr + rtl variants)
│   │   ├── WeatherEvent.vue    # storm cloud, lightning bolt, rain, struck-tree sequence
│   │   ├── Deer.vue            # drinking deer + drink-ripple
│   │   ├── Fox.vue             # peeking fox
│   │   ├── Beaver.vue          # full beaver story: surface → chew → dam
│   │   ├── Skunk.vue           # walking skunk
│   │   ├── Porcupine.vue       # walking porcupine
│   │   ├── Ecologist.vue       # field researcher; side + mode props (see below)
│   │   └── CameraTrap.vue      # tripod, IR LED, flash overlay
│   ├── EcosystemScene.vue      # root <svg> that composes svg/* and exposes a slot
│   ├── MetricsDiagram.vue      # Extent / Rate of decline / Area of occupancy SVG
│   ├── ArchitectureDiagram.vue # workflow diagram SVG
│   ├── FormatsDiagram.vue      # EE ↔ GeoParquet/COG → Lonboard SVG
│   ├── FrictionPile.vue        # chip-drop animation (Python env, cloud auth, etc.)
│   └── SetupCards.vue          # three-card layout: one command / fork / config
├── composables/
│   └── useEcologistPosition.ts # shared state bridge between measure and camera-trap slides
├── styles/
│   └── index.css               # brand tokens, font-faces, utility classes
└── layouts/
    └── full-bleed.vue          # edge-to-edge layout used by SVG slides
```

## Component Architecture

### SVG leaf components (`components/svg/`)

Every component in this directory renders a `<g>` element — never a root `<svg>`. This keeps coordinate space unified: all elements share the 1600×900 viewBox declared once in `EcosystemScene.vue`.

Each component:
- Accepts positional props (`x`, `y`) and variant props
- Owns its SVG markup in `<template>`
- Owns its keyframes and animation rules in `<style scoped>`
- Does **not** know about slide state; it just animates when CSS `--play-state` is `running`

Example interface:

```vue
<!-- Deer.vue -->
<script setup lang="ts">
defineProps<{ x?: number; y?: number; mode?: 'drink' | 'walk' }>()
</script>
<template>
  <g :transform="`translate(${x ?? 0} ${y ?? 0})`" class="deer">
    <!-- extracted SVG paths from index.qmd -->
  </g>
</template>
<style scoped>
.deer .neck { animation: deer-drink 9s infinite; animation-play-state: var(--play-state); }
@keyframes deer-drink { /* ... */ }
</style>
```

### `Ecologist.vue` props

```ts
defineProps<{
  side: 'left' | 'right'
  mode: 'wander' | 'camera-trap'
  initialX?: number          // used by camera-trap mode to continue from saved position
}>()
```

`side` selects the character art and default wander keyframes. `mode` selects the keyframe set: `wander` plays the 120s patrol loop; `camera-trap` plays the 80s directed sequence that ends with the character placing the camera and exiting.

### `EcosystemScene.vue`

Root `<svg viewBox="0 0 1600 900">`. Composes all scene elements. Exposes a default slot for slide-specific extras. Accepts `active` prop to control animation play state.

```vue
<template>
  <svg viewBox="0 0 1600 900" class="ecosystem-scene" :class="{ active }">
    <DayNightCycle />
    <Clouds />
    <Mountains />
    <Forest />
    <Lake />
    <Birds />
    <WeatherEvent />
    <Beaver />
    <Deer :x="420" mode="drink" />
    <Fox :x="680" />
    <Skunk />
    <Porcupine />
    <slot />
  </svg>
</template>
```

Slide-specific extras go in the slot:

```vue
<!-- MeasureEcosystemsSlide.vue -->
<EcosystemScene :active="isActive">
  <Ecologist side="left" mode="wander" />
  <Ecologist side="right" mode="wander" />
</EcosystemScene>
```

## Animation System

### CSS custom property cascade

`EcosystemScene` sets `--play-state` on its root element. Child components read it via `animation-play-state: var(--play-state)`. CSS custom properties inherit through the SVG tree so no prop drilling is needed.

```css
/* EcosystemScene.vue <style scoped> */
.ecosystem-scene        { --play-state: paused; }
.ecosystem-scene.active { --play-state: running; }
```

```css
/* Deer.vue <style scoped> — typical pattern */
.neck {
  animation: deer-drink 9s infinite;
  animation-play-state: var(--play-state);
}
```

### Active state detection

Each slide component that wraps `EcosystemScene` computes `isActive` via Slidev's composables:

```ts
import { useSlideContext } from '@slidev/client'
import { useNav } from '@slidev/client'
import { computed } from 'vue'

const { $page } = useSlideContext()
const nav = useNav()
const isActive = computed(() => nav.currentPage.value === $page)
```

### Looping vs. reveal animations

**Ecosystem scene animations** keep their negative `animation-delay` values from the original CSS. They do not reset to frame zero on slide re-entry — they continue mid-cycle. This is intentional: the scene is ambient, not a one-shot animation.

**Fragment reveals** on non-ecosystem slides (text rising in, diagrams drawing on) use Slidev's native `v-click` directive. The custom `.a-rise` and `.a-fade` classes from `custom.scss` are preserved as utility classes in `styles/index.css` for any cases where CSS-only is cleaner.

## State Bridge: Ecologist Position

The current presentation has a JavaScript hack that reads `getComputedStyle` from the ecologist DOM element when leaving `slide-measure-ecosystems` and injects the x-offset as a CSS custom property into `slide-camera-trap`, so the camera-trap animation starts from wherever the ecologists had wandered to.

Replaced with a module-level ref:

```ts
// composables/useEcologistPosition.ts
import { ref } from 'vue'

const position = ref<{ x: number } | null>(null)

export function useEcologistPosition() {
  return {
    position,
    save: (x: number) => { position.value = { x } },
  }
}
```

`MeasureEcosystemsSlide.vue` calls `save(x)` in its Slidev `onSlideLeave` hook, reading the reactive position tracked by `Ecologist.vue` (which `defineExpose`s a `currentX: Ref<number>` representing the current translation offset), not via DOM queries. `CameraTrapSlide.vue` reads `position.value` in `onSlideEnter` and passes it as `initialX` to `Ecologist`.

## SVG Migration Strategy

The Python scripts (`gen_ecosystem_scene.py`, `add_measure_slide.py`, `rebuild_camera_trap_slide.py`) generated the SVG that is currently inline in `index.qmd`. The migration treats that rendered output as the source of truth — the scripts are not re-run during the port.

Steps:
1. Extract the full inline SVG from `index.qmd` (the `#slide-ecosystems` block).
2. Identify logical `<g>` groups by their CSS classes and spatial role.
3. Move each group's markup into the corresponding Vue SFC `<template>`.
4. Pull the matching keyframes and rules from `custom.scss` into each SFC's `<style scoped>`.
5. Replace `animation-play-state: running` (or no explicit value) with `animation-play-state: var(--play-state)` on every animation property.
6. Archive the Python scripts to `scripts/archive/`; future geometry changes go directly into Vue SFC templates.

The 1600×900 coordinate space is preserved exactly. No geometry changes occur during the port.

## Non-Ecosystem Slides

The remaining 23 slides are ported as Markdown in `slides.md` with inline HTML where needed. The five slides with standalone SVG diagrams (`#slide-metrics`, `#slide-no-server`, `#slide-architecture`, `#slide-formats`, `#slide-setup`) become Vue components in `components/` following the same scoped-CSS pattern. The two iframe slides (`#slide-wildlife-insights`, `#slide-demo`) use Slidev's built-in iframe support.

## Build and CI

- Package manager: `pnpm` (per project convention)
- Slidev outputs to `slidev/dist/`; GitHub Actions updated to build from `slidev/` and deploy `slidev/dist/` to GitHub Pages
- Existing `images/` directory referenced via relative path from `slidev/`
- Font CDN URLs preserved from `custom.scss`

## Out of Scope

- Rewriting the Python SVG generators as Vue components (geometry is ported as static markup)
- Changing visual design, colors, or typography
- Changing slide content or narrative
