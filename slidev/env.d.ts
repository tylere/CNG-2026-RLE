/// <reference types="vite/client" />

// Type shim for @slidev/client — the actual package uses virtual Vite modules
// that are only resolvable at runtime. This shim declares the API surface we use.
declare module '@slidev/client' {
  import type { ComputedRef, Ref } from 'vue'

  export function useNav(): {
    currentPage: ComputedRef<number>
    currentSlideNo: ComputedRef<number>
    total: ComputedRef<number>
    hasPrev: ComputedRef<boolean>
    hasNext: ComputedRef<boolean>
    next(): Promise<void>
    prev(): Promise<void>
    go(page: number): Promise<void>
  }

  export function useSlideContext(): {
    $page: Ref<number>
    $clicks: Ref<number>
    $renderContext: Ref<string>
    $frontmatter: Record<string, unknown>
  }

  export function onSlideLeave(callback: () => void): void
  export function onSlideEnter(callback: () => void): void
}
