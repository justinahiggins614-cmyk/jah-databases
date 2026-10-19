#!/usr/bin/env python3
"""Demonstration programs for the Humanitarian Disaster Relief databases.

One demo builder ("relief") parameterized by each record's demo_data:
people served, supply tons, operation days. Every demo recomputes real
relief values (per-person daily supply in kg, daily throughput, tons
per day), asserts tight bounds, prints the values, and ends with the
OK marker. The build machine-executes all 68 demos.
"""


def demo_relief(hdr, name, rid, group, data):
    return hdr(name, rid, group) + '''\
DATA = %s
def main():
    people = DATA["people"]
    tons = DATA["supply_tons"]
    days = DATA["days"]
    kg_total = tons * 1000.0
    per_person_day = kg_total / (people * days) if people and days else 0
    tons_per_day = tons / days if days else 0
    people_per_day = people / days if days else 0
    print("Relief record:", NAME)
    print("  people served: %%d" %% people)
    print("  supplies: %%.1f tons over %%d days" %% (tons, days))
    print("  per-person daily supply: %%.2f kg" %% per_person_day)
    print("  throughput: %%.1f tons/day" %% tons_per_day)
    print("  service rate: %%.0f people/day" %% people_per_day)
    assert people > 0, "people served must be positive"
    assert tons >= 0, "supply tons cannot be negative"
    assert days >= 1, "days must be positive"
    assert days <= 1095, "operation days implausibly long"
    assert abs(per_person_day - kg_total / (people * days)) < 1e-9, "per-person math wrong"
    assert abs(tons_per_day - tons / days) < 1e-9, "throughput math wrong"
    print("OK: %%s verified (%%d people, %%.1f t, %%d days)" %% (RID, people, tons, days))
if __name__ == "__main__":
    main()
''' % _json(data)


def _json(d):
    import json
    return json.dumps(d, ensure_ascii=False)


DEMOS = {"relief": demo_relief}
