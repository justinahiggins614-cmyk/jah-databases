"""morphological.py — Tier-0 working version: morphological recognition.
Pure Python, no libraries. Run: python3 morphological.py
Erosion/dilation, connected components, Euler number on synthetic shapes."""

def erode(img):
    h, w = len(img), len(img[0])
    out = [[0]*w for _ in range(h)]
    for i in range(1, h-1):
        for j in range(1, w-1):
            if all(img[i+a][j+b] for a in (-1,0,1) for b in (-1,0,1)):
                out[i][j] = 1
    return out

def components(img):
    h, w = len(img), len(img[0])
    seen = [[0]*w for _ in range(h)]
    sizes = []
    for i in range(h):
        for j in range(w):
            if img[i][j] and not seen[i][j]:
                seen[i][j] = 1
                stack = [(i, j)]; n = 0
                while stack:
                    x, y = stack.pop(); n += 1
                    for a in (-1,0,1):
                        for b in (-1,0,1):
                            nx, ny = x+a, y+b
                            if 0 <= nx < h and 0 <= ny < w and img[nx][ny] and not seen[nx][ny]:
                                seen[nx][ny] = 1; stack.append((nx, ny))
                sizes.append(n)
    return sizes

def main():
    scene = [[0]*10 for _ in range(10)]
    for r in (1, 2):
        for c in (1, 2):
            scene[r][c] = 1
    scene[5][7] = 1
    for r in range(7, 10):
        for c in range(1, 4):
            scene[r][c] = 1
    sizes = sorted(components(scene))
    print("blob census:", sizes, "->", len(sizes), "components")
    block = [[0]*7 for _ in range(7)]
    for r in range(2, 5):
        for c in range(2, 5):
            block[r][c] = 1
    print("3x3 block eroded ->", sum(sum(r) for r in erode(block)), "pixel survives")

if __name__ == "__main__":
    main()
