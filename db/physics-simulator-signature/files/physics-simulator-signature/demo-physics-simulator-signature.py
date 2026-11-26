"""Demo program for the Physics Simulator Database (physics-simulator-signature).
Run: python3 demo-physics-simulator-signature.py
"""
import math
h, g = 10, 9.8
v = math.sqrt(2 * g * h)
print(f"A ball dropped from {h} metres hits the ground at {round(v, 1)} metres per second")
