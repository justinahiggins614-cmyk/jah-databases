"""contour_approximation.py — Tier-0 working version: contour approximation recognition.
Pure Python, no libraries. Run: python3 contour_approximation.py
Douglas-Peucker + vertex-count classification on synthetic contours."""

def perp_dist(p, a, b):
    (x0, y0), (x1, y1), (x2, y2) = p, a, b
    num = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
    den = ((y2-y1)**2 + (x2-x1)**2) ** 0.5
    return num/den if den else 0.0

def dp_open(pts, eps):
    if len(pts) < 3:
        return pts[:]
    a, b = pts[0], pts[-1]
    dmax, idx = 0, 0
    for i in range(1, len(pts)-1):
        d = perp_dist(pts[i], a, b)
        if d > dmax:
            dmax, idx = d, i
    if dmax > eps:
        return dp_open(pts[:idx+1], eps)[:-1] + dp_open(pts[idx:], eps)
    return [a, b]

def dp_closed(pts, eps):
    n = len(pts)
    dmax, idx = 0, 0
    for i in range(1, n):
        d = ((pts[i][0]-pts[0][0])**2 + (pts[i][1]-pts[0][1])**2) ** 0.5
        if d > dmax:
            dmax, idx = d, i
    return dp_open(pts[:idx+1], eps)[:-1] + dp_open(pts[idx:]+[pts[0]], eps)[:-1]

def classify(contour, eps=0.5):
    n = len(dp_closed(contour, eps))
    return {3: "triangle", 4: "quadrilateral", 5: "pentagon"}.get(n, "circle-candidate" if n >= 8 else "unknown")

def main():
    sq = [(0,0),(3,0.3),(6,0),(6.3,3),(6,6),(3,5.7),(0,6),(-0.3,3)]
    tri = [(0,0),(3,0.2),(6,0),(4.5,2.6),(3,5),(1.5,2.6)]
    print("square ->", classify(sq))
    print("triangle ->", classify(tri))

if __name__ == "__main__":
    main()
