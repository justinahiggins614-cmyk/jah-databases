import hashlib
FIGURES = {'JAH-UBF-000001': 168, 'JAH-UBF-000002': 173, 'JAH-UBF-000003': 169, 'JAH-UBF-000004': 172, 'JAH-UBF-000005': 170, 'JAH-UBF-000006': 173, 'JAH-UBF-000007': 173, 'JAH-UBF-000008': 170, 'JAH-UBF-000009': 176, 'JAH-UBF-000010': 180, 'JAH-UBF-000011': 176, 'JAH-UBF-000012': 180, 'JAH-UBF-000013': 178, 'JAH-UBF-000014': 176, 'JAH-UBF-000015': 183, 'JAH-UBF-000016': 181, 'JAH-UBF-000017': 185, 'JAH-UBF-000018': 183, 'JAH-UBF-000019': 189, 'JAH-UBF-000020': 187, 'JAH-UBF-000021': 185, 'JAH-UBF-000022': 189, 'JAH-UBF-000023': 193, 'JAH-UBF-000024': 199}
LABEL = 'universal-build-factory-database'
def compute():
    total = sum(FIGURES.values())
    n = len(FIGURES)
    mean = round(total / n, 4) if n else 0
    out = {"count": n, "label": LABEL, "max": max(FIGURES.values()), "mean": mean, "min": min(FIGURES.values()), "total": round(total, 4)}
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
