"""Demo program for the Hypothesis Testing Tool Database (hypothesis-testing-tool).
Run: python3 demo-hypothesis-testing-tool.py
"""
import math
def norm_p(z):
    return 1 - math.erf(abs(z) / math.sqrt(2))
heads, flips = 60, 100
z = (heads - flips / 2) / 5
print(f"60 heads in 100 flips gives z = {round(z, 2)} and p = {norm_p(z):.2f}")
