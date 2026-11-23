import hashlib
FIGURES = {'JAH-GREG-000001': 168, 'JAH-GREG-000002': 168, 'JAH-GREG-000003': 173, 'JAH-GREG-000004': 171, 'JAH-GREG-000005': 171, 'JAH-GREG-000006': 172, 'JAH-GREG-000007': 172, 'JAH-GREG-000008': 176, 'JAH-GREG-000009': 174, 'JAH-GREG-000010': 181, 'JAH-GREG-000011': 179, 'JAH-GREG-000012': 177, 'JAH-GREG-000013': 181, 'JAH-GREG-000014': 179, 'JAH-GREG-000015': 184, 'JAH-GREG-000016': 184, 'JAH-GREG-000017': 181, 'JAH-GREG-000018': 185, 'JAH-GREG-000019': 189, 'JAH-GREG-000020': 185, 'JAH-GREG-000021': 194, 'JAH-GREG-000022': 189, 'JAH-GREG-000023': 187, 'JAH-GREG-000024': 195}
LABEL = 'generator-registry-marketplace-database'
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
