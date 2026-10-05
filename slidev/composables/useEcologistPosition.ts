import { ref } from 'vue'

const position = ref<{ lx: number; rx: number } | null>(null)

export function useEcologistPosition() {
  return {
    position,
    save: (lx: number, rx: number) => { position.value = { lx, rx } }
  }
}
