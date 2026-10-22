#!/usr/bin/env python3
"""Flower finder - Tier-3 chain: nine numbers -> edges -> shapes -> Flower.
Public edition. Demonstrated on synthetic test shapes only.
Usage: python3 find-flower.py
"""
import math

# ---------------------------------------------------------------- pixel infra
W = H = 48
BG, FG = 10, 220

def make_grid(fill=BG): return [[fill] * W for _ in range(H)]

def _put(img, x, y, v=FG):
    if 0 <= x < W and 0 <= y < H: img[y][x] = v

def draw_line(img, x0, y0, x1, y1, v=FG, th=2):
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
    err = dx - dy; x, y = x0, y0
    while True:
        for ox in range(-th // 2, th // 2 + 1):
            for oy in range(-th // 2, th // 2 + 1): _put(img, x + ox, y + oy, v)
        if x == x1 and y == y1: break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x += sx
        if e2 < dx: err += dx; y += sy

def draw_circle(img, cx, cy, r, v=FG):
    for y in range(cy - r - 1, cy + r + 2):
        for x in range(cx - r - 1, cx + r + 2):
            if math.hypot(x - cx, y - cy) <= r + 0.4: _put(img, x, y, v)

def draw_ellipse(img, cx, cy, rx, ry, v=FG):
    for y in range(cy - ry - 1, cy + ry + 2):
        for x in range(cx - rx - 1, cx + rx + 2):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0: _put(img, x, y, v)

def draw_rect(img, x0, y0, x1, y1, v=FG):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1): _put(img, x, y, v)

def draw_tri(img, ax, ay, bx, by, cx, cy, v=FG):
    x0, x1 = min(ax, bx, cx), max(ax, bx, cx)
    y0, y1 = min(ay, by, cy), max(ay, by, cy)
    def s(px, py, qx, qy, rx, ry): return (ry - qy) * (px - qx) - (rx - qx) * (py - qy)
    d = s(ax, ay, bx, by, cx, cy)
    if d == 0: return
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            w1, w2, w3 = s(x, y, ax, ay, bx, by), s(x, y, bx, by, cx, cy), s(x, y, cx, cy, ax, ay)
            if (w1 >= 0 and w2 >= 0 and w3 >= 0) or (w1 <= 0 and w2 <= 0 and w3 <= 0):
                _put(img, x, y, v)

GX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
GY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

def convolve(img, k):
    out = []
    for y in range(H - 2):
        row = []
        for x in range(W - 2):
            s = 0
            for a in range(3):
                for b in range(3): s += k[a][b] * img[y + a][x + b]
            row.append(s)
        out.append(row)
    return out

def edge_map_k(img, kx, ky, T=250):
    gx = convolve(img, kx); gy = convolve(img, ky)
    out = set()
    for y in range(H - 2):
        for x in range(W - 2):
            if abs(gx[y][x]) + abs(gy[y][x]) >= T: out.add((x + 1, y + 1))
    return out

def edge_map(img, T=250):
    return edge_map_k(img, GX, GY, T)

def _bres(x0, y0, x1, y1):
    pts = []; dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
    err = dx - dy; x, y = x0, y0
    while True:
        pts.append((x, y))
        if x == x1 and y == y1: break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x += sx
        if e2 < dx: err += dx; y += sy
    return pts

def _thicken(pts, r=1):
    s = set()
    for x, y in pts:
        for ox in range(-r, r + 1):
            for oy in range(-r, r + 1): s.add((x + ox, y + oy))
    return s

def shape_template(ttype, p, dx=0, dy=0, dr=0):
    if ttype == 'circle':
        cx, cy, r = p; r = r + dr; pts = []
        for a in range(360):
            t = math.radians(a)
            pts.append((round(cx + dx + r * math.cos(t)), round(cy + dy + r * math.sin(t))))
        return _thicken(pts)
    if ttype == 'ellipse':
        cx, cy, rx, ry = p; pts = []
        for a in range(360):
            t = math.radians(a)
            pts.append((round(cx + dx + rx * math.cos(t)), round(cy + dy + ry * math.sin(t))))
        return _thicken(pts)
    if ttype == 'line':
        x0, y0, x1, y1 = p; return _thicken(_bres(x0 + dx, y0 + dy, x1 + dx, y1 + dy))
    if ttype == 'rect':
        x0, y0, x1, y1 = p
        pts = (_bres(x0 + dx, y0 + dy, x1 + dx, y0 + dy) + _bres(x1 + dx, y0 + dy, x1 + dx, y1 + dy)
               + _bres(x1 + dx, y1 + dy, x0 + dx, y1 + dy) + _bres(x0 + dx, y1 + dy, x0 + dx, y0 + dy))
        return _thicken(pts)
    if ttype == 'tri':
        ax, ay, bx, by, cx, cy = p
        pts = (_bres(ax + dx, ay + dy, bx + dx, by + dy) + _bres(bx + dx, by + dy, cx + dx, cy + dy)
               + _bres(cx + dx, cy + dy, ax + dx, ay + dy))
        return _thicken(pts)
    raise ValueError(ttype)

THR = 0.40  # part-presence threshold

def match_part(edg, ttype, p):
    """Tier-2 shape finder: template-match one part near its nominal pose."""
    drs = tuple(d for d in (-2, 0, 2) if ttype != 'circle' or p[2] + d >= 2) or (0,)
    best = (0.0, 0, 0, 0)
    for dr in drs:
        for dy in (-4, -2, 0, 2, 4):
            for dx in (-4, -2, 0, 2, 4):
                t = shape_template(ttype, p, dx, dy, dr)
                if len(t) < 8: continue
                s = len(t & edg) / len(t)
                if s > best[0]: best = (s, dx, dy, dr)
    return best  # (score, dx, dy, dr); dr is a radius delta for circles

def part_center(ttype, p, dx, dy):
    if ttype in ('circle', 'ellipse'): return (p[0] + dx, p[1] + dy)
    if ttype == 'rect': return ((p[0] + p[2]) / 2 + dx, (p[1] + p[3]) / 2 + dy)
    if ttype == 'tri': return ((p[0] + p[2] + p[4]) / 3 + dx, (p[1] + p[3] + p[5]) / 3 + dy)
    if ttype == 'line': return ((p[0] + p[2]) / 2 + dx, (p[1] + p[3]) / 2 + dy)

def ascii_art(img, w=24):
    sx = W / w; sy = H / (w // 2)
    lines = []
    yy = 0
    while yy < H:
        row = ''
        xx = 0
        while xx < W:
            blk = [img[y][x] for y in range(int(yy), min(H, int(yy + sy)))
                   for x in range(int(xx), min(W, int(xx + sx)))]
            row += '#' if sum(blk) / len(blk) > 100 else '.'
            xx += sx
        lines.append(row); yy += sy
    return '\n'.join(lines)

def part_bbox(ttype, p):
    if ttype in ('circle', 'ellipse'): return (p[0]-p[2]-2, p[1]-p[2]-2, p[0]+p[2]+2, p[1]+p[2]+2)
    if ttype == 'rect': return (p[0]-2, p[1]-2, p[2]+2, p[3]+2)
    if ttype == 'tri': return (min(p[0],p[2],p[4])-2, min(p[1],p[3],p[5])-2, max(p[0],p[2],p[4])+2, max(p[1],p[3],p[5])+2)
    if ttype == 'line': return (min(p[0],p[2])-3, min(p[1],p[3])-3, max(p[0],p[2])+3, max(p[1],p[3])+3)

def shift_parts(parts, ox, oy):
    out = []
    for name, tt, p in parts:
        if tt in ('circle', 'ellipse'): q = (p[0]+ox, p[1]+oy) + p[2:]
        elif tt == 'rect': q = (p[0]+ox, p[1]+oy, p[2]+ox, p[3]+oy)
        elif tt == 'tri': q = (p[0]+ox, p[1]+oy, p[2]+ox, p[3]+oy, p[4]+ox, p[5]+oy)
        elif tt == 'line': q = (p[0]+ox, p[1]+oy, p[2]+ox, p[3]+oy)
        out.append((name, tt, q))
    return out

def draw_thing(img, ox=0, oy=0):
    draw_circle(img, 24+ox, 18+oy, 4)
    for px, py in [(35,18),(30,28),(19,28),(13,18),(19,9),(30,9)]:
        draw_circle(img, px+ox, py+oy, 3)
    draw_line(img, 24+ox,22+oy, 24+ox,44+oy)
    draw_line(img, 24+ox,34+oy, 18+ox,30+oy)

def arrange(c):
    import math as _m
    petals = [c['petal-east'],c['petal-se'],c['petal-sw'],c['petal-west'],c['petal-nw'],c['petal-ne']]
    cx, cy = c['center']
    ring = [6 <= _m.hypot(px-cx, py-cy) <= 15 for px, py in petals]
    quads = {(1 if px>cx else -1, 1 if py>cy else -1) for px, py in petals}
    return [('petals ring the center', all(ring)),
            ('petals spread to 4+ quadrants', len(quads) >= 4),
            ('stem drops below the center', c['stem'][1] > cy),
            ('leaf grows off the stem', abs(c['leaf'][0]-c['stem'][0]) < 8)]

PARTS = [('center', 'circle', (24, 18, 4)), ('petal-east', 'circle', (35, 18, 3)), ('petal-se', 'circle', (30, 28, 3)), ('petal-sw', 'circle', (19, 28, 3)), ('petal-west', 'circle', (13, 18, 3)), ('petal-nw', 'circle', (19, 9, 3)), ('petal-ne', 'circle', (30, 9, 3)), ('stem', 'line', (24, 22, 24, 44)), ('leaf', 'line', (24, 34, 18, 30))]
THING_NAME = 'Flower'
KERNEL_X, KERNEL_Y, EDGE_T = GX, GY, 250
THR = 0.40

def main():
    img = make_grid()
    draw_thing(img)
    edg = edge_map_k(img, KERNEL_X, KERNEL_Y, EDGE_T)
    print('Tier 1: nine numbers -> edges: %d edge pixels' % len(edg))
    print('Tier 2: shape finders:')
    centers = {}
    allok = True
    for name, tt, p in PARTS:
        s, dx, dy, dr = match_part(edg, tt, p)
        ok = s >= THR
        allok = allok and ok
        cx, cy = part_center(tt, p, dx, dy)
        centers[name] = (cx, cy)
        print('  %-14s %-8s score=%.3f %s' % (name, tt, s, 'MATCH' if ok else 'miss'))
    print('Tier 3: knowing-when rule (arrangement):')
    rok = True
    for desc, good in arrange(centers):
        rok = rok and good
        print('  [%s] %s' % ('OK' if good else 'FAIL', desc))
    print('RESULT:', 'FOUND ' + THING_NAME if (allok and rok) else 'NOT FOUND')

if __name__ == '__main__':
    main()
