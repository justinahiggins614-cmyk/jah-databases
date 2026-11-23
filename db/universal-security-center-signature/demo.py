import hashlib
FIGURES = {'JAH-UISCS-000001': 160, 'JAH-UISCS-000002': 161, 'JAH-UISCS-000003': 163, 'JAH-UISCS-000004': 165, 'JAH-UISCS-000005': 166, 'JAH-UISCS-000006': 166, 'JAH-UISCS-000007': 166, 'JAH-UISCS-000008': 168, 'JAH-UISCS-000009': 168, 'JAH-UISCS-000010': 172, 'JAH-UISCS-000011': 171, 'JAH-UISCS-000012': 173, 'JAH-UISCS-000013': 176, 'JAH-UISCS-000014': 175, 'JAH-UISCS-000015': 175, 'JAH-UISCS-000016': 175, 'JAH-UISCS-000017': 179, 'JAH-UISCS-000018': 177, 'JAH-UISCS-000019': 181, 'JAH-UISCS-000020': 180, 'JAH-UISCS-000021': 181, 'JAH-UISCS-000022': 181, 'JAH-UISCS-000023': 185, 'JAH-UISCS-000024': 187}
LABEL = 'universal-security-center-signature-database'
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
