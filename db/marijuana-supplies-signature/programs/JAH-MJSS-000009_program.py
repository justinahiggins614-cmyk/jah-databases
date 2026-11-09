"""The Rolling Tray: working program.

Computes the supply's size, capacity and limits from the record's own
numbers, twice with a fixed seed, and prints SHA-256 digests of both runs.
Standard library only; no network. Run: python3 program.py
"""


class SupplyModel:
    """Model of the the rolling tray."""

    def run(self):
        import hashlib, json, random
        length_cm = 27.0
        width_cm = 16.0
        depth_cm = 2.5
        usable_area_cm2 = 380.0
        paper_area_cm2 = 11.0 * 4.5
        area_cm2 = length_cm * width_cm
        volume_cm3 = area_cm2 * depth_cm
        papers_fit = usable_area_cm2 / paper_area_cm2
        large_area_cm2 = 34.0 * 27.5
        large_ratio = large_area_cm2 / area_cm2
        def run_once(seed):
            rng = random.Random(seed)
            jitter = rng.uniform(-1.0, 1.0)
            return {"tray_area_cm2": round(area_cm2, 2), "usable_area_cm2": round(usable_area_cm2 + jitter, 2), "tray_volume_cm3": round(volume_cm3, 2), "papers_that_fit_flat": round(papers_fit, 2), "large_tray_area_cm2": round(large_area_cm2, 2), "large_to_medium_ratio": round(large_ratio, 2)}
        r1 = run_once(42)
        r2 = run_once(42)
        d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
        d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
        print("Tray area (cm2): %.2f" % r1["tray_area_cm2"])
        print("Usable area (cm2): %.2f" % r1["usable_area_cm2"])
        print("Tray volume to lip (cm3): %.2f" % r1["tray_volume_cm3"])
        print("Papers that fit flat: %.2f" % r1["papers_that_fit_flat"])
        print("Large tray area (cm2): %.2f" % r1["large_tray_area_cm2"])
        print("Large to medium ratio: %.2f" % r1["large_to_medium_ratio"])
        print("Run 1 SHA-256: %s" % d1)
        print("Run 2 SHA-256: %s" % d2)
        print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))


if __name__ == "__main__":
    SupplyModel().run()
