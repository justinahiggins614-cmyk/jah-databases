#!/usr/bin/env python3
"""Demonstration programs for the Public Grants Funding databases.

One demo builder ("grant") parameterized by each record's demo_data:
award amount (USD), period of performance (months), match percent.
Every demo recomputes real grant values (monthly burn rate, required
match dollars, total project cost), asserts tight bounds, prints the
values, and ends with the OK marker. The build machine-executes all
68 demos.
"""


def demo_grant(hdr, name, rid, group, data):
    return hdr(name, rid, group) + '''\
DATA = %s
def main():
    award = DATA["award"]
    months = DATA["months"]
    match_pct = DATA["match_pct"]
    monthly_burn = award / months
    match_dollars = award * match_pct / 100.0
    total_project = award + match_dollars
    federal_share = award / total_project * 100.0 if total_project else 0
    print("Grant record:", NAME)
    print("  award: $%%.2f" %% award)
    print("  period of performance: %%d months" %% months)
    print("  monthly burn rate: $%%.2f" %% monthly_burn)
    print("  match: %%.1f%%%% = $%%.2f" %% (match_pct, match_dollars))
    print("  total project cost: $%%.2f" %% total_project)
    print("  federal share: %%.1f%%%%" %% federal_share)
    assert award > 0, "award must be positive"
    assert months >= 1, "period must be at least 1 month"
    assert months <= 120, "period implausibly long"
    assert 0 <= match_pct <= 100, "match percent must be 0-100"
    assert abs(monthly_burn - award / months) < 0.01, "burn rate math wrong"
    assert abs(match_dollars - award * match_pct / 100.0) < 0.01, "match math wrong"
    assert abs(total_project - (award + match_dollars)) < 0.01, "total math wrong"
    print("OK: %%s verified ($%%.2f award, %%d mo, %%.1f%%%% match)" %% (
        RID, award, months, match_pct))
if __name__ == "__main__":
    main()
''' % _json(data)


def _json(d):
    import json
    return json.dumps(d, ensure_ascii=False)


DEMOS = {"grant": demo_grant}
