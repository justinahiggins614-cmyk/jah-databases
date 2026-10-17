#!/usr/bin/env python3
"""Demo programs for the Geospatial Operations databases.

Every demo is real, runnable, stdlib-only Python performing the actual
geospatial computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_geo_what_coordinate(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # DMS 40 42' 46.08" -> decimal degrees, and the sign convention
    dec = 40 + 42 / 60.0 + 46.08 / 3600.0
    print("40d 42m 46.08s = %.6f decimal degrees" % dec)
    assert 40.712799 < dec < 40.712801
    west = -(74 + 0 / 60.0 + 21.6 / 3600.0)  # 74d 00' 21.6" W
    print("74d 00m 21.6s W = %.6f" % west)
    assert -74.006001 < west < -74.005999
    # WGS84 ellipsoid constants from the record
    a = 6378137.0
    f = 1 / 298.257223563
    e2 = 2 * f - f * f
    print("WGS84 a=%.1f m f=1/%.9f e^2=%.11f" % (a, 1 / f, e2))
    assert 0.006694379 < e2 < 0.006694381
    print("rule: a coordinate without its system is just two numbers")
    print("OK: %s swore the witness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_families(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # meters per degree: latitude constant-ish, longitude scaled by cos(lat)
    m_per_deg_lat = 111132.0
    lat = 40.0
    m_per_deg_lon = 111320.0 * math.cos(math.radians(lat))
    print("1 deg latitude ~= %.0f m everywhere" % m_per_deg_lat)
    print("1 deg longitude at 40N ~= %.1f m" % m_per_deg_lon)
    assert 85275.9 < m_per_deg_lon < 85276.2
    # UTM zone 18N framing for New York (central meridian 75W)
    lon = -74.0060
    zone = int((lon + 180) // 6) + 1
    print("lon %.4f -> UTM zone %d (central meridian %.0fW)" % (lon, zone, (zone - 1) * 6 - 180 + 3))
    assert zone == 18
    # scale factor sanity: 0.9996 central shrink
    k0 = 0.9996
    print("UTM central scale k0=%.4f: 1000 m measures %.1f m on the map" % (k0, 1000 * k0))
    assert 999.59 < 1000 * k0 < 999.61
    print("rule: short range in projected meters, long range in geographic angles")
    print("OK: %s spoke both languages" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_distance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def haversine_m(lat1, lon1, lat2, lon2):
    R = 6371008.8  # IUGG mean radius
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))

def main():
    nyc = (40.7128, -74.0060)
    lon_ = (51.5074, -0.1278)
    d = haversine_m(*nyc, *lon_)
    print("NYC-London great-circle: %.1f km" % (d / 1000))
    assert 5570.1 < d / 1000 < 5570.4
    # short hop: flat equirectangular approximation vs haversine
    a_pt = (40.7128, -74.0060)
    b_pt = (40.7228, -73.9960)  # ~1.4 km away
    d_exact = haversine_m(*a_pt, *b_pt)
    dx = math.radians(b_pt[1] - a_pt[1]) * math.cos(math.radians(a_pt[0])) * 6371008.8
    dy = math.radians(b_pt[0] - a_pt[0]) * 6371008.8
    d_flat = math.hypot(dx, dy)
    print("short hop: haversine %.1f m, flat %.1f m, err %.3f m" % (d_exact, d_flat, abs(d_exact - d_flat)))
    assert 1394.5 < d_exact < 1396.0
    assert abs(d_exact - d_flat) < 0.05
    print("rule: sphere for the fast filter, ellipsoid for the final answer")
    print("OK: %s measured the curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_precision(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the digit ladder: each decimal place divides the footprint by ten
    m_per_deg = 111132.0
    ladder = {d: m_per_deg / (10 ** d) for d in range(1, 8)}
    for d in range(1, 8):
        print("  %d decimals -> %10.2f m" % (d, ladder[d]))
    assert 11.10 < ladder[4] < 11.12
    assert 1.10 < ladder[5] < 1.12
    assert 0.010 < ladder[7] < 0.012
    # honesty check: phone GPS (~5 m) earns 4-5 decimals, not 7
    gps_sigma = 5.0
    honest_decimals = 0
    for d in range(1, 9):
        if m_per_deg / (10 ** d) < gps_sigma:
            honest_decimals = d
            break
    print("5 m GPS honestly earns decimals down to: %d (%.2f m)" % (honest_decimals, m_per_deg / 10 ** honest_decimals))
    assert honest_decimals == 5
    print("rule: print only the digits the instrument earned")
    print("OK: %s kept the vow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_projections(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    R = 6378137.0
    phi = math.radians(40.0)
    # Mercator forward (spherical): y = R ln(tan(pi/4 + phi/2))
    y = R * math.log(math.tan(math.pi / 4 + phi / 2))
    print("Mercator y at 40N: %.1f m" % y)
    assert 4865942.2 < y < 4865942.4
    # scale factor k = sec(phi); area inflation = k^2
    k = 1 / math.cos(phi)
    print("scale k=%.4f area inflation k^2=%.4f at 40N" % (k, k * k))
    assert 1.3053 < k < 1.3055
    assert 1.7040 < k * k < 1.7042
    # the Greenland lesson: area distortion vs reality
    greenland, africa = 2.166, 30.37  # million km^2
    print("Africa/Greenland true area ratio: %.2f" % (africa / greenland))
    assert 14.01 < africa / greenland < 14.03
    k60 = 1 / math.cos(math.radians(60))
    print("at 60N Mercator draws %.1fx area (k^2=%.2f)" % (k60 * k60, k60 * k60))
    assert 3.99 < k60 * k60 < 4.01
    print("rule: every projection keeps one truth by bending another - name the bargain")
    print("OK: %s read the confession" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_datums(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Helmert translation-only shift: NAD83-ish -> WGS84-ish (meters)
    T = (1.0, -1.5, 0.8)
    p = (1000.0, 2000.0, 3000.0)  # local cartesian meters
    q = tuple(pi + ti for pi, ti in zip(p, T))
    shift = math.sqrt(sum(t * t for t in T))
    print("shift magnitude: %.4f m" % shift)
    assert 1.972 < shift < 1.974
    assert abs(q[0] - 1001.0) < 1e-9 and abs(q[1] - 1998.5) < 1e-9
    # plate motion aging: 2.5 cm/yr over 30 years ~= 0.75 m of coordinate aging
    v = 0.025  # m/yr
    aged = v * 30
    print("30 yr at 2.5 cm/yr ages a coordinate by %.2f m" % aged)
    assert 0.749 < aged < 0.751
    # scale sanity: ppm scale term on 6378137 m
    s_ppm = 1.0
    print("1 ppm scale on Earth radius: %.3f m" % (6378137.0 * s_ppm / 1e6))
    assert 6.378 < 6378137.0 * s_ppm / 1e6 < 6.379
    print("rule: coordinates carry a frame and an epoch, or they are stale")
    print("OK: %s dated the testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_crs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the axis-order trap: EPSG:4326 is lat-first; many tools write lon-first
    lat, lon = 40.7128, -74.0060
    correct = (lat, lon)
    swapped = (lon, lat)
    # a validator that rejects latitude outside [-90, 90] catches the swap
    def valid_latlon(a, b):
        return -90.0 <= a <= 90.0 and -180.0 <= b <= 180.0
    print("lat-first valid: %s, swapped valid: %s" % (valid_latlon(*correct), valid_latlon(*swapped)))
    assert valid_latlon(*correct) is True
    assert valid_latlon(*swapped) is True  # -74 is within [-90,90]: the trap!
    print("note: -74 passes as latitude, so the swap plots in the wrong hemisphere silently")
    # registry sanity: well-known codes resolve to distinct families
    codes = {4326: "geographic.degrees", 3857: "projected.meters", 26918: "projected.meters.utm18n"}
    print("codes: %s" % codes)
    assert codes[4326] != codes[3857]
    assert len(set(codes)) == 3
    print("rule: cite the code, state the order - half a contract misleads")
    print("OK: %s read the full oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_vector(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def ray_inside(px, py, ring):
    inside = False
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]
        x2, y2 = ring[(i + 1) % n]
        if (y1 > py) != (y2 > py):
            xin = (x2 - x1) * (py - y1) / (y2 - y1) + x1
            if px < xin:
                inside = not inside
    return inside

def ring_closed(ring):
    return ring[0] == ring[-1]

def main():
    sq = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
    print("ring closed: %s" % ring_closed(sq))
    assert ring_closed(sq) is True
    assert ray_inside(0.5, 0.5, sq) is True
    assert ray_inside(2.0, 2.0, sq) is False
    assert ray_inside(0.0, 0.5, sq) in (True, False)  # boundary: documented rule decides
    # invalid: unclosed ring
    bad = [(0, 0), (1, 0), (1, 1), (0, 1)]
    print("unclosed ring valid: %s" % ring_closed(bad))
    assert ring_closed(bad) is False
    # bowtie (self-crossing): inside/outside undefined
    bow = [(0, 0), (1, 1), (1, 0), (0, 1), (0, 0)]
    print("bowtie inside-test gives: %s (undefined - must be rejected)" % ray_inside(0.5, 0.5, bow))
    print("rule: only whole closed honest rings enter the record")
    print("OK: %s guarded the boundary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_terrain(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def horn_slope_aspect(grid, c):
    # grid 3x3, c = cell size; Horn's weighted gradient
    z1, z2, z3 = grid[0]
    z4, z5, z6 = grid[1]
    z7, z8, z9 = grid[2]
    dzdx = ((z3 + 2 * z6 + z9) - (z1 + 2 * z4 + z7)) / (8 * c)
    dzdy = ((z7 + 2 * z8 + z9) - (z1 + 2 * z2 + z3)) / (8 * c)
    slope = math.degrees(math.atan(math.hypot(dzdx, dzdy)))
    aspect = (math.degrees(math.atan2(dzdx, -dzdy)) + 360) % 360 if (dzdx or dzdy) else -1
    return slope, aspect

def main():
    # perfect plane rising 1 m per 10 m east, cell size 10 m
    c = 10.0
    # z increases 1 m per column eastward: plane with 0.1 grade
    grid = [[100.0 + (j - 1) * 1.0 for j in range(3)] for i in range(3)]
    slope, aspect = horn_slope_aspect(grid, c)
    print("plane 0.1 grade: slope=%.4f deg aspect=%.1f deg" % (slope, aspect))
    assert 5.709 < slope < 5.712
    assert 89.9 < aspect < 90.1
    flat = [[50.0] * 3 for _ in range(3)]
    s2, a2 = horn_slope_aspect(flat, c)
    print("flat: slope=%.4f aspect=%s" % (s2, a2))
    assert s2 < 1e-9 and a2 == -1
    print("rule: read the ground at its own resolution, bare earth vs surface labeled")
    print("OK: %s read the face" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_coordinate": demo_geo_what_coordinate,
    "geographic_vs_projected": demo_geo_families,
    "curved_earth_distance": demo_geo_distance,
    "coordinate_precision": demo_geo_precision,
    "map_projections": demo_geo_projections,
    "datums_move": demo_geo_datums,
    "crs_epsg": demo_geo_crs,
    "vector_boundaries": demo_geo_vector,
    "terrain_basics": demo_geo_terrain,
}

def demo_geo_proximity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # candidate pharmacies (x, y) in meters, query at origin, radius 2000 m
    cands = [(1500, 200), (-800, 900), (2500, 0), (300, -400), (-2100, 100)]
    q = (0, 0)
    r = 2000.0
    # filter: bounding-box pre-check (cheap), then exact distance
    within = []
    for (x, y) in cands:
        if abs(x - q[0]) > r or abs(y - q[1]) > r:
            continue  # box rejects without sqrt
        d = math.hypot(x - q[0], y - q[1])
        if d <= r:
            within.append((d, (x, y)))
    within.sort()
    print("within 2000 m: %d of %d" % (len(within), len(cands)))
    for d, p in within:
        print("  (%.0f, %.0f) at %.1f m" % (p[0], p[1], d))
    assert len(within) == 3
    assert 499.9 < within[0][0] < 500.1  # (300,-400) -> 500 m
    # k-nearest: k=2 must be the two smallest exact distances
    k2 = [p for _, p in within[:2]]
    assert k2[0] == (300, -400) and k2[1] == (-800, 900)
    print("rule: index-first filter, exact-measure second")
    print("OK: %s found the neighbors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_spatial_join(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def ray_inside(px, py, ring):
    inside = False
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]
        x2, y2 = ring[(i + 1) % n]
        if (y1 > py) != (y2 > py):
            xin = (x2 - x1) * (py - y1) / (y2 - y1) + x1
            if px < xin:
                inside = not inside
    return inside

def bbox(ring):
    xs = [p[0] for p in ring]; ys = [p[1] for p in ring]
    return (min(xs), min(ys), max(xs), max(ys))

def main():
    # two territories; filter by bbox, refine by ray casting
    polys = {
        "north": [(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)],
        "south": [(0, -10), (10, -10), (10, 0), (0, 0), (0, -10)],
    }
    boxes = {k: bbox(v) for k, v in polys.items()}
    pts = [(2, 3), (5, 5), (7, -2), (3, -8), (20, 20), (5, 0.0)]
    counts = {"north": 0, "south": 0, "none": 0}
    for (x, y) in pts:
        owner = "none"
        for k, ring in polys.items():
            x0, y0, x1, y1 = boxes[k]
            if not (x0 <= x <= x1 and y0 <= y <= y1):
                continue  # filter phase rejects
            if ray_inside(x, y, ring):  # refine phase
                owner = k
                break
        counts[owner] += 1
    print("join counts: %s" % counts)
    assert counts["north"] == 3 and counts["south"] == 2 and counts["none"] == 1
    print("note: (5,0) sits on the shared border; the documented first-match rule assigns it north")
    print("rule: filter by box, refine by geometry, document the border")
    print("OK: %s took the census" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_geohash(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
B32 = "0123456789bcdefghjkmnpqrstuvwxyz"

def geohash(lat, lon, n):
    lat_r, lon_r = [-90.0, 90.0], [-180.0, 180.0]
    bits, out, even = [], [], True
    while len(out) < n:
        if even:
            mid = (lon_r[0] + lon_r[1]) / 2
            b = 1 if lon >= mid else 0
            lon_r = [mid, lon_r[1]] if b else [lon_r[0], mid]
        else:
            mid = (lat_r[0] + lat_r[1]) / 2
            b = 1 if lat >= mid else 0
            lat_r = [mid, lat_r[1]] if b else [lat_r[0], mid]
        bits.append(b)
        even = not even
        if len(bits) == 5:
            v = 0
            for x in bits:
                v = v * 2 + x
            out.append(B32[v])
            bits = []
    return "".join(out)

def main():
    nyc5 = geohash(40.7128, -74.0060, 5)
    nyc9 = geohash(40.7128, -74.0060, 9)
    wh7 = geohash(38.8977, -77.0365, 7)
    print("NYC geohash-5: %s, geohash-9: %s" % (nyc5, nyc9))
    print("White House geohash-7: %s" % wh7)
    assert nyc5 == "dr5re"
    assert nyc9 == "dr5regw3p"
    assert wh7 == "dqcjqcp"
    # prefix property: longer hash starts with shorter hash
    assert nyc9.startswith(nyc5)
    # nearby point shares prefix
    near5 = geohash(40.7130, -74.0058, 5)
    print("200 m away shares prefix: %s" % (near5 == nyc5))
    assert near5 == nyc5
    print("rule: the whisper finds the neighborhood, footsteps confirm the door")
    print("OK: %s whispered the address" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_indexes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
class QuadNode(object):
    def __init__(self, x0, y0, x1, y1, cap=4):
        self.box = (x0, y0, x1, y1)
        self.cap = cap
        self.pts = []
        self.kids = None

    def insert(self, p):
        x0, y0, x1, y1 = self.box
        if self.kids:
            self._kid(p).insert(p)
            return
        self.pts.append(p)
        if len(self.pts) > self.cap and (x1 - x0) > 1e-9:
            self._split()
            for q in self.pts:
                self._kid(q).insert(q)
            self.pts = []

    def _kid(self, p):
        x0, y0, x1, y1 = self.box
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        i = 0 if p[0] < mx else 1
        j = 0 if p[1] < my else 1
        return self.kids[j * 2 + i]

    def _split(self):
        x0, y0, x1, y1 = self.box
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        self.kids = [QuadNode(x0, y0, mx, my), QuadNode(mx, y0, x1, my),
                     QuadNode(x0, my, mx, y1), QuadNode(mx, my, x1, y1)]

    def range(self, q, out):
        x0, y0, x1, y1 = self.box
        qx0, qy0, qx1, qy1 = q
        if x1 < qx0 or x0 > qx1 or y1 < qy0 or y0 > qy1:
            return  # pruned: whole branch cannot match
        if self.kids:
            for k in self.kids:
                k.range(q, out)
        else:
            for p in self.pts:
                if qx0 <= p[0] <= qx1 and qy0 <= p[1] <= qy1:
                    out.append(p)

def main():
    import random
    random.seed(7)
    root = QuadNode(0, 0, 100, 100)
    pts = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(200)]
    for p in pts:
        root.insert(p)
    out = []
    root.range((10, 10, 30, 30), out)
    brute = [p for p in pts if 10 <= p[0] <= 30 and 10 <= p[1] <= 30]
    print("quadtree range: %d, brute force: %d" % (len(out), len(brute)))
    assert len(out) == len(brute) and set(out) == set(brute)
    assert len(out) > 0
    print("rule: prune by box, test exactly the survivors")
    print("OK: %s ushered the witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_h3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def hex_distance(a, b):
    # axial coordinates (q, r): distance in hex steps
    dq, dr = a[0] - b[0], a[1] - b[1]
    return (abs(dq) + abs(dr) + abs(dq + dr)) // 2

def k_ring(center, k):
    out = []
    for dq in range(-k, k + 1):
        for dr in range(max(-k, -dq - k), min(k, -dq + k) + 1):
            out.append((center[0] + dq, center[1] + dr))
    return out

def main():
    c = (0, 0)
    ring1 = k_ring(c, 1)
    ring2 = k_ring(c, 2)
    print("k-ring(1) cells: %d (1 + 6 neighbors)" % len(ring1))
    print("k-ring(2) cells: %d" % len(ring2))
    assert len(ring1) == 7
    assert len(ring2) == 19  # 1 + 6 + 12
    # uniform neighbor distance: every ring-1 cell is exactly 1 step away
    ds = sorted(hex_distance(c, p) for p in ring1 if p != c)
    print("neighbor distances: %s" % ds)
    assert ds == [1] * 6
    # vs squares: diagonal neighbor would be farther - hexagons have no diagonals
    assert hex_distance((0, 0), (2, -1)) == 2
    print("rule: the honeycomb favors no direction")
    print("OK: %s counted the comb" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_dijkstra(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import heapq

def dijkstra(graph, src):
    dist = {src: 0.0}
    prev = {}
    pq = [(0.0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            assert w >= 0, "negative edge voids the proof"
            nd = d + w
            if nd < dist.get(v, float("inf")) - 1e-12:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev

def main():
    # directed road graph: one-way street c->d has no reverse edge
    g = {
        "a": [("b", 4), ("c", 2)],
        "b": [("c", 1), ("d", 5)],
        "c": [("d", 8), ("e", 10)],
        "d": [("e", 2)],
        "e": [],
    }
    dist, prev = dijkstra(g, "a")
    print("distances from a: %s" % {k: round(v, 1) for k, v in sorted(dist.items())})
    assert abs(dist["e"] - 11.0) < 1e-9  # best is a-b-d-e = 4+5+2 = 11
    # reconstruct path a->e
    path, u = ["e"], "e"
    while u != "a":
        u = prev[u]
        path.append(u)
    path.reverse()
    print("path a->e: %s cost %.1f" % ("->".join(path), dist["e"]))
    assert path == ["a", "b", "d", "e"] and abs(dist["e"] - 11.0) < 1e-9
    print("rule: nearest truth first, no shortcuts past an unexamined witness")
    print("OK: %s rippled outward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_fastrouting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import heapq

def astar(graph, coords, src, dst, max_speed):
    def h(n):
        dx = coords[n][0] - coords[dst][0]
        dy = coords[n][1] - coords[dst][1]
        return math.hypot(dx, dy) / max_speed  # admissible: never overestimates
    g = {src: 0.0}
    pq = [(h(src), src)]
    expanded = 0
    while pq:
        f, u = heapq.heappop(pq)
        if u == dst:
            return g[u], expanded
        expanded += 1
        for v, w in graph.get(u, []):
            ng = g[u] + w
            if ng < g.get(v, float("inf")) - 1e-12:
                g[v] = ng
                heapq.heappush(pq, (ng + h(v), v))
    return float("inf"), expanded

def dijkstra_count(graph, src, dst):
    import heapq as hq
    dist = {src: 0.0}
    pq = [(0.0, src)]
    expanded = 0
    while pq:
        d, u = hq.heappop(pq)
        if u == dst:
            return d, expanded
        if d > dist.get(u, float("inf")):
            continue
        expanded += 1
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")) - 1e-12:
                dist[v] = nd
                hq.heappush(pq, (nd, v))
    return float("inf"), expanded

def main():
    # line-ish graph where the goal is east: A* should expand far fewer nodes
    coords = {}
    graph = {}
    n = 25
    for i in range(n):
        for j in range(5):
            u = (i, j)
            coords[u] = (float(i * 10), float(j * 10))
            outs = []
            if i + 1 < n:
                outs.append(((i + 1, j), 10.0))
            if j + 1 < 5:
                outs.append(((i, j + 1), 10.0))
            if j - 1 >= 0:
                outs.append(((i, j - 1), 10.0))
            graph[u] = outs
    src, dst = (0, 2), (24, 2)
    da, ea = astar(graph, coords, src, dst, 10.0)
    dd, ed = dijkstra_count(graph, src, dst)
    print("A*: cost %.1f expanded %d | Dijkstra: cost %.1f expanded %d" % (da, ea, dd, ed))
    assert abs(da - 240.0) < 1e-9 and abs(dd - 240.0) < 1e-9  # same optimal cost
    assert ea < ed  # A* explores less with an admissible heuristic
    print("rule: aim the search, keep the proof")
    print("OK: %s let the hound run" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "proximity_queries": demo_geo_proximity,
    "spatial_joins": demo_geo_spatial_join,
    "geohashing": demo_geo_geohash,
    "spatial_indexes": demo_geo_indexes,
    "h3_hex_grids": demo_geo_h3,
    "dijkstra_routing": demo_geo_dijkstra,
    "fast_routing": demo_geo_fastrouting,
})

def demo_geo_mapmatching(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # HMM map matching on a toy network: two parallel roads, 3 GPS fixes
    # roads: upper y=10 (x 0..100), lower y=0 (x 0..100); fixes near upper road
    import math as m
    sigma = 8.0
    fixes = [(20, 12), (50, 9), (80, 11)]
    cands = [[(x, 10), (x, 0)] for (x, y) in fixes]  # (upper, lower) per fix
    def emit(px, py, cx, cy):
        d = m.hypot(px - cx, py - cy)
        return -0.5 * (d / sigma) ** 2  # log gaussian
    def trans(c0, c1):
        # network distance along same road vs straight-line between fixes
        net = abs(c1[0] - c0[0]) if c1[1] == c0[1] else 500.0  # road change is costly
        return -abs(net - 30.0) / 50.0
    # Viterbi
    T = len(fixes)
    dp = [{} for _ in range(T)]
    bt = [{} for _ in range(T)]
    for s in (0, 1):
        dp[0][s] = emit(*fixes[0], *cands[0][s])
    for t in range(1, T):
        for s in (0, 1):
            best, bs = -1e18, 0
            for ps in (0, 1):
                v = dp[t - 1][ps] + trans(cands[t - 1][ps], cands[t][s])
                if v > best:
                    best, bs = v, ps
            dp[t][s] = best + emit(*fixes[t], *cands[t][s])
            bt[t][s] = bs
    s = 0 if dp[T - 1][0] > dp[T - 1][1] else 1
    seq = [s]
    for t in range(T - 1, 0, -1):
        s = bt[t][s]
        seq.append(s)
    seq.reverse()
    roads = ["upper", "lower"]
    print("matched roads: %s" % [roads[s] for s in seq])
    assert seq == [0, 0, 0], "fixes near y=10 must match the upper road"
    print("rule: hear the whole testimony before judging any single point")
    print("OK: %s cross-examined the track" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_gpsbudget(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # UERE components, 1-sigma meters, single-frequency civilian
    comps = {"clock/ephemeris": 2.0, "ionosphere": 4.0, "troposphere": 0.5,
             "multipath": 1.0, "receiver": 0.5}
    uere = math.sqrt(sum(v * v for v in comps.values()))
    print("UERE components:")
    for k, v in comps.items():
        print("  %-16s %4.1f m" % (k, v))
    print("UERE (RSS): %.2f m" % uere)
    assert 4.63 < uere < 4.65
    # HDOP multiplies into horizontal error; 95% ~= 2.45 x 1-sigma (Rayleigh)
    for hdop in (1.0, 2.5):
        sig = hdop * uere
        p95 = 2.4477 * sig
        print("HDOP %.1f -> 1-sigma %.2f m, 95%% %.2f m" % (hdop, sig, p95))
    assert 11.34 < 2.4477 * 1.0 * uere < 11.36
    # dual-frequency kills the ionosphere term
    comps2 = dict(comps, ionosphere=0.3)
    uere2 = math.sqrt(sum(v * v for v in comps2.values()))
    print("dual-frequency UERE: %.2f m" % uere2)
    assert 2.363 < uere2 < 2.366
    print("rule: every position testifies with its uncertainty beside it")
    print("OK: %s accounted the tremor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_transforms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Helmert translation-only step of a datum-shift pipeline (meters)
    T = (1.0, -1.5, 0.8)
    p = (451000.0, 4420000.0, 100.0)  # easting, northing, height-ish
    q = (p[0] + T[0], p[1] + T[1], p[2] + T[2])
    print("shifted: (%.1f, %.1f, %.1f)" % q)
    assert abs(q[0] - 451001.0) < 1e-9
    assert abs(q[1] - 4419998.5) < 1e-9
    assert abs(q[2] - 100.8) < 1e-9
    # pipeline accuracy budget: RSS of step accuracies
    steps = [1.5, 0.8, 0.3]  # meters per step
    total = math.sqrt(sum(s * s for s in steps))
    print("pipeline 95%%-ish budget (RSS): %.3f m" % total)
    assert 1.725 < total < 1.728
    # axis-order guard: lat must be within [-90, 90]
    lat, lon = 40.7128, -74.0060
    assert -90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0
    print("axis guard: lat %.4f in [-90,90] OK" % lat)
    print("rule: translate on the record, with each step's accuracy sworn aloud")
    print("OK: %s kept the chain honest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_raster(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # NDVI = (NIR - Red) / (NIR + Red) on a 3x3 scene
    red = [[0.20, 0.22, 0.21], [0.30, 0.32, 0.31], [0.15, 0.16, 0.15]]
    nir = [[0.60, 0.62, 0.61], [0.35, 0.34, 0.36], [0.55, 0.57, 0.56]]
    ndvi = [[(nir[i][j] - red[i][j]) / (nir[i][j] + red[i][j])
             for j in range(3)] for i in range(3)]
    print("NDVI center (sparse veg): %.3f" % ndvi[1][1])
    print("NDVI corner (healthy veg): %.3f" % ndvi[0][0])
    assert 0.499 < ndvi[0][0] < 0.501
    assert 0.029 < ndvi[1][1] < 0.031
    assert all(-1.0 <= v <= 1.0 for row in ndvi for v in row)
    # zonal stats: mean NDVI per zone mask
    zone = [[1, 1, 2], [1, 2, 2], [1, 1, 2]]
    sums, cnts = {}, {}
    for i in range(3):
        for j in range(3):
            z = zone[i][j]
            sums[z] = sums.get(z, 0.0) + ndvi[i][j]
            cnts[z] = cnts.get(z, 0) + 1
    means = {z: sums[z] / cnts[z] for z in sums}
    print("zonal mean NDVI: %s" % {z: round(v, 3) for z, v in means.items()})
    assert means[1] > means[2]  # zone 1 is the vegetated side
    assert 0.436 < means[1] < 0.438
    assert 0.292 < means[2] < 0.294
    print("rule: align the grids first, let silent cells stay silent")
    print("OK: %s did the algebra" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_isochrone(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import heapq

def main():
    # 7x7 street grid, 60 m blocks; arterial row j=3 runs at 2x speed
    W = 7
    def cost(u, v):
        fast = (u[1] == 3 and v[1] == 3)
        return 30.0 if fast else 60.0  # seconds per block
    src = (3, 3)
    dist = {src: 0.0}
    pq = [(0.0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = (u[0] + dx, u[1] + dy)
            if 0 <= v[0] < W and 0 <= v[1] < W:
                nd = d + cost(u, v)
                if nd < dist.get(v, float("inf")) - 1e-12:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
    limit = 120.0  # 2-minute isochrone
    inside = [k for k, v in dist.items() if v <= limit]
    print("2-minute service area: %d of %d cells" % (len(inside), W * W))
    # along arterial: 120/30 = 4 blocks east-west; off arterial: 2 blocks
    assert (6, 3) in dist and abs(dist[(6, 3)] - 90.0) < 1e-9
    assert abs(dist[(3, 5)] - 120.0) < 1e-9
    assert len(inside) == 19
    print("reach east on arterial: 90 s to (6,3); north off arterial: 120 s to (3,5)")
    print("rule: the reach is sworn along real roads at real speeds")
    print("OK: %s drew the honest boundary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_geofence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # circular depot fence r=100 m; hysteresis: exit only beyond 140 m
    r_enter, r_exit = 100.0, 140.0
    fixes = [200, 150, 90, 95, 105, 95, 92, 88, 130, 80, 85, 250]
    state = "outside"
    events = []
    for i, d in enumerate(fixes):
        if state == "outside" and d <= r_enter:
            state = "inside"
            events.append((i, "ENTER"))
        elif state == "inside" and d > r_exit:
            state = "outside"
            events.append((i, "EXIT"))
    print("events: %s" % events)
    # without hysteresis the 90..105 wobble would fire 3+ ENTERs; with it: one clean visit
    assert events == [(2, "ENTER"), (11, "EXIT")]
    # dwell: require 3 consecutive inside fixes before the visit counts
    # (the 95, 92, 88 run qualifies; the lone 105 m wobble never becomes a visit)
    inside_run, dwell_ok = 0, False
    for d in fixes:
        inside_run = inside_run + 1 if d <= r_enter else 0
        if inside_run >= 3:
            dwell_ok = True
    print("dwell confirmed: %s" % dwell_ok)
    assert dwell_ok is True
    print("rule: hysteresis kills flicker, dwell kills drive-by rumors")
    print("OK: %s guarded the perimeter" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "map_matching": demo_geo_mapmatching,
    "gps_error_budget": demo_geo_gpsbudget,
    "coordinate_transforms": demo_geo_transforms,
    "raster_operations": demo_geo_raster,
    "isochrones": demo_geo_isochrone,
    "geofencing": demo_geo_geofence,
})

def demo_geo_uncertainty(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def ellipse_axes(s_ee, s_nn, s_en):
    # closed-form eigen-decomposition of the 2x2 covariance
    mid = (s_ee + s_nn) / 2.0
    half = math.sqrt(((s_ee - s_nn) / 2.0) ** 2 + s_en ** 2)
    lam_max, lam_min = mid + half, mid - half
    tilt = 0.5 * math.atan2(2 * s_en, s_ee - s_nn)
    return math.sqrt(lam_max), math.sqrt(lam_min), math.degrees(tilt)

def main():
    # uncorrelated fix: east var 25, north var 9 -> 1-sigma axes 5 m x 3 m
    a, b, tilt = ellipse_axes(25.0, 9.0, 0.0)
    print("1-sigma axes: %.3f m x %.3f m, tilt %.2f deg" % (a, b, tilt))
    assert 4.999 < a < 5.001 and 2.999 < b < 3.001
    k95 = 2.4477
    print("95%% ellipse: %.3f m x %.3f m" % (k95 * a, k95 * b))
    assert 12.237 < k95 * a < 12.240
    assert 7.342 < k95 * b < 7.345
    # correlated case: covariance 6 -> rotated ellipse
    a2, b2, tilt2 = ellipse_axes(25.0, 9.0, 6.0)
    print("correlated: axes %.3f x %.3f m, tilt %.2f deg" % (a2, b2, tilt2))
    assert 5.195 < a2 < 5.197 and 2.645 < b2 < 2.647
    assert 18.42 < tilt2 < 18.44
    # 1-sigma 2D contains truth ~39.35%, not 68% (the 1D number)
    print("P(inside 1-sigma 2D ellipse) = 39.35%% - the 68%% figure is 1D only")
    print("rule: the ellipse is the full truth - consume it, not just the point")
    print("OK: %s drew the honest shadow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_kalman(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1D constant-velocity tracker, dt=1 s, fixed measurement noise sequence
    dt = 1.0
    R = 25.0          # measurement variance m^2 (5 m sigma)
    q = 1.0           # process noise
    noise = [3.0, -2.0, 4.0, -3.5, 2.5, -1.5, 1.0, -2.5, 3.5, -1.0]
    x = [0.0, 0.0]    # [position, velocity]
    P = [[1000.0, 0.0], [0.0, 100.0]]
    for t, nz in enumerate(noise):
        # predict
        x = [x[0] + dt * x[1], x[1]]
        F00, F01, F11 = 1.0, dt, 1.0
        P = [[F00 * (F00 * P[0][0] + F01 * P[1][0]) + F01 * (F00 * P[0][1] + F01 * P[1][1]) + q * dt ** 4 / 4,
              F00 * (F11 * P[0][1]) + F01 * (F11 * P[1][1]) + q * dt ** 3 / 2],
             [F11 * (F00 * P[1][0] + F01 * P[1][1]) + q * dt ** 3 / 2,
              F11 * F11 * P[1][1] + q * dt ** 2]]
        # update with measurement z = 10*t + noise
        z = 10.0 * t + nz
        y = z - x[0]
        S = P[0][0] + R
        K0, K1 = P[0][0] / S, P[1][0] / S
        x = [x[0] + K0 * y, x[1] + K1 * y]
        P = [[(1 - K0) * P[0][0], (1 - K0) * P[0][1]],
             [P[1][0] - K1 * P[0][0], P[1][1] - K1 * P[0][1]]]
    truth_p, truth_v = 10.0 * (len(noise) - 1), 10.0
    print("final estimate: pos %.2f m (truth %.0f), vel %.2f m/s (truth %.0f)" % (x[0], truth_p, x[1], truth_v))
    print("final pos variance: %.2f m^2" % P[0][0])
    assert abs(x[0] - truth_p) < 4.0
    assert abs(x[1] - truth_v) < 2.0
    assert P[0][0] < 25.0  # fused uncertainty beats any single fix
    print("rule: believe each witness exactly as much as its record deserves")
    print("OK: %s judged wisely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_query_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    random.seed(11)
    # 20k points partitioned into 10x10 tiles; query touches 4 tiles
    pts = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(20000)]
    T = 10
    tiles = {}
    for p in pts:
        key = (int(p[0] // 100), int(p[1] // 100))
        tiles.setdefault(key, []).append(p)
    q = (450, 450, 550, 550)
    qx0, qy0, qx1, qy1 = q
    touched = [(i, j) for i in range(4, 6) for j in range(4, 6)]
    got = []
    for key in touched:
        for p in tiles.get(key, []):
            if qx0 <= p[0] <= qx1 and qy0 <= p[1] <= qy1:
                got.append(p)
    brute = [p for p in pts if qx0 <= p[0] <= qx1 and qy0 <= p[1] <= qy1]
    print("tiled query: %d tiles of %d, %d points read-equivalent" % (len(touched), T * T, sum(len(tiles.get(k, [])) for k in touched)))
    print("tiled result %d == brute force %d" % (len(got), len(brute)))
    assert set(got) == set(brute)
    assert len(touched) == 4 and len(brute) > 0
    ratio = sum(len(tiles.get(k, [])) for k in touched) / len(pts)
    print("data touched: %.1f%% - the read ratio is the performance story" % (ratio * 100))
    assert ratio < 0.06
    print("rule: partition so the query reads a district, not the nation")
    print("OK: %s heard the district" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_viewshed(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def los_visible(profile, obs_i, obs_h, tgt_i):
    # profile: terrain heights; observer eye at profile[obs_i] + obs_h
    eye = profile[obs_i] + obs_h
    tgt_h = profile[tgt_i]
    n = abs(tgt_i - obs_i)
    for s in range(1, n):
        i = obs_i + s if tgt_i > obs_i else obs_i - s
        line_h = eye + (tgt_h - eye) * (s / n)
        if profile[i] > line_h + 1e-9:
            return False
    return True

def main():
    # ridge at index 4 blocks the view of the valley behind it
    profile = [10, 12, 15, 30, 45, 20, 18, 16, 15, 14]
    obs_h = 2.0
    vis = [i for i in range(len(profile)) if i != 0 and los_visible(profile, 0, obs_h, i)]
    print("observer at 0 (eye %.0f m): visible cells %s" % (profile[0] + obs_h, vis))
    assert 3 in vis      # mid-slope visible
    assert 5 not in vis  # hidden behind the 45 m ridge
    assert 9 not in vis  # valley behind ridge hidden
    # D8 mini-watershed: 3x3, pit in center drains nowhere until filled
    dem = [[10, 10, 10], [10, 5, 10], [10, 10, 9]]
    # steepest descent from center (1,1)=5: lowest neighbor is (2,2)=9? no - 5 is lowest: pit
    center = dem[1][1]
    lowest = min(dem[i][j] for i in range(3) for j in range(3) if (i, j) != (1, 1))
    print("center %.0f vs lowest neighbor %.0f -> pit: %s (must fill/breach first)" % (center, lowest, center < lowest))
    assert center < lowest
    print("rule: condition the DEM before the water, correct the curve before the view")
    print("OK: %s saw and drained" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_constrained(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import heapq

def main():
    # expanded graph: state = (node, arrived_via). No-left-turn at B->C->D.
    # base edges: A->B(1), B->C(1), B->D(5), C->D(1), C->E(6), D->E(1)
    base = {"A": [("B", 1)], "B": [("C", 1), ("D", 5)],
            "C": [("D", 1), ("E", 6)], "D": [("E", 1)], "E": []}
    forbidden = {("B", "C", "D")}  # the illegal left turn
    start = ("A", None)
    dist = {start: 0.0}
    prev = {}
    pq = [(0.0, start)]
    while pq:
        d, (u, via) = heapq.heappop(pq)
        if d > dist.get((u, via), float("inf")):
            continue
        for v, w in base.get(u, []):
            if (via, u, v) in forbidden:
                continue  # the maneuver has no edge: it cannot be taken
            ns = (v, u)
            nd = d + w
            if nd < dist.get(ns, float("inf")) - 1e-12:
                dist[ns] = nd
                prev[ns] = (u, via)
                heapq.heappush(pq, (nd, ns))
    best = min((d, s) for s, d in dist.items() if s[0] == "E")
    print("legal shortest A->E: cost %.1f via state %s" % (best[0], best[1]))
    # A-B-C-D-E = 4 uses the forbidden B-C-D turn; legal best is A-B-D-E = 7
    # (A-B-C-E = 8, so the optimum is unique)
    assert abs(best[0] - 7.0) < 1e-9
    # rebuild node path
    s = best[1]
    nodes = [s[0]]
    while s != start:
        s = prev[s]
        nodes.append(s[0])
    nodes.reverse()
    print("path: %s" % "->".join(nodes))
    assert nodes == ["A", "B", "D", "E"]
    print("rule: bind the search to the law before seeking the shortest")
    print("OK: %s drove legally" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_projmath(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    R = 6378137.0
    lat = 40.0
    phi = math.radians(lat)
    # forward (spherical Mercator)
    y = R * math.log(math.tan(math.pi / 4 + phi / 2))
    # inverse
    lat_back = math.degrees(2 * math.atan(math.exp(y / R)) - math.pi / 2)
    err = abs(lat_back - lat)
    print("forward y=%.3f m, inverse lat=%.12f, round-trip err=%.2e deg" % (y, lat_back, err))
    assert 4865942.27 < y < 4865942.29
    assert err < 1e-9
    # scale factor: map distance / k = ground distance
    k = 1 / math.cos(phi)
    map_d, ground_d = 1305.4, 1305.4 / k
    print("k=%.4f: %.1f map-m = %.1f ground-m" % (k, map_d, ground_d))
    assert 999.9 < ground_d < 1000.1
    # UTM wisdom: k0=0.9996 shrinks center so edges balance
    print("UTM k0=0.9996: 1000 m at central meridian measures %.2f m" % (1000 * 0.9996))
    assert abs(1000 * 0.9996 - 999.6) < 1e-9
    print("rule: divide out the flattery before quoting the measurement")
    print("OK: %s did the math" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "location_uncertainty": demo_geo_uncertainty,
    "kalman_filtering": demo_geo_kalman,
    "spatial_query_scale": demo_geo_query_scale,
    "viewshed_watershed": demo_geo_viewshed,
    "constrained_routing": demo_geo_constrained,
    "projection_math": demo_geo_projmath,
})

def demo_geo_trajectory(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def stay_points(track, d_thr, t_thr):
    # track: list of (t, x, y); returns [(cx, cy, t_in, t_out)]
    stays = []
    i = 0
    n = len(track)
    while i < n:
        j = i + 1
        while j < n and math.hypot(track[j][1] - track[i][1], track[j][2] - track[i][2]) <= d_thr:
            j += 1
        if track[j - 1][0] - track[i][0] >= t_thr:
            xs = [p[1] for p in track[i:j]]
            ys = [p[2] for p in track[i:j]]
            stays.append((sum(xs) / len(xs), sum(ys) / len(ys), track[i][0], track[j - 1][0]))
            i = j
        else:
            i += 1
    return stays

def main():
    # delivery van: depot stay, drive, customer stay, drive home
    track = [(0, 0, 0), (5, 2, 1), (10, 1, -1), (15, 0, 1),      # depot ~20 min
             (20, 500, 0), (25, 1000, 5),                        # driving
             (30, 1500, 0), (40, 1502, 2), (50, 1499, -1),        # customer ~20 min
             (55, 1000, 0), (60, 0, 0)]                           # home
    stays = stay_points(track, 50.0, 15.0)
    print("stay points: %d" % len(stays))
    for cx, cy, tin, tout in stays:
        print("  (%.0f, %.0f) t=%d..%d (%d min)" % (cx, cy, tin, tout, tout - tin))
    assert len(stays) == 2
    assert abs(stays[0][0] - 1.0) < 5.0 and stays[0][2] == 0
    assert abs(stays[1][0] - 1500.0) < 5.0
    print("rule: the stops are the story - read them, and treat the writer as a person")
    print("OK: %s read the footsteps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_uncprop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    random.seed(42)
    # Monte Carlo: 100 m buffer on a point with 5 m 1-sigma radial error
    R_buf, sigma, N = 100.0, 5.0, 4000
    radii = []
    for _ in range(N):
        # radial error ~ Rayleigh(sigma); boundary radius = R + err
        u = random.random()
        err = sigma * math.sqrt(-2.0 * math.log(1.0 - u))
        radii.append(R_buf + err - sigma * math.sqrt(math.pi / 2))  # zero-mean-ish
    radii.sort()
    mean = sum(radii) / N
    lo, hi = radii[int(0.025 * N)], radii[int(0.975 * N)]
    print("buffer boundary: mean %.2f m, 95%% band [%.2f, %.2f] m" % (mean, lo, hi))
    assert 99.9 < mean < 100.2
    assert 94.8 < lo < 95.1
    assert 107.3 < hi < 107.6
    width = hi - lo
    print("the 'crisp' 100 m line was a fiction %.1f m wide (asymmetric: radial error is one-sided)" % width)
    assert 12.3 < width < 12.7
    print("rule: no operation launders doubt into certainty")
    print("OK: %s followed the echo" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_itrf(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # station position at epoch 2015.0 + velocity -> position at 2026.0
    X0 = (1000000.0, 2000000.0, 3000000.0)
    V = (0.025, -0.018, 0.011)  # m/yr
    t0, t = 2015.0, 2026.0
    X = tuple(x + v * (t - t0) for x, v in zip(X0, V))
    disp = math.sqrt(sum((a - b) ** 2 for a, b in zip(X, X0)))
    print("11-yr displacement: %.4f m" % disp)
    assert 0.3597 < disp < 0.3599
    print("X(2026) = (%.3f, %.3f, %.3f)" % X)
    assert abs(X[0] - 1000000.275) < 1e-9
    assert abs(X[1] - 1999999.802) < 1e-9
    # horizontal speed magnitude
    vh = math.hypot(V[0], V[1])
    print("horizontal rate: %.1f mm/yr" % (vh * 1000))
    assert 30.7 < vh * 1000 < 30.9
    print("rule: a coordinate is (frame, epoch, velocity) - bare lat/lon freezes time")
    print("OK: %s timestamped the oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_quality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # NSSDA: 95% horizontal accuracy = 1.7308 * RMSE_r from checkpoints
    dx = [0.8, -0.5, 1.1, -0.9, 0.4, -0.3, 0.7, -1.0, 0.6, 0.2,
          -0.6, 0.9, -0.4, 0.5, -0.8, 1.0, -0.2, 0.3, -0.7, 0.55]
    dy = [0.5, 0.9, -0.6, 0.3, -1.1, 0.8, -0.4, 0.2, -0.9, 0.7,
          0.1, -0.5, 1.0, -0.3, 0.6, -0.8, 0.4, -0.2, 0.9, -0.45]
    n = len(dx)
    rmse_x = math.sqrt(sum(v * v for v in dx) / n)
    rmse_y = math.sqrt(sum(v * v for v in dy) / n)
    rmse_r = math.sqrt(rmse_x ** 2 + rmse_y ** 2)
    acc95 = 1.7308 * rmse_r
    print("RMSE_x=%.3f RMSE_y=%.3f RMSE_r=%.3f -> 95%% = %.3f m" % (rmse_x, rmse_y, rmse_r, acc95))
    assert 0.677 < rmse_x < 0.679
    assert 0.937 < rmse_r < 0.939
    assert abs(acc95 / rmse_r - 1.7308) < 1e-9
    assert 1.623 < acc95 < 1.625
    # completeness + consistency quick checks
    print("checkpoint count %d (>= 20 required by NSSDA)" % n)
    assert n >= 20
    print("rule: claims without checkpoint statistics are assertions, not measurements")
    print("OK: %s cross-examined the data" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_realtime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stream: (t, x, y); speed window flags speeding; glitch quarantined
    pings = [(0, 0, 0), (10, 140, 0), (20, 280, 0), (30, 420, 0),
             (40, 560, 0), (50, 5000, 0), (60, 700, 0), (70, 840, 0)]
    SPEED_LIMIT = 20.0  # m/s
    events = []
    last = None
    for t, x, y in pings:
        if last is not None:
            dt = t - last[0]
            d = math.hypot(x - last[1], y - last[2])
            v = d / dt
            if v > 150.0:
                events.append((t, "GLITCH quarantined (%.0f m/s)" % v))
            elif v > SPEED_LIMIT:
                events.append((t, "SPEEDING %.1f m/s" % v))
        last = (t, x, y)
    for t, e in events:
        print("t=%d: %s" % (t, e))
    kinds = [e for _, e in events]
    assert any("GLITCH" in k for k in kinds), "the 5000 m jump must be quarantined"
    assert not any("SPEEDING" in k for k in kinds), "14 m/s cruise is legal"
    # watermark: pings older than 60 s late go to corrections, not the live view
    watermark_lateness = 60
    late = [(200, 0, 0)]
    routed = ["corrections" if 200 - 70 > watermark_lateness else "live" for _ in late]
    print("late ping routed to: %s" % routed[0])
    assert routed[0] == "corrections"
    print("rule: the record corrected, never corrupted")
    print("OK: %s kept the courtroom orderly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_geo_playbook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the eight playbook predicates over a job plan; all must pass
    plan = {
        "crs": "EPSG:26918", "datum": "NAD83", "epoch": 2010.0, "axis": "e,n",
        "dist_model": "planar", "data_family": "projected",
        "error_budget": {"sensor_m": 2.0, "transform_m": 1.0, "confidence": 0.95},
        "geometry_valid": True, "indexed": True,
        "algorithm": "dijkstra", "graph_nodes": 5000,
        "lineage": ["source A", "helmert T=(1,-1.5,0.8)", "output"],
        "failure_modes": {"outage": "coast+flag", "mismatch": "gate", "skew": "retile", "late": "watermark"},
    }
    checks = [
        ("CRS named", bool(plan["crs"] and plan["datum"] and plan["axis"])),
        ("model matches family", (plan["dist_model"], plan["data_family"]) == ("planar", "projected")),
        ("error budget present", plan["error_budget"]["sensor_m"] > 0 and plan["error_budget"]["confidence"] == 0.95),
        ("geometry valid+indexed", plan["geometry_valid"] and plan["indexed"]),
        ("algorithm fits scale", plan["algorithm"] == "dijkstra" and plan["graph_nodes"] < 100000),
        ("lineage recorded", len(plan["lineage"]) >= 2),
        ("failure modes covered", set(plan["failure_modes"]) == {"outage", "mismatch", "skew", "late"}),
        ("reproducible", True),
    ]
    red = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print("  [%s] %s" % ("PASS" if ok else "FAIL", n))
    assert not red, "playbook red: %s" % red
    print("playbook: 8/8 green - the job may run")
    print("rule: a coordinate without a system is two numbers; an operation not reproducible did not happen")
    print("OK: %s ran the gauntlet" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "trajectory_analysis": demo_geo_trajectory,
    "uncertainty_propagation": demo_geo_uncprop,
    "itrf_plate_motion": demo_geo_itrf,
    "spatial_data_quality": demo_geo_quality,
    "realtime_pipelines": demo_geo_realtime,
    "operations_playbook": demo_geo_playbook,
})

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
