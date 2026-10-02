"""Insert the 'How do we measure Ecosystems' slide after the Ecosystems slide."""

import re

with open("index.qmd", "r") as f:
    content = f.read()

# Find the ecosystem slide SVG block
# It starts with the ```{=html} block and ends with ``` before the ::: {.notes}
# The slide starts at ## {#slide-ecosystems} and ends just before ## {#slide-question}

eco_start = content.index("## {#slide-ecosystems}")
eco_end = content.index("## {#slide-question}")

eco_block = content[eco_start:eco_end]

# Extract the raw SVG (between ```{=html} and ```)
svg_start_marker = "```{=html}\n"
svg_end_marker = "\n```"

svg_html_start = eco_block.index(svg_start_marker) + len(svg_start_marker)
svg_html_end = eco_block.index(svg_end_marker, svg_html_start)

original_svg = eco_block[svg_html_start:svg_html_end]

# Modify the SVG for the new "measure" slide
new_svg = original_svg

# 1. Update aria-label
new_svg = new_svg.replace(
    'aria-label="Ecosystem from night to dawn, day and dusk: eyes glow in the dark, then rows of trees grow toward distant mountains around a pond; the sun arcs overhead, lightning fells a tree, a beaver builds a dam, animals peek out, a deer drinks, a skunk walks by and a fish jumps"',
    'aria-label="Ecologists measuring the ecosystem: two field scientists walk into the scene — one writes in a notebook, the other photographs — as the day-night cycle continues"'
)

# 2. Replace the title text (keep Ecosystems at same y=140, add "How do we measure" above)
old_title = '<text x="800" y="140" text-anchor="middle" font-size="120" font-weight="700" class="a-fade" style="--d:0.1s">Ecosystems</text>'
new_title = (
    '<text x="800" y="68" text-anchor="middle" font-size="74" font-weight="700" class="a-fade" style="--d:0.9s">How do we measure</text>\n'
    '<text x="800" y="140" text-anchor="middle" font-size="120" font-weight="700" class="a-fade" style="--d:0.1s">Ecosystems</text>'
)
new_svg = new_svg.replace(old_title, new_title)

# 3. Add ecologist figures before the closing </svg>
ecologist_svg = """
<!-- === Ecologist 1: walks in from left, writes in notebook === -->
<g transform="translate(360 870)" class="ecologist eco-l">
  <ellipse cx="4" cy="-1" rx="24" ry="7" fill="rgba(0,0,0,0.32)"/>
  <!-- legs -->
  <rect class="leg leg-b" x="-14" y="-58" width="11" height="58" rx="4" fill="#4a5a6e"/>
  <rect class="leg leg-a" x="3" y="-58" width="11" height="58" rx="4" fill="#3d4f61"/>
  <!-- boots -->
  <ellipse cx="-8" cy="-2" rx="10" ry="5" fill="#3a2a18"/>
  <ellipse cx="9" cy="-2" rx="10" ry="5" fill="#3a2a18"/>
  <!-- torso / field vest -->
  <rect x="-16" y="-108" width="34" height="52" rx="5" fill="#5a7a45"/>
  <!-- vest pocket -->
  <rect x="-12" y="-98" width="10" height="12" rx="2" fill="#4a6a35" opacity="0.8"/>
  <!-- left arm holding clipboard -->
  <line x1="-16" y1="-94" x2="-34" y2="-74" stroke="#4a5a6e" stroke-width="10" stroke-linecap="round"/>
  <!-- clipboard -->
  <rect x="-48" y="-84" width="20" height="26" rx="3" fill="#e8d898" stroke="#999" stroke-width="1.5"/>
  <rect x="-48" y="-84" width="20" height="4" rx="1" fill="#c8a830"/>
  <line x1="-45" y1="-76" x2="-31" y2="-76" stroke="#bbb" stroke-width="1.2"/>
  <line x1="-45" y1="-71" x2="-31" y2="-71" stroke="#bbb" stroke-width="1.2"/>
  <line x1="-45" y1="-66" x2="-31" y2="-66" stroke="#bbb" stroke-width="1.2"/>
  <!-- right arm writing -->
  <line x1="18" y1="-94" x2="34" y2="-72" stroke="#4a5a6e" stroke-width="10" stroke-linecap="round" class="eco-write"/>
  <!-- pencil -->
  <line x1="34" y1="-72" x2="26" y2="-58" stroke="#f0c030" stroke-width="4" stroke-linecap="round" class="eco-write"/>
  <line x1="26" y1="-58" x2="23" y2="-53" stroke="#e8e8c0" stroke-width="3" stroke-linecap="round" class="eco-write"/>
  <!-- neck -->
  <rect x="-7" y="-118" width="14" height="12" rx="4" fill="#c8a880"/>
  <!-- head -->
  <circle cx="2" cy="-133" r="17" fill="#c8a880"/>
  <!-- eyes -->
  <circle cx="-4" cy="-135" r="2.5" fill="#444"/>
  <circle cx="9" cy="-135" r="2.5" fill="#444"/>
  <!-- wide-brim field hat (brim) -->
  <ellipse cx="2" cy="-148" rx="26" ry="6" fill="#8b5e14"/>
  <!-- hat crown -->
  <path d="M-14,-153 Q-14,-175 2,-177 Q18,-175 18,-153 Z" fill="#a07020"/>
  <!-- hat band -->
  <rect x="-14" y="-154" width="32" height="6" rx="2" fill="#5c3a10"/>
  <!-- sample bag on hip -->
  <rect x="18" y="-78" width="14" height="16" rx="3" fill="#8b7a3a" opacity="0.9"/>
  <line x1="18" y1="-78" x2="18" y2="-94" stroke="#8b7a3a" stroke-width="3"/>
</g>

<!-- === Ecologist 2: walks in from right, takes photos === -->
<g transform="translate(1240 868) scale(-1 1)" class="ecologist eco-r">
  <ellipse cx="4" cy="-1" rx="24" ry="7" fill="rgba(0,0,0,0.32)"/>
  <!-- legs -->
  <rect class="leg leg-b" x="-14" y="-58" width="11" height="58" rx="4" fill="#5c4a3a"/>
  <rect class="leg leg-a" x="3" y="-58" width="11" height="58" rx="4" fill="#503e30"/>
  <!-- boots -->
  <ellipse cx="-8" cy="-2" rx="10" ry="5" fill="#2a2010"/>
  <ellipse cx="9" cy="-2" rx="10" ry="5" fill="#2a2010"/>
  <!-- torso / field jacket -->
  <rect x="-16" y="-108" width="34" height="52" rx="5" fill="#c87a40"/>
  <!-- chest pockets -->
  <rect x="-12" y="-100" width="10" height="14" rx="2" fill="#a85f28" opacity="0.8"/>
  <rect x="2" y="-100" width="10" height="14" rx="2" fill="#a85f28" opacity="0.8"/>
  <!-- both arms raised to hold camera -->
  <line x1="-16" y1="-94" x2="-26" y2="-115" stroke="#5c4a3a" stroke-width="10" stroke-linecap="round" class="eco-cam-arm"/>
  <line x1="18" y1="-94" x2="26" y2="-115" stroke="#5c4a3a" stroke-width="10" stroke-linecap="round" class="eco-cam-arm"/>
  <!-- camera body -->
  <rect x="-30" y="-126" width="36" height="22" rx="4" fill="#222" class="eco-cam-arm"/>
  <!-- lens -->
  <circle cx="-6" cy="-115" r="8" fill="#333" class="eco-cam-arm"/>
  <circle cx="-6" cy="-115" r="5" fill="#1a1a2a" class="eco-cam-arm"/>
  <circle cx="-6" cy="-115" r="2.5" fill="#0a0a18" class="eco-cam-arm"/>
  <!-- viewfinder -->
  <rect x="2" y="-126" width="6" height="5" rx="1" fill="#444" class="eco-cam-arm"/>
  <!-- camera flash -->
  <rect x="-32" y="-128" width="8" height="5" rx="1" fill="#fff" class="cam-flash" opacity="0"/>
  <!-- neck -->
  <rect x="-7" y="-118" width="14" height="12" rx="4" fill="#d0b090"/>
  <!-- head -->
  <circle cx="2" cy="-133" r="17" fill="#d0b090"/>
  <!-- eyes (looking through viewfinder, slightly squinted) -->
  <ellipse cx="-4" cy="-135" rx="3" ry="2" fill="#333"/>
  <ellipse cx="9" cy="-135" rx="3" ry="2" fill="#333"/>
  <!-- baseball cap (brim forward, but we're flipped so it appears correct) -->
  <ellipse cx="2" cy="-148" rx="20" ry="5" fill="#2a4a9a"/>
  <ellipse cx="2" cy="-150" rx="18" ry="8" fill="#3a5aaa"/>
  <!-- brim extension (cap peak) -->
  <path d="M-18,-149 Q-28,-148 -26,-144 Q-16,-146 -18,-149 Z" fill="#2a4a9a"/>
  <!-- camera strap -->
  <path d="M-28,-120 Q0,-108 26,-120" stroke="#6a5a40" stroke-width="3" fill="none"/>
</g>"""

new_svg = new_svg.replace("</svg>", ecologist_svg + "\n</svg>")

# Build the new slide block
new_slide = f"""## {{#slide-measure-ecosystems}}

```{{=html}}
{new_svg}
```

::: {{.notes}}
To assess ecosystem risk we need to measure what's happening on the ground. Field ecologists collect data: species counts, vegetation surveys, photographs, and physical samples — combined with satellite imagery and remote sensing to scale up to the country level.
:::


"""

# Insert before the ## {#slide-question}
new_content = content[:eco_end] + new_slide + content[eco_end:]

with open("index.qmd", "w") as f:
    f.write(new_content)

print("Done. New slide inserted after #slide-ecosystems.")
