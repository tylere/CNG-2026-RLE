import { ref } from 'vue'

const position = ref<{ x: number } | null>(null)

export function useEcologistPosition() {
  return {
    position,
    save: (x: number) => { position.value = { x } }
  }
}
