"""Demo program for the Planetary Simulator Database (planetary-simulator-signature).
Run: python3 demo-planetary-simulator-signature.py
"""
import math
g, big_m, r = 6.674e-11, 1.989e30, 1.496e11
v = math.sqrt(g * big_m / r) / 1000
print(f"Earth orbits the Sun at {round(v, 1)} kilometres per second")
