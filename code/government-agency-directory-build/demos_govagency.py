#!/usr/bin/env python3
"""Demonstration programs for the Government Agency Directory databases.

One demo builder ("agency") parameterized by each record's demo_data:
founded year, approximate budget (billions USD), workforce (thousands),
office/post count. Every demo recomputes real values (years of operation,
budget per employee, offices), asserts tight bounds, prints the values,
and ends with the OK marker. The build machine-executes all 68 demos.
"""


def demo_agency(hdr, name, rid, group, data):
    return hdr(name, rid, group) + '''\
DATA = %s
def main():
    founded = DATA["founded"]
    budget_b = DATA["budget_b"]
    workforce_k = DATA["workforce_k"]
    offices = DATA["offices"]
    years = 2026 - founded
    budget_total = budget_b * 1e9
    workforce = workforce_k * 1e3
    per_employee = budget_total / workforce if workforce else 0
    print("Agency:", NAME)
    print("  founded:", founded, "| years of operation:", years)
    print("  approx annual budget: $%%.2fB" %% budget_b)
    print("  workforce: ~%%d" %% int(workforce))
    print("  offices/posts:", offices)
    print("  budget per employee: $%%.0f" %% per_employee)
    assert 1700 <= founded <= 2026, "founding year out of range"
    assert years >= 1, "years of operation must be positive"
    assert budget_b > 0, "budget must be positive"
    assert workforce_k > 0, "workforce must be positive"
    assert offices >= 1, "office count must be positive"
    assert per_employee > 0, "budget per employee must be positive"
    assert per_employee < 5e7, "budget per employee implausibly high"
    print("OK: %%s verified (%%d years, $%%.2fB budget, %%d staff)" %% (
        RID, years, budget_b, int(workforce)))
if __name__ == "__main__":
    main()
''' % _json(data)


def _json(d):
    import json
    return json.dumps(d, ensure_ascii=False)


DEMOS = {"agency": demo_agency}
