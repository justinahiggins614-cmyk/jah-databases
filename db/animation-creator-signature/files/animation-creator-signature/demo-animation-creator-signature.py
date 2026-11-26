"""Demo program for the Animation Creator Database (animation-creator-signature).
Run: python3 demo-animation-creator-signature.py
"""
import random
rng = random.Random(7)
xs = [rng.randrange(100) for _ in range(6)]
print(f"A clip of {len(xs)} frames starts the ball at {xs[0]}")
