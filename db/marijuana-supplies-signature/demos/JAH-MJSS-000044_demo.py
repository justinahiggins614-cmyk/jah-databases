"""Demo: grow tent — Signature Grow Tent."""
import hashlib, math
def compute():
    l_ft = 5.0; w_ft = 5.0; h_ft = 6.5
    volume_ft3 = l_ft * w_ft * h_ft
    floor_ft2 = l_ft * w_ft
    fabric_ft2 = 2 * (l_ft * h_ft + w_ft * h_ft) + 2 * floor_ft2
    fan_cfm = 600.0
    exchanges = fan_cfm / volume_ft3
    seconds_per_exchange = 60.0 / exchanges
    return {"tent_ft": "5 x 5 x 6.5", "volume_ft3": round(volume_ft3, 1), "floor_ft2": round(floor_ft2, 1), "fabric_ft2": round(fabric_ft2, 1), "fan_cfm": fan_cfm, "exchanges_per_min": round(exchanges, 2), "seconds_per_exchange": round(seconds_per_exchange, 1)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"tent_ft: {a['tent_ft']}")
    print(f"volume_ft3: {a['volume_ft3']}")
    print(f"floor_ft2: {a['floor_ft2']}")
    print(f"fabric_ft2: {a['fabric_ft2']}")
    print(f"fan_cfm: {a['fan_cfm']}")
    print(f"exchanges_per_min: {a['exchanges_per_min']}")
    print(f"seconds_per_exchange: {a['seconds_per_exchange']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
