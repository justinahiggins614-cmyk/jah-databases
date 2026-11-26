"""Demo program for the Reaction Predictor Database (reaction-predictor-signature).
Run: python3 demo-reaction-predictor-signature.py
"""
ch4 = {"C": 1, "H": 4}
o2 = {"O": 2}
left_c = ch4["C"]
left_h = ch4["H"]
left_o = 2 * o2["O"]
right_c = 1
right_h = 2 * 2
right_o = 2 + 2 * 1
print(f"CH4 + 2O2 -> CO2 + 2H2O: C {left_c}, H {left_h}, O {left_o} on both sides")
