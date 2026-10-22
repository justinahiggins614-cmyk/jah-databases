"""feature_hierarchy.py — Tier-0 working version: feature hierarchy recognition.
Pure Python, no libraries. Run: python3 feature_hierarchy.py
Three hand-built layers: Sobel edges -> corners -> SQUARE unit fires."""

GX = [[-1,0,1],[-2,0,2],[-1,0,1]]
GY = [[-1,-2,-1],[0,0,0],[1,2,1]]

def convolve(img, k):
    kh, kw = len(k), len(k[0])
    return [[sum(k[a][b]*img[i+a][j+b] for a in range(kh) for b in range(kw))
             for j in range(len(img[0])-kw+1)] for i in range(len(img)-kh+1)]

def main():
    img = [[10]*9 for _ in range(9)]
    for c in range(2, 7):
        img[2][c] = 200; img[6][c] = 200
    for r in range(2, 7):
        img[r][2] = 200; img[r][6] = 200
    RX, RY = convolve(img, GX), convolve(img, GY)
    edge = [[1 if (RX[i][j]**2+RY[i][j]**2)**0.5 > 300 else 0 for j in range(7)] for i in range(7)]
    print("layer 1: %d edge units" % sum(sum(r) for r in edge))
    corners = []
    for i in range(7):
        for j in range(7):
            if not edge[i][j]:
                continue
            nb = [(a,b) for a in (-1,0,1) for b in (-1,0,1) if (a,b) != (0,0)
                  and 0 <= i+a < 7 and 0 <= j+b < 7 and edge[i+a][j+b]]
            if len(nb) == 2 and nb[0][0]*nb[1][0] + nb[0][1]*nb[1][1] == 0:
                corners.append((i, j))
    print("layer 2: %d corner units at %s" % (len(corners), corners))
    fire = {(1,1),(1,5),(5,1),(5,5)} <= set(corners)
    print("layer 3: SQUARE unit %s" % ("FIRES" if fire else "silent"))

if __name__ == "__main__":
    main()
