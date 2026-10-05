import { describe, it, expect, beforeEach } from 'vitest'
import { h, type Component } from 'vue'
import { mount } from '@vue/test-utils'
import Mountains from '../components/svg/Mountains.vue'
import DayNightCycle from '../components/svg/DayNightCycle.vue'
import CameraTrap from '../components/svg/CameraTrap.vue'

// Slidev keeps neighbouring slides mounted, so several copies of a scene share one
// document. A url(#id) must resolve to a gradient in its own copy: if it resolves to
// a copy on a hidden slide, Chrome paints nothing (the slide 4/5 ground bug).
function mountTwice(component: Component) {
  return mount({
    render: () => [h('svg', { class: 'copy' }, [h(component)]), h('svg', { class: 'copy' }, [h(component)])]
  }, { attachTo: document.body })
}

describe.each([
  ['Mountains', Mountains],
  ['DayNightCycle', DayNightCycle],
  ['CameraTrap', CameraTrap]
])('%s gradient ids', (_name, component) => {
  beforeEach(() => { document.body.innerHTML = '' })

  it('are unique across copies', () => {
    mountTwice(component)
    const ids = [...document.querySelectorAll('[id]')].map(el => el.id)
    expect(ids.length).toBeGreaterThan(0)
    expect(new Set(ids).size).toBe(ids.length)
  })

  it('resolve every url(#id) within the same copy', () => {
    mountTwice(component)
    for (const copy of document.querySelectorAll('svg.copy')) {
      const refs = [...copy.querySelectorAll('[fill]')]
        .map(el => el.getAttribute('fill')!.match(/^url\(#(.+)\)$/)?.[1])
        .filter((id): id is string => !!id)
      expect(refs.length).toBeGreaterThan(0)
      for (const id of refs) expect(copy.querySelector(`[id="${id}"]`), id).not.toBeNull()
    }
  })
})
