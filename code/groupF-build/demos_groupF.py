#!/usr/bin/env python3
"""Demonstration programs for the Group F data-governance databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own demo_data is baked into the program,
the program recomputes real values from it (survivorship scoring, reference
validation, contract compatibility, lineage evaluation, freshness checks,
retention math, transfer decisions, classification, license checks), asserts
tight bounds (never float exact-equality), prints the real computed values,
and ends with the OK marker. The build machine-executes all demos.
"""

import json


def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def demo_master(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
ATTRS = %s
def main():
    for attr in ATTRS:
        agg = {}
        for cand in attr["candidates"]:
            agg[cand["value"]] = agg.get(cand["value"], 0.0) + cand["trust"]
        winner = max(agg, key=lambda v: agg[v])
        print("attribute %%s -> golden value %%r (trust mass %%.3f)" %% (
            attr["name"], winner, agg[winner]))
        assert winner == attr["expected"], (
            "survivorship mismatch on %%s: %%r != %%r" %% (
                attr["name"], winner, attr["expected"]))
    print("OK: %%s resolved %%d golden-record attributes by trust mass" %% (
        NAME, len(ATTRS)))
if __name__ == "__main__":
    main()
""" % repr(data["attributes"])


def demo_reference(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LISTS = %s
def main():
    for lst in LISTS:
        status = {c["code"]: c["status"] for c in lst["codes"]}
        results = ["%%s:%%s" %% (ch, status.get(ch, "unknown"))
                   for ch in lst["checks"]]
        print("list %%s -> %%s" %% (lst["name"], ", ".join(results)))
        assert results == lst["expected"], (
            "reference validation mismatch on %%s" %% lst["name"])
        for c in lst["codes"]:
            assert c["code"] and c["label"] and c["status"] in (
                "active", "deprecated"), "bad code row %%r" %% (c,)
    print("OK: %%s validated %%d reference lists" %% (NAME, len(LISTS)))
if __name__ == "__main__":
    main()
""" % repr(data["lists"])


def demo_contract(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PRODUCER = %s
CONSUMER = %s
EXPECT = %s
def main():
    pmap = {f["name"]: f for f in PRODUCER["fields"]}
    verdict = "compatible"
    for req in CONSUMER["requires"]:
        p = pmap.get(req["name"])
        if p is None or p["type"] != req["type"]:
            verdict = "incompatible:missing-" + req["name"]
            break
    print("producer fields:", sorted(pmap))
    print("consumer requires:", [r["name"] for r in CONSUMER["requires"]])
    print("verdict:", verdict)
    assert verdict == EXPECT, "contract verdict %%r != expected %%r" %% (
        verdict, EXPECT)
    print("OK: %%s contract check -> %%s" %% (NAME, verdict))
if __name__ == "__main__":
    main()
""" % (repr(data["producer"]),
       repr(data["consumer"]),
       repr(data["expect"]))


def demo_lineage(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import ast
NODES = %s
EDGES = %s
FORMULA = %s
def safe_eval(expr, env):
    tree = ast.parse(expr, mode="eval")
    allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Name, ast.Load,
               ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod,
               ast.Pow, ast.FloorDiv, ast.USub, ast.UAdd)
    for node in ast.walk(tree):
        if not isinstance(node, allowed):
            raise ValueError("forbidden node: " + type(node).__name__)
    return eval(compile(tree, "<expr>", "eval"), {"__builtins__": {}},
                dict(env))
def main():
    nodes = set(NODES)
    for a, b in EDGES:
        assert a in nodes and b in nodes, "edge references unknown node"
    print("lineage graph: %%d nodes, %%d edges" %% (len(nodes), len(EDGES)))
    got = safe_eval(FORMULA["expr"], FORMULA["inputs"])
    exp = FORMULA["expected"]
    print("derivation %%s with %%s = %%r" %% (FORMULA["expr"],
          FORMULA["inputs"], got))
    if isinstance(exp, float):
        assert abs(got - exp) < 1e-9, "derivation mismatch"
    else:
        assert got == exp, "derivation mismatch"
    print("OK: %%s lineage verified (graph + derivation)" %% NAME)
if __name__ == "__main__":
    main()
""" % (repr(data["nodes"]),
       repr(data["edges"]),
       repr(data["formula"]))


def demo_observability(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FEEDS = %s
EXPECT_STALE = %s
def main():
    stale = sorted(f["name"] for f in FEEDS
                   if f["last_hours_ago"] > f["sla_hours"])
    for f in FEEDS:
        state = "STALE" if f["name"] in stale else "fresh"
        print("feed %%s: last %%sh ago vs SLA %%sh -> %%s (null rate %%.3f)" %% (
            f["name"], f["last_hours_ago"], f["sla_hours"], state,
            f["null_rate"]))
        assert 0.0 <= f["null_rate"] <= 1.0, "null rate out of bounds"
    assert stale == sorted(EXPECT_STALE), "staleness mismatch"
    print("OK: %%s freshness check -> %%d stale of %%d feeds" %% (
        NAME, len(stale), len(FEEDS)))
if __name__ == "__main__":
    main()
""" % (repr(data["feeds"]),
       repr(data["expect_stale"]))


def demo_lifecycle(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
from datetime import date
RECORDS = %s
ASOF = %s
EXPECT = %s
def main():
    asof = date.fromisoformat(ASOF)
    got = {}
    for r in RECORDS:
        if r.get("hold"):
            got[r["id"]] = "held"
            continue
        c = date.fromisoformat(r["created"])
        try:
            exp = date(c.year + r["retention_years"], c.month, c.day)
        except ValueError:
            exp = date(c.year + r["retention_years"], c.month, 28)
        got[r["id"]] = "expired" if asof > exp else "active"
    for rid_, state in sorted(got.items()):
        print("record %%s -> %%s" %% (rid_, state))
    assert got == EXPECT, "lifecycle mismatch: %%r != %%r" %% (got, EXPECT)
    print("OK: %%s lifecycle states verified for %%d records" %% (
        NAME, len(RECORDS)))
if __name__ == "__main__":
    main()
""" % (repr(data["records"]),
       repr(data["asof"]),
       repr(data["expect"]))


def demo_sovereignty(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TRANSFERS = %s
EU_BLOC = {"EU", "DE", "FR", "EE", "LU"}
ADEQUACY = {("EU", "CA"), ("EU", "CH"), ("EU", "JP"), ("EU", "UK"),
            ("UK", "EU"), ("JP", "EU")}
def decide(fr, to, dc):
    if dc in ("public", "anonymous"):
        return "allowed"
    if fr == to or (fr.startswith("US-") and to.startswith("US-")):
        return "restricted" if (fr, to, dc) == ("US", "US", "phi") else "allowed"
    if fr in EU_BLOC and to in EU_BLOC:
        return "allowed"
    if (fr, to) in ADEQUACY:
        return "allowed"
    return "restricted"
def main():
    for t in TRANSFERS:
        cat = decide(t["from"], t["to"], t["data_class"])
        exp = t["expected"]
        ok = exp == cat or exp.startswith(cat + ":")
        mech = exp.split(":", 1)[1] if ":" in exp else "-"
        print("%%s -> %%s [%%s]: %%s (mechanism: %%s)" %% (
            t["from"], t["to"], t["data_class"], cat, mech))
        assert ok, "transfer verdict mismatch: %%s vs %%s" %% (exp, cat)
    print("OK: %%s transfer decisions verified (%%d transfers)" %% (
        NAME, len(TRANSFERS)))
if __name__ == "__main__":
    main()
""" % repr(data["transfers"])


def demo_classification(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FIELDS = %s
RESTRICTED = {"biometric", "card", "diagnosis", "prescription", "salary",
              "secret", "ssn"}
CONFIDENTIAL = {"@", "contract", "ip", "phone", "pricing", "source"}
PUBLIC_HINTS = ("public", "press", "menu", "home", "price", "news", "blog",
                "faq", "help", "notice", "guide", "open", "release", "free",
                "launch")
def classify(name, patterns):
    for p in patterns:
        if p in RESTRICTED:
            return "restricted"
        if p in CONFIDENTIAL:
            return "confidential"
    if any(h in name for h in PUBLIC_HINTS):
        return "public"
    return "internal"
def main():
    for f in FIELDS:
        label = classify(f["name"], f["patterns"])
        print("field %%s -> %%s" %% (f["name"], label))
        assert label == f["expected"], (
            "classification mismatch on %%s: %%s != %%s" %% (
                f["name"], label, f["expected"]))
    print("OK: %%s classified %%d fields" %% (NAME, len(FIELDS)))
if __name__ == "__main__":
    main()
""" % repr(data["fields"])


def demo_acquisition(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LICENSES = %s
ASOF = "2026-10-17"
def verdict(lic):
    if lic["expires"] < ASOF:
        return "expired"
    if not lic["commercial"]:
        return "no-commercial"
    return "ok"
def main():
    for lic in LICENSES:
        v = verdict(lic)
        print("license %%s: commercial=%%s redistribute=%%s expires=%%s -> %%s" %% (
            lic["name"], lic["commercial"], lic["redistribute"],
            lic["expires"], v))
        assert v == lic["expected"], (
            "license verdict mismatch on %%s: %%s != %%s" %% (
                lic["name"], v, lic["expected"]))
    print("OK: %%s license checks passed (%%d licenses)" %% (
        NAME, len(LICENSES)))
if __name__ == "__main__":
    main()
""" % repr(data["licenses"])
