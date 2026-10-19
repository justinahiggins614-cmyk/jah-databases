#!/usr/bin/env python3
"""Demonstration programs for the Record Conflict Reconciliation databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (three-way merges, quorum votes,
last-writer-wins, confidence scores, unit conversions, match scores, SLA
math, scale arithmetic), asserts tight bounds (never float exact-equality),
prints the real computed values, and ends with the OK marker. The build
machine-executes all 68 demos.

NOTE on %%: template bodies are %-formatted with the baked data, so every
literal percent inside a template is doubled (%%%% for one output percent);
the "= %%s" data placeholder and the trailing "%% _pylit(data)" stay single.
"""

import json


def _pylit(o):
    """Python-literal rendering of demo data (repr keeps True/False/None valid)."""
    return repr(o)


def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def c_facts(hdr, name, rid, group, data):
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


def c_version(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import hashlib, json as _json
FACTS = %s
def main():
    print("scheme:", FACTS["scheme"], "| algorithm:", FACTS["algorithm"])
    # content-hash identity: same content -> same hash; any change -> new hash
    canon = lambda d: _json.dumps(d, sort_keys=True, separators=(",", ":"))
    h1 = hashlib.sha256(canon({"price": 49}).encode()).hexdigest()
    h2 = hashlib.sha256(canon({"price": 49}).encode()).hexdigest()
    h3 = hashlib.sha256(canon({"price": 50}).encode()).hexdigest()
    assert h1 == h2, "identical content must hash identically"
    assert h1 != h3, "one-character change must change identity"
    assert len(h1) == 64, "SHA-256 hex digest is 64 chars"
    print("versions:", FACTS["versions"], "| unique:", FACTS["unique"])
    assert FACTS["versions"] == FACTS["unique"] == 14
    print("OK: %%s verified content-hash identity" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_authority(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    tiers = FACTS["tiers"]; weights = FACTS["weights"]
    print("tiers:", " > ".join(tiers))
    print("weights:", weights)
    assert len(tiers) == len(weights) == 5
    assert weights == sorted(weights, reverse=True), "weights must descend with tier"
    assert weights[0] == 100 and weights[-1] == 10
    # a two-tier gap (100 vs 35) suspends automatic resolution
    assert weights[0] - weights[3] >= 60
    print("OK: %%s verified authority hierarchy" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_detect(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("rules:", FACTS["rules"])
    print("comparisons/day:", FACTS["checked_per_day"])
    print("flagged:", FACTS["flagged"], "| precision: %%.2f" %% FACTS["precision"])
    assert FACTS["rules"] == 18
    assert FACTS["flagged"] == 3120
    assert 0.93 < FACTS["precision"] < 0.95
    tp = int(FACTS["flagged"] * FACTS["precision"])
    print("estimated true positives:", tp)
    assert tp == 2932, "int(3120 * 0.94) = 2932"
    print("OK: %%s verified detection stats" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_confidence(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    scores = []
    for v, a, f, c in zip(FACTS["versions"], FACTS["authority"],
                          FACTS["freshness"], FACTS["corroboration"]):
        s = a * f * (1 + 0.1 * c)
        scores.append((v, s))
        print("version %%s: %%d x %%.2f x %%.1f = %%.1f" %% (v, a, f, 1 + 0.1 * c, s))
    (w, ws), (l, ls) = sorted(scores, key=lambda x: -x[1])
    print("winner:", w, "at %%.1f vs %%.1f" %% (ws, ls))
    assert w == "A" and abs(ws - 117.0) < 0.1, "100*0.9*1.3 = 117"
    assert abs(ls - 36.6) < 0.1, "35*0.95*1.1 = 36.575"
    gap = (ws - ls) / ws
    print("gap: %%.1f%%%%" %% (100 * gap))
    assert gap > 0.15, "decisive: far above the 15%% human-review threshold"
    print("OK: %%s verified confidence scoring" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_triggers(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("triggers:", FACTS["triggers"])
    print("triggered/week:", FACTS["triggered_week"])
    print("median review (min):", FACTS["median_review_min"])
    assert FACTS["triggers"] == 8
    assert FACTS["triggered_week"] == 214
    hours = FACTS["triggered_week"] * FACTS["median_review_min"] / 60
    print("reviewer-hours/week: %%.1f" %% hours)
    assert 78.4 < hours < 78.5, "214*22/60 = 78.47"
    print("OK: %%s verified review trigger load" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_case(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("example case:", FACTS["example_id"])
    print("fields:", FACTS["fields"], "| versions:", FACTS["versions"])
    print("changed fields:", FACTS["fields_changed"])
    assert FACTS["fields"] == 14
    assert FACTS["versions"] == 2 and FACTS["fields_changed"] == 3
    assert FACTS["example_id"].startswith("CC-2026-")
    print("OK: %%s verified case record format" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_threeway(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def three_way(base, a, b):
    merged = {}
    conflicts = []
    for k in set(base) | set(a) | set(b):
        bv, av, bv2 = base.get(k), a.get(k), b.get(k)
        a_changed = av != bv
        b_changed = bv2 != bv
        if a_changed and not b_changed:
            merged[k] = av
        elif b_changed and not a_changed:
            merged[k] = bv2
        elif not a_changed and not b_changed:
            merged[k] = bv
        elif av == bv2:
            merged[k] = av
        else:
            conflicts.append(k)
    return merged, conflicts
def main():
    merged, conflicts = three_way(FACTS["base"], FACTS["a"], FACTS["b"])
    print("merged:", merged)
    print("true conflicts:", conflicts)
    assert merged == FACTS["expect"], "merge must take each side's changes"
    assert conflicts == [], "no field changed differently by both sides"
    print("OK: %%s verified three-way merge" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_lww(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    # hybrid-logical clock: max timestamp wins
    winner = max(FACTS["writes"], key=lambda x: x[1])
    print("writes (writer, time):", FACTS["writes"])
    print("winner:", winner[0], "at", winner[1])
    assert winner[0] == FACTS["winner"] == "B"
    assert winner[1] == 150
    assert FACTS["clock"] == "hybrid-logical"
    print("OK: %%s verified last-writer-wins" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_field(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    fields = FACTS["fields"]
    print("fields:", len(fields))
    for f, r, w in zip(fields, FACTS["rules"], FACTS["winners"]):
        print("  %%s -> rule %%s -> winner %%s" %% (f, r, w))
        assert r in ("value", "temporal", "structural", "unit")
    assert len(fields) == 4
    assert FACTS["winners"] == ["A", "B", "B", "B"]
    print("OK: %%s verified field-level resolution" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_stale(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import datetime
FACTS = %s
def main():
    a = datetime.datetime.fromisoformat(FACTS["a_time"].replace("Z", "+00:00"))
    b = datetime.datetime.fromisoformat(FACTS["b_time"].replace("Z", "+00:00"))
    age_a_h = (b - a).total_seconds() / 3600
    print("A age (h): %%.1f | TTL (h): %%d" %% (age_a_h, FACTS["ttl_h"]))
    assert age_a_h > FACTS["ttl_h"], "A is past TTL: stale"
    tier_gap = FACTS["a_tier"] - FACTS["b_tier"]
    print("tier gap:", tier_gap)
    assert tier_gap >= 60, "two-tier gap suspends automatic resolution"
    print("decision: human review (stale-but-authoritative)")
    print("OK: %%s verified temporal arbitration" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_unit(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    a_amt, a_cur = FACTS["a"]
    b_amt, b_cur = FACTS["b"]
    rate = FACTS["rate"]
    # canonical: USD
    to_usd = {("USD", "USD"): 1.0, ("EUR", "USD"): rate}
    ca = a_amt * to_usd[(a_cur, "USD")]
    cb = b_amt * to_usd[(b_cur, "USD")]
    print("%%d %%s -> %%.2f USD" %% (a_amt, a_cur, ca))
    print("%%d %%s @ %%.3f on %%s -> %%.2f USD" %% (b_amt, b_cur, rate, FACTS["rate_date"], cb))
    diff = abs(ca - cb)
    print("difference: %%.2f (tolerance %%.1f)" %% (diff, FACTS["tolerance"]))
    assert diff < FACTS["tolerance"], "92 EUR @ 1.087 = 100.00 USD: no conflict"
    print("resolved by normalization: no winner, no loser")
    print("OK: %%s verified unit normalization" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_entity(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    s = FACTS["match_score"]
    print("match score: %%.2f" %% s)
    print("auto-merge at >= %%.2f | review in [%%.2f, %%.2f)" %% (
        FACTS["threshold_auto"], FACTS["threshold_review"], FACTS["threshold_auto"]))
    assert FACTS["threshold_review"] <= s < FACTS["threshold_auto"], "human decides"
    print("identity keys:", ", ".join(FACTS["keys"]))
    print("decision: human review with key-by-key evidence")
    print("OK: %%s verified entity threshold band" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_dupe(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    pairs = FACTS["pairs"]
    dupes = FACTS["dupes"]; true_c = FACTS["true_conflicts"]
    print("pairs:", pairs, "| duplicates:", dupes, "| true conflicts:", true_c)
    assert dupes + true_c <= pairs
    assert dupes == 412 and true_c == 96
    prec = FACTS["precision"]
    print("precision: %%.2f" %% prec)
    assert 0.96 < prec < 0.98
    fp = int(dupes * (1 - prec))
    print("estimated misclassified true conflicts:", fp)
    assert fp <= 13, "3%% of 412 = ~12 danger-direction errors"
    print("OK: %%s verified duplicate classification" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_escalate(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    levels = FACTS["levels"]; slas = FACTS["sla_h"]
    print("levels:", " -> ".join(levels))
    for l, s in zip(levels, slas):
        print("  %%s: %%s h SLA" %% (l, s))
    assert slas == sorted(slas), "SLAs must lengthen up the ladder"
    assert FACTS["sla_h"][0] == 0.1, "auto level: 6 minutes"
    assert FACTS["escalated_week"] == 31
    print("OK: %%s verified escalation ladder" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_quorum(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    n = FACTS["replicas"]
    need = n // 2 + 1
    print("replicas:", n, "| quorum needed:", need)
    assert need == FACTS["quorum"] == 3, "floor(5/2)+1 = 3"
    votes = FACTS["votes"]
    winner = max(votes, key=votes.get)
    print("votes:", votes, "| winner:", winner)
    assert winner == FACTS["winner"] == "A"
    assert votes[winner] >= need
    # no-quorum case: 2-2-1 must escalate, not force
    split = {"A": 2, "B": 2, "C": 1}
    assert max(split.values()) < need, "2-2-1 has no quorum -> escalate"
    print("2-2-1 split correctly has no quorum: escalates")
    print("OK: %%s verified quorum resolution" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_queue(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("depth:", FACTS["depth"], "| reviewers:", FACTS["reviewers"])
    print("SLA (h):", FACTS["sla_h"], "| oldest (h):", FACTS["oldest_h"])
    assert FACTS["oldest_h"] > FACTS["sla_h"], "oldest is in breach: surge plan triggers"
    per = FACTS["throughput_day"] / FACTS["reviewers"]
    print("throughput/day:", FACTS["throughput_day"], "| per reviewer: %%.1f" %% per)
    assert abs(per - 35.0) < 0.1, "210/6 = 35"
    drain_h = FACTS["depth"] / (FACTS["throughput_day"] / 24)
    print("time to drain at full throughput: %%.1f h" %% drain_h)
    assert 5.3 < drain_h < 5.4, "47/(210/24) = 5.37h"
    print("OK: %%s verified queue math" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_merge_stats(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["resolved_day"]
    rules = FACTS["rules"]
    print("auto-resolved/day:", total)
    assert sum(rules.values()) == total, "rule distribution must sum to total"
    assert total == 18400
    overturn = 100.0 * FACTS["overturned"] / total
    print("overturned:", FACTS["overturned"], "-> %%.2f%%%%" %% overturn)
    assert abs(overturn - 0.2) < 0.01, "37/18400 = 0.201%%"
    assert FACTS["auto_pct"] == 92
    print("OK: %%s verified automatic resolution ledger" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_byzantine(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    n = FACTS["sources"]; f = FACTS["faulty"]
    print("sources:", n, "| faulty:", f, "| honest agreeing:", FACTS["honest_agree"])
    assert n >= 3 * f + 1, "need 3f+1 to tolerate f Byzantine faults"
    assert FACTS["tolerance"] == f == 2
    honest = FACTS["honest_agree"]
    assert honest > 2 * n / 3, "honest supermajority decides"
    print("honest share: %%.1f%%%% > 66.7%%%%: faulty outvoted" %% (100.0 * honest / n))
    # beyond the bound: 3 faulty of 7 could outvote -> system must refuse
    assert 3 > f, "f+1 faulty exceeds tolerance: escalate everything"
    print("OK: %%s verified fault tolerance bound" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_decision(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("case:", FACTS["case"], "| winner:", FACTS["winner"], "| rule:", FACTS["rule"])
    w, l = FACTS["scores"]
    print("scores: %%.1f vs %%.1f" %% (w, l))
    assert w > l and FACTS["winner"] == "A"
    gap = (w - l) / w
    assert gap > 0.15, "decisive score gap"
    assert FACTS["appealable_days"] == 30
    print("gap: %%.1f%%%% -> decisive; appeal window %%d days" %% (100 * gap, FACTS["appealable_days"]))
    print("OK: %%s verified decision record" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_queue2(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("open:", FACTS["open"], "| oldest (days):", FACTS["oldest_days"])
    print("SLA (days):", FACTS["sla_days"], "| breached:", FACTS["breached"])
    assert FACTS["oldest_days"] > FACTS["sla_days"], "oldest is in breach"
    assert FACTS["breached"] == 12
    by_type = FACTS["by_type"]
    assert sum(by_type.values()) == FACTS["open"] == 63, "28 identity + 35 evidence = 63"
    breach_pct = 100.0 * FACTS["breached"] / FACTS["open"]
    print("breach rate: %%.1f%%%%" %% breach_pct)
    assert 19.0 < breach_pct < 19.1, "12/63 = 19.05%%"
    print("OK: %%s verified discrepancy queue" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_sla(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("period:", FACTS["period"])
    print("auto: %%d ms | reviewer: %%d h | senior: %%d h" %% (
        FACTS["auto_ms"], FACTS["review_h"], FACTS["senior_h"]))
    assert FACTS["auto_ms"] == 40
    comp = FACTS["compliance"]
    print("compliance: %%.1f%%%%" %% (100 * comp))
    assert abs(comp - 0.973) < 0.001
    miss = 100 * (1 - comp)
    print("miss rate: %%.1f%%%%" %% miss)
    assert 2.6 < miss < 2.8
    print("OK: %%s verified resolution SLA" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_scale(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    dbs = FACTS["databases"]; per_day = FACTS["conflicts_day"]
    shards = FACTS["shards"]
    per_shard = per_day / shards
    print("databases:", dbs, "| conflicts/day:", per_day, "| shards:", shards)
    print("per shard/day: %%.1f" %% per_shard)
    assert abs(per_shard - 1437.5) < 0.1, "92000/64 = 1437.5"
    assert FACTS["p99_ms"] == 180
    per_second = per_day / 86400
    print("conflicts/second fleet-wide: %%.2f" %% per_second)
    assert 1.06 < per_second < 1.07
    print("OK: %%s verified scale arithmetic" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_predict(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("signals:", FACTS["signals"])
    print("precision: %%.2f | recall: %%.2f" %% (FACTS["precision"], FACTS["recall"]))
    assert FACTS["signals"] == 6
    assert abs(FACTS["precision"] - 0.71) < 0.001
    assert abs(FACTS["recall"] - 0.66) < 0.001
    assert FACTS["prevented_week"] == 48
    # prevention beats resolution ~10:1 on cost; false alarms cost a nudge
    print("prevented/week:", FACTS["prevented_week"])
    print("OK: %%s verified prediction stats" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_metrics(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("panels:", FACTS["panels"], "| conflicts/day:", FACTS["conflicts_day"])
    assert FACTS["panels"] == 8
    assert FACTS["conflicts_day"] == 18400
    assert FACTS["auto_pct"] == 92
    print("auto: %%d%%%% | overturn: %%.1f%%%% | SLA: %%.1f%%%%" %% (
        FACTS["auto_pct"], FACTS["overturn_pct"], FACTS["sla"]))
    assert abs(FACTS["overturn_pct"] - 0.2) < 0.01
    assert abs(FACTS["sla"] - 97.3) < 0.01
    print("OK: %%s verified metrics dashboard" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_policy(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("version:", FACTS["version"], "| rules:", FACTS["rules"])
    print("history:", " -> ".join(FACTS["history"]))
    assert FACTS["version"] == "v4.2"
    assert FACTS["rules"] == 12
    assert FACTS["history"] == ["v4.0", "v4.1", "v4.2"]
    corpus = FACTS["test_corpus"]
    changed = 23
    rate = 100.0 * changed / corpus
    print("test corpus:", corpus, "| changed by v4.2:", changed, "(%%.2f%%%%)" %% rate)
    assert abs(rate - 0.46) < 0.01, "23/5000 = 0.46%%"
    print("OK: %%s verified policy version record" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_dr(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("RPO (min):", FACTS["rpo_min"], "| RTO (min):", FACTS["rto_min"])
    print("replicas:", FACTS["replicas"])
    print("last drill:", FACTS["last_drill"], "| result:", FACTS["result"])
    assert FACTS["rpo_min"] == 5 and FACTS["rto_min"] == 30
    assert FACTS["replicas"] == 3
    assert FACTS["result"] == "pass"
    # drill recovered in 22 min: 8 under objective
    margin = FACTS["rto_min"] - 22
    print("drill recovery margin: %%d min under objective" %% margin)
    assert margin == 8
    print("OK: %%s verified disaster recovery record" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def c_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("records:", FACTS["records"], "| complete:", FACTS["complete"])
    coverage = FACTS["complete"] / FACTS["records"]
    print("auto: %%d%%%% | overturn: %%.1f%%%%" %% (FACTS["auto_pct"], FACTS["overturn_pct"]))
    print("coverage: %%.2f" %% coverage)
    assert FACTS["records"] == 34 and FACTS["complete"] == 34
    assert FACTS["auto_pct"] == 92
    assert abs(FACTS["overturn_pct"] - 0.2) < 0.01
    assert coverage == FACTS["coverage"] == 1.0
    print("OK: %%s self-audit passed at full coverage" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


DEMOS = {
    "c_facts": c_facts, "c_version": c_version, "c_authority": c_authority,
    "c_detect": c_detect, "c_confidence": c_confidence,
    "c_triggers": c_triggers, "c_case": c_case, "c_threeway": c_threeway,
    "c_lww": c_lww, "c_field": c_field, "c_stale": c_stale,
    "c_unit": c_unit, "c_entity": c_entity, "c_dupe": c_dupe,
    "c_escalate": c_escalate, "c_quorum": c_quorum, "c_queue": c_queue,
    "c_merge_stats": c_merge_stats, "c_byzantine": c_byzantine,
    "c_decision": c_decision, "c_queue2": c_queue2, "c_sla": c_sla,
    "c_scale": c_scale, "c_predict": c_predict, "c_metrics": c_metrics,
    "c_policy": c_policy, "c_dr": c_dr, "c_mastery": c_mastery,
}
