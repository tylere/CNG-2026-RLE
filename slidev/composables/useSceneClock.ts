// One day/night clock shared by every EcosystemScene.
// Slidev hides inactive slides, which cancels their CSS animations, so each scene's
// day/night cycle would otherwise restart from the beginning whenever its slide is shown.
// Pinning those animations to a shared start time makes each slide continue the sky
// from where the previous ecosystem slide left off.

const CYCLE_MS = 60000
const OFFSET_MS = 18000 // the cycle's animation-delay: -18s (starts at daytime)

// Elements whose animations follow the shared clock (DayNightCycle + DayNightOverlay)
const CLOCK_TARGETS = '.day-night-cycle .sun, .day-night-cycle .daysky, .day-night-cycle .glow, .day-night-cycle .stars, .day-night-overlay .night, .day-night-overlay .eyes'

let epoch: number | null = null

function getEpoch(): number {
  epoch ??= document.timeline.currentTime as number
  return epoch
}

/** Align a scene's day/night animations to the shared clock. Call once the scene is visible. */
export function syncSceneClock(root: Element) {
  const start = getEpoch()
  for (const anim of root.getAnimations({ subtree: true })) {
    const target = (anim.effect as KeyframeEffect | null)?.target
    if (target instanceof Element && target.matches(CLOCK_TARGETS))
      anim.startTime = start
  }
}

/** Current position in the 60s day/night cycle, in ms (0 = midnight, 42000 = dusk begins). */
export function sceneCycleMs(): number {
  const elapsed = (document.timeline.currentTime as number) - getEpoch() + OFFSET_MS
  return ((elapsed % CYCLE_MS) + CYCLE_MS) % CYCLE_MS
}
