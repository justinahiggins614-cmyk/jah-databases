"""Demo program for the File Compressor Database (file-compressor).
Run: python3 demo-file-compressor.py
"""
import zlib
data = ("the quick brown fox jumps over the lazy dog. " * 10).encode()
comp = zlib.compress(data)
print(f"{len(data)} bytes compress to {len(comp)} bytes")
