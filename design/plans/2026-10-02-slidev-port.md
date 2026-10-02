# Slidev Port Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the CNG Forum 2026 presentation from Quarto/reveal.js to Slidev, with a Vue SFC component library of SVG primitives so any element can be modified once and reused across slides.

**Architecture:** A `slidev/` subdirectory contains the full Slidev project. SVG leaf components in `components/svg/` render `<g>` fragments composed by `EcosystemScene.vue` into a root `<svg>`. Animations are controlled by a `--play-state` CSS custom property that cascades through the SVG tree, toggled by the parent slide detecting its own active state via Slidev's `useNav()`.

**Tech Stack:** Slidev 0.49+, Vue 3, TypeScript, pnpm, Vitest (composable only)

**Spec:** `design/specs/2026-10-02-slidev-port-design.md`

## Global Constraints

- Canvas: `canvasWidth: 1600`, `aspectRatio: 16/9` — all SVG coordinates stay at 1600×900
- Color scheme: dark — `colorSchema: dark` in global frontmatter
- Brand background: `#1D232B`, text: `#F2F4F6`, accent yellow: `#FFD626`, accent blue: `#418BD9`
- Fonts: `iA Writer Quattro S` (sans) and `Berkeley Mono` (mono) loaded from `https://assets.radiant.earth/fonts/`
- Package manager: pnpm throughout — never npm or yarn
- All Vue components: `<script setup lang="ts">` syntax
- All SVG leaf components (`components/svg/*.vue`) render `<g>` elements only — no root `<svg>`
- No geometry changes — SVG coordinates copied verbatim from `index.qmd`
- Images referenced as `../images/` from within `slidev/` — Vite configured to allow parent dir
- Verify Slidev composable API (`useSlideContext`, `useNav`) against current docs at **sli.dev** before use — Slidev minor versions may have changed APIs since this plan was written

## Review Focus

- **`--play-state` inheritance through deeply-nested SVG**: Beaver story and camera-trap flash involve `<g>` elements nested 5+ levels deep inside components rendered inside `EcosystemScene`. Verify that `animation-play-state: var(--play-state, paused)` actually pauses animations when the scene is not active, not just the first level. Test: navigate away from the ecosystem slide; confirm no animation jank in the inactive slide stack. → **Task 6**, step "visual verify paused state".
- **Ecologist position bridge when slide is skipped**: If a user jumps directly to the camera-trap slide without visiting `slide-measure-ecosystems`, `position.value` is `null`. `CameraTrap.vue` must fall back to a default `initialX`. → **Task 3**, add test: `save()` never called → `position.value` is `null`; document the expected fallback value. **Task 7**, `Ecologist.vue`: `initialX` prop must default to the camera-trap-appropriate start position.
- **Animation restart on slide re-entry**: All ecosystem scene animations use negative `animation-delay` values to start mid-cycle — they should *not* restart from frame 0 on re-entry. Verify: navigate away and back; the scene should feel continuous. If `EcosystemScene` is unmounted/remounted by Slidev (not just hidden), animations will restart. Test: check Slidev's rendering behavior (keep-alive vs. unmount) in Task 6.
- **iframes in non-focused slides**: The wildlife-insights and demo slides use `layout: iframe`. Verify the iframe doesn't keep loading/reloading as you navigate past it. → **Task 10**, step "verify iframe behavior".
- **Slide count for backup slides**: The three backup slides should not count toward the total. Slidev's `hideInToc: true` hides from the table of contents but may not suppress the slide counter. Verify the presentation shows the expected slide count (not 26). → **Task 10**, note the slide-count display after adding backup slides.

---

## File Map

**Create:**
```
slidev/package.json
slidev/vite.config.ts
slidev/tsconfig.json
slidev/vitest.config.ts
slidev/slides.md
slidev/styles/index.css
slidev/layouts/full-bleed.vue
slidev/composables/useEcologistPosition.ts
slidev/test/useEcologistPosition.test.ts
slidev/components/svg/DayNightCycle.vue
slidev/components/svg/Clouds.vue
slidev/components/svg/Mountains.vue
slidev/components/svg/Forest.vue
slidev/components/svg/Lake.vue
slidev/components/svg/Birds.vue
slidev/components/svg/WeatherEvent.vue
slidev/components/svg/Deer.vue
slidev/components/svg/Fox.vue
slidev/components/svg/Beaver.vue
slidev/components/svg/Skunk.vue
slidev/components/svg/Porcupine.vue
slidev/components/svg/Ecologist.vue
slidev/components/svg/CameraTrap.vue
slidev/components/EcosystemScene.vue
slidev/components/MetricsDiagram.vue
slidev/components/ArchitectureDiagram.vue
slidev/components/FormatsDiagram.vue
slidev/components/FrictionPile.vue
slidev/components/SetupCards.vue
```

**Modify:**
```
.github/workflows/publish.yml   — update build step
```

**Archive (git mv, not delete):**
```
index.qmd        → scripts/archive/index.qmd
custom.scss      → scripts/archive/custom.scss
_quarto.yml      → scripts/archive/_quarto.yml
pyproject.toml   → scripts/archive/pyproject.toml
```

---

## Task 1: Scaffold Slidev project

**Files:**
- Create: `slidev/package.json`
- Create: `slidev/vite.config.ts`
- Create: `slidev/tsconfig.json`
- Create: `slidev/vitest.config.ts`
- Create: `slidev/slides.md` (title slide only for now)

- [ ] **Step 1: Create `slidev/package.json`**

```json
{
  "name": "cng-2026-rle",
  "private": true,
  "scripts": {
    "dev": "slidev --open",
    "build": "slidev build --base /",
    "export": "slidev export",
    "type-check": "vue-tsc --noEmit",
    "test": "vitest run"
  },
  "dependencies": {
    "@slidev/cli": "^0.49.0",
    "@slidev/theme-default": "^0.23.0",
    "vue": "^3.4.0"
  },
  "devDependencies": {
    "typescript": "^5.4.0",
    "vitest": "^1.6.0",
    "vue-tsc": "^2.0.0",
    "jsdom": "^24.0.0",
    "@vue/test-utils": "^2.4.0"
  }
}
```

- [ ] **Step 2: Create `slidev/vite.config.ts`**

This allows Vite to serve `../images/` (the project-root images directory) without the browser blocking cross-directory file access.

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    fs: {
      allow: ['..', '.']
    }
  }
})
```

- [ ] **Step 3: Create `slidev/tsconfig.json`**

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "jsx": "preserve",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "lib": ["ESNext", "DOM"],
    "baseUrl": "."
  },
  "include": [
    "slides.md",
    "components/**/*.ts",
    "components/**/*.vue",
    "composables/**/*.ts",
    "layouts/**/*.vue"
  ]
}
```

- [ ] **Step 4: Create `slidev/vitest.config.ts`**

```ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'jsdom'
  }
})
```

- [ ] **Step 5: Create `slidev/slides.md` with title slide only**

```md
---
theme: default
title: Cloud-Native Geospatial for Country-Scale Ecosystem Risk Assessment
author: Tyler Erickson
colorSchema: dark
canvasWidth: 1600
aspectRatio: 16/9
transition: fade
css: styles/index.css
background: ../images/hero_forest_coast.jpg
class: title-slide
---

# Cloud-Native Geospatial for Country-Scale Ecosystem Risk Assessment

CNG Forum 2026 · Cloud-Native Geo in Practice

Tyler Erickson
```

- [ ] **Step 6: Install dependencies and verify dev server starts**

```bash
cd slidev && pnpm install
pnpm dev
```

Expected: Slidev dev server opens at `http://localhost:3030` showing the title slide with the hero forest background image. If the image does not load, verify the `vite.config.ts` `fs.allow` setting.

- [ ] **Step 7: Commit**

```bash
git add slidev/
git commit -m "feat: scaffold Slidev project with title slide"
```

---

## Task 2: Brand styles and full-bleed layout

**Files:**
- Create: `slidev/styles/index.css`
- Create: `slidev/layouts/full-bleed.vue`

- [ ] **Step 1: Create `slidev/styles/index.css`**

Port brand tokens, font-faces, and utility classes from `custom.scss`. Replace all `.reveal` selectors with plain selectors (Slidev does not use a `.reveal` wrapper). The `.present` → `.slidev-page--current` mapping is NOT done here — animation gating is handled by the `--play-state` pattern and `v-click` in components, not by CSS selectors.

```css
/* Font faces — loaded from Radiant Earth CDN */
@font-face {
  font-family: 'iA Writer Quattro S';
  src: url('https://assets.radiant.earth/fonts/iAWriterQuattroS-Regular.woff2') format('woff2');
  font-weight: 400; font-style: normal; font-display: swap;
}
@font-face {
  font-family: 'iA Writer Quattro S';
  src: url('https://assets.radiant.earth/fonts/iAWriterQuattroS-Italic.woff2') format('woff2');
  font-weight: 400; font-style: italic; font-display: swap;
}
@font-face {
  font-family: 'iA Writer Quattro S';
  src: url('https://assets.radiant.earth/fonts/iAWriterQuattroS-Bold.woff2') format('woff2');
  font-weight: 700; font-style: normal; font-display: swap;
}
@font-face {
  font-family: 'iA Writer Quattro S';
  src: url('https://assets.radiant.earth/fonts/iAWriterQuattroS-BoldItalic.woff2') format('woff2');
  font-weight: 700; font-style: italic; font-display: swap;
}
@font-face {
  font-family: 'Berkeley Mono';
  src: url('https://assets.radiant.earth/fonts/BerkeleyMono-Regular.woff2') format('woff2');
  font-weight: 400; font-style: normal; font-display: swap;
}
@font-face {
  font-family: 'Berkeley Mono';
  src: url('https://assets.radiant.earth/fonts/BerkeleyMono-Oblique.woff2') format('woff2');
  font-weight: 400; font-style: italic; font-display: swap;
}
@font-face {
  font-family: 'Berkeley Mono';
  src: url('https://assets.radiant.earth/fonts/BerkeleyMono-Bold.woff2') format('woff2');
  font-weight: 700; font-style: normal; font-display: swap;
}
@font-face {
  font-family: 'Berkeley Mono';
  src: url('https://assets.radiant.earth/fonts/BerkeleyMono-Bold-Oblique.woff2') format('woff2');
  font-weight: 700; font-style: italic; font-display: swap;
}

/* Base */
:root {
  --color-bg: #1D232B;
  --color-text: #F2F4F6;
  --color-yellow: #FFD626;
  --color-blue: #418BD9;
}

.slidev-layout { font-family: 'iA Writer Quattro S', sans-serif; color: #F2F4F6; }
.slidev-layout h1, .slidev-layout h2, .slidev-layout h3 {
  color: #F2F4F6;
  font-family: 'iA Writer Quattro S', sans-serif;
  font-weight: 700;
  letter-spacing: 0.01em;
}
a { color: #F2F4F6; text-decoration: underline; text-decoration-color: rgba(33,38,247,0.9); text-decoration-thickness: 2px; text-underline-offset: 3px; }
a:hover { text-decoration-color: #FFD626; }
code, pre, .mono { font-family: 'Berkeley Mono', ui-monospace, monospace; }
:not(pre) > code { background: rgba(242,244,246,0.1); color: inherit; border-radius: 4px; padding: 0.1em 0.35em; }

/* Utility classes */
.big-number { font-size: 7rem; color: #FFD626; font-weight: 700; line-height: 1; display: block; text-align: center; }
.center-v { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; gap: 1rem; }
.muted { color: rgba(242,244,246,0.5) !important; font-size: 0.85em; }
.yellow { color: #FFD626; }
.eyebrow { font-family: 'Berkeley Mono', ui-monospace, monospace; font-size: 0.62em; font-weight: 400; letter-spacing: 0.18em; text-transform: uppercase; color: #FFD626; }
.hl { color: #FFD626; }
.formula { font-size: 3.5rem; color: #F2F4F6; text-align: center; line-height: 1.3; }
.formula .highlight { color: #FFD626; font-weight: 700; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; }
.statement { display: block; margin: 0; color: #F2F4F6; font-size: 1.9em; font-weight: 700; line-height: 1.1; letter-spacing: -0.02em; }
.statement.hl { color: #FFD626; }
.statement-sub { display: block; margin: 0; font-size: 1.1em; font-weight: 700; line-height: 1.2; }
.headline { display: block; margin: 0; color: #F2F4F6; font-size: 1.15em; font-weight: 700; line-height: 1.15; }
.slide-top { position: absolute; top: 40px; left: 0; right: 0; text-align: center; }
.faint { opacity: 0.18; }
.shadow { box-shadow: 0 8px 40px rgba(0,0,0,0.5); }
.left-v { display: flex; flex-direction: column; justify-content: center; }
.centered { text-align: center; }
.avatar img { border-radius: 50%; border: 4px solid rgba(242,244,246,0.15); }
.deep-shade { background: rgba(0,0,0,0.5); }
.deep-copy { color: rgba(242,244,246,0.7); font-size: 0.8em; }

/* Browser-chrome frame */
.frame { border-radius: 8px 8px 4px 4px; overflow: hidden; box-shadow: 0 8px 40px rgba(0,0,0,0.6); }
.frame::before { content: ''; display: block; height: 28px; background: #3a3f4b radial-gradient(circle at 16px 14px, #ff5f57 0 6px, transparent 6px) no-repeat, radial-gradient(circle at 36px 14px, #febc2e 0 6px, transparent 6px) no-repeat, radial-gradient(circle at 56px 14px, #28c840 0 6px, transparent 6px) no-repeat; background-size: auto; }

/* Book covers */
.covers { display: flex; gap: 3rem; align-items: center; justify-content: center; }
.tilt-l { transform: rotate(-4deg); }
.tilt-r { transform: rotate(4deg); }

/* Stats block */
.stats .num { font-size: 4rem; font-weight: 700; color: #FFD626; line-height: 1; }
.stats .unit { font-size: 1.1rem; color: rgba(242,244,246,0.7); }

/* Timed reveals — use with style="--d:Xs" */
.a-fade { opacity: 0; animation: fade-in 0.8s ease-out var(--d, 0s) both; }
.a-rise { opacity: 0; animation: rise-in 0.8s cubic-bezier(0.2,0.7,0.2,1) var(--d, 0s) both; }

@keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }
@keyframes rise-in { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: none; } }

/* Ken Burns on hero photo */
.title-slide { animation: kenburns 20s ease-out both; }
@keyframes kenburns { from { transform: scale(1); } to { transform: scale(1.12); } }

/* SVG draw-on: element needs pathLength="1", stroke-dasharray="1", stroke-dashoffset="1" */
.draw { animation: draw-1 0.7s ease-out var(--d, 0s) both; }
@keyframes draw-1 { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
```

- [ ] **Step 2: Create `slidev/layouts/full-bleed.vue`**

This layout removes all padding so a full-screen SVG scene can fill the slide edge-to-edge.

```vue
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
```

- [ ] **Step 3: Verify in dev server**

Run `pnpm dev` from `slidev/`. Confirm the title slide uses the correct fonts and colors. Check the network panel — both font CDN requests should return 200.

- [ ] **Step 4: Commit**

```bash
git add slidev/styles/ slidev/layouts/
git commit -m "feat: add brand styles and full-bleed layout"
```

---

## Task 3: `useEcologistPosition` composable

**Files:**
- Create: `slidev/composables/useEcologistPosition.ts`
- Create: `slidev/test/useEcologistPosition.test.ts`

- [ ] **Step 1: Write the failing tests**

```ts
// slidev/test/useEcologistPosition.test.ts
import { describe, it, expect, beforeEach } from 'vitest'
import { useEcologistPosition } from '../composables/useEcologistPosition'

describe('useEcologistPosition', () => {
  beforeEach(() => {
    const { position } = useEcologistPosition()
    position.value = null
  })

  it('starts as null', () => {
    const { position } = useEcologistPosition()
    expect(position.value).toBeNull()
  })

  it('saves and retrieves a position', () => {
    const { position, save } = useEcologistPosition()
    save(342)
    expect(position.value).toEqual({ x: 342 })
  })

  it('overwrites a previous position', () => {
    const { position, save } = useEcologistPosition()
    save(100)
    save(250)
    expect(position.value).toEqual({ x: 250 })
  })

  it('returns null when save was never called (skip-navigation case)', () => {
    const { position } = useEcologistPosition()
    // position.value was reset to null in beforeEach — verify null is returned
    expect(position.value).toBeNull()
  })
})
```

- [ ] **Step 2: Run tests and confirm failure**

```bash
cd slidev && pnpm test
```

Expected: 4 failing tests with "Cannot find module '../composables/useEcologistPosition'".

- [ ] **Step 3: Implement the composable**

```ts
// slidev/composables/useEcologistPosition.ts
import { ref } from 'vue'

const position = ref<{ x: number } | null>(null)

export function useEcologistPosition() {
  return {
    position,
    save: (x: number) => { position.value = { x } }
  }
}
```

Note: `position` is module-level so it survives across slide navigation within a session. This is intentional — the camera-trap slide reads the position that was saved when leaving the measure-ecosystems slide.

- [ ] **Step 4: Run tests and confirm passing**

```bash
pnpm test
```

Expected: 4 passing tests.

- [ ] **Step 5: Type-check**

```bash
pnpm type-check
```

Expected: no errors.

- [ ] **Step 6: Commit**

```bash
git add slidev/composables/ slidev/test/
git commit -m "feat: add useEcologistPosition composable with tests"
```

---

## Task 4: Scene background SVG components

These five components cover the static and ambient background of the ecosystem scene. Each follows the same pattern:
1. Copy the relevant SVG group(s) verbatim from `index.qmd` (`#slide-ecosystems` block, lines ~53–716)
2. Wrap in `<g>` (never `<svg>`) in the Vue `<template>`
3. Extract the matching keyframes and rules from `custom.scss` into `<style scoped>`
4. Replace every `animation:` shorthand to add an explicit `animation-play-state: var(--play-state, paused)` declaration

**Files:**
- Create: `slidev/components/svg/Mountains.vue`
- Create: `slidev/components/svg/DayNightCycle.vue`
- Create: `slidev/components/svg/Clouds.vue`
- Create: `slidev/components/svg/Forest.vue`
- Create: `slidev/components/svg/Lake.vue`

### SVG class → component mapping

| Component | Elements to extract from `index.qmd` (identify by CSS class or role) |
|-----------|----------------------------------------------------------------------|
| `Mountains.vue` | Mountain ridgeline `<polygon fill="#404a55">`, rock highlight `<polygon fill="#8b9197">` (×7), ground wave `<path fill="#284031">`, ground fill `<rect fill="url(#side-ground)">`, and the `<defs>` containing `side-ground`, `side-sun`, `side-water` linearGradients |
| `DayNightCycle.vue` | `<rect class="daysky">`, `.glow.dawn` ellipse, `.glow.dusk` ellipse, `.sun` group, `.night` rect, all `.eyes` groups (including `.late`), all `.night-pose` groups (owl etc.) |
| `Clouds.vue` | All `<g transform="translate(0 Ypx)"><g class="cloud" …>` groups |
| `Forest.vue` | All `<g transform="translate(…)"><g class="grow" …>` tree groups (both conifer `<polygon>` and deciduous `<circle>` variants) |
| `Lake.vue` | Stream `<polygon>`, stream `<polyline class="flow">`, ripple `<ellipse class="ripple">` elements, fish group, splash elements |

### CSS rules → component mapping

Extract these rule blocks from `custom.scss` and place in each component's `<style scoped>`:

| Component | CSS classes to extract |
|-----------|----------------------|
| `Mountains.vue` | None (static) |
| `DayNightCycle.vue` | `.daysky` (keyframes `day-sky`), `.glow.dawn/.dusk`, `.sun` (keyframes `sun-arc`), `.night`, `.eyes`, `.blink`, `.night-pose`, `.late` |
| `Clouds.vue` | `.cloud` (keyframes `cloud-drift`) |
| `Forest.vue` | `.grow` (keyframes `tree-grow`) |
| `Lake.vue` | `.flow` (keyframes `flow-march`), `.ripple` (keyframes `ripple-out`), `.fish`, `.splash` |

- [ ] **Step 1: Create `slidev/components/svg/Mountains.vue`**

Open `index.qmd`. The ecosystem SVG starts at `## {#slide-ecosystems}`. Find the `<defs>` block and the mountain/ground elements (they appear in the first ~50 lines of the SVG, before the clouds). Copy them verbatim.

```vue
<template>
  <g class="mountains">
    <!-- PASTE: <defs> block with side-ground, side-sun, side-water, side-glow gradients -->
    <!-- PASTE: mountain ridgeline <polygon fill="#404a55"> -->
    <!-- PASTE: 7× rock highlight <polygon fill="#8b9197"> -->
    <!-- PASTE: ground wave <path fill="#284031"> -->
    <!-- PASTE: ground fill <rect fill="url(#side-ground)"> -->
  </g>
</template>

<style scoped>
/* Mountains are static — no animation rules needed */
</style>
```

- [ ] **Step 2: Create `slidev/components/svg/DayNightCycle.vue`**

```vue
<template>
  <g class="day-night">
    <!-- PASTE: <rect class="daysky" …> -->
    <!-- PASTE: <ellipse class="glow dawn" …> -->
    <!-- PASTE: <ellipse class="glow dusk" …> -->
    <!-- PASTE: <g class="sun"> … </g> -->
    <!-- PASTE: <rect class="night" …> -->
    <!-- PASTE: all <g class="eyes"> groups -->
    <!-- PASTE: all <g class="eyes late"> groups (owl etc.) -->
    <!-- PASTE: any .night-pose groups -->
  </g>
</template>

<style scoped>
/* PASTE: .daysky keyframes (day-sky) and animation rule from custom.scss */
/* PASTE: .sun keyframes (sun-arc) and animation rule */
/* PASTE: .glow.dawn, .glow.dusk opacity rules */
/* PASTE: .night opacity animation */
/* PASTE: .eyes visibility rules (only visible when .night is showing) */
/* PASTE: .blink keyframes and rule */
/* PASTE: .late timing delay */

/* After pasting, add animation-play-state to every animated element: */
/* Example: */
.daysky {
  /* (pasted animation: day-sky 60s …) */
  animation-play-state: var(--play-state, paused);
}
/* Repeat for .sun, .night, .blink, etc. */
</style>
```

- [ ] **Step 3: Create `slidev/components/svg/Clouds.vue`**

```vue
<template>
  <g class="clouds">
    <!-- PASTE: all <g transform="translate(0 Ypx)"><g class="cloud" …> groups -->
  </g>
</template>

<style scoped>
/* PASTE: .cloud keyframes (cloud-drift) and animation rule */
.cloud { animation-play-state: var(--play-state, paused); }
</style>
```

- [ ] **Step 4: Create `slidev/components/svg/Forest.vue`**

```vue
<template>
  <g class="forest">
    <!-- PASTE: all <g transform="translate(…)"><g class="grow" …> tree groups -->
    <!-- There are roughly 40–60 trees; include all of them -->
  </g>
</template>

<style scoped>
/* PASTE: .grow keyframes (tree-grow) and animation rule */
.grow { animation-play-state: var(--play-state, paused); }
</style>
```

- [ ] **Step 5: Create `slidev/components/svg/Lake.vue`**

```vue
<template>
  <g class="lake">
    <!-- PASTE: stream polygon (the angular blue polygon near coordinates 339,546) -->
    <!-- PASTE: <polyline class="flow" …> (the stream highlight path) -->
    <!-- PASTE: all <ellipse class="ripple" …> elements -->
    <!-- PASTE: fish group and splash elements if present -->
  </g>
</template>

<style scoped>
/* PASTE: .flow keyframes and animation rule */
/* PASTE: .ripple keyframes and animation rule */
/* PASTE: .fish and .splash rules if present */
.flow, .ripple { animation-play-state: var(--play-state, paused); }
</style>
```

- [ ] **Step 6: Type-check**

```bash
cd slidev && pnpm type-check
```

Expected: no errors (these components have no TypeScript, but `vue-tsc` checks template syntax).

- [ ] **Step 7: Commit**

```bash
git add slidev/components/svg/Mountains.vue slidev/components/svg/DayNightCycle.vue slidev/components/svg/Clouds.vue slidev/components/svg/Forest.vue slidev/components/svg/Lake.vue
git commit -m "feat: add background SVG components (mountains, sky, clouds, forest, lake)"
```

---

## Task 5: Scene fauna SVG components

Same extraction pattern as Task 4. All animation rules get `animation-play-state: var(--play-state, paused)` added.

**Files:**
- Create: `slidev/components/svg/Birds.vue`
- Create: `slidev/components/svg/WeatherEvent.vue`
- Create: `slidev/components/svg/Deer.vue`
- Create: `slidev/components/svg/Fox.vue`
- Create: `slidev/components/svg/Beaver.vue`
- Create: `slidev/components/svg/Skunk.vue`
- Create: `slidev/components/svg/Porcupine.vue`

### SVG class → component mapping

| Component | Elements to extract |
|-----------|-------------------|
| `Birds.vue` | All `<g class="bird-fly …">` groups (4 birds, identified by `--d`, `--t`, `--y` inline styles) |
| `WeatherEvent.vue` | `.storm` cloud, `.bolt` lightning, `.flash` white-flash rect, `.struck` fallen tree, all `.rain` elements |
| `Deer.vue` | The drinking deer group (elements with `.drink` and `.drink-ripple` classes, located near the lake area) |
| `Fox.vue` | The `.peek` group (fox peeking from behind cover) |
| `Beaver.vue` | The `.beaver` group, `.log-fall`, `.log-move`, `.chips`, `.dam`, `.dam-pool`, `.beaver-head` elements |
| `Skunk.vue` | `<g transform="translate(-260.0 870.0)"><g class="skunk" …>` (search for `--sx:2120` in the SVG) |
| `Porcupine.vue` | Similar `.porcupine` group (search for `class="porcupine"`) |

### CSS rules → component mapping

| Component | CSS classes to extract from `custom.scss` |
|-----------|------------------------------------------|
| `Birds.vue` | `.bird-fly`, `.bird-fly.rtl`, `.bob`, `.flap`, `.bird` path style |
| `WeatherEvent.vue` | `.storm`, `.bolt`, `.flash`, `.struck`, `.rain` + keyframes |
| `Deer.vue` | `.drink`, `.drink-ripple` + keyframes |
| `Fox.vue` | `.peek` (keyframes `peek-hide`) |
| `Beaver.vue` | `.beaver`, `.log-fall`, `.log-move`, `.chips`, `.dam`, `.dam-pool`, `.beaver-head` (keyframes `chew`), `.chip` (hop) |
| `Skunk.vue` | `.skunk` (keyframes `skunk-walk`), `.leg-a`, `.leg-b` |
| `Porcupine.vue` | `.porcupine`, `.leg-a`, `.leg-b` |

- [ ] **Step 1–7: Create each component following the pattern from Task 4**

For each component:
1. Copy SVG markup from `index.qmd` (find by class name)
2. Wrap in `<g class="[component-name]">`
3. Paste matching CSS from `custom.scss` into `<style scoped>`
4. Add `animation-play-state: var(--play-state, paused)` to every animated element

Minimal template pattern (same for all):

```vue
<template>
  <g class="birds">
    <!-- PASTE SVG markup here -->
  </g>
</template>

<style scoped>
/* PASTE CSS from custom.scss here */
/* Add animation-play-state: var(--play-state, paused) to all animated elements */
</style>
```

- [ ] **Step 8: Type-check**

```bash
cd slidev && pnpm type-check
```

- [ ] **Step 9: Commit**

```bash
git add slidev/components/svg/
git commit -m "feat: add fauna SVG components (birds, weather, deer, fox, beaver, skunk, porcupine)"
```

---

## Task 6: `EcosystemScene.vue`

**Files:**
- Create: `slidev/components/EcosystemScene.vue`

`EcosystemScene.vue` is the root `<svg>` that assembles all scene components and controls animation play state. It also detects whether its containing slide is currently active.

- [ ] **Step 1: Create `slidev/components/EcosystemScene.vue`**

```vue
<script setup lang="ts">
import { computed } from 'vue'
import { useNav } from '@slidev/client'
import { useSlideContext } from '@slidev/client'
import DayNightCycle from './svg/DayNightCycle.vue'
import Clouds from './svg/Clouds.vue'
import Mountains from './svg/Mountains.vue'
import Forest from './svg/Forest.vue'
import Lake from './svg/Lake.vue'
import Birds from './svg/Birds.vue'
import WeatherEvent from './svg/WeatherEvent.vue'
import Deer from './svg/Deer.vue'
import Fox from './svg/Fox.vue'
import Beaver from './svg/Beaver.vue'
import Skunk from './svg/Skunk.vue'
import Porcupine from './svg/Porcupine.vue'

// Detect if the slide containing this component is the current slide.
// $page is the static page number of the slide this component lives in.
// currentPage is reactive and updates as the user navigates.
const { $page } = useSlideContext()
const { currentPage } = useNav()
const isActive = computed(() => currentPage.value === $page)
</script>

<template>
  <svg
    viewBox="0 0 1600 900"
    class="ecosystem-scene"
    :class="{ active: isActive }"
    aria-label="Animated ecosystem scene"
    style="width:100%;height:100%"
  >
    <Mountains />
    <DayNightCycle />
    <Clouds />
    <Forest />
    <Lake />
    <Birds />
    <WeatherEvent />
    <Deer />
    <Fox />
    <Beaver />
    <Skunk />
    <Porcupine />
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
```

- [ ] **Step 2: Add a test slide in `slides.md` and visually verify**

Temporarily append to `slides.md`:

```md
---
layout: full-bleed
---

<EcosystemScene />
```

Run `pnpm dev`. Navigate to that slide. Confirm:
- All scene elements render (mountains, trees, sky, animals, water)
- Animations play when the slide is active
- Navigate away and back — the scene resumes mid-cycle (animations do not restart from frame 0)

**Visual verify paused state**: While on a different slide, open DevTools and inspect the `.ecosystem-scene` SVG. Its `--play-state` should read `paused`. Animated elements should not be advancing.

If Slidev unmounts/remounts components on navigation (rather than show/hide), animations will restart on re-entry. If this happens, investigate Slidev's `keepAlive` option or wrap with `<KeepAlive>` in the layout.

- [ ] **Step 3: Type-check**

```bash
cd slidev && pnpm type-check
```

- [ ] **Step 4: Commit (remove test slide from slides.md first)**

```bash
git add slidev/components/EcosystemScene.vue slidev/slides.md
git commit -m "feat: add EcosystemScene composer with --play-state animation control"
```

---

## Task 7: Character SVG components

**Files:**
- Create: `slidev/components/svg/Ecologist.vue`
- Create: `slidev/components/svg/CameraTrap.vue`

### `Ecologist.vue`

The ecologist comes in two flavors (`side: 'left' | 'right'`) and two animation modes (`mode: 'wander' | 'camera-trap'`). It also exposes `currentX` for the position bridge.

The SVG markup for both characters is in `index.qmd`, in the `#slide-measure-ecosystems` SVG block (lines ~726–812). The left ecologist (`eco-l`) has a clipboard; the right (`eco-r`) holds a camera. The right character has a `scale(-1 1)` flip on its wrapper.

The camera-trap mode uses different keyframe names (`eco-l-ct-sequence`, `eco-r-ct-sequence`) found in `custom.scss`.

- [ ] **Step 1: Create `slidev/components/svg/Ecologist.vue`**

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps<{
  side: 'left' | 'right'
  mode: 'wander' | 'camera-trap'
  initialX?: number   // camera-trap mode: start x from saved position; defaults to side-appropriate entry
}>()

const startX = computed(() =>
  props.initialX ?? (props.side === 'left' ? 360 : 1240)
)

// Expose the element ref so the slide can read the computed CSS transform on leave.
// Do NOT try to track position via a reactive ref — the CSS animation drives the
// actual position; getComputedStyle(el).transform is the authoritative source.
const groupRef = ref<SVGGElement | null>(null)
defineExpose({ el: groupRef })
</script>

<template>
  <!-- Left ecologist: clipboard and pencil -->
  <g
    v-if="side === 'left'"
    ref="groupRef"
    :transform="`translate(${startX} 870)`"
    :class="['ecologist', 'eco-l', mode === 'camera-trap' ? 'eco-l-ct' : '']"
  >
    <!-- PASTE: left ecologist SVG from index.qmd lines ~728–768 (the eco-l group contents) -->
  </g>

  <!-- Right ecologist: camera; note the scale(-1 1) flip is on the outer wrapper -->
  <g
    v-if="side === 'right'"
    ref="groupRef"
    :transform="`translate(${startX} 868) scale(-1 1)`"
    :class="['ecologist', 'eco-r', mode === 'camera-trap' ? 'eco-r-ct' : '']"
  >
    <!-- PASTE: right ecologist SVG from index.qmd lines ~771–811 (the eco-r group contents) -->
  </g>
</template>

<style scoped>
/* PASTE from custom.scss: */
/* .ecologist.eco-l → eco-l-wander keyframes (120s patrol) */
/* .ecologist.eco-r → eco-r-wander keyframes (120s patrol) */
/* .ecologist.eco-l-ct → eco-l-ct-sequence keyframes (80s camera-trap sequence) */
/* .ecologist.eco-r-ct → eco-r-ct-sequence keyframes (80s camera-trap sequence) */
/* .eco-write → pencil oscillation */
/* .leg-a, .leg-b → leg swing */

/* Add animation-play-state to all animated sub-elements */
.ecologist, .ecologist * {
  animation-play-state: var(--play-state, paused);
}
</style>
```

**Position bridge design:** The CSS wander animation drives the ecologist's actual on-screen position — not any Vue reactive state. To capture the mid-animation x offset, `MeasureEcosystemsSlide` reads `getComputedStyle(ecoL.value.el).transform` in `onSlideLeave`, parses it as a `DOMMatrix`, and extracts `m41` (the translateX component). This is identical to the technique used in the original `index.qmd` JavaScript bridge. The `el` ref is the SVG `<g>` element exposed by `Ecologist.vue`.

### `CameraTrap.vue`

- [ ] **Step 2: Create `slidev/components/svg/CameraTrap.vue`**

The camera trap SVG is in `#slide-camera-trap` in `index.qmd` (after `## {#slide-camera-trap}`). Look for `.ct-tripod`, `.ct-status-led`, `.ct-ir-led`, `.ct-flash`, `.ct-ir-flash` elements.

```vue
<template>
  <g class="camera-trap">
    <!-- PASTE: ct-tripod group -->
    <!-- PASTE: ct-status-led element -->
    <!-- PASTE: ct-ir-led element -->
    <!-- PASTE: ct-flash glow element -->
    <!-- PASTE: ct-ir-flash glow element -->
  </g>
</template>

<style scoped>
/* PASTE from custom.scss: */
/* .ct-tripod → ct-tripod-appear keyframes */
/* .ct-status-led → blink rule */
/* .ct-ir-led → ct-ir-led pulse */
/* .ct-flash → ct-flash-fire keyframes */
/* .ct-ir-flash → simultaneous IR glow */

.camera-trap, .camera-trap * {
  animation-play-state: var(--play-state, paused);
}
</style>
```

- [ ] **Step 3: Type-check**

```bash
cd slidev && pnpm type-check
```

- [ ] **Step 4: Commit**

```bash
git add slidev/components/svg/Ecologist.vue slidev/components/svg/CameraTrap.vue
git commit -m "feat: add Ecologist and CameraTrap SVG components"
```

---

## Task 8: Ecosystem slides in `slides.md`

Add the three ecosystem slides. Each uses `EcosystemScene` with slide-specific slot content and wires up the position bridge.

**Files:**
- Modify: `slidev/slides.md`

Also create the two slide-level wrapper components (needed for lifecycle hooks):

- Create: `slidev/components/MeasureEcosystemsSlide.vue`
- Create: `slidev/components/CameraTrapSlide.vue`

- [ ] **Step 1: Create `slidev/components/MeasureEcosystemsSlide.vue`**

```vue
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
    save(matrix.m41)   // m41 = translateX component
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
```

- [ ] **Step 2: Create `slidev/components/CameraTrapSlide.vue`**

```vue
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
  <EcosystemScene>
    <Ecologist side="left" mode="camera-trap" :initial-x="ecoLStartX" />
    <Ecologist side="right" mode="camera-trap" />
    <CameraTrap />
  </EcosystemScene>
</template>
```

- [ ] **Step 3: Add ecosystem slides to `slides.md`**

After the title slide, append:

```md

---
id: slide-ecosystems
layout: full-bleed
---

<EcosystemScene />

---
id: slide-measure-ecosystems
layout: full-bleed
---

<MeasureEcosystemsSlide />

---
id: slide-camera-trap
layout: full-bleed
---

<CameraTrapSlide />
```

- [ ] **Step 4: Visually verify all three ecosystem slides**

Run `pnpm dev`. Check:
- Slide 2: ecosystem scene plays (trees grow, animals move, day/night cycles)
- Slide 3: same scene plus two ecologists wandering; heading "How do we measure Ecosystems?" fades in
- Slide 4: camera-trap sequence plays; deer walks to camera; flash fires
- Navigate from slide 3 → 4: the left ecologist's starting position on slide 4 should approximately match where they were when you left slide 3

- [ ] **Step 5: Commit**

```bash
git add slidev/components/MeasureEcosystemsSlide.vue slidev/components/CameraTrapSlide.vue slidev/slides.md
git commit -m "feat: add three ecosystem slides with position bridge"
```

---

## Task 9: Diagram components

Five components for slides with standalone SVG diagrams. Each follows the same pattern: extract the SVG from `index.qmd`, wrap in a Vue SFC, port animation CSS.

**Files:**
- Create: `slidev/components/MetricsDiagram.vue`
- Create: `slidev/components/ArchitectureDiagram.vue`
- Create: `slidev/components/FormatsDiagram.vue`
- Create: `slidev/components/FrictionPile.vue`
- Create: `slidev/components/SetupCards.vue`

### Extraction targets

| Component | Slide in `index.qmd` | What to extract |
|-----------|---------------------|----------------|
| `MetricsDiagram.vue` | `#slide-metrics` | SVG diagram: Extent blob, Rate-of-decline drawn line (`.draw` class), Area-of-occupancy grid + blob; fragment class triggers → convert to `v-click` |
| `ArchitectureDiagram.vue` | `#slide-architecture` | SVG workflow diagram nodes and edges |
| `FormatsDiagram.vue` | `#slide-formats` | Earth Engine ↔ GeoParquet/COG → Lonboard SVG |
| `FrictionPile.vue` | `#slide-friction` | Chip-drop pile: extract `.pile .chip` elements; CSS `chip-drop` keyframes; add `--play-state` |
| `SetupCards.vue` | `#slide-setup` | Three-card HTML layout: "One command" / "Fork a template" / "Config not code" — this is HTML, not SVG; port as a Vue template with the three-column grid |

### Animation notes

- **`MetricsDiagram.vue`**: The `.draw` class uses `pathLength="1"` + `stroke-dashoffset` to animate paths drawing on. Fragment reveals in reveal.js become `v-click` in Slidev:
  ```html
  <path v-click class="draw" … />
  ```
  Each `v-click` shows the element on the next presenter click.

- **`FrictionPile.vue`**: The chip-drop uses `chip-drop` keyframes with a `cubic-bezier(0.3, 1.4, 0.5, 1)` bounce. Apply `--play-state` so chips only animate when the slide is active. The chips appear sequentially in the original via increasing `animation-delay` values — keep these; they'll play automatically when the slide goes active.

- [ ] **Step 1–5: Create each component**

Follow the Task 4 extraction pattern. For each:
1. Find the slide in `index.qmd`
2. Extract the SVG or HTML
3. Place in Vue `<template>`
4. Port CSS to `<style scoped>`
5. Add `animation-play-state: var(--play-state, paused)` where needed

`FrictionPile.vue` needs to detect active state (same as `EcosystemScene`). Add:

```vue
<script setup lang="ts">
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'
const { $page } = useSlideContext()
const { currentPage } = useNav()
const isActive = computed(() => currentPage.value === $page)
</script>

<template>
  <div class="friction-pile" :class="{ active: isActive }">
    <!-- chip pile markup -->
  </div>
</template>

<style scoped>
.friction-pile { --play-state: paused; }
.friction-pile.active { --play-state: running; }
/* PASTE: .pile, .chip, chip-drop keyframes */
</style>
```

- [ ] **Step 6: Type-check**

```bash
cd slidev && pnpm type-check
```

- [ ] **Step 7: Commit**

```bash
git add slidev/components/
git commit -m "feat: add diagram components (metrics, architecture, formats, friction, setup)"
```

---

## Task 10: All remaining slides in `slides.md`

Port the remaining 22 slides. Most are HTML/Markdown. Two use iframe layouts.

**Files:**
- Modify: `slidev/slides.md`

The `.a-rise` and `.a-fade` utility classes defined in `styles/index.css` animate on mount. In Slidev, components are not remounted on every navigation by default. To make these replay on re-entry, wrap each animated slide's content in a `<div :key="String($page) + String(currentPage)">`… but this causes a re-mount flash. The simpler acceptable tradeoff: these animations play once when first visited. If full replay is needed, convert individual elements to `v-click`.

- [ ] **Step 1: Append all remaining slides to `slides.md`**

Add each slide in order after the existing slides. Use the following patterns:

**Speaker slide (`#slide-speaker`):**
```md
---
id: slide-speaker
---

<div class="absolute" style="left:180px;top:230px">
  <div class="a-rise avatar">
    <img src="../images/speaker.png" width="420" alt="Tyler Erickson" />
  </div>
</div>
<div class="absolute" style="left:720px;top:270px;width:800px">
  <div class="statement a-rise" style="--d:0.2s">Tyler Erickson</div>
  <div class="statement-sub a-rise" style="--d:0.4s"><span class="hl">VorGeo</span> · Founder</div>
  <div class="statement-sub a-rise" style="--d:0.6s"><span class="hl">Radiant Earth</span> · CTO</div>
  <div class="a-fade" style="--d:1s">
    <a href="https://www.linkedin.com/in/tylere" class="mono">linkedin.com/in/tylere</a><br>
    <a href="https://github.com/tylere" class="mono">github.com/tylere</a><br>
    <a href="https://www.analyze.earth" class="mono">analyze.earth</a>
  </div>
</div>
```

**Wildlife Insights iframe slide (`#slide-wildlife-insights`):**
```md
---
id: slide-wildlife-insights
layout: iframe
url: https://www.wildlifeinsights.org
---
```

**Demo iframe slide (`#slide-demo`):**
```md
---
id: slide-demo
layout: iframe
url: https://tylere.github.io/rle-tyler-colombia/
---
```

**Question slide (`#slide-question`):**
```md
---
id: slide-question
---

<img src="../images/colombia_ecosystems.png" class="faint" style="position:absolute;right:-50px;top:-60px;width:800px" />
<div class="center-v">
  <div class="statement">How at risk are a country's ecosystems?</div>
</div>
```

**RLE slide (`#slide-rle`):**
```md
---
id: slide-rle
---

<div class="two-col">
  <div>
    <div class="eyebrow">IUCN Red List of Ecosystems</div>
    <h2>A standardized framework for assessing ecosystem risk</h2>
    <img src="../images/iucn_guidelines_cover.png" style="width:300px" class="shadow" />
  </div>
  <div v-click>
    <img src="../images/get_hierarchy.png" style="width:560px" />
  </div>
</div>
```

**Covers slide (`#slide-covers`):**
```md
---
id: slide-covers
---

<div class="center-v">
  <div class="covers">
    <img src="../images/colombia_2017_cover.jpg" class="tilt-l shadow" style="width:380px" />
    <img src="../images/myanmar_2020_cover.jpg" class="tilt-r shadow" style="width:380px" />
  </div>
</div>
```

**Patchwork slide (`#slide-patchwork`):**
```md
---
id: slide-patchwork
---

<div class="center-v">
  <div class="statement">A patchwork of tools and ad hoc scripts</div>
  <div class="statement-sub muted">hard to share · reproduce · maintain</div>
</div>
```

**Metrics slide (`#slide-metrics`):**
```md
---
id: slide-metrics
---

<MetricsDiagram />
```

**Colombia slide (`#slide-colombia`):**
```md
---
id: slide-colombia
---

<div class="two-col">
  <div>
    <img src="../images/colombia_ecosystems.png" style="width:680px" />
  </div>
  <div class="stats">
    <div><span class="num">460,350</span><span class="unit">polygons</span></div>
    <div><span class="num">87</span><span class="unit">ecosystem types</span></div>
    <div><span class="num">1.7 GB</span><span class="unit">GeoParquet</span></div>
  </div>
</div>
```

**Goal slide (`#slide-goal`):**
```md
---
id: slide-goal
---

<div class="center-v">
  <div class="statement">An open-source, cloud-native assessment workflow</div>
</div>
```

**No-server slide (`#slide-no-server`):**
```md
---
id: slide-no-server
---

<div class="center-v">
  <ArchitectureDiagram variant="no-server" />
  <div class="statement-sub">No geospatial server required</div>
</div>
```

*(Note: if `ArchitectureDiagram` does not support a `variant` prop, inline the SVG directly in this slide instead of adding the prop.)*

**Architecture slide (`#slide-architecture`):**
```md
---
id: slide-architecture
---

<ArchitectureDiagram />
```

**Formats slide (`#slide-formats`):**
```md
---
id: slide-formats
---

<FormatsDiagram />
<div style="position:absolute;bottom:60px;left:0;right:0;text-align:center" class="muted">Static hosting · GitHub Pages</div>
```

**Doc-as-code slide (`#slide-doc-as-code`):**
```md
---
id: slide-doc-as-code
---

<div class="two-col">
  <div>
    <div class="eyebrow">Document as code</div>
    <h2>This page is a notebook</h2>
    <div class="statement-sub muted">code · narrative · maps</div>
  </div>
  <div>
    <div class="frame">
      <img src="../images/demo/criterion_b.png" style="width:100%" />
    </div>
  </div>
</div>
```

**Backup slides (uncounted):**

Slidev does not have a built-in "uncounted" slide feature. Use `hideInToc: true` to hide from the TOC. Verify whether this also suppresses the page counter — if not, add a note for the presenter.

```md
---
id: slide-backup-home
hideInToc: true
---

<img src="../images/demo/home.png" style="width:100%;height:100%;object-fit:contain" />

---
id: slide-backup-assessment
hideInToc: true
---

<div class="two-col">
  <img src="../images/demo/assessment.png" style="width:100%" />
  <img src="../images/demo/criterion_b.png" style="width:100%" />
</div>

---
id: slide-backup-map
hideInToc: true
---

<div class="center-v muted">Interactive Lonboard map — screenshot pending</div>
```

**Hard-part slide (`#slide-hard-part`):**
```md
---
id: slide-hard-part
---

<div class="center-v">
  <div class="statement">The hard part wasn't the geospatial computation.<br>It was setup.</div>
</div>
```

**Friction slide (`#slide-friction`):**
```md
---
id: slide-friction
---

<FrictionPile />
```

**Setup slide (`#slide-setup`):**
```md
---
id: slide-setup
---

<SetupCards />
```

**Falls-short slide (`#slide-falls-short`):**
```md
---
id: slide-falls-short
---

<div class="eyebrow">Lessons learned</div>
<ul>
  <li v-click>Source data behind logins</li>
  <li v-click>Cloud auth still a wall</li>
  <li v-click>GeoParquet row group sizing</li>
  <li v-click>CI retries</li>
</ul>
```

**Takeaways slide (`#slide-takeaways`):**
```md
---
id: slide-takeaways
---

<div class="eyebrow">Takeaways</div>
<ul>
  <li v-click>Cloud-native formats make maps static</li>
  <li v-click>Doc-as-code makes science reproducible</li>
  <li v-click>For non-engineers, setup <em>is</em> the product</li>
</ul>
```

**Thanks slide (`#slide-thanks`):**
```md
---
id: slide-thanks
background: ../images/hero_forest_coast.jpg
class: title-slide
---

<div class="center-v">
  <h2>Thank you</h2>
  <div class="a-fade" style="--d:0.5s">
    <a href="https://iucnrle.org" class="mono">iucnrle.org</a><br>
    <a href="https://github.com/rle-assessment" class="mono">github.com/rle-assessment</a><br>
    <a href="https://tylere.github.io/rle-tyler-colombia" class="mono">tylere.github.io/rle-tyler-colombia</a>
  </div>
</div>
```

- [ ] **Step 2: Verify iframe behavior**

Navigate to both iframe slides (wildlife-insights, demo). Confirm:
- The iframe loads correctly
- Navigating away from and back to the iframe does not cause duplicate loading requests in the network panel

- [ ] **Step 3: Verify slide count**

Check that the total slide count shown by Slidev matches expectations. The three backup slides (`hideInToc: true`) may or may not be excluded from the count depending on Slidev version.

- [ ] **Step 4: Type-check**

```bash
cd slidev && pnpm type-check
```

- [ ] **Step 5: Full presentation walkthrough**

Navigate all slides in order. Check for layout issues, missing images, or broken component references.

- [ ] **Step 6: Commit**

```bash
git add slidev/slides.md
git commit -m "feat: port all 26 slides to slides.md"
```

---

## Task 11: CI update and Quarto archive

**Files:**
- Modify: `.github/workflows/publish.yml`
- Archive: `index.qmd`, `custom.scss`, `_quarto.yml`, `pyproject.toml`

- [ ] **Step 1: Read the current `publish.yml`**

Open `.github/workflows/publish.yml` and identify the build and deploy steps.

- [ ] **Step 2: Update the build step**

Replace the Quarto render step with Slidev build. The new workflow should:
1. `cd slidev && pnpm install`
2. `pnpm build`
3. Deploy `slidev/dist/` to GitHub Pages (replacing the previous `docs/` output)

Exact YAML depends on the existing workflow structure — update in-place.

- [ ] **Step 3: Archive Quarto source files**

```bash
git mv index.qmd scripts/archive/index.qmd
git mv custom.scss scripts/archive/custom.scss
git mv _quarto.yml scripts/archive/_quarto.yml
git mv pyproject.toml scripts/archive/pyproject.toml
```

- [ ] **Step 4: Update `.gitignore`**

Remove `/docs/` from `.gitignore` (it was the Quarto output directory; Slidev outputs to `slidev/dist/` which is already covered by the Slidev `.gitignore`).

Add `slidev/dist/` if not already gitignored.

- [ ] **Step 5: Update `README.md`**

Update any references to Quarto commands (`quarto render`, `quarto preview`) to Slidev equivalents (`pnpm dev`, `pnpm build` from within `slidev/`).

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/publish.yml scripts/archive/ .gitignore README.md
git commit -m "chore: update CI for Slidev build, archive Quarto source"
```

---

## Execution Handoff

All 11 tasks produce independently reviewable commits. Tasks 4–5 (SVG extraction) are the most mechanical and benefit from careful visual verification. Tasks 6 and 8 are the highest-risk (animation timing, position bridge) and worth a focused review.
