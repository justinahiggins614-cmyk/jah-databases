"""Demo program for the Tax Calculator Database (tax-calculator-signature).
Run: python3 demo-tax-calculator-signature.py
"""
income, rate = 1000, 20
print(f"An income of {income} at an example rate of {rate} percent gives a tax of {income * rate // 100}")
