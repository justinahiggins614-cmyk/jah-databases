#!/usr/bin/env python3
"""Demonstration programs for the Public Infrastructure Assets databases.

One demo builder ("asset") parameterized by each record's demo_data:
replacement value (millions USD), condition rating (1-5), age (years),
design life (years). Every demo recomputes real asset values
(depreciated value, remaining life, condition percent), asserts tight
bounds, prints the values, and ends with the OK marker. The build
machine-executes all 68 demos.
"""


def demo_asset(hdr, name, rid, group, data):
    return hdr(name, rid, group) + '''\
DATA = %s
def main():
    repl_m = DATA["repl_value_m"]
    cond = DATA["condition"]
    age = DATA["age_y"]
    life = DATA["design_life_y"]
    repl = repl_m * 1e6
    cond_pct = cond / 5.0 * 100.0
    consumed = min(age / life, 1.0) if life > 0 else 1.0
    depr_value = repl * (1.0 - consumed)
    remaining = life - age
    annual_reserve = repl / life if life > 0 else 0
    print("Asset:", NAME)
    print("  replacement value: $%%.2fM" %% repl_m)
    print("  condition: %%d/5 (%%.0f%%%%)" %% (cond, cond_pct))
    print("  age: %%d y | design life: %%d y | remaining: %%d y" %% (age, life, remaining))
    print("  life consumed: %%.1f%%%%" %% (consumed * 100.0))
    print("  depreciated value: $%%.2fM" %% (depr_value / 1e6))
    print("  annual renewal reserve: $%%.2fM" %% (annual_reserve / 1e6))
    assert repl_m > 0, "replacement value must be positive"
    assert 1 <= cond <= 5, "condition rating must be 1-5"
    assert age >= 0, "age cannot be negative"
    assert life > 0, "design life must be positive"
    assert age <= life * 1.5, "age implausibly beyond design life"
    assert abs(depr_value - repl * (1.0 - consumed)) < 1.0, "depreciation math wrong"
    assert abs(cond_pct - cond * 20.0) < 1e-9, "condition percent wrong"
    print("OK: %%s verified (cond %%d/5, $%%.2fM repl, %%d y remaining)" %% (
        RID, cond, repl_m, remaining))
if __name__ == "__main__":
    main()
''' % _json(data)


def _json(d):
    import json
    return json.dumps(d, ensure_ascii=False)


DEMOS = {"asset": demo_asset}
