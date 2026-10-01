"""Generate the animated "Ecosystems" scene and write it into index.qmd.

A full-width, front-on ecosystem whose rows recede into the distance, running
from night through dawn, day and dusk. The scene replaces the
<svg class="canvas eco side"> ... </svg> block in index.qmd. Animations live in
custom.scss (the "Ecosystems slide" section). The layout is seeded, so
re-running gives the same scene.

Usage:  uv run scripts/gen_ecosystem_scene.py
"""
import math
import random
import re
from pathlib import Path

QMD = Path(__file__).resolve().parent.parent / 'index.qmd'
HAZE = (0x1D, 0x23, 0x2B)  # slide background; distant things blend toward it

GREENS = ['#3d7a3f', '#4f8a3c', '#2f6b3a', '#5c9443', '#3f7f5a', '#6a9a3a', '#4a8550']
CONIFER_GREENS = ['#24553a', '#2c6142', '#1f4d36', '#2e5c3a', '#335f33']
TRUNKS = ['#6b4a2b', '#7a5533', '#5e3f24']
GREYS = ['#7b8088', '#8a8f96', '#6f747b', '#958f86']


# ---------------------------------------------------------------- helpers
def hx(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def mix(c, k):
    """Blend colour c toward the background haze by fraction k (distance fade, stays opaque)."""
    return '#%02x%02x%02x' % tuple(int(a + (h - a) * k) for a, h in zip(hx(c), HAZE))


def tone(c, f):
    """Darken (f < 1) or lighten (f > 1) colour c."""
    if f < 1:
        return '#%02x%02x%02x' % tuple(int(a * f) for a in hx(c))
    return '#%02x%02x%02x' % tuple(int(a + (255 - a) * (f - 1)) for a in hx(c))


def f1(x):
    return f'{x:.1f}'


def pts(p):
    return ' '.join(f'{f1(x)},{f1(y)}' for x, y in p)


def put(x, y, inner, cls='', style='', flip=False, scale=1.0):
    """Place drawing `inner` (base at its origin) at (x, y); returns (sort key, svg)."""
    sx = -scale if flip else scale
    attr = f' class="{cls}"' if cls else ''
    attr += f' style="{style}"' if style else ''
    return y, f'<g transform="translate({f1(x)} {f1(y)}) scale({sx} {scale})"><g{attr}>' + ''.join(inner) + '</g></g>'


# ---------------------------------------------------------------- vegetation and rocks
def shadow(h):
    return f'<ellipse cx="{f1(h*0.14)}" cy="2" rx="{f1(h*0.3)}" ry="{f1(h*0.09)}" fill="rgba(0,0,0,0.28)"/>'


def conifer(h, col, trunk, k):
    col, trunk = mix(col, k), mix(trunk, k)
    out = [shadow(h * 0.8)]
    tw, th = h * 0.07, h * 0.2
    out.append(f'<rect x="{f1(-tw/2)}" y="{f1(-th)}" width="{f1(tw)}" height="{f1(th)}" fill="{trunk}"/>')
    tiers = random.choice([3, 4, 4])
    base, top = -th * 0.55, -h
    for i in range(tiers):
        y0 = base + (top - base) * i / (tiers + 0.5)
        y1 = top if i == tiers - 1 else base + (top - base) * (i + 1.8) / (tiers + 0.5)
        w = h * 0.52 * (1 - i / (tiers + 0.9)) * random.uniform(0.88, 1.1)
        j = lambda: random.uniform(-0.04, 0.04) * w
        ax = random.uniform(-0.03, 0.03) * w
        right = [(ax, y1), (w * 0.2 + j(), y1 + (y0 - y1) * 0.4), (w * 0.33 + j(), y1 + (y0 - y1) * 0.72),
                 (w / 2, y0), (w * 0.27, y0 - h * 0.025), (0, y0 + h * 0.015)]
        left = [(-w * 0.27, y0 - h * 0.025), (-w / 2, y0), (-w * 0.33 + j(), y1 + (y0 - y1) * 0.72),
                (-w * 0.2 + j(), y1 + (y0 - y1) * 0.4)]
        out.append(f'<polygon points="{pts(right + left)}" fill="{col}"/>')
        out.append(f'<polygon points="{pts(right)}" fill="rgba(0,0,0,0.22)"/>')
    return out


def blob_canopy(cx, cy, R, col, n):
    blobs = [(cx, cy, R * 0.72)]
    for i in range(n):
        a = 2 * math.pi * i / n + random.uniform(-0.3, 0.3)
        blobs.append((cx + R * 0.58 * math.cos(a) * random.uniform(0.8, 1.05),
                      cy + R * 0.45 * math.sin(a) * random.uniform(0.8, 1.05),
                      R * random.uniform(0.42, 0.6)))
    dark, light = tone(col, 0.7), col
    out = [f'<circle cx="{f1(x)}" cy="{f1(y)}" r="{f1(r)}" fill="{dark}"/>' for x, y, r in blobs]
    out += [f'<circle cx="{f1(x - r*0.14)}" cy="{f1(y - r*0.14)}" r="{f1(r*0.86)}" fill="{light}"/>' for x, y, r in blobs]
    for x, y, r in random.sample(blobs[1:], 2):
        out.append(f'<circle cx="{f1(x - r*0.3)}" cy="{f1(y - r*0.32)}" r="{f1(r*0.35)}" fill="{tone(col, 1.14)}"/>')
    top = min(y - r for x, y, r in blobs)
    return out, top


def broadleaf(h, col, trunk, k):
    col, trunk = mix(col, k), mix(trunk, k)
    out = [shadow(h)]
    cy, R = -h * 0.64, h * 0.3
    bw = h * 0.024
    out.append(f'<polygon points="{pts([(-h*0.045, 0), (-h*0.025, cy + R*0.2), (h*0.025, cy + R*0.2), (h*0.045, 0)])}" fill="{trunk}"/>')
    out.append(f'<path d="M0 {f1(cy + R*0.75)} L{f1(-R*0.55)} {f1(cy + R*0.05)} M0 {f1(cy + R*0.55)} L{f1(R*0.5)} {f1(cy - R*0.1)}" '
               f'stroke="{trunk}" stroke-width="{f1(bw)}" stroke-linecap="round" fill="none"/>')
    c, top = blob_canopy(0, cy, R, col, random.choice([5, 6, 7]))
    return out + c, top


def poplar(h, col, trunk, k, birch=False):
    col = mix(col, k)
    trunk = mix('#e6e0d4' if birch else trunk, k)
    out = [shadow(h * 0.7)]
    out.append(f'<rect x="{f1(-h*0.025)}" y="{f1(-h*0.45)}" width="{f1(h*0.05)}" height="{f1(h*0.45)}" fill="{trunk}"/>')
    if birch:
        mark = mix('#3a3a3a', k)
        for y in (0.08, 0.17, 0.27, 0.36):
            out.append(f'<rect x="{f1(-h*0.025 + random.uniform(0, h*0.02))}" y="{f1(-h*y)}" width="{f1(h*0.022)}" height="{f1(h*0.012)}" fill="{mark}"/>')
    cy, rx, ry = -h * 0.6, h * 0.15, h * 0.4
    out.append(f'<ellipse cx="0" cy="{f1(cy)}" rx="{f1(rx)}" ry="{f1(ry)}" fill="{tone(col, 0.7)}"/>')
    out.append(f'<ellipse cx="{f1(-rx*0.18)}" cy="{f1(cy - ry*0.05)}" rx="{f1(rx*0.8)}" ry="{f1(ry*0.92)}" fill="{col}"/>')
    out.append(f'<ellipse cx="{f1(-rx*0.4)}" cy="{f1(cy - ry*0.35)}" rx="{f1(rx*0.3)}" ry="{f1(ry*0.3)}" fill="{tone(col, 1.14)}"/>')
    return out


def random_tree(h_range, k):
    """A random conifer, broadleaf, poplar or birch of height in h_range."""
    kind = random.choices(['conifer', 'broadleaf', 'poplar', 'birch'], [40, 35, 15, 10])[0]
    if kind == 'conifer':
        return conifer(random.uniform(*h_range) * 1.1, random.choice(CONIFER_GREENS), random.choice(TRUNKS), k)
    if kind == 'broadleaf':
        return broadleaf(random.uniform(*h_range), random.choice(GREENS), random.choice(TRUNKS), k)[0]
    return poplar(random.uniform(*h_range) * 1.05, random.choice(GREENS), random.choice(TRUNKS), k, birch=(kind == 'birch'))


def bush(h, col, k):
    col = mix(col, k)
    out = [f'<ellipse cx="{f1(h*0.2)}" cy="2" rx="{f1(h*0.9)}" ry="{f1(h*0.22)}" fill="rgba(0,0,0,0.25)"/>']
    c, _ = blob_canopy(0, -h * 0.42, h * 0.62, col, 4)
    return out + c


def boulder(sz, col, k):
    col = mix(col, k)
    s = sz
    body = [(-s/2, 0), (-s*0.46, -s*0.34), (-s*0.2, -s*0.6), (s*0.24, -s*0.56), (s/2, -s*0.26), (s*0.47, 0)]
    topf = [(-s*0.46, -s*0.34), (-s*0.2, -s*0.6), (s*0.24, -s*0.56), (s*0.08, -s*0.33)]
    side = [(s*0.24, -s*0.56), (s/2, -s*0.26), (s*0.47, 0), (s*0.1, 0), (s*0.08, -s*0.33)]
    return [f'<ellipse cx="{f1(s*0.12)}" cy="1" rx="{f1(s*0.6)}" ry="{f1(s*0.14)}" fill="rgba(0,0,0,0.28)"/>',
            f'<polygon points="{pts(body)}" fill="{col}"/>',
            f'<polygon points="{pts(topf)}" fill="{tone(col, 1.18)}"/>',
            f'<polygon points="{pts(side)}" fill="{tone(col, 0.75)}"/>']


def tuft(x, y, s, col):
    return (f'<path d="M{f1(x-4*s)} {f1(y)} L{f1(x-2*s)} {f1(y-6*s)} M{f1(x)} {f1(y)} L{f1(x)} {f1(y-8*s)} '
            f'M{f1(x+4*s)} {f1(y)} L{f1(x+2*s)} {f1(y-6*s)}" stroke="{col}" stroke-width="{f1(1.5*s)}"/>')


# ---------------------------------------------------------------- animals
def fox_head():
    o, w, d = '#d9662b', '#f3ece2', '#2a1c14'
    return [f'<polygon points="-24,-28 -12,-8 12,-8 24,-28 22,2 0,22 -22,2" fill="{o}"/>',
            f'<polygon points="-20,-22 -13,-10 -8,-10" fill="{d}"/><polygon points="20,-22 13,-10 8,-10" fill="{d}"/>',
            f'<polygon points="-22,2 -8,6 0,22" fill="{w}"/><polygon points="22,2 8,6 0,22" fill="{w}"/>',
            f'<circle cx="-8" cy="-2" r="2.6" fill="{d}"/><circle cx="8" cy="-2" r="2.6" fill="{d}"/>',
            f'<circle cx="0" cy="19" r="3" fill="{d}"/>']


def rabbit_head():
    g, p, d = '#b9b4ac', '#e3a2a2', '#2a2a2a'
    return [f'<ellipse cx="-8" cy="-40" rx="6" ry="22" fill="{g}"/><ellipse cx="8" cy="-40" rx="6" ry="22" fill="{g}"/>',
            f'<ellipse cx="-8" cy="-40" rx="2.5" ry="15" fill="{p}"/><ellipse cx="8" cy="-40" rx="2.5" ry="15" fill="{p}"/>',
            f'<circle cx="0" cy="-8" r="15" fill="{g}"/>',
            f'<circle cx="-6" cy="-11" r="2.3" fill="{d}"/><circle cx="6" cy="-11" r="2.3" fill="{d}"/>',
            f'<circle cx="0" cy="-4" r="2" fill="#d98c8c"/>']


def owl_head():
    b, f, y, d = '#8a7a66', '#cbbb9f', '#FFD626', '#1a1a1a'
    return [f'<path d="M-20 40 L-20 -10 L-16 -26 L-7 -17 L7 -17 L16 -26 L20 -10 L20 40 Z" fill="{b}"/>',
            f'<circle cx="-8" cy="-6" r="8" fill="{f}"/><circle cx="8" cy="-6" r="8" fill="{f}"/>',
            f'<circle cx="-8" cy="-6" r="4.5" fill="{y}"/><circle cx="8" cy="-6" r="4.5" fill="{y}"/>',
            f'<circle cx="-8" cy="-6" r="2" fill="{d}"/><circle cx="8" cy="-6" r="2" fill="{d}"/>',
            f'<polygon points="-3,2 3,2 0,8" fill="#e3a83a"/>']


def night_pose(x, y, key, inner, scale=1.0, late=False):
    """The same animal sitting in its peek-out pose, shown only at night."""
    cls = 'night-pose late' if late else 'night-pose'
    return key - 0.4, f'<g transform="translate({f1(x)} {f1(y)}) scale({scale})"><g class="{cls}">' + ''.join(inner) + '</g></g>'


def peeker(x, y, key, inner, dx, dy, delay, period, scale=1.0):
    """An animal that peeks out from behind something drawn just after it (sort key `key`)."""
    g = (f'<g transform="translate({f1(x)} {f1(y)}) scale({scale})"><g class="peek" '
         f'style="--d:{delay}s; --p:{period}s; --dx:{dx}px; --dy:{dy}px">' + ''.join(inner) + '</g></g>')
    return key - 0.5, g


def deer(x, y, k, scale=1.0):
    """Side view, facing left; the neck pivots at the shoulder (see .drink in custom.scss)."""
    tan, dk = mix('#a8774a', k), mix('#7b5434', k)
    return f'''<g transform="translate({f1(x)} {f1(y)}) scale({scale})">
  <ellipse cx="6" cy="2" rx="34" ry="6" fill="rgba(0,0,0,0.28)"/>
  <rect x="-20" y="-28" width="5" height="28" fill="{dk}"/><rect x="-11" y="-28" width="5" height="28" fill="{tan}"/>
  <rect x="14" y="-28" width="5" height="28" fill="{dk}"/><rect x="22" y="-28" width="5" height="28" fill="{tan}"/>
  <ellipse cx="4" cy="-36" rx="28" ry="13" fill="{tan}"/>
  <ellipse cx="31" cy="-40" rx="4" ry="6" fill="#f0e8dc"/>
  <g class="drink">
    <polygon points="-18,-44 -30,-70 -21,-74 -8,-38" fill="{tan}"/>
    <ellipse cx="-31" cy="-74" rx="12" ry="7" transform="rotate(-20 -31 -74)" fill="{tan}"/>
    <polygon points="-24,-80 -18,-90 -16,-78" fill="{dk}"/>
    <path d="M-27 -80 Q-30 -96 -40 -100 M-29 -91 L-22 -98 M-23 -80 Q-16 -95 -8 -98" stroke="{dk}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <circle cx="-33" cy="-76" r="1.8" fill="#1a1a1a"/>
    <circle cx="-42" cy="-71" r="2" fill="#1a1a1a"/>
  </g>
</g>'''


def fish(x, y):
    return f'''<g transform="translate({f1(x)} {f1(y)})">
  <ellipse class="splash s1" cx="0" cy="0" rx="14" ry="5" fill="none" stroke="#bfe0f5" stroke-width="2"/>
  <ellipse class="splash s2" cx="56" cy="0" rx="14" ry="5" fill="none" stroke="#bfe0f5" stroke-width="2"/>
  <g class="fish"><path d="M-14 0 Q-4 -9 10 -2 L18 -8 L16 0 L18 8 L10 2 Q-4 9 -14 0 Z" fill="#f08a3c"/><circle cx="-8" cy="-1" r="1.6" fill="#1a1a1a"/></g>
</g>'''


def skunk(x0, y0, x1, y1, scale=1.0):
    """Walks from (x0, y0) to (x1, y1), facing right."""
    return f'''<g transform="translate({f1(x0)} {f1(y0)})"><g class="skunk" style="--sx:{f1(x1-x0)}px; --sy:{f1(y1-y0)}px"><g transform="scale({scale})">
  <ellipse cx="0" cy="2" rx="26" ry="5" fill="rgba(0,0,0,0.3)"/>
  <rect class="leg leg-a" x="-14" y="-10" width="5" height="11" fill="#15171a"/><rect class="leg leg-b" x="-6" y="-10" width="5" height="11" fill="#15171a"/>
  <rect class="leg leg-b" x="10" y="-10" width="5" height="11" fill="#15171a"/><rect class="leg leg-a" x="17" y="-10" width="5" height="11" fill="#15171a"/>
  <path class="tail" d="M-18 -16 Q-40 -22 -38 -46 Q-36 -62 -20 -58 Q-28 -46 -16 -30 Z" fill="#15171a"/>
  <path class="tail" d="M-24 -26 Q-34 -40 -27 -54" stroke="#f2f2f2" stroke-width="4" fill="none" stroke-linecap="round"/>
  <ellipse cx="2" cy="-17" rx="22" ry="11" fill="#15171a"/>
  <ellipse cx="23" cy="-15" rx="9" ry="7" fill="#15171a"/>
  <path d="M-16 -24 Q2 -32 22 -21" stroke="#f2f2f2" stroke-width="4" fill="none" stroke-linecap="round"/>
  <circle cx="26" cy="-16" r="1.6" fill="#f2f2f2"/>
  <circle cx="31" cy="-13" r="1.8" fill="#3a3a3a"/>
</g></g></g>'''


# ---------------------------------------------------------------- sky
def cloud(scale, dark=False):
    lo, hi = ('#3c424a', '#555c65') if dark else ('#c9d0d8', '#e3e8ee')
    return (f'<g transform="scale({scale})">'
            f'<ellipse cx="0" cy="0" rx="70" ry="20" fill="{lo}"/>'
            f'<circle cx="-30" cy="-12" r="26" fill="{hi}"/><circle cx="8" cy="-24" r="32" fill="{hi}"/>'
            f'<circle cx="42" cy="-8" r="22" fill="{hi}"/><ellipse cx="0" cy="-4" rx="66" ry="16" fill="{hi}"/>'
            '</g>')


def sky(prefix, clouds):
    out = [f'<g class="sun"><circle cx="800" cy="70" r="95" fill="url(#{prefix}-sun)"/>'
           '<circle cx="800" cy="70" r="46" fill="#FFD626"/></g>']
    for y, s, t, dl in clouds:
        out.append(f'<g transform="translate(0 {y})"><g class="cloud" style="--t:{t}s; --d:{dl}s; opacity:0.85">{cloud(s)}</g></g>')
    return out


def birds(n, y_range):
    """n small groups (1-3 birds) with random heights, directions, speeds, start times and wingbeats."""
    out = []
    for _ in range(n):
        y = random.uniform(*y_range)
        t = random.uniform(55, 95)      # one cycle; a crossing takes 60% of it
        d = random.uniform(6, 45)       # first appearance, after dawn
        rtl = ' rtl' if random.random() < 0.5 else ''
        bob = f'--b:{random.uniform(2.5, 4.5):.1f}s; --bob:{random.uniform(6, 16):.0f}px'
        members = []
        for i in range(random.choice([1, 1, 2, 3])):
            ox, oy = (0, 0) if i == 0 else (random.uniform(-90, -30), random.uniform(-25, 25))
            w = random.uniform(16, 26)
            members.append(f'<g transform="translate({f1(ox)} {f1(oy)})"><g class="flap" style="animation-duration:{random.uniform(0.32, 0.55):.2f}s; '
                           f'animation-delay:{-random.uniform(0, 0.5):.2f}s"><path class="bird" d="M{f1(-w)} 0 Q{f1(-w/2)} {f1(-w*0.54)} 0 0 '
                           f'Q{f1(w/2)} {f1(-w*0.54)} {f1(w)} 0"/></g></g>')
        out.append(f'<g class="bird-fly{rtl}" style="--d:{d:.1f}s; --t:{t:.0f}s; --y:{y:.0f}px"><g class="bob" style="{bob}">'
                   + ''.join(members) + '</g></g>')
    return out


def glowing_eyes(points, r, colour, late=False):
    """An animal's eyes, glowing in the dark (drawn above the night veil) and blinking.
    `late` eyes only show in the evening, for animals whose perch is still growing at the start."""
    blink = f'animation-duration:{random.uniform(3, 7):.1f}s; animation-delay:{-random.uniform(0, 6):.1f}s'
    dots = ''.join(f'<circle cx="{f1(x)}" cy="{f1(y)}" r="{f1(r*2.5)}" fill="{colour}" opacity="0.22"/>'
                   f'<circle cx="{f1(x)}" cy="{f1(y)}" r="{f1(r)}" fill="{colour}"/>' for x, y in points)
    return f'<g class="eyes{" late" if late else ""}"><g class="blink" style="{blink}">{dots}</g></g>'


def defs(prefix, ground_top, ground_bottom):
    return f'''  <defs>
    <linearGradient id="{prefix}-ground" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{ground_top}"/><stop offset="1" stop-color="{ground_bottom}"/>
    </linearGradient>
    <radialGradient id="{prefix}-sun">
      <stop offset="0.45" stop-color="#FFD626" stop-opacity="0.45"/><stop offset="1" stop-color="#FFD626" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="{prefix}-water" cx="0.45" cy="0.4" r="0.6">
      <stop offset="0" stop-color="#3b84b5"/><stop offset="1" stop-color="#1f557c"/>
    </radialGradient>
  </defs>'''


def pond(cx, cy, rx, ry, prefix, n_pebbles, lilies, ripples):
    out = [f'<ellipse cx="{f1(cx)}" cy="{f1(cy)}" rx="{f1(rx+14)}" ry="{f1(ry+9)}" fill="#9c8a62"/>',
           f'<ellipse cx="{f1(cx)}" cy="{f1(cy)}" rx="{f1(rx)}" ry="{f1(ry)}" fill="url(#{prefix}-water)"/>']
    for i in range(n_pebbles):
        a = random.uniform(0, 2 * math.pi)
        out.append(f'<ellipse cx="{f1(cx + (rx+8)*math.cos(a))}" cy="{f1(cy + (ry+5)*math.sin(a))}" rx="{f1(random.uniform(2.5, 5))}" ry="2.2" fill="{random.choice(GREYS)}"/>')
    for lx, ly in lilies:
        out.append(f'<path d="M{f1(cx+lx)} {f1(cy+ly)} m-9 0 a9 4.5 0 1 0 18 0 l-9 0 z" fill="#4f8a3c"/>')
    for ox, oy, dl in ripples:
        out.append(f'<ellipse class="ripple" style="animation-delay:{dl}s" cx="{f1(cx+ox)}" cy="{f1(cy+oy)}" rx="16" ry="6" fill="none" stroke="#9fd0ee" stroke-width="1.5"/>')
    return out


def drink_ripple(x, y):
    return f'<ellipse class="drink-ripple" cx="{f1(x)}" cy="{f1(y)}" rx="10" ry="4" fill="none" stroke="#bfe0f5" stroke-width="1.5"/>'


def beaver(x, y, drag):
    """Side view, facing left. Its walk, chew and drag (by --mx/--my) are timed in custom.scss (.beaver)."""
    fur, dk = '#6b4428', '#3b2a1d'
    return f'''<g transform="translate({f1(x)} {f1(y)})"><g class="beaver" style="{drag}"><g transform="scale(1.25)">
  <ellipse cx="2" cy="1" rx="26" ry="4" fill="rgba(0,0,0,0.28)"/>
  <ellipse cx="25" cy="-5" rx="15" ry="5" fill="{dk}"/>
  <ellipse cx="0" cy="-12" rx="21" ry="12" fill="{fur}"/>
  <ellipse cx="-10" cy="-1" rx="5" ry="3" fill="{dk}"/><ellipse cx="9" cy="-1" rx="5" ry="3" fill="{dk}"/>
  <g class="beaver-head">
    <circle cx="-19" cy="-17" r="10" fill="{fur}"/>
    <circle cx="-15" cy="-26" r="3" fill="{dk}"/>
    <circle cx="-23" cy="-19" r="1.7" fill="#111"/>
    <circle cx="-29" cy="-15" r="2.4" fill="#111"/>
    <rect x="-28" y="-11" width="4" height="4" fill="#e3a83a"/>
  </g>
</g></g></g>'''


SIDE_DEFS = '''  <defs>
    <radialGradient id="side-glow">
      <stop offset="0" stop-color="#ff9a4a" stop-opacity="0.55"/><stop offset="1" stop-color="#ff9a4a" stop-opacity="0"/>
    </radialGradient>
  </defs>'''


# ================================================================ side (front-on) scene
def side_scene():
    """Rows recede like the template's applause slide: farther rows are smaller and hazier.

    The land runs past the slide edges (X0..X1) and the SVG overflows, so the scene fills
    the screen even where reveal.js letterboxes the 1600x900 slide."""
    random.seed(5)
    X0, X1 = -320, 1920
    FAR_Y, MID_Y, NEAR_Y, TRAIL_Y = 565, 642, 815, 870
    K_FAR, K_MID, K_NEAR = 0.55, 0.3, 0.04
    PCX, PCY, PRX, PRY = 800, 706, 300, 42      # pond
    OWL_X, FOX_X, RABBIT_X = 1330, 1170, 505    # hiding places
    DEER_X, DEER_Y, DEER_S = 1132, 720, 1.1
    STRIKE_X = 1000                             # lightning hits the mid-row tree nearest here
    BEAVER_TREE, DAM = (610, 748), (515, 689)   # the sapling, and where the stream gets dammed
    items, ground = [], []

    def grow_delay(y):  # mostly random start times, loosely far-to-near
        return 0.3 + random.uniform(0, 5.5) + 2.0 * (y - 550) / 290

    # distant mountains with snowcaps, then rolling hills
    peaks = [(X0, 470), (-180, 410), (-60, 470), (90, 395), (230, 455), (370, 380), (520, 445), (690, 410), (850, 470), (1010, 385),
             (1160, 440), (1300, 375), (1450, 430), (1600, 400), (1740, 455), (X1, 405)]
    rock, snow = mix('#5d6b78', 0.45), mix('#e6ebf0', 0.45)
    ground.append(f'<polygon points="{pts(peaks + [(X1, 600), (X0, 600)])}" fill="{rock}"/>')
    for (x0, y0), (x, y), (x1, y1) in zip(peaks, peaks[1:], peaks[2:]):
        if y < 420:  # tall peaks get snow
            c = 0.28
            ground.append(f'<polygon points="{pts([(x, y), (x + (x1-x)*c, y + (y1-y)*c), (x + 6, y + 22), (x - 8, y + 16), (x + (x0-x)*c, y + (y0-y)*c)])}" fill="{snow}"/>')
    hills = mix('#2f5236', 0.38)
    ground.append(f'<path d="M{X0} 600 L{X0} 530 Q-150 480 -20 540 Q120 470 300 525 Q470 575 640 520 Q820 465 1000 530 Q1180 585 1350 515 Q1500 470 1620 520 Q1760 565 {X1} 505 L{X1} 600 Z" fill="{hills}"/>')
    ground.append(f'<rect x="{X0}" y="585" width="{X1 - X0}" height="515" fill="url(#side-ground)"/>')

    # stream: from the hills to the pond, widening as it comes closer
    path = [(340, 548), (300, 572), (372, 598), (338, 628), (440, 656), (540, 698)]
    left, right = [], []
    for i, (x, y) in enumerate(path):
        (xa, ya), (xb, yb) = path[max(i-1, 0)], path[min(i+1, len(path)-1)]
        n = math.hypot(xb - xa, yb - ya)
        nx, ny = -(yb - ya) / n, (xb - xa) / n
        w = 2 + 9 * i / (len(path) - 1)
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    ground.append(f'<polygon points="{pts(left + right[::-1])}" fill="#2f6f9e"/>')
    ground.append(f'<polyline class="flow" points="{pts(path)}" stroke="#7fc0ea" stroke-width="2.5" fill="none" stroke-linejoin="round"/>')

    # grass tufts, bigger as they come closer
    for i in range(150):
        x, y = random.uniform(X0, X1), random.uniform(600, 900)
        if ((x - PCX) / (PRX + 30)) ** 2 + ((y - PCY) / (PRY + 20)) ** 2 < 1:
            continue
        s = 0.6 + 1.2 * (y - 600) / 300
        ground.append(tuft(x, y, s, mix('#6fa356', K_MID * (900 - y) / 300)))

    # far row: small, hazy trees on the hills
    x = X0
    while x < X1:
        y = FAR_Y + random.uniform(-6, 6)
        items.append(put(x, y, random_tree((50, 78), K_FAR), 'grow', f'--d:{grow_delay(y):.1f}s', flip=random.random() < 0.5))
        x += random.uniform(48, 72)

    # mid row (leave room for the owl's tree)
    x = X0 + 20
    mid = []  # (x, index into items)
    while x < X1:
        if abs(x - OWL_X) > 70:
            y = MID_Y + random.uniform(-8, 8)
            mid.append((x, len(items)))
            items.append(put(x, y, random_tree((95, 130), K_MID), 'grow', f'--d:{grow_delay(y):.1f}s', flip=random.random() < 0.5))
        x += random.uniform(80, 115)
    inner, top = broadleaf(150, '#3d7a3f', '#6b4a2b', K_MID)
    items.append(put(OWL_X, MID_Y, inner, 'grow', f'--d:{grow_delay(MID_Y):.1f}s'))
    owl_y = MID_Y + top - 10
    items.append(peeker(OWL_X + 5, owl_y, MID_Y, owl_head(), 0, 55, 35, 21, 0.75))
    items.append(night_pose(OWL_X + 5, owl_y, MID_Y, owl_head(), 0.75, late=True))  # its tree is still a sapling at first

    # pond (between the mid and near rows), deer drinking, fish
    p = pond(PCX, PCY, PRX, PRY, 'side', 34, [(-210, 12), (-185, 22), (190, -8), (150, 20)],
             [(60, -6, 0), (-90, 12, 1.7), (-20, -18, 3.1)])
    muzzle = (DEER_X - 54.5 * DEER_S, DEER_Y - 29.8 * DEER_S)  # where the lowered head meets the water
    p.append(drink_ripple(muzzle[0], muzzle[1] + 8))
    items.append((PCY - PRY - 1, '<g>' + ''.join(p) + '</g>'))
    items.append((DEER_Y, deer(DEER_X, DEER_Y, 0.12, DEER_S)))
    items.append((PCY + 6, fish(PCX - 40, PCY + 6)))

    # near row: big, bright trees at the sides; bushes in front of the pond
    for x in (-250, -100, 55, 215, 340, 1450, 1585, 1730, 1870):
        y = NEAR_Y + random.uniform(-10, 10)
        items.append(put(x + random.uniform(-15, 15), y, random_tree((185, 235), K_NEAR), 'grow',
                         f'--d:{grow_delay(y):.1f}s', flip=random.random() < 0.5))
    for x in (640, 770, 905, 1020):
        y = 838 + random.uniform(-6, 6)
        items.append(put(x, y, bush(random.uniform(34, 46), random.choice(GREENS), K_NEAR), 'grow', f'--d:{grow_delay(y):.1f}s'))

    # scattered boulders, sized by distance
    for x, y in [(130, 690), (470, 745), (1240, 690), (1390, 760), (690, 655), (1530, 680), (300, 760)]:
        s = 14 + (y - 600) * 0.16
        items.append(put(x, y, boulder(s, random.choice(GREYS), K_MID * (900 - y) / 300)))

    # fox behind a near boulder, rabbit behind a near bush
    items.append(put(FOX_X, NEAR_Y, boulder(100, '#7b8088', K_NEAR)))
    items.append(peeker(FOX_X - 62, NEAR_Y - 34, NEAR_Y, fox_head(), 50, 8, 10, 17, 1.3))
    items.append(night_pose(FOX_X - 62, NEAR_Y - 34, NEAR_Y, fox_head(), 1.3))
    # (the bush is taller than the rabbit, ears and all, so it can hide completely)
    items.append(put(RABBIT_X, NEAR_Y, bush(80, '#4f8a3c', K_NEAR), 'grow', f'--d:{grow_delay(NEAR_Y):.1f}s'))
    items.append(peeker(RABBIT_X + 4, NEAR_Y - 72, NEAR_Y, rabbit_head(), 0, 61, 12, 19, 1.0))
    items.append(night_pose(RABBIT_X + 4, NEAR_Y - 72, NEAR_Y, rabbit_head(), 1.0))

    # ---- lightning: a storm cloud drifts over a mid-row tree, which is struck, falls, and later regrows
    sx_, si = min(mid, key=lambda t: abs(t[0] - STRIKE_X))
    key, g = items[si]
    g = re.sub(r'<ellipse [^>]*fill="rgba\(0,0,0,0\.28\)"/>', '', g, count=1)  # its ground shadow would rotate as it falls
    items[si] = (key, g.replace('<g class="grow"', '<g class="struck"><g class="grow"', 1) + '</g>')
    bolt = [(sx_ - 10, 322), (sx_ + 12, 380), (sx_ - 8, 410), (sx_ + 10, 470), (sx_ - 4, 500), (sx_ + 6, MID_Y - 100)]
    rain = ''.join(f'<path class="rain" style="animation-delay:{-random.uniform(0, 0.6):.2f}s" d="M{f1(dx)} 20 l-4 14" '
                   f'stroke="#9fb4c8" stroke-width="2" stroke-linecap="round"/>' for dx in range(-60, 70, 14))
    items.append((0, f'<g transform="translate({f1(sx_)} 300)"><g class="storm">{rain}{cloud(0.85, dark=True)}</g></g>'
                     f'<polyline class="bolt" points="{pts(bolt)}" fill="none" stroke="#fff6c2" stroke-width="4" stroke-linejoin="round"/>'))

    # ---- beaver: emerges from the pond, chews down a sapling, drags it onto the stream as a dam
    bx, by = BEAVER_TREE
    mx, my = DAM[0] + 60 - bx, DAM[1] + 1 - by  # the felled log's base ends up just right of the dam
    drag = f'--mx:{mx}px; --my:{my}px'
    inner, _ = broadleaf(115, '#5c9443', '#7a5533', 0.08)
    inner = inner[1:]  # no ground shadow: it would rotate with the falling tree
    items.append((by, f'<g transform="translate({bx} {by})"><g class="log-move" style="{drag}"><g class="log-fall">'
                      f'<g class="grow" style="--d:1.5s">{"".join(inner)}</g></g></g></g>'))
    chips = ''.join(f'<circle class="chip" style="animation-delay:{-i*0.13:.2f}s" cx="{f1(random.uniform(-6, 10))}" cy="{f1(random.uniform(-14, -4))}" '
                    f'r="2.2" fill="#d9b38c"/>' for i in range(5))
    items.append((by + 0.5, f'<g transform="translate({bx + 6} {by})"><g class="chips">{chips}</g></g>'))
    items.append((by + 4, beaver(bx + 40, by + 4, drag)))
    dam_x, dam_y = DAM
    dam = ''.join(f'<line x1="{f1(dam_x - 34 + i*7)}" y1="{f1(dam_y + random.uniform(-4, 4))}" x2="{f1(dam_x - 20 + i*7)}" '
                  f'y2="{f1(dam_y - 12 + random.uniform(-3, 3))}" stroke="#5e3f24" stroke-width="3" stroke-linecap="round"/>' for i in range(9))
    items.append((dam_y - 30, f'<ellipse class="dam-pool" cx="{dam_x - 44}" cy="{dam_y - 17}" rx="30" ry="7" fill="#2f6f9e"/>'))
    items.append((dam_y + 1, f'<g class="dam"><ellipse cx="{dam_x}" cy="{dam_y}" rx="36" ry="7" fill="#6b4a2b"/>{dam}</g>'))

    items.sort(key=lambda t: t[0])

    # ---- day and night: sky colour, dawn/dusk glows, and a darkening veil over the land
    sky_bg = [f'<rect class="daysky" x="{X0}" y="-260" width="{X1 - X0}" height="900"/>',
              f'<ellipse class="glow dawn" cx="60" cy="560" rx="900" ry="360" fill="url(#side-glow)"/>',
              f'<ellipse class="glow dusk" cx="1540" cy="560" rx="900" ry="360" fill="url(#side-glow)"/>']
    veil = f'<rect class="night" x="{X0}" y="-260" width="{X1 - X0}" height="1420" fill="#05070d"/>'
    flash = f'<rect class="flash" x="{X0}" y="-260" width="{X1 - X0}" height="1420" fill="#ffffff"/>'

    title = '<text x="800" y="140" text-anchor="middle" font-size="120" font-weight="700" class="a-fade" style="--d:0.1s">Ecosystems</text>'
    flock = birds(4, (150, 340))
    night_eyes = [  # positions match each animal's eyes in its night pose
        glowing_eyes([(DEER_X - 33 * DEER_S, DEER_Y - 76 * DEER_S)], 2.4, '#b8ff6a'),
        glowing_eyes([(FOX_X - 62 - 8 * 1.3, NEAR_Y - 34 - 2 * 1.3), (FOX_X - 62 + 8 * 1.3, NEAR_Y - 34 - 2 * 1.3)], 3.2, '#ffd84a'),
        glowing_eyes([(RABBIT_X + 4 - 6, NEAR_Y - 72 - 11), (RABBIT_X + 4 + 6, NEAR_Y - 72 - 11)], 2.8, '#ff9a6a'),
        glowing_eyes([(OWL_X + 5 - 8 * 0.75, owl_y - 6 * 0.75), (OWL_X + 5 + 8 * 0.75, owl_y - 6 * 0.75)], 3.2, '#FFD626', late=True)]

    return '\n'.join([
        '<svg class="canvas eco side" viewBox="0 0 1600 900" aria-label="Ecosystem from night to dawn, day and dusk: eyes glow in the dark, then rows of trees grow toward distant mountains around a pond; the sun arcs overhead, lightning fells a tree, a beaver builds a dam, animals peek out, a deer drinks, a skunk walks by and a fish jumps">',
        defs('side', '#26412d', '#3e6d3b'), SIDE_DEFS, *sky_bg,
        *sky('side', [(250, 0.9, 150, -30), (330, 0.65, 115, -80), (385, 0.8, 175, -130), (290, 0.55, 130, -50)]),
        *flock, *ground, *[s for _, s in items], skunk(-260, TRAIL_Y, 1860, TRAIL_Y, 1.4),
        veil, *night_eyes, flash, title, '</svg>'])


def main():
    text = QMD.read_text()
    pattern = re.compile(r'<svg class="canvas eco side".*?</svg>', re.S)
    if not pattern.search(text):
        raise SystemExit(f'No <svg class="canvas eco side"> block found in {QMD}')
    svg = side_scene()
    QMD.write_text(pattern.sub(lambda m: svg, text, count=1))
    print(f'Updated the Ecosystems scene in {QMD.name}')


if __name__ == '__main__':
    main()
