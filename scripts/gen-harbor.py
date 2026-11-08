import math, random
random.seed(7)
R = lambda a, b: random.uniform(a, b)
f = lambda v: f"{v:.1f}".rstrip('0').rstrip('.')
W, H, Q = 800, 1200, 712  # Q = quay line

def stroke(x, y, length, bulge, tilt, color, op):
    dy = length * tilt
    return (f'<path d="M{f(x)} {f(y)}q{f(length/2)} {f(-bulge)} {f(length)} {f(dy)}'
            f'q{f(-length/2)} {f(bulge*0.35)} {f(-length)} {f(-dy)}z" fill="{color}" opacity="{op}"/>')

def hill(fn):
    pts = ' '.join(f'L{x} {f(fn(x))}' for x in range(0, W + 1, 10))
    return f'M0 {f(fn(0))}{pts[pts.index(" ", 1):] if False else pts}V{H}H0Z'

back = lambda x: 902 + 10 * math.sin(x / 120)
mid = lambda x: 958 + 16 * math.sin(x / 150 + 1)
front = lambda x: 1056 + 18 * math.sin(x / 130 + 2.2)

out = []
A = out.append

# ---------- sky ----------
A('<rect width="800" height="760" fill="url(#h-sky)"/>')
A('<rect width="800" height="760" fill="url(#h-glow)"/>')
sky = []
for _ in range(260):
    y = R(0, 640); t = y / 640
    pal = ['#8fc2e0', '#6aa9d4', '#a9d3ea'] if t < 0.55 else ['#c4e0ec', '#f7e3c0', '#fbd9a8', '#f3eed8']
    sky.append(stroke(R(-60, 780), y, R(40, 120), R(4, 12), R(-0.25, 0.05), random.choice(pal), f(R(0.25, 0.5))))
A('<g>' + ''.join(sky) + '</g>')
A('<circle cx="430" cy="585" r="38" fill="#fff6d8"/>')

# clouds
def cloud(cx, cy, s):
    parts = [f'<ellipse cx="{f(cx+6*s)}" cy="{f(cy+14*s)}" rx="{f(120*s)}" ry="{f(20*s)}" fill="#cfe2ee"/>']
    for dx, dy, rx, ry in [(-70, 4, 60, 22), (-20, -10, 70, 32), (40, -4, 64, 26), (90, 6, 46, 18), (0, 8, 120, 20)]:
        parts.append(f'<ellipse cx="{f(cx+dx*s)}" cy="{f(cy+dy*s)}" rx="{f(rx*s)}" ry="{f(ry*s)}" fill="#fff" opacity=".9"/>')
    for _ in range(8):
        parts.append(stroke(cx + R(-90, 60) * s, cy + R(-20, 6) * s, R(30, 70) * s, R(3, 7) * s, R(-0.1, 0.05), '#fffaf0', '.7'))
    return ''.join(parts)
A('<g class="clouds">' + cloud(200, 170, 1.1) + cloud(590, 300, 0.85) + cloud(330, 450, 0.6) + cloud(720, 120, 0.7) + '</g>')

# gulls
gulls = ''.join(f'<path d="M{x} {y}q7 -7 14 0q7 -7 14 0" transform="scale({s})" transform-origin="{x} {y}"/>'
                for x, y, s in [(250, 330, 1), (290, 312, .8), (470, 230, .9), (510, 250, .7)])
A(f'<g class="gulls" fill="none" stroke="#34495e" stroke-width="2.2" stroke-linecap="round">{gulls}</g>')

# ---------- skyline ----------
far = ['<path d="M0 712V676h40v-14h30v14h44v-26h22v26h54v-10h36v10h44v-22h20v22h60v-14h40v14h54v-30h24v30h46v-12h38v12h50v-20h30v20h60v-16h40v16H800V712Z"/>']
# Heinrich-Hertz-Turm
far.append('<rect x="146" y="420" width="8" height="292"/><path d="M150 380V420" stroke="#9fb3c6" stroke-width="2"/>'
           '<ellipse cx="150" cy="470" rx="17" ry="7"/><rect x="138" y="472" width="24" height="12" rx="3"/><ellipse cx="150" cy="500" rx="11" ry="4"/>')
# St. Nikolai + Rathaus
far.append('<path d="M352 600L360 470 368 600z"/><rect x="348" y="598" width="24" height="114"/>'
           '<path d="M296 560l8-34 8 34z"/><rect x="292" y="558" width="24" height="154"/><rect x="250" y="640" width="110" height="72"/>')
A('<g fill="#a7bacb">' + ''.join(far) + '</g>')

mid_sky = []
# Speicherstadt
mid_sky.append('<rect x="20" y="640" width="190" height="84" fill="#9b4f3f"/><rect x="20" y="640" width="190" height="84" fill="url(#h-windows)"/>'
               '<path d="M20 640l30-28 30 28zM84 640l30-28 30 28zM148 640l31-28 31 28z" fill="#4b5a66"/>'
               '<rect x="34" y="604" width="10" height="20" fill="#6fa595"/>')
# Michel
mid_sky.append('<rect x="214" y="650" width="120" height="62" fill="#6f8aa0"/><rect x="258" y="560" width="34" height="152" fill="#7d97ab"/>'
               '<rect x="252" y="606" width="46" height="8" fill="#6f8aa0"/><rect x="265" y="526" width="20" height="36" fill="#8aa3b5"/>'
               '<path d="M264 528c0-15 4-23 11-34 7 11 11 19 11 34z" fill="#6fa595"/><path d="M275 494V452" stroke="#6fa595" stroke-width="2"/>'
               '<circle cx="275" cy="584" r="6" fill="#f3e9cf"/>')
# Elbphilharmonie
mid_sky.append('<rect x="470" y="650" width="180" height="62" fill="#8a6a5e"/><rect x="470" y="650" width="180" height="62" fill="url(#h-windows)" opacity=".6"/>'
               '<path d="M478 650V600Q514 560 552 584T612 566Q632 540 650 556V650Z" fill="url(#h-glass)"/>'
               '<g stroke="#fff" stroke-opacity=".4" stroke-width="1.5"><path d="M494 650V590M512 650V578M530 650V572M548 650V582M566 650V578M584 650V572M602 650V568M620 650V552M638 650V550"/></g>')
# container gantries
mid_sky.append('<g fill="none" stroke="#2f6f9a" stroke-width="5" stroke-linejoin="round">'
               '<path d="M660 712V600h44v112M660 640h44M642 600h96M704 600l26-30"/>'
               '<path d="M716 712V616h40v96M716 652h40M702 616h66"/></g>'
               '<path d="M378 712V610M352 610h72M378 610l-26 30M378 610l46 26" stroke="#3c4b57" stroke-width="3" fill="none"/>')
A('<g id="h-mid">' + ''.join(mid_sky) + '</g>')
A(f'<rect y="{Q}" width="800" height="12" fill="#4a5560"/>')

# ---------- water ----------
A(f'<rect y="{Q+12}" width="800" height="300" fill="url(#h-water)"/>')
A('<g mask="url(#h-fade-mask)" opacity=".35"><use href="#h-mid" transform="translate(0 1448) scale(1 -1)"/></g>')
water = [stroke(R(-40, 780), R(730, 930), R(50, 150), R(2, 5), R(-0.03, 0.03),
                random.choice(['#a9d3ea', '#2f6c96', '#d8ecf5', '#5d9cc2']), f(R(0.25, 0.5))) for _ in range(150)]
A('<g class="ripples">' + ''.join(water) + '</g>')
A('<g class="glint" fill="#fff3cf">' + ''.join(
    f'<rect x="{f(430-w/2)}" y="{y}" width="{w}" height="4" rx="2" opacity="{o}"/>'
    for y, w, o in [(732, 150, .7), (748, 116, .6), (766, 86, .5), (786, 60, .45), (808, 40, .35), (832, 24, .3)]) + '</g>')

# container ship
cols = ['#b5473a', '#d98a3d', '#2e7da6', '#3f8f5b', '#d9b23f', '#7a5a8c', '#c95f4e']
boxes = ''.join(f'<rect x="{20+i*17}" y="{-11-r*11}" width="16" height="10" fill="{random.choice(cols)}"/>'
                for r in range(3) for i in range(10) if not (r == 2 and random.random() < .35))
A('<g class="ship"><g transform="translate(0 792)">'
  f'<path d="M0 0H250L234 28H16Z" fill="#26394a"/><path d="M6 14H244L234 28H16Z" fill="#a8392f"/>{boxes}'
  '<rect x="198" y="-40" width="30" height="40" fill="#f2efe8"/><rect x="202" y="-34" width="22" height="5" fill="#35505f"/>'
  '<rect x="208" y="-52" width="8" height="12" fill="#26394a"/></g></g>')
# ferry
A('<g class="ferry"><g transform="translate(0 866)">'
  '<path d="M0 0h96l-12 20H10z" fill="#c8382f"/><rect x="14" y="-18" width="62" height="18" fill="#f4efe6"/>'
  '<rect x="24" y="-28" width="34" height="10" fill="#f4efe6"/>'
  '<g fill="#35505f"><rect x="20" y="-13" width="10" height="7"/><rect x="36" y="-13" width="10" height="7"/><rect x="52" y="-13" width="10" height="7"/></g>'
  '<path d="M-6 24h60M-18 30h40" stroke="#fff" stroke-opacity=".45" stroke-width="2" stroke-linecap="round"/></g></g>')

# ---------- green banks ----------
A('<path d="M0 893C150 872 300 890 440 908L440 918C300 902 150 884 0 905Z" fill="#ecd6a6"/>')
greens = {
    'back': (back, '#8dbf6e', ['#a3cf7e', '#7bb15e', '#b6d98d']),
    'mid': (mid, '#68a454', ['#7cb763', '#559348', '#8fc46c']),
    'front': (front, '#467f3f', ['#3a6e36', '#5a9a4c', '#2f5e2e']),
}
def bush_row(fn, xs, base_col):
    s = ''
    for x in xs:
        y = fn(x)
        for _ in range(6):
            s += f'<circle cx="{f(x+R(-14,14))}" cy="{f(y-R(4,16))}" r="{f(R(8,14))}" fill="{random.choice(base_col)}"/>'
    return s

def tree(x, base, size, cls):
    s = f'<g class="{cls}"><path d="M{f(x-5*size)} {f(base)}L{f(x-3*size)} {f(base-90*size)}h{f(6*size)}L{f(x+5*size)} {f(base)}z" fill="#5b4636"/>'
    cy = base - 120 * size
    for _ in range(26):
        a = R(0, 2 * math.pi); d = R(0, 55 * size)
        px, py = x + math.cos(a) * d * 1.1, cy + math.sin(a) * d * 0.8
        light = (px - x) / (60 * size) - (py - cy) / (60 * size)
        col = '#a6d27f' if light > 0.6 else '#7fb85f' if light > 0 else '#5b9a49' if light > -0.6 else '#3f7a3a'
        s += f'<circle cx="{f(px)}" cy="{f(py)}" r="{f(R(18,28)*size)}" fill="{col}"/>'
    for _ in range(14):
        s += stroke(x + R(-50, 30) * size, cy + R(-50, 30) * size, R(16, 30) * size, R(3, 6) * size, R(-0.3, 0.3), '#c3e39a', '.55')
    return s + '</g>'

for name in ['back', 'mid', 'front']:
    fn, base, pal = greens[name]
    A(f'<path d="{hill(fn)}" fill="{base}"/>')
    sts = []
    for _ in range(170 if name != 'back' else 110):
        x = R(-20, 790); top = fn(x)
        y = R(top + 4, min(top + 120, H))
        sts.append(stroke(x, y, R(18, 46), R(3, 7), R(-0.35, 0.1), random.choice(pal), f(R(0.45, 0.8))))
    A('<g>' + ''.join(sts) + '</g>')
    if name == 'mid':
        A(tree(655, mid(655) + 6, 0.8, 'sway'))
    if name == 'front':
        A(tree(175, front(175) + 20, 1.2, 'sway sway-slow'))
    # flowers on mid/front
    if name != 'back':
        fl = ''
        for _ in range(55 if name == 'mid' else 45):
            x = R(0, 800); top = fn(x); y = R(top + 8, top + 110)
            fl += f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(R(2,3.8))}" fill="{random.choice(["#fff8e7", "#f6d55c", "#f2a3b3", "#e2584b", "#fff8e7"])}"/>'
        A('<g>' + fl + '</g>')

# grass blades along the front ridge
blades = ''
for x in range(0, 801, 7):
    top = front(x) + R(-2, 4); h = R(14, 30); lean = R(-6, 6)
    blades += f'<path d="M{f(x)} {f(top+6)}q{f(lean/2)} {f(-h/2)} {f(lean)} {f(-h)}q{f(-lean/2+1.5)} {f(h/2)} 3 {f(h)}z" fill="{random.choice(["#3a6e36", "#5a9a4c", "#7cb763"])}"/>'
A('<g class="sway grass">' + blades + '</g>')

# ---------- foreground meadow (tall grass + stemmed flowers, swaying) ----------
def blade(x, base, h, lean, col):
    return (f'<path d="M{f(x)} {f(base)}q{f(lean*0.3)} {f(-h*0.55)} {f(lean)} {f(-h)}'
            f'q{f(-lean*0.55+2)} {f(h*0.5)} {f(4-lean*0.0)} {f(h)}z" fill="{col}"/>')

def flower(x, base, h, kind):
    lean = R(-10, 10); tx, ty = x + lean, base - h
    s = f'<path d="M{f(x)} {f(base)}q{f(lean*0.2)} {f(-h*0.5)} {f(lean)} {f(-h)}" stroke="#3f7a3a" stroke-width="2.2" fill="none"/>'
    s += stroke(x + lean * 0.3, base - h * 0.45, R(12, 18), 4, R(-0.6, -0.2) * random.choice([1, -1]), '#5a9a4c', '1')
    if kind == 'daisy':
        for k in range(8):
            a = k * 45
            s += f'<ellipse cx="{f(tx)}" cy="{f(ty-6)}" rx="2.6" ry="6.5" fill="#fffaf0" transform="rotate({a} {f(tx)} {f(ty)})"/>'
        s += f'<circle cx="{f(tx)}" cy="{f(ty)}" r="3.6" fill="#f2c335"/>'
    elif kind == 'poppy':
        for dx, dy in [(-4, 0), (4, 0), (0, -4), (0, 3)]:
            s += f'<circle cx="{f(tx+dx)}" cy="{f(ty+dy)}" r="6" fill="#d9483b"/>'
        s += f'<circle cx="{f(tx-1)}" cy="{f(ty-2)}" r="3" fill="#ef6a55"/><circle cx="{f(tx)}" cy="{f(ty)}" r="2.2" fill="#2b2b2b"/>'
    elif kind == 'cornflower':
        for k in range(7):
            a = math.radians(k * 360 / 7)
            s += f'<circle cx="{f(tx+math.cos(a)*4.5)}" cy="{f(ty+math.sin(a)*4.5)}" r="2.8" fill="#4f7fd1"/>'
        s += f'<circle cx="{f(tx)}" cy="{f(ty)}" r="2.4" fill="#2f4f9a"/>'
    else:  # buttercup cluster
        for dx, dy in [(0, 0), (-7, 8), (6, 6)]:
            s += f'<circle cx="{f(tx+dx)}" cy="{f(ty+dy)}" r="3.4" fill="#f4cf3d"/>'
    return s

groups = {'sway-a': [], 'sway-b': [], 'sway-c': []}
keys = list(groups)
for x in range(-10, 811, 5):
    base = H + 4
    groups[random.choice(keys)].append(blade(x + R(-3, 3), base, R(50, 120), R(-18, 18), random.choice(['#2f5e2e', '#3a6e36', '#4b8a44', '#5a9a4c', '#7cb763'])))
for _ in range(34):
    x = R(20, 780)
    groups[random.choice(keys)].append(flower(x, H + 4, R(70, 150), random.choice(['daisy', 'daisy', 'poppy', 'cornflower', 'buttercup'])))
for x in range(-5, 811, 9):  # short front tuft row
    groups[random.choice(keys)].append(blade(x, H + 4, R(24, 50), R(-10, 10), random.choice(['#2f5e2e', '#3a6e36'])))
for k, items in groups.items():
    A(f'<g class="sway {k}">' + ''.join(items) + '</g>')

A('<rect width="800" height="1200" filter="url(#h-grain)" opacity=".12" style="mix-blend-mode:multiply"/>')
A('<rect width="800" height="1200" fill="url(#h-vignette)"/>')

defs = '''<defs>
<linearGradient id="h-sky" x1="0" y1="0" x2="0" y2="740" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#5b9fd0"/><stop offset=".45" stop-color="#9fcde6"/><stop offset=".82" stop-color="#f3e3c0"/><stop offset="1" stop-color="#f6c89a"/></linearGradient>
<linearGradient id="h-water" x1="0" y1="724" x2="0" y2="1000" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#8dbcd2"/><stop offset=".5" stop-color="#4a87ad"/><stop offset="1" stop-color="#2b5f86"/></linearGradient>
<linearGradient id="h-glass" x1="0" y1="550" x2="0" y2="650" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#a9cfe2"/><stop offset="1" stop-color="#f1d6b0"/></linearGradient>
<radialGradient id="h-glow" cx="430" cy="585" r="320" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff1c4" stop-opacity=".95"/><stop offset="1" stop-color="#fff1c4" stop-opacity="0"/></radialGradient>
<radialGradient id="h-vignette" cx="400" cy="600" r="760" gradientUnits="userSpaceOnUse"><stop offset=".6" stop-color="#1b2a33" stop-opacity="0"/><stop offset="1" stop-color="#1b2a33" stop-opacity=".22"/></radialGradient>
<linearGradient id="h-fade" x1="0" y1="724" x2="0" y2="880" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="h-fade-mask"><rect y="724" width="800" height="160" fill="url(#h-fade)"/></mask>
<filter id="h-grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="3"/><feColorMatrix type="saturate" values="0"/></filter>
<pattern id="h-windows" width="14" height="16" patternUnits="userSpaceOnUse"><rect x="3" y="3" width="6" height="9" fill="#3a2a2a" opacity=".55"/></pattern>
</defs>'''

svg = f'<svg viewBox="0 0 800 1200" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{defs}{"".join(out)}</svg>'

astro = f'''---
// Painted Hamburg at golden hour, generated by scripts/gen-harbor.py (run from repo root) (brushstrokes are random but fixed):
// Heinrich-Hertz-Turm, Rathaus, St. Nikolai, Michel, Speicherstadt, Elbphilharmonie, container
// gantries, a container ship and a HADAG ferry on the Elbe, green banks with trees, tall grass and wildflowers.
---

<div class="harbor" role="img" aria-label="A painted illustration of Hamburg at golden hour: the TV tower, the Michel and the Elbphilharmonie above the harbour, a container ship and a ferry on the Elbe, and green riverbanks with trees, tall grass and wildflowers in front.">
  {svg}
</div>

<style>
  .harbor, .harbor :global(svg) {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
  .harbor :global(.sway) {{ transform-box: fill-box; transform-origin: 50% 100%; }}
  @media (prefers-reduced-motion: no-preference) {{
    .harbor :global(.clouds) {{ animation: drift 30s ease-in-out infinite alternate; }}
    .harbor :global(.gulls) {{ animation: glide 9s ease-in-out infinite alternate; }}
    .harbor :global(.ripples) {{ animation: shimmer 6s ease-in-out infinite alternate; }}
    .harbor :global(.glint) {{ animation: glint 3.4s ease-in-out infinite alternate; transform-box: fill-box; transform-origin: center; }}
    .harbor :global(.ship) {{ animation: ship 140s linear -55s infinite; }}
    .harbor :global(.ferry) {{ animation: ferry 60s linear -22s infinite; }}
    .harbor :global(.sway) {{ animation: sway 5s ease-in-out infinite alternate; }}
    .harbor :global(.sway-slow) {{ animation-duration: 7s; }}
    .harbor :global(.grass) {{ animation-duration: 3.6s; }}
    .harbor :global(.sway-a) {{ animation-duration: 3.2s; }}
    .harbor :global(.sway-b) {{ animation-duration: 4.1s; animation-delay: -1.3s; }}
    .harbor :global(.sway-c) {{ animation-duration: 3.7s; animation-delay: -2.2s; }}
      }}
  @keyframes drift {{ to {{ transform: translateX(80px); }} }}
  @keyframes glide {{ from {{ transform: translate(-20px, 6px); }} to {{ transform: translate(40px, -12px); }} }}
  @keyframes shimmer {{ from {{ transform: translateX(-12px); }} to {{ transform: translateX(12px); }} }}
  @keyframes glint {{ from {{ opacity: .7; transform: scaleX(.92); }} to {{ opacity: 1; transform: scaleX(1.05); }} }}
  @keyframes ship {{ from {{ transform: translateX(820px); }} to {{ transform: translateX(-300px); }} }}
  @keyframes ferry {{ from {{ transform: translateX(-140px); }} to {{ transform: translateX(840px); }} }}
  @keyframes sway {{ from {{ transform: rotate(-1.2deg); }} to {{ transform: rotate(1.2deg); }} }}
</style>
'''
open('src/components/Harbor.astro', 'w').write(astro)
print(len(astro))
