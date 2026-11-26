"""Demo program for the Video Summarizer Database (video-summarizer-signature).
Run: python3 demo-video-summarizer-signature.py
"""
frames = [120, 90, 200, 80, 210, 95]
best = sorted(frames, reverse=True)[:2]
print(f"The summary keeps {len(best)} frames: {best[0]} and {best[1]}")
