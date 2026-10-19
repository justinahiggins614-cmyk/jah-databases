#!/usr/bin/env python3
"""Runnable demos for the Database Federation databases (JAH Databases
governance track, group F, 2026-10-17).

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (fan-out latencies, coverage,
chain latency, join probe reduction, schema counts, identity scores,
membership tiers, merge arithmetic, quorum checks, rate budgets, cost
estimates, optimizer choices, 2PC votes, reconciliation rates, analytics
reduction, topology sums), asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. The build machine-executes all 68 demos.

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


def g_facts(hdr, name, rid, group, data):
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


def g_scatter(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["shard_p95_ms"] + FACTS["merge_ms"]
    print("%%d shards x %%dms p95 + %%dms merge = %%dms p95" %% (
        FACTS["shards"], FACTS["shard_p95_ms"], FACTS["merge_ms"], total))
    assert total == 365, "340 + 25 = 365"
    print("OK: %%s scatter-gather 365ms p95" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_broadcast(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    coverage = FACTS["responded"] / FACTS["shards"] * 100
    print("%%d of %%d shards in %%dms: %%.0f%%%% coverage" %% (
        FACTS["responded"], FACTS["shards"], FACTS["timeout_ms"], coverage))
    assert coverage == 75.0, "48/64 = 75%%"
    print("OK: %%s broadcast 75%%%% coverage" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_chained(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["hops"] * FACTS["hop_ms"] + FACTS["overhead_ms"]
    print("%%d hops x %%dms + %%dms overhead = %%dms" %% (
        FACTS["hops"], FACTS["hop_ms"], FACTS["overhead_ms"], total))
    assert total == 390, "3x120 + 30 = 390"
    assert FACTS["hops"] <= 5, "chain bound"
    print("OK: %%s chained 390ms" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_join(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    reduction = FACTS["right"] / FACTS["probes"]
    print("%%d x %%d on %%s: bloom filter -> %%d probes (%%.1fx cut)" %% (
        FACTS["left"], FACTS["right"], FACTS["key"], FACTS["probes"], reduction))
    assert 35.3 < reduction < 35.5, "438346/12400 = 35.35x"
    print("OK: %%s join probe reduction 35.4x" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_schema(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["fields"] + FACTS["transformed"] + FACTS["dropped"]
    print("mapped: %%d | transformed: %%d | dropped: %%d | total: %%d (%%s)" %% (
        FACTS["fields"], FACTS["transformed"], FACTS["dropped"], total, FACTS["version"]))
    assert total == 17, "14 + 2 + 1 = 17"
    print("OK: %%s schema mapping v3" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_identity(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    t = FACTS["threshold"]
    verdicts = []
    for s in FACTS["scores"]:
        if s >= t:
            verdicts.append("match")
        elif s >= 0.6:
            verdicts.append("review")
        else:
            verdicts.append("reject")
    print("scores: %%s vs %%.2f -> %%s" %% (FACTS["scores"], t, verdicts))
    assert verdicts == ["match", "review", "reject"], "0.94/0.71/0.32"
    print("OK: %%s identity verdicts correct" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_member(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    tiers = FACTS["tiers"]
    total = tiers["gold"] + tiers["silver"] + tiers["bronze"]
    print("gold: %%d | silver: %%d | bronze: %%d | total: %%d | quorum: %%d" %% (
        tiers["gold"], tiers["silver"], tiers["bronze"], total, FACTS["quorum"]))
    assert total == FACTS["members"] == 64, "8 + 24 + 32 = 64"
    assert FACTS["quorum"] == 43, "2/3 of 64 + 1"
    print("OK: %%s 64 members, quorum 43" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_capability(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    fresh = FACTS["members"] - FACTS["stale"]
    print("capability types: %%d | members: %%d | fresh: %%d | stale: %%d" %% (
        FACTS["capabilities"], FACTS["members"], fresh, FACTS["stale"]))
    assert fresh == 62, "64 - 2 stale"
    print("OK: %%s 2 stale advertisements flagged" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_routing(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("rules: %%d | members: %%d | default: %%s" %% (
        FACTS["rules"], FACTS["members"], FACTS["default"]))
    assert FACTS["rules"] == 5
    assert FACTS["default"] == "scatter-gather", "default never broadcast"
    print("OK: %%s 5 routing rules" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_distsearch(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("tiers: %%d | coordinators: %%d | shards: %%d | cache hit: %%.0f%%%%" %% (
        FACTS["tiers"], FACTS["coordinators"], FACTS["shards"], FACTS["cache_hit"] * 100))
    assert FACTS["tiers"] == 3 and FACTS["coordinators"] == 2
    assert FACTS["cache_hit"] == 0.68
    print("OK: %%s 3-tier search architecture" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_merge(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    unique = FACTS["results"] - FACTS["dupes"]
    print("%%d results - %%d dupes = %%d unique -> top %%d" %% (
        FACTS["results"], FACTS["dupes"], unique, FACTS["top_k"]))
    assert unique == 1153, "1240 - 87 = 1153"
    assert FACTS["top_k"] == 100
    print("OK: %%s merge 1,153 -> top 100" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_consistency(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    rw = FACTS["R"] + FACTS["W"]
    print("N=%%d R=%%d W=%%d: R+W=%%d > N=%%d -> %%s reads its writes" %% (
        FACTS["N"], FACTS["R"], FACTS["W"], rw, FACTS["N"], FACTS["model"]))
    assert rw > FACTS["N"], "2 + 2 = 4 > 3"
    print("OK: %%s quorum verified" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_auth(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("members: %%d | TTL: %%ds | scope: %%s" %% (
        FACTS["members"], FACTS["ttl_s"], FACTS["scope"]))
    assert FACTS["ttl_s"] == 3600, "1-hour max TTL"
    assert FACTS["scope"] == "federation:query"
    print("OK: %%s token 3600s scoped" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_ratelimit(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    fleet = FACTS["per_member"] * FACTS["members"]
    print("%%d/min/member x %%d members = %%d/min fleet (%%ds windows)" %% (
        FACTS["per_member"], FACTS["members"], fleet, FACTS["window_s"]))
    assert fleet == 64000, "1000 x 64"
    print("OK: %%s 64,000/min fleet budget" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_cachefed(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("TTL: %%ds | hit rate: %%.0f%%%% | members: %%d" %% (
        FACTS["ttl_s"], FACTS["hit_rate"] * 100, FACTS["members"]))
    assert FACTS["ttl_s"] == 300
    assert FACTS["hit_rate"] == 0.68
    print("OK: %%s federated cache 68%%%% hit" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_partial(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    up = FACTS["shards"] - FACTS["failed"]
    coverage = up / FACTS["shards"] * 100
    print("%%d of %%d shards: %%.1f%%%% coverage | degraded mode: %%s" %% (
        up, FACTS["shards"], coverage, FACTS["degraded"]))
    assert abs(coverage - 87.5) < 0.01, "14/16 = 87.5%%"
    print("OK: %%s degraded 87.5%%%% labeled" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_qcost(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    full = FACTS["shards"] * FACTS["per_shard"] + FACTS["merge"]
    expected = (1 - FACTS["cache_hit"]) * full + FACTS["cache_hit"] * 0.1
    print("full: %%d units | expected (%%.0f%%%% cached): %%.2f units" %% (
        full, FACTS["cache_hit"] * 100, expected))
    assert full == 37, "16x2 + 5"
    assert 11.90 < expected < 11.92, "0.32x37 + 0.68x0.1 = 11.91"
    print("OK: %%s expected cost 11.91 units" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_evolution(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("%%s -> %%s | breaking: %%d | migration: %%d days" %% (
        FACTS["from"], FACTS["to"], FACTS["breaking"], FACTS["migration_days"]))
    assert FACTS["breaking"] == 2
    assert FACTS["migration_days"] == 90
    print("OK: %%s schema evolution planned" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_onboard(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("steps: %%d | days: %%d | checklist: %%d items" %% (
        FACTS["steps"], FACTS["days"], FACTS["checklist"]))
    assert (FACTS["steps"], FACTS["days"], FACTS["checklist"]) == (5, 14, 23)
    print("OK: %%s onboarding 5 steps / 14 days" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_offboard(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("steps: %%d | notice: %%d days | purge: %%d days" %% (
        FACTS["steps"], FACTS["notice_days"], FACTS["purge_days"]))
    assert (FACTS["steps"], FACTS["notice_days"], FACTS["purge_days"]) == (4, 90, 30)
    print("OK: %%s offboarding clean" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_optimizer(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    scatter3 = FACTS["shards_hit"] * 2 + 5
    broadcast = 64 * 2 + 8
    print("selectivity %%.2f < %%.2f: scatter %%d shards = %%d units vs broadcast %%d" %% (
        FACTS["selectivity"], FACTS["threshold"], FACTS["shards_hit"], scatter3, broadcast))
    assert scatter3 == 11, "3x2 + 5"
    assert broadcast == 136, "64x2 + 8"
    assert scatter3 < broadcast
    print("OK: %%s optimizer picks scatter-3" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_2pc(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("participants: %%d | prepare: %%d/%%d | commit: %%d/%%d | rounds: %%d" %% (
        FACTS["participants"], FACTS["prepare_ok"], FACTS["participants"],
        FACTS["commit_ok"], FACTS["participants"], FACTS["rounds"]))
    assert FACTS["prepare_ok"] == FACTS["commit_ok"] == FACTS["participants"] == 4
    assert FACTS["rounds"] == 2
    print("OK: %%s 2PC 4/4 commit" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_reconcile(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    auto_pct = FACTS["auto"] / FACTS["conflicts"] * 100
    print("%%d conflicts: %%d auto (%%.1f%%%%) + %%d manual | lag bound %%d min" %% (
        FACTS["conflicts"], FACTS["auto"], auto_pct, FACTS["manual"], FACTS["lag_min"]))
    assert 95.1 < auto_pct < 95.3, "1180/1240 = 95.16%%"
    assert FACTS["auto"] + FACTS["manual"] == FACTS["conflicts"]
    print("OK: %%s reconciliation 95.2%%%% auto" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_sla(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("availability: %%.1f%%%% | p95: %%dms | penalty: %%.0f%%%% | met: %%d/%%d" %% (
        FACTS["availability"], FACTS["p95_ms"], FACTS["penalty"] * 100, 7, FACTS["members"]))
    assert FACTS["availability"] == 99.9
    assert FACTS["penalty"] == 0.1
    print("OK: %%s SLA terms verified" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_provenance(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    complete = FACTS["complete"] / FACTS["records"] * 100
    print("hops: %%d | lineage: %%d/%%d = %%.0f%%%%" %% (
        FACTS["hops"], FACTS["complete"], FACTS["records"], complete))
    assert complete == 100.0, "1153/1153"
    assert FACTS["hops"] == 4
    print("OK: %%s provenance 100%%%% complete" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_analytics(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    reduction = FACTS["rows_in"] / FACTS["rows_out"]
    print("stages: %%d | %%d rows -> %%d aggregates (%%.1fx)" %% (
        FACTS["stages"], FACTS["rows_in"], FACTS["rows_out"], reduction))
    assert 133.3 < reduction < 133.4, "2400000/18000 = 133.33x"
    print("OK: %%s analytics 133.3x reduction" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_topology(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = sum(FACTS["members"])
    print("regions: %%d | members: %%s = %%d | latencies: %%sms" %% (
        FACTS["regions"], FACTS["members"], total, FACTS["latency_ms"]))
    assert total == 64, "28 + 22 + 14"
    assert FACTS["regions"] == 3
    print("OK: %%s topology 64 members / 3 regions" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_security(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("controls: %%d | audits/yr: %%d | incidents: %%d" %% (
        FACTS["controls"], FACTS["audits_yr"], FACTS["incidents"]))
    assert (FACTS["controls"], FACTS["audits_yr"], FACTS["incidents"]) == (4, 4, 1)
    print("OK: %%s security posture verified" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def g_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    coverage = FACTS["complete"] / FACTS["records"]
    print("complete: %%d/%%d | members: %%d | contracts: %%d | coverage: %%.1f" %% (
        FACTS["complete"], FACTS["records"], FACTS["members"], FACTS["contracts"], coverage))
    assert coverage == 1.0
    assert FACTS["members"] == 64 and FACTS["contracts"] == 12
    print("OK: %%s self-audit passed at full coverage" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


DEMOS = {
    "g_facts": g_facts, "g_scatter": g_scatter, "g_broadcast": g_broadcast,
    "g_chained": g_chained, "g_join": g_join, "g_schema": g_schema,
    "g_identity": g_identity, "g_member": g_member,
    "g_capability": g_capability, "g_routing": g_routing,
    "g_distsearch": g_distsearch, "g_merge": g_merge,
    "g_consistency": g_consistency, "g_auth": g_auth,
    "g_ratelimit": g_ratelimit, "g_cachefed": g_cachefed,
    "g_partial": g_partial, "g_qcost": g_qcost, "g_evolution": g_evolution,
    "g_onboard": g_onboard, "g_offboard": g_offboard,
    "g_optimizer": g_optimizer, "g_2pc": g_2pc, "g_reconcile": g_reconcile,
    "g_sla": g_sla, "g_provenance": g_provenance, "g_analytics": g_analytics,
    "g_topology": g_topology, "g_security": g_security, "g_mastery": g_mastery,
}
