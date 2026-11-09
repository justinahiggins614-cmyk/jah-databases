"""Demo: dugout one-hitter kit — Signature Dugout One-Hitter Kit."""
import hashlib, math
def compute():
    case_l = 110.0; case_w = 30.0; case_h = 20.0
    stash_d = 18.0; stash_h = 75.0; bat_inner_r = 3.5; bowl_h = 14.0
    case_vol = case_l * case_w * case_h / 1000.0
    stash_vol = math.pi * (stash_d / 2.0) ** 2 * stash_h / 1000.0
    bowl_vol = math.pi * bat_inner_r ** 2 * bowl_h / 1000.0
    stash_mass = stash_vol * 0.35
    hit_mass = bowl_vol * 0.6
    hits = stash_mass / hit_mass
    return {"case_volume_cm3": round(case_vol, 2), "stash_volume_cm3": round(stash_vol, 2), "bowl_volume_cm3": round(bowl_vol, 2), "stash_mass_g": round(stash_mass, 2), "hit_mass_g": round(hit_mass, 2), "hits_per_fill": round(hits, 1)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"case_volume_cm3: {a['case_volume_cm3']}")
    print(f"stash_volume_cm3: {a['stash_volume_cm3']}")
    print(f"bowl_volume_cm3: {a['bowl_volume_cm3']}")
    print(f"stash_mass_g: {a['stash_mass_g']}")
    print(f"hit_mass_g: {a['hit_mass_g']}")
    print(f"hits_per_fill: {a['hits_per_fill']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
