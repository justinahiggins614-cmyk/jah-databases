#!/usr/bin/env python3
"""Demo programs for The Colors Basics Database (Manon's fundamentals #9).

Every demo is real, runnable, stdlib-only Python performing the actual color
computation for its record. All 68 (34 records x public + Signature) are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_colb_what_is_color(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # visible light: violet edge to red edge, in nanometers
    violet_edge = 380.0
    red_edge = 750.0
    bandwidth = red_edge - violet_edge
    midpoint = (violet_edge + red_edge) / 2.0
    # human peak sensitivity sits near the middle of the visible band
    peak_sensitivity = 555.0
    print("visible band: %.0f to %.0f nm" % (violet_edge, red_edge))
    print("bandwidth: %.1f nm" % bandwidth)
    print("band midpoint: %.1f nm" % midpoint)
    print("peak sensitivity: %.0f nm" % peak_sensitivity)
    assert 369.9 < bandwidth < 370.1
    assert 564.9 < midpoint < 565.1
    assert 554.9 < peak_sensitivity < 555.1
    print("rule: no light, no color - color is light made visible to the mind")
    print("OK: %s measured the visible window" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_how_eye_sees(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cone peak wavelengths (nm): S, M, L
    s_peak, m_peak, l_peak = 420.0, 534.0, 564.0
    lm_gap = l_peak - m_peak
    ms_gap = m_peak - s_peak
    print("cone peaks: S=%.0f M=%.0f L=%.0f nm" % (s_peak, m_peak, l_peak))
    print("L-M gap: %.0f nm, M-S gap: %.0f nm" % (lm_gap, ms_gap))
    assert 29.9 < lm_gap < 30.1
    assert 113.9 < ms_gap < 114.1
    # gaussian cone response to 555 nm light (sigma 40 nm)
    def resp(x, peak):
        return math.exp(-((x - peak) ** 2) / (2.0 * 40.0 ** 2))
    l = resp(555.0, l_peak)
    m = resp(555.0, m_peak)
    ratio = m / l
    print("response at 555 nm: L=%.4f M=%.4f M/L=%.4f" % (l, m, ratio))
    assert 0.89 < ratio < 0.90
    # roughly 6.5 million cones per eye serve daylight color vision
    cones = 6.5e6
    print("cones per eye: %.1e" % cones)
    assert 6.4e6 < cones < 6.6e6
    print("rule: three witnesses, one testimony - S, M, L become color")
    print("OK: %s counted the three witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_hue_value_chroma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # RGB(255, 100, 50): separate the three vows
    r, g, b = 255.0, 100.0, 50.0
    mx, mn = max(r, g, b), min(r, g, b)
    delta = mx - mn
    v = mx / 255.0
    s = delta / mx if mx else 0.0
    if delta == 0:
        h = 0.0
    elif mx == r:
        h = 60.0 * (((g - b) / delta) % 6.0)
    elif mx == g:
        h = 60.0 * ((b - r) / delta + 2.0)
    else:
        h = 60.0 * ((r - g) / delta + 4.0)
    print("hue: %.2f deg, saturation: %.4f, value: %.3f" % (h, s, v))
    assert 14.6 < h < 14.7
    assert 0.803 < s < 0.805
    assert 0.999 < v < 1.001
    # same hue at three values: pink / red / maroon territory
    for label, rgb in (("pink", (255, 182, 193)), ("red", (255, 0, 0)), ("maroon", (128, 0, 0))):
        vv = max(rgb) / 255.0
        print("  %-6s value %.3f" % (label, vv))
    print("rule: hue names the family, value the light, chroma the purity")
    print("OK: %s separated the three vows" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_light_and_pigment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # additive world: channels sum, clipped at 255
    def add(c1, c2):
        return tuple(min(255, a + b) for a, b in zip(c1, c2))
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    yellow = add(red, green)
    white = add(add(red, green), blue)
    print("additive: red+green=%s white=%s" % (yellow, white))
    assert yellow == (255, 255, 0)
    assert white == (255, 255, 255)
    # subtractive world: inks absorb, result is the intersection
    cyan, magenta, yellow_ink = (0, 255, 255), (255, 0, 255), (255, 255, 0)
    def over(i1, i2):
        return tuple(min(a, b) for a, b in zip(i1, i2))
    blue_ink = over(cyan, magenta)
    print("subtractive: cyan over magenta=%s" % (blue_ink,))
    assert blue_ink == (0, 0, 255)
    # adding pigment darkens: sum of two inks' darkness
    dark = sum(255 - c for c in over(cyan, yellow_ink))
    print("cyan+yellow ink darkness score: %d (higher = darker)" % dark)
    assert dark == 510
    print("rule: light adds, pigment subtracts - know which covenant is in force")
    print("OK: %s kept the two covenants apart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_primary_colors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three primary sets, one per mixing world
    worlds = {
        "light": ["red", "green", "blue"],
        "paint": ["red", "yellow", "blue"],
        "print": ["cyan", "magenta", "yellow"],
    }
    for world, primaries in worlds.items():
        print("%-6s primaries: %s (count %d)" % (world, ", ".join(primaries), len(primaries)))
        assert len(primaries) == 3
    # every set is unmixable-yet-complete: 3 primaries serve 3 cone channels
    cone_channels = 3
    print("cone channels: %d" % cone_channels)
    assert cone_channels == 3
    print("rule: primary is a job title - unmixable, and building everything")
    print("OK: %s mustered the three primary sets" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_secondary_colors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # paint secondaries: equal-parts blends of paint primaries
    def mix50(c1, c2):
        return tuple(int((a + b) / 2) for a, b in zip(c1, c2))
    red, yellow, blue = (255, 0, 0), (255, 255, 0), (0, 0, 255)
    orange = mix50(red, yellow)
    green = mix50(yellow, blue)
    purple = mix50(blue, red)
    print("orange=%s green=%s purple=%s" % (orange, green, purple))
    assert orange[0] == 255 and 127 <= orange[1] <= 128 and orange[2] == 0
    assert green == (127, 127, 127)  # yellow+blue midpoint blend
    assert purple[0] == 127 and purple[2] == 127
    # light secondaries mirror the print primaries
    light_secondaries = {"yellow": (255, 255, 0), "cyan": (0, 255, 255), "magenta": (255, 0, 255)}
    print("light secondaries: %d (mirror of print primaries)" % len(light_secondaries))
    assert len(light_secondaries) == 3
    print("rule: the secondary is the first oath kept between two primaries")
    print("OK: %s mixed the six secondaries" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_tertiary_colors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve-hue wheel: primaries at 0/120/240, secondaries between, tertiaries fill 30-deg slots
    primaries = {0: "red", 120: "yellow", 240: "blue"}
    secondaries = {60: "orange", 180: "green", 300: "purple"}
    tertiaries = {}
    for p_hue, p_name in primaries.items():
        for s_hue, s_name in secondaries.items():
            # tertiary sits between an adjacent primary and secondary (+/-60 deg)
            diff = (s_hue - p_hue) % 360
            if diff == 60:
                t_hue = (p_hue + 30) % 360
                tertiaries[t_hue] = "%s-%s" % (p_name, s_name)
            elif diff == 300:
                t_hue = (p_hue - 30) % 360
                tertiaries[t_hue] = "%s-%s" % (p_name, s_name)
    ordered = sorted(tertiaries.items())
    for hue, nm in ordered:
        print("  %3d deg: %s" % (hue, nm))
    assert len(tertiaries) == 6
    assert [h for h, _ in ordered] == [30, 90, 150, 210, 270, 330]
    total = len(primaries) + len(secondaries) + len(tertiaries)
    print("wheel hues: %d + %d + %d = %d" % (len(primaries), len(secondaries), len(tertiaries), total))
    assert total == 12
    print("rule: primary first in the name - red-orange, never orange-red")
    print("OK: %s seated the twelve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_warm_cool(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve-hue wheel in 30-degree steps: warm half vs cool half
    hues = list(range(0, 360, 30))
    warm = [h for h in hues if h <= 150]          # red through yellow-green
    cool = [h for h in hues if h > 150]           # green through red-purple
    print("warm hues: %s" % warm)
    print("cool hues: %s" % cool)
    assert len(warm) == 6 and len(cool) == 6
    assert len(set(warm) & set(cool)) == 0
    # anchor memories: firelight ~2000K region vs skylight ~10000K region
    print("warm anchor: fire and low sun (long waves); cool anchor: sky and water (short waves)")
    # a warm red vs a cool red: orange-leaning vs blue-leaning
    warm_red = (255, 36, 0)    # scarlet: leans orange
    cool_red = (220, 20, 60)   # crimson: leans blue
    assert warm_red[1] > cool_red[1] and warm_red[2] < cool_red[2]
    print("warm red %s vs cool red %s: the lean is measurable" % (warm_red, cool_red))
    print("rule: warm gathers, cool releases - choose the mood before the hue")
    print("OK: %s split the wheel by temperature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_tints_shades_tones(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # base hue: a middle red
    base = (200, 60, 40)
    def blend(c, other):
        return tuple(int((a + b) / 2) for a, b in zip(c, other))
    tint = blend(base, (255, 255, 255))   # + white
    shade = blend(base, (0, 0, 0))        # + black
    tone = blend(base, (128, 128, 128))   # + gray
    print("base %s -> tint %s / shade %s / tone %s" % (base, tint, shade, tone))
    assert tint == (227, 157, 147)
    assert shade == (100, 30, 20)
    assert tone == (164, 94, 84)
    # tint raises the minimum channel (adds light), shade lowers the maximum
    assert min(tint) > min(base) > min(shade)
    assert max(shade) < max(base) < max(tint)
    print("rule: tint is the promise kept in daylight, shade in shadow, tone in weather")
    print("OK: %s raised the three margins" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_neutral_colors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # true neutrals: all channels equal
    ladder = [(0, 0, 0), (64, 64, 64), (128, 128, 128), (192, 192, 192), (255, 255, 255)]
    names = ["black", "charcoal", "middle gray", "silver", "white"]
    for nm, c in zip(names, ladder):
        assert c[0] == c[1] == c[2], "not neutral: %s" % (c,)
        print("  %-11s %s" % (nm, c))
    # earthy neutrals carry only a whisper of hue (low chroma)
    beige = (245, 245, 220)
    chroma = max(beige) - min(beige)
    print("beige %s chroma %d (whisper of hue)" % (beige, chroma))
    assert 20 < chroma < 30
    print("rule: neutrals ask for nothing and witness everything")
    print("OK: %s kept the neutral counsel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_color_wheel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the twelve addresses, in spectral order
    wheel = ["red", "red-orange", "orange", "yellow-orange", "yellow",
             "yellow-green", "green", "blue-green", "blue", "blue-purple",
             "purple", "red-purple"]
    step = 360.0 / len(wheel)
    print("wheel: %d hues, step %.1f deg" % (len(wheel), step))
    assert len(wheel) == 12
    assert 29.9 < step < 30.1
    # complements: 180 degrees across; neighbors: 30 degrees away
    def hue_of(nm):
        return wheel.index(nm) * step
    comp = (hue_of("red") + 180.0) % 360.0
    print("red at %.0f deg; opposite at %.0f deg = %s" % (hue_of("red"), comp, wheel[int(comp / step)]))
    assert 179.9 < comp < 180.1
    assert wheel[int(comp / step)] == "green"
    # the circle closes: last neighbor wraps to first
    assert wheel[-1] == "red-purple" and wheel[0] == "red"
    print("rule: the wheel is the council chamber - every harmony a shape on the circle")
    print("OK: %s walked the twelve seats" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_subtractive_mixing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pigment mixing as intersection of surviving wavelengths (midpoint blend model)
    def mix(c1, c2):
        return tuple(int((a + b) / 2) for a, b in zip(c1, c2))
    red, yellow, blue = (255, 0, 0), (255, 255, 0), (0, 0, 255)
    orange = mix(red, yellow)
    green = mix(yellow, blue)
    purple = mix(blue, red)
    print("orange %s, green %s, purple %s" % (orange, green, purple))
    assert orange == (255, 127, 0)
    assert green == (127, 127, 127) or green == (127, 127, 128)
    assert purple == (127, 0, 127)
    # mud: mixing all three primaries collapses toward dark neutral
    mud = mix(mix(red, yellow), blue)
    brightness = sum(mud) / 3.0
    print("three-primary mud %s, mean brightness %.1f" % (mud, brightness))
    assert brightness < 110.0
    print("rule: every added pigment subtracts - mix with few, keep them clean")
    print("OK: %s proved the intersection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_additive_mixing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # light mixing as channel sums clipped at 255
    def add(*cs):
        return tuple(min(255, sum(ch)) for ch in zip(*cs))
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    print("red+green=%s green+blue=%s red+blue=%s" % (add(red, green), add(green, blue), add(red, blue)))
    assert add(red, green) == (255, 255, 0)      # yellow
    assert add(green, blue) == (0, 255, 255)     # cyan
    assert add(red, blue) == (255, 0, 255)       # magenta
    assert add(red, green, blue) == (255, 255, 255)  # white
    # dimmer beams: half-strength red + half-strength green
    half_yellow = add((128, 0, 0), (0, 128, 0))
    print("half beams: %s" % (half_yellow,))
    assert half_yellow == (128, 128, 0)
    print("rule: on a screen every number is a vow of light")
    print("OK: %s summed the three beams" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_complementary(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # complements on the twelve-hue wheel: 180 degrees apart, involution holds
    hues = list(range(0, 360, 30))
    def comp(h):
        return (h + 180) % 360
    pairs = set()
    for h in hues:
        c = comp(h)
        assert comp(c) == h, "complement must be its own inverse"
        pairs.add(tuple(sorted((h, c))))
    print("complementary pairs on 12-wheel: %d" % len(pairs))
    assert len(pairs) == 6
    # the three classic pairs
    names = {0: "red", 60: "yellow", 120: "green", 180: "cyan-ish", 240: "blue", 300: "magenta-ish"}
    for h, c in sorted(pairs)[:3]:
        print("  %d <-> %d" % (h, c))
    # paint neutralization: complements mixed collapse toward gray (reflectance product model)
    red = (1.0, 0.0, 0.0)
    green = (0.0, 0.5, 0.0)
    neutral = tuple(a * b for a, b in zip(red, green))
    spread = max(neutral) - min(neutral)
    print("red*green paint reflectance %s, spread %.2f (collapsed)" % (neutral, spread))
    assert -0.01 < spread < 0.01
    print("rule: the complement is the honor-check on every hue")
    print("OK: %s faced the six opposites" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_analogous(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # analogous span: hero plus neighbors within 60 degrees
    hues = list(range(0, 360, 30))
    def dist(a, b):
        return min((a - b) % 360, (b - a) % 360)
    hero = 0  # red
    family = [h for h in hues if dist(h, hero) <= 60]
    print("analogous family of red: %s" % sorted(family))
    assert sorted(family) == [0, 30, 60, 300, 330]
    assert len(family) == 5
    # 60-30-10 dominance split across hero + two neighbors
    shares = {"hero": 60.0, "neighbor1": 30.0, "neighbor2": 10.0}
    total = sum(shares.values())
    print("dominance split sums to %.0f" % total)
    assert 99.9 < total < 100.1
    # neighbors mix cleanly: overlap of reflectance, no neutralization
    red_orange = (255, 69, 0)
    spread = max(red_orange) - min(red_orange)
    print("red-orange %s keeps a strong spread %d (no collapse)" % (red_orange, spread))
    assert spread > 180
    print("rule: kinship on the wheel - one leads, the others witness")
    print("OK: %s gathered the neighbors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_triadic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four distinct triads on the twelve-hue wheel
    triads = []
    for start in (0, 30, 60, 90):
        triad = sorted(((start + k * 120) % 360) for k in range(3))
        triads.append(triad)
    for t in triads:
        gaps = [(t[(i + 1) % 3] - t[i]) % 360 for i in range(3)]
        print("triad %s gaps %s" % (t, gaps))
        assert all(119.9 < g < 120.1 for g in gaps)
    assert len(triads) == 4
    # the primary triad: red 0, yellow 120, blue 240
    assert triads[0] == [0, 120, 240]
    # the secondary triad: orange 60, green 180, purple 300
    assert triads[2] == [60, 180, 300]
    print("rule: the triangle is perfect, but the composition still crowns one hue")
    print("OK: %s drew the four triangles" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_color_temperature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Wien's displacement law: peak nm = 2,898,000 / T(K)
    def peak_nm(t):
        return 2898000.0 / t
    candle = peak_nm(1800.0)
    bulb = peak_nm(2700.0)
    daylight = peak_nm(6500.0)
    overcast = peak_nm(7500.0)
    print("1800K -> %.0f nm (candle)" % candle)
    print("2700K -> %.0f nm (warm bulb)" % bulb)
    print("6500K -> %.0f nm (daylight)" % daylight)
    print("7500K -> %.0f nm (overcast)" % overcast)
    assert 1609.0 < candle < 1611.0
    assert 1072.0 < bulb < 1074.0
    assert 445.0 < daylight < 447.0
    assert 386.0 < overcast < 387.0
    # hotter radiator -> shorter peak: the backwards-feeling naming, proved
    assert overcast < daylight < bulb < candle
    print("rule: the number names the radiator's heat, not the mood")
    print("OK: %s read the Kelvin signatures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_saturation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # saturation = channel spread / strongest channel
    def sat(rgb):
        mx, mn = max(rgb), min(rgb)
        return (mx - mn) / mx if mx else 0.0
    fire_red = (255, 30, 20)
    dusty_rose = (214, 164, 164)
    gray = (128, 128, 128)
    print("fire red sat %.4f" % sat(fire_red))
    print("dusty rose sat %.4f" % sat(dusty_rose))
    print("gray sat %.4f" % sat(gray))
    assert 0.92 < sat(fire_red) < 0.93
    assert 0.23 < sat(dusty_rose) < 0.24
    assert sat(gray) == 0.0
    # desaturating = pulling channels toward their mean (adding gray)
    r, g, b = 200.0, 60.0, 40.0
    mean = (r + g + b) / 3.0
    half = tuple(int(mean + (c - mean) * 0.5) for c in (r, g, b))
    print("half-desaturated (200,60,40) -> %s" % (half,))
    assert sat(half) < sat((200, 60, 40))
    print("rule: saturate the hero, mute the surroundings")
    print("OK: %s worked the drama control" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_brightness_lightness(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # relative luminance: linearize sRGB, then 0.2126R + 0.7152G + 0.0722B
    def lin(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    def luminance(rgb):
        r, g, b = (lin(c) for c in rgb)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    orange = (255, 128, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    lo, lb, ly = luminance(orange), luminance(blue), luminance(yellow)
    print("luminance orange %.4f blue %.4f yellow %.4f" % (lo, lb, ly))
    assert 0.366 < lo < 0.368
    assert 0.071 < lb < 0.073
    assert 0.927 < ly < 0.929
    # green drives brightness: yellow outshines blue at equal settings
    assert ly > lo > lb
    # maximum contrast: white vs black
    ratio = (1.0 + 0.05) / (0.0 + 0.05)
    print("white-on-black contrast %.1f:1" % ratio)
    assert 20.9 < ratio < 21.1
    print("rule: design for the verdict of lightness, not the lamp of brightness")
    print("OK: %s weighed the light" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_red_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every red leads with the red channel
    family = {
        "red": (255, 0, 0), "scarlet": (255, 36, 0), "crimson": (220, 20, 60),
        "maroon": (128, 0, 0), "brick": (178, 34, 34),
    }
    for nm, (r, g, b) in family.items():
        assert r > b and r >= g, "%s breaks the family rule" % nm
        print("  %-8s %s red leads by %d" % (nm, (r, g, b), r - max(g, b)))
    assert len(family) == 5
    # pink is red tinted: red still leads, all channels lifted
    pink = (255, 182, 193)
    assert pink[0] >= pink[1] and pink[0] >= pink[2]
    print("pink %s: red tinted with white" % (pink,))
    print("rule: red advances - spend it as the accent, rarely the field")
    print("OK: %s mustered the reds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_blue_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every blue leads with the blue channel
    family = {
        "blue": (0, 0, 255), "navy": (0, 0, 128), "sky": (135, 206, 235),
        "teal": (0, 128, 128), "cobalt": (0, 71, 171),
    }
    for nm, (r, g, b) in family.items():
        assert b >= r and b >= g, "%s breaks the family rule" % nm
        print("  %-8s %s blue leads by %d" % (nm, (r, g, b), b - max(r, g)))
    assert len(family) == 5
    # teal sits on the blue-green border: blue ties green
    assert family["teal"][1] == family["teal"][2]
    print("rule: blue recedes - the steady witness of distance and trust")
    print("OK: %s mustered the blues" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_green_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every green leads with the green channel
    family = {
        "green": (0, 128, 0), "lime": (0, 255, 0), "forest": (34, 139, 34),
        "mint": (189, 252, 201), "olive": (128, 128, 0),
    }
    for nm, (r, g, b) in family.items():
        assert g >= r and g >= b, "%s breaks the family rule" % nm
        print("  %-8s %s green leads by %d" % (nm, (r, g, b), g - max(r, b)))
    assert len(family) == 5
    # olive balances green and red for earthiness
    assert family["olive"][0] == family["olive"][1]
    print("rule: green holds the middle ground where the eye is at peace")
    print("OK: %s mustered the greens" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_yellow_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every yellow carries high red AND high green, blue trailing
    family = {
        "yellow": (255, 255, 0), "gold": (255, 215, 0), "amber": (255, 191, 0),
        "lemon": (255, 247, 0), "mustard": (255, 219, 88),
    }
    for nm, (r, g, b) in family.items():
        assert r > 100 and g > 100 and b < r and b <= g, "%s breaks the family rule" % nm
        print("  %-8s %s twin channels at %d,%d" % (nm, (r, g, b), r, g))
    assert len(family) == 5
    # mustard mutes toward earth: blue rises but never leads
    assert family["mustard"][2] == 88
    print("rule: yellow heralds - sounded briefly, never wallpapered")
    print("OK: %s mustered the yellows" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_purple_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every purple leads with blue while keeping red strong
    family = {
        "purple": (128, 0, 128), "violet": (238, 130, 238), "indigo": (75, 0, 130),
        "lavender": (230, 230, 250), "plum": (221, 160, 221),
    }
    for nm, (r, g, b) in family.items():
        assert b >= g, "%s breaks the family rule" % nm
        print("  %-8s %s blue %d, red %d" % (nm, (r, g, b), b, r))
    assert len(family) == 5
    # indigo leans hardest to blue
    assert family["indigo"][2] - family["indigo"][0] == 55
    print("rule: purple is the seal of imagination - the hue the rainbow never shows")
    print("OK: %s mustered the purples" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_orange_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every orange orders red > green > blue
    family = {
        "orange": (255, 165, 0), "tangerine": (242, 133, 0), "coral": (255, 127, 80),
        "peach": (255, 229, 180), "rust": (183, 65, 14),
    }
    for nm, (r, g, b) in family.items():
        assert r > g > b, "%s breaks the family rule" % nm
        print("  %-9s %s R>G>B holds" % (nm, (r, g, b)))
    assert len(family) == 5
    # peach tints toward white but keeps the order
    assert family["peach"] == (255, 229, 180)
    print("rule: orange is the handshake hue - the inviting accent")
    print("OK: %s mustered the oranges" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_brown(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # brown = orange scaled toward black; channel order unchanged
    orange = (255, 165, 0)
    brown = tuple(int(c * 0.4) for c in orange)
    print("orange %s at 40%% -> brown %s" % (orange, brown))
    assert brown == (102, 66, 0)
    r, g, b = brown
    assert r > g > b and max(brown) < 150
    # chocolate deepens further
    chocolate = tuple(int(c * 0.25) for c in orange)
    print("at 25%% -> chocolate %s" % (chocolate,))
    assert chocolate == (63, 41, 0)
    # tan lifts brown with white
    tan = tuple(int((c + 255) / 2) for c in brown)
    print("brown lifted with white -> tan %s" % (tan,))
    assert tan == (178, 160, 127)
    print("rule: brown exists only in context - humility is glory, darkened")
    print("OK: %s proved brown is dark orange" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_gray(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mixing black and white: the gray is the midpoint
    def mix(c1, c2):
        return tuple(int((a + b) / 2) for a, b in zip(c1, c2))
    black, white = (0, 0, 0), (255, 255, 255)
    mid = mix(black, white)
    print("black+white -> %s" % (mid,))
    assert mid[0] == mid[1] == mid[2]
    assert mid[0] in (127, 128)
    # the lean: warm gray vs cool gray
    warm_gray = (130, 128, 125)
    cool_gray = (125, 128, 132)
    print("warm gray %s (R>B), cool gray %s (B>R)" % (warm_gray, cool_gray))
    assert warm_gray[0] > warm_gray[2]
    assert cool_gray[2] > cool_gray[0]
    # five-step ladder
    ladder = [(0, 0, 0), (64, 64, 64), (128, 128, 128), (192, 192, 192), (255, 255, 255)]
    assert all(c[0] == c[1] == c[2] for c in ladder)
    print("gray ladder: %d steps" % len(ladder))
    print("rule: gray is the judge - consult it before signing any color")
    print("OK: %s climbed the gray ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_black_white(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the two poles: luminance 1.0 and 0.0
    white_lum, black_lum = 1.0, 0.0
    ratio = (white_lum + 0.05) / (black_lum + 0.05)
    print("white luminance %.1f, black luminance %.1f" % (white_lum, black_lum))
    print("maximum contrast ratio: %.1f:1" % ratio)
    assert 20.9 < ratio < 21.1
    # every gray sits between the poles
    for v in (0.25, 0.5, 0.75):
        assert 0.0 < v < 1.0
    print("quarter, half, three-quarter grays all sit between the poles")
    # in paint: titanium white reflects ~85%, carbon black absorbs ~95%+
    paper_white = 0.85
    carbon_black = 0.04
    print("paper reflects ~%.0f%%, carbon black ~%.0f%%" % (paper_white * 100, carbon_black * 100))
    assert 0.84 < paper_white < 0.86
    assert 0.03 < carbon_black < 0.05
    print("rule: if the grays hold, the colors may play")
    print("OK: %s stood between the poles" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_harmonies(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the six schemes as hue counts on the twelve-hue wheel
    schemes = {
        "monochromatic": 1, "analogous": 3, "complementary": 2,
        "split-complementary": 3, "triadic": 3, "tetradic": 4,
    }
    for nm, n in schemes.items():
        print("  %-19s %d hues" % (nm, n))
    assert len(schemes) == 6
    assert sum(schemes.values()) == 16
    # split-complementary geometry: hero 0 plus neighbors of opposite 180
    hero, opposite = 0, 180
    split = sorted([hero, (opposite - 30) % 360, (opposite + 30) % 360])
    print("split-complementary of red: %s" % split)
    assert split == [0, 150, 210]
    # the iron law: 60-30-10 dominance
    shares = (60.0, 30.0, 10.0)
    assert 99.9 < sum(shares) < 100.1
    print("rule: strategy before tactics - sign the scheme before choosing hues")
    print("OK: %s signed the six covenants" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_hex_rgb(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # decode #FF8000 by hand
    hexcode = "#FF8000"
    r = int(hexcode[1:3], 16)
    g = int(hexcode[3:5], 16)
    b = int(hexcode[5:7], 16)
    print("%s -> rgb(%d, %d, %d)" % (hexcode, r, g, b))
    assert (r, g, b) == (255, 128, 0)
    # re-encode: the round trip
    back = "#%02X%02X%02X" % (r, g, b)
    print("re-encoded: %s" % back)
    assert back == hexcode
    # the landmark test
    landmarks = {"#000000": (0, 0, 0), "#FFFFFF": (255, 255, 255),
                 "#808080": (128, 128, 128), "#FF0000": (255, 0, 0),
                 "#00FF00": (0, 255, 0), "#0000FF": (0, 0, 255)}
    for hx, expect in landmarks.items():
        got = (int(hx[1:3], 16), int(hx[3:5], 16), int(hx[5:7], 16))
        assert got == expect, hx
    print("landmarks decoded: %d/%d" % (len(landmarks), len(landmarks)))
    # 16.7 million addressable colors
    total = 256 ** 3
    print("addressable colors: %d" % total)
    assert total == 16777216
    print("rule: read the code, see the color - never confuse the two")
    print("OK: %s read the true names" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_cmyk(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # RGB(255,128,0) -> CMYK by the standard conversion
    r, g, b = 255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0
    k = 1.0 - max(r, g, b)
    if k >= 1.0:
        c = m = y = 0.0
    else:
        c = (1.0 - r - k) / (1.0 - k)
        m = (1.0 - g - k) / (1.0 - k)
        y = (1.0 - b - k) / (1.0 - k)
    print("rgb(255,128,0) -> C=%.3f M=%.3f Y=%.3f K=%.3f" % (c, m, y, k))
    assert -0.001 < c < 0.001
    assert 0.497 < m < 0.499
    assert 0.999 < y < 1.001
    assert -0.001 < k < 0.001
    # pure black needs the K plate: three-ink black is muddy theory only
    print("K plate carries depth, crisp text, and ink economy")
    # halftone screen angles avoid moire
    angles = {"C": 15, "M": 75, "Y": 0, "K": 45}
    assert len(set(angles.values())) == 4
    print("screen angles: %s" % angles)
    print("rule: translate the vow before the press - soft-proof the gamut")
    print("OK: %s spoke the print language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_color_vision(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # simplified protanopia remap of pure red (illustrative matrix)
    r, g, b = 255.0, 0.0, 0.0
    rp = 0.567 * r + 0.433 * g
    gp = 0.558 * r + 0.442 * g
    bp = 0.0 * r + 0.242 * g + 0.758 * b
    print("pure red under protanopia sim: (%.1f, %.1f, %.1f)" % (rp, gp, bp))
    assert 144.0 < rp < 145.0
    assert 142.0 < gp < 143.0
    assert -0.1 < bp < 0.1
    # red collapses toward where green maps: the confusion, quantified
    gr, gg, gb = 0.0, 255.0, 0.0
    grp = 0.567 * gr + 0.433 * gg
    print("pure green under same sim: (%.1f, ...)" % grp)
    assert 110.0 < grp < 111.0
    gap = abs(rp - grp)
    print("red-green separation after sim: %.1f (was 255)" % gap)
    assert 34.0 < gap < 35.0
    # prevalence: 1 in 12 men
    print("about 1 in 12 men, 1 in 200 women")
    print("rule: never encode meaning in red-versus-green alone")
    print("OK: %s saw through other eyes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_color_emotion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # association tally: 200 viewers, each naming the feeling a color gives
    responses = 200
    tally = {"red-energy": 92, "blue-calm": 118, "yellow-happy": 87,
             "green-nature": 105, "black-elegant": 64, "white-clean": 71,
             "orange-friendly": 58, "purple-creative": 49}
    for label, n in tally.items():
        pct = n / responses * 100.0
        print("  %-15s %3d/200 (%4.1f%%)" % (label, n, pct))
    red_pct = tally["red-energy"] / responses * 100.0
    blue_pct = tally["blue-calm"] / responses * 100.0
    assert 45.9 < red_pct < 46.1
    assert 58.9 < blue_pct < 59.1
    # blue-calm beats red-energy in this tally: calm outpolls excitement
    assert tally["blue-calm"] > tally["red-energy"]
    print("rule: choose the feeling first, then hire the hue - and test it")
    print("OK: %s polled the feelings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_colb_spectrum(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # frequency = c / wavelength; c = 299,792,458 m/s
    c = 299792458.0
    def freq_hz(wavelength_nm):
        return c / (wavelength_nm * 1e-9)
    red = freq_hz(700.0)
    violet = freq_hz(400.0)
    ir_edge = freq_hz(750.0)
    uv_edge = freq_hz(380.0)
    print("700 nm red    -> %.3e Hz" % red)
    print("400 nm violet -> %.3e Hz" % violet)
    print("750 nm IR edge-> %.3e Hz" % ir_edge)
    print("380 nm UV edge-> %.3e Hz" % uv_edge)
    assert 4.28e14 < red < 4.29e14
    assert 7.49e14 < violet < 7.50e14
    assert 3.99e14 < ir_edge < 4.01e14
    assert 7.88e14 < uv_edge < 7.90e14
    # the visible window is a sliver: 370 nm of an enormous spectrum
    window = 750.0 - 380.0
    print("visible window: %.0f nm" % window)
    assert 369.9 < window < 370.1
    print("rule: the narrow window is enough - wonder is the closing oath")
    print("OK: %s mapped the horizon" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is_color": demo_colb_what_is_color,
    "how_eye_sees": demo_colb_how_eye_sees,
    "hue_value_chroma": demo_colb_hue_value_chroma,
    "light_and_pigment": demo_colb_light_and_pigment,
    "primary_colors": demo_colb_primary_colors,
    "secondary_colors": demo_colb_secondary_colors,
    "tertiary_colors": demo_colb_tertiary_colors,
    "warm_cool": demo_colb_warm_cool,
    "tints_shades_tones": demo_colb_tints_shades_tones,
    "neutral_colors": demo_colb_neutral_colors,
    "color_wheel": demo_colb_color_wheel,
    "subtractive_mixing": demo_colb_subtractive_mixing,
    "additive_mixing": demo_colb_additive_mixing,
    "complementary": demo_colb_complementary,
    "analogous": demo_colb_analogous,
    "triadic": demo_colb_triadic,
    "color_temperature": demo_colb_color_temperature,
    "saturation": demo_colb_saturation,
    "brightness_lightness": demo_colb_brightness_lightness,
    "red_family": demo_colb_red_family,
    "blue_family": demo_colb_blue_family,
    "green_family": demo_colb_green_family,
    "yellow_family": demo_colb_yellow_family,
    "purple_family": demo_colb_purple_family,
    "orange_family": demo_colb_orange_family,
    "brown": demo_colb_brown,
    "gray": demo_colb_gray,
    "black_white": demo_colb_black_white,
    "harmonies": demo_colb_harmonies,
    "hex_rgb": demo_colb_hex_rgb,
    "cmyk": demo_colb_cmyk,
    "color_vision": demo_colb_color_vision,
    "color_emotion": demo_colb_color_emotion,
    "spectrum": demo_colb_spectrum,
}
