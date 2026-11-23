import hashlib
FIGURES = {'cost_usd': 14, 'form_min': 9, 'robots': 100, 'shape_robots': 92, 'success_pct': 96, 'table_m2': 2}
LABEL = 'swarm-robotics-laboratory-000004'
def compute():
    vals = list(FIGURES.values())
    total = sum(vals)
    n = len(vals)
    mean = round(total / n, 4) if n else 0
    out = {"count": n, "label": LABEL, "max": max(vals), "mean": mean, "min": min(vals), "total": total}
    return out
outputs = compute()
result = "|".join(f"{k}={v}" for k, v in sorted(outputs.items()))
h1 = hashlib.sha256(result.encode()).hexdigest()
outputs2 = compute()
result2 = "|".join(f"{k}={v}" for k, v in sorted(outputs2.items()))
h2 = hashlib.sha256(result2.encode()).hexdigest()
for k, v in sorted(outputs.items()):
    print(f"{k}: {v}")
print(f"Result: {result}")
print(f"Run 1 SHA-256: {h1}")
print(f"Run 2 SHA-256: {h2}")
print(f"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}")
