import hashlib
FIGURES = {'JAH-UBFS-000001': 160, 'JAH-UBFS-000002': 165, 'JAH-UBFS-000003': 163, 'JAH-UBFS-000004': 166, 'JAH-UBFS-000005': 164, 'JAH-UBFS-000006': 165, 'JAH-UBFS-000007': 167, 'JAH-UBFS-000008': 167, 'JAH-UBFS-000009': 168, 'JAH-UBFS-000010': 172, 'JAH-UBFS-000011': 170, 'JAH-UBFS-000012': 172, 'JAH-UBFS-000013': 172, 'JAH-UBFS-000014': 173, 'JAH-UBFS-000015': 175, 'JAH-UBFS-000016': 175, 'JAH-UBFS-000017': 179, 'JAH-UBFS-000018': 177, 'JAH-UBFS-000019': 181, 'JAH-UBFS-000020': 179, 'JAH-UBFS-000021': 180, 'JAH-UBFS-000022': 181, 'JAH-UBFS-000023': 185, 'JAH-UBFS-000024': 187}
LABEL = 'universal-build-factory-signature-database'
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
