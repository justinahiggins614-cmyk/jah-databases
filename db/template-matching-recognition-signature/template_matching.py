"""template_matching.py — Tier-0 working version: template matching recognition.
Pure Python, no libraries. Run: python3 template_matching.py
NCC search + JAH's two-gate knowing-when rule on a synthetic scene."""
import math

def ncc_at(img, T, i, j):
    n = len(T) * len(T[0])
    tm = sum(sum(r) for r in T) / n
    vals = [img[i+a][j+b] for a in range(len(T)) for b in range(len(T[0]))]
    pm = sum(vals) / n
    num = sum((img[i+a][j+b] - pm) * (T[a][b] - tm) for a in range(len(T)) for b in range(len(T[0])))
    dp = sum((v - pm) ** 2 for v in vals) ** 0.5
    dt = sum((T[a][b] - tm) ** 2 for a in range(len(T)) for b in range(len(T[0]))) ** 0.5
    return num / (dp * dt) if dp and dt else 0.0

def decide(img, T, tau_abs=0.8, tau_margin=0.25):
    spots = [(ncc_at(img, T, i, j), i, j)
             for i in range(len(img)-len(T)+1) for j in range(len(img[0])-len(T[0])+1)]
    spots.sort()
    peak, runner = spots[-1][0], spots[-2][0]
    bi, bj = spots[-1][1], spots[-1][2]
    return {"peak": peak, "runner_up": runner, "at": (bi, bj),
            "found": peak >= tau_abs and (peak - runner) >= tau_margin}

def main():
    T = [[200, 10, 200], [10, 200, 10], [200, 10, 200]]
    img = [[10]*9 for _ in range(9)]
    for r in range(3):
        for c in range(3):
            img[4+r][2+c] = T[r][c]
    d = decide(img, T)
    print("peak=%.3f runner-up=%.3f at=%s -> %s" %
          (d["peak"], d["runner_up"], d["at"], "FOUND" if d["found"] else "NOT FOUND"))

if __name__ == "__main__":
    main()
