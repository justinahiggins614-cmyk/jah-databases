"""Demo program for the Mathematical Proof Assistant Database (mathematical-proof-assistant).
Run: python3 demo-mathematical-proof-assistant.py
"""
P, Q = True, True
result = (P and ((not P) or Q)) == Q
print(f"Modus ponens: from P and P implies Q, Q follows: {result}")
