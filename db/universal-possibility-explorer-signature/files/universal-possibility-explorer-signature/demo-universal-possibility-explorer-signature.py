"""Demo program for the Universal Possibility Explorer Database (universal-possibility-explorer-signature).
Run: python3 demo-universal-possibility-explorer-signature.py
A picnic branching demo: weather chances times plan chances give 6 complete
paths. This is a simulation and design-study tool (FRONTIER): it maps stated
possibilities with stated chances, and never claims to explore all
possibilities or to predict the future.
"""
weather = {"Sunny": 0.5, "Cloudy": 0.3, "Rainy": 0.2}
plan = {"Park": 0.7, "Home": 0.3}
joy = {("Sunny", "Park"): 10, ("Sunny", "Home"): 6, ("Cloudy", "Park"): 8,
       ("Cloudy", "Home"): 6, ("Rainy", "Park"): 1, ("Rainy", "Home"): 7}
paths = []
for w, pw in weather.items():
    for p, pp in plan.items():
        paths.append((w, p, pw * pp, joy[(w, p)]))
paths.sort(key=lambda x: -x[2])
for w, p, chance, value in paths:
    print(f"{w} + {p}: chance {chance:.3f}, enjoyment {value}")
expected = sum(c * v for _, _, c, v in paths)
print(f"Expected enjoyment: {expected:.2f} out of 10")
print(f"Most likely path: {paths[0][0]} + {paths[0][1]} (chance {paths[0][2]:.3f})")
