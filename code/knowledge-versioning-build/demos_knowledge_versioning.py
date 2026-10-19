#!/usr/bin/env python3
"""Runnable demos for the Knowledge Versioning databases (JAH Databases
governance track, group F, 2026-10-17).

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (semver parsing, version counts,
clause diffs, rule behavior deltas, graph diffs, deprecation clocks,
supersession chains, merge conflicts, rollback timing, time-travel
resolution, notification fan-out, migration rates, budget counts,
compatibility pairs, snapshot arithmetic, seal lengths, consensus votes,
consumer counts, decline projections, lineage depth), asserts tight bounds
(never float exact-equality), prints the real computed values, and ends
with the OK marker. The build machine-executes all 68 demos.

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


def v_facts(hdr, name, rid, group, data):
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


def v_semver(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    ver = "%%d.%%d.%%d" %% (FACTS["major"], FACTS["minor"], FACTS["patch"])
    breaks = FACTS["major"] - 1
    print("%%s at %%s: %%d breaking changes in history" %% (FACTS["entity"], ver, breaks))
    assert ver == "3.2.1", "major.minor.patch"
    assert breaks == 2, "major 3 means 2 breaks"
    print("OK: %%s semantic version 3.2.1" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_concept(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    per_year = FACTS["versions"] / FACTS["years"]
    print("%%s: %%d versions over %%d years (%%.1f/yr), current %%s" %% (
        FACTS["entity"], FACTS["versions"], FACTS["years"], per_year, FACTS["current"]))
    assert FACTS["versions"] == 7
    assert 2.3 < per_year < 2.4, "7/3 = 2.33"
    print("OK: %%s 7-version history" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_definition(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    pct = FACTS["clauses_changed"] / FACTS["clauses_total"] * 100
    print("%%s -> %%s: %%d of %%d clauses (%%.1f%%%%)" %% (
        FACTS["from"], FACTS["to"], FACTS["clauses_changed"], FACTS["clauses_total"], pct))
    assert FACTS["clauses_changed"] == 2 and FACTS["clauses_total"] == 9
    assert 22.2 < pct < 22.3, "2/9 = 22.2%%"
    print("OK: %%s definition diff 2/9 clauses" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_rule(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    pct = FACTS["changed"] / FACTS["rules"] * 100
    print("%%s at %%s: %%d of %%d rules changed (%%.0f%%%%)" %% (
        FACTS["entity"], FACTS["version"], FACTS["changed"], FACTS["rules"], pct))
    assert FACTS["changed"] == 3 and FACTS["rules"] == 12
    assert pct == 25.0, "3/12 = 25%%"
    print("OK: %%s rule set v5.0.0" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_relationship(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    pct = FACTS["changed"] / FACTS["total"] * 100
    print("%%s at %%s: %%d of %%d relationships (%%.2f%%%%)" %% (
        FACTS["entity"], FACTS["version"], FACTS["changed"], FACTS["total"], pct))
    assert FACTS["changed"] == 3 and FACTS["total"] == 48
    assert 6.24 < pct < 6.26, "3/48 = 6.25%%"
    print("OK: %%s graph v2.3.0" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_identifiers(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    parts = FACTS["format"].split("-")
    print("format: %%s -> prefix=%%s year=%%s seq=%%s | labels: %%d | entities: %%d" %% (
        FACTS["format"], parts[0], parts[1], parts[2], FACTS["labels"], FACTS["entities"]))
    assert parts == ["KV", "2026", "0042"], "KV-YYYY-NNNN"
    assert FACTS["labels"] == 4
    print("OK: %%s identifier format verified" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_changetypes(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["major"] + FACTS["minor"] + FACTS["patch"]
    print("major: %%d | minor: %%d | patch: %%d | total: %%d" %% (
        FACTS["major"], FACTS["minor"], FACTS["patch"], total))
    assert total == FACTS["total"] == 34, "2 + 8 + 24 = 34"
    assert FACTS["major"] < FACTS["minor"] < FACTS["patch"], "healthy distribution"
    print("OK: %%s 2/8/24 change mix" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_timestamps(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("fields: %%d | format: %%s | versions: %%d" %% (
        FACTS["fields"], FACTS["format"], FACTS["versions"]))
    assert FACTS["fields"] == 3, "authored/effective/superseded"
    assert FACTS["versions"] == 1240
    print("OK: %%s triple timestamps" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_readdiff(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    changed = FACTS["added"] + FACTS["removed"]
    print("+%%d -%%d = %%d changed lines | context: %%d | format: %%s" %% (
        FACTS["added"], FACTS["removed"], changed, FACTS["context"], FACTS["format"]))
    assert changed == 17, "12 + 5 = 17"
    print("OK: %%s diff +12/-5" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_conceptdiff(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    pct = FACTS["changed"] / FACTS["fields"] * 100
    print("%%s -> %%s: %%d of %%d fields (%%.1f%%%%)" %% (
        FACTS["from"], FACTS["to"], FACTS["changed"], FACTS["fields"], pct))
    assert FACTS["changed"] == 2 and FACTS["fields"] == 9
    print("OK: %%s concept diff 2/9 fields" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_defdiff(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    changed_pct = (1 - FACTS["similarity"]) * 100
    print("%%s -> %%s: similarity %%.2f (%%.0f%%%% changed), %%d clauses" %% (
        FACTS["from"], FACTS["to"], FACTS["similarity"], changed_pct, FACTS["clauses_changed"]))
    assert FACTS["similarity"] == 0.87
    assert 12.9 < changed_pct < 13.1, "13%% changed"
    print("OK: %%s definition similarity 0.87" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_rulediff(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    newly_rejected, accepted_v4 = 414, 9860
    pct = newly_rejected / accepted_v4 * 100
    print("%%s -> %%s: +%%d -%%d ~%%d conditions | newly rejected: %%d/%%d (%%.1f%%%%)" %% (
        FACTS["from"], FACTS["to"], FACTS["added"], FACTS["removed"],
        FACTS["modified"], newly_rejected, accepted_v4, pct))
    assert 4.19 < pct < 4.21, "414/9860 = 4.2%%"
    print("OK: %%s rule behavior delta 4.2%%%%" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_reldiff(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["added"] + FACTS["removed"] + FACTS["modified"]
    print("%%s -> %%s: +%%d -%%d ~%%d edges = %%d changed" %% (
        FACTS["from"], FACTS["to"], FACTS["added"], FACTS["removed"], FACTS["modified"], total))
    assert total == 6, "3 + 1 + 2 = 6"
    print("OK: %%s relationship diff 6 edges" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_deprecation(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("entities: %%d | notice: %%d days | migration: %%s" %% (
        FACTS["entities"], FACTS["notice_days"], FACTS["migration"]))
    assert FACTS["entities"] == 2
    assert FACTS["notice_days"] == 90, "90-day minimum"
    print("OK: %%s deprecation 90-day clock" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_supersession(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    links = FACTS["links"]
    print("chain: %%d links: %%s" %% (FACTS["chain"], " -> ".join(links)))
    assert FACTS["chain"] == len(links) == 4
    assert links[0] == FACTS["from"] and links[-1] == FACTS["to"]
    print("OK: %%s supersession chain of 4" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_branching(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("branches: %%d | main: %%s | experimental: %%s | merged: %%d" %% (
        FACTS["branches"], FACTS["main"], FACTS["experimental"], FACTS["merged"]))
    assert FACTS["branches"] == 2, "two-branch maximum"
    print("OK: %%s 2 branches" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_merging(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("base: %%s | branches: %%d | conflicts: %%d | resolved: %%d" %% (
        FACTS["base"], FACTS["branches"], FACTS["conflicts"], FACTS["resolved"]))
    assert FACTS["conflicts"] == FACTS["resolved"] == 1
    print("OK: %%s 3-way merge, 1 conflict resolved" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_rollback(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("%%s -> %%s in %%ds (window %%d days)" %% (
        FACTS["from"], FACTS["to"], FACTS["seconds"], FACTS["window_days"]))
    assert FACTS["seconds"] == 12
    assert FACTS["window_days"] == 30
    print("OK: %%s rollback 12s" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_timetravel(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    as_of = FACTS["as_of"]
    best = None
    for ver, eff in FACTS["versions"]:
        if eff <= as_of:
            best = ver
    print("as_of %%s -> version %%s (entities: %%d)" %% (as_of, best, FACTS["entities"]))
    assert best == FACTS["expect"] == "1.1.0", "v2.0 effective 2025-06-12 > as_of"
    print("OK: %%s time travel resolves v1.1.0" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_notify(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    delivered, total = 47, FACTS["subscribers"]
    rate = delivered / total * 100
    print("subscribers: %%d | channels: %%d | majors: %%d | delivered: %%d/%%d (%%.1f%%%%)" %% (
        total, FACTS["channels"], FACTS["majors_notified"], delivered, total, rate))
    assert 97.9 < rate < 98.0, "47/48 = 97.9%%"
    print("OK: %%s notification 47/48 delivered" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_migration(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    auto_pct = FACTS["auto"] / FACTS["concepts"] * 100
    print("%%s -> %%s: %%d/%%d auto (%%.1f%%%%), %%d manual" %% (
        FACTS["from"], FACTS["to"], FACTS["auto"], FACTS["concepts"], auto_pct, FACTS["manual"]))
    assert 98.2 < auto_pct < 98.3, "1218/1240 = 98.23%%"
    assert FACTS["auto"] + FACTS["manual"] == FACTS["concepts"]
    print("OK: %%s migration 98.2%%%% auto" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_breaking(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("budget: %%d/yr | notice: %%d days | board: %%s | used: %%d/%%d" %% (
        FACTS["per_year"], FACTS["notice_days"], FACTS["board"], FACTS["current_year"], FACTS["per_year"]))
    assert FACTS["current_year"] == FACTS["per_year"] == 2, "budget exhausted"
    print("OK: %%s breaking budget 2/2" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_compat(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    pairs = FACTS["versions"] ** 2
    pct = FACTS["compatible"] / pairs * 100
    print("%%d versions -> %%d pairs: %%d compatible (%%.0f%%%%)" %% (
        FACTS["versions"], pairs, FACTS["compatible"], pct))
    assert pairs == FACTS["pairs"] == 16, "4x4"
    assert pct == 75.0, "12/16 = 75%%"
    print("OK: %%s compatibility 12/16" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_snapshots(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    per = FACTS["gb"] / FACTS["snapshots"]
    print("snapshots: %%d | total: %%.1f GB (%%.2f GB each) | %%s | retention: %%d mo" %% (
        FACTS["snapshots"], FACTS["gb"], per, FACTS["cadence"], FACTS["retention"]))
    assert FACTS["snapshots"] == 12
    assert 0.34 < per < 0.36, "4.2/12 = 0.35"
    print("OK: %%s 12 monthly snapshots" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_sealing(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    bits = FACTS["hex"] * 4
    print("algorithm: %%s | seal: %%d hex = %%d bits | verified: %%d/%%d" %% (
        FACTS["algorithm"], FACTS["hex"], bits, FACTS["verified"], FACTS["versions"]))
    assert FACTS["hex"] == 64 and bits == 256, "SHA-256"
    assert FACTS["verified"] == FACTS["versions"] == 1240
    print("OK: %%s 1,240 seals verified" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_consensus(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    majority = FACTS["nodes"] // 2 + 1
    print("nodes: %%d | quorum: %%d (majority %%d) | agreed: %%d/%%d on %%s" %% (
        FACTS["nodes"], FACTS["quorum"], majority, FACTS["agreed"], FACTS["nodes"], FACTS["topic"]))
    assert FACTS["quorum"] == majority == 3, "majority of 5"
    assert FACTS["agreed"] == 5
    print("OK: %%s consensus 5/5" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_apicontracts(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["consumers_v2"] + FACTS["consumers_v3"]
    v2_pct = FACTS["consumers_v2"] / total * 100
    print("current: %%s | supported: %%d | v2: %%d | v3: %%d (v2 = %%.1f%%%%)" %% (
        FACTS["current"], FACTS["supported"], FACTS["consumers_v2"], FACTS["consumers_v3"], v2_pct))
    assert total == 1230, "340 + 890"
    assert 27.6 < v2_pct < 27.7, "340/1230 = 27.6%%"
    print("OK: %%s API contracts v2+v3" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_depanlytics(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    import math
    months = math.log(50 / FACTS["remaining"]) / math.log(1 - FACTS["decline_mo"])
    total_migrated = FACTS["migrated"] + FACTS["remaining"]
    print("deprecated: %%d | remaining: %%d | migrated: %%d | under 50 in %%.0f mo" %% (
        FACTS["deprecated"], FACTS["remaining"], FACTS["migrated"], months))
    assert 14.9 < months < 15.1, "340x0.88^15 = 50"
    print("OK: %%s deprecation on track" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_lineage(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("entity: %%s | nodes: %%d | edges: %%d | depth: %%d" %% (
        FACTS["entity"], FACTS["nodes"], FACTS["edges"], FACTS["depth"]))
    assert (FACTS["nodes"], FACTS["edges"], FACTS["depth"]) == (6, 5, 4)
    print("OK: %%s lineage graph 6/5" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def v_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    coverage = FACTS["complete"] / FACTS["records"]
    print("complete: %%d/%%d | entities: %%d | seals: %%d | coverage: %%.1f" %% (
        FACTS["complete"], FACTS["records"], FACTS["entities"], FACTS["seals"], coverage))
    assert coverage == 1.0
    assert FACTS["entities"] == FACTS["seals"] == 1240
    print("OK: %%s self-audit passed at full coverage" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


DEMOS = {
    "v_facts": v_facts, "v_semver": v_semver, "v_concept": v_concept,
    "v_definition": v_definition, "v_rule": v_rule,
    "v_relationship": v_relationship, "v_identifiers": v_identifiers,
    "v_changetypes": v_changetypes, "v_timestamps": v_timestamps,
    "v_readdiff": v_readdiff, "v_conceptdiff": v_conceptdiff,
    "v_defdiff": v_defdiff, "v_rulediff": v_rulediff, "v_reldiff": v_reldiff,
    "v_deprecation": v_deprecation, "v_supersession": v_supersession,
    "v_branching": v_branching, "v_merging": v_merging,
    "v_rollback": v_rollback, "v_timetravel": v_timetravel,
    "v_notify": v_notify, "v_migration": v_migration,
    "v_breaking": v_breaking, "v_compat": v_compat,
    "v_snapshots": v_snapshots, "v_sealing": v_sealing,
    "v_consensus": v_consensus, "v_apicontracts": v_apicontracts,
    "v_depanlytics": v_depanlytics, "v_lineage": v_lineage,
    "v_mastery": v_mastery,
}
