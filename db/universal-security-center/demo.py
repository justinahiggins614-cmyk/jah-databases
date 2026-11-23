import hashlib
FIGURES = {'JAH-UISC-000001': 168, 'JAH-UISC-000002': 166, 'JAH-UISC-000003': 167, 'JAH-UISC-000004': 173, 'JAH-UISC-000005': 172, 'JAH-UISC-000006': 172, 'JAH-UISC-000007': 170, 'JAH-UISC-000008': 174, 'JAH-UISC-000009': 171, 'JAH-UISC-000010': 179, 'JAH-UISC-000011': 176, 'JAH-UISC-000012': 183, 'JAH-UISC-000013': 184, 'JAH-UISC-000014': 181, 'JAH-UISC-000015': 181, 'JAH-UISC-000016': 179, 'JAH-UISC-000017': 186, 'JAH-UISC-000018': 182, 'JAH-UISC-000019': 189, 'JAH-UISC-000020': 187, 'JAH-UISC-000021': 187, 'JAH-UISC-000022': 189, 'JAH-UISC-000023': 196, 'JAH-UISC-000024': 196}
LABEL = 'universal-security-center-database'
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
