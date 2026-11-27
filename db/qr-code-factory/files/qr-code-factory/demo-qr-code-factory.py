"""Demo program for the The QR Code Factory Database (qr-code-factory).
Run: python3 demo-qr-code-factory.py
Draws a QR-style matrix for a short text: finder patterns in three corners,
timing patterns along row 6 and column 6, one alignment pattern, and a data
area filled from a seeded pattern of the text. This is a QR-style display
model, not a verified scannable code.
"""
TEXT = "HELLO QR"
LEVEL = "M"
CAPACITY = {1: {"L": 17, "M": 14, "Q": 11, "H": 7},
            2: {"L": 32, "M": 26, "Q": 20, "H": 14},
            3: {"L": 53, "M": 44, "Q": 32, "H": 24},
            4: {"L": 78, "M": 64, "Q": 48, "H": 34}}

def fnv1a(s):
    h = 0x811C9DC5
    for ch in s:
        h ^= ord(ch)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h

def seeded_bits(seed, count):
    state = seed
    out = []
    for _ in range(count):
        state = (state * 1103515245 + 12345) & 0x7FFFFFFF
        out.append((state >> 16) & 1)
    return out

def build_matrix(text, level):
    version = 1 if len(text) <= 14 else 2 if len(text) <= 26 else 3 if len(text) <= 42 else 4
    n = 17 + 4 * version
    grid = [[0] * n for _ in range(n)]
    reserved = [[False] * n for _ in range(n)]

    def put(x, y, v):
        if 0 <= x < n and 0 <= y < n:
            grid[y][x] = v
            reserved[y][x] = True

    def finder(cx, cy):
        for dy in range(-1, 8):
            for dx in range(-1, 8):
                x, y = cx + dx, cy + dy
                v = 0
                if 0 <= dx < 7 and 0 <= dy < 7:
                    edge = dx in (0, 6) or dy in (0, 6)
                    center = 2 <= dx <= 4 and 2 <= dy <= 4
                    v = 1 if (edge or center) else 0
                put(x, y, v)

    finder(0, 0)
    finder(n - 7, 0)
    finder(0, n - 7)
    for i in range(8, n - 8):
        put(i, 6, 1 if i % 2 == 0 else 0)
        put(6, i, 1 if i % 2 == 0 else 0)
    if version >= 2:
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                edge = abs(dx) == 2 or abs(dy) == 2
                put(18 + dx, 18 + dy, 1 if (edge or (dx == 0 and dy == 0)) else 0)
    bits = seeded_bits(fnv1a(text + "|" + level), n * n)
    k = 0
    for y in range(n):
        for x in range(n):
            if not reserved[y][x]:
                grid[y][x] = bits[k]
            k += 1
    return version, n, grid

def main():
    version, n, grid = build_matrix(TEXT, LEVEL)
    quiet = 4
    print("QR-style matrix for %r: version %d, %d by %d modules" % (TEXT, version, n, n))
    print("Error correction level %s: byte capacity %d at this version" % (LEVEL, CAPACITY[version][LEVEL]))
    for y in range(-quiet, n + quiet):
        row = ""
        for x in range(-quiet, n + quiet):
            dark = grid[y][x] == 1 if 0 <= x < n and 0 <= y < n else False
            row += "##" if dark else "  "
        print(row)
    print("QR-style display model only: not a verified scannable code.")

if __name__ == "__main__":
    main()
