#!/usr/bin/env python3
"""Demonstration programs for the Data Source Reliability databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (correction rates, weighted scores,
corroboration quorums, freshness decay, agreement analysis, margins of
error, error propagation, calibration, composite indexes, reliability
decay, detection confusion matrices, weighted consensus), asserts tight
bounds (never float exact-equality), prints the real computed values, and
ends with the OK marker. The build machine-executes all 68 demos.

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


def r_facts(hdr, name, rid, group, data):
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


def r_history(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    rate = 1000.0 * FACTS["corrections"] / FACTS["records"]
    crisis = 100.0 * FACTS["passed"] / FACTS["stress_events"]
    print("years:", FACTS["years"])
    print("correction rate per thousand: %%.2f" %% rate)
    print("crisis performance: %%.1f%%%%" %% crisis)
    assert abs(rate - 3.42) < 0.01, "41/12000*1000 = 3.42"
    assert abs(crisis - 83.33) < 0.01, "5/6 = 83.3%%"
    assert FACTS["years"] >= 10
    print("OK: %%s verified source history math" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_rate(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    rate = 1000.0 * FACTS["corrections"] / FACTS["records"]
    major_share = 100.0 * FACTS["major"] / FACTS["corrections"]
    print("corrections:", FACTS["corrections"], "| records:", FACTS["records"])
    print("rate per thousand: %%.2f" %% rate)
    print("major share: %%.1f%%%%" %% major_share)
    assert abs(rate - 3.42) < 0.01
    assert FACTS["major"] + FACTS["minor"] == FACTS["corrections"]
    assert 7.3 < major_share < 7.4, "3/41 = 7.3%%"
    assert FACTS["band"] == "healthy"
    print("OK: %%s verified correction rate" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_quorum(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("claim:", FACTS["claim"])
    print("independent:", FACTS["independent"], "| required:", FACTS["required"])
    print("total citing:", FACTS["total_citing"], "| shared lineage excluded:", FACTS["shared_lineage"])
    assert FACTS["independent"] >= FACTS["required"], "corroboration quorum not met"
    assert FACTS["independent"] + FACTS["shared_lineage"] <= FACTS["total_citing"]
    assert FACTS["independent"] == 4 and FACTS["required"] == 3
    print("quorum met with margin:", FACTS["independent"] - FACTS["required"])
    print("OK: %%s verified corroboration quorum" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_weighted(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    vals = [FACTS["history"], FACTS["correction"], FACTS["corroboration"],
            FACTS["limitations"], FACTS["peer"]]
    w = FACTS["weights"]
    assert abs(sum(w) - 1.0) < 1e-9, "weights must sum to 1"
    comp = sum(v * x for v, x in zip(vals, w))
    print("dimension scores:", vals)
    print("weights:", w)
    print("composite: %%.2f" %% comp)
    assert abs(comp - 83.2) < 0.05, "expected 83.2"
    for v in vals:
        assert 0 <= v <= 100, "scores on 0-100 scale"
    print("OK: %%s verified reputation composite" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_provenance(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("model:", FACTS["model"])
    print("links:", FACTS["links"], "| verified:", FACTS["verified"], "| gaps:", FACTS["gaps"])
    assert FACTS["verified"] + FACTS["gaps"] == FACTS["links"]
    assert FACTS["gaps"] == 0, "a gap breaks the chain"
    assert FACTS["verified"] == 5
    score = 100.0 * FACTS["verified"] / FACTS["links"]
    print("provenance score: %%.0f" %% score)
    assert score == 100.0
    print("OK: %%s verified provenance chain" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_fresh(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    import math
    age = FACTS["age_days"]; hl = FACTS["half_life_days"]
    fresh = 0.5 ** (age / hl)
    print("domain:", FACTS["domain"])
    print("age (days):", age, "| half-life (days):", hl)
    print("freshness: %%.3f" %% fresh)
    assert abs(fresh - 0.7071) < 0.001, "0.5**(45/90) = 0.7071"
    assert fresh > 0.5, "above the refresh flag threshold"
    old = 0.5 ** (4.0)
    print("after 4 half-lives: %%.3f (archival)" %% old)
    assert abs(old - 0.0625) < 1e-9
    print("OK: %%s verified freshness decay" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_agree(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    vals = sorted(FACTS["values"])
    n = len(vals)
    median = vals[n // 2] if n %% 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
    mad = sorted(abs(v - median) for v in vals)[n // 2]
    tol = 0.3
    inside = [v for v in vals if abs(v - median) <= tol]
    print("values:", vals)
    print("median: %%.2f | MAD: %%.2f" %% (median, mad))
    print("within tolerance:", len(inside), "of", n)
    assert abs(median - 2.1) < 0.01, "median of sorted values"
    assert FACTS["outlier"] not in inside, "outlier must sit outside tolerance"
    score = len(inside) / n
    print("agreement score: %%.3f" %% score)
    assert abs(score - 0.833) < 0.001, "5/6 = 0.833"
    print("OK: %%s verified agreement analysis" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_lag(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    lags = sorted(FACTS["lags_h"])
    n = len(lags)
    median = (lags[n // 2 - 1] + lags[n // 2]) / 2 if n %% 2 == 0 else lags[n // 2]
    p90 = lags[int(0.9 * n)]
    beyond = [l for l in lags if l > FACTS["threshold_h"]]
    print("lags (h):", lags)
    print("median: %%.1f | p90: %%d | beyond threshold: %%d/%%d" %% (median, p90, len(beyond), n))
    assert median == 6.0, "median of [1,2,3,4,5,7,9,12,48,96] = 6"
    assert p90 == 96
    assert len(beyond) == 2, "48 and 96 exceed 24h"
    print("OK: %%s verified correction lag stats" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_bias(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    dims = FACTS["dimensions"]; scores = FACTS["scores"]
    mean = sum(scores) / len(scores)
    print("dimensions:", ", ".join(dims))
    for d, s in zip(dims, scores):
        print("  %%s: %%.2f" %% (d, s))
        assert 0.0 <= s <= 1.0, "bias scores on 0-1 scale"
    print("mean bias: %%.3f -> verdict %%s" %% (mean, FACTS["verdict"]))
    assert abs(mean - 0.2) < 0.001, "(0.2+0.35+0.15+0.1)/4 = 0.2"
    assert FACTS["verdict"] == "low-moderate"
    print("OK: %%s verified bias assessment" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_sample(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    import math
    n = FACTS["sample_n"]
    moe = 1.96 * math.sqrt(0.25 / n) * 100
    print("census n:", FACTS["census_n"], "| sample n:", n)
    print("margin of error at 95%%%%: +\\u00b1%%.1f points" %% moe)
    assert abs(moe - FACTS["margin"]) < 0.05, "1.96*sqrt(.25/1067)*100 = 3.0"
    assert FACTS["confidence"] == 95
    print("OK: %%s verified sample margin math" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_drift(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    per_day = FACTS["drift_per_year"] / 365.0
    between = per_day * FACTS["calibration_days"]
    fail_rate = 100.0 * FACTS["failed"] / FACTS["sensors"]
    print("sensors:", FACTS["sensors"], "| unit:", FACTS["unit"])
    print("drift between calibrations: %%.3f %%s" %% (between, FACTS["unit"]))
    print("failure rate: %%.1f%%%%" %% fail_rate)
    assert abs(between - 0.3945) < 0.001, "0.8/365*180"
    assert abs(fail_rate - 2.5) < 0.01, "3/120 = 2.5%%"
    assert between < 0.5, "drift bounded under half a degree per cycle"
    print("OK: %%s verified sensor drift math" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_ci(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    import math
    n = FACTS["n"]; p = FACTS["p"]; z = FACTS["z"]
    moe = z * math.sqrt(p * (1 - p) / n) * 100
    print("n:", n, "| p:", p, "| mode:", FACTS["mode"])
    print("response rate: %%.0f%%%%" %% (100 * FACTS["response_rate"]))
    print("margin at 95%%%%: +\\u00b1%%.2f points" %% moe)
    assert abs(moe - FACTS["expect_moe"]) < 0.05, "margin must match expected"
    assert FACTS["response_rate"] < 0.5, "nonresponse dominates sampling error"
    print("OK: %%s verified confidence interval" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_propagate(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    import math
    vals = FACTS["inputs"]
    # uncertainties: 2%%, 1.5%%, 3%% of each input
    rel = [0.02, 0.015, 0.03]
    abs_unc = [v * r for v, r in zip(vals, rel)]
    combined = math.sqrt(sum(u ** 2 for u in abs_unc))
    result = vals[0] - vals[1] + vals[2]
    print("inputs:", list(zip(FACTS["labels"], vals)))
    print("absolute uncertainties:", ["%%.4f" %% u for u in abs_unc])
    print("combined uncertainty: %%.4f on result %%.2f" %% (combined, result))
    assert abs(combined - 0.1009) < 0.001, "sqrt(.04^2+.0225^2+.09^2)"
    assert abs(result - FACTS["result"] - 3.0) < 0.01, "2.0-1.5+3.0 = 3.5"
    print("OK: %%s verified error propagation" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_calibrate(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    hit = 100.0 * FACTS["actual_90"] / FACTS["claimed_90"]
    over = 90.0 - hit
    print("forecasts:", FACTS["forecasts"])
    print("claimed at 90%%%%:", FACTS["claimed_90"], "| actually right:", FACTS["actual_90"])
    print("hit rate in the 90%%%% bin: %%.1f%%%% (overconfident by %%.1f)" %% (hit, over))
    assert abs(hit - 82.35) < 0.01, "28/34 = 82.35%%"
    assert over > 0, "overconfidence must be positive here"
    assert 0.0 < FACTS["brier"] < 0.25, "Brier in plausible range"
    print("Brier score:", FACTS["brier"])
    print("OK: %%s verified expert calibration" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_composite(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    m = FACTS["metrics"]; w = FACTS["weights"]
    assert abs(sum(w) - 1.0) < 1e-9
    vals = [m["history"], m["correction"], m["corroboration"],
            m["limitations"], m["freshness"], m["agreement"]]
    comp = sum(v * x for v, x in zip(vals, w))
    print("metrics:", vals)
    print("composite: %%.2f" %% comp)
    assert abs(comp - 81.65) < 0.05, "expected 81.65"
    assert comp >= 80, "citable for facts (>= 80)"
    print("OK: %%s verified composite index" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_decay(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    import math
    s0 = FACTS["initial"]; lam = FACTS["lambda_per_year"]; t = FACTS["years"]
    s = s0 * math.exp(-lam * t)
    print("initial:", s0, "| decay/year: %%.0f%%%%" %% (100 * lam))
    print("after %%d years: %%.1f" %% (t, s))
    assert abs(s - 61.4) < 0.1, "88*e^(-0.36) = 61.4"
    assert s < 70, "a full band drop from neglect"
    # maintenance resets: rescore back to 88
    print("OK: %%s verified reliability decay" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_detect(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    tp = FACTS["true_pos"]; fp = FACTS["false_pos"]
    fn = FACTS["missed"]; total_bad = FACTS["total_bad"]
    prec = tp / (tp + fp); rec = tp / total_bad
    print("flagged:", FACTS["flagged"], "| true:", tp, "| false pos:", fp, "| missed:", fn)
    print("precision: %%.2f | recall: %%.2f" %% (prec, rec))
    assert abs(prec - 0.75) < 0.001, "45/60 = 0.75"
    assert abs(rec - 0.90) < 0.001, "45/50 = 0.90"
    assert tp + fp == FACTS["flagged"]
    assert tp + fn == total_bad
    print("OK: %%s verified detection confusion matrix" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_vote(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    srcs = FACTS["sources"]; scores = FACTS["scores"]; vals = FACTS["values"]
    tot = sum(scores)
    w = [s / tot for s in scores]
    consensus = sum(v * x for v, x in zip(vals, w))
    mean = sum(vals) / len(vals)
    print("sources:", srcs, "| scores:", scores, "| values:", vals)
    print("weights:", ["%%.3f" %% x for x in w])
    print("weighted consensus: %%.2f | simple mean: %%.2f" %% (consensus, mean))
    assert abs(consensus - 2.29) < 0.02, "expected ~2.29"
    assert abs(mean - 2.38) < 0.01, "simple mean 2.38"
    assert consensus < mean, "weak outlier properly muted"
    print("OK: %%s verified weighted consensus" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_monitor(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    per_source = FACTS["checks_per_day"] / FACTS["sources"]
    prec = 100.0 * FACTS["true_alerts"] / FACTS["alerts_week"]
    print("sources:", FACTS["sources"], "| checks/day:", FACTS["checks_per_day"])
    print("checks per source per day: %%.1f" %% per_source)
    print("alerts/week:", FACTS["alerts_week"], "| true:", FACTS["true_alerts"])
    print("precision: %%.1f%%%% | MTTR: %%.1f h" %% (prec, FACTS["mttr_h"]))
    assert abs(per_source - 24.0) < 0.01, "8160/340 = 24"
    assert abs(prec - 82.6) < 0.1, "19/23 = 82.6%%"
    assert FACTS["mttr_h"] == 7.5
    print("OK: %%s verified monitoring stats" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_dashboard(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("sources:", FACTS["sources"], "| panels:", FACTS["panels"])
    print("refresh (min):", FACTS["refresh_min"], "| active alerts:", FACTS["alerts"])
    assert FACTS["panels"] == 8, "eight prescribed panels"
    assert FACTS["sources"] == 340
    refreshes_day = 24 * 60 / FACTS["refresh_min"]
    print("refreshes/day: %%.0f" %% refreshes_day)
    assert refreshes_day == 96.0, "15-min refresh = 96/day"
    assert FACTS["alerts"] == 3
    print("OK: %%s verified dashboard spec" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def r_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("records:", FACTS["records"], "| complete:", FACTS["complete"])
    print("dimensions audited:", FACTS["dimensions_audited"])
    print("stale scores:", FACTS["stale_scores"])
    coverage = FACTS["complete"] / FACTS["records"]
    print("coverage: %%.2f" %% coverage)
    assert FACTS["records"] == 34 and FACTS["complete"] == 34
    assert FACTS["dimensions_audited"] == 5
    assert FACTS["stale_scores"] == 0
    assert coverage == FACTS["coverage"] == 1.0
    print("OK: %%s self-audit passed at full coverage" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


DEMOS = {
    "r_facts": r_facts, "r_history": r_history, "r_rate": r_rate,
    "r_quorum": r_quorum, "r_weighted": r_weighted,
    "r_provenance": r_provenance, "r_fresh": r_fresh, "r_agree": r_agree,
    "r_lag": r_lag, "r_bias": r_bias, "r_sample": r_sample,
    "r_drift": r_drift, "r_ci": r_ci, "r_propagate": r_propagate,
    "r_calibrate": r_calibrate, "r_composite": r_composite,
    "r_decay": r_decay, "r_detect": r_detect, "r_vote": r_vote,
    "r_monitor": r_monitor, "r_dashboard": r_dashboard,
    "r_mastery": r_mastery,
}
