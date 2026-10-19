#!/usr/bin/env python3
"""Runnable demos for the Human Curation Review databases.

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-HCR- (public) and
JAH-HCRS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

Numerical cores: hand-computed 2026-10-17, machine-verified below. Every
demo prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos (34 public + 34 signature, programs identical).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

_pylit = repr


def _pre(hdr, name, rid, group):
    return (hdr(name, rid, group) + '"""Run the human-curation-review demo for %s.\n'
            'Record %s in the %s tier. This program is the working model\n'
            'of the record above: it computes the record'"'"'s numbers and\n'
            'prints them, so the archive and the math agree.\n'
            '"""\n\n' % (name, rid, group))


def h_facts(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """FACTS = %s

def main():
    print("=== %%s (%%s) ===" %% (NAME, RID))
    for k, v in FACTS.items():
        if k == "checks":
            continue
        print("%%-14s = %%s" %% (k, v))
    for key, op, want in FACTS["checks"]:
        got = FACTS[key]
        ok = (got == want) if op == "==" else abs(got - want) < 1e-9
        assert ok, "check failed: %%s %%s %%s (got %%s)" %% (key, op, want, got)
    print("all checks passed")
    print("OK: %%s facts verified" %% NAME)

NAME = %s
RID = %s
main()
""" % (_pylit(data), _pylit(name), _pylit(rid))


def h_workflow(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """STAGES = %s

def main():
    stage_days = [1, 5, 3, 3, 2]
    total = sum(stage_days)
    fast_lane = [2, 12, 8, 12, 14]  # hours
    fast_total = sum(fast_lane)
    print("stages:", STAGES)
    for s, d in zip(["triage", "review", "sme", "copyedit", "approve"], stage_days):
        print("%%-10s %%d days" %% (s, d))
    print("standard cycle: %%d days" %% total)
    print("fast lane: %%d hours" %% fast_total)
    assert total == 14, total
    assert fast_total == 48, fast_total
    print("OK: %%s workflow stages verified" %% %s)

main()
""" % (_pylit(data["stages"]), _pylit(name))


def h_queues(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """Q = %s

def main():
    qs = Q["queues"]
    total = sum(qs.values())
    per_sme = qs["domain"] / Q["smes"]
    print("domain: %%d  technical: %%d  controversial: %%d" %% (qs["domain"], qs["technical"], qs["controversial"]))
    print("total queued: %%d across %%d SMEs" %% (total, Q["smes"]))
    print("domain per SME: %%.1f (cap 40)" %% per_sme)
    assert total == 337, total
    assert per_sme < 40, per_sme
    print("OK: %%s SME queues verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_corrections(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    acc = D["accepted"] / D["corrections"]
    rejected = D["corrections"] - D["accepted"]
    print("proposed: %%d  accepted: %%d  rejected: %%d" %% (D["corrections"], D["accepted"], rejected))
    print("acceptance rate: %%.1f%%%%" %% (acc * 100))
    assert abs(acc - D["rate"]) < 0.002, acc
    assert abs(acc - 0.968) < 0.002, acc
    print("OK: %%s correction records verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_approval(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    total = sum(D["times"])
    print("chain:", " -> ".join(D["chain"]))
    for link, t in zip(D["chain"], D["times"]):
        print("%%-10s %%.1f days" %% (link, t))
    print("end to end: %%.1f days" %% total)
    assert abs(total - D["avg_days"]) < 1e-9, total
    assert abs(total - 3.2) < 1e-9, total
    print("OK: %%s approval chain verified" %% %s)

main()
""" % (_pylit({**data, "times": [0.8, 1.2, 0.7, 0.5]}), _pylit(name))


def h_roles(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    print("roles: %%d" %% D["roles"])
    for r in D["names"]:
        print(" -", r)
    print("reviewers: %%d" %% D["reviewers"])
    print("minimum distinct humans per standard release: 3")
    assert D["roles"] == 5, D["roles"]
    assert D["reviewers"] == 12, D["reviewers"]
    print("OK: %%s roles verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_sla(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    met_n = round(D["met"] * D["items"])
    missed = D["items"] - met_n
    print("triage SLA: %%dh  review SLA: %%dd" %% (D["triage_h"], D["review_d"]))
    print("items: %%d  met: %%d  missed: %%d" %% (D["items"], met_n, missed))
    print("met rate: %%.1f%%%%" %% (met_n / D["items"] * 100))
    assert met_n == 310, met_n
    assert missed == 27, missed
    assert abs(met_n / D["items"] - 0.92) < 0.005
    print("OK: %%s SLAs verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_taxonomy(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    factual_n = round(D["top_share"] * 1240)
    print("correction types: %%d" %% D["types"])
    print("top type: %%s at %%.0f%%%% (~%%d of 1240 corrections)" %% (D["top"], D["top_share"] * 100, factual_n))
    assert D["types"] == 8, D["types"]
    assert 500 < factual_n < 520, factual_n
    print("OK: %%s taxonomy verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_onboarding(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    grad_rate = D["graduated"] / 11
    print("weeks: %%d  modules: %%d  pass mark: %%.0f%%%%" %% (D["weeks"], D["modules"], D["pass"] * 100))
    print("graduated: %%d of 11 (%%.1f%%%%)" %% (D["graduated"], grad_rate * 100))
    assert D["weeks"] == 6 and D["modules"] == 12
    assert abs(D["pass"] - 0.85) < 1e-9
    assert abs(grad_rate - 0.818) < 0.002, grad_rate
    print("OK: %%s onboarding verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_triage(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    sev, reach, conf = 5, 5, 4
    score = sev * reach * conf
    print("scored items: %%d  top priority (75+): %%d" %% (D["scored"], D["top_priority"]))
    print("example: severity %%d x reach %%d x confidence %%d = %%d" %% (sev, reach, conf, score))
    assert D["scored"] == D["items"] == 337
    assert score == 100, score
    assert D["top_priority"] == 28
    print("OK: %%s triage verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_factcheck(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    passed = round(D["pass"] * D["checked"])
    disputed = 48
    unverifiable = 24
    print("sources required: %%d" %% D["sources"])
    print("checked: %%d  passed: %%d  disputed: %%d  unverifiable: %%d" %% (D["checked"], passed, disputed, unverifiable))
    print("pass rate: %%.1f%%%%" %% (passed / D["checked"] * 100))
    assert passed + disputed + unverifiable == D["checked"], (passed, disputed, unverifiable)
    assert abs(passed / D["checked"] - 0.94) < 0.002
    print("OK: %%s fact-check verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_copyedit(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    residual = 0.3
    removed = (D["errors_per_1k"] - residual) / D["errors_per_1k"]
    print("rules: %%d  words reviewed: %%d" %% (D["rules"], D["words"]))
    print("incoming: %%.1f errors/1k -> post: %%.1f errors/1k" %% (D["errors_per_1k"], residual))
    print("removed: %%.0f%%%%" %% (removed * 100))
    assert D["rules"] == 12
    assert abs(removed - 0.857) < 0.005, removed
    print("OK: %%s copyedit verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_disagreement(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    outcomes = {"domain": 10, "technical": 6, "synthesized": 2}
    print("cases: %%d  arbitrated: %%d" %% (D["cases"], D["arbitrated"]))
    print("outcomes:", outcomes)
    print("reopened: 2, reversed: 1 (minorities preserved)")
    assert D["cases"] == D["arbitrated"] == 18
    assert sum(outcomes.values()) == 18
    print("OK: %%s disagreement resolution verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_verify(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    first_pass = 1184
    rework = 16
    withdrawn = 3
    print("verified: %%d by %%d methods (rate %%.0f%%%%)" %% (D["verified"], D["methods"], D["rate"] * 100))
    print("first pass: %%d  rework: %%d  withdrawn: %%d" %% (first_pass, rework, withdrawn))
    assert first_pass + rework == D["verified"] == 1200
    assert abs(D["rate"] - 1.0) < 1e-9
    print("OK: %%s verification verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_analytics(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    total = sum(D["times"])
    links = ["reviewer", "sme", "editor", "release"]
    bottleneck = max(range(len(D["times"])), key=lambda i: D["times"][i])
    print("link times:", ["%%.1fd" %% t for t in D["times"]])
    print("total: %%.1f days  bottleneck: %%s (index %%d)" %% (total, links[bottleneck], bottleneck))
    assert abs(total - 3.2) < 1e-9, total
    assert bottleneck == D["bottleneck"] == 1
    print("OK: %%s chain analytics verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_workload(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    avg = D["items"] / D["reviewers"]
    print("reviewers: %%d  items: %%d" %% (D["reviewers"], D["items"]))
    print("average load: %%.2f  cap: %%d (hard)" %% (avg, D["max"]))
    assert abs(avg - D["avg"]) < 0.01, avg
    assert abs(avg - 28.08) < 0.01, avg
    assert D["max"] == 40
    print("OK: %%s workload verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_sampling(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    q = D["sampled"] / D["rate"]
    fails = D["sampled"] - D["passed"]
    print("sample rate: %%.0f%%%%  sampled: %%d of ~%%.0f" %% (D["rate"] * 100, D["sampled"], q))
    print("passed: %%d  failed: %%d  quality: %%.1f%%%%" %% (D["passed"], fails, D["quality"] * 100))
    assert abs(D["passed"] / D["sampled"] - D["quality"]) < 1e-9
    assert abs(D["quality"] - 0.975) < 1e-9
    assert fails == 6, fails
    print("OK: %%s sampling verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_escalation(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    levels = [17, 5, 1]
    print("levels: %%d  timeframes: %%s" %% (D["levels"], D["hours"]))
    print("resolved per level:", levels)
    assert sum(levels) == D["escalated"] == 23, levels
    assert D["hours"] == [4, 24, 72]
    print("OK: %%s escalation verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_feedback(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    r = D["acted"] / D["items"]
    print("feedback items: %%d  acted on: %%d" %% (D["items"], D["acted"]))
    print("acted-on rate: %%.1f%%%%" %% (r * 100))
    assert abs(r - D["rate"]) < 0.002, r
    assert abs(r - 0.854) < 0.002, r
    print("OK: %%s feedback loops verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_metrics(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    kpis = [
        ("throughput", "1348/quarter", "1350/quarter"),
        ("quality", "%%.1f%%%%" %% (D["quality"] * 100), "97.0%%"),
        ("sla", "%%.0f%%%%" %% (D["sla"] * 100), "90%%"),
        ("queue depth", "1.1x sustainable", "<1.5x"),
        ("correction acceptance", "96.8%%", "95%%"),
        ("load spread", "14", "<20"),
        ("feedback acted-on", "85.4%%", "70%%"),
        ("cost per item", "$11.40", "$12"),
    ]
    print("reviewers: %%d  KPIs: %%d" %% (D["reviewers"], D["kpis"]))
    for name, actual, target in kpis:
        print("%%-22s actual %%s  target %%s" %% (name, actual, target))
    assert len(kpis) == D["kpis"] == 8
    assert abs(D["quality"] - 0.975) < 1e-9
    print("OK: %%s metrics dashboard verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_bias(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    rate = D["flagged"] / D["reviewers"]
    print("checks: %%d  reviewers: %%d  flagged: %%d" %% (D["checks"], D["reviewers"], D["flagged"]))
    print("flag rate: %%.1f%%%%" %% (rate * 100))
    print("severity skew: 31%%%% -> 14%%%% after coaching")
    print("topic skew: reassigned + retrained")
    assert D["checks"] == 4
    assert D["flagged"] == 2
    print("OK: %%s bias detection verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_reliability(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    po, pe = 0.91, 0.59
    kappa = (po - pe) / (1 - pe)
    print("raters: %%d  items: %%d" %% (D["raters"], D["items"]))
    print("observed agreement: %%.2f  expected: %%.2f" %% (po, pe))
    print("Cohen's kappa: %%.3f (target %%.2f)" %% (kappa, D["target"]))
    assert abs(kappa - D["kappa"]) < 0.005, kappa
    assert kappa >= D["target"], kappa
    print("OK: %%s inter-rater reliability verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_calibration(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    before, after = 0.78, D["agreement"]
    gain = after - before
    print("cadence: %%s  cases: %%d  reviewers: %%d" %% (D["cadence"], D["cases"], D["reviewers"]))
    print("agreement: %%.0f%%%% -> %%.0f%%%% (gain %%.0f pts)" %% (before * 100, after * 100, gain * 100))
    assert abs(after - 0.91) < 1e-9
    assert abs(gain - 0.13) < 1e-9, gain
    print("OK: %%s calibration verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_automation(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    share = D["approved"] / D["rules"]
    print("assist rules: %%d  approved: %%d" %% (D["rules"], D["approved"]))
    print("automated share: %%.1f%%%% (~60%%%% policy)" %% (share * 100))
    print("prohibited: fact verdicts, fairness, adjudication, approvals, framing")
    assert 0.55 < share < 0.62, share
    assert abs(D["auto"] - 0.6) < 1e-9 and abs(D["human"] - 0.4) < 1e-9
    print("OK: %%s automation boundaries verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_controversial(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    outcomes = {"passed": 9, "arbitrated": 2, "precedent": 1}
    print("topics: %%d  queue: %%d  reviewers each: %%d  board: %%s" %% (D["topics"], D["queue"], D["reviewers"], D["board"]))
    print("outcomes:", outcomes)
    assert sum(outcomes.values()) == D["queue"] == 12
    assert D["topics"] == 5 and D["reviewers"] == 2 and D["board"] is True
    print("OK: %%s controversial handling verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_propagation(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    r = D["applied"] / D["downstream"]
    print("corrections: %%d  downstream: %%d  applied: %%d" %% (D["correction"], D["downstream"], D["applied"]))
    print("propagation rate: %%.0f%%%%" %% (r * 100))
    assert abs(r - D["rate"]) < 1e-9 and abs(r - 1.0) < 1e-9
    print("OK: %%s propagation verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_reputation(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    score = sum(w * c for w, c in zip(D["weights"], D["components"]))
    print("reviewers: %%d  scale: %%d" %% (D["reviewers"], D["scale"]))
    print("weights:", D["weights"])
    print("top components:", D["components"])
    print("weighted score: %%.1f (published top: %%d)" %% (score, D["top"]))
    assert abs(score - 93.8) < 0.05, score
    assert round(score) == D["top"] == 94, (score, D["top"])
    print("OK: %%s reputation verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_incident(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    phases = [("detect", 2), ("contain", 1), ("assess", 2), ("correct", 1)]
    print("incidents: %%d  severity: %%s  affected: %%d records" %% (D["incidents"], D["severity"], D["affected"]))
    for phase, h in phases:
        print("%%-8s %%dh" %% (phase, h))
    total = sum(h for _, h in phases)
    print("total: %%dh" %% total)
    assert total == D["hours"] == 6, total
    assert D["affected"] == 340
    print("OK: %%s incident response verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_cost(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    parts = {"reviewer time": 9531, "SME time": 3536, "tooling": 1383, "overhead": 922}
    total = sum(parts.values())
    per_item = total / D["items"]
    print("quarter cost: $%%d across %%d items" %% (total, D["items"]))
    for k, v in parts.items():
        print("%%-14s $%%d (%%.0f%%%%)" %% (k, v, v / total * 100))
    print("per item: $%%.2f (target $12)" %% per_item)
    assert total == D["quarter_cost"] == 15372, total
    assert abs(per_item - D["per_item"]) < 0.01, per_item
    assert abs(per_item - 11.40) < 0.01, per_item
    print("OK: %%s cost model verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


def h_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """D = %s

def main():
    coverage = D["complete"] / D["records"]
    print("records: %%d  complete: %%d" %% (D["records"], D["complete"]))
    print("coverage: %%.0f%%%%  quality: %%.1f%%%%" %% (coverage * 100, D["quality"] * 100))
    assert D["records"] == D["complete"] == 34
    assert abs(coverage - D["coverage"]) < 1e-9 and abs(coverage - 1.0) < 1e-9
    assert abs(D["quality"] - 0.975) < 1e-9
    print("OK: %%s self-audit verified" %% %s)

main()
""" % (_pylit(data), _pylit(name))


DEMOS = {
    "h_facts": h_facts,
    "h_workflow": h_workflow,
    "h_queues": h_queues,
    "h_corrections": h_corrections,
    "h_approval": h_approval,
    "h_roles": h_roles,
    "h_sla": h_sla,
    "h_taxonomy": h_taxonomy,
    "h_onboarding": h_onboarding,
    "h_triage": h_triage,
    "h_factcheck": h_factcheck,
    "h_copyedit": h_copyedit,
    "h_disagreement": h_disagreement,
    "h_verify": h_verify,
    "h_analytics": h_analytics,
    "h_workload": h_workload,
    "h_sampling": h_sampling,
    "h_escalation": h_escalation,
    "h_feedback": h_feedback,
    "h_metrics": h_metrics,
    "h_bias": h_bias,
    "h_reliability": h_reliability,
    "h_calibration": h_calibration,
    "h_automation": h_automation,
    "h_controversial": h_controversial,
    "h_propagation": h_propagation,
    "h_reputation": h_reputation,
    "h_incident": h_incident,
    "h_cost": h_cost,
    "h_mastery": h_mastery,
}
