"""Demo program for the Ocean Simulator Database (ocean-simulator).
Run: python3 demo-ocean-simulator.py
"""
import math
depth = 10
speed = round(math.sqrt(9.8 * depth), 1)
print(f"A wave in {depth} metres of water travels {speed} metres per second")
