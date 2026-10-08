import { ref } from 'vue'

// Fraction of the deer's walk to the camera completed when slide 6 was left (1 = at the camera;
// up to ~1.12 after it pushes the tripod), so slide 7 can start the deer where it was.
// null = slide 6 was never left (start at the lake).
const progress = ref<number | null>(null)

export function useDeerPosition() {
  return {
    progress,
    save: (p: number) => { progress.value = Math.min(1.2, Math.max(0, p)) }
  }
}
