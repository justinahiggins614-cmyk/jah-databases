"""Demo program for the AI Video Generator Database (ai-video-generator).
Run: python3 demo-ai-video-generator.py
"""
import random
rng = random.Random(7)
frames = [[rng.randrange(256) for _ in range(16)] for _ in range(6)]
print(f"A video of {len(frames)} frames with {len(frames[0])} pixels each")
