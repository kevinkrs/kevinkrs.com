# Generates src/components/Harbor.astro: a painted, poster-style Hamburg harbour.
# Run from the repo root: python3 scripts/gen-harbor.py  (seeded, so output is stable)
import math, random
random.seed(11)
R = lambda a, b: random.uniform(a, b)
C = random.choice
f = lambda v: f"{v:.1f}".rstrip('0').rstrip('.')
W, H, Q = 800, 1200, 716  # Q = quay line
out = []
A = out.append

def stroke(x, y, length, bulge, tilt, color, op=1):
    dy = length * tilt
    return (f'<path d="M{f(x)} {f(y)}q{f(length/2)} {f(-bulge)} {f(length)} {f(dy)}'
            f'q{f(-length/2)} {f(bulge*0.35)} {f(-length)} {f(-dy)}z" fill="{color}" opacity="{op}"/>')

def hill(fn):
    return f'M0 {f(fn(0))}' + ''.join(f'L{x} {f(fn(x))}' for x in range(0, W + 1, 10)) + f'V{H}H0Z'

# ---------- sky ----------
A('<rect width="800" height="760" fill="url(#h-sky)"/>')
A('<g>' + ''.join(stroke(R(-80, 780), R(0, 680), R(60, 160), R(3, 8), R(-0.3, -0.15), C(['#fff', '#d6e9f5', '#a9cde8']), f(R(.3, .6))) for _ in range(150)) + '</g>')

def cloud(cx, cy, s):
    blobs = [(R(-130, 130) * s, R(-40, 20) * s, R(26, 52) * s) for _ in range(16)]
    blobs += [(dx * s, 20 * s, 40 * s) for dx in range(-120, 121, 40)]  # flat-ish bottom
    edge = ''.join(f'<circle cx="{f(cx+dx)}" cy="{f(cy+dy)}" r="{f(r+3.5)}"/>' for dx, dy, r in blobs)
    body = ''.join(f'<circle cx="{f(cx+dx)}" cy="{f(cy+dy)}" r="{f(r)}"/>' for dx, dy, r in blobs)
    return f'<g fill="#fff">{edge}</g><g fill="#f7f1e3">{body}</g>'
A('<g class="clouds">' + cloud(150, 220, 1.2) + cloud(650, 330, 1.05) + cloud(430, 540, 0.75) + cloud(760, 110, 0.8) + '</g>')
A('<g class="gulls" fill="none" stroke="#2c3e50" stroke-width="2.2" stroke-linecap="round">' + ''.join(
    f'<path d="M{x} {y}q7 -7 14 0q7 -7 14 0"/>' for x, y in [(300, 300), (338, 286), (520, 210), (556, 226)]) + '</g>')

# ---------- skyline ----------
WIN = {  # body colour -> window pattern id
    '#1f3b63': 'h-win-light', '#2c5f9e': 'h-win-light', '#3f8f5b': 'h-win-light',
    '#f4f0e6': 'h-win-blue', '#e6c36a': 'h-win-dark', '#d9604a': 'h-win-light', '#9bc7e6': 'h-win-blue',
}
def block(x, w, h, col=None, roof=None):
    col = col or C(list(WIN))
    s = f'<rect x="{f(x)}" y="{f(Q-h)}" width="{f(w)}" height="{f(h)}" fill="{col}"/><rect x="{f(x)}" y="{f(Q-h)}" width="{f(w)}" height="{f(h)}" fill="url(#{WIN[col]})"/>'
    if roof:
        s += f'<rect x="{f(x-2)}" y="{f(Q-h-5)}" width="{f(w+4)}" height="6" fill="{roof}"/>'
    return s

sky = []
# TV tower
sky.append('<rect x="128" y="380" width="10" height="336" fill="#cfd8e0"/><path d="M133 330V380" stroke="#cfd8e0" stroke-width="2.5"/>'
           '<rect x="114" y="430" width="38" height="16" rx="5" fill="#3c4b57"/><rect x="118" y="446" width="30" height="8" fill="#e8eef3"/>'
           '<rect x="120" y="470" width="26" height="6" rx="3" fill="#3c4b57"/>')
# back row of colourful blocks
x = 30
while x < 780:
    w = R(34, 62)
    sky.append(block(x, w, R(70, 150), roof=C([None, '#d9433a', '#4f9c84', None])))
    x += w + R(-6, 6)
# Rathaus + St. Nikolai
sky.append('<rect x="330" y="560" width="26" height="156" fill="#e6cf9c"/><rect x="330" y="560" width="26" height="156" fill="url(#h-win-dark)"/>'
           '<path d="M328 562l15-46 15 46z" fill="#4f9c84"/><path d="M343 516V496" stroke="#4f9c84" stroke-width="2"/>'
           '<path d="M404 610L414 450 424 610z" fill="#2c3e50"/><rect x="400" y="606" width="28" height="110" fill="#3b4c5c"/>')
A('<g>' + ''.join(sky) + '</g>')

front = []
# Speicherstadt
front.append('<rect x="20" y="636" width="200" height="80" fill="#b5523e"/><rect x="20" y="636" width="200" height="80" fill="url(#h-win-dark)"/>'
             '<path d="M20 636l32-30 32 30zM88 636l32-30 32 30zM156 636l32-30 32 30z" fill="#2f4858"/>'
             '<rect x="114" y="590" width="12" height="24" fill="#4f9c84"/><path d="M112 592l8-14 8 14z" fill="#4f9c84"/>')
# Michel
front.append('<rect x="240" y="650" width="110" height="66" fill="#c45a44"/><rect x="240" y="650" width="110" height="66" fill="url(#h-win-dark)"/>'
             '<rect x="276" y="548" width="38" height="168" fill="#c45a44"/><rect x="270" y="600" width="50" height="8" fill="#f4f0e6"/>'
             '<rect x="284" y="510" width="22" height="40" fill="#4f9c84"/><path d="M283 512c0-16 5-25 12-37 7 12 12 21 12 37z" fill="#4f9c84"/>'
             '<path d="M295 475V430" stroke="#4f9c84" stroke-width="2.5"/><circle cx="295" cy="574" r="7" fill="#f6e7b8"/>')
# Elbphilharmonie
front.append('<rect x="470" y="646" width="190" height="70" fill="#a8533f"/><rect x="470" y="646" width="190" height="70" fill="url(#h-win-dark)"/>'
             '<path d="M478 646V596Q516 556 556 580T618 562Q640 534 660 552V646Z" fill="#6fa9d6"/>'
             '<path d="M478 596Q516 556 556 580T618 562Q640 534 660 552" stroke="#fff" stroke-width="4" fill="none"/>'
             '<g stroke="#fff" stroke-opacity=".7" stroke-width="1.6"><path d="M478 606H660M478 620H660M478 634H660"/></g>'
             '<g stroke="#5f9ccc" stroke-width="1.4"><path d="M500 646V588M524 646V572M548 646V576M572 646V576M596 646V570M620 646V560M644 646V548"/></g>')
# cranes
front.append('<g fill="none" stroke-width="5" stroke-linejoin="round"><path d="M672 716V604h42v112M672 644h42M654 604h94M714 604l24-30" stroke="#2c6fb7"/>'
             '<path d="M726 716V622h36v94M726 656h36M712 622h62" stroke="#d9433a"/></g>')
A('<g id="h-front">' + ''.join(front) + '</g>')

BUSH = ['#f2a0b5', '#d9433a', '#f1c04a', '#5aa04a', '#8cc152', '#2f6e3a', '#e8789a', '#3f9a6a']
DARK = {'#f2a0b5': '#d9708c', '#d9433a': '#a82c25', '#f1c04a': '#d39a22', '#5aa04a': '#2f6e3a',
        '#8cc152': '#5aa04a', '#2f6e3a': '#1d4a26', '#e8789a': '#c4507a', '#3f9a6a': '#25704a'}
def bush(x, y, w, h, col=None):
    col = col or C(BUSH)
    s = f'<path d="M{f(x-w/2)} {f(y)}A{f(w/2)} {f(h)} 0 0 1 {f(x+w/2)} {f(y)}Z" fill="{col}"/>'
    lines = ''.join(f'M{f(x)} {f(y-2)}L{f(x+math.cos(a)*w*0.36)} {f(y-2-math.sin(a)*h*0.72)}'
                    for a in [math.radians(d) for d in (35, 65, 90, 115, 145)])
    return s + f'<path d="{lines}" stroke="{DARK[col]}" stroke-width="2" stroke-linecap="round" fill="none"/>'

# quay-side bushes in front of the buildings
qb = sorted([(R(10, 790), R(30, 70)) for _ in range(34)], key=lambda t: -t[1])
A('<g>' + ''.join(bush(x, Q + 4, w, w * R(0.45, 0.65)) for x, w in qb) + '</g>')
A(f'<rect y="{Q+2}" width="800" height="10" fill="#2f4858"/>')

# ---------- water ----------
A(f'<rect y="{Q+12}" width="800" height="300" fill="url(#h-water)"/>')
A(f'<g mask="url(#h-fade-mask)" opacity=".3"><use href="#h-front" transform="translate(0 {2*Q+20}) scale(1 -1)"/></g>')
A('<g class="ripples">' + ''.join(stroke(R(-40, 780), R(736, 930), R(50, 150), R(2, 5), R(-0.03, 0.03),
    C(['#a9d3ea', '#3a78ae', '#d8ecf5', '#6aa8d6']), f(R(.3, .55))) for _ in range(140)) + '</g>')
cols = ['#d9433a', '#f1c04a', '#2c6fb7', '#3f8f5b', '#e8789a', '#f08a3c', '#1f3b63']
boxes = ''.join(f'<rect x="{20+i*17}" y="{-11-r*11}" width="16" height="10" fill="{C(cols)}"/>'
                for r in range(3) for i in range(10) if not (r == 2 and random.random() < .35))
A('<g class="ship"><g transform="translate(0 800)"><path d="M0 0H250L234 28H16Z" fill="#1f3b63"/><path d="M6 14H244L234 28H16Z" fill="#d9433a"/>'
  f'{boxes}<rect x="198" y="-40" width="30" height="40" fill="#f4f0e6"/><rect x="202" y="-34" width="22" height="5" fill="#2c3e50"/>'
  '<rect x="208" y="-52" width="8" height="12" fill="#1f3b63"/></g></g>')
A('<g class="ferry"><g transform="translate(0 872)"><path d="M0 0h96l-12 20H10z" fill="#d9433a"/><rect x="14" y="-18" width="62" height="18" fill="#f4f0e6"/>'
  '<rect x="24" y="-28" width="34" height="10" fill="#f4f0e6"/><g fill="#2c3e50"><rect x="20" y="-13" width="10" height="7"/><rect x="36" y="-13" width="10" height="7"/>'
  '<rect x="52" y="-13" width="10" height="7"/></g><path d="M-6 24h60M-18 30h40" stroke="#fff" stroke-opacity=".5" stroke-width="2" stroke-linecap="round"/></g></g>')

# ---------- banks ----------
bank = lambda x: 905 + 10 * math.sin(x / 110)
field = lambda x: 965 + 26 * math.sin(x / 170 + 0.6)
meadow = lambda x: 1060 - 0.09 * x + 14 * math.sin(x / 90)

def tree(x, base, s, crown):
    t = f'<g class="sway"><path d="M{f(x-5*s)} {f(base)}L{f(x-2.5*s)} {f(base-80*s)}h{f(5*s)}L{f(x+5*s)} {f(base)}z" fill="#6b4a33"/>'
    cy = base - 110 * s
    t += ''.join(f'<circle cx="{f(x+R(-40,40)*s)}" cy="{f(cy+R(-36,30)*s)}" r="{f(R(22,32)*s)}" fill="{crown[0]}"/>' for _ in range(9))
    t += ''.join(f'<circle cx="{f(x+R(-20,40)*s)}" cy="{f(cy+R(-40,10)*s)}" r="{f(R(14,22)*s)}" fill="{crown[1]}"/>' for _ in range(5))
    t += ''.join(stroke(x + R(-40, 30) * s, cy + R(-40, 30) * s, R(14, 24) * s, R(3, 5) * s, R(-0.5, 0.5), crown[2], '.8') for _ in range(10))
    return t + '</g>'

A(f'<path d="{hill(bank)}" fill="#7cbd55"/>')
A('<g>' + ''.join(bush(x, bank(x) + 8, w, w * .55) for x, w in [(260, 46), (300, 34), (440, 52), (500, 38), (560, 44)]) + '</g>')
A(tree(380, bank(380) + 8, 0.7, ('#2f6e3a', '#3f9a6a', '#8cc152')))
A(tree(620, bank(620) + 8, 0.85, ('#e8789a', '#f2a0b5', '#fde3ea')))

A(f'<path d="{hill(field)}" fill="#5f9e3c"/>')
stripes = ''.join(f'<path d="M{x} {f(field(x)+4)}Q{x+120} {f(field(x)+60)} {x+260} {H}" stroke="#4e8a31" stroke-width="7" fill="none" opacity=".7"/>'
                  for x in range(-260, 800, 36))
A(f'<clipPath id="h-field-clip"><path d="{hill(field)}"/></clipPath><g clip-path="url(#h-field-clip)">{stripes}</g>')
A(tree(150, field(150) + 14, 1.15, ('#2f6e3a', '#5aa04a', '#a6d27f')))
A(tree(700, field(700) + 10, 1.0, ('#25704a', '#3f9a6a', '#b6e0a0')))
A('<g>' + ''.join(bush(x, field(x) + 12, w, w * .55) for x, w in [(60, 56), (250, 48), (300, 40), (560, 52), (610, 40), (780, 50)]) + '</g>')

A(f'<path d="{hill(meadow)}" fill="#e8c25a"/>')
A('<g>' + ''.join(stroke(R(-20, 790), R(meadow(400) - 20, H), R(20, 50), R(3, 6), R(-0.4, 0.1), C(['#f1d27a', '#d9a83e', '#8cc152']), f(R(.5, .9))) for _ in range(120)) + '</g>')

# ---------- foreground: wheat, grass, big flowers, bees ----------
def wheat(x, base, h):
    lean = R(-14, 14); tx, ty = x + lean, base - h
    s = f'<path d="M{f(x)} {f(base)}q{f(lean*.2)} {f(-h*.5)} {f(lean)} {f(-h)}" stroke="#d9963a" stroke-width="2" fill="none"/>'
    for k in range(6):
        yy = ty + k * 7
        for side in (-1, 1):
            s += f'<ellipse cx="{f(tx+side*4)}" cy="{f(yy)}" rx="3" ry="6.5" fill="#efa93c" transform="rotate({side*22} {f(tx+side*4)} {f(yy)})"/>'
    s += f'<path d="M{f(tx)} {f(ty-4)}v38" stroke="#c4542f" stroke-width="1.6" stroke-dasharray="3 4"/>'
    return s

def blade(x, base, h, lean, col):
    return f'<path d="M{f(x)} {f(base)}q{f(lean*.3)} {f(-h*.55)} {f(lean)} {f(-h)}q{f(-lean*.55+2)} {f(h*.5)} 5 {f(h)}z" fill="{col}"/>'

def bloom(x, y, r, petal, center, n=8):
    s = ''.join(f'<ellipse cx="{f(x)}" cy="{f(y-r*.55)}" rx="{f(r*.32)}" ry="{f(r*.55)}" fill="{petal}" transform="rotate({k*360/n:.0f} {f(x)} {f(y)})"/>' for k in range(n))
    s += ''.join(f'<path d="M{f(x)} {f(y)}L{f(x)} {f(y-r*.7)}" stroke="{DARK.get(petal, "#000")}" stroke-opacity=".5" stroke-width="1.5" transform="rotate({k*360/n:.0f} {f(x)} {f(y)})"/>' for k in range(n))
    return s + f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r*.28)}" fill="{center}"/>'

DARK.update({'#c2307a': '#8d1f58', '#fffaf0': '#d8cdb8'})
groups = {'sway-a': [], 'sway-b': [], 'sway-c': []}
G = lambda: groups[C(list(groups))]
for x in range(-10, 811, 6):
    G().append(blade(x + R(-3, 3), H + 4, R(60, 150), R(-22, 22), C(['#2f6e3a', '#3f8f3a', '#5aa04a', '#8cc152', '#1d4a26'])))
for _ in range(28):
    G().append(wheat(R(0, 800), H + 4, R(110, 210)))
for _ in range(10):  # daisies and poppies on stems
    x, h = R(40, 760), R(60, 140)
    G().append(f'<path d="M{f(x)} {H+4}V{f(H-h)}" stroke="#2f6e3a" stroke-width="2.4"/>' +
               (bloom(x, H - h, 22, '#fffaf0', '#f1c04a') if random.random() < .5 else bloom(x, H - h, 16, '#d9433a', '#2c2c2c', 6)))
groups['sway-b'].append('<path d="M60 1210L64 1110" stroke="#2f6e3a" stroke-width="5"/>' + bloom(64, 1110, 74, '#d9433a', '#f1c04a', 7))
groups['sway-c'].append('<path d="M236 1210L232 1150" stroke="#2f6e3a" stroke-width="4"/>' + bloom(232, 1150, 50, '#c2307a', '#f1c04a', 10))
groups['sway-a'].append('<path d="M740 1210L736 1164" stroke="#2f6e3a" stroke-width="3"/>' + bloom(736, 1164, 26, '#fffaf0', '#d9433a', 12))
for x in range(-5, 811, 9):
    G().append(blade(x, H + 4, R(24, 54), R(-10, 10), C(['#1d4a26', '#2f6e3a'])))
for k, items in groups.items():
    A(f'<g class="sway {k}">' + ''.join(items) + '</g>')

bees = ''.join(f'<g class="bee b{i}" transform="translate({x} {y}) scale(1.7)"><ellipse rx="5" ry="3.6" fill="#f1c04a"/>'
               '<path d="M-1.5 -3.4v6.8M2 -3.2v6.4" stroke="#2c2c2c" stroke-width="1.6"/><circle cx="-5" r="2.2" fill="#2c2c2c"/>'
               '<ellipse cx="0" cy="-5.5" rx="3.4" ry="2.2" fill="#fff" opacity=".9"/><ellipse cx="3" cy="-5" rx="2.6" ry="1.8" fill="#fff" opacity=".8"/></g>'
               for i, (x, y) in enumerate([(130, 1050), (300, 1100), (200, 1000), (690, 1110), (560, 1060)]))
A(bees)

A('<rect width="800" height="1200" filter="url(#h-grain)" opacity=".14" style="mix-blend-mode:multiply"/>')

defs = '''<defs>
<linearGradient id="h-sky" x1="0" y1="0" x2="0" y2="740" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#78acd8"/><stop offset=".7" stop-color="#93c0e2"/><stop offset="1" stop-color="#c3dfee"/></linearGradient>
<linearGradient id="h-water" x1="0" y1="728" x2="0" y2="1000" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#8cc0e2"/><stop offset=".5" stop-color="#4f8fc6"/><stop offset="1" stop-color="#2f6aa3"/></linearGradient>
<linearGradient id="h-fade" x1="0" y1="728" x2="0" y2="880" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="h-fade-mask"><rect y="728" width="800" height="160" fill="url(#h-fade)"/></mask>
<filter id="h-grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="3"/><feColorMatrix type="saturate" values="0"/></filter>
<pattern id="h-win-light" width="10" height="12" patternUnits="userSpaceOnUse"><circle cx="5" cy="6" r="1.8" fill="#f4f0e6" opacity=".85"/></pattern>
<pattern id="h-win-blue" width="10" height="12" patternUnits="userSpaceOnUse"><circle cx="5" cy="6" r="1.8" fill="#2c5f9e"/></pattern>
<pattern id="h-win-dark" width="12" height="14" patternUnits="userSpaceOnUse"><rect x="4" y="4" width="4" height="7" rx="1" fill="#2c2c2c" opacity=".55"/></pattern>
</defs>'''

svg = f'<svg viewBox="0 0 800 1200" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{defs}{"".join(out)}</svg>'

astro = f'''---
// Painted Hamburg harbour, generated by scripts/gen-harbor.py (run from repo root). Do not edit by hand.
---

<div class="harbor" role="img" aria-label="A colourful painted illustration of Hamburg: the TV tower, the Michel, the Rathaus and the Elbphilharmonie behind rows of flowering bushes, a container ship and a ferry on the Elbe, and green fields, trees, wheat, big flowers and bees in front.">
  {svg}
</div>

<style>
  .harbor, .harbor :global(svg) {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
  .harbor :global(.sway) {{ transform-box: fill-box; transform-origin: 50% 100%; }}
  @media (prefers-reduced-motion: no-preference) {{
    .harbor :global(.clouds) {{ animation: drift 30s ease-in-out infinite alternate; }}
    .harbor :global(.gulls) {{ animation: glide 9s ease-in-out infinite alternate; }}
    .harbor :global(.ripples) {{ animation: shimmer 6s ease-in-out infinite alternate; }}
    .harbor :global(.ship) {{ animation: ship 140s linear -55s infinite; }}
    .harbor :global(.ferry) {{ animation: ferry 60s linear -22s infinite; }}
    .harbor :global(.sway) {{ animation: sway 5s ease-in-out infinite alternate; }}
    .harbor :global(.sway-a) {{ animation-duration: 3.2s; }}
    .harbor :global(.sway-b) {{ animation-duration: 4.1s; animation-delay: -1.3s; }}
    .harbor :global(.sway-c) {{ animation-duration: 3.7s; animation-delay: -2.2s; }}
    .harbor :global(.bee) {{ animation: buzz 2.4s ease-in-out infinite alternate; }}
    .harbor :global(.b1) {{ animation-duration: 1.9s; animation-delay: -.6s; }}
    .harbor :global(.b2) {{ animation-duration: 2.8s; animation-delay: -1.2s; }}
    .harbor :global(.b3) {{ animation-duration: 2.1s; animation-delay: -.3s; }}
    .harbor :global(.b4) {{ animation-duration: 2.6s; animation-delay: -1.7s; }}
  }}
  @keyframes drift {{ to {{ transform: translateX(80px); }} }}
  @keyframes glide {{ from {{ transform: translate(-20px, 6px); }} to {{ transform: translate(40px, -12px); }} }}
  @keyframes shimmer {{ from {{ transform: translateX(-12px); }} to {{ transform: translateX(12px); }} }}
  @keyframes ship {{ from {{ transform: translateX(820px); }} to {{ transform: translateX(-300px); }} }}
  @keyframes ferry {{ from {{ transform: translateX(-140px); }} to {{ transform: translateX(840px); }} }}
  @keyframes sway {{ from {{ transform: rotate(-1.2deg); }} to {{ transform: rotate(1.2deg); }} }}
  @keyframes buzz {{ 0% {{ translate: 0 0; }} 50% {{ translate: 14px -10px; }} 100% {{ translate: -10px 6px; }} }}
</style>
'''
open('src/components/Harbor.astro', 'w').write(astro)
print(len(astro))
