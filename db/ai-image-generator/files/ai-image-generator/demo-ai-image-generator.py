"""Demo program for the AI Image Generator Database (ai-image-generator).
Run: python3 demo-ai-image-generator.py
"""
import random
rng = random.Random(7)
grid = [rng.randrange(256) for _ in range(64)]
print(f"A grid of {len(grid)} pixels averages {round(sum(grid) / len(grid), 1)}")
