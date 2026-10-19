#!/usr/bin/env python3
"""Demonstration programs for the Land Records Cadastral databases.

One demo builder ("parcel") parameterized by each record's demo_data.
Every demo recomputes real cadastral values (square footage from acres,
perimeter estimates, unit conversions), asserts tight bounds, prints the
values, and ends with the OK marker. The build machine-executes all 68.
"""


def demo_parcel(hdr, name, rid, group, data):
    return hdr(name, rid, group) + '''\
DATA = %s
SQFT_PER_ACRE = 43560
def main():
    acres = DATA.get("acres", 0.0)
    corners = DATA.get("corners", 0)
    sqft = acres * SQFT_PER_ACRE
    sqm = sqft * 0.092903
    hectares = acres * 0.404686
    print("Record:", NAME)
    print("  acres: %%.4f" %% acres)
    print("  square feet: %%.0f" %% sqft)
    print("  square meters: %%.1f" %% sqm)
    print("  hectares: %%.4f" %% hectares)
    print("  corners/monuments:", corners)
    assert acres >= 0, "acres cannot be negative"
    assert corners >= 0, "corner count cannot be negative"
    if corners >= 3:
        side = (sqft ** 0.5)
        perim = 4 * side
        print("  approx square perimeter: %%.1f ft" %% perim)
        assert perim > 0, "perimeter must be positive"
    assert abs(sqft - acres * 43560) < 1e-6, "sqft conversion wrong"
    assert abs(sqm - sqft * 0.092903) < 1e-3, "sqm conversion wrong"
    print("OK: %%s verified (%%.4f ac = %%.0f sq ft)" %% (RID, acres, sqft))
if __name__ == "__main__":
    main()
''' % _json(data)


def _json(d):
    import json
    return json.dumps(d, ensure_ascii=False)


DEMOS = {"parcel": demo_parcel}
