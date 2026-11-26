"""Demo program for the Factorization Tool Database (factorization-tool-signature).
Run: python3 demo-factorization-tool-signature.py
"""
def factors(n):
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out
f = factors(12)
print(f"12 = {f[0]} times {f[1]} times {f[2]}")
