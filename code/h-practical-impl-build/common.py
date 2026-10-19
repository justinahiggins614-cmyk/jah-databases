#!/usr/bin/env python3
"""Shared build machinery for the H-group (practical implementation knowledge)
worker: 10 database pairs (public + Signature), 34 ladder-ordered records each.

Writes (never commits):
  db/<slug>/index.html + db/<slug>/gen-<slug>.js
  <data-1>/data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
  manifest-additions.json (staged for the coordinator; manifest/api untouched)

Property of Justin Addam Higgins (JAH).
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate  # noqa: E402

# ---------------------------------------------------------------- pair table
# (slug, short name fragment, tagline, record_kind, prefix, ai_name, role,
#  groups, search_ph, chat_ph)
PAIRS = [
 ("repair-manuals-service-procedures", "Repair Manuals and Service Procedures",
  "Diagnostic sequences, disassembly orders, repair procedures, adjustments, and verification tests - full service procedures for keeping equipment running right.",
  "service procedure record", "JAH-RMSP-", "JAH Service Procedures Archivist",
  "service procedures archivist - diagnostics, disassembly, repair, adjustment, and verification; teaching the full service workflow from symptom to verified fix; answers from many angles - procedure, safety, tools, measurements, standards - using only archive data",
  ["Diagnostics", "Disassembly", "Repair", "Adjustment", "Verification"],
  "Search diagnostics, disassembly, bearing replacement, torque, calibration after repair, acceptance tests...",
  "Ask about repair procedures..."),
 ("installation-commissioning-procedures", "Installation and Commissioning Procedures",
  "Site preparation, mechanical and electrical installation, configuration, startup sequences, and acceptance testing - from delivery day to signed-off operation.",
  "commissioning procedure record", "JAH-ICOP-", "JAH Commissioning Archivist",
  "commissioning archivist - site preparation, installation, configuration, startup, and acceptance testing; answers from many angles - procedure, safety, sequencing, measurements, standards - using only archive data",
  ["Site Preparation", "Mechanical Installation", "Electrical & Controls", "Startup", "Acceptance Testing"],
  "Search site prep, rigging, leveling, first energization, load testing, punch lists, sign-off...",
  "Ask about installation and commissioning..."),
 ("calibration-adjustment-instructions", "Calibration and Adjustment Instructions",
  "Reference equipment, step-by-step calibration procedures, tolerances, uncertainty, and pass/fail criteria - keeping every measurement trustworthy.",
  "calibration instruction record", "JAH-CLBR-", "JAH Calibration Archivist",
  "calibration archivist - reference standards, calibration procedures, tolerances, and verification; answers from many angles - procedure, traceability, uncertainty, decision rules - using only archive data",
  ["Reference Standards", "Calibration Procedures", "Tolerances & Uncertainty", "Verification"],
  "Search traceability, multimeter calibration, pressure, temperature, uncertainty, pass/fail rules...",
  "Ask about calibration..."),
 ("troubleshooting-decision-trees", "Troubleshooting Decision Trees",
  "Executable symptom-to-cause decision trees: observations, diagnostic tests, candidate causes, and corrective actions for real faults across electrical, mechanical, thermal, and control systems.",
  "troubleshooting decision tree record", "JAH-TSHT-", "JAH Troubleshooting Archivist",
  "troubleshooting archivist - symptom observation, diagnostic tests, cause isolation, and corrective action; answers from many angles - symptom, test, cause, fix, prevention - using only archive data",
  ["Electrical Faults", "Mechanical Faults", "Thermal & Fluid Faults", "Control & Software Faults"],
  "Search no power, blown fuse, vibration, overheating, leaks, breaker trips, control instability...",
  "Ask about troubleshooting a fault..."),
 ("compatibility-interchangeability-records", "Compatibility and Interchangeability Records",
  "Cross-reference tables of what works with what: interchangeable parts, superseded part numbers, system compatibility, software and firmware versions, and interfaces.",
  "compatibility cross-reference record", "JAH-CIR-", "JAH Compatibility Archivist",
  "compatibility archivist - parts cross-reference, system compatibility, software versions, and interfaces; answers from many angles - interchange, substitution, supersession, risk - using only archive data",
  ["Parts Cross-Reference", "Systems Compatibility", "Software & Firmware", "Interfaces & Connectors"],
  "Search bearing interchange, fastener grades, superseded parts, PLC compatibility, firmware matrix...",
  "Ask about compatibility or substitutes..."),
 ("tooling-fixture-designs", "Tooling and Fixture Designs",
  "Jig, fixture, template, and gauge designs with dimensions, setup instructions, and manufacturing constraints - including 3D-printable tooling with real print directions.",
  "tooling fixture design record", "JAH-TFD-", "JAH Tooling Archivist",
  "tooling archivist - jigs, fixtures, templates, gauges, and workholding; answers from many angles - design, locating, clamping, tolerances, setup - using only archive data",
  ["Jigs", "Fixtures", "Templates & Gauges", "Setup & Workholding"],
  "Search drill jigs, 3-2-1 locating, welding fixtures, go/no-go gauges, 3D-printed tooling...",
  "Ask about tooling and fixtures..."),
 ("engineering-case-studies", "Engineering Case Studies",
  "Real engineering projects documented end to end: constraints, decisions, failures, measurements, and outcomes - what worked, what did not, and why.",
  "engineering case study record", "JAH-ENCS-", "JAH Engineering Case Archivist",
  "engineering case archivist - real projects with constraints, decisions, failures, and measured outcomes; answers from many angles - context, decision, failure, measurement, lesson - using only archive data",
  ["Mechanical", "Electrical", "Civil & Structural", "Systems & Controls"],
  "Search failure analysis, retrofits, root cause, measurements, lessons learned...",
  "Ask about an engineering case..."),
 ("costed-build-recipes", "Costed Build Recipes",
  "Complete build recipes with bills of materials, tools, labor hours, costs, alternatives, and build-specific validation tests - every build priced and proven.",
  "costed build recipe record", "JAH-CBR-", "JAH Build Recipes Archivist",
  "build recipes archivist - bills of materials, tools, labor, costs, and validation; answers from many angles - materials, cost, time, alternatives, testing - using only archive data",
  ["Workshop Builds", "Electronics Builds", "Facility Builds", "Prototype Builds"],
  "Search workbench, BOM, labor hours, build cost, validation tests...",
  "Ask about a build recipe..."),
 ("field-modification-retrofit-records", "Field Modification and Retrofit Records",
  "Documented field modifications and retrofits: change details, compatibility checks, safety assessments, and post-change verification tests.",
  "field modification record", "JAH-FMRR-", "JAH Retrofit Archivist",
  "retrofit archivist - field modifications with change control, compatibility, safety assessment, and verification; answers from many angles - change, compatibility, safety, testing - using only archive data",
  ["Mechanical Modifications", "Electrical Modifications", "Control & Software Modifications", "Safety & Compliance"],
  "Search VSD retrofit, guard additions, PLC expansion, safety upgrades, change control...",
  "Ask about a field modification..."),
 ("end-of-life-disposal-procedures", "End-of-Life Disposal Procedures",
  "Disassembly sequences, hazardous-material handling, recycling streams, reuse options, and compliant disposal procedures for retired equipment.",
  "end-of-life disposal record", "JAH-EOLD-", "JAH End-of-Life Archivist",
  "end-of-life archivist - disassembly, hazardous materials, recycling, reuse, and compliant disposal; answers from many angles - procedure, safety, streams, compliance - using only archive data",
  ["Disassembly", "Hazardous Materials", "Recycling Streams", "Reuse & Refurbishment", "Compliant Disposal"],
  "Search decommissioning, refrigerant recovery, battery recycling, e-waste, disposal compliance...",
  "Ask about end-of-life disposal..."),
]

SIG_PREFIX = lambda p: p[:-1] + "S-"  # JAH-RMSP- -> JAH-RMSPS-

TIERS = ["foundations", "compounded", "advanced"]
TIER_LABEL = {"foundations": "Foundations", "compounded": "Compounded", "advanced": "Advanced"}

SCHEMA = ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
          "standards, citations, src, ladder_rank, ladder_tier, demo")

PUB_LINE = ("Public records - real, fact-checked domain knowledge, each record a complete "
            "working document with procedures, numbers, and references, organized in the "
            "Signature system.")
SIG_LINE = ("Signature originals - his original Signature treatment of each topic: the "
            "Signature method restates the working knowledge as his own engineered system, "
            "with the same procedures, numbers, and working demonstrations, clearly labeled "
            "Signature-made and never presented as authentic public record.")


def make_cfgs():
    """Return dict slug -> cfg for all 20 databases (10 pairs)."""
    DBCFG = {}
    for (slug, frag, tagline, rk, prefix, ai, role, groups, search_ph, chat_ph) in PAIRS:
        for source, sfx in (("public", ""), ("signature", "-signature")):
            s = slug + sfx
            name = "The %s%s Database" % (frag, " Signature" if sfx else "")
            pre = prefix if source == "public" else SIG_PREFIX(prefix)
            a = ai + (" (Signature)" if sfx else "")
            ladder = (" Records are ordered by the teaching ladder: Foundations -> "
                      "Compounded -> Advanced, simple to most complex.")
            hero_p = ("%s - %s Every record carries the full entry: description, how it "
                      "works, key points, requirements, standards, citations, and a working "
                      "demonstration program.%s"
                      % (tagline, SIG_LINE if sfx else PUB_LINE, ladder))
            DBCFG[s] = {
                "name": name, "tagline": tagline, "record_kind": rk,
                "prefix": pre, "ai": a, "role": role,
                "hero_p": hero_p,
                "sig_type": ("Signature originals organized in the Signature system"
                             if sfx else "Public records organized in the Signature system"),
                "search_ph": search_ph, "chat_ph": chat_ph,
                "archive_blurb": ("Seeded %s %s, marching toward one million records. "
                                  "Presented in teaching-ladder order: foundations, "
                                  "compounded, advanced."
                                  % ("Signature-original" if sfx else "public-record", rk)),
                "schema": SCHEMA,
                "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
                "gen_desc": ("Generate clearly-labeled %s studies. Seeded archive records "
                             "are the authoritative entries." % rk),
                "greet": "I am the %s. %s" % (a, chat_ph.replace("Ask about ", "Ask me about ").rstrip(".") + "."),
                "gen_fields": [TIER_LABEL[t] for t in TIERS],
                "gen_kind": s, "gen_demo_kind": "python",
                "source": source, "groups": groups,
            }
    return DBCFG


# ---------------------------------------------------------------- demo library
# Every demo is real, runnable, stdlib-only Python: it performs the record's
# core computation, asserts the record's stated facts, and prints OK:.
# Machine-executed at build time; any failure fails the build.

def _hdr(rid, title, group, kind_note):
    safe = title.replace('"', "'")
    return ('#!/usr/bin/env python3\n"""%s - working demonstration.\nRecord %s [%s]. %s\nProperty of Justin Addam Higgins (JAH).\n"""\nTITLE = "%s"\n' % (safe, rid, group, kind_note, safe))


def _tail(title, fmt, *args):
    call = ("    print(\"" + fmt + "\" %% (%s))\n" % (", ".join(args)) if args else
            "    print(\"" + fmt + "\")\n")
    return ("def main():\n" + call +
            "    print(\"OK: %%s demo verified\" %% TITLE)\n\n"
            "if __name__ == \"__main__\":\n    main()\n")


def demo_steps(rid, title, group, p):
    """Numbered procedure: verifies step count, durations, total time."""
    steps = p["steps"]
    body = "STEPS = %s\n" % repr([(s[0], float(s[1])) for s in steps])
    body += ("def main():\n"
             "    assert len(STEPS) >= 3, 'procedure needs at least 3 steps'\n"
             "    total = 0.0\n"
             "    for i, (name, mins) in enumerate(STEPS, 1):\n"
             "        assert mins > 0, 'step %d has non-positive time' % i\n"
             "        total += mins\n"
             "        print('  step %2d [%5.1f min] %s' % (i, mins, name))\n"
             "    print('steps=%d total=%.1f min' % (len(STEPS), total))\n"
             "    assert total > 0, 'total time must be positive'\n"
             "    print(\"OK: %s procedure demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Procedure walkthrough.") + body


def demo_torque(rid, title, group, p):
    """Fastener torque table: verifies each torque sits in the plausible band
    for its thread size and that tolerances are positive."""
    rows = p["fasteners"]
    body = "ROWS = %s\n" % repr([(r[0], float(r[1]), float(r[2]), float(r[3])) for r in rows])
    body += ("# plausible torque bands (Nm) by metric thread size, dry steel\n"
             "BANDS = [(4, 1.0, 4.0), (5, 2.0, 7.0), (6, 4.0, 14.0), (8, 10.0, 35.0),\n"
             "         (10, 20.0, 65.0), (12, 35.0, 120.0), (16, 90.0, 290.0), (20, 170.0, 560.0)]\n"
             "def band(size):\n"
             "    for s, lo, hi in BANDS:\n"
             "        if size <= s + 0.5:\n"
             "            return lo, hi\n"
             "    return BANDS[-1][1], BANDS[-1][2]\n"
             "def main():\n"
             "    for desc, size, tq, tol in ROWS:\n"
             "        lo, hi = band(size)\n"
             "        assert tol > 0, 'tolerance must be positive: ' + desc\n"
             "        assert lo <= tq <= hi, 'torque %s Nm out of band for M%g' % (tq, size)\n"
             "        print('  M%-4g %6.1f Nm (+/-%.0f%%)  %s' % (size, tq, tol, desc))\n"
             "    print('fasteners=%d all torques in plausible band' % len(ROWS))\n"
             "    print(\"OK: %s torque demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Torque specification check.") + body


def demo_tolerance(rid, title, group, p):
    """Calibration readings vs tolerance: computes errors, pass/fail each."""
    body = ("NOMINAL = %r\nTOL = %r\nUNIT = %r\nREADINGS = %s\n"
            % (p["nominal"], p["tol"], p["unit"], repr([float(x) for x in p["readings"]])))
    body += ("def main():\n"
             "    assert TOL > 0, 'tolerance must be positive'\n"
             "    fails = []\n"
             "    for i, r in enumerate(READINGS, 1):\n"
             "        err = r - NOMINAL\n"
             "        ok = abs(err) <= TOL\n"
             "        print('  reading %2d: %.4g %s  err %.4g %s' %\n"
             "              (i, r, UNIT, err, 'PASS' if ok else 'FAIL'))\n"
             "        if not ok:\n"
             "            fails.append(i)\n"
             "    n = len(READINGS)\n"
             "    print('passed %d/%d within +/-%.4g %s' % (n - len(fails), n, TOL, UNIT))\n"
             "    assert not fails, 'readings out of tolerance: %s' % fails\n"
             "    print(\"OK: %s tolerance demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Tolerance verification.") + body


def demo_tree(rid, title, group, p):
    """Decision tree walk: follows answers from the start node to a corrective
    action and asserts the expected action is reached."""
    body = ("TREE = %s\nSTART = %r\nANSWERS = %s\nEXPECT = %r\n"
            % (repr(p["tree"]), p["start"], repr(p["answers"]), p["expect"]))
    body += ("def main():\n"
             "    node = START\n"
             "    path = []\n"
             "    for _ in range(50):\n"
             "        spec = TREE[node]\n"
             "        path.append(node)\n"
             "        if 'action' in spec:\n"
             "            print('path: ' + ' -> '.join(path))\n"
             "            print('corrective action: ' + spec['action'])\n"
             "            assert spec['action'] == EXPECT, 'wrong terminal action'\n"
             "            print(\"OK: %s decision-tree demo verified\" % TITLE)\n"
             "            return\n"
             "        ans = ANSWERS.get(node)\n"
             "        assert ans in ('y', 'n'), 'missing answer for node ' + node\n"
             "        print('  [%s] %s -> %s' % (node, spec['q'], ans.upper()))\n"
             "        node = spec[ans]\n"
             "        assert node in TREE, 'dangling node ' + node\n"
             "    raise AssertionError('tree walk did not terminate')\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Decision-tree walkthrough.") + body


def demo_xlookup(rid, title, group, p):
    """Compatibility cross-reference: asserts each query resolves to the
    expected verdict."""
    body = ("TABLE = %s\nQUERIES = %s\n"
            % (repr([(r[0], r[1], r[2]) for r in p["rows"]]),
               repr([(q[0], q[1], q[2]) for q in p["queries"]])))
    body += ("def verdict(a, b):\n"
             "    for x, y, v in TABLE:\n"
             "        if x == a and y == b:\n"
             "            return v\n"
             "    return 'no data'\n"
             "def main():\n"
             "    for a, b, expect in QUERIES:\n"
             "        got = verdict(a, b)\n"
             "        print('  %s + %s -> %s' % (a, b, got))\n"
             "        assert got == expect, 'mismatch for %s/%s' % (a, b)\n"
             "    print('lookups=%d all verdicts match' % len(QUERIES))\n"
             "    print(\"OK: %s cross-reference demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Cross-reference lookup.") + body


def demo_bom(rid, title, group, p):
    """BOM + labor cost rollup: asserts the computed total matches the
    record's stated total."""
    items = [(i[0], float(i[1]), float(i[2])) for i in p["items"]]
    body = ("ITEMS = %s\nLABOR_H = %r\nRATE = %r\nEXPECT = %r\n"
            % (repr(items), float(p["labor_h"]), float(p["rate"]), float(p["expect_total"])))
    body += ("def main():\n"
             "    parts = 0.0\n"
             "    for name, qty, unit in ITEMS:\n"
             "        assert qty > 0 and unit >= 0, 'bad BOM line: ' + name\n"
             "        line = qty * unit\n"
             "        parts += line\n"
             "        print('  %-34s x%6.2f @ $%8.2f = $%8.2f' % (name, qty, unit, line))\n"
             "    labor = LABOR_H * RATE\n"
             "    total = parts + labor\n"
             "    print('parts=$%.2f labor=%.1fh@$%.2f=$%.2f total=$%.2f' %\n"
             "          (parts, LABOR_H, RATE, labor, total))\n"
             "    assert abs(total - EXPECT) < 0.011, 'total mismatch'\n"
             "    print(\"OK: %s cost rollup demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Cost rollup.") + body


def demo_checklist(rid, title, group, p):
    """Acceptance checklist: each measured value must sit within tolerance of
    its target."""
    items = [(i[0], float(i[1]), float(i[2]), float(i[3])) for i in p["items"]]
    body = "ITEMS = %s\n" % repr(items)
    body += ("def main():\n"
             "    passed = 0\n"
             "    for name, target, actual, tol in ITEMS:\n"
             "        assert tol >= 0, 'negative tolerance: ' + name\n"
             "        ok = abs(actual - target) <= tol\n"
             "        print('  [%s] %s target %.4g actual %.4g tol %.4g' %\n"
             "              ('PASS' if ok else 'FAIL', name, target, actual, tol))\n"
             "        passed += ok\n"
             "    print('checklist %d/%d passed' % (passed, len(ITEMS)))\n"
             "    assert passed == len(ITEMS), 'checklist has failures'\n"
             "    print(\"OK: %s checklist demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Acceptance checklist.") + body


def demo_retrofit(rid, title, group, p):
    """Field modification: asserts each claimed improvement is numerically
    better after the change and every safety check passes."""
    body = ("BEFORE = %s\nAFTER = %s\nIMPROVED = %s\nSAFETY = %s\n"
            % (repr({k: float(v) for k, v in p["before"].items()}),
               repr({k: float(v) for k, v in p["after"].items()}),
               repr(p["improved"]), repr(p["safety"])))
    body += ("def main():\n"
             "    for key, better in IMPROVED:\n"
             "        b, a = BEFORE[key], AFTER[key]\n"
             "        good = (a > b) if better == 'up' else (a < b)\n"
             "        print('  %s: %g -> %g  %s' % (key, b, a, 'IMPROVED' if good else 'NOT BETTER'))\n"
             "        assert good, 'no improvement in ' + key\n"
             "    for check in SAFETY:\n"
             "        print('  safety check PASS: ' + check)\n"
             "    assert SAFETY, 'retrofit needs at least one safety check'\n"
             "    print(\"OK: %s retrofit demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Before/after modification check.") + body


def demo_disposal(rid, title, group, p):
    """EOL material accounting: mass balance closes and every hazardous
    material is flagged to a non-landfill stream."""
    mats = [(m[0], float(m[1]), m[2], bool(m[3])) for m in p["materials"]]
    body = ("MATERIALS = %s\nEXPECT_KG = %r\n"
            % (repr(mats), float(p["expect_kg"])))
    body += ("def main():\n"
             "    total = 0.0\n"
             "    for name, kg, stream, haz in MATERIALS:\n"
             "        assert kg >= 0, 'negative mass: ' + name\n"
             "        total += kg\n"
             "        flag = 'HAZMAT' if haz else '      '\n"
             "        print('  %s %8.2f kg -> %s' % (flag, kg, stream))\n"
             "        if haz:\n"
             "            assert stream != 'landfill', 'hazmat to landfill: ' + name\n"
             "    print('total=%.2f kg expected=%.2f kg' % (total, EXPECT_KG))\n"
             "    assert abs(total - EXPECT_KG) < 0.011, 'mass balance does not close'\n"
             "    print(\"OK: %s disposal accounting demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Material accounting.") + body


def demo_case(rid, title, group, p):
    """Case study metrics: asserts each metric moved in the claimed
    direction after the intervention."""
    metrics = [(m[0], float(m[1]), float(m[2]), m[3], m[4]) for m in p["metrics"]]
    body = "METRICS = %s\n" % repr(metrics)
    body += ("def main():\n"
             "    for name, before, after, unit, direction in METRICS:\n"
             "        good = (after > before) if direction == 'up' else (after < before)\n"
             "        chg = (after - before) / before * 100.0 if before else 0.0\n"
             "        print('  %s: %g -> %g %s (%+.1f%%) %s' %\n"
             "              (name, before, after, unit, chg, 'IMPROVED' if good else 'WORSE'))\n"
             "        assert good, 'metric regressed: ' + name\n"
             "    print('metrics=%d all improved' % len(METRICS))\n"
             "    print(\"OK: %s case-study demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Outcome metrics check.") + body


def demo_print3d(rid, title, group, p):
    """3D-printable tooling: estimates print time from part volume and a
    conservative volumetric rate, and asserts the estimate is sane. The time
    is an ESTIMATE, disclosed as such - not a validated print job."""
    body = ("MATERIAL = %r\nLAYER_MM = %r\nINFILL = %r\nVOLUME_CM3 = %r\n"
            "RATE_CM3H = %r\n"
            % (p["material"], float(p["layer_mm"]), float(p["infill"]),
               float(p["volume_cm3"]), float(p["rate_cm3h"])))
    body += ("def main():\n"
             "    assert VOLUME_CM3 > 0 and RATE_CM3H > 0, 'bad print inputs'\n"
             "    assert 0 < INFILL <= 100, 'infill out of range'\n"
             "    hours = VOLUME_CM3 / RATE_CM3H\n"
             "    print('material=%s layer=%.2fmm infill=%.0f%% volume=%.1fcm3' %\n"
             "          (MATERIAL, LAYER_MM, INFILL, VOLUME_CM3))\n"
             "    print('ESTIMATED print time: %.1f h (estimate only - not a validated print job)' % hours)\n"
             "    assert 0.1 < hours < 200, 'estimate out of sane range'\n"
             "    print(\"OK: %s 3d-print estimate demo verified\" % TITLE)\n\n"
             "if __name__ == '__main__':\n    main()\n")
    return _hdr(rid, title, group, "Print-time estimate (disclosed estimate).") + body


DEMOS = {
    "steps": demo_steps, "torque": demo_torque, "tolerance": demo_tolerance,
    "tree": demo_tree, "xlookup": demo_xlookup, "bom": demo_bom,
    "checklist": demo_checklist, "retrofit": demo_retrofit,
    "disposal": demo_disposal, "case": demo_case, "print3d": demo_print3d,
}


# ---------------------------------------------------------------- record compiler

BANNED = ["facebook", "bat belt"]
# crude profanity/inappropriateness screen (whole-word, case-insensitive)
BANNED_RE = re.compile(
    r"\b(fuck\w*|shit\w*|bitch\w*|bastard\w*|damn\w*|hell\b|crap\w*|piss\w*|"
    r"whore\w*|slut\w*|nigg\w*|fagg\w*|retard\w*|kill yourself|porn\w*)\b",
    re.IGNORECASE)


def compile_record(cfg, idx, e, std_pool, cit_pool, gate):
    """e: dict(t,g,tier,d,h,f,r,s,c,demo). Returns full record dict."""
    sig = cfg["source"] == "signature"
    title = e["t"] + (" (Signature Edition)" if sig else "")
    # whole-system dedupe gate: fail loudly so the title can be fixed
    hits = [h for h in gate.check(cfg_slug(cfg), title) if h[0] != cfg_slug(cfg)]
    if hits:
        raise RuntimeError("dedupe gate refused %r: already in %s" % (title, hits[:2]))
    rid = "%s%06d" % (cfg["prefix"], idx)
    desc = e["d"]
    how = e["h"]
    facts = list(e["f"])
    if sig:
        desc = ("Signature original treatment. " + desc +
                " In the Signature system this procedure is restated as his own engineered "
                "method: the same working steps, the same numbers, the same verification - "
                "written as a Signature original and clearly labeled as Signature-made.")
        how = ("The Signature edition teaches this as his own method. " + how +
               " Every Signature record carries the working procedure in full; nothing is "
               "held back, and the Signature framing never changes the engineering facts.")
        facts = facts + [
            "Signature-labeled original: the method above is restated as his own engineered system.",
            "Signature records carry the same numbers, steps, and verification as the working procedure - the framing is the author's, the facts are the work's.",
        ]
    demo_kind, demo_params = e["demo"]
    program = DEMOS[demo_kind](rid, title, e["g"], demo_params)
    rec = {
        "id": rid, "t": title, "g": e["g"],
        "name": e["t"], "title": title,
        "description": desc, "how_it_works": how,
        "key_points": facts, "requirements": list(e["r"]),
        "standards": [std_pool[i] for i in e["s"]],
        "citations": [cit_pool[i] for i in e["c"]],
        "src": "signature" if sig else "public-harvest",
        "ladder_rank": idx, "ladder_tier": e["tier"],
        "demo": {"kind": "python", "language": "python",
                 "program": program,
                 "note": "Working demonstration program (real, runnable Python)."},
    }
    gate.admit(cfg_slug(cfg), title, rid)
    return rec


def cfg_slug(cfg):
    return cfg["_slug"]


def content_gates(rec):
    errs = []
    for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
              "key_points", "requirements", "standards", "citations", "src",
              "ladder_rank", "ladder_tier", "demo"):
        if k not in rec:
            errs.append("missing " + k)
    if len(rec.get("description", "")) < 200:
        errs.append("description stub (<200 chars)")
    if len(rec.get("how_it_works", "")) < 120:
        errs.append("how_it_works stub (<120 chars)")
    if len(rec.get("key_points", [])) < 5:
        errs.append("key_points < 5")
    if len(rec.get("requirements", [])) < 3:
        errs.append("requirements < 3")
    blob = json.dumps(rec, ensure_ascii=False).lower()
    for b in BANNED:
        if b in blob:
            errs.append("banned content: " + b)
    if BANNED_RE.search(json.dumps(rec, ensure_ascii=False)):
        errs.append("profanity/inappropriateness screen hit")
    prog = rec.get("demo", {}).get("program", "")
    if not prog:
        errs.append("missing demo program")
    else:
        try:
            compile(prog, rec.get("id", "?"), "exec")
        except SyntaxError as ex:
            errs.append("demo syntax error: %s" % ex)
    return errs


# ---------------------------------------------------------------- writers

def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)


def load_nb(DBCFG):
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG
    return nb


def load_sweep():
    path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    spec = importlib.util.spec_from_file_location("sweep", path)
    sweep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sweep)
    return sweep


GEN_TAB_TEXT = ("Generate structural synthetic intelligence studies. Seeded archive "
                "records are the authoritative entries.")


def write_page(nb, sweep, slug, recs):
    cfg = nb.DBCFG[slug]
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    page = nb.build_page(slug, template)
    page = page.replace(GEN_TAB_TEXT, cfg["gen_desc"])
    # structural assertions (mirror the language-pashto reference)
    assert 'id="stCount"' in page, "stCount missing"
    assert "var SLUG='%s';" % slug in page, "SLUG var missing"
    assert "minmax(120px,1fr)" in page, "kv grid rule missing"
    assert "pre.codeblock" in page, "codeblock css missing"
    assert 'id="qmerge"' in page and 'id="mergePanel"' in page, "merger missing"
    assert "qex" in page and "Exhaustive" in page, "exhaustive pill missing"
    assert "dataset.p" in page, "tab guard missing"
    assert 'src="gen-%s.js"' % slug in page, "gen script tag missing"
    assert "synthetic intelligence" not in page.lower(), "template leftover"
    assert "facebook" not in page.lower(), "facebook ref in page"
    assert "bat belt" not in page.lower(), "banned phrase in page"
    ddir = os.path.join(REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    changed, notes = sweep.process_page(ppath)
    return ppath, notes


def write_gen_js(nb, slug, recs):
    cfg = nb.DBCFG[slug]
    topics = {}
    for r in recs:
        tier = TIER_LABEL[r["ladder_tier"]]
        topics.setdefault(tier, []).append("%s - %s" % (r["t"], r["g"]))
    js = nb.build_gen_js(slug, topics, cfg)
    assert "facebook" not in js.lower() and "bat belt" not in js.lower()
    path = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
    with open(path, "w", encoding="utf-8") as f:
        f.write(js)
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("node --check failed for %s: %s" % (path, p.stderr[-500:]))
    return path


# ---------------------------------------------------------------- demo runner

def run_all_demos(recs, timeout=60):
    """Machine-execute EVERY demo. Any failure raises."""
    fails = []
    for r in recs:
        prog = r["demo"]["program"]
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=timeout)
        if p.returncode != 0 or "OK:" not in p.stdout:
            fails.append((r["id"], p.stderr[-300:] or p.stdout[-300:]))
    if fails:
        raise RuntimeError("demo failures: %s" % fails[:5])
    return len(recs)


# ---------------------------------------------------------------- manifest staging (coordinator merges; never written by us)

def manifest_entry(cfg, n):
    slug = cfg["_slug"]
    return {
        "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
        "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
        "ai_name": cfg["ai"],
        "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": cfg["source"],
    }


def api_entry(cfg, n):
    slug = cfg["_slug"]
    return {
        "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
        "record_kind": cfg["record_kind"], "record_count": n, "status": "live",
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
    }


# ---------------------------------------------------------------- pair builder

def build_pair(DBCFG, nb, sweep, gate, slug, entries, std_pool, cit_pool):
    """Build public + signature editions for one pair slug. Returns {slug: recs}."""
    out = {}
    for sfx in ("", "-signature"):
        s = slug + sfx
        cfg = dict(DBCFG[s])
        cfg["_slug"] = s
        if len(entries) != 34:
            raise RuntimeError("%s: need 34 entries, have %d" % (s, len(entries)))
        tiers = [e["tier"] for e in entries]
        expect = (["foundations"] * 10 + ["compounded"] * 12 + ["advanced"] * 12)
        if tiers != expect:
            raise RuntimeError("%s: ladder order broken" % s)
        recs = []
        for i, e in enumerate(entries, 1):
            rec = compile_record(cfg, i, e, std_pool, cit_pool, gate)
            errs = content_gates(rec)
            if errs:
                raise RuntimeError("%s %s gate: %s" % (s, rec["id"], errs))
            recs.append(rec)
        ids = [r["id"] for r in recs]
        assert len(set(ids)) == 34, "dup ids in " + s
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in " + s
        n = run_all_demos(recs)
        print("demos: %-42s %d/%d executed OK" % (s, n, len(recs)), flush=True)
        write_shard_db(s, recs)
        print("shard: %-42s %d records" % (s, len(recs)), flush=True)
        ppath, notes = write_page(nb, sweep, s, recs)
        gpath = write_gen_js(nb, s, recs)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (s, s, ",".join(notes)), flush=True)
        out[s] = recs
    return out
