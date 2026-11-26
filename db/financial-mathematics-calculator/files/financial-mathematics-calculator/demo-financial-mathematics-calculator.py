"""Demo program for the Financial Mathematics Calculator Database (financial-mathematics-calculator).
Run: python3 demo-financial-mathematics-calculator.py
"""
p, r, t = 1000, 0.05, 2
print(f"1000 at 5 percent for 2 years grows to {round(p * (1 + r) ** t, 2)}")
