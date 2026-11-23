import hashlib
FIGURES = {'JAH-MAICS-000001': 160, 'JAH-MAICS-000002': 162, 'JAH-MAICS-000003': 166, 'JAH-MAICS-000004': 163, 'JAH-MAICS-000005': 167, 'JAH-MAICS-000006': 165, 'JAH-MAICS-000007': 166, 'JAH-MAICS-000008': 170, 'JAH-MAICS-000009': 168, 'JAH-MAICS-000010': 169, 'JAH-MAICS-000011': 172, 'JAH-MAICS-000012': 172, 'JAH-MAICS-000013': 175, 'JAH-MAICS-000014': 175, 'JAH-MAICS-000015': 174, 'JAH-MAICS-000016': 175, 'JAH-MAICS-000017': 179, 'JAH-MAICS-000018': 177, 'JAH-MAICS-000019': 181, 'JAH-MAICS-000020': 183, 'JAH-MAICS-000021': 180, 'JAH-MAICS-000022': 181, 'JAH-MAICS-000023': 185, 'JAH-MAICS-000024': 187}
LABEL = 'master-ai-coordinator-signature-database'
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
