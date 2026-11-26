"""Demo program for the Thermodynamics Calculator Database (thermodynamics-calculator-signature).
Run: python3 demo-thermodynamics-calculator-signature.py
"""
n, r, t, p = 1, 0.0821, 273, 1
print(f"1 mole of gas at {t} kelvin fills {round(n * r * t / p, 2)} litres")
