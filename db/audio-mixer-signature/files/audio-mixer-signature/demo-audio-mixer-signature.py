"""Demo program for the Audio Mixer Database (audio-mixer-signature).
Run: python3 demo-audio-mixer-signature.py
"""
a = [0.5, 0.0, -0.5, 0.0]
b = [0.25, 0.25, 0.25, 0.25]
mixed = [round(x + y, 2) for x, y in zip(a, b)]
print(f"Mixing tracks with peaks {max(a)} and {max(b)} gives a mixed peak of {max(abs(x) for x in mixed)}")
