"""chamfer_matching.py — Tier-0 working version: chamfer matching recognition.
Pure Python, no libraries. Run: python3 chamfer_matching.py
3-4 distance transform + chamfer gate on a synthetic corner scene."""

def chamfer_dt(edge):
    INF = 10**9
    h, w = len(edge), len(edge[0])
    d = [[0 if edge[i][j] else INF for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if i > 0: d[i][j] = min(d[i][j], d[i-1][j]+3)
            if j > 0: d[i][j] = min(d[i][j], d[i][j-1]+3)
            if i > 0 and j > 0: d[i][j] = min(d[i][j], d[i-1][j-1]+4)
            if i > 0 and j < w-1: d[i][j] = min(d[i][j], d[i-1][j+1]+4)
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if i < h-1: d[i][j] = min(d[i][j], d[i+1][j]+3)
            if j < w-1: d[i][j] = min(d[i][j], d[i][j+1]+3)
            if i < h-1 and j < w-1: d[i][j] = min(d[i][j], d[i+1][j+1]+4)
            if i < h-1 and j > 0: d[i][j] = min(d[i][j], d[i+1][j-1]+4)
    return d

def score(dt, T, i, j):
    return sum(dt[i+a][j+b] for (a, b) in T) / len(T)

def main():
    scene = [[0]*10 for _ in range(10)]
    for c in range(3, 7):
        scene[3][c] = 1; scene[6][c] = 1
    for r in range(3, 7):
        scene[r][3] = 1; scene[r][6] = 1
    dt = chamfer_dt(scene)
    corner = [(0,0),(1,0),(2,0),(0,1),(0,2)]
    s = score(dt, corner, 3, 3)
    print("chamfer score at true corner: %.1f (bar 1.5) -> %s" % (s, "FOUND" if s <= 1.5 else "REJECT"))

if __name__ == "__main__":
    main()
