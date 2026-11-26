"""Demo program for the Digital Signature Tool Database (digital-signature-tool-signature).
Run: python3 demo-digital-signature-tool-signature.py
"""
import hashlib
h = int(hashlib.sha256(b"hello").hexdigest(), 16) % 3233
sig = pow(h, 2753, 3233)
print(f"Signing hello gives signature {sig}")
