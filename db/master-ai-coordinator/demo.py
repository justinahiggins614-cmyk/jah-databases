import hashlib
FIGURES = {'JAH-MAIC-000001': 168, 'JAH-MAIC-000002': 168, 'JAH-MAIC-000003': 174, 'JAH-MAIC-000004': 169, 'JAH-MAIC-000005': 173, 'JAH-MAIC-000006': 170, 'JAH-MAIC-000007': 170, 'JAH-MAIC-000008': 176, 'JAH-MAIC-000009': 174, 'JAH-MAIC-000010': 172, 'JAH-MAIC-000011': 178, 'JAH-MAIC-000012': 178, 'JAH-MAIC-000013': 183, 'JAH-MAIC-000014': 181, 'JAH-MAIC-000015': 179, 'JAH-MAIC-000016': 179, 'JAH-MAIC-000017': 185, 'JAH-MAIC-000018': 183, 'JAH-MAIC-000019': 189, 'JAH-MAIC-000020': 189, 'JAH-MAIC-000021': 186, 'JAH-MAIC-000022': 184, 'JAH-MAIC-000023': 191, 'JAH-MAIC-000024': 199}
LABEL = 'master-ai-coordinator-database'
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
