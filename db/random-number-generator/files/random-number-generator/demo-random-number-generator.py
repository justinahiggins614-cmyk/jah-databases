"""Demo program for the Random Number Generator Database (random-number-generator).
Run: python3 demo-random-number-generator.py
"""
import random
seed = 1
rng = random.Random(seed)
print(f"Seed {seed} gives {round(rng.random(), 4)}")
