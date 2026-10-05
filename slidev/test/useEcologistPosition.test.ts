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
    save(342, 1180)
    expect(position.value).toEqual({ lx: 342, rx: 1180 })
  })

  it('overwrites a previous position', () => {
    const { position, save } = useEcologistPosition()
    save(100, 900)
    save(250, 1050)
    expect(position.value).toEqual({ lx: 250, rx: 1050 })
  })

  it('returns null when save was never called (skip-navigation case)', () => {
    const { position } = useEcologistPosition()
    expect(position.value).toBeNull()
  })
})
