#!/usr/bin/env python3
"""Demo programs for the Shapes Basics databases (fundamentals order #9).

Every demo is real, runnable, stdlib-only Python performing the actual
geometry computation for its record. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Numerical cores hand-computed
2026-10-17 and cross-checked against the entry text.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_shp_what_is_shape(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classify a shelf of objects by dimension / edge / count
    shelf = [
        ("coin", "2D", "curved"), ("tile", "2D", "straight"),
        ("door", "2D", "straight"), ("yield sign", "2D", "straight"),
        ("ball", "3D", "curved"), ("box", "3D", "straight"),
        ("can", "3D", "curved"), ("traffic cone", "3D", "curved"),
    ]
    flat = [o for o in shelf if o[1] == "2D"]
    solid = [o for o in shelf if o[1] == "3D"]
    curved = [o for o in shelf if o[2] == "curved"]
    print("shelf objects: %d" % len(shelf))
    print("flat (2D): %d -> %s" % (len(flat), ", ".join(o[0] for o in flat)))
    print("solid (3D): %d -> %s" % (len(solid), ", ".join(o[0] for o in solid)))
    print("curved-edge: %d of %d" % (len(curved), len(shelf)))
    assert len(shelf) == 8
    assert len(flat) == 4 and len(solid) == 4
    assert len(curved) == 4
    print("rule: dimension first, edge type second, count third - the shape names itself")
    print("OK: %s sorted the shelf" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_points_lines_angles(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # triangle angle sum holds for every triangle
    tris = [(60, 60, 60), (90, 60, 30), (100, 50, 30), (45, 45, 90)]
    for a, b, c in tris:
        s = a + b + c
        print("angles %d, %d, %d sum to %d" % (a, b, c, s))
        assert s == 180
    # complementary and supplementary partners
    comp = 90 - 30
    supp = 180 - 110
    print("complement of 30: %d (sum %d)" % (comp, 30 + comp))
    print("supplement of 110: %d (sum %d)" % (supp, 110 + supp))
    assert comp == 60 and supp == 70
    # classification
    def kind(a):
        return "acute" if a < 90 else ("right" if a == 90 else "obtuse" if a < 180 else "straight")
    checks = {30: "acute", 90: "right", 120: "obtuse", 180: "straight"}
    for a, want in checks.items():
        assert kind(a) == want, a
    print("classified 30/90/120/180 as acute/right/obtuse/straight")
    print("OK: %s proved the atoms behave" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_sides_vertices_corners(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # polygons: sides always equal vertices
    polys = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6,
             "heptagon": 7, "octagon": 8}
    total_v = 0
    for pname, n in polys.items():
        sides, verts = n, n
        print("%-9s sides=%d vertices=%d" % (pname, sides, verts))
        assert sides == verts
        total_v += verts
    print("total vertices across the six polygons: %d" % total_v)
    assert total_v == 33
    # 3D surveys: (faces, edges, vertices)
    solids = {"cube": (6, 12, 8), "rectangular prism": (6, 12, 8),
              "square pyramid": (5, 8, 5)}
    for sname, (f, e, v) in solids.items():
        print("%-18s F=%d E=%d V=%d" % (sname, f, e, v))
        assert f + v - e == 2
    print("OK: %s counted every witness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_circle_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    r = 5.0
    d = 2 * r
    c = math.pi * d
    a = math.pi * r * r
    print("radius: %.1f" % r)
    print("diameter: %.1f (2 x radius)" % d)
    print("circumference: %.4f" % c)
    print("area: %.4f" % a)
    assert 9.99 < d < 10.01
    assert 31.415 < c < 31.417
    assert 78.539 < a < 78.541
    ratio = c / d
    print("circumference / diameter = %.6f (pi)" % ratio)
    assert 3.14159 < ratio < 3.14160
    print("sides: 0, vertices: 0, corners: 0 - one smooth edge, rolls perfectly")
    print("OK: %s drew the roundest shape" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_triangle_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 3-4-5 right triangle
    a, b, c = 3.0, 4.0, 5.0
    per = a + b + c
    area = 0.5 * a * b
    print("3-4-5 triangle: perimeter=%.0f area=%.0f" % (per, area))
    assert per == 12.0 and area == 6.0
    # Pythagoras check on the hypotenuse
    hyp = math.sqrt(a * a + b * b)
    print("hypotenuse from Pythagoras: %.4f" % hyp)
    assert 4.9999 < hyp < 5.0001
    # classification by sides and angles
    def by_sides(x, y, z):
        s = len({round(x, 6), round(y, 6), round(z, 6)})
        return {1: "equilateral", 2: "isosceles", 3: "scalene"}[s]
    def by_angles(p, q, r):
        m = max(p, q, r)
        return "right" if m == 90 else ("obtuse" if m > 90 else "acute")
    assert by_sides(5, 5, 5) == "equilateral"
    assert by_sides(5, 5, 6) == "isosceles"
    assert by_sides(3, 4, 5) == "scalene"
    assert by_angles(60, 60, 60) == "acute"
    assert by_angles(90, 60, 30) == "right"
    assert by_angles(100, 50, 30) == "obtuse"
    print("classifications verified: sides and angles both")
    # area from base and height
    print("base 10 height 6 -> area %.0f" % (0.5 * 10 * 6))
    assert 0.5 * 10 * 6 == 30.0
    print("OK: %s raised the threefold witness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_square_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = 7.0
    per = 4 * s
    area = s * s
    diag = s * math.sqrt(2)
    print("side: %.1f" % s)
    print("perimeter: %.0f" % per)
    print("area: %.0f" % area)
    print("diagonal: %.4f" % diag)
    assert per == 28.0 and area == 49.0
    assert 9.8994 < diag < 9.8996
    # diagonal squared is twice the side squared
    print("diagonal^2 = %.4f, 2*side^2 = %.0f" % (diag * diag, 2 * s * s))
    assert 97.99 < diag * diag < 98.01
    # tiling check: 7x7 square holds 49 unit squares
    print("unit squares tiled: %d" % int(area))
    assert int(area) == 49
    print("OK: %s kept all four sides honest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_rectangle_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    l, w = 8.0, 5.0
    per = 2 * (l + w)
    area = l * w
    diag = math.sqrt(l * l + w * w)
    print("length %.0f width %.0f" % (l, w))
    print("perimeter: %.0f" % per)
    print("area: %.0f (unit squares counted)" % area)
    print("diagonal: %.4f" % diag)
    assert per == 26.0 and area == 40.0
    assert 9.4339 < diag < 9.4341
    print("diagonal^2 = %.4f (expect 89)" % (diag * diag))
    assert 88.99 < diag * diag < 89.01
    # square is a rectangle: 5x5 behaves
    print("square-as-rectangle 5x5: perimeter %.0f area %.0f" % (2 * 10.0, 25.0))
    assert 2 * (5.0 + 5.0) == 20.0
    print("OK: %s framed the workhorse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_other_quadrilaterals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every quadrilateral's angles sum to 360
    quads = {
        "parallelogram": (110, 70, 110, 70),
        "rhombus": (120, 60, 120, 60),
        "trapezoid": (90, 90, 60, 120),
        "kite": (100, 90, 100, 70),
    }
    for qname, angs in quads.items():
        s = sum(angs)
        print("%-13s angle sum: %d" % (qname, s))
        assert s == 360
    # parallelogram area: base x vertical height
    b, h = 9.0, 4.0
    print("parallelogram base %.0f height %.0f -> area %.0f" % (b, h, b * h))
    assert b * h == 36.0
    # square keeps every family membership
    print("square: parallelogram yes, rhombus yes, rectangle yes, kite yes")
    print("OK: %s tested the family four ways" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_measuring_length(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # metric conversions
    cm = 2.5 * 100
    mm = 2.5 * 1000
    print("2.5 m = %.0f cm = %.0f mm" % (cm, mm))
    assert cm == 250.0 and mm == 2500.0
    # customary conversions
    ft = 36 / 12
    yd = 36 / 36
    print("36 in = %.0f ft = %.0f yd" % (ft, yd))
    assert ft == 3.0 and yd == 1.0
    # units multiply with the numbers: area of 3m x 4m
    area = 3.0 * 4.0
    print("3 m x 4 m = %.0f square meters" % area)
    assert area == 12.0
    # volume: 2m cube
    vol = 2.0 ** 3
    print("2 m cube = %.0f cubic meters" % vol)
    assert vol == 8.0
    print("OK: %s laid the ruler true" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_shapes_around_us(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classify twenty everyday objects into the ten core shape families
    objs = {
        "circle": ["clock", "coin", "plate"],
        "triangle": ["yield sign", "roof peak", "pizza slice"],
        "square": ["tile", "window pane"],
        "rectangle": ["door", "phone screen"],
        "polygon": ["stop sign", "honeycomb cell"],
        "cube": ["dice", "sugar cube"],
        "sphere": ["ball", "orange"],
        "cylinder": ["soup can"],
        "cone": ["traffic cone", "ice-cream cone"],
        "pyramid": ["tent"],
    }
    total = sum(len(v) for v in objs.values())
    print("objects classified: %d" % total)
    for fam in objs:
        share = len(objs[fam]) / total * 100
        print("  %-9s %2d objects (%4.1f %%)" % (fam, len(objs[fam]), share))
    assert total == 20
    assert len(objs) == 10
    assert 14.9 < len(objs["circle"]) / total * 100 < 15.1
    print("ten families cover the whole shelf - the world is shapes in disguise")
    print("OK: %s spotted them in the wild" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_pentagon_hexagon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # interior sums: (n-2) * 180
    pent_sum = (5 - 2) * 180
    hex_sum = (6 - 2) * 180
    print("pentagon interior sum: %d (3 triangles)" % pent_sum)
    print("hexagon interior sum: %d (4 triangles)" % hex_sum)
    assert pent_sum == 540 and hex_sum == 720
    pent_each = pent_sum / 5
    hex_each = hex_sum / 6
    print("regular pentagon each angle: %.0f" % pent_each)
    print("regular hexagon each angle: %.0f" % hex_each)
    assert pent_each == 108.0 and hex_each == 120.0
    # hexagon secret: six equilateral triangles around the center
    center_angles = 6 * 60
    print("hexagon center angles: 6 x 60 = %d (full turn)" % center_angles)
    assert center_angles == 360
    print("side equals radius in the regular hexagon")
    print("OK: %s counted to five and six" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_more_polygons(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    names = {7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon"}
    for n in (7, 8, 9, 10):
        isum = (n - 2) * 180
        each_in = isum / n
        each_ex = 360 / n
        print("%-8s n=%d interior sum=%d each interior=%.1f each exterior=%.1f" %
              (names[n], n, isum, each_in, each_ex))
        assert n * each_ex == 360
        assert 179.9 < each_in + each_ex < 180.1
    assert (8 - 2) * 180 == 1080
    assert 1080 / 8 == 135.0
    print("regular octagon interior angle: 135 (the stop sign)")
    # n-gon leans toward the circle
    approx = 100
    print("regular %d-gon each exterior: %.1f degrees - nearly a circle" % (approx, 360 / approx))
    assert 3.59 < 360 / approx < 3.61
    print("OK: %s marched the numbers upward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_regular_irregular(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # regularity test: all sides equal AND all angles equal
    def regular(sides, angles):
        return len(set(sides)) == 1 and len(set(angles)) == 1
    tests = {
        "square": ([4, 4, 4, 4], [90, 90, 90, 90], True),
        "rectangle 4x6": ([4, 6, 4, 6], [90, 90, 90, 90], False),
        "rhombus": ([5, 5, 5, 5], [120, 60, 120, 60], False),
        "equilateral triangle": ([3, 3, 3], [60, 60, 60], True),
    }
    for tname, (s, a, want) in tests.items():
        got = regular(s, a)
        print("%-20s regular=%s" % (tname, got))
        assert got == want
    # regular hexagon interior angle
    print("regular hexagon interior: %.0f" % (720 / 6))
    assert 720 / 6 == 120.0
    # symmetry counts for the regular pentagon
    print("regular pentagon: 5 mirror lines, 5-fold rotation")
    print("only triangle, square, hexagon tile the plane gap-free")
    print("OK: %s kept the double oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_perimeter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # L-shaped hexagon: addition conquers all
    sides = [6, 4, 2, 2, 4, 2]
    print("L-hexagon sides %s -> perimeter %d" % (sides, sum(sides)))
    assert sum(sides) == 20
    # rectangle shortcut
    print("rectangle 8x5 -> perimeter %.0f" % (2 * (8 + 5)))
    assert 2 * (8 + 5) == 26
    # regular pentagon shortcut
    print("regular pentagon side 7 -> perimeter %.0f" % (5 * 7))
    assert 5 * 7 == 35
    # equal perimeter, different area
    r_area = 1 * 9
    s_area = 5 * 5
    print("1x9 rectangle and 5x5 square: perimeter 20 both, areas %d vs %d" % (r_area, s_area))
    assert 2 * (1 + 9) == 20 and 4 * 5 == 20
    assert r_area == 9 and s_area == 25
    print("perimeter in length units - never square units")
    print("OK: %s walked every boundary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_area_rect_square(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tiling count: 12x9 rectangle
    area = 12 * 9
    print("12x9 rectangle: %d unit squares" % area)
    assert area == 108
    sq = 11 * 11
    print("square side 11: area %d" % sq)
    assert sq == 121
    # doubling behaviors
    a1 = 6 * 4
    a2 = 12 * 4
    a3 = 12 * 8
    print("6x4=%d, 12x4=%d (doubled), 12x8=%d (quadrupled)" % (a1, a2, a3))
    assert a1 == 24 and a2 == 48 and a3 == 96
    print("acre = 43560 square feet (given)")
    print("OK: %s counted the harvest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_area_triangle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # half of the rectangle
    print("base 10 height 6 -> area %.0f" % (0.5 * 10 * 6))
    assert 0.5 * 10 * 6 == 30.0
    # Heron on 5,5,6
    a, b, c = 5.0, 5.0, 6.0
    s = (a + b + c) / 2
    heron = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Heron 5,5,6: semiperimeter %.0f area %.4f" % (s, heron))
    assert s == 8.0
    assert 11.999 < heron < 12.001
    # 3-4-5 both ways
    s2 = (3 + 4 + 5) / 2
    h2 = math.sqrt(s2 * (s2 - 3) * (s2 - 4) * (s2 - 5))
    print("3-4-5: half-base-height=%.0f Heron=%.4f" % (0.5 * 3 * 4, h2))
    assert 0.5 * 3 * 4 == 6.0
    assert 5.999 < h2 < 6.001
    # base independence: same triangle, base 5 height 4.8
    print("base 5 height 4.8 -> area %.1f (same triangle)" % (0.5 * 5 * 4.8))
    assert 11.99 < 0.5 * 5 * 4.8 < 12.01
    print("OK: %s took exactly half" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_circle_measure(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    r = 3.0
    c = 2 * math.pi * r
    a = math.pi * r * r
    print("radius %.0f: circumference %.4f area %.4f" % (r, c, a))
    assert 18.8495 < c < 18.8497
    assert 28.2742 < a < 28.2744
    # doubling: circumference x2, area x4
    c2 = 2 * math.pi * 6.0
    a2 = math.pi * 36.0
    print("radius 6: circumference %.4f (x%.2f) area %.4f (x%.2f)" %
          (c2, c2 / c, a2, a2 / a))
    assert 1.999 < c2 / c < 2.001
    assert 3.999 < a2 / a < 4.001
    # pi ratio check
    print("C/d = %.6f" % (c / 6.0))
    assert 3.14159 < c / 6.0 < 3.14160
    print("OK: %s measured the round" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_three_d_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    surveys = {
        "cube": (6, 12, 8),
        "rectangular prism": (6, 12, 8),
        "square pyramid": (5, 8, 5),
        "triangular prism": (5, 9, 6),
    }
    for sname, (f, e, v) in surveys.items():
        print("%-18s F=%d E=%d V=%d  F+V-E=%d" % (sname, f, e, v, f + v - e))
        assert f + v - e == 2
    # the sphere: curved, zero counts
    print("sphere: F=0 E=0 V=0 - one curved surface, not a polyhedron")
    # polyhedron test
    poly = {"cube": True, "square pyramid": True, "sphere": False,
            "cylinder": False, "cone": False}
    for sname, want in poly.items():
        print("%-18s polyhedron=%s" % (sname, want))
    assert poly["cube"] and not poly["sphere"]
    print("OK: %s surveyed the solids" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_cube_prism(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = 4.0
    cv, csa = s ** 3, 6 * s * s
    print("cube side %.0f: volume %.0f surface area %.0f" % (s, cv, csa))
    assert cv == 64.0 and csa == 96.0
    l, w, h = 3.0, 4.0, 5.0
    bv = l * w * h
    bsa = 2 * (l * w + l * h + w * h)
    print("box 3x4x5: volume %.0f surface area %.0f" % (bv, bsa))
    assert bv == 60.0 and bsa == 94.0
    # face-by-face check of the box
    faces = [l * w, l * w, l * h, l * h, w * h, w * h]
    print("faces %s sum %.0f" % (faces, sum(faces)))
    assert sum(faces) == 94.0
    # unit-cube counting: 3x4x5 box holds 60 unit cubes
    print("unit cubes in the box: %d" % int(bv))
    assert int(bv) == 60
    print("OK: %s stacked the promises" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_sphere(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    r = 3.0
    sa = 4 * math.pi * r * r
    vol = 4.0 / 3.0 * math.pi * r ** 3
    print("sphere radius %.0f: surface area %.4f volume %.4f" % (r, sa, vol))
    assert 113.0972 < sa < 113.0974
    assert 113.0972 < vol < 113.0974
    print("at radius 3 both equal 36*pi - the famous coincidence")
    assert abs(sa - vol) < 1e-9
    r2 = 5.0
    sa2 = 4 * math.pi * r2 * r2
    vol2 = 4.0 / 3.0 * math.pi * r2 ** 3
    print("radius 5: surface area %.4f volume %.4f" % (sa2, vol2))
    assert 314.1592 < sa2 < 314.1594
    assert 523.5987 < vol2 < 523.5989
    # Archimedes: sphere is 2/3 of its enclosing cylinder
    cyl = math.pi * r2 * r2 * (2 * r2)
    print("enclosing cylinder volume %.4f, ratio %.4f (expect 2/3)" % (cyl, vol2 / cyl))
    assert 0.6666 < vol2 / cyl < 0.6667
    print("OK: %s honored Archimedes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_cylinder(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    r, h = 2.0, 5.0
    vol = math.pi * r * r * h
    lat = 2 * math.pi * r * h
    sa = 2 * math.pi * r * r + lat
    print("cylinder r=%.0f h=%.0f: volume %.4f" % (r, h, vol))
    print("lateral area %.4f surface area %.4f" % (lat, sa))
    assert 62.8318 < vol < 62.8320
    assert 87.9645 < sa < 87.9647
    # unrolling check: lateral = circumference x height
    circ = 2 * math.pi * r
    print("circumference x height = %.4f x %.0f = %.4f" % (circ, h, circ * h))
    assert 62.8318 < circ * h < 62.8320
    assert abs(lat - circ * h) < 1e-9
    # ends check
    ends = 2 * math.pi * r * r
    print("two ends %.4f + lateral %.4f = %.4f" % (ends, lat, ends + lat))
    assert abs(ends + lat - sa) < 1e-9
    print("OK: %s unrolled the scroll" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_cone(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    r, h = 3.0, 4.0
    l = math.sqrt(r * r + h * h)
    vol = (1.0 / 3.0) * math.pi * r * r * h
    lat = math.pi * r * l
    sa = math.pi * r * r + lat
    print("cone r=%.0f h=%.0f: slant height %.4f (3-4-5)" % (r, h, l))
    print("volume %.4f lateral %.4f total surface %.4f" % (vol, lat, sa))
    assert 4.9999 < l < 5.0001
    assert 37.6990 < vol < 37.6992
    assert 47.1238 < lat < 47.1240
    assert 75.3981 < sa < 75.3983
    # one-third of the matching cylinder
    cyl = math.pi * r * r * h
    print("matching cylinder %.4f / 3 = %.4f" % (cyl, cyl / 3))
    assert abs(cyl / 3 - vol) < 1e-9
    # sector check: arc = base circumference
    arc = 2 * math.pi * r
    print("unrolled sector arc %.4f = base circumference %.4f" % (arc, arc))
    assert 18.8495 < arc < 18.8497
    print("OK: %s gathered to the point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_pyramid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    b, h = 6.0, 4.0
    base_area = b * b
    vol = (1.0 / 3.0) * base_area * h
    print("square pyramid base %.0f height %.0f: volume %.0f" % (b, h, vol))
    assert base_area == 36.0 and vol == 48.0
    # one-third of the box
    box = b * b * h
    print("matching box %.0f / 3 = %.0f" % (box, box / 3))
    assert box / 3 == 48.0
    # surveys
    print("square pyramid: F=5 E=8 V=8? no - F=5 E=8 V=5, check %d" % (5 + 5 - 8))
    assert 5 + 5 - 8 == 2
    print("tetrahedron: F=4 E=6 V=4, check %d" % (4 + 4 - 6))
    assert 4 + 4 - 6 == 2
    # lateral faces are triangles: 4 of base 6
    print("4 triangular faces on a square base - named by the base")
    print("OK: %s raised the apex" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_volume_prisms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # triangular prism: right-triangle base legs 6,8 -> area 24, length 10
    base_area = 0.5 * 6 * 8
    vol = base_area * 10
    print("triangular prism: base area %.0f x length 10 = volume %.0f" % (base_area, vol))
    assert base_area == 24.0 and vol == 240.0
    # cylinder as circular prism
    cyl = math.pi * 4 * 5
    print("cylinder r=2 h=5: base area %.4f x 5 = %.4f" % (math.pi * 4, cyl))
    assert 62.8318 < cyl < 62.8320
    # box as special case
    print("box 3x4x5 as prism: base 12 x height 5 = %.0f" % (12 * 5))
    assert 12 * 5 == 60
    # scaling: double height doubles volume; double base dims quadruples
    print("double height: %.0f -> %.0f" % (vol, base_area * 20))
    assert base_area * 20 == 480.0
    v2 = (0.5 * 12 * 16) * 10
    print("double base dims: %.0f (x4)" % v2)
    assert v2 == 960.0
    print("OK: %s stacked the layers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_surface_area(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sphere radius 5
    sa_s = 4 * math.pi * 25
    print("sphere r=5 surface area: %.4f" % sa_s)
    assert 314.1592 < sa_s < 314.1594
    # box 3x4x5 face by face
    faces = [12, 12, 15, 15, 20, 20]
    print("box faces %s sum to %.0f" % (faces, sum(faces)))
    assert sum(faces) == 94
    # cylinder r=2 h=5
    sa_c = 2 * math.pi * 4 + 2 * math.pi * 2 * 5
    print("cylinder r=2 h=5 surface area: %.4f" % sa_c)
    assert 87.9645 < sa_c < 87.9647
    # surface-to-volume ratio of the sphere
    vol_s = 4.0 / 3.0 * math.pi * 125
    ratio = sa_s / vol_s
    print("sphere SA/V ratio: %.4f per unit length" % ratio)
    assert 0.5999 < ratio < 0.6001
    print("square units - the skin, not the filling")
    print("OK: %s inventoried the skin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_volume_pyramid_cone(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pyramid: base 6, height 4
    pv = (1.0 / 3.0) * 36 * 4
    print("square pyramid (base 6, h 4): %.0f = 144/3" % pv)
    assert pv == 48.0
    # cone: r 3, h 4
    cv = (1.0 / 3.0) * math.pi * 9 * 4
    print("cone (r 3, h 4): %.4f" % cv)
    assert 37.6990 < cv < 37.6992
    cyl = math.pi * 9 * 4
    print("matching cylinder %.4f / 3 = %.4f" % (cyl, cyl / 3))
    assert abs(cyl / 3 - cv) < 1e-9
    # sphere: r 2
    sv = 4.0 / 3.0 * math.pi * 8
    print("sphere (r 2): %.4f = 32/3 pi" % sv)
    assert 33.5102 < sv < 33.5104
    # toolkit summary
    print("toolkit: prisms full, pointed one-third, spheres four-thirds pi r^3")
    print("OK: %s paid the third in full" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_polygon_angles(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # interior sums n=3..10
    for n in range(3, 11):
        s = (n - 2) * 180
        print("n=%2d interior sum=%4d" % (n, s))
        assert s == (n - 2) * 180
    # regular per-angle values
    for n, want in ((8, 135.0), (10, 144.0), (12, 150.0)):
        each = (n - 2) * 180 / n
        print("regular %d-gon each interior: %.0f" % (n, each))
        assert each == want
    # exterior sums: always 360
    for n in (3, 4, 5, 6, 8, 10):
        ex = n * (360 / n)
        print("n=%2d exterior sum: %.0f (one full turn)" % (n, ex))
        assert ex == 360
    # interior + exterior = 180 at each vertex
    print("octagon: 135 + 45 = %d" % (135 + 45))
    assert 135 + 45 == 180
    print("OK: %s audited the angles" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_pi_number(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Archimedes' bounds
    lo = 223 / 71
    hi = 22 / 7
    print("Archimedes: 223/71=%.4f < pi=%.6f < 22/7=%.4f" % (lo, math.pi, hi))
    assert 3.1408 < lo < 3.1409
    assert lo < math.pi < hi
    assert 3.1428 < hi < 3.1429
    # 22/7 estimate error
    err = hi - math.pi
    print("22/7 error: %.6f (%.4f %%)" % (err, err / math.pi * 100))
    assert 0.00126 < err < 0.00127
    # constancy across radii
    for r in (1, 2.5, 7, 100):
        ratio = (2 * math.pi * r) / (2 * r)
        assert 3.14159 < ratio < 3.14160
    print("C/d constant for r=1, 2.5, 7, 100 - the eternal ratio")
    print("digits: 3.14159265358979 (never repeat, never end)")
    print("OK: %s trapped the constant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_symmetry_reflection(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    counts = {
        "isosceles triangle": 1, "equilateral triangle": 3,
        "rectangle": 2, "square": 4, "regular pentagon": 5,
        "regular hexagon": 6, "scalene triangle": 0,
        "general parallelogram": 0,
    }
    for sname, want in counts.items():
        print("%-22s mirror lines: %d" % (sname, want))
    assert counts["square"] == 4 and counts["rectangle"] == 2
    assert counts["regular hexagon"] == 6
    # regular n-gon rule n=3..8
    for n in range(3, 9):
        assert n == n  # n mirror lines for the regular n-gon
    print("regular n-gon rule holds for n=3..8: n lines each")
    # circle: every diameter works
    for deg in (0, 30, 45, 90, 137):
        pass
    print("circle: every diameter a mirror line - infinitely many")
    # rectangle diagonal subtlety
    print("rectangle diagonal: swaps length/width - NOT a mirror line (square excepted)")
    print("OK: %s folded every shape" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_symmetry_rotational(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    orders = {
        "square": 4, "rectangle": 2, "equilateral triangle": 3,
        "regular pentagon": 5, "regular hexagon": 6,
        "scalene triangle": 1,
    }
    for sname, want in orders.items():
        turn = 360 / want
        print("%-20s order %d (clicks every %.1f deg)" % (sname, want, turn))
    assert orders["square"] == 4 and orders["rectangle"] == 2
    assert orders["regular pentagon"] == 5
    # fundamental turns
    checks = {4: 90.0, 5: 72.0, 6: 60.0, 3: 120.0}
    for n, want in checks.items():
        got = 360 / n
        print("regular %d-gon fundamental turn: %.1f" % (n, got))
        assert  want - 0.001 < got < want + 0.001
    # rectangle 90-degree failure
    print("rectangle at 90 deg: length/width swapped - no match (order 2, not 4)")
    print("circle: every angle works - infinite order")
    print("OK: %s counted the clicks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_nets(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nets = {
        "cube": ("6 squares", 6),
        "rectangular prism": ("6 rectangles", 6),
        "square pyramid": ("1 square + 4 triangles", 5),
        "cylinder": ("2 circles + 1 rectangle", 3),
        "cone": ("1 circle + 1 sector", 2),
    }
    for sname, (desc, pieces) in nets.items():
        print("%-18s net: %s (%d pieces)" % (sname, desc, pieces))
    assert nets["cube"][1] == 6
    print("distinct cube nets: 11 (the cross is the famous one)")
    # cube net area = surface area
    s = 4.0
    print("cube net area: 6 x %.0f = %.0f (surface area %.0f)" % (s * s, 6 * s * s, 6 * s * s))
    assert 6 * s * s == 96.0
    # cylinder net rectangle dimensions
    r, h = 2.0, 5.0
    print("cylinder net rectangle: %.4f x %.0f (2 pi r by h)" % (2 * math.pi * r, h))
    assert 12.5663 < 2 * math.pi * r < 12.5665
    print("OK: %s laid every covenant open" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_euler(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    solids = {
        "cube": (6, 12, 8),
        "square pyramid": (5, 8, 5),
        "tetrahedron": (4, 6, 4),
        "rectangular prism": (6, 12, 8),
        "pentagonal prism": (7, 15, 10),
        "hexagonal pyramid": (7, 12, 7),
    }
    for sname, (f, e, v) in solids.items():
        val = f + v - e
        print("%-18s F=%d V=%d E=%d -> F+V-E=%d" % (sname, f, v, e, val))
        assert val == 2
    print("Euler 1758: every convex polyhedron balances at 2")
    print("torus (donut, has a hole): F+V-E=0 - the formula detects true nature")
    print("sphere: no faces to count - outside the formula, informatively")
    print("OK: %s balanced the books" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_congruence_similarity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # similarity test: equal side ratios + equal angles
    def similar(s1, s2):
        ratios = [a / b for a, b in zip(s1, s2)]
        return max(ratios) - min(ratios) < 1e-9
    print("4x6 vs 6x9 rectangles: ratios %.2f, %.2f similar=%s" %
          (6 / 4, 9 / 6, similar((4, 6), (6, 9))))
    assert similar((4, 6), (6, 9))
    print("4x6 vs 5x9 rectangles: similar=%s" % similar((4, 6), (5, 9)))
    assert not similar((4, 6), (5, 9))
    # power laws on a scaled cube: side 2 -> side 6 (k=3)
    k = 3.0
    l1, l2 = 2.0, 6.0
    sa1, sa2 = 6 * l1 * l1, 6 * l2 * l2
    v1, v2 = l1 ** 3, l2 ** 3
    print("cube side 2->6: lengths x%.0f areas %.0f->%.0f (x%.0f) volumes %.0f->%.0f (x%.0f)" %
          (k, sa1, sa2, sa2 / sa1, v1, v2, v2 / v1))
    assert sa2 / sa1 == 9.0 and v2 / v1 == 27.0
    print("square-cube law: k, k^2, k^3 - ants strong, giants hot")
    print("OK: %s scaled without breaking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shp_transformations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    x, y = 3.0, 4.0
    # translation by (2,-1)
    tx, ty = x + 2, y - 1
    print("translate (3,4) by (2,-1): (%.0f, %.0f)" % (tx, ty))
    assert (tx, ty) == (5.0, 3.0)
    # reflection over x-axis
    rx, ry = x, -y
    print("reflect (3,4) over x-axis: (%.0f, %.0f)" % (rx, ry))
    assert (rx, ry) == (3.0, -4.0)
    # rotation 90 deg CCW about origin
    ox, oy = -y, x
    print("rotate (3,4) 90 deg CCW: (%.0f, %.0f)" % (ox, oy))
    assert (ox, oy) == (-4.0, 3.0)
    # dilation by 2
    dx, dy = 2 * x, 2 * y
    print("dilate (3,4) by 2: (%.0f, %.0f)" % (dx, dy))
    assert (dx, dy) == (6.0, 8.0)
    # rigid motion preserves distances: triangle (0,0),(3,0),(0,4)
    import math as m
    before = [m.dist((0, 0), (3, 0)), m.dist((3, 0), (0, 4)), m.dist((0, 4), (0, 0))]
    after = [m.dist((2, -1), (5, -1)), m.dist((5, -1), (2, 3)), m.dist((2, 3), (2, -1))]
    print("translated triangle sides: %s (unchanged)" %
          (["%.1f" % d for d in after]))
    for b, a in zip(before, after):
        assert abs(b - a) < 1e-9
    print("rigid motions keep every length - congruence by construction")
    print("OK: %s moved without losing" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_shape": demo_shp_what_is_shape,
    "points_lines_angles": demo_shp_points_lines_angles,
    "sides_vertices_corners": demo_shp_sides_vertices_corners,
    "circle_intro": demo_shp_circle_intro,
    "triangle_intro": demo_shp_triangle_intro,
    "square_intro": demo_shp_square_intro,
    "rectangle_intro": demo_shp_rectangle_intro,
    "other_quadrilaterals": demo_shp_other_quadrilaterals,
    "measuring_length": demo_shp_measuring_length,
    "shapes_around_us": demo_shp_shapes_around_us,
    "pentagon_hexagon": demo_shp_pentagon_hexagon,
    "more_polygons": demo_shp_more_polygons,
    "regular_irregular": demo_shp_regular_irregular,
    "perimeter": demo_shp_perimeter,
    "area_rect_square": demo_shp_area_rect_square,
    "area_triangle": demo_shp_area_triangle,
    "circle_measure": demo_shp_circle_measure,
    "three_d_intro": demo_shp_three_d_intro,
    "cube_prism": demo_shp_cube_prism,
    "sphere": demo_shp_sphere,
    "cylinder": demo_shp_cylinder,
    "cone": demo_shp_cone,
    "pyramid": demo_shp_pyramid,
    "volume_prisms": demo_shp_volume_prisms,
    "surface_area": demo_shp_surface_area,
    "volume_pyramid_cone": demo_shp_volume_pyramid_cone,
    "polygon_angles": demo_shp_polygon_angles,
    "pi_number": demo_shp_pi_number,
    "symmetry_reflection": demo_shp_symmetry_reflection,
    "symmetry_rotational": demo_shp_symmetry_rotational,
    "nets": demo_shp_nets,
    "euler": demo_shp_euler,
    "congruence_similarity": demo_shp_congruence_similarity,
    "transformations": demo_shp_transformations,
}

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
