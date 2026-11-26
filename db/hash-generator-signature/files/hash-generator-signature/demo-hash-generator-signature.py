"""Demo program for the Hash Generator Database (hash-generator-signature).
Run: python3 demo-hash-generator-signature.py
"""
import hashlib
digest = hashlib.sha256("hello".encode()).hexdigest()
print(f"SHA-256 of hello is {digest}")
