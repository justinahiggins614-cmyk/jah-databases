import hashlib
FIGURES = {'JAH-GREGS-000001': 160, 'JAH-GREGS-000002': 162, 'JAH-GREGS-000003': 165, 'JAH-GREGS-000004': 163, 'JAH-GREGS-000005': 165, 'JAH-GREGS-000006': 165, 'JAH-GREGS-000007': 166, 'JAH-GREGS-000008': 170, 'JAH-GREGS-000009': 168, 'JAH-GREGS-000010': 173, 'JAH-GREGS-000011': 173, 'JAH-GREGS-000012': 171, 'JAH-GREGS-000013': 175, 'JAH-GREGS-000014': 173, 'JAH-GREGS-000015': 177, 'JAH-GREGS-000016': 176, 'JAH-GREGS-000017': 176, 'JAH-GREGS-000018': 177, 'JAH-GREGS-000019': 181, 'JAH-GREGS-000020': 179, 'JAH-GREGS-000021': 183, 'JAH-GREGS-000022': 181, 'JAH-GREGS-000023': 182, 'JAH-GREGS-000024': 187}
LABEL = 'generator-registry-marketplace-signature-database'
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
