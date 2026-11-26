"""Demo program for the Limit Calculator Database (limit-calculator-signature).
Run: python3 demo-limit-calculator-signature.py
"""
def f(x):
    return (x * x - 4) / (x - 2)
print(f"As x nears 2, (x squared - 4) / (x - 2) nears {round(f(1.9), 2)} from below and {round(f(2.1), 2)} from above: the limit is 4")
