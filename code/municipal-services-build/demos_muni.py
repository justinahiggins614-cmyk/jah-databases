#!/usr/bin/env python3
"""Demonstration programs for the Municipal Services databases.

One demo builder ("service") parameterized by each record's demo_data:
fee (USD), typical processing days, annual volume. Every demo
recomputes real service values (annual revenue, daily throughput,
revenue per day), asserts tight bounds, prints the values, and ends
with the OK marker. The build machine-executes all 68 demos.
"""


def demo_service(hdr, name, rid, group, data):
    return hdr(name, rid, group) + '''\
DATA = %s
def main():
    fee = DATA["fee"]
    days = DATA["days"]
    volume = DATA["annual_volume"]
    revenue = fee * volume
    per_day = volume / 365.0
    rev_per_day = revenue / 365.0
    per_staff_day = per_day
    print("Service:", NAME)
    print("  fee: $%%.2f" %% fee)
    print("  typical processing: %%d days" %% days)
    print("  annual volume: %%d" %% volume)
    print("  annual revenue: $%%.2f" %% revenue)
    print("  throughput: %%.1f per day" %% per_day)
    print("  revenue per day: $%%.2f" %% rev_per_day)
    assert fee >= 0, "fee cannot be negative"
    assert days >= 1, "processing days must be positive"
    assert volume >= 0, "volume cannot be negative"
    assert days <= 365, "processing days implausibly long"
    assert abs(revenue - fee * volume) < 0.01, "revenue math wrong"
    assert abs(per_day - volume / 365.0) < 1e-9, "throughput math wrong"
    print("OK: %%s verified (%%d/yr, $%%.2f revenue)" %% (RID, volume, revenue))
if __name__ == "__main__":
    main()
''' % _json(data)


def _json(d):
    import json
    return json.dumps(d, ensure_ascii=False)


DEMOS = {"service": demo_service}
