"""Demo: metal ashtray and poker volumes and heat storage — The Metal Ashtray with Poker."""
import hashlib, math
def compute():
    d = 100.0; h = 30.0; wall = 2.0; pk_d = 4.0; pk_l = 120.0; rho = 7.9; cp = 0.50; dT = 200.0
    cap_mm3 = math.pi * ((d - 2.0 * wall) / 2.0) ** 2 * h
    cap_cm3 = cap_mm3 / 1000.0
    outer_mm3 = math.pi * (d / 2.0) ** 2 * (h + wall)
    dish_cm3 = (outer_mm3 - cap_mm3) / 1000.0
    dish_g = dish_cm3 * rho
    pk_mm3 = math.pi * (pk_d / 2.0) ** 2 * pk_l
    pk_cm3 = pk_mm3 / 1000.0
    pk_g = pk_cm3 * rho
    total_g = dish_g + pk_g
    heat_J = total_g * cp * dT
    return {"capacity_mm3": round(cap_mm3, 2), "capacity_cm3": round(cap_cm3, 2), "dish_volume_cm3": round(dish_cm3, 2), "dish_mass_g": round(dish_g, 2), "poker_volume_cm3": round(pk_cm3, 2), "poker_mass_g": round(pk_g, 2), "total_mass_g": round(total_g, 2), "heat_to_200C_J": round(heat_J, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ['capacity_mm3', 'capacity_cm3', 'dish_volume_cm3', 'dish_mass_g', 'poker_volume_cm3', 'poker_mass_g', 'total_mass_g', 'heat_to_200C_J']:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
