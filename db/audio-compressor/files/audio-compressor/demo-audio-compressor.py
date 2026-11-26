"""Demo program for the Audio Compressor Database (audio-compressor).
Run: python3 demo-audio-compressor.py
"""
x, thr, ratio = 0.9, 0.5, 4
out = thr + (x - thr) / ratio
print(f"A sample of {x} past a threshold of {thr} at ratio {ratio} becomes {round(out, 2)}")
