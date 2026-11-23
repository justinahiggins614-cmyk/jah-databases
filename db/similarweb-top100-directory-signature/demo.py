import hashlib
FIGURES = {'category_index': 1, 'last_rank': 73, 'pair_records': 48, 'rank_sum': 229, 'records_per_edition': 24, 'sections': 16, 'sites': 8, 'sources_per_record': 3, 'top_rank': 1}
LABEL = 'search-engines'
def compute():
    total = sum(FIGURES.values())
    n = len(FIGURES)
    out = {"count": n, "label": LABEL, "max": max(FIGURES.values()), "min": min(FIGURES.values()), "total": total}
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
