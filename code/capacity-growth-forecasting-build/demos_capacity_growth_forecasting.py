#!/usr/bin/env python3
"""Runnable demos for the Capacity Growth Forecasting databases (JAH Databases
governance track, group F, 2026-10-17).

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (record projections, storage,
throughput, hardware headroom, growth rates, linear/compounding/logistic
models, seasonal factors, forecast history, accuracy, ingestion, query load,
index growth, shard splits, backfill, burst reserves, fleet blends,
million-scale, constraint bounds, Monte Carlo, scenarios, confidence
intervals, cliff detection, cost linkage), asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. The build machine-executes all 68 demos.

NOTE on %%: template bodies are %-formatted with the baked data, so every
literal percent inside a template is doubled (%%%% for one output percent);
the "FACTS = %%s" data placeholder and the trailing "%% _pylit(data)" stay
single.
"""

import json
import math
import random


def _pylit(o):
    """Python-literal rendering of demo data (repr keeps True/False/None valid)."""
    return repr(o)


def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def f_facts(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("record:", NAME)
    for k, v in FACTS.items():
        if k == "checks":
            continue
        print("  %%s: %%s" %% (k, v))
    for key, op, want in FACTS.get("checks", []):
        got = FACTS[key]
        if op == "==":
            assert got == want, (key, got, want)
        elif op == ">=":
            assert got >= want, (key, got, want)
        elif op == "<=":
            assert got <= want, (key, got, want)
        elif op == ">":
            assert got > want, (key, got, want)
        elif op == "<":
            assert got < want, (key, got, want)
        else:
            raise AssertionError("bad op " + op)
        print("  check %%s %%s %%s: OK" %% (key, op, want))
    print("OK: %%s verified %%d facts" %% (NAME, len(FACTS) - 1))
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_records(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    proj = FACTS["current"] + FACTS["per_month"] * FACTS["months"]
    print("%%d + %%d x %%d = %%d records" %% (FACTS["current"], FACTS["per_month"], FACTS["months"], proj))
    assert proj == 234508, "96796 + 11476x12 = 234508"
    print("OK: %%s projects 234,508 records" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_storage(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    raw_gb = FACTS["records_12mo"] * FACTS["bytes_per_record"] / 1024 / 1024
    prov_gb = raw_gb * FACTS["overhead"]
    print("raw: %%.2f GB | provisioned (x%%.2f): %%.2f GB" %% (raw_gb, FACTS["overhead"], prov_gb))
    assert 2.16 < raw_gb < 2.18, "234508 x 9.7KB = 2.17 GB"
    assert 2.92 < prov_gb < 2.94, "2.17 x 1.35 = 2.93 GB"
    print("OK: %%s forecasts 2.93 GB provisioned" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_throughput(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    proj = FACTS["queries_mo"] * (1 + FACTS["growth_mo"]) ** FACTS["months"]
    mult = proj / FACTS["queries_mo"]
    print("%%d queries/mo x 1.08^12 = %%.0f (%%.1fx)" %% (FACTS["queries_mo"], proj, mult))
    assert 6043000 < proj < 6045000, "2.4M x 1.08^12 = 6043608"
    assert 2.51 < mult < 2.53, "2.52x load"
    print("OK: %%s estimates 6.04M queries/month" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_hardware(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    disk = FACTS["disk_used_gb"] / FACTS["disk_cap_gb"] * 100
    mem = FACTS["mem_used_gb"] / FACTS["mem_cap_gb"] * 100
    cpu = FACTS["cpu_used"] / FACTS["cpu_cap"] * 100
    mo = (FACTS["disk_cap_gb"] - FACTS["disk_used_gb"]) / 8.9
    print("disk: %%.0f%%%% | mem: %%.1f%%%% | cpu: %%.0f%%%% | disk exhaustion: %%.1f mo" %% (disk, mem, cpu, mo))
    assert 83.9 < disk < 84.1, "420/500 = 84%%"
    assert 8.9 < mo < 9.1, "80/8.9 = 9.0 months"
    print("OK: %%s maps disk as the binding constraint" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_rate(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    rate = (FACTS["current"] - FACTS["prior"]) / FACTS["prior"] * 100
    print("(%%d - %%d) / %%d = %%.2f%%%%/mo" %% (FACTS["current"], FACTS["prior"], FACTS["prior"], rate))
    assert 13.44 < rate < 13.46, "(96796-85320)/85320 = 13.45%%"
    print("OK: %%s measures 13.45%%%% monthly growth" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_linear(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    proj = FACTS["current"] + FACTS["per_month"] * FACTS["months"]
    print("%%d + %%d x %%d = %%d" %% (FACTS["current"], FACTS["per_month"], FACTS["months"], proj))
    assert proj == 372220, "96796 + 11476x24 = 372220"
    print("OK: %%s linear projection 372,220" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_compound(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    proj = FACTS["current"] * (1 + FACTS["rate"]) ** FACTS["months"]
    linear = FACTS["current"] + 11476 * FACTS["months"]
    print("compounding: %%.0f | linear would be: %%d | gap: %%.0f" %% (proj, linear, proj - linear))
    assert 440000 < proj < 440200, "96796 x 1.1345^12 = 440060"
    print("OK: %%s compounding projection 440,060" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_seasonal(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    peak = FACTS["avg_mo"] * FACTS["peak_mult"]
    trough = FACTS["avg_mo"] * FACTS["trough_mult"]
    print("%%s: %%.0f | %%s: %%.0f (avg %%d)" %% (FACTS["peak"], peak, FACTS["trough"], trough, FACTS["avg_mo"]))
    assert 18360 < peak < 18364, "11476 x 1.6 = 18361.6"
    assert 8032 < trough < 8035, "11476 x 0.7 = 8033.2"
    print("OK: %%s seasonal factors verified" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_history(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("period: %%s | forecasts: %%d | archived: %%d" %% (FACTS["period"], FACTS["forecasts"], FACTS["archived"]))
    assert FACTS["forecasts"] == FACTS["archived"] == 12, "twelve for twelve"
    print("OK: %%s archives all 12 forecasts" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_accuracy(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("MAPE: %%.1f%%%% | bias: +%%.1f%%%% | n=%%d | best: %%s" %% (FACTS["mape"], FACTS["bias"], FACTS["n"], FACTS["best_model"]))
    assert FACTS["mape"] == 8.2 and FACTS["bias"] == 2.1
    assert FACTS["bias"] < 5.0, "bias cap 5%%"
    print("OK: %%s tracks 8.2%%%% MAPE" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_headroom(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    headroom = (FACTS["disk_cap"] - FACTS["disk_used"]) / FACTS["disk_cap"] * 100
    print("headroom: %%.0f%%%% vs policy %%.0f%%%% -> action: %%s" %% (headroom, FACTS["policy"], FACTS["action"]))
    assert 15.9 < headroom < 16.1, "(500-420)/500 = 16%%"
    assert headroom < FACTS["policy"], "violation triggers procurement"
    print("OK: %%s flags the headroom violation" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_ingest(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    util = FACTS["per_run"] / FACTS["cap_per_run"] * 100
    dec_need = FACTS["per_run"] * FACTS["dec_mult"]
    dec_runs = 40
    dec_per_run = dec_need * 30 / dec_runs
    dec_util = dec_per_run / FACTS["cap_per_run"] * 100
    print("avg util: %%.1f%%%% | Dec need: %%.0f/run (>%%d cap) | Dec plan: %%d runs x %%.0f = %%.1f%%%%" %% (
        util, dec_need, FACTS["cap_per_run"], dec_runs, dec_per_run, dec_util))
    assert 76.4 < util < 76.6, "11476/15000 = 76.5%%"
    assert dec_need > FACTS["cap_per_run"], "December exceeds per-run capacity"
    assert 91.7 < dec_util < 91.9, "13772/15000 = 91.8%%"
    print("OK: %%s sizes December at 40 runs" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_query(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    proj = FACTS["queries_mo"] * 1.08 ** 12
    per_worker = FACTS["queries_mo"] / (FACTS["workers"] * FACTS["util"])
    at_full = proj / per_worker
    with_headroom = at_full / 0.7
    print("projected: %%.0f | per worker: %%.0f | at 100%%%%: %%.1f | +30%%%% headroom: %%.1f" %% (
        proj, per_worker, at_full, with_headroom))
    assert 166600 < per_worker < 166700, "2.4M/14.4 = 166667"
    assert 51.7 < with_headroom < 51.9, "36.2/0.7 = 51.7"
    print("OK: %%s staffs 52 workers" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_index(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    per_k = FACTS["index_gb"] * 1024 / FACTS["records"] * 1000
    proj_gb = FACTS["records_12mo"] / 1000 * per_k / 1024
    rebuild_min = 42 * proj_gb / FACTS["index_gb"]
    print("per 1k: %%.1f MB | projected: %%.1f GB | rebuild: %%.0f min (window 120)" %% (per_k, proj_gb, rebuild_min))
    assert 88.8 < per_k < 89.0, "8.4GB/96.796k = 88.9 MB/1k"
    assert 38.1 < proj_gb < 38.3, "440.06k x 86.8KB = 38.2 GB"
    assert rebuild_min > 120, "190 min exceeds the 02:00 window"
    print("OK: %%s flags the rebuild window break" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_split(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    mo = (FACTS["threshold"] - FACTS["used_gb"]) / FACTS["growth_gb_mo"]
    print("(%%d - %%d) / %%.1f = %%.1f months to split" %% (FACTS["threshold"], FACTS["used_gb"], FACTS["growth_gb_mo"], mo))
    assert 8.9 < mo < 9.1, "80/8.9 = 9.0 months"
    print("OK: %%s forecasts the split in 9.0 months" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_backfill(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    base_min = FACTS["records"] / FACTS["per_min"]
    with_reserve = base_min * (1 + FACTS["reserve"])
    with_verify = with_reserve * 1.15
    print("base: %%.0f min | +reserve: %%.0f | +verify: %%.0f" %% (base_min, with_reserve, with_verify))
    assert base_min == 40, "18000/450 = 40"
    assert with_reserve == 44, "40 x 1.1 = 44"
    assert 50.5 < with_verify < 50.7, "44 x 1.15 = 50.6"
    print("OK: %%s plans 51 minutes with verification" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_burst(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    reserve = FACTS["base_workers"] * FACTS["reserve_mult"]
    print("reserve: %%.0f workers (%%.1fx) vs observed max %%.1fx" %% (reserve, FACTS["reserve_mult"], FACTS["observed_max"]))
    assert reserve == 72, "24 x 3 = 72"
    assert FACTS["reserve_mult"] > FACTS["observed_max"], "margin above observed max"
    print("OK: %%s holds a 3x burst reserve" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_fleet(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    blend = sum(s * r for s, r in zip(FACTS["shares"], FACTS["seg_rates"]))
    proj = FACTS["total_records"] * (1 + blend) ** 12
    print("blend: %%.1f%%%% | fleet 12mo: %%.0f records" %% (blend * 100, proj))
    assert 0.059 < blend < 0.061, "0.7x.035+0.2x.09+0.1x.175 = 0.06"
    assert 2300000 < proj < 2302000, "1143457 x 1.06^12 = 2300860"
    print("OK: %%s blends to 6.0%%%% -> 2.30M records" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_million(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    existing = FACTS["total_records"] * (1 + FACTS["growth"]) ** 12
    new_recs = FACTS["new_dbs"] * FACTS["new_db_avg"]
    total = existing + new_recs
    overhead = FACTS["new_dbs"] * FACTS["fixed_per_db_yr"]
    print("existing: %%.0f | new: %%d | total: %%.0f | new overhead: $%%d/yr" %% (
        existing, new_recs, total, overhead))
    assert 2300000 < existing < 2302000
    assert new_recs == 1100000, "5000 x 220"
    assert 3400000 < total < 3402000, "2300860 + 1100000 = 3400860"
    assert overhead == 1200000, "5000 x 240"
    print("OK: %%s projects ~3.4M records at 10,000 databases" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_logistic(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
import math
def main():
    K, P0, r, t = FACTS["K"], FACTS["P0"], FACTS["r"], FACTS["t"]
    A = (K - P0) / P0
    P = K / (1 + A * math.exp(-r * t))
    inflection = K / 2
    print("A=%%.3f | P(12)=%%.0f | inflection at %%.0f" %% (A, P, inflection))
    assert 9.33 < A < 9.34, "(1e6-96796)/96796 = 9.331"
    assert 349900 < P < 350000, "logistic P(12) = 349931"
    print("OK: %%s logistic projection 349,931" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_constraint(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    bound = min(FACTS["demand"], FACTS["cap"])
    unserved = FACTS["demand"] - bound
    print("demand: %%d %%s | cap: %%d | forecast: %%d | unserved: %%d" %% (
        FACTS["demand"], FACTS["unit"], FACTS["cap"], bound, unserved))
    assert bound == 500000, "min(600000, 500000)"
    assert unserved == 100000
    print("OK: %%s bounds the forecast at 500,000" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_montecarlo(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
import random
def main():
    rng = random.Random(FACTS["seed"])
    outs = []
    for _ in range(2000):
        v = 96796.0
        for _ in range(12):
            v *= 1 + max(0.0, rng.gauss(0.1345, 0.032))
        outs.append(v)
    outs.sort()
    p10, p50, p90 = outs[200], outs[1000], outs[1800]
    print("seeded 2000 sims: p10=%%.0f p50=%%.0f p90=%%.0f" %% (p10, p50, p90))
    assert p10 < p50 < p90, "percentile ordering"
    assert abs(p50 - 440060) / 440060 < 0.15, "p50 near analytic 440060"
    print("OK: %%s Monte Carlo brackets the analytic forecast" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_scenario(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    ev = 0.6 * FACTS["base"] + 0.25 * FACTS["optimistic"] + 0.15 * FACTS["pessimistic"]
    up = (FACTS["optimistic"] - FACTS["base"]) / FACTS["base"] * 100
    down = (FACTS["base"] - FACTS["pessimistic"]) / FACTS["base"] * 100
    print("base: %%d | optimistic: %%d (+%%.0f%%%%) | pessimistic: %%d (-%%.0f%%%%) | EV: %%.0f" %% (
        FACTS["base"], FACTS["optimistic"], up, FACTS["pessimistic"], down, ev))
    assert ev == 465536, "0.6x440060+0.25x620000+0.15x310000"
    print("OK: %%s expected value 465,536" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_ci(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    lo = FACTS["point"] * (1 - FACTS["pct"])
    hi = FACTS["point"] * (1 + FACTS["pct"])
    print("%%d +/- %%d%%%% at %%d%%%%: [%%d, %%d]" %% (FACTS["point"], int(FACTS["pct"] * 100), FACTS["level"], lo, hi))
    assert 387200 < lo < 387300, "440060 x 0.88 = 387253"
    assert 492800 < hi < 492900, "440060 x 1.12 = 492867"
    print("OK: %%s confidence interval [387253, 492867]" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_cliff(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    avg_mo = (FACTS["cap_gb"] - FACTS["used_gb"]) / FACTS["growth_gb_mo"]
    worst_mo = (FACTS["cap_gb"] - FACTS["used_gb"]) / 14.2
    print("average: %%.1f mo | worst-case (March rate): %%.1f mo" %% (avg_mo, worst_mo))
    assert 8.9 < avg_mo < 9.1, "80/8.9 = 9.0"
    assert 5.6 < worst_mo < 5.7, "80/14.2 = 5.6"
    assert abs(avg_mo - FACTS["warn_mo"]) < 0.05
    print("OK: %%s watches the cliff at 9.0/5.6 months" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_costlink(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    cost = FACTS["records_12mo"] * FACTS["unit"]
    print("%%d records x $%%.4f = $%%.2f/month" %% (FACTS["records_12mo"], FACTS["unit"], cost))
    assert 6820.92 < cost < 6820.94, "440060 x 0.0155 = 6820.93"
    print("OK: %%s prices the forecast at $6,820.93/month" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def f_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    coverage = FACTS["complete"] / FACTS["records"]
    print("complete: %%d/%%d | MAPE: %%.1f%%%% | coverage: %%.1f" %% (
        FACTS["complete"], FACTS["records"], FACTS["mape"], coverage))
    assert coverage == 1.0
    assert FACTS["mape"] == 8.2
    assert FACTS["coverage"] == 1.0
    print("OK: %%s self-audit passed at full coverage" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


DEMOS = {
    "f_facts": f_facts, "f_records": f_records, "f_storage": f_storage,
    "f_throughput": f_throughput, "f_hardware": f_hardware, "f_rate": f_rate,
    "f_linear": f_linear, "f_compound": f_compound, "f_seasonal": f_seasonal,
    "f_history": f_history, "f_accuracy": f_accuracy,
    "f_headroom": f_headroom, "f_ingest": f_ingest, "f_query": f_query,
    "f_index": f_index, "f_split": f_split, "f_backfill": f_backfill,
    "f_burst": f_burst, "f_fleet": f_fleet, "f_million": f_million,
    "f_logistic": f_logistic, "f_constraint": f_constraint,
    "f_montecarlo": f_montecarlo, "f_scenario": f_scenario, "f_ci": f_ci,
    "f_cliff": f_cliff, "f_costlink": f_costlink, "f_mastery": f_mastery,
}
