"""Demo program for the Voice Changer Database (voice-changer).
Run: python3 demo-voice-changer.py
"""
samples = [10, 20, 30]
factor = 2
shifted = [s * factor for s in samples]
print(f"Shifting {len(samples)} samples by {factor} gives {shifted[0]}, {shifted[1]} and {shifted[2]}")
