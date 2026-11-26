"""Demo program for the File Compressor Database (file-compressor-signature).
Run: python3 demo-file-compressor-signature.py
"""
import zlib
data = ("the quick brown fox jumps over the lazy dog. " * 10).encode()
comp = zlib.compress(data)
print(f"{len(data)} bytes compress to {len(comp)} bytes")
