"""Data-driven demo program builders. Every program is executed during build.
Property of Justin Addam Higgins (JAH)."""

def _safe(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'").replace('\n', ' ')

def scale_demo(title, scale_denom, example_cm):
    """Miniature scale conversion: real cm -> model cm."""
    t = _safe(title)
    return ('scale-converter',
"""# Scale conversion — %s
# At 1:%d scale, divide real-world centimeters by %d.
SCALE = %d
real_cm = %s
model_cm = real_cm / SCALE
model_mm = model_cm * 10
print("Real object: %%s cm" %% real_cm)
print("At 1:%%d the model is %%.2f cm (%%.1f mm)" %% (SCALE, model_cm, model_mm))
# A 170 cm person at this scale:
print("A 170 cm person becomes %%.2f cm tall" %% (170 / SCALE))
""" % (t, scale_denom, scale_denom, scale_denom, example_cm),
    'Converts real-world sizes to miniature scale with true division.')

def squarecube_demo(title, real_h_m, giant_h_m, real_mass_kg):
    """Square-cube law for giant objects."""
    t = _safe(title)
    return ('square-cube-law',
"""# Square-cube law — %s
# Linear scale factor k: surface grows k^2, volume and mass grow k^3.
real_h, giant_h, real_mass = %s, %s, %s
k = giant_h / real_h
print("Linear scale factor: %%.1fx" %% k)
print("Surface area factor: %%.1fx" %% k**2)
print("Volume/mass factor: %%.1fx" %% k**3)
print("A %%.0f kg object at this size would mass %%.0f kg" %% (real_mass, real_mass * k**3))
print("Support strength (area-based) only grows %%.1fx — this is why giant builds need internal structure." %% k**2)
""" % (t, real_h_m, giant_h_m, real_mass_kg),
    'Applies the square-cube law to giant-scale builds.')

def pendulum_demo(title, length_m):
    """Pendulum period for kinetic art."""
    t = _safe(title)
    return ('pendulum-period',
"""# Pendulum timing — %s
# Period T = 2*pi*sqrt(L/g), g = 9.81 m/s^2.
import math
L = %s
g = 9.81
T = 2 * math.pi * math.sqrt(L / g)
print("Pendulum length: %%s m" %% L)
print("Full period: %%.2f seconds" %% T)
print("Beats per minute: %%.1f" %% (60 / (T / 2)))
print("Half-period (one swing): %%.2f seconds" %% (T / 2))
""" % (t, length_m),
    'Computes the true swing period of a pendulum at the given length.')

def polygon_demo(title, sides, side_len):
    """Polygon geometry for geometric art."""
    t = _safe(title)
    return ('polygon-geometry',
"""# Polygon geometry — %s
import math
n, s = %d, %s
interior = (n - 2) * 180 / n
exterior = 360 / n
area = n * s * s / (4 * math.tan(math.pi / n))
print("Sides: %%d, side length: %%s" %% (n, s))
print("Interior angle: %%.2f degrees" %% interior)
print("Exterior (turn) angle: %%.2f degrees" %% exterior)
print("Area: %%.2f square units" %% area)
print("Full rotation check: %%d x %%.2f = 360" %% (n, exterior))
""" % (t, sides, side_len),
    'Computes interior/exterior angles and area of a regular polygon.')

def radial_demo(title, rings, points_per_ring):
    """Radial mandala point layout."""
    t = _safe(title)
    return ('radial-layout',
"""# Radial layout — %s
import math
rings, per = %d, %d
print("Rings: %%d, points per ring: %%d" %% (rings, per))
total = 0
for r in range(1, rings + 1):
    pts = []
    for i in range(per):
        a = 2 * math.pi * i / per
        pts.append((round(r * math.cos(a), 3), round(r * math.sin(a), 3)))
    total += len(pts)
    print("Ring %%d (radius %%d): first point %%s, step angle %%.1f deg" %% (r, r, pts[0], 360 / per))
print("Total plotted points: %%d" %% total)
""" % (t, rings, points_per_ring),
    'Generates true radial coordinates for a symmetric design.')

def thirds_demo(title, w, h):
    """Rule-of-thirds composition grid."""
    t = _safe(title)
    return ('composition-grid',
"""# Rule-of-thirds grid — %s
W, H = %s, %s
xs = [W / 3, 2 * W / 3]
ys = [H / 3, 2 * H / 3]
print("Canvas: %%s x %%s" %% (W, H))
print("Vertical thirds at x =", [round(x, 1) for x in xs])
print("Horizontal thirds at y =", [round(y, 1) for y in ys])
print("Power points (intersections):")
for x in xs:
    for y in ys:
        print("  (%%.1f, %%.1f)" %% (x, y))
""" % (t, w, h),
    'Computes rule-of-thirds grid lines and power points for a canvas.')

def spec_demo(title, specs, derived):
    """Factual spec table + derived lines of python code (as strings)."""
    t = _safe(title)
    rows = '\n'.join('specs.append(("%s", "%s"))' % (_safe(k), _safe(str(v))) for k, v in specs)
    dlines = '\n'.join(derived)
    return ('spec-table',
"""# %s
specs = []
%s
print("%%-22s | %%s" %% ("SPECIFICATION", "VALUE"))
print("-" * 60)
for k, v in specs:
    print("%%-22s | %%s" %% (k, v))
%s
""" % (t, rows, dlines),
    'Prints the specification table with a derived computation.')

def list_demo(title, items, header):
    """Prints a titled list with numbering."""
    t = _safe(title)
    rows = '\n'.join('items.append("%s")' % _safe(i) for i in items)
    return ('checklist',
"""# %s
items = []
%s
print("%s")
for i, it in enumerate(items, 1):
    print("%%d. %%s" %% (i, it))
print("Total: %%d items" %% len(items))
""" % (t, rows, _safe(header)),
    'Prints the full item list with a count.')
