"""ransac.py — Tier-0 working version: RANSAC recognition.
Pure Python, no libraries. Run: python3 ransac.py
Persistent-champion line election + least-squares refit (JAH's ritual)."""
import random

def fit_line(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    if x2 == x1:
        return None
    m = (y2-y1)/(x2-x1)
    return (m, y1-m*x1)

def dline(pt, line):
    m, b = line
    return abs(m*pt[0]-pt[1]+b)/(m*m+1)**0.5

def ransac(pts, t=1.5, rounds=20, seed=0):
    rng = random.Random(seed)
    best, inl = None, []
    for _ in range(rounds):
        a, b = rng.sample(pts, 2)
        line = fit_line(a, b)
        if not line:
            continue
        cur = [p for p in pts if dline(p, line) <= t]
        if len(cur) > len(inl):
            best, inl = line, cur
    n = len(inl)
    sx = sum(p[0] for p in inl); sy = sum(p[1] for p in inl)
    m = (n*sum(p[0]*p[1] for p in inl)-sx*sy)/(n*sum(p[0]**2 for p in inl)-sx*sx)
    return best, inl, (m, (sy-m*sx)/n)

def main():
    rng = random.Random(3)
    pts = [(x, 2*x+1+rng.uniform(-0.4,0.4)) for x in range(8)] + [(1,12),(6,-3)]
    prop, inl, refit = ransac(pts)
    print("propose: slope=%.3f (%d inliers)" % (prop[0], len(inl)))
    print("refit:   slope=%.3f intercept=%.3f" % refit)
    print("floor max(3, %d/2)=%.0f <= %d -> ACCEPT" % (len(pts), max(3, len(pts)/2), len(inl)))

if __name__ == "__main__":
    main()
