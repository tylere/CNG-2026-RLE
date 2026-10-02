"""
Rebuilds the #slide-camera-trap slide in index.qmd.

Narrative:
  1. Eco-r walks from right to the camera location (SVG x≈850).
  2. Camera trap drops in when eco-r arrives (~T=16s).
  3. Both ecologists walk offscreen as the sun goes down (~T=30-40s).
  4. Night falls. Deer at the lake walks left to stand just right of the camera.
  5. Camera flash fires (T=62s): localised glow around the deer.
  6. Deer's eyes go wide; deer shakes its head.
  7. Deer walks calmly back to the lake.
"""

import re, pathlib

QMD = pathlib.Path("index.qmd")
text = QMD.read_text()

# ── 1. Locate the measure-ecosystems slide ────────────────────────────────────
m_measure = re.search(
    r'## \{#slide-measure-ecosystems\}.*?(?=## \{#)',
    text, re.DOTALL
)
if not m_measure:
    raise RuntimeError("Could not find slide-measure-ecosystems")
measure_slide = m_measure.group(0)

# ── 2. Extract the landscape SVG body (up to but not including ecologists) ───
m_eco = re.search(
    r'(```\{=html\}\n<svg class="canvas eco side".*?)\n<!-- === Ecologist 1',
    measure_slide, re.DOTALL
)
if not m_eco:
    raise RuntimeError("Could not find SVG start / Ecologist 1 boundary")

eco_svg_raw = m_eco.group(1).replace("```{=html}\n", "", 1)
flash_match = re.search(r'<rect class="flash"[^/]*/>', eco_svg_raw)
eco_svg_body = eco_svg_raw[:flash_match.end()] if flash_match else eco_svg_raw

# Update aria-label.
eco_svg_body = eco_svg_body.replace(
    'aria-label="Ecologists measuring the ecosystem: two field scientists walk into the scene — one writes in a notebook, the other photographs — as the day-night cycle continues"',
    'aria-label="Camera trap at the pond captures the deer drinking at night"'
)

# ── 3. Extract ecologist SVG groups ──────────────────────────────────────────
m_eco_l = re.search(
    r'<!-- === Ecologist 1.*?(?=<!-- === Ecologist 2)',
    measure_slide, re.DOTALL
)
m_eco_r = re.search(
    r'<!-- === Ecologist 2.*?(?=</svg>)',
    measure_slide, re.DOTALL
)
if not m_eco_l or not m_eco_r:
    raise RuntimeError("Could not find ecologist groups")

eco_l_text = m_eco_l.group(0).strip()
eco_r_text = m_eco_r.group(0).strip()

# Rename classes so camera-trap CSS rules don't conflict with the wander rules.
eco_l_ct = eco_l_text.replace(
    'class="ecologist eco-l"', 'class="ecologist eco-l-ct"'
)
eco_r_ct = eco_r_text.replace(
    'class="ecologist eco-r"', 'class="ecologist eco-r-ct"'
)
# Strip the comment lines.
eco_l_ct = re.sub(r'<!-- .* -->\n?', '', eco_l_ct).strip()
eco_r_ct = re.sub(r'<!-- .* -->\n?', '', eco_r_ct).strip()

# ── 4. Wrap the drinking deer in .ct-lake-deer for CSS-animatable walk ────────
# The deer's outer group is translate(1132.0 720.0) scale(1.1).
eco_svg_body = re.sub(
    r'<g transform="translate\(1132\.0 720\.0\) scale\(1\.1\)">\n',
    '<g class="ct-lake-deer"><g transform="translate(1132.0 720.0) scale(1.1)">\n',
    eco_svg_body,
    count=1
)
# Close the outer wrapper: insert </g> just before the next sibling group.
eco_svg_body = eco_svg_body.replace(
    '</g>\n<g transform="translate(470.0 745.0)',
    '</g>\n</g>\n<g transform="translate(470.0 745.0)',
    1
)

# ── 5. Tag the deer's eye circles so CSS can animate them growing ────────────
# These are inside the .drink group of the deer at (1132, 720).
eco_svg_body = eco_svg_body.replace(
    '<circle cx="-33" cy="-76" r="1.8" fill="#1a1a1a"/>',
    '<circle cx="-33" cy="-76" r="1.8" fill="#1a1a1a" class="deer-ct-eye"/>',
    1
)
eco_svg_body = eco_svg_body.replace(
    '<circle cx="-42" cy="-71" r="2" fill="#1a1a1a"/>',
    '<circle cx="-42" cy="-71" r="2" fill="#1a1a1a" class="deer-ct-eye"/>',
    1
)

# ── 6. Add gradients to <defs> ────────────────────────────────────────────────
new_defs = '''\
    <radialGradient id="ct-ir-glow-g2" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ff5500" stop-opacity="0.75"/>
      <stop offset="1" stop-color="#ff5500" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ct-flash-glow-g" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0"   stop-color="#ffffff" stop-opacity="0.98"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.6"/>
      <stop offset="1"   stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>'''
eco_svg_body = eco_svg_body.replace(
    '</defs>\n<rect class="daysky"',
    new_defs + '\n</defs>\n<rect class="daysky"',
    1
)

# ── 7. New SVG elements ───────────────────────────────────────────────────────

# Camera trap on tripod: starts hidden (opacity="0"), drops in at T=16s.
# At SVG (850, 750); lens faces RIGHT toward the drinking deer at (1132, 720).
camera_trap = '''\
<g class="ct-tripod" transform="translate(850 750)" opacity="0">
  <line x1="0" y1="-92" x2="-46" y2="0" stroke="#555" stroke-width="5" stroke-linecap="round"/>
  <line x1="0" y1="-92" x2="6" y2="2" stroke="#555" stroke-width="5" stroke-linecap="round"/>
  <line x1="0" y1="-92" x2="44" y2="-5" stroke="#555" stroke-width="5" stroke-linecap="round"/>
  <!-- Camera body; lens faces right (toward the deer at x=1132) -->
  <rect x="-4" y="-128" width="60" height="40" rx="5" fill="#1c1c1c" stroke="#333" stroke-width="1.5"/>
  <circle cx="50" cy="-116" r="4" class="ct-ir-led" fill="#3a0000" opacity="0.3"/>
  <circle cx="50" cy="-107" r="4" class="ct-ir-led" fill="#3a0000" opacity="0.3"/>
  <circle cx="42" cy="-116" r="4" class="ct-ir-led" fill="#3a0000" opacity="0.3"/>
  <circle cx="42" cy="-107" r="4" class="ct-ir-led" fill="#3a0000" opacity="0.3"/>
  <circle cx="36" cy="-108" r="11" fill="#222" stroke="#555" stroke-width="2"/>
  <circle cx="36" cy="-108" r="7" fill="#111"/>
  <circle cx="36" cy="-108" r="3.5" fill="#080818"/>
  <circle cx="39" cy="-111" r="1.8" fill="rgba(255,255,255,0.22)"/>
  <circle cx="52" cy="-126" r="3" class="ct-status-led" fill="#ff2200" opacity="0.7"/>
</g>'''

# IR glow (fires at T=62s, illuminates the deer's position at x≈870).
ir_glow = '''\
<ellipse class="ct-ir-flash" cx="950" cy="690" rx="260" ry="180"
  fill="url(#ct-ir-glow-g2)" opacity="0"/>'''

# Camera flash: a broad radial glow centred on the deer.
ct_flash = '''\
<ellipse class="ct-flash" cx="870" cy="690" rx="500" ry="380"
  fill="url(#ct-flash-glow-g)" opacity="0"/>'''

# ── 8. Assemble the slide ─────────────────────────────────────────────────────
new_svg = (
    eco_svg_body + "\n"
    + eco_l_ct + "\n"
    + eco_r_ct + "\n"
    + camera_trap + "\n"
    + ir_glow + "\n"
    + ct_flash + "\n"
    + "</svg>"
)

new_slide = (
    "## {#slide-camera-trap}\n\n"
    "```{=html}\n"
    + new_svg + "\n"
    "```\n\n"
    "::: {.notes}\n"
    "Camera traps are triggered by motion and record wildlife continuously — "
    "including nocturnal behaviour invisible to daytime field surveys.\n"
    ":::\n"
)

# ── 9. Replace existing camera-trap slide ────────────────────────────────────
pattern = r'## \{#slide-camera-trap\}.*?(?=## \{#slide-wildlife)'
new_text = re.sub(pattern, new_slide + "\n\n", text, flags=re.DOTALL)

if new_text == text:
    raise RuntimeError("Pattern not matched — slide not replaced")

QMD.write_text(new_text)
print("Done. Camera-trap slide rebuilt.")
