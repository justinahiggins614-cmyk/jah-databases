"""Demo program for the Numerical Simulation Database (numerical-simulation).
Run: python3 demo-numerical-simulation.py
"""
y0, h = 1.0, 0.1
y1 = y0 + h * y0
print(f"A simulation steps y from {y0} to {round(y1, 2)} in one step of {h}")
