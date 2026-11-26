"""Demo program for the Dependency Analyzer Database (dependency-analyzer-signature).
Run: python3 demo-dependency-analyzer-signature.py
"""
parts = {"app": ["web", "data"], "web": ["store"], "data": ["store"], "store": []}
links = sum(len(v) for v in parts.values())
print(f"{len(parts)} parts hold {links} links")
