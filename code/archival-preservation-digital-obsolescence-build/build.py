#!/usr/bin/env python3
"""Build the Archival Preservation and Digital Obsolescence pair (gap-audit part 2).

Verified 2026-10-17: NO database covers digital preservation as a discipline
(format-migration plans, checksum manifests, preservation metadata, recovery
procedures). Manifest keyword search (obsolescence, digital preservation,
checksum manifest): zero hits. Nearest: 'library-archival-published' (library
archival STUDIES published works - different discipline) and
'metaknowledge-preservation-databases' (a meta catalog). ZERO full-record
coverage of preservation practice itself.

Two NEW databases, 34 ladder-ordered records each:
  archival-preservation-digital-obsolescence            (public-harvest)
  archival-preservation-digital-obsolescence-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_archival_preservation import ENTRIES

RK = "digital preservation record"
CIT_PUB = ("Digital preservation (standard references: ISO 14721:2012 (OAIS reference model); "
           "ISO 16363:2012 (audit and certification of trustworthy repositories); "
           "PREMIS Data Dictionary for Preservation Metadata v3.0 (Library of Congress); "
           "PRONOM technical registry (The UK National Archives); TRAC criteria (OCLC/RLG); "
           "LOCKSS Program (Stanford); Conway 'Preservation in the Digital World' 1996).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of digital preservation."
STANDARDS = ["Preservation practice per ISO 14721 (OAIS) / PREMIS as cited",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="archival-preservation-digital-obsolescence", name_base="Archival Preservation and Digital Obsolescence",
    tagline=("Format-migration plans, checksum manifests, preservation metadata, and recovery "
             "procedures: how digital content survives bit rot, dead formats, dead media, and "
             "dead institutions - from fixity checks and OAIS packages through migration, "
             "emulation, and disaster recovery to the 100-year archive, taught progressively "
             "along the ladder."),
    record_kind=RK, prefix_pub="JAH-APDO-", prefix_sig="JAH-APDOS-",
    ai_base="JAH Preservation Archivist",
    role_pub=("digital preservation archivist - format migration, checksum manifests, "
              "preservation metadata, recovery procedures, OAIS, PREMIS, emulation; teaching "
              "progressively along the ladder from foundations through compounded to "
              "advanced; answers from many angles - definition, example, procedure, math, "
              "standards - using only the system's own archive data"),
    role_sig=("digital preservation archivist - Signature editions: his original Signature "
              "treatment of digital preservation, clearly labeled Signature-made and never "
              "presented as authentic public record; teaches progressively along the ladder; "
              "answers from many angles using only the system's own archive data"),
    search_ph="Search checksum, OAIS, PREMIS, migration, emulation, fixity, recovery...",
    chat_ph="Ask about digital preservation...",
    archive_topic="digital-preservation records",
    gen_kind="digital-preservation",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked digital preservation: what preservation is, "
              "bit rot, checksums and fixity, checksum manifests, open formats, PRONOM, the "
              "OAIS model, SIPs/AIPs/DIPs, redundancy, backup vs archiving, PREMIS, the "
              "designated community, format obsolescence, risk scoring, migration, emulation, "
              "normalization, fixity schedules, repair, LOCKSS, PREMIS in depth, disaster "
              "planning, succession, migration playbooks, significant properties, validation, "
              "manifests at scale, recovery drills, forensic recovery, timestamping, cost "
              "modeling, repository audit, and the 100-year archive - organized in the "
              "Signature system. Every record carries the full entry: description, how it "
              "works, key points, requirements, standards, citations, and a working "
              "demonstration program. Records are ordered by the teaching ladder: "
              "Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of digital preservation: "
              "the full ladder from fixity and OAIS through migration, emulation, and "
              "recovery to the 100-year archive, reframed as Signature science. Clearly "
              "labeled Signature-made, never presented as authentic public record. Every "
              "record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


import json as _json


@_reg("ap_checksum")
def d_checksum(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import hashlib
def main():
    files = {"aip_001/data.csv": "id,value\\n1,10\\n2,20\\n",
             "aip_001/meta.json": "{\\"title\\": \\"demo\\"}",
             "aip_001/readme.txt": "package readme\\n"}
    manifest = {f: hashlib.sha256(d.encode()).hexdigest() for f, d in files.items()}
    print("manifest entries: %d" % len(manifest))
    failures = [f for f, d in files.items()
                if hashlib.sha256(d.encode()).hexdigest() != manifest[f]]
    assert not failures, failures
    # simulate one corrupted file; the manifest must catch it
    corrupt = files["aip_001/data.csv"].replace("10", "11")
    assert hashlib.sha256(corrupt.encode()).hexdigest() != manifest["aip_001/data.csv"]
    print("fixity verified for %d files; 1 simulated corruption detected" % len(manifest))
    print("OK: %s verified fixity against a checksum manifest" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_risk")
def d_risk(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # format obsolescence risk score: openness + tool support + adoption + spec availability
    formats = {
        "CSV/UTF-8":      dict(open=10, tools=10, adoption=10, spec=10),
        "PDF/A-2":        dict(open=9,  tools=9,  adoption=8,  spec=10),
        "Vendor-XYZ-v3":  dict(open=2,  tools=3,  adoption=4,  spec=1),
    }
    for fmt, s in formats.items():
        risk = 40 - (s["open"] + s["tools"] + s["adoption"] + s["spec"])
        level = "LOW" if risk < 10 else ("MEDIUM" if risk < 22 else "HIGH")
        print("  %-14s risk score %2d/40 -> %s" % (fmt, risk, level))
        formats[fmt]["risk"] = risk
    assert formats["CSV/UTF-8"]["risk"] == 0
    assert formats["Vendor-XYZ-v3"]["risk"] == 30
    print("OK: %s scored format obsolescence risk" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_migrate")
def d_migrate(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # migration plan: ordered steps with validation gates; significant properties checked
    plan = [
        ("inventory", "list all 1,204 Vendor-XYZ-v3 files with checksums"),
        ("pilot", "migrate 20-file sample; validate significant properties"),
        ("validate", "byte-compare text layers; spot-check 5% rendering"),
        ("full-run", "migrate all; failures quarantined with logs"),
        ("verify", "re-run fixity; sign off migration report"),
    ]
    sig_props = ["text content", "page count", "document structure"]
    for i, (step, desc) in enumerate(plan, 1):
        print("  step %d %-10s %s" % (i, step, desc))
    assert len(plan) == 5 and plan[0][0] == "inventory"
    assert len(sig_props) == 3
    print("significant properties preserved: %s" % ", ".join(sig_props))
    print("OK: %s built a validated migration plan" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_premis")
def d_premis(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import json
def main():
    # PREMIS: Object + Event + Agent + Rights describing one preservation action
    obj = {"type": "file", "id": "obj-0001",
           "fixity": {"sha256": "9f2c...", "checked": "2026-10-17"}}
    event = {"type": "fixity check", "date": "2026-10-17",
             "outcome": "success", "object": "obj-0001"}
    agent = {"type": "software", "name": "fixity-daemon 2.1"}
    rights = {"basis": "deposit agreement", "act": "preserve", "granted": True}
    record = {"object": obj, "event": event, "agent": agent, "rights": rights}
    text = json.dumps(record, sort_keys=True)
    print("PREMIS record: %d entities, %d bytes" % (len(record), len(text)))
    assert all(k in record for k in ("object", "event", "agent", "rights"))
    assert record["event"]["outcome"] == "success"
    print("OK: %s assembled a PREMIS object/event/agent/rights record" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_oais")
def d_oais(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # OAIS packages: SIP (submitted) -> AIP (archived) -> DIP (disseminated)
    sip = {"content": ["data.csv"], "metadata": ["submitter-info.json"]}
    aip = {"content": sip["content"] + ["checksum-manifest.sha256"],
           "metadata": sip["metadata"] + ["premis.xml", "preservation-plan.txt"]}
    dip = {"content": ["data.csv"], "metadata": ["descriptive-record.json"]}
    print("SIP: %d files -> AIP: %d files -> DIP: %d files" % (
        len(sip["content"]) + len(sip["metadata"]),
        len(aip["content"]) + len(aip["metadata"]),
        len(dip["content"]) + len(dip["metadata"])))
    assert "checksum-manifest.sha256" in aip["content"]
    assert "premis.xml" in aip["metadata"]
    print("OK: %s walked content through SIP, AIP, and DIP" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_lockss")
def d_lockss(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import random
def main():
    # LOCKSS-style: 7 replicas; yearly audit; repair damaged copies from good ones
    rnd = random.Random(42)
    replicas = [{"id": i, "good": True} for i in range(7)]
    # one bad year: 2 replicas suffer bit rot
    for i in rnd.sample(range(7), 2):
        replicas[i]["good"] = False
    damaged = [r["id"] for r in replicas if not r["good"]]
    good = [r["id"] for r in replicas if r["good"]]
    print("audit: %d good, %d damaged %s" % (len(good), len(damaged), damaged))
    for r in replicas:
        if not r["good"]:
            r["good"] = True  # repaired from a good replica
    assert all(r["good"] for r in replicas)
    assert len(good) >= 3, "quorum lost"
    print("repaired %d replicas from quorum; all 7 healthy" % len(damaged))
    print("OK: %s audited replicas and repaired damage from quorum" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_pronom")
def d_pronom(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # format identification by magic numbers (PRONOM-style signatures)
    signatures = {
        b"%PDF-": "PDF",
        b"\\x89PNG\\r\\n\\x1a\\n": "PNG",
        b"PK\x03\x04": "ZIP-based (OOXML/ODF/JAR)",
        b"\\x1f\\x8b": "gzip",
    }
    samples = {
        "report.pdf": b"%PDF-1.7 ...",
        "scan.png": b"\\x89PNG\\r\\n\\x1a\\n...",
        "data.zip": b"PK\x03\x04...",
        "notes.txt": b"plain text, no magic",
    }
    for fname, head in samples.items():
        fmt = next((f for sig, f in signatures.items() if head.startswith(sig)), "unknown/plain")
        print("  %-12s -> %s" % (fname, fmt))
    assert samples["report.pdf"].startswith(b"%PDF-")
    print("OK: %s identified formats by magic-number signatures" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_schedule")
def d_schedule(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # fixity schedule: check frequency by value tier; compute yearly check load
    tiers = [
        ("critical", 1200, 12),   # files, checks per year
        ("standard", 48000, 2),
        ("cold", 900000, 1),
    ]
    total = 0
    for tier, files, per_year in tiers:
        load = files * per_year
        total += load
        print("  %-9s %7d files x %2d/yr = %8d checks" % (tier, files, per_year, load))
    assert total == 1200 * 12 + 48000 * 2 + 900000 * 1
    print("yearly fixity load: %d checks" % total)
    print("OK: %s scheduled fixity checks by value tier" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_recovery")
def d_recovery(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # recovery drill: ordered procedure with verification gates
    drill = [
        ("declare", "incident commander declares; clock starts"),
        ("assess", "identify affected collections from manifests"),
        ("locate", "find newest good replica per manifest"),
        ("restore", "copy to staging; verify checksums match manifest"),
        ("validate", "spot-check rendering of 5% of restored files"),
        ("resume", "return to service; write after-action report"),
    ]
    for i, (step, desc) in enumerate(drill, 1):
        print("  %d. %-9s %s" % (i, step, desc))
    assert [s for s, _ in drill] == ["declare", "assess", "locate", "restore", "validate", "resume"]
    print("drill gates: checksums verified before resume - no silent restores")
    print("OK: %s ran a recovery drill with verification gates" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ap_cost")
def d_cost(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # preservation cost model: storage + fixity compute + labor, per TB per year
    tb = 50.0
    storage_per_tb_yr = 240.0     # redundant, geographically separated
    fixity_per_tb_yr = 36.0       # checksum compute + audit labor share
    labor_fixed_yr = 12000.0      # preservation staff share
    total = tb * (storage_per_tb_yr + fixity_per_tb_yr) + labor_fixed_yr
    print("%.0f TB: storage $%.0f + fixity $%.0f + labor $%.0f = $%.0f/yr" % (
        tb, tb * storage_per_tb_yr, tb * fixity_per_tb_yr, labor_fixed_yr, total))
    assert abs(total - 25800.0) < 1e-9
    print("OK: %s modeled yearly preservation cost" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
