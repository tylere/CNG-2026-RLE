"""Extract Forest.vue tree grow groups from index.qmd SVG source."""
import re

SRC = '/Users/tylere/conductor/workspaces/CNG-2026-RLE/vancouver/index.qmd'
OUT = '/Users/tylere/conductor/workspaces/CNG-2026-RLE/vancouver/slidev/components/svg/Forest.vue'

# Lines in index.qmd to skip (fauna, pond, stones, storm — those go in other components)
# First SVG block is lines 53-388 (1-indexed)
SKIP_CLASSES = {'peek', 'night-pose', 'skunk', 'beaver', 'drink', 'dam-pool', 'storm', 'rain', 'bolt', 'flash'}
SKIP_LINE_RANGES = [(303, 316), (291, 295)]  # deer + stones/pond

def should_skip(line, lineno):
    # Skip fauna and non-forest lines
    for start, end in SKIP_LINE_RANGES:
        if start <= lineno <= end:
            return True
    for cls in SKIP_CLASSES:
        if f'class="{cls}"' in line:
            return True
    return False

with open(SRC) as f:
    all_lines = f.readlines()

# Collect grass paths (lines 95-226, 0-indexed: 94-225)
grass_lines = []
for i in range(94, 226):
    line = all_lines[i].strip()
    if line.startswith('<path ') and 'stroke=' in line:
        grass_lines.append('    ' + line)

# Collect tree grows and struck tree (lines 228-380, 0-indexed: 227-379)
tree_lines = []
for i in range(227, 380):
    lineno = i + 1  # 1-indexed
    line = all_lines[i].strip()
    if should_skip(line, lineno):
        continue
    # Include grow groups, struck tree, and any unlabeled background elements
    # that aren't fauna or storm-related
    has_grow = 'class="grow"' in line
    has_struck = 'class="struck"' in line
    is_fauna_or_storm = any(f'class="{c}"' in line for c in SKIP_CLASSES)
    # Include rocks/stones that are purely static (no class at all or only transform)
    is_static_bg = (not is_fauna_or_storm and
                    '<g transform=' in line and
                    'class=' not in line and
                    lineno not in range(303, 317))
    if has_grow or has_struck or is_static_bg:
        tree_lines.append('    ' + line)

vue_content = '''<template>
  <g class="forest">
''' + '\n'.join(grass_lines) + '''
''' + '\n'.join(tree_lines) + '''
  </g>
</template>

<style scoped>
.grow {
  transform-box: fill-box;
  transform-origin: 50% 100%;
  animation: tree-grow 3s cubic-bezier(0.2, 0.7, 0.3, 1) var(--d, 0s) both;
  animation-play-state: var(--play-state, paused);
}

@keyframes tree-grow {
  from { transform: scale(0.4, 0); }
  to   { transform: scale(1, 1); }
}

.struck {
  transform-box: fill-box;
  transform-origin: 50% 100%;
  animation: struck 45s ease-in 14s infinite both;
  animation-play-state: var(--play-state, paused);
}

@keyframes struck {
  0%, 27%   { opacity: 1; transform: rotate(0deg) scale(1); animation-timing-function: ease-in; }
  31%       { opacity: 1; transform: rotate(86deg) scale(1); }
  70%       { opacity: 1; transform: rotate(86deg) scale(1); }
  76%       { opacity: 0; transform: rotate(86deg) scale(1); }
  77%       { opacity: 0; transform: rotate(0deg) scale(0.02); }
  79%       { opacity: 1; transform: rotate(0deg) scale(0.05); animation-timing-function: cubic-bezier(0.05, 0.75, 0.1, 1); }
  100%      { opacity: 1; transform: rotate(0deg) scale(1); }
}
</style>
'''

with open(OUT, 'w') as f:
    f.write(vue_content)

print(f"Written {len(grass_lines)} grass paths and {len(tree_lines)} tree elements to Forest.vue")
