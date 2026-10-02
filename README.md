# CNG-2026-RLE

Presentation for CNG Forum 2026 — "Cloud-Native Geospatial for Country-Scale Ecosystem Risk Assessment"

## Development

```bash
cd slidev
pnpm install
pnpm dev       # start dev server
pnpm build     # build for production (outputs to slidev/dist/)
pnpm test      # run composable tests
```

## Structure

- `slidev/` — Slidev presentation (Vue 3, pnpm)
  - `slides.md` — slide content
  - `components/` — Vue SFC components (SVG primitives + slide composites)
  - `composables/` — shared state (ecologist position bridge)
  - `layouts/` — custom Slidev layouts
- `scripts/` — Python generation scripts
- `scripts/archive/` — archived Quarto source files
- `images/` — static assets referenced by slides
