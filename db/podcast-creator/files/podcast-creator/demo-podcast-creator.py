"""Demo program for the Podcast Creator Database (podcast-creator).
Run: python3 demo-podcast-creator.py
"""
segments = [("intro", 2), ("talk", 10), ("outro", 2)]
total = sum(m for _, m in segments)
print(f"{len(segments)} segments make a show of {total} minutes")
