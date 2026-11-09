"""The Humidity Control Pack: working program.

Computes the supply's size, capacity and limits from the record's own
numbers, twice with a fixed seed, and prints SHA-256 digests of both runs.
Standard library only; no network. Run: python3 program.py
"""


class SupplyModel:
    """Model of the the humidity control pack."""

    def run(self):
        import hashlib, json, random
        target_rh = 62.0
        accuracy = 2.0
        saturation_g_per_m3 = 17.3
        headspace_ml = 236.5
        size67_mass_g = 67.0
        size67_capacity_g = 450.0
        low_rh = target_rh - accuracy
        high_rh = target_rh + accuracy
        vapour_at_target = saturation_g_per_m3 * target_rh / 100.0
        headspace_m3 = headspace_ml / 1000000.0
        vapour_in_headspace_g = headspace_m3 * vapour_at_target
        vapour_at_40 = saturation_g_per_m3 * 0.40
        vapour_to_add_g = (vapour_at_target - vapour_at_40) * headspace_m3
        flower_per_g_pack67 = size67_capacity_g / size67_mass_g
        flower_per_g_pack8 = 28.35 / 8.0
        def run_once(seed):
            rng = random.Random(seed)
            jitter = rng.uniform(-0.05, 0.05)
            return {"rh_low": round(low_rh, 2), "rh_high": round(high_rh, 2), "vapour_at_target_g_per_m3": round(vapour_at_target + jitter, 2), "vapour_in_headspace_g": round(vapour_in_headspace_g, 5), "vapour_to_add_from_40pct_g": round(vapour_to_add_g, 5), "flower_per_gram_pack67": round(flower_per_g_pack67, 2), "flower_per_gram_pack8": round(flower_per_g_pack8, 2)}
        r1 = run_once(42)
        r2 = run_once(42)
        d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
        d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
        print("RH low bound (percent): %.2f" % r1["rh_low"])
        print("RH high bound (percent): %.2f" % r1["rh_high"])
        print("Vapour at target (g per m3): %.2f" % r1["vapour_at_target_g_per_m3"])
        print("Vapour in headspace (g): %.5f" % r1["vapour_in_headspace_g"])
        print("Vapour to add from 40 percent (g): %.5f" % r1["vapour_to_add_from_40pct_g"])
        print("Flower per gram, size 67 pack: %.2f" % r1["flower_per_gram_pack67"])
        print("Flower per gram, size 8 pack: %.2f" % r1["flower_per_gram_pack8"])
        print("Run 1 SHA-256: %s" % d1)
        print("Run 2 SHA-256: %s" % d2)
        print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))


if __name__ == "__main__":
    SupplyModel().run()
