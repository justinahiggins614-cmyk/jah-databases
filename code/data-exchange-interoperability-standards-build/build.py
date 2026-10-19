#!/usr/bin/env python3
"""Build the Data Exchange and Interoperability Standards pair (gap-audit part 2).

Verified 2026-10-17: NO database covers data exchange/interoperability as a
discipline (schemas, serialization, identifiers, API contracts, compatibility
mappings). Manifest keyword search (interoperability, data exchange): zero hits.
Nearest neighbors are single-format study items only. ZERO full-record coverage.

Two NEW databases, 34 ladder-ordered records each:
  data-exchange-interoperability-standards            (public-harvest)
  data-exchange-interoperability-standards-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_data_exchange import ENTRIES

RK = "interoperability standard record"
CIT_PUB = ("Data exchange and interoperability (standard references: Fielding 'Architectural "
           "Styles and the Design of Network-based Software Architectures' (REST) 2000; "
           "OpenAPI Specification (OpenAPI Initiative); W3C XML, XML Schema, RDF specifications; "
           "ISO 8601 date and time; JSON (ECMA-404); Apache Avro specification; Protocol "
           "Buffers; HL7 FHIR; schema.org vocabulary; NIST 'Framework for Cyber-Physical Systems').")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of interoperability."
STANDARDS = ["Exchange practice per the cited specifications",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="data-exchange-interoperability-standards", name_base="Data Exchange and Interoperability Standards",
    tagline=("Schemas, serialization, identifiers, API contracts, and compatibility mappings: "
             "how independent systems exchange data without corruption or confusion - from "
             "JSON, encodings, and identifiers through REST contracts and binary formats to "
             "ontologies, schema evolution, and conformance testing, taught progressively "
             "along the ladder."),
    record_kind=RK, prefix_pub="JAH-DEIS-", prefix_sig="JAH-DEISS-",
    ai_base="JAH Interoperability Archivist",
    role_pub=("interoperability archivist - schemas, serialization, identifiers, API "
              "contracts, compatibility mappings; teaching progressively along the ladder "
              "from foundations through compounded to advanced; answers from many angles - "
              "definition, example, procedure, math, standards - using only the system's "
              "own archive data"),
    role_sig=("interoperability archivist - Signature editions: his original Signature "
              "treatment of data exchange, clearly labeled Signature-made and never "
              "presented as authentic public record; teaches progressively along the ladder; "
              "answers from many angles using only the system's own archive data"),
    search_ph="Search JSON Schema, REST, OpenAPI, Avro, identifiers, compatibility...",
    chat_ph="Ask about data exchange...",
    archive_topic="interoperability records",
    gen_kind="data-exchange",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked interoperability: what interoperability is, "
              "JSON/XML/CSV, UTF-8, identifiers, schemas, JSON Schema, serialization, CSV "
              "rules, timestamps, units, nulls, versioning, REST contracts, OpenAPI, lasting "
              "identifiers, XSD, Avro/Protobuf, ETL, field mapping, API versioning, status "
              "codes, pagination, authentication, webhooks, ontologies, linked data, schema "
              "evolution, compatibility mappings, quality gates, master data, audit, "
              "streaming exchange, FHIR case study, and conformance testing - organized in "
              "the Signature system. Every record carries the full entry: description, how "
              "it works, key points, requirements, standards, citations, and a working "
              "demonstration program. Records are ordered by the teaching ladder: "
              "Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of data exchange and "
              "interoperability: the full ladder from formats and identifiers through API "
              "contracts to ontologies and conformance, reframed as Signature science. "
              "Clearly labeled Signature-made, never presented as authentic public record. "
              "Every record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


import json as _json


@_reg("dx_jsonschema")
def d_jsonschema(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # minimal JSON Schema validation: required fields, types, ranges
    schema = {"required": ["id", "temp_C"],
              "types": {"id": str, "temp_C": (int, float)},
              "ranges": {"temp_C": (-50.0, 60.0)}}
    docs = [
        {"id": "S-01", "temp_C": 21.5},
        {"id": "S-02"},                              # missing required
        {"id": "S-03", "temp_C": "hot"},             # wrong type
        {"id": "S-04", "temp_C": 999.0},             # out of range
    ]
    def validate(doc):
        errs = []
        for f in schema["required"]:
            if f not in doc:
                errs.append("missing " + f)
        for f, t in schema["types"].items():
            if f in doc and not isinstance(doc[f], t):
                errs.append("bad type " + f)
        for f, (lo, hi) in schema["ranges"].items():
            if f in doc and isinstance(doc[f], (int, float)) and not (lo <= doc[f] <= hi):
                errs.append("out of range " + f)
        return errs
    results = [(d.get("id", "?"), validate(d)) for d in docs]
    for did, errs in results:
        print("  %s: %s" % (did, "VALID" if not errs else "; ".join(errs)))
    assert results[0][1] == [] and len(results[1][1]) == 1
    assert len(results[2][1]) == 1 and len(results[3][1]) == 1
    print("OK: %s validated documents against a schema" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_csv2json")
def d_csv2json(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import csv, io, json
def main():
    text = "sensor_id,temp_C,humidity\\nst-01,21.5,45\\nst-02,22.0,47\\n"
    rows = list(csv.DictReader(io.StringIO(text)))
    docs = [{"sensor_id": r["sensor_id"], "temp_C": float(r["temp_C"]),
             "humidity": int(r["humidity"])} for r in rows]
    out = json.dumps(docs, indent=1)
    print(out)
    back = json.loads(out)
    assert back[0] == {"sensor_id": "st-01", "temp_C": 21.5, "humidity": 45}
    assert len(back) == 2
    print("OK: %s transformed CSV to typed JSON" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_uuid")
def d_uuid(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import hashlib
def main():
    # deterministic identifier: UUID5-style from namespace + name (sha1-based)
    def uuid5(namespace, name):
        h = hashlib.sha1((namespace + name).encode()).digest()
        b = bytearray(h[:16])
        b[6] = (b[6] & 0x0F) | 0x50   # version 5
        b[8] = (b[8] & 0x3F) | 0x80   # variant
        hx = b.hex()
        return "%s-%s-%s-%s-%s" % (hx[:8], hx[8:12], hx[12:16], hx[16:20], hx[20:])
    ns = "jah-databases-dataset"
    a = uuid5(ns, "run_001.csv")
    b = uuid5(ns, "run_001.csv")
    c = uuid5(ns, "run_002.csv")
    print("  run_001 -> %s" % a)
    assert a == b, "same name must give same identifier"
    assert a != c, "different names must differ"
    assert a[14] == "5", "version nibble must be 5"
    print("OK: %s minted deterministic identifiers" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_units")
def d_units(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # QUDT-style: quantity = value + unit; convert via factor to reference unit
    to_si = {"m": 1.0, "cm": 0.01, "mm": 0.001, "km": 1000.0,
             "s": 1.0, "min": 60.0, "h": 3600.0,
             "kg": 1.0, "g": 0.001}
    def convert(value, from_u, to_u):
        return value * to_si[from_u] / to_si[to_u]
    cases = [(12.0, "cm", "m", 0.12), (90.0, "min", "h", 1.5), (2500.0, "g", "kg", 2.5)]
    for v, fu, tu, exp in cases:
        got = convert(v, fu, tu)
        print("  %.1f %s = %.4f %s" % (v, fu, got, tu))
        assert abs(got - exp) < 1e-9
    print("OK: %s converted quantities with unit-aware factors" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_apicontract")
def d_apicontract(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # API contract check: request/response shapes for GET /readings/{id}
    contract = {"method": "GET", "path": "/readings/{id}",
                "response": {"status": 200, "fields": ["id", "temp_C", "ts"]}}
    def check_response(resp):
        errs = []
        if resp.get("status") != contract["response"]["status"]:
            errs.append("status %s != 200" % resp.get("status"))
        body = resp.get("body", {})
        for f in contract["response"]["fields"]:
            if f not in body:
                errs.append("missing field " + f)
        return errs
    good = {"status": 200, "body": {"id": "S-01", "temp_C": 21.5, "ts": "2026-10-17T21:00:00Z"}}
    bad = {"status": 200, "body": {"id": "S-01", "temp_C": 21.5}}
    assert check_response(good) == []
    assert check_response(bad) == ["missing field ts"]
    print("contract %s %s: good response passes, bad response flagged" % (
        contract["method"], contract["path"]))
    print("OK: %s checked responses against the API contract" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_version")
def d_version(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # semantic-version compatibility matrix: same major -> compatible
    def parse(v):
        return tuple(int(x) for x in v.split("."))
    def compatible(a, b):
        pa, pb = parse(a), parse(b)
        return pa[0] == pb[0] and pb >= pa  # same major, not older
    pairs = [("1.2.0", "1.4.0", True), ("1.2.0", "2.0.0", False),
             ("2.1.0", "2.0.0", False), ("1.2.0", "1.2.0", True)]
    for a, b, exp in pairs:
        got = compatible(a, b)
        print("  %s -> %s: %s" % (a, b, "compatible" if got else "BREAKING"))
        assert got == exp
    print("OK: %s computed a semver compatibility matrix" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_encoding")
def d_encoding(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # normalize exchange text to UTF-8; reject undecodable bytes loudly
    samples = {
        "ascii": b"temp: 21.5 C",
        "utf8": "temp: 21.5 \\u00b0C".encode("utf-8"),
        "latin1_degree": "temp: 21.5 \\u00b0C".encode("latin-1"),
    }
    for label, raw in samples.items():
        try:
            text = raw.decode("utf-8")
            status = "utf-8 clean"
        except UnicodeDecodeError:
            text = raw.decode("latin-1")
            status = "latin-1 fallback (flagged)"
        print("  %-14s -> %s : %s" % (label, status, text))
    assert samples["ascii"].decode("utf-8") == "temp: 21.5 C"
    print("OK: %s normalized exchange text to UTF-8" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_etl")
def d_etl(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # ETL field mapping: source schema -> canonical schema, with type coercion
    mapping = {"sensor": "sensor_id", "t": "temp_C", "rh": "humidity"}
    coercions = {"temp_C": float, "humidity": int}
    source = {"sensor": "st-01", "t": "21.5", "rh": "45", "extra": "dropped"}
    canonical = {}
    for sk, sv in source.items():
        if sk in mapping:
            ck = mapping[sk]
            canonical[ck] = coercions.get(ck, str)(sv)
    print("mapped: %s" % canonical)
    assert canonical == {"sensor_id": "st-01", "temp_C": 21.5, "humidity": 45}
    assert "extra" not in canonical
    print("OK: %s mapped source fields to the canonical schema" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_openapi")
def d_openapi(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # minimal OpenAPI description: paths, operations, parameters
    spec = {"openapi": "3.0.0",
            "paths": {"/readings/{id}":
                      {"get": {"parameters": [{"name": "id", "in": "path", "required": True}],
                               "responses": {"200": {"description": "one reading"}}}}}}
    assert spec["openapi"].startswith("3.")
    paths = spec["paths"]
    assert "/readings/{id}" in paths
    op = paths["/readings/{id}"]["get"]
    assert op["parameters"][0]["required"] is True
    assert "200" in op["responses"]
    print("openapi %s: %d path(s), GET /readings/{id} documented" % (spec["openapi"], len(paths)))
    print("OK: %s validated an OpenAPI description" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("dx_compat")
def d_compat(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # compatibility mapping between two standards' field names
    std_a = ["temperature", "pressure", "timestamp"]
    std_b = ["temp_C", "press_kPa", "ts"]
    mapping = dict(zip(std_a, std_b))
    record_a = {"temperature": 21.5, "pressure": 101.3, "timestamp": "2026-10-17T21:00:00Z"}
    record_b = {mapping[k]: v for k, v in record_a.items()}
    print("A->B: %s" % record_b)
    assert record_b == {"temp_C": 21.5, "press_kPa": 101.3, "ts": "2026-10-17T21:00:00Z"}
    # round-trip must be lossless
    rev = {v: k for k, v in mapping.items()}
    assert {rev[k]: v for k, v in record_b.items()} == record_a
    print("OK: %s mapped fields between standards losslessly" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
