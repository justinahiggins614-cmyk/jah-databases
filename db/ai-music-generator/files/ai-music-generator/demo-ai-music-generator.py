"""Demo program for the AI Music Generator Database (ai-music-generator).
Run: python3 demo-ai-music-generator.py
"""
import random
scale = [60, 62, 64, 65, 67, 69, 71, 72]
rng = random.Random(7)
notes = [rng.choice(scale) for _ in range(8)]
print(f"A song of {len(notes)} notes starts on {notes[0]}")
