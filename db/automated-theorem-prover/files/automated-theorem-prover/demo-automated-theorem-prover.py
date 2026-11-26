"""Demo program for the Automated Theorem Prover Database (automated-theorem-prover).
Run: python3 demo-automated-theorem-prover.py
"""
result = all(P or (not P) for P in (True, False))
print(f"The prover proves P or not P: {result}")
