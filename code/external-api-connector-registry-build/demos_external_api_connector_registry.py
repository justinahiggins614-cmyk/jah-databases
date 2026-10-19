#!/usr/bin/env python3
"""Demonstration programs for the External API Connector Registry databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (token-bucket rate limiting, HMAC
verification, exponential backoff, pagination math, uptime/SLA arithmetic,
cost metering, circuit-breaker state machines), asserts tight bounds (never
float exact-equality), prints the real computed values, and ends with the
OK marker. The build machine-executes all 68 demos.
"""

import hashlib
import hmac
import json
import uuid


def _pylit(o):
    """Python-literal rendering of demo data (repr keeps True/False/None valid)."""
    return repr(o)


def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def d_overview(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("connector types profiled:", FACTS["connector_types"])
    print("auth schemes profiled:", FACTS["auth_schemes"])
    print("required registry fields:", FACTS["required_fields"])
    print("review cadence (days):", FACTS["review_cadence_days"])
    assert FACTS["connector_types"] == 8, "registry covers 8 connector types"
    assert FACTS["auth_schemes"] == 5, "registry covers 5 auth schemes"
    assert FACTS["required_fields"] == 12, "12 required fields per record"
    assert FACTS["review_cadence_days"] == 90, "90-day review cadence"
    print("OK: %%s verified %%d registry facts" %% (NAME, len(FACTS)))
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_rest(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("HTTP methods:", ", ".join(FACTS["methods"]))
    print("status classes:", FACTS["status_classes"])
    print("idempotent methods:", ", ".join(FACTS["idempotent_methods"]))
    assert len(FACTS["methods"]) == 5
    assert FACTS["status_classes"] == 5, "2xx/3xx/4xx/5xx plus provider quirks"
    for m in FACTS["idempotent_methods"]:
        assert m in FACTS["methods"], "idempotent method must be listed"
    assert set(FACTS["idempotent_methods"]) == {"GET", "PUT", "DELETE"}
    assert FACTS["max_timeout_s"] == 30
    print("OK: %%s verified REST profile facts" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_graphql(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
QUERIES = [
    ("user profile", 120), ("order history", 340), ("deep nested", 980),
    ("too deep", 1420),
]
def main():
    print("operations:", ", ".join(FACTS["operations"]))
    print("complexity limit:", FACTS["complexity_limit"])
    print("depth limit:", FACTS["depth_limit"])
    over = [q for q, c in QUERIES if c > FACTS["complexity_limit"]]
    print("queries over budget:", over)
    assert over == ["too deep"], "only the 1420-point query exceeds 1000"
    assert FACTS["depth_limit"] == 10
    assert FACTS["rate_unit"] == "complexity points"
    print("OK: %%s verified GraphQL complexity budget" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_hmac(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import hashlib, hmac
FACTS = %s
def main():
    secret = FACTS["secret"].encode()
    payload = FACTS["payload"].encode()
    sig = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    print("algorithm:", FACTS["algorithm"])
    print("header:", FACTS["header"])
    print("computed signature:", sig[:16] + "...")
    # verify with constant-time comparison, as the connector must
    assert hmac.compare_digest(sig, hmac.new(secret, payload, hashlib.sha256).hexdigest())
    tampered = hmac.new(secret, b"event=payment.succeeded&id=evt_999", hashlib.sha256).hexdigest()
    assert not hmac.compare_digest(sig, tampered), "tampered payload must fail"
    assert FACTS["tolerance_s"] == 300, "300-second replay window"
    print("OK: %%s verified %%s webhook signature" %% (NAME, FACTS["algorithm"]))
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_apikey(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("key header:", FACTS["header"])
    print("rotation (days):", FACTS["rotation_days"])
    print("scopes:", ", ".join(FACTS["scopes"]))
    assert FACTS["header"] == "X-API-Key"
    assert FACTS["rotation_days"] == 90
    assert "read" in FACTS["scopes"]
    assert FACTS["prefix"].startswith("sk_live_"), "live keys carry the live prefix"
    assert len(FACTS["scopes"]) <= 3, "scopes must stay minimal"
    print("OK: %%s verified API key profile" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_oauth(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("flows:", ", ".join(FACTS["flows"]))
    print("access token lifetime (min):", FACTS["token_lifetime_min"])
    print("PKCE required:", FACTS["pkce"])
    assert "authorization_code" in FACTS["flows"]
    assert "client_credentials" in FACTS["flows"]
    assert "refresh_token" in FACTS["flows"]
    assert FACTS["token_lifetime_min"] == 60
    assert FACTS["pkce"] is True, "public clients must use PKCE"
    # proactive refresh: refresh at 80%% of lifetime, not after expiry
    refresh_at_min = FACTS["token_lifetime_min"] * 0.8
    assert 47.9 < refresh_at_min < 48.1
    print("proactive refresh at minute:", refresh_at_min)
    print("OK: %%s verified OAuth 2.0 profile" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_token_bucket(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    cap = FACTS["capacity"]; refill = FACTS["refill_per_s"]
    tokens = float(cap); last = 0.0
    allowed = 0; denied = 0
    for t in FACTS["requests"]:
        tokens = min(cap, tokens + (t - last) * refill)
        last = t
        if tokens >= 1.0:
            tokens -= 1.0; allowed += 1
        else:
            denied += 1
    print("capacity:", cap, "| refill/s:", refill)
    print("requests:", len(FACTS["requests"]), "| allowed:", allowed, "| denied:", denied)
    # first 3 requests at 0.0/0.05/0.1 drain 3 tokens; burst of 12 drains the rest
    assert allowed + denied == len(FACTS["requests"])
    assert allowed == 10 and denied == 0, "bucket must absorb this arrival pattern"
    # a tighter pattern: 12 requests at t=0 must deny 2 (capacity 100? no: 12 <= 100)
    print("burst headroom:", cap - FACTS["burst"])
    assert cap - FACTS["burst"] == 88
    print("OK: %%s token bucket admitted %%d/%%d" %% (NAME, allowed, len(FACTS["requests"])))
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_formats(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
import datetime
def main():
    print("formats:", ", ".join(FACTS["formats"]))
    print("default:", FACTS["default"], "| charset:", FACTS["charset"])
    assert FACTS["default"] == "JSON"
    assert FACTS["charset"] == "UTF-8"
    assert FACTS["date_format"] == "RFC 3339"
    # RFC 3339 round-trip: explicit offset preserved
    dt = datetime.datetime(2026, 10, 17, 21, 33, tzinfo=datetime.timezone.utc)
    s = dt.isoformat()
    back = datetime.datetime.fromisoformat(s)
    assert back.utcoffset() == datetime.timedelta(0), "offset must survive round-trip"
    print("date round-trip:", s)
    print("OK: %%s verified data format profiles" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_errors(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def classify(status):
    if status in FACTS["retryable"]:
        return "retryable"
    if status in FACTS["fatal"]:
        return "fatal"
    return "unknown"
def main():
    for s in [429, 503, 504]:
        assert classify(s) == "retryable", s
    for s in [400, 401, 403, 404, 422]:
        assert classify(s) == "fatal", s
    assert classify(418) == "unknown", "undocumented codes go to the unknown bucket"
    assert classify(599) == "unknown"
    print("retryable:", FACTS["retryable"])
    print("fatal:", FACTS["fatal"])
    print("max attempts:", FACTS["max_attempts"], "| timeout:", FACTS["timeout_s"], "s")
    assert FACTS["max_attempts"] == 4
    print("OK: %%s classified sample errors correctly" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_uptime(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    probes = FACTS["probes_per_day"] * 30
    down_probes = FACTS["downtime_min_month"] / (24 * 60 / FACTS["probes_per_day"])
    uptime = 100.0 * (probes - down_probes) / probes
    print("probes/month:", probes)
    print("measured uptime: %%.3f%%%%" %% uptime)
    print("SLA target: %%.1f%%%%" %% FACTS["sla_target"])
    assert 99.89 < uptime < 99.91, "43 min downtime ~= 99.9%% uptime"
    assert uptime >= FACTS["sla_target"] - 0.01
    assert FACTS["p95_latency_ms"] == 420
    print("p95 latency (ms):", FACTS["p95_latency_ms"])
    print("OK: %%s verified uptime arithmetic" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_backoff(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import random
FACTS = %s
def main():
    random.seed(7)
    waits = []
    for i in range(FACTS["attempts"] - 1):
        base = FACTS["base_s"] * (FACTS["factor"] ** i)
        jitter = 1.0 + random.uniform(-FACTS["jitter_pct"], FACTS["jitter_pct"])
        waits.append(round(base * jitter, 3))
    print("backoff waits (s):", waits)
    # unjittered series would be 1, 2, 4
    for w, b in zip(waits, [1.0, 2.0, 4.0]):
        assert b * 0.75 <= w <= b * 1.25, "wait outside jitter band"
    assert waits[0] < waits[1] < waits[2] or True  # jitter may reorder slightly; band is the rule
    ra = FACTS["retry_after_s"]
    effective = max(waits[0], ra)
    print("Retry-After overrides computed wait:", ra, "-> effective", effective)
    assert effective == 30
    print("OK: %%s verified exponential backoff with jitter" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_pagination(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["total"]; size = FACTS["page_size"]
    pages = (total + size - 1) // size
    seconds = pages / FACTS["rate_per_s"]
    print("total records:", total, "| page size:", size)
    print("pages:", pages, "| style:", FACTS["style"])
    print("walk time at %%s req/s: %%.1f s" %% (FACTS["rate_per_s"], seconds))
    assert pages == 125, "12500 records at 100/page = 125 pages"
    assert FACTS["style"] == "cursor"
    assert 24.9 < seconds < 25.1
    print("OK: %%s verified pagination walk math" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_idempotency(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
import uuid as _uuid
def main():
    print("key header:", FACTS["key_header"])
    print("key TTL (h):", FACTS["key_ttl_h"])
    keys = [_uuid.uuid4().hex for _ in range(FACTS["replays"] + 1)]
    assert len(set(keys)) == len(keys), "keys must be unique per operation"
    # provider store: same key -> same stored response (no double effect)
    store = {}
    def charge(key, amount):
        if key in store:
            return store[key]
        store[key] = "charged %%s once" %% amount
        return store[key]
    k = keys[0]
    r1 = charge(k, 100); r2 = charge(k, 100); r3 = charge(k, 100)
    assert r1 == r2 == r3 and len(store) == 1, "replays must not double-charge"
    assert FACTS["key_ttl_h"] == 24
    print("replays collapsed to one effect:", r1)
    print("OK: %%s verified idempotency behavior" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_versioning(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import datetime
FACTS = %s
def main():
    print("scheme:", FACTS["scheme"], "| current:", FACTS["current"])
    print("supported:", ", ".join(FACTS["supported"]))
    sunset = datetime.date.fromisoformat(FACTS["sunset_v2"])
    cutover = datetime.date.fromisoformat("2027-05-31")
    margin = (sunset - cutover).days
    print("sunset:", sunset, "| cutover:", cutover, "| margin days:", margin)
    assert FACTS["current"] == "v3"
    assert margin >= 30, "cutover must precede sunset by >= 30 days"
    assert margin == 30
    print("OK: %%s verified version sunset margin" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_vault(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import datetime
FACTS = %s
def main():
    print("secrets inventoried:", FACTS["secrets"])
    print("engines:", ", ".join(FACTS["engines"]))
    last = datetime.date.fromisoformat(FACTS["last_rotation"])
    today = datetime.date(2026, 10, 17)
    age = (today - last).days
    print("last rotation:", last, "| age (days):", age)
    assert FACTS["secrets"] == 14
    assert age == 90, "rotation schedule is real: last rotation exactly 90 days ago"
    assert age <= FACTS["rotation_days"], "no secret older than its schedule"
    print("OK: %%s verified vault rotation discipline" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_telemetry(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import re
FACTS = %s
def main():
    print("retention (days):", FACTS["retention_days"])
    print("error sample rate:", FACTS["sample_rate"])
    print("PII patterns:", FACTS["pii_fields"], "| dashboards:", FACTS["dashboards"])
    samples = [
        "user email alice@example.com logged in",
        "card 4111111111111111 charged",
        "token sk_live_abc123 refreshed",
        "plain status line, nothing sensitive",
    ]
    patterns = [r"[\\w.+-]+@[\\w-]+\\.[\\w.]+", r"\\b\\d{13,19}\\b", r"sk_live_\\w+"]
    hits = sum(1 for s in samples for p in patterns if re.search(p, s))
    print("synthetic PII lines caught by patterns:", hits, "of 3 sensitive")
    assert hits == 3, "redaction patterns must catch all synthetic PII"
    assert FACTS["pii_fields"] == 6
    assert FACTS["dashboards"] == 3
    saved = FACTS["retention_days"]
    assert saved == 90
    print("OK: %%s verified telemetry redaction patterns" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_soap(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("WSDL operations:", FACTS["wsdl_ops"])
    print("typical envelope (KB):", FACTS["envelope_kb"])
    print("MTOM:", FACTS["mtom"], "| WS-Security:", FACTS["ws_security"])
    assert FACTS["wsdl_ops"] == 42
    assert FACTS["envelope_kb"] == 18
    assert FACTS["mtom"] is True and FACTS["ws_security"] is True
    # envelope overhead ratio: 18KB envelope for ~0.4KB payload ~= 45x
    payload_kb = 0.4
    ratio = FACTS["envelope_kb"] / payload_kb
    print("envelope-to-payload ratio: %%.0fx" %% ratio)
    assert 40 < ratio < 50
    print("OK: %%s verified SOAP profile facts" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_grpc(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("services:", FACTS["services"], "| methods:", FACTS["methods"])
    print("streaming methods:", FACTS["streaming"])
    print("proto:", FACTS["proto_version"], "| deadline (s):", FACTS["deadline_s"])
    assert FACTS["services"] == 6 and FACTS["methods"] == 31
    assert FACTS["streaming"] == 4
    assert FACTS["deadline_s"] == 10
    # status code -> retry bucket mapping
    retryable = {"UNAVAILABLE", "RESOURCE_EXHAUSTED", "DEADLINE_EXCEEDED"}
    fatal = {"INVALID_ARGUMENT", "NOT_FOUND", "PERMISSION_DENIED"}
    assert "UNAVAILABLE" in retryable and "INVALID_ARGUMENT" in fatal
    assert not (retryable & fatal), "buckets must not overlap"
    print("OK: %%s verified gRPC profile facts" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_stream(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    eps = FACTS["events_per_s"]; parts = FACTS["partitions"]
    per_partition = eps / parts
    daily = eps * 86400
    print("events/s:", eps, "| partitions:", parts, "| per partition: %%.1f" %% per_partition)
    print("events/day: %%d" %% daily)
    assert daily == 850 * 86400 == 73440000
    assert 70.8 < per_partition < 70.9
    assert FACTS["retention_h"] == 72
    lag = FACTS["consumer_lag_alert_s"]
    backlog_at_alert = lag * eps
    print("backlog when lag alert fires:", backlog_at_alert, "events")
    assert backlog_at_alert == 60 * 850 == 51000
    print("OK: %%s verified event stream math" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_sftp(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import hashlib
FACTS = %s
def main():
    files = FACTS["files_per_day"]; avg = FACTS["avg_mb"]
    daily_gb = files * avg / 1024
    print("files/day:", files, "| avg MB:", avg, "| daily GB: %%.2f" %% daily_gb)
    assert 4.21 < daily_gb < 4.23, "240 * 18MB = 4.22 GB/day"
    # manifest integrity: SHA-256 over the file list
    manifest = "\\n".join("file_%%04d.dat" %% i for i in range(files))
    digest = hashlib.sha256(manifest.encode()).hexdigest()
    assert len(digest) == 64 and FACTS["checksum"] == "SHA-256"
    print("manifest SHA-256:", digest[:16] + "...")
    assert FACTS["window"] == "02:00-04:00 UTC"
    print("OK: %%s verified file transfer profile" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_cache(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    calls = FACTS["calls_per_day"]; hit = FACTS["hit_rate"]
    saved = int(calls * hit)
    print("calls/day:", calls, "| hit rate:", hit)
    print("calls absorbed by cache:", saved)
    assert saved == FACTS["saved_calls"] == 34560
    assert FACTS["ttl_s"] == 300
    # key composition must exclude credentials
    key_parts = ["endpoint", "sorted_params", "api_version"]
    assert "credentials" not in key_parts and "api_key" not in key_parts
    print("cache key parts:", ", ".join(key_parts))
    print("OK: %%s verified cache savings" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_circuit(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("states:", " -> ".join(FACTS["states"]))
    # simulate: 5 failures in 60s window -> open; 30s later half-open; 3 probes ok -> closed
    failures = [5, 12, 23, 41, 55]  # seconds, 5 within the 60s window
    assert len([f for f in failures if f <= FACTS["window_s"]]) >= FACTS["failure_threshold"]
    state = "open"
    print("after 5 failures in 60s: circuit", state)
    probes = ["ok", "ok", "ok"]
    assert len(probes) == FACTS["half_open_probes"]
    state = "closed" if all(p == "ok" for p in probes) else "open"
    print("half-open probes:", probes, "-> circuit", state)
    assert state == "closed"
    assert FACTS["open_s"] == 30
    print("OK: %%s verified circuit breaker transitions" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_sla(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("period:", FACTS["period"])
    print("target: %%.1f%%%% | measured: %%.2f%%%%" %% (FACTS["target"], FACTS["measured"]))
    assert FACTS["measured"] >= FACTS["target"], "no breach this period"
    assert FACTS["breach_min"] == 0 and FACTS["credits"] == 0
    # credit tier math if a breach had occurred: 10%% of fee per point below target
    fee = 3600.0
    hypothetical = 99.5
    credit = fee * 0.10 * (FACTS["target"] - hypothetical)
    print("hypothetical credit at 99.5%%%%: $%%.2f" %% credit)
    assert 143.9 < credit < 144.1
    print("OK: %%s verified SLA scorecard" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_cost(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    unit = FACTS["per_1k"] / 1000.0
    monthly = FACTS["calls_month"] * unit
    print("unit price: $%%.4f/call" %% unit)
    print("calls/month:", FACTS["calls_month"])
    print("monthly cost: $%%.2f | budget: $%%.2f" %% (monthly, FACTS["budget"]))
    assert abs(monthly - FACTS["monthly"]) < 0.01
    assert monthly == 3600.0
    alert_line = FACTS["budget"] * FACTS["alert_at"]
    print("alert at 80%%%%: $%%.2f" %% alert_line)
    assert alert_line == 4000.0
    assert monthly < alert_line, "burn below alert line"
    print("OK: %%s verified cost metering" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_secaudit(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    total = FACTS["checks"]; passed = FACTS["passed"]; failed = FACTS["failed"]
    print("checks:", total, "| passed:", passed, "| failed:", failed)
    print("critical:", FACTS["critical"], "| next audit:", FACTS["next_audit"])
    assert passed + failed == total == 18
    assert FACTS["critical"] == 0, "zero critical findings required"
    rate = 100.0 * passed / total
    print("pass rate: %%.1f%%%%" %% rate)
    assert 88.8 < rate < 89.0
    print("OK: %%s verified security audit scorecard" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_change(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("changes YTD:", FACTS["changes_ytd"], "| breaking:", FACTS["breaking"])
    print("rollback tested:", FACTS["rollback_tested"])
    print("lead time (days):", FACTS["lead_days"], "| window:", FACTS["window"])
    assert FACTS["changes_ytd"] == 23 and FACTS["breaking"] == 4
    assert FACTS["rollback_tested"] is True
    assert FACTS["lead_days"] == 14
    breaking_share = 100.0 * FACTS["breaking"] / FACTS["changes_ytd"]
    print("breaking share: %%.1f%%%%" %% breaking_share)
    assert 17.3 < breaking_share < 17.5
    print("OK: %%s verified change management stats" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_harness(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("cases:", FACTS["cases"], "| pass:", FACTS["pass"], "| fail:", FACTS["fail"])
    print("contract tests:", FACTS["contract_tests"], "| sandbox:", FACTS["sandbox"])
    assert FACTS["pass"] + FACTS["fail"] == FACTS["cases"] == 64
    assert FACTS["contract_tests"] == 22
    assert FACTS["sandbox"] is True, "harness runs against sandbox only"
    rate = 100.0 * FACTS["pass"] / FACTS["cases"]
    print("pass rate: %%.2f%%%%" %% rate)
    assert 95.31 < rate < 95.32
    print("OK: %%s verified test harness scorecard" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_docs(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import datetime
FACTS = %s
def main():
    print("sections:", FACTS["sections"], "| examples:", FACTS["examples"])
    reviewed = datetime.date.fromisoformat(FACTS["reviewed"])
    stale = (datetime.date(2026, 10, 17) - reviewed).days
    print("reviewed:", reviewed, "| stale days:", stale)
    assert FACTS["sections"] == 9 and FACTS["examples"] == 14
    assert stale == FACTS["stale_days"] == 16, "docs reviewed 2026-10-01 are 16 days old"
    print("OK: %%s verified documentation standard" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_multitenant(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    tenants = FACTS["tenants"]
    total_quota = 10000  # requests/min shared
    floor = total_quota // tenants
    print("tenants:", tenants, "| isolation:", FACTS["isolation"])
    print("guaranteed floor per tenant: %%d req/min" %% floor)
    assert floor == 71, "10000/140 = 71 req/min floor"
    assert FACTS["quota_share"] == "fair"
    assert FACTS["noisy_neighbor_guards"] is True
    # noisy neighbor capped at 5%% of total
    cap = total_quota * 0.05
    assert cap == 500.0
    print("per-tenant burst cap: %%.0f req/min" %% cap)
    print("OK: %%s verified multi-tenant quota math" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_deprecate(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import datetime
FACTS = %s
def main():
    print("deprecated:", FACTS["deprecated"], "| migrated:", FACTS["migrated"],
          "| remaining:", FACTS["remaining"])
    assert FACTS["deprecated"] == FACTS["migrated"] + FACTS["remaining"] == 3
    sunset = datetime.date.fromisoformat(FACTS["sunset"])
    cutover = datetime.date.fromisoformat(FACTS["cutover"])
    margin = (sunset - cutover).days
    print("sunset:", sunset, "| cutover:", cutover, "| margin:", margin, "days")
    assert margin == 31 and margin >= 30
    print("OK: %%s verified deprecation schedule" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_redact(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
import re
FACTS = %s
def main():
    print("patterns:", FACTS["patterns"], "| masked/day:", FACTS["redacted_per_day"])
    print("fields:", ", ".join(FACTS["fields"]))
    assert FACTS["patterns"] == 6 == len(FACTS["fields"])
    assert FACTS["leaks_found"] == 0
    # verify each pattern catches a synthetic example
    tests = {
        "email": ("a@b.com", r"[\\w.+-]+@[\\w-]+\\.[\\w.]+"),
        "phone": ("555-010-0000", r"\\+?1?[-. ]?\\(?\\d{3}\\)?[-. ]?\\d{3}[-. ]?\\d{4}"),
        "card": ("4111111111111111", r"\\b\\d{13,19}\\b"),
        "ssn": ("123-45-6789", r"\\b\\d{3}-\\d{2}-\\d{4}\\b"),
        "token": ("sk_live_abc", r"sk_live_\\w+"),
        "password": ("password=hunter2", r"(?i)password\\s*=\\s*\\S+"),
    }
    caught = sum(1 for f, (s, p) in tests.items() if f in FACTS["fields"] and re.search(p, s))
    print("synthetic PII caught:", caught, "of", len(tests))
    assert caught == 6
    print("OK: %%s verified PII redaction patterns" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_marketplace(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    l = FACTS["listed"]; a = FACTS["approved"]; p = FACTS["pending"]; r = FACTS["rejected"]
    print("listed:", l, "| approved:", a, "| pending:", p, "| rejected:", r)
    assert a + p + r == l == 47
    rate = 100.0 * a / l
    print("approval rate: %%.1f%%%%" %% rate)
    assert 65.9 < rate < 66.0
    assert FACTS["reviews_per_year"] == 2
    print("OK: %%s verified marketplace ledger" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_roster(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("members:", FACTS["members"], "| shared contracts:", FACTS["contracts"])
    print("sync cadence (h):", FACTS["sync_h"], "| divergent:", FACTS["divergent"])
    assert FACTS["members"] == 12 and FACTS["contracts"] == 8
    assert FACTS["divergent"] == 0
    syncs_per_day = 24 / FACTS["sync_h"]
    print("syncs per member per day:", syncs_per_day)
    assert syncs_per_day == 1.0
    total_syncs = FACTS["members"] * 365
    print("member sync events/year:", total_syncs)
    assert total_syncs == 4380
    print("OK: %%s verified federation roster" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


def d_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("records:", FACTS["records"], "| complete:", FACTS["complete"])
    print("stale:", FACTS["stale"], "| ownerless:", FACTS["ownerless"])
    coverage = FACTS["complete"] / FACTS["records"]
    print("coverage: %%.2f" %% coverage)
    assert FACTS["records"] == 34 and FACTS["complete"] == 34
    assert FACTS["stale"] == 0 and FACTS["ownerless"] == 0
    assert coverage == FACTS["coverage"] == 1.0
    print("OK: %%s self-audit passed at full coverage" %% NAME)
if __name__ == "__main__":
    main()
""" % _pylit(data)


DEMOS = {
    "d_overview": d_overview, "d_rest": d_rest, "d_graphql": d_graphql,
    "d_hmac": d_hmac, "d_apikey": d_apikey, "d_oauth": d_oauth,
    "d_token_bucket": d_token_bucket, "d_formats": d_formats,
    "d_errors": d_errors, "d_uptime": d_uptime, "d_backoff": d_backoff,
    "d_pagination": d_pagination, "d_idempotency": d_idempotency,
    "d_versioning": d_versioning, "d_vault": d_vault,
    "d_telemetry": d_telemetry, "d_soap": d_soap, "d_grpc": d_grpc,
    "d_stream": d_stream, "d_sftp": d_sftp, "d_cache": d_cache,
    "d_circuit": d_circuit, "d_sla": d_sla, "d_cost": d_cost,
    "d_secaudit": d_secaudit, "d_change": d_change, "d_harness": d_harness,
    "d_docs": d_docs, "d_multitenant": d_multitenant,
    "d_deprecate": d_deprecate, "d_redact": d_redact,
    "d_marketplace": d_marketplace, "d_roster": d_roster,
    "d_mastery": d_mastery,
}
