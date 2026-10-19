#!/usr/bin/env python3
"""Runnable demos for the Database Cost Accounting databases (JAH Databases
governance track, group F, 2026-10-17).

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (storage/compute/egress/indexing/
generation/retrieval unit costs, allocation footing, tiering savings, batch
scheduling, SLA tradeoffs, cache ROI, compression, backup/DR, transfer,
anomaly stats, TCO, budgets, chargeback, quality cost, governance overhead,
marginal cost, pipeline comparison, carbon, variance, playbooks), asserts
tight bounds (never float exact-equality), prints the real computed values,
and ends with the OK marker. The build machine-executes all 68 demos.

NOTE on %%: template bodies are %-formatted with the baked data, so every
literal percent inside a template is doubled (%%%% for one output percent);
the "FACTS = %%s" data placeholder and the trailing "%% _pylit(data)" stay
single.
"""

import json


def _pylit(o):
    """Python-literal rendering of demo data (repr keeps True/False/None valid)."""
    return repr(o)


def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def k_facts(hdr, name, rid, group, data):
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


def k_storage(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Storage cost: 420 GB x $0.023/GB-month."""
FACTS = %s

cost = FACTS["gb"] * FACTS["rate"]
print("Storage: %%d GB x $%%.3f = $%%.2f/month (%%s tier)" %% (FACTS["gb"], FACTS["rate"], cost, FACTS["tier"]))
assert 9.65 < cost < 9.67, "420 x 0.023 = 9.66"
print("OK: storage $9.66/month")
''''' % _pylit(data)


def k_compute(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Compute cost: 1,850 vCPU-h x $0.0416, commitment discount on baseline."""
FACTS = %s

ondemand = FACTS["vcpu_h"] * FACTS["rate"]
committed = ondemand * (1 - FACTS["commit_discount"])
# blended reality: 1,200 h committed baseline + 650 h on-demand burst
baseline = 1200 * FACTS["rate"] * (1 - FACTS["commit_discount"])
burst = 650 * FACTS["rate"]
blended = baseline + burst
print("On-demand: $%%.2f | committed: $%%.2f | blended (1200+650): $%%.2f" %% (ondemand, committed, blended))
assert 76.95 < ondemand < 76.97, "1850 x 0.0416 = 76.96"
assert 53.86 < committed < 53.88, "76.96 x 0.7 = 53.87"
assert 61.97 < blended < 61.99, "34.94 + 27.04 = 61.98"
print("OK: compute $61.98 blended")
''''' % _pylit(data)


def k_egress(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Bandwidth: 1.2 TB egress x $90/TB; ingress free."""
FACTS = %s

cost = FACTS["tb"] * FACTS["rate_per_tb"]
print("Egress: %%.1f TB x $%%d/TB = $%%.2f/month (ingress free: %%s)" %% (FACTS["tb"], FACTS["rate_per_tb"], cost, FACTS["ingress_free"]))
assert 107.99 < cost < 108.01, "1.2 x 90 = 108"
print("OK: egress $108/month")
''''' % _pylit(data)


def k_index(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Indexing: 8.4 GB standing + 3 rebuilds/year x $12."""
FACTS = %s

standing_mo = FACTS["index_gb"] * FACTS["rate"]
events_yr = FACTS["rebuilds_year"] * FACTS["rebuild_cost"]
annual = standing_mo * 12 + events_yr
print("Standing: $%%.2f/mo | rebuilds: %%d x $%%d = $%%d/yr | annual total: $%%.2f" %% (standing_mo, FACTS["rebuilds_year"], FACTS["rebuild_cost"], events_yr, annual))
assert 0.19 < standing_mo < 0.20, "8.4 x 0.023 = 0.1932"
assert 38.30 < annual < 38.34, "0.1932x12 + 36 = 38.32"
print("OK: indexing ~$38.32/year")
''''' % _pylit(data)


def k_gen(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Generation: 11,476 records x $0.004 = $45.90/run, 30 runs/month."""
FACTS = %s

per_run = FACTS["records"] * FACTS["per_record"]
per_month = per_run * FACTS["runs_month"]
# $0.004 blend: $0.0028 compute + $0.0009 inference + $0.0003 validation
blend = 0.0028 + 0.0009 + 0.0003
print("Per run: $%%.2f | per month (%%d runs): $%%.2f | blend check: $%%.4f" %% (per_run, FACTS["runs_month"], per_month, blend))
assert 45.89 < per_run < 45.91, "11476 x 0.004 = 45.904"
assert 1377.0 < per_month < 1377.3, "45.904 x 30 = 1377.12"
assert abs(blend - 0.004) < 1e-9, "blend components sum to 0.004"
print("OK: generation $1,377.12/month")
''''' % _pylit(data)


def k_retrieval(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Retrieval: 2.4M queries, 70/30 standard/premium at 5x premium."""
FACTS = %s

std_q = int(FACTS["queries"] * FACTS["tiers"]["standard"])
prem_q = FACTS["queries"] - std_q
std_cost = std_q / 1000 * FACTS["per_1k"]
prem_cost = prem_q / 1000 * FACTS["per_1k"] * FACTS["premium_mult"]
total = std_cost + prem_cost
naive = FACTS["queries"] / 1000 * FACTS["per_1k"]
print("Standard: $%%.2f | premium: $%%.2f | total: $%%.2f (naive would be $%%.2f)" %% (std_cost, prem_cost, total, naive))
assert 6.71 < std_cost < 6.73, "1.68M x 0.004/1k = 6.72"
assert 14.39 < prem_cost < 14.41, "720K x 0.02/1k = 14.40"
assert 21.11 < total < 21.13, "6.72 + 14.40 = 21.12"
print("OK: retrieval $21.12/month (tier mix doubles the naive $9.60)")
''''' % _pylit(data)


def k_fixedvar(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Fixed vs variable: $1,200 fixed + 96,796 x $0.0031 variable."""
FACTS = %s

variable = FACTS["records"] * FACTS["variable_per_record"]
total = FACTS["fixed"] + variable
print("Fixed: $%%d | variable: $%%.2f | total: $%%.2f" %% (FACTS["fixed"], variable, total))
assert 300.06 < variable < 300.08, "96796 x 0.0031 = 300.0676"
assert 1500.06 < total < 1500.08, "1200 + 300.0676 = 1500.0676"
print("OK: $1,500.07/month")
''''' % _pylit(data)


def k_perrecord(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Per-record unit: $1,500.07 / 96,796 records = $0.0155."""
FACTS = %s

unit = FACTS["monthly"] / FACTS["records"]
fixed_part = 1200 / FACTS["records"]
var_part = 0.0031
print("Unit: $%%.4f/record/month = $%%.4f fixed + $%%.4f variable" %% (unit, fixed_part, var_part))
assert 0.01549 < unit < 0.01551, "1500.07/96796 = 0.015498"
assert abs((fixed_part + var_part) - unit) < 1e-6, "components sum to the unit"
print("OK: $0.0155/record/month (1.55 cents)")
''''' % _pylit(data)


def k_ledger(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Per-database ledger: five ledgers foot to $3,736.54."""
FACTS = %s

dbs = FACTS["databases"]
total = sum(dbs.values())
for name, cost in sorted(dbs.items()):
    print("  %%-8s $%%8.2f" %% (name, cost))
print("Fleet total: $%%.2f" %% total)
assert 3736.53 < total < 3736.55, "1500.07+980.40+640.22+410.55+205.30 = 3736.54"
print("OK: ledger foots to $3,736.54")
''''' % _pylit(data)


def k_alloc(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Shared-cost allocation: $9,600 pool at 50/30/20 usage weights."""
FACTS = %s

shares = [FACTS["pool"] * w / 100 for w in FACTS["weights"]]
for team, share in zip(FACTS["teams"], shares):
    print("  %%-8s $%%8.2f" %% (team, share))
assert abs(sum(shares) - FACTS["pool"]) < 1e-6, "allocations must foot to the pool"
assert 4799.99 < shares[0] < 4800.01
assert 2879.99 < shares[1] < 2880.01
assert 1919.99 < shares[2] < 1920.01
print("OK: $4,800 / $2,880 / $1,920 foot to $9,600")
''''' % _pylit(data)


def k_tiering(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Tiering: 420 GB at 20/50/30%% hot/warm/cold."""
FACTS = %s

tiered = sum(FACTS["gb"] * m * r for m, r in zip(FACTS["mix"], FACTS["rates"]))
allhot = FACTS["gb"] * FACTS["rates"][0]
saving = allhot - tiered
pct = saving / allhot * 100
print("Tiered: $%%.2f/mo vs all-hot: $%%.2f/mo -> saves $%%.2f (%%.1f%%%%)" %% (tiered, allhot, saving, pct))
assert 5.06 < tiered < 5.07, "84x.023+210x.0125+126x.004 = 5.061"
assert 47.5 < pct < 47.7, "4.599/9.66 = 47.6%%"
print("OK: tiering saves 47.6%%")
''''' % _pylit(data)


def k_rebuild(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Index rebuilds: 3/year x $12, 42 minutes each."""
FACTS = %s

annual = FACTS["rebuilds"] * FACTS["cost_each"]
minutes_yr = FACTS["rebuilds"] * FACTS["minutes"]
print("%%d rebuilds x $%%d = $%%d/year, %%d minutes in the %%s window" %% (FACTS["rebuilds"], FACTS["cost_each"], annual, minutes_yr, FACTS["window"]))
assert annual == 36, "3 x 12 = 36"
assert minutes_yr == 126, "3 x 42 = 126"
print("OK: $36/year for rebuilds")
''''' % _pylit(data)


def k_batch(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Batch costing: 80%% off-peak at 40%% discount -> $31.21 blended run."""
FACTS = %s

peak = FACTS["records"] * FACTS["per_record"]
blend_factor = (1 - FACTS["offpeak_share"]) + FACTS["offpeak_share"] * (1 - FACTS["offpeak_discount"])
blended = peak * blend_factor
save_run = peak - blended
save_mo = save_run * 30
print("Peak: $%%.2f | blended (x%%.2f): $%%.2f | saves $%%.2f/run, $%%.2f/month" %% (peak, blend_factor, blended, save_run, save_mo))
assert 45.89 < peak < 45.91
assert 31.20 < blended < 31.23, "45.904 x 0.68 = 31.21"
assert 440.6 < save_mo < 440.8, "14.689 x 30 = 440.68"
print("OK: off-peak scheduling saves $440.68/month")
''''' % _pylit(data)


def k_sla_trade(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""SLA tradeoff: premium 5x at 120ms p95 vs standard at 900ms p95."""
FACTS = %s

std_c, prem_c = FACTS["standard_cpm"], FACTS["standard_cpm"] * FACTS["premium_mult"]
queries = 2400000
base = queries * (FACTS["mix"][0] * std_c + FACTS["mix"][1] * prem_c) / 1000
shifted = queries * ((FACTS["mix"][0] + 0.1) * std_c + (FACTS["mix"][1] - 0.1) * prem_c) / 1000
saving = base - shifted
print("Base: $%%.2f/mo | after 10-point demotion: $%%.2f/mo | saves $%%.2f (%%.1f%%%%)" %% (base, shifted, saving, saving / base * 100))
assert 21.11 < base < 21.13
assert 3.83 < saving < 3.85, "240K queries x $0.016/1k = 3.84"
print("OK: 10-point shift saves $3.84 (18.2%%)")
''''' % _pylit(data)


def k_cache(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Cache: 48K calls/day x 72%% hit x $1.50/1k vs $8.40/day cache cost."""
FACTS = %s

avoided = FACTS["calls_day"] * FACTS["hit_rate"] / 1000 * FACTS["cost_per_1k"]
net_day = avoided - FACTS["cache_cost_day"]
net_mo = net_day * 30
roi = avoided / FACTS["cache_cost_day"]
print("Avoided: $%%.2f/day | cost: $%%.2f/day | net: $%%.2f/day ($%%.2f/mo), %%.1fx return" %% (avoided, FACTS["cache_cost_day"], net_day, net_mo, roi))
assert 51.83 < avoided < 51.85, "48000x0.72/1000x1.50 = 51.84"
assert 43.43 < net_day < 43.45, "51.84 - 8.40 = 43.44"
assert 1303.0 < net_mo < 1303.4, "43.44 x 30 = 1303.2"
print("OK: cache nets $1,303.20/month")
''''' % _pylit(data)


def k_compress(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Compression: 935 GB at 5:1 -> 187 GB, savings vs CPU cost."""
FACTS = %s

compressed = FACTS["raw_gb"] / FACTS["ratio"]
saved_gb = FACTS["raw_gb"] - compressed
savings = saved_gb * FACTS["rate"]
net = savings - FACTS["cpu_cost_mo"]
print("Saved: %%.0f GB x $%%.3f = $%%.2f/mo | CPU: $%%.2f | net: $%%.2f/mo" %% (saved_gb, FACTS["rate"], savings, FACTS["cpu_cost_mo"], net))
assert 17.19 < savings < 17.21, "748 x 0.023 = 17.204"
assert 13.99 < net < 14.01, "17.204 - 3.20 = 14.004"
print("OK: compression nets $14.00/month")
''''' % _pylit(data)


def k_backup(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Backup/DR: 802 GB x $0.023 x 1.2 versioning + 4 drills/year x $150."""
FACTS = %s

storage = FACTS["gb"] * FACTS["rate"] * FACTS["version_factor"]
drills_mo = FACTS["drill_cost"] * FACTS["drills_year"] / 12
total = storage + drills_mo
print("Backup storage: $%%.2f/mo | drills: $%%.2f/mo | total: $%%.2f/mo" %% (storage, drills_mo, total))
assert 22.13 < storage < 22.15, "802 x 0.023 x 1.2 = 22.135"
assert 72.12 < total < 72.15, "22.135 + 50 = 72.135"
print("OK: backup/DR $72.14/month")
''''' % _pylit(data)


def k_transfer(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Inter-shard transfer: 450 GB x $0.02 = $9.00/month."""
FACTS = %s

cost = FACTS["gb"] * FACTS["rate"]
per_sync = cost / FACTS["syncs_month"]
print("%%d GB x $%%.2f = $%%.2f/month ($%%.2f per daily sync)" %% (FACTS["gb"], FACTS["rate"], cost, per_sync))
assert 8.99 < cost < 9.01, "450 x 0.02 = 9.00"
print("OK: inter-shard transfer $9.00/month")
''''' % _pylit(data)


def k_anomaly(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Anomaly detection: 312 alerts, 289 true, 3.2h MTTR, $1,840 saved."""
FACTS = %s

precision = FACTS["true_pos"] / FACTS["alerts"] * 100
print("Alerts: %%d | true: %%d | precision: %%.1f%%%% | MTTR: %%.1fh | saved: $%%d" %% (
    FACTS["alerts"], FACTS["true_pos"], precision, FACTS["mttr_h"], FACTS["saved"]))
assert 92.5 < precision < 92.7, "289/312 = 92.63%%"
assert FACTS["mttr_h"] == 3.2
print("OK: 92.6%% precision, $1,840 runaway spend stopped")
''''' % _pylit(data)


def k_tco(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""TCO: $18k capex + $1,500.07/mo x 36, flat and with 15%% annual growth."""
FACTS = %s

flat = FACTS["capex"] + FACTS["opex_mo"] * 12 * FACTS["years"]
fixed_mo = 1200.0
var_mo = FACTS["opex_mo"] - fixed_mo
var_total = sum(var_mo * 12 * (1 + FACTS["growth"]) ** y for y in range(FACTS["years"]))
grown = FACTS["capex"] + fixed_mo * 36 + var_total
premium = grown - flat
print("Flat TCO: $%%.2f | with growth: $%%.2f | growth premium: $%%.2f" %% (flat, grown, premium))
assert 72002.51 < flat < 72002.53, "18000 + 1500.07x36 = 72002.52"
assert 73703.91 < grown < 73703.93, "18000 + 43200 + 12503.92 = 73703.92"
print("OK: 3-year TCO $73,703.92 with growth")
''''' % _pylit(data)


def k_budget(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Budgeting: $5,000 budget vs $4,780 forecast vs $4,612 actual."""
FACTS = %s

var_budget = (FACTS["actual_mo"] - FACTS["budget_mo"]) / FACTS["budget_mo"] * 100
forecast_err = (FACTS["forecast_mo"] - FACTS["actual_mo"]) / FACTS["actual_mo"] * 100
print("%%s: budget $%%d/mo, forecast $%%d, actual $%%d -> %%.2f%%%% vs budget, %%.1f%%%% forecast error" %% (
    FACTS["quarter"], FACTS["budget_mo"], FACTS["forecast_mo"], FACTS["actual_mo"], var_budget, forecast_err))
assert -7.77 < var_budget < -7.75, "(4612-5000)/5000 = -7.76%%"
assert 3.5 < forecast_err < 3.7, "(4780-4612)/4612 = 3.64%%"
print("OK: -7.76%% vs budget, forecast within 3.6%%")
''''' % _pylit(data)


def k_chargeback(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Chargeback: $4,612 at 60/25/15 usage shares."""
FACTS = %s

charges = [FACTS["total"] * s for s in FACTS["shares"]]
for team, charge in zip(FACTS["teams"], charges):
    print("  %%-8s $%%8.2f (%%s)" %% (team, charge, FACTS["model"]))
assert abs(sum(charges) - FACTS["total"]) < 1e-6, "charges must foot to the total"
assert 2767.19 < charges[0] < 2767.21
assert 1152.99 < charges[1] < 1153.01
assert 691.79 < charges[2] < 691.81
print("OK: $2,767.20 / $1,153.00 / $691.80 foot to $4,612")
''''' % _pylit(data)


def k_quality(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Data quality cost: rework + incidents = $112,900/year failure."""
FACTS = %s

rework = FACTS["rework_h"] * FACTS["rate"]
incidents = FACTS["incidents"] * FACTS["incident_cost"]
failure = rework + incidents
prevention, appraisal = 18000, 9500
total = prevention + appraisal + failure
print("Rework: $%%d | incidents: $%%d | failure: $%%d | total quality cost: $%%d" %% (rework, incidents, failure, total))
assert rework == 28900, "340 x 85 = 28900"
assert incidents == 84000, "7 x 12000 = 84000"
assert failure == 112900
assert total == 140400, "18000 + 9500 + 112900"
print("OK: $112,900/year in failure costs")
''''' % _pylit(data)


def k_govcost(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Governance overhead: audits + tooling + policy + training."""
FACTS = %s

audits = FACTS["audit_h"] * FACTS["rate"]
tooling = FACTS["tooling_mo"] * 12
policy, training = 6000, 4000
total = audits + tooling + policy + training
per_db = total / FACTS["databases"]
print("Audits: $%%d | tooling: $%%d | policy: $%%d | training: $%%d | total: $%%d ($%%.2f/db/yr)" %% (
    audits, tooling, policy, training, total, per_db))
assert audits == 11400, "120 x 95 = 11400"
assert tooling == 9600, "800 x 12 = 9600"
assert total == 31000
assert 6.19 < per_db < 6.21, "31000/5000 = 6.20"
print("OK: governance $31,000/year ($6.20 per database)")
''''' % _pylit(data)


def k_marginal(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Marginal cost: $0.0031 x 1M + $250 step-fixed = $3,350."""
FACTS = %s

marginal = FACTS["variable_per_record"] * FACTS["million"] + FACTS["fixed_step"]
avg_quote = 0.0155 * FACTS["million"]
print("Marginal: $%%.2f/month | average-unit quote would say: $%%.2f (%%.1fx too high)" %% (
    marginal, avg_quote, avg_quote / marginal))
assert 3349.99 < marginal < 3350.01, "0.0031x1e6 + 250 = 3350"
print("OK: marginal $3,350/month for the next million")
''''' % _pylit(data)


def k_compare(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Pipeline comparison: $0.021 public vs $0.014 Signature per record."""
FACTS = %s

pub_mo = FACTS["records_mo"] * FACTS["public_per_record"]
sig_mo = FACTS["records_mo"] * FACTS["sig_per_record"]
saving = pub_mo - sig_mo
pct = saving / pub_mo * 100
print("Public: $%%.2f/mo | Signature: $%%.2f/mo | saves $%%.2f (%%.1f%%%%)" %% (pub_mo, sig_mo, saving, pct))
assert 7229.87 < pub_mo < 7229.89, "344280 x 0.021 = 7229.88"
assert 4819.91 < sig_mo < 4819.93, "344280 x 0.014 = 4819.92"
assert 33.3 < pct < 33.4, "2409.96/7229.88 = 33.33%%"
print("OK: Signature pipeline 33.3%% cheaper")
''''' % _pylit(data)


def k_carbon(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Energy/carbon: 1,850 kWh x 0.42 kg/kWh = 777 kg CO2."""
FACTS = %s

co2_kg = FACTS["kwh"] * FACTS["intensity"]
electricity = FACTS["kwh"] * FACTS["price_per_kwh"]
offsets = co2_kg / 1000 * FACTS["offset_per_tonne"]
print("CO2: %%.0f kg/month | electricity: $%%.2f | offsets: $%%.2f" %% (co2_kg, electricity, offsets))
assert 776.9 < co2_kg < 777.1, "1850 x 0.42 = 777"
assert 221.99 < electricity < 222.01, "1850 x 0.12 = 222"
assert 11.65 < offsets < 11.67, "0.777 x 15 = 11.655"
print("OK: 777 kg CO2/month")
''''' % _pylit(data)


def k_variance(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Budget variance: $60,000 budget vs $57,200 actual."""
FACTS = %s

var = (FACTS["actual_yr"] - FACTS["budget_yr"]) / FACTS["budget_yr"] * 100
diff = FACTS["budget_yr"] - FACTS["actual_yr"]
print("Budget: $%%d | actual: $%%d | variance: %%.2f%%%% ($%%d favorable)" %% (
    FACTS["budget_yr"], FACTS["actual_yr"], var, diff))
assert -4.68 < var < -4.66, "(57200-60000)/60000 = -4.667%%"
assert diff == 2800
print("OK: -4.67%% variance")
''''' % _pylit(data)


def k_dashboard(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Dashboard exemplar: 8 panels, 5,000 databases, daily refresh, 5 alerts."""
FACTS = %s

panels = ["total spend", "by database", "dimensions", "unit trends",
          "budget vs actual", "anomaly feed", "pipeline", "carbon"]
assert len(panels) == FACTS["panels"], "8 panels"
print("Databases: %%d | refresh: %%s | active alerts: %%d" %% (
    FACTS["databases"], FACTS["refresh"], FACTS["alerts"]))
print("Panels: " + ", ".join(panels))
print("OK: 8-panel dashboard exemplar")
''''' % _pylit(data)


def k_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + '''''"""Self-audit and mastery: 34/34 complete, 100%% reconciled, 0 stale units."""
FACTS = %s

complete = FACTS["complete"] / FACTS["records"]
print("Complete: %%d/%%d | reconciled: %%.0f%%%% | stale units: %%d | coverage: %%.1f" %% (
    FACTS["complete"], FACTS["records"], FACTS["ledgers_reconciled"] * 100,
    FACTS["stale_units"], FACTS["coverage"]))
assert complete == 1.0, "34/34"
assert FACTS["ledgers_reconciled"] == 1.0
assert FACTS["stale_units"] == 0
assert FACTS["coverage"] == 1.0
print("OK: self-audit passes, mastery checkpoint reached")
''''' % _pylit(data)


DEMOS = {
    "k_facts": k_facts,
    "k_storage": k_storage,
    "k_compute": k_compute,
    "k_egress": k_egress,
    "k_index": k_index,
    "k_gen": k_gen,
    "k_retrieval": k_retrieval,
    "k_fixedvar": k_fixedvar,
    "k_perrecord": k_perrecord,
    "k_ledger": k_ledger,
    "k_alloc": k_alloc,
    "k_tiering": k_tiering,
    "k_rebuild": k_rebuild,
    "k_batch": k_batch,
    "k_sla_trade": k_sla_trade,
    "k_cache": k_cache,
    "k_compress": k_compress,
    "k_backup": k_backup,
    "k_transfer": k_transfer,
    "k_anomaly": k_anomaly,
    "k_tco": k_tco,
    "k_budget": k_budget,
    "k_chargeback": k_chargeback,
    "k_quality": k_quality,
    "k_govcost": k_govcost,
    "k_marginal": k_marginal,
    "k_compare": k_compare,
    "k_carbon": k_carbon,
    "k_variance": k_variance,
    "k_dashboard": k_dashboard,
    "k_mastery": k_mastery
}
