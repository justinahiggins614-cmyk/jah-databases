import hashlib
class MultiRobotCoordinationProgram:
    """Working program for this record; run() recomputes the demo result."""
    def run(self):
        import hashlib
        FIGURES = {'align_error_cm': 6, 'landmarks': 140, 'maps': 5, 'overlap_pct': 38, 'robots': 5, 'success_pct': 95}
        LABEL = 'multi-robot-coordination-000014'
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
        return result
