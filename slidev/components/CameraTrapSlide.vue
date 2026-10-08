<script setup lang="ts">
import { ref, computed, watch, nextTick, onUnmounted } from 'vue'
import { useNav, useSlideContext, onSlideLeave } from '@slidev/client'
import { useEcologistPosition } from '../composables/useEcologistPosition'
import { sceneCycleMs } from '../composables/useSceneClock'
import { useDeerPosition } from '../composables/useDeerPosition'
import Ecologist from './svg/Ecologist.vue'
import CameraTrap from './svg/CameraTrap.vue'
import AcousticSensor from './svg/AcousticSensor.vue'
import Deer from './svg/Deer.vue'

const { position } = useEcologistPosition()
const ecoLStartTx = computed(() => position.value?.lx ?? 0)
const ecoRStartTx = computed(() => position.value?.rx ?? 0)

const { $page, $clicks } = useSlideContext()
const { currentPage } = useNav()

// Click 1: the deer pushes the tripod into the lake (push and fall start at the click)
const pushed = computed(() => $clicks.value >= 1)

// Keep each startled-eye group on its animal's currently visible eyes (follows walking,
// drinking and peeking), and hide it while that animal is out of sight.
const startled = ref<SVGGElement | null>(null)

function effectiveOpacity(el: Element, root: Element) {
  let o = 1
  for (let e: Element | null = el; e && e !== root; e = e.parentElement)
    o *= parseFloat(getComputedStyle(e).opacity)
  return o
}

function insideClip(eye: SVGGraphicsElement, root: SVGSVGElement) {
  const clip = eye.ownerSVGElement // nested <svg> viewport (e.g. the rabbit's bush clip)
  if (!clip || clip === root) return true
  const e = eye.getBoundingClientRect(), c = clip.getBoundingClientRect()
  return e.top >= c.top && e.bottom <= c.bottom && e.left >= c.left && e.right <= c.right
}

// Is the eye actually showing, i.e. not behind a rock, bush or tree? Hit-test its centre and
// skip the night veil, the startled eyes themselves, and anything faded out.
function unobstructed(eye: SVGGraphicsElement, animal: Element, root: SVGSVGElement) {
  const r = eye.getBoundingClientRect()
  for (const el of document.elementsFromPoint(r.left + r.width / 2, r.top + r.height / 2)) {
    if (el === eye || animal.contains(el)) return true
    if (el === root || !root.contains(el)) continue
    if (el.closest('.day-night-overlay, .startled-eyes, .camera-trap')) continue  // thin tripod legs don't hide an eye
    if (effectiveOpacity(el, root) < 0.3) continue
    return false
  }
  return true
}

const lastPose = new WeakMap<Element, SVGCircleElement[]>()
const blocked = new WeakMap<Element, number>()

function trackEyes() {
  const g = startled.value
  const root = g?.ownerSVGElement
  const ctm = root?.getScreenCTM()
  if (!g || !root || !ctm) return
  const inv = ctm.inverse()
  for (const group of g.querySelectorAll<SVGGElement>('.s-eye')) {
    const animal = root.querySelector(group.dataset.animal!)
    const eyes = animal ? [...animal.querySelectorAll<SVGCircleElement>('.eye')] : []
    // Group eyes by pose (peek / night pose / the deer's head) and use the first visible pose
    const poses = new Map<Element, SVGCircleElement[]>()
    for (const eye of eyes) {
      const pose = eye.closest('.peek, .night-pose, .drink') ?? animal!
      poses.set(pose, [...(poses.get(pose) ?? []), eye])
    }
    const shown = (pe: SVGCircleElement[]) => pe.every(eye => effectiveOpacity(eye, root) > 0.3 && insideClip(eye, root))
    let visible = [...poses.values()].find(pe => shown(pe) && pe.every(eye => unobstructed(eye, animal!, root)))
    // Brief occlusions (a leg or branch passing in front) shouldn't make the eyes flicker:
    // keep following the last pose for up to 10 frames while it's still shown.
    const prev = lastPose.get(group)
    if (visible) { lastPose.set(group, visible); blocked.set(group, 0) }
    else if (prev && shown(prev) && (blocked.get(group) ?? 0) < 10) { visible = prev; blocked.set(group, (blocked.get(group) ?? 0) + 1) }
    group.setAttribute('visibility', visible ? 'visible' : 'hidden')
    if (!visible) continue
    group.querySelectorAll('.s-pt').forEach((pt, i) => {
      const eye = visible[Math.min(i, visible.length - 1)]
      const at = new DOMPoint(eye.cx.baseVal.value, eye.cy.baseVal.value)
        .matrixTransform(eye.getScreenCTM()!).matrixTransform(inv)
      pt.setAttribute('transform', `translate(${at.x} ${at.y})`)
    })
  }
}

let rafId = 0
watch(() => currentPage.value === $page.value, (active) => {
  cancelAnimationFrame(rafId)
  if (!active) return
  const loop = () => { trackEyes(); rafId = requestAnimationFrame(loop) }
  rafId = requestAnimationFrame(loop)
}, { immediate: true })
onUnmounted(() => cancelAnimationFrame(rafId))

// Deer starts approaching when dusk begins in the continuous day/night cycle.
// Dusk is at 70% of the 60s cycle (= 42s from cycle start).
// Flash fires 12s later, at the end of the deer's 12s approach.
const deerDelayS = ref(32)

watch(
  () => currentPage.value === $page.value,
  (isActive) => {
    if (!isActive) return
    nextTick(() => {
      const duskMs = 42000 // 70% of 60s = dusk begins
      const nowMs = sceneCycleMs()
      let delayMs = duskMs - nowMs
      if (delayMs < 0) delayMs = 0    // already at/past dusk — start immediately
      if (delayMs > 45000) delayMs = 32000 // dusk too far off — use fallback
      deerDelayS.value = Math.round(delayMs) / 1000
    })
  },
  { immediate: true }
)

// --ct-flash-delay is set on EcosystemScene so both CameraTrap and the startled eyes can read it
const deerDelay = computed(() => `${deerDelayS.value}s`)
const flashDelay = computed(() => `${deerDelayS.value + 12}s`)

// Hand the deer's position to slide 7: fraction of the walk to the camera (translateX 0 → -182px)
const deer = ref<InstanceType<typeof Deer> | null>(null)
const { save: saveDeer } = useDeerPosition()
onSlideLeave(() => {
  const el = deer.value?.$el as Element | undefined
  if (el) saveDeer(new DOMMatrix(getComputedStyle(el).transform).m41 / -182)
})
</script>

<template>
  <!-- --ct-flash-delay cascades from EcosystemScene SVG root to CameraTrap and startled-eyes -->
  <EcosystemScene trees-grown camera-trap no-deer
    :style="{ '--ct-flash-delay': flashDelay }">
    <Ecologist side="left" mode="camera-trap" :style="`--eco-l-start-tx: ${ecoLStartTx}px`" />
    <Ecologist side="right" mode="camera-trap" :style="`--eco-r-start-tx: ${ecoRStartTx}px`" />
    <!-- Deer above the forest but under the night veil, so it darkens at nightfall -->
    <template #under-night>
      <!-- Acoustic sensor attached by the left ecologist at 3.5s -->
      <AcousticSensor />
      <Deer ref="deer" camera-trap :push="pushed" :style="{ '--deer-ct-delay': deerDelay, '--deer-push-delay': '0s' }" />
    </template>
    <CameraTrap :knocked="pushed" />
    <!-- "Automated sensors" label fades in as the tripod grows at ~5s -->
    <text class="ct-label" x="800" y="450" text-anchor="middle"
      font-size="80px" font-weight="700" fill="#F2F4F6" font-family="'iA Writer Quattro S', sans-serif">
      Automated sensors
    </text>
    <!-- Startled eyes: scale 3.5× at flash time, hold 3s, shrink back.
         Drawn above the night veil so they glow; each frame they're moved onto the
         animal's visible eyes (class="eye"), and hidden while the animal is out of sight. -->
    <g ref="startled" class="startled-eyes">
      <g class="s-eye" data-animal=".deer-container" visibility="hidden">
        <g class="s-pt"><g class="s-scale"><circle r="6" fill="#b8ff6a" opacity="0.22"/><circle r="2.4" fill="#b8ff6a"/></g></g>
      </g>
      <g class="s-eye" data-animal=".fox-container" visibility="hidden">
        <g class="s-pt"><g class="s-scale"><circle r="8" fill="#ffd84a" opacity="0.22"/><circle r="3.2" fill="#ffd84a"/></g></g>
        <g class="s-pt"><g class="s-scale"><circle r="8" fill="#ffd84a" opacity="0.22"/><circle r="3.2" fill="#ffd84a"/></g></g>
      </g>
      <g class="s-eye" data-animal=".rabbit-container" visibility="hidden">
        <g class="s-pt"><g class="s-scale"><circle r="7" fill="#ff9a6a" opacity="0.22"/><circle r="2.8" fill="#ff9a6a"/></g></g>
        <g class="s-pt"><g class="s-scale"><circle r="7" fill="#ff9a6a" opacity="0.22"/><circle r="2.8" fill="#ff9a6a"/></g></g>
      </g>
      <g class="s-eye" data-animal=".owl-container" visibility="hidden">
        <g class="s-pt"><g class="s-scale"><circle r="8" fill="#FFD626" opacity="0.22"/><circle r="3.2" fill="#FFD626"/></g></g>
        <g class="s-pt"><g class="s-scale"><circle r="8" fill="#FFD626" opacity="0.22"/><circle r="3.2" fill="#FFD626"/></g></g>
      </g>
    </g>
  </EcosystemScene>
</template>

<style scoped>
.ct-label {
  opacity: 0;
  animation: ct-label-show 6s ease 5s both;
  animation-play-state: var(--play-state, paused);
}

@keyframes ct-label-show {
  0%   { opacity: 0; }
  15%  { opacity: 1; }
  80%  { opacity: 1; }
  100% { opacity: 0; }
}

/* Eyes snap to 3.5× at flash time (--ct-flash-delay inherited from ancestor SVG),
   hold for 3s (60% of 5s), then shrink back to faintly visible.
   Each eye scales about its own centre (.s-scale), so a pair doesn't spread apart. */
.startled-eyes .s-scale {
  transform-box: fill-box;
  transform-origin: center;
  opacity: 0;
  /* forwards, not both: during the delay the eyes must stay hidden, not show the 0% keyframe */
  animation: eye-startle 5s ease-out var(--ct-flash-delay, 44s) forwards;
  animation-play-state: var(--play-state, paused);
}

@keyframes eye-startle {
  0%   { opacity: 1; transform: scale(3.5); }
  60%  { opacity: 0.9; transform: scale(3.5); }
  100% { opacity: 0.2; transform: scale(1); }
}
</style>
