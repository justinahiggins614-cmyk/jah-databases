"""hough_voting.py — Tier-0 working version: Hough voting recognition.
Pure Python, no libraries. Run: python3 hough_voting.py
Line election over (theta, rho) with threshold + non-maximum suppression."""
import math

THETAS = [0, 45, 90, 135]

def vote(points, thetas=THETAS):
    acc = {}
    for (x, y) in points:
        for th in thetas:
            r = x*math.cos(math.radians(th)) + y*math.sin(math.radians(th))
            key = (th, round(r))
            acc[key] = acc.get(key, 0) + 1
    return acc

def peaks(acc, tau=3):
    cands = [(k, v) for k, v in acc.items() if v >= tau]
    out = []
    for (th, rho), v in cands:
        neigh = [acc.get((th+d, rho), 0) for d in (-45, 45)] + [acc.get((th, rho+d), 0) for d in (-1, 1)]
        if all(v >= n for n in neigh):
            out.append(((th, rho), v))
    return sorted(out)

def main():
    pts = [(1,1),(2,2),(3,3),(1,4),(2,3),(3,2)]
    found = peaks(vote(pts))
    for (th, rho), v in found:
        print("line: theta=%d rho=%d votes=%d" % (th, rho, v))
    print("shapes found:", len(found))

if __name__ == "__main__":
    main()
