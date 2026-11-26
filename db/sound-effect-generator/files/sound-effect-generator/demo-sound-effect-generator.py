"""Demo program for the Sound Effect Generator Database (sound-effect-generator).
Run: python3 demo-sound-effect-generator.py
"""
import random
rng = random.Random(7)
samples = [rng.randrange(100) for _ in range(6)]
print(f"A burst of {len(samples)} samples starts at {samples[0]}")
